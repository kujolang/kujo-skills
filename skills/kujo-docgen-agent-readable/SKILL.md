---
name: kujo-docgen-agent-readable
description: Use this skill when working on `kujo docgen`, generated documentation, docs-as-contract surfaces, agent-readable JSON/gap outputs, documentation coverage gates, README/reference alignment, or example smoke policy.
---

# Kujo DocGen And Agent-Readable Docs

DocGen is a compatibility and agent-readability surface, not just prose generation.

## DocGen Model

`kujo docgen` is model-driven and adapter-based:

- core orchestration: `src/docgen/core.rs`
- discovery: `src/docgen/discovery.rs`
- shared model: `src/docgen/model.rs`
- gaps: `src/docgen/gaps.rs`
- renderers: `src/docgen/render/*`
- adapters: `src/docgen/adapters/*`

DocGen is scan-only: no source execution, no imports/build steps, no external AI calls by default, symlink traversal skipped, bounded discovery, deterministic ordering, and HTML escaping.

## CLI Patterns

```bash
kujo docgen src/ --language kujo --out-dir docs/generated
kujo docgen . --out-dir docs/generated
kujo docgen . --public-only --fail-on-undocumented --fail-on-broken-links
kujo docgen . --emit-ai-tasks --out-dir docs/generated
```

`kujo docgen --json` has a documented stable payload and should be emitted from the typed builder in `src/docgen/core.rs`.

## Documentation Rules

- Treat docs, examples, and generated JSON as agent-consumed surfaces.
- Do not invent behavior in generated AI task prompts; mark uncertainty.
- Keep README, language spec, standard library reference, and tests aligned.
- Public-only DocGen gates depend on explicit `pub` visibility for Kujo symbols.
- Keep canonical examples runnable or parseable according to `tests/docs_examples.rs`.

## Validation

```bash
cargo test --test docgen_universal
cargo test --test cli_json_contracts
cargo test --test docs_examples
cargo test --test readme_contracts
```

## Sources Consulted

- Status: repo-backed: `docs/DOCGEN.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, `src/docgen/`.
- Status: repo-backed: `tests/docgen_universal.rs`, `tests/cli_json_contracts.rs`, `tests/docs_examples.rs`.

