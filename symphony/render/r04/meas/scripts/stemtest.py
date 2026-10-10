# render one stem from a fresh articulate run with a given config: stemtest.py W score cfg out stemname
import sys, os, subprocess
R="/mnt/project-files/symphony/render/r04"
W, score, cfgp, out, stem = sys.argv[1:6]
os.makedirs(out, exist_ok=True)
subprocess.run([sys.executable, R+"/articulate.py", W+"/score.midi", W+"/notes.csv", cfgp, out+"/render.midi", "--score", score], check=True, stdout=subprocess.DEVNULL)
import importlib.util
spec=importlib.util.spec_from_file_location("render", R+"/render.py"); rd=importlib.util.module_from_spec(spec); spec.loader.exec_module(rd)
mids = rd.split_stems(out+"/render.midi", out)
subprocess.run([sys.executable, R+"/stem.py", mids[stem], out+"/"+stem.replace(" ","_")+".wav", "--config", cfgp], check=True)
