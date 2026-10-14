"""Glowing-score video: the engraved score as one long line on a dark sheet, seen at an angle by a moving camera;
each note lights up in its part's colour while it sounds (after the look of Gilmar Araújo's animated scores).

python3 glow_video.py --strip strip/b --tempo parts.json --audio mockup.mp3 --out out.mp4 [--bars 53 64] [--still T ...]
"""
import argparse, json, math, re, subprocess, sys, os
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import FEATURES

ap = argparse.ArgumentParser()
ap.add_argument("--strip", required=True)
ap.add_argument("--tempo", required=True)
ap.add_argument("--audio")
ap.add_argument("--out", required=True)
ap.add_argument("--bars", type=int, nargs=2)
ap.add_argument("--fps", type=int, default=30)
ap.add_argument("--still", type=float, nargs="*")
ap.add_argument("--env", help="audio file for the loudness envelope (default: --audio)")
A = ap.parse_args()
W, H = 1920, 1080

# ---------- time ----------
bars = []
for line in open(f"{A.strip}/sections.txt"):
    p = line.split()
    if len(p) >= 3: bars += [int(p[2])] * int(p[1])
bar_qn = np.concatenate([[0], np.cumsum(bars)]).astype(float)
END_QN = bar_qn[-1]
steps = [tuple(x) for x in json.load(open(A.tempo))["tempo"]]
def q2s(q):
    t, lq, lb = 0.0, 0.0, steps[0][1]
    for tq, b in steps[1:]:
        if tq >= q: break
        t += (tq - lq) * 60 / lb; lq, lb = tq, b
    return t + (q - lq) * 60 / lb
gq = np.linspace(0, END_QN + 4, 30000); gt = np.array([q2s(q) for q in gq])
def s2q(t): return float(np.interp(t, gt, gq))
def bar_at(q): return int(np.searchsorted(bar_qn, q + 1e-6, side="right"))

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
    if ENV is None or t < 0: return 0.5
    return float(ENV[min(int(t * ENV_SR), len(ENV) - 1)])

# ---------- layout from the SVG ----------
svg = open(f"{A.strip}/strip.svg").read()
vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
ink_img = Image.open(f"{A.strip}/strip2.png").convert("L")
k = ink_img.size[0] / vb[2]
tr = re.compile(r'translate\(([-\d.]+), ([-\d.]+)\)')
staves, notes = {}, []
for m in re.finditer(r'<g class="(\w+)"((?: data-[\w-]+="[^"]*")*)>', svg):
    cls, attr = m.group(1), dict(re.findall(r'data-([\w-]+)="([^"]*)"', m.group(2)))
    if cls not in ("st", "nh"): continue
    end = svg.find("</g>\n</g>", m.end()) if cls == "nh" else svg.find('<g class=', m.end())
    body = svg[m.end():end if end > 0 else m.end() + 4000]
    pts = [(float(x), float(y)) for x, y in tr.findall(body)]
    if not pts: continue
    if cls == "st":
        ys = sorted(y for _, y in pts[:5])
        staves[attr["name"]] = (ys[0] * k, ys[-1] * k)
    else:
        notes.append((float(attr["m"]), float(attr.get("d", 0)), pts[0][0] * k, pts[0][1] * k))
names = sorted(staves, key=lambda n: staves[n][0])
sp = (staves[names[0]][1] - staves[names[0]][0]) / 4          # staff space in px
def staff_of(y):
    best = min(names, key=lambda n: max(staves[n][0] - y, y - staves[n][1], 0))
    return best
COL = {  # per part, LED-like colours (RGB)
    "Flutes 1·2": (120, 200, 255), "Oboes 1·2": (190, 255, 120), "Cor anglais": (230, 255, 140),
    "Clarinets 1·2": (255, 130, 220), "Bass clarinet": (220, 110, 255), "Bassoons 1·2": (255, 170, 80),
    "Contrabassoon": (255, 140, 60), "Horns 1·2": (255, 210, 120), "Horns 3·4": (255, 190, 100),
    "Trombones 1·2": (255, 80, 70), "Bass trombone": (255, 70, 90), "Tuba": (240, 90, 60),
    "Timpani": (255, 255, 255), "Harp RH": (110, 255, 230), "Harp LH": (90, 230, 255),
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

# ---------- flat sheet ----------
top = int(min(v[0] for v in staves.values()) - 14 * sp); bot = int(max(v[1] for v in staves.values()) + 10 * sp)
ink = np.asarray(ink_img, np.float32)[max(top, 0):bot] / 255.0   # 1 = paper, 0 = ink
NY = NY - max(top, 0)
FH, FW = ink.shape
PAPER = np.array([98, 101, 112], np.float32); INK = np.array([18, 19, 24], np.float32)
# paper texture: a slow brightness variation so the sheet reads as a surface
rng = np.random.default_rng(3)
tex = cv2.resize(rng.normal(0, 1, (FH // 64 + 2, FW // 64 + 2)).astype(np.float32), (FW, FH), interpolation=cv2.INTER_CUBIC)
paper = PAPER[None, None, :] * (1 + 0.035 * tex[..., None])
flat = (paper * ink[..., None] + INK * (1 - ink[..., None])).clip(0, 255).astype(np.uint8)
del paper, tex

stave_mid = {n: (staves[n][0] + staves[n][1]) / 2 - max(top, 0) for n in names}
V_ALL = (stave_mid[names[0]] + stave_mid[names[-1]]) / 2

def feat_v(bar):
    for a, b, lines, _ in FEATURES:
        if a <= bar <= b:
            vs = [stave_mid[s] for s, r in lines if s in stave_mid and r == "p"]
            if vs: return float(np.mean(vs))
    return V_ALL

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
_gr = np.random.default_rng(7)
GRAIN = [(_gr.normal(0, 1.0, (H, W, 1))).astype(np.float32) for _ in range(8)]
def frame_at(t, dt):
    q = s2q(max(t, 0))
    tu = play_x(s2q(max(t + 0.6, 0))) + 120
    tv = feat_v(bar_at(s2q(t + 1.0)))
    if state["u"] is None: state["u"], state["v"] = tu, tv
    state["u"] += (tu - state["u"]) * (1 - math.exp(-dt / 0.9))
    state["v"] += (tv - state["v"]) * (1 - math.exp(-dt / 2.5))
    Hm, proj3 = camera(state["u"], state["v"], t)
    # crop the flat sheet to what the camera can see
    Hi = np.linalg.inv(Hm)
    cs = cv2.perspectiveTransform(np.float32([[[0, 0], [W, 0], [W, H], [0, H], [W / 2, 0]]]), Hi)[0]
    u0 = int(max(0, min(state["u"] - 5000, cs[:, 0].min()))); u1 = int(min(FW, max(cs[:, 0].max(), 0)))
    u0 = max(u0, int(state["u"] - 7000)); u1 = min(u1, int(state["u"] + 7000))
    if u1 <= u0 + 10: u0, u1 = 0, FW
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
        for j in range(len(idx)):
            I = float(inten[j])
            if I < 0.02: continue
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
    bl = balls_at(t)
    if bl:
        B = np.array([[b[0], b[1] - max(top, 0), b[2]] for b in bl], np.float64)
        sc, dep = proj3(B)
        gp, _ = proj3(np.c_[B[:, :2], np.zeros(len(B))])
        # motion trail: where each airborne ball was over the last few frames
        for kt in range(1, 7):
            tb = [b for b in balls_at(t - kt * 0.018) if b[2] > 3]
            if not tb: continue
            TB = np.array([[b[0], b[1] - max(top, 0), b[2]] for b in tb], np.float64)
            tsc, tdep = proj3(TB)
            for (x_, y_, z_, al, col), (sx, sy), dz in zip(tb, tsc, tdep):
                if dz <= 10: continue
                rr = FOC * 0.42 * sp / dz * (1 - kt * 0.1)
                cv2.circle(glow, (int(sx * 4), int(sy * 4)), max(2, int(rr * 4)), (np.array(col, np.float32) * al * 0.5 * (1 - kt / 7)).tolist(), -1, cv2.LINE_AA, 2)
        for (x_, y_, z_, al, col), (sx, sy), dz, (gx, gy) in zip(bl, sc, dep, gp):
            if al <= 0.01 or dz <= 10: continue
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
        for kk in range(45, 0, -1): frame_at(t - kk / A.fps, 1 / A.fps)
        cv2.imwrite(f"{A.out}-{t:07.2f}.png", cv2.cvtColor(frame_at(t, 1 / A.fps), cv2.COLOR_RGB2BGR))
    sys.exit()

dur = T1 - T0
cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(A.fps), "-i", "-"]
if A.audio:
    if T0 >= 0: cmd += ["-ss", f"{T0:.3f}", "-i", A.audio, "-map", "0:v", "-map", "1:a"]
    else: cmd += ["-i", A.audio, "-filter_complex", f"[1:a]adelay={int(-T0*1000)}:all=1[a]", "-map", "0:v", "-map", "[a]"]
    cmd += ["-c:a", "aac", "-b:a", "320k", "-af", f"afade=t=in:d=0.8,afade=t=out:st={dur-1.5:.2f}:d=1.5"] if T0 >= 0 else ["-c:a", "aac", "-b:a", "320k"]
cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-t", f"{dur:.3f}", A.out]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
n = int(dur * A.fps)
for i in range(n):
    t = T0 + i / A.fps
    f = frame_at(t, 1 / A.fps)
    fade = min(1, (t - T0) / 0.8, (T1 - t) / 1.2)
    if fade < 1: f = (f * max(fade, 0)).astype(np.uint8)
    pr.stdin.write(f.tobytes())
    if i % 300 == 0: print(f"{i}/{n}", file=sys.stderr, flush=True)
pr.stdin.close(); pr.wait()
print("done", A.out, f"{dur:.1f}s")
