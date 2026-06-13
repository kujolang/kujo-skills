---
name: kujo-spec-workflows
description: "Use this skill when creating, validating, rendering, exporting, converting, documenting, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.json`, `.spec.toml`, `spec validate`, `render`, `export-agent-context`, `ci`, schemas, command inventory, shell completions, safe-write mode, template imports, or `spec` source/test changes."
---

# Kujo Spec Workflows

Use Spec to turn task requirements into structured, reviewable contracts with goals, scope, acceptance criteria, risks, dependencies, review expectations, and agent context exports.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
SPEC_REPO="${SPEC_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/spec}"
cd "${SPEC_REPO}"
export PATH="/path/to/kujo-spec/scripts:$PATH"
spec validate specs/dark-mode.spec.yml
spec render specs/dark-mode.spec.yml
spec export-agent-context specs/dark-mode.spec.yml
spec ci ./specs --format json --max-files 200 --jobs 4
```

## Workflow Notes

- YAML is the recommended authoring format; JSON specs do not need Python YAML/TOML parsing.
- Command inventory is generated from `spec help`; regenerate/check it when command surfaces change.
- Safe-write and template-source policies are security boundaries.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo Spec Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `schema/spec.schema.json`
3. `src/validate.kujo`
4. `src/render.kujo`
5. `src/export.kujo`
6. `src/convert.kujo`
7. `scripts/spec`
8. `docs/COMMAND_INVENTORY.md`
9. `tests/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
export KUJO_BIN=/path/to/kujo/target/release/kujo
bash tests/run_tests.sh
bash tests/benchmark.sh
bash scripts/release_quality_gates.sh
bash scripts/verify_docs_command_parity.sh
bash scripts/verify_completion_parity.sh
bash scripts/verify_test_runtime_parity.sh
```

## Search And Safety

- Use `spec version`; `--version` is documented as not implemented.
- Do not bypass safe-write restrictions without explicit user intent.
- Keep schema, examples, docs, command inventory, and completions aligned.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `package.json`.
- Status: repo-backed: `schema/spec.schema.json`.
- Status: repo-backed: `src/validate.kujo`.
