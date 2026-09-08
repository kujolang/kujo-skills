---
name: release-notes-changelog
display_name: Release Notes / Changelog Film
priority: 3
typical_duration: 35-60s
best_for: weekly digest, version release, multi-feature update
base_workflow: changelog-video | product-launch-video | general-video
reference_projects:
  - HyperFrames changelog-video skill
---

# Release Notes / Changelog Film

## Job to be done

Convert release notes into a video people will actually watch.

The source may be:

- GitHub release
- changelog Markdown
- a date range of merged work
- multiple repo releases
- weekly Kujo ecosystem update

The final video must **visualize the release**, not read the release notes aloud.

## Editorial rule

Raw release notes are source material, not the script.

For every candidate change, ask:

1. Does this matter to the target viewer?
2. Can it be demonstrated visually?
3. What changed in the user's workflow?
4. What is the minimum context needed?
5. Is it important enough to survive the duration budget?

Small fixes may be grouped. Important changes get their own beat.

## Story selection

Rank release items:

- **Tier A — headline**: biggest user-facing change
- **Tier B — supporting**: 2–4 meaningful improvements
- **Tier C — rapid-fire**: small but useful fixes
- **Tier D — omit from video**: internal/no visual value

Do not force every changelog item into the video.

## Default arc

1. Release name/version/date
2. Headline feature
3. Supporting feature
4. Supporting feature
5. Rapid-fire fixes/improvements
6. CTA / install / upgrade

Alternative weekly arc:

1. “This week in Kujo”
2. biggest ecosystem change
3. 2–4 repo updates
4. reliability/performance fixes
5. what to try now

## Visual mapping

Map release-note language to proof:

| Release note | Preferred visualization |
|---|---|
| New UI feature | real UI capture |
| New CLI command | real terminal sequence |
| Performance improvement | benchmark or measured before/after |
| Bug fix | before/after reproduction if useful |
| New provider | provider selection -> successful result |
| New API | concise code usage -> output |
| Agent behavior | workflow trace / timeline |
| Internal refactor | omit unless user-facing effect exists |
| Security hardening | safe architecture/control visualization; avoid exposing exploit detail |

Never invent benchmark numbers.

## Narration

Narration should explain **impact**, not implementation trivia.

Bad:
“Version 0.8.3 adds normalize-audio, background previews, and several fixes.”

Better:
“Audio clips can now match loudness automatically, previews keep running while you work, and Studio deletes a full selection the way you expect.”

Still: show each claim.

## Motion and pacing

- Headline feature gets the longest beat.
- Smaller updates can accelerate.
- Use a consistent caption rail when narration is dense.
- Use recurring section markers so the viewer understands the digest.
- Avoid identical card transitions between every item.
- Reuse product-specific motion motifs.

## Automation requirements

The video-making skill should support:

```yaml
source:
  type: github_release | changelog_md | git_range | manual
  repo:
  version:
  from:
  to:
selection:
  max_headlines: 1
  max_supporting: 4
  include_fixes: true
  include_internal: false
```

The agent should generate an intermediate `RELEASE_SELECTION.md` containing:

- all source items
- tier assignment
- visualizability score
- inclusion decision
- source/evidence link
- proposed visual

This makes the selection auditable.

## QA requirements

- every included change maps back to source text
- no omitted item is accidentally described as included
- version/date are correct
- terminal/UI recordings match released behavior
- benchmark claims are sourced
- captions do not cover critical UI
- scenes do not feel like a slide deck
- the video remains useful even if the viewer never opens the full changelog

## Acceptance criteria

- <=1 headline feature
- <=4 supporting features unless duration is increased
- actual proof for all Tier A/B items where feasible
- no narrated bullet list
- no fabricated UI
- no invented metrics
- release/version visible but not allowed to dominate the opening
- ending contains one next action

## Reference study

HyperFrames' repo-local changelog workflow is explicitly designed to turn weekly changelog Markdown into a roughly 45–60 second branded film with VO, captions, seam checks, and validation.

Reference:
https://github.com/heygen-com/hyperframes/blob/main/.agents/skills/README.md

The implementation should integrate with the current HyperFrames changelog workflow when available rather than reimplementing its validation stack.
