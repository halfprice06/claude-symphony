# s: four bars joined by ' | '; add first-theme slurs
def f(s):
    bars = s.split(' | ')
    def open_bar(b):
        t = b.split(' ')
        i = t.index('r8') if 'r8' in t else None
        if i is None: return b
        x = i + 1
        def addp(tok, c):
            # put after duration+articulations: append at end is fine in LilyPond
            return tok + c
        t[x] = addp(t[x], '('); t[x+1] = addp(t[x+1], ')'); t[x+2] = addp(t[x+2], '(')
        return ' '.join(t)
    def close_first(b):
        t = b.split(' '); t[0] += ')'; return ' '.join(t)
    bars[0] = open_bar(bars[0]); bars[1] = close_first(bars[1])
    bars[2] = open_bar(bars[2]); bars[3] = close_first(bars[3])
    return ' | '.join(bars)
