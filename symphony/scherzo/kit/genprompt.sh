#!/bin/bash
# genprompt.sh N "focus text" -> writes pN.txt in this folder. Cycle N reviews vNN (v01 for cycle 1) and produces v(N+1).
# Lens 9 (holistic) cycles also get their master scherzo from critics/MASTERS.txt (line k for the k-th lens-9 cycle).
KIT=/mnt/project-files/symphony/scherzo/kit; C=/mnt/project-files/symphony/scherzo/critics
N=$1; V=v$(printf %02d $N); K=$(( (N-1)%10 + 1 )); NNN=$(printf %03d $N)
L=$(sed -n "$((K+1))p" $C/LENSES.md | sed "s/^$K\. //")
RD=$(grep "^| $N |" $C/READING.md | awk -F' \\| ' '{print $3}' | sed 's/ |$//')
F="$2"
if [ $K -eq 9 ]; then
  MS=$(sed -n "$(( (N-9)/10 + 1 ))p" $C/MASTERS.txt)
  F="Your master scherzo for the holistic comparison: $MS. Also compare with v$(printf %02d $(( N>10 ? N-10 : 1 ))) and flag anything that got worse. $F"
fi
cd $KIT
python3 - "$NNN" "$V" "$L" "$F" "$RD" > p$N.txt <<'PY'
import sys
n,v,l,f,r=sys.argv[1:]
s=open('critic_prompt.txt').read()
s=s.replace('READING.',r+'.').replace('NNN',n).replace('VVV',v).replace('LENS.',l).replace('FOCUS',('Focus: '+f) if f else '')
print(s)
PY
echo $KIT/p$N.txt; grep -m1 "assigned reading:" p$N.txt | cut -c1-160
