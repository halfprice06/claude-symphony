"""Probe a Cubase .cpr: tempo map, MIDI parts, note and CC records. Usage: python3 -I cprprobe.py file.cpr"""
import sys, re, struct, collections
d = open(sys.argv[1], 'rb').read()
# tempo map: records of float spb, double sec, double ppq, 2 bytes, after MTempoTrackEvent header
i = d.find(b'MTempoTrackEvent\x00')
hdr = i + 17
print('tempo header', d[hdr:hdr+12].hex())
n = struct.unpack('>I', d[hdr+7:hdr+11])[0] if False else None
# search first record: float in 0.2..2 followed by double 0 and double 0
j = hdr
while j < hdr + 64:
    f = struct.unpack('>f', d[j:j+4])[0]
    if 0.2 < f < 2 and d[j+4:j+20] == b'\x00' * 16: break
    j += 1
recs = []
while True:
    f, sec, ppq = struct.unpack('>fdd', d[j:j+20])
    if not (0.1 < f < 3 and 0 <= sec < 1e5 and 0 <= ppq < 1e7): break
    if recs and (ppq < recs[-1][2] or sec < recs[-1][1]): break
    recs.append((f, sec, ppq, d[j+20:j+22].hex())); j += 22
print('tempo records', len(recs))
for r in recs[:12] + recs[-5:]: print('  spb %.4f (%.1f bpm) sec %.3f ppq %.1f %s' % (r[0], 60 / r[0], r[1], r[2], r[3]))
c = collections.Counter(r[3] for r in recs); print('  flag bytes', c.most_common(5))
notes = list(re.finditer(rb'([\x90-\x9f])(.{8})(.)([\x00-\x7f])([\x00-\x7f])\x00\x00\x00\x00\x00(.)GLFX', d, re.S))
print('note-like records', len(notes))
cb = collections.Counter(m.group(3) for m in notes); print('  byte before pitch', cb.most_common(5))
cf = collections.Counter(m.group(6) for m in notes); print('  byte before GLFX', cf.most_common(5))
for m in notes[:5]:
    k = d.find(b'adcn', m.end(), m.end() + 120)
    print('  ', m.start(), struct.unpack('>d', m.group(2))[0], m.group(4)[0], m.group(5)[0], k - m.end(), d[k+4:k+40].hex() if k > 0 else None)
ccs = list(re.finditer(rb'([\xb0-\xbf])(.{8})(.)([\x00-\x7f])([\x00-\x7f])\x00\x00\x00\x00\x00(.)GLFX', d, re.S))
print('cc-like records', len(ccs))
print('  cc numbers', collections.Counter(m.group(4)[0] for m in ccs).most_common(12))
print('  byte before ccnum', collections.Counter(m.group(3) for m in ccs).most_common(5))
# what follows CC records
fol = collections.Counter(); ty = collections.Counter(); fl = []
for m in ccs:
    tail = d[m.end()+10:m.end()+60]
    tag = tail[:4]
    fol[tag] += 1
    if tag == b'bOuc':
        a, b = struct.unpack('>ff', tail[14:18] + tail[22:26]) if False else (None, None)
        k = tail.find(b'yTuc'); ty[tail[k+4:k+14].hex() if k >= 0 else None] += 1
        fl.append(tail[4:30].hex())
print('after CC GLFX block:', fol.most_common(6))
print('cuTy values:', ty.most_common(6))
for x in fl[:8]: print('  ', x)
