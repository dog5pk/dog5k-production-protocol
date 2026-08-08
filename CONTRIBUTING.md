# Contributing to DPP

DPP improves through evidence, operational experience, and reproducible defects. It does not change merely because a different phrase sounds nicer on a Tuesday.

## Accepted Contribution Types

- Contradictions or ambiguities with concrete examples.
- Reproducible failures in real human-AI workflows.
- Proposed wording that closes a demonstrated loophole.
- Independent benchmark results comparing identical tasks with and without DPP.
- Corrections to formatting, grammar, links, or cross-references.
- Adoption guidance supported by practical use.

## Before Submitting

Read the current Reader Edition, Operational Edition, Governance document, and open issues. Confirm that the concern is not already addressed.

## Required Proposal Format

A material proposal must include:

1. The affected principle, criterion, or document.
2. The exact defect or operational problem.
3. A reproducible example or evidence.
4. Complete proposed wording.
5. Compatibility and versioning impact.
6. A method for evaluating whether the change works.
7. An explanation of why it improves DPP rather than expressing preference.

## Pull Requests

Pull requests should address one coherent change and must:

- explain what changed and why;
- update every affected edition consistently;
- update `CHANGELOG.md` for normative or behavioral changes;
- preserve established terminology unless evidence justifies changing it;
- contain no placeholders, fake examples, invented results, or decorative files; and
- pass link, formatting, and consistency review.

## Independent Benchmark Submissions

Use [`BENCHMARKS.md`](BENCHMARKS.md) as the governing method.

A valid benchmark submission must preserve the paired comparison and include:

- AI platform and model/version information when available;
- date of the test;
- complete Control output;
- complete DPP output;
- scoring rubric;
- Control and DPP scores;
- observed weaknesses or failures in either condition; and
- disclosure of retries, interruptions, tool use, contamination, or other conditions that could affect the result.

The benchmark task itself may remain private, but the submitter must state that both conditions received the exact same task.

Results are accepted whether DPP wins, ties, loses, or the comparison is inconclusive. Selective reporting is not acceptable.

## Editorial Corrections

Spelling, grammar, formatting, and broken-link corrections may be submitted without a full normative proposal when they do not change meaning.

## Licensing

By contributing, you agree that your contribution may be distributed under the repository's CC BY 4.0 license and that attribution may be recorded through Git history and release notes.

## Review Standard

Submissions are evaluated for correctness, clarity, necessity, compatibility, inspectability, and demonstrable value. Popularity and confidence are not substitutes for evidence. Neither is a heroic quantity of jargon.