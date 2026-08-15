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

AssetWorks never grants rights, consent, or publication authority. Carry Dossier rights references, disclose synthetic media, preserve source lineage and adapter/version identity, and reject traversal, symlinks, secrets, unsafe overwrite, or unbounded media operations.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `assetworks.kujo`, `src/`, adapter fixtures, schemas, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
