---
name: kujo-security-hardening
description: Use this skill when writing or reviewing Kujo scripts that touch files, processes, shell commands, network, databases, archives, HTML/static serving, AI provider egress, secrets, or untrusted input; it enforces Kujo's conservative native API security posture.
---

# Kujo Security Hardening

Be direct and conservative: Kujo is not a sandbox.

## Trust Model

- `kujo run` and `kujo test-run` default to trusted mode.
- Trusted mode means host-effect APIs run with ambient process privileges.
- For untrusted code, start with `--untrusted` and add only the required `--allow-*` flags.
- `--allow-*` flags imply restricted baseline with only those capabilities enabled.
- Treat `--allow-all` as trusted/full ambient-host execution.

## Capability Flags

- Files: `--allow-fs-read`, `--allow-fs-write`, `--allow-fs-delete`
- Process: `--allow-process-exec`
- Shell strings: `--allow-shell-exec`
- Environment: `--allow-env-read`, `--allow-env-write`
- Network: `--allow-net-client`, `--allow-net-server`, `--allow-net`
- AI provider egress: `--allow-ai`
- Database: `--allow-database`
- Nondeterminism/time: `--allow-clock`, `--allow-random`

## Safer Patterns

```bash
kujo run --untrusted --allow-fs-read ./script.kujo
kujo run --untrusted --allow-net-client ./fetch.kujo
kujo run --untrusted --allow-ai ./agent.kujo
```

- Prefer `spawn_process(["cmd", "arg"])` and `pipe_commands([...])` over shell strings.
- Never interpolate untrusted input into `execute(...)` or `execute_status(...)`.
- Keep `inherit_env` disabled unless required.
- Use timeouts and output limits for process/network flows.
- Apply external isolation for high-risk runs: containers, low-privilege service accounts, read-only filesystems, network ACLs/firewalls, and secret management.

## High-Risk Surfaces

- Outbound network can exfiltrate data or pivot internally. In untrusted network-client runs, understand `KUJO_NET_DESTINATION_POLICY=deny_private`.
- AI helpers (`ai_chat`, `ai_stream_chat`, `ai_embedding`, `ai_tool_loop`) use a separate `--allow-ai` gate. Prefer it over broad network-client access when a script only needs provider calls.
- Set `KUJO_AI_ALLOWED_ENDPOINTS` for shared automation; non-matching endpoints fail with deterministic `kind:"endpoint_denied"` errors. Deterministic AI test lanes should use strict replay cassettes, not live provider credentials.
- `html_response(...)` does not sanitize attacker-controlled content; escape `&`, `<`, `>`, `"`, and `'` or prefer JSON responses.
- `unzip` is hardened against traversal/symlinks and size limits, but archive extraction remains a high-risk write surface.
- `kujo serve` is local preview/testing, not a hardened internet edge.
- Database access should use least-privileged accounts and network restrictions.
- Crypto helpers are not a substitute for secret management or key rotation.

## Review Checklist

- Does the command run with the fewest `--allow-*` flags?
- Is shell execution avoided or strictly bounded?
- Are reads/writes/deletes scoped to intended paths?
- Are network destinations intentional and policy-compatible?
- Are secrets redacted from logs, JSON, and diagnostics?
- Are failure paths deterministic and non-zero?

## Validation

```bash
cargo test --test native_api_security_boundaries
cargo test --test runtime_security
cargo test --test serve_command_integration
cargo test --test ai_replay_hermeticity_contract
cargo test --test docs_policy_consistency_contract
```

## Sources Consulted

- Status: repo-backed: `docs/NATIVE_API_SECURITY_POSTURE.md`, `docs/SECURE_AI_SCRIPTING.md`, `docs/AI_RUNTIME.md`, `src/interpreter/capabilities.rs`.
- Status: repo-backed: `tests/native_api_security_boundaries.rs`, `tests/runtime_security.rs`, `tests/serve_command_integration.rs`.
