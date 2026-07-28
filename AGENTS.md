# Kujo Skills Agent Instructions

This repository distributes Kujo-focused Codex/agent skills. Treat it as a support/distribution repository; it does not enforce runtime behavior by itself.

## Required Reading

- `README.md`
- `guide/README.md`
- `docs/launch-checklist.md`
- Relevant `skills/*/SKILL.md`

## Validation

```bash
find skills -maxdepth 2 -name SKILL.md | sort
test -f skills/kujo-workcell-workflows/SKILL.md
test -f skills/kujo-site-kit-workflows/SKILL.md
test -f skills/kujo-tribunal-workflows/SKILL.md
test -f skills/kujo-relay-workflows/SKILL.md
test -f skills/kujo-redact-workflows/SKILL.md
rg -n "Ruff|ruff" README.md guide skills
git diff --check
```

## Evidence Rules

- Preserve skill inventory and sample skill-read validation logs for launch proof.
- Keep skill names, descriptions, commands, and repo paths exact.
- Do not imply third-party agents will obey skills without runtime enforcement.
- Workcell proof is required for this launch batch unless a blocker receipt documents the Docker/host blocker and closest equivalent proof.

## Prohibited Without Approval

Do not publish to a marketplace, install into a user's live agent profile, use live credentials, alter branch protection, force-push, rewrite history, or discard user changes.
