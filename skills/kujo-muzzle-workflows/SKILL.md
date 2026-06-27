---
name: kujo-muzzle-workflows
description: "Use this skill when setting up, running, or reviewing Muzzle quiet workflows for AI-assisted development: `muzzle init`, `.muzzle/workflows/`, `.muzzle/manifests/`, `muzzle run`, `--json`, `--verbose`, `--dry-run`, workflow logs/reports, loop mode, or Muzzle safety and output-contract changes."
---

# Kujo Muzzle Workflows

Use Muzzle as a workflow compression layer: run known local workflows quietly, keep full output on disk, and return compact summaries or JSON to the agent.

## Agent Workflow

- Check setup with `muzzle --help`, `muzzle version`, and `muzzle list`.
- Prefer `muzzle run <workflow>` for known noisy build, test, deploy, scan, or release tasks.
- Use `muzzle run <workflow> --json` when a downstream step should parse status, exit code, duration, `log_path`, or `report_path`.
- Use `muzzle run <workflow> --dry-run` before new, destructive, networked, deploy, publish, or production-like workflows.
- Use `--verbose` only when live full output is needed; otherwise read logs after failure.
- On failure, first inspect the compact error excerpt, then use `muzzle logs <workflow>` or the returned `log_path` to read the full log.

## Project Setup

```bash
cd /path/to/project
muzzle init
muzzle list
muzzle run hello
muzzle run hello --json
```

Muzzle creates `.muzzle/workflows/`, `.muzzle/manifests/`, `.muzzle/logs/`, `.muzzle/reports/`, and `.muzzle/state/`. Treat `logs`, `reports`, `state`, and `.kujo_cache/` as generated/local output.

## Workflow Authoring

Place scripts under `.muzzle/workflows/`. Supported runners:

- `kujo`: `.kujo`, default runner, executed with the Kujo runtime.
- `bash`: `.sh`, executed with `bash`.
- `python`: `.py`, executed with `python3`.
- `node`: `.js`, executed with `node`.

Runner resolution is CLI `--runner` override, then manifest `runner`, then script extension, then Kujo default.

For Bash workflows:

```bash
#!/usr/bin/env bash
set -euo pipefail

target="${1:-staging}"
echo "Running check for ${target}"
```

For Kujo workflows, keep output concise and deterministic:

```kujo
print("Starting build check...")
print("Build check complete.")
```

## Manifest Pattern

Add `.muzzle/manifests/<name>.json` when agents or humans need argument docs, safety metadata, or explicit runner/script mapping:

```json
{
  "name": "build-check",
  "summary": "Run the project build and tests.",
  "runner": "bash",
  "script": "workflows/build-check.sh",
  "args": [
    {"name": "target", "required": false, "description": "Optional build target."}
  ],
  "quiet_by_default": true,
  "safety": {
    "require_git_repo": true,
    "allow_dirty_tree": true,
    "requires_network": false,
    "human_approval_recommended": false
  }
}
```

Mark `human_approval_recommended: true` for deploys, publishing, destructive cleanup, production writes, credential use, or broad networked operations.

## Output Contracts

- Default output should stay compact: status, exit code, duration, report path, log path.
- `--json` should emit one machine-readable object on stdout and keep other chatter away from stdout.
- Full stdout/stderr belongs in `.muzzle/logs/`; Markdown and JSON reports belong in `.muzzle/reports/`.
- Non-zero workflow exits should propagate as failure.
- Preserve CLI text, exit behavior, JSON field names/types, report paths, and log paths unless the task explicitly changes a contract.

## Loop Mode

Use loop mode for repeated agent iterations:

```bash
muzzle loop start release-hardening --limit 10
muzzle loop next
muzzle loop done --note "Fixed README commands against CLI help"
muzzle loop status
muzzle loop summary
```

Only one loop is active per project; loop state persists under `.muzzle/state/loops/`.

## Safety

- Muzzle is a local workflow runner, not a sandbox.
- Scripts outside `.muzzle/workflows/` are rejected.
- Workflow names reject `/`, `\`, `..`, empty names, and names longer than 128 characters.
- Muzzle shell-quotes workflow arguments, but workflow scripts must still avoid `eval` and validate inputs.
- Secret redaction applies to summaries/error excerpts, not full logs or `--verbose` terminal output.
- Never print secrets; keep `.muzzle/logs/` and `.muzzle/reports/` out of version control.
- Use `--timeout <ms>` for long or risky workflows; default is 300000ms, max is 3600000ms.
- Muzzle itself does not network, commit, push, or modify git config; workflow scripts may do those things.

## Muzzle Repo Work

- Read in this order: `README.md`, `docs/agent-usage.md`, `docs/howto.md`, `docs/workflows.md`, `docs/security.md`, `muzzle.kujo`, `src/*.kujo`, `tests/muzzle_wrapper_regression.sh`.
- Use `rg` with exclusions for broad searches: `-g '!/.dogfood/**' -g '!/.muzzle/**' -g '!/.kujo_cache/**'`.
- Treat `.dogfood/` as historical unless the task explicitly targets it.
- Preserve agent-friendly examples and exact-output checks.
- For CLI behavior changes, run `bash tests/muzzle_wrapper_regression.sh` and add/update focused contract checks. The regression script is intentionally invoked through `bash`; it is not executable in the repository checkout.

## Sources Consulted

- Status: repo-backed: `README.md`, `AGENTS.md`, `docs/agent-usage.md`, `docs/howto.md`, `docs/workflows.md`, `docs/security.md`.
- Status: repo-backed: `src/runner.kujo`, `src/workflow.kujo`, `src/report.kujo`, `src/redact.kujo`, `src/loops.kujo`, `tests/muzzle_wrapper_regression.sh`.
