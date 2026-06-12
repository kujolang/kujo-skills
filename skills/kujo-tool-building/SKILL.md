---
name: kujo-tool-building
description: Use this skill when building practical Kujo CLI tools, quality gates, policy checkers, repo scanners, JSON-reporting scripts, or local automation that needs deterministic arguments, output, and exit behavior.
---

# Kujo Tool Building

Use Kujo tools as small deterministic programs with explicit inputs, short outputs, and automation-safe exits.

## Tool Skeleton

```kujo
argv := args()
if len(argv) < 1 {
  print("usage: kujo run tool.kujo -- <policy.json>")
  exit(2)
}

policy_path := argv[0]
raw := read_file(policy_path)
parsed := parse_json(raw)
if type(parsed) == "Error" {
  print("policy parse failure")
  exit(4)
}
```

Run script flags after `--`:

```bash
kujo run tool.kujo -- policy.json --format json
kujo run tool.kujo -- --help
```

## Output And Exit Rules

- `0`: success.
- `1`: policy/gate failure.
- `2`: usage error.
- `4`: runtime/semantic failure.
- For JSON tools, emit one machine-readable payload on stdout and keep human text off stdout.
- Use `eprint(...)` for stderr-friendly diagnostics where stdout is reserved for JSON.

## Repo-Backed Patterns

- Validate file paths, JSON parsing, and required keys up front.
- Prefer `parse_json` plus shape checks for policy inputs.
- Use local helpers for repeated report text:

```kujo
func section(title) { print(""); print("== " + title + " ==") }
func kv(label, value) { print("  " + label + ": " + value) }
func ok(message) { print("ok: " + message) }
```

- Prefer VM default: `kujo run tool.kujo -- args`.
- For file/network/process/database host effects, combine tool design with the security skill.

## Gotchas

- `args()` contains user args after the script path, not the script path itself.
- `has_key`, `contains`, `starts_with`, and `ends_with` return `1`/`0`.
- Collection helpers return new values; reassign.
- `write_file(path, content)` does not overwrite unless passed options with `{"overwrite": true}`.

## Validation

```bash
cargo run -- check tool.kujo --quiet
cargo run -- run tool.kujo -- fixture.json
cargo test --test docs_examples
```

For CLI-contract-like tooling changes in the repo:

```bash
cargo test --test cli_contracts
cargo test --test cli_json_contracts
```

## Sources Consulted

- Status: repo-backed: `docs/FIRST_TOOL_COOKBOOK.md`, `docs/STANDARD_LIBRARY_REFERENCE.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`.
- Status: repo-backed: `showcases/README.md`, `examples/README_examples.md`.

