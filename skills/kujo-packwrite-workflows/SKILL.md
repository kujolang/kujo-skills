---
name: kujo-packwrite-workflows
description: "Use this skill when generating, validating, reviewing, or maintaining PackWrite agent execution packs: `packwrite init`, `validate`, `prompt`, `config`, `doctor`, `packwrite.toml`, `MEGA_PROMPT.md`, generated `agent/` packs, model/provider setup, offline fake-response tests, or PackWrite CLI/source changes."
---

# Kujo PackWrite Workflows

Use PackWrite as a local-first workflow-pack compiler. It turns a repo-level
`MEGA_PROMPT.md` into a deterministic, validated `agent/` pack that downstream
implementation and review agents can follow. PackWrite does not implement the
project itself.

Canonical local source is usually
`/Users/robertdevore/2026/Kujolang/kujo-repos/packwrite`. Do not confuse
PackWrite with neighboring Kujo tools such as Muzzle, RunLedger, Eval, Spec, or
ChangeBucket. Muzzle runs quiet workflows, RunLedger records agent-run receipts,
Eval runs deterministic outcome checks, Spec defines task contracts, ChangeBucket
measures change footprint, and PackWrite compiles prompt/context into an
execution pack.

## Agent Workflow

1. Verify the Kujo runtime and launcher:

```bash
kujo --help
packwrite --help
packwrite version
```

If `packwrite` is not on `PATH`, run it from the repo with
`KUJO=/path/to/kujo /path/to/packwrite/bin/packwrite ...`. If `kujo` is not on
`PATH`, set `KUJO` to the interpreter path before using the launcher.

2. In the target repo, create or inspect the mega prompt:

```bash
cd /path/to/project
$EDITOR MEGA_PROMPT.md
```

A good mega prompt describes purpose, target users, use cases, non-goals,
architecture principles, guardrails, and definition of done. It does not need a
formal schema.

3. Check setup before spending a model call:

```bash
packwrite doctor
packwrite config
```

API keys come from environment variables only. Prefer `PACKWRITE_API_KEY`; provider
fallbacks include `DEEPSEEK_API_KEY`, `OPENAI_API_KEY`, and `ANTHROPIC_API_KEY`.
Never place keys in `packwrite.toml`, prompts, logs, examples, or committed files.

4. Preview, generate, and validate the pack:

```bash
packwrite init MEGA_PROMPT.md --dry-run
packwrite init MEGA_PROMPT.md --provider deepseek --model deepseek-v4-pro
packwrite validate
```

Use `--overwrite` only when replacing an existing output pack intentionally.
`--overwrite` performs a clean replace and prunes stale files. Use `--output <dir>`
to compare multiple packs manually.

5. Hand off to agents:

```bash
packwrite prompt deepseek
packwrite prompt codex-review
```

`prompt deepseek` prints the implementation-agent prompt. `prompt codex-review`
prints the independent reviewer prompt. These commands print verbatim prompt text
so they can be piped or pasted cleanly.

## Generated Pack Shape

Default output is `agent/`:

```text
agent/
  MASTER.md
  TODO.md
  HANDOFF.md
  DECISIONS.md
  REVIEW_CHECKLIST.md
  DEEPSEEK_START.md
  CODEX_REVIEW_PROMPT.md
  phases/
    00-project-brief.md
    01-<slug>.md
```

- `MASTER.md` holds stable intent and assumptions.
- `TODO.md` tracks phase completion and links phase files.
- `HANDOFF.md`, `DECISIONS.md`, and `REVIEW_CHECKLIST.md` are mutable run state.
- `phases/*.md` hold scoped phase specs, acceptance criteria, and suggested checks.
- Optional files are controlled by `[pack]` config toggles and must stay aligned
  with validation requirements.

Treat generated `agent/` packs as project artifacts. Do not silently rewrite or
delete one unless the user asks or passed `--overwrite`.

## Configuration

Resolution order is:

```text
defaults < global config < project packwrite.toml < CLI flags
```

Project config is `packwrite.toml`; global config is
`~/.config/packwrite/config.toml`. Active sections are `[prompt]`, `[output]`,
`[model]`, `[repo_context]`, and `[pack]`.

Common config:

```toml
[prompt]
file = "MEGA_PROMPT.md"

[output]
dir = "agent"
overwrite = false

[model]
provider = "deepseek"
model = "deepseek-v4-pro"
temperature = 0.1

[pack]
min_phases = 6
max_phases = 12
include_deepseek_prompt = true
include_codex_review_prompt = true
include_review_checklist = true
```

`[output].mode` and `--run-name` are reserved/deferred and should be documented as
such if touched. Provider presets exist for `deepseek`, `openai`, and `local`.
Other providers need an OpenAI-compatible chat-completions `--endpoint`.
Anthropic is not supported natively unless routed through an OpenAI-compatible
gateway.

## Safety And Privacy

- PackWrite sends a lightweight repo summary to the model, not full file contents.
- Default context collection skips dependency/build directories and secret-looking
  paths such as `.env*`, keys, PEM files, and names containing `secret` or `token`.
- Writes are sandboxed to the output directory; absolute, `..`, and escaping paths
  in model manifests are rejected.
- Model output must parse to JSON with a non-empty `files` array of `{path, content}`
  string pairs. Surrounding prose and fenced code blocks may be stripped, but there
  is no Markdown fallback parser.
- Use `--debug` or `PACKWRITE_DEBUG=1` for sanitized diagnostics. Use
  `--save-raw-response <file>` only intentionally because raw model responses may
  contain sensitive data.

## Offline And CI Usage

Use the fake-response seam to run PackWrite without a provider, API key, or network:

```bash
export PACKWRITE_FAKE_RESPONSE_FILE=/path/to/manifest.json
packwrite init MEGA_PROMPT.md
```

`PACKWRITE_FAKE_RESPONSE` also accepts an inline manifest string. This seam is used
by PackWrite's own tests and should stay fully offline.

## Maintaining PackWrite

Source map:

- `packwrite.kujo`: entry point.
- `bin/packwrite`: launcher wrapper.
- `src/cli.kujo`: command parsing, user-facing output, exit codes.
- `src/config.kujo`: layered config and TOML loading.
- `src/prompt.kujo`: mega-prompt discovery and reading.
- `src/repo_context.kujo`: safe repo summary collection.
- `src/ai.kujo`: OpenAI-compatible model adapter and distillation prompt.
- `src/pack.kujo`: manifest parsing, path safety, clean replace, dry runs.
- `src/validate.kujo`: deterministic pack validation.
- `src/errors.kujo`: result envelopes and canonical messages.
- `src/util.kujo`: predicates, char-safe string helpers, safe file helpers.
- `AGENTS.md`, `README.md`, `docs/HOWTO.md`, and `packwrite.example.toml`:
  canonical copyable guidance.

Preserve exact CLI output, prompt text, exit codes, JSON/config shapes, validation
rules, and examples unless intentionally changing the contract and updating tests.
All runtime output goes to stdout; use greppable prefixes such as `warning`, `!`,
`note:`, and `error:` when adding output.

Kujo runtime constraints that matter in this repo:

- Use `while` loops; `kujo check` rejects more than one `for` loop per function scope.
- Do not use `import ... as`.
- Do not trust raw `parse_json` or `parse_toml`; guard and type-check parsed values.
- Do not mix byte-based `len`/`index_of` with char-based `substring`; use helpers in
  `src/util.kujo`.
- Use `util.write_text` instead of raw overwrite writes.
- Keep library modules quiet; only `src/cli.kujo` prints and maps results to exit
  codes `0`, `1`, or `2`.

Validate changes with:

```bash
make check
make test
KUJO=/path/to/kujo ./tests/run.sh
```

`make test` runs `kujo check` plus the offline unit and CLI integration suite. For
CLI behavior changes, update `tests/cli_integration.sh` and any copyable docs after
inspecting the intended output.

## Search Hygiene

For broad searches, start with:

```bash
rg "pattern" src README.md docs AGENTS.md CONTRIBUTING.md packwrite.example.toml
```

Exclude generated or bulky paths such as `agent/`, `.git/`, `target/`, `dist/`,
`build/`, `coverage/`, `node_modules/`, and `.venv/` unless the task explicitly
targets them. Treat `tests/fixture.kujo`, `tests/packwrite_test.kujo`, and
`tests/cli_integration.sh` as behavior contracts, not style examples.
