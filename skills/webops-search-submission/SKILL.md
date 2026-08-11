---
name: webops-search-submission
description: "Use when preflighting or performing explicit ACT search submission through supported providers."
---

# Webops Search Submission

## Purpose

Use this skill for preflighting or performing explicit ACT search submission through supported providers. Its primary sources are SearchBridge providers/capabilities, site ownership, approved URL list, and receipt schema.

## Workflow

1. Verify provider support, ownership, URL host, quota/cost, and ACT authorization.
2. Preview the exact URL set and reject cross-host or unsupported Google Indexing API use.
3. Run SearchBridge submission with explicit confirmation.
4. Store receipt as received/accepted only and schedule independent index verification.

## Required Output

- preflight.
- approved URL set.
- submission receipt.
- future verification cue.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Never submit in OBSERVE/PROPOSE, bypass quotas, or claim guaranteed indexing. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
