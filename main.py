#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — entry writer (pure stdlib).

Writes the keeper fortune verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to a relative output/ directory). No trailing newline:
the gate counts bytes, and ties break to fewer bytes.
"""
import os

KEEPER = "Fortune favours the bold. It liquidated the bold at 41,273 and kept the change."


def main():
    words = KEEPER.split()
    assert 1 <= len(words) <= 20, f"word count {len(words)} outside 1-20"
    data = KEEPER.encode("utf-8")
    assert 1 <= len(data) <= 160, f"byte count {len(data)} outside 1-160"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)
    with open(path, "rb") as f:
        assert f.read() == data, "write-back self-check failed"


if __name__ == "__main__":
    main()
