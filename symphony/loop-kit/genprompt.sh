#!/bin/bash
# genprompt.sh N "focus text" -> writes pN.txt (assigned reading from critics/READING.md)
N=$1; V=v$((N+19)); K=$(( (N-1)%10 + 1 ))
L=$(sed -n "$((K+1))p" /mnt/project-files/symphony/mvt1/critics/LENSES.md | sed "s/^$K\. //")
RD=$(grep "^| $N |" /mnt/project-files/symphony/mvt1/critics/READING.md | awk -F' \\| ' '{print $3}' | sed 's/ |$//')
cd $KIT
python3 - "$N" "$V" "$L" "$2" "$RD" > p$N.txt <<'PY'
import sys
n,v,l,f,r=sys.argv[1:]
s=open('critic_prompt.txt').read()
s=s.replace('READING.',r+'.').replace('NNN',n).replace('VVV',v).replace('LENS.',l).replace('FOCUS',('Focus: '+f) if f else '')
print(s)
PY
echo p$N.txt; grep -m1 "assigned reading:" p$N.txt | cut -c1-160
