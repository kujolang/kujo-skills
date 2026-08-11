---
name: webops-analytics-analysis
description: "Use when analyzing real website behavior from normalized analytics evidence."
---

# Webops Analytics Analysis

## Purpose

Use this skill for analyzing real website behavior from normalized analytics evidence. Its primary sources are SearchBridge analytics result/v1, property identity settings, dimensions, metrics, and prior window.

## Workflow

1. Validate property, identity/reporting settings, date range, dimensions, metrics, sampling/modeling metadata, and freshness.
2. Compare like-for-like periods and segment only when necessary.
3. Describe measured behavior separately from explanations.
4. Minimize sensitive dimensions in artifacts and handoffs.

## Required Output

- measured behavior summary.
- segment evidence.
- comparison.
- privacy/coverage caveats.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Without an analytics provider, stop measured analysis; crawl data is not analytics. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
