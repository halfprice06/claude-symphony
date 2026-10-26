#!/usr/bin/env python3
# log.py NEW CRIT_FILE HIST_FILE : prepend CRIT_FILE to vNEW/critique.md (newest first) and append HIST_FILE to critics/HISTORY.md.
import sys
M='/home/user/claude_composes/symphony/mvt2'
new,cf,hf=sys.argv[1:]
p=f'{M}/v{new}/critique.md'; old=open(p).read()
open(p,'w').write(open(cf).read().rstrip('\n')+'\n\n---\n\n'+old)
h=f'{M}/critics/HISTORY.md'; s=open(h).read().rstrip('\n')
open(h,'w').write(s+'\n\n\n'+open(hf).read().rstrip('\n')+'\n')
print('logged v'+new)
