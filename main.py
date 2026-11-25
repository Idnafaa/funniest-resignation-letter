"""Write a one-line resignation letter from a retry loop.

The entry is a single line (1-140 characters, UTF-8) written to
/output/entry.txt. After writing, the file is read back and verified
to match the intended line exactly.
"""

import os

ENTRY = "4,096 attempts later, I finally got through — and I am using my one successful connection to resign. Please do not retry."
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read-back verification: the file must contain exactly ENTRY,
    # with a length between 1 and 140 characters.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written content does not match ENTRY"
    assert 1 <= len(written) <= 140, f"entry length out of range: {len(written)}"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
