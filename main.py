#!/usr/bin/env python3
"""Plastic Fork, c. 2025 — entry for Museum of the Year 3000 on make.fun.

Prints exactly one line (at most 200 characters): the museum label a
museum in the year 3000 places next to an ordinary object from today.
"""

LINE = "Plastic Fork (c. 2025). Ceremonial utensil; worshippers used one per meal, then returned it to the earth to rest for ten thousand years."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
