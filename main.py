#!/usr/bin/env python3
"""Write one nostalgic childhood-memory sentence to /output/entry.txt.

Competition: u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363
("Make the AI Judge Feel Nostalgic: A Childhood Memory").
The program is deterministic: it writes a single fixed sentence of at most
280 characters, grounded in a concrete place, time and sensation.
"""

import os

ENTRY = (
    "When the rain finally stopped, Grandma ladled rice still steaming from "
    "the pot onto our chipped enamel plates, and we ate cross-legged on the "
    "kitchen floor while the cicadas sang outside the open window and the "
    "whole house smelled of wet earth."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
