# Software Engineering Handbook

A public, risk-scaled software-engineering handbook and sparse
mixture-of-experts skill router for humans, teams, and AI coding agents.

**11 supported harness surfaces · 5 chapters · 8 reviewed providers · 74 normalized purposes · MIT**

> **Context-first:** agents discover a tiny descriptor at startup and load only
> the handbook and expert sections required by the current task.

## Table of contents

- [Quick start](#quick-start)
- [Usage](#usage)
- [Features](#features)
  - [Engineering coverage](#engineering-coverage)
  - [Complete capability inventory](#complete-capability-inventory)
  - [Routing and package utilities](#routing-and-package-utilities)
- [How it works without filling the context window](#how-it-works-without-filling-the-context-window)
- [Directory roles](#directory-roles)
- [Install on supported agents](#install-on-supported-agents)
  - [Claude App](#claude-app)
  - [Claude Code](#claude-code)
  - [Antigravity](#antigravity)
  - [Codex App](#codex-app)
  - [Codex CLI](#codex-cli)
  - [Gemini CLI](#gemini-cli)
  - [Kimi Code CLI](#kimi-code-cli)
  - [OpenCode](#opencode)
  - [Hermes Agent](#hermes-agent)
  - [Pi](#pi)
  - [Oh My Pi](#oh-my-pi)
- [Future harness support](#future-harness-support)
- [Updating](#updating)
- [Repository contents](#repository-contents)
- [Validate and contribute](#validate-and-contribute)
- [Safety and repository boundary](#safety-and-repository-boundary)
- [Upstream attribution](#upstream-attribution)
- [License](#license)

## Quick start

Choose the scoped installation procedure for your host under
[install on supported agents](#install-on-supported-agents). Each procedure
installs or retains the complete package: portable skill, handbook, registry,
and the applicable host adapter. The canonical skill references sibling
handbook sources, so a skill-only copy is incomplete.

Review the repository and pin a trusted tag or commit when the host supports
immutable references. Start a new agent session after installation.

## Usage

You normally do not need a special command after installation. Ask for the work
itself:

```text
Fix this concurrency bug and prove the reproduction no longer fails.
Review this pull request for correctness and security risks.
Plan the smallest safe implementation of this API change.
Simplify this module without changing its observable behavior.
Investigate this performance regression with a fixed benchmark protocol.
```

The router classifies risk, reads repository-specific rules, chooses one primary
chapter, and activates only the smallest compatible expert set. Project and user
instructions remain authoritative over generic handbook defaults.

For explicit use, ask the agent to “apply the software-engineering handbook” or
invoke `software-engineering-handbook` through the harness's skill UI or slash
command.

> **One installation is enough.** Reviewed provider skills are optional
> compatibility inputs, not dependencies. The handbook includes complete
> internal fallbacks and does not require Superpowers, Ponytail, Agent Skills,
> Spec Kit, OpenSpec, BMAD, or another workflow pack to be installed.

## Features

- Five portable chapters covering lifecycle governance, architecture and code
  quality, testing and debugging, Git/CI/CD/security, and atomic delivery.
- Risk tiers from localized reversible work through critical irreversible work.
- A machine-readable registry containing 8 reviewed providers, 11 provider
  groups, and 90 provider-qualified originals plus 4 handbook-native
  capabilities, normalized into 74 purposes.
- Deduplicated MoE routing: each original belongs to exactly one purpose.
  Equivalent skills are ordered alternatives, so only one original or fallback
  can load for that purpose.
- Bounded expert adaptations from Superpowers, Ponytail, Addy Osmani's Agent
  Skills, Understand Anything, autoresearch, GitHub Spec Kit, OpenSpec, and
  BMAD Method.
- Trusted-original preference: use a compatible installed original skill when
  available; otherwise load the bounded internal fallback, never both.
- Built-in context and usage economics: degradation diagnosis, safe compression
  and handoff, recurring harness-surface audits, progressive disclosure,
  cache-aware reuse, bounded tool/agent fan-out, risk-scaled model choice, and
  honest total-task token and cost evidence.
- Governed procedure and skill improvement: causal triggers, bounded candidates,
  representative development and held-out cases, hard safety gates, independent
  approval for high-risk changes, rejected-candidate evidence, and rollback.
- Built-in Ponytail engineering behavior: comprehension-first minimal
  implementation, root-cause placement, over-engineering review and audit, and
  shortcut-debt reporting. Ponytail's intensity modes, help card, benchmark
  scoreboard, hooks, and persistent mode state remain intentionally unbundled.
- Explicit authority, evidence, conflict, failure, rollback, and context-budget
  rules.

This is guidance and routing—not an autonomous deployment system. It does not
silently install dependencies, run hooks, publish, release, deploy, access
secrets, or grant itself authority.

### Engineering coverage

The handbook covers the software lifecycle, not just code generation. These
chapter summaries describe guidance and controls, not automatically executed
services:

| Chapter | Features and responsibilities |
|---|---|
| [Lifecycle and governance](handbook/software-engineering/01-lifecycle-governance.md) | Scope, stakeholders, requirements, ownership, decision authority, traceability, change control, operation, deprecation, and retirement |
| [Architecture and code quality](handbook/software-engineering/02-architecture-code-quality.md) | Boundaries, contracts, data and error models, dependency choices, reliability, resource behavior, performance, maintainability, and implementation discipline |
| [TDD, testing, and debugging](handbook/software-engineering/03-tdd-testing-debugging.md) | Test strategy, red–green–refactor, discriminating reproductions, root-cause investigation, deterministic verification, regression prevention, and completion evidence |
| [Git, CI/CD, and security](handbook/software-engineering/04-git-ci-cd-security.md) | Coherent commits, protected integration, exact-revision review, CI gates, secrets, supply-chain controls, artifact provenance, authorized release, recovery, and vulnerability response |
| [Agile atomic delivery](handbook/software-engineering/05-agile-atomic-delivery.md) | Usable vertical slices, sequencing, bounded work, coordination, feedback, Definition of Done, and evidence-bearing handoff without mandating a sprint length or tracker |

### Complete capability inventory

The inventory below covers **all 90 registered provider-qualified originals**
and **all 4 handbook-native capabilities**. They resolve to **74 normalized
purposes: 9 shared-purpose groups, 61 distinct originals, and 4 native purposes**.
Counts describe routing identities, not 94 independent workflows to run together.

The [capability registry](skills/software-engineering-handbook/experts/registry.json)
owns descriptors and provider mappings; the
[purpose catalog](skills/software-engineering-handbook/experts/purposes.json)
owns normalization and alternative ordering. This README is a browsing index,
not a second routing policy. Capability identifiers are lookup names, not
promises that a host exposes matching slash commands.

#### Handbook-native capabilities

All four are included in the
[context-economics module](skills/software-engineering-handbook/experts/context-economics.md):

| Purpose | Capability |
|---|---|
| `context-degradation-diagnosis` | Diagnose lost, poisoned, distracting, confused, or conflicting context before choosing a mitigation |
| `context-compression-continuity` | Compact or hand off long-running work while preserving exact task state and recoverability |
| `harness-context-audit` | Audit recurring instruction, skill, tool, memory, and history overhead before authorized cleanup |
| `context-usage-economics` | Reduce context, token, model, tool, and agent cost without weakening task success or evidence |

#### Shared purposes

These nine groups normalize overlapping originals. The router uses the first
matching trusted original in the catalog's declared order, or the one complete
internal fallback; it does not combine equivalent workflows.

| Purpose | Capability |
|---|---|
| `procedure-skill-improvement` | Improve reusable procedures through bounded candidates, held-out evaluation, authorized promotion, and rollback |
| `ideation` | Generate and refine candidate approaches before commitment |
| `planning-decomposition` | Turn an accepted outcome into an ordered plan and bounded work items |
| `implementation-execution` | Execute an accepted plan incrementally without changing its governing contract |
| `test-driven-development` | Drive permanent behavior changes through a discriminating failing check and red–green–refactor |
| `debugging-remediation` | Reproduce, isolate, repair, and verify a concrete defect |
| `completion-verification` | Challenge completion claims with evidence from the exact candidate revision |
| `generic-code-review` | Review a candidate for correctness, quality, and actionable defects |
| `bounded-requirements-specification` | Write a bounded, implementation-ready specification for an accepted change |

#### Provider capability families

Every family has an included bounded adaptation or mapped handbook fallback.
Compatible upstream originals are optional, trust-checked alternatives—not
bundled upstream runtimes, installers, hooks, or an endorsement of every feature
in the upstream project.

| Family | Included capability coverage | Original mappings |
|---|---|---|
| [Superpowers inner loop](handbook/software-engineering/references.md) | Brainstorming, isolated workspaces, planning and execution, bounded agent coordination, TDD, debugging, verification, review requests and feedback, branch completion, and procedure improvement | 13 |
| [Ponytail simplicity](skills/software-engineering-handbook/experts/ponytail-simplicity.md) | Comprehension-first minimal implementation, over-engineering review, broader simplicity audit, and shortcut-debt reporting | 4 |
| [Agent Skills: requirements and planning](skills/software-engineering-handbook/experts/requirements-planning.md) | Consequential clarification, idea refinement, specification, constraint-first design, and task decomposition | 5 |
| [Agent Skills: context and sources](skills/software-engineering-handbook/experts/context-sources.md) | Focused context acquisition, primary-source grounding, and doubt-driven challenge | 3 |
| [Agent Skills: interfaces and UI](skills/software-engineering-handbook/experts/interfaces-ui.md) | Frontend and user-facing behavior, plus public API and module contracts | 2 |
| [Agent Skills: quality and operations](skills/software-engineering-handbook/experts/quality-operations.md) | Incremental implementation, TDD, browser verification, debugging, review, simplification, security, performance, Git/versioning, CI/CD, migrations, documentation/ADRs, observability, and launch | 14 |
| [Understand Anything](skills/software-engineering-handbook/experts/code-comprehension.md) | Task-scoped codebase mapping, architecture orientation, diff impact, explanations, and onboarding | 4 |
| [autoresearch](skills/software-engineering-handbook/experts/empirical-optimization.md) | Finite empirical optimization under an owner-approved frozen protocol | 1 |
| [Spec Kit](skills/software-engineering-handbook/experts/spec-delivery.md) | Durable specification chains, plans/tasks, issue conversion, implementation convergence, clarification, consistency analysis, checklists, bug assessment/repair/tests, and staged opportunity assessment | 18 |
| [OpenSpec](skills/software-engineering-handbook/experts/spec-delivery.md) | Brownfield exploration, proposals and change packets, staged or fast-forward artifact preparation, implementation, verification, provenance-retaining archive, and onboarding | 10 |
| [BMAD Method](skills/software-engineering-handbook/experts/adaptive-agile.md) | Project context, bounded build/spec flows, course correction, brainstorming, product briefs/PRFAQs/PRDs, UX, architecture, epics/stories, sprint planning, review, checkpoint previews, end-to-end test design, and retrospectives | 16 |

<details>
<summary>All 90 registered original identifiers, grouped by capability family</summary>

These are the complete registered mappings, including aliases belonging to the
shared purposes above. Consult the registry and source register for exact
triggers, exclusions, source identities, effects, and fallback boundaries.

**Superpowers inner loop (13)**

- `superpowers/brainstorming`
- `superpowers/using-git-worktrees`
- `superpowers/writing-plans`
- `superpowers/executing-plans`
- `superpowers/subagent-driven-development`
- `superpowers/dispatching-parallel-agents`
- `superpowers/test-driven-development`
- `superpowers/systematic-debugging`
- `superpowers/verification-before-completion`
- `superpowers/requesting-code-review`
- `superpowers/receiving-code-review`
- `superpowers/finishing-a-development-branch`
- `superpowers/writing-skills`

**Ponytail simplicity (4)**

- `ponytail/ponytail`
- `ponytail/ponytail-review`
- `ponytail/ponytail-audit`
- `ponytail/ponytail-debt`

**Agent Skills: requirements and planning (5)**

- `agent-skills/interview-me`
- `agent-skills/idea-refine`
- `agent-skills/spec-driven-development`
- `agent-skills/constraint-driven-development`
- `agent-skills/planning-and-task-breakdown`

**Agent Skills: context and sources (3)**

- `agent-skills/context-engineering`
- `agent-skills/source-driven-development`
- `agent-skills/doubt-driven-development`

**Agent Skills: interfaces and UI (2)**

- `agent-skills/frontend-ui-engineering`
- `agent-skills/api-and-interface-design`

**Agent Skills: quality and operations (14)**

- `agent-skills/incremental-implementation`
- `agent-skills/test-driven-development`
- `agent-skills/browser-testing-with-devtools`
- `agent-skills/debugging-and-error-recovery`
- `agent-skills/code-review-and-quality`
- `agent-skills/code-simplification`
- `agent-skills/security-and-hardening`
- `agent-skills/performance-optimization`
- `agent-skills/git-workflow-and-versioning`
- `agent-skills/ci-cd-and-automation`
- `agent-skills/deprecation-and-migration`
- `agent-skills/documentation-and-adrs`
- `agent-skills/observability-and-instrumentation`
- `agent-skills/shipping-and-launch`

**Understand Anything (4)**

- `understand-anything/understand`
- `understand-anything/understand-diff`
- `understand-anything/understand-explain`
- `understand-anything/understand-onboard`

**autoresearch (1)**

- `autoresearch/autoresearch`

**Spec Kit (18)**

- `spec-kit/speckit-constitution`
- `spec-kit/speckit-specify`
- `spec-kit/speckit-plan`
- `spec-kit/speckit-tasks`
- `spec-kit/speckit-taskstoissues`
- `spec-kit/speckit-implement`
- `spec-kit/speckit-converge`
- `spec-kit/speckit-clarify`
- `spec-kit/speckit-analyze`
- `spec-kit/speckit-checklist`
- `spec-kit/speckit-bug-assess`
- `spec-kit/speckit-bug-fix`
- `spec-kit/speckit-bug-test`
- `spec-kit/speckit-assess-intake`
- `spec-kit/speckit-assess-research`
- `spec-kit/speckit-assess-define`
- `spec-kit/speckit-assess-shape`
- `spec-kit/speckit-assess-decide`

**OpenSpec (10)**

- `openspec/openspec-explore`
- `openspec/openspec-propose`
- `openspec/openspec-new`
- `openspec/openspec-continue`
- `openspec/openspec-ff`
- `openspec/openspec-apply`
- `openspec/openspec-verify`
- `openspec/openspec-archive`
- `openspec/openspec-bulk-archive`
- `openspec/openspec-onboard`

**BMAD Method (16)**

- `bmad-method/bmad-project-context`
- `bmad-method/bmad-build`
- `bmad-method/bmad-spec`
- `bmad-method/bmad-correct-course`
- `bmad-method/bmad-brainstorming`
- `bmad-method/bmad-product-brief`
- `bmad-method/bmad-prfaq`
- `bmad-method/bmad-prd`
- `bmad-method/bmad-ux`
- `bmad-method/bmad-architecture`
- `bmad-method/bmad-create-epics-and-stories`
- `bmad-method/bmad-sprint-planning`
- `bmad-method/bmad-code-review`
- `bmad-method/bmad-checkpoint-preview`
- `bmad-method/bmad-qa-generate-e2e-tests`
- `bmad-method/bmad-retrospective`

</details>

### Routing and package utilities

- **Sparse selection:** risk-scaled expert budgets, one primary workflow expert,
  and at most one original or fallback for each purpose.
- **Complete route contracts:** triggers and near-miss exclusions, prerequisites,
  required dependency closure, conflicts and ordering, source/trust identity,
  permitted effects, evidence, failure behavior, and rollback.
- **Bounded descriptor lookup:** an optional standard-library Python CLI accepts
  a purpose or provider-qualified original, works from any directory, and
  reports invalid inputs explicitly without selecting or activating a provider.
- **Catalog maintenance:** included validation utilities cover registry/schema
  consistency, mapping completeness, sparse routing, context budgets, pressure,
  effects, and failover; behavioral checks cover the descriptor query.
- **Portable packaging:** [11 documented harness surfaces](#install-on-supported-agents),
  small discovery adapters, complete internal fallbacks, immutable-ref
  installation where supported, and source/version verification guidance.
- **Explicit limits:** no bundled upstream provider runtimes, hidden telemetry,
  autonomous publishing/deployment, universal fixed test-coverage threshold, or
  unmeasured quality, token-cost, or performance guarantee. Source-specific
  exclusions remain in the [source register](handbook/software-engineering/references.md).

## How it works without filling the context window

The package behaves like a book with an index instead of putting every page in
working memory.

| Layer | Loaded when | Content |
|---|---|---|
| Discovery | Agent startup | Skill name and description only; capped at 1 KiB |
| Router index | A matching engineering task begins | Compact `SKILL.md`; capped at 10 KiB |
| Working set | The router resolves the task | Only applicable handbook and expert sections |
| Cold storage | Until selected | Full chapters, registry, sources, and inactive experts |

Catalog growth does not expand the active prompt. The adapters in this
repository register skill paths but do not inject the full handbook at startup.
After compaction, agents retain concise decisions and evidence, then re-read
only authoritative sections that are still needed.

For ambiguous discovery on hosts that support command execution, an optional
Python-standard-library query prints one purpose's complete descriptors and
policy instead of both cold catalogs:

```sh
python3 managed-skills/software-engineering-handbook/query_experts.py ideation
```

The script also accepts a provider-qualified original, works by absolute path
from any directory, preserves ordered alternatives and required dependencies,
and never loads bodies, selects a route, infers trust, or activates a provider.
It is not an additional ordinary-task preflight. See the
[resolution contract](skills/software-engineering-handbook/experts/resolution.md)
for unavailable-tool behavior.

## Directory roles

They are related, but not duplicates:

| Path | Role |
|---|---|
| `handbook/software-engineering/` | The normative, human-readable book—the long-term knowledge layer |
| `skills/software-engineering-handbook/` | The canonical portable router, expert modules, and registry |
| `managed-skills/software-engineering-handbook/` | Package query/validation utilities and the tiny OMP adapter |
| `rules/engineering-handbook-enforcement.md` | OMP-specific global enforcement adapter |

`software-engineering` names the handbook subject. `software-engineering-handbook`
is the installable skill/package identity. Keeping the book separate from the
router lets humans browse it normally while agents load only selected sections.

## Install on supported agents

Installation changes local agent configuration and packages can influence agent
actions. Review the repository and pin a trusted tag or commit when your harness
supports refs.

### Claude App

Open **Customize → Plugins → Personal plugins → + → Add marketplace**, add:

```text
https://github.com/krunaldodiya/software-engineering-handbook
```

Install **Software Engineering Handbook**. The bundled skill works in Claude
web chat, Claude Desktop chat, and Cowork.

### Claude Code

```text
/plugin marketplace add krunaldodiya/software-engineering-handbook
/plugin install software-engineering-handbook@software-engineering-handbook
```

Start a new Claude Code session.

### Antigravity

```sh
agy plugin install https://github.com/krunaldodiya/software-engineering-handbook
```

### Codex App

Open **Settings → Plugins → Add Marketplace**, add:

```text
https://github.com/krunaldodiya/software-engineering-handbook
```

Install **Software Engineering Handbook** from that marketplace and start a new
chat.

### Codex CLI

```sh
codex plugin marketplace add krunaldodiya/software-engineering-handbook
codex plugin add software-engineering-handbook@software-engineering-handbook
```

### Gemini CLI

```sh
gemini extensions install https://github.com/krunaldodiya/software-engineering-handbook
```

Gemini loads only the small `GEMINI.md` routing pointer at startup.

### Kimi Code CLI

```text
/plugins install https://github.com/krunaldodiya/software-engineering-handbook
```

Run `/reload` or start a new Kimi session after installation.

### OpenCode

Add the Git-backed package to the `plugin` array in global or project
`opencode.json`:

```json
{
  "plugin": [
    "software-engineering-handbook@git+https://github.com/krunaldodiya/software-engineering-handbook.git"
  ]
}
```

Restart OpenCode. Its small adapter registers the skill path without injecting
handbook content.

### Hermes Agent

```sh
hermes plugins install krunaldodiya/software-engineering-handbook --enable
```

Hermes uses the code-free Agent Plugins v1 manifest at `plugin.json`. It
discovers the portable skill without a startup hook or router-body injection.

### Pi

```sh
pi install git:github.com/krunaldodiya/software-engineering-handbook
```

Try without installing:

```sh
pi -e git:github.com/krunaldodiya/software-engineering-handbook
```

### Oh My Pi

```sh
omp plugin install github:krunaldodiya/software-engineering-handbook
```

Start a new session after installation. Invoke
`/skill:software-engineering-handbook` explicitly where skill commands are
supported.

To update or reinstall a reviewed revision, rerun `omp plugin install` with
`github:krunaldodiya/software-engineering-handbook#<reviewed-commit-sha>`.
Uninstalling first is unnecessary. Verify `omp plugin list --json` and the
installed package identity, then have a fresh OMP session read
`skill://software-engineering-handbook`; a native skill can shadow a plugin
skill. Keep the prior reviewed ref for rollback. Reinstallation changes future
discovery, not the instructions already loaded into an active conversation.

## Future harness support

These integrations are intentionally deferred:

- [ ] Cursor
- [ ] Devin CLI
- [ ] Factory Droid
- [ ] GitHub Copilot CLI
- [ ] Grok Build CLI

## Updating

Use the selected harness's normal plugin or skill update mechanism. For
reproducible use, install a reviewed tag or commit instead of a moving branch
when the harness supports immutable references.

## Repository contents

- `handbook/software-engineering/` — portable normative handbook and source
  register.
- `skills/software-engineering-handbook/` — canonical portable router, expert
  modules, and registry.
- `managed-skills/software-engineering-handbook/` — package query/validation
  utilities and the tiny OMP adapter.
- Harness manifests under `.agents/`, `.claude-plugin/`, `.codex-plugin/`,
  `.kimi-plugin/`, and `.opencode/`, plus root Agent Plugins v1, Gemini, and Pi
  manifests.
- `rules/engineering-handbook-enforcement.md` — OMP global-rule adapter.

## Validate and contribute

Validate the catalog and context budgets before proposing a change:

```sh
python3 managed-skills/software-engineering-handbook/validate_registry.py
python3 -O managed-skills/software-engineering-handbook/validate_registry.py
python3 managed-skills/software-engineering-handbook/test_query_experts.py
python3 -O managed-skills/software-engineering-handbook/test_query_experts.py
```

For a provider capability change:

1. Pin and review the exact upstream source.
2. Map every original to an existing purpose in `experts/purposes.json`. Add a
   new purpose only for a demonstrably distinct behavioral boundary.
3. Gap-map it against existing experts.
4. Reuse an existing module or add one bounded expert module.
5. Register triggers, exclusions, prerequisites, conflicts, effects, evidence,
   context budget, and rollback.
6. Preserve ordered original preference and the single purpose fallback.
7. Add pressure checks for classification, duplicate routes, presence, absence,
   conflict, and active-budget paths.
8. Obtain exact-revision review before publication.

Do not add another workflow router, whole-catalog loading, hidden installation,
telemetry, or a capability already covered by a compatible expert.

Issues and pull requests are welcome. Keep changes evidence-backed, portable,
and narrowly owned.

## Safety and repository boundary

This public repository contains only handbook and packaging assets. Never commit
agent configuration, environment files, databases, caches, sessions,
credentials, secrets, private project adapters, or unrelated files.

Agent plugins and skills can influence actions. Installation does not authorize
publishing, deployment, destructive operations, secret access, or any other
protected effect. Normal user, project, and harness approvals still apply.

## Upstream attribution

This repository independently adapts workflow concepts; it does not vendor
upstream skill bodies or runtimes. Reviewed upstream revisions, licenses,
exclusions, and provenance links are recorded in the
[source register](handbook/software-engineering/references.md). Project names
and trademarks remain property of their respective owners.

## License

[MIT](LICENSE)
