---
name: kujo-cross-repo-dogfood-runner
description: Use this skill when running recurring cross-repo Kujo dogfood checks, weekly/monthly ecosystem automation, tool interoperability audits, or multi-repo evidence collection using Concord, Fence, Scout, ChangeBucket, PatchBrief, Scent, RunLedger, Casefile, DocGen, and Muzzle.
---

# Kujo Cross-Repo Dogfood Runner

Run cross-repo dogfood checks as narrow, auditable batches. Prefer evidence over broad conclusions.

## Scope

- Use for recurring ecosystem checks across selected Kujo repos.
- Cover artifact drift, boundary checks, repo intelligence, change footprint, diffs, handoff packs, run receipts, failure bundles, and DocGen health.
- Keep each run bounded by repo list, time window, and check list.
- Do not make broad repo-wide rewrites unless the user explicitly scopes them.

## Default Workflow

1. Select in-scope repos and confirm whether the run is read-only, fix-forward, or report-only.
2. Check each repo's `README.md`, `AGENTS.md`, docs, manifests, tests, and recent commits.
3. Run Muzzle-wrapped checks where available; otherwise add a minimal local workflow for repeated dogfood commands.
4. Use Concord for drift, Fence for architecture, Scout for context packs, ChangeBucket for footprint, PatchBrief for diffs, Scent for handoff packs, RunLedger for receipts, Casefile for failures, and DocGen for generated docs/gaps.
5. Normalize findings into repo-scoped status, evidence, and next actions.
6. Commit only requested source changes; keep generated dogfood artifacts ignored unless explicitly tracked.

## Evidence Sources

- Repo docs, `AGENTS.md`, tests, scripts, entrypoint `*.kujo` files, manifests, lockfiles, CI config.
- Tool reports from Concord, Fence, Scout, ChangeBucket, PatchBrief, Scent, RunLedger, Casefile, and DocGen.
- Git state: branch, dirty tree, recent commits, changed files.

## Relevant Kujo Tools

- Use `kujo-concord-workflows`, `kujo-fence-workflows`, `kujo-scout-workflows`, `kujo-changebucket-workflows`, `kujo-patchbrief-workflows`, `kujo-scent-workflows`, `kujo-runledger-workflows`, `kujo-casefile-workflows`, `kujo-docgen-agent-readable`, and `kujo-muzzle-workflows` as needed by the selected checks.

## Muzzle-First Terminal Guidance

- Prefer `muzzle run <workflow> --json` for every noisy per-repo check.
- Use `--dry-run` before broad multi-repo writes, cleanup, publishing, security mutation, or generated-doc refreshes.
- If a reusable workflow is missing, create the smallest repo-local Muzzle workflow and manifest that can be rerun weekly.
- Keep logs/reports/state/caches out of commits unless source-owned by the repo.

## Validation

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kujo-cross-repo-dogfood-runner
../muzzle/muzzle run skill-check --json skills/kujo-cross-repo-dogfood-runner
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

For a real run, validate at least one representative repo end to end before scaling the same workflow across the batch.

## Report Format

```markdown
# Kujo Cross-Repo Dogfood Report

## Scope
- Repos:
- Mode: read-only | fix-forward | report-only
- Time window:

## Repo Results
- Repo:
- Checks:
- Status:
- Artifacts:
- Findings:
- Next action:

## Cross-Repo Patterns
- Pattern:
- Evidence:
- Suggested owner:

## Failures
- Repo:
- Casefile or log:
- Reproduction:

## Follow-Up Queue
- Task:
- Repo:
- Acceptance evidence:
```
