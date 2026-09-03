# Lifecycle and governance

## Purpose

This chapter governs how software work is framed, authorized, accepted, changed, learned from, and retired. Its objective is to keep an observable outcome, an accountable owner, the applicable authority, and trustworthy evidence connected throughout the lifecycle.

It is methodology-neutral. It does not prescribe planning cadence, team structure, architecture or coding technique, test implementation, version-control commands, or delivery tooling.

## Applicability

Apply this chapter when work creates or changes any of the following:

- an intended outcome, requirement, acceptance condition, or stakeholder commitment;
- ownership, approval authority, risk acceptance, or a lifecycle state;
- an externally relied-on behavior, operational obligation, data obligation, or support commitment;
- a decision whose reversal would be costly, disruptive, or incomplete;
- an exception, waiver, incident disposition, deprecation, or retirement.

The [handbook index](README.md) defines precedence, R1–R4 risk tiers, normative language, the shared exception model, and the minimum evidence record. This chapter refines those models for lifecycle decisions; it does not replace them. A departure from a **SHOULD** or **SHOULD NOT** in this chapter MUST record the reason and expected consequences in the governing work or decision record.

## 1. Outcome, ownership, and acceptance

### 1.1 Governing record

In this chapter, a change is **material** when it is classified R2–R4 or establishes or changes decision or risk authority, an externally relied-on requirement or acceptance contract, a lifecycle state or support commitment, or authorization for an irreversible action. A project adapter MAY classify additional changes as material but MUST NOT weaken this threshold.

Before a material change is accepted for implementation, its governing record MUST identify:

1. the intended observable outcome and the problem or obligation it addresses;
2. the affected people, systems, assets, or commitments, including material exclusions;
3. the accountable outcome owner;
4. the authority that may accept the result and any authority that may accept residual risk;
5. observable acceptance criteria and the source of each externally imposed criterion;
6. the current and intended lifecycle state; and
7. the initial risk tier with its rationale.

For R1 work, these items MAY be a few lines in the normal work record. R2–R4 work MUST keep them as explicit, reviewable fields or sections. Discovery MAY begin before every item is known, but irreversible action and acceptance MUST NOT proceed while the required owner or authority is unknown.

An **outcome owner** is accountable for whether the change solves the stated need. An **implementer** performs work. An **acceptance authority** decides whether the evidence satisfies the criteria. A **risk owner** may accept bounded residual risk. One person MAY fill multiple roles for R1 or R2 when authorized by local policy. R3 and R4 decisions MUST preserve the independence required by the index and MUST name any required independent reviewer or domain authority.

### 1.2 Acceptance criteria and decisions

Acceptance criteria MUST be:

- stated as observable behavior, state, property, or constraint rather than an activity;
- specific enough to produce a pass, fail, blocked, or not-run result;
- traceable to an owner, stakeholder need, obligation, or explicitly chosen design intent; and
- revised when the intended outcome or material assumptions change.

“Implemented,” “reviewed,” “tests pass,” or “looks correct” MUST NOT stand alone as acceptance criteria. Those statements may describe evidence methods, not the outcome being accepted.

The acceptance decision MUST record the decision state, decision authority, time, applicable change identity, evidence references, unmet criteria, and residual risk. A decision MAY be **accepted**, **rejected**, **blocked**, or **conditionally accepted**. Conditional acceptance MUST identify each open condition, its owner, its due or review event, and the authority for proceeding; it MUST use an approved exception when a mandatory rule or criterion is not met.

Failed, blocked, stale, or missing evidence MUST NOT be relabeled as acceptance. If an authority accepts residual risk, the record MUST distinguish that risk decision from a claim that the unmet criterion passed.

### 1.3 Scale discovery and design commitment

Discovery depth SHOULD match uncertainty and consequence:

- A **spike** answers a bounded feasibility or learning question. It MUST state
  the question, probe boundary, stop condition, and how retained code or data
  will be disposed of or separately authorized. A spike result is evidence for
  a decision, not production acceptance.
- A **bounded change** modifies a known flow under an existing outcome and
  authority. It SHOULD inspect the current source of truth, state the short
  design and falsifier, and proceed without a new approval ceremony when it
  remains inside the approved scope and risk controls.
- An **architectural change** creates or materially changes a boundary,
  contract, ownership model, trust model, or long-lived dependency. It MUST
  compare viable approaches, record material tradeoffs and assumptions, and
  obtain the decision authority required by §§1.1–1.2 before implementation
  commits the material choice.

Discovery MUST step up when newly observed complexity changes the applicable
path, risk tier, authority, or acceptance criteria. It MUST NOT step down merely
because work has started or effort has already been spent. Questions SHOULD be
asked only when the answer changes a material choice that cannot be resolved
from authoritative context; an executor SHOULD otherwise choose the smallest
safe option and proceed within its delegated authority.

Discovery SHOULD use the least costly medium that makes the decision clear.
Spatial, interface, or interaction choices MAY use diagrams, mockups, or an
interactive visual companion when seeing alternatives exposes ambiguity that
prose would hide. A text-only decision SHOULD remain text. Opening an external
surface, publishing content, collecting telemetry, or disclosing project
material still requires the applicable authority and privacy controls, and an
accessible textual equivalent SHOULD accompany decision-bearing visuals.

### 1.4 Specification continuity

A durable specification artifact chain SHOULD be created only when it carries a
current decision across a real boundary such as multiple sessions,
contributors, repositories, public contracts, or consequential review. Clear
localized work SHOULD use its existing governing record rather than duplicate
the same intent in a new methodology.

When a specification, design, plan, task set, and evidence record coexist, their
authority and derivation MUST be explicit. Before implementation, unresolved
contradictions, requirements without planned coverage, and tasks without an
accepted outcome MUST be corrected or recorded as blocking the dependent work.
A checklist MAY challenge the quality of requirements but MUST NOT stand in for
behavioral evidence.

A proposed requirements change SHOULD have a stable identity, base revision,
and explicit added, modified, and removed outcomes. A modified requirement MUST
state the complete intended contract rather than only its changed fragment.
Before acceptance, the candidate MUST be reconciled against the governing
requirements, material design decisions, tasks, and runtime evidence. The
reconciliation MUST NOT redefine acceptance merely to match the implementation.
Only an accepted change may update canonical specifications; its prior state,
decision, and provenance MUST remain reconstructable.

## 2. Lifecycle impact assessment

A material change MUST assess its effects beyond implementation. The assessment MUST mark each locally applicable area as **affected**, **not affected** with a brief basis, or **unknown**:

- upstream needs, requirements, assumptions, and decision records;
- downstream consumers, interfaces, dependencies, and compatibility commitments;
- data creation, migration, retention, export, deletion, and evidentiary records;
- security, privacy, safety, regulatory, contractual, and accessibility obligations;
- operation, observability, capacity, recovery, support, and incident response;
- user, operator, support, training, and reference information;
- rollout, coexistence, deprecation, replacement, and retirement; and
- ownership, funding, service commitments, and third-party responsibilities.

An R1 assessment MAY collapse unaffected areas into one statement when its basis is evident. R2–R4 assessments MUST make affected and unknown areas individually visible. An **unknown** that could change the risk tier, authority, acceptance criteria, or irreversible consequences MUST be resolved or explicitly accepted by the authorized risk owner before the affected decision proceeds.

Lifecycle impacts MUST be reassessed when scope, assumptions, dependencies, observed behavior, intended users, operating environment, or recovery options materially change. A change MUST NOT be declared complete while an identified lifecycle obligation has neither been completed nor assigned to an owner with an authorized disposition.

## 3. Decision authority and traceability

Every material decision MUST identify:

- the decision and its scope;
- the person or role making it;
- the source and boundary of that authority;
- the information and evidence considered;
- any dissent, unresolved constraint, or residual risk material to the outcome; and
- the condition that will cause review, expiry, or supersession when the decision is not permanent.

Authority MUST NOT be inferred from availability, seniority, implementation responsibility, tool access, or silence. A decision maker MUST NOT approve beyond their delegated scope. When required authority cannot be located, safe reversible work MAY continue, but the affected authorization, acceptance, release, destructive action, or retirement decision MUST pause.

For R1 and routine R2 decisions, the governing work record MAY be the decision record. R3 and R4 decisions, and decisions that are costly to reverse, MUST retain a durable record that permits an independent reader to reconstruct the decision, its authority, its basis, and its conditions.

Material alternatives and tradeoffs SHOULD be recorded for decisions that constrain future options or impose long-lived obligations. If they are not recorded, the governing record MUST state why the decision is sufficiently routine or reversible and what consequence that omission may have.

Superseding a decision MUST preserve the prior decision, link the replacement, and state why the previous basis no longer governs. History MUST NOT be rewritten to make a changed decision appear to have been the original one.

## 4. Risk classification and control selection

The change MUST use the highest applicable tier in the [index risk model](README.md#risk-tiers). Its classification record MUST include:

- the selected tier and triggered characteristics;
- affected assets, stakeholders, and obligations;
- plausible failure consequences, reach, reversibility, and material uncertainty;
- required owners, authorities, reviews, evidence, recovery, and retention controls; and
- known residual risk and its owner.

The record MAY reference an approved local assessment rather than duplicate it. Size, familiarity, schedule pressure, sunk cost, or a successful check MUST NOT by itself lower the tier.

Classification MUST be revisited when evidence reveals broader reach, weaker recovery, new sensitive data, changed authority, an unanticipated dependency, a failed control, or a materially different failure mode. Controls already required MUST remain in force until the reclassification and its rationale are authorized. When several classifications apply, the strictest applicable control governs unless an approved exception explicitly resolves the overlap.

Risk acceptance MUST name the risk, consequence, likelihood or uncertainty basis, affected scope, compensating controls, owner, and review or expiry condition. “Accepted risk” without those elements is not a valid disposition.

## 5. Evidence integrity for governance decisions

Evidence used for authorization, acceptance, exception, incident closure, or retirement MUST satisfy the [shared evidence model](README.md#evidence-model) and MUST be linked to the exact claim and decision it supports.

In addition:

- the evidence record MUST identify the applicable change, artifact, configuration, or operating state precisely enough to prevent accidental reuse;
- the recorder MUST preserve the observed result, including failures, partial execution, blocked steps, and relevant limitations;
- transformed or summarized evidence MUST retain a reference to its origin and MUST NOT change the meaning of the source result;
- evidence MUST be refreshed when a material change invalidates its subject, method, environment, assumptions, or independence;
- acceptance MUST NOT rely on expired evidence or evidence from a materially different subject without a documented equivalence basis; and
- access and retention MUST be proportionate to risk while excluding secrets, personal data, and unnecessary sensitive content.

A link, status badge, signature, review, or approval proves only what its authenticated source actually establishes. It MUST NOT be presented as evidence for a broader claim.

For R3 and R4 decisions, the evidence set MUST make reviewer identity and required independence visible. A person MUST NOT attest that an independent control occurred when they only performed or observed the underlying work.

If evidence is lost, corrupted, inaccessible, or discovered to be misleading, dependent open decisions MUST be marked for reassessment. Affected accepted or operating changes MUST be evaluated by the accountable owner, with containment or re-verification proportionate to the possible consequence.

## 6. Exceptions and waivers

An **exception** or **waiver** is a bounded authorization to depart from a rule, criterion, or control; the terms are equivalent in this chapter unless a project adapter distinguishes them. Accepting an ordinary residual risk without departing from a requirement is a risk decision, not an exception.

Every exception MUST satisfy the [index exception model](README.md#exception-model). Its record MUST also state:

- whether it affects authorization, acceptance, operation, evidence, or retirement;
- the prohibited or unavailable normal control;
- the compensating control and substitute evidence;
- the maximum affected scope and how that boundary is enforced;
- the owner responsible for removal; and
- the event that restores compliance, forces renewal, or stops the affected activity.

An exception MUST NOT:

- claim that an unmet rule or failed criterion passed;
- grant authority the approver does not possess;
- override law, higher-authority instruction, access boundaries, or truthful reporting;
- apply by analogy to an unlisted change, asset, environment, or period; or
- remain active after its expiry or removal condition.

Emergency action MAY precede normal approval only through an authorized emergency path. The action MUST be limited to necessary containment or recovery, and the record MUST identify the invoking authority, facts known at the time, scope, evidence, retrospective review event, and restoration plan. Emergency status MUST NOT become an indefinite substitute for ordinary governance.

Repeated, renewed, or structurally similar exceptions MUST trigger an owner review of the underlying rule, architecture, resourcing, or obligation. The review may retain the rule, change the system, or amend local policy through proper authority; it MUST NOT silently normalize noncompliance.

## 7. Change control

The governing record is a controlled statement of intent, not an immutable plan. A proposed change to any of the following MUST reopen the affected decision before acceptance:

- intended outcome, scope, stakeholder, or externally relied-on behavior;
- acceptance criterion or source obligation;
- lifecycle impact, risk tier, owner, or decision authority;
- material dependency, data use, operating condition, or recovery assumption;
- required control, evidence method, exception, or residual-risk disposition; or
- deprecation, transition, or retirement commitment.

The update MUST identify what changed, why, who authorized it, which earlier evidence or decisions are invalidated, and what new work or evidence is required. The prior record MUST remain reconstructable.

Scope discovered during work MUST NOT be silently absorbed. It MUST be either incorporated through the applicable change authority, separated into another governed change, or explicitly excluded with its consequence recorded. Work MAY continue on unaffected reversible portions while a change decision is pending.

A stop condition MUST be defined before R3 or R4 irreversible actions. Crossing that condition, losing required authority, or invalidating a critical assumption MUST pause the affected action and invoke the declared containment, recovery, or escalation path.

## 8. Incident and defect feedback

An incident or defect record MUST connect the observed problem to the affected outcome, requirement, control, owner, and lifecycle state when those are known. Initial containment MAY be authorized separately from final remediation, but the distinction and each authority MUST be visible.

Disposition MUST be one of the project's declared states or, absent an adapter, an unambiguous equivalent of:

- corrected and verified;
- accepted as bounded residual risk by an authorized owner;
- duplicate of a linked governing record;
- not reproducible or not confirmed, with methods, limits, and a review trigger; or
- deferred, with rationale, owner, consequence, priority basis, and review event.

Closure MUST record the disposition authority, supporting evidence, affected scope, remaining impact, and any follow-on obligation. Lack of reproduction, elapsed time, low report volume, or absence of a current owner MUST NOT by itself establish that a defect is harmless or resolved.

After material incidents and recurring defects, the accountable owner MUST assess whether to update:

- requirements, acceptance criteria, risk triggers, or ownership;
- lifecycle impact assumptions and similar exposed assets;
- decision, exception, evidence, recovery, or retirement controls; and
- retained operational or support information.

The depth of analysis MUST scale with consequence and recurrence. Corrective action SHOULD address the enabling condition rather than only the observed symptom. If it intentionally does not, the disposition MUST record why symptom-level treatment is sufficient, what recurrence remains possible, and who accepts that consequence.

Incident and defect records MUST protect reporters and affected people from unnecessary exposure of personal or sensitive data. Records MUST focus on conditions, decisions, and controls rather than unsupported attribution of blame.

## 9. Deprecation and retirement

Deprecation communicates an intended end or restriction of support. Retirement ends the governed use or obligation. Neither state is established merely by stopping implementation or removing a visible entry point.

Before deprecation or retirement, the owner MUST identify, as applicable:

- the retiring asset, capability, version, data set, interface, or service and its owner;
- known consumers, dependents, stakeholders, and contractual or regulatory obligations;
- replacement, migration, coexistence, communication, support, and accessibility needs;
- data retention, export, transfer, deletion, and evidentiary-record obligations;
- access, credential, integration, infrastructure, monitoring, recovery, and third-party cleanup;
- the final acceptance authority, criteria, planned state, and residual risk; and
- the period or event after which recovery, rollback, or restoration is no longer promised.

The transition SHOULD provide notice and a recovery path proportionate to dependency, consequence, and reversibility. If it does not, the retirement record MUST state why immediate or irreversible retirement is authorized, who bears the consequence, and what containment or assistance remains.

An asset MUST NOT be marked **retired** until the authorized owner has evidence that retirement criteria are met, required consumers and obligations are resolved or formally excepted, prohibited access and operation have ceased, retained records remain accessible for their required period, and residual risk has an owner. Unknown consumers or obligations that could create material harm MUST be resolved or accepted through the applicable authority before retirement.

Post-retirement monitoring or inquiry handling SHOULD continue for a risk-based observation period when delayed effects are plausible. If omitted, the record MUST state the basis for concluding that delayed effects are not material and where later reports will be directed.

Retirement MUST preserve the minimum decision, evidence, exception, incident, and ownership history needed to explain what existed, why it ended, what obligations remain, and who is accountable for them. Retention MUST comply with applicable deletion and privacy obligations; “retain everything” is not a valid default.

## Lightweight workflow

Use the smallest record and control set that satisfies the selected risk tier:

1. **Frame:** state the outcome, affected scope, owner, authority, criteria, lifecycle states, and exclusions.
2. **Classify:** select the highest applicable risk tier and identify required controls and residual-risk ownership.
3. **Assess:** mark lifecycle impact areas affected, unaffected with basis, or unknown; resolve decision-blocking unknowns.
4. **Authorize:** confirm authority before irreversible, externally consequential, or risk-accepting action.
5. **Execute and observe:** keep evidence tied to the exact claims and subject; report failure, blockage, and limits truthfully.
6. **Control change:** reopen decisions when scope, assumptions, authority, risk, criteria, or evidence validity changes.
7. **Decide:** record acceptance, rejection, blockage, or bounded conditional acceptance with authority and residual risk.
8. **Operate and learn:** connect incidents and defects back to requirements, controls, decisions, and similar exposures.
9. **Transition or retire:** resolve consumers and obligations, verify end-state criteria, retain necessary history, and assign remaining risk.

A project MAY combine these steps in one work record. Separate forms or meetings are not required unless a local rule or risk tier requires them.

## Evidence and decision gates

A lifecycle gate passes only when its required fields and evidence are present and the named authority records the decision.

| Gate | Minimum checkable evidence |
|---|---|
| **Ready for consequential action** | Outcome, scope, owner, authority, acceptance criteria, lifecycle assessment, risk tier, and required controls are recorded; blocking unknowns are resolved |
| **Authorized** | Decision, authority source, scope, conditions, time, and governing record are linked |
| **Accepted** | Every criterion has a result; failures and limits are visible; change identity and evidence context match; residual risk and exceptions have valid owners and approvals |
| **Changed** | Superseded intent or decision remains traceable; invalidated evidence is identified; reclassification and new authorization are complete where triggered |
| **Incident or defect closed** | Disposition, authority, evidence, affected scope, residual impact, and feedback actions are recorded |
| **Retired** | Consumers and obligations are resolved or excepted; prohibited operation and access have ceased; retained records and residual ownership are confirmed |

For R1, one person and one concise record MAY satisfy several gates. R2 adds explicit criteria and lifecycle impact review. R3 and R4 MUST add the owners, independent review, durable records, and authorization required by the index. A gate MUST fail closed when a mandatory field, authority, or decision-critical evidence item is absent.

## Exceptions to this chapter

Use the shared exception process; do not invent an informal bypass. The exception record MUST identify the exact rule in this chapter, affected gate, risk tier, compensating control, substitute evidence, approver authority, owner, scope, and expiry or review event.

No exception can waive truthful evidence, applicable law, higher-authority instructions, or the need for an authorized decision maker. If those prerequisites cannot be satisfied, the affected decision remains blocked.

## Anti-patterns

- **Activity as outcome:** “build the feature” or “finish the migration” replaces an observable result.
- **Owner by proximity:** the implementer is assumed to own product consequences or accept risk without delegated authority.
- **Approval by silence:** notification, elapsed time, or lack of objection is treated as authorization.
- **Criteria after the result:** acceptance is rewritten to match what happened rather than reopening the decision.
- **Checkbox impact assessment:** every area is marked unaffected without a basis, or unknowns are hidden.
- **Diff-size risk:** a small implementation change is labeled low risk despite privilege, data, contract, or irreversible effects.
- **Green-badge evidence:** a status is cited without its claim, subject, context, result, or limits.
- **Exception as success:** a waived control or accepted risk is reported as passed evidence.
- **Perpetual emergency:** temporary authority or compensating controls continue without review or restoration.
- **Invisible scope growth:** discovered work is absorbed without updating outcomes, risk, criteria, or authority.
- **Incident amnesia:** a defect is patched or closed without correcting invalid assumptions, controls, or similar exposures.
- **Abandonment as retirement:** work stops while consumers, data, access, records, or obligations remain ownerless.

## Project-adapter hooks

A project adapter SHOULD bind this chapter to local reality by defining:

- authoritative locations for outcomes, requirements, decisions, evidence, exceptions, incidents, defects, and retirement records;
- named outcome, acceptance, risk, emergency, deprecation, and retirement authorities, including delegation limits and escalation paths;
- local lifecycle states and their mapping to the gates in this chapter;
- a mapping from local risk classifications to R1–R4, plus domain-specific escalation triggers;
- mandatory lifecycle impact areas, regulated obligations, protected stakeholders, and data classes;
- evidence identity, freshness, independence, access, and retention requirements;
- exception and emergency review periods, renewal limits, registers, and stop conditions;
- material-change thresholds and the decisions each threshold reopens;
- incident and defect dispositions, severity triggers, feedback owners, and closure authorities; and
- deprecation notice, compatibility, migration, recovery, data disposition, observation, and retirement criteria.

If the adapter omits a hook, use the index and this chapter proportionately; do not invent a role, threshold, authority, or obligation. If a **SHOULD** hook is intentionally omitted, the adapter MUST record why it is unnecessary and what consequence the project accepts.

## Source basis

These sources inform the chapter's control intent; citation does not establish conformance or import requirements not stated above.

- **ISO/IEC/IEEE 12207:2026, _Software life cycle processes_** — supports lifecycle-wide, methodology-neutral governance spanning conception through retirement. [ISO catalogue and public abstract](https://www.iso.org/standard/90219.html)
- **ISO/IEC 25010:2023, _Product quality model_** — supports specifying and evaluating quality outcomes rather than treating process completion as product acceptance. [ISO catalogue and public abstract](https://www.iso.org/standard/78176.html)
- **ISO/IEC/IEEE 42010:2022, _Architecture description_** — supports explicit stakeholders, concerns, decisions, and traceable descriptions without mandating a notation or tool. [ISO catalogue and public abstract](https://www.iso.org/standard/74393.html)
- **NIST SP 800-218, _Secure Software Development Framework (SSDF) v1.1_** — supports defined roles and responsibilities, risk-based practices, protected evidence, vulnerability response, root-cause feedback, and continuous improvement across lifecycle models. [NIST publication](https://csrc.nist.gov/pubs/sp/800/218/final) · [DOI](https://doi.org/10.6028/NIST.SP.800-218)
- **OWASP Logging Cheat Sheet** — supports attributable, tamper-aware, privacy-conscious operational evidence and the exclusion of secrets and unnecessary sensitive data. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- **IETF BCP 14** — supplies the normative meaning of uppercase requirement words used here. [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) · [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html)

The ISO links expose catalogue metadata and public abstracts, not the complete normative standards. A project claiming conformance MUST obtain and assess the applicable full standards, editions, tailoring rules, and required evidence through an authorized process. See the handbook [primary source register](references.md) for source scope and limitations.
