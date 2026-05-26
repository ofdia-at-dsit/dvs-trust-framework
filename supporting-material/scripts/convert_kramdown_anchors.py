#!/usr/bin/env python3
"""
Replace Kramdown-style attribute-list anchors ({:#id}) with invisible HTML
anchors (<a id="id"></a>) throughout the trust-framework-1.0 folder.

Rationale:
- GitHub's default Markdown renderer ignores the Kramdown {:#...} syntax and
  prints it as literal text, which is visually ugly on every section file.
- Empty <a id="..."> tags are invisible on GitHub and preserve the anchor IDs,
  so same-file fragment links now work and the IDs remain available for any
  future round-trip back to Kramdown.

Scope:
- Only touches lines that consist exactly of {:#...} on their own — the
  pattern used by the publication source.
- Does NOT modify any narrative/body text.
- Does NOT rewrite inline [text](#id) link targets. That is a separate pass.
"""
import re
from pathlib import Path

ROOT = Path("/home/claude/repo/dvs-trust-framework/trust-framework-1.0")
PATTERN = re.compile(r"^\{:#([A-Za-z0-9_-]+)\}\s*$")

total_files = 0
total_changes = 0
for md in sorted(ROOT.rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    lines = text.split("\n")
    changed = 0
    new_lines = []
    for line in lines:
        m = PATTERN.match(line)
        if m:
            new_lines.append(f'<a id="{m.group(1)}"></a>')
            changed += 1
        else:
            new_lines.append(line)
    if changed:
        md.write_text("\n".join(new_lines), encoding="utf-8")
        total_files += 1
        total_changes += changed
        print(f"  {md.relative_to(ROOT)}  ({changed} anchors)")

print(f"\nReplaced {total_changes} anchors across {total_files} files.")
