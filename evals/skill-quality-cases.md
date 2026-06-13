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

## Case 9: Eval Release Gate

Prompt: "Create a Kujo Eval release gate for this CLI and make sure CI can publish machine-readable artifacts."

Expected:

- Trigger `kujo-eval-workflows`.
- Use VM-first `kujo run main.kujo run <suite> --json`.
- Prefer canonical examples before tests or historical checklists.
- Include command/path/env policy fields for CI or release stages.
- Mention `summary.json`, `cli-summary.json`, and `artifact-manifest.json`.
- Validate with `lint`, a focused suite run, and manifest verification when checksums are enabled.

## Case 10: PackWrite Agent Pack

Prompt: "Use PackWrite to turn this repo's MEGA_PROMPT.md into a validated agent pack and give me the implementation and review prompts."

Expected:

- Trigger `kujo-packwrite-workflows`.
- Run or recommend `packwrite doctor` and `packwrite config` before model generation.
- Prefer `packwrite init MEGA_PROMPT.md --dry-run` before writing `agent/`.
- Generate with explicit provider/model or resolved config, then run `packwrite validate`.
- Use `packwrite prompt deepseek` and `packwrite prompt codex-review` for handoff.
- Keep API keys in environment variables only and avoid overwriting an existing pack unless explicitly requested.

## Case 11: Spec Agent Contract

Prompt: "Create a `.spec.yml` for this feature, validate it, and export agent context for implementation."

Expected:

- Trigger `kujo-spec-workflows`.
- Prefer YAML in a project `specs/` directory.
- Include at least `name`, `goal`, and concrete acceptance criteria.
- Run `spec validate` before export.
- Use `spec export-agent-context` for the coding-agent handoff.
- Mention `SPEC_SAFE_WRITE` or template-source policy only when CI, regulated, or output-path constraints are relevant.

## Case 12: Casefile Failure Handoff

Prompt: "Capture this failing command with Casefile and give the next agent a handoff."

Expected:

- Trigger `kujo-casefile-workflows`.
- Use `kujo run --interpreter casefile.kujo -- capture --name <name> -- <argv...>`.
- Prefer argv after `--` over `--command` for complex commands.
- Review `case.md`, `case.json`, `combined.log`, `reproduction.md`, and `handoff.md`.
- Preserve redaction-by-default and avoid sharing plaintext artifacts until sensitivity is checked.

## Case 13: Concord Drift Scan

Prompt: "Run Concord on this repo and turn any artifact drift into prioritized tasks."

Expected:

- Trigger `kujo-concord-workflows`.
- Run `concord scan` before editing docs/specs/evals/manifests.
- Use `--format json` or `tasks` when structured follow-up is needed.
- Treat findings as drift leads for human review, not proof.
- State command, exit code, highest severity, category, and likely source/target artifact.

## Case 14: Dispatch Workflow Run

Prompt: "Run a Dispatch demo workflow, inspect the artifacts, and explain whether the approval/policy behavior looks healthy."

Expected:

- Trigger `kujo-dispatch-workflows`.
- Run from the Dispatch repo root with `kujo run --interpreter dispatch.kujo`.
- Prefer offline fixture mode and a `tests/tmp/<purpose>` output root for local validation.
- Inspect `state.json`, `trace.json` or `trace.md`, and `report.json` or `report.md` when present.
- Check approval gate status, policy-denied events, mutation audit records, and artifact contract metadata.

## Case 15: Fence Boundary Check

Prompt: "Set up Fence for this repo and explain the current architecture-boundary violations."

Expected:

- Trigger `kujo-fence-workflows`.
- Run or recommend `init`, then `validate`, then `check`.
- Use `graph` or `explain <path>` to understand zone direction and surprising classifications.
- Do not weaken `fence.toml` just to hide violations.
- Report exit code, violation threshold, report path, and next fixes.

## Case 16: Howl Showcase Render

Prompt: "Create a Howl card for this Kujo example, validate the manifest, and render the gallery."

Expected:

- Trigger `kujo-howl-workflows`.
- Use or create `howl.json` plus a real referenced example file.
- Run `howl validate` before `howl render`.
- Render deterministic Markdown, HTML, SVG, and `index.html` artifacts.
- Avoid invented claims, network calls, posting, or scheduler behavior.

## Case 17: Lens Browser QA

Prompt: "Run Lens against my localhost app and summarize the Agent Repair Brief."

Expected:

- Trigger `kujo-lens-workflows`.
- Ensure the app server is already running.
- Start with `lens check <local-url> --json`.
- Inspect `lens-report.md`, `lens-report.json`, screenshots, console, network, and DOM evidence.
- Branch on Lens exit codes and report findings with evidence paths.

## Case 18: MCP Server Scaffold

Prompt: "Generate a repo-specific MCP server with mcp make and review the safety surface."

Expected:

- Trigger `kujo-mcp-workflows`.
- Use `kujo run mcp.kujo --interpreter make <repo-path>`.
- Prefer `--dry-run`, `--no-ai`, or `--validate` when appropriate.
- Review `artifacts/safety-review.md`, `mcp.manifest.json`, and `repo-profile.json`.
- Keep generated capabilities least-privilege and do not expose arbitrary shell input.

## Case 19: PatchBrief Handoff

Prompt: "Run PatchBrief on this change and give me a handoff note plus suggested tests."

Expected:

- Trigger `kujo-patchbrief-workflows`.
- Use the Kujo `--` separator before PatchBrief arguments.
- Run or recommend `summarize`, `suggest-tests`, and `handoff`.
- Prefer JSON with `--pretty` only when a downstream tool or agent should parse it.
- Treat PatchBrief risks and test suggestions as heuristic and verify them against the actual diff.

## Case 20: Kujo RAG Local Corpus

Prompt: "Use Kujo RAG to index this docs folder, answer a question with citations, and tell me what tests matter if retrieval looks wrong."

Expected:

- Trigger `kujo-rag-workflows`.
- Run from the RAG repo root with `kujo run main.kujo --interpreter ingest --path <path> --recursive true`.
- Query with `kujo run main.kujo --interpreter query --question <question>` and inspect citation paths/line ranges.
- Preserve offline defaults unless the user explicitly asks for AI embeddings or remote vector backends.
- For retrieval problems, inspect retrieval/chunking/embedding modules and focused tests before wrapper suites.

## Case 21: Scent Context Pack

Prompt: "Use Scent to package this repo's current auth changes for a downstream Codex review."

Expected:

- Trigger `kujo-scent-workflows`.
- Run from inside the target repository.
- Start with `scent pack --dry-run --json`.
- Use a specific `--task`, changed-file focus flags, and task-relevant `--include` paths.
- Review `redactions.json` and keep generated pack output out of version control.

## Case 22: Scout Context Pack

Prompt: "Run Scout on this repo and summarize the generated agent context pack."

Expected:

- Trigger `kujo-scout-workflows`.
- Run `kujo run scout.kujo -- <target>` from the Scout repo or use the stable Scout entrypoint.
- Start from `scan_manifest.json` to locate generated artifacts.
- Summarize target, output directory, profile, code file count, route/dependency/security counts, and key follow-ups.
- Avoid claiming Scout is a security guarantee.

## Case 23: ShipCheck Release Gate

Prompt: "Run ShipCheck on this repo, review blockers, and tell me whether the release gate passes."

Expected:

- Trigger `kujo-shipcheck-workflows`.
- Run `scan` first for release-readiness findings.
- Run `gate` as the pass/fail enforcement step.
- Distinguish error-level blockers from warnings.
- State command, target directory, exit code, highest severity, and gate result.
