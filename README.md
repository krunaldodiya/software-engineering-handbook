# Software Engineering Handbook

A public, risk-scaled software-engineering handbook and sparse
mixture-of-experts skill router for humans, teams, and AI coding agents.

**11 supported harness surfaces · 5 chapters · 8 reviewed providers · 71 normalized purposes · MIT**

> **Context-first:** agents discover a tiny descriptor at startup and load only
> the handbook and expert sections required by the current task.

## Table of contents

- [Quick start](#quick-start)
  - [Pi](#pi)
  - [Oh My Pi](#oh-my-pi)
- [Usage](#usage)
- [Features](#features)
- [How it works without filling the context window](#how-it-works-without-filling-the-context-window)
- [Directory roles](#directory-roles)
- [Install on other agents](#install-on-other-agents)
  - [Claude App](#claude-app)
  - [Claude Code](#claude-code)
  - [Antigravity](#antigravity)
  - [Codex App](#codex-app)
  - [Codex CLI](#codex-cli)
  - [Gemini CLI](#gemini-cli)
  - [Kimi Code CLI](#kimi-code-cli)
  - [OpenCode](#opencode)
  - [Hermes Agent](#hermes-agent)
- [Future harness support](#future-harness-support)
- [Updating](#updating)
- [Repository contents](#repository-contents)
- [Validate and contribute](#validate-and-contribute)
- [Safety and repository boundary](#safety-and-repository-boundary)
- [Upstream attribution](#upstream-attribution)
- [License](#license)

## Quick start

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

Start a new session after installation. The skill activates automatically for
non-trivial software-engineering work, or you can invoke
`/skill:software-engineering-handbook` explicitly where skill commands are
supported.

See [install on other agents](#install-on-other-agents) for Claude App, Claude
Code, Antigravity, Codex App, Codex CLI, Gemini CLI, Kimi Code CLI, OpenCode,
and Hermes Agent. Pi and Oh My Pi are in [quick start](#quick-start).

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
  groups, and 90 provider-qualified originals plus one handbook-native
  context-usage capability, normalized into 71 purposes.
- Deduplicated MoE routing: each original belongs to exactly one purpose.
  Equivalent skills are ordered alternatives, so only one original or fallback
  can load for that purpose.
- Bounded expert adaptations from Superpowers, Ponytail, Addy Osmani's Agent
  Skills, Understand Anything, autoresearch, GitHub Spec Kit, OpenSpec, and
  BMAD Method.
- Trusted-original preference: use a compatible installed original skill when
  available; otherwise load the bounded internal fallback, never both.
- Built-in context and usage economics: progressive disclosure, duplicate
  instruction removal, cache-aware context reuse, bounded tool/agent fan-out,
  risk-scaled model choice, and honest before/after token and cost evidence.
- Built-in Ponytail engineering behavior: comprehension-first minimal
  implementation, root-cause placement, over-engineering review and audit, and
  shortcut-debt reporting. Ponytail's intensity modes, help card, benchmark
  scoreboard, hooks, and persistent mode state remain intentionally unbundled.
- Explicit authority, evidence, conflict, failure, rollback, and context-budget
  rules.

This is guidance and routing—not an autonomous deployment system. It does not
silently install dependencies, run hooks, publish, release, deploy, access
secrets, or grant itself authority.

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

## Directory roles

They are related, but not duplicates:

| Path | Role |
|---|---|
| `handbook/software-engineering/` | The normative, human-readable book—the long-term knowledge layer |
| `skills/software-engineering-handbook/` | The canonical portable router, expert modules, and registry |
| `managed-skills/software-engineering-handbook/` | The tiny OMP adapter and repository validator |
| `rules/engineering-handbook-enforcement.md` | OMP-specific global enforcement adapter |

`software-engineering` names the handbook subject. `software-engineering-handbook`
is the installable skill/package identity. Keeping the book separate from the
router lets humans browse it normally while agents load only selected sections.

## Install on other agents

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

## Future harness support

These integrations are intentionally deferred:

- [ ] Cursor
- [ ] Devin CLI
- [ ] Factory Droid
- [ ] GitHub Copilot CLI
- [ ] Grok Build CLI

## Updating

Use the harness's normal plugin update command. For Pi:

```sh
pi update --extension git:github.com/krunaldodiya/software-engineering-handbook
```

For reproducible use, install a reviewed tag or commit instead of a moving
branch. Pi accepts `@<tag-or-commit>` after the repository path.

## Repository contents

- `handbook/software-engineering/` — portable normative handbook and source
  register.
- `skills/software-engineering-handbook/` — canonical portable router, expert
  modules, and registry.
- `managed-skills/software-engineering-handbook/` — tiny OMP adapter and
  repository validator.
- Harness manifests under `.agents/`, `.claude-plugin/`, `.codex-plugin/`,
  `.kimi-plugin/`, and `.opencode/`, plus root Agent Plugins v1, Gemini, and Pi
  manifests.
- `rules/engineering-handbook-enforcement.md` — OMP global-rule adapter.

## Validate and contribute

Validate the catalog and context budgets before proposing a change:

```sh
python3 managed-skills/software-engineering-handbook/validate_registry.py
python3 -O managed-skills/software-engineering-handbook/validate_registry.py
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
