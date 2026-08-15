---
name: kujo-versionseal-workflows
description: "Use when operating or maintaining VersionSeal exact-version human approval: approval requests, approve/reject/request-changes decisions, revocation, expiry, checksum verification, quorum and separation-of-duties policies, signatures, replication conflicts, exports, or VersionSeal CLI/source/tests."
---

# Kujo VersionSeal Workflows

Use VersionSeal to bind an explicit human decision to an exact artifact checksum, scope, destination, action, conditions, and expiry.

## Workflow

1. Run `versionseal doctor --json` and initialize explicit state.
2. Create an approval `request` from a validated frozen package; preserve requester, checksum, destination, allowed action, unresolved queries, and expiry.
3. A verified human actor records exactly one `approve`, `reject`, or `request-changes` decision. Apply quorum and separation-of-duties policy when configured.
4. Use `revoke` or `expire` without rewriting earlier events.
5. Run `verify` and `validate`; inspect with `inspect`, `show`, `list`, and `history`; export only bounded reviewed records.

Credentials and signatures authenticate configured identities; they do not invent human authority. Any checksum, destination, action, condition, or validity mismatch fails closed. VersionSeal does not publish.

For repository changes, read `README.md`, `AGENTS.md`, `docs/contracts.md`, `docs/security.md`, `versionseal.kujo`, `src/`, schemas, fixtures, and tests. Run `bash scripts/validate.sh` and `git diff --check`.
