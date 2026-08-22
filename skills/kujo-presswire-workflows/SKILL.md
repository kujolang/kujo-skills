---
name: kujo-presswire-workflows
description: "Use when operating or maintaining PressWire approval-gated publication: adapter/capability inspection, preflight, schedule/publish ACT effects, status, corrections, unpublish/compensation, idempotency, reconciliation, receipts, CMS/Git-static/newsletter adapters, exports, or PressWire CLI/source/tests."
---

# Kujo PressWire Workflows

Use PressWire only for a bounded effect authorized by a valid VersionSeal decision for the exact GalleyPack checksum and destination.

## Workflow

1. Run `presswire doctor --json`, then inspect `adapters` and `capabilities` without credentials where possible.
2. Run `preflight --input <request> --actor <actor> --json`; verify approval identity, checksum, destination, action, adapter, target, cost/rollback posture, and idempotency key.
3. Use `schedule` or `publish` only with explicit `--act --yes` and a matching authorization. Do not infer ACT from credentials or a ready status.
4. Inspect `status`, `receipt`, and `history`. Reconcile uncertain provider outcomes before retrying.
5. Use `correct` or `unpublish` only when separately authorized and supported; preserve the original receipt and compensation state.

PressWire `0.2.0` is local-first and has no required hosted service, database server, model key, or sibling-tool dependency. It provides immutable records, append-only audit events, atomic writes, per-record locks, CMS/Git-static/newsletter conformance fixtures, resumable effect reconciliation, explicit compensation rules, optional signed VersionSeal verification, and deterministic partial-provider fault injection. JSON output uses the stable `ok/data/error/error_code/tool_version/contract_version` envelope; exit codes are `0` success, `1` operational failure, and `2` usage error.

Fixture adapters cannot target live destinations. A received provider response is not proof of indexing, delivery, or audience outcome. Never expose credentials, bypass checksum/approval drift, ignore duplicate-id/idempotency failures, or silently repeat an uncertain effect.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `presswire.kujo`, `src/`, adapter fixtures, schemas, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
