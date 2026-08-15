# Release Gates

## Evidence Order

1. Resolve the actual released baseline from GitHub releases and tags.
2. Compare it with repository version files, manifests, badges, changelog entries, specifications, eval fixtures, and install examples.
3. Establish the intended semantic version from the size and compatibility of the change.
4. Run repository-focused tests and clean-install proof.
5. Run release-readiness, ShipCheck, and any repository-required security, architecture, contract, or cross-platform gates.
6. Commit the release-bound source.
7. Re-run release gates on the exact commit.
8. Create and verify the tag, push, release, assets, CI, and published checksums.

## Invariants

- Treat a development version as unpublished until a matching verified release exists.
- Keep tags immutable after publication. Use a patch release for corrections.
- Prefer annotated tags; sign tags when repository policy or prior releases require signing.
- Verify binaries, archives, checksums, manifests, schemas, and installation examples according to repository scope.
- Record warnings separately from blockers. ShipCheck warnings may permit a gate exit of zero but still require review.
- Require a clean, synchronized working tree after push.
- Never describe ShipCheck alone as proof that tests, artifacts, network checks, or deployment passed.

## Authorization Boundary

Treat commit, push, tag, GitHub release, marketplace publication, and deployment as separate effects. Perform only effects explicitly authorized by the request or governing repository instructions.
