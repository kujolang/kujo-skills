# Voice defaults and overrides

Every style has a default ElevenLabs stock voice **when narration is requested**. Selecting a voice does not enable narration or authorize paid generation. Existing silence defaults remain, especially micro launches and kinetic drops. Settings and voice IDs live in [voices.json](voices.json); the tone descriptions below are Kujo creative direction, not a claim of an audition.

| Style | Voice | Delivery |
| --- | --- | --- |
| Cinematic hero | Brian | Deep, measured, cinematic |
| Apple-style micro | Sarah | Restrained, reassuring, minimal |
| Release notes | Daniel | Steady, articulate digest |
| Product proof reel | Chris | Conversational guide |
| Editorial thesis | George | Warm, thoughtful storyteller |
| Feature reveal | Jessica | Bright, friendly payoff |
| Integration | Eric | Smooth, assured handoff |
| Engineering / PR | Alice | Clear, educational explanation |
| Short product launch | Matilda | Professional, upbeat introduction |
| Kinetic drop | Liam | Energetic, concise announcement |

User overrides always win. The agent accepts ordinary requests such as “use George instead,” “use my saved voice named X,” or “use voice ID X.” Encode that choice in brief.json:

```json
{"voiceover": true, "voice": "George"}
```

```json
{
  "voiceover": true,
  "voice": {
    "voice_id": "USER_SELECTED_VOICE_ID",
    "name": "My voice",
    "direction": "Calm and conversational",
    "settings": {"speed": 0.95, "stability": 0.65}
  }
}
```

Replace USER_SELECTED_VOICE_ID with the actual alphanumeric provider ID. Precedence: explicit ID, explicit name, style default. Name matching for bundled defaults is case-insensitive. An unfamiliar name is preserved with `needs-name-resolution`, never silently replaced with a default. Resolve it against the account's current voice catalog before generation; ask only when multiple matches remain or the voice is unavailable. Never infer a voice ID from a person's name. User-selected existing licensed custom/cloned voices are accepted by ID; this does not request creating a clone.

Unspecified settings and delivery direction remain those of the selected video style even when the speaker changes. `voice.settings` can override stability, similarity_boost, style, use_speaker_boost and speed. The default model is eleven_multilingual_v2; an explicit model_id is passed through to the native workflow, which must check model/settings compatibility. Selection remains separate from `voiceover` so callers can retain a preferred speaker while exporting a silent version. Persist the caller's `voice` input; `resolved_voice` is derived on each normalization so changing styles does not accidentally pin the previous style's speaker.

`route` returns `resolved_voice`; `init` saves it in brief.json/BRIEF.md; `prepare` writes voiceover.json containing enabled, provider, ID/name, model, settings, direction and authored cues with start/end times. The native speech/mix workflow must consume that file instead of hardcoding Brian. It is a handoff contract, not a speech-generation command. Use provider-appropriate direction controls; never speak the direction text aloud or inject unsupported tags into multilingual-v2 narration. Include the actual voice ID/model/settings/text in generation receipts and cache keys so a speaker change cannot reuse old takes.

All ten IDs were returned by the configured account's read-only GET /v2/voices on 2026-09-08. No speech was generated or auditioned for this configuration change. Recheck voice availability before production, including saved custom voices; ElevenLabs documents upcoming default-voice changes in its [default voices guide](https://elevenlabs.io/docs/help-center/product/voices/my-voices/what-are-default-voices). An unavailable voice requires an explicit replacement decision; do not silently migrate speakers. Preserve generation-time licensing and existing credentials/authorization rules.
