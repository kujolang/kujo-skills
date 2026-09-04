---
name: videoops-generated-asset-manifesting
description: "Use when registering generated assets with complete provenance and shot mapping."
---

# VideoOps generated asset manifesting

## Purpose

Use this skill for registering generated assets with complete provenance and shot mapping. Primary sources are generated files, provider receipt, generation purpose, and asset schema.

## Workflow

Record origin, provider/tool class, prompt artifact reference, generated time, path, metadata, selected variant, usage status, requirement, and shots; verify file existence and schema.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Never invent cost, token usage, provider identity, or approval. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
