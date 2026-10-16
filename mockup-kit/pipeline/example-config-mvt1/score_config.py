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

# ---------- c11 ----------
# critic C #2 (step 1): every automatic re-bow point as it stood in the c10 build (parts.json `rebows`, after
# space_rebows), listed so that tempo changes no longer move them (rebow_fills.json and NOTCH_SKIP are keyed to these qn;
# a note with listed points takes no automatic points)
_REBOW_FROZEN = {
    'Violins I': [44.835, 48.597, 711.855, 722.781, 724.465, 726.511],
    'Violins II': [20.928, 25.503, 28.878, 32.878, 46.532, 49.128, 189.62, 714.517, 717.129, 720.532, 723.311, 724.779, 726.396],
    'Violas': [22.537, 24.863, 30.034, 32.364, 34.694, 36.856, 39.353, 52.384, 686.694, 699.507, 713.984, 716.517, 718.925, 721.333, 725.52, 726.816],
    'Violoncellos': [12.163, 13.891, 21.442, 26.516, 29.383, 31.393, 33.403, 37.377, 39.879, 41.38, 45.371, 49.683, 51.87, 152.461, 163.877, 169.146, 289.145, 293.758, 298.37, 713.449, 715.544, 717.638, 719.483, 721.869, 723.921, 725.21, 727.116],
    'Double basses': [13.381, 17.953, 22.003, 26.003, 30.571, 34.003, 38.003, 42.003, 46.003, 50.337, 52.92, 166.01, 292.0, 297.045, 470.813, 477.615, 484.105, 489.716, 495.114, 500.512, 506.408, 512.159, 714.671, 718.171, 720.004, 722.671, 724.803, 726.078],
}
REBOW_AT = {t_: sorted(set(REBOW_AT.get(t_, [])) | set(p_)) for t_, p_ in _REBOW_FROZEN.items()}
# critic C #2 (step 2): the Lento (56 beats), the transition (bars 33-44, 48 beats) and Tempo I (12 beats) ran at one
# constant tempo; arcs as the rest of the movement has had since c04/c08 (the Lento's last arc slows into the Allegro)
PHRASE_ARCS = PHRASE_ARCS + [(0, 16, "sub"), (16, 36), (36, 48), (48, 56, "main"), (128, 144), (144, 160, "sub"),
                             (712, 724, "sub")]
TEMPO_PUSH = TEMPO_PUSH + [(36, 46, 1.015)]
# critic C #1: arc ends on rhythmic figures. Bar 72's three hammer strokes came 0.501/0.541/0.476 s apart (the "main"
# arc ended mid-bar): the arc ends at 284 and beats 284-285 are held at x0.95, so the strokes are even and the third
# lands at 126. Bar 32's sixteenth run at 110.9 into the ff at 126: "sub". The arcs before the sub. p animandos of bars
# 62 and 156 slowed to 103-107.5 and the animando then jumped +11.6%: "open" (push only, no slowing; tools/score_to_parts)
# (actor: "open", not C's "sub": a "sub" slowing of beats 282-283 made the violas' slurred eighths 0.25 s long, which
# turned them from Sus MAX into Leg Slur MAX targets: articulation lengths are read on the shaped map without caesuras)
PHRASE_ARCS = [(272, 284, "open") if x_[:2] == (272, 286) else (120, 128, "sub") if x_[:2] == (120, 128)
               else (232, 244, "open") if x_[:2] == (232, 244) else (600, 620, "open") if x_[:2] == (600, 620) else x_
               for x_ in PHRASE_ARCS]
BEAT_STRETCH = {**BEAT_STRETCH, 284.0: 0.95, 285.0: 0.95}
# critic C #3: the hemiola accents of bars 23-25 / 135-137 on Violins II and Violas (abutting Sus MAX quarters, no lead)
# crossed +0.165-0.17 s late against +0.03-0.07 in the winds; every one is followed by a same-pitch quarter, so
# skip_next_same is off
ABUT_LEAD["Violins II"] = {"lead_s": 0.10, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": False,
                           "at": [91.0, 94.0, 97.0, 539.0, 542.0, 545.0]}
ABUT_LEAD["Violas"] = dict(ABUT_LEAD["Violins II"], at=[91.0, 94.0, 97.0, 539.0, 542.0, 545.0, 575.0])
# critic C #4: wind and brass Sus chord changes crossed +0.07-0.105 s (Horns 3/4 with the c07 0.06 s lead +0.015); flute
# and oboe Sus MAX entries had no entry lead (Oboe 2 reached peak - 6 dB at a median +0.166 s)
for t_ in ("Horn 1", "Horn 2", "Trombone 1", "Trombone 2", "Trumpet 1", "Trumpet 2", "Trumpet 3", "Oboe 1", "Oboe 2",
           "Flute 2"):
    ABUT_LEAD[t_] = {"lead_s": 0.05, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}
ENTRY_LEAD_ART_S["Flute"] = dict(ENTRY_LEAD_ART_S["wind"], **{"Sus MAX": 0.04})
ENTRY_LEAD_ART_S["Oboe"] = dict(ENTRY_LEAD_ART_S["Flute"])
# critic C #5: with the string mid entry leads (c07) the timpani strokes came 0.053 s after the strings; with C #4 the
# brass move 0.05 s earlier too
TIMP_DELAY_S = 0.045
# critic A #1: the c10 quarter fills released across the join into the second theme's tenuto (Horn 1 188: +7.2 dB at
# 188.75, -0.2 at 189.25; the tenuto's moved onset 188.888), so the line dipped 4.6-5.6 dB on the master at the tenuto
# the < leads to: the fills run to the tenuto (early_fills.json) and the tenuto trims ramp in over 1.0 s, so the first
# 0.4 s of each tenuto keeps its level and the trim still takes its bloom
for t_, qs_ in [("Horn 1", [189.0, 201.0, 589.0, 601.0]), ("Violoncellos", [189.0, 589.0, 601.0, 685.0]),
                ("Violas", [601.0])]:
    NOTE_TRIM_RAMP_S[t_] = {**NOTE_TRIM_RAMP_S.get(t_, {}), **{q_: 1.0 for q_ in qs_}}
# critic A #2: the sf of bar 20 (Violins I/II, qn 78, after the crescendo of bars 19-20; the only string sf) was a Leg BC
# legato target with the spike inside the transition: Violins II -5.5 dB under the note before, master -0.3. A fresh
# down-bow stroke, and the sf as the crescendo's arrival (spike to ff, then ff - 8)
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violins I": DOWNBOW_STROKE_AT["Violins I"] + [78.0],
                                               "Violins II": DOWNBOW_STROKE_AT["Violins II"] + [78.0]})
SF_ARRIVAL_AT = {**SF_ARRIVAL_AT, 78.0: "ff"}
# (actor) Violins I's stroke follows a Sus MAX eighth (no Leg -> Sus entry lead, as Violins II gets): the abutting lead
ABUT_LEAD["Violins I"] = {"lead_s": 0.06, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": False, "at": [78.0]}
# critic A #3: the violas' p espr. solo of bars 107-108 (qn 424-432) fell 4-9 dB on its tenuto C5 (429): a lead line
# (phrase tops), a fill and a tenuto trim as a step (note_trims.json, early_fills.json, roles.json)
LEAD_SPANS = dict(LEAD_SPANS, Violas=LEAD_SPANS["Violas"] + [(424, 432)])
NOTE_TRIM_RAMP_S["Violas"] = {**NOTE_TRIM_RAMP_S.get("Violas", {}), 429.0: 0.25}
# critic A #4: harp damps by note-off (the patch's 3019 ms release shortened to 200 ms: mix.json env_release_ms); each
# note rings 2.0 s past its written end unless a damp mark (244, 650, 654 m.d., 727) comes first. The c10 volume damp at
# 650 is removed (the note-offs damp now; tail_hold back on)
HARP_RING_S = 2.0
LEVEL_SHAPES["Harp"] = [s_ for s_ in LEVEL_SHAPES.get("Harp", []) if s_[0][0] != 650.0]
# critic B #1: the bar-122 brass lift and string cut (roles to 496) ran on into bar 124, where the flute/oboe/violin G5
# decrescendo carries the line: the brass now fall with their printed decrescendo (roles end at 492.5)
for t_ in ("Trombone 1", "Trombone 2", "Bass trombone"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(492.0, 0.0), (493.0, -3.0), (495.0, -7.0), (496.0, -7.0), (496.3, 0.0)]]
# critic B #3: Horn 4's C3-F3 notes play 10 dB hot at p/mp (note_trims.json): steps
NOTE_TRIM_RAMP_S["Horn 4"] = {**NOTE_TRIM_RAMP_S.get("Horn 4", {}), **{q_: 0.1 for q_ in [
    40.0, 72.0, 76.0, 80.0, 440.0, 620.0, 652.0, 88.0, 412.0, 415.0, 416.0, 418.0, 660.0, 152.0, 624.0, 648.0, 224.0, 240.0]}}
# critic B #5: bars 13-14: the violins' and flute's held G5 decrescendo fell only 2.3 dB and covered Horn 1's mp solo
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(48.0, 0.0), (49.0, -2.0), (50.0, -4.5), (51.5, -6.0), (52.2, -6.0), (52.5, 0.0)]]
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES.get("Flute 1", []) + [[(48.0, 0.0), (49.0, -2.0), (50.0, -4.5), (50.6, -4.5), (51.0, 0.0)]]
# c11 stem fix: SF_ARRIVAL_AT[78] = "ff" applies to every track with an sf at 78, and Violins II was at mp there (no
# crescendo in its part): its sf body sat at ff for two beats, +11..+20 dB over c10 and +10..+14 dB over the note before;
# Violins I's arrival body +10..+12 dB over the bar before (c10 +3..+6). Level shapes bring the attack to about +5 dB over
# the note before and the body back to its printed level (Violins II about mp, Violins I as the c10 arrival + 1 dB). The
# CC11 (ff layer on Violins II) stays as rendered: next cycle, make the arrival per track (only where a crescendo arrives)
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(77.95, 0.0), (78.05, 0.0), (78.3, -1.0), (78.55, -7.0), (78.8, -12.0),
                                                            (80.45, -12.0), (80.6, -2.0), (82.25, -2.0), (82.5, -3.5), (86.0, -3.0),
                                                            (88.0, -2.0), (88.3, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(77.85, 0.0), (77.95, -2.5), (78.25, -4.5), (78.75, -5.0), (79.0, -6.0),
                                                          (80.3, -6.0), (80.5, -4.0), (80.75, -2.0), (81.0, -1.0), (81.5, 0.0)]]

# ---------- c12 ----------
# critic A #1: the felt timpani Rls row crossfades eight dynamic layers on CC1 (V1 full at CC1 0-9, V2 23-26, V3 38-41,
# V4 54-58, V5 71-73, V6 86-90, V7 102-105, V8 118-127; read from Timpani Flt KS.oib); the track had no CC1 lane, so
# every roll played one loud layer. CC1 from the printed dynamic, ppp..fff on the layer centres
TIMP_CC1_MAP = [(22, 5), (34, 24), (46, 40), (58, 56), (72, 72), (88, 88), (114, 104), (124, 122)]
# (c12 first render: the layers are recorded at their own level. Against c11 (which played V8) the rolls measured ppp
# -40.7 dB (V1; the opening roll -87 dB, the attack probe's "silent"), pp -22, p -23, mf -8.3, f -7.3, ff -3.7, fff 0,
# beyond what CC7 and the volume envelope (+6 dB at most) can restore. Second step: ppp-pp on V4 (CC1 56), p 60, mp 66,
# mf V5, f V6, ff V7, fff V8 (1-8 kHz share measured V4 about -31, V5 -21.5, V6 -22, V7 -16.6, V8 -13 dB), and the
# lost level back in the volume envelope on the rolls (TIMP_ROLL_TRIM_DB, estimated from those layer deficits; refit
# on the second render by stem fix)
TIMP_CC1_MAP = [(22, 56), (34, 56), (46, 60), (58, 66), (72, 72), (88, 88), (114, 104), (124, 122)]
TIMP_ROLL_TRIM_DB = [(22, 17.0), (34, 17.0), (46, 15.0), (58, 12.0), (72, 9.0), (88, 7.3), (114, 3.7), (124, 0.0)]
# c12 stem fix (second render, roll body level against c11 by starting printed CC: ppp -0.6, pp -2.3, p -3.8, mp -0.7,
# mf -0.5, f 0.0, ff -0.1, fff 0.0 dB)
TIMP_ROLL_TRIM_DB = [(22, 17.6), (34, 19.0), (46, 18.6), (58, 12.7), (72, 9.5), (88, 7.3), (114, 3.7), (124, 0.0)]
# critic A #2: tongued wind/brass note changes get a short gap (they crossfaded like the slurs next to them)
WIND_DETACH = {"gap_s": 0.05, "frac": 0.12}
# (c12 first render: winds' tongued holes -3.6 -> -5.7 dB against -4.1 slurred, but brass only -3.0 -> -4.0 against -3.7
# slurred: the brass release and hall fill 0.05 s, as with the horn repeats (c07). Brass: 0.09 s, at most 0.18 of the note)
WIND_DETACH["by"] = {"brass": {"gap_s": 0.09, "frac": 0.18}}
# critic A #3: tenuto phrase tops 2-6 dB under the note before (note_trims.json): steps
for t_, qs_ in [("Horn 1", [413.0]), ("Violas", [436.0, 589.0, 429.0]), ("Flute 1", [436.0]), ("Bassoon 1", [413.0])]:
    NOTE_TRIM_RAMP_S[t_] = {**NOTE_TRIM_RAMP_S.get(t_, {}), **{q_: 0.1 for q_ in qs_}}
# critic A #5: Trombone 1 repeats at 122/456/492/564 dipped -2.9..+0.2 dB at the 0.06 s gap
WIND_REP_RETONGUE_BY = {**WIND_REP_RETONGUE_BY, "Trombone": {"gap_s": 0.08, "fall_cc": 10}}
# critic B #1: the second theme's dolce hairpins (all untargeted) ratcheted the celli from mf to CC 86-100 and Horn 1
# from mp to 80-94 (their f-ff layers). Targets: each swell crests a little over the printed level and returns to it
DYN["mf-"] = 68
DYN["mf+"] = 78
DYN["f-"] = 84
_t2vc = {184.0: "mf+", 187.5: "mf", 189.0: "mf+", 195.0: "f-", 196.0: "mf+", 201.0: "f-", 204.0: "mf"}
_t2hn = {184.0: "mp+", 187.5: "mp", 189.0: "mp+", 195.0: "mf-", 196.0: "mp+", 201.0: "mf-", 204.0: "mp"}
HP_TARGET_AT = {**HP_TARGET_AT,
                "Vc": {**HP_TARGET_AT["Vc"], **_t2vc, **{k_ + 400: v_ for k_, v_ in _t2vc.items()}},
                "Hn1": {**HP_TARGET_AT.get("Hn1", {}), **_t2hn, **{k_ + 400: v_ for k_, v_ in _t2hn.items()}},
                "Vla": {**HP_TARGET_AT.get("Vla", {}), **{k_ + 400: v_ for k_, v_ in _t2vc.items()}}}
# critic B #3: the final chord's celli fell 9.0 dB from bar 180 to 182 (violins 4-5): level shapes, re-bows untouched
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(721.5, 0.0), (722.3, 3.0), (724.0, 4.0), (728.6, 4.0), (729.0, 0.0)]]
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [[(722.0, 0.0), (723.0, 1.5), (728.6, 1.5), (729.0, 0.0)]]
# critic B #6: the f/ff timpani strokes at 125 and 284 were the loudest stem by 4.5-5.4 dB: steps on the stroke (it
# sounds TIMP_DELAY_S after the score onset), held to the next stroke
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(124.97, 0.0), (125.0, -2.0), (127.9, -2.0), (127.95, 0.0)],
                                                     [(283.97, 0.0), (284.0, -2.5), (284.97, -2.5), (285.0, 0.0)]]
# critic C #1: the second theme's first long notes (Horn 1, celli; 184-187.5 <) did not swell (CC11 alone moves the
# level little there): a swell in the volume envelope; the 188/588 quarter fills reduced (early_fills.json) so the
# decrescendo's last note sits under the eighth; Horn 1's 596 C5 grows 4 dB inside its printed decrescendo
for o_ in (0, 400):
    LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(184.25 + o_, 0.0), (187.4 + o_, 3.5), (187.6 + o_, 3.5), (187.85 + o_, 0.0)]]
    LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(184.25 + o_, 0.0), (187.4 + o_, 3.0), (187.6 + o_, 3.0), (187.85 + o_, 0.0)]]
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(596.1, 0.0), (597.9, -4.0), (598.05, 0.0)], [(196.1, 0.0), (197.9, -2.5), (198.05, 0.0)]]
# critic C #3: the tutti decrescendo after the sf of bar 41 (164-168) stayed flat: Horn 1 grew +2.2 dB (an auto fill at
# 165, removed in early_fills.json), Flute 2's G5 bloomed 10 dB inside the sf > of 160-164, Oboe 2 / Clarinet 2 grew
# (c12 first render: master 167-168 3.6 dB under 164-165, Horn 1 only -2.5 dB: -8 instead of -6)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(165.3, 0.0), (167.9, -8.0), (168.05, 0.0)]]
LEVEL_SHAPES["Flute 2"] = LEVEL_SHAPES.get("Flute 2", []) + [[(161.6, 0.0), (162.6, -6.0), (163.9, -8.0), (164.05, 0.0)]]
for tn_ in ("Oboe 1", "Oboe 2", "Clarinet 2"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(164.2, 0.0), (167.9, -4.0), (168.05, 0.0)]]
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(160.6, 0.0), (163.9, -3.0), (164.05, 0.0)]]
# critic C #2 (test, for Dan's ears: bars 131-142): loud brass accents had 2-5 kHz fronts 4.8 dB under the sound before
# them (real orchestra -4.2 front minus body; c11 -9.2): a short CC1 lift (+8 CC1 to +0.10 s, back over 0.10 s) on the
# CC1-layered brass, and the gentle swell full at +0.04 s instead of +0.07 s. No accent sample, no CC11 bump
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass=dict(GENTLE_ACCENT["brass"], cc1_front=(8, 0.10, 0.10), swell_s=(0.04, 0.25, 0.6)))
# (c12 first render: +8 CC1 from the onset moved the brass stems' 2-5 kHz front minus body only -14.5 -> -12.5 dB
# median, the master's -9.2 -> -8.5: the CC1 MidiController in the 1FH/1TP/1TB/1TU layer groups has fadeTime 120 ms.
# Second step: +14 CC1 from 0.05 s before the moved onset, held to +0.10 s, back over 0.15 s)
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass=dict(GENTLE_ACCENT["brass"], cc1_front=(14, 0.10, 0.15, 0.05)))

# ---------- c13 ----------
# c12 test that failed (critic C #2 of c12, A #6 of c13): the brass CC1 front is reverted; the swell timing stays
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass={k_: v_ for k_, v_ in GENTLE_ACCENT["brass"].items() if k_ != "cc1_front"})
# critic A #2: accents played as legato targets sag in the transition for 0.3-0.4 s, which filled the swell's window
# (Horn 1 273 at -1.2 dB under its eighth pickup): the swell is held through the sag on every gentle family
for f_ in ("brass", "wind", "string"):
    GENTLE_ACCENT = dict(GENTLE_ACCENT, **{f_: dict(GENTLE_ACCENT[f_], swell_s_leg=(0.04, 0.35, 0.7))})
# critic A #5: brass eighths got 0.18 x 0.238 = 0.043 s of tonguing gap (holes -3.2 dB, as smooth as slurred -3.8)
WIND_DETACH["by"] = {"brass": {"gap_s": 0.09, "frac": 0.30}}
# critic A #1: the celli's g,1:16 (bars 117-121) is a measured tremolo (MEAS_TREM, generic, on): repeated sixteenths as
# REP_SPLIT strokes; its TREM_JOIN/TREM_SPLIT span goes
TREM_JOIN = {k_: v_ for k_, v_ in TREM_JOIN.items() if k_ != "Violoncellos"}
# critic A #4 (test): the basses' repeated ff eighths of bars 27-31 fold to 1.2-1.8 dB on Sus MAX: the Detache row (key
# 79, not loaded before) over 104-124; bars 131-134 (520-536) are the control
ART_SPANS = {"Double basses": [{"from": 104.0, "to": 124.0, "art": "Detache"}]}
# critic C #3 (test): the key 64 crescendo take is audible only in its last 0.4 s. Key 65 is the longest take (.ews f4
# 11.5-12.1 s against f3 10.2-10.9 s, c01 critic C); with the c01 rule (ring after the peak about constant) its peak
# comes about 1.25 s later, so the lead grows by that much (measure the peak on the c13 render)
PERC_MAP["Suspended cymbal"]["ridecymbal"] = dict(PERC_MAP["Suspended cymbal"]["ridecymbal"], key=65, lead_s=1.50)
# critic A #6: the final-chord horn breath splits re-entered 3-7 dB over the decaying piece for 0.25 s, Horn 3 every
# 2.0-2.3 qn: Horn 3's middle split 724.6 -> 725.0, and -4 dB at each re-entry, back to 0 over about 0.5 s
BREATH_SPLIT_AT = dict(BREATH_SPLIT_AT, **{"Horn 3": {720.0: [722.3, 725.0, 726.6]}})
LEVEL_SHAPES["Horn 3"] = LEVEL_SHAPES.get("Horn 3", []) + [[(722.29, 0.0), (722.31, -4.0), (722.71, 0.0)],
                                                           [(724.99, 0.0), (725.01, -4.0), (725.25, 0.0)],
                                                           [(726.59, 0.0), (726.61, -4.0), (726.85, 0.0)]]
LEVEL_SHAPES["Horn 4"] = LEVEL_SHAPES.get("Horn 4", []) + [[(721.59, 0.0), (721.61, -4.0), (722.02, 0.0)],
                                                           [(724.29, 0.0), (724.31, -4.0), (724.55, 0.0)],
                                                           [(725.89, 0.0), (725.91, -4.0), (726.15, 0.0)]]
# critic A #6: the bar-51 tenuto (Horn 1 + celli) sat 3.0 dB under the quarter before: a step trim on Horn 1 201
# (note_trims.json) and a celli fill (early_fills.json)
NOTE_TRIM_RAMP_S["Horn 1"] = {**NOTE_TRIM_RAMP_S["Horn 1"], 201.0: 0.1}
# critic A #2: pickups that the accent fit could not clear (note_trims.json; steps ending at the accent's moved onset)
NOTE_TRIM_RAMP_S["Bassoon 1"] = {**NOTE_TRIM_RAMP_S.get("Bassoon 1", {}), 520.5: 0.1}
NOTE_TRIM_RAMP_S["Violoncellos"] = {**NOTE_TRIM_RAMP_S.get("Violoncellos", {}), 520.5: 0.1, 316.5: 0.1, 320.5: 0.1, 310.5: 0.1}
# critic C #4: Clarinet 1's accented G5s at 414/422 stood 5 dB over their neighbours (note_trims.json, steps)
NOTE_TRIM_RAMP_S["Clarinet 1"] = {**NOTE_TRIM_RAMP_S.get("Clarinet 1", {}), 414.0: 0.1, 422.0: 0.1}

# critics A #3 / C #2: the Horns 1-2 a2 passages (every onset in both parts the same pitch) on the two-horn KS Master
# (stem 33, appended last) instead of one solo horn sample raised 3 dB (UNI_BOOST). Horn 1 and Horn 2 rest there.
# Windows by Horn 1/2 onsets: 163-165, 272.5-314, 381.5-404, 464-480, 628-643.5, 664.5-676 (the single unison onsets
# 108 and 528 stay on the solo horns). Horn 1's per-onset rules inside the windows are copied to the new track; its
# pitch trims and legato pair/pitch extras (1FH samples) are not
TRACKS = TRACKS + [("Horns a2", ["Hn1"], B + "2 French Horns/06 Keyswitch/2FH KS Master.oib", "brass", -0.42)]
_A2W = [(163.0, 165.5), (272.5, 314.5), (381.5, 404.5), (464.0, 480.5), (628.0, 643.75), (664.5, 676.5)]
TRACK_WINDOWS = {**TRACK_WINDOWS, "Horns a2": (_A2W, True), "Horn 1": (_A2W, False), "Horn 2": (_A2W, False)}
_in_a2 = lambda q_: any(a_ - 1e-6 <= q_ < b_ - 1e-6 for a_, b_ in _A2W)
LEVEL_SHAPES["Horns a2"] = [s_ for s_ in LEVEL_SHAPES.get("Horn 1", []) if _in_a2(s_[0][0] + 0.1) or _in_a2(s_[-1][0] - 0.1)]
NOTE_TRIM_RAMP_S["Horns a2"] = {q_: v_ for q_, v_ in NOTE_TRIM_RAMP_S.get("Horn 1", {}).items() if _in_a2(q_)}
ABUT_LEAD["Horns a2"] = dict(ABUT_LEAD["Horn 1"])
BREATH_GAP_AT["Horns a2"] = {q_: v_ for q_, v_ in BREATH_GAP_AT.get("Horn 1", {}).items() if _in_a2(q_)}
BREATH_FALL_CC["Horns a2"] = {q_: v_ for q_, v_ in BREATH_FALL_CC.get("Horn 1", {}).items() if _in_a2(q_)}
# critic A #6: the celli's bar-51 tenuto starts at +2 dB (the c11 swell to +3 then as before)
LEVEL_SHAPES["Violoncellos"] = [s_ if s_ != [(201.0, 0.0), (202.95, 3.0), (204.2, 3.0), (204.7, 0.0)]
                                else [(200.99, 0.0), (201.03, 2.0), (202.95, 3.0), (204.2, 3.0), (204.7, 0.0)]
                                for s_ in LEVEL_SHAPES["Violoncellos"]]
NOTE_TRIM_RAMP_S["Clarinet 1"] = {**NOTE_TRIM_RAMP_S["Clarinet 1"], 408.5: 0.1}

# ---------- c13 stem fix (level only, measured on the c13 render) ----------
# critic B #5: the [0, 12, 12] + [12, 16, 9, 1] role pair added at their shared boundary (+2.3 dB at qn 12, kit
# section 4) and released the roll a bar early: back to [0, 16, 12] with a -3 dB shape over bar 4
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(12.4, 0.0), (12.9, -3.0), (15.6, -3.0), (15.9, 0.0)]]
# critic A #2: the pickup note trims started at the score onset (the pickups play 0.13-0.26 qn early as legato first
# notes), so they reached only the pickup's last 0.07 qn: exact cuts from the pickup's moved onset to the target's
for t_, sh_ in [("Bassoon 1", [(520.36, 0.0), (520.40, -5.0), (520.86, -5.0), (520.88, 0.0)]),
                ("Violoncellos", [(520.36, 0.0), (520.40, -5.0), (520.765, -5.0), (520.78, 0.0)]),
                ("Violoncellos", [(316.36, 0.0), (316.40, -4.0), (316.765, -4.0), (316.78, 0.0)]),
                ("Violoncellos", [(320.36, 0.0), (320.40, -2.0), (320.765, -2.0), (320.78, 0.0)]),
                ("Violoncellos", [(310.23, 0.0), (310.27, -3.0), (310.765, -3.0), (310.78, 0.0)]),
                ("Clarinet 1", [(408.37, 0.0), (408.41, -2.0), (408.99, -2.0), (409.0, 0.0)])]:
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [sh_]
# critic A #6: the Horn 4 re-entries were dips, not bumps (c12 -1..-5 dB at +0.1 s): its -4 dB shapes deepened them to
# -8: removed. Horn 3's bumps peak at +0.1-0.2 s (+5.3 / +5.6 dB left at 722.3 / 726.6): -6 there
LEVEL_SHAPES["Horn 4"] = [s_ for s_ in LEVEL_SHAPES["Horn 4"] if s_[0][0] not in (721.59, 724.29, 725.89)]
LEVEL_SHAPES["Horn 3"] = [s_ if s_[0][0] not in (722.29, 726.59) else
                          ([(722.29, 0.0), (722.31, -6.0), (722.5, -5.0), (722.75, 0.0)] if s_[0][0] == 722.29 else
                           [(726.59, 0.0), (726.61, -6.0), (726.72, -5.0), (726.85, 0.0)]) for s_ in LEVEL_SHAPES["Horn 3"]]
# critic C #1 stem fix: the bass-octave rows started their 0.5 qn ramp at 636.25 (a row with an end ramp ramps in over
# [q0 - 0.5, q0]), so they lifted the tuba at the 636.66 peak: rows start at 637.25 (roles.json); the bass trombone
# row 2 -> 0.5 dB (Violins I K-level had fallen to about the bass trombone's at 636-644)
# Tests that FAILED on the c13 render (left in so the render matches parts.json; revert in c14):
#  - ART_SPANS Double basses Detache 104-124 (1-8 kHz fold on the eighth grid 1.1 -> 1.3 dB, pass >= 4): revert is a
#    full rebuild of the Double basses (the Detache row is loaded only for it)
#  - PERC_MAP suspended cymbal key 65 / lead_s 1.50: the peak met the crash (+0.02 s, as key 64) but 6-16 kHz was still
#    -64.6 / -38.1 dB under the peak 1.5 / 1.0 s before the crash (pass -30 / -15): back to key 64, lead_s 0.25
#  - WIND_DETACH brass frac 0.30: brass changes with a 0.06-0.075 s gap holed -3.1 dB (slurred -3.5; pass -4.8)

# ---------- c14 ----------
# Reverts of the c13 tests (critic A #5): the basses' Detache row (a full rebuild of the Double basses), the suspended
# cymbal's key 65, the brass WIND_DETACH frac 0.30
ART_SPANS = {}
PERC_MAP["Suspended cymbal"]["ridecymbal"] = dict(PERC_MAP["Suspended cymbal"]["ridecymbal"], key=64, lead_s=0.25)
# critic A #3: brass eighths back to 0.09 s / 0.18 of the note, plus a 10 CC CC11 fall over the note's last 0.10 s
# (CC11 sets the Global Group volume on the Hollywood Brass KS Masters; their layers follow CC1), notes of 0.6 qn or less
WIND_DETACH["by"] = {"brass": {"gap_s": 0.09, "frac": 0.18, "fall_cc": 10, "fall_s": 0.10}}
# ONE_TIME (memory, BRIEF item 9): the c13 render ended at 45 GiB (32 compressed) with 33 instances. Measured with
# `footprint` on a settled session: reloading Violins I/II and the celli with their single-note Leg Port MAX rows (225,
# 685) took REAPER from 46.01 to 46.13 GB; deleting the Crash cymbals instance freed under 0.01 GB. The portamento rows
# stay (PORT_TARGETS unchanged); no percussion merge
# critic A #2 (test): the celli's 80 measured-tremolo strokes cycled the Stac RRx9 round robins in a fixed 9-stroke order
# (autocorrelation 0.71-0.93 at lag 9): CC36 resets in runs of 4-9 strokes
MEAS_TREM = dict(MEAS_TREM, rr_runs=[7, 5, 8, 6, 4, 9, 5, 7, 6, 8, 4, 7, 5, 9])
# critic A #6 (Flute 1's bar-28 accent 2.3 dB under its pickup): the pickup (109.5) is the second note of a two-note slur,
# so SLUR_PAIR_RELEASE already takes it down 2.5 dB; no separate cut
# critic C #1: bar 51's dolce Horn 1 + celli arrival (203) jumped 7.6 / 4.7 dB on one quarter (the Horn 1 envelope steps
# -1.2 -> +5.5 dB at 202.92; the celli's c10 hold +3): Horn 1 -5 over the arrival quarter, the celli hold ends at 203.05
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(202.88, 0.0), (202.95, -5.0), (204.0, -5.0), (204.2, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = [s_ if s_ != [(200.99, 0.0), (201.03, 2.0), (202.95, 3.0), (204.2, 3.0), (204.7, 0.0)]
                                else [(200.99, 0.0), (201.03, 2.0), (202.95, 3.0), (203.05, 0.0)]
                                for s_ in LEVEL_SHAPES["Violoncellos"]]
# critic C #2: the c08 E6 fill held +4 dB over the crescendo's F6/G6 (633-635.4), so the fff of bar 160 arrived 0.0-0.4
# dB over the crescendo's top: the fill lets go after the E6 (the E6 part is unchanged), and the A-flat6 climax note
# takes +2 dB on both violin sections
_e6fill_c14 = [(629.5, 0.0), (631.5, 4.0), (633.9, 4.0), (634.6, 2.0), (635.0, 0.0), (635.9, 0.0)]
_ab6 = [(636.6, 0.0), (636.9, 2.0), (639.2, 2.0), (639.6, 0.0)]
for tn_ in ("Violins I", "Violins II"):
    LEVEL_SHAPES[tn_] = [s_ if s_ != _e6fill else _e6fill_c14 for s_ in LEVEL_SHAPES[tn_]] + [_ab6]
# critic C #3: the ppp morendo final chord rose 1.4 dB inside its fermata (re-bow pieces) and faded only in its last
# second: -3 dB by 726, -7 by 727.5 on every track (the generic end fade stays on top)
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(724.25, 0.0), (726.0, -3.0), (727.5, -7.0), (729.0, -7.0)]]
# critic C #4: the ff after letter G (bars 118-120) sagged 2.5 dB on the master: the held ff parts +2.5 dB, the basses'
# G1 bloom taken back and its tail and re-bow pieces filled (re-bow rows unchanged)
for tn_ in ("Horn 3", "Horn 4", "Horns a2", "Bass trombone", "Tuba", "Contrabassoon", "Violins II", "Bassoon 1",
            "Bassoon 2", "Bass clarinet"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(467.6, 0.0), (468.6, 2.5), (479.6, 2.5), (480.4, 0.0)]]
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [
    [(464.2, 0.0), (464.8, -4.0), (467.4, -4.0), (468.4, 2.0), (469.0, 5.0), (470.7, 5.0), (470.95, 3.0), (483.6, 3.0),
     (484.0, 0.0)]]
# critics C #5 / B #2: the pp Violins II D-flat4 of bar 43 (167.75-172) bloomed 12.8 dB at flat CC11 and covered the
# horns' p phrase; the violas' B-flat3 in the same chord bumped +5 dB at 169.5
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(168.4, 0.0), (169.5, -3.0), (171.0, -6.0), (171.9, -7.5),
                                                            (172.25, -5.0), (172.6, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(169.25, 0.0), (169.5, -4.0), (169.9, -4.0), (170.2, 0.0)]]
# critic C #6: the recapitulation's < of 589-591 arrived 1.2 dB under its crest (the celli sag 4-5 dB on the arrival's
# legato join): a celli fill over the sag and Horn 1 +2.5 on the arrival
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(590.95, 0.0), (591.05, 4.0), (591.5, 4.0), (591.75, 0.0)]]
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(590.9, 0.0), (591.05, 2.5), (591.9, 2.5), (592.1, 0.0)]]
# critic B #4: the Horns a2 window roles now end with the note they cut (roles.json); the bar-79 phrase-end E4 tapers under
# the oboe / violins' entry
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES["Horns a2"] + [[(314.0, 0.0), (314.3, -2.5), (316.0, -5.0), (316.2, 0.0)]]

# ---------- c14 stem fix (level only, measured on the c14 render) ----------
# critic C #1: the bar-51 arrival went from +5.1 to +0.3 dB on the master (pass +1.5..+3.5): Horn 1's cut -5 -> -1.5
LEVEL_SHAPES["Horn 1"] = [s_ if s_ != [(202.88, 0.0), (202.95, -5.0), (204.0, -5.0), (204.2, 0.0)]
                          else [(202.88, 0.0), (202.95, -1.5), (204.0, -1.5), (204.2, 0.0)] for s_ in LEVEL_SHAPES["Horn 1"]]
# critic B #4: Horns a2 still 2.5 dB over Violins I at 314.5-315 (K-weighted; pass -2): a deeper phrase-end taper
LEVEL_SHAPES["Horns a2"] = [s_ if s_ != [(314.0, 0.0), (314.3, -2.5), (316.0, -5.0), (316.2, 0.0)]
                            else [(314.0, 0.0), (314.2, -5.0), (314.6, -7.5), (316.0, -8.0), (316.2, 0.0)]
                            for s_ in LEVEL_SHAPES["Horns a2"]]
# critic C #3: the morendo still rose 0.4 dB at 725.5 (re-bow pieces): a steeper first second
LEVEL_SHAPES["_all"] = [s_ if s_ != [(724.25, 0.0), (726.0, -3.0), (727.5, -7.0), (729.0, -7.0)]
                        else [(724.25, 0.0), (725.0, -1.5), (725.6, -3.2), (726.0, -3.5), (727.5, -7.0), (729.0, -7.0)]
                        for s_ in LEVEL_SHAPES["_all"]]
# the master's top sample peak (1.725 at qn 641.72, the low strings and brass sustaining before the bar-161 change;
# c13 1.587) set a 2.8 dB delivery limiter: -2.5 dB over 641.62-641.78 on the four largest contributors
for t_ in ("Violoncellos", "Tuba", "Trombone 1", "Bass trombone"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(641.55, 0.0), (641.62, -2.5), (641.78, -2.5), (641.83, 0.0)]]
# critic B #3: the basses at bars 27-31 rose about 8 dB, not the planned 4 (Detache revert, role, held loud EQ): bar 27
# 7.3 dB over the celli (K): the role [104, 128, 3, 1] -> 1.5 dB (roles.json)
# Tests that FAILED on the c14 render (left in so the render matches parts.json; replace or revert in c15):
#  - MEAS_TREM rr_runs (CC36 resets inside the music): celli stroke autocorrelation at lag 9 0.71/0.82/0.93 ->
#    0.73/0.85/0.92 (peak / 1-8 kHz / centroid; pass < 0.3): CC36 does not reset the round robin mid-render
#  - WIND_DETACH brass fall_cc 10: brass tongued changes with gaps under 0.06 s -3.1 -> -3.5 dB (pass -5.0); CC11 moves
#    about 1 dB per 10 CC at f/ff: a dB dip in the volume envelope is the next thing to try

# ---------- c15 ----------
# Reverts of the failed c14 tests: the CC36 resets inside the celli's measured tremolo (MEAS_TREM rr_runs) and the brass
# WIND_DETACH CC11 fall (fall_cc 10)
MEAS_TREM = {k_: v_ for k_, v_ in MEAS_TREM.items() if k_ != "rr_runs"}
# critic A #4 (test): the 80 measured-tremolo strokes (celli G2, bars 117-121) alternate between Stac RRx9 and the
# Stac On Bow RRx9 row (key 28, loaded for this; a full rebuild of the celli), seeded, about 45% Stac On Bow, no row more
# than 3 strokes in a row. alt_db (the rows' level offset) is set from the c15 render
MEAS_TREM = dict(MEAS_TREM, alt_row="Stac On Bow RRx9", alt_share=0.45, alt_seed=464, alt_max_run=3, alt_db=0.0)
# critic A #3: brass tongued note changes with a played gap under 0.07 s holed -3.5 dB, as slurred: a -4 dB volume dip
# from the note's end - 0.05 s to the next moved onset (simulated on the c14 stems: holes -5.5, master -0.1 dB)
WIND_DETACH["by"] = {"brass": {"gap_s": 0.09, "frac": 0.18, "dip_db": -5.0, "dip_fall_s": 0.05, "dip_min_cc": 84}}
# critic A #2 (test): a slur's short first note after a tongued note on the Sus row; the second note joins from it
SLUR_START_SUS = {"families": ("wind", "brass"), "max_qn": 0.6, "after_qn": 0.15}
# critic C #2 (test): unled wind/brass re-attacks after short gaps (median brass +0.104 s, winds +0.081; strings
# +0.048): a re-tongue lead per track, family values last (by_name takes the first track key contained in the name)
RETONGUE_LEAD_S = {"Horn 1": 0.09, "Horn 2": 0.09, "Trumpet 2": 0.08, "Trumpet 3": 0.08, "Tuba": 0.07, "Oboe 2": 0.08,
                   "Cor anglais": 0.08, "Oboe 1": 0.05, "brass": 0.05, "wind": 0.035}
# critic C #3: f/ff wind and brass entries at the tutti downbeats reached body - 3 dB at +0.12..+0.23 s: loud entry
# leads per track (soft, loud, mid); Oboe 2 / Flute 2 get loud-only values on top of their Sus MAX articulation lead
# (0.04), so their soft entries keep the old lead
ENTRY_LEAD_S = {"Horn 1": (0.10, 0.12, 0.05), "Horn 2": (0.10, 0.10, 0.05), "Trumpet 2": (0.10, 0.11, 0.05),
                "Trumpet 3": (0.10, 0.12, 0.05), "Trombone 1": (0.10, 0.11, 0.05), "Bassoon 1": (0.06, 0.12, 0.06),
                "Oboe 2": (0.0, 0.08, 0.0), "Flute 2": (0.0, 0.06, 0.0), **ENTRY_LEAD_S}
# critic C #5: unison hand-overs (Oboe 2 628, Horn 3 418) re-attacked 0.45 s after the beat: a longer overlap and a fade-in
UNI_DELAY_OVERLAP_QN, UNI_DELAY_FADE = 0.25, (-12.0, 0.2)
# critic C #1: the Allegro's first downbeat (celli f half note, qn 56) reached body - 3 dB at +0.33 s on Leg Slur MAX:
# a fresh Sus MAX stroke (58 joins as a Leg BC target), the envelope held at -5 dB from the moved onset
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violoncellos": DOWNBOW_STROKE_AT["Violoncellos"] + [56.0]})
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(55.94, 0.0), (55.96, 2.5), (56.5, 1.25), (57.0, 0.0)]]
# critic A #5: the violas' accented A-flat4 at 120 (a Leg BC target) carried a fitted -6 dB step (the fit read the
# transition peak as the accent) and sat 9.7 dB under its pickup: fit removed, +3 dB step trim (note_trims.json)
NOTE_TRIM_RAMP_S["Violas"] = {**NOTE_TRIM_RAMP_S.get("Violas", {}), 120.0: 0.1}
# critic B #5: Trumpet 2's pp G4 at bar 113 entered 7 dB under Trumpets 1 and 3: +4 dB step (note_trims.json)
NOTE_TRIM_RAMP_S["Trumpet 2"] = {**NOTE_TRIM_RAMP_S.get("Trumpet 2", {}), 448.0: 0.1}
# ---------- c15 stem fix (level only, measured on the c15 render) ----------
# critic A #3: brass short-gap holes -4.9 dB where dipped (-4.4 over all 87; pass -5): the dip -4 -> -5 dB (above)
# critic C #1: the Double basses' 220 entry fill overshot its body by 5 dB at +0.4 s: removed (early_fills.json)
# critic B #1: Horn 2's F4 at bar 57 (224) still 4 dB over the Violins I melody with the pitch trim: -3 dB step
NOTE_TRIM_RAMP_S["Horn 2"] = {**NOTE_TRIM_RAMP_S.get("Horn 2", {}), 224.0: 0.1}
# critic A #5: Violas 120 stood +5.2 dB over its pickup with the +3 dB step (pass 2-4): +1.5 (note_trims.json)
# accent_fits.json refit on the c15 render after the fixes above (brass 32/37, winds 126/142, strings 105/135 predicted in
# 2-4 dB; fit_accents.py no longer puts negative steps on legato targets moved more than 0.05 s early)
