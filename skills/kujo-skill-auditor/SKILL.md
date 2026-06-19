---
name: kujo-skill-auditor
description: Use this skill when reviewing, refreshing, or auditing the Kujo skills pack so each `skills/*/SKILL.md` file matches current Kujo tool behavior, commands, docs, tests, safety boundaries, and repo reality. Use for weekly skill maintenance, stale skill checks, trigger/index updates, or when Kujo tools changed and their agent skills may need synchronization.
---

# Kujo Skill Auditor

Audit Kujo skills against the actual current tool repositories. Treat `SKILL.md` files as operational contracts for future agents, not as marketing copy.

## Audit Rules

- Verify behavior from repo artifacts before editing: `README.md`, `AGENTS.md`, docs, command inventories, manifests, entrypoint `.kujo` files, tests, scripts, and recent commits.
- Keep skills short, imperative, and repo-backed. Preserve the existing Kujo skill style.
- Update only claims that are stale, incomplete, misleading, or missing important safety/test/CLI contract details.
- Do not invent commands, flags, artifacts, tests, release status, or safety guarantees.
- Do not hand-edit generated output in target tool repos unless that tool's docs say it is source-owned.

## Scope Discovery

Start in the skills repo, usually `kujo-skills`.

```bash
rg --files skills -g 'SKILL.md'
sed -n '1,220p' SKILLS_INDEX.md
sed -n '1,220p' evals/expected-skill-map.md
```

If no scope is specified, audit all Kujo tool workflow skills. For weekly maintenance, prioritize tool repos changed in the last 7-10 days:

```bash
for repo in ../*; do
  [ -d "$repo/.git" ] || continue
  git -C "$repo" log --since='10 days ago' --oneline -- README.md AGENTS.md docs src tests '*.kujo' scripts 2>/dev/null | sed "s#^#$(basename "$repo"): #"
done
```

Map skills to repos with `SKILLS_INDEX.md` first. Otherwise infer from the skill name: `kujo-runledger-workflows` maps to `../runledger`, `kujo-ai-chat-workflows` maps to `../ai-chat`, and core language/runtime skills map to `../kujo`.

## Per-Skill Review

For each audited skill:

1. Read the current `skills/<skill>/SKILL.md` and its `SKILLS_INDEX.md` row.
2. Inspect the target repo's source-of-truth files:
   - `README.md`, `AGENTS.md`, `docs/`, `SECURITY.md`, `CONTRIBUTING.md`
   - main entrypoints such as `*.kujo`, `src/*.kujo`, `server.js`, `backend/runtime/main.kujo`
   - tests and smoke scripts
   - specs/manifests such as `.spec.yml`, `eval.json`, `action.yml`, config examples
3. Search for changed or drift-prone surfaces:
   - command names, flags, subcommands, exit codes, JSON fields, artifact paths
   - default runtime mode, fixture/offline behavior, network/provider requirements
   - safety boundaries, auth/secrets handling, destructive operations
   - release gates, smoke tests, contract tests, generated-output rules
4. Compare the skill against the repo reality:
   - frontmatter triggers are specific enough and still accurate
   - workflow steps match current commands and expected artifacts
   - validation commands are real and focused
   - source references name files that still exist
   - no stale claim overstates readiness, security, automation, or AI behavior

Use `rg` for targeted evidence:

```bash
rg -n "usage|command|--json|--format|exit|artifact|smoke|test|fixture|offline|security|redact|release" README.md AGENTS.md docs src tests scripts *.kujo 2>/dev/null
```

## Editing Rules

- Make the smallest useful update to each stale skill.
- Prefer replacing stale specifics with current repo-backed specifics over adding broad caveats.
- If tool behavior changed enough to alter routing, update `SKILLS_INDEX.md`, `evals/expected-skill-map.md`, and `evals/trigger-queries.json`.
- If a skill becomes too broad, split the concern into trigger text, core workflow, and validation rather than adding long prose.
- Leave a skill unchanged when repo evidence confirms it is still accurate.

## Validation

Run the skill validator for changed skills:

```bash
python3 /Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

Also sanity-check the package:

```bash
git diff -- skills SKILLS_INDEX.md evals
python3 -m json.tool evals/trigger-queries.json >/dev/null
```

## Report Format

```markdown
# Kujo Skill Audit

## Scope
- Skills reviewed:
- Tool repos checked:
- Time window:

## Updated
- `skill-name`: what changed and why, with source files consulted

## Confirmed Current
- `skill-name`: key evidence

## Drift Found But Not Fixed
- Blocker or reason:

## Validation
- Commands run:
- Results:

## Next Watchlist
- Tool areas likely to need attention next week:
```
