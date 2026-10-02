#!/usr/bin/env python3
"""Inline \\input{...} lines so tools can read the talk as one string. Paths are relative to the repository root."""
import re, sys
from pathlib import Path
def flatten(path, root=None):
    path=Path(path); root=Path(root) if root else path.parent
    text=path.read_text()
    def sub(m):
        p=root/(m.group(1)+('' if m.group(1).endswith('.tex') else '.tex'))
        return flatten(p,root)
    return re.sub(r'^\\input\{([^}]+)\}[ \t]*$',sub,text,flags=re.M)
if __name__=='__main__':
    sys.stdout.write(flatten(sys.argv[1]))
