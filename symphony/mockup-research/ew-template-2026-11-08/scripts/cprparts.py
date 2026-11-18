"""List MIDI parts in a .cpr: name, start, length, offset, note count. Usage: python3 -I cprparts.py file.cpr"""
import sys, re, struct, collections
d = open(sys.argv[1], 'rb').read()
def classref(name):
    i = d.find(struct.pack('>I', len(name) + 1) + name + b'\x00') - 4
    return i, b'\x80\x00' + struct.pack('>H', (i - 0xE5) & 0xffff)
pe_def, pe_ref = classref(b'MMidiPartEvent')
pevs = [pe_def] + [m.start() for m in re.finditer(re.escape(pe_ref), d)]
out = []
for p in pevs:
    if p == pe_def:
        body = p + 4 + 4 + 15 + 2  # ffffffff, len, name, version
    else:
        body = p + 4
    ln = struct.unpack('>I', d[body:body+4])[0]
    start, length, off = struct.unpack('>ddd', d[body+6:body+30])
    # part name: first length-prefixed string after
    m = re.compile(rb'\x00\x00\x00([\x02-\x40])([ -~]+)\x00\xef\xbb\xbf', re.S).search(d, body + 30, body + 200)
    name = m.group(2).decode() if m else '?'
    end = body + 4 + ln
    nn = len(re.findall(rb'[\x90-\x9f].{8}.[\x00-\x7f][\x00-\x7f]\x00\x00\x00\x00\x00.GLFX', d[body:end], re.S))
    out.append((p, name, start, length, off, nn, end))
    print(f'{p:9d} {name[:28]:28s} start {start:10.2f} len {length:10.1f} off {off:9.1f} notes {nn:5d} end {end}')
print(len(out), 'parts;', sum(o[5] for o in out), 'notes in parts')
