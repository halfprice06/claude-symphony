#!/usr/bin/env python3
"""critic 5: onset sharpness of a whole mix (renders and reference recordings alike). Envelope: 5 ms RMS, 1 ms hop,
K-weighting not applied, 150 Hz high-pass (so basses and room rumble do not hide fronts). An onset = the envelope rises
>= 6 dB within 40 ms above the mean of the previous 60 ms, at a level within 20 dB of the file's p95 level. Per onset:
rise (dB) and the time it took (10-90 % amplitude), steepest 1 ms step (dB/ms), and the onset crest (peak in the
first 60 ms minus mean 150-400 ms). Prints medians and p90. Usage: mixonsets.py LABEL=FILE ..."""
import sys, subprocess, numpy as np
from scipy.signal import butter, sosfilt
def dec(p):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '48000', '-f', 'f32le', '-'], capture_output=True)
    return np.frombuffer(r.stdout, np.float32).astype(np.float64)
print('| file | onsets | per min | rise dB med | rise time ms med / p10 | steepest dB/ms med / p90 | onset crest dB med / p90 |')
print('|---|---|---|---|---|---|---|')
for a in sys.argv[1:]:
    lab, p = a.split('=', 1); x = dec(p); sr = 48000
    x = sosfilt(butter(2, 150, 'hp', fs=sr, output='sos'), x)
    h = 48; w = 240
    e = 10 * np.log10(np.convolve(x ** 2, np.ones(w) / w, 'same')[::h] + 1e-14)
    p95 = np.percentile(e[e > e.max() - 60], 95)
    ons = []; i = 60
    while i < len(e) - 420:
        base = 10 * np.log10(np.mean(10 ** (e[i - 60:i] / 10)))
        if e[i] < base + 1.0: i += 1; continue
        j = i + int(np.argmax(e[i:i + 40]))
        if e[j] - base >= 6 and e[j] >= p95 - 20:
            amp = 10 ** (e[i - 5:j + 1] / 20); a0 = 10 ** (base / 20); A = amp.max()
            k10 = np.argmax(amp >= a0 + 0.1 * (A - a0)); k90 = np.argmax(amp >= a0 + 0.9 * (A - a0))
            crest = e[i:i + 60].max() - 10 * np.log10(np.mean(10 ** (e[i + 150:i + 400] / 10)))
            ons.append((e[j] - base, k90 - k10, np.diff(e[i - 5:j + 1]).max(), crest))
            i = j + 150
        else:
            i += 5
    o = np.array(ons); mins = len(x) / sr / 60
    print(f'| {lab} | {len(o)} | {len(o)/mins:.1f} | {np.median(o[:,0]):.1f} | {np.median(o[:,1]):.0f} / {np.percentile(o[:,1],10):.0f} | '
          f'{np.median(o[:,2]):.2f} / {np.percentile(o[:,2],90):.2f} | {np.median(o[:,3]):.1f} / {np.percentile(o[:,3],90):.1f} |')
