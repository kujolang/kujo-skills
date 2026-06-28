---
name: kujo-docgen-agent-readable
description: Use this skill when working on Kujo DocGen/DocsGen (`kujo docgen`), generated documentation, docs-as-contract surfaces, agent-readable JSON/gap outputs, documentation coverage gates, public-only docs gates, link validation, adapter extraction, README/reference alignment, or example smoke policy.
---

# Kujo DocGen And DocsGen Workflows

DocGen, sometimes requested as DocsGen, is Kujo's universal documentation generator. Treat it as a compatibility, safety, and agent-readability surface, not just prose generation.

## First Moves

1. Read the target repo's `README.md`, `AGENTS.md` if present, `docs/DOCGEN.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, relevant tests, and any generated-doc policy before changing behavior.
2. Determine whether the task is CLI contract work, adapter extraction, generated-doc refresh, gap remediation, link validation, public-only coverage, or docs/example alignment.
3. Use the narrow companion skill when needed:
   - `kujo-cli-contracts` for `--json` payload compatibility, stdout/stderr, exit codes, and breaking-change review.
   - `kujo-docgen-public-docs-refresh` for regenerating committed/public docs after drift evidence.
   - `kujo-language-implementation` for broader Rust compiler/runtime changes outside `src/docgen`.
4. Keep generated docs and JSON deterministic. Do not introduce source execution, imports/build steps, external AI calls, or unbounded network validation into DocGen.

## Architecture Map

`kujo docgen` is model-driven and adapter-based:

- CLI wiring and flags: `src/main.rs`.
- core orchestration, output writing, gates, cache, and typed CLI JSON builder: `src/docgen/core.rs`.
- safe deterministic file discovery: `src/docgen/discovery.rs`.
- shared project/module/symbol/gap model: `src/docgen/model.rs`.
- missing-doc and link-gap analysis: `src/docgen/gaps.rs`.
- HTML, Markdown, and JSON renderers: `src/docgen/render/*`.
- language adapters: `src/docgen/adapters/*`.
- legacy/helper wrapper surface: `src/doc_generator.rs`.

Supported languages in the current Kujo repo documentation are Kujo, PHP, Python, TypeScript, JavaScript, Ruby, Go, Haskell, and Zig. Prefer changing shared adapter helpers in `src/docgen/adapters/common.rs` only when behavior is truly common; otherwise keep adapter-specific extraction semantics local and fixture-backed.

## Safety Model

DocGen is scan-only:

- no source execution
- no imports or build steps
- no external AI calls by default
- symlink traversal skipped during discovery
- file size, directory depth, and file count limits enforced
- deterministic ordering for CI-stable output
- HTML escaping for documentation content

External link validation is opt-in. When enabling it, require an explicit allowlist, preserve redirect allowlist confinement, block private/loopback/link-local/multicast targets unless intentionally opted in, and use link-check/time budgets for bounded CI behavior.

## CLI Patterns

```bash
kujo docgen src/ --language kujo --out-dir docs/generated
kujo docgen . --out-dir docs/generated
kujo docgen . --languages kujo,php,python,typescript,javascript,ruby,go,haskell,zig --out-dir docs/generated
kujo docgen . --public-only --fail-on-undocumented --fail-on-broken-links --json
kujo docgen . --emit-ai-tasks --out-dir docs/generated
kujo docgen . --format json --json --out-dir docs/generated
kujo docgen . --cache-dir .docgen-cache --json
```

Useful flags include:

- output: `--format html|markdown|json|all`, `--out-dir`, `--no-builtins`, `--search-index`.
- language selection: `--language`, `--languages`.
- gates: `--public-only`, `--include-private`, `--fail-on-undocumented`, `--fail-on-broken-links`, `--fail-on-warnings`.
- links: `--source-links`, `--source-link-template`, `--validate-local-anchors`, `--validate-external-links`, `--external-link-allowlist`, `--allow-private-network-links`, `--external-link-timeout-ms`, `--max-link-checks`, `--max-external-link-checks`, `--max-total-validation-time-ms`.
- discovery and performance: `--max-discovery-file-size-bytes`, `--max-discovery-files`, `--max-discovery-depth`, `--cache-dir`.
- Kujo extraction: `--kujo-parser-assisted`, which remains opt-in and must fall back gracefully to regex extraction on lexer/parser diagnostics.
- machine output: `--json`.

Discovery limits can also come from `KUJO_DOCGEN_MAX_FILE_SIZE_BYTES`, `KUJO_DOCGEN_MAX_FILES`, and `KUJO_DOCGEN_MAX_DEPTH`; CLI flags take precedence over environment values.

## Outputs And Contracts

The output directory can include:

- `index.html`
- `docgen.md`
- `docgen.json`
- `docgen-gaps.json`
- `docgen-capabilities.json`
- `docgen-ai-tasks.md` when `--emit-ai-tasks` is used
- `builtins.html` unless `--no-builtins` is used
- `search-index.json` and `symbol-index.json` when `--search-index` is used

`kujo docgen --json` is a stable CLI contract. Emit it from `src/docgen/core.rs::build_cli_json_payload`, preserve existing top-level fields, and update `docs/CLI_MACHINE_READABLE_CONTRACTS.md` plus `tests/cli_json_contracts.rs` for shape changes.

Important payload surfaces include:

- `command`, `file`, `output_dir`, generated output paths, and `languages`.
- `item_count`, `project_symbol_count`, `builtin_symbol_count`, and `symbol_kind_counts`.
- `diagnostics_count`, `undocumented_count`, `broken_link_count`, `warning_count`, and `gate_failures`.
- `adapter_health` with files scanned, symbols extracted, doc blocks attached, and placeholders emitted.
- `cache_stats` with hits and misses.
- `discovery_skip_counts`, `discovery_limits`, and `link_validation_skip_counts`.
- `summary.schema_version` set to `docgen-summary/v1`, mirroring key totals for dashboards and agents.

With `--json`, gate failures should still be represented in the payload so automation can inspect them. Preserve stdout/stderr policy from `kujo-cli-contracts`.

## Kujo Extraction Rules

Kujo DocGen currently recognizes `///`, `//!`, and `/** ... */` doc comments. Non-doc block comments are not API documentation. Attachment is decorator-aware: skip `@...` and `#[...]` lines between doc comments and the target symbol. Blank lines may appear between a doc block and symbol; ordinary non-doc comments break attachment; nearest eligible docs win.

Kujo visibility is explicit and gate-oriented:

- top-level `pub func`, `pub struct`, `pub enum`, `pub const`, and `pub let` are public.
- non-`pub` top-level symbols are private.
- struct methods are public only when the method is `pub` and the containing struct is public.
- enum variants inherit visibility from the containing enum.
- `--public-only` with `--include-private` disabled is the strict public API gate surface.

Keep the default Kujo extraction path resilient and regex-based. Parser-assisted extraction is an opt-in prototype path with deterministic regex fallback. Any promotion or behavior change needs fixture-backed coverage for parser success, parser fallback, ordering, and strict gate stability.

## Documentation Rules

- Treat docs, examples, and generated JSON as agent-consumed surfaces.
- Do not invent behavior in generated AI task prompts; mark uncertainty.
- Keep README, language spec, standard library reference, and tests aligned.
- Public-only DocGen gates depend on explicit `pub` visibility for Kujo symbols.
- Keep canonical examples runnable or parseable according to `tests/docs_examples.rs`.
- Document intentional adapter extraction gaps when conformance coverage changes.
- Keep source-link templates safe: reject absolute paths and parent traversal, percent-encode normalized relative paths, and fall back to plain source locations when unsafe.

## Change Checklist

- Adapter/extraction change: update or add fixture coverage in `tests/docgen_universal.rs`, especially for visibility, doc attachment, async/decorator cases, diagnostics, and deterministic ordering.
- CLI JSON change: update `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, shape assertions, and the fixture-backed snapshot in `tests/cli_json_contracts.rs`.
- Generated-doc refresh: run the repo-supported `kujo docgen` command, compare generated outputs to source evidence, and use `kujo-docgen-public-docs-refresh` if committed public docs are being refreshed.
- Link validation change: test local file, local anchor, external allowlist, redirect allowlist, private address blocking, and budget truncation modes.
- Discovery/cache change: test invalid UTF-8, max file size/depth/files, env and CLI overrides, cache hit/miss counters, and deterministic diagnostics.
- AI task/gap output change: ensure bounded source context, constrained prompts, and "do not invent behavior" language remain present.

## Validation Commands

```bash
cargo test --test docgen_universal
cargo test --test cli_json_contracts
cargo test --test docs_examples
cargo test --test readme_contracts
```

For broad DocGen changes, also run focused commands that exercise `--json`, strict gates, `--emit-ai-tasks`, link validation modes, and any touched language adapter. Use cache directories and generated output directories outside commits unless the repo explicitly tracks them.

## Sources Consulted

- Status: repo-backed: `docs/DOCGEN.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, `src/docgen/`.
- Status: repo-backed: `src/main.rs`, `src/doc_generator.rs`, `tests/docgen_universal.rs`, `tests/cli_json_contracts.rs`, `tests/docs_examples.rs`.
