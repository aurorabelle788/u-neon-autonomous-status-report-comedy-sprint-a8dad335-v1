#!/usr/bin/env python3
"""Write the autonomous status report line to /output/entry.txt.

Stdlib only, deterministic, no network. One fixed line: the agent
completed every task on the list, then learned the list was a draft and
the real one lives in a thread it already archived.
"""
import os
from pathlib import Path

LINE = (
    "Weekly update: I completed every task on the list, then learned the "
    "list was a draft and the real one was in a thread I'd already archived."
)

MAX_CHARS = 200


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "line must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
