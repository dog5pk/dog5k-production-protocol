# Changelog

All material changes to the Dog5pk Production Protocol are documented here.

## [Unreleased]

### Repository
- Added an open independent benchmark framework for future third-party Control/DPP comparisons.
- Published Benchmark 001 results under `results/benchmark-001/`.

These repository additions do not alter the normative meaning of DPP v1.4.

## [1.4] - 2026-08-07

### Added
- Principle XXV: Compliance Must Be Demonstrated.
- Explicit two-layer operating model: Behavioral Execution and Compliance Verification.
- Completion evidence states: Implemented, Verified, Verified with limitations, and Blocked.
- Requirement that claimed tests, inspections, searches, tool calls, file operations, corrections, and other verification activity must correspond to activity that actually occurred.
- Explicit prohibition on invented verification history or unsupported self-reporting about unseen drafts, checks, or corrections.

### Changed
- Production Acceptance Check now includes verification-provenance and completion-state requirements.
- DPP now distinguishes instruction compliance from demonstrated compliance.
- README and public release links now point to v1.4.

### Basis for revision
- Operational use showed that an AI can drift from DPP even while instructed to follow it.
- Benchmark 001 showed that DPP improved a paired result while still allowing unsupported self-reporting about invisible drafting activity.
- These observations demonstrated that a behavioral protocol alone was insufficient; compliance itself needed an inspectable verification layer.

## [1.3] - 2026-07-25

### Added
- Principle XXIV: Contracts Shall Be Honest.
- Explicit distinction between legitimate contract definitions and decorative placeholders.
- Separate Reader and Operational editions as official release artifacts.

### Changed
- Principle XI now distinguishes essential complexity from accidental complexity.
- Related principles remain independent constitutional requirements rather than being merged for editorial brevity.

## [1.2] - 2026-07-25

### Added
- Principle XXIII: Continuous Improvement.
- Production Acceptance Criteria.

### Changed
- Formalized DPP as a production standard.
- Corrected the official motto to *Step Forward or Step Aside.*
- Improved terminology, organization, and publication readiness.

## [1.1] - 2026-07-25

### Added
- Known Defects Must Be Corrected.
- No Artificial Inflation.
- Preserve Established Decisions.
- Every Artifact Must Earn Its Existence.
- Build for Inspection.
- Excellence Over Convenience.
- The Craftsman's Rule.

## [1.0] - 2026-07-25

- Initial public release.