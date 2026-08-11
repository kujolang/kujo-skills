---
name: webops-accessibility-review
description: "Use when running repeatable automated accessibility review with explicit manual gaps."
---

# Webops Accessibility Review

## Purpose

Use this skill for running repeatable automated accessibility review with explicit manual gaps. Its primary sources are Lens accessibility artifacts, rendered routes, and applicable manual review.

## Workflow

1. Define representative routes, states, and viewports.
2. Run deterministic automated checks and inspect evidence.
3. Group repeated root causes without hiding affected instances.
4. Name required manual keyboard, screen-reader, cognition, motion, and content checks.

## Required Output

- automated findings.
- affected routes/components.
- repair priorities.
- manual-review gaps.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Automation cannot certify full WCAG conformance. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
