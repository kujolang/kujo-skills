---
name: videoops-technical-render-review
description: "Use when checking render integrity, media, fonts, frames, dimensions, FPS, duration, and audio."
---

# VideoOps technical render review

## Purpose

Use this skill for checking render integrity, media, fonts, frames, dimensions, FPS, duration, and audio. Primary sources are rendered file, platform JSON, render log, FFmpeg/ffprobe, and HyperFrames checks.

## Workflow

Run deterministic integrity and metadata checks first; inspect errors, gaps, missing assets/fonts, placeholders, black frames, and stream mismatch; preserve commands and results.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Technical pass is necessary but cannot substitute for creative review. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
