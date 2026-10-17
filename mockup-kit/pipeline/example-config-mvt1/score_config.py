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

# ---------- c16 ----------
# critic A #1 (test): the main motive's eighth pickup after a rest played the Leg rows' slow first-note layer (pickup
# peak minus target body: winds Leg -8.6 dB, strings Leg -3.1, brass Leg -6.7; Violins I bar 35 -10.6 / -21.3 on its
# own sounding time; 12 of the 15 accents arriving at +0.20 s or later are their targets). Pickups after a rest on the
# Sus row, joined into the target (the SLUR_START_SUS join); strings -2.5 dB over the pickup (Sus over Leg at one CC11)
PICKUP_SUS = {"families": ("wind", "brass", "string"), "max_qn": 0.62, "rest_qn": 0.2, "min_target_qn": 0.5,
              "level_db": {"string": -2.5, "wind": 0.0, "brass": 0.0}}
# c16 stem fix: string pickups still a median -0.5 dB under their targets (15 of 28 over -1; pass -2..-5): -3.5 dB
PICKUP_SUS["level_db"] = dict(PICKUP_SUS["level_db"], string=-3.5)
# critic A #3: SLUR_START_SUS second notes (0.12-0.26 s) peaked +3.0 / +3.5 dB (winds / brass) over the first note's
# body: on short second notes the release starts at the moved onset, -3 dB on joined second notes
SLUR_PAIR_RELEASE = dict(SLUR_PAIR_RELEASE, short_s=0.35, full_short_s=0.12, join_db=-3.0)
# critic A #5: the basses' bar-72 hammer strokes (284 -> 285): the entry lead closed the 0.25 qn detach gap to 0.011 qn
DETACH_LEAD_KEEP_QN = 0.15
# critic A #5: Oboe 1's slur after the accented B-flat5 of bar 79 (314.5-316) sat 8-12 dB under the accent's body
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(314.37, 0.0), (314.39, 3.0), (315.95, 3.0), (316.0, 0.0)]]
# critic C #1: the c14 letter-G lift (+2.5 dB on ten held ff parts, 468.6-479.6) fell back to 0 at 480.4, the start of
# bar 121's printed crescendo, and the 484 arrival held the crescendo's top back 1.5 dB: bar 121 started 0.2 dB under
# bar 120 and the fff arrived as a +5.2 dB step. The lift is held and grows +1.5 dB through the crescendo
_lg_old = [(467.6, 0.0), (468.6, 2.5), (479.6, 2.5), (480.4, 0.0)]
_lg_new = [(467.6, 0.0), (468.6, 2.5), (479.6, 2.5), (483.5, 4.0), (484.0, 0.0)]
for tn_ in ("Horn 3", "Horn 4", "Horns a2", "Bass trombone", "Tuba", "Contrabassoon", "Violins II", "Bassoon 1",
            "Bassoon 2", "Bass clarinet"):
    LEVEL_SHAPES[tn_] = [_lg_new if s_ == _lg_old else s_ for s_ in LEVEL_SHAPES[tn_]]
ARRIVAL_WEIGHT_AT = {**ARRIVAL_WEIGHT_AT, 484.0: (-0.5, 1.5, 0.5)}
# critic C #4: the second theme's first dolce note (Horn 1 + celli, 184-187.5 <) rose only +0.4 / +0.2 dB: the linear
# c12 ramp offset the sample's 2.3 dB mid-note decay. A front-loaded swell to +5.5 (celli +5.0)
for o_ in (0, 400):
    _o12h = [(184.25 + o_, 0.0), (187.4 + o_, 3.5), (187.6 + o_, 3.5), (187.85 + o_, 0.0)]
    _o12c = [(184.25 + o_, 0.0), (187.4 + o_, 3.0), (187.6 + o_, 3.0), (187.85 + o_, 0.0)]
    LEVEL_SHAPES["Horn 1"] = [[(184.25 + o_, 0.0), (185.0 + o_, 1.5), (186.0 + o_, 4.0), (187.4 + o_, 5.5), (187.6 + o_, 5.5),
                               (187.85 + o_, 0.0)] if s_ == _o12h else s_ for s_ in LEVEL_SHAPES["Horn 1"]]
    LEVEL_SHAPES["Violoncellos"] = [[(184.25 + o_, 0.0), (185.0 + o_, 1.4), (186.0 + o_, 3.6), (187.4 + o_, 5.0),
                                     (187.6 + o_, 5.0), (187.85 + o_, 0.0)] if s_ == _o12c else s_
                                    for s_ in LEVEL_SHAPES["Violoncellos"]]
# critic C #5 rejected: on the c15 stem the on-beat and off-beat eighths of 664-676 differ by -0.7 dB (RMS, first
# 0.2 s; off-beats louder) and +2.4 dB in 50-140 Hz only, not 5 dB; a -2 dB on-beat step would reverse the metre
# critics B #3 / C #2: the cor anglais' p espr. solo of bars 5-8 sat under the sum of its accompaniment (-0.1..-0.6 dB,
# c00 +2..+3.8) and 6.4 dB under the celli's crest at 27-28: +3 dB to 27, +1.5 over the held G4 and the pp re-entry
# (B's +2.5 there halved: C asks to leave bars 7-8 to the strings' printed < p >, whose swell B cuts by 2-2.5 dB in
# roles.json); the celli's re-bow at 26.516 lost its two late bumps (rebow_fills.json). C's +3 simulated the solo
# +6 dB over the sum of the other stems at 19-21 with the basses' cut: +2
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [
    [(19.0, 0.0), (19.5, 2.0), (27.0, 2.0), (27.5, 1.5), (31.0, 1.5), (32.0, 0.0)]]
# critic A #2: bar 51's tenuto C5 (Horn 1 201, led 0.20 s since c15) opened with a 10 dB hole (c15 stem -42..-47 dB
# at -0.04..+0.04 s against the E-flat's -36). The critic's fill/trim change, simulated on the c15 stems, overshot by
# 6 dB at -0.12 s and left the note 5-7 dB low at +0.12..+0.3 s, so the c15 data stays and an exact shape fills the
# hole as measured (seconds from the score onset: 0 at -0.10, +6 at -0.04, +8 at 0, +6 at +0.04, +3 at +0.08, +2.5 at
# +0.30, 0 at +0.40); the celli's fill starts full 0.12 s before the score onset (0.16 overshot 5 dB in the simulation)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(200.8133, 0.0), (200.9253, 6.0), (201.0, 8.0), (201.0728, 6.0),
                                                    (201.1455, 3.0), (201.5457, 2.5), (201.7276, 0.0)]]
# ---------- c16 stem fix (level only, measured on the c16 render) ----------
# string pickups -2.5 -> -3.5 dB (PICKUP_SUS level_db, above); the brass theme pickups' +3 dB note trims back
# (note_trims.json); accent_fits.json refit on c16 (brass 34/37, winds 125/141, strings 103/135 predicted in 2-4 dB)
# Test that FAILED on the c16 render (left in so the render matches parts.json; revert in c17):
#  - PICKUP_SUS: the exposed pickups after a rest stayed 8.5-11.7 dB under their targets (Violins I 136.5 -11.0, Bass
#    clarinet 304.5/432.5 -8.5/-10.7, Oboe 1 312.5 -11.7; pass -6..-1): the mf first note after silence rises as slowly
#    on Sus as on Leg. Revert = PICKUP_SUS None, then refit accent_fits.json (the targets' fits moved with it)

# ---------- c17 ----------
# c16 test reverted (critic A #1): PICKUP_SUS off (the pickups play their c15 rows again; the string -3.5 dB goes with it)
PICKUP_SUS = None
# critic A #1: the theme's pickups after a rest sit on their samples' quiet first-note plateau, 4-18 dB under their
# targets (envelope removed; c15 Leg rows and c16 Sus rows within 1.7 dB of each other), so no lead or row fixes them:
# exact lifts = clip(-(mean c15/c16 deficit) - 2, 0, 10) dB, from the pickup's moved onset to its target's moved onset.
# They replace the +3 dB note trims on Trumpet 1 664.5/672.5 and Horns a2 664.5 (note_trims.json)
PICKUP_LIFT = {
    "Oboe 1": {312.5: 10.0},
    "Violins I": {136.5: 10.0, 312.5: 6.9, 72.5: 5.4, 148.5: 3.3, 144.5: 2.9},
    "Oboe 2": {408.5: 9.3},
    "Trumpet 1": {672.5: 9.6, 664.5: 8.9},
    "Horns a2": {664.5: 7.4, 310.5: 4.7},
    "Trombone 1": {520.5: 6.2},
    "Violas": {132.5: 6.8, 146.5: 6.8},
    "Bass clarinet": {304.5: 6.4, 432.5: 5.2},
    "Clarinet 1": {504.5: 6.2, 416.5: 5.1, 272.5: 3.8},
    "Flute 1": {552.5: 5.6, 104.5: 5.5},
}
# critic A #3: the Allegro's off-beat string syncopes (r8 + eighth tied to a quarter, mf) swelled +8 dB from their start
# to their last 0.2 s and crested on the next downbeat: weight at the start, then a slight taper
SYNCO_SHAPE = {"families": ("string",), "min_bpm": 100, "rest_qn": 0.25, "len_qn": (0.75, 2.0),
               "pts": [(-0.12, 6.0), (0.10, 6.0), (0.25, 3.0), (0.45, 0.0), (0.60, -3.0)]}
# ---------- c17 stem fix (level only, measured on the c17 render) ----------
# critic A #1 pass is each lifted pickup -6..-2 dB under its target's 200 ms peak and not over the target's body:
# lifts moved toward -4 dB (cap 12) where the render measured outside the range (Violins I 136.5 -12.2 and Oboe 1
# 312.5 -9.0 at 10 dB; Flute 1 104.5 -1.7, Trumpet 1 672.5 -0.8, Trombone 1 520.5 -1.6, Horns a2 664.5 +1.4 over its body)
PICKUP_LIFT["Flute 1"].update({104.5: 3.2, 552.5: 8.0})
PICKUP_LIFT["Oboe 1"].update({312.5: 12.0})
PICKUP_LIFT["Clarinet 1"].update({272.5: 1.8, 416.5: 7.3, 504.5: 9.5})
PICKUP_LIFT["Bass clarinet"].update({432.5: 8.2})
PICKUP_LIFT["Trumpet 1"].update({664.5: 6.9, 672.5: 6.4})
PICKUP_LIFT["Trombone 1"].update({520.5: 3.8})
PICKUP_LIFT["Violins I"].update({136.5: 12.0})
PICKUP_LIFT["Horns a2"].update({664.5: 5.2})

# ---------- c18 ----------
# critic C #1: letter G (bar 117): the ff tutti arrived 1.1-2.0 dB under the six-bar crescendo's top because the c14/c16
# hold on the ten held ff parts started at 467.6 (full 468.6), one bar after the arrival. It starts at the arrival now
# (+3 dB at 464.05) and adds 1.5 dB through bars 118-120 (the critic's +1 simulated bar 119 2.4 dB under 117); the
# 483.5-484 end and ARRIVAL_WEIGHT_AT 484 are unchanged
_lg_c18 = [(463.9, 0.0), (464.05, 3.0), (467.6, 3.0), (468.6, 4.0), (479.6, 4.0), (483.5, 4.0), (484.0, 0.0)]
for tn_ in ("Horn 3", "Horn 4", "Horns a2", "Bass trombone", "Tuba", "Contrabassoon", "Violins II", "Bassoon 1",
            "Bassoon 2", "Bass clarinet"):
    LEVEL_SHAPES[tn_] = [_lg_c18 if s_ == _lg_new else s_ for s_ in LEVEL_SHAPES[tn_]]
# critic C #2: bars 127-129 (pp < mf, then f < ff): Clarinet 1's p solo started 8-11 dB hot (roles, pickup lift, accent
# fit) and fell after its mf (the c06 shape took 3 dB away at 513-514): -3 dB at its start easing to 0 by the mf, and the
# mf line held +4.5 dB through the f crescendo to 520.3 (before the ff at 520.5); the celli eighths that carry the
# crescendo (508-512) rise +2 -> +4 dB. The pickup lift up to 505.0 is untouched
LEVEL_SHAPES["Clarinet 1"] = [s_ if s_ != [(504.5, 0.0), (512.0, 3.0), (513.0, 3.0), (514.0, 0.0)]
                              else [(504.5, 0.0), (512.0, 3.0), (514.0, 4.5), (519.5, 4.5), (520.3, 0.0)]
                              for s_ in LEVEL_SHAPES["Clarinet 1"]]
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(504.95, 0.0), (505.05, -3.0), (508.0, -2.0), (511.0, -0.5),
                                                            (512.0, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(507.7, 0.0), (508.0, 2.0), (511.7, 4.0), (511.95, 0.0)]]
# critic C #3: Lento bar 3: the low strings' second swell (qn 8-10, pp <) held a 7 dB master hole about 1 s into it
# (celli -13 dB, the same in c15-c17: the samples settle 1.0-1.3 s after their 8.0 notes begin), and the celli's fill
# and loop fill ended 0.35 s before the sample's dip did. Fills over the dip on celli, basses and bass clarinet; the
# celli loop fill "8.0" 5 -> 3 dB (loop_fills.json)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(8.74, 0.0), (8.82, 7.0), (9.2, 7.0), (9.32, 3.0), (9.45, 0.0)]]
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(8.7, 0.0), (8.82, 3.5), (9.0, 3.5), (9.15, 0.0)]]
LEVEL_SHAPES["Bass clarinet"] = LEVEL_SHAPES.get("Bass clarinet", []) + [[(8.7, 0.0), (8.8, 3.0), (9.0, 3.0), (9.12, 0.0)]]
# critic C #4: Bassoon 1's bar-34 solo: the C4 at 131.5 (inside the f > mf) jumped 4.2 dB over the note before (role +3
# plus the 5.3 dB early fill held to +0.1 s): -4.5 dB from just after its onset; the fill's part before the onset, which
# covers the join hole, stays
LEVEL_SHAPES["Bassoon 1"] = LEVEL_SHAPES["Bassoon 1"] + [[(131.47, 0.0), (131.55, -4.5), (131.75, -4.5), (132.24, 0.0)]]
# c18 stem fix: the render's 131.5 quarter still stood 2.2 dB over 131.0-131.5 (simulated -0.2; the sample varies
# between renders): -4.5 -> -6.5 dB
LEVEL_SHAPES["Bassoon 1"] = [s_ if s_ != [(131.47, 0.0), (131.55, -4.5), (131.75, -4.5), (132.24, 0.0)]
                             else [(131.47, 0.0), (131.55, -6.5), (131.75, -6.0), (132.24, 0.0)] for s_ in LEVEL_SHAPES["Bassoon 1"]]
# critic A #3: the recapitulation violas' off-beat dyads at 526.5-534.5 (every second one) end with a release burst 3-5 dB
# over their own body 0.03-0.09 s after the note-off (deterministic: c16 = c17 within 0.2 dB; the F4's energy): a -6 dB
# notch from the moved note-off - 0.01 qn to + 0.22 qn (note-offs 527.0 ... 535.0), 0.02 qn ramps (the critic's -5 dB
# to + 0.20 simulated 526.5 / 534.5 still +1.5 / +2.2 dB over their body)
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(e_ - 0.03, 0.0), (e_ - 0.01, -6.0), (e_ + 0.22, -6.0), (e_ + 0.24, 0.0)]
                                                   for e_ in (527.0, 529.0, 531.0, 533.0, 535.0)]
# critic A #2: bar 70's doubled f melody fell 3.5-5 dB on beat 4 (qn 279): Trumpet 1's 277 -> 279 legato join plays a
# transition spike 9 dB over the F5's body (peak 0.15 s before the beat): a -6 dB notch over it (positions of c16 and
# c17, to 279.0: simulated on c17, the spike's last frames at 278.94 stood 3.5 dB over the F5 with the critic's end
# 278.92); the Violins I E-flat6 (a passing step inside the slur at one f) releases -1 dB instead of -2.5
JOIN_NOTCH = dict(JOIN_NOTCH, **{"Trumpet 1": JOIN_NOTCH.get("Trumpet 1", []) + [(278.45, 279.0, -6.0)]})
SLUR_PAIR_RELEASE_DB_AT = {"Violins I": {279.0: -1.0}}
# critic A #2: the three repeating Violins I legato holes (c16 = c17) as exact fills, in seconds from the moved onset
# (Violins I is not an auto_fills track): 279 (bar 70, F6 -> E-flat6, hole +0.15..+0.50 s, 6.6 dB) +5 dB 0.17-0.42 s;
# 626 (bar 157, one 50 ms 6 dB dip at +0.05 s, the rest 2-3 dB) +5 at 0.04-0.09 s, +2 to 0.40 s; 720 (the final ppp,
# hole +0.23..+0.82 s, 8 dB) +7 dB 0.27-0.37 s. Each ends before the next note's transition (626 spikes at +0.51 s)
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [
    [(278.895, 0.0), (279.0, 5.0), (279.5254, 5.0), (279.6304, 0.0)],
    [(625.666, 0.0), (625.7445, 5.0), (625.8427, 5.0), (625.941, 2.0), (626.4527, 2.0), (626.5513, 0.0)],
    [(719.983, 0.0), (720.0413, 5.0), (720.083, 7.0), (720.1663, 7.0), (720.233, 3.0), (720.2913, 0.0)]]

# ---------- c19 ----------
# critic C #1: GENTLE_ACCENT wind/brass accents (plain Sus rows) played from the score onset with no lead (the c26 rule
# was written for the fast Sus Accent samples): unled accents arrived +0.107 s (brass) / +0.095 (winds) after the
# score onset against +0.045 for led notes, on the tutti hammer chords. ACC_ART_LEAD (generic, True) lets them take the
# re-tongue / entry leads; swells and CC11 stay on score time
# critic C #2: unled string Sus MAX strokes after a slur or a short gap (bar 72's hammer strokes 285/286 +0.14..+0.23 s,
# Violins I/II +0.12/+0.09 median, sample only): the re-tongue lead for strings (generic rule, string value here)
# (upper strings and celli only: the basses' repeated eighths are on time with ABUT_LEAD, c07; "Violins II" before
# "Violins I", which by_name would also match in "Violins II")
RETONGUE_LEAD_S = dict(RETONGUE_LEAD_S, **{"Violins II": 0.10, "Violins I": 0.10, "Violas": 0.10, "Violoncellos": 0.10})
# critic C #3: the first-theme Violins I slur heads (Sus MAX eighths, D-D-flat-C) sounded 0.065-0.08 s before the led
# Leg Slur target took over: the head starts with its target (SLUR_HEAD_LEAD, generic)
SLUR_HEAD_LEAD = {"string": True}
# critic C #4: Oboe 2 led notes arrived +0.104 s (other winds +0.046): loud entry lead 0.08 -> 0.14 s, re-tongue 0.08 ->
# 0.12 s; the Leg Slur entry extra stays 0.055 s (the critic's 0.16, and 0.10, on top of the 0.14 loud lead filled the
# eighth rest before 416.5 to 0.02 qn);
# Oboe 1's Leg Slur re-attacks after slur breaks (+0.21..+0.23 s, re-tongue lead 0.05 s) get +0.08 s on that row.
# "Oboe 2" goes before "Oboe" (by_name takes the first track key contained in the name)
ENTRY_LEAD_S = dict(ENTRY_LEAD_S, **{"Oboe 2": (0.0, 0.14, 0.0)})
RETONGUE_LEAD_S = dict(RETONGUE_LEAD_S, **{"Oboe 2": 0.12})
RETONGUE_LEAD_ART_S = {"Oboe 1": {"Leg Slur MAX": 0.08}}
# critic C #5: the recapitulation's poco rit. (bars 145-146) started a bar early (the "sub" arc slowed bar 144) and held
# 120 through bar 145: "open" (push only) and the ramp from 126, as bar 45 (176, 184, 126). The c07 reason for "sub"/120
# (no speed-up inside the rit.) holds: the open arc only pushes before 576 and the ramp falls from 126
PHRASE_ARCS = [x_ if x_[:2] != (568, 576) else (568, 576, "open") for x_ in PHRASE_ARCS]
RAMP_SPANS = [(576, 584, 126) if r_[:2] == (576, 584) else r_ for r_ in RAMP_SPANS]
# critic A #1: accented string notes on Leg BC MAX (the bow-change transition sags 0.15-0.4 s at the front; front-body
# median -0.2 dB on 18 notes against +1.6 on Sus MAX strokes): fresh Sus MAX strokes (accent_fits / accent_bodies rows of
# these notes removed; the stroke row's level is set back from the render)
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{
    "Violoncellos": DOWNBOW_STROKE_AT["Violoncellos"] + [91.0, 317.0, 321.0, 539.0],
    "Violins I": DOWNBOW_STROKE_AT["Violins I"] + [100.0, 142.0, 154.0, 533.0, 548.0]})
# critic A #2: the celli's two-note sighs 365/369 release inside the transition sag (-2.5 dB at +0.10 s): -1 dB, with fills
SLUR_PAIR_RELEASE_DB_AT = dict(SLUR_PAIR_RELEASE_DB_AT, **{"Violoncellos": {365.0: -1.0, 369.0: -1.0}})
# critic A #5 (test): the violas' f triplet eighths at letter G (bars 117-121, Sus MAX, onset separation median 3.7 dB
# against 9.8-14.3 for staccato elsewhere) on Stac On Bow RRx9 at the written length, stroke velocity (a row load: full
# rebuild of the Violas). Pass: separation median >= 6 dB, 2-5 kHz front - body <= +2 dB, level within 1 dB of c18
ART_SPANS = dict(ART_SPANS, **{"Violas": [{"from": 464.0, "to": 484.0, "art": "Stac On Bow RRx9", "full_len": True,
                                           "vel_by_cc": REP_SPLIT["stac_vel"]}]})
# critic B #1: letter G: the Bass trombone moves with the countermelody from 468 but carried the "held parts" lift and
# covered the ff theme (10 of 14 covered theme onsets): only the bar-121 crescendo part of the hold; the theme (Violins I,
# Flute 1, Oboe 1) +2.5 dB over 464.2-483.5
LEVEL_SHAPES["Bass trombone"] = [[(463.9, 0.0), (479.2, 0.0), (479.6, 4.0), (483.5, 4.0), (484.0, 0.0)] if s_ == _lg_c18
                                 else s_ for s_ in LEVEL_SHAPES["Bass trombone"]]
for tn_ in ("Violins I", "Flute 1", "Oboe 1"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(463.9, 0.0), (464.2, 2.5), (483.5, 2.5), (484.0, 0.0)]]
# ---------- c19 stem fix (level only, measured on the c19 render) ----------
# critic A #2/#4: the early_fills.json entries were written with the critic's times "from the moved onset" but the rule
# keys them to the score onset, so they sat 0.05-0.24 s late (the legato leads): converted (pre_s = lead + pre, hold_s =
# hold - lead). critic A #3: Violas 536 measured +7.3 dB over 537 with a 3 dB swell (fit [3.0, -4.0]), celli +4.2 (2.0)
# critic A #5 (test FAILED, revert in c20 = full Violas rebuild): Stac On Bow triplets separated less (onset median 4.5
# -> 2.6 dB, pass >= 6) and played 3.1 dB louder re master over 464-480: the level back with an exact -3 dB shape
# critic A #1 (test FAILED on 7 of 9 notes, revert in c20 except Violoncellos 321 and Violins I 533): the Leg -> Sus
# stroke cuts the legato note before it and the Sus attack blooms over 0.3-0.8 s (front-body Vc 91 -4.9 -> -12.4, Vc 539
# -3.2 -> -7.6, Vln I 548 -2.4 -> -4.8 dB); the two crescendo-arrival bodies that rose are set back
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(91.3, 0.0), (91.6, -4.5), (93.7, -4.5), (93.95, 0.0)],
                                                               [(539.3, 0.0), (539.6, -2.0), (541.7, -2.0), (541.95, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(463.97, 0.0), (463.99, -3.0), (483.6, -3.0), (484.0, 0.0)]]

# ---------- c20 ----------
# c19 tests reverted (critic A #3, c19 CHANGES): DOWNBOW strokes on 7 accented Leg BC notes made front-body worse (the Leg
# -> Sus cut plus a 0.3-0.8 s Sus bloom); celli 321 and Violins I 533 (front-body -6.0 -> -0.8 / -2.3 -> -0.7) stay
# strokes. Their c18 accent_fits / accent_bodies rows are back (Violins I 100/142/154/548, celli 317; refit after the
# render), and the c19 stem-fix body set-backs on celli 91/539 (which compensated the strokes) go
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{
    "Violoncellos": [q_ for q_ in DOWNBOW_STROKE_AT["Violoncellos"] if q_ not in (91.0, 317.0, 539.0)],
    "Violins I": [q_ for q_ in DOWNBOW_STROKE_AT["Violins I"] if q_ not in (100.0, 142.0, 154.0, 548.0)]})
LEVEL_SHAPES["Violoncellos"] = [s_ for s_ in LEVEL_SHAPES["Violoncellos"]
                                if s_ not in ([(91.3, 0.0), (91.6, -4.5), (93.7, -4.5), (93.95, 0.0)],
                                              [(539.3, 0.0), (539.6, -2.0), (541.7, -2.0), (541.95, 0.0)])]
# (c19 A #5 test failed: letter-G violas back on Sus MAX; the -3 dB level set-back goes with the row; full Violas rebuild)
ART_SPANS = {k_: v_ for k_, v_ in ART_SPANS.items() if k_ != "Violas"}
LEVEL_SHAPES["Violas"] = [s_ for s_ in LEVEL_SHAPES["Violas"]
                          if s_ != [(463.97, 0.0), (463.99, -3.0), (483.6, -3.0), (484.0, 0.0)]]
# critic A #3: the celli pickup 320.5 into the kept stroke at 321 sat 6.4 dB under its target (pass -6..-2)
PICKUP_LIFT["Violoncellos"] = {320.5: 2.5}
# critic A #4: SLUR_HEAD_LEAD heads started a median 0.06 s early with the target's 0.17 s lead (crossover -0.062 s,
# 7 heads -0.10..-0.15 s): their own 0.10 s lead
SLUR_HEAD_LEAD = dict(SLUR_HEAD_LEAD, lead_s=0.10)
# critic A #2: bar 152 (recapitulation): the violas' and celli's 32nd run B-C-D-E into the F (607, top of the crescendo)
# blurred and the F arrived 0.17-0.29 s late (its lead capped at 0.03 s by the 0.125 qn E): the run and the F move
# 0.12 s earlier together (generic GROUP_LEAD_AT)
GROUP_LEAD_AT = {"Violas": [(606.5, 607.0, 0.12)], "Violoncellos": [(606.5, 607.0, 0.12)]}
# critic A #1 (test, Violins I only; a row load = full Violins I rebuild): the slurred sixteenth runs of bars 32, 40 and
# 68 smeared on Sus MAX (own-pitch share 0.08-0.52, first dominance +0.08..+0.17 s on 0.119 s notes) on the 1st Violins
# KS Master's "Slur Runs" row (key 42: Leg Slur transitions plus recorded half-/whole-step scale samples), fast_leg (0.02
# qn overlap, no lead, no merge, targets v127). The targets 128, 160 and 272 stay on their rows; Violins II bar 32 is the
# control. Pass: own-pitch share median >= 0.6 and first dominance <= +0.06 s in bars 32 and 68, bar RMS within 1.5 dB of
# c19, 2-5 kHz first 80 ms - body <= +2 dB on the targets
STACLEG_SPANS = {"Violins I": [(127.0, 128.0, "Slur Runs"), (158.0, 160.0, "Slur Runs"), (270.0, 272.0, "Slur Runs")]}
# critic B #1: the Violins II tremolo row is 4-12 dB hotter than the violas' tremolo; the -3 dB roles release into the
# crescendos of bars 39-40 and 80-81, where it covered the melody (bar 40 onset margin median -3.1, covered 15 of 18;
# bars 80-81 entries covered 4 of 8): exact shapes, added to the roles (simulated: covered 15 -> 6 and 4 -> 2, each bar
# of both crescendos still louder than the one before)
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [
    [(151.9, 0.0), (152.0, -1.0), (156.0, -6.0), (159.9, -6.0), (160.0, -3.0), (162.0, -3.0), (162.5, 0.0)],
    [(315.9, 0.0), (316.0, 0.0), (323.6, -6.0), (324.2, -6.0), (324.3, 0.0)]]
# critic B #2: bars 78-79: the Horns a2 mf entry (pickup lift + accent fit + early fill: +5..+5.9 dB) was the loudest
# event of the passage, over the f entries after it, and covered the Oboe 1 / Violins I / celli mf entry by 6 dB: -4 dB
# from before the pickup's moved onset, back to 0 under the release notch (simulated: 312.5/313 -6.3/-5.9 -> -2.3/-2.1)
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES.get("Horns a2", []) + [[(310.0, 0.0), (310.2, -4.0), (313.4, -4.0), (313.9, 0.0)]]
# critic B #3: Lento bar 12: the violas' f double stop (two full-section samples) sat 1.6-2.7 dB over the Violins I f
# melody, whose 44.835 re-bow fill held the body 3-6 dB down: violas -2.5, Violins I +2.5 over the re-bowed piece
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(43.8, 0.0), (44.0, -2.5), (47.8, -2.5), (48.0, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(45.05, 0.0), (45.2, 2.5), (46.4, 2.5), (46.6, 0.0)]]
# critic B #4: bar 32: Horn 2's accented ff F4 was the loudest stem of the two tutti chords (-8.2..-9.4 re master, Violins
# I -10.4..-11.5): -3 dB
LEVEL_SHAPES["Horn 2"] = LEVEL_SHAPES.get("Horn 2", []) + [[(123.7, 0.0), (123.8, -3.0), (125.9, -3.0), (126.1, 0.0)]]
# critic C #2: coda bars 167-169: the basses' 24 f C2 eighths alternated the same two samples (on-beat minus off-beat
# front +4.8 dB stem / +3.8 master in 40-300 Hz; n vs n-2 within 0.3 dB on 86%): steps on the attacks (full 0.02 qn
# before each onset), weak notes lifted, with a period-6 irregularity
_cb20 = [(663.97, 0.0)]
for i_ in range(24):
    q_ = 664.0 + 0.5 * i_
    v_ = (-0.8 if i_ % 2 == 0 else 1.2) + (0.6, -0.4, 0.0, 0.5, -0.6, 0.2)[i_ % 6]   # c20 stem fix: -1.0/+2.5 -> -0.8/+1.2
    _cb20 += [(q_ - 0.02, v_), (q_ + 0.47, v_)]
_cb20 += [(676.0, 0.0)]
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [_cb20]
# critic C #4: bars 51-52 (exposition second theme, Horn 1 + celli): after the B-flat4 crest the A-flat4-G4 fell 12-16 dB
# (weak horn A-flat4, CC11 69 -> 63; the recapitulation falls under 7 dB): +3.5 Horn 1, +2.5 celli over 204.3-205.6
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(204.15, 0.0), (204.3, 3.5), (205.6, 3.5), (205.9, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(204.15, 0.0), (204.3, 2.5), (205.6, 2.5), (205.9, 0.0)]]
# critic C #3 (build/note_trims.json, early_fills.json, roles.json): the violas' p espr. solo of bars 107-110 peaked on
# the 429 tenuto (+13.7 dB of stacked fixes) and fell 8-13 dB before its top note: 429 trim 5 -> 1.5, fill 5 -> 2.5,
# role [424, 432, 2.5] -> [424, 437.5, 1.5]
# critic C #1 (build/mix.json): Double basses loud_eq third spec, an 80 Hz -5 dB low shelf over the loud spans (not the
# coda span)
# The run's last note joins its target (128, 160, 272) as a Leg BC target with the c19 lead (128, an accented down-bow ff
# that was Sus MAX by STR_ACC_AFTER_SUS after the Sus run, is now a Leg BC target like 160 and 272: as a listed Sus
# stroke after the legato row its lead cut the run's last note to 0.09 qn); the run's first note takes the entry lead
# ---------- c20 stem fix (level only, measured on the c20 render) ----------
# critic C #2: the coda basses' -1.0 / +2.5 steps overshot (40-300 Hz front on-minus-off, first 100 ms: +2.5 -> -1.1 dB
# on the stem; bars 167-169 RMS +1.3 dB): -0.8 / +1.2 (above). critic C #3: the violas' 429 tenuto fell 2.3 dB under 428
# with the 1.5 dB trim: 3.0 (note_trims.json)
# the bar-33 downbeat (Violins I 128, accented down-bow ff eighth after the run) now arrives as a Leg BC target from
# the Slur Runs row and sat 2.5 dB under its c19 Sus stroke (0.05-0.3 s): +2.5 dB from its moved onset (127.8125)
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(127.79, 0.0), (127.81, 2.5), (128.45, 2.5), (128.55, 0.0)]]

# ---------- c21 ----------
# critic A #1 (test, build/mix.json "sus_release_cap_ms" on Violas / Violoncellos / Double basses; full rebuild of the
# three tracks): the Sus MAX mf/f/ff sustain groups' AHDSR releases (Celli 524 ms, Basses 524-700, Violas 333-653) capped
# at 250 ms; rests and tutti cut-offs on Sus MAX fell only 4 dB in 0.18 s rests, the basses' ff eighths ran together
# critic A #2: bar 152: the violas' and celli's F (607, top of the crescendo, unslurred after the 32nd run) sat 3-4 dB
# under the run as a Sus -> Leg Slur join (slow first-note layer): a fresh Sus MAX stroke; GROUP_LEAD_AT keeps its 0.12 s
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violoncellos": DOWNBOW_STROKE_AT["Violoncellos"] + [607.0],
                                               "Violas": DOWNBOW_STROKE_AT.get("Violas", []) + [607.0]})
# critic A #3: the celli's slurred arpeggios of the second theme (bars 55-63, 155-158) crossed rising leaps +0.15..+0.21 s
# late, the lead held at the 0.45 cap (0.12 s): cap 0.75 over the two spans, rising steps of 5+ semitones +0.06 s
# (leg_leads.json; the raised cap only on those listed onsets, the other steps keep 0.45); a target keeps at least 0.10 s after the previous note's moved onset (the unled group heads)
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{"Violoncellos": [(219.0, 252.0, 0.75, "listed"), (616.0, 632.0, 0.75, "listed")]})
LEG_MIN_GAP_S = {"Violoncellos": 0.10}
# critic A #4 (leg_leads.json): the Slur Runs target 270.25 (a third from the v53 head) 0.10 s lead; Violins I 160 not
# changed (its lead is at the 0.75 cap of the 0.25 qn run note before it)
# critic B #1: bars 163-166: Oboe 1's untargeted decrescendo at 648 fell 114 -> 102 while the Violins I it doubles fell
# to mp (oboe 2-5 dB over the line); the mp counter-lines in the violas and Clarinet 1 sat 4-7 dB over the mp melody
HP_TARGET_AT = dict(HP_TARGET_AT, Ob1={648.0: "mf"})
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(651.8, 0.0), (652.0, 3.0), (661.8, 3.0), (662.2, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(652.0, 0.0), (652.3, -2.0), (661.8, -2.0), (662.0, 0.0)]]
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(651.8, 0.0), (652.0, -2.0), (661.8, -2.0), (662.0, 0.0)]]
# critic B #2 (roles.json Cor anglais [586, 620, 4] -> [586, 605, 4, 0.5]): the bar-153 sustained p notes covered the
# mf second theme; the 608 whole note's own bloom is held
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [[(608.0, 0.0), (608.6, -2.0), (611.6, -2.0), (612.0, 0.0)]]
# critic B #3: coda bars 173-174: the cello solo's crest (C5, 692) sat 4 dB under bar 172 with the cor anglais (+6 dB of
# stacked roles, holding the same C5) level with it: cor anglais -2.5 after its imitation entry, celli +3.5 at the crest
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES["Cor anglais"] + [[(687.3, 0.0), (687.6, -2.5), (694.6, -2.5), (694.8, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(691.6, 0.0), (691.9, 3.5), (693.2, 3.5), (693.8, 0.0)]]
# critic B #4 (test): the f/ff/fff rolls of the loud tuttis started at 4-12% of the master's 60-300 Hz (17th-26th of 32
# stems), so the fff arrivals had no audible drum: +3 dB over the three tutti spans; the settle acts on top
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(463.9, 0.0), (464.05, 3.0), (491.5, 3.0), (492.0, 0.0)],
                                                     [(627.9, 0.0), (628.05, 3.0), (643.5, 3.0), (644.0, 0.0)],
                                                     [(663.9, 0.0), (664.05, 3.0), (675.5, 3.0), (676.0, 0.0)]]
# critic B #5: the Violins II tremolo over the Violins I mp-cresc melody at 453.5-454 (-4.3/-3.5); bar 79 0.1 dB under 78
# (the Horns a2 accented mf entry at 311 the top stem)
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(452.8, 0.0), (453.2, -3.0), (455.8, -3.0), (456.2, 0.0)]]
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES["Horns a2"] + [[(310.4, 0.0), (310.5, -1.5), (311.5, -1.5), (311.7, 0.0)]]
# critic C #1-#3: build/mix.json (brass 4 kHz shelves, Trumpet 1 climax shelf -6, tam-tam 86 Hz bell2 -9, horn width 0.15
# with Horn 3/4 seats -0.38/-0.40)
# ---------- c21 stem fix (level only, measured on the c21 render) ----------
# critic A #2: the 607 F as a fresh Sus MAX stroke (v105) took the violas' F from -1.9 to +0.6 dB over the run but the
# celli's from +4.6 to -0.1 (body -37.5 -> -44.1 dB); both now lead (F first dominant -0.07 / +0.01 s from 607, c20
# +0.11 / +0.21): celli +5, violas +1 over the F, back to 0 before 609's moved onset
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(606.78, 0.0), (606.85, 5.0), (608.45, 5.0), (608.55, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(606.78, 0.0), (606.85, 1.0), (608.45, 1.0), (608.55, 0.0)]]
# rebow_fills.json: Double basses and Violas refit on c21 (the 250 ms release deepened the basses' re-bow dips, median
# -1.5 -> -3.2 dB); the celli refit lowered held bars 73-77 by 3.5 dB and was not kept

# ---------- c22 ----------
# critic A #1: the basses' ff repeated-eighth pedals (bars 27-31, 131-134, 140-142; Sus MAX eighths of 0.47 qn) swell to
# mid-note and play as one held note (eighth-grid fold 2.7-3.1 dB at 30-150 Hz, 1.7-2.5 dB at 1-4 kHz; control 7 dB):
# a -5 dB dip over the last 0.08 s before each next moved onset (STR_REP_DETACH, generic), +1.5 dB over the spans to
# keep the bar level (simulated: fold 6.5-7.8 / 5.6-6.9 dB, stem RMS -1.6 dB without the lift)
STR_REP_DETACH = {"at": {"Double basses": [(104.0, 124.25), (520.0, 536.25), (556.0, 568.0)]},
                  "dip_db": -5.0, "dip_s": 0.08, "ramp_s": 0.02, "back_s": 0.005, "max_qn": 0.5, "min_cc": 84}
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [
    [(103.85, 0.0), (103.95, 1.5), (124.0, 1.5), (124.1, 0.0)],
    [(519.85, 0.0), (519.95, 1.5), (536.0, 1.5), (536.1, 0.0)],
    [(555.85, 0.0), (555.95, 1.5), (568.0, 1.5), (568.1, 0.0)]]
# critic A #2 (rebow_fills.json): celli re-bows 39.879 / 41.38 / 49.683 refit on c21 (fit_rebows.py 21 --tracks
# Violoncellos, only these three rows merged: the 250 ms release cap moved the holes earlier; 39.879 was a 10 dB hole)
# critic A #3: string accents on the release-capped tracks refit on c21 (accent_fits.json / accent_bodies.json, Violas,
# Violoncellos, Double basses only)
# critic A #4 (test, mix.json Violas sus_release_cap_ms "rt_ms" 400): the Violas KS Master's Sus MAX release-trail ("RT")
# groups play their recorded release for 1660 ms; cap them at 400 ms as well (full Violas rebuild)
# critic A #5 (early_fills.json via auto_fills.py on c21): Horn 4 joins 415 / 453 opened to 5.9 / 5.2 dB after the c21
# horn rebuild
# critic B #1: bars 85-87, the basses' pizz. mf quarters 8.4 dB over their f pizz. and level with the cello fugato
# subject (three stacked fugato roles, +7 dB): -5 dB step, full before the first pluck
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(335.8, 0.0), (335.9, -5.0), (348.0, -5.0), (348.3, 0.0)]]
# critic B #2: bar 31, the celli's ff A-flat3 / F3 half notes bloom 6 dB over the Violins I theme (master 160-300 Hz
# +3.5..+5.5 dB over bars 28-30): -4 dB after the 120 attack, back before the 124 accent; the 122 fill 5.6 -> 3.0
# (early_fills.json); bar 82 -2 more (K only)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(120.3, 0.0), (120.6, -4.0), (123.75, -4.0), (124.0, 0.0)],
                                                             [(324.25, 0.0), (324.5, -2.0), (327.9, -2.0), (328.2, 0.0)]]
# critic B #3: bars 77-78, the bass-clarinet solo (mf espr.) level with the p tremolo and 3.5-5.3 dB under the mp
# Clarinet 1 answer
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES.get("Clarinet 1", []) + [[(306.3, 0.0), (306.45, -3.0), (309.8, -3.0), (310.2, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [[(304.3, 0.0), (304.5, -2.0), (306.4, -2.0), (306.6, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [[(304.3, 0.0), (304.5, -1.5), (306.4, -1.5), (306.6, 0.0)]]
# critic B #4: bar 115, Oboe 1 enters f cold, 7 dB under Oboe 2 and 3-5 dB under the flutes in unison
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES.get("Oboe 1", []) + [[(455.7, 0.0), (455.85, 4.0), (459.8, 4.0), (460.3, 0.0)]]
# critic C #1: bar 122, the celli's fff A-flat3 (first note of a Leg Slur phrase after the measured-tremolo Stac strokes,
# the slow first-note layer) falls 19 dB under its attack for 0.8 s: a fresh Sus MAX stroke; 488 joins it as Leg BC
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violoncellos": DOWNBOW_STROKE_AT["Violoncellos"] + [484.0]})
# critic C #2: bars 122-123, the fff sostenuto falls 2.8 dB (master M) before its printed decrescendo at bar 124 (brass
# -3..-7 dB inside held chords): +0.8..+1.5 dB on every wind, brass and string track from 485.5 to 492 (simulated: fall
# 1.4 dB, climax margin 160 > 122 0.94 dB S)
_sost = [(485.5, 0.0), (486.5, 0.8), (487.0, 1.5), (487.8, 1.5), (488.1, 0.5), (489.0, 0.8), (490.5, 1.2),
         (491.75, 1.5), (492.25, 0.0)]
for tn_ in [t_[0] for t_ in TRACKS if t_[3] in ("wind", "brass", "string")]:
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [_sost]
# critic C #4: bars 19-20, the Violins I crescendo into the sf at 78 is flat for five beats (0.0 dB): +2 dB rising
# c22 stem fix: the ramp to +2 at 77.75 left the sf at 78 level with the last half beat (-29.0 / -29.0 dB): the ramp
# now peaks at 77.5 and is gone by 77.75
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(74.25, 0.0), (77.5, 2.0), (77.75, 0.0)]]
# critic C #3: tools/deliver_master.py momentary cap (MOM_CAP_ABOVE 6 dB over the knee)
# ---------- c22 stem fix (level only, measured on the c22 render) ----------
# critic B #1 follow-up: the delivery ride did not make up the basses' fugato cut (delivered bars 85-87 -0.3/-0.9/-1.3
# dB): +1.5 dB on the celli, who carry the subject
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(335.8, 0.0), (336.0, 1.5), (348.0, 1.5), (348.3, 0.0)]]

# ---------- c23 ----------
# critic A #1: string and wind accents carried their emphasis as a swell centred 0.30 s after the beat (accented minus
# plain front-body 0 dB; the swell (0.07, 0.25, 0.6) rode a Sus MAX attack that still rises for 0.25 s): a shorter,
# earlier swell. Brass unchanged (the only family with front weight). Accent fits/bodies refit after the render
# (fit_accents.py --front-s, fit_accent_bodies.py --min-s 0.45 with the short-note ramp)
for f_ in ("wind", "string"):
    GENTLE_ACCENT = dict(GENTLE_ACCENT, **{f_: dict(GENTLE_ACCENT[f_], swell_s=(0.03, 0.15, 0.40),
                                                    swell_s_leg=(0.03, 0.22, 0.50))})
ACCENT_BODY_S_SHORT = (0.18, 0.28)
# critic A #2 (test): the accented down-bow hammer strokes swell through the note (peak +0.30 s, front - body -1.7 dB):
# the "Sus Marc LITE" row (key 25, a sustain with a marcato start; loaded on these three tracks: full rebuilds) at the
# strokes' velocity, chords included. Controls: bars 32/72 upper strings, bar 83 violas stay on Sus MAX
ART_SPANS = dict(ART_SPANS, **{
    "Violins I": [{"from": 327.9, "to": 331.0, "art": "Sus Marc LITE", "poly": True},
                  {"from": 563.9, "to": 567.9, "art": "Sus Marc LITE", "poly": True}],
    "Violins II": [{"from": 327.9, "to": 331.0, "art": "Sus Marc LITE", "poly": True},
                   {"from": 563.9, "to": 567.9, "art": "Sus Marc LITE", "poly": True}],
    "Violoncellos": [{"from": 283.9, "to": 286.0, "art": "Sus Marc LITE", "poly": True}]})
# critic A #3: Violins I staccato strokes (Stac RRx14) reached -3 dB at +0.10 s, peak +0.13 s (winds +0.04..+0.07)
STAC_LEAD_S = {"Violins I": 0.05, "Violas": 0.03}
# critic A #4 (test): the violas' ff off-beat dyads of bars 131-134 played their full eighth and filled the eighth rests
# (drop 1.9-8.4 dB, median 5.8): they end at 0.6 of the written eighth (mix.json rt_ms 400 reverted: the c22 test failed)
STR_REST_SHORT = {"at": {"Violas": [(520.0, 536.0)]}, "frac": 0.6, "max_qn": 0.5, "min_bpm": 120}
# critic B #1: bar 162, Horn 1 (untargeted decrescendo, 114 -> 102) and the fff hold left at +3 dB on Horn 1/2 (they rest
# in the Horns a2 window) put Horn 1 4-5 dB over the ff oboe/clarinet line while the brass fall to mp: Horn 1/3 target
# mf+ as Horn 2/4 reach p; the held +3 cancelled on Horn 1 and Horn 2 from the 644 ff mark
HP_TARGET_AT = dict(HP_TARGET_AT, Hn1={**HP_TARGET_AT.get("Hn1", {}), 644.0: "mf+"},
                    Hn3={**HP_TARGET_AT.get("Hn3", {}), 644.0: "mf+"})
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(644.25, 0.0), (644.5, -3.0), (651.8, -3.0), (652.0, 0.0)]]
LEVEL_SHAPES["Horn 2"] = LEVEL_SHAPES["Horn 2"] + [[(644.25, 0.0), (644.5, -3.0), (651.8, -3.0), (652.0, 0.0)]]
# critic B #2: bars 131-134, the ff first theme (clarinets, bassoons, celli; trombones f) covered at 14 of 19 onsets by
# the Violins I descant (simulated: margin -1.4 -> +1.1, covered 14 -> 5). Trombone 1's role is not touched
for t_, d_ in (("Violoncellos", 2.5), ("Bassoon 1", 2.5), ("Clarinet 1", 2.5), ("Violins I", -1.5), ("Violins II", -1.5)):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(520.1, 0.0), (520.3, d_), (535.8, d_), (536.0, 0.0)]]
# critic B #3: bars 145-146, Oboe 1's dolce p E5 swells 8.7 dB inside the note (the sample) to its own ff level
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(579.2, 0.0), (579.9, -3.0), (580.3, -5.0), (581.2, -5.0), (581.7, 0.0)]]
# critic B #4: bars 1-4, the bass clarinet sat 2-6.5 dB (A) over the celli in the pp unison (the line read as a bass
# clarinet solo, and its looped C at qn 11 was exposed): bass clarinet -2.5, celli +1.5 (to the 12.1 re-bow fills)
LEVEL_SHAPES["Bass clarinet"] = LEVEL_SHAPES["Bass clarinet"] + [[(2.7, 0.0), (2.9, -2.5), (16.4, -2.5), (16.6, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(2.7, 0.0), (2.9, 1.5), (11.9, 1.5), (12.1, 0.0)]]
# critic C #1: legato targets after an eighth on Violins II, violas and celli were held at the 0.45 cap (0.107 s at 126
# bpm) and crossed +0.09..+0.16 s late (141 notes): cap 0.75 over the movement (as Violins I since c06), each target
# at least 0.10 s after the previous moved onset. Replaces the celli's c21 "listed" spans (their leg_leads extras stay)
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{t_: [(0.0, 728.0, 0.75)] for t_ in ("Violins II", "Violas", "Violoncellos")})
LEG_MIN_GAP_S = {"Violoncellos": 0.10, "Violas": 0.10, "Violins II": 0.10}
# critic C #2: abutting Sus MAX strokes with no lead crossed +0.10..+0.12 s late (violas 94 notes, +0.08 s behind the
# brass in the theme of bars 69-71 / 167-169): measured onsets listed (0.10 s, the old note ending at the moved start);
# Violins II's slurred Sus MAX eighths 0.06 -> 0.10 s
ABUT_LEAD["Violas"] = dict(ABUT_LEAD["Violas"], at=ABUT_LEAD["Violas"]["at"] + [
    107.0, 107.5, 110.0, 111.5, 114.5, 134.5, 135.0, 135.5, 137.0, 148.5, 149.0, 149.5, 152.75,
    272.5, 273.5, 275.0, 276.0, 278.0, 278.5, 279.0, 280.0, 281.0, 282.0, 283.0, 353.0, 366.0, 388.5, 394.0, 397.0,
    398.0, 399.0, 401.0, 402.0, 403.0, 405.0, 406.0, 407.0, 427.5, 435.5, 441.0, 443.0, 449.0, 453.0, 454.0, 460.0,
    461.0, 463.0, 464.3333, 469.3333, 471.3333, 481.3333, 483.3333, 553.0, 555.0, 557.0, 558.0, 559.0, 561.0, 563.0,
    564.0, 567.0, 667.0, 667.5, 670.0, 671.5, 674.5])
ABUT_LEAD["Violoncellos"] = dict(ABUT_LEAD["Violins II"], at=[312.5, 313.0, 341.0, 350.0, 350.5, 355.0, 417.5, 419.0,
                                                             522.5, 523.0, 523.5, 525.0, 527.5, 530.5, 531.0, 531.5, 533.0])
ABUT_LEAD["Violins II"] = dict(ABUT_LEAD["Violins II"], at=ABUT_LEAD["Violins II"]["at"] + [
    80.5, 109.0, 110.0, 111.5, 278.0, 279.5, 282.0, 283.5, 365.0, 554.5, 558.0, 561.5])
SHORT_SUS_LEAD_S = 0.10
# critic C #3: Clarinet 1's legato had no lead (crossover +0.076 s, +0.045 behind the others; flute/oboe 0.03 s leads
# cross +0.03)
LEG_LEAD_S = dict(LEG_LEAD_S, Clarinet=0.05)
# critic C #4: Leg BC targets crossed 0.05-0.06 s after Leg Slur targets at the same lead on Violins II and violas
LEG_ART_EXTRA_S = dict(LEG_ART_EXTRA_S, **{"Violins II": dict(LEG_ART_EXTRA_S["Violins II"], **{"Leg BC MAX": 0.03}),
                                           "Violas": dict(LEG_ART_EXTRA_S["Violas"], **{"Leg BC MAX": 0.05})})
# critic C #5 (also build/entry_leads.json 118/383): Violins II Leg Slur entries arrive +0.14 s (mid lead 0.06 s)
ENTRY_LEAD_ART_S["Violins II"] = {"Leg Slur MAX": 0.06}
# (actor) caps for the C #2 leads: the listed viola sixteenth (152.75) and triplet strokes (0.33 qn) and Violins II's
# slurred sixteenths would have kept 0.02-0.06 s of the note before: at most 0.45 of that note's slot
SHORT_SUS_LEAD_CAP_FRAC = 0.45
for t_ in ("Violas", "Violoncellos", "Violins II"):
    ABUT_LEAD[t_] = dict(ABUT_LEAD[t_], cap_frac=0.45)
# ---------- c23 stem fix (level only, measured on the c23 render) ----------
# critic A #2 test: the Sus Marc LITE strokes put the weight at the front (front - body -4.9..+0.5 -> +0.4..+10 dB,
# peak +0.07..+0.20 s on 8 of 10) but played 2-8 dB louder than the Sus MAX strokes they replace (whole-note level):
# each stroke back to its c22 level + 0.5 dB (a step from the moved onset to the note end)
for t_, rows_ in (("Violins I", [(327.8721, 329.0, -5.4), (329.874, 331.0, -7.0), (563.8721, 565.54, -5.0), (565.79, 568.0, -6.9)]),
                  ("Violins II", [(327.8721, 329.0, -2.2), (329.874, 331.0, -2.7), (563.8721, 565.54, -6.4), (565.79, 568.0, -7.7)]),
                  ("Violoncellos", [(283.874, 284.5505, -5.6), (284.8005, 286.0, -1.4)])):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES[t_] + [[(m_ - 0.02, 0.0), (m_, d_), (e_, d_), (e_ + 0.04, 0.0)] for m_, e_, d_ in rows_]
# critic B #1 follow-up: Horn 1 still 3-8 dB over Horn 2 through the bar-162 decrescendo (Oboe 1 over Horn 1 only
# +0.4..+3.2 dB A, simulated target +4.5): a further fall to -4 dB by 647
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(644.6, 0.0), (645.5, -2.0), (647.0, -4.0), (648.2, -4.0), (648.4, 0.0)]]
# master top sample peak 1.603 at qn 641.14 (timpani stroke 0.41 + tuba 0.26 + celli + low brass in phase; c22 1.427
# there, raised by Clarinet 1 / Violins II timing): timpani and tuba -2 dB over the stroke's attack
for t_ in ("Timpani", "Tuba"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(640.97, 0.0), (641.0, -2.0), (641.3, -2.0), (641.36, 0.0)]]

# ---------- c24 ----------
# critic A #1: the c23 front-window accent refit drove 13 slurred wind/string accents (mostly targets of an eighth
# pickup, whose 0.18 s front window falls in the legato sag) to the swell+step cap: 4-7 dB louder than in c22 and 5-9 dB
# over their next plain notes (rule: 2-4). A cut of min(rise, over-next - 3.5) dB over the score onset - 0.03 .. + 0.35 s
# (0.03 s in, 0.15 s out), measured on the c23 stems. Clarinet 1 505 is left to B #4 (its fill is the cause).
_acut = [(-0.06, 0.0), (-0.03, 1.0), (0.35, 1.0), (0.50, 0.0)]
for t_, q_, d_ in (("Oboe 1", 105.0, -2.7), ("Clarinet 1", 151.0, -3.4), ("Clarinet 1", 273.0, -3.4),
                   ("Clarinet 1", 105.0, -3.1), ("Clarinet 1", 521.0, -1.1), ("Bassoon 1", 382.0, -5.1),
                   ("Violins II", 325.0, -4.6), ("Violins II", 381.0, -4.2), ("Violins II", 525.0, -3.9),
                   ("Violas", 325.0, -4.1), ("Violoncellos", 521.0, -4.0), ("Violoncellos", 382.0, -1.5)):
    LEVEL_SHAPES_S[t_] = LEVEL_SHAPES_S.get(t_, []) + [(q_, [(s_, d_ * v_) for s_, v_ in _acut])]
# critic A #2: the bar-142 Marc LITE half notes (Violins I/II 564, 566) collapsed after the stroke: the c23 stem fix set
# each whole note to its c22 level + 0.5, but the row carries its level in the front, so the bodies sat 3-6 dB under c22
# (Violins I 566 a 0.25 s stab, front - body +10.8). Body back to c22 (the step rows below raised by the body change)
# and the front left about +2.5 dB over it (a seconds shape from just before the moved onset to +0.25 s, ramp 0.05 s):
# Violins I 566 body +5.8 / front -2.3, Violins II 566 +3.4 / -2.9, Violins I 564 +1.6 / 0, Violins II 564 +1.3 / 0.
# Their accent_fits / accent_bodies rows stay (the deltas were measured with them); skip them in refits.
_mlb = {("Violins I", 563.8721): 1.6, ("Violins I", 565.79): 5.8, ("Violins II", 563.8721): 1.3, ("Violins II", 565.79): 3.4}
def _mlb_fix(t_, s_):
    if len(s_) == 4 and s_[0][1] == 0.0 and s_[1][1] == s_[2][1] and (t_, round(s_[1][0], 4)) in _mlb:
        d_ = _mlb[(t_, round(s_[1][0], 4))]
        return [s_[0], (s_[1][0], s_[1][1] + d_), (s_[2][0], s_[2][1] + d_), s_[3]]
    return s_
for t_ in ("Violins I", "Violins II"):
    LEVEL_SHAPES[t_] = [_mlb_fix(t_, s_) for s_ in LEVEL_SHAPES[t_]]
for t_, q_, f_ in (("Violins I", 566.0, -2.3 - 5.8), ("Violins II", 566.0, -2.9 - 3.4),
                   ("Violins I", 564.0, -1.6), ("Violins II", 564.0, -1.3)):
    LEVEL_SHAPES_S[t_] = LEVEL_SHAPES_S.get(t_, []) + [(q_, [(-0.15, 0.0), (-0.13, f_), (0.25, f_), (0.30, 0.0)])]
# critic A #5: the c23 Violins II Leg BC extra (+0.03) overshot (cap-free Leg BC -0.033 s, 8 targets -0.09..-0.12 s;
# joins of 4.5 dB or more rose): 0.0
LEG_ART_EXTRA_S = dict(LEG_ART_EXTRA_S, **{"Violins II": dict(LEG_ART_EXTRA_S["Violins II"], **{"Leg BC MAX": 0.0})})
# critic A #4: Violins I re-bows dip 4-6 dB (80 ms minimum). A refit (fit_rebows.py 23 --tracks "Violins I") changed the
# c10 rows by under 1 dB (simulated median dip -3.6 -> -3.55: the 0.12 s smoothed fit does not see these dips) and was
# not kept. Only 711.855 has a hole (-4..-6 dB from +0.0 to +0.30 s); the others are the sample's own 3 Hz bow/vibrato
# swing (+-3 dB, 0.3 s period). A fill there; 48.597's step is the c13 bar-13 diminuendo shape
LEVEL_SHAPES_S["Violins I"] = LEVEL_SHAPES_S.get("Violins I", []) + [(711.855, [(-0.03, 0.0), (0.02, 4.0), (0.28, 4.0), (0.38, 0.0)])]
# critic B #1: bar 26's ff tutti chord (qn 100-103.5) sat 0.7 dB under the third climax on delivered S max; the inner
# strings bloomed after the attack to the top of it (Violins II +6..+9, violas +3..+9 dB over their ff medians). The
# attack at 100.0 untouched (simulated by B: master -1.3 dB, Violins I the top string again)
for t_, d_, a_ in (("Violins II", -3.5, 100.35), ("Violas", -3.5, 100.35), ("Violins I", -1.5, 100.35),
                   ("Trumpet 1", -1.5, 100.3), ("Trumpet 2", -1.5, 100.3), ("Trumpet 3", -1.5, 100.3),
                   ("Trombone 1", -1.5, 100.3), ("Trombone 2", -1.5, 100.3), ("Bass trombone", -1.5, 100.3),
                   ("Tuba", -1.5, 100.3)):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(a_, 0.0), (a_ + (0.55 if a_ > 100.32 else 0.3), d_), (103.2, d_), (103.6, 0.0)]]
# critic B #3: bar 84, the celli's sub. p G2 (a fresh Leg Slur MAX first note) swells 8 dB inside the note to the top
# stem and the basses' G1 rebounds 7 dB: an unprinted hairpin (simulated: celli rise 3 dB, master -2 dB over 333-334.25)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(332.5, 0.0), (332.9, -3.0), (333.1, -5.0), (334.0, -5.0), (334.6, -2.0), (335.3, -2.0), (335.9, -3.0),
     (335.98, -9.0), (336.2, -9.0), (336.26, 0.0)]]
# (actor) the G2 also blooms again over its last half beat (-35 -> -32 dB) and its note-off at 336.0 plays a 0.3 s
# burst at -25 dB on the celli stem and the master (7-8 dB over the bar, before the solo pickup's moved onset 336.248):
# B's shape held at -2/-3 to the end and a -9 dB notch over 335.98-336.2
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(332.9, 0.0), (333.15, -3.5), (334.3, -3.5), (334.8, 0.0)]]
# critic B #4 (early_fills.json, here): Clarinet 1's c23 auto fill at 227 put the p espr. counter-line 4.6 dB over the
# Violins I melody onset: fill removed and -2.5 dB at the onset, back to 0 by 227.6; 505 / 507.5 fills 5.5 / 6.7 -> 2.5 /
# 3.5 (the bar-127 p solo: +5.8 dB over its neighbours)
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(226.85, 0.0), (226.95, -2.5), (227.1, -2.5), (227.6, 0.0)]]
# critic B #5: bars 45-46, the Oboe 1 p solo notes swell 8-9 dB inside each note to the oboe's own f level (CC11 flat
# 46; the exposition twin of the bar-146 note): exact shape (simulated: each note rises about 3 dB)
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(178.3, 0.0), (178.75, -3.0), (179.4, -3.0), (179.6, 0.0), (180.25, 0.0),
                                                   (180.6, -3.0), (181.0, -5.0), (181.9, -5.0), (182.0, 0.0)]]
# critic C #1: bars 49-50 / 149-150, the dolce second theme (Horn 1 + celli) sags 3.7 dB in the middle of its first
# phrase (Horn 1's envelope falls from +5.5 to +1..+2.5 at a flat CC11) and the celli fall 4-8 dB onto the top note of
# the printed < (195 -> 196, 595.5 -> 596; the samples)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(193.2, 0.0), (193.45, 3.0), (195.0, 3.0), (195.9, 6.0), (196.6, 5.5), (197.6, 4.0), (198.2, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(193.2, 0.0), (193.45, 2.0), (195.6, 2.0), (195.9, 6.5), (196.6, 6.0), (197.6, 4.0), (198.2, 0.0)],
    [(595.65, 0.0), (595.92, 6.0), (597.0, 5.0), (597.9, 2.0), (598.1, 0.0)]]
# critic C #2: the second-theme harp arpeggios (Harp Sus RR) jump 10-15 dB from note to note (p10-p90 19.6 dB over bars
# 47-68): movement II's c09 table (HARP_PITCH_VEL default) replaced by one fitted on c23 (-deviation / 0.37 dB per
# velocity step, halved for single notes, capped at +-12)
HARP_PITCH_VEL = {55: -6, 56: -12, 58: 5, 60: 5, 61: 9, 63: 0, 64: -8, 65: -12, 66: -12, 67: 6, 68: -9, 70: -12,
                  72: -7, 73: 12, 75: -12, 76: -10, 77: -12, 78: 12, 81: 12, 82: 12, 83: 10, 84: 10, 85: -12,
                  86: 12, 87: 12, 88: 12, 89: 12, 92: 5, 94: 12, 96: 4, 97: 12}
# critic C #3: coda bars 167-169, the basses' f eighths limp (each off-beat swells in late; on-beat minus off-beat front
# +6.9 dB stem / +3.1 master): STR_REP_DETACH over the span as on the ff pedals, +1.5 dB hold as on the other spans.
# (actor) C's on/off alternation 0/0 simulated worse (stem front on-off +3.25 -> +4.71 dB: the dips act at the note
# ends, the off-beats' fronts stay weak); with the c20 -0.8/+1.2 +2.71; -1.2/+1.6 (0.9 dB of front per dB of step, c20)
STR_REP_DETACH = dict(STR_REP_DETACH, at={**STR_REP_DETACH["at"], "Double basses": STR_REP_DETACH["at"]["Double basses"]
                                          + [(664.0, 676.0)]})
_cb24 = [(663.97, 0.0)]
for i_ in range(24):
    q_ = 664.0 + 0.5 * i_
    v_ = (-1.2 if i_ % 2 == 0 else 1.6) + (0.6, -0.4, 0.0, 0.5, -0.6, 0.2)[i_ % 6]
    _cb24 += [(q_ - 0.02, v_), (q_ + 0.47, v_)]
_cb24 += [(676.0, 0.0)]
LEVEL_SHAPES["Double basses"] = [s_ if s_ != _cb20 else _cb24 for s_ in LEVEL_SHAPES["Double basses"]] + [
    [(663.85, 0.0), (663.95, 1.5), (676.0, 1.5), (676.1, 0.0)]]
# critic C #4 (and the c23 C #6 deferral): four stretches ran at one fixed tempo: the exposition's first statement of
# the second theme (qn 184-200 at 112.0 for 17 beats; the recapitulation's (584, 600) has an arc), the sostenuto
# (488-504) and largamente (636-656) at 100.0, and the coda Allegro into the bar-170 fermata (664-679 at 126). Arcs as
# the rest of the movement has them; re-bows are frozen in qn (_REBOW_FROZEN). The animando ramps of bars 62-65 and
# 156-159 end at the printed last step (bar 65 had run to 120.1 against the printed 118, and the rit. of bar 66 then
# started 2.6% slower)
PHRASE_ARCS = PHRASE_ARCS + [(184, 200), (488, 504, "sub"), (636, 648, "sub"), (664, 679, "sub")]
RAMP_SPANS = [(244, 252, 115) if r_[:2] == (244, 260) else (620, 628, 115) if r_[:2] == (620, 632) else r_
              for r_ in RAMP_SPANS]
# (actor) the coda arc is there for its last beats into the fermata only; its apex hold (Violas, beat 673 x0.96) would
# put a hitch in the middle of the ff trumpet theme: APEX_SKIP (generic). The 196 (Horn 1 A-flat4, the printed < top)
# and 637 (largamente, Violins I top) apex holds stay
APEX_SKIP = {664}

# ---------- c25 ----------
# ONE_TIME #1 (loop pulse, measured on c24 with cycles/c25/actor_scripts/loopscan.py): the held single-sample wind/brass
# notes whose 100-300 Hz band or centroid autocorrelation at the loop lag reached 0.4: Bass clarinet 11 (centroid 0.72 at
# 3.95 s, -6.6 dB re master in the Lento), Bass clarinet 464 (band 0.64), Horn 4 289 (0.44 / 0.34), Bassoon 2 476 (0.72 /
# 0.83 at 4.7-4.9 s). Staggered breath splits into pieces of 2.1-3.1 s (shorter than any measured loop), irregular
BREATH_SPLIT_AT = dict(BREATH_SPLIT_AT, **{"Bass clarinet": {**BREATH_SPLIT_AT.get("Bass clarinet", {}), 11.0: [13.5],
                                                             464.0: [469.5, 474.5]},
                                           "Horn 4": {**BREATH_SPLIT_AT.get("Horn 4", {}), 289.0: [295.0, 299.5]},
                                           "Bassoon 2": {**BREATH_SPLIT_AT.get("Bassoon 2", {}), 476.0: [481.5, 487.0, 491.0]}})
# ONE_TIME #2: the c24 tempo side effects. Violins I/II 259.5 (slurred eighth, 0.254 s at 118 bpm) back to the short_sus
# Sus MAX path (SHORT_SUS_AT, generic); the tempo gates read the map before the phrase arcs (GATE_BPM_PRE_ARC, generic
# default True), which gives the clarinets' 637 (96 bpm under the largamente apex hold) their re-tongue lead back
SHORT_SUS_AT = {"Violins I": [259.5], "Violins II": [259.5]}
# critic A #2 (test): brass accents peak 0.21 s (median) after the beat, as plain brass notes do (front - mid -1.3 dB):
# the wind/string swell timing of c23 on the brass (db / soft_db, plain Sus, no accent sample, no CC11 bump unchanged)
GENTLE_ACCENT = dict(GENTLE_ACCENT, brass=dict(GENTLE_ACCENT["brass"], swell_s=(0.03, 0.15, 0.40), swell_s_leg=(0.03, 0.22, 0.50)))
# critic A #3: Oboe 1's falling whole steps E5 -> D5 (397.5, 582) and D5 -> C5 (90, 498, 538, 555.5) cross over 0.14-0.26 s
# late, identical in c23 and c24 (the 582 end of the bar-146 dolce solo dips 8 dB)
LEG_PAIR_EXTRA_S["Oboe 1"] = {**LEG_PAIR_EXTRA_S["Oboe 1"], (76, 74): 0.12, (74, 72): 0.10}
# critic B #2: letter K (628), Violins I's printed down-bow G5 was merged into its slurred G5 eighth (SLUR_REP_MERGE_SUS),
# so the melody's ff downbeat had no attack (7-9 dB under Violins II's stroke): a down-bow stroke as on Violins II, and
# Violins II's stroke front 2.5 dB lower (it was +9.2 dB over its own ff median)
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violins I": DOWNBOW_STROKE_AT["Violins I"] + [628.0]})
LEVEL_SHAPES_S["Violins II"] = LEVEL_SHAPES_S.get("Violins II", []) + [(628.0, [(-0.02, 0.0), (0.03, -2.5), (0.35, -2.5), (0.6, 0.0)])]
# critic B #3: recapitulation bars 136-139, Oboe 1 (unison) and Flute 1 (octave above) sat +1.7 / +2.9 dB (A, median)
# over the Violins I theme they double (exposition twin -0.5): Flute 1's pickup lift 8 -> 4, -3 dB on Flute 1 553-557.2,
# -2.5 dB on Oboe 1 542-547.8 (the 536-548 roles stay)
PICKUP_LIFT["Flute 1"].update({552.5: 4.0})
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES["Flute 1"] + [[(552.85, 0.0), (553.0, -3.0), (557.2, -3.0), (557.45, 0.0)]]
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(541.7, 0.0), (541.95, -2.5), (547.8, -2.5), (548.1, 0.0)]]
# critic C #2: the fff crash at bar 160 falls under the tutti's 4-12.5 kHz band 1.5 s after the stroke (-6.6 dB at +1.5 s,
# -10.8 at +2.0 s): +3.4 dB at 638.0 and +5 dB from 638.5 over the c09 shape (C proposed +2.9/+4; simulated on c24 that
# left -8.0 dB at +2.0 s against the 7 dB target; +3.4/+5 gives -1.9 / -7.0 at +1.5 / +2.0 s). Stroke, first 0.6 s and
# the -4 dB dip that protects the 636.04 master peak unchanged
LEVEL_SHAPES["Crash cymbals"] = [[(636.0, 0.0), (636.02, -4.0), (636.6, -4.0), (637.2, 0.0), (638.0, 6.5), (638.5, 10.0), (644.0, 11.0)]]
# critic A #1 (build/accent_fits.json, hand values): the hemiola accents of bars 22-24 / 135-137 (every neighbour accented,
# so fit_accents.py left them on the default mf swell, +1.7 dB): Clarinet 1 / Violoncellos 91, 94, 539, 542, 545 and
# Bassoon 1 94, 97, 542, 545
# critic B #1 / #4 (build/mix.json): Bass trombone dyn_trim f/ff/fff 3.9/6.3/4.7 -> 1.4/3.3/2.2; Horn 4 1.0/1.5/0.5 ->
# 2.5/4.0/2.0
# critic C #1 (test, build/mix.json, full rebuilds): width 0.05 on Horn 1-4, Trumpet 1, Cor anglais, Oboe 1, Clarinet 1
# (the solo patches' spaced mic pairs give each harmonic under 1 kHz its own position at width 0.15-0.5), seats moved to
# keep each track's measured 1.25-4 kHz image
# ---------- c25 stem fix (level only, measured on the c25 render) ----------
# ONE_TIME #1 follow-up: the breath-split pieces re-enter at their own sample level. Bass clarinet 11 (the ppp Lento
# unison, -5 dB re master): the second piece swells to +2.7 dB over the first; Horn 4 289 (pp): a +3.5 dB bloom 1.4-2.0 s
# into the second piece, then a 4 dB hole at the 299.5 re-entry (0.2 s frames, stems)
LEVEL_SHAPES_S["Bass clarinet"] = LEVEL_SHAPES_S.get("Bass clarinet", []) + [(13.5, [(1.0, 0.0), (2.0, -2.5), (3.48, -2.5), (3.72, 0.0)])]
LEVEL_SHAPES_S["Horn 4"] = LEVEL_SHAPES_S.get("Horn 4", []) + [(295.0, [(1.3, 0.0), (1.4, -3.5), (2.0, -3.5), (2.08, 0.0)]),
                                                             (299.5, [(-0.02, 0.0), (0.02, 2.5), (0.2, 2.5), (0.35, 0.0)])]
# critic A #2 follow-up: brass accents refit on c25 with the new swell timing (build/accent_fits.json; see its _doc)
# critic A #3 follow-up (build/early_fills.json): Oboe 1 582 fill retimed (dip 6.1 dB at the new lead), 498 lowered 5.8 ->
# 3.8 (its front now 9.7 dB over the previous body)
# critic A #3 follow-up: with the pair-extra leads the transition sag of Oboe 1's D5 -> C5 targets falls on the beat
# (stem, 60 ms frames): 90 a 7-8 dB hole over -0.06..+0.06 s (c24 none), 538 8 dB over -0.06..+0.12 s (c24 7 dB at +0.18):
# exact fills
LEVEL_SHAPES_S["Oboe 1"] = LEVEL_SHAPES_S.get("Oboe 1", []) + [
    (90.0, [(-0.10, 0.0), (-0.05, 3.0), (0.0, 6.0), (0.08, 5.0), (0.14, 2.0), (0.20, 0.0)]),
    (538.0, [(-0.10, 0.0), (-0.05, 3.0), (0.0, 6.5), (0.10, 6.0), (0.16, 3.0), (0.22, 0.0)])]

# ---------- c26 ----------
# critic A #1: the dolce second theme (celli + Horn 1, bars 49-50 / 149-150). The c24 C #1 celli shapes reached full gain
# on the celli's 596/196 Leg Slur transition burst (595.69-595.87, +8.5 dB over both bodies; 196 +6), and the celli and
# Horn 1 shapes ramped down into the 598/198 join (kit LEARNINGS section 6), leaving a 4.5 dB (recap) / 5-8 dB (expo)
# master hole on beat 3 inside the printed diminuendo. The rise now starts after the burst (notched), and the fall runs
# through the half note to before the 600/200 joins
_r_ = {((595.65, 0.0), (595.92, 6.0), (597.0, 5.0), (597.9, 2.0), (598.1, 0.0)):
       [(595.65, 0.0), (595.95, 0.0), (596.15, 6.0), (597.0, 5.0), (598.6, 3.0), (599.6, 0.0)],
       ((193.2, 0.0), (193.45, 2.0), (195.6, 2.0), (195.9, 6.5), (196.6, 6.0), (197.6, 4.0), (198.2, 0.0)):
       [(193.2, 0.0), (193.45, 2.0), (195.6, 2.0), (195.95, 2.0), (196.15, 6.5), (196.6, 6.0), (198.6, 3.0), (199.6, 0.0)],
       ((596.1, 0.0), (597.9, -4.0), (598.05, 0.0)): [(596.1, 0.0), (597.5, -3.0), (598.0, 0.0), (598.6, 1.0), (599.6, 0.0)],
       ((196.1, 0.0), (197.9, -2.5), (198.05, 0.0)): [(196.1, 0.0), (197.5, -2.0), (198.0, 0.0), (198.6, 1.5), (199.6, 0.0)],
       ((193.2, 0.0), (193.45, 3.0), (195.0, 3.0), (195.9, 6.0), (196.6, 5.5), (197.6, 4.0), (198.2, 0.0)):
       [(193.2, 0.0), (193.45, 3.0), (195.0, 3.0), (195.9, 6.0), (196.6, 5.5), (198.6, 3.0), (199.6, 0.0)]}
for tn_ in ("Violoncellos", "Horn 1"):
    _n_ = 0
    _new_ = []
    for s_ in LEVEL_SHAPES[tn_]:
        k_ = tuple(tuple(p_) for p_ in s_)
        if k_ in _r_:
            _new_.append(_r_[k_])
            _n_ += 1
        else:
            _new_.append(s_)
    LEVEL_SHAPES[tn_] = _new_
    assert _n_ == {"Violoncellos": 2, "Horn 1": 3}[tn_], (tn_, _n_)
# (actor, c26 stem fix) A's Horn 1 falls to -4 / -2.5 dB held across the 598/198 half notes simulated Horn 1 - celli
# -0.4 -> -5.6 / -2.4 -> -4.4 dB there (A's own pass: within 2 dB) and the render matched: the 596/196 C5 growth cut
# (-3 / -2) now ends rising into the join (0 at the score onset, before the moved 598/198 targets' sag ends) and follows the
# celli's added tail (+1 / +1.5 at 598.6 / 198.6; +2 at 598.6 put the 598 half note level with 596 inside the >); Horn 1's 598 join sag (10 dB, +0.15..+0.6 s on the c26 stem) filled
LEVEL_SHAPES_S["Horn 1"] = LEVEL_SHAPES_S.get("Horn 1", []) + [(598.0, [(0.05, 0.0), (0.2, 2.5), (0.55, 2.5), (0.75, 0.0)])]
# (actor, c26 stem fix) the exposition notch (195.66-195.92, -4) fell on the sag before that burst (the expo burst sits
# at +0.2..+0.3 s, 195.87-196.06, and lost 4.5 dB with the old +6.5 ramp): celli -41.8 dB at +0.15 s against -33 bodies;
# removed. The recapitulation notch fits its burst (c26 stem flat within 2 dB over the join)
JOIN_NOTCH = dict(JOIN_NOTCH, **{"Violoncellos": JOIN_NOTCH.get("Violoncellos", []) + [(595.66, 595.92, -5.0)]})
# critic C #1: the coda dies away on the master (bars 171-182, -13 dB) but the delivery ride is at its cap from 696, so
# the pp chorale delivered as loud as the mp cello solo (mp3 fall 1.0 dB, bar 176 over bar 171): -2 dB on every track
# from the chorale on (simulated: solo - chorale 1.0 -> 3.0 dB delivered, LRA 14.4 -> 15.2, span 19.1 -> 19.9 dB).
# Percussion tracks do not read "_all", so the tam-tam gets the shape itself
# (actor) on the 0.125 qn envelope grid: a breakpoint at 695.95 sharpened the grid-smeared soft-trim step of the chorale
# entries at 696 (Trombone 1 entry -10.6 dB for 0.05 qn against c25)
_coda26 = [(695.5, 0.0), (695.875, -3.5), (732.0, -3.5)]   # c30 (critic C #2): -2 -> -3.5
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [_coda26]
LEVEL_SHAPES["Tam-tam"] = LEVEL_SHAPES.get("Tam-tam", []) + [_coda26]
# critic C #2: Clarinet 1's p < mf (bars 127-128) moved +0.1 dB on the stem (the line falls into the throat and low
# register; accent fits at 505/510 bump both ends): +4 dB over the hairpin, back to the mf line at 513
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(504.75, 0.0), (511.5, 4.0), (512.9, 4.0), (513.2, 0.0)]]
# critic C #3: Lento bar 3, the opening motif's second pp < > rose 2.6 dB against bar 2's 7.1 (the celli sag 2-4 dB
# through 9.0-10.0): +3 dB at the crest on the three unison voices
for tn_ in ("Violoncellos", "Double basses", "Bass clarinet"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES[tn_] + [[(8.5, 0.0), (9.75, 3.0), (10.25, 3.0), (11.0, 0.0)]]
# critic C #4: the coda cello solo's first E-flat4 (680, mp <) sags 4-5 dB at 682.4-682.9 before its hairpin top, the
# same in c22-c25 (sample): +3.5 dB over the sag, gone before the 683.5 note's moved onset and step
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(682.15, 0.0), (682.55, 3.5), (683.15, 3.5), (683.3, 0.0)]]
# critic B #1 / #3 / #4 (build/roles.json): letter G held ff harmony Horn 3 -3.5, Horn 4 -2.0 (with the ff trim below),
# Tuba -3.0 over 464-484 (4 qn end ramp); Horn 4 -2.5 over the f bars 132-134 (524-536); Bass clarinet -3 on the bar-97
# ff whole note (384-388). (build/mix.json): Horn 4 dyn_trim ff 4.0 -> 2.0 (c25 B #4 overshoot outside its five chords);
# Tuba bell2 84 Hz -5 dB 0.3 oct (E2/F2 fundamental). B #2 (build/note_trims.json): Violas 436 +5 -> 0 (stale c12 trim)

# ---------- c27 ----------
# critic A #1: fugato bars 85-90. The Stac RRx9 row plays untrimmed at mf (ROW_TRIM_DB applies from CC11 80): celli
# staccatos +5.6 dB median (max +16.2) over the subject's legato notes and accent, violas +2.2, Violins II 367.5 +9.6.
# A's note-trim values as exact steps on the attack (a note trim ramps in over 0.1 s from the score onset and misses the
# 50 ms stroke peak); the celli run 343.5-347 is one step through its rests
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(338.45, 0.0), (338.48, -2.0), (338.92, -2.0), (338.97, -4.0), (339.85, -4.0), (339.95, 0.0)],
    [(343.45, 0.0), (343.48, -4.0), (347.6, -4.0), (347.72, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [
    [(350.38, 0.0), (350.42, -2.5), (351.65, -2.5), (351.75, 0.0)],
    [(355.88, 0.0), (355.92, -2.5), (356.4, -2.5), (356.5, 0.0)],
    [(357.88, 0.0), (357.92, -2.5), (358.4, -2.5), (358.5, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(367.45, 0.0), (367.48, -5.0), (367.78, -5.0), (367.88, 0.0)]]
# critic A #1: the celli's mp C at 348 was a disconnected Leg Slur MAX first note (the slow first-note layer; master
# 348.0-348.5 -43.9 dB against -34.3 / -36.1 either side, c11-c26): a fresh Sus MAX stroke at the score onset, and the
# c22 +1.5 fugato shape held through it (the +3 role [338, 348] -> [338, 348.5] in roles.json)
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violoncellos": DOWNBOW_STROKE_AT["Violoncellos"] + [348.0]})
_k27_ = [(335.8, 0.0), (336.0, 1.5), (348.0, 1.5), (348.3, 0.0)]
assert sum(1 for s_ in LEVEL_SHAPES["Violoncellos"] if [tuple(p_) for p_ in s_] == _k27_) == 1
LEVEL_SHAPES["Violoncellos"] = [[(335.8, 0.0), (336.0, 1.5), (348.5, 1.5), (348.8, 0.0)]
                                if [tuple(p_) for p_ in s_] == _k27_ else s_ for s_ in LEVEL_SHAPES["Violoncellos"]]
# critic B #3: bar 40, the timpani pp < roll was the top stem in K at 158-159 over the f orchestra and the Violins I run
# (envelope +19..+21 dB at the roll start): -2.5 dB over the bar's last two beats, back for the bar-41 sf
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(157.5, 0.0), (158.25, -2.5), (159.9, -2.5), (160.0, 0.0)]]
# critic B #4 (build/roles.json): Trombones 1/2 and Tuba [104, 124, -2, 0.5] in bars 27-31 (printed f under the ff theme,
# 3-5 dB over the ff horns), the row Trumpets 2/3 already have
# critic B #1 (build/mix.json): Double basses static mute_eq bells 61.7 Hz -6 / 73.4 Hz -5 (0.25 oct): the B1 and D2
# fundamentals are as strong as harmonics 2-4 (-2.2 / +0.6 dB) against -6..-21 on their neighbours
# critic C #1: Violins I Leg BC targets cross over +0.065 s (deviation +0.046 from the other sections) on the 0.17 s
# string lead, and its Leg Slur targets after eighths +0.075 (capped at 0.75 of the eighth): Leg BC +0.05; 30 listed
# Leg Slur onsets +0.05 in leg_leads.json with a 0.95 cap for listed onsets and LEG_MIN_GAP_S 0.10; four early Leg BC
# targets -0.05. Celli Leg BC extra -0.06 -> -0.02 (crossover +0.080, deviation +0.040); four early celli Leg BC
# targets -0.04 in leg_leads.json
LEG_ART_EXTRA_S = dict(LEG_ART_EXTRA_S, **{"Violins I": {"Leg BC MAX": 0.05},
                                           "Violoncellos": dict(LEG_ART_EXTRA_S["Violoncellos"], **{"Leg BC MAX": -0.02})})
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{"Violins I": [(56.0, 728.0, 0.95, "listed"), (56.0, 728.0, 0.75)]})
# (actor) LEG_MIN_GAP_S 0.06, not C's 0.10: at 0.10 every Violins I Leg Slur target after an unled eighth lost lead
# (21 targets 0.17 -> 0.135-0.138 s, 9 of them listed), since c26 already left only 0.068 s of a 126-bpm eighth
LEG_MIN_GAP_S = dict(LEG_MIN_GAP_S, **{"Violins I": 0.06})
# critic C #3 (build/leg_leads.json): 23 Violins II / violas / celli legato targets 0.08-0.19 s early on both the
# crossover and the own-pitch arrival: negative per-onset extras of (earliest - 0.03 s)
# critic C #2: the development's arcs slowed inside the letter-F ff phrase (bar 99, 115.9 bpm, then 122-128) and inside
# the six-bar crescendo to letter G (bar 110 a 12% "main" slowing, bar 113): (384, 396) and (440, 452) push only,
# (432, 440) "main" -> "sub"
PHRASE_ARCS = [(384, 396, "open") if x_[:2] == (384, 396) else (432, 440, "sub") if x_[:2] == (432, 440)
               else (440, 452, "open") if x_[:2] == (440, 452) else x_ for x_ in PHRASE_ARCS]
# critic C #4: the Più lento cello solo (bars 171-174) changed tempo direction five times in 12 beats (two 2-bar arcs
# with two apex holds): one 4-bar arc
assert sum(1 for x_ in PHRASE_ARCS if x_[:2] in ((680, 688), (688, 696))) == 2
PHRASE_ARCS = [x_ for x_ in PHRASE_ARCS if x_[:2] not in ((680, 688), (688, 696))] + [(680, 696, "main")]
# (actor) C #2 follow-up: the (440, 452) arc's apex hold put a 4% slower beat at 448 (bar 113, inside the crescendo to
# letter G that C's finding is about): no apex hold on that arc
APEX_SKIP = APEX_SKIP | {440}
# (actor) C #2 follow-up: with (384, 396) open, the (396, 408) arc's return beat put 122.2 bpm between 126 and 127.9 on
# bar 100's downbeat (C's check: bar 99 -> 100 within 2%): new generic PHRASE_RETURN_AFTER_OPEN, off here
PHRASE_RETURN_AFTER_OPEN = False
# ---------- c27 stem fix (level only, measured on the c27 render) ----------
# A #1 follow-up: the celli 348 C as a Sus MAX stroke at the printed mp (v58) still sat at -48.1 dB body (c26 Leg Slur
# first note -46.0; target -39.5), master 348.0-348.5 -45.4: A's fallback, a level step, sized to the target (+8 dB on
# the note from its moved onset, gone at the 349.5 stroke)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(347.7, 0.0), (347.78, 8.0), (349.35, 8.0), (349.47, 0.0)]]
# A #2: Clarinet 1's re-tongued accents 414 / 422 rendered in the bright state again (stem 2-5 kHz front-body +10.3 /
# +8.1, master front-pre +7.6 / +8.6; 626 dull, -11.4, left alone): A's post-render fix on the first 0.12 s, -7.5 dB
# rather than A's -5 (simulated on c27: -5 left the master at +4.6 / +4.7 against A's +3.5)
LEVEL_SHAPES_S["Clarinet 1"] = LEVEL_SHAPES_S.get("Clarinet 1", []) + [
    (q_, [(-0.02, 0.0), (0.0, -7.5), (0.12, -7.5), (0.30, 0.0)]) for q_ in (414.0, 422.0)]

# ---------- c28 ----------
# critic A #1: coda Più lento, bars 172-173: the cello solo's E-flat4 at 689.5 sat 3.3 dB (master) under its flat
# neighbours and the two eighths of the printed < into the top note (691, 691.5) 3-4 dB under 690, so the crescendo
# played as a fall (CC11 flat at 67; samples). Exact steps, not ramped into the joins; added to the c26 691.6 crest shape.
# The cor anglais' p E-flat5 at 684 (a legato target a sixth over its pickup) sat 5.4 dB under that pickup: +4
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(689.18, 0.0), (689.26, 5.0), (690.22, 5.0), (690.34, 0.0)],
    [(690.80, 0.0), (690.90, 3.5), (691.25, 3.5), (691.35, 4.0), (691.80, 4.0), (691.95, 4.0), (692.6, 4.0), (693.0, 1.5), (693.5, 1.5), (693.8, 0.0)]]
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [[(684.1, 0.0), (684.4, 4.0), (686.8, 4.0), (687.2, 0.0)]]
# critic A #2: second-theme harp arpeggios (bars 47-59): single notes 5-8 dB over their figure and half-note tops 5-8 dB
# under it, the same in c26 and c27 to 0.1 dB (the RR1 Pluck / RR2 Thumb Pick alternation, read from the .oib: two RR
# groups, each with its own velocity layers). Per-onset velocities (deviation / 0.4 dB per step, +-20, floor 40) on top of
# HARP_PITCH_VEL; the RR group order does not depend on velocity, so the other onsets keep their samples
VEL_SET = dict(VEL_SET, **{"Harp": {185.5: 56, 190.0: 76, 193.5: 57, 198.0: 88, 200.5: 40, 206.0: 84, 209.5: 58,
                                    218.0: 65, 222.0: 66, 231.0: 57, 234.0: 86, 234.5: 111, 235.0: 86, 235.5: 110}})
# critic C #1: letter G, bars 117-120: every held ff note took the swell / taper arc (CC11 114 -> 118 -> 109 on the bass
# line), so the tutti sagged 2-2.5 dB for three bars with no printed decrescendo: the swell_sost contour (held) there
ARRIVAL_HOLD_SPANS = ARRIVAL_HOLD_SPANS + [(464.0, 480.0)]
# critic C #2: letter F, bars 97-102: the violas' 48 unslurred f eighths had no beat (beats 1/3 minus the rest -0.02 dB):
# the METRIC_BOWED steps the other motor spans have
METRIC_BOWED = dict(METRIC_BOWED, **{"Violas": METRIC_BOWED["Violas"] + [(384.0, 408.0)]})
# critic C #4: delivered p10-to-max span 19.9 dB, the frames under p10 now mostly in Tempo I (bars 179-182, delivered S
# median -31.2 LUFS after the c26 -2 dB coda cut): +1.5 dB on every track from bar 179, held to the end (C: +1; stem fix)
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(711.0, 0.0), (712.0, 1.5), (732.0, 1.5)]]
# critic B #1 / #2 / #3 / #5 (build/roles.json): Violas [77.5, 82.75, +5, 0.5] (bars 19-21 espr. counter-line); Flute 1
# and Oboe 1 [463.5, 479.5, +4, 1.5] (letter G tune doubling); Violins II [211.5, 218.25, -4, 0.5] and
# [610.5, 618.0, -4.5, 0.5] (pp chords at the second-theme phrase ends); Bass clarinet [440, 456, -3.5, 2] and
# [703.5, 707.5, -3, 0.5], Clarinet 1 [705.75, 707.75, +2.5, 0.25]
# critic B #4 (build/pitch_trims.json): Double basses G2 / A-flat2 (43 / 44) -6 dB, the near-sine fundamental of bars
# 12-14 and 90; every other G2 / A-flat2 onset listed in _skip_onsets (bar 6 pp, the pizz. and the fugato, 413, 554,
# 612-614, the held 654) keeps its level
# critic C #3 (build/mix.json, test): Violoncellos loud_eq bell2 200 Hz +3 dB 1 oct (loud 160-250 Hz -10.3 dB re
# 250-2000 Hz against -7.7 in the Dvorak reference)
# ---------- c28 stem fix (level only, measured on the c28 render) ----------
# A #1 follow-up: master 691 1.6 dB under 690 and the top note 692 (-31.9) under 685 (-31.2, raised 0.7 dB by the cor
# anglais +4): the 691 step 3 -> 3.5 and the 692 step 2.5 -> 4 (flat through the 691.95 join), falling to 1.5 by 693
# (the A #1 shape above carries these values)
# (the Tempo I lift above is 1.5, not C's 1: the render gave span 19.6 dB with +1; C simulated 19.4 with +1.5)
# A #2 follow-up: the harp's velocity response at these onsets was 0.6-1.0 dB per step, not 0.4 (layer crossings: Pluck
# p/mp at 57/58, Thumb Pick mp/mf at 70/71): 185.5 v74 -> 56 -13.1 dB, 198 v76 -> 88 +11.4, 222 v74 -> 66 -11.8, and bar 59
# alternated +-7..9 dB. Exact steps on the attack, held to the next onset (kit c12/c21 plucked-note trims)
_h28 = [(185.5, 186.0, 4.5), (190.0, 192.0, 2.0), (198.0, 200.0, -5.5), (200.5, 201.0, -2.0), (206.0, 208.0, 3.0),
        (222.0, 222.5, 4.5), (231.0, 231.5, 3.0), (234.0, 234.5, 5.5), (234.5, 235.0, -5.5), (235.0, 235.5, 3.5),
        (235.5, 236.0, -3.5)]
LEVEL_SHAPES["Harp"] = LEVEL_SHAPES.get("Harp", []) + [[(a_ - 0.03, 0.0), (a_ - 0.01, v_), (b_ - 0.03, v_), (b_ - 0.01, 0.0)]
                                                       for a_, b_, v_ in _h28]
# C #1 follow-up: master K 468-480 still 0.8-1.7 dB under 464-466 (c27 1.2-2.5): +0.8 dB on every track over the
# plateau, held through the bar-121 crescendo to 482 and gone by 483.5 (before the 484 fff)
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(467.0, 0.0), (468.5, 0.8), (482.0, 0.8), (483.5, 0.0)]]
# C #3 follow-up: with the 200 Hz bell2 the celli rose 1.2-1.3 dB K re master in bars 27-31 and 117-120, which they do
# not lead (C's limit +0.5): roles.json Violoncellos [104, 124, -0.8, 0.5] and [464, 480, -0.8, 0.5]
# B #1 follow-up: violas 78-82 rose 2.5-4.8 dB (B simulated 4-5), still 8-9 dB under Violins I: the role 5 -> 6.5

# ---------- c29 ----------
# critic A #1: Lento bars 6-7, cor anglais solo: the A4 pitch trim (-5) ramps in over 0.25 qn from the joined eighth's
# moved onset (0.30 s of a 0.59 s note at 50.75 bpm), so it made a V inside the A4 (-42..-43 dB) and rose +4.8 dB into
# the G4's Leg Slur transition (master join -29.7, 6-8 dB over the G4 body): A's exact shape, simulated on c28
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES["Cor anglais"] + [
    [(23.70, 0.0), (23.725, 4.0), (23.80, 4.5), (23.83, 1.0), (23.85, -1.5), (23.92, -1.5), (23.955, -4.0), (23.99, -5.5),
     (24.03, -3.0), (24.07, 0.0), (24.10, 2.0), (24.60, 2.0), (25.00, 0.0)]]
# (c29 stem fix: A's shape as rendered left the A4's own rise at 23.84-23.87 4 dB over the A4 body (+4 still on it) and
# the join peak 4.0 dB over the G4 body on the master; refitted on the c28/c29 20 ms frames)
# critic A #2: second theme bar 52, Horn 1 + celli dolce: the printed > over 204-206 played as a 7 dB hole at the G
# eighth (celli -10 dB) and a 6 dB rebound on Horn 1's F (burst at 206.1, bloom to 207): fill the eighth, cut the F
# (the horn cut starts at 206.12, after the eighth's tail)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(205.35, 0.0), (205.5, 4.0), (206.5, 4.0), (206.9, 0.0)]]
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(205.35, 0.0), (205.5, 3.0), (206.0, 3.0), (206.08, 0.0),
                                                    (206.12, -4.0), (207.8, -4.0), (208.0, 0.0)]]
# critic A #3: two wind legato joins holed by the envelope: Clarinet 1 212 -> 213 (the A-flat4 throat trim ramps out
# at the G4's moved onset - 0.05, its early fill starts at 213.0: 9 dB stem hole) and Oboe 1 578 -> 579 (the E5 after
# a ninth arrives 0.2 s late; the 578.94 envelope step deepens the join)
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(212.64, 0.0), (212.72, 5.0), (213.04, 5.0), (213.12, 0.0)]]
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(578.90, 0.0), (578.96, 4.0), (579.40, 4.0), (579.55, 0.0)]]
# critic A #4 (build/rebow_fills.json): the celli 723.921 re-bow row raised +2.5..+6 dB over -0.04..+0.16 s
# critic B #1 / #2 / #4 (build/roles.json): Horn 1 [407.5, 419.5, 3.5, 0.5], Bassoon 1 and Violoncellos
# [407.5, 423.5, 3.5, 0.5] (bars 103-106 mf counter-line 5-9 dB under the f figure); Flute 1 / Oboe 1 letter-G rows
# start at 455.5 instead of 463.5 and Flute 2 [455.5, 463.5, 4, 0.5] (bars 115-116 f entry 7-12 dB under Violins I);
# Trombone 1 / 2 / Bass trombone [155.5, 159.75, -3, 0.2] (bar 40 f chord level with the mf cresc. melody)
# critic B #3 (build/pitch_trims.json): Double basses F1 / F2 (29 / 41) +3, G1 (31) -2 (F sat 3-4 dB under its
# neighbours, on the 87.3 Hz bell2; G1 +2.2)
# critic C #1 (build/mix.json): the c28 celli loud_eq bell2 200 Hz +3 reverted with its two -0.8 celli roles (the
# 198 Hz band was already 2-4 dB over Dvorak / Brahms 1 / Brahms 4; the shortfall at 125-160 Hz is the voicing)
# critic C #2 / #3 (build/mix.json): side_shelf bell 170 Hz -2 dB 1 oct on celli and basses (master 120-250 Hz
# correlation 0.44, references 0.54-0.58), plus a side high shelf 1.5 kHz +4 dB on the celli (stem above 4 kHz 0.87)

# ---------- c30 (final cycle; level only, every change simulated on the c29 stems) ----------
# critic A #1 (build/early_fills.json): ten celli/viola legato fills with pre_s 0.09-0.17 s acted on the old note
# (crossovers on the beat since c27): pre_s 0 on Violoncellos 650, 422, 266, 66, 712, 10, 4, 694 and Violas 429; the
# Violoncellos 687 fill removed and replaced by an exact shape (bar 172: the < peaked on the A-flat4 tail, G4 7-9 dB under)
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [
    (687.0, [(-0.25, 0.0), (-0.20, -2.0), (-0.03, -2.0), (0.0, 7.0), (0.36, 7.0), (0.52, 0.0)])]
# critic A #2: bars 43-44 p horn duet: Horn 2's held G4 fell 7 dB and its E-flat4 jumped 17 dB; Horn 1's C5 fell 15 dB
# in the printed > and its B-flat4 came in 17 dB over the C5's end
LEVEL_SHAPES["Horn 2"] = LEVEL_SHAPES.get("Horn 2", []) + [[(168.3, 0.0), (168.9, 1.5), (169.6, 3.0), (170.3, 6.0),
    (170.8, 8.0), (171.8, 8.0), (171.9, -4.0), (172.4, -6.0), (172.9, -3.0), (173.5, 0.0)]]
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES.get("Horn 1", []) + [[(172.0, 0.0), (172.315, 2.0), (172.63, 3.5), (173.05, 4.5),
    (173.47, 6.0), (173.806, 6.0), (173.89, -4.0), (174.1, -7.0), (174.73, -7.0), (175.15, -4.0), (175.675, -1.5),
    (175.99, 0.0)]]
# critic A #3: bar 153, the celli's slur-end A3 swelled 7 dB into the 612 bow (master +4.6 dB at a phrase end)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(611.1, 0.0), (611.2, -3.5), (611.45, -4.5), (611.85, -4.5),
                                                                (611.97, 0.0)]]
# critic A #4: fugato bar 89, the celli mp countersubject half note (Leg BC, 352) level with the mf subject (A: -4; -5.5
# here: with -4 the celli were still level with the violas on this measure, A wanted at least 1.5 dB under)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(351.9, 0.0), (352.2, -5.5), (353.8, -5.5), (353.95, 0.0)]]
# critic B #1: bars 45-46, Oboe 1's falling p line ended 5 dB over the F4 on its E-flat4 (role + "182" fill + sample)
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(181.95, 0.0), (182.05, -6.0), (183.0, -6.0), (183.2, 0.0)]]
# critic B #2: bar 93, the cor anglais's f staccato A4 (371) 5-9 dB over its line, the A-flat4 (370) 5 dB under it
# (the A4/A-flat4 pitch trims are right at p; the f step is local)
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES["Cor anglais"] + [[(370.98, 0.0), (371.08, -6.0), (371.75, -6.0), (372.0, 0.0)],
                                                              [(369.98, 0.0), (370.05, 3.0), (370.6, 3.0), (370.7, 0.0)]]
# critic B #3 (build/pitch_trims.json): Bassoon 1 C-sharp4 (61) trimmed on every articulation (Sus MAX notes 5-7 dB
# over their neighbours), the short Sus notes 351 / 391.5 skipped
# critic B #4: bar 114, the Violins I tune fell 4-5 dB inside the long mp cresc. (master dipped 1.5 dB)
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(453.05, 0.0), (453.25, 4.0), (455.35, 4.0), (455.55, 0.0)]]
# critic B #5 (build/note_trims.json): Bass clarinet 364 / 372 / 380 / 382 -4 dB (B-flat2s 5-9 dB over the line)
NOTE_TRIM_RAMP_S["Bass clarinet"] = {**NOTE_TRIM_RAMP_S.get("Bass clarinet", {}), 364.0: 0.1, 372.0: 0.1, 380.0: 0.1,
                                     382.0: 0.1}
# critic C #1: the fff tam-tam (484) sat 11-17 dB under the orchestra through 124-126 and its envelope fell with the
# brass: hold the ring up from after the stroke to the printed damp (attack and the damp itself unchanged)
LEVEL_SHAPES["Tam-tam"] = LEVEL_SHAPES.get("Tam-tam", []) + [
    [(485.0, 0.0), (488.0, 3.0), (492.0, 7.0), (496.0, 9.0), (504.2, 9.0), (504.4, 0.0)]]
# critic C #2: _coda26 -2 -> -3.5 dB (above) with tools/deliver_master.py TOP_RATIO 1.6 -> 2.5 (pp 0.8 -> about 2 dB
# under p in the mp3, limiter 2.1 -> about 1.3 dB)
# critic C #3: the delivery ride's lift grows +2 -> +6 dB across the cello solo after the ff fermata: +2 dB on every
# track over its first bars, handed back to the ride by 691
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(679.80, 0.0), (679.88, 2.0), (685.0, 2.0), (691.0, 0.0)]]
