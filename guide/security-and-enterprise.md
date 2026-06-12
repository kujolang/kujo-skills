# Security And Enterprise Reference

## Sources

- `docs/NATIVE_API_SECURITY_POSTURE.md`
- `docs/CLI_MACHINE_READABLE_CONTRACTS.md`
- `docs/STANDARD_LIBRARY.md`
- `tests/native_api_security_boundaries.rs`
- `tests/runtime_security.rs`
- `src/interpreter/capabilities.rs`

## Capability Model

Kujo is not a sandbox. Trusted/default mode runs with ambient process privileges.

Restricted execution:

```bash
kujo run --untrusted --allow-fs-read script.kujo
kujo run --untrusted --allow-net-client fetch.kujo
```

Capability flags include:

- `--allow-fs-read`, `--allow-fs-write`, `--allow-fs-delete`
- `--allow-process-exec`, `--allow-shell-exec`
- `--allow-env-read`, `--allow-env-write`
- `--allow-net-client`, `--allow-net-server`, `--allow-net`
- `--allow-database`
- `--allow-clock`, `--allow-random`
- `--allow-all`

Treat `--allow-all` as trusted execution.

## High-Risk Surfaces

- Shell strings: `execute`, `execute_status`; require `--allow-shell-exec`.
- Structured process execution: `spawn_process`, `pipe_commands`; require `--allow-process-exec`.
- Outbound network: HTTP/TCP/UDP helpers; require `--allow-net-client`.
- Listeners: HTTP/server sockets; require `--allow-net-server`.
- Database helpers require `--allow-database`.
- Archive extraction is a high-risk write surface.
- `html_response(...)` does not sanitize attacker-controlled content.
- `kujo serve` is local preview/testing, not a hardened internet-facing edge.

## Enterprise Operating Rules

- Prefer least-privilege Kujo capability flags plus external isolation.
- Use service accounts, read-only filesystems, narrow writable mounts, network ACLs, firewalls, and secret managers.
- For untrusted network-client runs, understand the outbound destination policy: `deny_private` blocks private/local/link-local/multicast/unspecified destinations unless explicitly overridden.
- Keep JSON outputs stable and auditable.
- Use release gates and record command evidence for release decisions.

