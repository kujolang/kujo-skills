---
name: videoops-asset-rights-triage
description: "Use when classifying media as approved, reference-only, blocked, or pending."
---

# VideoOps asset rights triage

## Purpose

Use this skill for classifying media as approved, reference-only, blocked, or pending. Primary sources are license evidence, intended use, source metadata, and VideoOps policy.

## Workflow

Verify the actual license or permission basis; evaluate attribution and intended-use compatibility; record the decision and evidence; default uncertainty to reference-only or blocked.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Never guess, launder, or overstate a license. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
