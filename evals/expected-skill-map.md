# Expected Skill Map

Use this map to sanity-check routing fixtures and natural-language trigger behavior.

| Query theme | Expected skill(s) |
|---|---|
| Cross-cutting Kujo project development, ecosystem routing, compact AI-native design, anti-slop review, and evidence-backed completion | `kujo-way-development`, plus the narrowest focused skill when needed |
| General `.kujo` syntax, functions, loops, imports, truthiness | `kujo-core-language` |
| Building Kujo JSON policy checkers, repo scanners, deterministic CLI tools | `kujo-tool-building`, optionally `kujo-enterprise-automation` |
| Untrusted Kujo scripts, capability flags, shell/network/files/db/archive/HTML/AI egress risk | `kujo-security-hardening` |
| CLI JSON, exit codes, stdout/stderr, diagnostics, LSP helper payloads | `kujo-cli-contracts` |
| Builtin arity, return values, capability gates, JSON/JSONL/file/process/network/db/crypto/rendering/AI APIs | `kujo-standard-library` |
| Test selection, release gates, enterprise verify, docs/example smoke tests | `kujo-testing-release-gates` |
| VM/interpreter drift, `--interpreter`, dual runtime checks | `kujo-runtime-parity` |
| Rust implementation changes | `kujo-language-implementation` |
| `kujo docgen`, generated docs, docs JSON, adapter extraction | `kujo-docgen-agent-readable` |
| Strict maintainer review | `kujo-maintainer-review` |
| Agents SDK runtime primitives, MCP 2026 helpers, adapter boundaries, offline fixtures | `kujo-agents-sdk-workflows` |
| AI Chat provider profiles, SSE streaming, tools, browser tools, Codex/Watchdog profiles, benchmarks | `kujo-ai-chat-workflows`, optionally `kujo-ai-sdk-workflows` or `kujo-watchdog-workflows` |
| AI SDK provider contracts, fixture mode, streaming, retries, redaction, live smoke | `kujo-ai-sdk-workflows` |
| Capsule benchmark handoff artifacts | `kujo-benchmarks-capsule-workflows` |
| Casefile evidence bundles and redaction | `kujo-casefile-workflows` |
| Change footprint budgets and risk reports | `kujo-changebucket-workflows` |
| CMS runtime, content models, delivery routes, auth, migrations | `kujo-cms-workflows` |
| Concord artifact/docs/schema drift | `kujo-concord-workflows` |
| CRUD API showcase and Next.js playground checks | `kujo-crud-api-workflows` |
| Dispatch workflows, resume/inspect/cleanup, plugins, event sinks | `kujo-dispatch-workflows` |
| Eval suites, snapshots, reports, artifact manifests, policy gates | `kujo-eval-workflows` |
| Fence architecture boundary checks | `kujo-fence-workflows` |
| Howl showcase cards, branded social cards, and galleries | `kujo-howl-workflows` |
| Kennel package manager, lockfiles, hosted registry, trust/source policy | `kujo-kennel-workflows` |
| Lens browser QA, quick checks, flows, screenshots, visual/accessibility checks | `kujo-lens-workflows` |
| Loop engineering harness | `kujo-loop-engineering-workflows` |
| Kujo MCP server generation and registries | `kujo-mcp-workflows` |
| Muzzle quiet workflows | `kujo-muzzle-workflows` |
| PackWrite execution packs | `kujo-packwrite-workflows` |
| PatchBrief summaries, suggested tests, handoffs | `kujo-patchbrief-workflows` |
| RAG ingest/query/serve/demo and release evals | `kujo-rag-workflows` |
| Redact scan/sanitize/verify/pack | `kujo-redact-workflows` |
| Relay missions, agents/models/runs, evidence bundles | `kujo-relay-workflows` |
| RunLedger receipts, usage/cost, verdicts, reports | `kujo-runledger-workflows` |
| Scent context packs | `kujo-scent-workflows` |
| Scout codebase intelligence scans | `kujo-scout-workflows` |
| ShipCheck release readiness | `kujo-shipcheck-workflows` |
| SiteKit design-system tokens/components/dist smoke/Workcell proof | `kujo-site-kit-workflows`, compatibility `kujo-sitekit-workflows` |
| SSG builds, docs bridge, docs starter, parallel builds, release gates | `kujo-ssg-workflows` |
| Spec task contracts | `kujo-spec-workflows` |
| Tribunal decision evidence | `kujo-tribunal-workflows` |
| Watchdog telemetry/proxy/dashboard/pricing/backups | `kujo-watchdog-workflows` |
| Workcell local container sandboxes | `kujo-workcell-workflows` |
| Weekly skill maintenance and stale skill/index/fixture drift | `kujo-skill-auditor` |
| Readiness posture/evidence audit | `kujo-readiness-auditor` |
| Docs/generated-artifact drift | `kujo-docs-drift-auditor` |
| Release gate and blocker triage | `kujo-release-gate-runner` |
| Release a Kujo tool, workflow, skill pack, or agent team and synchronize its verified website pages, visuals, social cards, discovery surfaces, deployment, and live checks | `kujo-ecosystem-launch` |
| Cross-repo dogfood evidence | `kujo-cross-repo-dogfood-runner` |
| Normalize audit findings into tasks | `kujo-backlog-normalizer` |
| Public DocGen docs refresh | `kujo-docgen-public-docs-refresh` |
| Dependabot/security alert triage | `kujo-dependabot-alert-triage` |

## Publishing House routing

| Query theme | Expected skill(s) |
|---|---|
| Install, route, run, inspect, or recover the complete Publishing House lifecycle | `kujo-publishing-house-workflows` |
| Create portable House, Brand, and Audience profiles | `publishing-house-profile-setup` |
| Run blind premium-quality calibration | `publishing-house-quality-calibration`, optionally `kujo-bluepencil-workflows` |
| Editorial ideas, commissions, assignments, packets, handoffs, and review queues | `kujo-storydesk-workflows` |
| Claims, sources, captured evidence, conflicts, quotations, consent, rights, and freshness | `kujo-dossier-workflows` |
| Exact editorial artifact packages, lineage, checksums, freezes, and drift | `kujo-galleypack-workflows` |
| Editorial reviews, blockers, disagreements, and calibration records | `kujo-bluepencil-workflows` |
| Exact-version human approval, rejection, revocation, expiry, and verification | `kujo-versionseal-workflows` |
| Approval-gated scheduling, publication, correction, unpublish, and receipts | `kujo-presswire-workflows` |
| Privacy-bounded audience measurement, feedback, learning, and follow-up | `kujo-readersignal-workflows` |
| Media planning, transforms, accessibility artifacts, provenance, and manifests | `kujo-assetworks-workflows` |

## WebOps routing

| Query theme | Expected skill(s) |
|---|---|
| Configuring or validating a portable WebOps site profile, repository binding, integration references, permission default, or site identity | `webops-site-profile` |
| Checking which WebOps website, repository, browser, search, analytics, performance, backlink, keyword, publishing, distribution, or submission capabilities are available | `webops-capability-preflight` |
| Creating, comparing, or updating stable WebOps findings, recommendations, actions, outcomes, and recurring-run history | `webops-longitudinal-findings` |
| Running, validating, verifying, comparing, reporting, or integrating SiteProbe website-intelligence crawls and signed `.siteprobe` artifacts | `kujo-siteprobe-workflows` |
| Running SearchBridge doctor, capability preflight, fixture providers, normalized evidence reads, batch reads, evidence-query, signed adapters, replay/cache, telemetry, or explicit ACT submission | `kujo-searchbridge-workflows` |
| Building, inspecting, comparing, explaining, analyzing, exporting, or consuming deterministic ContentGraph artifacts | `kujo-contentgraph-workflows` |
| Performing a deterministic technical SEO audit from crawl evidence | `webops-technical-seo` |
| Analyzing longitudinal measured search performance | `webops-search-performance` |
| Auditing crawlability, local indexability, and confirmed provider index state | `webops-indexation` |
| Finding query opportunities while separating measurement, estimates, and public research | `webops-keyword-opportunity` |
| Running repeatable AI/search visibility benchmark suites | `webops-ai-search-visibility` |
| Classifying site coverage against audience/search needs | `webops-content-gap` |
| Identifying content deterioration or staleness without conflating age and decline | `webops-content-decay` |
| Analyzing, proposing, or explicitly applying contextual internal links | `webops-internal-linking` |
| Reviewing website claims for outdated or invalid guidance | `webops-content-accuracy` |
| Identifying likely intent competition while separating normal overlap | `webops-cannibalization` |
| Assigning longitudinal content portfolio states | `webops-content-portfolio` |
| Reviewing obsolete or redundant content for keep, refresh, merge, redirect, or retire proposals | `webops-content-pruning` |
| Auditing site navigation, hierarchy, taxonomy, URLs, depth, clusters, and discoverability | `webops-information-architecture` |
| Auditing structured data and page/social metadata | `webops-schema-and-metadata` |
| Analyzing lab and field website performance as distinct evidence classes | `webops-web-performance` |
| Running repeatable automated accessibility review with explicit manual gaps | `webops-accessibility-review` |
| Auditing broken, redirected, malformed, or unexpected links | `webops-link-health` |
| Monitoring selected public competitors or peers for meaningful change | `webops-competitor-intelligence` |
| Analyzing new/lost backlinks, linked and unlinked mentions, and evidence-backed link concerns | `webops-backlink-and-mention-analysis` |
| Monitoring authoritative search, indexing, structured-data, analytics, browser, AI-search, and web-standard changes | `webops-search-standards-watch` |
| Preflighting or performing explicit ACT search submission through supported providers | `webops-search-submission` |
| Analyzing real website behavior from normalized analytics evidence | `webops-analytics-analysis` |
| Creating source-grounded distribution assets and optionally publishing with ACT authority | `webops-distribution` |
| Synthesizing validated specialist evidence into quiet WebOps reports | `webops-reporting` |
