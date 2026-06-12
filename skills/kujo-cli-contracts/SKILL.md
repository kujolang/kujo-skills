---
name: kujo-cli-contracts
description: Use this skill when changing Kujo CLI output, exit codes, diagnostics, `--json` payloads, `--json-runtime-diagnostics`, LSP helper JSON, formatter/linter/docgen JSON, or automation/toolchain compatibility behavior.
---

# Kujo CLI Contracts

Treat CLI output as a compatibility surface.

## Exit Codes

- `0`: success
- `1`: command/gate failure
- `2`: usage or argument parse error
- `3`: lexer/parser diagnostic failure
- `4`: runtime semantic/execution failure
- `5`: IO failure
- `6`: internal/tooling failure

Automation should treat any non-zero exit as failure unless a command-specific policy says otherwise.

## stdout/stderr Policy

- Successful `--json` payloads go to stdout.
- Failures normally put human-readable text on stderr and no JSON on stdout.
- Exception: `kujo run --json-runtime-diagnostics` emits runtime failure JSON on stdout and suppresses stderr.
- Exception: `kujo lsp-rename --json` emits runtime rename failure JSON on stdout and suppresses stderr.

## Stable JSON Surfaces

Contract-tested families include:

- `kujo format --json`
- `kujo lint --json`
- `kujo check --json`
- `kujo docgen --json`
- `kujo run --json-runtime-diagnostics`
- LSP helper commands with `--json`

Use typed/shared builders where they exist; for DocGen this includes `src/docgen/core.rs::build_cli_json_payload`.

## Breaking Changes

Breaking:

- removing fields
- renaming fields
- changing field types
- changing top-level shape
- changing exit-code meanings

Non-breaking:

- adding optional fields while preserving existing fields.

Payload-affecting changes require the same change set to update:

- `docs/CLI_MACHINE_READABLE_CONTRACTS.md`
- `tests/cli_json_contracts.rs`
- `CHANGELOG.md` compatibility/contract note

## Validation

```bash
cargo test --test cli_contracts
cargo test --test cli_json_contracts
cargo test --test diagnostics_golden
cargo test --test runtime_path_matrix_contract
```

For docs/examples affected by CLI examples:

```bash
cargo test --test docs_examples
cargo test --test readme_contracts
```

## Sources Consulted

- Status: repo-backed: `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, `src/main.rs`, `src/cli_output.rs`.
- Status: repo-backed: `tests/cli_contracts.rs`, `tests/cli_json_contracts.rs`, `tests/diagnostics_golden.rs`.

