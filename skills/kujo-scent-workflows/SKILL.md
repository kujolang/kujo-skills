---
name: kujo-scent-workflows
description: "Use this skill when creating, previewing, reviewing, or maintaining Scent context packs for agent handoff: `scent pack`, `--dry-run`, `--json`, `--budget`, `--target`, `--include`, `--exclude`, `--changed`, `--staged`, `--unstaged`, `.scent/` or generated pack artifacts, `context.md`, `context.json`, `manifest.json`, `files.json`, `redactions.json`, and Scent CLI/source/test changes."
---

# Kujo Scent Workflows

Use Scent to package local task context into structured, reviewable Markdown and JSON artifacts with provenance, bounded selection, and redaction metadata.

## Agent Workflow

- Run Scent from inside the repository being packed; it discovers the repo root from the current working directory.
- Start with `pack --dry-run --json` to estimate size, included files, and warnings before writing artifacts.
- Prefer an explicit `--task` that names the work the downstream agent should do, not a vague repo summary.
- Use `--changed`, `--staged`, or `--unstaged` when the handoff should focus on current working-tree changes.
- Use repeated `--include <path>` for important task areas and `--exclude <path>` for irrelevant generated, vendor, build, cache, or bulk data.
- Tune `--budget`, `--max-files`, and `--max-file-bytes` before broadening scope manually.
- Review `redactions.json` and the redaction section of `context.md` before sharing a pack.
- Treat generated packs as sensitive local artifacts; do not commit them unless the task explicitly concerns artifact fixtures or output contracts.

## Command Patterns

Build Kujo once if the release binary is missing:

```bash
cd /path/to/kujo
cargo build --release
```

Preview a pack without writing artifacts:

```bash
cd /path/to/target-repo
/path/to/kujo/target/release/kujo run /path/to/scent/scent.kujo pack \
  --task "review security posture" \
  --dry-run \
  --json
```

Write Markdown and JSON artifacts:

```bash
/path/to/kujo/target/release/kujo run /path/to/scent/scent.kujo pack \
  --task "implement auth fixes and validate tests" \
  --out /private/tmp/scent-pack \
  --format both
```

Focus on current changes and task-relevant directories:

```bash
/path/to/kujo/target/release/kujo run /path/to/scent/scent.kujo pack \
  --task "review workflow cues and risks" \
  --out /private/tmp/scent-pack \
  --changed \
  --staged \
  --unstaged \
  --include docs \
  --include src \
  --include tests \
  --max-files 20 \
  --max-file-bytes 20000 \
  --format both \
  --json
```

## CLI Contract

```text
scent pack --task <text>
  [--out <path>]
  [--budget <n>]
  [--target codex|claude|deepseek|generic]
  [--include <path>]
  [--exclude <path>]
  [--changed] [--staged] [--unstaged]
  [--max-files <n>]
  [--max-file-bytes <n>]
  [--format md|json|both]
  [--verbose]
  [--json]
  [--dry-run]
```

- `help`, `--help`, `pack --help`, `version`, and `--version` should stay clean and user-facing.
- `--target` selects the downstream model target (`codex`, `claude`, `deepseek`, or `generic`); it does not select a repo path.
- `--format md`, `json`, or `both` controls written context artifacts, while `--json` controls machine-readable stdout.
- `pack --dry-run` reports context estimates and should not write pack artifacts.
- Generated artifacts are `context.md`, `context.json`, `manifest.json`, `files.json`, `redactions.json`, and `metadata.json`.

## Output Review

- Inspect `context.md` for the human-readable task handoff.
- Inspect `context.json` when another tool or agent needs structured fields for task, target, budget, estimated tokens, repo metadata, instructions, selected files, changed files, redactions, excluded files, artifacts, and git metadata.
- Inspect `manifest.json` for include/truncate/exclude decisions and generated artifact records.
- Inspect `files.json` for candidate inventory, scoring, selected status, and changed/staged/unstaged markers.
- Inspect `redactions.json` as the authoritative per-pack redaction audit.
- Inspect `metadata.json` for run-level provenance.

## Safety

- Treat Scent redaction as best-effort and pattern-based, not a guarantee that no sensitive data remains.
- Keep generated pack directories such as `.scent/`, `out/`, and temporary pack paths out of version control unless deliberately testing artifact shape.
- Exclude generated or bulk paths from broad scans unless the task explicitly targets them; Scent already avoids `.git/`, `target/`, `.scent/`, and `out/` in normal selection.
- Avoid shell interpolation with task text in wrapper scripts; pass arguments as argument arrays or quote deliberately.

## Scent Repo Work

- Read in this order: `README.md`, `docs/scent.md`, `SECURITY.md`, `CONTRIBUTING.md`, then `scent.kujo`.
- Treat `README.md` as the canonical copyable example surface and `docs/scent.md` as the reference contract.
- Preserve deterministic selection, bounded traversal, explicit budget decisions, and redaction-first output behavior.
- Prefer small local helpers already present in `scent.kujo` before adding ad hoc output formatting or command-building code.
- Keep user-facing CLI flag, artifact, JSON field, and exit behavior changes reflected in `README.md` and `docs/scent.md`.
- For broad searches in the Scent repo, exclude generated and bulk paths:

```bash
rg --files -g '!target/**' -g '!out/**' -g '!.scent/**' -g '!.git/**'
```

Run focused validation for Scent changes:

```bash
cd /path/to/scent
/path/to/kujo/target/release/kujo run scent.kujo help
/path/to/kujo/target/release/kujo run scent.kujo version
/path/to/kujo/target/release/kujo run scent.kujo --version
/path/to/kujo/target/release/kujo check scent.kujo
/path/to/kujo/target/release/kujo run scent.kujo pack --task "smoke" --dry-run --json
```

## Sources Consulted

- Status: repo-backed: Scent `README.md`, `docs/scent.md`, `SECURITY.md`, `CONTRIBUTING.md`.
- Status: repo-backed: `scent.kujo` command surface, artifact contract, redaction pipeline, and inline smoke checks.
