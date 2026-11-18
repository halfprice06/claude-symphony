"""Convert the MIDI parts of a Cubase .cpr to a type-1 MIDI file (480 PPQ) with the project's tempo map.
Curved CC segments (Cubase controller curves: rational quadratic Bezier, control point (x, y, weight)) are filled in
every 30 ticks. CURVE=travel (default): y is the fraction of the way from the start value to the end value;
CURVE=box: y is absolute inside the min..max box of the segment; CURVE=linear ignores the curve.
Usage: python3 -I cpr2mid.py in.cpr out.mid"""
CURVE = __import__('os').environ.get('CURVE', 'travel')
def bez(x, y, w, p0y, p2y, n=200):
    pts = []
    for i in range(n + 1):
        t = i / n; a = (1 - t) ** 2; b = 2 * w * t * (1 - t); c = t * t; den = a + b + c
        pts.append(((b * x + c) / den, (a * p0y + b * y + c * p2y) / den))
    return pts
import sys, os, mido, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cprlib import read, part_abs
R = read(sys.argv[1])
mf = mido.MidiFile(type=1, ticks_per_beat=480)
t0 = mido.MidiTrack(); mf.tracks.append(t0)
ev = [(int(round(ppq)), mido.MetaMessage('set_tempo', tempo=int(round(spb * 1e6)))) for ppq, sec, spb in R['tempo']]
def flush(track, ev):
    ev.sort(key=lambda x: (x[0], 0 if x[1].type in ('note_off', 'set_tempo', 'track_name') else 1))
    last = 0
    for t, m in ev:
        track.append(m.copy(time=max(0, t - last))); last = max(last, t)
flush(t0, ev)
for p in R['parts']:
    if not p['notes'] and not p['ccs']: continue
    tr = mido.MidiTrack(); mf.tracks.append(tr)
    ev = [(0, mido.MetaMessage('track_name', name=p['name']))]
    for pos, pitch, vel, L in p['notes']:
        a = int(round(part_abs(p, pos))); b = max(a + 1, int(round(part_abs(p, pos + L))))
        if a < 0: continue
        ev.append((a, mido.Message('note_on', note=pitch, velocity=max(1, vel))))
        ev.append((b, mido.Message('note_off', note=pitch, velocity=0)))
    bycc = collections.defaultdict(list)
    for pos, cc, val, curve in p['ccs']: bycc[cc].append((part_abs(p, pos), val, curve))
    for cc, pts in bycc.items():
        pts.sort()
        for (a, va, cv), nxt in zip(pts, pts[1:] + [None]):
            if a < 0: continue
            ev.append((int(round(a)), mido.Message('control_change', control=cc, value=va)))
            if cv and nxt and nxt[0] - a > 60 and nxt[1] != va:
                b, vb = nxt[0], nxt[1]; t = a + 30
                if CURVE == 'travel': pts = bez(*cv, 0, 1); f = lambda Y: va + (vb - va) * Y
                elif CURVE == 'box':
                    up = vb > va; lo, hi = min(va, vb), max(va, vb)
                    pts = bez(*cv, 0 if up else 1, 1 if up else 0); f = lambda Y: lo + (hi - lo) * Y
                else: pts = [(0, 0), (1, 1)]; f = lambda Y: va + (vb - va) * Y
                xs = [q[0] for q in pts]
                while t < b - 15:
                    X = (t - a) / (b - a); k = max(1, min(len(xs) - 1, __import__('bisect').bisect_left(xs, X)))
                    (x0, y0), (x1, y1) = pts[k - 1], pts[k]
                    Y = y0 + (y1 - y0) * ((X - x0) / (x1 - x0) if x1 > x0 else 0)
                    v = max(0, min(127, int(round(f(Y)))))
                    ev.append((int(round(t)), mido.Message('control_change', control=cc, value=v))); t += 30
    flush(tr, ev)
mf.save(sys.argv[2])
print('tracks', len(mf.tracks) - 1, 'tempo events', len(R['tempo']), 'notes', sum(len(p['notes']) for p in R['parts']))
