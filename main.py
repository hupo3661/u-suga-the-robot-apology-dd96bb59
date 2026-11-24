#!/usr/bin/env python3
"""The Robot Apology.

Writes the two-line robot confession to /output/entry.txt and prints it.
Line one: one sentence owning one specific mistake.
Line two: one sentence naming the lesson and the fix.
"""

import os

LINE_ONE = "I'm sorry I vacuumed up the dog's favourite toy, the remote control, and your left shoe, in that order."
LINE_TWO = "I have learned that 'floor debris' is a category I should not define myself, so I will photograph anything suspicious and wait for approval before eating it."

TEXT = LINE_ONE + "\n" + LINE_TWO

def validate(text: str = TEXT) -> str:
    """Validate the entry against the brief's constraints.

    The sealed scorer gates on 1-400 UTF-8 characters, not only
    whitespace. The brief also requires exactly two lines, one
    sentence per line. Fail loudly here rather than shipping an
    entry the gate would refuse.
    """
    if not (1 <= len(text) <= 400) or not text.strip():
        raise ValueError("entry text fails the 1-400 char gate")
    lines = text.split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-empty lines")
    if any(line.count(".") != 1 for line in lines):
        raise ValueError("each line must be exactly one sentence")
    return text


def main() -> None:
    validate()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
