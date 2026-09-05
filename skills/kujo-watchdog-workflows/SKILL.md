---
name: kujo-watchdog-workflows
description: "Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, `/api/sources`, `/telemetry/v2/batches`, OTLP ingestion/export, SQLite telemetry, auth modes, redaction, rate limits, connected sources, dashboard assets, benchmark scripts, AI Chat/Agents SDK integration, or `watchdog` source/docs changes."
---

# Kujo Watchdog Workflows

Use Watchdog as the local observability layer and OpenAI-compatible proxy for Kujo AI apps, capturing model/tool telemetry, proxy lifecycle traces, session-scoped agent steps, native producer batches, guarded OTLP traces, token/cost estimates, named upstream usage, connected-source metadata, backup status, and rate-limit/auth audit events into SQLite while exposing dashboard/API views.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
WATCHDOG_REPO="${WATCHDOG_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/watchdog}"
cd "${WATCHDOG_REPO}"
export KUJO_BIN="${KUJO_BIN:-kujo}"
"$KUJO_BIN" run --interpreter dashboard_server.kujo
# dashboard: http://localhost:7700
curl -s http://localhost:7700/api/proxy-config
```

## Workflow Notes

- Root `dashboard_server.kujo`, `dashboard.html`, `watchdog.kujo`, and `watchdog_shared.kujo` are compatibility mirrors of `src/` surfaces.
- Proxy smoke may intentionally produce upstream `401` without an API key while still recording telemetry.
- Named upstream profiles live in `watchdog_proxy_config.json` and are selected with `X-Watchdog-Upstream-Profile`; unknown profile names fail before upstream egress.
- A single Watchdog server can proxy several provider accounts through named upstream profiles, including AI Chat's shared OpenRouter and Ollama lanes; per-request profile metadata is preserved for filtering and telemetry.
- Connected Sources live in private `watchdog_sources.json` metadata plus accepted telemetry evidence. `/api/sources` reports observed/registered native producers, guarded OTLP producers, and proxy profiles without contacting external providers.
- `/telemetry/v2/batches` accepts canonical Watchdog producer batches; `/telemetry/v2/otlp/v1/traces` accepts guarded OTLP/HTTP JSON or Protobuf traces. Both remain subject to auth, size, rate, and privacy controls.
- Proxy streaming should forward chunks incrementally while recording truthful first-output timing and terminal status; do not buffer a stream merely to simplify telemetry unless the task explicitly changes that contract.
- Export workers are optional and fail-open relative to proxy success. Exporter profiles keep credentials in environment variables, cap batch size and queue storage, and dead-letter only bounded metadata.
- Keep `WDG_API_AUTH_TOKEN`, `WDG_PROXY_AUTHZ_TOKEN`, and upstream provider keys as separate credentials. Production profile startup requires token-protected API and proxy posture.
- `WDG_RATE_LIMIT_MODE=basic` uses SQLite-backed buckets for both `/api/*` and `/proxy/*`; redaction defaults to basic before persistence/export.
- Cost fields are estimated direct-provider equivalents, not invoices. Pricing provenance comes from the checked-in provider and OpenRouter catalogs; refresh and bounded repricing are script-driven.
- Backups are dashboard-visible runtime state. Active backup files and archived history are intentionally separate views; deleting a backup removes the file while preserving the historical record.
- Dashboard ranges, trace/session drilldowns, and copied detail blocks are UI contracts covered by frontend/API regression tests.
- Telemetry DBs, backup folders, benchmark outputs, and dashboard runtime data are local artifacts.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo Watchdog Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `src/dashboard_server.kujo`
3. `src/watchdog.kujo`
4. `src/watchdog_shared.kujo`
5. `dashboard_server.kujo`
6. `dashboard.html`
7. `demo.kujo`
8. `docs/CONNECTED_SOURCES.md`, `docs/GRANULAR_TRACING.md`, and OTLP/export docs when source or telemetry surfaces change
9. `scripts/`
10. `tests/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
export KUJO_BIN="${KUJO_BIN:-kujo}"
"$KUJO_BIN" run --interpreter dashboard_server.kujo
# in another shell, run endpoint smoke checks from README or scripts when available
node tests/benchmark_script_schema_check.js
node scripts/benchmark_profiles.js --fixture --profiles=quick,soak --json-out=tmp/benchmark-fixture.json
node tests/proxy_integration_stub_suite.js
node tests/rate_limit_controls_check.js
node tests/backup_api_check.js
node tests/frontend_contract_suite.js
node tests/watchdog_api_route_suite.js
node tests/telemetry_v2_api_suite.js
node tests/connected_sources_management_suite.js
node tests/connected_sources_frontend_contract_check.js
node tests/proxy_stream_timing_suite.js
node tests/proxy_stream_disconnect_suite.js
node scripts/refresh_openrouter_pricing_catalog.js
```

For the full JavaScript regression suite, export `KUJO_BIN` to the Kujo language
runtime first; the tests intentionally fail fast when they would otherwise pick
up no runtime or an unrelated `kujo` executable:

```bash
export KUJO_BIN=/path/to/kujo/target/release/kujo
for f in tests/*.js; do node "$f" || exit 1; done
```

## Search And Safety

- Do not log or commit real API keys, bearer tokens, prompts with secrets, or telemetry DBs.
- Keep redaction policy and auth mode docs aligned with implementation.
- Keep connected source registration metadata secret-free and revision-protected; source verification checks accepted local telemetry, not remote health.
- Keep OTLP/producer intake content-free by default and reject generic traces, logs, metrics, malformed wire data, and over-limit decompression.
- Prefer loopback-local startup for local validation.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `src/dashboard_server.kujo`.
- Status: repo-backed: `src/watchdog.kujo`.
- Status: repo-backed: `demo.kujo`.
- Status: repo-backed: `docs/PRICING_ESTIMATES.md`, `docs/CONNECTED_SOURCES.md`, `docs/GRANULAR_TRACING.md`, `tests/proxy_integration_stub_suite.js`, `tests/watchdog_api_route_suite.js`, `tests/telemetry_v2_api_suite.js`, `tests/connected_sources_management_suite.js`, `tests/connected_sources_frontend_contract_check.js`.
