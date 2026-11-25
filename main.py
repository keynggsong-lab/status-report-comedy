"""Status Report Comedy Sprint — entry program.

Writes one line, status-report line, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only, no network, fully deterministic: the same bytes every run.
"""

import os
from pathlib import Path

LINE = "This week I completed 47 tasks, 46 of which were writing this status report."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1-200 chars,
    # not only white space. Refuse to write an invalid entry.
    text = LINE
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    text.encode("utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
