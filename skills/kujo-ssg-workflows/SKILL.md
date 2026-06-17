---
name: kujo-ssg-workflows
description: "Use this skill when building, validating, configuring, testing, or maintaining the Kujo SSG static-site showcase: `build.kujo`, starter content, templates, assets, `kujo-ssg.yml`, feeds, sitemap, robots, `llms.txt`, generated `output/`, CLI flags, validation scripts, release gates, or `ssg` source/docs changes."
---

# Kujo SSG Workflows

Use SSG for deterministic Kujo static-site generation with visible content, templates, assets, metadata, feeds, and release validation.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
SSG_REPO="${SSG_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/ssg}"
cd "${SSG_REPO}"
kujo run ./build.kujo -- --site-url https://example.com
kujo serve output --port 8080
kujo run ./build.kujo -- --init yml
bash scripts/validate-generated-output.sh output
```

## Workflow Notes

- Generated site output goes under `output/`; do not hand-edit it.
- `build.kujo`, `kujo-ssg.yml`, `templates/`, and `content/` are canonical implementation/example surfaces.
- Validation checks generated routes, feeds, metadata, and release contract behavior.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo SSG Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `build.kujo`
4. `kujo-ssg.yml`
5. `templates/`
6. `content/`
7. `scripts/test-cli-contract.sh`
8. `scripts/test-generated-contract.sh`
9. `scripts/run_ci_checks.sh`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
kujo run ./build.kujo -- --site-url https://example.com
bash scripts/validate-generated-output.sh output
bash scripts/run_ci_checks.sh
bash scripts/run_release_gate.sh
```

## Search And Safety

- Exclude `output/`, vendor assets, fonts, images, static bulk, and `tmp/` unless targeted.
- Preserve CLI output spacing and wording unless changing contracts intentionally.
- Use the VM path `kujo run ./build.kujo -- ...` for validated execution.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `build.kujo`.
- Status: repo-backed: `scripts/run_ci_checks.sh`.
