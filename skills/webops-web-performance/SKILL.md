---
name: webops-web-performance
description: "Use when analyzing lab and field website performance as distinct evidence classes."
---

# Webops Web Performance

## Purpose

Use this skill for analyzing lab and field website performance as distinct evidence classes. Its primary sources are SearchBridge PageSpeed/CrUX, Lens environment-relative metrics, and prior runs.

## Workflow

1. Label each metric lab, field, or local environment-relative.
2. Validate device/form factor, URL/origin, collection period, and comparable configuration.
3. Compare distributions/percentiles separately from lab audits.
4. Connect regressions to changes only when evidence supports the relationship.

## Required Output

- lab results.
- field results.
- comparison.
- bounded hypotheses.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not merge lab and field values or infer causation from timing alone. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
