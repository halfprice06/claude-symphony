"""Quick objective checks on a LilyPond MIDI file.

Prints per-track ranges and density, range violations for known instruments,
melodic statistics for the top line, exposed parallel fifths/octaves between
the top voice and the bass, and a bar-by-bar loudness/density profile.
"""
import sys
import collections
import mido

# Practical sounding ranges (MIDI numbers) for orchestral writing.
RANGES = {
    'piccolo': (74, 105), 'flute': (60, 96), 'oboe': (58, 91), 'english horn': (52, 81),
    'cor anglais': (52, 81), 'clarinet': (50, 91), 'bass clarinet': (34, 72),
    'bassoon': (34, 75), 'contrabassoon': (22, 53), 'horn': (34, 77), 'french horn': (34, 77),
    'trumpet': (54, 82), 'trombone': (40, 72), 'bass trombone': (34, 67), 'tuba': (26, 65),
    'timpani': (38, 57), 'harp': (24, 103), 'violin': (55, 100), 'viola': (48, 88),
    'cello': (36, 79), 'contrabass': (28, 60), 'double bass': (28, 60),
}
NAMES = 'C C# D Eb E F F# G Ab A Bb B'.split()


def pname(n):
    return f"{NAMES[n % 12]}{n // 12 - 1}"


def load(path):
    mid = mido.MidiFile(path)
    tpb = mid.ticks_per_beat
    tracks = []
    tempo_map = []
    for tr in mid.tracks:
        name = ''
        t = 0
        on = {}
        notes = []
        for msg in tr:
            t += msg.time
            if msg.type == 'track_name' and not name:
                name = msg.name
            elif msg.type == 'instrument_name' and not name:
                name = msg.name
            elif msg.type == 'set_tempo':
                tempo_map.append((t, msg.tempo))
            elif msg.type == 'note_on' and msg.velocity > 0:
                on.setdefault((msg.channel, msg.note), []).append((t, msg.velocity))
            elif msg.type in ('note_off', 'note_on'):
                k = (msg.channel, msg.note)
                if on.get(k):
                    st, vel = on[k].pop(0)
                    notes.append((st, t, msg.note, vel))
        if notes:
            tracks.append((name or f'track{len(tracks)}', sorted(notes)))
    return tpb, tracks, sorted(tempo_map)


def seconds(tick, tpb, tempo_map):
    sec, last_t, tempo = 0.0, 0, 500000
    for t, tp in tempo_map:
        if t >= tick:
            break
        sec += (t - last_t) / tpb * tempo / 1e6
        last_t, tempo = t, tp
    return sec + (tick - last_t) / tpb * tempo / 1e6


def main(path):
    tpb, tracks, tempo_map = load(path)
    bar = tpb * 4
    end = max(n[1] for _, ns in tracks for n in ns)
    nbars = end // bar + 1
    print(f"Duration: {seconds(end, tpb, tempo_map):.0f}s, ~{nbars} bars (4/4 assumed)\n")
    print("Tracks: name | notes | range | violations")
    for name, ns in tracks:
        lo, hi = min(n[2] for n in ns), max(n[2] for n in ns)
        key = next((k for k in sorted(RANGES, key=len, reverse=True) if k in name.lower()), None)
        viol = ''
        if key:
            rlo, rhi = RANGES[key]
            bad = [n for n in ns if n[2] < rlo or n[2] > rhi]
            if bad:
                viol = f"{len(bad)} notes out of range ({key} {pname(rlo)}-{pname(rhi)}), first at bar {bad[0][0] // bar + 1}: {pname(bad[0][2])}"
        print(f"  {name:28s} {len(ns):5d}  {pname(lo)}-{pname(hi)}  {viol}")

    # Skyline (top voice) and bass across all tracks, using every note sounding at each attack.
    events = collections.defaultdict(list)
    allnotes = [n for _, ns in tracks for n in ns]
    for st, en, p, v in allnotes:
        events[st].append((p, en))
    times = sorted(events)
    top, bot = [], []
    active = []
    idx = 0
    allnotes.sort()
    for t in times:
        while idx < len(allnotes) and allnotes[idx][0] <= t:
            active.append(allnotes[idx]); idx += 1
        active = [n for n in active if n[1] > t]
        hi = max(active, key=lambda n: n[2]); lo = min(active, key=lambda n: n[2])
        top.append((t, hi[2], hi[0] == t))
        bot.append((t, lo[2], lo[0] == t))

    # Melody stats for first track (assumed top line)
    name, ns = tracks[0]
    mel = [n[2] for n in ns]
    ints = [b - a for a, b in zip(mel, mel[1:])]
    steps = sum(1 for i in ints if abs(i) <= 2)
    leaps = sum(1 for i in ints if abs(i) >= 5)
    rep = sum(1 for i in ints if i == 0)
    print(f"\nTop-line ({name}) intervals: {len(ints)} | steps {steps*100//max(1,len(ints))}% | "
          f"leaps>=4th {leaps*100//max(1,len(ints))}% | repeats {rep*100//max(1,len(ints))}%")
    hist = collections.Counter(abs(i) for i in ints)
    print("  interval histogram (semitones):", dict(sorted(hist.items())))

    # Parallel fifths/octaves between the sounding top and bottom, both re-attacked.
    # Runs of three or more consecutive parallel octaves are treated as deliberate doublings;
    # runs of fifths are always reported (cycle 12 found five hidden fifths at bar 96).
    moves = []
    prev = None
    for (t, hi, ah), (_, lo, al) in zip(top, bot):
        if hi == lo:
            prev = None
            continue
        iv = (hi - lo) % 12
        if not (ah and al):
            prev = (t, hi, lo, iv)
            continue
        if prev:
            pt, phi, plo, piv = prev
            ok = iv == piv and iv in (0, 7) and hi != phi and lo != plo and (hi - phi) * (lo - plo) > 0
            moves.append((ok, (t // bar + 1, 'octaves' if iv == 0 else 'fifths', pname(phi), pname(hi), pname(plo), pname(lo))))
        prev = (t, hi, lo, iv)
    par, doublings, run = [], 0, []
    for ok, info in moves + [(False, None)]:
        if ok:
            run.append(info)
            continue
        if len(run) >= 2 and all(r[1] == 'octaves' for r in run):
            doublings += 1
        else:
            par.extend(run)
        run = []
    print(f"\nOuter-voice parallels (top vs bass, similar motion): {len(par)}  (+{doublings} doubling runs ignored)")
    for p in par[:25]:
        print(f"  bar {p[0]}: {p[1]} {p[2]}->{p[3]} over {p[4]}->{p[5]}")

    # Density / register profile per 4 bars
    print("\nProfile per 4 bars: attacks | voices sounding (avg) | top | bottom")
    for b0 in range(0, nbars, 4):
        t0, t1 = b0 * bar, (b0 + 4) * bar
        att = sum(1 for t in times if t0 <= t < t1 for _ in events[t])
        ps = [p for t in times if t0 <= t < t1 for p, _ in events[t]]
        sounding = []
        for k in range(8):
            tt = t0 + k * bar // 2
            c = sum(1 for _, nsx in tracks for st, en, p, v in nsx if st <= tt < en)
            sounding.append(c)
        if ps:
            print(f"  bars {b0+1:3d}-{b0+4:3d}: {att:4d} | {sum(sounding)/len(sounding):4.1f} | {pname(max(ps)):4s} | {pname(min(ps))}")
        else:
            print(f"  bars {b0+1:3d}-{b0+4:3d}: rest")


if __name__ == '__main__':
    main(sys.argv[1])
