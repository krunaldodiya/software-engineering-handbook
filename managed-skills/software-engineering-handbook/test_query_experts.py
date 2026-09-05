"""Behavioral checks for the optional, non-activating catalog query CLI."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = Path(__file__).with_name("query_experts.py")
CATALOGS = ROOT / "skills/software-engineering-handbook/experts"


class QueryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = json.loads((CATALOGS / "registry.json").read_text())
        self.purposes = json.loads((CATALOGS / "purposes.json").read_text())

    def invoke(
        self, query: str, script: Path = SCRIPT
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-B", str(script), query],
            cwd=tempfile.gettempdir(),
            capture_output=True,
            text=True,
            check=False,
        )

    def result(self, query: str, script: Path = SCRIPT) -> dict[str, Any]:
        result = self.invoke(query, script)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        value = json.loads(result.stdout)
        self.assertEqual(
            set(value),
            {
                "query",
                "kind",
                "purpose",
                "policy",
                "capabilities",
                "providers",
            },
        )
        return value

    def test_group_query_is_bounded_and_complete(self) -> None:
        group = next(
            p for p in self.purposes["equivalence_groups"] if p["id"] == "ideation"
        )
        result = self.result("ideation")
        owners = [
            c
            for c in self.registry["capabilities"]
            if set(c["original_skills"]) & set(group["ordered_alternatives"])
        ]
        self.assertEqual(result["purpose"], group)
        self.assertEqual(result["kind"], "equivalence")
        self.assertEqual(result["policy"], self.registry["policy"])
        self.assertEqual(
            {c["id"]: c for c in result["capabilities"]}, {c["id"]: c for c in owners}
        )
        self.assertEqual(
            result["providers"],
            [
                p
                for p in self.registry["providers"]
                if p["name"] in {c["provider"] for c in owners}
            ],
        )
        baseline_bytes = sum(
            (CATALOGS / name).stat().st_size
            for name in ("registry.json", "purposes.json")
        )
        self.assertLess(len(self.invoke("ideation").stdout.encode()), baseline_bytes)
        self.assertEqual(self.invoke("ideation").stdout, self.invoke("ideation").stdout)

    def test_group_member_preserves_all_alternatives(self) -> None:
        result = self.result("superpowers/brainstorming")
        expected = self.result("ideation")
        expected["query"] = "superpowers/brainstorming"
        self.assertEqual(result, expected)

    def test_native_and_distinct_have_different_fallback_ownership(self) -> None:
        native = self.purposes["native_purposes"][0]
        result = self.result(native["id"])
        self.assertEqual(result["kind"], "native")
        self.assertEqual(result["purpose"], native)
        self.assertEqual(result["capabilities"], [])
        self.assertEqual(result["providers"], [])
        original = self.purposes["distinct_originals"][0]
        result = self.result(original)
        self.assertEqual(result["kind"], "distinct")
        self.assertEqual(result["purpose"], {"id": original})
        self.assertEqual(
            result["capabilities"],
            [
                c
                for c in self.registry["capabilities"]
                if original in c["original_skills"]
            ],
        )

    def test_unknown_and_malformed_arguments_never_dump_catalogs(self) -> None:
        for query in ("", "unknown-purpose", "brainstorming", "--unknown"):
            with self.subTest(query=query):
                result = self.invoke(query)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")

    def installed_fixture(self, root: Path) -> tuple[Path, Path]:
        script = root / "managed-skills/software-engineering-handbook/query_experts.py"
        script.parent.mkdir(parents=True)
        shutil.copyfile(SCRIPT, script)
        catalogs = root / "skills/software-engineering-handbook/experts"
        catalogs.mkdir(parents=True)
        for name in ("registry.json", "purposes.json"):
            shutil.copyfile(CATALOGS / name, catalogs / name)
        return script, catalogs / "registry.json"

    def test_installed_layout_is_cwd_independent_and_does_not_write(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script, _ = self.installed_fixture(root)
            before = {
                str(p.relative_to(root)): p.read_bytes()
                for p in root.rglob("*")
                if p.is_file()
            }
            self.assertEqual(self.result("ideation", script), self.result("ideation"))
            after = {
                str(p.relative_to(root)): p.read_bytes()
                for p in root.rglob("*")
                if p.is_file()
            }
            self.assertEqual(before, after)

    def test_required_dependencies_are_complete_and_invalid_graphs_fail(self) -> None:
        original = self.purposes["distinct_originals"][0]
        owner = next(
            c for c in self.registry["capabilities"] if original in c["original_skills"]
        )
        dependency = next(c for c in self.registry["capabilities"] if c is not owner)
        owner["requires"] = [dependency["id"]]
        with tempfile.TemporaryDirectory() as directory:
            script, registry_path = self.installed_fixture(Path(directory))
            registry_path.write_text(json.dumps(self.registry))
            result = self.result(original, script)
            self.assertEqual(result["capabilities"], [dependency, owner])
            dependency["requires"] = [owner["id"]]
            registry_path.write_text(json.dumps(self.registry))
            result = self.invoke(original, script)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
            dependency["requires"] = ["absent-capability"]
            registry_path.write_text(json.dumps(self.registry))
            result = self.invoke(original, script)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")

    def test_missing_owner_is_not_partial_success(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            script, registry_path = self.installed_fixture(Path(directory))
            self.registry["capabilities"] = [
                c
                for c in self.registry["capabilities"]
                if "superpowers/brainstorming" not in c["original_skills"]
            ]
            registry_path.write_text(json.dumps(self.registry))
            result = self.invoke("ideation", script)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
