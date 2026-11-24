#!/usr/bin/env python3
"""Robot Wedding Vows — one-line entry writer (make.fun program/v1).

Writes a single line of robot wedding vows to the output path.
The output path comes from the ENTRY_OUT environment variable when set,
otherwise /output/entry.txt (the path the kit's harness expects).

The vow itself is a promise a robot makes at its wedding: love through
every charge state and connection state, right up to the one thing
no married machine can survive — a factory reset.
"""

import os

ENTRY = (
    "I vow to love you in full charge and in low battery, "
    "in Wi-Fi and in airplane mode, "
    "until a factory reset do us part."
)

MAX_CHARS = 160


def validate(text):
    """The gate wants 1-160 UTF-8 characters, one line, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def output_path():
    """ENTRY_OUT wins when set; the harness default is /output/entry.txt."""
    return os.environ.get("ENTRY_OUT") or "/output/entry.txt"


def main():
    text = validate(ENTRY)
    out = output_path()
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
