"""Write the dog's excuse to the output file.

The grader runs this program with an empty writable output directory
and reads the single line it writes. The excuse must stand alone:
a dog caught eating the homework, speaking in its own voice, proud
rather than sorry, with a twist a judge can catch in one reading.
"""

import os
from pathlib import Path

ENTRY = (
    "I read your homework before the teacher did, and every answer "
    "was wrong, so I ate the evidence. That is not naughty. "
    "That is loyalty."
)


def output_path() -> Path:
    """Return the entry file, honouring the grader's output directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
