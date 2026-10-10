"""Re-fit per-stem dynamic corrections as a straight line in printed-dynamic steps (no per-step zig-zag):
from measurement D (stems_summary) and the corrections/gains that were active in D, estimate each stem's raw
level relative to Violins I per dynamic, fit raw ~ a + b*step, and set corr(step) = -k*b*(step - 6) and the
gain so the median matches the target; then shift so corrections are <= 0 (headroom).
usage: calib_lin.py STEMS_SUMMARY OLD_CONFIG_JSON NEW_CONFIG_JSON"""
import json, sys, numpy as np
S={s['stem']:s for s in json.load(open(sys.argv[1]))['stems']}
old=json.load(open(sys.argv[2])); c=json.load(open(sys.argv[3]))
STEP={"pp":1,"p":2,"mp":3,"mf":4,"f":5,"ff":6,"fff":7}; K=0.8
v=S['Violins I']['level_by_dynamic_LUFS']
for st,t in c["balance_targets_dB"].items():
    if st.startswith('_') or st not in S: continue
    l=S[st]['level_by_dynamic_LUFS']; oc=old["stems"][st].get("dyn_corr_dB",{})
    ds=[d for d in STEP if d in l and d in v and l[d]['n']>=4 and v[d]['n']>=4]
    if len(ds)<2: continue
    xs=np.array([STEP[d] for d in ds],float); cps=sorted((STEP[d],x) for d,x in oc.items())
    oc_at=lambda s: float(np.interp(s,[p[0] for p in cps],[p[1] for p in cps])) if cps else 0.0
    raw=np.array([l[d]['median']-v[d]['median']-oc_at(STEP[d]) for d in ds])
    b=np.polyfit(xs,raw,1)[0] if len(ds)>=3 else 0.0
    b=float(np.clip(b,-2.5,2.5))
    corr={d:round(-K*b*(s-6),2) for d,s in STEP.items()}
    sh=max(corr.values()); corr={d:round(x-sh,2) for d,x in corr.items()}
    dg=float(np.median([t-raw[i]-corr[ds[i]] for i in range(len(ds))]))
    c["stems"][st]["gain_dB"]=round(old["stems"][st]["gain_dB"]+dg,2)
    c["stems"][st]["dyn_corr_dB"]=corr
    print(f"{st:14s} slope vs VlnI {b:+.2f} dB/step  gain {c['stems'][st]['gain_dB']:+.2f}  corr pp {corr['pp']:+.1f} ff {corr['ff']:+.1f}")
json.dump(c,open(sys.argv[3],'w'),indent=1)
