---
name: kujo-scout-workflows
description: "Use this skill when scanning, packaging, reviewing, or maintaining Scout codebase intelligence outputs: `scout.kujo`, `--quick`, `--output`, `--max-depth`, dependency maps, route/API discovery, security findings, SARIF/JSONL exports, baselines, Kennel index metadata, generated context packs, or `scout` source/test changes."
---

# Kujo Scout Workflows

Use Scout to map a repository into agent-readable context: file tree, language mix, dependencies, routes, security smells, review checklist, baselines, and optional Kennel-compatible metadata.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
SCOUT_REPO="${SCOUT_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/scout}"
cd "${SCOUT_REPO}"
kujo run scout.kujo -- . --quick
kujo run scout.kujo -- ../my-project
kujo run scout.kujo -- ./src --skip-deps --skip-routes -o ./security-audit
kujo run scout.kujo -- ./src --security-export sarif --security-export jsonl -o ./security-audit
```

## Workflow Notes

- Scout writes run output under `results/` or the requested output root; inspect before committing.
- Security findings are signals for review, not proof of exploitability.
- Baselines suppress known findings; explain when generating or refreshing one.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo Scout Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `scout.kujo`
3. `lib/scout_runtime.kujo`
4. `lib/security_exports.kujo`
5. `lib/path_filters.kujo`
6. `tests/scripts/`
7. `docs/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
SCOUT_SKIP_SLOW=1 tests/scripts/run_all_scout_tests.sh
tests/scripts/test_test002_route_matrix.sh
tests/scripts/test_test003_security_matrix.sh
tests/scripts/test_test005_golden_snapshots.sh
```

## Search And Safety

- Do not scan huge generated/vendor directories unless the user targets them.
- Preserve relative path defaults unless absolute paths are requested.
- Keep Kennel-compatible output shape stable when changing index metadata.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `scout.kujo`.
- Status: repo-backed: `lib/scout_runtime.kujo`.
