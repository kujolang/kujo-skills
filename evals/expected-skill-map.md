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
| Kujo RAG Starter Kit ingest/query/API, local RAG indexes, namespaces, parser/chunking/embedding/retrieval changes, release-eval gates | `kujo-rag-workflows`, optionally `kujo-core-language`, `kujo-tool-building`, `kujo-security-hardening`, or `kujo-enterprise-automation` |
| Dispatch workflow orchestration, `dispatch.kujo`, run state, traces, reports, approval gates, policy profiles | `kujo-dispatch-workflows`, optionally `kujo-tool-building` or `kujo-enterprise-automation` |
| Scent context packs, `scent pack`, dry-run estimates, pack artifacts, redaction audits | `kujo-scent-workflows`, optionally `kujo-tool-building` or `kujo-enterprise-automation` |
| MCP servers, `mcp make`, generated `.mcp/`, manifests, tool/resource registries, endpoint/security tests | `kujo-mcp-workflows`, optionally `kujo-tool-building`, `kujo-security-hardening`, or `kujo-enterprise-automation` |
| Howl showcase artifacts, `howl.json`, rendered cards/galleries/captions | `kujo-howl-workflows`, optionally `kujo-tool-building` or `kujo-core-language` |
| Casefile evidence bundles, `.casefile/`, `capture`, handoff, redaction, cleanup | `kujo-casefile-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| ShipCheck release-readiness scans, `scan`, `checklist`, `gate`, json reports, CI release gates | `kujo-shipcheck-workflows`, optionally `kujo-cli-contracts` or `kujo-enterprise-automation` |
| Lens browser QA, `.lens.toml`, reports, screenshots, flows, visual/accessibility checks | `kujo-lens-workflows`, optionally `kujo-tool-building` or `kujo-enterprise-automation` |
| PatchBrief git-diff summaries, test suggestions, handoff notes, JSON briefs | `kujo-patchbrief-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Agents SDK runners, tools, approvals, handoffs, tracing, artifact/session/memory/retrieval contracts | `kujo-agents-sdk-workflows`, optionally `kujo-ai-sdk-workflows` or `kujo-tool-building` |
| AI Chat provider profiles, SSE streaming, SQLite chat state, smoke tests, bridge chat behavior | `kujo-ai-chat-workflows`, optionally `kujo-ai-sdk-workflows` or `kujo-watchdog-workflows` |
| AI SDK provider contracts, fixture mode, streaming, retries, redaction, live smoke, release gates | `kujo-ai-sdk-workflows`, optionally `kujo-security-hardening` or `kujo-enterprise-automation` |
| ChangeBucket change footprint, churn metrics, file categories, budget enforcement | `kujo-changebucket-workflows`, optionally `kujo-cli-contracts` |
| CMS content models, delivery routes, auth boundaries, webhooks, jobs, release gates | `kujo-cms-workflows`, optionally `kujo-security-hardening` or `kujo-enterprise-automation` |
| CRUD API showcase, item/project APIs, Next.js playground, smoke tests, DR/performance drills | `kujo-crud-api-workflows`, optionally `kujo-security-hardening` or `kujo-lens-workflows` |
| Eval suites, reports, snapshots, policy profiles, artifact manifests, command inventory | `kujo-eval-workflows`, optionally `kujo-cli-contracts` or `kujo-enterprise-automation` |
| Fence architecture boundaries, fence.toml, check/explain/graph/baseline workflows | `kujo-fence-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Kennel package/dependency manifests, lockfiles, static indexes, trust/source policy | `kujo-kennel-workflows`, optionally `kujo-security-hardening` or `kujo-enterprise-automation` |
| PackWrite mega prompts, agent packs, validation, provider config, fake AI responses | `kujo-packwrite-workflows`, optionally `kujo-ai-sdk-workflows` or `kujo-cli-contracts` |
| RunLedger agent run receipts, usage/cost, compare/report, .runledger data | `kujo-runledger-workflows`, optionally `kujo-patchbrief-workflows` |
| Scout codebase maps, route/dependency/security scans, baselines, SARIF/JSONL, Kennel metadata | `kujo-scout-workflows`, optionally `kujo-kennel-workflows` or `kujo-security-hardening` |
| Spec task contracts, validation, render/export, schemas, command inventory, safe-write mode | `kujo-spec-workflows`, optionally `kujo-eval-workflows` or `kujo-dispatch-workflows` |
| SSG static site build, templates/content, generated output, feeds/sitemap/llms, release gates | `kujo-ssg-workflows`, optionally `kujo-lens-workflows` or `kujo-shipcheck-workflows` |
| Watchdog AI telemetry, OpenAI-compatible proxy, request traces, auth/redaction/rate limits | `kujo-watchdog-workflows`, optionally `kujo-ai-chat-workflows` or `kujo-ai-sdk-workflows` |
| VM/interpreter drift, `--interpreter`, `--runtime dual`, parity matrix | `kujo-runtime-parity` |
| Rust implementation changes in parser/compiler/VM/interpreter/native APIs | `kujo-language-implementation` |
| `kujo docgen`, docs JSON, agent-readable docs, AI task output | `kujo-docgen-agent-readable` |
| Strict maintainer review | `kujo-maintainer-review` |
