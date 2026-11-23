"""Office Jokes entry: write one office joke to /output/entry.txt."""

import os

JOKE = "The fastest reply-all in the company is 'please remove me from this thread' - sent to all 400 of us."


def main():
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
