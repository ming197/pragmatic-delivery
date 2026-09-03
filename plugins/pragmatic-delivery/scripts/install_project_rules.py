#!/usr/bin/env python3
"""Install an idempotent managed Pragmatic Delivery block into project instructions."""

from __future__ import annotations

import argparse
from pathlib import Path


START = "<!-- pragmatic-delivery:start -->"
END = "<!-- pragmatic-delivery:end -->"


def update_file(path: Path, block: str, check: bool) -> str:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if START in existing or END in existing:
        if existing.count(START) != 1 or existing.count(END) != 1:
            raise RuntimeError(f"Malformed managed block in {path}")
        before, remainder = existing.split(START, 1)
        _, after = remainder.split(END, 1)
        prefix = before.rstrip()
        updated = (prefix + "\n\n" if prefix else "") + block + after
    else:
        separator = "\n\n" if existing.strip() else ""
        updated = existing.rstrip() + separator + block + "\n"

    if updated == existing:
        return "current"
    if not check:
        path.write_text(updated, encoding="utf-8")
    return "would-update" if check else ("updated" if existing else "created")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("both", "codex", "claude"), default="both")
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    plugin_root = Path(__file__).resolve().parent.parent
    block = (plugin_root / "assets" / "project-rules.md").read_text(encoding="utf-8").strip()
    project = args.project.resolve()
    targets = []
    if args.target in ("both", "codex"):
        targets.append(project / "AGENTS.md")
    if args.target in ("both", "claude"):
        targets.append(project / "CLAUDE.md")

    for target in targets:
        print(f"{target.name}: {update_file(target, block, args.check)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
