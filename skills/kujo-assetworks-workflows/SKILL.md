---
name: kujo-assetworks-workflows
description: "Use when operating or maintaining AssetWorks media production: asset plans, deterministic probes, render/convert/resize adapters, captions, transcripts, thumbnails, accessibility records, provenance, rights references, checksums, manifests, signed exports, FFmpeg/image adapter conformance, or AssetWorks CLI/source/tests."
---

# Kujo AssetWorks Workflows

Use AssetWorks to plan and validate reviewable media assets with exact provenance, rights references, accessibility artifacts, and checksums.

## Workflow

1. Run `assetworks doctor --json` and initialize explicit state.
2. Record the requested operation and source identity with `plan`; inspect inputs before any transform.
3. Use `render`, `convert`, or `resize` only through a declared supported adapter and bounded output path. Unsupported transforms become blockers.
4. Create `captions`, `transcript`, and `thumbnail` records where the format requires them.
5. Produce a checksum-backed `manifest`, then run `validate`; inspect with `report`, `history`, and `show` before export.

AssetWorks `0.3.0` requires Kujo `1.5.0` and is local-first with no required hosted service, database server, model key, or sibling-tool dependency. It provides immutable records, append-only creation events, atomic no-replace writes, transaction-journal recovery, bounded pages, deterministic media probes, offline FFmpeg/image adapter conformance, optional container-confined codecs, 64 MiB..4 GiB streaming checksums, RSA/HMAC signed manifests, larger-state sharded collections, and backup/restore preserving immutable signatures and media references. Development `main` additionally has resumable backup/migration and recovery drills plus offline SRT/WebVTT conversion and transcript extraction that are not in the v0.3.0 archive. JSON output uses the stable `ok/data/error/error_code/tool_version/contract_version` envelope; exit codes are `0` success, `1` operational failure, and `2` usage error.

AssetWorks never grants rights, consent, or publication authority. Carry Dossier rights references, disclose synthetic media, preserve source lineage and adapter/version identity, and reject traversal, symlinks, secret-shaped fields, malformed JSON, incompatible schemas, duplicate IDs, checksum drift, unsafe overwrite, or unbounded media operations.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `docs/ADAPTERS.md`, `docs/RECOVERY.md`, `docs/BACKUP_RESTORE.md`, `assetworks.kujo`, `src/`, adapter fixtures, schemas, and tests. Use the Kujo 1.5.0 runtime or exact README source pin. Run `"$KUJO_BIN" run tests/test.kujo`, `KUJO_BIN="$KUJO_BIN" bash scripts/validate.sh` with explicit FFmpeg binaries for the full gate, and `git diff --check`.
