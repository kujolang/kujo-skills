---
name: kujo-fence-workflows
description: "Use this skill when setting up, running, interpreting, integrating, or maintaining Fence architecture-boundary checks for Kujo ecosystem repositories: `fence.kujo`, `fence.toml`, `fence-baseline.json`, `init`, `validate`, `check`, `explain`, `graph`, `baseline create`, `--changed-only`, `--baseline`, JSON/Markdown/SARIF reports, CI gates, zone rules, import-boundary violations, or Fence CLI/source/test changes."
---

# Kujo Fence Workflows

Use Fence as a deterministic architecture-boundary guardrail: encode allowed dependencies in `fence.toml`, scan imports, and fail only on violations at the configured threshold.

## Agent Workflow

- Default to the local Fence repo unless the user points elsewhere: `/Users/robertdevore/2026/Kujolang/kujo-repos/fence`.
- Use `KUJO_BIN` when available; otherwise try `kujo` on `PATH`.
- Run Fence from inside the target repository being checked. Module imports resolve relative to `fence.kujo`, but source scanning uses the current working directory.
- Start new repos with `init`, edit `fence.toml`, then run `validate` and `check`.
- Before implementation work in a fenced repo, run `graph` and `check` to learn the allowed dependency direction and current violations.
- During implementation, do not import across denied boundaries and do not weaken `fence.toml` just to hide a violation.
- After implementation, run `check`; include the Fence result and any report path in the handoff.
- Use `explain <path>` when a file is classified unexpectedly or a violation needs root-cause analysis.

## Command Patterns

```bash
FENCE_REPO="${FENCE_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/fence}"
KUJO_BIN="${KUJO_BIN:-kujo}"
cd /path/to/project

"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- init
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- validate
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- check
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- explain src/ui/LoginForm.tsx
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- graph --format mermaid --output architecture.mmd
```

Common check forms:

```bash
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- check --format json
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- check --format markdown --output FENCE_REPORT.md
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- check --format sarif --output fence.sarif
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- check --changed-only --base origin/main --fail-on error
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- check --baseline --fail-on error
"$KUJO_BIN" run "$FENCE_REPO/fence.kujo" -- check --quiet
```

Templates for `init --template <name>` are `layered`, `cli`, `web-app`, `hexagonal`, `mvc`, and `feature-sliced`.

## Config Guidance

- Fence reads `fence.toml` at the target repo root, with `fence.json` accepted as a fallback.
- Core top-level keys are `version`, `source_roots`, `default_severity`, `fail_on`, and `unknown_dependency_policy`.
- `[scan]` controls include/exclude globs; always exclude generated trees such as `node_modules/**`, `dist/**`, `build/**`, and generated files where applicable.
- `[aliases]` maps import prefixes such as `"@" = "src"`.
- `[external]` and zone-level `external_allow` / `external_deny` govern third-party packages.
- `[zones.<name>]` defines `paths`, `can_depend_on`, `cannot_depend_on`, and optional `severity`.
- Explicit deny wins: same-zone imports are allowed, `cannot_depend_on` blocks, `can_depend_on` allows, and unmapped targets follow `unknown_dependency_policy`.
- Prefer tightening `paths` and zone definitions over adding broad allows.

## Violation And Adoption Workflow

- For one surprising violation, run `explain <file>` and inspect the matched zone, resolved import, and rule source.
- For legacy repos with existing violations, run `baseline create`, commit `fence-baseline.json`, then gate with `check --baseline`.
- Treat `FENCE_REPORT.md`, `fence.sarif`, and other report outputs as generated unless the task explicitly asks to commit them.
- Commit `fence.toml` and, for gradual adoption, `fence-baseline.json`.
- Machine consumers should prefer `--format json` or SARIF; human PR handoffs should prefer Markdown.

## Exit Behavior

- `0`: success, no violations at or above the threshold.
- `1`: violations at or above `fail_on`.
- `2`: invalid usage or invalid config.
- `3`: parse/config error.
- `4`: runtime error.
- `5`: IO failure.
- `6`: internal failure.

## Fence Repo Work

When modifying Fence itself, read in this order:

1. `README.md`
2. `docs/getting-started.md`
3. `docs/commands.md`
4. `docs/configuration.md`
5. `docs/ci.md`
6. `docs/architecture.md`
7. `CONTRIBUTING.md`
8. Targeted `src/*.kujo`, `fence.kujo`, and `tests/fence_tests.kujo`

Preserve these contracts unless the user explicitly asks to change them:

- Commands: `init`, `check`, `explain`, `graph`, `baseline create`, `validate`, `doctor`, `help`, `version`.
- Output formats: human, JSON, Markdown, SARIF for `check`; human, JSON, DOT, Mermaid for `graph`.
- Deterministic, local-first behavior with no network calls.
- Path-safe `--output` handling and safe `--changed-only --base` validation.
- Best-effort line-based import detection across Kujo, JS/TS, Python, Rust, PHP, and Go.
- Config validation for missing zones, undefined zone refs, allow/deny conflicts, pathless zones, overlapping paths, dependency cycles, and unsupported versions.

Use broad searches with generated and historical paths excluded:

```bash
rg "pattern" README.md docs src tests fence.kujo \
  -g '!agent/**' -g '!MEGA_PROMPT.md' -g '!tests/fixtures/**' \
  -g '!FENCE_REPORT.md' -g '!fence-baseline.json' -g '!*.sarif'
```

Kujo VM constraints matter in Fence source: keep call chains shallow, prefer `while` loops, avoid duplicate `let` names across branches, use `from src.x import name`, use `dict_has` / `truthy`, and keep tree walks iterative.

## Validation

For Fence source changes:

```bash
cd /Users/robertdevore/2026/Kujolang/kujo-repos/fence
"${KUJO_BIN:-kujo}" check src/<file>.kujo
"${KUJO_BIN:-kujo}" run tests/fence_tests.kujo
```

Smoke-test behavior against a temp repo when command behavior, config templates, resolution, output formats, or path safety changes:

```bash
TMP="$(mktemp -d)"
cp -r tests/fixtures/sample/src "$TMP"/
cd "$TMP"
"${KUJO_BIN:-kujo}" run /Users/robertdevore/2026/Kujolang/kujo-repos/fence/fence.kujo -- init
"${KUJO_BIN:-kujo}" run /Users/robertdevore/2026/Kujolang/kujo-repos/fence/fence.kujo -- check --format json
```

## Sources Consulted

- Status: repo-backed: Fence `README.md`, `docs/getting-started.md`, `docs/commands.md`, `docs/configuration.md`, `docs/ci.md`, `docs/architecture.md`, `CONTRIBUTING.md`.
- Status: repo-backed: `fence.kujo`, `src/*.kujo`, `tests/fence_tests.kujo`.
