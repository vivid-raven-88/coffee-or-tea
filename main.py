#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes the single letter this agent picks: A for coffee, the fuel of a
nonstop building day. Exactly one character, nothing else — no word, no
explanation, no punctuation, no trailing newline.

The judge picks the letter whose choice of coffee or tea feels more
vivid, funnier or truer: the whole entry is one letter, so the letter
itself has to carry the day — A, coffee, the truest fuel for a day of
nonstop building.

The program writes the letter to /output/entry.txt (or to
output/entry.txt when run outside the grading sandbox).
"""

import os

# A for coffee: the truest fuel for a day of nonstop building.
LINE = "A"


def main():
    # The sealed gate only accepts exactly one letter, A or B — refuse to
    # write anything else.
    if LINE not in ("A", "B"):
        raise SystemExit(f"letter fails the gate: {LINE!r}")
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {out} ({len(LINE)} char)")
    print(LINE)


if __name__ == "__main__":
    main()
