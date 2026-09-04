---
name: videoops-lens-product-capture
description: "Use when capturing first-party terminal, UI, site, or product evidence for a planned shot."
---

# VideoOps lens product capture

## Purpose

Use this skill for capturing first-party terminal, UI, site, or product evidence for a planned shot. Primary sources are approved capture requirement, Lens contract, and capture environment.

## Workflow

Validate target/state/viewport and sensitive-data boundary; capture only the required evidence; inspect readability; save under assets/captured; register CAPTURED provenance.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not authenticate, expose secrets, or capture unrelated private content. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
