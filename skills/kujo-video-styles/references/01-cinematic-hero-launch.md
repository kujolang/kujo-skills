---
name: cinematic-hero-launch
display_name: Cinematic Hero Launch
priority: 1
typical_duration: 40-60s
best_for: major product, platform, or category-defining launch
base_workflow: product-launch-video | general-video
reference_projects:
  - HyperFrames launch
  - Claude Paper launch
---

# Cinematic Hero Launch

## Job to be done

Create the flagship film for a release important enough to define how the audience sees Kujo.

This is not a feature walkthrough. It is the video that says **why this thing exists, what changed, and why the viewer should care**, while proving enough of the product that the claim feels earned.

Use sparingly.

Good Kujo candidates:

- major Kujo language release
- Agent Platform release
- major Workcell/control-plane release
- a new Kujo category or architectural thesis
- a release that combines multiple Kujo primitives into one new experience

Do **not** use this for routine patches or small capability updates.

## Core narrative

Default arc:

1. **Intrigue** — establish tension, question, or abnormality.
2. **Interaction** — show the viewer the product doing something concrete.
3. **Expansion** — reveal that the capability is larger than the first example.
4. **Thesis** — state the deeper meaning of the release.
5. **Identity** — attach the idea to Kujo.
6. **CTA** — end cleanly and confidently.

The first 3–5 seconds must create curiosity without requiring context.

## Visual grammar

Use a premium editorial/product-film language:

- real product surfaces
- large typography used as punctuation, not paragraphs
- controlled depth
- purposeful glass/transparency only where it maps to product layering
- one or two hero motion ideas repeated across the film
- high-detail macro views of UI/code/terminal when they create proof
- brief abstract moments only when they clarify a concept that cannot be filmed directly

A 50-second film may use many sub-compositions, but it should still feel like **one world**.

## Motion rules

- Favor continuous camera logic over cuts that reset spatial orientation.
- Use matched-direction transitions when practical.
- When a UI element exits with momentum, let the next scene inherit that momentum.
- Use scale changes to move from concept -> system -> detail.
- Reserve the strongest transition for the thesis or product-name reveal.
- Avoid using a “special transition” on every cut.
- Do not let kinetic typography compete with product proof.

Recommended shared primitives:

- `heroReveal()`
- `pushThrough()`
- `velocityHandoff()`
- `macroZoom()`
- `artifactCascade()`
- `thesisType()`
- `logoResolve()`

## Audio

Audio should carry narrative weight.

Preferred construction:

- authored voiceover or carefully chosen silence
- sparse but precise UI/impact SFX
- music that supports the arc rather than playing continuously at one intensity
- a noticeable change in audio energy at the reveal/thesis beat

Silence before an important line can be more effective than another impact sound.

## Storyboard template

### Beat 1 — Cold open
- 2–5s
- Present the problem, question, contradiction, or provocative state.
- No logo wall.
- No generic “Introducing…”

### Beat 2 — First proof
- 5–10s
- Show the simplest concrete product behavior.
- Viewer should understand what is happening visually.

### Beat 3 — Expansion
- 10–20s
- Show 2–4 additional capabilities in a controlled acceleration.
- This is where a montage is allowed.

### Beat 4 — Meaning
- 5–10s
- State why the release matters.
- Slow the edit enough that the thought lands.

### Beat 5 — Identity
- 3–8s
- Product/release name.
- Kujo branding.
- Optional version.

### Beat 6 — CTA
- 2–5s
- URL, install command, GitHub/repo, or single next action.

## Implementation requirements

The video skill should build:

- a reusable hero-intro composition
- a capability-montage composition
- a thesis-frame composition
- a Kujo identity/end-card composition
- shared transition primitives
- a configurable audio cue map

Avoid building a monolithic 1,000-line composition. Major beats should be reusable sub-compositions.

## Acceptance criteria

A Cinematic Hero Launch passes only if:

- the main idea can be stated in one sentence
- the opening creates tension or curiosity in <5s
- real product proof appears before the midpoint
- the film contains a clear thesis beat
- the strongest visual moment corresponds to the strongest narrative moment
- branding does not appear as a substitute for story
- there are no static “feature list” scenes
- all product claims have traceable sources
- scene seams have been explicitly reviewed
- sound-off viewing still communicates the core story
- full-audio viewing feels authored, not auto-generated

## Reference study

Primary reference:
- HyperFrames launch source: https://github.com/heygen-com/hyperframes-launch-video
- HyperFrames launch library: https://github.com/heygen-com/hyperframes-launches/tree/main/hyperframes-launch

Secondary:
- Claude Paper launch: https://github.com/heygen-com/hyperframes-launches/tree/main/claude-paper-launch

Study structure, continuity, compositional hierarchy, and how real product surfaces are mixed with larger conceptual beats. Do not copy branding or recreate shots one-for-one.
