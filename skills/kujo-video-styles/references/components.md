# Reusable scenes and motion

The compiler uses the same primitives an agent can import into a native composition. `assets/motion.js` creates no timeline: call `KujoMotion.create(tl, motionProfile)` with the composition's registered paused timeline. Functions accept a DOM element/scoped selector, global start in seconds and duration. Pass element lists to codeReveal/artifactFan. `velocityHandoff(outgoing, incoming, t, d, distance)` shares direction and constant speed across an overlapping native scene boundary. `audioCue(event, t)` creates timing labels only; author actual SFX through native media/audio tools.

| Component | Source/content | Purpose and reusable treatments |
| --- | --- | --- |
| hero / thesis | Short grounded assertion plus optional evidence | Hero intro, thesis frame, oversized claim / principle wordmark; mask/type/zoom |
| product | Actual image/video capture or terminal artifact | UI focus/crop, spotlight, zoom-to-detail, panel/modal expand, cursor/tap, result resolve |
| artifacts | Actual captured outputs | Capability montage / artifact stack; fan/cascade; split long montages into independent shots |
| identity | Supplied logo/logomark, exact product/version, CTA | Shared end-card / micro sting; logo resolve, loop resolve |
| code / terminal / diff | Local actual excerpt file, <=24 lines | Sequential line reveal, representative before/after excerpts, line focus, interface reveal, trace/log/test output; never fabricate a pass/fail result |
| flow | 2–5 source-backed `nodes` | Handoff boundary, call flow/dependency chain, connector reveal; use an authentic diagram asset for a branching graph |
| contrast | Exactly two comparable proof assets | Before/after split, result comparison, evidence/quote contrast; match capture framing |
| steps | 1–5 source-backed `steps` | Repeated-step / prompt-round-trip sequence and friction; stagger |
| metric | `value`, `unit`, `measurement` | Measured delta/emphasis; `countUp` animates a prepared digit strip without frame callbacks |
| quote | Actual source excerpt and attribution in support | Editorial evidence plate, short quotation, no invented endorsement |
| kinetic | Short name/version/copy | Kinetic wordmark, mask slam, fast scale; optional authored rulers/texture |

Shared library also supplies entrance/exit, push/pull, scale-through, caption rail, subtle texture opacity and audio labels. Style reference names heroReveal/pushThrough/macroZoom/artifactCascade/thesisType/logoResolve are callable aliases. The source pack's optional chromatic, grid and 3D effects are creative options; add only when the story needs them, using current native registry primitives. No effect is required just to fill a beat.

All design colors and font families resolve through `brand-tokens.json`/`brand_profile`; the defaults derive from the existing Kujo trust-at-speed recipe. Logo assets remain explicit inputs so a partner logo is never silently replaced with Kujo. Provide real partner captures and accurate relationship wording for integrations.

The starter has three responsive canvas shapes and a single root timeline assembled from small component functions. It is a production starting point, not a set of shot-for-shot reference-film clones. `prepare` regenerates composition files: once editing them directly, stop calling prepare or port edits back into the plan/library. Use native composition tools for sub-compositions, intricate branching diagrams, overlapping transitions, tracked crops and full typography direction.
