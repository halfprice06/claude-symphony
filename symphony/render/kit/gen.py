import sys
kind,N=sys.argv[1],int(sys.argv[2]); extra=sys.argv[3] if len(sys.argv)>3 else ""
t=open(f'/mnt/project-files/symphony/render/kit/{kind}.txt').read()
if kind=='critic':
    t=t.replace('{SETUP}',extra or "Render r{NN} with its own render.py on each test input (out-m1.mp3/out-m2.mp3 in r{NN}/ are the actor's renders; re-render at least one yourself to confirm they match the code).")
    rep={'{N}':str(N),'{NN}':f'{N:02d}','{N1}':str(N+1),'{PP}':f'{N-1:02d}'}
else:  # actor N builds rN from critic N-1
    t=t.replace('{EXTRA}',extra)
    rep={'{N1}':str(N),'{NN1}':f'{N:02d}','{N}':str(N-1),'{NN}':f'{N-1:02d}'}
for k in sorted(rep,key=len,reverse=True): t=t.replace(k,rep[k])
open(f'/tmp/claude-0/{kind}{N:02d}.txt','w').write(t)
print(f'/tmp/claude-0/{kind}{N:02d}.txt')
