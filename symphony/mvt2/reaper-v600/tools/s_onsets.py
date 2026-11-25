"""mvt2 c51: audible note starts by critic A's S measure (tools/pcx.py s_start: the earlier of pcX and the robust
crossover on legato joins, pcX alone on entries and repeats), for every legato join of every track and for the
thematic lines (LINES below; critic A's c51 list). Use it for every lead fit and report; do not fit on a
dominant-pitch reading or on pcX alone (c51 lead notes; validation in cycles/c51/reports/A.md).

mvt2 c54: join rows carry "octave" / "pcx_valid" / "old_fall6" and "flat" (join_flags below); the report lists them.

usage: s_onsets.py RENDER_DIR PARTS.json OUT.json [--x0 S] [--tracks "A,B"]
  RENDER_DIR holds NN_<track>.wav on score time (a full render, or a range render with its pre-roll cut);
  --x0: time of the files' first sample on the map (0 for renders that start at score qn 0).
compare: s_onsets.py --report A.json [B.json]   (per line: min, max, median, outside 25 / 60 ms; Violins I against II)
"""
import sys, json, os, csv
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pcx
WORK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINES = [
    ("Horn 3", 6, 18, "intro C-Db-C, bars 3-6"), ("Horn 1", 17, 42, "theme A, bars 6-14"),
    ("Oboe 1", 42, 66, "answer, bars 15-22"), ("Violin I solo", 48, 66, "solo, bars 17-22"),
    ("Violins I", 65, 90, "theme A, bars 22-30"), ("Violins II", 65, 90, "theme A, bars 22-30"),
    ("Violoncellos", 63, 90, "counter-melody, bars 22-30"), ("Bass clarinet", 90, 108, "solo, bars 31-36"),
    ("Flute 1", 107, 124, "theme B, bars 36-40"), ("Cor anglais", 124, 140, "theme B, bars 41-44"),
    ("Flute 1", 124, 140, "theme B answer, bars 41-44"), ("Oboe 1", 139, 152, "B flat minor head, bars 45-47"),
    ("Violoncellos", 140, 152, "B flat minor head, bars 45-47"), ("Cor anglais", 150, 172, "quotation, bars 47-52"),
    ("Violins I", 172, 204, "theme B, bars 53-60"), ("Violins II", 172, 204, "theme B, bars 53-60"),
    ("Horn 1", 172, 204, "counter-melody, bars 53-60"), ("Violoncellos", 172, 204, "bars 53-60"),
    ("Violins I", 204, 220, "climax, bars 61-64"), ("Trombone 1", 212, 220, "quotation, bars 63-64"),
    ("Horn 1", 220, 238, "motto tail, bars 65-70"), ("Violins I", 237, 262, "theme A', bars 70-78"),
    ("Violins II", 237, 262, "theme A', bars 70-78"), ("Violoncellos", 238, 262, "counter-melody, bars 71-78"),
    ("Violins I", 262, 274, "cadence, bars 79-82"), ("Clarinet 1", 280, 292, "motto tail, bars 85-88")]
DOUBLED = [(65, 90), (172, 204), (237, 262)]   # Violins I and II on the same onsets
# mvt2 c53 (critic A #4): pieces of one held note (re-bow pieces, tremolo continuations) and same-pitch repeats that S
# cannot read are not line notes: {track: [score onsets]} (matched within 0.01 qn)
LINE_SKIP = {"Violins I": [205.949, 216.0, 264.417], "Violoncellos": [148.0]}


def slur_spans():
    sl = {}
    for r in csv.reader(open(WORK + "/build/mockup-events.tsv"), delimiter="\t"):
        if len(r) > 4 and r[3] == "slur":
            sl.setdefault(r[0], []).append((float(r[1]), int(r[4])))
    out = {}
    for st, v in sl.items():
        a = None
        for q, d in sorted(v):
            if d == -1:
                a = q
            elif a is not None:
                out.setdefault(st, []).append((a, q)); a = None
    return out


def join_flags(x, tmv, ts, te, pitch, prev, x0=0.0):
    """mvt2 c54 (critic A #3, #4): two cases in which pcX is not a reading of the new note.
    octave: the interval is a multiple of 12 semitones, so every harmonic of the higher pitch is a harmonic of the lower
    one and the band pcX reads holds the old note: pcx_valid False, S = the crossover, and old_fall6 = the time (s re the
    beat) at which the lower-pitch-only band (the old pitch's harmonics that the new one lacks, or the new pitch's for a
    falling octave) has changed by 6 dB against its mean over the 0.3 s before the note-on.
    flat: the new pitch's band changes by less than 6 dB over the 100 ms around pcX's half-amplitude crossing (t50), so
    the thresholds lie on a level stretch and small level changes move the reading (Violoncellos 77, c53): report the
    crossover beside pcX."""
    out = {}
    if prev is not None and pitch != prev and (pitch - prev) % 12 == 0:
        out.update(octave=True, pcx_valid=False)
        lo, hi = min(pitch, prev), max(pitch, prev)
        t, e, _ = pcx.band_env(x, tmv - 0.45, min(te, ts + 0.6), lo, hi, x0=x0)
        m = (t >= tmv - 0.4) & (t <= tmv - 0.1)
        if m.any():
            ref = e[m].mean(); k = np.where((t >= tmv - 0.1) & (np.abs(e - ref) >= 6))[0]
            out["old_fall6"] = float(t[k[0]] - ts) if len(k) else None
    a = pcx.attack_pcx(x, tmv, ts, te - tmv, pitch, prev, x0=x0) or {}
    if a.get("t50") is not None:
        t, e, _ = pcx.band_env(x, tmv - 0.25, ts + 0.6, pitch, prev, x0=x0)
        m = (t >= ts + a["t50"] - 0.05) & (t <= ts + a["t50"] + 0.05)
        if m.any() and e[m].max() - e[m].min() < 6:
            out["flat"] = True
    return out


def measure(render, parts, x0=0.0, tracks=None, q_hi=None):
    import soundfile as sf
    tm = pcx.TM(parts["tempo"]); T = {t["name"]: t for t in parts["tracks"]}
    SL = slur_spans()
    want = {l[0] for l in LINES} | {n for n, t in T.items() if pcx.legato_joins(t)}
    out = {"joins": {}, "lines": {}}
    cache = {}
    for name in [t["name"] for t in parts["tracks"]]:
        if name not in want or (tracks and name not in tracks):
            continue
        f = pcx.stem_path(render, parts, name)
        if not f:
            continue
        x, sr = sf.read(f, dtype="float32", always_2d=True)
        tend = x0 + len(x) / sr
        tr = T[name]; rows = []
        for p, n in pcx.legato_joins(tr):
            tmv, ts, te = tm.sec(n["qn"]), tm.sec(n["sq"]), tm.sec(n["qn"] + n["dur"])
            if ts + 0.7 > tend or tmv - 0.3 < x0 or (q_hi and n["sq"] > q_hi):
                continue
            s, pc, xr = pcx.s_start(x, tmv, ts, te, n["pitch"], p["pitch"], x0=x0)
            row = {"sq": n["sq"], "pitch": n["pitch"], "prev": p["pitch"], "lead": ts - tmv, "S": s, "pcx": pc, "xr": xr,
                   "prev_sq": p["sq"]}
            row.update(join_flags(x, tmv, ts, te, n["pitch"], p["pitch"], x0))
            if row.get("octave"):   # pcX reads the old note's even harmonics: S is the crossover alone
                row["S"] = xr
            rows.append(row)
        out["joins"][name] = rows
        jb = {round(r["sq"], 3): r for r in rows}
        sl = [s for st in tr["staves"] for s in SL.get(st, [])]
        for nm, lo, hi, label in LINES:
            if nm != name:
                continue
            by = {}
            for n in tr["notes"]:
                if lo <= n.get("sq", n["qn"]) < hi and not any(abs(n.get("sq", n["qn"]) - q_) < 0.01 for q_ in LINE_SKIP.get(nm, [])):
                    by.setdefault(round(n.get("sq", n["qn"]), 3), []).append(n)
            ns = [max(v, key=lambda n: n["pitch"]) for k, v in sorted(by.items())]
            lr = []
            for i, n in enumerate(ns):
                sq = n.get("sq", n["qn"]); ts, tmv, te = tm.sec(sq), tm.sec(n["qn"]), tm.sec(n["qn"] + n["dur"])
                if ts + 0.7 > tend or tmv - 0.3 < x0 or (q_hi and sq > q_hi):
                    continue
                r = {"sq": sq, "pitch": n["pitch"], "lead": ts - tmv,
                     "slur": next((k for k, (a, b) in enumerate(sl) if a - 0.01 <= sq <= b + 0.01), None)}
                j = jb.get(round(sq, 3))
                if j is not None and j["pitch"] == n["pitch"]:
                    r.update(kind="join", S=j["S"], pcx=j["pcx"], xr=j["xr"], prev=j["prev"])
                    r.update({k_: j[k_] for k_ in ("octave", "pcx_valid", "old_fall6", "flat") if k_ in j})
                else:
                    s, pc, _ = pcx.s_start(x, tmv, ts, te, n["pitch"], None, x0=x0)
                    r.update(kind="entry", S=s, pcx=pc, xr=None, prev=None)
                # heard length: filled by report() from the next note's S
                r["printed_s"] = (tm.sec(ns[i + 1].get("sq", ns[i + 1]["qn"])) - ts) if i + 1 < len(ns) else None
                lr.append(r)
            out["lines"][f"{nm} | {label}"] = lr
        print(name, len(rows), "joins", flush=True)
    return out


def stats(rows):
    v = np.array([r["S"] for r in rows if r.get("S") is not None]) * 1000
    d = [abs(b["S"] - a["S"]) * 1000 for a, b in zip(rows, rows[1:]) if a.get("S") is not None and b.get("S") is not None
         and a["slur"] is not None and a["slur"] == b["slur"]]
    if not len(v):
        return None
    return dict(n=len(rows), found=len(v), min=v.min(), max=v.max(), med=float(np.median(v)), o25=int((abs(v) > 25).sum()),
                o60=int((abs(v) > 60).sum()), pairs=len(d), p25=int(sum(x > 25 for x in d)), p60=int(sum(x > 60 for x in d)))


def doubled(J):
    out = []
    a = {}; b = {}
    for k, v in J["lines"].items():
        if k.startswith("Violins I |"):
            a.update({round(r["sq"], 3): r for r in v})
        if k.startswith("Violins II |"):
            b.update({round(r["sq"], 3): r for r in v})
    for lo, hi in DOUBLED:
        ks = [q for q in sorted(a) if lo <= q < hi and q in b and a[q].get("S") is not None and b[q].get("S") is not None]
        d = np.array([a[q]["S"] - b[q]["S"] for q in ks]) * 1000
        out.append((lo, hi, ks, d))
    return out


def report(files):
    Js = [json.load(open(f)) for f in files]
    fm = lambda s: "   --" if s is None else f"{s['min']:+5.0f} {s['max']:+5.0f} {s['med']:+4.0f} | {s['o25']:2d} {s['o60']:2d} of {s['found']:2d} | pairs {s['pairs']:2d}: {s['p25']:2d} >25 {s['p60']:2d} >60"
    print("line | per file: min max median (ms) | outside 25, 60 | slur neighbours")
    tot = [np.zeros(5) for _ in Js]
    for nm, lo, hi, label in LINES:
        k = f"{nm} | {label}"; cells = []
        for i, J in enumerate(Js):
            s = stats(J["lines"].get(k, []))
            if s:
                tot[i] += [s["o25"], s["o60"], s["found"], s["p25"], s["p60"]]
            cells.append(fm(s))
        print(f"{nm + ', ' + label:44s} " + "  ||  ".join(cells))
    for i, t in enumerate(tot):
        print(f"ALL LINES file {i + 1}: outside 25: {t[0]:.0f}, outside 60: {t[1]:.0f} of {t[2]:.0f}; slur neighbours over 25: {t[3]:.0f}, over 60: {t[4]:.0f}")
    for i, J in enumerate(Js):
        n = sum(len(v) for v in J["joins"].values()); s = np.array([r["S"] for v in J["joins"].values() for r in v if r["S"] is not None]) * 1000
        print(f"all legato joins file {i + 1}: {n} ({len(s)} found): within 25: {(abs(s) <= 25).sum()}, within 60: {(abs(s) <= 60).sum()}, median {np.median(s):+.0f} ms")
        fl = [(nm_, r) for nm_, v in J["joins"].items() for r in v if r.get("octave") or r.get("flat")]
        if fl:   # mvt2 c54: joins whose pcX is not a firm reading
            f3 = lambda v_: "--" if v_ is None else f"{v_ * 1000:+.0f}"
            print("  octave joins (S = crossover; old band changes 6 dB at): " + (", ".join(f"{nm_} {r['sq']:g} xr {f3(r['xr'])} / {f3(r.get('old_fall6'))} ms" for nm_, r in fl if r.get("octave")) or "none"))
            fx = [(nm_, r) for nm_, r in fl if r.get("flat") and not r.get("octave") and r["pcx"] is not None and r["xr"] is not None and abs(r["pcx"] - r["xr"]) > 0.025]
            print(f"  level band around t50 (pcX not firm): {sum(1 for _, r in fl if r.get('flat'))} joins; pcX and crossover over 25 ms apart at {len(fx)}: " + ", ".join(f"{nm_} {r['sq']:g} ({f3(r['pcx'])} / {f3(r['xr'])})" for nm_, r in fx[:30]))
        for lo, hi, ks, d in doubled(J):
            if len(d):
                print(f"  Violins I - II, qn {lo}-{hi}: {len(ks)} onsets, over 30 ms apart: {(abs(d) > 30).sum()}, over 60: {(abs(d) > 60).sum()}, max {abs(d).max():.0f} ms"
                      + (" at " + ", ".join(f"{q:g} ({x:+.0f})" for q, x in zip(ks, d) if abs(x) > 60) if (abs(d) > 60).any() else ""))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--report":
        report(a[1:])
    else:
        x0 = float(a[a.index("--x0") + 1]) if "--x0" in a else 0.0
        tr = a[a.index("--tracks") + 1].split(",") if "--tracks" in a else None
        qh = float(a[a.index("--qhi") + 1]) if "--qhi" in a else None
        J = measure(a[0], json.load(open(a[1])), x0=x0, tracks=tr, q_hi=qh)
        json.dump(J, open(a[2], "w"), default=float)
