"""Write the competition entry as deterministic UTF-8 bytes."""

import os
from pathlib import Path
import sys


ENTRY = (
    "// This sleep keeps payment retries from charging twice. "
    "If you make checkout faster, customers pay for it."
)


def main() -> int:
    if not ENTRY.strip() or len(ENTRY) > 200 or any(c in ENTRY for c in "\r\n"):
        print("Invalid entry: expected one nonblank line of at most 200 characters.", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
