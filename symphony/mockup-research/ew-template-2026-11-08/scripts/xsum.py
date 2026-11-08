"""Cross-file summary from smf2 JSON outputs, grouped by instrument family from track names."""
import json, glob, re, statistics as st, collections, sys
FAM = [('perc', r'timp|drum|snare|cymbal|piatti|tam|taiko|boom|hit|perc|tom|gong|triangle|shaker|ride|kit|anvil|stick|chime|slap|rain|glock|marimba|vib|celest|bell|xylo|crotal'),
       ('keys/harp', r'harp|piano|steinway|keys|celeste|dulcimer|guitar|kantele|mandolin|accordion|harmonium|typewriter'),
       ('str-short', r'spic|stac|short|pizz|marc|portato|5/0|\bss\b shorts'),
       ('brass', r'horn|trumpet|\btp|trombone|\btbn|bones|tuba|\btb1|brass|cimbasso'),
       ('winds', r'flute|\bfl|oboe|\bob|clarinet|\bcl|bassoon|\bbsn|piccolo|pcl|winds|recorder|whistle|ney|english'),
       ('str-long', r'viol|vln|cello|\bvc|\bva\b|\bva[ab]\b|\bv[12]|bass|string|css|scs|legato|leg\b|trem|flaut|harmonic|\bcb\b|ensemble|ens|albion|mural|ark|lacrim|choir')]
def fam(n):
    n = (n or '').lower()
    for f, rx in FAM:
        if re.search(rx, n): return f
    return 'other'
rows = collections.defaultdict(lambda: collections.defaultdict(list))
perfile = {}
for fn in sorted(glob.glob('reports/*.json')):
    D = json.load(open(fn))
    for name, d in D.items():
        tr = d['tracks']; perfile[name] = tr
        for t in tr:
            if t['n'] < 15: continue
            f = fam(t['name'])
            R = rows[f]
            R['files'].append(name)
            R['ongrid'].append(t['ongrid'] * 100)
            if t['mode_share'] >= 0.3: R['shift'].append(t['mode_ms'])
            if t['ov_med'] is not None and t['ov_n'] >= 10: R['ov'].append(t['ov_med'])
            if t['rep_med'] is not None and t['rep_n'] >= 5 and t['rep_med'] > 0: R['rep'].append(t['rep_med'])
            R['vel_iqr'].append(t['vel_iqr'][1] - t['vel_iqr'][0]); R['vel_med'].append(t['vel_med'])
            l1 = t['lanes'].get('1')
            if l1 and l1['ev'] > 50: R['cc1rate'].append(l1['rate']); R['cc1step'].append(l1['step'])
            if t.get('cc1_vel_r') is not None: R['r'].append(t['cc1_vel_r'])
def q(v, f="{:.0f}"):
    v = sorted(v)
    return f"{f.format(st.median(v))} [{f.format(v[len(v)//4])}..{f.format(v[3*len(v)//4])}] n={len(v)}" if v else '-'
for f, R in sorted(rows.items()):
    print(f"\n## {f}: {len(R['ongrid'])} tracks from {len(set(R['files']))} files")
    print(f"  onsets on 16th grid %: {q(R['ongrid'])}")
    print(f"  constant shift (tracks whose most common offset covers >=30% of notes), ms: {q(R['shift'])}")
    print(f"  legato overlap ms (median per track): {q(R['ov'])}")
    print(f"  repeated-note gap ms: {q(R['rep'])}")
    print(f"  velocity median {q(R['vel_med'])}; velocity IQR width {q(R['vel_iqr'])}")
    print(f"  CC1 events/s {q(R['cc1rate'], '{:.1f}')}; CC1 median step {q(R['cc1step'])}; r(velocity, CC1 at onset) {q(R['r'], '{:.2f}')}")
print("\n## per file: share of tracks mostly off-grid (<20% on grid), and shifts used")
for name, tr in perfile.items():
    tr = [t for t in tr if t['n'] >= 15]
    off = sum(1 for t in tr if t['ongrid'] < 0.2) / len(tr) * 100
    sh = collections.Counter((t['mode_ms'] if t['mode_share'] >= .3 else None) for t in tr)
    print(f"{name}: {len(tr)} tracks, {off:.0f}% mostly off-grid; shifts {dict(sh.most_common(6))}")
