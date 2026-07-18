---
name: kujo-ai-chat-workflows
description: "Use this skill when running, configuring, testing, extending, or maintaining the AI Chat local multi-provider chat app: `npm run dev`, `npm run smoke`, SQLite chat state, provider profiles, encrypted API keys, SSE streaming, transcription, `bridge_chat.kujo`, HTTP/API contracts, smoke tests, or `ai-chat` source/docs changes."
---

# Kujo AI Chat Workflows

Use AI Chat as the local showcase app for provider-gated chat workflows, durable SQLite state, multi-pane comparisons, provider-neutral tool execution, Watchdog-routed providers, benchmark panes, SSE streaming, and offline fixture smoke paths.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
AI_CHAT_REPO="${AI_CHAT_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/ai-chat}"
cd "${AI_CHAT_REPO}"
npm install
ENCRYPTION_SECRET=replace_with_strong_secret API_AUTH_TOKEN=replace_with_strong_token KUJO_BIN=/absolute/path/to/kujo AI_SDK_PATH=/path/to/ai-sdk/src AI_CHAT_HOST=127.0.0.1 PORT=4173 npm run dev
# open http://127.0.0.1:4173
```

## Workflow Notes

- Runtime database, browser artifacts, benchmark runs, and backup outputs live under configured data paths; do not commit runtime data.
- `/api/chat/stream` emits SSE `token`, `thinking`, `done`, and `error` events. Preserve complete upstream text/thinking streams plus final metadata and usage detail payloads when changing bridge or route plumbing.
- Provider profiles now include managed Watchdog paths for OpenRouter and Ollama TUD, pane profiles for repeated comparisons, and a benchmark runner that creates one chat per test under `data/benchmark-runs/`.
- Provider-neutral tools include `web_search` plus Playwright-backed `browser_open`, `browser_snapshot`, `browser_act`, and `browser_close`; `browser_use` remains a compatibility adapter and screenshot results are authenticated chat artifacts.
- Browser tools are isolated per chat/pane scope, default read-only, reject private/local/cloud-metadata targets unless explicitly allowed for local testing, and require `BROWSER_ENABLED=1` plus Playwright Chromium.
- Offline fixture smoke is the safest provider-free validation path.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo AI Chat Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `SETUP_AND_INSTALL.md`
4. `.env.example`
5. `bridge_chat.kujo`
6. `docs/API_CONTRACT.md`
7. `server.js`
8. `lib/tool-runtime.js` and browser runtime modules when tool execution changes
9. `tests/`
10. `scripts/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
npm test
API_AUTH_TOKEN=replace_with_strong_token PORT=4173 npm run smoke
BROWSER_ENABLED=1 API_AUTH_TOKEN=replace_with_strong_token PORT=4173 npm run smoke:browser
API_AUTH_TOKEN=replace_with_strong_token npm run benchmark:run -- --tests /path/to/benchmark.md --pane-profile "OpenRouter (TUD)"
npm run db:backup
npm run db:vacuum
```

## Search And Safety

- Exclude `node_modules/`, `data/`, and lockfile bulk from broad readability sweeps unless targeted.
- Never print or commit real provider keys, Watchdog token files, encrypted secrets, session tokens, browser screenshots/artifacts, benchmark response dumps, or SQLite runtime data.
- Keep API/SSE contract docs aligned with endpoint behavior.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `package.json`.
- Status: repo-backed: `bridge_chat.kujo`.
