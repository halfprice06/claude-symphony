#!/usr/bin/env python3
"""Compare tools/stems.py summaries (several renders): balance per printed dynamic, steps, inversions, loudest stems,
articulation audio metrics. Spread is computed two ways: against Violins I (critic 1's measure) and against the median
of the string stems (Vln I, Vln II, Vla, Vc) at the same printed dynamic, which is not moved by one stem's melody lift.
Usage: stemcmp.py label stems_summary.json stem_bars.csv [label summary bars ...]"""
import json, sys, csv, numpy as np
from collections import defaultdict
DY = ["pp", "p", "mp", "mf", "f", "ff"]
STR = ["Violins I", "Violins II", "Violas", "Violoncellos"]
a = sys.argv[1:]
for i in range(0, len(a), 3):
    lab, sf, bf = a[i:i + 3]
    d = json.load(open(sf)); S = {s["stem"]: s for s in d["stems"]}; B = d["blend"]
    L = defaultdict(dict); D = defaultdict(dict)
    for r in csv.DictReader(open(bf)):
        if r["loud_LUFS"] in ("", "nan"): continue
        L[int(r["bar"])][r["stem"]] = float(r["loud_LUFS"]); D[int(r["bar"])][r["stem"]] = r["dyn"]
    rel = defaultdict(lambda: defaultdict(list))
    for b in L:
        for st, v in L[b].items():
            dy = D[b][st]
            if dy not in DY: continue
            refs = [L[b][s] for s in STR if s in L[b] and s != st and D[b].get(s) == dy]
            if refs: rel[st][dy].append(v - np.median(refs))
    print(f"\n## {lab}")
    print(f"balance inversions {B['balance_inversions_n']}; loudest-minus-second median {B['loudest_minus_second_dB_median']} dB; "
          f"bars one stem leads by >=6 dB {B['bars_where_one_stem_leads_by_6dB_plus']}; loudest counts {dict(list(B['loudest_stem_count'].items())[:7])}")
    sp1, sp2 = [], []
    print("| stem | dB/step | vs Vln I by dyn pp..ff | spread | vs string median by dyn pp..ff (bars) | spread |")
    print("|---|---|---|---|---|---|")
    v1 = S.get("Violins I", {}).get("level_by_dynamic_LUFS", {})
    for st, s in sorted(S.items()):
        if st in ("drums",) or st.startswith("Harp"): continue
        lv = s["level_by_dynamic_LUFS"]
        r1 = [lv[x]["median"] - v1[x]["median"] if x in lv and x in v1 and lv[x]["n"] >= 2 and v1[x]["n"] >= 2 else np.nan for x in DY]
        r2 = [np.median(rel[st][x]) if len(rel[st][x]) >= 2 else np.nan for x in DY]
        f1 = [x for x in r1 if not np.isnan(x)]; f2 = [x for x in r2 if not np.isnan(x)]
        s1 = max(f1) - min(f1) if len(f1) >= 2 else np.nan; s2 = max(f2) - min(f2) if len(f2) >= 2 else np.nan
        if st != "Violins I" and not np.isnan(s1): sp1.append(s1)
        if not np.isnan(s2): sp2.append(s2)
        fmt = lambda r: " ".join("." if np.isnan(x) else f"{x:+.1f}" for x in r)
        print(f"| {st} | {s['dB_per_dynamic_step']} | {fmt(r1)} | {s1:.1f} | {fmt(r2)} | {s2:.1f} |")
    print(f"median spread vs Vln I {np.median(sp1):.1f} dB (stems >6: {sum(1 for x in sp1 if x>6)}); vs string median {np.median(sp2):.1f} dB (stems >6: {sum(1 for x in sp2 if x>6)})")
    print("articulation audio: stem | accent boost (n) | staccato sus75 / audible ratio (n) | detached audible ratio | slurred dip / detached dip | tremolo env std dB / peaks/s (n) | pizz audible s / ratio (n)")
    for st, s in sorted(S.items()):
        A = s["articulation_audio"]
        g = lambda k, f: A.get(k, {}).get(f)
        print(f"  {st}: acc {A.get('accent_peak_boost_dB_median')} ({A.get('accent_boost_n')}) | stacc {g('staccato','sustain75_dB_median')} / {g('staccato','audible_ratio_median')} ({g('staccato','n')}) | det {g('detached','audible_ratio_median')} | dips {A.get('slurred_boundary_dip_dB_median')} / {A.get('detached_boundary_dip_dB_median')} | trem {g('tremolo','trem_env_std_dB_median')} / {g('tremolo','trem_peaks_per_s_median')} ({g('tremolo','n')}) | pizz {g('pizz','audible_len_s_median')} / {g('pizz','audible_ratio_median')} ({g('pizz','n')})")
