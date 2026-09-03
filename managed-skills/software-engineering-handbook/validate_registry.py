"""Validate the handbook expert registry and routing invariants."""

from __future__ import annotations

import copy
import json
from collections.abc import Callable
from pathlib import Path
from typing import cast

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "experts" / "registry.json"
SKILL = ROOT / "SKILL.md"

REQUIRED_FIELDS = {
    "adapters",
    "authority",
    "conflicts",
    "context_budget",
    "effects",
    "evidence",
    "fallback_module",
    "fallback_section",
    "higher_authority_contracts",
    "id",
    "inputs",
    "kind",
    "license",
    "lifecycle_state",
    "near_miss_exclusions",
    "optional_companions",
    "ordering_constraints",
    "original_skills",
    "outputs",
    "owner",
    "permitted_effects",
    "provider",
    "phase",
    "replacement_deprecation",
    "required_capabilities",
    "required_data",
    "required_tools",
    "requires",
    "rollback_disable",
    "scope",
    "scripts",
    "shared_references",
    "source_identity",
    "stop_conditions",
    "triggers",
    "unavailable_behavior",
    "version",
}

AGENT_SKILLS = {
    "interview-me",
    "idea-refine",
    "spec-driven-development",
    "constraint-driven-development",
    "planning-and-task-breakdown",
    "incremental-implementation",
    "test-driven-development",
    "context-engineering",
    "source-driven-development",
    "doubt-driven-development",
    "frontend-ui-engineering",
    "api-and-interface-design",
    "browser-testing-with-devtools",
    "debugging-and-error-recovery",
    "code-review-and-quality",
    "code-simplification",
    "security-and-hardening",
    "performance-optimization",
    "git-workflow-and-versioning",
    "ci-cd-and-automation",
    "deprecation-and-migration",
    "documentation-and-adrs",
    "observability-and-instrumentation",
    "shipping-and-launch",
}

EXPECTED_SOURCES = {
    "superpowers": "86babb696875227929e85420f287d6309374b93f",
    "ponytail": "0a4dd63ad4541f4f655c4108a295916f3c1d8fda",
    "agent-skills": "a0dd41844acdfcd0fbc8f66d27f0ee6d3029ce22",
    "understand-anything": "840ad7d66d881cb50f4f33011785308c7a018503",
    "autoresearch": "228791fb499afffb54b46200aca536f79142f117",
    "spec-kit": "bca679051abb80d6cf0cd909f2539a28a10eb7eb",
    "openspec": "a0ddb60d040c61f4907436a9d91310934b1dda63",
    "bmad-method": "9ce3c397c9b238de96f7365da8019f6f66b059da",
}

EXPECTED_VERSIONS = {
    "superpowers": "6.3.0",
    "ponytail": "4.9.0",
    "agent-skills": "0.6.8",
    "understand-anything": "2.9.4",
    "autoresearch": "pinned-2026-09-03",
    "spec-kit": "1.0.0",
    "openspec": "1.11.0",
    "bmad-method": "6.11.0",
}

PROVIDER_FIELDS = {"name", "version", "source_commit", "status"}

EXPECTED_SKILL_NAMES = {
    "superpowers": {
        "brainstorming",
        "using-git-worktrees",
        "writing-plans",
        "executing-plans",
        "subagent-driven-development",
        "dispatching-parallel-agents",
        "test-driven-development",
        "systematic-debugging",
        "verification-before-completion",
        "requesting-code-review",
        "receiving-code-review",
        "finishing-a-development-branch",
        "writing-skills",
    },
    "ponytail": {"ponytail", "ponytail-review", "ponytail-audit", "ponytail-debt"},
    "agent-skills": AGENT_SKILLS,
    "understand-anything": {
        "understand",
        "understand-diff",
        "understand-explain",
        "understand-onboard",
    },
    "autoresearch": {"autoresearch"},
    "spec-kit": {
        "speckit-constitution",
        "speckit-specify",
        "speckit-plan",
        "speckit-tasks",
        "speckit-taskstoissues",
        "speckit-implement",
        "speckit-converge",
        "speckit-clarify",
        "speckit-analyze",
        "speckit-checklist",
        "speckit-bug-assess",
        "speckit-bug-fix",
        "speckit-bug-test",
        "speckit-assess-intake",
        "speckit-assess-research",
        "speckit-assess-define",
        "speckit-assess-shape",
        "speckit-assess-decide",
    },
    "openspec": {
        "openspec-explore",
        "openspec-propose",
        "openspec-new",
        "openspec-continue",
        "openspec-ff",
        "openspec-apply",
        "openspec-verify",
        "openspec-archive",
        "openspec-bulk-archive",
        "openspec-onboard",
    },
    "bmad-method": {
        "bmad-project-context",
        "bmad-build",
        "bmad-spec",
        "bmad-correct-course",
        "bmad-brainstorming",
        "bmad-product-brief",
        "bmad-prfaq",
        "bmad-prd",
        "bmad-ux",
        "bmad-architecture",
        "bmad-create-epics-and-stories",
        "bmad-sprint-planning",
        "bmad-code-review",
        "bmad-checkpoint-preview",
        "bmad-qa-generate-e2e-tests",
        "bmad-retrospective",
    },
}

EXPECTED_ORIGINALS = {
    provider: {f"{provider}/{name}" for name in names}
    for provider, names in EXPECTED_SKILL_NAMES.items()
}

ALLOWED_EFFECTS = {
    "read",
    "authorized planning artifacts",
    "authorized source edits",
    "authorized source edits in isolation",
    "authorized verification commands",
    "owned reversible scratch",
}

EXPECTED_BUDGETS = {
    "R0": {"primary": 0, "specialists": 0, "evaluator": 0},
    "R1": {"primary": 0, "specialists": 1, "evaluator": 0},
    "R2": {"primary": 1, "specialists": 1, "evaluator": 0},
    "R3": {"primary": 1, "specialists": 2, "evaluator": 1},
    "R4": {"primary": 1, "specialists": 2, "evaluator": 1},
}

EXPECTED_POLICY_VALUES: dict[str, object] = {
    "core": "handbook",
    "max_primary_workflow_experts": 1,
    "prefer_trusted_original": True,
    "discover_originals_from_host_registry_only": True,
    "load_internal_fallback_when_original_absent": True,
    "allow_duplicate_original_and_fallback": False,
    "load_unselected_bodies": False,
    "selection_mode": "sparse_descriptor_first",
    "catalog_growth_expands_active_set": False,
    "provider_qualified_original_identity": True,
    "original_descriptor_trigger_must_match": True,
    "startup_payload": "frontmatter_descriptor_only",
    "startup_payload_max_bytes": 1024,
    "router_index_max_bytes": 10240,
    "registry_scan_mode": "selected_descriptors_only",
    "chapter_load_mode": "relevant_sections_first",
    "retain_inactive_detail": False,
}

EXPECTED_FORBIDDEN_ROUTERS = {
    "superpowers/using-superpowers",
    "agent-skills/using-agent-skills",
}

DESCRIPTOR_STRING_FIELDS = {
    "authority",
    "context_budget",
    "effects",
    "evidence",
    "fallback_module",
    "fallback_section",
    "id",
    "kind",
    "license",
    "lifecycle_state",
    "owner",
    "phase",
    "provider",
    "replacement_deprecation",
    "rollback_disable",
    "scope",
    "source_identity",
    "unavailable_behavior",
}

DESCRIPTOR_LIST_FIELDS = {
    "adapters",
    "conflicts",
    "higher_authority_contracts",
    "inputs",
    "near_miss_exclusions",
    "optional_companions",
    "ordering_constraints",
    "original_skills",
    "outputs",
    "permitted_effects",
    "required_capabilities",
    "required_data",
    "required_tools",
    "requires",
    "scripts",
    "shared_references",
    "stop_conditions",
    "triggers",
}

NONEMPTY_DESCRIPTOR_LIST_FIELDS = {
    "adapters",
    "higher_authority_contracts",
    "inputs",
    "near_miss_exclusions",
    "ordering_constraints",
    "original_skills",
    "outputs",
    "permitted_effects",
    "shared_references",
    "stop_conditions",
    "triggers",
}


class ValidationError(ValueError):
    """A registry or pressure-test invariant failed."""


def check(condition: object, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def expect_failure(action: Callable[[], object], message: str) -> None:
    try:
        action()
    except ValidationError:
        return
    raise ValidationError(message)


def matching_originals(
    capability: dict[str, object],
    facts: set[str],
    registered: dict[str, set[str]],
) -> set[str]:
    allowed = strings(capability["original_skills"])
    return {
        identity
        for identity, triggers in registered.items()
        if identity in allowed and facts & triggers
    }


def validate_dependency_graph(capabilities: list[dict[str, object]]) -> None:
    by_id = {str(capability["id"]): capability for capability in capabilities}
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(capability_id: str) -> None:
        check(capability_id in by_id, f"missing dependency: {capability_id}")
        check(capability_id not in visiting, f"dependency cycle: {capability_id}")
        if capability_id in visited:
            return
        visiting.add(capability_id)
        for dependency in strings(by_id[capability_id]["requires"]):
            visit(dependency)
        visiting.remove(capability_id)
        visited.add(capability_id)

    for capability_id in by_id:
        visit(capability_id)


def resolve(
    capabilities: list[dict[str, object]],
    *,
    facts: set[str],
    available_requirements: set[str],
    registered_originals: dict[str, set[str]],
    trusted_originals: set[str],
    budget: dict[str, int],
) -> dict[str, str]:
    by_id = {str(capability["id"]): capability for capability in capabilities}
    selected = {
        capability_id: capability
        for capability_id, capability in by_id.items()
        if facts & strings(capability["triggers"])
        and not facts & strings(capability["near_miss_exclusions"])
    }

    pending = list(selected.values())
    while pending:
        capability = pending.pop()
        missing = strings(capability["required_capabilities"]) - available_requirements
        check(not missing, f"unavailable requirements: {sorted(missing)}")
        for dependency in strings(capability["requires"]):
            check(dependency in by_id, f"missing dependency: {dependency}")
            if dependency not in selected:
                selected[dependency] = by_id[dependency]
                pending.append(by_id[dependency])

    selected_values = list(selected.values())
    for index, left in enumerate(selected_values):
        for right in selected_values[index + 1 :]:
            check(
                not has_conflict(left, right),
                f"unresolved conflict: {left['id']} and {right['id']}",
            )

    routes: dict[str, str] = {}
    for capability in selected_values:
        capability_id = str(capability["id"])
        route = choose(
            capability,
            matching_originals(capability, facts, registered_originals),
            trusted_originals,
        )
        if (
            capability["kind"] == "workflow"
            and capability["fallback_module"] == "handbook"
            and budget["primary"] == 0
        ):
            route = "fallback:handbook"
        routes[capability_id] = route

    active_values = [
        capability
        for capability in selected_values
        if routes[str(capability["id"])] != "fallback:handbook"
    ]
    primary = sum(capability["kind"] == "workflow" for capability in active_values)
    specialists = sum(
        capability["kind"] == "specialist" for capability in active_values
    )
    evaluators = sum(capability["kind"] == "evaluator" for capability in active_values)
    check(
        fits_budget(
            budget,
            primary=primary,
            specialists=specialists,
            evaluator=evaluators,
        ),
        "active expert budget exceeded",
    )
    return routes


def transition(previous: str, desired: str, *, effects_started: bool) -> str:
    check(
        not effects_started or previous == desired,
        "implementation failover after side effects requires reconciliation",
    )
    return desired


def strings(value: object) -> set[str]:
    check(isinstance(value, list), "registry invariant failed")
    raw = cast(list[object], value)
    result = {item for item in raw if isinstance(item, str) and bool(item.strip())}
    check(len(result) == len(raw), "registry invariant failed")
    return result


def validate_descriptor_shape(capability: dict[str, object]) -> None:
    capability_id = str(capability.get("id"))
    check(set(capability) == REQUIRED_FIELDS, f"descriptor schema: {capability_id}")
    version = capability.get("version")
    check(
        isinstance(version, int) and not isinstance(version, bool) and version > 0,
        f"invalid capability version: {capability_id}",
    )
    for field in DESCRIPTOR_STRING_FIELDS:
        value = capability.get(field)
        check(
            isinstance(value, str) and bool(value.strip()),
            f"invalid {field}: {capability_id}",
        )
    for field in DESCRIPTOR_LIST_FIELDS:
        values = strings(capability.get(field))
        if field in NONEMPTY_DESCRIPTOR_LIST_FIELDS:
            check(values, f"empty {field}: {capability_id}")
    check(
        capability.get("kind") in {"workflow", "specialist", "evaluator"},
        f"invalid kind: {capability_id}",
    )
    check(
        capability.get("lifecycle_state") == "active",
        f"invalid lifecycle state: {capability_id}",
    )


def choose(capability: dict[str, object], matched: set[str], trusted: set[str]) -> str:
    matches = strings(capability["original_skills"]) & matched & trusted
    if matches:
        return f"original:{min(matches)}"
    module = capability["fallback_module"]
    check(isinstance(module, str), "registry invariant failed")
    return f"fallback:{module}"


def fits_budget(
    limit: dict[str, int], *, primary: int, specialists: int, evaluator: int
) -> bool:
    return (
        primary <= limit["primary"]
        and specialists <= limit["specialists"]
        and evaluator <= limit["evaluator"]
    )


def has_conflict(left: dict[str, object], right: dict[str, object]) -> bool:
    left_id = left["id"]
    right_id = right["id"]
    check(
        isinstance(left_id, str) and isinstance(right_id, str),
        "registry invariant failed",
    )
    return right_id in strings(left["conflicts"]) or left_id in strings(
        right["conflicts"]
    )


def validate_policy(
    data: dict[str, object],
) -> tuple[dict[str, object], dict[str, dict[str, int]]]:
    check(
        set(data)
        == {"schema_version", "router", "policy", "providers", "capabilities"},
        "registry top-level schema",
    )
    schema_version = data.get("schema_version")
    check(
        type(schema_version) is int and schema_version == 1,
        "registry schema version",
    )
    check(data.get("router") == "software-engineering-handbook", "router identity")

    raw_policy = data.get("policy")
    check(isinstance(raw_policy, dict), "policy must be an object")
    policy = cast(dict[str, object], raw_policy)
    expected_keys = set(EXPECTED_POLICY_VALUES) | {
        "default_budgets",
        "forbidden_original_routers",
    }
    check(set(policy) == expected_keys, "policy schema")
    for key, expected in EXPECTED_POLICY_VALUES.items():
        actual = policy.get(key)
        check(
            type(actual) is type(expected) and actual == expected,
            f"policy invariant: {key}",
        )

    raw_budgets = policy.get("default_budgets")
    check(isinstance(raw_budgets, dict), "default budgets must be an object")
    raw_budget_map = cast(dict[str, object], raw_budgets)
    check(set(raw_budget_map) == set(EXPECTED_BUDGETS), "default risk tiers")
    for tier, expected_limit in EXPECTED_BUDGETS.items():
        raw_limit = raw_budget_map[tier]
        check(isinstance(raw_limit, dict), f"invalid {tier} budget")
        limit = cast(dict[str, object], raw_limit)
        check(set(limit) == set(expected_limit), f"invalid {tier} budget fields")
        for field, expected in expected_limit.items():
            actual = limit.get(field)
            check(
                type(actual) is int and actual == expected,
                f"invalid {tier} {field} budget",
            )
    budgets = cast(dict[str, dict[str, int]], raw_budgets)
    check(
        strings(policy.get("forbidden_original_routers")) == EXPECTED_FORBIDDEN_ROUTERS,
        "forbidden original routers",
    )
    return policy, budgets


def validate_providers(
    data: dict[str, object],
) -> tuple[list[dict[str, object]], list[str]]:
    raw_providers = data.get("providers")
    check(isinstance(raw_providers, list), "providers must be a list")
    raw_provider_list = cast(list[object], raw_providers)
    check(
        all(isinstance(provider, dict) for provider in raw_provider_list),
        "provider entries must be objects",
    )
    providers = cast(list[dict[str, object]], raw_provider_list)
    provider_names: list[str] = []
    for provider in providers:
        check(set(provider) == PROVIDER_FIELDS, "provider schema")
        name = provider.get("name")
        version = provider.get("version")
        source_commit = provider.get("source_commit")
        status = provider.get("status")
        check(
            isinstance(name, str) and bool(name.strip()),
            "invalid provider name",
        )
        provider_name = cast(str, name)
        check(
            isinstance(version, str) and bool(version.strip()),
            f"invalid provider version: {name}",
        )
        check(
            isinstance(source_commit, str)
            and len(source_commit) == 40
            and all(character in "0123456789abcdef" for character in source_commit),
            f"invalid provider source commit: {name}",
        )
        check(
            isinstance(status, str) and status.startswith("active_"),
            f"provider status: {name}",
        )
        provider_names.append(provider_name)
    check(len(provider_names) == len(set(provider_names)), "duplicate providers")
    check(set(provider_names) == set(EXPECTED_SOURCES), "provider inventory")
    check(
        {
            cast(str, provider["name"]): cast(str, provider["source_commit"])
            for provider in providers
        }
        == EXPECTED_SOURCES,
        "provider source pins",
    )
    check(
        {
            cast(str, provider["name"]): cast(str, provider["version"])
            for provider in providers
        }
        == EXPECTED_VERSIONS,
        "provider versions",
    )
    return providers, provider_names


def main() -> None:
    raw_data = json.loads(REGISTRY.read_text())
    check(isinstance(raw_data, dict), "registry root must be an object")
    data = cast(dict[str, object], raw_data)
    policy, budgets = validate_policy(data)
    skill_bytes = SKILL.read_bytes()
    check(skill_bytes.startswith(b"---\n"), "skill frontmatter")
    frontmatter_end = skill_bytes.find(b"\n---\n", 4)
    check(frontmatter_end >= 0, "skill frontmatter")
    check(
        frontmatter_end + len(b"\n---\n")
        <= cast(int, policy["startup_payload_max_bytes"]),
        "startup descriptor byte budget",
    )
    check(
        len(skill_bytes) <= cast(int, policy["router_index_max_bytes"]),
        "router index byte budget",
    )

    providers, provider_names = validate_providers(data)

    raw_capabilities = data.get("capabilities")
    check(isinstance(raw_capabilities, list), "capabilities must be a list")
    capabilities = cast(list[dict[str, object]], raw_capabilities)
    ids = [str(capability.get("id")) for capability in capabilities]
    check(len(ids) == len(set(ids)), "duplicate capability identities")
    id_set = set(ids)
    forbidden = strings(policy.get("forbidden_original_routers"))
    covered: dict[str, set[str]] = {provider: set() for provider in provider_names}

    for capability in capabilities:
        validate_descriptor_shape(capability)
        capability_id = cast(str, capability["id"])
        provider = cast(str, capability["provider"])
        check(provider in provider_names, f"unknown provider: {capability_id}")
        source_identity = cast(str, capability["source_identity"])
        check(
            EXPECTED_SOURCES[provider] in source_identity,
            f"unbound source identity: {capability_id}",
        )

        originals = strings(capability.get("original_skills"))
        check(originals, f"no original capability identities: {capability_id}")
        check(forbidden.isdisjoint(originals), f"forbidden router: {capability_id}")
        check(
            covered[provider].isdisjoint(originals),
            f"duplicate provider capability: {capability_id}",
        )
        for identity in originals:
            prefix, separator, name = identity.partition("/")
            check(
                separator == "/" and prefix == provider and bool(name),
                f"unqualified original identity: {identity}",
            )
        covered[provider].update(originals)

        permitted = strings(capability.get("permitted_effects"))
        check(
            permitted <= ALLOWED_EFFECTS,
            f"prohibited effect in {capability_id}: {sorted(permitted - ALLOWED_EFFECTS)}",
        )

        module_value = capability.get("fallback_module")
        check(
            isinstance(module_value, str),
            f"invalid fallback module: {capability_id}",
        )
        module = cast(str, module_value)
        if module != "handbook":
            path = ROOT / module
            check(path.is_file(), str(path))
            text = path.read_text()
            check(text.endswith("\n"), str(path))
            section_value = capability.get("fallback_section")
            check(
                isinstance(section_value, str),
                f"invalid fallback section: {capability_id}",
            )
            section = cast(str, section_value)
            check(f"# {section}" in text, str((path, section)))

        for companion in strings(capability.get("optional_companions")):
            check(companion in id_set, str((capability_id, companion)))
        for conflict in strings(capability.get("conflicts")):
            check(
                conflict in id_set or conflict in forbidden,
                str((capability_id, conflict)),
            )

    check(covered == EXPECTED_ORIGINALS, "provider capability coverage")
    validate_dependency_graph(capabilities)
    invalid_schema = copy.deepcopy(data)
    invalid_schema["schema_version"] = 999
    expect_failure(
        lambda: validate_policy(invalid_schema),
        "unsupported schema version was accepted",
    )
    invalid_schema_type = copy.deepcopy(data)
    invalid_schema_type["schema_version"] = True
    expect_failure(
        lambda: validate_policy(invalid_schema_type),
        "boolean schema version was accepted",
    )
    invalid_primary_type = copy.deepcopy(data)
    cast(dict[str, object], invalid_primary_type["policy"])[
        "max_primary_workflow_experts"
    ] = True
    expect_failure(
        lambda: validate_policy(invalid_primary_type),
        "boolean primary workflow limit was accepted",
    )
    invalid_r1_type = copy.deepcopy(data)
    invalid_r1_policy = cast(dict[str, object], invalid_r1_type["policy"])
    invalid_r1_budgets = cast(
        dict[str, dict[str, object]],
        invalid_r1_policy["default_budgets"],
    )
    invalid_r1_budgets["R1"]["specialists"] = True
    expect_failure(
        lambda: validate_policy(invalid_r1_type),
        "boolean R1 specialist budget was accepted",
    )
    invalid_core = copy.deepcopy(data)
    cast(dict[str, object], invalid_core["policy"])["core"] = "other"
    expect_failure(
        lambda: validate_policy(invalid_core),
        "alternate policy core was accepted",
    )
    invalid_fallback = copy.deepcopy(data)
    cast(dict[str, object], invalid_fallback["policy"])[
        "load_internal_fallback_when_original_absent"
    ] = False
    expect_failure(
        lambda: validate_policy(invalid_fallback),
        "disabled absent-original fallback was accepted",
    )
    invalid_startup_payload = copy.deepcopy(data)
    cast(dict[str, object], invalid_startup_payload["policy"])["startup_payload"] = (
        "whole_skill"
    )
    expect_failure(
        lambda: validate_policy(invalid_startup_payload),
        "whole-skill startup payload was accepted",
    )
    invalid_r3 = copy.deepcopy(data)
    invalid_r3_policy = cast(dict[str, object], invalid_r3["policy"])
    invalid_r3_budgets = cast(
        dict[str, dict[str, int]],
        invalid_r3_policy["default_budgets"],
    )
    invalid_r3_budgets["R3"] = {"primary": 99, "specialists": 99, "evaluator": 99}
    expect_failure(
        lambda: validate_policy(invalid_r3),
        "expanded R3 budget was accepted",
    )
    invalid_provider_versions: tuple[object, ...] = ([], "")
    for provider_version in invalid_provider_versions:
        invalid_provider = copy.deepcopy(data)
        cast(list[dict[str, object]], invalid_provider["providers"])[0]["version"] = (
            provider_version
        )
        expect_failure(
            lambda candidate=invalid_provider: validate_providers(candidate),
            "invalid provider version was accepted",
        )
    invalid_provider_schema = copy.deepcopy(data)
    cast(list[dict[str, object]], invalid_provider_schema["providers"])[0]["extra"] = (
        True
    )
    expect_failure(
        lambda: validate_providers(invalid_provider_schema),
        "undeclared provider field was accepted",
    )
    for field, value in (
        ("effects", ""),
        ("phase", ""),
        ("kind", "bogus"),
        ("inputs", ["   "]),
    ):
        invalid_descriptor = copy.deepcopy(capabilities[0])
        invalid_descriptor[field] = value
        expect_failure(
            lambda descriptor=invalid_descriptor: validate_descriptor_shape(descriptor),
            f"invalid descriptor {field} was accepted",
        )

    check(
        fits_budget(budgets["R0"], primary=0, specialists=0, evaluator=0)
        and not fits_budget(budgets["R0"], primary=0, specialists=1, evaluator=0),
        "R0 core-only budget",
    )
    superpowers = next(
        capability
        for capability in capabilities
        if capability["id"] == "superpowers.inner-loop"
    )
    for trigger in strings(superpowers["triggers"]):
        result = resolve(
            capabilities,
            facts={trigger},
            available_requirements=set(),
            registered_originals={},
            trusted_originals=set(),
            budget=budgets["R1"],
        )
        check(
            result["superpowers.inner-loop"] == "fallback:handbook",
            f"R1 handbook fallback: {trigger}",
        )
    superpowers_original = min(strings(superpowers["original_skills"]))
    result = resolve(
        capabilities,
        facts={"implementation"},
        available_requirements=set(),
        registered_originals={superpowers_original: {"implementation"}},
        trusted_originals={superpowers_original},
        budget=budgets["R1"],
    )
    check(
        result["superpowers.inner-loop"] == "fallback:handbook",
        "R1 budget-incompatible original must use the core fallback",
    )

    ponytail_identity = "ponytail/ponytail"
    registered_ponytail = {ponytail_identity: {"coding"}}
    result = resolve(
        capabilities,
        facts={"coding"},
        available_requirements=set(),
        registered_originals=registered_ponytail,
        trusted_originals={ponytail_identity},
        budget=budgets["R1"],
    )
    check(
        result == {"ponytail.simplicity": f"original:{ponytail_identity}"},
        "positive original route",
    )
    result = resolve(
        capabilities,
        facts={"coding"},
        available_requirements=set(),
        registered_originals=registered_ponytail,
        trusted_originals=set(),
        budget=budgets["R1"],
    )
    check(
        result == {"ponytail.simplicity": "fallback:experts/ponytail-simplicity.md"},
        "untrusted original fallback",
    )
    result = resolve(
        capabilities,
        facts={"coding"},
        available_requirements=set(),
        registered_originals={ponytail_identity: {"refactoring"}},
        trusted_originals={ponytail_identity},
        budget=budgets["R1"],
    )
    check(
        result == {"ponytail.simplicity": "fallback:experts/ponytail-simplicity.md"},
        "original trigger mismatch fallback",
    )
    result = resolve(
        capabilities,
        facts={"coding"},
        available_requirements=set(),
        registered_originals={"other/ponytail": {"coding"}},
        trusted_originals={"other/ponytail"},
        budget=budgets["R1"],
    )
    check(
        result == {"ponytail.simplicity": "fallback:experts/ponytail-simplicity.md"},
        "provider identity substitution",
    )
    result = resolve(
        capabilities,
        facts={"coding", "non-coding work"},
        available_requirements=set(),
        registered_originals=registered_ponytail,
        trusted_originals={ponytail_identity},
        budget=budgets["R1"],
    )
    check(result == {}, "near-miss exclusion")

    expect_failure(
        lambda: resolve(
            capabilities,
            facts={"durable specification artifact chain", "revisioned change packet"},
            available_requirements=set(),
            registered_originals={},
            trusted_originals=set(),
            budget=budgets["R4"],
        ),
        "conflicting spec workflows were accepted",
    )
    expect_failure(
        lambda: resolve(
            capabilities,
            facts={"explicit request for bounded automated experimentation"},
            available_requirements=set(),
            registered_originals={},
            trusted_originals=set(),
            budget=budgets["R1"],
        ),
        "unavailable empirical requirements were accepted",
    )
    result = resolve(
        capabilities,
        facts={"explicit request for bounded automated experimentation"},
        available_requirements={
            "isolated workspace",
            "frozen evaluator",
            "finite resource budget",
        },
        registered_originals={},
        trusted_originals=set(),
        budget=budgets["R1"],
    )
    check(
        result
        == {
            "autoresearch.empirical-optimization": "fallback:experts/empirical-optimization.md"
        },
        "available empirical fallback",
    )
    expect_failure(
        lambda: resolve(
            capabilities,
            facts={"coding", "unfamiliar code"},
            available_requirements=set(),
            registered_originals={},
            trusted_originals=set(),
            budget=budgets["R1"],
        ),
        "active expert pressure was not enforced",
    )

    cyclic: list[dict[str, object]] = [
        {"id": "fixture/a", "requires": ["fixture/b"]},
        {"id": "fixture/b", "requires": ["fixture/a"]},
    ]
    expect_failure(
        lambda: validate_dependency_graph(cyclic),
        "dependency cycle was accepted",
    )
    check(
        transition("fallback:x", "fallback:x", effects_started=True) == "fallback:x",
        "stable post-effect route",
    )
    expect_failure(
        lambda: transition(
            "original:provider/skill",
            "fallback:module",
            effects_started=True,
        ),
        "post-effect failover was accepted",
    )

    repo_root = ROOT.parents[1]
    documents = [
        repo_root / "README.md",
        repo_root / "LICENSE",
        ROOT / "SKILL.md",
        repo_root / "rules" / "engineering-handbook-enforcement.md",
        *(repo_root / "handbook" / "software-engineering").glob("*.md"),
        *(ROOT / "experts").glob("*.md"),
    ]
    for path in documents:
        check(path.read_bytes().endswith(b"\n"), str(path))

    originals = sum(len(skills) for skills in covered.values())
    print(
        f"PASS: {len(providers)} providers, {len(capabilities)} capability groups, "
        f"{originals} original capabilities, descriptor schema, sparse routing, "
        "pressure, effects, and failover"
    )


if __name__ == "__main__":
    main()
