import sys, glob, os, numpy as np, soundfile as sf
sys.path.insert(0,'/mnt/project-files/symphony/render/r02')
import sfzplay
from scipy.signal import welch
D='/mnt/project-files/symphony/render/assets/vpo3/libs/Other/Samples/Timpani/'
for p in sorted(glob.glob(D+'timpani-roll-*.wav')):
    x,sr=sf.read(p,always_2d=True); m=x.mean(1)
    lp=sfzplay._read_wav_loop(p)
    h=int(0.005*sr); k=len(m)//h
    e=np.sqrt((m[:k*h].reshape(k,h)**2).mean(1)+1e-12)
    # envelope modulation spectrum over the loop region (or steady part)
    a=int(0.5*sr)//h; b=k
    env=e[a:b]; env=env/env.mean()-1
    f,P=welch(env,fs=1/0.005,nperseg=min(len(env),512))
    sel=(f>3)&(f<40)
    pk=f[sel][np.argmax(P[sel])]
    ratio=10*np.log10(P[sel].max()/np.median(P[sel]))
    edb=20*np.log10(e[a:b]); 
    print(os.path.basename(p), 'sr',sr,'len %.2fs'%(len(m)/sr),'loop',None if lp is None else ('%.2f-%.2fs'%(lp[0]/sr,lp[1]/sr)),
      'env std %.2f dB'%edb.std(),'mod peak %.1f Hz, %.1f dB over median'%(pk,ratio))
