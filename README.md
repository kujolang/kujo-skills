# Kujo Agent Skills

This package contains Agent Skills for working on and with the Kujo programming language and adjacent Kujo tools.

The skills are extracted from Kujo repositories rather than generic agent advice. They encode Kujo-specific defaults for writing `.kujo` programs, building CLI tools, preserving VM-first runtime behavior, respecting native capability boundaries, maintaining machine-readable CLI contracts, recording tool workflows, and contributing safely to the Rust implementation.

## Contents

- `SKILLS_INDEX.md`: skill catalog and activation map.
- `EXTRACTION_REPORT.md`: repository evidence, source map, confidence notes, and gaps.
- `VALIDATION_REPORT.md`: format/scope validation and maintainer review checklist.
- `guide/`: longer reference material distilled from repo docs, tests, and implementation.
- `skills/`: drop-in Agent Skills. Each folder name matches its skill name.
- `evals/`: trigger examples and quality cases for skill routing.

## Installation

Copy the desired folders from `skills/` into an Agent Skills-compatible location, or keep the whole `kujo-skills/` package under version control and point your agent workflow at it.

## Important Boundaries

- Kujo is VM-first for ordinary `kujo run <file>` workflows.
- The interpreter is an explicit fallback/debug path, not the default for ordinary scripts.
- Kujo is not a sandbox. Use `--untrusted` and least-privilege `--allow-*` flags for untrusted scripts, plus external isolation for high-risk environments.
- The repository has conflicting release-readiness wording in places. The skills follow the explicit pre-1.0 readiness boundary in `README.md`, `docs/LANGUAGE_SPEC.md`, `ROADMAP.md`, `docs/V1_SCOPE.md`, and `docs/PRE_V1_MASTER_UNFINISHED_CHECKLIST.md`.
