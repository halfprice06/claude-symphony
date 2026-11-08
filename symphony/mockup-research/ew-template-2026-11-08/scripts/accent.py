import sys, mido, statistics as st, collections
fn = sys.argv[1]; m = mido.MidiFile(fn); ppq = m.ticks_per_beat
for tr in m.tracks:
    name = ''; t = 0; on = {}; notes = []
    for e in tr:
        t += e.time
        if e.type == 'track_name': name = e.name
        elif e.type == 'note_on' and e.velocity > 0: on.setdefault(e.note, []).append((t, e.velocity))
        elif e.type in ('note_off', 'note_on') and on.get(e.note):
            t0, v = on[e.note].pop(0); notes.append((t0, t, e.note, v))
    notes.sort()
    sh = [n for n in notes if n[1] - n[0] < ppq // 2]
    if len(sh) < 40: continue
    onsets = sorted(set(n[0] for n in sh))
    ioi = collections.Counter(b - a for a, b in zip(onsets, onsets[1:]) if b > a)
    sub = ioi.most_common(1)[0][0]
    per = max(1, round(ppq / sub))
    pos = collections.defaultdict(list); bar = collections.defaultdict(list)
    for n in sh:
        pos[round((n[0] % ppq) / sub) % per].append(n[3])
        if n[0] % ppq == 0: bar[(n[0] // ppq) % 4].append(n[3])
    # how varied are velocities at the same position (is it a fixed pattern or random?)
    within = st.median([st.pstdev(v) for v in pos.values() if len(v) > 5])
    print(f"{name[:44]:44s} n={len(sh)} grid {sub}t ({per}/beat) | mean vel by slot " +
          ' '.join(f'{k}:{st.mean(v):.0f}' for k, v in sorted(pos.items()) if len(v) > 5) +
          ' | beat 1-4 ' + ' '.join(f'{st.mean(v):.0f}' for k, v in sorted(bar.items())) +
          f' | sd within slot {within:.1f}')
