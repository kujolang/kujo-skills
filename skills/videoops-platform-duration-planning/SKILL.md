---
name: videoops-platform-duration-planning
description: "Use when enforcing project video dimensions, FPS, and duration."
---

# VideoOps platform duration planning

## Purpose

Use this skill for enforcing project video dimensions, FPS, and duration. Primary sources are intake/platform.json and current project requirements.

## Workflow

Validate dimensions, aspect ratio, FPS, target/max duration, caption and audio intent; calculate frame totals; reject incompatible timing; record platform assumptions that require current verification.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not hard-code mutable social-platform limits outside the project contract. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
