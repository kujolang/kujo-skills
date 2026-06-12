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
| VM/interpreter drift, `--interpreter`, `--runtime dual`, parity matrix | `kujo-runtime-parity` |
| Rust implementation changes in parser/compiler/VM/interpreter/native APIs | `kujo-language-implementation` |
| `kujo docgen`, docs JSON, agent-readable docs, AI task output | `kujo-docgen-agent-readable` |
| Strict maintainer review | `kujo-maintainer-review` |

