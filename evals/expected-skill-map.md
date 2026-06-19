# Expected Skill Map

Use this map to sanity-check trigger routing.

| Query theme | Expected skill(s) |
|---|---|
| General `.kujo` syntax, functions, loops, imports, truthiness | `kujo-core-language` |
| Building a JSON policy checker or repo scanner in Kujo | `kujo-tool-building`, optionally `kujo-enterprise-automation` |
| Running untrusted Kujo, shell/network/files/db/archive/HTML risks | `kujo-security-hardening` |
| CI/operator automation with auditability and capability minimization | `kujo-enterprise-automation`, optionally `kujo-cli-contracts` |
| CLI JSON output, exit codes, stdout/stderr, diagnostics, LSP helper payloads | `kujo-cli-contracts` |
| Builtin function usage, arity, capability gates, JSON/file/process/network/db/crypto APIs | `kujo-standard-library` |
| Test selection, release gates, docs/example smoke tests | `kujo-testing-release-gates` |
| Muzzle quiet workflows, `.muzzle/workflows/`, manifests, logs/reports, loop mode | `kujo-muzzle-workflows`, optionally `kujo-tool-building` or `kujo-enterprise-automation` |
| Casefile evidence bundles, `.casefile/`, `capture`, handoff, redaction, cleanup | `kujo-casefile-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Concord artifact drift, CLI/docs drift, Spec/Eval alignment, examples, source-of-truth findings | `kujo-concord-workflows`, optionally `kujo-cli-contracts`, `kujo-eval-workflows`, or `kujo-spec-workflows` |
| Dispatch workflow orchestration, `dispatch.kujo`, run state, traces, reports, approval gates, policy profiles | `kujo-dispatch-workflows`, optionally `kujo-tool-building` or `kujo-enterprise-automation` |
| Fence architecture boundaries, `fence.toml`, import violations, zone rules, baselines, SARIF/Markdown reports | `kujo-fence-workflows`, optionally `kujo-tool-building`, `kujo-cli-contracts`, or `kujo-enterprise-automation` |
| Howl showcase artifacts, `howl.json`, rendered cards/galleries/captions | `kujo-howl-workflows`, optionally `kujo-tool-building` or `kujo-core-language` |
| Lens browser QA, `.lens.toml`, reports, screenshots, flows, visual/accessibility checks | `kujo-lens-workflows`, optionally `kujo-tool-building` or `kujo-enterprise-automation` |
| MCP servers, `mcp make`, generated `.mcp/`, manifests, tool/resource registries, endpoint/security tests | `kujo-mcp-workflows`, optionally `kujo-tool-building`, `kujo-security-hardening`, or `kujo-enterprise-automation` |
| PatchBrief git-diff summaries, test suggestions, handoff notes, JSON briefs | `kujo-patchbrief-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Kujo RAG Starter Kit ingest/query/API, local RAG indexes, namespaces, parser/chunking/embedding/retrieval changes, release-eval gates | `kujo-rag-workflows`, optionally `kujo-core-language`, `kujo-tool-building`, `kujo-security-hardening`, or `kujo-enterprise-automation` |
| Scent context packs, `scent pack`, dry-run estimates, pack artifacts, redaction audits | `kujo-scent-workflows`, optionally `kujo-tool-building` or `kujo-enterprise-automation` |
| Scout codebase intelligence scans, context packs, security exports, baselines, Kennel metadata, fixtures, snapshots | `kujo-scout-workflows`, optionally `kujo-tool-building`, `kujo-security-hardening`, or `kujo-enterprise-automation` |
| ShipCheck release-readiness scans, `scan`, `checklist`, `gate`, json reports, CI release gates | `kujo-shipcheck-workflows`, optionally `kujo-cli-contracts` or `kujo-enterprise-automation` |
| RunLedger agent-run receipts, usage/cost capture, verdicts, compare/report, `.runledger/` JSON | `kujo-runledger-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Kujo Eval deterministic suites, checks, snapshots, reports, artifact manifests, policy profiles, CI gates | `kujo-eval-workflows`, optionally `kujo-cli-contracts` or `kujo-enterprise-automation` |
| ChangeBucket code-change footprint, blast-radius/risk reports, file-category counts, budget checks | `kujo-changebucket-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Spec task contracts, `.spec.yml`, validation, export-agent-context, export-eval, schema/policy and CI changes | `kujo-spec-workflows`, optionally `kujo-eval-workflows`, `kujo-cli-contracts`, or `kujo-enterprise-automation` |
| PackWrite agent execution packs, `MEGA_PROMPT.md`, `packwrite.toml`, provider setup, prompt handoff, offline fake-response tests | `kujo-packwrite-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Agents SDK runners, tools, approvals, handoffs, tracing, artifact/session/memory/retrieval contracts | `kujo-agents-sdk-workflows`, optionally `kujo-ai-sdk-workflows` or `kujo-tool-building` |
| AI Chat provider profiles, SSE streaming, SQLite chat state, smoke tests, bridge chat behavior | `kujo-ai-chat-workflows`, optionally `kujo-ai-sdk-workflows` or `kujo-watchdog-workflows` |
| AI SDK provider contracts, fixture mode, streaming, retries, redaction, live smoke, release gates | `kujo-ai-sdk-workflows`, optionally `kujo-security-hardening` or `kujo-enterprise-automation` |
| CMS content models, delivery routes, auth boundaries, webhooks, jobs, release gates | `kujo-cms-workflows`, optionally `kujo-security-hardening` or `kujo-enterprise-automation` |
| CRUD API showcase, item/project APIs, Next.js playground, smoke tests, DR/performance drills | `kujo-crud-api-workflows`, optionally `kujo-security-hardening` or `kujo-lens-workflows` |
| Kennel package/dependency manifests, lockfiles, static indexes, trust/source policy | `kujo-kennel-workflows`, optionally `kujo-security-hardening` or `kujo-enterprise-automation` |
| SSG static site build, templates/content, generated output, feeds/sitemap/llms, release gates | `kujo-ssg-workflows`, optionally `kujo-lens-workflows` or `kujo-shipcheck-workflows` |
| Watchdog AI telemetry, OpenAI-compatible proxy, request traces, auth/redaction/rate limits | `kujo-watchdog-workflows`, optionally `kujo-ai-chat-workflows` or `kujo-ai-sdk-workflows` |
| Weekly Kujo skill maintenance, stale SKILL.md drift, skill/index trigger refresh | `kujo-skill-auditor` |
| Recurring Kujo readiness posture, release preparedness, evidence gaps | `kujo-readiness-auditor`, optionally `kujo-shipcheck-workflows`, `kujo-fence-workflows`, or `kujo-eval-workflows` |
| Kujo docs drift, generated-doc staleness, README/reference mismatch | `kujo-docs-drift-auditor`, optionally `kujo-concord-workflows`, `kujo-scout-workflows`, or `kujo-docgen-agent-readable` |
| Kujo release gates, pre-tag checks, release blocker triage | `kujo-release-gate-runner`, optionally `kujo-shipcheck-workflows`, `kujo-eval-workflows`, or `kujo-docgen-agent-readable` |
| Cross-repo Kujo dogfood, recurring ecosystem checks, multi-repo evidence collection | `kujo-cross-repo-dogfood-runner`, optionally `kujo-concord-workflows`, `kujo-scent-workflows`, or `kujo-runledger-workflows` |
| Normalize Kujo audit findings, drift, release blockers, DocGen gaps, security triage into tasks | `kujo-backlog-normalizer`, optionally `kujo-spec-workflows` or `kujo-shipcheck-workflows` |
| Refresh Kujo DocGen public docs, generated docs, gap outputs, coverage gates | `kujo-docgen-public-docs-refresh`, optionally `kujo-docgen-agent-readable` |
| Dependabot or GitHub security alert triage across Kujo repos | `kujo-dependabot-alert-triage`, optionally `kujo-backlog-normalizer`, `kujo-patchbrief-workflows`, or `kujo-changebucket-workflows` |
| VM/interpreter drift, `--interpreter`, `--runtime dual`, parity matrix | `kujo-runtime-parity` |
| Rust implementation changes in parser/compiler/VM/interpreter/native APIs | `kujo-language-implementation` |
| `kujo docgen`, docs JSON, agent-readable docs, AI task output | `kujo-docgen-agent-readable` |
| Strict maintainer review | `kujo-maintainer-review` |
