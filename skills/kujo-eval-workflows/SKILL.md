---
name: kujo-eval-workflows
description: "Use this skill when creating, running, debugging, or maintaining Kujo Eval deterministic evaluation suites: `eval.json`, `kujo run main.kujo run`, `report`, `compare`, `lint`, `list-checks`, `snapshots`, `policy-explain`, `verify-manifest`, snapshot tests, JSON/HTTP/file/command checks, Eval artifacts, policy profiles, CI gates, or Eval CLI/source/test changes."
---

# Kujo Eval Workflows

Use Eval as a deterministic outcome checker for agents, CLIs, files, JSON
payloads, HTTP endpoints, snapshots, and workflow artifacts. Eval belongs to
Kujo's Control layer: Spec defines what should happen; Eval checks whether the
actual output produced the required evidence.

Canonical local source is usually
`/Users/robertdevore/2026/Kujolang/kujo-repos/eval`. Do not confuse Eval with
neighboring Kujo tools such as Muzzle, RunLedger, Spec, or PackWrite. Muzzle
runs quiet workflows, RunLedger records agent-run receipts, Spec defines task
contracts, PackWrite assembles prompt/context packets, and Eval performs
deterministic pass/fail assertions.

## Agent Workflow

1. Verify the runtime and command surface:

```bash
export KUJO_BIN=/path/to/kujo/target/release/kujo
"$KUJO_BIN" --version
"$KUJO_BIN" run main.kujo version
"$KUJO_BIN" run main.kujo list-checks
```

Use the Kujo language runtime binary, not the unrelated Python `kujo` linter.
The canonical invocation is `kujo run main.kujo <command> [options]`. VM-first
execution is the default; use `--interpreter` only for parity/debugging.

2. Prefer canonical examples before mining tests or historical checklists:

- `examples/release_gate_suite.json`: minimal passing smoke/release suite.
- `examples/enterprise_cli_quality_gate.json`: policy-first CLI checks.
- `examples/enterprise_api_contract_gate.json`: fixture-backed API contract checks.
- `examples/enterprise_agent_output_gate.json`: agent output structure/content checks.
- `examples/policy_profile_release_gate.json`: profile-driven policy defaults.
- `examples/strict_enterprise_policy_gate.json`: strict release policy gate.
- `examples/sandbox_adjacent_policy_gate.json`: constrained fixture-only policy boundary.

Treat `examples/basic_suite.json` as an expected-fail demo. Treat
`examples/large_suite_fixture.json` and `examples/io_heavy_regression_suite.json`
as scale/performance fixtures, not first-copy onboarding examples.

3. Run suites with isolated output directories and machine-readable output:

```bash
"$KUJO_BIN" run main.kujo run examples/release_gate_suite.json --output-dir .eval_quickstart --json
"$KUJO_BIN" run main.kujo run examples/release_gate_suite.json --output-dir .eval_quickstart --summary-only
"$KUJO_BIN" run main.kujo report examples/release_gate_suite.json --rerun --output-dir .eval_quickstart --format html
```

Generated artifacts include `eval-report.<ext>`, `last_run.json`,
`history.json`, `summary.json`, `last_failures.json`, `cli-summary.json`, and
`artifact-manifest.json`. Treat `.eval_*`, `eval_results/`, report outputs, and
snapshot updates as generated unless the task explicitly targets them.

4. When failures occur, inspect artifacts before changing checks:

```bash
"$KUJO_BIN" run main.kujo run eval.json --output-dir .eval_debug --json
"$KUJO_BIN" run main.kujo report eval.json --output-dir .eval_debug --format md
"$KUJO_BIN" run main.kujo compare .eval_old/last_run.json .eval_debug/last_run.json
```

Use `--quiet` for CI noise control, `--verbose` when check details are needed,
`--filter`, `--tags`, `--skip-tags`, and `--only-failed` for focused reruns, and
`--summary-channel-path <file>` when another tool needs the stable handoff
artifact somewhere other than the output directory.

## Suite Authoring

Create or edit pure JSON suites. Do not add `#` comments; use `_comment` fields
or adjacent docs if humans need notes.

Minimum shape:

```json
{
  "name": "my-agent-eval",
  "description": "Checks the agent output contract.",
  "version": "1.0.0",
  "output_dir": "./eval_results",
  "snapshot_dir": "./snapshots",
  "stop_on_failure": false,
  "tests": [
    {
      "name": "agent output file exists",
      "check": "file_exists",
      "params": {
        "path": "./output/agent-result.json"
      }
    }
  ]
}
```

Common check families:

- Command/output: `command_succeeds`, `command_fails`, `exit_code_equals`,
  `output_contains`, `output_does_not_contain`, `output_matches_glob`,
  `command_timing_less_than`.
- Files/directories: `file_exists`, `file_contains`, `file_matches_regex`,
  `file_line_count`, `two_files_equal`, `directory_diff`, `directory_contains`.
- JSON/data: `json_matches_shape`, `json_value_equals`,
  `stdout_json_matches_shape`, `command_stdout_json_path_equals`.
- Snapshots: `snapshot_matches`; create/update baselines with
  `--update-snapshots` or `params.update: "true"`.
- Environment/HTTP: `env_var_equals`, `http_status`, `http_body_contains`.

Use `retry` only for known flaky external surfaces, `depends_on` to skip
downstream checks after prerequisite failures, and `timeout_seconds` for any
command that could hang. Use `parallel_workers` for independent file-check
fast paths when deterministic ordering still matters.

## Policy And CI

For CI or enterprise gates, fail closed deliberately:

```json
{
  "policy_profile": "release-gate",
  "require_command_policy": true,
  "path_policy_mode": "allowlist-required",
  "allowed_commands": ["kujo", "bash"],
  "allowed_command_patterns": ["kujo run main.kujo"],
  "blocked_arg_patterns": ["rm -rf", "curl | sh"],
  "allowed_paths": ["./examples", "./output"],
  "allowed_env_vars": ["CI"]
}
```

Inspect effective policy before relying on it:

```bash
"$KUJO_BIN" run main.kujo policy-explain examples/release_gate_suite.json --policy-stage release --json
```

Use `--artifact-checksums` or `artifact_checksums: true` when downstream systems
need integrity evidence, then verify with:

```bash
"$KUJO_BIN" run main.kujo verify-manifest --output-dir .eval_quickstart --json
```

Remember Eval is not a sandbox. Command and file checks run in the host
environment. For high-risk suites, combine Eval policy fields with containers,
isolated runners, least-privilege mounts, and external watchdogs.

## Maintaining Eval

Source map:

- `main.kujo`: CLI dispatch and command orchestration.
- `src/cli.kujo`: CLI parsing and help text.
- `src/config.kujo`: suite loading, validation, known checks, policy normalization.
- `src/checks.kujo`: 27 check implementations and command/file safety logic.
- `src/eval_core.kujo`: suite execution, retries, dependencies, comparison.
- `src/report.kujo`: Markdown, HTML, JUnit, TAP, and NDJSON reports.
- `src/snapshot.kujo`: snapshot listing, update, and comparison.
- `schema/eval-suite.schema.json`: suite contract schema.
- `tests/*_tests.kujo`: contract, CLI integration, security, coverage, quality,
  stress, benchmark, and runtime parity coverage.

When adding a check type:

1. Implement the check in `src/checks.kujo`.
2. Register it in `run_check`.
3. Add it to `KNOWN_CHECKS` in `src/config.kujo`.
4. Update `schema/eval-suite.schema.json`.
5. Update `docs/eval-suite-reference.md`, `docs/API_REFERENCE.md`, and any
   command inventory/docs parity expectations.
6. Add contract, CLI, and edge-case coverage.

When adding CLI commands or report formats, preserve exact output contracts
unless the task explicitly changes them. Update help text, generated command
inventory, docs parity checks, and integration tests together.

Validate changes with the smallest relevant command first, then broaden:

```bash
"$KUJO_BIN" run main.kujo lint eval.json
"$KUJO_BIN" run main.kujo run examples/release_gate_suite.json --output-dir .eval_smoke --json
"$KUJO_BIN" test
bash scripts/generate_command_inventory.sh --check
bash scripts/verify_docs_command_parity.sh
bash scripts/verify_artifact_contract.sh
bash scripts/release_quality_gates.sh
```

Use release/parity scripts' watchdog environment variables when local runtime
capture is noisy or slow, especially `KUJO_EVAL_GATE_TIMEOUT_SECONDS`,
`KUJO_EVAL_DOCS_WATCHDOG_TIMEOUT_SECONDS`, and benchmark budget variables.

## Kujo Gotchas

- Use `push(arr, value)`; never write `arr[len(arr)] := value`.
- Assign dict literals to a temporary before passing them to `push()`.
- Do not use `test` as a variable name; use `tdef` or `test_item`.
- Keep `from ... import ...` statements at file top level.
- Export functions that are imported across modules.
- Compare `path_exists()` with `true`/`false`, not `1`/`0`.
- `contains()` and `has_key()` may behave int-like; follow existing local
  comparisons when changing nearby code.
- Interpreter-mode RUFRUN001 warnings can be benign; rely on exit code and
  generated artifacts for pass/fail decisions.

## Search Hygiene

For broad searches, exclude generated/bulk output unless the task targets it:

```bash
rg "pattern" -g '!eval_results/**' -g '!tests/*.out' -g '!examples/fixtures/contracts/**' -g '!.eval_*/**'
```

Prioritize canonical examples, `README.md`, `docs/QUICKREF.md`,
`docs/eval-suite-reference.md`, `docs/COMMAND_INVENTORY.md`,
`docs/ARCHITECTURE.md`, and `docs/agent-notes.md` before older checklists or
generated reports.
