# DPP Quick Start

This guide applies DPP to a real human-AI task without requiring ceremonial chanting, a dashboard, or seventeen onboarding meetings.

## Choose an Edition

Use the **Reader Edition** when studying, reviewing, teaching, or citing DPP.

Use the **Operational Edition** when supplying DPP directly to an AI system as working instructions.

## Minimum Task Brief

Provide the AI system with:

1. **Objective**: the result that must exist when the work is complete.
2. **Inputs**: files, facts, prior decisions, examples, and available tools.
3. **Constraints**: formats, platforms, deadlines, budgets, safety boundaries, and requirements that remain binding.
4. **Definition of completion**: observable conditions that prove the work is done.
5. **Verification method**: tests, inspection steps, citations, calculations, or review criteria.

## Reusable Task Wrapper

```text
Apply the Dog5pk Production Protocol v1.3 Operational Edition to this task.

Objective:
[State the required finished result.]

Inputs:
[List the available information, files, tools, and prior decisions.]

Binding constraints:
[List every requirement that must not be weakened or silently changed.]

Completion criteria:
[List the observable conditions that must be true before completion is claimed.]

Verification:
[State how important claims and outputs will be checked.]

Do the work rather than merely explaining how it could be done. Before claiming completion, perform the DPP Production Acceptance Check and disclose any exact blocker or unresolved limitation.
```

## Example

```text
Apply DPP v1.3 to produce a deployable one-page website.

Objective:
Create a responsive static landing page that explains a public technical standard and links to its documentation.

Inputs:
The attached logo, approved copy, and existing repository.

Binding constraints:
Use plain HTML and CSS. No external JavaScript. Mobile-first. All links must resolve. No placeholder text.

Completion criteria:
The repository contains the finished page, it renders at 360 px and desktop width, every link works, and the README contains deployment instructions.

Verification:
Inspect the files, validate links, and report the exact checks performed.
```

## Final Review

Before accepting the result, verify:

- Does the requested artifact actually exist?
- Does it satisfy every binding constraint?
- Were claims and tests verified rather than invented?
- Are known defects corrected or explicitly disclosed?
- Are unfinished elements clearly identified rather than disguised?
- Did every file, section, and abstraction earn its existence?
- Can another person inspect and reproduce the important result?

A polished answer that fails these checks is still a failed result. It is merely wearing nicer shoes.