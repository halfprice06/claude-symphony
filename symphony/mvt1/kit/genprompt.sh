#!/bin/bash
# genprompt.sh N "focus text" -> writes kit/pN.txt. Series 3: cycle N reviews vN and produces v(N+1).
M=/home/user/claude_composes/symphony/mvt1; KIT=$M/kit; C=$M/critics
N=$1; V=v$N; K=$(( (N-1)%10 + 1 ))
L=$(sed -n "$((K+1))p" $C/LENSES3.md | sed "s/^$K\. //")
RD=$(grep "^| $N |" $C/READING3.md | awk -F' \\| ' '{print $3}' | sed 's/ |$//')
F="$2"
if [ $K = 9 ]; then MS=$(grep "^| $N |" $C/MASTERS.md | awk -F' \\| ' '{print $2}' | sed 's/ |$//'); F="Your master movement for lens 9: $MS. Compare also with v$((N-10)). $F"; fi
cd $KIT
python3 - "$N" "$V" "$L" "$F" "$RD" > p$N.txt <<'PY'
import sys
n,v,l,f,r=sys.argv[1:]
s=open('critic_prompt.txt').read()
s=s.replace('READING.',r+'.').replace('NNN',n).replace('VVV',v).replace('LENS.',l).replace('FOCUS',('Focus: '+f) if f.strip() else '')
print(s)
PY
echo $KIT/p$N.txt; grep -m1 "assigned reading:" p$N.txt | cut -c1-160
