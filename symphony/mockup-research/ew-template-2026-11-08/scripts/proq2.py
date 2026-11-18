"""Decode FabFilter Pro-Q 2 AU 'data' blobs: 12-byte header (count at bytes 8-11, BE), then (BE uint32 index, BE float) pairs.
Per band 7 params: enabled, freq (log2 Hz), gain dB, Q (normalised; Q=0.025*1600**n assumed), shape, slope, stereo placement.
Usage: python3 -I proq2.py file.data.bin ..."""
import sys, struct, os
SH = ['Bell', 'LowShelf', 'LowCut', 'HighShelf', 'HighCut', 'Notch', 'BandPass', 'TiltShelf']
SL = ['6', '12', '18', '24', '30', '36', '48', '72', '96']
ST = ['L', 'R', 'Stereo', 'Mid', 'Side']
for f in sys.argv[1:]:
    d = open(f, 'rb').read(); n = struct.unpack('>I', d[8:12])[0]
    p = {}
    for k in range(n):
        o = 12 + 8 * k
        if o + 8 > len(d): break
        i, v = struct.unpack('>If', d[o:o+8]); p[i] = v
    bands = []
    for b in range(24):
        en, fr, g, qn, sh, sl, stp = [p.get(b*7+j) for j in range(7)]
        if en != 1.0: continue
        s = SH[int(sh)] if sh is not None and int(sh) < len(SH) else sh
        txt = f"{s} {2**fr:.0f} Hz"
        if s in ('Bell', 'LowShelf', 'HighShelf', 'TiltShelf'): txt += f" {g:+.1f} dB"
        if s in ('Bell', 'Notch', 'BandPass'): txt += f" Q~{0.025*1600**qn:.2f}"
        if s in ('LowCut', 'HighCut'): txt += f" {SL[int(sl)] if int(sl) < len(SL) else sl} dB/oct"
        if stp is not None and int(stp) != 2: txt += f" ({ST[int(stp)] if int(stp) < len(ST) else stp})"
        bands.append(txt)
    glob = {i: round(v, 3) for i, v in p.items() if i >= 168}
    print(f"{os.path.basename(f).split('_AU_')[0]}: " + "; ".join(bands) + f"  | globals {glob}")
