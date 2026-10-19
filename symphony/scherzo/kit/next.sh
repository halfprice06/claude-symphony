#!/bin/bash
# next.sh N "critique text" "history text" : promote critic N's scratch copy to v(N+1), log it, write the prompt for N+1 (third series helper).
set -e
M=/home/user/claude_composes/symphony/scherzo; N=$1; S=/tmp/critic-$(printf %03d $N)/work
rm -f $S/allplayers.*
bash $M/kit/promote.sh $((N+1)) $N $S 2>&1 | grep -v "^  bar"
python3 $M/kit/log.py $N "$2" "$3"
bash $M/kit/genprompt.sh $((N+1)) "$4"
