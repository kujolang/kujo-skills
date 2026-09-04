---
name: videoops-generation-handoff
description: "Use when writing exact generation requests for unresolved custom media."
---

# VideoOps generation handoff

## Purpose

Use this skill for writing exact generation requests for unresolved custom media. Primary sources are GENERATE requirement, shot context, style plan, brand, and adjacent shots.

## Workflow

Specify purpose, aspect/crop, duration, motion direction, negative space, palette, prohibited motifs, delivery format, variants, and acceptance; preserve requirement/shot IDs.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not generate the media or request unrelated filler. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
