"""Compact mockup-MIDI analyser with tempo-correct ms offsets.
Usage: python3 -I smf2.py out.json file.mid [file2.mid ...]
Per track: notes, velocity, grid timing (constant shift), overlaps, repeated-note gaps, CC lanes.
Per lane CC1/CC11/CC2: phrase arcs (value at 0..100% of each phrase, relative to the phrase max),
phrase-start ramp, pre-roll before onset, end taper, long-note swells, velocity vs CC correlation.
Prints a text report and writes raw aggregates to out.json for cross-file summaries."""
import sys, json, collections, statistics as st, bisect, mido

def q(v, f="{:.0f}"):
    v = sorted(v)
    if not v: return "-"
    return f"{f.format(st.median(v))} [{f.format(v[len(v)//4])}..{f.format(v[3*len(v)//4])}] n={len(v)}"

def pearson(a, b):
    if len(a) < 10: return None
    ma, mb = st.mean(a), st.mean(b)
    sa = sum((x-ma)**2 for x in a) ** .5; sb = sum((y-mb)**2 for y in b) ** .5
    return None if not sa or not sb else sum((x-ma)*(y-mb) for x, y in zip(a, b)) / sa / sb

out_json = sys.argv[1]; ALL = {}
import os; LANES = tuple(int(x) for x in os.environ.get("LANES", "1,11,2").split(","))
FRACS = (0, .1, .25, .5, .75, .9, 1.0)
for path in sys.argv[2:]:
    mf = mido.MidiFile(path); PPQ = mf.ticks_per_beat
    tempos = [(0, 500000)]
    for tr in mf.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == 'set_tempo': tempos.append((t, m.tempo))
    tempos.sort()
    # cumulative ms at each tempo change
    cum = [(0, 0.0, tempos[0][1])]
    for tt, tp in tempos[1:]:
        t0, m0, tp0 = cum[-1]
        cum.append((tt, m0 + (tt - t0) * tp0 / PPQ / 1000, tp))
    ct_ticks = [c[0] for c in cum]; ct_ms = [c[1] for c in cum]
    def ms(tick):
        j = bisect.bisect_right(ct_ticks, tick) - 1; t0, m0, tp = cum[j]
        return m0 + (tick - t0) * tp / PPQ / 1000
    def tick(msv):
        j = bisect.bisect_right(ct_ms, msv) - 1; j = max(j, 0); t0, m0, tp = cum[j]
        return int(t0 + (msv - m0) * 1000 * PPQ / tp)
    def tempo_at(tk):
        return cum[bisect.bisect_right(ct_ticks, tk) - 1][2]
    bpms = sorted(set(round(60e6 / tp) for _, tp in tempos))
    name_file = path.split('/')[-1]
    print(f"\n######## {name_file}: PPQ {PPQ}, {len(bpms)} tempi {bpms[0]}..{bpms[-1]} bpm, {len(tempos)} tempo events")
    F = collections.defaultdict(list)  # file-level aggregates
    tracks_out = []
    for tr in mf.tracks:
        name = None; t = 0; on = {}; notes = []; cc = collections.defaultdict(list)
        for m in tr:
            t += m.time
            if m.type == 'track_name' and name is None: name = m.name.strip()
            elif m.type == 'note_on' and m.velocity > 0: on.setdefault(m.note, []).append((t, m.velocity))
            elif m.type in ('note_off', 'note_on'):
                if on.get(m.note): t0, v = on[m.note].pop(0); notes.append((t0, t, m.note, v))
            elif m.type == 'control_change': cc[m.control].append((t, m.value))
        if not notes: continue
        notes.sort()
        # keyswitches: notes below 24 that are very short and not musical; treat < 24 as KS only if track has many notes >= 36
        lowks = [n for n in notes if n[2] < 24]
        real = [n for n in notes if n[2] >= 24] if len(lowks) < len(notes) * 0.5 else notes
        if len(real) < 8: continue
        T = {'name': name, 'n': len(real)}
        vel = [n[3] for n in real]
        dur = [ms(n[1]) - ms(n[0]) for n in real]
        g = PPQ // 4
        offs = []
        for n in real:
            r = n[0] % g; o = r if r <= g / 2 else r - g
            offs.append(o * tempo_at(n[0]) / PPQ / 1000)
        rounded = collections.Counter(round(o) for o in offs)
        mode_ms, mode_n = rounded.most_common(1)[0]
        ongrid = sum(1 for o in offs if abs(o) < 0.5) / len(offs)
        # overlaps (legato) and repeated-note gaps, monophonic-ish neighbours
        ov = []; rep = []; gaps = []
        for a, b in zip(real, real[1:]):
            if b[0] <= a[0]: continue
            d = ms(a[1]) - ms(b[0])
            if d > 0 and d < 400: ov.append(d)
            elif d <= 0 and -d < 150: gaps.append(-d)
            if a[2] == b[2] and 0 <= ms(b[0]) - ms(a[1]) < 300: rep.append(ms(b[0]) - ms(a[1]))
        T.update(vel_med=st.median(vel), vel_iqr=(sorted(vel)[len(vel)//4], sorted(vel)[3*len(vel)//4]),
                 vel_distinct=len(set(vel)), ongrid=ongrid, mode_ms=mode_ms, mode_share=mode_n/len(offs),
                 off_med=st.median(offs), dur_med=st.median(dur),
                 ov_med=st.median(ov) if ov else None, ov_n=len(ov), gap_med=st.median(gaps) if gaps else None,
                 rep_med=st.median(rep) if rep else None, rep_n=len(rep))
        lanes = {}
        for k, v in cc.items():
            if len(v) < 2: continue
            vals = [x[1] for x in v]; span = (ms(v[-1][0]) - ms(v[0][0])) / 1000
            steps = [abs(b[1]-a[1]) for a, b in zip(v, v[1:]) if b[1] != a[1]]
            lanes[k] = dict(ev=len(v), lo=min(vals), hi=max(vals), med=st.median(vals),
                            rate=len(v)/span if span else 0, step=st.median(steps) if steps else 0)
        T['lanes'] = {str(k): v for k, v in lanes.items()}
        # phrases: gap > 150 ms between max end so far and next onset
        phrases = []; cur = [real[0]]; end = real[0][1]
        for n in real[1:]:
            if ms(n[0]) - ms(end) > 150: phrases.append(cur); cur = [n]; end = n[1]
            else: cur.append(n); end = max(end, n[1])
        phrases.append(cur)
        T['phrases'] = len(phrases)
        T['phrase_len_med'] = st.median([ms(max(x[1] for x in p)) - ms(p[0][0]) for p in phrases])
        for lane in LANES:
            c = cc.get(lane, [])
            if len(c) < 20: continue
            ctk = [x[0] for x in c]; vals = [x[1] for x in c]
            if max(vals) - min(vals) < 10: continue
            def at(tk):
                j = bisect.bisect_right(ctk, tk) - 1
                return c[j][1] if j >= 0 else c[0][1]
            key = f"cc{lane}"
            # velocity vs CC at onset
            T[f'{key}_vel_r'] = pearson([n[3] for n in real], [at(n[0]) for n in real])
            for p in phrases:
                s = p[0][0]; e = max(x[1] for x in p)
                L = ms(e) - ms(s)
                v0 = at(s)
                # pre-roll: did CC move in the 300 ms before onset?
                pre = at(tick(ms(s) - 300))
                F[f'{key}_preroll'].append(v0 - pre)
                F[f'{key}_onset'].append(v0)
                if L >= 1500:
                    samp = [at(tick(ms(s) + f * L) - (1 if f == 1.0 else 0)) for f in FRACS]
                    inner = [at(tick(ms(s) + i / 40 * L)) for i in range(41)]
                    mx = max(inner); mn = min(inner)
                    F[f'{key}_arc_range'].append(mx - mn)
                    for f, v in zip(FRACS, samp): F[f'{key}_arc_{f}'].append(v - mx)
                    F[f'{key}_peakpos'].append(inner.index(mx) / 40)
                    F[f'{key}_start_ramp500'].append(at(tick(ms(s) + 500)) - v0)
                    F[f'{key}_end_taper1000'].append(at(e - 1) - at(tick(ms(e) - 1000)))
                    F[f'{key}_phrase_moving'].append(1 if mx - mn >= 6 else 0)
            # long single notes (>= 1.2 s), swell shape relative to onset value
            for n in real:
                L = ms(n[1]) - ms(n[0])
                if L < 1200: continue
                v0 = at(n[0])
                sh = [at(tick(ms(n[0]) + f * L) - (1 if f == 1.0 else 0)) - v0 for f in (.25, .5, .75, 1.0)]
                F[f'{key}_long_q'].append(sh)
        tracks_out.append(T)
        lane_s = " ".join(f"CC{k}:{v['ev']}ev {v['lo']}-{v['hi']} {v['rate']:.1f}/s" for k, v in sorted(lanes.items(), key=lambda x: -x[1]['ev'])[:4])
        print(f"- {name} | n={len(real)} vel {T['vel_med']:.0f} [{T['vel_iqr'][0]}..{T['vel_iqr'][1]}] d={T['vel_distinct']} | "
              f"grid {ongrid*100:.0f}% mode {mode_ms:+d}ms ({T['mode_share']*100:.0f}%) | dur {T['dur_med']:.0f} | "
              f"ov {T['ov_med'] and round(T['ov_med'])} (n={len(ov)}) gap {T['gap_med'] and round(T['gap_med'])} rep {T['rep_med'] and round(T['rep_med'])} (n={len(rep)}) | "
              f"phr {len(phrases)} ~{T['phrase_len_med']/1000:.1f}s | {lane_s}"
              + (f" | r(vel,cc1)={T['cc1_vel_r']:.2f}" if T.get('cc1_vel_r') is not None else ""))
    print("== file summary")
    for key in sorted(set(k.rsplit('_', 1)[0] if k.split('_')[1] in ('arc',) else k for k in F)):
        pass
    for lane in LANES:
        key = f"cc{lane}"
        if not F.get(f'{key}_onset'): continue
        arc = "; ".join(f"{int(f*100)}% {q(F[f'{key}_arc_{f}'])}" for f in FRACS if F.get(f'{key}_arc_{f}'))
        print(f"CC{lane}: phrases>=1.5s n={len(F.get(f'{key}_arc_range', []))}, moving(>=6) {st.mean(F[f'{key}_phrase_moving'])*100 if F.get(f'{key}_phrase_moving') else 0:.0f}%")
        print(f"   arc (value minus phrase max): {arc}")
        print(f"   arc range {q(F.get(f'{key}_arc_range', []))}; peak position {q(F.get(f'{key}_peakpos', []), '{:.2f}')}")
        print(f"   onset value {q(F[f'{key}_onset'])}; pre-roll change in 300ms before onset {q(F[f'{key}_preroll'])}")
        print(f"   ramp first 500ms {q(F.get(f'{key}_start_ramp500', []))}; end taper last 1000ms {q(F.get(f'{key}_end_taper1000', []))}")
        lq = F.get(f'{key}_long_q', [])
        if lq:
            print(f"   long notes >=1.2s (n={len(lq)}) change vs onset at 25/50/75/100%: " + ", ".join(q([x[i] for x in lq]) for i in range(4)))
            print(f"      share rising to mid >=4: {sum(1 for x in lq if x[1] >= 4)/len(lq)*100:.0f}%, falling at end <=-4 vs mid: {sum(1 for x in lq if x[3]-x[1] <= -4)/len(lq)*100:.0f}%, flat (all |d|<3): {sum(1 for x in lq if all(abs(y)<3 for y in x))/len(lq)*100:.0f}%")
    ALL[name_file] = {'ppq': PPQ, 'bpm': [bpms[0], bpms[-1]], 'tracks': tracks_out, 'agg': {k: v for k, v in F.items()}}
json.dump(ALL, open(out_json, 'w'))
