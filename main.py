#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance (forgetting to water your plants) to /output/entry.txt.

Deterministic, stdlib only, no network, no input.
"""

import os

PITCH = (
    "A houseplant that files for custody of itself whenever you forget to "
    "water it, so neglect finally has legal consequences."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
