# Contributing

Contributions should keep each skill concise, operational, and backed by current Kujo repository evidence.

## Workflow

1. Create a focused branch.
2. Update the relevant `skills/<name>/SKILL.md` and its source references.
3. Update `SKILLS_INDEX.md` and routing fixtures when activation behavior changes.
4. Run the release-readiness gate.
5. Open a pull request describing the source-of-truth artifacts and validation used.

```bash
bash tests/release-readiness.sh
bash tests/clean-checkout.sh
```

Do not invent commands, flags, safety guarantees, or release status. Preserve VM-first execution, explicit capability boundaries, and the distinction between skill guidance and runtime enforcement.
