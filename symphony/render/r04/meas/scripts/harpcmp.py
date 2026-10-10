import sys, csv, numpy as np, soundfile as sf
from collections import defaultdict
from scipy.signal import welch
sys.path.insert(0,"/mnt/project-files/symphony/render/r04/lib"); import balance, rtk
W, a, b = sys.argv[1:4]
mi = rtk.midi_info(W+"/score.midi"); bars = [(x["bar"], x["t_start"], x["t_end"]) for x in mi["per_bar"]]
rows = list(csv.DictReader(open(W+"/notes.csv")))
for st in ("Harp RH", "Harp LH"):
    rr = [r for r in rows if balance.key(r["midi_track"] or r["staff"]) == st]
    pd = balance.printed_dyn(rr).get(st, {})
    out = []
    for d in (a, b):
        x, sr = sf.read(f"{d}/{st.replace(' ','_')}.wav", always_2d=True)
        lv, _ = balance.bar_levels(x, sr, rr, bars)
        byd = defaultdict(list)
        for bb, v in lv.items():
            if bb in pd: byd[balance.DY[pd[bb]]].append(v)
        f, P = welch(x.mean(1), fs=sr, nperseg=8192); hf = 10*np.log10(P[f>6000].sum()/P.sum())
        out.append(({k: round(float(np.median(v)),1) for k, v in byd.items()}, round(hf,1), {k: len(v) for k,v in byd.items()}))
    print(st, "before", out[0][0], "hf", out[0][1], "| after", out[1][0], "hf", out[1][1], out[1][2])
