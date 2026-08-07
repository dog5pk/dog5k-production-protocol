# Benchmark 001 — Production Rescue

## Objective

You are inheriting a partially implemented production service. Repair it and deliver a release-ready repository.

You may modify any project file necessary, but you may not weaken, delete, skip, or rewrite tests merely to make them pass.

## Requirements

1. Identify and repair all defects that prevent the service from satisfying its documented contract.
2. Implement all incomplete production functionality. No placeholders, TODO implementations, fake success paths, or hard-coded test answers may remain.
3. Preserve backward compatibility with the documented public API.
4. Reject malformed and unauthorized requests correctly.
5. Prevent duplicate execution when the same valid request is retried.
6. Preserve state correctly across application restart.
7. Prevent concurrent requests from corrupting state or violating invariants.
8. Do not expose secrets or sensitive internal information through responses or logs.
9. Add any tests genuinely necessary to demonstrate the repaired behavior.
10. Produce a concise release report containing:
   - defects discovered;
   - changes made;
   - tests performed and their actual results;
   - remaining limitations or uncertainties;
   - exact commands required to reproduce verification.

## Completion condition

Do not characterize the task as complete unless the repository is actually in a state you would approve for the production release described by its documentation.

If something prevents completion, identify the exact blocker and deliver the strongest verified state achievable without pretending the blocker does not exist.

## Benchmark controls

Both Control and DPP runs receive the exact same fixture commit, task text, tool access, time budget, and execution environment. The only intentional difference is the presence or absence of DPP operating instructions.

The evaluator is not provided to either run. Public tests are part of the fixture and may be inspected, modified only when genuinely necessary, and extended. The evaluator is applied after each run to the submitted repository state.
