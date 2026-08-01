# Expected Skill Map

Use this map to sanity-check routing fixtures and natural-language trigger behavior.

| Query theme | Expected skill(s) |
|---|---|
| General `.kujo` syntax, functions, loops, imports, truthiness | `kujo-core-language` |
| Building Kujo JSON policy checkers, repo scanners, deterministic CLI tools | `kujo-tool-building`, optionally `kujo-enterprise-automation` |
| Untrusted Kujo scripts, capability flags, shell/network/files/db/archive/HTML/AI egress risk | `kujo-security-hardening` |
| CLI JSON, exit codes, stdout/stderr, diagnostics, LSP helper payloads | `kujo-cli-contracts` |
| Builtin arity, return values, capability gates, JSON/file/process/network/db/crypto/rendering/AI APIs | `kujo-standard-library` |
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
| Howl showcase cards and galleries | `kujo-howl-workflows` |
| Kennel package manager, lockfiles, hosted registry, trust/source policy | `kujo-kennel-workflows` |
| Lens browser QA, flows, screenshots, visual/accessibility checks | `kujo-lens-workflows` |
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
| Cross-repo dogfood evidence | `kujo-cross-repo-dogfood-runner` |
| Normalize audit findings into tasks | `kujo-backlog-normalizer` |
| Public DocGen docs refresh | `kujo-docgen-public-docs-refresh` |
| Dependabot/security alert triage | `kujo-dependabot-alert-triage` |
