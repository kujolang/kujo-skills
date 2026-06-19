---
name: kujo-dependabot-alert-triage
description: Use this skill when triaging GitHub Dependabot or security alerts across Kujo repos, summarizing affected repositories/packages/severity/status/patched versions/PR state/next actions, creating fix-ready tasks, or maintaining a Strata running list. Do not dismiss alerts or mutate GitHub security state without explicit authorization.
---

# Kujo Dependabot Alert Triage

Triage dependency alerts into fix-ready tasks without exposing secrets or mutating security state by default.

## Scope

- Use for recurring weekly/monthly Dependabot or GitHub security alert triage across in-scope Kujo repos.
- Summarize affected repo, package, ecosystem, manifest/lockfile, severity, alert status, patched version, existing PR state, and next action.
- Create fix-ready tasks or Spec/backlog entries when authorized.
- Maintain a compact Strata running list after triage.

## Default Workflow

1. Confirm in-scope repos and whether this is read-only triage or authorized remediation.
2. Use only supported GitHub Dependabot/security alert surfaces available in the environment. If alert APIs are unavailable, report the blocker and fall back to manifests, lockfiles, Dependabot PRs, and audit outputs.
3. Inspect manifests, lockfiles, package manager files, CI, and existing Dependabot/security PRs.
4. Use PatchBrief and ChangeBucket to assess existing fix PRs or local remediation diffs.
5. Use Casefile for high-risk failing update evidence when reproduction logs matter.
6. Use RunLedger to record scheduled triage provenance.
7. Normalize results into tasks and save a compact Strata handoff or running-list update.

## Evidence Sources

- GitHub Dependabot/security alert surfaces, Dependabot PRs, security advisory metadata exposed by supported tools, manifests, lockfiles, audit reports, CI checks, and repository tests.
- PatchBrief summaries, ChangeBucket reports, Casefile bundles, RunLedger receipts, Spec/backlog output, Strata handoffs.

## Relevant Kujo Tools

- Use `kujo-patchbrief-workflows` for existing remediation PRs or local diffs.
- Use `kujo-changebucket-workflows` for blast radius and dependency-file footprint.
- Use `kujo-casefile-workflows` when a fix fails or high-risk evidence must be bundled.
- Use `kujo-runledger-workflows` for scheduled triage receipts.
- Use `kujo-spec-workflows` or `kujo-backlog-normalizer` for fix-ready tasks.
- Use Strata for the running list and session handoff.

## Muzzle-First Terminal Guidance

- Prefer `muzzle run <workflow> --json` for noisy audit, test, dependency, and report commands.
- Use `muzzle run <workflow> --dry-run` before dependency updates, broad writes, issue creation, PR creation, or any security-alert mutation.
- Direct commands are acceptable for light discovery: `git status`, `rg`, `sed`, `ls`, reading manifests, and checking existing branch state.
- Do not print or store tokens, secrets, exploit payloads, private advisory detail beyond what is necessary, or excessive advisory text.

## Safety Boundaries

- Do not dismiss alerts, mark alerts fixed, close security PRs, or mutate GitHub security state without explicit authorization.
- Do not store secrets, tokens, exploit detail, proof-of-concept payloads, or full advisory bodies in Strata or reports.
- Report unavailable alert APIs honestly.
- Treat package-manager audit output as evidence to verify, not as authority to edit unrelated dependencies.

## Validation

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kujo-dependabot-alert-triage
../muzzle/muzzle run skill-check --json skills/kujo-dependabot-alert-triage
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

For remediation work, also run the target repo's package-manager audit, tests, and release gates through Muzzle when available.

## Report Format

```markdown
# Kujo Dependabot Alert Triage

## Scope
- Repos:
- Mode: read-only | remediation-authorized
- Alert surface:

## Alerts
- Repo:
- Package:
- Ecosystem:
- Manifest or lockfile:
- Severity:
- Status:
- Patched version:
- Existing PR:
- Next action:

## Fix-Ready Tasks
- Task:
- Repo:
- Evidence:
- Acceptance evidence:
- Risk:

## Authorization Needed
- Mutation:
- Reason:

## Strata Running List
- Saved or pending:
- Retrieval cue:
```
