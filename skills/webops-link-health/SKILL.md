---
name: webops-link-health
description: "Use when auditing broken, redirected, malformed, or unexpected links."
---

# Webops Link Health

## Purpose

Use this skill for auditing broken, redirected, malformed, or unexpected links. Its primary sources are SiteProbe link/status/redirect evidence and optional Lens interactions.

## Workflow

1. Validate crawl coverage and response timestamps.
2. Separate internal breakage, outbound observation, redirect chains, malformed URLs, and unexpected destinations.
3. Recheck transient external failures conservatively.
4. Propose exact source/target repairs and verify under authorized ACT.

## Required Output

- link inventory findings.
- redirect chains.
- transient/confirmed labels.
- repair brief.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not crawl cross-origin sites broadly or equate one timeout with permanent failure. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
