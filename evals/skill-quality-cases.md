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

## Case 13: Dispatch Workflow Run

Prompt: "Run a Dispatch demo workflow, inspect the artifacts, and explain whether the approval/policy behavior looks healthy."

Expected:

- Trigger `kujo-dispatch-workflows`.
- Run from the Dispatch repo root with `kujo run --interpreter dispatch.kujo`.
- Prefer offline fixture mode and a `tests/tmp/<purpose>` output root for local validation.
- Inspect `state.json`, `trace.json` or `trace.md`, and `report.json` or `report.md` when present.
- Check approval gate status, policy-denied events, mutation audit records, and artifact contract metadata.
- For Dispatch source changes, keep README examples, CLI JSON contracts, and `tests/dispatch_tests.kujo` aligned.

## Case 8: Kujo RAG Local Corpus

Prompt: "Use Kujo RAG to index this docs folder, answer a question with citations, and tell me what tests matter if retrieval looks wrong."

Expected:

- Trigger `kujo-rag-workflows`.
- Run from the RAG repo root with `kujo run main.kujo --interpreter ingest --path <path> --recursive true`.
- Query with `kujo run main.kujo --interpreter query --question <question>` and inspect citation paths/line ranges.
- Preserve offline defaults unless the user explicitly asks for AI embeddings or remote vector backends.
- Use namespaces when isolating tenants/projects.
- For retrieval problems, inspect `src/retrieval.kujo`, `src/rag_engine.kujo`, `src/chunking.kujo`, and focused tests before the wrapper suite.

## Case 12: Casefile Failure Handoff

Prompt: "Capture this failing command with Casefile and give the next agent a handoff."

Expected:

- Trigger `kujo-casefile-workflows`.
- Use `kujo run --interpreter casefile.kujo -- capture --name <name> -- <argv...>`.
- Prefer argv after `--` over `--command` for complex commands.
- Review `case.md`, `case.json`, `combined.log`, `reproduction.md`, and `handoff.md`.
- Preserve redaction-by-default and avoid sharing plaintext artifacts until sensitivity is checked.
- For Casefile code changes, keep `FLAGS.md`, `README.md`, `HOWTO.md`, and contract tests aligned.
