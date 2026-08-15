---
name: kujo-galleypack-workflows
description: "Use when operating or maintaining GalleyPack production packages: artifact checksums, lineage, evidence/review attachments, package build/freeze, claim comparison, exact-version diff and drift validation, signed trees, archive/object-store adapters, exports, or GalleyPack CLI/source/tests."
---

# Kujo GalleyPack Workflows

Use GalleyPack to bind editorial artifacts and review dependencies to exact immutable package versions.

## Workflow

1. Run `galleypack doctor --json` and initialize explicit state.
2. Register exact files with `add`; use `relate` for source, derivative, adaptation, variant, or replacement lineage.
3. Attach Dossier and BluePencil references with `evidence attach` and `review attach`.
4. Use `claims compare` before accepting claim-boundary changes. Create a package with `build`; use `freeze` only when required artifacts and reviews are complete.
5. Run `validate` to re-hash bound files and `diff` to compare versions. Inspect with `show`, `report`, and `history`; export only reviewed bundles.

GalleyPack does not edit source files, average missing reviews, approve, or publish. Any byte drift invalidates the exact package identity and downstream approval. Reject traversal, symlinks, secret-shaped fields, duplicate IDs, incompatible schemas, oversized input, or unsafe overwrite.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `galleypack.kujo`, `src/`, schemas, fixtures, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
