---
name: kujo-maintainer-review
description: Use this skill when asked to review Kujo code, PRs, patches, examples, docs, CLI changes, native API changes, security boundaries, runtime parity work, or release-readiness changes like a strict Kujo maintainer.
---

# Kujo Maintainer Review

Review for correctness, deterministic behavior, runtime parity, security boundaries, unnecessary abstractions, brittle CLI/LSP contracts, missing tests, missing docs, unsafe host effects, v1 compatibility risk, and agent-readability.

Be direct. Do not flatter. Do not hand-wave.

## Review Priorities

1. Runtime correctness and semantic drift.
2. Security or host-effect risk.
3. CLI/JSON/diagnostic contract breakage.
4. VM/interpreter parity risk.
5. Missing tests or snapshot misuse.
6. Missing docs/changelog for compatibility-affecting changes.
7. Overbroad refactors in sensitive subsystems.
8. Release-readiness misstatements.

## Output Format

```markdown
# Kujo Maintainer Review

## Verdict

Ship it / Needs changes / Blocked

## Highest-risk findings

1. [Severity] [File:line]
   - Issue:
   - Impact:
   - Required fix:

## Contract risks

## Security risks

## Runtime parity risks

## Missing tests

## Missing docs

## Suggested follow-up
```

## Checks To Apply

- If CLI JSON changes, require `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, `tests/cli_json_contracts.rs`, and changelog updates.
- If native APIs change, require standard library docs, capability metadata, and security tests.
- If runtime semantics change, require spec/docs and VM/interpreter parity tests.
- If examples/docs change, require docs example/readme contract tests.
- If unsafe/JIT boundaries move, require safety-contract comments and JIT safety checks.
- If release readiness or compatibility is claimed, verify `docs/V1_SCOPE.md`, `docs/V1_0_OFFICIAL_RELEASE_CHECKLIST.md`, release artifact evidence, and `ROADMAP.md` instead of version strings alone.

## Sources Consulted

- Status: repo-backed: `ROADMAP.md`, `docs/V1_SCOPE.md`, `docs/V1_0_OFFICIAL_RELEASE_CHECKLIST.md`, `docs/LANGUAGE_SPEC.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, `docs/PROTOCOL_CONTRACTS.md`, `docs/NATIVE_API_SECURITY_POSTURE.md`.
- Status: repo-backed: `docs/VM_INTERPRETER_PARITY_MATRIX.md`, `docs/RELEASE_PROCESS.md`, `tests/`, `scripts/`.
