#!/usr/bin/env python3
"""Read-only repository preflight for Kujo ecosystem launches."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


SEMVER = re.compile(r"^(?:v)?\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def run_git(repo: Path, *args: str) -> tuple[int, str]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip()


def inspect_repo(path_text: str, require_clean: bool, tag: str | None) -> tuple[dict[str, object], list[str]]:
    path = Path(path_text).expanduser().resolve()
    errors: list[str] = []
    record: dict[str, object] = {"path": str(path), "exists": path.is_dir()}
    if not path.is_dir():
        errors.append(f"repository path does not exist: {path}")
        return record, errors

    code, inside = run_git(path, "rev-parse", "--is-inside-work-tree")
    record["git_repository"] = code == 0 and inside == "true"
    if not record["git_repository"]:
        errors.append(f"not a git repository: {path}")
        return record, errors

    _, branch = run_git(path, "branch", "--show-current")
    _, head = run_git(path, "rev-parse", "HEAD")
    _, status = run_git(path, "status", "--porcelain=v1")
    _, origin = run_git(path, "remote", "get-url", "origin")
    record.update(
        {
            "branch": branch or None,
            "head": head or None,
            "dirty": bool(status),
            "origin": origin or None,
            "readme": (path / "README.md").is_file(),
            "changelog": (path / "CHANGELOG.md").is_file(),
        }
    )

    version_file = path / "VERSION"
    record["version_file"] = version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else None

    if require_clean and status:
        errors.append(f"working tree is dirty: {path}")
    if not origin:
        errors.append(f"origin remote is missing: {path}")

    if tag:
        code, resolved = run_git(path, "rev-parse", "--verify", f"refs/tags/{tag}^{{}}")
        record["required_tag"] = tag
        record["tag_exists"] = code == 0
        record["tag_commit"] = resolved or None
        if code != 0:
            errors.append(f"required tag is missing: {tag} in {path}")

    return record, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--launch-type", required=True, choices=("tool", "workflow", "skill", "agent-team"))
    parser.add_argument("--source", action="append", required=True, help="Source repository path; repeat for batches")
    parser.add_argument("--site", help="Optional site repository path")
    parser.add_argument("--release-version", help="Intended semantic version")
    parser.add_argument("--release-authorized", action="store_true")
    parser.add_argument("--deploy-authorized", action="store_true")
    parser.add_argument("--require-clean", action="store_true")
    parser.add_argument("--require-tag", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    if args.release_version and not SEMVER.fullmatch(args.release_version):
        errors.append(f"invalid semantic version: {args.release_version}")
    if args.require_tag and not args.release_version:
        errors.append("--require-tag requires --release-version")

    tag = None
    if args.require_tag and args.release_version:
        tag = args.release_version if args.release_version.startswith("v") else f"v{args.release_version}"

    repositories: list[dict[str, object]] = []
    for source in args.source:
        record, repo_errors = inspect_repo(source, args.require_clean, tag)
        record["role"] = "source"
        repositories.append(record)
        errors.extend(repo_errors)

    if args.site:
        record, repo_errors = inspect_repo(args.site, args.require_clean, None)
        record["role"] = "site"
        repositories.append(record)
        errors.extend(repo_errors)

    receipt = {
        "schema": "kujo.ecosystem-launch.preflight/v1",
        "ok": not errors,
        "launch_type": args.launch_type,
        "release": {"version": args.release_version, "authorized": args.release_authorized},
        "deployment": {"authorized": args.deploy_authorized, "site_in_scope": bool(args.site)},
        "repositories": repositories,
        "errors": errors,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
