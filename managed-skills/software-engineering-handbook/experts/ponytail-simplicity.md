# Ponytail simplification expert

Use for coding, refactoring, dependency choices, or an explicit
over-engineering review after the canonical router selects this fallback.

## Implementation ladder

Understand the task and trace the affected flow first. Then stop at the first
rung that completely satisfies the contract:

1. Do not build a speculative capability.
2. Reuse the repository's established helper, type, pattern, or configuration.
3. Use the standard library.
4. Use a native platform feature.
5. Use an already approved and installed dependency.
6. Use the smallest direct implementation.

Root-cause placement beats a smaller symptom patch. Prefer deletion over
addition and boring code over a new abstraction. Do not add a dependency,
interface with one implementation, factory for one product, configurability for
a fixed value, compatibility alias after a clean cutover, or scaffolding for a
future requirement.

## Non-negotiable boundaries

Minimalism MUST NOT remove explicit scope, trust-boundary validation,
authorization, privacy, security, data-loss protection, accessibility,
error handling, evidence, or required tests. Physical and environment-dependent
systems retain necessary calibration and safety controls. A user-requested full
implementation remains full scope.

A deliberate simplification with a proven ceiling may carry one concise
`ponytail:` comment naming the ceiling and upgrade condition. Do not use the
comment to excuse a current defect or requirement.

## Review and audit

For a changed diff, report one actionable line per removable complexity:
location, what to delete or simplify, and the existing/native replacement. For
a repository audit, rank only evidence-backed opportunities; do not mutate.
Harvest `ponytail:` comments into a debt ledger only when requested.

Benchmark scoreboards, help text, intensity modes, hooks, global state, and
subagent injection are not engineering controls in this fallback.

## Evidence

The result must remain the smallest complete diff and pass the changed path's
observable verification. Compare behavior, not line count. When two solutions
are equally small, choose the one with safer edge-case behavior.
