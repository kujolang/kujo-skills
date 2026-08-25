# Security, Contracts, And Validation

Read this reference when code has host effects, exposes a CLI/machine contract,
or is ready for final verification.

## Security Boundary

Kujo is not a sandbox. Trusted execution has ambient process privileges.

For untrusted execution:

- Start with `--untrusted`; add only required `--allow-*` capabilities.
- Prefer `--allow-ai` over broad network access for AI-only egress.
- Set `KUJO_AI_ALLOWED_ENDPOINTS`; use `--deny-private-net` when required.
- Keep credentials outside source and wrap them with `secret(...)` in Kujo.
- Never put untrusted input in a shell command string.
- Escape generated HTML.
- Bound process, network, model, and tool time/output.
- Require explicit approval for destructive, privileged, expensive, publishing,
  or externally visible actions.

Instructions, manifests, and capability declarations are guidance, not
enforcement. The runtime and surrounding OS/container, identity, and network
controls enforce permissions and isolation.

## CLI Contract

Use the standard exit policy unless a narrower public contract overrides it:

- `0`: success
- `1`: generic failure or unmet gate
- `2`: usage/argument error
- `3`: lexer/parser diagnostic
- `4`: runtime/semantic failure
- `5`: I/O failure
- `6`: internal/tooling failure

For machine-readable commands, reserve successful stdout for the documented
JSON payload, send ordinary diagnostics to stderr, and treat non-zero exit as
authoritative. Preserve field names, schema versions, ordering, and optionality.
Payload changes require matching code, contract tests, docs, and changelog.

Separate script flags from Kujo flags:

```bash
kujo run tool.kujo -- --help
kujo run tool.kujo -- summarize --format json
```

## Validation By Target

Kujo script or tool:

```bash
kujo format --check path/to/file.kujo
kujo lint path/to/file.kujo
kujo check path/to/file.kujo
kujo run path/to/file.kujo -- <fixture-args>
```

Kujo package:

```bash
kujo package-install --frozen
kujo test
kujo test-run tests/relevant_tests.kujo -v
```

Language/runtime work starts with targeted Rust tests. Broad changes may need
`cargo fmt --check`, `cargo check`, `cargo test`, docs/CLI/diagnostic contract
tests, and VM/dual runtime gates.

Verify relevant happy, expected-failure, usage, I/O, malformed, boundary,
deterministic, repeated, denied, budget, timeout, cancellation, and
multi-iteration paths. Inspect snapshots before updating them. If a gate is
blocked, preserve the exact command, evidence, blocker class, and next action.

## Version-Sensitive VM Caveat

Observed on 2026-08-25: a `let` scratch binding declared inside a loop can pass
`kujo check` but fail on a later VM iteration with:

```text
KUJOVM001 Cannot reassign immutable let binding
```

Use `mut` for affected per-iteration scratch bindings and test multiple
iterations. Recheck after compiler/VM changes; do not turn this workaround into
a permanent language rule.

## Definition Of Done

- Behavior lives in the correct ecosystem layer.
- Inputs, outputs, bounds, effects, errors, authority, and stop conditions are
  explicit.
- Source is formatted, linted, checked, and executed on the required runtime.
- Relevant success, failure, boundary, denied, and deterministic paths pass.
- AI behavior has offline fixtures or strict replay.
- Effects have capability and approval boundaries.
- Affected tests, docs, examples, fixtures, lockfiles, and changelog agree.
- Only scoped files changed; commit/push/clean status is verified, not assumed.
- Remaining blockers have evidence and one exact next action.
