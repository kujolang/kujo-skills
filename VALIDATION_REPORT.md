# Kujo Skills Validation Report

## Skill format validation

All 11 required skill folders exist under `skills/`, and each folder name matches the `name` field in its `SKILL.md` frontmatter:

- `kujo-core-language`
- `kujo-tool-building`
- `kujo-security-hardening`
- `kujo-enterprise-automation`
- `kujo-cli-contracts`
- `kujo-standard-library`
- `kujo-testing-release-gates`
- `kujo-runtime-parity`
- `kujo-language-implementation`
- `kujo-docgen-agent-readable`
- `kujo-maintainer-review`

Each `SKILL.md` includes valid Agent Skills-style frontmatter with `name` and `description`.

## Trigger description review

Descriptions are specific and include both domain and activation cues. They avoid generic "best practices" phrasing and mention Kujo-specific surfaces such as `.kujo`, VM/interpreter, native capability flags, CLI JSON contracts, DocGen, LSP helper JSON, and release gates.

## Skill overlap review

Expected overlap exists by design:

- `kujo-security-hardening` and `kujo-enterprise-automation` both cover capability-minimal execution. The security skill is for code/security review; the enterprise skill is for CI/operator workflow design.
- `kujo-cli-contracts` and `kujo-docgen-agent-readable` both mention DocGen JSON. The CLI skill owns payload/exit compatibility; the DocGen skill owns documentation pipeline and agent-readable artifacts.
- `kujo-runtime-parity` and `kujo-language-implementation` both mention parity tests. The parity skill is for runtime behavior diagnosis; the implementation skill is for Rust subsystem changes.

No skill is redundant enough to merge without losing trigger precision.

## Missing coverage

Intentional omissions from the required catalog:

- Detailed LSP/editor setup.
- Package workflow authoring beyond package-install/package-lock verification.
- Tree-sitter maintenance.
- Performance benchmarking and criterion workflows.
- Static server implementation details.

These are suggested as future skills in `EXTRACTION_REPORT.md`.

## Over-broad skills

- `kujo-language-implementation` is necessarily broad because it covers Rust contribution boundaries. It stays usable by providing a subsystem map and validation by change type.
- `kujo-enterprise-automation` could become broad if expanded; current content is limited to deterministic CLI behavior, JSON, capability-minimal execution, CI, and external isolation.

## Over-specific skills

- None of the skills encode one-off roadmap items as primary workflow steps. Specific commands are validation gates rather than narrow task assumptions.

## Hallucination risk review

Risk controls applied:

- Every skill includes a "Sources consulted" section.
- Claims about sandboxing, release readiness, VM defaults, CLI contracts, and capabilities were taken from repo docs/tests/implementation.
- Inferred conventions are explicitly marked in the extraction report or skill source notes.
- The package avoids claiming missing source files were reviewed.

Known risk areas:

- Release status is contradictory across docs.
- Some examples use older style forms; idiomatic style guidance should be maintainer-reviewed.
- Custom enterprise JSON report field names are inferred conventions, not formal language contracts.

## Recommended maintainer review checklist

1. Reconcile release readiness wording across `README.md`, `docs/RELEASE_PROCESS.md`, `docs/ARCHITECTURE.md`, `docs/V1_SCOPE.md`, and `docs/PRE_V1_MASTER_UNFINISHED_CHECKLIST.md`.
2. Confirm whether new idiomatic Kujo examples should prefer `let`/`mut`/`const` with `:=` exclusively.
3. Confirm whether custom enterprise tool JSON field naming should be documented as a formal convention.
4. Refresh standard-library skill after any builtin/capability/tier changes.
5. Refresh runtime-parity skill after any `kujo test` default or VM/interpreter parity matrix change.
6. Decide whether to add future LSP/editor, package workflow, and performance skills.

