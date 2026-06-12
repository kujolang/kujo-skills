# Tool Building Reference

## Sources

- `docs/FIRST_TOOL_COOKBOOK.md`
- `docs/STANDARD_LIBRARY_REFERENCE.md`
- `docs/CLI_MACHINE_READABLE_CONTRACTS.md`
- `showcases/README.md`

## CLI Tool Shape

Use `args()` for user arguments:

```kujo
argv := args()
if len(argv) < 1 {
  print("usage: kujo run quality_gate.kujo -- <policy.json>")
  exit(2)
}
```

When script flags can collide with Kujo CLI flags, run:

```bash
kujo run tool.kujo -- --help
kujo run tool.kujo -- policy.json --format json
```

## Deterministic Gates

- `2`: usage error.
- `1`: policy/gate failure.
- `4`: runtime/semantic failure.
- `0`: success.

Validate input shape early. For JSON:

```kujo
raw := read_file(policy_path)
parsed := parse_json(raw)
if type(parsed) == "Error" {
  print("policy parse failure")
  exit(4)
}
```

## Output Helpers

Small scripts can print directly. Multi-step reports should use local helpers:

```kujo
func section(title) { print(""); print("== " + title + " ==") }
func kv(label, value) { print("  " + label + ": " + value) }
func ok(message) { print("ok: " + message) }
func fail(message) { print("fail: " + message) }
```

Machine-readable tools should emit one JSON payload on stdout with `to_json(...)` or `to_json_pretty(...)`; keep human diagnostics concise and away from stdout when stdout is the contract.

## Common Gotchas

- `args()` excludes the script path.
- `has_key`, `contains`, `starts_with`, and `ends_with` return `1`/`0`.
- `push`, `insert`, `remove_at`, `concat`, `map`, and similar helpers return new values.
- `write_file(path, content)` errors if the file exists; use `{"overwrite": true}` intentionally.
- Prefer VM default: `kujo run tool.kujo -- args`.

