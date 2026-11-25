"""mvt2 c55: statistics of the track volume envelopes that build_reaper.py would write for a build folder.

Usage: env_stats.py BUILD_DIR [--src build_reaper.py] [--json OUT.json] [--all]
  BUILD_DIR holds parts.json and mix.json. Nothing is sent to REAPER (build_reaper.py is read up to ENV_LUA only).
Per track: points, points per second (of the piece) and per sounding second, envelope travel in dB (sum of |steps|),
the share of the travel inside single notes (more than 40 ms from a note's start and end), at note edges and in rests,
the notes whose envelope moves 3 dB or more inside the note, and how many of those carry no hairpin, dynamic change or
accent ("unmarked"). With parts.json `vol_cls` (score_to_parts.py from c55) also the travel per class (slow / level /
shape; slow is the written envelope minus the level and shape lanes, so it holds the mix trims and the phrase arch).
"""
import bisect, json, os, sys
import numpy as np

BUILD = sys.argv[1]
rest = sys.argv[2:]
SRCF = rest[rest.index("--src") + 1] if "--src" in rest else os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_reaper.py")
SRC = open(SRCF).read()
SRC = SRC[:SRC.index("ENV_LUA = ")]
ns = {"__name__": "build_reaper_partial"}
argv = sys.argv
sys.argv = ["build_reaper.py", os.path.join(BUILD, "parts.json"), "/private/tmp/claude-501/mockup-loop/mvt2-stemfix-jobs"]
try:
    exec(compile(SRC, "build_reaper.py", "exec"), ns)
finally:
    sys.argv = argv
D, PRE, q2s = ns["d"], ns["PRE"], ns["q2s"]
END_S = q2s(D["score_end"])
SC = ns.get("ENV_SCALE", lambda db: 10 ** (db / 80.0))


def env_fn(vp):
    t = np.array([q2s(p["qn"] - PRE) if p["qn"] >= PRE else -1.0 for p in vp])
    v = np.array([p["db"] for p in vp])
    return t, v


def at(t, v, x):
    """the written envelope at times x (REAPER's fader-scale line between points)"""
    return 80 * np.log10(np.interp(x, t, 10 ** (v / 80)))


def step_lane(lane, qs):
    if not lane:
        return np.zeros(len(qs))
    lq = np.array([p[0] for p in lane]); lv = np.array([0.0] + [p[1] for p in lane])
    return lv[np.searchsorted(lq, np.array(qs) + 1e-6, side="right")]


rows, tot = [], {"points": 0, "travel": 0.0, "inside": 0.0, "edge": 0.0, "rest": 0.0, "notes": 0, "n3": 0, "n3_unmarked": 0,
                 "cls": {"slow": 0.0, "level": 0.0, "shape": 0.0}}
for tr in D["tracks"]:
    vp = ns["vol_points"](tr)
    t, v = env_fn(vp)
    m = t >= 0
    t, v = t[m], v[m]
    # distinct onsets: (moved on s, end s, score on qn, end qn)
    by = {}
    for n in tr["notes"]:
        k = round(n["qn"], 3)
        e = n["qn"] + n["dur"]
        by[k] = max(by.get(k, e), e)
    ons = sorted(by)
    spans = []
    for i, o in enumerate(ons):
        e = by[o] if i + 1 == len(ons) else min(by[o], ons[i + 1])
        spans.append((q2s(o), q2s(e), o, e))
    snd = sum(b - a for a, b, _, _ in spans)
    # travel by segment, allotted by the segment's midpoint
    seg = np.abs(np.diff(v)); mid = 0.5 * (t[1:] + t[:-1])
    starts = np.array([a for a, b, _, _ in spans]); ends = np.array([b for a, b, _, _ in spans])
    ins = np.zeros(len(mid), bool); edg = np.zeros(len(mid), bool)
    for a, b in zip(starts, ends):
        ins |= (mid > a + 0.04) & (mid < b - 0.04)
        edg |= (np.abs(mid - a) <= 0.04) | (np.abs(mid - b) <= 0.04)
    edg &= ~ins
    travel = float(seg.sum())
    n3 = n3u = 0
    hp = tr.get("hairpins", []); dc = tr.get("dyn_curve", []); acc = set(round(x, 2) for x in tr.get("accent_q", []))
    for a, b, oq, eq in spans:
        if b - a < 0.12:
            continue
        xs = np.concatenate([np.arange(a + 0.04, b - 0.04, 0.01), t[(t > a + 0.04) & (t < b - 0.04)]])
        if len(xs) < 2:
            continue
        ev = at(t, v, xs)
        if ev.max() - ev.min() >= 3.0:
            n3 += 1
            marked = any(h0 < eq - 0.05 and h1 > oq + 0.05 for h0, h1, *_ in hp) or any(oq + 0.05 < q < eq - 0.05 for q, _ in dc) \
                or tr.get("family") == "timp" or eq >= D["score_end"] - 3.01
            n3u += 0 if marked else 1
    r = {"track": tr["name"], "points": len(vp), "onsets": len(ons), "per_onset": len(vp) / max(1, len(ons)),
         "per_s": len(vp) / END_S, "per_sounding_s": len(vp) / max(1e-9, snd), "travel": travel,
         "inside": float(seg[ins].sum()), "edge": float(seg[edg].sum()), "rest": float(seg[~ins & ~edg].sum()),
         "n3": n3, "n3_unmarked": n3u}
    if tr.get("vol_cls"):
        g = sorted({p["qn"] - PRE for p in vp if p["qn"] >= PRE} | {q for c in tr["vol_cls"].values() for q, _ in c})
        lv, sh = step_lane(tr["vol_cls"].get("level", []), g), step_lane(tr["vol_cls"].get("shape", []), g)
        gt = np.array([q2s(q) for q in g])
        full = at(t, v, gt)
        r["cls"] = {"level": float(np.abs(np.diff(lv)).sum()), "shape": float(np.abs(np.diff(sh)).sum()),
                    "slow": float(np.abs(np.diff(full - lv - sh)).sum())}
        for c in r["cls"]:
            tot["cls"][c] += r["cls"][c]
    rows.append(r)
    for k in ("points", "travel", "inside", "edge", "rest", "n3", "n3_unmarked"):
        tot[k] += r[k]
    tot["notes"] += len(ons)
print(f"{'track':17s} points onsets /onset   /s  /snd s  travel dB  inside  notes>=3dB  unmarked")
for r in rows:
    if "--all" in rest or r["points"] >= 0:
        print(f"{r['track']:17s} {r['points']:6d} {r['onsets']:6d} {r['per_onset']:6.1f} {r['per_s']:5.2f} {r['per_sounding_s']:6.2f} "
              f"{r['travel']:9.0f}  {100 * r['inside'] / max(1e-9, r['travel']):5.0f}%  {r['n3']:6d}  {r['n3_unmarked']:6d}")
print(f"\nall {len(rows)} tracks, {END_S:.0f} s: {tot['points']} points, {tot['points'] / END_S:.1f} per second in total, "
      f"{tot['points'] / max(1, tot['notes']):.1f} per onset ({tot['notes']} onsets)")
print(f"travel {tot['travel']:.0f} dB: inside single notes {100 * tot['inside'] / tot['travel']:.0f} %, within 40 ms of a note's "
      f"start or end {100 * tot['edge'] / tot['travel']:.0f} %, in rests {100 * tot['rest'] / tot['travel']:.0f} %")
print(f"notes moving 3 dB or more inside the note: {tot['n3']} of {tot['notes']} ({100 * tot['n3'] / max(1, tot['notes']):.0f} %), "
      f"unmarked {tot['n3_unmarked']}")
if any("cls" in r for r in rows):
    c = tot["cls"]
    print(f"travel by class (lanes before they are summed): slow {c['slow']:.0f} dB, level {c['level']:.0f}, shape {c['shape']:.0f}")
if "--json" in rest:
    json.dump({"tracks": rows, "total": tot, "end_s": END_S}, open(rest[rest.index("--json") + 1], "w"), indent=1)
