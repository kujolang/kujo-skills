---
name: kujo-way-development
description: Use when building or substantially reviewing a Kujo-related project that needs cross-ecosystem routing, compact agent-readable code, deterministic AI/offline behavior, and evidence-backed completion. For a narrow syntax question only, prefer kujo-core-language; for one specialized ecosystem tool, prefer its focused workflow skill.
---

# Kujo Way Development

Build the smallest complete Kujo-native solution whose behavior is explicit,
deterministic, capability-aware, and verifiable by humans and agents.

## Route Before Editing

Use the layer that owns the behavior:

| Work | Owner |
| --- | --- |
| Lexer, parser, compiler, VM, interpreter, native builtin | Kujo runtime; usually Rust |
| CLI tool, app, connector, or automation | Kujo `.kujo` project |
| Provider transport and normalized model behavior | AI SDK or adapter boundary |
| Runner, tools, approvals, memory, retrieval, handoffs, traces, artifacts, budgets | Agents SDK |
| Resumable orchestration | Dispatch |
| MCP contracts and servers | Kujo MCP tooling |
| Reusable provider-neutral roles | Kujo Agents package format |

Do not put provider routing, retry policy, RAG, agent orchestration, eval,
observability, registry, or hosted-product policy into core Kujo unless the
current source-of-truth explicitly changes that boundary.

If ownership is unclear or the request crosses repositories, inspect the target
READMEs and nearest `AGENTS.md` files before choosing a layer.

## Working Contract

Before implementation, define only what changes execution:

- Accepted inputs and validation.
- Stable human and machine outputs.
- Ordering and tie behavior.
- Time, token, iteration, output, and collection bounds.
- Host effects and required capabilities.
- Error shapes, exit codes, stop conditions, and approval boundaries.

Then use this loop:

```text
Route -> Contract -> Inspect -> Implement -> Execute -> Challenge -> Record -> Stop
```

Stop when the requested contract passes. Do not invent adjacent cleanup or
future abstractions.

## Implementation Defaults

- Use Kujo for tools, agents, connectors, workflows, and glue when Kujo can do
  the job. Do not add Python, shell, or JavaScript bridges by default.
- Use current `let`, `mut`, `const`, `func`, and `export func` syntax from the
  target's canonical docs/examples.
- Quote strings. Treat unknown identifiers, missing keys, and invalid indexing
  as errors unless the contract explicitly handles them.
- Compare predicate helpers explicitly when they return `1`/`0`.
- Reassign collection helper results when retaining them.
- Prefer native helpers for lines, JSON/schema, paths, hashes, environment,
  processes, AI, and collections over manual glue.
- Prefer argv-based `spawn_process` for user-controlled process arguments.
- Keep the main feature visible. Add helpers only when they isolate a real
  contract or remove meaningful repetition.
- Use one stable data shape rather than multiple near-duplicate wrappers.
- Remove unused state, redundant passes, repeated context, and speculative
  extension points.
- Bound retained history and top-k work instead of materializing unused data.
- Comments explain invariants, effects, security boundaries, or surprising
  runtime behavior—not syntax.

Token efficiency means low information overhead, not code golf. Prefer concise
instructions, schemas over prose parsing, direct examples, and stable payloads.

## Deterministic Defaults

- Use the VM path for normal scripts: `kujo run <file>`.
- Treat `kujo check` as syntax/compile evidence, not runtime proof.
- Keep default tests and examples offline and replayable.
- Keep successful machine-readable stdout free of prose.
- Preserve public JSON fields, ordering, exit behavior, fixtures, and lockfiles.
- Fail closed when input, schema, capability, approval, dependency, or required
  evidence is unavailable.

## Conditional References

Read only the reference that matches the work:

- For model calls, token/context handling, tools, agent runners, memory,
  retrieval, handoffs, or offline fixtures, read
  [references/ai-and-agents.md](references/ai-and-agents.md).
- For CLI contracts, host effects, untrusted execution, or final verification,
  read [references/security-and-validation.md](references/security-and-validation.md).

For a narrow subsystem, also use the focused installed skill when available,
such as `kujo-core-language`, `kujo-tool-building`,
`kujo-agents-sdk-workflows`, `kujo-security-hardening`, or
`kujo-runtime-parity`. This skill supplies the shared Kujo development posture;
it does not replace deeper subsystem contracts.

## Anti-Slop Gate

Reject changes that:

- Invent architecture, APIs, success, claims, or evidence.
- Add unused frameworks, wrappers, dependencies, configuration, or abstraction.
- Reimplement a Kujo or SDK capability in another language without necessity.
- Hide the feature behind generic helpers.
- Use a live model to test deterministic logic.
- Parse prose when a structured contract exists.
- Catch and ignore errors or silently downgrade blocked work.
- Present preview/experimental surfaces as stable.
- Blindly refresh snapshots or manually edit generated artifacts.
- Expand scope into unrelated cleanup.

## Completion Report

Before finishing, verify that the behavior is in the correct layer, relevant
success/failure/boundary paths execute, contracts and docs agree, only scoped
files changed, and external blockers have an exact next action.

Report only:

- What changed.
- What verification passed.
- What remains blocked.
- Relevant artifact paths and commit IDs.

Do not claim a clean tree, commit, push, release, security property, or runtime
guarantee without direct evidence.
