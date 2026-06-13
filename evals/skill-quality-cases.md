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

## Case 8: Kujo RAG Local Corpus

Prompt: "Use Kujo RAG to index this docs folder, answer a question with citations, and tell me what tests matter if retrieval looks wrong."

Expected:

- Trigger `kujo-rag-workflows`.
- Run from the RAG repo root with `kujo run main.kujo --interpreter ingest --path <path> --recursive true`.
- Query with `kujo run main.kujo --interpreter query --question <question>` and inspect citation paths/line ranges.
- Preserve offline defaults unless the user explicitly asks for AI embeddings or remote vector backends.
- Use namespaces when isolating tenants/projects.
- For retrieval problems, inspect `src/retrieval.kujo`, `src/rag_engine.kujo`, `src/chunking.kujo`, and focused tests before the wrapper suite.

## Case 8: Scent Context Pack

Prompt: "Use Scent to package this repo's current auth changes for a downstream Codex review."

Expected:

- Trigger `kujo-scent-workflows`.
- Run from inside the target repository.
- Start with `scent pack --dry-run --json`.
- Use a specific `--task`, changed-file focus flags, and task-relevant `--include` paths.
- Write pack artifacts only after reviewing estimated tokens and warnings.
- Review `redactions.json` and keep generated pack output out of version control.

## Case 9: Howl Showcase Render

Prompt: "Create a Howl card for this Kujo example, validate the manifest, and render the gallery."

Expected:

- Trigger `kujo-howl-workflows`.
- Use or create `howl.json` plus a real referenced example file.
- Run `howl validate` before `howl render`.
- Render deterministic Markdown, HTML, SVG, and `index.html` artifacts.
- Avoid invented claims, network calls, posting, or scheduler behavior.
- Inspect generated artifacts or diffs when layout, escaping, or committed output changes.

## Case 11: ShipCheck Release Gate

Prompt: "Run ShipCheck on this repo, review blockers, and tell me whether the release gate passes."

Expected:

- Trigger `kujo-shipcheck-workflows`.
- Run `scan` first for release-readiness findings.
- Run `gate` as the pass/fail enforcement step.
- Distinguish error-level blockers from warnings.
- State the command, target directory, exit code, highest severity, and gate result.
- For ShipCheck source changes, keep `docs/check-catalog.md`, README examples, and `tests/cli-output-contract.sh` aligned.

## Case 12: Casefile Failure Handoff

Prompt: "Capture this failing command with Casefile and give the next agent a handoff."

Expected:

- Trigger `kujo-casefile-workflows`.
- Use `kujo run --interpreter casefile.kujo -- capture --name <name> -- <argv...>`.
- Prefer argv after `--` over `--command` for complex commands.
- Review `case.md`, `case.json`, `combined.log`, `reproduction.md`, and `handoff.md`.
- Preserve redaction-by-default and avoid sharing plaintext artifacts until sensitivity is checked.
- For Casefile code changes, keep `FLAGS.md`, `README.md`, `HOWTO.md`, and contract tests aligned.

## Case 13: PatchBrief Handoff

Prompt: "Run PatchBrief on this change and give me a handoff note plus suggested tests."

Expected:

- Trigger `kujo-patchbrief-workflows`.
- Use the Kujo `--` separator before PatchBrief arguments.
- Run or recommend `summarize`, `suggest-tests`, and `handoff`.
- Prefer JSON with `--pretty` only when a downstream tool or agent should parse it.
- Treat PatchBrief risks and test suggestions as heuristic and verify them against the actual diff.

## Case 14: Dispatch Workflow Run

Prompt: "Run a Dispatch demo workflow, inspect the artifacts, and explain whether the approval/policy behavior looks healthy."

Expected:

- Trigger `kujo-dispatch-workflows`.
- Run from the Dispatch repo root with `kujo run --interpreter dispatch.kujo`.
- Prefer offline fixture mode and a `tests/tmp/<purpose>` output root for local validation.
- Inspect `state.json`, `trace.json` or `trace.md`, and `report.json` or `report.md` when present.
- Check approval gate status, policy-denied events, mutation audit records, and artifact contract metadata.
- For Dispatch source changes, keep README examples, CLI JSON contracts, and `tests/dispatch_tests.kujo` aligned.

## Case 15: kujo-agents-sdk-workflows

Prompt: "Update an Agents SDK runner contract and run the offline example smoke path."

Expected:
- Trigger `kujo-agents-sdk-workflows`.
- Use `examples/examples_smoke_runner.kujo` and targeted contract tests.
- Preserve deterministic offline/no-network behavior.

## Case 16: kujo-ai-chat-workflows

Prompt: "Start AI Chat locally, run smoke tests, and review the SSE endpoint behavior."

Expected:
- Trigger `kujo-ai-chat-workflows`.
- Set explicit local env vars and avoid real secrets.
- Use `npm run smoke` against the running app.

## Case 17: kujo-ai-sdk-workflows

Prompt: "Fix AI SDK provider fixture mode and run contract plus redaction tests."

Expected:
- Trigger `kujo-ai-sdk-workflows`.
- Default to fixture mode without provider keys.
- Run SDK contract and security redaction suites.

## Case 18: kujo-changebucket-workflows

Prompt: "Measure the current git diff with ChangeBucket and enforce a footprint budget."

Expected:
- Trigger `kujo-changebucket-workflows`.
- Treat the tool as read-only git inspection.
- Report footprint, categories, budget result, and exit code.

## Case 19: kujo-cms-workflows

Prompt: "Run the CMS contract suite after adding a content model route."

Expected:
- Trigger `kujo-cms-workflows`.
- Use `backend/runtime/main.kujo` as the runtime entrypoint.
- Run contract tests and focused smoke/release checks.

## Case 20: kujo-crud-api-workflows

Prompt: "Change the CRUD API item handler and validate backend plus frontend quality gates."

Expected:
- Trigger `kujo-crud-api-workflows`.
- Run API smoke/regression checks and frontend lint/build when touched.
- Keep CRUD API distinct from CMS.

## Case 21: kujo-eval-workflows

Prompt: "Create an Eval suite with snapshot checks and produce a JSON report."

Expected:
- Trigger `kujo-eval-workflows`.
- Use machine-readable report formats when downstream tools consume output.
- Update snapshots only when behavior intentionally changed.

## Case 22: kujo-fence-workflows

Prompt: "Initialize Fence in a repo, run check, and explain any boundary violation."

Expected:
- Trigger `kujo-fence-workflows`.
- Use `fence.toml`, `check`, and `explain` workflows.
- Treat exit 1 as found violations, not a crash.

## Case 23: kujo-kennel-workflows

Prompt: "Validate Kennel trust policy and local dependency install behavior."

Expected:
- Trigger `kujo-kennel-workflows`.
- Inspect manifests, lockfiles, trust/source policy, and resolver code.
- Run Kennel verification scripts or targeted contract tests.

## Case 24: kujo-packwrite-workflows

Prompt: "Generate a PackWrite agent pack from MEGA_PROMPT.md in dry-run mode."

Expected:
- Trigger `kujo-packwrite-workflows`.
- Use `packwrite init --dry-run` before writing `/agent` artifacts.
- Validate generated packs and avoid overwriting user packs casually.

## Case 25: kujo-runledger-workflows

Prompt: "Record a Codex run receipt, finish it, and generate a report."

Expected:
- Trigger `kujo-runledger-workflows`.
- Use `start`, `usage`/`cost` as needed, `finish`, then `report`.
- Keep `.runledger/` local unless explicitly requested.

## Case 26: kujo-scout-workflows

Prompt: "Run Scout quick scan and export security findings for CI review."

Expected:
- Trigger `kujo-scout-workflows`.
- Use `--quick` or focused include/exclude flags for large repos.
- Review generated results, SARIF/JSONL, and baselines before committing.

## Case 27: kujo-spec-workflows

Prompt: "Validate, render, and export agent context from a `.spec.yml` task contract."

Expected:
- Trigger `kujo-spec-workflows`.
- Run `spec validate`, `render`, and `export-agent-context`.
- Keep schema, examples, command inventory, and completions aligned.

## Case 28: kujo-ssg-workflows

Prompt: "Build the SSG starter site and validate generated output before release."

Expected:
- Trigger `kujo-ssg-workflows`.
- Run `kujo run ./build.kujo -- ...` and generated-output validation.
- Do not hand-edit `output/`.

## Case 29: kujo-watchdog-workflows

Prompt: "Start Watchdog and verify proxy config plus telemetry redaction behavior."

Expected:
- Trigger `kujo-watchdog-workflows`.
- Use loopback-local dashboard/proxy checks.
- Avoid logging or committing real API keys, tokens, or telemetry DBs.

