---
name: videoops-approval-decision
description: "Use when producing deterministic VideoOps PASS or FAIL from defect evidence."
---

# VideoOps approval decision

## Purpose

Use this skill for producing deterministic VideoOps PASS or FAIL from defect evidence. Primary sources are technical gates, review dimensions, thresholds, confidence, and revision count.

## Workflow

Fail on unresolved BLOCKER/HIGH or configured threshold breach; pass only when required dimensions and technical gates meet policy; write approval and fix list consistently; escalate after three failed cycles.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not approve because rendering succeeded or downgrade quality to meet budget. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
