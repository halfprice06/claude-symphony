"""Fit stem gains and per-dynamic corrections from a stems.py run (relative to Violins I at each printed
dynamic). usage: calib.py STEMS_SUMMARY CONFIG [gain_rate corr_rate]"""
import json, sys, numpy as np
S={s['stem']:s for s in json.load(open(sys.argv[1]))['stems']}
cfgp=sys.argv[2]; c=json.load(open(cfgp))
gr=float(sys.argv[3]) if len(sys.argv)>3 else 0.8; cr=float(sys.argv[4]) if len(sys.argv)>4 else 0.6
T=c["balance_targets_dB"]
DY=["pp","p","mp","mf","f","ff","fff"]
v=S['Violins I']['level_by_dynamic_LUFS']
for st,t in T.items():
    if st not in S: continue
    l=S[st]['level_by_dynamic_LUFS']
    diff={d:t-(l[d]['median']-v[d]['median']) for d in DY if d in l and d in v and l[d]["n"]>=4 and v[d]["n"]>=4}
    if not diff: continue
    med=float(np.median(list(diff.values())))
    sc=c["stems"][st]; sc["gain_dB"]=round(sc["gain_dB"]+gr*med,2)
    corr=sc.get("dyn_corr_dB",{})
    for d,x in diff.items():
        corr[d]=round(float(np.clip(corr.get(d,0)+cr*(x-med),-6,6)),2)
    sc["dyn_corr_dB"]=corr
    print(f"{st:14s} gain {sc['gain_dB']:+6.2f} (step {gr*med:+.2f}) corr {corr}")
json.dump(c,open(cfgp,'w'),indent=1)
