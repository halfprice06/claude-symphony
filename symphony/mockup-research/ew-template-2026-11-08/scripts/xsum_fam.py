import re
FAM = [('perc', r'timp|drum|snare|cymbal|piatti|tam|taiko|boom|hit|perc|tom|gong|triangle|shaker|ride|kit|anvil|stick|chime|slap|rain|glock|marimba|vib|celest|bell|xylo|crotal'),
       ('keys/harp', r'harp|piano|steinway|keys|celeste|dulcimer|guitar|kantele|mandolin|accordion|harmonium|typewriter'),
       ('str-short', r'spic|stac|short|pizz|marc|portato|5/0|\bss\b shorts'),
       ('brass', r'horn|trumpet|\btp|trombone|\btbn|bones|tuba|\btb1|brass|cimbasso'),
       ('winds', r'flute|\bfl|oboe|\bob|clarinet|\bcl|bassoon|\bbsn|piccolo|pcl|winds|recorder|whistle|ney|english'),
       ('str-long', r'viol|vln|cello|\bvc|\bva\b|\bva[ab]\b|\bv[12]|bass|string|css|scs|legato|leg\b|trem|flaut|harmonic|\bcb\b|ensemble|ens|albion|mural|ark|lacrim|choir')]
def fam(n):
    n = (n or '').lower()
    for f, rx in FAM:
        if re.search(rx, n): return f
    return 'other'
