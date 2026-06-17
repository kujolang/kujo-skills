---
name: kujo-language-implementation
description: "Use this skill when contributing to Kujo's Rust implementation: lexer, parser, AST, diagnostics, compiler, VM, interpreter, module loader, native functions, CLI, LSP, DocGen, JIT, or runtime security boundaries."
---

# Kujo Language Implementation

Start by locating the subsystem owner; keep changes narrow and semantics-preserving unless the issue explicitly changes behavior.

## Subsystem Map

- Lexer/parser/AST/diagnostics: `src/lexer.rs`, `src/parser.rs`, `src/ast.rs`, `src/errors.rs`.
- Compiler/VM/bytecode: `src/compiler.rs`, `src/vm.rs`, `src/bytecode.rs`.
- Interpreter: `src/interpreter/mod.rs`, `environment.rs`, `value.rs`.
- Native functions: `src/interpreter/native_functions/*`.
- Capabilities: `src/interpreter/capabilities.rs`.
- Modules/packages: `src/module.rs`, `src/package_workflow.rs`.
- CLI/output: `src/main.rs`, `src/cli_output.rs`.
- LSP: `src/lsp_*`.
- DocGen: `src/docgen/*`.
- Static server: `src/serve_http.rs`.

## Implementation Rules

- Preserve language semantics unless the task requires a change.
- Update tests and docs with every semantic, CLI, native API, or security boundary change.
- Do not patch around symptoms when a central abstraction owns the behavior.
- Keep parse/lexer failures structured and deterministic.
- Keep VM and interpreter behavior aligned or document/test divergence.
- Native functions need arity, capability, docs, and tests.
- Unsafe/JIT function-pointer calls should remain behind audited wrappers in `src/jit.rs`.

## Validation By Change Type

- Parser/lexer: `cargo test --test parser_diagnostics_contract`, `cargo test --test language_spec_contracts`, plus relevant unit tests.
- Runtime semantics: `cargo test --test vm_interpreter_parity_surfaces`, `cargo run -- test --runtime vm`, `cargo run -- test --runtime dual`.
- CLI JSON: `cargo test --test cli_json_contracts`.
- Security/native capabilities: `cargo test --test native_api_security_boundaries`, `cargo test --test runtime_security`.
- Unsafe/JIT: `bash scripts/check_jit_safety_contracts.sh src/jit.rs`, `cargo test --test jit_safety_contract_checker`.

## Sources Consulted

- Status: repo-backed: `docs/ARCHITECTURE.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `docs/NATIVE_API_SECURITY_POSTURE.md`.
- Status: repo-backed: `src/`, `tests/vm_interpreter_parity_surfaces.rs`, `scripts/check_jit_safety_contracts.sh`.
