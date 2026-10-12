#!/usr/bin/env python3
"""r03: passages derived from the score's own markings, for any version and metre (no bar lists in config).

melodies(events.tsv, notes rows, bar_s, ...) -> marked melody phrases
    every text script whose text matches config melodies.pattern (default espr|dolce|cantabile|solo) in the
    LilyPond event log; the phrase starts at the bar of the staff's first note at or after the mark and runs while the
    staff has notes in consecutive bars, at most max_bars bars (critic 1's rule, as critics/c02/scripts/melody2.py).
rolls(notes rows, bar_s) -> timpani rolls longer than one bar (tremolo-marked timpani notes; r07: chains of untied
    tremolo notes with no gap count as one roll, roll_chains).

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


def _hp_state(dyn, hp, inner, L_whole):
    """(dyn, hairpin) in force at the end of a note: its own printed state, then its inner events before its end."""
    d, h = dyn, hp or ""
    for it in (inner or "").split(";"):
        if not it:
            continue
        rp, e = it.split(":", 1)
        if float(rp) >= L_whole - 1e-9:
            continue
        if e.startswith("dyn:"):
            d = e[4:].replace("sub. ", ""); h = ""
        elif e in ("cresc-1", "decresc-1"):
            h = e[:-2]
        elif e in ("cresc1", "decresc1"):
            h = ""
    return d, h


def roll_chains(rows, tpb, gap_ticks=2):
    """r07 (critic 6, plan 1): one roll however it is written. Timpani tremolo notes that follow each other with no gap
    (a new untied note each bar, or a pitch change inside the roll) are one roll. Returns a list of chains
    [{"members": [rows in time order], "row": merged row}], one per roll (single notes too). The merged row is the
    first member's row with notated_ticks / notated_s spanning the whole chain and an 'inner' event list that holds
    every member's inner events plus, at each later member's start, the change of printed state it carries
    (hairpin stop, new dynamic, hairpin start), in the same 'relpos(whole notes):event' format as notes.csv."""
    tr = [r for r in rows if key(r["staff"]).startswith("Timp") and "tremolo" in (r["arts"] or "")]
    tr.sort(key=lambda r: (int(r["tick_on"]), int(r["pitch"])))
    chains = []
    for r in tr:
        if chains:
            last = chains[-1]["members"][-1]
            end = int(last["tick_on"]) + int(last["notated_ticks"])
            if abs(int(r["tick_on"]) - end) <= gap_ticks:
                chains[-1]["members"].append(r)
                continue
        chains.append({"members": [r]})
    W = 4.0 * tpb
    for c in chains:
        m = c["members"]; r0 = m[0]
        if len(m) == 1:
            c["row"] = r0
            continue
        tk0 = int(r0["tick_on"])
        ev = []
        d, h = r0["dyn"], r0["hairpin"] or ""
        for k, r in enumerate(m):
            off = (int(r["tick_on"]) - tk0) / W
            L = int(r["notated_ticks"]) / W
            if k > 0:
                # the printed state this member starts with, as events at its start
                nd, nh = r["dyn"], r["hairpin"] or ""
                if h and (nd != d or nh != h):
                    if nd == d:
                        ev.append((off, h + "1"))  # hairpin stop without a new dynamic
                if nd != d and nd:
                    ev.append((off, "dyn:" + nd))
                if nh and (nh != h or nd != d):
                    ev.append((off, nh + "-1"))
            last = k == len(m) - 1
            for it in (r.get("inner") or "").split(";"):
                if not it:
                    continue
                rp, e = it.split(":", 1)
                if float(rp) >= L - 1e-9 and not last:
                    continue  # 'after' event of a member: the next member's own state carries it
                ev.append((off + float(rp), e))
            d, h = _hp_state(r["dyn"], r["hairpin"], r.get("inner"), L)
        end_tk = int(m[-1]["tick_on"]) + int(m[-1]["notated_ticks"])
        mr = dict(r0)
        mr["notated_ticks"] = end_tk - tk0
        mr["notated_s"] = round(float(m[-1]["t_on_s"]) + float(m[-1]["notated_s"]) - float(r0["t_on_s"]), 4)
        mr["inner"] = ";".join(f"{p:g}:{e}" for p, e in ev)
        mr["chain_n"] = len(m)
        c["row"] = mr
    return chains


def rolls(rows, bar_s, min_bars=1.0, tpb=None):
    """[(t_start, t_end, [bars], dyn, hairpin)] for timpani rolls longer than min_bars of their first bar.
    r07: with tpb, a roll is a chain of tremolo notes with no gap (roll_chains), not a single note."""
    out = []
    src = [c["row"] for c in roll_chains(rows, tpb)] if tpb else rows
    for r in src:
        if not key(r["staff"]).startswith("Timp") or "tremolo" not in (r["arts"] or ""):
            continue
        t0 = float(r["t_on_s"]); L = float(r["notated_s"]); b0 = int(r["bar"])
        blen = bar_s[b0] - bar_s[b0 - 1] if b0 < len(bar_s) else 2.0
        if L <= blen * min_bars * 1.01:
            continue
        bs = [b for b in range(1, len(bar_s)) if bar_s[b - 1] < t0 + L - 0.05 and bar_s[b] > t0 + 0.05]
        out.append((t0, t0 + L, bs, r["dyn"], r["hairpin"]))
    return out


def roll_segments(rows, mi, min_bars=1.0):
    """r05 (critic 4, plan 1d): the printed segments of each timpani roll longer than one bar, for the balance stage's
    roll rule (one cut per segment keeps the printed shape). A segment starts at the roll's start and at every printed
    dynamic or hairpin start/stop inside it (notes.csv 'inner'). Returns {roll t_start: [(first bar, last bar, kind)]},
    kind 'cresc' when a crescendo hairpin runs from the segment's start, else 'flat'."""
    import bisect
    tpb = mi["tpb"]; grid = list(mi["bar_ticks"])
    out = {}
    merged = {round(float(c["row"]["t_on_s"]), 3): c["row"] for c in roll_chains(rows, tpb)}
    for t0, t1, bs, dyn, hp in rolls(rows, mi["bar_s"], min_bars, tpb=tpb):
        r = merged[round(t0, 3)]
        tk0 = int(r["tick_on"]); L = int(r["notated_ticks"])
        cuts = [(bs[0], "cresc" if hp == "cresc" else "flat")]
        state = hp or ""
        for it in (r.get("inner") or "").split(";"):
            if not it:
                continue
            rp, e = it.split(":", 1)
            tk = tk0 + int(round(float(rp) * 4 * tpb))
            if tk >= tk0 + L:
                continue
            if e.startswith("dyn:") or e in ("cresc1", "decresc1"):
                state = ""
            elif e in ("cresc-1", "decresc-1"):
                state = e[:-2]
            b = bisect.bisect_right(grid, tk)  # 1-based bar of the event
            if b not in bs:
                continue
            if cuts[-1][0] == b:
                cuts[-1] = (b, "cresc" if state == "cresc" else "flat")
            else:
                cuts.append((b, "cresc" if state == "cresc" else "flat"))
        segs = []
        for k, (b, kind) in enumerate(cuts):
            e = cuts[k + 1][0] - 1 if k + 1 < len(cuts) else bs[-1]
            segs.append((b, e, kind))
        out[round(t0, 3)] = segs
    return out
