---
name: kujo-hardening
description: "Use for a deep repository hardening, cleanup, performance, resource, token/context efficiency, and reliability pass, including requests to use the Kujo or Cujo hardening skill to review, fix, or update a repo. Supports review-only and implementation modes. Not a default for isolated bug fixes or ordinary feature work."
---

# Kujo Hardening

Turn one repository into a measurably stronger, simpler, safer system while preserving supported behavior. Read implementation and prove conclusions; a large diff is not a success criterion. This workflow applies across languages in the Kujo ecosystem and to other repositories when requested.

## Choose the mode and boundary

- **Review:** Requests to review, audit, inspect, or assess produce evidence and prioritized recommendations. Do not modify implementation. A repository-local report is allowed unless the user requests strictly read-only work.
- **Fix:** Requests to harden, fix, clean up, optimize, or update using this skill authorize implementing justified, high-confidence improvements within the requested scope. Complete verification and affected documentation.
- Explicit caller constraints override these defaults. A bare invocation defaults to review. Do not infer an ecosystem-wide rewrite from a single-repository request.
- Identify the target Git root, applicable instructions, branch, starting SHA, existing changes, and requested scope. Preserve user work. Related repositories may be inspected for contracts; write only to the target repository unless separately authorized. Document cross-repository dependencies and follow-ups.
- Use repository-specific build/test commands and installed focused skills when relevant; this skill does not assume Kujo source or require optional ecosystem tools. It does not itself authorize publishing, deployment, commits, pushes, destructive migration, or live external operations. Honor authorization already given by the caller.

## Evidence and compatibility rules

Before changing behavior, identify affected APIs, CLI/exit/error contracts, schemas and serialization, configuration and environment variables, filesystem behavior, package/network interfaces, generated artifacts, tests, and downstream consumers. Preserve compatibility; explain any necessary correction and migration path.

Distinguish measured facts, code-supported inference, likely issues, and hypotheses. Do not invent benchmark improvements, token savings, or security findings. Measure representative workloads before and after with the same method, record conditions and variability, and verify equivalent useful behavior. Label token estimates explicitly.

Fix root causes. Never weaken assertions, disable tests, swallow errors, conceal races with sleeps/timeouts, silently truncate required data, remove validation, bypass security, hardcode host-specific behavior, substitute brittle parsing for structured data, or hide failures behind broad fallbacks. Preserve safety, diagnostics, observability, determinism, and correctness while reducing cost.

Do not remove apparent dead weight until supported functionality, releases, downstream consumers, tests, docs, and compatibility contracts have been checked. Preserve uncertain candidates and record the uncertainty. Avoid cosmetic churn, one-off abstractions, speculative caching, and dependency replacement without maintenance and correctness evidence.

## Execute the pass

1. Read [the audit checklist](references/audit-checklist.md) before beginning. Cover phases 0–16 against actual implementation, recording evidence or an explicit not-applicable rationale for each area. Respect a narrower caller scope and disclose exclusions.
2. Establish the existing build/test/check baseline before edits. Capture pre-existing failures separately. Benchmark only relevant dimensions: runtime, resources, build/output size, token/context size, command output, or dependency surface.
3. Maintain a finding ledger with evidence, confidence, impact, priority, action, and status. P0 covers correctness, security, integrity, dangerous concurrency, and broken contracts; P1 covers meaningful performance/resource/context waste, major maintainability issues, and critical missing tests; P2 covers useful simplification and smaller efficiency/ergonomic improvements; P3 is cosmetic. Do not spend substantial effort on P3 while meaningful P0–P2 work remains.
4. In review mode, stop short of implementation and report findings, verification limits, and recommended fixes. In fix mode, execute phases 17–18: implement high-confidence in-scope improvements, add practical behavioral regression coverage, update affected docs, and add stable regression gates where worthwhile. Document how intentional growth updates budgets; do not add flaky gates or meaningless benchmarks.
5. Rerun the full relevant verification suite and comparable benchmarks. Separate baseline failures, new failures, unavailable checks, and unresolved hypotheses. Do not claim success with a known introduced regression. If blocked, preserve useful partial evidence and identify the exact unfinished work.

For AI-facing repositories, explicitly evaluate progressive disclosure, schema/tool registration size, replay/retry amplification, handoff/context duplication, and command-result volume. Prefer execute → preserve evidence → concise receipt. Never trade away necessary context or observability for smaller outputs.

## Deliver and finish

Read [the report contract](references/report.md) when creating the audit report, normally at `docs/audits/repository-hardening.md` or the established repository location. Preserve baseline evidence and distinguish this run from earlier audits. Include exact verification commands and statuses, measured impact, compatibility effects, cross-repository requirements, and meaningful remaining work. Keep verbose logs in artifacts rather than the final chat reply.

Completion requires coverage of all applicable areas, supported findings, honest baseline comparisons, and an accurate report. Fix mode also requires verified justified improvements, practical regression coverage, accurate affected documentation, and no known introduced regression. Do not manufacture changes when inspection shows no justified improvement. Existing failures or unavailable checks must remain explicit limitations rather than a false all-pass claim.

Return a concise receipt: result, highest-value changes or review findings, supported measurements, verification, meaningful unresolved work, cross-repository follow-ups, and final commit SHA if committed. Respect a caller request for an even shorter response while preserving the detailed report.
