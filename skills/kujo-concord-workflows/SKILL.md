---
name: kujo-concord-workflows
description: "Use this skill when scanning, reporting, triaging, or maintaining Concord artifact-drift checks for Kujo ecosystem repositories: `concord scan`, `check`, `report`, `tasks`, `--format json`, `--output`, CLI/docs drift, Spec/Eval alignment, manifest/docs alignment, version consistency, example validity, source-of-truth findings, `.dogfood/concord/` outputs, or Concord CLI/source/test changes."
---

# Kujo Concord Workflows

Use Concord to detect whether a repository's code, CLI help, docs, examples, Spec files, Eval checks, manifests, package metadata, versions, and release artifacts still describe the same product. Treat findings as drift leads for human review, not proof of correctness.

## Quick Start

Default to the local Concord repo unless the user points to another checkout:

```bash
CONCORD_REPO="${CONCORD_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/concord}"
cd "$CONCORD_REPO"
./kujo run concord.kujo -- scan --dir /path/to/project
```

Use these common forms:

```bash
./kujo run concord.kujo -- scan --dir /path/to/project
./kujo run concord.kujo -- scan --dir /path/to/project --format json
./kujo run concord.kujo -- scan --dir /path/to/project --output concord-report.md
./kujo run concord.kujo -- check cli-docs --dir /path/to/project
./kujo run concord.kujo -- tasks --dir /path/to/project --output concord-tasks.md
```

If scanning the Concord repo itself, omit `--dir` from inside the repo.

## Scan Workflow

- Run `scan` for a full artifact drift report before changing docs, specs, evals, manifests, examples, or CLI contracts.
- Prefer `--format json` when another tool or follow-up script needs stable fields. The JSON report includes `findings` with `id`, `severity`, `confidence`, `category`, `title`, and `summary`.
- Use `--output <path>` for durable reports. Keep generated dogfood artifacts under `.dogfood/concord/` when working inside the Concord repo.
- Use `tasks` after a scan when the user wants actionable fix cards rather than the full report.
- Summarize findings by severity, category, likely source artifact, likely target artifact, and whether human review is required.
- For low-confidence findings, explain the uncertainty before editing source artifacts.

## Check Categories

- `cli-docs`: compare documented commands against CLI help output.
- `spec-eval`: compare Spec acceptance criteria against Eval checks.
- `manifest`: compare package metadata against README/docs.
- `versions`: compare version metadata across manifests, docs, badges, and changelogs.
- `examples`: verify example commands and referenced files.
- `source-of-truth`: identify authoritative artifact mappings and missing source-of-truth cues.
- `all`: run every category, equivalent to `scan`.

Use `check <category>` for focused verification while editing one artifact family. `check` exits `3` when findings exist, so treat exit `3` as a verification failure with useful output, not a tool crash.

## Exit Codes

- `0`: no drift, or only low-severity findings for `scan`.
- `1`: high-severity or critical drift found by `scan`.
- `2`: invalid arguments, missing target directory, or configuration error.
- `3`: `check` found findings and returned a category verification failure.

Do not collapse these into pass/fail without context. In final responses, state which command ran, the exit code, and the highest severity found.

## Fixing Drift

- Prefer updating the artifact that is least authoritative. If unsure, use `source-of-truth` findings and repository conventions to decide.
- Preserve copyable command examples. Concord is intended to help agents keep examples aligned with real commands.
- After edits, rerun the narrow `check <category>` first, then run full `scan` if the change touched multiple artifact families.
- Avoid treating Concord as a formatter or auto-fixer. It surfaces mismatches and task cards; the agent still chooses and applies the appropriate edit.

## Concord Repo Work

When modifying Concord itself, read in this order:

1. `README.md`
2. `concord.kujo`
3. `src/common.kujo`
4. `src/scanner.kujo`
5. Relevant `src/checks/*.kujo`
6. `src/reporter.kujo` or `src/fix_tasks.kujo` when output shape changes
7. `tests/concord_tests.kujo`

Preserve these contracts unless the user explicitly asks to change them:

- Commands: `scan`, `check <category>`, `report`, `tasks`, `version`, `help`, `--help`, `--version`.
- Options: `--dir <path>`, `--format markdown|json`, `--output <path>`.
- Categories: `cli-docs`, `spec-eval`, `manifest`, `versions`, `examples`, `source-of-truth`, `all`.
- Report headings: `# Concord Drift Report`, `## Summary`, `## Findings`.
- JSON findings fields: `id`, `severity`, `confidence`, `category`, `title`, `summary`.
- Exit behavior: `scan` returns `1` for high/critical drift, `check` returns `3` for any category findings.

Run validation after Concord code changes:

```bash
cd /Users/robertdevore/2026/Kujolang/kujo-repos/concord
./kujo test
./kujo run concord.kujo -- scan
./kujo run concord.kujo -- scan --format json
```

Use `rg` for broad searches and exclude generated dogfood output unless the task targets it:

```bash
rg "pattern" -g '!/.dogfood/**' -g '!/.kujo_cache/**'
```

## Continuous Loop

Use the loop runner only when the user asks for repeated dogfood scans, trend artifacts, or CI-style gate summaries:

```bash
scripts/concord_continuous_loop.sh --iterations 1
scripts/concord_continuous_loop.sh --iterations 0 --sleep-seconds 600
scripts/concord_continuous_loop.sh --iterations 1 --strict-gate
```

Loop artifacts belong under `.dogfood/concord/loop/`: per-run outputs, trend JSONL, latest summary, and upstream issue drafts.

## Sources Consulted

- Status: repo-backed: `README.md`, `concord.spec.yml`, `concord.kujo`, `tests/concord_tests.kujo`.
- Status: repo-backed: `src/common.kujo`, `src/scanner.kujo`, `src/checks/*.kujo`, `src/reporter.kujo`, `src/fix_tasks.kujo`.
