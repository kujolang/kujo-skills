# AI And Agent Development

Read this reference only when the task uses model calls, AI helpers, agent
runners, tools, memory, retrieval, handoffs, traces, artifacts, or budgets.

## AI-Native Means Offline-Capable

Build a deterministic local path before live provider integration.

- `ai_request_hash`: credential-free deterministic request identity.
- `ai_text`, `ai_image_url`, `ai_message`: portable multimodal messages.
- `ai_chat`, `ai_stream_chat`, `ai_embedding`, `ai_tool_loop`: provider effects
  behind the dedicated AI capability.
- `ai_count_tokens`: stable local estimate, never billing-grade tokenization.
- `ai_fit_context`: bounded history that preserves system messages and the last
  user message.
- `json_schema_validate`: local validation for model output, tool arguments,
  and config.
- `vec_*`: local vector math, not storage or retrieval policy.
- `secret` and narrowly contained `reveal`: credential handling at the provider
  boundary.

Use typed/structured errors when operators need deterministic recovery. Bound
model calls by time, tokens, cost, iterations, output size, and approved
endpoints as applicable.

## Strict Replay

Default AI tests and examples to replay:

```bash
KUJO_AI_REPLAY=tests/fixtures/ai_cassettes \
KUJO_AI_REPLAY_MODE=strict \
kujo run path/to/example.kujo
```

Strict replay must not open a socket. Review cassettes before sharing because
they may contain model output or prompt-derived content after credential
redaction.

## Agents SDK Build Order

Use Agents SDK instead of hand-rolling a loop. Add only required primitives:

1. Stable agent identity, concise instructions, execution contract,
   capabilities, and model-policy references.
2. Injected AI SDK adapter. Keep provider selection outside the runner.
3. Tool contracts with IDs, JSON schemas, permissions, risk, timeout, and
   deterministic error mapping.
4. Approval, guardrail, and redaction policy before effectful tools.
5. Explicit budgets for calls, steps, handoffs, memory, artifacts, tokens,
   cost, elapsed time, and iterations as applicable.
6. Session and memory stores with scope and provenance.
7. Bounded retrieval with citations and an offline mock provider.
8. Handoffs with maximum depth and visited-target loop protection.
9. Trace and artifact sinks through their contracts.
10. `create_no_network_harness` proof before any live integration.

Prompts and manifests express intent; they do not grant permissions,
credentials, isolation, or external effects. Runtime adapters must enforce
permission ceilings and fail closed when approval or isolation is unavailable.

## Provider-Neutral Role Package

Use this portable shape for reusable roles:

```text
AGENT.md
SKILL.md
manifest.json
input.schema.json
output.schema.json
```

Define authority, evidence requirements, escalation, handoffs, and stop
conditions. Keep hosted behavior additive and behind adapters.

## Agent Verification

Use the target Agents SDK checkout's pinned `KUJO_BIN` and canonical offline
commands. Typical focused checks are:

```bash
"$KUJO_BIN" test-run tests/relevant_tests.kujo -v
"$KUJO_BIN" test-run tests/example_smoke_tests.kujo -v
"$KUJO_BIN" run examples/examples_smoke_runner.kujo --interpreter
```

The interpreter command is the current Agents SDK example contract; VM remains
the normal default for ordinary Kujo scripts.

Challenge denied approvals, invalid tool input, unknown tools, exhausted
budgets, cancellation, timeout, replay miss, retrieval limits, handoff loops,
memory scope, artifact bounds, and deterministic repeated runs as applicable.
