---
name: kujo-workcell-workflows
description: "Use this skill when initializing, validating, inspecting, running, verifying, cleaning, or maintaining Workcell 1.1 execution harnesses: `workcell.json`, `bin/workcell`, `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `backends`, `recover`, `.workcell/runs/`, summaries, receipts, manifests, artifacts, Docker/Podman boundaries, alpha backend adapters, release reports, or Workcell source/docs changes."
---

# Kujo Workcell Workflows

Use Workcell 1.1 as a stable Kujo-native local and CI OCI execution harness for AI agents and workflows. It creates disposable Git worktrees, runs declared commands in bounded Docker or Podman containers, exports declared artifacts, records receipts, and cleans up. Treat Docker/Podman as the stable physical boundary and Kujo as the policy/evidence boundary. The provider-neutral definition/backend/receipt surface and remote adapters are additive alpha contracts, not part of the stable isolation guarantee.

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
./bin/workcell inspect --file workcell.json --summary
./bin/workcell run --file workcell.json --repo . --no-pull --summary
./bin/workcell verify --run .workcell/runs/<run-id> --json
```

## Workflow Notes

- Workcell rejects dirty source repos by default so user changes are not silently omitted from disposable worktrees.
- `workcell validate --schema` emits `workcell-definition/v1`; `workcell help --json` emits the CLI/exit-code contract.
- Agent-facing `inspect --summary` and `run --summary` emit compact `workcell-inspect-summary/v1` and `workcell-run-summary/v1` pointers. Read `receipt.json` only when detailed evidence is needed, and verify persisted evidence with `verify --json`.
- `workcell run` writes `.workcell/runs/<run-id>/` with `receipt.json`, logs, integrations, patch/change records including untracked files, integrity manifest, and artifacts.
- `workcell verify --run <run-directory> --json` verifies immutable evidence hashes without exposing secret values.
- The default `contained-standard` profile uses no network, non-root host-mapped UID/GID, read-only root, bounded CPU/memory/PIDs/time/output, no new privileges, dropped capabilities, no devices, no host namespaces, no Docker socket, explicit env, and one disposable workspace mount.
- Podman is supported through the same OCI policy boundary. Rootless engine posture, runtime class selection, egress declarations, load evidence, and ecosystem integrations are explicit validation surfaces rather than implicit safety guarantees.
- `backends` lists built-ins and explicitly supplied external adapter manifests; `recover` reconciles owned external-backend journals without deleting resources whose ownership does not match.
- Portable `workcell-definition/v2alpha1`, `workcell-backend/v1alpha1`, and `workcell-receipt/v2alpha1` keep workload definitions provider-neutral. Docker and Podman resolve through the built-in OCI lifecycle; E2B, Vercel Sandbox, Daytona, and Cloudflare Sandbox require exact adapter/profile evidence and credential-gated certification before live claims.
- Artifact policy rejects malformed definitions and unsafe paths before runtime execution; secret redaction and binary-artifact inspection failures must remain fail-closed.
- Declared secret values and common base64 encodings are redacted from stdout/stderr, verification output, receipts, artifacts, and the generated Git patch; `artifacts.secret_action: reject` also rejects a run whose patch contained a declared secret and avoids persisting that patch.
- Workcell 1.x is stable for the documented local and CI Docker/Podman contract. It is not a hardened microVM, hosted service, multi-tenant runner, universal enterprise sandbox, or live-provider certification.

When reporting results, state the command, backend, run directory, exit code, receipt/manifest paths, cleanup outcome, and any host-boundary assumptions.

## Workcell Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `docs/security-model.md`
3. `docs/enterprise-deployment.md`
4. `docs/workcell-definition.md`
5. `docs/runtime-lifecycle.md`
6. `docs/api-compatibility.md`
7. `docs/backend-adapters.md`, `docs/adapter-authoring.md`, `docs/provider-operations.md`, and provider docs when portable backend behavior changes
8. `main.kujo`
9. Relevant `src/`
10. `workcell.json`
11. Relevant `tests/`
12. `docs/known-limitations.md`

Preserve CLI contracts, restrictive defaults, source repo cleanliness checks, output path containment, secret redaction, manifest verification, labeled cleanup, and explicit Docker/Podman boundary language unless the user explicitly changes them.

Run validation after source, docs, definition, runtime, or contract changes:

```bash
./tests/run.sh
./tests/run.sh --check-only
./tests/quality.sh
./tests/release_report.sh
npm ci --ignore-scripts --prefix adapters/official
npm test --prefix adapters/official
npm run integrity:check --prefix adapters/official
KUJO="$KUJO" "$KUJO" run tests/official_adapters_test.kujo
KUJO="$KUJO" ./tests/docker_integration.sh
REQUIRE_BACKEND=true KUJO="$KUJO" ./tests/egress_integration.sh
KUJO="$KUJO" ./tests/load_integration.sh docker
NETWORK_MODE=custom NETWORK_NAME=<deployment-network> \
  ALLOWED_URL=https://allowed.example.test DENIED_URL=https://denied.example.test \
  KUJO="$KUJO" ./tests/egress_deployment_contract.sh docker
git diff --check
```

Use Docker/Podman integration tests only when the selected engine is available and the task warrants host-runtime checks.

## Search And Safety

- Exclude `.workcell/runs/`, temporary worktrees, built images, and generated reports unless targeted.
- Never print or persist secret values; receipts should contain secret names only.
- Do not delete host resources outside Workcell-owned labels and paths.
- Treat egress profiles as operator-owned infrastructure; Workcell records selected policy but does not replace host firewall/proxy enforcement.
- Treat remote provider adapters as trusted host code. Do not put provider credentials or provider options in workload definitions or caller context, and do not upgrade provider-claimed controls to Workcell-enforced evidence.

Use `rg` for broad searches and exclude generated, dependency, cache, and run-output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`, `docs/security-model.md`, `docs/enterprise-deployment.md`, `docs/workcell-definition.md`, `docs/runtime-lifecycle.md`, `docs/api-compatibility.md`, `docs/backend-adapters.md`, `docs/adapter-authoring.md`, `docs/provider-operations.md`, `docs/known-limitations.md`.
- Status: repo-backed: `main.kujo`, `src/`, `workcell.json`, `bin/workcell`, `tests/`, `docker/`.
