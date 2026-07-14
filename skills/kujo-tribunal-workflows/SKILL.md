---
name: kujo-tribunal-workflows
description: "Use this skill when running, reviewing, integrating, or maintaining Tribunal local decision-evidence workflows: `tribunal review`, `resume`, `compare`, `re-review`, `kill`, `validate`, `audit`, `verify`, bundle/store/provenance commands, signed evidence, trust policies, run artifacts, schemas, release gates, or Tribunal source/docs changes."
---

# Kujo Tribunal Workflows

Use Tribunal for local-first adversarial decision review with durable evidence, specialist testimony, cross-examination, a fatal-flaw pass, a ruling, and an execution-ready decision packet. Treat it as inspectable decision evidence, not a public hosted service or universal enterprise certification.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
TRIBUNAL_REPO="${TRIBUNAL_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/tribunal}"
cd "$TRIBUNAL_REPO"
export KUJO_BIN="${KUJO_BIN:-../kujo/target/release/kujo}"
./bin/tribunal version
./bin/tribunal doctor
./bin/tribunal validate examples/product-decision.md
./bin/tribunal review examples/product-decision.md --panel fast-two-model
./bin/tribunal list --status completed --limit 5
```

## Workflow Notes

- Mock mode is deterministic, offline, credential-free, and the default.
- Live provider calls go through the adjacent Kujo AI SDK; Tribunal owns hearing orchestration and evidence, not provider transport.
- Completed hearings write run artifacts under `tribunal-runs/<run-id>/` by default, including record, receipt, manifest, event log, prompts, testimony, ruling, decision packet, and optional signature.
- Exit codes are stable: `0` success, `1` runtime failure, `2` usage/configuration error, and `3` integrity failure.
- Normal production verification uses `tribunal audit <run-id> --trust-policy <path> --target audit --require-signature --json`.
- Never commit private keys. Prefer `seal-provider` for HSM/KMS custody when managed signing is required.
- Current production posture is local/operator-controlled; shared service, regulated deployment, and public hosted service claims require deployment-specific certification and independent review evidence.

When reporting results, state the command, run ID, run directory, exit code, integrity/signature status, trust-policy target, and any unsupported production claims avoided.

## Tribunal Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `docs/OPERATIONS.md`
3. `docs/ENTERPRISE_READINESS.md`
4. `docs/THREAT_MODEL.md`
5. `docs/NEXT_SESSION_REVIEW.md` and the latest `docs/NEXT_SESSION_REVIEW_V*.md`
6. `tribunal.kujo`
7. Relevant `src/*.kujo`
8. Relevant `schemas/*.json`
9. `tests/tribunal_tests.kujo`, `tests/cli_integration.kujo`, `tests/enterprise_tests.kujo`, `tests/property_tests.kujo`
10. Relevant `scripts/*_gate.kujo`

Preserve command syntax, schema versions, evidence immutability, signature/trust-policy semantics, lock/recovery behavior, and explicit production-readiness limits unless the user explicitly changes them.

Run validation after source, docs, schema, command, or release-contract changes:

```bash
for file in $(find . -name '*.kujo' -not -path './.git/*'); do
  "$KUJO_BIN" check "$file"
done
"$KUJO_BIN" run tests/tribunal_tests.kujo
"$KUJO_BIN" run tests/cli_integration.kujo
"$KUJO_BIN" run tests/enterprise_tests.kujo
"$KUJO_BIN" run tests/property_tests.kujo
"$KUJO_BIN" run scripts/schema_gate.kujo
"$KUJO_BIN" run scripts/security_review_gate.kujo
```

## Search And Safety

- Exclude `tribunal-runs/`, generated bundles, private keys, and bulk evidence unless targeted.
- Treat `docs/security/INDEPENDENT_REVIEW_COMMISSION.md` as commissioned-review evidence, not proof of completion.
- Do not claim hosted-service readiness, multi-tenant auth, or regulated deployment certification without explicit deployment evidence.
- Preserve sealed evidence; create new artifacts rather than editing run contents.

Use `rg` for broad searches and exclude generated, dependency, cache, and run-output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`, `docs/OPERATIONS.md`, `docs/ENTERPRISE_READINESS.md`, `docs/THREAT_MODEL.md`, `docs/NEXT_SESSION_REVIEW_V0.8.md`.
- Status: repo-backed: `tribunal.kujo`, `src/*.kujo`, `schemas/*.json`, `tests/*.kujo`, `scripts/*_gate.kujo`.
