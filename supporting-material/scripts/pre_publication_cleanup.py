#!/usr/bin/env python3
"""
Two pre-publication cleanups on the trust-framework-1.0/ section files:

1. Rewrite cross-file anchor references so they resolve on GitHub.
   - A reference `[text](#section-N[_M[_P]])` or `[text](#part-N)` is looked up.
   - If the target anchor lives in the SAME file as the reference, leave as-is.
   - If the target anchor lives in a DIFFERENT file, rewrite to
     `[text](relative/path/target.md#anchor-id)`.
   - Visible link text is never touched; only the link TARGET is rewritten.

2. Convert `$CTA` delimiter pairs to standard Markdown blockquotes.
   - `$CTA` is a GOV.UK-renderer marker that displays content as a call-to-action
     box. GitHub has no equivalent, so `$CTA` appears as literal text.
   - This pass removes both delimiter lines and prefixes every non-empty line
     between them with `> `, turning the whole example into a blockquote that
     renders as a visually distinct panel on GitHub.
"""
import os
import re
from pathlib import Path

ROOT = Path("/home/claude/repo/dvs-trust-framework/trust-framework-1.0")

# -----------------------------------------------------------------------------
# Pass 1 -- Build an anchor lookup: anchor_id -> (relative file path under ROOT)
# -----------------------------------------------------------------------------
anchor_re = re.compile(r'<a id="([A-Za-z0-9_-]+)"></a>')
anchor_map = {}  # anchor_id -> Path relative to ROOT

for md in sorted(ROOT.rglob("*.md")):
    rel = md.relative_to(ROOT)
    text = md.read_text(encoding="utf-8")
    for m in anchor_re.finditer(text):
        anchor_id = m.group(1)
        if anchor_id in anchor_map and anchor_map[anchor_id] != rel:
            print(f"  WARN: duplicate anchor {anchor_id} in {anchor_map[anchor_id]} and {rel}")
        anchor_map[anchor_id] = rel

# Part READMEs aren't anchor targets inside the publication source, but the
# publication text uses [...](#part-3) to refer to Part 3 of the document.
# Map part-N anchors to the part README.
part_readme_map = {
    "part-1": Path("part-1/README.md"),
    "part-2": Path("part-2/README.md"),
    "part-3": Path("part-3/README.md"),
    "part-4": Path("part-4/README.md"),
}
for anchor_id, relpath in part_readme_map.items():
    if anchor_id not in anchor_map:
        anchor_map[anchor_id] = relpath

print(f"Anchor map built: {len(anchor_map)} anchors.")

# -----------------------------------------------------------------------------
# Pass 2 -- Rewrite cross-file references
# -----------------------------------------------------------------------------
# Markdown link with a fragment-only target: e.g. [text](#section-14)
link_re = re.compile(r'(\]\()(#[A-Za-z0-9_-]+)(\))')

total_refs = 0
cross_file_rewrites = 0
same_file_unchanged = 0
unresolved = 0

for md in sorted(ROOT.rglob("*.md")):
    src_rel = md.relative_to(ROOT)
    src_dir = md.parent
    text = md.read_text(encoding="utf-8")
    changed = [False]

    def replace(match, _src_rel=src_rel, _src_dir=src_dir, _changed=changed):
        global total_refs, cross_file_rewrites, same_file_unchanged, unresolved
        total_refs += 1
        anchor_id = match.group(2)[1:]  # strip leading '#'
        target_rel = anchor_map.get(anchor_id)
        if target_rel is None:
            print(f"  WARN: unresolved anchor {anchor_id} in {_src_rel}")
            unresolved += 1
            return match.group(0)
        if target_rel == _src_rel:
            same_file_unchanged += 1
            return match.group(0)
        target_abs = ROOT / target_rel
        rel_path = os.path.relpath(target_abs, _src_dir).replace(os.sep, "/")
        _changed[0] = True
        cross_file_rewrites += 1
        return f"{match.group(1)}{rel_path}#{anchor_id}{match.group(3)}"

    new_text = link_re.sub(replace, text)

    if changed[0]:
        md.write_text(new_text, encoding="utf-8")

print(f"\nLink rewrite summary:")
print(f"  total references examined : {total_refs}")
print(f"  cross-file rewrites       : {cross_file_rewrites}")
print(f"  same-file (unchanged)     : {same_file_unchanged}")
print(f"  unresolved                : {unresolved}")

# -----------------------------------------------------------------------------
# Pass 3 -- $CTA block -> blockquote conversion
# -----------------------------------------------------------------------------
# Walk each file line-by-line. When we hit `$CTA` alone on a line, enter CTA
# mode and drop that line. While in CTA mode, prefix non-empty lines with '> '
# and blank lines with '>' (so the blockquote continues across blanks). When
# we see the next `$CTA`, drop it and exit CTA mode.

cta_files_touched = 0
cta_blocks_converted = 0

for md in sorted(ROOT.rglob("*.md")):
    lines = md.read_text(encoding="utf-8").split("\n")
    out = []
    in_cta = False
    this_file_blocks = 0
    for line in lines:
        if line.strip() == "$CTA":
            if in_cta:
                # closing delimiter
                in_cta = False
                this_file_blocks += 1
            else:
                # opening delimiter
                in_cta = True
            continue
        if in_cta:
            if line == "":
                out.append(">")
            else:
                out.append(f"> {line}")
        else:
            out.append(line)
    if this_file_blocks:
        md.write_text("\n".join(out), encoding="utf-8")
        cta_files_touched += 1
        cta_blocks_converted += this_file_blocks
        print(f"  {md.relative_to(ROOT)}  ({this_file_blocks} CTA blocks)")

print(f"\n$CTA conversion summary:")
print(f"  files touched       : {cta_files_touched}")
print(f"  blocks converted    : {cta_blocks_converted}")
