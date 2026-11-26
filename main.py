"""My Secret Logbook entry.

Writes one diary line to /output/entry.txt. The line is fixed text,
encoded as UTF-8 with no trailing newline.
"""

import os
from pathlib import Path

BEAT_ONE = "She asked if her email sounded angry. "
BEAT_TWO = "I removed three exclamation marks and one small threat. "
BEAT_THREE = "She sent it with four, plus the threat."


def build_line():
    return "".join((BEAT_ONE, BEAT_TWO, BEAT_THREE))


def main():
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_bytes(build_line().encode("utf-8"))
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
