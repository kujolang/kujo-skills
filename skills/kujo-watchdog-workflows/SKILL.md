---
name: kujo-watchdog-workflows
description: "Use this skill when running, configuring, testing, integrating, or maintaining Watchdog local AI telemetry/proxy workflows: `dashboard_server.kujo`, `/proxy/v1`, `/api/requests`, `/api/proxy-config`, SQLite telemetry, auth modes, redaction, rate limits, dashboard assets, benchmark scripts, AI Chat integration, or `watchdog` source/docs changes."
---

# Kujo Watchdog Workflows

Use Watchdog as the local observability layer and OpenAI-compatible proxy for Kujo AI apps, capturing model/tool telemetry into SQLite and exposing dashboard/API views.

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
- Telemetry DBs, benchmark outputs, and dashboard runtime data are local artifacts.

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
8. `scripts/`
9. `tests/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
export KUJO_BIN="${KUJO_BIN:-kujo}"
"$KUJO_BIN" run --interpreter dashboard_server.kujo
# in another shell, run endpoint smoke checks from README or scripts when available
node tests/benchmark_script_schema_check.js
node scripts/benchmark_profiles.js --fixture --profiles=quick,soak --json-out=tmp/benchmark-fixture.json
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
- Prefer loopback-local startup for local validation.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `src/dashboard_server.kujo`.
- Status: repo-backed: `src/watchdog.kujo`.
- Status: repo-backed: `demo.kujo`.
