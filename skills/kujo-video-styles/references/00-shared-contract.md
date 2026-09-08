# Kujo HyperFrames Video System — Shared Contract

This document defines the rules shared by every Kujo video type in this pack.

## Purpose

These video types are **creative/storytelling layers**, not replacements for HyperFrames' native workflows. The implementation should preserve HyperFrames' router, validation, deterministic rendering, media handling, and specialized skills, then apply the Kujo type after the correct underlying workflow has been selected.

Examples:

- Product/site launch -> HyperFrames `product-launch-video`
- GitHub PR/code change -> HyperFrames `pr-to-video`
- Very short unnarrated motion unit -> HyperFrames `motion-graphics`
- Custom multi-scene film -> HyperFrames `general-video`
- Weekly release-note digest -> HyperFrames changelog workflow where available

The Kujo layer should decide *how the story is told*.

## Global quality bar

Every video must satisfy all of the following:

1. **One dominant idea.** The viewer should understand the point even with the sound off.
2. **Show proof, not claims.** Prefer real UI, terminal output, code, diagrams generated from real data, product captures, or actual artifacts.
3. **No slide-deck pacing.** Avoid a sequence of static cards with dissolve transitions.
4. **Motion has continuity.** Incoming and outgoing scenes should share direction, momentum, scale, or visual anchors when possible.
5. **Design is restrained.** Fewer high-quality effects beat many unrelated effects.
6. **Audio is authored.** SFX, VO, music, and silence are intentional rather than afterthoughts.
7. **Text is editorial.** Large copy is short. Supporting copy is subordinate. Never make the viewer read release notes.
8. **Deterministic render.** Animation must use HyperFrames-compatible timing/seek patterns.
9. **Real assets first.** Do not fabricate product UI when authentic screenshots, recordings, terminal captures, logos, diagrams, or code are available.
10. **Every frame earns its existence.** If a beat does not advance the story, remove it.

## Kujo visual direction

The implementation must consume Kujo brand tokens rather than hard-code a single palette into every template.

Recommended token interface:

```json
{
  "brand": {
    "background": "...",
    "foreground": "...",
    "muted": "...",
    "accent": "...",
    "danger": "...",
    "success": "...",
    "fontDisplay": "...",
    "fontBody": "...",
    "fontMono": "...",
    "logo": "...",
    "logomark": "..."
  }
}
```

When the real Kujo brand system provides a token, use it. Do not invent a new competing style system.

## Motion doctrine

Build a shared motion library so all formats feel related.

At minimum provide:

- entrance / exit primitives
- mask reveals
- scale-through transitions
- directional push / pull transitions
- velocity-matched scene handoff
- shared cursor treatment
- terminal/code reveal primitives
- kinetic type primitives
- logo sting
- caption rail
- UI focus / spotlight
- zoom-to-detail
- artifact stack / fan
- count-up / metric emphasis
- connector / flow-line animation
- subtle noise / texture layer where appropriate
- audio cue hooks

Use a small number of easing families consistently. A scene should not use random easing values per element.

## Input contract

Every type should accept a normalized brief:

```yaml
video_type:
goal:
audience:
primary_message:
cta:
duration_target:
aspect_ratio:
source_kind:
source:
release_or_feature_name:
version:
proof_assets:
must_show:
must_not_show:
voiceover:
music:
captions:
brand_profile:
```

Not every field is required. The router should determine missing values from the source where possible.

## Output contract

Each run should produce or update:

- `BRIEF.md`
- `STORYBOARD.md`
- `SCRIPT.md` when narration exists
- design/frame tokens used by the composition
- captured or normalized source assets
- HyperFrames composition source
- render/preview metadata
- QA report
- final rendered video when the calling workflow asks for it

## Storyboard contract

Every beat should specify:

```yaml
beat:
purpose:
duration:
visual:
source_of_truth:
copy:
motion:
audio:
transition_in:
transition_out:
verification:
```

`source_of_truth` is mandatory for any factual product claim.

## Asset hierarchy

Prefer assets in this order:

1. Actual product capture
2. Actual terminal/code/output
3. Actual diagram derived from product/repo data
4. Brand asset
5. Abstract visualization
6. Generated decorative media

Generated decorative media must never substitute for proof when proof exists.

## Agent implementation rules

The video-making skill should:

1. Route into the correct HyperFrames base workflow.
2. Select a Kujo video type.
3. Load this shared contract.
4. Load exactly one type spec unless the user asks for a hybrid.
5. Build the brief.
6. Gather evidence/assets.
7. Storyboard before implementation.
8. Implement with shared motion primitives.
9. Run HyperFrames lint/validation and the workflow-specific checks.
10. Review snapshots across the timeline.
11. Check seams at every scene boundary.
12. Verify claims against the original source.
13. Report what was and was not verified.

## Anti-slop rules

Reject or rewrite any concept that depends on:

- endless floating glass cards
- generic AI brain/network imagery
- meaningless particle fields
- fake terminal text
- fake metrics
- fake customer quotes
- long bullet lists
- every word animated individually
- a new visual style for every scene
- constant camera movement with no narrative purpose
- decorative 3D inserted only to appear expensive
- stock-music pacing that ignores the visual story

The target is **specific, authored, technically credible motion design**.
