import sys, os, subprocess, numpy as np, soundfile as sf, mido, json
sys.path.insert(0,'/mnt/project-files/symphony/render/r02'); import sfzplay
V='/tmp/rcritic-01/dl/vpo/Virtual-Playing-Orchestra3/'
SR=48000; O='/tmp/rcritic-02/windtest/'
inst=[('flute','Woodwinds/flute-SEC',73,81),('oboe','Woodwinds/oboe-SEC',68,69),('clarinet','Woodwinds/clarinet-SEC',71,64),
      ('bassoon','Woodwinds/bassoon-SEC',70,50),('english-horn','Woodwinds/english-horn-SOLO',69,64),('horn','Brass/french-horn-SEC',60,65),
      ('trumpet','Brass/trumpet-SEC',56,72),('trombone','Brass/trombone-SEC',57,53),('tuba','Brass/tuba-SOLO',58,41),
      ('violin1','Strings/1st-violin-SEC',48,76),('viola','Strings/viola-SEC',48,60)]
def fl(prog,key,dur,vel):
    m=mido.MidiFile(); t=mido.MidiTrack(); m.tracks.append(t)
    t.append(mido.Message('program_change',program=prog,channel=0))
    t.append(mido.Message('note_on',note=key,velocity=vel,time=0))
    t.append(mido.Message('note_off',note=key,velocity=0,time=int(dur*960)))  # 120bpm tpb 480 -> 960 ticks/s
    t.append(mido.Message('note_off',note=0,velocity=0,time=int(4*960)))
    m.ticks_per_beat=480; p=O+'t.mid'; m.save(p)
    subprocess.run(['fluidsynth','-ni','-q','-R','0','-C','0','-g','0.5','-r',str(SR),'-O','float','-T','wav','-F',O+'t.wav','/usr/share/sounds/sf2/FluidR3_GM.sf2',p],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    x,_=sf.read(O+'t.wav',dtype='float32',always_2d=True); return x
def vp(f,key,dur,vel):
    s=sfzplay.Sfz(V+f+'.sfz'); return sfzplay.render(s,[(0.0,dur,key,vel)],SR,6.0,seed=3)
def metr(x,dur):
    m=x.mean(1); h=int(0.005*SR); k=len(m)//h; e=10*np.log10((m[:k*h].reshape(k,h)**2).mean(1)+1e-14)
    pk=e.max(); ipk=np.argmax(e)
    att=np.nonzero(e>=pk-3)[0][0]*0.005
    # level at note-off
    i0=int(dur/0.005); lvl=e[max(i0-4,0):i0].mean() if dur>0.2 else pk
    after=e[i0:]
    t20=(np.nonzero(after<lvl-20)[0][:1]*0.005).tolist(); t40=(np.nonzero(after<lvl-40)[0][:1]*0.005).tolist()
    aud=np.nonzero(e>pk-20)[0][-1]*0.005
    # tail correlation (after note-off+50ms, while within 40 dB)
    a=int((dur+0.05)*SR); b=int((dur+0.05+ (t40[0] if t40 else 1.0))*SR)
    L,R=x[a:b,0],x[a:b,1]; tc=float(np.dot(L,R)/np.sqrt(np.dot(L,L)*np.dot(R,R)+1e-20))
    bc=float(np.dot(x[:,0],x[:,1])/np.sqrt(np.dot(x[:,0],x[:,0])*np.dot(x[:,1],x[:,1])+1e-20))
    X=np.abs(np.fft.rfft(m[:int((dur+0.3)*SR)]))**2; f=np.fft.rfftfreq(int((dur+0.3)*SR),1/SR); cen=float((X*f).sum()/X.sum())
    return dict(attack_ms=int(round(att*1000)), t20_after_off=float(t20[0]) if t20 else None, t40_after_off=float(t40[0]) if t40 else None, audible_to_m20dB_s=round(float(aud),3), corr=round(bc,2), tail_corr=round(tc,2), centroid=int(round(cen)))
res={}
for name,f,prog,key in inst:
    r={}
    for lab,dur in (('sus1s',1.0),('short',0.12)):
        r['FluidR3_'+lab]=metr(fl(prog,key,dur,80),dur)
        r['VPO_'+lab]=metr(vp(f+('-sustain' if lab=='sus1s' else '-staccato'),key,dur,80),dur)
    # velocity range VPO sustain 42 vs 91
    lv=[]
    for vel in (42,91):
        y=vp(f+'-sustain',key,1.0,vel); lv.append(10*np.log10((y[:int(1.0*SR)]**2).mean()+1e-20))
    r['VPO_sus_level_range_42_91_dB']=round(float(lv[1]-lv[0]),1)
    lv=[]
    for vel in (42,91):
        y=fl(prog,key,1.0,vel); lv.append(10*np.log10((y[:int(1.0*SR)]**2).mean()+1e-20))
    r['FluidR3_level_range_42_91_dB']=round(float(lv[1]-lv[0]),1)
    res[name]=r
    print(name, json.dumps(r))
json.dump(res,open(O+'windtest.json','w'),indent=1)
