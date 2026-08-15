---
name: kujo-ecosystem-launch
description: "Use this skill when releasing a Kujo ecosystem tool, workflow, skill pack, or agent team and synchronizing its verified public web presence: implementation hardening, clean-install proof, version and changelog alignment, ShipCheck and repository gates, GitHub commit/tag/release operations, Kujolang.ai or agents.kujolang.ai catalog pages, Kujo dither heroes or agent portraits, Howl social cards, metadata/schema/sitemap/RSS/robots/llms.txt updates, SEO and AI-search auditing, deployment, live verification, or a release-only/site-only recovery pass."
---

# Kujo Ecosystem Launch

Coordinate an evidence-backed release-to-site launch. Invoke existing specialist skills and repository-owned commands in a fixed dependency order; do not duplicate their implementation guidance or claim unavailable checks passed.

## Establish The Launch Contract

1. Read every in-scope repository's `AGENTS.md`, release documentation, current version sources, tests, CI configuration, and recent history.
2. Record:
   - launch type: `tool`, `workflow`, `skill`, or `agent-team`;
   - source repositories and intended released commits;
   - release version and whether commit, tag, signing, push, and GitHub release are authorized;
   - target site repository and whether deployment is authorized;
   - visual mode: `dither`, `portraits`, `existing`, or `none`;
   - affected catalogs, navigation, counts, feeds, and discovery files;
   - required tests, clean-install proof, release gates, and live checks.
3. Run `scripts/launch_preflight.py` before editing. Treat its result as repository-state evidence, not release certification.
4. Read [release-gates.md](references/release-gates.md). Read [site-sync.md](references/site-sync.md) whenever site work is in scope. Then read only the matching launch variant:
   - [tool-launch.md](references/tool-launch.md)
   - [workflow-launch.md](references/workflow-launch.md)
   - [skill-launch.md](references/skill-launch.md)
   - [agent-team-launch.md](references/agent-team-launch.md)

Do not broaden release or deployment authority. A request to build is not authorization to tag, publish, deploy, mutate production, or rewrite an existing release.

## Execute The Stage-Gated Pipeline

### 1. Establish The Before Baseline

- Resolve the canonical repositories, current branch, remote, release/tag state, working-tree state, published site routes, and existing audit artifacts.
- Preserve an immutable before snapshot for SEO, performance, catalog counts, and live-route checks when the site is in scope.
- Derive public content from released or release-bound source artifacts, not memory or an unrelated working tree.

### 2. Harden And Prove The Product

- Invoke the narrowest domain skill plus `kujo-loop-engineering-workflows` for bounded changes.
- Run focused tests first, then the repository's complete required gates.
- Prove fresh-checkout or isolated installation when users will copy installation commands.
- Verify offline/fixture and live/provider boundaries honestly. Never present unconfigured adapters as working integrations.

### 3. Prepare And Publish The Release

- Invoke `kujo-release-gate-runner` and `kujo-shipcheck-workflows` where available.
- Align every authoritative version source, README badge, changelog, specification, eval fixture, install example, and release note.
- Commit small coherent changes. Re-run gates on the exact commit to be tagged.
- Create an annotated, signed tag when repository policy and configured signing support require it. Never rewrite an immutable published tag; issue a corrective release.
- Push the branch and tag, create the GitHub release, verify its target commit and required assets, and confirm CI.
- Stop site publication if no canonical released source exists unless the user explicitly authorized a documented preview.

### 4. Synchronize The Public Site

- Invoke `kujo-ssg-workflows` or the target site's canonical build skill.
- Add or update the correct catalog/detail/team pages, source links, navigation, cross-links, counts, and copy from the verified release.
- Keep general public copy version-agnostic. Use release-pinned versions in install commands, compatibility statements, release notes, or evidence where reproducibility requires them.
- Invoke `generate-kujo-dither-heroes` for Kujo ecosystem pages when installed, or the repository's approved visual workflow. Use ImageGen portrait generation for agent-team headshots. Do not substitute generic or reused art.
- Finalize hero or portrait assets before invoking `kujo-howl-workflows`; regenerate every dependent social card after visual changes.
- Update title/description metadata, canonicals, schema, sitemap, RSS/feeds, robots policy, `llms.txt`, and other repository-owned discovery surfaces.

### 5. Audit, Deploy, And Verify

- Build and validate generated output before deployment.
- Invoke `audit-seo-ai-search` when installed, preserving before/after evidence and clearly separating unavailable provider measurements.
- Invoke `kujo-lens-workflows` or browser QA for representative desktop/mobile routes, interactions, accessibility, links, images, and social previews.
- Deploy only with explicit authority and the repository-supported workflow.
- Verify every affected production route, release link, asset, catalog count, metadata surface, deployment result, and final working tree.
- Re-run `scripts/launch_preflight.py --require-clean --require-tag` for each released source repository when applicable.

## Stop Gates

- Stop release on failing required tests, an error-level ShipCheck gate, missing version alignment, unproven install commands, conflicting targets, unavailable publication authority, or missing required artifacts.
- Stop deployment on broken builds, missing/duplicate routes, incorrect counts, visual or social-card drift, broken links, metadata/schema/feed failures, or unverified production routing.
- Report unavailable external measurements as unavailable; do not convert them into passes or failures.
- Preserve unrelated user changes. Never force-push, rewrite history, delete release assets, or replace a repository target to make a launch appear complete.

## Final Launch Receipt

Return a compact receipt containing:

- launch type, source repositories, released commits, versions, tags, and release URLs;
- tests, clean-install proof, ShipCheck result, CI, signing, and artifact verification;
- site commits, affected routes, visual assets, Howl cards, metadata/discovery updates, audit reports, deployment, and live checks;
- deviations, unavailable checks, blockers, and exact follow-up;
- final branch/remote synchronization and clean-worktree state for every changed repository;
- Strata consolidation and SignalBox results required by repository instructions.

Do not call the launch complete until evidence proves every authorized stage and deliverable.
