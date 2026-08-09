---
name: kujo-agents-sdk-workflows
description: "Use this skill when working on Kujo Agents SDK runtime primitives, examples, offline fixtures, agent runners, tools, approvals, handoffs, tracing, artifact/session/memory stores, retrieval providers, integration adapters, MCP 2026 helpers, budget limits, no-network harnesses, or `agents-sdk` source/test changes."
---

# Agents SDK Workflows

Use Agents SDK for library-first agent workflow primitives built on top of AI SDK. Treat bundled examples as the canonical copyable behavior and tests as contract coverage for deterministic offline agent runs and integration adapter boundaries.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
AGENTS_SDK_REPO="${AGENTS_SDK_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/agents-sdk}"
cd "${AGENTS_SDK_REPO}"
export KUJO_BIN="${KUJO_BIN:-/path/to/kujo/target/debug/kujo}"
"$KUJO_BIN" run examples/examples_smoke_runner.kujo --interpreter
"$KUJO_BIN" test
```

## Workflow Notes

- `examples/*_agent.kujo` are canonical runnable examples; `examples/examples_smoke_runner.kujo` is the offline aggregate smoke path.
- Offline fixture behavior and no-network boundaries are part of the public contract.
- Integration adapters live behind `src/agents/integrations/adapters.kujo`; MCP `2026-07-28` support is limited to stateless JSON-RPC request helpers, required per-request `_meta`, Streamable HTTP routing headers, tool-list cache metadata, input-required result normalization, unsupported-version errors, and lossless tool schema/display metadata mapping into registry contracts.
- Expected-output fixtures under `tests/*.out` are behavior contracts, not prose examples.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Agents SDK Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `docs/DEVELOPER_GUIDE.md`
4. `docs/EXAMPLES.md`
5. `src/`
6. `examples/`
7. `tests/`
8. `docs/INTEGRATION_BOUNDARIES.md` when adapter behavior changes

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
export KUJO_BIN="${KUJO_BIN:-/path/to/kujo/target/debug/kujo}"
"$KUJO_BIN" run examples/module_exports_smoke.kujo --interpreter
"$KUJO_BIN" run examples/examples_smoke_runner.kujo --interpreter
"$KUJO_BIN" test-run tests/run_basic_runner_tests.kujo -v
"$KUJO_BIN" test-run tests/integration_adapters_contract_tests.kujo -v
bash scripts/ci_no_network_enforcement.sh
```

## Search And Safety

- Preserve public result shapes and deterministic offline behavior.
- Do not refresh expected-output fixtures unless the matching behavior intentionally changed.
- Prefer targeted contract tests before the whole suite for narrow source changes.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `docs/INTEGRATION_BOUNDARIES.md`, `src/agents/integrations/adapters.kujo`.
- Status: repo-backed: `examples/examples_smoke_runner.kujo`.
- Status: repo-backed: `tests/run_basic_runner_tests.kujo`, `tests/integration_adapters_contract_tests.kujo`.
