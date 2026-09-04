---
name: videoops-fix-list-application
description: "Use when applying Critic issues with one outcome per item."
---

# VideoOps fix list application

## Purpose

Use this skill for applying Critic issues with one outcome per item. Primary sources are schema-valid fix list, exact reviewed draft, composition, and acceptance criteria.

## Workflow

Verify draft/checksum lineage; apply each issue narrowly; mark APPLIED, PARTIAL, REJECTED, or BLOCKED with evidence; rerun affected gates; render a new version.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not ignore issues, rewrite unrelated scenes, or exceed three review cycles. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
