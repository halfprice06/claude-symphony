import sys, subprocess, numpy as np
from scipy.signal import butter, sosfilt
def dec(p):
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','2','-ar','48000','-'],capture_output=True)
    return np.frombuffer(r.stdout,np.float32).reshape(-1,2)
for p in sys.argv[1:]:
    x=dec(p); sr=48000
    sos=butter(4,8000,'highpass',fs=sr,output='sos')
    h=sosfilt(sos,x.mean(1).astype(np.float64))
    w=int(0.05*sr); n=len(h)//w
    hb=h[:n*w].reshape(n,w); rms=np.sqrt((hb**2).mean(1))+1e-9; pk=np.abs(hb).max(1)
    # local reference: median rms of neighbouring 11 blocks
    from scipy.ndimage import median_filter
    ref=median_filter(rms,11)+1e-9
    full=np.sqrt((x.mean(1)[:n*w].reshape(n,w)**2).mean(1))
    cand=np.where((pk/ref>12)&(pk>1e-3))[0]
    print(p.split('/')[-2]+'/'+p.split('/')[-1],'blocks',n,'click candidates (HF peak >12x local HF rms):',len(cand),'at s',[round(c*0.05,2) for c in cand[:15]])
    dc=x.mean(0); print('  DC offset',dc)
