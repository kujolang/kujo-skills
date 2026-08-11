---
name: webops-capability-preflight
description: "Use when checking which WebOps website, repository, browser, search, analytics, performance, backlink, keyword, publishing, distribution, or submission capabilities are available."
---

# Webops Capability Preflight

## Purpose

Use this skill for checking which WebOps website, repository, browser, search, analytics, performance, backlink, keyword, publishing, distribution, or submission capabilities are available. Its primary sources are WebOps capability schema plus tool doctor/capabilities outputs.

## Workflow

1. Load the site profile and requested agent contract.
2. Check required, recommended, and optional capabilities independently.
3. Record provider, evidence mode, missing environment reference, cost/write boundary, and degradation path.
4. Stop only when a required capability has no honest degraded mode.

## Required Output

- capability receipt.
- available/unavailable matrix.
- degraded execution decision.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Never repeatedly prompt for credentials or convert unavailable evidence into zero. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
