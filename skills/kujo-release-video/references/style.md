# The trust-at-speed recipe

Reference: `kujo-hyperframes/trust-at-speed`, complete audio edition at commit `1b16d33`. Bundled source is a generalized derivative, not a screenshot or embedded reference video.

Paper #f9f9f9, ink #060606, Departure Mono, official Kujo SVG, generous negative space. One shared 1920×1080 stage. Keep the product name and version legible; the Kujo mark identifies the ecosystem and must not be represented as a different product's unique logo.

| Time | Function | Motion / audio |
| --- | --- | --- |
| 0–1.5 | Product/version recognition | Quiet brand pulse and ordered pixel field; low tonal pulse |
| 1.5–2.75 | One clear reason to care | Ink cut, large two-line type with quick directional entry; transition air |
| 2.75–5.65 | Concrete use or change | Bordered task/command screen scales in, modest camera push, typed input, cursor click |
| 5.65–8.6 | How the change works | Five sequential steps or attributes; rising interface pings |
| 8.6–11.8 | Evidence or outcomes | Ink proof screen, three spaced check reveals, confirmation tones |
| 11.8–15 | Name, version, next step | Thin aperture contracts into the opening lockup; restrained chord and final hold |

The five rows are a layout, not a requirement that every tool has an agent loop. They can decompose one improvement into input → action → intermediate state → output → finish. Do not invent five features to fill them. Likewise, three proof rows can be documented capabilities or changes; a drawn check does not imply an actual evaluation passed. When release evidence is sparse, simplify copy and use illustration labeling.

Short copy and voice work together. Aim for roughly 28–38 spoken words overall, with intentional gaps for the click and confirmations. Avoid reading version numbers or commands aloud unless that helps the viewer. Write a pronunciation alias for ambiguous tool names in `spoken_text`; keep public spelling in `text`. Use natural phrasing, not release-note bullet fragments spoken as a list.

96 BPM ambient sine pads and quiet arpeggio; dry short clicks; no large trailer drums or incessant whooshes. Voice-following carve returns the music between sentences. Master near −16 LUFS, peak below −1 dBTP after AAC. Keep original takes and separate stems; trim with handles, never cut off a word to satisfy the runtime.

The entire animation is a paused seekable GSAP timeline. Initial states, character reveals and later state changes must remain deterministic in reverse/random seeks. Keep the opening and final frame matching. Preview and export use the same master WAV. Changes to typography and labels still require layout checks and frame inspection.

Visual reference: [validated preset contact sheet](../assets/style-contact-sheet.jpg).
