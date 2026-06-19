---
name: kujo-docgen-public-docs-refresh
description: Use this skill when refreshing Kujo DocGen public docs, generated documentation, agent-readable JSON/gap outputs, coverage gates, README/reference alignment, or example smoke policy after readiness or docs-drift evidence. Use `kujo docgen` and validate before committing; do not publish or deploy without explicit supported authorization.
---

# Kujo DocGen Public Docs Refresh

Refresh generated/public docs only from verified source evidence. Treat DocGen output as an agent-readable contract.

## Scope

- Use after readiness or docs-drift evidence shows generated/public docs, gap outputs, README/reference alignment, or examples are stale.
- Use `kujo docgen` and the `kujo-docgen-agent-readable` skill before choosing exact flags.
- Refresh generated docs, agent-readable JSON, gap outputs, coverage gates, and example smoke policy when the repo supports those outputs.
- Do not publish, deploy, upload, or release docs without explicit authorization and a supported workflow.

## Default Workflow

1. Read the target repo's `README.md`, `AGENTS.md`, DocGen docs, generated-doc policy, tests, and scripts.
2. Confirm the drift evidence from readiness/docs audits before writing generated files.
3. Run a Muzzle dry-run or documented non-writing preview when available.
4. Run the supported `kujo docgen` command for the target output, such as public-only, gap, AI task, or docs output modes documented in that repo.
5. Compare generated output against source changes, README/reference claims, and examples.
6. Run DocGen, CLI JSON, docs example, and README/reference validation required by the target repo.
7. Commit only source-owned generated/public docs and report skipped publish/deploy steps.

## Evidence Sources

- `docs/DOCGEN.md`, `docs/CLI_MACHINE_READABLE_CONTRACTS.md`, README/reference docs, examples, DocGen tests, generated output directories, gap JSON/Markdown, AI task output.
- Source modules under DocGen implementation and adapters when working in the Kujo compiler repo.
- Readiness and docs drift reports that justify the refresh.

## Relevant Kujo Tools

- Use `kujo-docgen-agent-readable` for DocGen model, flags, public-only gates, gap outputs, README/reference alignment, and example smoke policy.
- Use `kujo-docs-drift-auditor` before refresh when drift evidence is unclear.
- Use `kujo-release-gate-runner` when the refresh is part of a release gate.
- Use `kujo-muzzle-workflows` for quiet generated-doc and validation commands.

## Muzzle-First Terminal Guidance

- Prefer `muzzle run <workflow> --json` for DocGen refresh and validation commands.
- Use `muzzle run <workflow> --dry-run` before broad generated output writes when the workflow supports it.
- If no workflow exists, create a minimal Muzzle workflow that runs the repo-documented DocGen command and validation checks.
- Keep logs, reports, state, and caches out of commits unless the repo explicitly tracks them.

## Validation

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kujo-docgen-public-docs-refresh
../muzzle/muzzle run skill-check --json skills/kujo-docgen-public-docs-refresh
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

For the Kujo compiler repo, prefer the documented DocGen validation suite, including DocGen, CLI JSON contract, docs examples, and README contract tests when touched.

## Report Format

```markdown
# Kujo DocGen Public Docs Refresh

## Scope
- Repo:
- Source evidence:
- Outputs refreshed:

## Commands
- Workflow or command:
- Result:
- Artifact:

## Alignment Checks
- README/reference:
- Examples:
- Gap output:
- Public-only coverage:

## Skipped Actions
- Publish/deploy:
- Reason:

## Follow-Up
- Task:
- Acceptance evidence:
```
