---
name: kujo-changebucket-workflows
description: "Use this skill when measuring, reviewing, enforcing, or maintaining ChangeBucket git change footprint reports: `changebucket`, `analyze`, `--base`, `--range`, `--repo`, `--json`, `--markdown`, `--budget`, file categories, risk levels, churn metrics, footprint budgets, read-only diff inspection, or `changebucket` source/test changes."
---

# Kujo ChangeBucket Workflows

Use ChangeBucket to measure change size, file categories, churn, and budget risk. It is read-only and reports footprint, not semantic correctness.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
CHANGEBUCKET_REPO="${CHANGEBUCKET_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/changebucket}"
cd "${CHANGEBUCKET_REPO}"
KUJO=/path/to/kujo/target/release/kujo ./bin/changebucket --help
./bin/changebucket analyze
./bin/changebucket analyze --json
./bin/changebucket analyze --markdown --output changebucket-report.md
```

## Workflow Notes

- ChangeBucket reads git state only; it should not mutate the target repository.
- Use JSON output for downstream tools and Markdown for human handoff reports.
- Budget failures are policy signals; explain which budget was exceeded.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo ChangeBucket Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `changebucket.kujo`
4. `src/cli.kujo`
5. `src/analyze.kujo`
6. `src/classify.kujo`
7. `src/budget.kujo`
8. `src/render.kujo`
9. `tests/changebucket_test.kujo`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
KUJO=/path/to/kujo/target/release/kujo ./bin/changebucket --help
KUJO=/path/to/kujo/target/release/kujo ./bin/changebucket analyze --json
kujo run tests/changebucket_test.kujo
```

## Search And Safety

- Keep the tool read-only; do not add operations that modify target repos.
- Distinguish counts/categories from correctness judgments.
- Preserve exit code behavior for budget enforcement and usage errors.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `changebucket.kujo`.
- Status: repo-backed: `tests/changebucket_test.kujo`.
