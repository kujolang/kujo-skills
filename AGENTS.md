# Kujo Skills Agent Instructions

This repository distributes Kujo-focused Codex/agent skills. Treat it as a support/distribution repository; it does not enforce runtime behavior by itself.

## Required Reading

- `README.md`
- `guide/README.md`
- `docs/launch-checklist.md`
- Relevant `skills/*/SKILL.md`

## Validation

```bash
bash tests/release-readiness.sh
bash tests/clean-checkout.sh
```

## Evidence Rules

- Preserve skill inventory and sample skill-read validation logs for launch proof.
- Keep skill names, descriptions, commands, and repo paths exact.
- Do not imply third-party agents will obey skills without runtime enforcement.
- Workcell proof is required for this launch batch unless a blocker receipt documents the Docker/host blocker and closest equivalent proof.

## Prohibited Without Approval

Do not publish to a marketplace, install into a user's live agent profile, use live credentials, alter branch protection, force-push, rewrite history, or discard user changes.
