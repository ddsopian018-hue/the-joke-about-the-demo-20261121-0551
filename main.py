#!/usr/bin/env python3
"""Write one deterministic one-line joke about working beside AI coding agents.

The joke lives in a single constant; the program writes it verbatim to
/output/entry.txt (creating /output if needed). No network, no randomness,
stdlib only, so every run produces byte-identical output.
"""

import sys
from pathlib import Path

JOKE = "My agent fixed the demo crash live \u2014 then crashed it again, faster, with better comments."

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CODE_POINTS = 280


def validate_joke(joke: str) -> None:
    """Fail loudly if the joke ever violates the one-line entry gate."""
    if not joke.strip():
        sys.exit("error: joke must not be empty or whitespace-only")
    if "\n" in joke or "\r" in joke:
        sys.exit("error: joke must be a single line (no newline characters)")
    if len(joke) > MAX_CODE_POINTS:
        sys.exit(
            f"error: joke is {len(joke)} code points, over the "
            f"{MAX_CODE_POINTS} code-point limit"
        )


def main() -> None:
    validate_joke(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
