import sys; sys.path.insert(0,'/mnt/project-files/symphony/render/r03'); sys.path.insert(0,'/mnt/project-files/symphony/render/r03/lib')
import render, rtk, csv
midi, out = sys.argv[1:3]
import os; os.makedirs(out, exist_ok=True)
p = render.split_stems(midi, out); print(p.keys())
mi = rtk.midi_info(midi)
w = csv.writer(open(os.path.join(out,'bars.csv'),'w')); w.writerow(['bar','t_start','t_end'])
for b in mi['per_bar']: w.writerow([b['bar'],b['t_start'],b['t_end']])
open(os.path.join(out,'empty.csv'),'w').write('stem,bar,LUFS\n')
