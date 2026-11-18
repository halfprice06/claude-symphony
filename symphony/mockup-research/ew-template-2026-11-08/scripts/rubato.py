"""Beat-level tempo stats for MIDI files with tempo maps: deviation from a 17-beat moving median, slow outliers,
and the slowest-to-fastest spread of 4-bar medians. Usage: python3 -I rubato.py file.mid ..."""
import sys, mido, bisect, statistics as st
for f in sys.argv[1:]:
    mf = mido.MidiFile(f); P = mf.ticks_per_beat
    ev = []
    for tr in mf.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == 'set_tempo': ev.append((t, 60e6 / m.tempo))
    ev.sort(); tk = [e[0] for e in ev]
    # first and last note
    first, last = 10**12, 0
    for tr in mf.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == 'note_on' and m.velocity > 0: first = min(first, t); last = max(last, t)
    bpm = lambda x: ev[max(bisect.bisect_right(tk, x) - 1, 0)][1]
    beats = [bpm(b * P + P // 2) for b in range(first // P, last // P)]
    dev = []
    for i, b in enumerate(beats):
        w = beats[max(0, i - 8):i + 9]; m = st.median(w); dev.append((b - m) / m * 100)
    absd = sorted(abs(d) for d in dev)
    blocks = [st.median(beats[i:i+16]) for i in range(0, len(beats) - 15, 16)]
    steps = sum(1 for a, b in zip(beats, beats[1:]) if a != b)
    print(f"{f.split('/')[-1]}: {len(beats)} beats, tempo changes on {steps/len(beats)*100:.0f}% of beats; "
          f"|dev| median {st.median(absd):.1f}%, 90th pct {absd[int(len(absd)*.9)]:.1f}%; beats >15% slower {sum(1 for d in dev if d < -15)}, >25% slower {sum(1 for d in dev if d < -25)}; "
          f"4-bar medians {min(blocks):.0f}..{max(blocks):.0f} bpm" if blocks else "")
