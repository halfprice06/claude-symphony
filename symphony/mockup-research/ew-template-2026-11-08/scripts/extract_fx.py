"""Extract verbatim FX chains (REAPER chunk text) and decoded settings for the mix tracks of an EW template .RPP.
Usage: python3 -I extract_fx.py <project.RPP> <outdir>"""
import sys, os, re, json, base64, struct, math, zlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
L = open(src, encoding='utf-8', errors='replace').read().replace('\r', '').split('\n')
WANT = {"STRINGS","BRASS","WOODWINDS","PIANO + HARP + TUNED PERC","ORCHESTRAL PERC","MISC","STRING VERB","BRASS VERB",
        "WW VERB","PERC VERB","CHOIR VERB","LONG VERB","ALGO GLUE","DELAY","Harp KS Master","Timpani Flt KS"}
def block_end(i):
    d = 0
    for j in range(i, len(L)):
        s = L[j].strip()
        if s.startswith('<'): d += 1
        elif s == '>':
            d -= 1
            if d == 0: return j
    raise ValueError
# track index for AUXRECV names
tracks = []
for i, l in enumerate(L):
    if l.startswith('  <TRACK'):
        e = block_end(i); nm = next(x[9:].strip('"') for x in L[i:e] if x.startswith('    NAME '))
        tracks.append((nm, i, e))
def dec_reaeq(b):
    bands = []
    d = b[60:]
    k = 8
    while k + 32 <= len(d):
        t, en = struct.unpack('<ii', d[k:k+8]); f, g, q = struct.unpack('<ddd', d[k+8:k+32])
        if not (0 <= t <= 12 and en in (0, 1) and 10 < f < 24000): break
        names = {0:"low shelf",1:"high shelf",3:"low pass",4:"high pass",8:"band (peak)",9:"band (alt)",6:"notch",7:"band pass"}
        bands.append({"type": t, "type_name": names.get(t, str(t)), "enabled": bool(en), "freq_hz": round(f, 2),
                      "gain_db": round(20*math.log10(g), 2) if g > 0 else None, "bw_oct": round(q, 3)})
        k += 33
    return bands
def fx_blocks(i0, i1):
    res = []; i = i0
    while i < i1:
        if re.match(r'\s*<(VST|JS|AU|CLAP) ', L[i]):
            e = block_end(i); res.append((i, e)); i = e
        i += 1
    return res
summary = {}
def handle(label, i0, i1, extra):
    blocks = fx_blocks(i0, i1)
    fx = []
    for (a, e) in blocks:
        head = L[a].strip(); raw = [x.strip() for x in L[a+1:e]]
        name = re.match(r'<\w+ "([^"]*)"', head).group(1)
        b = b''.join(base64.b64decode(s + '=' * (-len(s) % 4)) for s in raw[:-1])
        ent = {"fx": name, "chunk_header": head, "chunk_base64_lines": raw, "bypass_line": L[a-1].strip()}
        if 'ReaEQ' in name: ent["decoded_bands"] = dec_reaeq(b)
        if 'Spaces II' in name:
            m = re.search(rb'\{"selectedPreset".*?\}(?=\{)', b, re.S)
            if m: ent["decoded_state"] = json.loads(m.group(0))
        if 'Opus' in name:
            k = b.find(b'\x1f\x8b')
            js = json.loads(zlib.decompressobj(31).decompress(b[k:]))
            ent["note"] = "Opus state omitted (large); see opus-mics.txt"
            ent.pop("chunk_base64_lines")
        fx.append(ent)
    summary[label] = dict(extra, fx=fx)
    # verbatim FXCHAIN text
    with open(os.path.join(out, 'chunks', re.sub(r'[^A-Za-z0-9]+', '_', label).strip('_') + '.txt'), 'w') as f:
        f.write('\n'.join(L[i0:i1+1]) + '\n')
os.makedirs(os.path.join(out, 'chunks'), exist_ok=True)
# master
for i, l in enumerate(L):
    if l.strip() == '<MASTERFXLIST':
        handle('MASTER', i, block_end(i), {}); break
for idx, (nm, a, e) in enumerate(tracks):
    if nm not in WANT: continue
    vol = pan = None; aux = []
    for x in L[a:e]:
        if x.startswith('    VOLPAN '): p = x.split(); vol = float(p[1]); pan = float(p[2])
        if x.startswith('    AUXRECV '):
            p = x.split(); aux.append({"from_track": tracks[int(p[1])][0], "mode": int(p[2]), "mode_name": {0:"post-fader",1:"pre-FX",3:"pre-fader (post-FX)"}.get(int(p[2])),
                                       "level_db": round(20*math.log10(float(p[3])), 2), "pan": float(p[4]), "raw": x.strip()})
    fxs = next((j for j in range(a, e) if L[j].strip() == '<FXCHAIN'), None)
    extra = {"track_index": idx, "fader_db": round(20*math.log10(vol), 2) if vol else None, "pan": pan, "receives": aux}
    if fxs is None: summary[nm] = dict(extra, fx=[]); continue
    handle(nm, fxs, block_end(fxs), extra)
json.dump(summary, open(os.path.join(out, 'mix-fx.json'), 'w'), indent=1)
print('\n'.join(f"{k}: {[f['fx'] for f in v['fx']]}" for k, v in summary.items()))
