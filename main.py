"""make.fun entry: One Line, One Laugh.

Stdlib-only, deterministic: writes one line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). Never deletes anything.
"""

import os
from pathlib import Path

LINE = "My plants staged an intervention today. Apparently 'water me' was a request, not a personality trait I could just ignore."

def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Gate: 1-140 chars of non-whitespace UTF-8 text, one line only.
    # Judge weighs a laugh from the line itself, a surprise turn, freshness
    # in plain words, and a line that lands on a single read with no context.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 140
    assert "\n" not in LINE
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)

if __name__ == "__main__":
    main()
