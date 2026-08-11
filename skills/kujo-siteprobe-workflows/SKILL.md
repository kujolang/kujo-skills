---
name: kujo-siteprobe-workflows
description: "Use when running, validating, comparing, reporting, or integrating SiteProbe website-intelligence crawls and `.siteprobe` artifacts."
---

# Kujo Siteprobe Workflows

## Purpose

Use this skill for running, validating, comparing, reporting, or integrating SiteProbe website-intelligence crawls and `.siteprobe` artifacts. Its primary sources are `../siteprobe` README, CLI, schemas, tests, and security contract.

## Workflow

1. Run `siteprobe doctor` and select a bounded same-origin target.
2. Use `siteprobe crawl <url> --max-pages N --max-depth N --out <run>`; preserve robots compliance by default.
3. Run `siteprobe validate <run>` before consuming artifacts.
4. Use `compare`, `report`, `links`, or `sitemap` for the narrow downstream need.

## Required Output

- validated SiteProbe run.
- pages/links/findings artifacts.
- comparison evidence.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

SiteProbe is not Lens, Scout, a JS renderer, SEO advisor, security scanner, form submitter, or cross-origin crawler. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
