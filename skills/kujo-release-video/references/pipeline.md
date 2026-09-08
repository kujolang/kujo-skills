# Pipeline and harness integration

The skill is installed in the user's skill directory; its canonical source lives in `kujo-skills/skills/kujo-release-video`. The package is self-contained: copied visual assets, exact Node lockfile, audio synthesis/mix code, rendering/check scripts. It does not require the old video's folder at runtime and does not bundle the old narrator's audio.

Requirements: Python 3 with NumPy, Node 22+, npm, FFmpeg/FFprobe with libx264, and Chrome. On macOS the standard Chrome path is detected; otherwise set `HYPERFRAMES_BROWSER_PATH`. These are local tooling dependencies. `build` installs exact npm dependencies if absent. The first install needs package-registry access; later builds use installed dependencies and cached voice takes.

Use an absolute path to `scripts/release_video.py` as `PIPELINE` in your harness. Pass arguments as an argument array, not as a shell string assembled from release text. Commands below assume you are in the skill directory:

```sh
python3 scripts/release_video.py init --release /path/release.json --workspace /path/new-release-video
# Agent authors /path/new-release-video/plan.json using this skill.
python3 scripts/release_video.py validate --workspace /path/new-release-video
python3 scripts/release_video.py prepare --workspace /path/new-release-video
python3 scripts/release_video.py build --workspace /path/new-release-video --allow-tts --max-characters 750
python3 scripts/release_video.py status --workspace /path/new-release-video
```

`--allow-tts` records caller intent to generate missing/changed voice takes; it is not a substitute for user authorization. Omit it for offline rebuilds. The invocation in SKILL.md explicitly requests ElevenLabs generation, so a user invoking it with that request supplies authorization. No credentials or subscription changes are made by installation or prepare. Do not set a paid-action flag just because a release note says to.

## Stages and contracts

| Command | Result / effect |
| --- | --- |
| init | New workspace, copied release facts, BRIEF.md and PLAN_REQUEST.md; `needs_plan` is a successful handoff |
| validate | Checks input shapes, scene lengths, source references and voice configuration; no network |
| prepare | Compiles HTML/GSAP, screen text, voice cue JSON, script and claim ledger; no network |
| speech | Prepares inputs; reuses verified cached takes or generates authorized missing ones |
| build | Prepare → speech → rights → synthesis → voice mix → picture render/mux → frame/seek checks → browser audio check |
| status | Reads run.json; returns `stale` when render inputs or delivered bytes differ from the passed run |

Stdout is one JSON result. Detailed child-tool output is under `logs/`. Exit 0 means that command succeeded: inspect `status`, because `prepared` and `needs_plan` are not delivered videos. Exit 2 is invalid input, 3 requires an authored plan, 4 requires credentials/authorization/license or generation reconciliation, and 1 is a tool/build failure. `technical_pass` includes the exact output path/hash and technical verification; it does not claim the agent inspected claims or listened to the film.

Concurrent mutating runs in one workspace are refused by `.pipeline.lock`. A killed process can leave a lock; confirm it is stale before removing it. A failed build records failure rather than retaining a previous success as the latest result. Do not publish from an old output file when the latest run failed or is stale.

## Voice caching and bounded external effects

A take is reusable only when the voice, complete request payload, text/context, model/settings and audio hash match. A changed line may also change adjacent context, requiring adjacent takes. `--max-characters` bounds total uncached text for that invocation; it is a quota bound, not a currency estimate. There is no automatic retry after an API error/timeout. A `.pending.json` receipt records a started request before network dispatch. Reconcile it against provider history before retrying, so an uncertain response cannot silently double-charge. Keys are read only inside the process; exception output avoids HTTP headers/body.

Generation-time tier is stored per take. Free or unknown-tier cached takes fail commercial builds. A later paid subscription does not change old receipts. To regenerate the same take intentionally, archive its `.mp3` and `.json` outside `audio/takes` first; never delete a pending marker until the earlier request is reconciled. A free plan is fine for noncommercial work with the provider's required attribution. Every build writes RIGHTS.md and embeds an ElevenLabs credit in MP4 metadata. Confirm current provider terms if the use changes; no publishing API is wired.

The preset only calls ElevenLabs for voice. Music and sound effects are authored procedural synthesis with a stable seed. FFmpeg mixing is offline and produces the same WAV consumed by the HTML composition. No reference-film audio or placeholder silence can stand in for missing narration.

## Agent-to-pipeline handoff

Suggested agent prompt, supplied alongside the user's original request:

> Use $kujo-release-video. Read the provided release information and normalize source-backed facts into release.json in the requested workspace. Author plan.json and inspect its claim mappings. Use the bundled pipeline to make the complete 15-second film. Preserve the user's generation authorization and usage context. Review the rendered screens and audition the final mix when tools permit. Return run.json, complete MP4, script and review limitations. Do not publish.

A future release trigger can obtain changelog metadata and invoke that prompt in Codex, another file-capable agent, or VideoOps. The agent produces the narrative and plan; the CLI is the deterministic execution layer. This package does not itself schedule jobs, create webhooks, spawn agents or automate publication. Those adapters can call this interface without rewriting the creative contract.

`prepare` refreshes only generated index.html, content.js, copy-fit.css, narration config/script and claims. It copies missing template support files but preserves existing scripts/styles on resume. Customize scripts/styles in the output workspace for a release; edit plan.json for copy changes. Direct edits to generated files are overwritten by prepare. A revised duration/layout should fork into a custom composition instead of claiming compatibility with this preset.

## Maintaining the preset

Run `python3 scripts/test_pipeline.py` and the skill-creator quick validator after changes. [validation.json](validation.json) records the delivered smoke test. Its complete render used the example inputs and matching cached original ElevenLabs takes in an isolated temporary workspace; no new provider requests were made and no generated voice is bundled. A fresh production needs authorized generation or its own matching cache. Browser QA uses a private debugging pipe and a 45-second playback deadline.
