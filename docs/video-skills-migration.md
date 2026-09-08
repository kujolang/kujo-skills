# Video skills migration

`kujo-skills` is the canonical home of `kujo-release-video` and `kujo-video-styles`.
Both were migrated together from `kujolang/kujo-hyperframes` commit
`89785161a585a25dd57ce4f346f33fdddf312b68`. The source snapshot and per-file hashes
are in [video-skills-import.json](video-skills-import.json). Migration changes
catalog, installation and handoff documentation; executable code, templates,
voice defaults and source assets retain their behavior and original bytes.
Historical validation records inside the skills describe their original runs;
they are not a claim that this migration repeated paid generation or rendering.

Install both entire folders as siblings in the chosen agent profile. The styles
compiler locates the release preset's GSAP and Departure Mono assets relative to
its own skill location, so no HyperFrames repository checkout is required at
runtime. Keep the font license, GSAP notice and Kujo brand provenance. Native
HyperFrames tools, Node/FFmpeg and generation providers remain production
requirements according to the selected workflow. No voices or account keys are
bundled. Finished films, capture workspaces and historical references stay in
`kujo-hyperframes`.

## Routing and media ownership

- `kujo-release-video`: existing self-contained fixed 15-second production CLI.
  Its cached speech and deterministic sound/mix pipeline are preserved as a
  compatibility preset; migrating it does not replace working production APIs.
- `kujo-video-styles`: creative layer and optional compiler for ten video styles,
  with per-style voice defaults and explicit caller name/ID overrides.
- `kujo-videoops-workflows`: team orchestration, role contracts and review gates.
- `videoops-media-provider-execution`: shared speech/SFX/music acquisition for
  team productions; runtime lives in `kujo-agents/videoops/tools`.

For a VideoOps production, Creative Director selects the preset/style and voice;
Media Generator maps the authored speech cues and resolved voice ID/model/settings
from `voiceover.json` into the current runtime's versioned speech request schema.
The cue file is not itself a schema-valid GENERATE request or an authorization.
Use the current `kujo-agents/videoops/00-media-toolchain.md` contract to create
bounded requests and preserve provider receipts, alignment and approved local
paths. Import already generated preset audio through the local media-import path
instead of generating it again. HyperFrames Editor owns placement and mixing.
Do not invoke both provider routes for the same cue or pretend the fixed preset's
receipt substitutes for a shared runtime receipt. Style/voice selection never
supplies generation authority; honor the user's existing authorization and bounds.

The new preset catalog sections precede generator-owned VideoOps sections so
`generate_videoops_skills.kujo` does not erase them. Routing fixtures cover the
fixed preset, alternative styles and the distinction from raw provider execution.

## Validation

`bash tests/release-readiness.sh` validates all 135 skills and runs the video
regressions. `bash tests/clean-checkout.sh` also runs the isolated video bundle
check. `bash tests/video-skills-install.sh` copies only the two video folders into
a temporary profile, checks imported executable/assets hashes, validates metadata,
runs their offline Python tests from that profile and exercises shared motion.
The tests include compiling all ten styles across three aspect ratios, actual
local asset bundling, variable-duration narration handoffs and voice overrides.
No HyperFrames checkout, paid provider call, or live-profile installation is
needed by these gates.
