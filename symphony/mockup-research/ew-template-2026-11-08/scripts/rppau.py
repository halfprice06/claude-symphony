"""Dump AU plugin states from an RPP: decode each <AU ...> chunk (base64 -> plist) and print keys.
Usage: python3 -I rppau.py file.rpp outdir"""
import sys, re, base64, plistlib, os, json
lines = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\n'); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
track = None; i = 0; n = 0
while i < len(lines):
    s = lines[i].strip()
    if s.startswith('NAME ') and lines[i].startswith('    NAME'): track = s[5:].strip('"')
    if s.startswith('<AU '):
        hdr = s; j = i + 1; b = []
        while lines[j].strip() != '>': b.append(lines[j].strip()); j += 1
        raw = base64.b64decode(''.join(b[:-1]) + '==' if False else ''.join(x for x in b))
        # REAPER AU chunk: plist bytes possibly followed by extra; find plist start
        k = raw.find(b'bplist'); k2 = raw.find(b'<?xml')
        start = k if k >= 0 else k2
        name = re.match(r'<AU "([^"]*)"', s).group(1)
        try:
            pl = plistlib.loads(raw[start:]) if start >= 0 else None
        except Exception as e:
            # trim trailing bytes for xml
            try: pl = plistlib.loads(raw[start:raw.rfind(b'</plist>') + 8])
            except Exception as e2: pl = None
        fn = f"{out}/{n:03d}_{re.sub('[^A-Za-z0-9]+','_',track or '')}_{re.sub('[^A-Za-z0-9]+','_',name)}"
        open(fn + '.bin', 'wb').write(raw)
        keys = list(pl.keys()) if isinstance(pl, dict) else None
        print(n, track, '|', name, '| raw', len(raw), 'plist keys', keys)
        if isinstance(pl, dict):
            for kk, vv in pl.items():
                if isinstance(vv, bytes): open(f"{fn}.{kk}.bin", 'wb').write(vv)
        n += 1; i = j
    i += 1
