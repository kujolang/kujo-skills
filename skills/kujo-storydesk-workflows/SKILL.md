---
name: kujo-storydesk-workflows
description: "Use when operating or maintaining StoryDesk editorial control: ideas, campaigns, commissions, assignments, claims, dependencies, status/block events, daily/range/resumable packets, handoffs, review queues, JSON or SQLite state, policy transitions, signed exports, adapter conformance, or StoryDesk CLI/source/tests."
---

# Kujo StoryDesk Workflows

Use StoryDesk as the source of truth for editorial queue and ownership state, not as approval or publication authority.

## Workflow

1. Run `storydesk doctor --json`, then `storydesk init --state <state> --json` for new state.
2. Capture work with `idea add`, `campaign create`, `commission create`, `assign`, and `claim`; require `--actor` for mutations and use `--timestamp` or `--id` when reproducibility matters.
3. Record transitions through `status`, `block`, and `handoff`; use an organization-owned `--transition-policy` when configured.
4. Build bounded operator views with `packet daily`, `packet range`, `packet generate`, and `review-queue`. Use `--checkpoint` plus `--resume` for large packet generation.
5. Inspect with `show` and `history`; run `validate` before handoff. Use `export` and `export verify` for portable or signed bundles.

Default to immutable JSON. Use `--storage-adapter sqlite` only after the target environment passes the documented benchmark/admission gate. Keep state paths explicit; reject traversal, symlinks, secrets, duplicate IDs, schema-major drift, and unsafe overwrites. `--dry-run` validates without writing; `--force` applies only to an explicitly named safe export.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `storydesk.kujo`, `src/`, fixtures, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
