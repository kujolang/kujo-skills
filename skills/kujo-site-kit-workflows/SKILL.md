---
name: kujo-site-kit-workflows
description: "Use this skill when building, validating, consuming, or maintaining SiteKit 1.0 design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, `dist/sitekit.js`, theme behavior, Tabler icon assets, accessibility checks, browser/release smoke tests, or Workcell evidence."
---

# Kujo Site Kit Workflows

This is the canonical hyphenated skill name for the `site-kit` repository. The older `kujo-sitekit-workflows` skill remains a compatibility alias; prefer this name for new launch-batch references. Use SiteKit 1.0 as a stable, source-vendored, AI-readable design system for accessible, semantic, token-driven websites and interfaces. Its supported consumer artifact is the generated `dist/` directory with fonts beside the CSS. Generated `DESIGN.md`, `css/generated/*`, `docs/components.md`, component manifests, and `dist/*` are distribution outputs unless the generator owns the change.

## Quick Start

```bash
SITEKIT_REPO="${SITEKIT_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/site-kit}"
cd "$SITEKIT_REPO"
npm run build
npm run lint
npm run validate
npm run snapshot
npm run smoke
npm run generated:check
npm run release:check
open examples/component-lab/index.html
git diff --check
```

## Launch Proof

For launch-batch work, run the native gate first, then Workcell when the local Docker image is available. The current local proof uses the pinned local Workcell base image and `--no-pull`:

```bash
workcell run --file docs/workcell-launch-gate.json --repo . --no-pull
workcell verify --run .workcell/runs/<run-id> --json
```

If Workcell cannot run because Docker or the pinned base image is unavailable, write a blocker receipt naming the failed command, host/Docker reason, closest native proof, and safe resume command.

## Boundaries

- SiteKit is stable at `1.0.0`, but still `private: true`; it ships as a source/dist release and not as an npm publication or hosted design-system deployment.
- The stable v1 contract covers tokens, themes, schemas, semantic templates, generated CSS/JS, layout recipes, documented progressive hooks, and representative static consumers.
- Browser/accessibility proof is representative unless the current Playwright Chromium, Firefox, and WebKit desktop/tablet/mobile release matrix is actually run.
- Preserve token, schema, semantic HTML, focus, and reduced-motion contracts.
- Do not hand-edit generated output when source generators own the change.
- Preserve the consumer distribution relationship: `dist/sitekit.css`, optional `dist/sitekit.js`, and sibling `dist/fonts/*`.
- Keep bundled Tabler icons, native scrollbar theming, the three supported themes, and full-screen mobile menu behavior aligned with README and generated manifests.

## Sources Consulted

- Status: repo-backed: `README.md`, `AGENTS.md`, `docs/launch-checklist.md`.
- Status: repo-backed: `docs/workcell-launch-gate.json`, `tests/browser/README.md`, `tests/browser/smoke.mjs`.
