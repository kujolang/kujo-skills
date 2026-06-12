---
name: kujo-runtime-parity
description: Use this skill when investigating VM versus interpreter behavior, deciding runtime flags, adding language/runtime surfaces, updating parity tests, or preventing accidental interpreter-default workflows.
---

# Kujo Runtime Parity

Kujo is VM-first for normal execution.

## Runtime Decisions

- Day-to-day script: `kujo run <file>`.
- Debug/compat isolation: `kujo run --interpreter <file>`.
- Fixture compatibility sweep: `kujo test --runtime dual`.
- Strict VM gate: `kujo test --runtime vm`.
- Parity drift suite: `cargo test --test vm_interpreter_parity_surfaces`.

Do not make `--interpreter` the normal path for user docs or ordinary module imports.

## Debug Loop

1. Reproduce on VM default.
2. Reproduce with `--interpreter`.
3. Minimize the `.kujo` program.
4. Check `docs/VM_INTERPRETER_PARITY_MATRIX.md` for known supported, unsupported, or divergent status.
5. Add a parity test if the surface is meant to match.
6. If divergence is intentional, document it in the parity matrix and user-facing guidance.

## Acceptable Divergence

Only accept divergence when it is explicit, deterministic, documented, and tested. Unsupported surfaces should fail with clear errors, not silently fall back to different semantics.

## Validation

```bash
cargo test --test vm_interpreter_parity_surfaces
cargo run -- test --runtime vm
cargo run -- test --runtime dual
cargo test --test runtime_path_matrix_contract
```

## Sources Consulted

- Status: repo-backed: `docs/VM_INTERPRETER_PARITY_MATRIX.md`, `docs/VM_INTERPRETER_MIGRATION_PLAYBOOK.md`, `docs/ARCHITECTURE.md`.
- Status: repo-backed: `tests/vm_interpreter_parity_surfaces.rs`, `tests/cli_contracts.rs`, `tests/runtime_path_matrix_contract.rs`.

