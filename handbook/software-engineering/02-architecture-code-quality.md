# Architecture and code quality

## Purpose

This chapter defines durable, language-neutral defaults for turning intended behavior into understandable structures with explicit boundaries, contracts, failure behavior, and operating limits. Its goal is not a preferred architecture style. It is to make consequential design choices visible, keep change local, and ensure that software remains safe to evolve.

The chapter is informed by the concern- and viewpoint-based treatment of architecture in [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), the product-quality model of [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html), the lifecycle breadth of [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html), the Agile principle of continuous attention to technical excellence and simplicity, and OWASP guidance on useful, privacy-aware logging. These sources shape the decision model; citation does not claim conformance or import requirements not stated here.

## Applicability and ownership

Use this chapter when work changes or depends on:

- component, module, process, service, storage, trust, or ownership boundaries;
- data, command, event, API, configuration, or error contracts;
- dependency direction or the introduction, replacement, or removal of a dependency;
- state, time, randomness, concurrency, I/O, retries, or other side effects;
- compatibility, migration, rollout, rollback, or persisted representation;
- latency, throughput, capacity, memory, storage, connection, or cost behavior;
- diagnostic signals, audit-relevant events, privacy exposure, or maintainability; or
- a structural change whose consequences extend beyond one local implementation.

This chapter owns design qualities, architecture decisions, implementation discipline, and resource and failure behavior. It does **not** define test process or debugging mechanics (chapter 3), CI or release workflow (chapter 4), lifecycle authority (chapter 1), or delivery slicing (chapter 5). It may state what design evidence a change needs, but the applicable chapters determine how verification and delivery are performed.

## Decision criteria

Design is a tradeoff among concerns, not a contest for maximum abstraction. For each material choice, evaluate at least:

1. **Correctness:** Which invariants and externally observable behaviors must hold?
2. **Change locality:** How many independently owned or deployed elements must change together?
3. **Failure containment:** Where can a fault propagate, and how is partial failure represented?
4. **Compatibility:** Which callers, stored data, messages, or operators rely on the current contract?
5. **Operability:** Can expected states, failures, and resource pressure be distinguished without exposing sensitive data?
6. **Resource use:** What bounds apply at normal, peak, and degraded load?
7. **Security and privacy:** What authority and data cross the boundary, and what is the minimum necessary exposure?
8. **Maintainability:** Can a future maintainer find the governing decision, understand the dependency direction, and change one concern without reconstructing hidden assumptions?
9. **Reversibility:** Can the choice be changed or rolled back without destructive or coordinated intervention?

The decision SHOULD use the simplest design that satisfies the applicable concerns and known constraints. A more complex design requires a concrete benefit against an identified risk or requirement. A material SHOULD deviation requires a recorded reason and consequence assessment in the governing change or decision record; a formal exception is required only when local policy or the risk tier requires one. An aesthetic preference is not sufficient.

## Normative rules

### 1. Explicit architecture decisions

A decision is material when it establishes or changes a cross-boundary contract, dependency direction, data ownership rule, trust boundary, compatibility promise, irreversible representation, operational limit, or structure that multiple changes will build upon.

- Material decisions **MUST** record the problem and scope, relevant concerns and constraints, options considered, selected option, significant tradeoffs, consequences, owner, status, and replacement or review condition.
- The record **MUST** identify assumptions whose failure would invalidate the decision and link to the affected contracts or components.
- The record **MUST** be durable and discoverable from the affected system or change. R1–R2 decisions MAY be a concise code-adjacent or work-item note; R3–R4 decisions require an independently reviewable record.
- A decision record **MUST NOT** present a diagram, technology choice, or outcome without its rationale and boundary conditions.
- Architecture descriptions **SHOULD** show only the views needed by affected stakeholders—for example dependency, data, runtime, trust, or deployment views—rather than maintain a comprehensive model with no decision use.
- Superseded decisions **MUST** remain traceable to their replacements when historical context is needed to understand persisted data, compatibility, or risk.

Architecture documentation is evidence of reasoning, not proof that implementation conforms to it.

### 2. Modular boundaries, cohesion, and coupling

- Each module or component **MUST** have a coherent responsibility, explicit owned state where applicable, and an identifiable boundary contract.
- A boundary **MUST** expose the smallest surface needed by its consumers and **MUST NOT** expose mutable internals, storage details, or incidental implementation types unless those are deliberately part of the contract.
- Dependencies **SHOULD** point toward more stable policies or contracts, not toward volatile details. Deviations are acceptable when indirection would add more cost or ambiguity than it removes; record the reason when the dependency is cross-team, cross-process, or difficult to reverse.
- Cyclic dependencies between independently changeable units **SHOULD NOT** be introduced. If a cycle is retained, its required invariant, ownership, initialization order, and failure consequences **MUST** be explicit.
- Shared mutable state **MUST** have one declared owner and defined synchronization, consistency, and failure semantics. Mutation from unowned paths **MUST NOT** be allowed.
- Cross-boundary calls **MUST** make authority, data transfer, timeout or termination behavior, and failure outcomes visible at the abstraction level where they matter.
- A boundary **MUST NOT** be created solely to match a fashionable pattern, hypothetical scale, or organization chart. It should reduce a demonstrated coupling, ownership, safety, deployment, or change-locality problem.

A useful boundary lets one side change without requiring knowledge of the other's internals. A boundary that merely forwards every operation, shares the same data representation, and requires coordinated releases is usually separation in name only.

### 3. Simplicity, necessity, and duplication

KISS, YAGNI, and DRY are decision heuristics, not absolute laws.

- **KISS:** Implementations **SHOULD** minimize concepts, states, control paths, and configuration while preserving required behavior, safety, and clarity. “Simple” means easier to reason about under actual constraints, not merely fewer lines.
- **YAGNI:** Generalization, extension points, configuration, distribution, caching, and speculative scale mechanisms **MUST** be justified by a current requirement, measured constraint, or low-cost imminent need. Hypothetical future reuse alone is insufficient.
- **DRY:** A rule or invariant **MUST** have one authoritative owner. Repeated knowledge that can diverge **SHOULD** be consolidated or generated. Superficially similar code with different reasons to change **SHOULD NOT** be coupled merely to remove textual repetition.
- An abstraction **SHOULD** be introduced only when it gives a stable name to a proven concept, protects an invariant, or removes repeated change risk. If consumers need flags, downcasts, knowledge of implementations, or coordinated edits to use it, reconsider the abstraction.
- The implementation **MUST NOT** retain obsolete aliases, parallel paths, or dead abstractions after a clean cutover unless an explicit compatibility window requires them.

The governing question is “what knowledge must remain consistent?”, not “how can the fewest lines be written?” This interpretation aligns with the Agile principle that simplicity is the art of maximizing work not done, without treating omission of necessary quality work as simplicity ([Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html)).

### 4. Typed and versioned contracts

A contract includes accepted inputs, produced outputs, invariants, state transitions, errors, timing or ordering promises, authority, and compatibility behavior—not just a function signature or schema.

- Every externally relied-on or cross-boundary contract **MUST** define valid and invalid inputs, required outputs, failure categories, ownership, and compatibility expectations.
- Contract representations **SHOULD** be machine-checkable where the project environment supports it: for example schemas, interface definitions, constrained data types, or executable validators. When this is impractical, the deviation **MUST** identify how ambiguity and drift are controlled.
- Types and schemas **MUST** encode meaningful domain states and constraints when doing so prevents invalid or ambiguous states. A broad primitive, unstructured map, or stringly encoded state **SHOULD NOT** replace a known finite or constrained model merely for convenience.
- Validation **MUST** occur at the boundary where data changes trust, ownership, representation, or authority. Internal code MAY rely on established invariants only after that boundary has established them.
- A material contract and each communicated representation of it **MUST** have an identifiable revision. The compatibility policy **MUST** state which producer and consumer revisions may interact and how unsupported revisions fail.
- Optionality, defaults, units, encoding, ordering, uniqueness, nullability, identifier semantics, and unknown-field behavior **MUST** be explicit wherever misunderstanding can change behavior.
- Generated or duplicated contract artifacts **MUST** name an authoritative source and a drift-control mechanism. Competing hand-maintained definitions of the same contract **MUST NOT** be treated as co-authoritative.
- Internal type safety **MUST NOT** be presented as proof that serialized, untrusted, dynamically obtained, or version-skewed data satisfies the contract.

Version identifiers need not use a universal numbering scheme. They need to distinguish behavior sufficiently for compatibility, diagnosis, and migration decisions.

### 5. Deterministic core and controlled side effects

- Domain decisions and transformations **SHOULD** be deterministic for the same explicit inputs. Time, randomness, identity, locale, environment, mutable global state, network, storage, and process state **SHOULD** enter through explicit boundaries.
- Side effects **SHOULD** be concentrated at edges or behind narrow capabilities so policy can be reasoned about separately from effect execution.
- Effectful operations **MUST** define ordering, duplication, partial completion, timeout or cancellation, and retry semantics where those outcomes are possible.
- An operation that may be retried **MUST** either be idempotent for its declared scope or carry an explicit deduplication, reconciliation, or at-most-once decision. “Retry” **MUST NOT** be assumed safe.
- Concurrent mutation **MUST** define the protected invariant, coordination mechanism, consistency model, and behavior under contention or interruption.
- Nondeterminism that is intrinsic to the domain or required for security or performance MAY remain, but its source, bounds, and effect on reproducibility **MUST** be visible. It **MUST NOT** be hidden behind an apparently pure contract.

This rule favors functional cores and imperative shells where useful; it does not require functional programming, dependency injection frameworks, or process isolation.

### 6. Errors and failure behavior

- Expected failure modes **MUST** be part of the contract and represented distinctly enough for the caller to choose a correct response.
- Errors **MUST** preserve actionable context and causal information across boundaries while excluding secrets and unnecessary sensitive data.
- Code **MUST NOT** discard, blanket-catch, silently convert, or log-and-ignore a failure unless the contract explicitly defines that outcome and its safety has been assessed.
- Recovery **MUST** occur only at a layer with enough information and authority to restore an invariant, select a fallback, retry safely, compensate, or present the failure. Otherwise, the error **MUST** propagate with context.
- User-facing, machine-facing, and operator-facing error representations **SHOULD** be separated when their information and stability needs differ.
- Fallback behavior **MUST** state what property is degraded, how the degradation is observable, and when normal behavior resumes. A fallback **MUST NOT** silently weaken authorization, integrity, privacy, or a declared safety invariant.
- Cleanup and compensation **MUST** account for partial initialization and partial completion. The original failure **MUST NOT** be lost behind a cleanup failure.

### 7. Compatibility and migrations

Compatibility is a property of interacting versions and data, not a promise that all old behavior lasts forever.

- Before changing a relied-on contract or persisted representation, the change **MUST** identify affected producers, consumers, stored data, operators, and rollback paths.
- The change **MUST** state its compatibility direction and window: backward, forward, both, or deliberately incompatible.
- A migration **MUST** define preconditions, transformation or coexistence rules, progress and completion criteria, interruption behavior, verification signals, and rollback or forward-recovery strategy.
- When versions can overlap, changes **SHOULD** use an expand–migrate–contract sequence or another strategy that keeps every permitted version pair valid. A different sequence requires a reason and assessment of mixed-version risk.
- Destructive or lossy transformation **MUST NOT** begin until the authorized recovery strategy and point of no return are explicit.
- Readers **SHOULD** tolerate only explicitly allowed evolution. Silently accepting malformed or semantically unknown data is not forward compatibility.
- Writers **SHOULD NOT** emit a new representation until required readers can handle it or traffic/data isolation prevents incompatibility.
- Compatibility code, dual writes, feature switches, and legacy fields **MUST** have an owner and removal condition. Once the supported window closes, obsolete paths **SHOULD** be removed rather than becoming permanent parallel behavior.

Lifecycle approval and deprecation ownership belong to chapter 1; verification mechanics belong to chapter 3; release sequencing belongs to chapters 4 and 5.

### 8. Performance and resource bounds

- Material paths **MUST** identify the finite resources they consume and the behavior when a relevant limit is reached. Resources include time, memory, storage, bandwidth, connections, threads or tasks, queue depth, external calls, and monetary cost.
- Untrusted or externally controlled input **MUST NOT** cause unbounded allocation, recursion, concurrency, buffering, retries, cardinality, or work amplification.
- Latency, throughput, capacity, and availability claims **MUST** name workload, environment, percentile or aggregation, duration, data volume, and acceptable error behavior. A context-free “fast” or “scalable” claim is not a requirement.
- Performance work **SHOULD** address a measured bottleneck or an explicit budget. Speculative optimization is acceptable only when later correction would be prohibitively expensive; record that irreversibility rationale.
- A performance optimization **MUST NOT** weaken correctness, authorization, privacy, durability, or failure visibility without an approved tradeoff.
- Queues, caches, pools, batches, and retries **MUST** have bounds, eviction or shedding behavior, and failure semantics. Their defaults **MUST NOT** be treated as an architecture decision.
- Backpressure or load shedding **MUST** preserve the most important invariants and produce a distinguishable outcome; silent dropping is allowed only when it is an explicit contract.
- Resource ownership and release **MUST** be clear across success, failure, timeout, and cancellation paths.

### 9. Dependency discipline

This section governs architectural use of dependencies. Supply-chain acquisition, provenance, vulnerability response, and CI enforcement belong to chapter 4.

- A new dependency **MUST** solve a stated need better than a local implementation when lifecycle cost, failure modes, operational footprint, compatibility, and removal cost are considered.
- Only the smallest required public surface **SHOULD** be depended upon. Consumers **SHOULD NOT** rely on undocumented behavior, transitive availability, global initialization, or internal representations.
- Direct and runtime dependencies **MUST** be declared in the project's authoritative dependency mechanism. A required transitive dependency **MUST** be made direct rather than relied upon accidentally.
- The owner of a dependency integration **MUST** define upgrade and replacement responsibility, supported version or compatibility policy, failure behavior, and data or authority granted to it.
- A wrapper or adapter **SHOULD** be introduced when it protects a domain contract from volatile vendor details, constrains authority, or makes replacement materially safer. Pass-through wrappers with no policy or isolation **SHOULD NOT** be added.
- Duplicate dependencies with overlapping roles **SHOULD** be consolidated when doing so reduces material maintenance or runtime cost. They MAY remain when compatibility, isolation, migration, or meaningfully different requirements justify them; record the reason.
- Removing a dependency **MUST** also remove obsolete configuration, initialization, permissions, compatibility paths, and documentation within the change's authorized scope.

### 10. Observability and privacy

Observability is designed around decisions operators and maintainers need to make, not around collecting everything.

- Material components **MUST** expose enough signals to distinguish normal operation, expected rejection, dependency failure, resource pressure, degraded mode, and invariant violation where those states are operationally relevant.
- Signals **MUST** use stable event meanings and include the minimum correlation, contract revision, outcome, and timing context needed for diagnosis.
- Security-relevant or audit-relevant events **MUST** be represented as explicit outcomes rather than inferred only from free-form text.
- Logs, metrics, traces, diagnostics, and error reports **MUST NOT** contain secrets, credentials, private keys, session material, or unnecessary personal or sensitive data.
- Any permitted personal or sensitive telemetry **MUST** have a stated operational purpose and data classification, collect only the minimum data needed for that purpose, restrict access to least-privilege identities, use transport and storage protection appropriate to its classification, and enforce its defined retention and deletion policy.
- Attacker-controlled values carried in telemetry **MUST** be encoded or neutralized for the specific sink and kept distinct from record syntax so they cannot forge records or change record boundaries, fields, labels, or control sequences. Such values **MUST NOT** create unbounded labels, dimensions, cardinality, or cost.
- Security-relevant and audit-relevant records **MUST** use tamper-resistant or tamper-evident integrity controls, deletion protection, and access accountability proportionate to their risk and required retention.
- Redaction, hashing, or truncation **MUST NOT** be assumed to make data anonymous without an applicable privacy assessment.
- Diagnostic failure **MUST NOT** break the primary business invariant unless audit completeness is itself a required fail-closed control.
- Signal volume, retention limits, and behavior during telemetry backpressure **MUST** be bounded for material paths.

These rules apply the outcome of the [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)—useful security and operational records without prohibited or unnecessary sensitive data—without requiring a particular logging stack.

### 11. Maintainability

- Names and module structures **MUST** communicate domain meaning and ownership rather than incidental mechanics where the distinction affects future change.
- Non-obvious invariants, constraints, and “why” decisions **MUST** be recorded near the narrowest durable source that governs them. Comments **SHOULD NOT** restate syntax or preserve obsolete history available elsewhere.
- Public and cross-boundary behavior **MUST** have one discoverable source of truth. Documentation, schemas, configuration, and implementation **MUST NOT** knowingly contradict it.
- Change **SHOULD** leave the touched area no harder to understand than before. Necessary temporary complexity requires an owner, bounded scope, removal condition, and discoverable record.
- Dead code, unreachable configuration, stale compatibility paths, and misleading comments **MUST** be removed when their obsolescence is established and removal is within scope.
- Cleverness that depends on undocumented ordering, obscure language behavior, or implicit environmental state **SHOULD NOT** be used when a direct expression satisfies the same constraints.
- Generated code and generated artifacts **MUST** identify their source and regeneration path and **SHOULD NOT** be hand-edited unless the project declares that workflow.
- A refactor **MUST** preserve the declared external contract unless contract change and migration are explicitly in scope.

### 12. Reusable procedures and skills

A reusable agent procedure, skill, playbook, template, or workflow is an
executable policy surface and MUST satisfy the same clarity, authority, and
maintainability expectations as other cross-boundary contracts.

- It **MUST** have one coherent purpose and trigger metadata that states when it
  applies in observable terms. Topic keywords alone are insufficient when they
  would activate unrelated work.
- It **MUST** state prerequisites, stop conditions, prohibited effects,
  authority boundaries, expected evidence, and behavior when a required
  capability is unavailable.
- It **SHOULD** describe actions and invariants independently of one harness or
  tool, with platform mappings kept in scoped references or adapters.
- It **MUST NOT** weaken higher-authority safety, privacy, security, repository,
  or domain controls; require side effects that its trigger does not authorize;
  or invent a new source of product or risk authority.
- Its main path **SHOULD** remain concise. Detailed examples, templates, and
  platform mappings SHOULD be loaded only when their branch applies.
- A material revision **MUST** preserve a version or change identity, identify
  affected consumers, and remove or supersede obsolete parallel instructions
  through the lifecycle change-control rules.

Validation MUST challenge both selection and execution. At minimum, validation
of a changed material procedure MUST include a positive trigger case, a
near-miss non-trigger case, a conflict-precedence case, an
unavailable-capability case, and a pressure case that attempts a plausible
shortcut. Stateful or automatically injected procedures SHOULD also be
exercised after the environment's context-reset or compaction boundary.
Evaluation MUST inspect observable actions, prohibited effects, evidence, and
stop behavior rather than accept the procedure's prose or self-report as proof.

#### Governed improvement of procedures and skills

A procedure or skill MAY improve from experience only through a controlled,
versioned candidate. An executor MUST NOT rewrite its active governing
instructions, promote its own candidate, or treat task content, retrieved
material, tool output, or user-interface text as authority to change policy.

Improvement MUST start from an explicit request or from causal evidence of a
repeated or material procedure failure or near miss, sustained procedure
blockage, or measured recurring procedure cost. A single unexplained anomaly or
preference is insufficient. Before
editing, freeze the target identity, owner, affected consumers, objective,
mandatory invariants, prohibited effects, resource bounds, approval authority,
rollback, and stopping conditions.

The current and candidate versions MUST be evaluated on equivalent,
representative cases. Development cases used to shape the candidate MUST be
separate from held-out promotion cases. Prefer deterministic assertions for
objective behavior and use semantic evaluation only as supplemental evidence.
Mandatory safety, authority, privacy, negative, and compatibility cases are
hard gates; an aggregate score MUST NOT average away their failure.

Each iteration SHOULD make one smallest coherent edit. Prefer removing
ambiguity or replacing a faulty rule over accumulating reminders. Training or
evaluation inputs MUST be sanitized and MUST NOT expose credentials, private
data, or proprietary traces beyond the authorized evidence boundary.

Promotion requires meaningful aggregate improvement across the representative
baseline and candidate results, including meaningful held-out improvement, no
mandatory regression, no common-path or resource regression exceeding its
frozen bound, stable evidence appropriate to the risk tier and bound to the
exact candidate identity, a verified rollback or disable path, and authorized
approval. For R3–R4 changes, the proposer or optimizer MUST NOT be the sole
approver. Rejected candidates and reasons SHOULD remain discoverable when they
prevent repetition, but that rejection evidence is not adopted guidance. Only
a candidate that passes promotion and adoption MAY update durable procedure,
skill, or memory state. Every adopted candidate MUST retain its rollback or
disable path and a post-adoption observation point.

Stop and reject or revise the candidate when evidence is flaky, the evaluation
set no longer represents the intended workload, authority is unclear, a
mandatory case regresses, the iteration bound is reached, or further changes
produce no material improvement. Source acceptance, publication, installation,
and host activation remain separate controlled effects.

#### Scalable procedure-pack architecture

A scalable procedure pack SHOULD use three context tiers: a tiny discovery
descriptor, a compact routing index, and a task-local working set. The full
registry, chapters, provider packs, examples, and inactive expert bodies remain
cold storage. Startup MUST NOT preload them for possible future use. Resolution
SHOULD locate only matching descriptors, then load only the applicable
sections. Across compaction, retain concise decisions, outcomes, and evidence
rather than copied procedure bodies; re-read authoritative text when needed or
changed.


A growing procedure system SHOULD treat procedures as versioned capability
modules rather than concatenate whole packs into one prompt. One project or
environment MUST own the canonical registry and primary routing decision.
Supplementary packs MAY contribute individually selected capabilities, but
multiple active meta-routers MUST NOT compete for routing, command names,
authority, or lifecycle policy.

Each registered capability MUST have a collision-resistant canonical identity
that includes a namespace and name, plus a version and immutable source or
content identity. Its descriptor MUST state:

- owner, source, license, lifecycle state, replacement or deprecation path, and
  capability-specific rollback or disable path;
- phase or category, positive triggers, near-miss exclusions, scope, and
  context-loading budget;
- required dependencies, optional companions, conflicts, and ordering
  constraints;
- required tools, data, shared references, scripts, and behavior when any is
  unavailable;
- permitted side effects, required authority, inputs, outputs, stop
  conditions, and evidence; and
- applicable adapters and the higher-authority rules or contracts it cannot
  supersede.

The resolver MUST first apply handbook and project precedence, then determine
applicability from trigger, exclusion, scope, and prerequisite facts. It MUST
resolve required dependencies as an acyclic graph; reject duplicate identities,
cycles, missing required dependencies, and unresolved conflicts; and select
only the applicable capability bodies and references. Dependency order, pack
popularity, installation order, or a local priority field MUST NOT override the
authority model. The resolver SHOULD emit a bounded selection record containing
the chosen identities, versions, reasons, dependencies, rejected conflicts, and
unavailable requirements without copying the full procedures.

Required shared references and scripts MUST either travel with the capability
or be resolved through a declared, versioned, integrity-checked dependency.
Installing one capability MUST fail clearly at preflight when a required asset
is absent; it MUST NOT silently weaken the procedure. Registration or
resolution MUST NOT perform hidden network access, installation, telemetry,
hooks, state writes, execution, subagent injection, commits or resets,
publishing, release, or other effects. Acquisition and enablement of those
effects require their own explicit authority and supply-chain controls.

The registry, resolver contract, and generic validation corpus SHOULD remain
stable as packs are added. Pack-specific platform commands and integration
details belong in scoped adapters. Adding a capability SHOULD add a descriptor,
body, references, and tests—not a parallel precedence model or edits to every
existing capability.

The catalog MAY grow broad, but the per-task active set MUST remain sparse. At
runtime, the resolver SHOULD use descriptor-only discovery and a risk-scaled
loading budget. Catalog size MUST NOT determine body loading. A localized
low-risk task SHOULD use the governing core without an expert body unless a
specific trigger applies. The default SHOULD remain one primary workflow expert
and the fewest non-overlapping specialists needed for current risks; exceeding
the local budget requires a named reason. Unselected
bodies MUST NOT be loaded, and an unchanged selected body already present in
current uncompacted context SHOULD be reused.

When the host exposes a trusted compatible original skill for a selected
capability, the resolver SHOULD use that original and suppress its internal
fallback. Discovery MUST use the host's registered descriptors rather than
network or filesystem search. For consequential work, source/version/content
identity MUST satisfy the project adapter's trust policy. If the original is
absent, untrusted, incompatible, or unavailable, the resolver MAY use a
contract-equivalent internal fallback. It MUST NOT load both, activate an
external meta-router, or fail over after side effects without first reconciling
state at a safe boundary.

#### Governed mixture of expert procedures

The canonical handbook skill MAY operate as a workflow-level
mixture-of-experts router. The handbook core remains the always-applicable
governing expert; external sources contribute candidate procedures, not
co-equal authority. "Best combination" means the smallest compatible set for
the current outcome and risks, not loading all available experts.

For one task, the resolver SHOULD select at most one primary workflow expert
and MAY add specialist experts only for distinct contracts or risks. An
independent evaluator or adjudicator MAY be selected where the risk tier
requires one. Each selected expert MUST have a non-overlapping role, explicit
inputs and outputs, mutation ownership, stop conditions, and acceptance
evidence. Experts MUST NOT recursively route other experts, negotiate away a
conflict, self-approve a boundary requiring independence, or expand their own
authority. The coordinator or resolver owns composition and applies the
handbook's conflict decision.

Candidate outputs MUST be reconciled against shared invariants before
integration. A primary workflow answer does not outvote a security, domain,
provenance, or evidence failure. Disagreement without an authorized
deterministic rule MUST remain explicit and block only the dependent decision.
The selection record SHOULD identify the governing core, primary expert,
specialists, evaluator, versions, reasons, and disposition of every material
conflict.

An empirical optimization or autonomous-research expert has additional entry
conditions. Before it runs, an owner MUST approve a measurable objective,
frozen evaluation and holdout boundaries, invariant checks, an isolated
mutation allowlist, baseline, resource and attempt budgets, stop conditions,
result ledger, and rollback path. Experiments MUST remain reproducible and
comparable, and a retained candidate MUST still pass the normal functional,
security, quality, review, and delivery gates. Such an expert MUST NOT run an
unbounded loop, mutate shared history, change its own evaluator, install
dependencies, publish results, or reach production. Any later dependency
acquisition, publication, integration, or release MUST occur outside the expert
through the ordinary authorized supply-chain, review, and delivery workflow.

## Lightweight workflow

Use the smallest version of this workflow that can expose the material risks:

1. **Frame the change.** State the observable goal, affected concerns, invariants, owners, boundaries, and risk tier.
2. **Map the current design.** Locate the authoritative contracts, dependency direction, state ownership, side effects, consumers, persisted data, resource limits, and existing decisions. Do not design from an isolated file.
3. **Choose criteria before a solution.** Rank correctness, compatibility, containment, operability, resource, privacy, maintainability, and reversibility concerns. Record non-negotiable constraints.
4. **Compare viable options.** Include the simplest option and “do nothing” where meaningful. Reject options using explicit criteria, not style preference.
5. **Specify boundaries and transitions.** Define contracts, invalid states, error outcomes, effects, resource bounds, version interactions, migration stages, and diagnostic signals before relying on implementation details.
6. **Implement a clean path.** Reuse the project's established patterns, keep policy separate from effects where useful, migrate every authorized caller, and remove obsolete paths unless a compatibility window requires them.
7. **Challenge the design claims.** Collect the evidence below. Use chapter 3 for behavioral verification and chapter 4 for repository, dependency-security, and release gates.
8. **Close the decision.** Update the authoritative contract and decision status; name residual risks, compatibility debt, temporary mechanisms, and removal conditions.

R1 work may capture this in a change description. R2 work usually needs an explicit contract and design note. R3–R4 work requires named ownership, independently reviewable decisions, failure and recovery analysis, and evidence proportionate to blast radius.

## Evidence and architecture gates

A material architecture change is not ready for acceptance until the applicable claims have evidence tied to the candidate revision or artifact under the handbook evidence model.

| Claim | Minimum useful evidence | Gate failure example |
|---|---|---|
| Decision is justified | Decision record with concerns, alternatives, consequences, assumptions, and owner | Technology named with no problem or tradeoff |
| Boundary is real | Dependency/ownership view plus inspection showing only declared interactions | Hidden shared state or reverse import bypasses boundary |
| Contract is unambiguous | Versioned contract showing inputs, outputs, invariants, errors, optionality, and compatibility | Signature exists but invalid inputs or errors are unspecified |
| Effects are controlled | Effect inventory and failure analysis covering timeout, retry, duplication, cancellation, and partial completion | Retry added to a non-idempotent operation |
| Migration is safe enough | Version-interaction matrix, data transition plan, point of no return, and rollback/forward-recovery evidence | New writer activates before old readers can cope |
| Resources are bounded | Budget or limit table linked to workload, overload behavior, and observed measurement where a claim is quantitative | Unlimited queue or context-free benchmark |
| Dependency is warranted | Need-versus-alternatives note, authority/data exposure, compatibility policy, owner, and exit cost | Convenience dependency with no owner or removal path |
| Operation is diagnosable and private | Signal catalogue and sink-specific sample inspection showing outcomes, correlation, bounds, attacker-controlled-value neutralization, purpose and classification, least-privilege access, protected transport and storage, enforced retention and deletion, and security/audit-record integrity as applicable | Secret or uncontrolled sensitive data, forgeable record boundaries, attacker-controlled cardinality, or mutable audit evidence |
| Maintenance debt is bounded | Named owner and removal condition for temporary complexity or compatibility code | “Temporary” dual path with no end condition |

Evidence MAY be a concise diff inspection, generated contract comparison, static dependency view, measured experiment, runtime observation, migration rehearsal, or other falsifiable artifact. Exact test design belongs to chapter 3. Exact automation and required CI gates belong to chapter 4.

A gate **MUST** fail or produce an explicit exception when a required contract, owner, limit, migration condition, or recovery behavior is absent. A diagram, review approval, green pipeline, or benchmark alone **MUST NOT** substitute for the specific claim it does not exercise.

## Exceptions and deviations

The handbook-wide exception model applies to every **MUST** and **MUST NOT** in this chapter.

For a **SHOULD** or **SHOULD NOT** deviation, the change record **MUST** state, when material:

- the rule and affected scope;
- the constraint or tradeoff that makes the default unsuitable;
- consequences for coupling, compatibility, failure containment, resource use, privacy, and maintenance as applicable; and
- the owner and reconsideration trigger when the deviation creates ongoing cost.

Examples of potentially valid deviations include retaining duplication because two rules have independent ownership, exposing a dependency type because translation would add a lossy second model, accepting nondeterminism intrinsic to a protocol, or making a measured optimization before abstraction cleanup. These are not blanket waivers; the evidence must fit the exact scope.

No exception may conceal failed evidence, invent compatibility, authorize sensitive-data collection, or silently weaken an invariant. Emergency architecture debt **MUST** have an authorized scope, compensating control, expiry or review event, and durable follow-up record.

## Concrete anti-patterns

- **Architecture by noun:** selecting “microservice,” “event-driven,” “clean,” or another label before identifying concerns, boundaries, and costs.
- **Diagram as proof:** a desired-state picture that omits actual dependencies, shared state, version overlap, and failure paths.
- **Distributed monolith:** separately deployed units that require coordinated change, share representations or storage, and fail together.
- **Layer laundering:** pass-through layers that add names and mappings but protect no invariant and reduce no coupling.
- **God module or junk drawer:** unrelated responsibilities accumulated behind one convenient import or service.
- **Premature platform:** extension points, plug-in systems, generic repositories, or configuration added for uncommitted future consumers.
- **Wrong DRY:** coupling two coincidentally similar rules so either owner can break the other.
- **Stringly contract:** meaningful states, units, identifiers, or failures encoded in unrestricted strings or maps despite known constraints.
- **Version field theater:** carrying a version identifier while every reader assumes one representation and unsupported versions fail unpredictably.
- **Boolean blindness:** a success flag or null value erases distinct failure outcomes that require different caller actions.
- **Catch-and-continue:** swallowing an error, returning a plausible default, or logging success while an invariant is no longer known to hold.
- **Retry as recovery:** repeating a side effect without idempotency, deduplication, a budget, or terminal behavior.
- **Flag-day migration:** changing all producers, consumers, and stored data as one irreversible step without valid mixed-version states.
- **Permanent temporary path:** dual writes, legacy fields, feature switches, or adapters with no owner or removal condition.
- **Unbounded by default:** queues, caches, recursion, concurrency, labels, buffers, or input-driven work left to grow until failure.
- **Benchmark theater:** reporting best-case averages or microbenchmarks with no representative workload, variance, correctness check, or resource cost.
- **Dependency for convenience:** importing a large or privileged dependency for a small need without lifecycle and replacement analysis.
- **Wrapper theater:** a one-to-one façade that leaks every dependency concept and creates no policy boundary.
- **Log everything:** collecting complete payloads “for debugging,” exposing sensitive data and unbounded cost without a diagnostic decision.
- **Comments as archaeology:** stale narratives and restated code obscure the current invariant and authoritative decision.
- **Refactor smuggling:** changing public behavior, error semantics, data shape, or performance guarantees under a “no behavior change” label.

## Project-adapter hooks

A project adapter SHOULD make these rules executable by defining only the local details that matter:

- architecture decision location, required fields, owner roles, review threshold, and supersession convention;
- module/component ownership, allowed dependency directions, boundary-enforcement mechanism, and generated-code policy;
- authoritative interface/schema locations, contract validation mechanism, version naming, compatibility matrix, and deprecation window;
- domain invariants, identifier/unit conventions, allowed error taxonomy, and rules for unknown or invalid data;
- approved sources of time, randomness, configuration, identity, and I/O; concurrency and consistency expectations;
- migration mechanisms, mixed-version constraints, data backup or forward-recovery policy, and point-of-no-return authority;
- service objectives and representative workloads; latency, capacity, memory, storage, concurrency, queue, retry, timeout, and cost budgets;
- dependency selection criteria, ownership metadata, permitted authority/data exposure, version policy, and replacement expectations, while chapter 4 defines provenance and vulnerability controls;
- event naming, correlation rules, sink-specific encoding or neutralization and record-boundary preservation, data purpose and classification, least-privilege access, protected transport and storage, enforced retention and deletion, security/audit-record integrity, cardinality bounds, and telemetry-failure policy;
- complexity or analysis thresholds when they defend a stated maintainability risk, with an exception path rather than an arbitrary universal score; and
- exact evidence locations and local commands, with test commands delegated to chapter 3 and CI/release gates delegated to chapter 4.

For telemetry that permits personal or sensitive data or supplies security or audit evidence, a project adapter **MUST** bind the applicable controls above to enforceable mechanisms and evidence.

Adapters **MUST NOT** turn examples into universal framework mandates, require an architecture style without stated concerns, or claim that a tool score proves design quality. Thresholds and required views **MUST** map to a named risk or decision. Local rules that weaken a chapter requirement require the handbook exception path.

## Source traceability

The handbook's consolidated primary-source register is [references.md](references.md). This chapter relies particularly on:

- [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) for architecture descriptions organized around stakeholder concerns without mandating a notation, method, or tool;
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) for treating quality as a set of explicit product characteristics that must be specified and evaluated rather than asserted generally;
- [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html) for lifecycle breadth, including acquisition, development, operation, maintenance, and retirement consequences;
- [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html) for continuous attention to technical excellence, good design, and simplicity without importing a named delivery method;
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) for security- and operation-relevant logging that excludes secrets and unnecessary sensitive data; and
- [NIST SP 800-218, Secure Software Development Framework 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) for outcome-oriented secure design and third-party component discipline that can be adapted to organizational risk.

The public ISO pages provide catalogue metadata and abstracts, not the complete standards. This chapter does not claim ISO, NIST, OWASP, or Agile conformance. A project making such a claim must obtain the applicable full source, select and tailor its requirements, and produce the required evidence.
