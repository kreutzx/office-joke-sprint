import os

LINE = (
    "Our CEO said 'we're a family' 14 times this quarter; families don't "
    "usually schedule the layoffs for Friday."
)


def main():
    # Office joke; the gate allows at most 200 characters; this line is 108.
    assert 1 <= len(LINE.strip()) <= 200, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
