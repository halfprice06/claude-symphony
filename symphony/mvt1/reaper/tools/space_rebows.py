"""mvt1 c03 (critic A #2): space the automatic string re-bows across sections.

Usage: space_rebows.py PARTS_JSON [--write] [--sep S] [--min-piece S] [--max-piece S]

score_to_parts.py gives each string track its own re-bow phase and piece length (AUTO_REBOW), but it does not look at
the other tracks, so sections can still change bow together (the final ppp chord: five sections within 0.34 s at qn
726.4, master dips 2.5-5.2 dB). This reads every string track's re-bows from parts.json ([qn, note end, pitch, piece
start, automatic point before any move]) and, in time order, moves an automatic point that falls within SEP seconds
(default REBOW_MIN_SEP_S = 0.6) of an already placed point of another track to the nearest position (at most
MAX_MOVE = 1.5 s away) that is SEP from every placed point of the other tracks and keeps every piece of its note between
MIN_PIECE (1.5 s, the AUTO_REBOW limit) and MAX_PIECE (4.5 s). Listed points (REBOW_AT, no automatic point) never move. A point that fits neither way stays.

Writes build/rebow_moves.json {track: {"automatic point": new qn}} (read by score_to_parts.py) and, for every moved
point that has a fitted shape in build/rebow_fills.json under its old key and none under the new one, copies the shape
to the new key (the shape is relative to its re-bow in seconds; refit it on the next render). Run it on a parts.json
built without rebow_moves.json, or with the moves already applied: it always starts from the automatic points.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:]
PJ = args[0]
WRITE = "--write" in args
opt = lambda k, dflt: float(args[args.index(k) + 1]) if k in args else dflt
SEP, MIN_PIECE, MAX_PIECE = opt("--sep", 0.6), opt("--min-piece", 1.5), opt("--max-piece", 4.5)
MAX_MOVE = opt("--max-move", 1.5)   # seconds
D = json.load(open(PJ))
T = D["tempo"]


def q2s(q):
    t, lq, lb = 0.0, 0.0, T[0][1]
    for tq, b in T:
        if tq >= q:
            break
        t += (tq - lq) * 60 / lb; lq, lb = tq, b
    return t + (q - lq) * 60 / lb


def s2q(t):
    lo, hi = 0.0, D["end_qn"] + 8
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if q2s(mid) < t else (lo, mid)
    return (lo + hi) / 2


pts = []   # dicts: track, note key, auto (s or None), t (s), piece start (s), note end (s)
for tr in D["tracks"]:
    for r in tr.get("rebows") or []:
        if len(r) < 5:
            sys.exit("parts.json re-bows have no piece start / automatic point: rebuild it with the c03 score_to_parts.py")
        p, e, pitch, q0, pa = r
        auto = pa if pa is not None else None
        pts.append({"track": tr["name"], "note": (tr["name"], round(e, 3), pitch), "auto_q": auto,
                    "t": q2s(auto if auto is not None else p), "e": q2s(e)})
# pieces: within one note the points in time order; the first piece starts at the note start (score_to_parts records
# the piece start of each point, which for the first point is the note start)
by_note = {}
for tr in D["tracks"]:
    for r in tr.get("rebows") or []:
        by_note.setdefault((tr["name"], round(r[1], 3), r[2]), []).append(r)
note_start = {k: q2s(min(v, key=lambda r: r[0])[3]) for k, v in by_note.items()}
pts.sort(key=lambda x: x["t"])
for x in pts:
    x["t0"] = x["t"]


def bounds(x):
    same = sorted([y for y in pts if y["note"] == x["note"]], key=lambda y: y["t"])
    k = next(j for j, y in enumerate(same) if y is x)
    return (same[k - 1]["t"] if k > 0 else note_start[x["note"]]), (same[k + 1]["t"] if k + 1 < len(same) else x["e"])


def clashes(x, t):
    return [y for y in pts if y is not x and y["track"] != x["track"] and abs(y["t"] - t) < SEP - 1e-6]


# local search: each automatic point that clashes moves to the nearest valid position (on a 0.05 s grid at most MAX_MOVE
# from its automatic time, SEP from every point of the other tracks as they stand, pieces within MIN_PIECE..MAX_PIECE);
# repeated until nothing changes. Run from several processing orders (fixed seed); the result with the fewest clashing
# pairs, then the smallest total move, is kept.
import random


def n_clash():
    ts_ = sorted((x["t"], x["track"]) for x in pts)
    return sum(1 for i_, a_ in enumerate(ts_) for b_ in ts_[i_ + 1:] if b_[0] - a_[0] < SEP - 1e-6 and a_[1] != b_[1])


GRID = [k * 0.05 for k in range(-int(MAX_MOVE / 0.05), int(MAX_MOVE / 0.05) + 1)]
rng = random.Random(1)
best = None
for run in range(40):
    for x in pts:
        x["t"] = x["t0"]
    order = list(pts)
    if run:
        rng.shuffle(order)
    for _ in range(20):
        changed = False
        for x in order:
            if x["auto_q"] is None or not clashes(x, x["t"]):
                continue
            lo, hi = bounds(x)
            ok = lambda c: c - lo >= MIN_PIECE and hi - c >= MIN_PIECE and c - lo <= MAX_PIECE and hi - c <= MAX_PIECE
            cands = sorted((x["t0"] + g for g in GRID), key=lambda c: abs(c - x["t0"]))
            new = next((c for c in cands if ok(c) and not clashes(x, c)), None)
            if new is not None and abs(new - x["t"]) > 1e-6:
                x["t"] = new
                changed = True
        if not changed:
            break
    score = (n_clash(), sum(abs(x["t"] - x["t0"]) for x in pts))
    if best is None or score < best[0]:
        best = (score, [x["t"] for x in pts])
for x, t in zip(pts, best[1]):
    x["t"] = t
print(f"best of 40 orders: {best[0][0]} clashing pairs, total move {best[0][1]:.2f} s")
moves, report = {}, []
for x in pts:
    if x["auto_q"] is None:
        continue
    if abs(x["t"] - x["t0"]) > 1e-6:
        moves.setdefault(x["track"], {})[f"{x['auto_q']:.3f}"] = round(s2q(x["t"]), 3)
        report.append((x["track"], x["auto_q"], round(s2q(x["t"]), 3), round(x["t"] - x["t0"], 3)))
    elif clashes(x, x["t"]):
        report.append((x["track"], x["auto_q"], None, 0.0))
for r in report:
    print(f"{r[0]:15s} {r[1]:8.3f} -> {r[2] if r[2] is not None else 'kept (no room)'}  ({r[3]:+.3f} s)")
ts = sorted((x["t"], x["track"]) for x in pts)
close = [(round(b[0] - a[0], 3), a[1], b[1], round(s2q(a[0]), 3)) for a, b in zip(ts, ts[1:]) if a[1] != b[1] and b[0] - a[0] < SEP - 1e-6]
print(f"{len(moves and [1 for r in report if r[2] is not None])} moved, {len(close)} pairs of sections still closer than {SEP} s:", close[:12])
if WRITE:
    json.dump({"_doc": f"tools/space_rebows.py on {os.path.basename(PJ)}: automatic re-bow point -> moved point (sep {SEP} s)", **moves},
              open(f"{ROOT}/build/rebow_moves.json", "w"), indent=0)
    rf_path = f"{ROOT}/build/rebow_fills.json"
    RF = json.load(open(rf_path))
    # a fitted shape whose automatic point moved a little with its note (a changed lead moves the note start, and the
    # points are placed in seconds from it) follows it: an orphan key goes to the nearest automatic point of the same
    # track within 0.25 qn that has no shape
    rekeyed = 0
    for tr in D["tracks"]:
        fills = RF.get(tr["name"], {})
        autos = sorted({round(r[4] if r[4] is not None else r[0], 3) for r in tr.get("rebows") or []})
        keys = {round(float(k), 3): k for k in fills if not k.startswith("_")}
        for kq, k in sorted(keys.items()):
            if any(abs(kq - a_) < 0.002 for a_ in autos):
                continue
            free = [a_ for a_ in autos if abs(a_ - kq) < 0.25 and not any(abs(a_ - k2) < 0.002 for k2 in keys)]
            if free:
                a_ = min(free, key=lambda a_: abs(a_ - kq))
                fills[f"{a_:.3f}"] = fills.pop(k)
                keys = {round(float(k2), 3): k2 for k2 in fills if not k2.startswith("_")}
                rekeyed += 1
    print("re-keyed", rekeyed, "shapes to their notes' new automatic points")
    copied = 0
    for tn, mv in moves.items():
        fills = RF.get(tn, {})
        keys = {round(float(k), 3): k for k in fills if not k.startswith("_")}
        for old, new in mv.items():
            ko = keys.get(round(float(old), 3))
            kn = f"{new:.4f}".rstrip("0").rstrip(".")
            if ko is not None and round(new, 3) not in keys:
                fills[kn] = fills.pop(ko)
                copied += 1
    json.dump(RF, open(rf_path, "w"), indent=0)
    print("wrote build/rebow_moves.json; moved", copied, "fitted shapes to their new points")
