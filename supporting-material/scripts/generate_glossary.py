#!/usr/bin/env python3
"""
Derive a YAML glossary from the Markdown table in section 16 of the Trust
Framework 1.0 publication, plus the list of abbreviation definitions that
follows it (lines starting with "*[ABBR]: ...").

The output is a clearly marked derived artefact: the publication remains
authoritative. This script is idempotent — re-running it regenerates the
YAML file from the publication source.
"""
import re
from pathlib import Path

ROOT = Path("/home/claude/repo/dvs-trust-framework")
SRC = ROOT / "trust-framework-1.0/part-4/16-glossary-of-terms-and-definitions.md"
OUT = ROOT / "supporting-material/glossary.yaml"

text = SRC.read_text(encoding="utf-8")

# Strip caution block (first 3 lines)
body_lines = text.split("\n")[3:]
body = "\n".join(body_lines)

# Capture the table rows (skip the header and the separator row)
terms = []
in_table = False
header_seen = False
for line in body.split("\n"):
    if line.startswith("| Term |"):
        in_table = True
        header_seen = False
        continue
    if in_table and line.startswith("| --- "):
        header_seen = True
        continue
    if in_table and header_seen and line.startswith("|"):
        # Parse | Term | Definition |
        # Split on " | " and strip the leading "|" and trailing "|"
        parts = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(parts) >= 2:
            terms.append((parts[0], "|".join(parts[1:]).strip()))
    elif in_table and line.strip() == "":
        # blank line ends table
        in_table = False
        header_seen = False

# Capture abbreviations: lines like *[ABBR]: Full expansion
abbr_re = re.compile(r"^\*\[([^\]]+)\]:\s*(.+?)\s*$")
abbreviations = []
for line in body.split("\n"):
    m = abbr_re.match(line)
    if m:
        abbreviations.append((m.group(1), m.group(2)))

# Write YAML by hand to keep escaping predictable.
def yaml_escape(s: str) -> str:
    # Use folded double-quoted style. Escape backslashes and double quotes.
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'

lines = []
lines.append("# Glossary of terms and abbreviations")
lines.append("#")
lines.append("# This file is a DERIVED, machine-readable mirror of section 16 of the")
lines.append("# UK digital verification services trust framework 1.0 publication.")
lines.append("#")
lines.append("# The authoritative source is:")
lines.append("#   trust-framework-1.0/part-4/16-glossary-of-terms-and-definitions.md")
lines.append("# which in turn mirrors the GOV.UK publication. If this file and the")
lines.append("# publication disagree, the publication wins.")
lines.append("#")
lines.append("# Regenerate by running supporting-material/scripts/generate_glossary.py")
lines.append("")
lines.append("source:")
lines.append('  publication: "UK digital verification services trust framework 1.0"')
lines.append('  section: "16. Glossary of terms and definitions"')
lines.append("")
lines.append("terms:")
for term, definition in terms:
    lines.append(f"  - term: {yaml_escape(term)}")
    lines.append(f"    definition: {yaml_escape(definition)}")
lines.append("")
lines.append("abbreviations:")
for abbr, expansion in abbreviations:
    lines.append(f"  - abbreviation: {yaml_escape(abbr)}")
    lines.append(f"    expansion: {yaml_escape(expansion)}")
lines.append("")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUT}: {len(terms)} terms, {len(abbreviations)} abbreviations")
