---
name: kujo-cms-workflows
description: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery routes, auth boundaries, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes."
---

# Kujo CMS Workflows

Use CMS as the server-first Kujo showcase for content models, public delivery routes, auth-gated writes, webhooks, jobs, tenants, workspaces, and operational gates.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
CMS_REPO="${CMS_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/cms}"
cd "${CMS_REPO}"
cp .env.example .env
/path/to/kujo/target/debug/kujo run --interpreter backend/runtime/main.kujo
# default API: http://127.0.0.1:4200
```

## Workflow Notes

- The canonical runtime entrypoint is `backend/runtime/main.kujo`; there is no standalone CLI wrapper.
- Public discovery routes, auth-gated write routes, and operational scripts are part of the showcase surface.
- Webhook/background-job scripts may mutate local queues; inspect env and paths first.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo CMS Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `backend/runtime/main.kujo`
3. `backend/config/config.kujo`
4. `backend/core/`
5. `backend/modules/`
6. `tests/cms_contract_tests.kujo`
7. `scripts/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
/path/to/kujo/target/debug/kujo test-run tests/cms_contract_tests.kujo
CMS_GATE_RUN_PERF=false KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/run-release-gate.sh
KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/smoke-api.sh
KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/verify-compat-startup.sh
```

## Search And Safety

- Default to loopback-local binds unless the user explicitly needs another host.
- Do not commit local `.env`, database, backup, result, or runtime artifacts.
- Keep API contract tests and docs aligned when routes or schemas change.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `tests/cms_contract_tests.kujo`.
- Status: repo-backed: `backend/runtime/main.kujo`.
