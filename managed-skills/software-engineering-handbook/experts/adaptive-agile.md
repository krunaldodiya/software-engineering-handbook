# Adaptive agile-delivery experts

Use for a multi-slice initiative that needs right-sized planning, readiness,
course correction, status, a human walkthrough, or retrospective learning. A
clear localized change stays on the handbook's direct path. This fallback does
not load the BMAD router, agents, installer, or module runtime.

## Choose planning depth

Start at the earliest unresolved decision, not at a mandatory phase zero.

- A clear, reversible change may enter the build loop directly.
- A bounded feature needs an accepted specification and dependency-aware tasks.
- A product or cross-system initiative may also need discovery, UX, architecture
  invariants, epics, and readiness review.

Risk, uncertainty, coordination, and durability determine depth. Artifact count,
story points, or provider ceremony do not.

## Context, product, and architecture

`bmad-project-context` verifies commands, policies, conventions, decisions, and
known pitfalls in the current repository without overwriting user-owned
guidance.

`bmad-brainstorming`, `bmad-product-brief`, `bmad-prfaq`, and `bmad-prd` are
alternative discovery depths. Use one path, not all. A brief captures an already
credible problem; PRFAQ works backward from user value and challenges demand,
feasibility, and stakeholder questions; a PRD makes outcomes, scope, constraints,
acceptance, and unresolved decisions durable.

`bmad-ux` captures user journeys, interaction states, accessibility, and
actual-surface acceptance for interface-heavy work. `bmad-architecture` records
only the invariants and boundaries needed to keep independently built slices
compatible. `bmad-spec` distills accepted inputs into a concise what-before-how
contract with outcomes, non-goals, constraints, scenarios, and acceptance.

## Epics, stories, and readiness

`bmad-create-epics-and-stories` decomposes accepted outcomes into vertical,
independently useful slices with observable acceptance. Do not create technical
layer epics or split work merely to fill a sprint.

`bmad-sprint-planning` checks whether the selected slice has sufficient current
inputs, authority, dependencies, ownership, failure rules, and acceptance
methods. Report:

- `PASS` — implementation can start;
- `CONCERNS` — named non-blocking risks or later improvements remain; or
- `FAIL` — a missing prerequisite would make the current slice unsafe,
  dishonest, unusable, or unverifiable.

Concerns do not become blockers without a violated current acceptance condition
or concrete current risk. Sprint status is a derived view of authoritative work,
not a second tracker; validate or repair it from source records.

## Build, review, and walkthrough

`bmad-build` is the ordinary clarify → plan → implement → review → present loop
under handbook controls. `bmad-code-review` is exact-byte review;
`bmad-qa-generate-e2e-tests` produces changed-contract API or end-to-end
evidence; and `bmad-checkpoint-preview` guides a human from purpose and
acceptance to changed behavior, risks, and proof. A walkthrough is not approval
unless the reviewer has that authority and records a verdict.

## Correct course

On a material change signal, `bmad-correct-course` stops expansion at the next
safe boundary and compares the new fact with the accepted scope, architecture,
slices, and evidence. Preserve valid completed work. Then choose the smallest
honest correction: update the current artifact, re-slice remaining work, redo a
now-invalid decision, or abandon the candidate. Never rewrite history or relabel
a failed acceptance condition as later work.

## Retrospective

`bmad-retrospective` runs after an accepted epic or material incident. Compare
planned outcomes and controls with observed delivery, record causes rather than
blame, assign only concrete improvements with owners and triggers, and feed any
material change through correct-course or ordinary backlog authority. A
retrospective cannot retroactively approve the delivered change.

## Effects and evidence

This fallback creates or edits planning artifacts only when the governing task
authorizes them. It does not install BMAD, create personas, run party-mode agent
discussions, publish tracker items, mutate status fields, or start unattended
epic loops. Evidence is a right-sized artifact chain, readiness verdict,
source-derived status, exact-byte review/walkthrough record, and retained course
correction or retrospective decision when applicable.
