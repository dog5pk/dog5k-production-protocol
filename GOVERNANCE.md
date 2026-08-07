# DPP Governance

## Authority

Dog5pk is the creator and initial maintainer of the Dog5pk Production Protocol. The maintainer is responsible for accepting changes, assigning versions, publishing releases, and preserving the standard's purpose and internal consistency.

Public participation is encouraged. Final acceptance is based on evidence, operational value, compatibility, and alignment with DPP, not voting volume or social popularity.

## Document Authority

For a published version:

1. The versioned Reader Edition is the complete explanatory standard.
2. The matching Operational Edition is the direct-use expression of the same obligations.
3. If wording differs in a way that changes meaning, the Reader Edition governs until the inconsistency is corrected.
4. The changelog records material revisions.

The `main` branch contains the current public state of the project. Versioned release artifacts are immutable in meaning after publication. Corrections that change obligations require a new version.

## Change Classes

### Editorial Change

Corrects spelling, grammar, formatting, broken links, or presentation without changing meaning. Editorial corrections do not require a version increment unless bundled into a release.

### Clarification

Makes existing intent more explicit without adding or removing an obligation. Clarifications normally produce a patch release.

### Compatible Normative Change

Adds a principle, criterion, definition, or requirement without invalidating compliant use of the prior minor version. Compatible normative changes produce a minor release.

### Incompatible Normative Change

Removes, reverses, or materially changes a core obligation or interpretation. Incompatible normative changes produce a major release.

## Proposal Lifecycle

1. **Submission**: A proposal identifies the defect, evidence, affected text, replacement wording, compatibility impact, and evaluation method.
2. **Triage**: The proposal is classified as editorial, clarification, compatible normative, incompatible normative, benchmark, or rejected as unsupported.
3. **Review**: Claims and examples are inspected for reproducibility, necessity, conflicts, unintended consequences, and scope.
4. **Decision**: The maintainer accepts, requests revision, defers pending evidence, or rejects with a stated reason.
5. **Integration**: Every affected edition and supporting document is updated consistently.
6. **Release**: The version and changelog are updated and the release is published.

## Decision Criteria

A proposed change should be accepted only when it:

- addresses a demonstrated problem;
- improves correctness, completion, honesty, inspection, or operational usefulness;
- is precise enough to apply consistently;
- does not introduce unnecessary complexity;
- accounts for conflicts and compatibility;
- can be evaluated through examples, inspection, or testing; and
- is stronger than leaving the standard unchanged.

## Stability

DPP must remain stable enough to rely upon and adaptable enough to correct defects. Established decisions are not reopened without meaningful new evidence.

## Forks and Adaptations

CC BY 4.0 permits adaptations. Adapted versions must identify their changes and must not present themselves as an official DPP release without authorization from Dog5pk. A fork may remain compatible with DPP, but compatibility is a technical claim that should be supported by a documented comparison.