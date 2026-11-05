# Audit report contract

Derived from the same user-supplied hardening prompt. In review mode, record proposed changes rather than implemented changes. If repository writes are forbidden, return the report without writing it. Record the verified code commit as the ending SHA; for uncommitted work record HEAD plus dirty status. A report commit cannot contain its own SHA. Mark unmeasured dimensions and unavailable checks explicitly.

# Cross-Repository Findings

If you discover a problem outside the current repository, record it separately.

For each cross-repository finding provide:

- affected repository,
- dependency or contract involved,
- evidence,
- impact,
- recommended change,
- whether the current repository requires that change,
- compatibility concerns.

Do not silently expand the implementation scope.

---

# Required Final Report

Create or update a repository-local audit report such as:

`docs/audits/repository-hardening.md`

Use another location if the repository already has an established convention.

The report must include:

## Repository

- repository name
- branch
- starting SHA
- ending SHA
- purpose
- important dependencies/integrations

## Baseline

What was tested and measured before changes.

## Findings

A table:

| ID | Priority | Area | Finding | Evidence | Action | Status |
|---|---|---|---|---|---|---|

## Changes Implemented

For every meaningful change:

- problem,
- root cause,
- implementation,
- files affected,
- tests added/changed,
- compatibility considerations,
- measured impact where applicable.

## Performance & Efficiency

Include applicable before/after data for:

- runtime,
- memory,
- build,
- binary/output size,
- token/context usage,
- output verbosity,
- dependency surface.

Do not include meaningless dimensions.

## Security

Summarize trust boundaries reviewed, vulnerabilities fixed, tests added, and remaining concerns.

## Compatibility

Explicitly state whether:

- public APIs changed,
- CLI behavior changed,
- file formats changed,
- schemas changed,
- config changed,
- environment variables changed,
- external consumers may be affected.

## Cross-Repository Follow-Ups

List anything requiring another Kujo repository.

## Remaining Work

Classify remaining work as:

- **P0**
- **P1**
- **P2**
- **P3**
- **Needs more evidence**
- **Not worth changing**

## Verification Receipt

Provide the exact commands executed and whether they passed.

Keep verbose logs in artifacts/files when appropriate rather than dumping enormous output into the final response.

---

