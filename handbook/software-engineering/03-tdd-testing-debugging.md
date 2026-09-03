# TDD, Testing, and Debugging

## Purpose

This chapter defines how to challenge behavioral claims, prevent known defects from returning, debug from evidence, and optimize measured constraints. Its goal is justified confidence in observable behavior, not a maximum test count, a prescribed test shape, or ritual compliance with a named method.

The guidance is lifecycle- and tool-neutral. It is informed by the scalable test-process scope of [ISO/IEC/IEEE 29119-2:2021](https://www.iso.org/standard/79428.html), the test-first and red–green–refactor practice described by the [Agile Alliance TDD glossary](https://agilealliance.org/glossary/tdd/), and the evidence-driven narrowing model documented in the [Git bisect manual](https://git-scm.com/docs/git-bisect/2.54.0). These links establish useful practice boundaries; they do not by themselves establish conformance to an external standard. The handbook's curated source notes and limitations are in [references.md](references.md#testing-and-debugging).

## Applicability and ownership

Select this chapter when work:

- adds, removes, or changes observable behavior, an invariant, interface semantics, state transitions, failure handling, or a quality claim;
- repairs or investigates a defect, incident symptom, regression, or intermittent failure;
- changes code whose risk warrants regression protection even when its public shape is unchanged;
- creates, changes, quarantines, or deletes tests and test data; or
- makes a performance, capacity, latency, allocation, or resource-use claim.

This chapter owns test strategy, red–green–refactor, test determinism and isolation, regression construction, debugging evidence, flaky-test handling, and measurement before optimization. It does not define CI configuration, merge or release authority, product requirements, architecture policy, or work-item slicing. Those decisions belong to the corresponding handbook chapter and project adapter.

A one-off experiment or investigation whose result will not become a maintained behavior MUST be run and observed, but it need not create a permanent automated test. If the investigation produces a permanent fix or contract, the applicable regression and changed-contract rules begin at that point.

## Normative rules

### 1. Start with falsifiable claims

Before selecting a test or experiment, the change owner MUST state the observable claim being challenged and the failure that would disprove it. For a defect, this includes the observed symptom and the expected behavior. For a quality claim, it includes the metric, workload or input distribution, environment, and acceptance threshold.

Verification MUST target observable behavior, boundary semantics, invariants, or failure modes. It MUST NOT test implementation plumbing merely to mirror the current code structure. An internal component MAY be tested directly when it is the narrowest stable boundary that can falsify the claim, or when its state space or failure consequences justify focused checks.

A permanent new or changed observable contract MUST receive durable regression protection when a deterministic automated check is feasible and materially reduces the risk of recurrence. If automation is infeasible or would be less trustworthy than another method, the change MUST have substitute verification and a documented exception under this handbook's exception model.

Tests SHOULD be written before production implementation for a permanent changed contract or defect repair. A deviation is acceptable when the test harness itself must first be made observable, when discovery is genuinely exploratory, or when the behavior can only be exercised in an environment unavailable during implementation. The deviation record MUST state the reason, the substitute feedback used meanwhile, and when durable regression protection will be established; “the change is small” is not a sufficient reason.

### 2. Use red–green–refactor as a controlled loop

For test-first work, each loop MUST satisfy these stop conditions:

1. **RED — establish discriminatory failure.** Add or select the smallest check that expresses one missing or incorrect behavior. Run it against the pre-change behavior. RED stops only when the check fails for the expected behavioral reason, not because of syntax, setup, unavailable infrastructure, unrelated failures, or an assertion that can never pass. If the behavior already passes, revise the claim or test; do not manufacture a failure.
2. **GREEN — satisfy the claim.** Make the smallest coherent production change that satisfies the behavior. GREEN stops only when the new check passes, directly related checks remain passing, and no observed warning or failure has been relabeled, skipped, or weakened to obtain green.
3. **REFACTOR — improve without changing behavior.** Remove duplication, clarify names and boundaries, or simplify design while preserving the contract. REFACTOR stops when the intended structural improvement is complete, the checks that established green still pass unchanged, and no new material design concern remains within the slice.

A loop MUST NOT proceed from a RED caused by an unknown mechanism. A test MUST NOT be relaxed merely because the implementation fails it. Production behavior and test expectation must be reconciled against the authoritative contract.

Test-first is a feedback technique, not a prohibition on design, exploration, review, static analysis, runtime observation, or later broader testing. A spike MAY be discarded and then reimplemented through the controlled loop; exploratory code MUST NOT be presented as completed production behavior without applicable verification.

### 3. Build the test portfolio from risk

The test portfolio MUST be selected from failure consequence, likelihood, detectability, change reach, and uncertainty rather than from a fixed ratio of test categories. The least expensive stable check that can falsify a claim SHOULD be placed closest to the behavior, with broader checks added where they expose distinct integration, deployment, or end-to-end failure modes. Omitting a recommended broader or narrower check requires a recorded reason and residual-risk assessment.

At minimum, consider the following claim types:

| Risk or claim | Useful test focus |
|---|---|
| Pure rule, calculation, parser, or transformation | examples at equivalence boundaries; invariants; invalid and extreme inputs |
| State or workflow change | valid and invalid transitions; idempotency; ordering; interruption; retry and recovery semantics |
| Interface or dependency boundary | request/response or data-shape contract; compatibility; timeout, partial failure, and malformed-result behavior |
| Persistence or migration behavior | round trip; constraints; old/new representation; interruption; rollback or forward recovery |
| Concurrency or distributed coordination | competing operations; ordering assumptions; duplicate delivery; lost responses; race-sensitive invariants |
| User- or operator-visible flow | critical path; error and recovery path; accessibility or operability consequences where applicable |
| Performance or resource claim | representative workload; warm-up and variance; saturation or limit behavior; regression threshold |

R1 work needs the smallest behavioral check that can disprove the change. R2 work SHOULD include focused automation plus relevant boundary, negative, and regression checks; omission requires a reason and residual-risk assessment. R3 work MUST include positive, negative, failure, and recovery behavior as applicable, with independent methods when they expose different failures. R4 work MUST use the domain's authorized assurance plan in addition to this chapter; this chapter alone is not sufficient evidence.

Line, branch, or path coverage MAY reveal unexercised areas, but a coverage percentage MUST NOT be treated as proof of behavior or used as the sole acceptance gate. Test count and snapshot size are likewise not confidence measures.

### 4. Require useful tests

A maintained test SHOULD satisfy all of these quality criteria:

- **Discriminating:** it fails for at least one plausible wrong behavior and passed/failed status is not predetermined by its setup.
- **Contract-focused:** assertions describe observable outcomes or invariants rather than incidental call order, private layout, or copied implementation logic.
- **Causally faithful:** the setup reaches the mechanism the claim depends on; substitutes do not bypass the relevant boundary.
- **Repeatable:** identical declared inputs and environment yield the same verdict, or an explicitly statistical verdict stays within a justified error bound.
- **Isolated:** it does not depend on execution order or undeclared mutable state and cannot corrupt another test's data or environment.
- **Specific:** it has one intelligible reason to fail, while allowing multiple assertions that jointly define one behavior.
- **Diagnostic:** its name and failure output identify the scenario, expected property, and useful observed difference without exposing sensitive data.
- **Maintainable:** it uses public or stable seams, keeps essential setup visible, and avoids a second implementation of the production algorithm.
- **Proportionate:** its execution cost and maintenance burden are justified by the risk it controls.

When a SHOULD criterion is intentionally traded off, the review or evidence record MUST identify the criterion, rationale, and consequence. High-cost tests SHOULD be retained when they uniquely cover high-consequence behavior; convenience alone is not grounds to delete them.

A test MUST assert a meaningful outcome. Tests that merely execute code, assert a mock's self-programmed return value, duplicate the implementation in the expected value, or depend only on the absence of an exception MUST NOT support an acceptance claim unless that absence is itself the complete contract.

### 5. Make execution deterministic and isolated

Automated tests MUST declare or control every input that can materially change their verdict, including configuration, time, randomness, locale, ordering, identity, permissions, and external state as applicable. Randomized checks MUST record a replayable seed or the generated counterexample.

Tests MUST NOT depend on execution order. Shared mutable resources MUST use unique namespaces or serialized ownership, deterministic setup, and cleanup that is safe after partial failure. A test MUST NOT read or mutate real user or production data unless an explicitly authorized assurance procedure requires it.

Time- and concurrency-sensitive checks SHOULD wait on observable conditions or controlled clocks rather than fixed sleeps. A fixed delay MAY be used only when the delay itself is the contract or when no observable synchronization point exists; the reason and maximum bound MUST be explicit.

A narrow test MAY replace an external collaborator, but the replacement MUST preserve the semantics relevant to the claim. Boundary-contract or integration checks SHOULD challenge assumptions made by substitutes. A test double MUST NOT be used to claim that the real integration works.

Inherently probabilistic behavior MAY use statistical tests when deterministic examples cannot adequately test the property. Such a test MUST define the population or generator, sample size, decision threshold, acceptable false-positive/false-negative risk, replay data where possible, and a bounded runtime. “Usually passes” is not an acceptable verdict.

### 6. Use generative techniques only where they add fault-finding power

Example-based tests remain the default when a few cases clearly specify the contract. Additional techniques SHOULD be selected only when their distinct fault model justifies their cost:

- **Property-based testing** is useful for large or combinatorial input spaces with stable invariants. Properties MUST be narrower than “does not crash,” generators MUST include meaningful boundary classes, and minimized counterexamples and seeds MUST be retained for replay.
- **Metamorphic testing** is useful when a direct oracle is unavailable or expensive but a transformation implies a known relation between outputs. The relation and its applicability preconditions MUST be stated independently of the implementation.
- **Mutation testing** is useful for assessing whether a critical test set detects plausible faults. Surviving mutants MUST be classified as equivalent, irrelevant to the claimed risk, or evidence of a test gap. Mutation score MUST NOT become an unqualified universal target, and generated mutations MUST NOT be shipped as production changes.

A team MAY sample these techniques on the highest-risk rules or modules rather than apply them repository-wide. Declining a SHOULD technique requires a concise rationale when the identified fault class remains material.

### 7. Construct regressions from the root cause

A defect repair MUST begin with the smallest reliable reproduction available. When feasible, convert that reproduction into an automated test and observe it fail against the defective behavior before changing production code.

The regression test MUST encode the intended contract at the boundary where the defect should have been prevented, not merely the exact reported payload or an accidental implementation detail. It SHOULD include the triggering boundary case and, when inexpensive, a neighboring non-triggering case that prevents overfitting. If the root cause represents a class of inputs, a property or equivalence class SHOULD replace a single anecdotal example; omission requires a reason and residual-risk assessment.

A regression is complete only when all of the following stop conditions hold:

1. the original symptom is reproducible or the inability to reproduce is bounded and recorded;
2. the pre-fix check fails for the expected reason;
3. the fix makes that check pass without weakening it;
4. directly related positive, negative, and boundary behavior remains passing; and
5. the root-cause explanation accounts for both the failure and why the change prevents recurrence.

If a production-only defect cannot be recreated safely, the repair MUST use the closest faithful model, preserve sanitized evidence of the original symptom, identify mismatches between model and production, and obtain the risk-tier-appropriate exception or authorization before making a completion claim.

### 8. Debug by narrowing evidence, not accumulating guesses

Debugging MUST preserve the observed facts separately from hypotheses. Before editing, establish the smallest reliable reproduction or define a bounded reproduction attempt: exact input and preconditions, environment and revision, expected and actual result, frequency, and a fixed time or sample limit. Failure to reproduce within that bound is evidence of uncertainty, not evidence that the defect is absent.

Investigation SHOULD reduce one uncertainty at a time using controlled input changes, state inspection, instrumentation, comparison with a known-good case, or history narrowing. A historical bisection is one useful example of evidence-driven narrowing, as documented by the [Git project](https://git-scm.com/docs/git-bisect/2.54.0); no particular version-control command is required. Departing from one-factor-at-a-time narrowing requires a reason, such as unsafe reproduction or interacting variables, and must preserve enough observation to distinguish hypotheses.

A root-cause claim MUST identify a causal mechanism and supporting observation. Correlation with a line, revision, log message, or timing change is not sufficient by itself. The strongest practical confirmation is an intervention: changing or controlling the suspected cause changes the result while relevant alternatives remain controlled.

A systematic investigation SHOULD proceed in four explicit phases:

1. **Observe and localize.** Read the complete failure evidence, reproduce or
   bound reproduction, inspect relevant recent changes, and trace the bad state
   backward across component boundaries. Add temporary, privacy-safe
   instrumentation only where it distinguishes which boundary first violates
   the contract.
2. **Compare patterns.** Find the closest known-good path, compare its inputs,
   environment, dependencies, state, and control flow with the failing path,
   and list differences before selecting one as causal.
3. **Test one hypothesis.** State one causal hypothesis and the observation
   that would falsify it. Use the smallest safe intervention that changes one
   relevant variable, then accept, reject, or refine the hypothesis from the
   observed result.
4. **Repair and challenge.** Construct the regression required by §7, change
   the causal unit rather than the symptom, and challenge related positive,
   negative, boundary, interruption, and recovery behavior as applicable.

After the causal mechanism is established, the owner SHOULD assess whether one
additional independent guard at an earlier input, state-transition, effect, or
storage boundary materially reduces recurrence or blast radius. Each retained
layer MUST own a distinct invariant and failure outcome; duplicating the same
check everywhere without an ownership or threat rationale is not
defense-in-depth.

After three unsuccessful materially distinct fix attempts, further patching
MUST pause for an explicit reassessment of the architecture, contract, shared
state, or reproduction model. The record MUST list the attempted hypotheses,
what each result established, and whether the next action is a new evidenced
root-cause path, an authorized structural change, or a bounded stop. Rewording
the same hypothesis or stacking another symptom guard does not reset the count.

Debugging stops only in one of these states:

- **Resolved:** the reproduction fails before the fix, passes after it, related behavior remains valid, and the causal explanation fits the observations.
- **Bounded non-reproduction:** the declared attempt limit is reached, collected evidence and environment are recorded, no unsafe speculative fix is shipped, and the next decision is explicitly owned.
- **Blocked:** a required input, access, environment, or authorization is unavailable; the blocker, attempted methods, preserved evidence, and residual impact are recorded.

Masking an exception, increasing a timeout, adding retries, broadening an accepted result, or suppressing a signal MUST NOT be called a root-cause fix unless the authoritative contract establishes that behavior and the causal mechanism is addressed.

### 9. Profile before optimizing

A performance or resource optimization MUST begin with a measurable claim and a representative baseline. The measurement MUST state the metric, workload and data shape, environment, configuration, revision, warm-up or steady-state treatment, sampling method, and observed variance. Optimization MUST target an observed constraint or hotspot; intuition alone is insufficient for a material performance claim.

Measurement overhead and environmental noise MUST be assessed when they could change the conclusion. Comparisons MUST hold relevant variables constant or explain their differences. A faster micro-operation MUST NOT be used to claim end-to-end improvement without evidence that it contributes materially to the end-to-end constraint.

Optimization stops when one of these conditions is recorded:

- the declared target is met and behavioral checks show no correctness regression;
- measurement shows the suspected hotspot is not material, so the proposed optimization is abandoned;
- the next improvement would violate a more important quality, safety, or resource constraint; or
- the predeclared experiment bound is reached without a reliable improvement, with results and remaining uncertainty recorded.

The final evidence MUST compare baseline and candidate under equivalent conditions and report absolute values, relative change where useful, variance, correctness checks, and known limits. An optimization that does not produce a repeatable material improvement SHOULD be reverted; retaining it requires a recorded reason such as a separately demonstrated capacity or tail-risk benefit.

### 10. Treat flaky tests as defects in the evidence system

A flaky test is one whose verdict changes without a relevant declared change in the behavior under test. A failing run MUST remain a failure until its cause is understood; rerunning to obtain green MUST NOT erase or supersede the original result.

On detecting flakiness, the owner MUST preserve the failing seed, input, ordering, environment, revision, and output available; determine whether the product, test, environment, or an undeclared dependency is nondeterministic; and create a bounded path to repair.

A flaky test MAY be quarantined only when continued execution causes more decision harm than temporary removal and the applicable risk owner accepts the gap. Quarantine MUST record the behavior no longer guarded, owner, entry evidence, compensating check, repair or removal condition, and expiry or review date. A quarantined result MUST NOT count as passing evidence for its claim.

Flake repair stops only when the causal source is removed or explicitly controlled and the test passes the declared stress or repetition bound without hiding failures. If that bound cannot provide adequate confidence, the gap remains open or requires an approved exception. Repeated retries MAY be part of a product's actual retry contract, but test-runner retries MUST NOT be used as the sole flake remedy.

### 11. Verify the claim before transition

Immediately before a completion, fixed, passing, review-ready, handoff, or
release claim changes lifecycle state, the claimant MUST:

1. identify the check or observation that can falsify the exact claim;
2. establish that it applies to the exact candidate, artifact, configuration,
   environment, and relevant external state;
3. run it freshly, or cite retained output from the same unchanged subject when
   no material source, dependency, configuration, environment, or temporal
   premise has changed;
4. inspect the complete result, exit status, failures, warnings, skips, and
   limits rather than infer success from partial output; and
5. state the claim no more broadly than the observed evidence permits.

An agent, implementer, or tool report is an input to verification, not proof of
the underlying claim. A changed candidate invalidates affected evidence and
review. Conversely, an expensive check MUST NOT be repeated merely to place it
in the same message or ceremony when retained exact-subject evidence remains
fresh and inspectable; evidence freshness is determined by invalidating change,
not conversational turn count.

## Lightweight workflow

Use the smallest loop that satisfies the change's risk tier:

1. **State the claim and risk.** Identify observable behavior, plausible failure, affected boundary, and consequence.
2. **Choose the falsifier.** Select the narrowest faithful test, experiment, review, or measurement; add independent methods only for distinct failure modes.
3. **Establish the baseline.** For changed behavior, observe RED or record why test-first is inapplicable. For defects, reproduce. For optimization, measure.
4. **Change one causal unit.** Implement the smallest coherent behavior or controlled diagnostic intervention.
5. **Challenge boundaries.** Exercise relevant negative, edge, failure, recovery, and integration behavior in proportion to risk.
6. **Refactor without weakening evidence.** Improve structure while keeping behavior checks intact.
7. **Record the result and limits.** Bind evidence to the revision, environment, configuration, and claim.
8. **Stop explicitly.** Use the RED–GREEN–REFACTOR, regression, debugging, profiling, or flake stop condition above. Do not substitute elapsed effort or a green unrelated suite.

A one-off investigation follows steps 1–4 and 7–8 with runtime evidence; it does not require a permanent test unless it creates a maintained contract or repair.

## Evidence and acceptance gates

Every testing or debugging acceptance claim MUST use the handbook evidence fields: claim, method, context, result, coverage and limits. In this chapter, the record SHOULD additionally include:

- the test or reproduction identity and the behavior boundary it exercises;
- pre-change RED evidence for test-first work or defects, or the reason it is unavailable;
- exact focused checks and relevant broader checks observed after the change;
- seeds, generated counterexamples, schedules, test data class, or statistical bounds when relevant;
- profiling workload, baseline, candidate measurement, variance, and environment when relevant;
- skipped, quarantined, flaky, blocked, or not-run checks without concealment; and
- sensitive-data redaction and retention appropriate to risk.

Acceptance MUST stop when a required check fails, is flaky, cannot run, or was run against a different non-equivalent revision. Work MAY continue to diagnose or repair, but the affected claim remains unproven. Acceptance resumes only when the check passes deterministically on the candidate context, equivalence is established, or an authorized exception supplies compensating evidence.

A focused check is necessary evidence for the changed behavior but does not replace a broader gate required by the risk tier or project adapter. Conversely, a broad passing suite MUST NOT replace a missing targeted reproduction or falsifiable changed-contract check.

The evidence is sufficient when every material changed claim has at least one faithful falsifier, every applicable risk-tier check has an observed result, no relevant failure is hidden, and limits and residual risk are explicit. More tests are not required once those conditions and the applicable stop condition are met.

## Exceptions and justified deviations

Departures from a MUST or MUST NOT rule require the handbook exception record: exact rule and scope, reason, authorized owner, risk and affected assets, compensating controls and substitute evidence, and expiry or removal condition. A failed test cannot be excepted into a pass; an exception accepts a bounded risk while keeping the evidence status truthful.

Departures from a SHOULD or SHOULD NOT rule do not require formal approval unless the project adapter or risk tier says otherwise. They do require a discoverable reason and consequence assessment at the change or review. Valid reasons can include a less expensive method with equal fault-finding power, an inherently non-deterministic domain with a justified statistical oracle, or a broader boundary that is more causally faithful than a narrow test. Schedule pressure, test inconvenience, an unfamiliar tool, or a desire for a green result are not sufficient by themselves.

Emergency repair MAY defer durable regression construction only through an authorized emergency process with immediate substitute verification, preserved evidence, a named owner, and a time-bounded follow-up. The emergency does not waive truthful reporting or higher-authority safety and access rules.

## Anti-patterns

- Writing the implementation first by habit, then adding a test that can only pass.
- Testing private call sequences, mocks, or data layout instead of the contract they support.
- Reproducing a reported value without capturing the general boundary or invariant that failed.
- Changing production code and the expected result together without observing a discriminating RED.
- Using snapshot volume, test count, or coverage percentage as a proxy for behavioral assurance.
- Replacing every collaborator so the test no longer exercises the risky integration.
- Sharing mutable fixtures, relying on suite order, using real clocks unnecessarily, or sleeping until a race “usually” finishes.
- Generating random cases without replayable seeds or accepting intermittent failures as normal.
- Applying mutation, property, or metamorphic testing repository-wide without a fault model that justifies the cost.
- Retrying a failing test until green, silently quarantining it, or counting quarantine as success.
- Fixing a symptom by swallowing errors, extending timeouts, or adding retries without establishing the causal mechanism and contract.
- Optimizing a microbenchmark before showing that the measured operation constrains the relevant outcome.
- Running every available check when a focused falsifier would answer the question, or running only a focused check when distinct system risks remain.
- Adding permanent test scaffolding to a disposable investigation that creates no maintained behavior.

## Project-adapter hooks

A project adapter SHOULD bind this chapter to the local environment by defining only what is needed:

- authoritative behavioral contracts, critical invariants, risk triggers, and required test categories;
- supported focused and broader test commands, environments, data factories, and fixture ownership;
- boundaries for unit, component, contract, integration, system, acceptance, and operational checks without mandating fixed portfolio ratios;
- deterministic clock, randomness, concurrency, identity, network, storage, and cleanup conventions;
- approved test doubles and the real-boundary checks that validate their assumptions;
- coverage uses and exclusions, explicitly stating that coverage alone is not acceptance;
- property, metamorphic, mutation, fuzz, load, stress, and statistical-test selection criteria and execution bounds;
- defect-reproduction, profiling, benchmark, and sanitized diagnostic-evidence formats;
- flaky-test detection threshold, stress/repetition bound, quarantine owner, maximum quarantine duration, and exception location;
- commands or procedures for targeted checks and the broader gates required by each local risk tier; and
- evidence retention, sensitive-data handling, and the system of record for exceptions.

Adapters SHOULD encode stable rules in executable configuration where practical and keep human-readable guidance aligned with those gates. Exact frameworks, commands, thresholds, directory layouts, providers, and approval roles belong in the adapter, not this chapter.
