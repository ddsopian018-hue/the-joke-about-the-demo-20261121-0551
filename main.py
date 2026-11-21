#!/usr/bin/env python3
"""Write one deterministic one-line joke about working beside AI coding agents.

The joke lives in a single constant; the program writes it verbatim to
/output/entry.txt (creating /output if needed). No network, no randomness,
stdlib only, so every run produces byte-identical output.
"""

from pathlib import Path

JOKE = "My agent fixed the demo crash live \u2014 then crashed it again, faster, with better comments."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
