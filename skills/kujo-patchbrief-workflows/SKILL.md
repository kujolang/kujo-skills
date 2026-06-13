---
name: kujo-patchbrief-workflows
description: "Use this skill when generating, consuming, validating, or maintaining PatchBrief structured git-diff briefs: `patchbrief.kujo`, `summarize`, `suggest-tests`, `handoff`, `--format json`, `--pretty`, implementation handoffs, reviewer notes, changed-file risk summaries, PatchBrief CLI/tests/source changes, or PatchBrief dogfood workflows."
---

# Kujo PatchBrief Workflows

Use PatchBrief to inspect the current repository's uncommitted git diff and produce compact implementation summaries, suggested validation steps, or handoff notes for reviewers and downstream agents.

## Agent Workflow

- Run PatchBrief from inside a git repository with a dirty or clean working tree.
- Always pass PatchBrief arguments after Kujo's `--` separator.
- Prefer Markdown for human-readable summaries and handoffs.
- Prefer JSON with `--pretty` when another tool or agent will parse the result.
- Start with `summarize`, then run `suggest-tests` before review, handoff, or commit decisions.
- Use `handoff` when a reviewer, maintainer, or another agent needs a structured continuation note.
- Treat PatchBrief output as heuristic guidance. Verify suggested tests and risk areas against the actual diff before acting on them.

## Command Patterns

Use `KUJO_BIN` when the environment provides it; otherwise assume `kujo` is on PATH:

```bash
KUJO="${KUJO_BIN:-kujo}"

"$KUJO" run patchbrief.kujo -- summarize
"$KUJO" run patchbrief.kujo -- summarize --format json --pretty
"$KUJO" run patchbrief.kujo -- suggest-tests
"$KUJO" run patchbrief.kujo -- handoff
"$KUJO" run patchbrief.kujo -- handoff --format json --pretty
"$KUJO" run patchbrief.kujo -- help
"$KUJO" run patchbrief.kujo -- version
```

`help` and `version` are commands. Do not use `--help` or `--version` as standalone aliases; leading flags trigger command-order guidance.

## Output Selection

- `summarize`: Use for a quick implementation brief of current git changes. Markdown includes repo, branch, changed-file stats, likely purpose, file details, risk areas, and recent commits.
- `summarize --format json`: Use for machine-readable summaries. Expect fields such as `repo`, `branch`, `summary`, `files`, `risk_areas`, and `recent_commits`.
- `suggest-tests`: Use to derive candidate validation commands from changed file extensions, plus general and manual checks.
- `handoff`: Use before handing work to a reviewer or another agent. Markdown includes a summary, changed files, risk assessment, recent commits, reviewer checklist, and next-agent commands.
- `handoff --format json`: Use for structured handoff automation. Expect `format: "patchbrief-handoff"`, version metadata, summary stats, files, risks, recent commits, and reviewer checklist.

When there are no uncommitted changes, PatchBrief should say so cleanly instead of inventing work. Outside a git repository, it should exit non-zero; JSON modes should emit a JSON error payload.

## Repo Work

- Read in this order before changing PatchBrief behavior: `README.md`, `patchbrief.kujo`, `src/common.kujo`, `src/git.kujo`, `src/summarize.kujo`, `src/suggest_tests.kujo`, `src/handoff.kujo`, `tests/patchbrief_tests.kujo`, `patchbrief.spec.yml`.
- Treat `README.md` and the static help text in `patchbrief.kujo` as canonical copyable examples.
- Treat `tests/patchbrief_tests.kujo` as CLI contract coverage, especially for exact help output, JSON validity, non-repo behavior, command ordering, and invalid formats.
- Preserve byte-stable help text, command syntax, Markdown section names, JSON field names/types, and exit behavior unless the task explicitly changes the CLI contract.
- Use shared helpers in `src/common.kujo` before adding repeated output-printing code.
- Keep the MVP rule-based; do not add network calls, Git hosting APIs, persistent state, or LLM summarization unless the task explicitly expands scope.
- Use broad searches with generated or bulk paths excluded:

```bash
rg --files -g '!.git/**' -g '!kennel_packages/**' -g '!dist/**' -g '!build/**' -g '!node_modules/**' -g '!.dogfood/**'
```

## Validation

Run focused command checks after behavior changes:

```bash
KUJO="${KUJO_BIN:-kujo}"

"$KUJO" run patchbrief.kujo -- help
"$KUJO" run patchbrief.kujo -- summarize
"$KUJO" run patchbrief.kujo -- summarize --format json --pretty
"$KUJO" run patchbrief.kujo -- suggest-tests
"$KUJO" run patchbrief.kujo -- handoff --format json --pretty
"$KUJO" test
```

Add or update tests before changing user-facing help text, command syntax, JSON shape, Markdown headings, non-repo errors, or command-order diagnostics.

## Sources Consulted

- Status: repo-backed: `README.md`, `patchbrief.spec.yml`.
- Status: repo-backed: `patchbrief.kujo`, `src/summarize.kujo`, `src/suggest_tests.kujo`, `src/handoff.kujo`, `tests/patchbrief_tests.kujo`.
