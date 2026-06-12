# Implementation Contributor Guide

## Sources

- `docs/ARCHITECTURE.md`
- `ROADMAP.md`
- `CONTRIBUTING.md`
- `src/`
- `docs/NATIVE_API_SECURITY_POSTURE.md`
- `tests/vm_interpreter_parity_surfaces.rs`

## Repo Structure

- Frontend: `src/lexer.rs`, `src/parser.rs`, `src/ast.rs`, `src/errors.rs`.
- Compiler/VM: `src/compiler.rs`, `src/bytecode.rs`, `src/vm.rs`.
- Interpreter: `src/interpreter/mod.rs`, `environment.rs`, `value.rs`, `control_flow.rs`.
- Native APIs: `src/interpreter/native_functions/*`, capability metadata in `src/interpreter/capabilities.rs`.
- Modules/packages: `src/module.rs`, `src/package_workflow.rs`.
- CLI/output: `src/main.rs`, `src/cli_output.rs`.
- LSP: `src/lsp_*`.
- DocGen: `src/docgen/*`.
- Static server: `src/serve_http.rs`.

## Contribution Rules

- Preserve documented language semantics unless the issue explicitly calls for a behavior change.
- Keep docs/tests/implementation synchronized.
- Centralize diagnostics and shared rendering instead of duplicating output formatting.
- Add or update parity tests for runtime surfaces.
- Update `docs/STANDARD_LIBRARY.md` and capability tests when native builtin arity/capability changes.
- Keep unsafe/JIT function-pointer calls behind audited wrappers and run JIT safety checks when moving unsafe boundaries.
- For parser/lexer changes, preserve safety limits and structured diagnostics.

## Avoid

- Broad refactors of `src/vm.rs`, `src/jit.rs`, or interpreter internals without a specific checklist item.
- Runtime-specific fixes that make VM and interpreter diverge silently.
- Ad hoc string munging for structured payloads when typed builders exist.
- Snapshot churn without behavior intent.

