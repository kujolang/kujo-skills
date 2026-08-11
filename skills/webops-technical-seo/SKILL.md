---
name: webops-technical-seo
description: "Use when performing a deterministic technical SEO audit from crawl evidence."
---

# Webops Technical SEO

## Purpose

Use this skill for performing a deterministic technical SEO audit from crawl evidence. Its primary sources are SiteProbe artifacts, WebOps history, and optional Lens/inspection evidence.

## Workflow

1. Validate crawl coverage and robots/sitemap state.
2. Evaluate statuses, redirects, canonicals, indexability, metadata, structured data, and internal graph conditions.
3. Separate crawl-visible facts from rendered or provider-confirmed state.
4. Prioritize reproducible findings and delegate specialized interpretation.

## Required Output

- technical findings.
- affected URLs.
- severity/evidence.
- specialist handoffs.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not emulate a search engine, perform vulnerability scans, or claim local indexability means indexed. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
