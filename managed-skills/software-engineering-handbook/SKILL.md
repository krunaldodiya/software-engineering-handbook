---
name: software-engineering-handbook
description: "Apply the global risk-scaled software-engineering handbook and route the smallest compatible set of registered expert procedures for non-trivial implementation, review, testing, debugging, delivery, and maintenance work."
---

# Software Engineering Handbook

Use this skill for non-trivial software engineering work. It supplies global defaults; it does not replace explicit system, user, product, domain, repository, or executable-gate requirements.

## Mixture-of-experts router

This skill is the single workflow-level router. Its catalog may grow broad while
each task keeps a sparse active set: inspect compact descriptors first, then
activate only the few experts whose exact triggers and current risks require
them. Catalog size MUST NOT determine per-task body loading. The handbook core
always owns precedence, risk, authority, evidence, and delivery claims. Expert
modules add bounded technique; they do not form a second methodology or
provider vote.

### Context hierarchy

Keep the catalog in cold storage, not in the prompt. Startup discovery loads
only this skill's frontmatter descriptor. When the trigger matches, this file
is the book-style index. The active working set contains only the applicable
handbook sections and selected expert sections.

Never preload the full handbook, registry, provider pack, or expert catalog for
possible future use. When resolution is ambiguous, locate and read only the
matching registry descriptors. Preserve concise decisions, outcomes, and
evidence across compaction; re-read authoritative sections only when needed or
changed. Context consumption MUST remain independent of catalog size and leave
the large majority of the window for project facts and work.

The validator caps the startup descriptor at 1 KiB and this routing index at
10 KiB; growth belongs in cold, selectively loaded modules.

### Fast selection

Do not load all capabilities. For a localized R1 task with no expert trigger,
use the handbook core only. Otherwise match observable facts against this
compact index and load only the selected module or trusted original skill:

| Current need | Capability |
|---|---|
| discovery, planning, debugging, verification, review, branch completion, procedure authoring | mapped Superpowers capability in the handbook |
| coding minimalism or over-engineering review | `experts/ponytail-simplicity.md` |
| consequential ambiguity, specification, constraints, or task decomposition | `experts/requirements-planning.md` |
| durable spec/change artifacts, consistency analysis, convergence, or canonical archive | the selected section of `experts/spec-delivery.md` |
| multi-slice agile planning, readiness, course correction, status, walkthrough, or retrospective | the selected section of `experts/adaptive-agile.md` |
| unfamiliar context, external API facts, or high-consequence uncertainty | `experts/context-sources.md` |
| public interface, API, frontend, interaction, or accessibility | `experts/interfaces-ui.md` |
| implementation, test, browser, review, security, performance, CI/CD, migration, observability, or launch | the selected section of `experts/quality-operations.md` |
| large/unfamiliar codebase map, architecture orientation, or impact analysis | `experts/code-comprehension.md` |
| explicitly authorized measurable automated experiments | `experts/empirical-optimization.md` |

Default budget: R0 uses the handbook core only; R1 uses no expert or one
specialist; R2 uses at most one primary workflow expert and one specialist;
R3–R4 may add a second specialist or an independent evaluator when a distinct
current risk requires it. Exceed those budgets only for named non-overlapping
risks and record why. A module containing several sections loads only the
selected section. Reuse an unchanged module
already present in uncompacted context.

### Original-skill preference

Before loading an internal module, inspect the host's already registered skill
descriptors—never the network or filesystem—for the provider-qualified original
names declared in the module and `experts/registry.json`. The original
descriptor's own trigger must match. When a trusted compatible original is
registered, use it and suppress the internal fallback.
For R3–R4 work, use an original only when the host or project adapter can bind
it to an approved source/version/content identity; otherwise use the internal
fallback and report the limit. Never load both versions or either provider
meta-router (`using-superpowers`, `using-agent-skills`).

The handbook core still governs an original skill. A contradictory instruction,
unauthorized effect, missing prerequisite, or unavailable tool is surfaced or
stopped under handbook precedence. Do not switch from original to fallback
after side effects; reconcile at a safe boundary and resolve again.

### Resolution

When multiple capabilities plausibly match, read `experts/resolution.md` and
the relevant descriptors in `experts/registry.json`. Resolve scope,
prerequisites, dependencies, companions, conflicts, and original availability
before loading bodies. Select the smallest compatible set, at most one primary
workflow expert, and only specialists with distinct roles. Process experts load
before implementation experts. Provider popularity, installation order,
dependency order, or majority vote never decides.

Superpowers, Ponytail, Agent Skills, Understand Anything, autoresearch, Spec
Kit, OpenSpec, and BMAD Method are active as reviewed adapted capabilities.
Portable fallbacks live in responsibility-specific modules. Original provider
routers, hooks, installers, persistent services, runtime dependencies, and side
effects are not bundled or silently activated.
The source identities, adaptation maps, exclusions, and update rules are in
`references.md`.

## On-demand reading

1. Treat this file as the hot routing index. For localized R0–R1 work, do not
   load another handbook body unless a specific rule or expert trigger requires
   it.
2. For R2–R4 work, inspect the chapter map in
   `~/.omp/agent/handbook/software-engineering/README.md`, select one primary
   chapter, and load only the relevant sections by default. Read the full
   chapter only when the task spans it or a chapter-wide R3–R4 failure mode
   requires it. Secondary chapters remain section-only unless the same test
   applies.
3. Load only the selected section of an expert module. Use
   `experts/resolution.md` and only matching descriptors from
   `experts/registry.json` when selection is ambiguous.
4. Read `references.md` only when source selection, provenance, or an external
   standard materially affects the task.

## Operating sequence

- Classify consequence using the handbook's R1–R4 model; reclassify when new facts increase reach, irreversibility, uncertainty, or impact.
- Resolve applicable local sources of truth and repository gates before choosing process or commands.
- Define the observable outcome, authority, acceptance evidence, and lifecycle effects.
- Deliver the smallest coherent end-to-end slice that proves value; do not substitute technical or documentation layers when working behavior is required.
- Prefer test-first development for changed permanent observable contracts; apply chapter 3's documented deviations when test-first is inapplicable. Reproduce defects before repair and measure before performance optimization.
- Keep changes reviewable and tie verification, review, artifacts, and release decisions to the exact revision.
- Report what was exercised, what was not, and every residual or deferred boundary without inflating claims.

## Precedence and exceptions

A more specific authorized local rule overrides a generic handbook default within its scope. Never silently weaken safety, authorization, privacy, security, evidence integrity, or regulated controls. Handbook exceptions must be explicit, scoped, owned, justified, compensated, and bounded by an expiry, review event, or removal condition as defined by the index.
