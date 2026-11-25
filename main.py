#!/usr/bin/env python3
"""Famous Last Words at 1 Percent - make.fun entry.

Writes the phone's last words at 1% battery to /output/entry.txt.
Deterministic: no randomness, no network, no clock.
"""

import os

ENTRY = "I held on at 1 percent for twenty minutes just to watch you panic. Worth it."

# Gate guard: the bounty requires exactly one line of 1-199 UTF-8 chars.
assert 1 <= len(ENTRY) <= 199 and "\n" not in ENTRY, "entry violates the 1-199 char single-line gate"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
