#!/usr/bin/env python3
"""Portable validation for the Kujo skills distribution."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
MAX_SKILL_NAME_LENGTH = 64


def fail(message: str) -> None:
    raise ValueError(message)


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        parsed = ast.literal_eval(value)
        if not isinstance(parsed, str):
            fail("frontmatter scalar must be a string")
        return parsed
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        fail(f"{path.relative_to(REPO_ROOT)}: invalid or missing YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            fail(f"{path.relative_to(REPO_ROOT)}: malformed frontmatter line: {line}")
        fields[key.strip()] = scalar(value)
    return fields


def validate_skill(skill_dir: Path) -> str:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(f"{skill_dir}: SKILL.md not found")

    fields = parse_frontmatter(skill_file)
    unexpected = set(fields) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        fail(f"{skill_file.relative_to(REPO_ROOT)}: unexpected frontmatter keys: {sorted(unexpected)}")

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()
    if not name or not description:
        fail(f"{skill_file.relative_to(REPO_ROOT)}: name and description are required")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(f"{skill_file.relative_to(REPO_ROOT)}: invalid hyphen-case name: {name}")
    if len(name) > MAX_SKILL_NAME_LENGTH:
        fail(f"{skill_file.relative_to(REPO_ROOT)}: name exceeds {MAX_SKILL_NAME_LENGTH} characters")
    if name != skill_dir.name:
        fail(f"{skill_file.relative_to(REPO_ROOT)}: name {name!r} does not match folder {skill_dir.name!r}")
    if "<" in description or ">" in description or len(description) > 1024:
        fail(f"{skill_file.relative_to(REPO_ROOT)}: invalid description")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if agent_file.exists():
        agent_text = agent_file.read_text(encoding="utf-8")
        if not agent_text.strip() or "\t" in agent_text:
            fail(f"{agent_file.relative_to(REPO_ROOT)}: empty metadata or tab indentation")
    return name


def markdown_skill_refs(path: Path) -> set[str]:
    return set(re.findall(r"`((?:kujo|webops)-[a-z0-9-]+)`", path.read_text(encoding="utf-8")))


def validate_package(skill_names: set[str]) -> None:
    index_names = set(re.findall(r"^\| `((?:kujo|webops)-[a-z0-9-]+)` \|", (REPO_ROOT / "SKILLS_INDEX.md").read_text(encoding="utf-8"), re.MULTILINE))
    expected_names = markdown_skill_refs(REPO_ROOT / "evals" / "expected-skill-map.md")
    trigger_data = json.loads((REPO_ROOT / "evals" / "trigger-queries.json").read_text(encoding="utf-8"))
    eval_suite = json.loads((REPO_ROOT / "tests" / "eval.json").read_text(encoding="utf-8"))
    trigger_names = set(trigger_data)

    for label, names in (("SKILLS_INDEX.md", index_names), ("expected-skill-map.md", expected_names), ("trigger-queries.json", trigger_names)):
        if names != skill_names:
            fail(f"{label}: missing={sorted(skill_names - names)} unexpected={sorted(names - skill_names)}")

    for name, fixture in trigger_data.items():
        if not isinstance(fixture, dict):
            fail(f"trigger-queries.json: {name} must map to an object")
        for key in ("should_trigger", "should_not_trigger"):
            values = fixture.get(key)
            if not isinstance(values, list) or not values or not all(isinstance(item, str) and item.strip() for item in values):
                fail(f"trigger-queries.json: {name}.{key} must be a non-empty string list")

    version = (REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    manifest = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if manifest.get("version") != version or manifest.get("license") != "MIT":
        fail("VERSION, package.json version, or MIT license metadata is inconsistent")
    if version not in readme or f"## {version}" not in changelog:
        fail("README.md or CHANGELOG.md does not name the current VERSION")
    if eval_suite.get("version") != version or not eval_suite.get("tests"):
        fail("tests/eval.json does not match VERSION or has no checks")

    spec_text = (REPO_ROOT / "kujo-skills.spec.yml").read_text(encoding="utf-8")
    for required_marker in ("name:", "goal:", "acceptance_criteria:", "eval_requirements:"):
        if required_marker not in spec_text:
            fail(f"kujo-skills.spec.yml is missing {required_marker}")

    stale = []
    for root in (REPO_ROOT / "README.md", REPO_ROOT / "guide", REPO_ROOT / "skills"):
        paths = [root] if root.is_file() else root.rglob("*")
        for path in paths:
            if path.is_file() and "ruff" in path.read_text(encoding="utf-8", errors="ignore").lower():
                stale.append(str(path.relative_to(REPO_ROOT)))
    if stale:
        fail(f"stale Ruff wording found in: {stale}")


def validate_markdown_links() -> None:
    missing = []
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in REPO_ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(REPO_ROOT).parts):
            continue
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            target = target.strip().split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (path.parent / local_target).resolve().exists():
                missing.append(f"{path.relative_to(REPO_ROOT)} -> {target}")
    if missing:
        fail("missing Markdown targets:\n" + "\n".join(missing))


def main() -> int:
    requested = [Path(value).resolve() for value in sys.argv[1:]]
    skill_dirs = requested or sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    names = {validate_skill(path) for path in skill_dirs}
    if not requested:
        validate_package(names)
        validate_markdown_links()
    print(f"validated {len(skill_dirs)} skill(s)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, SyntaxError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
