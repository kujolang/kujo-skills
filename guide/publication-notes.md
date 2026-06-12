# Publication Notes

## Public Naming Conventions

- Package directory: `kujo-skills/`.
- Skill names and folders are lowercase hyphenated and match exactly.
- Use `Kujo` for the language name and `kujo` for the CLI command.
- Use `.kujo` for source files.

## Command Assumptions

Repo-backed current commands include:

- `kujo run <file>`
- `kujo run --interpreter <file>`
- `kujo check <file>`
- `kujo doctor`
- `kujo docgen <path>`
- `kujo test --runtime vm|dual|interpreter`
- `kujo test-run <file>`
- `kujo init`, `kujo package-add`, `kujo package-install`, `kujo package-install --frozen`
- `kujo serve [dir]`
- `kujo lsp`

## Release Readiness Assumptions

The repo has conflicting wording:

- `README.md`, `docs/LANGUAGE_SPEC.md`, `docs/V1_SCOPE.md`, and `docs/PRE_V1_MASTER_UNFINISHED_CHECKLIST.md` state Kujo remains pre-1.0 until roadmap/checklist gates are closed.
- `docs/RELEASE_PROCESS.md` says "Kujo is now at `1.0.0`."
- `docs/ARCHITECTURE.md` says current crate version is `0.14.0`, while the repo reports current crate version elsewhere as `1.0.0`.

Publication recommendation: before public release of these skills, maintainers should reconcile release-status wording and decide whether skills should say "pre-1.0" or "1.0 released but still with post-release caveats." This extraction follows the conservative pre-1.0 boundary.

## Missing Requested Source Material

The requested root files `DOGFOOD_NOTES.md` and `BUG_HUNT_REPORT.md` were not present in this checkout.

## Editor/LSP Notes

The skills mention LSP JSON helper surfaces and `kujo lsp`, but do not attempt to document every editor integration. Consult `docs/INSTALLATION_LSP_EDITORS.md`, `docs/EDITOR_ADAPTER_BASELINES.md`, and `docs/PROTOCOL_CONTRACTS.md` before publishing editor-specific skills.

## Skills To Revisit Before Public Release

- `kujo-testing-release-gates`: update once release state is reconciled.
- `kujo-runtime-parity`: update if `kujo test` default changes from `dual`.
- `kujo-standard-library`: refresh after builtin tier/capability promotions.
- `kujo-security-hardening`: refresh after any native capability or outbound policy change.

