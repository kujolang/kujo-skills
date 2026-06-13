---
name: kujo-shipcheck-workflows
description: "Use this skill when running, reviewing, integrating, or maintaining ShipCheck release-readiness workflows for Kujo ecosystem repositories: `shipcheck.kujo`, `scan`, `checklist`, `gate`, `release-note`, `--format json`, CI release gates, markdown/json reports, release check catalogs, gate exit semantics, or ShipCheck CLI/source/test changes."
---

# Kujo ShipCheck Workflows

Use ShipCheck to inspect whether a local repository has enough release-readiness signals to ship. Treat findings as release blockers and review items, not as a release certification.

## Quick Start

Default to the local ShipCheck repo unless the user points to another checkout:

```bash
SHIPCHECK_REPO="${SHIPCHECK_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/shipcheck}"
cd "$SHIPCHECK_REPO"
kujo run shipcheck.kujo scan --dir /path/to/project
```

Use these common forms:

```bash
kujo run shipcheck.kujo scan --dir /path/to/project
kujo run shipcheck.kujo scan --dir /path/to/project --format json
kujo run shipcheck.kujo checklist --dir /path/to/project
kujo run shipcheck.kujo gate --dir /path/to/project
kujo run shipcheck.kujo gate --dir /path/to/project --format json
kujo run shipcheck.kujo release-note --dir /path/to/project
```

If scanning ShipCheck itself from inside the ShipCheck repo, omit `--dir`.

## Scan Workflow

- Run `scan` first to surface repository health, code quality, documentation, and release metadata findings.
- Use `--format json` when a CI step, policy script, or follow-up analysis needs stable fields.
- Run `checklist` when the user wants actionable release tasks in human-readable form.
- Run `gate` as the enforcement step after fixes. Do not use `scan` as a blocking gate.
- Run `release-note` only as a draft generator from recent git commits; final release notes still need human editing.
- Summarize results by failed error checks, warning checks, release impact, and recommended next action.
- Do not commit generated artifacts such as `shipcheck-report.json` unless the user explicitly asks.

## Gate Semantics

- `scan` is informational and can print findings without failing the command.
- `gate` exits `1` when any error-level check fails.
- `gate` exits `0` when no error-level checks fail, even if warnings remain.
- Warnings do not block by themselves, but call them out as release review items.
- ShipCheck does not run tests, linters, release artifact validation, publishing, or network checks.

In final responses after running ShipCheck, state the command, target directory, exit code, highest severity, and whether the release gate passed.

## Check Coverage

ShipCheck currently runs 16 checks across 4 categories:

- Repository health: `git-repo`, `readme`, `license`, `ignore-files`.
- Code quality: `tests-exist`, `lint-command`, `format-command`, `ci-config`.
- Documentation: `readme-install`, `readme-usage`, `examples`, `docs`.
- Release metadata: `version-metadata`, `changelog`, `kennel-manifest`, `entry-point`.

Error-level failures block `gate`: `git-repo`, `readme`, `tests-exist`, `version-metadata`, and `changelog`. Other failing checks are warnings unless ShipCheck source changes update the catalog.

## ShipCheck Repo Work

When modifying ShipCheck itself, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `docs/operations.md`
4. `docs/check-catalog.md`
5. `shipcheck.spec.yml`
6. `shipcheck.kujo`
7. `src/checks.kujo`, `src/scan.kujo`, `src/report.kujo`
8. `tests/cli-output-contract.sh`

Preserve these contracts unless the user explicitly asks to change them:

- Commands: `scan`, `checklist`, `gate`, `release-note`, `version`, `help`.
- Options: `--dir <path>`, `--format markdown|json` for `scan` and `gate`.
- Help/version usage: standalone `--help` and `--version` aliases are not implemented in this wrapper.
- Gate behavior: error-level failures return `1`; warning-only results return `0`.
- JSON report identity: `tool` is `shipcheck`, `version` is current release, and `summary.total_checks` matches the check catalog.
- Public docs: keep `README.md`, `docs/operations.md`, and `docs/check-catalog.md` aligned with source behavior.

Use `rg` for broad searches and exclude generated or historical bulk paths unless the task targets them:

```bash
rg "pattern" -g '!eval_results/**' -g '!.dogfood/**'
```

When sweeping examples, start with:

```bash
rg -n "print\\(|format json|checklist|gate|release-note" README.md docs examples src shipcheck.kujo
```

## Validation

Run focused checks for touched Kujo files, then run the CLI contract test:

```bash
cd /Users/robertdevore/2026/Kujolang/kujo-repos/shipcheck
tests/cli-output-contract.sh
kujo run shipcheck.kujo scan --dir .
kujo run shipcheck.kujo scan --dir . --format json
kujo run shipcheck.kujo gate --dir .
```

If `kujo` is not on `PATH`, set `KUJO_BIN` for the contract test:

```bash
KUJO_BIN=/path/to/kujo tests/cli-output-contract.sh
```

For source changes that add, remove, rename, or re-severity checks, update `src/checks.kujo`, `docs/check-catalog.md`, `README.md`, and the contract tests together.

## Sources Consulted

- Status: repo-backed: `README.md`, `AGENTS.md`, `shipcheck.spec.yml`, `tests/cli-output-contract.sh`.
- Status: repo-backed: `docs/operations.md`, `docs/check-catalog.md`, `shipcheck.kujo`, `src/checks.kujo`, `src/scan.kujo`, `src/report.kujo`.
