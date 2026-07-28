---
name: kujo-site-kit-workflows
description: "Use this skill when building, validating, consuming, or maintaining SiteKit design-system artifacts in the `site-kit` repository: tokens, component schemas/templates/CSS, generated `dist/sitekit.css`, optional `dist/sitekit.js`, accessibility checks, browser smoke tests, launch checklist, or Workcell evidence."
---

# Kujo Site Kit Workflows

This is the canonical hyphenated skill name for the `site-kit` repository. The older `kujo-sitekit-workflows` skill remains a compatibility alias; prefer this name for new launch-batch references.

## Quick Start

```bash
SITEKIT_REPO="${SITEKIT_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/site-kit}"
cd "$SITEKIT_REPO"
npm run build
npm run lint
npm run validate
npm run snapshot
npm run smoke
git diff --check
```

## Launch Proof

For launch-batch work, run the native gate first, then Workcell when the local Docker image is available:

```bash
workcell run --file docs/workcell-launch-gate.json --repo .
workcell verify --run .workcell/runs/<run-id> --json
```

If Workcell cannot run because Docker or the pinned base image is unavailable, write a blocker receipt naming the failed command, host/Docker reason, closest native proof, and safe resume command.

## Boundaries

- SiteKit is private/internal at `0.1.0`; do not imply npm publication or hosted design-system deployment.
- Browser/accessibility proof is local and representative unless a broader device/browser matrix is actually run.
- Preserve token, schema, semantic HTML, focus, and reduced-motion contracts.
- Do not hand-edit generated output when source generators own the change.
