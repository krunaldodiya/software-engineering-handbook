# Primary source register

**Register date:** 2026-09-03

This register contains primary standards, specifications, official practice guides, and versioned workflow sources used to shape this handbook's shared model and five chapter boundaries. The “Used for” notes identify each source's limited contribution; they do not import an entire external document as a handbook requirement. Access dates are given for living or undated web publications.

## Normative language

- **IETF, RFC 2119, _Key words for use in RFCs to Indicate Requirement Levels_ — March 1997.** [RFC Editor](https://www.rfc-editor.org/rfc/rfc2119.html). Used for the base meanings of MUST, SHOULD, and MAY.
- **IETF, RFC 8174 / BCP 14, _Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words_ — May 2017.** [RFC Editor](https://www.rfc-editor.org/rfc/rfc8174.html). Used for the rule that BCP 14 meanings apply only to all-capital key words.

## Lifecycle, governance, architecture, and quality

- **ISO/IEC/IEEE 12207:2026, _Systems and software engineering — Software life cycle processes_, Edition 2 — published 2026-04-29.** [ISO catalogue and public abstract](https://www.iso.org/standard/90219.html). Used to set the handbook's lifecycle breadth and its methodology-neutral, iterative, incremental applicability.
- **ISO/IEC 25010:2023, _Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model_, Edition 2 — published 2023-11-15.** [ISO catalogue and public abstract](https://www.iso.org/standard/78176.html). Used to separate product-quality concerns from process mechanics and to require quality claims to be specified and evaluated.
- **ISO/IEC/IEEE 42010:2022, _Software, systems and enterprise — Architecture description_, Edition 2 — published 2022-11-07.** [ISO catalogue and public abstract](https://www.iso.org/standard/74393.html). Used to distinguish architecture concerns and descriptions from mandated notations, methods, formats, or tools.

## Testing and debugging

- **ISO/IEC/IEEE 29119-2:2021, _Software and systems engineering — Software testing — Part 2: Test processes_, Edition 2 — published 2021-10-28.** [ISO catalogue and public abstract](https://www.iso.org/standard/79428.html). Used to make testing lifecycle-model-independent and scalable across governance, management, and implementation.
- **Agile Alliance, _Test-Driven Development_ glossary — living guide, accessed 2026-08-15.** [Agile Alliance](https://agilealliance.org/glossary/tdd/). Used for the test-first, red–green–refactor practice boundary; it does not make TDD the only permissible verification method.
- **Git project, `git-bisect` manual for Git 2.54.0 — 2026-04-20 documentation release, accessed 2026-08-15.** [Git documentation](https://git-scm.com/docs/git-bisect/2.54.0). Used for evidence-driven narrowing of regressions rather than guess-based debugging.

## Secure development, delivery, and supply-chain integrity

- **NIST Special Publication 800-218, _Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities_ — final, 2022-02-03.** [NIST CSRC](https://csrc.nist.gov/pubs/sp/800/218/final) · [DOI](https://doi.org/10.6028/NIST.SP.800-218). Used for integrating outcome-oriented secure practices into any software lifecycle and for scaling implementation to organizational risk.
- **OWASP Application Security Verification Standard 5.0.0 — released 2025-05-30.** [OWASP project page](https://owasp.org/www-project-application-security-verification-standard/) · [versioned source](https://github.com/OWASP/ASVS/tree/v5.0.0). Used for scoped, version-qualified, verifiable application-security requirements; web-application-specific controls require a project adapter.
- **OWASP Logging Cheat Sheet — living guide, accessed 2026-08-15.** [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html). Used for evidence and operational logging that is useful without disclosing secrets or unnecessary sensitive data.
- **SLSA Specification 1.2 — versioned specification, publication date not stated on the version page; accessed 2026-08-15.** [SLSA 1.2](https://slsa.dev/spec/v1.2/) · [source requirements](https://slsa.dev/spec/v1.2/source-requirements) · [build requirements](https://slsa.dev/spec/v1.2/build-requirements). Used to distinguish source integrity, build integrity, provenance, and verification, and to scale supply-chain assurance by explicit levels rather than a provider-specific pipeline.

## Incremental and atomic delivery

- **Manifesto for Agile Software Development, _Principles behind the Agile Manifesto_ — 2001, accessed 2026-08-15.** [Official manifesto site](https://agilemanifesto.org/principles.html). Used for early and continuous delivery, short feedback intervals, working-software evidence, sustainable pace, technical excellence, simplicity, and regular adaptation without imposing a named methodology.
- **Ken Schwaber and Jeff Sutherland, _The Scrum Guide: The Definitive Guide to Scrum_ — November 2020.** [Official PDF](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf). Used for the increment, Definition of Done, transparency, inspection, and adaptation concepts; sprint events and accountabilities are not universal handbook mandates.
- **Agile Alliance, _Incremental Development_ glossary — living guide, accessed 2026-08-15.** [Agile Alliance](https://agilealliance.org/glossary/incremental-development/). Used to define delivery as successive usable slices rather than phase-only partial products.
- **Git project, `git-add` manual for Git 2.54.0 — 2026-04-20 documentation release, accessed 2026-08-15.** [Git documentation](https://git-scm.com/docs/git-add/2.54.0). Used for deliberate selection and inspection of the content of a change set; exact commands remain adapter material.

## Agentic workflow practice sources

### Active provider status in the canonical handbook mixture

The `software-engineering-handbook` skill is the only primary router. The
portable adaptations below are active. For each selected capability, a trusted
compatible original skill is preferred when already registered; otherwise the
main skill loads its internal fallback. It never loads both.

| Expert source | Status | Bounded role |
|---|---|---|
| Handbook core | Active governing core | Precedence, risk, authority, evidence, architecture, testing, delivery, and acceptance |
| Superpowers 6.3.0 | Active adapted capabilities | Discovery, isolation, planning, execution, debugging, verification, review, and procedure validation |
| Ponytail 4.9.0 | Active original-preferred fallback | Comprehension-first simplicity, over-engineering review/audit, and deliberate-debt ledger |
| Agent Skills 0.6.8 | Active original-preferred fallbacks | Requirements/planning, context/sources, interfaces/UI, and quality/operations capability groups |
| Understand Anything 2.9.4 | Active original-preferred bounded fallback | Task-scoped structural comprehension, architecture orientation, and advisory change impact |
| autoresearch at the pinned revision below | Active original-preferred bounded fallback | Finite empirical optimization under a frozen protocol; no integration or release authority |
| GitHub Spec Kit 1.0.0 | Active original-preferred fallback | Durable spec chains, clarification, artifact analysis, implementation convergence, and bounded idea/bug workflows |
| OpenSpec 1.11.0 | Active original-preferred fallback | Lightweight brownfield change packets, requirement deltas, verification, and provenance-retaining archive |
| BMAD Method 6.11.0 | Active original-preferred fallback | Right-sized agile planning, readiness, course correction, status, walkthrough, and retrospective |

Hindsight remains outside this mixture because it is a memory layer, not a
software-development workflow expert.

#### obra Superpowers

- **obra, _Superpowers_ 6.3.0 — commit
  `86babb696875227929e85420f287d6309374b93f`, accessed 2026-09-02.**
  [Versioned source](https://github.com/obra/superpowers/tree/86babb696875227929e85420f287d6309374b93f).
  The pinned `LICENSE` is MIT.
  Used for applicable-skill preflight, scaled discovery, root-cause debugging,
  claim verification, isolated workspaces, review handling, executable plans,
  coordinated agents, recovery ledgers, and procedure validation. The provider
  meta-router is not adopted.

- **obra, _Superpowers_ cross-harness package surfaces — commit
  `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, accessed 2026-09-03.**
  [Versioned source](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797).
  Used only as a compatibility reference for current harness manifest locations
  and install entry points. The handbook package does not adopt its startup
  body-injection hooks; adapters register the small discovery entry point and
  preserve on-demand loading.

| Superpowers capability | Handbook fallback |
|---|---|
| `using-superpowers` | Main skill router and README applicable-procedure preflight; original meta-router prohibited |
| `brainstorming` | Chapter 1 §1.3 and chapter 2 lightweight workflow |
| brainstorming visual companion | Chapter 1 §1.3 visual decision support |
| `using-git-worktrees` | Chapter 4 GCS-1 |
| `writing-plans` | Chapter 5 §16 |
| `executing-plans` | Chapter 5 §§12 and 16 |
| `subagent-driven-development` | Chapter 5 §§12, 15, and 16 |
| `dispatching-parallel-agents` | Chapter 5 §15 |
| `test-driven-development` and test-quality guidance | Chapter 3 §§2, 4, 5, and 7 |
| `systematic-debugging` | Chapter 3 §8 |
| debugging support techniques | Chapter 3 §§5 and 8 |
| `verification-before-completion` | Chapter 3 §11 and chapter 4 GCS-3 |
| `requesting-code-review` | Chapter 4 GCS-2 and chapter 5 §13 |
| `receiving-code-review` | Chapter 4 GCS-2 |
| `finishing-a-development-branch` | Chapter 4 GCS-8 |
| `writing-skills` | Chapter 2 §12 |

#### Ponytail

- **Dietrich Gebert, _Ponytail_ 4.9.0 — commit
  `0a4dd63ad4541f4f655c4108a295916f3c1d8fda`, accessed 2026-09-03.**
  [Versioned source](https://github.com/DietrichGebert/ponytail/tree/0a4dd63ad4541f4f655c4108a295916f3c1d8fda).
  The pinned `LICENSE` is MIT.

`ponytail`, `ponytail-review`, `ponytail-audit`, and `ponytail-debt` map to
`experts/ponytail-simplicity.md`. The fallback preserves the comprehension-first
ladder and safety exclusions. `ponytail-gain`, `ponytail-help`, intensity modes,
benchmark claims, hooks, state files, subagent injection, and install/uninstall
effects are not engineering capabilities and are not bundled.

#### Addy Osmani Agent Skills

- **Addy Osmani and contributors, _Agent Skills_ 0.6.8 — commit
  `a0dd41844acdfcd0fbc8f66d27f0ee6d3029ce22`, accessed 2026-09-02.**
  [Versioned source](https://github.com/addyosmani/agent-skills/tree/a0dd41844acdfcd0fbc8f66d27f0ee6d3029ce22).
  The pinned `LICENSE` is MIT.

All 24 lifecycle skills have an internal owner. A trusted installed original is
preferred per skill. The `using-agent-skills` meta-router is prohibited.

| Internal module | Original skills covered |
|---|---|
| `experts/requirements-planning.md` | `interview-me`, `idea-refine`, `spec-driven-development`, `constraint-driven-development`, `planning-and-task-breakdown` |
| `experts/context-sources.md` | `context-engineering`, `source-driven-development`, `doubt-driven-development` |
| `experts/interfaces-ui.md` | `frontend-ui-engineering`, `api-and-interface-design` |
| `experts/quality-operations.md` | `incremental-implementation`, `test-driven-development`, `browser-testing-with-devtools`, `debugging-and-error-recovery`, `code-review-and-quality`, `code-simplification`, `security-and-hardening`, `performance-optimization`, `git-workflow-and-versioning`, `ci-cd-and-automation`, `deprecation-and-migration`, `documentation-and-adrs`, `observability-and-instrumentation`, `shipping-and-launch` |

Shared-reference loss, provider hooks, commands, personas, fixed thresholds, and
whole-pack context loading are not imported. The internal modules use handbook
authority and load only the selected section.

#### Understand Anything

- **Egonex, _Understand Anything_ 2.9.4 — commit
  `840ad7d66d881cb50f4f33011785308c7a018503`, accessed 2026-09-03.**
  [Versioned source](https://github.com/Egonex-AI/Understand-Anything/tree/840ad7d66d881cb50f4f33011785308c7a018503).
  The pinned plugin manifest declares MIT.

`understand`, `understand-diff`, `understand-explain`, and
`understand-onboard` map to `experts/code-comprehension.md`. The fallback uses
native LSP/AST/reference/search tools first, separates structural facts from
semantic hypotheses, binds freshness to all working states, and treats impact as
advisory.

The installer, dependency build, internal agent swarm, persistent knowledge
graph, dashboard, semantic chat/search, domain or knowledge-base analysis,
auto-update hook, worktree redirect, external model use, server/browser launch,
and generated-data commits are not bundled.

#### Karpathy autoresearch

- **Andrej Karpathy, _autoresearch_ — commit
  `228791fb499afffb54b46200aca536f79142f117`, accessed 2026-09-03.**
  [Versioned source](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117).
  The pinned README declares MIT, but no root license file was present when
  reviewed; redistribution still requires sufficient license evidence.

The compatible `autoresearch` capability maps to
`experts/empirical-optimization.md`. The fallback adopts a baseline, scalar
objective, fixed protocol, keep/discard/crash ledger, and simplicity criterion.
It replaces the source's indefinite loop and git-reset autonomy with finite
budgets, frozen evaluator/holdout/invariants, isolated mutations, categorical
effect prohibitions, and ordinary handoff gates.

#### GitHub Spec Kit

- Expected value: durable what-before-how artifacts, consistency analysis, and
  convergence against explicit requirements.
- Scope fit: strong for multi-session, multi-contributor, contract, and
  assurance-heavy changes; unnecessary for clear localized work.
- Material risk: artifact ceremony, stale parallel truth, and unauthorized issue
  publication if the whole CLI workflow is imported.
- Smallest alternative: one internal specification-delivery module using
  existing project rules and trackers.
- Decision: **accepted** as original-preferred capability fallbacks; CLI,
  initialization, extensions, presets, and bundles remain external.

- **GitHub, _Spec Kit_ 1.0.0 — commit
  `bca679051abb80d6cf0cd909f2539a28a10eb7eb`, accessed 2026-09-03.**
  [Versioned source](https://github.com/github/spec-kit/tree/bca679051abb80d6cf0cd909f2539a28a10eb7eb).
  The pinned README declares MIT.

The core `speckit-constitution`, `speckit-specify`, `speckit-plan`,
`speckit-tasks`, `speckit-taskstoissues`, `speckit-implement`,
`speckit-converge`, `speckit-clarify`, `speckit-analyze`, and
`speckit-checklist` capabilities map to `experts/spec-delivery.md`. The same
module owns the reviewed bug workflow (`speckit-bug-assess`,
`speckit-bug-fix`, `speckit-bug-test`) and idea-assessment sequence
(`speckit-assess-intake`, `speckit-assess-research`,
`speckit-assess-define`, `speckit-assess-shape`,
`speckit-assess-decide`). Existing repository policy remains the constitution;
creating tracker issues is always a separately authorized effect.

#### OpenSpec

- Expected value: a lighter brownfield change lifecycle with explicit
  requirement deltas and accepted canonicalization.
- Scope fit: strong when requirements evolve with code and must retain an
  auditable current and proposed state.
- Material risk: duplicate sources of truth, telemetry, generated-data drift,
  and heavyweight cross-repository stores.
- Smallest alternative: reuse the specification-delivery module with
  change-local deltas and archive semantics.
- Decision: **accepted** for explore/propose/apply/verify/archive capabilities;
  runtime, dashboard, telemetry, stores, and updater remain excluded.

- **Fission AI, _OpenSpec_ 1.11.0 — commit
  `a0ddb60d040c61f4907436a9d91310934b1dda63`, accessed 2026-09-03.**
  [Versioned source](https://github.com/Fission-AI/OpenSpec/tree/a0ddb60d040c61f4907436a9d91310934b1dda63).
  The pinned package metadata and README declare MIT.

`openspec-explore`, `openspec-propose`, `openspec-new`,
`openspec-continue`, `openspec-ff`, `openspec-apply`, `openspec-verify`,
`openspec-archive`, `openspec-bulk-archive`, and `openspec-onboard` map to
`experts/spec-delivery.md`. The fallback keeps fast-forward bounded by ordinary
analysis and authority, requires exact-byte verification before archive, and
keeps canonical specs unchanged when a delta is unaccepted.

#### BMAD Method

- Expected value: right-sized agile planning plus explicit readiness, course
  correction, status, walkthrough, and retrospective loops.
- Scope fit: strong for multi-slice initiatives; its full persona and module
  system is redundant with the canonical router.
- Material risk: methodology duplication, excessive artifacts, hidden tracker
  mutation, and unattended epic execution.
- Smallest alternative: one self-contained adaptive-agile fallback that reuses
  handbook authority, evidence, planning, and review controls without peer routing.
- Decision: **accepted** for the 16 distinct pinned Method skills; agents,
  personas, party mode, installer, modules, and unattended loop are excluded.

- **BMad Code, _BMAD Method_ 6.11.0 — commit
  `9ce3c397c9b238de96f7365da8019f6f66b059da`, accessed 2026-09-03.**
  [Versioned source](https://github.com/bmad-code-org/BMAD-METHOD/tree/9ce3c397c9b238de96f7365da8019f6f66b059da).
  The pinned package metadata and README declare MIT; BMAD names remain their
  owner's trademarks.

The capability set in the pinned `module-help.csv` maps to
`experts/adaptive-agile.md`: `bmad-project-context`, `bmad-build`, `bmad-spec`,
`bmad-correct-course`, `bmad-brainstorming`, `bmad-product-brief`,
`bmad-prfaq`, `bmad-prd`, `bmad-ux`, `bmad-architecture`,
`bmad-create-epics-and-stories`, `bmad-sprint-planning`, `bmad-code-review`,
`bmad-checkpoint-preview`, `bmad-qa-generate-e2e-tests`, and
`bmad-retrospective`. The fallback uses `PASS`/`CONCERNS`/`FAIL` readiness
without turning non-blocking improvements into blockers.

#### Additional popular specification skills

- Expected value: conversation-to-spec synthesis, explicit test seams, and
  issue decomposition.
- Scope fit: the useful parts already fit the requirements-planning and
  specification-delivery experts.
- Material risk: the reviewed `to-spec` workflow publishes automatically and
  assumes tracker configuration, which exceeds planning authority.
- Smallest alternative: retain its useful highest-stable-test-seam and explicit
  out-of-scope checks in the internal fallback.
- Decision: **deferred** as a provider because it adds no distinct expert
  contract after adaptation.

- **Matt Pocock, _skills_, `to-spec` — commit
  `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`, accessed 2026-09-03.**
  [Versioned source](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/to-spec/SKILL.md).
  Consulted after the public Skills leaderboard surfaced `to-spec`, `to-prd`,
  `to-tickets`, and `to-issues`.

### Original-preference and fallback contract

`skills/software-engineering-handbook/experts/registry.json` owns provider and
capability inventory. `experts/purposes.json` classifies all originals into
deduplicated semantic purposes. `experts/resolution.md` defines selection.

1. Discover availability from host-registered descriptors only; do not search
   the network or filesystem.
2. Resolve the task to a semantic purpose before loading bodies. Default to core
   only for a localized low-risk task with no expert trigger.
3. For an equivalence group, prefer the first trusted compatible original in
   declared order whose provider-qualified identity and descriptor trigger
   match. For R3–R4 work, its source/version/content identity must satisfy the
   project adapter's trust policy.
4. Load at most one original or fallback per purpose. If every alternative is
   absent, untrusted, incompatible, or unavailable, use the purpose's single
   fallback.
5. Never activate an external meta-router or fail over after side effects
   without reconciling at a safe boundary.
6. Keep the handbook core authoritative. Expert output remains a proposal until
   normal evidence and acceptance gates pass.

### Package organization and extension

Portable capabilities are separated by responsibility under
`skills/software-engineering-handbook/experts/`. The compact main skill contains
only the fast routing index; modules load progressively.

New providers use the same stable path: pin and review the source; map each
original to an existing purpose before proposing a demonstrably distinct new
boundary; reject duplicate routers and non-workflow surfaces; add or reuse one
bounded module; register triggers/exclusions/dependencies/effects/evidence and
rollback; validate classification, ordered alternatives, duplicate-route
rejection, original-present/original-absent/conflict paths, then enable without
editing every existing expert. Provider updates repeat provenance,
compatibility, pressure, and exact-byte review.

## Source and conformance limitations

The ISO links above expose catalogue metadata and public abstracts, not the complete normative standards. Those abstracts establish the standards' identity, edition, date, stated scope, and exclusions used in this handbook architecture. They **do not establish implementation conformance, certification, or a complete interpretation of any ISO/IEC/IEEE requirement**. A project claiming conformance MUST obtain and assess the applicable full standard, edition, normative references, tailoring rules, and required evidence through an authorized process.

Likewise, citing NIST, OWASP, SLSA, Scrum, Agile Alliance, IETF, Git,
Superpowers, Ponytail, Agent Skills, Understand Anything, autoresearch, Spec
Kit, OpenSpec, BMAD Method, or another reviewed skill does not by itself prove
compliance or correct implementation. Projects must select
applicable requirements, record versions and tailoring, implement controls in
their actual environment, and produce evidence for the claims they make.
