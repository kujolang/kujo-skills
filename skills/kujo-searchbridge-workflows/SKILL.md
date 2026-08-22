---
name: kujo-searchbridge-workflows
description: "Use when running SearchBridge doctor, capability preflight, fixture providers, normalized evidence reads, batch reads, evidence-query, signed adapters, replay/cache, OpenTelemetry, or explicit ACT submission."
---

# Kujo Searchbridge Workflows

## Purpose

Use this skill for running SearchBridge doctor, capability preflight, fixture providers, normalized evidence reads, batch reads, evidence-query, signed adapters, replay/cache, OpenTelemetry, or explicit ACT submission. Its primary sources are `../searchbridge` README, provider research, schemas, tests, and security contract.

## Workflow

1. For SearchBridge `0.3.0`, use the prepared Kujo `v1.0.2` runtime at commit `3bc5b4f1634d9883a789a0c2a0e6a266f72b77b2` until the release is published and checksum-verified.
2. Run `./searchbridge doctor`, `capabilities --deterministic`, and `providers` without credentials.
3. Use `--fixture --offline --deterministic` for deterministic GSC, GA4, PageSpeed, CrUX, Bing, Ahrefs, IndexNow, and batch coverage.
4. For live reads, supply short-lived environment credentials and explicit `--page-size`, `--max-pages`, `--max-total-rows`, timeout, retry, and output budgets; use `--format jsonl` for large GSC/GA4 exports.
5. Use `batch --commands pagespeed,crux` only for read operations; mutation commands cannot enter batch.
6. Use `evidence-query --evidence-path <jsonl>` for bounded JSONL filters and joins without loading full evidence into memory.
7. For external adapters, require detached signatures plus exact capability, endpoint, and credential allowlists.
8. For submission require the operator's `index.submission` capability and ACT authority plus `submit --capability index.submission --act --yes`; retain the receipt.

## Required Output

- normalized result/v1 evidence.
- capability matrix.
- ACT submission receipt.
- batch partial-success records, replay/cache records, or OTLP file output when explicitly requested.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

SearchBridge fetches evidence and never invents interpretation; a received submission is not proof of indexing. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation. Cache
and replay files contain provider evidence; keep them access-controlled and out
of releases. OpenTelemetry is opt-in and must exclude URLs, headers, tokens,
bodies, and rows.

## Verification

Run `bash scripts/validate.sh`, `./searchbridge search-performance --fixture --offline --deterministic`, the benchmark script, and `examples/ci_quality_gate.kujo` for SearchBridge changes. Validate source artifacts with their owning tool before interpretation. Run the current repository's WebOps cross-reference validation when agent, skill, tool, capability, or workflow mappings change.
