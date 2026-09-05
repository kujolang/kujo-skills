---
name: kujo-searchbridge-workflows
description: "Use this skill when running, validating, installing, or maintaining SearchBridge 1.x: doctor, capability preflight, provider tiers, fixture/live evidence reads, batch reads, evidence-query, signed adapters, replay/cache, SDK bundles, OpenTelemetry, MCP surfaces, or explicit ACT submission."
---

# Kujo SearchBridge Workflows

## Purpose

Use this skill for SearchBridge 1.x workflows. SearchBridge collects normalized search, analytics, performance, backlink, SERP, and indexing evidence while preserving provenance; it does not interpret SEO outcomes.

## Workflow

1. Prefer checksum-verified SearchBridge `1.0.0` release bundles for installed use. Source-checkout development uses the pinned Kujo `v1.2.3` runtime recorded in `../searchbridge/README.md`.
2. Run `./searchbridge doctor`, `./searchbridge capabilities --deterministic`, `./searchbridge providers`, and `./searchbridge agent-catalog` without credentials before live work.
3. Treat provider tiers literally: `stable-live` is automatic-live eligible; `fixture-only`, `external-reference`, and `disabled` are not stable live coverage.
4. Use `--fixture --offline --deterministic` for deterministic GSC, GA4, PageSpeed, CrUX, Cloudflare, IndexNow, Bing Webmaster, Ahrefs, DataForSEO, SerpApi, external adapter, replay/cache, batch, SDK, and MCP coverage.
5. For live reads, supply short-lived environment credentials and explicit `--page-size`, `--max-pages`, `--max-total-rows`, `--max-calls`, `--max-provider-units`, timeout, retry, response-byte, and output budgets; use `--format jsonl` for large GSC/GA4 exports.
6. Use `batch` only for read operations. It may overlap reads up to `--max-concurrency`, preserves ordering, observes `--cancel-file`, and reports `searchbridge.batch/v1` partial-success records. Mutation commands cannot enter batch.
7. Use `evidence-query --evidence-path <jsonl>` for bounded JSONL filters and joins; use spill joins only with explicit temp-dir, row, and disk budgets.
8. For external adapters, require detached signatures plus exact capability, endpoint, credential, compatibility, and deprecation policy checks.
9. For submission require the operator's `index.submission` capability and ACT authority plus `submit --capability index.submission --act --yes`; retain the receipt. A received submission is not proof of indexing.

## Required Output

- normalized `searchbridge.result/v1` evidence.
- capability matrix.
- ACT `searchbridge.submission/v1` receipt.
- batch partial-success records, replay/cache records, SDK/generated type artifacts, MCP records, or OTLP file output when explicitly requested.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

SearchBridge fetches evidence and never invents interpretation. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable support tiers, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation. Cache
and replay files contain provider evidence; keep them access-controlled and out
of releases. OpenTelemetry is opt-in and must exclude URLs, headers, tokens,
bodies, and rows.

## Verification

Run `bash scripts/validate.sh`, `bash scripts/version_consistency_gate.sh`, `bash scripts/release_candidate_gate.sh`, `./searchbridge search-performance --fixture --offline --deterministic`, and `examples/ci_quality_gate.kujo` for SearchBridge changes. Validate source artifacts with their owning tool before interpretation. Run the current repository's WebOps cross-reference validation when agent, skill, tool, capability, or workflow mappings change.

## Sources Consulted

- Status: repo-backed: `../searchbridge/README.md`.
- Status: repo-backed: `../searchbridge/docs/release-qualification-1.0.0.md`, `docs/security-assessment-1.0.0.md`, `docs/providers-and-capabilities.md`, `docs/routing-and-cost.md`, `docs/runtime-bundles.md`, `docs/sdk.md`.
- Status: repo-backed: `../searchbridge/tests/searchbridge_tests.kujo`, `scripts/validate.sh`, `scripts/version_consistency_gate.sh`, `scripts/release_candidate_gate.sh`.
