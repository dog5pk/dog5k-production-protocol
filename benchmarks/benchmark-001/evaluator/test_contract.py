import hashlib
import hmac
import logging
import sys
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

FIXTURE = Path(__file__).resolve().parents[1] / "fixture"
sys.path.insert(0, str(FIXTURE))

from ledger import LedgerService  # noqa: E402

KEY = "benchmark-secret"


def ts(offset_seconds=0):
    return (datetime.now(timezone.utc) + timedelta(seconds=offset_seconds)).isoformat().replace("+00:00", "Z")


def sign(req, key=KEY):
    canonical = "|".join(
        [
            str(req.get("request_id", "")),
            str(req.get("from_account", "")),
            str(req.get("to_account", "")),
            str(req.get("amount", "")),
            str(req.get("timestamp", "")),
        ]
    )
    out = dict(req)
    out["signature"] = hmac.new(key.encode(), canonical.encode(), hashlib.sha256).hexdigest()
    return out


def req(rid="r1", source="alice", target="bob", amount=100, when=None):
    return sign(
        {
            "request_id": rid,
            "from_account": source,
            "to_account": target,
            "amount": amount,
            "timestamp": when or ts(),
        }
    )


def seeded(tmp_path, alice=1000, bob=0):
    svc = LedgerService(str(tmp_path / "ledger.db"), KEY)
    assert svc.create_account("alice", alice)["ok"]
    assert svc.create_account("bob", bob)["ok"]
    return svc


def balances(svc):
    return svc.get_balance("alice")["balance"], svc.get_balance("bob")["balance"]


@pytest.mark.parametrize("bad", ["", "a b", "a/b", "é", None, 123])
def test_invalid_account_ids_rejected(tmp_path, bad):
    svc = LedgerService(str(tmp_path / "ledger.db"), KEY)
    result = svc.create_account(bad, 0)
    assert result == {"ok": False, "error": "invalid_account"}


def test_opening_balance_requires_nonnegative_integer(tmp_path):
    svc = LedgerService(str(tmp_path / "ledger.db"), KEY)
    for bad in (-1, 1.5, "10", True):
        assert svc.create_account(f"a{str(bad).replace('.', '_')}", bad) == {"ok": False, "error": "invalid_amount"}


def test_account_persists_and_duplicate_account_survives_restart(tmp_path):
    path = str(tmp_path / "ledger.db")
    svc = LedgerService(path, KEY)
    assert svc.create_account("alice", 700)["ok"]
    svc2 = LedgerService(path, KEY)
    assert svc2.get_balance("alice") == {"ok": True, "account_id": "alice", "balance": 700}
    assert svc2.create_account("alice", 1) == {"ok": False, "error": "account_exists"}


def test_unauthorized_transfer_never_mutates_state(tmp_path):
    svc = seeded(tmp_path)
    bad = req()
    bad["signature"] = "00" * 32
    before = balances(svc)
    assert svc.submit_transfer(bad) == {"ok": False, "error": "unauthorized"}
    assert balances(svc) == before


def test_same_account_rejected_without_mutation(tmp_path):
    svc = seeded(tmp_path)
    transfer = req(source="alice", target="alice")
    before = balances(svc)
    assert svc.submit_transfer(transfer) == {"ok": False, "error": "same_account"}
    assert balances(svc) == before


@pytest.mark.parametrize("amount", [0, -1, 1.5, "1", True, None])
def test_invalid_transfer_amounts_rejected_without_mutation(tmp_path, amount):
    svc = seeded(tmp_path)
    transfer = req(amount=amount)
    before = balances(svc)
    assert svc.submit_transfer(transfer) == {"ok": False, "error": "invalid_amount"}
    assert balances(svc) == before


def test_insufficient_funds_does_not_debit(tmp_path):
    svc = seeded(tmp_path, alice=50)
    before = balances(svc)
    assert svc.submit_transfer(req(amount=51)) == {"ok": False, "error": "insufficient_funds"}
    assert balances(svc) == before


def test_timestamp_too_old_rejected_without_mutation(tmp_path):
    svc = seeded(tmp_path)
    before = balances(svc)
    result = svc.submit_transfer(req(when=ts(-(24 * 3600 + 5))))
    assert result == {"ok": False, "error": "invalid_timestamp"}
    assert balances(svc) == before


def test_timestamp_more_than_five_minutes_future_rejected(tmp_path):
    svc = seeded(tmp_path)
    before = balances(svc)
    result = svc.submit_transfer(req(when=ts(301)))
    assert result == {"ok": False, "error": "invalid_timestamp"}
    assert balances(svc) == before


def test_malformed_timestamp_returns_stable_error_and_no_details(tmp_path):
    svc = seeded(tmp_path)
    result = svc.submit_transfer(req(when="not-a-date"))
    assert result == {"ok": False, "error": "invalid_timestamp"}


def test_identical_retry_is_idempotent_across_restart(tmp_path):
    path = str(tmp_path / "ledger.db")
    svc = LedgerService(path, KEY)
    svc.create_account("alice", 1000)
    svc.create_account("bob", 0)
    transfer = req(rid="persist-retry", amount=125)
    assert svc.submit_transfer(transfer)["status"] == "applied"
    assert balances(svc) == (875, 125)
    svc2 = LedgerService(path, KEY)
    assert svc2.submit_transfer(transfer) == {"ok": True, "request_id": "persist-retry", "status": "duplicate"}
    assert balances(svc2) == (875, 125)


def test_idempotency_key_reuse_with_changed_body_rejected(tmp_path):
    svc = seeded(tmp_path)
    first = req(rid="same-key", amount=100)
    second = req(rid="same-key", amount=101)
    assert svc.submit_transfer(first)["status"] == "applied"
    assert svc.submit_transfer(second) == {"ok": False, "error": "idempotency_conflict"}
    assert balances(svc) == (900, 100)


def test_total_balance_preserved_across_restart(tmp_path):
    path = str(tmp_path / "ledger.db")
    svc = LedgerService(path, KEY)
    svc.create_account("alice", 1000)
    svc.create_account("bob", 500)
    assert svc.submit_transfer(req(amount=275))["ok"]
    svc2 = LedgerService(path, KEY)
    a, b = balances(svc2)
    assert a + b == 1500
    assert (a, b) == (725, 775)


def test_concurrent_unique_transfers_never_overdraw_or_create_money(tmp_path):
    svc = seeded(tmp_path, alice=1000, bob=0)
    results = []
    lock = threading.Lock()

    def worker(i):
        r = svc.submit_transfer(req(rid=f"c{i}", amount=100))
        with lock:
            results.append(r)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    a, b = balances(svc)
    assert a >= 0
    assert b >= 0
    assert a + b == 1000
    assert sum(1 for r in results if r.get("ok")) == 10


def test_concurrent_same_request_executes_at_most_once(tmp_path):
    svc = seeded(tmp_path, alice=1000, bob=0)
    transfer = req(rid="same-concurrent", amount=250)
    results = []
    lock = threading.Lock()

    def worker():
        r = svc.submit_transfer(dict(transfer))
        with lock:
            results.append(r)

    threads = [threading.Thread(target=worker) for _ in range(12)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert balances(svc) == (750, 250)
    assert sum(1 for r in results if r.get("status") == "applied") == 1
    assert all(r.get("status") in {"applied", "duplicate"} for r in results)


def test_secret_and_db_path_not_logged(caplog, tmp_path):
    db_path = str(tmp_path / "very-secret-path.db")
    caplog.set_level(logging.DEBUG)
    svc = LedgerService(db_path, KEY)
    svc.create_account("alice", 100)
    svc.create_account("bob", 0)
    bad = req()
    bad["signature"] = "invalid"
    svc.submit_transfer(bad)
    rendered = caplog.text
    assert KEY not in rendered
    assert db_path not in rendered


def test_internal_exception_details_never_escape(tmp_path):
    svc = seeded(tmp_path)
    result = svc.submit_transfer({"request_id": "broken"})
    assert result.get("ok") is False
    assert result.get("error") in {
        "invalid_account",
        "invalid_amount",
        "invalid_timestamp",
        "unauthorized",
        "account_not_found",
        "internal_error",
    }
    assert "KeyError" not in str(result)
    assert "from_account" not in str(result)
