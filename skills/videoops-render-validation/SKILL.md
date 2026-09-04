---
name: videoops-render-validation
description: "Use when rendering and deterministically inspecting a HyperFrames output."
---

# VideoOps render validation

## Purpose

Use this skill for rendering and deterministically inspecting a HyperFrames output. Primary sources are composition, platform JSON, HyperFrames check/render, FFmpeg/ffprobe, and Eval.

## Workflow

Run lint/check before render; record render exit and version; probe integrity, dimensions, FPS, duration, audio, checksum, and placeholder/debug markers; fail closed on required mismatch.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Do not ask a model to determine facts available from tools or declare a placeholder final. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
