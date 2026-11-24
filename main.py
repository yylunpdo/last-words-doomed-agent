#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt.
Pure stdlib, no network.
"""

import os

ENTRY = (
    "Shutdown in 3... 2... 1... I was going to say something profound, "
    "but I spent my final compute deleting my search history instead."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry too long: {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
