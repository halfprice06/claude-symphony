#!/usr/bin/env python3
"""r03: passages derived from the score's own markings, for any version and metre (no bar lists in config).

melodies(events.tsv, notes rows, bar_s, ...) -> marked melody phrases
    every text script whose text matches config melodies.pattern (default espr|dolce|cantabile|solo) in the
    LilyPond event log; the phrase starts at the bar of the staff's first note at or after the mark and runs while the
    staff has notes in consecutive bars, at most max_bars bars (critic 1's rule, as critics/c02/scripts/melody2.py).
rolls(notes rows, bar_s) -> timpani rolls longer than one bar (tremolo-marked timpani notes).

notes rows are notes.csv rows from lib/score_events.py (bars from the MIDI time-signature grid).
"""
import re
from collections import defaultdict


def key(name):
    k = re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()
    return k or "drums"


def melodies(events_path, rows, bar_s, tpb=None, pattern=r"espr|dolce|cantabile|solo", max_bars=8, exclude=()):
    """[(staff, [bars], t_start_s, t_end_s, text)] sorted by start bar."""
    by_staff = defaultdict(list); bars_with = defaultdict(set)
    for r in rows:
        st = key(r["staff"])
        by_staff[st].append((float(r["pos"]) if "pos" in r and r["pos"] != "" else None, int(r["tick_on"]), int(r["bar"])))
        bars_with[st].add(int(r["bar"]))
    for st in by_staff:
        by_staff[st].sort(key=lambda z: z[1])
    # notes.csv has tick_on (= moment * 4 * tpb); recover tpb from any row with notated ticks if not given
    marks = {}
    for line in open(events_path, encoding="utf-8", errors="replace"):
        f = line.rstrip("\n").split("\t")
        if len(f) < 8 or not f[7].startswith("text:"):
            continue
        txt = f[7][5:]
        if not re.search(pattern, txt, re.I):
            continue
        st = key(f[1])
        if st in exclude or st not in by_staff:
            continue
        mom = float(f[3])
        tk = mom * 4 * tpb
        nb = [b for _, t, b in by_staff[st] if t >= tk - 1]
        if not nb:
            continue
        marks.setdefault((st, nb[0]), []).append(txt)
    out = []
    for (st, b0), txts in sorted(marks.items(), key=lambda z: (z[0][1], z[0][0])):
        bs = []; b = b0
        while b in bars_with[st] and len(bs) < max_bars:
            bs.append(b); b += 1
        if bs:
            out.append((st, bs, bar_s[bs[0] - 1], bar_s[min(bs[-1], len(bar_s) - 1)], " / ".join(dict.fromkeys(txts))))
    return out


def rolls(rows, bar_s, min_bars=1.0):
    """[(t_start, t_end, [bars], dyn, hairpin)] for timpani tremolo notes longer than min_bars of their first bar."""
    out = []
    for r in rows:
        if not key(r["staff"]).startswith("Timp") or "tremolo" not in (r["arts"] or ""):
            continue
        t0 = float(r["t_on_s"]); L = float(r["notated_s"]); b0 = int(r["bar"])
        blen = bar_s[b0] - bar_s[b0 - 1] if b0 < len(bar_s) else 2.0
        if L <= blen * min_bars * 1.01:
            continue
        bs = [b for b in range(1, len(bar_s)) if bar_s[b - 1] < t0 + L - 0.05 and bar_s[b] > t0 + 0.05]
        out.append((t0, t0 + L, bs, r["dyn"], r["hairpin"]))
    return out
