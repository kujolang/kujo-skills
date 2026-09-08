# Input contract v1

The executable validator in `scripts/release_video.py` is authoritative. Copy the JSON shapes from [release.example.json](../examples/release.example.json) and [plan.example.json](../examples/plan.example.json); these are explicitly a style demonstration of the original film, not real new-release facts.

## release.json — supplied facts

- `schema_version`: 1.
- `product`: name, 1–24 characters; `version`: exact release label, 1–20; `url`: display URL, 1–32.
- `usage`: `commercial` or `noncommercial`. Free/open-source software does not by itself establish noncommercial use. Use the actual intended use; do not silently choose noncommercial just to pass an account check.
- `facts`: nonempty array of `{id, text, source}`. IDs are unique; sources are actual inspected release URLs, repository paths/revisions or supplied document references. Keep enough source context to verify a claim later. Unverified notes may be preserved as context but cannot become demonstrated results.

An agent normalizes free-form release information into this shape. The pipeline does not fetch release URLs or infer product capabilities by itself.

## plan.json — agent-authored story

- `schema_version`: 1; `duration`: 15. No other runtime/dimension preset is currently supported.
- `screen_mode`: `illustration` (default for constructed UI) or `verified`; verified requires `verification_source` and actual agent review of that source.
- `fact_refs`: nonempty lists of known fact IDs for `brand`, `hook`, `task`, `loop`, `proof`. Covers associated spoken and screen copy; semantic truth must be reviewed by the agent.
- `music_seed`: integer 0–4294967295. Vary for a release-specific texture; stable on rebuild.
- `task`: typed input, at most 30 characters.
- `stages`: exactly five short labels, at most 18 characters each.
- `evidence`: exactly three labels, at most 28 characters each.
- `copy`: the fields in the example. `loop_title` is three lines (≤11 characters each), `proof_title` two (≤12). `hook_1` ≤12, `hook_2` ≤6, `tagline` ≤42, `button` ≤10. Remaining limits are in `LIMITS` in the validator; it reports the specific offending field. These bounds protect this layout; don't cram long release notes into them.
- `voice`: stock `voice_id`, display `name`, `model_id: eleven_multilingual_v2`, voice settings and `lines`. Lines are keyed `speed`, `goal`, `loop`, `proof`, `brand`; each is `{text, spoken_text?}`. No credentials. The default example uses Brian and the proven voice settings.

The compiler emits `content.js` using serialized data and fills HTML with escaped text. Release content never becomes shell code or JavaScript instructions. Do not bypass this by interpolating untrusted notes into script tags or commands.

Cue windows: speed 1.48–2.72, goal 2.96–5.25, loop 5.83–8.35, proof 8.72–11.62, brand 12.06–14.80 seconds. The mixer preserves pitch, uses a gentle 94% pace where possible, and refuses fitting that would exceed 128% speed. If a line is too long, rewrite it; do not raise the ceiling to force a paragraph into a cue.
