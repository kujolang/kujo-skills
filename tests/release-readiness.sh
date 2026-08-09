#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 scripts/validate_skills.py
python3 -m json.tool package.json >/dev/null
python3 -m json.tool evals/trigger-queries.json >/dev/null
python3 -m json.tool tests/eval.json >/dev/null

test -f skills/kujo-workcell-workflows/SKILL.md
test -f skills/kujo-site-kit-workflows/SKILL.md
test -f skills/kujo-tribunal-workflows/SKILL.md
test -f skills/kujo-relay-workflows/SKILL.md
test -f skills/kujo-redact-workflows/SKILL.md

bash .github/scripts/check-kujo-tool-artifacts.sh
git diff --check

echo "release-readiness validation passed"
