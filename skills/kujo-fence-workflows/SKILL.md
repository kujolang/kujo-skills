---
name: kujo-fence-workflows
description: "Use this skill when initializing, checking, explaining, graphing, validating, adopting, or maintaining Fence architecture-boundary enforcement: `fence.kujo`, `fence.toml`, `init`, `check`, `explain`, `graph`, `baseline create`, `validate`, `doctor`, templates, exit codes, boundary violations, import classification, or `fence` source/test changes."
---

# Kujo Fence Workflows

Use Fence to prevent architecture-boundary crossings in local repositories through deterministic config-driven import and dependency checks.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
FENCE_REPO="${FENCE_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/fence}"
cd "${FENCE_REPO}"
kujo run fence.kujo -- init
kujo run fence.kujo -- check
kujo run fence.kujo -- explain src/ui/LoginForm.tsx
kujo run fence.kujo -- graph --format mermaid --output architecture.mmd
```

## Workflow Notes

- Run Fence from inside the target repo or pass the absolute `fence.kujo` path; scanning uses the current directory.
- `baseline create` supports gradual adoption for legacy violations; do not hide new violations in the baseline without review.
- Graph outputs and reports are generated artifacts; decide whether they belong in the repo before committing.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo Fence Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `docs/getting-started.md`
3. `docs/configuration.md`
4. `docs/architecture.md`
5. `fence.kujo`
6. `src/cli.kujo`
7. `src/rules.kujo`
8. `src/imports.kujo`
9. `src/zones.kujo`
10. `tests/fence_tests.kujo`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
kujo run fence.kujo -- validate
kujo run fence.kujo -- check
kujo run tests/fence_tests.kujo
```

## Search And Safety

- Treat exit `1` as boundary violations, not a tool crash.
- Preserve config templates and exit codes unless explicitly changing contracts.
- Avoid archived prompt surfaces as canonical examples.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `fence.kujo`.
- Status: repo-backed: `tests/fence_tests.kujo`.
