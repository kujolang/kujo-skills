---
name: kujo-publishing-house-workflows
description: "Use when installing, running, inspecting, recovering, integrating, or maintaining the Kujo Publishing House workflow suite: daily desk, governance, commissioning, evidence dossiers, primary pieces, asset production, editorial review, adaptation, format production, approval/publication, post-publication learning, fixture/live modes, capability preflight, exact compatibility locks, agent-step receipts, Dispatch state, or Publishing House workflow source/tests."
---

# Kujo Publishing House Workflows

Use the Publishing House as a receipt-driven editorial lifecycle. Keep strategy, creation, independent review, exact-version human approval, publication effects, and measurement as separate authorities.

## Start And Route

1. Read `../kujo-workflows/docs/publishing-house/README.md`, the selected kit's `README.md` and `HOWTO.md`, and its `workflow.json`.
2. For an isolated installation, run `bash scripts/install-publishing-house.sh --prefix <absolute-prefix> --source-repos <repos-root> --kujo-bin <kujo> --demo`, then run `<prefix>/bin/publishing-house-doctor`.
3. For a source checkout, set `KUJO_REPOS` and `KUJO_BIN`; use `bash scripts/run-publishing-house-fixture.sh --out <new-output>` for the complete offline proof.
4. Route to the narrowest kit: governance, daily desk, commissioning, evidence dossier, primary piece, asset production, editorial review, adaptation, format production, approval/publication, or post-publication learning.
5. Inspect `state.json`, `report.json`, capability receipts, agent-step receipts, tool record references, Dispatch trace/report, and the blocker or completion receipt.

## Permission And Recovery

- Treat `OBSERVE`, `PROPOSE`, and `ACT` as upper bounds. Only Publishing Operations may perform the exact publication action authorized by a valid VersionSeal decision.
- Treat credentials as capability, never authority. Never infer approval from a status, prompt, conversation, or available adapter.
- Bind approval to the exact GalleyPack checksum, destination, action, conditions, and expiry. Any reviewed-byte change requires a new package and approval.
- Resume only the same paused run with its exact VersionSeal result. Repeating a completed run must be an idempotent read.
- Preserve `unsupported`, `unavailable`, `blocked`, `rejected`, `skipped`, `failed`, `paused`, and `completed` as distinct outcomes.

## Fixture And Live Boundaries

- Fixture mode is offline, deterministic, credential-free, and external-effect-free except for the explicitly labeled local publication fixture.
- Live mode must be explicit and must validate compatible model, retrieval, identity, measurement, and destination adapters before any mutation. Never fall back from live to fixture data.
- Resolve and read every canonical role and skill contract before executing an agent step; path strings in receipts are not proof that a contract was applied.
- Fail closed on incompatible tool commits/contracts, secret-shaped persisted input, missing required capabilities, or a broader requested effect than the approval allows.

## Repository Work

Read `AGENTS.md`, root `README.md`, `contracts/README.md`, `docs/audit/README.md`, `docs/launch-checklist.md`, `docs/publishing-house/`, `lib/publishing_house/`, the affected kits, and their tests. Preserve record ownership: StoryDesk, Dossier, GalleyPack, BluePencil, AssetWorks, VersionSeal, PressWire, ReaderSignal, Dispatch, and Agents SDK remain authoritative for their own artifacts.

Validate with:

```bash
python3 scripts/validate_catalog.py --json
python3 scripts/validate_contracts.py
python3 -m unittest discover -s tests -p 'test_publishing_house*.py'
bash scripts/run-publishing-house-fixture.sh --out "$(mktemp -d)/publishing-house-proof"
git diff --check
```

Use the locked installer or clean detached worktrees when sibling checkout commits differ from `docs/publishing-house/compatibility-matrix.json`; do not misreport compatibility drift as a product failure.
