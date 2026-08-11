---
name: webops-content-decay
description: "Use when identifying content deterioration or staleness without conflating age and decline."
---

# Webops Content Decay

## Purpose

Use this skill for identifying content deterioration or staleness without conflating age and decline. Its primary sources are SearchBridge longitudinal results, ContentGraph, factual sources, analytics, and history.

## Workflow

1. Validate comparable search/analytics windows and content identity.
2. Evaluate measured movement separately from factual age, source change, and structural signals.
3. Classify measurement, inference, and unknowns.
4. Recommend refresh only when evidence names what should change and why.

## Required Output

- decay candidates.
- measured/inferred evidence.
- confidence.
- refresh rationale.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Without provider data, do not claim measured decline; old content is not automatically stale. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
