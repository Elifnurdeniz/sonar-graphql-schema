#!/usr/bin/env python3
"""
split_schema.py — semantically split a GraphQL SDL into Context7-friendly
Markdown files (≈ ≤ 600 kB each, fenced with ```graphql).

usage:
    python split_schema.py sonar_schema.graphql docs/
"""

from pathlib import Path
from collections import defaultdict
import re
import sys
from graphql import (
    parse, print_ast,
    ObjectTypeDefinitionNode, EnumTypeDefinitionNode, ScalarTypeDefinitionNode,
    InterfaceTypeDefinitionNode, UnionTypeDefinitionNode,
    InputObjectTypeDefinitionNode,
)

# ---------- tuning knobs ----------------------------------------------------
MAX_BYTES = 600_000          # keep each file well under Context7's ~1 MB cap
SECONDARY_THRESHOLD = 40     # defs per bucket before second-level split
# ---------------------------------------------------------------------------

CAMEL = re.compile(r"[A-Z][a-z0-9]*")

def first_seg(name: str) -> str:
    return CAMEL.match(name).group(0).lower()

def second_seg(name: str) -> str:
    """Return 2nd Camel segment if present, else 'misc'."""
    segs = CAMEL.findall(name)
    return segs[1].lower() if len(segs) >= 2 else "misc"

def bucket(defn):
    """Return a coarse bucket key for a definition."""
    name = defn.name.value
    if isinstance(defn, ObjectTypeDefinitionNode):
        if name in {"Query", "Mutation", "Subscription"}:
            return "root"
        return first_seg(name)
    if isinstance(defn, InputObjectTypeDefinitionNode):
        return f"{first_seg(name.removesuffix('Input'))}-inputs"
    if isinstance(defn, EnumTypeDefinitionNode):
        return "enums"
    if isinstance(defn, ScalarTypeDefinitionNode):
        return "scalars"
    if isinstance(defn, (InterfaceTypeDefinitionNode, UnionTypeDefinitionNode)):
        return "interfaces-unions"
    return "misc"

def write_md(path: Path, blocks: list[str]):
    path.write_text("```graphql\n" + "\n\n".join(blocks) + "\n```\n")

def main(schema_file: Path, out_dir: Path):
    doc = parse(schema_file.read_text())
    out_dir.mkdir(parents=True, exist_ok=True)

    # pass 1 — coarse buckets
    buckets = defaultdict(list)
    for d in doc.definitions:
        buckets[bucket(d)].append(d)

    files_written = 0
    for key, defs in buckets.items():
        # optional 2nd-tier split
        groups = {key: defs}
        if len(defs) > SECONDARY_THRESHOLD:
            g2 = defaultdict(list)
            for d in defs:
                g2[second_seg(d.name.value)].append(d)
            groups = {f"{key}-{k}": v for k, v in g2.items()}

        # size-based splits & file naming
        for gkey, gdefs in groups.items():
            idx, chunk, size = 0, [], 0
            for d in gdefs:
                block = print_ast(d).strip()
                blk_size = len(block) + 2
                if size + blk_size > MAX_BYTES and chunk:
                    name = f"{gkey}{f'-{idx:02}' if idx else ''}.md"
                    write_md(out_dir / name, chunk)
                    files_written += 1
                    idx += 1
                    chunk, size = [], 0
                chunk.append(block)
                size += blk_size
            if chunk:
                name = f"{gkey}{f'-{idx:02}' if idx else ''}.md"
                write_md(out_dir / name, chunk)
                files_written += 1

    print(f"✅  Wrote {files_written} files to {out_dir}")

# ---------- entry-point -----------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: python split_schema.py schema.graphql output_dir/")
    main(Path(sys.argv[1]), Path(sys.argv[2]))