#!/usr/bin/env python3
"""cmajor.py VERSION_DIR: list bars where the sounding pitch classes are exactly C, E, G (the cyclic rule: no C-major triad in the scherzo)."""
import sys, mido
m = mido.MidiFile(sys.argv[1] + '/score.midi')
ev = []
for t in m.tracks:
    tt = 0
    for x in t:
        tt += x.time
        if x.type == 'note_on' and x.velocity > 0: ev.append((tt, x.note, 1))
        elif x.type == 'note_off' or (x.type == 'note_on' and x.velocity == 0): ev.append((tt, x.note, -1))
ev.sort(); on = {}; bars = set(); i = 0
while i < len(ev):
    t = ev[i][0]
    while i < len(ev) and ev[i][0] == t:
        _, n, d = ev[i]; on[n] = on.get(n, 0) + d
        if on[n] <= 0: on.pop(n)
        i += 1
    if {n % 12 for n in on} == {0, 4, 7}: bars.add(int(t / m.ticks_per_beat / 3) + 1)
print("C-major triads: " + (", ".join(map(str, sorted(bars))) if bars else "none"))
