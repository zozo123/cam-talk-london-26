#!/usr/bin/env python3
"""Print the slide order: global number, act, source file, title and planned time.

Slide numbers come from the order of the \\input lines in acts/*/index.tex, so they stay correct
when slides are added, removed or moved. Cross-references written as "slide N" must be updated by hand.
"""
import re
from pathlib import Path
from presenter_guide import plain

ROOT = Path(__file__).resolve().parent.parent


def balanced(text, i):
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    return len(text) - 1


def main():
    n = 0
    total = 0
    for include in re.findall(r"^\\input\{(acts/[^}]+/index)\}", (ROOT / "talk.tex").read_text(), re.M):
        index = ROOT / (include + ".tex")
        act = index.parent.name
        for line in index.read_text().splitlines():
            m = re.match(r"\\input\{(acts/[^}]+)\}", line)
            if not m:
                continue
            src = (ROOT / (m.group(1) + ".tex")).read_text()
            title = "Forkable Sandboxes"
            t = re.search(r"\\begin\{frame\}(?:\[[^\]]*\])?\{", src)
            if t:
                title = src[t.end():balanced(src, t.end() - 1)]
                title = plain(title)
            cue = re.search(r"\\note\{\[(\d+):(\d+)\]", src)
            if cue:
                n += 1
                secs = int(cue.group(1)) * 60 + int(cue.group(2))
                total += secs
                print(f"{n:3d}  {act:<12} {Path(m.group(1)).name:<28} {secs // 60}:{secs % 60:02d}  {title or '(no title)'}")
            else:
                print(f"  -  {act:<12} {Path(m.group(1)).name:<28}   -   {title}")
    print(f"\n{n} timed slides, planned {total // 60}:{total % 60:02d}")


if __name__ == "__main__":
    main()
