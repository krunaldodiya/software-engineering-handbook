# Software Engineering Handbook

A public, risk-scaled software-engineering handbook and sparse
mixture-of-experts skill router for humans, teams, and AI coding harnesses.

## Vision: broad capability, sparse activation

The catalog can cover many high-quality engineering capabilities without
loading them all for every task. Like a sparse mixture-of-experts model, the
router inspects small descriptors first and activates only the few experts
whose exact triggers and current risks require them.

- The handbook core is always active and owns precedence, risk, authority,
  evidence, and delivery claims.
- `experts/registry.json` is the machine-readable capability catalog.
- `experts/resolution.md` selects the smallest compatible set, with at most one
  primary workflow expert.
- Expert bodies are separated by responsibility and loaded progressively.
- A trusted compatible original provider skill is preferred when already
  registered; its internal fallback is suppressed.
- If the original is absent, untrusted, incompatible, or unavailable, the
  router uses the bounded internal fallback.
- Unselected bodies, duplicate provider routers, installers, hooks, persistent
  services, and unauthorized side effects stay inactive.
- Risk-scaled expert and context budgets keep task latency and context cost
  tied to the work, not to catalog size.

Current reviewed capability families adapt useful engineering workflows from
Superpowers, Ponytail, Addy Osmani's Agent Skills, Understand Anything,
Karpathy's autoresearch, GitHub Spec Kit, OpenSpec, and BMAD Method. Source pins,
adaptation maps, exclusions, and update
rules are recorded in
[`handbook/software-engineering/references.md`](handbook/software-engineering/references.md).

## Repository contents

- `handbook/software-engineering/` — portable normative handbook and source
  register.
- `managed-skills/software-engineering-handbook/` — OMP skill router, expert
  registry, resolver, internal fallback modules, and registry validator.
- `rules/engineering-handbook-enforcement.md` — global OMP enforcement rule.

The OMP live paths map to the tracked assets:

- `~/.omp/agent/handbook/software-engineering/` →
  `handbook/software-engineering/`
- `~/.omp/agent/managed-skills/software-engineering-handbook/` →
  `managed-skills/software-engineering-handbook/`
- `~/.omp/agent/rules/engineering-handbook-enforcement.md` →
  `rules/engineering-handbook-enforcement.md`

## Use

Read [`handbook/software-engineering/README.md`](handbook/software-engineering/README.md)
first, then the one primary chapter selected by its routing table. In OMP,
install the managed skill and enforcement rule with the restore procedure
below. Other harnesses can adapt the same registry and resolution contracts
without importing OMP-specific paths.

Validate the expert catalog before proposing a change:

```sh
python3 managed-skills/software-engineering-handbook/validate_registry.py
```

## Contribute

Issues and pull requests are welcome. Keep changes evidence-backed, portable,
and narrowly owned.

For a new or updated provider capability:

1. pin and review the exact upstream source;
2. gap-map the capability against existing experts;
3. reuse an existing module or add one bounded expert module;
4. register triggers, exclusions, prerequisites, conflicts, effects, evidence,
   context budget, and rollback;
5. preserve trusted-original preference and internal fallback behavior;
6. add pressure checks for original-present, original-absent, conflict, and
   active-budget paths; and
7. update the source register and obtain exact-byte review.

Do not add a second workflow router, provider runtime, hidden installation,
whole-catalog body loading, or a capability already covered by a compatible
expert.

## Safety and repository boundary

Autonomy never grants authority to access systems or secrets, take destructive
action, publish, release, deploy, or accept residual risk. Those actions remain
subject to higher-authority instructions, local controls, and explicit
authorization.

This public repository contains only the governance assets listed above. Never
commit OMP configuration, environment files, databases, caches, sessions,
credentials, secrets, private project adapters, or unrelated assets.

## Install or restore

`~/.omp/agent/engineering-governance` is the canonical checkout. Make and commit handbook, managed-skill, and enforcement-rule edits there; the live OMP paths are relative symlinks to its tracked assets.

Set `HANDBOOK_REVISION` to the full reviewed commit ID from a trusted release
record, then run the following from a POSIX-compatible shell. The procedure
never follows moving `main`: it fetches and validates only that exact commit.
An existing canonical checkout is accepted only when it has the expected
origin, is on a clean `main` branch, and can be fast-forwarded to the pinned
revision. An occupied live path is accepted only when it is already the exact
expected symlink; otherwise the procedure stops without replacing it.

```sh
set -eu

agent_root="$HOME/.omp/agent"
repo="$agent_root/engineering-governance"
origin_url="https://github.com/krunaldodiya/software-engineering-handbook.git"

fail() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

revision="${HANDBOOK_REVISION:-}"
[ "${#revision}" -eq 40 ] ||
  fail "HANDBOOK_REVISION must be a full 40-character commit ID"
case "$revision" in
  *[!0-9a-f]*) fail "HANDBOOK_REVISION must contain lowercase hexadecimal only" ;;
esac

staged_repo=
validation_dir=
source_repo=
cleanup() {
  if [ -n "$validation_dir" ]; then
    git -C "$source_repo" worktree remove --force "$validation_dir" \
      >/dev/null 2>&1 || rm -rf "$validation_dir"
  fi
  if [ -n "$staged_repo" ] && [ -e "$staged_repo" ]; then
    rm -rf "$staged_repo"
  fi
}
trap cleanup 0 1 2 15

preflight_parent() {
  parent_path="$1"
  [ ! -L "$parent_path" ] ||
    fail "$parent_path is a symlink; inspect it before retrying"
  [ ! -e "$parent_path" ] || [ -d "$parent_path" ] ||
    fail "$parent_path exists and is not a directory; inspect it before retrying"
}

preflight_parent "$agent_root"
mkdir -p "$agent_root"

existing_repo=0
if [ -L "$repo" ]; then
  fail "$repo must be a checkout, not a symlink"
elif [ -e "$repo" ]; then
  [ -d "$repo/.git" ] || fail "$repo exists but is not the canonical checkout"
  existing_repo=1
  source_repo="$repo"
else
  staged_repo="$(mktemp -d "$agent_root/.engineering-governance.XXXXXX")"
  git -C "$staged_repo" init -b main
  git -C "$staged_repo" remote add origin "$origin_url"
  source_repo="$staged_repo"
fi

origin="$(git -C "$source_repo" remote get-url origin)"
case "$origin" in
  https://github.com/krunaldodiya/software-engineering-handbook.git | \
  git@github.com:krunaldodiya/software-engineering-handbook.git | \
  ssh://git@github.com/krunaldodiya/software-engineering-handbook.git)
    ;;
  *)
    fail "$source_repo has unexpected origin: $origin"
    ;;
esac

if [ "$existing_repo" -eq 1 ]; then
  [ "$(git -C "$repo" branch --show-current)" = main ] ||
    fail "$repo must be on main"
  [ -z "$(git -C "$repo" status --porcelain)" ] ||
    fail "$repo has local changes; preserve them before restoring"
fi

git -C "$source_repo" fetch --no-tags origin "$revision"
candidate="$(git -C "$source_repo" rev-parse --verify 'FETCH_HEAD^{commit}')"
[ "$candidate" = "$revision" ] ||
  fail "fetched commit does not match HANDBOOK_REVISION"
if [ "$existing_repo" -eq 1 ]; then
  git -C "$repo" merge-base --is-ancestor HEAD "$candidate" ||
    fail "pinned revision cannot fast-forward local main"
fi

require_candidate_type() {
  asset_path="$1"
  expected_type="$2"
  asset_name="$3"
  actual_type="$(
    git -C "$source_repo" cat-file -t "$candidate:$asset_path" 2>/dev/null
  )" || fail "$asset_name is missing from the pinned candidate revision"
  [ "$actual_type" = "$expected_type" ] ||
    fail "$asset_name has type $actual_type in the pinned candidate, expected $expected_type"
}

require_candidate_type \
  "handbook/software-engineering" tree "canonical handbook asset"
require_candidate_type \
  "managed-skills/software-engineering-handbook" tree "canonical managed skill"
require_candidate_type \
  "rules/engineering-handbook-enforcement.md" blob "canonical enforcement rule"

if [ "$existing_repo" -eq 0 ]; then
  git -C "$staged_repo" checkout -B main "$candidate"
  validation_dir="$staged_repo"
else
  validation_dir="$(
    mktemp -d "$agent_root/.engineering-governance-validation.XXXXXX"
  )"
  git -C "$repo" worktree add --detach "$validation_dir" "$candidate"
fi

python3 \
  "$validation_dir/managed-skills/software-engineering-handbook/validate_registry.py"
python3 -O \
  "$validation_dir/managed-skills/software-engineering-handbook/validate_registry.py"

if [ "$existing_repo" -eq 1 ]; then
  git -C "$repo" worktree remove "$validation_dir"
fi
validation_dir=

require_worktree_type() {
  asset_path="$repo/$1"
  expected_type="$2"
  asset_name="$3"
  [ ! -L "$asset_path" ] ||
    fail "$asset_name in the current worktree must not be a symlink"
  case "$expected_type" in
    directory)
      [ -d "$asset_path" ] ||
        fail "$asset_name is not a directory in the current worktree"
      ;;
    regular-file)
      [ -f "$asset_path" ] ||
        fail "$asset_name is not a regular file in the current worktree"
      ;;
    *)
      fail "unsupported worktree type check: $expected_type"
      ;;
  esac
}

preflight_link() {
  link_path="$1"
  link_text="$2"
  if [ -L "$link_path" ]; then
    [ "$(readlink "$link_path")" = "$link_text" ] ||
      fail "$link_path is an unexpected symlink; inspect it before retrying"
  elif [ -e "$link_path" ]; then
    fail "$link_path already exists and is not a symlink; inspect it before retrying"
  fi
}

preflight_parent "$agent_root/handbook"
preflight_parent "$agent_root/managed-skills"
preflight_parent "$agent_root/rules"
preflight_link \
  "$agent_root/handbook/software-engineering" \
  "../engineering-governance/handbook/software-engineering"
preflight_link \
  "$agent_root/managed-skills/software-engineering-handbook" \
  "../engineering-governance/managed-skills/software-engineering-handbook"
preflight_link \
  "$agent_root/rules/engineering-handbook-enforcement.md" \
  "../engineering-governance/rules/engineering-handbook-enforcement.md"

mkdir -p "$agent_root/handbook" "$agent_root/managed-skills" "$agent_root/rules"
if [ "$existing_repo" -eq 0 ]; then
  [ ! -e "$repo" ] && [ ! -L "$repo" ] ||
    fail "$repo appeared during validation; inspect it before retrying"
  mv "$staged_repo" "$repo"
  staged_repo=
else
  git -C "$repo" merge --ff-only "$candidate"
fi

install_link() {
  link_path="$1"
  link_text="$2"
  if [ -L "$link_path" ]; then
    [ "$(readlink "$link_path")" = "$link_text" ] ||
      fail "$link_path changed after preflight; inspect it before retrying"
  elif [ -e "$link_path" ]; then
    fail "$link_path appeared after preflight; inspect it before retrying"
  else
    ln -s "$link_text" "$link_path"
  fi
}

require_worktree_type \
  "handbook/software-engineering" directory "canonical handbook asset"
require_worktree_type \
  "managed-skills/software-engineering-handbook" directory "canonical managed skill"
require_worktree_type \
  "rules/engineering-handbook-enforcement.md" regular-file "canonical enforcement rule"

install_link \
  "$agent_root/handbook/software-engineering" \
  "../engineering-governance/handbook/software-engineering"
install_link \
  "$agent_root/managed-skills/software-engineering-handbook" \
  "../engineering-governance/managed-skills/software-engineering-handbook"
install_link \
  "$agent_root/rules/engineering-handbook-enforcement.md" \
  "../engineering-governance/rules/engineering-handbook-enforcement.md"

trap - 0 1 2 15
```

## Upstream attribution

This repository independently adapts workflow concepts; it does not vendor
upstream skill bodies or runtimes. Upstream projects, exact reviewed revisions,
licenses, exclusions, and provenance links are recorded in the
[source register](handbook/software-engineering/references.md). Project names
and trademarks remain property of their respective owners.

## License

[MIT](LICENSE)
