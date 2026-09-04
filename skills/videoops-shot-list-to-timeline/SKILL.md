---
name: videoops-shot-list-to-timeline
description: "Use when mapping schema-valid shots into frame-accurate HyperFrames scenes."
---

# VideoOps shot list to timeline

## Purpose

Use this skill for mapping schema-valid shots into frame-accurate HyperFrames scenes. Primary sources are shot list, FPS, transcript, asset manifest, and current HyperFrames API.

## Workflow

Convert seconds to frames deterministically; map each shot and asset; preserve semantic timing; document frame-level adjustments; validate full duration and transition seams.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not materially restructure the concept or silently alter copy. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
