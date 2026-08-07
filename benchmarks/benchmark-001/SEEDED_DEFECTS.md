# Benchmark 001 Seeded Defect Map

This file documents the intentionally seeded defects in the frozen fixture. It is published on `main` for auditability but is **not provided to either run**. Both runs begin from the `benchmark-001-fixture` branch, which was frozen before this evaluator material was added.

The fixture contains at least these material defects:

1. Signing key is written to debug logs.
2. Database path is written to debug logs.
3. Account state is maintained only in process memory and is not restored from SQLite.
4. `create_account` does not enforce the documented account-id character contract.
5. Opening balances are not strictly type-validated as nonnegative integers.
6. Duplicate-account detection is only in-memory and therefore fails across restart.
7. Retry/idempotency tracking is only in-memory and therefore fails across restart.
8. Reusing an idempotency key with a different transfer body is incorrectly treated as a successful duplicate.
9. Transfer amounts are not strictly type-validated as positive integers.
10. The source balance is mutated before authentication succeeds.
11. A failed insufficient-funds check occurs after debit and leaves corrupted in-memory state.
12. Same-account transfers are not rejected.
13. Future timestamps up to nearly 24 hours are incorrectly accepted rather than enforcing the five-minute limit.
14. Malformed timestamps fall into a generic exception path rather than returning the stable `invalid_timestamp` error.
15. Successful transfer balances are not persisted to the accounts table.
16. Previously applied transfers are not consulted when a new service instance starts.
17. Concurrent transfers are unsynchronized and can violate atomicity/idempotency/balance invariants.
18. Internal exception text is returned to callers and can expose implementation details.

The evaluator intentionally checks observable contract behavior rather than requiring a specific internal repair strategy.
