import re,sys,glob,os
W=sys.argv[1]
order=[l.split()[0] for l in open(W+'/sections.txt') if l.strip()]
# tempo per bar (half notes per minute) roughly from global: approximate map
tempo={}
def tempo_at(b):
    if 51<=b<=66 or 67<=b<=82: return 72
    if 205<=b<=210: return 90
    if 211<=b<=222: return 72
    if 223<=b<=234: return 56
    if 235<=b<=246: return 66
    if 247<=b<=272: return 88
    if b>=273: return 72
    return 84
insts=['FluteOne','FluteTwo','OboeOne','OboeTwo','CorAnglais','ClOne','ClTwo','BassCl','BsnOne','BsnTwo','Cbsn','HnOne','HnTwo','HnThree','HnFour','TptOne','TptTwo','TptThree','TbnOne','TbnTwo','BassTbn','Tuba']
def strip_tags(s):
    # remove \tag #'part { ... } blocks, keep \tag #'score {...} content
    out='';i=0
    while i<len(s):
        m=re.match(r"\\tag\s*#'(part|score)\s*",s[i:])
        if m:
            j=i+m.end()
            if s[j]=='{':
                d=0;k=j
                while True:
                    if s[k]=='{':d+=1
                    elif s[k]=='}':
                        d-=1
                        if d==0:break
                    k+=1
                inner=s[j+1:k]
                if m.group(1)=='score': out+=' '+inner+' '
                i=k+1;continue
            else:
                # tag applies to next token: skip the token if part
                tok=re.match(r"\s*(\S+)",s[j:])
                if m.group(1)=='part': i=j+tok.end();continue
                i=j;continue
        out+=s[i];i+=1
    return out
def events(s):
    s=strip_tags(s)
    s=re.sub(r'%[^\n]*','',s)
    s=re.sub(r'\\markup\s*(\\\w+\s*)*(\{[^{}]*(\{[^{}]*\}[^{}]*)*\}|"[^"]*"|#"[^"]*")','',s)
    s=re.sub(r'\\grace\s*\{[^}]*\}','',s)
    s=re.sub(r'"[^"]*"','',s)
    s=s.replace('\\breathe',' @ ')
    s=re.sub(r'\\[<>!]',' ',s); s=s.replace('->',' ').replace('-<',' ')
    s=re.sub(r'\\transpose\s+\S+\s+\S+',' ',s)
    s=re.sub(r'\\(clef|tweak|override|set|offset|once\s+\\override)\s+[\w.-]+',' ',s)
    s=re.sub(r"#'?\([^)]*\)",' ',s)
    s=re.sub(r'#\S+',' ',s)
    s=re.sub(r'\b(?!R\d)\w*[A-Z][\w.]*',' ',s)
    s=re.sub(r'\\[a-zA-Z]+',' ',s)
    ev=[];last=4;
    for m in re.finditer(r"(<[^>]*>|[a-g](?:is|es|s)*[',]*|R|r|s)(\d+)?(\.*)(\*(\d+))?|(~)|@",s):
        if m.group(6): 
            if ev: ev[-1][2]=True
            continue
        if m.group(0)=='@': ev.append(['b',0,False]);continue
        tok=m.group(1)
        if tok is None: continue
        if m.group(2): last=int(m.group(2)); dots=len(m.group(3))
        else: dots=len(m.group(3))
        d=4.0/last*(2-0.5**dots)
        if m.group(5): d*=int(m.group(5))
        kind='r' if tok in('r','R','s') else 'n'
        ev.append([kind,d,False])
    return ev
res={}
bar0=1
secstart={}
for l in open(W+'/sections.txt'):
    p=l.split()
    if not p: continue
    secstart[p[0]]=(bar0,int(p[1])); bar0+=int(p[1])
for inst in insts:
    stream=[]
    for sec,(b0,n) in secstart.items():
        txt=open(f'{W}/sections/{sec}.ily').read()
        m=re.search(r'^'+sec+inst+r'\s*=\s*(\\drummode\s*)?\{',txt,re.M)
        if not m:
            stream.append(('r',b0,n*4.0));continue
        i=m.end()-1;d=0;k=i
        while True:
            if txt[k]=='{':d+=1
            elif txt[k]=='}':
                d-=1
                if d==0:break
            k+=1
        body=txt[i+1:k]
        # expand variable references like \recPOboeTwoDiv : ignore
        ev=events(body)
        t=0.0
        tot=sum(e[1] for e in ev)
        if abs(tot-n*4)>0.01: print('LEN',inst,sec,tot,n*4,file=sys.stderr)
        for e in ev:
            stream.append((e[0],b0+t/4,e[1],e[2])); t+=e[1]
    # find stretches
    cur=None;sec=0
    out=[]
    for e in stream:
        if e[0]=='n':
            if cur is None: cur=e[1];sec=0
            sec+=e[2]/4*60/tempo_at(int(e[1]))*2
            end=e[1]+e[2]/4
        else:
            if cur is not None and (e[0]=='b' or e[2]>0):
                out.append((sec,cur,end));cur=None
    if cur is not None: out.append((sec,cur,end))
    for sec,a,b in sorted(out,reverse=True)[:4]:
        if sec>9: print(f'{inst:10s} {sec:5.1f}s  bars {a:.2f}-{b:.2f}')
