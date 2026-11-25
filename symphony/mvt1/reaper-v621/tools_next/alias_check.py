"""mvt1 c46 (critic B #1): check that a test alias plays exactly its source's data where it plays, before its stem is
compared with the source's stem or replaces it.

c45 judged three release-trail tests and two legato tests on whole-piece aliases whose CC1 / CC11 lanes were not their
sources' (score_to_parts.py carried "espr." boosts to the window's end; fixed with alias_dup()), and a test stem
replaced the Violas stem with the violas 3-7 dB too loud in six bars. Run this on the build a test was rendered from.

Usage: alias_check.py PARTS [MIX] [track ...] [--allow KEY ...] [--stems MAIN.wav TEST.wav]
  PARTS: a parts.json; MIX: its mix.json (default: mix.json next to PARTS). Tracks: alias names (default: every track
  with "test": true and "alias_of"). For each alias, over its sounding spans (each note's moved onset to its end) and
  its windows (parts.json "alias_windows", else its notes' score onsets):
  - notes (score onset, pitch, moved onset, length, velocity) against the source's notes in the windows;
  - the keyswitch row in effect at each note's moved onset, and the keyswitch events inside each window's span;
  - every CC lane (cc1, cc11, cc7, cc15, cc36, cc70): the held value at every point time of either lane inside the
    sounding spans and at each span's start;
  - the written volume envelope (build_reaper.vol_points with each track's mix entry; 0.05 dB) at every point time
    inside the sounding spans;
  - the mix.json entries (keys not starting with "_"): listed when they differ (only the key under test should).
  Exit 1 when any parts.json data differ, unless the data class is listed with --allow (notes, ks, cc1, cc11, cc7,
  cc15, cc36, cc70, vol). --stems: the per-bar (4 qn) level difference of two rendered stems (score time, pre-roll
  cut), with bars beyond 1 dB listed.
"""
import bisect, json, os, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
LANES = ("cc1", "cc11", "cc7", "cc15", "cc36", "cc70")
EPS = 1e-6


def load_build(parts, mix):
    """build_reaper.py's code above its Lua jobs, run on this parts.json / mix.json (as stem_fix.py does)"""
    src = open(os.path.join(TOOLS, "build_reaper.py")).read()
    src = src[:src.index("ENV_LUA = ")]
    ns = {"__name__": "build_reaper_partial"}
    argv = sys.argv
    sys.argv = ["build_reaper.py", parts, "/private/tmp/claude-501/mockup-loop/alias-check-jobs"]
    try:
        exec(compile(src, "build_reaper.py", "exec"), ns)
    finally:
        sys.argv = argv
    if mix is not None and os.path.abspath(mix) != os.path.abspath(os.path.join(os.path.dirname(parts), "mix.json")):
        ns["MIX"].clear()
        ns["MIX"].update(json.load(open(mix)))
    return ns


def held(lane, t, default=None):
    """value of a step lane [[qn, v], ...] at qn t"""
    xs = [p[0] for p in lane]
    k = bisect.bisect_right(xs, t + EPS)
    return lane[k - 1][1] if k else (lane[0][1] if lane else default)


def lin(pts, t):
    xs = [p["qn"] for p in pts]
    k = bisect.bisect_left(xs, t)
    if k <= 0:
        return pts[0]["db"]
    if k >= len(xs):
        return pts[-1]["db"]
    a, b = pts[k - 1], pts[k]
    return a["db"] + (b["db"] - a["db"]) * (t - a["qn"]) / max(1e-12, b["qn"] - a["qn"])


def check(ns, alias, allow=()):
    """list of (data class, message) differences of alias against its source"""
    tracks = {t["name"]: t for t in ns["d"]["tracks"]}
    a = tracks[alias]
    s = tracks[a["alias_of"]]
    wins = [tuple(w) for w in a.get("alias_windows", [])]
    if not wins and a["notes"]:
        wins = [(min(n["sq"] for n in a["notes"]), max(n["sq"] for n in a["notes"]) + 1e-3)]
    inw = lambda q: any(w0 - EPS <= q < w1 - EPS for w0, w1 in wins)
    out = []
    key = lambda n: (round(n["sq"], 4), n["pitch"], round(n["qn"], 4), round(n["dur"], 4), n["vel"])
    na = sorted(key(n) for n in a["notes"])
    nb = sorted(key(n) for n in s["notes"] if inw(n["sq"]))
    if na != nb:
        only_a = sorted(set(na) - set(nb))[:4]
        only_s = sorted(set(nb) - set(na))[:4]
        out.append(("notes", f"{len(na)} alias / {len(nb)} source notes in the windows; alias only {only_a}, source only {only_s}"))
    spans = sorted((n["qn"], n["qn"] + n["dur"]) for n in a["notes"])
    insp = lambda q: any(x0 - EPS <= q <= x1 + EPS for x0, x1 in spans)
    # keyswitch row in effect at each moved onset, and the events inside each window's span
    ksa = sorted((k["qn"], k["art"]) for k in a["ks"])
    kss = sorted((k["qn"], k["art"]) for k in s["ks"])
    bad = [n["qn"] for n in a["notes"] if held([[q, r] for q, r in ksa], n["qn"]) != held([[q, r] for q, r in kss], n["qn"])]
    if bad:
        out.append(("ks", f"row differs at {len(bad)} onsets, first {bad[:4]}"))
    for w0, w1 in wins:
        on_ = [n for n in a["notes"] if w0 - EPS <= n["sq"] < w1 - EPS]
        if not on_:
            continue
        x0, x1 = min(n["qn"] for n in on_) - 0.05, max(n["qn"] + n["dur"] for n in on_)
        ea = [(round(q, 4), r) for q, r in ksa if x0 <= q <= x1]
        es = [(round(q, 4), r) for q, r in kss if x0 <= q <= x1]
        if ea != es:
            out.append(("ks", f"keyswitch events in {w0}-{w1}: alias {len(ea)} / source {len(es)}; first differing "
                              f"{next(((p, q) for p, q in zip(ea + [None] * 9, es + [None] * 9) if p != q), None)}"))
    for ln in LANES:
        la, ls = a.get(ln, []), s.get(ln, [])
        if not la and not ls:
            continue
        ts = sorted({p[0] for p in la + ls if insp(p[0])} | {x0 for x0, _ in spans})
        diff = [(round(t, 4), held(la, t), held(ls, t)) for t in ts if held(la, t) != held(ls, t)]
        if diff:
            out.append((ln, f"{len(diff)} of {len(ts)} sounding times differ, e.g. {diff[:3]} (qn, alias, source); "
                            f"largest {max(abs((x[1] or 0) - (x[2] or 0)) for x in diff)}"))
    if alias not in ns["MIX"]["tracks"]:
        out.append(("mix", f"no mix.json entry for {alias}: the source's is used here, build_reaper.py would stop"))
        ns["MIX"]["tracks"][alias] = ns["MIX"]["tracks"][a["alias_of"]]
    va, vs = ns["vol_points"](a), ns["vol_points"](s)
    pre = ns["PRE"]
    ts = sorted({p["qn"] for p in va + vs if insp(p["qn"] - pre)} | {x0 + pre for x0, _ in spans})
    diff = [(round(t - pre, 4), round(lin(va, t), 2), round(lin(vs, t), 2)) for t in ts if abs(lin(va, t) - lin(vs, t)) > 0.05]
    if diff:
        out.append(("vol", f"{len(diff)} of {len(ts)} sounding times differ by over 0.05 dB, e.g. {diff[:3]} (qn, alias, "
                           f"source); largest {max(abs(x[1] - x[2]) for x in diff):.2f} dB"))
    ma, ms = ns["mix_for"](alias), ns["mix_for"](a["alias_of"])
    mk = sorted(k for k in set(ma) | set(ms) if not k.startswith("_") and ma.get(k) != ms.get(k))
    return out, mk


def stems(ns, main, test):
    import numpy as np
    import soundfile as sf
    xa, sr = sf.read(main, dtype="float64", always_2d=True)
    xb, _ = sf.read(test, dtype="float64", always_2d=True)
    n = min(len(xa), len(xb))
    q2s = ns["q2s"]
    pre = ns["PRE"]
    end = ns["d"]["score_end"]
    rows = []
    for b in range(int(end // 4)):
        i0, i1 = int(q2s(4 * b) * sr) - int(q2s(0) * sr), int(q2s(4 * b + 4) * sr) - int(q2s(0) * sr)
        i0, i1 = max(0, i0), min(n, i1)
        if i1 <= i0:
            continue
        pa = np.mean(xa[i0:i1] ** 2) + 1e-20
        pb = np.mean(xb[i0:i1] ** 2) + 1e-20
        lv = 10 * np.log10(pa)
        rows.append((b + 1, 10 * np.log10(pb / pa), lv))
    return rows


def main():
    args = sys.argv[1:]
    allow = []
    stem_pair = None
    if "--allow" in args:
        i = args.index("--allow")
        j = i + 1
        while j < len(args) and not args[j].startswith("--"):
            allow.append(args[j]); j += 1
        args = args[:i] + args[j:]
    if "--stems" in args:
        i = args.index("--stems")
        stem_pair = args[i + 1:i + 3]
        args = args[:i] + args[i + 3:]
    parts = args[0]
    mix = args[1] if len(args) > 1 and args[1].endswith(".json") else None
    names = args[2:] if mix else args[1:]
    ns = load_build(parts, mix)
    tracks = ns["d"]["tracks"]
    if not names:
        names = [t["name"] for t in tracks if t.get("test") and t.get("alias_of")]
    fail = False
    for nm in names:
        diffs, mk = check(ns, nm, allow)
        hard = [d for d in diffs if d[0] not in allow]
        fail |= bool(hard)
        src = next(t for t in tracks if t["name"] == nm)["alias_of"]
        print(f"ALIAS CHECK {nm} (of {src}): {'OK' if not diffs else 'DIFFERS'}; mix keys differing: {mk or 'none'}")
        for c, m in diffs:
            print(f"  {c}{' (allowed)' if c in allow else ''}: {m}")
    if stem_pair:
        rows = stems(ns, *stem_pair)
        off = [r for r in rows if abs(r[1]) > 1.0 and r[2] > -80]
        med = sorted(r[1] for r in rows if r[2] > -80)
        print(f"STEMS {os.path.basename(stem_pair[1])} - {os.path.basename(stem_pair[0])}: median per bar "
              f"{med[len(med) // 2]:+.2f} dB; bars beyond 1 dB (bar, dB, main level): "
              f"{[(b, round(d, 1), round(l, 1)) for b, d, l in off]}")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
