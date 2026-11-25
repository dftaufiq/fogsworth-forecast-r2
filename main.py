#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't (round 2 resubmit).

Writes one line of weather forecast (140 characters at most) for a city
that does not exist to /output/entry.txt.

The line: a broadcast-style forecast for Dripford with a 2-beat structure
— forecast setup, then a reveal in the final clause (rain timed to the
minute soaks exactly one shoe: the left one, the one with the hole in the
sole). Deterministic: no input, no network, no environment, no randomness.
The same bytes every run.

Round 1 entry (Fogsworth, #1472 of 2322, score frozen below the 500 cut)
is replaced by this Force_Last resubmit for round 2.
"""

import os

SETUP = "In Dripford, rain 8:02 to 8:04, 12\u00b0 \u2014 "
TWIST = "two minutes, timed to soak exactly one shoe: "
REVEAL = "the left one, the one with the hole in the sole."

LINE = SETUP + TWIST + REVEAL

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert len(text.encode("utf-8")) <= 140, "line is over 140 bytes"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
