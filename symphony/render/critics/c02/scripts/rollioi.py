import sys, glob, os, numpy as np, soundfile as sf
from scipy.signal import find_peaks, butter, sosfiltfilt
D='/mnt/project-files/symphony/render/assets/vpo3/libs/Other/Samples/Timpani/'
for p in sorted(glob.glob(D+'timpani-roll-*.wav')):
    x,sr=sf.read(p,always_2d=True); m=x.mean(1)
    # onset strength: high-passed (>200 Hz) energy, 2 ms hop
    sos=butter(2,200,'highpass',fs=sr,output='sos'); y=sosfiltfilt(sos,m)
    h=int(0.002*sr); k=len(y)//h
    e=10*np.log10((y[:k*h].reshape(k,h)**2).mean(1)+1e-12)
    d=np.diff(e,prepend=e[0]); d[d<0]=0
    pk,_=find_peaks(np.convolve(d,np.ones(3)/3,'same'),distance=int(0.045/0.002),prominence=2)
    t=pk*0.002; t=t[(t>0.5)&(t<5.0)]
    ioi=np.diff(t)
    print(os.path.basename(p)[13:16],'strokes %d rate %.1f/s IOI median %.1f ms, CV %.1f %%, p10-p90 %.0f-%.0f ms'%(len(t),1/np.median(ioi),1000*np.median(ioi),100*ioi.std()/ioi.mean(),1000*np.percentile(ioi,10),1000*np.percentile(ioi,90)))
