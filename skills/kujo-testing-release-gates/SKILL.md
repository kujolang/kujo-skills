---
name: kujo-testing-release-gates
description: Use this skill when testing Kujo scripts, examples, docs, security behavior, runtime parity, CLI contracts, or Rust implementation changes, and when preparing or reviewing release-gate readiness.
---

# Kujo Testing And Release Gates

Run targeted tests after each logical change; broaden when behavior, contracts, or release readiness are affected.

## Core Commands

```bash
cargo fmt --check
cargo check
cargo test
cargo run -- test --runtime vm
cargo run -- test --runtime dual
```

Docs/examples:

```bash
cargo test --test docs_examples
cargo test --test readme_contracts
```

CLI/contracts:

```bash
cargo test --test cli_contracts
cargo test --test cli_json_contracts
cargo test --test diagnostics_golden
```

Runtime parity:

```bash
cargo test --test vm_interpreter_parity_surfaces
```

Security:

```bash
cargo test --test native_api_security_boundaries
cargo test --test runtime_security
cargo test --test serve_command_integration
```

Release gates:

```bash
bash scripts/release_gate.sh --minimal
bash scripts/release_gate.sh --full
bash scripts/release_candidate_gate.sh --full
bash scripts/enterprise_verify.sh --minimal
bash scripts/enterprise_verify.sh --full
```

AI-native enterprise evidence:

```bash
cargo test --test enterprise_verify_contract
cargo test --test ai_replay_hermeticity_contract
cargo test --test docs_policy_consistency_contract
KUJO_AI_REPLAY=tests/fixtures/ai_cassettes KUJO_AI_REPLAY_MODE=strict cargo run -- run examples/ai_enterprise_replay_showcase.kujo
```

## Rules

- Do not change behavior without tests and docs.
- Do not blindly update snapshots. Inspect expected vs actual output first.
- For CLI JSON output changes, update contract docs, tests, and changelog.
- For native API capability changes, update standard library docs and security posture.
- For AI helper or AI egress changes, update `docs/AI_RUNTIME.md`, `docs/SECURE_AI_SCRIPTING.md`, security posture docs, replay fixtures, and enterprise evidence docs together.
- For runtime behavior changes, add parity coverage or document intentional divergence.
- For release readiness, follow `ROADMAP.md` and `docs/PRE_V1_MASTER_UNFINISHED_CHECKLIST.md`, not crate version alone.

## Sources Consulted

- Status: repo-backed: `README.md`, `ROADMAP.md`, `docs/RELEASE_PROCESS.md`, `docs/PRE_V1_MASTER_UNFINISHED_CHECKLIST.md`.
- Status: repo-backed: `tests/docs_examples.rs`, `tests/cli_contracts.rs`, `tests/cli_json_contracts.rs`, `tests/enterprise_verify_contract.rs`, `tests/ai_replay_hermeticity_contract.rs`, `scripts/release_gate.sh`, `scripts/release_candidate_gate.sh`, `scripts/enterprise_verify.sh`.
