"""Movement I (mvt1/v221) score config for score_to_parts.py. Run in score_to_parts.py's namespace: S, W, B, H, P (patch
folders), DYN and every default table are available. Per-onset tables start empty (cycle 0); the loop's actors add to
them. Score qn: bars are 4/4 throughout, bar b starts at qn 4 (b - 1); the last release is qn 728 (bar 182)."""
SCORE_END = 728.0
SCORE_TITLE = "mvt1-mockup"

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
    ("Trumpet 3", ["Tpt3"], B + "Solo Trumpet/06 Keyswitch/1TP KS Master.oib", "brass", 0.15),
    ("Trombone 1", ["Tbn1"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.35),
    ("Trombone 2", ["Tbn2"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.4),
    ("Bass trombone", ["BTbn"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.45),
    ("Tuba", ["Tuba"], B + "Solo Tuba/06 Keyswitch/1TU KS Master.oib", "brass", 0.5),
    ("Timpani", ["Timp"], P + "Drums/Timpani/Timpani Flt KS.oib", "timp", 0.0),
    # player 1: tam-tam (bars 122-126 fff heavy beater; bar 175 pp soft stick) and the crash cymbals (bar 160 fff);
    # player 2: suspended cymbal roll pp < into the crash (bar 159). One patch each.
    ("Tam-tam", ["Perc"], P + "Cymbals/Cymbal Pairs/32in Med Tam Tam.oib", "perc", 0.1),
    ("Suspended cymbal", ["Perc"], P + "Cymbals/Sus Cymbal/18in Zildjian Sus Cymbal Cres.oib", "perc", 0.2),
    # c05 (critic C #1): the 19in A Crash (Long samples 6.2-8.8 s) was gone under the fff tutti within about a second; the
    # 22in K Crash (Long 9.4 s, key 60 Long RRx1-3 read from its region map, 62/64 Short, same as the 19in) rings longer
    ("Crash cymbals", ["Perc"], P + "Cymbals/Cymbal Pairs/22in Zildjian K Crash.oib", "perc", 0.15),
    ("Harp", ["HarpR", "HarpL"], H + "01 Maestro Patches/Harp Sus RR.oib", "harp", -0.55),
    ("Violins I", ["VlnI"], S + "1st Violins/06 Keyswitch/1st Violins KS Master.oib", "string", -0.6),
    ("Violins II", ["VlnII"], S + "2nd Violins/06 Keyswitch/2nd Violins KS Master.oib", "string", -0.3),
    ("Violas", ["Vla"], S + "Violas/06 Keyswitch/Violas KS Master.oib", "string", 0.15),
    ("Violoncellos", ["Vc"], S + "Celli/06 Keyswitch/Celli KS Master.oib", "string", 0.4),
    ("Double basses", ["Cb"], S + "Basses/05 Keyswitch/Basses KS Master.oib", "string", 0.6),
]

# Percussion strokes (score_to_parts.build_perc_track). Keys read from the .oib region maps: Tam Tam Long RR = 36 (12
# velocity layers); Crash Long = 60 (7 layers); Sus Cymbal "Crs" (a recorded crescendo roll ending in a let-ring) = 60, 62,
# 64, 65 (four lengths, shortest first), vel 1-89 the p take, 90-127 the f take. The roll of bar 159 (pp <, into the fff
# crash at qn 636) starts on its written beat for cycle 0; its lead_s should be set so the sample's peak meets qn 636.
# c01 (A #4, B #4, C #2): on c00 the key 60 roll (f1, the shortest take, 8.3-9.3 s) peaked 0.84-0.9 s after its start
# and was 16-22 dB down at the crash (qn 636; bar 159 lasts 1.98 s). Key 64 (f3, 10.2-10.9 s; .ews frame counts read by
# critic C) is inferred to peak about 2.4 s after its start if every take rings about 8 s after its peak, so lead_s 0.45
# puts the peak on qn 636 (unverified: measure the stem's peak time on c01 and set lead_s = peak - 1.98 s).
# c01 (B #4): the pp soft-stick tam-tam at qn 696 played velocity 40, a dark layer 20 dB under the orchestra with nothing
# over 2 kHz: velocity floor 60.
# c03 (critic C #3): the crash and the tam-tam sounded 60-70 ms ahead of the sustained sections' attacks: delay_s 0.05.
# The suspended-cymbal peak must still meet the crash, which is now 0.05 s (delay) + 0.15 s (CAESURA at 636) later
# relative to the roll's written start (qn 632): lead_s 0.45 -> 0.25.
PERC_MAP = {"Tam-tam": {"tamtam": {"key": 36, "min_s": 12.0, "vel_min": 60, "delay_s": 0.05}},
            "Suspended cymbal": {"ridecymbal": {"key": 64, "vel": 105, "min_s": 6.0, "lead_s": 0.25}},
            "Crash cymbals": {"crashcymbal": {"key": 60, "min_s": 9.0, "delay_s": 0.05}}}

# c01 (B #3): the coda cello solo (bars 171-174, mp espr.) has five untargeted hairpins; the untargeted rules ratcheted
# it from CC 58 to 93 (above f) and the stem measured its own f level, 8-9 dB over a printed mp, with the cor anglais
# imitation 11 dB under it. Each swell now crests at mf (or a little under) and returns to mp. "mp+" is a level between
# mp and mf (a target equal to the current level would start the hairpin 12 CC lower, the "niente <" rule).
DYN["mp+"] = 65
HP_TARGET_AT = {"Vc": {680.0: "mf", 683.5: "mp", 685.0: "mp+", 691.0: "mf", 692.0: "mp"}}

# c01 (B #5): the first cello and bass note (the pickup at qn 3, Leg Slur MAX first note at pp) blooms 7-10 dB over the
# next note's body within 0.4 s; their note trims ramp in over the bloom (build/note_trims.json)
NOTE_TRIM_RAMP_S = {"Violoncellos": {3.0: 0.3}, "Double basses": {3.0: 0.3}}

# The printed rit./allargando/animando steps (global.ily \mt) smoothed into 0.25 qn ramps: (start qn, end qn, tempo at
# the start). Bars 45-46 poco rit. into Poco meno mosso, 62-68 poco animando + rit., 121-122 allargando into sostenuto,
# 145-146 poco rit., 156-158 poco animando, 165-166 rit., 177-178 rit. The sostenuto (123-126), largamente (160-164) and
# the final bar's 30 bpm fermata are tempo steps, left as printed.
RAMP_SPANS = [(176, 184, 126), (244, 260, 112), (260, 272, 118), (480, 488, 126), (576, 584, 126), (620, 632, 112),
              (656, 664, 100), (704, 712, 72)]

# c02 (A #3): timpani rolls that end on a tied, unrolled note (the MIDI merges the tie into the roll): a stroke there.
# The pp/dim. tied ends (54, 249, 581) stay rolls ending in their diminuendo (felt strokes below v53 are near silent).
# On c01 the stem was flat through the tied notes at 46, 460, 561 and 641 (+-1 dB of the roll): no attack
TIMP_TIE_STROKES = [46.0, 460.0, 561.0, 641.0]

# c02: the Violoncellos' bar 72-76 held A flat keeps its c01 re-bow points (fitted shapes in build/rebow_fills.json): the
# detached bar-72 strokes (DETACH_ACCENTS) moved the note's start from 285.55 to 286.0, which moved the automatic points
REBOW_AT = {"Violoncellos": [289.145, 293.758, 298.37]}

# c03 (critic C #6): the printed tutti breath before the fff of bar 160 takes time (the master did not dip at qn 636);
# the bar-170 fermata over the rest after the ff chord lasts 2.5 s (24 bpm) instead of 1.5 s, so the silence reads as
# a fermata before the cello's Piu lento solo. PHRASE_ARCS deferred (they move the Lento re-bows that were refitted).
CAESURA = {636.0: 0.15}
BEAT_STRETCH = {679.0: 0.6}

# c03 (critic C #5): legato leads measured against the other sections' attacks at the same onsets (axis-independent):
# Violoncellos Leg BC MAX -0.118 s (n=36), Oboe 1 -0.098 (12), Horn 1 -0.100 (7), Clarinet 1 -0.070 (15), Cor anglais
# -0.066; Violins I/II and Violas Leg BC within +-0.01. Cut each early group by about half its measured lead. The Leg
# Slur extras and the movement II per-pitch tables stay (C's soft-join and per-pitch numbers were measured on the
# shifted c02 axis: 0.08-0.2 s of each is the time-map error), except the Oboe F5 -> Eb5 pair (-0.05..-0.075 s at 126
# after correcting the axis).
LEG_LEAD_S = dict(LEG_LEAD_S, **{"Oboe": 0.03, "Cor anglais": 0.05, "Clarinet": 0.0, "Horn": 0.06})
LEG_ART_EXTRA_S = {"Violins II": {"Leg Slur MAX": 0.04, "Leg BC MAX": -0.03},
                   "Violoncellos": {"Leg Slur MAX": 0.05, "Leg BC MAX": -0.06},
                   "Violas": {"Leg Slur MAX": 0.025}}
LEG_PAIR_EXTRA_S = dict(LEG_PAIR_EXTRA_S, **{"Oboe 1": {(73, 72): 0.10, (77, 75): 0.05}})

# c03 (critic A #5, #6): articulation tests (Bassoon 1 Stac DblTng RRx9 bars 87-89, Double basses Marc Shrt RRx4 bars
# 27-28) both failed on the c03 render (cycles/c03/CHANGES.md) and are reverted in c04: no ART_SPANS.
ART_SPANS = {}

# c04 (c03 open item): the c03 wind entry extras (+0.11 s Leg Slur MAX / Leg Slur, +0.07 Sus Non Vib) moved the flute and
# oboe pickups from +0.05 to -0.03 s, 0.04-0.09 s ahead of the violins: halved
ENTRY_LEAD_ART_S = dict(ENTRY_LEAD_ART_S, wind={"Leg Slur MAX": 0.055, "Leg Slur": 0.055, "Sus Non Vib": 0.035})

# c04 (critic A #2): Horn 1's slurred tenutos at the top of the dolce second-theme phrase (bars 48, 51, 148, 151) rose
# 8-9 dB over the note before when re-tongued on Sus MAX: joined on Leg Slur MAX with a portato notch
PORTATO_JOIN_AT = {"Horn 1": [189.0, 201.0, 589.0, 601.0]}

# c04 (critics A #3, C #4): the opening ppp roll (19 s), the bar-13 roll and the final roll cycle in colour at the loop
# period (centroid autocorrelation 0.89-0.95): re-struck in irregular 2.5-3.3 s pieces. 464 and 484 (masked by the
# tutti and the tam-tam) stay whole as the control; their loop profiles stay too
TIMP_ROLL_RESTRIKE = dict(TIMP_ROLL_RESTRIKE, at=[0.0, 48.0, 720.0])
# c05 (critic A #6): the control rolls at 464 and 484 (bars 117-130) still cycle in colour (centroid autocorrelation
# 0.92-0.96, folded swing 350-375 cents); under the retransition (bars 127-130) the roll is the floor, 10.5 dB under the
# master. Same rule and seed; their loop profile (484) is removed from build/loop_profiles.json
TIMP_ROLL_RESTRIKE = dict(TIMP_ROLL_RESTRIKE, at=[0.0, 48.0, 464.0, 484.0, 720.0])

# c05 (critic A #4): portamento on the two expressive leaps HO's Leg Port MAX can play: the coda cello solo's minor sixth
# up (qn 685, bar 172; the join dipped 7.4 dB) and the violins' "sul A" sixth (qn 225, bar 57). Loads the Leg Port MAX
# row on these three tracks (a full rebuild of each)
PORT_TARGETS = {"Violoncellos": {685.0: 100}, "Violins I": {225.0: 100}, "Violins II": {225.0: 100}}

# c05 (critic A #3, test): slurred Sus MAX eighths (short_sus) 0.05 s early on Violins I and II; Violas and Violoncellos
# are the control (Vln I/II crossed a median +0.12 s, the winds doubling them +0.035..+0.095 s)
SHORT_SUS_LEAD_TRACKS = ("Violins I", "Violins II")
# c06: the c05 test failed (0.05 s of lead moved the crossover 0.015-0.02 s): reverted
SHORT_SUS_LEAD_TRACKS = ()

# c05 (critic C #2): the final ppp chord's held horn notes (12.8 s each, one sample) cycle in colour at the loop period
# (Horn 4: autocorrelation 0.91 at 100-300 Hz, 0.72 centroid; folded swing 19.7 dB at 100-300 Hz) after the c03 level
# profile. Staggered breaths, each piece 3.6-5.0 s (720-724 is 1.2 s/qn, 724-728 2 s/qn), the two horns 0.5-1.0 s apart;
# the Horn 4 loop profile at 720 is removed
BREATH_SPLIT_AT = {"Horn 4": {720.0: [723.0, 725.5]}, "Horn 3": {720.0: [723.5, 726.0]}}
# c06 (critic C #4, A #6): two splits 2.5 s apart restarted the same sample shape every 4.2-4.6 s (Horn 3 fundamental
# band autocorrelation 0.91 at 4.6 s, master 250-274 Hz 0.63 at 4.5 s): three splits per horn at irregular spacing,
# pieces 1.9-4.2 s, Horn 4 offset by about half a trough; the re-entry dip halved (the stem dips reached 8.9 dB)
BREATH_SPLIT_AT = {"Horn 3": {720.0: [722.3, 724.6, 726.6]}, "Horn 4": {720.0: [721.6, 723.8, 725.9]}}
BREATH_SPLIT = dict(BREATH_SPLIT, dip_db=-1.5)

# c04 (critic B #2): the coda pp strokes (bars 179-180, the C-G-C figure) at v56 peaked 17-26 dB under the master; the
# felt patch steps 8-16 dB between v56 and v64
TIMP_VEL = {712.0: 62, 713.5: 62, 714.0: 62, 716.0: 62, 717.5: 62, 718.0: 62}

# c04 (critic C #5): the sf of bar 41 (after the f crescendo of bars 38-40, decrescendo to the mf of bar 42) fell back
# under bar 40 within a beat (post-spike level - 10 CC); it is the transition's tutti arrival with the horns' ff a2
SF_ARRIVAL_AT = {160.0: "ff"}

# c04 (critic C #1): lead lines (phrase tops by pitch, soft-hairpin dB ramps; movement II c14/c18/c22). Score qn
LEAD_SPANS = {"Violins I": [(56, 128), (220, 244), (440, 480), (520, 576), (620, 644)],
              "Cor anglais": [(20, 36)], "Horn 1": [(184, 220), (584, 620)],
              "Violoncellos": [(184, 220), (584, 620), (680, 696)],
              "Clarinet 1": [(504, 520)], "Violas": [(664, 680)]}
HP_SOFT_EXTRA_SPANS = {"Clarinet 1": [(220, 244)], "Horn 2": [(220, 244)], "Cor anglais": [(683, 695)]}

# c04 (critic C #2, step 1): phrase arcs and pushes only where no string note carries a re-bow (the re-bow points and
# fitted shapes stay valid); the Lento and coda arcs wait for a cycle that refits the re-bows
PHRASE_ARCS = [(56, 72, "sub"), (72, 88), (104, 120, "sub"), (120, 128, "main"),
               (200, 220, "main"), (220, 232, "sub"), (232, 244),
               (520, 536, "sub"), (536, 552), (552, 568, "sub"), (568, 576, "main"),
               (584, 600), (600, 620)]
# (148, 160) dropped: the push moved the celli's re-bows at 152.46/163.88 by 0.01 qn (C's rule: rows must not change)
TEMPO_PUSH = [(88, 100, 1.015), (552, 564, 1.015)]

# ---------- c06 ----------
# critic A #1: the fff downbeat of bar 160 (after the caesura) is a printed down-bow on Violins I/II (and Violins II's
# 628): a fresh Sus MAX stroke instead of a Leg BC transition (Vln I sagged 7.3 dB at the beat, Vln II 6.2, Vc 5.3)
DOWNBOW_STROKE_AT = {"Violins I": [636.0], "Violins II": [628.0, 636.0], "Violoncellos": [636.0]}
# critic B #1: accented notes on the gentle families were to play the plain velocity + vel_add (brass +5, winds and
# strings +10). Rendered in c06, the 485 accented Sus notes with 10-15 less velocity were identical to c05 to 0.01 dB in
# body and peak on every track: the KS Master sustain rows ignore velocity. Off (no vel_add); the accent level is the
# swell: brass db 4.0 -> 2.5 (stem fix after the c06 render: the theme accents stood 6-7 dB over the notes around them)
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass=dict(GENTLE_ACCENT["brass"], db=2.5))
# critic A #3: slurred wind tenutos at f/ff (bars 69-70, 98-102) re-tongued on Sus MAX dipped 5-12 dB and arrived under
# the eighth before them: joined as portato legato targets like Horn 1's
PORTATO_JOIN_AT = dict(PORTATO_JOIN_AT, **{"Oboe 1": [277.0, 393.0, 400.0, 405.0], "Cor anglais": [393.0, 400.0, 405.0],
                                            "Flute 1": [277.0, 393.0, 400.0, 405.0, 436.0], "Flute 2": [277.0],
                                            "Bassoon 1": [413.0], "Trumpet 1": [277.0]})
# critic C #1: the fff downbeat of bar 160 and the fff of bar 122 arrive with a step (master momentary step +0.4 dB at
# 636, +2.5 at 484, against +3..+6 at the other tutti arrivals)
ARRIVAL_WEIGHT_AT = {636.0: (-2.5, 2.5), 484.0: (-1.5, 1.5)}
# c06 stem fix: at +2.5 dB the arrival with the crash made the master's top peak (1.70 at qn 636.3 after the string
# shapes below, delivery limiter 3.9 dB): +1.5 at 636 (the step from the held-back crescendo top stays 4 dB)
ARRIVAL_WEIGHT_AT = {636.0: (-2.5, 1.5), 484.0: (-1.5, 1.5)}
# c06 stem fix (critic C #6): the Violins I A-flat6 join at qn 637.9 (with Horn 1) is the second master peak (1.60)
JOIN_NOTCH = dict(JOIN_NOTCH, **{"Violins I": [(637.6, 638.1, -1.5)]})
# critic C #2: bars 60-61 crescendo (236-244) fell 7 dB on Violins I and the master did not rise; the sub. p at 244 fell
# only 3.3 dB (Horn 3 rose 3.5 dB). A +4 dB ramp on the hairpin's tracks, gone just before the subito, and -3 dB on every
# track over the sub. p bar (Horn 3 a further -3)
_hp236 = [(236.0, 0.0), (243.9, 4.0), (243.94, 0.0)]
_subp = [(243.94, 0.0), (244.0, -3.0), (247.5, -3.0), (248.0, 0.0)]
LEVEL_SHAPES = {tn_: [_hp236] for tn_ in ("Violins I", "Violins II", "Violas", "Clarinet 1", "Bassoon 2", "Horn 2",
                                          "Horn 3", "Horn 4", "Double basses")}
LEVEL_SHAPES["_all"] = [_subp]
LEVEL_SHAPES["Horn 3"] = LEVEL_SHAPES["Horn 3"] + [_subp]
# critic C #5: Clarinet 1's p < mf (504.5-512, the theme over the crescendo pedal) did not grow (-39.3 -> -39.7 dB); its
# mf hpgain (+2) gets +3 more, held a beat past the arrival
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(504.5, 0.0), (512.0, 3.0), (513.0, 3.0), (514.0, 0.0)]]
# c06 stem fix: the down-bow strokes at 636 played 2-6.5 dB over the arrival weight (Sus MAX at fff against the Leg BC
# joins of c05; Violins II +11.5 dB over c05 in the first quarter beat) and made the master's top peak (1.84 at qn
# 636.2, delivery limiter 4.4 dB): level shapes take each stroke back to c05 + the arrival weight
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(635.9, 0.0), (635.94, -6.0), (636.3, -5.0), (636.75, -4.0), (637.4, -3.5), (637.6, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(635.9, 0.0), (635.94, -3.5), (636.3, -3.0), (636.75, -2.0), (637.4, -1.5), (637.6, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = [[(635.9, 0.0), (635.94, -2.0), (636.75, -1.5), (637.4, -1.2), (637.6, 0.0)]]
# critic C #5: the fff tam-tam (qn 484) rang on past its printed damp (bar 127): -24 dB over 0.5 s from the note's end
PERC_MAP["Tam-tam"]["_damp"] = [(504.2, -24.0, 0.5)]
# critic A #5 (test, Violins II the control): slurred non-first eighths of 0.20-0.25 s on Violins I stay Leg Slur MAX
# legato targets with the lead cap raised to 0.75 of the previous note (Sus MAX eighths crossed a median +0.10 s late)
SHORT_SUS_LEG_TRACKS = ("Violins I",)
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{"Violins I": [(56.0, 728.0, 0.75)]})
# critic B #1, #2, #6: note trims as steps (0.1 s ramp): the brass themes' legato notes (+3), the oboe's bar 145 pickup,
# Horn 1's re-attacked slur starts in the second theme
NOTE_TRIM_RAMP_S = dict(NOTE_TRIM_RAMP_S, **{
    "Horn 1": {q_: 0.1 for q_ in [272.5, 274.5, 275.0, 275.5, 276.0, 276.5, 277.0, 277.5, 280.0, 280.5, 281.0, 281.5,
                                  664.5, 666.5, 667.0, 667.5, 668.0, 669.0, 669.5, 672.5, 674.5, 675.0, 675.5, 192.0, 592.0]},
    "Trumpet 1": {q_: 0.1 for q_ in [664.5, 666.5, 667.0, 667.5, 668.0, 669.0, 669.5, 672.5, 674.5, 675.0, 675.5]},
    "Oboe 1": {578.0: 0.1}})

# ---------- c07 ----------
# ONE_TIME (Dan's item 8) + critic A #3: the theme head g8( es'4.->) in Horn 1 (273, 665, 673), Trumpet 1 (665, 673)
# and Trombone 1 (521, 529) was the only slurred accent re-tongued on Sus (after a 0.07 qn gap): it stood 4.8-8.4 dB
# over the slur's other notes (Horn 1 673 +9.5) with a bright or late attack. Brass slurred accents stay legato targets
# and take only the swell, as the winds have since c01
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass=dict(GENTLE_ACCENT["brass"], keep_legato=True))
# critic A #1: loud Sus MAX / Stac notes in lines that mix rows sat 2-6 dB over the Leg rows at the same CC11 (Sus minus
# Leg at CC11 >= 80: Violins II +4.7, Violas +5.6, Violoncellos +2.1, Violins I +1.7 dB; Stac 4-10 dB over); about 85%
ROW_TRIM_DB = {"Violins II": {"Sus MAX": (-4.0, 80)},
               "Violas": {"Sus MAX": (-4.5, 80), "Stac RRx9": (-4.0, 80)},
               "Violoncellos": {"Sus MAX": (-1.5, 80), "Stac RRx9": (-4.0, 80)},
               "Violins I": {"Sus MAX": (-1.5, 80), "Stac RRx14": (-3.0, 80)}}
# critic A #2: horn repeats dipped a median 1.3-4.1 dB (54 of 92 under 3 dB), Bassoon 2's ff eighths of bar 82
# 0.6-2.1 dB: the Solo French Horn release and the hall fill a 0.06 s gap
WIND_REP_RETONGUE_BY = {"Horn": {"gap_s": 0.10, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15}}
WIND_REP_RETONGUE_SHORT = {"max_qn": 0.5, "min_bpm": 100.0, "gap_s": 0.10, "frac": 0.45, "fall_cc": 8}
BREATH_FALL_BY = {"Horn": 10}
# critic A #2: the low brass played through the printed breath before the fff of bar 160 (gap 0.02-0.065 qn after the
# c06 entry leads; dips 0.7-2.5 dB against Trumpet 1's 10.7)
BREATH_GAP_AT = dict(BREATH_GAP_AT, **{"Trombone 1": {632.0: 0.22}, "Bass trombone": {632.0: 0.22},
                                       "Trumpet 3": {632.0: 0.22}})
BREATH_FALL_CC = dict(BREATH_FALL_CC, **{"Trombone 1": {632.0: 10}, "Bass trombone": {632.0: 10},
                                         "Trumpet 3": {632.0: 10}})
# critic A #5: every ff timpani stroke at v110, pickups as hard as the downbeats they lead to (0.35 dB per velocity step)
TIMP_METRIC_VEL = {"down": 0, "mid": -3, "beat": -5, "off": -9, "jit": 2, "min_cc": DYN["f"]}
# critic A #6: the c06 Violins I eighths test (Leg Slur MAX): kept (crossover +0.065 against Violins II's +0.095 s;
# stem dips equal at the 17 shared onsets, master dips 4 of 45 at -4 dB); the three worst joins back to Sus MAX
SHORT_SUS_LEG_SKIP = {"Violins I": [77.5, 259.5, 455.5]}
# critic A #6: two wind portato joins dip more as legato targets than they did re-tongued (Oboe 1 405 6.5 dB, c05 Sus
# 4.4; Flute 1 393 6.8, c05 6.1): back to the re-tongue
PORTATO_JOIN_AT = dict(PORTATO_JOIN_AT, **{"Oboe 1": [277.0, 393.0, 400.0], "Flute 1": [277.0, 400.0, 405.0, 436.0]})
# critic C #1: the basses changed pitch a median +0.155 s after the score (celli +0.05) on 95 abutting Sus MAX changes;
# Horns 3/4 Sus chord changes +0.10/+0.115 s (the kit's movement II c20 rule, scaled to the measured lag)
ABUT_LEAD = {"Double basses": {"lead_s": 0.12, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True},
             "Horn 3": {"lead_s": 0.06, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True},
             "Horn 4": {"lead_s": 0.06, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}}
# critic C #2: slurred Sus MAX eighths on Violins II cross a median +0.122 s late; the c05 lead failed because the old
# note kept sounding. Lead 0.06 s with the previous note ending 0.03 qn after the moved onset (Violas the control;
# Violins I is on the A #6 Leg Slur test)
SHORT_SUS_LEAD_S, SHORT_SUS_LEAD_TRACKS, SHORT_SUS_LEAD_KEEP_OVERLAP = 0.06, ("Violins II",), 0.03
# critic C #3: string entries after a rest at CC11 51-80 in the Allegro reach body - 4 dB at +0.17 s (f layer +0.05-0.09)
ENTRY_LEAD_S = dict(ENTRY_LEAD_S, string=(0.12, 0.06, 0.12))
# (not the basses: their off-beat eighths of bars 15-22 are at body level at the onset; Basses KS Master entries keep 0.06)
ENTRY_LEAD_S["Double basses"] = (0.12, 0.06)
# critic C #4: the (568, 576) "main" arc slowed beat 575 to 111 bpm and the printed poco rit. of bar 145 then started at
# 126 (a 13% speed-up inside a rit.); the animandos of bars 62 and 156 started at 112 from a 103 bpm beat, under the
# printed 115
PHRASE_ARCS = [x_ if x_[:2] != (568, 576) else (568, 576, "sub") for x_ in PHRASE_ARCS]
RAMP_SPANS = [(576, 584, 120) if r_[:2] == (576, 584) else (244, 260, 115) if r_[:2] == (244, 260)
              else (620, 632, 115) if r_[:2] == (620, 632) else r_ for r_ in RAMP_SPANS]
# critic B #1: the 22in crash stroke makes the master's top peak (1.56 at qn 636.33, 0.34 of the sample): -4 dB on the
# attack, the ring at +1.4 s untouched
LEVEL_SHAPES["Crash cymbals"] = [[(636.0, 0.0), (636.02, -4.0), (636.6, -4.0), (637.2, 0.0)]]
# c07 stem fix: the violas' STR_SHORT_AFTER_SUS strokes carry the c05 fitted roles [388.5,408,-4] and [464,484,-3.5,4]
# (the same row offset); elsewhere the strokes are trimmed with the notes around them (the render left the accented Sus
# notes at Violas 110/670 6.6-6.8 dB under the untrimmed stroke after them)
ROW_TRIM_SKIP = {"Violas": [(388.5, 408.0), (464.0, 484.0)]}

# ---------- c08 ----------
# critic C #1: ARRIVAL_WEIGHT_AT's 4 qn hold-back cancelled the printed crescendo bar into both fff arrivals (bar 159:
# +0.8 dB over 632-636, the master at 635.5 0.1 dB under bar 158; bar 121 +1.6): the hold-back is now a breath over the
# last 0.5 qn. The violins' held E6 (629-633, CC11 flat) decayed 6-9 dB before the crescendo's quarter notes: +4 dB fill
ARRIVAL_WEIGHT_AT = {636.0: (-2.5, 1.5, 0.5), 484.0: (-1.5, 1.5, 0.5)}
_e6fill = [(629.5, 0.0), (631.5, 4.0), (633.0, 4.0), (635.4, 4.0), (635.9, 0.0)]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [_e6fill]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [_e6fill]
# critic C #4 (hand version): the celli's held notes in the dolce second theme play their small hairpins flat or the wrong
# way (the Sus/Leg sustain decays as much as the CC11 hairpin adds): ramps ending 0.05 qn before the next onset
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(184.0, 0.0), (187.45, 3.0), (187.5, 3.0), (188.0, 0.0)], [(201.0, 0.0), (202.95, 3.0), (203.3, 0.0)],
    [(589.0, 0.0), (590.95, 2.5), (591.3, 0.0)], [(196.0, 0.0), (197.95, -2.5), (198.3, 0.0)]]
# critic B #2: the bar 122 fff chord was led by the violins (4-6 dB over trumpets/trombones, 8-11 over the horns) with a
# hollow middle (violas 13 dB under Violins II, basses 0.3% of the master): from the downbeat (0.2 qn ramp, the bar-121
# approach untouched) to bar 123
_b122 = lambda d_: [(484.0, 0.0), (484.2, d_), (492.0, d_), (492.5, 0.0)]
for tn_, d_ in [("Violins I", -3.0), ("Violins II", -3.0), ("Horn 1", 4.0), ("Horn 2", 4.0), ("Horn 3", 4.0),
                ("Horn 4", 4.0), ("Violas", 6.0), ("Double basses", 4.0), ("Trumpet 1", 1.5), ("Trumpet 2", 1.5),
                ("Trumpet 3", 1.5)]:
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [_b122(d_)]
# critic B #3: the bar-82 ff motive's Trumpet 1 sat 2.6-6.6 dB under Trumpet 2's held note and 7-9 dB under the violins
# (the celli the loudest stem); roles.json has the held trumpets and the violas
LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES["Trumpet 1"] + [[(324.2, 0.0), (324.4, 4.0), (328.0, 4.0), (328.5, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(324.0, 0.0), (324.25, -3.0), (328.0, -3.0), (328.5, 0.0)]]
# critic B #1: hot f/ff notes (build/note_trims.json) as steps; critic A #1: Violins I's merged slur-end Sus MAX notes
_steps = {"Violoncellos": [100.0, 548.0, 556.0, 526.0, 272.0], "Oboe 1": [95.0, 99.0, 100.0, 113.0, 479.0, 553.0, 557.0],
          "Horn 1": [97.0, 633.0], "Flute 1": [118.0, 121.5, 160.0, 482.0, 561.5], "Flute 2": [285.0, 459.0],
          "Bass clarinet": [284.0, 286.0, 554.0], "Clarinet 1": [414.0, 417.0, 422.0], "Trombone 1": [632.0, 676.0],
          "Violins I": [59.5, 571.5]}
for tn_, qs_ in _steps.items():
    NOTE_TRIM_RAMP_S[tn_] = {**NOTE_TRIM_RAMP_S.get(tn_, {}), **{q_: 0.1 for q_ in qs_}}
# critic A #5: horn breaths dipped 2.1-3.2 dB (the fall applies only at mf or louder; soft horns need it too), Flute 1 /
# Oboe 1 3.0/3.9 dB before the fff (keys: the onset of the note that ends at the breath; Horn 1 468 and Horn 4 504 are merged held notes)
BREATH_GAP_AT = dict(BREATH_GAP_AT, **{"Horn 1": {468.0: 0.4}, "Horn 3": {252.0: 0.4, 532.0: 0.4}, "Horn 4": {504.0: 0.4},
                                       "Flute 1": {634.0: 0.12}, "Oboe 1": {634.0: 0.12}})
BREATH_FALL_CC = dict(BREATH_FALL_CC, **{"Horn 1": {468.0: 8}, "Horn 3": {252.0: 8, 532.0: 8}, "Horn 4": {504.0: 8},
                                         "Flute 1": {634.0: 8}, "Oboe 1": {634.0: 8}})
# critic A #5: Horn 4's p pedal repeats still dip a median 2.7 dB (8 of 12 under 3): longer gap and a deeper fall
WIND_REP_RETONGUE_BY = {"Horn 4": {"gap_s": 0.14, "frac": 0.35, "fall_cc": 14, "fall_s": 0.18}, **WIND_REP_RETONGUE_BY}
# critic A #4: tremolo chord changes dipped 4-10 dB (11 of 41); the celli's five untied G2 tremolo whole notes (bars
# 117-121) pulsed once per bar (level autocorrelation 0.88 at the two-bar lag, swing 7.9 dB)
TREM_JOIN = {"Violins II": [(304.0, 324.0), (440.0, 464.0), (584.0, 620.0)], "Violas": [(154.0, 168.0), (304.0, 324.0)],
             "Violoncellos": [(464.0, 484.0)]}
# critic C #5: the Allegro accompaniment eighths have no metric shape (downbeat minus neighbours -0.4..+0.6 dB)
METRIC_BOWED = {tn_: [(56.0, 128.0), (272.0, 286.0), (520.0, 568.0)] for tn_ in ("Violas", "Violoncellos", "Double basses")}
# critic A #6: loud timpani off-beats and pickups hit as hard as the downbeats (velocity moved them 0.6 dB in c07)
METRIC_TIMP_DB = {"down": 0.0, "mid": -1.0, "beat": -2.0, "off": -3.0, "min_cc": DYN["f"]}
# critic C #2: the closing and the whole development (qn 272-480, 99 s) played at exactly 126 bpm. Arcs and pushes only
# where no string note is re-bowed (all spans end by 464); the coda cello solo's arcs keep the violas' two automatic
# re-bow points in qn (listed, so the arcs do not move them)
PHRASE_ARCS = PHRASE_ARCS + [(272, 286, "main"), (324, 332, "main"), (332, 348, "sub"), (348, 360, "sub"),
                             (384, 396), (396, 408, "main"), (408, 416, "sub"), (416, 424), (424, 432, "sub"),
                             (432, 440, "main"), (440, 452, "sub")]
TEMPO_PUSH = TEMPO_PUSH + [(308, 324, 1.015), (364, 384, 1.015), (452, 464, 1.01)]
REBOW_AT = dict(REBOW_AT, **{"Violas": [686.694, 699.507]})
PHRASE_ARCS = PHRASE_ARCS + [(680, 688, "sub"), (688, 696, "main")]
# the repeated-note accompaniment eighths are REP_SPLIT strokes (most of the violas' unslurred eighths): steps on them too
METRIC_BOWED_REP = True

# ---------- c09 ----------
# critic C #1: the Hollywood Brass KS Masters and the Clarinet KS Master crossfade their dynamic layers with CC1 (read
# from the .oib layer groups: "1Tb p/mp/f/ff", "1FH pp/mf/f/ff", "1V pp/p/mf/f/ff", "Tu pp/mf/f/ff", "Cl p/mp/f" each
# have a cc 1 rescaler on their Source volume); CC1 57-87 played every printed dynamic on the mp-f samples. The bass
# clarinet (BC KS Master) uses CC11 and keeps the old formula. The contrabassoon's CC1 57-87 sat in the CB KS Master's
# Non Vib fade (64-80): held at 40 (Non Vib only)
CC1_DYN_TRACKS = ("Horn", "Trumpet", "Trombone", "Bass trombone", "Tuba", "Clarinet ")
CC1_HOLD = {"Contrabassoon": 40}
# critic A #1: short hairpins (HP_SHORT_S, generic) and the coda cello's 683.5 ">" now follows that rule (its "mp"
# target took the line 13 CC down inside half a beat); Horn 1's dolce tenuto portato notch 10 -> 4 CC
HP_TARGET_AT = {"Vc": {k_: v_ for k_, v_ in HP_TARGET_AT["Vc"].items() if k_ != 683.5}}
PORTATO_JOIN_NOTCH = {"Horn 1": 4}
# critic A #2 (test): Violins I's theme-head accents after an eighth pickup slurred up 8-12 semitones sat -0.3..+2.2 dB
# over their neighbours at the fit's caps (+5 swell, +5 step): fresh Sus MAX strokes (the DOWNBOW_STROKE_AT path); their
# accent_fits rows are removed so the next refit starts from the default swell
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violins I": DOWNBOW_STROKE_AT["Violins I"] + [57.0, 65.0, 113.0, 479.0]})
# critic A #4: tremolo entries after a held note started with a 5-10 dB hole (TREM_ENTRY_LEAD_S, generic); the Violins II
# split piece 0.33 qn after a chord change (592.33) re-attacked: clear_qn 0.3 -> 1.0
TREM_ENTRY_LEAD_S = 0.08
TREM_SPLIT = dict(TREM_SPLIT, clear_qn=1.0)
# critic B #3: the printed crescendo roll of bar 159 grew +0.8 dB while the master rose 2.3: +5 dB over the bar, meeting
# the fff stroke at 636
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES.get("Timpani", []) + [[(632.0, 0.0), (635.9, 5.0), (636.1, 0.0)]]
# critic C #4: the fff crash (l.v.) at 636 was gone 1 s after the hit (4-12 kHz -11.9 dB re master at +1.5 s): the c07
# attack cut stays, the ring is held up over the largamente bar
LEVEL_SHAPES["Crash cymbals"] = [[(636.0, 0.0), (636.02, -4.0), (636.6, -4.0), (637.2, 0.0), (638.5, 5.0), (644.0, 6.0)]]
# critic C #5: the two held wind notes that still loop at the 3.95 s period (Bassoon 2 G2 at qn 48, 8.4 s; Bass clarinet
# G2 at 492, 7.2 s): irregular breath splits as the c06 horns
BREATH_SPLIT_AT = dict(BREATH_SPLIT_AT, **{"Bassoon 2": {48.0: [51.4]}, "Bass clarinet": {492.0: [496.8, 500.9]}})

# ---------- c10 ----------
# critic C #2: bars 60-61 (236-244): the crescendo still fell on Violins I (the falling line plays 6 dB quieter in the
# samples than the +4 dB _hp236 ramp adds; master last beat under the first): second ramps from the second note, gone
# before the sub. p
_hp238 = lambda d_: [(238.0, 0.0), (243.9, d_), (243.94, 0.0)]
for tn_, d_ in [("Violins I", 7.0), ("Violins II", 5.0), ("Horn 3", 3.0), ("Violas", 3.0)]:
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [_hp238(d_)]
# critic C #3a: the celli's c08 hairpin ramps in the dolce second theme released just before the arrival note (191/591
# measured 2.3-3.4 dB under the crest): held through the arrival; the missing exposition shape at 189; 201 held to 204.2
LEVEL_SHAPES["Violoncellos"] = [s_ for s_ in LEVEL_SHAPES["Violoncellos"] if s_[0][0] not in (589.0, 201.0)] + [
    [(589.0, 0.0), (590.95, 2.5), (591.9, 2.5), (592.2, 0.0)], [(189.0, 0.0), (190.95, 2.5), (191.9, 2.5), (192.2, 0.0)],
    [(201.0, 0.0), (202.95, 3.0), (204.2, 3.0), (204.7, 0.0)]]
# critic B #4: timpani crescendo rolls on top of the melody (bars 62-63: -6.5 dB re master over the violins' sub. p tune;
# bars 80-81: the loudest or second stem in 7 of 8 beats, growing 2.7 dB while the master grew 8): the roll settles
# under the texture after its attack and grows into the next downbeat
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [
    [(245.5, 0.0), (246.5, -2.0), (247.5, -3.5), (248.6, -3.5), (249.5, 0.0)],
    [(316.3, 0.0), (316.9, -3.5), (319.5, -3.0), (323.9, 2.0), (324.0, 0.0)]]
# critic C #4: the ff < into the fff of bar 160: the brass did not grow (Trumpet 1 -3.3 dB across the hairpin); a start-
# low shape on the 11 brass tracks (the arrival weight's 0.5 qn hold-back and the breaths are untouched)
for tn_ in ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trumpet 1", "Trumpet 2", "Trumpet 3", "Trombone 1", "Trombone 2",
            "Bass trombone", "Tuba"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(631.9, 0.0), (632.3, -3.0), (635.4, 0.0)]]
# critic A #4 (step 1): the harp's étouffez at qn 650 (over a rest): the F2 chord rang 24 -> 13 dB through the rest. A
# damp in the volume envelope (tail_hold false for the Harp in build/mix.json), restored before the 652 chord. The damps
# at 244 and 654 need a second harp instance (new notes start with the damp): deferred
LEVEL_SHAPES["Harp"] = LEVEL_SHAPES.get("Harp", []) + [[(650.0, 0.0), (650.08, -30.0), (651.9, -30.0), (651.98, 0.0)]]
# critic A #2 (item 3, as a notch skip): an automatic re-bow 0.12-0.52 qn before a printed same-pitch bow change inside a
# merged note made a second dip (the 14 CC bow-change notch) 0.15 s after the re-bow (celli 39.879/40.0 -> the master fell
# 3.6 dB in the bars 9-11 crescendo; 51.87/52.0, 163.877/164.0, 719.483/720.0; violas 52.384/52.0). The re-bow already
# changes bow there: no notch. The fitted shapes of these re-bows are refit on the c10 render
NOTCH_SKIP = dict(NOTCH_SKIP, **{"Violoncellos": [40.0, 52.0, 164.0, 720.0], "Violas": [52.0]})
# critic C #6: two exposed held notes still cycle in colour at the loop period (Cor anglais 27-35, centroid
# autocorrelation 0.65; Horn 4 720, level 0.65 / centroid 0.59 with pieces of 2.2/2.1 s): one breath inside the cor
# anglais tie, Horn 4's middle split moved so that its pieces differ by 0.5 s or more
BREATH_SPLIT_AT = dict(BREATH_SPLIT_AT, **{"Cor anglais": {27.0: [31.3]}, "Horn 4": {720.0: [721.6, 724.3, 725.9]}})
# critic C #3b / A #1 (combined, simulated on the c09 stems): Horn 1's tenuto F4 at 189 blooms 10 dB inside the note
# (note trim -6 plus -2.5 over 190.0-190.95); the < arrivals 191/591 (+3 dB note trims) take a 0.25 s ramp so the trim is
# there on the arrival's first beat; the unmarked 192/592 downbeats lose their c06 lifts (they were the phrases' loudest
# beats, over the printed crest at 196/596)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(189.9, 0.0), (190.1, -2.5), (190.85, -2.5), (190.95, 0.0)]]
NOTE_TRIM_RAMP_S["Horn 1"] = {**NOTE_TRIM_RAMP_S["Horn 1"], 191.0: 0.25, 591.0: 0.25}
# c10 stem fix: Trumpets 1-2 still fell 1.1-1.2 dB over 632.3-635.5 with the -3 dB start (the Trumpet 1 F5 pitch trim
# -6 -> -2 raised the hairpin's first notes): -5.5 dB at the start for them
for tn_ in ("Trumpet 1", "Trumpet 2"):
    LEVEL_SHAPES[tn_] = [s_ if s_ != [(631.9, 0.0), (632.3, -3.0), (635.4, 0.0)] else [(631.9, 0.0), (632.3, -5.5), (635.4, 0.0)]
                         for s_ in LEVEL_SHAPES[tn_]]
