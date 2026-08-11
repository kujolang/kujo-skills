---
name: kujo-searchbridge-workflows
description: "Use when running SearchBridge doctor, capability preflight, fixture providers, normalized evidence reads, or explicit ACT submission."
---

# Kujo Searchbridge Workflows

## Purpose

Use this skill for running SearchBridge doctor, capability preflight, fixture providers, normalized evidence reads, or explicit ACT submission. Its primary sources are `../searchbridge` README, provider research, schemas, tests, and security contract.

## Workflow

1. Run `searchbridge doctor`, `capabilities`, and `providers` without credentials.
2. Use `--fixture` for deterministic GSC, GA4, PageSpeed, CrUX, Bing, Ahrefs, and IndexNow coverage.
3. For live reads, supply short-lived environment credentials and bounded dimensions/rows.
4. For submission require the operator's ACT authority plus `submit --act --yes`; retain the receipt.

## Required Output

- normalized result/v1 evidence.
- capability matrix.
- ACT submission receipt.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

SearchBridge fetches evidence and never invents interpretation; a received submission is not proof of indexing. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
