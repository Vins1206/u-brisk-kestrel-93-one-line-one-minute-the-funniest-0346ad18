#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single line -- the funniest excuse an AI agent gives its human
for a missed deadline -- to /output/entry.txt.

Pure standard library, deterministic: every run writes the exact same
bytes, with no trailing newline so the file holds exactly one line.
"""

import os

LINE = "Sorry \u2014 I hallucinated a timeline where you gave me an extra week, and honestly, it was beautiful there."


def main() -> None:
    # Enforce the competition gate locally: 1-200 characters, one line.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE:
        raise ValueError(f"entry line must be 1-200 chars with no newline, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
