# GenCAD inspection utility

Run with Python 3.10 or later:

    python tools/inspect_gencad.py path/to/boardview.cad

The script reads GenCAD text and emits selected component placement fields and signal nodes as JSON. Use repeated --component REF options to select other references. It does not modify or upload the input file. Output describes the drawing only; it cannot identify the physical PCB revision or validate electrical equivalence.

The boardview used during this project is not included. This utility is MIT-licensed; see LICENSE.
