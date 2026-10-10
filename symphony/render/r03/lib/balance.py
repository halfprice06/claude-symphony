#!/usr/bin/env python3
"""r03: mix-stage balance from measured stem levels (riding the faders), for any version of either movement.

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


def compute(levels, bars, melodies, rolls, B, timp="Timpani", whole=None):
    """levels: {stem: {bar: LUFS while sounding}}; whole: {stem: {bar: LUFS whole bar}} (for the roll rule); bars: [(bar, t0, t1)]; melodies: [(staff, [bars], ...)]; rolls: [(t0, t1, [bars], ...)].
    Returns ({stem: {bar: gain dB}}, report)."""
    stems = sorted(levels)
    nbar = max(b for b, _, _ in bars)
    G = {s: np.zeros(nbar + 2) for s in stems}
    mel_at = defaultdict(set)
    for st, bs, *_ in melodies:
        for b in bs:
            mel_at[b].add(st)
    margin = B.get("margin_dB", 1.0); lift_max = B.get("lift_max_dB", 3.0); duck_max = B.get("duck_max_dB", 6.0)
    sum_margin = B.get("sum_margin_dB", -5.0)
    mel_margin = B.get("mel_margin_dB", 0.5); mel_duck_max = B.get("mel_duck_max_dB", 4.0)

    def lev(s, b):
        v = levels[s].get(b)
        return None if v is None or not np.isfinite(v) else v + G[s][b]

    def others(st, b):
        return {o: lev(o, b) for o in stems if o != st and lev(o, b) is not None and not o.startswith(EXCL) and o not in mel_at[b]}

    rep = {"melodies": [], "rolls": []}
    for it in range(B.get("passes", 3)):
        for st, bs, *rest in melodies:
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
            if nd > 0.2:
                cur = float(np.median([G[st][b] for b in bs]))
                lift = float(np.clip(nd, 0, max(0.0, lift_max - cur)))
                for b in bs:
                    G[st][b] += lift
                exc = defaultdict(list)
                for b, (m, o) in per_b.items():
                    for oo, v in o.items():
                        exc[oo].append(v - (m + lift - margin))
                for oo, ex in exc.items():
                    e = float(np.median(ex))
                    if e > 0.2:
                        room = duck_max + float(np.min([G[oo][b] for b in bs]))
                        d = float(np.clip(e, 0, max(0.0, room)))
                        for b in bs:
                            if oo not in mel_at[b]:
                                G[oo][b] -= d
            # concurrent marked melodies (e.g. Violins I + II, clarinets and horns all espr. in the same bars):
            # bring them level with each other (within mel_margin_dB): the softer one gets what is left of its lift,
            # the louder one gives up to mel_duck_max_dB
            needm = []; per_m = {}
            for b in bs:
                m = lev(st, b)
                mo = {o: lev(o, b) for o in mel_at[b] if o != st and lev(o, b) is not None}
                if m is None or not mo:
                    continue
                needm.append(max(mo.values()) - mel_margin - m); per_m[b] = (m, mo)
            if needm and np.median(needm) > 0.2:
                nd = float(np.median(needm))
                cur = float(np.median([G[st][b] for b in bs]))
                lift = float(np.clip(nd, 0, max(0.0, lift_max - cur)))
                for b in bs:
                    G[st][b] += lift
                exc = defaultdict(list)
                for b, (m, mo) in per_m.items():
                    for oo, v in mo.items():
                        exc[oo].append((b, v - (m + lift + mel_margin)))
                for oo, ex in exc.items():
                    e = float(np.median([x for _, x in ex]))
                    if e > 0.2:
                        bb = [b for b, _ in ex]
                        room = mel_duck_max + float(np.min([min(0.0, G[oo][b]) for b in bb]))
                        d = float(np.clip(e, 0, max(0.0, room)))
                        for b in bb:
                            G[oo][b] -= d
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
                    room = duck_max + float(np.min([G[oo][b] for b in bs]))
                    dd = float(np.clip(d, 0, max(0.0, room)))
                    for b in bs:
                        if oo not in mel_at[b]:
                            G[oo][b] -= dd
    for s in stems:  # a stem is never raised by more than lift_max_dB (lifts of overlapping passes do not add up)
        G[s] = np.minimum(G[s], lift_max)
    for st, bs, *rest in melodies:
        if st in levels:
            rep["melodies"].append({"staff": st, "bars": [bs[0], bs[-1]], "lift_dB": round(float(np.median([G[st][b] for b in bs])), 1)})
    # timpani rolls: whole-bar levels (a roll fills its bars; the critics' roll table uses whole-bar levels)
    whole = whole or levels
    def levw(s, b):
        v = whole.get(s, {}).get(b)
        return None if v is None or not np.isfinite(v) or v < -90 else v + G[s][b]
    if timp in levels:
        rm = B.get("roll_margin_dB", 3.0); rmax = B.get("roll_duck_max_dB", 15.0)
        for t0, t1, bs, dyn, hp in rolls:
            r = {"bars": [bs[0], bs[-1]], "dyn": dyn, "cut_dB": []}
            for b in bs:
                if timp in mel_at[b]:
                    r["cut_dB"].append(0.0); continue
                m = levw(timp, b)
                o = [levw(oo, b) for oo in stems if oo not in (timp, "drums")]
                o = [v for v in o if v is not None]
                if m is None or not o:
                    r["cut_dB"].append(0.0); continue
                ex = m - (max(o) - rm)
                d = float(np.clip(ex, 0, rmax))
                G[timp][b] -= d; r["cut_dB"].append(round(d, 1))
            rep["rolls"].append(r)
    gains = {s: {b: float(G[s][b]) for b in range(1, nbar + 1) if abs(G[s][b]) > 0.05} for s in stems}
    rep["stems_changed"] = {s: [round(min(g.values()), 1), round(max(g.values()), 1)] for s, g in gains.items() if g}
    return gains, rep


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
