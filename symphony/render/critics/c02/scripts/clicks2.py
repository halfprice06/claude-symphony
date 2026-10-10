import sys, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
from scipy.ndimage import median_filter
for p in sys.argv[1:]:
    x,sr=sf.read(p,dtype='float32'); m=x.mean(1).astype(np.float64)
    sos=butter(4,6000,'highpass',fs=sr,output='sos'); h=sosfilt(sos,m)
    w=int(0.001*sr); n=len(h)//w
    e=(h[:n*w].reshape(n,w)**2).mean(1)+1e-16
    ref=median_filter(e,41)
    full=(m[:n*w].reshape(n,w)**2).mean(1)
    fullref=np.convolve(full,np.ones(41)/41,'same')+1e-16
    jump=10*np.log10(e/ref)
    # isolated: next frames drop back within 3 ms; signal must be audible: HF frame above -90 dBFS and wideband level > -70
    cand=np.nonzero((jump>15)&(10*np.log10(e)>-95)&(10*np.log10(fullref)>-80))[0]
    iso=[c for c in cand if c+4<n and jump[c+4]<6]
    # merge
    ev=[]; 
    for c in iso:
        if not ev or c-ev[-1]>20: ev.append(c)
    print(p.split('/')[-1],'isolated HF spikes (>15 dB over 41 ms median, back within 4 ms):',len(ev),[round(c*0.001,3) for c in ev[:12]], 'max jump %.0f dB'%(max([jump[c] for c in ev]) if ev else 0))
