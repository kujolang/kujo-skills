---
name: webops-information-architecture
description: "Use when auditing site navigation, hierarchy, taxonomy, URLs, depth, clusters, and discoverability."
---

# Webops Information Architecture

## Purpose

Use this skill for auditing site navigation, hierarchy, taxonomy, URLs, depth, clusters, and discoverability. Its primary sources are ContentGraph, SiteProbe graph/depth, Lens navigation evidence, and source structure.

## Workflow

1. Map navigation, hierarchy, categories, tags, breadcrumbs, URL patterns, and content clusters.
2. Identify orphaning, excessive depth, weak connections, duplicate taxonomy, and user-journey gaps.
3. Separate crawl graph from rendered navigation.
4. Propose incremental architecture changes with URL migration implications.

## Required Output

- IA map.
- discoverability findings.
- taxonomy/URL risks.
- sequenced proposals.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not redesign taxonomy from graph metrics alone or change URLs without redirect planning. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
