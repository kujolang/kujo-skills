---
name: kujo-ssg-workflows
description: "Use this skill when building, validating, configuring, testing, or maintaining the Kujo SSG static-site showcase: `build.kujo`, starter content, templates, assets, `kujo-ssg.yml`, feeds, sitemap, robots, `llms.txt`, generated `output/`, CLI flags, parallel shard builds, DocGen docs bridge, reusable docs starter, experimental static WebMCP, local Ability pack, validation scripts, release gates, or `ssg` source/docs changes."
---

# Kujo SSG Workflows

Use SSG for deterministic Kujo static-site generation with visible content, templates, assets, metadata, feeds, optional WebMCP browser-agent artifacts, a local Ability pack, and release validation.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
SSG_REPO="${SSG_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/ssg}"
cd "${SSG_REPO}"
kujo run ./build.kujo -- --site-url https://example.com
kujo serve output --port 8080
kujo run ./build.kujo -- --init yml
kujo run ./build.kujo -- --site-url https://example.com --drafts --no-aliases --posts-at-root
kujo run ./build.kujo -- --site-url https://example.com --download-remote-images
kujo run ./build.kujo -- --site-url https://example.com --webmcp
KUJO_BIN=/path/to/kujo bash scripts/build-parallel.sh auto auto --content content --output output --site-url https://example.com --posts-per-page 25
kujo run scripts/docgen_ssg_bridge.kujo -- --target-repo /path/to/repo --content-out content/reference --docgen-out .docgen/output --cache-dir .docgen/cache --site-url https://docs.example.com --strict
bash scripts/package-docs-template.sh
bash scripts/validate-generated-output.sh output
kennel validate
kujo run tests/ability_pack_tests.kujo --interpreter
KUJO_BIN="$(command -v kujo)" bash scripts/test-ability-pack-integration.sh
```

## Workflow Notes

- Generated site output goes under `output/`; do not hand-edit it.
- `build.kujo`, `kujo-ssg.yml`, `templates/`, and `content/` are canonical implementation/example surfaces.
- Validation checks generated routes, feeds, metadata, docs contracts, and release contract behavior.
- Config discovery prefers `kujo-ssg.yml`, then `kujo-ssg.yaml`, then `kujo-ssg.json`; CLI flags override config values.
- Draft content is excluded by default. Use `--drafts` only for preview/staging builds, and `--no-aliases` to skip flat `.html` redirect aliases for lower large-site write I/O.
- Use `--posts-at-root` when post permalinks must remain at `/<slug>/` while the blog listing stays under `/<blog_slug>/`.
- Use `--download-remote-images` only when remote `featured_image` mirroring is required and network capability is deliberately enabled; local featured-image paths are checked against approved content/assets roots.
- Custom collections under `content/<type>/*.md` generate `/<type>/<slug>/` routes, per-type listing pages, taxonomy sections, and public `llms.txt` collection entries.
- `scripts/docgen_ssg_bridge.kujo` converts stable `docgen-summary/v1` output into manifest-tracked Markdown, refuses paths escaping the SSG root, and can run the build/validation gates unless `--skip-build` or `--skip-validation` is explicit.
- `starters/docs-site/` packages a reusable docs starter with docs templates, local search, generated-reference update automation, and local assets.
- Use `--no-aux` when the build only needs page/item routes and should skip feed, sitemap, robots, and `llms.txt`.
- Use `--webmcp` only for the experimental static WebMCP v1 build target. It emits `output/.well-known/kujo-site-index.json`, `output/assets/js/kujo-webmcp.js`, and minified JS when `--minify` is enabled; drafts and arbitrary metadata must never enter the agent index.
- WebMCP registers exactly `get_site_info`, `search_site`, `list_content`, and `get_content` through `document.modelContext`; it is same-origin, public-content-only, read-only, and separate from Kujo Ability.
- The local Ability pack under `abilities/` covers project inspection, bounded source listing, generated-output validation, approval-gated/idempotent builds, output comparison, deployment readiness, and deterministic artifact export. It does not publish or deploy.
- Absolute `--output` paths are supported by the current CLI contract; verify generated output paths deliberately before deleting or publishing.
- The current render hot path delegates to native Kujo builtins: `escape_xml`, `render_markdown`, `render_layout_native`, and `render_listing_card`. Keep byte-identical behavior against the interpreted helpers when touching these paths.
- Large sites can use `scripts/build-parallel.sh <shards|auto> <concurrency|auto> [build args...]`; it drives `build.kujo --phase setup|posts|finalize` and `--shard i --shards N`, with byte-identical output except sitemap URL order.
- Remaining performance work is in-repo SSG work, especially frontmatter parsing and listing finalization, unless runtime evidence shows a Kujo VM regression.

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
10. `scripts/docgen_ssg_bridge.kujo`, `scripts/update_docs.kujo`, and `starters/docs-site/` when docs bridge or starter behavior changes
11. `docs/webmcp.md`, `scripts/test-webmcp-runtime.js`, and WebMCP fixtures when browser-agent output changes
12. `docs/ability-integration.md`, `abilities/`, `kennel.toml`, `kennel.lock`, and Ability tests when host Ability behavior changes

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
kujo run ./build.kujo -- --site-url https://example.com
bash scripts/validate-generated-output.sh output
bash scripts/test-cli-contract.sh
bash scripts/test-docs-contract.sh
bash scripts/test-docgen-ssg-bridge.sh
bash scripts/test-docs-template.sh
node scripts/test-webmcp-runtime.js
kujo run tests/ability_pack_tests.kujo --interpreter
KUJO_BIN="$(command -v kujo)" bash scripts/test-ability-pack-integration.sh
bash scripts/run_ci_checks.sh
bash scripts/run_release_gate.sh
```

## Search And Safety

- Exclude `output/`, vendor assets, fonts, images, static bulk, and `tmp/` unless targeted.
- Preserve CLI output spacing and wording unless changing contracts intentionally.
- Use the VM path `kujo run ./build.kujo -- ...` for validated execution.
- Do not replace the native render fast path with slower interpreted string assembly unless the change is explicitly scoped and benchmarked.
- Keep static WebMCP progressive, opt-in, public-only, and independent from authenticated Ability operations.
- Do not add deploy authority to the SSG Ability pack; deployment belongs to a separately versioned provider-owned pack.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `build.kujo`.
- Status: repo-backed: `docs/current-capability-matrix.md`, `docs/performance-findings.md`, `docs/webmcp.md`, `docs/ability-integration.md`, `scripts/build-parallel.sh`, `scripts/docgen_ssg_bridge.kujo`, `scripts/update_docs.kujo`, `scripts/package-docs-template.sh`, `scripts/test-cli-contract.sh`, `scripts/test-docs-contract.sh`, `scripts/test-docgen-ssg-bridge.sh`, `scripts/test-docs-template.sh`, `scripts/test-webmcp-runtime.js`, `scripts/test-ability-pack-integration.sh`, `scripts/run_ci_checks.sh`.
