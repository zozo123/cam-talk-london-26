#!/usr/bin/env python3
"""Build PRESENTER-GUIDE.md from the speaker notes in talk.tex and the files it includes and check per-slide pacing.

Each main slide's \\note{} starts with an [m:ss] cue; backup notes start with [backup].
`--check` exits non-zero if any main slide exceeds MAX_WPM or the total leaves the window.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from texflat import flatten

MAX_WPM = 125
TOTAL_WINDOW_S = (35 * 60, 45 * 60)
ROOT = Path(__file__).resolve().parent.parent


def frames(tex):
    for m in re.finditer(r"\\begin\{frame\}(\[[^\]]*\])?(\{(?P<title>(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\})?(?P<body>.*?)\\end\{frame\}", tex, re.S):
        body = m.group("body")
        note = re.search(r"\\note\{\[(?P<cue>[^\]]+)\]\s*(?P<text>.*?)\}\s*$", body.strip(), re.S)
        if not note:
            continue
        title = m.group("title") or ""
        if not title:
            head = re.search(r"\\bfseries ((?:[^\\}]|\\\\)+)", body)
            title = " ".join(head.group(1).replace("\\\\", " ").split()) if head else "Title"
        title = re.sub(r"\\(ev|surf)\{[^{}]*(\{[^{}]*\}[^{}]*)*\}", "", title)
        title = title.replace("$n$", "n").replace("\\", "").strip()
        yield title, note.group("cue"), " ".join(note.group("text").split())


def plain(text):
    text = re.sub(r"\\[a-zA-Z]+\*?(\{([^{}]*)\})?", lambda m: m.group(2) or "", text)
    return text.replace("``", '"').replace("''", '"').replace("~", " ").replace("$", "")


def main():
    tex = flatten(ROOT / "talk.tex")
    rows, backups, total = [], [], 0
    for title, cue, text in frames(tex):
        text = plain(text)
        if cue == "backup":
            backups.append((title, text))
            continue
        mins, secs = cue.split(":")
        dur = int(mins) * 60 + int(secs)
        words = len(text.split())
        rows.append((title, dur, total, words, 60 * words / dur, text))
        total += dur
    fast = [r for r in rows if r[4] > MAX_WPM]
    words = sum(r[3] for r in rows)
    out = ["# Presenter guide: Forkable Sandboxes", "",
           "**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.", "",
           f"Generated from the notes in `acts/` by `tools/presenter_guide.py`. {len(rows)} main slides, {len(backups)} end-matter pages. "
           f"Planned talk: **{total // 60}:{total % 60:02d}**, {words} spoken words, {60 * words / total:.0f} wpm average, "
           f"peak {max(r[4] for r in rows):.0f} wpm. These are planned cues, not a measured rehearsal.", "",
           "## Run of show", "", "| # | Slide | Cue | Clock | Words | wpm |", "|---|---|---|---|---|---|"]
    for i, (title, dur, start, w, wpm, _) in enumerate(rows, 1):
        end = start + dur
        out.append(f"| {i} | {title} | {dur // 60}:{dur % 60:02d} | {start // 60}:{start % 60:02d}-{end // 60}:{end % 60:02d} | {w} | {wpm:.0f} |")
    out += ["", "## Script", ""]
    for i, (title, dur, start, w, wpm, text) in enumerate(rows, 1):
        out += [f"### {i:02d}. {title}", "", f"*{dur // 60}:{dur % 60:02d}, starts at {start // 60}:{start % 60:02d}*", "", text, ""]
    out += ["## End matter (untimed)", ""]
    for i, (title, text) in enumerate(backups, 1):
        out += [f"### E{i}. {title}", "", text, ""]
    (ROOT / "PRESENTER-GUIDE.md").write_text("\n".join(out))
    print(f"{len(rows)} main slides, total {total // 60}:{total % 60:02d}, {words} words, peak {max(r[4] for r in rows):.0f} wpm")
    for i, r in enumerate(rows, 1):
        print(f"{i:2d} {r[1]:4d}s {r[3]:4d}w {r[4]:5.0f} wpm  {r[0][:60]}")
    if "--check" in sys.argv:
        ok = not fast and TOTAL_WINDOW_S[0] <= total <= TOTAL_WINDOW_S[1]
        if not ok:
            print("PACING CHECK FAILED:", [r[0] for r in fast], total)
            sys.exit(1)


if __name__ == "__main__":
    main()
