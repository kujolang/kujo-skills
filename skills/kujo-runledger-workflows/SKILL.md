---
name: kujo-runledger-workflows
description: "Use this skill when recording, comparing, reporting, or maintaining RunLedger receipts for AI-agent build runs: `runledger start`, `finish`, `usage`, `cost`, `note`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` JSON files, run verdicts, token/cost capture, read-only git metadata receipts, RunLedger reports, or RunLedger CLI/tests/source changes."
---

# Kujo RunLedger Workflows

Use RunLedger as a local receipt system for agent attempts, not as an automated
judge. It records facts, manual usage/cost data, human verdicts, follow-ups, and
read-only git metadata in plain JSON.

Canonical local source is usually
`/Users/robertdevore/2026/Kujolang/kujo-repos/runledger`. Do not confuse
RunLedger with neighboring Kujo tools such as ChangeBucket, Eval, Spec, or
PackWrite. ChangeBucket measures change footprint, Eval runs deterministic
outcome checks, Spec defines task contracts, PackWrite assembles prompt/context
packets, and RunLedger records agent-run receipts and comparison reports. If a
user points at a neighboring Kujo repo such as `changebucket/`, `eval/`,
`spec/`, or `packwrite/`, verify whether the actual RunLedger checkout exists
beside it as `runledger/` before changing RunLedger-specific instructions.

## Agent Workflow

1. Verify the Kujo runtime and launcher:

```bash
kujo --help
runledger version
```

`kujo --help` should show a `run` command. Python's unrelated `kujo` lint tool
is not compatible. If the wrapper is not on `PATH`, run it from the repo with
`KUJO=/path/to/kujo ./bin/runledger ...`, or use
`kujo run /path/to/runledger/runledger.kujo -- <command> ...`. Keep the `--`
separator when invoking through `kujo run`.

2. Start each attempt before the agent changes the target repo:

```bash
runledger start --provider openai --model codex --task "Build Tool X" \
  --prompt ./prompt.md --repo /path/to/repo
```

Capture the returned run id. Use the same `--task` across comparable attempts.

3. During or after the run, add only data you actually know:

```bash
runledger usage <run-id> --input 190000 --output 26000 --cache-read 0 --cache-write 0
runledger cost <run-id> --total 0.92 --currency USD
runledger note <run-id> "Tests passed after one fix"
runledger followup <run-id> "Add JSON-output tests"
```

Usage and cost are manual; do not invent token counts, provider pricing, or totals.

4. Finish with a terminal status and concise verdict:

```bash
runledger finish <run-id> --status partial --verdict "good foundation, needs docs fixes"
```

Valid terminal statuses are `pass`, `partial`, `fail`, and `abandoned`.
`in_progress` is valid in stored records but not accepted by `finish`.

5. Inspect or publish summaries:

```bash
runledger list
runledger show <run-id>
runledger compare --task "Build Tool X"
runledger report --task "Build Tool X" --output RUNLEDGER_REPORT.md
```

Use `--json` with `list`, `show`, or `compare` when another tool should parse
the result. Use `--ledger <dir>` on any command, or `RUNLEDGER_DIR`, when the
receipt store should live somewhere other than `./.runledger`.

## Ledger Location

- Default storage is `./.runledger/runs/<run-id>.json` relative to the current
  working directory.
- Override with `--ledger <dir>` on commands or `RUNLEDGER_DIR`.
- A ledger can track runs across many repos; `--repo` only identifies the target repo for git metadata.
- Run ids are human-readable and sortable: `YYYY-MM-DD-<model>-<task>-NNN`.
- Treat `.runledger/`, temp ledgers, and generated report outputs as
  local/generated artifacts unless the task explicitly targets them.

## Git Metadata

RunLedger uses read-only git commands to capture start/end commit, dirty state,
and changed files. It must not stage, commit, reset, checkout, or otherwise
mutate git state.

If `--repo` is not a git repo, git fields should be `null` or empty and commands should still succeed.

## Output And Exit Contracts

- Exit `0`: success.
- Exit `1`: operational failure, such as no such run, invalid status, or corrupt file.
- Exit `2`: usage error, such as missing arguments, unknown commands, or invalid numeric flags.
- `list --json`, `show --json`, and `compare --json` print raw JSON.
- `report` prints markdown unless `--output <file>` is provided.
- Report output surfaces facts and human verdicts; it does not declare a best or worst run automatically.
- Stored `commands` and `tests` arrays are reserved by the schema; the current CLI does not populate them.

## Maintaining RunLedger

Source map:

- `runledger.kujo`: entry point.
- `bin/runledger`: launcher wrapper.
- `src/cli.kujo`: command parsing, user-facing output, exit codes.
- `src/storage.kujo`: local JSON persistence and id generation.
- `src/gitmeta.kujo`: read-only git metadata.
- `src/render.kujo`: tables, `show`, `compare`, and markdown reports.
- `src/record.kujo`: record schema defaults and status validation.
- `AGENTS.md`: maintainer orientation, search hygiene, and verification notes.
- `README.md` and `examples/build-tool-x.md`: canonical copyable examples.

Preserve exact CLI/report output unless intentionally updating integration
expectations and examples. Keep examples in `README.md` and
`examples/build-tool-x.md` copyable; use
`examples/RUNLEDGER_REPORT.example.md` for report shape, not source-code style.

Broad searches should exclude generated or bulky receipt output unless the task
targets it: `.runledger/`, temporary ledgers, and generated report outputs.

Validate changes with:

```bash
./tests/run.sh
KUJO=/path/to/kujo ./tests/run.sh
KUJO=/path/to/kujo ./bin/runledger help
```

`tests/run.sh` runs both `tests/runledger_test.kujo` and
`tests/cli_integration.sh`. For command-output changes, update
`tests/cli_integration.sh` and any generated report examples after inspecting
the intended output.
