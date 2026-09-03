# Code-comprehension expert

Use only for a large, unfamiliar, or cross-cutting subsystem, change-impact
analysis, or onboarding selected for the current engineering task.
Knowledge-base analysis, semantic chat, dashboards, and persistent memory are
out of scope.

## Fast path first

Use the platform's language server, AST search, references, definitions, text
search, and focused source reads before building a broader map. Stop when those
tools answer the current decision. Do not scan the repository merely because
this expert is available.

Escalate to a task-scoped map only when cross-file structure, architecture, or
blast radius remains materially uncertain. Bound directories, file types,
exclusions, maximum files, context, time, and cost before scanning.

## Structural map

Prefer deterministic facts:

- files, symbols, imports/exports, references, inheritance, calls, tests, build
  and deployment configuration;
- module/layer ownership and entry points supported by source structure; and
- exact revision plus staged, unstaged, and untracked project state.

Separate these from LLM-generated summaries, architecture labels, tours, domain
interpretations, and inferred relationships. Semantic claims require source
citations and remain hypotheses until verified.

## Privacy and effects

Classify and exclude secrets, credentials, personal data, generated/private
artifacts, vendored code, and irrelevant paths before analysis. Do not send code
or metadata to an external model without exact authority and provider controls.
Generated scratch defaults to an owned ignored temporary location and is deleted
or retained only under the task's evidence policy.

The fallback does not install/build dependencies, dispatch an internal agent
swarm, redirect writes to a main worktree, create a persistent knowledge graph,
start a server/browser/dashboard, enable hooks, or commit generated data.

## Change impact

Bind impact analysis to the base and candidate revisions. Start with changed
symbols and follow language-aware callers, dependents, contracts, tests, data,
configuration, and deployment edges only as far as the current risk requires.
A graph edge or one-hop neighbor means “inspect,” not “is affected.” Confirm
callsites and behavior with source and executable checks.

If the map is stale, partial, malformed, or missing files, state the exact limit.
It cannot support completeness, review, acceptance, or “no impact” claims.

## Output

Return a compact project/subsystem map, relevant paths and symbols, verified
structural relationships, source-linked semantic hypotheses, changed-risk areas,
and explicit omissions. Do not dump a full graph into context.
