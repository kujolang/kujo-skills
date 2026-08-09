# Kujo Skills 0.1.0 Launch Evidence

- Evidence date: 2026-08-08
- Source branch: `weekly-kujo-skills-audit-2026-07-04`
- Source commit: `20c5b36`

## Portable repository gate

```bash
bash tests/release-readiness.sh
bash tests/clean-checkout.sh
```

Result: passed. The gate validated all 53 skill frontmatter records, exact folder/name alignment, the complete index and routing-fixture inventory, package/version/license consistency, local Markdown targets, the required five launch-batch skills, artifact-ignore policy, formatting, and a temporary-profile installation of `kujo-core-language`.

Sample skill-read evidence:

- `kujo-core-language`: frontmatter name matched its folder; description was present and within the supported contract.
- `kujo-workcell-workflows`, `kujo-site-kit-workflows`, `kujo-tribunal-workflows`, `kujo-relay-workflows`, and `kujo-redact-workflows`: exact `SKILL.md` paths were present.
- `SKILLS_INDEX.md`, `evals/expected-skill-map.md`, and `evals/trigger-queries.json`: each named the same 53-skill set.

A fresh local clone of commit `20c5b36` also passed both commands with a clean worktree.

## Spec and Eval

```bash
spec validate kujo-skills.spec.yml --strict --json
kujo run ../eval/main.kujo lint tests/eval.json
kujo run ../eval/main.kujo run tests/eval.json --output-dir eval_results/release-readiness --json
```

Result: Spec passed with no errors or warnings. Eval lint passed, and all three deterministic checks passed.

## Release readiness and drift

```bash
kujo run shipcheck.kujo gate --dir /path/to/kujo-skills --format json
./kujo run concord.kujo -- scan --dir /path/to/kujo-skills --format json
```

Result: ShipCheck exited `0` with `gate_passed: 1`, 14 passing checks, no error failures, and two non-applicable Kujo-entrypoint warnings for this support/distribution repository. Concord exited `0` with no findings and highest severity `none`.

## Workcell

```bash
workcell run --file docs/workcell-launch-gate.json --repo . --no-pull
workcell verify --run .workcell/runs/wc-6c5ec39e21e44606ac9fe6698e4a115d --json
```

Result:

- Backend: Docker through the local Colima Workcell host.
- Run: `wc-6c5ec39e21e44606ac9fe6698e4a115d`.
- Exit: `0`.
- Cleanup: complete.
- Verification: `ok: true`; manifest schema `workcell-manifest/v1`, six files, 7,521 bytes.
- Artifact: `kujo-skills-workcell-proof.txt` recorded version `0.1.0`, 53 skills, all five required workflow skills, and the isolated `kujo-core-language` installation.

The receipt and integrity manifest remain local generated evidence under `.workcell/runs/` and are intentionally excluded from version control.

## Remaining boundary

This evidence does not publish to a marketplace, install into a live agent profile, create a release tag, or prove that third-party agents enforce skill instructions.
