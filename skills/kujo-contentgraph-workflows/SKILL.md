---
name: kujo-contentgraph-workflows
description: "Use when building, inspecting, comparing, exporting, or consuming deterministic ContentGraph artifacts."
---

# Kujo Contentgraph Workflows

## Purpose

Use this skill for building, inspecting, comparing, exporting, or consuming deterministic ContentGraph artifacts. Its primary sources are `../contentgraph` README, methodology, schemas, tests, and security contract.

## Workflow

1. Select validated SiteProbe, local source, and optional SearchBridge inputs.
2. Run `contentgraph build` with explicit node/output/report budgets and reviewed thresholds.
3. Inspect clusters, orphans, overlaps, related pages, and link opportunities as candidates.
4. Use `compare` for longitudinal graph changes and `export` for downstream systems.

## Required Output

- contentgraph graph/v1.
- nodes/edges.
- clusters/overlaps/orphans.
- link opportunities.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Lexical similarity is not semantic truth, cannibalization proof, or permission to mutate content. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
