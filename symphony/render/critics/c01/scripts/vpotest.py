import mido, subprocess, os, sys, numpy as np, soundfile as sf, json
SFZ="/tmp/rcritic-01/dl/vpo/Virtual-Playing-Orchestra3"
X="/tmp/rcritic-01/dl/sfizz/x"
env=dict(os.environ, LD_LIBRARY_PATH=f"{X}/usr/lib/x86_64-linux-gnu:{X}/usr/lib")
D="/tmp/rcritic-01/vpotest"
def mk(path, note, vels, dur, gap, cc1=None, prog=0):
    m=mido.MidiFile(ticks_per_beat=480); t=mido.MidiTrack(); m.tracks.append(t)
    t.append(mido.MetaMessage('set_tempo',tempo=500000))
    t.append(mido.Message('program_change',program=prog,time=0))
    if cc1 is not None: t.append(mido.Message('control_change',control=1,value=cc1))
    for v in vels:
        t.append(mido.Message('note_on',note=note,velocity=v,time=int(gap*960)))
        t.append(mido.Message('note_off',note=note,velocity=0,time=int(dur*960)))
    t.append(mido.MetaMessage('end_of_track',time=1920)); m.save(path)
def rend_sfz(sfz,mid,wav):
    subprocess.run([f"{X}/usr/bin/sfizz_render","--sfz",sfz,"--midi",mid,"--wav",wav,"-s","48000","-q","3"],env=env,check=True,capture_output=True)
def rend_fs(mid,wav):
    subprocess.run(["fluidsynth","-ni","-q","-R","0","-C","0","-g","0.2","-r","48000","-T","wav","-F",wav,"/usr/share/sounds/sf2/FluidR3_GM.sf2",mid],check=True,capture_output=True)
def analyse(wav, vels, dur, gap):
    x,sr=sf.read(wav,always_2d=True); y=x.mean(1)
    out=[]; t=0.0
    for v in vels:
        t+=gap; a=int(t*sr); b=int((t+dur)*sr); seg=y[a:b] if b>a+100 else y[a:a+int(0.1*sr)]
        # level: rms over the note (first max(dur,0.3)s) in dB
        s=y[a:a+int(max(dur,0.3)*sr)]
        lev=10*np.log10(np.mean(s**2)+1e-20)
        S=np.abs(np.fft.rfft(s*np.hanning(len(s))))**2; f=np.fft.rfftfreq(len(s),1/sr)
        cen=float((f*S).sum()/S.sum())
        # envelope 10ms, audible length to -20 dB from peak
        h=int(0.01*sr); e=np.array([np.sqrt(np.mean(y[i:i+h]**2)+1e-20) for i in range(a,min(len(y),a+int((dur+gap-0.01)*sr)),h)])
        ed=20*np.log10(e); pk=ed.max(); k=int(np.argmax(ed)); att=k*10
        bl=np.where(ed[k:]<pk-20)[0]; aud=round((k+bl[0])*0.01,2) if len(bl) else '>%.2f'%(dur+gap)
        out.append({"vel":v,"level_dB":round(lev,1),"centroid_Hz":round(cen),"attack_ms_to_peak":att,"audible_s":aud})
        t+=dur
    return out
res={}
vels=[32,42,53,64,74,84,91,110,127]
tests={
 "vpo_vln1_sustain":(f"{SFZ}/Strings/1st-violin-SEC-sustain.sfz",76,1.5,0.6),
 "vpo_vln1_PERF":(f"{SFZ}/Strings/1st-violin-SEC-PERF.sfz",76,1.5,0.6),
 "vpo_vln1_staccato":(f"{SFZ}/Strings/1st-violin-SEC-staccato.sfz",76,0.15,1.2),
 "vpo_vln1_pizz":(f"{SFZ}/Strings/1st-violin-SEC-pizzicato.sfz",76,0.3,1.5),
 "vpo_vln1_trem":(f"{SFZ}/Strings/1st-violin-SEC-tremolo.sfz",76,1.5,0.6),
 "vpo_horn_sustain":(f"{SFZ}/Brass/french-horn-SEC-sustain.sfz",65,1.5,0.6),
 "vpo_trb_sustain":(f"{SFZ}/Brass/trombone-SEC-sustain.sfz",58,1.5,0.6),
 "vpo_oboe_staccato":(f"{SFZ}/Woodwinds/oboe-SEC-staccato.sfz",72,0.15,1.2),
 "vpo_timp_roll":(f"{SFZ}/Percussion/timpani-roll.sfz",43,2.0,0.6),
}
for k,(sfz,note,dur,gap) in tests.items():
    if not os.path.exists(sfz): print("missing",sfz); continue
    mid=f"{D}/{k}.mid"; wav=f"{D}/{k}.wav"; mk(mid,note,vels,dur,gap)
    rend_sfz(sfz,mid,wav); res[k]=analyse(wav,vels,dur,gap)
for k,(prog,note,dur,gap) in {"fr3_strings48":(48,76,1.5,0.6),"fr3_strings48_stacc":(48,76,0.15,1.2),"fr3_pizz45":(45,76,0.3,1.5),"fr3_horn60":(60,65,1.5,0.6)}.items():
    mid=f"{D}/{k}.mid"; wav=f"{D}/{k}.wav"; mk(mid,note,vels,dur,gap,prog=prog); rend_fs(mid,wav); res[k]=analyse(wav,vels,dur,gap)
json.dump(res,open(f"{D}/vpotest.json","w"),indent=1)
for k,v in res.items():
    lv=[r["level_dB"] for r in v]; c=[r["centroid_Hz"] for r in v]
    print(f"{k:22s} level v32..127 {lv[0]:6.1f}..{lv[-1]:6.1f} (pp42->ff91 {lv[5+1]-lv[1]:+.1f} dB) centroid {c[1]}->{c[6]} Hz  attack v42/v91 {v[1]['attack_ms_to_peak']}/{v[6]['attack_ms_to_peak']} ms  audible v74 {v[4]['audible_s']}")
