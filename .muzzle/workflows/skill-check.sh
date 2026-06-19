#!/usr/bin/env bash
set -euo pipefail

validator="/Users/robertdevore/.codex/skills/.system/skill-creator/scripts/quick_validate.py"

if [ "$#" -gt 0 ]; then
  skills=("$@")
else
  skills=()
  while IFS= read -r skill; do
    skills+=("$skill")
  done < <(find skills -mindepth 1 -maxdepth 1 -type d | sort)
fi

for skill in "${skills[@]}"; do
  python3 "$validator" "$skill"
done

python3 -m json.tool evals/trigger-queries.json >/dev/null

echo "validated ${#skills[@]} skill(s) and evals/trigger-queries.json"
