"""Summary of one measurement folder against r01 (critic 1's numbers). usage: report.py DIR [REFDIR]"""
import json, sys, numpy as np
D=sys.argv[1]; R=sys.argv[2] if len(sys.argv)>2 else '/mnt/project-files/symphony/render/critics/c01/stems_r01_wet'
DY=["pp","p","mp","mf","f","ff"]
def load(p):
    d=json.load(open(p+'/stems_summary.json')); return {s['stem']:s for s in d['stems']}, d['blend']
S,B=load(D+'/stems'); S0,B0=load(R)
def rel(S):
    v=S['Violins I']['level_by_dynamic_LUFS']; out={}
    for k,s in S.items():
        l=s['level_by_dynamic_LUFS']; out[k]={d:round(l[d]['median']-v[d]['median'],1) for d in DY if d in l and d in v and l[d]['median'] is not None}
    return out
r,r0=rel(S),rel(S0)
print("stem | rel VlnI pp p mp mf f ff | spread (r01) | dB/step (r01) | acc boost (r01) | stacc75 | dip slur/det")
sp=[];sp0=[]
for k in sorted(S):
    a=S[k]['articulation_audio']; a0=S0.get(k,{}).get('articulation_audio',{})
    vals=list(r[k].values()); v0=list(r0.get(k,{}).values())
    s=max(vals)-min(vals) if len(vals)>1 else None; s0=max(v0)-min(v0) if len(v0)>1 else None
    if s is not None and k!='Violins I': sp.append(s)
    if s0 is not None and k!='Violins I': sp0.append(s0)
    st=a.get('staccato',{}).get('sustain75_dB_median')
    print(f"{k:14s}|"+" ".join(f"{r[k].get(d,float('nan')):+5.1f}" for d in DY)+f" | {s if s is None else round(s,1)} ({s0 if s0 is None else round(s0,1)}) | {S[k]['dB_per_dynamic_step']} ({S0.get(k,{}).get('dB_per_dynamic_step')}) | {a.get('accent_peak_boost_dB_median')} ({a0.get('accent_peak_boost_dB_median')}) n{a.get('accent_boost_n')} | {st} | {a.get('slurred_boundary_dip_dB_median')}/{a.get('detached_boundary_dip_dB_median')}")
print("median spread", round(float(np.median(sp)),1), "(r01", round(float(np.median(sp0)),1),")")
for k in ['balance_inversions_n','loudest_minus_second_dB_median']: print(k, B[k], '(r01', B0[k],')')
print('loudest counts', B['loudest_stem_count'])
print('top inversions', B['balance_inversions_top_pairs'][:8])
