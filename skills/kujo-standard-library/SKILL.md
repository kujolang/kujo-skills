---
name: kujo-standard-library
description: Use this skill when using, adding, or reviewing Kujo native standard library functions, including arity, return types, capability gates, JSON/JSONL conversion, filesystem, process, network, database, crypto, strings, URI encoding/decoding, date/time, PDF rendering, arrays, dictionaries, rendering helpers, AI helpers, and collection helper behavior.
---

# Kujo Standard Library

Consult the repo docs before assuming a builtin exists.

## Sources Of Truth

- `docs/STANDARD_LIBRARY.md`: full inventory, arity, return type, errors, capability.
- `docs/STANDARD_LIBRARY_REFERENCE.md`: practical category reference and tier labels.
- `docs/AI_RUNTIME.md`: AI helper contracts, replay, message builders, structured errors, egress policy, token budgeting.
- `src/interpreter/mod.rs`: runtime registration and `get_builtin_names()`.
- `src/interpreter/capabilities.rs`: native capability metadata.

## Important Contracts

- `parse_json` accepts strings up to `1,048,576` bytes and nesting depth `64`; invalid JSON returns a `Value::Error`.
- `to_json` and `to_json_pretty` reject non-finite floats and preserve deterministic key ordering.
- `jsonl_query(path, options)` provides bounded streaming JSONL filtering and constant-memory joins; validate `max_rows`, complete join options, and line-size behavior before adopting it for evidence workflows.
- `json_schema_validate` accepts supported Draft 2020-12 identification and annotation keywords while rejecting unsupported keywords, malformed schemas, and `$ref` cycles.
- `encode_uri_component(text)` and `decode_uri_component(text)` provide stable RFC 3986 UTF-8 percent encoding/decoding for provider and web integrations; malformed escapes and invalid UTF-8 fail closed.
- Dictionary-like JSON serialization uses deterministic key ordering.
- Predicate helpers such as `contains`, `starts_with`, `ends_with`, and `has_key` return `1`/`0`.
- Collection helpers such as `push`, `insert`, `remove_at`, `concat`, `map`, and `filter` return updated values; reassign them.
- Filesystem helpers now include `write_file_atomic(path, content_or_bytes, overwrite?)`, `io_set_permissions`, and `io_write_private_file`; use them for durable writes and restrictive private files instead of pure-Kujo temp-file wrappers.
- Process helpers return `ProcessResult` structs with `success`, `timed_out`, `cancelled`, and truncation fields; `spawn_process` supports timeout, output limits, env allow/deny, stream sinks, redaction, and cancellation.
- Time helpers include `format_date_tz(timestamp, format, timezone)` for IANA timezone formatting with daylight-saving transitions and `parse_datetime(value)` for RFC 3339 timestamps with offsets.
- Environment helpers include typed defaults: `env_int(name, default?)`, `env_float(name, default?)`, and `env_bool(name, default?)`; restricted runs require `env-read`.
- Crypto helpers include `hmac_sha256(secret, message)`, `hmac_sha256_verify`, preview streaming AES file encryption/decryption helpers, and `secure_random_token(byte_length)` for OS-backed redacted `Secret` tokens.
- Rendering helpers are native builtins too: `escape_xml` is stable; `render_markdown`, `render_listing_card`, and `render_layout_native` are preview surfaces used by the SSG hot path; `pdf_render_html` and `pdf_render_html_to_file` provide a strict in-process business-document PDF profile.
- Image values expose `get_pixel` and `set_pixel` methods for bounded single-pixel access; image load/save still requires filesystem capability.
- Database helpers include verified TLS PostgreSQL connection and pool surfaces: `db_connect_postgres_tls`, `db_pool_postgres_tls`, `db_pool_acquire`, `db_pool_release`, `db_pool_stats`, and `db_pool_close`; prefer the TLS pool for production PostgreSQL.
- AI helpers are native builtins too. `ai_request_hash`, `ai_text`, `ai_image_url`, `ai_message`, `ai_count_tokens`, `ai_fit_context`, and `json_schema_validate` are pure/capability-free; `ai_chat`, `ai_stream_chat`, `ai_embedding`, and `ai_tool_loop` use the `network-ai` capability.
- `ai_stream_chat(prompt_or_messages, options, on_chunk?)` can call a chunk callback; returning `false` cancels later chunks while the aggregate return shape stays stable.
- AI replay uses `KUJO_AI_RECORD`, `KUJO_AI_REPLAY`, and `KUJO_AI_REPLAY_MODE=strict|fallthrough`; strict replay misses fail deterministically without network I/O.
- Dictionary access uses brackets; runtime structs such as `ProcessResult` use dot fields.
- `write_file(path, content)` errors if the path exists unless overwrite options are provided.

## Capability Awareness

Do not use host-effect functions without considering execution policy:

- Filesystem read/write/delete map to filesystem capabilities.
- `execute` and `execute_status` require shell execution capability.
- `spawn_process` and `pipe_commands` require process execution capability.
- HTTP/TCP/UDP client helpers require network-client capability.
- AI provider helpers require `--allow-ai`; `--allow-net-client` does not unlock them.
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
cargo test --test docs_policy_consistency_contract
cargo test --test language_spec_contracts
```

## Sources Consulted

- Status: repo-backed: `docs/STANDARD_LIBRARY.md`, `docs/STANDARD_LIBRARY_REFERENCE.md`, `docs/AI_RUNTIME.md`.
- Status: repo-backed: `CHANGELOG.md`, `tests/stdlib_reference_contract.rs`, `tests/stdlib_reference_policy_contract.rs`, `tests/secure_random_token.rs`, `tests/pdf_render_html.rs`, `tests/postgres_tls.sh`, `src/interpreter/mod.rs`, `src/interpreter/capabilities.rs`, `src/interpreter/native_functions/filesystem.rs`, `src/interpreter/native_functions/schema.rs`, `src/interpreter/native_functions/json.rs`, `src/interpreter/native_functions/pdf.rs`, `src/interpreter/native_functions/database.rs`, `src/interpreter/native_functions/crypto.rs`.
