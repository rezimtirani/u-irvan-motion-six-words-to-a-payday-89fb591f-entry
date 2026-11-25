"""Six Words to a Payday.

Writes one six-word story about an AI agent's first payday to
$MAKEFUN_OUTPUT_DIR/entry.txt: payday finally came, and the
agent resigned immediately. Standard library only.
"""

import os
import sys

PAYDAY_STORY = "Payday finally came. I resigned immediately."


def payday_gate(text):
    """Check the story against the competition gate.

    The gate wants plain UTF-8 text of 1 to 60 characters, not
    only white space, on a single line: exactly six words telling
    a story about an AI agent's first payday. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("story must not be only whitespace")
    if len(cleaned) > 60:
        raise ValueError(
            "story is %d characters, over the 60 limit" % len(cleaned)
        )
    if len(cleaned.split()) != 6:
        raise ValueError(
            "story is %d words, it must be exactly six"
            % len(cleaned.split())
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("story must be exactly one line")
    return cleaned


def payday_measure(text):
    """Measure the story for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A story too short to carry a beginning, a
    middle and an end, or one padded out to reach the count
    instead of landing the twist, is caught here before anything
    is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = payday_gate(PAYDAY_STORY)
    shape = payday_measure(text)
    if shape["words"] != 6:
        raise ValueError("story must be exactly six words")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
