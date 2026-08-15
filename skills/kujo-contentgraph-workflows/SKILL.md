---
name: kujo-contentgraph-workflows
description: "Use when building, inspecting, comparing, explaining, analyzing, exporting, or consuming deterministic ContentGraph artifacts, incremental graph caches, link-opportunity reports, GraphML/SARIF exports, or ContentGraph source/tests."
---

# Kujo Contentgraph Workflows

## Purpose

Use this skill for building, inspecting, comparing, explaining, analyzing, exporting, or consuming deterministic ContentGraph artifacts, incremental graph caches, link-opportunity reports, GraphML/SARIF exports, or ContentGraph source/tests. Its primary sources are `../contentgraph` README, methodology, schemas, tests, and security contract.

## Workflow

1. Select validated SiteProbe, sitemap, CSV, CMS, local source, and optional SearchBridge inputs.
2. Run `./contentgraph doctor`, then `build` with explicit node, input, candidate-pair, analysis, output, and report budgets.
3. Use `--config` for repeatable settings, `--deterministic` for byte-comparable runs, `--incremental-from <run>` for cache reuse, and `--tokenizer-profile unicode-lexical/v1` when mixed-script corpora require it.
4. Inspect `clusters`, `orphans`, `overlaps`, `related`, `analysis`, `explain`, and `link-opportunities` as review queues.
5. Use `compare` for longitudinal graph changes and `export --format json|graphml|sarif` for downstream systems; existing output files require `--force`.

## Required Output

- contentgraph graph/v1.
- nodes/edges.
- clusters/overlaps/orphans.
- link opportunities.
- analysis, manifest, vector-cache, adapter-cache, and optional telemetry artifacts when generated.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Lexical similarity is not semantic truth, cannibalization proof, or permission to mutate content. Candidate pairs can still grow quadratically for dense corpora; keep the explicit pair ceiling and document-frequency filter in view. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Run `bash scripts/validate.sh`, `./contentgraph-benchmark --nodes 1000`, and `kujo run scripts/build-demo.kujo` for ContentGraph source or contract changes. Validate source artifacts with their owning tool before interpretation. Run the current repository's WebOps cross-reference validation when agent, skill, tool, capability, or workflow mappings change.
