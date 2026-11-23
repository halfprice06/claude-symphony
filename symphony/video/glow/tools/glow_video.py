"""Glowing-score video: the engraved score as one long line on a dark sheet, seen at an angle by a moving camera;
each note lights up in its part's colour while it sounds (after the look of Gilmar Araújo's animated scores).

python3 glow_video.py --strip BUILD --tempo data/<mvt>-tempo.json --audio mockup.mp3 [--stems data/<mvt>-stems.npz]
                      --out out.mp4 [--bars 53 64] [--still T ...] [--jobs 4]

--tempo: {"tempo": [[qn, bpm], ...], "head_s": s}; the tempo map REAPER played; head_s is the audio before score qn 0.
--stems: 20 Hz loudness of each mockup stem; the camera looks at the staves that are loudest (without it, at the
         staves with the most onsets).
--jobs N renders N parts of the video in parallel processes and joins them; the frames are the same as one process makes.
"""
import argparse, bisect, json, math, re, subprocess, sys, os, tempfile
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

ap = argparse.ArgumentParser()
ap.add_argument("--strip", required=True)
ap.add_argument("--tempo", required=True)
ap.add_argument("--audio")
ap.add_argument("--stems")
ap.add_argument("--out", required=True)
ap.add_argument("--bars", type=int, nargs=2)
ap.add_argument("--fps", type=int, default=60)
ap.add_argument("--still", type=float, nargs="*")
ap.add_argument("--env", help="audio file for the loudness envelope (default: --audio)")
ap.add_argument("--jobs", type=int, default=1)
ap.add_argument("--part", type=int, nargs=2, help=argparse.SUPPRESS)      # first and last frame (internal, --jobs)
ap.add_argument("--focus-report", action="store_true", help="print the staff the camera follows, bar by bar, and stop")
ap.add_argument("--focus-report-full", action="store_true", help="with --focus-report: also the staff layout and the note onsets per staff in each bar")
ap.add_argument("--split", default="none", choices=["none", "stack", "slant", "inset", "pullback"],
                help="when two far-apart groups both lead: split the screen in two bands, along the slant of the score, "
                     "show the second group in an inset window, or pull the camera back to show both")
ap.add_argument("--split-report", action="store_true", help="print the stretches that would get a split screen, and stop")
ap.add_argument("--split-bars", type=int, nargs="*", help="split only in these bar ranges (pairs A B), groups found from the stems")
ap.add_argument("--split-staves", nargs=2, help="with --split-bars: the staves the upper and lower views centre on")
ap.add_argument("--annotations", help="JSON with \"splits\" (each with its own mode stack|pullback and panel zooms) and \"captions\" for the whole movement (annotations/<mvt>.json)")
ap.add_argument("--annotations-check", action="store_true", help="check the --annotations file against the score and the rules in annotations/BRIEF.md, print every item with its times, and stop")
ap.add_argument("--captions", help="analysis captions (JSON, see overlays.load_captions)")
ap.add_argument("--caption-style", default="score", choices=["bar", "score", "card"],
                help="a subtitle band, notes written on the score next to the notes they describe, or a card with music examples")
ap.add_argument("--labels", default="none", choices=["none", "letters", "icons", "names"],
                help="say which instrument plays: abbreviations riding on the jumping lights, the lights drawn as "
                     "instrument icons, or the instrument's name glowing on the paper beside its line")
A = ap.parse_args()
W, H = 1920, 1080
CHILD = A.part is not None
if CHILD: cv2.setNumThreads(1)     # the parts already fill the cores
def log(*a):
    if not CHILD: print(*a, file=sys.stderr, flush=True)

# ---------- time ----------
TJ = json.load(open(A.tempo))
HEAD = float(TJ.get("head_s", 0.0))          # audio seconds before score qn 0
steps = [tuple(x) for x in TJ["tempo"]]
def q2s(q):
    t, lq, lb = 0.0, 0.0, steps[0][1]
    for tq, b in steps[1:]:
        if tq >= q: break
        t += (tq - lq) * 60 / lb; lq, lb = tq, b
    return t + (q - lq) * 60 / lb

svg = open(f"{A.strip}/strip.svg").read()
bl = sorted({float(x) for x in re.findall(r'<g class="bl" data-m="([-\d.]+)"', svg)} - {0.0})
bar_qn = np.array([0.0] + [b for b in bl if b > 0])      # bar k starts at bar_qn[k-1]; the last entry is the end
END_QN = float(bar_qn[-1])
gq = np.linspace(0, END_QN + 4, 40000); gt = np.array([q2s(q) for q in gq])
def s2q(t): return float(np.interp(t, gt, gq))

# loudness envelope of the recording: the lights swell with the orchestra
ENV_SR = 200
_ea = A.env or A.audio
if _ea:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", _ea, "-ac", "1", "-ar", "8000", "-f", "f32le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32)
    rms = np.sqrt(np.convolve(a[: len(a) // 40 * 40].reshape(-1, 40).astype(np.float64) ** 2 @ np.ones(40) / 40, np.ones(30) / 30, "same"))
    db = 20 * np.log10(rms + 1e-5)
    lo_, hi_ = np.percentile(db, 5), np.percentile(db, 99.5)
    ENV = np.clip((db - lo_) / (hi_ - lo_), 0, 1)
else:
    ENV = None
def loud(t):
    t = t + HEAD                   # score seconds -> file seconds
    if ENV is None or t < 0: return 0.5
    return float(ENV[min(int(t * ENV_SR), len(ENV) - 1)])

# ---------- layout from the SVG ----------
vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
PNG_W = Image.open(f"{A.strip}/strip2.png").size[0]
k = PNG_W / vb[2]
tr = re.compile(r'translate\(([-\d.]+), ([-\d.]+)\)')
staves, notes = {}, []
for m in re.finditer(r'<g class="(\w+)"((?: data-[\w-]+="[^"]*")*)>', svg):
    cls, attr = m.group(1), dict(re.findall(r'data-([\w-]+)="([^"]*)"', m.group(2)))
    if cls not in ("st", "nh"): continue
    end = svg.find("</g>\n</g>", m.end())        # the group's own end (a one-line staff must not run into the next grobs)
    body = svg[m.end():end if end > 0 else m.end() + 4000]
    pts = [(float(x), float(y)) for x, y in tr.findall(body)]
    if not pts: continue
    if cls == "st":
        ys = sorted(y for _, y in pts[:5])
        staves[attr["name"]] = (ys[0] * k, ys[-1] * k)
    else:
        notes.append((float(attr["m"]), float(attr.get("d", 0)), pts[0][0] * k, pts[0][1] * k, attr.get("t") == "1"))
names = sorted(staves, key=lambda n: staves[n][0])
BLX = {}
for m in re.finditer(r'<g class="bl" data-m="([-\d.]+)">', svg):
    pts = tr.findall(svg[m.end():m.end() + 600])
    if pts: BLX[float(m.group(1))] = min(BLX.get(float(m.group(1)), 1e12), float(pts[0][0]) * k)
five = [n for n in names if staves[n][1] - staves[n][0] > 1]
sp = (staves[five[0]][1] - staves[five[0]][0]) / 4          # staff space in px
def staff_of(y):
    return min(names, key=lambda n: max(staves[n][0] - y, y - staves[n][1], 0))
COL = {  # per part, LED-like colours (RGB)
    "Flutes 1·2": (120, 200, 255), "Oboes 1·2": (190, 255, 120), "Cor anglais": (230, 255, 140),
    "Clarinets 1·2": (255, 130, 220), "Bass clarinet": (220, 110, 255), "Bassoons 1·2": (255, 170, 80),
    "Contrabassoon": (255, 140, 60), "Horns 1·2": (255, 210, 120), "Horns 3·4": (255, 190, 100),
    "Trumpets 1·2": (255, 240, 90), "Trumpet 3": (255, 225, 70),
    "Trombones 1·2": (255, 80, 70), "Bass trombone": (255, 70, 90), "Tuba": (240, 90, 60),
    "Timpani": (255, 255, 255), "Percussion": (215, 225, 255), "Harp RH": (110, 255, 230), "Harp LH": (90, 230, 255),
    "Violins I": (255, 240, 215), "Violins II": (255, 205, 160), "Violas": (200, 170, 255),
    "Violoncellos": (255, 160, 190), "Double basses": (255, 130, 130)}
def sat(c, k=1.5):
    c = np.array(c, np.float32); g = c.mean()
    return np.clip(g + (c - g) * k, 0, 255)
COL = {n: sat(c) for n, c in COL.items()}
N = []
for q, d, x, y, tied in notes:
    st = staff_of(y)
    t0, t1 = q2s(q), q2s(q + max(d, 0.25))
    N.append((t0, t1, x + 0.65 * sp, y, np.array(COL.get(st, (255, 255, 255)), np.float32), st, tied))
N.sort(key=lambda n: n[0])
NTIE = np.array([n[6] for n in N], bool)     # a tie arrives at this head: the same note continued, not a new attack
N = [n[:6] for n in N]
# bouncing lights: per part, up to 3 balls hop from each onset's notes to the next onset's notes
from collections import defaultdict
_G = defaultdict(dict)
for (t0, t1, x, y, c, st), tie_ in zip(N, NTIE): _G[st].setdefault(round(t0, 4), []).append((x, y, t1, tie_))
TRACKS = []
for st, dct in _G.items():
    ts = sorted(dct); groups = [sorted(dct[t], key=lambda p: p[1]) for t in ts]
    slide = [all(p[3] for p in g) for g in groups]   # every head tied over: the light slides along the paper, no jump
    nb = min(max(len(g) for g in groups), 3)
    TRACKS.append((np.array(ts), groups, np.array(COL.get(st, (255, 255, 255)), np.float32), nb, st, slide))
DROP = 0.55
def balls_at(t):
    """(x, y, z, alpha, colour, staff, voice) of every ball at time t"""
    out = []
    for ts, groups, col, nb, st, slide in TRACKS:
        n0 = len(out)
        i = int(np.searchsorted(ts, t, side="right")) - 1
        for j in range(nb):
            if i < 0:
                if ts[0] - t < DROP:
                    q = groups[0][min(j, len(groups[0]) - 1)]; s_ = (ts[0] - t) / DROP
                    out.append((q[0], q[1], 260 * s_ * s_, 1 - s_, col, st, j))
                continue
            g = groups[i]; p_ = g[min(j, len(g) - 1)]; end = max(n[2] for n in g)
            if i + 1 < len(ts):
                nt = ts[i + 1]; q = groups[i + 1][min(j, len(groups[i + 1]) - 1)]
                gap = nt - ts[i]
                resting = (nt - end) > 0.9          # a real rest: the light goes out, then drops onto the next note
                if not resting:
                    hop = min(gap, 0.45 if slide[i + 1] else 0.75); st_ = nt - hop
                    if t >= st_:
                        s_ = (t - st_) / hop
                        if slide[i + 1]:   # a tie: glide along the paper to the continued note
                            s_ = s_ * s_ * (3 - 2 * s_)
                            out.append((p_[0] + (q[0] - p_[0]) * s_, p_[1] + (q[1] - p_[1]) * s_, 0.0, 1.0, col))
                        else:
                            dist = math.hypot(q[0] - p_[0], q[1] - p_[1])
                            hh = float(np.clip(0.35 * dist + 30, 30, 200))
                            out.append((p_[0] + (q[0] - p_[0]) * s_, p_[1] + (q[1] - p_[1]) * s_, hh * 4 * s_ * (1 - s_), 1.0, col))
                    else:
                        out.append((p_[0], p_[1], 0.0, 1.0, col))   # stays fully lit until it jumps
                else:
                    if t <= end + 0.25:
                        out.append((p_[0], p_[1], 0.0, 1.0, col))
                    elif t < end + 0.65:
                        s_ = (t - end - 0.25) / 0.4
                        out.append((p_[0], p_[1], 120 * s_ * s_, 1 - s_, col))      # lifts off and fades
                    elif nt - t < DROP:
                        s_ = (nt - t) / DROP
                        out.append((q[0], q[1], 260 * s_ * s_, 1 - s_, col))
            else:
                if t <= end + 0.3: out.append((p_[0], p_[1], 0.0, float(np.clip((end + 0.3 - t) / 0.3, 0, 1)) if t > end else 1.0, col))
            if len(out) > n0 and len(out[-1]) == 5: out[-1] = out[-1] + (st, j)
    return out
NT0 = np.array([n[0] for n in N]); NT1 = np.array([n[1] for n in N])
NX = np.array([n[2] for n in N]); NY = np.array([n[3] for n in N])
NC = np.array([n[4] for n in N])
# playhead x per qn (leftmost head at each onset)
on = {}
for q, d, x, y, _ in notes: on[q] = min(on.get(q, 1e9), x)
oq = np.array(sorted(on)); ox = np.array([on[q] for q in oq])
ox = np.maximum.accumulate(ox)
def play_x(q): return float(np.interp(q, oq, ox))

# ---------- flat sheet (built once, shared by the parts through a memory-mapped file) ----------
top = int(min(v[0] for v in staves.values()) - 14 * sp); bot = int(max(v[1] for v in staves.values()) + 10 * sp)
top = max(top, 0)
NY = NY - top
FLAT = f"{A.strip}/flat-{top}-{bot}.npy"
PAPER = np.array([98, 101, 112], np.float32); INK = np.array([18, 19, 24], np.float32)
if not os.path.exists(FLAT):
    log("building the sheet", FLAT)
    ink_all = Image.open(f"{A.strip}/strip2.png").convert("L")
    ink = np.asarray(ink_all)[top:bot]
    FH, FW = ink.shape
    # paper texture: a slow brightness variation so the sheet reads as a surface
    rng = np.random.default_rng(3)
    tex = cv2.resize(rng.normal(0, 1, (FH // 64 + 2, FW // 64 + 2)).astype(np.float32), (FW, FH), interpolation=cv2.INTER_CUBIC)
    flat = np.lib.format.open_memmap(FLAT + ".tmp.npy", mode="w+", dtype=np.uint8, shape=(FH, FW, 3))
    for c0 in range(0, FW, 4096):
        i_ = ink[:, c0:c0 + 4096, None].astype(np.float32) / 255.0      # 1 = paper, 0 = ink
        paper = PAPER[None, None, :] * (1 + 0.035 * tex[:, c0:c0 + 4096, None])
        flat[:, c0:c0 + 4096] = (paper * i_ + INK * (1 - i_)).clip(0, 255).astype(np.uint8)
    flat.flush(); del flat, tex, ink, ink_all
    os.replace(FLAT + ".tmp.npy", FLAT)
flat = np.load(FLAT, mmap_mode="r")
FH, FW = flat.shape[:2]

stave_mid = {n: (staves[n][0] + staves[n][1]) / 2 - top for n in names}
V_ALL = (stave_mid[names[0]] + stave_mid[names[-1]]) / 2

# ---------- where the camera looks up and down the score ----------
# The loudest staves (from the mockup's stems) a moment ahead: a loudness-weighted density over the height of the
# score, and its highest peak. Only staves with notes in the window count, so a reverb tail does not hold the camera
# on bars of rest. A new peak takes over only when it is clearly stronger (x1.5) than the one being followed and the
# camera has stayed DWELL seconds, or at once (after 1 s) when the group being followed has nearly stopped. Without
# the dwell, winds and strings answering each other every bar or two kept the camera between them, on empty staves.
def stem_staves(nm):
    """the strip staves a mockup stem plays on"""
    pre = [("Bass clarinet", ["Bass clarinet"]), ("Contrabassoon", ["Contrabassoon"]), ("Bass trombone", ["Bass trombone"]),
           ("Flute", ["Flutes 1·2"]), ("Oboe", ["Oboes 1·2"]), ("Cor anglais", ["Cor anglais"]), ("Clarinet", ["Clarinets 1·2"]),
           ("Bassoon", ["Bassoons 1·2"]), ("Horn 3", ["Horns 3·4"]), ("Horn 4", ["Horns 3·4"]), ("Horn", ["Horns 1·2"]),
           ("Trumpet 3", ["Trumpet 3"] if "Trumpet 3" in staves else ["Trumpets 1·2"]), ("Trumpet", ["Trumpets 1·2"]),
           ("Trombone", ["Trombones 1·2"]), ("Tuba", ["Tuba"]), ("Timpani", ["Timpani"]),
           ("Tam-tam", ["Percussion"]), ("Suspended cymbal", ["Percussion"]), ("Crash cymbals", ["Percussion"]), ("Bass drum", ["Percussion"]),
           ("Harp", ["Harp RH", "Harp LH"]), ("Violins II", ["Violins II"]), ("Violin", ["Violins I"]), ("Viola", ["Violas"]),
           ("Violoncello", ["Violoncellos"]), ("Cello", ["Violoncellos"]), ("Double bass", ["Double basses"])]
    for p, sts in pre:
        if nm.startswith(p): return [s for s in sts if s in stave_mid]
    return []
FOCUS_SR = 10
# amplitude weights: a solo wind line stands out at a lower level than a string section; rolls and cymbals rarely
# carry the line
FAMILY_GAIN = {**{s: 1.6 for s in ("Flutes 1·2", "Oboes 1·2", "Cor anglais", "Clarinets 1·2", "Bass clarinet", "Bassoons 1·2", "Contrabassoon")},
               **{s: 0.8 for s in ("Violins I", "Violins II", "Violas", "Violoncellos", "Double basses")},
               "Timpani": 0.6, "Percussion": 0.6}
DWELL = 6.0      # seconds the camera stays with a group of staves before it may switch to a stronger one
def focus_track():
    n = int((q2s(END_QN) + 12) * FOCUS_SR)
    tt = np.arange(n) / FOCUS_SR
    sids = {s: i for i, s in enumerate(names)}
    Wt = np.zeros((len(names), n))                    # weight per staff over time
    if A.stems:
        z = np.load(A.stems)
        fr = float(z["frame"]); dbm = z["db"].astype(np.float32)
        en = 10 ** (dbm / 10)                          # energy per 50 ms frame
        # mean energy over [t - 0.25, t + 1.75] s: the camera looks a little ahead
        w0, w1 = int(round(0.25 / fr)), int(round(1.75 / fr))
        cs = np.concatenate([np.zeros((len(en), 1)), np.cumsum(en, 1)], 1)
        idx = np.clip(np.round(tt / fr).astype(int), 0, en.shape[1] - 1)
        lo = np.clip(idx - w0, 0, en.shape[1]); hi = np.clip(idx + w1, 1, en.shape[1])
        mean = (cs[:, hi] - cs[:, lo]) / np.maximum(hi - lo, 1)
        for i, nm in enumerate(z["names"]):
            sts = stem_staves(str(nm))
            for s in sts: Wt[sids[s]] += mean[i] * FAMILY_GAIN.get(s, 1.0) ** 2 / len(sts)
        Wt = np.sqrt(Wt)                                # amplitude
        has = np.zeros(Wt.shape, bool)                  # only staves with notes in the window count
        for t0, t1, x, y, c, st in N:
            a_, b_ = int(math.floor((t0 - 1.75) * FOCUS_SR)), int(math.ceil((t1 + 0.25) * FOCUS_SR))
            if b_ > 0: has[sids[st], max(a_, 0):min(b_, n)] = True
        Wt *= has
    else:
        for t0, t1, x, y, c, st in N:
            a_, b_ = int((t0 - 1.75) * FOCUS_SR), int((t0 + 0.25) * FOCUS_SR)
            Wt[sids[st], max(a_, 0):max(b_, 0)] += 1
        Wt = np.minimum(Wt, 4)
    vs = np.arange(0, FH, 10.0)
    K = np.exp(-0.5 * ((vs[:, None] - np.array([stave_mid[s] for s in names])[None, :]) / 250.0) ** 2)
    D = K @ Wt                                          # density over the height, per time step
    out = np.empty(n); cur = None; since = 0
    for i in range(n):
        d = D[:, i]
        if d.max() <= 1e-9:
            out[i] = vs[cur] if cur is not None else V_ALL; continue
        best = int(d.argmax())
        if cur is None: cur = best; since = i
        else:
            # follow the peak being watched as it drifts; switch only to a clearly stronger one, and not too often
            lo_, hi_ = max(cur - 30, 0), min(cur + 31, len(vs))
            cur = lo_ + int(d[lo_:hi_].argmax())
            held = (i - since) / FOCUS_SR
            if (d[best] > 1.5 * d[cur] and held >= DWELL) or (d[cur] < 0.25 * d[best] and held >= 1.0): cur = best; since = i
        out[i] = vs[cur]
    FT.update(D=D, vs=vs, Wt=Wt, n=n)
    return out
FT = {}
FOCUS = focus_track()
def feat_v(t):
    return float(FOCUS[int(np.clip(t * FOCUS_SR, 0, len(FOCUS) - 1))])
def bar_at(t): return int(np.searchsorted(bar_qn, s2q(t), side="right"))

# ---------- split screen: two groups of staves far apart that both lead ----------
SEP = 900.0        # px of score height: farther apart than one view shows well
def split_track():
    """[(t0, t1, v_upper, v_lower, why)]: stretches where two groups of staves at least SEP apart both matter, either
    because the loudness density has a second peak there at least 0.6 of the first, or because a staff near the top and
    one near the bottom play the same rhythm (a doubling across the score)"""
    D, vs, Wt, n = FT["D"], FT["vs"], FT["Wt"], FT["n"]
    up = np.full(n, np.nan); lo = np.full(n, np.nan); why = np.zeros(n, int)
    # local maxima of the density over the height
    for i in range(n):
        d = D[:, i]
        if d.max() <= 1e-9: continue
        pk = [k for k in range(len(d)) if d[k] > 0.05 * d.max() and d[k] >= d[max(k - 8, 0):k + 9].max()]
        if len(pk) < 2: continue
        p1 = max(pk, key=lambda k: d[k])
        far = [k for k in pk if abs(vs[k] - vs[p1]) >= SEP]
        if not far: continue
        p2 = max(far, key=lambda k: d[k])
        if d[p2] >= 0.6 * d[p1]:
            up[i], lo[i] = sorted((vs[p1], vs[p2])); why[i] = 1
    # rhythmic doubling between far staves (each staff's onsets in [t - 1, t + 2])
    ons = {s_: np.unique(np.round([nn[0] for nn in N if nn[5] == s_], 3)) for s_ in names}
    act = Wt > 0
    for i in range(0, n, 5):
        t = i / FOCUS_SR
        win = {s_: o[(o >= t - 1) & (o < t + 2)] for s_, o in ons.items()}
        best = None
        for a_ in names:
            if len(win[a_]) < 4: continue
            for b_ in names:
                if stave_mid[b_] - stave_mid[a_] < SEP or len(win[b_]) < 4: continue
                oa, ob = win[a_], win[b_]
                j = np.searchsorted(ob, oa).clip(1, len(ob) - 1)
                hit = (np.minimum(np.abs(ob[j] - oa), np.abs(ob[j - 1] - oa)) < 0.04).sum()
                sim = hit / max(len(oa), len(ob))
                if sim >= 0.8 and (best is None or sim > best[0]): best = (sim, a_, b_)
        if best and np.isnan(up[i]):
            for k in range(i, min(i + 5, n)):
                up[k], lo[k] = stave_mid[best[1]], stave_mid[best[2]]; why[k] = 2
    c = ~np.isnan(up)
    # close gaps up to 1.5 s, keep stretches of 4 s or more
    runs, i = [], 0
    while i < n:
        if not c[i]: i += 1; continue
        j = i
        while j < n and (c[j] or (j + 15 < n and c[j:j + 15].any())): j += 1
        if (j - i) / FOCUS_SR >= 4.0:
            seg = slice(i, j); ok = c[seg]
            runs.append([i / FOCUS_SR, j / FOCUS_SR, float(np.median(up[seg][ok])), float(np.median(lo[seg][ok])),
                         "loud" if (why[seg] == 1).sum() >= (why[seg] == 2).sum() else "doubling"])
        i = j
    return runs
def split_at_bars(pairs):
    """split stretches for the given bars: the two groups are the density's two strongest peaks at least SEP apart"""
    D, vs = FT["D"], FT["vs"]; out = []
    for a_, b_ in zip(pairs[::2], pairs[1::2]):
        t0, t1 = q2s(bar_qn[a_ - 1]), q2s(bar_qn[b_])
        ups, los = [], []
        for i in range(int(t0 * FOCUS_SR), int(t1 * FOCUS_SR)):
            d = D[:, i]
            if d.max() <= 1e-9: continue
            p1 = int(d.argmax()); far = np.abs(vs - vs[p1]) >= SEP
            if not far.any(): continue
            p2 = int(np.argmax(np.where(far, d, -1)))
            u_, l_ = sorted((vs[p1], vs[p2])); ups.append(u_); los.append(l_)
        if A.split_staves: out.append([t0, t1, stave_mid[A.split_staves[0]], stave_mid[A.split_staves[1]], "staves"])
        elif ups: out.append([t0, t1, float(np.median(ups)), float(np.median(los)), "bars"])
    return out
def pos_to_s(p):
    """score position "bar.q" (q = 1 + quarter notes after the bar line) to seconds"""
    b, _, qq = str(p).partition(".")
    return q2s(bar_qn[int(b) - 1] + (float(qq) - 1 if qq else 0))
ANN = json.load(open(A.annotations)) if A.annotations else None
if ANN is not None:
    _bad = sorted({x[k_] for x in ANN.get("splits", []) for k_ in ("upper", "lower")} | {c["anchor"]["staff"] for c in ANN.get("captions", []) if c.get("anchor")} | {c["chord_staff"] for c in ANN.get("captions", []) if c.get("chord_staff")} - set(names))
    _bad = [b_ for b_ in _bad if b_ not in names]
    if _bad: sys.exit(f"{A.annotations}: unknown staff names {_bad}; valid: {names}")
    SPLITS = [dict(t0=pos_to_s(x["from"]), t1=pos_to_s(x["to"]), va=stave_mid[x["upper"]], vb=stave_mid[x["lower"]],
                   mode=x.get("mode", "stack"), za=float(x.get("upper_zoom", 1.0)), zb=float(x.get("lower_zoom", 1.0)),
                   why=x.get("bars", ""), what=x.get("what", "")) for x in ANN.get("splits", [])]
    for sp_ in SPLITS: sp_.update(za0=sp_["za"], zb0=sp_["zb"])
else:
    _sp = split_at_bars(A.split_bars) if A.split_bars else (split_track() if (A.split != "none" or A.split_report) else [])
    SPLITS = [dict(t0=a_, t1=b_, va=c_, vb=d_, mode=A.split, za=1.0, zb=1.0, why=w_) for a_, b_, c_, d_, w_ in _sp]
SPLIT_IN = 1.1     # s: the screen opens into two views (and closes again) over this time
def split_amount(t):
    """(0..1 eased, the split) of the split screen at time t; the split is a dict with t0, t1, va (upper target),
    vb (lower target), mode (stack, slant, inset, pullback), za and zb (how far each panel pulls back)"""
    for sp_ in SPLITS:
        t0, t1 = sp_["t0"], sp_["t1"]
        if t0 - SPLIT_IN <= t <= t1 + SPLIT_IN:
            x = float(np.clip(min((t - (t0 - SPLIT_IN)) / SPLIT_IN, (t1 + SPLIT_IN - t) / SPLIT_IN), 0, 1))
            return x * x * (3 - 2 * x), sp_
    return 0.0, None
if A.split_report:
    near = lambda v: min(names, key=lambda s_: abs(stave_mid[s_] - v))
    for sp_ in SPLITS:
        print(f"{sp_['t0']:6.1f}-{sp_['t1']:6.1f}s  bars {bar_at(sp_['t0']):3d}-{bar_at(sp_['t1']):3d}  {near(sp_['va']):14s} + {near(sp_['vb']):14s}  {sp_['mode']} ({sp_['why']})")
    sys.exit()

ABBR_R = {"Flutes 1·2": "Fl", "Oboes 1·2": "Ob", "Cor anglais": "Ca", "Clarinets 1·2": "Cl", "Bass clarinet": "Bcl", "Bassoons 1·2": "Bn", "Contrabassoon": "Cbn", "Horns 1·2": "Hn12", "Horns 3·4": "Hn34", "Trumpets 1·2": "Tpt12", "Trumpet 3": "Tpt3", "Trombones 1·2": "Tbn12", "Bass trombone": "Btbn", "Tuba": "Tba", "Timpani": "Timp", "Percussion": "Perc", "Harp RH": "HpR", "Harp LH": "HpL", "Violins I": "Vn1", "Violins II": "Vn2", "Violas": "Va", "Violoncellos": "Vc", "Double basses": "Cb"}
if A.focus_report:
    bq = bar_qn
    if A.focus_report_full:   # staff layout, then per bar: start time, the camera's staff, onsets per staff
        print("# staves, top to bottom: name, centre y in px (one normal view covers about +-450 px around its centre)")
        for n_ in names: print(f"#   {n_:16s} {stave_mid[n_]:7.0f}")
    for b in range(1, len(bq)):
        t = q2s(bq[b - 1]); v = feat_v(t + 1.0)
        line = f"bar {b:3d} {t:6.1f}s  {min(names, key=lambda s_: abs(stave_mid[s_] - v))}"
        if A.focus_report_full:
            t1_ = q2s(bq[b]) if b < len(bq) else t + 4
            cnt = defaultdict(int)
            for n_ in N:
                if t - 1e-6 <= n_[0] < t1_ - 1e-6: cnt[n_[5]] += 1
            line += "  | " + ", ".join(f"{ABBR_R.get(k_, k_)} {cnt[k_]}" for k_ in names if cnt[k_])
        print(line)
    sys.exit()

# ---------- camera ----------
FOC = 2600.0
CAM = dict(az=45.0, el=38.0, roll=12.0, d=1450.0)
if os.environ.get("CAM"): CAM.update(json.loads(os.environ["CAM"]))
def camera(tu, tv, t, cx=None, cy=None, dmul=1.0, elx=0.0):
    """3D camera over the sheet (z up out of the paper), behind-left of the focus, looking up the page and along the line;
    the focus lands at screen (cx, cy) (default: centre, a little low)"""
    cx = W * 0.5 if cx is None else cx; cy = H * 0.55 if cy is None else cy
    az = math.radians(CAM["az"] + 2.0 * math.sin(t / 23.0))
    el = math.radians(CAM["el"] + elx + 1.5 * math.sin(t / 19.0))
    d = (CAM["d"] + 50 * math.sin(t / 31.0)) * dmul
    T = np.array([tu, tv, 0.0])
    back = np.array([-math.sin(az), math.cos(az), 0.0])
    C = T + d * (math.cos(el) * back + math.sin(el) * np.array([0, 0, 1.0]))
    f = T - C; f /= np.linalg.norm(f)
    r = np.cross(np.array([0, 0, 1.0]), f); r /= np.linalg.norm(r)
    u = np.cross(f, r)
    rl = math.radians(CAM["roll"]); cr, sr = math.cos(rl), math.sin(rl)
    def proj3(P):
        P = np.atleast_2d(P); D = P - C
        z = D @ f; x = FOC * (D @ r) / z; y = -FOC * (D @ u) / z
        return np.stack([cx + cr * x - sr * y, cy + sr * x + cr * y], 1), z
    src = np.float32([[tu - 400, tv - 400], [tu + 400, tv - 400], [tu + 400, tv + 400], [tu - 400, tv + 400]])
    dst, _ = proj3(np.c_[src, np.zeros(4)])
    return cv2.getPerspectiveTransform(src, dst.astype(np.float32)), proj3

# ---------- what a split-screen panel or a pull-back shows ----------
# The camera looks along the line at an angle, so the part of the paper where the music is being played (just left of
# the focus) is seen much further above the focus than below it. An annotation names one staff and a zoom per panel and
# assumes about 300 px x zoom of height either side of that staff; each panel is therefore fitted here to the staves
# that play within that height during the moment, and to the staff of any note on the score shown meanwhile.
_reach = {}
def reach(z, half, elx=0.0, xr=-60.0):
    """(up, down): how far above and below its focus a view pulled back by z shows the paper at the playing position
    (from 210 px behind the focus to xr px past it; rows above the focus are cut off on the right, so text that runs to
    the right there needs a larger xr). half: one panel of the stacked split, else the whole frame"""
    k_ = (round(z, 3), half, elx, round(xr / 20.0))
    if k_ not in _reach:
        hh_ = H * 0.5 if half else H
        _, proj = camera(0.0, 0.0, 0.0, W * 0.5, hh_ * 0.55, z, elx)
        def seen(dy, xs):
            P, zz = proj(np.array([[x_, dy, 0.0] for x_ in xs]))
            return bool(np.all(zz > 0) and np.all((P[:, 0] > 50) & (P[:, 0] < W - 50) & (P[:, 1] > 34) & (P[:, 1] < hh_ - 34)))
        up = dn = 0
        while up < 3000 and seen(-(up + 10), (-210.0, max(xr, -60.0))): up += 10
        while dn < 3000 and seen(dn + 10, (-210.0, -60.0)): dn += 10
        _reach[k_] = (up, dn)
    return _reach[k_]
def fit_view(reqs, prefer, half, elx=0.0, zmax=2.0):
    """(focus, zoom, fits): the least pull-back that shows every requirement (top, bottom, xr) at the playing position,
    with the focus as near to prefer as that allows"""
    for z in np.arange(1.0, zmax + 0.001, 0.05):
        lo_f = max(b_ - reach(float(z), half, elx)[1] for _, b_, _ in reqs)            # the focus may not be higher than this
        hi_f = min(t_ + reach(float(z), half, elx, x_)[0] for t_, _, x_ in reqs)       # nor lower than this
        if lo_f <= hi_f: return float(np.clip(prefer, lo_f, hi_f)), float(z), True
    return (lo_f + hi_f) / 2, float(z), False
def sees(f_, z, half, elx, reqs):
    return all(f_ - reach(z, half, elx, x_)[0] <= t_ and b_ <= f_ + reach(z, half, elx)[1] for t_, b_, x_ in reqs)
def plays(st, t0, t1):
    """the staff has at least two notes, or sounds for a quarter of the time, between t0 and t1"""
    ns = [(max(n_[0], t0), min(n_[1], t1)) for n_ in N if n_[5] == st and n_[0] < t1 - 1e-6 and n_[1] > t0 + 1e-6]
    return len(ns) >= 2 or sum(b_ - a_ for a_, b_ in ns) >= 0.25 * (t1 - t0)
PAD_UP, PAD_DN = 6.0 * sp, 4.5 * sp            # room for the staff, its ledger lines and its name above it
_STR = ["Violins I", "Violins II", "Violas", "Violoncellos", "Double basses"]
_WW = ["Flutes 1·2", "Oboes 1·2", "Cor anglais", "Clarinets 1·2", "Bass clarinet", "Bassoons 1·2", "Contrabassoon"]
_MENTION = [(r"\bflutes?\b", ["Flutes 1·2"]), (r"\boboes?\b", ["Oboes 1·2"]), (r"\bcor anglais\b", ["Cor anglais"]),
            (r"\bbass clarinet\b", ["Bass clarinet"]), (r"(?<!bass )\bclarinets?\b", ["Clarinets 1·2"]),
            (r"\bcontrabassoon\b", ["Contrabassoon"]), (r"\bbassoons?\b", ["Bassoons 1·2"]),
            (r"\bhorns? (?:1|2)\b", ["Horns 1·2"]), (r"\bhorns? (?:3|4)\b", ["Horns 3·4"]),
            (r"\bhorns\b(?! ?[1-4])|\bfour horns\b", ["Horns 1·2", "Horns 3·4"]),
            (r"\btrumpets? (?:1|2)\b", ["Trumpets 1·2"]), (r"\btrumpet 3\b", ["Trumpet 3"]), (r"\btrumpets\b(?! ?[1-3])", ["Trumpets 1·2", "Trumpet 3"]),
            (r"\bbass trombone\b", ["Bass trombone"]), (r"(?<!bass )\btrombones?\b", ["Trombones 1·2"]), (r"\btuba\b", ["Tuba"]),
            (r"\btimpani\b", ["Timpani"]), (r"\bharp\b", ["Harp RH", "Harp LH"]),
            (r"\bfirst violins?\b|\bviolins i\b|\bsolo violin\b", ["Violins I"]), (r"\bsecond violins?\b|\bviolins ii\b|\bviolins i·ii\b", ["Violins II"]),
            (r"\bviolins\b(?! i)|\bviolin sections\b", ["Violins I", "Violins II"]), (r"\bviolas?\b", ["Violas"]),
            (r"\bcellos?\b|\bvioloncellos?\b", ["Violoncellos"]), (r"\bbasses\b", ["Double basses"]),
            (r"\bstrings?\b", _STR), (r"\bwoodwinds?\b|\bwinds\b", _WW)]
def mentioned(text):
    """the staves an annotation's text names (instrument words; "strings" and "woodwind" as groups)"""
    t_ = text.lower()
    return {n_ for pat, sts in _MENTION if re.search(pat, t_) for n_ in sts}
def cap_span(c):
    """the paper a note on the score takes (top, bottom): its label above the bracket, the staff, chord names below"""
    v = stave_mid[c["anchor"]["staff"]]
    return v - 11.0 * sp, v + (8.5 if c.get("chords") else 4.5) * sp
def cap_reqs(c):
    """what must be in shot for a note on the score: its staff with the bracket (and chord names below), and the row
    of its label above, wide enough for the label (the label is moved along its row to stay in shot)"""
    v = stave_mid[c["anchor"]["staff"]]; al_ = ov.text_alpha(c.get("short", c["kind"]), "italic", 64)
    cw = 3.2 * sp * al_.shape[1] / al_.shape[0]
    return [(v - 4.5 * sp, v + (9.0 if c.get("chords") else 5.5) * sp, -60.0), (v - 11.0 * sp, v - 5.0 * sp, cw - 300.0)]
SPLIT_NOTES, SPLIT_INFO = [], []               # what the fit could not do (problems; remarks), for --annotations-check
def fit_splits(caps):
    staff_req = lambda n_: (stave_mid[n_] - PAD_UP, stave_mid[n_] + PAD_DN, -60.0)
    for sp_ in SPLITS:
        if sp_["mode"] not in ("stack", "pullback"): continue
        t0, t1 = sp_["t0"], sp_["t1"]
        during = [c for c in caps if c.get("anchor") and c["t0"] < t1 - 0.5 and c["t1"] > t0 + 0.5]
        if sp_["mode"] == "pullback":
            reqs = [(sp_["va"] - PAD_UP, sp_["vb"] + PAD_DN, -60.0)] + [r_ for c in during for r_ in cap_reqs(c)]
            sp_["fp"], sp_["zp"], ok = fit_view(reqs, (sp_["va"] + sp_["vb"]) / 2, False, 10.0, 2.6)
            if not ok: SPLIT_NOTES.append((sp_, "the pull-back cannot show all of it"))
            continue
        said = mentioned(sp_.get("what", ""))
        panels = {k_: dict(v=v_, must=[], want=sorted((n_ for n_ in names if abs(stave_mid[n_] - v_) <= 300 * z_ + 1 and plays(n_, t0, t1)), key=lambda n_: abs(stave_mid[n_] - v_)))
                  for k_, v_, z_ in (("a", sp_["va"], sp_["za0"]), ("b", sp_["vb"], sp_["zb0"]))}
        for c in during:                       # a note shown during the split goes into the panel nearer to its staff
            v = stave_mid[c["anchor"]["staff"]]
            panels[min(panels, key=lambda k_: abs(panels[k_]["v"] - v))]["must"].append(c)
        for k_, p_ in panels.items():
            which = "upper" if k_ == "a" else "lower"; reqs = []; left = []
            for c in p_["must"]:               # first the notes on the score
                if fit_view(reqs + cap_reqs(c), p_["v"], True, 0.0, 2.2)[2]: reqs += cap_reqs(c)     # a note may pull the panel back a little further
                else: SPLIT_NOTES.append((sp_, f"the note at {c['from']} on {c['anchor']['staff']} does not fit in the {which} panel"))
            for n_ in [n_ for n_ in p_["want"] if n_ in said]:      # then the playing staves the annotation's text names
                if fit_view(reqs + [staff_req(n_)], p_["v"], True)[2]: reqs.append(staff_req(n_))
                else: left.append(n_)
            if not reqs:                       # nothing named plays here: the named staff, or the nearest staff that plays
                reqs = [staff_req(p_["want"][0])] if p_["want"] else [(p_["v"] - PAD_UP, p_["v"] + PAD_DN, -60.0)]
            z_ = fit_view(reqs, p_["v"], True, 0.0, 2.2)[1]
            for n_ in [n_ for n_ in p_["want"] if n_ not in said]:  # other playing staves only where they need no further pull-back
                f2_, z2_, ok2_ = fit_view(reqs + [staff_req(n_)], p_["v"], True, 0.0, 2.2)
                if ok2_ and z2_ <= z_ + 1e-6: reqs.append(staff_req(n_))
            sp_["f" + k_], sp_["z" + k_], _ = fit_view(reqs, p_["v"], True, 0.0, 2.2)
            lo, hi = min(r_[0] for r_ in reqs), max(r_[1] for r_ in reqs)
            sp_["s" + k_] = sp_["z" + k_] * (1.4 if hi - lo > PAD_UP + PAD_DN + 1 else 1.0)   # several staves: light and keep sharp more of the height
            sp_["r" + k_] = (lo, hi)
            if left: SPLIT_INFO.append((sp_, f"{which} panel leaves out {', '.join(left)}"))
state = {"u": None, "v": None, "vv": 0.0}
# Up and down the camera moves as a critically damped spring (V_W rad/s), starting and stopping smoothly, with a speed
# limit (V_MAX px/s on the paper), and it starts toward a group LOOK seconds before the group is due. (A plain 2.5 s lag
# never arrived before the next change and left the camera between the groups.) Dan chose these gentler values with
# 60 fps on 2026-11-23 so that text stays readable during a move: the fastest move is about 24 px a frame on screen.
# The first full videos used 2.5 / 1300 / 1.0 at 30 fps (68 px a frame); the gentler moves leave the aim more than
# 300 px off a playing staff about 1 % more of the time (scherzo 2 %).
V_W = float(os.environ.get("V_W", 2.0))
V_MAX = float(os.environ.get("V_MAX", 900.0))
LOOK = float(os.environ.get("LOOK", 1.3))
state2 = {"v": None, "vv": 0.0}          # the second view of a split screen
def spring(st_, tv, dt):
    st_["vv"] += (V_W * V_W * (tv - st_["v"]) - 2 * V_W * st_["vv"]) * dt
    st_["vv"] = float(np.clip(st_["vv"], -V_MAX, V_MAX))
    st_["v"] += st_["vv"] * dt
def step(t, dt):
    """move the camera's focus for the frame at time t (along the line: 0.9 s lag; up and down: the spring above)"""
    tu = play_x(s2q(max(t + 0.6, 0))) + 120
    tv = feat_v(t + LOOK)
    ca = caption_target(t)
    if ca is not None: tv = ca                    # a note on the score holds the camera on its staff
    sa, sp_ = split_amount(t + 0.6)
    mode = sp_["mode"] if sp_ else "none"
    if sa > 0: va, vb = sp_.get("fa", sp_["va"]), sp_.get("fb", sp_["vb"])     # each panel's fitted focus
    if state["u"] is None: state["u"], state["v"], state["vv"] = tu, tv, 0.0
    state["u"] += (tu - state["u"]) * (1 - math.exp(-dt / 0.9))
    if sa > 0 and mode in ("stack", "slant"):
        tv = va                                   # the upper view takes the upper group
    elif sa > 0 and mode == "pullback":
        tv = sp_.get("fp", (va + vb) / 2)         # look between the groups while pulled back
    spring(state, tv, dt)
    if sa > 0:
        if state2["v"] is None: state2["v"], state2["vv"] = state["v"], state["vv"]   # the second view splits off the first
        other = vb if mode in ("stack", "slant") else (vb if abs(vb - state["v"]) > abs(va - state["v"]) else va)
        spring(state2, other, dt)
    else:
        state2["v"] = None

import overlays as ov
ICON_HOVER = 3.4 * sp                       # an icon floats this high over its note, so the lit note stays visible
# Names on the paper (Dan, 2026-11-23: the names appeared and moved about without a visible rule). Every name is now
# printed at a fixed place on the paper and never moves on it. Two rules place them:
#   1. Entry: where a part comes in after NAME_REST seconds or more of rest, its name ends just before its first note.
#   2. Column: at set bar lines about NAME_STEP px apart (the same bar lines for every staff), each part that is playing
#      through that bar line has its name again, ending at the bar line, so the names line up down the page as they do
#      at the start of a system in a printed score.
# A staff never has two names closer than NAME_NEAR px. A name is dim while its part rests and bright while it plays.
NAME_REST, NAME_STEP, NAME_NEAR, NAME_DIM = 2.5, 800.0, 500.0, 0.42
RUNS = {}                                   # per staff: stretches of playing with no rest of NAME_REST or more
for t0, t1, x, y, c, st in N:
    r_ = RUNS.setdefault(st, [])
    if r_ and t0 - r_[-1][1] < NAME_REST: r_[-1][1] = max(r_[-1][1], t1)
    else: r_.append([t0, t1, x])
NAME_COLS = []                              # (time, x) of the bar lines that carry a column of names
_last = min(n[2] for n in N)
for q_, x_ in sorted(BLX.items()):
    if x_ - _last >= NAME_STEP: NAME_COLS.append((q2s(q_), x_)); _last = x_
def name_size(st):
    al_ = ov.text_alpha(ov.NAME.get(st, st), "italic", 64)
    return al_, 3.0 * sp * al_.shape[1] / al_.shape[0]      # text 3 staff spaces high on the paper
NAME_LABELS = {}                            # per staff: [x of the text's right end, width, [(t0, t1) hidden by a note on the score]]
for st, runs in RUNS.items():
    ww = name_size(st)[1]; xs = []
    for t0, t1, x in runs:                  # rule 1; an entry on a column's bar line is lined up with the column
        xr = next((xc - 0.6 * sp for tc, xc in NAME_COLS if abs(tc - t0) < 1e-3), x - 1.6 * sp)
        if not xs or xr - xs[-1] >= NAME_NEAR: xs.append(xr)
    for tc, xc in NAME_COLS:                # rule 2
        xr = xc - 0.6 * sp
        if any(t0 < tc - 1e-3 and t1 > tc + 0.05 for t0, t1, _ in runs) and not any(-(ww + 4 * sp) < xr - x_ < NAME_NEAR for x_ in xs):
            xs.append(xr)
    NAME_LABELS[st] = [[xr, ww, []] for xr in sorted(xs)]
RUN_T0 = {st: [r_[0] for r_ in runs] for st, runs in RUNS.items()}
def part_active(st, t):
    """0..1: the part is playing (rises over the half second before an entry, falls after its last note)"""
    i = bisect.bisect_right(RUN_T0[st], t + 0.5) - 1
    if i < 0: return 0.0
    t0, t1, _ = RUNS[st][i]
    return float(np.clip(min((t - t0 + 0.5) / 0.5, (t1 + 1.4 - t) / 1.0), 0, 1))
def draw_names(layer, t, Hm, U):
    wf = Hm[2] @ np.array([U, 0.0, 1.0])
    for st, labs in NAME_LABELS.items():
        i0 = bisect.bisect_left(labs, [U - 2500.0]); i1 = bisect.bisect_right(labs, [U + 3500.0])
        if i0 >= i1: continue
        al_, _ = name_size(st); c = COL.get(st, np.float32([255, 255, 255]))
        a0 = NAME_DIM + (1 - NAME_DIM) * part_active(st, t)
        y1 = staves[st][0] - top - 0.6 * sp; y0 = y1 - 3.0 * sp
        for xr, ww, hid in labs[i0:i1]:
            a = a0 * (1 - max((ov.fade(t, h0 - 0.5, h1 + 0.5, 0.5) for h0, h1 in hid), default=0.0))
            if a <= 0.01: continue
            src = np.float64([[xr - ww, y0], [xr, y0], [xr, y1], [xr - ww, y1]])
            if np.any((np.c_[src, np.ones(4)] @ Hm[2]) * wf <= 0): continue      # part of it is behind the camera
            q = cv2.perspectiveTransform(np.float32(src)[None], Hm)[0]
            ov.warp_sprite(layer, al_, q, np.minimum(255, np.array(c) * 0.55 + 115) * a)
CAPS = []
if A.captions: CAPS = ov.load_captions(A.captions, pos_to_s)
elif ANN is not None and ANN.get("captions"): CAPS = ov.load_captions(ANN["captions"], pos_to_s)
# The camera needs time to travel. It leaves for a split 1.7 s before the split starts and is free again 0.5 s after it
# ends, and it takes about 1.5 s to reach a staff it cannot see yet. Where a note on the score sits next to a split
# that does not show its staff, or two notes on distant staves follow each other directly, the times are trimmed here
# (the note if it stays 4.5 s long, else the split if it stays 4 s long) so that every note is in shot while it is shown.
TIME_NOTES, TIME_INFO = [], []
def in_split_view(c, sp_):
    if sp_["mode"] == "pullback": return sees(sp_["fp"], sp_["zp"], False, 10.0, cap_reqs(c))
    return any(sees(sp_["f" + k_], sp_["z" + k_], True, 0.0, cap_reqs(c)) for k_ in "ab")
def settle_times(caps):
    mm = lambda t: f"{int(t // 60)}:{t % 60:04.1f}"
    CMIN, SMIN = 4.0, 3.5                                             # shortest note and split after a trim
    seq = [c for c in caps if c.get("anchor")]
    for i_, c in enumerate(seq):
        prev_end = seq[i_ - 1]["t1"] if i_ else -1e9
        next_start = seq[i_ + 1]["t0"] if i_ + 1 < len(seq) else 1e9
        for sp_ in SPLITS:
            if sp_["mode"] not in ("stack", "pullback"): continue
            if (c["t0"] < sp_["t1"] - 0.5 and c["t1"] > sp_["t0"] + 0.5) or in_split_view(c, sp_): continue
            cd, sd = c["t1"] - c["t0"], sp_["t1"] - sp_["t0"]
            if sp_["t0"] - 1.7 < c["t1"] <= sp_["t0"] + 0.5:          # the note ends as the camera leaves for the split
                need = c["t1"] - (sp_["t0"] - 1.7)
                keeps = all(tc <= c["t1"] - need - 0.3 for tc, _ in c.get("chords", []))     # no chord name lost
                if cd - need >= CMIN and keeps: c["t1"] -= need; TIME_INFO.append((c, f"ends {need:.1f} s earlier, before the split at {mm(sp_['t0'])}"))
                elif sd - need >= SMIN: sp_["t0"] += need; TIME_INFO.append((sp_, f"starts {need:.1f} s later, after the note ending {mm(c['t1'])}"))
                elif cd - need >= CMIN: c["t1"] -= need; TIME_INFO.append((c, f"ends {need:.1f} s earlier, before the split at {mm(sp_['t0'])}"))
                elif c["t0"] - need >= prev_end + 0.2: c["t0"] -= need; c["t1"] -= need; TIME_INFO.append((c, f"shown {need:.1f} s earlier, before the split at {mm(sp_['t0'])}"))
                else: TIME_NOTES.append((c, f"ends {sp_['t0'] - c['t1']:.1f} s before the split at {mm(sp_['t0'])}, which does not show its staff"))
            if sp_["t1"] - 0.5 <= c["t0"] < sp_["t1"] + 2.0:          # the note starts before the camera is back from the split
                need = sp_["t1"] + 2.0 - c["t0"]
                if cd - need >= CMIN: c["t0"] += need; TIME_INFO.append((c, f"starts {need:.1f} s later, after the split ending {mm(sp_['t1'])}"))
                elif sd - need >= SMIN: sp_["t1"] -= need; TIME_INFO.append((sp_, f"ends {need:.1f} s earlier, before the note at {mm(c['t0'])}"))
                elif c["t1"] + need <= next_start - 0.2: c["t0"] += need; c["t1"] += need; TIME_INFO.append((c, f"shown {need:.1f} s later, after the split ending {mm(sp_['t1'])}"))
                else: TIME_NOTES.append((c, f"starts {c['t0'] - sp_['t1']:.1f} s after the split ending {mm(sp_['t1'])}, which does not show its staff"))
    for a, b in zip(seq, seq[1:]):                                    # two notes in a row on staves too far apart for one view
        need = 1.5 - (b["t0"] - a["t1"])
        if need <= 0 or any(c["t0"] < sp_["t1"] + 0.5 and c["t1"] > sp_["t0"] - 1.7 for c in (a, b) for sp_ in SPLITS): continue
        if sees(stave_mid[a["anchor"]["staff"]] - 4 * sp, 1.0, False, 0.0, cap_reqs(b)): continue
        keeps = all(tc <= a["t1"] - need - 0.3 for tc, _ in a.get("chords", []))
        if a["t1"] - a["t0"] - need >= CMIN and keeps: a["t1"] -= need; TIME_INFO.append((a, f"ends {need:.1f} s earlier, so the camera can reach the next note"))
        elif b["t1"] - b["t0"] - need >= CMIN: b["t0"] += need; TIME_INFO.append((b, f"starts {need:.1f} s later, so the camera can reach it"))
        elif a["t1"] - a["t0"] - need >= CMIN: a["t1"] -= need; TIME_INFO.append((a, f"ends {need:.1f} s earlier, so the camera can reach the next note"))
        else: TIME_NOTES.append((b, f"follows the note on {a['anchor']['staff']} too closely for the camera to reach it"))
def caption_target(t):
    """while a note on the score is shown (and 2 s before, so the camera has arrived), aim at its staff, a little above
    the staff's middle so the label over it is in shot too"""
    if A.caption_style != "score": return None
    for c in CAPS:
        an = c.get("anchor")
        if an and c["t0"] - 2.0 <= t <= c["t1"]: return stave_mid[an["staff"]] - 4 * sp
    return None
VIEW_Y = [0.0, float(H)]        # the rows of the frame that the view being drawn fills (one panel of a split fills half)
def visible_span_x(Hm, ys, U, margin=110):
    """(left, right): the stretch of the strip, along the heights ys, that this view shows at least margin px inside
    its part of the frame (found on a 20 px grid, then refined by bisection so that text held at an end moves smoothly)"""
    wf = Hm[2] @ np.array([U, ys[0], 1.0])
    def good_at(xs):
        ok_all = np.ones(len(xs), bool)
        for y in ys:
            P = Hm @ np.stack([xs, np.full_like(xs, y), np.ones_like(xs)])
            w = P[2]; ok = w * wf > 0                              # the same side of the camera as the focus
            sx = np.where(ok, P[0] / np.where(ok, w, 1), -1e9); sy = np.where(ok, P[1] / np.where(ok, w, 1), -1e9)
            ok_all &= ok & (sx >= margin) & (sx < W - margin * 0.5) & (sy > VIEW_Y[0] + 30) & (sy < VIEW_Y[1] - 30)
        return ok_all
    xs = np.arange(U - 5000, U + 5001, 20, dtype=np.float64)
    good = np.nonzero(good_at(xs))[0]
    if not len(good): return U - 950, U - 950
    def refine(inside, outside):
        for _ in range(12):
            mid = (inside + outside) / 2
            if good_at(np.array([mid]))[0]: inside = mid
            else: outside = mid
        return inside
    return refine(float(xs[good[0]]), float(xs[good[0]]) - 20.0), refine(float(xs[good[-1]]), float(xs[good[-1]]) + 20.0)
def x_at_s(ts):
    """x on the strip at score time ts (first notes, or the bar line when it is a bar's start)"""
    q = s2q(ts)
    for bq, bx in BLX.items():
        if abs(bq - q) < 1e-3: return bx
    return play_x(q) - 1.2 * sp
if ANN is not None:
    fit_splits(CAPS); settle_times(CAPS); SPLIT_NOTES.clear(); SPLIT_INFO.clear(); fit_splits(CAPS)
# A note's label is written at one fixed place on the paper: at the start of its bracket, or further right when the
# passage is long, so that it is still in shot when the note is about to go. (It follows the left edge of the frame
# only if no fixed place is in shot for the whole time.)
for c in CAPS:
    an = c.get("anchor")
    if not an: continue
    al_ = ov.text_alpha(c.get("short", c["kind"]), "italic", 64); cw = 3.2 * sp * al_.shape[1] / al_.shape[0]
    bx0 = x_at_s(an["t0"]) - sp
    need = play_x(s2q(max(c["t1"] - 0.8, c["t0"]))) - 330       # in shot shortly before the note goes
    room = play_x(s2q(c["t0"])) + 880 - cw                      # in shot when the note appears
    in_split = any(c["t0"] < sp_["t1"] + SPLIT_IN and c["t1"] > sp_["t0"] - SPLIT_IN for sp_ in SPLITS)
    c["lx"] = bx0 if in_split else min(max(bx0, need), max(bx0, room))   # a split's panel is too narrow for a place further right
    if A.labels == "names" and A.caption_style == "score":      # a name gives way while a note is drawn over its place
        bx1 = max(x_at_s(an["t1"]) - sp, c["lx"] + cw)
        for lab in NAME_LABELS.get(an["staff"], []):
            if lab[0] > bx0 - 3 * sp and lab[0] - lab[1] < bx1 + 3 * sp: lab[2].append((c["t0"], c["t1"]))
if A.annotations_check:
    mmss = lambda t: f"{int(t // 60)}:{t % 60:04.1f}"
    def onsets(st, t0, t1): return sum(1 for n_ in N if n_[5] == st and t0 - 1e-6 <= n_[0] < t1 - 1e-6)
    def sounding(st, t0, t1): return sum(1 for n_ in N if n_[5] == st and n_[0] < t1 - 1e-6 and n_[1] > t0 + 1e-6)
    end_s = q2s(bar_qn[-1]); bad = 0
    def flag(msg):
        global bad
        bad += 1; print(f"      !! {msg}")
    print(f"splits: {len(ANN.get('splits', []))}")
    for i_, (x, sp_) in enumerate(zip(ANN.get("splits", []), SPLITS)):
        d_ = sp_["t1"] - sp_["t0"]; dist = sp_["vb"] - sp_["va"]
        near_ = lambda v: ABBR_R.get(min(names, key=lambda n_: abs(stave_mid[n_] - v)), "?")
        shows = (f"pulled back x{sp_['zp']:.2f}" if sp_["mode"] == "pullback" else
                 " | ".join(f"{near_(sp_['r' + k_][0] + PAD_UP)}-{near_(sp_['r' + k_][1] - PAD_DN)} x{sp_['z' + k_]:.2f}" for k_ in "ab"))
        print(f"  {mmss(sp_['t0'])}-{mmss(sp_['t1'])} ({d_:4.1f} s) bars {x.get('bars', '?'):9s} {sp_['mode']:8s} {ABBR_R.get(x['upper'])} x{sp_['za0']} / {ABBR_R.get(x['lower'])} x{sp_['zb0']}; shows {shows}")
        for s2_, msg in SPLIT_NOTES:
            if s2_ is sp_: flag(msg)
        for s2_, msg in SPLIT_INFO + TIME_INFO:
            if s2_ is sp_: print(f"      ({msg})")
        if not (0 <= sp_["t0"] < sp_["t1"] <= end_s + 1e-6): flag("outside the movement")
        if d_ < 3.0: flag("shorter than 3 s")
        if dist <= 0: flag("upper is not above lower")
        if sp_["mode"] not in ("stack", "pullback"): flag(f"mode {sp_['mode']}")
        if not (1.0 <= sp_["za0"] <= 1.8 and 1.0 <= sp_["zb0"] <= 1.8): flag("zoom outside 1.0-1.8")
        if i_ and sp_["t0"] - SPLITS[i_ - 1]["t1"] < 4.0: flag(f"only {sp_['t0'] - SPLITS[i_ - 1]['t1']:.1f} s after the previous split")
    print(f"notes: {len(CAPS)}")
    for i_, c in enumerate(CAPS):
        d_ = c["t1"] - c["t0"]; an = c.get("anchor")
        print(f"  {mmss(c['t0'])}-{mmss(c['t1'])} ({d_:4.1f} s) bars {c.get('bars', '?'):9s} {c['kind']:13s} [{an['staff'] if an else '-'}] {c.get('short', '')}")
        if not (0 <= c["t0"] < c["t1"] <= end_s + 1e-6): flag("outside the movement")
        if not (4.0 - 1e-3 <= d_ <= 12.0 + 1e-3): flag("not 4-12 s long")
        if an and (an["t0"] > c["t1"] or an["t1"] < c["t0"]): flag("the bracket is not shown during the note's time")
        if i_ and c["t0"] < CAPS[i_ - 1]["t1"] - 1e-6: flag("overlaps the previous note")
        if len(c.get("short", "")) > 48: flag(f"short text has {len(c['short'])} characters")
        if c["kind"] not in ("Theme", "Motive", "Harmony", "Counterpoint", "Form", "Orchestration", "Quotation"): flag(f"kind {c['kind']}")
        if not an: flag("no anchor"); continue
        if not sounding(an["staff"], an["t0"], an["t1"]): flag(f"{an['staff']} has no notes inside the bracket")
        if an["t1"] <= an["t0"]: flag("anchor ends before it starts")
        for tc, lab in c.get("chords", []):
            if not (c["t0"] - 4.0 <= tc <= c["t1"]): flag(f"chord {lab} at {mmss(tc)} is outside the note's time")
        for c2_, msg in TIME_INFO:
            if c2_ is c: print(f"      ({msg})")
        for c2_, msg in TIME_NOTES:
            if c2_ is c: flag(msg)
    print(f"{bad} problems")
    sys.exit(1 if bad else 0)
def draw_score_notes(layer, t, Hm, U):
    """caption style 'score': a bracket drawn round the passage, its label written on the paper above it, and chord
    names written above the staff as the music reaches them"""
    for c in CAPS:
        a = ov.fade(t, c["t0"], c["t1"])
        if a <= 0: continue
        an = c.get("anchor")
        if an:
            st = an["staff"]; x0, x1 = x_at_s(an["t0"]) - sp, x_at_s(an["t1"]) - sp
            y0, y1 = staves[st][0] - top - 2.2 * sp, staves[st][1] - top + 2.2 * sp
            pts = np.float32([[x0, y0], [x1, y0], [x1, y1], [x0, y1], [x0, y0]])
            # the outline draws itself over 0.8 s
            dr = float(np.clip((t - c["t0"]) / 0.8, 0, 1))
            seg = np.linalg.norm(np.diff(pts, axis=0), axis=1); L = seg.sum() * dr
            path = [pts[0]]
            for i_, sl in enumerate(seg):
                if L <= 0: break
                f_ = min(1.0, L / sl); path.append(pts[i_] + (pts[i_ + 1] - pts[i_]) * f_); L -= sl
            P = cv2.perspectiveTransform(np.float32(path)[None], Hm)[0]
            cv2.polylines(layer, [np.round(P * 4).astype(np.int32)], False, (np.float32(ov.GOLD) * 0.9 * a).tolist(), 2, cv2.LINE_AA, 2)
            lab = c.get("short", c["kind"])
            al_ = ov.text_alpha(lab, "italic", 64)
            hh = 3.2 * sp; ww = hh * al_.shape[1] / al_.shape[0]
            yb = y0 - 0.9 * sp
            xl_, xr_ = visible_span_x(Hm, [yb, yb - hh - 2.2 * sp], U)
            x0 = max(min(c["lx"], xr_ - ww), xl_)                # fixed on the paper; moved only as far as keeps it in the shot
            q = cv2.perspectiveTransform(np.float32([[[x0, yb - hh], [x0 + ww, yb - hh], [x0 + ww, yb], [x0, yb]]]), Hm)[0]
            ov.warp_sprite(layer, al_, q, np.float32(ov.GOLD) * a)
            kd = ov.text_alpha(c["kind"].upper(), "sansbold", 40)
            hk = 1.7 * sp; wk = hk * kd.shape[1] / kd.shape[0]
            yk = yb - hh - 0.5 * sp
            q = cv2.perspectiveTransform(np.float32([[[x0, yk - hk], [x0 + wk, yk - hk], [x0 + wk, yk], [x0, yk]]]), Hm)[0]
            ov.warp_sprite(layer, kd, q, np.float32(ov.GOLD) * 0.75 * a)
        for tc, lab in c.get("chords", []):
            if t < tc - 0.15: continue
            ac = a * float(np.clip((t - tc + 0.15) / 0.3, 0, 1))
            st = c.get("chord_staff", an["staff"] if an else names[0])
            x0 = play_x(s2q(tc)) - 0.4 * sp
            hh = 2.6 * sp; y1 = staves[st][1] - top + 3.0 * sp + hh   # below the staff, as harmonic analysis is written; the label is above
            al_ = ov.text_alpha(lab, "serif", 64); ww = hh * al_.shape[1] / al_.shape[0]
            q = cv2.perspectiveTransform(np.float32([[[x0, y1 - hh], [x0 + ww, y1 - hh], [x0 + ww, y1], [x0, y1]]]), Hm)[0]
            ov.warp_sprite(layer, al_, q, np.float32([235, 238, 255]) * ac)
def draw_caption_panel(img, t):
    for c in CAPS:
        a = ov.fade(t, c["t0"], c["t1"])
        if a <= 0: continue
        if A.caption_style == "bar":
            o, y0 = ov.bar_overlay(c, W, H); ov.composite(img, o, 0, y0, a)
        else:
            o, (x0, y0) = ov.card_overlay(c, W, H); ov.composite(img, o, x0, y0, a)

_gr = np.random.default_rng(7)
GRAIN = [(_gr.normal(0, 1.0, (H, W, 1))).astype(np.float32) for _ in range(8)]
def view(t, U, V, cx=None, cy=None, dmul=1.0, elx=0.0, spread=1.0):
    """the sheet, the lit notes and the lights as one camera at focus (U, V) sees them (float RGB, before vignette)"""
    Hm, proj3 = camera(U, V, t, cx, cy, dmul, elx)
    # crop the flat sheet to what the camera can see
    Hi = np.linalg.inv(Hm)
    cs = cv2.perspectiveTransform(np.float32([[[0, 0], [W, 0], [W, H], [0, H], [W / 2, 0]]]), Hi)[0]
    reach = 7000 * dmul
    u0 = int(max(0, min(U - 5000 * dmul, cs[:, 0].min()))); u1 = int(min(FW, max(cs[:, 0].max(), 0)))
    u0 = max(u0, int(U - reach)); u1 = min(u1, int(U + reach))
    if u1 <= u0 + 10: u0, u1 = 0, min(FW, 14000)
    Tm = np.array([[1, 0, u0], [0, 1, 0], [0, 0, 1]], np.float64)
    img = cv2.warpPerspective(flat[:, u0:u1], Hm @ Tm, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(10, 10, 12)).astype(np.float32)
    # lighting: dim the sheet away from the playing area
    fx, fy = cv2.perspectiveTransform(np.float32([[[U, V]]]), Hm)[0, 0]
    yy, xx = np.mgrid[0:H:8, 0:W:8]
    fall = np.exp(-(((xx - fx) / 1500) ** 2 + ((yy - fy) / (900 * spread)) ** 2)).astype(np.float32)
    fall = cv2.resize(0.45 + 0.45 * fall, (W, H))
    img *= fall[..., None]
    # depth of field: soften far from the focus
    blur = cv2.GaussianBlur(img, (0, 0), 3.0)
    dm = cv2.resize(np.clip((np.abs(yy - fy) / (520 * spread)) ** 1.5 + (np.abs(xx - fx) / 1500) ** 2, 0, 1).astype(np.float32), (W, H))
    img = img * (1 - dm[..., None]) + blur * dm[..., None]
    # notes lit now
    lo = np.searchsorted(NT0, t - 40); hi = np.searchsorted(NT0, t + 0.001)
    idx = np.arange(lo, hi)
    idx = idx[(NT1[idx] + 30 > t)]
    glow = np.zeros((H, W, 3), np.float32)
    if len(idx):
        age = t - NT0[idx]
        held = t <= NT1[idx]
        tied = NTIE[idx]
        inten = np.where(held, 0.7 + np.where(tied, 0.0, 0.3 * np.exp(-age / 0.35)), 0.7 * (0.55 + 0.45 * np.exp(-(t - NT1[idx]) / 1.5)) * np.exp(-(t - NT1[idx]) / 14.0))
        inten *= np.where(tied, 1.0, np.clip(age / 0.04, 0, 1))
        Lg = 0.72 + 0.5 * loud(t)
        inten = np.where(held, inten * Lg, inten)
        pts = cv2.perspectiveTransform(np.stack([NX[idx], NY[idx]], 1)[None].astype(np.float32), Hm)[0]
        pr = cv2.perspectiveTransform(np.stack([NX[idx] + sp * 0.62, NY[idx]], 1)[None].astype(np.float32), Hm)[0]
        pv = cv2.perspectiveTransform(np.stack([NX[idx], NY[idx] + sp * 0.48], 1)[None].astype(np.float32), Hm)[0]
        _, ndep = proj3(np.c_[NX[idx], NY[idx], np.zeros(len(idx))])   # depth in front of the camera
        for j in range(len(idx)):
            I = float(inten[j])
            if I < 0.02 or ndep[j] < 300: continue    # notes behind the camera would project mirrored, as huge blobs
            x, y = pts[j]
            if not (-80 < x < W + 80 and -80 < y < H + 80): continue
            ax = float(np.hypot(*(pr[j] - pts[j]))); ay = float(np.hypot(*(pv[j] - pts[j])))
            ang = math.degrees(math.atan2(*(pr[j] - pts[j])[::-1]))
            c = NC[idx[j]] * I
            cv2.ellipse(glow, (int(x * 4), int(y * 4)), (max(1, int(ax * 4)), max(1, int(ay * 4))), ang, 0, 360, c.tolist(), -1, cv2.LINE_AA, 2)
            cv2.ellipse(glow, (int(x * 4), int(y * 4)), (max(1, int(ax * 2.0)), max(1, int(ay * 2.0))), ang, 0, 360, (np.minimum(255, NC[idx[j]] * 0.4 + 160) * I).tolist(), -1, cv2.LINE_AA, 2)
            if age[j] < 0.3 and not tied[j]:   # a thin ring spreads out from the note as it is struck (not a tied continuation)
                s_ = age[j] / 0.3; rk = 1.3 + 1.6 * s_
                cv2.ellipse(glow, (int(x * 4), int(y * 4)), (max(1, int(ax * 4 * rk)), max(1, int(ay * 4 * rk))), ang, 0, 360, (NC[idx[j]] * 0.55 * (1 - s_) ** 2).tolist(), 3, cv2.LINE_AA, 2)
    # the bouncing lights
    bl_ = balls_at(t)
    ovl = np.zeros((H, W, 3), np.float32)          # crisp light drawn after the halos: letters, names, notes on the score
    if bl_:
        B = np.array([[b[0], b[1] - top, b[2] + (ICON_HOVER if (A.labels == "icons" and b[6] == 0) else 0)] for b in bl_], np.float64)
        sc, dep = proj3(B)
        gp, _ = proj3(np.c_[B[:, :2], np.zeros(len(B))])
        # motion trail: where each airborne ball was over the last few frames
        for kt in range(1, 7):
            tb = [b for b in balls_at(t - kt * 0.018) if b[2] > 3]
            if not tb: continue
            TB = np.array([[b[0], b[1] - top, b[2] + (ICON_HOVER if (A.labels == "icons" and b[6] == 0) else 0)] for b in tb], np.float64)
            tsc, tdep = proj3(TB)
            for (x_, y_, z_, al, col, *_), (sx, sy), dz in zip(tb, tsc, tdep):
                if dz <= 300: continue
                rr = FOC * 0.42 * sp / dz * (1 - kt * 0.1)
                cv2.circle(glow, (int(sx * 4), int(sy * 4)), max(2, int(rr * 4)), (np.array(col, np.float32) * al * 0.5 * (1 - kt / 7)).tolist(), -1, cv2.LINE_AA, 2)
        for (x_, y_, z_, al, col, st_, j_), (sx, sy), dz, (gx, gy) in zip(bl_, sc, dep, gp):
            if al <= 0.01 or dz <= 300: continue    # a ball at or behind the camera (a long note's head) would cover the frame
            rr = FOC * 0.42 * sp / dz
            c = np.array(col, np.float32)
            icon = A.labels == "icons" and j_ == 0
            zz = z_ + (ICON_HOVER if icon else 0)
            if zz > 4:   # a pool of light on the paper under the ball, fainter the higher it flies
                pa = al * 0.5 * max(0.0, 1 - zz / 260)
                cv2.ellipse(glow, (int(gx * 4), int(gy * 4)), (int(rr * 4 * 2.2), int(rr * 4 * 1.1)), CAM["roll"], 0, 360, (c * pa).tolist(), -1, cv2.LINE_AA, 2)
            if icon:     # the light drawn as its instrument, hovering over the note: a soft glow behind, the icon crisp
                cv2.circle(glow, (int(sx * 4), int(sy * 4)), max(2, int(rr * 4 * 1.6)), (c * al * 0.55).tolist(), -1, cv2.LINE_AA, 2)
                ov.add_sprite(ovl, ov.icon_alpha(ov.ICON.get(st_, "violin"), float(np.clip(rr * 9.0, 64, 112))), sx, sy,
                              np.minimum(255, c * 0.5 + 135) * al)
            else:
                cv2.circle(glow, (int(sx * 4), int(sy * 4)), max(2, int(rr * 4)), (np.minimum(255, c * 0.55 + 140) * al * 1.25).tolist(), -1, cv2.LINE_AA, 2)
            if A.labels == "letters" and j_ == 0:   # the part's abbreviation riding just above its light
                fp = float(np.clip(rr * 4.2, 28, 46))
                w_ = al * float(np.clip(1.35 - math.hypot(sx - W / 2, sy - H * 0.55) / (0.6 * W), 0, 1))
                if w_ > 0.02:
                    ov.add_sprite(ovl, ov.text_alpha(ov.ABBR.get(st_, st_), "sansbold", fp), sx, sy - rr - fp * 0.8,
                                  np.minimum(255, c * 0.6 + 110) * w_)
    if A.labels == "names": draw_names(ovl, t, Hm, U)
    if CAPS and A.caption_style == "score": draw_score_notes(ovl, t, Hm, U)
    core = glow
    # tight halo keeps each note separate; the wide one only tints the paper.
    # A soft limit stops overlapping halos from adding up to a white blob.
    halo1 = cv2.GaussianBlur(core, (0, 0), 4.5)
    halo2 = cv2.GaussianBlur(cv2.resize(core, (W // 4, H // 4), interpolation=cv2.INTER_AREA), (0, 0), 9)
    halo2 = cv2.resize(halo2, (W, H))
    whiten = core.max(2, keepdims=True) * 0.3
    G = core * 1.1 + whiten + halo1 * 3.0
    G = 250 * (1 - np.exp(-G / 250))
    Hw = halo2 * (3.4 + 2.6 * loud(t))
    Hw = 95 * (1 - np.exp(-Hw / 95))
    out = img + G + Hw + img * (halo1 * 1.0 + Hw).mean(2, keepdims=True) / 160
    if ovl.any():   # darken the paper round the text so it reads over the notation, then add the text
        m = cv2.GaussianBlur(np.clip(ovl.max(2) / 90, 0, 1), (0, 0), 7)
        out *= 1 - 0.62 * np.clip(m * 2.2, 0, 1)[..., None]
        out += ovl + cv2.GaussianBlur(ovl, (0, 0), 2.4) * 0.9
    return out, Hm

_yy, _xx = np.mgrid[0:H, 0:W].astype(np.float32)
VIGNETTE = np.clip(1.15 - 0.55 * (((_xx - W / 2) / (W / 2)) ** 2 + ((_yy - H / 2) / (H / 2)) ** 2), 0, 1)[..., None]
def frame_at(t, dt):
    step(t, dt)
    sa, sp_ = split_amount(t + 0.6)
    mode = sp_["mode"] if sp_ else "none"
    if sp_: va, vb, za, zb = sp_["va"], sp_["vb"], sp_["za"], sp_["zb"]
    U = state["u"]
    if sa <= 0.001 or mode == "none":
        out, Hm = view(t, U, state["v"])
    elif mode == "pullback":
        far = abs(vb - va)
        zp = sp_.get("zp", float(np.clip((far + 700) / 1000, 1, 2.6)))
        out, Hm = view(t, U, state["v"], dmul=1 + sa * (zp - 1), elx=sa * 10, spread=1 + sa * 1.6)
    elif mode == "inset":
        out, Hm = view(t, U, state["v"])
        sub, _ = view(t, U, state2["v"], dmul=0.92)
        sw, sh = int(W * 0.40), int(H * 0.40)
        small = cv2.resize(sub * VIGNETTE ** 0.5, (sw, sh), interpolation=cv2.INTER_AREA)
        below = state2["v"] > state["v"]
        x0 = W - sw - 44; y0 = (H - sh - 44) if below else 44
        sc_ = 0.85 + 0.15 * sa                        # the window grows in from its corner
        small = cv2.resize(small, (max(8, int(sw * sc_)), max(8, int(sh * sc_))), interpolation=cv2.INTER_AREA)
        sh2, sw2 = small.shape[:2]; x0 += sw - sw2; y0 += (sh - sh2) if below else 0
        shadow = np.zeros((H, W), np.float32); shadow[y0:y0 + sh2, x0:x0 + sw2] = 1
        shadow = cv2.GaussianBlur(shadow, (0, 0), 18)[..., None]
        out = out * (1 - 0.55 * sa * shadow)
        inset = (small, x0, y0, sa)                   # pasted after the vignette, so the corner window stays bright
    else:   # stack / slant: the lower view opens from the foot of the frame
        yd = H * (1 - 0.5 * sa)
        if mode == "stack":
            ca, cb_ = (W * 0.5, yd * 0.55), (W * 0.5, yd + (H - yd) * 0.55)
        else:
            ca, cb_ = (W * 0.46, yd * 0.55), (W * 0.54, yd + (H - yd) * 0.55)
        VIEW_Y[:] = [0.0, yd]
        top_, Hm = view(t, U, state["v"], *ca, dmul=1 + sa * (za - 1), spread=1 + sa * (sp_.get("sa", za) - 1))
        VIEW_Y[:] = [yd, float(H)]
        bot_, Hm2 = view(t, U, state2["v"], *cb_, dmul=1 + sa * (zb - 1), spread=1 + sa * (sp_.get("sb", zb) - 1))
        VIEW_Y[:] = [0.0, float(H)]
        if mode == "stack":
            ang = 0.0
        else:   # the seam runs with the staff lines as they lie on the screen
            p0, p1 = cv2.perspectiveTransform(np.float32([[[U - 300, state["v"]], [U + 300, state["v"]]]]), Hm)[0]
            ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
        sd = (_yy - yd) - (_xx - W / 2) * math.tan(ang)          # signed distance below the seam (vertical)
        m = np.clip(sd / 3.0 + 0.5, 0, 1)[..., None]
        out = top_ * (1 - m) + bot_ * m
        seam = np.exp(-(sd / 1.6) ** 2)[..., None] * np.float32([150, 160, 185]) * sa
        out += seam + cv2.GaussianBlur(seam, (0, 0), 6) * 1.2
    # vignette
    out *= VIGNETTE
    if mode == "inset" and sa > 0.001:
        small, x0, y0, sa = inset; sh2, sw2 = small.shape[:2]
        win = out[y0:y0 + sh2, x0:x0 + sw2]
        out[y0:y0 + sh2, x0:x0 + sw2] = win * (1 - sa) + small * sa
        frame = np.zeros((H, W, 3), np.float32)
        cv2.rectangle(frame, (x0, y0), (x0 + sw2 - 1, y0 + sh2 - 1), (205, 212, 228), 2, cv2.LINE_AA)
        out += (frame + cv2.GaussianBlur(frame, (0, 0), 3) * 0.8) * 0.55 * sa
    out += GRAIN[int(t * 30) % len(GRAIN)]   # fine film grain so the dark sheet doesn't band
    if CAPS and A.caption_style in ("bar", "card"): draw_caption_panel(out, t)
    return np.clip(out, 0, 255).astype(np.uint8)

if A.bars:
    T0 = q2s(bar_qn[A.bars[0] - 1]) - 1.5; T1 = q2s(bar_qn[A.bars[1]]) + 1.0
else:
    T0, T1 = -2.0, q2s(END_QN) + 7.0

if A.still:
    for t in A.still:
        state["u"] = None                     # step the camera from the start, as the video does
        for kk in range(int((t - T0) * A.fps), 0, -1): step(t - kk / A.fps, 1 / A.fps)
        cv2.imwrite(f"{A.out}-{t:07.2f}.png", cv2.cvtColor(frame_at(t, 1 / A.fps), cv2.COLOR_RGB2BGR))
    sys.exit()

dur = T1 - T0
n = int(dur * A.fps)
VENC = ["-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p"]

def render(i0, i1, out):
    """frames i0..i1-1 to a video-only file (the camera is first stepped through the earlier frames)"""
    for i in range(i0):
        step(T0 + i / A.fps, 1 / A.fps)
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(A.fps), "-i", "-"] + VENC + [out]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(i0, i1):
        t = T0 + i / A.fps
        f = frame_at(t, 1 / A.fps)
        fade = min(1, (t - T0) / 0.8, (T1 - t) / 1.2)
        if fade < 1: f = (f * max(fade, 0)).astype(np.uint8)
        pr.stdin.write(f.tobytes())
        if (i - i0) % 300 == 0: print(f"part {i0}-{i1}: {i - i0}/{i1 - i0}", file=sys.stderr, flush=True)
    pr.stdin.close(); pr.wait()

if CHILD:
    render(A.part[0], A.part[1], A.out)
    sys.exit()

tmp = tempfile.mkdtemp(prefix="glow-", dir=os.path.dirname(os.path.abspath(A.out)))
parts = []
cuts = np.linspace(0, n, A.jobs + 1).astype(int)
procs = []
for j in range(A.jobs):
    pf = f"{tmp}/part{j:02d}.mp4"; parts.append(pf)
    args = [sys.executable, os.path.abspath(__file__), "--strip", A.strip, "--tempo", A.tempo, "--out", pf, "--fps", str(A.fps),
            "--part", str(cuts[j]), str(cuts[j + 1])]
    if _ea: args += ["--env", _ea]
    if A.stems: args += ["--stems", A.stems]
    if A.bars: args += ["--bars", str(A.bars[0]), str(A.bars[1])]
    args += ["--split", A.split, "--labels", A.labels, "--caption-style", A.caption_style]
    if A.split_bars: args += ["--split-bars"] + [str(b) for b in A.split_bars]
    if A.split_staves: args += ["--split-staves"] + A.split_staves
    if A.annotations: args += ["--annotations", A.annotations]
    if A.captions: args += ["--captions", A.captions]
    procs.append(subprocess.Popen(args, env=dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")))
codes = [p.wait() for p in procs]
if any(codes): sys.exit(f"a part failed: {codes}")
open(f"{tmp}/list.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
cmd = ["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{tmp}/list.txt"]
if A.audio:
    a0 = T0 + HEAD                      # file time of the first frame
    if a0 >= 0: cmd += ["-ss", f"{a0:.3f}", "-i", A.audio]
    else: cmd += ["-i", A.audio]
    filt = f"adelay={int(round(-a0 * 1000))}:all=1," if a0 < 0 else ""
    filt += f"afade=t=in:d=0.8,afade=t=out:st={dur - 1.5:.2f}:d=1.5" if A.bars else "anull"
    cmd += ["-map", "0:v", "-map", "1:a", "-af", filt, "-c:a", "aac", "-b:a", "320k"]
cmd += ["-c:v", "copy", "-movflags", "+faststart", "-t", f"{dur:.3f}", A.out]
subprocess.run(cmd, check=True)
for p in parts: os.remove(p)
os.remove(f"{tmp}/list.txt"); os.rmdir(tmp)
print("done", A.out, f"{dur:.1f}s")
