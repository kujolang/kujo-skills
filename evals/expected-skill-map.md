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
| RunLedger agent-run receipts, usage/cost capture, verdicts, compare/report, `.runledger/` JSON | `kujo-runledger-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Kujo Eval deterministic suites, checks, snapshots, reports, artifact manifests, policy profiles, CI gates | `kujo-eval-workflows`, optionally `kujo-cli-contracts` or `kujo-enterprise-automation` |
| ChangeBucket code-change footprint, blast-radius/risk reports, file-category counts, budget checks | `kujo-changebucket-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| Spec task contracts, `.spec.yml`, validation, export-agent-context, export-eval, schema/policy and CI changes | `kujo-spec-workflows`, optionally `kujo-eval-workflows`, `kujo-cli-contracts`, or `kujo-enterprise-automation` |
| PackWrite agent execution packs, `MEGA_PROMPT.md`, `packwrite.toml`, provider setup, prompt handoff, offline fake-response tests | `kujo-packwrite-workflows`, optionally `kujo-tool-building` or `kujo-cli-contracts` |
| VM/interpreter drift, `--interpreter`, `--runtime dual`, parity matrix | `kujo-runtime-parity` |
| Rust implementation changes in parser/compiler/VM/interpreter/native APIs | `kujo-language-implementation` |
| `kujo docgen`, docs JSON, agent-readable docs, AI task output | `kujo-docgen-agent-readable` |
| Strict maintainer review | `kujo-maintainer-review` |
