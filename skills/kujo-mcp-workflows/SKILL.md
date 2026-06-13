---
name: kujo-mcp-workflows
description: "Use this skill when generating, running, validating, deploying, or maintaining Kujo MCP servers and repo-specific MCP scaffolds: `mcp make`, `kujo run mcp.kujo --interpreter make`, `mcp-server.json`, MCP tool/resource registries, generated `.mcp/` outputs, `mcp.manifest.json`, repo profiles, MCP safety tiers, auth/host/request guardrails, endpoint tests, or MCP source/test changes."
---

# Kujo MCP Workflows

Use the MCP framework to build guarded Model Context Protocol servers in Kujo, or to generate a repo-specific MCP server and review packet with `mcp make`.

## Agent Workflow

- Classify the request first: local demo server, generated repo server, framework/source change, generated artifact review, or deployment hardening.
- Prefer the current reliable invocation for generation: `kujo run mcp.kujo --interpreter make <repo-path>`. The intended future `kujo mcp make <repo-path>` shape is not the dependable path yet.
- Treat generated `.mcp/` outputs as reviewable scaffolds, not magic truth. Inspect `repo-profile.json`, `mcp.manifest.json`, and `artifacts/safety-review.md` before recommending exposure.
- Keep MCP server capabilities least-privilege: read-only tools and allowlisted safe commands by default; review-required and blocked capabilities stay disabled unless explicitly justified.
- Run focused tests after narrow edits and `bash tests/run_all_tests.sh` after security, config, endpoint, generation, or registry changes.

## Repo Orientation

When working in the MCP repo, read in this order:

1. `README.md`
2. `docs/mcp-reference.md`
3. `docs/mcp-make.md`
4. `docs/security-model.md`
5. The task-specific source files under `src/`
6. The matching `tests/*.sh` or `tests/*.kujo`

For framework source changes, important entry points are:

- `server.kujo`: demo server entry point.
- `mcp.kujo`: thin compatibility wrapper and `make` dispatch.
- `src/core/framework.kujo`: schema helpers, path guards, safe read/write helpers, JSON responses.
- `src/tools/registry.kujo`: demo tool metadata and handlers.
- `src/resources/registry.kujo`: resource metadata and readers.
- `src/commands/make.kujo`: `mcp make` CLI argument parsing and orchestration.
- `src/make/*.kujo`: repo analysis, generated server writing, manifest schemas, validation, artifacts, enrichment.

Use search exclusions for generated outputs unless the task targets them:

```bash
rg "term" --glob '!.mcp/**' --glob '!demo/**/.mcp/**'
```

## Local Server

Start the demo server from the MCP repo:

```bash
bash scripts/run_server.sh
```

Default endpoint:

```text
http://127.0.0.1:8931/mcp/v1
```

Expected health shape:

```json
{"status":"ok","server":"mcp-demo","version":"0.1.0"}
```

Endpoint contracts:

- `GET /health`
- `POST /tools/list`
- `POST /tools/call`
- `POST /resources/list`
- `POST /resources/read`
- `GET /logs`

Demo tools live in `src/tools/registry.kujo`: `read_project_docs`, `search_files`, `generate_summary`, `write_safe_patch`, `read_text_range`, `write_text_safe`, `list_tree_recursive`, and `grep_text`.

Demo resources live in `src/resources/registry.kujo`: `project://docs`, `files://tree`, `log://calls`, `prompt://onboarding`, and `workflow://checklist-loop`.

## Generate Repo-Specific Servers

Use `mcp make` to analyze a local repo and create a safe scaffold plus review artifacts:

```bash
kujo run mcp.kujo --interpreter make <repo-path>
```

Common options:

```bash
kujo run mcp.kujo --interpreter make <repo-path> --out <generated-server-dir>
kujo run mcp.kujo --interpreter make <repo-path> --artifacts <artifacts-dir>
kujo run mcp.kujo --interpreter make <repo-path> --profile-only
kujo run mcp.kujo --interpreter make <repo-path> --artifacts-only
kujo run mcp.kujo --interpreter make <repo-path> --no-ai
kujo run mcp.kujo --interpreter make <repo-path> --validate
kujo run mcp.kujo --interpreter make <repo-path> --dry-run
```

Use `--dry-run` to preview paths and classification without writes. Use `--no-ai` when deterministic offline output is required or AI enrichment is unavailable. Use `--validate` when the generated server needs self-check coverage in the artifact report.

Default output layout:

```text
<repo>/
  .mcp/
    generated-server/
      README.md
      repo-profile.json
      mcp.manifest.json
      mcp-server.json
      src/
      tests/
      examples/
    artifacts/
      README.md
      repo-map.md
      mcp-surface-plan.md
      safety-review.md
      validation-report.md
      fix-backlog.md
      fix-backlog.json
      agent-handoff.md
      patchbrief.md
      shipcheck.md
      howto.md
      mcp-findings.md
      mcp-findings.json
```

Review generated outputs in this order:

1. `artifacts/safety-review.md`
2. `mcp.manifest.json`
3. `repo-profile.json`
4. `artifacts/validation-report.md`
5. `artifacts/fix-backlog.md`
6. `artifacts/agent-handoff.md`

Generated manifests must keep tools, resources, prompts, `safe_command_map`, and `blocked_commands` consistent. Safety tiers are `read_only`, `safe_command`, `write_scaffold`, `review_required`, and `blocked`.

## Source Change Rules

- Keep `mcp.kujo` thin; put real implementation in `src/`.
- Keep tool metadata and handlers centralized in `src/tools/registry.kujo`.
- Keep resources centralized in `src/resources/registry.kujo`.
- Preserve schema discoverability through `tools/list`.
- Return deterministic, field-specific validation errors for malformed tool arguments.
- Keep path operations inside `permissions.allowed_directories`; reject traversal, absolute paths where inappropriate, sibling-prefix bypasses, read-only patterns, and oversized payloads.
- Do not expose arbitrary shell input. Generated safe command tools must come from allowlisted, fixed commands.
- Report sensitive files by path only; never copy secret values into generated artifacts.
- Treat `mcp make --help` and `mcp make --version` as unsupported wrapper gaps unless source docs/tests have changed.

## Deployment Hardening

For remote deployments:

- Start from `mcp-server.production.example.json`.
- Store `auth.token` outside source control and keep `auth.enabled` true.
- Bind the Kujo process to an internal/private interface.
- Terminate TLS at a reverse proxy or ingress.
- Keep `http.max_request_body_bytes`, `http.rate_limit_enabled`, and `http.rate_limit_per_minute` bounded.
- Use gateway or load-balancer throttling for multi-instance deployments because the built-in limiter is process-local.
- Keep `permissions.allowed_directories` narrow and `read_only_patterns` deny-first.

## Verification

For MCP repo changes:

```bash
bash tests/run_all_tests.sh
```

For security-sensitive edits:

```bash
bash tests/test_02_security_regression_suite.sh
```

For endpoint behavior:

```bash
bash tests/test_03_endpoint_integration.sh
```

For `mcp make` changes:

```bash
bash tests/feat_06_mcp_make.sh
```

For generated server review, prefer:

```bash
kujo run mcp.kujo --interpreter make <repo-path> --validate --no-ai
```

If `kujo` is not on `PATH`, resolve the runtime from the MCP repo:

```bash
bash scripts/find_kujo_runtime.sh
```

## Sources Consulted

- Status: repo-backed: MCP `README.md`, `docs/mcp-reference.md`, `docs/mcp-make.md`.
- Status: repo-backed: `docs/security-model.md`, `docs/production-deployment.md`.
- Status: repo-backed: `mcp.kujo`, `src/commands/make.kujo`, `src/tools/registry.kujo`, `src/resources/registry.kujo`, `tests/run_all_tests.sh`.
