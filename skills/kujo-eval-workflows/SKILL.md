---
name: kujo-eval-workflows
description: "Use this skill when creating, running, comparing, reporting, or maintaining Kujo Eval suites: `eval run`, `report`, `compare`, `snapshots`, `lint`, `policy-explain`, `verify-manifest`, JUnit/TAP/HTML/NDJSON reports, snapshot updates, policy profiles, artifact manifests, command inventories, or `eval` source/test changes."
---

# Kujo Eval Workflows

Use Eval for deterministic checks of agents, workflows, CLIs, files, snapshots, and generated outputs. Treat Eval reports as evidence of observed behavior, not a substitute for review.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
EVAL_REPO="${EVAL_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/eval}"
cd "${EVAL_REPO}"
export KUJO_BIN="${KUJO_BIN:-/path/to/kujo/target/debug/kujo}"
./kujo run main.kujo -- run examples/basic.eval.yml
./kujo run main.kujo -- report --format html
./kujo run main.kujo -- list-checks --json
```

## Workflow Notes

- Prefer JSON, NDJSON, JUnit, or TAP when downstream tools need machine-readable evidence.
- Use `--update-snapshots` only when the expected output intentionally changed.
- Artifact manifests and checksums are release evidence; inspect failures before regenerating.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo Eval Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `main.kujo`
3. `src/cli.kujo`
4. `src/eval_core.kujo`
5. `src/checks.kujo`
6. `src/report.kujo`
7. `src/snapshot.kujo`
8. `docs/COMMAND_INVENTORY.md`
9. `tests/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
export KUJO_BIN="${KUJO_BIN:-/path/to/kujo/target/debug/kujo}"
bash scripts/cli_smoke_matrix.sh
bash scripts/generate_command_inventory.sh --check
"$KUJO_BIN" test-run tests/contract_tests.kujo
"$KUJO_BIN" test-run tests/cli_integration_tests.kujo
```

## Search And Safety

- Do not update snapshots as a reflex; first explain the behavior change.
- Preserve exit behavior for failed checks and invalid suites.
- Keep command inventory, docs, and CLI help aligned after command changes.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `main.kujo`.
- Status: repo-backed: `src/cli.kujo`.
- Status: repo-backed: `tests/contract_tests.kujo`.
