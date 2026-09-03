# Context and usage economics expert

Use only when context pressure, token consumption, monetary cost, repeated tool
payloads, model choice, or agent orchestration cost is a current decision. This
is one internal specialist inside the handbook package, not another installed
skill.

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

## Measurement and claims

Compare a baseline and candidate on the same task boundary, model/provider,
inputs, cache state, and acceptance check where practical. Record observed input,
output, cached, and reasoning tokens when exposed; calls, latency, cost, and
whether the task passed. Separate startup, main-agent, subagent, tool, and
compaction cost when the host reports them separately.

Never claim savings from a hypothetical baseline, a different workload, list
price alone, or token count that excludes failed retries and orchestration.
Qualitative changes may be reported as design decisions, not measured savings.

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
