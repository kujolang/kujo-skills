---
name: kujo-rag-workflows
description: "Use this skill when setting up, running, extending, testing, or maintaining the Kujo RAG Starter Kit: `kujo run main.kujo --interpreter ingest|query|serve|demo|bootstrap`, local/offline RAG indexes, namespace isolation, parser/chunking/embedding/retrieval changes, API ingest/query endpoints, OpenAPI/SDK parity, release-evaluation gates, large-corpus benchmarks, index maintenance, bootstrap templates, or RAG security/operations docs."
---

# Kujo RAG Workflows

Use Kujo RAG for local-first retrieval-augmented generation over docs, source, and mixed corpora. Default to offline hash embeddings and local JSON indexes unless the task explicitly targets AI providers or remote vector backends.

## Running RAG

Run from the RAG repo root. Stable CLI commands use interpreter mode:

```bash
cp .env.example .env
kujo run main.kujo --interpreter ingest --path ./examples/kujo_docs --recursive true
kujo run main.kujo --interpreter query --question "How does Kujo handle module imports?"
kujo run main.kujo --interpreter serve --host 127.0.0.1 --port 8787
kujo run main.kujo --interpreter demo
kujo run main.kujo --interpreter bootstrap --target ./results/bootstrap_repo
```

Use namespaces for tenant/project isolation:

```bash
kujo run main.kujo --interpreter ingest --path ./docs --recursive true --namespace team_a
kujo run main.kujo --interpreter query --question "What changed?" --namespace team_a
```

If multiple Kujo binaries may exist, set `KUJO_BIN=/absolute/path/to/kujo`. Use the execution bridge when the task specifically asks for non-interpreter preference with fallback:

```bash
KUJO_BIN=/absolute/path/to/kujo kujo run scripts/run_main_auto.kujo --interpreter query --question "What is Kujo optimized for?"
```

`help`, `--help`, and `--version` render the same help text in this repo; do not expect a separate version banner.

## Adoption Recipes

For documentation corpora:

```bash
export KUJO_RAG_INGEST_EXTENSIONS=md,markdown,txt
export KUJO_RAG_CHUNK_STRATEGY=line
kujo run main.kujo --interpreter ingest --path ./docs --recursive true
```

For code repositories:

```bash
export KUJO_RAG_INGEST_EXTENSIONS=kujo,md,txt
export KUJO_RAG_CHUNK_STRATEGY=fixed
export KUJO_RAG_CHUNK_SIZE=1100
export KUJO_RAG_CHUNK_OVERLAP=180
kujo run main.kujo --interpreter ingest --path ./src --recursive true
```

For mixed workspaces:

```bash
export KUJO_RAG_INGEST_EXTENSIONS=md,markdown,txt,kujo,pdf
export KUJO_RAG_CHUNK_STRATEGY=line
export KUJO_RAG_TOP_K=8
kujo run main.kujo --interpreter ingest --path ./knowledge --recursive true
```

API smoke path:

```bash
kujo run main.kujo --interpreter serve --host 127.0.0.1 --port 8787
curl -s http://127.0.0.1:8787/health
curl -s -X POST http://127.0.0.1:8787/query -H "Content-Type: application/json" -d '{"query":"What is Kujo optimized for?","namespace":"default"}'
```

`/ingest` and `/ingest/jobs` are scoped by `KUJO_RAG_API_INGEST_ALLOWED_ROOTS`; rejected paths return `ingest_path_forbidden`.

## Repo Work

Read in this order before changing behavior:

1. `README.md`
2. `main.kujo`
3. `.env.example`
4. The affected module under `src/`
5. `docs/adoption-playbook.md` for external adoption or setup work
6. `docs/extension-guide.md` for parser/provider/retrieval extensions
7. `docs/agent-implementation-checklist.md` when working checklist items
8. `docs/release-process.md` when changing release gates, artifacts, versioning, or rollback behavior

Primary modules:

- CLI/config: `main.kujo`, `src/cli_args.kujo`, `src/config.kujo`, `src/env_loader.kujo`.
- Ingestion/parsing/chunking: `src/ingestion.kujo`, `src/parsers.kujo`, `src/chunking.kujo`.
- Retrieval/indexing: `src/embeddings.kujo`, `src/vector_store.kujo`, `src/vector_backend.kujo`, `src/retrieval.kujo`, `src/rag_engine.kujo`.
- API/ops: `src/query_api.kujo`, `src/privacy_workflows.kujo`, `src/retention_policy.kujo`, `src/audit_log.kujo`.
- Release/evaluation: `src/release_eval.kujo`, `scripts/run_*.kujo`, `config/*.json`, `openapi/`, `sdk/javascript/`.

## Extension Points

Parser and embedding selection are registry-based:

- Parser registry: `get_parser_registry()` in `src/parsers.kujo`.
- Embedding provider registry: `get_embedding_provider_registry()` in `src/embeddings.kujo`.

To add a parser or provider:

1. Add the implementation function.
2. Register it in the registry map.
3. Preserve fallback behavior: text parser fallback and hash embedding fallback.
4. Add registry, fallback, and behavior tests.
5. Update `README.md` and `docs/extension-guide.md` if public behavior changes.

For retrieval changes in `src/retrieval.kujo`, keep deterministic tie ordering, preserve existing query response fields, and test filter/ranking interactions. Generated SDK files are contract outputs; regenerate through the OpenAPI contract workflow instead of hand-editing `sdk/javascript/kujo-rag-client.generated.js`.

## Validation

Use focused tests first, then wider gates:

```bash
kujo run tests/test_unit.kujo --interpreter
kujo run tests/test_integration.kujo --interpreter
KUJO_BIN=/absolute/path/to/kujo kujo run scripts/run_tests.kujo --interpreter
```

Use targeted subsets through the wrapper:

```bash
KUJO_RAG_TEST_FILES=tests/test_api_contract.kujo,tests/test_security.kujo kujo run scripts/run_tests.kujo --interpreter
```

Run specialized gates when the touched surface requires them:

```bash
kujo run scripts/run_release_evaluation.kujo --interpreter
kujo run scripts/run_openapi_contract_review.kujo --interpreter
KUJO_RAG_OPENAPI_REGENERATE=true kujo run scripts/run_openapi_contract_review.kujo --interpreter
kujo run scripts/run_chunking_preset_ab_evaluation.kujo --interpreter
kujo run scripts/run_large_corpus_benchmarks.kujo --interpreter
kujo run scripts/maintain_index.kujo --interpreter
```

For release work, also run the relevant gates in `docs/release-process.md`, including release artifacts, supply-chain scan, canary replay, AI drift, multilingual eval, architecture fitness, config schema, chaos, performance/cost, and readiness scorecard checks as applicable.

## Operations and Safety

- Keep offline-first behavior intact by default: `KUJO_RAG_EMBEDDING_PROVIDER=hash`, `KUJO_RAG_VECTOR_BACKEND=local_json`.
- Enable strict production checks with `KUJO_RAG_STRICT_CONFIG=true` or `KUJO_RAG_ENV=production`; production strict mode requires non-default namespace, bearer auth, non-default index path, and at-rest encryption key configuration.
- Treat auth, RBAC, audit logging, redaction, rate limiting, abuse controls, CORS, TLS reverse proxy guidance, and ingest path scoping as security surfaces. Update docs and tests with behavior changes.
- Preserve PDF parser safety constraints: `KUJO_RAG_PDF_EXTRACTOR` must be a single safe binary/path token, file paths must be quoted, and parser timeout/sandbox byte budgets must produce deterministic fallback metadata.
- Use `KUJO_RAG_INDEX_MAINTENANCE_MODE=report` before apply mode; apply mode must pass before/after probe correctness and latency-regression checks.

## Search Hygiene

Start broad searches with canonical surfaces:

```bash
rg <pattern> README.md main.kujo src docs/adoption-playbook.md docs/extension-guide.md examples/kujo_docs tests scripts \
  -g '!data/**' \
  -g '!results/**' \
  -g '!sdk/**' \
  -g '!openapi/**' \
  -g '!config/*.json' \
  -g '!compatibility/**'
```

Treat `tests/`, evaluation corpora, malformed parser corpora, `config/*.json`, `openapi/`, and `sdk/` as contracts or generated outputs unless the task explicitly targets them. Runtime outputs live under ignored `data/` and `results/`.

## Sources Consulted

- Status: repo-backed: `README.md`, `main.kujo`, `.env.example`.
- Status: repo-backed: `docs/adoption-playbook.md`, `docs/extension-guide.md`, `docs/agent-implementation-checklist.md`, `docs/release-process.md`.
- Status: repo-backed: `scripts/run_tests.kujo`, `src/*`, `tests/*`, `config/*`, `openapi/kujo-rag-openapi.json`.
