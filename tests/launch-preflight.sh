#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
preflight="$repo_root/skills/kujo-ecosystem-launch/scripts/launch_preflight.py"
test_root="$(mktemp -d "${TMPDIR:-/tmp}/kujo-skills-XXXXXX")"
trap 'rm -rf -- "$test_root"' EXIT

fixture_repo="$test_root/source"
mkdir -p "$fixture_repo"
git -C "$fixture_repo" init -q
git -C "$fixture_repo" config user.name "Kujo Skills Test"
git -C "$fixture_repo" config user.email "test@example.invalid"
git -C "$fixture_repo" remote add origin 'https://test-only-user:test-only-password@example.invalid/kujolang/fixture.git?token=fixture-token'
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

python3 -c 'import json,sys; data=json.load(open(sys.argv[1])); repo=data["repositories"][0]; assert data["ok"] is True; assert repo["tag_exists"] is True; assert repo["origin"]=="https://example.invalid/kujolang/fixture.git"' "$test_root/success.json"

if python3 "$preflight" --launch-type skill --source "$fixture_repo" --release-version nope > "$test_root/invalid.json"; then
  echo "invalid semantic version unexpectedly passed" >&2
  exit 1
fi

printf 'dirty\n' >> "$fixture_repo/README.md"
if python3 "$preflight" --launch-type skill --source "$fixture_repo" --release-version 0.4.0 --require-clean > "$test_root/dirty.json"; then
  echo "dirty repository unexpectedly passed" >&2
  exit 1
fi

git -C "$fixture_repo" add README.md
git -C "$fixture_repo" commit -qm "Advance fixture after the tag"
if python3 "$preflight" --launch-type skill --source "$fixture_repo" --release-version 0.4.0 --require-clean --require-tag > "$test_root/old-tag.json"; then
  echo "an older tag unexpectedly certified HEAD" >&2
  exit 1
fi
grep -Fq 'required tag does not identify current HEAD' "$test_root/old-tag.json"

echo "launch preflight contract passed"
