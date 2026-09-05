---
name: kujo-ai-sdk-workflows
description: "Use this skill when building, testing, integrating, or maintaining Kujo AI SDK provider primitives: OpenAI-compatible chat/embeddings contracts, native provider drivers, provider presets, model catalogs, fixture mode, streaming callbacks, retries/backoff, redaction, live provider smoke tests, Watchdog telemetry bridge examples, benchmark quality gates, release gates, provider package contracts, or `ai-sdk` source/docs changes."
---

# Kujo AI SDK Workflows

Use AI SDK for provider-gated SDK primitives that normalize chat and embeddings behavior across offline fixtures, configured live OpenAI-compatible providers, and validated native provider drivers.

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
- Live provider smoke may skip during ordinary local runs when no provider key is configured, but release/prerelease validation requires at least one configured provider secret unless a manual workflow explicitly allows the skip.
- Response contracts, API contract policy, and tests must move together. Streaming requests set `stream_options.include_usage`, and normalized usage accepts both `prompt_tokens`/`completion_tokens` and `input_tokens`/`output_tokens`.
- Native provider packages attach a validated `ai-sdk-provider-driver` 1.0.0 function bundle. Drivers encode bounded request descriptors and decode provider-native responses; they never perform network I/O or select transport.
- `src/model_catalog.kujo` owns provider-owned model metadata for deterministic routing. Persist catalog ID, version, hash, provider, model, preference class, and source; do not fabricate prices, token limits, or measurements.
- Keep endpoint allowlists, protected-header policy, structured-output schema validation, response-size limits, fallback providers, benchmark thresholds, and provider capability metadata aligned with README and tests.
- Use SDK-owned `resolve_model_preference(provider, preference)` when callers need provider-neutral model intent. Provider presets own class-to-model mappings; downstream orchestration should persist the returned `provider`, `model`, `preference_class`, and `source` instead of duplicating routing tables.
- Watchdog telemetry mapping is metadata-only. Provider-reported cost stays provider-reported; do not convert estimates into billed cost.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo AI SDK Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `src/ai_sdk.kujo`
3. `src/providers.kujo`
4. `src/driver.kujo`, `src/openai_compatible_driver.kujo`, and provider-driver tests when native package behavior changes
5. `src/model_catalog.kujo`, `examples/model_preferences.kujo`, and `scripts/generate_model_catalog.kujo` when model routing changes
6. `docs/API_CONTRACT_POLICY.md`, `docs/KUJO_PROVIDER_PACKAGE_CONTRACT_V1.md`, `docs/PROVIDER_EXTENSION_GUIDE.md`, and `docs/TELEMETRY_INTEROPERABILITY.md`
7. Other `examples/`
8. `scripts/`
9. `tests/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
export KUJO_BIN="${KUJO_BIN:-/path/to/kujo/target/debug/kujo}"
"$KUJO_BIN" test-run tests/sdk_contract_tests.kujo
"$KUJO_BIN" run examples/model_preferences.kujo
"$KUJO_BIN" run scripts/generate_model_catalog.kujo --interpreter -- examples/dispatch-model-catalog.config.json --output dispatch-model-catalog.json
"$KUJO_BIN" test-run tests/sdk_contract_resilience_tests.kujo
"$KUJO_BIN" test-run tests/sdk_contract_embeddings_tests.kujo
"$KUJO_BIN" test-run tests/security_redaction_tests.kujo
"$KUJO_BIN" test-run tests/reliability_failure_modes_tests.kujo
"$KUJO_BIN" test-run tests/parser_fuzz_smoke_tests.kujo
"$KUJO_BIN" test-run tests/provider_driver_contract_tests.kujo
"$KUJO_BIN" test-run tests/provider_driver_security_tests.kujo
"$KUJO_BIN" test-run tests/model_catalog_tests.kujo
"$KUJO_BIN" test-run tests/watchdog_telemetry_contract_tests.kujo
"$KUJO_BIN" test-run tests/feature_smoke_tests.kujo
"$KUJO_BIN" test-run tests/bugfix_regression_tests.kujo
"$KUJO_BIN" test-run tests/hardening_regression_tests.kujo
python3 tests/wrapper_regression_tests.py
./kujo run examples/telemetry_bridge.kujo --interpreter
"$KUJO_BIN" run scripts/benchmark_quality_gate.kujo
bash scripts/release_quality_gates.sh
bash scripts/verify_docs.sh
bash scripts/supply_chain_policy_check.sh
```

## Search And Safety

- Do not require network or secrets for default local validation.
- Redact provider keys and sensitive headers in examples, logs, and generated artifacts.
- Do not let custom request headers override protected `Authorization` or `Content-Type` unless `allow_unsafe_header_override` is explicitly set; CR/LF-bearing custom headers are dropped.
- Keep structured-output requests provider-capability aware: fail fast with `unsupported_feature` when JSON mode is requested against a provider that does not advertise support.
- Treat driver packages as trusted executable dependencies to pin, review, and test. Core owns transport, retries, governance, endpoint policy, response-size checks, redaction, and normalized contracts.
- Thrown injected transports must normalize to terminal `transport_error` without leaking credentials. Buffered streaming callbacks do not prove incremental network delivery or redirect-hop bounds.
- Document breaking response-contract changes and update contract tests.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `src/ai_sdk.kujo`, `src/providers.kujo`, `src/model_catalog.kujo`, `src/driver.kujo`, `src/openai_compatible_driver.kujo`, `src/watchdog_telemetry.kujo`.
- Status: repo-backed: `docs/API_CONTRACT_POLICY.md`, `docs/KUJO_PROVIDER_PACKAGE_CONTRACT_V1.md`, `docs/PROVIDER_EXTENSION_GUIDE.md`, `docs/TELEMETRY_INTEROPERABILITY.md`, `docs/audits/repository-hardening.md`.
- Status: repo-backed: `tests/sdk_contract_tests.kujo`, `tests/provider_driver_contract_tests.kujo`, `tests/provider_driver_security_tests.kujo`, `tests/model_catalog_tests.kujo`, `tests/watchdog_telemetry_contract_tests.kujo`, `scripts/release_quality_gates.sh`.
