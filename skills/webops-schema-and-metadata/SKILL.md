---
name: webops-schema-and-metadata
description: "Use when auditing structured data and page/social metadata."
---

# Webops Schema And Metadata

## Purpose

Use this skill for auditing structured data and page/social metadata. Its primary sources are SiteProbe metadata/structured-data artifacts, visible content, and current authoritative guidance.

## Workflow

1. Validate titles, descriptions, canonicals, robots, Open Graph, social/article metadata, and JSON-LD syntax.
2. Check structured data relevance and consistency with visible content.
3. Identify duplicates, omissions, obsolete patterns, and conflicts.
4. Propose only source-supported values/types and verify after changes.

## Required Output

- metadata matrix.
- schema findings.
- duplicates/conflicts.
- repair brief.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not invent visible facts, keyword-stuff, or guarantee rich results. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
