# Kujo Skills Validation Report

**Validation date:** 2026-07-10

## Scope

- Skill folders discovered: 46
- Frontmatter/folder-name agreement: 46/46
- Trigger-query map coverage: 46/46
- Expected-skill-map coverage: 46/46
- Machine-specific path scan in `SKILL.md` files: no matches

## Validation evidence

Every folder under `skills/` contains one `SKILL.md` whose frontmatter `name`
matches its folder name. `evals/trigger-queries.json` supplies trigger and
non-trigger examples for every current skill; the expected-map catalog now also
covers every skill, including `kujo-loop-engineering-workflows`.

The validation uses the Agent Skills structural validator for each skill,
Python JSON parsing for the trigger map, and a cross-file name-set comparison.
It proves collection structure and routing coverage; it does not prove that a
particular external tool, provider, browser, or credentialed integration is
available on every host.

## Trigger and safety review

- Trigger/non-trigger examples are present for all 46 skills.
- The existing skill contracts retain their explicit safety boundaries for
  filesystem, process, network, provider, release, and publication work.
- Collection-wide adversarial routing remains a follow-up: add runnable
  evaluator assertions that verify a router rejects unsafe or out-of-scope
  activations rather than treating descriptive examples as execution proof.

## Remaining release blockers

- The checkout is on `weekly-kujo-skills-audit-2026-07-04`, not `main`.
- No collection-level CI/release/version/license/changelog policy was confirmed
  in this pass.
- Kujo v1 wording must be reconciled after the core release state changes.

## Re-run commands

```bash
find skills -mindepth 2 -maxdepth 2 -name SKILL.md -print
python3 -m json.tool evals/trigger-queries.json >/dev/null
```
