#!/usr/bin/env python3
"""Title screen and movement title cards for the joined video of the four glow videos.

  title_cards.py --spec cards/cards.json --out-dir DIR [--credits credits.json] [--stills]

Each card is a short video without sound, encoded like the parts of a movement video (libx264, preset slow, CRF 18,
yuv420p, 60 fps, 1920x1080), so that tools/join_videos.py can join cards and movements without encoding the pictures
again. A card starts and ends in black, as every movement video does.

The look: the opening page of the movement that follows (a frame of its video, one second in), out of focus and dim,
moving slowly towards the viewer; over it the words in the gold and the fonts of the labels on the score, with a soft
halo like the lit notes.

cards.json (page paths are relative to the file, or to --pages):
  {"title": {"file": "00-title", "page": "frames/mvt1-page.png", "seconds": 12,
             "title": "Symphony No. 1", "sub": "in C minor"},
   "movements": [{"file": "10-mvt1", "page": "frames/mvt1-page.png", "seconds": 5, "over": "SYMPHONY NO. 1 IN C MINOR",
                  "numeral": "I", "name": "", "tempo": "Lento — Allegro appassionato"}, ...]}
The credits under the title come from --credits, a JSON list [["ROLE", "Name", "detail or empty"], ...] (up to three
or four side by side). That file is not kept in the repository.

A movement's card can stay over the start of its movement instead of ending in black ("handover_cut": K, with
--video FILE=MOVEMENT.mp4): the card's last K frames lie over the movement's first K frames, so the music starts
behind the card. Its background is then the movement's own picture, out of focus and dim; near the end it comes into
focus, the words go, and the card's last frames are the movement's frames K-10 to K-1. join_videos.py then takes the
movement from frame K on ("MOVEMENT.mp4@K"), which must be a key frame, and lets its sound start K frames earlier.
A page is one frame of the movement's video, one second in (before the music starts):
  ffmpeg -ss 1 -i mvt1-glow-video.mp4 -frames:v 1 frames/mvt1-page.png
"""
import argparse, json, os, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import overlays as ov

W, H, FPS = 1920, 1080, 60
GOLD = np.float32(ov.GOLD)                      # the colour of the labels on the score
VENC = ["-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p"]      # as glow_video.py
FADE = 0.8                                      # seconds from black and to black

def smooth(x):
    x = float(np.clip(x, 0, 1)); return x * x * (3 - 2 * x)

def line(layer, cx, y, s, kind, px, level=1.0, tracking=0.0):
    """one centred line of text, base line at y, added to a float layer (0..1); tracking: extra px between letters"""
    f = ov.font(kind, px)
    adv = [f.getlength(ch) for ch in s]
    wid = sum(adv) + tracking * (len(s) - 1)
    im = Image.new("L", (W, H), 0); d = ImageDraw.Draw(im)
    if tracking:
        x = cx - wid / 2
        for ch, a in zip(s, adv):
            d.text((x, y), ch, font=f, fill=255, anchor="ls"); x += a + tracking
    else:
        d.text((cx - wid / 2, y), s, font=f, fill=255, anchor="ls")
    layer += np.asarray(im, np.float32) / 255 * level
    return wid

def rule(layer, cx, y, wid, level=0.6):
    """a thin rule that thins out towards its ends"""
    x = np.arange(W, dtype=np.float32)
    a = np.clip(1 - np.abs(x - cx) / (wid / 2), 0, 1) ** 0.6
    layer[int(y) - 1:int(y) + 1] += a[None] * level

def title_layers(c):
    """(words that come first, words that come second)"""
    a = np.zeros((H, W), np.float32); b = np.zeros((H, W), np.float32)
    line(a, W / 2, 452, c["title"], "serif", 136)
    line(a, W / 2, 540, c["sub"], "italic", 64, 0.92)
    rule(a, W / 2, 600, 300)
    cr = c.get("credits", [])
    xs = W / 2 + 470 * (np.arange(len(cr)) - (len(cr) - 1) / 2)
    for x, (role, name, detail) in zip(xs, cr):
        line(b, x, 722, role, "sansbold", 23, 0.62, 5.0)
        line(b, x, 780, name, "serif", 46)
        if detail: line(b, x, 824, detail, "italic", 29, 0.72)
    return a, b

def movement_layers(c):
    a = np.zeros((H, W), np.float32)
    if c.get("over"): line(a, W / 2, 372, c["over"], "sansbold", 23, 0.55, 6.0)
    line(a, W / 2, 566, c["numeral"], "serif", 176)
    rule(a, W / 2, 622, 240)
    if c.get("name"):
        line(a, W / 2, 712, c["name"], "serif", 72)
        line(a, W / 2, 778, c["tempo"], "italic", 48, 0.9)
    else:
        line(a, W / 2, 716, c["tempo"], "italic", 64, 0.95)
    return a, None

_yy, _xx = np.mgrid[0:H, 0:W].astype(np.float32)
# darker towards the edges and behind the words
DIM = (0.88 * np.exp(-(((_xx - W / 2) / (W * 0.62)) ** 2 + ((_yy - H / 2) / (H * 0.62)) ** 2))
       * (1 - 0.38 * np.exp(-(((_xx - W / 2) / (W * 0.30)) ** 2 + ((_yy - H * 0.54) / (H * 0.24)) ** 2))))[..., None]
BLUR = 9.0
def shade(im, p=0.0):
    """a picture out of focus and dim (p = 0), as it is (p = 1), or between the two"""
    if p >= 1: return im
    sg = BLUR * (1 - p)
    if sg > 0.3: im = cv2.GaussianBlur(im, (0, 0), sg)
    return im * (DIM + (1 - DIM) * p)
def background(path):
    """the page, out of focus and dim"""
    im = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB).astype(np.float32)
    if im.shape[:2] != (H, W): im = cv2.resize(im, (W, H), interpolation=cv2.INTER_AREA)
    return shade(im)
def video_frames(path, n):
    """the first n frames of a video (uint8 RGB), one after the other"""
    pr = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0", "-frames:v", str(n), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                          stdout=subprocess.PIPE)
    for k in range(n):
        buf = pr.stdout.read(W * H * 3)
        if len(buf) < W * H * 3: sys.exit(f"{path}: only {k} frames of {W}x{H} could be read")
        yield np.frombuffer(buf, np.uint8).reshape(H, W, 3)
    pr.stdout.close(); pr.wait()
def zoomed(f, z):
    M = np.float32([[z, 0, W / 2 * (1 - z)], [0, z, H / 2 * (1 - z)]])
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

def lit(a):
    """(cover, light): the words cover the page in gold, and a soft halo of light lies round them"""
    a = np.clip(a, 0, 1)
    halo = cv2.GaussianBlur(a, (0, 0), 7) * 0.40 + cv2.GaussianBlur(a, (0, 0), 28) * 0.30
    return a[..., None], (halo * (1 - a))[..., None] * GOLD
def put(f, layer, k):
    """the words at strength k (0..1) over the frame"""
    cover, light = layer
    return f * (1 - cover * k) + GOLD * cover * k + light * k

HOLD = 60          # a handover card shows the movement's frame 60 (its own fade from black is over) until that frame is due
def frames(c, kind, base, video=None):
    """the card's frames (uint8 RGB)"""
    T = float(c["seconds"]); n = int(round(T * FPS))
    a, b = title_layers(c) if kind == "title" else movement_layers(c)
    la = lit(a); lb = lit(b) if b is not None else None
    K = int(c.get("handover_cut", 0)) if video else 0
    if K:   # the card lies over the movement's first K frames and hands over to the movement at frame K
        if not HOLD < K: sys.exit("handover_cut must be more than 60 frames")
        src, cur, fr = video_frames(video, K), -1, None
        for i in range(n):
            t = i / FPS
            m = max(i - (n - K), HOLD)                            # the movement's frame behind this frame of the card
            while cur < m: fr = next(src); cur += 1
            p = smooth((i - (n - 90)) / 80)                       # comes into focus over the last 1.5 s; the last 10 frames are the movement's own
            f = shade(fr.astype(np.float32), p)
            z = 1.0 + 0.03 * (1 - smooth(i / (n - 90)))           # the page draws back slowly to its real size
            if z > 1.0002: f = zoomed(f, z)
            f = put(f, la, smooth((t - 0.4) / 0.9) * (1 - smooth((i - (n - 85)) / 60)))
            f *= smooth(t / FADE)
            yield np.clip(f, 0, 255).astype(np.uint8)
        return
    bg = background(os.path.join(base, c["page"]))
    for i in range(n):
        t = i / FPS
        f = zoomed(bg, 1.0 + 0.045 * t / T)                       # the page comes slowly nearer
        f = put(f, la, smooth((t - 0.4) / 0.9))
        if lb is not None: f = put(f, lb, smooth((t - float(c.get("credits_at", 2.3))) / 1.2))
        f *= smooth(min(t / FADE, (T - t - 1 / FPS) / FADE))
        yield np.clip(f, 0, 255).astype(np.uint8)

def still(c, kind, base, out, video=None):
    """the card as it stands when all its words are there"""
    want = int(round(float(c["seconds"]) * FPS) * (0.5 if video else 0.62))
    for i, f in enumerate(frames(c, kind, base, video)):
        if i == want:
            Image.fromarray(f).save(out); return

def encode(c, kind, base, out, video=None):
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + VENC + [out]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in frames(c, kind, base, video): pr.stdin.write(f.tobytes())
    pr.stdin.close()
    if pr.wait(): sys.exit(f"ffmpeg failed for {out}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True); ap.add_argument("--out-dir", required=True)
    ap.add_argument("--credits", help="JSON list of [role, name, detail] shown under the title")
    ap.add_argument("--pages", help="folder the page paths are relative to (default: the spec's folder)")
    ap.add_argument("--video", action="append", default=[], metavar="FILE=MOVEMENT.mp4",
                    help="the movement video behind a card that has handover_cut (FILE is the card's file name)")
    ap.add_argument("--only", nargs="*", help="only these cards (file names)")
    ap.add_argument("--stills", action="store_true", help="write one PNG per card instead of the videos")
    A = ap.parse_args()
    videos = dict(v.split("=", 1) for v in A.video)
    spec = json.load(open(A.spec)); base = A.pages or os.path.dirname(os.path.abspath(A.spec))
    if A.credits: spec["title"]["credits"] = json.load(open(A.credits))
    os.makedirs(A.out_dir, exist_ok=True)
    cards = [("title", spec["title"])] + [("movement", m) for m in spec["movements"]]
    for kind, c in cards:
        if A.only and c["file"] not in A.only: continue
        if c.get("handover_cut") and c["file"] not in videos: sys.exit(f"{c['file']} has handover_cut: give --video {c['file']}=MOVEMENT.mp4")
        out = os.path.join(A.out_dir, c["file"] + (".png" if A.stills else ".mp4"))
        (still if A.stills else encode)(c, kind, base, out, videos.get(c["file"]))
        print(out, flush=True)
