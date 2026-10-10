import music21 as m21, sys
f=sys.argv[1]; a,b,w=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
s=m21.converter.parse(f)
for st in range(a,b,w):
    ex=s.measures(st,st+w-1)
    try: k=ex.analyze('key'); print(st,st+w-1,k, round(k.correlationCoefficient,2))
    except Exception as e: print(st,e)
