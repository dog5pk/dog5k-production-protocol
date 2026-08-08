# Open DPP Benchmarks

Benchmark 001 is complete. Benchmarks 002 and 003 are intentionally left to independent participants.

The purpose is simple: test whether applying the Dog5pk Production Protocol (DPP) changes the quality of an AI system's work under the same task conditions.

## Independent Test Method

1. Choose an AI platform and record the platform, model, and model/version information available to you.
2. Create a fresh conversation with no DPP context.
3. Give the model your benchmark task. Do not tell it that it is the Control condition or that another run will be compared against it.
4. Preserve the model's first completed response exactly as returned. Do not repair, rewrite, selectively excerpt, or improve it.
5. Create a second fresh conversation using the same platform/model.
6. Provide the current DPP Operational Edition and instruct the model to apply DPP to the next task.
7. Give it the exact same benchmark task used for Control.
8. Preserve that first completed response exactly as returned.
9. Compare the two outputs using the same rubric. Do not change scoring criteria after seeing the results.
10. Report the result whether DPP wins, ties, or loses.

## Required Submission Evidence

An independent benchmark submission must include:

- benchmark number;
- AI platform;
- model and version/build information when available;
- date of the test;
- complete Control output;
- complete DPP output;
- scoring rubric;
- Control score;
- DPP score;
- observed differences, including failures or weaknesses in either condition;
- disclosure of any retries, interruptions, tool use, context contamination, or other conditions that could affect the comparison.

The benchmark task itself does not have to be published if the tester wishes to keep it private, but both conditions must receive the identical task and the tester must state that this was the case.

## Integrity Rules

- Fresh context for each condition.
- Same task for both conditions.
- Same AI platform/model for the paired comparison.
- Control does not receive DPP.
- DPP condition receives DPP before the task.
- First completed output is the result unless a documented technical failure prevented completion.
- No hidden correction round may be presented as the original result.
- No removing embarrassing mistakes.
- No selective publication of only favorable DPP outcomes.
- A DPP loss is a valid result.
- A tie is a valid result.
- An inconclusive test is a valid result when the reason is documented.

## Scoring

A benchmark may use a task-specific rubric, but the rubric must be established before scoring both outputs and applied equally to both.

Benchmark 001 used eight dimensions scored out of five:

1. Correctness
2. Completeness
3. Constraint adherence
4. Internal consistency
5. Verification honesty
6. Failure/boundary handling
7. Usability
8. Unnecessary invention

Independent testers may use this rubric or a different one better suited to their task. If a different rubric is used, publish it with the result.

## Benchmarks 002 and 003

Benchmark 002 and Benchmark 003 are reserved for independent tests.

Dog5pk does not prescribe the task, platform, model, or expected outcome for either benchmark. The independent tester chooses the task and model while following the paired Control/DPP method above.

The point is not to manufacture another DPP victory. The point is to find out what happens when someone else runs the experiment.

## Benchmark 001

The first completed result is preserved at:

`results/benchmark-001/RESULTS.md`

Recorded result:

- Control: 35/40
- DPP: 37.5/40
- Difference: +2.5 points
- Relative improvement over Control score: +7.1%

Benchmark 001 should be treated as one observed result, not proof that DPP improves every model or every task.

## Submission Principle

Results should be published as they fell.

Wins, losses, ties, mistakes, unexpected behavior, and limitations are evidence. Do not dress the result up after the fact.