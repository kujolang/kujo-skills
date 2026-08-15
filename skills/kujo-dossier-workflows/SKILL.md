---
name: kujo-dossier-workflows
description: "Use when operating or maintaining Dossier evidence ledgers: claims, sources, captured support, evidence classification, conflicts, quotations, consent, rights, freshness, verification, packets, reports, exports, encryption/signing adapters, or Dossier CLI/source/tests."
---

# Kujo Dossier Workflows

Use Dossier to record what a material claim may honestly rely on. A URL, recorded assertion, consent record, or rights record is evidence—not automatic verification or authority.

## Workflow

1. Run `dossier doctor --json` and initialize explicit state.
2. Create claims with `claim add`, preserving fact, observation, inference, opinion, or hypothesis.
3. Add sources and exact captured support with `source add` and `evidence attach`; include source location, checksum, retrieval time, reviewer, and artifact/claim identity.
4. Use `evidence classify`, `conflict add`, `quote add`, `consent record`, `rights record`, and `freshness check` without erasing disagreement or overstating scope.
5. Run `verify` and `validate`; create bounded `packet`, `report`, or `export` outputs for downstream review.

Verified evidence requires exact support and provenance. Keep `verified`, `observed`, `inferred`, `opinion`, `hypothesis`, `planned`, `conflicted`, `expired`, `unavailable`, and `rejected` distinct. Never turn a citation into approval, rights, consent, or certainty.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `dossier.kujo`, `src/`, schemas, fixtures, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
