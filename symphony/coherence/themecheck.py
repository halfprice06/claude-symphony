#!/usr/bin/env python3
"""Theme record comparison. Reports which recorded themes a version changed; it blocks nothing
(Dan, 2026-10-12: the scherzo themes are not locked; the record lets the finale follow their changes).

The record file (e.g. themes-scherzo.ly) holds each recorded theme as a LilyPond variable in absolute pitch,
3/4 bars, starting at bar 1 of the variable (leading rests give the beat it starts on), and lines
    %@ <theme> <instrument variable suffix> <bar> [<number of notes> [<first note, counted from 1>]]
naming every place the theme must appear in the movement (part of the theme when a note count is given:
that many notes, from the first note or from the given note).

    themecheck.py RECORD VERSION_DIR          compare every %@ line; exit 1 if any theme changed or is missing
    themecheck.py RECORD VERSION_DIR [--beats 4]  for a movement with 4 quarter beats per bar (default 3)
    themecheck.py RECORD VERSION_DIR --find   list every place in every part where a theme (or its first 6+ notes) occurs

Comparison: pitch intervals between successive notes modulo 12 (so transposition and octave changes are allowed),
the length of every note but the last, the time from each note to the next (rests count), and the beat the theme
starts on. The last note's length may differ (endings vary). A theme found intact at a different bar of the same
part (one no other %@ line of that theme and part names) is reported MOVED; a changed or missing one CHANGED.
"""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "/home/user/claude_composes/symphony/coherence"); import lyparse

# quarter beats per bar (3 for the scherzo; pass --beats 4 for a 2/2 or 4/4 movement)
BEATS = int(sys.argv[sys.argv.index('--beats') + 1]) if '--beats' in sys.argv else 3

N = 'C C# D D# E F F# G G# A A# B'.split()
def nm(p): return N[p % 12] + str(p // 12 - 1)

def lock_themes(lock):
    raw = open(lock).read()
    themes = {}
    for name, body in lyparse.variables(lock).items():
        pos, ev = 0, []
        merged = []
        for p, l, tie in lyparse.events(body):
            if merged and merged[-1][3] and merged[-1][1] == p and p is not None:
                q = merged[-1]; merged[-1] = (q[0], p, q[2] + l, tie)
            else:
                merged.append((pos, p, l, tie))
            pos += l
        themes[name] = [(s, p, l) for s, p, l, _ in merged if p is not None]
    occ = []
    for m in re.finditer(r'^%@\s+(\w+)\s+(\w+)\s+(\d+)(?:\s+(\d+))?(?:\s+(\d+))?(?:\s+(abs))?', raw, re.M):
        occ.append((m.group(1), m.group(2), int(m.group(3)), int(m.group(4)) if m.group(4) else None,
                    int(m.group(5)) if m.group(5) else 1, bool(m.group(6))))
    return themes, occ

def shape(notes, absolute=False):
    """notes: list of (abs_onset, pitch, length) -> comparable tuple; absolute=True also compares the pitches themselves"""
    iv = tuple((b[1] - a[1]) % 12 for a, b in zip(notes, notes[1:]))
    ln = tuple(n[2] for n in notes[:-1])
    ioi = tuple(b[0] - a[0] for a, b in zip(notes, notes[1:]))
    beat = notes[0][0] % BEATS
    return (iv, ln, ioi, beat, tuple(n[1] for n in notes)) if absolute else (iv, ln, ioi, beat)

def part_notes(vdir, suffix):
    out = []
    for bar, beat, p, l in lyparse.part_events(vdir, suffix):
        out.append(((bar - 1) * BEATS + beat, p, l, bar))
    return out

def matches(part, theme, n):
    want = shape([(s, p, l) for s, p, l in theme[:n]])
    hits = []
    for i in range(len(part) - n + 1):
        seg = [(o, p, l) for o, p, l, _ in part[i:i + n]]
        if shape(seg) == want:
            hits.append(part[i][3])
    return hits

def describe(notes):
    return ' '.join(f"{nm(p)}/{l}" for _, p, l, *_ in notes)

def suffixes(vdir):
    s = set()
    for name, _, _ in lyparse.sections(vdir):
        path = os.path.join(vdir, 'sections', name + '.ily')
        if os.path.exists(path):
            s |= {k[len(name):] for k in lyparse.variables(path) if k.startswith(name)}
    return sorted(s)

def main():
    lock, vdir = sys.argv[1], sys.argv[2]
    themes, occ = lock_themes(lock)
    if '--find' in sys.argv:
        for t, notes in themes.items():
            for suf in suffixes(vdir):
                part = part_notes(vdir, suf)
                full = matches(part, notes, len(notes))
                pre = [b for b in matches(part, notes, min(6, len(notes))) if b not in full]
                if full or pre:
                    print(f"{t:12} {suf:10} full: {full}  first-6 only: {pre}")
        return 0
    bad = 0
    for t, suf, bar, n, first, ab in occ:
        notes = themes[t][first - 1:]
        n = n or len(notes)
        part = part_notes(vdir, suf)
        here = [i for i, x in enumerate(part) if x[3] >= bar]
        ok = False
        if here:
            i = here[0]
            seg = [(o, p, l) for o, p, l, _ in part[i:i + n]]
            ok = len(seg) == n and part[i][3] == bar and shape(seg, ab) == shape(notes[:n], ab)
        if ok:
            print(f"ok    {t} {suf} {bar} ({n} notes from note {first}{', at pitch' if ab else ''})")
            continue
        claimed = {o[2] for o in occ if o[0] == t and o[1] == suf}
        if ab:
            moved = []
            bad += 1
            got = part[here[0]:here[0] + n] if here else []
            print(f"CHANGED {t} {suf} {bar} ({n} notes from note {first}, at pitch): theme changed, moved or transposed")
            print(f"      record:  {describe([(s, p, l) for s, p, l in notes[:n]])}")
            print(f"      version: {describe(got)}")
            continue
        moved = [b for b in matches(part, notes, n) if b not in claimed]
        if moved:
            print(f"MOVED {t} {suf}: expected at {bar}, found intact at {moved}; update the %@ line in the record")
            continue
        bad += 1
        got = part[here[0]:here[0] + n] if here else []
        print(f"CHANGED {t} {suf} {bar} ({n} notes from note {first}): theme changed or missing")
        print(f"      record:  {describe([(s, p, l) for s, p, l in notes[:n]])}")
        print(f"      version: {describe(got)}")
    print(f"theme record: {len(occ) - bad}/{len(occ)} unchanged" + ("" if not bad else f", {bad} CHANGED"))
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())
