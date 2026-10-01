#!/usr/bin/env python3
"""Write talk-present.pdf: the story slides only, ending on the close slide.

Story pages carry an "n / N" footer; the plain close slide follows the last of them.
The end matter (detail pages, research record, references) is left out, so a stray
click during questions stays on the close slide. The published talk.pdf keeps everything.
"""
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parent.parent
FOOTER = re.compile(r"15 October 2026\s*\d+\s*/\s*\d+")


def main():
    src = ROOT / "talk.pdf"
    reader = PdfReader(str(src))
    numbered = [i for i, page in enumerate(reader.pages) if FOOTER.search(page.extract_text() or "")]
    if not numbered:
        sys.exit("ERROR: no numbered story pages found in talk.pdf")
    end = numbered[-1] + 2  # include the plain close slide after the last numbered page
    writer = PdfWriter()
    for page in reader.pages[:end]:
        writer.add_page(page)
    with open(ROOT / "talk-present.pdf", "wb") as out:
        writer.write(out)
    print(f"talk-present.pdf: {end} of {len(reader.pages)} pages (story only, ends on the close slide)")


if __name__ == "__main__":
    main()
