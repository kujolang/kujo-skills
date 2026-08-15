---
name: kujo-readersignal-workflows
description: "Use when operating or maintaining ReaderSignal privacy-bounded audience learning: measurement snapshots, feedback, comparisons, uncertainty/sample-size handling, learning records, follow-up recommendations, deletion/retention receipts, signed publication verification, adapter fixtures, reports, or ReaderSignal CLI/source/tests."
---

# Kujo ReaderSignal Workflows

Use ReaderSignal to preserve measured response and bounded learning without claiming causation or manufacturing unavailable analytics.

## Workflow

1. Run `readersignal doctor --json` and initialize explicit state.
2. Create a privacy-reviewed `snapshot` tied to a verified PressWire publication receipt, provider/window identity, metric definitions, sample size, and collection limitations.
3. Record qualitative `feedback` with consent and privacy scope.
4. Use `compare` only across compatible definitions and windows; preserve uncertainty and small-sample limitations.
5. Create `learn` and `followup` records as recommendations, not automatic commissions. Validate and inspect with `report`, `history`, and `show` before export.

ReaderSignal does not prove causality, commission work, alter editorial history, or authorize publication. Record unavailable measurement as unavailable, never zero. Preserve policy-versioned retention/deletion receipts and reject secrets or unnecessary personal data.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `readersignal.kujo`, `src/`, schemas, fixtures, benchmarks, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
