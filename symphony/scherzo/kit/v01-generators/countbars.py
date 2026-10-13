# count bars of every section variable (bar checks '|' and R2.*n), compare with sections.txt
import re, sys, os
v = sys.argv[1]
lens = {l.split()[0]: int(l.split()[1]) for l in open(os.path.join(v, 'sections.txt')) if l.strip()}
for sec, n in lens.items():
    txt = open(os.path.join(v, 'sections', sec + '.ily')).read()
    for m in re.finditer(rf'^{sec}(\w+) = {{ (.*) }}\s*$', txt, re.M):
        body = m.group(2).strip().rstrip('|').strip()
        cnt = 0
        for b in body.split('|'):
            b = b.strip()
            r = re.fullmatch(r'R2\.\*(\d+)', b)
            cnt += int(r.group(1)) if r else 1
        if cnt != n:
            print(sec, m.group(1), cnt, 'expected', n)
