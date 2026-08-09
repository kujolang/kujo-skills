# Examples

## Core language review

Install the core language and security skills together:

```bash
mkdir -p ~/.codex/skills
cp -R skills/kujo-core-language ~/.codex/skills/
cp -R skills/kujo-security-hardening ~/.codex/skills/
```

Example routing prompt:

```text
Use $kujo-core-language and $kujo-security-hardening to review this script for current syntax, VM behavior, and least-privilege execution.
```

## Release-readiness bundle

```bash
mkdir -p ~/.codex/skills
cp -R skills/kujo-shipcheck-workflows ~/.codex/skills/
cp -R skills/kujo-concord-workflows ~/.codex/skills/
cp -R skills/kujo-workcell-workflows ~/.codex/skills/
```

Example routing prompt:

```text
Use ShipCheck, Concord, and Workcell to produce a local release-readiness report with reproducible evidence.
```

## Verify before installing

```bash
bash tests/release-readiness.sh
bash tests/clean-checkout.sh
```
