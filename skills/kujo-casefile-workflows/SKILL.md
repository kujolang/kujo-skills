---
name: kujo-casefile-workflows
description: "Use this skill when capturing, reviewing, handing off, cleaning, or maintaining Casefile local failure evidence bundles: `casefile.kujo`, `casefile.toml`, `.casefile/`, `capture`, `show latest`, `list`, `doctor`, `clean`, `--from-log`, `--manual`, `--mirror-exit-code`, redaction, path safety, or Casefile CLI/tests/source changes."
---

# Kujo Casefile Workflows

Use Casefile to turn local failures, existing logs, or manual incident notes into structured evidence bundles for debugging, review, and handoff.

## Agent Workflow

- Prefer interpreter mode in the Casefile repo: `kujo run --interpreter casefile.kujo -- <command>`.
- If `KUJO_BIN` is available, use `"$KUJO_BIN" run --interpreter casefile.kujo -- <command>`.
- Start new repos with `init`, `validate`, and often `doctor`.
- Use `capture --name <name> -- <argv...>` for failing commands; prefer argv after `--` over `--command` for complex commands.
- Use `capture --from-log <path> --name <name>` when rerunning is expensive or impossible.
- Use `capture --manual --name <name> --notes <text>` for incident notes or external context.
- Use `capture --mirror-exit-code` in CI when upstream automation must preserve the captured command's failure status.
- Review with `list`, `show latest --format markdown`, and `show latest --format json`.
- Share `case.md`, `case.json`, and `handoff.md` first; read `combined.log`, `reproduction.md`, `git-status.txt`, and `git-diff-stat.txt` when debugging.

## Command Patterns

```bash
export KUJO_BIN="/path/to/kujo/target/debug/kujo"

"$KUJO_BIN" run --interpreter casefile.kujo -- init
"$KUJO_BIN" run --interpreter casefile.kujo -- validate
"$KUJO_BIN" run --interpreter casefile.kujo -- doctor

"$KUJO_BIN" run --interpreter casefile.kujo -- capture --name failing-tests -- false
"$KUJO_BIN" run --interpreter casefile.kujo -- capture --name api-test -- npm test -- --runInBand
"$KUJO_BIN" run --interpreter casefile.kujo -- capture --from-log /tmp/failed-build.log --name ci-log
"$KUJO_BIN" run --interpreter casefile.kujo -- capture --manual --name prod-note --notes "Observed elevated 500 rates after deploy window"

"$KUJO_BIN" run --interpreter casefile.kujo -- list
"$KUJO_BIN" run --interpreter casefile.kujo -- show latest --format markdown
"$KUJO_BIN" run --interpreter casefile.kujo -- show latest --format json
```

Help is available through `help`, `--help`, or `-h`. There is no standalone version command; `--version` is unsupported and should exit `2`.

## Bundle Contract

Default output root is `.casefile/`. Treat it as generated local evidence unless the task explicitly asks to inspect or preserve it.

Each case directory is timestamped and normally contains:

```text
.casefile/<YYYY-MM-DD-HHMMSS-name>/
  case.md
  case.json
  command.txt
  stdout.log
  stderr.log
  combined.log
  git-status.txt
  git-diff-stat.txt
  environment.json
  reproduction.md
  handoff.md
```

Mode-aware captures may omit files that do not apply. Machine consumers should prefer `case.json`; humans and handoff prompts should start with `case.md` and `handoff.md`.

## Safety And Output

- Redaction is enabled by default for common API keys, bearer tokens, password-like assignments, authorization headers, and private-key markers.
- Use `--no-redact` only in trusted local workflows where raw secrets are acceptable in plaintext artifacts.
- Keep `output_dir` inside the repository root. Casefile rejects traversal and prefix-sibling escapes.
- Preview retention with `clean --keep <N> --dry-run` or `clean --older-than <Nd> --dry-run` before deleting.
- `clean` is restricted to the configured output root and should skip unsafe targets.
- Casefile core workflows are local and deterministic; do not add network calls to core command paths.
- Artifacts are plaintext at rest; do not share bundles until notes and logs have been checked for sensitivity.

## Exit Behavior

- Successful command processing exits `0`.
- Argument, config, and usage errors exit `2`.
- Capture execution or artifact write failures exit non-zero, commonly `4`.
- `capture --mirror-exit-code` returns the captured command exit code.
- A failed command captured without `--mirror-exit-code` can still exit `0` after writing evidence.

## Repo Work

- Read in this order before changing Casefile behavior: `README.md`, `AGENTS.md`, `HOWTO.md`, `FLAGS.md`, `SECURITY.md`, `CONTRIBUTING.md`, `casefile.kujo`, `tests/casefile_cli_test_v2.kujo`.
- Treat `FLAGS.md` as the authoritative command and flag surface.
- Treat `README.md` and `HOWTO.md` as the canonical copyable examples.
- Treat `tests/` as CLI contract coverage, not the first source for user-facing examples.
- Preserve redaction-by-default, path safety, guarded cleanup, deterministic local execution, and structured `case.json`.
- When changing command surface or semantics, update `README.md`, `FLAGS.md`, `HOWTO.md`, and `SECURITY.md` if the trust boundary or risk model changes.
- Use broad searches with generated paths excluded:

```bash
rg --files -g '!target/**' -g '!.casefile/**' -g '!node_modules/**' -g '!vendor/**'
```

## Validation

```bash
export KUJO_BIN="/path/to/kujo/target/debug/kujo"
"$KUJO_BIN" run --interpreter casefile.kujo -- help
"$KUJO_BIN" run --interpreter casefile.kujo -- init
"$KUJO_BIN" run --interpreter casefile.kujo -- validate
"$KUJO_BIN" test-run -v tests/casefile_cli_test_v2.kujo
```

Use isolated temp directories for capture behavior tests so generated `.casefile/` output does not pollute the repository.

## Sources Consulted

- Status: repo-backed: `README.md`, `AGENTS.md`, `HOWTO.md`, `FLAGS.md`, `SECURITY.md`, `CONTRIBUTING.md`.
- Status: repo-backed: `casefile.kujo`, `tests/casefile_cli_test_v2.kujo`.
