---
name: kujo-scout-workflows
description: "Use this skill when running, interpreting, extending, or maintaining Scout, the Kujo-native codebase intelligence tool: `kujo run scout.kujo`, repo context packs, `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, `scan_manifest.json`, security exports, baseline suppression, Kennel metadata, Scout fixtures, snapshots, or Scout regression scripts."
---

# Kujo Scout Workflows

Use Scout to turn a local repository into an agent-readable context pack with structure, dependencies, routes, security smells, review checklists, and machine-readable manifests.

## Running Scout

Prefer the stable entrypoint from the Scout repo root:

```bash
kujo run scout.kujo -- . --quick
kujo run scout.kujo -- ../target-project -o ./reports -d 6
kujo run scout.kujo -- ./src --skip-deps --skip-routes -o ./security-audit
```

Use `--quick` or `--output-profile minimal` when the user wants a compact first-pass context pack. Use full output when downstream agents need `FILE_TREE.md`, `AGENTS.md`, `CHECKLIST.md`, route tables, and review material.

Scout writes to `<output-root>/<project-name>-YYYYMMDD-HHmmss-<epoch-ms>/`. By default the output root is `./results`.

## Interpreting Outputs

- Start with `scan_manifest.json` for artifact paths, schema version, and run metadata.
- Use `README.md` for the human report: metrics, routes, dependencies, and security findings.
- Use `llms.txt` for compact context injection.
- Use `AGENTS.md` when preparing an AI coding assistant to work in the scanned repo.
- Use `CHECKLIST.md` for review follow-up, especially security-highlighted items.
- Use `intelligence.json` for programmatic parsing and automation.
- Treat `security.sarif` and `security.jsonl` as optional exports enabled by `--security-export sarif` or `--security-export jsonl`.

When summarizing a scan, include the target, output directory, code file count, route/dependency/security counts, profile, and the most important follow-up findings. Do not claim Scout proves a repo is safe; it surfaces signals for review.

## Common Modes

```bash
# Route-only scan
kujo run scout.kujo -- ./api --skip-security --skip-deps -o ./api-routes

# Security exports for CI or security tooling
kujo run scout.kujo -- ./src --security-export sarif --security-export jsonl -o ./security-audit

# Baseline accepted findings
kujo run scout.kujo -- ./src --write-baseline --baseline scout-baseline.json
kujo run scout.kujo -- ./src --show-suppressed

# Kennel-compatible outputs
kujo run scout.kujo -- ./src --kennel-index --kennel-metadata -o ./scan-output
```

Config precedence is `CLI flags > config.json values > built-in hard defaults`. Keep `scout.kujo` version and `config.json` `tool.version` aligned.

## Scout Repo Work

Read in this order before changing Scout:

1. `README.md`
2. `scout.kujo`
3. `config.json`
4. `docs/SCOUT_EVOLUTION_CHECKLIST.md`
5. `docs/CONTRIBUTING_SCOUT.md` when working checklist items or contributor process
6. `docs/RELEASE_PROCESS.md` when changing versioning or release flow

Work checklist items top-to-bottom, one item per loop. Keep implementation, tests, docs, checkbox update, and work-log entry in the same focused change.

## Extension Points

- Language and manifest discovery: update `LANGUAGE_MAP` and `MANIFEST_FILES`.
- Route detection: extend language-specific route pattern blocks in the scan loop.
- Security detection: update `SECURITY_PATTERNS` and helper logic without reintroducing self-matches or obvious false positives.
- New artifact outputs: add payload builders and write steps near the output section.
- CLI flags: update argument parsing, `config.json`, README options, and tests together.

When adding analyzers or outputs, add or update a purpose-built fixture under `tests/fixtures/`, a focused script under `tests/scripts/`, generated schema/snapshot contracts when applicable, and the checklist work log.

## Testing

Check prerequisites when the environment is unknown:

```bash
kujo run --help >/dev/null
jq --version
python3 -c "import jsonschema; print(jsonschema.__version__)"
```

Use focused tests first, then the aggregate suite:

```bash
tests/scripts/test_test002_route_matrix.sh
tests/scripts/test_test003_security_matrix.sh
SCOUT_SKIP_SLOW=1 tests/scripts/run_all_scout_tests.sh
tests/scripts/run_all_scout_tests.sh
tests/scripts/check_version_consistency.sh
```

Set `KUJO_BIN=/absolute/path/to/kujo` when multiple Kujo binaries exist or the repo-local resolver is not enough.

## Search Hygiene

Use broad searches with generated output exclusions:

```bash
rg <pattern> README.md docs lib scout.kujo tests/scripts -g '!tests/tmp/**' -g '!results/**'
```

Treat `tests/fixtures/**` as regression contracts, not style guidance. Treat `tests/fixtures/test005/snapshots/**`, `tests/tmp/**`, and `results/**` as generated or golden output unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`, `config.json`, `CHANGELOG.md`, `scout.kujo`.
- Status: repo-backed: `docs/CONTRIBUTING_SCOUT.md`, `docs/SCOUT_EVOLUTION_CHECKLIST.md`, `docs/RELEASE_PROCESS.md`.
- Status: repo-backed: `tests/scripts/run_all_scout_tests.sh`, `tests/scripts/lib.sh`, `tests/fixtures/schemas/*`.
