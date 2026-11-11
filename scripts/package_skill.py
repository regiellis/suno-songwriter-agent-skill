#!/usr/bin/env python3
"""Build or verify the skill ZIP served by the documentation site."""

import argparse
from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the ZIP is missing or stale')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    destination = root / 'docs/downloads/suno-songwriter.zip'
    files = [root / name for name in ('SKILL.md', 'README.md', 'CHANGELOG.md', 'LICENSE')]
    files += sorted((root / 'references').glob('*.md'))
    files += sorted((root / 'agents').glob('*.yaml'))
    buffer = BytesIO()
    with ZipFile(buffer, 'w', compression=ZIP_DEFLATED) as archive:
        for path in files:
            entry = ZipInfo('suno-songwriter/' + path.relative_to(root).as_posix())
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    content = buffer.getvalue()
    if args.check:
        if not destination.exists() or destination.read_bytes() != content:
            parser.exit(1, 'Skill ZIP is missing or stale. Run python3 scripts/package_skill.py\n')
        print('Skill ZIP matches source.')
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        print(f'Built {destination.relative_to(root)} ({len(files)} files, {len(content):,} bytes).')


if __name__ == '__main__':
    main()
