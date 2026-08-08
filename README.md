# Dog5pk Production Protocol (DPP)

**A production standard for rigorous human-AI collaboration.**

[![Version](https://img.shields.io/badge/version-1.4-blue)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-public_standard-brightgreen)](reader/DPP-v1.4-Reader.md)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey)](LICENSE.md)

**Creator:** Dog5pk  
**Motto:** *Step Forward or Step Aside.*

DPP is a platform-independent production standard for collaboration between humans and artificial intelligence. It exists to close the gap between work that looks finished and work that survives inspection, implementation, and reality.

DPP requires correctness, completion, evidence, honest uncertainty, disciplined judgment, respect for constraints, professional responsibility, and demonstrable compliance. It rejects fake progress, decorative scaffolding, unsupported confidence, invented verification history, and incomplete work presented as complete.

## Start Here

| Resource | Purpose |
|---|---|
| [Whitepaper](whitepaper/DPP-Whitepaper-v1.0.md) | Design rationale, operating model, limitations, and research agenda |
| [Reader Edition v1.4](reader/DPP-v1.4-Reader.md) | The complete public standard with explanations and acceptance criteria |
| [Operational Edition v1.4](operational/DPP-v1.4-Operational.md) | Compact operating instructions for direct AI use |
| [Quick Start](docs/QUICKSTART.md) | Apply DPP to a real task in minutes |
| [Open Benchmarks](BENCHMARKS.md) | Independently test DPP using paired Control/DPP runs |
| [Benchmark 001 Results](results/benchmark-001/RESULTS.md) | First published paired result |
| [Governance](GOVERNANCE.md) | How DPP versions and proposals are managed |
| [Contributing](CONTRIBUTING.md) | How to report defects and propose improvements |

## What Changed in v1.4

DPP v1.4 adds a second layer to the protocol: **compliance verification**.

An AI system following DPP is no longer expected merely to assert that it complied. Before claiming completion, it must compare the actual work and available evidence against the user's objective, constraints, established decisions, material claims, and Production Acceptance Criteria.

DPP now explicitly separates:

- **Behavioral Execution** — perform the work under DPP.
- **Compliance Verification** — inspect whether the work actually complied.

It also distinguishes four completion evidence states: **Implemented**, **Verified**, **Verified with limitations**, and **Blocked**.

## What DPP Requires

Work governed by DPP should be:

- technically correct;
- complete relative to the stated objective;
- honest about uncertainty and limitations;
- free of known correctable defects;
- free of fake implementations and decorative scaffolding;
- consistent with established decisions and explicit constraints;
- supported by evidence appropriate to the claim;
- inspectable and reproducible where practical;
- free of invented verification history;
- explicit about whether work is implemented, verified, verified with limitations, or blocked when that distinction matters;
- production-minded without accidental complexity; and
- measurably improved by each meaningful interaction.

## What DPP Is Not

DPP is not a jailbreak, prompt exploit, model override, safety bypass, or claim that artificial intelligence can be made infallible.

It is a standard against which the quality, completeness, honesty, and verifiability of human-AI production work can be evaluated.

## Use DPP

1. Choose the Reader Edition for study or the Operational Edition for direct use.
2. Provide the AI system with the task, constraints, available evidence, and definition of completion.
3. Require execution under DPP.
4. Require the final work to pass DPP's Compliance Verification and Production Acceptance Check before completion is claimed.
5. Verify material claims, tests, links, files, and outputs against the available record.

## Repository Structure

```text
.
├── whitepaper/      # Design rationale and research agenda
├── reader/          # Complete explanatory editions
├── operational/     # Direct-use operating editions
├── docs/            # Adoption and reference guidance
├── results/         # Published benchmark results
├── examples/        # Practical usage examples
└── .github/         # Structured issue and contribution workflows
```

## Versioning

DPP uses semantic versioning for the standard:

- **Major:** incompatible change to core obligations or meaning.
- **Minor:** new principle, criterion, or compatible normative requirement.
- **Patch:** clarification or correction that does not change intended obligations.

The current public release is **v1.4**. Material changes are documented in [CHANGELOG.md](CHANGELOG.md).

## License and Attribution

DPP is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE.md).

Suggested attribution:

> Dog5pk Production Protocol (DPP), version 1.4, created by Dog5pk, licensed under CC BY 4.0.

## Citation

Machine-readable citation metadata is provided in [CITATION.cff](CITATION.cff).

---

**Reality is the benchmark. Finished work is the objective. Compliance must survive inspection.**