#!/usr/bin/env python3
"""Portable validation for the Kujo skills distribution."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
MAX_SKILL_NAME_LENGTH = 64
MAX_MARKDOWN_BYTES = 1024 * 1024


def fail(message: str) -> None:
    raise ValueError(message)


def location(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)


def read_markdown(path: Path) -> str:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_MARKDOWN_BYTES:
        fail(f"{location(path)}: expected a regular Markdown file of at most {MAX_MARKDOWN_BYTES} bytes")
    return path.read_text(encoding="utf-8")


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        parsed = ast.literal_eval(value)
        if not isinstance(parsed, str):
            fail("frontmatter scalar must be a string")
        return parsed
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    content = read_markdown(path)
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        fail(f"{location(path)}: invalid or missing YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            fail(f"{location(path)}: malformed frontmatter line")
        key = key.strip()
        if key in fields:
            fail(f"{location(path)}: duplicate frontmatter key: {key}")
        fields[key] = scalar(value)
    return fields


def validate_skill(skill_dir: Path) -> str:
    if skill_dir.is_symlink() or not skill_dir.is_dir():
        fail(f"{location(skill_dir)}: expected a regular skill directory")
    for entry in skill_dir.rglob("*"):
        if entry.is_symlink() or not (entry.is_file() or entry.is_dir()):
            fail(f"{location(entry)}: linked or nonregular skill content")
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(f"{skill_dir}: SKILL.md not found")

    fields = parse_frontmatter(skill_file)
    unexpected = set(fields) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        fail(f"{location(skill_file)}: unexpected frontmatter keys: {sorted(unexpected)}")

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()
    if not name or not description:
        fail(f"{location(skill_file)}: name and description are required")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(f"{location(skill_file)}: invalid hyphen-case name: {name}")
    if len(name) > MAX_SKILL_NAME_LENGTH:
        fail(f"{location(skill_file)}: name exceeds {MAX_SKILL_NAME_LENGTH} characters")
    if name != skill_dir.name:
        fail(f"{location(skill_file)}: name {name!r} does not match folder {skill_dir.name!r}")
    if "<" in description or ">" in description or len(description) > 1024:
        fail(f"{location(skill_file)}: invalid description")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if agent_file.exists():
        agent_text = agent_file.read_text(encoding="utf-8")
        if not agent_text.strip() or "\t" in agent_text:
            fail(f"{location(agent_file)}: empty metadata or tab indentation")
    return name


def markdown_skill_refs(path: Path) -> set[str]:
    return set(re.findall(r"`((?:kujo|webops|videoops|publishing-house)-[a-z0-9-]+)`", path.read_text(encoding="utf-8")))


def validate_package(skill_names: set[str]) -> None:
    index_names = set(re.findall(r"^\| `((?:kujo|webops|videoops|publishing-house)-[a-z0-9-]+)` \|", (REPO_ROOT / "SKILLS_INDEX.md").read_text(encoding="utf-8"), re.MULTILINE))
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
        positive = {item.strip().casefold() for item in fixture["should_trigger"]}
        negative = {item.strip().casefold() for item in fixture["should_not_trigger"]}
        if positive & negative:
            fail(f"trigger-queries.json: {name} has contradictory trigger examples")

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
        paths = [root] if root.is_file() else root.rglob("*.md")
        for path in paths:
            if path.is_file() and "ruff" in read_markdown(path).lower():
                stale.append(str(path.relative_to(REPO_ROOT)))
    if stale:
        fail(f"stale Ruff wording found in: {stale}")


def validate_markdown_links() -> None:
    missing = []
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in REPO_ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(REPO_ROOT).parts):
            continue
        for target in pattern.findall(read_markdown(path)):
            target = target.strip()
            if not target:
                continue
            if target.startswith("<") and ">" in target:
                target = target[1:target.index(">")]
            else:
                target = target.split(maxsplit=1)[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / local_target).resolve()
            if local_target and (Path(local_target).is_absolute() or not resolved.is_relative_to(REPO_ROOT) or not resolved.exists()):
                missing.append(f"{path.relative_to(REPO_ROOT)} -> {target}")
    if missing:
        fail("missing Markdown targets:\n" + "\n".join(missing))


def main() -> int:
    requested = [Path(value).absolute() for value in sys.argv[1:]]
    skill_dirs = requested or sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir() or path.is_symlink())
    names = set()
    for path in skill_dirs:
        name = validate_skill(path)
        if name in names:
            fail(f"{location(path)}: duplicate skill: {name}")
        names.add(name)
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
