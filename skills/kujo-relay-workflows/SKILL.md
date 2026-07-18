---
name: kujo-relay-workflows
description: "Use this skill when running, validating, inspecting, repairing, or maintaining Relay bounded agent mission workflows: `bin/relay`, `doctor`, `chat`, `models`, `agents`, `missions`, `runs`, fixture/live provider paths, PackWrite/RunLedger/ChangeBucket/Eval evidence, event bundles, tool-result bundles, run indexes, Watchdog route posture, or Relay source/docs changes."
---

# Kujo Relay Workflows

Use Relay as the Kujo-native composition and execution layer for bounded local agent missions. It composes AI SDK, Agents SDK, PackWrite, RunLedger, ChangeBucket, Eval, Capsule, and Chain of Command contracts rather than replacing them.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
RELAY_REPO="${RELAY_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/relay}"
cd "$RELAY_REPO"
export KUJO_BIN="${KUJO_BIN:-/Users/robertdevore/2026/Kujolang/kujo-repos/kujo/target/release/kujo}"
./bin/relay doctor --json
./bin/relay agents validate --json
./bin/relay chat "Summarize the mission boundary" --fixture --json
./bin/relay chat "Stream a short answer" --fixture --stream
./bin/relay models probe fixture-model --fixture --json
./bin/relay runs list --json
./bin/relay runs rebuild --json
```

Run the local acceptance set before claiming broad Relay health:

```bash
bash tests/relay_acceptance.sh
```

## Workflow Notes

- Fixture mode is default for safe local operation and records `direct_ai_sdk` as the deterministic no-network route. Live calls require configured Watchdog/AI SDK posture and must not silently bypass Watchdog.
- `missions run` writes PackWrite packets and manifest, AgentEvent-compatible JSONL, sealed RelayReceipt index, RunLedger receipt, ChangeBucket result, Eval result, optional provider tool-result bundle, resumable state, and Markdown/JSON reports under `.relay/runs/<run-id>/`.
- Provider-generated tool planning is opt-in with `agent_tool_mode: "provider"` plus `agent_tool_allowlist`; Relay still executes normalized `relay.write_file` and `relay.run_command` calls through the same Agents SDK policy worker and persists typed tool results.
- Mission budgets include step, repair, token, output, write, tool-call, and tool-turn ceilings. Aggregate mission tokens cap at 65,536 and individual provider requests cap at 16,384.
- Write-enabled missions require `allow_writes: true` and `approval.approved: true`; paths must stay inside the real workspace and cannot traverse `.git`, `.env`, or symlinked parents.
- Commands execute as direct argv from explicit allowlists; `bash`/`sh` repository actions additionally require exact `allowed_script_hashes`. Shell syntax, destructive Git operations, credential paths, force-push, and traversal patterns are denied.
- Evidence reads fail closed for unsafe paths, oversized artifacts, report identity drift, event-chain tampering, and missing required receipts/state.
- Relay is hardened local alpha, not enterprise-production-ready. External live-provider proof, authenticated multi-tenant operation, durable concurrent storage, full Workcell isolation/recovery, and release gates remain open.

When reporting results, state the command, fixture/live mode, run ID, evidence paths, verification status, exit code, and whether any enterprise-readiness claim is out of scope.

## Relay Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `docs/command-reference.md`
3. `docs/integration-matrix.md`
4. Latest relevant `docs/next-session-enhancement-backlog*.md`
5. `main.kujo`
6. Relevant `src/*.kujo`
7. Relevant `schemas/*.json`
8. Relevant `examples/*.json`
9. Relevant `tests/relay_*`

Preserve mission policy checks, bounded JSON/JSONL evidence, redaction, capability registry semantics, Watchdog posture, run-index integrity, event-chain verification, output budgets, direct-argv execution, and fail-closed evidence persistence unless the task explicitly changes them.

Run validation after source, docs, schema, mission, adapter, or evidence-contract changes:

```bash
bash tests/relay_acceptance.sh
git diff --check
```

For focused changes, run the narrow smoke named in `README.md`, then the aggregate acceptance runner before finishing.

## Search And Safety

- Exclude `.relay/runs/`, generated PackWrite packets, and bulk backlogs unless targeted.
- Do not print provider tokens, registry capabilities, private keys, or raw credential-bearing environment values.
- Treat live Watchdog/provider proof as unavailable unless the environment is explicitly configured and verified.
- Keep relative tool paths rooted at the Relay checkout before subprocess cwd changes.

Use `rg` for broad searches and exclude generated, dependency, cache, and run-output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`, `docs/command-reference.md`, `docs/integration-matrix.md`, `docs/next-session-enhancement-backlog-2026-07-13-v85.md`.
- Status: repo-backed: `main.kujo`, `src/*.kujo`, `schemas/*.json`, `examples/*.json`, `tests/relay_acceptance.sh`, `tests/relay_*`.
