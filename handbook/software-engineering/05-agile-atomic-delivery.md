# 5. Agile atomic delivery

## Purpose

This chapter turns an intended outcome into small, coherent increments that can be inspected, accepted, and delivered without losing the outcome in handoffs or process. It favors early working behavior, bounded work in progress, short evidence-bearing feedback loops, and adaptation based on observed results.

“Agile” here describes those operating properties, not a required framework. A project MAY use fixed iterations, continuous flow, or another lifecycle. No sprint length, meeting schedule, tracker, role title, branch model, or multi-person or multi-agent ceremony is required by this chapter.

The source concepts are early and continuous delivery, working software as the primary measure of progress, simplicity, sustainable pace, and regular adaptation from the [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html); successive usable, user-visible increments from the Agile Alliance’s [Incremental Development](https://agilealliance.org/glossary/incremental-development/) guide; and the usable increment, coherent goal, transparency, inspection, adaptation, backlog refinement, and Definition of Done described by the [2020 Scrum Guide](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf). These sources motivate the rules; this chapter does not import an entire framework.

## Applicability and ownership

Apply this chapter when work must be decomposed, ordered, started, coordinated, handed off, accepted, delivered, or adapted from feedback. It applies equally to a single engineer or agent, a team, and a coordinated set of teams or agents.

The backlog, WIP-policy, delivery-cadence, and recurring-retrospective rules below apply to an ongoing delivery system. For an isolated R1 slice outside such a system, the built-in default is one active slice, with no separate backlog or WIP record and no recurring retrospective. A material delivery failure, near miss, or sustained blockage still requires the event-triggered learning review in §11.

This chapter owns:

- the coherence and size of delivery slices;
- readiness to start and the meaning of done;
- work-in-progress control, carryover, and feedback cadence;
- delivery-oriented handoffs and autonomy boundaries; and
- proportionate review of a slice as a unit of value.

Other chapters retain their boundaries. [Lifecycle and governance](01-lifecycle-governance.md) owns stakeholder authority, scope, and formal decisions. [Architecture and code quality](02-architecture-code-quality.md) owns design and implementation quality. [TDD, testing, and debugging](03-tdd-testing-debugging.md) owns verification strategy and test mechanics. [Git, CI/CD, and security](04-git-ci-cd-security.md) owns change-set integrity, pipeline controls, security, deployment authorization, and provenance.

## Operating definitions

- **Outcome:** an observable benefit, risk reduction, or learning decision for a named consumer or operator.
- **Vertical slice:** the smallest end-to-end change that produces an inspectable outcome across every necessary layer. “Vertical” does not require a user interface; an API consumer, operator, downstream system, or validated decision may be the beneficiary.
- **Task:** implementation work within a slice. A task may be necessary without being independently valuable or deliverable.
- **Increment:** one or more completed slices that work with what already exists and are usable within their stated release boundary.
- **Definition of Ready (DoR):** a lightweight entry policy establishing that a candidate slice is understood well enough to start responsibly. It is not a claim that uncertainty has been eliminated.
- **Definition of Done (DoD):** the shared minimum state a slice must reach before it may be represented as complete.
- **Work in progress (WIP):** started work that has not met the DoD, including work waiting for review, validation, a decision, or integration.
- **Delivery:** making a completed increment available to its intended feedback or use boundary. Delivery does not by itself authorize production deployment.

## Normative rules

### 1. Start from value and preserve one coherent goal

Each slice MUST state one coherent goal in terms of an observable outcome, affected consumer, or decision to be enabled. Acceptance criteria MUST describe evidence of that outcome rather than merely the production of files, layers, meetings, or activity.

A slice MUST be small enough to complete and evaluate in the project’s normal feedback interval. If it is not, it MUST be split by outcome, scenario, workflow step, policy case, data boundary, or reversible rollout boundary while preserving end-to-end behavior in each resulting slice.

A slice MUST NOT mix unrelated cleanup, opportunistic features, or independent policy changes. Necessary implementation tasks MAY span layers and specialties, but they remain parts of the same goal. Work discovered outside the goal SHOULD be recorded and ordered separately; it MAY be included only when excluding it would make the slice incorrect, unsafe, or materially more expensive, and that reason MUST be recorded with the slice.

The first implementation iteration for a behavior slice MUST seek the smallest safe, honest, usable end-to-end path that can satisfy the explicit current acceptance criteria and applicable risk-tier controls, before optional hardening or perfection. A bounded, honest subset is valid progress when it is usable within its declared boundary, omitted capabilities are explicit, and no claim implies that those capabilities exist.

### 2. Prefer usable vertical slices over layer completion

When working behavior is the deliverable, decomposition MUST follow usable end-to-end behavior. Documentation-layer, test-layer, schema-layer, backend-layer, interface-layer, “scaffold,” or “foundation” completion alone MUST NOT be represented as delivery of that behavior. Producing a plan, specification, documentation set, test shell, or implementation shell is not progress evidence for a working-behavior claim unless that artifact is itself the requested outcome.

A technical or learning slice MAY precede user-visible behavior when it independently resolves a material uncertainty, enables a necessary capability, or reduces a named risk. Such a slice MUST state the question or capability, bounded scope, observable result, decision owner, and the condition for integrating or discarding it. It MUST NOT be relabeled as delivered user value.

Horizontal decomposition MAY be used when an end-to-end slice would be unsafe, impossible under an external sequencing constraint, or less reversible. The exception path in this chapter applies, and the plan MUST identify the earliest subsequent vertical integration point.

Only a defect—including an unmet applicable control—that makes the stated slice unsafe, dishonest, or unusable within its declared boundary or violates explicit current acceptance criteria, including applicable risk-tier gates, MAY block that first working path. Findings about completeness, optimization, abstraction, additional evidence, resilience, or perfection that do not meet this test MUST be recorded and separately ordered for later iterations; they MUST NOT silently enlarge the current slice. This rule does not defer evidence or controls required by current acceptance criteria, the risk tier, safety, authorization, or truthful reporting.

Any proposed control that delays working behavior MUST name the concrete current failure or risk it addresses, use the least costly adequate control, and define the condition that ends the delay. A generic possibility, preference, or desire for future completeness is not sufficient.

Before implementation, the delivery owner MUST partition the intended work into
**first-working-slice requirements** and **later improvements**. The first set
contains only behavior and controls required for the current slice to be safe,
honest, usable, authorized, and compliant with its explicit acceptance criteria
and risk tier. Everything else starts in the later set. Starting an epic,
sprint, or broad work item MUST NOT be interpreted as authority to absorb every
possible hardening, replay, attestation, generalization, optimization, or future
threat-model concern into one change. An oversized work item MUST be split
before ordinary implementation rather than implemented as one progressively
expanding pull request.

After every review or failed gate, the delivery owner MUST classify each finding
against that partition before editing code. A blocker MUST cite the violated
current acceptance condition, applicable control, or concrete current
safety/correctness/usability/evidence failure. A finding that improves a future
boundary but does not satisfy that blocking test MUST be recorded separately and
MUST NOT ratchet the current slice's scope. Review depth MAY increase with risk;
the supported product boundary and current acceptance claim do not expand merely
because a reviewer can imagine another threat or future use.

A **scope-expansion circuit breaker** MUST stop ordinary implementation before a
repair adds a new subsystem, persistence or replay model, attestation mechanism,
provider, generalized abstraction, delivery surface, or threat model that was
not required by the first-working-slice partition. Work may resume only after
the existing slice is reduced, the addition is shown to be the least costly
adequate fix for a current blocker, or authorized scope is explicitly changed.
The delivery owner is accountable for applying this circuit breaker
proactively; a stakeholder MUST NOT have to monitor the implementation and
remind the executor to preserve working-feature-first sequencing.

Useful verified work from an oversized attempt SHOULD be retained when it still
serves the accepted slice cleanly. Sunk effort alone MUST NOT justify keeping
harmful complexity, and avoiding sunk-cost waste MUST NOT justify discarding
coherent tested behavior. Prefer finishing the bounded usable core, isolating or
removing only weight that harms it, and ordering the remainder separately.

### 3. Keep the backlog ordered and refinement proportional

For an ongoing delivery system, the active backlog MUST be a visible, ordered set of candidate outcomes, defects, risk reductions, and necessary enabling work. Ordering MUST reflect current value, risk, dependency, urgency, and learning—not age or sunk effort alone. The person or body authorized to change priorities MUST be discoverable.

Refinement SHOULD concentrate on the next plausible work rather than fully specifying distant inventory. A project deviating from this default MUST state the planning constraint that justifies earlier detail and how stale assumptions will be revisited. Refinement MUST split oversized items, expose dependencies and authority needs, identify acceptance evidence, and remove or re-evaluate obsolete work.

Backlog size, point totals, task counts, and documentation volume MUST NOT be used as evidence of delivered value.

### 4. Use a lightweight Definition of Ready

A slice is ready only when the people or agents expected to execute it can identify:

1. the coherent goal and intended consumer;
2. observable acceptance criteria or, for an experiment, the question and decision rule;
3. relevant scope boundaries, dependencies, constraints, and known authority limits;
4. the initial risk tier and the required review or evidence controls; and
5. a completion path small enough for the normal feedback interval.

The DoR MUST NOT require certainty that can only be obtained by doing the work, exhaustive design for distant possibilities, or estimates that have no decision use. Discovery work MAY be ready with uncertainty when it has a bounded question, budget or stopping condition, safe operating boundary, and expected decision.

An item that fails the DoR MUST be refined, split, investigated, or explicitly declined before ordinary implementation starts. An authorized incident or emergency path MAY start before all readiness information exists, but scope, authority, safety boundary, and the next decision point MUST still be explicit.

A readiness report MAY use **PASS**, **CONCERNS**, or **FAIL**. `PASS` means the
current slice can start. `CONCERNS` records non-blocking risks or later
improvements and MUST NOT block work unless a concern identifies a violated
current acceptance condition or concrete current safety, correctness,
usability, authority, or evidence failure. `FAIL` MUST name the missing
prerequisite and the exact work boundary it blocks.

### 5. Limit WIP and finish before starting

Within an ongoing delivery system, each delivery unit—an individual, agent pool, team, or service group—MUST have an explicit WIP policy appropriate to its capacity and risk. The policy MAY be a numeric limit or a rule such as “one primary slice per executor,” but it MUST count waiting work and make breaches visible. An isolated R1 slice uses the built-in single-active-slice default above and requires no separate WIP record.

New work MUST NOT be started when the applicable WIP limit is reached unless an authorized expedite condition applies. The default response to blocked or aging work SHOULD be to unblock, pair, review, reduce scope while preserving the goal, or stop the work—not to open more unrelated work. If a unit instead starts additional work, it MUST record why that action reduces overall risk or delay and when the WIP breach will end.

Urgent work SHOULD displace or pause lower-priority work explicitly rather than silently increase WIP. A WIP limit MUST NOT prevent immediate containment of a safety, security, privacy, availability, or data-integrity incident.

### 6. Define done as a usable, truthful state

A project’s DoD MUST be common and visible for work within the same product or release boundary. At minimum, a completed slice MUST:

- meet its observable acceptance criteria;
- be integrated with the current supported state and not leave required layers, callers, migrations, or cleanup knowingly incomplete;
- satisfy the risk-tier controls and applicable quality, verification, security, and delivery gates owned by the other chapters;
- include required user, operator, contract, configuration, and recovery information when the change affects them;
- carry evidence tied to the relevant revision or artifact and state material limits or residual risk; and
- be usable or releasable within its declared boundary without hidden follow-up work.

A slice that misses any applicable DoD condition MUST be described as not done, blocked, or exception-approved; it MUST NOT receive partial “done” credit. Review, a demonstration, elapsed iteration time, merge, or deployment alone does not establish done.

The DoD SHOULD be strengthened when escaped defects, repeated carryover, operational evidence, or changed risk exposes a missing control. If it is not strengthened, the responsible owner MUST record why another change better addresses the failure mode. The DoD MUST NOT be weakened to make current work appear complete.

### 7. Remain neutral between sprints and continuous flow

An ongoing delivery system MAY organize feedback using fixed iterations, continuous pull, scheduled release trains, or a hybrid. Whatever the model, it MUST provide:

- an ordered source of candidate work;
- a visible current goal and active WIP;
- a bounded interval or event for inspecting working results;
- a way to reorder or stop work as evidence changes; and
- a regular opportunity to improve the delivery system.

A cadence MUST NOT become a reason to batch completed value until an arbitrary ceremony. Conversely, continuous flow MUST NOT eliminate explicit goals, review points, stakeholder feedback, or retrospection.

### 8. Keep completed work continuously deliverable

Completed slices SHOULD be integrated and made available to their authorized feedback boundary promptly, in the smallest safe batch. A project that batches completed work MUST identify the economic, regulatory, operational, compatibility, or risk reason, plus the next release opportunity. Convenience or calendar habit alone is not sufficient when batching materially delays learning or increases risk.

“Continuously deliverable” means the current candidate can satisfy its applicable release controls on demand; it does not mean every change is automatically deployed to every environment. Feature exposure, deployment, migration, and publication MUST remain within the authorization and safety controls defined elsewhere.

An incomplete slice MAY be integrated behind a proven isolation mechanism only when it cannot affect unauthorized consumers, its incomplete state is visible, and removal or completion is owned. Hidden dormant code MUST NOT be used to claim the slice is done.

### 9. Close the feedback loop

Every delivered slice MUST name the feedback sought and the earliest reasonable observation point. Depending on the outcome, feedback MAY come from direct use, stakeholder inspection of working behavior, an experiment, operational signals, support evidence, or an acceptance decision.

Feedback MUST be compared with the slice’s acceptance criteria or hypothesis and MUST result in one of: accept, adapt, revert or contain, investigate, or intentionally stop. Material findings MUST update the backlog, risk classification, acceptance criteria, or operating controls as appropriate. Collecting metrics or holding a review without a decision or adaptation path does not close the loop.

Feedback collection MUST respect applicable privacy, security, safety, and data-minimization boundaries.

### 10. Handle carryover without disguising it

At a timebox boundary or expected completion point, unfinished work MUST remain not done. The responsible delivery unit MUST inspect why it carried over, re-evaluate value and risk, and then explicitly continue, split, reorder, stop, or return it to the backlog.

A carried slice MUST NOT be mechanically copied forward with stale scope, acceptance criteria, risk classification, or forecast. Splitting MAY isolate a completed end-to-end outcome from remaining work; it MUST NOT relabel completed technical layers as working behavior. Repeated carryover SHOULD trigger reduced WIP, smaller slices, dependency removal, capacity correction, or a DoR/DoD review. If none is adopted, the reason and accepted consequence MUST be recorded.

A material change signal during execution MUST trigger course correction at the
next safe boundary. The delivery unit MUST compare the new fact with the
accepted outcome, architecture, slices, risk, and evidence; preserve completed
work that remains valid; and explicitly update, re-slice, redo, or abandon the
affected candidate. It MUST NOT silently absorb scope, rewrite the prior record,
or relabel a failed current condition as later work.

### 11. Inspect and improve the delivery system

An ongoing delivery system MUST reflect at a regular cadence. Every delivery unit, including an isolated R1 executor, MUST perform a bounded learning review after a material delivery failure, near miss, or sustained blockage. The format MAY be asynchronous and MAY involve one person or agent; a meeting is not required.

A retrospective MUST use observed evidence, distinguish system conditions from blame, and produce either:

- one or more bounded improvements with an owner, intended effect, and observation point; or
- an explicit decision that no change is warranted, with the evidence supporting that decision.

Improvement work MUST enter the same visible ordering and WIP system as other work. Retrospective action counts MUST NOT substitute for evidence that flow, quality, safety, or value improved.

When the improvement changes a reusable procedure or skill, its retrospective
action is a candidate, not an automatically adopted rule. The owner MUST
evaluate the current and candidate versions against representative development
and held-out cases, retain mandatory safety and authority checks as hard gates,
and adopt only a materially better non-regressing candidate through normal
change control. A failed or inconclusive candidate SHOULD be rejected rather
than accumulated as additional instruction text. Chapter 2 §12 defines the
governed procedure-improvement contract.

### 12. Bound autonomy by goal, authority, and risk

An executing person or agent SHOULD be free to choose implementation sequence, local techniques, and internal task decomposition within the approved goal, architecture, repository rules, risk controls, and WIP policy. If that autonomy is constrained further, the constraint and its decision purpose MUST be explicit rather than inferred from status or tool access.

Autonomy MUST NOT be interpreted as authority to:

- change the intended outcome or acceptance criteria unilaterally;
- expand material scope or mix unrelated work into the slice;
- accept residual risk, approve an exception, or self-authorize a protected action;
- cross access, privacy, safety, deployment, publication, spending, or destructive-operation boundaries; or
- report unobserved evidence or declare incomplete work done.

When blocked by missing authority or a consequential ambiguity, the executor MUST preserve safe completed work, state the decision needed and its impact, and escalate to the authorized owner. It SHOULD continue only independent work that cannot prejudice that decision. If it instead proceeds on a reversible assumption, it MUST record the assumption, why delay posed greater cost or risk, the safe boundary, and the point at which confirmation is required.

Delegation MUST carry the goal, scope boundaries, acceptance criteria, risk controls, relevant context, expected evidence, and escalation path. The delegator remains accountable for integration and truthful completion. Multiple agents, reviewers, handoffs, or consensus rituals MUST NOT be required merely to demonstrate process; use them only when coordination, independence, expertise, capacity, or the risk tier calls for them.

#### Autonomous goal-mode execution

When an execution harness offers a persistent goal or continuous-work mode, a
delivery unit SHOULD use it for a Ready, bounded slice when uninterrupted
execution shortens feedback without weakening authority, WIP, verification,
review, or delivery controls. The objective MUST identify the governing work
record, observable outcome, current slice and exclusions, accepted contracts,
owned mutation boundary, dependencies, risk controls, expected evidence,
escalation path, and pause or stop conditions. Enabling goal mode is an
execution choice, not a lifecycle approval or acceptance decision.

Goal-mode work MUST count as WIP and MUST preserve one accountable integration
owner. It MUST pause at the next safe boundary when it reaches missing or changed
authority, a consequential unresolved decision, a protected or irreversible
action, an unavailable external prerequisite, a scope-expansion boundary,
conflicting shared mutation, or a review or release freeze that requires stable
bytes. The executor MUST preserve completed work and evidence, state the exact
prerequisite and impact, and MUST NOT convert the pause into completion,
acceptance, or permission to continue on a broader assumption.

Resuming a persisted goal MUST revalidate the governing record, current WIP and
priority, repository or artifact identity, owned scope, material decisions,
external prerequisites, and applicability of earlier evidence. Restored session
state alone MUST NOT authorize stale work. If the harness cannot pause safely,
restore state truthfully, or enforce the required ownership and effect
boundaries, the delivery unit SHOULD use the ordinary bounded workflow instead.

##### Coordinator-supervised goal topology

The default goal-mode topology SHOULD be one accountable coordinator supervising
one dedicated goal-running executor, followed by coordinator-started independent
reviewers. Goal mode is an execution loop on that executor; it does not by
itself create a reasoning-only manager or authorize a nested agent hierarchy.
The coordinator retains top-level interpretation, goal framing, scope and
contract decisions, mutation ownership, integration, review routing,
repository-wide verification, and delivery claims. The goal-running executor
directly performs its assigned edits and focused checks within the frozen
boundary.

A goal-running executor MUST NOT recursively delegate or spawn agents unless the
governing work explicitly defines a multi-agent topology, producer/consumer
contracts, non-overlapping ownership, validation ownership, and integration
authority. Convenience, continuous operation, or the availability of subagents
is not sufficient. Independent reviewers MUST be started and scoped by the
coordinator rather than by the implementation executor they review.

Decision work and implementation work SHOULD be routed by responsibility. Goal
framing, architecture or domain-policy decisions, source or evidence-policy
decisions, security analysis, acceptance design, and independent review belong
to a decision-capable coordinator or fresh decision agent. A goal whose
contracts, ownership, failure rules, and tests are frozen may use an
implementation-focused executor. If that executor encounters a consequential
ambiguity, it MUST pause rather than decide implicitly or switch roles merely
to continue. The coordinator MUST route the bounded question to a fresh
decision-capable agent, preserve the decision and evidence in the governing
record, revalidate shared state, and then resume or restart implementation.

Before an R3 or R4 implementation goal starts on a new contract, persistence or
revision boundary, evidence model, security boundary, or consequential state
machine, the coordinator or a decision-capable agent MUST freeze an adversarial
acceptance matrix. The matrix MUST cover the positive path; malformed,
unsupported, insufficient, conflicting, and unavailable states; exact boundary
and limit-plus-one cases; combined-failure precedence; interruption, retry,
rollback, and recovery; identity and provenance substitution; concurrency or
shared-mutation cases when applicable; historical compatibility; and every
external authority or temporal observation gate. Each row MUST state the
observable result, prohibited effects, and evidence method.

The implementation-focused goal MUST begin by adding or identifying
discriminating failing checks for that matrix before making the behavior green.
A passing happy path, broad suite, or prose contract does not compensate for a
missing adversarial row. If implementation exposes a consequential case not
resolved by the frozen matrix, the executor MUST pause and route the decision
back through the coordinator; it MUST NOT silently choose behavior and rely on
post-implementation review to design the contract. Independent review still
challenges the matrix and may identify genuinely missed current blockers, but
it SHOULD NOT be the first point at which ordinary named failure, precedence,
replay, or recovery semantics are specified.

After a goal finishes, the coordinator MUST capture its complete report and
observed focused evidence, end or release its mutation assignment, freeze the
candidate bytes, and start required independent reviews. A review blocker MUST
be classified against the current slice before repair. Any repair changes the
candidate and invalidates prior exact-byte verdicts; use a bounded repair goal
only after the findings and ownership boundary are frozen, then repeat the
applicable verification and independent review.

### 13. Make review low-ceremony and risk-based

Every slice MUST receive an author or executor self-review against its goal, scope, risk classification, DoD, and evidence before it is offered as done. Additional review MUST follow the shared risk tiers:

- **R1:** focused self-review plus the smallest behavioral check may be sufficient unless a local rule requires independence;
- **R2:** review SHOULD include another informed perspective when behavior is user-visible, the component is shared, or uncertainty is material; omission requires a recorded reason and consequence assessment;
- **R3:** independent review by a person or agent with relevant competence and no responsibility to justify the implementation MUST occur; and
- **R4:** the independently reviewable evidence and explicit domain, security, safety, or release authorities required by the project MUST approve within their scope.

Review MUST challenge the observable claim, slice coherence, unintended scope, failure and rollback implications, evidence limits, and unresolved risk. It SHOULD reuse inspectable artifacts and asynchronous feedback rather than add meetings or duplicate gates. If more ceremony is chosen, its risk-reduction purpose and exit condition MUST be clear.

Reviewers MUST assess the candidate against the stated slice and its applicable controls. They MUST NOT turn an optional future improvement into a release blocker unless the finding meets the blocking test in §2 or an existing explicit gate; a blocking finding MUST identify the violated acceptance condition or concrete current failure or risk.

Reviewer count, agent count, comments, approvals, or meeting attendance MUST NOT substitute for reviewer competence, independence where required, or evidence. An automated reviewer MAY supplement any tier, but it MUST NOT satisfy a required independent judgment unless the governing adapter explicitly establishes that equivalence for the decision and failure mode.

A guided walkthrough MAY help a human reviewer move from purpose and acceptance
criteria to changed behavior, risks, and proof. It is a navigation aid, not an
approval; it satisfies a review gate only when the reviewer has the required
competence and authority and records a verdict against the exact candidate.

### 14. Make handoffs evidence-bearing

When a slice changes executor, reviewer, team, or operating owner, the handoff MUST identify:

- the coherent goal and current state;
- the exact completed and remaining scope;
- relevant revision or artifact identities;
- observed evidence, failures, and what was not exercised;
- open decisions, dependencies, risks, and authority boundaries; and
- the next action and accountable owner.

A status label, verbal assurance, summary without artifact identity, or claim that “tests pass” without context is insufficient for a material handoff. Handoff depth SHOULD scale with risk and discontinuity; a low-risk same-session transfer MAY be a concise note. If a handoff is intentionally lighter, the sender MUST ensure the recipient can still verify state without reconstructing material context.

### 15. Make multi-agent execution an explicit topology

When multiple agents execute or review one outcome, the coordinator MUST define
the decomposition, shared contracts, file or artifact ownership, dependency
edges, validation ownership, and integration boundary before work starts.
Independent slices SHOULD run concurrently; shared mutations MUST have one
owner or be serialized. Agents MUST NOT invent producer/consumer contracts
independently or recursively delegate direction they do not own.

Reviewers MUST inspect one stable candidate. An interrupted, incomplete,
stale-revision, or partially delivered review has no verdict, and any reviewed
byte change invalidates the prior verdict. Repository-wide gates SHOULD run once
on the integrated stable candidate rather than redundantly in every worker.

Executor and model selection SHOULD use the least costly capability that can
reliably satisfy the role: mechanical work may use a focused executor;
cross-boundary integration needs broader context; consequential design,
security, domain decisions, and independent final review need the competence
required by their risk. Price or speed MUST NOT lower the required independence,
authority, or judgment, and the selected role SHOULD be explicit in the
assignment.

While agents are running, the coordinator SHOULD advance independent local work
rather than poll repeatedly. When genuinely idle, it SHOULD use bounded waits
and periodically reconcile live assignments so a lost or stalled executor is
detected. Absence of a report is not completion, and an active executor MUST NOT
be interrupted solely to produce a progress update.

Agent resources SHOULD follow a paired acquire/release lifecycle. After an
agent's result, evidence, and needed artifact references are captured, its
process, pane, tab, worktree, or other execution resource SHOULD be released
promptly. Active agents MUST NOT be terminated merely for cosmetic cleanup or a
timebox; let them reach a safe result or explicitly cancel them for a concrete
correctness, authority, or operational reason.

### 16. Make plans executable and recovery state durable

A separate implementation plan SHOULD be created only when dependency order,
handoff, interruption, or review complexity makes an in-chat or work-record
task list insufficient. It MUST remain subordinate to the governing outcome and
contract. An executable plan MUST identify:

- the goal, current state, scope and non-goals, authoritative specification,
  risk controls, and stop conditions;
- exact affected responsibilities, files or artifacts where known, interfaces
  produced and consumed, dependency edges, and integration ownership;
- coherent tasks with observable acceptance evidence and applicable focused
  commands or runtime scenarios; and
- required documentation, migration, cleanup, review, and delivery effects
  inside the task whose behavior needs them.

Plans MUST NOT contain placeholders, defer ordinary named failure semantics to
the implementer, prescribe nonexistent tools, or present speculative
scaffolding as a deliverable. Before execution, the coordinator SHOULD
preflight the plan for internal contradictions, uncovered acceptance criteria,
shared-file or interface conflicts, invalid task order, and instructions that
violate the governing contract. A plan defect MUST be ruled against the
authoritative specification and recorded; it MUST NOT silently redefine it.

Execution SHOULD keep one task or one same-shape mechanical batch as the
smallest reviewable unit. Independent units MAY run concurrently only after
their contracts, ownership, validation, and integration boundary are frozen.
Each delegated brief MUST include the task requirements, relevant global
constraints, owned mutation surface, inputs and outputs, acceptance evidence,
prohibited effects, escalation path, and report location. It MUST prohibit
nested delegation unless the accepted topology explicitly authorizes it.

Review repair SHOULD use a bounded loop: freeze the finding and correction
scope, assign one owner, run the focused evidence that challenges the repair,
and obtain scoped re-review on the changed candidate. Repeated non-convergence
MUST trigger the debugging architecture breaker in chapter 3 rather than
unbounded reviewer/fixer churn. A current-slice blocker cannot be parked or
outvoted merely because a round limit was reached.

Long-running, multi-agent, or compaction-prone execution MUST retain a recovery
ledger outside transient conversation memory. The ledger SHOULD identify the
governing plan or goal, task state, material rulings and assumptions, executor
assignments, exact revisions or artifacts, observed evidence, open findings,
and next action. It MAY live in harness state, an ignored owned workspace, or
the governing record; it MUST NOT create repository documentation or expose
sensitive data merely for bookkeeping. On resume, current authoritative state
and artifact identities MUST be revalidated before the ledger is trusted.

## Lightweight workflow

Use the smallest version of this loop that preserves the controls above:

1. **Frame the outcome.** Name one consumer, observable result, boundaries, and current risk tier.
2. **Slice vertically.** Find the smallest safe, honest, usable path through the necessary layers. Declare any bounded subset and omissions; separate and order optional hardening or perfection later.
3. **Make it ready.** Define acceptance evidence, dependencies, authority needs, DoD additions, and a completion path within the feedback interval. Any control that delays the working path must identify a concrete current failure or risk, use the least costly adequate response, and state when the delay ends.
4. **Pull within WIP.** Start only when capacity exists; expose waiting work and stop or escalate when the goal or authority becomes unclear.
5. **Build and integrate.** Establish the first working path before optional improvement, keep the change coherent, incorporate feedback early, and apply the technical controls from the relevant chapters.
6. **Challenge the stated claim.** Self-review every slice; add independent or specialist review according to risk. Observe the working result, distinguish blockers from later improvements, and do not overclaim omitted capability.
7. **Finish and deliver.** Meet the DoD, retain concise evidence, and make the increment available to its authorized feedback boundary.
8. **Adapt.** Compare feedback with the intended outcome, update ordering or controls, inspect carryover, and adopt a bounded improvement when evidence warrants it.

For an isolated R1 change, this may be one executor, one active slice, no separate backlog or WIP record, one focused check, one concise evidence note, and no recurring retrospective. Higher-risk work adds independence, authorization, retained evidence, staged exposure, or recovery controls because of its failure modes—not because of a prescribed methodology.

## Evidence and gates

The shared [evidence model](README.md#evidence-model) applies. The following gates are decision points, not required meetings or tracker states.

| Gate | Minimum question | Acceptable evidence examples | Fail or pause when |
|---|---|---|---|
| **Ready** | Can this outcome be started responsibly and finished within the feedback boundary? | outcome and acceptance statement; dependency and authority check; risk classification; bounded experiment rule | goal, consumer, authority, safe boundary, or completion path is materially unclear |
| **Pull** | Is there capacity under the WIP policy or isolated R1 default? | visible active-work count, explicit ongoing WIP policy, or the built-in isolated single-slice default | the applicable limit is reached without an authorized reason to displace or exceed it |
| **Slice integrity** | Is this the smallest safe, honest, usable end-to-end outcome without unrelated scope? | focused change inspection; working path demonstration; explicit subset and omissions; separately ordered later improvements | only technical or documentation layers are complete for a behavior claim; omitted capability is overclaimed; or optional work silently enlarges the slice |
| **Done** | Does the candidate meet every applicable DoD condition for the stated slice? | observed acceptance behavior; relevant chapter gates; revision-bound result and limitations | evidence is missing or belongs to another revision; follow-up required for the stated slice remains; an applicable gate failed; or optional future work is treated as blocking without a violated acceptance condition or concrete current failure or risk |
| **Delivery** | Can the increment reach its authorized feedback boundary safely? | release candidate identity; isolation or rollback evidence as applicable; authorization record for protected boundaries | exposure exceeds authority, isolation is unproven, or recovery needs exceed accepted risk |
| **Feedback** | What was learned and what decision follows? | observed use or signal; stakeholder acceptance; experiment result; backlog or control update | signals have no interpretation, decision owner, or adaptation path |

Evidence SHOULD be recorded once and referenced across gates rather than copied. For R1 and most R2 work, a compact record containing claim, method, revision, result, limits, and next decision is usually enough. R3 and R4 work MUST retain the independent reviews, authorizations, failure evidence, and recovery or containment evidence required by the shared risk model.

Flow measures such as item age, blocked time, WIP, cycle time, throughput, carryover frequency, escaped defects, or time to feedback MAY diagnose the system. They MUST NOT become targets that reward gaming, unsafe speed, oversized batching, or reclassification of unfinished work. Metrics SHOULD be disaggregated enough to reveal materially different work and interpreted with qualitative context. If a metric is used without those safeguards, its owner MUST document why misinterpretation risk is acceptably low.

## Exceptions

A departure from a MUST or MUST NOT in this chapter MUST follow the handbook’s [exception model](README.md#exception-model). A SHOULD or SHOULD NOT may be departed from only after recording the reason and assessing consequences; a formal exception is required when local policy or the risk tier says so.

Chapter-specific exception requirements are:

- **Horizontal-first work:** name the external constraint or safety reason, the independently verifiable result, the owner, the integration risk, and the earliest vertical integration point.
- **WIP breach:** name the expedite condition, displaced or paused work, added risk, decision authority, and the event that restores the limit.
- **Incomplete release boundary:** name the isolation mechanism, prohibited exposure, removal or completion owner, verification, and expiry or review event. It cannot be used to call the slice done if the DoD is unmet.
- **Batched delivery:** name the binding constraint, batch boundary, next release opportunity, and controls for accumulated integration and rollback risk.
- **Reduced review:** permitted only below a tier that requires independence; name the omitted perspective, reason, substitute challenge, and residual uncertainty.

Urgency, a deadline, sunk effort, small diff size, a passing broad test suite, or the use of multiple agents is not by itself an exception rationale.

## Anti-patterns

- **Layer masquerading as value:** calling a schema, backend, interface shell, test scaffold, or documentation set a delivered feature when no requested behavior works end to end.
- **Perfection before function:** delaying the first safe, honest, usable path for non-blocking completeness, optimization, abstraction, extra evidence, resilience, or polish instead of ordering that work later.
- **Review by imagined scope:** blocking the stated slice on optional future capabilities or controls without a violated current acceptance condition or concrete current failure or risk.
- **Document waterfall:** assigning separate requirements, design, implementation, test, and documentation “slices” whose only integration and behavioral proof is deferred to the end.
- **Everything is ready:** admitting vague items, then discovering the consumer, authority, or acceptance rule only after work has spread.
- **Ready means frozen:** using the DoR to prohibit learning or treating an estimate as a promise rather than revising the plan from evidence.
- **Done by declaration:** closing work because time expired, a review occurred, code merged, or most tasks completed while required behavior or gates remain.
- **Carryover normalization:** copying unfinished work forward without examining size, blockage, value, risk, or capacity.
- **Busy-system optimization:** maximizing utilization or parallel starts while review queues, integration delay, and feedback time grow.
- **Priority by interruption:** adding every urgent request without explicitly stopping, displacing, or reordering existing WIP.
- **Ceremony as evidence:** counting stand-ups, planning sessions, agents, reviewers, approvals, or reports instead of observing the outcome.
- **Autonomy without authority:** allowing an executor to expand scope, accept risk, cross a protected boundary, or self-approve because it can perform the action technically.
- **Delegation by filename:** splitting work by documents or components without giving each executor the outcome, boundaries, acceptance evidence, and integration owner.
- **Demo theater:** presenting prepared output while avoiding the actual working path, failure case, or current integrated state.
- **Metrics as quotas:** optimizing points, velocity, throughput, coverage, or cycle time at the expense of value, quality, safety, or truthful status.
- **Retrospective archive:** repeatedly recording the same issue without an owned experiment, observation point, or explicit decision not to act.
- **Continuous delivery conflated with deployment:** either bypassing authorization in the name of speed or withholding safe feedback because production deployment is not yet allowed.

## Project-adapter hooks

A project adapter SHOULD bind this chapter to the local environment without copying it. Define only what makes the generic control executable:

- the product or service boundary, intended consumers, value signals, and authorized priority owner;
- the normal feedback interval or triggering events, whether using sprints, continuous flow, release trains, or a hybrid;
- the backlog source of truth, refinement horizon, aging or stale-work policy, and dependency representation;
- the DoR and DoD, including risk-tier additions and links to executable quality, security, evidence, and release gates;
- the WIP policy for each delivery unit, how waiting work is counted, expedite conditions, and who may authorize a breach;
- the local meaning of a vertical slice, with representative good and rejected decompositions for the product;
- handoff fields, artifact and revision identity format, evidence location, and retention period;
- feedback sources, decision owners, acceptable data handling, and the conditions for accept, adapt, contain, revert, or stop;
- carryover inspection triggers and the authority to split, reorder, abandon, or rescope work;
- retrospective cadence or event triggers, improvement ownership, and observation method;
- autonomy boundaries for people and agents, protected operations, escalation paths, and assumptions that require confirmation;
- the mapping from R1–R4 to self-review, peer, independent, specialist, and approval requirements; and
- locally authorized exceptions, their approvers, expiry rules, and register.

Adapters SHOULD prefer links to authoritative tracker configuration, repository policy, executable gates, and operating procedures over prose duplication. They MUST NOT turn examples into universal requirements, require multi-agent execution without a risk or coordination need, weaken the shared exception model silently, or claim that framework terminology establishes compliance.

## Source notes

- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) supports early and continuous delivery of valuable software, frequent working results, sustainable pace, technical excellence, simplicity, motivated and self-organizing teams, and regular adjustment.
- [Agile Alliance: Incremental Development](https://agilealliance.org/glossary/incremental-development/) distinguishes successive usable, user-visible vertical increments from completing technical components in sequence.
- [The Scrum Guide, November 2020](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf) provides the source concepts of a single coherent goal, a usable verified increment, an ordered and refined backlog, Definition of Done, transparency, inspection, adaptation, and retrospection. This handbook deliberately does not universalize Scrum’s accountabilities, events, or timeboxes.
- The editions, access date, and limits of these sources are recorded in the handbook’s [primary source register](references.md#incremental-and-atomic-delivery). Citation supplies provenance; it does not by itself establish conformance or replace project-specific evidence.
