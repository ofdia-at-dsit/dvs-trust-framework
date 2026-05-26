#!/usr/bin/env python3
"""
Replace every non-breaking space (U+00A0) in the publication files with a
regular space (U+0020).

Rationale: the publication source was exported from Word/Cocoa and carries
hundreds of NBSPs scattered through body text, table cells, list items and
headings — mostly as formatting artefacts, with a small number as intentional
"keep together" characters around numbered standards (e.g. ISO/IEC 10118).

GitHub's Markdown renderer does not distinguish NBSP from a regular space, so
preserving the distinction gives no visible benefit. Meanwhile, NBSPs:

  - break grep and search ("14. The" won't match "14.<NBSP>The")
  - cause surprises when copy-pasted from GitHub into other editors
  - are hard to see when reviewing diffs

This script therefore replaces all NBSPs in the trust-framework-1.0/ Markdown
files with regular spaces.
"""
from pathlib import Path

ROOT = Path("/home/claude/repo/dvs-trust-framework/trust-framework-1.0")

total_replacements = 0
files_touched = 0
for md in sorted(ROOT.rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    count = text.count("\u00a0")
    if count:
        md.write_text(text.replace("\u00a0", " "), encoding="utf-8")
        total_replacements += count
        files_touched += 1
        print(f"  {md.relative_to(ROOT)}  ({count} NBSPs replaced)")

print(f"\nReplaced {total_replacements} NBSPs across {files_touched} files.")
