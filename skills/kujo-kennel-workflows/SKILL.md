---
name: kujo-kennel-workflows
description: "Use this skill when inspecting, using, validating, or maintaining Kennel package/dependency workflows: `kennel.kujo`, package manifests, lockfiles, file dependencies, static indexes and mirrors, trust policy, source policy, semver range resolution, local hosted-registry lifecycle, install/update/validate behavior, release gates, or `kennel` source/test changes."
---

# Kujo Kennel Workflows

Use Kennel for Kujo package/dependency workflows, including local packages, lockfiles, trust policy, static indexes, and deterministic validation gates.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
KENNEL_REPO="${KENNEL_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/kennel}"
cd "${KENNEL_REPO}"
kujo run kennel.kujo --interpreter -- help
kujo run kennel.kujo --interpreter -- init --name kennel-demo
kujo run kennel.kujo --interpreter -- add file:../some-local-package --alias some-local-package
kujo run kennel.kujo --interpreter -- install
kujo run kennel.kujo --interpreter -- validate
```

## Workflow Notes

- Package manifests, lockfiles, static indexes/mirrors, trust policy, source policy, and local hosted-registry artifacts are contract surfaces.
- Local hosted-registry lifecycle, auth, publish/access/visibility/search/metadata APIs, and hosted install against local artifacts are in the launch-safe scope. Operated public registry service, public discovery, hosted moderation, malware scanning, and public trust scoring remain deferred.
- Generated package directories and `.kennel_tmp/` are bulk/runtime surfaces.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo Kennel Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `kennel.kujo`
4. `src/cli.kujo`
5. `src/manifest.kujo`
6. `src/installer.kujo`
7. `src/lockfile.kujo`
8. `src/resolver.kujo`
9. `tests/kennel_contract_tests.kujo`
10. `scripts/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
bash scripts/verify-all.sh
bash scripts/verify-all.sh core
bash scripts/verify-profiles.sh stage3
bash scripts/verify-security-regression-suite.sh
kujo run tests/kennel_contract_tests.kujo
```

`scripts/verify-all.sh` is the broad release gate; pass `core` for a fast
baseline when a full gate is unnecessary. Profile names are `core`, `stage2`,
`stage3`, `security`, and `full`. Use the narrower profile, security, or
contract commands for offline-focused local validation.

## Search And Safety

- Preserve CLI output byte-for-byte unless changing user-facing wording intentionally.
- Do not weaken trust, source, or mutable-ref policies without explicit scope.
- Exclude `.kennel_tmp/**` and `kennel_packages/**` from broad sweeps.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `kennel.kujo`.
- Status: repo-backed: `tests/kennel_contract_tests.kujo`, `scripts/verify-all.sh`, `scripts/verify-profiles.sh`.
