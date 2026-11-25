"""Attack-timing probe (c05, from critic A's probe.py). usage: probe_attacks.py <render dir> [parts.json]
Exit status 1 when any check fails.
Sound start = first 10 ms frame after the score onset (sq) reaching max(peak-20 dB, floor+6 dB), peak over 1.5 s.
Reference attacks are isolated (rest before) and their samples have no slow attack, so anything over 0.06 s is engine lateness."""
import sys, json, glob, os, numpy as np, soundfile as sf
R = sys.argv[1]; P = sys.argv[2]
T = json.load(open(P))['tempo']
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# The checks are score-specific: build/probe.json next to parts.json, {"ref": [[track, score qn, limit s], ...],
# "holes": [[track, qn], ...], "sustain": [[track, qn, limit dB], ...], "opening": [track, ...]}. Missing lists are skipped.
PRB = json.load(open(os.path.join(os.path.dirname(os.path.abspath(P)), 'probe.json')))
def q2s(q):
    tt, lq, lb = 0.0, 0.0, T[0][1]
    for tq, b in T:
        if tq >= q: break
        tt += (tq - lq) * 60 / lb; lq, lb = tq, b
    return tt + (q - lq) * 60 / lb
import rendermap   # mvt1 c03: renders c00-c02 sound 1/6 qn early on the parts.json map
q2s = rendermap.wrap(q2s, rendermap.cycle_of(R))
REF = [tuple(x) for x in PRB.get('ref', [])]   # mvt II: Vc 108/112/114/116, Vla 124, Cb 108, Tbn1 212.5, Timp 277 (0.06 s); Vln I 171 (0.15), Vln II 42 (0.20)
HOLES = [tuple(x) for x in PRB.get('holes', [])]   # tremolo entries after a held note
bad = 0
for name, q, lim in REF:
    f = glob.glob(os.path.join(R, f'*_{name}.wav'))[0]
    x, sr = sf.read(f, dtype='float32'); x = x.mean(1); hop = int(0.01 * sr); n = len(x) // hop
    e = 20 * np.log10(np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, 1)) + 1e-9)
    # mvt1 c03 (critic A #1): the search starts 0.3 s before the score onset (floor from the 0.08 s before that), so an
    # early note is reported as a negative start (c00-c02 sounded 1/6 qn early and read +0.00)
    i = int(round(q2s(q) / 0.01)); fl = e[i - 38:i - 30].max(); w = e[i - 30:i + 150]; pk = w.max()
    d = int(np.argmax(w >= max(pk - 20, fl + 6))) * 0.01 - 0.30
    ok = d <= lim; bad += not ok
    print(f'{name:14s} qn {q:6.1f}  start {d:+.2f} s  (limit {lim:.2f})  {"ok" if ok else "LATE"}{"  (early)" if d < -0.10 else ""}')
for name, q in HOLES:
    f = glob.glob(os.path.join(R, f'*_{name}.wav'))[0]
    x, sr = sf.read(f, dtype='float32'); x = x.mean(1); hop = int(0.01 * sr); n = len(x) // hop
    e = 20 * np.log10(np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, 1)) + 1e-9)
    i = int(round(q2s(q) / 0.01)); before = np.median(e[i - 30:i - 5]); dip = e[i + 5:i + 45].min()
    ok = before - dip <= 6; bad += not ok
    print(f'{name:14s} qn {q:6.1f}  dip {before - dip:5.1f} dB in the first 0.45 s  (limit 6)  {"ok" if ok else "HOLE"}')
# c18 (critic C #2): sustained-note dips after the legato transition. Horn 1 qn 34 (the solo's crest): plateau = loudest
# 50 ms frame in [s, s+0.4 s], dip = plateau - quietest 50 ms frame in [s+0.4, s+0.9 s], on the stereo power (L^2+R^2)/2.
# The mono fold read 12.7 dB in c17 because L and R are anti-correlated there (corr -0.7..-0.86); in stereo power it was
# 7.5 dB for one frame
for name, q, lim in [tuple(x) for x in PRB.get('sustain', [])]:
    f = glob.glob(os.path.join(R, f'*_{name}.wav'))[0]
    x, sr = sf.read(f, dtype='float32'); hop = int(0.05 * sr); n = len(x) // hop
    e = 10 * np.log10(np.mean((x[:n * hop] ** 2).mean(1).reshape(n, hop), 1) + 1e-18)
    i = int(round(q2s(q) / 0.05)); dip = e[i:i + 8].max() - e[i + 8:i + 18].min()
    ok = dip <= lim; bad += not ok
    print(f'{name:14s} qn {q:6.1f}  sustain dip {dip:5.1f} dB in s+0.4..0.9 s  (limit {lim:.0f})  {"ok" if ok else "HOLE"}')
# c06 (A #1): the opening chord; Opus dropped events on the first block of the render (Hn3 -75 dB in c05, Vln II/Vla
# silent in c04). Each voice's loudest 50 ms in the first 1.5 s must be above -70 dB.
for name in PRB.get('opening', []):
    f = glob.glob(os.path.join(R, f'*_{name}.wav'))[0]
    x, sr = sf.read(f, dtype='float32'); x = x.mean(1); hop = int(0.05 * sr); n = int(1.5 * sr) // hop
    pk = 20 * np.log10(np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, 1)).max() + 1e-9)
    ok = pk > -70; bad += not ok
    print(f'{name:14s} qn    0.0  opening max {pk:6.1f} dB  (limit -70)  {"ok" if ok else "SILENT"}')
print('late or hole:', bad)
sys.exit(1 if bad else 0)
