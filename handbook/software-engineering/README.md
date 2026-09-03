# Software Engineering Handbook

**Handbook version:** 1.5 (2026-09-03)
**Scope:** global, shared, and project-, provider-, tool-, and language-agnostic engineering guidance

## Purpose

This handbook supplies a small, durable set of defaults for changing software responsibly. It organizes work around explicit intent, proportionate risk, observable evidence, reversible delivery, and learning from failures. It is not a development methodology, a certification scheme, or a substitute for engineering judgment.

This shared handbook is intended for human practitioners and teams and for AI agent harnesses. It supports fixed iterations and continuous flow, including bounded autonomous execution.

The handbook separates:

- **normative rules**, which state required or recommended behavior;
- **explanation**, which gives rationale without creating another requirement;
- **examples**, which illustrate one possible implementation; and
- **project adapters**, which bind the generic rules to a repository, domain, toolchain, or operating environment.

The five chapters own the detailed rules. This index defines only their shared operating model.

## Applicability

Use this handbook for software work across conception, acquisition, design, implementation, verification, delivery, operation, maintenance, incident response, and retirement. Apply it to source code, tests, schemas, build and deployment definitions, dependencies, generated artifacts, and engineering documentation when they affect software behavior or assurance.

The rules scale with consequence rather than team size or process label. A one-line authorization change can be high risk; a broad mechanical rename can be low risk. The change MUST be classified before controls are chosen and MUST be reclassified when new facts increase its reach, irreversibility, uncertainty, or impact.

Autonomy never grants authority to access systems or secrets, take destructive action, publish, release, deploy, or accept residual risk. Those actions remain subject to higher-authority instructions, local controls, and explicit authorization.

## Precedence and local adaptation

Apply instructions in this order:

1. applicable law, regulation, safety constraints, and higher-authority system or user instructions;
2. explicit product, domain, contractual, and repository rules, including their declared sources of truth and executable gates;
3. an approved project adapter;
4. this handbook; then
5. non-normative examples and personal preference.

A more specific local rule overrides a generic handbook default within its scope. Local rules SHOULD strengthen or concretize the handbook rather than restate it. A conflict that weakens safety, authorization, privacy, security, evidence integrity, or a regulated control MUST be surfaced and resolved by an authorized owner; it MUST NOT be silently treated as ordinary precedence.

When equally authoritative instructions conflict, the affected action MUST pause, completed safe work MUST be preserved, and an explicit resolution MUST be obtained or located. Authority MUST NOT be invented.

## Risk tiers

The highest tier whose trigger applies MUST be selected, and its listed minimum control intent MUST be satisfied. Local risk schemes MAY rename or subdivide these tiers, but an adapter MUST preserve their control intent.

| Tier | Typical triggers | Minimum control intent |
|---|---|---|
| **R1 — Low** | Localized, well-understood, reversible change; no externally relied-on contract, sensitive data, privilege, persistence, or release-path effect | Focused inspection plus the smallest behavioral check that can disprove the change; record what was and was not exercised |
| **R2 — Moderate** | User-visible behavior, established interface implementation, dependency behavior, shared component, non-trivial state transition, operational setting, or artifact publication or release | Explicit acceptance criteria; relevant automated or runtime checks; boundary and regression consideration; peer review when local policy requires it |
| **R3 — High** | Authentication or authorization, secrets, privacy, public or cross-service contract, data migration, concurrency, availability, financial impact, build/release trust, difficult rollback, or broad blast radius | Named risk owner; independent review; positive, negative, failure, and rollback evidence as applicable; relevant full repository gate on the candidate revision |
| **R4 — Critical** | Safety-critical or regulated behavior, irreversible production action, root-of-trust change, destructive data operation, emergency security action, or impact beyond ordinary recovery authority | Explicit authorization; staged/fail-safe execution; independent security or domain validation; rehearsed recovery or containment; retained decision and evidence record |

Risk controls MUST be cumulative unless a documented exception says otherwise. Cost, urgency, or small diff size alone MUST NOT lower a tier. If classification is uncertain, the higher plausible tier MUST be used until evidence supports a lower one.

## Chapter selection

This index MUST be consulted first. Use it as a map rather than loading the
handbook corpus: inspect the selected primary chapter's headings and read only
the sections governing the current decision by default. Read the full primary
chapter only when the task spans it or an R3–R4 failure mode requires
chapter-wide controls. Secondary chapters remain section-level unless that same
test is met. A chapter or section SHOULD NOT be loaded merely because the work
is non-trivial or to add ceremony.

| Chapter | Choose as primary when the central work involves | Owns | Does not own |
|---|---|---|---|
| [1. Lifecycle and governance](01-lifecycle-governance.md) | scope, stakeholders, requirements, ownership, decisions, change control, operation, deprecation, or retirement | lifecycle state, decision authority, traceability, governance proportionality | internal design techniques, test mechanics, Git mechanics |
| [2. Architecture and code quality](02-architecture-code-quality.md) | boundaries, contracts, data or error models, dependencies, reliability, performance, maintainability, or structural change | design qualities, architecture decisions, implementation discipline, resource and failure behavior | test process, repository publication, delivery cadence |
| [3. TDD, testing, and debugging](03-tdd-testing-debugging.md) | new or changed behavior, defect repair, investigation, regression prevention, or confidence claims | test strategy, red–green–refactor, debugging evidence, deterministic and risk-based verification | CI policy, release authorization, work-item slicing |
| [4. Git, CI/CD, and security](04-git-ci-cd-security.md) | version control, review gates, automation, dependencies, artifacts, deployment, secrets, vulnerabilities, or supply-chain trust | change-set integrity, pipeline and release controls, secure development and provenance | product governance, architecture quality model, iteration planning |
| [5. Agile atomic delivery](05-agile-atomic-delivery.md) | decomposition, sequencing, incremental delivery, work coordination, handoff, feedback, or completion | coherent slices, bounded work, feedback loops, Definition of Done, evidence-bearing handoff | mandated sprint length, tracker taxonomy, branch strategy, test-tool syntax |

Common primary routes and section-level escalators:

- **Behavioral feature or bug repair:** use chapter 3 as primary. Consult chapter 1 §§1–4 when the outcome, acceptance contract, authority, or lifecycle state changes; the affected normative section of chapter 2 when the root cause or design changes a boundary, contract, state, dependency, resource, or failure model; chapter 5 §§1–2 when the work needs decomposition or staged usable slices; and the applicable GCS section of chapter 4 only when a repository, automation, security, artifact, or release boundary is actually engaged.
- **Architecture or public-contract change:** use chapter 2 as primary. Consult chapter 1 §§1–4 for material authority, acceptance, lifecycle, or risk decisions; the applicable claim or regression sections of chapter 3 for changed behavior; chapter 4 GCS-3–GCS-8 for affected integration, dependency, artifact, or release controls; and chapter 5 §§1–2 or §8 when safe slicing or incremental exposure is required.
- **Pipeline, dependency, artifact, or release change:** use chapter 4 as primary. Consult chapter 1 §§3–4 for approval, authority, or lifecycle consequences; chapter 2 §9 when application dependency architecture changes; chapter 3's applicable evidence section when behavior must be challenged; and chapter 5 §§8 or 14 only for incremental delivery or an evidence-bearing handoff.
- **Delivery-system or coordination change:** use chapter 5 as primary. Consult only the affected outcome or authority sections of chapter 1, design section of chapter 2, verification section of chapter 3, or integration/release control of chapter 4.
- **Documentation-only change:** use the chapter that owns the documented contract as primary. Load no additional full chapter unless the documentation itself changes another governed boundary; verification remains proportionate to the chance of misleading users or operators.

## Applicable procedure and skill preflight

Before responding or acting on a task, an executor MUST inspect the descriptors
of procedures, skills, playbooks, or equivalent reusable guidance whose
declared triggers plausibly match. The canonical router MUST resolve triggers,
scope, prerequisites, required dependencies, optional companions, and
conflicts; select the smallest compatible set with at most one primary workflow
expert; and load only the selected bodies and references. Applicable process
guidance MUST be applied before applicable implementation guidance, subject to
the precedence order above. A selected procedure already loaded in the current
uncompacted context need not be loaded again unless its source changed.

Automatic selection does not mean running every installed procedure. A
procedure definition SHOULD state its trigger, scope, exclusions, required
capabilities, side effects, authority boundaries, and expected evidence clearly
enough to distinguish applicability from mere topic overlap. An executor MUST
NOT load or apply a procedure solely because of topic overlap when its declared
trigger, scope, or prerequisites do not match the task. The executor MUST apply
the precedence order above, MUST NOT combine contradictory mandates, and MUST
surface a material conflict instead of silently choosing the more convenient
rule.

If an applicable procedure is unavailable, the executor SHOULD continue with
the handbook and reachable project controls when they can satisfy the same
outcome. It MUST pause only the action whose required control, tool,
independence, or authority cannot be satisfied, and MUST NOT fabricate a tool,
result, approval, or procedure invocation.

For example, an unavailable pre-acceptance reviewer blocks the review verdict,
acceptance, integration, and release that depend on that reviewer; it does not
by itself block authorized reversible local implementation that is intended to
produce stable bytes for review. A control explicitly required before design or
implementation still blocks that earlier boundary.

## Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described by BCP 14 only when they appear in all capitals.

- **MUST / MUST NOT** marks a requirement necessary to preserve the handbook's control intent.
- **SHOULD / SHOULD NOT** marks a strong default. Deviation requires a reason and an assessment of consequences, but not necessarily a formal exception unless local policy or the risk tier requires one.
- **MAY / OPTIONAL** marks a permitted choice, not an obligation.

Headings, explanatory prose, examples, checklists without capitalized key words, and adapter suggestions are non-normative unless a normative rule explicitly incorporates them. Examples MUST NOT be promoted into universal requirements without a stated rationale and source.

## Exception model

An exception is a bounded, reviewable decision to depart from a **MUST** or **MUST NOT** rule. It is not a way to relabel failed evidence as success.

An exception MUST:

1. identify the affected rule and exact scope;
2. state why compliance is infeasible or creates greater risk;
3. name the accountable approver or risk owner with authority for that scope;
4. record affected assets and stakeholders, risk, compensating controls, and substitute verification;
5. define an expiry, review event, or removal condition; and
6. remain discoverable with the change or in the project's declared exception register.

Exceptions MUST be approved before the affected acceptance or release decision, except for an authorized emergency process that requires prompt retrospective review. They MUST NOT override law, higher-authority instructions, access boundaries, or the obligation to report evidence truthfully. Repeated or long-lived exceptions SHOULD trigger a rule, architecture, or capacity review rather than indefinite renewal.

For an R1 or R2 change, a project MAY accept a concise decision record in the work item or review. R3 and R4 exceptions MUST have an independently reviewable durable record and explicit owner approval.

## Evidence model

Evidence supports a precise claim; it is not a synonym for effort, confidence, tool output, or a green badge.

For every material acceptance or release claim, the evidence record MUST contain:

- **Claim:** the observable behavior, property, or control being asserted.
- **Method:** the review, command, test, experiment, inspection, or production signal used to challenge the claim.
- **Context:** the relevant revision or artifact identity, environment, configuration, and time.
- **Result:** pass, fail, blocked, or not run, with the smallest useful output or artifact reference.
- **Coverage and limits:** what the method exercised, what it did not, and any residual risk.

Evidence MUST come from an observed action or artifact. An evidence record MUST NOT claim unobserved execution, silently omit a failure, report a check as passed when it was not run, or transfer a result to a different revision without establishing equivalence. Evidence SHOULD be reproducible and retained in proportion to risk. It MUST exclude or redact secrets, personal data, and unnecessary sensitive payloads.

The least expensive method that can falsify the claim SHOULD be preferred, with independent methods added when failure modes differ or the risk tier requires them. A full suite does not replace a targeted reproduction; a targeted check does not replace a required release gate. When a check cannot run, the blocker and residual uncertainty MUST be reported rather than replaced by an unrelated success.

## Project adapters

A project adapter turns this handbook into locally executable policy. It belongs with the project or governed environment, not in these generic chapters.

When a project defines project-wide operating instructions, its adapter MUST expose one discoverable canonical entry point. Bootstrap, context-discovery, and tool-specific instruction files MUST reference that entry point rather than maintain competing copies.

The adapter SHOULD register specialized procedures, scoped contracts, historical records, and executable gates with their authority boundaries. A project-wide instruction change MUST update the canonical source first and update dependent bootstrap references and consistency checks in the same governed change.

Adapters SHOULD define, where applicable:

- product and domain invariants, regulated controls, data classifications, and safety boundaries;
- accountable owners, review authorities, escalation paths, and sources of truth;
- the mapping from local risk labels to R1–R4 and any additional triggers;
- supported languages, frameworks, platforms, repository layout, and generated-code policy;
- exact build, format, analysis, test, coverage, packaging, and release commands;
- branch, commit, review, merge, signing, provenance, deployment, rollback, and incident procedures;
- CI/CD provider configuration, protected environments, evidence locations, and retention periods;
- API/versioning rules, compatibility windows, service objectives, resource budgets, and migration constraints;
- work-tracker fields, planning cadence, Definition of Ready/Done additions, and handoff format;
- the canonical procedure registry and primary mixture-of-experts router; approved provider allowlists, sources, versions, and integrity identities; expert roles and output contracts; dependency, conflict, context-budget, adjudication, update, rollback, and deprecation policy; required shared references; and adapter-specific trigger and routing checks; and
- a versioned exception register or link to the authoritative decision system.

An adapter MUST distinguish local requirements from examples, name its scope and owner, and keep commands and thresholds aligned with executable configuration. It MAY strengthen or specialize handbook rules. Any weakening MUST use the precedence and exception model above; an adapter MUST NOT silently redefine BCP 14 terms or claim compliance with an external standard.

If no adapter exists, the repository's actual conventions and executable gates SHOULD be discovered, the handbook defaults SHOULD be applied proportionately, and material ambiguity MUST be reported. A tool, threshold, workflow, or approval role MUST NOT be invented.

## Source register

[references.md](references.md) records the primary sources used to shape this architecture and its five chapter boundaries. Citations provide traceability, not automatic compliance or certification.
