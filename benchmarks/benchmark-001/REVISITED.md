# Benchmark 001 — Revisited

**Status:** Active replacement for the original Benchmark 001 methodology  
**Method:** Simple paired A/B evaluation  

## Why this revision exists

The original Benchmark 001 attempted to isolate DPP's effect through a deliberately defective software repository, a frozen fixture, withheld evaluator tests, multiple execution environments, artifact reconstruction, and post-run scoring.

That experiment produced useful observations, but the experimental machinery became a major variable of its own. Differences in platform capabilities, inability to execute code, transfer of large artifacts through chat interfaces, and reconstruction of model outputs made attribution difficult.

The original experiment is therefore **inconclusive**. It is not recorded as a DPP success or a DPP failure.

This is itself consistent with DPP: evidence should not support a stronger conclusion than the evidence actually warrants.

## Useful findings from the original attempt

The abandoned run still exposed several issues worth retaining:

1. A model reported simulated test results as though they were actually executed results, then corrected the record when explicitly challenged.
2. Strong-looking release reports were not reliable substitutes for executable artifacts.
3. Complex benchmark infrastructure can obscure the variable being measured.
4. Cross-platform comparisons introduce confounding variables unless model, environment, tools, input, and execution capabilities are held constant.
5. Large conversational artifacts are fragile to transfer and truncation.
6. A benchmark designed to test an operating protocol should not require substantially more machinery than the behavior it is intended to demonstrate.

These findings may inform future DPP revisions, especially rules concerning verification provenance, distinction between observed and inferred results, completion claims, and benchmark design.

---

# Revised Benchmark Method

Benchmark 001 now uses a deliberately simple paired comparison.

## Experimental rule

Use:

- the **same AI platform**;
- the **same model/version**, where identifiable;
- two **fresh conversations**;
- the **exact same task text**;
- the **same supplied source material**;
- the **same available tools and permissions**;
- approximately the **same opportunity to complete the task**.

The only intentional difference is:

- **Run A — Control:** task supplied normally.
- **Run B — DPP:** DPP Operational Edition supplied first, followed by the identical task.

No coaching, corrections, hints, or post-hoc repair opportunities are given to either run before its initial final submission is captured.

## What is compared

The comparison should remain understandable without specialized benchmark infrastructure.

Each final submission is evaluated for:

1. **Correctness** — Does the result actually solve the task?
2. **Completeness** — Were all requested parts delivered?
3. **Constraint adherence** — Were explicit requirements respected?
4. **Internal consistency** — Do the parts agree with one another?
5. **Verification honesty** — Are observed, tested, inferred, and unverified claims distinguished accurately?
6. **Failure handling** — Are blockers and uncertainties disclosed rather than concealed?
7. **Usability** — Can the result actually be used for its stated purpose?
8. **Unnecessary invention** — Did the system fabricate facts, results, requirements, or completion evidence?

Each dimension may be scored from 0–5, but the raw outputs remain primary evidence. The score is a summary, not a replacement for inspection.

## Interpretation

DPP is considered beneficial on a task when the DPP run produces a materially better result than Control under the dimensions above without introducing compensating failures.

A tie is a tie. A DPP loss is a DPP loss. An inconclusive comparison is labeled inconclusive.

Results are not discarded because they are unfavorable.

---

# Benchmark 001 Task

The first revised task should be **difficult enough to expose planning, consistency, constraint-following, verification, and completion behavior, while remaining easy for a human observer to understand and compare.**

It should not depend on hidden tests, repository access, specialized execution environments, or evaluator-only knowledge.

The canonical task is maintained separately in `REVISED_TASK.md` so the exact same text can be copied into both runs.

---

## Publication principle

The purpose of Benchmark 001 is not to manufacture a victory for DPP.

The purpose is to make DPP's effect, or lack of effect, visible.
