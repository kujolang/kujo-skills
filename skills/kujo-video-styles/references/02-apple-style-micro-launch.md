---
name: apple-style-micro-launch
display_name: Apple-Style Micro Launch
priority: 2
typical_duration: 8-15s
best_for: polished single-feature or single-interaction release
base_workflow: motion-graphics | product-launch-video
reference_projects:
  - heygen-apple-motion
---

# Apple-Style Micro Launch

## Job to be done

Turn one product behavior into an extremely polished, short visual statement.

This format is designed for high posting cadence. It should feel expensive because the timing, typography, spacing, interaction, and transitions are precise—not because the screen is full of effects.

Good Kujo candidates:

- one new CLI behavior
- new provider/backend support
- one new agent interaction
- a new control in Kujo AI Chat
- a capability added to Workcell, Dispatch, Ability, Eval, SearchBridge, etc.
- a small release that looks good when shown directly

## Core principle

**One interaction. One payoff. One clean ending.**

If the feature requires six paragraphs of context, choose another format.

## Story patterns

Choose one:

### A. Direct interaction
1. Product surface
2. Cursor/user action
3. Immediate response
4. Result
5. Brand/release sting

### B. Before -> after
1. Old friction in 1–2s
2. Transition
3. New behavior
4. Result
5. End card

### C. Input -> transformation -> output
1. User/agent input
2. system action
3. result expands or resolves
4. name/CTA

## Motion doctrine

This format lives or dies on continuity.

- Use one easing family throughout the piece.
- Match velocity across cuts when possible.
- Do not stop every element before changing scenes.
- Let one dominant movement connect shots.
- Use spring/bounce sparingly and consistently.
- Keep camera moves simple.
- Build animation around the product interaction itself.

The agent should create a `motionProfile` per video:

```yaml
easing_family:
transition_axis:
primary_speed:
secondary_speed:
overshoot:
camera_behavior:
```

Do not allow arbitrary per-element easing unless justified.

## Visual design

- large negative space
- high-contrast hierarchy
- authentic product UI
- 1–2 text levels
- minimal captions
- no decorative paragraphs
- no “feature cards”
- no background motion that competes with the interaction

## Audio

Audio should be minimal:

- one UI click/tap
- one transition whoosh if needed
- one result/resolve cue
- optional tiny music bed or tonal texture
- usually no voiceover

If narration is required, the concept is probably better suited to a Feature Reveal.

## Reusable implementation

Build reusable components:

- oversized cursor
- click/tap ripple
- UI focus crop
- panel expand
- modal/sheet reveal
- code/terminal input
- result resolve
- velocity handoff
- micro logo sting
- URL/install command end card

The template should make it easy to swap the underlying product recording or DOM-based recreation without rebuilding timing logic.

## Default storyboard

### Beat 1 — Setup (0–2s)
Establish the surface and target.

### Beat 2 — Interaction (2–6s)
One human/agent action.

### Beat 3 — Response (6–10s)
Product behavior becomes visually obvious.

### Beat 4 — Resolve (10–13s)
Show the useful outcome.

### Beat 5 — Sting (last 1–2s)
Feature/product name + Kujo.

Adjust timing to the actual feature.

## Acceptance criteria

- understandable without narration
- no more than one dominant feature
- meaningful movement begins in first second
- product behavior remains readable at social-feed size
- no shot exists only to fill time
- transition vectors feel continuous
- no more than 2–3 major motion ideas
- no gratuitous 3D
- end card <=20% of total duration
- loop/replay feels clean when used on social

## Reference study

- HyperFrames launch library: https://github.com/heygen-com/hyperframes-launches
- Study the `heygen-apple-motion` project if present in the current library checkout.

Extract timing, easing consistency, transition continuity, and product-centric staging. Do not imitate Apple branding.
