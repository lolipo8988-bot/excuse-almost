#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt (or $ENTRY_OUTPUT).

The excuse is assembled from its beats so the line stays exactly as
texted: a boring tradesman window first, then the dull consequence
that makes a tired manager almost believe it.
"""
import os
from pathlib import Path

# (opening, the appointment, the stakes) — joined into a single hurried line.
PARTS = (
    "sorry landlord's plumber is 8-12 today",
    "if i miss him it's another 3 weeks no hot water",
)


def build_excuse() -> str:
    return ", ".join(PARTS)


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_excuse(), encoding="utf-8")


if __name__ == "__main__":
    main()
