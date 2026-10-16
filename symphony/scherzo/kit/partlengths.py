#!/usr/bin/env python3
"""partlengths.py VERSION_DIR: report every part whose length (in quarter notes, parsed with coherence/lyparse.py)
differs from its section's bars x beats in sections.txt. Replaces v01-generators/countbars.py, which missed lines
ending in a comment and part-combine directives. Prints "part lengths: all match" when clean."""
import sys, os
sys.path.insert(0, '/home/user/claude_composes/symphony/coherence')
import lyparse
v = sys.argv[1]; bad = 0
for name, bars, beats in lyparse.sections(v):
    path = os.path.join(v, 'sections', name + '.ily')
    for var, body in lyparse.variables(path).items():
        total = sum(l for _, l, _ in lyparse.events(body))
        if total != bars * beats:
            bad += 1
            print(f"{var}: {float(total / beats):g} bars, expected {bars}")
print("part lengths: all match" if not bad else f"part lengths: {bad} mismatched")
