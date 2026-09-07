---
name: videoops-media-provider-execution
description: "Use when generating authorized voiceover, sound effects or music and importing local media through shared VideoOps adapters."
---

# VideoOps media provider execution

## Purpose

Use this skill for generating authorized voiceover, sound effects or music and importing local media through shared VideoOps adapters. Primary sources are kujo-agents/videoops/tools/bin/videoops media CLI, versioned request/result/authorization contracts, GENERATE manifest and scoped authority.

## Workflow

Use the shared media doctor/providers surface without authentication by default. Submit only explicit GENERATE requests through media generate; local assets use media import. Preserve originals, normalized derivatives, alignment and result receipts. Keep provider capability, entitlement, authorization, rights and usage approval separate. Authorization must bind operator-approved exact request fingerprints and credit/cost estimate bounds; requests cannot choose their own smaller reservation. Resume existing jobs; reconcile UNKNOWN_OUTCOME before any retry. Hand normalized paths and provenance to HyperFrames media-use/audio; HyperFrames owns the mix. Record unsupported capabilities and actual mocked/local/live evidence independently.

## Required Output

Write only the role-owned, workspace-relative artifacts named by the current VideoOps agent contract. Include evidence, unavailable capabilities, attempt number, model profile, validation outcome, and an explicit handoff or blocker.

## Boundaries

Never put credential values in arguments or artifacts, assume TTS grants music access, substitute providers silently, or impose a particular voice/style. Read kujo-agents/videoops/00-media-toolchain.md for executable command examples. Preserve role ownership, rights, credentials, provider-cost approval, and the distinction between deterministic facts and model judgment.

## Verification

Validate required inputs before work and outputs afterward. Run deterministic checks before semantic evaluation. Use at most two economical attempts, record stage-local escalation, and never accept a failed artifact because of cost pressure.
