---
name: kujo-docs-drift-auditor
description: Use this skill when auditing Kujo documentation drift, README/reference mismatches, generated-doc staleness, CLI/docs drift, example validity, or recurring docs health using Concord, Scout, PatchBrief, Lens, DocGen, and Muzzle evidence.
---

# Kujo Docs Drift Auditor

Find documentation drift from source evidence and turn it into small, verifiable fixes.

## Scope

- Use for weekly/monthly docs drift checks across Kujo repos or for a focused repo after source changes.
- Compare docs against current code, CLI help, tests, examples, generated artifacts, and machine-readable contracts.
- Use Lens only when UI docs or screenshots require browser proof.
- Avoid broad process docs; report drift and precise fixes.

## Default Workflow

1. Identify target docs and source-of-truth artifacts.
2. Inspect `README.md`, `AGENTS.md`, docs, examples, tests, scripts, generated docs, and relevant `*.kujo` entrypoints.
3. Use Concord for artifact drift and CLI/docs mismatch leads.
4. Use Scout for repo context packs when the source surface is large.
5. Use PatchBrief to summarize doc/code deltas before creating tasks.
6. Use DocGen evidence for generated/public docs and gap outputs.
7. Use Lens for UI proof only when local web docs or screenshots are part of the claim.
8. Report each drift item with source file, target doc, evidence, and a minimal fix path.

## Evidence Sources

- Source: `README.md`, `AGENTS.md`, docs, examples, tests, scripts, `*.kujo`, `src/`, CLI help output, generated docs.
- Generated artifacts: DocGen outputs, Concord reports, Scout packs, PatchBrief summaries, Lens reports/screenshots.
- Historical context: recent commits, prior docs drift reports, Strata handoffs.

## Relevant Kujo Tools

- Use `kujo-concord-workflows` for docs/artifact drift checks.
- Use `kujo-scout-workflows` for large repo source mapping.
- Use `kujo-patchbrief-workflows` for changed-file summaries and suggested tests.
- Use `kujo-lens-workflows` when visual/UI docs need browser evidence.
- Use `kujo-docgen-agent-readable` for DocGen outputs, gaps, public-only gates, and README/reference alignment.
- Use `kujo-muzzle-workflows` for quiet recurring scans.

## Muzzle-First Terminal Guidance

- Prefer `muzzle run <workflow> --json` for Concord, Scout, PatchBrief, Lens, DocGen, and docs validation checks.
- Use `--dry-run` before broad generated-doc refreshes or any workflow that writes many files.
- When no Muzzle workflow exists, add a minimal workflow for the recurring docs check and keep generated logs/reports/state ignored.
- Use direct `rg`, `sed`, `ls`, and `git diff` only for light discovery and focused inspection.

## Validation

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kujo-docs-drift-auditor
../muzzle/muzzle run skill-check --json skills/kujo-docs-drift-auditor
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

For a real audit, validate every proposed doc fix against the source artifact or generated output that made it stale.

## Report Format

```markdown
# Kujo Docs Drift Audit

## Scope
- Repos:
- Docs:
- Source surfaces:

## Drift Findings
- Source of truth:
- Stale doc:
- Evidence:
- Severity:
- Minimal fix:

## Generated Docs
- DocGen or generated artifact:
- Status:
- Gap output:

## UI Proof
- Lens artifact:
- Result:

## Validation
- Workflow:
- Result:
- Artifact:
```
