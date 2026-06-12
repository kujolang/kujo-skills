---
name: kujo-enterprise-automation
description: Use this skill when designing Kujo automation for CI, policy gates, operational workflows, enterprise-safe scripting, audit logs, machine-readable reports, or capability-minimal production runs.
---

# Kujo Enterprise Automation

Design Kujo automation as deterministic, auditable, and capability-minimal.

## Defaults

- Use VM default: `kujo run workflow.kujo -- args`.
- Reserve stdout for machine-readable JSON when the workflow is consumed by automation.
- Treat non-zero exit codes as authoritative failure signals.
- Keep policy inputs explicit and validated at startup.
- Prefer `kujo package-install --frozen` to verify manifests/lockfiles without rewriting them.

## Execution Policy

For untrusted or shared environments:

```bash
kujo run --untrusted --allow-fs-read --allow-net-client workflow.kujo -- policy.json
```

Add only capabilities the workflow requires. Recommend external controls for real enterprise isolation: containers, service accounts, read-only filesystems, narrow writable mounts, network ACLs, firewall egress policy, and secrets managers.

## JSON And Diagnostics

- Use documented CLI JSON surfaces as contracts.
- For custom tools, output a stable object with fields such as `status`, `summary`, `findings`, and `exit_code`.
- Keep human diagnostics concise and route them away from stdout when stdout is JSON.
- Use stable rule IDs or finding categories when reports are consumed by CI.

## Release And CI

- For repo changes, run targeted tests first and release gates when scope is broad.
- For CLI JSON or diagnostics changes, update docs, contract tests, and changelog notes.
- Record command outcomes for release readiness or operational sign-off.

## Safe Failure Behavior

- Usage/config errors should fail early with `exit(2)`.
- Policy failures should return `exit(1)` with deterministic findings.
- Runtime misuse should fail rather than silently coercing values.
- Avoid nondeterminism (`random`, clock, network) unless the workflow explicitly needs it and capabilities permit it.

## Sources Consulted

- Status: repo-backed: `README.md`, `docs/FIRST_TOOL_COOKBOOK.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, `docs/RELEASE_PROCESS.md`.
- Status: repo-backed: `docs/NATIVE_API_SECURITY_POSTURE.md`, `showcases/README.md`, `docs/INSTALL_MATRIX.md`.
- Status: inferred; needs maintainer confirmation: suggested custom JSON field names for user-authored enterprise tools are conventions derived from repo output style, not a formal Kujo script schema.

