# Testing And Release Reference

## Sources

- `README.md`
- `ROADMAP.md`
- `docs/RELEASE_PROCESS.md`
- `docs/PRE_V1_MASTER_UNFINISHED_CHECKLIST.md`
- `docs/VM_INTERPRETER_PARITY_MATRIX.md`
- `tests/docs_examples.rs`
- `scripts/release_gate.sh`

## Targeted Development Tests

Run the smallest relevant tests while developing, then broader gates for risky changes.

Common commands:

```bash
cargo fmt --check
cargo check
cargo test
cargo test --test docs_examples
cargo test --test readme_contracts
cargo test --test cli_contracts
cargo test --test cli_json_contracts
cargo test --test diagnostics_golden
cargo test --test vm_interpreter_parity_surfaces
cargo run -- test --runtime vm
cargo run -- test --runtime dual
```

Security:

```bash
cargo test --test native_api_security_boundaries
cargo test --test runtime_security
cargo test --test serve_command_integration
```

Release:

```bash
bash scripts/release_gate.sh --minimal
bash scripts/release_gate.sh --full
bash scripts/release_candidate_gate.sh --full
bash scripts/release_candidate_gate.sh --roadmap-only
```

## Rules

- Do not change behavior without tests and docs.
- Do not blindly update snapshots; inspect expected vs actual.
- CLI JSON changes require docs, tests, and changelog notes.
- Native API capability changes require standard library docs and security posture updates.
- Runtime behavior changes require parity checks or documented divergence.

