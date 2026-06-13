---
name: kujo-packwrite-workflows
description: "Use this skill when generating, validating, debugging, or maintaining PackWrite agent execution packs: `MEGA_PROMPT.md`, `packwrite init`, `validate`, `prompt deepseek`, `prompt codex-review`, provider/model config, dry-run/overwrite behavior, fake AI responses, `/agent` pack outputs, offline tests, or `packwrite` source/test changes."
---

# Kujo PackWrite Workflows

Use PackWrite to compile a project mega-prompt into a validated `/agent` execution pack. It writes operating instructions for implementation/review agents; it does not implement the project itself.

## Quick Start

Default to the local repo unless the user points to another checkout:

```bash
PACKWRITE_REPO="${PACKWRITE_REPO:-/Users/robertdevore/2026/Kujolang/kujo-repos/packwrite}"
cd "${PACKWRITE_REPO}"
KUJO=/path/to/kujo/target/release/kujo ./bin/packwrite --help
./bin/packwrite doctor
./bin/packwrite init MEGA_PROMPT.md --dry-run
./bin/packwrite validate
./bin/packwrite prompt codex-review
```

## Workflow Notes

- Generated `/agent` packs are task artifacts; inspect before committing and avoid overwriting user packs without explicit intent.
- `init --dry-run` previews parse and planning without writing files.
- AI calls can be fully faked in tests through `PACKWRITE_FAKE_RESPONSE_FILE`.

When reporting results, state the command, target path, exit code, important artifact paths, and whether the result is advisory, blocking, or a generated output that still needs review.

## Kujo PackWrite Workflows Repo Work

When modifying this repository, read in this order:

1. `README.md`
2. `AGENTS.md`
3. `docs/HOWTO.md`
4. `docs/CONFIGURATION.md`
5. `docs/ARCHITECTURE.md`
6. `packwrite.kujo`
7. `src/cli.kujo`
8. `src/pack.kujo`
9. `src/validate.kujo`
10. `tests/`

Preserve documented command names, output contracts, and fixture behavior unless the user explicitly asks to change them.

Run validation after source, docs, contract, or example changes:

```bash
make test KUJO=/path/to/kujo/target/release/kujo
make check KUJO=/path/to/kujo/target/release/kujo
KUJO=/path/to/kujo/target/release/kujo ./tests/run.sh
```

## Search And Safety

- All output is stdout; preserve prefixed categories and exit codes.
- Do not hide generated pack phases or provider configuration behind broad abstractions.
- Keep fixtures explicit when exact output is a contract.

Use `rg` for broad searches and exclude generated, dependency, cache, and output directories unless the task explicitly targets them.

## Sources Consulted

- Status: repo-backed: `README.md`.
- Status: repo-backed: `AGENTS.md`.
- Status: repo-backed: `packwrite.kujo`.
- Status: repo-backed: `tests/packwrite_test.kujo`.
