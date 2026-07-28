# Launch Checklist

Current launch scope: `locally verified support/distribution technical preview`. The skill inventory validates locally, including current Workcell, SiteKit, Tribunal, Relay, and Redact workflow skills. Distribution marketplace actions and Workcell proof remain outside the completed local evidence.

## Local Gates

- [x] Skill inventory checked with `find skills -maxdepth 2 -name SKILL.md | sort`.
- [x] Required next-batch workflow skills checked by exact path.
- [x] Stale Ruff wording sweep checked with `rg -n "Ruff|ruff" README.md guide skills`.
- [x] Formatting checked with `git diff --check`.
- [ ] Workcell proof checked with `workcell run --file docs/workcell-launch-gate.json --repo .`.
- [ ] Clean-checkout install/use validation on a separate machine.

## Current External Blocker

Workcell proof is blocked by the local Docker image build/pull path. The Workcell base image could not be fetched from Docker Hub because `auth.docker.io` timed out.

Closest equivalent proof: local skill inventory, required-path checks, stale wording sweep, and formatting check.

Safe resume command:

```bash
cd /Users/robertdevore/2026/Kujolang/kujo-repos/workcell
DOCKER_HOST=unix:///Users/robertdevore/.colima/kujo-workcell/docker.sock docker build --tag kujolang/workcell-base:local docker/
cd /Users/robertdevore/2026/Kujolang/kujo-repos/kujo-skills
workcell run --file docs/workcell-launch-gate.json --repo .
```

## Forbidden Launch Actions

Marketplace distribution, live profile installation, public releases, final release tags, live credentials, branch-protection changes, force-pushes, and claims of runtime enforcement remain out of scope.
