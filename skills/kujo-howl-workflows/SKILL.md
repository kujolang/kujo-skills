---
name: kujo-howl-workflows
description: "Use this skill when creating, validating, rendering, reviewing, or maintaining Howl showcase artifacts for Kujo examples: `howl init`, `howl validate`, `howl list`, `howl show`, `howl caption`, `howl render`, `howl.json`, `examples/*.kujo`, `dist/howl/`, deterministic SVG/Markdown/HTML cards, static galleries, social captions, or Howl CLI/source/test changes."
---

# Kujo Howl Workflows

Use Howl to turn real Kujo examples plus manifest metadata into deterministic, reviewable showcase artifacts: SVG cards, Markdown snippets, standalone HTML pages, and a static gallery.

## Agent Workflow

- Check setup with `howl help` or `KUJO=/path/to/kujo/target/release/kujo ./bin/howl help`.
- Prefer `howl validate` before rendering, committing artifacts, or editing showcase metadata.
- Use `howl list` to discover card ids, then `howl show <id>` to inspect the manifest metadata and code preview.
- Use `howl caption <id>` for deterministic share copy, and `howl caption <id> --platform x` for the X.com-bounded variant.
- Use `howl render` to regenerate `dist/howl/`, or `howl render --out <dir> --format svg|html|markdown` for targeted output.
- After edits, rerun validation and inspect generated artifacts by diffing text output, opening `dist/howl/index.html`, or grepping rendered HTML/SVG for escaping-sensitive content.

## Project Setup

```bash
cd /path/to/project
howl init
howl validate
howl list
howl render
```

`howl init` creates `howl.json` and `examples/clear-intent.kujo` without overwriting existing files unless `--force` is passed. The default render output is `dist/howl/`; treat it as generated unless the repo intentionally commits showcase artifacts.

When `howl` is not on `PATH`, run the bundled launcher from the Howl repo:

```bash
export KUJO=/path/to/kujo/target/release/kujo
/path/to/howl/bin/howl validate --manifest ./howl.json
```

The launcher preserves the caller's working directory, so manifests and output paths resolve relative to where the command is invoked.

## Manifest Pattern

Use `howl.json` as the source of truth. Required card fields are `id`, `title`, and `file`; optional fields include `tagline`, `language`, `concepts`, `expected_output`, `caption`, `cta`, `notes`, `url`, and `variant`.

```json
{
  "project": {
    "name": "Kujo",
    "tagline": "Programming language for AI-native software",
    "url": ""
  },
  "theme": { "name": "minimal", "mode": "light" },
  "cards": [
    {
      "id": "clear-intent",
      "title": "Clear intent over boilerplate",
      "tagline": "Kujo favors code that humans and agents can continue safely.",
      "file": "examples/clear-intent.kujo",
      "language": "kujo",
      "concepts": ["clear intent", "agent-readable code", "low-noise syntax"],
      "expected_output": "Ready, agent",
      "caption": "AI-native software needs code that explains intent without burying it in ceremony.",
      "cta": "Kujo: programming language for AI-native software."
    }
  ]
}
```

Keep `file` paths relative to the manifest directory. Howl rejects paths that escape that tree. Keep examples small, copyable, and truthful; Howl renders text and does not run or type-check the referenced examples.

## Artifact Contracts

`howl render` writes:

- `<id>.md`: portable Markdown for READMEs, blogs, GitHub discussions, and release notes.
- `<id>.html`: standalone HTML with embedded CSS and no remote assets.
- `<id>.svg`: 1600x900 social card using system fonts and escaped card content.
- `index.html`: static gallery linking each card's artifacts.

Preserve these contracts unless the user explicitly asks for a breaking change. If output layout or escaping changes, inspect generated `.html` and `.svg` artifacts, not just tests.

## CLI Contracts

- Commands: `init`, `validate`, `list`, `show <id>`, `caption <id>`, `render`, `help`, `version`.
- Shared options: `--manifest PATH`.
- Render options: `--out DIR`, `--format all|svg|html|markdown`, `--max-code-lines N`, `--max-output-lines N`.
- Caption option: `--platform x`.
- Init option: `--force`.
- Exit code `0`: success.
- Exit code `1`: usage error, invalid manifest, unknown command, or other user-facing failure.

Prefer clear, itemized validation errors that report every manifest problem at once.

## Safety And Scope

- Howl is offline and deterministic. Do not add network calls, LLM calls, telemetry, posting, scheduling, or package-registry dependencies.
- Howl must not invent claims. Render only manifest fields and referenced example text.
- Escape all card-derived content before writing HTML or SVG.
- Keep manifest file paths contained under the manifest directory.
- Do not turn Howl into a docs-site generator, linter, reviewer, web framework, or social poster.
- Keep generated `dist/howl/` and `tmp_test_*/` out of broad searches unless the task explicitly targets them.

## Howl Repo Work

- Read in this order: `README.md`, `AGENTS.md`, `src/cli.kujo`, `src/manifest.kujo`, `src/render_svg.kujo`, `tests/howl_test.kujo`.
- Use default search exclusions: `rg "term" --glob '!dist/**' --glob '!tmp_test_*/**'`.
- Preserve the Kujo dialect already used in Howl: `func`, `export func`, `:=`, `mut`, `has_key(...) == 1`, index-based `while` loops, and reassignment after `push`.
- Keep `src/cli.kujo` as the only argv/stdout/filesystem dispatch layer. Renderers should stay pure functions from `(card, project)` to string.
- Use `write_out` for generated files because `write_file` refuses to overwrite in the VM.
- Prioritize canonical examples in `examples/*.kujo`, `howl.json`, README snippets, and starter manifest text over test fixtures when improving copyable examples.

## Verification

For Howl source changes:

```bash
export KUJO=/path/to/kujo/target/release/kujo
for f in src/*.kujo howl.kujo tests/howl_test.kujo; do
  "$KUJO" check "$f" || exit 1
done
./tests/run.sh
```

For end-to-end behavior:

```bash
T=$(mktemp -d) && cd "$T" && \
  /path/to/howl/bin/howl init && \
  /path/to/howl/bin/howl validate && \
  /path/to/howl/bin/howl render && \
  ls dist/howl/
```

For committed generated artifacts, regenerate and run `git diff --exit-code dist/howl`.

## Sources Consulted

- Status: repo-backed: Howl `README.md`, `AGENTS.md`, `src/cli.kujo`.
- Status: repo-backed: `src/manifest.kujo`, `src/render_svg.kujo`, `tests/howl_test.kujo`.
