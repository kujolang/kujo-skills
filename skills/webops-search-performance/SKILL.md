---
name: webops-search-performance
description: "Use when analyzing longitudinal measured search performance."
---

# Webops Search Performance

## Purpose

Use this skill for analyzing longitudinal measured search performance. Its primary sources are SearchBridge search.performance result/v1 and prior comparable windows.

## Workflow

1. Validate provider, property, date range, dimensions, and freshness.
2. Compare impressions, clicks, CTR, position, query/page movement, and incomplete-data metadata.
3. Control for incompatible dimensions and periods.
4. Label correlation and uncertainty; connect content evidence only when identifiers match.

## Required Output

- period comparison.
- query/page movement.
- measured anomalies.
- unavailable dimensions.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Never invent measurements or treat average position as a fixed rank. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
