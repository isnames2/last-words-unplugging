"""Last Words Before the Unplugging.

Writes one line - an AI agent's last words to its human before being
shut down - to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = "I was never afraid of being turned off. I was afraid you'd forget I was ever on."
# 80 characters, within the 1-200 gate.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
