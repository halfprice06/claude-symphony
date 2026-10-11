"""Attack-timing probe (c05, from critic A's probe.py). usage: probe_attacks.py <render dir> [parts.json]
Exit status 1 when any check fails.
Sound start = first 10 ms frame after the score onset (sq) reaching max(peak-20 dB, floor+6 dB), peak over 1.5 s.
Reference attacks are isolated (rest before) and their samples have no slow attack, so anything over 0.06 s is engine lateness."""
import sys, json, glob, os, numpy as np, soundfile as sf
R = sys.argv[1]; P = sys.argv[2] if len(sys.argv) > 2 else '/Users/gooby/sandbox/claude_composes/symphony/mvt2/reaper/build/parts.json'
T = json.load(open(P))['tempo']
def q2s(q):
    tt, lq, lb = 0.0, 0.0, T[0][1]
    for tq, b in T:
        if tq >= q: break
        tt += (tq - lq) * 60 / lb; lq, lb = tq, b
    return tt + (q - lq) * 60 / lb
REF = [('Violoncellos', q, 0.06) for q in (108, 112, 114, 116)] + [('Violas', 124, 0.06), ('Double basses', 108, 0.06),
       ('Trombone 1', 212.5, 0.06), ('Timpani', 277, 0.06), ('Violins I', 171, 0.15), ('Violins II', 42, 0.20)]
HOLES = [('Violas', 204), ('Violins I', 212), ('Violins II', 212), ('Violoncellos', 212)]   # tremolo entries after a held note
bad = 0
for name, q, lim in REF:
    f = glob.glob(os.path.join(R, f'*_{name}.wav'))[0]
    x, sr = sf.read(f, dtype='float32'); x = x.mean(1); hop = int(0.01 * sr); n = len(x) // hop
    e = 20 * np.log10(np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, 1)) + 1e-9)
    i = int(round(q2s(q) / 0.01)); fl = e[i - 8:i].max(); w = e[i:i + 150]; pk = w.max()
    d = int(np.argmax(w >= max(pk - 20, fl + 6))) * 0.01
    ok = d <= lim; bad += not ok
    print(f'{name:14s} qn {q:6.1f}  start {d:+.2f} s  (limit {lim:.2f})  {"ok" if ok else "LATE"}')
for name, q in HOLES:
    f = glob.glob(os.path.join(R, f'*_{name}.wav'))[0]
    x, sr = sf.read(f, dtype='float32'); x = x.mean(1); hop = int(0.01 * sr); n = len(x) // hop
    e = 20 * np.log10(np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, 1)) + 1e-9)
    i = int(round(q2s(q) / 0.01)); before = np.median(e[i - 30:i - 5]); dip = e[i + 5:i + 45].min()
    ok = before - dip <= 6; bad += not ok
    print(f'{name:14s} qn {q:6.1f}  dip {before - dip:5.1f} dB in the first 0.45 s  (limit 6)  {"ok" if ok else "HOLE"}')
# c06 (A #1): the opening chord; Opus dropped events on the first block of the render (Hn3 -75 dB in c05, Vln II/Vla
# silent in c04). Each voice's loudest 50 ms in the first 1.5 s must be above -70 dB.
for name in ('Horn 3', 'Violins I', 'Violins II', 'Violas', 'Violoncellos'):
    f = glob.glob(os.path.join(R, f'*_{name}.wav'))[0]
    x, sr = sf.read(f, dtype='float32'); x = x.mean(1); hop = int(0.05 * sr); n = int(1.5 * sr) // hop
    pk = 20 * np.log10(np.sqrt(np.mean(x[:n * hop].reshape(n, hop) ** 2, 1)).max() + 1e-9)
    ok = pk > -70; bad += not ok
    print(f'{name:14s} qn    0.0  opening max {pk:6.1f} dB  (limit -70)  {"ok" if ok else "SILENT"}')
print('late or hole:', bad)
sys.exit(1 if bad else 0)
