#!/usr/bin/env python3
"""
Replace U+00A0 NON-BREAKING SPACE with U+0020 SPACE inside Markdown heading
lines only (lines whose first non-whitespace character is '#').

Body text is left alone, because some body NBSPs are deliberate typographic
spacers (for example `ISO/IEC\u00a018370` where the NBSP keeps the standard
name together on one line) while others are artefacts. That distinction
needs OfDIA's view, so the narrower cleanup runs in headings only.

This is idempotent — re-running it makes no further changes once headings
are NBSP-free.
"""
from pathlib import Path

ROOT = Path("/home/claude/repo/dvs-trust-framework/trust-framework-1.0")
NBSP = "\u00a0"

total_replaced = 0
files_touched = 0
for md in sorted(ROOT.rglob("*.md")):
    lines = md.read_text(encoding="utf-8").split("\n")
    this_file = 0
    out_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#") and NBSP in line:
            n = line.count(NBSP)
            new_line = line.replace(NBSP, " ")
            out_lines.append(new_line)
            this_file += n
        else:
            out_lines.append(line)
    if this_file:
        md.write_text("\n".join(out_lines), encoding="utf-8")
        files_touched += 1
        total_replaced += this_file
        print(f"  {md.relative_to(ROOT)}  ({this_file} heading NBSPs replaced)")

print(f"\nReplaced {total_replaced} NBSPs across {files_touched} files (headings only).")
