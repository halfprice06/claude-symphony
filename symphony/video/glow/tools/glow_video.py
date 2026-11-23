"""Glowing-score video: the engraved score as one long line on a dark sheet, seen at an angle by a moving camera;
each note lights up in its part's colour while it sounds (after the look of Gilmar Araújo's animated scores).

python3 glow_video.py --strip BUILD --tempo data/<mvt>-tempo.json --audio mockup.mp3 [--stems data/<mvt>-stems.npz]
                      --out out.mp4 [--bars 53 64] [--still T ...] [--jobs 4]

--tempo: {"tempo": [[qn, bpm], ...], "head_s": s}; the tempo map REAPER played; head_s is the audio before score qn 0.
--stems: 20 Hz loudness of each mockup stem; the camera looks at the staves that are loudest (without it, at the
         staves with the most onsets).
--jobs N renders N parts of the video in parallel processes and joins them; the frames are the same as one process makes.
"""
import argparse, json, math, re, subprocess, sys, os, tempfile
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
ap.add_argument("--fps", type=int, default=30)
ap.add_argument("--still", type=float, nargs="*")
ap.add_argument("--env", help="audio file for the loudness envelope (default: --audio)")
ap.add_argument("--jobs", type=int, default=1)
ap.add_argument("--part", type=int, nargs=2, help=argparse.SUPPRESS)      # first and last frame (internal, --jobs)
ap.add_argument("--focus-report", action="store_true", help="print the staff the camera follows, bar by bar, and stop")
A = ap.parse_args()
W, H = 1920, 1080
CHILD = A.part is not None
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
        notes.append((float(attr["m"]), float(attr.get("d", 0)), pts[0][0] * k, pts[0][1] * k))
names = sorted(staves, key=lambda n: staves[n][0])
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
for q, d, x, y in notes:
    st = staff_of(y)
    t0, t1 = q2s(q), q2s(q + max(d, 0.25))
    N.append((t0, t1, x + 0.65 * sp, y, np.array(COL.get(st, (255, 255, 255)), np.float32), st))
N.sort(key=lambda n: n[0])
# bouncing lights: per part, up to 3 balls hop from each onset's notes to the next onset's notes
from collections import defaultdict
_G = defaultdict(dict)
for t0, t1, x, y, c, st in N: _G[st].setdefault(round(t0, 4), []).append((x, y, t1))
TRACKS = []
for st, dct in _G.items():
    ts = sorted(dct); groups = [sorted(dct[t], key=lambda p: p[1]) for t in ts]
    nb = min(max(len(g) for g in groups), 3)
    TRACKS.append((np.array(ts), groups, np.array(COL.get(st, (255, 255, 255)), np.float32), nb))
DROP = 0.55
def balls_at(t):
    """(x, y, z, alpha, colour) of every ball at time t"""
    out = []
    for ts, groups, col, nb in TRACKS:
        i = int(np.searchsorted(ts, t, side="right")) - 1
        for j in range(nb):
            if i < 0:
                if ts[0] - t < DROP:
                    q = groups[0][min(j, len(groups[0]) - 1)]; s_ = (ts[0] - t) / DROP
                    out.append((q[0], q[1], 260 * s_ * s_, 1 - s_, col))
                continue
            g = groups[i]; p_ = g[min(j, len(g) - 1)]; end = max(n[2] for n in g)
            if i + 1 < len(ts):
                nt = ts[i + 1]; q = groups[i + 1][min(j, len(groups[i + 1]) - 1)]
                gap = nt - ts[i]
                resting = (nt - end) > 0.9          # a real rest: the light goes out, then drops onto the next note
                if not resting:
                    hop = min(gap, 0.75); st_ = nt - hop
                    if t >= st_:
                        s_ = (t - st_) / hop
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
    return out
NT0 = np.array([n[0] for n in N]); NT1 = np.array([n[1] for n in N])
NX = np.array([n[2] for n in N]); NY = np.array([n[3] for n in N])
NC = np.array([n[4] for n in N])
# playhead x per qn (leftmost head at each onset)
on = {}
for q, d, x, y in notes: on[q] = min(on.get(q, 1e9), x)
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
# score, and its highest peak. A new peak takes over only when it is clearly stronger (x1.5) than the one being
# followed, so the camera does not swing between two groups of similar weight.
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
DWELL = 3.0      # seconds the camera stays with a group of staves before it may switch to another
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
        if cur is None: cur = best
        else:
            # follow the peak being watched as it drifts; switch only to a clearly stronger one, and not too often
            lo_, hi_ = max(cur - 30, 0), min(cur + 31, len(vs))
            cur = lo_ + int(d[lo_:hi_].argmax())
            if d[best] > 1.5 * d[cur] and (i - since) >= DWELL * FOCUS_SR: cur = best; since = i
        out[i] = vs[cur]
    return out
FOCUS = focus_track()
def feat_v(t):
    return float(FOCUS[int(np.clip(t * FOCUS_SR, 0, len(FOCUS) - 1))])
if A.focus_report:
    bq = bar_qn
    for b in range(1, len(bq)):
        t = q2s(bq[b - 1]); v = feat_v(t + 1.0)
        print(f"bar {b:3d} {t:6.1f}s  {min(names, key=lambda s_: abs(stave_mid[s_] - v))}")
    sys.exit()

# ---------- camera ----------
FOC = 2600.0
CAM = dict(az=45.0, el=38.0, roll=12.0, d=1450.0)
if os.environ.get("CAM"): CAM.update(json.loads(os.environ["CAM"]))
def camera(tu, tv, t):
    """3D camera over the sheet (z up out of the paper), behind-left of the focus, looking up the page and along the line"""
    az = math.radians(CAM["az"] + 2.0 * math.sin(t / 23.0))
    el = math.radians(CAM["el"] + 1.5 * math.sin(t / 19.0))
    d = CAM["d"] + 50 * math.sin(t / 31.0)
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
        return np.stack([W * 0.5 + cr * x - sr * y, H * 0.55 + sr * x + cr * y], 1), z
    src = np.float32([[tu - 400, tv - 400], [tu + 400, tv - 400], [tu + 400, tv + 400], [tu - 400, tv + 400]])
    dst, _ = proj3(np.c_[src, np.zeros(4)])
    return cv2.getPerspectiveTransform(src, dst.astype(np.float32)), proj3

state = {"u": None, "v": None}
def step(t, dt):
    """move the camera's focus for the frame at time t (smoothed: 0.9 s along the line, 2.5 s up and down)"""
    tu = play_x(s2q(max(t + 0.6, 0))) + 120
    tv = feat_v(t + 1.0)
    if state["u"] is None: state["u"], state["v"] = tu, tv
    state["u"] += (tu - state["u"]) * (1 - math.exp(-dt / 0.9))
    state["v"] += (tv - state["v"]) * (1 - math.exp(-dt / 2.5))

_gr = np.random.default_rng(7)
GRAIN = [(_gr.normal(0, 1.0, (H, W, 1))).astype(np.float32) for _ in range(8)]
def frame_at(t, dt):
    step(t, dt)
    Hm, proj3 = camera(state["u"], state["v"], t)
    # crop the flat sheet to what the camera can see
    Hi = np.linalg.inv(Hm)
    cs = cv2.perspectiveTransform(np.float32([[[0, 0], [W, 0], [W, H], [0, H], [W / 2, 0]]]), Hi)[0]
    u0 = int(max(0, min(state["u"] - 5000, cs[:, 0].min()))); u1 = int(min(FW, max(cs[:, 0].max(), 0)))
    u0 = max(u0, int(state["u"] - 7000)); u1 = min(u1, int(state["u"] + 7000))
    if u1 <= u0 + 10: u0, u1 = 0, min(FW, 14000)
    Tm = np.array([[1, 0, u0], [0, 1, 0], [0, 0, 1]], np.float64)
    img = cv2.warpPerspective(flat[:, u0:u1], Hm @ Tm, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(10, 10, 12)).astype(np.float32)
    # lighting: dim the sheet away from the playing area
    fx, fy = cv2.perspectiveTransform(np.float32([[[state["u"], state["v"]]]]), Hm)[0, 0]
    yy, xx = np.mgrid[0:H:8, 0:W:8]
    fall = np.exp(-(((xx - fx) / 1500) ** 2 + ((yy - fy) / 900) ** 2)).astype(np.float32)
    fall = cv2.resize(0.45 + 0.45 * fall, (W, H))
    img *= fall[..., None]
    # depth of field: soften far from the focus
    blur = cv2.GaussianBlur(img, (0, 0), 3.0)
    dm = cv2.resize(np.clip((np.abs(yy - fy) / 520) ** 1.5 + (np.abs(xx - fx) / 1500) ** 2, 0, 1).astype(np.float32), (W, H))
    img = img * (1 - dm[..., None]) + blur * dm[..., None]
    # notes lit now
    lo = np.searchsorted(NT0, t - 40); hi = np.searchsorted(NT0, t + 0.001)
    idx = np.arange(lo, hi)
    idx = idx[(NT1[idx] + 30 > t)]
    glow = np.zeros((H, W, 3), np.float32)
    if len(idx):
        age = t - NT0[idx]
        held = t <= NT1[idx]
        inten = np.where(held, 0.7 + 0.3 * np.exp(-age / 0.35), 0.7 * (0.55 + 0.45 * np.exp(-(t - NT1[idx]) / 1.5)) * np.exp(-(t - NT1[idx]) / 14.0))
        inten *= np.clip(age / 0.04, 0, 1)
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
            if age[j] < 0.3:   # a thin ring spreads out from the note as it is struck
                s_ = age[j] / 0.3; rk = 1.3 + 1.6 * s_
                cv2.ellipse(glow, (int(x * 4), int(y * 4)), (max(1, int(ax * 4 * rk)), max(1, int(ay * 4 * rk))), ang, 0, 360, (NC[idx[j]] * 0.55 * (1 - s_) ** 2).tolist(), 3, cv2.LINE_AA, 2)
    # the bouncing lights
    bl_ = balls_at(t)
    if bl_:
        B = np.array([[b[0], b[1] - top, b[2]] for b in bl_], np.float64)
        sc, dep = proj3(B)
        gp, _ = proj3(np.c_[B[:, :2], np.zeros(len(B))])
        # motion trail: where each airborne ball was over the last few frames
        for kt in range(1, 7):
            tb = [b for b in balls_at(t - kt * 0.018) if b[2] > 3]
            if not tb: continue
            TB = np.array([[b[0], b[1] - top, b[2]] for b in tb], np.float64)
            tsc, tdep = proj3(TB)
            for (x_, y_, z_, al, col), (sx, sy), dz in zip(tb, tsc, tdep):
                if dz <= 300: continue
                rr = FOC * 0.42 * sp / dz * (1 - kt * 0.1)
                cv2.circle(glow, (int(sx * 4), int(sy * 4)), max(2, int(rr * 4)), (np.array(col, np.float32) * al * 0.5 * (1 - kt / 7)).tolist(), -1, cv2.LINE_AA, 2)
        for (x_, y_, z_, al, col), (sx, sy), dz, (gx, gy) in zip(bl_, sc, dep, gp):
            if al <= 0.01 or dz <= 300: continue    # a ball at or behind the camera (a long note's head) would cover the frame
            rr = FOC * 0.42 * sp / dz
            c = np.array(col, np.float32)
            if z_ > 4:   # a pool of light on the paper under the ball, fainter the higher it flies
                pa = al * 0.5 * max(0.0, 1 - z_ / 260)
                cv2.ellipse(glow, (int(gx * 4), int(gy * 4)), (int(rr * 4 * 2.2), int(rr * 4 * 1.1)), CAM["roll"], 0, 360, (c * pa).tolist(), -1, cv2.LINE_AA, 2)
            cv2.circle(glow, (int(sx * 4), int(sy * 4)), max(2, int(rr * 4)), (np.minimum(255, c * 0.55 + 140) * al * 1.25).tolist(), -1, cv2.LINE_AA, 2)
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
    # vignette
    out *= cv2.resize(np.clip(1.15 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2), 0, 1).astype(np.float32), (W, H))[..., None]
    out += GRAIN[int(t * 30) % len(GRAIN)]   # fine film grain so the dark sheet doesn't band
    return np.clip(out, 0, 255).astype(np.uint8)

if A.bars:
    T0 = q2s(bar_qn[A.bars[0] - 1]) - 1.5; T1 = q2s(bar_qn[A.bars[1]]) + 1.0
else:
    T0, T1 = -2.0, q2s(END_QN) + 7.0

if A.still:
    for t in A.still:
        state["u"] = None
        for kk in range(45, 0, -1): step(t - kk / A.fps, 1 / A.fps)
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
