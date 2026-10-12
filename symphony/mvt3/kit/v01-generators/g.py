# helper for writing movement III sections: pitch names (Dutch, absolute) <-> MIDI, chord voicing, patterns
import re
PC={'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
def pc(name):
    base=name[0]; acc=name[1:]
    v=PC[base]
    if base in 'ea' and acc.startswith('s') and not acc.startswith('is'): # es, as -> aes form handled below
        pass
    n=0; a=acc
    while a:
        if a.startswith('is'): n+=1; a=a[2:]
        elif a.startswith('es'): n-=1; a=a[2:]
        elif a.startswith('s'): n-=1; a=a[1:]
        else: break
    return v+n
def midi(p):
    m=re.match(r"([a-g](?:isis|eses|is|es|s)?)([',]*)$",p)
    name,octs=m.group(1),m.group(2)
    o=octs.count("'")-octs.count(",")
    base=48+12*o+PC[name[0]]
    # accidental shift, but octave is fixed by the letter (b# etc)
    return base+(pc(name)-PC[name[0]])
def octs(o):
    return "'"*o if o>0 else ","*(-o)
def at(name,o): return name+octs(o)
def place(names,lo,hi):
    out=[]
    for n in names:
        for o in range(-4,5):
            p=at(n,o)
            if lo<=midi(p)<=hi: out.append(p)
    return sorted(out,key=midi)
def nearest(name,ref):
    best=None
    for o in range(-4,5):
        p=at(name,o)
        if best is None or abs(midi(p)-ref)<abs(midi(best)-ref): best=p
    return best
def chord(ps): return "<"+" ".join(ps)+">" if len(ps)>1 else ps[0]
def shift(ly,k):
    """shift every note token in a LilyPond string by k octaves (k>0 up)"""
    def rep(m):
        name,o=m.group(1),m.group(2)
        cur=o.count("'")-o.count(",")
        return name+octs(cur+k)
    return re.sub(r"(?<![a-zA-Z\\])((?:[a-g](?:isis|eses|is|es|s)?))([',]*)(?=[0-9<>\s\(\)~\-\\\^_|]|$)",rep,ly)
LET='cdefgab'
def transpose_p(p,steps,semis):
    m=re.match(r"([a-g])((?:isis|eses|is|es|s)?)([',]*)$",p)
    l,acc,o=m.group(1),m.group(2),m.group(3)
    oc=o.count("'")-o.count(",")
    src=midi(p)
    li=LET.index(l)+steps
    noc=oc+li//7; nl=LET[li%7]
    base=48+12*noc+PC[nl]
    d=src+semis-base
    accs={-2:'eses',-1:'es',0:'',1:'is',2:'isis'}[d]
    if nl in 'ea' and accs.startswith('es'): accs=accs[1:] if nl=='a' else accs[1:]
    name=nl+accs
    if name=='es' or name=='as': pass
    if nl=='a' and accs=='s': name='aes'
    if nl=='a' and accs=='ses': name='aeses'
    if nl=='e' and accs=='s': name='es'
    if nl=='e' and accs=='ses': name='eses'
    return name+octs(noc)
def transpose(ly,steps,semis):
    def rep(m): return transpose_p(m.group(1)+m.group(2),steps,semis)
    return re.sub(r"(?<![a-zA-Z\\\"])([a-g](?:isis|eses|is|es|s)?)([',]*)(?=[0-9<>\s\(\)~\-\\\^_|]|$)",rep,ly)
def raise_below(ly,lo):
    def rep(m):
        p=m.group(1)+m.group(2)
        while midi(p)<lo: p=shift(p,1)
        return p
    return re.sub(r"(?<![a-zA-Z\\\"])([a-g](?:isis|eses|is|es|s)?)([',]*)(?=[0-9<>\s\(\)~\-\\\^_|]|$)",rep,ly)
