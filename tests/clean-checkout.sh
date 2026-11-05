#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

test_root="$(mktemp -d)"
trap 'rm -rf -- "$test_root"' EXIT

profile_skills="$test_root/profile/skills"
mkdir -p "$profile_skills"
cp -R skills/kujo-core-language "$profile_skills/"
cp -R skills/kujo-way-development "$profile_skills/"

test -f "$profile_skills/kujo-core-language/SKILL.md"
python3 scripts/validate_skills.py "$profile_skills/kujo-core-language"
grep -Fq 'name: kujo-core-language' "$profile_skills/kujo-core-language/SKILL.md"
test -f "$profile_skills/kujo-way-development/SKILL.md"
test -f "$profile_skills/kujo-way-development/references/ai-and-agents.md"
test -f "$profile_skills/kujo-way-development/references/security-and-validation.md"
python3 scripts/validate_skills.py "$profile_skills/kujo-way-development"
grep -Fq 'name: kujo-way-development' "$profile_skills/kujo-way-development/SKILL.md"

cp -R skills/kujo-hardening "$profile_skills/"
python3 scripts/validate_skills.py "$profile_skills/kujo-hardening"
test -s "$profile_skills/kujo-hardening/references/audit-checklist.md"
test -s "$profile_skills/kujo-hardening/references/report.md"
test -s "$profile_skills/kujo-hardening/agents/openai.yaml"

bash tests/video-skills-install.sh

echo "clean install/use validation passed"
