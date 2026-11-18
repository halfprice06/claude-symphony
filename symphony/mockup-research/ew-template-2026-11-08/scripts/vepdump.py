"""Parse the Vienna Ensemble Pro project embedded in a Cubase .cpr (zstd + Qt QDataStream of QVariant maps).
Usage: python3 -I vepdump.py file.cpr (or an already decoded file.vep.bin) -> prints the channel tree and a channel table.
Needs the zstandard package for .cpr input."""
import sys, struct, json, re, base64
d = open(sys.argv[1], 'rb').read()
if d[:4] == b'RIFF':
    import zstandard
    m = re.search(rb'"serverData":"([A-Za-z0-9+/=]+)"', d)
    d = zstandard.ZstdDecompressor().decompress(base64.b64decode(m.group(1)), max_output_size=500_000_000)
class P:
    def __init__(s, d, i=0): s.d = d; s.i = i
    def u32(s): v = struct.unpack('>I', s.d[s.i:s.i+4])[0]; s.i += 4; return v
    def qstr(s):
        n = s.u32()
        if n == 0xffffffff: return None
        v = s.d[s.i:s.i+n].decode('utf-16-be', 'replace'); s.i += n; return v
    def var(s):
        t = s.u32(); s.i += 1  # null flag
        if t == 1: v = s.d[s.i] != 0; s.i += 1; return v
        if t in (2, 3): v = struct.unpack('>i' if t == 2 else '>I', s.d[s.i:s.i+4])[0]; s.i += 4; return v
        if t in (4, 5): v = struct.unpack('>q' if t == 4 else '>Q', s.d[s.i:s.i+8])[0]; s.i += 8; return v
        if t in (6, 135): v = struct.unpack('>d', s.d[s.i:s.i+8])[0]; s.i += 8; return v
        if t == 38: v = struct.unpack('>f', s.d[s.i:s.i+4])[0]; s.i += 4; return v
        if t == 7: s.i += 2; return '?'
        if t == 67: s.i += 11; return 'color'
        if t == 10: return s.qstr()
        if t == 11: return [s.qstr() for _ in range(s.u32())]
        if t == 12:
            n = s.u32()
            if n == 0xffffffff: return b''
            v = s.d[s.i:s.i+n]; s.i += n; return v
        if t in (8, 28): return {s.qstr(): s.var() for _ in range(s.u32())}
        if t == 9: return [s.var() for _ in range(s.u32())]
        raise ValueError(f'type {t} at {s.i}')
p = P(d, 8)
top = {}
try:
    while p.i < len(d):
        k = p.qstr(); top[k] = p.var()
except Exception as e:
    print('stopped:', e, 'keys so far', list(top)[:40])
def short(v):
    if isinstance(v, bytes): return f'<{len(v)} bytes>'
    if isinstance(v, float): return round(v, 4)
    return v
def walk(o, depth=0, path=''):
    if isinstance(o, dict):
        if 'title' in o or 'pluginName' in o:
            keys = ('title', 'pluginName', 'Volume', 'Balance', 'Center', 'Width', 'Mute', 'Bypass', 'PreFader', 'Aux Send', 'output', 'index', 'vstProgram')
            info = {k: short(o[k]) for k in keys if k in o and not isinstance(o[k], (dict, list))}
            params = o.get('parameters')
            if isinstance(params, (dict, list)) and 'pluginName' in o:
                info['params'] = str(params)[:160]
            print('  ' * depth + json.dumps(info, default=str))
        for k, v in o.items():
            if isinstance(v, (dict, list)): walk(v, depth + 1, path + '/' + str(k))
    elif isinstance(o, list):
        for v in o: walk(v, depth, path)
walk(top)

# compact table: one row per channel
import math
def db(g): return '-inf' if not g else f'{20*math.log10(g):+.1f}'
print('\n== channel table (fader dB, pan centre 0..1 with width, sends dB->output, plugins)')
def table(o, depth=0, group=''):
    if isinstance(o, dict):
        if 'title' in o:
            pr = o.get('parameters') if isinstance(o.get('parameters'), dict) else {}
            vol = pr.get('Volume'); plugs = []; sends = []; pan = ''
            for key in ('fxPlugins', 'postFxPlugins', 'auxSends'):
                for pl in o.get(key, []) if isinstance(o.get(key), list) else []:
                    if not isinstance(pl, dict): continue
                    nm = pl.get('pluginName'); pp = pl.get('parameters') if isinstance(pl.get('parameters'), dict) else {}
                    if nm == 'Aux Send': sends.append(f"{db(pp.get('Volume'))}->{pl.get('output')}{' pre' if pp.get('PreFader') else ''}")
                    elif nm == 'Vienna Stereo Pan': pan = f"c{pp.get('Center', 0):.2f} w{pp.get('Width', 0):.2f}"
                    elif nm: plugs.append(nm + (' (byp)' if pp.get('Bypass') else ''))
            print(f"{'  '*depth}{o.get('index')}: {o['title'][:30]:30s} fader {db(vol) if vol is not None else '?':>6} | {pan:13s} | sends {','.join(sends) or '-'} | {', '.join(plugs)} | mir {str(o.get('mirWetSendOutput', ''))[:20]}")
        for k, v in o.items():
            if isinstance(v, (dict, list)) and k not in ('fxPlugins', 'postFxPlugins', 'auxSends', 'parameters'): table(v, depth + (1 if 'title' in o else 0))
    elif isinstance(o, list):
        for v in o: table(v, depth)
table(top)
