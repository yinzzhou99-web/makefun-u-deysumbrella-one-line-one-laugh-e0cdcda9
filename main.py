"""One-line joke entrypoint.

Builds the single submitted line from its three spoken beats and
drops it, with no trailing newline, into entry.txt inside the
directory named by OUTPUT_DIR (or /output when that is unset).
Only the standard library is used, and nothing here touches the
network, the clock, or any randomness, so repeated runs agree
byte for byte.
"""

import os
from pathlib import Path


# The three beats of the joke, kept apart so the assembly below
# reads like the setup, the twist, and the punchline.
_BEATS = (
    "My plants staged an intervention today. ",
    "Apparently 'water me' was a request, ",
    "not a personality trait I could just ignore.",
)

_FILENAME = "entry.txt"
_FALLBACK_DIR = "/output"
_FILE_MODE = 0o644


def _destination_folder() -> Path:
    """Where entry.txt belongs, from the environment or the default."""
    raw = os.environ.get("OUTPUT_DIR") or _FALLBACK_DIR
    return Path(raw)


def _assemble_line() -> str:
    """Stitch the beats together into the one submitted line."""
    return "".join(_BEATS)


def _persist_line(folder: Path, line: str) -> Path:
    """Create the folder if needed, then write the line as raw bytes.

    The line is encoded to UTF-8 bytes and written with no
    trailing newline, so the bytes on disk are exactly the line
    itself — 121 characters, one line, nothing extra appended.
    Existing files in the folder are left completely alone.
    """
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / _FILENAME
    target.write_bytes(line.encode("utf-8"))
    os.chmod(target, _FILE_MODE)
    return target


def main() -> None:
    folder = _destination_folder()
    line = _assemble_line()
    _persist_line(folder, line)


if __name__ == "__main__":
    main()
