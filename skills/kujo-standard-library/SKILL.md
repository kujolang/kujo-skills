---
name: kujo-standard-library
description: Use this skill when using, adding, or reviewing Kujo native standard library functions, including arity, return types, capability gates, JSON conversion, filesystem, process, network, database, crypto, strings, arrays, dictionaries, rendering helpers, and collection helper behavior.
---

# Kujo Standard Library

Consult the repo docs before assuming a builtin exists.

## Sources Of Truth

- `docs/STANDARD_LIBRARY.md`: full inventory, arity, return type, errors, capability.
- `docs/STANDARD_LIBRARY_REFERENCE.md`: practical category reference and tier labels.
- `src/interpreter/mod.rs`: runtime registration and `get_builtin_names()`.
- `src/interpreter/capabilities.rs`: native capability metadata.

## Important Contracts

- `parse_json` accepts strings up to `1,048,576` bytes and nesting depth `64`; invalid JSON returns a `Value::Error`.
- `to_json` and `to_json_pretty` reject non-finite floats.
- Dictionary-like JSON serialization uses deterministic key ordering.
- Predicate helpers such as `contains`, `starts_with`, `ends_with`, and `has_key` return `1`/`0`.
- Collection helpers such as `push`, `insert`, `remove_at`, `concat`, `map`, and `filter` return updated values; reassign them.
- Rendering helpers are native builtins too: `escape_xml` is stable; `render_markdown`, `render_listing_card`, and `render_layout_native` are preview surfaces used by the SSG hot path.
- Dictionary access uses brackets; runtime structs such as `ProcessResult` use dot fields.
- `write_file(path, content)` errors if the path exists unless overwrite options are provided.

## Capability Awareness

Do not use host-effect functions without considering execution policy:

- Filesystem read/write/delete map to filesystem capabilities.
- `execute` and `execute_status` require shell execution capability.
- `spawn_process` and `pipe_commands` require process execution capability.
- HTTP/TCP/UDP client helpers require network-client capability.
- Server/listener helpers require network-server capability.
- Database helpers require database capability.
- Clock/random helpers require clock/random capabilities in restricted mode.

## Review Checklist For New Builtins

- Add runtime implementation and registration.
- Add centralized arity metadata when possible.
- Add capability metadata if host effects exist.
- Update `docs/STANDARD_LIBRARY.md` and `docs/STANDARD_LIBRARY_REFERENCE.md`.
- Add or update tests in stdlib/security contract suites.

## Validation

```bash
cargo test --test stdlib_reference_contract
cargo test --test stdlib_reference_policy_contract
cargo test --test native_api_security_boundaries
```

## Sources Consulted

- Status: repo-backed: `docs/STANDARD_LIBRARY.md`, `docs/STANDARD_LIBRARY_REFERENCE.md`.
- Status: repo-backed: `tests/stdlib_reference_contract.rs`, `tests/stdlib_reference_policy_contract.rs`, `src/interpreter/mod.rs`, `src/interpreter/capabilities.rs`.
