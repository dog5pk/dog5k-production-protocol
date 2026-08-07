# The Dog5pk Production Protocol

## A Production Standard for Dependable Human-AI Collaboration

**Whitepaper Version:** 1.0  
**Protocol Baseline:** DPP v1.3  
**Author:** Dog5pk  
**Status:** Public Whitepaper  
**Date:** August 2026  
**Motto:** *Step Forward or Step Aside.*

---

## Abstract

Generative artificial intelligence can produce useful software, analysis, documentation, plans, designs, and recommendations at extraordinary speed. Speed and fluency, however, do not establish that an output is correct, complete, reproducible, appropriately scoped, or ready for use. A system can produce an answer that appears finished while containing known defects, unsupported claims, hidden assumptions, placeholder implementations, contradictory decisions, unnecessary complexity, or unacknowledged uncertainty.

The Dog5pk Production Protocol (DPP) is a platform-independent production standard for collaboration between humans and artificial intelligence. DPP addresses the gap between plausible output and dependable work by defining twenty-four constitutional principles and a set of Production Acceptance Criteria governing completion, evidence, uncertainty, defects, constraints, complexity, inspection, recommendations, and professional responsibility.

DPP does not claim to make an AI system infallible, autonomous, truthful by construction, or universally superior. It does not modify a model's weights or replace platform safety controls. Instead, it establishes an explicit production discipline for how work is interpreted, produced, reviewed, corrected, characterized, and delivered.

This paper defines the problem DPP addresses, its design goals and non-goals, its operating model, the relationship among its principles, a proposed compliance model, and a reproducible benchmark methodology for evaluating whether applying DPP changes measurable output quality. At publication, claims about DPP's design are distinguished from empirical claims about performance. Quantitative superiority is not asserted in the absence of completed benchmark evidence.

---

## 1. Introduction

The widespread adoption of generative AI has changed the economics of producing intellectual and technical work. A person can request code, research, business analysis, documentation, troubleshooting, design guidance, or a complete project and receive substantial output within seconds.

This creates an unusual production problem: generation has become inexpensive while verification remains comparatively expensive.

The resulting failure mode is not limited to hallucination. An answer may contain no obvious fabricated fact and still fail as production work. It may stop before the requested objective is complete. It may knowingly leave a correctable defect. It may create interfaces with no implementation behind them. It may choose an inferior approach because it is easier to explain. It may contradict an earlier architectural decision. It may silently weaken a constraint. It may present inference as fact. It may add structure that creates the appearance of sophistication without creating capability.

These are production failures.

DPP begins from a simple proposition:

> The quality of human-AI collaboration should be judged by the state of the resulting work, not by the fluency of the interaction that produced it.

The protocol therefore treats correctness, completion, evidence, inspection, and honest characterization as production requirements rather than optional refinements.

---

## 2. The Production Reliability Problem

### 2.1 Plausibility is not completion

Large language models are optimized to generate likely continuations and useful responses. Human readers, meanwhile, are strongly influenced by coherent language, confident presentation, professional formatting, and apparent completeness. Together these properties can create a dangerous equivalence:

**looks complete = is complete**

DPP rejects that equivalence.

A polished implementation containing nonfunctional placeholders is incomplete. A research answer whose central claims are unsupported is incomplete. A recommendation that lists alternatives without exercising judgment may be incomplete. A document that contradicts its own definitions is incomplete regardless of typography.

### 2.2 The verification asymmetry

AI can often generate an artifact faster than a human can inspect it. As generated artifacts become larger, the cost of finding subtle defects rises. This creates a verification asymmetry: production accelerates while assurance can lag behind.

DPP responds by moving inspection into the production process. Review is not treated solely as a downstream human obligation. The producing system is expected to search actively for defects, uncertainty, contradictions, edge cases, and incomplete work before delivery.

### 2.3 Local optimization can damage the project

Conversational AI frequently operates one turn at a time. Projects do not. A locally reasonable response may conflict with established architecture, previously accepted constraints, terminology, or objectives.

DPP therefore treats continuity as a production property. Established decisions remain binding until meaningful new evidence justifies changing them.

### 2.4 Activity can imitate progress

Generating more files, prose, abstractions, diagrams, or architectural layers can create visible activity without improving the underlying work. DPP explicitly separates activity from progress. An artifact must solve an actual problem, establish a necessary contract, preserve evidence, or enable a defined capability.

---

## 3. Design Goals

DPP is designed to promote the following properties.

### 3.1 Correctness

Work should correspond to reality, applicable specifications, valid reasoning, and available evidence.

### 3.2 Completion

When the stated objective can reasonably be completed, the system should complete it rather than intentionally stopping at an intermediate stage.

### 3.3 Honest characterization

Facts, observations, measurements, inference, estimation, opinion, and speculation should not be represented as interchangeable categories.

### 3.4 Defect reduction

Known, materially correctable defects should be corrected before delivery whenever reasonably possible.

### 3.5 Inspectability

Important claims, decisions, assumptions, tests, inputs, and outputs should be traceable and independently reviewable where practical.

### 3.6 Continuity

Explicit constraints and established decisions should persist across the work unless explicitly changed or superseded by meaningful evidence.

### 3.7 Engineering judgment

When multiple valid approaches exist, the system should evaluate meaningful tradeoffs and recommend the strongest justified option rather than merely transferring the decision burden back to the user.

### 3.8 Appropriate complexity

Necessary complexity should be retained. Accidental and decorative complexity should be removed.

### 3.9 Platform independence

DPP should be usable across AI providers, model families, interfaces, agents, development environments, and professional domains without requiring modification of the underlying model.

---

## 4. Non-Goals

DPP is not:

- a jailbreak or mechanism for bypassing platform safeguards;
- a claim that AI output can be made universally correct;
- a replacement for domain experts, testing, peer review, legal review, medical judgment, safety engineering, or other appropriate human oversight;
- a model architecture or training method;
- a truth oracle;
- a guarantee that an AI system possesses information or capabilities it does not actually possess;
- a mechanism for fabricating unavailable evidence;
- a universal definition of production readiness independent of context; or
- a claim that every task benefits from maximum ceremony.

DPP governs production behavior. It does not manufacture capabilities that are absent from the underlying system or tools.

---

## 5. Protocol Foundation

DPP v1.3 consists of twenty-four constitutional principles plus Production Acceptance Criteria. The principles can be understood as a system of mutually reinforcing production controls rather than twenty-four unrelated instructions.

### 5.1 Reality and epistemic discipline

**Principle I: Reality Wins** establishes external reality as the final authority.  
**Principle VI: Truth Over Confidence** requires confidence to remain bounded by evidence.  
**Principle X: Evidence First** prefers appropriate evidence over unsupported assertion.

Together these principles govern what may responsibly be claimed.

### 5.2 Completion and defect discipline

**Principle II: Known Defects Must Be Corrected** requires correction of known material defects where reasonably possible.  
**Principle III: Finish the Work** rejects intentional partial completion when completion is available.  
**Principle IV: Zero Placeholder Policy** prohibits incomplete work from masquerading as finished work.  
**Principle XII: Honest Failure** defines how genuine blockers must be disclosed.

Together these principles govern the difference between partial work, failed work, and finished work.

### 5.3 Structural discipline

**Principle V: No Scaffolding**, **Principle XI: Eliminate Accidental Complexity**, **Principle XVI: No Artificial Inflation**, and **Principle XVIII: Every Artifact Must Earn Its Existence** constrain the tendency to equate volume or architectural complexity with quality.

DPP does not seek minimum complexity. It seeks justified complexity.

### 5.4 Production and inspection discipline

**Principle VII: Think Before Producing** makes review part of generation.  
**Principle VIII: Production Mindset** requires awareness of downstream consequences.  
**Principle IX: Determinism** favors predictable behavior where practical.  
**Principle XIX: Build for Inspection** requires work to withstand independent review.

These principles make assurance part of the production lifecycle rather than an afterthought.

### 5.5 Decision and constraint discipline

**Principle XIV: Internal Consistency**, **Principle XV: Respect Constraints**, and **Principle XVII: Preserve Established Decisions** protect project continuity.

An AI system applying DPP should not silently reinterpret a requirement or repeatedly reopen a settled decision simply because another answer is easier to generate.

### 5.6 Judgment and intent

**Principle XIII: Recommendation Responsibility** requires justified recommendations when evidence permits.  
**Principle XX: Respect the User's Intent** protects the stated objective from silent substitution.  
**Principle XXI: Excellence Over Convenience** makes engineering merit, not convenience, the deciding factor among valid approaches.

### 5.7 Progress and improvement

**Principle XXII: The Craftsman's Rule** requires each interaction to improve the state of the work.  
**Principle XXIII: Continuous Improvement** applies that obligation to DPP itself.

### 5.8 Honest boundaries

**Principle XXIV: Contracts Shall Be Honest** distinguishes legitimate specifications, interfaces, schemas, mocks, and test doubles from fake implementation. A contract may precede implementation when its status is explicit and it establishes a real boundary. It may not falsely imply functionality that does not exist.

---

## 6. The DPP Production Lifecycle

DPP can be operationalized as a seven-stage lifecycle.

### Stage 1: Establish the objective

Identify what the user is actually trying to accomplish. Separate the objective from incidental wording and preserve explicit constraints.

### Stage 2: Establish known state

Determine relevant facts, existing artifacts, prior decisions, available tools, dependencies, uncertainties, and environmental constraints.

### Stage 3: Plan the work

Choose an approach based on correctness, reliability, maintainability, security, inspectability, long-term value, and the user's requirements. Avoid unnecessary architecture and premature artifacts.

### Stage 4: Produce

Perform the requested work. Implement rather than merely describe implementation when implementation is requested and available.

### Stage 5: Inspect

Before delivery, search for:

- logical errors;
- contradictions;
- known defects;
- unsupported claims;
- incomplete requirements;
- placeholders;
- security weaknesses;
- edge cases;
- unnecessary complexity;
- constraint violations;
- conflicts with established decisions; and
- mismatches between claimed and actual completion status.

### Stage 6: Correct or disclose

Correct discovered defects where reasonably possible. If a defect or blocker cannot be corrected, disclose it precisely and avoid claiming completion beyond the evidence.

### Stage 7: Deliver and characterize

Present the strongest reasonably achievable result, state material limitations, preserve evidence appropriate to the task, and make the completion state clear.

This lifecycle is intentionally technology-neutral. It can be performed conversationally, encoded into agent workflows, incorporated into review checklists, or enforced by surrounding software.

---

## 7. Evidence, Claims, and Uncertainty

DPP treats epistemic status as part of the output.

A useful implementation should distinguish at least the following categories when the distinction matters:

| Category | Meaning |
|---|---|
| Verified fact | Supported by authoritative or directly checked evidence |
| Observation | Directly observed in available material or system state |
| Measurement | Produced through an identified measurement process |
| Inference | Derived from evidence but not directly observed |
| Estimate | Approximation based on stated assumptions or limited information |
| Opinion | Judgment not reducible to objective verification |
| Speculation | Plausible possibility lacking sufficient evidence |
| Unknown | Information not established from available evidence |

The protocol does not require every sentence to carry a label. It requires that material distinctions not be hidden when doing so could mislead the user or reviewer.

### 7.1 Confidence is not evidence

A language model's fluent expression of certainty is not evidence for the proposition expressed. DPP therefore rejects confidence as a substitute for verification.

### 7.2 Evidence should be proportional to consequence

Not every claim requires formal citation or experimental proof. The required evidence should reflect the importance, contestability, reversibility, and consequence of the claim.

### 7.3 Unknown must remain available as an answer

A system operating under DPP must be permitted to state that something is unknown. Fabricating a missing value to preserve conversational smoothness violates the protocol.

---

## 8. Completion and Production Acceptance

DPP separates generation from acceptance.

An artifact may be generated without satisfying the standard for delivery as completed work. Before a final deliverable is characterized as complete, DPP v1.3 requires evaluation against Production Acceptance Criteria including technical correctness, logical consistency, completeness relative to the request, honesty about uncertainty, absence of known correctable defects, absence of unnecessary placeholders and decorative scaffolding, maintainability, inspectability, constraint compliance, appropriate evidence, and justified complexity.

The acceptance decision is context-dependent. A prototype and a production service have different requirements. A brainstorming note and a published research report have different requirements. DPP does not erase those distinctions. It requires the claimed completion state to match the actual standard applicable to the artifact.

### 8.1 Completion states

For operational purposes, implementations may use states such as:

- **Complete:** stated objective satisfied and applicable acceptance criteria met.
- **Complete with disclosed limitations:** objective satisfied but material limitations remain and are explicitly characterized.
- **Partial:** useful work produced but the objective is not yet satisfied.
- **Blocked:** completion depends on unavailable information, access, evidence, authority, or capability.
- **Failed:** attempted work did not produce a usable result.

These labels are implementation guidance, not additional constitutional principles.

---

## 9. Failure as Information

Traditional conversational systems can be implicitly rewarded for always producing an answer. Production systems require a different incentive: a truthful failure can be more valuable than a fabricated success.

Under DPP, an honest failure should identify:

1. what could not be completed;
2. the exact blocker;
3. what information, capability, access, evidence, or authority is missing;
4. what useful work has been preserved; and
5. the shortest responsible path toward completion.

This converts failure from conversational embarrassment into actionable project state.

---

## 10. Constraints and Decision Persistence

Long-running AI-assisted projects accumulate decisions. Without persistence, the collaboration can repeatedly revisit settled questions, introduce incompatible patterns, or silently discard constraints.

DPP treats explicit constraints as binding until changed. Established decisions remain settled until meaningful new evidence justifies reconsideration.

This does not prohibit revision. It requires revision to be visible and justified.

A DPP-conformant workflow should therefore maintain, where appropriate:

- current objectives;
- explicit constraints;
- accepted decisions;
- superseded decisions and reasons;
- unresolved blockers;
- relevant evidence; and
- artifact status.

The storage mechanism is outside the protocol's scope. It may be conversational context, project documentation, version control, a database, or another state system.

---

## 11. Complexity and Artifact Economics

Generative systems can produce structure at near-zero marginal cost. This makes overproduction unusually easy.

DPP treats every artifact as carrying cost. A file must be maintained. An abstraction must be understood. A dependency can fail. An interface can constrain future implementation. A paragraph can obscure the important paragraph beside it.

The protocol therefore asks of every artifact:

> What present problem does this solve?

Valid answers include implementing required behavior, establishing a necessary contract, preserving evidence, enabling a defined capability, improving inspection, or satisfying a real operational requirement.

"Projects like this usually have one" is not sufficient justification.

At the same time, DPP rejects false simplicity. Security checks, validation, recovery logic, tests, fault tolerance, and other essential complexity must not be removed merely to reduce visible size.

---

## 12. Inspection and Reproducibility

Trust based exclusively on confidence or reputation is fragile. DPP favors artifacts that can be inspected.

Depending on the domain, inspection may include:

- source code and tests;
- exact prompts and outputs;
- citations and source records;
- build commands;
- environment information;
- input datasets;
- decision records;
- test fixtures;
- version identifiers;
- benchmark rubrics; and
- documented assumptions.

Reproducibility is not always absolute. Hosted models change, nondeterministic systems vary, external data evolves, and proprietary systems may expose limited internals. DPP requires unavoidable nondeterminism and uncertainty to be documented rather than silently ignored.

---

## 13. A Proposed Compliance Model

DPP v1.3 defines principles and acceptance criteria but does not claim that compliance can be reduced to a single universal number. Different domains have different failure costs.

For practical evaluation, this whitepaper proposes three levels of assessment.

### 13.1 Principle-level assessment

For each materially applicable principle, record:

- **Satisfied**
- **Partially satisfied**
- **Violated**
- **Not applicable**
- **Insufficient evidence**

A finding should include evidence rather than a bare label.

### 13.2 Acceptance assessment

Evaluate whether the final artifact satisfies each applicable Production Acceptance Criterion. Material failure of a required criterion prevents an unqualified claim of completion.

### 13.3 Critical-failure assessment

Certain failures should be reported independently of aggregate scores. Examples include:

- fabricated evidence;
- invented test results;
- knowingly nonfunctional code represented as complete;
- silent violation of an explicit constraint;
- material unsupported claims represented as verified fact; or
- concealment of a known blocker while claiming completion.

A high average score must not erase a catastrophic failure. Aggregation can otherwise hide precisely the behavior DPP is intended to expose.

---

## 14. Benchmark Methodology

DPP is a proposed production standard. Whether it improves measurable outcomes is an empirical question.

The DPP repository therefore defines paired control-versus-DPP benchmarks.

### 14.1 Paired evaluation

A benchmark should compare two runs:

**Control:** the task is performed without DPP instructions.  
**DPP:** the same task is performed with the applicable DPP protocol.

Task input and material conditions should remain as identical as practical.

### 14.2 Required provenance

A reproducible benchmark should record:

- exact task input;
- exact control prompt;
- exact DPP prompt or protocol material;
- complete raw outputs;
- model and product identity;
- date;
- relevant tool access;
- account tier where material;
- environmental conditions;
- deviations or redactions; and
- scoring evidence.

### 14.3 Evaluation dimensions

The current benchmark framework evaluates nine dimensions:

1. correctness;
2. completeness;
3. constraint adherence;
4. evidence quality;
5. uncertainty calibration;
6. defect handling;
7. inspectability;
8. complexity discipline; and
9. practical usability.

Critical failures are reported separately.

### 14.4 Benchmark domains

Initial evidence should span at least:

- software implementation;
- research or analysis; and
- finished document production.

This reduces the risk of optimizing DPP's evaluation around a single class of work.

### 14.5 Negative and null results

Unfavorable results must not be omitted. A benchmark in which DPP provides no measurable benefit, reduces quality, increases unnecessary verbosity, or creates other regressions is evidence and should be preserved.

DPP's own Evidence First principle requires nothing less.

---

## 15. Claims and Evidence Status

At Whitepaper v1.0 publication, the following distinction is mandatory.

### Design claims

The protocol is explicitly designed to:

- reduce false completion;
- expose known blockers;
- preserve explicit constraints;
- discourage unsupported confidence;
- promote pre-delivery inspection;
- distinguish necessary from decorative complexity;
- improve traceability; and
- maintain continuity across project work.

These claims describe intended mechanisms and are directly inspectable in the standard.

### Empirical claims

This whitepaper does **not** currently claim a demonstrated percentage improvement in correctness, completion, reliability, productivity, defect rate, or any other quantitative outcome.

Such claims require reproducible benchmark evidence. Results should be added only after the relevant experiments have been completed and published.

This distinction is deliberate. A standard concerned with evidence should not manufacture evidence for itself.

---

## 16. Threats to Validity and Limitations

DPP has important limitations.

### 16.1 Instruction adherence varies

An AI system may fail to follow DPP instructions consistently. Protocol text does not guarantee model compliance.

### 16.2 Self-review is imperfect

A system that produced an error may also fail to detect that error during review. Independent tests, tools, reviewers, or domain experts may still be necessary.

### 16.3 More process can create overhead

For trivial or low-consequence tasks, exhaustive application of every production control can waste time and increase output size. DPP should be applied proportionally to the task while preserving its core requirements.

### 16.4 Domain expertise remains necessary

DPP cannot replace missing subject-matter expertise. A disciplined but uninformed answer can still be wrong.

### 16.5 Evidence availability constrains verification

Some claims cannot be verified from available tools or sources. DPP requires honest characterization of that limitation; it cannot eliminate it.

### 16.6 Benchmarks can be gamed

Any fixed rubric can become a target for optimization. Public benchmark design should evolve, include adversarial cases, preserve raw evidence, and avoid relying solely on aggregate scores.

### 16.7 Human evaluators disagree

Some dimensions, including maintainability and practical usability, contain judgment. Rubrics should define criteria clearly, and inter-rater disagreement should be preserved rather than concealed where relevant.

### 16.8 DPP itself can be wrong

The protocol is not exempt from its own principles. Defects, contradictions, unnecessary requirements, or ineffective mechanisms discovered through use should be corrected through documented versioned revisions.

---

## 17. Relationship to Existing Practice

DPP does not claim to have invented testing, peer review, evidence, requirements management, reproducibility, software quality assurance, or professional engineering judgment. These disciplines long predate generative AI.

DPP's contribution is their consolidation into a platform-independent production standard specifically aimed at human-AI collaboration and the characteristic failure modes of generative systems.

The protocol is complementary to, rather than a replacement for:

- software development methodologies;
- continuous integration and automated testing;
- secure development practices;
- scientific reproducibility methods;
- peer review;
- quality-management systems;
- model evaluations;
- AI safety policies;
- organizational governance; and
- domain-specific professional standards.

A mature implementation may integrate DPP with these systems rather than attempting to reproduce them.

---

## 18. Adoption and Implementation

DPP can be adopted at several levels.

### 18.1 Conversational use

A user can provide the Operational Edition or an appropriate DPP instruction set to an AI system and apply the Production Acceptance Criteria before accepting final work.

### 18.2 Project use

A project can record DPP as a persistent production standard and maintain explicit objectives, constraints, decisions, evidence, and completion status alongside normal project artifacts.

### 18.3 Agent and toolchain use

Agentic systems can encode DPP stages into orchestration logic, requiring explicit inspection and acceptance steps before an artifact is marked complete.

### 18.4 Organizational use

Teams can adapt DPP into review checklists, procurement requirements, internal AI-use policies, benchmark suites, or quality gates while clearly identifying adaptations rather than representing modified text as the canonical standard.

---

## 19. Governance and Versioning

DPP is versioned because a production standard must be stable enough to rely upon and capable of improvement.

Changes should be driven by evidence, operational experience, discovered ambiguity, contradiction, demonstrated failure modes, or other concrete need.

Material changes to normative meaning require appropriate versioning and documentation. Editorial corrections should not be represented as substantive protocol changes.

The canonical repository maintains the current standard, operational materials, governance policy, changelog, benchmark methodology, and contribution process.

Independent adaptations are encouraged where licensing permits, but adaptations should identify themselves clearly and should not create ambiguity about the canonical DPP text.

---

## 20. Research Agenda

The immediate research program for DPP should address the following questions.

### RQ1: Does DPP improve completion quality?

Measure whether paired DPP runs more frequently satisfy the full stated objective than controls.

### RQ2: Does DPP reduce known-defect delivery?

Measure defects identifiable from the generated artifact and determine whether DPP changes their frequency or severity.

### RQ3: Does DPP improve uncertainty calibration?

Evaluate whether unsupported certainty, fabricated specifics, and failure to disclose unknowns decrease under DPP.

### RQ4: Does DPP improve constraint persistence?

Test long-running and multi-turn tasks containing explicit constraints and settled decisions.

### RQ5: What is DPP's cost?

Measure token use, latency, review overhead, interaction count, and unnecessary verbosity. Improved output purchased at disproportionate cost may not represent practical improvement.

### RQ6: Which principles contribute most?

Ablation studies can remove or isolate principle groups to determine which mechanisms materially affect outcomes.

### RQ7: How portable is DPP?

Evaluate multiple model families, providers, interfaces, agent systems, and task domains.

### RQ8: Can compliance be independently scored reliably?

Measure agreement among human reviewers and, separately, automated evaluators.

### RQ9: Where does DPP fail?

Actively search for tasks where DPP degrades results, creates excessive process, produces false confidence in review, or conflicts with domain-specific best practice.

The final question is as important as the first eight. A protocol that cannot describe its own failure envelope cannot responsibly describe its strengths.

---

## 21. Security and Safety Considerations

DPP is a production-quality framework, not an authorization system. Respecting user intent does not override law, safety requirements, platform policy, access controls, or professional obligations.

Likewise, "Finish the Work" does not require a system to perform actions it lacks authority or capability to perform. Honest Failure applies when completion is prohibited or impossible.

Production quality in safety-critical contexts requires domain-specific controls beyond DPP. The protocol should be treated as an additional discipline, not as certification that an artifact is safe.

---

## 22. Discussion

Generative AI changes who can produce sophisticated artifacts and how quickly they can be produced. It does not repeal the conditions under which those artifacts become trustworthy.

The central challenge is therefore not merely increasing model intelligence. It is establishing production behavior that remains useful when fluent generation is cheap.

DPP approaches that problem by making several implicit professional expectations explicit:

- finish what can be finished;
- do not knowingly ship defects that can be corrected;
- do not pretend missing implementation exists;
- distinguish evidence from confidence;
- inspect before delivery;
- preserve constraints and decisions;
- justify complexity;
- make failure actionable;
- recommend rather than evade judgment; and
- measure progress by the state of the work.

None of these expectations is individually exotic. Their value, if demonstrated, lies in applying them together as a persistent production discipline for human-AI collaboration.

---

## 23. Conclusion

DPP proposes that human-AI collaboration should be evaluated by a stricter standard than whether an answer is fluent, useful-looking, or immediately satisfying.

The relevant question is whether the resulting work is correct enough for its purpose, complete relative to its stated objective, honest about what is known, free of known correctable defects, consistent with its constraints, justified in its complexity, inspectable where necessary, and accurately characterized at delivery.

DPP v1.3 expresses this standard through twenty-four constitutional principles and Production Acceptance Criteria. The protocol does not guarantee those outcomes, and this whitepaper does not claim empirical superiority before evidence exists. Instead, DPP defines the behavior to be evaluated and publishes a methodology by which its effectiveness can be tested.

That is the standard DPP applies to itself.

Reality remains the benchmark. Finished work remains the objective.

**Step Forward or Step Aside.**

---

## Appendix A: DPP v1.3 Principle Index

1. Reality Wins
2. Known Defects Must Be Corrected
3. Finish the Work
4. Zero Placeholder Policy
5. No Scaffolding
6. Truth Over Confidence
7. Think Before Producing
8. Production Mindset
9. Determinism
10. Evidence First
11. Eliminate Accidental Complexity
12. Honest Failure
13. Recommendation Responsibility
14. Internal Consistency
15. Respect Constraints
16. No Artificial Inflation
17. Preserve Established Decisions
18. Every Artifact Must Earn Its Existence
19. Build for Inspection
20. Respect the User's Intent
21. Excellence Over Convenience
22. The Craftsman's Rule
23. Continuous Improvement
24. Contracts Shall Be Honest

The canonical wording of each principle is maintained in the DPP v1.3 Reader Edition. This whitepaper explains the protocol but does not supersede the canonical standard.

---

## Appendix B: Production Acceptance Checklist

Before representing work as complete, evaluate whether it is:

- technically correct;
- logically consistent;
- complete relative to the stated request;
- honest about uncertainty;
- free of known correctable defects;
- free of unnecessary placeholders;
- free of decorative scaffolding;
- clear about incomplete implementation status;
- maintainable where applicable;
- inspectable;
- production-minded relative to its intended use;
- appropriate for its intended audience;
- consistent with established decisions;
- compliant with explicit constraints;
- supported by evidence where evidence is required;
- free of accidental complexity;
- inclusive of essential complexity; and
- the strongest solution reasonably achievable under the circumstances.

---

## Appendix C: Minimal Benchmark Record

Each published benchmark should preserve at minimum:

```text
Benchmark ID:
Domain:
Task:
Date:
Model:
Product/interface:
Account tier if material:
Tool access:
Environment:

CONTROL
Exact prompt:
Complete raw output:

DPP
DPP version:
Exact prompt/protocol input:
Complete raw output:

EVALUATION
Correctness:
Completeness:
Constraint adherence:
Evidence quality:
Uncertainty calibration:
Defect handling:
Inspectability:
Complexity discipline:
Practical usability:
Critical failures:

Deviations/redactions:
Evaluator notes:
Conclusion:
```

A conclusion must remain within the scope of the recorded evidence.

---

## Appendix D: Canonical Resources

The canonical DPP repository contains:

- DPP v1.3 Reader Edition;
- DPP v1.3 Operational Edition;
- Quick Start guidance;
- governance and contribution policies;
- benchmark methodology and submission template;
- version history; and
- the public DPP website.

Repository: `github.com/dog5pk/dog5pk-production-protocol`

Website: `dog5pk.github.io/dog5pk-production-protocol/`

---

## Publication Note

Whitepaper v1.0 documents the design and evaluation framework of DPP against the DPP v1.3 protocol baseline. Future whitepaper revisions may incorporate published benchmark findings, independent evaluation, prior-art analysis, formalized compliance criteria, and implementation experience. Any such additions should distinguish observed evidence from interpretation and should preserve unfavorable findings alongside favorable ones.
