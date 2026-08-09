# Launch Checklist

Current launch scope: MIT-licensed `0.1.0` support/distribution technical preview. The portable repository gate and Workcell proof cover the full skill inventory and the required Workcell, SiteKit, Tribunal, Relay, and Redact workflow skills. Marketplace actions remain outside the completed evidence.

## Local Gates

- [x] Skill inventory checked with `find skills -maxdepth 2 -name SKILL.md | sort`.
- [x] Required next-batch workflow skills checked by exact path.
- [x] Stale Ruff wording sweep checked with `rg -n "Ruff|ruff" README.md guide skills`.
- [x] Formatting checked with `git diff --check`.
- [x] All skills, routing fixtures, metadata, and local Markdown links checked with `python3 scripts/validate_skills.py`.
- [x] Portable CI gate added through `tests/release-readiness.sh` and `.github/workflows/validate.yml`.
- [x] Workcell proof checked with `workcell run --file docs/workcell-launch-gate.json --repo . --no-pull`.
- [ ] Clean-checkout install/use validation on a separate machine.

## Workcell Proof Notes

Workcell proof uses the no-network `contained-standard` profile and asserts the `0.1.0` metadata, 53-skill inventory, public policy files, and all five required launch-batch skills. The local Colima host requires `TMPDIR` under `/Users/robertdevore/2026/Kujolang/kujo-repos/.workcell-host-tmp` so the disposable worktree mount is visible inside the VM.

Resume command:

```bash
export DOCKER_HOST=unix:///Users/robertdevore/.colima/kujo-workcell/docker.sock
export DOCKER_CONFIG=/tmp/kujo-next-batch-docker-config
export TMPDIR=/Users/robertdevore/2026/Kujolang/kujo-repos/.workcell-host-tmp
workcell run --file docs/workcell-launch-gate.json --repo . --no-pull
workcell verify --run .workcell/runs/<run-id> --json
```

## Forbidden Launch Actions

Marketplace distribution, live profile installation, release tags, live credentials, branch-protection changes, force-pushes, and claims of runtime enforcement remain out of scope for this local proof.
