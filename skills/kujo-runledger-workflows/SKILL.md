---
name: kujo-runledger-workflows
description: "Use this skill when recording, updating, comparing, reporting, or maintaining RunLedger local AI-agent run receipts: `runledger start`, `finish`, `usage`, `cost`, `followup`, `list`, `show`, `compare`, `report`, `.runledger/` data, markdown reports, ledger JSON schema, git metadata capture, or `runledger` source/test changes."
---

# Kujo RunLedger Workflows

Use RunLedger to record local receipts for AI-agent build runs: prompt, provider/model, repo state, changed files, test result, verdict, follow-ups, usage, and cost.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
RUNLEDGER_REPO="${RUNLEDGER_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/runledger}"
cd "${RUNLEDGER_REPO}"
KUJO=/path/to/kujo/target/release/kujo ./bin/runledger help
./bin/runledger start --provider openai --model codex --task "Build Tool X" --prompt ./examples/build-tool-x.md --repo .
./bin/runledger list
./bin/runledger compare
./bin/runledger report --output RUNLEDGER_REPORT.md
```

## Workflow Notes

- `.runledger/` contains local run data; treat it as runtime data unless the user explicitly wants it committed.
- Reports are generated handoff artifacts and should be reviewed before sharing or committing.
- RunLedger records facts and manual verdicts; it does not judge code quality by itself.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo RunLedger Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `runledger.kujo`
4. `src/cli.kujo`
5. `src/storage.kujo`
6. `src/gitmeta.kujo`
7. `src/render.kujo`
8. `tests/runledger_test.kujo`
9. `tests/cli_integration.sh`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
KUJO=/path/to/kujo/target/release/kujo ./tests/run.sh
KUJO=/path/to/kujo/target/release/kujo ./bin/runledger help
kujo run tests/runledger_test.kujo
```

## Search And Safety

- Avoid committing `.runledger/`, temp ledgers, or generated report outputs unless requested.
- Preserve exact CLI/report output unless updating integration expectations.
- Use terminal statuses only for `finish`: `pass`, `partial`, `fail`, `abandoned`.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `runledger.kujo`.
- Status: repo-backed: `tests/runledger_test.kujo`.
