---
name: webops-indexation
description: "Use when auditing crawlability, local indexability, and confirmed provider index state."
---

# Webops Indexation

## Purpose

Use this skill for auditing crawlability, local indexability, and confirmed provider index state. Its primary sources are SiteProbe robots/sitemap/page artifacts and optional SearchBridge URL inspection.

## Workflow

1. Classify crawl access, response, canonical, robots, noindex, and sitemap membership.
2. Label local conclusions `appears indexable` or `appears not indexable`.
3. Add `confirmed indexed/not indexed` only from current provider evidence.
4. Track conflicts and follow-up verification separately from submission.

## Required Output

- local indexability matrix.
- confirmed index evidence.
- conflicts.
- coverage gaps.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not infer indexed from HTTP 200, sitemap presence, or canonical alone. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
