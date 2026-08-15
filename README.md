# Kujo Agent Skills

[![Version](https://img.shields.io/badge/version-0.4.1-black)](https://github.com/kujolang/kujo-skills)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)
[![built with Kujo](https://img.shields.io/badge/built%20with-Kujo-white.svg)](https://github.com/kujolang/kujo)

Repository-backed Agent Skills for the [Kujo programming language](https://kujolang.ai) and its ecosystem tools.

The catalog gives coding agents exact Kujo commands, safety boundaries, validation gates, and source-of-truth paths. It covers everyday `.kujo` development, the Rust runtime, the complete Publishing House editorial toolchain, and focused ecosystem workflows.

## Why use this pack?

- Route work to 95 focused skills instead of one broad prompt, including the release-to-site `kujo-ecosystem-launch` coordinator, 30 WebOps skills, and 11 Publishing House tool, profile, quality, and lifecycle skills.
- Keep VM-first execution, capability boundaries, and CLI contracts explicit.
- Ground recommendations in Kujo repositories, tests, and operational docs.
- Validate the complete catalog offline with one command.
- Install only the skills an agent actually needs.

## Quick start

Clone and validate the pack:

```bash
git clone https://github.com/kujolang/kujo-skills.git
cd kujo-skills
bash tests/release-readiness.sh
```

Install one skill into a personal Codex skill directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/kujo-core-language ~/.codex/skills/
```

Then ask Codex to use it:

```text
Use $kujo-core-language to review this .kujo script for current syntax and VM-first execution.
```

Other Agent Skills-compatible runtimes may use a different skill directory. Copy the complete skill folder, including `SKILL.md` and any `agents/` metadata.

## Find the right skill

Start with the [skill catalog](SKILLS_INDEX.md). Common entry points include:

| Goal | Skill |
|---|---|
| Write or review Kujo source | `kujo-core-language` |
| Build a deterministic Kujo CLI tool | `kujo-tool-building` |
| Review capability and host-effect safety | `kujo-security-hardening` |
| Run release-readiness checks | `kujo-shipcheck-workflows` |
| Release a Kujo project and synchronize its public web presence | `kujo-ecosystem-launch` |
| Detect documentation or artifact drift | `kujo-concord-workflows` |
| Run isolated local workflow proof | `kujo-workcell-workflows` |
| Audit or refresh this skills pack | `kujo-skill-auditor` |
| Crawl and compare a website | `kujo-siteprobe-workflows` |
| Normalize search/analytics/provider evidence | `kujo-searchbridge-workflows` |
| Build deterministic content relationships | `kujo-contentgraph-workflows` |
| Run a WebOps methodology | the narrowest `webops-*` skill |
| Run the Publishing House lifecycle | `kujo-publishing-house-workflows` |
| Operate a Publishing House tool | the narrowest tool-specific workflow skill |

See [examples](examples/README.md) for installation bundles and routing prompts.

## Repository map

- [`SKILLS_INDEX.md`](SKILLS_INDEX.md): complete catalog and activation map.
- [`skills/`](skills/): drop-in Agent Skills; folder names match skill names.
- [`evals/`](evals/): positive and negative trigger-routing fixtures.
- [`guide/`](guide/): longer language, runtime, security, tooling, and release guidance.
- [`docs/launch-checklist.md`](docs/launch-checklist.md): technical-preview evidence and remaining boundaries.
- [`tests/`](tests/): portable repository and clean-install validation.
- [`kujo-skills.spec.yml`](kujo-skills.spec.yml): technical-preview scope and acceptance criteria.

## Release and support status

This repository is the MIT-licensed `0.4.1` technical preview of the Kujo skills pack. Kujo `v1.0.1` is the current stable language/runtime baseline for the Publishing House toolchain; individual skills preserve explicit preview or experimental boundaries for narrower APIs.

The pack provides guidance, not runtime enforcement. An agent or host must load a skill and enforce its own permissions. Kujo itself is not a sandbox: use `--untrusted`, least-privilege `--allow-*` flags, and external isolation for high-risk scripts.

Marketplace publication, automatic installation into live profiles, and claims that third-party agents will obey these skills remain outside this repository's evidence boundary.

For contribution, support, and vulnerability-reporting guidance, see [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md).

## License

Released under the [MIT License](LICENSE).
