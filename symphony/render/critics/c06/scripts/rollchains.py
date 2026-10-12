#!/usr/bin/env python3
"""critic 6: timpani roll CHAINS: consecutive tremolo notes with no gap (untied: a new note each bar or a pitch change)
that together last longer than one bar. marks.rolls() only sees single notes longer than a bar. Usage: rollchains.py WORK"""
import sys, csv
W = sys.argv[1]
rows = [r for r in csv.DictReader(open(f'{W}/notes.csv')) if r['staff'].startswith('Timp') and 'tremolo' in (r['arts'] or '')]
rows.sort(key=lambda r: float(r['t_on_s']))
chains = []; cur = []
for r in rows:
    t0 = float(r['t_on_s'])
    if cur and abs(t0 - (float(cur[-1]['t_on_s']) + float(cur[-1]['notated_s']))) < 0.05:
        cur.append(r)
    else:
        if cur: chains.append(cur)
        cur = [r]
if cur: chains.append(cur)
for c in chains:
    if len(c) < 2: continue
    L = float(c[-1]['t_on_s']) + float(c[-1]['notated_s']) - float(c[0]['t_on_s'])
    print(f"bars {c[0]['bar']}-{c[-1]['bar']} ({L:.1f} s, {len(c)} notes): " + ' | '.join(f"{r['bar']}:{r['pitch']} {r['dyn']}{'/'+r['hairpin'] if r['hairpin'] else ''} v{r['midi_vel']}" for r in c))
