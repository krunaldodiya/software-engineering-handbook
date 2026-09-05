"""Print relevant catalog descriptors; never select or activate an expert."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

CATALOGS = (
    Path(__file__).resolve().parents[2] / "skills/software-engineering-handbook/experts"
)


def query_catalog(
    query: str, registry: dict[str, Any], purposes: dict[str, Any]
) -> dict[str, Any]:
    native = next((p for p in purposes["native_purposes"] if p["id"] == query), None)
    group = next(
        (
            p
            for p in purposes["equivalence_groups"]
            if p["id"] == query or query in p["ordered_alternatives"]
        ),
        None,
    )
    if native is not None:
        kind, purpose, originals = "native", native, []
    elif group is not None:
        kind, purpose, originals = "equivalence", group, group["ordered_alternatives"]
    elif query in purposes["distinct_originals"]:
        kind, purpose, originals = "distinct", {"id": query}, [query]
    else:
        raise ValueError("unknown exact purpose or provider-qualified original")

    capabilities = registry["capabilities"]
    by_id = {c["id"]: c for c in capabilities}
    if len(by_id) != len(capabilities):
        raise ValueError("duplicate capability identity")
    descriptors: list[dict[str, Any]] = []
    included: set[str] = set()
    visiting: set[str] = set()

    def include(capability_id: str) -> None:
        if capability_id in visiting:
            raise ValueError("required capability dependency cycle")
        if capability_id in included:
            return
        if capability_id not in by_id:
            raise ValueError("missing required capability descriptor")
        visiting.add(capability_id)
        capability = by_id[capability_id]
        for dependency in capability["requires"]:
            include(dependency)
        visiting.remove(capability_id)
        included.add(capability_id)
        descriptors.append(capability)

    for original in originals:
        owners = [c for c in capabilities if original in c["original_skills"]]
        if len(owners) != 1:
            raise ValueError("original must have exactly one owning descriptor")
        include(owners[0]["id"])

    provider_names = {c["provider"] for c in descriptors}
    providers = [p for p in registry["providers"] if p["name"] in provider_names]
    if (
        len(providers) != len(provider_names)
        or {p["name"] for p in providers} != provider_names
    ):
        raise ValueError("missing or duplicate provider metadata")
    return {
        "query": query,
        "kind": kind,
        "purpose": purpose,
        "policy": registry["policy"],
        "capabilities": descriptors,
        "providers": providers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "purpose", help="exact semantic-purpose ID or provider-qualified original"
    )
    args = parser.parse_args()
    try:
        registry = json.loads((CATALOGS / "registry.json").read_text(encoding="utf-8"))
        purposes = json.loads((CATALOGS / "purposes.json").read_text(encoding="utf-8"))
        result = query_catalog(args.purpose, registry, purposes)
        output = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Catalog query failed: {error}", file=sys.stderr)
        return 2
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
