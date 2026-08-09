---
name: kujo-redact-workflows
description: "Use this skill when scanning, sanitizing, verifying, packing, or maintaining Redact local deterministic anonymization workflows: `redact.kujo`, `scan`, `sanitize`, `verify`, `pack`, policy YAML files, `.redact/runs/` audit artifacts, leakage checks, unsafe originals, AI-stub boundaries, or Redact CLI/source/test changes."
---

# Kujo Redact Workflows

Use Redact for local-first deterministic anonymization of text and Markdown into model-ready context with a local audit trail. Treat it as a review aid, not a guarantee that no sensitive data remains.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
REDACT_REPO="${REDACT_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/redact}"
cd "$REDACT_REPO"
kujo run redact.kujo scan fixtures/sample.md --policy fixtures/sample.policy.yaml
kujo run redact.kujo sanitize fixtures/sample.md --policy fixtures/sample.policy.yaml --out sample.redacted.md
kujo run redact.kujo verify sample.redacted.md --policy fixtures/sample.policy.yaml
kujo run redact.kujo pack ./notes --policy external-safe --out redacted-pack
```

## Workflow Notes

- Supported inputs are `.txt`, `.md`, and the `-` stdin contract; current Kujo VM builds return an unsupported-runtime error for stdin rather than reading it silently.
- Supported policies are the documented flat-YAML subset with category actions, term dictionaries, and optional role mappings.
- Detection is deterministic: email, phone, URL/domain, credit card with Luhn, API key/token, money, date, configured names, and strategy phrases.
- Transformations include `remove`, `placeholder`, `role-preserve`, `generalize`, `range`, and `date-generalize`.
- Audit output lives under `.redact/runs/<timestamp>/` with manifests, detections, decisions, transformations, verifier report, policy snapshot, hashes, and warnings.
- Raw sensitive values are not written by default. Avoid `--unsafe-store-originals` except in trusted local debugging, and never share or commit those artifacts.
- AI is a stubbed provider contract only in the MVP; Redact must not make provider calls unless repo behavior explicitly changes.

When reporting results, state the command, input/output paths, exit code, verifier risk, audit directory, and whether human review is still required.

## Redact Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `docs/security.md`
3. `docs/architecture.md`
4. `redact.kujo`
5. `src/cli.kujo`
6. `src/policy.kujo`, `src/detect.kujo`, `src/transform.kujo`, `src/verify.kujo`, `src/audit.kujo`
7. `tests/redact_tests.kujo`
8. `tests/run.sh`

Preserve documented command names, policy behavior, audit schema intent, leakage checks, and safe-write behavior unless the user explicitly asks to change them.

Run validation after source, docs, policy, or contract changes:

```bash
bash tests/run.sh
```

## Search And Safety

- Exclude `.redact/runs/` and generated packs from broad readability sweeps unless targeted.
- Do not print raw sensitive samples from user data, audit logs, or `--unsafe-store-originals`.
- Use a new output path for sanitized files so source files are not silently overwritten.
- Treat unsupported YAML structures as policy errors rather than assuming they work.

Use `rg` for broad searches and exclude generated, dependency, cache, and audit directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`, `docs/security.md`, `docs/architecture.md`.
- Status: repo-backed: `redact.kujo`, `src/*.kujo`, `tests/redact_tests.kujo`, `tests/run.sh`.
