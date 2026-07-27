#!/usr/bin/env python3
"""
update_caution_block.py

Set (or refresh) the standard caution block at the top of every Markdown
file in the repository.

The caution block is three lines:
    > [!CAUTION]
    > <caution text>
    <blank line>

Run from anywhere in the repo:
    python supporting-material/scripts/update_caution_block.py

Idempotent: running it a second time makes no further changes.
Edit CAUTION_TEXT below to change the wording across the whole repo.
"""

from pathlib import Path

# scripts/ lives at supporting-material/scripts, so the repo root is two up.
ROOT = Path(__file__).resolve().parents[2]

# The single line of caution text (without the "> " blockquote prefix).
CAUTION_TEXT = (
    "This repository is a workspace copy for navigation, drafting, version "
    "control and collaboration. It is not the official statement of government "
    "policy and must not be relied on as such."
    "For the authoritative version, see the UK digital verification services trust framework 1.0 on GOV.UK. Test Caution Block."
)

LINE1 = "> [!CAUTION]"
LINE2 = f"> {CAUTION_TEXT}"

# Paths to leave alone (tooling, not workspace content).
SKIP_PREFIXES = (
    ".github/",
    "docs-site/README.md",
    "docs-site/node_modules/",
    "TEMPLATE-USAGE.md",
)


def should_skip(rel_path: str) -> bool:
    return any(rel_path == p or rel_path.startswith(p) for p in SKIP_PREFIXES)


def update_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()

    # If the file already opens with the caution marker, drop the old
    # marker + text lines and keep the rest; otherwise keep everything.
    if lines and lines[0].strip() == LINE1:
        body = lines[2:]
    else:
        body = lines

    # Remove any leading blank lines so we never stack blank lines.
    while body and body[0].strip() == "":
        body.pop(0)

    new_lines = [LINE1, LINE2, ""] + body
    updated = "\n".join(new_lines)
    if original.endswith("\n"):
        updated += "\n"

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if should_skip(rel):
            continue
        if update_file(path):
            print(f"updated: {rel}")
            changed += 1
    print(f"\nDone. {changed} file(s) changed.")


if __name__ == "__main__":
    main()
