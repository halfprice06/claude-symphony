import numpy as np, soundfile as sf, glob, os, sys
from scipy.signal import butter, sosfilt
def bands(p,g):
    x,sr=sf.read(p,dtype='float32'); m=x.mean(1).astype(np.float64)*10**(g/20)
    out={}
    for lo,hi in [(20,100),(100,250)]:
        sos=butter(4,[lo,hi],'bandpass',fs=sr,output='sos'); out[(lo,hi)]=(sosfilt(sos,m)**2).sum()
    out['all']=(m**2).sum(); return out
res={}
for lab,d,g in [('r01','/tmp/rcritic-01/wet',-2.2),('r02','/tmp/rcritic-02/wetwav',1.5)]:
    res[lab]={os.path.basename(p)[:-4]:bands(p,g) for p in sorted(glob.glob(d+'/*.wav'))}
for lab in res:
    tot=sum(v['all'] for v in res[lab].values())
    print(lab,'mix 20-100 share %.1f dB, 100-250 %.1f'%(10*np.log10(sum(v[(20,100)] for v in res[lab].values())/tot),10*np.log10(sum(v[(100,250)] for v in res[lab].values())/tot)))
print('stem: 20-100 Hz energy (dB, same absolute scale incl. master gain) r01 -> r02 ; 100-250 Hz r01 -> r02')
for st in res['r02']:
    a=res['r01'].get(st); b=res['r02'][st]
    f=lambda v:10*np.log10(v+1e-20)
    print('%-14s %6.1f -> %6.1f ; %6.1f -> %6.1f'%(st,f(a[(20,100)]) if a else np.nan,f(b[(20,100)]),f(a[(100,250)]) if a else np.nan,f(b[(100,250)])))
