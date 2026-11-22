"""Movement III (Scherzo) score config for score_to_parts.py, series 1 (score symphony/scherzo/v600), c00 port.

Run in score_to_parts.py's namespace (S, W, B, H, P, DYN and every default table are available). Score qn: 3/4
throughout, bar b starts at qn 3 (b - 1); the last release is qn 1128 (bar 376 ends). Allegro vivace 2. = 88 (quarter
264), Trio "Un poco meno mosso" 2. = 76 (quarter 228) from bar 153, Tempo I from 253, Piu mosso 2. = 96 from 325, Meno
mosso (tempo del Trio) 2. = 76 from 341.

Port (2026-11-07): tracks as Movement I series 2 (symphony/mvt1/reaper-v621, same instrumentation) minus its percussion
and Trumpet 3 (both tacet here), plus the divisi / solo / harmonics tracks the scherzo needs (below). The generic-rule
settings are Movement I's (an Allegro; its settings of generic rules that are not keyed to its own onsets), with
Movement II's later generic settings (horn CC1 map of mvt2 c31). Every per-onset table starts empty: the loop's actors
add to them. See README.md "Port" and cycles/c00/PORT.md for each decision."""
SCORE_END = 1128.0
SCORE_TITLE = "scherzo-mockup"   # REAPER item names and the mp3 name (cycles/cNN/scherzo-mockup-cNN.mp3)

# track name, source staves (mockup.ly staff names), patch file, family, pan (superseded by the seat in build/mix.json).
# Stem numbers follow this order; append new tracks at the end so earlier stems keep their numbers.
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
    ("Trombone 1", ["Tbn1"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.35),
    ("Trombone 2", ["Tbn2"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.4),
    ("Bass trombone", ["BTbn"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.45),
    ("Tuba", ["Tuba"], B + "Solo Tuba/06 Keyswitch/1TU KS Master.oib", "brass", 0.5),
    ("Timpani", ["Timp"], P + "Drums/Timpani/Timpani Flt KS.oib", "timp", 0.0),
    ("Harp", ["HarpR", "HarpL"], H + "01 Maestro Patches/Harp Sus RR.oib", "harp", -0.55),
    ("Violins I", ["VlnI"], S + "1st Violins/06 Keyswitch/1st Violins KS Master.oib", "string", -0.6),
    ("Violins II", ["VlnII"], S + "2nd Violins/06 Keyswitch/2nd Violins KS Master.oib", "string", -0.3),
    ("Violas", ["Vla"], S + "Violas/06 Keyswitch/Violas KS Master.oib", "string", 0.15),
    ("Violoncellos", ["Vc"], S + "Celli/06 Keyswitch/Celli KS Master.oib", "string", 0.4),
    ("Double basses", ["Cb"], S + "Basses/05 Keyswitch/Basses KS Master.oib", "string", 0.6),
    # c00 port: the harp harmonics (bars 149-152 "harm.", Hp R.H. B and L.H. E-G sharp chords; bar 375 the closing chord)
    # on Harp Harmonics (Movement II's track). The score's \harmOct sets \transposition c'' around them, so the MIDI
    # pitches already sound an octave above the written notes; HARM_ALL_PITCHES keeps every chord note
    ("Harp harmonics", ["HarpR", "HarpL"], H + "02 Individual Articulation Patches/Harp Harmonics.oib", "harm", -0.55),
    # c00 port: bars 349-356 "dolce, solo (gli altri tacet)" on the half-section 1st Violins KS Master DIV A (Movement II's
    # Violin I solo track; no solo violin library is installed). TRACK_WINDOWS routes the notes
    ("Violin I solo", ["VlnI"], S + "1st Violins Divisi/06 Keyswitch/1st Violins KS Master DIV A.oib", "string", -0.6),
    # c00 port: the violas' "div." passages (bars 209-224 tenuto thirds and fourths under the trio tune's return; bars
    # 349-356 under the solo violin) on the half-section Violas KS Master DIV B (Movement II's Violas div track).
    # TRACK_SPLITS routes the upper note of each pair. The "non div." double stops (bars 72, 105-120, 300, 305-320, 339)
    # stay on the section
    ("Violas div", ["Vla"], S + "Violas Divisi/06 Keyswitch/Violas KS Master DIV B.oib", "string", 0.15),
]

TRACK_WINDOWS = {"Violin I solo": (1044.0, 1068.0, True), "Violins I": (1044.0, 1068.0, False)}
TRACK_SPLITS = {"Violas div": ("Violas", [(624.0, 672.0), (1044.0, 1068.0)], "rank")}
# c00 port: Vln II "la metà" (bar 349) is read as metà (META_DB) to the end; no "tutti" follows in the part
HARM_ALL_PITCHES = True

# Printed tempo changes (global.ily \mt steps in the MIDI) smoothed into 0.25 qn ramps: (start qn, end qn, tempo at the
# start, quarter bpm). bar 149-152 poco rit. (252/240/232/228 into the Trio's 228); bars 237-252, the Trio's poco rit.
# (222/214/206/198) and the poco a poco accelerando (198-254, every two bars) into Tempo I at 253, one span as the
# score's c113 comment asks ("one tempo curve through 237-253"); bars 370-375 rit. (210/196/180/160/140).
# Left as printed steps: the bar-2 fermata (bar 2 at quarter 88: Hn 1's held G sharp and the violins' held ppp G sharp,
# no onset inside the bar, so a step lengthens the fermata without bending any rhythm), the G.P. bar 340 (quarter 96,
# silence) and the last bar 376 (quarter 50, the final fermata on Hn 1's G sharp). The Trio, Tempo I, Piu mosso and
# Meno mosso are printed tempo changes (steps). "ritmo di tre battute" (bar 89) and "ritmo di quattro battute" (bar
# 101) are phrase groupings with no tempo change (\mt 264): nothing in the tempo map; listed in RITMO_BATTUTE for the loop
RAMP_SPANS = [(444, 456, 264), (708, 756, 228), (1107, 1125, 228)]
RITMO_BATTUTE = [(264.0, 300.0, 3), (300.0, 312.0, 4)]   # (from qn, to qn, bars per group); read by no tool

# Printed "sul A" text spans (TextSpanner, not in the event list's texts; logged as "textspan" by build/mockup.ly):
# score qn of the first and last note (inclusive). CC70 rests at 127 (FP4) outside them (mvt1 c38-c41)
SUL_SPANS = {"Violins I": [(0.0, 23.0, "a"), (528.0, 538.0, "a"), (1089.0, 1125.0, "a")],
             "Violins II": [(364.0, 383.5, "a"), (839.5, 851.5, "a"), (1044.0, 1054.0, "a")]}
SUL_DEFAULT_CC70 = 127
SUL_FP4_CC70 = 127

# ---------- generic rules: Movement I's settings (symphony/mvt1/reaper-v621/build/score_config.py, c43) ----------
# Only settings that are not keyed to Movement I's onsets or bars, and only family- or patch-level entries of mixed
# tables (track entries that answered one Movement I passage are left out). The values were fitted on Movement I's
# Allegro (quarter 126); the scherzo runs at quarter 264, so lead and gap rules in seconds take a larger share of each
# note here: the c01+ critics should check them first.
ACCENT_BODY_S_SHORT = (0.18, 0.28)
BREATH_FALL_BY = {"Horn": 10}
BREATH_SPLIT = dict(BREATH_SPLIT, dip_db=-1.5)
# brass and clarinet dynamics on CC1 (kit README "Starting a new mockup" 5; mvt1 c30-c32, mvt2 c30), the horn CC1 map
# of mvt2 c31 (soft horn legato transitions: keep horn CC1 at 57 or more, soft levels from the volume envelope)
CC1_DYN_TRACKS = ("Horn", "Trumpet", "Trombone", "Bass trombone", "Tuba", "Clarinet ")
CC1_HOLD = {"Contrabassoon": 40}
CC1_DYN_MAP_BY = {"Horn": [(22, 57), (34, 60), (46, 64), (58, 68), (72, 72), (88, 86), (114, 108), (124, 120)]}
CUTOFF_EARLY_S = {"string": 0.05, "brass": 0.04}
DETACH_LEAD_KEEP_QN = 0.15
DYN.update({"mp+": 65, "mf-": 68, "mf+": 78, "f-": 84})
ENTRY_LEAD_ART_S = {"wind": {"Leg Slur MAX": 0.055, "Leg Slur": 0.055, "Sus Non Vib": 0.035},
                    "brass": {"Leg Slur MAX": 0.02}, "Bassoon": {}, "Contrabassoon": {},
                    "Flute": {"Leg Slur MAX": 0.055, "Leg Slur": 0.055, "Sus Non Vib": 0.035, "Sus MAX": 0.04},
                    "Oboe": {"Leg Slur MAX": 0.055, "Leg Slur": 0.055, "Sus Non Vib": 0.035, "Sus MAX": 0.04}}
ENTRY_LEAD_S = dict(ENTRY_LEAD_S, **{"string": (0.12, 0.06, 0.12), "brass": (0.06, 0.05), "Bassoon": (0.06, 0.06),
                                     "Contrabassoon": (0.06, 0.06), "Double basses": (0.12, 0.06)})
GENTLE_ACCENT = {
    "brass": {"arts": ("Sus MAX", "Sus Max", "Sus Non Vib MAX", "Sus Vib MAX", "Sus Non Vib"), "db": 2.5, "soft_db": 2.5,
              "swell_s": (0.03, 0.15, 0.4), "keep_legato": True, "swell_s_leg": (0.03, 0.22, 0.5)},
    "wind": {"arts": ("Sus MAX", "Sus Max", "Sus Non Vib"), "db": 3.5, "soft_db": 2.0, "swell_s": (0.03, 0.15, 0.4),
             "keep_legato": True, "swell_s_leg": (0.03, 0.22, 0.5)},
    "string": {"arts": ("Sus MAX",), "db": 3.0, "soft_db": 2.0, "swell_s": (0.03, 0.15, 0.4),
               "swell_s_leg": (0.03, 0.22, 0.5)}}
HARP_RING_S = 2.0
HELD_DECRESC_DB = {"wind": 3.0, "string": 3.0}
HP_NIENTE = {"steps": 2, "rest_qn": 1.0}
HP_SF_TARGET = {"staves": ("Hn1", "Hn2", "Hn3", "Hn4", "Tpt1", "Tpt2", "Tbn1", "Tbn2", "BTbn", "Tuba"), "to": "f", "from_f": "ff"}
LEG_JOIN_TRIM_HOLD = {"wind": (0.04, 0.08), "brass": (0.06, 0.08), "string": (0.06, 0.08), "Oboe 1": (0.02, 0.06),
                      "Oboe 2": (0.02, 0.06)}
LEG_LEAD_S = dict(LEG_LEAD_S, **{"Violin I solo": 0.12, "Violins II": 0.2, "Violas": 0.2, "string": 0.17, "brass": 0.1,
                                 "Oboe": 0.05, "Bassoon": 0.06, "Bass clarinet": 0.05, "Cor anglais": 0.05, "Flute": 0.03,
                                 "Clarinet": 0.05, "wind": 0.0, "Horn": 0.06})
LEG_MIN_GAP_S = {"Violoncellos": 0.1, "Violas": 0.1, "Violins II": 0.1, "Violins I": 0.06}
LEG_VEL_EXTRA_S = {"Bass clarinet": (70, 0.09), "Oboe": (70, 0.05), "wind": (70, 0.04)}
LEG_ART_EXTRA_S = {"Violins II": {"Leg Slur MAX": 0.04, "Leg BC MAX": 0.0},
                   "Violoncellos": {"Leg Slur MAX": 0.05, "Leg BC MAX": -0.02},
                   "Violas": {"Leg Slur MAX": 0.025, "Leg BC MAX": 0.05},
                   "Violins I": {"Leg BC MAX": 0.05}}
LEG_CAP_FRAC = {t_: [(0.0, SCORE_END, 0.75)] for t_ in ("Violins I", "Violins II", "Violas", "Violoncellos")}
METRIC_BOWED_REP = True
METRIC_TIMP_DB = {"down": 0.0, "mid": -1.0, "beat": -2.0, "off": -3.0, "min_cc": 88}
TIMP_METRIC_VEL = {"down": 0, "mid": -3, "beat": -5, "off": -9, "jit": 2, "min_cc": 88}
PICKUP_LIFT_TAIL_S = {"wind": (0.04, 0.08), "brass": (0.06, 0.08), "Oboe 1": (0.02, 0.06), "Oboe 2": (0.02, 0.06),
                      "string": (0.06, 0.08)}
PORTATO_TAIL_JOIN = True
REP_ROW_GAP_S = (0.06, 0.15)
REP_ROW_REPEATS_ONLY = ("brass",)
RETONGUE_LEAD_S = dict(RETONGUE_LEAD_S, **{"brass": 0.05, "wind": 0.035, "Violins II": 0.1, "Violins I": 0.1,
                                           "Violas": 0.1, "Violoncellos": 0.1})
RETONGUE_LEAD_SLOW_S = {"Bassoon": 0.06, "string": 0.07, "wind": 0.04, "brass": 0.05}
# per-row level trims of the string KS Masters (sample properties: these rows play louder than the section's others)
ROW_TRIM_DB = {"Violins II": {"Sus MAX": (-4.0, 80)},
               "Violas": {"Sus MAX": (-4.5, 80), "Stac RRx9": (-4.0, 80)},
               "Violoncellos": {"Sus MAX": (-1.5, 80), "Stac RRx9": (-4.0, 80)},
               "Violins I": {"Sus MAX": (-1.5, 80), "Staccatissimo RRx9": (-3.0, 80)}}
SLUR_HEAD_LEAD = {"string": True, "lead_s": 0.1}
SLUR_PAIR_RELEASE = dict(SLUR_PAIR_RELEASE, short_s=0.35, full_short_s=0.12, join_db=-3.0)
SLUR_START_SUS = {"families": ("wind", "brass"), "max_qn": 0.6, "after_qn": 0.15}
STAC_LEAD_S = {"Violins I": 0.045, "Violas": 0.04, "Violins II": 0.035, "Violoncellos": 0.025, "Cor anglais": 0.03}
# 1st Violins: "Staccatissimo RRx9" plays the "V1 Stac" samples (row names swapped in the patch; mvt1 c36)
STAC_ROW = {"Violins I": "Staccatissimo RRx9"}
STR_REP_AFTER_STAC = {"max_qn": 1.0, "max_gap_qn": 0.5}
SYNCO_SHAPE = {"families": ("string",), "min_bpm": 100, "rest_qn": 0.25, "len_qn": (0.75, 2.5),
               "pts": [(-0.12, 6.0), (0.1, 6.0), (0.25, 3.0), (0.45, 0.0), (0.6, -3.0)]}
TIMP_CC1_MAP = [(22, 56), (34, 56), (46, 60), (58, 66), (72, 72), (88, 88), (114, 104), (124, 122)]
TIMP_DELAY_S = 0.02
TIMP_RH_ALT = {"max_gap_s": 0.8, "add": 24}
TIMP_ROLL_TRIM_DB = [(22, 17.6), (34, 19.0), (46, 18.6), (58, 12.7), (72, 9.5), (88, 7.3), (114, 3.7), (124, 0.0)]
TREM_ENTRY_LEAD_S = 0.04
TREM_JOIN_LEAD_S = 0.22
TREM_SPLIT = dict(TREM_SPLIT, clear_qn=1.0)
UNI_DELAY_FADE = (-12.0, 0.2)
UNI_DELAY_OVERLAP_QN = 0.25
WIND_DETACH = {"gap_s": 0.05, "frac": 0.12,
               "by": {"brass": {"gap_s": 0.09, "frac": 0.18, "dip_db": -5.0, "dip_fall_s": 0.05, "dip_min_cc": 84}}}
WIND_REP_PORTATO = True
WIND_REP_RETONGUE_BY = {"Horn": {"gap_s": 0.1, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15},
                        "Trombone": {"gap_s": 0.08, "fall_cc": 10}}
WIND_REP_RETONGUE_SHORT = {"max_qn": 0.5, "min_bpm": 100.0, "gap_s": 0.1, "frac": 0.45, "fall_cc": 8}
WIND_WIDE_LEG = 12
# Harp Sus RR per-pitch velocity offsets (sample unevenness, measured on Movement I's renders)
HARP_PITCH_VEL = {55: -6, 56: -12, 58: 5, 60: 5, 61: 9, 63: 0, 64: -8, 65: -12, 66: -12, 67: 6, 68: -9, 70: -12,
                  72: -7, 73: 12, 75: -12, 76: -10, 77: -12, 78: 12, 81: 12, 82: 12, 83: 10, 84: 10, 85: -12, 86: 12,
                  87: 12, 88: 12, 89: 12, 92: 5, 94: 12, 96: 4, 97: 12}
# the fp / sfp attack: (attack dynamic, held to qn, at p by qn). Movement I's default 0.12 / 0.25 qn is 57 / 119 ms at
# its quarter 126; at the scherzo's quarter 264 the same times are 0.25 / 0.5 qn (Movement II, quarter 52, set 0.2 / 0.4)
FP_SPIKE = ("f", 0.25, 0.5)
CC1_HOLD = dict(CC1_HOLD, **{"Violin I solo": 72})   # mvt2 c32: DIV A solo CC1 held in the Sus Vib set

# ---------- c01 (actor, on the c00 render; cycles/c01/CHANGES.md) ----------
# critic A #1: the accented note after the theme head's staccatos (and the fff summit downbeat, bar 336) started a slur
# on Leg Slur MAX after a Stac-row note, so it played the slow first-note layer: Violins I median -3.1 dB under the
# staccato before it (p statements -8..-14 dB, summit -15 dB; master bar 336 under bar 337). Fresh Sus MAX strokes
# (the DOWNBOW_STROKE_AT path: entry lead, REBOW_VEL_BY_CC velocity, no delayed-vibrato dip); the next slurred note joins
# from the stroke as a Leg BC target
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{
    "Violins I": [39.0, 51.0, 69.0, 75.0, 111.0, 123.0, 207.0, 213.0, 285.0, 300.0, 315.0, 327.0, 345.0, 351.0, 759.0,
                  771.0, 789.0, 795.0, 819.0, 891.0, 897.0, 915.0, 927.0, 945.0, 951.0, 999.0, 1005.0],
    "Violins II": [132.0, 195.0, 315.0, 327.0, 345.0, 351.0, 915.0, 927.0, 945.0, 951.0, 981.0, 999.0, 1005.0],
    "Violas": [123.0, 132.0, 183.0, 267.0, 723.0, 819.0, 879.0, 978.0, 999.0, 1005.0],
    "Violoncellos": [975.0, 999.0, 1005.0]})
# critic A #3 (S1): in the two ff tutti statements (bars 105-120, 305-320) the repeated staccato eighths blurred on the
# master (median dip 2.7 / 1.9 dB; the Stac samples outlast the 0.114 s eighth at ff). The printed staccatos there play
# the sections' staccatissimo recordings (row -> samples read from the .oib, cycles/c01/actor_scripts/rowsamples.py:
# 1st Violins "Stac RRx14" = V1 StacSs, 2nd Violins "Stac Slur RRx6" = V2 StacSs, Violas / Celli "Staccatissimo RRx16"
# = StacSs), at the velocity the Stac row had; "poly" keeps the violas' non div. double stops on the same row. The
# rows' ROW_TRIM_DB start at the replaced rows' values (to be measured on this render)
_TUTTI_STAC = [(312.0, 360.0), (912.0, 960.0)]
for _t, _r in (("Violins I", "Stac RRx14"), ("Violins II", "Stac Slur RRx6"), ("Violas", "Staccatissimo RRx16"),
               ("Violoncellos", "Staccatissimo RRx16")):
    ART_SPANS[_t] = ART_SPANS.get(_t, []) + [{"from": a_, "to": b_, "art": _r, "mark": "staccato", "poly": True}
                                             for a_, b_ in _TUTTI_STAC]
ROW_TRIM_DB = dict(ROW_TRIM_DB, **{"Violins I": dict(ROW_TRIM_DB["Violins I"], **{"Stac RRx14": (-3.0, 80)}),
                                   "Violas": dict(ROW_TRIM_DB["Violas"], **{"Staccatissimo RRx16": (-4.0, 80)}),
                                   "Violoncellos": dict(ROW_TRIM_DB["Violoncellos"], **{"Staccatissimo RRx16": (-4.0, 80)})})
# critic A #4 / C #5, MANUAL-GAPS #1: every printed woodwind staccato on the KS Masters' recorded "Stac DblTng RRx9" row
# instead of a Sus MAX slice cut inside its attack (cor anglais eighths played 0.036-0.057 s). Movement I c39 measured
# the row: harmonic peak +0.06..+0.16 s (slices +0.09..+0.33), rise 0.03-0.09 s, natural decay; velocity is the layer
# and level (its mf 82 / f 96, extended down here for the p / pp statements). One more row per track, no instance
_WSTAC = [(22, 44), (34, 54), (46, 64), (58, 72), (72, 82), (88, 96), (114, 112), (124, 118)]
for _t in ("Flute 1", "Flute 2", "Oboe 1", "Oboe 2", "Cor anglais", "Clarinet 1", "Clarinet 2", "Bassoon 1"):
    ART_SPANS[_t] = ART_SPANS.get(_t, []) + [{"from": 0.0, "to": SCORE_END, "art": "Stac DblTng RRx9",
                                              "mark": "staccato", "vel_by_cc": _WSTAC}]
# Movement I c39: the cor anglais row perceived 0.04 s late on the score onset (0.03 s lead); the faster-speaking rows
# of the other winds start 0.02 s early (the strings' Stac leads are 0.025-0.045 s)
STAC_LEAD_S = dict(STAC_LEAD_S, **{t_: 0.02 for t_ in ("Flute 1", "Flute 2", "Oboe 1", "Oboe 2", "Clarinet 1",
                                                       "Clarinet 2", "Bassoon 1")})
# critic A #6: the printed "port." of bar 214 (Violins I C sharp 6 -> F sharp 6, the glissando line, tC.ily c538) on
# the Leg Port MAX row (Movement I c11-c12: intermediate semitones +17-21 dB for a violin fourth)
PORT_TARGETS = dict(PORT_TARGETS, **{"Violins I": {640.0: 100}})
# a WARNING since the port (c00 parts.json printed it too): Horn 1's p < > mp (bars 207-208) capped its untargeted
# crescendo at the mp mark (kit 4: from p or softer the cap is the mark itself), so the > fell under mp and the printed
# mp at 624 sat at CC 52. The crest goes a little over the arrival
HP_TARGET_AT = dict(HP_TARGET_AT, **{"Hn1": {618.0: "mf-"}})
# with 1005 a stroke, the summit's following accented half notes (1008 printed down-bow, 1010, 1012) turned into Sus MAX
# strokes by STR_ACC_AFTER_SUS at v127 with no lead (the celli's 1008 a same-pitch Leg Slur re-attack): each is a
# printed accented stroke, so they take the DOWNBOW_STROKE_AT path too (lead and stroke velocity)
DOWNBOW_STROKE_AT = {t_: v_ + ([1008.0, 1010.0, 1012.0] if t_ in ("Violins I", "Violins II", "Violas", "Violoncellos")
                               else []) for t_, v_ in DOWNBOW_STROKE_AT.items()}

# ---------- c02 (actor, on the c01 render; cycles/c02/CHANGES.md) ----------
# ONE_TIME (BRIEF item 7): c01 settled at 49-50 GB, over the 45 GB cap. Rows that play only a few notes move to a row the
# track already loads (ROW_REMAP), so the rarely played row is not loaded (sample regions per row read from the .oib:
# cycles/c02/actor_scripts/rowcost.py). Brass Leg Slur MAX (10.5-10.7 thousand regions each) played only the two slur
# heads at 300 and 996 (3 qn crescendo notes, nothing joined to them); Oboe 2's Leg Slur MAX three slur heads (300, 900,
# 1005); the bass clarinet's Leg Slur 11 pp/p notes with two joins (237, 264); Violas div's two Leg BC MAX joins
ROW_REMAP = dict(ROW_REMAP, **{t_: {"Leg Slur MAX": "Sus MAX"} for t_ in ("Trombone 1", "Trombone 2", "Bass trombone",
                                                                          "Tuba", "Oboe 2")})
ROW_REMAP["Bass clarinet"] = {"Leg Slur": "Sus Non Vib"}
ROW_REMAP["Violas div"] = {"Leg BC MAX": "Leg Slur MAX"}
# the inner strings' remaining bow-change joins (Violas 17, Violins II 25 after the hemiola strokes below; 20.7 / 27.2
# thousand regions) join on Leg Slur MAX with a bow-change notch, the BC_SOFT path these two sections already take at
# pp-p. Violins I and the celli keep Leg BC MAX
ROW_REMAP["Violas"] = {"Leg BC MAX": "Leg Slur MAX"}
ROW_REMAP["Violins II"] = {"Leg BC MAX": "Leg Slur MAX"}
# and the woodwind "Stac DblTng RRx9" row (c01) on the three tracks with the fewest staccatos (Oboe 2 16-26, Bassoon 1
# 20, Clarinet 1 35, all in tuttis doubled by a track that keeps the row): back to the Sus MAX slices
for _t in ("Oboe 2", "Bassoon 1", "Clarinet 1"):
    ART_SPANS[_t] = [x_ for x_ in ART_SPANS.get(_t, []) if x_["art"] != "Stac DblTng RRx9"]
# critic A #3: the shared woodwind staccato table played Oboe 1's staccatos over its accents (accent minus staccato
# median +0.4 -> -5.6 dB) and left the cor anglais' 4.5 dB soft: Oboe 1 every velocity 12 lower, cor anglais 10 higher
for _t, _d in (("Oboe 1", -12), ("Cor anglais", 10)):
    ART_SPANS[_t] = [dict(x_, vel_by_cc=[(c_, max(1, min(127, v_ + _d))) for c_, v_ in _WSTAC])
                     if x_["art"] == "Stac DblTng RRx9" else x_ for x_ in ART_SPANS[_t]]
# critic A #4 (S1): the 2nd Violins' tutti staccatissimo row (Stac Slur RRx6 = V2 StacSs) did not separate the repeated
# eighths (stem dips 0.1-0.8 dB) and carried the master's trough: the Spiccato row (V2 Spic pp/mp/f/ff, manual p.93:
# shorter than staccato), 3 dB down as a start
ART_SPANS["Violins II"] = [dict(x_, art="Spiccato RRx9") if x_["art"] == "Stac Slur RRx6" else x_
                           for x_ in ART_SPANS["Violins II"]]
ROW_TRIM_DB["Violins II"] = dict(ROW_TRIM_DB["Violins II"], **{"Spiccato RRx9": (-3.0, 80)})
# critic A #1 (with c01's open item): the p / mp theme-head accents of Violins I (accent, two slurred eighths) still sat
# 9-15 dB under the staccato before them as Sus MAX strokes at v52 (as slow as the Leg Slur first note). The manual's
# Legato Slur Staccato row costs 54 thousand sample regions (rejected for memory); Movement I c23's "Sus Marc LITE" row
# (8.5 thousand) moves an accented stroke's weight to its first 0.25 s (front minus body -1.9 -> +2.4 dB, peak 0.29 ->
# 0.17 s) and plays 2-8 dB louder: on the nine p / mp heads (the f heads and 819 stay Sus MAX strokes as the control);
# STR_STROKE_ROWS keeps the stroke's lead
_MARC_HEADS = [39.0, 51.0, 69.0, 75.0, 285.0, 759.0, 771.0, 789.0, 795.0]
ART_SPANS["Violins I"] = [{"from": q_ - 0.01, "to": q_ + 0.01, "art": "Sus Marc LITE",
                           "vel_by_cc": [(34, 70), (46, 78), (58, 86), (72, 94)]} for q_ in _MARC_HEADS] \
    + ART_SPANS["Violins I"]
# critic A #2: the f hemiola "ritmo di quattro battute" (bars 101-104, 301-304): 31 unslurred accented half notes were
# Leg BC MAX targets, Leg Slur first notes or (celli) merged into one 11.6 qn note. Fresh Sus MAX strokes (the stroke
# list also stops the celli's same-pitch merge)
_HEM = [300.0, 302.0, 304.0, 306.0, 308.0, 310.0, 902.0, 904.0, 906.0, 908.0, 910.0]
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{
    t_: sorted(set(DOWNBOW_STROKE_AT.get(t_, []) + _HEM)) for t_ in ("Violins II", "Violas", "Violoncellos")})
DOWNBOW_STROKE_AT["Violins I"] = sorted(set(DOWNBOW_STROKE_AT["Violins I"] + [902.0, 904.0, 906.0, 908.0, 910.0]))
# critic A #6: the violas' slurred same-pitch tenuto pairs (portato) of bars 209-224 merged with a 10 CC notch that the
# rising hairpins hid (no dip): 18 CC
_PORT_PAIRS = [629.0, 638.0, 641.0, 644.0, 647.0, 650.0, 653.0, 656.0, 659.0, 662.0, 665.0, 668.0, 671.0]
MERGE_NOTCH_AT = dict(MERGE_NOTCH_AT, **{t_: {q_: 18 for q_ in _PORT_PAIRS} for t_ in ("Violas", "Violas div")})
# critic C #2: the fff summit downbeat (bar 336, qn 1005) arrived as a dip: the string strokes at REBOW_VEL_BY_CC's top
# (v96) spoke 9-10 dB under Violins I's v119 staccatissimo quarter before it. Strokes v112, that quarter v105, and the
# arrival weight (2 dB held back over the last beat, +2.5 dB at the arrival)
for _t in ("Violins I", "Violins II", "Violas", "Violoncellos"):
    VEL_SET[_t] = {**VEL_SET.get(_t, {}), 1005.0: 112}
VEL_SET["Violins I"][1004.0] = 105
ARRIVAL_WEIGHT_AT = {**ARRIVAL_WEIGHT_AT, 1005.0: (-2.0, 2.5, 1.0)}
# critic C #4: timpani crescendo rolls held flat (the roll trim table fell 11 dB from p to f under bar 101's p < f roll):
# hold 60% of the trim's fall under a printed crescendo; the pp < f roll of bars 205-208 already grows 11.6 dB (skipped,
# and 3 dB less over its last bar); the codetta's pp roll (bars 237-240, 12-19 dB under every other stem) +4 dB
TIMP_ROLL_TRIM_HOLD_CRESC = 0.6
TIMP_ROLL_TRIM_HOLD_SKIP = [618.0]
LEVEL_SHAPES = dict(LEVEL_SHAPES, **{"Timpani": LEVEL_SHAPES.get("Timpani", []) + [
    [(620.0, 0.0), (621.0, -3.0), (623.9, -3.0), (624.0, 0.0)],
    [(707.9, 0.0), (708.0, 4.0), (718.0, 4.0), (718.5, 0.0)]]})
# critic C #5: the harp's p espress. hairpins of the F major episode (bars 73-80) reached v80-98, louder than the mp
# theme: capped at 78
VEL_CAP_SPANS = dict(VEL_CAP_SPANS, **{"Harp": [(216.0, 240.0, 78)]})
# c02 stem fix (measured on the c02 render): the Sus Marc LITE heads came out +4.4..+14.6 dB over the staccato before
# them (mean of the first 150 ms against its 100 ms peak; target -3..+4) and lifted theme A's bars 5.5 dB: an exact
# level step from the moved onset (0.528 qn early) to just before the slurred eighths, set per head to land at +2 dB
_MARC_FIX = {39.0: -7.8, 51.0: -12.0, 69.0: -2.4, 75.0: -7.9, 285.0: -12.0, 759.0: -7.7, 771.0: -10.8, 789.0: -2.8,
             795.0: -8.0}
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES.get("Violins I", []) + [
    [(q_ - 0.62, 0.0), (q_ - 0.56, d_), (q_ + 1.9, d_), (q_ + 1.98, 0.0)] for q_, d_ in _MARC_FIX.items()]

# ---------- c03 (actor, on the c02 render; cycles/c03/CHANGES.md) ----------
# critic A #1: the p / mp Sus Marc LITE heads at v70-94 triggered the row's *f* marcato attack ("V1 MarcSh f", velocity
# 66-108; mp 1-65, read from the .oib): 2-5 kHz front +3.2..+4.7 dB over the body, master 2-5 kHz jump up to +9.3 dB.
# Velocities inside the mp band (<= 65). The _MARC_FIX steps stay until they are refitted on this render
ART_SPANS["Violins I"] = [dict(x_, vel_by_cc=[(34, 50), (46, 56), (58, 61), (72, 64)])
                          if x_["art"] == "Sus Marc LITE" else x_ for x_ in ART_SPANS["Violins I"]]
# critic A #2 (S1, MANUAL-GAPS #2, manual p.112 Legato Slur Repetitions): the clarinets' slurred repeated quarters were
# merged into one held note (dips -2.3..+2.7 dB). Memory-neutral form (critic A's first choice): a whole-piece REP_ROW
# span puts every Leg Slur and Sus Non Vib note of both clarinets on "Leg Slur Rep" (the keyswitch only: every rule
# still sees the old rows; 15.6 thousand regions in, Leg Slur 13.7 + Sus Non Vib 1.2 out). The merge skips slurred
# repeats inside a REP_ROW span, so the repeats take the re-tongue gap and CC11 fall (REP_ROW_GAP_S 0.06-0.15 s, clear
# of the row's 30 ms VoiceTimer, mvt1 c37-c38). (A first c03 attempt used ROW_REMAP Leg Slur -> Leg Slur Rep: rules keyed
# on the "Leg Slur" name then dropped the clarinets' entry leads and shortened notes before legato notes; replaced)
REP_ROW = dict(REP_ROW, **{t_: [(0.0, SCORE_END, "Leg Slur Rep")] for t_ in ("Clarinet 1", "Clarinet 2")})
# critic A #3: the woodwind portato repeats (bass clarinet and Bassoon 2 at 423-438, the hemiola, 963 / 966) took the
# tenuto rule's 0.06 qn gap (14 ms at quarter 264) before WIND_REP_PORTATO could re-tongue them (dips 0.4-0.9 dB)
WIND_REP_PORTATO_TENUTO = True
# critic A #5: Oboe 1's "Stac DblTng RRx9" played +4.5 dB over Flute 1's at f/ff (c00 on Sus slices: -1.6), so its
# accented heads were the softest notes of the head (-5.4..-10.4 dB under the staccato before); velocity barely moves
# the row (c02): a level trim from CC11 72 up (ROW_TRIM_WINDS, new generic)
ROW_TRIM_WINDS = True
ROW_TRIM_DB["Oboe 1"] = {"Stac DblTng RRx9": (-5.0, 72)}
# critics B #2 / C #4 (manual p.124 Felt Short): the 10 printed timpani staccatos (12, 165, 393, 549, 597, 722, 861,
# 968, 984, 1014) rang on the Lng row; the bar-339 stroke filled the G.P. (timpani -39.6 against a master of -38.2)
TIMP_STAC_ROW = "Timpani Flt Sht"
# critic C #1: the long note after a slurred eighth (hemiola, trio tune) arrived 0.1-0.26 s late as a Sus-to-Leg
# transition: the eighth stays on the legato row whenever the next note of its slur is 1 qn or longer
SHORT_SUS_TO_LONG_ANY = True
# critic C #2: the f hemiola strokes (101-104, 301-304) and the summit's accented halves abut the note before, so no
# entry lead applied: perceived +55..+226 ms against the winds' -7..+63. ABUT_LEAD 0.08 s at the listed onsets
_ABUT_AT = [302.0, 304.0, 306.0, 308.0, 310.0, 904.0, 906.0, 908.0, 910.0, 1008.0, 1010.0, 1012.0]
ABUT_LEAD = dict(ABUT_LEAD, **{t_: {"lead_s": 0.08, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": False,
                                    "at": _ABUT_AT} for t_ in ("Violins II", "Violins I", "Violas")})
# critic C #5: the section pizz. rows speak 22-50 ms after the bows and the basses' pizz.; C #6: the 2nd Violins'
# tutti "Spiccato RRx9" had no staccato lead (+20 ms against Violins I +5)
PIZZ_LEAD_S = {"Violas": 0.045, "Violins II": 0.035, "Violoncellos": 0.035}
STAC_LEAD_SPIC = True
# (Violas 904 and 906 already took the Leg -> Sus entry path, 0.06-0.12 s lead and v105: they keep that path)
ABUT_LEAD["Violas"] = dict(ABUT_LEAD["Violas"], at=[q_ for q_ in _ABUT_AT if q_ not in (904.0, 906.0)])
# critic B #6: the basses' pp arco staccato A1 at 96 (v45) peaked over the p leggiero counterstatement (the A1 pitch trim
# covers pizz. only): -6 dB as a step from before its onset through the rest (a note-trim ramp never reaches -6 dB on a
# 0.5 qn note), back before the next entry at 101.5
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [[(95.85, 0.0), (95.9, -6.0), (100.9, -6.0), (101.0, 0.0)]]
# ONE_TIME #3 (Movement I c44, Dan's S1): STR_REP_NEW_BOW (generic, ported from Movement I's tools with its c45 lead
# fix): loud / accented / slur-head / slurred-tenuto same-pitch string repeats that the legato merge joined into the note
# before with a CC11 notch become fresh Sus MAX strokes after a min(0.06 s, 25%) gap (portato 0.05 s and a 6 / 8 CC fall)
# with the string re-tongue lead; soft repeats inside one slur stay merged; other soft repeats become re-bow points
STR_REP_NEW_BOW = {"gap_s": 0.06, "frac": 0.25, "stroke_cc": DYN["mf"], "stroke_mark": "mp", "head_cc": DYN["p"], "sus_min_s": 0.4,
                   "portato": {"gap_s": 0.05, "frac": 0.25, "fall_cc": 6, "fall_cc_loud": 8, "fall_s": 0.04},
                   "sus_lead_s": 0.10}
# critic C #6: loud string entries on Leg Slur MAX's first-note layer arrived +80..+100 ms (medians Violins I +102,
# Violins II +96, celli +82, Violas div +61) with the 0.06 s loud entry lead: +0.06 s above CC11 80 (new generic option)
ENTRY_LEAD_LOUD_ART_S = {"string": {"Leg Slur MAX": 0.06}}

# ---------- c03 stem fix (measured on the c03 render) ----------
# critic A #1 refit: with the mp-band velocities 7 of the 9 heads sit +2.4..+3.7 dB over the staccato before them (target
# +2..+4) and lost the bright front; 51 and 771 came out +6.5 / +6.3 dB with a bright front: -3 dB more on those two
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [
    [(q_ - 0.62, 0.0), (q_ - 0.56, -3.0), (q_ + 1.9, -3.0), (q_ + 1.98, 0.0)] for q_ in (51.0, 771.0)]
# critics B #2 / C #4: the Sht row did not empty the G.P. (the long strokes of bars 337-338 still ring: timpani stem
# -42 / -51 dB in qn 1017-1019 against Violins I -60 / -87). A volume-envelope cut there is undone by build_reaper's
# tail hold (rests hold the last note's level, BRIEF S3), so this needs a pre-hall CC7 fall in a later cycle: open

# ---------- c04 (actor, on the c03 render; cycles/c04/CHANGES.md) ----------
# critics B #4 / C #3 (c03 open item): the G.P. (bar 340) was the timpani's undamped ring of the Lng strokes 1008-1012,
# 13-24 dB over the orchestra's hall. A pre-hall damp after the bar-339 Sht chord has spoken (new generic TIMP_DAMP_AT:
# the CC7 lane falls 127 -> 1 over 1014.5-1015.25, about 0.16 s at quarter 288, and holds to the next onset at 1086), and
# the drum 4 dB down from before the 1008 stroke through the G.P. (roles.json; the 1014 stroke was the loudest stem)
TIMP_DAMP_AT = [(1014.5, 1015.25, 1)]
# critics B #2 / C #5: the harp's p espress. tune of the F major episode was the loudest soft passage (5-12 dB over every
# other soft tune; the pp chords of 81-88 over Clarinet 1's dolce tune): the p pluck layer (Pluck p 1-57) and lower for
# the pp chords, with roles -3 / -2
VEL_CAP_SPANS["Harp"] = [(216.0, 240.0, 56), (240.0, 264.0, 50)]
# critic A #3 (S1): the coda build's staccato eighth pairs (bars 328-335, qn 981-1005) still played the plain Stac rows
# (master pair dips median 2.4 dB, violas / Violins II 0 dB at several pairs) that the two tutti statements replaced:
# the tutti staccatissimo rows (all loaded already) over 981-1005 too; the strokes at 981 / 999 / 1005 are not staccato
# (not the celli: their tuttis have no staccato, so "Staccatissimo RRx16" is not loaded there; 13.9 thousand regions)
for _t, _r in (("Violins I", "Stac RRx14"), ("Violins II", "Spiccato RRx9"), ("Violas", "Staccatissimo RRx16")):
    ART_SPANS[_t] = ART_SPANS[_t] + [{"from": 981.0, "to": 1005.0, "art": _r, "mark": "staccato", "poly": True}]
# critic C #1: theme A's staccato heads replayed identical samples phrase after phrase (Violins I bars 13 / 17 / 25 head
# notes xcorr 0.98-1.00 on the stem; the round robin returns to one position after each row change). The second and
# fourth four-bar phrase of each p / mp statement play the loaded "Stac RRx14" (V1 StacSs) instead of "Staccatissimo
# RRx9" (V1 Stac), so neighbouring phrases use different samples; the Marc LITE heads (listed first) stay
ART_SPANS["Violins I"] = ART_SPANS["Violins I"] + [{"from": a_, "to": b_, "art": "Stac RRx14", "mark": "staccato"}
                                                   for a_, b_ in ((48.0, 60.0), (72.0, 84.0), (768.0, 780.0), (792.0, 804.0))]
# critic A #1 (S1, manual p.102-103 short notes / double tonguing): Trumpet 1's staccato theme head played cut Sus Non
# Vib MAX slices (quarters peak +115 ms, the second repeated eighth dip 1.5 dB median, no peak of its own at 319.5 /
# 325.5 / 331.5): every printed staccato on the 1TP "StacSs DblTng RRx9" row (4,080 regions, the smaller of the two
# double-tongue rows; memory at the 45 GB cap, so Trumpet 2 (dips 3.5 dB) stays on Sus slices this cycle). Velocity
# under the top band (overblown attack at the highest velocity, p.102; Dan: weight, not bite). One staccato lead for
# all four notes of a head (STAC_LEAD_S now takes brass rows too, generic)
_TSTAC = [(22, 50), (34, 58), (46, 66), (58, 74), (72, 84), (88, 96), (114, 106), (124, 110)]
ART_SPANS["Trumpet 1"] = ART_SPANS.get("Trumpet 1", []) + [{"from": 0.0, "to": SCORE_END, "art": "StacSs DblTng RRx9",
                                                            "mark": "staccato", "vel_by_cc": _TSTAC}]
STAC_LEAD_S["Trumpet 1"] = 0.02
# critic A #2 fallback (the portato rows deferred for memory): the soft horn tenuto repeats dipped 7-11 dB (Horn 3, bars
# 73-88) and 12-14 dB (Horn 1, 630-663) against 2.5 dB on Horn 4 at the same bar lines; a tenuto is a full-value note
# (target 3-6 dB): smaller re-tongue gap and CC11 fall
WIND_REP_RETONGUE_BY["Horn"] = {"gap_s": 0.07, "frac": 0.25, "fall_cc": 8, "fall_s": 0.12}
# critic C #2 (BRIEF item 6): the fff summit (bar 337) was only 1.0-1.3 dB over the ff arrivals of bars 104 / 304 in the
# master and the mp3, with no room above (limiter 2.5 dB): the delivery ride takes the hemiola arrivals and bar 72 down
# (RIDE_TRIMS, delivery only; the stems and the master keep their levels)
RIDE_TRIMS = [[(300.0, 0.0), (303.0, -2.0), (311.6, -2.0), (312.4, 0.0)],
              [(897.0, 0.0), (900.0, -2.0), (911.6, -2.0), (912.4, 0.0)],
              [(212.5, 0.0), (213.5, -1.5), (215.6, -1.5), (216.3, 0.0)]]

# ---------- c04 stem fix (measured on the c04 render) ----------
# critic A #1 level: Trumpet 1's pp staccatos of bars 101-103 on the StacSs row came out +6.2 dB over c03's Sus slices
# (-44.6 against -50.8 dB RMS over qn 300-309, 6.6 dB over Trumpet 2); the ff tutti (312-360) and the coda (993-1005)
# stayed within 0.5 dB. -6 dB over the pp staccatos (the held 309 note on Sus Non Vib keeps its level)
LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES.get("Trumpet 1", []) + [[(299.5, 0.0), (299.7, -6.0), (308.75, -6.0), (308.85, 0.0)]]

# ---------- c05 (actor, on the c04 render; cycles/c05/CHANGES.md) ----------
# critic A #1: the f hemiola's accented half notes (bars 101-104, 301-304) peaked 150-340 ms after each beat (master
# front minus body -0.1..-5.7 dB): a -3 dB body cut on the strings, -2 dB on the double reeds (build/accent_bodies.json,
# ACCENT_BODY_S_SHORT (0.18, 0.28) s); more lead on the late strokes after the sfp (902 / 904) and on Violins I's
# 300-310 strokes (REATTACK_LEAD_AT replaces a smaller lead only); Violins I / II 904 at v85 (was 65, between 902's v105
# and 906's v78)
REATTACK_LEAD_AT = dict(REATTACK_LEAD_AT, **{
    "Violins I": {**{q_: 0.13 for q_ in (302.0, 304.0, 306.0, 308.0, 310.0)}, 902.0: 0.20, 904.0: 0.20},
    "Violins II": {902.0: 0.20, 904.0: 0.20}, "Violoncellos": {902.0: 0.20, 904.0: 0.20},
    "Violas": {902.0: 0.18, 904.0: 0.18}})
for _t in ("Violins I", "Violins II"):
    VEL_SET[_t] = {**VEL_SET.get(_t, {}), 904.0: 85}
# critic A #2: Violins II's con sord. arpeggio groups (168-196) led only each group's first note (0.12 s entry lead):
# heads -0.02 s, followers +0.05 s on the pcx medians. One 0.05 s lead for every note of the span
GROUP_LEAD_AT = dict(GROUP_LEAD_AT, **{"Violins II": GROUP_LEAD_AT.get("Violins II", []) + [(501.5, 587.5, 0.05)]})
# critic A #3: Horn 1's repeated tenuto dotted halves (627-666) still dipped 7-11 dB, 80-140 ms under -3 dB, with the
# c04 horn re-tongue: Horn 1 gets a smaller gap and fall (listed before "Horn": the lookup takes the first prefix match)
# and a 0.09 s re-tongue lead so the new note's rise overlaps the old note's end
WIND_REP_RETONGUE_BY = {"Horn 1": {"gap_s": 0.035, "frac": 0.15, "fall_cc": 4, "fall_s": 0.08}, **WIND_REP_RETONGUE_BY}
# (RETONGUE_LEAD_S applies to every Horn 1 re-tongue in the piece; REATTACK_LEAD_AT on the five repeats alone was
# tried and rejected: it ends the old note 0.02 qn before the moved onset, a 5 ms gap instead of the re-tongue's 35 ms)
RETONGUE_LEAD_S["Horn 1"] = 0.09
# critic A #6: the violas' div. portato pairs (209-224) dipped a median 1.2 / -0.7 dB (Violas / Violas div): a longer
# portato gap and a deeper CC11 fall
STR_REP_NEW_BOW["portato"] = {"gap_s": 0.08, "frac": 0.3, "fall_cc": 12, "fall_cc_loud": 14, "fall_s": 0.08}
# critic B #1: in the ff tutti theme the flutes' "Stac DblTng RRx9" head sat 8-18 dB under Violins I and 16-20 dB under
# their own accented Sus G6 (row jump plus GENTLE_ACCENT): ff staccatos +6 dB (CC11 >= 100 only; the f and softer
# staccatos stay), the long top notes cut in roles.json
for _t in ("Flute 1", "Flute 2"):
    ROW_TRIM_DB[_t] = {**ROW_TRIM_DB.get(_t, {}), "Stac DblTng RRx9": (6.0, 100)}
# critic B #3: Oboe 1's sub. p espress. octave with Flute 1 (bars 277-280) sat 6.5-12 dB under the flute and level with
# the pp violas: a level shape (not a role, so the hairpin peak at 832 does not jump over the flute)
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES.get("Oboe 1", []) + [
    [(827.5, 0.0), (828.0, 7.0), (831.5, 7.0), (832.3, 2.0), (833.5, 4.0), (840.0, 4.0), (840.5, 0.0)]]

# ---------- c06 (actor, on the c05 render; cycles/c06/CHANGES.md) ----------
# critic A #1 (S1): the c04 "Stac RRx14" phrases rang the first repeated eighth through the second (stem pair dips
# 2.0-5.1 dB against 6.7-8.5 on Staccatissimo RRx9): the repeated-eighth pairs (49, 55, 73, 79, 769, 775, 793, 799 and
# the eighth after each) go back to the theme's Staccatissimo row; the other notes of those phrases keep the alternate
# samples (C #1 c04)
_RR14_OLD = ((48.0, 60.0), (72.0, 84.0), (768.0, 780.0), (792.0, 804.0))
ART_SPANS["Violins I"] = [x_ for x_ in ART_SPANS["Violins I"]
                          if not (x_["art"] == "Stac RRx14" and (x_["from"], x_["to"]) in _RR14_OLD)]
ART_SPANS["Violins I"] = ART_SPANS["Violins I"] + [
    {"from": a_, "to": b_, "art": "Stac RRx14", "mark": "staccato"}
    for a_, b_ in ((48.0, 49.0), (50.0, 55.0), (56.0, 60.0), (72.0, 73.0), (74.0, 79.0), (80.0, 84.0),
                   (768.0, 769.0), (770.0, 775.0), (776.0, 780.0), (792.0, 793.0), (794.0, 799.0), (800.0, 804.0))]
# critic A #2: the violas' slurred tenuto pairs of bars 209-224 played weak-strong (first note on Leg Slur MAX's quiet
# first-note layer after a gap, the second a Sus MAX stroke: +5.4 dB median step). Tried first: the first notes on Sus
# MAX by ART_SPANS; the span bypasses the portato rule, so the second notes lost their lead and gap (re-attack at the
# score onset after 16 ms). The critic's fallback instead: level trims on the first notes (build/note_trims.json)
# critic A #3: the f hemiola strokes of Violins I (bars 101-104, 301-304) still peaked 110-415 ms after the beat on Sus
# MAX (a body cut cannot make a front): the loaded "Sus Marc LITE" row (the theme heads' fix), its f layer at about v80,
# with a level step over each span (Marc LITE plays 2-8 dB over a Sus MAX stroke; refit on the render)
ART_SPANS["Violins I"] = [{"from": a_, "to": b_, "art": "Sus Marc LITE", "vel_by_cc": [(58, 74), (72, 80), (88, 84), (100, 88)]}
                          for a_, b_ in ((299.5, 311.0), (901.5, 911.0))] + ART_SPANS["Violins I"]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [
    [(299.3, 0.0), (299.4, -5.0), (311.9, -5.0), (312.0, 0.0)],
    [(900.95, 0.0), (901.05, -2.0), (911.9, -2.0), (912.0, 0.0)]]   # c06 stem fix: -5 left 902-912 3.6 dB under c05
# critic A #5 (MANUAL-GAPS #10 / #17): Horn 1's slurred tenuto dotted halves of bars 210-222 still had 115-170 ms holes
# on Sus MAX re-tongues: the 1FH "Port Lng" row (775 regions), recorded for this tongued, connected repeat; velocity by
# layer, about v70-80 at f (the tied 642 and the slurred 645-646 stay off the span)
ART_SPANS["Horn 1"] = [{"from": a_, "to": b_, "art": "Port Lng", "vel_by_cc": [(34, 56), (46, 62), (58, 68), (72, 74), (88, 80), (100, 86)]}
                       for a_, b_ in ((626.5, 641.5), (647.5, 664.0))] + ART_SPANS.get("Horn 1", [])
# an ART_SPANS note skips the re-tongue lead (the Port Lng notes came out at their score onsets): the c05 re-tongue lead
# (0.09 s) as a re-attack lead
REATTACK_LEAD_AT["Horn 1"] = {**REATTACK_LEAD_AT.get("Horn 1", {}),
                              **{q_: 0.09 for q_ in (627.0, 630.0, 633.0, 636.0, 639.0, 648.0, 651.0, 654.0, 657.0, 659.0, 660.0, 663.0)}}
# critic C #1: the tutti sfp of bar 301 had no sf. Strings: the 900 half note is an unslurred fresh down-bow (it joined the
# ff note before as a Leg Slur transition at v53): a Sus MAX stroke at v105. Winds: the entries led early onto the sfp
# held the curve's pre-spike p (new generic FP_SPIKE_FROM_ONSET: the pull holds the spike's level)
DOWNBOW_STROKE_AT = {**DOWNBOW_STROKE_AT, **{t_: sorted(set(DOWNBOW_STROKE_AT.get(t_, []) + [900.0]))
                                             for t_ in ("Violins I", "Violins II", "Violas", "Violoncellos")}}
for _t in ("Violins I", "Violins II", "Violas", "Violoncellos"):
    VEL_SET[_t] = {**VEL_SET.get(_t, {}), 900.0: 105}
FP_SPIKE_FROM_ONSET = True
# the 900 strokes abut the ff notes of bar 300: V1 / V2 / violas got no lead and the celli's entry lead (0.528 qn) left
# the 899 note sounding under the stroke; ABUT_LEAD (0.08 s, the hemiola strokes' value) ends the note before
for _t in ("Violins I", "Violins II", "Violas"):
    ABUT_LEAD[_t] = dict(ABUT_LEAD[_t], at=sorted(set(ABUT_LEAD[_t]["at"] + [900.0])))
ABUT_LEAD["Violoncellos"] = {"lead_s": 0.08, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": False, "at": [900.0]}
# critic C #4: the trumpets' pp < f of bars 101-104 restarted at pp after the bar-102 rest (bar-103 group 5-12 dB under
# the first, the f 18-25 dB over it): the hairpin stays open to the f (new generic HP_KEEP_ACROSS_REST), and Trumpet 1's
# c04 flat -6 dB step becomes a ramp to -2
HP_KEEP_ACROSS_REST = {"Tpt1": 9.0, "Tpt2": 9.0}
LEVEL_SHAPES["Trumpet 1"] = [r_ for r_ in LEVEL_SHAPES["Trumpet 1"] if r_ != [(299.5, 0.0), (299.7, -6.0), (308.75, -6.0), (308.85, 0.0)]] \
    + [[(299.5, 0.0), (299.7, -6.0), (308.75, -2.0), (308.85, 0.0)]]
# critic C #5: the fff summit's roll vanished within a bar (bump decay, -9 dB at 1007.95) and the bar-332 mf < f roll
# stayed flat: a held roll body under the summit and 5 dB of growth into bar 333 (both under printed ff / crescendo)
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [
    [(1005.7, 0.0), (1006.0, 5.0), (1007.0, 8.0), (1007.85, 8.0), (1007.9, 0.0)],
    [(993.0, 0.0), (995.9, 5.0), (995.95, 0.0)]]
# critic C #3 (delivery only): the delivered trio climax (bar 218) was no louder than its f at bar 197 or bar 222 (the ride
# lifts the bars around it 6.8-8 dB, the climax 2.7): RIDE_TRIMS hold back the f bars around it
RIDE_TRIMS = RIDE_TRIMS + [[(587.0, 0.0), (588.0, -2.0), (601.0, -2.0), (602.0, 0.0)],
                           [(624.0, 0.0), (625.0, -1.0), (648.0, -1.0), (649.0, 0.0)],
                           [(659.0, 0.0), (660.0, -2.0), (671.0, -2.0), (672.0, 0.0)]]

# ---------- c07 (actor, on the c06 render; cycles/c07/CHANGES.md) ----------
# critic B #2 (manual p.150: velocity picks the layer; Thumb pick p 1-42 / mp 43-70): the harp's pp chords under the soft
# solo tunes (trio Cl 1, bars 185-192 Ob 1, codetta, Meno mosso Hn 3) played the Thumb mp layer at v52: capped at 42
VEL_CAP_SPANS["Harp"] = VEL_CAP_SPANS["Harp"] + [(456.0, 504.0, 42), (552.0, 576.0, 42), (672.0, 711.0, 42),
                                                 (1020.0, 1044.0, 42)]
# critic A #3 (S1): Violins I tutti pairs still merged on "Stac RRx14" (325.5 0.9, 331.5 2.4, 355.5 2.4, 925.5 0.9,
# 931.5 2.6, 955.5 2.8 dB stem dip): those pairs on the theme's "Staccatissimo RRx9" (listed first: the first span wins)
ART_SPANS["Violins I"] = [{"from": a_, "to": a_ + 1.0, "art": "Staccatissimo RRx9", "mark": "staccato", "poly": True}
                          for a_ in (325.0, 331.0, 355.0, 925.0, 931.0, 955.0)] + ART_SPANS["Violins I"]
# Violins II pairs 313-314, 319-320, 913-914, 919-920 (dips 1.1-2.5 dB) on the loaded "Stac RRx9"
ART_SPANS["Violins II"] = [{"from": a_, "to": a_ + 1.0, "art": "Stac RRx9", "mark": "staccato", "poly": True}
                           for a_ in (313.0, 319.0, 913.0, 919.0)] + ART_SPANS["Violins II"]
ROW_TRIM_DB["Violins II"] = {**ROW_TRIM_DB.get("Violins II", {}), "Stac RRx9": (-4.0, 80)}
# critic A #5: Horn 1 Port Lng left holes at 636 / 639 / 651 / 654 (6-12.5 dB): those spans back to Sus MAX with the c05
# re-tongue (0.09 s RETONGUE_LEAD_S); Port Lng kept on 626.5-635.5, 647.5-650.5 and 656-664
ART_SPANS["Horn 1"] = [x_ for x_ in ART_SPANS["Horn 1"] if x_.get("art") != "Port Lng"] + [
    {"from": a_, "to": b_, "art": "Port Lng", "vel_by_cc": [(34, 56), (46, 62), (58, 68), (72, 74), (88, 80), (100, 86)]}
    for a_, b_ in ((626.5, 635.5), (647.5, 650.5), (656.0, 664.0))]
REATTACK_LEAD_AT["Horn 1"] = {q_: v_ for q_, v_ in REATTACK_LEAD_AT["Horn 1"].items() if q_ not in (636.0, 639.0, 651.0, 654.0)}
# critic C #3: the reprise hemiola and summit strokes scattered by up to 171 ms (pcx): leads re-set toward the flute
REATTACK_LEAD_AT["Violins I"] = {**REATTACK_LEAD_AT["Violins I"], 902.0: 0.11, 904.0: 0.13}
REATTACK_LEAD_AT["Violas"] = {**REATTACK_LEAD_AT["Violas"], 904.0: 0.25}
REATTACK_LEAD_AT["Violins II"] = {**REATTACK_LEAD_AT["Violins II"], 906.0: 0.15, 910.0: 0.13, 1008.0: 0.13, 1010.0: 0.13,
                                  1012.0: 0.13}
# critic A #4 (manual p.80: velocity sets the Leg Slur transition speed): the dolce solo at one moderate legato
# velocity (was v124 then v90 inside one phrase), lead +0.03 s for the slower transitions
LEG_VEL_SPANS = {**LEG_VEL_SPANS, "Violin I solo": [(1043.5, 1068.0, 82)]}
LEG_LEAD_S["Violin I solo"] = 0.15
# ---------- c07 ONE_TIME (EastWest template MIDI rules, plan sections 5-8) and research batches 5-7 ----------
# item 1 (repeat gaps 60-100 ms; strings 90, winds 63): string re-bow gap 0.06 -> 0.09 s and wind re-tongue 0.06 -> 0.065 s,
# each capped at 30 % of the note (was 25 %: at quarter 264 an eighth is 114 ms). Horn rules keep their fitted values
STR_REP_NEW_BOW = {**STR_REP_NEW_BOW, "gap_s": 0.09, "frac": 0.3}
WIND_REP_RETONGUE = {**WIND_REP_RETONGUE, "gap_s": 0.065, "frac": 0.3}
# item 2 (legato overlap 45-80 ms strings, 33-58 ms winds / brass; joins overlapped 9-11 ms): floors 60 / 45 ms, at most
# 35 % of the target's own length (critic A: fast slurred eighths keep their pitch)
LEG_OVERLAP_MIN_S = {"string": 0.06, "wind": 0.045, "brass": 0.045}
LEG_OVERLAP_MAX_FRAC = 0.35
# item 3 (legato velocity follows the dynamic, r 0.35 around 90+; manual p.80 / p.144: velocity is the transition speed):
# the strings' and brass' legato targets by the dynamic lane instead of 124 everywhere (the finale's c07 table)
LEG_VEL_STRONG = {"string": [(52, 100), (65, 106), (80, 112), (100, 118), (127, 124)],
                  "brass": [(52, 100), (65, 106), (80, 112), (100, 118), (127, 124)]}
# item 4 + batches 6-7 (phrase shape by music type): the finale's c07 PHRASE_SHAPE. Lyrical spans (the second idea,
# the trio, the Meno mosso coda) keep the centred arch; the Allegro's driving phrases enter a little high, peak early
# and fall (milder than the finale's: the scherzo's balance is fitted per bar); builds peak at the end
PHRASE_SHAPE = {"families": ("string", "wind", "brass"), "min_s": 2.0, "gap_s": 0.25, "start": -12,
                "rise": [(0.4, 3), (0.8, 8)], "peak": (10, 0.45), "pre_end": (1.0, 4), "end": -12,
                "scale": {"ppp": 0.6, "pp": 0.8, "p": 1.0, "mp": 1.0, "mf": 1.0, "f": 0.6, "ff": 0.35, "fff": 0.2},
                "floor": 8, "cap": {"brass": 108}, "hp_fade_s": 0.25, "step_s": 0.1, "cc1_floor": 36,
                "types": {"build_cc": 10, "drive": (4, (6, 0.15), -6), "drive_min_bpm": 0,
                          "lyric_spans": [(132.0, 168.0), (360.0, 420.0), (456.0, 720.0), (828.0, 864.0),
                                          (1020.0, 1128.0)]}}
# batch 5 item 3: crescendos reach 70 % of their rise at 40 % of the hairpin; diminuendos keep 65 % to their last onset
HP_CURVE = {"cresc": (0.4, 0.7), "decresc_last": 0.35, "min_qn": 1.0}
# batch 7 (short-note velocity by beat position, 15-25 steps; critic A: put the contrast between beat 1 and beats 2-3,
# never drop the second of a repeated pair more than 5): downbeat +8, beats 2-3 -4, off-beat eighths -6, +-4 seeded,
# only in the Allegro (quarter 250 or faster), on staccato / spiccato / pizzicato rows
SHORT_BEAT_VEL = {"families": ("string", "brass"), "rows": ("Stac", "Spic", "Pizz", "StacSs"), "beat1": 8, "beat": -4,
                  "off": -6, "rand": 4, "seed": 7, "min_bpm": 250, "meter_qn": 3.0, "pair_max": 5}
# batch 5 item 5 (tempo changes on about 20 % of beats, breaths; critic C #5's list): one slower beat before the phrase
# joints of the Allegro (no change inside its phrases) and lighter breaths at the trio's / Meno mosso's four-bar ends.
# BEAT_STRETCH multiplies the beat's tempo
BEAT_STRETCH = {**BEAT_STRETCH, 35.0: 0.92, 359.0: 0.88, 827.0: 0.90, 167.0: 0.94, 863.0: 0.94, 971.0: 0.94,
                **{q_: 0.92 for q_ in (479.0, 503.0, 527.0, 551.0, 575.0, 587.0, 599.0, 611.0, 647.0, 695.0,
                                       1031.0, 1043.0, 1055.0, 1079.0)},
                671.0: 0.85, 1067.0: 0.85}
# critic C #4: the pizzicato round robins (4 per note) ran a 4-bar accent cycle over the printed 3-bar groups of bars
# 89-98 (celli 8 dB, basses 5.5 dB spread): a round-robin reset at each group head; the reprise's violas / Violins II
# pizz. start from a fixed position
RR_RESET_AT = {"Violoncellos": [264.0, 273.0, 282.0, 291.0], "Double basses": [264.0, 273.0, 282.0, 291.0],
               "Violas": [756.0], "Violins II": [756.0]}
# critic A #2: the two slurred eighths after each accented half note of the theme head were covered by the half note's
# release (first eighth own-pitch -13..-27 dB at v53, a soft Sus MAX attack takes ~0.3 s; tutti v100 -6..-9): the
# slurred short notes start 0.06 s early (the note before ends 0.02 qn after the moved onset, cap 45 % of its slot),
# the soft statements' first eighths at v88, and Violins I's Sus Marc LITE release capped at 120 ms (mix.json)
SHORT_SUS_LEAD_TRACKS = ("Violins I", "Violins II", "Violas")
SHORT_SUS_LEAD_S = 0.06
SHORT_SUS_LEAD_KEEP_OVERLAP = 0.02
SHORT_SUS_LEAD_CAP_FRAC = 0.45
VEL_SET["Violins I"] = {**VEL_SET.get("Violins I", {}), **{q_: 88 for q_ in (41.0, 53.0, 71.0, 77.0, 761.0, 773.0, 791.0, 797.0)}}
# c07 (orchestrator, Movement I c51 critics): timpani roll hairpins stay linear (an early-rising curve made a fff -> pp
# roll rise up to 8 dB over a horn solo there); SHORT_BEAT_VEL off this cycle: on the HO string short rows velocity
# picks the layer, and one velocity table moved notes between layers by about 10 dB (Movement I c51); the beat weight
# goes into the volume envelope in a later cycle (+1.5 / 0 / -1 dB)
HP_CURVE = {**HP_CURVE, "skip_families": ("timp",)}
SHORT_BEAT_VEL = None

# ---------- c08 (actor, on the c07 render; cycles/c08/CHANGES.md) ----------
# critic A #1: the second slurred eighth after each accented half note stayed at v53-63 (own-pitch dominance -2..-9 dB,
# both eighths -15 dB under the half note at 69 / 789); the retransition's tail (285) and the fugato tails got nothing:
# v85 on the second eighths, v88 / v85 on the other tails, and the celli take the 0.06 s slurred-short lead too
VEL_SET["Violins I"] = {**VEL_SET["Violins I"], **{q_: 85 for q_ in (41.5, 53.5, 71.5, 77.5, 761.5, 773.5, 791.5, 797.5)},
                        287.0: 88, 287.5: 85}
VEL_SET["Violins II"] = {**VEL_SET.get("Violins II", {}), 197.0: 88, 197.5: 85}
VEL_SET["Violas"] = {**VEL_SET.get("Violas", {}), 185.0: 88, 185.5: 85, 881.0: 88, 881.5: 85}
VEL_SET["Violoncellos"] = {**VEL_SET.get("Violoncellos", {}), 173.0: 88, 173.5: 85, 869.0: 88, 869.5: 85}
SHORT_SUS_LEAD_TRACKS = SHORT_SUS_LEAD_TRACKS + ("Violoncellos",)
# critic A #2: the tutti sfp (bar 301, qn 900): the sf held 0.25 qn (57 ms at quarter 264) and was at p by 114 ms, before
# the soft wind attacks (v53) reached their peak (+123..+175 ms): Flute 1 and the cor anglais swelled instead. The sf holds
# about 0.10 s and is at p by about 0.20 s; the winds enter at v100; Violins I's stroke on the Marcato Sustain row (manual
# pp.91-92 "extra power at the start", loaded), with a re-attack lead because ART_SPANS notes skip the lead rules
FP_SPIKE = ("f", 0.45, 0.9)
for _t in ("Flute 1", "Flute 2", "Oboe 1", "Oboe 2", "Cor anglais", "Clarinet 1", "Clarinet 2", "Bassoon 1", "Bassoon 2",
           "Contrabassoon"):
    VEL_SET[_t] = {**VEL_SET.get(_t, {}), 900.0: 100}
ART_SPANS["Violins I"] = [{"from": 899.6, "to": 900.1, "art": "Sus Marc LITE",
                           "vel_by_cc": [(58, 74), (72, 80), (88, 84), (100, 88)]}] + ART_SPANS["Violins I"]
REATTACK_LEAD_AT["Violins I"] = {**REATTACK_LEAD_AT["Violins I"], 900.0: 0.08}
# critics A #3 / C #4 (S1): the coda build's repeated eighth pairs (985-998) merged (master dips 1.7-4.9 dB; Violins II
# Spiccato 2.9-3.7 dB, Violins I Stac RRx14 3.2-6.1 dB on the stem): the tutti statements' pair rows (c07 A #3, loaded)
# listed first; Oboe 2's and Clarinet 1's staccato slices, which fill the gaps (47 % / 19 % of the gap energy), at 0.35
# of their slot (new generic STAC_LEN_SPANS)
_CODA_PAIRS = (985.0, 988.0, 991.0, 994.0, 997.0)
ART_SPANS["Violins I"] = [{"from": a_, "to": a_ + 1.0, "art": "Staccatissimo RRx9", "mark": "staccato", "poly": True}
                          for a_ in _CODA_PAIRS] + ART_SPANS["Violins I"]
ART_SPANS["Violins II"] = [{"from": a_, "to": a_ + 1.0, "art": "Stac RRx9", "mark": "staccato", "poly": True}
                           for a_ in _CODA_PAIRS] + ART_SPANS["Violins II"]
STAC_LEN_SPANS = {"Oboe 2": [(984.0, 1005.0, 0.35)], "Clarinet 1": [(984.0, 1005.0, 0.35)]}
# critic A #4 (S1, S2) and B #4: the horns' tutti staccato quarters were Sus MAX slices peaking +0.12 s late with merged
# repeats; Trumpet 2's on Sus Non Vib slices 5 dB under Trumpet 1's StacSs row. The 1FH "StacSs RRx9" (6,910 regions) for
# Horns 1-2 and the 1TP "StacSs DblTng RRx9" (4,080) for Trumpet 2, with Trumpet 1's velocity table, lead and its pp step
# over 300-309 (c04: the row plays about 6 dB over a slice at low velocity); Horn 2's tenuto repeats a deeper fall.
# Memory: paid for by unloading Violins I's Leg Port MAX (22,428 regions, A #6 below)
for _t in ("Horn 1", "Horn 2"):
    ART_SPANS[_t] = ART_SPANS.get(_t, []) + [{"from": 0.0, "to": SCORE_END, "art": "StacSs RRx9", "mark": "staccato",
                                              "vel_by_cc": _TSTAC}]
    STAC_LEAD_S[_t] = 0.02
ART_SPANS["Trumpet 2"] = ART_SPANS.get("Trumpet 2", []) + [{"from": 0.0, "to": SCORE_END, "art": "StacSs DblTng RRx9",
                                                            "mark": "staccato", "vel_by_cc": _TSTAC}]
STAC_LEAD_S["Trumpet 2"] = 0.02
LEVEL_SHAPES["Trumpet 2"] = LEVEL_SHAPES.get("Trumpet 2", []) + [[(299.5, 0.0), (299.7, -6.0), (308.75, -2.0), (308.85, 0.0)]]
WIND_REP_RETONGUE_BY = {"Horn 2": {"gap_s": 0.07, "frac": 0.25, "fall_cc": 12, "fall_s": 0.12}, **WIND_REP_RETONGUE_BY}
# critic A #6: the printed "port." at bar 214 played as a plain jump on Leg Port MAX at v100 (pitch track: C sharp 6 held
# to 0.02 s before the beat, F sharp 6 within 10 ms), and that one note loaded 22,428 regions: a Leg Slur MAX target at
# v55 (manual p.144: low legato velocity plays more of the recorded slide); the row unloads (c01-c02 do-not-touch item,
# answered with the pitch-track measurement)
PORT_TARGETS = {k_: v_ for k_, v_ in PORT_TARGETS.items() if k_ != "Violins I"}
LEG_VEL_SPANS = {**LEG_VEL_SPANS, "Violins I": LEG_VEL_SPANS.get("Violins I", []) + [(639.9, 640.1, 55)]}
# critic C #1: theme A's reprise replayed the first statement sample for sample (33 of 48 short notes identical), and the
# head pairs replayed the row's first takes inside each statement. Reprise: phrases 1 and 3 (756-768, 780-792) on the 1st
# Violins "Spiccato RRx9" (manual p.93, the leggiero stroke; 7,929 regions), phrases 2 and 4 (768-780, 792-804) all on
# the theme's "Staccatissimo RRx9" (their c04 Stac RRx14 alternation dropped there, so every reprise phrase uses another
# row than the statement's same phrase); the statement's second-phrase pair (49) on Spiccato too. Listed first (the
# Marc LITE heads are not staccato, so they keep their row)
ART_SPANS["Violins I"] = [{"from": 48.9, "to": 49.6, "art": "Spiccato RRx9", "mark": "staccato"}] + \
    [{"from": a_, "to": b_, "art": r_, "mark": "staccato"}
     for a_, b_, r_ in ((755.9, 768.0, "Spiccato RRx9"), (768.0, 780.0, "Staccatissimo RRx9"),
                        (780.0, 792.0, "Spiccato RRx9"), (792.0, 804.0, "Staccatissimo RRx9"))] + ART_SPANS["Violins I"]
ROW_TRIM_DB["Violins I"] = {**ROW_TRIM_DB["Violins I"], "Spiccato RRx9": (-3.0, 80)}
# critic C #6: Flute 1's fff summit B6 (1005) arrived on Leg Slur MAX and sagged 9 dB in 0.33 s: a fresh Sus MAX (loaded)
# with the woodwind staccato lead
ART_SPANS["Flute 1"] = [{"from": 1004.8, "to": 1005.1, "art": "Sus MAX", "vel_by_cc": [(0, 100), (127, 104)]}] + \
    ART_SPANS.get("Flute 1", [])   # v104, not the fff mark's v127 (weight, not bite)
REATTACK_LEAD_AT["Flute 1"] = {**REATTACK_LEAD_AT.get("Flute 1", {}), 1005.0: 0.02}
# critic C #2: Clarinet 1's trio tune notes that fall out or stick out at the same onsets in both statements (residual
# against a 5-note running median): note trims in build/note_trims.json; the long phrase end (498 / 666) as a step
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Clarinet 1": {**NOTE_TRIM_RAMP_S.get("Clarinet 1", {}), 498.0: 0.02, 666.0: 0.02}}
# ONE_TIME_c08 item 4 (EW template plan section 6; Movement I c51's SHORT_CC11_PARK, ported): the string short rows with
# CC11 parked at 120 and the level returned in the volume envelope (the Global Group CC11 table of all five HS KS
# Masters read from the .oib: 0 -> 0, 8 -> 0.1875, 9-10 -> 0.2, 69 -> 0.5, 127 -> 0.9915), velocities unchanged (HO short
# rows switch layer by velocity); beat weight in the envelope in the Allegro, triple metre: the bar's downbeat +1.5 dB,
# beats 2-3 0, the eighth after a beat -0.5 (critic A: the second of a repeated pair within 1 dB of the first)
_ALLEGRO = [(36.0, 168.0), (168.0, 312.0), (312.0, 420.0), (756.0, 972.0), (972.0, 1005.0)]
SHORT_CC11_PARK = {"families": ("string",), "rows": ("Stac", "Staccatissimo", "Spiccato"), "cc": 120,
                   "gg_amp": [(0, 0.0), (8, 0.1875), (9, 0.2), (10, 0.2), (69, 0.5), (127, 0.99152)], "fade_s": 0.12,
                   "beat_db": {"downbeat": 1.5, "beat": 0.0, "and": -0.5, "sixteenth": -1.0, "meter_qn": 3.0},
                   "beat_spans": {t_: _ALLEGRO for t_ in ("Violins I", "Violins II", "Violas", "Violoncellos",
                                                          "Double basses")}}
# c07 critic C #2.4 (ONE_TIME_c08 item 6): in the solo (349-356) the Violin I solo's joins sat +57 ms late (pcx on c07)
# and Flute 1 "col Vl. solo" -53 ms early. The flute's soft-legato extra (0.06 s) off over the span (new generic
# LEG_SOFT_EXTRA_SKIP); the solo's refit per-onset offsets (build/leg_leads.json) were capped at 0.45 of the previous
# note's slot, so the solo takes the sections' 0.75 cap over its window
LEG_SOFT_EXTRA_SKIP = {"Flute 1": [(1043.5, 1068.0)]}
LEG_CAP_FRAC = {**LEG_CAP_FRAC, "Violin I solo": [(1043.5, 1068.0, 0.75)]}
# critic A #5 (manual p.92; MANUAL-GAPS #14): Violins I's natural harmonic E6 (bars 141-149, ppp "harm., change bow
# freely") played as a stopped vibrato note (H2 +1.3 dB over H1, 7 cents of pitch modulation). The 2nd Violins KS Master
# has a "Harmonics" row (590 regions, keyed at the sounding pitch 79-108, p and mf layers), and Violins II rests over
# qn 394-501: the Violins II track plays the two tied notes on that row (new generic BORROW_NOTES), with Violins I's ppp
# and decrescendo (SHARED_DYN / SHARED_HP); Violins I leaves them out (TRACK_WINDOWS)
BORROW_NOTES = {"Violins II": [("VlnI", 419.5, 446.0)]}
TRACK_WINDOWS = {**TRACK_WINDOWS, "Violins I": ([(1044.0, 1068.0), (419.5, 446.0)], False)}
SHARED_DYN = {**SHARED_DYN, "Violins II": list(SHARED_DYN.get("Violins II", [])) + [(420.0, "ppp")]}
SHARED_HP = {**SHARED_HP, "Violins II": list(SHARED_HP.get("Violins II", [])) + [(438.0, 444.0, "decresc")]}
ART_SPANS["Violins II"] = [{"from": 419.5, "to": 446.0, "art": "Harmonics"}] + ART_SPANS["Violins II"]
REBOW_SAME_ROWS = tuple(REBOW_SAME_ROWS) + ("Harmonics",)   # the harmonic's re-bow (loops 1.8-5.2 s) stays on its row

# ---- c09 (cycles/c09/CHANGES.md) ----
# A #1: the soft theme-head tails (two slurred eighths after the accented half note) as legato targets of the half note
SHORT_SUS_LEG_AT = {"Violins I": [41.0, 41.5, 53.0, 53.5, 71.0, 71.5, 77.0, 77.5, 287.0, 287.5, 761.0, 761.5, 773.0, 773.5,
                                  791.0, 791.5, 797.0, 797.5]}
# A #5: celli transition spikes in the gaps of Violins I's repeated-eighth pairs 763.5 / 799.5 (spike - 2 dB)
JOIN_NOTCH = {**JOIN_NOTCH, "Violoncellos": JOIN_NOTCH.get("Violoncellos", []) + [(763.05, 763.55, -4.0), (799.05, 799.6, -4.5)]}
# A #6: Horn 1's printed breath at 648 (the Port Lng span's re-tongue lead had replaced the gap: 11 ms); 0.335 qn = 88 ms
# at quarter 228. Soft string end (0.31 s, limit 0.30): Violins I's last ppp G sharp fades
# 6 dB over its last 0.25 qn (0.3 s at quarter 50) under the fermata (the end is the dry sample's own ppp fall; NOTE_END_AT
# would move the fitted re-bows of the held note)
NOTE_END_AT = {**NOTE_END_AT, "Horn 1": {646.0: 647.35}}
LEVEL_SHAPES = {**LEVEL_SHAPES, "Violins I": LEVEL_SHAPES.get("Violins I", []) + [[(1127.75, 0.0), (1128.0, -6.0)]]}
# A #4 (reverted in c10: celli +285 -> +367 ms, basses +146 -> +166 ms; the velocity, lead and fill did not help):
# VEL_SET["Double basses"] 504.0 / 1071.0: 53
# B #4 / B #5: these trims as steps (the default 0.6 s ramp reached only part of the trim on a 0.11 s staccato and on
# the held E4's attack)
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Violoncellos": {**NOTE_TRIM_RAMP_S.get("Violoncellos", {}), 111.0: 0.02, 114.0: 0.02},
                    "Clarinet 2": {**NOTE_TRIM_RAMP_S.get("Clarinet 2", {}), 588.0: 0.1, 600.0: 0.1, 603.0: 0.1, 606.0: 0.1}}

# ---- c10 (cycles/c10/CHANGES.md) ----
# C #1: one-beat soft swells (< inside p / dolce, no target) rose 6-11 dB in one beat (Horn 1 441, Clarinet 1 472):
# at quarter 228-264 every one-beat hairpin lasts 0.6 s or less, so the short-hairpin cap applies to crescendos too
HP_SHORT_KINDS = ("decresc", "cresc")
# B #1: the coda build's four-bar p < ff (984-996) reached f two bars early under HP_CURVE (70 % of the rise at 40 %):
# crescendos of more than three and a half bars (not the 9 qn sfp < hemiolas at 300 / 900) reach 35 % of their rise at 60 % of their length (new generic "cresc_long")
HP_CURVE = {**HP_CURVE, "cresc_long": {"min_qn": 10.5, "pt": (0.6, 0.35)}}
# C #3: Horn 1's last G sharp: the decrescendo's -2.5 dB was released 1 qn after its arrival, mid-note, into the fermata
# (new generic HP_DEC_HOLD_HELD); the sample's own +2.7 dB swell over 1124-1126 is taken back in the envelope
HP_DEC_HOLD_HELD = True
LEVEL_SHAPES = {**LEVEL_SHAPES, "Horn 1": LEVEL_SHAPES.get("Horn 1", []) + [[(1123.5, 0.0), (1126.0, -2.5), (1128.0, -2.5)]]}
# A #1: the flutes' staccato quarters were cut by their note-off 7.5 dB under the recorded decay (Stac DblTng has no
# release trail, manual p.110): written quarters held to 0.85 of their value (eighths unchanged)
STAC_LEN_SPANS = {**STAC_LEN_SPANS, "Flute 1": [(0.0, SCORE_END, 0.85, 1.0)], "Flute 2": [(0.0, SCORE_END, 0.85, 1.0)]}
# A #2: Flute 1's sfp at 900 never reached the sf (unslurred Sus MAX at v100 peaked +0.23 s, after the CC11 fall)
VEL_SET["Flute 1"] = {**VEL_SET.get("Flute 1", {}), 900.0: 118}
# (it enters after a rest: 0.03 s more entry lead in entry_leads.json, 0.04 -> 0.07 s)
# A #3 (S1): the Trio return's slurred tenuto horn repeats merged (dips 1.4-2.2 dB): the notes before them end earlier
# (Horn 2: 0.10 s gap instead of 0.07 s; Horn 1: 63 ms before the Port Lng re-attack's moved onset)
NOTE_END_AT = {**NOTE_END_AT, "Horn 1": {**NOTE_END_AT.get("Horn 1", {}), 627.0: 629.42, 630.0: 632.42, 660.0: 662.42},
               "Horn 2": {**NOTE_END_AT.get("Horn 2", {}), 624.0: 626.43, 639.0: 641.43, 648.0: 650.43}}
# A #4 (manual p.144: legato velocity is the transition speed): the celli's espress. trio tune at v80 (was 106 / 112),
# with 0.03 s more lead for the slower transitions (LEG_VEL_EXTRA_S under v85; only this span plays celli targets that soft)
LEG_VEL_SPANS = {**LEG_VEL_SPANS, "Violoncellos": LEG_VEL_SPANS.get("Violoncellos", []) + [(504.5, 552.0, 80)]}
LEG_VEL_EXTRA_S = {"Violoncellos": (85, 0.03), **LEG_VEL_EXTRA_S}
# A #5: Flute 2's low unison repeated eighths (121, 127, 817, 823) blur; trims in note_trims.json as steps, and the
# reprise starts its round robins from a fixed position
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Flute 2": {**NOTE_TRIM_RAMP_S.get("Flute 2", {}),
                                                    **{q_: 0.02 for q_ in (121.0, 121.5, 127.0, 127.5, 817.0, 817.5, 823.0, 823.5)}}}
RR_RESET_AT = {**RR_RESET_AT, "Flute 2": [817.0]}
# A #6: the soft heads 51 / 75: the first slurred eighth 10 dB under the half note: v100 (faster transition) and +3 dB
VEL_SET["Violins I"] = {**VEL_SET["Violins I"], 53.0: 100, 77.0: 100}
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Violins I": {**NOTE_TRIM_RAMP_S.get("Violins I", {}), 53.0: 0.02, 77.0: 0.02}}
# B #4: the celli trio entry's second note (v106 target at the top of the first note's rise) spiked 5-10 dB
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Violoncellos": {**NOTE_TRIM_RAMP_S["Violoncellos"], 506.0: 0.02}}
# B #5: the reprise's violas pizz. beat-2 notes (note_trims +3) as steps
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Violas": {**NOTE_TRIM_RAMP_S.get("Violas", {}),
                    **{q_: 0.02 for q_ in (757.0, 760.0, 763.0, 766.0, 769.0, 772.0, 775.0, 781.0, 784.0, 787.0, 790.0,
                                           793.0, 796.0, 799.0)}}}
# C #2: bar 45's strings: the < peaked on the accented first note (accent fits 4.5 -> 1.0 in accent_fits.json); the
# strings take the shape the winds have
for _t in ("Violins I", "Violins II", "Violas", "Violoncellos"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(133.0, 0.0), (136.0, 2.0), (137.0, 2.0), (141.0, 0.0)]]
# C #4 (manual p.69: CC11 and velocity set the harp's loudness): the harp's hairpins sound in the volume envelope
# (soft-hairpin ramps for the harp family, the p espress. line of bars 73-80 as a lead span, 4 dB at its two crests)
HP_GAIN_SOFT_DB = {**HP_GAIN_SOFT_DB, "harp": 3.0}
HP_SOFT_EXTRA_SPANS = {**HP_SOFT_EXTRA_SPANS, "Harp": [(216.0, 240.0)]}
HP_SOFT_GAIN_AT = {**HP_SOFT_GAIN_AT, "Harp": {216.0: 4.0, 228.0: 4.0}}
# C #5: the pp < f roll of bars 205-208 grew only 2 dB under its crescendo after rising 3 dB with none printed: the c02
# -3 dB over 621-624 is removed and the roll's own build before 618 is flattened
LEVEL_SHAPES["Timpani"] = [r_ for r_ in LEVEL_SHAPES["Timpani"] if r_ != [(620.0, 0.0), (621.0, -3.0), (623.9, -3.0), (624.0, 0.0)]] + \
    [[(612.5, 0.0), (617.5, -3.0), (618.5, 0.0)]]
# ONE_TIME item 10 (Movement I c51 item 2): phrase-shape offsets on the winds x1.4 (new generic "family_scale")
PHRASE_SHAPE = {**PHRASE_SHAPE, "family_scale": {"wind": 1.4}}
# c10 stem fix (measured on the c10 render): the one-beat swells kept most of their rise after the CC cap (C #1:
# Horn 1 441 +7.3 dB, Clarinet 1 472 +8.7, Horn 3 1029.5 +7.9 over the note before): level shapes over each crest
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(440.2, 0.0), (440.9, -2.5), (441.7, -2.5), (442.3, 0.0)]]
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES.get("Clarinet 1", []) + [[(471.0, 0.0), (471.9, -3.5), (473.5, -3.5), (474.3, 0.0)]]
LEVEL_SHAPES["Horn 3"] = LEVEL_SHAPES.get("Horn 3", []) + [[(1028.2, 0.0), (1029.0, -3.0), (1029.9, -3.0), (1030.5, 0.0)]]

# ---------- c11 (actor, on the c10 render; cycles/c11/CHANGES.md) ----------
# critic B #1 (c10 regression): the winds' x1.4 phrase-shape scale multiplied the clarinets' CC1 arch, and CC1 is their
# dynamic-layer lane (Clarinets 1-2 +2.6..+4.5 dB in bars 46-52, Clarinet 1 +2.7..+3.9 in 210-211). New generic
# "family_scale_skip_cc1": the scale stays on the winds whose phrase shape is in CC11
PHRASE_SHAPE = {**PHRASE_SHAPE, "family_scale_skip_cc1": True}
# critics A #1 / C #1: the note after a slurred eighth came 0.1-0.27 s late in the strings: its lead was capped at
# 0.375 qn of the eighth's printed length while the eighth itself started a full lead early (new generic
# LEG_CAP_FROM_MOVED: the cap is measured from the previous note's moved onset). Not the solo violin (not flagged).
# Violins II only after notes of an eighth or shorter: its runs of quarters measured on time on c10 at the capped lead
# (median -2 ms at 197 ms; the full 240 ms would put them 45 ms early). Violins I, violas and celli at any length:
# their runs of quarters measured +30..+66 ms late at the capped 170 ms (cycles/c11/actor_scripts/predict11.py)
LEG_CAP_FROM_MOVED = {"Violins I": None, "Violas": None, "Violoncellos": None, "Violins II": 0.5}
# critic C #6: the last rit. (bars 370-375) kept slowing through its last printed step, held two bars (new generic)
RAMP_LAST_STEP_HOLD_QN = 6.0
# finale c11 technique 20 (SHARED-TECHNIQUES): a listed per-onset legato offset is added to base + extras before the clamp
LEG_LEAD_CLAMP_TOTAL = True
# critics A #4 / C #3: Violins I legato joins measured 30-50 ms behind the beat (previous pitch excluded; Leg Slur MAX
# median +38 ms, Leg BC MAX +9): one row extra, as Violins II / violas / celli have. The 36 Leg Slur MAX joins already
# fitted in leg_leads.json lose the same 0.04 s there (apply11.py), so their leads do not move
LEG_ART_EXTRA_S = {**LEG_ART_EXTRA_S, "Violins I": {**LEG_ART_EXTRA_S.get("Violins I", {}), "Leg Slur MAX": 0.04}}
# A #4: the celli's trio tune at v80 still joined +39 ms late (c10's 0.03 s extra under v85): 0.06 s
LEG_VEL_EXTRA_S = {**LEG_VEL_EXTRA_S, "Violoncellos": (85, 0.06)}
# ONE_TIME_c11 item 14: Flute 2's Leg Slur MAX joins measured +40 ms median against Flute 1's +2 ms at the same 0.03 s lead
LEG_LEAD_S = {"Flute 2": 0.07, **LEG_LEAD_S}
# critics A #3 / C #4, ONE_TIME_c11 item 13: the sfp hemiola of bars 301-302.
# 904: the strokes (Sus MAX at CC11 94) spoke 60-80 ms after the note-on and had 0.20-0.25 s of lead (pcX -122..-190 ms)
REATTACK_LEAD_AT["Violins II"] = {**REATTACK_LEAD_AT["Violins II"], 902.0: 0.09, 904.0: 0.09}
REATTACK_LEAD_AT["Violas"] = {**REATTACK_LEAD_AT["Violas"], 902.0: 0.07, 904.0: 0.07}
REATTACK_LEAD_AT["Violoncellos"] = {**REATTACK_LEAD_AT["Violoncellos"], 902.0: 0.09, 904.0: 0.09}
REATTACK_LEAD_AT["Double basses"] = {**REATTACK_LEAD_AT.get("Double basses", {}), 902.0: 0.08}
# 902: the accent was missing in Violins II, violas and celli: their strokes start at CC11 63 (the p after the sfp) and
# spoke 211-377 ms after the note-on behind a 14-18 dB hole (Violins I, on the Sus Marc LITE row, was on time). Strokes
# at CC11 75 or more speak in 60-110 ms on these patches, and a volume swell does not change the time (new generic
# ACCENT_CC_AT): CC11 +22 at the stroke, back to the curve 0.5 qn after the beat, with leads for the faster attack
# (0.20 / 0.18 / 0.20 s before). The -3 dB body cuts at 902 are removed and a +3 dB swell is fitted (accent tables)
for _t in ("Violins II", "Violas", "Violoncellos"):
    ACCENT_CC_AT[_t] = {**ACCENT_CC_AT.get(_t, {}), 902.0: (22, 0.5)}
# 900: the basses were left out of c09's sf stroke: note-on at CC11 52 (the p point before the spike), pcX +115 ms.
# ABUT_LEAD ends the ff note before and starts the stroke 0.08 s early on the spike (FP_SPIKE_FROM_ONSET)
ABUT_LEAD["Double basses"] = {"lead_s": 0.08, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": False,
                              "at": sorted(set(ABUT_LEAD.get("Double basses", {}).get("at", []) + [900.0]))}
# 900: sf fronts short of the other sections' on c10 (first 0.1 s against 901.5: Violins II +4 dB short; Flute 1's sf
# open since c10): level bumps in the finale's form (technique 13), from the moved onset, gone before the p
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [[(899.6, 0.0), (899.65, 4.0), (900.1, 4.0), (900.5, 0.0)]]
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES.get("Flute 1", []) + [[(899.64, 0.0), (899.69, 3.0), (900.5, 3.0), (900.9, 0.0)]]
# critics A #2 / C #2: Horn 1's call (bars 3-5): the E4 at qn 9 swelled 4-5 dB after its attack and the G#3 at 6 was
# late (leads in leg_leads.json / entry_leads.json): a level shape over the E4 that takes the sample's swell back.
# The swell belongs to the E4's own sample (CC1 and CC11 move 3 and 8 steps over the note), so it follows the note-on:
# on c10 (note-on 8.74) the level per 0.25 qn was -34.7 at 10.0, -36.2 at 11.0, -32.9 at 12.0, -34.3 at 12.75, -41.8
# at 13.5; with the c11 lead the note-on is 0.44 qn earlier and the shape is placed for that. The D#4 at 14 entered
# 2 dB over the E4's end: -2 dB over its first half beat
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(9.6, 0.0), (10.0, -1.0), (10.6, -1.0), (11.5, -5.9), (12.0, -6.6),
                                                    (12.3, -6.0), (13.0, 0.0), (13.6, 0.0), (14.0, -2.0), (14.3, -1.5),
                                                    (14.7, 0.0)]]
# critic B #5: Oboe 2's F5 at 903 (sfp <) was 6.1 / 5.4 / 6.6 / 3.1 / 1.2 / 3.3 dB over Oboe 1 per half beat on c10; B's
# -3 note trim with a 0.1 s ramp left +4.6 / +2.4 / +3.6 in the simulation (the difference falls over the bar), so the
# cut is a shape (finale technique 22: use a level shape where a note trim falls short)
LEVEL_SHAPES["Oboe 2"] = LEVEL_SHAPES.get("Oboe 2", []) + [[(902.7, 0.0), (902.95, -5.5), (904.2, -5.5), (904.8, -2.0),
                                                            (905.9, -2.0), (906.1, 0.0)]]
# open since c10 (horns' slurred tenuto repeats, bars 209-222; A #5 proposed the "Leg Slur Rep MAX" row, +0.25 GB:
# rejected, CHANGES.md). Measured against the note before (not the c10 metric), Horn 2's repeats already dip 3.3-5.8 dB
# and Horn 1's Port Lng repeats have 13-14.5 dB holes (limit 8): Horn 1's notes before them end 20 ms before the
# re-attack's moved onset instead of 63 ms
NOTE_END_AT = {**NOTE_END_AT, "Horn 1": {**NOTE_END_AT.get("Horn 1", {}), 627.0: 629.58, 630.0: 632.58, 660.0: 662.58}}
# critic B #2 (basses' arco G#1) / B #5 (Oboe 2's F5): bowed / blown note trims act from the attack (default ramp 0.6 s)
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S,
                    "Double basses": {**NOTE_TRIM_RAMP_S.get("Double basses", {}), 142.0: 0.1, 507.0: 0.1, 531.0: 0.1, 651.0: 0.1},
                    "Oboe 2": {**NOTE_TRIM_RAMP_S.get("Oboe 2", {}), 900.0: 0.1, 990.0: 0.1}}
# A #2: Horn 1's G#3 at qn 6 (a re-tongue after a 0.13 qn gap) sounded +84 ms late with the track's 0.09 s
RETONGUE_LEAD_AT = {**RETONGUE_LEAD_AT, "Horn 1": {**RETONGUE_LEAD_AT.get("Horn 1", {}), 6.0: 0.13}}
# c10's +5.5 dB trims on the theme-head eighths at 53 / 77 (A #6) ended at the next note-on, which the c11 leads put before
# the trimmed eighth's own score onset (realised +3.5 dB): the plateau lasts to 0.025 s before the next score onset, as on c10
LEG_JOIN_TRIM_HOLD_TO_AT = {**LEG_JOIN_TRIM_HOLD_TO_AT, "Violins I": {53.5: 0.025, 77.5: 0.025}}
# ONE_TIME_c11 item 3 (finale technique 15): three ramps of the delivery rows ran against a printed hairpin
# (cycles/c11/actor_scripts/ride_ramps11.py). Row at 300: its 2 dB fall lay over the first bar of the tutti crescendo
# 300-310 (delivered step bar 101 -> 102 +1.7 dB, master +2.8): the fall is now in the 0.4 qn before the subito f.
# Row at 587: its fall lay in the last bar of the crescendo 576-588 (delivered bar 196 -> 197 -0.6 dB, master +1.3): it is
# spread over the whole crescendo. Row at 659: its return lay in the last bar before the pp codetta at 672 (delivered
# 669 -> 672 +0.3 dB, master -1.7): it is spread over the diminuendo 666-672. Rows replaced by their first qn
_c11_rows = {300.0: [(299.6, 0.0), (300.0, -2.0), (311.6, -2.0), (312.4, 0.0)],
             587.0: [(576.0, 0.0), (588.0, -2.0), (601.0, -2.0), (602.0, 0.0)],
             659.0: [(659.0, 0.0), (660.0, -2.0), (666.0, -2.0), (672.0, 0.0)]}
assert all(any(r_[0][0] == q_ for r_ in RIDE_TRIMS) for q_ in _c11_rows), "RIDE_TRIMS: a c11 row has no row to replace"
RIDE_TRIMS = [_c11_rows.get(r_[0][0], r_) for r_ in RIDE_TRIMS]

# ---------------------------------------------------------------------------------------------------------------------
# cycle 12 (cycles/c12/CHANGES.md has the measured reasons)
# critic A #2 (harp tune, bars 73-80): Sus RR alternates Pluck Long and Thumb Pick from note to note, and at the capped
# velocity 56 the tune's notes read -5.4 to +8.4 dB around their median (600-5000 Hz, first 100 ms, c11 stem; the same
# to 0.1 dB in c08). Per-onset velocities for the tune's top voice only (56 - deviation / 0.6, A's table; keys are
# (qn, pitch) so the notes under the tune keep the cap's 56). Valid while no harp note is added before qn 216 (the
# alternation counts notes). The first note (qn 216) also gets +5 dB on its attack (note_trims.json, critic C #5).
# critic C #5's shift of the span caps (subtract span top - cap, floors 43 / 30) was built into the tool and generated:
# 45 of 53 notes of bars 73-80 landed on the floor 43 (the hairpin takes the span's top to 98), 76 of 82 in bars
# 153-168 at 30-33, and the usual note fell by 7-22 steps (3-7 dB at 0.3-0.6 dB per step) in every span. That neither
# keeps the differences nor holds the levels of the caps (A's Do-not-touch), so the rows stay three-value clip rows.
_c12_harp = {216.0: (81, 65), 217.0: (77, 54), 218.0: (81, 52), 219.0: (84, 61), 221.0: (82, 62), 221.5: (81, 61),
             222.0: (79, 57), 223.0: (74, 63), 224.0: (79, 54), 225.0: (82, 56), 227.0: (81, 52), 227.5: (79, 58),
             228.0: (77, 53), 229.0: (72, 57), 230.0: (77, 42), 231.0: (81, 52), 233.0: (79, 56), 233.5: (77, 53),
             234.0: (76, 54), 235.0: (79, 54), 236.0: (82, 63), 237.0: (81, 59)}
VEL_SET = {**VEL_SET, "Harp": {**VEL_SET.get("Harp", {}), **{(q_, p_): v_ for q_, (p_, v_) in _c12_harp.items()}}}
# critic A #1 (timpani): in a hand-alternated figure the left-hand strokes (the plain keys) read 3.4-8.0 dB under the
# right-hand strokes (the keys two octaves up) at the same velocity up to 79, so the downbeat stroke of motive x was the
# weakest of each statement (30 of 30). Velocity steps added to those left-hand strokes, by velocity band
TIMP_RH_ALT = {**TIMP_RH_ALT, "lh_vel_add": [(55, 10), (63, 8), (71, 4), (79, 6)]}
# critic A #3 (timpani): the summit roll (bar 336) fell 4 dB over its last beat and the stroke that ends it (qn 1008) read
# 6 dB under the roll's start: the roll's rise continues to its end, and the stroke after it gets +5 dB at full value
LEVEL_SHAPES["Timpani"] = [r_ for r_ in LEVEL_SHAPES["Timpani"]
                           if r_ != [(1005.7, 0.0), (1006.0, 5.0), (1007.0, 8.0), (1007.85, 8.0), (1007.9, 0.0)]] + \
    [[(1005.7, 0.0), (1006.0, 5.0), (1007.0, 10.0), (1007.5, 12.0), (1007.85, 15.0), (1007.9, 0.0)],
     [(1007.97, 0.0), (1008.0, 5.0), (1008.45, 5.0), (1008.5, 0.0)]]
assert len(LEVEL_SHAPES["Timpani"]) == len({str(r_) for r_ in LEVEL_SHAPES["Timpani"]}), "Timpani LEVEL_SHAPES: duplicate row"
# critic C #1: three legato transitions louder than the notes on each side (celli 505.5 +7, 569.5 +5; Clarinet 1 459 +4)
# and Horn 1's arrival at 1077, 6 dB over its phrase
JOIN_NOTCH = {**JOIN_NOTCH,
              "Violoncellos": JOIN_NOTCH.get("Violoncellos", []) + [(505.5, 506.0, -7.0), (569.4, 569.9, -5.0)],
              "Clarinet 1": JOIN_NOTCH.get("Clarinet 1", []) + [(458.95, 459.2, -4.0)]}
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(1076.75, 0.0), (1076.85, -6.0), (1077.4, -6.0), (1078.0, 0.0)]]
# critic B #2: the violins' pickup eighth before bars 129 / 285 was 4-8 dB over its own downbeat
# critic B #3: Violins I's C6 at qn 69 / 789 stood 4-4.5 dB over the line
# critic B #4: Violins I's closing note fell in one step at bar 373 (the role row 1116-1128, removed in roles.json by
# cycles/c12/actor_scripts/apply12.py): the same 2.5 dB now falls over bars 372-374
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [
    [(383.42, 0.0), (383.47, -6.0), (383.93, -6.0), (383.99, 0.0)], [(851.42, 0.0), (851.47, -6.0), (851.93, -6.0), (851.99, 0.0)],
    [(68.6, 0.0), (69.0, -4.5), (70.0, -4.5), (70.08, 0.0)], [(788.6, 0.0), (789.0, -4.0), (790.0, -4.0), (790.08, 0.0)],
    [(1113.0, 0.0), (1122.0, -2.5), (1128.0, -2.5)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [
    [(383.42, 0.0), (383.47, -9.5), (383.93, -9.5), (383.99, 0.0)], [(851.42, 0.0), (851.47, -9.5), (851.93, -9.5), (851.99, 0.0)]]
# critic B #4: Horn 1's last note (bars 367-376) swelled and sagged by 2-3.5 dB under a flat lane (the sample's own
# shape, measured on c11): two correction shapes (valid while the note's moved onset 1100.772 and its CC1 stay)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [
    [(1111.7, 0.0), (1112.9, -3.5), (1114.5, -3.3), (1115.2, -2.4), (1116.6, -2.4), (1117.3, -1.5), (1118.6, -0.6), (1120.5, 0.0)],
    [(1120.5, 0.0), (1122.3, 2.5), (1122.9, 2.5), (1123.4, 1.8), (1124.0, 0.6), (1124.6, 0.8), (1125.07, 2.5), (1125.3, 2.0),
     (1125.5, 0.5), (1125.7, -0.7), (1126.3, -0.7), (1126.6, 0.7), (1127.0, 0.0)]]
# critic C #3: Oboe 1's first note of its trio statement (qn 552, +5 dB in note_trims.json) is raised from its attack;
# the celli's first trio note (qn 504) rose for 0.3 s: the legato-velocity span starts before it (velocity 80, not 63)
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Oboe 1": {**NOTE_TRIM_RAMP_S.get("Oboe 1", {}), 552.0: 0.1}}
LEG_VEL_SPANS = {**LEG_VEL_SPANS, "Violoncellos": [(503.3, 552.0, 80) if r_ == (504.5, 552.0, 80) else r_
                                                    for r_ in LEG_VEL_SPANS["Violoncellos"]]}
assert (503.3, 552.0, 80) in LEG_VEL_SPANS["Violoncellos"]
# critic C #4: the accented half notes of the two ff tuttis (Violins I / II, Sus MAX) started 2-5 dB under their own
# body (stem, first 80 ms against 100-200 ms; level peak 160-260 ms after the beat, perceived onset +19..+53 ms). The
# family's swell (full from 0.03 to 0.15 s, gone by 0.4 s) weighs both windows alike, and a body cut starts at 0.18 s,
# after the measured body. Now: a longer entry lead (0.06 s -> 0.09-0.11 s; the notes enter after a rest, so the extras
# are in entry_leads.json, cycles/c12/actor_scripts/apply12.py) and a swell at full value on the beat that is gone by
# 0.24 s (ACCENT_DB_AT + ACCENT_SWELL_S_AT replace the fitted swells of 4.5 / 0.0 dB there)
_c12_acc = {"Violins I": (315.0, 327.0, 915.0, 927.0), "Violins II": (315.0, 327.0, 915.0, 927.0, 345.0, 945.0)}
for _t, _d in _c12_acc.items():
    ACCENT_DB_AT[_t] = {**ACCENT_DB_AT.get(_t, {}), **{q_: 4.5 for q_ in _d}}
    ACCENT_SWELL_S_AT[_t] = {**ACCENT_SWELL_S_AT.get(_t, {}), **{q_: (0.0, 0.08, 0.24) for q_ in _d}}
# lost horn attacks of c11's first render (Horn 1 qn 155.6 / 164.6, Horn 4 251.8): each was the first note of a slur on
# a legato row whose note before, on another row, ended 6.8-13.6 ms earlier, so the legato script could take it as
# joined and play the sustain layer's slow attack with no transition (a 0.5 s hole). The note before such a first note
# now ends at least 0.032 s (three 512-sample blocks) before it; winds and brass only (the strings' short gaps carry
# fitted leads and re-bow fills and were not reported)
LEG_HEAD_MIN_GAP_S = {"wind": 0.032, "brass": 0.032}
# ONE_TIME c12 item 2 (the sf of the sfp at bar 301, qn 900, on the woodwinds): on c11 the first 0.1 s of the sf read
# 5.4-8.2 dB under each track's own ff accent of bar 300 on Flute 1 (with c11's +3 dB bump), Flute 2, Oboe 1 and
# Clarinet 1 (the other woodwinds within 2 dB or over; the horns are marked p there, trumpets and trombones rest).
# Post-fader bump over 0.35 qn: +3 dB on Flute 2, Oboe 1, Clarinet 1; Flute 1's +3 becomes +4 (the weakest front).
# The Cor anglais enters on that note with no lead (first 0.1 s -52 dB, half level 106 ms late): entry lead in
# entry_leads.json (cycles/c12/actor_scripts/apply12.py)
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES["Flute 1"] + [[(899.64, 0.0), (899.69, 1.0), (900.35, 1.0), (900.75, 0.0)]]
for _t, _on in (("Flute 2", 899.758), ("Oboe 1", 899.758), ("Clarinet 1", 899.846)):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(_on - 0.05, 0.0), (_on, 3.0), (900.35, 3.0), (900.75, 0.0)]]
# ONE_TIME c12 item 29 (the basses' arco E2 reads 4.9 dB under the track's other pitches at the same CC11: +3 dB note
# trims in note_trims.json): the default 0.6 s ramp is as long as a three-beat note at this tempo (the trim reached
# +1.7 dB at the end of the note at 140), so these trims ramp in over 0.1 s
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Double basses": {**NOTE_TRIM_RAMP_S.get("Double basses", {}),
                    **{float(_q): 0.1 for _q in (140, 150, 504, 513, 624, 633, 666, 1071, 1074, 1077, 1080)}}}

# ONE_TIME c12 item 16 (Movement II c49: a round-robin reset inside the score is repeatable): c11 found single staccato
# woodwind notes 1-6 dB apart between two renders of the same data at 317-357 and 912-958 (the take order moved). A reset
# before the first "Stac DblTng RRx9" note of each passage on the five tracks that play it
RR_RESET_AT = {**RR_RESET_AT, **{_t: sorted(set(RR_RESET_AT.get(_t, []) + [312.0, 912.0]))
                                 for _t in ("Flute 1", "Flute 2", "Oboe 1", "Cor anglais", "Clarinet 2")}}

# c12 (orchestrator: why is the post-render save stale): after the c10 and c11 renders the stale tracks were ones that
# left their legato row 2-70 ms after their last legato note and re-attacked the same pitch in "Sus MAX"; no track whose
# legato row was still selected at the end was stale. Test in this render: three of the tracks stale after both
# renders get their legato row's keyswitch again 5 qn after the score's end; Horn 4 and Violoncellos (stale after
# c11) and the Contrabassoon (stale after c10) stay as they were, as controls. Result in cycles/c12/CHANGES.md
END_LEG_KS = {"Violins I": 5.0, "Violas": 5.0, "Bassoon 2": 5.0}

# c12 (coordinator, mvt2 c50 finding 1): Horn 3's +3 dB pitch trim on F#3 sits on legato targets (323, 356, 800, 923, 956)
PITCH_TRIM_MIRROR = {"Horn 3"}

# ---- c13 (cycles/c13/CHANGES.md) ----
# critic A #4 / ONE_TIME_c13 items 2 and 5c: the 22 BEAT_STRETCH beats of c07 (6-18 % long, +0.53 s in all) are tempo
# changes the score does not print; removed. The printed changes (RAMP_SPANS, the fermatas, the G.P.) stay
BEAT_STRETCH = {}
# ONE_TIME_c13 item 6: the trailing legato keyswitch test of c12 failed (the treated tracks were stale again)
END_LEG_KS = {}
# critic A #2 (new generic LEG_HEAD_AFTER_ROW_LEAD_S): 62 legato-row notes that follow a note on another row had no lead
# and sounded +30..+186 ms late by measure S (bar 49 beat 1 in three string sections, Violas 382 / 850, the woodwinds'
# first slurred eighth after the Sus MAX half note of each loud theme head). Values: A's, 0.85 of the measured lateness
# (strings per onset, winds one value per track); other string notes of the class 0.10 s. The lead is at most half of
# 0.3 of the previous note's written length (after an eighth pickup: 34 ms, so bar 49's downbeat gets 34 of the 120 ms
# asked; at 0.5 the Sus MAX pickup before it was cut from 171 to 85 ms, which ends it as it starts to speak). On
# the winds the note before ends 32 ms before the moved onset (LEG_HEAD_MIN_GAP_S's value); the strings keep the
# 0.01 qn gap they were rendered with
LEG_HEAD_AFTER_ROW_LEAD_S = {
    "string": 0.10, "Flute 1": 0.035, "Flute 2": 0.05, "Oboe 1": 0.055, "Cor anglais": 0.05, "Clarinet 2": 0.055,
    "wind": 0.05, "gap_s": {"wind": 0.032}, "cap_frac": 0.3,
    "at": {"Violins I": {144.0: 0.12, 157.5: 0.08, 385.5: 0.04, 853.5: 0.04},
           "Violins II": {144.0: 0.115, 157.5: 0.08, 385.5: 0.04, 853.5: 0.04},
           "Violas": {144.0: 0.12, 382.0: 0.15, 387.0: 0.10, 618.0: 0.12, 840.0: 0.05, 850.0: 0.155, 855.0: 0.12},
           "Violoncellos": {192.0: 0.12, 840.0: 0.14, 853.0: 0.085, 144.0: 0.04}}}
# critic A #3: three joins after a slurred eighth were held by the lead cap (Violins II 372: 74 ms lead, +180 ms;
# Violin I solo 1052 / 1061.5: 99 ms leads, +87 / +107 ms). The solo's cap is measured from the moved onset after
# notes of an eighth or shorter (as Violins II); Violins II 372 gets the whole slot. The rows in leg_leads.json aim at
# half of the lateness: the eighth before each must still be heard (a transition takes longer than the eighth lasts)
LEG_CAP_FROM_MOVED = {**LEG_CAP_FROM_MOVED, "Violin I solo": 0.5}
LEG_CAP_FRAC = {**LEG_CAP_FRAC, "Violins II": [(371.9, 372.1, 1.0)] + LEG_CAP_FRAC["Violins II"]}
# critic A #3: Flute 2's joins in bars 305-320 read +30 ms median against Flute 1's +6 on the same notes (10 of 43
# 65-114 ms late, all with the same 51 ms lead): one row lead more per track, no per-onset rows (Movement II c51)
LEG_ART_EXTRA_S = {**LEG_ART_EXTRA_S, "Flute 2": {"Leg Slur MAX": 0.03}}
# critic A #1 (5): the violins' slurred Sus MAX eighth pairs of the two ff tuttis read -33 / -36 ms (median) at the
# 0.06 s lead: Violins I 0.03 (its soft pairs are legato targets, SHORT_SUS_LEG_AT), Violins II 0.045 (its soft pair
# at 197.5 read +40). (4): the celli's fugato pairs at 173 / 869: the first eighth's slot was nearly empty (-60 dB
# against the half note's -48) and the second +101 ms late on Sus MAX: the first eighth becomes a legato target of the
# Leg Slur MAX half note, the second gets 0.10 s more lead and +4 dB (LEVEL_SHAPES below: the note lasts 0.11 s)
_c13_loud = [q_ + h_ for q_ in (125.0, 317.0, 329.0, 343.0, 347.0, 353.0, 821.0, 917.0, 929.0, 943.0, 947.0, 953.0, 1001.0)
             for h_ in (0.0, 0.5)]   # the v100 pairs only: the soft Sus MAX pairs keep 0.06 (they speak later)
SHORT_SUS_LEAD_AT = {"Violoncellos": {173.5: 0.16, 869.5: 0.16},
                     "Violins I": {q_: 0.03 for q_ in _c13_loud + [209.0, 209.5, 893.0, 893.5]},
                     "Violins II": {q_: 0.045 for q_ in _c13_loud}}
SHORT_SUS_LEG_AT = {**SHORT_SUS_LEG_AT, "Violoncellos": [173.0, 869.0]}
# critic A #5: same-pitch staccato eighth pairs that did not separate on the stem (trumpets median 3.4 / 2.6 dB, 5 and
# 7 of 10 under 3; celli coda pairs 0.1-1.2 dB; Violins II 985.5-994.5 -0.3..0.8): the printed staccatos of those
# passages at 0.7 of their MIDI length (40 ms eighths, 80 ms quarters at quarter 264)
STAC_LEN_SPANS = {**STAC_LEN_SPANS,
                  "Trumpet 1": [(300.0, 360.0, 0.7), (900.0, 960.0, 0.7), (984.0, 1008.0, 0.7)],
                  "Trumpet 2": [(300.0, 360.0, 0.7), (900.0, 960.0, 0.7), (984.0, 1008.0, 0.7)],
                  "Violoncellos": [(972.0, 1008.0, 0.7)], "Violins II": [(984.0, 996.0, 0.7)]}
# critic A #6 (new generic KS_MIN_LEAD_S): 600 of 1,263 keyswitches sat under 8 ms before their note (0.03 qn at quarter
# 264; one audio block is 10.7 ms), and the two notes that changed between the c11 and c12 renders on identical data
# both follow such a keyswitch.
# Coordinator (finale c13, SHARED-TECHNIQUES 37-39): a keyswitch 45 ms early did not stop level changes between renders
# there, so the keyswitches are not moved wholesale: one-track range test on Horn 1 only (environment variable
# C13_KS_EARLY=1 builds the test data; two renders of each state; result in cycles/c13/CHANGES.md). Off in the data
# Coordinator (Movement II c52 A): string joins that move between renders of identical data are legato targets whose
# row differs from the row of the note they overlap. Test on the celli's trio tune (paired range renders): keyswitch
# 0.15 s early (C13_KS_EARLY=1) and one legato row for the line (C13_VC_ONE_ROW=1)
KS_MIN_LEAD_S = {"Violoncellos": 0.15} if __import__("os").environ.get("C13_KS_EARLY") == "1" else {}
if __import__("os").environ.get("C13_VC_ONE_ROW") == "1":
    ROW_REMAP["Violoncellos"] = {"Leg BC MAX": "Leg Slur MAX"}

# critic B #1: Violins I's hemiola half notes on Sus Marc LITE were 4-9.5 dB over Violins II an octave lower and at
# the section's fff level (300-312 -22.7..-16.6, 900-912 -21.6..-14.8 against -21..-23.5 in the ff theme): level
# steps -5 -> -8 and -2 -> -6.5
_c13_v1 = {str([(299.3, 0.0), (299.4, -5.0), (311.9, -5.0), (312.0, 0.0)]): [(299.3, 0.0), (299.4, -8.0), (311.9, -8.0), (312.0, 0.0)],
           str([(900.95, 0.0), (901.05, -2.0), (911.9, -2.0), (912.0, 0.0)]): [(900.95, 0.0), (901.05, -6.5), (911.9, -6.5), (912.0, 0.0)],
           # critic B #2: c12's pickup rows left the pickup 8.4 / 8.6 dB under its downbeat: -6 -> -3
           str([(383.42, 0.0), (383.47, -6.0), (383.93, -6.0), (383.99, 0.0)]): [(383.42, 0.0), (383.47, -3.0), (383.93, -3.0), (383.99, 0.0)],
           str([(851.42, 0.0), (851.47, -6.0), (851.93, -6.0), (851.99, 0.0)]): [(851.42, 0.0), (851.47, -3.0), (851.93, -3.0), (851.99, 0.0)]}
_n = len(LEVEL_SHAPES["Violins I"])
LEVEL_SHAPES["Violins I"] = [_c13_v1.pop(str(r_), r_) for r_ in LEVEL_SHAPES["Violins I"]]
assert not _c13_v1 and len(LEVEL_SHAPES["Violins I"]) == _n, "c13: a Violins I LEVEL_SHAPES row was not found"
# critic B #2: the staccato pickup at 155.5 (Stac RRx14, v109: 7-9 dB over the ff downbeat, the only event outside the
# tuttis in the master's top 45 peaks) -8; the f head notes at 204 / 888 (7 dB over the same pitch two beats later) -4.5
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [
    [(155.2, 0.0), (155.25, -8.0), (155.93, -8.0), (155.99, 0.0)],
    [(203.7, 0.0), (203.75, -4.5), (204.6, -4.5), (204.7, 0.0)], [(887.7, 0.0), (887.75, -4.5), (888.6, -4.5), (888.7, 0.0)]]
_c13_v2 = [[(383.42, 0.0), (383.47, -9.5), (383.93, -9.5), (383.99, 0.0)], [(851.42, 0.0), (851.47, -9.5), (851.93, -9.5), (851.99, 0.0)]]
assert all(r_ in LEVEL_SHAPES["Violins II"] for r_ in _c13_v2)
LEVEL_SHAPES["Violins II"] = [[(a_, -7.5 if v_ == -9.5 else v_) for a_, v_ in r_] if r_ in _c13_v2 else r_
                              for r_ in LEVEL_SHAPES["Violins II"]]
# critic B #3: the first stroke of the timpani's soft statements of motive x still 3-8 dB under the other three by
# peak (c12's lh_vel_add closed part of it): level steps over the first stroke (as the f statements have at 270 / 279).
# The p solo of bars 9-12 (+7) is in roles.json
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [
    [(q_ - 0.08, 0.0), (q_ - 0.05, d_), (q_ + 0.9, d_), (q_ + 0.95, 0.0)]
    for q_, d_ in ((288.0, 2.0), (291.0, 4.5), (294.0, 6.0), (297.0, 3.0), (720.0, 3.0), (738.0, 4.0), (744.0, 5.0))]
# critic A #1 (4): the celli's second fugato eighth, 5-9 dB under the quarter after it
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES.get("Violoncellos", []) + [
    [(q_ - 0.12, 0.0), (q_ - 0.06, 4.0), (q_ + 0.3, 4.0), (q_ + 0.36, 0.0)] for q_ in (173.5, 869.5)]

# critic A #1 (1-3): the nine soft theme-head pairs of Violins I (two slurred eighths, the second heard 2-74 ms) on the
# "Slur Runs" row, paid for by unloading Leg BC MAX (ROW_REMAP to Leg Slur MAX). Tested in c13 with a one-track range
# render of bars 13-28 before the full render (the result is in cycles/c13/CHANGES.md); _C13_SLUR_RUNS holds the
# decision (below)
import os as _os
# Coordinator (Movement I c54, mockup-kit README "Steady rhythm in fast string themes"): one row for the whole line
# cured the uneven theme there (Sus Marc LITE, slurred notes 90 ms early). Third variant of the same range test: the two
# eighths on Sus Marc LITE, the row of the head's half note (ART_SPANS; 0.09 s re-attack leads). _C13_V1_PAIRS holds the
# decision: "leg" (c09-c12: Leg Slur MAX targets), "runs" or "marc"; C13_V1_PAIRS in the environment overrides it
_C13_V1_PAIRS = _os.environ.get("C13_V1_PAIRS") or "marc"   # range test 2026-11-10: "marc" adopted, "runs" failed
_C13_SLUR_RUNS = _C13_V1_PAIRS == "runs"
if _C13_V1_PAIRS == "marc":
    _sr = (41.0, 53.0, 71.0, 77.0, 287.0, 761.0, 773.0, 791.0, 797.0)
    _pq = [q_ + h_ for q_ in _sr for h_ in (0.0, 0.5)]
    ART_SPANS["Violins I"] = [{"from": q_ - 0.01, "to": q_ + 0.01, "art": "Sus Marc LITE",
                               "vel_by_cc": [(34, 70), (46, 78), (58, 86), (72, 94)]} for q_ in _pq] + ART_SPANS["Violins I"]
    REATTACK_LEAD_AT["Violins I"] = {**REATTACK_LEAD_AT["Violins I"], **{q_: 0.09 for q_ in _pq}}
    SHORT_SUS_LEG_AT = {**SHORT_SUS_LEG_AT, "Violins I": [q_ for q_ in SHORT_SUS_LEG_AT["Violins I"] if q_ not in _pq]}
    VEL_SET["Violins I"] = {k_: v_ for k_, v_ in VEL_SET["Violins I"].items() if k_ not in _sr}
    # level steps (C13_V1_LEVELS=0 leaves them out, as in the range test): on the test render (rangetest/ml2) the
    # eighths' own-pitch peaks stood +4.6 / +9.5 (41), +12.7 / +14.4 (53), +10.5 / +8.9 (71), +6.6 / +9.7 dB (77) over
    # the half note's body; steps to about +1 dB. The reprise's four pairs take the same values (same notes); 287 a mean.
    # Second test: the second eighth 3 dB more, and its step held through its release to just before the staccato's
    # beat (the return at the staccato's note-on, 45 ms before the beat, lifted the ringing eighth over the staccato)
    if _os.environ.get("C13_V1_LEVELS") != "0":
        _lv = {41.0: (-4.0, -8.0), 53.0: (-11.0, -13.0), 71.0: (-9.0, -8.0), 77.0: (-6.0, -9.0), 287.0: (-8.0, -10.0),
               761.0: (-4.0, -8.0), 773.0: (-11.0, -13.0), 791.0: (-9.0, -8.0), 797.0: (-6.0, -9.0)}
        LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [
            [(q_ - 0.45, 0.0), (q_ - 0.41, a_), (q_ + 0.07, a_), (q_ + 0.1, b_ - 3.0), (q_ + 0.93, b_ - 3.0), (q_ + 1.02, 0.0)]
            for q_, (a_, b_) in _lv.items()]
    # after the first c13 render: the second eighth's release (note end 5 ms before the staccato's note-on, 120 ms
    # release cap) rang over the staccato quarter's start, lifted by the level step's return (the staccato's pitch
    # became the dominant one 50-150 ms after its beat; c12: 12-48 ms before). The second eighth ends 60 ms earlier
    # (C13_V1_E2END=0: as first rendered)
    if _os.environ.get("C13_V1_E2END") != "0":
        NOTE_END_AT = {**NOTE_END_AT, "Violins I": {**NOTE_END_AT.get("Violins I", {}), **{q_ + 0.5: q_ + 0.52 for q_ in _sr}}}
if _C13_SLUR_RUNS:
    _sr = (41.0, 53.0, 71.0, 77.0, 287.0, 761.0, 773.0, 791.0, 797.0)
    STACLEG_SPANS = {**STACLEG_SPANS, "Violins I": [(q_, q_ + 1.0, "Slur Runs") for q_ in _sr]}
    SHORT_SUS_LEG_AT = {**SHORT_SUS_LEG_AT, "Violins I": [q_ for q_ in SHORT_SUS_LEG_AT["Violins I"]
                                                           if not any(a_ <= q_ < a_ + 1.0 for a_ in _sr)]}
    VEL_SET["Violins I"] = {k_: v_ for k_, v_ in VEL_SET["Violins I"].items() if k_ not in _sr}
    ROW_REMAP["Violins I"] = {"Leg BC MAX": "Leg Slur MAX"}
    # both eighths 0.05 s early (Movement I c20: the row's notes sounded +0.05..+0.06 s); the second ones are rows in
    # leg_leads.json (the run-target lead), the first ones are heads after the Sus Marc LITE half note
    LEG_HEAD_AFTER_ROW_LEAD_S = {**LEG_HEAD_AFTER_ROW_LEAD_S, "at": {
        **LEG_HEAD_AFTER_ROW_LEAD_S["at"], "Violins I": {**LEG_HEAD_AFTER_ROW_LEAD_S["at"]["Violins I"], **{q_: 0.05 for q_ in _sr}}}}

# critic B #1 (after the c13 render): with Violins I's hemiola steps the mix itself is 0.3-1.0 dB lower in bars 103-104
# and 1.3-1.9 dB lower in bars 303-304 (K-weighted master), so the two delivery rows over them give back that much:
# -2 -> -1.5 (300-312) and -2 -> -0.5 (897-912). Delivery only: no REAPER data changes
_n = 0
for _r in RIDE_TRIMS:
    for _i, (_q, _v) in enumerate(_r):
        if _v == -2.0 and _r[0][0] in (299.6, 897.0):
            _r[_i] = (_q, -1.5 if _r[0][0] == 299.6 else -0.5); _n += 1
assert _n == 4, f"c13 RIDE_TRIMS: {_n} points changed"


# ---------- c14 (actor, on the c13 render; cycles/c14/CHANGES.md) ----------
# Critics A #1 / B #1: the nine soft theme-head figures of Violins I. c13 put the two slurred eighths on time; the levels
# were wrong: the Sus Marc LITE half note falls 11-16 dB before the slur goes on, the pair sat 5-10 dB under the half
# note's start and the landing staccato 4-14 dB over the pair. One level row per figure replaces c13's pair row, fitted
# on the c13 stem (cycles/c14/actor_scripts/themefit14.py; the envelope is post-fader, so the fit is exact for the
# same MIDI): the half note's second beat lifted by u (tail 7 dB under its first 300 ms), both eighths 3 dB under the
# half note's first 300 ms (a, b; the step now starts as the first eighth sounds, 0.12 qn before its beat, not at its
# note-on 0.41 qn before, where it cut the half note's tail), the landing staccato at about 4 dB under (d, from its
# note-on; no return to 0 dB under the ringing eighth). Rows, leads, velocities and note ends are c13's
# Dan, 2026-11-11 (he opened REAPER: large volume peaks and valleys on single notes look and sound unnatural): levels
# at the source first. The eighths played at velocity 78-94 next to a half note at 56-64 and were then cut 4-13 dB in
# the envelope: they take A's lower velocity table and c13's pair rows are removed. What velocity does not reach (the
# half note's own decay, a residue of 2 dB or more on a pair or on the landing staccato) is fitted on a whole-piece pass
# of this data under the lock (themefit14.py --pass -> build/c14_theme_rows.json: u = lift of the half note's second
# beat, a / b = the eighths, d = the landing staccato from its note-on; 0 = no point). C14_THEME=env keeps c13's
# velocities with rows fitted on the c13 stem (the first form of this fix, simulated only)
_old = [[(q_ - 0.45, 0.0), (q_ - 0.41, a_), (q_ + 0.07, a_), (q_ + 0.1, b_ - 3.0), (q_ + 0.93, b_ - 3.0), (q_ + 1.02, 0.0)]
        for q_, (a_, b_) in _lv.items()]
assert all(r_ in LEVEL_SHAPES["Violins I"] for r_ in _old), "c14: a c13 theme-head row was not found"
LEVEL_SHAPES["Violins I"] = [r_ for r_ in LEVEL_SHAPES["Violins I"] if r_ not in _old]
# Result of the velocity test (whole-piece pass V0b, 2026-11-11): at velocity 56-70 the Sus Marc LITE eighths played at
# -26..-31 dB, 5-11 dB OVER the half note's first 300 ms (-32..-39): on this LITE row velocity does not set the level
# (manual p.64: CC11 is loudness, CC1 dynamics). So c13's velocities stay and the level is one step per figure part,
# fitted on the c13 stem (themefit14.py --rows; exact for the same MIDI): one level for both eighths, the landing
# staccato, and a lift of the half note's second beat only where it is 2 dB or more. C14_THEME=vel builds the test data
if _os.environ.get("C14_THEME", "env") == "env":
    _c14_lv = {41.0: (2.0, -7.0, -7.0, -4.0), 53.0: (3.5, -10.0, -10.0, -8.0), 71.0: (0.0, -7.0, -7.0, 0.0),
               77.0: (2.0, -7.5, -7.5, -5.5), 287.0: (0.0, -11.5, -11.5, -8.0), 761.0: (2.5, -7.0, -7.0, -4.0),
               773.0: (3.5, -8.0, -8.0, -6.0), 791.0: (0.0, -8.0, -8.0, 0.0), 797.0: (2.0, -7.0, -7.0, -4.0)}
else:
    for _a in ART_SPANS["Violins I"]:
        if _a.get("art") == "Sus Marc LITE" and any(abs(_a["from"] - (q_ - 0.01)) < 1e-6 for q_ in _pq):
            _a["vel_by_cc"] = [(34, 50), (46, 56), (58, 62), (72, 70)]
    # (the second eighths still carried c08's fixed velocity 85 from their time as legato targets)
    VEL_SET["Violins I"] = {k_: v_ for k_, v_ in VEL_SET["Violins I"].items() if k_ not in [q_ + 0.5 for q_ in _sr]}
    _p = _os.path.join(globals().get("BUILD", "."), "c14_theme_rows.json")
    _c14_lv = {float(k_): tuple(v_) for k_, v_ in __import__("json").load(open(_p)).items()} if _os.path.exists(_p) else {}
# Movement I c56 (coordinator, 2026-11-11): a level step keyed to a moved note-on cuts the end of the note before it
# (join holes 9.0 dB with, 4.7 without). Every step of these rows is a 0.04 qn crossfade on the next note's score
# onset: the half note's lift ends on the first eighth's beat, a / b change on the eighths' beats, d on the landing's
for q_, (u_, a_, b_, d_) in _c14_lv.items():
    pts_ = [(q_ - 1.2, 0.0), (q_ - 0.55, u_), (q_ - 0.02, u_), (q_ + 0.02, a_), (q_ + 0.48, a_), (q_ + 0.52, b_), (q_ + 0.98, b_),
            (q_ + 1.02, d_), (q_ + 1.40, d_), (q_ + 1.46, 0.0)]
    if any((u_, a_, b_, d_)):
        LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[p_ for k_, p_ in enumerate(pts_) if k_ in (0, len(pts_) - 1)
                                                                   or p_[1] != pts_[k_ - 1][1] or p_[1] != pts_[k_ + 1][1]]]

# Critic A #3 (finale technique 49): legato-row string notes that follow a Sus MAX eighth or a staccato, or leap more
# than an octave (no transition sample beyond an octave, manual p.80-81), started 70-190 ms late (bar 49 beat 1: Violins
# I +116, Violins II +105, Violas +139 ms against the winds' +8..+39). They are fresh Sus MAX strokes 0.06 s early; the
# note before keeps its end (new generic REATTACK_KEEP_END). Their LEG_HEAD_AFTER_ROW_LEAD_S rows go. Soft notes of the
# class (v41 and under, the two sub. p entries) stay on the legato row
_c14_strokes = {"Violins I": [144.0, 157.5, 385.5, 853.5], "Violins II": [144.0, 123.0, 819.0, 853.5],
                "Violas": [144.0, 855.0],   # not 382 / 387: as strokes they took the lead of the repeated E4 after them
                "Violoncellos": [157.5, 853.0, 207.0, 891.0, 648.0, 840.0]}   # not 171 (p: a soft stroke speaks as late)
if _os.environ.get("C14_STROKES") != "0":
    DOWNBOW_STROKE_AT = {**DOWNBOW_STROKE_AT, **{t_: sorted(set(DOWNBOW_STROKE_AT.get(t_, []) + v_)) for t_, v_ in _c14_strokes.items()}}
    # (the five that follow a staccato after a gap are entries: they take the string entry lead, not a re-attack lead)
    _c14_ent = (123.0, 819.0, 207.0, 891.0)
    REATTACK_LEAD_AT = {**REATTACK_LEAD_AT, **{t_: {**REATTACK_LEAD_AT.get(t_, {}), **{q_: 0.06 for q_ in v_ if q_ not in _c14_ent}}
                                               for t_, v_ in _c14_strokes.items()}}
    REATTACK_KEEP_END = {t_: list(v_) for t_, v_ in _c14_strokes.items()}
    LEG_HEAD_AFTER_ROW_LEAD_S = {**LEG_HEAD_AFTER_ROW_LEAD_S, "at": {
        t_: {q_: s_ for q_, s_ in v_.items() if q_ not in _c14_strokes.get(t_, [])} for t_, v_ in LEG_HEAD_AFTER_ROW_LEAD_S["at"].items()}}

# Critic A #4 (Movement II c52, ONE_TIME_c14 items 2, 7): one legato row per string line. Joins whose row differs from
# the row of the note before moved by about 100 ms between renders of identical data (10 of 138 against 4 of 340
# same-row joins, c12 -> c13). Violins I, Violoncellos and the solo take the form Violins II and the Violas have had
# since c02 (Leg BC MAX notes on Leg Slur MAX with the bow-change notch; Leg BC MAX is unloaded), and the keyswitch of
# every remaining row change sits 0.15 s before its note. Every legato lead of the three tracks is refitted under the
# lock on whole-piece passes of the three stems (cycles/c14/actor_scripts/wholepass14.py, refit14.py ->
# build/leg_leads.json). C14_ONE_ROW=0 builds the data without it (the fallback if the refit cannot be verified)
if _os.environ.get("C14_ONE_ROW") != "0":
    for _t in ("Violins I", "Violoncellos", "Violin I solo"):
        ROW_REMAP[_t] = {**ROW_REMAP.get(_t, {}), "Leg BC MAX": "Leg Slur MAX"}
    # ("Violins II" first: by_name matches a key that is part of the track name, and "Violins I" is part of it)
    # c13's one-row test on the celli's trio tune read every join 120-260 ms early: the row's lead extra 0.05 -> -0.05
    # before the refit, so that the refit starts nearer
    LEG_ART_EXTRA_S = {**LEG_ART_EXTRA_S, "Violoncellos": {"Leg Slur MAX": -0.05}}
    KS_MIN_LEAD_S = {"Violins II": 0.0, **KS_MIN_LEAD_S, "Violins I": 0.15, "Violoncellos": 0.15, "Violin I solo": 0.15}

# Critic A #5: Flute 2 against Flute 1 in the second tutti (a2, slurred eighths): the lateness is fixed per pitch pair
# and repeats to the millisecond. The track's lead request is 100 ms (c11 / c13 raised it) but on running eighths the
# default cap (0.45 of the eighth) holds every join at 51 ms, which is why those raises did nothing. The joins of A's
# eight slowest pitch pairs (S +52..+111 ms) are listed in leg_leads.json (value 0; apply14.py) and take a cap of 0.75
# of the eighth (85 ms, +34 ms); the other joins keep 51 ms. Oboe 1's first slurred eighth of the loud heads read
# -43 ms (median) at the 0.055 s row lead: 0.02
LEG_CAP_FRAC = {**LEG_CAP_FRAC, "Flute 2": [(912.0, 960.0, 0.75, "listed")]}
LEG_HEAD_AFTER_ROW_LEAD_S = {**LEG_HEAD_AFTER_ROW_LEAD_S, "Oboe 1": 0.02}
# Critic A #6: the celli's second fugato eighths read -36 / -30 ms at the 0.16 s lead: 0.10
SHORT_SUS_LEAD_AT = {**SHORT_SUS_LEAD_AT, "Violoncellos": {173.5: 0.10, 869.5: 0.10}}

# Critic B #3: the harp's espressivo melody of bars 73-80 was under its own left hand (158 + 198 Hz bands 6.7 dB over
# the melody's): every left-hand note (A3 and lower) at velocity 46 (was 56, the cap's value); the melody keeps c12's
_C14_HARP_LH = [(216.0, 41), (217.0, 48), (217.0, 53), (217.0, 57), (219.0, 41), (220.0, 48), (220.0, 53), (220.0, 57),
                (222.0, 43), (223.0, 50), (223.0, 55), (223.0, 58), (225.0, 43), (226.0, 52), (226.0, 55), (226.0, 58),
                (228.0, 45), (229.0, 48), (229.0, 53), (229.0, 57), (231.0, 38), (232.0, 50), (232.0, 53), (232.0, 57),
                (234.0, 40), (235.0, 52), (235.0, 58), (237.0, 41), (238.0, 48), (238.0, 53), (238.0, 57)]
VEL_SET = {**VEL_SET, "Harp": {**VEL_SET.get("Harp", {}), **{k_: 46 for k_ in _C14_HARP_LH}}}
# Critic C #5: the timpani's pp roll of bars 237-240 grew 5 dB (the roll sample) while everything else faded
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(713.5, 0.0), (715.0, -2.5), (717.0, -6.0), (718.0, -6.0)]]
# Critic C #4: Oboe 1's line peaked a bar after its printed hairpin (A5 at 1038 6 dB over the B5 at 1036: the phrase
# arch raises CC11 straight after the printed diminuendo). A level step on the notes after the hairpin
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES.get("Oboe 1", []) + [[(1038.0, 0.0), (1038.5, -4.0), (1040.0, -4.0), (1041.0, 0.0)]]
# Critic C #5: Flute 1's staccato E6 on the two tutti downbeats (note_trims.json) as steps
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Flute 1": {**NOTE_TRIM_RAMP_S.get("Flute 1", {}), 312.0: 0.02, 912.0: 0.02}}
# Critic C #4: Clarinet 1's soft F5 / G5 at 243, 735, 904 (note_trims.json) with a short ramp
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Clarinet 1": {**NOTE_TRIM_RAMP_S.get("Clarinet 1", {}), 243.0: 0.05, 735.0: 0.05, 904.0: 0.05},
                    # C #4 Bassoon 1 699 / 702 and Oboe 1 1036; C #5 Flute 2's E6 on the tutti downbeats (as loud as Flute 1's)
                    "Bassoon 1": {**NOTE_TRIM_RAMP_S.get("Bassoon 1", {}), 699.0: 0.05, 702.0: 0.05},
                    "Oboe 1": {**NOTE_TRIM_RAMP_S.get("Oboe 1", {}), 1036.0: 0.05},
                    "Flute 2": {**NOTE_TRIM_RAMP_S.get("Flute 2", {}), 312.0: 0.02, 912.0: 0.02}}
# ONE_TIME_c14 item 8b / Movement II c53: the join notches (celli and Clarinet 1) were written in absolute qn; they
# are now timed in seconds from the moved note-on (new generic JOIN_NOTCH_S, ported from Movement II), with the
# offsets they had on the c13 note-ons, so they follow the refit
JOIN_NOTCH_S = {'Violoncellos': {764.0: (0.004, 0.118, -4.0), 800.0: (0.004, 0.129, -4.5), 506.0: (0.076, 0.208, -7.0), 570.0: (0.062, 0.194, -5.0)}, 'Clarinet 1': {459.0: (0.037, 0.103, -4.0)}}
JOIN_NOTCH = {}
# Critic B #2: the basses' ff arco E1 / B1 of the two tuttis (+2 dB in note_trims.json) with a short ramp
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Double basses": {**NOTE_TRIM_RAMP_S.get("Double basses", {}), **{float(q_): 0.05 for q_ in (
    312, 315, 318, 321, 324, 330, 333, 345, 348, 354, 357, 912, 915, 918, 921, 924, 930, 933, 945, 948, 954, 957)}}}
# Critic A #4 / ONE_TIME_c14 item 8a: former Leg BC MAX notes that start softer on the one row than they did in c13 get
# a level-only step over the note (build/c14_row_levels.json, written by cycles/c14/actor_scripts/rowlevel14.py from a
# whole-piece pass of the refitted data; absent = none)
_p = _os.path.join(globals().get("BUILD", "."), "c14_row_levels.json")
if _os.path.exists(_p):
    for _t, _rows in __import__("json").load(open(_p)).items():
        LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[tuple(p_) for p_ in r_] for r_ in _rows]
# Critic C #1 (after the c14 render): the fugato's p entries still lay under the ppp opening in the delivered file
# (bars 57-60 -34.8..-36.9 against -32.0 / -31.1 for bars 1-2, plain dB of the mp3): C's two delivery rows, +2 dB.
# Delivery only: no REAPER data changes
RIDE_TRIMS = RIDE_TRIMS + [[(167.5, 0.0), (168.5, 2.0), (196.0, 2.0), (204.0, 0.0)], [(863.5, 0.0), (864.5, 2.0), (882.0, 2.0), (888.0, 0.0)]]


# ---------- c15 (actor, on the c14 render; cycles/c15/CHANGES.md) ----------
# Dan, 2026-11-11, after opening REAPER: "how much the volume adjustment was adjusted in large peaks and valleys on so
# many individual notes, even with fast successive notes volume peaks up and down every note. To me it seemed
# unnatural". Critics A #1-#5, B #1-#3, C #3 measured the causes on the c14 stems:
# (1) row trims and pitch trims returned to 0 dB between the notes of every staccato run (Oboe 1 bar 105: 0.1 / 5.1 dB
#     per eighth): ONE_LEVEL gives every note of an eighth or less one value of the per-note layers, held from join to
#     join, and ROW_TRIM_HOLD_QN keeps a row trim through the gaps of a run;
# (2) level steps at a legato join stood on the moved note-on and cut the old note's last 60 ms (Clarinet 1: join holes
#     6-10 dB with the layers, 2-5 without): TRIM_STEP_S puts pitch and row trims as flat levels whose steps stand
#     10 ms after the next note's score onset when the old note still sounds;
# (3) the slow layers were drawn as stairs: VOL_GRID_QN 0.125 (build_reaper.py's own grid) and mix.json env_simplify_db;
# (4) the metric weight (342 steps starting 45 ms before the beat) helped no line consistently: off.
VOL_GRID_QN = 0.125
ONE_LEVEL = {"tags": ["level:pitch_trim", "level:row_trim", "level:note_trim", "level:metric_db", "level:uni_boost",
                      "level:meas_trem", "level:pickup", "level:chord", "level:contour", "shape:accent",
                      "shape:accent_body", "shape:marc_body", "shape:beat_db", "shape:tenuto", "shape:synco"],
             "max_qn": 0.55, "ramp_s": 0.03, "leg_center_s": 0.005, "gap_qn": 1.0, "tail_s": 0.25}
# (center_by: simulated on the c14 stem, Clarinet 1's join holes at 138 / 399 / 468 / 840: c14 8.4 / 10.2 / 7.7 / 8.6 dB,
# centre +10 ms 6.7 / 8.3 / 5.0 / 5.4, +30 ms 3.9 / 5.4 / 3.1 / 3.4, +50 ms 2.4 / 4.3 / 2.2 / 2.6, no envelope 2.4 / 4.7 / 0.3 / 2.2;
# Horn 3's recall 1020-1044 steps 0.8 dB in c14, 1.3 at +10 ms, 1.9 at +30, 2.2 at +50: the horn keeps +10 ms)
TRIM_STEP_S = {"ramp_s": 0.04, "center_s": 0.01, "pre_s": (0.03, 0.01), "center_by": {"Clarinet 1": 0.05, "Clarinet 2": 0.05}}
ROW_TRIM_HOLD_QN = 1.0
SHORT_CC11_PARK = {**SHORT_CC11_PARK, "beat_db": None}
# The park's CC11 steps (and the envelope's mirror of Opus's 120 ms CC11 fade, 5-12 dB) stood 4 ms before a run's first
# stroke and 2 ms before the first note after the run, so the first stroke of every run and the first 120 ms of every
# note after one carried a ramp. They now stand in the gaps: up to 0.15 s before the run (not before the end of the note
# before it) and 0.02 s after the run's last note-off (C15_PARK=0: as before)
# Result on the data (no render): the share of notes with over 3 dB inside stayed 17 % and the short notes moving over
# 1 dB went 323 -> 327, because the strokes' note-offs leave gaps of a few ms only. Not used (C15_PARK=1 builds it)
if _os.environ.get("C15_PARK") == "1":
    SHORT_CC11_PARK = {**SHORT_CC11_PARK, "pre_s": 0.15, "post_s": 0.02}
# Critic A #6: accent swells stacked over 4.5 dB on 7 wind notes (db 3.5); Movement I's cap
GENTLE_ACCENT = {**GENTLE_ACCENT, "wind": {**GENTLE_ACCENT["wind"], "db": 3.0}}
ACCENT_SWELL_MAX_DB = 3.0
# Critic B #3 / A #5: the timpani's loud single strokes take their weight from the velocity (B: 22 velocity steps =
# +2.5..+3.1 dB over 20-170 ms, the spike's own 2.9 dB), not from a +6 dB envelope spike
if _os.environ.get("C15_TIMP") != "0":
    TIMP_LOUD_VEL_ADD = (22, 125, 3.0)

# Critics A #2 / C #3: the theme head of Violins I (nine soft figures). c14's figure row held the half note's lift u
# until the first eighth's beat while c13's half-note body row had already returned to 0: for 20-30 ms the envelope
# stood 7-12 dB over both (a spike on the eighth's beat in 7 of 9 figures). One row per figure now: the half note's
# body level runs to the first eighth's note-on (q - 0.40) and crossfades to the eighths' level by q - 0.20 (C's form,
# simulated on the c14 stem: a steady rise into the eighth's body at all nine); u is dropped. The eighths' level and
# the landing staccato's are c14's.
_n = 0
for q_, (u_, a_, b_, d_) in _c14_lv.items():
    _pts = [(q_ - 1.2, 0.0), (q_ - 0.55, u_), (q_ - 0.02, u_), (q_ + 0.02, a_), (q_ + 0.48, a_), (q_ + 0.52, b_), (q_ + 0.98, b_),
            (q_ + 1.02, d_), (q_ + 1.40, d_), (q_ + 1.46, 0.0)]
    _fig = [p_ for k_, p_ in enumerate(_pts) if k_ in (0, len(_pts) - 1) or p_[1] != _pts[k_ - 1][1] or p_[1] != _pts[k_ + 1][1]]
    assert _fig in LEVEL_SHAPES["Violins I"], f"c15: the c14 theme row at {q_} was not found"
    _body = [r_ for r_ in LEVEL_SHAPES["Violins I"] if len(r_) == 4 and abs(r_[-1][0] - (q_ - 0.02)) < 1e-6 and r_[-1][1] == 0.0
             and r_[1][1] == r_[2][1]]
    assert len(_body) <= 2, f"c15: {len(_body)} body rows at {q_}"   # (53 and 773 carry two: -12 / -10.8 and -3)
    LEVEL_SHAPES["Violins I"] = [r_ for r_ in LEVEL_SHAPES["Violins I"] if r_ != _fig and r_ not in _body]
    _L = round(sum(r_[1][1] for r_ in _body), 2)
    _head = [tuple(_body[0][0]), (_body[0][1][0], _L), (q_ - 0.40, _L)] if _body else [(q_ - 0.40, 0.0)]
    # (the landing staccato loses the metric weight's +1.5 dB and sits 2-2.7 dB under the pair instead of 0.9-1.4; giving
    # it back raised the theme's step median from 1.7 to 2.3 dB on the simulation, so it is not given back)
    _row = _head + [(q_ - 0.20, a_)] + ([(q_ + 0.48, a_), (q_ + 0.52, b_)] if a_ != b_ else []) \
        + ([(q_ + 0.98, b_), (q_ + 1.02, d_)] if b_ != d_ else []) + [(q_ + 1.40, d_), (q_ + 1.46, 0.0)]
    LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [_row]
    _n += len(_body)
print(f"  c15 theme-head rows: 9 figures, {_n} with a half-note body row", file=__import__("sys").stderr)

# Critic A #3: level steps that cut the note before them.
# (a) c14's row-level steps (build/c14_row_levels.json) on consecutive notes returned to 0 dB between the old note's
#     moved end and the next score onset (a 6 dB notch 60 ms wide in the transition: holes 4.2-5.6 dB with, -1.8..0.8
#     without). Rows of one track that follow each other within 1 qn are one line: the level goes from one value to
#     the next on the next note's score onset without passing 0.
for _t, _rows in __import__("json").load(open(_p)).items():
    _rows = sorted([[tuple(p_) for p_ in r_] for r_ in _rows], key=lambda r_: r_[0][0])
    assert all(r_ in LEVEL_SHAPES[_t] for r_ in _rows) and all(len(r_) == 4 for r_ in _rows), "c15: a c14 row-level step was not found"
    LEVEL_SHAPES[_t] = [r_ for r_ in LEVEL_SHAPES[_t] if r_ not in _rows]
    _lines = []
    for r_ in _rows:
        if _lines and r_[0][0] - _lines[-1][-2][0] < 1.0:
            _lines[-1] = _lines[-1][:-2] + [(r_[0][0], _lines[-1][-2][1])] + r_[1:]
        else:
            _lines.append(list(r_))
    LEVEL_SHAPES[_t] = LEVEL_SHAPES[_t] + _lines
    print(f"  c15 row-level steps {_t}: {len(_rows)} rows in {len(_lines)} lines", file=__import__("sys").stderr)
# (b) Violins I 155.5 (c13's -8 dB row on the staccato pickup) started 0.3 qn before the pickup and cut the last 60 ms
#     of the note before it (hole 9.0 dB with, 1.0 without): it starts on the pickup's score onset
_old = [(155.2, 0.0), (155.25, -8.0), (155.93, -8.0), (155.99, 0.0)]
assert _old in LEVEL_SHAPES["Violins I"], "c15: the 155.5 row was not found"
LEVEL_SHAPES["Violins I"] = [r_ for r_ in LEVEL_SHAPES["Violins I"] if r_ != _old] + [[(155.46, 0.0), (155.5, -8.0), (155.93, -8.0), (155.99, 0.0)]]
# Oboe 1's staccato row trim was a hat that left each note's ring at 0 dB; held through the run at -5 the staccatos sat
# 1.0-1.7 dB lower against the slurred notes around them (simulated on the c14 stem: step median 1.7 -> 2.3). At -3.5
# the eighths keep their c14 level (-0.2 dB) and the staccato quarters rise 1.9 dB; -4.2 splits the difference
ROW_TRIM_DB["Oboe 1"] = {"Stac DblTng RRx9": (-4.2, 72)}

# ----- c15 timing (critic C) and balance (critic B); table rows: cycles/c15/actor_scripts/apply15.py -----
# C #2: the trio tune in the celli and Horn 3 (bars 169-184) limped: the long notes after a pickup eighth (qn 512, 524)
# and 510 arrived 110-170 ms late. Celli: 510's refit offset -0.115 s removed (leg_leads.json); the minimum gap between
# note-ons 0.1 -> 0.06 s inside 504-576 (it held the leads of 512 / 524 at 147 / 102 ms); the notes after a pickup
# eighth at velocity 112 (manual p.144: velocity sets the transition's speed; bars 209-224 at v112-118 land +38..+57)
LEG_MIN_GAP_AT = {"Violoncellos": [(504.0, 576.0, 0.06)]}
VEL_SET["Violoncellos"] = {**VEL_SET.get("Violoncellos", {}), 512.0: 112, 524.0: 112, 536.0: 112, 567.0: 112, 572.0: 112}
# Horn 3 with them: legato targets +0.05 s (leg_leads.json), the four re-tongued heads 0.05 -> 0.12 s
RETONGUE_LEAD_AT = {**RETONGUE_LEAD_AT, "Horn 3": {**RETONGUE_LEAD_AT.get("Horn 3", {}), 510.0: 0.12, 516.0: 0.12, 519.0: 0.12, 522.0: 0.12}}
# C #4: Sus MAX strokes with 60 ms of lead spoke late (class +25 ms; Violins I 144 +76..+112, Violas 855 +68..+92):
# the late ones take the longer class (75-115 ms leads read +3..+5 ms)
REATTACK_LEAD_AT = {**REATTACK_LEAD_AT,
                    "Violins I": {**REATTACK_LEAD_AT.get("Violins I", {}), 144.0: 0.13, 385.5: 0.085, 853.5: 0.085},
                    "Violins II": {**REATTACK_LEAD_AT.get("Violins II", {}), 144.0: 0.085},
                    "Violas": {**REATTACK_LEAD_AT.get("Violas", {}), 855.0: 0.11}}
# B #5: the basses' note trims at 138 / 140 / 642 and the ff G1 are steps
NOTE_TRIM_RAMP_S = {**NOTE_TRIM_RAMP_S, "Double basses": {**NOTE_TRIM_RAMP_S.get("Double basses", {}),
                                                           **{q_: 0.05 for q_ in (138.0, 140.0, 642.0, 162.0, 351.0, 939.0, 951.0)}}}
# B #6: the summit (bars 336-339) stood 4.4 dB over every other loud passage in the delivered file and set both the
# span (19.8 dB) and the limiter (3.0 dB): -1 dB in the delivery only
RIDE_TRIMS = RIDE_TRIMS + [[(1004.0, 0.0), (1005.0, -1.0), (1016.5, -1.0), (1017.0, 0.0)]]


# ---------- c15, second part: Dan's decision of 2026-11-11 16:30Z ----------
# "i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to
# fix our problem." Rule: the track volume envelope keeps slow balance only (roles, hairpin gains as ramps, roll shapes,
# fades); no per-note volume move, no exceptions. What the per-note layers did moves to the instrument side or is left
# audible and listed in cycles/c15/CHANGES.md.
VOL_CLASSES = ("slow",)
LEVEL_ROW_SLOW_QN = 3.0      # LEVEL_SHAPES rows that hold one level for a bar or more stay, as passage levels
UNI_BOOST_AS_ROLE = True     # the unison boost (74 notes on 7 tracks, a phrase level already: critic B) as role spans
# The string short rows go back to their printed CC11 (SHORT_CC11_PARK parked CC11 at 120 and returned the level, 2-8 dB
# per section, in the volume envelope; the level is the same by the patches' own CC11 table, now made in Opus)
_park15 = SHORT_CC11_PARK
SHORT_CC11_PARK = None
if _os.environ.get("C15_SIM_PARK") == "1":   # analysis only: the park and its return lane as the simulation target
    SHORT_CC11_PARK = _park15
# Per-pitch sample-level corrections (build/pitch_trims.json, 14 tracks) are per-region volumes in the Opus state
# (mix.json region_gain_db, written by cycles/c15/actor_scripts/adopt15.py from the table); none in the envelope
PITCH_TRIM_IN_OPUS = ["Horn 4", "Horn 1", "Horn 2", "Horn 3", "Double basses", "Violoncellos", "Clarinet 1", "Clarinet 2",
                      "Flute 2", "Oboe 2", "Cor anglais", "Oboe 1", "Trumpet 1", "Flute 1"]
# The timpani's clipped strokes get no flat level either (TIMP_LOUD_VEL_ADD third value 0)
if TIMP_LOUD_VEL_ADD:
    TIMP_LOUD_VEL_ADD = (TIMP_LOUD_VEL_ADD[0], TIMP_LOUD_VEL_ADD[1], 0.0)
# Violins I's "Sus Marc LITE" row (the theme head's half notes and slurred eighths, the hemiola strokes) is 8 dB lower
# in the Opus state (mix.json region_gain_db row_db): the hemiola level rows of bars 101-104 / 301-304 give the 8 dB back
_h1, _h2 = [(299.3, 0.0), (299.4, -8.0), (311.9, -8.0), (312.0, 0.0)], [(900.95, 0.0), (901.05, -6.5), (911.9, -6.5), (912.0, 0.0)]
assert _h1 in LEVEL_SHAPES["Violins I"] and _h2 in LEVEL_SHAPES["Violins I"], "c15: a hemiola level row was not found"
LEVEL_SHAPES["Violins I"] = [r_ for r_ in LEVEL_SHAPES["Violins I"] if r_ not in (_h1, _h2)] + [[(900.95, 0.0), (901.05, 1.5), (911.9, 1.5), (912.0, 0.0)]]


# =====================================================================================================================
# c16 (2026-11-11): instrument-side fixes after the removal of every per-note volume move (cycles/c16/CHANGES.md)
# =====================================================================================================================
# 1. Re-bows of exposed held notes (critics A #1, C #1; Dan's note 8). Without their fills the re-bows of Violins I's
# ppp G sharp and of the harmonic E6 dipped 9-13 dB and stayed 3-6 dB low for over a second.
# - the two short notes (5.3 s and 5.6 s: one pass over the 3.95 s loop point) keep one bow
AUTO_REBOW_SKIP = {**AUTO_REBOW_SKIP, "Violins I": [0.0], "Violins II": [420.0]}
# - the last note (14.9 s): Violins I re-bows twice (the c15 points; the third, on the fermata bar's downbeat, is
#   dropped), all pieces on "Sus MAX" (the first piece on "Leg Slur MAX" stood 3.5 dB over the others), and the idle
#   "Violin I solo" instance (DIV A, another sample set) plays the same note with its own bow changes halfway between
#   ("change bow freely"); the track that holds lifts its CC11 while the other starts a new bow
REBOW_AT = {**REBOW_AT, "Violins I": sorted(set(REBOW_AT.get("Violins I", [])) | {1103.814, 1116.299})}
ART_AT = {**ART_AT, "Violins I": {**ART_AT.get("Violins I", {}), 1089.0: "Sus MAX"}}
HELD_DOUBLE = {"Violins I": [{"span": (1089.0, 1128.0), "to": "Violin I solo", "rebow_at": [1096.14, 1110.66, 1121.0],
                              "cc11_add": 0, "cc1": 38, "lift": (7, 0.15, 0.45, 1.0)}]}

# 3. Accents (critics A #2, C #4; finale c17 #1). CC11 on the sustain rows gains 0.3-0.5 dB per unit up to about 106 and
# nothing above, and 152 of 321 accents stood at CC11 110 or more. The printed ff rests at 100 on the strings and 98 on
# the woodwinds (fff 104); mix.json dyn_trim_db "ff" makes up the level. Each accent raises CC11 for 0.15 s: +12 below
# the loud range, up to 118 (strings) / 121 (woodwinds) in it. Brass and timpani: unchanged (no brass accents here).
# (first values: strings 100 / top 118, winds 98 / top 121. Finale c17, measured on its render (technique 70): rest at
# 104-105, woodwinds 104 and not 98 because CC11 88-98 is a plateau on the woodwind sustains; bump to about 124,
# held 0.15 s, back by 0.45 s; fronts no brighter. Taken over before our build.)
CC11_REST_MAP = {"string": [(0, 0), (96, 96), (114, 104), (127, 108)], "wind": [(0, 0), (96, 96), (114, 104), (127, 108)]}
ACCENT_CC = {"string": {"add": 12, "add_loud": 20, "loud_cc": 98, "top": 124, "hold_s": 0.15, "rel_s": 0.3, "skip": [899.0]},
             "wind": {"add": 12, "add_loud": 10, "loud_cc": 98, "top": 116, "hold_s": 0.08, "rel_s": 0.22, "skip": [899.0]}}
# (pass PA under the lock, 2026-11-15, with wind add_loud 20 / top 124 / 0.15 + 0.3 s: woodwind ff accents +4.0 dB over
# their neighbours (median; Flute 1 +3.2, cor anglais +3.1, Bassoon 1 +4.2), strings ff +0.8, mf-f +1.5, p-mp +2.3.
# Dan on the finale's accents (2026-11-11): "a little bit over done"; target here +1.0 to +2.0 median, none over +3:
# the woodwinds' loud bump is halved and shortened (finale c18's shape); the strings keep theirs)
# (899: the accented ff upbeat before the tutti sfp stays at the resting level, so the sf at 900 stands over it: B #4)
# accented slur heads of the woodwinds under f play the tongued sustain (they played the legato row's slow first-note
# layer: Oboe 1's appoggiatura 2.6-11.4 dB under its figure)
ACCENT_SUS_MIN_CC = {"wind": 44}

# 4. The sf of the tutti sfp (bar 301; critics B #4, C #3): Violins I's sf note played "Sus Marc LITE" (the theme head's
# row, -8 dB in the Opus state since c15): it plays "Sus MAX". With CC11_REST_MAP the ff upbeat rests at 100 and the
# sfp's attack keeps its printed level + 8 (CC11_REST_SFP_ADD): 122-127.
ART_AT["Violins I"] = {**ART_AT.get("Violins I", {}), 900.0: "Sus MAX"}
# the summit's margin in the delivery (C #3: 1.0 dB over bar 300; c14 2.4): c15's -1 dB ride row over 1004-1017 goes,
# and the 897-912 row starts a bar earlier so that bar 300 is held back like bars 301-304
_n0 = len(RIDE_TRIMS)
RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if not (abs(r_[0][0] - 1004.0) < 1e-6 and abs(r_[1][1] + 1.0) < 1e-6)]
assert len(RIDE_TRIMS) == _n0 - 1, "c16: the c15 summit ride row was not found"
_k = [k_ for k_, r_ in enumerate(RIDE_TRIMS) if abs(r_[0][0] - 897.0) < 1e-6 and r_[0][1] == 0.0]
assert len(_k) == 1, f"c16: {len(_k)} ride rows start at 897"
RIDE_TRIMS[_k[0]] = [(894.0, 0.0), (897.0, RIDE_TRIMS[_k[0]][1][1])] + list(RIDE_TRIMS[_k[0]][1:])

# 5. Timpani (critic B #1). The loud strokes' velocity +22 put them in the top sample layers (Lng row layers 93-98,
# 99-110, 111-120, 121-124 ...: 2-5 kHz share of the first 80 ms +5.6 dB) for -0.7 dB of level: +8, capped at 104,
# and the 2.5 dB go into passage roles (roles.json). The roll under the summit (bar 336) holds CC1 118 and does not
# settle; the mf < f roll of bar 332 crosses the Rls row's layers (CC1 62 -> 104; it was flat on 73 -> 88).
TIMP_LOUD_VEL_ADD = (8, 104, 0.0)
TIMP_SETTLE_SKIP = [1005.0]
TIMP_CC1_AT = {1005.0: (118, 118), 993.0: (62, 104)}
# the two single strokes that carried a -5 / -4 dB fader row (roles.json rows of 0.7 qn, removed): 20 / 16 velocity steps
VEL_SET["Timpani"] = {**VEL_SET.get("Timpani", {}), 597.0: 96, 624.0: 103}

# 6. Legato after a row change (critic C #2; B #6). The keyswitch of Violins II and the violas stood 7 ms before its
# note: a legato-row note then started in one of two ways from render to render (Violas 579 / 585 near silent in c12
# and c15, present in c08 and c14; Violins II 855 crossing at -2 or +88 ms on identical data). Every keyswitch 0.15 s
# ahead (Violins I, the celli and the solo since c14), and the row-change joins take the first-note time as their lead
KS_MIN_LEAD_S = {**KS_MIN_LEAD_S, "Violins II": 0.15, "Violas": 0.15}
ROW_CHANGE_LEAD_S = {"Violins I": 0.235, "Violins II": 0.245, "Violas": 0.20, "Violoncellos": 0.21, "Violas div": 0.20}
# per-onset leads refitted on whole-piece passes under the lock (cycles/c16/actor_scripts/refit16.py -> build/lead_set.json)
if _os.path.exists(f"{BUILD}/lead_set.json"):
    LEAD_SET_AT = {k_: v_ for k_, v_ in __import__("json").load(open(f"{BUILD}/lead_set.json")).items() if not k_.startswith("_")}
# same-pitch slur heads on the legato row (the slow first-note layer; the two near-silent viola notes): the sustain row
ART_AT["Violas"] = {**ART_AT.get("Violas", {}), 579.0: "Sus MAX", 585.0: "Sus MAX"}
# downbeats after a pickup eighth (the lead cannot be longer than the eighth): fresh Sus MAX strokes 0.08 s early, the
# c14 form (DOWNBOW_STROKE_AT, REATTACK_KEEP_END); the legato row returns on the next note
_c16_strokes = {"Violins I": [372.0], "Violins II": [372.0, 385.5], "Violoncellos": [524.0]}
DOWNBOW_STROKE_AT = {**DOWNBOW_STROKE_AT, **{t_: sorted(set(DOWNBOW_STROKE_AT.get(t_, []) + v_)) for t_, v_ in _c16_strokes.items()}}
REATTACK_LEAD_AT = {**REATTACK_LEAD_AT, **{t_: {**REATTACK_LEAD_AT.get(t_, {}), **{q_: 0.08 for q_ in v_}} for t_, v_ in _c16_strokes.items()}}
REATTACK_KEEP_END = {**REATTACK_KEEP_END, **{t_: sorted(set(REATTACK_KEEP_END.get(t_, []) + v_)) for t_, v_ in _c16_strokes.items()}}

# 8. Balances a per-note level used to carry (critics B #3, #5; C #5-6), on the instrument side.
# Oboe 1 at the reprise's sub. p (bars 277-279, the octave with Flute 1): CC11 37 -> 48 at the mark, 42 -> 56 at 832
CC11_ADD_SPANS = {"Oboe 1": [(827.95, 832.0, 11, 14), (832.0, 838.0, 14, 10), (838.0, 840.0, 10, 0)],
                  # the celli's trio tune head (qn 504) swelled 18 dB through its first note: CC11 flat at 59 from the start
                  "Violoncellos": [(503.0, 506.0, 10, 0)]}
# the basses' div. pizzicato octaves of bars 253-268 (two notes on the full section): velocity 53 -> 42 (3 dB)
VEL_SET["Double basses"] = {**VEL_SET.get("Double basses", {}), **{float(q_): 42 for q_ in
                            (756, 759, 762, 765, 768, 771, 774, 777, 780, 783, 786, 789, 792, 795, 797, 798, 801)}}

# 9. Repeats (critic A #5; finale c17 #3): tongued same-pitch repeats ran together where the played gap was under
# 60 ms (the trumpets' three chords at 1008-1012: 6 ms, 0.0 dB of separation; Horn 1's tenuto repeats: 35 ms, 2.2 dB)
REP_GAP_FLOOR_S = {"brass": 0.09, "wind": 0.065}
WIND_REP_RETONGUE_BY = {**WIND_REP_RETONGUE_BY, "Horn 1": {"gap_s": 0.065, "frac": 0.2, "fall_cc": 8, "fall_s": 0.08}}

# 10. Phrase heads and join bumps (critic A #6): soft cello joins at velocity 70-90 bumped on 0 of 13, at 91-110 on 14
# of 55: the three bumping targets at 80; CC11 lifts on the late heads (ACCENT_CC_AT, the c11 mechanism)
VEL_SET["Violoncellos"] = {**VEL_SET.get("Violoncellos", {}), 570.0: 80, 764.0: 80, 800.0: 80}
ACCENT_CC_AT = {**ACCENT_CC_AT,
                "Violoncellos": {**ACCENT_CC_AT.get("Violoncellos", {}), 794.0: (10, 1.0), 542.0: (10, 1.0)},
                "Bassoon 1": {**ACCENT_CC_AT.get("Bassoon 1", {}), 353.0: (8, 0.75), 953.0: (8, 0.75)},
                "Clarinet 1": {**ACCENT_CC_AT.get("Clarinet 1", {}), 576.0: (8, 0.75)}}


# =====================================================================================================================
# c17 (2026-11-15): cycles/c17/CHANGES.md. Instrument side only; the volume envelope keeps slow balance.
# =====================================================================================================================
# 1. The closing solos (critic B #1). Horn 1's last G sharp: the guard removed the 2.5 dB rise after the note's start;
# CC11 is plain level on the horns (their dynamic layers are on CC1): +11 units from the note-on (the solo violin's
# role start is in roles.json)
# (resumed 22:20: +11 was B's value from a family slope of 0.22 dB per unit; Movement I c59 measured 0.55-0.61 dB per
# unit on the horns at CC11 46-58 and +6.5 dB from +8 units on Horn 1. Target +2.5 dB: +4 units, checked on the render)
CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Horn 1": CC11_ADD_SPANS.get("Horn 1", []) + [(1100.7, 1128.0, 14, 14),   # (16: 0-2 dB over c16, c15 is 2-3 over)
                                                                           (-0.5, 5.9, 8, 8)]}
# (first c17 render: with gain -4.0 Horn 1 read 1.3-2.8 dB under c16 in every section but the call; gain -2.3 and the
# two offsets 8 units lower: 22 / 13 -> 14 / 8... the last note read c16 +1 dB with 22)
# (range test H1b: +5 units gave +1.1 dB on the soft G sharp, 0.22 dB per unit at CC11 about 35, not the 0.55 of mf)
# (range test H1a, 22:40: with the Close mic leading (mix.json: Close -1.4 / Main -5.2 dB, gain -4.0) the horn call keeps
# its c16 level but the soft G sharp reads 2.8 dB lower: +5 units on bars 1-2 and +4 more on the last note)

# 3. The last violin G sharp (critics A #3, C #2): three bow changes 3.0 s apart instead of five 1.9 s apart (each
# instance needs 1.0-2.2 s to come back after its own change): the copy at 266.0 s and 272.0 s, Violins I at 269.0 s;
# the holder's CC11 lift starts 0.3 s before the other's change and is complete on it; the copy plays "Sus MAX" (its
# re-attacks on "Leg Slur MAX" were 7 dB weaker in the fundamental and 4 dB brighter)
REBOW_AT = {**REBOW_AT, "Violins I": sorted((set(REBOW_AT.get("Violins I", [])) - {1103.814, 1116.299}) | {1110.963})}
HELD_DOUBLE = {"Violins I": [{"span": (1089.0, 1128.0), "to": "Violin I solo", "rebow_at": [1099.912, 1119.618],
                              "cc11_add": 0, "cc1": 38, "lift": (10, 0.0, 0.30, 0.55, 0.3), "art": "Sus MAX"}]}
# (range test LN, 23:10: dips of the sum at the three changes 6.9 / 3.6 / 1.5 dB with a lift of 7: 10)
# (lift: complete on the change, held 0.30 s, back over 0.55 s: Movement II c57 #2)

# 4. Accents (critic A #2; Dan 2026-11-11: "the accents are little bit over done now"; target for isolated accents:
# median +1.0..+2.0 dB over the neighbours, 90th percentile under +3.5, no track over +3). Shape: held 0.06 s from
# the later of the moved note-on and score onset - 0.03 s, back over 0.20 s (the c16 shape lasted lead + 0.15 + 0.3 s:
# a louder note, not a weighted start). Per track the bump A derived from the c15 (no bump) and c16 readings; rows
# with their own accent get none. The bar 72 / 300 chords
# (critic B #2): +8, so the sf of bar 301 at CC11 127 stands over them
# (resumed: hold 0.08 s counted from the score onset when the note is led (pre_s 0), so a led note has its full bump on
# the beat and for 80 ms after it: Movement II c57 #3, finale c19 #3)
_acc17 = {"hold_s": 0.08, "rel_s": 0.20, "from_moved": True, "pre_s": 0.0, "skip_rows": ("Sus Marc LITE",),
          "skip": [899.0], "loud_cc": 98}
# (the 9+ / 16+ stave scaling was prepared and dropped before the build: Movement I c59 measured that when every track
# rises E dB the sum rises E dB; the option "scale_staves" stays in the tool, unused)
_ACC_BY = {"Flute 1": (2, 0, 116), "Flute 2": (12, 10, 116), "Oboe 1": (12, 4, 116), "Cor anglais": (0, 0, 116),
           "Clarinet 1": (0, 0, 116), "Clarinet 2": (12, 0, 116), "Bassoon 1": (0, 0, 116),
           "Violins I": (3, 12, 124), "Violins II": (2, 6, 124), "Violas": (5, 20, 124)}
# (first c17 render, isolated accents, median: Violins I +2.6 with 6 / 20, Violins II +3.6 with 8 / 14 (their short rows
# stand 1.5-3 dB lower now, so the accent reads larger), Bassoon 1 +3.9 with 12 / 0: lowered to 3 / 12, 2 / 6, 0 / 0;
# bars 72 / 300 fell 5.4-5.7 dB in the master with +8: +12 on the strings)
ACCENT_CC = {"string": {**_acc17, "add": 12, "add_loud": 20, "top": 124, "add_at": {213.0: 12, 897.0: 12}},
             "wind": {**_acc17, "add": 12, "add_loud": 10, "top": 116, "add_at": {213.0: 8, 897.0: 8}},
             **{t_: {**_acc17, "add": a_, "add_loud": l_, "top": top_,
                     "add_at": {213.0: (12 if top_ == 124 else min(8, l_)), 897.0: (12 if top_ == 124 else min(8, l_))}}
                for t_, (a_, l_, top_) in _ACC_BY.items()}}
# A #6: the CC11 lifts of c16 on Bassoon 1 353 / 953 and Clarinet 1 576 did nothing (0 dB per unit at ff): removed
ACCENT_CC_AT = {**ACCENT_CC_AT, "Bassoon 1": {k_: v_ for k_, v_ in ACCENT_CC_AT.get("Bassoon 1", {}).items() if k_ not in (353.0, 953.0)},
                "Clarinet 1": {k_: v_ for k_, v_ in ACCENT_CC_AT.get("Clarinet 1", {}).items() if k_ != 576.0}}

# 5. The sf of bar 301 and crescendo gains on held notes (critic B #2, #3).
# - "non div." chords of one section play two or three full-section samples: -7 / -11 CC11 units (1.5 dB per
#   doubling at 0.22 dB per unit) on the chords of bars 72 and 300 and the summit's stops (found: 3 chords each on
#   Violins II, Violas and Violoncellos; the violas' spans 360-420 and 624-672 hold no chord in the data, so their
#   two roles stay)
_ch17 = [(213.0, 216.0), (897.0, 900.0), (1005.0, 1017.0)]
CHORD_CC11 = {"Violins I": {"by": {2: 7, 3: 11}, "spans": _ch17}, "Violins II": {"by": {2: 7, 3: 11}, "spans": _ch17},
              "Violoncellos": {"by": {2: 7, 3: 11}, "spans": _ch17},
              "Violas": {"by": {2: 7, 3: 11}, "spans": _ch17 + [(360.0, 420.0), (624.0, 672.0)]},
              "Violas div": {"by": {2: 7, 3: 11}, "spans": [(624.0, 672.0)]}}
# - a crescendo gain that would be released inside a held note goes into CC11; the gains of the crescendos into bars
#   72 and 300 are dropped (their release took 2.3-2.8 dB away across the upbeat and the sf; the rise is in CC11)
HP_GAIN_TO_CC11 = {f_: {"db_per_unit": 0.22, "cap_add": 10, "min_s": 0.25, "rel_s": 0.6, "drop_ends": [213.0, 897.0],
                        "max_arrival_cc": 100}   # (records/hp_to_cc11_clipped.txt: 16 gains into ff arrivals lost 1.5-4 dB)
                   for f_ in ("string", "wind", "brass")}

# 6. Legato lead cap (critic A #1): measured from the previous note's moved note-on (build/lead_set.json keeps its values)
PREV_MIN_SOUND_S = 0.06
# the cello slur 504 -> 506 bursts 8-9 dB over both bodies (the transition sample; the +10 CC11 of c16 at 503-506 is
# gone): CC11 -14 across the transition (0.33 dB per unit at CC11 56-62), inside Opus; the same at 789
CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Violoncellos": [r_ for r_ in CC11_ADD_SPANS.get("Violoncellos", []) if r_[0] != 503.0]
                  + [(504.95, 505.25, 0, -14), (505.25, 505.6, -14, 0)]}

# 7. Leftover per-note lines (critic B #4): the c14 row-level lines that hold one level for 3 qn were written as slow
# rows (+6 dB over three notes on the celli at 333-341.4 and 933-941.4): no c14 row-level line is written
_c14_keys = {tuple(map(tuple, r_)) for r_ in __import__("json").load(open(_p)).get("Violoncellos", [])}
_n0 = len(LEVEL_SHAPES["Violoncellos"])
LEVEL_SHAPES["Violoncellos"] = [r_ for r_ in LEVEL_SHAPES["Violoncellos"]
                                if not (len({v_ for _, v_ in r_ if v_ != 0.0}) == 1 and r_[-1][0] - r_[0][0] >= 3.0
                                        and any(abs(r_[1][0] - k_) < 0.2 for k_ in (333.0, 933.0)))]
assert _n0 - len(LEVEL_SHAPES["Violoncellos"]) == 2, f"c17: {_n0 - len(LEVEL_SHAPES['Violoncellos'])} one-level celli lines found"

# 9. Timpani (critic B #6): the five summit strokes (printed fff) played velocity 121-125, the brightest layers, and a
# role then cut them 4 dB: velocity 104 (the cap of every other loud stroke), the role is removed (roles.json)
VEL_SET["Timpani"] = {**VEL_SET.get("Timpani", {}), 1008.0: 104, 1010.0: 104, 1012.0: 104, 1014.0: 104}
# 8. celli pp pizzicato sits on a sample-layer edge (velocity 41: -64.7 dB, 47: -57.8, 53: -51.8; the patch's layer
# changes at 50 / 51): the B pedal of bars 89-98 at velocity 52
VEL_SET["Violoncellos"] = {**VEL_SET.get("Violoncellos", {}), **{float(q_): 52 for q_ in range(264, 292)}}

# 5c. Slope guard (critic B): role edges on the score onset of a led note end on its moved note-on, over 0.03 s
ROLE_EDGE_MOVED = 0.03

# 10. (critic A #5) Horn 1's tenuto repeats on "Port Lng" (630, 633, 663) separated by 1.2-1.4 dB with a 90 ms gap; its
# other tenuto repeats play "Sus MAX" (5.3 dB median)
ART_AT = {**ART_AT, "Horn 1": {**ART_AT.get("Horn 1", {}), 630.0: "Sus MAX", 633.0: "Sus MAX", 663.0: "Sus MAX"}}
# (critic A #6) the two exposed join bumps of bars 349-356 (+7.5 / +7.9 dB): the targets at velocity 64 (upper strings
# gain 0.45-0.85 dB per 10 on the legato row's fronts)
VEL_SET["Violas div"] = {**VEL_SET.get("Violas div", {}), 1047.0: 64}
VEL_SET["Violin I solo"] = {**VEL_SET.get("Violin I solo", {}), 1065.0: 64}

# first c17 render: Violas bar 326 (qn 975-978, the coda's first entry) fell 8.6 dB with its one-bar +4.5 role and the
# soft staccato row gain gone: CC11 +14 over the bar (the row gain halved in mix.json)
CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Violas": CC11_ADD_SPANS.get("Violas", []) + [(974.8, 978.0, 14, 14)]}


# =====================================================================================================================
# c18 (2026-11-16): cycles/c18/CHANGES.md. Instrument side only; the volume envelope keeps slow balance.
# =====================================================================================================================
# 1. Crescendo arrivals (critics B #1-2, C #1). The c17 conversions of crescendo gains into CC11 assumed 0.22 dB per
# unit; on the c17 render (cycles/c18/actor_scripts/slope18.py: stem change less envelope change, over the CC11 change,
# c16 -> c17) the arrivals came within 0.5 dB of c16 only on Flute 1 (0.23 dB per unit at CC11 99-108), cor anglais
# (0.17), Violins I and II (0.16); the bassoons, clarinets, contrabassoon, oboe, horns, low brass, violas, celli and
# basses lost 1.3-6.5 dB (0.14 dB per unit or less, negative on the bassoons at CC11 88-98). Those four keep the CC11
# rule; every other gain stays in the envelope as the hairpin ramp, held to its arrival as before and released at
# 2.8 dB/s or slower (across a printed decrescendo: to its end; by the next softer printed mark). The gains into
# bars 72 and 300 are dropped on the strings only; on the winds and horns they come back, and a dropped gain that
# continues a chain keeps the earlier gain (bassoons 210 / 894). The gain at the sfp of bar 301 is held through the sf
# and released 0.22 s after it with the CC11 fall to the p (finale technique 78)
_hp18 = {"convert": False, "keep_rel_db_s": 2.8, "drop_keep_chain": True}
_hp18_cc = {"db_per_unit": 0.22, "cap_add": 10, "min_s": 0.25, "rel_s": 0.6, "max_arrival_cc": 100, "keep_rel_db_s": 2.8,
            "drop_keep_chain": True}
# (bars 72 / 300 on the winds: the chained crescendos' rise to +7 dB is not written, the earlier +4 dB is held; a
# simulation of the envelope on the c17 stems put bar 300 1 dB over the tutti with the rise)
_hp18w = {**_hp18, "drop_ends": [213.0, 897.0], "drop_only_chained": True}
HP_GAIN_TO_CC11 = {"wind": dict(_hp18w), "brass": dict(_hp18w), "string": {**_hp18, "drop_ends": [213.0, 897.0]},
                   "Flute 1": {**_hp18_cc, "drop_ends": [213.0, 897.0], "drop_only_chained": True},
                   "Cor anglais": {**_hp18_cc, "drop_ends": [213.0, 897.0], "drop_only_chained": True},
                   "Violins I": {**_hp18_cc, "drop_ends": [213.0, 897.0]}, "Violins II": {**_hp18_cc, "drop_ends": [213.0, 897.0]}}
HP_SUBITO_SFP_DELAY_S = 0.22
# bars 72 / 300 accents: +8 on every woodwind (min(8, add_loud) gave 0 on Flute 1, cor anglais, both clarinets and
# Bassoon 1); Flute 2's accent as B #4 asks (its isolated-accent p90 +5.4)
_ACC_BY = {**_ACC_BY, "Flute 2": (5, 4, 116)}
ACCENT_CC = {**ACCENT_CC, **{t_: {**_acc17, "add": a_, "add_loud": l_, "top": top_,
                                  "add_at": {213.0: (12 if top_ == 124 else 8), 897.0: (12 if top_ == 124 else 8)}}
                             for t_, (a_, l_, top_) in _ACC_BY.items()}}

# 2. Summit order (B #4-5, C #2): the summit's double and triple stops keep their CC11 (a section playing stops at fff is
# louder than one line); the ff accented timpani strokes at 114 (104 put them 3-5 dB under the printed f strokes before)
CHORD_CC11 = {t_: {**c_, "spans": [s_ for s_ in c_["spans"] if s_ != (1005.0, 1017.0)]} for t_, c_ in CHORD_CC11.items()}
VEL_SET["Timpani"] = {**VEL_SET["Timpani"], 1008.0: 114, 1010.0: 114, 1012.0: 114, 1014.0: 114}

# 4. String legato joins (critic A #1): the transition swells 98-128 ms before the beat (+3.3..+3.7 dB median over the new
# note's body): a CC11 dip from the moved note-on + 0.03 s, held to the beat - 0.02 s, back by the beat + 0.10 s, per
# join from the c17 measurement (excess 2.5-4 dB: 3 units, 4-6: 6, 6-9: 9, 9+: 12; build/leg_trans.json)
_lt = __import__("json").load(open(f"{BUILD}/leg_trans.json")) if _os.path.exists(f"{BUILD}/leg_trans.json") else {}
LEG_TRANS_CC = {t_: {"table": v_, "min_lead_s": 0.12, "from_s": 0.03, "fall_s": 0.03, "hold_s": -0.02, "ret_s": 0.10}
                for t_, v_ in _lt.items() if not t_.startswith("_") and t_ in (_os.environ.get("C18_LTC", "Violins I,Violins II,Violas,Violoncellos,Violin I solo,Violas div").split(","))}
# the c17 celli dip at 504.95-505.6 (mistimed: it ended before the swell)
CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Violoncellos": [r_ for r_ in CC11_ADD_SPANS["Violoncellos"] if not 504.9 < r_[0] < 505.3]}

# 5. Horn 1's motto tail (critic A #2): the three slurred arrivals at velocity 72 (velocity sets the transition speed on
# the brass legato rows, manual p.106; 106-112 is the fastest slur and left an 8-20 dB sag after each)
VEL_SET["Horn 1"] = {**VEL_SET.get("Horn 1", {}), 1071.0: 72, 1074.0: 72, 1077.0: 72}

# 6. Wind and brass joins (critic A #4; finale c19 #1; Movement I c60 #6): a pitch change between held notes (0.4 s or
# more) on one sustain row ends the old note 0.04 s after the new note-on (it left 50-90 ms of silence; finale c19 used
# 0.04-0.05 s, never on legato rows); held same-pitch
# repeats (0.6 s or more) keep a 25 ms gap, short tongued repeats keep the 65 / 90 ms floor (the trumpets' chords)
WIND_DETACH = {**WIND_DETACH, "overlap_s": 0.04, "overlap_min_s": 0.4,
               "by": {f_: {**v_, "overlap_s": 0.04, "overlap_min_s": 0.4} for f_, v_ in WIND_DETACH.get("by", {}).items()}}
REP_GAP_FLOOR_LONG_S = {"min_s": 0.6, "gap_s": 0.025}

# 8. Fugato (critic C #3): each p entry's held note louder than the one before (celli 171 -43.2, violas 183 -44.4,
# Violins II 195 -50.7 dB). Measured slopes on these notes c16 -> c17: violas 0.14 dB per unit (CC11 48 -> 41), Violins II
# 0.25 (52 -> 42)
CC11_ADD_SPANS = {**CC11_ADD_SPANS,
                  "Violas": CC11_ADD_SPANS.get("Violas", []) + [(182.9, 185.0, 14, 14), (878.9, 881.0, 14, 14)],
                  "Violins II": CC11_ADD_SPANS.get("Violins II", []) + [(194.9, 197.0, 30, 30)]}

# 9. Smaller items. Violins I's accented theme notes at 51 / 771 on "Sus Marc LITE" bit (2-5 kHz +6 dB): "Sus MAX" with
# the track's accent (A #5). The celli pp pizzicato group heads (the weakest round-robin sample on 264 / 273 / 282 / 291,
# 4.5 dB under the next): velocity 56, inside the layer above the 50 / 51 edge (A #6)
ART_AT["Violins I"] = {**ART_AT.get("Violins I", {}), 51.0: "Sus MAX", 771.0: "Sus MAX"}
VEL_SET["Violoncellos"] = {**VEL_SET["Violoncellos"], 264.0: 56, 273.0: 56, 282.0: 56, 291.0: 56}
# the violas' accented D4 at 978 lost the +14 at its led note-on (B #6 note)
CC11_ADD_SPANS["Violas"] = [(974.8, 979.4, 14, 14) if r_ == (974.8, 978.0, 14, 14) else r_ for r_ in CC11_ADD_SPANS["Violas"]]

# Delivery at -14 LUFS (Dan 2026-11-17; finale c21: ride rows on the ff passages, not mix trims): on the c18 render the
# quiet lift and top ride left the summit 0.1 LU over the trio's ff and bar 72; these rows bring it to +0.7 LU
RIDE_TRIMS = RIDE_TRIMS + [[(622.0, 0.0), (624.0, -2.0), (671.0, -2.0), (673.0, 0.0)],
                           [(211.5, 0.0), (212.5, -1.5), (216.3, -1.5), (217.0, 0.0)],
                           [(895.5, 0.0), (896.5, -2.0), (900.0, -2.0), (901.0, 0.0)],
                           [(911.0, 0.0), (912.4, -1.0), (959.0, -1.0), (961.0, 0.0)]]

# After the c18 render (not rendered yet; build/ is ahead of cycles/c18/build_render/):
# - Violins II's fugato held note 195: +30 units gave +14.3 dB (-50.8 -> -36.5, 0.48 dB per unit), 4.4 dB over the
#   violas' entry (-40.9): +24, aimed at about 1.5 dB over the violas
# - Violins I 51 / 771 on "Sus MAX" fell 7-8 dB (bars 18 and 258 -6.9 / -4.8 dB in the master): back to the theme's row
CC11_ADD_SPANS["Violins II"] = [(194.9, 197.0, 24, 24) if r_ == (194.9, 197.0, 30, 30) else r_ for r_ in CC11_ADD_SPANS["Violins II"]]
ART_AT["Violins I"] = {k_: v_ for k_, v_ in ART_AT["Violins I"].items() if k_ not in (51.0, 771.0)}


# =====================================================================================================================
# c19 (2026-11-17): cycles/c19/CHANGES.md. Instrument side only (Dan 2026-11-11: no per-note volume moves).
# =====================================================================================================================
# 1. String legato joins (critics A #1, C #2): the c18 CC11 dip over each transition did not reach the swell (the
#    renders are identical to 0.0 dB for 50 ms after each note-on; the swell peaks at about +70 ms, in the transition
#    sample) and moved string legato attacks 4-20 ms later. Removed; the transition groups ("TLeg <pitch>") of the
#    strings' "Leg Slur MAX" rows are lowered by region volume instead (mix.json region_gain_db, "group:TLeg")
LEG_TRANS_CC = {}

# 2. Wind overlap (critic C #1): tools/score_to_parts.py now tests the played row (REP_ROW's "Leg Slur Rep" on the
#    clarinets is legato: 34 tongued notes were slurred); woodwind overlap only between notes of 0.6 s or more (the
#    hemiola half notes of bars 101-104 / 301-304, 0.455 s, arrived 30-180 ms late with it)
WIND_DETACH = {**WIND_DETACH, "by": {**WIND_DETACH.get("by", {}),
                                      "wind": {**WIND_DETACH.get("by", {}).get("wind", {}), "overlap_s": 0.04, "overlap_min_s": 0.6}}}
# (critic A #5 asks to delete REP_GAP_FLOOR_LONG_S as a no-op; in parts.json it still sets 40 held same-pitch repeats
# (Horn 2, Horn 4, low brass, Bassoon 2) 20 ms shorter gaps than the floor: kept, the repeats are a do-not-touch item)

# 3. Hidden inner lines (critic B #1, #4; Dan 2026-11-17): Violins II's con sord. arpeggios of the trio (bars 168-184)
#    8.6-9.8 dB under the celli, best band -7.4 dB: +9 units (0.48 dB per unit at p: about +4.3 dB); the celli's first
#    fugato entry 4.1 dB under the violas' at the same p: +8 units
CC11_ADD_SPANS = {**CC11_ADD_SPANS,
                  "Violins II": CC11_ADD_SPANS.get("Violins II", []) + [(501.3, 551.4, 9, 9)],
                  "Violoncellos": CC11_ADD_SPANS.get("Violoncellos", []) + [(170.9, 174.0, 8, 8)]}

# 4. Horn 1's A4 -> G sharp 4 transition sample holes 9-11 dB at +0.30-0.34 s at every velocity (critic A #2; not phase):
#    the G sharps at 442 / 598 / 1077 play "Sus MAX" (a soft re-tongue), the A4 ends at the G sharp's moved note-on
ART_AT = {**ART_AT, "Horn 1": {**ART_AT.get("Horn 1", {}), 442.0: "Sus MAX", 598.0: "Sus MAX", 1077.0: "Sus MAX"}}
VEL_SET["Horn 1"] = {k_: v_ for k_, v_ in VEL_SET["Horn 1"].items() if k_ != 1077.0}   # (velocity 72 did nothing)

# 5. Leads (critics A #4, C #3-4): celli 933 / 948 back to their c17 leads (build/lead_set.json); Violins I 597 a
#    "Sus MAX" stroke (its lead_set row was capped at 132 ms by PREV_MIN_SOUND_S and did nothing)
DOWNBOW_STROKE_AT["Violins I"] = sorted(set(DOWNBOW_STROKE_AT["Violins I"] + [597.0]))
REATTACK_LEAD_AT["Violins I"] = {**REATTACK_LEAD_AT["Violins I"], 597.0: 0.085}
# Horn 3's re-tongued heads 510 / 519 asked 0.12 s and got 79 ms (RETONGUE_LEAD_CAP 0.3 x the 1 qn note before);
# the targets after the pickup eighths (512, 524) at legato velocity 120 (manual p.144: tighter transition, same level)
RETONGUE_LEAD_CAP_AT = {"Horn 3": {510.0: 0.46, 519.0: 0.46}}
VEL_SET["Horn 3"] = {**VEL_SET.get("Horn 3", {}), 512.0: 120, 524.0: 120}

# 6. Clarinet 1 the loudest stem in f-ff tuttis (critic B #3; up to +3.9 dB over Violins I): f / ff / fff layers 6-10
#    CC1 units lower (the clarinet's dynamics are on CC1)
CC1_DYN_MAP_BY = {**CC1_DYN_MAP_BY, "Clarinet 1": [(22, 18), (34, 28), (46, 42), (58, 54), (72, 68), (88, 80), (114, 98), (124, 110)]}

# 7. Accents (critic A #3; Dan 2026-11-11): string bumps at most 6 units where the resting CC11 is under 60
ACCENT_CC = {k_: ({**v_, "soft_cc": 60, "add_soft": 6} if (k_ == "string" or k_ in ("Violins I", "Violins II", "Violas")) else v_)
             for k_, v_ in ACCENT_CC.items()}

# 9. Per-note fader rows replaced on the instrument side (critic B #6; Dan's rule): the trumpets' pp eighths 994-995
#    (role -4 / -5 dB) and Horns 3-4's approach 990-995.8 (role -4) in CC11 (about 0.25-0.3 dB per unit there)
CC11_ADD_SPANS = {**CC11_ADD_SPANS,
                  **{t_: CC11_ADD_SPANS.get(t_, []) + [(993.85, 995.0, -u_, -u_), (995.0, 995.6, -u_, 0)]
                     for t_, u_ in (("Trumpet 1", 14), ("Trumpet 2", 16))},
                  **{t_: CC11_ADD_SPANS.get(t_, []) + [(989.5, 995.0, -14, -14), (995.0, 995.8, -14, 0)]
                     for t_ in ("Horn 3", "Horn 4")}}
# (the stroke left the next slurred note, 600, on "Sus MAX" at velocity 52 with no lead: it joins from the stroke on the
# legato row, as 158 does after the 157.5 stroke)
ART_AT["Violins I"] = {**ART_AT.get("Violins I", {}), 600.0: "Leg Slur MAX"}
VEL_SET["Violins I"] = {**VEL_SET.get("Violins I", {}), 600.0: 100}   # (c18's legato velocity there)
# (Horn 1's three Sus MAX G sharps 0.05 s early: a Sus MAX horn note from silence reaches body - 3 dB in 0.04-0.06 s)
REATTACK_LEAD_AT["Horn 1"] = {**REATTACK_LEAD_AT.get("Horn 1", {}), 442.0: 0.05, 598.0: 0.05, 1077.0: 0.05}

# Delivery (after the c19 render; finale c22 and Movement I c60/c61 notes): the trio ride row reached -2 dB on the ff
# arrival of bar 209 (master +2.3 LU over bar 208, mp3 -0.0): it now ramps over the arrival bar. (A row of -1.5 / -3 dB on
# bars 334-335 was tested for the summit step, master +1.8, mp3 0.0: bar 335 moved 0.1 LU, its 400 ms maximum is the
# bar-336 downbeat itself; not kept)
RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if r_ != [(622.0, 0.0), (624.0, -2.0), (671.0, -2.0), (673.0, 0.0)]] + \
             [[(625.0, 0.0), (627.0, -2.0), (671.0, -2.0), (673.0, 0.0)]]


# =====================================================================================================================
# c20 (2026-11-17): cycles/c20/CHANGES.md. Instrument side only (Dan 2026-11-11: no per-note volume moves); hidden inner
# lines first (Dan 2026-11-17). Range-test switches (environment; the defaults are the adopted values):
# C20_PAIRS sus | detache | stacsl, C20_V999 none | vel | marc, C20_CL1ROW rep | leg
# =====================================================================================================================
# 1a. Violins II's con sord. arpeggios (critic B #1): covered from bar 175 once Violins I join; their CC11 drifts from 54
#     to 50 over 519-546 with no hairpin. The +9 of c19 rises to +17 over 526-549.4 and returns before the printed
#     decrescendo of 549.5 (0.48 dB per unit at p: about +2 to +4 dB in bars 177-183)
_v2t = (501.3, 551.4, 9, 9)
assert _v2t in CC11_ADD_SPANS["Violins II"], "c20: the c19 Violins II trio span was not found"
CC11_ADD_SPANS["Violins II"] = [r_ for r_ in CC11_ADD_SPANS["Violins II"] if r_ != _v2t] + \
    [(501.3, 526.0, 9, 9), (526.0, 534.0, 9, 14), (534.0, 549.4, 14, 17), (549.4, 551.4, 17, 9)]

# 2. Slurred eighth pairs in the Allegro's staccato lines (critic C #2): two "Sus MAX" notes of 0.12 s never reach their
#    body (bar 23: -41.6 / -52.0 / -47.7 / -30.0 dB under a crescendo). Range test bars 20-24 and 113-119 against a
#    control from the same start: "Detache" (manual p.90) or "StacSl Leg BC + Slur + Port MAX" (p.99)
_C20_PAIRS = _os.environ.get("C20_PAIRS", "sus")   # c21 (Dan 2026-11-17, bar 23 "blur together ... lasting too long"): back to the c19 state, see the c21 block   # range tests: Detache on Violins I adopted (holes 4 -> 1 of 12
# pairs), not on Violins II (no better than Sus MAX); StacSl rejected (p pairs -10..-14 dB, f pairs +6..+14, +2.3 GB)
_c20_pairs = {"Violins I": [67.0, 113.0, 125.0, 209.0, 317.0, 329.0, 343.0, 347.0, 353.0, 787.0, 821.0, 893.0, 917.0,
                            929.0, 943.0, 947.0, 953.0, 1001.0],
              "Violins II": [125.0, 197.0, 317.0, 329.0, 343.0, 347.0, 353.0, 821.0, 917.0, 929.0, 943.0, 947.0, 953.0,
                             983.0, 1001.0]}
if _C20_PAIRS in ("detache", "detache1"):
    DETACHE_SPANS = {t_: [(q_ - 0.01, q_ + 0.51) for q_ in v_] for t_, v_ in _c20_pairs.items()
                     if _C20_PAIRS == "detache" or t_ == "Violins I"}
elif _C20_PAIRS == "stacsl":
    STACLEG_ART = "StacSl Leg BC + Slur + Port MAX"
    STACLEG_SPANS = {**STACLEG_SPANS, "Violins I": [(q_ - 0.01, q_ + 0.51) for q_ in _c20_pairs["Violins I"]]}
if _C20_PAIRS in ("detache", "detache1", "stacsl"):   # (the rows' own velocity, 100 / 110, only on the loud pairs; the soft pairs
    # at about their staccato neighbours' velocity + 5, as Sus MAX played them)
    VEL_SET["Violins I"] = {**VEL_SET["Violins I"], **{q_ + h_: v_ for q_, v_ in ((67.0, 62), (113.0, 66), (787.0, 69)) for h_ in (0.0, 0.5)}}
    for t_, l_ in (("Violins I", 0.045), ("Violins II", 0.035)):   # (the rows take no lead: the staccato lead, STAC_LEAD_S)
        if t_ == "Violins I" or _C20_PAIRS == "detache":
            LEAD_SET_AT[t_] = {**LEAD_SET_AT.get(t_, {}), **{str(q_ + h_): l_ for q_ in _c20_pairs[t_] for h_ in (0.0, 0.5)}}
    if _C20_PAIRS == "detache":
        VEL_SET["Violins II"] = {**VEL_SET.get("Violins II", {}), **{q_ + h_: v_ for q_, v_ in ((197.0, 88), (983.0, 68)) for h_ in (0.0, 0.5)}}

# 3. Summit arrival on the mp3 (critic C #1; finale technique 94): a delivery ride row deeper than the limiter's own
#    reduction on bars 331-335, released into the fff (C's offline run on the c19 master: fff +1.3 LU over bar 335)
RIDE_TRIMS = RIDE_TRIMS + [[(990.0, 0.0), (993.0, -2.0), (996.0, -4.0), (1004.6, -4.5), (1005.1, 0.0)]]

# 4. Accented half notes after staccato eighths (critic A #2): the cor anglais and Flute 1 had no accent bump (_ACC_BY
#    0); their accents came in 1.7-4.8 dB under the eighths for 100-200 ms. +6 units, and the accented Sus note after a
#    staccato starts 0.04 s earlier (the staccato before it plays with no lead)
_ACC_BY = {**_ACC_BY, "Cor anglais": (6, 6, 116), "Flute 1": (6, 6, 116)}
ACCENT_CC = {**ACCENT_CC, **{t_: {**_acc17, "add": _ACC_BY[t_][0], "add_loud": _ACC_BY[t_][1], "top": _ACC_BY[t_][2],
                                  "add_at": {213.0: 8, 897.0: 8}} for t_ in ("Cor anglais", "Flute 1")}}
ROW_CHANGE_ACC_ADD_S = {"Flute 1": 0.04, "Oboe 1": 0.04, "Cor anglais": 0.04}

# 6. Clarinet 1's trio tune (critic C #3): range test on "Leg Slur" (the tune 456-504 has no same-pitch repeats)
if _os.environ.get("C20_CL1ROW", "rep") == "leg":
    REP_ROW = dict(REP_ROW, **{"Clarinet 1": [(0.0, 456.0, "Leg Slur Rep"), (504.0, SCORE_END, "Leg Slur Rep")]})

# 7. Clarinet 1 bar 214 (critic B #3): its mf hairpin gains in the trio return (2 dB each) put the crest at beat 640
#    6.3 dB over Violins I, at a printed mf against the violins' f: dropped. Violins I's accented G6 at 999 2.6 dB
#    under its own staccatos: range test velocity 112 against "Sus Marc LITE"
HP_GAIN_TO_CC11 = {**HP_GAIN_TO_CC11, "Clarinet 1": {**HP_GAIN_TO_CC11["wind"], "drop_always": [633.0, 640.0, 645.0, 663.0]}}
_C20_V999 = _os.environ.get("C20_V999", "none")   # c21 (critic B #2): back to "Sus MAX" (the LITE row's -8 dB put bar 333 6 dB under 332 / 334)
_C20_V999_c20 = "marc"   # (range renders unreliable at this start; marc adopted on B's
# reading of the row's accented halves at 302 / 910, +4.0 / +1.5 dB; Sus MAX velocity does not set level)
if _C20_V999 == "vel":
    VEL_SET["Violins I"] = {**VEL_SET["Violins I"], 999.0: 112}
elif _C20_V999 == "marc":
    ART_SPANS["Violins I"] = [{"from": 998.99, "to": 999.01, "art": "Sus Marc LITE",
                               "vel_by_cc": [(58, 74), (72, 80), (88, 84), (100, 88), (114, 96)]}] + ART_SPANS["Violins I"]

# 9. Smaller items.
# - Horn 1's "Sus MAX" G sharps (critic A #3): CC1 65-69 faded in part of the f layer (10-15 dB brighter than the
#   slurred A4 under the diminuendo): at most 51 (the mf layer) from just before the moved note-on
CC1_SET_SPANS = {"Horn 1": [(441.7, 445.0, 51), (597.7, 600.0, 51), (1076.7, 1097.2, 51)],
# - the cor anglais' hemiola notes (critic A #6): CC1 45, the non-vibrato layer (the D sharp swings 7-9 dB at +0.1-0.4 s)
                 "Cor anglais": [(301.8, 303.6, 45), (305.8, 307.6, 45), (901.8, 903.6, 45), (905.8, 907.6, 45)]}
# - the timpani's crescendo of bar 335 into the ff roll (critics A #5, B): four strokes at 104 played flat
#   (the "Timpani Flt Sht" layers: 93-98, 99-104, 105-110, 111-115; 98 / 104 / 106 / 110 climb three layers and stay
#   under the ff accents' 111-115 layer at 1008-1014; the coordinator's 100 / 104 / 108 / 112 put 1004 in that layer)
VEL_SET["Timpani"] = {**VEL_SET["Timpani"], 1002.0: 98, 1003.0: 104, 1003.5: 106, 1004.0: 110}
# - single staccato notes 7-11 dB off their neighbours (critic C #4): into the next velocity layer (the short rows'
#   layer edges: 1st Violins Staccatissimo 54 / 55, 2nd Violins Spiccato 79 / 80, Stac 91 / 92)
VEL_SET["Violins I"] = {**VEL_SET["Violins I"], 60.0: 52}
VEL_SET["Violins II"] = {**VEL_SET.get("Violins II", {}), 957.0: 78, 988.5: 94}
ROW_CHANGE_ACC_SKIP = [213.0, 300.0, 897.0, 1005.0]   # (the sf chords of bars 72 / 300, the hemiola's f, the fff downbeat)

# 5. String legato swell (critic A #1): range tests from the same start against a control: Violas "TLeg" -6 dB and
#    celli LegatoSpeed RELEASE 200 ms both failed (cycles/c20/CHANGES.md). Third test (finale technique 98): "Sus MAX"
#    on the long arrival notes that swell most (re-bowed, so no longer slurred); C20_LEGSUS=1
if _os.environ.get("C20_LEGSUS") == "1":
    for t_, qs_ in (("Violas", (726.0, 632.0, 387.0, 375.0)), ("Violoncellos", (516.0, 637.0)),
                    ("Violin I solo", (1065.0, 1049.0)), ("Violas div", (1047.0,))):
        ART_AT[t_] = {**ART_AT.get(t_, {}), **{q_: "Sus MAX" for q_ in qs_}}
        REATTACK_LEAD_AT[t_] = {**REATTACK_LEAD_AT.get(t_, {}), **{q_: 0.085 for q_ in qs_}}
# (result: Sus MAX on the celli's 516 took its swell away (body -35.8 -> -39.9 dB) but the slurred 514 before it fell
# 14 dB for its whole length; the violas' 726 body unchanged. Not adopted: the swell stays, listed in CHANGES.md)

# After the c20 render: Horn 1's CC1 cap at 51 took the G sharps' brightness down 3.7-4.1 dB only (still 11-15 dB over
# the A4's; target within 5) and their bodies 6.3-6.9 dB (bars 363-364 -1.8 / -2.5 dB in the master): removed. The
# cor anglais cap stays (swing +0.1-0.4 s 8.5-13.4 -> 1.7-6.9 dB)
CC1_SET_SPANS = {k_: v_ for k_, v_ in CC1_SET_SPANS.items() if k_ != "Horn 1"}


# =====================================================================================================================
# c21 (2026-11-17): cycles/c21/CHANGES.md. Instrument side only (Dan 2026-11-11: no per-note volume moves); -14 LUFS
# delivery and inner lines (Dan 2026-11-17). Range-test switches (environment; defaults are the adopted values):
# C21_DET2 (lead of the Detache pairs' second note, s), C21_SACC 0 | 1 (woodwind "Sus Accent MAX"), C21_V1TRIO 0 | 1
# =====================================================================================================================
# 1. Hall at the G.P. on the delivered mp3 (critic C #1): the limiter releases after the fff chord stops and lifts the
#    tail about 6 dB (G.P. drop at +0.3 s master 18.3 dB, mp3 12.0; 20 dB fall 0.33 / 0.47 s). A delivery-only row that
#    follows the release down and is back at 0 before bar 341 (C's simulation: drop 18.1 dB, fall 0.35 s, I / LRA /
#    limiter / bar 341 unchanged)
RIDE_TRIMS = RIDE_TRIMS + [[(1015.3, 0.0), (1015.8, -6.0), (1019.4, -6.0), (1019.8, 0.0)]]

# 2. Coda pp stretto, bars 325-327 (critic B #1, Dan 2026-11-17 "too soft ... especially in quiet parts"): role rows in
#    build/roles.json (cycles/c21/actor_scripts/apply21.py); the celli's accented half note at 975 ("Sus MAX", CC11 28-35)
#    reads 7-11 dB under its own staccatos: +16 units (to 44-51, under the pp layer's 52). Violins II's 981 half note
#    starts at CC11 36 inside the crescendo: +8 easing to 0 at 983. The violas' 978 half note keeps c18's +14, which now
#    lasts to the slurred pair's note-on (it fell 14 units 0.3 qn before the note's end)
CC11_ADD_SPANS = {**CC11_ADD_SPANS,
                  "Violoncellos": CC11_ADD_SPANS.get("Violoncellos", []) + [(974.3, 976.70, 16, 16)],
                  "Violins II": CC11_ADD_SPANS.get("Violins II", []) + [(980.35, 983.0, 8, 0)]}
assert (974.8, 979.4, 14, 14) in CC11_ADD_SPANS["Violas"]
CC11_ADD_SPANS["Violas"] = [(974.8, 979.68, 14, 14) if r_ == (974.8, 979.4, 14, 14) else r_ for r_ in CC11_ADD_SPANS["Violas"]]

# 4. Violins I "Detache" pairs (critics A #3, B #5): the second note peaks 0.115 s after its note-on (the first 0.038 s),
#    so with one 0.045 s lead its weight lands almost on the next eighth and the slur reads as a 9 dB trough: the second
#    note 0.09 s early (the release cap on "Detache" is in mix.json)
_det2 = float(_os.environ.get("C21_DET2", "0.09"))
if _C20_PAIRS in ("detache", "detache1"):   # (C20_PAIRS=sus: the c19 state, Sus MAX pairs with their c19 leads)
    LEAD_SET_AT["Violins I"] = {**LEAD_SET_AT["Violins I"], **{str(q_ + 0.5): _det2 for q_ in _c20_pairs["Violins I"]}}

# 6. Bassoon 2's trio phrase (critic B #3): a 12 s phrase whose crescendo to p ends 2.5 s before its held notes was a
#    "build" (enter -12, rise to +14 at 0.95): its held p notes swelled 10 dB with no hairpin. A crescendo makes a build
#    only when it arrives within 1.5 s of the phrase end; no printed-rise test inside the lyric spans
if _os.environ.get("C21_PSOLD") != "1":   # (C21_PSOLD=1: the c20 rule, to list the phrases that change type)
    PHRASE_SHAPE = {**PHRASE_SHAPE, "types": {**PHRASE_SHAPE["types"], "build_end_s": 1.5, "build_rise_lyric": False,
                                              "build_rule_spans": [(456.0, 720.0)]}}
# (everywhere, the rule turned 41 phrases from build to lyric, 34 of them the second idea's tutti phrases of bars 45-56,
# 121-132 and 277-288: their printed crescendos kept their rise, but their ff ends fell 8-17 units; kept to the trio,
# where 7 phrases change: Bassoon 2 528-551 (end 60 -> 32 units), Clarinet 1 573-600, Bassoon 1 576-587, Horns 1-2
# 582-600 and 648-669, violas 576-624, no crescendo rise changed)

# 7. Accents (critic A #2): 113 of 144 isolated accents are sustained notes after a staccato, whose attack is 2.1 dB
#    stronger; the accented notes peak 0.29-0.35 s after the beat. The c20 0.04 s on Flute 1 / Oboe 1 / cor anglais
#    (+1.8-2.4 dB on the first 100 ms) extended to Flute 2, Clarinet 2 and the strings; Violins II not after "Stac RRx9"
#    (that group already reads +3.2)
ROW_CHANGE_ACC_ADD_S = {**ROW_CHANGE_ACC_ADD_S, **{t_: 0.04 for t_ in ("Flute 2", "Clarinet 2", "Violins I", "Violins II",
                                                                     "Violas", "Violoncellos")}}
ROW_CHANGE_ACC_SKIP_PREV = {"Violins II": ["Stac RRx9"]}
#    Oboe 1 (critic B #4): the accented D5 at 276 heads a "Leg Slur MAX" slur at CC11 46 (6.6 against 12-15 for its
#    staccatos): "Sus MAX" as on 87 / 99; the accented B5 at 111 reads 14.8 dB under the staccato before it: CC11 +12
ART_AT["Oboe 1"] = {**ART_AT.get("Oboe 1", {}), 276.0: "Sus MAX"}
CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Oboe 1": CC11_ADD_SPANS.get("Oboe 1", []) + [(110.6, 112.85, 12, 12)]}
#    range test (C21_SACC=1): the woodwind KS Masters' own "Sus Accent MAX" row on the accented Sus notes after
#    staccatos, Oboe 1 87-123 and cor anglais 300-351, no CC11 bump on that row, velocity 70 at p-mf / 90 at f
# (range test, A against a control from the same start: Oboe 1 first 100 ms against its neighbours -3.8 -> -2.2 dB median,
# peak 0.29 -> 0.03 s after the beat, 2-5 kHz attack minus body -3.4..+1.0 dB (no bite), 111 -11.2 -> -7.3 with the
# +12; cor anglais no better (300 -1.0 -> -7.0): adopted on Oboe 1 only, C21_SACC=1 for both)
_sacc = _os.environ.get("C21_SACC", "oboe")
if _sacc in ("1", "oboe"):
    for t_, qv_ in (("Oboe 1", {87.0: 70, 99.0: 70, 111.0: 70, 123.0: 90}),
                    ("Cor anglais", {300.0: 80, 315.0: 90, 327.0: 90, 345.0: 90, 351.0: 90})):
        if _sacc == "oboe" and t_ != "Oboe 1":
            continue
        ART_AT[t_] = {**ART_AT.get(t_, {}), **{q_: "Sus Accent MAX" for q_ in qv_}}
        VEL_SET[t_] = {**VEL_SET.get(t_, {}), **qv_}
        ACCENT_CC[t_] = {**ACCENT_CC[t_], "skip_rows": tuple(ACCENT_CC[t_].get("skip_rows", ())) + ("Sus Accent MAX",)}

# 9. Violins I's trio doubling of the celli's tune, bars 177-184 (critic A #6; manual p.144: legato velocity is the
#    transition speed): velocity 80 like the celli (106-112 before)
if _os.environ.get("C21_V1TRIO", "1") == "1":
    LEG_VEL_SPANS = {**LEG_VEL_SPANS, "Violins I": LEG_VEL_SPANS.get("Violins I", []) + [(527.5, 552.0, 80)]}


# =====================================================================================================================
# c22 (2026-11-17): cycles/c22/CHANGES.md. Instrument side only (Dan 2026-11-11: no per-note volume moves); Dan's bar 23
# figure first, hidden inner lines and the -14 delivery (Dan 2026-11-17). Range-test switches (environment; defaults are
# the adopted values): C22_PAIRS 0 | 1, C22_V1LEAD 0 | 1, C22_WACC 0 | 1 (flute / oboe "Sus Accent MAX"), C22_MARC 0 | 1
# (Violins II / violas accents on "Sus Marc LITE"), C22_LOOK (crescendo look-ahead, qn)
# =====================================================================================================================
# 1. Bar 23 figure (critic A #1, #5; Dan's note): the soft Sus MAX pairs (CC11 54-73) play the p groups (350 ms release
#    cap) and ring 0.17-0.29 s, 7-13 dB under their neighbours; velocity does nothing on this row (no MidiVelocity
#    processor, regions 1-127). CC11 lift from the preceding note's note-off into the second pair note (Opus smooths CC11
#    over 120 ms = 0.53 qn), onto the mf groups (150 ms cap); the loud pairs (CC11 82-92) +8
_C22_PAIRS = _os.environ.get("C22_PAIRS", "short")
# (range test, bars 21-43 and 256-266 against a control from the same start: the lift brought the pairs to -3.4 / -6.9,
# -2.1 / -5.1 and -1.1 / +2.3 dB from their neighbours (c21 -8.5 / -12.8, -6.9 / -13.1, -17.3 / -11.7), but the second
# pair note at mf grew into the landing note (bar 23: decay before the next note-on 1.5 -> -4.2 dB, figure median
# 2.7 -> 0.0) and the landing notes fell 4-11 dB; bar 42's loud pair 5.2 -> 1.7 dB. Rejected (Dan's blur note first):
# C22_PAIRS=1 rebuilds it. Fallback, "marc": the nine theme-head pairs' treatment on the three soft pairs)
if _C22_PAIRS == "1":
    CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Violins I": CC11_ADD_SPANS.get("Violins I", [])
                      + [(66.30, 67.70, 20, 20), (112.30, 113.70, 20, 20), (786.30, 787.70, 16, 16)]
                      + [(q_ - 0.70, q_ + 0.70, 8, 8) for q_ in (125.0, 209.0, 821.0, 893.0)]}

# (range tests, control / lift to 67.7 / "marc" / "short" from 66.3 / "short" from 66.45; cycles/c22/CHANGES.md): only
# "short" brought the second pair note's decay before the landing note up everywhere (bar 23 1.5 -> 8.2, 38 5.5 -> 7.3,
# 263 4.1 -> 5.3 dB) with the pairs nearer their neighbours (bar 23 -8.5 / -12.8 -> -2.4 / -0.8, 38 -6.9 / -13.1 ->
# -3.9 / -8.5, 263 -17.3 / -11.7 -> +1.2 / +2.4); at bar 23 the preceding staccato quarter's tail rose under the lift
# (decay before the G 3.8 -> -2.9 dB; figure median 2.7 -> 0.9), so bar 23 keeps the c21 state (the coordinator's rule:
# no occurrence worse than c21). Adopted on bars 38 and 263
_skip22 = [float(x_) for x_ in _os.environ.get("C22_SKIP", "66").split(",") if x_]
_s22 = float(_os.environ.get("C22_LIFT_FROM", "0.45"))   # lift start after the preceding quarter (its note ends at +0.30)
if _C22_PAIRS == "short":   # the lift ends 0.06 qn after the second pair note's moved note-on: its group (mf, 150 ms
    # release cap) is chosen at the note-on, then CC11 falls under it (Opus smooths over 0.53 qn), so it does not grow
    # into the landing note
    CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Violins I": CC11_ADD_SPANS.get("Violins I", [])
                      + [(_s22 + q_, q_ + 1.30, a_, a_) for q_, a_ in ((66.0, 20), (112.0, 20), (786.0, 16)) if q_ not in _skip22]}
if _C22_PAIRS == "marc":
    _pq22 = [q_ + h_ for q_ in (67.0, 113.0, 787.0) for h_ in (0.0, 0.5)]
    ART_SPANS["Violins I"] = [{"from": q_ - 0.01, "to": q_ + 0.01, "art": "Sus Marc LITE",
                               "vel_by_cc": [(34, 70), (46, 78), (58, 86), (72, 94)]} for q_ in _pq22] + ART_SPANS["Violins I"]
    REATTACK_LEAD_AT["Violins I"] = {**REATTACK_LEAD_AT["Violins I"], **{q_: 0.09 for q_ in _pq22 if q_ not in (67.0, 787.0)}}
    # (67 / 787 follow a staccato quarter that ends early, so no re-attack lead applies: the entry lead put them 0.12 s
    # early; 0.09 s as the others)
    LEAD_SET_AT["Violins I"] = {**LEAD_SET_AT.get("Violins I", {}), "67.0": 0.09, "787.0": 0.09}
    SHORT_SUS_LEG_AT = {**SHORT_SUS_LEG_AT, "Violins I": [q_ for q_ in SHORT_SUS_LEG_AT["Violins I"] if q_ not in _pq22]}
    NOTE_END_AT = {**NOTE_END_AT, "Violins I": {**NOTE_END_AT.get("Violins I", {}), **{q_ + 0.5: q_ + 0.52 for q_ in (67.0, 113.0, 787.0)}}}

# 4. Crescendos into the ff tuttis (critic C #3): Flute 1's p < ... ff printed one beat after the hairpin's stop stayed at
#    mp and stepped +46 units at the ff (qn 300-312, 900-912)
HP_TARGET_LOOKAHEAD_QN = float(_os.environ.get("C22_LOOK", "2.5"))

# 5. Accents (critics A #2, A #3, B #4; Dan 2026-11-11: median +1..+2 dB over the neighbours, no track over +3)
#    Flutes: the KS Master's own "Sus Accent MAX" (layers 1-74 / 75-114 / 115-127, the "StacSs" overlay) on the accented
#    Sus MAX notes, velocity 70 under CC11 80, 90 from 80, no CC11 bump on that row (Oboe 1's c21 settings).
#    Oboe 1's four p accents (B #4: 1.3-8.8 dB under the staccato before them at velocity 70, the soft layer): 96, the
#    f accent 123: 105 (both in the middle layer, 75-114)
_wacc = {"Flute 1": [87.0, 99.0, 111.0, 123.0, 132.0, 144.0, 207.0, 213.0, 300.0, 302.0, 304.0, 306.0, 308.0, 310.0,
                     315.0, 327.0, 345.0, 351.0, 789.0, 819.0, 828.0, 891.0, 897.0, 902.0, 904.0, 906.0, 908.0, 910.0,
                     945.0, 999.0, 1005.0, 1008.0, 1010.0, 1012.0, 1014.0],
         "Flute 2": [123.0, 213.0, 315.0, 327.0, 345.0, 351.0, 819.0, 897.0, 945.0, 1014.0]}
_wacc_cc = {"Flute 1": {87.0: 46, 99.0: 46, 111.0: 51, 300.0: 52, 302.0: 60, 789.0: 74, 828.0: 60, 891.0: 79, 902.0: 57}}
# (CC11 at the note-on with the crescendo look-ahead below; 304-310 / 904-910 now 82-104)
if _os.environ.get("C22_WACC", "1") == "1":
    for t_, qs_ in _wacc.items():
        ART_AT[t_] = {**ART_AT.get(t_, {}), **{q_: "Sus Accent MAX" for q_ in qs_}}
        VEL_SET[t_] = {**VEL_SET.get(t_, {}), **{q_: (70 if _wacc_cc.get(t_, {}).get(q_, 100) < 80 else 90) for q_ in qs_}}
        ACCENT_CC[t_] = {**ACCENT_CC.get(t_, ACCENT_CC.get("wind", {})),
                         "skip_rows": tuple(ACCENT_CC.get(t_, ACCENT_CC.get("wind", {})).get("skip_rows", ())) + ("Sus Accent MAX",)}
    VEL_SET["Oboe 1"] = {**VEL_SET["Oboe 1"], 87.0: 96, 99.0: 96, 111.0: 96, 123.0: 105}
#    Violins II / violas: their accents on Sus MAX peak 225-262 ms after the beat with the body louder than the front
#    (A #2); the sections' own "Sus Marc LITE" (marcato overlay over the sustain, manual p.91-92) as on Violins I, with
#    Violins I's velocities by CC11; region gain, soft-layer trim and 120 ms release cap in mix.json; no CC11 bump there
_marc = {"Violins II": [123.0, 132.0, 144.0, 213.0, 300.0, 302.0, 304.0, 306.0, 308.0, 310.0, 315.0, 327.0, 345.0, 351.0,
                        819.0, 897.0, 902.0, 904.0, 906.0, 908.0, 910.0, 915.0, 927.0, 945.0, 951.0, 999.0, 1005.0,
                        1008.0, 1010.0, 1012.0, 1014.0],
         "Violas": [123.0, 132.0, 144.0, 213.0, 300.0, 302.0, 304.0, 306.0, 308.0, 310.0, 819.0, 897.0, 902.0, 904.0,
                    906.0, 908.0, 910.0, 999.0, 1005.0, 1008.0, 1010.0, 1012.0, 1014.0]}
C22_MARC = _os.environ.get("C22_MARC", "0") == "1"
# (range test against a control: Violins II's tutti accents 300 / 302 read -47 / +49 dB against their neighbours (the
# row's notes did not start where the Sus MAX notes had), the violas' 902-910 -0.8 -> -2.8 median, 213 unchanged; the
# finale's c24 found the same row negative on 2nd Violins / violas held chords: rejected, C22_MARC=1 rebuilds it)
if C22_MARC:
    for t_, qs_ in _marc.items():
        ART_SPANS[t_] = [{"from": q_ - 0.01, "to": q_ + 0.01, "art": "Sus Marc LITE",
                          "vel_by_cc": [(58, 74), (72, 80), (88, 84), (100, 88)]} for q_ in qs_] + ART_SPANS.get(t_, [])
        ACCENT_CC[t_] = {**ACCENT_CC.get(t_, ACCENT_CC["string"]),
                         "skip_rows": tuple(ACCENT_CC.get(t_, ACCENT_CC["string"]).get("skip_rows", ())) + ("Sus Marc LITE",)}

# 7. Violins I repeated staccato eighths (critic A #4): in 8 of 49 same-pitch pairs the first eighth (peak 81-103 ms after
#    its note-on) covers the second's attack: 0.07 s lead on the first eighth only (0.045 s STAC_LEAD_S on the second)
if _os.environ.get("C22_V1LEAD", "0") == "1":   # (range test: separation median 4.5 -> 3.8 dB (bars 20-43), 4.6 -> 5.1 (256-266), p10 0.4 -> 0.8 / 3.1 -> 0.9: no gain, rejected)
    LEAD_SET_AT["Violins I"] = {**LEAD_SET_AT.get("Violins I", {}), **{str(q_): 0.07 for q_ in (
        37.0, 43.0, 49.0, 55.0, 64.0, 73.0, 79.0, 91.0, 103.0, 106.0, 109.0, 115.0, 121.0, 127.0, 205.0, 283.0, 292.0,
        313.0, 319.0, 325.0, 331.0, 340.0, 349.0, 355.0, 757.0, 763.0, 769.0, 775.0, 784.0, 793.0, 799.0, 811.0, 817.0,
        823.0, 889.0, 913.0, 919.0, 925.0, 931.0, 940.0, 949.0, 955.0, 982.0, 985.0, 988.0, 991.0, 994.0, 997.0)}}
#    Fugato violas entries, bars 61 / 293 (critic C #5): the entry bar is the low point of the fugato (3.5 dB under the bar
#    before); the head's staccatos at CC11 41-50 +8 over the entry's first bar
CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Violas": CC11_ADD_SPANS.get("Violas", []) + [(179.6, 182.9, 8, 8), (875.6, 878.9, 8, 8)]}

# 6. Delivery (critics C #1, C #4; shared spec 2026-11-17 "climax margin before loudness range"): ride rows on the rival
#    ff passages (bar 53, the trio's A6 at 651, on top of its -2 row) and a lift of the counterstatement, the softest p
#    passage on the mp3 (-21.5 against the ppp intro -18.8), returning to 0 across the printed crescendo of 37-40; the
#    chain itself (peak compressor -9 dB 3:1, top ride 6 dB under p95, quiet lift 2.1) is in tools/deliver_master.py
RIDE_TRIMS = RIDE_TRIMS + [[(154.0, 0.0), (156.0, -1.5), (164.0, -1.5), (166.0, 0.0)],
                           [(645.0, 0.0), (647.0, -1.5), (656.0, -1.5), (659.0, 0.0)],
                           [(83.5, 0.0), (84.5, 1.5), (104.0, 2.0), (108.0, 2.0), (116.0, 0.0)]]


# =====================================================================================================================
# c23 (2026-11-17): cycles/c23/CHANGES.md. Instrument side only (Dan 2026-11-11: no per-note volume moves); Dan's bar 23
# figure first, then Violins I staccato blur, accents and the coda / trio balance. Range-test switches (environment;
# defaults are the adopted values): C23_F23 (bar 23 route: "lead", "cc1", both comma-separated, or "" for the c22 state),
# C23_LOUD (the same route on the loud pairs 125 / 209 / 821 / 893: 1 | 0), C23_STAC (Violins I STAC_MIN_SOUND_S: 1 | 0),
# C23_WACC (woodwind tutti accents on the accent rows: 1 | 0), C23_FHP (Flute 1 crescendo shape: 1 | 0). The release caps
# that go with C23_F23 "cap" and C23_STAC live in build/mix.json (cycles/c23/actor_scripts/apply23.py)
# =====================================================================================================================
# 1. Bar 23 figure (critics A #1, C #1; Dan's note): the soft pair G5 / A5 (qn 67 / 67.5, "Sus MAX", CC11 59-62) sits
#    13 dB under its neighbours and both eighths peak 116 / 138 ms after their note-on (an eighth is 114 ms), so A still
#    sounds when the landing B starts (decay 1.8 dB). (a) lead 0.10 s on both, each ending 0.03 s before the next moved
#    note-on (C #1); (b) CC1 floor 108 over the pair (Molto Vib, recorded louder; the staccato F sharp before and the
#    landing B have no CC1 processor), CC11 unchanged (A #1a)
# (range tests from qn 54 against a control from the same start, cycles/c23/CHANGES.md: lead -> pair -8.5 / -12.8 ->
# -2.3 / -4.3 and -3.2 / -5.1 dB (two passes), A -> B decay 1.5 -> 6.6 / 7.1 dB, G -> A 10.7 -> 8.4 / 5.3, figure median
# 2.7 -> 3.9 / 3.3; F sharp -> G 3.8 -> 1.1 / 1.2 (the earlier G under the staccato's tail; with the G at 0.06 s -3.2,
# round-robin scatter). cc1 -> the A at +3.5 dB over its neighbours and still rising into the B (decay -1.9): rejected.
# Sus MAX p cap 150 ms alone: decay 1.5 -> 1.4, pair -8.2 / -10.9: no gain, not adopted. Adopted: lead, bar 23 only)
_f23 = [x_ for x_ in _os.environ.get("C23_F23", "lead").split(",") if x_]
_loud23 = _os.environ.get("C23_LOUD", "0") == "1"
# (C23_LOUD=1, range test: pairs 125 / 209 / 821 / 893 nearer their neighbours by 1-3 dB, but the second note's decay
# before the landing note fell 2.0 -> 0.4 (125), 1.9 -> 0.4 (209), figure median 9.0 -> 4.4 dB (821 / 893): rejected)
_pairs23 = [(67.0, 108, (66.35, 67.70))] + ([(q_, 112, (q_ - 0.65, q_ + 0.70)) for q_ in (125.0, 209.0, 821.0, 893.0)] if _loud23 else [])
if "lead" in _f23:
    _l23 = float(_os.environ.get("C23_LEAD", "0.10"))
    _q23 = lambda q_, s_: s_ * 264.0 / 60.0   # (seconds to qn at quarter 264: every pair is in the Allegro, Tempo I)
    for q_, _, _ in _pairs23:
        _l1 = float(_os.environ.get("C23_LEAD1", str(_l23)))   # the first pair note's lead (the staccato before it rings under an early G)
        LEAD_SET_AT["Violins I"] = {**LEAD_SET_AT.get("Violins I", {}), str(q_): _l1, str(q_ + 0.5): _l23}
        # each pair note ends 0.03 s before the next moved note-on (the landing note keeps its own lead, 0.045 s)
        _land_on = q_ + 1.0 - _q23(0, 0.045)
        NOTE_END_AT = {**NOTE_END_AT, "Violins I": {**NOTE_END_AT.get("Violins I", {}),
                                                     q_: q_ + 0.5 - _q23(0, _l23) - _q23(0, 0.03),
                                                     q_ + 0.5: _land_on - _q23(0, 0.03)}}
if "cc1" in _f23:
    CC1_FLOOR_SPANS = {**CC1_FLOOR_SPANS, "Violins I": CC1_FLOOR_SPANS.get("Violins I", [])
                       + [(a_, b_, c_) for _, c_, (a_, b_) in _pairs23]}

# 2. Violins I staccato blur (critic A #2): the staccatissimo eighths (written 57 ms) end before their 81-98 ms peak and
#    ring on the 524 ms release (separation 4.0 dB median against 6.6 / 6.8 on Violins II / violas): the note-off after
#    the peak (0.10 s), with the 150 ms any_dyn cap on the three short rows in mix.json (never the cap alone: c21)
# (C23_STAC=1 with the cap, range test: separation 4.5 -> 5.8 dB (56-132) but 4.7 -> 1.2 (tutti 313-360), and the 60 ms
# peaks -48.9 -> -53.8 / -36.9 -> -56.9 dB: the cap still cut the peaks. Rejected; A #2 stays open)
if _os.environ.get("C23_STAC", "0") == "1":
    STAC_MIN_SOUND_S = {**STAC_MIN_SOUND_S, "Violins I": 0.10}

# 3b. Tutti accents land late (critic C #2): the accented half notes of bars 106 / 110 / 116 / 118 and 306 / 310 / 316 /
#    318 on "Sus MAX" (Oboe 1, cor anglais) and "Leg Slur Rep" (Clarinet 2) peak 0.2-0.4 s after the downbeat: the KS
#    Masters' accent rows (overlay layers read from the .oib: OB 1-74 / 75-114 / 115-127, EH 1-109 / 110-127, CL 1-60 /
#    61-96 / 97-116 / 117-127), velocity 90 as the flutes, no CC11 bump on that row; the 0.04 s ROW_CHANGE_ACC_ADD_S
#    (onsets 60-75 ms early, peaks unmoved) is dropped on these notes for these tracks and Violins I / II
_tq23 = [315.0, 327.0, 345.0, 351.0, 915.0, 927.0, 945.0, 951.0]
# (range test from the same starts: Oboe 1 first 100 ms against its neighbours -2.6 -> -0.3 dB median, first 100 ms
# against 150-350 ms -3.1 -> -1.8; cor anglais against the note before -3.0 -> -4.2, peak 0.28 -> 0.34 s; Clarinet 2
# -4.5 -> -6.8; the dropped 0.04 s on Violins I / II: Violins II's accents -4.0 -> -6.3, Violins I -1.6 -> -1.8.
# Adopted on Oboe 1 only, with no change to ROW_CHANGE_ACC_ADD_S; C23_WACC=all rebuilds the tested set)
_wacc23 = _os.environ.get("C23_WACC", "oboe")
if _wacc23 in ("oboe", "all"):
    for t_, row_ in (("Oboe 1", "Sus Accent MAX"), ("Cor anglais", "Sus Accent MAX"), ("Clarinet 2", "Sus Accent")):
        if _wacc23 == "oboe" and t_ != "Oboe 1":
            continue
        ART_AT[t_] = {**ART_AT.get(t_, {}), **{q_: row_ for q_ in _tq23}}
        VEL_SET[t_] = {**VEL_SET.get(t_, {}), **{q_: 90 for q_ in _tq23}}
        ACCENT_CC[t_] = {**ACCENT_CC.get(t_, ACCENT_CC.get("wind", {})),
                         "skip_rows": tuple(ACCENT_CC.get(t_, ACCENT_CC.get("wind", {})).get("skip_rows", ())) + (row_,)}
        # (the accent rows take no sustain lead of their own: 0.04 s, the flutes' total on this row, peaks +0..+126 ms)
        LEAD_SET_AT[t_] = {**LEAD_SET_AT.get(t_, {}), **{str(q_): 0.04 for q_ in _tq23}}
if _wacc23 == "all":
    ROW_CHANGE_ACC_SKIP = {"_all": list(ROW_CHANGE_ACC_SKIP) if not isinstance(ROW_CHANGE_ACC_SKIP, dict) else ROW_CHANGE_ACC_SKIP.get("_all", []),
                           **{t_: _tq23 for t_ in ("Violins I", "Violins II")}}

# 6. Flute 1's crescendos into the tuttis (critic C #3): CC11 rises 46 -> 94 over the first 4 qn of each 10 qn hairpin,
#    then only 94 -> 104 over the last 6 while the line falls 8 semitones (the stem flat or falling). max_arrival_cc 124
#    was the coordinator's route, but these two hairpin gains are not converted at all (no note sounds 0.25 s past
#    their release, so they stay in the envelope whatever the cap; parts.json unchanged): instead a linear CC11 rise to
#    124 over the last 6 qn (+0 at 904 / 304, +20 at the hairpin's stop), held to the A5's last 0.5 qn and gone before
#    the ff staccato's note-on (CC11 is global volume on the short rows, so the ff staccato must not take the lift)
if _os.environ.get("C23_FHP", "0") == "1":   # (c24: off, critic B #3)
    CC11_ADD_SPANS = {**CC11_ADD_SPANS, "Flute 1": CC11_ADD_SPANS.get("Flute 1", [])
                      + [x_ for b_ in (300.0, 900.0) for x_ in ((b_ + 4.0, b_ + 10.0, 0, 20), (b_ + 10.0, b_ + 11.3, 20, 20),
                                                              (b_ + 11.3, b_ + 11.75, 20, 0))]}

# 3c. Violins II accents (critic A #4): on "Sus MAX" they have no front and peak 0.21-0.26 s late; the 2nd Violins KS
#    Master's "Marc Lng RRx4" (manual p.93; read from the .oib: 6 ms attack, layers 1-89 / 90-127, 372-394 ms release,
#    3,760 regions) on the f / ff accents written up to a half note, velocity 80 at f, 100 at ff, no CC11 bump on that row
_mlng23 = [132.0, 144.0, 300.0, 302.0, 304.0, 306.0, 308.0, 310.0, 315.0, 327.0, 345.0, 351.0, 819.0, 899.0, 902.0, 904.0,
           906.0, 908.0, 910.0, 915.0, 927.0, 945.0, 951.0, 999.0, 1008.0, 1010.0, 1014.0]
# (range test 312-360: accents -4.0 -> -20.2 dB against their neighbours, the staccatos' 60 ms peaks -34.0 -> -54.3,
# separation 7.2 -> 0.0: the row change broke the following notes. Rejected)
if _os.environ.get("C23_MARCLNG", "0") == "1":
    ART_SPANS["Violins II"] = [{"from": q_ - 0.01, "to": q_ + 0.01, "art": "Marc Lng RRx4",
                                "vel_by_cc": [(88, 80), (98, 100)]} for q_ in _mlng23] + ART_SPANS.get("Violins II", [])
    ACCENT_CC["Violins II"] = {**ACCENT_CC.get("Violins II", ACCENT_CC["string"]),
                               "skip_rows": tuple(ACCENT_CC.get("Violins II", ACCENT_CC["string"]).get("skip_rows", ())) + ("Marc Lng RRx4",)}


# =====================================================================================================================
# c24 (2026-11-17): cycles/c24/CHANGES.md. Dan's rule (no per-note volume moves) checked by the fixed guard
# (cycles/c24/actor_scripts/guard24.py: the envelope REAPER gets, no exempt windows); lyrical phrase entries; theme A's
# pizzicato bass; Violins I staccato; Flute 1 into 105 / 305; bar 23. The generic envelope rate limit is mix.json
# "note_slew" (tools/build_reaper.py). Range-test switches (environment; defaults are the adopted values): C24_PS (phrase
# shape: "new" | "old"), C24_ORPH (Violins I orphan short-row groups: "off" | "cap" | "none"; mix.json is written by
# cycles/c24/actor_scripts/apply24.py), C24_SPIC (Violins I D5 / D sharp 5 / F sharp 5 staccatos on "Spiccato RRx9":
# 1 | 0), C24_F23 (bar 23 CC11 lift after the trough: 1 | 0), C24_FL (Flute 1 into 105 / 305: 1 | 0)
# =====================================================================================================================
# 1b. Dan's rule (critic B #1, #2): role edges moved to rests or ramps in build/roles.json (apply24.py); two rows become
#     CC11 (pre-hall) spans: celli [362, 396, -4] (an edge on the score onset of a legato target led 0.53 qn) and violas
#     [192, 198, 3.5] (its end inside the pp slur head led 0.26 qn); at CC11 32-48 about 0.45 dB per unit
CC11_ADD_SPANS = {**CC11_ADD_SPANS,
                  "Violoncellos": CC11_ADD_SPANS.get("Violoncellos", []) + [(361.45, 396.0, -9, -9)],
                  "Violas": CC11_ADD_SPANS.get("Violas", []) + [(191.4, 196.7, 8, 8)]}
#     the summit's arrival weight (2.5-4.5 dB steps inside the led notes of 22 tracks at 1005): full 5 ms before each
#     track's moved note-on, held to the arrival note's end, released over 0.5 qn after it
ARRIVAL_WEIGHT_MOVED = 0.5

# 2. Lyrical phrase entries (critic C #1, Dan's inner lines): 23 of 108 lyric / build phrases in the lyrical spans
#    entered 7-12 dB under their next three notes (the arch's -12 at the first onset, x1.4 on the winds: 28 CC11 units
#    inside the first note or two, with no printed hairpin). Gentler arch, no wind scale; builds enter at -6
if _os.environ.get("C24_PS", "new") == "new":
    PHRASE_SHAPE = {**PHRASE_SHAPE, "start": -4, "rise": [(0.4, 2), (0.8, 4)], "peak": (6, 0.45), "end": -8,
                    "family_scale": {"wind": 1.0},
                    "types": {**PHRASE_SHAPE["types"], "build_start": -6}}
#    the violas' p cresc line of bars 193-196 (critic B #4): its first note starts a slur from silence on "Leg Slur MAX"
#    (-59.7 dB, 6-14 dB under the celli / basses at the same p): "Sus MAX" on that note (loaded; the row of 579 / 585)
#    and CC11 +8 over the phrase
ART_AT["Violas"] = {**ART_AT.get("Violas", {}), 576.0: "Sus MAX"}
CC11_ADD_SPANS["Violas"] = CC11_ADD_SPANS["Violas"] + [(575.4, 588.0, 8, 8)]

# 4. Violins I staccato (critic A #1): the same-pitch eighth pairs on D5, D sharp 5 and F sharp 5 separate by 0.2-2.3 dB
#    on every short row (B4 / E5 / B5 5.4-6.4): those pitches on "Spiccato RRx9" (manual p.92; loaded, 9 rotating groups,
#    318 ms release)
if _os.environ.get("C24_SPIC", "1") == "1":
    STAC_ROW_BY_PITCH = {**STAC_ROW_BY_PITCH, "Violins I": [(74, 75, "Spiccato RRx9"), (78, 78, "Spiccato RRx9")]}

# 5. Flute 1 into bars 105 / 305 (critic B #3): the c23 CC11 ramp (C23_FHP) is off (its rise was lost under
#    CC11_REST_MAP, its return wrote a fall into the arrival); no envelope gain is held into the arrival; the crescendo
#    is carried by the velocity of the accented half notes ("Sus Accent MAX": velocity sets the attack, manual p.100)
if _os.environ.get("C24_FL", "1") == "1":
    CC11_ADD_SPANS["Flute 1"] = [r_ for r_ in CC11_ADD_SPANS.get("Flute 1", [])
                                 if not any(abs(r_[0] - (b_ + x_)) < 1e-6 for b_ in (300.0, 900.0) for x_ in (4.0, 10.0, 11.3))]
    HP_GAIN_TO_CC11 = {**HP_GAIN_TO_CC11, "Flute 1": {**HP_GAIN_TO_CC11.get("Flute 1", HP_GAIN_TO_CC11["wind"]),
                                                       "drop_always": [310.0, 910.0]}}
    VEL_SET["Flute 1"] = {**VEL_SET.get("Flute 1", {}), 300.0: 70, 302.0: 76, 304.0: 82, 306.0: 88, 308.0: 94, 310.0: 100,
                          902.0: 70, 904.0: 78, 906.0: 86, 908.0: 94, 910.0: 100}

# 6. Bar 23 (critic A #3): a CC11 lift from the trough after the F sharp to just after the A's moved note-on
if _os.environ.get("C24_F23", "1") == "1":
    CC11_ADD_SPANS["Violins I"] = CC11_ADD_SPANS.get("Violins I", []) + [(66.72, 67.12, 20, 20)]

# 7. Smaller items
#  - celli legato joins (critic A #4): velocity 112 (the faster transition, manual p.144) on the legato targets 6 or more
#    semitones from the note before that were softer (the leg_leads refit is deferred)
VEL_SET["Violoncellos"] = {**VEL_SET.get("Violoncellos", {}), **{q_: 112 for q_ in (
    196.0, 362.0, 364.0, 511.5, 576.0, 794.0, 797.0, 830.0, 832.0, 844.0, 1056.0)}}
#  - bar 58 swings +-2.9 dB from render to render on unchanged data (critic C #5): a round-robin reset in the celli's
#    rest before the fugato
RR_RESET_AT = {**RR_RESET_AT, "Violoncellos": sorted(set(RR_RESET_AT.get("Violoncellos", []) + [167.0]))}
#  - the trio climax ride row [645-659] -1.5 (critic C #6): its job is done by Flute 1's [648, 660, -4]
RIDE_TRIMS = [r_ for r_ in RIDE_TRIMS if r_ != [(645.0, 0.0), (647.0, -1.5), (656.0, -1.5), (659.0, 0.0)]]
#  - the celli's pp line under the solo violin, bars 349-352 (critic B #5): the harp's chords capped at velocity 45
VEL_CAP_SPANS["Harp"] = VEL_CAP_SPANS["Harp"] + [(1040.0, 1068.0, 45)]
#  - the trio tune's hot half-step joins (critic C #2a; finale technique 121's counter-shape): CC11 -8 from the join's
#    moved note-on, held 0.35 s, back by 0.8 s, at 516 and 526 (506 has its c17 -14 dip)
if _os.environ.get("C24_CEL", "1") == "1":
    CC11_ADD_SPANS["Violoncellos"] = CC11_ADD_SPANS["Violoncellos"] + [
        (515.22, 516.55, -8, -8), (516.55, 518.26, -8, 0), (524.97, 526.30, -8, -8), (526.30, 528.0, -8, 0)]

# ---------------------------------------------------------------------------------------------------------------------
# c25 (actor on the c24 render; cycles/c25/CHANGES.md). Switches: C25_SPIC (A / none), C25_AW (1 / 0), C25_HP (1 / 0)
# 1. Violins I Spiccato level (critics A #1, C #1): the rerouted D5 / D sharp 5 / F sharp 5 staccatos peaked +2.8..+3.3 dB
#    over their staccato neighbours (c18 -0.7..-1.2). The row's layers are v1-54 / 55-89 / 90-114 / 115-127 (load_oib):
#    the rerouted notes under 90 lose 13 velocity steps (vel_add, 4th value; 5th: only under 90), so they all play the
#    1-54 layer, which mix.json region_gain_db cuts 2 dB; the v95 tutti notes are cut 4 dB in the 90-114 / 115-127
#    regions (apply25.py B); no original Spiccato note plays in either cut layer
if _os.environ.get("C25_SPIC", "A") == "A":
    _va = int(_os.environ.get("C25_SPIC_VEL", "-13"))   # range tests P1 (-10: soft notes still +2.5..+2.9) and P2 (-13 + the 1-54 layer -2 dB: +1.3 / -0.1 / -0.9)
    STAC_ROW_BY_PITCH = {**STAC_ROW_BY_PITCH, "Violins I": [(74, 75, "Spiccato RRx9", _va, 90), (78, 78, "Spiccato RRx9", _va, 90)]}
# 2. Printed hairpins that start on a led note's score onset ramp from 20 ms before its moved note-on (critic B #4a)
if _os.environ.get("C25_HP", "1") == "1":
    HP_START_MOVED = 0.02
# 3. Summit (critic B #3): the arrival weight only where a printed rise leads into 1005 (not the trumpets, printed f with
#    no change, which stepped +5.7 dB over the fff woodwinds), held at most 1.5 qn; the rest +3.0 (was 2.5)
if _os.environ.get("C25_AW", "1") == "1":
    ARRIVAL_WEIGHT_RISE_ONLY = True
    ARRIVAL_WEIGHT_HOLD_CAP = 1.5
    ARRIVAL_WEIGHT_AT = {**ARRIVAL_WEIGHT_AT, 1005.0: (-2.0, 3.0, 1.0)}
#    and a hairpin's gain is held to the end of a note sounding across its hold's end, at most 3 qn (critic B #4d)
if _os.environ.get("C25_HP", "1") == "1":
    HP_HOLD_TO_NOTE_END = 3.0
# 4. Delivery (shared spec item 6, LRA 10.5 or more): the delivered LRA read 10.4; the fugato lifts of the delivery ride
#    (167.5-204 and 863.5-888, +2 dB) to +1.5 (tested on the c25 master: LRA 10.6, p10 -20.3, summit limiter 3.5 dB)
RIDE_TRIMS = [[(q_, 1.5 if abs(v_ - 2.0) < 1e-9 else v_) for q_, v_ in r_] if r_[0][0] in (167.5, 863.5) else r_ for r_ in RIDE_TRIMS]

# ---------------------------------------------------------------------------------------------------------------------
# c26 (actor on the c25 render; cycles/c26/CHANGES.md). Range-test switches (environment; defaults are the adopted
# values): C26_SLUR (woodwind slur ends before staccatos: 1 | 0), C26_OBV (Oboe 1 tutti staccato velocity: 1 | 0),
# C26_BODY (accent fronts: 1 | 0), C26_SUM (summit stroke on "Sus Marc LITE" + counter-shape: 1 | 0)
# 1. Dan's figure in the woodwinds (critic A #1): in both tutti statements the slurred eighth on the legato row rang over
#    the staccato quarter after it (old pitch louder 70 ms after the staccato's note-on). The slur end before a staccato
#    ends 35 ms before the staccato's moved note-on (new generic SLUR_END_BEFORE_STAC); release caps and f-layer trail
#    gain in mix.json (apply26.py)
_FIG_SPANS = [(312.0, 360.0), (912.0, 960.0)]
if _os.environ.get("C26_SLUR", "1") == "1":
    for _t in ("Flute 1", "Flute 2", "Oboe 1", "Clarinet 2"):
        SLUR_END_BEFORE_STAC[_t] = {"s": 0.035, "spans": _FIG_SPANS, "rows": ("Leg",), "min_qn": 0.15}
#    Oboe 1's staccato quarters there peaked 16 dB under the slurred eighth before (v100, middle layer 75-114 of
#    "Stac DblTng RRx9", load_oib): the top layer (115-127)
if _os.environ.get("C26_OBV", "1") == "1":
    VEL_SET["Oboe 1"] = {**VEL_SET["Oboe 1"], **{q_: 118 for b_ in (312.0, 912.0) for q_ in (b_ + 6, b_ + 18, b_ + 32, b_ + 36, b_ + 42)}}
# 5. Accent fronts (critic A #2): accents on the sustain rows peaked 0.23-0.27 s after the beat with the first 80 ms
#    2-3.6 dB under the body (the envelope accent bodies are gone under Dan's rule). The CC11 bump is up 0.06 s before
#    the moved note-on on the strings, and a CC11 body dip follows it (-8 units, -4 where the resting CC11 is under 60;
#    -6 on cor anglais, Clarinet 2 and Oboe 1's Sus MAX accents)
if _os.environ.get("C26_BODY", "1") == "1":
    for _t in ("Violins I", "Violins II", "Violas"):
        ACCENT_CC[_t] = {**ACCENT_CC.get(_t, ACCENT_CC["string"]), "lead_s": 0.06, "body_cc": -8, "body_soft": -4,
                         "body_s": (0.22, 0.36)}
    for _t in ("Cor anglais", "Clarinet 2", "Oboe 1"):
        ACCENT_CC[_t] = {**ACCENT_CC.get(_t, ACCENT_CC.get("wind", {})), "body_cc": -6, "body_s": (0.22, 0.36)}
# 4. Summit (critics B #2, C #1): the fff downbeat at 1005 lands at the crescendo's level and blooms 0.3-0.5 s later.
#    The stroke on "Sus Marc LITE" (marcato overlay over the sustain, manual p.91-92) on Violins I / II and violas
#    (finale technique 140: v92, lead 0.085 s: build/entry_leads.json +0.025 s on the 0.06 s lead, apply26.py), and a
#    CC11 counter-shape on the held notes after it (C #1)
if _os.environ.get("C26_SUM", "1") == "1":
    for _t in ("Violins I", "Violins II", "Violas"):
        ART_SPANS[_t] = [{"from": 1004.9, "to": 1005.1, "art": "Sus Marc LITE", "vel_by_cc": [(0, 92), (127, 92)]}] + ART_SPANS.get(_t, [])
        CC11_ADD_SPANS[_t] = CC11_ADD_SPANS.get(_t, []) + [(1005.35, 1006.0, 0, -10), (1006.0, 1007.3, -10, -10), (1007.3, 1007.5, -10, 0)]
# 6. The sfp < of bar 301 (critic C #2): the p lasted about 1 qn and the crescendo was 70 % done by 904; the crescendo
#    after an fp / sfp holds the p 1 qn and rises late (new generic HP_CURVE "cresc_after_fp"); the 902 stroke lift
#    +22 -> +12; the delivery ride lets the sf through (ends at 899.6 / 900.0)
HP_CURVE = {**HP_CURVE, "cresc_after_fp": {"pt": (0.6, 0.3), "hold_qn": 1.0}}
for _t in ("Violins II", "Violas", "Violoncellos"):
    if 902.0 in ACCENT_CC_AT.get(_t, {}):
        ACCENT_CC_AT[_t] = {**ACCENT_CC_AT[_t], 902.0: (12, 0.5)}
RIDE_TRIMS = [[(895.5, 0.0), (896.5, -2.0), (899.6, -2.0), (900.0, 0.0)] if r_ == [(895.5, 0), (896.5, -2), (900, -2), (901, 0)] else r_
              for r_ in RIDE_TRIMS]
# 7. Violins I's rerouted Spiccato notes (critic A #3): 17 notes at v67-87 landed in the uncut 55-89 layer after -13:
#    three rows per pitch range by original velocity, so every rerouted note under 90 plays the 1-54 layer
STAC_ROW_BY_PITCH = {**STAC_ROW_BY_PITCH, "Violins I": [
    (74, 75, "Spiccato RRx9", -13, 67), (74, 75, "Spiccato RRx9", -20, 80), (74, 75, "Spiccato RRx9", -33, 90),
    (78, 78, "Spiccato RRx9", -13, 67), (78, 78, "Spiccato RRx9", -20, 80), (78, 78, "Spiccato RRx9", -33, 90)]}
# 8. Flute 2's ff accent at bar 72 entered 11 dB low on the accent row at v90 (critic C #5b): v110 (the attack layer)
VEL_SET["Flute 2"] = {**VEL_SET.get("Flute 2", {}), 213.0: 110}
#    delivery (shared spec item 6): the first c26 delivery read LRA 10.4; the fugato ride lifts +1.5 -> +0.5 dB (tested
#    on the c26 master: LRA 10.5, summit lead +0.68 LU, limiter 3.6 dB; +1.0 gave 10.4)
RIDE_TRIMS = [[(q_, 0.5 if abs(v_ - 1.5) < 1e-9 else v_) for q_, v_ in r_] if r_[0][0] in (167.5, 863.5) else r_ for r_ in RIDE_TRIMS]

# ---------------------------------------------------------------------------------------------------------------------
# c27 (actor on the c26 render; cycles/c27/CHANGES.md). Range-test switches (environment; defaults are the adopted
# values): C27_MARC (Violins I soft-head marcato lift: 1 | 0), C27_ACC (accent timing / sizes: 1 | 0), C27_BODY (body
# dip earlier: 1 | 0), C27_VLA (violas' off-beat double stops v82: 1 | 0), C27_SLH (soft legato heads: 1 | 0),
# C27_RR (ritmo di tre battute resets: 1 | 0)
# 1. Arrival fades (critic B #1): a crescendo gain left in the envelope holds as a passage level until the next printed
#    change (decrescendo start, softer mark: released there; louder mark: shrinks by the CC11 rise; first rest; 8 qn,
#    then a rest within 4 qn or the slow release; B proposed 16: the trio climax celli held +5.4 dB for 13 qn);
#    mix.json cresc_trim_hold "release_at": "mark" (apply27.py) does the same for the held trim
HP_GAIN_TO_CC11 = {k_: ({**v_, "hold_until_mark_qn": 8.0, "hold_rest_extra_qn": 4.0} if isinstance(v_, dict) and v_.get("keep_rel_db_s") else v_)
                   for k_, v_ in HP_GAIN_TO_CC11.items()}
#    Horn 3's unison-boost span (critic B #4.1): edges in the rests before / after the run
UNI_BOOST_ROLE_IN_RESTS = True
# 2. Violins I's soft theme heads on "Sus Marc LITE" (critic A #1): the marcato spike is followed by a 7-13 dB hole at
#    0.21-0.39 s (the row's sustain sits 16+ dB under the marcato at CC11 44-80): CC11 +14 from 0.10 to 0.22 s after the
#    beat, held to the next note-on (generic ACCENT_CC "marc_lift"); the marcato's vel<66 layer -8 dB (apply27.py)
if _os.environ.get("C27_MARC", "1") == "1":
    ACCENT_CC["Violins I"] = {**ACCENT_CC["Violins I"],
                              "marc_lift": {"cc": int(_os.environ.get("C27_MARC_CC", "14")), "s": (0.10, 0.22),
                                            "rows": ("Sus Marc LITE",), "max_cc": 80, "vel_max": 70}}
# 3. Accent timing and sizes (critics C #1, A #2, A #3): the accents started 30-40 ms before the beat (c21's 0.04 s add,
#    c25's cor anglais +0.05 s, c26's bump lead) and peaked late: no ROW_CHANGE_ACC_ADD_S on Violins I (the cor anglais
#    +0.05 s is undone in entry_leads.json, apply27.py); Clarinet 2's tutti accents got no bump (CC11 104 over loud_cc
#    98, add_loud 0): add_loud 8, lead_s 0.06; the violas' accents +4.5 dB over their neighbours: add_loud 20 -> 14
if _os.environ.get("C27_ACC", "1") == "1":
    ROW_CHANGE_ACC_ADD_S = {k_: v_ for k_, v_ in ROW_CHANGE_ACC_ADD_S.items() if k_ != "Violins I"}
    ACCENT_CC["Clarinet 2"] = {**ACCENT_CC["Clarinet 2"], "add_loud": 8, "lead_s": 0.06}
    ACCENT_CC["Violas"] = {**ACCENT_CC["Violas"], "add_loud": 14}
# 4. Tutti downbeats (critic C #2): the accent body dip is full before beat 2 (0.227 s at quarter 264)
if _os.environ.get("C27_BODY", "1") == "1":
    for _t in ("Violins I", "Violins II", "Violas", "Cor anglais", "Clarinet 2", "Oboe 1"):
        ACCENT_CC[_t] = {**ACCENT_CC[_t], "body_s": (0.14, 0.24)}
#    the violas' off-beat "non div." staccatissimo double stops of the tuttis (v95, +4 dB role for their slurred pairs)
#    stood 2.8 dB over the basses' downbeat: v82 (range-tested: velocity picks the layer on HS short rows)
_VLA_OFF = [_b + _k * 3 + _o for _b in (312.0, 912.0) for _k in range(16) for _o in (1.0, 2.0)
            if _b + _k * 3 + _o not in (317.0, 329.0, 353.0, 917.0, 929.0, 953.0)]   # not the slurred pairs (Sus MAX)
if _os.environ.get("C27_VLA", "1") == "1":
    VEL_SET["Violas"] = {**VEL_SET.get("Violas", {}), **{_q: int(_os.environ.get("C27_VLA_V", "82")) for _q in _VLA_OFF}}
# 5. Soft legato string heads in the trio and Meno mosso reach -6 dB 150-330 ms after the beat (critic C #3; finale
#    technique 139): CC11 +10 from 0.06 s before the moved note-on to +0.25 s, gone by +0.45 s (generic SOFT_LEG_HEAD_CC)
if _os.environ.get("C27_SLH", "1") == "1":
    SOFT_LEG_HEAD_CC = {"string": {"rows": ("Leg",), "max_cc": 70, "rest_qn": 0.5, "add": 10, "pre_s": 0.06,
                                   "hold_s": 0.25, "gone_s": 0.45, "spans": [(456.0, 720.0), (1020.0, 1128.0)]},
                        "Violoncellos": {"rows": ("Leg",), "max_cc": 70, "rest_qn": 0.5, "add": 10, "pre_s": 0.06,
                                         "hold_s": 0.25, "gone_s": 0.45, "spans": [(456.0, 720.0), (1020.0, 1128.0)],
                                         "skip": [564.0]}}   # range test: 564 (CC11 46, not late: -6 dB at +127 ms) rose 5.1 dB
# 6. Smaller: the ritmo di tre battute resets put the softest pizzicato on every group head (critic C #4). Range test
#    (rangetest P0 / P1): the celli's round robins after a reset play -48.4 / -45.8 / -49.9 dB (second sample the
#    loudest); a reset one bar before each head puts heads 273 / 282 / 291 on it. Basses: C's resets [264, 270, 279, 288]
#    left the heads -49.1 / -49.0 / -48.6 (were -48.7 / -48.6 / -47.3): unchanged
if _os.environ.get("C27_RR", "1") == "1":
    RR_RESET_AT = {**RR_RESET_AT,
                   "Violoncellos": sorted(set(x_ for x_ in RR_RESET_AT["Violoncellos"] if x_ not in (273.0, 282.0, 291.0)) | {270.0, 279.0, 288.0})}
#    Flute 2's slur end 35 -> 20 ms (critic C) was range-tested and not adopted: Dan's figure A median +13.1 -> +11.6,
#    notes under +3 1 -> 2 (the c26 woodwind state stays, critic A)

# ---------------------------------------------------------------------------------------------------------------------
# c28 (actor on the c27 render; cycles/c28/CHANGES.md). JSON edits: cycles/c28/actor_scripts/apply28.py (roles.json,
# mix.json). Range-test switches (environment; defaults are the adopted values): C28_SPIC (Violins I pitch reroute only
# for pairs: 1 | 0), C28_TEN (tutti tenuto quarters on short rows: 1 | 0), C28_ACC (accent body / sizes: 1 | 0), C28_TIMP
# (hard sticks: 1 | 0), C28_V1E (soft heads' eighths: "a" overlap + v62 | "0" as c27)
# 1. Dan's figure at bars 110 / 310 (critic A #1): the pitch reroute to "Spiccato RRx9" only for the halves of same-pitch
#    staccato pairs (new generic STAC_ROW_BY_PITCH_REP_ONLY); the 32 single notes go back to their c18 rows and
#    velocities (the vel_add rows key on the reroute)
if _os.environ.get("C28_SPIC", "1") == "1":
    STAC_ROW_BY_PITCH_REP_ONLY = {"Violins I": True}
# 2. Arrival sags (critic B #1, #2; Dan's rule): a kept crescendo gain holds to a printed decrescendo within 32 qn when the
#    cap passes with no printed change, only a rest of 2 qn or more ends a hold early, short arrival notes are held too
#    (they skipped _keep()), and the 300-310 / 900-910 crescendos into the ff tuttis drop their gain on the woodwinds and
#    strings (B #2c: they rise on CC11 and the brass entries; with the 2 qn rest rule their hold would lift the whole
#    tutti; "drop_always", since drop_ends keeps an unchained wind gain); brass unchanged (not in B's sag list); mix.json
#    cresc_trim_hold the same (apply28.py)
HP_GAIN_TO_CC11 = {k_: ({**v_, "hold_to_dec_qn": 32.0, "hold_rest_min_qn": 2.0, "keep_short_arrivals": True}
                        if isinstance(v_, dict) and v_.get("keep_rel_db_s") else v_) for k_, v_ in HP_GAIN_TO_CC11.items()}
HP_GAIN_TO_CC11 = {k_: ({**v_, "drop_always": sorted(set(v_.get("drop_always", [])) | {309.0, 310.0, 909.0, 910.0})}
                        if isinstance(v_, dict) and k_ != "brass" else v_) for k_, v_ in HP_GAIN_TO_CC11.items()}
# 3. Summit (critic B #3; Dan's rule): the single-note arrival weight at 1005 (+3 dB on 15 tracks for 1.5 qn, then a step
#    back) is replaced by a passage level [1005, 1017, +2.5] in roles.json (apply28.py)
ARRIVAL_WEIGHT_AT = {k_: v_ for k_, v_ in ARRIVAL_WEIGHT_AT.items() if abs(k_ - 1005.0) > 1e-6}
# 4. Tutti downbeats (critics C #1, A #3): the tenuto quarters of the bass group in the ff tuttis play "Sus MAX" and peak
#    95-172 ms after the beat (the quarter lasts 227 ms): basses "Marc Lng RRx4" (manual p.93), trombones, bass trombone
#    and tuba "Portato" (p.101: full length, not tied, not staccato), by an ART_SPANS "tenuto" mark filter (new)
#    Range test (cycles/c28/records/range_P0.txt / range_P1.txt, 312-360): no row was faster or heavier. Basses on Marc Lng:
#    peak +175 -> +155 ms, -6 dB point -15 -> +65 ms, downbeat over beats 2-3 +1.5 -> +0.3 dB; tuba on Portato: peak +165
#    -> +188 ms, downbeat +2.8 -> -0.2 dB; trombones / bass trombone on Portato 5.4-6.6 dB softer and 15-20 ms later.
#    Not adopted (C28_TEN=1 brings it back for a test)
if _os.environ.get("C28_TEN", "0") == "1":
    for _t, _r in (("Double basses", "Marc Lng RRx4"), ("Tuba", "Portato"), ("Bass trombone", "Portato"),
                   ("Trombone 1", "Portato"), ("Trombone 2", "Portato")):
        ART_SPANS[_t] = [{"from": _a, "to": _b, "art": _r, "mark": "tenuto"} for _a, _b in ((311.9, 360.0), (911.9, 960.0))] \
            + ART_SPANS.get(_t, [])
#    the accent body dip back to c26's (0.22, 0.36) (c27's earlier dip landed on the attack's bloom), Violins II's bump
#    6 -> 10 and Violins I's 12 -> 14 (critic A #3)
#    Range test: Violins II's accents peak 0.279 -> 0.184 s, first 100 ms over the neighbours -1.2 -> -0.5 dB; Violins I
#    -6 dB point +33 -> +1 ms (no accent over +3 dB: 1 -> 0); the cor anglais peaked later (0.151 -> 0.249 s): the earlier
#    dip stays on the woodwinds (and on the violas, not measured)
if _os.environ.get("C28_ACC", "1") == "1":
    for _t in ("Violins I", "Violins II"):
        ACCENT_CC[_t] = {**ACCENT_CC[_t], "body_s": (0.22, 0.36)}
    ACCENT_CC["Violins II"] = {**ACCENT_CC["Violins II"], "add_loud": 10}
    ACCENT_CC["Violins I"] = {**ACCENT_CC["Violins I"], "add_loud": 14}
# 5. Timpani hard sticks (critic C #2, MANUAL-GAPS #6): the score prints "hard sticks" at bar 1; one instance cannot
#    change patches mid-movement, so the track plays "Timpani Hrd KS" throughout (the six "soft sticks" strokes of
#    341-376 are pp / ppp near the rim); the felt rows' names map to the hard rows (KS_ALIASES in score_to_parts.py)
if _os.environ.get("C28_TIMP", "1") == "1":
    TRACKS = [(n_, s_, p_.replace("Timpani Flt KS.oib", "Timpani Hrd KS.oib"), f_, pan_) for n_, s_, p_, f_, pan_ in TRACKS]
# 7. Violins I's soft heads' slurred eighths (critic A #2): 0.02 qn apart with an f-layer marcato on each (a 14.6 dB
#    trough, two detached strokes): variant a) both at v62 (the 1-65 marcato layer, cut 6 dB in mix.json). The 0.02 qn
#    overlap (NOTE_END_AT q+2 = q+2.124) was written but is clipped to the next moved onset - 0.02 qn, so the range test
#    ran v62 alone: eighth 1's 2-5 kHz front over the staccato before +6.8 -> +1.0 dB, its level -3.1 dB, the trough
#    relative to the eighth unchanged (-0.8 dB), landing +0.3 -> +0.4, bar 23 figure within 0.7 dB
_SR28 = (41.0, 53.0, 71.0, 77.0, 287.0, 761.0, 773.0, 791.0, 797.0)
if _os.environ.get("C28_V1E", "a") == "a":
    VEL_SET["Violins I"] = {**VEL_SET["Violins I"], **{q_ + h_: 62 for q_ in _SR28 for h_ in (0.0, 0.5)}}
# 8. Delivery (finale c29 note via the coordinator: a ride row that steps down at a crescendo's ff arrival reverses the
#    arrival on the mp3): the -1.0 row of the 305 tutti starts after bar 305 (911.0 -> 914.6), and the rows that cut
#    bars 104 / 304 (the crescendos' last bars) end before them. Tested on the c28 master (one render, two deliveries):
#    arrival 305 -0.4 (c27) / +0.4 -> +0.4, bar 304 -9.8 -> -9.5, f -> ff 1.77 -> 1.88 LU, LRA 10.8 -> 10.9, limiter 3.7 / 3.8
def _ride28(r_):
    if r_[0][0] == 911.0:
        return [(914.6, 0.0), (915.0, -1.0), (959.0, -1.0), (961.0, 0.0)]
    if r_[0][0] == 299.6:
        return [(299.6, 0.0), (300.0, -1.5), (308.6, -1.5), (309.0, 0.0)]
    if r_[0][0] == 894.0:
        return [(894.0, 0.0), (897.0, -0.5), (900.0, -0.5), (908.6, -0.5), (909.0, 0.0)]
    return r_
RIDE_TRIMS = [_ride28(r_) for r_ in RIDE_TRIMS]

# ---------------------------------------------------------------------------------------------------------------------
# c29 (actor on the c28 render; cycles/c29/CHANGES.md). JSON edits: cycles/c29/actor_scripts/apply29.py (roles.json,
# mix.json, lead_set.json). Range-test switches (environment; defaults are the adopted values): C29_TIMP (soft-stick
# alias in pass 2: 1 | 0), C29_VCH (celli countermelody heads on Sus MAX: 1 | 0), C29_TEN_END (tutti tenutos end at
# q + 0.85: 1 | 0), C29_TEN_ACC (brass / horn tenutos on "Sus Accent MAX" at this velocity: 0 = off), C29_BMARC (basses'
# tenutos on "Marc Sus LITE" at this velocity: 0 = off), C29_VLA_V (violas' tutti off-beat double stops, c27's v82)
# 3. Timpani sticks (critics A #1, C #3): the score prints "soft sticks" at bar 146 (qn 435) and 341 (1020) and "medium
#    sticks" at bar 225 (672); since c28 every stroke and roll played Timpani Hrd KS (trio pp strokes 14-19 dB brighter in
#    1-5 kHz than felt). The soft and medium spans play a felt alias "Timpani soft" in the second render pass (one more
#    Opus instance outside the main project's 45 GB). Medium (672-864) on felt: the 1-5 kHz share of its strokes was
#    -27.8 dB on felt (c18) and -18.4 on hard (c28) against A's half-way target -24, so felt is the nearer one (no range
#    test: both values come from full renders). The felt-fitted timpani tables carry over (MANUAL-GAPS #6); TRACK_WINDOWS
#    rests the main track there. The windows start and end in rests (444 is the first stroke after 435; the 858 stroke
#    ends at 861.5; 1014 ends at 1014.5)
_TW29 = [(435.0, 864.0), (1020.0, 1128.0)]
if _os.environ.get("C29_TIMP", "1") == "1":
    ALIAS_TRACKS = {**ALIAS_TRACKS, "Timpani soft": {"source": "Timpani", "windows": _TW29,
                                                     "patch": next(t_[2] for t_ in TRACKS if t_[0] == "Timpani").replace("Timpani Hrd KS.oib", "Timpani Flt KS.oib")}}
    PASS2_TRACKS = tuple(PASS2_TRACKS) + ("Timpani soft",)
    TRACK_WINDOWS = {**TRACK_WINDOWS, "Timpani": (_TW29, False)}
# 5. The celli's tenor countermelody heads at 312 / 912 (critic B #2): the espress. G3 starts a new slur after the
#    accented unslurred B2 but played as a "Leg Slur MAX" transition out of it, led 0.31 s (lead_set.json, removed in
#    apply29.py): a plain Sus MAX head with the ordinary entry lead
if _os.environ.get("C29_VCH", "1") == "1":
    ART_SPANS["Violoncellos"] = [{"from": 311.99, "to": 312.01, "art": "Sus MAX"},
                                 {"from": 911.99, "to": 912.01, "art": "Sus MAX"}] + ART_SPANS.get("Violoncellos", [])
    #    the head follows the B2's written end with no rest, so no lead branch moved it (0 lead): a 0.06 s re-attack lead
    #    (the string entry lead); the B2 then ends 0.02 qn before it
    REATTACK_LEAD_AT["Violoncellos"] = {**REATTACK_LEAD_AT.get("Violoncellos", {}), 312.0: 0.06, 912.0: 0.06}
# 6. Tutti tenuto downbeats (critics A #2, B #4): (a) the tenuto quarters of the low group end at q + 0.85 (34 ms before
#    beat 2; the KS release then falls in the rest) - each qualifying note's next onset is 3 qn away; (b) brass / horns
#    on "Sus Accent MAX" (manual p.100: velocity sets the attack's loudness, CC1 the sustain); (c) basses on "Marc Sus
#    LITE" (p.100: velocity opens the marcato's low-pass); violas' off-beat shorts (c27 v82, B #4)
_TEN29 = {"Trombone 1": (312.0,), "Trombone 2": (312.0,), "Bass trombone": (312.0,), "Tuba": (312.0,),
          "Horn 1": (312.0, 912.0), "Horn 2": (312.0, 912.0), "Contrabassoon": (312.0, 912.0),
          "Double basses": (312.0, 912.0)}
if _os.environ.get("C29_TEN_END", "1") == "1":
    for _t, _bs in _TEN29.items():
        NOTE_END_AT[_t] = {**NOTE_END_AT.get(_t, {}),
                           **{_b + 3.0 * _k: _b + 3.0 * _k + 0.85 for _b in _bs for _k in range(16)
                              if not (_t == "Bass trombone" and _b + 3.0 * _k == 354.0)}}
_TACC29 = int(_os.environ.get("C29_TEN_ACC", "0"))
if _TACC29:
    for _t in ("Trombone 1", "Trombone 2", "Bass trombone", "Tuba", "Horn 1", "Horn 2"):
        ART_SPANS[_t] = [{"from": _b - 0.1, "to": _b + 48.0, "art": "Sus Accent MAX", "mark": "tenuto"} for _b in _TEN29[_t]] \
            + ART_SPANS.get(_t, [])
        VEL_SET[_t] = {**VEL_SET.get(_t, {}), **{_b + 3.0 * _k: _TACC29 for _b in _TEN29[_t] for _k in range(16)}}
_BM29 = int(_os.environ.get("C29_BMARC", "0"))
if _BM29:
    ART_SPANS["Double basses"] = [{"from": _b - 0.1, "to": _b + 48.0, "art": "Marc Sus LITE", "mark": "tenuto"}
                                  for _b in (312.0, 912.0)] + ART_SPANS.get("Double basses", [])
    VEL_SET["Double basses"] = {**VEL_SET.get("Double basses", {}), **{_b + 3.0 * _k: _BM29 for _b in (312.0, 912.0) for _k in range(16)}}
#    Range test 312-360 (cycles/c29/records/range_P0/P1/P2.txt, same start 155.4): (a) tenuto group downbeat over beats 2-3
#    +2.0 -> +3.9 dB, master +0.1 -> +0.5, shapes unchanged, levels -0.3..-0.8 dB: adopted. (b) "Sus Accent MAX" v70 on
#    the brass / horns: peaks +165 -> +185..+195 ms, -6 dB point +25 -> +55..+90 ms, 2-5 kHz front-body -4.5 -> -12.3 dB
#    (a darker, later swell), group downbeat +0.5: rejected. (c) basses "Marc Sus LITE" v80: peak +128 -> +180 ms, +4.1 dB
#    level: rejected. Violas v88: off-beat shorts +0.5 dB (no layer step); v92: +5.3 dB, 1 dB over the basses' downbeat
#    (B's own gate): both rejected, c27's v82 kept
VEL_SET["Violas"] = {**VEL_SET["Violas"], **{_q: int(_os.environ.get("C29_VLA_V", "82")) for _q in _VLA_OFF}}
# 1. Delivery f -> ff (critic B #3b): the coda ride row before the fff deepens (the arrival itself untouched); with
#    deliver_master.py TOP_ABOVE -3 it gives the summit lead back (B's simulation 0.58 -> 0.74)
RIDE_TRIMS = [([(990.0, 0.0), (993.0, -2.0), (996.0, -4.0), (1002.0, -5.0), (1004.6, -5.5), (1005.1, 0.0)]
               if r_ == [(990.0, 0.0), (993.0, -2.0), (996.0, -4.0), (1004.6, -4.5), (1005.1, 0.0)] else r_) for r_ in RIDE_TRIMS]
assert any(r_[3] == (1002.0, -5.0) for r_ in RIDE_TRIMS if len(r_) > 3), "c29: coda ride row not found"

# ---------------------------------------------------------------------------------------------------------------------
# c30 (actor on the c29 render; cycles/c30/CHANGES.md). JSON edits: cycles/c30/actor_scripts/apply30.py (roles.json:
# summit string edges 1004.75 -> 1005, celli countermelody roles from 312 / 912, Horn 1's one-note row deleted, the
# 205-208 roll's role release; mix.json: Horn 3 E4 region gain). Switches (environment; defaults are the adopted values):
# C30_UNI (1 | 0), C30_ROLL (1 | 0), C30_TVEL (1 | 0), C30_BRASS (1 | 0), C30_FUG (1 | 0)
# 1. Summit stroke (critic A #1): the 1004.75 edges moved to 1005 (apply30.py); Violins II's and the violas' rows chain
#    there (-5 -> +0.5, +1 -> +4), and chained crossfades were not pinned by ROLE_EDGE_MOVED: pinned at 1005
ROLE_EDGE_MOVED_CHAINED_AT = (1005.0,)
# 2. Horn 3 (critic B #2): its 312-358 unison-boost run was three role spans (+3.01, +4.77 on the three-player E4 at
#    350-353, +3.01) whose rest-placed edges overlapped and summed inside the notes (+4.8 dB swells at 349.7 and 352.7):
#    adjacent runs merge whatever their boost (the run takes the boost its notes hold longest). (B's inferred cause, the
#    breath at 348, was not it: the runs met with no gap. UNI_RUN_GAP_QN 3.0 was tried and left at 1.0: it changed
#    nothing on Horn 3 but merged Oboe 1's 120-128.5 / 816-824.5 runs across rests and filled the boost into them)
if _os.environ.get("C30_UNI", "1") == "1":
    UNI_RUN_MERGE_VALUES = True
    UNI_RUN_GAP_QN = float(_os.environ.get("C30_UNI_GAP", "1.0"))
# 3. Celli countermelody head (critic A #2): the ff B2 before the head ends at 311.5 / 911.5 (a bow lift of about 54 ms
#    before the leap), so the +4.5 role step from 312 / 912 (apply30.py) lands in a rest the guard accepts
NOTE_END_AT["Violoncellos"] = {**NOTE_END_AT.get("Violoncellos", {}), 310.0: 311.5, 910.0: 911.5}
# 4. Close (critic C #2; Dan's rule): Horn 1's last G sharp loses its one-note +6 dB fader row (apply30.py); CC11 +20
#    instead of +14 (range test H1b, c17: 0.22 dB per unit at CC11 about 35; Movement I c59: 0.55-0.61 at 46-58)
CC11_ADD_SPANS["Horn 1"] = [((1100.7, 1128.0, 20, 20) if r_ == (1100.7, 1128.0, 14, 14) else r_) for r_ in CC11_ADD_SPANS["Horn 1"]]
assert (1100.7, 1128.0, 20, 20) in CC11_ADD_SPANS["Horn 1"], "c30: Horn 1 CC11 row not found"
# 5. Delivery (critic C #1; deliver_master.py MOM_CAP_ABOVE 3 -> 0): exposed p / pp solos came out at the f level on
#    the mp3; ride rows for the horn call, the violin solo and Hn 1's tail, the close; the 305-320 row -1.0 -> -1.5 keeps
#    the summit lead (C simulated all six spec items passing, p10 -21.1)
RIDE_TRIMS = [([(914.6, 0.0), (915.0, -1.5), (959.0, -1.5), (961.0, 0.0)]
               if r_ == [(914.6, 0.0), (915.0, -1.0), (959.0, -1.0), (961.0, 0.0)] else r_) for r_ in RIDE_TRIMS]
assert [(914.6, 0.0), (915.0, -1.5), (959.0, -1.5), (961.0, 0.0)] in RIDE_TRIMS, "c30: 305-320 ride row not found"
_RIDE30 = {"call": [(5.0, 0.0), (6.0, -2.0), (16.5, -2.0), (18.0, 0.0)],
           "solo": [(1043.0, 0.0), (1044.0, -2.0), (1079.0, -2.0), (1080.0, 0.0)],
           "close": [(1088.0, 0.0), (1092.0, -1.0), (1100.0, -2.5), (1128.0, -2.5)]}
for _k in _os.environ.get("C30_RIDES", "call,solo,close").split(","):
    if _k:
        RIDE_TRIMS = RIDE_TRIMS + [_RIDE30[_k]]
# 6a. Reprise fugato subject (critic B #3): the celli's slurred held notes at 866.4-870 sit 9 CC11 under their p twin at
#     170.4-174 (the source of the lower baseline not traced): one span matching the phrase to its twin
if _os.environ.get("C30_FUG", "1") == "1":
    CC11_ADD_SPANS["Violoncellos"] = CC11_ADD_SPANS["Violoncellos"] + [(866.3, 870.0, 9, 9)]
# 6b. The pp < f roll of bars 205-208 (critic C #3): the role and the LEVEL_SHAPES row release over 618-621 instead of in
#     0.5-1 qn at the hairpin's start, and the roll trim holds under the crescendo as on every other crescendo roll
if _os.environ.get("C30_ROLL", "1") == "1":
    LEVEL_SHAPES["Timpani"] = [([(612.5, 0.0), (617.5, -3.0), (618.0, -3.0), (621.0, 0.0)]
                                if r_ == [(612.5, 0.0), (617.5, -3.0), (618.5, 0.0)] else r_) for r_ in LEVEL_SHAPES["Timpani"]]
    assert [(612.5, 0.0), (617.5, -3.0), (618.0, -3.0), (621.0, 0.0)] in LEVEL_SHAPES["Timpani"], "c30: roll row not found"
    TIMP_ROLL_TRIM_HOLD_SKIP = [q_ for q_ in TIMP_ROLL_TRIM_HOLD_SKIP if abs(q_ - 618.0) > 1e-6]
# 6c. Coda ppp strokes "near the rim" (critic A #5; manual p.123: velocity sets the felt dynamics): under the pp strokes
if _os.environ.get("C30_TVEL", "1") == "1":
    #     (TIMP_RH_ALT lh_vel_add +10 lifts the alternating LH strokes 1110 / 1111.5 after VEL_SET: 40 plays 50)
    VEL_SET["Timpani"] = {**VEL_SET["Timpani"], 1110.0: 40, 1111.5: 40, 1111.0: 44, 1112.0: 44, 1122.0: 44}
# 6d. Brass at the 101-104 arrival (critic B #4): the 309 / 310 crescendo gains dropped on trumpets, trombones and tuba
#     as on the winds and strings in c28 (the horns keep theirs)
if _os.environ.get("C30_BRASS", "1") == "1":
    for _t in ("Trumpet 1", "Trumpet 2", "Trombone 1", "Trombone 2", "Bass trombone", "Tuba"):
        _b = HP_GAIN_TO_CC11.get(_t, HP_GAIN_TO_CC11["brass"])
        HP_GAIN_TO_CC11 = {**HP_GAIN_TO_CC11, _t: {**_b, "drop_always": sorted(set(_b.get("drop_always", [])) | {309.0, 310.0})}}
# 0. Dan's note on the c29 mp3 (2026-11-18 21:15Z): "in mov 3 at 39 seconds in the recording the strings overlapping slur
#    together really bad something went wrong". 0:36-0:39 is bars 52-55 (qn 154-165): the strings' slurred descent C (158,
#    a quarter) - B (159, half) - A - G, after the eighths of bar 53. The B is a "Leg Slur MAX" target led about 0.22 s
#    (0.96 qn at quarter 264), so its transition starts 0.04 qn after the C's own note-on and the C is never heard as its
#    own note, and the B's pitch still arrives late (pcx, c29: Violins I +107 ms, celli +80); the celli's E at 154 (a new
#    slur, joined legato from the F sharp) arrives +252 ms late, the violas' D at 162 +105 ms. Reprise (bars 284-287, qn
#    850-859): celli 850 +133 ms, violas 850 +154, Violins II 855 +108. The same data since c16 (lead_set refit) and c18.
#    These notes start as fresh "Sus MAX" heads with the string re-attack lead (0.06 s), as the celli head at 312 (c29)
_DAN30 = {"Violins I": (159.0, 855.0), "Violins II": (159.0, 855.0), "Violoncellos": (154.0, 159.0, 850.0, 855.0),
          "Violas": (162.0,)}   # (violas 850 dropped: it re-timed the tenuto G repeats at 852-853)
#    Range test (cycles/c30/records/dan_P0.txt / dan_P1.txt, same starts 153.6 / 851.2 / 849.4): the C -> B crossover
#    -316 ms (the B's band over the C's from before the C's own onset) -> +4..+68 ms, so the C sounds as a quarter; the
#    heads' perceived attack (pcx pc) with the 0.06 s lead: V1 / V2 / Vc 159 +78 / +91 / +61 ms, 855 +111 / +134 / +143,
#    Vc 154 +32, Vla 162 +41: each head's lead is raised by its pc beyond +20 ms (a lead moves the same attack earlier)
_LEAD30 = {("Violins I", 159.0): 0.12, ("Violins II", 159.0): 0.13, ("Violoncellos", 159.0): 0.10,
           ("Violas", 162.0): 0.08, ("Violins I", 855.0): 0.15, ("Violins II", 855.0): 0.17, ("Violoncellos", 855.0): 0.18}
if _os.environ.get("C30_DAN", "1") == "1":
    for _t, _qs in _DAN30.items():
        ART_SPANS[_t] = [{"from": _q - 0.01, "to": _q + 0.01, "art": "Sus MAX"} for _q in _qs] + ART_SPANS.get(_t, [])
        REATTACK_LEAD_AT[_t] = {**REATTACK_LEAD_AT.get(_t, {}), **{_q: _LEAD30.get((_t, _q), 0.06) for _q in _qs}}
        # the c16 lead_set refit leads (Violins I 159 0.255 s, celli 154 0.18 / 159 0.135) would override the head's lead
        LEAD_SET_AT[_t] = {k_: v_ for k_, v_ in LEAD_SET_AT.get(_t, {}).items() if not any(abs(float(k_) - _q) < 0.02 for _q in _qs)}
# 5b. (after the render) the summit lead read +0.46 LU on the mp3, the rival now bar 335: the strings' summit stroke led
#     to 1004.592 lands in bar 335 with its full front (item 1). The coda ride row's last points -5.0 / -5.5 -> -6.0 / -6.5
#     (simulated on the c30 master: lead +0.56, f -> ff 2.07, LRA 11.8, limiter 4.2 dB; one render, two deliveries)
RIDE_TRIMS = [([(990.0, 0.0), (993.0, -2.0), (996.0, -4.0), (1002.0, -6.0), (1004.6, -6.5), (1005.1, 0.0)]
               if r_ == [(990.0, 0.0), (993.0, -2.0), (996.0, -4.0), (1002.0, -5.0), (1004.6, -5.5), (1005.1, 0.0)] else r_) for r_ in RIDE_TRIMS]
assert [(990.0, 0.0), (993.0, -2.0), (996.0, -4.0), (1002.0, -6.0), (1004.6, -6.5), (1005.1, 0.0)] in RIDE_TRIMS, "c30: coda row"
