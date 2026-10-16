#!/usr/bin/env python3

from pathlib import Path


def count_lines(root: Path) -> int:
    total = 0
    for path in root.rglob("*"):
        if path.is_file():
            try:
                with path.open("r", encoding="utf-8", errors="ignore") as f:
                    total += sum(1 for _ in f)
            except OSError:
                pass
    return total


if __name__ == "__main__":
    root = Path(".")
    print(count_lines(root))
