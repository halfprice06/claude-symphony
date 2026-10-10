# quick timpani-only test: articulate + Timpani stem; per long roll: start level (0.4-0.8 s), end change, max
import sys, os, subprocess, csv, numpy as np, soundfile as sf
R="/mnt/project-files/symphony/render"; sys.path.insert(0,R+"/r04"); sys.path.insert(0,R+"/r04/lib"); sys.path.insert(0,R+"/tools")
import rtk
W, score, cfgp, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
subprocess.run([sys.executable, R+"/r04/articulate.py", W+"/score.midi", W+"/notes.csv", cfgp, out+"/render.midi", "--score", score], check=True, stdout=subprocess.DEVNULL)
import importlib.util
spec=importlib.util.spec_from_file_location("render", R+"/r04/render.py"); rd=importlib.util.module_from_spec(spec); spec.loader.exec_module(rd)
mids = rd.split_stems(out+"/render.midi", out)
subprocess.run([sys.executable, R+"/r04/stem.py", mids["Timpani"], out+"/Timpani.wav", "--config", cfgp], check=True)
x, sr = sf.read(out+"/Timpani.wav", always_2d=True)
k = rtk.k_weight(x, sr); e = (k**2).sum(1)
def lev(a,b): i,j=int(a*sr),int(b*sr); return 10*np.log10(e[i:j].mean()+1e-20)-0.691
mi = rtk.midi_info(W+"/score.midi")
for r in csv.DictReader(open(W+"/notes.csv")):
    if r['staff'].startswith('Timp') and 'tremolo' in r['arts']:
        t0=float(r['t_on_s']); L=float(r['notated_s']); b0=int(r['bar'])
        blen = mi["bar_s"][b0]-mi["bar_s"][b0-1]
        if L <= blen*1.01: continue
        st=lev(t0+0.4,t0+0.8); en=lev(t0+L-0.8,t0+L); mid=lev(t0+0.8, t0+L)
        print(f"bar {b0} {r['dyn']:4s} {r['hairpin'] or '-':7s} L {L:5.1f}  start {st:6.1f}  body {mid:6.1f}  end {en:6.1f}  change {en-st:+5.1f}")
