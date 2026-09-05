---
name: kujo-cms-workflows
description: "Use this skill when running, validating, extending, or maintaining the Kujo CMS server-first showcase: `backend/runtime/main.kujo`, content models, delivery/discovery routes, auth/admin/session boundaries, WebMCP, Abilities/API connectors, extension packages, SEO/content/media workflows, contract tests, startup compatibility, webhook/background jobs, migration safety, backup/restore, release gates, or `cms` source/docs changes."
---

# Kujo CMS Workflows

Use CMS as the server-first Kujo showcase for content models, public delivery/discovery routes, auth-gated writes, WebMCP, portable Abilities, connectors, extension packages, webhooks, jobs, tenants, workspaces, and operational gates.

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
- Public discovery routes, published-only anonymous reads, auth-gated write/admin routes, framework-neutral sessions, entry locks, revisions/rollback, webhook/background-job scripts, and operational scripts are part of the showcase surface.
- WebMCP is enabled by default through `/.well-known/kujo-webmcp.json`, `/assets/js/kujo-webmcp.js`, `/v1/webmcp/*`, and `/.well-known/kujo-site-index.json`. It exposes only same-origin read-only published content tools: `get_site_info`, `search_site`, `list_content`, and `get_content`.
- Portable theme/plugin package flows use bounded ZIP ingestion/upload, one canonical manifest, receipt-bound SHA-256 evidence, and managed storage. Package code is not executed during installation.
- CMS Abilities use strict `kujo.ability/v1` definitions, permission-scoped execution, request-bound one-time approvals for mutations, keyed idempotency, tenant-aware principals, and MCP-ready descriptors. Legacy `confirmed: true` is compatibility input only and grants no authority.
- Connector endpoints and provider credentials stay server-side. Browser and package descriptors must not receive secrets or endpoint values.
- `bash scripts/cms-seo.sh help`, `bash scripts/cms-content.sh help`, `bash scripts/cms-extensions.sh help`, and `bash scripts/cms-ai.sh help` expose API-equivalent terminal workflows.
- The documented release gate covers contract, smoke, startup compatibility, integration, security, and optional performance checks; default branch protection remains the known governance item before claiming enterprise-complete posture.
- Webhook/background-job scripts may mutate local queues; inspect env and paths first.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo CMS Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `backend/runtime/main.kujo`
3. `backend/config/config.kujo`
4. `backend/core/`
5. `backend/modules/`
6. `backend/routes/`
7. `docs/abilities.md`, `docs/extensions.md`, and `docs/webmcp.md` when agent, package, or browser-tool surfaces change
8. `tests/cms_contract_tests.kujo`
9. `scripts/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, auth, route, or example changes:

```bash
/path/to/kujo/target/debug/kujo test-run tests/cms_contract_tests.kujo
CMS_GATE_RUN_PERF=false KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/run-release-gate.sh
KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/smoke-api.sh
KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/verify-compat-startup.sh
KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/integration-enterprise-security.sh
KUJO_BIN=/path/to/kujo/target/debug/kujo bash scripts/integration-multitenant.sh
node scripts/test-webmcp-runtime.js
```

## Search And Safety

- Default to loopback-local binds unless the user explicitly needs another host.
- Do not commit local `.env`, database, backup, result, or runtime artifacts.
- Keep API contract tests and docs aligned when routes or schemas change.
- Keep WebMCP public-only/read-only and Ability mutation paths separate.
- Preserve production startup checks for trusted ingress limits, durable rate limiting, and bootstrap-token posture.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `tests/cms_contract_tests.kujo`.
- Status: repo-backed: `backend/runtime/main.kujo`.
- Status: repo-backed: `docs/abilities.md`, `docs/extensions.md`, `docs/webmcp.md`, `docs/ability-pack-certification-2026-09-02.md`, `docs/hardening-evaluation-2026-08-30.md`, `docs/release-gate-evidence-2026-07-10.md`, `docs/enterprise-production-readiness-plan.md`.
