#!/usr/bin/env python3
"""Inspect selected component placements and signal nodes in a GenCAD 1.4 text file.

This read-only utility prints records from the input boardview. It does not
modify the input, decode proprietary data, or establish which physical PCB a
drawing represents.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

TARGETS = ("U3D1", "R7R2", "R4E5", "R4E7", "R4E23", "R4E1", "U3D6")
COMPONENT_RE = re.compile(r"^COMPONENT\s+(\S+)")
NODE_RE = re.compile(r"^NODE\s+(\S+)\s+(\S+)")


def parse_gencad(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if "$HEADER" not in text or not re.search(r"(?m)^GENCAD 1\.4\s*$", text):
        raise ValueError("input is not identified as GenCAD 1.4 text")
    components: dict[str, dict[str, str]] = {}
    nets: dict[str, list[dict[str, str]]] = {}
    section = ""
    current_component: str | None = None
    current_net: str | None = None

    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("$") and not line.startswith("$END"):
            section = line
            current_component = None
            current_net = None
            continue
        if line.startswith("$END"):
            section = ""
            current_component = None
            current_net = None
            continue

        if section == "$COMPONENTS":
            match = COMPONENT_RE.match(line)
            if match:
                current_component = match.group(1)
                components[current_component] = {}
                continue
            if current_component:
                key, _, value = line.partition(" ")
                if key in {"PLACE", "LAYER", "ROTATION", "SHAPE", "DEVICE"}:
                    components[current_component][key.lower()] = value.strip()

        elif section == "$SIGNALS":
            if line.startswith("SIGNAL "):
                current_net = line.split(None, 1)[1]
            elif line.startswith("NODE ") and current_net:
                match = NODE_RE.match(line)
                if match:
                    ref, pin = match.groups()
                    nets.setdefault(ref, []).append({"pin": pin, "net": current_net})

    return {"components": components, "nets": nets}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("boardview", type=Path, help="GenCAD 1.4 text file to inspect")
    parser.add_argument(
        "--component",
        action="append",
        dest="components",
        help="component reference to include; repeat for multiple references",
    )
    args = parser.parse_args()
    if not args.boardview.is_file():
        parser.error(f"not a file: {args.boardview}")

    parsed = parse_gencad(args.boardview)
    selected = args.components or list(TARGETS)
    missing = [ref for ref in selected if ref not in parsed["components"]]
    result = {
        "input": args.boardview.name,
        "format": "GenCAD 1.4 text (not independently revision-identified)",
        "components": {
            ref: {
                **parsed["components"].get(ref, {}),
                "nets": parsed["nets"].get(ref, []),
            }
            for ref in selected
            if ref in parsed["components"]
        },
        "missing_components": missing,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
