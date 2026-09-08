---
name: feature-reveal
display_name: Feature Reveal / Pain-to-Payoff
priority: 6
typical_duration: 15-35s
best_for: a feature that removes obvious friction
base_workflow: product-launch-video
reference_projects:
  - timeline-launch
  - inspector-launch
---

# Feature Reveal / Pain-to-Payoff

## Job to be done

Make one new feature feel inevitable by showing the friction it removes.

Best for:

- an action that used to require multiple steps
- a reliability issue that is now solved
- a new control that replaces prompt round-trips
- a workflow that is dramatically shorter
- a new editor/inspector/interactive capability

## Core story

**Old friction -> tension -> reveal -> new behavior -> payoff**

The before state should be recognizable, not exaggerated.

Do not make the previous product look intentionally broken.

## Default storyboard

### Beat 1 — Friction
2–6s

Show the old workflow or problem directly.

### Beat 2 — Cost
2–5s

Make the repeated action, waiting, ambiguity, or extra work visible.

### Beat 3 — Reveal
1–4s

Introduce the feature.

This can be a hard visual reset, camera shift, panel reveal, or interface transformation.

### Beat 4 — New workflow
5–12s

Show the feature actually performing the task.

### Beat 5 — Payoff
3–6s

Show fewer steps, clearer state, faster completion, or better control.

### Beat 6 — Name
1–3s

Feature + Kujo.

## Evidence rules

Claims like “faster,” “one click,” or “no round-trip” must be literally true.

If the improvement is measured, use real timing or benchmark data.

If the advantage is qualitative, show the shorter workflow without inventing a percentage.

## Motion

Before the reveal:
- slightly repetitive or constrained movement can communicate friction.

After the reveal:
- motion becomes simpler, cleaner, more direct.

This creates a physical feeling of reduced friction.

Do not make the “before” intentionally ugly unless that reflects the real experience.

## Copy

Use copy as a pivot:

Examples of structures:
- “Before: …” / “Now: …”
- “Stop asking the model to …”
- “Change it directly.”
- “One control. Immediate result.”

The actual wording should come from the release.

## Implementation components

- before/after split
- repeated-step sequence
- prompt/round-trip sequence
- reveal wipe
- focus/zoom
- direct manipulation UI
- result comparison
- metric delta if sourced

## Acceptance criteria

- the pain is visible, not merely narrated
- the feature reveal occurs before 60% of runtime
- the new workflow is shown in full enough to understand
- no inflated comparison
- no fake timings
- before/after states use comparable framing
- payoff is obvious without voiceover

## Reference study

Timeline:
https://github.com/heygen-com/hyperframes-launches/tree/main/timeline-launch

Inspector:
https://github.com/heygen-com/hyperframes-launches/tree/main/inspector-launch

Study how the release itself changes the interaction model.
