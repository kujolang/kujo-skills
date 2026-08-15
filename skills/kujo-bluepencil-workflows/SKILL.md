---
name: kujo-bluepencil-workflows
description: "Use when operating or maintaining BluePencil editorial review and calibration: eight-dimension reviews, blockers, verdicts, reviewer disagreement, style/brand/claims/format/accessibility checks, blind calibration, signed bundles, model-adapter conformance, reports, or BluePencil CLI/source/tests."
---

# Kujo BluePencil Workflows

Use BluePencil for immutable review evidence across consequence, distinctiveness, insight, defensibility, craft, brand integrity, format fidelity, and strategic purpose.

## Workflow

1. Run `bluepencil doctor --json` and initialize explicit state.
2. Freeze the artifact identity and rubric/reviewer identity before `review`.
3. Record focused `style`, `brand`, `claims`, `format`, or `accessibility` findings without presenting deterministic checks as taste.
4. Use `compare` and `disagreements` to preserve independent judgments. Use `calibrate` only with blinded candidates and the canonical rubric/corpus.
5. Run `validate`; inspect `report`, `show`, and `history`; export only reviewed records.

Allowed verdicts are `pass`, `pass_with_queries`, `revise`, `blocked`, `reject`, and `unverified`. Any blocking finding forbids a pass. Do not average away blockers or claim that calibration automates editorial judgment. BluePencil proposes review outcomes; it never approves publication or rewrites the artifact.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `bluepencil.kujo`, `src/`, the calibration corpus, schemas, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
