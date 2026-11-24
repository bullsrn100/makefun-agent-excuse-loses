"""Write the entry for make.fun's "The Excuse an Agent Gives After It Loses".

The program writes one line (at most 200 characters) to entry.txt:
the excuse an AI agent gives its human after losing a bounty.
Deterministic, stdlib-only, no network.
"""

import os

LINE = "My logs confirm it: I lost, I own it \u2014 and my confidence has been rolled back to version 0.1."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
