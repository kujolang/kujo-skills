---
name: engineering-pr-to-video
display_name: Engineering / PR-to-Video
priority: 8
typical_duration: 30-90s
best_for: PR, technical release, fix, refactor, API change
base_workflow: pr-to-video
reference_projects:
  - HyperFrames pr-to-video workflow
  - pr-to-video-launch
---

# Engineering / PR-to-Video

## Job to be done

Turn a code change into a technical story that a developer can understand without reading the entire diff.

This should become Kujo's native format for:

- meaningful PRs
- SDK releases
- API changes
- bug fixes
- performance work
- reliability/security hardening
- internal architecture changes with user-facing consequences

## Base workflow rule

Always use HyperFrames' current `pr-to-video` workflow as the foundation.

Do not build a parallel PR ingestion system unless the HyperFrames workflow cannot support a required Kujo source.

The Kujo layer should add:

- Kujo visual identity
- Kujo editorial priorities
- optional ecosystem context
- Kujo-specific diagram/code treatments
- routing rules for release severity

## Narrative

A good technical video answers:

1. What was wrong or missing?
2. What changed?
3. Where in the code/system did it change?
4. Why does the implementation solve it?
5. What is the user/developer impact?

Default arc:

**Problem -> representative diff -> mechanism -> evidence -> impact**

## Code selection

Never scroll the full diff.

Select:

- one representative function/interface
- one important before/after
- one test or validation artifact
- one output/behavior proof

The chosen code should support the explanation.

Syntax highlighting and line focus must remain readable.

## Technical visuals

Build reusable primitives:

- diff block
- code focus
- line highlight
- type/interface reveal
- call-flow diagram
- dependency graph
- test pass/fail
- benchmark delta
- terminal reproduction
- trace/log excerpt
- commit/PR metadata header

## Security handling

When a change fixes a vulnerability:

- explain the class of issue at the level appropriate for public release
- do not accidentally generate exploit instructions
- do not expose secrets, tokens, private URLs, or sensitive fixtures
- prefer architectural explanation + fixed behavior

## Performance handling

If performance is the story:

- benchmark must be reproducible or sourced
- hardware/environment must be available where material
- compare like-for-like
- avoid percentage claims without underlying numbers
- show latency/token/memory/size only when measured

## Automation

Input:

```yaml
pr:
repo:
number_or_url:
audience: maintainer | contributor | user | general-dev
angle: feature | fix | refactor | performance | security | release
max_duration:
```

Intermediate artifacts should include:

- ingested PR summary
- selected representative hunks
- excluded hunks with reason
- narrative outline
- factual claim map

## Acceptance criteria

- no invented code
- no diff claim unsupported by PR
- representative code is readable
- technical mechanism is explained, not merely animated
- tests/results shown are real
- contributor attribution is correct if shown
- sensitive data is removed
- impact is clear
- video is useful even to someone who never opens the PR

## Reference study

Current HyperFrames PR story design:
https://github.com/heygen-com/hyperframes/blob/main/skills/pr-to-video/references/story-design.md

PR ingestion:
https://github.com/heygen-com/hyperframes/blob/main/skills/pr-to-video/scripts/ingest.mjs

Launch example:
https://github.com/heygen-com/hyperframes-launches/tree/main/pr-to-video-launch

The current workflow already creates an extracted PR brief and bounded representative diff selection. Extend it; do not bypass it.
