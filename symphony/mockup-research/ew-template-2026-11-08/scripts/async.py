"""Ensemble asynchrony: cluster note onsets from different tracks that fall within 70 ms of the cluster's first onset;
for clusters with >= 3 tracks report the spread (last - first track onset) and each family's mean offset vs the cluster median.
Usage: python3 -I async.py file.mid ..."""
import sys, mido, bisect, statistics as st, re, collections
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xsum_fam import fam
for f in sys.argv[1:]:
    mf = mido.MidiFile(f); P = mf.ticks_per_beat
    ev = []
    for tr in mf.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == 'set_tempo': ev.append((t, m.tempo))
    ev = sorted(ev) or [(0, 500000)]
    if ev[0][0] > 0: ev.insert(0, (0, 500000))
    cum = [(ev[0][0], 0.0, ev[0][1])]
    for tt, tp in ev[1:]:
        t0, m0, tp0 = cum[-1]; cum.append((tt, m0 + (tt - t0) * tp0 / P / 1000, tp))
    ct = [c[0] for c in cum]
    def ms(x):
        t0, m0, tp = cum[bisect.bisect_right(ct, x) - 1]; return m0 + (x - t0) * tp / P / 1000
    on = []
    for ti, tr in enumerate(mf.tracks):
        name = next((m.name for m in tr if m.type == 'track_name'), '')
        t = 0; firsts = {}
        for m in tr:
            t += m.time
            if m.type == 'note_on' and m.velocity > 0 and m.note >= 24:
                on.append((ms(t), ti, fam(name)))
    on.sort()
    spreads = []; famoff = collections.defaultdict(list)
    i = 0
    while i < len(on):
        j = i; tracks = {}
        while j < len(on) and on[j][0] - on[i][0] <= 70:
            tracks.setdefault(on[j][1], (on[j][0], on[j][2])); j += 1
        if len(tracks) >= 3:
            ts = sorted(v[0] for v in tracks.values()); spreads.append(ts[-1] - ts[0])
            med = st.median(ts)
            for v in tracks.values(): famoff[v[1]].append(v[0] - med)
            i = j
        else:
            i += 1
    if not spreads: print(f.split('/')[-1], 'no clusters'); continue
    s = sorted(spreads)
    print(f"{f.split('/')[-1]}: {len(s)} entries of 3+ tracks; spread first-to-last track ms median {st.median(s):.0f}, IQR {s[len(s)//4]:.0f}..{s[3*len(s)//4]:.0f}; exactly together (<1 ms) {sum(1 for x in s if x < 1)/len(s)*100:.0f}%")
    print("   family offset vs entry median ms: " + ", ".join(f"{k} {st.mean(v):+.0f} (n={len(v)})" for k, v in sorted(famoff.items()) if len(v) >= 20))
