---
name: webops-keyword-opportunity
description: "Use when finding query opportunities while separating measurement, estimates, and public research."
---

# Webops Keyword Opportunity

## Purpose

Use this skill for finding query opportunities while separating measurement, estimates, and public research. Its primary sources are SearchBridge search/keyword results, public research, and ContentGraph coverage.

## Workflow

1. Classify each input as measured, third-party estimate, or public observation.
2. Associate queries with existing pages and topic clusters.
3. Score opportunity from evidence quality, relevance, coverage gap, and business fit rather than volume alone.
4. Report missing provider families explicitly.

## Required Output

- opportunity candidates.
- evidence class.
- coverage relationship.
- confidence.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not present keyword estimates as measured site demand or guarantee rankings. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
