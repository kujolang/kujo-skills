---
name: videoops-media-normalization
description: "Use when inspecting, trimming, and transcoding approved source media while preserving originals."
---

# VideoOps media normalization

## Purpose

Use this skill for inspecting, trimming, and transcoding approved source media while preserving originals. Primary sources are approved asset, FFmpeg/ffprobe, target shot, and manifest.

## Workflow

Probe streams and properties; preserve source; create deterministic normalized copy; trim only irrelevant head/tail; verify output checksum, codec, dimensions, FPS/duration, and audio.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not creatively edit, overwrite originals, or normalize unapproved media. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
