---
name: kujo-sitekit-workflows
description: "Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts: tokens, component schemas/templates/CSS, layout recipes, generated `dist/sitekit.css`, optional `dist/sitekit.js`, `DESIGN.md`, accessibility/semantic standards, examples, snapshots, smoke tests, or SiteKit source/docs changes."
---

# Kujo SiteKit Workflows

Use SiteKit as the source-driven, AI-readable design system for accessible, semantic, token-driven websites and interfaces. Treat tokens, schemas, templates, component CSS, recipes, and standards as source of truth; generated outputs are distribution artifacts.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
SITEKIT_REPO="${SITEKIT_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/site-kit}"
cd "$SITEKIT_REPO"
npm run build
npm run lint
npm run validate
npm run snapshot
npm run smoke
open examples/component-lab/index.html
```

For consumers, preserve the distribution relationship:

```text
dist/sitekit.css
dist/sitekit.js
dist/fonts/*
```

## Workflow Notes

- The package is private/internal at `0.1.0`; consumers copy or vendor `dist/`, or use the repo as a local dependency. Do not imply npm publication.
- `npm run build` regenerates reset, primitive and semantic tokens, theme overrides, base styles, components, utilities, `dist/sitekit.css`, optional behavior JS, and font assets.
- `dist/sitekit.js` is optional progressive behavior for documented hooks: dropdowns, popovers, drawers, dialogs, tooltips, theme controls, and focus behavior.
- `css/generated/*` is useful for source inspection; consumers should not manually assemble generated CSS.
- Browser/accessibility testing is a separate pre-launch requirement for representative consuming layouts; package release checks alone are not proof for every site.
- Prefer existing components and tokens before adding page-specific styles or new primitives.

When reporting results, state the command, generated artifacts, changed source surfaces, validation output, and whether browser/accessibility review remains.

## SiteKit Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `DESIGN.md`
4. Relevant `standards/*.md`
5. Relevant `components/*/*.schema.json`, `.html`, `.css`, `.md`, and `examples.json`
6. Relevant `tokens/*.json` and `tokens/themes/*.json`
7. Relevant `recipes/*.json` and `layouts/*.html`
8. `scripts/build`, `scripts/validate-components`, `scripts/lint`, `scripts/snapshot-components`
9. `tests/` and `examples/`

Preserve semantic HTML, token usage, focus behavior, reduced-motion/accessibility constraints, component schemas, and distribution compatibility unless the user explicitly changes the design-system contract.

Run validation after source, docs, component, token, recipe, layout, or generated-distribution changes:

```bash
npm run build
npm run lint
npm run validate
npm run snapshot
npm run smoke
```

## Search And Safety

- Do not hand-edit `dist/`, `DESIGN.md`, or `css/generated/*` when the source generator should own the change.
- Do not introduce raw hex colors in component CSS when tokens exist.
- Do not remove focus styles, heading hierarchy, semantic elements, or documented behavior hooks.
- Keep `dist/fonts/*` beside `dist/sitekit.css` when packaging or copying output.

Use `rg` for broad searches and exclude generated distribution files unless the task targets distribution output.

## Sources Consulted

- Status: repo-backed: `README.md`, `AGENTS.md`, `DESIGN.md`, `docs/components.md`.
- Status: repo-backed: `components/`, `tokens/`, `recipes/`, `layouts/`, `standards/`, `scripts/`, `tests/`, `examples/`, `dist/README.md`.
