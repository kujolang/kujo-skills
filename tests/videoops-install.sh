#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
profile="$(mktemp -d)"
trap 'rm -rf "$profile"' EXIT
cp -R "$root/skills/kujo-videoops-workflows" "$root"/skills/videoops-* "$profile/"
for skill_dir in "$profile"/*; do
  python3 "$root/scripts/validate_skills.py" "$skill_dir"
done
for source in "$root/skills/kujo-videoops-workflows/SKILL.md" "$root"/skills/videoops-*/SKILL.md; do
  skill="$(basename "$(dirname "$source")")"
  cmp "$source" "$profile/$skill/SKILL.md"
done
printf 'VideoOps temporary-profile install and byte comparison passed\n'
