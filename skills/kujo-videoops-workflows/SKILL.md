---
name: kujo-videoops-workflows
description: "Use when operating the complete Kujo VideoOps team for a new content release, product demo, launch video, social video, explainer, or another arbitrary production request; also use when invoking the VideoOps Producer, coordinating all five specialist agents, packaging a mega prompt, or resuming a VideoOps workspace."
---

# Kujo VideoOps Workflows

Use this skill as the harness-neutral team entry point. The real production surface is the `VideoOps Producer` plus five specialist role contracts. The deterministic workflow fixture is acceptance evidence, not the production implementation.

## Start

1. Locate `kujo-agents/videoops/producer/AGENT.md`. If the harness cannot access that repository, require the user to attach the complete `videoops/` package.
2. Read `videoops/README.md`, all `00-*.md` shared standards, `producer/AGENT.md`, and `producer/SKILL.md`.
3. Preserve the user's complete request. Accept either existing PackWrite `intake/` artifacts or a plain-language mega prompt. Normalize missing intake inside the target workspace without discarding requirements. The Kujo-native `videoops-production/bin/run --workspace <path> --request <prompt.md>` command can initialize this safely and emit `RUN_VIDEOOPS.md`.
4. Confirm only choices whose absence would materially change the result. Otherwise record reasonable assumptions and continue.

## Operate The Team

Run the roles in this order: Creative Director, Asset Scout, Media Generator only for explicit `GENERATE` items, HyperFrames Editor, and independent Video Critic. Before each stage, read that role's `AGENT.md` and `SKILL.md` plus every named skill available to the harness. Use native subagents or handoffs when supported; otherwise execute one role at a time with isolated role context. Files, schemas, receipts, and handoffs are the durable boundary in either mode.

Use current HyperFrames skills and CLI behavior for composition work. Use browser capture, repository assets, local media tools, and generation providers only when available and authorized. Never pretend an unavailable integration ran. Ask before paid media generation, authenticated capture, publication, or another external effect.

## Review And Completion

Run deterministic render checks before semantic review. The Editor may not approve its own output. A Critic FAIL must contain a bounded fix list; send only that list and exact reviewed-render lineage back to the Editor. Repeat review for the revised candidate and stop after three failed cycles. Finalize only the exact candidate the Critic passed. Report the final path, checksum, render metadata, approval, revisions, external effects, cost/token evidence when available, and remaining blockers.

## Harness Invocation

A compatible harness needs filesystem access to the agent package and the tools required by the requested production. Invoke it with: `Use the VideoOps Producer at <kujo-agents>/videoops/producer/AGENT.md. Read and follow the complete VideoOps package, then execute this production request through the five specialist roles: <request>. Work in <workspace>.` The same invocation works in Codex, Claude Code, Hermes, Paperclip, or another file-capable agent runtime; adapters may translate the manifest, but must preserve role boundaries and permissions.
