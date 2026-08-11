---
name: webops-reporting
description: "Use when synthesizing validated specialist evidence into quiet WebOps reports."
---

# Webops Reporting

## Purpose

Use this skill for synthesizing validated specialist evidence into quiet WebOps reports. Its primary sources are Validated current/prior WebOps artifacts, finding history, actions, outcomes, and availability receipts.

## Workflow

1. Validate input runs and specialist ownership.
2. Lead with what improved, regressed, changed, requires action, can wait, and could not be checked.
3. Deduplicate persistent findings by stable ID and keep full evidence machine-readable.
4. Do not redo specialist analysis or convert recommendations into claimed actions.

## Required Output

- quiet human report.
- machine evidence references.
- attention queue.
- availability summary.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

A large pass count must not bury a few actionable findings. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
