---
name: kujo-release-gate-runner
description: Use this skill when running Kujo release gates, recurring release-readiness automation, pre-tag checks, blocker triage, or monthly gate evidence collection across ShipCheck, Eval, Fence, ChangeBucket, RunLedger, Casefile, DocGen gates, and Muzzle workflows.
---

# Kujo Release Gate Runner

Run release gates as evidence-producing automation. Keep pass/fail signals tied to exact commands and artifacts.

## Scope

- Use before tags, releases, dependency updates, generated docs refreshes, or recurring release checks.
- Cover release readiness, eval correctness, architecture boundaries, change footprint, generated docs contracts, and failure evidence.
- Do not publish, deploy, tag, or mutate release state without explicit authorization and a supported workflow.

## Default Workflow

1. Confirm target repo, branch, version intent, and whether publishing/tagging is in scope.
2. Inspect release docs, `README.md`, `AGENTS.md`, changelog/release notes, CI config, tests, and manifests.
3. Run focused tests first when a recent change has an obvious blast radius.
4. Run release gates through Muzzle where available: ShipCheck, Eval, Fence, ChangeBucket, DocGen gates, and repo-specific release checks.
5. Capture failures with Casefile when logs or reproduction steps are needed.
6. Record run evidence with RunLedger when this is part of a multi-agent or scheduled release process.
7. Report blockers, warnings, artifacts, and exact next commands.

## Evidence Sources

- Release docs and scripts, CI config, changelog, manifests, lockfiles, generated docs, test suites.
- ShipCheck, Eval, Fence, ChangeBucket, DocGen, RunLedger, and Casefile artifacts.
- `git status`, `git log`, `git diff --stat`, and pushed branch status.

## Relevant Kujo Tools

- Use `kujo-shipcheck-workflows` for release scans and gates.
- Use `kujo-eval-workflows` for deterministic eval gates.
- Use `kujo-fence-workflows` for architecture boundary gates.
- Use `kujo-changebucket-workflows` for footprint and risk gates.
- Use `kujo-runledger-workflows` for release-run receipts.
- Use `kujo-casefile-workflows` for failure bundles.
- Use `kujo-docgen-agent-readable` for DocGen public-only, coverage, README/reference, and example smoke gates.
- Use `kujo-muzzle-workflows` for quiet orchestration.

## Muzzle-First Terminal Guidance

- Prefer `muzzle run <workflow> --json` for release, build, test, audit, DocGen, and gate commands.
- Use `muzzle run <workflow> --dry-run` before publish, deploy, tag, broad write, security-alert mutation, or networked workflows.
- If no release workflow exists, add a minimal Muzzle manifest that documents runner, args, timeout, and safety flags.
- Do not commit Muzzle logs, reports, state, or caches unless the repo explicitly tracks them.

## Validation

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kujo-release-gate-runner
../muzzle/muzzle run skill-check --json skills/kujo-release-gate-runner
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

For a real release gate, validate the repository's documented release command plus any ShipCheck/Eval/Fence/DocGen gates required by scope.

## Report Format

```markdown
# Kujo Release Gate Report

## Scope
- Repo:
- Branch:
- Release intent:
- Publishing authorized: yes/no

## Gate Results
- Gate:
- Workflow or command:
- Exit:
- Artifact:
- Status:

## Blockers
- Finding:
- Evidence:
- Required fix:

## Warnings
- Finding:
- Follow-up:

## Final Status
- Gate verdict:
- Commit or branch:
- Next action:
```
