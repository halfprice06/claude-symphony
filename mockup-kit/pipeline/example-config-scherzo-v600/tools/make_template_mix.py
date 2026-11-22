"""Write a copy of a mix.json with EastWest's template mix keys added (mvt1 c50; loop/TEMPLATE-PLAN.md sections 1-3, 8;
the keys are documented in tools/TEMPLATE-TOOLS.md).

Usage: python3 tools/make_template_mix.py [SRC_MIX] [OUT] [--parts PARTS]
  defaults: build/mix.json -> build/mix_template06.json, with build/parts.json for each track's patch and alias source.
  Every key of SRC is kept; the template keys are added (or replaced when SRC already has them), so the output can be
  regenerated from whatever mix.json c49 leaves. The old keys stay where the new ones override them ("mics",
  "width_by_mic", "send", "reverb"), so a track can go back to the c49 layout by setting the new keys to null
  ("mic_db", "pan_by_mic", "family_eq", "send_profile", "reaper_pan": null and "opus_reverb_off": false).

Sources of the values (symphony/mockup-research/ew-template-2026-11-08/):
  - mic levels: opus-mics.txt, per patch: the KS Master's own value where the template loads it; Celli and Basses KS
    Masters load Main only in the template, so their Close is the template's Leg Slur patch (-6.6, -3.3 dB), as the plan
    asks for Close on every string section; no template value for 2TP (Trumpet 1's -10.1 dB: Trumpets a2 is its alias),
    1TB (the template's 2TB, -9.3 dB) and CB (the bassoon's -8.6 dB).
  - mic pans: TEMPLATE-PLAN section 1 ("Close at the seat with the track width, Main and Surround full width").
  - REAPER track pans: TEMPLATE-PLAN section 1 (none given for winds, harp, timpani, percussion: centre).
  - returns, send levels and return faders: ho-mix-fx.json (receives and fader_db of each VERB track): strings -5.56,
    brass -8.77, winds -8.36, percussion and timpani -6.41, harp -8.77 dB; faders +1.03 / +0.66 dB; ALGO GLUE +5.82 dB
    with receives -9.62 / -5.65 / -7.27 / -6.81 / -6.41 dB (disabled: "test in pass 2").
  - family and master EQ: the decoded ReaEQ bands of ho-mix-fx.json (TEMPLATE-PLAN section 3 rounds them).
  - the Duc variant (TEMPLATE-PLAN section 8): a 2.3 s true-stereo rear IR (Spaces II "Hollywood Scoring Stage TS RR
    2.3s", impulse names from its .preset file), low cut 184 Hz and high cut 3 kHz before the IR, return -5.5 dB, sends
    0 dB, celli and basses -1.6 dB with their short rows at -7 dB, pre-delay 12 ms (duc-mix.txt, VSR S24 value 13
    read as pre-delay; inferred).
"""
import json, os, sys
from collections import OrderedDict

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
args = [a for a in sys.argv[1:]]
PARTS = args[args.index("--parts") + 1] if "--parts" in args else os.path.join(ROOT, "build", "parts.json")
pos = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--parts")]
SRC = pos[0] if pos else os.path.join(ROOT, "build", "mix.json")
OUT = pos[1] if len(pos) > 1 else os.path.join(ROOT, "build", "mix_template06.json")
if os.path.abspath(OUT) == os.path.abspath(os.path.join(ROOT, "build", "mix.json")):
    sys.exit("refusing to overwrite build/mix.json; write the template copy elsewhere and adopt it deliberately")

mix = json.load(open(SRC), object_pairs_hook=OrderedDict)
parts = {t["name"]: t for t in json.load(open(PARTS))["tracks"]}

# opus-mics.txt per patch (stem name in parts.json)
MIC_DB = {
    "1st Violins KS Master": {"Close": -9.0, "Main": 0.0},
    "2nd Violins KS Master": {"Close": -7.7, "Main": 0.0},
    "Violas KS Master": {"Close": -7.0, "Main": 0.0},
    "Celli KS Master": {"Close": -6.6, "Main": 0.0},     # template KS Master: Main only; Leg Slur patch -6.6
    "Basses KS Master": {"Close": -3.3, "Main": 0.0},    # template KS Master: Main only; Leg Slur patch -3.3
    "1FH KS Master": {"Close": -6.3, "Main": 0.0},
    "2FH KS Master": {"Close": -7.7, "Main": 0.0},
    "1TP KS Master": {"Close": -10.1, "Main": 0.0},      # the patch also loads Surround 1.0 by default: unloaded here
    "2TP KS Master": {"Close": -10.1, "Main": 0.0},      # no template value: Trumpet 1's (Trumpets a2 is its alias)
    "1TB KS Master": {"Close": -9.3, "Main": 0.0},       # the template's 2TB KS Master
    "1TU KS Master": {"Close": -10.2, "Main": 0.0},
    "FL KS Master": {"Close": 0.0, "Main": -4.7},
    "FL2 KS Master": {"Close": 0.0, "Main": -3.4},
    "OB KS Master": {"Close": 0.0, "Main": -20.6},
    "EH KS Master": {"Close": 0.0, "Main": -11.6},
    "CL KS Master": {"Close": 0.0, "Main": -3.4},
    "BC KS Master": {"Close": 0.0, "Main": -9.8},
    "BS KS Master": {"Close": 0.0, "Main": -8.6},
    "CB KS Master": {"Close": 0.0, "Main": -8.6},        # no template value: the bassoon's
    "Harp Sus RR": {"Close": 0.0, "Mid": 0.0, "Main": -9.0},   # the template's Harp KS Master
    "Timpani Flt KS": {"Close": -8.4, "Main": -6.9, "Surround": 0.0},
    "32in Med Tam Tam": {"Main": 0.0},                   # template cymbals and tam-tam: Main only
    "18in Zildjian Sus Cymbal Cres": {"Main": 0.0},
    "22in Zildjian K Crash": {"Main": 0.0},
}
GROUP_MIC_DB = {   # for a track whose patch is not listed above
    "string": {"Close": -6.0, "Main": 0.0}, "horn": {"Close": -6.3, "Main": 0.0}, "trumpet": {"Close": -10.1, "Main": 0.0},
    "lowbrass": {"Close": -9.3, "Main": 0.0}, "wind": {"Close": 0.0, "Main": -8.6},
    "timp": {"Close": -8.4, "Main": -6.9, "Surround": 0.0}, "harp": {"Close": 0.0, "Mid": 0.0, "Main": -9.0},
    "perc": {"Main": 0.0},
}
PAN_BY_MIC = OrderedDict([("Close", "seat"), ("Mid", "full"), ("Main", "full"), ("Surround", "full")])
REAPER_PAN = {"Violins I": -0.10, "Violins II": -0.21, "Violas": 0.0, "Violoncellos": 0.15, "Double basses": 0.23,
              "Horn 1": -0.18, "Horn 2": -0.16, "Horn 3": -0.15, "Horn 4": -0.13, "Horns a2": -0.16,
              "Trumpet 1": 0.03, "Trumpet 2": 0.06, "Trumpet 3": 0.10, "Trumpets a2": 0.05,
              "Trombone 1": 0.15, "Trombone 2": 0.15, "Bass trombone": 0.15, "Tuba": 0.23}
FAMILY_OF_GROUP = {"string": "strings", "horn": "brass", "trumpet": "brass", "lowbrass": "brass", "wind": "woodwinds",
                   "harp": "harp", "timp": "timpani", "perc": None}


def band(kind, hz, db=None, bw=None):
    b = OrderedDict([("band", kind), ("hz", hz)])
    if db is not None:
        b["db"] = db
    if bw is not None:
        b["bw_oct"] = bw
    return b


FAMILY_EQS = OrderedDict([
    ("_doc", "mvt1 c50 (TEMPLATE-PLAN section 3): the template's section-bus / track ReaEQ bands (ho-mix-fx.json "
             "decoded_bands), one ReaEQ after every other FX of each track of the family (build_reaper.py family_eq)"),
    ("strings", [band("highpass", 53.0, bw=2.0), band("bell", 456.0, -2.2, 0.75), band("bell", 1005.0, -5.0, 0.945),
                 band("highshelf", 4730.0, 4.0, 0.33)]),
    ("brass", [band("highpass", 41.0, bw=2.0), band("bell", 475.0, -5.4, 1.92), band("bell", 821.0, -7.8, 1.92),
               band("highshelf", 7490.0, 4.0, 1.92)]),
    ("woodwinds", [band("bell", 447.0, -5.1, 0.89), band("bell", 1000.0, -3.1, 0.89), band("bell", 2200.0, -4.7, 1.7),
                   band("highshelf", 7590.0, 5.1, 2.0)]),
    ("harp", [band("highpass", 183.0, bw=2.0), band("bell", 304.0, -8.3, 1.39), band("bell", 1270.0, -8.6, 0.62),
              band("highshelf", 7680.0, 8.0, 1.39)]),
    ("timpani", [band("highpass", 44.0, bw=1.142), band("bell", 84.43, 8.58, 1.39), band("bell", 385.0, -11.5, 2.54),
                 band("highshelf", 6960.0, 9.1, 1.39)]),
])
MASTER_EQ = [band("highpass", 42.0, bw=2.0), band("bell", 167.0, -1.6, 1.39), band("bell", 1180.0, -1.9, 1.39),
             band("highshelf", 8008.0, 0.8, 1.39)]


def verb(chunk, fader, **extra):
    r = OrderedDict([("fx", [OrderedDict([("chunk", chunk), ("fx", "ReaEQ")]), OrderedDict([("chunk", chunk), ("fx", "Spaces")])]),
                     ("fader_db", fader)])
    r.update(extra)
    return r


RETURNS = OrderedDict([
    ("_doc", "mvt1 c50 (TEMPLATE-PLAN section 2): REAPER return tracks, each a ReaEQ then EW Spaces II loaded from the "
             "template's verbatim chunks (return_chunks_dir). Stems 91.. in this order (tools/return_stems.py). A return "
             "is built only when some track sends to it."),
    ("R Strings", verb("STRING_VERB.txt", 1.03, _src="STRING VERB: S. Cal. Hall Strings TS RR 3.3s, pre-delay 19.6 ms; "
                                                     "EQ HPF 87 Hz, -6.7 dB at 2.67 kHz, LPF 8.49 kHz")),
    ("R Brass", verb("BRASS_VERB.txt", 1.03, _src="BRASS VERB: S. Cal. Hall Brass TS RR 3.3s (Horns L / Brass R rear "
                                                  "impulses), 10 ms; EQ HPF 100 Hz, -4.8 dB at 2.57 kHz, LPF 5.63 kHz")),
    ("R Winds", verb("WW_VERB.txt", 1.03, _src="WW VERB: San Francisco Hall TS RR 3.4s, 18.5 ms; EQ as R Brass")),
    ("R Perc", verb("PERC_VERB.txt", 0.66, _src="PERC VERB: Northwest Hall TS RR 2.6s, 10 ms; EQ as R Brass")),
    ("R Glue", OrderedDict([("fx", [OrderedDict([("chunk", "ALGO_GLUE.txt"), ("fx", "ReaEQ")]),
                                    OrderedDict([("chunk", "ALGO_GLUE.txt"), ("fx", "ReaVerbate")])]),
                            ("fader_db", 5.82), ("enabled", False),
                            ("_src", "ALGO GLUE (ReaEQ HPF 100, -0.8 dB at 2.45 kHz, LPF 5.63 kHz; ReaVerbate). Off: the "
                                     "plan tests it in pass 2. Check ReaVerbate's Dry slider in REAPER first.")])),
    ("R Duc", OrderedDict([
        ("fx", [OrderedDict([("reaeq", [band("highpass", 184.0, bw=2.0), band("lowpass", 3000.0, bw=2.0)])]),
                OrderedDict([("chunk", "PERC_VERB.txt"), ("fx", "Spaces"), ("set", OrderedDict([
                    ("presetName", "Hollywood Scoring Stage TS RR 2.3s"),
                    ("fileName", "Hollywood Scoring Stage TS RR 2.3s.preset"),
                    ("path", "/Library/Application Support/East West/EW Spaces II/Presets/Stages/LA Scoring Stages/S-S"),
                    ("folderImage", "/Library/Application Support/East West/EW Spaces II/Presets/Stages/LA Scoring Stages/LA Scoring Stages.png"),
                    ("impulseA", "//ir/LA Scoring Stages/S-S/Hollywood Scoring Stage L Rear"),
                    ("impulseB", "//ir/LA Scoring Stages/S-S/Hollywood Scoring Stage R Rear"),
                    ("delay", 0.012)]))])]),
        ("fader_db", -5.5),
        ("_src", "TEMPLATE-PLAN section 8 (Duc, 'still a bit mushy'): one hall of 2.1-2.45 s; here Spaces II's 2.3 s "
                 "true-stereo rear Hollywood Scoring Stage IR (the PERC VERB state with the IR, preset labels and a 12 ms "
                 "pre-delay replaced), low cut 184 Hz and high cut 3 kHz in a ReaEQ before it, return -5.5 dB. Used by "
                 "send profile 'duc' only. Duc's instruments reach his master through -5.4 dB group buses while his hall "
                 "sends are taken before them, and VSR S24's wet level is not Spaces II's: match the wet level by "
                 "measurement before the A/B (raising this fader by about 5.4 dB copies his routing)."),
    ])),
])


def sends(**kw):
    return OrderedDict(kw)


SEND_PROFILES = OrderedDict([
    ("_doc", "mvt1 c50: post-fader sends per group and profile (build_reaper.py send_list). 'ew' = the template "
             "(ho-mix-fx.json receives; R Glue is disabled in returns, so its sends are skipped); 'duc' = TEMPLATE-PLAN "
             "section 8 (with the celli / basses send_offset_db and send_row_db track keys)."),
    ("ew", OrderedDict([
        ("string", OrderedDict([("R Strings", -5.56), ("R Glue", -9.62)])),
        ("horn", OrderedDict([("R Brass", -8.77), ("R Glue", -5.65)])),
        ("trumpet", OrderedDict([("R Brass", -8.77), ("R Glue", -5.65)])),
        ("lowbrass", OrderedDict([("R Brass", -8.77), ("R Glue", -5.65)])),
        ("wind", OrderedDict([("R Winds", -8.36), ("R Glue", -7.27)])),
        ("timp", OrderedDict([("R Perc", -6.41), ("R Glue", -6.41)])),
        ("perc", OrderedDict([("R Perc", -6.41), ("R Glue", -6.41)])),
        ("harp", OrderedDict([("R Perc", -8.77), ("R Glue", -6.81)])),
    ])),
    ("duc", OrderedDict((g, OrderedDict([("R Duc", 0.0)])) for g in
                        ("string", "horn", "trumpet", "lowbrass", "wind", "timp", "perc", "harp"))),
])
LOW_SHORT_ROWS = {"Celli KS Master": ["Pizzicato RRx4", "Stac RRx9", "Stac On Bow RRx9"],
                  "Basses KS Master": ["Pizz RRx4", "Staccato RRx9"],   # scherzo c06: the rows its basses play
                  "Basses KS Master": ["Pizz RRx4"]}

out = OrderedDict()
for k, v in mix.items():
    out[k] = v
    if k == "_doc":
        out["_c50"] = ("mvt1 c50 template mix (tools/make_template_mix.py; keys in tools/TEMPLATE-TOOLS.md): Opus reverb "
                       "off, REAPER returns per family loaded from the EastWest template's chunks with post-fader sends "
                       "(profile 'ew'; 'duc' for the section 8 A/B), per-mic levels in dB (mic_db) with Close at the seat "
                       "and Main/Mid/Surround full width (pan_by_mic), REAPER track pans (reaper_pan), family EQ "
                       "(family_eq) and the master EQ for the delivery (master_eq). The old keys (mics, width_by_mic, "
                       "send, reverb) stay for a pass-2 copy of the old layout and are inert where the new ones apply.")
out["opus_reverb_off"] = True
out["return_chunks_dir"] = "/Users/gooby/sandbox/claude_composes/symphony/mockup-research/ew-template-2026-11-08/ho-mix-chunks"
out["return_load"] = "vst_chunk"
out["returns"] = RETURNS
out["send_profiles"] = SEND_PROFILES
out["send_profile"] = "ew"
out["family_eqs"] = FAMILY_EQS
out["master_eq"] = MASTER_EQ

for g, e in out["groups"].items():
    if g.startswith("_"):
        continue
    e["mic_db"] = OrderedDict(GROUP_MIC_DB.get(g, {"Close": -6.0, "Main": 0.0}))
    e["pan_by_mic"] = OrderedDict(PAN_BY_MIC)
    e["family_eq"] = FAMILY_OF_GROUP.get(g)
    e["_c50"] = "template mix: mic_db / pan_by_mic / family_eq (the old mics and width_by_mic are inert under them)"

n_mic = n_pan = 0
for name, e in out["tracks"].items():
    if name.startswith("_"):
        continue
    t = parts.get(name)
    src = t.get("alias_of") if t else None
    stem = t["stem"] if t else None
    if stem in MIC_DB:
        e["mic_db"] = OrderedDict(MIC_DB[stem])
        n_mic += 1
    rp = REAPER_PAN.get(name, REAPER_PAN.get(src))
    if rp is not None:
        e["reaper_pan"] = rp
        n_pan += 1
    if stem in LOW_SHORT_ROWS:
        # scherzo c06 (plan update 96d05220: the Duc sends are a default on top of the EW returns): celli and basses longs
        # -1.6 dB under the strings' send, their short rows -7 dB (-1.6 - 5.4), on R Strings as on R Duc
        e["send_offset_db"] = OrderedDict([("R Strings", -1.6), ("R Duc", -1.6)])
        e["send_row_db"] = OrderedDict([(rk, OrderedDict((r, -5.4) for r in LOW_SHORT_ROWS[stem])) for rk in ("R Strings", "R Duc")])
    if stem == "Celli KS Master DIV A":
        e["send_offset_db"] = OrderedDict([("R Duc", -1.6)])

# ---- scherzo c06 (loop/ONE_TIME.md; EW-TEMPLATE-PLAN sections 1, 3, 8) ----
# Seats: the plan gives the template's Close seats for strings and brass (the factory Close pans of the KS Masters); the
# winds, harp and timpani keep the scherzo's seats (the factory wind pans put the flutes right and the clarinets left).
TEMPLATE_SEAT = {"Violins I": -0.31, "Violins II": -0.07, "Violas": 0.0, "Violoncellos": 0.33, "Double basses": 0.62,
                 "Violas div": 0.0, "Horn 1": -0.25, "Horn 2": -0.25, "Horn 3": -0.25, "Horn 4": -0.25,
                 "Trumpet 1": 0.31, "Trumpet 2": 0.31, "Trombone 1": 0.25, "Trombone 2": 0.25, "Bass trombone": 0.25,
                 "Tuba": 0.35}
# Basses: Duc's -2.4..-3.6 dB at 205-250 Hz (plan section 8) as a fifth band of the strings' family EQ
out["family_eqs"]["strings_basses"] = list(FAMILY_EQS["strings"]) + [band("bell", 230.0, -3.0, 1.0)]
# The DIV A / DIV B patches load only a Close mic: keep it at the patch's 0.66 (-3.6 dB), the level their c01-c05 gains
# were matched at (the group's Close -6 dB would drop them 2.4 dB)
DIV_MIC_DB = {"Close": -3.6}
FAMILY_HPF = {"strings": 53.0, "strings_basses": 53.0, "brass": 41.0, "harp": 183.0, "timpani": 44.0}
removed = []
for name, e in out["tracks"].items():
    if name.startswith("_"):
        continue
    t = parts.get(name)
    stem = t["stem"] if t else None
    if name in TEMPLATE_SEAT:
        e["_seat_c05"] = e.get("seat")
        e["seat"] = TEMPLATE_SEAT[name]
    if stem in ("1st Violins KS Master DIV A", "Violas KS Master DIV B"):
        e["mic_db"] = OrderedDict(DIV_MIC_DB)
    if stem == "Basses KS Master":
        e["family_eq"] = "strings_basses"
    fam = e.get("family_eq", out["groups"].get(e.get("group"), {}).get("family_eq"))
    # remove the per-track EQ bands the family EQ now does: a high-pass at or under the family's own high-pass
    # (the woodwinds' family EQ has none, so their 30-40 Hz high-passes stay), and the basses' +4 dB at 180 Hz (c00 port,
    # a body boost against Duc's cut at 205-250 Hz, which the plan makes the default)
    if isinstance(e.get("eq"), list):
        keep = []
        for b_ in e["eq"]:
            if b_.get("band") == "highpass" and fam in FAMILY_HPF and float(b_["hz"]) <= FAMILY_HPF[fam]:
                removed.append(f"{name}: highpass {b_['hz']} Hz (family {fam} {FAMILY_HPF[fam]} Hz)")
                continue
            if stem == "Basses KS Master" and b_.get("band") == "bell" and abs(float(b_["hz"]) - 180) < 1:
                removed.append(f"{name}: bell 180 Hz +4 dB (Duc's basses cut at 230 Hz)")
                continue
            keep.append(b_)
        e["_eq_c05"] = e["eq"]
        e["eq"] = keep
# The family EQ takes 1-10 dB of K-weighted loudness off each track (c05 stems through the new EQ, ffmpeg ebur128,
# cycles/c06/actor_scripts/eq_comp.py): brass -6..-10, woodwinds -2..-5, harp -6..-7, strings -1..-5 dB. The c01-c05
# balance (critics' roles and trims) was set against the old levels, so each track's gain_db gets the loudness back and
# the family EQ changes the colour, not the balance. The mic changes (not simulable) are checked on the render.
EQ_COMP_DB = {"Flute 1": -4.6, "Flute 2": -4.7, "Oboe 1": -4.4, "Oboe 2": -4.2, "Cor anglais": -4.7, "Clarinet 1": -4.6, "Clarinet 2": -4.7, "Bass clarinet": -2.0, "Bassoon 1": -4.8, "Bassoon 2": -4.8, "Contrabassoon": -2.7, "Horn 1": -9.6, "Horn 2": -7.7, "Horn 3": -7.8, "Horn 4": -8.7, "Trumpet 1": -6.1, "Trumpet 2": -7.1, "Trombone 1": -7.2, "Trombone 2": -7.6, "Bass trombone": -7.4, "Tuba": -6.2, "Timpani": -1.7, "Harp": -7.1, "Violins I": -2.0, "Violins II": -2.3, "Violas": -2.1, "Violoncellos": -1.0, "Double basses": -4.6, "Harp harmonics": -6.3, "Violin I solo": -1.8, "Violas div": -1.8}
for name, d_ in EQ_COMP_DB.items():
    e = out["tracks"][name]
    e["_gain_c05"] = e["gain_db"]
    e["gain_db"] = round(e["gain_db"] - d_, 1)
# c06 stem fix (measured on the c06 render, cycles/c06/actor_scripts/kres.py: K-weighted integrated loudness of each stem,
# c05 -> c06): the mic layout (woodwind Close 1.0 as the main mic, harp Mid) made the flutes +3.3..+3.5 dB, Clarinet 2
# +2.7, the bassoons +1.5..+2.1 and the harp +2.2 louder, and the low brass 1.1-2.1 dB softer; each gain takes the residual
# back (residuals under 1.5 dB and those explained by this cycle's roles are left)
MIC_RESIDUAL_DB = {"Flute 1": -3.5, "Flute 2": -3.0, "Clarinet 2": -2.5, "Bassoon 2": -2.0, "Bassoon 1": -1.5, "Harp": -2.0,
                   "Harp harmonics": -2.0, "Trombone 1": 1.0, "Trombone 2": 1.5, "Bass trombone": 2.0, "Tuba": 1.5}
for name, d_ in MIC_RESIDUAL_DB.items():
    out["tracks"][name]["gain_db"] = round(out["tracks"][name]["gain_db"] + d_, 1)
for r_ in removed:
    print("removed", r_)

open(OUT, "w").write(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(f"{OUT}: {len(out['tracks'])} tracks ({n_mic} with a patch mic_db, {n_pan} with reaper_pan), "
      f"{len([k for k in RETURNS if not k.startswith('_')])} returns, profiles {[k for k in SEND_PROFILES if not k.startswith('_')]}")
