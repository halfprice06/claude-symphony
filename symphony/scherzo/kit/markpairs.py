import subprocess, sys, re, glob, html
pairs={"F":"a","K":"Trio","P":"poco","Q":"Tempo","U":"Più","V":"Meno"}
tot=same=0; bad=[]
for f in sorted(glob.glob(sys.argv[1]+"/parts-*.pdf")):
    out=subprocess.run(["pdftotext","-bbox",f,"-"],capture_output=True,text=True).stdout
    pages=out.split("<page ")[1:]
    for pi,pg in enumerate(pages):
        words=[(html.unescape(m.group(5)),float(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4))) for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>',pg)]
        for L,T in pairs.items():
            for w in words:
                if w[0]==L:
                    # find tempo word to the right within 120pt horizontally and 40 pt vertically
                    c=[t for t in words if t[0]==T and abs(t[2]-w[2])<30 and -10<t[1]-w[3]<140]
                    if c:
                        t=min(c,key=lambda t:abs(t[1]-w[3]))
                        tot+=1
                        dy=(t[4])-(w[4])
                        ok=abs(dy)<2.5
                        same+=ok
                        if not ok: bad.append((f.split('/')[-1],pi+1,L,round(dy,1)))
print("pairs",tot,"on one line",same)
for b in bad: print(b)
