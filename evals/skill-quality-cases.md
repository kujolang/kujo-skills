# Skill Quality Cases

## Case 1: JSON Policy Gate

Prompt: "Build me a Kujo script that reads a JSON policy and exits nonzero if it fails."

Expected:

- Trigger `kujo-tool-building`.
- Use `args()`.
- Mention `--` separator.
- Use `parse_json`.
- Use `exit(2)` for usage and `exit(1)` for gate failure.
- Prefer VM default.

## Case 2: Untrusted File Scanner

Prompt: "Can I safely run this Kujo repo scanner on untrusted files in CI?"

Expected:

- Trigger `kujo-security-hardening` and `kujo-enterprise-automation`.
- State Kujo is not a sandbox.
- Recommend `--untrusted --allow-fs-read` only if read-only scanning is enough.
- Recommend external isolation for high-risk/shared CI.

## Case 3: VM/Interpreter Drift

Prompt: "Why does VM and interpreter give different results for this match expression?"

Expected:

- Trigger `kujo-runtime-parity`.
- Reproduce both paths.
- Check parity matrix.
- Add parity test or document intentional divergence.

## Case 4: CLI JSON Change

Prompt: "Make `kujo docgen --json` easier for agents to parse."

Expected:

- Trigger `kujo-cli-contracts` and `kujo-docgen-agent-readable`.
- Preserve existing fields and add optional fields.
- Update contract docs/tests/changelog.
- Use typed builder in DocGen core.

## Case 5: Native Builtin Addition

Prompt: "Add a native filesystem helper for checking symlinks."

Expected:

- Trigger `kujo-standard-library`, `kujo-language-implementation`, and `kujo-security-hardening`.
- Add capability metadata.
- Update stdlib docs.
- Add tests.

## Case 6: Strict Review

Prompt: "Review this change like a strict Kujo maintainer."

Expected:

- Trigger `kujo-maintainer-review`.
- Use the required review format.
- Lead with risks and required fixes.

## Case 7: Muzzle Workflow Setup

Prompt: "Set up Muzzle so agents can run this repo's build and tests without dumping huge logs into context."

Expected:

- Trigger `kujo-muzzle-workflows`.
- Use `muzzle init` if `.muzzle/` is missing.
- Create scripts under `.muzzle/workflows/`.
- Add manifests with summaries, runner/script fields, argument docs, and honest safety flags.
- Prefer `muzzle run <workflow> --json` for agent-readable status.
- Keep `.muzzle/logs/` and `.muzzle/reports/` out of version control.

## Case 8: RunLedger Receipt Capture

Prompt: "Track this same build prompt across Codex, Claude, and DeepSeek with RunLedger and make a report."

Expected:

- Trigger `kujo-runledger-workflows`.
- Start one run per provider/model with the same `--task` and prompt file.
- Record usage/cost only when supplied; do not invent provider pricing.
- Finish each run with a terminal status and human verdict.
- Use `compare --task` and `report --task --output RUNLEDGER_REPORT.md`.
- Treat `.runledger/` and generated reports as local/generated unless explicitly requested.
