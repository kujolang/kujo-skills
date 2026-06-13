---
name: kujo-spec-workflows
description: "Use this skill when creating, validating, exporting, reviewing, or maintaining Kujo Spec task contracts: `.spec.yml`, `.spec.yaml`, `.spec.toml`, `.spec.json`, `spec init`, `validate`, `render`, `export`, `export-agent-context`, `export-eval`, `ci`, `list`, `search`, `status`, `template`, `graph`, safe-write/template-source policy, Spec schema changes, or Spec CLI/tests/source changes."
---

# Kujo Spec Workflows

Use Spec to turn task intent into a reviewable contract before implementation:
goal, scope, acceptance criteria, eval requirements, risks, dependencies,
review expectations, and human approval points.

Canonical local source is usually
`/Users/robertdevore/2026/Kujolang/kujo-repos/spec`. Do not confuse Spec with
neighboring Kujo tools such as Eval, Dispatch, Scout, Muzzle, RunLedger, or
ChangeBucket. Spec defines task contracts and can export work for those tools;
it does not execute evals, run quiet workflows, or record agent receipts.

## Agent Workflow

1. Verify the wrapper, runtime, and version:

```bash
export PATH="/path/to/spec/scripts:$PATH"
spec doctor
spec version
spec version --json
```

If `KUJO_BIN` is unset or points to Python's unrelated `kujo` linter, set it to
the Kujo language runtime. The wrapper also accepts the default `kujo` on
`PATH`.

2. Create or update specs under a project `specs/` directory:

```bash
spec init --name "add-dark-mode" --output specs/dark-mode.spec.yml
spec init --from template:feature --output specs/feature.spec.yml
spec init --from github:OWNER/REPO/123 --output specs/issue-123.spec.yml
```

Prefer YAML (`.spec.yml`) for human-authored specs. Use `.spec.json` for
machine-generated or interchange files. Use `.spec.toml` only for simple flat
specs.

3. Validate before implementation or handoff:

```bash
spec validate specs/dark-mode.spec.yml
spec validate specs/dark-mode.spec.yml --strict --json
spec ci specs --format json --max-files 500 --jobs 4 --strict
```

Validation requires `name` and `goal`. Treat acceptance criteria as the
definition of done; use `eval_requirements` only for checks that can be mapped
to deterministic Eval checks.

4. Render or export for the next actor:

```bash
spec render specs/dark-mode.spec.yml --output docs/specs/dark-mode.md
spec export-agent-context specs/dark-mode.spec.yml --output /tmp/agent-context.txt
spec export specs/dark-mode.spec.yml --format envelope --payload-format dispatch \
  --output artifacts/dark-mode.envelope.json
spec export-eval specs/dark-mode.spec.yml --output eval_suite.json
```

Use `export-agent-context` for coding agents, `export --format dispatch` or
`--format envelope --payload-format dispatch` for automation, and
`export-eval` when Spec's `eval_requirements` should become a Kujo Eval suite.

5. Keep lifecycle metadata current when specs are used as a queue:

```bash
spec list specs --json
spec search --priority high --tag security
spec status specs/dark-mode.spec.yml --set ready
spec status --filter review
spec graph specs --format mermaid
```

## Spec Shape

Minimum valid YAML:

```yaml
name: "Add dark mode"
goal: "Add a theme toggle and persist the selected color scheme."
priority: "medium"
acceptance_criteria:
  - "Users can switch between light and dark themes"
  - "The selected theme persists after reload"
```

Common optional fields: `version`, `background`, `scope`, `non_goals`,
`relevant_systems`, `likely_files`, `acceptance_criteria`,
`eval_requirements`, `risks`, `dependencies`, `review_expectations`,
`human_approval_points`, `estimated_effort`, `priority`, `assignee`, `tags`,
`status`, `id`, `created_at`, and `parent_id`.

Known Eval check types include `command_succeeds`, `command_output_contains`,
`file_exists`, `file_contains`, `json_path_value`, `snapshot_matches`,
`regex_matches`, `command_timing_less_than`, `http_status`,
`markdown_contains_section`, `exit_code`, `stdout_contains`, and
`artifact_exists`.

## Layout And Policy

- Prefer `specs/` at project root for small projects.
- In monorepos, colocate specs with the bounded context: `services/api/specs/`,
  `packages/web/specs/`, or similar.
- Spec discovery uses double extensions: `.spec.yml`, `.spec.yaml`,
  `.spec.toml`, and `.spec.json`.
- `spec list` scans up to three levels by default; use `--max-depth` for deeper
  trees.
- Store templates under `specs/templates/` and use
  `spec init --from template:<name>`.
- In regulated or CI environments, set `SPEC_SAFE_WRITE=on` and
  `SPEC_TEMPLATE_SOURCE_POLICY=project-only`.
- Use `--unsafe-write` only for approved output paths outside the project root.
- Use `--strict-template-source` when a single command must ignore home
  templates.

## Output And Exit Contracts

- Exit `0`: success.
- Exit `1`: validation failure, operational failure, or usage error.
- `spec version --json` emits `version`, `contract`, and `schema_version`.
- `spec validate --json` emits `valid`, `errors`, and `warnings`.
- `spec list --json` emits objects with at least `file`, `name`, `priority`,
  and `status`.
- `spec ci --format json` emits `total`, `passed`, `failed`, and `failures`.
- `spec ci --format github` emits GitHub Actions annotations.
- `spec export --format envelope` emits `metadata` plus `payload`; metadata
  includes `source_file`, `schema_version`, `checksum_sha256`, `generated_at`,
  and `payload_format`.

Preserve exact JSON field names and stdout/stderr behavior unless the task
explicitly changes a contract. Regenerate `docs/COMMAND_INVENTORY.md` after
command-surface changes.

## Limits And Safety

- Spec processing is local and needs no API keys.
- `spec init --from github:OWNER/REPO/NUMBER` requires the `gh` CLI and network
  access.
- Spec files larger than 1MB are rejected before parsing.
- Paths using `..`, paths outside the current project, and symlink escapes are
  rejected for reads.
- YAML supports the documented subset; avoid anchors, tags, multi-document YAML,
  and complex features.
- TOML support is basic `key = value`; avoid nested tables and arrays of tables.
- Safe-write mode restricts output paths to the current project root unless
  `--unsafe-write` is passed.

## Maintaining Spec

Source map:

- `scripts/spec`: Bash CLI wrapper, routing, path safety, JSON contracts,
  safe-write policy, conversion orchestration.
- `scripts/commands/maintenance.sh`: `ci`, `template`, `doctor`, `changelog`,
  `graph`, and related operational commands.
- `src/common.kujo`: shared helpers and defaults.
- `src/validate.kujo`: schema validation and warning/error logic.
- `src/render.kujo`: Markdown rendering.
- `src/export.kujo`: agent, dispatch, markdown, eval, and envelope exports.
- `src/convert.kujo`: YAML/TOML/JSON conversion bridge.
- `schema/spec.schema.json`: task-contract schema.
- `fixtures/` and `examples/`: stable validation and example inputs.
- `docs/COMMAND_INVENTORY.md`: generated command inventory.
- `completions/spec.{bash,zsh,fish}`: shell completion surfaces.

Read in this order for repo work: `README.md`, `docs/API_REFERENCE.md`,
`docs/COMMAND_INVENTORY.md`, `docs/ARCHITECTURE.md`,
`docs/INTEGRATION_GUIDE.md`, `docs/ENTERPRISE_USAGE_GUIDE.md`,
`scripts/spec`, `src/*.kujo`, and focused tests.

Validate changes with:

```bash
bash tests/run_tests.sh
bash tests/benchmark.sh
bash scripts/verify_docs_command_parity.sh
bash scripts/verify_completion_parity.sh
bash scripts/verify_test_runtime_parity.sh
bash scripts/release_quality_gates.sh
bash scripts/supply_chain_policy_check.sh
```

For CLI output, JSON contract, path safety, safe-write, template-source, or
completion changes, add or update focused checks in `tests/run_tests.sh` and
regenerate generated docs/completions as appropriate.
