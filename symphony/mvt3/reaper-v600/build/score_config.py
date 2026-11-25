"""Movement IV, Finale (symphony/mvt3/v600) score config for score_to_parts.py. Run in score_to_parts.py's namespace: S, W,
B, H, P (patch folders), DYN and every default table are available.

Score qn: 2/2 throughout (bar = 4 qn), bar b starts at qn 4 (b - 1); 279 bars, the final chord (bar 279, qn 1112) is a
quarter followed by rests with a fermata on the last rest; SCORE_END is the end of bar 279 (qn 1116).

mvt3 c00 (port baseline, 2026-11-07): the generic settings are Movement I series 2's values at its c42 (symphony/mvt1/
reaper-v621/build/score_config.py, read with tools/score_to_parts.py's defaults; every family- or track-level value that
does not name a score onset). Every per-onset table of Movement I (shapes, leads, windows, breaths, re-bow points, arcs)
is left out: they belong to Movement I's bars. The per-note tables in build/*.json start empty. The loop's actors add the
Finale's own values below, one dated block per cycle.
"""
SCORE_END = 1116.0
SCORE_TITLE = "mvt3-mockup"

# track name, source staves (mockup.ly staff names), patch file, family, pan (superseded by the seat in build/mix.json).
# Stem numbers follow this order; append new tracks at the end so earlier stems keep their numbers.
# mvt3 c25 (critic C c25 #3b, ruling 9; manual p.122): the bass drum on the 40in Ludwig (same key map as the 36in: Felt
# Short 36, Felt Long / Dbl 38, Roll 40, read with opus_state); env C25_BD=36in restores the 36in
_BD_PATCH = __import__("os").environ.get("C25_BD", "40in") + " Ludwig Bass Drum"
TRACKS = [
    ("Flute 1", ["Fl1"], W + "Flute/05 Keyswitch/FL KS Master.oib", "wind", -0.15),
    ("Flute 2", ["Fl2"], W + "Flute 2/05 Keyswitch/FL2 KS Master.oib", "wind", -0.1),
    ("Oboe 1", ["Ob1"], W + "Oboe/05 Keyswitch/OB KS Master.oib", "wind", 0.05),
    ("Oboe 2", ["Ob2"], W + "Oboe/05 Keyswitch/OB KS Master.oib", "wind", 0.1),
    ("Cor anglais", ["CA"], W + "English Horn/05 Keyswitch/EH KS Master.oib", "wind", 0.15),
    ("Clarinet 1", ["Cl1"], W + "Clarinet/05 Keyswitch/CL KS Master.oib", "wind", -0.2),
    ("Clarinet 2", ["Cl2"], W + "Clarinet/05 Keyswitch/CL KS Master.oib", "wind", -0.15),
    ("Bass clarinet", ["BCl"], W + "Bass Clarinet/05 Keyswitch/BC KS Master.oib", "wind", -0.25),
    ("Bassoon 1", ["Bn1"], W + "Bassoon/05 Keyswitch/BS KS Master.oib", "wind", 0.2),
    ("Bassoon 2", ["Bn2"], W + "Bassoon/05 Keyswitch/BS KS Master.oib", "wind", 0.25),
    ("Contrabassoon", ["Cbn"], W + "Contrabassoon/05 Keyswitch/CB KS Master.oib", "wind", 0.3),
    ("Horn 1", ["Hn1"], B + "Solo French Horn/06 Keyswitch/1FH KS Master.oib", "brass", -0.45),
    ("Horn 2", ["Hn2"], B + "Solo French Horn/06 Keyswitch/1FH KS Master.oib", "brass", -0.4),
    ("Horn 3", ["Hn3"], B + "Solo French Horn/06 Keyswitch/1FH KS Master.oib", "brass", -0.35),
    ("Horn 4", ["Hn4"], B + "Solo French Horn/06 Keyswitch/1FH KS Master.oib", "brass", -0.3),
    ("Trumpet 1", ["Tpt1"], B + "Solo Trumpet/06 Keyswitch/1TP KS Master.oib", "brass", 0.05),
    ("Trumpet 2", ["Tpt2"], B + "Solo Trumpet/06 Keyswitch/1TP KS Master.oib", "brass", 0.1),
    ("Trumpet 3", ["Tpt3"], B + "Solo Trumpet/06 Keyswitch/1TP KS Master.oib", "brass", 0.15),
    ("Trombone 1", ["Tbn1"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.35),
    ("Trombone 2", ["Tbn2"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.4),
    ("Bass trombone", ["BTbn"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.45),
    ("Tuba", ["Tuba"], B + "Solo Tuba/06 Keyswitch/1TU KS Master.oib", "brass", 0.5),
    # v600 prints "hard sticks" (bar 1 and the retuning note): the hard-stick KS patch (same rows and keys as the felt
    # one Movement I used; its TIMP_CC1_MAP / TIMP_ROLL_TRIM_DB below were fitted on felt and need a check on c00)
    ("Timpani", ["Timp"], P + "Drums/Timpani/Timpani Hrd KS.oib", "timp", 0.0),
    # percussion, 2 players: crash cymbals (qn 888, 1048, 1108-1112) and bass drum (888, 1108-1112), one patch each
    ("Crash cymbals", ["Perc"], P + "Cymbals/Cymbal Pairs/22in Zildjian K Crash.oib", "perc", 0.15),
    ("Bass drum", ["Perc"], P + ("Drums/" + _BD_PATCH + ".oib"), "perc", 0.0),
    ("Harp", ["HarpR", "HarpL"], H + "01 Maestro Patches/Harp Sus RR.oib", "harp", -0.55),
    ("Violins I", ["VlnI"], S + "1st Violins/06 Keyswitch/1st Violins KS Master.oib", "string", -0.6),
    ("Violins II", ["VlnII"], S + "2nd Violins/06 Keyswitch/2nd Violins KS Master.oib", "string", -0.3),
    ("Violas", ["Vla"], S + "Violas/06 Keyswitch/Violas KS Master.oib", "string", 0.15),
    ("Violoncellos", ["Vc"], S + "Celli/06 Keyswitch/Celli KS Master.oib", "string", 0.4),
    ("Double basses", ["Cb"], S + "Basses/05 Keyswitch/Basses KS Master.oib", "string", 0.6),
]

# Percussion strokes (score_to_parts.build_perc_track). Keys read from the .oib region maps: 22in K Crash Long = 60
# (7 velocity layers, RRx1-3; 62/64 Short); 36in Ludwig Bass Drum: Felt Short 36, Felt Long 38 (7 layers, RR1-4), Hard
# Short 60, Hard Long 62. v600 prints no beater for the bass drum: felt (the orchestral default). Both instruments let
# ring: the strokes at 888 and 1108 are whole notes tied on, the final quarter at 1112 is under a fermata.
PERC_MAP = {"Crash cymbals": {"crashcymbal": {"key": 60, "min_s": 9.0, "delay_s": 0.05}},
            "Bass drum": {"bassdrum": {"key": 38, "min_s": 6.0, "delay_s": 0.05}}}

# Trumpet 1's muted solo (qn 680 "con sord., dolce cantabile" to 792 "senza sord."): the 1TP KS Master's "Mute Sus" row
# (key 36, read from the patch; loaded only on this track)
ART_SPANS = {"Trumpet 1": [{"from": 679.9, "to": 791.9, "art": "Mute Sus"}]}

# Tempo. The score MIDI realises every printed rit./accel./stringendo/allargando as tempo steps (global.ily \mt; qn bpm):
# 168 (2 = 84) from 0; poco rit. bars 49-50 (160, 150) -> Poco meno mosso 144 at 200; animando bar 82 (152, 160) -> Tempo I
# 168 at 328; poco rit. 149-150 (156, 140) -> 168 at 600; poco rit. 197-198 (160, 150) -> 168 at 792; poco a poco
# accelerando 205-210 (172, 176, 180, 184) -> Largamente 144 at 840; allargando 221-222 (124, 112) -> Maestoso 112 at 888;
# Poco piu mosso 132 at 936; stringendo 245-246 (136, 146, 156, 166) -> Piu allegro 176 at 984; broadening 271-272 (164,
# 152) -> Largamente 144 at 1088. Each stepped span becomes a ramp (start qn, end qn, tempo at the start).
RAMP_SPANS = [(192, 200, 168), (324, 328, 144), (592, 600, 168), (784, 792, 168), (816, 840, 168), (880, 888, 144),
              (976, 984, 132), (1080, 1088, 176)]

# ---------- generic settings carried over from Movement I series 2 at its c42 ----------
DYN.update({"mp+": 65, "mf-": 68, "mf+": 78, "f-": 84})

# dynamics on CC1 for the Hollywood Brass KS Masters and the Clarinet KS Master (their dynamic-layer controller)
CC1_DYN_TRACKS = ("Horn", "Trumpet", "Trombone", "Bass trombone", "Tuba", "Clarinet ")
CC1_HOLD = {"Contrabassoon": 40}

# timpani (Movement I's felt-stick fit; see the TRACKS note)
TIMP_CC1_MAP = [(22, 56), (34, 56), (46, 60), (58, 66), (72, 72), (88, 88), (114, 104), (124, 122)]
TIMP_ROLL_TRIM_DB = [(22, 17.6), (34, 19.0), (46, 18.6), (58, 12.7), (72, 9.5), (88, 7.3), (114, 3.7), (124, 0.0)]
TIMP_DELAY_S = 0.02
TIMP_RH_ALT = {"max_gap_s": 0.8, "add": 24}
TIMP_METRIC_VEL = {"down": 0, "mid": -3, "beat": -5, "off": -9, "jit": 2, "min_cc": DYN["f"]}
METRIC_TIMP_DB = {"down": 0.0, "mid": -1.0, "beat": -2.0, "off": -3.0, "min_cc": DYN["f"]}
TIMP_ROLL_RESTRIKE = dict(TIMP_ROLL_RESTRIKE, at=[], min_s=6.0, seg_s=(2.5, 3.3), vel_jit=3, dip_db=-1.5,
                          dip_s=(0.03, 0.14, 0.22))

# legato and entry leads (seconds), per family and track
LEG_LEAD_S = {"Flute 2": 0.05, "Violins II": 0.2, "Violas": 0.2, "string": 0.17, "brass": 0.1, "Oboe": 0.05,
              "Bassoon": 0.06, "Bass clarinet": 0.05, "Cor anglais": 0.05, "Flute": 0.03, "Clarinet": 0.05, "wind": 0.0,
              "Horn": 0.06}
ENTRY_LEAD_S = dict(ENTRY_LEAD_S, **{"Horn 1": (0.06, 0.09, 0.05), "Horn 2": (0.06, 0.08, 0.05),
                                     "Trumpet 2": (0.06, 0.09, 0.05), "Trumpet 3": (0.06, 0.07, 0.05),
                                     "Trombone 1": (0.06, 0.07, 0.05), "Bassoon 1": (0.06, 0.12, 0.06),
                                     "Oboe 2": (0.0, 0.14, 0.0), "Flute 2": (0.0, 0.06, 0.0),
                                     "string": (0.12, 0.06, 0.12), "Double basses": (0.12, 0.06)})
ENTRY_LEAD_ART_S = dict(ENTRY_LEAD_ART_S, wind={"Leg Slur MAX": 0.055, "Leg Slur": 0.055, "Sus Non Vib": 0.035})
ENTRY_LEAD_ART_S["Flute"] = dict(ENTRY_LEAD_ART_S["wind"], **{"Sus MAX": 0.04})
ENTRY_LEAD_ART_S["Oboe"] = dict(ENTRY_LEAD_ART_S["Flute"])
LEG_PAIR_EXTRA_S = {"Violoncellos": {(56, 60): 0.15},
                    "Violas": {(60, 63): 0.1, (65, 61): 0.12, (58, 61): 0.1, (57, 60): 0.1, (60, 58): -0.1,
                               (65, 64): -0.08, (52, 51): -0.08},
                    "Horn 1": {(65, 70): -0.12},
                    "Oboe 1": {(73, 72): 0.1, (77, 75): 0.05, (76, 74): 0.12, (74, 72): 0.1}}
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{t_: [(0.0, SCORE_END, 0.75)]
                                     for t_ in ("Violins I", "Violins II", "Violas", "Violoncellos")})
LEG_MIN_GAP_S = {"Violoncellos": 0.1, "Violas": 0.1, "Violins II": 0.1, "Violins I": 0.06}
LEG_VEL_EXTRA_S = {"Bass clarinet": (70, 0.09), "Oboe": (70, 0.05), "wind": (70, 0.04)}
LEG_ART_EXTRA_S = {"Violins II": {"Leg Slur MAX": 0.04, "Leg BC MAX": 0.0},
                   "Violoncellos": {"Leg Slur MAX": 0.05, "Leg BC MAX": -0.02},
                   "Violas": {"Leg Slur MAX": 0.025, "Leg BC MAX": 0.05}, "Violins I": {"Leg BC MAX": 0.05}}
SHORT_SUS_LEG_TRACKS = ("Violins I",)
SHORT_SUS_LEAD_S, SHORT_SUS_LEAD_TRACKS, SHORT_SUS_LEAD_KEEP_OVERLAP = 0.1, ("Violins II",), 0.03
SHORT_SUS_LEAD_CAP_FRAC = 0.45
RETONGUE_LEAD_S = {"Horn 1": 0.09, "Horn 2": 0.09, "Trumpet 2": 0.08, "Trumpet 3": 0.08, "Tuba": 0.07, "Oboe 2": 0.12,
                   "Cor anglais": 0.08, "Oboe 1": 0.07, "brass": 0.05, "wind": 0.035, "Violins II": 0.1,
                   "Violins I": 0.1, "Violas": 0.1, "Violoncellos": 0.1, "Flute 2": 0.07}
RETONGUE_LEAD_ART_S = {"Oboe 1": {"Leg Slur MAX": 0.08}}
RETONGUE_LEAD_SLOW_S = {"Bassoon": 0.06, "string": 0.07, "wind": 0.04, "brass": 0.05}
SLUR_HEAD_LEAD = {"string": True, "lead_s": 0.1}
STAC_ROW = {"Violins I": "Staccatissimo RRx9"}
STAC_LEAD_S = {"Violins I": 0.045, "Violas": 0.04, "Violins II": 0.035, "Violoncellos": 0.025, "Cor anglais": 0.03}
TREM_JOIN_LEAD_S = 0.22
TREM_ENTRY_LEAD_S = 0.04
TREM_SPLIT = dict(TREM_SPLIT, clear_qn=1.0)
DETACH_LEAD_KEEP_QN = 0.15
UNI_DELAY_OVERLAP_QN, UNI_DELAY_FADE = 0.25, (-12.0, 0.2)
CUTOFF_EARLY_S = {"string": 0.05, "brass": 0.04}

# string rows and finger positions
ROW_TRIM_DB = {"Violins II": {"Sus MAX": (-4.0, 80)},
               "Violas": {"Sus MAX": (-4.5, 80), "Stac RRx9": (-4.0, 80)},
               "Violoncellos": {"Sus MAX": (-1.5, 80), "Stac RRx9": (-4.0, 80)},
               "Violins I": {"Sus MAX": (-1.5, 80), "Staccatissimo RRx9": (-3.0, 80)}}
SUL_DEFAULT_CC70 = 127
SUL_FP4_CC70 = 127
STR_REP_AFTER_STAC = {"max_qn": 1.0, "max_gap_qn": 0.5}
METRIC_BOWED_REP = True

# winds and brass: detached notes, repeats, breaths, accents
WIND_DETACH = {"gap_s": 0.05, "frac": 0.12,
               "by": {"brass": {"gap_s": 0.09, "frac": 0.18, "dip_db": -5.0, "dip_fall_s": 0.05, "dip_min_cc": 84}}}
WIND_REP_RETONGUE_BY = {"Horn 4": {"gap_s": 0.14, "frac": 0.35, "fall_cc": 14, "fall_s": 0.18},
                        "Horn": {"gap_s": 0.1, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15},
                        "Trombone": {"gap_s": 0.08, "fall_cc": 10}}
WIND_REP_RETONGUE_SHORT = {"max_qn": 0.5, "min_bpm": 100.0, "gap_s": 0.1, "frac": 0.45, "fall_cc": 8}
WIND_REP_PORTATO = True
PORTATO_TAIL_JOIN = True
WIND_WIDE_LEG = 12
BREATH_FALL_BY = {"Horn": 10}
BREATH_SPLIT = dict(BREATH_SPLIT, dip_db=-1.5)
SLUR_START_SUS = {"families": ("wind", "brass"), "max_qn": 0.6, "after_qn": 0.15}
SLUR_PAIR_RELEASE = dict(SLUR_PAIR_RELEASE, short_s=0.35, full_short_s=0.12, join_db=-3.0)
REP_ROW_GAP_S = (0.06, 0.15)
REP_ROW_REPEATS_ONLY = ("brass",)
PICKUP_LIFT_TAIL_S = {"wind": (0.04, 0.08), "brass": (0.06, 0.08), "Oboe 1": (0.02, 0.06), "Oboe 2": (0.02, 0.06),
                      "string": (0.06, 0.08)}
LEG_JOIN_TRIM_HOLD = {"wind": (0.04, 0.08), "brass": (0.06, 0.08), "string": (0.06, 0.08), "Oboe 1": (0.02, 0.06),
                      "Oboe 2": (0.02, 0.06)}
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass=dict(GENTLE_ACCENT["brass"], db=2.5, keep_legato=True))
ACCENT_BODY_S_SHORT = (0.18, 0.28)
SYNCO_SHAPE = {"families": ("string",), "min_bpm": 100, "rest_qn": 0.25, "len_qn": (0.75, 2.5),
               "pts": [(-0.12, 6.0), (0.1, 6.0), (0.25, 3.0), (0.45, 0.0), (0.6, -3.0)]}
HP_SF_TARGET = {"staves": ("Hn1", "Hn2", "Hn3", "Hn4", "Tpt1", "Tpt2", "Tpt3", "Tbn1", "Tbn2", "BTbn", "Tuba"),
                "to": "f", "from_f": "ff"}
HP_NIENTE = {"steps": 2, "rest_qn": 1.0}
HELD_DECRESC_DB = {"wind": 3.0, "string": 3.0}
PHRASE_RETURN_AFTER_OPEN = False

# harp
HARP_RING_S = 2.0
HARP_PITCH_VEL = {55: -6, 56: -12, 58: 5, 60: 5, 61: 9, 63: 0, 64: -8, 65: -12, 66: -12, 67: 6, 68: -9, 70: -12,
                  72: -7, 73: 12, 75: -12, 76: -10, 77: -12, 78: 12, 81: 12, 82: 12, 83: 10, 84: 10, 85: -12,
                  86: 12, 87: 12, 88: 12, 89: 12, 92: 5, 94: 12, 96: 4, 97: 12}

# ---------- mvt3 c01 (2026-11-07; critics on the c00 render: cycles/c01/reports/A-C.md) ----------
# critic A #1: printed staccatos on the brass / bassoon KS Masters' short rows instead of half-length Sus slices (Horn
# 3/4 -10 dB length 0.48 s against a written quarter of 0.36 s and the strings' 0.27-0.33 s). Rows read from ks_maps:
# 1FH "StacSs RRx9" (key 27), "Marc Shrt RRx4" (28); BS / 1TP "Stac DblTng RRx9" (28). Velocity is the layer (manual
# p.102: avoid the top velocities). Horns 3/4: StacSs in F1 (qn 40-104, f) and Marc Shrt in the ff recapitulation
# (600-664) as an A/B in one render
_hn_stac_vel = [(60, 70), (90, 88), (110, 98), (124, 100)]
ART_SPANS = dict(ART_SPANS, **{
    "Horn 3": [{"from": 40.0, "to": 104.0, "art": "StacSs RRx9", "mark": "staccato", "vel_by_cc": _hn_stac_vel},
               {"from": 600.0, "to": 664.0, "art": "Marc Shrt RRx4", "mark": "staccato", "vel_by_cc": _hn_stac_vel}],
    "Horn 4": [{"from": 40.0, "to": 104.0, "art": "StacSs RRx9", "mark": "staccato", "vel_by_cc": _hn_stac_vel},
               {"from": 600.0, "to": 664.0, "art": "Marc Shrt RRx4", "mark": "staccato", "vel_by_cc": _hn_stac_vel}],
    "Bassoon 1": [{"from": 40.0, "to": 132.0, "art": "Stac DblTng RRx9", "mark": "staccato",
                   "vel_by_cc": [(58, 72), (72, 82), (88, 96), (114, 104)]}]})
for _tp in ("Trumpet 1", "Trumpet 2", "Trumpet 3"):
    ART_SPANS[_tp] = ART_SPANS.get(_tp, []) + [{"from": 632.0, "to": 664.0, "art": "Stac DblTng RRx9", "mark": "staccato",
                                                "vel_by_cc": [(88, 88), (114, 98), (124, 100)]}]
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Bassoon 1": 0.03})
# critic A #2 (S1): the basses' hammered repeated eighths (coda 199-210, Piu allegro to the Largamente 247-277) ran
# together (re-attack dip median 4.3-5.3 dB, 67 under 3 dB; eighth-grid fold 1.9-3.1 dB). Movement I's c22 dip and +1.5
# dB hold (its bars 27-31: dip median 8.0, fold 5.5 dB), min_cc lowered to f so the f stretches are included; and
# Movement I's c37 metric steps on the lower strings
STR_REP_DETACH = {"at": {"Double basses": [(792.0, 840.25), (984.0, 1108.25)]},
                  "dip_db": -5.0, "dip_s": 0.08, "ramp_s": 0.02, "back_s": 0.005, "max_qn": 0.5, "min_cc": 72}
LEVEL_SHAPES = dict(LEVEL_SHAPES, **{"Double basses": [[(791.85, 0.0), (791.95, 1.5), (840.0, 1.5), (840.1, 0.0)],
                                                        [(983.85, 0.0), (983.95, 1.5), (1108.0, 1.5), (1108.1, 0.0)]]})
METRIC_BOWED = {tn_: [(792.0, 816.0), (984.0, 1080.0)] for tn_ in ("Violas", "Violoncellos", "Double basses")}
# critic A #4: sul tasto on violas / celli / basses (no Flautando row) as the non-vibrato layer; "last 2 desks" /
# "last desk" (qn 376-392) a quarter section; a Flautando note split at a re-bow keeps Flautando (REBOW_KEEP_ARTS)
TASTO_CC1 = 0
LAST_DESK_DB = -4.0
# critic A #5: the harp's bar 43/45/47 harmonics (written B flat 3, "sound 8va"; mockup.midi has 70) on the harp track, and the bar 277
# glissando G3 -> G6 on C-D-E-G-A (finale.ily) written out up to E6, the landing chord's G6 at 1108 unchanged
HARM_ON_TRACK = {"Harp": 0}   # the MIDI already carries the sounding B flat 4 (70)
GLISS_SPANS = {"HarpR": [(1106.0, 1107.9, 55, 88, (0, 2, 4, 7, 9), 90, 112)]}
# critic B #1 (and C #4): the fff arrivals (qn 888, 1048, 1108) put woodwinds +7.9 dB and strings +6.9 dB in the
# post-hall envelope against brass +2.9 (hairpin gains chained into fff with CC11 already at 126). Finale: no extra fff
# chain rise on winds and strings
HP_CHAIN_RISE_FFF = {"wind": 0.0, "string": 0.0, "brass": 0.5}
# critic B #2: the Violins I / II Tremolo rows sit 3-9 dB over their Sus rows (bars 224-225, 255-262, 273-277 covered
# the chorale)
ROW_GAIN_DB = {"Violins I": {"Tremolo": -3.0}, "Violins II": {"Tremolo": -4.0}}

# ---------- mvt3 c02 (2026-11-07; critics on the c01 render: cycles/c02/reports/A-C.md) ----------
# critic A #1 (Dan's S1; Movement I c44's STR_REP_NEW_BOW ported in tools/score_to_parts.py, same values): a same-pitch
# string repeat that the legato merge joined into the note before (49 in the Finale, e.g. Vc 602 one 6.62 qn note over
# four printed half notes; stem dips 0-3 dB) is a new bow when not inside the note before's slur: loud ones a fresh Sus
# MAX stroke after min(0.06 s, 25%); slurred tenuto repeats (the louré at 796, 988) after min(0.05 s, 25%) with a 6 / 8
# CC fall; pp-p ones a re-bow point. Repeats inside one slur stay merged (the "change bow at will" chorale notes, the
# slurred portato quarters)
STR_REP_NEW_BOW = {"gap_s": 0.06, "frac": 0.25, "stroke_cc": DYN["mf"], "stroke_mark": "mp", "head_cc": DYN["p"], "sus_min_s": 0.4,
                   "portato": {"gap_s": 0.05, "frac": 0.25, "fall_cc": 6, "fall_cc_loud": 8, "fall_s": 0.04}}
# A #1: the basses' repeated half / quarter notes of the f-ff bass line outside the coda detach spans (median dip 2.2 dB,
# 25 of 40 under 3): the same -5 dB / 0.08 s dip before same-pitch repeats up to a half note
STR_REP_DETACH["at"]["Double basses"] = sorted(STR_REP_DETACH["at"]["Double basses"] + [
    (a_, b_, {"max_qn": 2.0, "same_pitch_only": True}) for a_, b_ in ((64.0, 104.0), (148.0, 172.0), (596.0, 672.0))],
    key=lambda s_: s_[0])
# A #1: bassoons / contrabassoon re-tongue repeats with the horns' gap and fall (0.06 s and 6 CC were filled by the release
# and hall at G1-G2: dips 1.7-2.3 dB; the bass trombone's 0.08 s measured 7 dB)
WIND_REP_RETONGUE_BY = dict({"Bassoon": {"gap_s": 0.1, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15},
                             "Contrabassoon": {"gap_s": 0.1, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15}},
                            **WIND_REP_RETONGUE_BY)
# A #2 (S2): only Violins II led its slurred Sus MAX eighths (0.1 s), 57 ms ahead of Violins I and the violas in unison
# (120 notes); all three upper sections now lead the same, smaller amount
SHORT_SUS_LEAD_S, SHORT_SUS_LEAD_TRACKS = 0.06, ("Violins I", "Violins II", "Violas")
# A #3: horn staccatos: Horns 3/4 F1 off-beats StacSs (-10 dB length 0.10 s, the shortest notes in the texture) ->
# Marc Shrt RRx4 (0.18 s); Horn 1's staccatos in the F1 tune on Marc Shrt too (they rang 0.26-0.29 s on Sus / Leg rows)
for _hn in ("Horn 3", "Horn 4"):
    ART_SPANS[_hn] = [dict(sp_, art="Marc Shrt RRx4") if sp_["from"] == 40.0 else sp_ for sp_ in ART_SPANS[_hn]]
ART_SPANS["Horn 1"] = ART_SPANS.get("Horn 1", []) + [
    {"from": a_, "to": b_, "art": "Marc Shrt RRx4", "mark": "staccato", "vel_by_cc": _hn_stac_vel}
    for a_, b_ in ((40.0, 104.0), (552.0, 664.0), (816.0, 828.0), (1056.0, 1076.0))]
# A #4: the printed portamento at bar 236 (Vln I / II C5 -> A5, "port." under "sul A") on Leg Port MAX (Movement I's
# velocity 100); the row is loaded, so both tracks need a full rebuild
PORT_TARGETS = {"Violins I": {941.0: 100}, "Violins II": {941.0: 100}}
# A #5: the violas' f portato entry at bar 224 started a merged Leg Slur MAX note from nothing (10.9 dB hole at 893):
# its first note is a fresh Sus MAX stroke
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violas": [892.0]})
# critic C #3: the sfp at bar 149 (qn 592) had no sf (spike 43 ms at 168 qpm, notes at the p velocity 53): the sf level
# is held 0.12 s and falls to p by 0.30 s; the notes at the mark take velocity 96 (Sus rows; legato targets keep theirs)
SFP_SPIKE_S, SFP_VEL = (0.12, 0.30), 96
# critic C #1 (b): the fff arrivals of bars 263 and 278 read level with the accented chords before them: Movement I's
# arrival weight with the short 0.5 qn hold-back
ARRIVAL_WEIGHT_AT = {**ARRIVAL_WEIGHT_AT, 1108.0: (-1.0, 2.0, 0.5), 1048.0: (-1.0, 1.5, 0.5)}
# critic C #1 (c): the held fff of bar 278 sags with CC1 flat (last minus first quarter: Horn 1 -5.1, Bass trombone -4.4,
# Trumpet 2 -3.5 dB): counter-shapes to about 80% of the sag
for _t, _d in (("Horn 1", 4.0), ("Bass trombone", 3.5), ("Trumpet 2", 3.0)):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(1108.5, 0.0), (1112.5, _d), (1113.0, _d), (1113.2, 0.0)]]
# critic C #2 (BRIEF item 6): delivered LRA 17.0 LU / span 21.4 dB: the p-pp passages (second theme 51-66 and its
# return 171-186, bassoon solo / harp 114-126, transition 43-50, 95-98) sat at the ride's +10 dB cap. Delivery-ride
# trims (deliver_master.py), ramps of 1 qn ending at the next louder entry; refit on the render
RIDE_TRIMS = [[(167.0, 0.0), (168.0, 1.5), (199.0, 1.5), (200.0, 3.0), (263.0, 3.0), (264.0, 0.0)],
              [(375.0, 0.0), (376.0, 1.5), (391.0, 1.5), (392.0, 0.0)],
              [(451.0, 0.0), (452.0, 2.5), (503.0, 2.5), (504.0, 0.0)],
              [(679.0, 0.0), (680.0, 3.0), (743.0, 3.0), (744.0, 0.0)]]
# A #1 scope: the chorale's "change bow at will" whole notes (Vc / Cb 892-940) keep the merge and its staggered re-bows
# (the critic's keep list). The slurred portato quarters (Violas 893-911, Violins II 921-931) are portato strokes like
# the louré (with the violas' head at 892 a Sus MAX stroke, a kept merge after it would start an unled Leg Slur note)
STR_REP_NEW_BOW["skip"] = {"Violoncellos": [(892.5, 940.5)], "Double basses": [(892.5, 940.5)]}
# the slur heads that followed a portato / repeat stroke lost the legato join they had from the merged note before
# (they would start as unled Leg BC MAX notes): fresh Sus MAX strokes too
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violas": [892.0, 896.0, 900.0, 904.0, 906.0, 908.0, 912.0],
                                               "Violins II": [924.0, 928.0, 932.0], "Violins I": [431.0]})
# refit on the c02 render (delivery only, deliver_master.py rerun on the c02 master): the soft-passage trims x0.85
# (LRA 14.2 -> 14.6 LU), and C #4's fallback: the final Largamente 273-276 +2.5, the retransition stop chord 147-150 -1.5
# (mp3 RMS 273-276 was 2.5 dB under 147-150; now 1.4 dB over; 223 and 278 stay the loudest, limiter 2.3 dB)
RIDE_TRIMS = [[(q_, round(d_ * 0.85, 3)) for q_, d_ in r_] for r_ in RIDE_TRIMS] + [
    [(1087.0, 0.0), (1088.0, 2.5), (1103.0, 2.5), (1104.0, 0.0)], [(583.0, 0.0), (584.0, -1.5), (599.0, -1.5), (600.0, 0.0)]]

# ---------- mvt3 c03 (2026-11-07; critics on the c02 render: cycles/c03/reports/A-C.md) ----------
# no-WARNING rule (64 lines through c02): fp / sfp checked after the attack (tools), and two hairpin shapes that missed
# their printed marks: mf > mf / sf > p with a new note at the mark (the mark restates), ff < > ff / pp < > pp (a swell
# from the mark, not a "niente <" 12 CC under it)
HP_DIM_RESTATE, HP_SWELL_AT_MARK = True, True
# critic C #1 (S2): the note after an accented slur head (F1's head motive: wind +87..+101, brass +94..+137 ms) and the
# long note after slurred loud eighths (strings, +118 ms) were unled first notes on the legato row
ACC_HEAD_JOIN = True
SHORT_SUS_DETACH_JOIN_LEG = True
# critic C #2 (S2): string entries after rests on Leg Slur MAX (+68 ms behind brass) and tremolo entries (+40 ms)
ENTRY_LEAD_ART_S = dict(ENTRY_LEAD_ART_S, string=dict(ENTRY_LEAD_ART_S.get("string", {}), **{"Leg Slur MAX": 0.06}))
TREM_ENTRY_LEAD_S = 0.08
# critic C #3 (S2): the basses' abutting long pitch changes on Sus MAX (no Leg BC row) landed +66 ms after the
# orchestra (Movement I's ABUT_LEAD, not carried over by the port); only notes of 0.75 qn or longer
ABUT_LEAD = dict(ABUT_LEAD, **{"Double basses": {"lead_s": 0.07, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True,
                                                  "rebow_ok": True, "cap_frac": 0.45, "min_qn": 0.75}})
# critic C #6a: the allargando into the 223 arrival extrapolated to 106.4 qpm under its printed 112
RAMP_END_CLAMP = True
# critic A #1 (S1): portato / louré gaps 43-50 ms were filled by the release (harmonic-band dips 1-3 dB); tenuto repeats
# (Vc 324-327, 976-983) a new bow; the basses' tenuto repeats in bar 82 and 245-246 take the detach dip
STR_REP_NEW_BOW["portato"] = {"gap_s": 0.08, "frac": 0.25, "fall_cc": 10, "fall_cc_loud": 12, "fall_s": 0.06}
STR_REP_NEW_BOW["tenuto"] = {"gap_s": 0.07, "frac": 0.25, "fall_cc": 8, "fall_s": 0.05}
STR_REP_DETACH["at"]["Double basses"] = sorted(STR_REP_DETACH["at"]["Double basses"] + [
    (a_, b_, {"max_qn": 2.0, "same_pitch_only": True}) for a_, b_ in ((322.0, 328.0), (976.0, 984.0))], key=lambda s_: s_[0])
# A #1: Trombone 1's slurred repeat into the tenuto at 988 dipped 0.9 dB: the horn re-tongue values
WIND_REP_RETONGUE_BY = dict(WIND_REP_RETONGUE_BY, **{"Trombone 1": {"gap_s": 0.1, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15}})
# critic A #2: the printed stopped-horn notes ("+", mockup-events `stopped`) on the 1FH KS Master's "Stop Sus" row (key
# 80, keys 36-76, the Sus MAX layer scheme); the open "Sus MAX" played them before
for _hn, _sp in (("Horn 1", [(191.9, 199.9), (667.9, 675.9)]), ("Horn 2", [(667.9, 675.9)]),
                 ("Horn 3", [(547.9, 551.9)]), ("Horn 4", [(547.9, 551.9)])):
    ART_SPANS[_hn] = ART_SPANS.get(_hn, []) + [{"from": a_, "to": b_, "art": "Stop Sus"} for a_, b_ in _sp]
# critic A #3 (S2): Trumpet 1's p dolce solo (bars 51-66) arrived 47 ms early on v124 slurs: a slower transition
# (manual p.106: velocity is the transition speed) with leg_leads.json offsets of -0.035 s on its targets
LEG_VEL_SPANS = dict(LEG_VEL_SPANS, **{"Trumpet 1": [(200.5, 264.0, 96)]})
# critic A #6: the bar-236 portamento was a short scoop: a slower slide
PORT_TARGETS = {"Violins I": {941.0: 80}, "Violins II": {941.0: 80}}
# critic B #1: Movement I's felt-stick roll trims flattened the hard-stick rolls to 6.6 dB from p to fff (a p roll the
# 5th-loudest stem at 872); refit on the c02 hard-stick layer curve to f-20 .. f+5
TIMP_ROLL_TRIM_DB = [(22, 7.7), (34, 9.2), (46, 10.7), (58, 9.8), (72, 9.4), (88, 7.3), (114, 5.9), (124, 2.6)]
# critic B #2: the final fff roll (1108) fell 5 dB under the settle and dropped out of the last chord
TIMP_SETTLE_SKIP = [1108.0]
# critic B #5: the bass drum is printed ff under the crash's fff at 888 and 1108 (both read the staff's last mark, fff)
PERC_MAP["Bass drum"]["bassdrum"]["vel"] = 114

# ---------- mvt3 c04 (2026-11-07; critics on the c03 render: cycles/c04/reports/A-C.md) ----------
# critic A #1 (S2): wind legato targets at v80 / v90 kept the v100 lead and arrived 100-190 ms late (LegatoSpeed: a lower
# velocity starts the transition sample later); per-track (velocity at or below, extra s) lists from the measured excess
# over each track's v100 median (tools: a list form of LEG_VEL_EXTRA_S)
LEG_VEL_EXTRA_S = {"Bass clarinet": (70, 0.09),
                   "Bassoon": [(60, 0.16), (80, 0.09)],
                   "Oboe 1": [(60, 0.10), (80, 0.07)], "Oboe 2": [(60, 0.12), (80, 0.11)],
                   "Cor anglais": [(80, 0.05), (90, 0.08)],
                   "Flute 2": [(60, 0.10), (80, 0.06)], "Flute 1": [(60, 0.07), (80, 0.03)],
                   "Clarinet 2": [(80, 0.02)], "Clarinet 1": [(60, 0.0)], "wind": (70, 0.04)}
# critic A #1.3: Flute 1's soft joins at 169.5-171.5 landed 37-45 ms early
LEG_SOFT_EXTRA_S = dict(LEG_SOFT_EXTRA_S, **{"Flute 1": (50, 0.03)})
# critic A #3 (manual p.110; Dan: mushy): printed wind staccatos on the KS Masters' "Stac DblTng RRx9" row (key 28) over
# the whole piece, Bassoon 1's velocity map; they were Sus / Leg slices that swelled into the note-off (band peak +114..
# +182 ms after the onset against +74 ms on Bassoon 1's staccato row)
_ww_stac_vel = [(58, 72), (72, 82), (88, 96), (114, 104)]
for _w in ("Flute 1", "Flute 2", "Oboe 1", "Clarinet 1"):
    ART_SPANS[_w] = ART_SPANS.get(_w, []) + [{"from": 0.0, "to": SCORE_END, "art": "Stac DblTng RRx9",
                                              "mark": "staccato", "vel_by_cc": _ww_stac_vel}]
ART_SPANS["Bassoon 1"] = [dict(ART_SPANS["Bassoon 1"][0], to=SCORE_END)]
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Flute 1": 0.03, "Flute 2": 0.03, "Oboe 1": 0.03, "Clarinet 1": 0.03})
# critic C #4 (S2): per-onset string legato leads (build/leg_leads.json, fitted on the c02 / c03 pcX); a listed join may
# lead up to 0.9 of the previous note (the new joins after slurred eighths were held at 0.75 of the eighth: +85..+128 ms)
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{t_: [(0.0, SCORE_END, 0.9, "listed")] + LEG_CAP_FRAC.get(t_, [])
                                     for t_ in ("Violins I", "Violins II", "Violas", "Violoncellos")})
# Movement I c45 (coordinator, 2026-11-07): STR_REP_NEW_BOW "sus_min_s" repeats take the string re-tongue lead (tools);
# the basses have no RETONGUE_LEAD_S value, so "sus_lead_s" 0.10 s (Movement I's value)
STR_REP_NEW_BOW["sus_lead_s"] = 0.10

# ---------- mvt3 c05 (2026-11-07; critics on the c04 render: cycles/c05/reports/A-C.md) ----------
# critic A #3: the final crash and bass drum (bar 278 whole notes tied to the bar-279 quarter) stop with the orchestra's
# last quarter at 1113 (finale.ily: cymc1->\fff~ | cymc4 r4 r2\fermata; the fermata is on the rest); min_s 9.0 / 6.0 rang
# them into the silent fermata (crash alone on the master from +1 s). The 888 / 1048 strokes keep min_s
PERC_END_AT = {"Crash cymbals": {1108.0: 1113.2}, "Bass drum": {1108.0: 1113.2}}
# c05 stem fix (measured on the c05 render): the note-off at 1113.2 did not damp the crash; it rang on at about 7 dB/s
# (crash stem -50.1 dB at +1 s after the cut-off, the master -49.3: still the whole tail). The players damp at the cut-off:
# a post-hall fall over 1 s (40 / 30 dB, about the hall's own decay rate, RT60 1.5-2 s) from the note-off (PERC_MAP _damp)
PERC_MAP["Crash cymbals"]["_damp"] = [(1113.2, -40.0, 1.0)]
PERC_MAP["Bass drum"]["_damp"] = [(1113.2, -30.0, 1.0)]
# critic A #1 (S1, S2): the violas' ff repeated quarters at 176 qpm (1033-1047, 0.34 s) fell under sus_min_s 0.4 and got
# neither the new-bow gap nor the re-tongue lead (pc +111 ms, dip 4.4 dB)
STR_REP_NEW_BOW["sus_min_s"] = 0.3
# critic A #1.2: the celli's Sus MAX repeat strokes on the ff bass line (604-658) still arrive +136..+184 ms with the
# 0.10 s lead: 0.07 s more on Sus MAX re-tongue leads (0.6 x the excess)
RETONGUE_LEAD_ART_S = dict(RETONGUE_LEAD_ART_S, **{"Violoncellos": {"Sus MAX": 0.07}})
# critic A #5 (S2): cello pizzicato landed +42 ms (pc) against the basses' +3 ms on all 24 shared onsets; Violins II +25
PIZZ_LEAD_S = {"Violoncellos": 0.035, "Violins II": 0.015}
# critic A #4 (S2): muted Trumpet 1 (Mute Sus, butted fresh attacks, no lead) trailed the cor anglais it doubles by 35 ms
ROW_LEAD_S = {"Trumpet 1": {"Mute Sus": 0.035}}

# ---------- mvt3 c06 (2026-11-08; critics on the c05 render: cycles/c06/reports/A-C.md; EastWest template mix in mix.json) ----------
# critic A #1 (S2): the crash and bass drum strokes were delayed 0.05 s (PERC_MAP delay_s, Movement I c03 by analogy with
# felt timpani, never measured on the crash): the crash reached -6 dB at +98..+104 ms against the brass -3 dB at
# +13..+47 ms at 888 / 1048 / 1108. Percussion on the beat (EW research section 7); the crash's own rise to -10 dB
# takes about 45 ms, so a 0.02 s lead. PERC_END_AT (1113.2) and the _damp stay
PERC_MAP["Crash cymbals"]["crashcymbal"].update({"delay_s": 0.0, "lead_s": 0.02})
PERC_MAP["Bass drum"]["bassdrum"]["delay_s"] = 0.0

# ---------- mvt3 c07 (2026-11-08; critics on the c06 render: cycles/c07/reports/A-C.md; EW research batches 1-5) ----------
def _front(tbl, **kw):
    """the table with these keys first (by_name takes the first key contained in the track name)"""
    return dict(kw, **{k_: v_ for k_, v_ in tbl.items() if k_ not in kw})
# critic A #1 (S1; EW brass repeat median 98 ms): trumpets, trombones, bass trombone and tuba re-tongue after 0.10 s with
# the brass fall (trumpets 80-89 ms, B.tbn / tuba 60 ms: dry+return dips 4.9-5.8 dB, 5-9 repeats under 3 dB); prefix
# lookup, so "Bass trombone" needs its own key; first match wins
_brass_rt = {"gap_s": 0.10, "frac": 0.3, "fall_cc": 10, "fall_s": 0.15}
WIND_REP_RETONGUE_BY = _front(WIND_REP_RETONGUE_BY, **{"Trumpet": dict(_brass_rt), "Trombone": dict(_brass_rt),
                                                      "Bass trombone": dict(_brass_rt), "Tuba": dict(_brass_rt)})
WIND_REP_RETONGUE_BY.pop("Trombone 1", None)   # (shadowed by "Trombone" since c03; same gap)
# A #1.2 (EW strings 90 ms): string new-bow strokes, tenuto and portato repeats after 0.09 s
STR_REP_NEW_BOW.update({"gap_s": 0.09, "frac": 0.3})
STR_REP_NEW_BOW["tenuto"]["gap_s"] = 0.09
STR_REP_NEW_BOW["portato"]["gap_s"] = 0.09
# A #5 (S1): a same-pitch voice inside a div. chord, not slurred, at mf or louder: the new-bow gap (it kept 11-16 ms)
STR_REP_NEW_BOW["chord"] = {"gap_s": 0.09, "frac": 0.3}
# A #1.3 (S1): the celli's f-ff Sus MAX repeats (604-658, 828) merged with their release (dips 1.7-3.9 dB, pc +121..+204
# ms): the basses' -5 dB / 0.08 s detach dip before same-pitch repeats up to a half note; the extra 0.07 s Sus MAX
# re-tongue lead (c05, bought about 10 ms) is removed
STR_REP_DETACH["at"]["Violoncellos"] = [(a_, b_, {"max_qn": 2.0, "same_pitch_only": True}) for a_, b_ in (
    (64.0, 104.0), (320.0, 330.0), (432.0, 440.0), (560.0, 580.0), (596.0, 672.0), (704.0, 712.0), (824.0, 836.0),
    (876.0, 884.0), (968.0, 984.0))]
RETONGUE_LEAD_ART_S.pop("Violoncellos", None)
# A #2 / C #6 (EW research batch 4: legato velocity follows the dynamic; floor 100 because the c02 targets at v60-100
# were 220-385 ms late): string and brass legato targets by the dynamic lane at the target, with the matching extra
# lead (strings 1.1 ms per velocity step from the LegatoSpeed table, brass about 0.4 ms); loud wind targets +8
LEG_VEL_STRONG = {"string": [(52, 100), (65, 106), (80, 112), (100, 118), (127, 124)],
                  "brass": [(52, 100), (65, 106), (80, 112), (100, 118), (127, 124)]}
LEG_VEL_EXTRA_S = dict(LEG_VEL_EXTRA_S, string=[(100, 0.027), (106, 0.020), (112, 0.013), (118, 0.007)],
                       brass=[(100, 0.010), (106, 0.007), (112, 0.005), (118, 0.002)])
LEG_VEL_DYN_ADD = {"wind": (DYN["ff"], 8)}
# A #2 (EW legato overlaps 45-80 ms strings, 33-58 ms winds / brass; ours 14 ms): overlap floors
LEG_OVERLAP_MIN_S = {"string": 0.045, "wind": 0.035, "brass": 0.035}
# A #3 (string staccato rows: f and ff shared a velocity layer, the top layer was never used; EW: CC parked high,
# dynamics by velocity): velocity by the printed level on each section's staccato row; the level step is refit on the
# render (ROW_GAIN_DB below is the inferred +1.9 dB of 95 -> 118 at ff, taken back as -1.5 dB on the whole row)
_str_stac_vel = [(58, 66), (72, 80), (88, 100), (114, 118), (124, 124)]
for _t, _r in (("Violins I", "Staccatissimo RRx9"), ("Violins II", "Stac RRx9"), ("Violas", "Stac RRx9"),
               ("Violoncellos", "Stac RRx9"), ("Double basses", "Staccato RRx9")):
    ROW_VEL_BY_CC[_t] = {_r: _str_stac_vel}
    ROW_GAIN_DB[_t] = dict(ROW_GAIN_DB.get(_t, {}), **{_r: -1.5})
# A #3: wind staccatos capped at v104 (already), trumpet staccato lead 0.02 s (pc +28..+33 ms with no lead; tools: brass
# family allowed)
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Trumpet 1": 0.02, "Trumpet 2": 0.02, "Trumpet 3": 0.02})
# A #4 / C #4 (S2, 0.6 x the measured residual): per-track entry leads
ENTRY_LEAD_S = _front(ENTRY_LEAD_S, **{"Oboe 2": (0.0, 0.11, 0.0), "Contrabassoon": (0.04, 0.04),
                                       "Horn 2": (0.04, 0.06, 0.03), "Trumpet 1": (0.10, 0.065),
                                       "Trombone 1": (0.06, 0.09, 0.05), "Trombone 2": (0.06, 0.09, 0.05),
                                       "Bassoon 2": (0.05, 0.05)})
# C #3 / A #4: Oboe 1 early by 8-16 ms: its articulation entry extras -0.01 s
ENTRY_LEAD_ART_S = _front(ENTRY_LEAD_ART_S, **{
    "Oboe 1": {k_: round(v_ - 0.01, 3) for k_, v_ in ENTRY_LEAD_ART_S["Oboe"].items()},
    # A #4: string slur heads on Leg Slur MAX late (Vc +50, Vln I +38, Vln II +26 ms): extra 0.06 -> 0.09 / 0.08 / 0.075
    "Violoncellos": dict(ENTRY_LEAD_ART_S["string"], **{"Leg Slur MAX": 0.09}),
    "Violins II": dict(ENTRY_LEAD_ART_S["string"], **{"Leg Slur MAX": 0.075}),
    "Violins I": dict(ENTRY_LEAD_ART_S["string"], **{"Leg Slur MAX": 0.08})})
# C #2 (S2): upper strings 40-85 ms late in the closing group F, the chorale P and the final Largamente T: Sus MAX leads
# on abutting notes (span form, capped at 0.45 of the note before), tremolo entries in T
for _t in ("Violins I", "Violins II", "Violas"):
    ROW_LEAD_S[_t] = dict(ROW_LEAD_S.get(_t, {}), **{"Sus MAX": [(888.0, 936.0, 0.07), (1088.0, 1116.0, 0.07)] + (
        [(328.0, 392.0, 0.11)] if _t != "Violins I" else [])})
TREM_ENTRY_LEAD_SPANS = {"Violins II": [(1088.0, 1116.0, 0.12)], "Violins I": [(1088.0, 1116.0, 0.10)]}
# PHRASE_SHAPE (cycles/c06 critic C #1-#2, A #2; EW research batches 2-4): -12 at the first onset, +3 / +8 by 0.4 / 0.8 s,
# +10 at 45 %, +4 1 s before the last note-off, -12 at it; scaled by the printed level; brass CC1 at most 108
PHRASE_SHAPE = {"families": ("string", "wind", "brass"), "min_s": 2.0, "gap_s": 0.25, "start": -12,
                "rise": [(0.4, 3), (0.8, 8)], "peak": (10, 0.45), "pre_end": (1.0, 4), "end": -12,
                "scale": {"ppp": 0.6, "pp": 0.8, "p": 1.0, "mp": 1.0, "mf": 1.0, "f": 0.6, "ff": 0.35, "fff": 0.2},
                "floor": 8, "cap": {"brass": 108}, "hp_fade_s": 0.25, "step_s": 0.1,
                "cc1_floor": 36,
                # coordinator 2026-11-08 (research batches 6-7, Balfe): shape by music type. Builds (the printed level
                # rises 10+ CC, or a crescendo ends in the phrase's last quarter) peak at 0.95; driving music (outside
                # the lyrical sections D-E, L-M, the Largamente O and Q) enters high (+6), peaks at 0.15 (+10) and
                # falls to -10; lyrical lines keep the centred arch
                "types": {"build_cc": 10, "drive": (6, (10, 0.15), -10), "drive_min_bpm": 0,
                          "lyric_spans": [(200.0, 328.0), (680.0, 792.0), (840.0, 888.0), (936.0, 984.0)]}}   # (CC1-layer tracks: no dip under CC1 36, the layer boundaries at 30-36, kit section 4)
# research batch 5 item 3: crescendos reach 70 % of their rise at 40 % of the hairpin; diminuendos keep 65 % of their
# level to their last onset and fall on that held note
HP_CURVE = {"cresc": (0.4, 0.7), "decresc_last": 0.35, "min_qn": 1.0}
# C #5 (research batch 5 item 5: tempo changes on about 20 % of beats, breaths): caesuras before the seven big entries
# after a general rest, and phrase arcs on the lyrical sections (no arc in the Allegro sections)
CAESURA = {72.0: 0.06, 104.0: 0.08, 392.0: 0.08, 632.0: 0.06, 664.0: 0.06, 816.0: 0.05, 1108.0: 0.10}
PHRASE_ARCS = [(200, 216, "sub"), (216, 232), (232, 248, "sub"), (248, 264, "main"), (264, 280, "sub"), (280, 296),
               (296, 312, "sub"), (312, 324, "open"),
               (680, 696, "sub"), (696, 712), (712, 728, "sub"), (728, 744, "main"), (744, 760, "sub"), (760, 776),
               (776, 784, "open"),
               (840, 856), (856, 872, "main"),
               (936, 952, "sub"), (952, 968, "main"), (968, 976, "open")]

# ---------- mvt3 c08 (2026-11-08; critics on the c07 render: cycles/c08/reports/A-C.md; research batches 6-7 carry-over) ----------
# critic A #1: the final fff chord fell 20 dB in 0.22 s (master; dry 0.15 s), trumpets / violas 57-62 dB down at +0.3 s
# (release caps, CUTOFF_EARLY_S, no hall send on the low brass). The last chord's wind / brass / string notes are held
# 0.45 s past the written end (1113.0) under a curved post-fader fall (-8 at 0.15 s, -16 at 0.3 s, -24 at 0.45 s); the
# returns follow the fall and keep their tails. Targets: -20 dB in 0.40-0.50 s, drop at +0.3 s 14-17 dB
FINAL_RING = {"at": 1112.0, "end": 1113.0, "ring_s": 0.45, "pts": [(0.15, -8.0), (0.30, -16.0), (0.45, -24.0)],
              "families": ("wind", "brass", "string")}
# critics A #2 + C #4 (research batch 7 item 2: 15-25 velocity steps strongest to weakest, about 3-5 dB on short rows),
# one table: velocity does not move the KS Master Sus MAX rows (Movement I c06), so the metre is a level step per onset.
# c07 measured on the Cb stem (first 120 ms of each eighth): 792-840 down - off +1.0 dB, 984-1056 +3.5, 1056-1088 -1.4
# (the bow-direction round robin puts the strong stroke on the off-beats). C's table on every span (3.5 dB down to off),
# the spans extended over the hammered 816-840 and to 1088 on the basses (bar 271); A's stronger off-beat cut on the
# basses' 1056-1088. No seeded jitter: the round robins already scatter 3-6 dB SD per position (c07)
METRIC_BOWED_DB = {"down": 2.0, "mid": 1.0, "beat": 0.0, "off": -1.5}
METRIC_BOWED = {"Violas": [(792.0, 840.0), (984.0, 1080.0)], "Violoncellos": [(792.0, 840.0), (984.0, 1080.0)],
                "Double basses": [(792.0, 840.0), (984.0, 1088.0)]}
METRIC_BOWED_DB_SPANS = {"Double basses": [(1056.0, 1088.0, {"down": 1.5, "mid": 1.0, "beat": 0.0, "off": -2.5})]}
# MANUAL-GAPS #6 trial (A #2 fallback): a round-robin reset on Opus's reset controller (CC16, Preferences.json) before the
# basses' 1056 eighths, so the bow-direction cycle restarts there
RR_RESET_AT = {"Double basses": [1056.0]}
# critic A #3: four held notes played as late stubs by the unison outlast rule (Oboe 2 844 / 856 under Oboe 1's slurred
# line, Horn 1 118, Horn 2 122: -22.8..-200 dB re their track medians): they play from their own onset, -6 dB until the
# kept note ends, then a 0.25 qn ramp to 0
UNI_OUTLAST_PLAY = {"min_delay_qn": 0.3, "db": -6.0, "ramp_qn": 0.25}
# critic A #5: the bar-236 portamento showed no glide (passing-pitch share max -10.4 / -8.9 dB): a slower slide (LegatoSpeed
# start offset smaller at a lower velocity, kit section 5), with 0.04 s more lead in leg_leads.json
PORT_TARGETS = {"Violins I": {941.0: 45}, "Violins II": {941.0: 45}}
# critic A #6 (S1): the celli's whole-note repeat 824 -> 828 (f, unslurred) dipped 1.5 dB: the detach span 824-836 takes
# repeats up to a whole note (it stopped at a half note)
STR_REP_DETACH["at"]["Violoncellos"] = [(a_, b_, dict(o_, max_qn=4.0) if a_ == 824.0 else o_)
                                        for a_, b_, o_ in STR_REP_DETACH["at"]["Violoncellos"]]
# critic C #3.1 (S3): bar 219's "sub. p" (qn 872): the held-decrescendo levels (-3 / -6 dB) were released at the subito,
# so twelve tracks stepped up and the master did not drop (-32.9 -> -33.2 dB; winds -49.6 -> -40.2): held through it and
# released across the crescendo 876-880
HELD_DECRESC_CARRY = {"max_qn": 8.0}
# critic C #3.3 (S3): the sfp at bar 149 (qn 592) peaked 0.18 s late and 1.9 dB under the ff before, the p only 5.4-6.0 dB
# under it: a longer, stronger sf (string sfp notes 0.06 s more lead in entry_leads.json)
SFP_SPIKE_S, SFP_VEL = (0.15, 0.35), 110
# (the Violins I / II and basses sfp notes at 592 are abutting re-attacks, which entry_leads.json does not reach: the same
# 0.06 s as a span row lead)
for _t in ("Violins I", "Violins II", "Double basses"):
    ROW_LEAD_S[_t] = dict(ROW_LEAD_S.get(_t, {}))
    ROW_LEAD_S[_t]["Sus MAX"] = sorted(ROW_LEAD_S[_t].get("Sus MAX", []) + [(591.9, 592.1, 0.06)])
# c08 stem fix (measured on the c08 render, Cb stem, first 120 ms of each eighth): the CC16 reset at 1056 flipped the
# bow-direction cycle (raw off-beat strokes now 3.3 dB under the beats), so A's table overshot: down - off +6.9, beat - off
# +5.3 dB at 1056-1088 (target +3..+4.5); 984-1056 +5.5 (C's target 2.5-3.5). Smaller steps on both spans
METRIC_BOWED_DB_SPANS = {"Double basses": [(984.0, 1056.0, {"down": 1.0, "mid": 0.5, "beat": 0.0, "off": -0.5}),
                                           (1056.0, 1088.0, {"down": 0.5, "mid": 0.5, "beat": 0.0, "off": -0.5})]}

# ---------- mvt3 c09 (2026-11-08; critics on the c08 render: cycles/c09/reports/A-C.md) ----------
# critics A #1 + B #4 (S3): the sfp at 592 and the fp at 832 started on the p layer: every led note's pull read the CC
# after the spike (23 of 24 tracks at CC 46 at the note-on), and the timpani's first CC7 point read p (28) under a +13 dB
# hairpin gain. The attack level now starts at the mark (tools FP_SPIKE_AT_MARK), so the pulls, the brass CC1 and the
# timpani CC7 / hairpin gain start from the sf. The spike is held 0.10 s and falls by 0.30 s after the score onset
# (with the c08 leads gone, about 0.15 / 0.35 s from the moved note-on, A's values)
FP_SPIKE_AT_MARK = True
SFP_SPIKE_S, SFP_VEL = (0.10, 0.30), 110
# A #1: the c08 string sfp leads (+0.06 s) are removed: with the attack on the loud layer they only made the sf early
for _t in ("Violins I", "Violins II", "Double basses"):
    ROW_LEAD_S[_t]["Sus MAX"] = [x_ for x_ in ROW_LEAD_S[_t]["Sus MAX"] if x_ != (591.9, 592.1, 0.06)]
# Movement I c51 (carry-over 2): timpani roll hairpins stay linear
HP_CURVE["skip_staves"] = ("Timp",)
# B #3 (S3): a driving phrase that enters on a subito-softer mark or a printed drop of 6 CC or more takes no positive
# offset ("drop": held at the printed level, then the drive's end fall); the strings entered about 11 CC over the sub. p
PHRASE_SHAPE["types"]["drop"] = {"cc": 6}
# A #3 (item 4): brass accent fronts 3-10 dB duller than unaccented notes (the swell peaked 70 ms after the attack of a
# led note): the swell starts at the moved note-on and peaks at 0.02 s
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass=dict(GENTLE_ACCENT["brass"], swell_s=(0.02, 0.18, 0.45)))
ACCENT_SWELL_FROM_MOVED = ("brass",)
# A #2 (S1): unslurred same-pitch string repeats whose next note's lead closed the gap (violas 820-832 2 ms, Vln I 884
# 10 ms): the EW string gap (90 ms, at most 30 % of the onset distance) before the moved note-on, at mp or louder
STR_REP_NEW_BOW["plain"] = {"gap_s": 0.09, "frac": 0.3, "min_cc": DYN["mp"]}
# A #4 (S2): the basses' hammered eighths lilt long-short (on-beat attacks 24-28 ms slower than off-beats) in 816-840 and
# 1088-1108, but not after c08's CC16 reset at 1056: a reset at every span start
RR_RESET_AT = {"Double basses": [792.0, 816.0, 984.0, 1056.0, 1088.0]}
# B #1: the ff harp chord at 524 played v126-127, the Nail Pick group (manual p.69), 10 dB over the orchestra
HARP_VEL_MAX = 123
# (not under "change bow at will" from bar 217 to the bar-222 run: the held p / mp chords re-bow there, A keeps them)
STR_REP_NEW_BOW["plain"]["skip"] = {t_: [(864.0, 884.0)] for t_ in ("Violins I", "Violins II", "Violoncellos", "Double basses")}
# A #1: the fp at 832 the same way: the f attack held 0.10 s, at p by 0.30 s (it lasted 41 / 86 ms in qn), velocity 96
# (it played v53, the p velocity; c02 measured v96 + 0.12 / 0.30 s within 1 dB of the ff before at the sfp)
FP_SPIKE_S, FP_VEL = (0.10, 0.30), 96
# c09 stem fix (measured on the c09 render, Cb stem, first 120 ms of each eighth, after the CC16 resets at every span
# start): 792-816 down - off +6.2 dB (target +2..+4) with the default table, 1088-1108 0.0 / beat - off +0.4 with no
# table at all (outside METRIC_BOWED). 816-840 +3.5, 984-1056 +3.5 and 1056-1088 +3.8 hold. A smaller table on 792-816
# and a table on 1088-1108
METRIC_BOWED["Double basses"] = [(792.0, 840.0), (984.0, 1108.0)]
METRIC_BOWED_DB_SPANS["Double basses"] = sorted(METRIC_BOWED_DB_SPANS["Double basses"] + [
    (792.0, 816.0, {"down": 0.0, "mid": 0.0, "beat": 0.0, "off": -0.5}),
    (1088.0, 1108.0, {"down": 1.5, "mid": 1.0, "beat": 0.5, "off": -1.5})], key=lambda r_: r_[0])

# ---------- mvt3 c10 (2026-11-09; critics on the c09 render: cycles/c10/reports/A-C.md) ----------
# critic A #1 (S1, S2): the basses' hammered eighths kept 0.03 qn (8-12 ms) gaps; in the master half of them dipped under
# 3 dB (medians 2.2-3.1 dB) and the off-beat ran into the downbeat (long-short lilt). Movement I c51's REP_SPLIT gap keys
# (ported in tools): a stroke into a same-pitch stroke ends max(0.06, min(0.08, 0.35 x slot)) s early at mp or louder
# (0.063 s at 168 qpm); the basses' detach dip -5 -> -3 dB on the coda / Piu allegro / Largamente spans, +0.5 dB on them
REP_SPLIT = dict(REP_SPLIT, gap_s=0.08, frac=0.35, gap_min_s=0.06, gap_min_cc=DYN["mp"])
STR_REP_DETACH["at"]["Double basses"] = [
    ((s_[0], s_[1], dict(s_[2] if len(s_) > 2 else {}, dip_db=-3.0)) if (s_[0], s_[1]) in ((792.0, 840.25), (984.0, 1108.25))
     else s_) for s_ in STR_REP_DETACH["at"]["Double basses"]]
LEVEL_SHAPES["Double basses"] = [[(q_, d_ + 0.5 if d_ else d_) for q_, d_ in sh_] if sh_[0][0] in (791.85, 983.85) else sh_
                                 for sh_ in LEVEL_SHAPES["Double basses"]]
# critic A #2 (S2; manual p.108, Flute 2 is another player): the slur-start joins carried one 0.12 s lead for every track
# (Flute 1 median -36 ms, Flute 2 +45 ms; a 160-260 ms flam on the ff F1 heads); per-track values (tools: dict form) and
# Flute 2's v100 joins +0.02 s (median +32 against Flute 1's +8)
SOST_JOIN_LEAD_S = {"Flute 1": 0.085, "Flute 2": 0.16, "default": 0.12}
LEG_VEL_EXTRA_S = dict(LEG_VEL_EXTRA_S, **{"Flute 2": [(60, 0.10), (80, 0.06), (100, 0.02)]})
# critic A #4 (manual p.109, MANUAL-GAPS #5, never tried): Bassoon 1's "solo, espress." (bars 115-125, pp strings only)
# on the BS KS Master's "Leg Slur Exp" row (key 77: slower attack, growing vibrato); one more row, one track
ART_SPANS["Bassoon 1"] = ART_SPANS.get("Bassoon 1", []) + [{"from": 455.9, "to": 496.0, "art": "Leg Slur Exp"}]
# critic C #3 (S3): the sf of the sfp at 592 is a late swell on the strings (first 0.1 s 3-7 dB under the ff before,
# peak +0.10..+0.30 s): the celli (unled) start 0.08 s early; a short post-fader bump on the strings' attack (the
# envelope sits before the returns since c06, so the hall gets it too). The winds and brass already lead 0.05-0.12 s
# and still peak 0.22-0.26 s late (the sample's rise, not the note-on), so no more leads there
ROW_LEAD_S["Violoncellos"] = dict(ROW_LEAD_S.get("Violoncellos", {}))
ROW_LEAD_S["Violoncellos"]["Sus MAX"] = sorted(ROW_LEAD_S["Violoncellos"].get("Sus MAX", []) + [(591.9, 592.1, 0.08)]) \
    if isinstance(ROW_LEAD_S["Violoncellos"].get("Sus MAX", []), list) else ROW_LEAD_S["Violoncellos"]["Sus MAX"]
for _t, _d in (("Violins I", 3.0), ("Violins II", 3.0), ("Violas", 3.0), ("Violoncellos", 5.0), ("Double basses", 5.0)):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(591.95, 0.0), (592.0, _d), (592.22, _d), (592.35, 0.0)]]
# critic B #1: the chorale motto's tied G4 (1016-1024) decays 3.2 dB in 2.7 s (the ff sample's own fall): a +2 dB shape
# (the c05 -3 dB row is deleted in roles.json)
LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES.get("Trumpet 1", []) + [[(1016.0, 0.0), (1023.5, 2.0), (1024.0, 0.0)]]
# critic C #2: Horns 1 and 3 fall 1.8 dB inside the printed crescendo of 275-276 (qn 1096-1104); held to the fff at 278
for _t in ("Horn 1", "Horn 3"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(1096.0, 0.0), (1104.0, 2.5), (1107.85, 2.5), (1108.0, 0.0)]]
# critic C #2: the 1088-1104 ride trim ended with a -2.5 dB step on the downbeat of 277, flattening the crescendo into
# 278 in the mp3 (master 275-278 -16.4 / -16.2 / -14.3 / -11.7, mp3 -14.1 / -14.0 / -14.1 / -11.2): a falling row held
# through the final chord (simulated on the c09 master: crescendo restored, 278 over 223, limiter 1.7 dB)
RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if r_[0][0] != 1087.0] + [
    [(1087.0, 0.0), (1088.0, 2.5), (1096.0, 2.0), (1104.0, 2.0), (1107.9, 1.5), (1108.0, 1.0), (1113.0, 1.0), (1113.5, 0.0)]]
# critic C #1 (delivery, refit on the c10 master): after a loud passage the ride's slow lift kept rising 6-10 s into the
# soft music (transition C fades in +7.7 dB where the master rises 2.8; the bassoon solo inverted). The 167-264 and
# 451-504 flat steps are replaced by deliver_master.py --fit-flat rows (fitted on cycles/c10/render/00_Master.wav),
# every value +1.5 dB (C's simulation on c09)
_FIT10 = {
    (164.0, 200.0): [3.48, 3.15, 2.83, 2.51, 2.21, 1.92, 1.64, 1.37, 1.12, 0.89, 0.67, 0.48, 0.29, 0.13, -0.02, -0.16,
                     -0.28, -0.39, -0.49],
    (200.0, 264.0): [0.39, 0.3, 0.23, 0.18, 0.13, 0.1, 0.07, 0.05, 0.04, 0.04, 0.04, 0.04, 0.05, 0.07, 0.09, 0.12, 0.17,
                     0.22, 0.28, 0.36, 0.44, 0.55, 0.66, 0.79, 0.95, 1.11, 1.28, 1.47, 1.66, 1.87, 2.08, 2.3, 2.53],
    (452.0, 504.0): [6.06, 4.63, 4.03, 3.62, 3.24, 2.87, 2.52, 2.19, 1.89, 1.61, 1.37, 1.16, 0.99, 0.86, 0.77, 0.71, 0.68,
                     0.7, 0.74, 0.82, 0.92, 1.05, 1.21, 1.38, 1.58, 1.78, 1.99]}
RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if r_[0][0] not in (167.0, 451.0)]
for (_a, _b), _v in _FIT10.items():
    _q = [_a + 2 * i for i in range(len(_v))]
    _q[-1] = _b - 0.1
    _off = [(1.5 if _a != 164.0 else min(1.5, max(0.0, (q_ - 164.0) / 8.0 * 1.5)) - (1.0 if q_ < 168.0 else 0.0))
            for q_ in _q] if _a == 164.0 else [1.5] * len(_q)
    RIDE_TRIMS.append([(_a - 0.05, 0.0)] + [(q_, round(v_ + o_, 2)) for q_, v_, o_ in zip(_q, _v, _off)] + [(_b, 0.0)])
# c10 stem fix (measured on the c10 render, Cb stem, first 120 ms of each eighth): with the REP_SPLIT gaps the strokes'
# position levels moved (new stroke layout, so the c09 "do not refit" note does not apply): 1088-1108 down - off +1.1
# (was +3.0), 984-1056 beat - off -0.1 (was +2.9); 792-840 and 1056-1088 hold (+2.6..+4.1)
METRIC_BOWED_DB_SPANS["Double basses"] = [
    (a_, b_, {"down": 2.5, "mid": 2.0, "beat": 1.0, "off": -2.5}) if a_ == 1088.0 else
    ((a_, b_, {"down": 1.0, "mid": 1.5, "beat": 1.5, "off": -0.5}) if a_ == 984.0 else (a_, b_, o_))
    for a_, b_, o_ in METRIC_BOWED_DB_SPANS["Double basses"]]

# ---------- mvt3 c11 (2026-11-09; critics on the c10 render: cycles/c11/reports/A-C.md) ----------
# critic A #1 (S1, S2; coordinator item 1): judged at the basses' fundamental (30-120 Hz), the on-beat repeats are the weak
# ones (1056-1088 stem 2.3 dB on-beat against 12.0 off-beat): the up-bow off-beat stroke swells through its note-off into
# the downbeat. A gap-only dip of -9 dB before every beat (tools: STR_REP_DETACH "beat_gap_db"), and the downbeat's metric
# step starts at the onset instead of 0.03 s early (tools: the same option). The -3 dB detach dip and the 63 ms gaps stay
STR_REP_DETACH["at"]["Double basses"] = [
    ((s_[0], s_[1], dict(s_[2], beat_gap_db=-9.0)) if (s_[0], s_[1]) in ((792.0, 840.25), (984.0, 1108.25)) else s_)
    for s_ in STR_REP_DETACH["at"]["Double basses"]]
# critic B #3 (coordinator item 2, S3): the winds' and brass' sf at the 592 sfp sits 2.9-4.5 dB under the ff before in its
# first 0.1 s (sample rise; leads do not move it, c10): the strings' c10 post-fader bump (+3 dB, 0.35 qn) on Horn 1,
# Trombone 1, Clarinet 1 and Bassoon 1; Horn 3 +4 (its front was 4.1 dB under; C #6's -2 dB trim ramps in over 0.6 s).
# Trumpets keep their ff (they do not play the sfp). Sus Accent MAX (A #2, C #1) deferred: REAPER settles at 45 GB
for _t, _d in (("Horn 1", 3.0), ("Horn 3", 4.0), ("Trombone 1", 3.0), ("Clarinet 1", 3.0), ("Bassoon 1", 3.0)):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(591.95, 0.0), (592.0, _d), (592.22, _d), (592.35, 0.0)]]
# critic A #4 (S1; coordinator item 5): tools now test the STR_REP_NEW_BOW "chord" rule before the generic string tenuto
# rule; a chord repeat that starts a new slur takes a longer gap than a louré repeat inside a slur (portato 0.09 s + fall)
STR_REP_NEW_BOW["chord"] = dict(STR_REP_NEW_BOW["chord"], head_gap_s=0.12)
# critic B #1 (coordinator item 6): bar 275's turn tune (Trumpets 1-2, Fl 1, Cl 1, Vln I) sat under the held horns
# (Horn 1 4-9.5 dB over Trumpet 1 on the eighths): Horns 1 / 3 start the new chord at -4 / -3 dB and rise to +2.5 by
# 1104 (each first point at the moved note-on); Trombone 2 -2 dB the same way. Trumpet 1's G4 eighths +3 (note_trims.json)
for _t, _sh in (("Horn 1", [(1095.78, -4.0), (1099.0, -4.0), (1104.0, 2.5), (1107.85, 2.5), (1108.0, 0.0)]),
                ("Horn 3", [(1095.88, -3.0), (1099.0, -3.0), (1104.0, 2.5), (1107.85, 2.5), (1108.0, 0.0)])):
    LEVEL_SHAPES[_t] = [sh_ for sh_ in LEVEL_SHAPES[_t] if sh_[0] != (1096.0, 0.0)] + [_sh]
LEVEL_SHAPES["Trombone 2"] = LEVEL_SHAPES.get("Trombone 2", []) + [[(1095.88, -2.0), (1099.0, -2.0), (1104.0, 0.0)]]
# critic C #5 (coordinator item 8, delivery): the 164-200 ride row lifted the mp3 1.5 dB exactly at the subito p of bar 42
# (mp3 f -> p 6.8 dB against the master's 9.2): the row is 0 to 166 and ramps to its fitted value (+1.5) by 176 (by 172
# the c11 mp3 put bar 43 1.2 dB over bar 42 where the master falls 2.6; re-delivered on the c11 master: 42 -> 43 -0.1)
for _i, _r in enumerate(RIDE_TRIMS):
    if _r[0][0] == 163.95:
        _v = dict((q_, v_) for q_, v_ in zip([164.0 + 2 * i for i in range(len(_FIT10[(164.0, 200.0)]))],
                                             _FIT10[(164.0, 200.0)]))
        _v[199.9] = _v.pop(200.0) if 200.0 in _v else _v.pop(max(_v))
        RIDE_TRIMS[_i] = [(163.95, 0.0)] + [(q_, round((v_ + 1.5) * min(1.0, max(0.0, (q_ - 166.0) / 10.0)), 2))
                                            for q_, v_ in sorted(_v.items())] + [(200.0, 0.0)]
# (A #4's labels were inverted: in the events the slurs run 840-842, 844-846, ..., so the 0.06 qn repeats A measured at
# 3.6 dB are the louré repeats inside each slur and the 0.09 s ones at 10.1 dB are the slur starts. Slur starts now
# 0.12 s, louré chord repeats 0.06 s: both clearer, the new bow still the clearer break)
STR_REP_NEW_BOW["chord"]["loure_gap_s"] = 0.06
# B #1: Trumpet 1's G4 eighths (1097, 1097.5) +3 dB as one shape from the first eighth's moved note-on (1096.88) to the
# next note's (1097.925); per-note trims left a 50 ms unlifted front on the second eighth
LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES.get("Trumpet 1", []) + [[(1096.86, 0.0), (1096.88, 3.0), (1097.9, 3.0), (1097.92, 0.0)]]

# ---------- mvt3 c12 (2026-11-09; critics on the c11 render: cycles/c12/reports/A-C.md) ----------
# critics A #2 / C #3 (coordinator item 3, S3): the sfp at 592 had a second hump at +0.25 s (the brass Sus samples keep
# rising while CC1 is held): a post-fader notch 0.11-0.40 s after the mark (LEVEL_SHAPES_S, seconds), and the c11 +3 dB
# front on the four tracks that did not have it. No "Sus Accent MAX" row (memory stays as c11)
for _t, _g in (("Bass trombone", -5.0), ("Trombone 2", -5.0), ("Horn 3", -4.0), ("Tuba", -4.0), ("Horn 1", -3.0),
               ("Trombone 1", -3.0)):
    LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(592.0, [(0.11, 0.0), (0.19, _g), (0.30, _g), (0.40, 0.0)])]
for _t in ("Bass trombone", "Trombone 2", "Tuba", "Trumpet 3"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(591.95, 0.0), (592.0, 3.0), (592.22, 3.0), (592.35, 0.0)]]
# critic A #3 (coordinator item 6): the muted solo's D4 and C4 sit 4.2-4.5 dB under the E flat 4 next to them on equal
# data (Mute Sus row): +3 dB from each D4's moved note-on to the note after the C4
LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES.get("Trumpet 1", []) + [
    [(683.88, 0.0), (683.92, 3.0), (685.86, 3.0), (685.92, 0.0)], [(715.88, 0.0), (715.92, 3.0), (717.86, 3.0), (717.92, 0.0)]]
# critic A #3 (coordinator item 6): slurred joins of the muted solo: the old note ends 0.03 s after the moved onset
ROW_SLUR_OVERLAP_S = {"Trumpet 1": {"Mute Sus": 0.03}}
# critic A #1 (S1; coordinator item 4): the cellos' same-pitch half-note repeats on Sus MAX dipped 1.4-3.4 dB with the
# -5 dB / 0.08 s detach dip (the Sus MAX release fills the gap): -10 dB over 0.10 s on the two spans A lists; the repeats
# at 630 and 658 follow a legato-row note at velocity 124 and started 7-10 dB under it: +4 dB on the repeat
STR_REP_DETACH["at"]["Violoncellos"] = [
    (a_, b_, dict(o_, dip_db=-10.0, dip_s=0.10) if (a_, b_) in ((64.0, 104.0), (596.0, 672.0)) else o_)
    for a_, b_, o_ in STR_REP_DETACH["at"]["Violoncellos"]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES.get("Violoncellos", []) + [
    [(629.72, 0.0), (629.76, 4.0), (630.6, 4.0), (631.0, 0.0)], [(657.72, 0.0), (657.76, 4.0), (658.6, 4.0), (659.0, 0.0)]]
# the repeats that kept 7-24 ms gaps: the cello sites lie inside STR_REP_DETACH spans (the "tenuto" and "plain" rules
# leave those to the dip; 325 is under the dip's min_cc), Violas 728 is under the "plain" min_cc (mp). Listed by score
# onset (tools: "plain" "force"). Not listed: Violas 426, 556, 564 (p repeats that STR_REP_NEW_BOW "soft" plays as re-bow
# pieces with their fills: the force rule does not cut re-bow pieces), Violoncellos 564 (a Stac RRx9 eighth before a
# legato slur start: the staccato sample ends by itself), Violins I 896 (Tremolo to Tremolo), Violins I 876 and
# Violins II 880 (held two-note p chords under the printed "change bow at will", c09 skip 864-884)
STR_REP_NEW_BOW["plain"]["force"] = {"Violoncellos": [325.0, 327.0, 832.0], "Violas": [728.0]}
# after the c12 render (level-only: tools/stem_fix.py on the stems, build_reaper.py --mix-only in REAPER): two forced gaps
# stayed filled by the release tail of the note before (item 4 dip 3.8 dB at Violoncellos 325, -4.4 dB at Violas 728,
# where a pp repeat at -67 dB follows a note at -62 dB). A notch inside the gap, in seconds before the note-on
# (LEVEL_SHAPES_S): -8 dB gives a dip of 10.1 dB at the celli; the violas need -16 dB for 7.1 dB (-12 dB gave 3.1 dB).
# The other ten sites of item 4 have 6 dB or more without a notch
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [(325.0, [(-0.085, 0.0), (-0.060, -8.0), (-0.015, -8.0), (0.0, 0.0)])]
LEVEL_SHAPES_S["Violas"] = LEVEL_SHAPES_S.get("Violas", []) + [(728.0, [(-0.070, 0.0), (-0.050, -16.0), (-0.015, -16.0), (0.0, 0.0)])]
# critic C #4 (coordinator item 7, delivery): the 164 ride row lifted the mp3 5 dB in 4.3 s after the subito p (bar 43 did
# not fall, bar 44 was 4.2 dB over bar 43 against the master's 2.4): C's dB offsets on the c11 row, so the total delivery
# gain rises about linearly from qn 164 to 196; the 680 row reaches its value at 696 instead of 680 (the printed p -> pp
# of bars 170-174 was delivered flat)
_C12_164 = {166.0: -0.4, 168.0: -1.5, 170.0: -2.2, 172.0: -2.75, 174.0: -3.2, 176.0: -3.1, 178.0: -2.8, 180.0: -2.5,
            182.0: -2.1, 184.0: -1.7, 186.0: -1.58, 188.0: -1.45, 190.0: -1.08, 192.0: -0.7, 194.0: -0.35}
for _i, _r in enumerate(RIDE_TRIMS):
    if _r[0][0] == 163.95:
        RIDE_TRIMS[_i] = [(q_, round(v_ + _C12_164.get(q_, 0.0), 2)) for q_, v_ in _r]
    elif _r[0][0] == 679.0:
        RIDE_TRIMS[_i] = [(679.0, 0.0), (680.0, 1.0), (696.0, 2.55), (743.0, 2.55), (744.0, 0.0)]
# critic A #4 (S2; coordinator item 9): the basses' on-beat eighths of 1088-1108 reached their level +89 ms after the beat
# (1056-1088: +10 ms; the gap before the beat is 73 ms here against 61 ms). A 0.03 s onset lead on every beat: the gap
# becomes 43 ms (A's second option gives 42 ms) and the c11 beat-gap dip stays (it ends at the moved onset); 0.06 s would
# leave a 13 ms gap and drop the dip. The led stroke keeps its note end (tools: ROW_LEAD_KEEP_END), so the 73 ms gap
# before the off-beat eighth does not grow to 103 ms
ROW_LEAD_S["Double basses"] = dict(ROW_LEAD_S.get("Double basses", {}))
ROW_LEAD_S["Double basses"]["Sus MAX"] = sorted(list(ROW_LEAD_S["Double basses"].get("Sus MAX", []))
                                                + [(q_ - 0.02, q_ + 0.02, 0.03) for q_ in range(1088, 1108)])
ROW_LEAD_KEEP_END = {"Double basses": {"Sus MAX": [(1087.98, 1108.0)]}}
# critic C #2 (coordinator item 8): the first chorale (bars 223-234, qn 888-936) ran at a constant 112 bpm with no phrase
# end: default arc on its first phrase (to the half cadence, bar 228) and "sub" on its second (bars 230-234, before the
# step to 132). Tempo only; the tables keyed in seconds were re-checked on these bars (cycles/c12/CHANGES.md)
PHRASE_ARCS = PHRASE_ARCS + [(888, 912), (916, 936, "sub")]

# ---------- mvt3 c13 (2026-11-09; critics on the c12 render: cycles/c13/reports/A-C.md) ----------
# item 1 (A #1, B #3): Bassoon 1's solo (bars 115-122, "Leg Slur Exp"): notes printed p spanned 11.6 dB (highest 100 ms
# level -53.1 at 475 to -41.5 at 480; the row's quarter notes end before its swell). A's four shapes per note; at 464 the
# A4 started in a 5-6 dB dip from -0.10 to +0.15 s (B's shape; the 150 ms lead and the +2 dB note trim stay)
LEVEL_SHAPES["Bassoon 1"] = LEVEL_SHAPES.get("Bassoon 1", []) + [
    [(458.9, 0.0), (459.0, 4.5), (460.9, 4.5), (461.0, 0.0)],
    [(461.9, 0.0), (462.0, -2.5), (462.9, -2.5), (463.0, 0.0)],
    [(471.9, 0.0), (472.0, -3.0), (474.9, -3.0), (475.0, 6.0), (475.9, 6.0), (476.0, 0.0)],
    [(478.9, 0.0), (479.0, 3.0), (479.9, 3.0), (480.0, -5.0), (481.9, -5.0), (482.0, -2.0), (483.9, -2.0), (484.0, 3.0),
     (485.0, 3.0), (486.0, 0.0)]]
LEVEL_SHAPES_S["Bassoon 1"] = LEVEL_SHAPES_S.get("Bassoon 1", []) + [
    (464.0, [(-0.14, 0.0), (-0.10, 5.0), (0.10, 5.0), (0.22, 2.0), (0.30, 0.0)])]
LEG_RAMP_OK = {"Bassoon 1": [464.0]}   # the 464 shape is fitted to the dip inside this join (A's 50 ms levels)
# item 2 (B #1): the fff timpani rolls of bars 223 and 278 fell 9-12 dB under their first stroke within 0.5 s (index
# -11 dB at 127 Hz, -7 dB at 160 Hz against the tutti). The body of each roll up; first strokes unchanged; both shapes
# are back at 0 dB before the next event (892, FINAL_RING)
LEVEL_SHAPES_S["Timpani"] = LEVEL_SHAPES_S.get("Timpani", []) + [
    (888.0, [(0.20, 0.0), (0.45, 5.0), (1.95, 5.0), (2.08, 0.0)]),
    (1108.0, [(0.30, 0.0), (0.50, 4.0), (1.95, 4.0), (2.09, 0.0)])]
# item 3 (B #2): Horn 1's p theme, bars 139-140: the first note (G4, "Sus MAX", CC1 42) -56.0 dBFS stem mean, under
# Horn 3/4, Violas and Clarinet 1; the staccato F4 at 556 -35.9 (louder than the printed f four bars later); the
# staccatos at 558 / 559 -39.5 / -40.3. Shapes in seconds (a note trim's 0.6 s ramps are longer than these eighths).
# 552: B's +10 dB simulated on the c12 stem gave -46.5 dBFS against -43.2 for the second note (target: first note not
# under the second), so +14 dB (+13.5 left it 0.1 dB under). With B's fall at 0.56-0.64 s the stem dipped 9 dB for
# 0.1 s before the slurred note (note-on at +0.644 s, at its level from +0.70 s; 50 ms windows -44.7 / -53.3 / -49.7 /
# -45.0), so the fall is at 0.63-0.72 s, under the rise of the next note
LEVEL_SHAPES_S["Horn 1"] = LEVEL_SHAPES_S.get("Horn 1", []) + [
    (552.0, [(-0.14, 0.0), (-0.12, 14.0), (0.63, 14.0), (0.72, 0.0)]),   # B: +10 to 0.56 / 0.64 s; see the note above
    (556.0, [(-0.03, 0.0), (-0.01, -8.0), (0.19, -8.0), (0.23, 0.0)]),
    (558.0, [(-0.03, 0.0), (-0.01, -4.5), (0.55, -4.5), (0.60, 0.0)])]
# item 4 (C #1 fix B, B #5): the stops at bars 2, 6 and 94: the celli's and basses' stems hold the tail (the tutti's
# time to -20 dB was 0.41-0.44 s on the master and up to 0.50 s on the mp3). A 6 dB release fade over 0.32 s after each
# stop, back at 0 dB before the next entry (celli 8.83 / 23.41 / 375.41, basses 15.83 / 31.66 / 375.83). 6 dB in 0.32 s
# is slower than the hall's own fall (13-18 dB in 0.3 s), so it is not a cut of the tail (BRIEF S3)
POST_SHAPES_S = dict(POST_SHAPES_S)
POST_SHAPES_S["Violoncellos"] = POST_SHAPES_S.get("Violoncellos", []) + [
    (5.0, [(0.08, 0.0), (0.40, -6.0), (1.20, -6.0), (1.32, 0.0)]),
    (21.0, [(0.08, 0.0), (0.40, -6.0), (0.72, -6.0), (0.81, 0.0)]),
    (374.0, [(0.03, 0.0), (0.35, -6.0), (0.42, -6.0), (0.47, 0.0)])]
POST_SHAPES_S["Double basses"] = POST_SHAPES_S.get("Double basses", []) + [
    (5.0, [(0.08, 0.0), (0.40, -6.0), (1.50, -6.0), (1.70, 0.0)]),
    (21.0, [(0.08, 0.0), (0.40, -6.0), (1.50, -6.0), (1.70, 0.0)]),
    (374.0, [(0.03, 0.0), (0.35, -6.0), (0.55, -6.0), (0.62, 0.0)])]
# item 5 (C): bars 255-256 (qn 1016-1024): the 31.5-125 Hz share fell to -23.0 / -20.9 dB between -14.7 (bar 254) and
# -17.1 (bar 257). Basses +2.5 dB over the two bars; the Bass trombone's -3 dB row starts at 1024 (roles.json)
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [
    [(1015.5, 0.0), (1016.0, 2.5), (1024.0, 2.5), (1024.5, 0.0)]]
# item 6 (A #4, C #4; MANUAL-GAPS #6): the crash at bar 263 (qn 1048) was 3.3 dB under the other two strokes (4-12 kHz
# -34.8 against -31.1 / -32.0 dB): the patch has three round-robin takes ("Long RRx1/2/3", read from "22in Zildjian K
# Crash.oib"), and the -3 dB role row at 1046-1060 is deleted (roles.json). A reset half a beat before each of the
# three strokes makes every stroke play the first take.
# item 9 (A): the same reset at the start of the pizzicato passage (bars 51-66) on its four tracks; the celli and basses
# start at 200.0, Violins II and Violas at 201.0 (their first note of the passage)
RR_RESET_AT = dict(RR_RESET_AT, **{"Crash cymbals": [887.5, 1047.5, 1107.5], "Violoncellos": [200.0],
                                   "Double basses": sorted(RR_RESET_AT["Double basses"] + [200.0]),
                                   "Violins II": [201.0], "Violas": [201.0]})
# item 7 (A #2): the muted Trumpet 1 solo (qn 680-744, "Mute Sus"): one 0.03 s overlap at every slurred join gave two
# pitches together for 97-144 ms where the new pitch speaks fast (683, 684, 686, 690, 715, 716, 718, 720, 724, 727, 728)
# and a late new pitch (+59..+85 ms at -6 dB) where it speaks slowly (687, 692, 694, 719, 723, 726). Per join: overlap
# 0.03 s at 685, 691, 717, 725; 0.02 s at 688, 723; 0.06 s with a 0.085 s lead at 687, 692, 694, 719, 726; 0.065 s lead
# at 723; elsewhere in the solo the note before ends at the moved onset (0.0) and the lead stays 0.035 s.
# The c12 +3 dB shapes at 684-686 and 716-718 are keyed on moved onsets with the 0.035 s lead, which stays there
ROW_SLUR_OVERLAP_S = {"Trumpet 1": {"Mute Sus": [
    (684.9, 685.1, 0.03), (686.9, 687.1, 0.06), (687.9, 688.1, 0.02), (690.9, 691.1, 0.03), (691.9, 692.1, 0.06),
    (693.9, 694.1, 0.06), (716.9, 717.1, 0.03), (718.9, 719.1, 0.06), (722.9, 723.1, 0.02), (724.9, 725.1, 0.03),
    (725.9, 726.1, 0.06), (680.0, 744.0, 0.0)]}}
ROW_LEAD_S["Trumpet 1"] = {"Mute Sus": [(q_ - 0.1, q_ + 0.1, 0.085) for q_ in (687, 692, 694, 719, 726)]
                           + [(722.9, 723.1, 0.065), (0.0, 1e9, 0.035)]}
# item 9 (A): Violins I "4 soli" at 485: the first eighth was 8-13 dB under the next ones (5 dB at 473). +4 dB from
# the moved onset (0.12 s before the beat) to 0.15 s after the beat
LEVEL_SHAPES_S["Violins I"] = LEVEL_SHAPES_S.get("Violins I", []) + [
    (485.0, [(-0.14, 0.0), (-0.12, 4.0), (0.12, 4.0), (0.18, 0.0)])]
# item 10 (A #3): the keyswitch of a row change without a rest goes 0.045 s before the note-on and not earlier than
# 5 ms after the previous note-on (was KS_LEAD = 0.06 qn: median 10-21 ms per track, minimum 7.1 ms). None = the old
# rule. cycles/c13/CHANGES.md has the range-render test this value had to pass
# c13 range-render test (cycles/c13/logs/kstest_compare.log): failed check (a), so the old 0.06 qn rule stays.
# The tested value was 0.045
KS_LEAD_S = None
# Violins II at 152 (ff, accent, slur start): a leap of 21 semitones down into "Leg Slur MAX" from an overlapping F6
# left a 0.4 s hole on the stem (-65 dB against -40). A fresh "Sus MAX" stroke 0.07 s early; the F6 before it ends
# 0.06 s before the new note-on (152 - 0.13 s = 151.636 qn at 168 bpm). DOWNBOW_STROKE_AT instead of A's ART_SPANS
# row: with ART_SPANS the note is no legato note, so the slur's next note (154) lost its join (unled first-note layer
# at 154.0, velocity 85; c12 had it joined at 153.57, velocity 124). The stroke keeps its end (ROW_LEAD_KEEP_END), so
# it overlaps the moved 154 target by the standard amount
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violins II": sorted(DOWNBOW_STROKE_AT.get("Violins II", []) + [152.0])})
ROW_LEAD_KEEP_END = dict(ROW_LEAD_KEEP_END, **{"Violins II": {"Sus MAX": [(151.9, 152.1)]}})
ROW_LEAD_S["Violins II"] = dict(ROW_LEAD_S.get("Violins II", {}))
ROW_LEAD_S["Violins II"]["Sus MAX"] = sorted(list(ROW_LEAD_S["Violins II"].get("Sus MAX", [])) + [(151.9, 152.1, 0.07)])
NOTE_END_AT = dict(NOTE_END_AT)
NOTE_END_AT["Violins II"] = dict(NOTE_END_AT.get("Violins II", {}))
NOTE_END_AT["Violins II"][151.5] = 151.636
# With 152 a "Sus MAX" stroke and no legato note, ROW_TRIM_DB's "Leg-row note within 3 qn" test no longer holds for
# the ff eighths at 148.5-150.0, which lost their -4 dB row trim (volume-envelope diff against c12: +4.0 dB over
# 148.31-150.36). This row gives it back; it sums with the trim that still starts at 150.30-150.36 to a flat -4 dB
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [
    [(148.302, 0.0), (148.362, -4.0), (150.302, -4.0), (150.362, 0.0)]]
# score change at bar 150 (the D pickup at 599.0 is removed in the low instruments): the celli's sfp chord at 592 is a
# ROW_LEAD_S stroke that kept its played length, so its note end was 0.08 s (0.224 qn) before 599.0, where the pickup
# used to follow. Before the new rest that end was 49 ms ahead of the other strings' (CUTOFF_EARLY_S: 598.886). The
# chord keeps its written end, so CUTOFF_EARLY_S sets the release with the family
ROW_LEAD_KEEP_END = dict(ROW_LEAD_KEEP_END, **{"Violoncellos": {"Sus MAX": [(591.9, 592.1)]}})

# ---------- mvt3 c14 (2026-11-10; critics on the c13 render: cycles/c14/reports/A-C.md; coordinator's rulings in the task) ----------
# item 1 (A #4, manual p.145 Round Robin Reset; c13's proposal): tools/build_reaper.py sends CC16 127 in the pre-roll of
# every track (PRE_RR_RESET). RR_RESET_ALL_AT (tools): the same reset before each section's first note on every pitched
# track except the harp, so a section's takes do not depend on the data before it and a range render that starts before
# a listed point plays what the full render plays. Points: the rehearsal letters and the pizzicato / solo passages
RR_RESET_ALL_AT = [40.0, 104.0, 168.0, 200.0, 264.0, 328.0, 392.0, 456.0, 536.0, 600.0, 680.0, 744.0, 792.0, 840.0, 888.0,
                   936.0, 984.0, 1056.0, 1088.0]
# item 2a (A #1 class A): a slurred string note that entered a legato row directly after a "Sus MAX" eighth got no
# transition and played the row's slow first-note layer (S +45..+144 ms at the theme's apex notes). Fresh "Sus MAX"
# strokes (the slur's next note joins from them), led by the short-note lead with the note end kept.
# item 2a (A #2): the cantabile entries of bars 67 and 187 (first notes on "Leg Slur MAX", body 0.35-0.40 s after the
# beat, S +200..+270 ms) as "Sus MAX" strokes too (Violins I / II 264 and 744, Violoncellos 264)
_C14_STROKES = {"Violins I": [50.0, 66.0, 82.0, 97.5, 134.0, 610.0, 264.0, 744.0],
                "Violins II": [50.0, 66.0, 82.0, 97.5, 310.0, 264.0, 744.0],
                "Violas": [76.0, 610.0, 642.0],
                "Violoncellos": [114.0, 130.0, 310.0, 264.0],
                "Double basses": [114.0, 130.0]}
_C14_ENTRY_STROKES = (264.0, 744.0)
for _t, _qs in _C14_STROKES.items():
    DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{_t: sorted(set(DOWNBOW_STROKE_AT.get(_t, [])) | set(_qs))})
    _j = [q_ for q_ in _qs if q_ not in _C14_ENTRY_STROKES]
    ROW_LEAD_S[_t] = dict(ROW_LEAD_S.get(_t, {}))
    ROW_LEAD_S[_t]["Sus MAX"] = sorted([(q_ - 0.1, q_ + 0.1, 0.06) for q_ in _j] + list(ROW_LEAD_S[_t].get("Sus MAX", [])))
    ROW_LEAD_KEEP_END = dict(ROW_LEAD_KEEP_END, **{_t: dict(ROW_LEAD_KEEP_END.get(_t, {}))})
    ROW_LEAD_KEEP_END[_t]["Sus MAX"] = sorted(list(ROW_LEAD_KEEP_END[_t].get("Sus MAX", [])) + [(q_ - 0.1, q_ + 0.1) for q_ in _j])
# item 2 (A #6, coordinator): unprinted tempo changes over 5 % of a beat. The seven caesuras stand before entries after
# a general rest and have no printed mark: halved to under 5 % (were +7.0..+12.0 %). Phrase arcs whose last beat has no
# printed breath mark: (248, 264) "main" (+9.4 %) and (760, 776) default (+6.4 %) become "sub" (+3.7 %). The arcs that
# end on a printed breath mark (232, 296, 712, 744, 856, 872, 912, 968) and the printed rit. / allargando ramps stay
CAESURA = {72.0: 0.03, 104.0: 0.035, 392.0: 0.035, 632.0: 0.03, 664.0: 0.03, 816.0: 0.025, 1108.0: 0.04}
PHRASE_ARCS = [((a_[0], a_[1], "sub") if (a_[0], a_[1]) in ((248, 264), (760, 776)) else a_) for a_ in PHRASE_ARCS]
# item 3 (C #1): a hole at the downbeat of bar 222 (master -17.6 -> -22.2 dBFS at +247 ms; the same in c09-c13).
# Violins I's unslurred B5 at 884 repeated a pitch of the chord before and played "Leg Slur MAX" from its first-note
# layer (-58 dBFS at +0.15 s): a new bow on "Sus MAX". Trumpet 1 and Horn 1 enter mf there and took 0.5 s to rise:
# +4 dB fronts. (The cellos' G2 swell before it: the pitch trim of C #5.)
ART_SPANS["Violins I"] = ART_SPANS.get("Violins I", []) + [{"from": 883.9, "to": 886.0, "art": "Sus MAX"}]
for _t in ("Trumpet 1", "Horn 1"):
    LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(884.0, [(-0.05, 0.0), (-0.03, 4.0), (0.30, 4.0), (0.55, 0.0)])]
# item 3 (C #2): the printed diminuendo of bars 39-41 (ff / f at 152 to the p of bar 42) came out as a 10 dB step at
# bar 42: "decresc_last" kept 65 % of the fall for the last onset, an eighth 0.22 s before the end. A diminuendo longer
# than 6 qn stays linear, and a last onset less than 0.35 s before the end is not used (tools). The earlier "bar 42
# subito" do-not-touch item is reopened for this curve only
HP_CURVE = dict(HP_CURVE, decresc_last_max_qn=6.0, decresc_last_min_s=0.35)
# item 3 (C #3): the stringendo of bars 245-246 sagged 2-4 dB before the Piu allegro. Violins I's printed "cresc. molto"
# stopped at the rest of 978 and the lone-swell rule returned it to mf (CC11 79-80 in the unison scale against Violins
# II's 107-112): a crescendo to the ff of 247. Horns 1-2 and Trumpets 1-2 hold a tied note under the phrase taper:
# +3 dB by 983.3, back at 0 before the led note of 984
SHARED_HP = dict(SHARED_HP, **{"Violins I": list(SHARED_HP.get("Violins I", [])) + [(978.0, 984.5, "cresc")]})
# (C's row ended at 983.85; the tied notes end at 982.89 and the led notes of 984 start at 983.58-983.65, Horn 2's
# quarter at 983.0, so the row is back at 0 dB by 982.95)
for _t in ("Horn 1", "Horn 2", "Trumpet 1", "Trumpet 2"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(978.5, 0.0), (982.6, 3.0), (982.9, 3.0), (982.95, 0.0)]]
# item 3 (C #6, manual p.63: CC11 fades to silence): the four "dal niente" clarinet entries started at their full pp
# level 0.1-0.2 s after the note-on: a fade-in after the fader, from -18 dB, at -6 dB by 0.8 s, full by 1.6 s
for _t, _q in (("Clarinet 2", 184.0), ("Clarinet 1", 200.0), ("Clarinet 2", 680.0), ("Bass clarinet", 680.0)):
    LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(_q, [(-0.085, 0.0), (-0.04, -18.0), (0.0, -18.0), (0.8, -6.0), (1.6, 0.0)])]   # note-ons 32-35 ms before the beat; Clarinet 2's note before 680 ends 124 ms before it
# item 4 (B #2): the first theme's head note (qn 40, f, accent) stood 6-10 dB over the rest of its phrase on Violins I,
# Violins II and Violas (Dan: an accent is 2-4 dB of weight): 2 dB off the swell that peaks 0.25-0.4 s after the onset;
# the first 50 ms of the attack stay
for _t in ("Violins I", "Violins II", "Violas"):
    LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(40.0, [(0.05, 0.0), (0.15, -2.0), (0.70, -2.0), (0.90, 0.0)])]
# item 4 (A #3): Trumpets 1-2 in the Piu allegro head (984-1000, f): the slurred notes on "Leg Slur MAX" at CC1 84-90
# were 10-13 dB under the first note and the tenuto A5 (the row falls off steeply under CC1 100). Level only (the printed
# f against the horns' ff stays): steps on the moved note-ons of 987.5, 991 and 992
LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES.get("Trumpet 1", []) + [
    [(987.16, 0.0), (987.20, 7.0), (988.93, 7.0), (988.97, 0.0)],
    [(990.61, 0.0), (990.65, 4.0), (991.66, 4.0), (991.70, 7.0), (999.85, 7.0), (999.95, 0.0)]]
LEVEL_SHAPES["Trumpet 2"] = LEVEL_SHAPES.get("Trumpet 2", []) + [
    [(987.16, 0.0), (987.20, 7.0), (988.93, 7.0), (988.97, 0.0)],
    [(990.61, 0.0), (990.65, 2.0), (991.66, 2.0), (991.70, 7.0), (999.85, 7.0), (999.95, 0.0)]]
# item 6 (A #5): muted Trumpet 1: at 684, 686, 716, 718 the "Mute Sus" release held the old pitch 82-96 ms into the new
# note: the note before ends 0.045 s before the moved note-on (tools: a negative ROW_SLUR_OVERLAP_S value is a gap); no
# extra lead
ROW_SLUR_OVERLAP_S["Trumpet 1"]["Mute Sus"] = [(q_ - 0.1, q_ + 0.1, -0.045) for q_ in (684, 686, 716, 718)] \
    + ROW_SLUR_OVERLAP_S["Trumpet 1"]["Mute Sus"]
# item 2a: Double basses 130 is not a stroke (the same-pitch note at 131 would start as an unled "Leg Slur MAX" note)
DOWNBOW_STROKE_AT["Double basses"] = [q_ for q_ in DOWNBOW_STROKE_AT["Double basses"] if q_ != 130.0]
ROW_LEAD_S["Double basses"]["Sus MAX"] = [x_ for x_ in ROW_LEAD_S["Double basses"]["Sus MAX"] if x_ != (129.9, 130.1, 0.06)]
ROW_LEAD_KEEP_END["Double basses"]["Sus MAX"] = [x_ for x_ in ROW_LEAD_KEEP_END["Double basses"]["Sus MAX"] if x_ != (129.9, 130.1)]
# item 2b (A #1, winds and brass: one lead per track and row, no per-onset rows): Horn 1's legato joins read +16..+20 ms
# (median of three lines, 29-40 of 59-61 notes outside 25 ms): +0.02 s on its "Leg Slur MAX" targets. Its "Sus MAX" notes
# joined from a legato note had no lead (+29..+70 ms at 52, 68 and in the recapitulation): 0.04 s on those four notes
# (a span over the whole theme also moved the accent swells of 84, 88, 100, which A did not measure late). Trumpet 1's loud legato targets (velocity over 118: coda 2 and the Piu allegro, medians +13..+18 ms) +0.02 s;
# its p solo (velocity 96, median -10 ms) is not touched. Horn 1's six early notes after "Marc Shrt": entry_leads.json
LEG_ART_EXTRA_S = dict(LEG_ART_EXTRA_S, **{"Horn 1": {"Leg Slur MAX": 0.02}})
ROW_LEAD_S["Horn 1"] = dict(ROW_LEAD_S.get("Horn 1", {}), **{"Sus MAX": [(q_ - 0.1, q_ + 0.1, 0.04) for q_ in (52, 68, 612, 628)]})
LEG_VEL_EXTRA_S = dict(LEG_VEL_EXTRA_S, **{"Trumpet 1": [(100, 0.010), (106, 0.007), (112, 0.005), (118, 0.002), (127, 0.02)]})
# item 4 (B #2): the theme's second note after the head: Violins II fall 5.7-9.5 dB from the head to it (bars 11, 19,
# 151), Violas 5.9 dB (bar 11). Lifts as level shapes that start with the short mirror ramp at the target's moved
# note-on (m - 0.05 .. m + 0.03 qn; Movement II c50: a 0.25 qn ramp on a legato target reads 60-100 ms late) and end
# before the next note-on. The moved note-ons are those of this build (leg_leads.json rows at 42, 74, 602): if a row
# there changes, move the first two points with it
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [
    [(41.4936, 0.0), (41.5736, 1.5), (43.25, 1.5), (43.33, 0.0)],
    [(73.6056, 0.0), (73.6856, 3.5), (75.25, 3.5), (75.33, 0.0)],
    [(601.446, 0.0), (601.526, 3.0), (603.25, 3.0), (603.33, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [[(41.4376, 0.0), (41.5176, 1.5), (43.25, 1.5), (43.33, 0.0)]]
LEG_RAMP_OK = dict(LEG_RAMP_OK, **{"Violins II": [42.0, 74.0, 602.0], "Violas": [42.0]})
ROW_LEAD_KEEP_END = dict(ROW_LEAD_KEEP_END, **{"Horn 1": {"Sus MAX": [(q_ - 0.1, q_ + 0.1) for q_ in (52, 68, 612, 628)]}})
# item 4 (B #1): per-pluck level trims for the pizzicato bass line (build/pluck_trims.json, fitted by
# cycles/c14/actor_scripts/pluckfit.py on range renders made after the resets); empty or missing file = none
import os as _os
_pt = f"{BUILD}/pluck_trims.json"
if _os.path.exists(_pt):
    for _t, _rows in json.load(open(_pt)).items():
        if not _t.startswith("_"):
            LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(float(q_), [tuple(p_) for p_ in pts_]) for q_, pts_ in _rows]
# coordinator (c14): the master fell 17.5 / 17.3 dB in 0.3 s at the stops of bars 6 and 94 (limit 17; all three critics:
# the mix is at the dry edge, do not dry any stop further). The c13 release fades of those two stops -6 -> -5 dB
for _t in ("Violoncellos", "Double basses"):
    POST_SHAPES_S[_t] = [(q_, [(x_, -5.0 if d_ == -6.0 else d_) for x_, d_ in pts_]) if q_ in (21.0, 374.0) else (q_, pts_)
                         for q_, pts_ in POST_SHAPES_S[_t]]
# item 2a: the strokes that stand inside a line take the "Sus MAX" row trim like the eighths before them (tools:
# ROW_TRIM_STROKES). Without it the stroke had no trim and the eighths before the strokes at 66 lost theirs (+4 dB on
# Violins II 64-65.5: their only Leg-row neighbour within 3 qn had been the note that is now a stroke)
ROW_TRIM_STROKES = {t_: [q_ for q_ in qs_ if q_ not in _C14_ENTRY_STROKES] for t_, qs_ in _C14_STROKES.items()}
# ----- after the range pre-check (two range renders of the build above, cycles/c14/logs/) -----
# the entries of bars 67 / 187 as "Sus MAX" strokes rose as slowly as the legato first note (Violins I at 264, 100 ms
# steps from the beat: c13 -51 -48 -43 -39 -37, stroke -55 -50 -43 -44 -39 dB; S +260 -> +206, +270 -> +164, +199 ->
# +167 ms): not strokes. They stay legato entries with the entry lead at its 0.30 s cap (entry_leads.json) and a front
# after the fader: +5 dB from the note-on to 0.12 s after the beat, gone by 0.40 s
for _t in ("Violins I", "Violins II", "Violoncellos"):
    DOWNBOW_STROKE_AT[_t] = [q_ for q_ in DOWNBOW_STROKE_AT[_t] if q_ not in _C14_ENTRY_STROKES]
    LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(q_, [(-0.33, 0.0), (-0.31, 5.0), (0.12, 5.0), (0.40, 0.0)])
                                                       for q_ in ((264.0, 744.0) if _t != "Violoncellos" else (264.0,))]
# the unslurred note after the stroke at 66 (Violins I / II 68, now "Sus MAX" on the beat) read +94 / +116 ms: 0.09 s lead.
# Strokes that still read late (Violins I 97.5 +56, 610 +42; Violas 76 +38, 642 +58; Violins II 310 +54 ms): 0.09 s
for _t, _qs in (("Violins I", (68.0, 97.5, 610.0)), ("Violins II", (68.0, 310.0)), ("Violas", (76.0, 642.0))):
    ROW_LEAD_S[_t]["Sus MAX"] = sorted([(q_ - 0.1, q_ + 0.1, 0.09) for q_ in _qs]
                                       + [x_ for x_ in ROW_LEAD_S[_t]["Sus MAX"] if not any(abs((x_[0] + x_[1]) / 2 - q_) < 0.01 for q_ in _qs)])
    ROW_LEAD_KEEP_END[_t]["Sus MAX"] = sorted(set(ROW_LEAD_KEEP_END[_t]["Sus MAX"]) | {(67.9, 68.1)})
# score change of 2026-11-10, bar 90: Flute 1, Oboe 1 and Clarinet 1 now land together on the accented F at 358. Range
# pre-check, S: Flute 1 +28, Oboe 1 +14, Clarinet 1 +40 ms: small row leads on the flute and the clarinet
ROW_LEAD_S["Flute 1"] = dict(ROW_LEAD_S.get("Flute 1", {}), **{"Sus MAX": [(357.9, 358.1, 0.015)]})
ROW_LEAD_S["Clarinet 1"] = dict(ROW_LEAD_S.get("Clarinet 1", {}), **{"Sus Non Vib": [(357.9, 358.1, 0.03)]})
ROW_LEAD_KEEP_END = dict(ROW_LEAD_KEEP_END, **{"Flute 1": {"Sus MAX": [(357.9, 358.1)]}, "Clarinet 1": {"Sus Non Vib": [(357.9, 358.1)]}})
# item 5 (B #4, C #4; delivery only, fitted on cycles/c14/render/00_Master.wav by cycles/c14/actor_scripts/ridefit.py): the
# ride gain rose through the static p-pp music after two diminuendos (bars 42-51 +5.6 dB, bars 171-176 +3.8 dB). The
# 163.95 and 679.0 rows are replaced: the gain now rises during the printed diminuendos (152-166, 664-678) and is held
# flat over 166-198 and 678-743 (C's layout). Measured: gain within 0.12 dB over bars 43-50 and 0.11 dB over 171-176
RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if r_[0][0] not in (163.95, 679.0)] + [
    [(151.95, 0.0), (152.0, 0.0), (156.0, 0.9), (160.0, 1.79), (164.0, 2.69), (166.0, 3.14), (168.0, 2.77), (170.0, 2.61), (172.0, 2.28), (174.0, 2.03), (176.0, 1.68), (178.0, 1.24), (180.0, 1.07), (182.0, 1.06), (184.0, 0.68), (186.0, 0.6), (188.0, 0.6), (190.0, 0.36), (192.0, 0.03), (194.0, -0.03), (196.0, -0.24), (198.0, -0.46), (199.9, 0.0)],
    [(663.95, 0.0), (664.0, 0.0), (668.0, 0.88), (672.0, 1.77), (676.0, 2.65), (678.0, 3.09), (680.0, 2.87), (682.0, 2.44), (684.0, 2.17), (686.0, 1.8), (688.0, 1.72), (690.0, 1.47), (692.0, 1.08), (694.0, 0.86), (696.0, 0.59), (698.0, 0.55), (700.0, 0.18), (702.0, 0.09), (704.0, 0.01), (706.0, 0.08), (708.0, 0.02), (710.0, -0.04), (712.0, 0.1), (714.0, 0.17), (716.0, 0.24), (718.0, 0.36), (720.0, 0.44), (722.0, 0.53), (724.0, 0.8), (726.0, 0.82), (728.0, 1.22), (730.0, 1.28), (732.0, 1.41), (734.0, 1.54), (736.0, 1.88), (738.0, 2.14), (740.0, 2.17), (742.0, 2.42), (743.9, 2.42), (744.0, 0.0)]]

# ---------- mvt3 c15 (2026-11-10; critics on the c14 render: cycles/c15/reports/A-C.md; coordinator's rulings in the task) ----------
# Priority: steady note timing in the fast themes (Dan heard Movement I's theme as choppy and out of time).
# item 1 (A #3, C #1, B #1): the first theme (bars 11-26, 151-170) on Violins I / II and Violas and F1 in the bass
# (bars 27-34) on Violoncellos and Double basses changed row on two joins in three; a legato-row note after a "Sus MAX"
# note took one of two start times between renders (38 %). One row: every note that is not a printed staccato plays
# "Sus MAX" (tools: STEADY_LINE, ported from Movement I c54; "Sus MAX" and not "Sus Marc LITE": it is loaded, and its
# long notes hold their level), the staccato quarters keep their short rows. One lead per class and track; slurred
# notes end "overlap_s" after the next note-on, a new bow "gap_s" before it. The accented halves lead 0.09 s.
import os as _os15
_C15_STEADY = _os15.environ.get("C15_STEADY", "1") == "1"
_C15_LV = json.load(open(f"{BUILD}/steady_levels.json")) if _os15.path.exists(f"{BUILD}/steady_levels.json") else {}
_C15_LEADS = json.load(open(f"{BUILD}/steady_leads.json")) if _os15.path.exists(f"{BUILD}/steady_leads.json") else {}
# start values per track (c14, S: "Sus MAX" joins with a 0.06 s lead read Violins I -12 ms at CC11 100+ and -1 at
# 80-99, Violins II +6 / +10, Violas -9 / -13; with no lead Violoncellos +27..+34, basses +21); refit on the range
# renders into build/steady_leads.json {track: {"from-to": {class: s}}} (classes: slur, tongue, first, rep)
_C15_BASE = {"Violins I": 0.06, "Violins II": 0.07, "Violas": 0.06, "Violoncellos": 0.04, "Double basses": 0.03}
# start levels per row (B #1's row trims; ROW_TRIM_DB is skipped inside the spans: with no legato row left its
# "Leg-row neighbour" test would trim only the notes near a span's edge); per-note steps fitted on the range renders
# (cycles/c15/actor_scripts/fit15.py) are in build/steady_levels.json
_C15_LVDEF = {"Violins I": {"Sus MAX": 0.0, "Staccatissimo RRx9": -6.0}, "Violins II": {"Sus MAX": -2.5, "Stac RRx9": -3.0},
              "Violas": {"Sus MAX": -3.0, "Stac RRx9": -4.0}, "Violoncellos": {"Sus MAX": -1.5, "Stac RRx9": -4.0},
              "Double basses": {"Sus MAX": 0.0, "Staccato RRx9": 0.0}}
# A #1a / C #2: Violins I's theme in octaves (632-664, no lead before: +72..+122 ms on the long notes) 0.08 s; A #1b:
# the violas' leggiero eighths of bars 19-26 (+17..+112 ms at 0.06 s, heads +60..+68 with none) 0.09 s
_C15_BASE_SPAN = {("Violins I", 632.0): 0.08, ("Violas", 72.0): 0.09}
_C15_SPANS = {"Violins I": [(40.0, 72.0), (72.0, 104.0), (600.0, 632.0), (632.0, 664.0), (664.0, 680.0)],
              "Violins II": [(40.0, 72.0), (72.0, 104.0), (600.0, 632.0), (632.0, 664.0), (664.0, 680.0)],
              "Violas": [(40.0, 72.0), (72.0, 104.0), (600.0, 632.0), (632.0, 664.0), (664.0, 680.0)],
              "Violoncellos": [(104.0, 136.0)], "Double basses": [(104.0, 136.0)]}
# mvt3 c24 (critic A c24 #1, ruling 5): the celli's unslurred half-note bass line of bars 11-26 and 151-166 played on
# "Leg BC MAX" and swelled late in every note (back +3.4..+9.2 dB over the front, five 200 ms holes of 6 dB or more; the
# basses on "Sus MAX" stayed flat): the celli join the one-row spans (to 664: the slurs of 668-676 stay on the legato
# rows). C24_VC=det plays these spans (all but 104-136) on "Detache" (key 30), as in range T1; C24_VC=off leaves them out
_C24_VC = _os15.environ.get("C24_VC", "det")   # c25 ruling 3: "det" (both statements on Detache, v91; see the c25 block)
if _C24_VC != "off":
    _C15_SPANS["Violoncellos"] = [(40.0, 72.0), (72.0, 104.0), (104.0, 136.0), (600.0, 632.0), (632.0, 664.0)]
# the accented halves and dotted halves of the theme (A): 0.09 s lead (and a +3 dB front, below)
_C15_ACC = {t_: [40.0, 52.0, 56.0, 68.0, 72.0, 84.0, 88.0, 100.0, 600.0, 612.0, 616.0, 628.0, 632.0, 644.0, 648.0, 660.0]
            for t_ in ("Violins I", "Violins II", "Violas")}
_C15_ACC.update({t_: [104.0, 116.0, 120.0, 132.0] for t_ in ("Violoncellos", "Double basses")})
if _C15_STEADY:
    for _t, _sps in _C15_SPANS.items():
        STEADY_LINE[_t] = []
        for _a, _b in _sps:
            _b0 = _C15_BASE_SPAN.get((_t, _a), _C15_BASE[_t])
            _ld = dict({"slur": _b0, "tongue": _b0, "first": _b0, "rep": _b0, "acc": 0.09},
                       **_C15_LEADS.get(_t, {}).get(f"{_a:g}-{_b:g}", {}))
            STEADY_LINE[_t].append({
                "from": _a, "to": _b, "art": ("Detache" if (_C24_VC == "det" and _t == "Violoncellos" and _a != 104.0) else "Sus MAX"),  # c24: det = every celli span but 104-136 (range T1)
                "lead_s": _ld["slur"], "tongue_lead_s": _ld["tongue"],
                "first_lead_s": _ld["first"], "rep_lead_s": _ld["rep"], "overlap_s": 0.02, "gap_s": 0.03, "rep_gap_s": 0.05,
                "poly": True, "level_all": True, "level_db": _C15_LV.get(_t, {}), "level_default": _C15_LVDEF[_t],
                "at": {q_: {"lead_s": _ld["acc"]} for q_ in _C15_ACC[_t] if _a <= q_ < _b}})
            # A: the accented halves swell in on "Sus MAX" (first 80 ms 4.5-7 dB under the body): a +3 dB front from the
            # moved note-on, gone by 0.30 s (the form of the c10 sf bump); the head notes 40 and 600 only +1
            LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [
                (q_, [(-_ld["acc"], 0.0), (-_ld["acc"] + 0.02, 1.0 if q_ in (40.0, 600.0) else 3.0),
                      (0.12, 1.0 if q_ in (40.0, 600.0) else 3.0), (0.30, 0.0)])
                for q_ in _C15_ACC[_t] if _a <= q_ < _b]
    # the c14 strokes, their leads and row-trim marks inside the spans have no target left
    def _in15(t_, q_):
        return any(a_ - 0.2 <= q_ < b_ for a_, b_ in _C15_SPANS.get(t_, []))
    for _t in _C15_SPANS:
        DOWNBOW_STROKE_AT[_t] = [q_ for q_ in DOWNBOW_STROKE_AT.get(_t, []) if not _in15(_t, q_)]
        ROW_TRIM_STROKES[_t] = [q_ for q_ in ROW_TRIM_STROKES.get(_t, []) if not _in15(_t, q_)]
        if isinstance(ROW_LEAD_S.get(_t, {}).get("Sus MAX"), list):
            ROW_LEAD_S[_t]["Sus MAX"] = [x_ for x_ in ROW_LEAD_S[_t]["Sus MAX"]
                                         if not (x_[1] - x_[0] < 1.0 and _in15(_t, (x_[0] + x_[1]) / 2))]
        if _t in ROW_LEAD_KEEP_END and "Sus MAX" in ROW_LEAD_KEEP_END[_t]:
            ROW_LEAD_KEEP_END[_t]["Sus MAX"] = [x_ for x_ in ROW_LEAD_KEEP_END[_t]["Sus MAX"]
                                                if not (x_[1] - x_[0] < 1.0 and _in15(_t, (x_[0] + x_[1]) / 2))]
        ROW_TRIM_SKIP[_t] = list(ROW_TRIM_SKIP.get(_t, [])) + [(a_ - 0.3, b_) for a_, b_ in _C15_SPANS[_t]]
    # c14's head shape at 40 and second-note lifts (42, 74, 602) were fitted on the legato rows: removed
    for _t in ("Violins I", "Violins II", "Violas"):
        LEVEL_SHAPES_S[_t] = [x_ for x_ in LEVEL_SHAPES_S.get(_t, []) if not (x_[0] == 40.0 and x_[1][1] == (0.15, -2.0))]
    LEVEL_SHAPES["Violins II"] = [sh_ for sh_ in LEVEL_SHAPES["Violins II"] if sh_[0][0] not in (41.4936, 73.6056, 601.446)]
    LEVEL_SHAPES["Violas"] = [sh_ for sh_ in LEVEL_SHAPES["Violas"] if sh_[0][0] != 41.4376]
    LEG_RAMP_OK = {k_: v_ for k_, v_ in LEG_RAMP_OK.items() if k_ not in ("Violins II", "Violas")}

    # item 2 (A #1c): Violins I's countersubject, bars 27-34 (all "Sus MAX" already): heads +18 ms with no lead, second
    # and fourth eighths +10 / +20 at 0.06 s, third eighths -34 ms (median of 14). One span, class leads, the third
    # eighths (odd quarters) 0.03 s. No level steps here (ROW_TRIM_DB stays in force)
    STEADY_LINE["Violins I"].append({
        "from": 104.0, "to": 136.0, "art": "Sus MAX", "lead_s": _C15_LEADS.get("Violins I", {}).get("104-136", {}).get("slur", 0.07),
        "tongue_lead_s": _C15_LEADS.get("Violins I", {}).get("104-136", {}).get("tongue", 0.02),
        "first_lead_s": _C15_LEADS.get("Violins I", {}).get("104-136", {}).get("first", 0.02),
        "overlap_s": 0.011, "gap_s": 0.004, "rep_gap_s": 0.05, "poly": True,
        "at": {float(q_): {"lead_s": _C15_LEADS.get("Violins I", {}).get("104-136", {}).get("third", 0.03)} for q_ in range(105, 135, 2)}})
# item 2 (A #1d): the low strings' staccato quarters in 104-136 read +28..+95 ms (Violoncellos 0.025 s lead, basses none)
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Double basses": 0.04})
ROW_LEAD_S["Violoncellos"]["Stac RRx9"] = [(104.0, 136.0, 0.05)]
# item 2 (C #2.1): the 0.11 s "Sus MAX" span lead of the closing group (328-392) read -53 (Violas) / -39 ms (Violins II)
for _t in ("Violins II", "Violas"):
    ROW_LEAD_S[_t]["Sus MAX"] = [((a_, b_, 0.06) if (a_, b_, s_) == (328.0, 392.0, 0.11) else (a_, b_, s_)) for a_, b_, s_ in ROW_LEAD_S[_t]["Sus MAX"]]
# item 2 (C #2.3): Violins I 970-976 (div., "Sus MAX", no lead) read +96..+156 ms: 0.10 s, the note end kept
ROW_LEAD_S["Violins I"]["Sus MAX"] = sorted([(969.5, 976.5, 0.10)] + list(ROW_LEAD_S["Violins I"]["Sus MAX"]))
ROW_LEAD_KEEP_END["Violins I"]["Sus MAX"] = sorted(list(ROW_LEAD_KEEP_END["Violins I"]["Sus MAX"]) + [(969.5, 976.5)])
# item 3 (A #4, C #1): the second theme keeps its legato rows; the slurred eighths of the Poco meno mosso (0.208 s) stay
# on the legato row on Violins II and Violoncellos as they do on Violins I (tools: SHORT_SUS_LEG_SPANS), so Violins II's
# F at 300 is no longer a "Sus MAX" > "Leg BC MAX" join; the c14 strokes at 310 go with them. leg_leads.json /
# entry_leads.json carry A's corrections. B: the +5 dB front at 264 ends earlier (it bulged 4 dB at 0.2-0.4 s); no
# front on Violins I at 744 (there the note speaks 148 ms early with it)
SHORT_SUS_LEG_SPANS = {"Violins II": [(264.0, 328.0)], "Violoncellos": [(264.0, 328.0)]}
for _t in ("Violins II", "Violoncellos"):
    DOWNBOW_STROKE_AT[_t] = [q_ for q_ in DOWNBOW_STROKE_AT[_t] if q_ != 310.0]
    ROW_TRIM_STROKES[_t] = [q_ for q_ in ROW_TRIM_STROKES.get(_t, []) if q_ != 310.0]
    ROW_LEAD_S[_t]["Sus MAX"] = [x_ for x_ in ROW_LEAD_S[_t]["Sus MAX"] if not (abs((x_[0] + x_[1]) / 2 - 310.0) < 0.01 and x_[1] - x_[0] < 1.0)]
    ROW_LEAD_KEEP_END[_t]["Sus MAX"] = [x_ for x_ in ROW_LEAD_KEEP_END[_t]["Sus MAX"] if not abs((x_[0] + x_[1]) / 2 - 310.0) < 0.01]
for _t in ("Violins I", "Violins II", "Violoncellos"):
    LEVEL_SHAPES_S[_t] = [((q_, [(-0.33, 0.0), (-0.31, 5.0), (0.02, 5.0), (0.20, 0.0)]) if q_ == 264.0 and pts_[1] == (-0.31, 5.0) and _t != "Violoncellos" else (q_, pts_))
                          for q_, pts_ in LEVEL_SHAPES_S[_t] if not (_t == "Violins I" and q_ == 744.0 and pts_[1] == (-0.31, 5.0))]
# item 4 (C #4): the basses' eighths limped in 1056-1108: on-beat strokes -32 ms with c12's 0.03 s lead (1088-1108),
# off-beat strokes +22..+36 ms with none. The on-beat rows are deleted; off-beat eighths lead 0.03 s (1088-1108) and
# 0.035 s (1056-1088), note ends kept
# Range test R1 (cycles/c15/logs/chk15_R1.log, envelope half-rise): with these leads the off-beat strokes read +50 / +68 ms
# (c14: +54 / +39) and the on-beat strokes +4 / +1 (c14: +10 / -30): the off-beat rise did not follow its note-on, so
# the block is off (C15_CBLEADS=1 builds it) and the c14 leads stay; open for c16
if _os15.environ.get("C15_CBLEADS", "0") == "1":
    ROW_LEAD_S["Double basses"]["Sus MAX"] = sorted(
        [x_ for x_ in ROW_LEAD_S["Double basses"]["Sus MAX"] if not (1087.9 < x_[0] < 1108.0 and x_[2] == 0.03)]
        + [(q_ + 0.48, q_ + 0.52, 0.03) for q_ in range(1088, 1108)] + [(q_ + 0.48, q_ + 0.52, 0.035) for q_ in range(1056, 1088)])
    ROW_LEAD_KEEP_END["Double basses"]["Sus MAX"] = sorted([x_ for x_ in ROW_LEAD_KEEP_END["Double basses"]["Sus MAX"] if x_ != (1087.98, 1108.0)]
                                                           + [(1055.98, 1108.0)])
    ROW_LEAD_KEEP_GAP = {"Double basses": {"Sus MAX": [(1055.98, 1108.0)]}}   # (S1: the 60-73 ms gaps before the off-beat strokes stay)
# item 5 (C #5, A #2): winds and brass, one lead per track / row and a pitch-pair table.
# Clarinet 1 "Leg Slur" joins +23 ms (n 40, robust SD 10); Oboe 1's re-tongued "Sus MAX" notes with the 0.07 s lead
# -45..-50 ms (n 14, three sections): 0.03 s in those sections (tools: RETONGUE_LEAD_SPANS); Oboe 1 and Horn 1 pairs (the falling semitone F4-E4 carried the source
# extra LEG_EXTRA_S 0.15 s of Horn 1's F4 and read -128 / -152 ms)
LEG_ART_EXTRA_S = dict(LEG_ART_EXTRA_S, **{"Clarinet 1": {"Leg Slur": 0.02}})
RETONGUE_LEAD_SPANS = {"Oboe 1": [(536.0, 600.0, 0.03), (792.0, 816.0, 0.03), (1088.0, 1108.0, 0.03)]}   # (bars 1-10 read +48 ms with the same lead: left)
LEG_PAIR_EXTRA_S = dict(LEG_PAIR_EXTRA_S,
                        **{"Oboe 1": {**LEG_PAIR_EXTRA_S["Oboe 1"], (79, 77): 0.06, (77, 76): 0.035, (74, 72): 0.065},
                           "Horn 1": {**LEG_PAIR_EXTRA_S["Horn 1"], (59, 62): 0.05, (50, 53): -0.06, (65, 64): -0.13}})
# Horn 1's stopped note at 668 ("Stop Sus", no lead) read +189 ms
ROW_LEAD_S["Horn 1"] = dict(ROW_LEAD_S["Horn 1"], **{"Stop Sus": [(667.9, 668.1, 0.12)]})
# A #2 range test: brass legato targets at velocity 116 and over were unsteady on Horn 1 and Trumpet 1 (same-row joins,
# robust SD 45 / 50 ms against 19 / 16 under 116): capped at 112 on these two tracks. C15_BRASSCAP=0 builds without it
# Range test R1 (cycles/c15/logs/captest_R1.log): Horn 1 bars 11-26 robust SD 69 -> 48 ms (one note -2.7 dB), bars
# 151-170 33 -> 23 ms, Trumpet 1 coda 2 31 -> 39 ms: the conditions (under 25 ms, no note down more than 2 dB) are met
# on one of three lines, so the cap is off (default "0") and the family ladder stays
if _os15.environ.get("C15_BRASSCAP", "0") == "1":
    for _t in ("Horn 1", "Trumpet 1"):
        LEG_VEL_STRONG = _front(LEG_VEL_STRONG, **{_t: [(52, 100), (65, 106), (127, 112)]})
    LEG_VEL_EXTRA_S = dict(LEG_VEL_EXTRA_S, **{"Trumpet 1": [(100, 0.010), (106, 0.007), (112, 0.005), (118, 0.002)]})
# B #1a: Horn 1's "Marc Shrt RRx4" eighths in the f theme (40-104) 4.3 dB over its legato notes: 15 velocity steps lower
ART_SPANS["Horn 1"] = [dict(sp_, vel_by_cc=[(60, 58), (90, 73), (110, 84), (124, 88)]) if (sp_["from"], sp_.get("art")) == (40.0, "Marc Shrt RRx4") else sp_
                       for sp_ in ART_SPANS["Horn 1"]]
# B #1b: head notes 7-8.5 dB over their second notes: Violoncellos 1064 -3, Clarinet 2 1056 -4 (the cello head at 120 is
# inside the one-row span and fitted there)
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [(1064.0, [(0.05, 0.0), (0.15, -3.0), (0.80, -3.0), (1.00, 0.0)])]
LEVEL_SHAPES_S["Clarinet 2"] = LEVEL_SHAPES_S.get("Clarinet 2", []) + [(1056.0, [(0.05, 0.0), (0.15, -4.0), (0.80, -4.0), (1.00, 0.0)])]
# item 6 (B #2): the downbeats of bars 222 and 245 (qn 884, 976): every string part changes bow together and the stems
# drop 6-16 dB for 0.2-0.3 s under a printed crescendo, after the celli's G2 has been the loudest stem. Celli: a
# counter-shape on the two G2 whole notes and a +4 dB front on the next note; violins: the new bow 0.08 s early (0.10 s
# on Violins I at 976, C #2.3) with a +3 dB front. Violins I stay on "Sus MAX" through the run to 888 (A: the run
# dropped 7 dB on the legato row)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(881.0, 0.0), (883.0, -4.0), (883.70, -5.0), (883.72, 0.0)], [(973.0, 0.0), (975.0, -3.0), (975.66, -4.0), (975.68, 0.0)]]
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S["Violoncellos"] + [
    (q_, [(-0.02, 0.0), (0.0, 6.0 if q_ == 884.0 else 4.0), (0.25, 6.0 if q_ == 884.0 else 4.0), (0.45, 0.0)]) for q_ in (884.0, 976.0)]   # (R1: master step at 884 -1.5 dB with +4: +6)
for _t in ("Violins I", "Violins II"):
    ROW_LEAD_S[_t]["Sus MAX"] = sorted([(883.9, 884.1, 0.08)] + ([(975.9, 976.1, 0.08)] if _t == "Violins II" else [])
                                       + list(ROW_LEAD_S[_t]["Sus MAX"]))
    ROW_LEAD_KEEP_END[_t]["Sus MAX"] = sorted(list(ROW_LEAD_KEEP_END[_t]["Sus MAX"]) + [(883.9, 884.1), (975.9, 976.1)])
    LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [
        (884.0, [(-0.08, 0.0), (-0.06, 5.0), (0.20, 5.0), (0.40, 0.0)]),   # (R1: +3 left the stems 6-9 dB down: +5)
        (976.0, [(-0.10 if _t == "Violins I" else -0.08, 0.0), (-0.08 if _t == "Violins I" else -0.06, 3.0), (0.20, 3.0), (0.40, 0.0)])]
ART_SPANS["Violins I"] = [dict(sp_, to=888.0) if (sp_["from"], sp_["to"]) == (883.9, 886.0) else sp_ for sp_ in ART_SPANS["Violins I"]]
ROW_LEAD_S["Violins I"]["Sus MAX"] = sorted([(886.9, 887.6, 0.03)] + list(ROW_LEAD_S["Violins I"]["Sus MAX"]))   # the run's slurred eighths (ff: +19 ms with no lead)
ROW_LEAD_KEEP_END["Violins I"]["Sus MAX"] = sorted(list(ROW_LEAD_KEEP_END["Violins I"]["Sus MAX"]) + [(886.9, 887.6)])
ROW_SLUR_OVERLAP_S["Violins I"] = {"Sus MAX": [(886.9, 887.6, 0.011)]}
# item 6 (B #6): bar 42 (qn 164-168): the printed p landed at the level of the pp that follows (strings 0-3 dB over
# their pp): +2 dB on the strings from the p onset, ramped out into the pp. HP_CURVE and the ride rows stay
for _t in ("Violins I", "Violins II", "Violas", "Violoncellos", "Double basses"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(163.9, 0.0), (164.1, 2.0), (167.0, 2.0), (168.0, 0.0)]]
# coordinator: the master fell 17.7 / 17.9 dB in 0.3 s at the stops of bars 2 and 6 (limit 17): the release fades
# after those two stops -6 / -5 -> -4 dB (bar 94's stays -5)
for _t in ("Violoncellos", "Double basses"):
    POST_SHAPES_S[_t] = [(q_, [(x_, -4.0 if d_ < -3.9 else d_) for x_, d_ in pts_]) if q_ in (5.0, 21.0) else (q_, pts_)
                         for q_, pts_ in POST_SHAPES_S[_t]]
# item 7 (A, C #6): unprinted tempo changes inside the theme and at Tempo I under the muted trumpet, to under 3 %: the
# caesuras at 72 and 632 (bars 18 / 158, between the theme's two phrases) 0.03 -> 0.02 s; the four arcs that end at
# bars 174, 182, 190, 194 (no printed breath mark; the score keeps Tempo I there) "sub" -> "light" (tools). The arcs
# that end on printed breath marks (712, 744) and every printed ramp stay. C15_TEMPO=0 builds the c14 map
if _os15.environ.get("C15_TEMPO", "1") == "1":
    CAESURA = {**CAESURA, 72.0: 0.02, 632.0: 0.02}
    PHRASE_ARCS = [((a_[0], a_[1], "light") if (a_[0], a_[1]) in ((680, 696), (712, 728), (744, 760), (760, 776)) else a_) for a_ in PHRASE_ARCS]
# the c14 Trumpet 1 shape at 987.16 is a step at the moved note-on of the legato target 987.5 (the target's lead moves
# by a few ms with the velocity cap): meant to act inside that transition
LEG_RAMP_OK = dict(LEG_RAMP_OK, **{"Trumpet 1": [987.5]})
# coordinator (Movement II c52, tested on 127 row-change joins): the keyswitch of every remaining row change on the
# theme lines goes 0.15 s before its note (not earlier than 5 ms after the previous note-on): first theme "Sus MAX" /
# staccato-row changes, second theme "Leg Slur MAX" / "Leg BC MAX" / "Sus MAX" changes. C15_KS=0 builds without it
if _os15.environ.get("C15_KS", "1") == "1":
    # Range test R1: on the second theme's legato rows (264-328, 744-792) the early keyswitch came with joins +36..+45 ms
    # later at the median (Violins I 187-198: 12 / 3 -> 17 / 11 outside 25 / 60 ms with no other change on most notes):
    # only the first-theme spans (sustain and staccato rows) keep it
    KS_LEAD_SPANS = {t_: [(a_, b_, 0.15) for a_, b_ in ((40.0, 104.0), (600.0, 680.0))]
                     for t_ in ("Violins I", "Violins II", "Violas")}
    KS_LEAD_SPANS.update({"Violoncellos": [(104.0, 136.0, 0.15)], "Double basses": [(104.0, 136.0, 0.15)]})
    KS_LEAD_SPANS["Violins I"] = KS_LEAD_SPANS["Violins I"] + [(104.0, 136.0, 0.15)]
# Movement II c53 (coordinator): rows keyed on a note-on follow lead changes. The cello front at 264 started 0.31 s
# before the beat; its note-on is now 0.21 s before it
LEVEL_SHAPES_S["Violoncellos"] = [((q_, [(-0.23, 0.0), (-0.21, 5.0), (0.12, 5.0), (0.40, 0.0)]) if q_ == 264.0 and pts_[1] == (-0.31, 5.0) else (q_, pts_))
                                  for q_, pts_ in LEVEL_SHAPES_S["Violoncellos"]]
# Movement II c53 (coordinator): a note moved to another row can start 3-7 dB under its body (a printed new bow that
# starts like the middle of a slur). build/steady_fronts.json {track: [[score qn, [[s, dB], ...]]]}: level-only start
# shapes fitted on the range render (fit15.py: notes of 0.6 s or longer whose start is more than 3 dB under the body)
_C15_FR = json.load(open(f"{BUILD}/steady_fronts.json")) if _os15.path.exists(f"{BUILD}/steady_fronts.json") else {}
if _C15_STEADY:
    for _t, _rows in _C15_FR.items():
        LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(float(q_), [tuple(p_) for p_ in pts_]) for q_, pts_ in _rows]

# ---------- mvt3 c16 (2026-11-11; critics on the c15 render: cycles/c16/reports/A-C.md; coordinator's rulings) ----------
# Item 1 (first priority; Dan, 11 Nov: the volume lane showed "large peaks and valleys on so many individual notes").
# c15 had 53,696 envelope points, 2,357 of 9,061 notes moving 3 dB or more inside the note. Tools: VOL_PER_NOTE (the
# on / cap3 / off switch for the range table; env STP_VOL_PER_NOTE), VOL_LIN (ramps drawn as ramps), build_reaper.py
# THIN_DB (collinear points dropped). Per layer:
VOL_LIN = True
# 1c: every level step between two notes is keyed to the next note's SCORE onset (30 ms crossfade), not its led note-on
LEVEL_STEP_AT_SCORE = True
# 1c accents (A #2): strings and woodwinds front-weighted from the moved note-on (was: 0 dB at the score onset, peak at
# +0.07..+0.25 s, back at +0.60 s, so a quarter's accent ran 0.24 s into the next note and runs of accents stacked to
# 4.5-5.4 dB; accented fronts measured 0.9-3.7 dB weaker than plain ones). No stacking, +3 dB at most (sf excepted),
# one flat level on notes of an eighth or less. The brass keep their c09 shape (Trombone 1 / Bass trombone fronts good)
ACCENT_SWELL_FROM_MOVED = ("brass", "string", "wind")
# (A proposed (0.02, 0.12, 0.35): simulated on the c15 stems the accents then stood 1.4-2.5 dB over their neighbours on
# the upper strings, at the low end of Dan's 2-4 dB; the plateau runs to +0.18 s)
GENTLE_ACCENT = dict(GENTLE_ACCENT, string=dict(GENTLE_ACCENT["string"], swell_s=(0.02, 0.18, 0.40)),
                     wind=dict(GENTLE_ACCENT["wind"], swell_s=(0.02, 0.18, 0.40)))
ACCENT_FRONT = ("string", "wind")
ACCENT_NO_STACK = True
ACCENT_CAP_DB = 3.0
ACCENT_SHORT_FLAT_QN = 0.5
# 1c: notes of an eighth or less: one level per note (stepped pitch and note trims, no slur-pair release inside)
SHORT_ONE_LEVEL_QN = 0.5
# 1c UNI_BOOST (B #4: the per-note +3 dB switch made the line less even in all seven lines measured): one held level
# per doubled phrase; Horn 1 / Horn 2 / Trumpet 1 keep their c15 mean level (they fall 1.5-2.4 dB without the boost)
UNI_BOOST_HOLD_QN = 2.0
# 1c: the c15 +3 dB fronts on the theme's accented halves were the accent's weight a second time (now the accent is
# front-weighted itself); the +1 dB at 40 and 600 stays
if _C15_STEADY:
    for _t in _C15_SPANS:
        LEVEL_SHAPES_S[_t] = [x_ for x_ in LEVEL_SHAPES_S.get(_t, [])
                              if not (x_[0] in _C15_ACC[_t] and len(x_[1]) == 4 and x_[1][1][1] == 3.0 and x_[1][3] == (0.30, 0.0))]
# 1c steady levels (A #1, B #2, C #2): c15 fitted one level step per theme note (506 values, -14.0 to +9.0 dB), most of
# it one offset per row. Now: one level per row and span group (build/steady_rows.json), the staccato rows' offset
# moved into velocity (ROW_VEL_SPANS; rows refitted on the range render by cycles/c16/actor_scripts/rowfit.py), and only
# the notes 3 dB or more from their row level keep a value (build/steady_levels.json: 97 of 506; basses from 1.5 dB,
# their steps measured as a gain; cycles/c16/actor_scripts/reduce_levels.py)
_C16_ROWS = json.load(open(f"{BUILD}/steady_rows.json")) if _os15.path.exists(f"{BUILD}/steady_rows.json") else {}
if _C15_STEADY:
    for _t, _sps in _C15_SPANS.items():
        for _sp in STEADY_LINE[_t]:
            _g = next((v_ for k_, v_ in _C16_ROWS.get(_t, {}).items()
                       if float(k_.split("-")[0]) <= _sp["from"] < float(k_.split("-")[1])), None)
            if _g is not None and _sp.get("level_default") is _C15_LVDEF[_t]:
                _sp["level_default"] = _g
# range render R1 (velchk.py: the rows answer to velocity): Violins I 100 -> 84 -9.4 dB, 118 -> 96 -3.4; Violas 100 -> 80
# -7.8; Violoncellos 118 -> 96 -11.0; Double basses -7.3. Violins I 40-104 84 -> 88; Violins II 600-680 118 -> 100 (its
# staccato quarters stood 4.6 dB over the sustain row with -3.9 dB on them)
ROW_VEL_SPANS = {"Violins I": {"Staccatissimo RRx9": [(40.0, 104.0, 88), (600.0, 680.0, 96)]},
                 "Violins II": {"Stac RRx9": [(600.0, 680.0, 100)]},
                 "Violas": {"Stac RRx9": [(40.0, 104.0, 80)]},
                 "Violoncellos": {"Stac RRx9": [(104.0, 136.0, 96)]},
                 "Double basses": {"Staccato RRx9": [(104.0, 136.0, 96)]}}
# Item 3: the celli / basses release fades after the stops of bars 2 and 6 are deleted (they made those stops drier:
# 17.4 / 18.0 dB at +0.3 s against the 17 dB limit); bar 94's (374.0) stays. The return rides are in mix.json
for _t in ("Violoncellos", "Double basses"):
    POST_SHAPES_S[_t] = [(q_, pts_) for q_, pts_ in POST_SHAPES_S[_t] if q_ not in (5.0, 21.0)]
# Item 5 (B #6): the basses' metric steps in bars 273-277 alternated 6.2 dB between successive eighths: 3 dB at most
METRIC_BOWED_DB_SPANS["Double basses"] = [
    (a_, b_, {"down": 1.5, "mid": 1.5, "beat": 0.5, "off": -1.5}) if a_ == 1088.0 else (a_, b_, o_)
    for a_, b_, o_ in METRIC_BOWED_DB_SPANS["Double basses"]]
# Item 4a (C #4): the theme's return in coda 1 (792-816) and the Piu allegro (984-1056) on one row, as the first theme
# since c15: 14 + 63 changes onto a legato row remained there. Class leads start from each track's 600-632 classes and
# are fitted on the range render (build/steady_leads.json, keys "792-816", "984-1056", "984-1012"); one level per span
# (steady_rows.json, the span's level against c15: the sustain row is louder than the legato rows it replaces)
_C16_SPANS = {"Violins I": [(792.0, 816.0), (984.0, 1056.0)], "Violins II": [(792.0, 816.0), (984.0, 1056.0)],
              "Violas": [(792.0, 816.0), (984.0, 1056.0)], "Violoncellos": [(792.0, 816.0), (984.0, 1012.0)]}
_C16_ACC = [793.0, 801.0, 985.0, 993.0, 1001.0, 1009.0]
if _os15.environ.get("C16_STEADY", "1") == "1":
    for _t, _sps in _C16_SPANS.items():
        for _a, _b in _sps:
            _k = f"{_a:g}-{_b:g}"
            _b0 = _C15_LEADS.get(_t, {}).get("600-632", {})
            _ld = dict({"slur": _b0.get("slur", _C15_BASE[_t]), "tongue": _b0.get("tongue", _b0.get("slur", _C15_BASE[_t])),
                        "first": _b0.get("first", _C15_BASE[_t]), "rep": _b0.get("rep", _b0.get("slur", _C15_BASE[_t])),
                        "acc": _b0.get("acc", 0.09)}, **_C15_LEADS.get(_t, {}).get(_k, {}))
            STEADY_LINE[_t].append({
                "from": _a, "to": _b, "art": "Sus MAX", "lead_s": _ld["slur"], "tongue_lead_s": _ld["tongue"],
                "first_lead_s": _ld["first"], "rep_lead_s": _ld["rep"], "overlap_s": 0.02, "gap_s": 0.03, "rep_gap_s": 0.09,
                "poly": True, "level_all": True, "level_db": {}, "level_default": _C16_ROWS.get(_t, {}).get(_k, {}),
                "at": {q_: {"lead_s": _ld["acc"]} for q_ in _C16_ACC if _a <= q_ < _b}})
        ROW_TRIM_SKIP[_t] = list(ROW_TRIM_SKIP.get(_t, [])) + [(a_ - 0.3, b_) for a_, b_ in _sps]
        KS_LEAD_SPANS[_t] = list(KS_LEAD_SPANS.get(_t, [])) + [(a_, b_, 0.15) for a_, b_ in _sps]
# Item 4b (A #6): Violins I's entries after rests at 48 and 608 are late on "Sus MAX" (stem -10.1 / -11.9 dB in the first
# 50 ms after the beat with a flat envelope; leads 90 / 66 ms): 0.15 / 0.14 s. (61 and 64 read late through the early
# level step of the next eighth: no lead change, the steps are keyed to the score onset now.)
if _C15_STEADY:
    for _sp in STEADY_LINE["Violins I"]:
        for _q, _l in ((48.0, 0.15), (608.0, 0.14)):
            if _sp["from"] <= _q < _sp["to"] and "level_all" in _sp:
                _sp["at"] = {**_sp.get("at", {}), _q: {"lead_s": _l}}
# Item 4f (A #4, S1): same-pitch repeats that did not separate (dips 0.4-2.2 dB): inside the new spans the repeat gap
# is 0.09 s (research default 60-100 ms; the c15 spans keep 0.05). (ROW_LEAD_KEEP_GAP on the violas' repeats of 816-840
# did not change their 53 ms gaps: those leads are not ROW_LEAD_S leads. Open for c17.)
# Item 4e (C #4): the basses' repeated eighths on a short row with velocity by position, no fader dips and no metric
# steps there. _C16_CB_ROW / _C16_CB_SPANS are the built values ("" = the c15 "Sus MAX" strokes with the dips); env C16_CB
# ("Stac On Bow RRx9" / "Marc Shrt RRx4" / "none") and C16_CB_SPAN ("792-840" or "792-840,984-1108") override them for
# the range test (cycles/c16/actor_scripts/p1cb.sh, cbtest.py). Result in cycles/c16/CHANGES.md
_C16_CB_ROW, _C16_CB_SPANS = "Stac On Bow RRx9", "792-840,984-1108"
_C16_CB = _os15.environ.get("C16_CB", _C16_CB_ROW)
if _C16_CB and _C16_CB != "none":
    ART_SPANS = dict(ART_SPANS)
    for _sp16 in _os15.environ.get("C16_CB_SPAN", _C16_CB_SPANS).split(","):
        _a16, _b16 = (float(x_) for x_ in _sp16.split("-"))
        ART_SPANS["Double basses"] = list(ART_SPANS.get("Double basses", [])) + [
            {"from": _a16, "to": _b16, "art": _C16_CB, "max_qn": 0.5, "unslurred": True, "len_frac": 0.58,
             "vel_metric": ({"down": 110, "mid": 98, "beat": 98, "off": 88} if "C16_CB" in _os15.environ
                            else {"down": 90, "mid": 80, "beat": 80, "off": 70}), "vel_jit": 5}]
        def _cut16(sps_, a16_=_a16, b16_=_b16):
            out_ = []
            for s_ in sps_:
                a_, b_ = s_[0], s_[1]
                if b_ <= a16_ or a_ >= b16_:
                    out_.append(s_); continue
                if a_ < a16_: out_.append((a_, a16_) + tuple(s_[2:]))
                if b_ > b16_: out_.append((b16_, b_) + tuple(s_[2:]))
            return out_
        STR_REP_DETACH["at"]["Double basses"] = _cut16(STR_REP_DETACH["at"]["Double basses"])
        METRIC_BOWED["Double basses"] = _cut16(METRIC_BOWED["Double basses"])
# coordinator (the scherzo's c15 critics, checked here with cycles/c16/actor_scripts/gapret.py): between the staccato
# quarters of the theme the level step fell back to 0 dB and returned (Violins I 46 / 62 / 78 / 94: 6.8 dB up and down
# in each gap): the spans hold their level across gaps of up to 1.25 qn
for _t in STEADY_LINE:
    for _sp in STEADY_LINE[_t]:
        if _sp.get("level_all"):
            _sp["level_rest_qn"] = 1.25
# the same for the row trims (Violas 108 / 110 / 124, Violins I 636-639: -4 / -4.5 dB returned to 0 in every gap)
ROW_TRIM_HOLD_QN = 1.0
# coordinator (the scherzo's c15 critics: beat weight helped no line there): ours, simulated on the c15 stems with the
# metric steps off (logs/stepmed_states_sim.log): Timpani 2.23 -> 4.02 and 1.36 -> 2.76 dB (kept); Violas 3.13 -> 3.00,
# Violoncellos equal (removed: no gain, fewer points); Double basses 2.30 -> 1.43 and 3.68 -> 3.00 (their steps are the
# beat weight itself; kept with the dips until the short-row test of item 4e decides)
METRIC_BOWED = {k_: v_ for k_, v_ in METRIC_BOWED.items() if k_ not in ("Violas", "Violoncellos")}


# ---------- mvt3 c16, final decision (Dan, 11 Nov 16:30Z, through the coordinator, during the lock) ----------
# "yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other
# ways to fix our problem". The track volume envelope keeps only slow balance: roles, printed hairpins and dynamics as
# ramps, the held unison phrase level, printed player-count marks, timpani roll levels over whole rolls, the final fade
# (and the return rides in mix.json). Every rule keyed to a single note is off, on every track, with no exceptions:
VOL_PER_NOTE = "off"
VOL_PER_NOTE_KEEP = ()
VOL_PER_NOTE_RULES = tuple(VOL_PER_NOTE_RULES) + ("swell", "sost")
CHORD_CUTS = False            # divisi / double-stop / tremolo-chord cuts and ROW_GAIN_DB (rows: mix.json row_volume_db)
POST_SHAPES_S = {}            # the release fade after the stop of bar 94 (a shape keyed to one note end)
# Instrument-side replacements made in this cycle:
# - accents: a CC11 (CC1 on the brass and clarinets) bump of 5 units on every printed accent (ACCENT_BUMP_AT; c00's 8
#   units reached the top layer and were heard as harsh), in place of the fader swell
ACCENT_BUMP_AT = {t_[0]: 5 for t_ in TRACKS if t_[3] in ("wind", "brass", "string")}
# - the theme's staccato rows: velocity (ROW_VEL_SPANS above); each one-row span keeps one level, as a role
# (cycles/c16/actor_scripts/span_roles.py wrote the span levels of build/steady_rows.json into build/roles.json)
# - the basses' repeated eighths (792-840, 984-1108): "Stac On Bow RRx9" at 58 % of the slot, velocity by position in
#   the bar (range test: separation median 9.8-12.8 dB with no fader dip, under 3 dB 12 / 6 / 5 of 86 / 128 / 103;
#   "Marc Shrt RRx4" 8.0-11.0 dB, 8 / 12 / 2; "Sus MAX" without its dips 0.2-4.9 dB). The test level stood 9-11 dB over
#   c15: velocities 110 / 98 / 98 / 88 -> 90 / 80 / 80 / 70. Its strokes read 42 / 24 ms early with the 0.04 s
#   staccato lead: 0.005 / 0.02 s in 792-840 / 984-1056 (ROW_LEAD_S)
ROW_LEAD_S["Double basses"] = dict(ROW_LEAD_S.get("Double basses", {}), **{"Stac On Bow RRx9": [(792.0, 840.0, 0.005), (984.0, 1056.0, 0.02)]})
# - Horn 1 / Horn 2 / Trumpet 1: the held unison phrase level (UNI_BOOST_HOLD_QN) stays; it is not keyed to single notes


# ---------- mvt3 c17 (2026-11-11; critics on the c16 render: cycles/c17/reports/A-C.md; coordinator's rulings 1-10) ----------
# Standing rule (Dan, 11 Nov): the track volume envelope holds slow balance only; every fix is on the instrument
# (CC11 / CC1 / CC7, velocity, rows, note lengths, gaps). tools/instr_post.py is the generic post-pass; its values:
_C17 = _os15.environ.get("C17", "1") == "1"
_C17_OFF = set(_os15.environ.get("C17_OFF", "").split(","))      # rule names left out (range tests)
# Ruling 1: a held unison level spans a whole phrase (8 qn or more, one level) or is dropped (45 plateaus of one or two
# notes in c16: Horn 1 795-808, Trumpet 2 656-662 and 983-995, ...)
if _C17:
    UNI_BOOST_MIN_QN = 8.0
    UNI_BOOST_ONE_LEVEL = True
# Ruling 2: the old 5-unit bump is replaced by the post-pass accents
if _C17:
    ACCENT_BUMP_AT = {t_[0]: 0 for t_ in TRACKS if t_[3] in ("wind", "brass", "string")}
# Ruling 7 (C #3): from qn 912 the celli play the printed whole notes of the pedal C (new bow on each bar line, with the
# basses and the brass chord changes); the merge stays for 892.5-912
STR_REP_NEW_BOW["skip"] = dict(STR_REP_NEW_BOW["skip"], Violoncellos=[(892.5, 911.5)] if _C17 else [(892.5, 940.5)])
# Ruling 4c (A #1, B #3): the basses' short-row eighths: 45 % of the slot; velocity across the layer boundary between
# 88 and 100 (velocity 65-95 gave no beat weight); the onset lead is in INSTR_POST row_onset (ROW_LEAD_S acts only on
# abutting notes)
_C17_CB_VEL = {"down": 100, "mid": 92, "beat": 96, "off": 84}
if _C17:
    ART_SPANS["Double basses"] = [dict(s_, len_frac=0.45, vel_metric=dict(_C17_CB_VEL), vel_jit=3)
                                  if s_.get("art") == "Stac On Bow RRx9" else s_ for s_ in ART_SPANS["Double basses"]]
    ROW_LEAD_S["Double basses"] = {k_: v_ for k_, v_ in ROW_LEAD_S.get("Double basses", {}).items() if k_ != "Stac On Bow RRx9"}
# Ruling 6 (A #5, B #5): timpani. The right-hand strokes (TIMP_RH_ALT keys, +24) measure 4 dB over the left-hand ones
# at equal velocity (cycles/c17/actor_scripts/timpmeas.py on the c16 stem: G 43 -39.4 / 67 -35.5, C 48 -41.5 / 72
# -37.5 dB at velocity 110; 0.27 dB per step), and the off-beat strokes are the right-hand ones: that is why on-beat
# strokes stood 2-3 dB under the off-beat ones. Right hand -12 steps (vel_pitch), bar position spread 16 steps
if _C17:
    # (range render T1 with 2.5: stem +1.7..+2.5 dB over c16 where c16 stood 2.8-4.5 under c15: 4.0)
    TIMP_ROLL_TRIM_DB = [(c_, round(d_ - 4.0, 2)) for c_, d_ in TIMP_ROLL_TRIM_DB]
    TIMP_METRIC_VEL = {"down": 6, "mid": 0, "beat": -4, "off": -10, "jit": 3, "min_cc": DYN["f"]}
_C17_REST = {
    # resting level of plain notes at ff (and above): the controller has no room for an accent at 114 (strings /
    # woodwinds slope 0.1-0.2 dB per unit there). mix.json dyn_trim_db ff / fff carry the level back (slow)
    "string": {"cc11": [(0, 0), (88, 88), (114, 105), (124, 116), (127, 119)]},
    # (first build: winds 98 at ff. Movement I c58: 88-98 is a plateau on the wind rows, so ff would sit level with f;
    # 104, above it, as the strings)
    "wind": {"cc11": [(0, 0), (88, 88), (114, 104), (124, 113), (127, 116)]},
    "brass": {"cc11": [(0, 0), (88, 88), (114, 100), (124, 106), (127, 108)]},
}
for _t in ("Clarinet 1", "Clarinet 2"):          # CC1-layered like the brass: CC11 is plain volume
    _C17_REST[_t] = _C17_REST["brass"]
_C17_ACC_SHAPE = {"pre_s": 0.02, "hold_s": 0.15, "end_s": 0.45}
_C17_ACC = {
    "string": [dict(_C17_ACC_SHAPE, lane="cc11", amt=[(46, 8), (72, 10), (88, 16), (114, 19)], max=124)],
    # (soft woodwind accents stay small: in the bassoon / clarinet family patches the next layer fades in at CC11 30-38,
    # kit LEARNINGS section 4: +4 units added 8-11 dB on one bassoon pitch)
    # (range render T1: flutes +3.1 / +4.5 dB with 26 units at ff: 22)
    "wind": [dict(_C17_ACC_SHAPE, lane="cc11", amt=[(34, 2), (46, 5), (72, 10), (88, 14), (114, 20)], max=124)],
    # brass and clarinets: a volume accent (CC11 is the Global Group volume there, no change of layer: weight, not
    # bite), 21 % of the resting value, plus a small CC1 part (the patch's CC1 controller fades over 120 ms: 0.08 s early)
    "brass": [dict(_C17_ACC_SHAPE, lane="cc11", amt_rel=0.21, max=127),
              dict(_C17_ACC_SHAPE, lane="cc1", amt=[(0, 5)], max=112, pre_s=0.08)],
}
for _t in ("Horn 1", "Horn 2", "Horn 3", "Horn 4"):
    _C17_ACC[_t] = [dict(_C17_ACC_SHAPE, lane="cc11", amt_rel=0.21, max=127),
                    dict(_C17_ACC_SHAPE, lane="cc1", amt=[(0, 7)], max=117, pre_s=0.08)]
for _t in ("Clarinet 1", "Clarinet 2"):
    _C17_ACC[_t] = [dict(_C17_ACC_SHAPE, lane="cc11", amt_rel=0.21, max=127),
                    dict(_C17_ACC_SHAPE, lane="cc1", amt=[(0, 6)], max=112, pre_s=0.08)]
# range render T1 (accent over neighbours, c16 -> T1): strings 0.7-2.2 -> 2.5-3.2 dB, woodwinds -0.6..1.6 -> 2.5-4.5,
# Horn 1 2.5 -> 4.2, Trumpet 1 / 3 0.5 / 2.9 -> 5.3 / 5.0, trombones / tuba 0.2-1.6 -> 2.1-3.2; fronts no brighter than
# plain notes. Trumpets 21 % -> 13 % (CC1 +3), Horn 1 -> 16 %
for _t in ("Trumpet 1", "Trumpet 2", "Trumpet 3"):
    _C17_ACC[_t] = [dict(_C17_ACC_SHAPE, lane="cc11", amt_rel=0.13, max=127),
                    dict(_C17_ACC_SHAPE, lane="cc1", amt=[(0, 3)], max=112, pre_s=0.08)]
_C17_ACC["Horn 1"] = [dict(_C17_ACC_SHAPE, lane="cc11", amt_rel=0.16, max=127),
                      dict(_C17_ACC_SHAPE, lane="cc1", amt=[(0, 7)], max=117, pre_s=0.08)]
_C17_NOTE_CC = {
    # Ruling 4a (B #3, dynamic removed, 226 "Sus MAX" notes): E flat 2 -7.1, F sharp 1 -4.4, F1 / F2 -3.7, E2 -2.6,
    # E flat 1 -1.9, B flat 1 -1.4; G1 +2.0, C sharp 2 +2.5, A flat 1 +2.9 dB. Units from 0.32 dB per unit under 100 and
    # 0.16 at 100-114 (the lane is flat above 114, so at ff weak pitches gain little and loud ones are lowered)
    "Double basses": [
        # range render T1: velocity 80-100 does nothing on "Stac On Bow RRx9" (peak by velocity -27.6 / -28.5 / -26.0 /
        # -27.9 / -26.8 / -27.5 dB at 80 / 84 / 88 / 92 / 96 / 100): the beat weight is a CC11 offset on the off-beat
        # eighths (the half-note beat is "on")
        # (range render T2 with -10 units: on-beat strokes 0.8-1.6 dB over the off-beat ones; -22 for about 3 dB)
        {"lane": "cc11", "rows": ("Stac On Bow",), "beat": {"period": 2.0, "on": 0, "off": -22}},
        # (first form, a CC11 table: {27: 6, 29: 12, 30: 14, 31: -6, 32: -9, 34: 4, 37: -8, 39: 20, 40: 8, 41: 12}. Replaced
        # before the first build by per-region volumes in the Opus state, the scherzo's c15 technique: mix.json
        # "region_gain_db" on the Sus / Leg rows, exact dB at every dynamic; CC11 cannot raise a weak pitch at ff)
        # the short row's own pitch levels (B #3, 984-1080): A flat 1 -24.8, D2 -27.5, A1 -27.9, G1 -30.4, C2 -31.0,
        # F1 -31.9, F2 -34.9, E2 -36.7 dBFS
        # (not applied: B's table and the actor's peak measure on the same stem disagree on the order of the pitches
        # (A flat 1 loudest / among the softest), so no table for this row until a range render settles it)
    ],
    # Ruling 3 (B #2): "Leg Slur MAX" 3-7 dB under "Sus MAX" at f / ff on the strings (Violins II -4.3 / -7.1). The
    # legato rows are raised and the sustain row lowered about the same line level, by printed dynamic
    "Violins I": [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, 6), (114, 12)], "Sus MAX": [(72, 0), (88, -4), (114, -2)]}}],
    "Violins II": [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, 8), (114, 14)], "Sus MAX": [(72, 0), (88, -6), (114, -6)]}}],
    "Violas": [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, 8), (114, 10)], "Sus MAX": [(72, 0), (88, -6), (114, -2)]}}],
    "Violoncellos": [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, 6), (114, 10)], "Sus MAX": [(72, 0), (88, -5), (114, -3)]}}],
    # Ruling 10 (B #6): muted Trumpet 1, bars 171-186: C4 / D4 -4.0 dB, C5 +3.0, D5 +3.8, E flat 5 and above +7..+10
    # about the line's median at one controller value (0.8 dB per CC1 unit at this level)
    "Trumpet 1": [{"lane": "cc1", "rows": ("Mute",), "pitch": {**{60: 5, 62: 5, 72: -4, 74: -5}, **{p_: -8 for p_ in range(75, 90)}}}],
}
_C17_GAP = {
    # Ruling 5 (A #3, B #5): tongued (unslurred) joins on the sustain rows with a played gap under 60 ms run together
    # (dips 0.5-2.9 dB; 60-100 ms: 4.7-12 dB)
    # (the chorale's whole notes, 888-936.5, take their own breath: INSTR_POST gap_set)
    "brass": {"floor_s": 0.09, "cap_frac": 0.5, "min_len_s": 0.07, "rows": ("Sus",), "prev_rows": ("Sus", "Leg"), "skip": [(888.0, 936.5)]},
    "wind": {"floor_s": 0.068, "cap_frac": 0.4, "min_len_s": 0.07, "rows": ("Sus",), "prev_rows": ("Sus", "Leg")},
}
# range render T1 (separation at the changed joins, c16 -> T1): Tuba 2.3 -> 5.6 dB, Trumpet 1 2.9 -> 5.6, Flute 1 2.5
# -> 6.3, Clarinet 1 1.0 -> 4.3, Bassoon 1 1.0 -> 3.8, Trombone 1 2.3 -> 3.3, Horn 1 1.2 -> 2.6, Oboe 1 0.5 -> 2.3,
# Horn 3 -1.1 -> -1.5: horns and trombones 0.12 s, oboes 0.085 s
for _t in ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trombone 1", "Trombone 2", "Bass trombone"):
    _C17_GAP[_t] = dict(_C17_GAP["brass"], floor_s=0.12)
for _t in ("Oboe 1", "Oboe 2", "Cor anglais"):
    _C17_GAP[_t] = dict(_C17_GAP["wind"], floor_s=0.085)
_C17_RR_C2 = [0.030, 0.066, 0.031, 0.067, 0.058, 0.037, 0.048, 0.073, 0.057]   # A #1: half-rise by position - 0.045 s
INSTR_POST = {
    "rest_map": _C17_REST,
    "accent": _C17_ACC,
    "note_cc": _C17_NOTE_CC,
    "gap_floor": _C17_GAP,
    # (range render T1 with 0.06 s: half-rise against the grid -14 / -31 / -31 / -4 ms by c17meas.py cb, where c16 read
    # +40 / +20 / +10 / +20; critic A's detector read c16 +79 / +96 / +56 / +57. The two detectors differ by about
    # 40-50 ms on these 43-87 Hz strokes, so the lead is set between them: 0.04 s)
    # Ruling 7, second part (A #3): the chorale's brass whole notes (888-936) dipped 4-12 dB at every bar line with the
    # 0.09 s re-tongue gap: a breath of 0.045 s there
    "gap_set": {"brass": [{"from": 888.0, "to": 936.5, "min_qn": 3.0, "gap_s": 0.045}]},
    "row_onset": {"Double basses": [
        {"row": "Stac On Bow", "from": 792.0, "to": 840.0, "lead_s": 0.04},
        {"row": "Stac On Bow", "from": 984.0, "to": 1056.0, "lead_s": 0.04},
        {"row": "Stac On Bow", "from": 1056.0, "to": 1108.0, "lead_s": 0.04,
         **({"rr_leads_s": _C17_RR_C2, "rr_pitch": 36} if _os15.environ.get("C17_RR", "0") == "1" else {})}]},
    # (per-position leads are off: with a second detector (c17meas.py cb) the nine positions read 95, 82, 58, 102, 22,
    # 66, 47, 64, 98 ms on the same stem, so A's table is the detector's as much as the samples'; flat 0.06 s)
    # Ruling 8 (A #6, B #6, C #2): the tail of the bar 204 stop is the celli's dry open G2: the celli / basses note
    # ends 0.075 s early with a CC11 fall inside Opus (before the sends); the returns are not touched
    "note_end": {"Violoncellos": [{"end": 814.0, "early_s": 0.075}], "Double basses": [{"end": 814.0, "early_s": 0.075}]},
    "cc_shape": {t_: [{"lane": "cc11", "at": 814.0, "pts": [(-0.215, 0), (-0.075, -32), (0.44, -32), (0.50, 0)]}]
                 for t_ in ("Violoncellos", "Double basses")},
    # Ruling 7 (C #3): the pedal C of bars 229-234 (and the celli in 1088-1104): no gap at the bow change, a swell of
    # 8 units (at most 9 % of the lane) across each join; the same on the worst re-bow holes elsewhere
    "rebow_join": {"Violoncellos": [{"from": 912.0, "to": 936.5, "gap_s": 0.005, "swell": 8, "swell_rel": 0.09},
                                    {"from": 1088.0, "to": 1104.5, "gap_s": 0.005, "swell": 8, "swell_rel": 0.09},
                                    {"at": [185.29], "gap_s": 0.005, "swell": 8, "swell_rel": 0.09}],
                   "Double basses": [{"from": 912.0, "to": 936.5, "gap_s": 0.005, "swell": 8, "swell_rel": 0.09},
                                     {"at": [567.03, 578.0], "gap_s": 0.005, "swell": 8, "swell_rel": 0.09}],
                   "Violas": [{"at": [564.0], "gap_s": 0.005, "swell": 8, "swell_rel": 0.09}]},
    # Ruling 10 (A #6): the sfp of bar 149 (qn 592): the strings' p lasted 0.3 s (CC11 46 at 592.83, 71 at 593.5):
    # the lane stays under 52-54 until 594.5 and reaches the printed arrival over 594.5-600
    "cc_cap": {t_: [{"lane": "cc11", "pts": [(592.8, 52), (594.5, 54), (597.5, 106), (600.0, 127)]}]
               for t_ in ("Violins I", "Violins II", "Violas", "Violoncellos")},
    "vel_pitch": {"Timpani": [{"row": "", "pitch": {p_: -12 for p_ in range(60, 90)}, "min": 40}]},
    # Ruling 1 / 6 (C #4): the timpani roll levels leave the fader: the whole envelope is folded into CC7 (linear
    # amplitude in Opus), 2.5 dB lower, and mix.json gain_db rises by 2.5 (strokes +2.5 dB, rolls where they were)
    # (the rolls into 888 and 984 stand 7.7 / 5.4 dB over a stroke at CC7 127, so the strokes sit at CC7 -5.2 dB:
    # first build: shift 5.2, roll trims 2.5 dB lower, gain +0.7; final: shift 5.0, roll trims 4.0 lower, gain +2.0)
    "vol_to_cc7": {"Timpani": {"shift_db": 5.0}},
    # Ruling 1 (A #6, B, C #4): no fader move of 2 dB or more within 60 ms inside a sounding note (the final fade
    # excepted): hairpin-gain and held-decrescendo releases, role / player-count edges move to the led note's note-on
    # Movement I c58 (coordinator): the dynamic trims step at the score onset, inside the led note's first 50-240 ms
    "dyn_step_on": {"min_cc": 8, "pre_s": 0.03},
    "vol_guard": {"min_db": 2.0, "win_s": 0.06, "rate_db_s": 20.0, "pre_s": 0.03, "lead_max_s": 0.45, "skip_after": 1112.9},
}
# Ruling 10 (A #4, B #6): the c14 per-pluck levels (build/pluck_trims.json, fitted in dB after the CC16 resets at 200,
# 456, 680; off the fader since c16: celli 11.6-15.4 dB range at one velocity) as velocity; steps per dB fitted on a
# range render (cycles/c17/actor_scripts/pluckvel.py)
# (range render T1 at 3 steps per dB: celli 0.16, basses 0.12 dB per step: 6 and 8 steps per dB)
_C17_PLUCK_STEPS = {"Violoncellos": 6.0, "Double basses": 8.0}
_pt17 = json.load(open(f"{BUILD}/pluck_trims.json")) if _os15.path.exists(f"{BUILD}/pluck_trims.json") else {}
INSTR_POST["vel_db"] = {t_: [{"row": "Pizz", "table": {str(q_): pts_[1][1] for q_, pts_ in rows_}, "steps_per_db": _C17_PLUCK_STEPS.get(t_, 6.0),
                              "min": 8, "max": 110}]
                        for t_, rows_ in _pt17.items() if not t_.startswith("_")}
for _k in _C17_OFF:
    INSTR_POST.pop(_k, None)
if not _C17:
    INSTR_POST = None


# ---------- mvt3 c18 (2026-11-15; critics on the c17 render: cycles/c18/reports/A-C.md; coordinator's rulings 1-12) ----------
# Dan after c17: "The accents are little bit over done now". Standing rule: no per-note fader move.
_C18 = _os15.environ.get("C18", "1") == "1"
if _C18 and INSTR_POST:
    # Ruling 1: accents about half of c17, at the front of the note (the c17 bump stood 60-450 ms after the note-on:
    # A's four-window table), a 12-unit step cap, and a scale where many staves accent one onset
    # (the scale for doubled beats of the first ruling, "tutti_scale": [(9, 0.75), (16, 0.6)], was taken out before the
    # render on the coordinator's later note from Movement I c59: when every track rises E dB the sum rises E dB, so
    # the scale only makes tutti accents weaker than solo ones)
    _C18_SH = {"pre_s": 0.03, "hold_s": 0.06, "end_s": 0.22, "max_step": 12}
    _C18_ACC = {
        "string": [dict(_C18_SH, lane="cc11", amt=[(46, 4), (72, 5), (88, 8), (114, 10)], max=124)],   # (116 left no room on the legato rows at ff: 105 + 12)
        "wind": [dict(_C18_SH, lane="cc11", amt=[(34, 1), (46, 3), (72, 5), (88, 7), (114, 10)], max=118, min_units=1)],
        "brass": [dict(_C18_SH, lane="cc11", amt_rel=0.10, max=127),
                  dict(_C18_SH, lane="cc1", amt=[(0, 2)], max=112, pre_s=0.08)],
    }
    for _t in ("Violins I", "Violoncellos"):          # B: +4.7 / +4.5 dB at f in c17
        _C18_ACC[_t] = [dict(_C18_SH, lane="cc11", amt=[(46, 4), (72, 5), (88, 7), (114, 10)], max=124)]
    for _t in ("Flute 1", "Flute 2"):                  # A: median +4.7 / +4.3 dB in c17
        _C18_ACC[_t] = [dict(_C18_SH, lane="cc11", amt=[(34, 1), (46, 3), (72, 4), (88, 6), (114, 8)], max=118, min_units=1)]
    for _t in ("Horn 2", "Horn 3", "Horn 4"):
        _C18_ACC[_t] = [dict(_C18_SH, lane="cc11", amt_rel=0.10, max=127),
                        dict(_C18_SH, lane="cc1", amt=[(0, 3)], max=117, pre_s=0.08)]
    _C18_ACC["Horn 1"] = [dict(_C18_SH, lane="cc11", amt_rel=0.08, max=127),
                          dict(_C18_SH, lane="cc1", amt=[(0, 3)], max=117, pre_s=0.08)]
    for _t in ("Clarinet 1", "Clarinet 2"):
        _C18_ACC[_t] = [dict(_C18_SH, lane="cc11", amt_rel=0.10, max=127),
                        dict(_C18_SH, lane="cc1", amt=[(0, 3)], max=112, pre_s=0.08)]
    for _t in ("Trumpet 1", "Trumpet 2", "Tuba"):      # no CC1 part
        _C18_ACC[_t] = [dict(_C18_SH, lane="cc11", amt_rel=0.06, max=127)]
    _C18_ACC["Trumpet 3"] = [dict(_C18_SH, lane="cc11", amt_rel=0.05, max=127)]   # C: median +4.6 in c17, +3.7 in c16
    for _t in ("Trombone 2", "Bass trombone"):         # A: the CC1 part made their fronts 5-7 dB brighter in 2-5 kHz
        _C18_ACC[_t] = [dict(_C18_SH, lane="cc11", amt_rel=0.10, max=127)]
    INSTR_POST["accent"] = _C18_ACC

    # Ruling 2: the fader. The release of a hairpin's dB gain is no faster than 2.8 dB/s (it was 2-4 dB over one
    # quarter on the held arrival note); the guard now catches every unprinted move of 1.5 dB or more steeper than
    # 3 dB/s inside a sounding note (c17: 2 dB within 60 ms) and moves it into the rest before the note or stretches
    # it to 2.8 dB/s; the falls after fp / sfp are no longer kept on the fader (they are CC11 now: cc_cap, cc_scale)
    HP_REL_MAX_DB_S = 2.8
    INSTR_POST["vol_guard"] = {"min_db": 1.5, "win_s": 0.5, "rate_db_s": 2.8, "pre_s": 0.03, "lead_max_s": 0.45,
                               "skip_after": 1112.9, "hairpin_ok": True, "fall_keep_db": 99.0, "max_iter": 8,
                               "rate_short_db_s": 20.0, "short_s": 0.5,
                               # the end of the introduction's figure level (roles [8.8, 15.9], bars 3-4): it falls over
                               # the figure's last eighth, before the ff chord of bar 5; moved earlier it undid the level
                               "skip": [(15.2, 16.1)]}
    # B #4: Horn 3's held unison level in the counterstatement (+3.5 dB over 105-136; the loudest stem by 2.8 dB)
    VOL_RULE_OFF = dict(VOL_RULE_OFF, **{"Horn 3": dict(VOL_RULE_OFF.get("Horn 3", {}), uni_boost=[(103.0, 137.0)])})

    # Ruling 3: the sfp of bar 149 (qn 592). The sf gets a front (CC11 +10 from 0.03 s before the moved note-on, back by
    # 0.22 s; brass and clarinets CC1 +4 as well); the strings reach the printed ff at 596 (c17: 106 only at 597.5);
    # the p of the other staves is held by a ceiling in the lane instead of the fader rows [593, 596] (deleted)
    _C18_SFP = ["Flute 1", "Flute 2", "Oboe 1", "Oboe 2", "Cor anglais", "Clarinet 1", "Clarinet 2", "Bass clarinet",
                "Bassoon 1", "Bassoon 2", "Contrabassoon", "Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trumpet 3",
                "Trombone 1", "Trombone 2", "Bass trombone", "Tuba", "Violins I", "Violins II", "Violas",
                "Violoncellos", "Double basses"]
    # (range render I1 with a 0.10 s attack before the fall: the sf front stood 2 dB under the ff before it, +1.1 dB
    # over c17: a fresh sustain needs more than 0.15 s to speak; the fall now starts 0.22 s after the mark)
    SFP_SPIKE_S = (0.22, 0.42)
    _C18_CC1 = {t_ for t_ in _C18_SFP + ["Trumpet 1", "Trumpet 2"] if t_.startswith(tuple(CC1_DYN_TRACKS))}
    _cs = {t_: list(v_) for t_, v_ in INSTR_POST["cc_shape"].items()}
    for _t in _C18_SFP:
        _cs.setdefault(_t, []).append({"lane": "cc11", "at": 592.0, "from_note": True,
                                       "pts": [(-0.03, 10), (0.24, 10), (0.32, 0)]})
        if _t in _C18_CC1:
            _cs[_t].append({"lane": "cc1", "at": 592.0, "from_note": True, "pts": [(-0.08, 4), (0.24, 4), (0.32, 0)]})
    _cap = {t_: [{"lane": "cc11", "pts": [(592.9, 52), (593.6, 58), (595.0, 86), (596.0, 105)]}]
            for t_ in ("Violins I", "Violins II", "Violas", "Violoncellos", "Double basses")}
    _C18_P = {"Flute 1": 40, "Flute 2": 40, "Oboe 1": 50, "Oboe 2": 50, "Cor anglais": 46, "Clarinet 1": 44,
              "Clarinet 2": 44, "Bass clarinet": 50, "Bassoon 1": 44, "Bassoon 2": 44, "Contrabassoon": 50, "Horn 1": 50,
              "Horn 2": 50, "Horn 3": 50, "Horn 4": 50, "Trumpet 3": 50, "Trombone 1": 50, "Trombone 2": 50,
              "Bass trombone": 50, "Tuba": 46}
    for _t, _x in _C18_P.items():
        _cap[_t] = [{"lane": "cc11", "pts": [(592.8, _x), (593.6, _x + 6), (595.0, 84), (596.0, 100 if _t in _C18_CC1 else 104)]}]
        if _t in _C18_CC1:
            _cap[_t].append({"lane": "cc1", "pts": [(592.8, _x - 4), (593.6, _x + 2), (595.0, 84), (596.0, 108)]})
    # the muted Trumpet 1, bars 181-182 (C #4): the per-bar fader rows 680-732 are deleted; the printed diminuendo to
    # the p of 728 in CC1 ("Mute Sus": 0.8 dB per unit), and G4 / A flat 4 +4 units
    _cap["Trumpet 1"] = [{"lane": "cc1", "pts": [(722.0, 60), (723.0, 59), (724.0, 58), (725.0, 54), (726.0, 51), (727.0, 47), (727.9, 41)]}]
    INSTR_POST["cc_cap"] = _cap
    # the fp of bar 209 (rows [833.25, 839]) and the sub. p of bar 219 (rows [871.7, 878] / [872, 880]) as a factor on
    # CC11 (the volume on brass and clarinets, 40 log10; the same law assumed on woodwinds and strings)
    _sc = {}
    for _t, _d in {"Horn 1": -1.5, "Horn 2": -3.5, "Horn 3": -1.5, "Horn 4": -3.5, "Trombone 2": -1.5, "Tuba": -5.0,
                   "Clarinet 1": -7.0, "Clarinet 2": -5.5, "Oboe 1": -8.5, "Bassoon 2": -7.0, "Violas": -5.0,
                   "Flute 2": -10.0}.items():
        _sc.setdefault(_t, []).append({"lane": "cc11", "pts": [(832.75, 0.0), (833.25, _d), (833.26, _d), (839.0, 0.0)]})
    for _t in ("Horn 3", "Horn 4", "Trumpet 1", "Trumpet 2", "Trumpet 3", "Trombone 1", "Trombone 2", "Bass trombone"):
        _sc.setdefault(_t, []).append({"lane": "cc11", "pts": [(871.2, 0.0), (871.7, -4.0), (874.0, -4.0), (878.0, 0.0)]})
    for _t, _d in {"Violoncellos": -5.0, "Flute 1": -8.0, "Cor anglais": -7.0}.items():
        _sc.setdefault(_t, []).append({"lane": "cc11", "pts": [(871.5, 0.0), (872.0, _d), (876.0, _d), (880.0, 0.0)]})
    # C #6: the held unison of bar 138 (Horns 3 / 4, rows [548, 552, +10.5 / +7.5]) inside the patch
    _sc.setdefault("Horn 3", []).append({"lane": "cc11", "pts": [(547.5, 0.0), (548.0, 10.5), (552.0, 10.5), (552.5, 0.0)]})
    _sc.setdefault("Horn 4", []).append({"lane": "cc11", "pts": [(547.5, 0.0), (548.0, 7.5), (552.0, 7.5), (552.5, 0.0)]})
    # passage levels whose edge falls on a held note with no rest (the guard would ride the note before for 1-3 s):
    # inside the patch instead of a role row (k: dB per decade of CC11: 40 exact on brass, about 33 on the woodwind
    # rows at mf, about 47 on soft strings (0.6 dB per unit near 40))
    for _t, _a, _b, _d, _k in (("Violins I", 168.0, 200.0, -8.0, 47.0), ("Flute 1", 304.0, 320.0, -7.0, 33.0),
                               ("Flute 1", 952.0, 964.0, -3.0, 33.0), ("Flute 1", 1012.0, 1016.0, -4.0, 33.0),
                               ("Horn 1", 264.0, 300.0, 4.0, 40.0)):
        _sc.setdefault(_t, []).append({"lane": "cc11", "k": _k, "pts": [(_a - 0.3, 0.0), (_a - 0.27, _d), (_b - 0.3, _d), (_b - 0.27, 0.0)]})
    for _t in ("Flute 1", "Flute 2", "Oboe 1", "Bassoon 2", "Cor anglais"):
        _sc[_t] = [dict(r_, k=r_.get("k", 33.0)) for r_ in _sc.get(_t, [])]
    INSTR_POST["cc_scale"] = _sc

    # Ruling 4: the chorale (bars 224-234) and bar 222
    # - the breaths of the whole notes are spread per player (the score prints no common breath; c17: about 15 tracks
    #   ended within 20-50 ms before each bar line): woodwinds 0.035 s and up, brass 0.045 s and up
    _C18_BREATH = {"Flute 1": 0.035, "Flute 2": 0.047, "Oboe 1": 0.050, "Oboe 2": 0.062, "Cor anglais": 0.055,
                   "Clarinet 1": 0.065, "Clarinet 2": 0.077, "Bass clarinet": 0.070, "Bassoon 1": 0.045, "Bassoon 2": 0.057,
                   "Contrabassoon": 0.050, "Horn 1": 0.065, "Horn 2": 0.055, "Horn 3": 0.075, "Horn 4": 0.060,
                   "Trumpet 1": 0.045, "Trumpet 2": 0.055, "Trumpet 3": 0.050, "Trombone 1": 0.080, "Trombone 2": 0.070,
                   "Bass trombone": 0.085, "Tuba": 0.060}
    INSTR_POST["gap_set"] = {t_: [{"from": 888.0, "to": 936.5, "min_qn": 3.0, "gap_s": g_}] for t_, g_ in _C18_BREATH.items()}
    for _k in list(_C17_GAP):
        if _k == "wind" or _k in ("Oboe 1", "Oboe 2", "Cor anglais"):
            _C17_GAP[_k] = dict(_C17_GAP[_k], skip_long=[(888.0, 936.5, 3.0)])
    # Ruling 11: the bassoons' release fills a 68 ms gap (A: 2.7-3.5 dB at 68 ms, 6.3-7.7 dB at 80-110 ms)
    for _t in ("Bassoon 1", "Bassoon 2", "Contrabassoon"):
        _C17_GAP[_t] = dict(_C17_GAP["wind"], floor_s=0.095)
    # - the pedal C ("change bow at will"): two-bar notes, the basses' bow changes one bar after the celli's
    #   (celli change at 916, 924, 932; basses at 920, 928), with the bow-change swell of c17 on each
    INSTR_POST["note_merge"] = {"Violoncellos": [920.0, 928.0], "Double basses": [916.0, 924.0, 932.0]}
    # (Movement II c57, relayed: a lift at a new bow must outlast the slow start: held 0.30 s, back over 0.55 s)
    INSTR_POST["rebow_join"] = {t_: [dict(r_, hold_s=0.30, back_s=0.55) for r_ in l_] for t_, l_ in INSTR_POST["rebow_join"].items()}
    # - bar 222 (qn 884, C #3: a 7 dB hole for 0.3 s; every part started a new slow sustain within 30 ms): the new
    #   notes lead by 0.12 s (Trumpet 1 / Horn 1 0.15 s), Violins II and Violas hold the old note 0.12 s across
    INSTR_POST["onset_lead"] = {"Violins II": [{"at": [884.0], "lead_s": 0.12}], "Violas": [{"at": [884.0], "lead_s": 0.12}],
                                "Violins I": [{"at": [884.0], "lead_s": 0.12}],
                                "Trumpet 1": [{"at": [884.0], "lead_s": 0.15}], "Horn 1": [{"at": [884.0], "lead_s": 0.15}]}
    INSTR_POST["note_end"] = dict(INSTR_POST["note_end"],
                                  **{"Violins II": [{"end": 883.8, "tol": 0.3, "early_s": -0.12, "pitch": (71, 79)}],
                                     "Violas": [{"end": 883.9, "tol": 0.3, "early_s": -0.12, "pitch": (59,)}]})
    # (range render I1: the hole fell from 4.8 to 3.7 dB; what is left is the celli's bow-change legato into D3,
    # 10.5 dB down for 0.3 s: CC11 +12 over its first 0.35 s)
    _cs.setdefault("Violoncellos", []).append({"lane": "cc11", "at": 884.0, "from_note": True,
                                               "pts": [(-0.03, 12), (0.35, 12), (0.7, 0)]})
    for _t in ("Trumpet 1", "Horn 1"):
        _cs.setdefault(_t, []).append({"lane": "cc1", "at": 884.0, "from_note": True,
                                       "pts": [(-0.06, 0), (-0.03, 10), (0.35, 10), (0.7, 0)]})
    # Ruling 10: bar 204's CC11 fall 32 -> 24 units (c17: 17.4 dB at +0.3 s, limit 17)
    for _t in ("Violoncellos", "Double basses"):
        _cs[_t] = [dict(r_, pts=[(-0.215, 0), (-0.075, -24), (0.44, -24), (0.50, 0)]) if r_.get("at") == 814.0 else r_ for r_ in _cs[_t]]
    # Ruling 12: the clarinets' dal niente entries (C #6: at full level 0.1 s after the note-on): CC11 (their volume)
    # from the floor
    for _t, _q in (("Clarinet 2", 184.0), ("Clarinet 1", 200.0), ("Clarinet 2", 680.0)):
        _cs.setdefault(_t, []).append({"lane": "cc11", "at": _q, "from_note": True, "pts": [(-0.04, -18), (0.5, -8), (1.2, 0)]})
    INSTR_POST["cc_shape"] = _cs

    # Ruling 5: pizzicato. The c17 velocity table crossed a sample layer (B #2: 8-13 dB at velocity 48-56): the table is
    # deleted, velocities stay under the layer step, and the per-pitch levels are region volumes on the Pizz rows
    # (mix.json region_gain_db, fitted on the c16 stems at flat velocity 41: cycles/c18/logs/pizz_pitch_c16.json)
    INSTR_POST.pop("vel_db", None)
    INSTR_POST["vel_cap"] = {"Violoncellos": [{"row": "Pizz", "max": 47}], "Double basses": [{"row": "Pizz", "max": 52}]}

    # Ruling 7: legato rows 3-4 dB over the sustain rows at the same pitch (A #1: Trumpet 1 +4.2, Trumpet 2 +3.3, Horn 1
    # +3.2, Oboe 2 +3.2, Oboe 1 +2.1): CC11 is the volume on brass (40 log10), split between the two rows; the c17
    # string offsets overshot on Violoncellos (legato +3.2 over sustain) and Violas (-3.7)
    _nc = {t_: list(v_) for t_, v_ in _C17_NOTE_CC.items()}
    _nc["Trumpet 1"] = _nc.get("Trumpet 1", []) + [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, -6), (114, -9)], "Sus": [(72, 0), (88, 5), (114, 8)]}}]
    _nc["Trumpet 2"] = [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, -5), (114, -7)], "Sus": [(72, 0), (88, 5), (114, 7)]}}]
    _nc["Horn 1"] = [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, -5), (114, -7)], "Sus": [(72, 0), (88, 4), (114, 6)]}}]
    _nc["Oboe 1"] = [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, -5), (114, -8)]}}]
    _nc["Oboe 2"] = [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, -8), (114, -12)]}}]
    _nc["Violoncellos"] = [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, 4), (114, 4)], "Sus MAX": [(72, 0), (88, -5), (114, -3)]}}]
    _nc["Violas"] = [{"lane": "cc11", "row_dyn": {"Leg": [(72, 0), (88, 8), (114, 16)], "Sus MAX": [(72, 0), (88, -6), (114, -6)]}}]
    # the muted Trumpet 1: G4 / A flat 4 +4 units (in place of the fader rows 688-696)
    _nc["Trumpet 1"][0] = dict(_nc["Trumpet 1"][0], pitch={**_nc["Trumpet 1"][0]["pitch"], 67: 4, 68: 4})
    # Ruling 9 (C #5): the introduction. The f figure of bars 3-4 fell 2-3 dB (CC11 75-82, c16 88) while the ff chords
    # of bars 1-2 / 5-6 rose 3-5 dB (bar 1 to bar 3 17.7 dB, c16 14.2)
    # (range render I1 with C's values, figure +7 and chords -10 / -10 / -4 / -14: the figure rose 4 dB, the chords fell
    # 7 dB on Violins I and 11 dB on Violins II (master chord -2 dB): "Sus MAX" is flat above about 103 and falls about
    # 0.7 dB per unit under 100. Rendered values: figure +5, chords -3 / -2 / -1 / -4)
    for _t, _a in (("Violins I", -3), ("Violins II", -2), ("Violas", -1), ("Violoncellos", -4)):
        _nc[_t] = _nc[_t] + [{"lane": "cc11", "from": 8.8, "to": 15.95, "add": 5},
                             {"lane": "cc11", "from": -0.1, "to": 5.1, "add": _a},
                             {"lane": "cc11", "from": 15.9, "to": 21.1, "add": _a}]
    INSTR_POST["note_cc"] = _nc

    # Ruling 8: timpani, bars 247-270 (A #6): the right-hand keys still 5 dB louder at equal velocity after -12 steps
    # (0.17 dB per step), and the second beat (left-hand low C) carried -4
    INSTR_POST["vel_pitch"] = {"Timpani": [{"row": "", "pitch": {p_: -24 for p_ in range(60, 90)}, "min": 40}]}
    TIMP_METRIC_VEL = dict(TIMP_METRIC_VEL, beat=2, off=-8)
    for _k in _C17_OFF:
        INSTR_POST.pop(_k, None)


# ---------- mvt3 c19 (2026-11-15; critics on the c18 render: cycles/c19/reports/A-C.md; coordinator's rulings 1-10) ----------
# Standing rule: no per-note fader move. Dan on c17: accents a little overdone; c18 halved them: no general raise here.
_C19 = _os15.environ.get("C19", "1") == "1"
_C19_OFF = set(_os15.environ.get("C19_OFF", "").split(","))      # parts of this block left out (range tests / fallbacks)
if _C19 and INSTR_POST:
    # Ruling 1: the chorale's bar lines (896-932). Every wind and brass whole note ended 95-155 ms before the bar line
    # and the next began 50-90 ms before it: a 35-90 ms silence on about 20 tracks inside the same 100-150 ms. Now:
    # - a join that changes pitch has no gap: the old note ends 0.04 s (woodwinds, trumpets) or 0.05 s (horns, trombones,
    #   tuba) after the new note-on (the sustain rows are polyphonic, manual p.101 / p.109; never on a legato row);
    # - a same-pitch join (an overlap would stop the new note) keeps a 0.025 s gap; the leads below differ by track, so
    #   these gaps do not coincide (Trombone 1 / Oboe 1 about 0.17 s before the bar line, Bass trombone 0.15, Tuba 0.11,
    #   Horn 2 / clarinets / bassoons 0.06);
    # - the lead of each track follows its measured rise (B's table: time to within 3 dB of the body);
    # - the printed breaths (892 brass; 900 tuba, bass trombone, bassoons; 912 bassoons; 920 upper woodwinds) keep the
    #   c18 gap, and so do the joins into 888 and 892.
    _C19_LEAD = {"Flute 1": 0.05, "Flute 2": 0.05, "Oboe 1": 0.15, "Oboe 2": 0.12, "Clarinet 1": 0.04, "Clarinet 2": 0.04,
                 "Horn 1": 0.12, "Horn 2": 0.04, "Horn 3": 0.05, "Horn 4": 0.05, "Trumpet 1": 0.06, "Trumpet 2": 0.10,
                 "Trombone 1": 0.15, "Trombone 2": 0.09, "Bass trombone": 0.13, "Tuba": 0.09}
    _C19_BREATH_AT = {"brass": [892.0], "Tuba": [892.0, 900.0], "Bass trombone": [892.0, 900.0], "Bassoon 1": [900.0, 912.0],
                      "Bassoon 2": [900.0, 912.0], "Contrabassoon": [900.0, 912.0], "wind": [920.0]}
    _C19_CH_AT = [896.0, 900.0, 904.0, 906.0, 908.0, 910.0, 912.0, 914.0, 916.0, 920.0, 924.0, 928.0, 932.0]
    if "chorale" not in _C19_OFF:
        _gs, _ol = {}, {t_: list(v_) for t_, v_ in INSTR_POST["onset_lead"].items()}
        for _t, _g in _C18_BREATH.items():
            _fam = next(f_ for n_, _s, _p, f_, _x in [t5_[:5] for t5_ in TRACKS] if n_ == _t)
            _sk = _C19_BREATH_AT.get(_t, _C19_BREATH_AT.get(_fam, []))
            _ov = -0.05 if _t.startswith(("Horn", "Trombone", "Bass trombone", "Tuba")) else -0.04
            _gs[_t] = [{"from": 888.0, "to": 894.0, "min_qn": 3.0, "gap_s": _g},
                       {"from": 894.0, "to": 936.5, "min_qn": 0.9, "gap_s": _ov, "pitch": "diff", "skip_at": _sk},
                       {"from": 894.0, "to": 936.5, "min_qn": 0.9, "gap_s": 0.025, "pitch": "same", "skip_at": _sk},
                       # a printed breath: a real gap of 0.10 s (the tool's own breath is 0.16 s there)
                       {"from": 894.0, "to": 936.5, "min_qn": 0.9, "gap_s": 0.10, "only_at": [q_ for q_ in _sk if q_ > 894.0]}]
            if _t in _C19_LEAD:
                _ol.setdefault(_t, []).append({"at": [q_ for q_ in _C19_CH_AT if q_ not in _sk], "lead_s": _C19_LEAD[_t],
                                               "set": True, "gap_s": 0.025, "rows": ("Sus",)})
        # the low strings recovered only 190-450 ms after the bar line ("Leg BC MAX" at 904-912 on the celli; the basses'
        # new "Sus MAX" bow takes 0.18 s to speak): the celli's whole notes of 900-912 on "Sus MAX" (ART_SPANS below),
        # each 0.15 s before the bar line, the basses' 0.18 s, the old note held 0.10 s past the new note-on where the
        # pitch changes; the basses' two pedal bow changes (920, 928) keep the c18 join without its CC11 lift
        _gs["Violoncellos"] = [{"from": 899.0, "to": 915.0, "min_qn": 1.9, "gap_s": -0.10, "pitch": "diff", "rows": ("Sus",)}]
        # (the celli's two whole-note C3 of 892 / 896: on "Sus MAX" the tool re-bows at 896 with a 90 ms gap)
        _gs["Violoncellos"].append({"from": 895.0, "to": 897.0, "min_qn": 1.9, "gap_s": 0.03, "pitch": "same", "rows": ("Sus",)})
        _gs["Double basses"] = [{"from": 899.0, "to": 915.0, "min_qn": 1.9, "gap_s": -0.10, "pitch": "diff", "rows": ("Sus",)},
                                {"from": 895.0, "to": 897.0, "min_qn": 1.9, "gap_s": 0.03, "pitch": "same", "rows": ("Sus",)}]
        _ol.setdefault("Violoncellos", []).append({"at": [900.0, 904.0, 908.0, 912.0], "lead_s": 0.15, "set": True, "rows": ("Sus",)})
        _ol.setdefault("Double basses", []).append({"at": [896.0, 900.0, 904.0, 908.0, 912.0, 920.0, 928.0], "lead_s": 0.18,
                                                    "set": True, "gap_s": 0.03, "rows": ("Sus",)})
        INSTR_POST["rebow_join"] = dict(INSTR_POST["rebow_join"], **{"Double basses": [
            dict(r_, swell=0) if r_.get("from") == 912.0 else r_ for r_ in INSTR_POST["rebow_join"]["Double basses"]]})
        # Violins II at 900 (C: a 12 dB hole for 370 ms: the G5 the tremolo held, re-struck on "Leg Slur MAX" with no
        # lead): a fresh "Sus MAX" stroke (DOWNBOW_STROKE_AT keeps the legato join of the next note; an ART_SPANS row
        # left the A5 of 906 on the unled first-note layer)
        DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violins II": sorted(DOWNBOW_STROKE_AT.get("Violins II", []) + [900.0])})
        ART_SPANS["Violoncellos"] = ART_SPANS.get("Violoncellos", []) + [{"from": 891.9, "to": 916.1, "art": "Sus MAX"}]
        _ol["Violoncellos"] += [{"at": [892.0], "lead_s": 0.08, "set": True, "gap_s": 0.03, "rows": ("Sus",)},
                                {"at": [916.0], "lead_s": 0.10, "set": True, "gap_s": 0.005, "rows": ("Sus",)}]
        # bar 222 (qn 884, hole 3.6 dB, target 3): the celli's bow-change legato into D3 fell 10 dB for 0.3 s: the D3 on
        # "Sus MAX", 0.15 s before the bar line, the G2 held 0.08 s past its note-on
        ART_SPANS["Violoncellos"].append({"from": 883.9, "to": 887.9, "art": "Sus MAX"})
        _ol["Violoncellos"].append({"at": [884.0], "lead_s": 0.15, "set": True, "rows": ("Sus",)})
        _gs["Violoncellos"].append({"from": 883.5, "to": 884.5, "min_qn": 0.9, "gap_s": -0.08, "pitch": "diff", "rows": ("Sus",)})
        INSTR_POST["cc_shape"] = {t_: [r_ for r_ in l_ if not (t_ == "Violoncellos" and r_.get("at") == 884.0)]
                                  for t_, l_ in INSTR_POST["cc_shape"].items()}
        INSTR_POST["gap_set"], INSTR_POST["onset_lead"] = _gs, _ol
        # (the woodwinds' tongued-join floor would undo the overlaps after the chorale's half notes)
        INSTR_POST["gap_floor"] = {k_: (dict(v_, skip_long=[(888.0, 936.5, 0.9)]) if v_.get("skip_long") else v_)
                                   for k_, v_ in INSTR_POST["gap_floor"].items()}
        # bar 224 (qn 892): the fff arrival's fader level fell 4-7 dB inside the first chorale note (Trumpet 1 +8 -> +1 dB
        # at 8.7 dB/s, Horns +3 -> -1): one step in the printed breath before the note
        INSTR_POST["vol_step_at"] = {t_: [{"at": 892.0, "win_qn": 2.0}] for t_ in ("Trumpet 1", "Horn 1", "Horn 2", "Horn 3")}

    # Ruling 2: faults made by c18
    # - Horn 3, bars 27-34: the held unison level is tagged "uni_hold" (score_to_parts.py), so c18's "uni_boost" switch
    #   matched nothing. The +3.5 dB is the a2 for the dropped Horn 4; it stood from 104.5 to 151.5 on the fader and
    #   made Horn 3 the loudest stem (-33.7 dB; basses -34.1, tuba -34.9). Now inside the patch (CC11 is the volume on
    #   brass, 40 log10) over the unison only, at +1.6 dB: about 1.5 dB under the basses
    VOL_RULE_OFF = dict(VOL_RULE_OFF, **{"Horn 3": dict(VOL_RULE_OFF.get("Horn 3", {}), uni_hold=[(103.0, 152.0)])})
    _sc = {t_: list(v_) for t_, v_ in INSTR_POST["cc_scale"].items()}
    _sc.setdefault("Horn 3", []).append({"lane": "cc11", "k": 40.0, "pts": [(103.5, 0.0), (103.55, 1.6), (135.9, 1.6), (136.0, 0.0)]})
    # - the muted Trumpet 1, bar 182: the G5 sample of "Mute Sus" is hot (region gain -4 dB, mix.json); the +4 units on
    #   G4 / A flat 4 are removed
    _nc = {t_: list(v_) for t_, v_ in INSTR_POST["note_cc"].items()}
    _nc["Trumpet 1"][0] = dict(_nc["Trumpet 1"][0], pitch={k_: v_ for k_, v_ in _nc["Trumpet 1"][0]["pitch"].items() if k_ not in (67, 68)})
    #   Against the cor anglais it doubles the trumpet read +4.0 / +5.5 / +2.0 / -0.5 dB on the four quarters of bar 182
    #   (724-727; -2.4 dB over 680-724). The region gain takes the G5; B's CC11 values for the F5 and E flat 5 (72 -> 56,
    #   67 -> 60; CC11 is the volume): a ceiling over 725-727. The CC1 ceiling stays (A)
    _cap19 = {t_: list(v_) for t_, v_ in INSTR_POST["cc_cap"].items()}
    _cap19["Trumpet 1"] = _cap19.get("Trumpet 1", []) + [{"lane": "cc11", "pts": [(724.8, 90), (724.9, 56), (725.85, 56), (725.9, 60), (726.95, 60), (727.0, 90)]}]
    INSTR_POST["cc_cap"] = _cap19
    # - the cor anglais' held notes of the muted duet swelled 5-10 dB inside the note on "Leg Slur MAX" at flat CC11
    #   (ruling: held notes on "Sus MAX"; the row is named "Sus Max" in the EH KS Master)
    #   (first build with ART_SPANS "Sus MAX", "min_qn" 1.5: nine joins of the duet lost their legato transition: the
    #   note after each held note entered "Leg Slur MAX" unled with no overlap, the class that left a 0.4 s hole at
    #   Violins II 152 in c13. So the legato row stays and the swell is taken out in CC11, B's fix: -10 units from
    #   0.35 s after the note-on to 0.3 s before the note-off. C19_CA=row builds the ruled row change for a range test)
    if _os15.environ.get("C19_CA", "cc") == "row":
        ART_SPANS["Cor anglais"] = ART_SPANS.get("Cor anglais", []) + [{"from": 680.0, "to": 744.0, "art": "Sus MAX", "min_qn": 1.5}]
    else:
        INSTR_POST["note_shape"] = {"Cor anglais": [{"lane": "cc11", "rows": ("Leg Slur",), "from": 680.0, "to": 744.0,
                                                     "min_qn": 1.5, "units": -10, "in_s": 0.35, "out_s": 0.3}]}

    # Ruling 5: accents, no general raise.
    # (a) brass: the 0.22 s bump was over before the row spoke (rise 80-135 ms; matched +0.2 to +0.5 dB): the same
    #     amounts, held 0.12 s and back by 0.30 s. No CC1 part on clarinets (their level falls as CC1 passes 105) or
    #     on horns 1 / 2 / 4; CC1 +3 on the trombones and Horn 3 (matched +0.1 to +0.5 dB at ff)
    # (b) string "Sus MAX" notes resting at CC11 82-89 (printed f, the steep part of the row: +8 units gave up to
    #     +6.5 dB): +4 units there
    # (d) a note led by more than 0.22 s: the bump's hold and end count from the score onset
    _C19_BR = {"pre_s": 0.03, "hold_s": 0.12, "end_s": 0.30, "max_step": 12}
    _acc = {}
    for _t, _l in INSTR_POST["accent"].items():
        _fam = _t if _t in ("string", "wind", "brass") else next(f_ for n_, _s, _p, f_, _x in [t5_[:5] for t5_ in TRACKS] if n_ == _t)
        _new = []
        for _r in _l:
            _r = dict(_r, lead_key_s=0.22)
            if _fam == "string":
                _r["rest_amt"] = [(80, 90, 4, ("Sus MAX",))]
            if _fam == "brass":
                if _r.get("lane") == "cc1":
                    continue
                _r.update(hold_s=_C19_BR["hold_s"], end_s=_C19_BR["end_s"])
            if _t.startswith("Clarinet") and _r.get("lane") == "cc1":
                continue
            _new.append(_r)
        _acc[_t] = _new
    for _t in ("Trombone 1", "Trombone 2", "Bass trombone", "Horn 3"):
        _base = [r_ for r_ in _acc.get(_t, _acc["brass"]) if r_.get("lane") != "cc1"]
        _acc[_t] = _base + [dict(_C19_BR, lane="cc1", amt=[(0, 3)], max=117 if _t == "Horn 3" else 112, pre_s=0.08, lead_key_s=0.22)]
    if "accent" not in _C19_OFF:
        INSTR_POST["accent"] = _acc

    # Ruling 6: the stop of bar 204 (19.2 dB at +0.3 s, limit 17): the celli and basses left 75-200 ms before the tutti
    # (C): their early end 0.075 -> 0.03 s and the CC11 fall 24 -> 12 units; a 2.5 dB return ride at 814 (mix.json)
    INSTR_POST["note_end"] = dict(INSTR_POST["note_end"], **{
        t_: [dict(r_, early_s=0.03) if r_.get("end") == 814.0 else r_ for r_ in INSTR_POST["note_end"][t_]]
        for t_ in ("Violoncellos", "Double basses")})
    _cs = {t_: list(v_) for t_, v_ in INSTR_POST["cc_shape"].items()}
    for _t in ("Violoncellos", "Double basses"):
        _cs[_t] = [dict(r_, pts=[(-0.10, 0), (-0.03, -12), (0.44, -12), (0.50, 0)]) if r_.get("at") == 814.0 else r_ for r_ in _cs[_t]]
    # Ruling 10: the clarinets' dal niente entries (5-7 dB under their level, target 8): from -24 units, held to 0.19 s
    # after the note-on (score onset + 0.15 s)
    for _t, _q in (("Clarinet 2", 184.0), ("Clarinet 1", 200.0), ("Clarinet 2", 680.0)):
        _cs[_t] = [dict(r_, pts=[(-0.04, -24), (0.19, -22), (0.6, -9), (1.3, 0)]) if (r_.get("at"), r_.get("from_note")) == (_q, True)
                   and r_["pts"][0][1] == -18 else r_ for r_ in _cs[_t]]
    INSTR_POST["cc_shape"] = _cs
    # Ruling 10: trombones 4-5 dB under the trumpets at ff in bars 199-204 (-39.0 against -34.4 to -35.6): +2 dB inside
    # the patch over 792-814 (in 273-277 they are within 2 dB already, so no ff trim)
    for _t in ("Trombone 1", "Trombone 2"):
        _sc.setdefault(_t, []).append({"lane": "cc11", "k": 40.0, "pts": [(791.4, 0.0), (791.45, 2.0), (814.3, 2.0), (814.4, 0.0)]})
    INSTR_POST["cc_scale"] = _sc
    INSTR_POST["note_cc"] = _nc

    # Ruling 7: celli pizzicato (range 7-12 dB; one key's takes differ by 5-10 dB): a round-robin reset before every
    # pluck, so a key always plays the same take, then per-pitch region volumes (mix.json; fitted on the range render)
    if "pizzrr" not in _C19_OFF:
        INSTR_POST["rr_each"] = {"Violoncellos": [{"row": "Pizz", "from": a_, "to": b_, "pre_s": 0.05, "skip_repeat": True}
                                                  for a_, b_ in ((200.0, 264.0), (456.0, 488.0), (680.0, 744.0))]}

    # Ruling 8: the basses' hammered eighths (one late pulse per quarter: on-beat bump peaks +74 ms, off-beat 0-2 dB;
    # the 80 ms note ended 30-35 ms before the stroke's own peak): 70 % of the slot, lead 0.075 s, off-beat CC11 -8
    if _os15.environ.get("C19_CB", "new") == "new":
        _C19_CB_LEN, _C19_CB_LEAD = float(_os15.environ.get("C19_CB_LEN", "0.70")), float(_os15.environ.get("C19_CB_LEAD", "0.075"))
        ART_SPANS["Double basses"] = [dict(s_, len_frac=_C19_CB_LEN) if s_.get("art") == "Stac On Bow RRx9" else s_
                                      for s_ in ART_SPANS["Double basses"]]
        INSTR_POST["row_onset"] = {"Double basses": [dict(r_, lead_s=_C19_CB_LEAD) for r_ in INSTR_POST["row_onset"]["Double basses"]]}
        _nc["Double basses"] = [dict(r_, beat=dict(r_["beat"], off=-8)) if r_.get("beat") else r_ for r_ in _nc["Double basses"]]

    # Ruling 9: bars 91-92 and 277: the unaccented eighth between two accents (79-109 ms on the sustain row, 4-7 dB
    # under its neighbours) on the double-tongue short row (manual p.109-110), velocity 95; the tuba's on its
    # "StacSs DblTng RRx9"; a round-robin reset before each bar
    if "eighth" not in _C19_OFF:
        for _t, _row in (("Trumpet 1", "Stac DblTng RRx9"), ("Trumpet 2", "Stac DblTng RRx9"), ("Trumpet 3", "Stac DblTng RRx9"),
                         ("Tuba", "StacSs DblTng RRx9")):
            ART_SPANS[_t] = ART_SPANS.get(_t, []) + [{"from": q_ - 0.1, "to": q_ + 0.1, "art": _row, "vel_by_cc": [(0, 95), (127, 95)]}
                                                     for q_ in (361.5, 365.5, 1105.5)]
            RR_RESET_AT = dict(RR_RESET_AT, **{_t: sorted(set(RR_RESET_AT.get(_t, [])) | {360.0, 1104.0})})
    for _k in _C17_OFF:
        INSTR_POST.pop(_k, None)

if _C19:
    # Ruling 3: tutti entries spread over a median 148 ms (target 36-55) because the same tracks always speak first
    # (C, half-rise on true entries): Oboe 2 -68 (0.15 s lead) / -96 (re-tongue 0.12), Flute 2 -64, Bassoon 1 -44,
    # Bassoon 2 -34, Contrabassoon -26, Trombones 1 / 2 -40 / -49, Horns 3 / 4 -59 / -49, Horn 2 -33; Tuba +25
    if "leads" not in _C19_OFF:
        ENTRY_LEAD_S = _front(ENTRY_LEAD_S, **{
            "Oboe 2": (0.0, 0.03, 0.0), "Flute 2": (0.0, 0.0, 0.0), "Bassoon 2": (0.02, 0.02), "Contrabassoon": (0.015, 0.015),
            "Trombone 1": (0.06, 0.045, 0.05), "Trombone 2": (0.06, 0.045, 0.05), "Bassoon 1": (0.02, 0.02, 0.02),
            "Horn 2": (0.04, 0.03, 0.03), "Horn 3": (0.05, 0.05), "Horn 4": (0.05, 0.05), "Tuba": (0.10, 0.07)})
        RETONGUE_LEAD_S = dict(RETONGUE_LEAD_S, **{"Oboe 2": 0.04, "Flute 2": 0.03})
        # (the notes of Trombones 1 / 2 with their own fitted leads keep them: the c15 extras of build/entry_leads.json
        # were fitted on the 0.09 s base, and six notes realised 0.15 s)
        _C19_TB_KEEP = {"Trombone 1": [413.0, 821.0, 992.5, 1000.5, 1080.5], "Trombone 2": [1080.5]}
        _C19_TB_EXTRA = 0.045
    # C #4: Violoncellos bar 142 (qn 564, pp, 5.3 qn on "Leg Slur MAX" after three staccato quarters: half a second
    # late): "Sus MAX"
    ART_SPANS["Violoncellos"] = ART_SPANS.get("Violoncellos", []) + [{"from": 563.9, "to": 569.4, "art": "Sus MAX"}]
    if INSTR_POST:
        INSTR_POST["onset_lead"] = dict(INSTR_POST.get("onset_lead", {}), **{"Violoncellos": INSTR_POST.get("onset_lead", {}).get("Violoncellos", [])
                                        + [{"at": [564.0], "lead_s": 0.12, "set": True, "rows": ("Sus",)}]})
        if "leads" not in _C19_OFF:
            for _t, _l in _C19_TB_KEEP.items():
                INSTR_POST["onset_lead"][_t] = INSTR_POST["onset_lead"].get(_t, []) + [{"at": _l, "lead_s": 0.15, "set": True}]


# ---------- mvt3 c20 (2026-11-16; critics on the c19 render: cycles/c20/reports/A-C.md; coordinator's rulings 1-9) ----------
# Standing rule (Dan): no per-note fader move. Dan 17 Nov: "overall the tracks are too soft ... instruments with
# interesting internal lines that are hidden"; shared delivery target -14 LUFS (tools/deliver_master.py, ruling 1)
_C20 = _os15.environ.get("C20", "1") == "1"
_C20_OFF = set(_os15.environ.get("C20_OFF", "").split(","))      # parts of this block left out (range tests / fallbacks)
_C20_STR = ("Violins I", "Violins II", "Violas", "Violoncellos", "Double basses")
_C20_WIND = ("Flute 1", "Flute 2", "Oboe 1", "Oboe 2", "Bassoon 1", "Bassoon 2", "Contrabassoon")
_C20_BRASS = ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trumpet 1", "Trumpet 2", "Trumpet 3", "Trombone 1", "Trombone 2",
              "Bass trombone", "Tuba", "Clarinet 1", "Clarinet 2")   # clarinets: CC1-layered, CC11 = volume, as brass
if _C20 and INSTR_POST:
    _cap20 = {t_: list(v_) for t_, v_ in INSTR_POST.get("cc_cap", {}).items()}
    _cs20 = {t_: list(v_) for t_, v_ in INSTR_POST.get("cc_shape", {}).items()}
    _sc20 = {t_: list(v_) for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _nc20 = {t_: list(v_) for t_, v_ in INSTR_POST.get("note_cc", {}).items()}
    _vs20 = {}
    # Ruling 2: the fff arrivals of bars 223 (qn 888) and 263 (qn 1048) had no step in the orchestra (B, C: strings /
    # winds' hairpin gains fell 2.5 dB during the crescendo into 223; at 263 every family fell 1.5-3.7 dB at the
    # downbeat; the CC lanes were at the top before the arrival). The crescendo stays under the ff resting values up to
    # the arrival's moved note-on (strings CC11 105, woodwinds 104, brass and clarinets CC11 100 / CC1 108), the
    # arrival steps to the fff values (strings 116 -> 118, woodwinds 113 -> 115, brass CC11 106 -> 112; brass CC1 back to
    # its lane's 120, the top layer) and holds them to the next printed dynamic (892) or rest (1052.5)
    if "climax" not in _C20_OFF:
        for _arr, _from, _end in ((888.0, 884.0, 892.0), (1048.0, 1040.0, 1052.5)):
            for _t in _C20_STR + _C20_WIND + _C20_BRASS:
                _cv = 105 if _t in _C20_STR else (104 if _t in _C20_WIND else 100)
                _cap20.setdefault(_t, []).append({"lane": "cc11", "pts": [(_from, _cv), (_arr, _cv)], "to_note": _arr})
                _cs20.setdefault(_t, []).append({"lane": "cc11", "at": _arr, "from_note": True, "hold_to": _end,
                                                 "units": 2 if _t in _C20_STR + _C20_WIND else 6})
                if _t in _C20_BRASS:
                    _cap20[_t].append({"lane": "cc1", "pts": [(_from, 108), (_arr, 108)], "to_note": _arr})
        # the hairpin gains: into 223 the bar-221 gain arrives at f (+3.0 strings / +4.0 winds at 884) and is held, not
        # raised to +5.5 / +6.5 and released during the f -> fff crescendo; the brass keep their arrival gain through
        # the fff bar (Trumpet 2 fell 5.0 -> 1.2 dB inside it); at 263 Horns 3 / 4 (+5.0 -> +2.0) and Violins II (+2.5 ->
        # +0.5) keep theirs to the rest at 1052.5
        for _t in ("Violins I", "Violas", "Violoncellos", "Double basses"):
            _vs20.setdefault(_t, []).append({"pts": [(880.0, None), (884.0, 3.0), (887.9, 3.0), (888.0, "at:888.5")]})
        _vs20.setdefault("Violins II", []).append({"pts": [(880.0, None), (884.0, 3.0), (887.5, 3.0)]})
        for _t in _C20_WIND + ("Clarinet 1", "Clarinet 2"):
            _vs20.setdefault(_t, []).append({"pts": [(880.0, None), (884.0, "at:888.5"), (888.5, "at:888.5")]})
        for _t in _C20_BRASS[:11]:
            _vs20.setdefault(_t, []).append({"pts": [(888.0, "at:888.0"), (891.7, "at:888.0")]})
        for _t in ("Horn 3", "Horn 4", "Violins II"):
            _vs20.setdefault(_t, []).append({"pts": [(1048.0, "at:1048.0"), (1052.4, "at:1048.0")]})
        # bar 150 (ff, qn 596): the sfp crescendo's gains (+2 to +5 dB) were held to 598-599; they fall to the level
        # before 592 by 599 (C asked 598; 599 keeps the fall near the 2.8 dB/s release rate inside the held notes), then
        # join the line into 600
        _b150 = {"Violoncellos": 1.5, "Horn 1": 3.0, "Horn 3": 3.0}
        for _t in _C20_STR + _C20_WIND + _C20_BRASS + ("Cor anglais", "Bass clarinet"):
            _vs20.setdefault(_t, []).append({"pts": [(596.0, None), (599.0, _b150.get(_t, 0.0)), (600.0, None)]})
    # Ruling 3: hidden inner lines (held phrase levels; inside the patch where the lane has room: cc_scale, k = dB per
    # decade of CC11: 40 exact on brass and clarinets, about 33 on the woodwind rows, about 47 on soft strings)
    if "inner" not in _C20_OFF:
        # - the clarinets' leggiero broken chords, bars 11-26 and 151-170 (C: 18.6 dB under the master, 11 under
        #   Violins I): the -2.5 dB role rows of 40-104 are deleted (roles.json, data20.py) and CC1 +6 (the layer)
        for _t in ("Clarinet 1", "Clarinet 2"):
            for _a, _b in ((40.0, 104.0), (600.0, 680.0)):
                _nc20.setdefault(_t, []).append({"lane": "cc1", "from": _a, "to": _b, "add": 6})
        # - Bassoon 1's off-beat chords in the same bars (B: 16.5 dB under the loudest stem): +3 dB
        for _a, _b in ((40.0, 104.0), (600.0, 680.0)):
            _sc20.setdefault("Bassoon 1", []).append({"lane": "cc11", "k": 33.0, "pts": [(_a - 0.3, 0.0), (_a - 0.27, 3.0), (_b - 0.3, 3.0), (_b - 0.27, 0.0)]})
        # - bars 27-34 (qn 104-136): the violins' countersubject and its flute doubling under F1 in the bass: Horns 3-4,
        #   Bass trombone and Tuba -2 dB inside the patch (CC11 = volume on brass); the flutes +3 dB (roles.json)
        for _t in ("Horn 3", "Horn 4", "Bass trombone", "Tuba"):
            _sc20.setdefault(_t, []).append({"lane": "cc11", "k": 40.0, "pts": [(103.7, 0.0), (103.73, -2.0), (135.7, -2.0), (135.73, 0.0)]})
        # - the celli and violas' counter-melody under the violins' F2, bars 67-79 (C: 5.4-6 dB under): +3 dB in CC11
        for _t in ("Violoncellos", "Violas"):
            _sc20.setdefault(_t, []).append({"lane": "cc11", "k": 47.0, "pts": [(263.7, 0.0), (263.73, 3.0), (315.7, 3.0), (315.73, 0.0)]})
        # - F1's head, bars 83-86 (qn 328-344): Clarinet 1 and Oboe 1 +3 dB, Horn 3 (the accompaniment, +1.7 dB since
        #   c19's routing) -2 dB
        for _t, _d, _k in (("Clarinet 1", 3.0, 40.0), ("Oboe 1", 3.0, 33.0), ("Horn 3", -2.0, 40.0)):
            _sc20.setdefault(_t, []).append({"lane": "cc11", "k": _k, "pts": [(327.7, 0.0), (327.73, _d), (343.7, _d), (343.73, 0.0)]})
        # - the f counter-line of bars 212-215 (qn 844-857: celli, Bassoon 1, Horns 3-4; 10-15 dB under the trumpets'
        #   theme B): Horns 3-4 CC1 +6 (B: 0.21 dB per unit on "Sus MAX", so also a role row); celli / Bassoon 1 and
        #   the Violins II rows in roles.json
        for _t in ("Horn 3", "Horn 4"):
            _nc20.setdefault(_t, []).append({"lane": "cc1", "from": 843.9, "to": 857.0, "add": 6})
    # Ruling 9: trombones 4 dB under the trumpets at ff in bars 199-204: CC1 +6 for the phrase (manual p.101)
    if "small" not in _C20_OFF:
        for _t in ("Trombone 1", "Trombone 2"):
            _nc20.setdefault(_t, []).append({"lane": "cc1", "from": 791.9, "to": 816.0, "add": 6})
        # celli accents +5.5 dB median (A): amounts halved
        INSTR_POST["accent"] = dict(INSTR_POST["accent"], Violoncellos=[
            dict(r_, amt=[(46, 2), (72, 3), (88, 4), (114, 5)], rest_amt=[(80, 90, 2, ("Sus MAX",))])
            for r_ in INSTR_POST["accent"].get("Violoncellos", INSTR_POST["accent"]["string"])])
        # bar 91: the master's (and the delivery limiter's) third-highest peak is one Bass trombone E flat 2 crest
        # (stem -9.2 dBFS, 9 dB over every other stem): CC11 -15 units (about -2.5 dB) on the two accented halves
        _nc20.setdefault("Bass trombone", []).append({"lane": "cc11", "from": 359.9, "to": 360.1, "add": -15})
        _nc20.setdefault("Bass trombone", []).append({"lane": "cc11", "from": 363.9, "to": 364.1, "add": -15})
        # entries (A): Horn 4 +50 ms and Horn 2 +32 ms late in the tutti chords
        ENTRY_LEAD_S = _front(ENTRY_LEAD_S, **{"Horn 4": (0.095, 0.095), "Horn 2": (0.07, 0.06, 0.06)})
        # bar 246 (qn 980-983): the printed tenuto quarters of the celli / basses ran together (0.31-0.38 s notes in a
        # 0.36 s slot): forced new-bow gaps (Dan's rule min(0.06 s, 25 %))
        STR_REP_NEW_BOW["plain"]["force"] = dict(STR_REP_NEW_BOW["plain"]["force"], **{
            "Violoncellos": sorted(set(STR_REP_NEW_BOW["plain"]["force"].get("Violoncellos", [])) | {981.0, 982.0, 983.0}),
            "Double basses": sorted(set(STR_REP_NEW_BOW["plain"]["force"].get("Double basses", [])) | {981.0, 982.0, 983.0})})
        # crash rise -3 dB point +30..+36 ms after the beat (bass drum +6..+8): lead 0.02 -> 0.04 s
        PERC_MAP["Crash cymbals"]["crashcymbal"]["lead_s"] = 0.04
    # Ruling 2: the crash and bass drum of the final chord are the master's sample peaks (B: limiter 4.3-4.8 dB, all on
    # the final chord): velocity -2
    if "climax" not in _C20_OFF:
        PERC_VEL_ADD = {"Crash cymbals": [(1107.0, 1116.0, -2)], "Bass drum": [(1107.0, 1116.0, -2)]}
    # Ruling 5 (A #1): the basses' hammered eighths ("Stac On Bow RRx9": a hidden release-extension group and 749 ms
    # releases, mix.json): 60 % of the slot, lead 0.10 s
    if "cb" not in _C20_OFF:
        ART_SPANS["Double basses"] = [dict(s_, len_frac=0.60) if s_.get("art") == "Stac On Bow RRx9" else s_
                                      for s_ in ART_SPANS["Double basses"]]
        INSTR_POST["row_onset"] = {"Double basses": [dict(r_, lead_s=0.10) for r_ in INSTR_POST["row_onset"]["Double basses"]]}
    INSTR_POST["cc_cap"], INSTR_POST["cc_shape"], INSTR_POST["cc_scale"], INSTR_POST["note_cc"] = _cap20, _cs20, _sc20, _nc20
    INSTR_POST["vol_set"] = _vs20
if _C20:
    # Ruling 2: delivery-side phrase levels (deliver_master.py reads parts.json "ride_trims"): the short ff stabs of bars
    # 1-2, 5-6, 94, 113, 131-132 kept their peaks under the top ride while it pressed the long fff passages (C); the
    # chorale's printed diminuendo (bars 229-233) shrank 3.4 -> 1.4 dB under the new delivery
    if "climax" not in _C20_OFF:
        RIDE_TRIMS = RIDE_TRIMS + [
            [(0.0, -2.5), (8.0, -2.5), (8.25, 0.0)], [(15.75, 0.0), (16.0, -2.5), (24.0, -2.5), (24.25, 0.0)],
            [(371.75, 0.0), (372.0, -2.0), (376.0, -2.0), (376.25, 0.0)], [(447.75, 0.0), (448.0, -2.0), (452.0, -2.0), (452.25, 0.0)],
            [(519.75, 0.0), (520.0, -2.0), (528.0, -2.0), (528.25, 0.0)],
            [(912.0, 0.0), (932.0, -2.0), (936.0, 0.0)]]

# ---------- mvt3 c21 (2026-11-17; critics on the c20 render: cycles/c21/reports/A-C.md; coordinator's rulings 1-10) ----------
# Standing rule (Dan): no per-note fader move; every fix on the instrument side, a held phrase level or a delivery ride.
_C21 = _os15.environ.get("C21", "1") == "1"
_C21_OFF = set(_os15.environ.get("C21_OFF", "").split(","))      # parts left out (range tests / fallbacks)
if _C21:
    # Ruling 1 (B #1, variant w11): delivery rides. The final row (+2.5 / +2.0 / +1.0 dB over 1087-1113.5) becomes -2.5 on
    # the final chord; -3 / -4.5 dB at bars 222-223; -1.5 / -2 at bar 263; -3 / -2 / -1.5 dB on the ff stabs (added to
    # the c20 rows). Simulated on the c20 master with mix.json deliver.ratio 1.8 and the loudness loop: -14.0 LUFS, LRA
    # 11.5, TP -1.0, p10 -22.3, limiter 5.8 / 3.3 / 2.9 dB at final / 223 / 263, order final -7.2 > 223 -7.6 > 263 -8.2 >
    # ff -9.1 (cycles/c21/logs/deliv_c20_redelivered.log)
    if "rides" not in _C21_OFF:
        RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if r_[0][0] != 1087.0] + [
            # after the c21 render (limiter 6.7 dB on the final chord, final level with 223): final -2.5 -> -3.5, bar 223
            # -4.5 -> -5.5 (simulated on the c21 master: limiter 5.7 / 4.2 / 3.8 dB, order final -7.6 > 223 -7.8 > 263 -7.9)
            [(1087.0, 0.0), (1088.0, 0.0), (1104.0, 0.0), (1107.9, -3.5), (1108.0, -3.5), (1113.0, -3.5), (1113.5, 0.0)],
            [(883.5, 0.0), (884.0, -3.0), (887.9, -3.0), (888.0, -5.5), (891.5, -5.5), (892.0, 0.0)],
            [(1045.5, 0.0), (1046.0, -1.5), (1051.5, -1.5), (1052.0, 0.0)],
            [(1043.5, 0.0), (1044.0, -2.0), (1046.0, -2.0), (1046.5, 0.0)]]
        for _a, _b, _d in ((360.0, 376.0, -3.0), (436.0, 452.0, -3.0), (1052.0, 1056.0, -3.0), (660.0, 664.0, -3.0),
                           (848.0, 852.0, -3.0), (524.0, 528.0, -2.0), (596.0, 600.0, -2.0), (16.0, 24.0, -1.5)):
            RIDE_TRIMS.append([(_a - 0.5, 0.0), (_a, _d), (_b, _d), (_b + 0.5, 0.0)])
        RIDE_TRIMS.append([(0.0, -1.5), (8.0, -1.5), (8.25, 0.0)])
if _C21 and INSTR_POST:
    _sc21 = {t_: list(v_) for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _nc21 = {t_: list(v_) for t_, v_ in INSTR_POST.get("note_cc", {}).items()}
    # Ruling 3 (A #1, B #4): the basses' eighths in the accelerando 816-840 (strokes about 0.10 s, stroke peaks -9.3 dB
    # under c19; the region gain +4 dB in mix.json gives the rest of the spans): CC11 +5 dB there (k 47, soft strings)
    if "cb" not in _C21_OFF:
        _sc21.setdefault("Double basses", []).append({"lane": "cc11", "k": 47.0, "pts": [(815.7, 0.0), (815.73, 5.0), (839.7, 5.0), (839.73, 0.0)]})
    if "inner" not in _C21_OFF:
        # Ruling 4: inner lines in CC11 (CC1 lifts sat on layer plateaus: clarinets mp layer 0.77 -> 0.98 over CC1 52-76;
        # horns f + ff 1.29 -> 1.26 over CC1 86-92)
        # - clarinets 151-170 (qn 600-680): CC1 +6 out, CC11 +3 dB (k 40: CC11 is the volume on the CL KS Master)
        for _t in ("Clarinet 1", "Clarinet 2"):
            _nc21[_t] = [r_ for r_ in _nc21.get(_t, []) if not (r_.get("lane") == "cc1" and r_.get("from") == 600.0 and r_.get("add") == 6)]
            _sc21.setdefault(_t, []).append({"lane": "cc11", "k": 40.0, "pts": [(599.7, 0.0), (599.73, 3.0), (679.7, 3.0), (679.73, 0.0)]})
        # - Oboe 1 +2 dB more at F1's head 328-344 (B: -5.0 dB under Violins I, target within 3)
        _sc21.setdefault("Oboe 1", []).append({"lane": "cc11", "k": 33.0, "pts": [(327.7, 0.0), (327.73, 2.0), (343.7, 2.0), (343.73, 0.0)]})
        # - counter-line 212-215: Horns 3-4 CC1 +6 out, CC11 +3 dB
        for _t in ("Horn 3", "Horn 4"):
            _nc21[_t] = [r_ for r_ in _nc21.get(_t, []) if not (r_.get("lane") == "cc1" and r_.get("from") == 843.9)]
            _sc21.setdefault(_t, []).append({"lane": "cc11", "k": 40.0, "pts": [(843.6, 0.0), (843.63, 3.0), (856.7, 3.0), (856.73, 0.0)]})
        # - trombones 199-204 (2.3-3.3 dB under the trumpets): CC11 +1.5 dB on top of c20's CC1 +6
        for _t in ("Trombone 1", "Trombone 2"):
            _sc21.setdefault(_t, []).append({"lane": "cc11", "k": 40.0, "pts": [(791.6, 0.0), (791.63, 1.5), (815.7, 1.5), (815.73, 0.0)]})
        # - the trumpets' mf staccato off-beats of bars 159-166 (qn 633-662), 22 dB under Violins I: velocity 88 -> 96
        #   (the park below takes CC11 out of their dynamic)
        INSTR_POST["vel_add"] = dict(INSTR_POST.get("vel_add") or {})
        for _t in ("Trumpet 1", "Trumpet 2", "Trumpet 3"):
            INSTR_POST["vel_add"][_t] = list(INSTR_POST["vel_add"].get(_t, [])) + [{"from": 632.9, "to": 662.5, "add": 8, "row": "Stac"}]
    # Ruling 4 (B #3): brass short rows park CC11 at the ff resting value 100 and CC1 at 85 or more; velocity carries the
    # printed dynamic (manual p.53 / p.64). Not on string pizzicato (its per-key table was fitted at CC11 34)
    if "park" not in _C21_OFF:
        INSTR_POST["short_cc_park"] = {t_: [{"rows": ["Stac", "StacSs", "Marc Shrt"], "cc11": 100, "cc1_min": 85, "pre_s": 0.05}]
                                       for t_ in _os15.environ.get("C21_PARK", "Trumpet 1,Trumpet 2,Trumpet 3").split(",") if t_}
    # Ruling 1: the one real single-track crest left at the climaxes: Trombone 1's accented halves at bar 277 (C #3:
    # 0.70 dB of peak for 0.44 LU; limiter 4.0 dB there): CC11 -10 units
    if "small" not in _C21_OFF:
        _nc21.setdefault("Trombone 1", []).append({"lane": "cc11", "from": 1103.9, "to": 1106.1, "add": -10})
    INSTR_POST["cc_scale"], INSTR_POST["note_cc"] = _sc21, _nc21
    # Ruling 9 (A, B, C): the cor anglais' bar-150 vol_set row ended at 600 and its own hairpin release came back there
    # (0 at 599, +1.73 at 600, falling to 0 by 601.75 inside the note 600-602: -1.5 dB over 0.5 s). Dropping the row
    # left the release running from 598 through the note (measured in parts.json): the row now holds 0 from 599 to the
    # end of that release (601.8), so nothing moves inside the note
    if "small" not in _C21_OFF:
        INSTR_POST["vol_set"] = dict(INSTR_POST.get("vol_set") or {})
        INSTR_POST["vol_set"]["Cor anglais"] = [r_ for r_ in INSTR_POST["vol_set"].get("Cor anglais", []) if r_["pts"][0][0] != 596.0] + [
            {"pts": [(596.0, None), (599.0, 0.0), (601.8, 0.0), (601.85, None)]}]
    # Ruling 6 (A #2): the cor anglais' legato-target bloom is the patch (TLeg about 5 dB under a 465 ms sustain fade-in):
    # variant A = mix.json region gain TLeg +4 dB, c19's -10 unit note_shape deleted. C21_CA=sus: C's variant ("Sus Max"
    # over the unison spans 680-696 and 712-731) for the range test
    if "ca" not in _C21_OFF:
        INSTR_POST["note_shape"] = {k_: v_ for k_, v_ in (INSTR_POST.get("note_shape") or {}).items() if k_ != "Cor anglais"}
        if _os15.environ.get("C21_CA", "sus") == "sus":   # range test R1 / R2: C is flatter (see CHANGES)
            ART_SPANS["Cor anglais"] = ART_SPANS.get("Cor anglais", []) + [{"from": 679.9, "to": 696.0, "art": "Sus MAX"},
                                                                           {"from": 711.9, "to": 731.0, "art": "Sus MAX"}]
if _C21:
    # Ruling 8 (A #5): the celli's re-bowed same-pitch repeats (median dip 2.2 dB, 15 of 26 under 3): the "stroke" and
    # "sus_min_s" new bows take the portato class's CC11 fall
    if "rebow" not in _C21_OFF:
        STR_REP_NEW_BOW["stroke_fall"] = {"fall_cc": 10, "fall_cc_loud": 12, "fall_s": 0.06}
    # Ruling 7 (A #4): the harp's printed harmonics (qn 168 / 176 / 184) and the bar-277 glissando on the Harp KS Master's
    # "Harmonics" and "Gliss Technique" rows (manual p.70); the rest on "Sus RR". The KS Master's triggers sit on keys
    # 21-35, inside the harp's range: mix.json "ks_keys" moves Harmonics / Gliss Technique to 112 / 113 and
    # "ks_unused_off" takes the key off the other triggers (build/ks_maps_extra.json has the same keys)
    if "harp" not in _C21_OFF:
        TRACKS = [(t_[0], t_[1], H + "04 Keyswitch/Harp KS Master.oib") + tuple(t_[3:]) if t_[0] == "Harp" else t_ for t_ in TRACKS]
        ART_SPANS["Harp"] = [{"from": 167.9, "to": 191.0, "art": "Harmonics"}, {"from": 1105.9, "to": 1107.9, "art": "Gliss Technique"},
                             {"from": -10.0, "to": SCORE_END + 10.0, "art": "Sus RR"}]

# ---------- mvt3 c22 (2026-11-17; critics on the c21 render: cycles/c22/reports/A-C.md; coordinator's rulings 1-8) ----------
# Standing rule (Dan): no per-note fader move; every fix on the instrument side, a held phrase level or a delivery ride.
_C22 = _os15.environ.get("C22", "1") == "1"
_C22_OFF = set(_os15.environ.get("C22_OFF", "").split(","))      # parts left out (range tests / fallbacks)
if _C22:
    if "rides" not in _C22_OFF:
        # Ruling 2 (C #1c): the crescendo into bar 263 kept +0.5 dB on the mp3: the 1043.5-1046.5 -2 dB row is deleted and
        # the 1045.5 row starts at the arrival. C #3d: the final row steps at the downbeat (it ramped -3.5 dB across the
        # crescendo of bar 277). Ruling 3 (C #2): the -1.5 dB rows on bars 1-2 / 5-6 (the ff no louder than bar 10's
        # crescendo on the mp3) and the 519.75 row (bar 131's f arrival under its crescendo) are deleted; bars 9-11 -2 dB
        # evenly. B #2: ff bars at the fff level: -2.5 dB at 1080-1088, -1.5 at 584-596 and 792-840 (simulated by B and C on
        # the c21 master: every ff bar 1.5 dB or more under fff but 277; final / 223 / 263 within 0.1 dB of c21)
        _drop22 = {((0.0, -1.5), (8.0, -1.5)), ((15.5, 0.0), (16.0, -1.5)), ((519.75, 0.0), (520.0, -2.0)),
                   ((1043.5, 0.0), (1044.0, -2.0)), ((1045.5, 0.0), (1046.0, -1.5)), ((1087.0, 0.0), (1088.0, 0.0))}
        RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if (tuple(r_[0]), tuple(r_[1])) not in _drop22] + [
            [(1047.8, 0.0), (1047.95, -1.5), (1051.5, -1.5), (1052.0, 0.0)],
            # after the c22 render (limiter 6.4 dB on the final chord; mp3 1040-1047 only +0.7 over 1032-1039, 263 over 262
            # +0.4): the final row -3.5 -> -4.0, and the crescendo's earlier bars ridden down (-1.5 at 1032 easing to 0 at
            # the arrival): simulated on the c22 master: limiter 6.0, rise +1.5, 263 over 262 +0.5 (cycles/c22/CHANGES.md)
            [(1087.0, 0.0), (1104.0, 0.0), (1107.8, -1.0), (1107.95, -4.0), (1113.0, -4.0), (1113.5, 0.0)],
            [(1031.5, 0.0), (1032.0, -1.5), (1040.0, -1.0), (1046.0, -0.5), (1047.8, 0.0)],
            [(31.5, 0.0), (32.0, -2.0), (44.0, -2.0), (48.0, 0.0)]]
        for _a, _b, _d in ((1080.0, 1088.0, -2.5), (584.0, 596.0, -1.5), (792.0, 840.0, -1.5)):
            RIDE_TRIMS.append([(_a - 0.5, 0.0), (_a, _d), (_b, _d), (_b + 0.5, 0.0)])
    if "final" not in _C22_OFF:
        # Ruling 2 (C #3a): the three-bar crescendo into the final fff (1096-1108): brass hairpin gain 2 -> 4 dB, woodwinds
        # 4 -> 5 dB (a printed hairpin as a dB ramp; the brass already sit in their top layer there)
        HP_GAIN_AT_DB = {1096.0: {"brass": 4.0, "wind": 5.0}}
    # Ruling 4 (A #1): the trumpets take the horns' re-tongue (gap 0.1 s, fall 12); with the f / ff release 240 ms (mix.json)
    if "tpt" not in _C22_OFF:
        WIND_REP_RETONGUE_BY = _front(WIND_REP_RETONGUE_BY, Trumpet={"gap_s": 0.1, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15})
    # Ruling 6 (A #3a): wind legato velocity floor (manual p.144: 110-127 plays the shorter transition), as the strings' and
    # brass'; 46 % of the wind legato targets at velocity 71-90 had a 6 dB hole between transition and sustain
    # Range test R1 / R2 (cycles/c22/CHANGES.md): the floor changed nothing (6 dB holes on Flute 1 / Flute 2 / Oboe 1 /
    # Clarinet 1 3 / 4 / 6 / 4 in c21 -> 3 / 4 / 7 / 5), so it is off; C22_WFLOOR=1 turns it on
    if _os15.environ.get("C22_WFLOOR") == "1":
        LEG_VEL_STRONG = dict(LEG_VEL_STRONG, wind=[(52, 96), (65, 100), (80, 104), (100, 110), (127, 116)])
    # Ruling 8 (A #6): the basses' accelerando eighths 816-840 0.30 -> 0.33 qn (0.66 of the eighth slot)
    if "cb" not in _C22_OFF:
        _cb22 = []
        for s_ in ART_SPANS["Double basses"]:
            if s_.get("art") == "Stac On Bow RRx9" and s_.get("from") == 792.0 and s_.get("to") == 840.0:
                _cb22 += [dict(s_, to=816.0), dict(s_, **{"from": 816.0, "len_frac": 0.66})]
            else:
                _cb22.append(s_)
        ART_SPANS["Double basses"] = _cb22
    # Ruling 6 (A #3, scherzo c19): Horn 1's legato holes at +0.3 s (90, 286, 868): those targets on "Sus MAX" without an
    # overlap (gap_set below), lead 0.06 s
    if "hn1" not in _C22_OFF:
        ART_SPANS["Horn 1"] = ART_SPANS.get("Horn 1", []) + [{"from": x_ - 0.1, "to": x_ + 0.1, "art": "Sus MAX"} for x_ in (90.0, 286.0, 868.0)]
if _C22 and INSTR_POST:
    _sc22 = {t_: list(v_) for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _cap22 = {t_: list(v_) for t_, v_ in INSTR_POST.get("cc_cap", {}).items()}
    _gs22 = {t_: list(v_) for t_, v_ in INSTR_POST.get("gap_set", {}).items()}
    _ol22 = {t_: list(v_) for t_, v_ in INSTR_POST.get("onset_lead", {}).items()}
    _vs22 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("vol_set") or {}).items()}
    if "climax" not in _C22_OFF:
        # Ruling 2 (C #1a): the caps of the 1048 arrival become ramps (each line keeps 3-6 units of step at the arrival);
        # the 888 caps stay
        for _t, _v in _cap22.items():
            _new = []
            for r_ in _v:
                if r_.get("to_note") == 1048.0:
                    if r_["lane"] == "cc1":
                        r_ = dict(r_, pts=[(1040.0, 108), (1047.9, 116)])
                    elif _t in _C20_STR:
                        r_ = dict(r_, pts=[(1040.0, 108), (1047.9, 112)])
                    elif _t in _C20_WIND:
                        r_ = dict(r_, pts=[(1040.0, 107), (1047.9, 110)])
                    else:
                        r_ = dict(r_, pts=[(1040.0, 102), (1047.9, 106)])
                _new.append(r_)
            _cap22[_t] = _new
        # C #1b: the brass hairpin gain of the 1024-1032 crescendo was released (2 dB over 1034-1038) before the
        # 1040-1048 crescendo began: held from 1032 to the arrival at its 1032 value (equal to the arrival value)
        for _t, _s in (("Horn 1", 1036.0), ("Horn 2", 1036.0), ("Trombone 1", 1036.0), ("Trombone 2", 1036.0), ("Trumpet 3", 1034.0)):
            _vs22.setdefault(_t, []).append({"pts": [(_s, None), (1048.0, "at:" + str(_s))]})
    if "final" not in _C22_OFF:
        # C #3b: Horn 1's -3.5 dB role row from 1104 (a fader step inside the note of 1104, in the crescendo) is deleted
        # (roles.json); the same -3.5 dB goes into CC11 (the volume on the horn KS Master, k 40) from the rest before the
        # final chord (1106.9-1107.84)
        _sc22.setdefault("Horn 1", []).append({"lane": "cc11", "k": 40.0, "pts": [(1107.0, 0.0), (1107.4, -3.5), (1116.5, -3.5), (1116.53, 0.0)]})
    if "chorale" not in _C22_OFF:
        # Ruling 5 (A #2): the chorale's same-pitch repeats (onset_lead "set" rows of c19): the re-tongue fall moves with the
        # moved note-on (back 0.01 qn before it), 18 units deep on horns, trombones, bass trombone and tuba
        for _t in list(_ol22):
            _ol22[_t] = [dict(r_, move_fall=True, **({"fall_cc": 18} if _t.startswith(("Horn", "Trombone", "Bass trombone", "Tuba")) else {}))
                         if (r_.get("set") and r_.get("gap_s") == 0.025 and 896.0 in r_.get("at", [])) else r_ for r_ in _ol22[_t]]
    if "hn1" not in _C22_OFF:
        _ol22["Horn 1"] = _ol22.get("Horn 1", []) + [{"at": [90.0, 286.0, 868.0], "lead_s": 0.06, "set": True, "rows": ("Sus",)}]
        _gs22["Horn 1"] = _gs22.get("Horn 1", []) + [{"from": 85.0, "to": 870.0, "min_qn": 0.5, "gap_s": 0.0, "rows": ("Sus", "Leg"),
                                                      "only_at": [90.0, 286.0, 868.0]}]
    if "wleg" not in _C22_OFF:
        # A #3: Flute 2's 0.17-0.20 s legato overlaps (602, 634, 842, 1074; 9.5-13.8 dB holes) capped at the wind floor
        _gs22["Flute 2"] = _gs22.get("Flute 2", []) + [{"from": 600.0, "to": 1076.0, "min_qn": 0.5, "gap_s": -0.035, "rows": ("Sus", "Leg"),
                                                        "allow_leg": True, "only_at": [602.0, 634.0, 842.0, 1074.0]}]
    if "bal" not in _C22_OFF:
        # Ruling 7 (B #3): muted Trumpet 1 2.8 dB under the cor anglais in their unison (679.7-731): CC11 +2.5 dB (k 40)
        _sc22.setdefault("Trumpet 1", []).append({"lane": "cc11", "k": 40.0, "pts": [(679.7, 0.0), (679.73, 2.5), (731.0, 2.5), (731.03, 0.0)]})
        # B #4: the violas' and celli's mp counter-lines over the violins' mf tune (bars 73-74, 76, 79): CC11 -3 dB (k 47)
        for _t, _sp in (("Violas", ((287.7, 296.3), (299.7, 304.3))), ("Violoncellos", ((299.7, 304.3), (311.7, 316.3)))):
            for _a, _b in _sp:
                _sc22.setdefault(_t, []).append({"lane": "cc11", "k": 47.0, "pts": [(_a, 0.0), (_a + 0.03, -3.0), (_b, -3.0), (_b + 0.03, 0.0)]})
        # B #6: the trumpets' mf off-beats 159-166 level with Horn 3's f: Trumpets 1-2 velocity +8 -> +4
        INSTR_POST["vel_add"] = dict(INSTR_POST.get("vel_add") or {})
        for _t in ("Trumpet 1", "Trumpet 2"):
            INSTR_POST["vel_add"][_t] = [dict(r_, add=4) if r_.get("from") == 632.9 else r_ for r_ in INSTR_POST["vel_add"].get(_t, [])]
        # C #4: Horn 4's pp held A flat 3 (bars 43-47) dips 4.5 / 7.6 dB about 2.9 s apart (a looped sustain): CC11 fill
        # (C's points from the c21 stem)
        _sc22.setdefault("Horn 4", []).append({"lane": "cc11", "k": 40.0, "pts": [(171.4, 0), (172.5, 3.0), (173.1, 4.5), (173.8, 3.0), (174.6, 0),
                                                                                  (179.8, 0), (180.8, 5.0), (181.5, 7.0), (182.1, 5.0), (182.9, 0)]})
    if "acc" not in _C22_OFF:
        # Ruling 8 (A #5): Trumpet 3's accented half notes 1024-1044 1.2 dB under its plain notes: the trombones' accent
        # (CC11 0.10 x rest, CC1 +3) over 1016-1048
        _acc22 = dict(INSTR_POST["accent"])
        _t3 = _acc22.get("Trumpet 3", _acc22["brass"])
        _tb = _acc22.get("Trombone 1", _acc22["brass"])
        _acc22["Trumpet 3"] = [dict(r_, to=1016.0) for r_ in _t3] + [dict(r_, **{"from": 1048.0}) for r_ in _t3] + \
                              [dict(r_, **{"from": 1016.0, "to": 1048.0}) for r_ in _tb]
        INSTR_POST["accent"] = _acc22
    if "mono" not in _C22_OFF:
        # Ruling 2 (C #3c): inside a printed crescendo a note's resting level does not fall under the note before
        # (PHRASE_SHAPE and the per-note contours already skip hairpins; this catches row offsets and note_cc falls)
        INSTR_POST["cresc_mono"] = {"string": {"lanes": ("cc11",), "tol": 1.0}, "wind": {"lanes": ("cc11",), "tol": 1.0},
                                    "brass": {"lanes": ("cc11", "cc1"), "tol": 1.0},
                                    # (not on Trombone 1's accented halves of bar 277: c21's -10 unit crest cut, limiter)
                                    "Trombone 1": {"lanes": ("cc11", "cc1"), "tol": 1.0, "skip": [(1103.5, 1106.5)]}}
    INSTR_POST["cc_scale"], INSTR_POST["cc_cap"], INSTR_POST["gap_set"] = _sc22, _cap22, _gs22
    INSTR_POST["onset_lead"], INSTR_POST["vol_set"] = _ol22, _vs22

# ---------- mvt3 c23 (2026-11-17; critics on the c22 render: cycles/c23/reports/A-C.md; coordinator's rulings 1-8) ----------
# Standing rule (Dan): no per-note fader move; every fix on the instrument side, a held phrase level or a delivery ride.
_C23 = _os15.environ.get("C23", "1") == "1"
_C23_OFF = set(_os15.environ.get("C23_OFF", "").split(","))      # parts left out (range tests / fallbacks)
if _C23:
    if "arr" not in _C23_OFF:
        # Ruling 1 (C #1): air before the fff arrivals: a caesura on the last beat before 888 (the allargando's 112 -> about
        # 106) and before 1048 (176, about 7 % on the last half-note beat); bar 223 starts at 112 without the arc's push
        CAESURA = {**CAESURA, 888.0: 0.06, 1048.0: 0.05}
        PHRASE_ARCS = [((892, 912) + tuple(a_[2:]) if (a_[0], a_[1]) == (888, 912) else a_) for a_ in PHRASE_ARCS]
    if "cb" not in _C23_OFF:
        # Ruling 6 (A #5): the basses' accelerando eighths 816-840 released before their own peak: 0.33 -> 0.37 qn
        ART_SPANS["Double basses"] = [dict(s_, len_frac=0.74) if (s_.get("art") == "Stac On Bow RRx9" and s_.get("from") == 816.0) else s_
                                      for s_ in ART_SPANS["Double basses"]]
    if "rides" not in _C23_OFF:
        # Ruling 1 (B #1, V12, then milder): delivery rows before each fff arrival (simulated on the c22 master with
        # deliver_master.py; in-bar momentary maxima on the mp3): bar 223 over 222 +1.7 -> +3.4 dB (220 < 221 < 222 < 223
        # kept), 263 over 262 +0.5 -> +1.2, final over 277 +0.6 -> +1.4, bars 273-277 rising, 131 over 130; limiter 6.0 ->
        # 6.3 dB on the final chord. Refitted on the c23 master after the render (cycles/c23/CHANGES.md)
        _rp23 = {(883.5, 0.0): [(879.5, 0.0), (880.0, -3.5), (884.0, -5.0), (887.9, -5.0), (888.0, -4.5), (891.5, -4.5), (892.0, 0.0)],
                 (1031.5, 0.0): [(1023.5, 0.0), (1024.0, -2.5), (1032.0, -3.5), (1040.0, -3.0), (1046.0, -2.5), (1047.8, -2.5), (1047.95, 0.0)],
                 (1079.5, 0.0): [(1079.5, 0.0), (1080.0, -3.5), (1088.0, -3.5), (1092.0, -2.5), (1096.0, -2.0), (1104.0, -3.0), (1107.8, -3.5), (1107.95, 0.0)]}
        # after the c23 render (re-delivered on its master): the final row's arrival -4.0 -> -4.5 and bar 223's -4.5 -> -5.0
        # (limiter 6.4 -> 5.9 dB, final and 223 tie at -7.5); the final row holds -8 dB over the chord's tail from 1113.3
        # (the mp3's final-chord drop at +0.3 s was 7.8 dB against 16.1 on the master: the lift raised the hall tail;
        # now 15.6 dB; the scherzo c21 note)
        _rp23[(883.5, 0.0)] = [(q_, (-5.0 if q_ in (888.0, 891.5) else d_)) for q_, d_ in _rp23[(883.5, 0.0)]]
        _rp23[(1087.0, 0.0)] = [(1087.0, 0.0), (1104.0, 0.0), (1107.8, -1.0), (1107.95, -4.5), (1113.0, -4.5), (1113.3, -8.0),
                                (1120.0, -8.0), (1120.5, 0.0)]
        RIDE_TRIMS = [_rp23.get(tuple(r_[0]), r_) for r_ in RIDE_TRIMS] + [[(511.5, 0.0), (512.0, -1.5), (519.5, -1.5), (520.0, 0.0)]]
    # Ruling 5 (c): the early wind legato holes (0.1-0.25 s after the note-on; 200 ms window): those targets on the
    # sustain row 0.06 s early, no overlap (Horn 1's c22 fix)
    _C23_SUS = {"Oboe 1": ("Sus MAX", (384.0, 964.0, 1014.0)), "Cor anglais": ("Sus MAX", (708.0, 738.0)),
                "Clarinet 1": ("Sus Non Vib", (606.0, 998.0, 1014.0))}
    if "wsus" not in _C23_OFF:
        for _t, (_row, _at) in _C23_SUS.items():
            ART_SPANS[_t] = ART_SPANS.get(_t, []) + [{"from": x_ - 0.1, "to": x_ + 0.1, "art": _row} for x_ in _at]
    # Ruling 7 (C #5): the opening chord: Horn 1 (+129 ms) and Tuba (+77 ms) entered late (no lead before qn 0.5 for
    # brass unless listed in entry_leads.json: the extras are there)
    # Ruling 4 (B #2): the Violins II role step at 899.9 crosses over in the rest between the tremolo's end (899.847) and
    # the moved note-on of 900 (899.867)
    ROLE_EDGE_XF = {"Violins II": {899.9: (899.848, 899.866)}}
if _C23 and INSTR_POST:
    _sc23 = {t_: list(v_) for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _gs23 = {t_: list(v_) for t_, v_ in INSTR_POST.get("gap_set", {}).items()}
    _ol23 = {t_: list(v_) for t_, v_ in INSTR_POST.get("onset_lead", {}).items()}
    _ne23 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_end") or {}).items()}
    if "arr" not in _C23_OFF:
        # Ruling 1 (C #1.2): a 0.06 s lift before 1048 on the strings (Violins I overlapped the arrival by 34 ms): the note
        # sounding into the arrival ends 0.06 s before the track's moved 1048 note-on (no CC11 fall: a gap, not a subito)
        for _t in ("Violins I", "Violins II", "Violas", "Violoncellos"):
            _ne23.setdefault(_t, []).append({"end": 1048.0, "tol": 0.3, "gap_next_s": 0.06})
    if "chorale" not in _C23_OFF:
        # Ruling 2 (A #1, B #4, C #3): the chorale's same-pitch repeats (896-932) took a 0.025 s gap, filled by the 237 ms
        # release and Opus's 120 ms CC fade (dip median 3.0 dB at gaps under 0.04 s against 6.7 dB at 0.08-0.12 s): 0.12 s
        # on horns, trombones, bass trombone and tuba, 0.08 s on oboes and clarinets; the c22 moved fall goes, and those
        # rows take no CC11 fall at all (instr_post onset_lead "no_fall" removes the re-tongue fall, moved or not)
        _g23 = {t_: (0.12 if t_.startswith(("Horn", "Trombone", "Bass trombone", "Tuba")) else 0.08)
                for t_ in ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trombone 1", "Trombone 2", "Bass trombone", "Tuba",
                           "Oboe 1", "Oboe 2", "Clarinet 1", "Clarinet 2")}
        for _t in set(_gs23) | set(_ol23):
            _g = _g23.get(_t)
            _gs23[_t] = [dict(r_, gap_s=_g) if (_g and r_.get("pitch") == "same" and r_.get("gap_s") == 0.025 and r_.get("from") == 894.0) else r_
                         for r_ in _gs23.get(_t, [])]
            _new = []
            for r_ in _ol23.get(_t, []):
                if r_.get("set") and r_.get("gap_s") == 0.025 and 896.0 in r_.get("at", []):
                    r_ = {k_: v_ for k_, v_ in r_.items() if k_ not in ("move_fall", "fall_cc")}
                    if _g:
                        r_ = dict(r_, gap_s=_g, no_fall=True)
                _new.append(r_)
            if _t in _ol23:
                _ol23[_t] = _new
    if "tpt" not in _C23_OFF:
        # Ruling 3 (A #2, B #3): the trumpets' mf off-beats 159-166 on "Stac DblTng RRx9" (layers 1-54 / 55-75 / 76-94 /
        # 95-127, patch): velocity 88 + 7 = 95, the top layer (c21's +8 measured -2.2 / -3.3 dB under Horn 3)
        for _t in ("Trumpet 1", "Trumpet 2"):
            INSTR_POST["vel_add"][_t] = [dict(r_, add=7) if r_.get("from") == 632.9 else r_ for r_ in INSTR_POST["vel_add"].get(_t, [])]
    if "inner" not in _C23_OFF:
        # Ruling 4 (B #5): Horn 3's p G3 / A3 (pp-layer samples 11-14 dB under Horn 4's E3 / F3 at the same CC1): Horn 3
        # +8 dB, Horn 4 -3 dB in CC11 (k 40) over 935.6-947.75 (edges in the rests); Oboe 1's mf F5 of bars 143-144 (11 dB
        # under Clarinet 1's D5): +5 dB (k 33) over 567.5-575.75
        _sc23.setdefault("Horn 3", []).append({"lane": "cc11", "k": 40.0, "pts": [(935.6, 0.0), (935.65, 8.0), (947.7, 8.0), (947.75, 0.0)]})
        _sc23.setdefault("Horn 4", []).append({"lane": "cc11", "k": 40.0, "pts": [(935.6, 0.0), (935.65, -3.0), (947.7, -3.0), (947.75, 0.0)]})
        _sc23.setdefault("Oboe 1", []).append({"lane": "cc11", "k": 33.0, "pts": [(567.5, 0.0), (567.55, 5.0), (575.7, 5.0), (575.75, 0.0)]})
    if "hn4" not in _C23_OFF:
        # Ruling 8 (A #6): Horn 4's held A flat 3 fill peaked 0.24-0.30 qn after the dips (placed on score time, the note is
        # led): the first fill 0.45 qn earlier, the second narrowed to the dip
        _sc23["Horn 4"] = [r_ for r_ in _sc23.get("Horn 4", []) if not (r_.get("pts") and r_["pts"][0][0] == 171.4)] + [
            {"lane": "cc11", "k": 40.0, "pts": [(171.0, 0), (172.05, 3.0), (172.65, 4.5), (173.35, 3.0), (174.15, 0),
                                                (180.45, 0), (180.85, 5.0), (181.1, 7.0), (181.4, 5.0), (181.8, 0)]}]
    if "acc" not in _C23_OFF:
        # Ruling 8 (A #4): Trumpet 3's accents 1016-1048 (+1.1 dB): CC11 0.20 x rest with the c17 timing (hold 0.15 s, back
        # by 0.45 s; Opus smooths CC over 120 ms), CC1 +3 kept; max_step 12 -> 20 (the cap held the first build's bump at
        # +12 units over the note before: CC11 99 against plain 95)
        _acc23 = dict(INSTR_POST["accent"])
        _acc23["Trumpet 3"] = [(dict(r_, amt_rel=0.20, hold_s=0.15, end_s=0.45, max_step=20) if (r_.get("from") == 1016.0 and r_.get("lane") == "cc11") else r_)
                               for r_ in _acc23["Trumpet 3"]]
        INSTR_POST["accent"] = _acc23
    if "wsus" not in _C23_OFF:
        # Ruling 5 (c): the wind targets moved to the sustain row (ART_SPANS above) start 0.06 s early with no overlap
        for _t, (_row, _at) in _C23_SUS.items():
            _ol23[_t] = _ol23.get(_t, []) + [{"at": list(_at), "lead_s": 0.06, "set": True, "rows": ("Sus",)}]
            _gs23[_t] = _gs23.get(_t, []) + [{"from": min(_at) - 5.0, "to": max(_at) + 2.0, "min_qn": 0.5, "gap_s": 0.0,
                                              "rows": ("Sus", "Leg"), "only_at": list(_at)}]
    if "cb" not in _C23_OFF:
        # Ruling 6 (C #2): the basses' strokes half-rise about 55 ms before the beat and 75 ms before the timpani (lead
        # 0.10 s put the peak on the beat): lead 0.06 s (C23_CBLEAD for the range test)
        INSTR_POST["row_onset"] = {"Double basses": [dict(r_, lead_s=float(_os15.environ.get("C23_CBLEAD", "0.06")))
                                                     for r_ in INSTR_POST["row_onset"]["Double basses"]]}
    INSTR_POST["cc_scale"], INSTR_POST["gap_set"], INSTR_POST["onset_lead"], INSTR_POST["note_end"] = _sc23, _gs23, _ol23, _ne23

# ---------- mvt3 c24 (2026-11-17; critics on the c23 render: cycles/c24/reports/A-C.md; coordinator's rulings 1-12) ----------
# Standing rule (Dan): no per-note fader move; every fix on the instrument side, a held phrase level or a delivery ride.
_C24 = _os15.environ.get("C24", "1") == "1"
_C24_OFF = set(_os15.environ.get("C24_OFF", "").split(","))      # parts left out (range tests / fallbacks)
# string chord notes for "Sus Marc LITE" (ruling 2): C24_MARC = "on" (all), "ab" (range A/B: bars 1-2 at the chords'
# velocity (top marcato layer), bars 5-6 at velocity 92 (middle layer)), "off"
_C24_MARC = _os15.environ.get("C24_MARC", "on")
# (1088 is printed tremolo on all four sections: it stays on the Tremolo row)
_C24_MARC_AT = (0.0, 4.0, 16.0, 20.0, 372.0, 584.0, 1104.0)
_C24_MARC_VEL = int(_os15.environ.get("C24_MARC_VEL", "92"))    # 0: the note's own velocity
_C24_MARC_TR = tuple(_os15.environ.get("C24_MARC_TR", "Violins I").split(","))
_C24_STR = ("Violins I", "Violins II", "Violas", "Violoncellos")
_C24_BRASS = ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trumpet 1", "Trumpet 2", "Trumpet 3", "Trombone 1", "Trombone 2",
              "Bass trombone", "Tuba")
if _C24:
    if "marc" not in _C24_OFF and _C24_MARC != "off":
        # Ruling 2 (critic C #1): the accented ff tutti chords swelled for 0.3-0.5 s on "Sus MAX" (Violins I 11.4 dB under
        # their peak at the start, peak +450 ms; median master peak 212 ms after the beat over 44 accented tutti chords,
        # Dvorak 125 ms). The chord notes on "Sus Marc LITE" (key 25; marcato sample + LITE sustain, manual p.91-92), lead
        # 0.085 s (Movement I c58: level at +9..+51 ms), the LITE sustain held up by a +4 dB region gain (mix.json)
        # (range T1: Violins I peaked +225 ms at 16 (c23 +475) with the front at body level in 2-5 kHz on the middle
        # layer; Violins II / Violas / celli started 13-25 dB under their peak and peaked as late as on "Sus MAX": Violins
        # I only, velocity 92 (the middle marcato layer: 2-5 kHz front -0.4 / 0.0 dB re the body against +3.1 / +6.7 on
        # the top layer))
        for _t in _C24_MARC_TR:
            _rows = []
            for _x in _C24_MARC_AT:
                _r = {"from": _x - 0.3, "to": _x + 0.3, "art": "Sus Marc LITE", "poly": True}
                if _C24_MARC == "ab" and _x in (16.0, 20.0):
                    _r["vel_add"] = -19   # 111 -> 92: the middle marcato layer (1V 66-108, V2 61-99, Va 62-105, Vc 61-99)
                elif _C24_MARC_VEL:
                    _r["vel_add"] = _C24_MARC_VEL - 111
                _rows.append(_r)
            ART_SPANS[_t] = _rows + list(ART_SPANS.get(_t, []))
    if "tbn" not in _C24_OFF:
        # Ruling 8 (critic A #4): Trombone 1's slurred accents in the Piu allegro heads (985 / 993 / 1001) on "Leg Slur MAX"
        # v118 bit (2-5 kHz +5.4..+10.9 dB over the body; master jump +2.8 dB at 993): tongued on "Sus MAX" at v103 as
        # their neighbours 990 / 998 / 1006, the pickup ends 0.02 s before (instr_post note_end below)
        ART_SPANS["Trombone 1"] = [{"from": x_ - 0.1, "to": x_ + 0.1, "art": "Sus MAX"} for x_ in (985.0, 993.0, 1001.0)] \
            + list(ART_SPANS.get("Trombone 1", []))
    # (range T1 against CTRL, 200 ms holes: 352 6.0 -> under 4, 876 8.1 -> 4.7 kept; 286 8.3 -> 9.8 and 860 fixed but the
    # legato note after it (864) 14.6 dB: 286 and 860 back on their c23 rows)
    _C24_VC_AT = (352.0, 876.0)
    if "vc" not in _C24_OFF:
        # Ruling 5 (critic A #2): four slurred-line legato sags of the celli (286 8.3 dB, 352 6.0, 860 10.2, 876 8.1 dB):
        # the targets on "Sus MAX" (polyphonic) 0.06 s earlier than their c23 note-on with a 0.03 s overlap; 860 (an
        # octave leap down onto a 4-qn note) as a new entry with a 0.02 s gap (instr_post rows below)
        ART_SPANS["Violoncellos"] = list(ART_SPANS.get("Violoncellos", [])) + [
            {"from": x_ - 0.1, "to": x_ + 0.1, "art": "Sus MAX", "poly": True} for x_ in _C24_VC_AT]
    if "tempo" not in _C24_OFF:
        # Ruling 10 (critic C #3): a breath before the subito entries after the ff stops of bars 94 and 113 (no time was
        # taken: tempo exactly 84 there), and a little before the B flat pedal of bar 43
        BEAT_STRETCH = {**BEAT_STRETCH, 375.0: 0.90, 451.0: 0.90, 167.0: 0.95}
    if "rides" not in _C24_OFF:
        # Ruling 3 (critic B #1): the brass chorale's f (bars 224-225) sat under the p-mf trumpet solo of bars 61-62 on
        # the mp3 (the top ride, smoothed over 3 s, still turned down after the fff of 223): +3 dB from the printed breath
        # after the fff chord (simulated on the c23 master: 224 / 225 -17.7 / -16.3 -> -15.4 / -13.3 dB, every other bar
        # unchanged, limiter 5.9)
        RIDE_TRIMS = list(RIDE_TRIMS) + [[(892.0, 0.0), (893.0, 3.0), (899.5, 3.0), (901.0, 0.0)]]
        # after the c24 render (shared spec, coordinator 17 Nov: the final chord is the summit and leads bars 223 / 263
        # and every ff bar by 0.5 LU or more on the mp3; re-delivered on the c24 master, variant g): 223's arrival -5.0 ->
        # -7.4 dB with bar 222 -5.0 -> -5.8; bars 261-262 -2.5 -> -3.3; bar 263 itself -2.0 dB (new row); the AirPods rows.
        # Result: final -7.5, 223 -8.1, 263 -8.3, loudest ff bar (227) -8.1; steps 223 +3.1, 263 +0.6, final +0.9;
        # LRA 11.8, p10 -22.3, limiter 5.8 dB (first delivery: final and 223 tied at -7.5)
        RIDE_TRIMS = [([(879.5, 0.0), (880.0, -3.5), (884.0, -5.8), (887.9, -5.8), (888.0, -7.4), (891.5, -7.4), (892.0, 0.0)] if r_[0][0] == 879.5 else
                       [(1023.5, 0.0), (1024.0, -2.5), (1032.0, -3.5), (1040.0, -3.3), (1046.0, -3.3), (1047.8, -3.3), (1047.95, 0.0)] if r_[0][0] == 1023.5 else r_)
                      for r_ in RIDE_TRIMS] + [[(1047.9, 0.0), (1048.0, -2.0), (1051.5, -2.0), (1052.0, 0.0)]]
        if _os15.environ.get("C24_AIRPODS", "1") == "1":
            # Ruling 3 (B #1 sim3, Dan's AirPods note): +2 dB on the quietest music of the mp3 (bars 171-180, 97-98)
            RIDE_TRIMS = RIDE_TRIMS + [[(679.5, 0.0), (680.0, 2.0), (719.5, 2.0), (720.5, 0.0)],
                                       [(383.5, 0.0), (384.0, 2.0), (391.8, 2.0), (392.0, 0.0)]]
    if "pedal" not in _C24_OFF:
        # Ruling 6 (critic B, other checks): the basses' pp pedal of bars 43-50 had a fader ramp -5.5 -> -3 dB inside the
        # re-bowed note of 170.9 (the release of the 164-168 decrescendo's -2.5 dB gain at 2.8 dB/s, no printed hairpin):
        # no gain on that decrescendo for the basses (its CC11 fall 52 -> 32 stays)
        HP_SOFT_ACC_SKIP = list(HP_SOFT_ACC_SKIP) + [(164.0, "Double basses")]
if _C24 and INSTR_POST:
    _sc24 = {t_: [dict(r_) for r_ in v_] for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _ne24 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_end") or {}).items()}
    _ol24 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("onset_lead") or {}).items()}
    _gs24 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("gap_set") or {}).items()}
    _cs24 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("cc_shape") or {}).items()}
    _nc24 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_cc") or {}).items()}
    _C24_K20 = _C24_BRASS + ("Clarinet 1", "Clarinet 2")
    _C24_RESIZED = []
    if "law" not in _C24_OFF:
        # Ruling 1 (critic B #2): on the brass and clarinet KS Masters CC11 is linear volume (20 log10): every cc_scale
        # row on those tracks is now written at k 20. Rows that were planned as a dB value keep their dB (they now deliver
        # it; at k 40 they delivered half); rows whose delivered level was fitted on a render or confirmed by a critic keep
        # their lane (dB halved at k 20): the counterstatement rows at 103.5 / 103.7 (B c24: bass theme 6 dB over the
        # countersubject, do not touch), the muted Trumpet 1's unison row at 679.7 (B c24: within 1-3 dB of the cor
        # anglais), Horn 4's fill at 171 (fitted on the c22 render); Horn 3 / Horn 4 at 935.6 are set by ruling 7 below
        INSTR_POST["cc_scale_k"] = {t_: 20.0 for t_ in _C24_K20}
        _keep = {103.5, 103.7, 679.7, 171.0}
        for _t in _C24_K20:
            _new = []
            for r_ in _sc24.get(_t, []):
                if r_.get("lane", "cc11") == "cc11" and float(r_.get("k", 40.0)) == 40.0:
                    q0_ = r_["pts"][0][0]
                    if q0_ in _keep:
                        r_ = dict(r_, k=20.0, pts=[(p_[0], p_[1] / 2.0) for p_ in r_["pts"]])
                        _C24_RESIZED.append((_t, q0_, "lane kept"))
                    else:
                        r_ = dict(r_, k=20.0)
                        _C24_RESIZED.append((_t, q0_, "dB kept"))
                _new.append(r_)
            if _t in _sc24:
                _sc24[_t] = _new
    if "inner" not in _C24_OFF:
        # Ruling 7: inner voices
        # - Horn 3's p G3 / A3 in bars 235-237 (B: 6.2-8.8 dB under Horn 4; C: CC1 36-39 keeps them in the weak layer,
        #   manual p.101; Movement I c59: CC1 42 -> 52 raised G3 about 7 dB): CC1 +12 over 935.6-947.75; CC11 as c23
        #   delivered it (+4.0 dB at k 20, measured), Horn 4 -1.5 dB at k 20 (c23's -3 at k 40)
        _sc24["Horn 3"] = [r_ for r_ in _sc24.get("Horn 3", []) if r_["pts"][0][0] != 935.6] + [
            {"lane": "cc11", "k": 20.0, "pts": [(935.6, 0.0), (935.65, 4.0), (947.7, 4.0), (947.75, 0.0)]}]
        _sc24["Horn 4"] = [r_ for r_ in _sc24.get("Horn 4", []) if r_["pts"][0][0] != 935.6] + [
            {"lane": "cc11", "k": 20.0, "pts": [(935.6, 0.0), (935.65, -1.5), (947.7, -1.5), (947.75, 0.0)]}]
        if "hn3cc1" not in _C24_OFF:
            _nc24.setdefault("Horn 3", []).append({"lane": "cc1", "from": 935.6, "to": 947.75, "add": 12})
        # - Oboe 1's mf F5 of bars 143-144 (c23 overshoot: level with Clarinet 1, aim 4-5 under): +5 -> +2 dB (k 33)
        #   (range T1: +2 gave 7.8 dB under the clarinet, c23's +5 1.2: +3.5)
        _sc24["Oboe 1"] = [(dict(r_, pts=[(p_[0], 3.5 if p_[1] == 5.0 else p_[1]) for p_ in r_["pts"]]) if r_["pts"][0][0] == 567.5 else r_)
                           for r_ in _sc24.get("Oboe 1", [])]
        # - Clarinet 1's pp echo of bar 121 (as loud as the bassoon solo it answers; altissimo samples): -5 dB (k 20)
        _sc24.setdefault("Clarinet 1", []).append({"lane": "cc11", "k": 20.0, "pts": [(480.75, 0.0), (480.8, -5.0), (485.95, -5.0), (486.0, 0.0)]})
        # - Trombone 2's E3 in the 223 chord (4.6 dB over Trombone 1 with identical data: sample level by pitch): -3 dB
        _sc24.setdefault("Trombone 2", []).append({"lane": "cc11", "k": 20.0, "pts": [(887.85, 0.0), (887.9, -3.0), (891.65, -3.0), (891.7, 0.0)]})
    if "acc" not in _C24_OFF:
        # Ruling 7 (B #2): Trumpet 3's accents 1016-1048 (+1.3 dB; bump CC11 88 -> 106 = +1.6 dB at the true 20 log10):
        # amt_rel 0.20 -> 0.33 (CC11 88 -> 117, +2.5 dB)
        _acc24 = dict(INSTR_POST["accent"])
        _acc24["Trumpet 3"] = [(dict(r_, amt_rel=0.33) if (r_.get("from") == 1016.0 and r_.get("lane") == "cc11") else r_)
                               for r_ in _acc24["Trumpet 3"]]
        INSTR_POST["accent"] = _acc24
    if "arr" not in _C24_OFF:
        # Ruling 4 (critic A #3; no breath is printed before 223): a fresh tongued attack on the fff chord at 888 (gaps
        # 45-80 ms there against 88-122 ms at 1048, where the brass re-attack dips 5.1-11.2 dB): the whole notes into 888
        # end 0.10 s before the track's next note-on on horns, trombones, bass trombone, tuba, Trumpets 2-3; 0.08 s on
        # Trumpet 1 (the leading-tone arrival) and the winds; no CC11 fall; Flute 1, strings, timpani untouched
        for _t in ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trombone 1", "Trombone 2", "Bass trombone", "Tuba", "Trumpet 2", "Trumpet 3"):
            _ne24.setdefault(_t, []).append({"end": 888.0, "tol": 0.3, "gap_next_s": 0.10})
        for _t in ("Trumpet 1", "Oboe 1", "Oboe 2", "Clarinet 1", "Clarinet 2", "Bassoon 1", "Bassoon 2", "Contrabassoon"):
            _ne24.setdefault(_t, []).append({"end": 888.0, "tol": 0.3, "gap_next_s": 0.08})
        # (range T1: the c18 chorale breath rows (gap_set from 888, 0.035-0.085 s) set the 888 join after note_end and
        # undid it: those rows skip the 888 join)
        for _t in ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trombone 1", "Trombone 2", "Bass trombone", "Tuba", "Trumpet 1",
                   "Trumpet 2", "Trumpet 3", "Oboe 1", "Oboe 2", "Clarinet 1", "Clarinet 2", "Bassoon 1", "Bassoon 2", "Contrabassoon"):
            _gs24[_t] = [(dict(r_, skip_at=tuple(r_.get("skip_at", ())) + (888.0,)) if r_.get("from", 0) <= 888.0 < r_.get("to", 0) else r_)
                         for r_ in _gs24.get(_t, [])]
    if "marc" not in _C24_OFF and _C24_MARC != "off":
        # Ruling 2: the marcato chords start 0.085 s before the score onset (Movement I c58) and take no CC11 accent bump
        # (the marcato sample is the accent; Movement I c55: slow-front accent shapes added 4.5 dB on this row)
        for _t in _C24_MARC_TR:
            _ol24.setdefault(_t, []).append({"at": list(_C24_MARC_AT), "lead_s": 0.085, "set": True, "rows": ("Sus Marc",)})
        _acc24m = dict(INSTR_POST["accent"])
        for _k in ("string",) + _C24_STR:
            if _k in _acc24m:
                _acc24m[_k] = [dict(r_, skip_rows=("Sus Marc",)) for r_ in _acc24m[_k]]
        INSTR_POST["accent"] = _acc24m
        # the printed ff of 16 and 584 steps CC11 at the score onset, 0.085 s after the led chord starts (lane 84-90 at
        # the moved note-on, 101-107 at the onset): the step moves to the moved note-on (from 0.06 s before it: Opus
        # smooths CC); values from parts.json (lane at the onset minus lane at the moved note-on)
        for _t, _d16, _d584 in (("Violins I", 17, 19), ("Violins II", 17, 16), ("Violas", 17, 17), ("Violoncellos", 17, 17)):
            if _t not in _C24_MARC_TR:
                continue
            for _x, _d in ((16.0, _d16), (584.0, _d584)):
                _cs24.setdefault(_t, []).append({"lane": "cc11", "at": _x, "from_note": True, "pts": [(-0.06, _d), (0.085, _d), (0.09, 0)]})
    if "tbn" not in _C24_OFF:
        for x_ in (985.0, 993.0, 1001.0):
            _ne24.setdefault("Trombone 1", []).append({"end": x_, "tol": 0.3, "gap_next_s": 0.02})
    if "vc" not in _C24_OFF:
        # Ruling 5: the celli sag targets (ART_SPANS above): lead = c23 lead + 0.06 s; 0.03 s overlap (286, 352, 876),
        # 860 a new entry (0.02 s gap)
        _ol24.setdefault("Violoncellos", []).extend([
            {"at": [352.0], "lead_s": 0.307, "set": True, "rows": ("Sus",)},
            {"at": [876.0], "lead_s": 0.307, "set": True, "rows": ("Sus",)}])
        _gs24.setdefault("Violoncellos", []).append({"from": 280.0, "to": 880.0, "min_qn": 0.5, "gap_s": -0.03, "allow_leg": True,
                                                    "rows": ("Sus", "Leg"), "only_at": [352.0, 876.0]})
    if "step" not in _C24_OFF:
        # Ruling 9 (critic A #5): the dynamic step arrived 0.27 / 0.22 s after the led note started (Movement I c61):
        # Violins II at 511 (CC11 32 until the score onset, then 72) and the celli at 952 (43 -> 88) take the new level
        # from their moved note-on
        _cs24.setdefault("Violins II", []).append({"lane": "cc11", "at": 511.0, "from_note": True, "pts": [(0.0, 39), (0.27, 39), (0.28, 0)]})
        _cs24.setdefault("Violoncellos", []).append({"lane": "cc11", "at": 952.0, "from_note": True, "pts": [(0.0, 45), (0.217, 45), (0.23, 0)]})
    INSTR_POST["cc_scale"], INSTR_POST["note_end"], INSTR_POST["onset_lead"], INSTR_POST["gap_set"] = _sc24, _ne24, _ol24, _gs24
    INSTR_POST["cc_shape"], INSTR_POST["note_cc"] = _cs24, _nc24

# ---------- mvt3 c25 (2026-11-17; critics on the c24 render: cycles/c25/reports/A-C.md; coordinator's rulings 1-9) ----------
# Standing rule (Dan): no per-note fader move; every fix on the instrument side, a held passage level (roles.json, with
# the role edges in rests: ROLE_EDGE_XF) or a delivery ride. Env C25=0 leaves the block out, C25_OFF=a,b leaves parts out.
_C25 = _os15.environ.get("C25", "1") == "1"
_C25_OFF = set(_os15.environ.get("C25_OFF", "").split(","))
_C25_RBC = _os15.environ.get("C25_RBC", "-14")   # range T1 at -10: bow rises 6.3 / 4.9 / 8.6 -> 3.6 / 2.0 / 5.7 dB   # basses' re-bow CC11 counter-shape depth (units), ruling 4
if _C25:
    if "themeb" not in _C25_OFF:
        # Ruling 1 (critic B #3): the bars 209-210 crescendo gains (+2..+4 dB) were held into the ff downbeat of bar 211 and
        # released after it, so the accompaniment hit its ff 2-4 dB over its own ff and the trumpets' theme B head sat
        # 6.9 dB under it: the gain is gone by the printed ff (tools/score_to_parts.py HP_END_AT_TARGET)
        HP_END_AT_TARGET = {"spans": [(831.5, 840.0)], "within_qn": 1.0, "max_dyn": "ff"}
    if "timp" not in _C25_OFF:
        # Ruling 5 (critic C #2): the fff roll of 223 fell CC7 96 -> 38 within 0.25 qn (timpani 26th of 31 stems in bar
        # 223): one ramp over the printed decrescendo to the f of 892; at 1048 (fff, no hairpin) a ramp from the level
        # before the arrival to the roll's own level by 1050; 1108 (the final chord) unchanged
        TIMP_ARRIVAL_RAMP = [(888.0, 892.0), (1048.0, 1050.0)]
    # role edges placed in the rests between notes (crossfade windows, played qn)
    ROLE_EDGE_XF = dict(ROLE_EDGE_XF)
    ROLE_EDGE_XF["Violins II"] = {**ROLE_EDGE_XF.get("Violins II", {}), 631.8: (630.95, 631.8), 659.8: (659.775, 659.85)}
    ROLE_EDGE_XF["Violoncellos"] = {**ROLE_EDGE_XF.get("Violoncellos", {}), 39.86: (39.849, 39.884), 104.0: (103.802, 103.82),
                                    600.0: (598.9, 599.9), 663.62: (663.6, 663.66)}
if _C25 and INSTR_POST:
    _sc25 = {t_: [dict(r_) for r_ in v_] for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _ol25 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("onset_lead") or {}).items()}
    _gs25 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("gap_set") or {}).items()}
    _cs25 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("cc_shape") or {}).items()}
    _nc25 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_cc") or {}).items()}
    _vc25 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("vel_cap") or {}).items()}
    _cc25 = {t_: [dict(r_) for r_ in v_] for t_, v_ in (INSTR_POST.get("cc_cap") or {}).items()}
    if "inner" not in _C25_OFF:
        # Ruling 1 (critic C #1; Dan 17 Nov "inner lines hidden"): the second violins' f espress. countersubject of bars
        # 159-165 sat 15-17 dB under the first violins (CC11 75-82 against 107, role -2.9, velocity 83): CC11 to 88-92
        # (under the 94 layer step of the Sus MAX start-mode ranges), velocity 100 as in the same figure at 104-120, role
        # 0 over 631.8-659.8 (roles.json); the clarinets on the same figure +2 dB (k 20)
        _nc25.setdefault("Violins II", []).extend([
            {"lane": "cc11", "rows": ("Sus",), "from": 631.9, "to": 644.9, "add": 13},
            {"lane": "cc11", "rows": ("Sus",), "from": 644.9, "to": 659.9, "add": 10}])
        _vc25.setdefault("Violins II", []).append({"row": "Sus MAX", "min": 100, "max": 100, "from": 631.9, "to": 659.9})
        for _t in ("Clarinet 1", "Clarinet 2"):
            _sc25.setdefault(_t, []).append({"lane": "cc11", "k": 20.0, "pts": [(631.7, 0.0), (631.73, 2.0), (659.85, 2.0), (659.88, 0.0)]})
        # (critic B #4) the cor anglais / Horn 1 espressivo line of bars 217-218 3-9 dB under the violins' held f > mf
        # chords: the chord printed at 864 -5 CC11 units on both violin sections (a passage level inside the patch; the
        # roles of the line are in roles.json)
        for _t in ("Violins I", "Violins II"):
            _nc25.setdefault(_t, []).append({"lane": "cc11", "from": 863.95, "to": 864.05, "add": -5})
    if "marc" not in _C25_OFF:
        # Ruling 2 (critic B #1): the Violins I "Sus Marc LITE" chords 7-10 dB over c23 and 5-10 dB over Violins II and the
        # violas: the LITE region gain +4 -> 0 (mix.json) and -5 dB on CC11 over each chord (k 20: on LITE strings CC11 is
        # loudness only, manual p.62); the row, velocity 92, the lead and the CC11 step rows stay
        # (range T1: with the region gain removed, -5 dB at k 20 took the Violins I fronts 8.5 dB down and the body 14 dB
        # (bar 1 front -35.4 against Violins II -34.1, body -42.8 against -30.1): the row's CC11 is not 20 log10. The
        # CC11 scale is dropped (env C25_V1CC=1 restores it); the -4 dB region gain removal alone is kept)
        for _a, _b in (((-0.2, 5.0), (15.6, 21.0), (371.6, 373.88), (583.6, 588.0), (1103.6, 1105.05))
                       if _os15.environ.get("C25_V1CC") == "1" else ()):
            _sc25.setdefault("Violins I", []).append({"lane": "cc11", "k": 20.0, "pts": [(_a, 0.0), (_a + 0.03, -5.0), (_b - 0.05, -5.0), (_b, 0.0)]})
        # (critic A #2) the lower strings' accented ff chord at 16 started on the f layer (CC11 steps 82 -> 99 at the
        # note-on, lead 0): the step 0.06 s ahead and a front at the knee (lane + 5 = 104-105) for 0.12 s, gone by 0.30 s
        for _t in ("Violins II", "Violas", "Violoncellos"):
            _cs25.setdefault(_t, []).append({"lane": "cc11", "at": 16.0, "from_note": True,
                                             "pts": [(-0.06, 17), (-0.005, 17), (0.0, 5), (0.12, 5), (0.30, 0)]})
        # at 584 the celli: a 0.04 s lead and the step (88 -> 106 at the score onset) from 0.06 s before the moved note-on
        _ol25.setdefault("Violoncellos", []).append({"at": [584.0], "lead_s": 0.04, "set": True, "rows": ("Sus",)})
        # (the accent's pre-note ceiling, rest + bump from the lane before the step, would hold the front at 89: no_pre_cap)
        _cs25.setdefault("Violoncellos", []).append({"lane": "cc11", "at": 584.0, "from_note": True, "no_pre_cap": True,
                                                     "pts": [(-0.06, 18), (0.035, 18), (0.04, 0)]})
    if "vc" not in _C25_OFF:
        # Ruling 3 (critic A #1): the celli bass line of bars 11-26 / 151-166 on "Detache" (C24_VC "det" above). Patch read
        # (opus_state): the Detache groups "1V mp" / "1V ff" cover velocity 1-127 with no velocity processor, and CC11
        # crossfades them (the mp group's CC11 -> volume connection has intensity -1); the f statement at CC11 84-87 sat
        # in the crossfade (c24 range: 9-23 dB swells), the ff statement at 100-105 was flat. The f statement plays at the
        # ff statement's CC11 (+14 units: 89-92 -> 103-106; the Sus MAX row offset -5 does not apply to Detache) and its
        # level comes from a held passage level (roles.json [39.86, 103.81]); velocity 91 on both (the ruling's value; it
        # does not change the sound); release caps mp 300 / ff 150 ms (mix.json)
        _nc25.setdefault("Violoncellos", []).append({"lane": "cc11", "rows": ("Detache",), "from": 39.9, "to": 103.9, "add": 14})
        _vc25.setdefault("Violoncellos", []).append({"row": "Detache", "min": 91, "max": 91, "from": 39.9, "to": 664.1})
    if "rebow" not in _C25_OFF:
        # Ruling 4 (critic A #3): each new bow of the basses' pp pedal (bars 43-50) bloomed 5-10 dB at 0.75-1.5 s and sagged:
        # a CC11 counter-shape per bow (build/rebow_cc11.json, the format tools/fit_rebows.py --cc11 writes); depth by
        # C25_RBC (range test)
        _rbc = json.load(open(f"{BUILD}/rebow_cc11.json")) if _os15.path.exists(f"{BUILD}/rebow_cc11.json") else {}
        for _t, _rows in _rbc.items():
            if _t.startswith("_"):
                continue
            for _k, _pts in _rows.items():
                _sc = float(_C25_RBC) / -10.0 if _t == "Double basses" else 1.0
                _cs25.setdefault(_t, []).append({"lane": "cc11", "at": float(_k), "from_note": True,
                                                 "pts": [(float(x_), round(float(y_) * _sc)) for x_, y_ in _pts]})
    if "harp" not in _C25_OFF:
        # Ruling 6 (critic B #2): the ff chord of bar 132 at velocity 123 (top pluck layer) 13 dB over every other stem:
        # velocity 96 (the f layer; mix.json dyn_trim ff +2 -> -2; the p arpeggio's role -6 -> -10 in roles.json)
        _vc25.setdefault("Harp", []).append({"row": "", "min": 96, "max": 96, "from": 523.9, "to": 524.1})
    if "acc" not in _C25_OFF:
        # Ruling 8 (critic B #6 / A #4): Trumpet 3's accents 1016-1048 (+1.2-1.4 dB, held 0.48 s like the body): CC11 bump
        # held 0.20 s, back by 0.35 s; a CC1 bump +7 for 0.25 s (brass CC1 is the dynamic layer, manual p.100); the bump
        # at 1044 was removed by the 1040-1048 crescendo ceiling (cc_cap of the 1048 arrival): the ceiling holds the
        # resting lane only there ("acc_free", tools/instr_post.py)
        _acc25 = dict(INSTR_POST["accent"])
        _acc25["Trumpet 3"] = [(dict(r_, hold_s=0.20, end_s=0.35) if (r_.get("from") == 1016.0 and r_.get("lane") == "cc11") else
                                dict(r_, amt=[(0, 7)], hold_s=0.25, end_s=0.40, max=127, max_step=20) if (r_.get("from") == 1016.0 and r_.get("lane") == "cc1") else r_)
                               for r_ in _acc25["Trumpet 3"]]
        INSTR_POST["accent"] = _acc25
        _cc25["Trumpet 3"] = [(dict(r_, acc_free=True) if (r_.get("pts") and abs(r_["pts"][0][0] - 1040.0) < 0.01) else r_)
                              for r_ in _cc25.get("Trumpet 3", [])]
    if "mute" not in _C25_OFF:
        # Ruling 8 (critic A #5): Trumpet 1's slurred con sordino solo on "Mute Sus" (no muted legato row) dipped 4-7 dB at
        # four joins inside the slurs (688, 715, 726, 727): pitch-changing joins inside the slurs of 680-694 and 712-728
        # overlap 0.06 s (the sustain row crossfades two voices), and the four targets start 0.04 s earlier
        _gs25.setdefault("Trumpet 1", []).extend([
            {"from": 680.0, "to": 693.9, "min_qn": 0.2, "gap_s": -0.06, "rows": ("Mute",), "pitch": "diff"},
            {"from": 712.0, "to": 727.9, "min_qn": 0.2, "gap_s": -0.06, "rows": ("Mute",), "pitch": "diff"}])
        _ol25.setdefault("Trumpet 1", []).extend([
            {"at": [688.0, 715.0, 727.0], "lead_s": 0.075, "set": True, "rows": ("Mute",)},
            {"at": [726.0], "lead_s": 0.125, "set": True, "rows": ("Mute",)}])
    if "taper" not in _C25_OFF:
        # Ruling 8 (critic A #6): Horn 1 and Trumpet 1 barely lifted before the fff of 223 (3.1 / 1.6 dB): a CC1 taper over
        # the last 0.25 s of the 884 note (brass CC1 is the dynamic layer, smoothed over 120 ms); the 888 step stays. The
        # crescendo's ceiling (cc_cap 108 to the arrival) sits under the raw lane (117-120 there), so -15 on the raw lane
        # took only 5 units off the played value: -25 (played 108 -> 93-95, the critic's -15)
        for _t in ("Horn 1", "Trumpet 1"):
            _cs25.setdefault(_t, []).append({"lane": "cc1", "at": 888.0, "from_note": True,
                                             "pts": [(-0.38, 0), (-0.14, -25), (-0.006, -25), (-0.005, 0)]})
    INSTR_POST["cc_scale"], INSTR_POST["onset_lead"], INSTR_POST["gap_set"] = _sc25, _ol25, _gs25
if _C25 and "rides" not in _C25_OFF:
    # after the c25 render (shared spec): the first delivery had the limiter at 6.3 dB on the final chord (40in bass drum)
    # and bar 212 (theme B, louder by its new roles) level with bar 223 at -8.1; re-delivered on the c25 master (variant
    # c): final -4.5 -> -5.5, 223 -7.4 -> -8.4, bar 212 -1.0 dB (new row), bar 263 -2.0 -> -2.6: final -7.8, 223 -8.4,
    # 263 -8.4, limiter 5.4 dB, LRA 11.3
    def _r25(r_):
        q0_ = r_[0][0]
        if q0_ == 1087.0:
            return [(q_, -5.5 if q_ in (1107.95, 1113.0) else v_) for q_, v_ in r_]
        if q0_ == 879.5:
            return [(q_, -8.4 if q_ in (888.0, 891.5) else v_) for q_, v_ in r_]
        if q0_ == 1047.9:
            return [(q_, -2.6 if q_ in (1048.0, 1051.5) else v_) for q_, v_ in r_]
        return r_
    RIDE_TRIMS = [_r25(r_) for r_ in RIDE_TRIMS] + [[(843.8, 0.0), (844.0, -1.0), (847.9, -1.0), (848.0, 0.0)]]
    INSTR_POST["cc_shape"], INSTR_POST["note_cc"], INSTR_POST["vel_cap"], INSTR_POST["cc_cap"] = _cs25, _nc25, _vc25, _cc25

# ---------- mvt3 c26 (2026-11-17; critics on the c25 render: cycles/c26/reports/A-C.md; coordinator's rulings 1-8) ----------
# Standing rule (Dan, 11 Nov): the track volume envelope holds slow balance only; no per-note fader move. Env C26=0 leaves
# the block out, C26_OFF=a,b leaves parts out; C26_WIND picks the wind-solo variant per track for the range tests
# ("Flute 1:A,Clarinet 1:B,..."; A = run heads v90, B = "Leg Slur Runs", C = sustain-row targets, 0 = none).
_C26 = _os15.environ.get("C26", "1") == "1"
_C26_OFF = set(_os15.environ.get("C26_OFF", "").split(","))
_C26_WIND = dict(x_.split(":") for x_ in _os15.environ.get("C26_WIND", "Flute 1:0,Clarinet 1:C,Oboe 1:B,Bassoon 1:C").split(",") if ":" in x_)
_C26_MARC_VEL = int(_os15.environ.get("C26_MARC_VEL", "0"))   # Violins I "Sus Marc LITE" chord velocity (ruling 8); 0 = c24's 92
# (range T1 at v80: Violins I front minus Violins II +7.2 / +8.9 -> +7.7 / +6.2 dB at 0 / 16, body +0.9 / +1.7 -> +3.7 / +4.6: withdrawn)
_C26_RUNS = {   # ruling 6: (span, head qn, weak targets, sustain row, {note score qn: CC1 offset that copies CC11 into CC1})
    "Flute 1": ((168.8, 174.1), (169.0,), (169.5, 170.0), "Sus MAX",
                {169.0: -76, 169.5: -75, 170.0: -63, 170.5: -61, 171.0: -59, 171.5: -57, 172.0: -54, 172.5: -44, 173.0: -38, 173.5: -35, 174.0: -33}),
    "Clarinet 1": ((176.8, 182.1), (177.0,), (177.5, 178.0), "Sus Non Vib",
                   {177.0: 10, 177.5: 10, 178.0: 10, 178.5: 10, 179.0: 9, 179.5: 6, 180.0: 4, 180.5: 4, 181.0: 4, 181.5: 4, 182.0: 4}),
    "Oboe 1": ((184.8, 188.1), (185.0,), (185.5, 187.5), "Sus MAX",
               {185.0: -58, 185.5: -47, 186.0: -46, 186.5: -45, 187.0: -44, 187.5: -45, 188.0: -51}),
    "Bassoon 1": ((455.9, 516.0), (456.0, 496.0), (459.0, 460.0, 464.0, 475.0, 499.0, 507.0), "Sus MAX", {}),   # c30 ruling 1: + 464, 475
}
if _C26:
    if "decresc" not in _C26_OFF:
        # Ruling 1 (A #5, B #6, C #3): the held-decrescendo level is released at the led next note's moved onset over 0.25 s
        # (the basses' note at 932 is tied on through the onset: 1.1 s, under 3 dB/s) (tools/score_to_parts.py)
        HELD_DECRESC_LED_RELEASE = {"Double basses": 1.1, "string": 0.25, "wind": 0.25}
        # the other in-note edges: unison phrase level released in the rest before the led note (Trombone 2 at 152); the
        # player-count marks at 376 ("sul tasto, last 2 desks") and 485 ("4 soli") step in the rest before the led note
        UNI_HOLD_END_REST = True
        CHORD_SEG_EDGE_REST = True
        # celli role edges (roles.json rows split): the bar 1-4 lift ends in the gap before the ff chord of 16 (the quarter
        # at 15 ends 0.055 s earlier, a lift before the down-bow accent: INSTR_POST note_end below); the 1016-1032 lift ends
        # in the 1031.784-1031.824 gap before the tied F2
        ROLE_EDGE_XF = dict(ROLE_EDGE_XF)
        ROLE_EDGE_XF["Violoncellos"] = {**ROLE_EDGE_XF.get("Violoncellos", {}), 15.9: (15.852, 15.872), 1032.0: (1031.786, 1031.822)}
        ROLE_EDGE_XF["Violins I"] = {**ROLE_EDGE_XF.get("Violins I", {}), 15.9: (15.705, 15.755)}
    if "timp" not in _C26_OFF:
        # Ruling 4 (B #4a): the final chord's fff roll started at CC7 36 (-11 dB) against 97 at 223: the 223 law, CC7 97 at
        # the note-on, about 85 at the end of the fermata (no printed decrescendo)
        TIMP_ARRIVAL_RAMP = list(TIMP_ARRIVAL_RAMP) + [(1108.0, 1113.0, 97, 85)]
    if "cc7" not in _C26_OFF:
        # Ruling 5 (B #1, #2; manual p.64 / p.151: CC7 sets a track's upper level inside the patch): passage levels in CC7,
        # edges in rests: violas -3.0 dB over the theme B head (838.85-839.81 rest; back in the 847.94-848.0 gap), Violins I
        # -4.0 dB over the countersubject bars 159-165 (630.86-631.82 rest; back in the 659.69-659.78 gap)
        CC7_POINTS = dict(CC7_POINTS)
        CC7_POINTS["Violas"] = [(839.3, 90), (847.96, 127)]
        CC7_POINTS["Violins I"] = [(631.4, 80), (659.73, 127)]
    if "rr" not in _C26_OFF:
        # Ruling 7 (A #2): the celli's Detache G2 pairs at 96-98 and 656-658: a round-robin reset before the first note, so
        # the repeat plays the second take (second-take repeats rise 8.9-10.3 dB, first-take 1.4-1.8)
        RR_RESET_AT = dict(RR_RESET_AT, Violoncellos=sorted(list(RR_RESET_AT.get("Violoncellos", [])) + [96.0, 656.0]))
    if "marc" not in _C26_OFF and _C26_MARC_VEL:
        # Ruling 8 (A, other checks): the Violins I marcato chord fronts about 5 dB over Violins II at v92: v80 (range test)
        ART_SPANS["Violins I"] = [(dict(r_, vel_add=_C26_MARC_VEL - 111) if (r_.get("art") == "Sus Marc LITE" and "vel_add" in r_) else r_)
                                  for r_ in ART_SPANS.get("Violins I", [])]
    if "tpt" not in _C26_OFF:
        # Ruling 8 (A #3): the trumpets' tenuto at 989 on "Sus Non Vib MAX" stood 12-15 dB over the slur's legato notes: on
        # "Leg Slur MAX" as a target (Movement I c07: a tenuto to a new pitch is a legato target), weight in CC11 below
        for _t in ("Trumpet 1", "Trumpet 2"):
            ART_SPANS[_t] = [{"from": 988.9, "to": 989.1, "art": "Leg Slur MAX"}] + list(ART_SPANS.get(_t, []))
    for _t, (_sp, _heads, _weak, _srow, _cc1) in _C26_RUNS.items():
        _v = _C26_WIND.get(_t, "0")
        if _v == "B" and _t != "Bassoon 1":
            # Ruling 6 variant B (A #1; manual p.112): the runs (seconds throughout) on "Leg Slur Runs"
            ART_SPANS[_t] = [{"from": _sp[0], "to": _sp[1], "art": "Leg Slur Runs"}] + list(ART_SPANS.get(_t, []))
        elif _v == "C":
            # variant C: the weak targets on the sustain row (the c23 fix)
            ART_SPANS[_t] = [{"from": x_ - 0.1, "to": x_ + 0.1, "art": _srow} for x_ in _weak] + list(ART_SPANS.get(_t, []))
if _C26 and INSTR_POST and "guard" not in _C26_OFF:
    # Ruling 1 / coordinator's note (scherzo c24: a slope guard that skipped hairpin spans missed most violations): the
    # fader guard no longer leaves moves under printed hairpins alone (a hairpin ramp steeper than 3 dB/s inside a held
    # note is stretched to 2.8 dB/s or moved before the note), and the bar 3-4 skip window is gone (the role edge is in
    # a rest now)
    INSTR_POST["vol_guard"] = dict(INSTR_POST["vol_guard"], skip=[])   # hairpin_ok False tried: 30 hairpin ramps moved before their note-ons (crescendo gains ahead of the notes): withdrawn
if _C26 and INSTR_POST:
    _sc26 = {t_: [dict(r_) for r_ in v_] for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _ol26 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("onset_lead") or {}).items()}
    _gs26 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("gap_set") or {}).items()}
    _cs26 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("cc_shape") or {}).items()}
    _nc26 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_cc") or {}).items()}
    _vc26 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("vel_cap") or {}).items()}
    _cc26 = {t_: [dict(r_) for r_ in v_] for t_, v_ in (INSTR_POST.get("cc_cap") or {}).items()}
    _ne26 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_end") or {}).items()}
    if "decresc" not in _C26_OFF:
        _ne26.setdefault("Violoncellos", []).append({"end": 16.0, "tol": 0.02, "early_s": 0.055})
        _ne26.setdefault("Violins I", []).append({"end": 16.0, "tol": 0.02, "early_s": 0.107})
    if "stops" not in _C26_OFF:
        # Ruling 2 (B #5, C #2b): the celli note that ends each tutti stop (bars 94, 113) kept CC11 at 102-109 through its
        # release (falling only at the next entry): a ceiling from 0.02 s before the note-off to 0.08 s after it, 109 -> 80
        # and 102 -> 75 (about -6 dB), held to the next entry's own value
        _cc26.setdefault("Violoncellos", []).extend([
            {"lane": "cc11", "pts": [(373.80, 109), (374.08, 80), (375.40, 80), (375.462, 58)]},
            {"lane": "cc11", "pts": [(449.80, 102), (450.08, 75), (451.40, 75), (451.462, 46)]}])
    if "brass1048" not in _C26_OFF:
        # Ruling 4 (B #4b): the brass crescendo into 263 topped out at CC11 106-107 by 1047.5 (the fff step +0.5 dB): a
        # ceiling of 98 over 1043.8-1047.85 on the resting lane (accent bumps free); CC1 keeps rising
        # (range T1 against CTRL: master 1048-1050 over 1045-1047.5 +0.2 -> +0.1 dB: no effect; withdrawn, env C26_BRASSCAP=1)
        for _t in (_C24_BRASS if _os15.environ.get("C26_BRASSCAP") == "1" else ()):
            _cc26.setdefault(_t, []).append({"lane": "cc11", "pts": [(1043.8, 98), (1047.85, 98)], "acc_free": True})
        # (B #4c) the celli's fff whole notes at 1048: a front at the CC11 ceiling for the first 0.035 s (584's shape; the
        # lane is already 113-115 there)
        _cs26.setdefault("Violoncellos", []).append({"lane": "cc11", "at": 1048.0, "from_note": True, "no_pre_cap": True,
                                                     "pts": [(-0.06, 12), (0.035, 12), (0.04, 0)]})
    if "bal" not in _C26_OFF:
        # Ruling 5 (B #1): theme B head: trumpets CC1 +10 (ceiling 116: their ff 114), Trumpet 1's 842 note CC11 held near
        # the head's level (91 -> 108); violas' CC11 reaches the printed f (88) by 841.5 (CC7 above)
        for _t in ("Trumpet 1", "Trumpet 2"):
            _nc26.setdefault(_t, []).append({"lane": "cc1", "from": 839.7, "to": 846.9, "add": 10})
            _cc26.setdefault(_t, []).append({"lane": "cc1", "pts": [(839.6, 116), (847.0, 116)]})
        _nc26.setdefault("Trumpet 1", []).append({"lane": "cc11", "from": 841.95, "to": 842.05, "add": 17})
        _cc26.setdefault("Violas", []).append({"lane": "cc11", "pts": [(839.75, 107), (841.5, 88), (841.85, 88)]})
        # (B #3) the celli's p bass line of bars 235-238 played at CC11 34-36 (pp), 11 dB under the basses and violas: +12
        _nc26.setdefault("Violoncellos", []).append({"lane": "cc11", "from": 935.6, "to": 947.5, "add": 12})
    if "rr" not in _C26_OFF:
        # Ruling 7 (A #2): the five-G2 chain 600-608: 0.10 s gaps (was about 0.05) and a -12 CC11 notch on the old note
        # before each repeat (CC11 crossfades the Detache mp / ff groups)
        _gs26.setdefault("Violoncellos", []).append({"from": 601.5, "to": 608.5, "min_qn": 1.0, "gap_s": 0.10,
                                                     "rows": ("Detache",), "pitch": "same"})
        for _x in (602.0, 604.0, 606.0, 608.0):
            _cs26.setdefault("Violoncellos", []).append({"lane": "cc11", "at": _x, "from_note": True,
                                                         "pts": [(-0.18, 0), (-0.06, -12), (0.0, 0)]})
    if "tpt" not in _C26_OFF:
        # Ruling 8 (A #3): 989 as a legato target with +2 dB in CC11 (k 20: x1.26 on about 94); CC1 held at the head's
        # value (about 90) over 984-1000 (the "drive" phrase shape fell 89 -> 79)
        _off = {991.0: 3, 992.0: 4, 993.5: 5, 994.0: 6, 995.0: 6, 995.5: 7, 996.0: 8, 998.0: 9, 989.0: 2}
        for _t in ("Trumpet 1", "Trumpet 2"):
            _cs26.setdefault(_t, []).append({"lane": "cc11", "at": 989.0, "from_note": True,
                                             "pts": [(0.03, 0), (0.08, 24), (0.40, 24), (0.70, 0)]})
            for _x, _a in _off.items():
                _nc26.setdefault(_t, []).append({"lane": "cc1", "from": _x - 0.05, "to": _x + 0.05, "add": _a})
            _vc26.setdefault(_t, []).append({"row": "Leg", "min": 118, "max": 118, "from": 990.9, "to": 991.1})
    if "hn1" not in _C26_OFF:
        # Ruling 8 (A #4): Horn 1 before 888: the CC1 taper sat on the ff plateau (dip 3.7 dB): a CC11 taper 100 -> 56
        # (-5 dB at k 20) instead; Trumpet 1's CC1 taper stays
        _cs26["Horn 1"] = [r_ for r_ in _cs26.get("Horn 1", []) if not (r_.get("lane") == "cc1" and r_.get("at") == 888.0)] + [
            {"lane": "cc11", "at": 888.0, "from_note": True, "pts": [(-0.40, 0), (-0.16, -44), (-0.006, -44), (-0.005, 0)]}]
    if "mute" not in _C26_OFF:
        # Ruling 8 (A #4): the muted Trumpet 1's slurred joins at 685 / 688 / 717 / 726 sag 4-4.5 dB for 0.3 s: +2.5 dB in
        # CC11 (k 20: +33 % of the lane: 53 -> 71, 62 -> 82)
        for _x, _u in ((685.0, 18), (688.0, 18), (717.0, 18), (726.0, 20)):
            _cs26.setdefault("Trumpet 1", []).append({"lane": "cc11", "at": _x, "from_note": True,
                                                      "pts": [(-0.02, 0), (0.03, _u), (0.25, _u), (0.40, 0)]})
    # Ruling 6 (A #1): the soft wind solos
    for _t, (_sp, _heads, _weak, _srow, _cc1) in _C26_RUNS.items():
        _v = _C26_WIND.get(_t, "0")
        if _v == "A":   # run heads at v90 (were v53)
            for _h in _heads:
                _vc26.setdefault(_t, []).append({"row": "Leg", "min": 90, "max": 90, "from": _h - 0.2, "to": _h + 0.1})
        elif _v == "B" and _cc1:   # Leg Slur Runs: dynamics from CC1, copied from CC11
            for _x, _a in _cc1.items():
                _nc26.setdefault(_t, []).append({"lane": "cc1", "from": _x - 0.05, "to": _x + 0.05, "add": _a})
        elif _v == "C":   # the c23 sustain-row fix: 0.06 s early, 0.03 qn (0.011 s) overlap
            _ol26.setdefault(_t, []).append({"at": list(_weak), "lead_s": 0.06, "set": True, "rows": ("Sus",)})
            _gs26.setdefault(_t, []).append({"from": min(_weak) - 1.0, "to": max(_weak) + 0.5, "min_qn": 0.4, "gap_s": -0.011,
                                             "rows": ("Sus", "Leg"), "only_at": list(_weak), "allow_leg": True})
    if "bn" not in _C26_OFF:
        # Ruling 6 (A #1b): the bassoon solo's targets after a quarter note led by 0.42 qn at v80 and cut the quarter: the
        # normal lead 0.168 qn (0.06 s at 168 qpm) at v100; the quarter before ends 0.098 qn after the new onset as the
        # other joins (0.252 qn = 0.09 s later)
        _bnq = (468.0, 480.0, 500.0, 503.0, 508.0)   # c30 ruling 1: 464 moved to variant C (was first here)
        _ol26.setdefault("Bassoon 1", []).append({"at": list(_bnq), "lead_s": 0.06, "set": True})
        for _x in _bnq:
            _vc26.setdefault("Bassoon 1", []).append({"row": "Leg", "min": 100, "max": 100, "from": _x - 0.05, "to": _x + 0.05})
        for _e in (467.874, 479.678, 499.678, 502.648, 507.678):   # c30 ruling 1: 463.678 removed
            _ne26.setdefault("Bassoon 1", []).append({"end": _e, "tol": 0.01, "early_s": -0.09})
    INSTR_POST["cc_scale"], INSTR_POST["onset_lead"], INSTR_POST["gap_set"] = _sc26, _ol26, _gs26
    INSTR_POST["cc_shape"], INSTR_POST["note_cc"], INSTR_POST["vel_cap"], INSTR_POST["cc_cap"] = _cs26, _nc26, _vc26, _cc26
    INSTR_POST["note_end"] = _ne26
if _C26 and "rides" not in _C26_OFF:
    # Ruling 3 (C #1, simulated on the c25 master): the arrival rows of bars 91, 110, 199 begin over their crescendos (the
    # bar before the ff lowered, the ff bars unchanged); bars 205-208 +2 dB (printed f, 4-6 dB under the f of bars 11-26 on
    # the mp3); the 1023.5 row deeper into 263; bar 227 -1.5 dB
    def _r26(r_):
        q0_ = r_[0][0]
        if q0_ == 359.5:
            return [(352.0, 0.0), (354.0, 0.0), (359.9, -3.0), (360.0, -3.0), (376.0, -3.0), (376.5, 0.0)]
        if q0_ == 435.5:
            return [(427.5, 0.0), (428.0, 0.0), (432.0, -2.0), (435.9, -4.0), (436.0, -3.0), (452.0, -3.0), (452.5, 0.0)]
        if q0_ == 791.5:
            return [(783.5, 0.0), (784.0, 0.0), (788.0, -1.0), (791.9, -3.0), (792.0, -1.5), (815.5, -1.5), (816.0, 1.0),
                    (818.0, 2.0), (831.9, 2.0), (836.0, 0.0), (839.9, -1.5), (840.0, -1.5), (840.5, 0.0)]
        if q0_ == 1023.5:
            return [(1023.5, 0.0), (1024.0, -2.5), (1032.0, -3.5), (1040.0, -3.3), (1044.0, -3.5), (1047.8, -4.8), (1047.95, 0.0)]
        return r_
    RIDE_TRIMS = [_r26(r_) for r_ in RIDE_TRIMS] + [[(903.5, 0.0), (904.0, -1.5), (907.9, -1.5), (908.4, 0.0)]]

# ---------------------------------------------------------------------------------------------------------------------
# mvt3 c27 (critics' reports cycles/c27/reports/A.md, B.md, C.md on the c26 render; the coordinator's rulings 1-8).
# Dan's standing rule (11 Nov): the track volume envelope holds slow balance only. Toggles for the range tests:
#   C27=0 (block off), C27_OFF=part,part; C27_CA a|b|0 (cor anglais bars 171-186); C27_V2 marc|sus (Violins II's accented
#   chords); C27_CB lead|cc7 (the basses' pp re-bows)
_C27 = _os15.environ.get("C27", "1") == "1"
_C27_OFF = set(_os15.environ.get("C27_OFF", "").split(","))
_C27_CA = _os15.environ.get("C27_CA", "b")
_C27_V2 = _os15.environ.get("C27_V2", "marc")
_C27_CB = _os15.environ.get("C27_CB", "0")
if _C27 and "wind" not in _C27_OFF:
    # Ruling 8 (A #6): Flute 1's run on variant C (the sustain-row targets that cured the clarinet), weak targets 169.5 /
    # 170 / 173; Bassoon 1's 320 join (13-15 dB hole) joins its variant-C targets
    # (the c26 block has already run: the variant-C parts are added here and in the INSTR_POST part below)
    _C27_VC = {}
    if _C26_WIND.get("Flute 1", "0") == "0":
        _C27_VC["Flute 1"] = (169.5, 170.0, 173.0)
    if _C26_WIND.get("Bassoon 1") == "C":
        _C27_VC["Bassoon 1"] = (320.0,)
    for _t, _w in _C27_VC.items():
        ART_SPANS[_t] = [{"from": x_ - 0.1, "to": x_ + 0.1, "art": "Sus MAX"} for x_ in _w] + list(ART_SPANS.get(_t, []))
if _C27 and "ca" not in _C27_OFF and _C27_CA == "a":
    # Ruling 2 variant a (A #1 fix A): the cor anglais' slurred unison spans back on "Leg Slur MAX" (the c21 "Sus MAX" spans
    # removed); "Sus MAX" only on the notes of 2 qn or more (where c21 measured the legato bloom), led 0.06 s (c23 rule)
    ART_SPANS["Cor anglais"] = [r_ for r_ in ART_SPANS.get("Cor anglais", []) if not (r_.get("art") == "Sus MAX" and r_.get("from") in (679.9, 711.9))]
    ART_SPANS["Cor anglais"] = [{"from": x_ - 0.1, "to": x_ + 0.1, "art": "Sus MAX"} for x_ in (680.0, 688.0, 692.0, 712.0, 720.0, 728.0)] \
        + ART_SPANS["Cor anglais"]
if _C27 and CC7_POINTS is not None:
    CC7_POINTS = dict(CC7_POINTS)
    if "bal263" not in _C27_OFF:
        # Ruling 3 (B #1): the celli's held notes 1032-1047.8 at -2.5 dB in CC7 (95), in over 1032-1033, back in the
        # 1047.78-1047.89 gap
        CC7_POINTS["Violoncellos"] = list(CC7_POINTS.get("Violoncellos", [])) + [(1032.33, 111), (1032.67, 103), (1033.0, 95), (1047.84, 127)]
    if "inner" not in _C27_OFF:
        # Ruling 4 (B #2, #3): passage levels in CC7 with edges in rests: basses -3 dB under the Horn 1 counter-line
        # (263.4 in the 261-263.73 rest, back in the 319.54-319.76 rest); Horn 1 -3 dB and violas -2 dB over the
        # countersubject bars 159-165 (rests 630.89-631.79 / 630.86-631.78; back at 659.80 / 659.69); basses -4 dB under the
        # celli's p line of bars 235-237 (934.91-935.79 rest; back at the 952 note's moved onset)
        CC7_POINTS["Double basses"] = list(CC7_POINTS.get("Double basses", [])) + [(263.4, 90), (319.65, 127), (935.35, 80), (951.854, 127)]
        CC7_POINTS["Horn 1"] = list(CC7_POINTS.get("Horn 1", [])) + [(631.3, 90), (659.80, 127)]
        CC7_POINTS["Violas"] = list(CC7_POINTS.get("Violas", [])) + [(631.3, 101), (659.69, 127)]
    if _C27_CB == "cc7" and "cb" not in _C27_OFF:
        # Ruling 7 variant b (B, coordinator's checks): the basses' re-bow counter-shape in CC7 over +0.6..+1.4 s
        # (127 -> 74 / 93 / 60), the CC11 shapes off (rebow_cc11.json is skipped below)
        # (2.8 qn per second at 168 qpm: 127 at +0.45 s, the depth from +0.8 to +1.2 s, back at +1.6 s, in 4 steps a side)
        _cbr = []
        for _x, _v in ((170.859, 74), (181.676, 93), (190.533, 60)):
            _d = 20 * __import__("math").log10(_v / 127.0)
            for _j in range(5):
                _cbr.append((round(_x + 1.26 + 0.98 * _j / 4, 3), int(round(127 * 10 ** (_d * _j / 4 / 20)))))
            for _j in range(1, 5):
                _cbr.append((round(_x + 3.36 + 1.12 * _j / 4, 3), int(round(127 * 10 ** (_d * (4 - _j) / 4 / 20)))))
        CC7_POINTS["Double basses"] = sorted(list(CC7_POINTS.get("Double basses", [])) + _cbr)
if _C27 and "rides" not in _C27_OFF:
    # Ruling 4 (B, listening note 1): theme B's ff at bar 212 only 0.12 LU under the fff of 223 on the mp3: -1 dB over
    # 840.5-856
    RIDE_TRIMS = list(RIDE_TRIMS) + [[(840.0, 0.0), (840.5, -1.0), (855.9, -1.0), (856.4, 0.0)]]
    # delivery refit on the c27 render (final over 223 +0.4, bars 39 / 248 within 0.5 of the final): the 888 arrival
    # -8.4 -> -8.8 dB, bars 39 and 248 -0.6 dB (re-delivered on the c27 master: final -8.0, 223 -8.5, 263 -8.6)
    RIDE_TRIMS = [([(879.5, 0.0), (880.0, -3.5), (884.0, -5.8), (887.9, -5.8), (888.0, -8.8), (891.5, -8.8), (892.0, 0.0)] if r_[0][0] == 879.5 else r_)
                  for r_ in RIDE_TRIMS] + [[(151.5, 0.0), (152.0, -0.6), (155.9, -0.6), (156.4, 0.0)],
                                           [(987.5, 0.0), (988.0, -0.6), (991.9, -0.6), (992.4, 0.0)]]
if _C27 and INSTR_POST:
    _sc27 = {t_: [dict(r_) for r_ in v_] for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _ol27 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("onset_lead") or {}).items()}
    _cs27 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("cc_shape") or {}).items()}
    _nc27 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_cc") or {}).items()}
    _vc27 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("vel_cap") or {}).items()}
    _cc27 = {t_: [dict(r_) for r_ in v_] for t_, v_ in (INSTR_POST.get("cc_cap") or {}).items()}
    _ne27 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_end") or {}).items()}
    _gs27 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("gap_set") or {}).items()}
    if "dir" not in _C27_OFF:
        # Ruling 1 (A #2b): the soft crescendos on brass and clarinet held notes rose 1-2 dB against a falling trim: CC11
        # starts 4 dB low (k 20: CC11 is linear volume on these KS Masters) and reaches the lane at the hairpin's end
        for _t, _pts in (("Horn 1", [(323.70, -4.0), (326.40, 0.0)]),
                         ("Trombone 1", [(879.85, -4.0), (883.60, 0.0)]), ("Trombone 2", [(879.85, -4.0), (883.60, 0.0)]),
                         ("Trumpet 1", [(718.50, 0.0), (718.76, -4.0), (723.90, 0.0)]),
                         ("Clarinet 1", [(303.80, -4.0), (306.90, 0.0)]), ("Clarinet 1", [(539.85, -4.0), (547.70, 0.0)]),
                         ("Clarinet 1", [(941.90, -4.0), (944.00, 0.0)])):
            _sc27.setdefault(_t, []).append({"lane": "cc11", "k": 20.0, "pts": _pts})
        # (B #4) the stopped horns ("Stop Sus" does not answer CC1): CC11 ceilings 127 -> 50 over the sf > of 548 (Horns
        # 3-4) and 87 -> 35 over the f > p of 668 (Horns 1-2), held to the note's end; the trim no longer rises
        # (build_reaper SOFT_DECRESC_KEEP 0)
        _cc27.setdefault("Horn 3", []).append({"lane": "cc11", "pts": [(548.25, 127), (551.88, 50)]})
        _cc27.setdefault("Horn 4", []).append({"lane": "cc11", "pts": [(548.25, 127), (551.60, 50)]})
        for _t, _e in (("Horn 1", 675.66), ("Horn 2", 675.88)):
            _cc27.setdefault(_t, []).append({"lane": "cc11", "pts": [(668.20, 87), (671.90, 35), (_e, 35)]})
    if "inner" not in _C27_OFF:
        # Ruling 4 (B #2): the c25 clarinet +2 dB CC11 scale at 632-660 could not act (CC11 at its ceiling): a role instead
        for _t in ("Clarinet 1", "Clarinet 2"):
            _sc27[_t] = [r_ for r_ in _sc27.get(_t, []) if r_["pts"][0][0] != 631.7]
    if "str" not in _C27_OFF:
        # Ruling 5 (A #3, B #6): the lower strings' accented ff chords at 16 / 584 / 1104 reach their body 80-230 ms after
        # Violins I: leads 0.12 s (onset_lead, the end kept), the quarter at 15 ends 0.13 s early
        for _t in ("Violas", "Violoncellos") + (("Violins II",) if _C27_V2 == "sus" else ()):
            _ol27.setdefault(_t, []).append({"at": [16.0, 584.0, 1104.0], "lead_s": 0.12, "set": True, "rows": ("Sus",)})
        for _t in ("Violins II", "Violas", "Violoncellos"):
            _ne27[_t] = [r_ for r_ in _ne27.get(_t, []) if not (abs(r_.get("end", 0) - 16.0) < 0.01)] + [{"end": 16.0, "tol": 0.02, "early_s": 0.13}]
        # the celli's chained role edge at 15.9 (c26 window 15.852-15.872) lies in the new rest before the led chord
        ROLE_EDGE_XF["Violoncellos"] = {**ROLE_EDGE_XF.get("Violoncellos", {}), 15.9: (15.640, 15.660)}
        if _C27_V2 == "marc":
            # variant marc (B #6): Violins II's chords at 0 / 16 / 584 / 1104 on "Sus Marc LITE" with Violins I's lead and
            # velocities (92; 108 at 1104), the CC11 step 0.06 s ahead of the moved note-on (c25 A: the c24 rejection came
            # from the step landing on the note-on); no CC11 accent bump on the row
            ART_SPANS["Violins II"] = [{"from": x_ - 0.3, "to": x_ + 0.3, "art": "Sus Marc LITE", "poly": True,
                                        "vel_add": (108 if x_ == 1104.0 else 92) - (127 if x_ == 1104.0 else 111)}
                                       for x_ in (0.0, 16.0, 584.0, 1104.0)] + list(ART_SPANS.get("Violins II", []))
            _ol27.setdefault("Violins II", []).append({"at": [0.0, 16.0, 584.0, 1104.0], "lead_s": 0.085, "set": True, "rows": ("Sus Marc",)})
            _cs27["Violins II"] = [r_ for r_ in _cs27.get("Violins II", []) if not (r_.get("at") in (16.0, 584.0) and r_.get("lane") == "cc11")]
            for _x, _d in ((16.0, 17), (584.0, 16)):
                _cs27["Violins II"].append({"lane": "cc11", "at": _x, "from_note": True, "no_pre_cap": True, "pts": [(-0.06, _d), (0.085, _d), (0.09, 0)]})
        # (C #2 variant B) the soft cantabile string slur heads (pc +138..+240 ms: the recorded first-note sample) take a
        # CC11 front: +10 units from 0.06 s before the moved note-on to +0.25 s, gone by +0.45 s (longer than the 120 ms
        # CC11 fadeTime); this replaces the envelope fronts of c11 / c15 at 264 / 744 (VOL_PER_NOTE off had dropped them)
        for _t, _xs in (("Violins I", (264.0, 424.0)), ("Violins II", (264.0, 424.0, 744.0)), ("Violas", (264.0, 424.0, 744.0, 937.0)),
                        ("Violoncellos", (264.0, 424.0, 488.0))):
            for _x in _xs:
                _cs27.setdefault(_t, []).append({"lane": "cc11", "at": _x, "from_note": True, "pts": [(-0.06, 10), (0.25, 10), (0.45, 0)]})
    if "wind" not in _C27_OFF:
        for _t, _w in _C27_VC.items():   # variant C (c26): 0.06 s early, 0.011 s overlap
            _ol27.setdefault(_t, []).append({"at": list(_w), "lead_s": 0.06, "set": True, "rows": ("Sus",)})
            _gs27.setdefault(_t, []).append({"from": min(_w) - 1.0, "to": max(_w) + 0.5, "min_qn": 0.4, "gap_s": -0.011,
                                             "rows": ("Sus", "Leg"), "only_at": list(_w), "allow_leg": True})
    if "ca" not in _C27_OFF and _C27_CA == "a":
        # variant a: the "Sus MAX" notes inside the phrases start 0.06 s early (the keyswitch moves with them)
        _ol27.setdefault("Cor anglais", []).append({"at": [688.0, 692.0, 720.0, 728.0], "lead_s": 0.06, "set": True, "rows": ("Sus",)})
    if "ca" not in _C27_OFF and _C27_CA == "b":
        # Ruling 2 variant b (A #1 fix B): the cor anglais keeps "Sus MAX" (polyphonic) over the unison spans; every note
        # after the first of each span leads 0.10 s and keeps its end, so each note ends 0.10 s after the next note-on
        # (the two cross-fade)
        _ol27.setdefault("Cor anglais", []).append({"at": [683.0, 684.0, 685.0, 686.0, 687.0, 688.0, 690.0, 691.0, 692.0, 694.0,
                                                           715.0, 716.0, 717.0, 718.0, 719.0, 720.0, 723.0, 724.0, 725.0, 726.0,
                                                           727.0, 728.0], "lead_s": 0.10, "set": True})
    if "stops" not in _C27_OFF:
        # Ruling 8 (C #5): the celli ring 0.54 s past the stops of bars 2, 6, 204: the c26 cut-off ceiling (-6 dB from 0.02 s
        # before the note-off to 0.08 s after, held to the next entry)
        _cc27.setdefault("Violoncellos", []).extend([
            {"lane": "cc11", "pts": [(4.944, 98), (5.224, 72), (5.80, 72), (5.84, 105)]},
            {"lane": "cc11", "pts": [(20.944, 98), (21.224, 72), (21.80, 72), (21.84, 105)]},
            {"lane": "cc11", "pts": [(813.86, 97), (814.14, 70), (814.70, 70), (814.756, 93)]}])
    if "arr263" not in _C27_OFF:
        # Ruling 3 (C #3): Bassoon 1, Flute 2 and the bass clarinet play their fff note at 1048 4-6 dB under their last
        # quarter of bar 262 with CC11 and the trims rising (the fff sample / region is softer): CC11 +8 for the first
        # 0.5 s of the note, gone by 1.2 s (into the printed diminuendo)
        for _t in ("Bassoon 1", "Flute 2", "Bass clarinet"):
            _cs27.setdefault(_t, []).append({"lane": "cc11", "at": 1048.0, "from_note": True, "no_pre_cap": True,
                                             "pts": [(-0.02, 0), (0.03, 8), (0.50, 8), (1.20, 0)]})
    if "bn" not in _C27_OFF:
        # Ruling 8 (A #6): Bassoon 1 at 514 (v60, led 0.22 s after a half note): v100, the 0.168 qn lead of its neighbours,
        # the half note before ending 0.098 qn after the new onset
        _ol27.setdefault("Bassoon 1", []).append({"at": [514.0], "lead_s": 0.06, "set": True})
        _vc27.setdefault("Bassoon 1", []).append({"row": "Leg", "min": 100, "max": 100, "from": 513.95, "to": 514.05})
        _vc27.setdefault("Bassoon 1", []).append({"row": "Sus", "min": 100, "max": 100, "from": 513.95, "to": 514.05})
        _ne27.setdefault("Bassoon 1", []).append({"end": 513.482, "tol": 0.01, "early_s": -0.09})
    if "tpt" not in _C27_OFF:
        # Ruling 6 (A #5, C #4): the trumpets' legato targets in 984.5-999.9 8-12 dB under the slur's head: CC1 +12
        # (the dynamic layer), ceiling 110; 989's CC11 bump halved (+24 -> +12)
        for _t in ("Trumpet 1", "Trumpet 2"):
            _nc27.setdefault(_t, []).append({"lane": "cc1", "from": 984.5, "to": 999.9, "add": 12})
            _cc27.setdefault(_t, []).append({"lane": "cc1", "pts": [(984.45, 110), (999.95, 110)]})
            _cs27[_t] = [(dict(r_, pts=[(0.03, 0), (0.08, 12), (0.40, 12), (0.70, 0)]) if (r_.get("at") == 989.0 and r_.get("lane") == "cc11") else r_)
                         for r_ in _cs27.get(_t, [])]
    if "cb" not in _C27_OFF and _C27_CB == "lead":
        # Ruling 7 variant a (A #4): each new piece of the basses' pp pedal leads 0.10 s (the release cap is already 500 ms
        # at pp / p in mix.json); the old piece ends 0.03 qn before the moved onset
        _ol27.setdefault("Double basses", []).append({"at": [181.676, 190.533], "lead_s": 0.10, "set": True, "gap_s": 0.012})
    if "cb" not in _C27_OFF and _C27_CB == "cc7":
        _cs27["Double basses"] = [r_ for r_ in _cs27.get("Double basses", []) if r_.get("at") not in (170.859, 181.676, 190.533)]
    if "vc951" not in _C27_OFF:
        pass   # (celli 951.5 / 870.4: carried by DYN_TRIM_TO_CC7, see CHANGES)
    INSTR_POST["cc_scale"], INSTR_POST["onset_lead"], INSTR_POST["cc_shape"], INSTR_POST["note_cc"] = _sc27, _ol27, _cs27, _nc27
    INSTR_POST["vel_cap"], INSTR_POST["cc_cap"], INSTR_POST["note_end"], INSTR_POST["gap_set"] = _vc27, _cc27, _ne27, _gs27

# ---------------------------------------------------------------------------------------------------------------------
# mvt3 c28 (critics' reports cycles/c28/reports/A.md, B.md, C.md on the c27 render; the coordinator's rulings 1-8).
# Toggles: C28=0 (block off), C28_OFF=part,part; C28_LSA=1 (ruling 7 variant A: "Leg Slur Accent MAX" on the accented
# slur heads, range test)
_C28 = _os15.environ.get("C28", "1") == "1"
_C28_OFF = set(_os15.environ.get("C28_OFF", "").split(","))
_C28_LSA = _os15.environ.get("C28_LSA", "0") == "1"
if _C28 and CC7_POINTS is not None and "bal" not in _C28_OFF:
    # Ruling 4 (B #3): the bass clarinet's held A flat 1 is the loudest stem of bar 261 (+6 dB velocity step at 1040):
    # CC7 81 (-3.9 dB) over 1039.70-1047.87, both edges in existing gaps
    CC7_POINTS = dict(CC7_POINTS)
    CC7_POINTS["Bass clarinet"] = list(CC7_POINTS.get("Bass clarinet", [])) + [(1039.70, 81), (1047.87, 127)]
if _C28 and INSTR_POST:
    _sc28 = {t_: [dict(r_) for r_ in v_] for t_, v_ in INSTR_POST.get("cc_scale", {}).items()}
    _cs28 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("cc_shape") or {}).items()}
    _nc28 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_cc") or {}).items()}
    _cc28 = {t_: [dict(r_) for r_ in v_] for t_, v_ in (INSTR_POST.get("cc_cap") or {}).items()}
    _gs28 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("gap_set") or {}).items()}
    _vs28 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("vol_set") or {}).items()}
    _gf28 = {t_: dict(v_) for t_, v_ in (INSTR_POST.get("gap_floor") or {}).items()}
    if "solo" not in _C28_OFF:
        # Ruling 3 (A #2): Trumpet 1's open solo, bars 51-66: each slur head swells 9 dB (CC1 36 -> 50) and the legato
        # targets sit 4-8 dB under it: the heads' CC1 capped at start + 6 (42), the targets CC1 +4 (to the crescendo 239)
        _cc28.setdefault("Trumpet 1", []).extend([{"lane": "cc1", "pts": [(199.80, 42), (202.78, 42)]},
                                                  {"lane": "cc1", "pts": [(215.85, 43), (218.78, 43)]},
                                                  {"lane": "cc1", "pts": [(231.85, 43), (234.78, 43)]}])
        for _a, _b in ((202.5, 215.0), (218.5, 231.0), (234.5, 239.0)):
            _nc28.setdefault("Trumpet 1", []).append({"lane": "cc1", "from": _a, "to": _b, "add": 4})
    if "tpt" not in _C28_OFF:
        # Ruling 3 (A #4, B #5, C #3): Più allegro slur 984-999: the c27 CC1 +12 -> +6; 989 (tenuto) loses its CC11 bump
        # and takes CC1 -12 / -6 (Trumpet 1 / 2) held to the 991 note-on; 991 CC11 -5 dB (k 20) over its note
        for _t, _u in (("Trumpet 1", -12), ("Trumpet 2", -6)):
            _nc28[_t] = [(dict(r_, add=6) if (r_.get("lane") == "cc1" and r_.get("from") == 984.5 and r_.get("add") == 12) else r_)
                         for r_ in _nc28.get(_t, [])]
            _nc28[_t].append({"lane": "cc1", "from": 988.9, "to": 989.1, "add": _u})
            _cs28[_t] = [r_ for r_ in _cs28.get(_t, []) if not (r_.get("at") == 989.0 and r_.get("lane") == "cc11")]
            _sc28.setdefault(_t, []).append({"lane": "cc11", "k": 20.0, "pts": [(990.64, 0.0), (990.70, -5.0), (991.75, -5.0), (991.80, 0.0)]})
        # (A #5) Trombone 1's accented dotted quarters 984-1080 cut to a quarter by the 0.12 s floor (9 dB holes): 0.05 s
        _gs28.setdefault("Trombone 1", []).append({"from": 984.0, "to": 1080.0, "min_qn": 0.95, "gap_s": 0.05})
        _g = dict(_gf28.get("Trombone 1") or {})
        _g["skip_long"] = list(_g.get("skip_long", [])) + [(984.0, 1080.0, 0.95)]
        _gf28["Trombone 1"] = _g
    if "gate" not in _C28_OFF:
        # Ruling 2 (gate items): the bassoons' 596 vol_set row released inside the ff note at 600 (1.7 -> 0 dB over
        # 600-601.65): the row holds 0 from 599 to 601.8 (as the cor anglais in c21)
        for _t in ("Bassoon 1", "Bassoon 2", "Contrabassoon"):
            _vs28[_t] = [r_ for r_ in _vs28.get(_t, []) if r_["pts"][0][0] != 596.0] + [
                {"pts": [(596.0, None), (599.0, 0.0), (601.8, 0.0), (601.85, None)]}]
        # the harp's printed dynamic at 952 stepped the envelope 2.9 dB inside ringing notes (no rest from 936 on; the
        # harp has no CC7 path): the step becomes a printed-dynamic ramp over 952-956.5 (1.7 dB/s at 128-134 qpm)
        # (range of the data: the pipeline's vol_guard stretched the compensating rise to 950.1-951.4, ahead of the trim
        # step, so the harp row is off; the harp's 2.9 dB step at the 952 chord is left and reported)
        if _os15.environ.get("C28_HARP", "0") == "1":
            _vs28.setdefault("Harp", []).append({"pts": [(951.9, None), (952.0, 0.48), (956.5, None)]})
    if "stops" not in _C28_OFF:
        # Ruling 6 (C #4): the celli stop ceilings at bars 6 and 204 at half their c27 depth (98 -> 85, 97 -> 84)
        _cc28["Violoncellos"] = [
            ({"lane": "cc11", "pts": [(20.944, 98), (21.224, 85), (21.80, 85), (21.84, 105)]} if r_.get("pts", [[0]])[0][0] == 20.944 else
             {"lane": "cc11", "pts": [(813.86, 97), (814.14, 84), (814.70, 84), (814.756, 93)]} if r_.get("pts", [[0]])[0][0] == 813.86 else r_)
            for r_ in _cc28.get("Violoncellos", [])]
    INSTR_POST["cc_scale"], INSTR_POST["cc_shape"], INSTR_POST["note_cc"], INSTR_POST["cc_cap"] = _sc28, _cs28, _nc28, _cc28
    INSTR_POST["gap_set"], INSTR_POST["vol_set"], INSTR_POST["gap_floor"] = _gs28, _vs28, _gf28
if _C28 and CC7_POINTS is not None and INSTR_POST and "gate" not in _C28_OFF:
    # Ruling 2 (A #6): two envelope rises at slurred joins (no rest near) become a level step at the new note-on: CC7
    # holds the old level through the old note (compensating the envelope) and returns over +-0.05 qn of the note-on
    def _c28_comp(a_, b_, on_, diff_):
        """CC7 points: -diff_(q) dB over [a_, on_ - 0.05], back to 127 at on_ + 0.05"""
        pts_, q_ = [], a_
        while q_ < on_ - 0.05 - 1e-6:
            pts_.append((round(q_, 4), int(round(127 * 10 ** (-max(0.0, diff_(q_)) / 20)))))
            q_ += 0.025
        pts_.append((round(on_ - 0.05, 4), int(round(127 * 10 ** (-max(0.0, diff_(on_ - 0.05)) / 20)))))
        v_ = pts_[-1][1]
        for j_ in range(1, 5):
            pts_.append((round(on_ - 0.05 + 0.025 * j_, 4), int(round(v_ + (127 - v_) * j_ / 4))))
        return pts_
    CC7_POINTS = dict(CC7_POINTS)
    # Oboe 1, 851.46-851.69: the envelope's +3.0 dB (vol 1.5 -> 4.5) before the led 852 note-on (851.712)
    CC7_POINTS["Oboe 1"] = sorted(list(CC7_POINTS.get("Oboe 1", [])) + _c28_comp(
        851.462, 851.692, 851.712, lambda q_: 0.0 if q_ < 851.462 else min(3.0, 3.0 * (q_ - 851.462) / 0.23)))
    # Violas, 775.26-775.95: the mp after the decrescendo rose 2.6 dB inside the Leg BC note: the envelope reaches the mp
    # level by 775.20 (vol_set), CC7 keeps the decrescendo's level to the note-on 775.263
    _vs = dict(INSTR_POST.get("vol_set") or {})
    _vs["Violas"] = list(_vs.get("Violas", [])) + [{"pts": [(774.75, None), (775.20, -2.47), (775.945, -2.47)]}]
    INSTR_POST["vol_set"] = _vs
    def _va_diff(q_):
        orig_ = -4.15 + (-5.04 + 4.15) * (q_ - 774.75) / (775.2629 - 774.75)
        new_ = -4.15 + (-2.47 + 4.15) * min(1.0, (q_ - 774.75) / 0.45)
        return new_ - orig_
    CC7_POINTS["Violas"] = sorted(list(CC7_POINTS.get("Violas", [])) + _c28_comp(774.75, 775.24, 775.2629, _va_diff))
if _C28 and "rides" not in _C28_OFF:
    # Ruling 5 (C #2 variant v6; B #6): bar 223 only 0.7 dB over the chorale's bar 228 on the mp3: -2 dB over 900-912
    # (keeps the c24 chorale entry over the trumpet solo of bars 61-62, which B's 892-901 +1 would have lowered); the
    # Largamente 271-273 3-4 dB under bar 255: the 1079.5 row eased to -2.0 over 1080-1096
    RIDE_TRIMS = [([(1079.5, 0.0), (1080.0, -2.0), (1088.0, -2.0), (1092.0, -2.0), (1096.0, -2.0), (1104.0, -3.0), (1107.8, -3.5), (1107.95, 0.0)]
                   if r_[0][0] == 1079.5 else r_) for r_ in RIDE_TRIMS] + [[(899.5, 0.0), (900.0, -2.0), (911.9, -2.0), (912.5, 0.0)]]

# ---------------------------------------------------------------------------------------------------------------------
# mvt3 c29 (critics' reports cycles/c29/reports/A.md, B.md, C.md on the c28 render; the coordinator's rulings 1-8).
# Toggles: C29=0 (block off), C29_OFF=part,part (t243, ca, hn, solo43, ob95, tpt, pick, bn320, rides)
_C29 = _os15.environ.get("C29", "1") == "1"
_C29_OFF = set(_os15.environ.get("C29_OFF", "").split(","))
# Ruling 1 (A #1-#3; the c27 cor anglais "variant b" form): slurred joins that dip 8-12.5 dB on "Leg Slur MAX" (or start
# late as the legato row's first note after a Sus-row head) play on the sustain row; each note after the first leads
# 0.10 s and keeps its end, so it overlaps the next note-on by about 0.10 s (polyphonic Sus rows cross-fade)
_C29_SUS = {}   # track: [(from, to, row, [onsets led], velocity or None)]
if _C29 and "t243" not in _C29_OFF:
    # bar 243 "molto espr.": Trumpets 1-2 and Horn 1, slur 968-983 (the head 968 is already on the Sus row)
    for _t, _row in (("Trumpet 1", "Sus Non Vib MAX"), ("Trumpet 2", "Sus Non Vib MAX"), ("Horn 1", "Sus MAX")):
        _C29_SUS.setdefault(_t, []).append((969.4, 983.5, _row, [970.0, 973.0, 978.0], 95))
if _C29 and "ca" not in _C29_OFF:
    # cor anglais 696-706 and 731-740 (the heads 696 / 731 lead as before; 708 / 738 already on Sus MAX since c23)
    _C29_SUS.setdefault("Cor anglais", []).extend([
        (698.9, 707.0, "Sus MAX", [699.0, 700.0, 701.0, 702.0, 703.0, 704.0, 706.0], None),
        (730.9, 741.0, "Sus MAX", [732.0, 733.0, 734.0, 735.0, 736.0, 740.0], None)])
if _C29 and "hn" not in _C29_OFF:
    # accented brass slurs (F1 head motive, "ben marc."): the notes after the Sus-row head (Horn 1's slur-ending staccato
    # 76 / 820 stays on "Marc Shrt RRx4")
    # (range test VAR against CTRL: Horn 1 at 818 stem dip 3.7 -> 4.4 dB, master 819.5 3.3 -> 4.4, front +10.5 -> +15.3:
    # rejected, 818 stays on the legato row; 74 / 146 / 578 adopted)
    _C29_SUS.setdefault("Horn 1", []).extend([(73.9, 75.6, "Sus MAX", [74.0, 75.5], 90)])
    _C29_SUS.setdefault("Horn 3", []).extend([(145.9, 148.1, "Sus MAX", [146.0, 147.5, 148.0], 90),
                                              (577.9, 580.1, "Sus MAX", [578.0, 579.5, 580.0], 90)])
for _t, _rows in _C29_SUS.items():
    ART_SPANS[_t] = [{"from": a_, "to": b_, "art": r_} for a_, b_, r_, _, _ in _rows] + list(ART_SPANS.get(_t, []))
if _C29 and INSTR_POST:
    _ol29 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("onset_lead") or {}).items()}
    _vc29 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("vel_cap") or {}).items()}
    _nc29 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("note_cc") or {}).items()}
    _cc29 = {t_: [dict(r_) for r_ in v_] for t_, v_ in (INSTR_POST.get("cc_cap") or {}).items()}
    _vs29 = {t_: list(v_) for t_, v_ in (INSTR_POST.get("vol_set") or {}).items()}
    for _t, _rows in _C29_SUS.items():
        for a_, b_, r_, at_, v_ in _rows:
            _ol29.setdefault(_t, []).append({"at": list(at_), "lead_s": 0.10, "set": True})
            if v_ is not None:
                _vc29.setdefault(_t, []).append({"row": "Sus", "min": v_, "max": v_, "from": a_, "to": b_})
    if "solo43" not in _C29_OFF:
        # Ruling 2 (B #1; manual p.92: Sustain at pp with CC1 at 0 for a section without a harmonics patch): Violins I's
        # printed "harm." B flat 5 over bars 43-50 on the non-vibrato layer (cap from the rest before its led note-on)
        _cc29.setdefault("Violins I", []).append({"lane": "cc1", "pts": [(167.30, 0), (198.90, 0)]})
    if "tpt" not in _C29_OFF:
        # Ruling 6 (A #5, B #4): Trumpet 1's tenuto 989 CC1 -12 -> -7 (2.0 dB under its neighbours in c28)
        _nc29["Trumpet 1"] = [(dict(r_, add=-7) if (r_.get("lane") == "cc1" and r_.get("from") == 988.9 and r_.get("add") == -12) else r_)
                              for r_ in _nc29.get("Trumpet 1", [])]
    if "pick" not in _C29_OFF:
        # Ruling 6 (A #4): the eighth pickups into the accented quarters (bars 91-92, 277) merged with them (0.7-2.7 dB): the
        # quarters lead 0.02 s (was 0.05), the pickups v95 -> 82 (layer 76-94 of "Stac DblTng RRx9", c23 table)
        for _t in ("Trumpet 1", "Trumpet 2", "Trumpet 3"):
            _ol29.setdefault(_t, []).append({"at": [362.0, 366.0, 1106.0], "lead_s": 0.02, "set": True, "rows": ("Sus",)})
            for _x in (361.5, 365.5, 1105.5):
                _vc29.setdefault(_t, []).append({"row": "Stac", "min": 82, "max": 82, "from": _x - 0.05, "to": _x + 0.05})
    if "bn320" not in _C29_OFF:
        # Ruling 8 (A #6): Bassoon 1's 320 note rose 2.9 dB inside it (the decrescendo's undershoot returning to the p
        # level): the envelope reaches the p level in the rest before the led note-on (319.63-319.86) and holds
        _vs29.setdefault("Bassoon 1", []).append({"pts": [(319.64, None), (319.70, "at:320.6"), (320.60, "at:320.6")]})
    if "hn" not in _C29_OFF:
        # (Horn 3 578: the +3 dB step at 578 now falls inside the head's crossfade tail; vol_guard had put it 0.003 qn
        # before the led note-on in c28: the same place, by hand)
        _vs29.setdefault("Horn 3", []).append({"pts": [(577.62, None), (577.655, "at:577.98"), (577.98, "at:577.98")]})
    INSTR_POST["onset_lead"], INSTR_POST["vel_cap"], INSTR_POST["note_cc"] = _ol29, _vc29, _nc29
    INSTR_POST["cc_cap"], INSTR_POST["vol_set"] = _cc29, _vs29
if _C29 and "rides" not in _C29_OFF:
    # Ruling 4 (B #2, C #5): the 1079.5 row stepped to -2 dB exactly at the ff arrival of bar 271: 0 to 1083.5, -1 from 1084
    RIDE_TRIMS = [([(1079.5, 0.0), (1083.5, 0.0), (1084.0, -1.0), (1096.0, -1.0), (1104.0, -3.0), (1107.8, -3.5), (1107.95, 0.0)]
                   if r_[0][0] == 1079.5 else r_) for r_ in RIDE_TRIMS]
if _C29 and "solo43" not in _C29_OFF:
    # Ruling 2 (B #1): +1 dB on the transition's delivery ride over the solos of bars 43-50 (the pad is lowered by roles)
    RIDE_TRIMS = list(RIDE_TRIMS) + [[(166.0, 0.0), (168.0, 1.0), (198.0, 1.0), (199.9, 0.0)]]

# ---- mvt3 c30 (last cycle; coordinator's rulings on the c29 render; env C30_OFF="bn,rides" turns parts off) ----
_C30_OFF = set(_os15.environ.get("C30_OFF", "").split(","))
if "rides" not in _C30_OFF:
    # Ruling 2 (C #1, simulated on the c29 master): bars 95-98 (mf -> p under the oboe solo) were the softest bars of the
    # mp3 after the c29 roles (4-8 LU under the p trumpet solo of bars 51-66): +3.5 dB delivery ride over the passage,
    # from the oboe's entry to the gap before bar 99 (the roles stay)
    RIDE_TRIMS = list(RIDE_TRIMS) + [[(376.25, 0.0), (376.75, 3.5), (391.5, 3.5), (391.9, 0.0)]]
    # Ruling 3 (C #4, simulated): the opening ff chords (bars 1-2, 5-6) within 0.6 LU of the fff at bar 223: -1 dB more
    # on top of the existing -2.5 dB rows (rows add in deliver_master.py)
    RIDE_TRIMS += [[(0.0, -1.0), (8.0, -1.0), (8.25, 0.0)], [(15.75, 0.0), (16.0, -1.0), (24.0, -1.0), (24.25, 0.0)]]
