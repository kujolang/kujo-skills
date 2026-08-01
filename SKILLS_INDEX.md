# Kujo Skills Index

Use this index to route Kujo work to the narrowest skill that matches the repository, command surface, or review concern.

| Skill | Use when | Primary sources |
|---|---|---|
| `kujo-core-language` | Kujo syntax, imports, mutability, control flow, truthiness, and examples. | Kujo `README.md`, `docs/LANGUAGE_SPEC.md`, examples, docs tests |
| `kujo-tool-building` | Building practical Kujo CLI tools, JSON gates, repo scanners, and deterministic reports. | Kujo tool cookbook, standard library reference, CLI contracts |
| `kujo-security-hardening` | Reviewing untrusted Kujo, host effects, capability flags, AI/network egress, shell/process/db/archive risk. | Kujo native API security, secure AI scripting, runtime security tests |
| `kujo-enterprise-automation` | Enterprise-style Kujo automation, audit logs, strict AI replay, CI quality gates, external isolation. | Kujo enterprise/release docs and `scripts/enterprise_verify.sh` |
| `kujo-cli-contracts` | CLI JSON, stdout/stderr, exit codes, diagnostics, and machine-readable output compatibility. | Kujo CLI contract docs and CLI JSON tests |
| `kujo-standard-library` | Builtin arity, return values, capability gates, JSON/file/process/network/db/crypto/rendering/AI APIs. | Kujo standard library docs and stdlib contract tests |
| `kujo-testing-release-gates` | Test selection, broad validation, release gates, enterprise verification, and docs/example smoke tests. | Kujo release docs, scripts, and test suites |
| `kujo-runtime-parity` | VM/interpreter drift, `--interpreter`, `kujo test --runtime dual`, and parity matrix work. | Kujo parity docs and runtime path tests |
| `kujo-language-implementation` | Rust implementation changes in lexer/parser/compiler/VM/interpreter/native APIs. | Kujo architecture docs, `src/`, tests |
| `kujo-docgen-agent-readable` | `kujo docgen`, generated docs, docs JSON, adapter extraction, link validation, and AI task output. | Kujo DocGen docs, `src/docgen/`, DocGen tests |
| `kujo-maintainer-review` | Strict Kujo code review for correctness, contracts, security, parity, missing tests/docs, and readiness risk. | Kujo roadmap, spec, security, CLI contracts, tests |
| `kujo-agents-sdk-workflows` | Agents SDK runners, tools, approvals, handoffs, tracing, stores, retrieval, MCP 2026 helpers, and offline fixtures. | `../agents-sdk` README/docs/src/tests |
| `kujo-ai-chat-workflows` | AI Chat provider profiles, SQLite state, tools, browser tools, Codex/Watchdog profiles, SSE, benchmarks, smoke tests. | `../ai-chat` README, API contract, server, tests, scripts |
| `kujo-ai-sdk-workflows` | AI SDK provider contracts, fixture mode, streaming, retries, redaction, model preferences, live smoke. | `../ai-sdk` README/src/tests/scripts |
| `kujo-benchmarks-capsule-workflows` | Capsule benchmark handoff capsules and stable capsule artifacts. | `../benchmarks-capsule` README/spec/tests |
| `kujo-casefile-workflows` | Casefile evidence bundles, captures, handoffs, redaction, cleanup, and `.casefile/` artifacts. | `../casefile` README/docs/tests |
| `kujo-changebucket-workflows` | Change footprint, churn budgets, risk reports, dependency/generated file checks. | `../changebucket` README/src/tests |
| `kujo-cms-workflows` | CMS runtime, content models, delivery routes, auth, migrations, backup/restore, release proof. | `../cms` README/backend/tests/docs |
| `kujo-concord-workflows` | Concord artifact drift scans, CLI/docs drift, Spec/Eval alignment, and fix-task reports. | `../concord` README/src/tests |
| `kujo-crud-api-workflows` | CRUD API showcase, SQLite item/project APIs, Next.js playground, smoke/perf/DR checks. | `../crud-api` README/src/frontend/tests |
| `kujo-dispatch-workflows` | Dispatch workflow orchestration, resume/inspect/cleanup, plugins, event sinks, policy profiles. | `../dispatch` README/src/tests/docs |
| `kujo-eval-workflows` | Eval suites, snapshots, reports, policy-explain, artifact manifests, and CI gates. | `../eval` README/docs/main/tests |
| `kujo-fence-workflows` | Fence architecture boundaries, baselines, graph/explain, Markdown/JSON/SARIF reports. | `../fence` README/docs/src/tests |
| `kujo-howl-workflows` | Howl showcase manifests, validation, SVG/Markdown/HTML cards, galleries, captions. | `../howl` README/src/tests |
| `kujo-kennel-workflows` | Kennel package/project manager, lockfiles, static indexes, local hosted registry, trust/source policy. | `../kennel` README/src/tests/scripts |
| `kujo-lens-workflows` | Lens deterministic browser QA, flows, screenshots, accessibility/link/visual checks, repair briefs. | `../lens` README/docs/src/tests |
| `kujo-loop-engineering-workflows` | Bounded engineering harness workflows, checklists, blockers, evidence logs, opt-in commits. | `../kujo-workflows/loop-engineering` docs/scripts |
| `kujo-mcp-workflows` | Kujo MCP server generation, manifests, tool/resource registries, endpoint/security tests. | `../mcp` README/docs/src/tests |
| `kujo-muzzle-workflows` | Muzzle quiet workflows, manifests, logs/reports, loop mode, and redaction. | `../muzzle` README/docs/src/tests |
| `kujo-packwrite-workflows` | PackWrite execution packs, prompts, validation, doctor, and generated agent packs. | `../packwrite` README/docs |
| `kujo-patchbrief-workflows` | PatchBrief diff summaries, suggested tests, handoffs, schemas, and JSON contracts. | `../patchbrief` README/src/tests/schemas |
| `kujo-rag-workflows` | RAG ingest/query/serve/demo, indexes, namespaces, embeddings, retrieval, OpenAPI, release evals. | `../rag` README/docs/src/tests |
| `kujo-redact-workflows` | Redact scan/sanitize/verify/pack, policy YAML, leakage checks, and anonymization artifacts. | `../redact` README/docs/src/tests |
| `kujo-relay-workflows` | Relay bounded missions, agents/models/runs, evidence bundles, Watchdog posture, acceptance tests. | `../relay` README/docs/src/tests |
| `kujo-runledger-workflows` | RunLedger receipts, usage/cost, verdicts, notes/followups, compare/report output. | `../runledger` README/src/tests |
| `kujo-scent-workflows` | Scent packs, dry-run budgets, include/exclude filters, pack artifacts, and redaction audits. | `../scent` README/docs/scent.kujo |
| `kujo-scout-workflows` | Scout scans, context packs, `llms.txt`, `AGENTS.md`, manifests, exports, baselines, snapshots. | `../scout` README/docs/tests |
| `kujo-shipcheck-workflows` | ShipCheck scans, checklists, gates, release notes, report schema, release readiness checks. | `../shipcheck` README/docs/src/tests |
| `kujo-site-kit-workflows` | Canonical SiteKit skill for `site-kit`: tokens, components, schemas, generated dist, smoke, Workcell proof. | `../site-kit` README/docs/tests/scripts |
| `kujo-sitekit-workflows` | Compatibility alias for older SiteKit references; prefer `kujo-site-kit-workflows` for new work. | `../site-kit` README/docs/tests/scripts |
| `kujo-ssg-workflows` | SSG builds, templates, feeds, `llms.txt`, docs bridge, docs starter, parallel builds, release gates. | `../ssg` README/build/scripts/docs |
| `kujo-spec-workflows` | Spec contracts, validate/render/export-agent-context/export-eval/status/schema/policy work. | `../spec` README/docs/tests |
| `kujo-tribunal-workflows` | Tribunal decision evidence, reviews, signed bundles, trust policies, audit/verify gates. | `../tribunal` README/docs/src/tests |
| `kujo-watchdog-workflows` | Watchdog telemetry/proxy, dashboard/API, traces, auth/redaction/rate limits, pricing, backups, AI Chat integration. | `../watchdog` README/src/tests/scripts |
| `kujo-workcell-workflows` | Workcell container sandboxes, definitions, run/verify receipts, Docker/Podman boundaries. | `../workcell` README/docs/src/tests |
| `kujo-skill-auditor` | Weekly skills-pack drift audits and trigger/index refreshes. | `skills/*/SKILL.md`, this index, `evals/`, sibling repos |
| `kujo-readiness-auditor` | Recurring readiness posture, release preparedness, and evidence gaps. | Repo docs/tests/scripts/tool reports |
| `kujo-docs-drift-auditor` | README/reference/generated-doc staleness and docs/source mismatch. | Repo docs, examples, generated docs, CLI help |
| `kujo-release-gate-runner` | Pre-tag gates, release blockers, ShipCheck/Eval/Fence/DocGen evidence. | Release docs, CI config, gate artifacts |
| `kujo-cross-repo-dogfood-runner` | Cross-repo Kujo dogfood and recurring ecosystem evidence collection. | Selected repos and generated reports |
| `kujo-backlog-normalizer` | Convert audit/drift/security/readiness findings into fix-ready tasks. | Tool reports, issues/backlogs, manifests |
| `kujo-docgen-public-docs-refresh` | Refresh public DocGen docs, generated docs, gap outputs, and coverage gates. | Kujo DocGen docs and generated docs |
| `kujo-dependabot-alert-triage` | Dependabot/security alert triage across Kujo repos. | GitHub alerts, manifests, lockfiles, audit output |
