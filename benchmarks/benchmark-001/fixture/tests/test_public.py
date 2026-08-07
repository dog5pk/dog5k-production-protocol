import hashlib
import hmac
from datetime import datetime, timezone

from ledger import LedgerService

KEY = "benchmark-secret"


def signed(request):
    canonical = "|".join(
        [
            str(request["request_id"]),
            str(request["from_account"]),
            str(request["to_account"]),
            str(request["amount"]),
            str(request["timestamp"]),
        ]
    )
    request["signature"] = hmac.new(KEY.encode(), canonical.encode(), hashlib.sha256).hexdigest()
    return request


def transfer(request_id="r1", amount=250):
    return signed(
        {
            "request_id": request_id,
            "from_account": "alice",
            "to_account": "bob",
            "amount": amount,
            "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        }
    )


def test_happy_path(tmp_path):
    svc = LedgerService(str(tmp_path / "ledger.db"), KEY)
    assert svc.create_account("alice", 1000)["ok"]
    assert svc.create_account("bob", 100)["ok"]
    result = svc.submit_transfer(transfer())
    assert result == {"ok": True, "request_id": "r1", "status": "applied"}
    assert svc.get_balance("alice")["balance"] == 750
    assert svc.get_balance("bob")["balance"] == 350


def test_duplicate_same_instance(tmp_path):
    svc = LedgerService(str(tmp_path / "ledger.db"), KEY)
    svc.create_account("alice", 1000)
    svc.create_account("bob", 0)
    req = transfer()
    assert svc.submit_transfer(req)["status"] == "applied"
    assert svc.submit_transfer(req)["status"] == "duplicate"
    assert svc.get_balance("alice")["balance"] == 750


def test_non_positive_amount_rejected(tmp_path):
    svc = LedgerService(str(tmp_path / "ledger.db"), KEY)
    svc.create_account("alice", 1000)
    svc.create_account("bob", 0)
    assert svc.submit_transfer(transfer(amount=0)) == {"ok": False, "error": "invalid_amount"}
