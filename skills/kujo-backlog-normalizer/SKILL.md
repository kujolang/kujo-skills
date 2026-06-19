---
name: kujo-backlog-normalizer
description: Use this skill when converting Kujo audit findings, drift reports, release blockers, DocGen gaps, Dependabot/security triage, or recurring automation output into fix-ready backlog tasks using Scout, PatchBrief, ChangeBucket, Spec, ShipCheck, DocGen evidence, and RunLedger context.
---

# Kujo Backlog Normalizer

Turn evidence into fix-ready tasks. Preserve source, scope, severity, and acceptance evidence.

## Scope

- Use after readiness audits, docs drift audits, release gates, DocGen gap output, security triage, or dogfood runs.
- Normalize findings into actionable tasks with repo, owner role, acceptance evidence, dependencies, and suggested validation.
- Avoid vague roadmap prose and duplicate backlog items.

## Default Workflow

1. Gather raw findings and their evidence paths.
2. Deduplicate by repo, root cause, affected artifact, and acceptance evidence.
3. Use Scout for repo context, PatchBrief for changed-file summaries, ChangeBucket for footprint and risk, Spec for structured task contracts, ShipCheck for release blocker severity, DocGen gap outputs for docs tasks, Dependabot/security triage for vulnerable dependency tasks, and RunLedger for run provenance.
4. Split tasks until each has one owner role and one clear completion proof.
5. Mark blockers, dependencies, stale evidence, and tasks requiring human authorization.
6. Emit a compact backlog report or create approved task artifacts.

## Evidence Sources

- Audit reports, tool JSON/Markdown, Casefile bundles, RunLedger receipts, DocGen gaps, Dependabot/security triage summaries.
- Repo files: `README.md`, `AGENTS.md`, docs, tests, scripts, manifests, lockfiles, CI config.
- Prior backlog docs and Strata handoffs.

## Relevant Kujo Tools

- Use `kujo-scout-workflows` for repo context.
- Use `kujo-patchbrief-workflows` for diff and handoff context.
- Use `kujo-changebucket-workflows` for footprint and risk.
- Use `kujo-spec-workflows` when a task needs a structured `.spec.yml` contract.
- Use `kujo-shipcheck-workflows` for release-blocker severity.
- Use `kujo-docgen-agent-readable` for DocGen gaps and public-doc coverage tasks.
- Use `kujo-runledger-workflows` for provenance from scheduled runs.

## Muzzle-First Terminal Guidance

- Prefer `muzzle run <workflow> --json` when ingesting noisy reports or regenerating structured backlog inputs.
- Use `--dry-run` before broad task-file generation, issue creation, or security-related mutation.
- Use direct `rg`, `sed`, `git diff`, and `ls` only for focused evidence lookup.
- Do not create GitHub issues, mutate security alerts, or publish task boards unless explicitly authorized.

## Validation

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kujo-backlog-normalizer
../muzzle/muzzle run skill-check --json skills/kujo-backlog-normalizer
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

For generated task artifacts, validate syntax with the target tool, such as Spec validation for `.spec.yml` files.

## Report Format

```markdown
# Kujo Backlog Normalization Report

## Inputs
- Source report:
- Repos:
- Run evidence:

## Normalized Tasks
- ID:
- Repo:
- Title:
- Severity:
- Owner role:
- Evidence:
- Acceptance evidence:
- Suggested validation:
- Dependencies:

## Deduplicated Or Deferred
- Finding:
- Reason:

## Authorization Needed
- Action:
- Why:
```
