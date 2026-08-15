#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
preflight="$repo_root/skills/kujo-ecosystem-launch/scripts/launch_preflight.py"
test_root="$(mktemp -d)"
trap 'rm -rf -- "$test_root"' EXIT

fixture_repo="$test_root/source"
mkdir -p "$fixture_repo"
git -C "$fixture_repo" init -q
git -C "$fixture_repo" config user.name "Kujo Skills Test"
git -C "$fixture_repo" config user.email "test@example.invalid"
git -C "$fixture_repo" remote add origin https://example.invalid/kujolang/fixture.git
printf '0.4.0\n' > "$fixture_repo/VERSION"
printf '# Fixture\n' > "$fixture_repo/README.md"
printf '# Changelog\n' > "$fixture_repo/CHANGELOG.md"
git -C "$fixture_repo" add VERSION README.md CHANGELOG.md
git -C "$fixture_repo" commit -qm "Create fixture"
git -C "$fixture_repo" tag -a v0.4.0 -m "v0.4.0"

python3 "$preflight" \
  --launch-type skill \
  --source "$fixture_repo" \
  --release-version 0.4.0 \
  --release-authorized \
  --require-clean \
  --require-tag > "$test_root/success.json"

python3 -c 'import json,sys; data=json.load(open(sys.argv[1])); assert data["ok"] is True; assert data["repositories"][0]["tag_exists"] is True' "$test_root/success.json"

if python3 "$preflight" --launch-type skill --source "$fixture_repo" --release-version nope > "$test_root/invalid.json"; then
  echo "invalid semantic version unexpectedly passed" >&2
  exit 1
fi

printf 'dirty\n' >> "$fixture_repo/README.md"
if python3 "$preflight" --launch-type skill --source "$fixture_repo" --release-version 0.4.0 --require-clean > "$test_root/dirty.json"; then
  echo "dirty repository unexpectedly passed" >&2
  exit 1
fi

echo "launch preflight contract passed"
