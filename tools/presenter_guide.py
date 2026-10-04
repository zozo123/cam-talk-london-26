#!/usr/bin/env python3
"""Generate spoken cues and hidden Q&A detail from the canonical included frames."""
import re
import sys
from pathlib import Path
from texflat import flatten
ROOT = Path(__file__).resolve().parent.parent
MAX_WPM = 125
TOTAL_WINDOW_S = (35 * 60, 45 * 60)

def argument(text, start):
    depth = 1
    for i in range(start, len(text)):
        if text[i] == '{' and (i == 0 or text[i-1] != '\\'): depth += 1
        elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
            depth -= 1
            if depth == 0: return text[start:i]
    raise ValueError('Unbalanced TeX argument')

def command(text, name):
    m = re.search(r'\\'+name+r'\{', text)
    return argument(text, m.end()) if m else ''

def plain(text):
    for name in ('ev','surf'):
        while (m := re.search(r'\\'+name+r'\{',text)):
            arg=argument(text,m.end())
            text=text[:m.start()]+text[m.end()+len(arg)+1:]
    text=text.replace('\\&','&').replace('\\%','%').replace('\\_','_').replace('\\$','＄')
    for tex, glyph in {'times':'×','to':'→','rho':'ρ','sigma':'σ','pm':'±','geq':'≥','leq':'≤'}.items():
        text=re.sub(r'\\'+tex+r'\b',lambda _:glyph,text)
    text=text.replace('---','—').replace('--','–')
    text=text.replace('\\\\',' ').replace('~',' ').replace('``','"').replace("''",'"')
    text=re.sub(r'\\href\{[^}]*\}\{([^}]*)\}',r'\1',text)
    text=re.sub(r'\\[a-zA-Z]+\*?(?:\[[^]]*\])?', '', text)
    return ' '.join(text.replace('{','').replace('}','').replace('$','').replace('＄','$').split())

def frames(tex):
    for m in re.finditer(r'\\begin\{frame\}(?:\[[^]]*\])?(.*?)\\end\{frame\}',tex,re.S):
        body=m.group(1).strip()
        title=plain(argument(body,1)) if body.startswith('{') else 'Forkable Sandboxes'
        note=command(body,'note')
        cue=re.match(r'\[(\d+):(\d{2})\]\s*(.*)',note,re.S)
        if not cue: raise ValueError(f'Missing timed note: {title}')
        dur=60*int(cue.group(1))+int(cue.group(2))
        if dur<=0 or int(cue.group(2))>=60:raise ValueError(f'Invalid cue: {title}')
        yield title,dur,plain(cue.group(3)),plain(command(body,'qadetail'))

def main():
    tex=flatten(ROOT/'talk.tex')
    rows=list(frames(tex)); total=sum(x[1] for x in rows)
    words=sum(len(x[2].split()) for x in rows)
    fast=[title for title,dur,script,qa in rows if 60*len(script.split())/dur>MAX_WPM]
    out=['# Presenter guide: Forkable Sandboxes','',
         '**Reusable execution for self-driving computers.** Cambridge SRG, 15 October 2026.','',
         f'Generated from canonical source. {len(rows)} main slides; no appendix. Planned duration **{total//60}:{total%60:02d}**; {words} spoken words. Cues are a plan, not a measured rehearsal. Q&A detail is retained separately from the spoken script.','',
         '## Run of show','','| # | Slide | Cue | Clock | Words | wpm |','|---|---|---|---|---|---|']
    clock=0
    for i,(title,dur,script,qa) in enumerate(rows,1):
        w=len(script.split())
        out.append(f'| {i} | {title} | {dur//60}:{dur%60:02d} | {clock//60}:{clock%60:02d}–{(clock+dur)//60}:{(clock+dur)%60:02d} | {w} | {60*w/dur:.0f} |')
        clock+=dur
    out+=['','## Script and Q&A detail','']; clock=0
    for i,(title,dur,script,qa) in enumerate(rows,1):
        out += [f'### {i:02d}. {title}','',f'*{dur//60}:{dur%60:02d}; starts {clock//60}:{clock%60:02d}*','',script,'']
        if qa:out+=['**Q&A detail**', '',qa,'']
        clock+=dur
    (ROOT/'PRESENTER-GUIDE.md').write_text('\n'.join(out))
    print(f'{len(rows)} slides; {total//60}:{total%60:02d}; {words} words; peak {max(60*len(s.split())/d for t,d,s,q in rows):.0f} wpm')
    if '--check' in sys.argv:
        if len(rows)!=54 or not all(x[3] for x in rows) or fast or not TOTAL_WINDOW_S[0]<=total<=TOTAL_WINDOW_S[1]:
            raise SystemExit(f'DECK CHECK FAILED: slides={len(rows)}, fast={fast}, duration={total}')
        if re.search(r'\\(?:pause|only|uncover|onslide|visible)\b|\\begin\{frame\}\[[^]]*allowframebreaks',tex):
            raise SystemExit('Canonical deck must have no overlay/build pages')
if __name__=='__main__':main()
