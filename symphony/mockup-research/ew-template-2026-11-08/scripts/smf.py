"""Stats for a Standard MIDI File mockup: per track CC lanes, velocity, timing vs grid, overlaps, repeated-note gaps,
and CC1/CC11 shape around phrase starts/ends. Usage: python3 -I smf.py file.mid [ks_below=24]"""
import sys, collections, statistics as st, bisect, mido
mf = mido.MidiFile(sys.argv[1]); KS = int(sys.argv[2]) if len(sys.argv) > 2 else 24
PPQ = mf.ticks_per_beat
# tempo map
tempos = [(0, 500000)]
for tr in mf.tracks:
    t = 0
    for m in tr:
        t += m.time
        if m.type == 'set_tempo': tempos.append((t, m.tempo))
tempos.sort()
def ms(tick):
    tot = 0.0; last_t, last_tempo = 0, tempos[0][1]
    for tt, tp in tempos[1:]:
        if tt >= tick: break
        tot += (tt - last_t) * last_tempo / PPQ / 1000; last_t, last_tempo = tt, tp
    return tot + (tick - last_t) * last_tempo / PPQ / 1000
bpms = sorted(set(round(60e6 / tp, 1) for _, tp in tempos))
print(f"PPQ {PPQ}, tempi {bpms[:12]}{'...' if len(bpms)>12 else ''}, length {ms(max(sum(m.time for m in tr) for tr in mf.tracks))/1000:.0f} s")
def q(v, f="{:.0f}"):
    v = sorted(v)
    return (f"med {f.format(st.median(v))} (IQR {f.format(v[len(v)//4])}..{f.format(v[3*len(v)//4])}, n={len(v)})") if v else "-"
agg = collections.defaultdict(lambda: collections.defaultdict(list))
for tr in mf.tracks:
    name = None; t = 0; notes = []; on = {}; cc = collections.defaultdict(list)
    for m in tr:
        t += m.time
        if m.type == 'track_name' and name is None: name = m.name
        elif m.type == 'note_on' and m.velocity > 0: on.setdefault(m.note, []).append((t, m.velocity))
        elif m.type in ('note_off', 'note_on'):
            if on.get(m.note): t0, v = on[m.note].pop(0); notes.append((t0, t, m.note, v))
        elif m.type == 'control_change': cc[m.control].append((t, m.value))
        elif m.type == 'pitchwheel': cc['PB'].append((t, m.pitch))
    if not notes and not cc: continue
    notes.sort()
    ks = [n for n in notes if n[2] < KS]; real = [n for n in notes if n[2] >= KS]
    print(f"\n### {name}: {len(real)} notes, {len(ks)} keyswitch-range (<{KS}) notes {sorted(set(n[2] for n in ks))[:12]}")
    if real:
        print(f"  velocity {q([n[3] for n in real])}, distinct {len(set(n[3] for n in real))}")
        g = PPQ // 4
        off = [((n[0] % g) if (n[0] % g) <= g/2 else (n[0] % g) - g) for n in real]
        offms = [ms(n[0]) - ms(n[0] - o) for n, o in zip(real, off)]
        print(f"  onsets exactly on 16th grid {sum(1 for o in off if o == 0)/len(off)*100:.0f}%; off-grid offsets ms {q([o for o in offms if o != 0])}")
        ov = [ms(a[1]) - ms(b[0]) for a, b in zip(real, real[1:]) if b[0] > a[0] and a[1] > b[0]]
        rep = [ms(b[0]) - ms(a[1]) for a, b in zip(real, real[1:]) if a[2] == b[2] and 0 <= ms(b[0]) - ms(a[1]) < 300]
        dur = [ms(n[1]) - ms(n[0]) for n in real]
        print(f"  overlap into next ms {q(ov)} | repeated-pitch gap ms {q(rep)} | durations ms {q(dur)}")
    for k, v in sorted(cc.items(), key=lambda x: str(x[0])):
        vals = [x[1] for x in v]; span = (ms(v[-1][0]) - ms(v[0][0])) / 1000 if len(v) > 1 else 0
        print(f"  CC{k}: {len(v)} ev, range {min(vals)}..{max(vals)}, med {st.median(vals)}, {len(v)/span if span else 0:.1f}/s")
    # shapes for CC1 and CC11 lanes with >= 50 events
    for lane in (1, 11):
        c = cc.get(lane, [])
        if len(c) < 50 or not real: continue
        ct = [x[0] for x in c]
        def at(tk):
            j = bisect.bisect_right(ct, tk) - 1; return c[j][1] if j >= 0 else None
        for k, n in enumerate(real):
            pe = max([m[1] for m in real[:k]], default=-10**9)
            kind = 'start' if ms(n[0]) - ms(max(pe, 0)) > 150 or pe < 0 else 'legato'
            b = at(n[0])
            if b is None: continue
            for o in (-200, -100, 0, 100, 200, 400, 800):
                tk = n[0] + int(o / 1000 * PPQ * 2)  # approx at 120 bpm
                v = at(tk)
                if v is not None: agg[(lane, kind)][o].append(v - b)
            nx = real[k+1][0] if k + 1 < len(real) else 10**12
            if ms(nx) - ms(n[1]) > 150:
                e = at(n[1])
                for o in (-1000, -500, -250):
                    v = at(n[1] + int(o / 1000 * PPQ * 2))
                    if v is not None and e is not None: agg[(lane, 'end')][o].append(v - e)
print("\n== CC shape summary across tracks (change vs value at onset / note-off; offsets approximate)")
for key, d in sorted(agg.items(), key=lambda x: str(x[0])):
    print(f"CC{key[0]} {key[1]}: " + "; ".join(f"{o:+d}ms {q(v)}" for o, v in sorted(d.items())))
