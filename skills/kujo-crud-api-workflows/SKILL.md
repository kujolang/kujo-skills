---
name: kujo-crud-api-workflows
description: "Use this skill when running, testing, extending, or maintaining the CRUD API showcase: `main.kujo`, SQLite item/project APIs, Next.js playground, auth strategies, smoke tests, frontend lint/build, DR/performance drills, API contracts, release checklist, or `crud-api` source/docs changes."
---

# Kujo CRUD API Workflows

Use CRUD API as the compact Kujo + SQLite server-first showcase with a minimal Next.js playground and contract-tested item/project workflows.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
CRUD_API_REPO="${CRUD_API_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/crud-api}"
cd "${CRUD_API_REPO}"
KUJO_BIN=/path/to/kujo
"$KUJO_BIN" run main.kujo --interpreter
# default API: http://127.0.0.1:4100
curl -s http://127.0.0.1:4100/health
```

## Workflow Notes

- Backend starts from `main.kujo`; frontend playground lives under `frontend/`.
- API write auth, request validation, and concurrency behavior are contract surfaces.
- Generated DB files, frontend build output, and smoke artifacts should stay out of commits unless explicitly requested.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo CRUD API Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `main.kujo`
3. `src/handlers.kujo`
4. `src/auth.kujo`
5. `src/db.kujo`
6. `src/validation.kujo`
7. `frontend/`
8. `tests/`
9. `scripts/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
make test KUJO_BIN=/path/to/kujo
KUJO_BIN=/path/to/kujo ./scripts/run-smoke-tests.sh
./scripts/quality-check.sh
cd frontend && npm run lint
cd frontend && npm run build
```

## Search And Safety

- Default server binds to `127.0.0.1`; preserve reviewed local showcase defaults.
- Do not mix CMS behavior into this smaller CRUD API surface.
- Keep cURL examples, tests, and API contract docs in sync.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `main.kujo`.
- Status: repo-backed: `frontend/package.json`.
- Status: repo-backed: `src/handlers.kujo`.
