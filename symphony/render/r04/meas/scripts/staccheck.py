# per staccato/detached note of one staff: peak and level at +250 ms, audible length (to -20 dB) on a stem wav
import sys, csv, numpy as np, soundfile as sf, re
nf, wav, staff = sys.argv[1:4]
x, sr = sf.read(wav, always_2d=True); x = x.mean(1); h = int(0.01*sr)
e = x[:len(x)//h*h].reshape(-1,h); e = 10*np.log10((e**2).mean(1)+1e-20)
rows=[r for r in csv.DictReader(open(nf)) if r['staff']==staff]
ons=np.array(sorted(set(float(r['t_on_s']) for r in rows)))
res={'stac':[], 'det':[]}
for r in rows:
    t=float(r['t_on_s']); L=float(r['notated_s']); arts=r['arts'].split('|') if r['arts'] else []
    if ((ons>t+1e-3)&(ons<t+float(sys.argv[4] if len(sys.argv)>4 else 0.4))).any(): continue
    cls='stac' if 'staccato' in arts else ('det' if not arts and r['slur']=='' and L<0.6 else None)
    if not cls: continue
    i=int(t*100); pk=e[i:i+12].max(); a250=e[i+25]-pk
    below=np.nonzero(e[i+3:i+300]<pk-20)[0]; aud=(below[0]+3)*0.01 if len(below) else np.nan
    res[cls].append((pk,a250,aud,aud/L))
for k,v in res.items():
    if v: v=np.array(v); print(k, len(v), "peak %.1f  +250ms %.1f  audible %.2f s  ratio %.2f"%tuple(np.nanmedian(v,0)))
