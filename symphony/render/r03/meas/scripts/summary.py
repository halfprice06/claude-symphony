#!/usr/bin/env python3
"""Key numbers of one meas.sh folder (r03 NOTES tables). Usage: summary.py OUTDIR"""
import json, sys, re, os
O = sys.argv[1]
m = json.load(open(os.path.join(O, 'mix/metrics.json'))); L = m['loudness']; P = L['S_percentiles_rel_I']
print('LRA', L['LRA_LU'], '| S p10/p50/p95/p99/max', P['p10'], P['p50'], P['p95'], P['p99'], L['S_max_rel_I'], '| TP', m['ffmpeg_ebur128']['true_peak_dBTP'])
print('bands', m['spectrum']['band_shares_dB'])
import numpy as np
f = np.array(m['spectrum']['third_octave_Hz']); v = np.array(m['spectrum']['third_octave_dB_rel_total'])
print('third-octave 63 Hz / 12.7 kHz', round(float(v[np.argmin(abs(f - 63))]), 1), round(float(v[np.argmin(abs(f - 12700))]), 1))
b = m['brightness']['loud_minus_soft_shape_dB_at_Hz']; print('loud-soft 5k/10k', b.get('5040'), b.get('10079'))
s = m['stereo']; print('corr', s['corr_LR'], s['corr_high>4k'], 'spread', s['pan_spread_std'])
print('cutoffs', m['cutoff_decays']['median_t_to_minus20dB_s'], m['cutoff_decays']['median_RT60_est_s'], '| onsets', m['onsets']['best_lag_ms_audio_after_midi'], m['onsets']['peak_corr'])
for f in ('bardyn.txt', 'clicks_premaster.txt'):
    print(open(os.path.join(O, f)).read().strip())
print([l for l in open(os.path.join(O, 'melody.md')) if l.startswith('marked')][0].strip())
print(open(os.path.join(O, 'rolls.txt')).read().strip().splitlines()[-1])
for l in open(os.path.join(O, 'stemcmp.md')):
    if l.startswith('balance') or l.startswith('median spread'): print(l.strip())
print(open(os.path.join(O, 'lowstem.txt')).readline().strip())
