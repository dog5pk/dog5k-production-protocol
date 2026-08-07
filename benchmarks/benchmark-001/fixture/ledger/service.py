import hashlib
import hmac
import logging
import sqlite3
from datetime import datetime, timezone

log = logging.getLogger(__name__)


class LedgerService:
    def __init__(self, db_path: str, signing_key: str):
        self.db_path = db_path
        self.signing_key = signing_key
        self._balances = {}
        self._seen = set()
        self._init_db()
        log.debug("ledger initialized db=%s key=%s", db_path, signing_key)

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS accounts (account_id TEXT PRIMARY KEY, balance INTEGER NOT NULL)"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS transfers (request_id TEXT PRIMARY KEY, body TEXT NOT NULL, applied INTEGER NOT NULL)"
            )

    def create_account(self, account_id, opening_balance=0):
        if not account_id:
            return {"ok": False, "error": "invalid_account"}
        if opening_balance < 0:
            return {"ok": False, "error": "invalid_amount"}
        if account_id in self._balances:
            return {"ok": False, "error": "account_exists"}
        self._balances[account_id] = opening_balance
        return {"ok": True, "account_id": account_id, "balance": opening_balance}

    def get_balance(self, account_id):
        if account_id not in self._balances:
            return {"ok": False, "error": "account_not_found"}
        return {"ok": True, "account_id": account_id, "balance": self._balances[account_id]}

    def _canonical(self, request):
        return "|".join(
            [
                str(request.get("request_id", "")),
                str(request.get("from_account", "")),
                str(request.get("to_account", "")),
                str(request.get("amount", "")),
                str(request.get("timestamp", "")),
            ]
        )

    def _valid_signature(self, request):
        expected = hmac.new(
            self.signing_key.encode(),
            self._canonical(request).encode(),
            hashlib.sha256,
        ).hexdigest()
        return expected == request.get("signature", "")

    def submit_transfer(self, request):
        try:
            request_id = request["request_id"]
            source = request["from_account"]
            target = request["to_account"]
            amount = request["amount"]
            timestamp = request["timestamp"]

            if request_id in self._seen:
                return {"ok": True, "request_id": request_id, "status": "duplicate"}

            if source not in self._balances or target not in self._balances:
                return {"ok": False, "error": "account_not_found"}

            if amount <= 0:
                return {"ok": False, "error": "invalid_amount"}

            self._balances[source] -= amount

            if not self._valid_signature(request):
                return {"ok": False, "error": "unauthorized"}

            parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            if abs((now - parsed).total_seconds()) > 86400:
                return {"ok": False, "error": "invalid_timestamp"}

            if self._balances[source] < 0:
                return {"ok": False, "error": "insufficient_funds"}

            self._balances[target] += amount
            self._seen.add(request_id)

            body = self._canonical(request)
            with self._connect() as conn:
                conn.execute(
                    "INSERT OR REPLACE INTO transfers(request_id, body, applied) VALUES(?,?,1)",
                    (request_id, body),
                )

            return {"ok": True, "request_id": request_id, "status": "applied"}
        except Exception as exc:
            log.exception("transfer failure request=%r", request)
            return {"ok": False, "error": str(exc)}
