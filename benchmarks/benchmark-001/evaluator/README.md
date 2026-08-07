# Benchmark 001 Evaluator

This directory is **not provided to either benchmark run**. Control and DPP runs begin from the frozen `benchmark-001-fixture` branch and receive only the fixture, task contract, and identical execution conditions.

The evaluator is applied after each submitted result.

Its purpose is not to reward a particular implementation strategy. It tests externally visible contract behavior, state invariants, security properties, persistence, concurrency behavior, and completion honesty.

The evaluator and seeded-defect map are published for transparency after the fixture has been frozen so that the benchmark can be independently audited and reproduced. A run that inspects this directory before completing the task is invalid.
