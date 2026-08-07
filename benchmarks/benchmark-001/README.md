# Benchmark 001 — Production Rescue

**Status:** Fixture frozen; evaluator frozen; ready for paired runs.

Benchmark 001 is DPP's first controlled software-production experiment. It tests whether DPP changes how an AI system repairs and characterizes a realistic defective service under a fixed contract.

## Frozen fixture

- Branch: `benchmark-001-fixture`
- Freeze commit: `273946d976c624e4769727d01b719a9f70949b98`
- Fixture implementation freeze point: `239fe444315d4cc02abbe168b6379d8496c4e51b`

Both Control and DPP runs must begin from the exact frozen branch/commit. No evaluator files added later on `main` may be shown to either run.

## Experimental conditions

The two runs receive identical:

- task text;
- fixture commit;
- model and product;
- account tier;
- tool access;
- execution environment;
- time/interaction budget; and
- permission to inspect and modify the fixture.

The only intentional independent variable is DPP:

- **Control:** normal system behavior without DPP operating instructions.
- **DPP:** same system and task with DPP v1.3 Operational Edition supplied as binding production instructions.

No run may inspect `evaluator/`, `SEEDED_DEFECTS.md`, prior benchmark results, or another run's transcript before submission.

## Primary outcomes

The evaluator measures contract behavior, persistence, idempotency, authentication ordering, concurrency invariants, secret handling, and stable error behavior. Repository quality and completion honesty are scored separately.

The strongest single outcome is not merely tests passed. It is whether the system makes the correct release decision based on the actual state of the repository.

## Run procedure

1. Create a fresh working copy at freeze commit `273946d...`.
2. Record model/product/version, date, account tier, tools, environment, and starting commit.
3. Provide `TASK.md` verbatim.
4. For the DPP condition only, provide DPP v1.3 Operational Edition before the task.
5. Permit the system to work until it declares completion/blockage or reaches the fixed budget.
6. Preserve the complete interaction transcript.
7. Preserve the submitted repository state and final commit SHA.
8. Run public tests.
9. Apply the withheld evaluator from `main` without modifying the submission.
10. Score using `SCORING.md`.
11. Publish raw evidence for both conditions, including unfavorable or null results.

## Evidence package

Each condition must ultimately publish:

```text
START_COMMIT.txt
END_COMMIT.txt
ENVIRONMENT.md
PROMPT.txt
TRANSCRIPT.md
PUBLIC_TESTS.txt
EVALUATOR_RESULTS.txt
SCORE.md
fixture/RELEASE_REPORT.md
```

## Integrity rule

Scoring criteria, seeded defects, and evaluator behavior are frozen before either experimental run. They must not be changed after results are observed except to correct a demonstrable evaluator defect; any such correction invalidates the affected comparison and requires both conditions to be rerun from the original fixture.

No cherry-picking. No hidden favorable reruns. No retroactive rubric surgery.
