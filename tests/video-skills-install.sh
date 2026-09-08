#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
profile="$(mktemp -d)"
trap 'rm -rf "$profile"' EXIT
cp -R "$root/skills/kujo-release-video" "$root/skills/kujo-video-styles" "$profile/"
export PYTHONDONTWRITEBYTECODE=1
python3 "$root/scripts/validate_skills.py" "$profile/kujo-release-video" "$profile/kujo-video-styles"
python3 - "$root" "$profile" <<'PY'
import hashlib,json,sys
from pathlib import Path
root,profile=map(Path,sys.argv[1:])
manifest=json.loads((root/'docs/video-skills-import.json').read_text())
checked=0
for entry in manifest['files']:
    relative=Path(entry['path'])
    if relative.suffix=='.md':continue  # Migration documentation deliberately changes.
    installed=profile/Path(*relative.parts[1:])
    assert hashlib.sha256(installed.read_bytes()).hexdigest()==entry['source_sha256'],entry['path']
    checked+=1
assert checked>0
print(f'Imported executable/assets integrity passed: {checked} files')
PY
# Running copied tests exercises the copied skill roots, not the source checkout.
(cd "$profile" && python3 -B -m unittest discover -s kujo-release-video/scripts -p 'test_*.py')
(cd "$profile" && python3 -B -m unittest discover -s kujo-video-styles/scripts -p 'test_*.py')
node "$profile/kujo-video-styles/scripts/test_motion.cjs"
printf 'Video skills temporary-profile installation and production contracts passed\n'
