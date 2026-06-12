---
name: kujo-core-language
description: Use this skill when writing, editing, explaining, or reviewing Kujo `.kujo` source code, including syntax, bindings, imports, functions, control flow, collections, truthiness, runtime errors, and VM-first execution defaults.
---

# Kujo Core Language

Use this as the default baseline for general Kujo coding tasks.

## Repo-Backed Defaults

- Write `.kujo` files using current syntax from `docs/LANGUAGE_SPEC.md` and canonical examples, not legacy expected-fail examples.
- Run ordinary scripts with `kujo run <file>`; VM is the default path.
- Use `--interpreter` only for explicit compatibility/debug isolation.
- Prefer `let` for immutable bindings, `mut` for bindings that are reassigned or mutated, and `const` for constants.
- `name := value` updates an existing mutable binding when present; otherwise it creates a mutable binding in the current scope.
- Quote strings explicitly. Unknown identifiers are runtime errors.
- Use `has_key`, `get`, or `get_default` before dictionary access that may be missing.
- Treat out-of-bounds array/string indexing, integer overflow, division by zero, and modulo by zero as runtime errors.

## Syntax Surfaces To Use

- Functions: `func name(args) { ... }`; fallthrough returns `null`.
- Async functions: `async func name(args) { ... }` where runtime support applies.
- Control flow: `if`/`else`, `while`, `loop`, `for item in values`, `match`, `try`/`except`, `throw`.
- Data: arrays (`[1, 2]`), dictionaries (`{"key": value}`), structs/enums where current examples/spec support them.
- Imports: `import module`, `from module import symbol`, and dotted imports such as `from src.util import value`.

## Truthiness

Falsey: `false`, `null`, `0`, `0.0`, `""`, `[]`, `{}`.

Truthy: all other values, including `"false"`.

`&&` and `||` short-circuit and return booleans.

## Agent Gotchas

- Do not copy files listed as "Legacy or Expected-Fail Examples" in `examples/README_examples.md`.
- Predicate helpers such as `has_key`, `contains`, `starts_with`, and `ends_with` return `1`/`0`; compare explicitly.
- Collection helpers such as `push`, `insert`, `remove_at`, `concat`, `map`, and `filter` return new values; reassign the result.
- Imported functions must be exported from the source module.
- Do not claim Kujo is release-ready solely from crate version strings; use roadmap/checklist evidence.

## Validation

For normal script work:

```bash
cargo run -- check path/to/file.kujo --quiet
cargo run -- run path/to/file.kujo
```

For changes affecting examples/docs:

```bash
cargo test --test docs_examples
cargo test --test readme_contracts
```

For runtime behavior changes:

```bash
cargo test --test vm_interpreter_parity_surfaces
cargo run -- test --runtime vm
cargo run -- test --runtime dual
```

## Sources Consulted

- Status: repo-backed: `README.md`, `docs/LANGUAGE_SPEC.md`, `docs/VM_INTERPRETER_PARITY_MATRIX.md`, `docs/VM_INTERPRETER_MIGRATION_PLAYBOOK.md`.
- Status: repo-backed: `examples/README_examples.md`, `tests/docs_examples.rs`, `tests/vm_interpreter_parity_surfaces.rs`.
- Status: inferred; needs maintainer confirmation: prefer `let`/`mut`/`const` plus `:=` for new idiomatic code even though some examples still use legacy `=` style.

