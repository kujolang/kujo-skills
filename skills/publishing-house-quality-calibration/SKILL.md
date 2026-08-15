---
name: publishing-house-quality-calibration
description: "Use when running, reviewing, extending, or maintaining Publishing House premium-quality calibration: the eight-dimension rubric, blinded A/B fixtures, judge protocol/schema, expected judgments, generic-work signals, blocking failures, role coverage, BluePencil calibration records, or calibration corpus validation."
---

# Publishing House Quality Calibration

Use the reviewed blind corpus to calibrate editorial judgment, not to replace it with a score.

## Workflow

1. Read `../kujo-agents/publishing-house/00-quality-standard.md` and every file directly required by `publishing-house/evals/README.md`.
2. Preserve blinded labels `A` and `B`; do not reveal expected judgments before the reviewer commits a result.
3. Rate consequence, distinctiveness, insight, defensibility, craft, brand integrity, format fidelity, and strategic purpose with `EXCEPTIONAL`, `STRONG`, `ADEQUATE`, `WEAK`, `FAILED`, or `UNVERIFIED`.
4. Record passage/asset evidence, generic-work signals, uncertainty, blocking failures, and rationale. Never average away a failed defensibility, rights, privacy, approval, or artifact-integrity gate.
5. Compare the completed judgment with the checksum-bound expected record. Use BluePencil `calibrate` for immutable reviewer/rubric identity when available.
6. When adding a case, preserve blind-pair schema, checksum, role coverage, both expected classifications, all eight ratings, decisive dimensions, and corpus manifest integrity.

Run `python3 scripts/validate_publishing_house.py` in `kujo-agents` and `bash scripts/validate.sh` in `bluepencil` after relevant changes. Report calibration drift as evidence for review, not proof that editorial taste is automated.
