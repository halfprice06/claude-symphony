import csv, numpy as np, soundfile as sf, sys
from scipy.signal import welch, butter, sosfiltfilt
sys.path.insert(0,'/mnt/project-files/symphony/render/r02'); import sfzplay
rows=[r for r in csv.DictReader(open('/tmp/rcritic-02/notes.csv')) if r['staff']=='Timpani' and 'tremolo' in r['arts']]
def env(path):
    x,sr=sf.read(path,dtype='float32'); m=x.mean(1)
    return m,sr
m,sr=env(sys.argv[1])
h=int(0.01*sr); k=len(m)//h
E=(m[:k*h].reshape(k,h)**2).mean(1)
sos=butter(4,4000,'highpass',fs=sr,output='sos')
samp={43:('G2',43),44:('G2',43),48:('C3',48),51:('D3',50),46:('A2',45)}
D='/mnt/project-files/symphony/render/assets/vpo3/libs/Other/Samples/Timpani/'
print('bar dyn hp len | start dB, end dB, settle | modpeak Hz, prom dB | autocorr max (lag s) | seam HF jump dB')
for r in rows:
    L=float(r['notated_s']); 
    if L<1.9: continue
    t0=float(r['t_on_s']); t1=t0+L
    a=int((t0+0.35)/0.01); b=int(t1/0.01)
    e=E[a:b]; edb=10*np.log10(e+1e-14)
    st=edb[:50].mean(); en=edb[-100:].mean() if len(edb)>150 else edb[-50:].mean()
    lin=np.sqrt(e); lin=lin/lin.mean()-1
    # modulation spectrum on 10ms envelope (Nyquist 50 Hz)
    f,P=welch(lin,fs=100,nperseg=min(len(lin),256))
    s=(f>=3)&(f<=40); pk=f[s][np.argmax(P[s])]; prom=10*np.log10(P[s].max()/np.median(P[s]))
    # autocorr of detrended dB envelope, lags 1.5-6 s
    d=edb-np.convolve(edb,np.ones(51)/51,'same')
    d=d[25:-25]; d=d-d.mean()
    ac=np.correlate(d,d,'full')[len(d)-1:]; ac/=ac[0]
    lo,hi=150,min(600,len(d)-50)
    acm=(ac[lo:hi].max(), (lo+np.argmax(ac[lo:hi]))*0.01) if hi>lo+10 else (np.nan,np.nan)
    # loop seam times
    key=int(r['pitch']); name,kc=samp.get(key,('G2',43))
    p=D+f'timpani-roll-{name}-PB-loop.wav'; ls,le=sfzplay._read_wav_loop(p)
    ratio=2**((key-kc)/12)*44100/sr
    seams=[]; ts=t0+ le/44100/ (ratio*sr/44100)  # time to reach loop end
    per=(le-ls+1)/44100/(ratio*sr/44100)
    while ts<t1: seams.append(ts); ts+=per
    jumps=[]
    for ts in seams:
        i=int(ts*sr); seg=sosfiltfilt(sos,m[i-int(0.2*sr):i+int(0.2*sr)])
        w=int(0.005*sr); q=(seg[:len(seg)//w*w].reshape(-1,w)**2).mean(1); c=len(q)//2
        jumps.append(10*np.log10(q[c-2:c+3].max()/np.median(q)))
    print(r['bar'],r['dyn'],r['hairpin'] or '-', '%.1f'%L,'| %.1f %.1f %+.1f | %.1f %.1f | %.2f (%.2f) | seams %d, max %.1f'%(st,en,en-st,pk,prom,acm[0],acm[1],len(seams),max(jumps) if jumps else np.nan))
