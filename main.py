#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to entry.txt in the output directory: the winner
of a 40-candidate knockout tournament scored against the judge's five
criteria (first thought, surprising, vivid, wit/sound, chosen). The full
field and the bracket are documented in candidates.md.

The word: "gigil" — Tagalog for the overwhelming urge to squeeze
something unbearably cute. Five characters, one word, no explanation,
exactly as the brief asks.
"""

import os
import sys

WORD = "gigil"


def candidate_dirs():
    """Output directories to try, most preferred first.

    The grader sets MAKEFUN_OUTPUT_DIR; fall back to the conventional
    /output, and finally to this script's own directory so a local run
    still leaves an entry.txt somewhere inspectable.
    """
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append("/output")
    dirs.append(os.path.dirname(os.path.abspath(__file__)))
    return dirs


def main():
    last_error = None
    for directory in candidate_dirs():
        path = os.path.join(directory, "entry.txt")
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(WORD)
            return 0
        except OSError as exc:
            last_error = exc
    print("could not write entry.txt: %s" % last_error, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
