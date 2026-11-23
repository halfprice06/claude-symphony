"""svg_to_png.py strip.svg strip2.png : render the one-line SVG to a greyscale PNG at the scale of the approved
movement II strip (9.335 px per staff space: 14264 px for its 1527.97-unit line). Cairo surfaces stop at 32767 px,
so a long movement is rendered in tiles of the same SVG (viewBox windows) and joined."""
import re, sys, io
import numpy as np, cairosvg
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

PX = 14264 / 1527.9685          # px per SVG unit (one staff space at staff size 18)
TILE = 12000                     # tile width in px
src, dst = sys.argv[1], sys.argv[2]
svg = open(src).read()
root = re.search(r"<svg[^>]*>", svg)
vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', root.group(0)).group(1).split()]
W, H = int(round(vb[2] * PX)), int(round(vb[3] * PX))
out = np.full((H, W), 255, np.uint8)
for x0 in range(0, W, TILE):
    tw = min(TILE, W - x0)
    u0, uw = vb[0] + x0 / PX, tw / PX
    tag = re.sub(r'viewBox="[^"]+"', f'viewBox="{u0:.4f} {vb[1]:.4f} {uw:.4f} {vb[3]:.4f}"', root.group(0))
    tag = re.sub(r'width="[^"]+"', f'width="{uw:.4f}"', tag, count=1)
    tag = re.sub(r'height="[^"]+"', f'height="{vb[3]:.4f}"', tag, count=1)
    png = cairosvg.svg2png(bytestring=(svg[:root.start()] + tag + svg[root.end():]).encode(), output_width=tw, output_height=H, background_color="white")
    im = np.asarray(Image.open(io.BytesIO(png)).convert("L"))
    out[:, x0:x0 + tw] = im[:H, :tw]
Image.fromarray(out).save(dst)
print(f"{dst}: {W} x {H} px")
