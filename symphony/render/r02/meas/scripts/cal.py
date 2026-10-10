import sys, numpy as np, json
sys.path.insert(0,'/mnt/project-files/symphony/render/r02'); import sfzplay
V="/mnt/project-files/symphony/render/assets/vpo3/Strings/"
INS={"Violins I":("1st-violin",[60,67,74,81,88]),"Violins II":("2nd-violin",[58,65,72,79]),"Violas":("viola",[50,57,64,71]),"Violoncellos":("cello",[38,45,52,59,64]),"Double basses":("bass",[29,34,40,47])}
sr=48000
def lev(y,a,b):
    return 10*np.log10(np.mean(y[a:b]**2)+1e-20)
def peak(y):
    h=int(0.05*sr); e=[np.mean(y[i:i+h]**2) for i in range(0,len(y)-h,h//2)]
    return 10*np.log10(max(e)+1e-20)
res={}
for st,(ins,keys) in INS.items():
    r={}
    for art,dur,ov in [("sustain",1.5,{"attack":0.05}),("sustain_short",0.25,{"attack":0.015,"skip_db":-4}),("staccato",0.12,{}),("accent",0.5,{}),("pizzicato",0.2,{}),("tremolo",1.5,{"attack":0.05})]:
        f=art.split('_')[0]
        s=sfzplay.Sfz(V+f"{ins}-SEC-{f}.sfz"); vals=[]
        for k in keys:
            y=sfzplay.render(s,[(0.0,dur,k,74,ov)],sr,dur+2.5).mean(1)
            vals.append(lev(y,int(0.6*sr),int(1.4*sr)) if art in("sustain","tremolo") else peak(y))
        r[art]=round(float(10*np.log10(np.mean(10**(np.array(vals)/10)))),1)
    res[st]=r; print(st,r)
json.dump(res,open('cal.json','w'),indent=1)
