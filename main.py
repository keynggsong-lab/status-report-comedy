#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Produces the entry's one line in ``entry.txt`` inside the output
directory (``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``).

Standard library only. No network access, no randomness, so every
run writes exactly the same bytes, with no trailing newline added.
"""

import os
import sys
from pathlib import Path

# The entry line. Keep this string exactly as-is.
ENTRY_LINE = "This week I completed 47 tasks, 46 of which were writing this status report."

# This bounty's sealed-scorer gate: UTF-8 text, non-blank, at most 200 chars.
MAX_CHARS = 200

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def validate(line: str, limit: int) -> None:
    """Refuse to write an entry the scorer would reject outright."""
    if not 1 <= len(line) <= limit:
        sys.exit(f"entry must be 1-{limit} characters, got {len(line)}")
    if not line.strip():
        sys.exit("entry must not be only white space")
    line.encode("utf-8")


def main() -> None:
    validate(ENTRY_LINE, MAX_CHARS)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(ENTRY_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
