---
name: kujo-benchmarks-capsule-workflows
description: "Use this skill when running, validating, comparing, or maintaining the Capsule benchmark tool: `bin/capsule`, `make`, `inspect`, `validate`, `--stable`, `--dry-run`, `capsule.json`, `capsule.md`, `manifest.json`, fixture projects, benchmark evidence, or benchmarks-capsule source/test changes."
---

# Kujo Benchmarks Capsule Workflows

Use Capsule as a benchmark artifact and deterministic Kujo CLI that turns a local project directory into a structured handoff capsule for another agent or human.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
CAPSULE_REPO="${CAPSULE_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/benchmarks-capsule}"
cd "$CAPSULE_REPO"
./bin/capsule --help
./bin/capsule make ./fixtures/basic-project --out ./tmp/basic --stable
./bin/capsule inspect ./tmp/basic/capsule.json
./bin/capsule validate ./tmp/basic/capsule.json
./bin/capsule make ./fixtures/basic-project --dry-run
```

## Workflow Notes

- `bin/capsule` is a thin launcher; all logic lives in Kujo under `src/`.
- `make` writes `capsule.json`, `capsule.md`, and `manifest.json` unless `--format` or `--dry-run` changes output.
- `--stable` pins timestamp to `1970-01-01T00:00:00Z`, sorts output, uses POSIX-style relative paths, and should produce byte-identical repeated output.
- `validate` checks required shape, list types, file records, ignored reason vocabulary, and SHA-256 hex fields.
- Exit codes are `0` success, `1` validation/check failure, `2` usage error, and `3` unexpected runtime error.
- The project is a benchmark run artifact; evidence under `benchmark/` records the model/tool run and should not be confused with normal generated output.

When reporting results, state the command, output directory, stable mode, generated files, validation result, and whether benchmark evidence was touched.

## Capsule Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `SPEC.md`
3. `ACCEPTANCE.md`
4. `TOOLCHAIN_NOTES.md`
5. `src/cli.kujo`, `src/main.kujo`, `src/scanner.kujo`, `src/schema.kujo`, `src/manifest.kujo`, `src/markdown.kujo`
6. `tests/*.kujo`
7. `scripts/run_checks.sh`
8. Relevant `fixtures/`
9. Relevant `benchmark/` evidence only when the task targets benchmark artifacts

Preserve CLI command names, output shapes, stable-mode determinism, redacted previews, ignore semantics, manifest checksums, and exit-code behavior unless the task explicitly changes the contract.

Run validation after source, docs, fixture, benchmark, or contract changes:

```bash
bash scripts/run_checks.sh
```

## Search And Safety

- Exclude `tmp/`, generated capsule outputs, and benchmark bulk unless targeted.
- Secret redaction is intentionally simple and not a full secret scanner; do not overstate it.
- Remember that `inspect` and `validate` are subject to Kujo's `parse_json` 1 MiB input cap.
- Keep `KUJO_BIN` and launcher behavior compatible with the sibling Kujo release fallback.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`, `SPEC.md`, `ACCEPTANCE.md`, `TOOLCHAIN_NOTES.md`.
- Status: repo-backed: `bin/capsule`, `src/*.kujo`, `tests/*.kujo`, `scripts/run_checks.sh`, `fixtures/`, `benchmark/`.
