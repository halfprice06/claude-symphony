#!/usr/bin/env python3
"""Flatten a LilyPond score.midi to a timed event list for gmrender.swift.

Usage: midi2events.py score.midi events.txt
Output lines: "<seconds> <status> <data1> <data2>", then "len <seconds>".
Each General MIDI program gets its own channel (drums stay on channel 10), because LilyPond
wraps channels when a score has more than 16 staves. No other change is made to the notes,
velocities, controllers or tempo.
"""
import struct, sys

def vlq(t, i):
    v = 0
    while True:
        b = t[i]; i += 1; v = (v << 7) | (b & 0x7f)
        if not b & 0x80: return v, i

def parse(path):
    d = open(path, 'rb').read()
    assert d[:4] == b'MThd', 'not a MIDI file'
    ntr, div = struct.unpack('>HH', d[10:14])
    pos, tracks = 14, []
    for _ in range(ntr):
        assert d[pos:pos+4] == b'MTrk'
        ln = struct.unpack('>I', d[pos+4:pos+8])[0]
        t = d[pos+8:pos+8+ln]; pos += 8 + ln
        i = tick = rs = 0; evs = []
        while i < len(t):
            dt, i = vlq(t, i); tick += dt
            b = t[i]
            if b == 0xff:
                typ = t[i+1]; ln2, i = vlq(t, i + 2)
                if typ == 0x51: evs.append((tick, 'tempo', int.from_bytes(t[i:i+ln2], 'big')))
                i += ln2
            elif b in (0xf0, 0xf7):
                ln2, i = vlq(t, i + 1); i += ln2
            else:
                if b & 0x80: rs = b; i += 1
                n = 1 if rs & 0xf0 in (0xc0, 0xd0) else 2
                evs.append((tick, 'ch', rs & 0xf0, rs & 0x0f, t[i], t[i+1] if n == 2 else 0)); i += n
        tracks.append(evs)
    return div, tracks

def main(src, out):
    div, tracks = parse(src)
    # one channel per program, as symphony/mvt1/tools/fixmidi.py does
    free = [c for c in range(16) if c != 9]; chan_of_prog = {}; chan_of_track = {}
    for k, evs in enumerate(tracks):
        first = next((e for e in evs if e[1] == 'ch' and e[2] == 0xc0 and e[3] != 9), None)
        if first is None: continue
        if first[4] not in chan_of_prog:
            if not free: sys.exit('more than 15 programs')
            chan_of_prog[first[4]] = free.pop(0)
        chan_of_track[k] = chan_of_prog[first[4]]
    tempo = sorted((e[0], e[2]) for evs in tracks for e in evs if e[1] == 'tempo')
    def seconds(tick):
        sec, last, us = 0.0, 0, 500000
        for tk, u in tempo:
            if tk >= tick: break
            sec += (tk - last) * us / div / 1e6; last, us = tk, u
        return sec + (tick - last) * us / div / 1e6
    rows = []
    for k, evs in enumerate(tracks):
        for e in evs:
            if e[1] != 'ch': continue
            _, _, hi, ch, a, b = e
            if ch != 9: ch = chan_of_track.get(k, ch)
            off = hi == 0x80 or (hi == 0x90 and b == 0)
            pri = 0 if off else (2 if hi == 0x90 else 1)
            rows.append((e[0], pri, hi | ch, a, b))
    rows.sort()
    cache = {}
    with open(out, 'w') as f:
        for tick, _, st, a, b in rows:
            if tick not in cache: cache[tick] = seconds(tick)
            f.write(f"{cache[tick]:.5f} {st} {a} {b}\n")
        f.write(f"len {seconds(rows[-1][0]) + 3.0:.3f}\n")
    notes = sum(1 for r in rows if r[1] == 2)
    print(f"{src}: {notes} notes, {seconds(rows[-1][0]):.1f} s, channels {dict(sorted(chan_of_prog.items()))}")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
