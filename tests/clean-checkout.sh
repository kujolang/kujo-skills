#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

test_root="$(mktemp -d)"
trap 'rm -rf -- "$test_root"' EXIT

profile_skills="$test_root/profile/skills"
mkdir -p "$profile_skills"
cp -R skills/kujo-core-language "$profile_skills/"

test -f "$profile_skills/kujo-core-language/SKILL.md"
python3 scripts/validate_skills.py "$profile_skills/kujo-core-language"
grep -Fq 'name: kujo-core-language' "$profile_skills/kujo-core-language/SKILL.md"

echo "clean install/use validation passed"
