import sys, os, json, subprocess, numpy as np, soundfile as sf, mido
R="/mnt/project-files/symphony/render/r04"; sys.path.insert(0,R); sys.path.insert(0,R+"/lib")
import sfzplay
cfg=json.load(open(R+"/config.json")); sr=48000
def fluid(prog, pitch, vel, L):
    m=mido.MidiFile(); t=mido.MidiTrack(); m.tracks.append(t)
    t.append(mido.Message('program_change',program=prog,channel=0))
    t.append(mido.Message('note_on',note=pitch,velocity=vel,time=0)); t.append(mido.Message('note_off',note=pitch,velocity=0,time=int(L*960)))
    m.ticks_per_beat=480; m.save('/tmp/a4/fc.mid')
    subprocess.run(["fluidsynth","-ni","-q","-R","0","-C","0","-g",str(cfg["fluid_gain"]),"-r",str(sr),"-O","float","-T","wav","-F","/tmp/a4/fc.wav",cfg["sf2"],"/tmp/a4/fc.mid"],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    x,_=sf.read('/tmp/a4/fc.wav',always_2d=True); return x
inst=sfzplay.Sfz(R+"/sfz/flute-stac-vsco2.sfz")
def pk(x):
    h=int(0.01*sr); e=(x**2).sum(1); n=len(e)//h; e=e[:n*h].reshape(n,h).mean(1)
    e=np.convolve(e,np.ones(5)/5,'same'); p=10*np.log10(e.max()+1e-20)
    i=np.argmax(e); lev=10*np.log10(e+1e-20)
    below=np.nonzero(lev[i:]<p-20)[0]; return p, (below[0]*0.01+i*0.01 if len(below) else None)
for pitch in (72,76,79,84,88):
  for vel in (60,90):
    a=fluid(73,pitch,vel,0.11); b=sfzplay.render(inst,[(0.0,0.11,pitch,vel,None)],sr,1.0)
    pa,la=pk(a); pb,lb=pk(b)
    print(pitch,vel,"fluid peak %.1f len %.2f | vsco peak %.1f len %.2f | diff %.1f"%(pa,la,pb,lb,pb-pa))
