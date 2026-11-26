#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

test_root="$(mktemp -d "${TMPDIR:-/tmp}/kujo-skills-XXXXXX")"
trap 'rm -rf -- "$test_root"' EXIT

profile_skills="$test_root/profile/skills"
mkdir -p "$profile_skills"
cp -R skills/. "$profile_skills/"
python3 scripts/validate_skills.py "$profile_skills"/*

test -f "$profile_skills/kujo-core-language/SKILL.md"
grep -Fq 'name: kujo-core-language' "$profile_skills/kujo-core-language/SKILL.md"
test -f "$profile_skills/kujo-way-development/SKILL.md"
test -f "$profile_skills/kujo-way-development/references/ai-and-agents.md"
test -f "$profile_skills/kujo-way-development/references/security-and-validation.md"
grep -Fq 'name: kujo-way-development' "$profile_skills/kujo-way-development/SKILL.md"

test -s "$profile_skills/kujo-hardening/references/audit-checklist.md"
test -s "$profile_skills/kujo-hardening/references/report.md"
test -s "$profile_skills/kujo-hardening/agents/openai.yaml"

fixture="$test_root/validator-check"
mkdir -p "$fixture"
printf '%s\n' '---' 'name: validator-check' 'name: validator-check' 'description: Fixture' '---' > "$fixture/SKILL.md"
if python3 scripts/validate_skills.py "$fixture" > "$test_root/validator.log" 2>&1; then
  echo "duplicate frontmatter key accepted" >&2
  exit 1
fi
grep -Fq 'duplicate frontmatter key: name' "$test_root/validator.log"
printf '%s\n' '---' 'name: validator-check' 'description: Fixture' '---' > "$fixture/SKILL.md"
ln -s SKILL.md "$fixture/linked.md"
if python3 scripts/validate_skills.py "$fixture" > "$test_root/validator.log" 2>&1; then
  echo "linked skill file accepted" >&2
  exit 1
fi
grep -Fq 'linked or nonregular skill content' "$test_root/validator.log"

bash tests/video-skills-install.sh

echo "clean install/use validation passed"
