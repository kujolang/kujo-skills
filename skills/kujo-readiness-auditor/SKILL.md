---
name: kujo-readiness-auditor
description: Use this skill when auditing Kujo repositories for recurring readiness posture, release preparedness, production gaps, evidence quality, or weekly/monthly readiness reports across ShipCheck, Fence, Eval, Concord, ChangeBucket, RunLedger, and Casefile outputs.
---

# Kujo Readiness Auditor

Audit readiness from repo-backed evidence. Treat readiness as a current evidence snapshot, not a permanent label.

## Scope

- Use for weekly or monthly readiness audits of one or more Kujo repos.
- Focus on release blockers, drift, architecture boundaries, test/eval health, change footprint, evidence gaps, and next actions.
- Do not claim universal enterprise readiness unless the repo's own gates and live-environment evidence support it.
- Do not create broad roadmap docs; produce an audit report or focused backlog items.

## Default Workflow

1. Identify target repos, branch, time window, and intended audience.
2. Recall prior readiness handoffs from Strata when available.
3. Inspect `README.md`, `AGENTS.md`, docs, tests, scripts, CI config, manifests, and recent commits.
4. Run or review current evidence from ShipCheck, Fence, Eval, Concord, ChangeBucket, RunLedger, and Casefile using their repo-specific skills before relying on tool output.
5. Classify each finding as blocker, risk, gap, stale evidence, or confirmed healthy.
6. Produce a concise report with command evidence, artifact paths, and owner-ready next actions.

## Evidence Sources

- Repository: `README.md`, `AGENTS.md`, `docs/`, `tests/`, `scripts/`, `*.kujo`, manifests, lockfiles, CI config.
- Tool outputs: ShipCheck scans/gates, Fence reports, Eval reports, Concord findings, ChangeBucket summaries, RunLedger receipts, Casefile bundles.
- History: recent commits, previous readiness docs, Strata handoffs, open backlog items.

## Relevant Kujo Tools

- Use `kujo-shipcheck-workflows` for release-readiness scans and gates.
- Use `kujo-fence-workflows` for architecture-boundary evidence.
- Use `kujo-eval-workflows` for deterministic evaluation suites.
- Use `kujo-concord-workflows` for artifact and docs drift.
- Use `kujo-changebucket-workflows` for change footprint and blast-radius evidence.
- Use `kujo-runledger-workflows` for agent-run receipts.
- Use `kujo-casefile-workflows` when failures need durable evidence bundles.

## Muzzle-First Terminal Guidance

- Prefer `muzzle run <workflow> --json` for noisy readiness, scan, audit, test, and gate commands.
- Use `muzzle run <workflow> --dry-run` before broad write, cleanup, publishing, deploy-like, or networked workflows.
- If no repo workflow exists, create a minimal `.muzzle/workflows/` script and manifest for the repeatable check; do not commit `.muzzle/logs/`, `.muzzle/reports/`, `.muzzle/state/`, or caches unless explicitly tracked.
- Direct commands are acceptable for light discovery: `git status`, `rg`, `sed`, `ls`, `git log`, and reading small files.

## Validation

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kujo-readiness-auditor
../muzzle/muzzle run skill-check --json skills/kujo-readiness-auditor
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

For a real audit, also run the target repo's current ShipCheck/Fence/Eval/Concord/ChangeBucket gates through Muzzle when available.

## Report Format

```markdown
# Kujo Readiness Audit

## Scope
- Repos:
- Branches:
- Time window:
- Requested cadence:

## Evidence Run
- Tool:
- Command or workflow:
- Result:
- Artifact:

## Findings
- Severity:
- Repo:
- Evidence:
- Impact:
- Next action:

## Confirmed Healthy
- Area:
- Evidence:

## Gaps And Unknowns
- Missing evidence:
- Required follow-up:

## Backlog Output
- Fix-ready task:
- Owner or role:
- Acceptance evidence:
```
