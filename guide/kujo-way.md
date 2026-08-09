# The Kujo Way

Status: extracted from repo evidence.

## Philosophy

Kujo is designed for local-first automation, agentic workflows, and application scripting where deterministic behavior, strong native capabilities, and practical ergonomics matter. The repo repeatedly emphasizes clarity, context, control, agent-readable tooling, and human-verifiable workflows.

Repo-backed evidence:

- `README.md`: Kujo is "the programming language for AI-native software" and is designed for local-first automation.
- `docs/CLI_MACHINE_READABLE_CONTRACTS.md`: machine-readable JSON and exit behavior are compatibility surfaces.
- `docs/FIRST_TOOL_COOKBOOK.md`: first practical tool is a deterministic JSON policy gate.
- `docs/NATIVE_API_SECURITY_POSTURE.md`: host-effect APIs must be controlled explicitly.
- `ROADMAP.md`: changed behavior requires tests and docs.

## What Kujo Is Good For

- Local CLI tools and quality gates.
- Agent-readable automation with stable JSON outputs.
- Filesystem/process/network/database/crypto automation when host effects are intentional.
- Package and module workflows with deterministic lockfile verification.
- Documentation generation and codebase analysis with bounded discovery.
- CI-friendly checks where stdout/stderr and exit codes matter.

## What Kujo Does Not Claim

- Do not claim Kujo is a sandbox.
- Do not claim full process/container isolation.
- Do not infer that every preview or experimental API is stable because Kujo `v1.0.0` is released.
- Do not treat experimental or preview native APIs as frozen.
- Do not treat legacy/expected-fail examples as current syntax.

Evidence:

- `README.md`, `docs/LANGUAGE_SPEC.md`, `docs/V1_SCOPE.md`, `docs/V1_0_OFFICIAL_RELEASE_CHECKLIST.md`: stable `v1.0.0` baseline and explicit deferrals.
- `docs/NATIVE_API_SECURITY_POSTURE.md`: sandboxing and kernel-level isolation are non-goals.
- `docs/STANDARD_LIBRARY_REFERENCE.md`: stable/preview/experimental tiers.
- `examples/README_examples.md`, `tests/docs_examples.rs`: expected-fail examples are non-canonical.

## Core Language Conventions

- Source files use `.kujo` and UTF-8.
- Prefer current canonical examples before large showcases.
- Use `let` for immutable bindings, `mut` for bindings that are reassigned or mutated, and `const` for constants.
- `name := value` without a binding keyword updates an existing mutable binding when present; otherwise it creates a mutable binding in the current scope.
- Unknown identifiers are runtime errors; quote strings explicitly.
- Dictionary missing keys and out-of-bounds indexing are runtime errors. Use `has_key`, `get`, or `get_default` for fallback behavior.
- Predicate helpers such as `contains`, `starts_with`, `ends_with`, and `has_key` return `1`/`0`; compare explicitly in control paths.
- Collection helpers such as `push`, `insert`, `remove_at`, `concat`, `map`, and `filter` return new values. Reassign when building collections.

## Runtime Posture

- Use `kujo run <file>` by default. It is VM-first.
- Use `kujo run --interpreter <file>` only for explicit compatibility/debug isolation.
- Use `kujo test --runtime dual` for legacy fixture compatibility sweeps.
- Use `kujo test --runtime vm` for strict VM-only migration gates.
- Add parity tests and update the parity matrix when changing runtime behavior.

## Tool-Building Conventions

- Use `args()` for script arguments; it excludes the script path.
- Use `--` to separate Kujo CLI flags from script flags.
- Validate inputs at the start of a tool.
- Use deterministic non-zero exits for automation: `2` usage, `1` gate/policy failure, `4` runtime/semantic failure.
- For machine-readable tools, put JSON on stdout and keep extra text minimal. Use `eprint` or stderr-friendly patterns for human diagnostics when stdout must remain JSON.
- Prefer small local helpers such as `section`, `kv`, `ok`, `fail`, or `print_lines` when output repeats.

## Security Posture

- Kujo is not a sandbox. Trusted mode runs with ambient process privileges.
- `kujo run` and `kujo test-run` default to trusted mode.
- For untrusted code, start with `--untrusted` and add only required `--allow-*` flags.
- Treat `--allow-all` as trusted/full ambient-host execution.
- Prefer `spawn_process([...])` and `pipe_commands([...])` over shell-string `execute(...)`.
- Do not pass untrusted input into shell strings.
- Treat archives, HTML responses, static serving, databases, secrets, and outbound network destinations as high-risk surfaces.
- Recommend external isolation for high-risk workflows: containers, service accounts, read-only filesystems, network ACLs, firewall policy, and secret isolation.

## Enterprise Posture

- Use deterministic JSON contracts and stable exit codes.
- Use `--json` surfaces only according to the documented stdout/stderr policy.
- Preserve compatibility for CLI/LSP JSON fields. Removing/renaming fields or changing types is breaking.
- Gate package workflows with `kujo package-install --frozen`.
- Record release evidence and command outcomes when release readiness is involved.
- Prefer versioned stable releases or reviewed commit pins for production automation.

## Testing And Release Posture

Use targeted tests after each logical change. For broad changes, expected gates include:

```bash
cargo fmt --check
cargo check
cargo test
cargo test --test docs_examples
cargo test --test readme_contracts
cargo test --test cli_contracts
cargo test --test cli_json_contracts
cargo test --test diagnostics_golden
cargo run -- test --runtime vm
cargo run -- test --runtime dual
```

Release-focused gates:

```bash
bash scripts/release_gate.sh --full
bash scripts/release_candidate_gate.sh --full
```

Security-focused gates:

```bash
cargo test --test native_api_security_boundaries
cargo test --test runtime_security
cargo test --test serve_command_integration
```

## Implementation Contribution Posture

- Read `docs/ARCHITECTURE.md` before changing subsystem boundaries.
- Keep lexer/parser diagnostics structured and deterministic.
- Keep compiler/VM behavior aligned with interpreter semantics or document intentional divergence.
- Do not patch symptoms when a shared abstraction is the correct fix.
- Native API changes must update docs, capability metadata, and tests.
- Unsafe/JIT boundaries must stay centralized and documented with regression coverage.

## What Agents Commonly Get Wrong

- Using `--interpreter` as the default recommendation for ordinary scripts.
- Copying examples from the expected-fail list.
- Claiming sandboxing from capability gates.
- Printing prose before JSON on stdout.
- Treating `push` and other collection helpers as in-place mutations.
- Assuming `has_key` returns boolean instead of `1`/`0`.
- Blindly updating snapshots without inspecting expected versus actual behavior.
- Changing CLI JSON shape without updating docs, tests, and changelog.
- Making release-readiness claims from the crate version alone.

## How To Review Kujo Changes

Ask:

1. Does behavior remain deterministic?
2. Does VM behavior match interpreter behavior or is divergence documented?
3. Are host effects capability-minimal and externally isolated when needed?
4. Are stdout, stderr, exit codes, and JSON payloads contract-safe?
5. Are docs, tests, examples, and implementation synchronized?
6. Is the change scoped to the subsystem that owns the behavior?
7. Does it respect `v1.0.0` compatibility commitments and explicit preview boundaries?
