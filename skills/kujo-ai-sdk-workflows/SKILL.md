---
name: kujo-ai-sdk-workflows
description: "Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, provider presets, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, telemetry bridge examples, benchmark quality gates, release gates, or `ai-sdk` source/docs changes."
---

# Kujo AI SDK Workflows

Use AI SDK for provider-gated SDK primitives that normalize OpenAI-compatible chat and embeddings behavior across offline fixtures and configured live providers.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
AI_SDK_REPO="${AI_SDK_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/ai-sdk}"
cd "${AI_SDK_REPO}"
export KUJO_BIN="${KUJO_BIN:-/path/to/kujo/target/debug/kujo}"
./kujo run examples/main.kujo
# fixture mode is used automatically when provider keys are absent
```

## Workflow Notes

- Fixture mode must remain deterministic and safe without provider secrets.
- Live provider smoke is opt-in and may skip when no provider key is configured.
- Response contracts, API contract policy, and tests must move together.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo AI SDK Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `src/ai_sdk.kujo`
3. `src/providers.kujo`
4. `docs/API_CONTRACT_POLICY.md`
5. `examples/`
6. `scripts/`
7. `tests/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
export KUJO_BIN="${KUJO_BIN:-/path/to/kujo/target/debug/kujo}"
"$KUJO_BIN" test-run tests/sdk_contract_tests.kujo
"$KUJO_BIN" test-run tests/security_redaction_tests.kujo
./kujo run examples/telemetry_bridge.kujo --interpreter
bash scripts/release_quality_gates.sh
bash scripts/supply_chain_policy_check.sh
```

## Search And Safety

- Do not require network or secrets for default local validation.
- Redact provider keys and sensitive headers in examples, logs, and generated artifacts.
- Document breaking response-contract changes and update contract tests.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `src/ai_sdk.kujo`.
- Status: repo-backed: `src/providers.kujo`.
- Status: repo-backed: `tests/sdk_contract_tests.kujo`.
