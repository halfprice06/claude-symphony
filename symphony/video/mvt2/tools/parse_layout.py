"""Read video-N.svg pages (one system each) into layout.json: per system the staff line positions by staff name,
note/rest columns (qn, x), bar lines (qn, x), all in PNG pixel coordinates of video-pageN.png."""
import re, json, sys, glob
from PIL import Image

build = sys.argv[1]
out = []
n = len(glob.glob(f"{build}/video-*.svg"))
tr = re.compile(r'translate\(([-\d.]+), ([-\d.]+)\)')
for i in range(1, n + 1):
    s = open(f"{build}/video-{i}.svg").read()
    vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    im = Image.open(f"{build}/video-page{i}.png")
    k = im.size[0] / vb[2]
    staves, cols, bars = {}, [], []
    # walk the attributed groups: <g class=... data-...> then content until the matching </g>
    for m in re.finditer(r'<g class="(\w+)"((?: data-[\w-]+="[^"]*")*)>', s):
        cls, attr = m.group(1), dict(re.findall(r'data-([\w-]+)="([^"]*)"', m.group(2)))
        # content up to the closing tag of this group (groups are not nested in each other)
        depth, j = 1, m.end()
        while depth:
            a, b = s.find("<g", j), s.find("</g>", j)
            if a != -1 and a < b:
                depth += 1; j = a + 2
            else:
                depth -= 1; j = b + 4
        body = s[m.end():j]
        pts = [(float(x), float(y)) for x, y in tr.findall(body)]
        if not pts:
            continue
        if cls == "st":
            ys = sorted(y for _, y in pts)
            x1 = [float(v) for v in re.findall(r'x1="([-\d.]+)"', body)]
            x2 = [float(v) for v in re.findall(r'x2="([-\d.]+)"', body)]
            x0 = pts[0][0]
            staves.setdefault(attr["name"], []).append(
                [round((x0 + min(x1)) * k, 1), round((x0 + max(x2)) * k, 1), round(ys[0] * k, 1), round(ys[-1] * k, 1)])
        elif cls in ("nh", "rs", "mm"):
            cols.append((float(attr["m"]), round(pts[0][0] * k, 1), cls))
        elif cls == "bl":
            bars.append((float(attr["m"]), round(pts[0][0] * k, 1)))
    # a staff symbol is one group per staff per system
    st = {name: v[0] for name, v in staves.items()}
    top = min(v[2] for v in st.values()); bot = max(v[3] for v in st.values())
    left = min(v[0] for v in st.values()); right = max(v[1] for v in st.values())
    # note columns: per qn the leftmost notehead x (fallback: rests)
    by = {}
    for q, x, c in cols:
        if c == "mm":
            continue
        pri = 0 if c == "nh" else 1
        cur = by.get(q)
        if cur is None or (pri, x) < cur:
            by[q] = (pri, x)
    notes = sorted((q, v[1]) for q, v in by.items())
    out.append({"page": i, "png": f"video-page{i}.png", "size": im.size, "staves": st,
                "top": top, "bottom": bot, "left": left, "right": right,
                "cols": notes, "bars": sorted(set(bars))})
json.dump(out, open(f"{build}/layout.json", "w"), indent=0)
for o in out:
    print(o["page"], o["cols"][0][0] if o["cols"] else None, o["cols"][-1][0] if o["cols"] else None,
          len(o["staves"]), int(o["bottom"] - o["top"]), int(o["left"]), int(o["right"]))
