# compare stems: stemab.py notes.csv midi staff wav1 [wav2 ...]  (tools/stems.py analyse_stem on each)
import sys, csv, json
sys.path.insert(0, '/mnt/project-files/symphony/render/tools')
import stems, rtk, numpy as np
nf, midi, staff = sys.argv[1:4]
rows = [r for r in csv.DictReader(open(nf)) if stems.key(r['midi_track'] or r['staff']) == staff]
for r in rows:
    for k in ('t_on_s', 'notated_s'): r[k] = float(r[k])
    r['t_off_s'] = float(r['t_off_s']) if r['t_off_s'] else None
    r['bar'] = int(r['bar']); r['midi_vel'] = int(r['midi_vel']) if r['midi_vel'] else ''
bars = rtk.midi_info(midi)['per_bar']
for w in sys.argv[4:]:
    o, br = stems.analyse_stem(staff, w, rows, bars, None)
    A = o['articulation_audio']; g = lambda c, k: A.get(c, {}).get(k)
    print(w.split('/')[-1], 'sounding', o['loud_while_sounding_LUFS'], 'dB/step', o['dB_per_dynamic_step'],
          {d: v['median'] for d, v in o['level_by_dynamic_LUFS'].items()},
          '| det ratio', g('detached', 'audible_ratio_median'), 'stacc75', g('staccato', 'sustain75_dB_median'), 'stacc ratio', g('staccato', 'audible_ratio_median'),
          'acc', A.get('accent_peak_boost_dB_median'), A.get('accent_boost_n'), 'attack ms', g('detached', 'attack_ms_median_clean_onsets'), 'centroid', o['centroid_Hz'])
