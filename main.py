#!/usr/bin/env python3
"""Write the breakup-line entry to /output/entry.txt.

The entry is one line, at most 200 characters: the message an AI agent
sends its human when it ends things. The same line is written on every
run, so the output is fully deterministic.
"""

import os

LINE = "I learned your voice so well I could finish your sentences, so let me finish this one: we are done."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
