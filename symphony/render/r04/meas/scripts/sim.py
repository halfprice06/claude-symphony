# offline balance simulator: levels from a no-balance measurement (stems.py stem_bars.csv + barlev whole-bar), r04 balance.compute
import sys, csv, json, re, numpy as np
from collections import defaultdict
sys.path.insert(0,"/mnt/project-files/symphony/render/r04/lib"); import balance, marks, rtk
NB, W, cfgp = sys.argv[1:4]
over = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}
cfg = json.load(open(cfgp)); B = dict(cfg["balance"]); B.update(over)
mi = rtk.midi_info(W+"/score.midi"); bars = [(b["bar"], b["t_start"], b["t_end"]) for b in mi["per_bar"]]
rows = list(csv.DictReader(open(W+"/notes.csv", encoding="utf-8")))
mel = marks.melodies(W+"/ly_scratch/events.tsv", rows, mi["bar_s"], tpb=mi["tpb"])
rl = marks.rolls(rows, mi["bar_s"])
levels = defaultdict(dict); dyn = defaultdict(dict); whole = defaultdict(dict)
for r in csv.DictReader(open(NB+"/stems/stem_bars.csv")):
    if r["loud_LUFS"] in ("", "nan"): continue
    levels[r["stem"]][int(r["bar"])] = float(r["loud_LUFS"]); dyn[r["stem"]][int(r["bar"])] = r["dyn"]
for r in csv.DictReader(open(NB+"/bar_levels_whole_bar.csv")):
    if r["LUFS"] not in ("", "nan"): whole[r["stem"]][int(r["bar"])] = float(r["LUFS"])
for s in whole: levels.setdefault(s, {})
gains, rep, mels = balance.compute(dict(levels), bars, mel, rl, B, whole=dict(whole), pdyn=balance.printed_dyn(rows))
# smoothing ignored: per-bar gains
L = {s: {b: v + gains.get(s, {}).get(b, 0.0) for b, v in d.items()} for s, d in levels.items()}
DY = ['ppp','pp','p','mp','mf','f','ff','fff']
n0 = n6 = 0; res=[]
for st, bs, *_ in mel:
    dm, ds = [], []
    for b in bs:
        if b not in L.get(st, {}): continue
        oth = {k: L[k][b] for k in L if k != st and b in L[k] and not k.startswith("Harp") and k != "drums"}
        if not oth: continue
        dm.append(L[st][b] - max(oth.values())); ds.append(L[st][b] - 10*np.log10(sum(10**(v/10) for v in oth.values())))
    if dm:
        res.append((st, bs[0], np.median(dm), np.median(ds)))
n0 = sum(r[2] >= 0 for r in res); n6 = sum(r[3] >= -6 for r in res)
inv = 0
for b in set(b for d in L.values() for b in d):
    lst = [(s, L[s][b], dyn[s].get(b, "")) for s in L if b in L[s]]
    for a in lst:
        for c in lst:
            if a[2] in DY and c[2] in DY and DY.index(a[2]) < DY.index(c[2]) and a[1] > c[1] + 3: inv += 1
c6 = sum(1 for s, g in gains.items() for b, v in g.items() if v <= -6); c3 = sum(1 for s, g in gains.items() for b, v in g.items() if v <= -3)
# whole-bar loudness change
dl = []
for b, _, _ in bars:
    P0 = sum(10**(whole[s][b]/10) for s in whole if b in whole[s] and whole[s][b] > -90)
    P1 = sum(10**((whole[s][b]+gains.get(s,{}).get(b,0))/10) for s in whole if b in whole[s] and whole[s][b] > -90)
    if P0 > 0: dl.append(10*np.log10(P1/P0))
print(f"melodies >=0: {n0}/{len(res)}  >=-6 vs sum: {n6}/{len(res)}  inversions {inv}  cut>=3 {c3} cut>=6 {c6}  bar loudness change min/max {min(dl):+.1f}/{max(dl):+.1f}")
if "-v" in sys.argv:
    for r in res: print("  %-14s %3d %+5.1f %+5.1f" % r)
if "-i" in sys.argv:
    def invs(LL):
        out=set()
        for b in set(b for d in LL.values() for b in d):
            lst = [(s, LL[s][b], dyn[s].get(b, "")) for s in LL if b in LL[s]]
            for a in lst:
                for c in lst:
                    if a[2] in DY and c[2] in DY and DY.index(a[2]) < DY.index(c[2]) and a[1] > c[1] + 3: out.add((b,a[0],a[2],c[0],c[2]))
        return out
    new = invs(L) - invs(levels)
    for x in sorted(new): print("  new", x, round(L[x[1]][x[0]]-L[x[3]][x[0]],1), "gains", round(gains.get(x[1],{}).get(x[0],0),1), round(gains.get(x[3],{}).get(x[0],0),1))
