"""Minimal reader for MIDI data in Cubase .cpr files (Cubase 12-14 era), reverse-engineered on one file.
read(path) -> dict(tempo=[(ppq, sec, spb)], parts=[dict(name, start, length, off, notes=[(pos, pitch, vel, len)], ccs=[(pos, cc, val, curve or None)] where curve=(x, y, weight) of a rational quadratic Bezier control point)])
Positions are in ticks at 480 PPQ, relative to the part (see part_abs)."""
import re, struct
NOTE = re.compile(rb'([\x90-\x9f])(.{8})(.)([\x00-\x7f])([\x00-\x7f])\x00\x00\x00\x00\x00(.)GLFX', re.S)
CC = re.compile(rb'([\xb0-\xbf])(.{8})(.)([\x00-\x7f])([\x00-\x7f])\x00\x00\x00\x00\x00(.)GLFX', re.S)
NAME = re.compile(rb'\x00\x00\x00([\x02-\x40])([ -~]+)\x00\xef\xbb\xbf', re.S)

def read(path):
    d = open(path, 'rb').read()
    i = d.find(b'MTempoTrackEvent\x00') + 17; j = i
    while j < i + 64:
        f = struct.unpack('>f', d[j:j+4])[0]
        if 0.2 < f < 2 and d[j+4:j+20] == b'\x00' * 16: break
        j += 1
    tempo = []
    while True:
        f, sec, ppq = struct.unpack('>fdd', d[j:j+20])
        if not (0.1 < f < 3 and 0 <= sec < 1e5 and 0 <= ppq < 1e7): break
        if tempo and (ppq < tempo[-1][0] or sec < tempo[-1][1]): break
        tempo.append((ppq, sec, f)); j += 22
    def classref(name):
        k = d.find(struct.pack('>I', len(name) + 1) + name + b'\x00') - 4
        return k, b'\x80\x00' + struct.pack('>H', (k - 0xE5) & 0xffff)
    pe_def, pe_ref = classref(b'MMidiPartEvent')
    parts = []
    for p in [pe_def] + [m.start() for m in re.finditer(re.escape(pe_ref), d)]:
        body = p + 4 + 4 + 15 + 2 if p == pe_def else p + 4
        ln = struct.unpack('>I', d[body:body+4])[0]
        start, length, off = struct.unpack('>ddd', d[body+6:body+30])
        m = NAME.search(d, body + 30, body + 200)
        end = body + 4 + ln; seg = d[body:end]
        notes = []
        for n in NOTE.finditer(seg):
            k = seg.find(b'adcn', n.end(), n.end() + 120)
            L = struct.unpack('>d', seg[k+14:k+22])[0] if k > 0 else 0.0
            notes.append((struct.unpack('>d', n.group(2))[0], n.group(4)[0], n.group(5)[0], L))
        ccs = []
        for c in CC.finditer(seg):
            tail = seg[c.end()+10:c.end()+60]
            curve = None
            if tail[:4] == b'bOuc':
                if tail[6:8] == b'\x80\x00':  # reference to the curve class: ref(4) len(4) then 3 floats
                    f0 = 14
                else:  # first use: inline class definitions, then version(2) len(4) then 3 floats
                    tail = seg[c.end()+10:c.end()+160]; f0 = tail.find(b'RationalBezier\x00') + 15 + 6
                curve = struct.unpack('>fff', tail[f0:f0+12])
            ccs.append((struct.unpack('>d', c.group(2))[0], c.group(4)[0], c.group(5)[0], curve))
        parts.append(dict(name=m.group(2).decode() if m else '?', start=start, length=length, off=off, notes=notes, ccs=ccs))
    return dict(tempo=tempo, parts=parts)

def part_abs(part, pos, mode='minus'):
    if mode == 'minus': return part['start'] + pos - part['off']
    if mode == 'plus': return part['start'] + pos + part['off']
    return part['start'] + pos
