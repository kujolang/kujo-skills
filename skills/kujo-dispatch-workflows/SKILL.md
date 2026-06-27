---
name: kujo-dispatch-workflows
description: "Use this skill when running, inspecting, extending, or maintaining Dispatch reliable AI workflow orchestration: `dispatch.kujo`, `kujo run dispatch.kujo`, `demo`, `resume`, `templates`, `runs`, `show`, `inspect`, `doctor`, `cleanup`, `export-run`, `import-run`, workflow templates, declarative workflow files, plugins, approval gates, trace/report/state artifacts, tool policy profiles, bundle signing, offline fixture runs, SDK bridge integration, or Dispatch CLI/tests/source changes."
---

# Kujo Dispatch Workflows

Use Dispatch as a control-layer workflow engine for repeatable AI orchestration: route structured work through workflow templates, persist run state, emit trace/report artifacts, and make approval, policy, retry, and handoff behavior auditable.

## Agent Workflow

- Read `README.md` first, then `AGENTS.md`. For release, deployment, extension, or backlog work, read the specific doc named in the request.
- Prefer safe local fixture runs first. Dispatch defaults to `DISPATCH_OFFLINE_FIXTURE=true`, so normal demo/test paths do not need provider credentials.
- Run commands from the Dispatch repo root so relative paths, output roots, fixtures, and bridge scripts resolve consistently.
- Use the VM path `kujo run dispatch.kujo ...` for Dispatch CLI commands unless a task explicitly targets interpreter fallback or parity.
- Treat `outputs/`, `tests/tmp/`, `target/`, and `.ci/` as generated or bulk output unless the task explicitly targets them.
- Preserve CLI text, exit behavior, JSON envelope keys, artifact paths, and exact output contracts unless the request intentionally changes them.

## Quick Commands

```bash
cd /path/to/dispatch

kujo run dispatch.kujo demo "How do AI workflows improve reliability?" --yes --non-interactive
kujo run dispatch.kujo demo "Repo review" --workflow-file examples/workflows/custom-review.json --input-json '{"repo":"kujo"}' --plugin sample --yes --non-interactive
kujo run dispatch.kujo templates --json
kujo run dispatch.kujo runs --json --diagnostics
kujo run dispatch.kujo inspect <run-id> --json
kujo run dispatch.kujo resume <run-id> --yes --non-interactive
```

Use `--output-root tests/tmp/<purpose>` for local validation that should not pollute normal `outputs/`.

## Command Surface

- `demo "topic"` starts a template-backed workflow. Use `--workflow research-report` or `--workflow crud-reliability` to select a built-in template, or `--workflow-file <json>` plus `--input-json '{...}'` for a declarative workflow spec and structured run input.
- `--plugin sample` exercises the built-in plugin injection path; use `src/core/plugins.kujo` and `src/plugins/builtin_plugins.kujo` for extension work.
- `resume <run-id>` continues a persisted run, commonly after an approval pause.
- `templates [--json]` lists available workflow templates and summary metadata.
- `runs [--json] [--diagnostics]` lists and filters the run catalog by status, workflow, topic, tags, issues, limit, and offset.
- `show <run-id>` prints a compact run summary; `inspect <run-id>` prints artifacts and contract metadata.
- `doctor [--json]` diagnoses run state/catalog health; `doctor --write` persists repairs.
- `cleanup` defaults to dry-run. Add `--apply` only when deletion is requested and the scope is clear.
- `export-run` and `import-run` move run bundles. Use `--sign-bundle`/`--verify-bundle-signature` with `DISPATCH_BUNDLE_SIGNING_KEY` or `--signing-key`.
- `--webhook-sink <path.jsonl>` writes lifecycle events to a guarded local JSONL sink, `--webhook-url <https-url>` best-effort posts events, and `--cancel-after-step <step-id>` requests cooperative cancellation.

When strict mutation mode is enabled, `doctor --write`, `cleanup --apply`, and `import-run` require `--confirm-mutation` or `DISPATCH_MUTATION_CONFIRM=true`.

## Artifacts

Each run writes to `<output-root>/<run-id>/`:

- `state.json`: full run state snapshot.
- `trace.json`: structured execution trace.
- `trace.md`: human-readable trace timeline.
- `report.md`: human-readable report when report generation completes.
- `report.json`: machine-readable report payload when report generation completes.
- `dispatch-mutations.jsonl`: audit log for repairs, cleanup, imports, and policy-denied tool attempts.
- `.dispatch-run-index.json`: run catalog index under the output root.

Machine-readable state, trace, and report artifacts include contract metadata such as `artifact_contract_version`, `schema_name`, and `schema_version`. Dispatch redacts sensitive field names such as `api_key`, `token`, `authorization`, `secret`, and `password` before persistence.

## Policy And Safety

- Policy sources resolve through profile, config, environment, then explicit CLI allow/deny controls; CLI flags have final precedence.
- Built-in profiles: `development`/`dev` is open, `staging` denies `flaky_reliability_tool`, and `production`/`prod` allows the known safe fixture/report tools while denying the flaky reliability tool.
- Use `--allow-tools` and `--deny-tools` for focused policy tests, especially when changing `src/core/tool_policy.kujo`.
- Default `--sources-dir`, `--output-root`, and `--config` handling is intentionally constrained. Only set `DISPATCH_ALLOW_ANY_SOURCES_DIR`, `DISPATCH_ALLOW_ANY_OUTPUT_ROOT`, or `DISPATCH_ALLOW_ANY_CONFIG_PATH` for explicit local validation.
- Use `DISPATCH_SDK_DEBUG_OUTPUT=true` only for local bridge debugging because it exposes raw bridge stdout/stderr in parse-error details.

## Repo Work

- CLI entrypoint and routing: `dispatch.kujo`.
- Argument parser: `src/cli/cli_args.kujo`.
- Workflow templates and template listing: `src/workflows/workflow.kujo`.
- Orchestration engine: `src/core/runner.kujo`.
- Agent handlers: `src/agents/agent.kujo`.
- Tool registry and payload adapters: `src/tools/tool.kujo`, plus `tools/source_lookup.kujo`, `tools/content_processing.kujo`, and `tools/reliability_tools.kujo`.
- Run persistence/catalog/doctor/cleanup/bundles: `src/core/state.kujo`.
- Approval, retry, handoff, hooks, report, trace, policy, and plugin behavior: matching modules under `src/core/`.
- External SDK bridge: `sdk_adapter.kujo` and `bridge_chat.kujo`.

For broad searches, exclude generated paths:

```bash
rg "pattern" -g '!target/**' -g '!outputs/**' -g '!tests/tmp/**' -g '!**/.git/**'
```

## Extension Patterns

- Add workflow templates in `src/workflows/workflow.kujo`; update `create_workflow_templates`, template ordering, `templates` output expectations, README examples, and tests.
- Add declarative workflow loading behavior in `src/workflows/loader.kujo` and keep `demo --workflow-file` examples and tests aligned.
- Add tools through `src/tools/tool.kujo` with payload adapters instead of runner-specific branching; place domain handlers in `tools/*.kujo` when they are reusable.
- Register external tool/agent injection through `src/core/plugins.kujo` rather than editing core orchestration for project-specific behavior.
- Keep approval, retry, cancellation, timeout, handoff, report, and trace changes covered by focused tests and artifact contract checks.
- Prefer copyable README examples over test-only examples when changing user-facing behavior.

## Validation

For a basic local fixture smoke:

```bash
export DISPATCH_OFFLINE_FIXTURE=true
kujo run dispatch.kujo demo "Dispatch smoke" --yes --non-interactive --output-root tests/tmp/dispatch-smoke
kujo run dispatch.kujo runs --output-root tests/tmp/dispatch-smoke --json --diagnostics
kujo run tests/benchmarks/run_throughput.kujo 10
```

For repo test coverage:

```bash
kujo test-run tests/sdk_adapter_tests.kujo -v
kujo test-run tests/policy_precedence_tests.kujo -v
kujo test-run tests/dispatch_tests.kujo -v
```

When using a locally built Kujo binary:

```bash
export KUJO_BIN=/path/to/kujo/target/debug/kujo
$KUJO_BIN test-run tests/sdk_adapter_tests.kujo -v
$KUJO_BIN test-run tests/policy_precedence_tests.kujo -v
$KUJO_BIN test-run tests/dispatch_tests.kujo -v
```

## Troubleshooting

- If live SDK integration fails, set `AI_SDK_PATH` to a local checkout containing `ai_sdk.kujo` and `providers.kujo`.
- If child bridge execution fails, verify `KUJO_BIN` and `DISPATCH_SDK_BRIDGE_SCRIPT`.
- If fixture source validation fails, use the default `examples/research-report/sources` or explicitly opt in with `DISPATCH_ALLOW_ANY_SOURCES_DIR=true`.
- If Kujo emits undefined-function warnings but the command exits successfully and artifacts are correct, treat exit status and functional output as authoritative.

## Sources Consulted

- Status: repo-backed: `README.md`, `AGENTS.md`.
- Status: repo-backed: `dispatch.kujo`, `src/cli/cli_args.kujo`, `src/workflows/workflow.kujo`, `src/workflows/loader.kujo`, `src/plugins/builtin_plugins.kujo`, `tests/dispatch_tests.kujo`, `docs/benchmarks.md`.
