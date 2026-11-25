"""Per-pitch level comparison of two renders (c49, critic B #6).

A change of mic mix, of a family EQ bell or of a patch moves the pitches of one track by different amounts (c44:
Bassoon 1 A flat 3 fell 10 dB against the rest of its line, and the family and solo checks did not see it). This check
compares each pitch of a track with the track's own median change between two renders.

Usage: pitch_check.py OLD_RENDER OLD_BUILD NEW_RENDER NEW_BUILD [--tracks "A,B"] [--db 2.5] [--min-qn 0.9] [--cc 1.5]
                      [--all] [--out FILE]
  OLD_BUILD / NEW_BUILD: the folder holding that render's parts.json (cycles/cNN/rendered_build).
  For every note of at least --min-qn quarter notes that exists in both builds with the same pitch and whose CC1 and CC11
  (at the middle of the note) agree within --cc: K-weighted level of the note body (20-80 % of the sounding note) in the
  new render minus the old one, minus the change of the track's vol_db there. Grouped by pitch; a pitch is reported
  when its median differs from the track's median change by --db or more (--all prints every pitch).
Run it after every render in which `mics`, a family EQ, a width or a patch changed, and correct a reported pitch in
build/pitch_trims.json (or note_trims.json for one note)."""
import sys, os, glob, json, bisect
import numpy as np, soundfile as sf

a = sys.argv[1:]


def opt(k, d=None, flag=False):
    if k in a:
        i = a.index(k)
        if flag:
            del a[i]; return True
        v = a[i + 1]; del a[i:i + 2]; return v
    return False if flag else d


TRACKS = opt("--tracks"); DB = float(opt("--db", 2.5)); MINQN = float(opt("--min-qn", 0.9)); CC = float(opt("--cc", 1.5))
ALL = opt("--all", flag=True); OUT = opt("--out")
OR_, OB, NR, NB = a[:4]
SR = 48000
NN = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


class TM:
    def __init__(s, tempo):
        s.pts = sorted((float(q), float(b)) for q, b in tempo); s.q = [x for x, _ in s.pts]; s.t = [0.0]
        for (q0, b0), (q1, _) in zip(s.pts, s.pts[1:]):
            s.t.append(s.t[-1] + (q1 - q0) * 60.0 / b0)

    def sec(s, q):
        i = max(0, bisect.bisect_right(s.q, q) - 1); return s.t[i] + (q - s.q[i]) * 60.0 / s.pts[i][1]


def val(pts, q):
    if not pts:
        return float("nan")
    qs = [p[0] for p in pts]; i = bisect.bisect_right(qs, q) - 1
    if i < 0:
        return pts[0][1]
    if i >= len(pts) - 1:
        return pts[-1][1]
    q0, v0, q1, v1 = pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]
    return v0 + (v1 - v0) * (q - q0) / (q1 - q0) if q1 > q0 else v1


def _bq(b, a_, f):
    z = np.exp(-2j * np.pi * f / SR); return (b[0] + b[1] * z + b[2] * z * z) / (a_[0] + a_[1] * z + a_[2] * z * z)


def body_k(x, t0, t1):
    """K-weighted mean-square level (dB) of x between t0 and t1 (BS.1770 response applied to one FFT of the segment)"""
    s = x[int(t0 * SR):int(t1 * SR)]
    if len(s) < 256:
        return float("nan")
    f = np.fft.rfftfreq(len(s), 1 / SR)
    kw = np.abs(_bq([1.53512485958697, -2.69169618940638, 1.19839281085285], [1, -1.69065929318241, 0.73248077421585], f)
                * _bq([1, -2, 1], [1, -1.99004745483398, 0.99007225036621], f)) ** 2
    p = sum((np.abs(np.fft.rfft(s[:, c].astype(np.float64))) ** 2 * kw).sum() for c in range(s.shape[1]))
    return 10 * np.log10(max(2 * p / len(s) ** 2, 1e-20))


def stem(rdir, name):
    f = [p for p in glob.glob(f"{rdir}/*.wav") if os.path.basename(p).split("_", 1)[-1][:-4] == name]
    if not f:
        return None
    x, sr = sf.read(f[0], always_2d=True, dtype="float32"); assert sr == SR
    return x


PA, PB = json.load(open(f"{OB}/parts.json")), json.load(open(f"{NB}/parts.json"))
ta, tb = TM(PA["tempo"]), TM(PB["tempo"])
TA = {t["name"]: t for t in PA["tracks"]}; TB = {t["name"]: t for t in PB["tracks"]}
names = [n.strip() for n in TRACKS.split(",")] if TRACKS else [t["name"] for t in PB["tracks"] if t["name"] in TA]
lines = [f"pitch check: {OR_} -> {NR}; notes of at least {MINQN} qn, CC1 / CC11 within {CC}; reported from {DB} dB"]
nflag = 0
for name in names:
    A, B = TA.get(name), TB.get(name)
    if A is None or B is None:
        continue
    xa, xb = stem(OR_, name), stem(NR, name)
    if xa is None or xb is None:
        continue
    nb = {round(n.get("sq", n["qn"]), 2): n for n in B["notes"]}
    rows = []
    for n in A["notes"]:
        m = nb.get(round(n.get("sq", n["qn"]), 2))
        if m is None or n["dur"] < MINQN or m["dur"] < MINQN or m["pitch"] != n["pitch"]:
            continue
        mid, mid2 = n["qn"] + 0.5 * n["dur"], m["qn"] + 0.5 * m["dur"]
        c = [abs(val(A.get(k) or [], mid) - val(B.get(k) or [], mid2)) for k in ("cc1", "cc11")]
        if any(x > CC for x in c if x == x):
            continue
        dv = val(B.get("vol_db") or [], mid2) - val(A.get("vol_db") or [], mid)
        dv = 0.0 if dv != dv else dv
        la = body_k(xa, ta.sec(n["qn"] + 0.2 * n["dur"]), ta.sec(n["qn"] + 0.8 * n["dur"]))
        lb = body_k(xb, tb.sec(m["qn"] + 0.2 * m["dur"]), tb.sec(m["qn"] + 0.8 * m["dur"]))
        if la != la or lb != lb or la < -90 or lb < -90:
            continue
        rows.append((n.get("sq", n["qn"]), n["pitch"], lb - la - dv))
    if not rows:
        continue
    med = float(np.median([r[2] for r in rows])); by = {}
    for sq, p, d in rows:
        by.setdefault(p, []).append((sq, d))
    out = []
    for p in sorted(by):
        ds = [d for _, d in by[p]]; dm = float(np.median(ds)) - med
        if ALL or abs(dm) >= DB:
            nflag += abs(dm) >= DB
            out.append(f"   {NN[p % 12]}{p // 12 - 1} ({p}): {dm:+.1f} dB re the track, n={len(ds)}, range {min(ds) - med:+.1f}..{max(ds) - med:+.1f},"
                       f" at qn {', '.join(f'{s:g}' for s, _ in by[p][:8])}" + (" <<" if abs(dm) >= DB else ""))
    if out or abs(med) >= 1.0:
        lines.append(f"{name}: {len(rows)} notes, median change {med:+.1f} dB")
        lines += out
lines.append(f"{nflag} pitch(es) differ from their track's median change by {DB} dB or more")
print("\n".join(lines))
if OUT:
    open(OUT, "w").write("\n".join(lines) + "\n")
