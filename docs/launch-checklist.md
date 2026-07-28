# Launch Checklist

Current launch scope: `locally verified support/distribution technical preview`. The skill inventory and Workcell proof validate locally, including current Workcell, SiteKit, Tribunal, Relay, and Redact workflow skills. Distribution marketplace actions remain outside the completed local evidence.

## Local Gates

- [x] Skill inventory checked with `find skills -maxdepth 2 -name SKILL.md | sort`.
- [x] Required next-batch workflow skills checked by exact path.
- [x] Stale Ruff wording sweep checked with `rg -n "Ruff|ruff" README.md guide skills`.
- [x] Formatting checked with `git diff --check`.
- [x] Workcell proof checked with `workcell run --file docs/workcell-launch-gate.json --repo . --no-pull`.
- [ ] Clean-checkout install/use validation on a separate machine.

## Workcell Proof Notes

Workcell proof passed after building `kujolang/workcell-base:local` with `DOCKER_BUILDKIT=0`, using the Colima Workcell Docker host, and setting `TMPDIR` to a path under `/Users/robertdevore/2026/Kujolang/kujo-repos/.workcell-host-tmp` so the disposable worktree mount was visible inside the Colima VM.

Resume command:

```bash
export DOCKER_HOST=unix:///Users/robertdevore/.colima/kujo-workcell/docker.sock
export DOCKER_CONFIG=/tmp/kujo-next-batch-docker-config
export TMPDIR=/Users/robertdevore/2026/Kujolang/kujo-repos/.workcell-host-tmp
workcell run --file docs/workcell-launch-gate.json --repo . --no-pull
workcell verify --run .workcell/runs/<run-id> --json
```

## Forbidden Launch Actions

Marketplace distribution, live profile installation, public releases, final release tags, live credentials, branch-protection changes, force-pushes, and claims of runtime enforcement remain out of scope.
