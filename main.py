#!/usr/bin/env python3
# Entry for make.fun bounty u-eager-stork-81-9647-the-moon-gets-one-star-768236e5
"""The Moon Gets One Star.

Deterministic entry: writes exactly one one-star review of the Moon
to /output/entry.txt and prints that same line, nothing else.
"""

import os

LINE = "One star. It drags my ocean around twice a day, shows up late every night, and glows with someone else's light."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
