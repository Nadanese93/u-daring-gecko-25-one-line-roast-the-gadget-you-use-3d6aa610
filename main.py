"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 stdlib only. No network, no randomness.
"""

import os

MAX_CHARS = 200

LINE = "My robot vacuum has mapped my house 400 times and still attacks the same rug like it's personal."

def main():
    if not LINE:
        raise ValueError("roast line is empty")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("roast line must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError("roast line exceeds 200 characters")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
