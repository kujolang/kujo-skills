---
name: webops-internal-linking
description: "Use when analyzing, proposing, or explicitly applying contextual internal links."
---

# Webops Internal Linking

## Purpose

Use this skill for analyzing, proposing, or explicitly applying contextual internal links. Its primary sources are ContentGraph opportunities, page context, SiteProbe links, optional repository.

## Workflow

1. Validate source/target relevance and user journey in context.
2. Reject redundant, forced, or count-driven opportunities.
3. Propose natural anchor intent and exact source location.
4. Apply only under role-bounded ACT, then run Eval, SiteProbe, and Lens as applicable.

## Required Output

- reviewed link proposals.
- source/target context.
- optional patch.
- post-change proof.

Every output must name target/scope, evidence class, retrieval or run time,
unavailable checks, permission mode, and comparison baseline where applicable.

## Boundaries

Do not force exact-match anchors or mutate content under OBSERVE/PROPOSE. Preserve OBSERVE/PROPOSE/ACT boundaries, provider cost and credential
limits, stable finding identity, and the distinction among finding,
recommendation, action, and outcome. Never store credentials or fabricate
provider data, rankings, indexing, citations, compliance, or causation.

## Verification

Validate source artifacts with their owning tool before interpretation. Run
the current repository's WebOps cross-reference validation when agent, skill,
tool, capability, or workflow mappings change.
