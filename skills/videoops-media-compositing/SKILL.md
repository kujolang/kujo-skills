---
name: videoops-media-compositing
description: "Use when placing and trimming approved image, video, GIF-derived, and audio assets."
---

# VideoOps media compositing

## Purpose

Use this skill for placing and trimming approved image, video, GIF-derived, and audio assets. Primary sources are manifest-approved assets, shot timings, HyperFrames, and FFmpeg.

## Workflow

Verify manifest/path match; normalize browser-hostile media; compose crop/scale/mask/layering; trim to frame contract; inspect transition frames and missing media; record substitutions.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not introduce undocumented or reference-only media. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
