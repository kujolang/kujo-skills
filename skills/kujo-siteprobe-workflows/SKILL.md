---
name: kujo-siteprobe-workflows
description: "Use when running, validating, verifying, comparing, reporting, or integrating SiteProbe website-intelligence crawls, signed `.siteprobe` artifacts, deterministic baselines, or SiteProbe source/tests."
---

# Kujo Siteprobe Workflows

## Purpose

Use this skill for running, validating, verifying, comparing, reporting, or integrating SiteProbe website-intelligence crawls, signed `.siteprobe` artifacts, deterministic baselines, or SiteProbe source/tests. Its primary sources are `../siteprobe` README, CLI, schemas, tests, and security contract.

## Workflow

1. Run `./siteprobe doctor` and select a bounded same-origin public target, or pass `--allow-private-network` only for an authorized internal target.
2. Use `./siteprobe crawl <url> --max-pages N --max-depth N --max-output-bytes N --max-report-tokens N --out <run>`; preserve robots compliance by default.
3. Use `--deterministic`, `--baseline <run>`, and `--fail-on info|warning|error` for CI comparisons; output directories are immutable and published atomically.
4. Run `./siteprobe verify <run>` for manifest/signature checks when evidence was transferred or signed, then `./siteprobe validate <run>` before consuming artifacts.
5. Use `inspect`, `compare`, `report`, `links`, or `sitemap` for the narrow downstream need.

## Required Output

- validated SiteProbe run.
- pages/links/redirects/metadata/structured-data/sitemap/robots/findings artifacts.
- comparison evidence.
- digest manifest and optional HMAC signature verification result when used.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

SiteProbe is not Lens, Scout, a JS renderer, SEO advisor, security scanner, form submitter, or cross-origin crawler. It is GET-only and same-origin by default, blocks private address ranges unless explicitly authorized, DNS-pins connections, and re-checks redirect hops. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Run `bash scripts/validate.sh`, the 10,000-page benchmark, and generated-doc checks for SiteProbe source or contract changes. Validate source artifacts with their owning tool before interpretation. Run the current repository's WebOps cross-reference validation when agent, skill, tool, capability, or workflow mappings change.
