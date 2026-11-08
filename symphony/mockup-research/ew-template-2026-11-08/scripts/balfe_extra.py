import sys, mido, statistics as st, collections, math
def load(fn):
    m = mido.MidiFile(fn); ppq = m.ticks_per_beat
    tempo = []  # (tick, us/beat)
    for tr in m.tracks:
        t = 0
        for e in tr:
            t += e.time
            if e.type == 'set_tempo': tempo.append((t, e.tempo))
    tempo.sort()
    if not tempo or tempo[0][0] > 0: tempo.insert(0, (0, 500000))
    def sec(tick):
        s = 0.0; last_t, last_us = 0, tempo[0][1]
        for tt, us in tempo[1:]:
            if tt >= tick: break
            s += (tt - last_t) * last_us / 1e6 / ppq; last_t, last_us = tt, us
        return s + (tick - last_t) * last_us / 1e6 / ppq
    tracks = []
    for tr in m.tracks:
        name = ''; t = 0; on = {}; notes = []; cc = collections.defaultdict(list)
        for e in tr:
            t += e.time
            if e.type == 'track_name': name = e.name
            elif e.type == 'note_on' and e.velocity > 0: on.setdefault((e.channel, e.note), []).append((t, e.velocity))
            elif e.type in ('note_off', 'note_on'):
                k = (e.channel, e.note)
                if on.get(k): t0, v = on[k].pop(0); notes.append((t0, t, e.note, v))
            elif e.type == 'control_change': cc[e.control].append((t, e.value))
        if notes or cc: tracks.append(dict(name=name, notes=sorted(notes), cc=cc))
    return ppq, sec, tracks
def ccat(lst, t):
    v = None
    for tt, vv in lst:
        if tt > t: break
        v = vv
    return v
fn = sys.argv[1]; ppq, sec, tracks = load(fn)
print('#', fn)
# 1. identical CC lanes
sig = collections.defaultdict(list)
for tr in tracks:
    for c in (1, 11):
        if len(tr['cc'][c]) > 20: sig[(c, tuple(tr['cc'][c]))].append(tr['name'])
print('== tracks sharing an identical CC lane')
for (c, _), names in sig.items():
    if len(names) > 1: print(f'CC{c}:', ' | '.join(names))
# 2. short notes: velocity by 16th position and accent pattern
print('== short notes (<250 ms): velocity by position in beat')
for tr in tracks:
    sh = [n for n in tr['notes'] if sec(n[1]) - sec(n[0]) < 0.25]
    if len(sh) < 40: continue
    pos = collections.defaultdict(list)
    for n in sh:
        q = round((n[0] % ppq) / (ppq / 4)) % 4
        pos[q].append(n[3])
    beat = collections.defaultdict(list)
    for n in sh:
        b = int(n[0] // ppq) % 4
        if n[0] % ppq == 0: beat[b].append(n[3])
    vs = [n[3] for n in sh]
    steps = [abs(sh[i + 1][3] - sh[i][3]) for i in range(len(sh) - 1) if sh[i + 1][0] > sh[i][0]]
    print(f"{tr['name'][:40]:40s} n={len(sh)} vel med {st.median(vs)} IQR {sorted(vs)[len(vs)//4]}-{sorted(vs)[3*len(vs)//4]} | by 16th " +
          ' '.join(f'{k}:{st.mean(v):.0f}(n{len(v)})' for k, v in sorted(pos.items())) +
          ' | downbeat by beat ' + ' '.join(f'{k+1}:{st.mean(v):.0f}' for k, v in sorted(beat.items())) +
          f' | step to next med {st.median(steps) if steps else None}')
# 3. long notes: CC1 vs CC11 relation
print('== CC1 and CC11 on the same track: CC11 minus CC1 and lead/lag')
for tr in tracks:
    a, b = tr['cc'][1], tr['cc'][11]
    if len(a) < 50 or len(b) < 50: continue
    t0 = min(a[0][0], b[0][0]); t1 = max(a[-1][0], b[-1][0]); step = ppq // 8
    xs = []; ys = []
    t = t0
    ia = ib = 0; va = a[0][1]; vb = b[0][1]
    while t <= t1:
        while ia < len(a) and a[ia][0] <= t: va = a[ia][1]; ia += 1
        while ib < len(b) and b[ib][0] <= t: vb = b[ib][1]; ib += 1
        xs.append(va); ys.append(vb); t += step
    d = [y - x for x, y in zip(xs, ys)]
    def corr(x, y):
        mx, my = st.mean(x), st.mean(y); sx = math.sqrt(sum((i-mx)**2 for i in x)); sy = math.sqrt(sum((j-my)**2 for j in y))
        return sum((i-mx)*(j-my) for i, j in zip(x, y)) / (sx*sy) if sx and sy else float('nan')
    best = max(range(-16, 17), key=lambda L: corr(xs[max(0,L):len(xs)+min(0,L)], ys[max(0,-L):len(ys)-max(0,L)]))
    sd = sorted(d)
    print(f"{tr['name'][:40]:40s} CC11-CC1 med {st.median(d):+.0f} IQR {sd[len(sd)//4]:+d}..{sd[3*len(sd)//4]:+d} r={corr(xs,ys):.2f} best lag {best/8:.2f} beats (+ = CC11 moves earlier)")
# 4. phrase starts: CC1 at first note of a phrase (after >=1 s rest) and how fast it rises
print('== phrase entries (after >=1 s rest) on tracks with CC1 lanes: CC1 at onset, +250 ms, +500 ms, +1 s (medians)')
for tr in tracks:
    a = tr['cc'][1]
    if len(a) < 50: continue
    rows = []; last_end = -1e9
    for n in tr['notes']:
        s0 = sec(n[0])
        if s0 - last_end >= 1.0:
            vals = []
            for dt in (0, .25, .5, 1.0):
                # find tick for s0+dt by search
                tk = n[0]
                while sec(tk) < s0 + dt: tk += ppq // 16
                vals.append(ccat(a, tk))
            rows.append(vals)
        last_end = max(last_end, sec(n[1]))
    if rows and all(r[0] is not None for r in rows):
        print(f"{tr['name'][:40]:40s} n={len(rows)} " + ' '.join(f'{lab}:{st.median([r[i] for r in rows]):.0f}' for i, lab in enumerate(['0', '250ms', '500ms', '1s'])))
# 5. CC7 rides
print('== CC7 lanes with >20 events')
for tr in tracks:
    c = tr['cc'][7]
    if len(c) > 20:
        vs = [v for _, v in c]
        print(f"{tr['name'][:40]:40s} n={len(c)} range {min(vs)}-{max(vs)} over {sec(c[-1][0])-sec(c[0][0]):.1f}s")
