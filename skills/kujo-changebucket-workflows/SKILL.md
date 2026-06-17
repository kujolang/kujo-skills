---
name: kujo-changebucket-workflows
description: "Use this skill when measuring or enforcing code-change footprint with ChangeBucket: `changebucket`, `changebucket check`, `--json`, `--markdown`, `--output`, `--base`, `--head`, `--repo`, budget flags, risk/blast-radius reports, file-category counts, generated markdown reports, or ChangeBucket CLI/tests/source changes."
---

# Kujo ChangeBucket Workflows

Use ChangeBucket to measure the size, shape, and blast-radius footprint of a git change. It reports counts and categories; it does not review correctness, summarize semantics, or record agent runs.

Canonical local source is usually `/Users/robertdevore/2026/Kujolang/kujo-repos/changebucket`. Do not confuse ChangeBucket with RunLedger or PatchBrief: RunLedger records agent-run receipts, PatchBrief explains what changed, and ChangeBucket measures footprint only.

## Agent Workflow

1. Verify the launcher and Kujo runtime:

```bash
changebucket --help
changebucket version
```

If the wrapper is not on `PATH`, run it from the repo with `KUJO=/path/to/kujo ./bin/changebucket ...`, or use `kujo run /path/to/changebucket/changebucket.kujo -- <args>`. Keep the `--` separator when invoking through `kujo run`.

2. Measure the current worktree by default:

```bash
changebucket
changebucket --json
changebucket --markdown
changebucket --output CHANGE_BUCKET.md
```

Default worktree mode compares against `HEAD` and includes untracked, non-ignored files. Use `--base main` to compare the worktree against another ref.

3. Use range mode for committed refs:

```bash
changebucket --base main --head HEAD
changebucket --repo /path/to/repo --base origin/main --head feature-branch
```

Providing `--head` switches to `base..head` mode and ignores the working tree and untracked files.

4. Enforce a budget with `check`:

```bash
changebucket check --max-files 20 --max-churn 800
changebucket check --max-files 20 --max-churn 800 \
  --no-deletes --no-dependency-changes --no-lockfile-changes
```

Budget flags on the default command are informational and still exit `0`. Put `check` before budget flags when the budget should fail the process.

## Output Contracts

- `changebucket [options]` prints a text, JSON, or markdown footprint report and exits `0` on successful analysis.
- `changebucket check [budget options]` exits `1` when the budget is exceeded.
- `--json` prints exactly one JSON object to stdout.
- `--output <file>` writes a markdown report and prints `Wrote report to <file>`.
- Non-git targets print `error: not a git repository: <path>` and exit `1`.
- Unknown commands exit `2`.

The JSON model is the internal contract between analysis and rendering: `{base, head, generated_at, summary, categories, budget, files}`. `categories` always includes `source`, `tests`, `docs`, `config`, `dependency_manifests`, `lockfiles`, `generated`, `ci`, `scripts`, and `other`, even when some arrays are empty.

## Interpreting Results

- Risk level is a blast-radius heuristic, not a quality score.
- `high`: more than 20 files, churn over 1000, any deletes, or generated files touched.
- `low`: at most 5 files, churn at most 200, no deletes, and no dependency, lockfile, CI, or generated changes.
- `medium`: everything else.
- A file can appear in multiple category lists, so category counts can overlap; `files_changed` is the unique file count.
- Single-line replacements count as both an addition and a deletion in git numstat.

Use ChangeBucket after agent edits when the user asks how large a change was, whether the edit stayed within an expected scope, whether dependencies/lockfiles/config/generated/CI files changed, or whether a PR needs a simple footprint gate.

## Maintaining ChangeBucket

Read in this order for repo work:

- `README.md`: user behavior, categories, risk, JSON shape.
- `AGENTS.md`: maintainer orientation and current status.
- `src/analyze.kujo`: model construction and risk heuristic.
- `src/diffsrc.kujo`: read-only git layer.
- `src/classify.kujo`: file-category rules.
- `src/cli.kujo`: parsing, dispatch, exit codes.
- `src/render.kujo`: text and markdown output contracts.
- `tests/changebucket_test.kujo`: behavior contracts.

Preserve exact CLI/report output unless intentionally updating integration expectations. Treat `examples/CHANGE_BUCKET.example.md` as generated output documentation; update it only when the markdown report contract changes.

Broad searches should exclude generated output unless the task targets report samples:

```bash
rg -n "pattern" -g '!examples/CHANGE_BUCKET.example.md'
```

Validate changes with:

```bash
for f in changebucket.kujo src/*.kujo tests/*.kujo; do $KUJO check "$f"; done
./tests/run.sh
$KUJO run changebucket.kujo -- --help
```

The test suite is filesystem-isolated, creates throwaway git repos under `$TMPDIR`, and needs no network or credentials.

## Safety Boundaries

- ChangeBucket itself is read-only over git: `git diff`, `git ls-files`, and `git rev-parse`.
- Never stage, commit, reset, checkout, clean, stash, or apply patches as part of measuring a footprint.
- Generated markdown reports are local artifacts unless the user explicitly wants them committed.
- Resist adding configurable category plugins or diff-file parsing unless real usage demands it; those are known future ideas, not current contracts.
