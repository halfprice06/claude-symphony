import sys, glob, os, csv, numpy as np, soundfile as sf
sys.path.insert(0,'/mnt/project-files/symphony/render/tools'); import rtk
bars=list(csv.DictReader(open('/tmp/rcritic-02/r02/bars.csv')))
bt={int(b['bar']):(float(b['t_start']),float(b['t_end'])) for b in bars}
S={}
for p in sorted(glob.glob('/tmp/rcritic-02/wetwav/*.wav')):
    x,sr=sf.read(p,dtype='float64'); k=rtk.k_weight(x,sr); S[os.path.basename(p)[:-4]]=(k**2).sum(1)
sr=48000
def lev(st,a,b):
    e=S[st][int(a*sr):int(b*sr)]; return 10*np.log10(e.mean()+1e-20)-0.691
rolls=[(1,4),(11,14),(41,43),(117,121),(122,130),(144,146),(167,169),(181,182)]
print('roll bars | per bar: timpani minus loudest other stem (dB) [loudest] ; timpani share of mix')
cnt=0;tot=0
for a,b in rolls:
    out=[]
    for bar in range(a,b+1):
        t0,t1=bt[bar]; T=lev('Timpani',t0,t1)
        o=sorted(((lev(s,t0,t1),s) for s in S if s not in ('Timpani','drums')),reverse=True)
        mix=10*np.log10(sum(S[s][int(t0*sr):int(t1*sr)].mean() for s in S)+1e-20)-0.691
        out.append('%d:%+.1f[%s] %.1f'%(bar,T-o[0][0],o[0][1][:6],T-mix)); tot+=1; cnt+= T>o[0][0]
    print(a,b,' '.join(out))
print('bars where timpani is loudest stem:',cnt,'of',tot)
