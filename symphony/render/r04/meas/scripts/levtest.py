import sys, subprocess, re, numpy as np, soundfile as sf
sys.path.insert(0,"/mnt/project-files/symphony/render/r04/lib"); import leveler, rtk
def stats(path):
    r = subprocess.run(["ffmpeg","-nostats","-i",path,"-af","ebur128","-f","null","-"],capture_output=True,text=True).stderr
    s=r[r.rfind("Summary:"):]; I=float(re.search(r"I:\s+(-?[\d.]+) LUFS",s).group(1)); L=float(re.search(r"LRA:\s+(-?[\d.]+) LU",s).group(1))
    x,sr=sf.read(path,always_2d=True); t,S=rtk.loudness_series(x,sr,3.0,0.1); S=S[S>I-20-10]  # rough gate
    return I,L,np.percentile(S-I,[10,50,95]),(S-I).max()
for p in sys.argv[1:]:
    x,sr=sf.read(p,always_2d=True); I,L,pc,mx=stats(p); print(p,"before I %.1f LRA %.1f p10/50/95 %s max %.1f"%(I,L,np.round(pc,1),mx))
    for th,ra in ((6,2),(5,2),(6,3)):
        y,gm=leveler.apply(x,sr,I,threshold_LU=th,ratio=ra); sf.write('/tmp/a4/lv.wav',y.astype(np.float32),sr,subtype='FLOAT')
        I2,L2,pc2,mx2=stats('/tmp/a4/lv.wav'); print("  th %d ratio %d: I %.1f LRA %.1f p10/50/95 %s max %.1f (rel new I) min gain %.1f"%(th,ra,I2,L2,np.round(pc2,1),mx2,gm))
