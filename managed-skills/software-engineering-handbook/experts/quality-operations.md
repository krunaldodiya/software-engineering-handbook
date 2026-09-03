# Quality and operations experts

Load only the section selected by the canonical router and apply it with the
owning handbook chapter.

## Incremental implementation and TDD

Original skills: `incremental-implementation`, `test-driven-development`.

Deliver the smallest safe vertical slice. For a changed permanent observable
contract, start with one discriminating failing check, implement the minimum
root-cause change, then refactor under green evidence. Use the handbook's
risk-based deviations when a test cannot precede the change. Do not commit a
scaffold, mock-only path, or layer without end-to-end behavior.

## Browser verification and debugging

Original skills: `browser-testing-with-devtools`,
`debugging-and-error-recovery`.

Exercise the actual browser or runtime surface. Inspect semantic UI state,
console, network, storage, and performance only as required by the failure.
Debug by reproducing, observing/localizing, tracing backward, comparing a known
good path, testing one hypothesis, repairing the source, and challenging the
fix. Stop and reassess architecture or hidden shared state after repeated
materially distinct failed fixes. Never hide the error or replace real evidence
with a fallback that claims success.

## Review and simplification

Original skills: `code-review-and-quality`, `code-simplification`.

Review exact stable bytes against the governing contract, likely failure modes,
and current risk. Separate blockers from optional improvements. Verify feedback
against source, make bounded corrections, and re-review changed risk boundaries.
Simplify only after behavior is understood; preserve external contracts and
Chesterton's Fence for unknown constraints. Use the Ponytail expert for a
focused over-engineering pass.

## Security and hardening

Original skill: `security-and-hardening`.

Identify assets, trust boundaries, actors, abuse paths, authorization, data
classification, secrets, dependency and provenance risk, logging/privacy, and
failure containment. Validate at boundaries, use least privilege and secure
defaults, and fail closed for authorization or evidence-integrity failures.
Security review cannot be replaced by a checklist, self-review, or a successful
build.

## Performance optimization

Original skill: `performance-optimization`.

Optimize only a measured requirement or regression. Capture a representative
baseline, isolate the bottleneck, change one causal factor, and compare latency,
throughput, memory, allocation, network, and cost as applicable. Preserve
correctness and resource limits. A microbenchmark or local metric does not prove
user-visible or production improvement without representative conditions.

## Git, CI/CD, and versioning

Original skills: `git-workflow-and-versioning`, `ci-cd-and-automation`.

Keep change sets coherent and reviewable. Use repository-native isolation,
branch, commit, review, merge, signing, and hosted-gate rules. Automation must be
deterministic, fail closed, expose complete failure evidence, and bind artifacts
to the exact source. Do not create commits, push, alter protected settings, or
trigger deployment without authority.

## Deprecation, documentation, and ADRs

Original skills: `deprecation-and-migration`, `documentation-and-adrs`.

A compatibility window needs owner, consumers, telemetry/evidence, migration
path, deadline or review event, and removal condition. Clean cutovers remove
obsolete aliases and paths. Documentation records current behavior and why;
ADRs are for material durable decisions, not routine code choices. Update every
affected contract document in the same governed change and remove stale claims.

## Observability and launch

Original skills: `observability-and-instrumentation`, `shipping-and-launch`.

Instrument only decision-useful signals: structured privacy-safe logs, metrics,
traces, health, and alerts tied to user or operator symptoms. State ownership,
cardinality, retention, and redaction must be explicit. Launch requires exact
artifact identity, staged exposure where risk warrants, rollback, monitoring,
owner authority, and post-release evidence. Feature flags need lifecycle and
removal; they are not permanent architecture.

## Evidence

Every selected section inherits the handbook's exact-subject verification,
independent review, and delivery rules. Load no unrelated section merely because
this module is selected.
