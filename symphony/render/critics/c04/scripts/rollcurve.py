#!/usr/bin/env python3
"""critic 4: timpani roll level curve over time (rolls longer than one bar).
For each roll: timpani K-weighted level in consecutive 1 s windows (re the 0.2-1.2 s window), the timpani against the
loudest other stem (whole K-weighted level, same window), and the timpani in its own band (f0/1.2 .. min(3 f0, 1 kHz))
against the sum of all other stems. Prints the curves and summary: settle by the end, fraction of roll windows with
in-band ratio >= -10 dB ("audible" proxy), and the attack peak (max 50 ms K-weighted level in the first 0.4 s) above
the body (median of windows after 1.2 s).
Usage: rollcurve.py WORK label"""
import sys, os, csv, glob, numpy as np, soundfile as sf
from scipy.signal import butter, sosfiltfilt
W, lab = sys.argv[1:3]
sys.path.insert(0, "/mnt/project-files/symphony/render/r04/lib"); import marks, rtk
mi = rtk.midi_info(os.path.join(W, "score.midi")); rows = list(csv.DictReader(open(os.path.join(W, "notes.csv"), encoding="utf-8")))
R = [r for r in rows if r["staff"].startswith("Timp") and "tremolo" in (r["arts"] or "")]
rl = marks.rolls(rows, mi["bar_s"])
stems = {os.path.basename(p)[:-4]: p for p in glob.glob(os.path.join(W, "stems", "*.wav")) if not p.endswith("_syn.wav")}
sr = sf.info(stems["Timpani"]).samplerate
def seg(name, a, b):
    n = int(b * sr) - max(0, int(a * sr))
    x, _ = sf.read(stems[name], start=max(0, int(a * sr)), stop=int(b * sr), dtype="float64", always_2d=True)
    if len(x) < n: x = np.vstack([x, np.zeros((n - len(x), x.shape[1]))])
    return x
def kl(x):
    k = rtk.k_weight(x, sr); return 10 * np.log10((k ** 2).sum(1).mean() + 1e-20) - 0.691
print(f"{lab}: roll | dyn | hairpin | len s | attack peak over body dB | settle (last 1 s re 0.2-1.2 s) dB | timp - loudest other per 1 s | in-band per 1 s | in-band >= -10 dB share | min in-band")
summ = []
for t0, t1, bs, dyn, hp in rl:
    r = min(R, key=lambda r: abs(float(r["t_on_s"]) - t0)); p = int(r["pitch"])
    f0 = 440 * 2 ** ((p - 69) / 12); lo, hi = f0 / 1.2, min(f0 * 3, 1000)
    sos = butter(4, [lo, hi], "bandpass", fs=sr, output="sos")
    T = seg("Timpani", t0, t1 + 0.1)
    O = {n: seg(n, t0, t1 + 0.1) for n in stems if n not in ("Timpani",)}
    wins = [(0.2, 1.2)] + [(a, a + 1.0) for a in np.arange(1.2, t1 - t0 - 0.99, 1.0)]
    if t1 - t0 - 1.0 > 1.2 and wins[-1][1] < t1 - t0 - 0.05: wins.append((t1 - t0 - 1.0, t1 - t0))
    lv, rel, band = [], [], []
    tb = sosfiltfilt(sos, T.mean(1))
    ob = {n: sosfiltfilt(sos, x.mean(1)) for n, x in O.items()}
    for a, b in wins:
        i, j = int(a * sr), int(b * sr)
        lt = kl(T[i:j]); lv.append(lt)
        oth = [v for v in (kl(x[i:j]) for n, x in O.items() if n != "drums") if v > -70]
        rel.append(lt - max(oth) if oth else np.nan)   # nan: timpani alone
        pt = (tb[i:j] ** 2).mean(); po = sum((y[i:j] ** 2).mean() for y in ob.values())
        band.append(10 * np.log10(pt / po) if po > 1e-9 * pt and po > 1e-14 else np.nan)   # nan: timpani alone in band
    # attack: max 50 ms K level in first 0.4 s vs median body windows
    k = rtk.k_weight(T[: int(0.45 * sr)], sr); e = (k ** 2).sum(1); h = int(0.05 * sr)
    pk = max(10 * np.log10(e[i:i + h].mean() + 1e-20) - 0.691 for i in range(0, len(e) - h, h // 2))
    body = np.median(lv[1:]) if len(lv) > 1 else lv[0]
    band = np.array(band); bb = band[np.isfinite(band)]; aud = float((bb >= -10).mean()) if len(bb) else 1.0
    settle = lv[-1] - lv[0]
    summ.append((bs[0], bs[-1], dyn, t1 - t0, pk - body, settle, aud, float(bb.min()) if len(bb) else np.nan, float(np.nanmedian(rel))))
    print(f"{bs[0]}-{bs[-1]} | {dyn} | {hp or '-'} | {t1-t0:.1f} | {pk-body:+.1f} | {settle:+.1f} | {' '.join(f'{v:+.0f}' for v in rel)} | {' '.join(f'{v:+.0f}' for v in band)} | {aud:.2f} | {(bb.min() if len(bb) else np.nan):+.1f}")
print(f"{lab}: summary bars dyn len attack-over-body settle audible-share min-inband median(timp-loudest)")
for s in summ: print(f"  {s[0]}-{s[1]} {s[2]} {s[3]:.1f}s  {s[4]:+.1f}  {s[5]:+.1f}  {s[6]:.2f}  {s[7]:+.1f}  {s[8]:+.1f}")
