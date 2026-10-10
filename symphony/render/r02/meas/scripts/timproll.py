"""Timpani against the other stems in every roll longer than one bar (Dan's rule, BRIEF.md 2026-10-09).
Per bar K-weighted loudness of each stem WAV (whole bar, not only while sounding), from the stems the mix uses.
usage: timproll.py notes.csv MIDI STEMDIR"""
import csv, sys, glob, os, numpy as np, soundfile as sf
sys.path.insert(0,'/mnt/project-files/symphony/render/tools'); import rtk
rows=list(csv.DictReader(open(sys.argv[1]))); mi=rtk.midi_info(sys.argv[2]); bs=mi['bar_s']
rolls=[]
for r in rows:
    if r['staff']=='Timpani' and 'tremolo' in r['arts'] and int(r['notated_ticks'])>1536:
        b0=int(r['bar']); nb=int(np.ceil(int(r['notated_ticks'])/1536)); rolls.append((b0,nb,r))
need=sorted({b for b0,nb,_ in rolls for b in range(b0,b0+nb)})
L={}
for p in sorted(glob.glob(os.path.join(sys.argv[3],'*.wav'))):
    st=os.path.basename(p)[:-4].replace('_',' ')
    if st=='drums': continue
    x,sr=sf.read(p,dtype='float32'); k=rtk.k_weight(x.astype(np.float64),sr) if x.ndim==2 else None
    L[st]={b:10*np.log10((k[int(bs[b-1]*sr):int(bs[b]*sr)]**2).sum(1).mean()+1e-20)-0.691 for b in need}
print("| roll bars | printed dyn (hairpin) | length s | timpani LUFS (median of bars) | loudest other stem | timpani minus loudest other (median, max) dB | bars where timpani is loudest |")
print("|---|---|---|---|---|---|---|")
tot=loud=0
for b0,nb,r in rolls:
    d=[];t=[];who=[];nl=0
    for b in range(b0,b0+nb):
        o={k:v[b] for k,v in L.items() if k!='Timpani'}; k=max(o,key=o.get)
        d.append(L['Timpani'][b]-o[k]); t.append(L['Timpani'][b]); who.append(k); nl+=d[-1]>0
    tot+=len(d); loud+=nl
    print(f"| {b0}-{b0+nb-1} | {r['dyn']} ({r['hairpin'] or '-'}) | {float(r['notated_s']):.1f} | {np.median(t):.1f} | {max(set(who),key=who.count)} | {np.median(d):+.1f}, {max(d):+.1f} | {nl} of {len(d)} |")
print(f"\ntimpani loudest stem in {loud} of {tot} roll bars")
