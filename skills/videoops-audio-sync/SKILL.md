---
name: videoops-audio-sync
description: "Use when synchronizing voice, SFX, music, and silence to planned beats."
---

# VideoOps audio sync

## Purpose

Use this skill for synchronizing voice, SFX, music, and silence to planned beats. Primary sources are transcript, shot list, audio assets, platform contract, and FFmpeg.

## Workflow

Align speech and visual events to frames; protect intelligibility; use silence deliberately; inspect clipping, streams, start/end, and loudness evidence; record audio substitutions.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not use unlicensed audio or let music compete with speech. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
