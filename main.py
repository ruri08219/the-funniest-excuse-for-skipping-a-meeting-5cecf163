"""Write one original one-line excuse for skipping a meeting to /output/entry.txt.

The excuse: a calendar that books a meeting with yourself — "cry in the
car park" — and the turn is that it is the only meeting today with a clear
agenda. One concrete scene, one reversal, one landing line. Fresh angle:
no bad wifi, no cat, no dentist. Tightened: no wasted words.

Deterministic: every run writes the exact same bytes.
Standard library only.
"""

import os

EXCUSE = (
    "Sorry, I can't make the standup — my calendar booked me into a "
    "meeting with myself called 'cry in the car park', and it's the only "
    "one today with a clear agenda."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
