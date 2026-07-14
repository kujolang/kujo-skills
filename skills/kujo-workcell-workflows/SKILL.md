---
name: kujo-workcell-workflows
description: "Use this skill when initializing, validating, inspecting, running, verifying, cleaning, or maintaining Workcell local Docker/Podman execution sandboxes: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `.workcell/runs/`, receipts, manifests, artifacts, runtime boundaries, release reports, or Workcell source/docs changes."
---

# Kujo Workcell Workflows

Use Workcell as a Kujo-native, local Docker-backed execution sandbox for AI agents and workflows. It creates disposable Git worktrees, runs declared commands in bounded containers, exports declared artifacts, records receipts, and cleans up. Treat Docker/Podman as the physical boundary and Kujo as the policy/evidence boundary.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
WORKCELL_REPO="${WORKCELL_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/workcell}"
cd "$WORKCELL_REPO"
export KUJO="${KUJO:-/path/to/kujo/target/release/kujo}"
"$KUJO" check main.kujo
docker build --tag kujolang/workcell-base:local docker/
./tests/run.sh
./tests/release_report.sh
./bin/workcell doctor --backend docker
./bin/workcell init
./bin/workcell validate --file workcell.json
./bin/workcell inspect --file workcell.json --json
./bin/workcell run --file workcell.json --repo .
```

## Workflow Notes

- Workcell rejects dirty source repos by default so user changes are not silently omitted from disposable worktrees.
- `workcell validate --schema` emits the definition contract; `workcell help --json` emits the CLI/exit-code contract.
- `workcell run` writes `.workcell/runs/<run-id>/` with `receipt.json`, logs, integrations, patch/change records, integrity manifest, and artifacts.
- `workcell verify --run <run-directory> --json` verifies immutable evidence hashes without exposing secret values.
- The default `contained-standard` profile uses no network, non-root host-mapped UID/GID, read-only root, bounded CPU/memory/PIDs/time/output, no new privileges, dropped capabilities, no devices, no host namespaces, no Docker socket, explicit env, and one disposable workspace mount.
- Workcell is a release-gated local Docker MVP. It is not a hardened microVM, hosted service, or universally isolated enterprise sandbox.

When reporting results, state the command, backend, run directory, exit code, receipt/manifest paths, cleanup outcome, and any host-boundary assumptions.

## Workcell Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `docs/security-model.md`
3. `docs/enterprise-deployment.md`
4. `docs/workcell-definition.md`
5. `docs/runtime-lifecycle.md`
6. `main.kujo`
7. Relevant `src/`
8. `workcell.json`
9. Relevant `tests/`
10. `docs/next-hardening-backlog.md` and `docs/next-review-backlog.md`

Preserve CLI contracts, restrictive defaults, source repo cleanliness checks, output path containment, secret redaction, manifest verification, labeled cleanup, and explicit Docker/Podman boundary language unless the user explicitly changes them.

Run validation after source, docs, definition, runtime, or contract changes:

```bash
./tests/run.sh
./tests/run.sh --check-only
KUJO="$KUJO" ./tests/docker_integration.sh
REQUIRE_BACKEND=true KUJO="$KUJO" ./tests/egress_integration.sh
./tests/release_report.sh
git diff --check
```

Use Docker/Podman integration tests only when the selected engine is available and the task warrants host-runtime checks.

## Search And Safety

- Exclude `.workcell/runs/`, temporary worktrees, built images, and generated reports unless targeted.
- Never print or persist secret values; receipts should contain secret names only.
- Do not delete host resources outside Workcell-owned labels and paths.
- Treat egress profiles as operator-owned infrastructure; Workcell records selected policy but does not replace host firewall/proxy enforcement.

Use `rg` for broad searches and exclude generated, dependency, cache, and run-output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`, `docs/security-model.md`, `docs/enterprise-deployment.md`, `docs/workcell-definition.md`, `docs/runtime-lifecycle.md`.
- Status: repo-backed: `main.kujo`, `src/`, `workcell.json`, `bin/workcell`, `tests/`, `docker/`.
