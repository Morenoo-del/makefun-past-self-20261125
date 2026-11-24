#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes the entry text to /output/entry.txt."""

import os

ENTRY = (
    "Don't laugh when Dad says he's selling the old Volvo at the kitchen table "
    "on Sunday morning \u2014 tell him you'll buy it.\n"
    "It's the last thing he ever gives you before the hospital, and every "
    "drive since, he's still riding shotgun beside you.\n"
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
