# Agent pipeline contract

## Install / discover

Keep `kujo-video-styles` and `kujo-release-video` as sibling skill folders. The starter reuses the existing preset's vendored GSAP and Departure Mono plus its font license; no network asset load is needed. Install/link both into the agent's skills directory. The canonical source is `kujo-skills/skills/kujo-video-styles`. For a checkout install on macOS/Linux:

```bash
ln -s /absolute/kujo-skills/skills/kujo-release-video ~/.codex/skills/kujo-release-video
ln -s /absolute/kujo-skills/skills/kujo-video-styles ~/.codex/skills/kujo-video-styles
```

Do not replace an existing skill directory without inspecting it. The native HyperFrames entry/domain workflows are production dependencies, discovered and installed via their current entry skill. Python 3.9+ runs the Kujo CLI. Native checks/rendering need the current HyperFrames CLI, Node and FFmpeg per that workflow. No renderer/package version is silently pinned by the Kujo layer.

`list`, `route`, `init`, `validate`, `prepare` return `{ok,result}` on exit 0 or `{ok:false,error}` on exit 2. No paid calls, remote ingestion, account changes or publishing occur. `init` requires a nonexistent workspace. Run one job per workspace. Preserve logs with the external harness's run ID.

## Normalized input (`brief.json`)

```json
{
  "video_type": "short-product-launch",
  "goal": "Announce the release",
  "audience": "Developers using the tool",
  "primary_message": "One source-backed message",
  "cta": "An actual next action",
  "duration_target": 20,
  "aspect_ratio": "16:9",
  "source_kind": "github_release",
  "source": {"repo": "owner/repo", "version": "exact-tag"},
  "release_or_feature_name": "Actual product name",
  "version": "exact-tag",
  "proof_assets": [],
  "must_show": [],
  "must_not_show": [],
  "voiceover": false,
  "music": false,
  "captions": false,
  "brand_profile": {}
}
```

This is a schema illustration, not factual content for a film. Inspect the user's source before authoring copy. `init` tolerates missing facts for intake; `validate`/`prepare` require goal, audience, primary message, CTA, source and release/feature name. `source` can be a URL/path or native structured release/git-range input. Native workflow handles ingestion; Kujo never fetches or executes source strings. Supply `source_kind: github_pr` for a PR. `fps` defaults to 24; 25/30/60 supported. Canvas: 16:9 (1920×1080), 9:16 (1080×1920), 1:1 (1080×1080).

Automatic routing hints: `multiple_changes`, `single_interaction`, `integration`, `pain_to_payoff`, `breadth`, `thesis`, `major_release`, and `intent: teaser|drop|sting`. They are caller/agent decisions after inspecting intent, not arbitrary keywords scraped from source. Explicit `video_type` overrides inference. The native-selected `base_workflow` may be supplied; PR provenance still requires `pr-to-video`. Supply `available_workflows: ["changelog-video"]` only after actual discovery. Otherwise changelog falls back to the product/custom workflow. A short narrated film does not route to motion-graphics.

`voiceover`/`music`/`captions` default false; true or an authored preference enables the production requirement. `brand_profile` is a partial token object: background, foreground, muted, accent, danger, success, fontDisplay, fontBody, fontMono, logo, logomark. Resolve actual brand values before production; optional local logos must be inside the workspace. Paths are portable workspace-relative, not remote URLs. The emitted token file records the resolved values; change brand_profile to change a rebuild.

## Evidence and plan

Each `plan.sources` item needs unique `id`, `source` (URL/path), `range` (line/hunk/time), `claim` and `verification` (what the agent inspected). Each beat must name these IDs in `source_of_truth`. Both narration and copy must be semantically supported; IDs alone cannot establish truth. The agent manually reviews `must_show`, `must_not_show`, every claim and the selected reference's acceptance checklist.

Each `brief.proof_assets` item:

```json
{
  "id": "capture-1", "kind": "terminal", "media_type": "text",
  "path": "assets/actual-output.txt", "source": "Actual command/run artifact",
  "timestamp_or_range": "Exact lines or capture time",
  "claim_supported": ["fact-1"], "verification": "How this output was inspected",
  "authentic": true, "rights": "Source/ownership/license basis"
}
```

Kinds: ui, terminal, code, log, diagram, browser, artifact. Media: image/video/text. Video also needs inspected `media_duration` and optional `media_start` (seconds); the range must cover its beat. Optional `crop` has normalized x/y/width/height inside the source. Crops apply to images/video; native tools handle animated reframing. Text excerpts must contain actual bounded source, <=24 lines/120 characters per line (narrow layouts may need less). No shell/HTML interpretation occurs. Assets must exist within the workspace. Non-authentic visuals require `conceptual: true` on their beat and receive visible labeling; they never count toward real-proof runtime.

`init` writes a style-specific beat blueprint. Every beat has id, role, purpose, duration, visual, copy, support, source_of_truth, proof_assets, motion, audio, transition_in/out, verification, narration and conceptual. Complete empty values. [Components](components.md) defines component-specific fields. `caption` is optional authored visible text; produce sentence-level caption timing through the native caption workflow when needed. `audio` is a list of `{event,offset}` cue intentions, offset relative to beat start.

Durations must sum within one frame. A deliberate departure from a recommended type range requires `duration_override_reason`. Narrated micro/drop styles also need `voiceover_reason`. The plan's motionProfile has easing_family power2/3/4, transition_axis x/y, primary_speed and secondary_speed in seconds (0,1], overshoot 0, camera_behavior focus/static. Author other motion profiles through the native workflow rather than bypassing starter validation.

The validator enforces structural references, local asset availability, evidence runtime (70% proof reel), reveal/proof timing, selected type limits and component inputs. It cannot audit actual visual truth, partner status, performance comparability, or creative quality. Keep QA pending until reviewed. RELEASE_SELECTION accounts for all changelog items and omissions; PR_SELECTION records native ingestion, selected and excluded hunks with reasons. These editorial artifacts must be filled by the agent, not just created.

## Production / QA

1. Native entry selects workflow and inspects source. Run route/init, author plan and gather assets. Keep the chosen native workflow in BRIEF.
2. Validate, then prepare. Outputs: composition/, STORYBOARD, optional SCRIPT, brand tokens, source-assets with content hashes, cue map, structural checks with exact sample times, and not-rendered metadata. `prepare` rewrites generated composition, so preserve direct artistic edits or reuse motion/components in native source instead.
3. Use the native workflow's full audio pipeline. Optional `plan.audio_master` points to a local authored mix; `audio_provenance` records provider, generation-time license, music/SFX rights and mix source. Native media tools own synthesis and audio QA. No fake voice fallback. If sound was requested but no master exists, render metadata explicitly says not-produced. Do not deliver a supposedly complete film in that state.
4. Run native `hyperframes check composition --snapshots` and snapshot the times in checks.json. Review midpoints and seam ±1 frame, portrait/mobile text, real capture source ranges and final/loop frame. Fix overflows in source; do not suppress layout findings without evidence. Inspect unvoiced micro/drop payoff timing and continuity; verify each reference's remaining qualitative acceptance criteria in QA.md.
5. Preview/render per the user's requested scope through native HyperFrames. Use the same master in preview and render. If exporting silent and complete variants, label them clearly. Verify requested duration, dimensions, fps and audio streams with ffprobe; update render-metadata with command, CLI version, actual file path/hash and QA result. State listening/review limitations honestly. Include rights and source mappings. A structural pass is never a completed production verdict.

## Verification for maintainers

```bash
python3 -m unittest discover -s skills/kujo-video-styles/scripts -p 'test_*.py'
node skills/kujo-video-styles/scripts/test_motion.cjs
python3 -m unittest discover -s skills/kujo-release-video/scripts -p 'test_*.py'
```

The tests use explicitly synthetic source fixtures solely to exercise the compiler; they are not production proof or user-facing demos. Browser checks and seek tests complement these unit gates; a successful fixture render does not approve future authored films.

Optional browser integration gate: `node scripts/test_browser.mjs <prepared-fixtures-parent> <absolute-puppeteer-core-module> <Chrome-executable>` (paths relative to this skill). It checks all settled beats for visible content and text bounds, catches page/request failures, and compares pixel hashes after reverse/random seeks. Fixtures must be compiled first with the test helper; evidence remains outside the repository.

Checked implementation coverage is recorded in [validation.json](validation.json). This evidence applies to the skill tooling, not to future authored release claims.

## Voice selection

[Per-style voices and overrides](voices.md) define the default speaker and delivery settings. `voiceover` still controls whether narration is requested; `voice` selects its speaker. `route`/`init` expose derived `resolved_voice`; `prepare` emits `voiceover.json` for the native speech workflow, with authored narration cues using actual beat durations. User ID/name overrides win, unknown names remain unresolved until catalog lookup, and no paid call or automatic speaker substitution occurs. The original fixed release preset still defaults to Brian.

## VideoOps team integration

When these styles are used by the VideoOps team, use `videoops-media-provider-execution` and the current `kujo-agents/videoops/00-media-toolchain.md` contract for speech/SFX/music acquisition. Map `voiceover.json` cues and resolved voice ID/model/settings into the runtime's versioned speech request; this cue file is neither a GENERATE request nor authorization. Preserve operator-approved bounds, originals, alignment and receipts, then hand approved local media to HyperFrames for placement/mixing. Import existing preset audio instead of generating it twice. Standalone style authoring still uses the native HyperFrames workflow.
