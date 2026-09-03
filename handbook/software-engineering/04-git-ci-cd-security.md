# Git, CI/CD, and Security

## Purpose

This chapter protects the integrity of a change from selection through review, integration, build, release, deployment, and vulnerability response. Its universal outcomes are provider-neutral: coherent revisions, protected integration, exact-revision evidence, fail-closed gates, least privilege, controlled secrets, known inputs, verifiable artifacts, reversible delivery, and accountable response.

The rules are informed by the outcome-oriented [NIST Secure Software Development Framework (SSDF) 1.1](https://doi.org/10.6028/NIST.SP.800-218), the source and build integrity models in [SLSA 1.2](https://slsa.dev/spec/v1.2/), and version-qualified, verifiable application-security requirements in [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/). These references guide control design; citing or following this chapter alone does not establish conformance, certification, or a particular SLSA level.

## Applicability and boundary

Select this chapter when work changes or relies on:

- version-control history, protected references, review, or merge policy;
- CI workflows, runners, credentials, required checks, or evidence retention;
- dependencies, package sources, build tools, generated outputs, or artifact stores;
- signing, attestations, software bills of materials, provenance, or release archives;
- deployment authorization, environments, promotion, rollback, or emergency release paths;
- secrets, privileged automation, vulnerability intake, remediation, or disclosure; or
- a security or supply-chain assurance claim.

This chapter owns change-set integrity and pipeline, artifact, release, and secure-development controls. Chapter 3 owns how tests and debugging are designed; this chapter owns when their results become integration or release gates. Chapter 1 owns product authority and lifecycle decisions; this chapter ensures that authorized decisions are enforced and evidenced in delivery systems. Chapter 5 owns work slicing; this chapter applies the narrower requirement that accepted revisions remain coherent and reviewable.

Apply the [handbook risk tiers](README.md#risk-tiers). Small diff size does not lower the risk of a privilege, secret, dependency, pipeline, or release-path change.

## Universal control outcomes

The rules in this section state outcomes every project can implement without adopting a particular hosting provider, branch model, CI product, registry, signing service, or deployment platform. Concrete configuration belongs in a project adapter.

### GCS-1 — Coherent, reviewable revisions

1. Every accepted source revision MUST be uniquely identifiable and its parentage and change content MUST be reviewable. A mutable branch, tag, channel, or release name MUST NOT be used as the sole identity of evidence or an artifact.
2. A commit SHOULD contain one coherent purpose and only its implementation, directly necessary tests, migration/configuration, and documentation. Unrelated formatting, refactoring, dependency updates, or features SHOULD NOT be mixed into it.
3. A departure from the preceding SHOULD rules is justified when an indivisible generated change, coordinated schema migration, mechanical transformation, or other cross-cutting operation is safer as one revision. The review record MUST then explain why it is indivisible and provide a practical way to inspect the parts.
4. The author MUST inspect the selected change set before publication. “Atomic” means logically cohesive, independently explainable, and safe to accept or reject; it does not impose a line, file, or commit-count limit. Selective staging is one possible mechanism, as illustrated by the [Git staging model](https://git-scm.com/docs/git-add), not a universal tool requirement.
5. Each revision admitted to a protected baseline MUST leave that baseline in a valid state under its required gates. A repository MAY use a reviewed squash or equivalent integration strategy when the final admitted revision, rather than every private work-in-progress revision, satisfies this rule.
6. Protected history MUST NOT be rewritten or protected release references moved. A legal or privacy expunging process is the narrow exception: it MUST be authorized, preserve a private audit record where lawful, assess downstream impact, and publish replacement identities or consumer guidance as appropriate. SLSA describes why continuous history and immutable revisions matter in its [source requirements](https://slsa.dev/spec/v1.2/source-requirements).

7. Concurrent, high-risk, or interruption-prone work SHOULD use the
   repository or harness's native isolated workspace mechanism when isolation
   reduces shared-state risk. Before mutation, the executor MUST identify the
   baseline, workspace, branch or equivalent change identity, ownership, and
   allowed integration path.
8. Isolation MUST NOT be improvised by installing an unapproved tool or
   dependency, copying sensitive state, weakening protections, or creating a
   second source of repository truth. A new workspace dependency follows
   GCS-6.
9. Cleanup MUST target only an owned, inactive workspace after required state,
   evidence, and recovery information are retained. Unknown user work,
   untracked material, active agents, or a workspace still needed for review or
   recovery MUST NOT be deleted for cosmetic cleanup.

### GCS-2 — Protected integration and final-revision review

1. Every shared baseline from which software is released or deployed MUST be protected by enforceable integration policy. The policy MUST prevent unreviewed direct updates, unauthorized deletion or movement of release references, and bypass of required checks.
2. Review MUST cover the actual change and context being accepted, including generated or binary content through a trustworthy human-readable representation or verified provenance. Unreviewable content MUST be treated as a risk, not silently ignored.
3. R3 and R4 changes MUST receive independent review by an actor authorized for the affected risk. An author or automation that can propose a change MUST NOT unilaterally grant the approval required to accept that same high-risk change.
4. Required approval MUST apply to the final revision. If the revision changes after approval, affected approvals MUST be dismissed and the changed result reviewed again. A project MAY retain approval for a demonstrably non-material, policy-defined transformation only when the transformation is trusted, the equivalence is mechanically established, and that exception is visible in evidence.
5. Administrative bypass MUST be disabled by default. An authorized emergency or recovery bypass MUST identify the actor, exact revision, reason, affected controls, time, and required retrospective review. A bypass is an exception, not a successful execution of the bypassed controls.

6. A material review request SHOULD provide one inspectable package containing
   the goal and acceptance criteria, exact base and candidate identities,
   coherent diff or artifact representation, changed contracts and risks,
   observed checks with limits, and known failures or unresolved decisions.
   Reviewers MUST NOT be required to reconstruct material context from mutable
   chat, branch names, or scattered summaries.
7. Review feedback MUST be evaluated as a technical claim against the
   authoritative contract and stable candidate. The receiver MUST verify the
   cited behavior or source, classify whether it violates a current acceptance
   condition or control, and record a reason when accepting, rejecting, or
   deferring a material finding. Blind implementation and defensive dismissal
   are both invalid.
8. A correction creates a new candidate and MUST receive verification and
   re-review proportionate to the changed failure surface. A scoped re-review
   MAY verify a bounded correction when the unchanged context and earlier
   verdict remain demonstrably applicable; broader reach requires broader
   review.

These outcomes reflect SLSA’s protected-reference, continuity, human-readable-change, and final-revision review concepts without requiring a specific SLSA level or source-control product.

### GCS-3 — Evidence bound to the exact candidate

1. A required check or review MUST identify the exact immutable source revision to which it applies. When integration produces a different result than the reviewed head, the required gates MUST evaluate the actual integration candidate or establish its equivalence before acceptance.
2. A result from an ancestor, sibling, previous merge attempt, differently configured run, or rebuilt artifact MUST NOT authorize a changed revision or artifact.
3. The evidence record MUST identify the relevant policy/configuration version, environment or runner class, method, result, and produced artifact digest where applicable, consistent with the [handbook evidence model](README.md#evidence-model).
4. Release and deployment decisions MUST use immutable artifact identity, normally a cryptographic digest. Human-readable versions and channels MAY point to that identity but MUST NOT replace it.
5. A gate that cannot reliably bind results to the accepted revision MUST be redesigned, replaced, or explicitly treated as advisory. Advisory evidence MUST NOT satisfy a required gate.

### GCS-4 — Fail-closed CI gates

1. A protected baseline MUST have a small stable set of required checks that can falsify its universal acceptance claims. Additional checks MUST be triggered by changed contracts, risk tier, affected paths, dependency changes, privilege, data, build/release configuration, or other declared risk signals.
2. Required gates MUST include the applicable build or compile checks, behavioral verification, static or security analysis, dependency policy, schema/configuration validation, and release checks. “Applicable” is determined by the project’s declared contracts and risk model; it is not permission to omit a relevant control silently.
3. A failed, missing, skipped, canceled, timed-out, stale, malformed, or indeterminate required check MUST block integration or release. Security findings at or above a project’s blocking threshold MUST fail the gate. They MUST NOT be converted to warnings, unconditional success, ignored exit codes, log-only annotations, or automatic “continue on error” behavior.
4. A security failure can be accepted only through the handbook exception model: the underlying result remains failed, the bounded exception is separately approved, and the acceptance evidence shows both the failure and the exception. The displayed gate state MUST NOT misrepresent failure as success.
5. Path or risk selection MAY add or substitute an equivalent specialized gate, but MUST NOT create an unprotected path around a universal baseline. Rules for changed-files detection and generated configuration are themselves security-sensitive and MUST be reviewed and tested.
6. Required checks MUST be deterministic enough to support acceptance. Re-running until green, concealing retries, or silently quarantining a failing check MUST NOT count as evidence. A temporary quarantine requires an owner, expiry, risk record, and substitute control protecting the same contract.
7. Gate latency SHOULD be reduced by early fast checks, safe caching, and parallel independent jobs rather than by weakening required outcomes. A slower gate MAY be deferred to the release candidate when the adapter states why pre-integration execution is disproportionate, names the protected release point, and prevents release without the result.

NIST SSDF practices PO.3/PO.4 and PW.7/PW.8 support automated evidence and defined security check criteria; SLSA Source describes continuous technical enforcement of claims such as testing before acceptance.

### GCS-5 — Least privilege, trusted execution, and secrets

1. Human and machine identities MUST receive only the permissions, resource scope, and duration needed for their assigned action. Build, review, release, deployment, provenance-signing, and administration authority SHOULD be separated when their compromise has materially different consequences.
2. A combined role is acceptable for low-risk work or constrained teams when its scope is explicit. For R3 or R4, combining proposal with approval, or untrusted build execution with release/signing authority, requires a documented exception and compensating independent verification.
3. Untrusted source, proposed changes, dependency scripts, test inputs, or forked contributions MUST NOT execute in a context that exposes protected secrets, write access to protected resources, release authority, or a reusable privileged runner. Trust MUST be established before crossing into a privileged stage.
4. Automation SHOULD use short-lived, workload-bound credentials. Long-lived credentials are justified only when the environment cannot issue suitable short-lived credentials; the adapter MUST record the limitation, restrict scope, rotate them, and define a migration or review trigger.
5. Secrets MUST be stored in an approved secret-management boundary and MUST NOT be committed to source, embedded in build definitions or artifacts, printed in logs, exposed to untrusted jobs, or passed through an avoidably broad environment. Logs and retained evidence MUST redact secrets in accordance with the [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).
6. Secret access MUST be attributable and revocable. Rotation or revocation MUST occur after suspected disclosure, role change, or compromise according to risk. Removing a secret from the latest source revision is not remediation when history, logs, caches, or artifacts still contain it.
7. A discovered secret exposure MUST be treated as an incident: revoke or contain first, assess every copy and use, rotate dependent credentials, then use the governed expunging process if history cleanup is necessary. The cleanup MUST NOT conceal the incident record.
8. Build and workflow dependencies that can execute code or influence evidence MUST be treated as privileged dependencies. They MUST be pinned to an immutable identity or resolved under an equivalently integrity-protected mechanism, with changes reviewed before privileged use.

### GCS-6 — Dependency and supply-chain control

1. Before adding or materially upgrading a component, the change MUST identify its purpose, origin, selected version or digest, resolution/lock state, transitive impact, applicable license or policy constraints, maintenance posture, and known vulnerability status. A dependency MUST NOT be added when maintained in-project or existing functionality meets the need with lower total risk.
2. Direct and transitive dependencies that affect a release MUST be inventoried at the resolved identities actually built. Lock or resolution metadata MUST be updated and reviewed with the declaring change; manifest-only intent is insufficient when resolution can differ.
3. Sources, package registries, mirrors, build tools, base images, plugins, and workflow components MUST have an explicit trust policy. High-risk inputs MUST use authenticity and integrity verification appropriate to their ecosystem; movable names alone are insufficient where immutable digests or equivalent verification are available.
4. Known vulnerabilities above the adapter’s blocking risk threshold MUST prevent introduction or release unless an authorized, scoped exception records exploitability, exposure, compensating controls, affected versions, owner, and expiry. An unavailable fix does not turn a finding into a warning.
5. Released and supported components MUST be monitored for newly disclosed vulnerabilities and source compromise. Findings MUST be triaged in context—affected version, reachability, exploitability, exposure, and impact—without silently discarding database false positives or uncertain matches.
6. A release SHOULD carry a machine-readable component inventory or SBOM sufficient to identify affected direct and transitive components. If the ecosystem cannot produce a reliable inventory, the release record MUST describe the gap and the alternative method used to answer “which releases contain this component?”
7. Automated update proposals MAY reduce maintenance cost, but the proposing automation MUST NOT approve its own privileged change. Updates remain subject to dependency review, exact-revision gates, and artifact verification.

These outcomes derive from NIST SSDF PW.4 and PS.3 and SLSA’s source/build integrity model. A provider’s dependency-review feature is one adapter, not the universal control.

### GCS-7 — Controlled builds, reproducibility, artifacts, and provenance

1. A release artifact MUST be built from an exact source revision through a declared, version-controlled build definition in a controlled environment. Inputs that can affect output—including dependencies, toolchains, parameters, base environments, and fetched material—MUST be pinned, captured, or explicitly identified as unresolved risk.
2. The build process MUST identify every released output by cryptographic digest. Release artifacts and their integrity metadata MUST be stored immutably or with equivalent write protection and retained according to support, investigation, rollback, and legal needs.
3. The release record MUST link the output digest to its source revision, build definition, builder identity, relevant parameters and resolved dependencies, gate results, and component inventory. For R3 and R4 releases, provenance MUST be authenticated by a trust boundary that the untrusted build steps cannot forge.
4. Provenance MUST be generated contemporaneously with the build by the system best positioned to observe the facts. A build script’s self-authored statement alone MUST NOT be treated as independent proof of the script’s behavior.
5. Builds SHOULD be reproducible for artifact classes where independent rebuilds can meaningfully compare outputs. A justified exception includes unavoidable signing, timestamp, randomized, hardware, or environment inputs; the adapter MUST identify and minimize those sources, define the comparison method, and preserve enough provenance to explain expected differences. Reproducibility MUST NOT be claimed from a single build.
6. R3 and R4 release processes SHOULD perform an independent rebuild or equivalent integrity verification when the project’s threat model depends on reproducibility. Omission requires the risk owner to record why another control gives stronger or more feasible assurance.
7. Build isolation MUST scale with risk. Untrusted builds MUST NOT access provenance-signing material or influence another build. Shared caches MUST be integrity-protected and scoped so that an untrusted producer cannot poison a trusted result. Clean or ephemeral environments SHOULD be used where residue could change output; persistent environments require documented sanitation and integrity checks.
8. Deployment SHOULD promote the already verified artifact by digest rather than rebuild for each environment. If promotion is infeasible, the release record MUST explain why; an environment-specific rebuild or transformation is a new artifact and MUST receive a new identity, provenance link, and applicable verification.
9. Consumers MUST be able to verify artifact integrity before use. Signing MAY provide authenticity, but signatures MUST be checked against an explicit trust policy, and key lifecycle, revocation, and compromise response MUST be defined.

SLSA’s [Build 1.2 requirements](https://slsa.dev/spec/v1.2/build-requirements) distinguish the existence, authenticity, and unforgeability of provenance and progressively stronger hosted and isolated builds. They require a consistent build process, not byte-for-byte reproducibility; this chapter therefore makes reproducibility a risk-scaled recommended default, not an automatic SLSA claim. NIST SSDF PS.2 and PS.3 support release-integrity verification, protected archives, and component provenance.

### GCS-8 — Release, deployment, and recovery

1. Every release MUST have an immutable artifact identity, source revision, applicable gate results, authorization, supported configuration/migration information, and owner. Deployment MUST record the artifact digest actually placed in each governed environment.
2. Release authorization MUST be distinct from mere build success. The authorizer MUST have the declared authority and the evidence needed to evaluate residual risk; CI automation MAY enforce the decision but MUST NOT invent authority.
3. A production-affecting change MUST have a recovery strategy chosen before deployment. It MAY be rollback, roll-forward, feature disablement, traffic isolation, or restore, but it MUST address state, schema, compatibility, dependencies, and security consequences rather than assume an old binary can always be redeployed.
4. R3 and R4 releases MUST provide rollback or containment evidence appropriate to the failure mode. R4 recovery MUST be rehearsed or otherwise independently validated before the irreversible step unless an authorized emergency process records why rehearsal creates greater risk.
5. Deployment SHOULD be staged, progressively exposed, or guarded by health signals when blast radius can be reduced. Direct full deployment is justified when staging is technically meaningless or creates greater risk; the release record MUST state the rationale and the immediate containment signal.
6. Post-deployment verification MUST test the deployed digest and the critical behavior or invariant named by the release. A healthy pipeline is not evidence that production received or can run the intended artifact.
7. Rollback or containment MUST preserve forensic evidence and MUST NOT hide a failed release. The incident, affected identities, observed result, and final disposition MUST remain discoverable.
8. An emergency release MAY use a pre-authorized fast path, but it MUST preserve exact identities, least privilege, minimum applicable security checks, and contemporaneous action logs. Bypassed review or checks MUST remain recorded as bypassed and receive prompt retrospective review.

9. Finishing a development branch or equivalent workspace MUST follow the
   project adapter's authorized disposition: integrate, open or update a review
   request, retain for later work, or abandon. A successful check does not by
   itself authorize publication, merge, release, deployment, or deletion.
10. Branch or workspace cleanup MUST wait until the selected disposition is
    complete, review and recovery records are retained, and no active executor
    or reviewer depends on it. Deletion of a shared or unknown workspace
    requires its owner's authority.

### GCS-9 — Vulnerability intake, remediation, and learning

1. Released software MUST have a discoverable reporting channel, triage owner, supported-version policy, severity or risk method, escalation path, and coordinated communication process appropriate to its consumers.
2. Every credible report MUST be acknowledged, protected from unnecessary disclosure, investigated, and tracked to a documented disposition. Lack of immediate reproduction MUST NOT be equated with invalidity.
3. Triage MUST consider exploitability, exposure, affected versions and artifacts, impact, active exploitation, available containment, and downstream consumers. Component inventory and provenance SHOULD be used to identify affected releases. When either is unavailable or incomplete, the triage record MUST describe the gap and the alternative identification method.
4. Remediation targets MUST be risk-based, with explicit urgent escalation for active exploitation or critical impact. Temporary containment MUST have an owner and remain linked to permanent remediation or an explicit risk acceptance with review/expiry.
5. A fixed release MUST have regression evidence, updated affected-version information, artifact identity, and consumer communication appropriate to the risk. Embargoed details and personal data MUST be access-controlled without suppressing the existence and status of the response.
6. Material vulnerabilities MUST receive causal analysis, a search for the same weakness class, and a review of the development or delivery control that allowed it. Where feasible, the project MUST add a prevention or detection control and verify it on the fixed revision.
7. Response records MUST distinguish remediation, mitigation, accepted risk, duplicate, and not affected. A security failure MUST NOT be closed merely because a scanner was muted or a warning was hidden.

These rules implement the outcome of NIST SSDF RV.1–RV.3: ongoing identification, risk-based response, root-cause analysis, class-wide search, and process improvement.

### GCS-10 — Honest use of external control frameworks

1. A project MUST NOT claim NIST SSDF, SLSA, OWASP ASVS, or other formal conformance merely because it cites this chapter, uses a named tool, emits an SBOM or attestation, or passes selected checks.
2. A conformance or level claim MUST identify the exact framework and version, applicable scope, selected or tailored requirements, responsible assessor, and retained evidence. Every requirement of a claimed SLSA track and level MUST be satisfied for the claimed subject; source and build tracks MUST NOT be conflated.
3. If a project represents NIST SSDF alignment, its mapping MUST identify the actual practice/task and implemented outcome. A project MAY omit a non-applicable practice only through its documented risk-based tailoring process; it MUST NOT describe a partial informal mapping as NIST certification.
4. A web-application adapter that uses or claims OWASP ASVS alignment MUST select version-qualified, testable requirements and retain their evidence. Non-web projects MAY use applicable ideas, but MUST NOT imply that ASVS is a universal release or supply-chain standard.
5. A project choosing SLSA for standardized source or build assurance MUST identify its target track, level, subject, and verification policy. A lower or unclaimed level can still provide useful controls; projects MUST describe the controls they actually meet rather than overstate a level.

## Lightweight workflow

Use the smallest workflow that preserves the applicable outcomes:

1. **Classify.** Identify the risk tier and whether the change affects protected source, privileges, secrets, dependencies, build inputs, release artifacts, deployment, or supported software.
2. **Assemble.** Select a coherent change set; inspect its full diff, dependency resolution, generated content, and workflow/configuration effects. Record any justified mixed or large revision.
3. **Review the final candidate.** Obtain the required independent and domain/security review. Re-review after material changes and preserve the exact candidate identity.
4. **Gate exactly.** Run the baseline and triggered checks on the integration candidate. Treat missing or indeterminate results as blocking; expose failures and exceptions separately.
5. **Build and identify.** Build in the declared trust boundary, record inputs and provenance, generate the component inventory, and identify outputs by digest. Verify integrity before release.
6. **Authorize and deliver.** Authorize the named artifact, promote that artifact, record the deployed digest, observe post-deployment behavior, and exercise the chosen rollback or containment path when needed.
7. **Monitor and respond.** Monitor supported releases and dependencies, investigate credible reports, contain and remediate by risk, communicate, and feed root causes back into gates and design.

R1 work may compress these steps into a diff inspection and one focused gate. R3 and R4 work requires distinct, retained evidence at the review, build, authorization, and recovery boundaries.

## Evidence and release gates

Evidence MUST meet the shared evidence model and MUST be retained in proportion to the risk and support lifetime. The following table defines minimum chapter-specific evidence; an adapter may strengthen it.

| Decision | Required evidence |
|---|---|
| Accept a protected revision | immutable source identity; human-readable final diff; required approvals; required check identities and results bound to the candidate; disclosed bypasses or exceptions |
| Accept a dependency change | manifest and resolved/lock diff; purpose and source; direct/transitive impact; license/policy disposition; vulnerability result and any approved exception |
| Accept a CI or privilege change | before/after trust boundary and permissions; untrusted-input analysis; secret exposure analysis; validation of failure behavior, including a deliberately failing or denied case |
| Publish a release | source and artifact digests; build definition and builder identity; relevant inputs; gate results; component inventory; provenance and integrity-verification result; authorization |
| Deploy a release | environment; artifact digest; deployer/authorizer; configuration/migration identity; time; post-deployment result; rollback or containment readiness |
| Close a vulnerability | affected versions/artifacts; risk and disposition; fix or acceptance authority; regression result on the fixed revision; communication; sibling search and process action for material cases |

A gate is **required** only when the protected policy marks it so for the candidate. A required result MUST be machine-enforced where the platform can do so. Manual evidence MAY cover judgment or an unavailable mechanism, but it MUST name the observer, exact subject, observation, time, and limits. A green aggregate badge without inspectable constituent results is insufficient for R3 or R4.

## Exceptions and emergencies

Use the [handbook exception model](README.md#exception-model). In this chapter:

- an exception MUST preserve the original failed, missing, or bypassed result and record the separate acceptance decision;
- an exception to a security or supply-chain gate MUST name the affected artifacts/releases, exploit or compromise scenario, compensating controls, monitoring, owner, approver, and expiry or removal condition;
- an exception MUST NOT grant access the approver lacks authority to grant, expose a secret to an untrusted context, falsify provenance, or claim an external assurance level whose requirements are unmet;
- recurring bypasses, repeated false positives, or long-lived dependency waivers SHOULD trigger repair of the gate or underlying system. Renewal is justified only when the owner re-evaluates current exposure and explains why repair remains less safe or infeasible; and
- an emergency path MUST be pre-authorized where foreseeable, narrowly privileged, logged, and retrospectively reviewed. Urgency can shorten sequencing but MUST NOT make failures disappear.

If infrastructure cannot execute a required gate, the decision is **blocked**, not passed. An authorized exception may permit a bounded action with substitute evidence, but the record must state the unverified claim and residual uncertainty.

## Anti-patterns

- Large “cleanup plus feature plus dependency update” revisions that obscure intent, or tiny commits split so finely that no revision is meaningful.
- Reviewing one revision and merging another without re-establishing approval and checks.
- Treating a branch name, tag, version string, container tag, or deployment channel as immutable identity.
- Allowing administrators, bots, or merge queues to bypass policy without an attributable exception record.
- Marking a security scanner non-blocking, swallowing its exit code, filtering its output, or rerunning until the badge turns green.
- Letting changed-files rules skip the very workflow, generated file, or policy that controls their selection.
- Running untrusted proposed code with write tokens, deployment authority, signing keys, protected secrets, or a persistent privileged runner.
- Committing secrets, then deleting only the latest copy; masking the log while leaving the credential valid.
- Adding a dependency because it is popular, auto-generated, or already cached without reviewing resolved identity and transitive risk.
- Pinning a privileged build component to a movable label while describing it as immutable.
- Producing an SBOM or attestation that is incomplete, self-asserted by untrusted build steps, unverified by consumers, or detached from the artifact digest.
- Rebuilding separately in each environment and calling the outputs the same release.
- Calling a build reproducible after one successful run, or treating reproducibility as synonymous with provenance.
- Defining rollback as “redeploy the old binary” without accounting for state, schema, compatibility, or credential changes.
- Closing a vulnerability because a rule was suppressed, the affected component was renamed, or the report was inconvenient to reproduce.
- Advertising “SLSA compliant,” “NIST certified,” or “OWASP compliant” without a versioned scope, complete applicable requirements, and supporting evidence.

## Project-adapter hooks

A project adapter MUST keep the universal outcomes above distinct from local mechanisms. The hooks below are adapter material; include only those applicable to the project and link them to executable configuration:

### Source and review adapter

- protected baselines and release references; who may propose, approve, integrate, administer, and expunge;
- merge strategy, final-candidate semantics, stale-approval behavior, generated/binary review method, and whether a merge queue is used;
- commit or review-unit conventions, path ownership, security-sensitive paths, signing policy if any, and auditable emergency bypass;
- local risk labels mapped to R1–R4 and the changes that trigger independent security, domain, or release review.

### CI trust and gate adapter

- exact required check names, commands, triggering rules, timeouts, retry policy, policy/configuration identity, and evidence retention;
- how results bind to the final integration revision and how aggregate gates expose constituent failures;
- trusted and untrusted runner classes, network boundaries, cache scopes, workspace cleanup, and restrictions on proposed changes;
- job-by-job permissions, identity federation or credential issuance, protected environments, secret namespaces, redaction, rotation, and incident contacts;
- the structured exception source and the mechanism that ensures failures remain visible while an exception is evaluated.

### Dependency and supply-chain adapter

- authoritative manifests, lock/resolution files, registries and mirrors, immutable pinning rules, allowed sources and licenses, and component-inventory/SBOM format;
- vulnerability sources, blocking thresholds, reachability/exploitability triage, remediation targets, alert ownership, supported versions, and waiver expiry;
- review requirements for build tools, workflow components, base images, generated code, vendored material, and automated update identities.

### Build and artifact adapter

- canonical build definition and commands; builder trust boundary; permitted network inputs; toolchain and environment pinning; cache-integrity controls;
- artifact naming and digest algorithms, provenance format and issuer, signing/trust policy, verification command, key lifecycle, transparency or timestamping where used;
- reproducibility scope, normalization rules, known nondeterministic inputs, independent rebuild method, and comparison criteria;
- artifact registry permissions, immutability, retention, quarantine/revocation, release archive, and consumer access to integrity/provenance material.

### Release, deployment, and response adapter

- release authorities, promotion stages, environment protections, deployment identity record, health signals, rollout limits, and post-deployment checks;
- rollback, roll-forward, disablement, isolation, restore, schema/data compatibility, rehearsal cadence, and emergency-release procedure;
- vulnerability reporting channel, private intake boundary, triage roles, severity/risk method, active-exploitation escalation, communication/advisory process, and root-cause follow-up;
- any exact NIST SSDF practice/task, SLSA track/level, or OWASP ASVS version/control mapping the project actually claims, plus assessment ownership and evidence location.

A provider-specific feature MAY implement one or more hooks, but its product name or green status is not the control outcome. The adapter MUST explain what the feature enforces, where its evidence is found, and what happens when it is unavailable or indeterminate. It MUST NOT weaken fail-closed security behavior by relabeling a required failure as advisory.

## Source notes

- [NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://doi.org/10.6028/NIST.SP.800-218): risk-scaled, outcome-oriented secure development; protected software, release integrity and archives, third-party components, security verification, and vulnerability response.
- [SLSA 1.2 source requirements](https://slsa.dev/spec/v1.2/source-requirements): immutable revisions, reliable history, protected references, control continuity, human-readable changes, exact final-revision review, and source provenance.
- [SLSA 1.2 build requirements](https://slsa.dev/spec/v1.2/build-requirements): consistent builds, output digests, provenance existence/authenticity/unforgeability, hosted builds, and isolation.
- [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0): versioned application-security verification requirements suitable for an applicable web-application adapter, not a universal compliance label.
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html): useful security logging while excluding credentials, tokens, keys, and unnecessary sensitive data.
- [Git `add` documentation](https://git-scm.com/docs/git-add): one example of deliberate change-set selection and staged-diff inspection; exact commands remain adapter material.

These links provide traceability for the chapter’s synthesis. They do not import every source requirement into every project and do not, by themselves, prove conformance.
