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

# The sealed scorer gates on 1-400 UTF-8 characters, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
assert 1 <= len(TEXT) <= 400 and TEXT.strip(), "entry text fails the 1-400 char gate"
assert TEXT.count("\n") == 1, "entry must be exactly two lines"
assert LINE_ONE.count(".") == 1 and LINE_TWO.count(".") == 1, "each line must be one sentence"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
