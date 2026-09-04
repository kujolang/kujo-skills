---
name: videoops-actionable-fix-writing
description: "Use when writing schema-valid timestamped repairs from validated defects."
---

# VideoOps actionable fix writing

## Purpose

Use this skill for writing schema-valid timestamped repairs from validated defects. Primary sources are critic evidence, fix-list schema, reviewed draft lineage, and role boundaries.

## Workflow

Assign stable IDs/severity; cite timestamp or frame range; state problem, impact, exact required change, and testable acceptance; initialize PENDING; order blockers first.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not write vague feedback such as make it cooler or silently implement fixes. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
