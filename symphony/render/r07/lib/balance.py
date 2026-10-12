#!/usr/bin/env python3
"""r03/r04: mix-stage balance from measured stem levels (riding the faders), for any version of either movement.

Input: the placed (wet) stems of one render, notes.csv rows, the bar grid, the marked melodies and the timpani rolls
derived from the score (lib/marks.py). Output: a slow gain curve (dB) per stem, applied by stem.py before pan and
room (stage 2), and a report.

Level measure: K-weighted momentary loudness (400 ms, 100 ms hop) while the staff's notes sound, power mean per bar,
the same measure as tools/stems.py stem_bars.csv, so the targets are the critics' measures.

1. Marked melodies (critic 2, plan 3 and 4; mock-up practice: balance between staves as a fader on the accompaniment
   as well as the melody, not an extra rise that lifts the whole bar,
   https://vi-control.net/community/threads/questions-about-prepping-ahead-for-dynamics-and-volume-for-orchestral-mock-ups.159951/):
   for each phrase, need = median over its bars of (loudest other stem + margin - melody). The melody gets at most
   lift_max_dB of it; every other stem that is louder than (melody - margin) is cut by its median excess (at most
   duck_max_dB). Stems that carry a marked melody in the same bar are never cut, and harp and percussion are left out
   of the comparison. If the melody stays more than sum_margin_dB under the power sum of all other stems (other
   melodies included), all other non-melody stems get a further common cut (within duck_max_dB). Marked melodies sounding together are brought level with
   each other (the softer one lifted within lift_max_dB, the louder one cut by at most mel_duck_max_dB).
   Several passes on the predicted levels (gains are linear).
2. Timpani rolls longer than a bar (Dan, BRIEF.md: long rolls must never be the loudest stem unless the score marks the
   timpani as leading): in every bar of such a roll the timpani is cut until it sits roll_margin_dB under the loudest
   other stem (at most roll_duck_max_dB), unless the timpani carries a solo/espr. mark there.
Gains are constant per bar and smoothed with a smooth_s moving average.
"""
import re
from collections import defaultdict
import numpy as np
import rtk

EXCL = ("Harp", "drums")


def key(name):
    k = re.sub(r"[^A-Za-z0-9 ]", "", name.split(":")[0]).strip()
    return k or "drums"


def bar_levels(x, sr, rows, bars):
    """({bar: LUFS while sounding}, {bar: LUFS over the whole bar}) for one stem (x: (n, 2) float)."""
    tM, M = rtk.loudness_series(x, sr, 0.4, 0.1)
    sounding = np.zeros_like(tM, dtype=bool)
    nb = defaultdict(int)
    for r in rows:
        t0 = float(r["t_on_s"]); t1 = float(r["t_off_s"]) if r["t_off_s"] not in ("", None) else t0 + float(r["notated_s"])
        sounding |= (tM >= t0 + 0.1) & (tM <= t1)
        nb[int(r["bar"])] += 1
    out, whole = {}, {}
    for b, a, e in bars:
        mw = (tM >= a) & (tM < e)
        if mw.any():
            whole[b] = rtk.power_mean_lufs(M[mw])
        if not nb.get(b):
            continue
        m = sounding & mw
        if m.sum() < 3:
            continue
        out[b] = rtk.power_mean_lufs(M[m])
    return out, whole


DY = ["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff"]


def printed_dyn(rows):
    """{stem: {bar: index into DY of the loudest printed dynamic of the stem's notes in that bar}} (r04)."""
    pd = defaultdict(dict)
    for r in rows:
        d = "p" if r["dyn"] == "fp" else r["dyn"]  # forte-piano: the held note is piano
        if d in DY:
            st = key(r["midi_track"]) if r.get("midi_track") else key(r["staff"]); b = int(r["bar"])
            pd[st][b] = max(pd[st].get(b, 0), DY.index(d))
    return pd


def compute(levels, bars, melodies, rolls, B, timp="Timpani", whole=None, pdyn=None, roll_segs=None):
    """levels: {stem: {bar: LUFS while sounding}}; whole: {stem: {bar: LUFS whole bar}}; bars: [(bar, t0, t1)];
    melodies: [(staff, [bars], ...)]; rolls: [(t0, t1, [bars], ...)]; pdyn: printed_dyn(rows).
    Returns ({stem: {bar: gain dB}}, report).

    r04 (critic 3, plan item 1): the balance obeys the printed dynamics.
      a. a stem printed LOUDER than the melody in a bar is never cut there; a stem printed at the same dynamic is cut by
         at most duck_same_dB, a stem printed softer by at most duck_max_dB;
      b. a phrase ends at the first bar where the melody is printed f or louder and at least tutti_frac of the sounding
         stems are printed f or louder (a tutti); no stem is cut in such tutti bars;
      c. marked melodies are never cut: concurrent marked melodies are only lifted (within lift_max_dB);
      d. the summed loudness of every bar stays within preserve_dB of its no-balance loudness (relief between staves,
         not a quieter bar);
      e. (curve) smoothing smooth_s, about 1.25 s: fader slopes of a few dB/s."""
    stems = sorted(levels)
    nbar = max(b for b, _, _ in bars)
    whole = whole or levels
    pdyn = pdyn or {}
    G = {s: np.zeros(nbar + 2) for s in stems}
    margin = B.get("margin_dB", 1.0); lift_max = B.get("lift_max_dB", 3.0); duck_max = B.get("duck_max_dB", 6.0)
    duck_same = B.get("duck_same_dB", 4.0)
    sum_margin = B.get("sum_margin_dB", -5.0); mel_margin = B.get("mel_margin_dB", 0.0)
    tutti_frac = B.get("tutti_frac", 0.5); F = DY.index("f")

    def pd(s, b):
        return pdyn.get(s, {}).get(b)

    # tutti bars: most sounding stems (harp and percussion left out) printed f or louder
    tutti = set()
    for b, _, _ in bars:
        snd = [s for s in stems if not s.startswith(EXCL) and levels[s].get(b) is not None and pd(s, b) is not None]
        if snd and sum(pd(s, b) >= F for s in snd) >= tutti_frac * len(snd):
            tutti.add(b)
    mels = []; cut_short = []; tstart = set()
    for st, bs, *rest in melodies:
        nb = []
        if B.get("tutti_lift_dB") and bs and bs[0] in tutti and (pd(st, bs[0]) or 0) >= F:
            # r05 (critic 4, plan 4): a marked phrase that STARTS in a printed f/ff tutti (m1 bassoons espr. f 33-40)
            # keeps a lift of at most tutti_lift_dB; nothing is cut in tutti bars (cap)
            nb = list(bs); tstart.add((st, bs[0]))
            mels.append((st, nb))
            continue
        for b in bs:
            if b in tutti and (pd(st, b) or 0) >= F:
                break
            nb.append(b)
        if len(nb) < len(bs):
            cut_short.append((st, bs[0], bs[-1], nb[-1] if nb else None))
        if nb:
            mels.append((st, nb))
    mel_at = defaultdict(set)
    for st, bs in mels:
        for b in bs:
            mel_at[b].add(st)

    def lev(s, b):
        v = levels[s].get(b)
        return None if v is None or not np.isfinite(v) else v + G[s][b]

    def cap(o, st, b):
        """largest cut (positive dB) allowed on stem o in bar b under melody st"""
        if b in tutti or o in mel_at[b]:
            return 0.0
        po = pd(o, b)
        # compare with the softest marked melody sounding in the bar, so that a cut made for one melody never puts
        # a stem under another melody printed softer than it
        pms = [pd(m, b) for m in mel_at[b] | {st} if pd(m, b) is not None]
        pm = min(pms) if pms else None
        if po is None or pm is None:
            return duck_same
        if po > pm:
            return 0.0
        return duck_same if po == pm else duck_max

    def duck(o, st, bs, d):
        for b in bs:
            G[o][b] = max(G[o][b] - d, min(G[o][b], -cap(o, st, b)))

    inv_margin = B.get("inv_margin_dB")

    def ceiling(st, b):
        """largest lift in bar b that keeps melody st at most inv_margin_dB over every sounding stem printed LOUDER
        than it (a lift must not turn the printed order upside down; r04)"""
        if inv_margin is None:
            return 99.0
        m = lev(st, b); pm = pd(st, b)
        if m is None or pm is None:
            return 99.0
        lo = [lev(o, b) for o in stems if o != st and not o.startswith(EXCL) and lev(o, b) is not None
              and pd(o, b) is not None and pd(o, b) > pm]
        return max(0.0, min(lo) + inv_margin - m) if lo else 99.0

    def others(st, b):
        return {o: lev(o, b) for o in stems if o != st and lev(o, b) is not None and not o.startswith(EXCL) and o not in mel_at[b]}

    rep = {"melodies": [], "rolls": [], "tutti_bars": sorted(tutti), "phrases_ended_at_tutti": cut_short}
    for it in range(B.get("passes", 3)):
        for st, bs in mels:
            if st not in levels:
                continue
            need = []; per_b = {}
            for b in bs:
                m = lev(st, b); o = others(st, b)
                if m is None or not o:
                    continue
                need.append(max(o.values()) + margin - m); per_b[b] = (m, o)
            if not need:
                continue
            nd = float(np.median(need))
            lmax = min(lift_max, B.get("tutti_lift_dB", lift_max)) if (st, bs[0]) in tstart else lift_max
            if B.get("per_bar_need"):
                # r05 (critic 4, plan 4): the need per bar (median of the bar and its neighbours in the phrase),
                # not the phrase median: short phrases and phrases whose competitor changes from bar to bar get
                # their relief; lifts and cuts per bar, under the same caps (cap(), ceiling(), lift_max)
                pbs = [b for b in bs if b in per_b]
                nneed = {}
                for i, b in enumerate(pbs):
                    w = [per_b[q][1] and (max(per_b[q][1].values()) + margin - per_b[q][0]) for q in pbs[max(0, i - 1):i + 2]]
                    nneed[b] = float(np.median(w))
                for b in pbs:
                    if nneed[b] <= 0.2:
                        continue
                    m, o = per_b[b]
                    lift = float(np.clip(nneed[b], 0, max(0.0, lmax - G[st][b])))
                    lift = min(lift, ceiling(st, b))
                    G[st][b] += lift
                    for oo, v in o.items():
                        e = v - (m + lift - margin)
                        if e > 0.2:
                            duck(oo, st, [b], e)
            elif nd > 0.2:
                cur = float(np.median([G[st][b] for b in bs]))
                lift = float(np.clip(nd, 0, max(0.0, lmax - cur)))
                lb = {b: min(lift, ceiling(st, b)) for b in bs}
                for b in bs:
                    G[st][b] += lb[b]
                exc = defaultdict(list)
                for b, (m, o) in per_b.items():
                    for oo, v in o.items():
                        exc[oo].append(v - (m + lb[b] - margin))
                for oo, ex in exc.items():
                    e = float(np.median(ex))
                    if e > 0.2:
                        duck(oo, st, bs, e)
            # concurrent marked melodies: the softer one is lifted (within lift_max_dB); none is cut
            needm = []
            for b in bs:
                m = lev(st, b)
                mo = [lev(o, b) for o in mel_at[b] if o != st and lev(o, b) is not None]
                if m is None or not mo:
                    continue
                needm.append(max(mo) - mel_margin - m)
            if needm and np.median(needm) > 0.2:
                cur = float(np.median([G[st][b] for b in bs]))
                lift = float(np.clip(float(np.median(needm)), 0, max(0.0, lift_max - cur)))
                for b in bs:
                    G[st][b] += min(lift, ceiling(st, b))
            # power sum of the others
            sm = []
            for b in bs:
                m = lev(st, b)
                o = [lev(oo, b) for oo in stems if oo != st and not oo.startswith(EXCL)]
                o = [v for v in o if v is not None]
                if m is not None and o:
                    sm.append(m - 10 * np.log10(sum(10 ** (v / 10) for v in o)))
            if sm and np.median(sm) < sum_margin:
                d = float(sum_margin - np.median(sm))
                for oo in set(oo for b in bs for oo in others(st, b)):
                    duck(oo, st, bs, d)
    for s in stems:  # a stem is never raised by more than lift_max_dB (lifts of overlapping passes do not add up)
        G[s] = np.minimum(G[s], lift_max)
    # d. keep each bar's summed loudness within preserve_dB of the no-balance bar
    pres = B.get("preserve_dB")
    rep["bar_offset_dB"] = {}
    if pres is not None:
        for b, _, _ in bars:
            P0 = P1 = 0.0
            for s in stems:
                v = whole.get(s, {}).get(b)
                if v is None or not np.isfinite(v) or v < -90:
                    continue
                P0 += 10 ** (v / 10); P1 += 10 ** ((v + G[s][b]) / 10)
            if P0 <= 0 or P1 <= 0:
                continue
            diff = 10 * np.log10(P0 / P1)
            off = float(np.sign(diff) * max(0.0, abs(diff) - pres))
            if abs(off) > 0.05 and any(abs(G[s][b]) > 0.05 for s in stems):
                for s in stems:
                    G[s][b] += off
                rep["bar_offset_dB"][b] = round(off, 2)
    for st, bs in mels:
        if st in levels:
            rep["melodies"].append({"staff": st, "bars": [bs[0], bs[-1]], "lift_dB": round(float(np.median([G[st][b] for b in bs])), 1)})
    # timpani rolls: whole-bar levels (a roll fills its bars; the critics' roll table uses whole-bar levels)
    def levw(s, b):
        v = whole.get(s, {}).get(b)
        return None if v is None or not np.isfinite(v) or v < -90 else v + G[s][b]
    if timp in levels:
        rm = B.get("roll_margin_dB", 3.0); rmax = B.get("roll_duck_max_dB", 15.0)
        rmc = B.get("roll_margin_cresc_dB", 0.5)
        for t0, t1, bs, dyn, hp in rolls:
            r = {"bars": [bs[0], bs[-1]], "dyn": dyn, "cut_dB": []}
            segs = (roll_segs or {}).get(round(t0, 3)) or [(b, b, "flat") for b in bs]
            if roll_segs is None:
                segs = [(b, b, "flat") for b in bs]
            r["segments"] = segs
            carry = 0.0
            for a, e, kind in segs:
                # r05 (critic 4, plan 1d): one cut per printed segment of the roll (the largest any of its bars needs),
                # so the printed shape and the settle survive; the others' level is their level while sounding (a
                # stem entering late in a bar no longer counts as quiet and makes an exposed roll look too loud);
                # inside a printed crescendo the timpani is only kept under the loudest stem (roll_margin_cresc_dB)
                need = []; floor = {}
                for b in range(a, e + 1):
                    if b not in bs or timp in mel_at[b]:
                        continue
                    # r07 (critic 6, plan 1): the timpani may lead only where it is printed louder than every
                    # sounding stem; where it is printed softer than the loudest printed stem it sits a further
                    # roll_margin_step_dB per printed step under it (a f roll under a ff tutti: 3-9 dB under)
                    tp_ = pd(timp, b)
                    op_ = [pd(oo, b) for oo in stems if oo not in (timp, "drums") and not oo.startswith(EXCL)
                           and levels[oo].get(b) is not None and pd(oo, b) is not None]
                    if tp_ is not None and op_ and tp_ > max(op_) and B.get("roll_lead_if_printed_louder", True):
                        continue
                    # (not inside a printed crescendo: the bar's printed timpani dynamic is only where the roll starts)
                    xm = 0.0 if kind == "cresc" else B.get("roll_margin_step_dB", 0.0) * max(0, (max(op_) if op_ else 0) - (tp_ if tp_ is not None else 99))
                    m = levw(timp, b)
                    o = []
                    for oo in stems:
                        if oo in (timp, "drums"):
                            continue
                        v = lev(oo, b) if B.get("roll_others_sounding", True) else None
                        o.append(v if v is not None else levw(oo, b))
                    o = [v for v in o if v is not None]
                    if m is None or not o:
                        continue
                    need.append(m - (max(o) - (rmc if kind == "cresc" else rm) - xm))
                    # never the loudest stem over the whole bar either (Dan): whole-bar levels, roll_margin_whole_dB,
                    # per bar (an exposed first bar, where the roll sounds alone before the others enter, would
                    # otherwise pull the whole roll down and mask its end)
                    ow = [levw(oo, b) for oo in stems if oo not in (timp, "drums")]
                    ow = [v for v in ow if v is not None]
                    if ow:
                        floor[b] = m - (max(ow) - B.get("roll_margin_whole_dB", 0.5))
                d = float(np.clip(max(need), 0, rmax)) if need else 0.0
                if B.get("roll_carry_cut", True):
                    # r06 (critic 5, plan 4c): the largest cut so far carries into later segments unless a printed
                    # crescendo starts there, so a later, softer-printed segment is never made relatively louder
                    # (r05: m2 2-3 printed > rendered -0.7 dB; m1 122-130 fff > pp narrowed by 3 dB)
                    if kind != "cresc":
                        d = max(d, carry)
                    carry = d
                fl = 0.0
                for b in range(a, e + 1):
                    # the whole-bar floor holds from the bar that needs it to the segment's end (the cut never
                    # falls inside a segment, so it cannot undo the settle)
                    fl = max(fl, floor.get(b, 0.0))
                    if b in bs and timp not in mel_at[b]:
                        G[timp][b] -= float(np.clip(max(d, fl), 0, rmax))
                r["cut_dB"].append(round(d, 1))
            rep["rolls"].append(r)
    # r07 (critic 6, plan 5): "spot microphone" on exposed soft solos. Where a marked melody plays printed <= mf and at
    # most spot_max_stems stems sound, the bar's sounding stems are raised together (relief kept) toward the median
    # loudness of the bars printed at the same (loudest printed) dynamic, at most spot_lift_max_dB, never past
    # spot_target_dB under that median. Recordings put spot microphones on solo winds and ride them with the score;
    # a solo wind over a thin texture otherwise sits 4-8 dB under the median bar of its printed dynamic.
    sl = B.get("spot_lift_max_dB", 0.0)
    rep["spot_lift"] = {}
    if sl > 0:
        MF = DY.index("mf")
        def bar_pow(b):
            v = [levw(s, b) for s in stems if s != "drums"]
            v = [x for x in v if x is not None]
            return 10 * np.log10(sum(10 ** (x / 10) for x in v)) if v else None
        bdyn = {}
        for b, _, _ in bars:
            ds = [pd(s, b) for s in stems if s != "drums" and levels[s].get(b) is not None and pd(s, b) is not None]
            if ds:
                bdyn[b] = max(ds)
        P = {b: bar_pow(b) for b in bdyn}
        med = {}
        for d in set(bdyn.values()):
            vals = [P[b] for b in bdyn if bdyn[b] == d and P[b] is not None]
            if len(vals) >= 3:
                med[d] = float(np.median(vals))
        for b in sorted(bdyn):
            ms = [st for st in mel_at[b] if (pd(st, b) or 0) <= MF]
            if not ms or bdyn[b] > MF or P[b] is None or bdyn[b] not in med:
                continue
            snd = [s for s in stems if s != "drums" and levels[s].get(b) is not None]
            if len(snd) > B.get("spot_max_stems", 4):
                continue
            up = float(np.clip(med[bdyn[b]] + B.get("spot_target_dB", -1.0) - P[b], 0.0, sl))
            if up > 0.05:
                for s in snd:
                    G[s][b] += up
                rep["spot_lift"][b] = round(up, 1)
    gains = {s: {b: float(G[s][b]) for b in range(1, nbar + 1) if abs(G[s][b]) > 0.05} for s in stems}
    rep["stems_changed"] = {s: [round(min(g.values()), 1), round(max(g.values()), 1)] for s, g in gains.items() if g}
    return gains, rep, mels


def curve(gb, bars, end_s, smooth_s=0.4, dt=0.01):
    """(times, dB) on a dt grid from per-bar gains, smoothed with a smooth_s moving average."""
    t = np.arange(0.0, end_s + dt, dt)
    g = np.zeros_like(t)
    for b, a, e in bars:
        if b in gb:
            g[(t >= a) & (t < e)] = gb[b]
    k = max(1, int(smooth_s / dt))
    g = np.convolve(np.pad(g, (k // 2, k - k // 2 - 1), mode="edge"), np.ones(k) / k, mode="valid")
    return np.stack([t, g])
