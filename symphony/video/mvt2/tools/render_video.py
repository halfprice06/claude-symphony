"""Render the movement II score video.

python3 render_video.py --build build --tempo parts.json|score.midi --audio mockup.mp3 --out video.mp4 [--offset S] [--start S --dur S]

The audio's time 0 is score qn 0 (the mockup pipeline cuts its pre-roll off); --offset shifts the score against the audio.
"""
import argparse, json, subprocess, sys, os, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from features import FEATURES, BREAKS

ap = argparse.ArgumentParser()
ap.add_argument("--build", default="build")
ap.add_argument("--tempo", required=True)
ap.add_argument("--audio")
ap.add_argument("--out", required=True)
ap.add_argument("--offset", type=float, default=0.0)
ap.add_argument("--fps", type=int, default=30)
ap.add_argument("--start", type=float, default=0.0)
ap.add_argument("--dur", type=float)
ap.add_argument("--still", type=float, nargs="*", help="write PNG stills at these video times instead")
ap.add_argument("--sections", help="sections.txt of the engraved version (default: BUILD/sections.txt)")
A = ap.parse_args()
A.sections = A.sections or f"{A.build}/sections.txt"

W, H = 1920, 1080
VW = 1660                      # score viewport width; the panel takes the rest
PW = W - VW
INTRO, OUTRO = 4.0, 5.0
PAPER = np.array([246, 241, 230], np.float32)
PANEL = (34, 30, 27)
CREAM = (238, 230, 214)
DIM = (160, 150, 136)
RED = (176, 23, 51)
BLUE = (26, 92, 158)
TINT = {"p": np.array([250, 214, 214], np.float32), "s": np.array([212, 228, 248], np.float32)}
FONT = "/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-"
def font(kind, size): return ImageFont.truetype(FONT + kind + ".otf", size)

# ---------- score time ----------
bars = []
for line in open(A.sections):
    p = line.split()
    if len(p) >= 3: bars += [int(p[2])] * int(p[1])
bar_qn = [0.0]
for b in bars: bar_qn.append(bar_qn[-1] + b)          # bar_qn[k-1] = start of bar k
END_QN = bar_qn[-1]
def bar_at(q):
    for k in range(len(bars), 0, -1):
        if q >= bar_qn[k - 1] - 1e-6: return k
    return 1

if A.tempo.endswith(".json"):
    steps = [tuple(x) for x in json.load(open(A.tempo))["tempo"]]
else:
    import mido
    mf = mido.MidiFile(A.tempo); tpb = mf.ticks_per_beat; steps = []
    for tr in mf.tracks:
        t = 0
        for m in tr:
            t += m.time
            if m.type == "set_tempo": steps.append((t / tpb, mido.tempo2bpm(m.tempo)))
    steps = sorted(set(steps))
if steps[0][0] > 0: steps.insert(0, (0.0, steps[0][1]))
def qn_to_sec(q):
    t, lq, lb = 0.0, 0.0, steps[0][1]
    for tq, bpm in steps[1:]:
        if tq >= q: break
        t += (tq - lq) * 60 / lb; lq, lb = tq, bpm
    return t + (q - lq) * 60 / lb
grid = np.linspace(0, END_QN + 8, 40000)
grid_t = np.array([qn_to_sec(q) for q in grid])
def sec_to_qn(t): return float(np.interp(t, grid_t, grid))
MUSIC_END = qn_to_sec(END_QN)

audio_len = None
if A.audio:
    audio_len = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", A.audio]))
TOTAL = INTRO + max(MUSIC_END + 3.0, (audio_len or 0) + A.offset) + OUTRO

# ---------- systems ----------
L = json.load(open(f"{A.build}/layout.json"))
assert len(L) == len(BREAKS), (len(L), len(BREAKS))
sys_qn = [bar_qn[b - 1] for b in BREAKS] + [END_QN]
CROP_X0 = 40
systems = []
for i, s in enumerate(L):
    img = Image.open(f"{A.build}/{s['png']}").convert("RGB")
    x1 = min(img.size[0], int(s["right"]) + 40)
    y0 = max(0, int(s["top"]) - 230); y1 = min(img.size[1], int(s["bottom"]) + 170)
    sc = VW / (x1 - CROP_X0)
    im = img.crop((CROP_X0, y0, x1, y1))
    im = im.resize((VW, round((y1 - y0) * sc)), Image.LANCZOS)
    ink = np.asarray(im, np.float32) / 255.0
    def X(x, sc=sc): return (x - CROP_X0) * sc
    def Y(y, sc=sc, y0=y0): return (y - y0) * sc
    staves = {n: (X(v[0]), X(v[1]), Y(v[2]), Y(v[3])) for n, v in s["staves"].items()}
    q0, q1 = sys_qn[i], sys_qn[i + 1]
    cols = [(q, X(x) + 11) for q, x in s["cols"] if q0 - 1e-6 <= q < q1 - 1e-6]
    endbar = [X(x) for q, x in s["bars"] if abs(q - q1) < 1e-6]
    end_x = endbar[0] if endbar else X(s["right"])
    cols.append((q1, end_x))
    # x of each bar's start in this system (for highlight bands)
    bx = {}
    for k in range(BREAKS[i], (BREAKS[i + 1] if i + 1 < len(BREAKS) else len(bars) + 1)):
        q = bar_qn[k - 1]
        bl = [X(x) for qq, x in s["bars"] if abs(qq - q) < 1e-6]
        bx[k] = bl[0] if (bl and k != BREAKS[i]) else cols[0][1] - 30
    bx["end"] = end_x
    systems.append(dict(ink=ink, h=ink.shape[0], staves=staves, cols=cols, bx=bx, q0=q0, q1=q1,
                        first=BREAKS[i], spacing=(staves[next(iter(staves))][3] - staves[next(iter(staves))][2]) / 4))

def sys_at(q):
    for i in range(len(systems) - 1, -1, -1):
        if q >= systems[i]["q0"] - 1e-6: return i
    return 0

def play_x(S, q):
    c = S["cols"]
    if q <= c[0][0]: return c[0][1]
    for (qa, xa), (qb, xb) in zip(c, c[1:]):
        if qa <= q <= qb: return xa + (xb - xa) * (q - qa) / max(qb - qa, 1e-9)
    return c[-1][1]

def feature_of(bar):
    for f in FEATURES:
        if f[0] <= bar <= f[1]: return f
    return None

def bands(S):
    """highlight rectangles in this system: (x0, x1, y0, y1, role, first bar, last bar)"""
    out = []
    last = max(k for k in S["bx"] if k != "end")
    sp = S["spacing"]
    for a, b, lines, _ in FEATURES:
        lo, hi = max(a, S["first"]), min(b, last)
        if lo > hi: continue
        for st, r in lines:
            if st not in S["staves"]: continue
            x0 = S["bx"][lo]; x1 = S["bx"][hi + 1] if hi + 1 in S["bx"] else S["bx"]["end"]
            v = S["staves"][st]
            out.append((x0, x1, v[2] - 1.6 * sp, v[3] + 1.6 * sp, r, lo, hi))
    return out
for S in systems: S["bands"] = bands(S)

def target_y(S, q):
    """camera top (system px) that centres the featured staves at score time q"""
    vh = H
    if S["h"] <= vh: return (S["h"] - vh) / 2
    f = feature_of(bar_at(min(q, END_QN - 1e-3)))
    ys = []
    if f:
        for role in ("p", "s"):
            yy = [S["staves"][st][2:] for st, r in f[2] if r == role and st in S["staves"]]
            if yy: ys.append((min(y[0] for y in yy), max(y[1] for y in yy)))
    if not ys:
        c = S["h"] / 2
    else:
        lo, hi = min(y[0] for y in ys), max(y[1] for y in ys)
        if hi - lo > vh - 200: lo, hi = ys[0]            # too wide: the main line wins
        c = (lo + hi) / 2
    return min(max(c - vh / 2, 0), S["h"] - vh)

# ---------- panel ----------
MARKS = {7: "A", 15: "B", 23: "C", 37: "D", 45: "E", 53: "F", 61: "G", 65: "H", 71: "J", 83: "K"}
TEMPI = [(1, "Adagio"), (35, "poco rit."), (37, "Poco più mosso"), (47, "poco rit."), (48, "poco sostenuto"),
         (53, "a tempo, poco a poco animando"), (60, "poco allargando"), (61, "Largamente"), (64, "allargando"),
         (65, "Tempo I"), (78, "poco allargando"), (83, "a tempo"), (89, "rit.")]
SHORT = {"Violins I": "Violins I", "Violins II": "Violins II", "Violoncellos": "Cellos", "Horns 1·2": "Horn 1",
         "Horns 3·4": "Horn 3", "Oboes 1·2": "Oboe 1", "Flutes 1·2": "Flute 1", "Cor anglais": "Cor anglais",
         "Bass clarinet": "Bass clarinet", "Trombones 1·2": "Trombone 1", "Harp RH": "Harp", "Timpani": "Timpani",
         "Clarinets 1·2": "Clarinet 1"}

def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= width: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

F_SMALL, F_TITLE, F_BAR, F_TXT, F_ITAL, F_MARK = font("regular", 19), font("italic", 40), font("regular", 64), font("regular", 23), font("italic", 23), font("bold", 30)
panel_cache = {}
def panel(bar, sidx):
    key = (bar, sidx)
    if key in panel_cache: return panel_cache[key]
    im = Image.new("RGB", (PW, H), PANEL); d = ImageDraw.Draw(im)
    x = 24; w = PW - 2 * x
    d.text((x, 30), "SYMPHONY No. 1", font=F_SMALL, fill=DIM)
    d.text((x, 52), "IN C MINOR", font=F_SMALL, fill=DIM)
    d.text((x, 76), "II. Adagio", font=F_TITLE, fill=CREAM)
    d.line((x, 132, PW - x, 132), fill=(80, 72, 64), width=1)
    d.text((x, 146), "BAR", font=F_SMALL, fill=DIM)
    d.text((x, 166), str(bar), font=F_BAR, fill=CREAM)
    mk = max([k for k in MARKS if k <= bar], default=None)
    if mk:
        bw = 52; bx0 = PW - x - bw
        d.rectangle((bx0, 176, bx0 + bw, 176 + bw), outline=CREAM, width=2)
        d.text((bx0 + bw / 2, 176 + bw / 2 + 1), MARKS[mk], font=F_MARK, fill=CREAM, anchor="mm")
    tp = [t for k, t in TEMPI if k <= bar][-1]
    y = 252
    for ln in wrap(d, tp, F_ITAL, w):
        d.text((x, y), ln, font=F_ITAL, fill=CREAM); y += 30
    y += 14
    d.line((x, y, PW - x, y), fill=(80, 72, 64), width=1); y += 22
    f = feature_of(bar)
    if f:
        for ln in wrap(d, f[3], F_TXT, w):
            d.text((x, y), ln, font=F_TXT, fill=CREAM); y += 31
        y += 14
        for st, r in f[2]:
            col = RED if r == "p" else BLUE
            d.rounded_rectangle((x, y + 6, x + 16, y + 22), 3, fill=col)
            d.text((x + 28, y), SHORT.get(st, st), font=F_SMALL, fill=CREAM)
            y += 30
        if any(r == "s" for _, r in f[2]):
            y += 8
            d.rounded_rectangle((x, y + 6, x + 16, y + 22), 3, fill=RED); d.text((x + 28, y), "melody", font=F_SMALL, fill=DIM)
            d.rounded_rectangle((x + 112, y + 6, x + 128, y + 22), 3, fill=BLUE); d.text((x + 140, y), "counter", font=F_SMALL, fill=DIM)
    panel_cache[key] = np.asarray(im, np.uint8)
    return panel_cache[key]

def minimap(frame, S, cam):
    """thumbnail of the whole system with the visible window, at the bottom of the panel"""
    if S["h"] <= H: return
    tw = PW - 48; sc = tw / VW; th = int(S["h"] * sc)
    if "thumb" not in S:
        t = Image.fromarray((S["ink"] * 255).astype(np.uint8)).resize((tw, th), Image.BILINEAR)
        S["thumb"] = np.asarray(t, np.float32) / 255.0
    y0 = H - 70 - th; x0 = VW + 24
    base = np.empty((th, tw, 3), np.float32); base[:] = PAPER
    for bx0, bx1, by0, by1, r, lo, hi in S["bands"]:
        base[max(0, int(by0 * sc)):int(by1 * sc), max(0, int(bx0 * sc)):int(bx1 * sc)] = TINT[r]
    frame[y0:y0 + th, x0:x0 + tw] = (base * S["thumb"]).astype(np.uint8)
    vy0 = y0 + int(cam * sc); vy1 = vy0 + int(H * sc)
    for yy in (vy0, vy1 - 1):
        frame[max(yy - 1, y0):yy + 1, x0:x0 + tw] = RED
    frame[vy0:vy1, x0:x0 + 2] = RED; frame[vy0:vy1, x0 + tw - 2:x0 + tw] = RED

def progress(frame, t):
    x0, x1, y = VW + 24, W - 24, H - 34
    frame[y:y + 3, x0:x1] = (80, 72, 64)
    p = min(max((t - INTRO) / max(MUSIC_END, 1), 0), 1)
    frame[y:y + 3, x0:x0 + int((x1 - x0) * p)] = CREAM

# ---------- frames ----------
def score_view(i, cam, q, alpha_active=True):
    S = systems[i]
    top = int(round(cam))
    base = np.empty((H, VW, 3), np.float32); base[:] = PAPER
    ink = np.ones((H, VW, 3), np.float32)
    a, b = max(top, 0), min(top + H, S["h"])
    if b > a: ink[a - top:b - top] = S["ink"][a:b]
    bar = bar_at(q)
    for bx0, bx1, by0, by1, r, lo, hi in S["bands"]:
        active = lo <= bar <= hi
        al = 0.85 if active else 0.35
        ya, yb = int(by0) - top, int(by1) - top
        ya, yb = max(ya, 0), min(yb, H)
        xa, xb = max(int(bx0), 0), min(int(bx1), VW)
        if yb > ya and xb > xa:
            base[ya:yb, xa:xb] = PAPER * (1 - al) + TINT[r] * al
    img = base * ink
    if S["q0"] - 1e-6 <= q <= S["q1"] + 1e-6:
        x = int(play_x(S, q))
        sys_top, sys_bot = max(int(S["staves_top"]) - top, 0), min(int(S["staves_bot"]) - top, H)
        img[sys_top:sys_bot, max(x - 5, 0):x + 5] = img[sys_top:sys_bot, max(x - 5, 0):x + 5] * 0.82 + np.array(RED, np.float32) * 0.18
        img[sys_top:sys_bot, max(x - 1, 0):x + 1] = img[sys_top:sys_bot, max(x - 1, 0):x + 1] * 0.35 + np.array(RED, np.float32) * 0.65
    return img

for S in systems:
    S["staves_top"] = min(v[2] for v in S["staves"].values()) - 30
    S["staves_bot"] = max(v[3] for v in S["staves"].values()) + 30

title_bg = Image.new("RGB", (W, H), PANEL); d = ImageDraw.Draw(title_bg)
d.text((W / 2, 420), "SYMPHONY No. 1 IN C MINOR", font=font("regular", 34), fill=DIM, anchor="mm")
d.text((W / 2, 500), "II. Adagio", font=font("italic", 96), fill=CREAM, anchor="mm")
d.text((W / 2, 600), "Score and orchestral mockup", font=font("regular", 30), fill=DIM, anchor="mm")
TITLE = np.asarray(title_bg, np.float32)

TRANS = 0.45   # system change crossfade (s), centred slightly before the new system's first beat
cam_state = {"i": None, "y": 0.0}
def frame_at(t, dt):
    tm = t - INTRO - A.offset
    q = sec_to_qn(max(tm, 0))
    i = sys_at(q)
    S = systems[i]
    # camera: follow the featured lines 0.8 s ahead, smoothed
    tgt = target_y(S, sec_to_qn(max(tm + 0.8, 0)))
    if cam_state["i"] != i:
        cam_state["i"] = i; cam_state["y"] = target_y(S, q)
    else:
        k = 1 - math.exp(-dt / 0.7)
        cam_state["y"] += (tgt - cam_state["y"]) * k
    img = score_view(i, cam_state["y"], q)
    # crossfade into the next system
    if i + 1 < len(systems):
        tn = qn_to_sec(systems[i + 1]["q0"])
        if tn - TRANS * 0.6 <= tm < tn:
            u = (tm - (tn - TRANS * 0.6)) / (TRANS * 0.6)
            nxt = score_view(i + 1, target_y(systems[i + 1], systems[i + 1]["q0"]), systems[i + 1]["q0"] - 1)
            img = img * (1 - u) + nxt * u
    frame = np.empty((H, W, 3), np.uint8)
    frame[:, :VW] = np.clip(img, 0, 255).astype(np.uint8)
    frame[:, VW:] = panel(bar_at(min(q, END_QN - 1e-3)), i)
    minimap(frame, S, cam_state["y"])
    progress(frame, t)
    frame[:, VW:VW + 1] = (20, 18, 16)
    # title in, title out
    if t < INTRO:
        u = min(max((t - (INTRO - 1.0)) / 1.0, 0), 1)
        frame = (TITLE * (1 - u) + frame * u).astype(np.uint8)
    elif t > TOTAL - 2.5:
        u = min((t - (TOTAL - 2.5)) / 2.0, 1)
        frame = (frame * (1 - u) + TITLE * u).astype(np.uint8)
    return frame

if A.still:
    for t in A.still:
        cam_state["i"] = None
        for k in range(30, 0, -1): frame_at(t - k / A.fps, 1 / A.fps)
        Image.fromarray(frame_at(t, 1 / A.fps)).save(f"{A.out}-{t:07.2f}.png")
    sys.exit()

dur = A.dur if A.dur else TOTAL - A.start
cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(A.fps), "-i", "-"]
if A.audio:
    delay = INTRO + A.offset - A.start
    if delay >= 0:
        cmd += ["-i", A.audio, "-filter_complex", f"[1:a]adelay={int(delay*1000)}:all=1,apad[a]", "-map", "0:v", "-map", "[a]"]
    else:
        cmd += ["-ss", str(-delay), "-i", A.audio, "-filter_complex", "[1:a]apad[a]", "-map", "0:v", "-map", "[a]"]
    cmd += ["-c:a", "aac", "-b:a", "320k", "-ar", "48000"]
cmd += ["-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-tune", "stillimage", "-movflags", "+faststart", "-t", f"{dur:.3f}", A.out]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
n = int(dur * A.fps)
for f in range(n):
    t = A.start + f / A.fps
    pr.stdin.write(frame_at(t, 1 / A.fps).tobytes())
    if f % 300 == 0: print(f"{f}/{n}", file=sys.stderr, flush=True)
pr.stdin.close(); pr.wait()
print("done", A.out, f"{dur:.1f}s")
