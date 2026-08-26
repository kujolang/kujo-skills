---
name: kujo-way-development
description: Use when building or substantially reviewing a Kujo-related project that needs cross-ecosystem routing, compact agent-readable code, deterministic AI/offline behavior, and evidence-backed completion. For a narrow syntax question only, prefer kujo-core-language; for one specialized ecosystem tool, prefer its focused workflow skill.
---

# Kujo Way Development

The Kujo Way: build the smallest complete Kujo-native solution whose behavior is
explicit, deterministic, capability-aware, and verifiable by humans and agents.
When a claim, contract, or behavior is in doubt, verify it on the runtime rather
than asserting it.

For the fuller philosophy (conventions, "what agents commonly get wrong", and a
review checklist), read `guide/kujo-way.md` in the kujo-skills repo. For a
runnable minimal example done the Kujo Way, see
[references/example-policy-gate.kujo](references/example-policy-gate.kujo).

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

## Worked Example (The Kujo Way In Code)

A minimal deterministic JSON policy gate. It is the canonical first Kujo tool:
local, offline, explicit contract, clean JSON on stdout, diagnostics on stderr,
and non-zero exits that mean something.

```kujo
# policy_gate.kujo - minimal deterministic JSON policy gate
# Usage: kujo run policy_gate.kujo -- '{"min": 3}' '{"value": 5}'

func main() {
    let argv := args()
    if len(argv) < 2 {
        eprint("usage: policy_gate.kujo -- <rule-json> <input-json>")
        exit(2)  # usage/argument error
    }

    # parse_json errors on invalid input -> fail closed, no silent fallback.
    let rules := parse_json(argv[0])
    let input := parse_json(argv[1])

    let value := input["value"]
    if has_key(rules, "min") == 1 && value < rules["min"] {
        print(to_json({"ok": false, "reason": "value below min"}))
        exit(1)  # gate/policy failure
    }

    print(to_json({"ok": true}))
    exit(0)
}

main()
```

Why this is the Kujo Way (not just valid syntax):

- `kujo run` (VM path) is the default; no `--interpreter` shortcut.
- Inputs are validated up front and bad input fails closed at `parse_json`.
- Strings are quoted; dictionary access uses real keys; `has_key(...) == 1`
  compares the predicate explicitly instead of trusting truthiness.
- Successful stdout is clean JSON; human diagnostics use `eprint` to stderr.
- Exit codes follow the CLI contract: `2` usage, `1` policy failure, `0` success
  (runtime/parse failure returns `4`, also non-zero and authoritative).
- No frameworks, no speculative abstraction — just the contract the task needs.

Run it:

```bash
kujo check references/example-policy-gate.kujo --quiet
kujo run  references/example-policy-gate.kujo -- '{"min": 3}' '{"value": 5}'   # -> {"ok":true}, exit 0
kujo run  references/example-policy-gate.kujo -- '{"min": 3}' '{"value": 2}'   # -> {"ok":false,...}, exit 1
```

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
