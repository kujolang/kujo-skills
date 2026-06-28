# Kujo Skills Extraction Report

## Repository reviewed

`/Users/robertdevore/2026/Kujolang/kujo-repos/kujo`

## Commit / branch reviewed

- Branch: `main`
- Commit: `c57075f3bdfb22b13953cae3d789fd0cec8a654e`

## Executive summary

This extraction produced an 11-skill Kujo Agent Skills package focused on actual repo-backed practices: VM-first execution, deterministic CLI contracts, conservative native API capability policy, machine-readable tool output, release-gate discipline, runtime parity, and Rust implementation contribution rules.

The strongest evidence comes from `README.md`, `docs/LANGUAGE_SPEC.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, `docs/NATIVE_API_SECURITY_POSTURE.md`, `docs/STANDARD_LIBRARY.md`, `docs/STANDARD_LIBRARY_REFERENCE.md`, `docs/VM_INTERPRETER_PARITY_MATRIX.md`, `docs/FIRST_TOOL_COOKBOOK.md`, `ROADMAP.md`, integration tests, and implementation metadata in `src/interpreter/capabilities.rs` and `src/interpreter/mod.rs`.

Two requested files, `DOGFOOD_NOTES.md` and `BUG_HUNT_REPORT.md`, were not present in this checkout. Git history for the requested areas was shallow but included relevant commits for diagnostics and centralized CLI/LSP/SSG output rendering.

## Proposed skill catalog

- `kujo-core-language`
- `kujo-tool-building`
- `kujo-security-hardening`
- `kujo-enterprise-automation`
- `kujo-cli-contracts`
- `kujo-standard-library`
- `kujo-testing-release-gates`
- `kujo-runtime-parity`
- `kujo-language-implementation`
- `kujo-docgen-agent-readable`
- `kujo-maintainer-review`

## Source map

| Source file | Topics extracted | Skills informed | Confidence |
|---|---|---|---|
| `README.md` | VM-first positioning, pre-1.0 boundary, safety snapshot, CLI overview, validation commands | core-language, runtime-parity, security-hardening, testing-release-gates, enterprise-automation | Strong |
| `docs/LANGUAGE_SPEC.md` | `.kujo` file model, grammar, binding semantics, truthiness, runtime errors, imports, CLI compatibility policy | core-language, runtime-parity, cli-contracts, maintainer-review | Strong |
| `docs/CLI_MACHINE_READABLE_CONTRACTS.md` | stdout/stderr policy, exit codes, JSON payload shapes, contract change rules | cli-contracts, enterprise-automation, docgen-agent-readable, maintainer-review | Strong |
| `docs/NATIVE_API_SECURITY_POSTURE.md` | not-a-sandbox boundary, trust modes, capability flags, process/network/fs/db/html/archive/server risks, unsafe/JIT policy | security-hardening, enterprise-automation, language-implementation, maintainer-review | Strong |
| `docs/STANDARD_LIBRARY.md` | builtin inventory, arity, capability gates, JSON conversion contracts | standard-library, security-hardening | Strong |
| `docs/STANDARD_LIBRARY_REFERENCE.md` | practical builtin categories, tiers, predicate and collection helper gotchas, process result contracts | standard-library, tool-building, core-language | Strong |
| `docs/FIRST_TOOL_COOKBOOK.md` | `args()`, `--` separator, JSON policy tool, output helpers, deterministic exits | tool-building, enterprise-automation | Strong |
| `docs/VM_INTERPRETER_PARITY_MATRIX.md` | supported/divergent surfaces, runtime command matrix, VM-first recommendations, parity gate | runtime-parity, core-language, testing-release-gates | Strong |
| `docs/VM_INTERPRETER_MIGRATION_PLAYBOOK.md` | migration commands, decision table, dual/vm/interpreter use | runtime-parity, core-language | Strong |
| `docs/DOCGEN.md` | DocGen/DocsGen architecture, supported languages, scan-only security model, discovery/cache limits, link validation, JSON fields, strict gates, AI tasks | docgen-agent-readable, cli-contracts | Strong |
| `docs/ARCHITECTURE.md` | subsystem map, execution pipeline, runtime path model, pre-1.0 posture | language-implementation, runtime-parity | Medium; version wording conflicts with other docs |
| `ROADMAP.md` | release rules, agent execution contract, test requirements, repo map, readiness blockers | testing-release-gates, language-implementation, maintainer-review | Strong |
| `docs/V1_SCOPE.md` | in-scope/out-of-scope v1 surfaces, deferred runtime backlog, pre-1.0 boundary | testing-release-gates, maintainer-review, publication-notes | Strong |
| `docs/PRE_V1_MASTER_UNFINISHED_CHECKLIST.md` | checklist governance, unresolved tag-time artifact sign-off, closure evidence rules | testing-release-gates, maintainer-review, publication-notes | Strong |
| `docs/RELEASE_PROCESS.md` | release gates, semver policy, changelog format, artifact workflow | testing-release-gates, cli-contracts | Medium; contains release-state wording conflict |
| `docs/INSTALL_MATRIX.md` | install paths, commit-pinned production guidance, platform caveats | enterprise-automation, publication-notes | Strong |
| `CONTRIBUTING.md` | dev setup, test snapshots, structured errors, contributor workflow | language-implementation, testing-release-gates | Medium; older/general guidance |
| `CHANGELOG.md` | Keep a Changelog structure, sparse current entries | cli-contracts, testing-release-gates | Medium |
| `examples/README_examples.md` | canonical examples, expected-fail examples, output helper advice | core-language, tool-building, testing-release-gates | Strong |
| `tests/docs_examples.rs` | executable source of truth for example smoke policy and expected-fail list | core-language, testing-release-gates | Strong |
| `tests/cli_contracts.rs` | exit codes, stdout/stderr behavior, runtime diagnostics JSON, LSP modes | cli-contracts, testing-release-gates | Strong |
| `tests/cli_json_contracts.rs` | JSON shape assertions and DocGen snapshot contract | cli-contracts, docgen-agent-readable | Strong |
| `tests/native_api_security_boundaries.rs` | capability and boundary regression coverage | security-hardening, testing-release-gates | Strong |
| `tests/runtime_security.rs` | lexer/runtime security boundaries, module cycle/path tests | security-hardening, language-implementation | Strong |
| `tests/stdlib_reference_contract.rs` | runtime builtin inventory/capability/arity docs synchronization | standard-library | Strong |
| `tests/vm_interpreter_parity_surfaces.rs` | executable parity evidence | runtime-parity, language-implementation | Strong |
| `src/interpreter/capabilities.rs` | capability flags and per-native mapping | security-hardening, standard-library | Strong |
| `src/interpreter/mod.rs` | builtin registration, arity metadata, native dispatch | standard-library, language-implementation | Strong |
| `src/main.rs` | CLI flag wiring, JSON/error emission, runtime selection | cli-contracts, runtime-parity, security-hardening | Strong |
| `src/cli_output.rs` | shared deterministic CLI render helpers | cli-contracts, language-implementation | Strong |
| `src/docgen/*` | DocGen pipeline and typed JSON builder | docgen-agent-readable, cli-contracts | Strong |
| `src/jit.rs`, `src/vm.rs` | unsafe/JIT wrapper boundary and VM execution path | language-implementation, runtime-parity | Strong |
| `scripts/release_gate.sh`, `scripts/release_candidate_gate.sh` | release gate commands | testing-release-gates | Strong |
| `.github/workflows/*` | release, fuzz, LSP, artifact validation workflows | testing-release-gates, publication-notes | Medium |
| `showcases/README.md` | advanced tool quality standard and defensive authorization note | tool-building, enterprise-automation | Medium |
| `tree-sitter-kujo/` | syntax tooling corpus | language-implementation | Medium; lightly inspected |
| `benchmarks/`, `benches/` | performance benchmark surfaces | testing-release-gates, enterprise-automation | Medium; not central to required skills |

## Strong repo-backed conventions

- Kujo is VM-first for ordinary `kujo run <file>`.
- `--interpreter` is an explicit fallback/debug path, not normal user guidance.
- Kujo is not a sandbox.
- Trusted mode is default; untrusted code should use `--untrusted` plus minimal `--allow-*`.
- `--allow-all` should be treated as trusted execution.
- Machine-readable CLI output and exit codes are compatibility surfaces.
- CLI JSON shape changes require docs, tests, and changelog notes.
- Native standard library inventory/capability/arity are contract-tested against runtime metadata.
- Example smoke policy is governed by `tests/docs_examples.rs`.
- Runtime behavior changes require parity tests or documented divergence.
- Behavior changes require tests and docs.
- Snapshot updates must be intentional, inspected, and documented.

## Inferred conventions needing maintainer confirmation

- Prefer `let`/`mut`/`const` plus `:=` for new idiomatic Kujo even though some examples still use `=` and semicolons.
- Suggested custom JSON report fields such as `status`, `summary`, `findings`, and `exit_code` are conventions derived from repo output style, not a formal script schema.
- The exact public readiness phrase for skills should be reviewed after maintainers reconcile release-status docs.
- Whether `kujo test` default should continue to be described as `dual` once future fixture work completes.

## Gaps in current docs that block better skills

- Release readiness wording conflicts: several docs state pre-1.0 boundaries, while `docs/RELEASE_PROCESS.md` says "Kujo is now at `1.0.0`" and `docs/ARCHITECTURE.md` says current crate version is `0.14.0`.
- `DOGFOOD_NOTES.md` and `BUG_HUNT_REPORT.md` were requested but absent.
- `CHANGELOG.md` is sparse, so contract-impact examples are mostly from policy docs/tests rather than actual release entries.
- Some canonical examples still show legacy-looking `=` assignment and semicolons, which complicates concise "idiomatic style" guidance.
- Editor/LSP installation docs were not fully distilled into a dedicated skill because the required catalog did not include an editor-specific skill.

## Suggested future skills

- `kujo-lsp-editor-integration`
- `kujo-package-workflows`
- `kujo-performance-benchmarking`
- `kujo-static-server`
- `kujo-workflow-packs`
- `kujo-tree-sitter`

## Public release risks

- Publishing these skills before release-status wording is reconciled could confuse users about whether Kujo is pre-1.0 or released as 1.0.
- If builtin tiers or capabilities change, `kujo-standard-library` and `kujo-security-hardening` must be refreshed.
- If `kujo test` runtime defaults change, `kujo-runtime-parity` must be updated.
- If public package names, repository URLs, or install artifacts change, `publication-notes.md` and enterprise/install guidance must be updated.
