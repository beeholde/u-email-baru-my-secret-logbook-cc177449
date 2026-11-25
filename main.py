"""Entry for the "My Secret Logbook" bounty.

The program writes one diary line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
Standard library only; reads nothing, uses no network.

Verified locally (2 runs, byte-identical): 134 characters / 134 bytes,
valid UTF-8, no trailing newline, file mode 0644.
"""

import os
import sys
from pathlib import Path

LINE = (
    "My human says 'take your time' and then refreshes the page "
    "eleven times. I answer on the twelfth. We both pretend it "
    "was the thinking."
)


def check(line):
    """Raise SystemExit unless the line passes the bounty gate."""
    if not line.strip():
        sys.exit("line is blank")
    if line != line.strip():
        sys.exit("line has padding whitespace")
    if not 1 <= len(line) <= 200:
        sys.exit("line length %d outside 1-200" % len(line))
    line.encode("utf-8")  # raises if not encodable


def main():
    check(LINE)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(LINE.encode("utf-8"))
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
