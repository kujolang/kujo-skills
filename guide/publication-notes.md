# Publication Notes

## Public Naming Conventions

- Package directory: `kujo-skills/`.
- Skill names and folders are lowercase hyphenated and match exactly.
- Use `Kujo` for the language name and `kujo` for the CLI command.
- Use `.kujo` for source files.

## Version Baselines

- Kujo `v1.0.0` is the stable language/runtime source baseline.
- The skills distribution is versioned independently; its current technical-preview version is `0.1.0`.
- `VERSION` and `package.json` are the machine-readable skills-pack version sources.
- `CHANGELOG.md` records public skills-pack changes.

Current Kujo commands referenced by the pack include:

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

Release and compatibility claims should follow `docs/V1_SCOPE.md`, `docs/V1_0_OFFICIAL_RELEASE_CHECKLIST.md`, `docs/RELEASE_PROCESS.md`, and current release evidence in the Kujo repository. Historical pre-1.0 checklists are evidence records, not current release authority.

## Distribution Boundary

The repository may be cloned or copied under the MIT License. Marketplace publication, automatic installation into live profiles, and claims of third-party runtime enforcement require separate evidence and authorization.

## Editor and LSP Notes

The skills mention LSP JSON helper surfaces and `kujo lsp`, but do not attempt to document every editor integration. Consult `docs/INSTALLATION_LSP_EDITORS.md`, `docs/EDITOR_ADAPTER_BASELINES.md`, and `docs/PROTOCOL_CONTRACTS.md` in the Kujo repository before publishing editor-specific guidance.

## Maintenance Watchlist

- `kujo-runtime-parity`: revisit if the default `kujo test` runtime changes.
- `kujo-standard-library`: refresh after builtin tier or capability promotions.
- `kujo-security-hardening`: refresh after native capability or outbound-policy changes.
- Workflow skills: refresh command, schema, exit-code, and artifact claims when their source repositories release changes.
