---
name: webops-longitudinal-findings
description: "Use when creating, comparing, or updating stable WebOps findings, recommendations, actions, outcomes, and recurring-run history."
---

# Webops Longitudinal Findings

## Purpose

Use this skill for creating, comparing, or updating stable WebOps findings, recommendations, actions, outcomes, and recurring-run history. Its primary sources are WebOps finding/history schemas and prior run artifacts.

## Workflow

1. Read the previous relevant run, unresolved findings, and actions.
2. Normalize agent/check, target, and issue identity into a deterministic ID.
3. Classify NEW, PERSISTENT, RESOLVED, REGRESSED, or REOPENED from evidence.
4. Store finding, recommendation, action, and outcome as separate records.

## Required Output

- finding records.
- state transitions.
- comparison summary.
- history update.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

A recommendation is not an action; an action does not prove causation. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
