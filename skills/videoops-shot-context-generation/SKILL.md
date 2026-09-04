---
name: videoops-shot-context-generation
description: "Use when generating media that fits its actual edit neighbors and timing."
---

# VideoOps shot context generation

## Purpose

Use this skill for generating media that fits its actual edit neighbors and timing. Primary sources are shot list, style plan, adjacent shots, and generation requirement.

## Workflow

Inspect entry/exit frames, visual intensity, motion direction, crop, overlays, and duration; formulate context-aware generation; validate transition compatibility.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not evaluate assets in isolation from the intended timeline. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
