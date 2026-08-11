---
name: webops-cannibalization
description: "Use when identifying likely intent competition while separating normal overlap."
---

# Webops Cannibalization

## Purpose

Use this skill for identifying likely intent competition while separating normal overlap. Its primary sources are ContentGraph overlaps plus SearchBridge query/page evidence.

## Workflow

1. Start with high lexical overlap candidates, not conclusions.
2. Compare intent, SERP/query associations, page purpose, canonical state, and longitudinal performance.
3. Classify normal overlap, supporting cluster, or likely cannibalization.
4. Recommend differentiation, merge, canonical, or no action with evidence.

## Required Output

- intent comparison.
- candidate classification.
- query/page evidence.
- bounded recommendation.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Shared terms alone do not prove cannibalization. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
