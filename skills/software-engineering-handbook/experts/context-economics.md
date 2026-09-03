# Context and usage economics expert

Use only when context pressure, token consumption, monetary cost, repeated tool
payloads, model choice, or agent orchestration cost is a current decision. This
is one internal specialist inside the handbook package, not another installed
skill.

## Diagnose context degradation

Before reducing context, distinguish the failure:

- **lost-in-middle** — a present fact or instruction is ignored;
- **poisoning** — an incorrect claim or tool result keeps propagating;
- **distraction** — irrelevant material competes with the current decision;
- **confusion** — constraints from separate tasks are mixed; or
- **clash** — authoritative-looking sources conflict by version or scope.

Verify that the same task works with a small clean context before blaming window
size, and use repeated observations when normal model variance is plausible.
Remove poisoned or stale material instead of layering corrections over it.
Resolve clashes through authority and version precedence. Choose the smallest
adequate response: write bulky state outside the window, select less input,
compress relevant history, or isolate genuinely independent work.

## Preserve value before reducing tokens

Optimize successful work per unit cost, not token count in isolation. Required
authority, project facts, contracts, uncertainty, safety controls, and acceptance
evidence stay in context. A cheaper run that guesses, repeats work, or misses a
boundary is not an optimization.

Set a finite task-local budget when the host exposes reliable measurements:
model and reasoning level, input and output tokens, calls, tool or agent fan-out,
elapsed time, and monetary cost. Treat provider estimates and cached-token
accounting as provider-specific evidence, not universal facts.

## Reduction order

Apply the first adequate reduction and stop:

1. Remove duplicate routers, overlapping skills, repeated instructions, and
   already-settled context.
2. Load only the governing section, affected source, changed-contract tests,
   exact error, and one established pattern. Keep the catalog and unrelated
   files cold.
3. Reuse an unchanged in-context source. Prefer stable prompt prefixes and
   provider caching when available; rewriting a cacheable prefix can cost more
   than the tokens removed.
4. Replace large or superseded tool output with a recoverable reference or
   concise factual summary. Compact only at a safe semantic boundary and retain
   decisions, file state, failures, evidence, and next action.
5. Use one agent for coupled work. Delegate only genuinely independent slices
   whose parallel or specialist value exceeds duplicated setup and context.
6. Use the least costly model and reasoning level that can satisfy the current
   risk and acceptance contract. Escalate for consequential ambiguity or failed
   evidence, not by default.
7. Bound retries, searches, generated output, and repeated reviews. Stop when the
   decision is supported or the exact missing prerequisite is known.

## Context compression and continuity

Mask duplicate, superseded, or resolved tool output behind a retrievable
reference before summarizing the remaining history. Never compress active error
evidence, governing instructions, tool schemas, code, commands, URLs, paths,
symbols, revisions, numeric values, or other exact identifiers needed to
continue.

Prefer anchored incremental summaries over repeatedly regenerating the full
summary. Preserve explicit sections for goal and authority, decisions, files
read and changed, exact failures, verification state, residual risks, and next
action. Keep the source or immutable artifact recoverable until continuation
probes confirm factual recall, artifact tracking, decisions, and next action.
Monitor repeated re-reading or re-derivation: rising re-fetch cost means the
compression was too aggressive.

When changing tasks or resuming a cold session, start with a lean project-bound
handoff instead of replaying unrelated history. Never move private context
across projects or users.

## Harness audit and cleanup

Inventory every recurring context surface before optimizing it: system and
project instructions, skill descriptors, tool and MCP schemas, memory,
retrieved documents, hooks, conversation history, and tool output. Attribute
observed tokens or bytes and usage frequency where the host exposes them, then
rank duplicate, unused, or oversized surfaces by recoverable cost and risk.

Before disabling or rewriting a surface, check dependents and authority, keep a
human-readable backup outside auto-discovered directories, present the exact
change when approval is required, and remeasure after a fresh session. The
handbook and its own experts are not exempt from this audit. Do not add daemons,
keep-warm probes, telemetry, or a second optimization package merely to save
tokens.

## Measurement and claims

Analyze total tokens and cost per successful task, not one request. Include
failed retries, re-fetching, compaction, coordinator and subagent setup, and
tool calls. Check model-to-task fit, cache utilization, redundant agent work,
oversized recurring instructions or schemas, and output that could remain
retrievable outside the window.

Compare a baseline and candidate on the same task boundary, model/provider,
inputs, cache state, and acceptance check where practical. Record observed
input, output, cached, and reasoning tokens when exposed; calls, latency, cost,
and whether the task passed. Separate startup, main-agent, subagent, tool, and
compaction cost when the host reports them separately.

Never claim savings from a hypothetical baseline, a different workload, list
price alone, or token count that excludes failed retries and orchestration.
Published ratios and thresholds are source- and model-specific starting points,
not defaults. Qualitative changes may be reported as design decisions, not
measured savings.

## Host controls

Use native usage and compaction controls instead of adding another dependency.
For OMP, `omp stats` inspects session usage, `omp usage` inspects provider limits,
and `/compact` is available when a safe summary boundary is reached. Use more
specialized pruning or compaction only when configured and verified for the
active model; do not compact reflexively when a stable cached prefix is cheaper.
Other harness adapters should bind equivalent commands without changing this
contract.

## Evidence

Return the chosen reduction, preserved context, observed before/after metrics
when available, acceptance result, and limits. If reliable billing or cache data
is unavailable, say so and report only the measurements actually observed.
