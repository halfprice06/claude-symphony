#!/usr/bin/env python3
"""Rewrite the bar/beat columns of a notes.csv (tools/score_events.py assumes 4/4: bar = tick // whole + 1) with the
MIDI's own time-signature grid (rtk.midi_info), so mixed-metre movements (mvt2: 3/4 + 4/4) get correct bar numbers.
Usage: fixbars.py notes.csv midi out.csv"""
import csv, sys, bisect
sys.path.insert(0, "/mnt/project-files/symphony/render/tools")
import mido
src, midi, out = sys.argv[1:4]
m = mido.MidiFile(midi); tpb = m.ticks_per_beat
sigs = []
for tr in m.tracks:
    t = 0
    for x in tr:
        t += x.time
        if x.type == "time_signature": sigs.append((t, x.numerator, x.denominator))
sigs = sorted(set(sigs)) or [(0, 4, 4)]
end = max(sum(x.time for x in tr) for tr in m.tracks)
bars = []; tick = 0; k = 0
while tick <= end:
    while k + 1 < len(sigs) and sigs[k + 1][0] <= tick: k += 1
    bars.append(tick); tick += int(sigs[k][1] * tpb * 4 / sigs[k][2])
rows = list(csv.DictReader(open(src, encoding="utf-8")))
changed = 0
for r in rows:
    tk = int(r["tick_on"]); i = bisect.bisect_right(bars, tk) - 1
    nb = i + 1
    if int(r["bar"]) != nb: changed += 1
    r["bar"] = nb; r["beat"] = round((tk - bars[i]) / tpb + 1, 3)
w = csv.DictWriter(open(out, "w", newline="", encoding="utf-8"), fieldnames=list(rows[0].keys()))
w.writeheader(); w.writerows(rows)
print(f"{len(rows)} notes, {changed} bar numbers changed, {len(bars)} bars in grid")
