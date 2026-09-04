---
name: videoops-asset-manifest-maintenance
description: "Use when maintaining schema-valid asset records and shot mappings."
---

# VideoOps asset manifest maintenance

## Purpose

Use this skill for maintaining schema-valid asset records and shot mappings. Primary sources are asset requirements, filesystem evidence, and asset-manifest schema.

## Workflow

Reconcile one record per requirement; validate status, origin, usage, rights, path, and used_by mappings; reject missing files and contradictory states; write deterministic ordering.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not mark an absent or rights-unclear asset approved. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
