---
name: kujo-loop-engineering-workflows
description: "Use this skill when an agent should work through a bounded engineering task in an arbitrary repository with the Kujo loop-engineering harness: repo-local `.loop-engineering/` initialization, Markdown checklist classification, scoped local fixes only, deterministic eval gates, per-iteration evidence, structured external blockers, optional small commits/pushes, optional Strata handoff, and a fixed final summary contract."
---

# Kujo Loop Engineering Workflows

Use the Loop Engineering harness to make agent work bounded, evidence-backed, and honest about blockers.

Canonical harness path:

```bash
/Users/robertdevore/2026/Kujolang/kujo-repos/kujo-workflows/loop-engineering
```

If this path does not exist in the current environment, locate the `kujo-workflows/loop-engineering` checkout before continuing.

## Core Contract

Follow this loop:

```text
Goal -> Context -> Act -> Evaluate -> Record -> Stop
```

Do not run placeholder/demo work unless the user explicitly asks for a demo. Do not report success when work is blocked by private registry access, SSH/Git push failures, CI/release pipeline ownership, human approval, contract-first scope, or out-of-repo changes.

## Initialize A Target Repo

From the target repository:

```bash
/Users/robertdevore/2026/Kujolang/kujo-repos/kujo-workflows/loop-engineering/scripts/init-repo-loop.sh
```

This creates:

```text
.loop-engineering/
  loop.yml
  ledger.tsv
  SUMMARY.md
  iterations/
  blockers.md
  evidence/
```

Edit `.loop-engineering/loop.yml` for the specific task:

- Set `objective`.
- Set `checklist_file` when a Markdown checklist exists.
- Keep `allowed_actions` scoped to local repo work unless the user explicitly broadens scope.
- Keep deploy, destructive cleanup, production config changes, release actions, and contract changes blocked unless explicitly approved.
- Configure `eval_gates` with the repo's real install/test/lint/typecheck/build commands.
- Enable commits only when requested.
- Set `commit.push: true` only when the user explicitly asks for push behavior.

## Checklist Mode

When a Markdown task checklist exists, run:

```bash
/Users/robertdevore/2026/Kujolang/kujo-repos/kujo-workflows/loop-engineering/scripts/run-workflow.sh --checklist path/to/checklist.md
```

Classify each item as:

- `local-fixable`
- `already-done`
- `external-blocked`
- `policy-blocked`
- `requires-human-approval`
- `out-of-repo`
- `needs-contract-first`
- `needs-release-pipeline`

Only implement `local-fixable` items. Record every other item in `.loop-engineering/SUMMARY.md`, `.loop-engineering/checklist.tsv`, or `.loop-engineering/blockers.md` with evidence and exact next action.

## Config Mode

For normal execution, run:

```bash
/Users/robertdevore/2026/Kujolang/kujo-repos/kujo-workflows/loop-engineering/scripts/run-workflow.sh --config .loop-engineering/loop.yml
```

Use `LOOP_ACT_CMD` only when a deterministic local action command is available:

```bash
LOOP_ACT_CMD="your-agent-or-script-command" \
/Users/robertdevore/2026/Kujolang/kujo-repos/kujo-workflows/loop-engineering/scripts/run-workflow.sh --config .loop-engineering/loop.yml
```

The Bash harness records and gates work; it does not replace the current agent's responsibility to inspect code, implement local-fixable changes, and verify results.

## Evidence Requirements

Every iteration should leave:

```text
.loop-engineering/iterations/NNN/
  context.md
  action.md
  diff.patch
  eval.log
  verdict.yml
```

When a gate fails, inspect the relevant `eval.log` or per-gate log. If the failure is external, normalize it into `.loop-engineering/blockers.md` instead of retrying blindly.

## External Blockers

Treat these as blockers, not task failures or success:

- Private package registry/auth failures, including `ERR_PNPM_TARBALL_URL_MISMATCH`, `E401`, `403`, missing auth headers, or private Composer/NPM auth errors.
- Remote Git/SSH failures, including connection refused, public key denial, or unavailable remote.
- Network/DNS failures.
- Required human approval.
- Release pipeline, protected branch, CI ownership, or release-manifest gaps.
- Contract-first changes that must start in another repo or source-of-truth package.

Record blockers with:

```yaml
blockers:
  - id: private-registry-auth
    command: "pnpm install --frozen-lockfile"
    evidence: "..."
    status: external-blocked
    next_action: "Restore private registry/auth/policy access."
```

## Commit And Push Policy

Commit only when requested or configured:

```yaml
commit:
  enabled: true
  strategy: small_meaningful
  push: false
```

Use small meaningful commits. If `push: true` and push fails, record the push as an external blocker and do not call the workflow successful because local work committed.

## Optional Strata Hook

When requested, configure:

```yaml
memory:
  enabled: true
  provider: strata
  project: "Agent Notes"
  mode: consolidate
  retrieval_tests: true
```

Save one session handoff, one atomic memory for completed durable state, one TODO/commitment memory for remaining external blockers, and retrieval test results. Deduplicate against existing Strata notes before writing.

## Final Report Contract

End with exactly this shape:

```markdown
# Loop Engineering Summary

## Verdict

success | partial | blocked | failed

## Completed

- ...

## Verification

- passed: ...
- blocked: ...
- failed: ...

## Commits

- ...

## Remaining

- ...

## External Blockers

- ...

## Next Start

- ...
```

Keep the final answer concise. Include whether verification passed, whether changes were committed/pushed, and any unresolved blockers.
