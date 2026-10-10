import sys, json, numpy as np, soundfile as sf
sys.path.insert(0,"/mnt/project-files/symphony/render/r04/lib"); sys.path.insert(0,"/mnt/project-files/symphony/render/tools")
import rtk, busq
ref = {}
for l in open("/mnt/project-files/symphony/render/critics/c03/ltas_vs_refs.txt").read().splitlines()[2:]:
    p=l.split(); ref[float(p[0])]=(float(p[5])+float(p[6]))/2
eq = json.loads(sys.argv[1])
for w in sys.argv[2:]:
    x, sr = sf.read(w, always_2d=True); m = x.mean(1)
    f, P = rtk.psd(m, sr)
    for lab, PP in (("before", P), ("after", P*busq.power_response(eq, sr, np.maximum(f,1e-3)))):
        b = rtk.third_octave(f, PP); bs = rtk.band_shares(f, PP)
        d = {fc: b[i]-ref[round(fc,0)] if round(fc,0) in ref else None for i, fc in enumerate(rtk.THIRD_OCT)}
        sel = [62,99,125,250,315,630,794,4000,5040,6350,8000,10079]
        def g(fc): 
            k=min(d, key=lambda z: abs(z-fc)); return d[k]
        print(w.split('/')[-2], lab, "<100 %.1f"%bs['20-100Hz'], " ".join("%d:%+.1f"%(fc,g(fc)) for fc in sel))
