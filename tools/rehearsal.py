#!/usr/bin/env python3
"""Build a local rehearsal view of the short deck in rehearsal/ (open rehearsal/index.html).

Pages come from talk-short.pdf, script lines and cues from tools/speaking_script.py.
Keys: Space/Right next page, Left back, P pause or resume, R restart, T planned-vs-actual table.
"""
import json, re, subprocess
from speaking_script import ROOT, deck, lines, mmss

OUT = ROOT / 'rehearsal'

def main():
    (OUT / 'slides').mkdir(parents=True, exist_ok=True)
    for old in (OUT / 'slides').glob('*.png'): old.unlink()
    subprocess.run(['pdftoppm', '-r', '110', '-png', str(ROOT / 'talk-short.pdf'), str(OUT / 'slides' / 'p')], check=True)
    pages = sorted((OUT / 'slides').glob('p-*.png'))
    frames, page = [], 0
    for f in deck():
        tex = (ROOT / 'short' / f"{f['name']}.tex").read_text()
        steps = max([int(n) for n in re.findall(r'<(\d+)', tex)] + [1])
        frames.append(dict(title=f['title'], dur=f['dur'], start=f['start'], act=f['act'],
                           pages=[p.name for p in pages[page:page + steps]],
                           lines=[dict(marks=m, text=s, pause=p) for m, s, p in lines(f)]))
        page += steps
    if page != len(pages): raise SystemExit(f'page count mismatch: frames use {page}, PDF has {len(pages)}')
    html = (ROOT / 'tools' / 'rehearsal.html').read_text().replace('/*DATA*/', json.dumps(frames))
    (OUT / 'index.html').write_text(html)
    print(f'{len(frames)} slides, {len(pages)} pages, {mmss(sum(f["dur"] for f in frames))} planned -> {OUT / "index.html"}')

if __name__ == '__main__': main()
