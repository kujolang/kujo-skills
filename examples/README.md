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

## VideoOps media provider bundle

Regenerate from canonical Kujo sources, validate, then copy the bundle using the
same installation convention as other skills. Installing into a live profile
requires operator authorization; implementation tests use a temporary profile.

```bash
kujo run scripts/generate_videoops_skills.kujo
bash tests/release-readiness.sh
bash tests/videoops-install.sh
# Only after operator authorization, choose the actual target profile:
# cp -R skills/kujo-videoops-workflows skills/videoops-* "$PROFILE_SKILLS/"
```

The bundle references the shared kujo-agents/videoops/tools runtime and kujo-agents toolchain
contract. It does not embed provider credentials, private voice selections or a
second mixer. Read the runtime's operator setup docs for environment/OS-secret
references and scoped authority; skill installation grants no account authority.
Do not patch a cached third-party HyperFrames skill. Approved local media paths,
alignment and normalized receipts are the stable media-use/audio integration.
