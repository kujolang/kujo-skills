# Kujo Skills Index

Use this index to route Kujo work to the narrowest skill that matches the repository, command surface, or review concern.

| Skill | Use when | Primary sources |
|---|---|---|
| `kujo-core-language` | Kujo syntax, imports, mutability, control flow, truthiness, and examples. | Kujo `README.md`, `docs/LANGUAGE_SPEC.md`, examples, docs tests |
| `kujo-tool-building` | Building practical Kujo CLI tools, JSON gates, repo scanners, and deterministic reports. | Kujo tool cookbook, standard library reference, CLI contracts |
| `kujo-security-hardening` | Reviewing untrusted Kujo, host effects, capability flags, AI/network egress, shell/process/db/archive risk. | Kujo native API security, secure AI scripting, runtime security tests |
| `kujo-enterprise-automation` | Enterprise-style Kujo automation, audit logs, strict AI replay, CI quality gates, external isolation. | Kujo enterprise/release docs and `scripts/enterprise_verify.sh` |
| `kujo-cli-contracts` | CLI JSON, stdout/stderr, exit codes, diagnostics, and machine-readable output compatibility. | Kujo CLI contract docs and CLI JSON tests |
| `kujo-standard-library` | Builtin arity, return values, capability gates, JSON/JSONL/file/process/network/db/crypto/rendering/AI APIs. | Kujo standard library docs and stdlib contract tests |
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
| `kujo-howl-workflows` | Howl showcase manifests, validation, SVG/Markdown/HTML cards, branded social cards, galleries, captions. | `../howl` README/src/tests |
| `kujo-kennel-workflows` | Kennel package/project manager, lockfiles, static indexes, local hosted registry, trust/source policy. | `../kennel` README/src/tests/scripts |
| `kujo-lens-workflows` | Lens deterministic browser QA, quick checks, flows, screenshots, accessibility/link/visual checks, repair briefs. | `../lens` README/docs/src/tests |
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
| `kujo-ecosystem-launch` | Stage-gated Kujo tool, workflow, skill-pack, or agent-team releases plus verified public site synchronization. | Source release artifacts, target site repositories, specialist skills, release and deployment evidence |
| `kujo-cross-repo-dogfood-runner` | Cross-repo Kujo dogfood and recurring ecosystem evidence collection. | Selected repos and generated reports |
| `kujo-backlog-normalizer` | Convert audit/drift/security/readiness findings into fix-ready tasks. | Tool reports, issues/backlogs, manifests |
| `kujo-docgen-public-docs-refresh` | Refresh public DocGen docs, generated docs, gap outputs, and coverage gates. | Kujo DocGen docs and generated docs |
| `kujo-dependabot-alert-triage` | Dependabot/security alert triage across Kujo repos. | GitHub alerts, manifests, lockfiles, audit output |

## Publishing House skills

| Skill | Use when | Primary sources |
|---|---|---|
| `kujo-publishing-house-workflows` | Installing, routing, running, recovering, or maintaining the complete Publishing House lifecycle. | `../kujo-workflows/docs/publishing-house/`, workflow kits, runtime, contracts, tests |
| `publishing-house-profile-setup` | Creating or validating portable House, Brand, and Audience profiles. | `../kujo-agents/publishing-house/` constitution, shared contracts, permission model |
| `publishing-house-quality-calibration` | Running or maintaining blind premium-quality calibration without automating editorial taste. | Publishing House quality standard/evals and BluePencil calibration contracts |
| `kujo-storydesk-workflows` | Operating editorial ideas, commissions, assignments, queues, packets, handoffs, and review state. | `../storydesk` README, CLI, contracts, security, tests |
| `kujo-dossier-workflows` | Recording and verifying claims, sources, evidence, conflicts, quotations, consent, rights, and freshness. | `../dossier` README, CLI, contracts, security, tests |
| `kujo-galleypack-workflows` | Packaging exact artifact versions with lineage, evidence, reviews, checksums, and drift validation. | `../galleypack` README, CLI, contracts, security, tests |
| `kujo-bluepencil-workflows` | Running structured editorial reviews, disagreements, focused checks, and blind calibration. | `../bluepencil` README, CLI, calibration corpus, contracts, tests |
| `kujo-versionseal-workflows` | Requesting, recording, verifying, revoking, or expiring exact-version human approvals. | `../versionseal` README, CLI, policy/signature contracts, tests |
| `kujo-presswire-workflows` | Preflighting and performing approval-gated publication, correction, or unpublish effects. | `../presswire` README, CLI, adapter contracts, security, tests |
| `kujo-readersignal-workflows` | Capturing privacy-bounded measurements, feedback, comparisons, learning, and follow-up recommendations. | `../readersignal` README, CLI, privacy/retention contracts, tests |
| `kujo-assetworks-workflows` | Planning and validating media transforms, accessibility artifacts, provenance, and manifests. | `../assetworks` README, CLI, adapter contracts, security, tests |

## WebOps skills

| Skill | Use when | Primary sources |
|---|---|---|
| `webops-site-profile` | Configuring or validating a portable WebOps site profile, repository binding, integration references, permission default, or site identity. | WebOps profile schema and Agency Runner site profiles |
| `webops-capability-preflight` | Checking which WebOps website, repository, browser, search, analytics, performance, backlink, keyword, publishing, distribution, or submission capabilities are available. | WebOps capability schema plus tool doctor/capabilities outputs |
| `webops-longitudinal-findings` | Creating, comparing, or updating stable WebOps findings, recommendations, actions, outcomes, and recurring-run history. | WebOps finding/history schemas and prior run artifacts |
| `kujo-siteprobe-workflows` | Running, validating, verifying, comparing, reporting, or integrating SiteProbe website-intelligence crawls and signed `.siteprobe` artifacts. | `../siteprobe` README, CLI, schemas, tests, and security contract |
| `kujo-searchbridge-workflows` | Running SearchBridge doctor, capability preflight, fixture providers, normalized evidence reads, batch reads, evidence-query, signed adapters, replay/cache, telemetry, or explicit ACT submission. | `../searchbridge` README, provider research, schemas, tests, and security contract |
| `kujo-contentgraph-workflows` | Building, inspecting, comparing, explaining, analyzing, exporting, or consuming deterministic ContentGraph artifacts. | `../contentgraph` README, methodology, schemas, tests, and security contract |
| `webops-technical-seo` | Performing a deterministic technical SEO audit from crawl evidence. | SiteProbe artifacts, WebOps history, and optional Lens/inspection evidence |
| `webops-search-performance` | Analyzing longitudinal measured search performance. | SearchBridge search.performance result/v1 and prior comparable windows |
| `webops-indexation` | Auditing crawlability, local indexability, and confirmed provider index state. | SiteProbe robots/sitemap/page artifacts and optional SearchBridge URL inspection |
| `webops-keyword-opportunity` | Finding query opportunities while separating measurement, estimates, and public research. | SearchBridge search/keyword results, public research, and ContentGraph coverage |
| `webops-ai-search-visibility` | Running repeatable AI/search visibility benchmark suites. | Fixed query suite, configured surfaces, dated response evidence, and prior benchmark |
| `webops-content-gap` | Classifying site coverage against audience/search needs. | ContentGraph corpus, research, optional query data, and current site profile |
| `webops-content-decay` | Identifying content deterioration or staleness without conflating age and decline. | SearchBridge longitudinal results, ContentGraph, factual sources, analytics, and history |
| `webops-internal-linking` | Analyzing, proposing, or explicitly applying contextual internal links. | ContentGraph opportunities, page context, SiteProbe links, optional repository |
| `webops-content-accuracy` | Reviewing website claims for outdated or invalid guidance. | Current authoritative primary sources, content corpus, and retrieval provenance |
| `webops-cannibalization` | Identifying likely intent competition while separating normal overlap. | ContentGraph overlaps plus SearchBridge query/page evidence |
| `webops-content-portfolio` | Assigning longitudinal content portfolio states. | ContentGraph, search, analytics, backlink, freshness, and business-purpose evidence |
| `webops-content-pruning` | Reviewing obsolete or redundant content for keep, refresh, merge, redirect, or retire proposals. | ContentGraph, accuracy review, measured providers, backlinks, and business context |
| `webops-information-architecture` | Auditing site navigation, hierarchy, taxonomy, URLs, depth, clusters, and discoverability. | ContentGraph, SiteProbe graph/depth, Lens navigation evidence, and source structure |
| `webops-schema-and-metadata` | Auditing structured data and page/social metadata. | SiteProbe metadata/structured-data artifacts, visible content, and current authoritative guidance |
| `webops-web-performance` | Analyzing lab and field website performance as distinct evidence classes. | SearchBridge PageSpeed/CrUX, Lens environment-relative metrics, and prior runs |
| `webops-accessibility-review` | Running repeatable automated accessibility review with explicit manual gaps. | Lens accessibility artifacts, rendered routes, and applicable manual review |
| `webops-link-health` | Auditing broken, redirected, malformed, or unexpected links. | SiteProbe link/status/redirect evidence and optional Lens interactions |
| `webops-competitor-intelligence` | Monitoring selected public competitors or peers for meaningful change. | Public web evidence, bounded SiteProbe runs, optional SearchBridge estimates, and prior baseline |
| `webops-backlink-and-mention-analysis` | Analyzing new/lost backlinks, linked and unlinked mentions, and evidence-backed link concerns. | SearchBridge backlink data, public web research, and prior run |
| `webops-search-standards-watch` | Monitoring authoritative search, indexing, structured-data, analytics, browser, AI-search, and web-standard changes. | Official search-engine, analytics, browser, standards-body, and provider documentation |
| `webops-search-submission` | Preflighting or performing explicit ACT search submission through supported providers. | SearchBridge providers/capabilities, site ownership, approved URL list, and receipt schema |
| `webops-analytics-analysis` | Analyzing real website behavior from normalized analytics evidence. | SearchBridge analytics result/v1, property identity settings, dimensions, metrics, and prior window |
| `webops-distribution` | Creating source-grounded distribution assets and optionally publishing with ACT authority. | Approved published content, Howl, distribution integration, permission receipt, and brand constraints |
| `webops-reporting` | Synthesizing validated specialist evidence into quiet WebOps reports. | Validated current/prior WebOps artifacts, finding history, actions, outcomes, and availability receipts |
