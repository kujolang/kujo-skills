#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
test_root="$(mktemp -d)"
trap 'rm -rf -- "$test_root"' EXIT

fixture_repo="$test_root/one-commit"
mkdir -p "$fixture_repo/.github/scripts" "$fixture_repo/config"
cp "$repo_root/.github/scripts/check-kujo-tool-artifacts.sh" "$fixture_repo/.github/scripts/"
cp "$repo_root/config/kujo-tool-artifacts.gitignore" "$fixture_repo/config/"
cp "$repo_root/.gitignore" "$fixture_repo/.gitignore"

git -C "$fixture_repo" init -q
git -C "$fixture_repo" config user.name "Kujo Skills Test"
git -C "$fixture_repo" config user.email "test@example.invalid"
git -C "$fixture_repo" add .github config .gitignore
git -C "$fixture_repo" commit -qm "Create one-commit fixture"

output="$test_root/output.log"
bash "$fixture_repo/.github/scripts/check-kujo-tool-artifacts.sh" > "$output" 2>&1
grep -Fq '[tool-artifacts] OK: ignore rules are present; no commit range to scan' "$output"
if grep -Eq 'fatal:|\[tool-artifacts\] ERROR:' "$output"; then
  echo "single-commit guard emitted an unexpected error" >&2
  cat "$output" >&2
  exit 1
fi

echo "tool artifacts single-commit guard passed"
