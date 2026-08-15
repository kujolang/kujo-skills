---
name: kujo-lens-workflows
description: "Use this skill when setting up, running, interpreting, or maintaining Lens deterministic browser and visual QA workflows: `lens check`, `lens check --quick`, `lens inspect`, `lens flow`, `.lens.toml`, `.lens/runs/`, `lens-report.json`, Agent Repair Briefs, screenshots, accessibility checks, link checks, visual baselines, CI action wiring, RunLedger/Howl output, or Lens source/test changes."
---

# Kujo Lens Workflows

Use Lens as the evidence layer after building or changing a web UI: open the app in a real browser, capture deterministic artifacts, and return a repair-oriented report without LLM or vision-model judgment.

## Agent Workflow

- Prefer Lens after meaningful frontend changes when a local URL is available.
- Start with `lens --help` and `lens --version` if the install is uncertain.
- Ensure the app server is running before Lens; Lens verifies rendered behavior, not server startup.
- Run `lens check <url> --quick` for fast inner-loop diagnosis, then a full default desktop+mobile check before handoff when UI evidence matters.
- Branch on Lens exit codes: `0` pass, `1` findings at or above `--fail-on`, `2` invalid input, `3` browser/provider failure, `4` artifact-write failure.
- Read `.lens/runs/<id>/lens-report.md` for humans and `lens-report.json` for automation. Use the Agent Repair Brief first when fixing failures.
- Treat `.lens/runs/`, screenshots, videos, reports, and baselines as generated artifacts unless the project intentionally commits baselines.

## Setup

```bash
kujo --version
cd /path/to/lens/bridge && npm install && npm run install-browser
cd /path/to/lens && chmod +x lens
```

Lens looks for Kujo at `../kujo/target/debug/kujo` relative to the `lens` wrapper. If the layout differs:

```bash
export KUJO_BIN="/path/to/kujo/target/debug/kujo"
```

## Check Mode

Use `check` for the normal "did the page render and behave sanely?" loop.

```bash
lens check http://localhost:3000 --quick --json
lens check http://localhost:3000 --fail-on error --json
lens check http://localhost:3000 --html --check-links --accessibility
lens check http://localhost:5173 --viewport desktop --viewport mobile
```

Important flags:

- `--check-links`: shallow same-origin link checks only.
- `--quick`: compact one-viewport agent repair profile; use full checks for final evidence.
- `--accessibility` or `--a11y`: axe-core automated accessibility checks.
- `--spec <path>`: deterministic browser assertions from a JSON spec.
- `--baseline`, `--compare-baseline`, `--update-baseline`: visual regression baseline workflow.
- `--perf`: opt-in LCP/CLS/TTFB metrics; treat numbers as environment-relative.
- `--crawl --max-depth <n> --max-pages <n>`: bounded same-origin crawl, not a general crawler.
- `--html`: write a self-contained HTML report.
- `--ledger <path>` and `--howl <path>`: write ecosystem integration outputs.
- `--allow-external`: required for public URLs. Keep this explicit and rare.

Default output:

```text
.lens/runs/<timestamp>/
  lens-report.md
  lens-report.json
  metadata.json
  console.json
  network.json
  dom-summary.json
  screenshots/desktop.png
  screenshots/mobile.png
```

When repairing failures, inspect artifacts named by the finding evidence before guessing root cause. Common finding prefixes are `LENS-PAGELOAD`, `LENS-CONSOLE`, `LENS-NETWORK`, `LENS-BLANK`, `LENS-OVERFLOW`, `LENS-SCREENSHOT`, `LENS-LINKS`, `LENS-A11Y`, `LENS-VISUAL`, and `LENS-PERF`.

## Flow Workflow

Use flows when the task requires proving a user journey, modal, toggle, logged-in path, or other explicit interaction.

```bash
lens inspect http://localhost:3000/account --json
lens flow flows/account.json --validate --json
lens flow flows/account.json --execute --record --walkthrough --out .lens/runs/account
```

Author flows from real selector evidence:

- Run `lens inspect <url> --json`; do not invent selectors.
- Prefer selectors in this order: id, `data-testid`, `aria-label`, input name or placeholder, link `href`, then text.
- Add `safe: true` to every `click`.
- Add `secret: true` to password, token, or credential `type` steps.
- Add assertions after state-changing actions: `wait_for_selector`, `wait_for_text`, `assert_selector`, `assert_not_selector`, `assert_text`, `assert_no_console_errors`, or `assert_no_failed_requests`.
- Cap repair iterations around three loops. Persistent assertion failure is a finding to report, not something to paper over.

Flow safety rules matter: destructive-looking actions require both top-level `allow_destructive: true` and step-level `"destructive": true`; public URLs require `allow_external: true`; recordings can capture rendered sensitive content and should be reviewed before sharing.

## Project Config And CI

Place project defaults in `.lens.toml` when commands become repetitive:

```toml
fail_on       = "warning"
timeout       = 30
viewports     = ["desktop", "mobile"]
check_links   = true
accessibility = true
a11y_tags     = ["wcag2a", "wcag2aa"]
```

Precedence is built-in defaults, then config file, then CLI flags. An explicit missing or malformed `--config <path>` is an input error; an absent implicit `.lens.toml` is ignored.

For GitHub Actions, use Lens `action.yml`: install bridge dependencies, run `./lens check`, and upload `.lens/runs/ci` as the report artifact. CI should branch on the Lens exit code rather than scraping prose.

## Safety And Privacy

- Lens is local-first: `localhost`, `127.0.0.1`, and `::1` are allowed by default; external URLs need `--allow-external`.
- Ordinary `lens check` observes only; it does not click, type, submit forms, log in, or persist browser storage.
- Authenticated checks should use `--auth-file <path>` with a Playwright storage-state file kept out of git.
- Lens never stores request bodies, response bodies, cookies, or auth headers in normal artifacts.
- Redaction is defense-in-depth across captures, findings, reports, Eval output, and the Agent Repair Brief. Still review screenshots and recordings before sharing outside the team.
- Lens is not Lighthouse, Playwright Test, a security scanner, a crawler, or a WCAG certifier. Use it for deterministic browser QA and repair evidence.

## Lens Repo Work

When modifying Lens itself:

- Read in this order: `README.md`, `CONTRIBUTING.md`, `docs/getting-started.md`, `docs/reference.md`, `docs/flow-authoring.md`, `examples/`, then targeted `src/*.kujo` and `bridge/*.js`.
- Use `rg` with exclusions for broad searches: `-g '!/.git/**' -g '!/bridge/node_modules/**' -g '!/docs/assets/**' -g '!/.lens/**'`.
- Preserve invariants: no AI in the check path, localhost-only by default, no unredacted secrets in artifacts or reports, deterministic output, no state mutation outside opted-in flow execution.
- For behavior changes, add tests in `tests/lens_tests.kujo`; if `bridge/*.js` changes, run `node --check bridge/browser-bridge.js` and targeted bridge tests when applicable.
- Run `kujo run tests/lens_tests.kujo` before finishing Lens source changes.
- For performance-sensitive changes, compare `scripts/bench.sh` medians before and after.
- If capture/store/report surfaces change, add redaction coverage and verify with secret-bearing URLs or typed secret flow data.
- Update `README.md`, `docs/getting-started.md`, `docs/reference.md`, `docs/flow-authoring.md`, examples, `src/config.kujo` help text, versions, and `CHANGELOG.md` when user-facing behavior changes.

## Sources Consulted

- Status: repo-backed: Lens `README.md`, `docs/getting-started.md`, `docs/reference.md`, `docs/flow-authoring.md`, `CONTRIBUTING.md`, `action.yml`, `examples/.lens.toml`.
- Status: repo-backed: Lens `lens`, `lens.kujo`, `src/config.kujo`, `src/flow.kujo`, `src/flow_exec.kujo`, `src/visual.kujo`, `src/redact.kujo`.
