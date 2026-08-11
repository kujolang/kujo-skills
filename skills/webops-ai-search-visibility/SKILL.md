---
name: webops-ai-search-visibility
description: "Use when running repeatable AI/search visibility benchmark suites."
---

# Webops AI Search Visibility

## Purpose

Use this skill for running repeatable AI/search visibility benchmark suites. Its primary sources are Fixed query suite, configured surfaces, dated response evidence, and prior benchmark.

## Workflow

1. Freeze query text, locale, surface/model, configuration, and collection window.
2. Run only available surfaces and preserve exact availability.
3. Record observed mentions/citations with source evidence.
4. Compare like-for-like runs and flag surface/model changes.

## Required Output

- benchmark run.
- surface availability.
- observed citations/mentions.
- longitudinal comparison.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not fabricate citations, universalize one surface, or claim stable GEO certainty. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
