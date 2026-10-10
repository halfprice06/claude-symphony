#!/usr/bin/env python3
"""critic 5: mix table (markdown) from tools/measure.py metrics.json folders. Usage: mixtable.py label=dir ... > out.md
Third-octave columns are relative to the mean of the four Brahms references (I and II of 1 and 4)."""
import sys, json, numpy as np
R = '/mnt/project-files/symphony/render/critics'
refs = [f'{R}/c00/ref_brahms1_i_musopen', f'{R}/c00/ref_brahms4_i_musopen', f'{R}/c04/ref_brahms1_ii_musopen', f'{R}/c04/ref_brahms4_ii_musopen']
def load(d):
    import os
    p = d + '/metrics.json' if os.path.exists(d + '/metrics.json') else d + '/mix/metrics.json'
    return json.load(open(p))
F = load(refs[0])['spectrum']['third_octave_Hz']
mean = np.mean([load(r)['spectrum']['third_octave_dB_rel_total'] for r in refs], axis=0)
bands = [62.5, 78.7, 250.0, 315.0, 793.7, 2519.8, 3174.8, 6349.6, 8000.0]
cols = [a.split('=', 1) for a in sys.argv[1:]]
rows = {}
for lab, d in cols:
    m = load(d); L = m['loudness']; E = m['ffmpeg_ebur128']; S = L['S_percentiles_rel_I']; sp = m['spectrum']
    b = sp['band_shares_dB']; st = m['stereo']; pk = m['peaks']
    t = np.array(sp['third_octave_dB_rel_total']) - mean
    rows.setdefault('integrated LUFS / true peak dBTP', []).append(f"{E['I_LUFS']} / {E['true_peak_dBTP']}")
    rows.setdefault('LRA LU', []).append(f"{E['LRA_LU']}")
    rows.setdefault('short-term p10 / p50 / p95 rel I', []).append(f"{S['p10']} / {S['p50']} / {S['p95']}")
    rows.setdefault('short-term p99 / max rel I', []).append(f"{S['p99']} / {L['S_max_rel_I']}")
    rows.setdefault('share < 100 Hz / 2-6 kHz / > 6 kHz dB', []).append(f"{b['20-100Hz']} / {b['2000-6000Hz']} / {b['6000-20000Hz']}")
    rows.setdefault('1/3 oct vs Brahms mean: ' + ' / '.join(str(int(round(x))) for x in bands), []).append(
        ' / '.join(f"{t[F.index(x)]:+.1f}" for x in bands))
    rows.setdefault('L/R corr (low/mid/high); pan spread', []).append(
        f"{st['corr_LR']:.2f} ({st['corr_low<250']:.2f}/{st['corr_mid250-4k']:.2f}/{st['corr_high>4k']:.2f}); {st['pan_spread_std']:.2f}")
    rows.setdefault('clipped samples; crest dB', []).append(f"{pk['samples_abs_gt_1.0']}; {pk['crest_factor_dB']}")
print('| | ' + ' | '.join(l for l, _ in cols) + ' |')
print('|---|' + '---|' * len(cols))
for k, v in rows.items():
    print(f'| {k} | ' + ' | '.join(v) + ' |')
