# write a test config with VPO sfz engines for wind/brass staves: windcfg.py base_config out_config vpo_root [staff ...]
import json, sys
base, out, root = sys.argv[1:4]; only = sys.argv[4:]
c = json.load(open(base))
M = {"Flutes 12": ("Woodwinds/flute-SOLO", "Woodwinds/flute-SEC"), "Oboes 12": ("Woodwinds/oboe-SOLO", "Woodwinds/oboe-SEC"),
     "Cor anglais": ("Woodwinds/english-horn-SOLO", None), "Clarinets 12": ("Woodwinds/clarinet-SOLO", "Woodwinds/clarinet-SEC"),
     "Bass clarinet": ("Woodwinds/bass-clarinet-SOLO", None), "Bassoons 12": ("Woodwinds/bassoon-SOLO", "Woodwinds/bassoon-SEC"),
     "Contrabassoon": ("Woodwinds/contrabassoon-SOLO", None), "Horns 12": ("Brass/french-horn-SOLO", "Brass/french-horn-SEC"),
     "Horns 34": ("Brass/french-horn-SOLO", "Brass/french-horn-SEC"), "Trumpets 12": ("Brass/trumpet-SOLO", "Brass/trumpet-SEC"),
     "Trumpet 3": ("Brass/trumpet-SOLO", None), "Trombones 12": ("Brass/trombone-SOLO", "Brass/trombone-SEC"),
     "Bass trombone": ("Brass/bass-trombone-SOLO", None), "Tuba": ("Brass/tuba-SOLO", None)}
ENV = [[0.35, {"attack": 0.015, "skip_db": -4, "release": 0.25}], [0.8, {"attack": 0.03, "skip_db": -8, "release": 0.35}],
       [None, {"attack": 0.06, "skip_db": -14, "release": 0.5}]]
for st, (solo, sec) in M.items():
    if only and st not in only: continue
    S = c["stems"][st]
    ch = {}
    for base in range(4):
        pre = sec if (base == 2 and sec) else solo
        ch[str(base)] = {"file": f"{root}/{pre}-sustain.sfz", "env": ENV}
        ch[str(base + 4)] = {"file": f"{root}/{pre}-staccato.sfz"}
        ch[str(base + 8)] = {"file": f"{root}/{pre}-accent.sfz", "env": [[None, {"release": 0.4}]]}
    S["engine"] = "sfz"; S["artic_channels"] = True
    S["sfz"] = {"gain_dB": 0.0, "tail_s": 4.0, "channels": ch}
json.dump(c, open(out, "w"), indent=1)
