"""Overlays for the glow video (concepts, November 2026): which instrument is playing (letters, icons, names on the
paper) and analysis captions (a subtitle bar, notes written on the score, a card with music examples).
Pure drawing helpers; glow_video.py decides what to draw where."""
import io, json, math, os, textwrap
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(HERE, "..", "icons")
FONT = {"serif": "/usr/share/fonts/opentype/urw-base35/C059-Roman.otf",
        "italic": "/usr/share/fonts/opentype/urw-base35/C059-Italic.otf",
        "bold": "/usr/share/fonts/opentype/urw-base35/C059-Bold.otf",
        "sans": "/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf",
        "sansbold": "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"}
FF = "/usr/share/fonts/truetype/freefont/"
FALLBACK = {"serif": FF + "FreeSerif.ttf", "italic": FF + "FreeSerifItalic.ttf", "bold": FF + "FreeSerifBold.ttf",
            "sans": FF + "FreeSans.ttf", "sansbold": FF + "FreeSansBold.ttf"}
SPECIAL = set("♭♯♮→⁶")                 # not in C059 or Carlito

ABBR = {"Flutes 1·2": "Fl", "Oboes 1·2": "Ob", "Cor anglais": "C.a.", "Clarinets 1·2": "Cl", "Bass clarinet": "B.cl",
        "Bassoons 1·2": "Bn", "Contrabassoon": "Cbn", "Horns 1·2": "Hn", "Horns 3·4": "Hn", "Trumpets 1·2": "Tpt",
        "Trumpet 3": "Tpt", "Trombones 1·2": "Tbn", "Bass trombone": "B.tbn", "Tuba": "Tba", "Timpani": "Timp",
        "Percussion": "Perc", "Harp RH": "Hp", "Harp LH": "Hp", "Violins I": "Vn I", "Violins II": "Vn II",
        "Violas": "Va", "Violoncellos": "Vc", "Double basses": "Cb"}
NAME = {"Flutes 1·2": "Flutes", "Oboes 1·2": "Oboes", "Clarinets 1·2": "Clarinets", "Bassoons 1·2": "Bassoons",
        "Trumpets 1·2": "Trumpets", "Trombones 1·2": "Trombones", "Harp RH": "Harp", "Harp LH": "Harp",
        "Violoncellos": "Cellos"}
ICON = {"Flutes 1·2": "flute", "Oboes 1·2": "oboe", "Cor anglais": "cor-anglais", "Clarinets 1·2": "clarinet",
        "Bass clarinet": "bass-clarinet", "Bassoons 1·2": "bassoon", "Contrabassoon": "bassoon", "Horns 1·2": "horn",
        "Horns 3·4": "horn", "Trumpets 1·2": "trumpet", "Trumpet 3": "trumpet", "Trombones 1·2": "trombone",
        "Bass trombone": "trombone", "Tuba": "tuba", "Timpani": "timpani", "Percussion": "percussion",
        "Harp RH": "harp", "Harp LH": "harp", "Violins I": "violin", "Violins II": "violin", "Violas": "violin",
        "Violoncellos": "cello", "Double basses": "double-bass"}

_font_cache = {}
def font(kind, px, fallback=False):
    k = (kind, int(px), fallback)
    if k not in _font_cache: _font_cache[k] = ImageFont.truetype((FALLBACK if fallback else FONT)[kind], int(px))
    return _font_cache[k]
def runs(s):
    """split a string into runs for the main font and for the fallback font (accidentals)"""
    out = []
    for ch in s:
        fb = ch in SPECIAL
        if out and out[-1][1] == fb: out[-1][0] += ch
        else: out.append([ch, fb])
    return out
def text_width(s, kind, px):
    return sum(font(kind, px, fb).getlength(r) for r, fb in runs(s))
def draw_text(d, xy, s, kind, px, fill):
    """draw text with its baseline at xy[1], switching to the fallback font for accidentals"""
    x, y = xy
    for r, fb in runs(s):
        d.text((x, y), r, font=font(kind, px, fb), fill=fill, anchor="ls"); x += font(kind, px, fb).getlength(r)

def wrap(s, kind, px, maxw):
    """lines of s no wider than maxw px"""
    lines, cur = [], ""
    for w_ in s.split():
        t_ = (cur + " " + w_).strip()
        if cur and text_width(t_, kind, px) > maxw: lines.append(cur); cur = w_
        else: cur = t_
    return lines + ([cur] if cur else [])

_text_cache = {}
def text_alpha(s, kind, px, pad=4):
    """greyscale alpha (float32 0..1) of a line of text"""
    k = (s, kind, int(px))
    if k not in _text_cache:
        f = font(kind, px)
        asc, desc = f.getmetrics()
        im = Image.new("L", (int(text_width(s, kind, px)) + 2 * pad, asc + desc + 2 * pad), 0)
        draw_text(ImageDraw.Draw(im), (pad, pad + asc), s, kind, px, 255)
        _text_cache[k] = np.asarray(im, np.float32) / 255.0
    return _text_cache[k]

_icon_cache = {}
def icon_alpha(name, px):
    """greyscale alpha of an instrument icon, px high"""
    px = int(max(8, px))
    k = (name, px)
    if k not in _icon_cache:
        import cairosvg
        png = cairosvg.svg2png(url=os.path.join(ICON_DIR, name + ".svg"), output_width=px, output_height=px)
        _icon_cache[k] = np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"), np.float32)[..., 3] / 255.0
    return _icon_cache[k]

def add_sprite(layer, alpha, cx, cy, col, gain=1.0):
    """add a coloured sprite (alpha mask) centred at (cx, cy) to a float layer"""
    h, w = alpha.shape
    x0, y0 = int(round(cx - w / 2)), int(round(cy - h / 2))
    X0, Y0, X1, Y1 = max(x0, 0), max(y0, 0), min(x0 + w, layer.shape[1]), min(y0 + h, layer.shape[0])
    if X1 <= X0 or Y1 <= Y0: return
    a = alpha[Y0 - y0:Y1 - y0, X0 - x0:X1 - x0, None]
    layer[Y0:Y1, X0:X1] += a * (np.asarray(col, np.float32) * gain)

def warp_sprite(layer, alpha, quad, col, gain=1.0):
    """add a sprite mapped onto a screen quadrilateral (tl, tr, br, bl), e.g. text lying on the paper"""
    h, w = alpha.shape
    q = np.float32(quad)
    x0, y0 = np.floor(q.min(0)).astype(int) - 2; x1, y1 = np.ceil(q.max(0)).astype(int) + 2
    X0, Y0, X1, Y1 = max(x0, 0), max(y0, 0), min(x1, layer.shape[1]), min(y1, layer.shape[0])
    if X1 <= X0 or Y1 <= Y0 or (x1 - x0) > 3 * layer.shape[1]: return
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), q - np.float32([X0, Y0]))
    a = cv2.warpPerspective(alpha, M, (X1 - X0, Y1 - Y0), flags=cv2.INTER_LINEAR)
    layer[Y0:Y1, X0:X1] += a[..., None] * (np.asarray(col, np.float32) * gain)

# ---------- captions ----------
GOLD = (255, 214, 150)
def load_captions(path, pos_to_s):
    """captions JSON: [{"from": "63.1", "to": "64.3", "kind": "Motive", "text": ..., "short": ..., "bars": "63–64",
    "anchor": {"staff": "Trombones 1·2", "from": "63.1", "to": "65.1"}, "chords": [["60.1", "A♭"], ...],
    "examples": [{"png": "...", "label": "..."}]}]; positions are "bar.quarter" (quarter notes counted from 1)"""
    caps = json.load(open(path)) if isinstance(path, str) else [dict(c) for c in path]
    for c in caps:
        c["t0"], c["t1"] = pos_to_s(c["from"]), pos_to_s(c["to"])
        if "chords" in c: c["chords"] = [(pos_to_s(p), lab) for p, lab in c["chords"]]
        if "anchor" in c:
            c["anchor"]["t0"], c["anchor"]["t1"] = pos_to_s(c["anchor"]["from"]), pos_to_s(c["anchor"]["to"])
    return caps

def fade(t, t0, t1, a=0.45):
    return float(np.clip(min((t - t0) / a, (t1 - t) / a), 0, 1))

_card_cache = {}
def _rgba(im):
    """premultiplied RGBA float (0..1)"""
    a = np.asarray(im, np.float32) / 255.0
    a[..., :3] *= a[..., 3:]
    return a

def bar_overlay(c, W, H):
    """style 'bar': a subtitle band at the foot of the frame (RGBA float)"""
    k = ("bar", id(c))
    if k in _card_cache: return _card_cache[k]
    im = Image.new("RGBA", (W, 300), (0, 0, 0, 0))
    g = np.linspace(0, 1, 300)[:, None] ** 1.6 * 0.78                     # dark gradient behind the text
    band = np.zeros((300, W, 4), np.float32); band[..., 3] = g
    d = ImageDraw.Draw(im)
    x = 120
    lab = c["kind"].upper() + ("   ·   bars " + c["bars"] if c.get("bars") else "")
    draw_text(d, (x, 172), lab, "sansbold", 24, GOLD + (255,))
    lines = wrap(c["text"], "serif", 36, W - 2 * x)
    for i, ln in enumerate(lines[:2]):
        draw_text(d, (x, 222 + i * 46), ln, "serif", 36, (245, 245, 250, 255))
    fg = _rgba(im)
    out = fg + band * (1 - fg[..., 3:])
    _card_cache[k] = (out, H - 300)
    return _card_cache[k]

def card_overlay(c, W, H):
    """style 'card': a card at the top left with the text and, when given, the music examples in notation"""
    k = ("card", id(c))
    if k in _card_cache: return _card_cache[k]
    cw = 640; pad = 30
    lines = wrap(c["text"], "serif", 29, cw - 2 * pad)
    exs = []
    for e in c.get("examples", []):
        ex = Image.open(e["png"]).convert("RGBA")
        sc = min(1.0, (cw - 2 * pad) / ex.size[0]); ex = ex.resize((int(ex.size[0] * sc), int(ex.size[1] * sc)), Image.LANCZOS)
        exs.append((ex, e.get("label", "")))
    h = pad + 34 + len(lines) * 38 + sum(ex.size[1] + 40 for ex, _ in exs) + pad
    im = Image.new("RGBA", (cw, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, cw - 1, h - 1), 18, fill=(10, 12, 18, 196), outline=(255, 255, 255, 46), width=2)
    draw_text(d, (pad, pad + 16), c["kind"].upper() + ("  ·  bars " + c["bars"] if c.get("bars") else ""), "sansbold", 22, GOLD + (255,))
    y = pad + 34
    for ln in lines:
        draw_text(d, (pad, y + 28), ln, "serif", 29, (240, 240, 246, 255)); y += 38
    for ex, lab in exs:
        y += 8
        draw_text(d, (pad, y + 18), lab, "sans", 20, (190, 195, 210, 255)); y += 26
        im.alpha_composite(ex, (pad, y)); y += ex.size[1] + 6
    _card_cache[k] = (_rgba(im), (56, 52))
    return _card_cache[k]

def composite(img, ov, x0, y0, a):
    """blend a premultiplied RGBA float overlay (0..1) onto an image (0..255 float) at (x0, y0) with extra opacity a"""
    h, w = ov.shape[:2]
    X0, Y0, X1, Y1 = max(x0, 0), max(y0, 0), min(x0 + w, img.shape[1]), min(y0 + h, img.shape[0])
    if X1 <= X0 or Y1 <= Y0 or a <= 0: return
    o = ov[Y0 - y0:Y1 - y0, X0 - x0:X1 - x0]
    al = o[..., 3:] * a
    img[Y0:Y1, X0:X1] = img[Y0:Y1, X0:X1] * (1 - al) + o[..., :3] * 255 * a
