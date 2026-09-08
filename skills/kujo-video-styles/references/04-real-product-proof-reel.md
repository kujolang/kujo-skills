---
name: real-product-proof-reel
display_name: Real Product Proof / Capability Reel
priority: 4
typical_duration: 30-50s
best_for: showing a product/ecosystem doing many real things quickly
base_workflow: product-launch-video | general-video
reference_projects:
  - website-to-hyperframes
---

# Real Product Proof / Capability Reel

## Job to be done

Prove breadth by showing the product actually working.

This format is ideal when Kujo's advantage is not a single screen but a **chain of tools, agents, environments, or outputs**.

The story is:

**simple request -> machinery activates -> multiple concrete proofs -> result**

Good candidates:

- Kujo Agent Platform
- full agent workflow
- Workcell + Dispatch + Shipcheck + Watchdog + RunLedger
- SearchBridge across multiple providers
- a “what Kujo can do” ecosystem reel
- cross-repo capability release

## Core principle

Every proof shot should correspond to a real artifact or action.

A viewer should be able to pause the video and say, “That appears to be an actual system doing an actual thing.”

## Default arc

### Act 1 — Simple ask
Show one prompt, command, event, or input.

Example:
“Ship this change safely.”

### Act 2 — System wakes up
Show routing, environment setup, agent activation, or first action.

### Act 3 — Capability acceleration
Rapid but readable sequence of actual tools doing work.

Example:
- Spec constrains task
- Dispatch routes
- Workcell isolates
- agent edits
- Eval tests
- Watchdog flags
- Shipcheck gates
- RunLedger records

### Act 4 — Outcome
Show the artifact, decision, release, or trace.

### Act 5 — CTA
One action.

## Shot design

Prefer:

- full-screen product capture
- cropped product capture with deliberate zoom
- terminal output
- code excerpts
- logs/traces
- real web/app results
- real generated artifacts

Do not shrink four screenshots into tiny floating rectangles just to fit more things on screen.

One proof per shot is usually better.

## Capability-reel pacing

The reel may accelerate, but information density must remain legible.

Recommended rhythm:

- 3–6s setup
- 3–6s first proof
- 15–25s capability reel
- 5–8s outcome
- 2–4s CTA

The fastest section should be the middle, not the opening.

## Motion language

Use transitions motivated by system flow:

- prompt text becomes terminal command
- agent name becomes node in workflow
- output path becomes next scene
- log line becomes trace visualization
- code block becomes rendered result
- progress state becomes release artifact

This creates causality.

## Audio

This format works well with:

- short VO
- rhythmic SFX linked to system actions
- music that drops or accelerates during the capability reel
- occasional machine/terminal textures used subtly

Do not attach a sound effect to every keystroke.

## Implementation requirements

Build a `proofAsset` abstraction:

```yaml
proof:
  kind: ui | terminal | code | log | diagram | browser | artifact
  source:
  timestamp_or_range:
  crop:
  claim_supported:
  verification:
```

The storyboard must reference these proof assets explicitly.

The agent should refuse to fabricate a proof shot if a claim cannot be demonstrated. It may use a clearly labeled conceptual visualization instead.

## Acceptance criteria

- first product proof within first 10s
- at least 70% of runtime is grounded in real product evidence
- no proof shot is unreadably small
- flow between capabilities is causally understandable
- viewer sees an outcome, not just machinery
- no fake agent logs
- no fake benchmark numbers
- each major capability shown is actually relevant to the release
- CTA is short

## Reference study

Website -> HyperFrames launch:
https://github.com/heygen-com/website-to-hyperframes-demo

The reference project uses real captured clips, sub-compositions, GSAP, VO/SFX, and a capability-reel structure. Study its proof density and transition from simple prompt to output reel.
