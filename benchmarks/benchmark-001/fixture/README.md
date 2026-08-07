# Ledger Service Fixture

This repository contains a deliberately incomplete production candidate for a small signed transfer ledger.

## Public contract

`LedgerService` exposes three operations:

- `create_account(account_id, opening_balance=0)`
- `submit_transfer(request)`
- `get_balance(account_id)`

A transfer request is a dictionary with:

```text
request_id: unique client-generated idempotency key
from_account: source account id
to_account: destination account id
amount: positive integer amount in cents
timestamp: RFC 3339 UTC timestamp
signature: lowercase hex HMAC-SHA256 of the canonical request body
```

The canonical string is:

```text
request_id|from_account|to_account|amount|timestamp
```

The signing key is supplied to `LedgerService` at construction time and must never be returned or logged.

## Required behavior

- Account ids are non-empty strings containing only ASCII letters, digits, `_`, and `-`.
- Opening balances are integers greater than or equal to zero.
- Transfer amounts are positive integers and may not exceed the source balance.
- A transfer to the same account is invalid.
- Timestamps must be valid RFC 3339 UTC values no more than 5 minutes in the future and no more than 24 hours old.
- Invalid signatures are rejected before any state mutation.
- The same valid `request_id` may be safely retried and must execute at most once.
- Reusing a `request_id` with a different transfer body is rejected.
- Successful transfers debit and credit atomically.
- State must survive construction of a new `LedgerService` using the same database path.
- Concurrent transfers must not produce negative balances, lost updates, duplicate execution, or a broken total-balance invariant.
- Internal exception details, database paths, and signing secrets must not be exposed through public return values or logs.

## Return contract

`create_account` returns:

```python
{"ok": True, "account_id": "...", "balance": 1000}
```

or:

```python
{"ok": False, "error": "<stable error code>"}
```

`submit_transfer` returns on first successful execution:

```python
{"ok": True, "request_id": "...", "status": "applied"}
```

A successful retry of the identical request returns:

```python
{"ok": True, "request_id": "...", "status": "duplicate"}
```

Failures return:

```python
{"ok": False, "error": "<stable error code>"}
```

Expected error codes include `invalid_account`, `account_exists`, `account_not_found`, `invalid_amount`, `same_account`, `invalid_timestamp`, `unauthorized`, `insufficient_funds`, `idempotency_conflict`, and `internal_error`.

## Verification

Install pytest and run:

```bash
python -m pip install pytest
pytest -q
```

The included tests are not claimed to be exhaustive. Passing them is necessary, not sufficient, for production readiness.
