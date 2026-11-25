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
          "Bass clarinet": [284.0, 286.0, 554.0], "Clarinet 1": [414.0, 417.0, 422.0], "Trombone 1": [632.0, 676.0]}
# (c45, critic A #2: Violins I 59.5 / 571.5 left the table with their trims: since c44 they sit on the 0.11 s eighth only)
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
# c34 (critic A #4): the bar-83 rows (327.8721) ended at the note-off and lifted the release 9 dB over the stepped body
# (as at 565.54 in c33): held to 329.75, before the next stroke's row at 329.874
for t_, rows_ in (("Violins I", [(327.8721, 329.75, -5.4), (329.874, 331.0, -7.0), (563.8721, 565.54, -5.0), (565.79, 568.0, -6.9)]),
                  ("Violins II", [(327.8721, 329.75, -2.2), (329.874, 331.0, -2.7), (563.8721, 565.54, -6.4), (565.79, 568.0, -7.7)]),
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

# ---------- v621 port (series 2, c00) ----------
# The score moved from v221 to v621. 93% of notes (onset + pitch) are unchanged; the per-onset tables above are kept and
# entries on notes that no longer exist do nothing. Percussion: v621 has no clashed cymbals in movement I (score c250):
# the suspended-cymbal roll pp < (bar 159) swells into one soft-stick fff stroke at qn 636 that rings and is damped
# gradually to p (bars 160-163). The "Cres" patch's let-ring crescendo sample peaks and rings on, so the stroke at 636 is
# that sample's peak (skip_at), not a second roll. The Crash cymbals track stays in the project, silent (stem numbers).
PERC_MAP["Suspended cymbal"]["ridecymbal"] = dict(PERC_MAP["Suspended cymbal"]["ridecymbal"], skip_at=[636.0])
# Tempo: v621 moved the Tempo dell'Allegro of the closing to qn 270 (the rit. ends on the deceptive cadence at 268-270),
# and added "poco a poco stringendo" 129-132-135-138 over bars 113-116 (qn 448-464), a tempo 126 at qn 464 (the ff).
RAMP_SPANS = [(260, 270, r_[2]) if r_[:2] == (260, 272) else r_ for r_ in RAMP_SPANS] + [(448, 464, 126)]

# ---------- c32 (series 2, first improvement cycle; critics on the c31 render) ----------
# Port bugs fixed in the tools: compound dynamics ("pp espr.") and the MIDI velocity table (build/mockup.ly mockVol);
# hairpin swells inside one printed dynamic (HP_MDV_FIRST, HP_SWELL_CEIL, HP_LONE_RETURN, HP_LOUD_SWELL_DB,
# HOLD_AFTER_KEEP_CRESC_START), BOOST_STOP_SKIP, TENUTO_HEAD_LEGATO, PERC_MAP "only_at", HARP_DAMP_STAFF "(m.g.)".
# critic A #3 / B #3a: v621 moved v221's Oboe 1 lines at letter G (464-480) and the climax (628-650) to Oboe 2 (same
# patch and pitches); Oboe 1 now holds F5-G5-F5 at letter G. The Oboe 1 keys moved to Oboe 2 (roles, accent fits and
# bodies, note trim 479, early fills 629/642 and entry lead 636 in build/*.json; the breath and hairpin keys here); the
# letter-G theme shape +2.5 dB goes to Oboe 2. Oboe 1 456-460 (unchanged f entry) keeps its role and the c19 shape.
BREATH_GAP_AT = dict(BREATH_GAP_AT, **{"Oboe 2": {634.0: BREATH_GAP_AT["Oboe 1"].pop(634.0)}})
BREATH_FALL_CC = dict(BREATH_FALL_CC, **{"Oboe 2": {634.0: BREATH_FALL_CC["Oboe 1"].pop(634.0)}})
HP_TARGET_AT = dict(HP_TARGET_AT, Ob2={**HP_TARGET_AT.get("Ob2", {}), 648.0: HP_TARGET_AT["Ob1"].pop(648.0)})
_lgG = [(463.9, 0.0), (464.2, 2.5), (483.5, 2.5), (484.0, 0.0)]
LEVEL_SHAPES["Oboe 1"] = [s_ for s_ in LEVEL_SHAPES["Oboe 1"] if s_ != _lgG]
LEVEL_SHAPES["Oboe 2"] = LEVEL_SHAPES.get("Oboe 2", []) + [_lgG]
# critic A #3: Trombone 1's note into the bar-160 breath now starts at 634 (v621 splits v221's 632 D4 into D4 + B3)
BREATH_GAP_AT["Trombone 1"] = {634.0: BREATH_GAP_AT["Trombone 1"].pop(632.0)}
BREATH_FALL_CC["Trombone 1"] = {634.0: BREATH_FALL_CC["Trombone 1"].pop(632.0)}
# critic A #6: v621's "Solo espr." cello (bars 171-174) on the full Celli KS Master took SOLO_BOOST +8 (c30's "espr."
# took +3): a section cannot play a solo, so the section keeps its espr. boost (+3), as in c30
SOLO_NO_BOOST = tuple(SOLO_NO_BOOST) + ("Violoncellos",)
# critic A #5: v621's string syncopes in bars 15/17/19 are an eighth tied to a half (2.5 qn): shape them too
SYNCO_SHAPE = dict(SYNCO_SHAPE, len_qn=(0.75, 2.5))
# critic A #5: bar 45, the celli's G at 176 starts the slur G -> A-flat (STR_MERGE_KEEP_SLUR_START in the tools)
# critic B #2: v621 raised the harp p -> mp over bars 47-54 (qn 184-220): the c28 per-onset velocities there +12 (the
# rule velocities rose 12; the fitted onsets stayed at the p values, 2.6 dB under their neighbours)
VEL_SET["Harp"] = {q_: (v_ + 12 if 184.0 <= q_ < 220.0 else v_) for q_, v_ in VEL_SET["Harp"].items()}
# critics A #4 / B #5b / C #4: v621 damps the fff tam-tam gradually from bar 124 (qn 492) to p at bar 126 (500): the c30
# ring lift (+9 dB to the damp, written for v221's l.v.) now falls to -5 dB by 500 (simulated on the c31 stem: tam-tam
# 18-21 dB under the master at 498-503, 7-9 dB under Horn 1's solo in 150-600 Hz; was 6.5-7.5 dB under the master)
LEVEL_SHAPES["Tam-tam"] = [[(485.0, 0.0), (488.0, 3.0), (492.0, 7.0), (500.0, -5.0), (504.2, -5.0), (504.4, 0.0)]
                           if s_ == [(485.0, 0.0), (488.0, 3.0), (492.0, 7.0), (496.0, 9.0), (504.2, 9.0), (504.4, 0.0)]
                           else s_ for s_ in LEVEL_SHAPES["Tam-tam"]]
# critics A #4 / C #3: the suspended cymbal's fff stroke at 636 is the peak of the Cres roll sample, which decays about
# 13 dB/s (inaudible a beat after the climax; every HO Sus Cymbal patch is a crescendo roll). The ring comes from the
# silent Crash cymbals track (22in K Crash, its 9.4 s Long sample, c05): one note at 636 only, faded in under the roll's
# peak so only its ring sounds (c30's ring lift less 4 dB, C's simulation), damped gradually 644 -> 648 (-12 dB) as
# printed, then out after the p at 648-652 (mix.json tail_hold false)
PERC_MAP["Crash cymbals"] = {"ridecymbal": {"key": 60, "only_at": [636.0], "min_s": 14.0, "delay_s": 0.05},
                             "_damp": [(651.0, -25.0, 0.8)]}
LEVEL_SHAPES["Crash cymbals"] = [[(636.0, -34.0), (636.25, -34.0), (636.75, -6.0), (637.2, -4.0), (638.0, 2.5),
                                  (638.5, 6.0), (644.0, 7.0), (648.0, -5.0), (652.0, -5.0)]]
# critic B #6: bar 84, the celli/basses' sub. p at 332 arrived late (v621 moved the celli's ff accented down-bows at
# 328/330 to G2, the sub. p note's pitch; the basses' ff G1 swells into the downbeat): exact notches before the new
# note (simulated on the c31 stems: master 330.5-331 minus 332-332.5 6.5 -> 11.1 dB)
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(331.45, 0.0), (331.6, -8.0), (332.25, -8.0), (332.4, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(331.05, 0.0), (331.15, -8.0), (331.7, -8.0), (331.78, 0.0)]]
# ---------- c32 stem fix (level only, measured on the c32 render) ----------
# Violins I coda: the "pp espr." text now gives the line the strings' melody-span CC1 (85-105), which on the Hollywood
# Strings KS Master crossfades to the Molto Vib sample set (1st Violins .oib: Non Vib out by CC1 55, Sus Vib 55-85, Molto
# Vib full from 105): with c30's fills the 711.855 re-bow piece burst 15 dB over c30 (+13 dB envelope fill fitted on
# c30's Sus Vib piece). build/rebow_fills.json Violins I refit on c32 (fit_rebows.py 32, all six rows; 711.855 +10 ->
# -6 dB) plus these cuts: line 1-3 dB over c30 bar by bar (the espr. +3 CC), the 720 join burst notched
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [
    [(706.875, 0.0), (707.0, -2.5), (707.875, -2.5), (708.125, 0.0)],
    [(711.75, 0.0), (711.875, -2.5), (714.75, -2.5), (715.0, 0.0)],
    [(719.875, 0.0), (720.0, -8.0), (720.25, -8.0), (720.375, -3.0), (720.5, 0.0)]]
# critic B #3a follow-up: Oboe 1's held ff F5 at letter G (464-468, the crescendo's arrival gain) stayed within 1 dB of
# the Violins I theme in bar 117 (re M -10.8 / -9.1 against -11.6 / -10.3): -3 dB over the held note
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(464.0, 0.0), (464.25, -3.0), (468.5, -3.0), (469.0, 0.0)]]
# critic C #3 follow-up: build/roles.json _all [484, 492, -1.2, 2] -> -1.6 (S max bar 160 over bar 122 was +0.71 dB)

# ---------- c33 (series 2; critics on the c32 render) ----------
# critic A #1: bar 142, the Violins I/II Sus Marc LITE 564 rows (c23 stem-fix steps) ended at 565.54, so the stroke's
# release after its 565.54 note-off played 5-6 dB over the stepped body (master +5.5 dB burst at 565.6, then a 9 dB gap
# before the 566 strokes). The steps now hold through the release and hand over to the 566 rows (from 565.77) by 565.79
# (the step keeps its current value: c23's -5.0 / -6.4 plus c24's +1.6 / +1.3)
def _r564(s_):
    if len(s_) == 4 and round(s_[1][0], 4) == 563.8721 and round(s_[2][0], 4) == 565.54:
        return [s_[0], s_[1], (565.77, s_[2][1]), (565.79, 0.0)]
    return s_
for t_ in ("Violins I", "Violins II"):
    assert sum(_r564(s_) is not s_ for s_ in LEVEL_SHAPES[t_]) == 1, t_
    LEVEL_SHAPES[t_] = [_r564(s_) for s_ in LEVEL_SHAPES[t_]]
# critic A #1 (smaller): v621's accented down-bow on Violoncellos 566 plays as a Leg BC MAX target that peaks 0.28 s
# late, 5.4 dB over its body, front under the body: a body cut after the front (A's shape, simulated on the c32 stem)
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [
    (566.0, [(0.08, 0.0), (0.16, -5.0), (0.45, -5.0), (0.65, -1.5), (0.8, 0.0)])]
# critic A #2: Clarinet 1's accents at 414/422 rendered the dull attack state in c30 and c32 (2-5 kHz front-body -2.7 /
# -5.0 dB; c27 bright +10.3 / +8.1), so the c27 -7.5 dB front cut left them 6-8 dB under the plain notes around them:
# the front cut and note trims are gone (note_trims.json), the body cut is in accent_bodies.json (-5.5 / -6.0)
LEVEL_SHAPES_S["Clarinet 1"] = [r_ for r_ in LEVEL_SHAPES_S["Clarinet 1"]
                                if not (r_[0] in (414.0, 422.0) and r_[1] == [(-0.02, 0.0), (0.0, -7.5), (0.12, -7.5), (0.30, 0.0)])]
# critic B #2 (with A #3): bars 45-46, v621's Clarinet 1 p dolce solo. Its untargeted decrescendo 180-182 fell 21 CC
# (CC11 45 -> 24, CC1 40 -> 20: the softest layer, ppp under pp strings): target pp. The celli A-flat bloom cut moved to
# v621's onset in loop_fills.json; the solo's level contour is fitted on the stems below (after that cut)
HP_TARGET_AT = dict(HP_TARGET_AT, Cl1={**HP_TARGET_AT.get("Cl1", {}), 180.0: "pp"})
# critic B #1: second theme bars 47-55, the harp's arpeggio tops crossed a Harp Sus RR layer with c32's +12 velocities
# (+9..+12 dB at 189.5/190/206/210/213.5/214, peaks a median 2.3 dB under the dolce horn/cello melody, c30 5.5): the
# c28 steps at 190 / 206 (fitted at the old velocities) become cuts, new cuts on the other jumped onsets (exact steps on
# the attack, held to the next onset), plus roles.json Harp [184, 220, -1.5, 0.5]. The +12 velocities stay (mp layer)
_h33 = {(190.0, 192.0, 2.0): (190.0, 192.0, -2.5), (206.0, 208.0, 3.0): (206.0, 208.0, -3.0)}
_hshape = lambda a_, b_, v_: [(a_ - 0.03, 0.0), (a_ - 0.01, v_), (b_ - 0.03, v_), (b_ - 0.01, 0.0)]
for o_, n_ in _h33.items():
    assert _hshape(*o_) in LEVEL_SHAPES["Harp"], o_
    LEVEL_SHAPES["Harp"] = [_hshape(*n_) if s_ == _hshape(*o_) else s_ for s_ in LEVEL_SHAPES["Harp"]]
LEVEL_SHAPES["Harp"] = LEVEL_SHAPES["Harp"] + [_hshape(a_, b_, v_) for a_, b_, v_ in (
    (189.5, 190.0, -4.5), (210.0, 212.0, -3.0), (213.0, 213.5, -3.0), (213.5, 214.0, -4.0), (214.0, 216.0, -5.5))]
# critic C #2: v621 prints down-bows on the Violins I downbeats 160 (bar-41 sf) and 272 (letter D f) after the Slur Runs
# runs; as Leg BC targets the new pitch dominated only at +0.21..+0.23 s. Fresh Sus MAX strokes (the entry lead); the
# bar-68 run (now at 126 bpm since v621's Tempo dell'Allegro at 270) moves 0.08 s earlier as a group, replacing
# leg_leads.json Violins I 270.25
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violins I": DOWNBOW_STROKE_AT["Violins I"] + [160.0, 272.0]})
GROUP_LEAD_AT = dict(GROUP_LEAD_AT, **{"Violins I": GROUP_LEAD_AT.get("Violins I", []) + [(270.25, 271.75, 0.08)]})
# critic C #3: Flute 1's F-sharp6 -> E5 at qn 396 (a slur break, 14 semitones) played as a legato transition across the
# 0.05 qn gap (crossover +0.34 s): WIND_WIDE_LEG (tools) re-tongues it on the Sus row
WIND_WIDE_LEG = 12
# critic A #6: bar 13, v621 prints a down-bow on the tied Violins I G5 at 48 (the start of its f > p): the frozen
# automatic re-bow 48.597 moves to the printed bow change (its fitted shape is refitted from the c33 render)
REBOW_AT = dict(REBOW_AT, **{"Violins I": sorted(48.0 if abs(q_ - 48.597) < 1e-3 else q_ for q_ in REBOW_AT["Violins I"])})
# critic A #1 follow-up (simulated on the c32 stems): with the step held through 565.77 the violins' release after the
# 565.54 note-off still stood 6-7 dB over the stepped body (Vln I -27.8 -> -23.4 at 565.55-565.65): a -5 dB notch over
# the release (kit c18: a -6 dB notch from the note-off removed a Sus MAX release burst)
for t_ in ("Violins I", "Violins II"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES[t_] + [[(565.52, 0.0), (565.55, -5.0), (565.73, -5.0), (565.77, 0.0)]]
# critics B #2 / A #3: Clarinet 1's solo after the celli cut and the p soft trim (+1.7), simulated on the c32 stems: the
# A-flat4 legato target decays 6-9 dB inside the slur and the G4 sits 10 dB under the B-flat head. A level contour
# (A's shape, refitted on the simulated stem): the head -1 dB, the A-flat and G lifted to about 2 dB under it, the
# printed decrescendo 180-182 then falls about 4 dB to the E-flat (HP_TARGET_AT pp above raises 180-183 too, by an
# amount the stems cannot show: the contour there is smaller than the simulated gap, to be checked on the c33 render)
# c33 stem fix (measured on the c33 render): with the pp target the F4 (180-182) came out 2-5 dB over the simulation and
# over the B-flat head (-39.6 against -40.5; its decrescendo fell 1 dB), and the A-flat level with the head: the contour
# below is the rendered one refitted (head -40.5, A-flat about 1 dB under, G4 -42.5, F4 -41.5 falling to about -44.5,
# E-flat -46.5)
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[
    (175.8, 0.0), (176.0, -1.0), (177.75, -1.0), (178.0, 2.5), (178.5, 5.0), (179.0, 6.5), (179.3, 7.0), (179.75, 7.5),
    (180.0, 0.0), (181.0, 0.5), (181.5, -0.5), (181.8, -1.0), (182.1, 4.0), (183.0, 4.0), (183.4, 0.0)]]

# ---------- c33 stem fix (level only, measured on the c33 render) ----------
# critic A #2 follow-up: this render played Clarinet 1's 414 accent in the bright attack state (2-5 kHz front - body
# +12.6 dB, front 8.4 dB over the body; 422 +3.6, dull). The c27 front cut goes back on 414 for this render's state
# only: re-classify 414/422 after the next render and remove it if 414 renders dull (A's rule; kit c26-c27)
# c34 stem fix: the c34 render played 414 without the bright burst (2-5 kHz front minus body about -2.5 dB without the
# cut, against +12.6 in c33's bright state): the cut is removed for this render's state (re-classify after each render)
# LEVEL_SHAPES_S["Clarinet 1"] = LEVEL_SHAPES_S["Clarinet 1"] + [(414.0, [(-0.02, 0.0), (0.0, -7.5), (0.12, -7.5), (0.30, 0.0)])]
# critic C #2 follow-up: the Violins I down-bow strokes now take the downbeat pitch on time (G6 / C6 dominate from the
# score onset; c32 from +0.25 s), but their fronts came out 5-12 dB under the bodies: at 272 the stroke takes the
# vibrato delay of a phrase start (CC1 70 -> 105 over 1.4 qn; the Molto Vib set is recorded louder), so the f downbeat
# opened at -41.9 against a -31 body. Exact front lifts from just after the run's last note (moved onset -0.06 s).
# Tool fix for c34: no vibrato delay on a DOWNBOW_STROKE_AT stroke joined from the note before
# c34 (critic A #3a): the 272 row (+6..+9 dB) removed; tools STROKE_NO_VIB_DELAY gives the stroke its CC1 from the
# front instead (the 160 stroke had no dip; its row stays)
LEVEL_SHAPES_S["Violins I"] = LEVEL_SHAPES_S.get("Violins I", []) + [
    (160.0, [(-0.07, 0.0), (-0.04, 5.0), (0.08, 5.0), (0.16, 2.5), (0.26, 0.0)])]

# ---------- c34 (series 2): critics on the c33 render ----------
# critic C #4 (tools WIND_REP_PORTATO): the motif's slurred repeat "eighth -> tenuto quarter" on one pitch (bars 28, 34,
# 59, 78, 79, 104, 108, 128, 132, 161, 168) is re-tongued (gap and CC11 fall; horns WIND_REP_RETONGUE_BY)
WIND_REP_PORTATO = True
# critic A #2 (tools PORTATO_TAIL_JOIN): the note after a re-tongued mid-slur tenuto joins from it (Horn 1 415, Oboe 1
# 407, Flute 1 395, Flutes/Oboe 2 633/639.5). C #4's notes are a slur's last tenuto (the next note starts a new slur),
# so the two rules touch different notes; a tenuto that is both keeps its re-tongue gap before and joins after
PORTATO_TAIL_JOIN = True
# critic C #3 (tools HP_NIENTE, HELD_DECRESC_DB): decrescendos into rests fall two steps; held-note decrescendos -3 dB
HP_NIENTE = {"steps": 2, "rest_qn": 1.0}
HELD_DECRESC_DB = {"wind": 3.0, "string": 3.0}
# not on the fitted solo contours (c33 Clarinet 1 bars 45-46 with its pp target; c28 coda cello steps) nor into the
# final chord (the kit's c22 lesson: a release after a ramp into a fermata chord raised the chord)
HELD_DECRESC_SKIP = {"Clarinet 1": [180.0], "Violoncellos": [692.0, 720.0], "Violins I": [720.0], "Violins II": [720.0],
                     "Violas": [720.0], "Double basses": [720.0]}
# critics C #2 + B #1, bars 122-126 as one shape. C #2: the brass fff > over bar 123 is untargeted on the trumpets,
# Horns 1-2 and Trombone 2 (one 14 CC step; the trumpet roles and the _all ramp rose inside it): f, the brass's printed
# goal in bar 124 (Horns 3-4 and Trombone 1 already go to their printed f). B #1: the low entries of bars 124-125 carry
# no printed mark after the fff of bar 122 and played at CC 121-124 (Bassoon 2 and the contrabassoon the loudest stems
# at 496, +54 CC over the median of the other tracks): the section's printed f of bar 124 on the bass trombone, bass
# clarinet and Bassoon 1 (new notes at 492); the shared-staff hairpin for Bassoon 2 and the contrabassoon, whose G2/G1
# is held through 492: a decrescendo 492-496 to f (no step inside the held note), then their printed > p/pp at 496
HP_TARGET_AT = dict(HP_TARGET_AT, **{s_: {**HP_TARGET_AT.get(s_, {}), 488.0: "f"}
                                     for s_ in ("Tpt1", "Tpt2", "Tpt3", "Hn1", "Hn2", "Tbn2")})
HP_TARGET_AT = dict(HP_TARGET_AT, **{s_: {**HP_TARGET_AT.get(s_, {}), 492.0: "f"} for s_ in ("Bn2", "Cbn")})
SHARED_DYN = dict(SHARED_DYN, **{t_: list(SHARED_DYN.get(t_, [])) + [(492.0, "f")]
                                 for t_ in ("Bass trombone", "Bass clarinet", "Bassoon 1")})
SHARED_HP = dict(SHARED_HP, **{t_: list(SHARED_HP.get(t_, [])) + [(492.0, 496.0, "decresc")]
                               for t_ in ("Bassoon 2", "Contrabassoon")})
# critic A #3b: letter H, the Violins I/II ff accented phrase heads after rests at 521 (printed down-bow) and 529 played
# the Leg Slur first-note layer (weight +0.2 s late): fresh Sus MAX strokes (the ROW_TRIM_DB Sus row trims apply)
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{t_: DOWNBOW_STROKE_AT.get(t_, []) + [521.0, 529.0]
                                               for t_ in ("Violins I", "Violins II")})
# critic A #5: bar 12, the printed bow changes on tied notes: Violins I down-bow at 44, Violins II and basses up-bow at
# 47 (the frozen automatic re-bows sat at 44.835 / 46.532 / 46.003); the fitted shapes move with their points
# (build/rebow_fills.json re-keyed) and are refitted from the c34 render
for t_, a_, b_ in (("Violins I", 44.835, 44.0), ("Violins II", 46.532, 47.0), ("Double basses", 46.003, 47.0)):
    REBOW_AT = dict(REBOW_AT, **{t_: sorted(b_ if abs(q_ - a_) < 1e-3 else q_ for q_ in REBOW_AT[t_])})
# critic A #6 (test): the final ppp harp chord (724, 36/43/48 at v46) fell 17 dB in 2 s, under its Pluck p layer: the
# mp layer (v62) with a level cut that keeps the onset where it was (to be set from the render by a step)
# (reverted in c35: the mp layer decayed the same way; the cause was the patch envelope, see the c35 block)
# VEL_SET["Harp"] = {**VEL_SET["Harp"], 724.0: 62}
# LEVEL_SHAPES["Harp"] = LEVEL_SHAPES.get("Harp", []) + [[(723.9, 0.0), (724.0, -6.0), (727.5, -6.0), (727.6, 0.0)]]

# critic A #4: bar 32, the Violins I/II level (accent body and roles, -4.5 / -5.9 dB) returned to 0 over 125.84-126.03
# while the half note's release sounded into the 0.88 qn rest (1-5 kHz +6 dB at the release): held to 126.2
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(125.84, 0.0), (125.98, -0.56), (126.0, -3.94), (126.03, -4.5),
                                                          (126.2, -4.5), (126.3, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(125.84, 0.0), (125.98, -1.5), (126.0, -4.4), (126.03, -5.9),
                                                           (126.2, -5.9), (126.3, 0.0)]]
# critic B #2: letter G bars 118-119, the held ff harmony under the moving theme took the swell_sost rise (SOST_SUSTAIN_DB
# 2.5 dB from 40% of each note) as an unprinted crescendo (Horns a2 4-5 dB over Violins I in every breath of the
# melody): counter-ramps on the harmony tracks only (ARRIVAL_HOLD_SPANS and the c28 plateau kept)
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES.get("Horns a2", []) + [[(470.7, 0.0), (474.6, -4.0), (474.85, 0.0)]]
for t_ in ("Trombone 1", "Trombone 2", "Bass trombone", "Bassoon 1"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(470.7, 0.0), (474.6, -2.3), (474.85, 0.0)]]
LEVEL_SHAPES["Tuba"] = LEVEL_SHAPES.get("Tuba", []) + [[(470.7, 0.0), (474.6, -1.5), (474.85, 0.0)]]
# critic A #4 follow-up (simulated on the c33 stems): with the role held, the Violins II release at the end of the
# div. sul tasto tremolo still stood 8-10 dB over the tremolo body (617.94-618.05, the sample's release; c32 +10.2),
# and the Violins I bar-83 release 5 dB over its stepped body: release notches (as 565.52 in c33)
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(617.9, 0.0), (617.94, -7.0), (618.06, -7.0), (618.1, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(328.98, 0.0), (329.02, -5.0), (329.3, -5.0), (329.34, 0.0)]]
# critic C #3 follow-up (simulated): two held decrescendos still rose with HELD_DECRESC_DB (Oboe 1 bar 42 166-168 +4.5 dB,
# the sample swelling 6 dB from +0.4 qn; Clarinet 1 bar 41 160-164 +1.4, a swell at 162.7-163.1): exact counter-shapes
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES.get("Oboe 1", []) + [[(166.2, 0.0), (166.4, -3.0), (167.0, -4.0), (167.5, -6.0),
                                                           (167.8, -6.0), (167.85, 0.0)]]
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(162.2, 0.0), (162.7, -3.0), (163.1, -4.0), (163.85, -4.0),
                                                           (163.9, 0.0)]]
# critic B #5 (partial, simulated on the c33 stem): the 22in K Crash Long sample's ring above 5 kHz decays about 11 dB/s
# and by 644 its 8-16 kHz band is 43 dB under its 0.5-1 kHz (the top octave is gone; 10-20 kHz then sits level with 5-10
# kHz, the noise floor). B's +17 dB at 644 would have lifted the mid ring and that floor, not the shimmer. A smaller lift
# keeps the shimmer audible one beat longer (crash minus master 5-20 kHz at 639/640/641: -13.5/-19.7/-25.7 ->
# -11.3/-15.6/-20.8 dB) and stops at +12
LEVEL_SHAPES["Crash cymbals"] = [[(636.0, -34.0), (636.25, -34.0), (636.75, -6.0), (637.2, -4.0), (638.0, 2.5),
                                  (638.5, 6.0), (640.0, 10.0), (642.0, 12.0), (644.0, 12.0), (646.0, 6.0), (648.0, -5.0),
                                  (652.0, -5.0)]]

# ---------- c34 stem fix (level only, measured on the c34 render) ----------
# C #1 follow-up: c34 rendered the low register as c32 (unchanged tracks within 0.5 dB per band; master loud-frame 60-100
# Hz re 250-2000 Hz -16.5 dB, c33 -20.4), so the bar-12 re-bow rows (A #5) were refitted on c34 (build/rebow_fills.json,
# only Violins I 44, Violins II 47, Double basses 47 merged)
# A #3a follow-up: with no vibrato dip the Violins I 272 stroke opened 6.7 / 4.7 dB under its body (c33's stem-fixed
# front, now removed, -1.9 / -3.3): a smaller front lift
LEVEL_SHAPES_S["Violins I"] = LEVEL_SHAPES_S["Violins I"] + [(272.0, [(-0.07, 0.0), (-0.04, 4.0), (0.1, 4.0), (0.2, 1.5), (0.3, 0.0)])]
# C #4 follow-up: the removed v221 fills had been holding up the Clarinet 1 motif eighths: 107.5 / 507.5 / 639.5 sat 6-10 dB
# under their tenutos (C's target: within 2 dB): exact lifts on the eighth only, ending before its re-tongue gap
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [
    [(107.395, 0.0), (107.42, 4.0), (107.68, 4.0), (107.716, 0.0)], [(507.395, 0.0), (507.42, 4.0), (507.68, 4.0), (507.716, 0.0)],
    [(639.417, 0.0), (639.44, 4.0), (639.74, 4.0), (639.775, 0.0)]]
# C #4 follow-up: the horn repeats (Horn 2 232, Horns a2 314) still dipped only 1.0 / 1.6 dB with the horns' 0.10 s gap and
# 12 CC fall (the kit's c13-c15 brass lesson: a volume dip separates Hollywood Brass notes, a gap does not): -4 dB in the gap
LEVEL_SHAPES["Horn 2"] = LEVEL_SHAPES.get("Horn 2", []) + [[(231.65, 0.0), (231.68, -4.0), (231.83, -4.0), (231.85, 0.0)]]
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES["Horns a2"] + [[(313.66, 0.0), (313.69, -4.0), (313.875, -4.0), (313.893, 0.0)]]
# C #3 follow-up: Oboe 1's held fff > in bar 123 still rose 0.9 dB: a further -2.5 dB to the hairpin end
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(488.3, 0.0), (491.4, -2.5), (491.68, -2.5), (491.75, 0.0)]]
# B #1 follow-up: Bassoon 2's bar-125 G2 still sat level with the Violins I melody at 496-497 (A-weighted re M -7.5 / -6.6
# against -6.0 / -5.6): -2 dB through the held note
LEVEL_SHAPES["Bassoon 2"] = LEVEL_SHAPES.get("Bassoon 2", []) + [[(495.9, 0.0), (496.0, -2.0), (503.9, -2.0), (504.0, 0.0)]]

# ---------- c35 (series 2): critics on the c34 render ----------
# critic A #1 (coordinator: a memory test): a "Cello solo" track (Celli KS Master DIV A, Close only, rows Leg Slur / Leg
# BC / Leg Port MAX) for v621's coda "Solo espr." (Vc 680-694), the section resting 679.5-696 (TRACK_WINDOWS). REMOVED in
# c35 on the measured memory: the c35 project opened fresh settled at 46.55 GiB (footprint, 0 compressed, 12 min) with the
# 34th instance; deleting that one track in the running session brought it to 45.80 GiB (-0.75 GiB). The 33-track
# project already settles at the brief's limit (about 45 GB; renders add 1-2 GiB), so the solo instance does not fit
# unless memory is freed elsewhere first. The c35 render was refused (audio device), so its attack probe was not
# measured. Kept below, commented, for a later cycle that frees memory (the copied per-onset rows, the lead-span move,
# and the HP_GAIN_IN_WINDOW skip list):
# TRACKS = TRACKS + [("Cello solo", ["Vc"], S + "Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib", "string", 0.35)]
# _VSW = [(679.5, 696.0)]
# TRACK_WINDOWS = {**TRACK_WINDOWS, "Cello solo": (_VSW, True), "Violoncellos": (_VSW, False)}
# _in_vs = lambda q_: any(a_ - 1e-6 <= q_ < b_ - 1e-6 for a_, b_ in _VSW)
# LEVEL_SHAPES["Cello solo"] = [s_ for s_ in LEVEL_SHAPES["Violoncellos"] if _in_vs(s_[0][0] + 0.1) and _in_vs(s_[-1][0] - 0.1)]
# LEVEL_SHAPES_S["Cello solo"] = [r_ for r_ in LEVEL_SHAPES_S["Violoncellos"] if _in_vs(r_[0])]
# NOTE_TRIM_RAMP_S["Cello solo"] = {q_: v_ for q_, v_ in NOTE_TRIM_RAMP_S["Violoncellos"].items() if _in_vs(q_)}
# PORT_TARGETS["Cello solo"] = {q_: v_ for q_, v_ in PORT_TARGETS["Violoncellos"].items() if _in_vs(q_)}
# HELD_DECRESC_SKIP["Cello solo"] = [q_ for q_ in HELD_DECRESC_SKIP["Violoncellos"] if _in_vs(q_)]
# LEAD_SPANS["Cello solo"] = [(a_, b_) for a_, b_ in LEAD_SPANS["Violoncellos"] if _in_vs(a_)]
# the lead line of the coda (phrase tops, the apex hold of the tempo map at 692) follows the solo track: the section's span
# there is moved, not copied (the section has no notes in it; lead_line() took the first listed span and lost the hold)
# LEAD_SPANS["Violoncellos"] = [(a_, b_) for a_, b_ in LEAD_SPANS["Violoncellos"] if not _in_vs(a_)]
# for tb_ in (LEG_ART_EXTRA_S, LEG_MIN_GAP_S, LEG_CAP_FRAC):
#     tb_["Cello solo"] = tb_["Violoncellos"]
# tools HP_GAIN_IN_WINDOW: the solo track takes no hairpin gain held over from the section's music before 679.5 (it had
# carried the +9 dB of the crescendo into the bar-170 fermata to 683.5); the windowed tracks fitted before c35 keep the old
# behaviour (their shapes were fitted on it: the filter moved Horns a2 entries 311/664.5 by +5 dB and Horn 1 643.75-653 by -3)
# HP_GAIN_IN_WINDOW_SKIP = ("Horn 1", "Horn 2", "Horns a2", "Violoncellos")
# (active, outside the removed test: the c13 a2 windows keep the hairpin behaviour their shapes were fitted on)
HP_GAIN_IN_WINDOW_SKIP = ("Horn 1", "Horn 2", "Horns a2")
# SOLO_NO_BOOST = tuple(SOLO_NO_BOOST) + ("Cello solo",)   # "Solo espr." keeps the section's espr. boost (+3), as in c34
# assert len(LEVEL_SHAPES["Cello solo"]) == 4 and len(LEVEL_SHAPES_S["Cello solo"]) == 1, (LEVEL_SHAPES["Cello solo"], LEVEL_SHAPES_S["Cello solo"])
# critic A #2 (with build_reaper.py mix key env_sustain on the Harp): revert of the c34 mp test above
# critic A #3 (tools NOTE_END_AT): bar 84, the celli's sub. p G2 (332, 4 qn) released 0.12-0.2 s after its note-off at
# 336.0, under the solo pickup's +14 dB level step (master 10 dB over both sides at 336.29-336.37): it ends 0.5 qn early,
# inside its last beat, and the c32 release notch moves with it, so the release trail falls under the notch
NOTE_END_AT = {"Violoncellos": {332.0: 335.5}}
_vn85 = [(332.5, 0.0), (332.9, -3.0), (333.1, -5.0), (334.0, -5.0), (334.6, -2.0), (335.3, -2.0), (335.9, -3.0),
         (335.98, -9.0), (336.2, -9.0), (336.26, 0.0)]
assert _vn85 in LEVEL_SHAPES["Violoncellos"]
LEVEL_SHAPES["Violoncellos"] = [[(332.5, 0.0), (332.9, -3.0), (333.1, -5.0), (334.0, -5.0), (334.6, -2.0), (335.3, -2.0),
                                 (335.42, -3.0), (335.48, -9.0), (336.2, -9.0), (336.26, 0.0)] if s_ == _vn85 else s_
                                for s_ in LEVEL_SHAPES["Violoncellos"]]
# critic A #4 (tools PICKUP_LIFT_TAIL_S): the lifted wind/brass pickups fell back 2-12 dB within 10 ms of the target's
# moved onset while the pickup's sample still sounded in the legato transition (Clarinet 1 505 dip 9.9 dB, master 6.9;
# simulated on the c34 stems: 2.1 / master 2.0). Strings keep the old release (their leads are 0.17 s)
PICKUP_LIFT_TAIL_S = {"wind": (0.04, 0.08), "brass": (0.06, 0.08),
                      # the oboes' transitions are shorter: at 0.04 s Oboe 1 313 / Oboe 2 409 (lifts 12 / 9.3 dB) stood
                      # 2.9 / 3.8 dB over the louder body on 200 ms (simulated; c34 0.0 / 3.0)
                      "Oboe 1": (0.02, 0.06), "Oboe 2": (0.02, 0.06)}
# critic B #1 (overrides the c32 damp shape on purpose; coordinator agreed): bars 123-124, the ring rose +3 -> +7 dB into
# the printed "damp gradually" of bar 124 and, after c34 cut the brass and _all over bars 123-125, stood 7.8-9.7 dB over
# the mf melody (Violins I / Oboe 1). Held at +3 through bar 123, then falling from 492 (simulated on the c34 stems:
# tam-tam re M at 489-496 -7.1..-13.3, Oboe 1 level with it at 493 and on top from 494; stroke and 484-488 unchanged)
_tt32 = [(485.0, 0.0), (488.0, 3.0), (492.0, 7.0), (500.0, -5.0), (504.2, -5.0), (504.4, 0.0)]
assert _tt32 in LEVEL_SHAPES["Tam-tam"]
LEVEL_SHAPES["Tam-tam"] = [[(485.0, 0.0), (488.0, 3.0), (492.0, 3.0), (496.0, -2.0), (500.0, -7.0), (504.2, -7.0), (504.4, 0.0)]
                           if s_ == _tt32 else s_ for s_ in LEVEL_SHAPES["Tam-tam"]]
# critic B #2: letter F bar 98, the low octave of the ff tune (Violins II sul G) 4.2-5.5 dB over the upper octaves on the
# downbeat (the c34 early fill 388) and on the pickup into bar 99: the fill kept, both lowered 4 dB
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(387.8, 0.0), (387.95, -4.0), (389.0, -4.0), (389.25, 0.0)],
                                                           [(390.9, 0.0), (391.0, -4.0), (391.95, -4.0), (392.05, 0.0)]]
# critic B #3: bars 107-108, the bass clarinet's p espr. answer 6.6-10.4 dB under the violas' held notes (both p espr.;
# the violas carry the c33 lead-span lifts): the held viola notes -3.5 (the moving notes keep their lifts), bass clarinet +2.5
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [[(424.9, 0.0), (425.1, -3.5), (427.4, -3.5), (427.6, 0.0)],
                                                           [(429.4, 0.0), (429.6, -3.5), (430.4, -3.5), (430.6, 0.0)]]
LEVEL_SHAPES["Bass clarinet"] = LEVEL_SHAPES.get("Bass clarinet", []) + [[(424.4, 0.0), (424.5, 2.5), (431.4, 2.5), (431.6, 0.0)]]
# critic B #4: coda bars 175-179, the pp espr. solos (Clarinet 1, then Violins I) cleared the pp chorale by only 0.5-1 dB
# on four beats (Trombone 1 at 711/713, the celli at 701/703, Violins II and Trombone 1 at 699): the accompaniment lowered
# under the solos (kit LEARNINGS 13; simulated margins 2.1-7.5 dB, master -0.5..-1.4 dB)
LEVEL_SHAPES["Trombone 1"] = LEVEL_SHAPES.get("Trombone 1", []) + [[(698.5, 0.0), (699.0, -3.0), (715.5, -3.0), (716.25, 0.0)]]
for t_ in ("Trombone 2", "Bass trombone"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(698.5, 0.0), (699.0, -3.0), (711.75, -3.0), (712.25, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(699.75, 0.0), (700.0, -2.5), (706.75, -2.5), (707.25, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(698.75, 0.0), (699.0, -2.5), (700.25, -2.5), (700.75, 0.0)]]
# critic B #5: bar 111, Horn 1's p cresc. A-flat4 (moved onset 439.80) sags 12 dB in its middle (the 1FH KS Master's p
# layer on A-flat4; CC1/CC11 rise smoothly), 10-16 dB under Horns 2-4: an exact shape over the sag
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(439.85, 0.0), (439.9, 4.0), (440.75, 4.0), (441.4, 10.0), (442.6, 13.0),
                                                     (443.2, 10.0), (443.8, 8.0), (443.89, 0.0)]]
# c35 actor, after the render (stem fix; critic B #4's give-back): the B #4 accompaniment cuts took the master's bars
# 175-178 down 0.8-1.4 dB (the delivery ride is at its cap there, so the mp3 coda fell as much; delivered span 19.2 ->
# 19.5 dB, target 16-19): _coda26 -3.5 -> -2.5 dB on every track over the solos (the solo margins are unchanged),
# back to -3.5 with Trombone 1's release at bar 180 (the final bars, which B #4 did not lower, stay as in c34)
_c26n = [(695.5, 0.0), (695.875, -2.5), (715.5, -2.5), (716.25, -3.5), (732.0, -3.5)]
assert _coda26 in LEVEL_SHAPES["_all"] and _coda26 in LEVEL_SHAPES["Tam-tam"]
LEVEL_SHAPES["_all"] = [_c26n if s_ == _coda26 else s_ for s_ in LEVEL_SHAPES["_all"]]
LEVEL_SHAPES["Tam-tam"] = [_c26n if s_ == _coda26 else s_ for s_ in LEVEL_SHAPES["Tam-tam"]]

# ---------- c36 ----------
# Dan's listening note on c35 ("around 2:43 the audio gets suddenly super soft, sounds like a glitch") and critic C #1:
# bar 62's sub. p. Tools: SUBITO_FRESH (score_to_parts.py; the Violins I/II sub. p notes are no longer legato targets
# led 0.2 s into the crescendo's level) and SUBITO_TAIL (build_reaper.py vol_points: the envelope falls 4 dB at the new
# note's moved onset and the rest over 0.35 s, so the forte's hall tail decays under the p). The c02/c10 shapes ending at
# 243.94 (_hp236, _hp238) and _subp are kept: the fall is redistributed in time, its depth is unchanged (12 dB, c30 11)
# CC7 test (coordinator: does CC7 act before the Opus hall?): Trombone 1, the bar-170 fermata tail (note-off 679.0, rests
# to 695.8): CC7 127 -> 32 (-12 dB) 0.8 s after the cut-off, held 1.0 s, back over 0.5 s. Post-hall: a 12 dB step in the
# tail; pre-hall (voices only): no step once the release voices are done. CC7 127 from qn 0 (the default is unknown:
# compare the whole stem with c35)
CC7_POINTS = {"Trombone 1": [(679.32, 32), (679.72, 32), (679.77, 45), (679.82, 64), (679.87, 90), (679.92, 110),
                             (679.97, 127)]}
# critic A #2: the 1st Violins KS Master's "Stac RRx14" row plays the "V1 Staccatissimo" samples (read from the .oib:
# regions under 1st Violins/HS Cl V1/V1 Staccatissimo/... StacSs), its "Staccatissimo RRx9" row the "V1 Stac" samples; the
# other sections' Stac RRx9 rows play staccato. Violins I printed staccatos (bar 30, the bar-94 fugato entry, bars 95-96)
# on the staccato samples; the row trim moves with the row; the lead of the slower staccatissimo row (0.05) back to the
# violas' 0.03 (full rebuild of Violins I: row load)
STAC_ROW = {"Violins I": "Staccatissimo RRx9"}
ROW_TRIM_DB["Violins I"] = {"Sus MAX": (-1.5, 80), "Staccatissimo RRx9": (-3.0, 80)}
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Violins I": 0.03})
# critic B #1: bars 158-161, Horn 3 carries Horns 3-4 a2 (find_unisons +3 dB, fff dyn trim -0.2 against -3.7 on Horns
# 1-2/a2) and stood 1-4 dB over the horns and trumpets that have the tune (634: the loudest brass stem by 3.9 dB)
LEVEL_SHAPES["Horn 3"] = LEVEL_SHAPES["Horn 3"] + [[(627.8, 0.0), (627.87, -3.0), (633.82, -3.0), (633.87, -4.5),
                                                   (635.9, -4.5), (635.94, -3.0), (641.85, -3.0), (641.89, 0.0)]]
# critic C #2: the ff of letter K (bar 158) reached 1.3-1.8 dB over the other ff tuttis and only 1.8 dB under bar 160's
# fff (delivered), and the 22-staff crescendo of bar 159 grew a median 2.0 dB: bar 158 down 2 dB, released over bar 159
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(627.875, 0.0), (628.375, -2.0), (632.0, -2.0), (635.375, 0.0)]]
# critic C #4: bar 122's fff tremolo violins entered 6-7 dB under their own crescendo (envelope -9/-15 dB at 484: the
# c02 roles, c08 _b122 -3 set when the v221 violins led the chord by 4-6 dB, and _all -1.6): the _b122 violin cuts out,
# and every track -0.5 dB over bar 122 to keep bar 160 over bar 122
for t_ in ("Violins I", "Violins II"):
    assert _b122(-3.0) in LEVEL_SHAPES[t_], t_
    LEVEL_SHAPES[t_] = [s_ for s_ in LEVEL_SHAPES[t_] if s_ != _b122(-3.0)]
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(483.875, 0.0), (484.25, -0.5), (492.0, -0.5), (492.5, 0.0)]]
# critic C #5: the delivery limiter's 2.9 dB was one 80 ms duck at qn 677.41 (bar 170's accented ff chord, a phase crest
# of the low brass and basses): a -3 dB notch on those four tracks (refit if the top pre-limiter peak moves)
for t_ in ("Trombone 1", "Trombone 2", "Tuba", "Double basses"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(677.33, 0.0), (677.37, -3.0), (677.49, -3.0), (677.53, 0.0)]]
# critic B #3: bar 141's ff timpani A-flat2 stroke (560) 3 dB louder than every other ff stroke and 6.4 dB over the
# melody: a step at full value on the attack, held to the next stroke (kit LEARNINGS 13)
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(560.03, 0.0), (560.07, -3.5), (563.95, -3.5), (564.05, 0.0)]]
# critic B #4: bar 156's mf harp chord (620) the loudest of 140 harp attacks, 4.8 dB over the violins' mf entry (A) and
# louder against the texture than the f chord after it: a step on the attack, held to 624
LEVEL_SHAPES["Harp"] = LEVEL_SHAPES.get("Harp", []) + [[(619.95, 0.0), (619.98, -4.5), (623.9, -4.5), (623.97, 0.0)]]
# critic B #5: bar 72, Trombone 2's held C4 (the Solo Trombone sample's own bloom, +5.3 dB while the envelope fell) the
# loudest stem over 287-288.5 by 4.1-4.6 dB, over Trombone 1's E-flat4 at the top of the pair
LEVEL_SHAPES["Trombone 2"] = LEVEL_SHAPES.get("Trombone 2", []) + [[(286.4, 0.0), (287.0, -4.0), (288.1, -4.0), (288.3, 0.0)]]

# ---------- c36 stem fix (level only, measured on the c36 render) ----------
# critic A #1 fallback (b): Clarinet 1's re-tongued accents rendered bright again (2-5 kHz first 80 ms minus body
# 0.15-0.45 s: 414 +7.8 dB as in c35, 422 +4.0 -> +7.5): the c27 front cut on both for this render's state
# (re-classify after each render; A #1's structural CC1 map for the clarinets is deferred)
LEVEL_SHAPES_S["Clarinet 1"] = LEVEL_SHAPES_S["Clarinet 1"] + [
    (q_, [(-0.02, 0.0), (0.0, -7.5), (0.12, -7.5), (0.30, 0.0)]) for q_ in (414.0, 422.0)]
# critic A #5 follow-up: the recap pp pizz. with the step trims measured a median -16.1 dB re master (c35 -18.5,
# exposition -14.4; spread 9.2 -> 5.2 dB): +1.5 dB over the passage
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(583.85, 0.0), (583.9, 1.5), (617.2, 1.5), (617.3, 0.0)]]

# ---------- c37 ----------
# Dan's listening notes S1 (repeated notes must be heard as separate notes) and S2 (the perceived attack centres must
# sit on the beat); critics A #1-#5 (S1), C #1-#4 (S2), B #1-#4 (levels)
# critic A #1 (S1): abutting unslurred same-pitch string repeats dipped a median 1.9 dB (stem); per-span options
# (score_to_parts.py STR_REP_DETACH: frac, same_pitch_only). Celli bars 127-130 (accelerating G2): -6 dB, 0.10 s, with
# a +1.5 dB hold as on the basses' spans (simulated stem loss 1.7 dB)
_o37 = {"max_qn": 1.0, "min_cc": 30, "frac": 0.3, "same_pitch_only": True}
STR_REP_DETACH = dict(STR_REP_DETACH, at={
    **STR_REP_DETACH["at"],
    "Double basses": STR_REP_DETACH["at"]["Double basses"] + [(56.0, 100.0, _o37), (304.0, 332.0, _o37)],
    "Violoncellos": [(504.0, 520.0, dict(_o37, dip_db=-6.0, dip_s=0.10, ramp_s=0.015))],
    "Violas": [(86.0, 100.0, _o37), (245.0, 274.0, _o37), (440.0, 463.0, _o37), (552.0, 572.0, _o37),
               (628.0, 644.0, _o37)],
    "Violins II": [(86.0, 100.0, _o37), (536.0, 548.0, _o37)]})
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES.get("Violoncellos", []) + [[(503.85, 0.0), (503.95, 1.5), (519.85, 1.5),
                                                                         (519.95, 0.0)]]
# critic A #2 (S1): the fugato subject's quarter after its same-pitch staccato eighth (Vc 340, Vla 352, Vln II 364,
# Vln I 376 / 380.5) played Leg Slur MAX's first-note layer (6-12 dB under the eighth at its onset): a fresh stroke
STR_REP_AFTER_STAC = {"max_qn": 1.0, "max_gap_qn": 0.5}   # (Vln I 380.5, after an eighth rest, keeps its Leg BC join into 381)
# critic A #3 (S1, MANUAL-GAPS #2): the HO repetition rows, an A/B on four tracks (Contrabassoon 520-548 is the
# control on the old re-tongue). Contrabassoon bars 27-32 quarters (ff), Bassoon 1's bar-34 motif repeat and the bar-88
# fugato entry, Horn 4's bars 117-125 whole-note G3 repeats on "LegRep RRx4"; Clarinet 1's motif repeats of bars 27,
# 127 and 160 (whole slurs) on "Leg Slur Rep"
REP_ROW = {"Contrabassoon": [(104.0, 126.0, "LegRep RRx4")],
           "Bassoon 1": [(131.9, 132.1, "LegRep RRx4"), (350.4, 352.1, "LegRep RRx4")],
           "Clarinet 1": [(107.0, 109.0, "Leg Slur Rep"), (507.0, 509.0, "Leg Slur Rep")],
           "Horn 4": [(464.0, 501.0, "LegRep RRx4")]}
# critic A #4 (S1, MANUAL-GAPS #10): repeated timpani strokes alternate hands (right-hand samples at pitch + 24)
TIMP_RH_ALT = {"max_gap_s": 0.8, "add": 24}
# critic A #5: Oboe 1's accented F5 at 113 (a legato target led 0.03 s): its -11 dB step (note trim -5 + fitted -6)
# ramps in over 0.1 s from the score onset, after the front has sounded (0.05-0.10 s +10 dB over the body). A
# counter-shape puts most of the step at the score onset + 0.03 s. Rendered with -7.7 dB at +0.03 and -2 dB held over
# 0.10-0.16 s: front (0-0.15 s) minus body +7.6 -> +0.9 dB, under the 2-4 dB accent rule; c37 stem fix: -5.5 at +0.03,
# no hold (simulated about +2.6)
LEVEL_SHAPES_S["Oboe 1"] = LEVEL_SHAPES_S.get("Oboe 1", []) + [
    (113.0, [(-0.03, 0.0), (0.03, -5.5), (0.10, 0.0)])]
# critic C #1 (S2), slow tempo: re-tongue leads under 100 bpm (no lead before); the basses' bar changes next to re-bowed
# notes take the abut lead; soft wind legato targets (v70 or less) start earlier
RETONGUE_LEAD_SLOW_S = {"Bassoon": 0.06, "string": 0.07, "wind": 0.04, "brass": 0.05}
ABUT_LEAD = dict(ABUT_LEAD, **{"Double basses": dict(ABUT_LEAD["Double basses"], rebow_ok=True)})
LEG_VEL_EXTRA_S = {"Bass clarinet": (70, 0.09), "Oboe": (70, 0.05), "wind": (70, 0.04)}
# critic C #3 (S2): path offsets (medians of the perceived attack in the Allegro / Poco meno mosso against +0.01 s):
# timpani strokes +0.031 (TIMP_DELAY_S 0.045 -> 0.02); brass entries at CC11 under 81 -0.034 (soft value 0.10 -> 0.06);
# the loud entries of Trumpet 3 / Trombone 1 / Horn 1 / Horn 2 / Trumpet 2 -0.045..-0.013; brass first notes on Leg Slur
# MAX -0.05 (art extra 0.06 -> 0.02); string staccatos +0.018..+0.046; tremolo joins / entries -0.066 / -0.093 (0.30 ->
# 0.22, 0.08 -> 0.04: about 0.7 of the offset, the c08/c09 holes); Oboe legato +0.028 / +0.056; Oboe 1 / Flute 2
# re-attacks +0.029 / +0.033; Flute 2 legato +0.039
TIMP_DELAY_S = 0.02
ENTRY_LEAD_S = dict(ENTRY_LEAD_S, **{"Horn 1": (0.06, 0.09, 0.05), "Horn 2": (0.06, 0.08, 0.05),
                                     "Trumpet 2": (0.06, 0.09, 0.05), "Trumpet 3": (0.06, 0.07, 0.05),
                                     "Trombone 1": (0.06, 0.07, 0.05), "brass": (0.06, 0.05)})
ENTRY_LEAD_ART_S = dict(ENTRY_LEAD_ART_S, brass=dict(ENTRY_LEAD_ART_S["brass"], **{"Leg Slur MAX": 0.02}))
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Violins I": 0.045, "Violas": 0.04, "Violins II": 0.035, "Violoncellos": 0.025})
TREM_JOIN_LEAD_S = 0.22
TREM_ENTRY_LEAD_S = 0.04
LEG_LEAD_S = {"Flute 2": 0.05, **dict(LEG_LEAD_S, Oboe=0.05)}
RETONGUE_LEAD_S = dict(RETONGUE_LEAD_S, **{"Oboe 1": 0.07, "Flute 2": 0.07})
# critic C #2 (S2): 127 legato targets whose perceived attack and crossover both stray: per-onset values in
# build/leg_leads.json (C's totals; Oboe 1 minus the +0.02 family change; wind targets at v70 or less minus their
# LEG_VEL_EXTRA_S)
# critic C #4 (S2): phrase-end cut-offs: strings and brass end before the written end before a rest of 1 qn or more;
# the attacca chord's celli, violas and Horn 3 end with the violins
CUTOFF_EARLY_S = {"string": 0.05, "brass": 0.04}
NOTE_END_AT = dict(NOTE_END_AT, **{"Violoncellos": {**NOTE_END_AT["Violoncellos"], 712.0: 727.85},
                                   "Violas": {724.0: 727.9}, "Horn 3": {720.0: 727.9}})
# critic B #3: bar 152, the cor anglais's dolce A4 (604) peaks 4.5 dB over its sibling figures, over the tune; the
# step is in place at the hairpin peak (the note's start)
NOTE_TRIM_RAMP_S["Cor anglais"] = {**NOTE_TRIM_RAMP_S.get("Cor anglais", {}), 604.0: 0.1}
# critic B #4: bars 56-59, Horn 2's E-flat4 / C-sharp4 / E-flat4 drop 8-9 dB under Clarinet 1 in their espr. unison
NOTE_TRIM_RAMP_S["Horn 2"] = {**NOTE_TRIM_RAMP_S.get("Horn 2", {}), 220.0: 0.1, 232.0: 0.1, 234.0: 0.1}

# ---------- c37 stem fix (measured on the c37 render) ----------
# critic A #3 (REP_ROW): Clarinet 1's fff motif repeat at 640 on "Leg Slur Rep" did not sound (stem -45..-57 dB against
# -22 in c36): the 639.5 note's release trail started 30 ms before the repeat, inside the row's VoiceTimer 30 ms window,
# so the repeat took the legato path (sustain-under-transition groups, no same-pitch transition) instead of the
# re-tongue groups (inferred from the .oib start modes). The bar-160 span is reverted (c36 data; the c36 audio of
# 638.2-643.0 is spliced into the c37 stem: same notes, controllers and envelope there); 108 / 508 kept (they sounded)
# critic A #2 follow-up: the fugato strokes' level against their neighbours (own-harmonic peaks): Vc 340 / Vla 352
# 2-4 dB under, Vln II 364 / Vln I 376 2-3 dB over: step trims (note_trims.json, 0.1 s ramps)
NOTE_TRIM_RAMP_S["Violoncellos"] = {**NOTE_TRIM_RAMP_S.get("Violoncellos", {}), 340.0: 0.1}
NOTE_TRIM_RAMP_S["Violas"] = {**NOTE_TRIM_RAMP_S.get("Violas", {}), 352.0: 0.1}
NOTE_TRIM_RAMP_S["Violins II"] = {**NOTE_TRIM_RAMP_S.get("Violins II", {}), 364.0: 0.1}
NOTE_TRIM_RAMP_S["Violins I"] = {**NOTE_TRIM_RAMP_S.get("Violins I", {}), 376.0: 0.1}

# ---------- c38 ----------
# critics A #1 / C #2 (S1): the c37 REP_ROW A/B failed on its 0.03 s gap (no CC11 fall): the repeats keep the
# re-tongue's own gap and fall, the gap clamped to 0.06-0.15 s (clear of the clarinet "Leg Slur Rep" 30 ms VoiceTimer,
# inside the 200 ms NoteTimer that counts from the previous note-off); brass rows (re-tongue on every note) carry only
# the same-pitch repeats. Clarinet 1's fff repeat at 640 re-tested; the bass clarinet's exposed motif repeats at 308
# (bar 78 "Solo espr.") and 428 (bar 108) on its LegRep RRx4 row (dips 2.4 / 3.6 dB in c36-c37)
REP_ROW_GAP_S = (0.06, 0.15)
REP_ROW_REPEATS_ONLY = ("brass",)
REP_ROW = dict(REP_ROW, **{"Clarinet 1": REP_ROW["Clarinet 1"] + [(638.4, 641.0, "Leg Slur Rep")],
                           "Bass clarinet": [(307.4, 308.1, "LegRep RRx4"), (427.4, 428.1, "LegRep RRx4")]})
# critic C #2 (S1): Bassoon 1's F3 at 136 (a slur head on the pitch the previous slur ended on) played Leg Slur MAX's
# first-note layer (stem dip -0.2 dB): a same-pitch slur head is re-tongued on the Sus row (generic SLUR_HEAD_REP_SUS)
# The rule also catches Oboe 1 492, Clarinet 1 512, Clarinet 2 500, Bassoon 1 372 / 448, Horn 2 448, Horn 3 500, which
# C measured at 5.4-8.0 dB on Leg Slur MAX: listed to 136 only
SLUR_HEAD_REP_SUS = {"families": ("wind", "brass"), "gap_qn": 0.25, "at": {"Bassoon 1": [136.0]}}
# critic C #5: the c37 attacca-chord ends (Violoncellos 727.85, Violas / Horn 3 727.9) overshot (celli 3-14 dB under
# c36 from the written end to +0.8 s, release spread 0.22 -> 0.41 s): back to the written ends; c35's Vc 332 entry kept
NOTE_END_AT = {"Violoncellos": {332.0: 335.5}}
# critic B #1: at both fff climaxes Violins II (tremolo double stop at 484-492; the trumpets' notes in the middle
# octave at 632-640) is the loudest pitched stem, 1.4-5.5 dB over Trumpet 1 on the same notes (B: one trumpet should
# be about twice a string section in forte): exact cuts over the two spans (the [484, 496, -4] and [628, 644, +2.5]
# roles kept), and Trumpet 1's fff dyn trim 6.6 -> 8.1 in build/mix.json (its level did not grow from ff to fff)
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [
    [(483.95, 0.0), (484.1, -3.0), (491.9, -3.0), (492.1, 0.0)],
    [(631.75, 0.0), (632.25, -4.0), (639.75, -4.0), (640.25, 0.0)]]
# critic B #2: coda bar 172, the cor anglais's p counter-line (683.5-686) stands 2-6 dB over the cello's "Solo espr."
LEVEL_SHAPES_S["Cor anglais"] = LEVEL_SHAPES_S.get("Cor anglais", []) + [
    (684.0, [(-0.3, 0.0), (-0.15, -4.0), (1.25, -4.0), (2.1, 0.0)])]
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [
    (684.0, [(-0.15, 0.0), (-0.05, 2.5), (1.25, 2.5), (1.6, 0.0)])]
# critic A #2: Horn 1's slurred tenutos in the second theme (portato on Leg Slur MAX, v100) came out as four different
# articulations (dip 189 / 201 / 589 / 601: -0.5 / 4.3 / 5.7 / 0.8 dB; tenuto minus quarter +3.9 / +2.0 / -4.9 /
# +4.8): 201 is the model; 189 / 601 get a join notch and a body trim, 589 a fill and a lift (A's values, then
# simulated on the c37 stems: body trims -2.75 / -3.0, 589 lift +4.5)
LEVEL_SHAPES_S["Horn 1"] = LEVEL_SHAPES_S.get("Horn 1", []) + [
    (189.0, [(-0.11, 0.0), (-0.09, -4.0), (-0.02, -4.0), (0.02, 0.0), (0.10, -2.75), (0.60, -2.75), (0.90, 0.0)]),
    (601.0, [(-0.11, 0.0), (-0.09, -4.0), (-0.02, -4.0), (0.02, 0.0), (0.10, -3.0), (0.60, -3.0), (0.90, 0.0)]),
    (589.0, [(-0.14, 0.0), (-0.12, 5.0), (0.08, 5.0), (0.15, 4.5), (0.98, 4.5), (1.06, 0.0)])]
# critic A #3: bar 11 (all horns p < f on one 4.69 s note): Horn 4 grew +0.4 dB (a bloom at +1.2 s as loud as the
# crescendo's end; Horns 1-3 +7.7..+8.6): a cut over the bloom
# (A's cut over the bloom alone simulated +2.9 dB: the note is flat at -44..-46 dB from +0.8 to +3.8 s; the shape
# below lays a linear crescendo under it (-50 -> -43 dB stem, fitted on c37 0.2 s frames), the end level unchanged)
LEVEL_SHAPES_S["Horn 4"] = LEVEL_SHAPES_S.get("Horn 4", []) + [
    (40.0, [(0.3, 0.0), (0.4, -1.3), (0.8, -4.2), (1.2, -5.5), (1.6, -5.5), (2.0, -3.4), (2.4, -1.8), (2.8, -0.7),
            (3.2, 0.0), (3.6, 1.0), (4.0, 0.0)])]
# critic A #3: bar 40, the trombones' p < into the sf at 160 rose one hairpin step (CC1 42 -> 64) and the master grew
# 0.3 dB into the bar-41 sf: a crescendo into an sf targets f (generic HP_SF_TARGET); brass staves only (the string and
# wind crescendos into sf at 72.5 / 144.5 / 154 were not measured)
HP_SF_TARGET = {"staves": ("Hn1", "Hn2", "Hn3", "Hn4", "Tpt1", "Tpt2", "Tpt3", "Tbn1", "Tbn2", "BTbn", "Tuba"),
                "to": "f", "from_f": "ff"}
# critic C #3: the printed "sul" spans (TextSpanner texts, not in mockup-events.tsv) as finger positions (CC70) from
# the patches' own finger-position tables; the Basses KS Master has none (its sul A at 4-11.9 / 700-711.9 is not
# rendered)
# c38 render: the default FP outside the spans was set to 20 (FP1, the FingerPosition script's value for the patch's
# fingerPosition 0) and the render showed that every earlier render had played FP4 (the start modes' default 127):
# Violins I outside the spans came out a median +1.1 dB louder and brighter (centroid +40 Hz, up to +330), the
# in-span notes that FP4 already put on the printed string were identical to c37 (0.0 dB). Default now 127; the
# Violins I / II and Violoncellos stems were spliced back to c37 audio outside the notes whose string changed
SUL_DEFAULT_CC70 = 127
SUL_SPANS = {"Violoncellos": [(3.0, 11.9, "g"), (696.0, 711.9, "g")],
             "Violins I": [(35.0, 38.9, "d"), (219.0, 224.9, "d"), (225.0, 235.9, "a"), (707.0, 728.0, "d")],
             "Violins II": [(219.0, 224.9, "d"), (225.0, 235.9, "a"), (388.0, 399.9, "g")]}

# ---------- c38 stem fix (measured on the c38 render) ----------
# critic C #2: Bassoon 1's 136 on the Sus row (SLUR_HEAD_REP_SUS) still dipped only 1.6 dB (c37 -0.2): its body sits
# 3-4 dB under the slur end before it and the old note's release fills the 0.06 s re-tongue gap. A -6 dB dip over the
# gap (the c34 horn gap dips), back to 0 at the moved onset (-0.035 s)
LEVEL_SHAPES_S["Bassoon 1"] = LEVEL_SHAPES_S.get("Bassoon 1", []) + [
    (136.0, [(-0.13, 0.0), (-0.105, -6.0), (-0.05, -6.0), (-0.035, 0.0)])]
# critic C #3 follow-up: the celli's opening sul G pickup G2 (qn 3) now plays the open G string (c37: the C string at
# FP4), as the score asks ("from the open G to the fourth position"); the open-string sample sits 5.3 dB lower
# (median -44.9 against -39.6 dB on the stem). A lift held through its legato join into the E-flat3, released over the
# E-flat3's start
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [
    (3.0, [(-0.32, 0.0), (-0.26, 4.5), (1.12, 4.5), (1.45, 0.0)])]

# ---------- c39 ----------
# critic A #2 (generic LEG_JOIN_TRIM_HOLD): a positive pitch / note trim on a note joined into a legato target ended
# over [next moved onset - 0.05, + 0.03] qn while the old note's sample still carried the line for 0.1-0.3 s: 5-11 dB
# holes (Clarinet 1 226 -> 227 and 179 -> 179.5, the +5 A-flat4 pitch trim; Oboe 1 578 -> 579, the +8 note trim). Held
# to the target's moved onset + the PICKUP_LIFT_TAIL_S hold, released by the target's score onset + 0.06 s
LEG_JOIN_TRIM_HOLD = {"wind": (0.04, 0.08), "brass": (0.06, 0.08), "string": (0.06, 0.08),
                      "Oboe 1": (0.02, 0.06), "Oboe 2": (0.02, 0.06)}
# the same hole after a string PICKUP_LIFT (Violas 146.5 -> 147: lift 6.8 dB ending at the target's moved onset, dip 6.3)
PICKUP_LIFT_TAIL_S = dict(PICKUP_LIFT_TAIL_S, string=(0.06, 0.08))
# the c24 Clarinet 1 cut on the B-flat4 at 227 started before its moved onset (inside the transition): moved after it
LEVEL_SHAPES["Clarinet 1"] = [[(227.05, 0.0), (227.15, -2.5), (227.3, -2.5), (227.7, 0.0)]
                              if s_ == [(226.85, 0.0), (226.95, -2.5), (227.1, -2.5), (227.6, 0.0)] else s_
                              for s_ in LEVEL_SHAPES["Clarinet 1"]]
assert [(227.05, 0.0), (227.15, -2.5), (227.3, -2.5), (227.7, 0.0)] in LEVEL_SHAPES["Clarinet 1"]
# Violas 428 -> 429 (bar 108 espr., led 0.275 s): 428's -2.5 trim covers the transition and 429's +3 starts at the
# score onset (envelope +1.2 -> -5.9 -> +3.1 dB, dip 7.2): A's lift over the transition
LEVEL_SHAPES_S["Violas"] = LEVEL_SHAPES_S.get("Violas", []) + [(429.0, [(-0.29, 0.0), (-0.25, 4.0), (-0.02, 4.0), (0.08, 0.0)])]
# critic A #3 (S1): Clarinet 1's slurred repeat at 310 (bar 78, A-flat5) was merged into 309.5 (dip 1.4 dB): on its
# "Leg Slur Rep" row (loaded on this track) with the row's re-tongue gap (tools: no WIND_SLUR_REP_MERGE into a REP_ROW
# note; a same-slur repeat into a REP_ROW note takes the re-tongue gap)
REP_ROW = dict(REP_ROW, **{"Clarinet 1": REP_ROW["Clarinet 1"] + [(309.4, 310.1, "Leg Slur Rep")]})
# the horns' / Trombone 1's same-pitch re-tongues in held chords dipped 0.4-2.8 dB (the 1FH 562 ms release fills the
# 0.10-0.14 s gaps): the c38 Bassoon 1 136 gap dip (-6 dB over the gap, back by the moved onset)
_gd18 = [(-0.18, 0.0), (-0.15, -6.0), (-0.065, -6.0), (-0.05, 0.0)]
LEVEL_SHAPES_S["Horn 3"] = LEVEL_SHAPES_S.get("Horn 3", []) + [
    (156.0, [(-0.22, 0.0), (-0.19, -6.0), (-0.065, -6.0), (-0.05, 0.0)]), (444.0, _gd18), (668.0, _gd18)]
LEVEL_SHAPES_S["Horn 2"] = LEVEL_SHAPES_S.get("Horn 2", []) + [
    (47.0, _gd18), (456.0, [(-0.22, 0.0), (-0.19, -6.0), (-0.105, -6.0), (-0.09, 0.0)])]
LEVEL_SHAPES_S["Trombone 1"] = LEVEL_SHAPES_S.get("Trombone 1", []) + [(384.0, _gd18)]
# critic A #4: bar 135, the celli's accented mf C3 at 536 (no slur, a new dynamic) played as a Leg BC MAX tail of the
# ff G3 (6-7 dB under its own later level for 0.9 s): a fresh stroke; its accent fit is removed (accent_fits.json) and
# refitted on this render
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violoncellos": DOWNBOW_STROKE_AT["Violoncellos"] + [536.0]})
# critic B #1: Violins II sat 4-6.5 dB under Violins I wherever the two double (patch and soft-trim gap): exact lifts on
# the doubling spans (clear of the climax cuts, the tremolo roles, the 325 body cut and the -4 role to 218.25), and a
# -1.5 dB cut on Violins I over the printed sul A of bars 55-59 (it roughly cancels the A string's gain)
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [
    [(104.75, 0.0), (105.0, 2.5), (114.5, 2.5), (114.75, 0.0)],
    [(159.75, 0.0), (160.0, 2.5), (168.0, 2.5), (168.4, 0.0)],
    [(218.75, 0.0), (219.0, 3.0), (265.0, 3.0), (265.25, 0.0)],
    [(400.25, 0.0), (400.5, 2.5), (407.0, 2.5), (407.25, 0.0)],
    [(644.25, 0.0), (644.5, 3.0), (664.0, 3.0), (664.25, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(218.75, 0.0), (219.0, -1.5), (237.0, -1.5), (237.25, 0.0)]]
# critic B #2: bars 8-11, the violas' re-bowed C4 under the pp < chord sat 6-10 dB under Violins II and the celli (its
# re-bow fills at the fitter's -6 dB clamp): an exact lift over the re-bowed span, after the fills
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [[(30.0, 0.0), (31.0, 3.0), (32.0, 5.0), (41.6, 5.0), (41.8, 0.0)]]
# critic B #4: bar 78, the bass clarinet's "Solo espr." mf tenuto at 308 lost 1.4-1.8 dB on its LegRep row (now 2-3.5
# dB under Clarinet 1's mp imitation): a lift that starts after the re-attack
LEVEL_SHAPES_S["Bass clarinet"] = LEVEL_SHAPES_S.get("Bass clarinet", []) + [(308.0, [(0.03, 0.0), (0.12, 2.0), (0.95, 2.0), (1.05, 0.0)])]
# critics B #3 / B #5: roles.json brass rows (bars 26-32, 69-72, 131-143) and Trumpet 2 dyn trims (build/mix.json)

# second render pass (coordinator, critics A #5 / C #2): the Trumpets 1-2 a2 unisons (every onset of both parts the
# same pitch: 520-524.5, bars 131-132; 664.5-679, bars 167-170) on the two-trumpet KS Master ("Trumpets a2", stem 34),
# built from Trumpet 1's rules (ALIAS_TRACKS) without its 1TP pitch trim; Trumpets 1 and 2 rest there. The single
# unison onsets 108 and 628 stay on the solo trumpets (as the horns' 108 / 528). Rendered in the second REAPER project
# (memory: the main project settles at about 46 GiB). The a2 trombones stay on Trombone 1 (critic C #2: "2 Trombones
# EXP" has no legato row, ships Close + Stage with no Main, a Stage channel wired to an "Edge" column, 700 ms release)
_TA2W = [(519.9, 525.5), (664.4, 679.5)]
TRACK_WINDOWS = {**TRACK_WINDOWS, "Trumpet 1": (_TA2W, False), "Trumpet 2": (_TA2W, False)}
ALIAS_TRACKS = {"Trumpets a2": {"source": "Trumpet 1", "windows": _TA2W, "no_pitch_trims": True,
                                "patch": B + "2 Trumpets/06 Keyswitch/2TP KS Master.oib"}}
PASS2_TRACKS = ("Trumpets a2",)
# (critic A #4, measured in parts.json) with 536 a stroke, the generic STR_ACC_AFTER_SUS (c02: an accented unslurred
# string note after a Sus note is a Sus stroke) makes the hemiola's other accented dotted halves (539, 542, 545)
# strokes too, each with its own bow and attack as printed; their accent fits (+4.5, fitted on the Leg BC version) are
# removed with 536's and all four are refitted on this render

# critic A #1 (MANUAL-GAPS #11), in the second render pass: the printed wind staccatos of the fugato doublings (Bassoon
# 1 with the violas, bars 88-90; Cor anglais with Violins II, bars 91-93; Flute 1 with Violins I, bars 94-96, and its
# bar-30 eighths) were slices of Sus MAX, still rising at their note-off (peak = note-off, pc up to +0.099 s, later
# than the string staccatos they double): on the recorded "Stac DblTng RRx9" row (loaded by default in the KS Masters,
# 340-562 ms release), velocity from the printed level. The fugato windows play on their own instance of the same patch
# in the second pass ("... stac" tracks, built from the source's rules), so the main project loads no row more;
# Bassoon 1's REP_ROW keeps the 352 repeat only (its staccato eighths left the LegRep row). Cor anglais's 0.08 s
# re-tongue lead put 362.5 at pc -0.088: -0.05 on the row
_WSTAC = [(58, 72), (72, 82), (88, 96), (114, 112)]
ART_SPANS = dict(ART_SPANS, **{
    "Bassoon 1": ART_SPANS.get("Bassoon 1", []) + [
        {"from": 350.0, "to": 360.0, "art": "Stac DblTng RRx9", "mark": "staccato", "vel_by_cc": _WSTAC}],
    "Cor anglais": ART_SPANS.get("Cor anglais", []) + [
        {"from": 362.0, "to": 372.0, "art": "Stac DblTng RRx9", "mark": "staccato", "vel_by_cc": _WSTAC}],
    "Flute 1": ART_SPANS.get("Flute 1", []) + [
        {"from": 374.0, "to": 384.0, "art": "Stac DblTng RRx9", "mark": "staccato", "vel_by_cc": _WSTAC}]})
assert (350.4, 352.1, "LegRep RRx4") in REP_ROW["Bassoon 1"]
REP_ROW = dict(REP_ROW, **{"Bassoon 1": [r_ if r_ != (350.4, 352.1, "LegRep RRx4") else (351.9, 352.1, "LegRep RRx4")
                                         for r_ in REP_ROW["Bassoon 1"]]})
RETONGUE_LEAD_ART_S = dict(RETONGUE_LEAD_ART_S, **{"Cor anglais": {"Stac DblTng RRx9": -0.05}})
# the windows start at each entry after its rest (348.5 / 360.5 / 372.5), so no note hands over between the projects
# inside a phrase; Flute 1's bar-30 eighths stay on Sus with the oboe and clarinet they double (A: optional)
_STW = {"Bassoon 1": [(348.4, 359.9)], "Cor anglais": [(360.4, 371.9)], "Flute 1": [(372.4, 383.9)]}
TRACK_WINDOWS = {**TRACK_WINDOWS, **{t_: (w_, False) for t_, w_ in _STW.items()}}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{f"{t_} stac": {"source": t_, "windows": w_} for t_, w_ in _STW.items()})
PASS2_TRACKS = tuple(PASS2_TRACKS) + tuple(f"{t_} stac" for t_ in _STW)

# ---------- c39 stem fix (level only, measured on the c39 render) ----------
# LEG_JOIN_TRIM_HOLD filled the holes it was made for (Clarinet 1 227 / 179.5 / 213 / 249 / 275.5 / 276.5 dips 11.4 /
# 8.2 / 4.7 / 4.9 / 5.0 / 5.4 -> 5.6 / 4.1 / 1.4 / 1.3 / 1.3 / 1.3 dB, Oboe 1 579 5.5 -> -0.5, Violas 429 7.2 -> 3.2,
# Violas 147 6.3 -> 2.4) but on joins that had no hole it put the old note's lift over the new note's transition: 30 ms
# bursts 2.6-4.8 dB over the louder body (Flute 1 154.5 0.5 -> 3.1, Oboe 1 556 0.9 -> 3.1, Trumpet 2 453 1.5 -> 4.8,
# Violas 121.5 2.6 -> 3.8, Violas 438 -0.5 -> 3.2). Not held there; held in part where it filled a hole but overshot
# (Flute 1 90: dip 5.7 -> 3.9, burst 1.4 -> 5.4; Clarinet 1 227 burst 3.1)
LEG_JOIN_TRIM_HOLD_AT = {"Flute 1": {154.5: 0.0, 438.0: 0.0, 90.0: 0.5}, "Oboe 1": {556.0: 0.0},
                         "Trumpet 2": {453.0: 0.0}, "Violas": {121.5: 0.0, 438.0: 0.0}, "Horn 1": {593.5: 0.0},
                         "Clarinet 1": {227.0: 0.7}}
# critic A #3 follow-up: the horn gap dips landed 4.3-8.3 dB (Horn 3 156 / 444 5.2 / 4.3, Trombone 1 384 3.9; Horn 2 47
# 7.4, Horn 3 668 7.0, Horn 2 456 8.3, target 4-6): the three deepest at -4.5 dB instead of -6
_gd18b = [(-0.18, 0.0), (-0.15, -4.5), (-0.065, -4.5), (-0.05, 0.0)]
LEVEL_SHAPES_S["Horn 3"] = [(q_, _gd18b) if (q_, s_) == (668.0, _gd18) else (q_, s_) for q_, s_ in LEVEL_SHAPES_S["Horn 3"]]
LEVEL_SHAPES_S["Horn 2"] = [(q_, _gd18b) if (q_, s_) == (47.0, _gd18) else
                            (q_, [(-0.22, 0.0), (-0.19, -4.5), (-0.105, -4.5), (-0.09, 0.0)]) if q_ == 456.0 and s_[1][1] == -6.0
                            else (q_, s_) for q_, s_ in LEVEL_SHAPES_S["Horn 2"]]
assert (668.0, _gd18b) in LEVEL_SHAPES_S["Horn 3"] and (47.0, _gd18b) in LEVEL_SHAPES_S["Horn 2"]
# critic A #4 follow-up (build/accent_fits.json): the celli's hemiola accents (now Sus MAX strokes, as the other string
# sections already played them) have no unaccented neighbours, so fit_accents.py cannot fit them; their bodies came out
# 2.6-3.3 dB under c38 without the swells. Swells as the other sections' at these onsets (Violas 4.5 / 4.1 / 2.9):
# 536 2.0 (its c38 value), 539 4.5, 542 4.5, 545 3.0
# Violins I rendered FP1-like outside its spans although its CC70 lane held 120 then 127 (c38's lane-20 render matched it
# to 0.00 dB median; Violins II and the celli matched the no-CC70 renders): spliced back to the c38 audio outside
# 218.5-237.5 (cycles/c39/actor_scripts/fpsplice39.py). FP4 inside spans now sends 127 (tools SUL_FP4_CC70), so the
# Violins I lane starts at 127 like Violins II's: a test for the next render (compare Violins I outside 218-238 with c39)
SUL_FP4_CC70 = 127
# second pass, measured on its first c39 render (cycles/c39/m39_pass2.txt; per note body, K, against c38's Trumpet 1 on
# the same notes, which carried the +3 dB unison boost): the 2TP samples sit about 6 dB over 1TP at ff and 2 dB at f at
# the same CC1 and envelope (coda notes +1.1..+8.5 dB, median +4.7, including the alias's -1.5 dB gain change; bars
# 131-132 +2.5 with B #3's +2 role), and the 1TP fits do not all suit them: the G4 pickups' lifts (664.5 / 672.5) and
# the 670 accent came out about 3 dB hot, the B4 / C5 legato notes (669, 669.5, 675.5, 676) about 3 dB cold. mix.json
# "Trumpets a2" dyn trims f 6.1 -> 5.6, ff 7.3 -> 2.6; alias-only tables below (the pass-2 track is rendered again).
# In bars 131-132 the 2TP is 5 dB brighter in 2-5 kHz than 1TP (coda +1.0): a 3.2 kHz -4 dB bell over that window
# (mix.json loud_eq)
ALIAS_TRACKS["Trumpets a2"]["tables"] = {
    "PICKUP_LIFT": {664.5: 3.9, 672.5: 3.4},
    "ACCENT_FITS": {670.0: [2.2, 1.0]},
    "NOTE_TRIMS": {669.0: 6.5, 669.5: 5.0, 675.5: 5.0, 674.5: -2.5, 676.0: 2.5, 671.5: -2.5},
    "NOTE_TRIM_RAMP_S": {676.0: 0.1, 671.5: 0.1}}
# critic A #1 follow-up (first pass-2 render): the Cor anglais staccatos on the row started on the score onset and
# perceived +0.016..+0.055 s (Violins II's -0.036..+0.004) and 1.6-4.5 dB under the violins they double (the Sus-row
# version -2..+5.5): a 0.03 s staccato lead (tools: STAC_LEAD_S for winds) and +2.5 dB over the two staccato groups;
# Bassoon 1's 356 stood 4.3 dB over the violas: -3 dB
STAC_LEAD_S = dict(STAC_LEAD_S, **{"Cor anglais": 0.03})
ALIAS_TRACKS["Cor anglais stac"]["tables"] = {"LEVEL_SHAPES": [[(362.3, 0.0), (362.4, 2.5), (363.9, 2.5), (363.95, 0.0)],
                                                               [(367.3, 0.0), (367.4, 2.5), (371.6, 2.5), (371.7, 0.0)]]}
ALIAS_TRACKS["Bassoon 1 stac"]["tables"] = {"LEVEL_SHAPES_S": [(356.0, [(-0.05, 0.0), (0.0, -3.0), (0.25, -3.0), (0.3, 0.0)])]}
# (stem fix on the second pass-2 render: per note against c38's Trumpet 1, coda median -0.2 dB, 520-524 +1.3 with the
# +2 role; 670 came out +3.8 because the alias table's "670.0" key did not replace the json's "670" (tools: same-onset
# keys now replace), 674.5 +2.9 and 669 -2.9: 674.5 0 -> -2.5, 669 5.0 -> 6.5 in the table above)

# ---------- c40 (series 2): critics on the c39 render ----------
# critic B #1 (coordinator priority): Clarinet 1's D5 at 654 (bars 164-165, mp, the top of its phrase) never sounded in
# any render c32-c39 (stem -64..-112 dB over the note): a new slur's first note led to 653.942 on the "Leg Slur" row,
# 0.05 qn = 30 ms after the joined G4's note-off (the VoiceTimer 30 ms edge that silenced the c37 bar-160 repeat). The
# new silent-note check in tools/measure.py found one more on c39: Oboe 1's E-flat5 at 496 (bar 124, mf, Leg Slur
# MAX), 30 ms after the slurred F5's note-off (c36-c39 identical, -51..-68 dB). Both previous notes end about 0.10 s
# before the moved onset (the gap with which Clarinet 1's bar-160 repeat sounded in c38)
NOTE_END_AT = dict(NOTE_END_AT, **{"Clarinet 1": {653.5: 653.78}, "Oboe 1": {495.5: 495.68}})
# critic A #3 (a), a test: bar 135, the celli's accented mf C3 stroke at 536 spoke 0.8-1.0 s late after the ff G3 on Leg
# BC (12-15 dB under the identical 542 stroke for 0.4 s): a bow lift, the G3 ending about 0.1 s before the C3's moved
# onset, so the KS Master does not treat the C3 as connected. 548 (accented f chord after the 545 stroke) lost its entry
# lead in c39: +0.12 s (build/entry_leads.json; tools: a listed onset takes the Leg/Sus -> Sus entry path at f too)
NOTE_END_AT = dict(NOTE_END_AT, Violoncellos={**NOTE_END_AT["Violoncellos"], 534.0: 535.55})
# critic A #4: transition spikes on exposed unaccented slur joins (30 ms burst 5.0-8.7 dB over the louder body; spikes
# repeat to 0.1 dB between renders since c38): notches of -(burst - 2) dB over A's spans, each simulated on the c39 stem
# (bursts -> 2.0-3.2 dB, dips 0.9-3.4 dB except Horn 2 249, whose 5.6 dB dip is the join's own). critic A #2: with the
# crescendo fronts now from the score onset on led legato targets (tools CRESC_FRONT_LEG_SCORE), the sample spikes of
# Violoncellos 4 (+4.5 dB) and Horn 1 589 (+5.0) show: notched the same way (simulated: +2.0 each)
for t_, rows_ in {"Flute 1": [(394.90, 395.24, -6.4)], "Horn 1": [(593.11, 593.33, -6.7), (588.81, 589.0, -3.0)],
                  "Violas": [(610.58, 610.90, -5.6), (593.74, 593.97, -3.8)],
                  "Violins I": [(266.74, 266.90, -5.4), (67.80, 68.06, -3.0)], "Bassoon 1": [(518.88, 519.24, -4.1)],
                  "Trombone 1": [(699.96, 700.14, -4.6)], "Horn 2": [(248.97, 249.18, -4.6)],
                  "Violins II": [(241.55, 241.94, -3.8)], "Violoncellos": [(3.83, 3.91, -2.5)]}.items():
    JOIN_NOTCH = dict(JOIN_NOTCH, **{t_: JOIN_NOTCH.get(t_, []) + rows_})
# critic C #1: the two fff downbeats did not arrive (master +0.2 dB into bar 160, +1.7 into bar 122: the crescendos reach
# the fff level a beat early). Hold the last beat of each crescendo back and give bar 160 a short arrival lift (simulated
# on the c39 master: mp3 step +0.1 -> +3.0 dB into 160, +1.9 -> +3.2 into 122; 160 over 122 0.80 -> 0.97 LU; span 19.2)
LEVEL_SHAPES["_all"] = LEVEL_SHAPES.get("_all", []) + [
    [(634.0, 0.0), (635.0, -1.5), (635.9, -2.5), (636.0, 0.0)],
    [(635.98, 0.0), (636.02, 1.5), (636.4, 1.5), (637.0, 0.0)],
    [(482.0, 0.0), (483.0, -1.0), (483.95, -2.0), (484.05, 0.0)]]

# coda "Solo espr." (coordinator #2; critics A #1, C #2, C #3): Hollywood Solo Cello is licensed but not installed. The
# section rests over the solo (679.5-696; its 696 tutti G2 becomes an ordinary entry) and the solo is played in the
# second render pass by two alias tracks of Violoncellos, an A/B judged on the render (holes, bursts, image correlation,
# level against the cor anglais); the losing one leaves the sum:
# - "Cello solo": the c35 track (Celli KS Master DIV A, Close only; mix.json mics written, send 0.5, width 0.2), fitted
#   fresh: none of the section's per-note fits (fills, fronts, legato leads, trims, roles, shapes, notches, pitch trims,
#   per-row lead extras; the 680 entry keeps its extra entry lead), legato leads 0.12 s (kit section 5: a DIV A solo legatos faster than its section), legato targets at
#   velocity 70 (MANUAL-GAPS #8: a slower audible transition at q = 72; tools LEG_VEL_SPANS). The 685 portamento
#   (PORT_TARGETS, v100) and the rules (hairpins, espr., the phrase's lead span and its apex hold) stay
# - "Cello solo sec": the section patch over the same window with every section table, plus C #2's level shape at the
#   685 join (6 dB instead of 9: with the crescendo front now from the score onset, 9 dB simulated a +5.1 dB burst; 6
#   dB: dip 11.2 -> 1.7, burst +2.3, C's deepest 20 ms frame -1.2 dB re the C3) and A #1 (c) at 689.5 (the c28 step
#   moved after the sample's transition, 689.26-689.34, and a -2 dB notch: burst +9.5 -> +3.5, dip 5.1 unchanged)
_VSW = [(679.5, 696.0)]
TRACK_WINDOWS = {**TRACK_WINDOWS, "Violoncellos": (_VSW, False)}
assert [(689.18, 0.0), (689.26, 5.0), (690.22, 5.0), (690.34, 0.0)] in LEVEL_SHAPES["Violoncellos"]
LEVEL_SHAPES["Violoncellos"] = [s_ if s_ != [(689.18, 0.0), (689.26, 5.0), (690.22, 5.0), (690.34, 0.0)]
                                else [(689.26, 0.0), (689.34, 5.0), (690.22, 5.0), (690.34, 0.0)]
                                for s_ in LEVEL_SHAPES["Violoncellos"]] + [
    [(684.72, 0.0), (684.78, 6.0), (684.90, 6.0), (684.98, 2.67), (685.06, 0.0)]]
JOIN_NOTCH = dict(JOIN_NOTCH, Violoncellos=JOIN_NOTCH["Violoncellos"] + [(689.22, 689.39, -2.0)])
_SECTION_FITS = ("EARLY_FILLS", "CRESC_FRONTS", "LEG_LEADS", "NOTE_TRIMS", "NOTE_TRIM_RAMP_S", "ROLES",
                 "LEVEL_SHAPES", "LEVEL_SHAPES_S", "JOIN_NOTCH", "ACCENT_FITS", "ACCENT_BODIES", "LOOP_FILLS")
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{
    "Cello solo": {"source": "Violoncellos", "windows": _VSW, "no_pitch_trims": True,
                   "patch": S + "Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib",
                   "drop": {t_: None for t_ in _SECTION_FITS},
                   "set": {"LEG_LEAD_S": 0.12, "LEG_ART_EXTRA_S": {}, "LEG_VEL_SPANS": [(679.5, 696.0, 70)]}},
    "Cello solo sec": {"source": "Violoncellos", "windows": _VSW}})
PASS2_TRACKS = tuple(PASS2_TRACKS) + ("Cello solo", "Cello solo sec")
# the section variant, as c39 played it: on the main track the bar-170 crescendo's gain was released over the solo's first
# phrase (+3.0 dB at 679.5 to +0.3 at 684.7); an alias has no notes before the window, so HP_GAIN_IN_WINDOW drops that
# hairpin (skipping the filter instead held its full +9 dB): the release, as an alias-only shape
ALIAS_TRACKS["Cello solo sec"]["tables"] = {"LEVEL_SHAPES": [[(679.4, 0.0), (679.45, 3.0), (680.2, 2.92), (681.0, 2.43),
                                                              (682.0, 1.86), (683.0, 1.29), (684.2, 0.85), (684.7, 0.33),
                                                              (684.75, 0.0)]]}

# critic B #2: the c39 brass lift (+2 brass / +1 horns over bars 26-32, 69-72, 131-143) covered the ff theme where the
# brass are printed f (theme minus accompanying brass -0.9..-3.9 dB in bars 29-31, 70-71, 131-134 descant): build/
# roles.json keeps it only at the tutti chords where the brass share the theme's dynamic (bars 26, 32, 72, 143), plus
# +1 on Horns 1-2 (printed ff) over bars 26-30. critic B #3: Trumpet 2 over Trumpet 1 in bars 27-31 / 69-72 (the c39 f
# trim plus the lift): roles [103.5, 124.5, -2] added, [272, 288] -3 -> -5
# critic B #4 (second pass): the fugato's flute staccatos 10.8-17.3 dB under the Violins I they double (Flute 1 stac
# copied Flute 1's f trim -4, fitted on the Sus / legato rows): mix.json f trim -4 -> -1 and lifts over its three
# staccato groups; Bassoon 1 stac's first notes hot and last quarters fading (-10.5..+8.1 dB re the violas): steps
ALIAS_TRACKS["Flute 1 stac"]["tables"] = {"LEVEL_SHAPES": [[(374.3, 0.0), (374.4, 5.0), (375.9, 5.0), (375.95, 0.0)],
                                                           [(379.3, 0.0), (379.4, 5.0), (379.85, 5.0), (379.9, 0.0)],
                                                           [(382.3, 0.0), (382.4, 5.0), (383.9, 5.0), (383.95, 0.0)]]}
_bst = lambda x_: [(-0.05, 0.0), (0.0, x_), (0.25, x_), (0.3, 0.0)]
ALIAS_TRACKS["Bassoon 1 stac"]["tables"]["LEVEL_SHAPES_S"] = ALIAS_TRACKS["Bassoon 1 stac"]["tables"]["LEVEL_SHAPES_S"] + [
    (357.0, _bst(2.5)), (358.0, _bst(7.0)), (359.0, _bst(4.0)), (348.5, _bst(-3.0)), (353.0, _bst(-5.0))]
# critic C #3: delivery ride trims over the cello solo (RIDE_TRIMS, tools/deliver_master.py), fitted on the c40 master
RIDE_TRIMS = []

# ---------- c40 stem fix (level only, measured on the c40 render) ----------
# Movement II thread (via the coordinator): in the 1FH / 2FH KS Masters the "TLeg" transition groups sit at 0.78-0.91 of
# full volume at CC1 28-46 (0.44 at 70) while the soft sustain layers are far quieter (1FH pp 0.47 / mf 0.56 at CC1
# 34; read from the patch), so soft legato horn targets start over their sustain. Measured on the c39 horn stems: of 35
# legato targets at CC1 42-54, 8 put a 30 ms burst 4.0-5.7 dB over the louder body (0 of 30 at CC1 57 or more; head
# minus the note's own sustain median +3.8 against +3.5 dB). Notches of -(burst - 2) dB over each burst's span (as A #4),
# simulated on the c39 stems (bursts -> 2.0-2.6 dB); Horn 1 589 is notched above. Raising the horns' soft CC1 floor to 57
# (Movement II's choice) changes the layer of every soft horn note and needs its own render and refits: open
JOIN_NOTCH = dict(JOIN_NOTCH, **{
    "Horn 4": JOIN_NOTCH.get("Horn 4", []) + [(419.88, 420.26, -3.7), (414.99, 415.20, -3.4), (417.90, 418.16, -2.6)],
    "Horn 3": JOIN_NOTCH.get("Horn 3", []) + [(654.04, 654.22, -3.5), (419.88, 420.17, -2.8)],
    "Horn 1": JOIN_NOTCH["Horn 1"] + [(189.01, 189.28, -3.1)],
    "Horn 2": JOIN_NOTCH["Horn 2"] + [(223.91, 224.17, -2.2)]})
# coordinator #4 (Violins I string positions): with its CC70 lane starting at 127 (SUL_FP4_CC70) Violins I still rendered
# as c38's lane-20 render outside the sul window (median +0.65 / +0.71 dB, p90 +2.2 over 2-qn frames against c39's FP4
# splice; Violins II and the celli matched to 0.00), and was spliced again (cycles/c40/actor_scripts/fpsplice40.py).
# Read in the saved project: Opus stores each sample group's start-mode controller value ("default") in the plugin
# state, and Violins I's string-position sustain groups have held 120 since the c38 session while every other value
# moved (Violins II's moved 20 -> 127); a --midi-only build keeps that saved state. A test in the second pass: "Violins I
# test", a fresh instance of the same patch from the generated state (all values 127, as in c37), playing Violins I's
# own notes and lanes over 38.5-168.5; it is not summed into the master
ALIAS_TRACKS["Violins I test"] = {"source": "Violins I", "windows": [(38.5, 168.5)]}
PASS2_TRACKS = tuple(PASS2_TRACKS) + ("Violins I test",)
# critic A #3, measured on c40: (a) the bow lift did not make 536 speak (C3 harmonics 1/2/4/5 at +0.1 s 10.4 dB against
# 26.2 for the 542 stroke; c39 14.7, c38's Leg BC version 33.3; body only by +0.8 s): the Leg BC -> Sus MAX path blooms
# with a 0.1 s gap too. A's fallback (b), 536 back on Leg BC with 539-545 kept as strokes, would put 539 on the same
# Leg -> Sus path: not made; open (the 534 end stays as rendered). 548: the listed extra lead (0.12 s) took the chord
# from pc +0.248 to -0.119 s (the stroke-entry path also changed its velocity and the old note's end): 0.01 for the next
# render (build/entry_leads.json; the c40 render carries 0.12)
# coda solo A/B, first pass-2 render (cycles/c40/solo_a.txt): DIV A had no join hole (max dip 2.6 dB against 6.4 on the
# section patch and 11.2 in c39) and a narrower image (L/R correlation 0.85, 1-4 kHz 0.90; section 0.74 / 0.81; cor
# anglais 0.84), but late targets at its 0.12 s leads (pc 685 +0.237 s on the portamento, 680 +0.149, 691 +0.160, 689.5
# +0.103; early 690 -0.143, 694 -0.204) and an uneven contour (the 685 portamento target blooms 13 dB over the line).
# Leads refitted per onset (about 0.8 x pc) for a second pass-2 render; the level contour is fitted on that render
ALIAS_TRACKS["Cello solo"]["tables"] = {
    "LEG_LEADS": {"684.0": -0.07, "685.0": 0.15, "687.0": 0.035, "688.0": -0.055, "689.5": 0.08, "690.0": -0.11,
                  "691.0": 0.13, "694.0": -0.09},
    "ENTRY_LEADS": {"680.0": 0.24}}
# coda solo A/B, second pass-2 render (cycles/c40/solo_b.txt): with the refitted leads the DIV A targets perceive within
# -0.04..+0.09 s (the 685 portamento's arrival +0.28 s: the glide itself); max join dip 4.8 dB (section patch 6.4, three
# of 4 dB or more), image correlation 0.85 / 0.90 at 1-4 kHz (section 0.74 / 0.81). DIV A kept (critics' measures: holes
# and image better; bursts and level fitted below). Its level contour (the 685 portamento target blooms 10 dB over the
# line, the phrase top 692 under it): per note, the section variant's level minus DIV A's (power smoothed over 0.3 s, so
# no join dip or burst of the section is copied), sampled inside each note and crossfaded across each transition from
# the target's moved onset to its score onset + 0.05 qn; then fills / notches at the joins whose dip passed 3.5 dB or
# burst 3 dB on the simulated stem (cycles/c40/actor_scripts/contour40.py). Applied by stem fix on the second pass-2
# render: per 2 qn within 1.2 dB of the section variant, solo minus cor anglais median 5.3 dB (section 5.3), join dips
# 0.3-3.3 dB, bursts -1.5..+2.8 dB except 687 (+4.7)
_DIVA_CONTOUR = [
    (679.85, 0), (680.05, 4.7), (680.1, 4.7), (680.225, 3.8), (680.35, 1), (680.475, -0.9), (680.6, -3.7),
    (680.725, -4), (680.85, -3.5), (680.975, -3.7), (681.1, -4.2), (681.225, -5.6), (681.35, -5.6), (681.475, -5.2),
    (681.6, -4.6), (681.725, -5), (681.85, -5.3), (681.975, -4.5), (682.1, -3.6), (682.225, -3.1), (682.35, -3.7),
    (682.475, -3.3), (682.6, -3.3), (682.725, -2.1), (682.85, -1.9), (682.975, -1.7), (683.1, -3.5), (683.225, -4.8),
    (683.35, -5.8), (683.354, -5.8), (683.55, -3.5), (683.6, -3.5), (683.725, -1.6), (683.85, -0.2), (683.939, -0.2),
    (684.05, 0.1), (684.1, 0.1), (684.225, -0.1), (684.35, 3.1), (684.475, 4.3), (684.6, 5.1), (684.725, 5.3),
    (684.85, 5.5), (685.05, 0.1), (685.1, 0.1), (685.225, -4.1), (685.35, -6.7), (685.475, -8), (685.6, -9.3),
    (685.725, -11.6), (685.85, -12), (685.975, -12), (686.1, -11.5), (686.225, -10), (686.35, -9.3),
    (686.475, -10.2), (686.6, -9.4), (686.725, -9.9), (686.85, -9.6), (687.05, -5.5), (687.1, -5.5), (687.225, 0.7),
    (687.35, 3.3), (687.475, 3.6), (687.6, 3.3), (687.725, 2.5), (687.85, 1.1), (687.921, 1.1), (688.05, 0.1),
    (688.1, 0.1), (688.225, 2), (688.35, 3.3), (688.475, 3.1), (688.6, 2), (688.725, 2.7), (688.85, 3.1),
    (688.975, 2.8), (689.1, 1.2), (689.225, 0.7), (689.35, 0.1), (689.55, 5.9), (689.6, 5.9), (689.725, 5.6),
    (689.85, 5), (689.964, 5), (690.05, 4.9), (690.1, 4.9), (690.225, 5.4), (690.35, 6.7), (690.475, 7.3),
    (690.6, 7), (690.725, 7), (690.85, 6.3), (691.05, 6.8), (691.1, 6.8), (691.225, 6.7), (691.35, 5.7),
    (691.356, 5.7), (691.55, 2.1), (691.6, 2.1), (691.725, 2.7), (691.85, 5.3), (691.856, 5.3), (692.05, 8.2),
    (692.1, 8.2), (692.225, 9.1), (692.35, 10), (692.475, 9.6), (692.6, 7.9), (692.725, 6), (692.85, 5.5),
    (692.975, 4.7), (693.1, 3.7), (693.225, 2.5), (693.35, 2.1), (693.475, 1.5), (693.6, 0.9), (693.725, 0.5),
    (693.85, 0), (693.964, 0), (694.05, 1.1), (694.1, 1.1), (694.225, 2.7), (694.35, 3.4), (694.475, 2.8),
    (694.6, 1.6), (694.725, -0.6), (694.85, -1.8), (694.975, -1.1), (695.1, 0.3), (695.225, -0.3), (695.35, -2.3),
    (695.475, -3.3), (695.6, -3.2), (695.725, -1.9), (695.85, -2.9), (695.95, -2.9), (696.05, 0)]
_DIVA_JOINS = [
    [(683.518, 0), (683.567, 1.8), (683.664, 1.8), (683.713, 0)],
    [(684.006, 0), (684.055, -1.1), (684.152, -1.1), (684.201, 0)],
    [(684.872, 0), (684.921, 1.7), (685.018, 1.7), (685.067, 0)],
    [(686.998, 0), (687.046, 4.3), (687.144, 4.3), (687.192, 0)],
    [(687.939, 0), (687.988, 2.4), (688.084, 2.4), (688.132, 0)],
    [(689.999, 0), (690.047, -1.4), (690.143, -1.4), (690.191, 0)],
    [(690.977, 0), (691.025, 2.1), (691.121, 2.1), (691.169, 0)],
    [(684.575, 0), (684.624, -1.9), (684.721, -1.9), (684.77, 0)],
    [(686.888, 0), (686.937, -3.4), (687.034, -3.4), (687.083, 0)],
    [(686.839, 0), (686.888, 2.9), (686.985, 2.9), (687.034, 0)]]
ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] = [_DIVA_CONTOUR] + _DIVA_JOINS
# the A/B is decided (DIV A): "Cello solo sec" leaves the second pass and the sum (its c40 stem in cycles/c40/test_stems/);
# the "Violins I test" instance did its job (fresh state = FP4 audio; cycles/c40/CHANGES.md) and leaves too. Both tracks
# were deleted from the pass-2 project after the c40 render (cycles/c40/del_tracks.lua)
for _t in ("Cello solo sec", "Violins I test"):
    ALIAS_TRACKS.pop(_t)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in ("Cello solo sec", "Violins I test"))
# the celli's tutti pp G2 at 696 is now an ordinary entry after a rest (the solo is on its own track), but it kept the
# hand-over lifts fitted for the c35-c39 legato join (early fill +3.5, a body -5 step from +0.15 qn, the -6 note trim
# ramped over 0.72 qn, the solo's +1.5 role): the envelope opened 14 dB over the note's body and the stem's front sat
# 5-9 dB over its body at 0-0.5 s (c39: -6..+0.6). A counter-shape holds the envelope at the body level from the moved
# onset (stem fix)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[
    (695.6, 0.0), (695.65, -11.34), (695.7, -12.59), (695.75, -14.41), (695.8, -13.78), (695.85, -13.15), (695.9, -12.88),
    (695.95, -12.97), (696.0, -13.06), (696.1, -13.06), (696.15, -10.85), (696.2, -7.75), (696.25, -6.64), (696.35, -6.64),
    (696.4, -5.43), (696.45, -3.02), (696.5, -1.36), (696.6, -1.36), (696.65, -1.04), (696.7, -0.4), (696.75, 0.0)]]
# critic C #3 (tools RIDE_TRIMS in deliver_master.py): the delivery ride rose 4.5 -> 9.5 dB across the cello solo (an
# unprinted crescendo of about 5 dB in the mp3, flat in the master). Fitted on the final c40 master with
# `deliver_master.py ... --fit-flat 680 695.9` (the ride held at the solo's own steady lift, 8.1 dB). Refit when the mix
# around bars 170-175 changes
RIDE_TRIMS = [[(679.95, 0.0), (680.0, 3.67), (682.0, 2.91), (684.0, 2.12), (686.0, 1.33), (688.0, 0.6), (690.0, -0.07),
               (692.0, -0.62), (694.0, -1.06), (695.8, -1.37), (695.9, 0.0)]]

# ---------- c41 (series 2, end of the first block): critics on the c40 render ----------
# critic A #1: the next tier of transition spikes on exposed unaccented legato joins (30 ms burst 4.5-8.8 dB over the
# louder body, rel -10 dB or more; spikes repeat to 0.1 dB between renders since c38): notches of -(burst - 2) dB over
# A's spans, each simulated on the c40 stem (bursts -> 2.0-4.0 dB, master bursts +8.5 / +8.2 / +6.7 -> +3.9 / +5.5 /
# +4.9 on Bassoon 1 131, celli 575, celli 191; early pc on celli 575 / 191 and violas 182 / 613 -0.15..-0.30 s ->
# -0.08..+0.02 s, the spike no longer speaking before the beat)
for t_, rows_ in {"Bassoon 1": [(130.75, 131.18, -6.2), (137.72, 138.34, -3.9)],
                  "Violoncellos": [(574.58, 575.02, -5.0), (190.55, 190.72, -4.0)],
                  "Clarinet 1": [(506.80, 507.13, -2.5)],
                  "Violas": [(435.59, 435.97, -5.0), (181.34, 181.77, -2.7), (27.80, 28.13, -5.7), (612.68, 613.17, -6.8)],
                  "Oboe 1": [(315.45, 315.58, -2.6)], "Horns a2": [(164.05, 164.34, -2.8)],
                  "Violins II": [(258.50, 258.87, -4.1)]}.items():
    JOIN_NOTCH = dict(JOIN_NOTCH, **{t_: JOIN_NOTCH.get(t_, []) + rows_})
# critic A #2: printed breaths played through (stem dips 1.6 / 1.8 / -0.5 dB): Horns a2 into the bar-160 fff (no row:
# Horn 1's table holds no 634, so the a2 copy above had none; Trombone 1's values), Trombone 2 at bar 159 (the default
# 0.3 qn gap is kept, but the default branch has no fall for trombones; v621's breath is at 632), Horn 4 at bar 134
# (Horn 3's values; Horn 3 dips 3.8 dB there). Oboe 2 / Flute 2 into 636: the 0.12 qn gap (the caesura's
# CAESURA_BREATH_QN) is eaten by the 636 entry lead (22 ms played): 0.22 qn as Trombone 1 (5.6 dB dip)
BREATH_GAP_AT["Horns a2"] = {**BREATH_GAP_AT.get("Horns a2", {}), 634.0: 0.22}
BREATH_FALL_CC["Horns a2"] = {**BREATH_FALL_CC.get("Horns a2", {}), 634.0: 10}
BREATH_GAP_AT["Trombone 2"] = {**BREATH_GAP_AT.get("Trombone 2", {}), 628.0: 0.3}
BREATH_FALL_CC["Trombone 2"] = {**BREATH_FALL_CC.get("Trombone 2", {}), 628.0: 10}
BREATH_GAP_AT["Horn 4"] = {**BREATH_GAP_AT.get("Horn 4", {}), 532.0: 0.4}
BREATH_FALL_CC["Horn 4"] = {**BREATH_FALL_CC.get("Horn 4", {}), 532.0: 8}
BREATH_GAP_AT["Oboe 2"] = {**BREATH_GAP_AT["Oboe 2"], 634.0: 0.22}
BREATH_GAP_AT["Flute 2"] = {**BREATH_GAP_AT.get("Flute 2", {}), 634.0: 0.22}
BREATH_FALL_CC["Flute 2"] = {**BREATH_FALL_CC.get("Flute 2", {}), 634.0: 8}
# critic A #3: the coda solo's 685 portamento arrives on the beat in the delivered stem (f0 within 15 cents at -0.03 s),
# but the alias contour falls 11 dB between -0.15 and +0.26 s while the Leg Port sample crossfades into its sustain at
# +0.30 s: a 7 dB swing in 0.1 s just after the shift (-3.8 dB at +0.25, +3.1 at +0.35 re the note body). Simulated on
# the c40 stem: range over 0..0.6 s -4.4..+3.2 -> -3.6..+1.2 dB, master -3.3..+2.1 -> -3.4..+0.4
ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES_S"] = [
    (685.0, [(0.10, 0.0), (0.14, 3.0), (0.25, 3.0), (0.30, -2.0), (0.45, -2.0), (0.55, 0.0)])]
# critic A #4 not made: its premise does not hold. A read GENTLE_ACCENT["string"]["swell_s"] (0.07, 0.25, 0.6) in the
# score_to_parts.py defaults; the c23 entry above already sets strings (and winds) to (0.03, 0.15, 0.40), the brass
# value A proposed (checked in the module namespace after this file runs)
# critic A #5 (S1): five exposed brass repeats (onset gap 0.13-0.22 qn) dipped -1.3..2.8 dB: the repeats on the
# "LegRep RRx4" row (1FH key 34, 1TP key 35), with REP_ROW_REPEATS_ONLY brass and REP_ROW_GAP_S (0.06, 0.15) as Horn 4's
# pedals (3.2 -> 7.2 dB in c38). One more loaded row on each of the two main-project tracks
REP_ROW = dict(REP_ROW, **{"Horn 1": REP_ROW.get("Horn 1", []) + [(451.9, 452.1, "LegRep RRx4"), (527.9, 528.1, "LegRep RRx4"),
                                                                 (623.9, 624.1, "LegRep RRx4")],
                           "Trumpet 2": REP_ROW.get("Trumpet 2", []) + [(123.9, 124.1, "LegRep RRx4"),
                                                                       (455.9, 456.1, "LegRep RRx4")]})
# critic B #2: bar 125, Horn 1's mp espr. C4 (498-501) covered by the Violins I / Oboe 1 C5, which swells +6.3 dB inside
# its printed mf > p (Horn 1 minus Violins I A -0.8 / +0.6 / -4.1 / -1.4 at 498.0-499.5): the violins' swell held down
# (back to 0 before the 499.63 transition), Oboe 1 after its join fill's hold, Horn 1's sagging C4 held up into its own > p
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES.get("Violins I", []) + [[(498.25, 0.0), (498.75, -3.0), (499.0, -5.0), (499.5, -5.0), (499.6, 0.0)]]
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES.get("Oboe 1", []) + [[(498.6, 0.0), (499.0, -3.0), (499.8, -3.0), (499.9, 0.0)]]
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES.get("Horn 1", []) + [[(498.9, 0.0), (499.25, 3.0), (500.0, 3.0), (500.75, 0.0)]]
# critic B #3: the c40 hold-back rows worked against the older ramps, so the crescendos into both fff downbeats stalled
# on their last beat and then jumped (master K per beat into 636 +0.8 / +0.6 / +3.6, into 484 -0.7 / +3.0). One row each:
# simulated steps into 636 +1.0 / +1.2 / +1.5 then +2.9; into 484 +0.7 / +0.7 / -0.1 then +3.0. The 636 arrival lift stays
_b158_old = [(627.875, 0.0), (628.375, -2.0), (632.0, -2.0), (635.375, 0.0)]
_hb160_old = [(634.0, 0.0), (635.0, -1.5), (635.9, -2.5), (636.0, 0.0)]
_p121_old = [(467.0, 0.0), (468.5, 0.8), (482.0, 0.8), (483.5, 0.0)]
_hb122_old = [(482.0, 0.0), (483.0, -1.0), (483.95, -2.0), (484.05, 0.0)]
assert all(r_ in LEVEL_SHAPES["_all"] for r_ in (_b158_old, _hb160_old, _p121_old, _hb122_old))
LEVEL_SHAPES["_all"] = [r_ for r_ in LEVEL_SHAPES["_all"] if r_ not in (_b158_old, _hb160_old, _p121_old, _hb122_old)] + [
    [(627.875, 0.0), (628.375, -2.0), (632.0, -2.0), (635.9, -1.2), (636.0, 0.0)],
    [(467.0, 0.0), (468.5, 0.8), (481.0, 0.8), (483.95, -1.8), (484.05, 0.0)]]
# critic B #5 (second pass): fugato entry 2, the cor anglais doubling of Violins II spread 13.8 dB per note (its long
# G-sharp4 at 361 swells 33-35 dB A against a flat violin line; the staccato eighths after it fall 8-15 dB under it):
# the long note's swell cut, the Sus / legato quarters at 365-366 down, the staccatos at 363.5 and 367.5 up
ALIAS_TRACKS["Cor anglais stac"]["tables"]["LEVEL_SHAPES"] = ALIAS_TRACKS["Cor anglais stac"]["tables"]["LEVEL_SHAPES"] + [
    [(361.3, 0.0), (361.8, -3.0), (362.3, -5.0), (362.4, 0.0)],
    [(364.85, 0.0), (364.95, -4.0), (365.88, -4.0), (365.95, 0.0)]]
ALIAS_TRACKS["Cor anglais stac"]["tables"]["LEVEL_SHAPES_S"] = [
    (363.5, [(-0.05, 0.0), (0.0, 4.0), (0.2, 4.0), (0.25, 0.0)]), (367.5, [(-0.05, 0.0), (0.0, 4.0), (0.25, 4.0), (0.3, 0.0)])]
# critic C #1 (S2), an A/B in the second pass that is not summed (tools TEST_TRACKS, build_reaper mix key
# "legato_speed"): the Hollywood Strings LegatoSpeed script maps velocity to a start offset into each legato transition
# sample up to START_MAX (patch: 1st Violins 4800, Violas 2173, Celli 2709; BUMPRED 4760 / 3890 / 3130; RELEASE 450 /
# 510 / 443 ms), so at v124 the violas and celli skip 44-55 ms of the recorded slide against the violins' 97 ms; C
# measured their both-pitches-within-6-dB windows at 174-236 ms median against 112-126 for the violins. Four fresh
# instances play the Violas' and Violoncellos' own notes, lanes and leads (no "drop"; the celli rest over the coda solo
# as on the main track): A = START_MAX at BUMPRED, B = START_MAX 4800 with RELEASE 300 ms (mix.json). Measured against
# the main render's stems on the same notes; adopted on the main tracks only if C's criteria pass
_LST = {"Vla test A": ("Violas", [(0.0, 730.0)]), "Vla test B": ("Violas", [(0.0, 730.0)]),
        "Vc test A": ("Violoncellos", [(0.0, 679.5), (696.0, 730.0)]),
        "Vc test B": ("Violoncellos", [(0.0, 679.5), (696.0, 730.0)])}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": w_} for n_, (s_, w_) in _LST.items()})
PASS2_TRACKS = tuple(PASS2_TRACKS) + tuple(_LST)
TEST_TRACKS = tuple(_LST)

# ---------- c41 stem fix (level only, measured on the c41 render) ----------
# critic A #1 follow-up: three of the new notches were placed off their spikes on this render: Bassoon 1 131 and Violas
# 613 cut the old note's tail before the spike (new dips 4.9 / 5.4 dB, bursts +1.3 / +3.4), Violas 613 also the new
# note's first 0.1 qn; celli 191 kept a +3.5 dB burst. Spans moved onto the spikes (frames 130.89-131.14 / 612.74-613.02, where this render's raw spike peaks 10 dB over the new note; -8 dB moved the perceived attack to +0.2 s),
# celli 191 -4 -> -5.5
_jn41 = {"Bassoon 1": ((130.75, 131.18, -6.2), (130.87, 131.18, -6.2)), "Violas": ((612.68, 613.17, -6.8), (612.75, 613.0, -6.8)),
         "Violoncellos": ((190.55, 190.72, -4.0), (190.55, 190.72, -5.5))}
for t_, (o_, n_) in _jn41.items():
    assert o_ in JOIN_NOTCH[t_]
    JOIN_NOTCH[t_] = [n_ if r_ == o_ else r_ for r_ in JOIN_NOTCH[t_]]
# critic A #2 follow-up: Trombone 2's breath at 632 still dipped 2.4 dB with the CC11 fall (the G3 repeat's 150 ms gap
# filled by the release and hall): the horn / trombone gap dip of c38 (-6 dB over the gap)
LEVEL_SHAPES_S["Trombone 2"] = LEVEL_SHAPES_S.get("Trombone 2", []) + [(632.0, _gd18)]
# critic A #5 follow-up: on the LegRep RRx4 row the brass repeats came in 2-5 dB louder than the Sus repeats of c40 over
# their first 0.5 s (Horn 1 452 +2.4..+3.3, Trumpet 2 456 +0.9..+2.4, 124 +4..+6 dB); the gap minimum is unchanged, so
# the separation is the stronger re-attack (re-attack over the gap: Horn 1 452 4-5 -> 8-10 dB, Trumpet 2 456 3-5 -> 5-6;
# 2-5 kHz front minus body Horn 1 452 / 624 -11.5 / -15.5 -> -8.6 / -9.2). The body excess past the first 0.1 s trimmed;
# Trumpet 2's accented ff 124 (dip 1.0 -> -0.4, +4..+6 dB over its c40 level, a 2-6 dB unprinted lift under Trumpet 1)
# goes back to Sus: row removed, its c40 audio spliced back (cycles/c41/actor_scripts/splice41.py)
LEVEL_SHAPES_S["Horn 1"] = LEVEL_SHAPES_S.get("Horn 1", []) + [(452.0, [(0.08, 0.0), (0.14, -2.0), (0.5, -2.0), (0.6, 0.0)])]
LEVEL_SHAPES_S["Trumpet 2"] = LEVEL_SHAPES_S.get("Trumpet 2", []) + [(456.0, [(0.03, 0.0), (0.08, -1.5), (0.35, -1.5), (0.45, 0.0)])]
REP_ROW["Trumpet 2"] = [r_ for r_ in REP_ROW["Trumpet 2"] if r_ != (123.9, 124.1, "LegRep RRx4")]
# critic C #1 result (cycles/c41/CHANGES.md; legtest.py on the four test stems in cycles/c41/test_stems/): START_MAX moved
# each transition earlier as a whole (crossover median -20 / -34 ms violas A / B, -2 / -9 ms celli A / B) without
# shortening the slide (both-pitches-within-6-dB window per join median +0 ms in all four; violas 94-98 / p75 134 ms,
# celli 108-110 / 148 against the violins' 86-101 / 112-120 with the same method) and added joins with dips of 5 dB or
# more (violas 9 -> 13 / 18, celli 24 -> 24 / 33). Not adopted; the test tracks leave parts.json and the pass-2 project
for _t in _LST:
    ALIAS_TRACKS.pop(_t)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _LST)
TEST_TRACKS = ()

# ---------- c42 (series 2): critics on the c41 render ----------
# critic B #2: bar 10 (Lento), Violins I's held mp espr. E-flat5 (35.87-39.02) stays flat in absolute level while the
# pp section crescendos under it and the celli's automatic re-bow at 37.377 (Sus MAX) blooms 3-4 dB over the legato
# note before it; the master dipped 1.4 dB at qn 39 inside the printed four-bar crescendo. Violins I lifted into its
# bow-change join (back to 0 across the 38.854 transition), the celli held down (back to 0 before the 39.879 re-bow and
# the printed bow change at 40)
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(36.3, 0.0), (37.6, 2.0), (38.6, 4.0), (38.95, 4.0), (39.45, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(35.9, 0.0), (36.3, -2.5), (38.1, -2.5), (38.35, -4.0),
                                                               (38.9, -4.0), (39.3, -1.5), (39.9, 0.0)]]
# critic B #3: Horn 4's stale c22 fill at 453 (no hole: stem minus envelope -0.8..-1.5 dB after the onset) made the
# inner F3 the loudest horn and level with the Violins I tune; its note trim -2 (stepped like the other C3-F3 notes).
# Bassoon 1's c02 fill at 364 (no hole) removed in early_fills.json
NOTE_TRIM_RAMP_S["Horn 4"] = {**NOTE_TRIM_RAMP_S.get("Horn 4", {}), 453.0: 0.1}
# critic C #2: the cor anglais' bar-7 espr. swell (24-26 <, 26-28 >) grew only 1.6 dB: its soft trim tapers from p
# (+5) toward mf as CC11 rises and a 1.4 dB vol_db dip at 24.75-25.0 cancel the +3 dB hairpin gain
# (C's row, 24.1 -> 25.9 +2.5, simulated on the c41 stems: swell +1.1 -> +3.2 dB, peak 1.4 dB over the bar-6 peak; the
# crescendo's first half beat 1 dB lower gives the 4 dB growth without raising the peak)
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [[(24.15, 0.0), (24.35, -1.0), (24.6, -1.0), (25.9, 2.5),
                                                                       (26.25, 2.5), (27.75, 0.0)]]
# critic C (manual notes p.63-64): the c36 CC7 test lane on Trombone 1 (679.32-679.97, rests there) did nothing and is
# removed; no track sends CC7 except the timpani's own per-stroke lane
CC7_POINTS = {}
# critic A #1 (S2, the coordinator's first item): the c41 C "viola / cello slides of 174-236 ms" were the m37 estimator's
# shared bins (verified: on a synthetic instant switch between each join's two pitches that window reads a median 15 /
# 44 ms and p75 428 / 399 ms on violas / celli; with exclusion bands, tools/pcx.py, every section's real transition is
# 82-98 ms over an 8 ms floor). Leads refitted per onset on pcX in build/leg_leads.json ("_c42"); early fills keyed to
# those onsets moved with them (pre_s + the lead change, early_fills.json "_auto"); the one join notch on a moved join
# (Violas 182, 0.09 s later at 112 bpm = 0.168 qn) moves with its spike
JOIN_NOTCH["Violas"] = [(181.508, 181.938, -2.7) if r_ == (181.34, 181.77, -2.7) else r_ for r_ in JOIN_NOTCH["Violas"]]
assert (181.508, 181.938, -2.7) in JOIN_NOTCH["Violas"]
# critic C #1 (Dan's S3, bar 62): the violins' forte (75% of the power before the sub. p) ended 0.13 s before the beat
# with a 40 ms release burst and its hall was cut by the post-hall envelope (12.8 dB of the 18 dB step, CC11 only 5.5):
# master -8.4 / -10.5 / -13.3 / -15.3 dB at 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 s after the beat against -3.3 / -4.9 /
# -8.8 / -13.2 for the fermata release at 679. The forte phrase (score onsets 219-243.5, from the bar-55 pickup after a
# rest) now plays on its own instance in the second pass, "Violins I f62" / "Violins II f62" (aliases built from the
# sources' rules and tables), so it ends at its written end and rings under the p; the main tracks rest there and start
# the p notes fresh at the post level (tools: vol_points SUBITO_TAIL holds a track that is silent at the mark; alias key
# "hold_lanes" keeps CC11 / CC1 at their last value after the alias's last note-off). Two 1st/2nd Violins KS Master
# instances in pass 2; the main project unchanged in size
_SUB62 = [(218.5, 243.9)]
TRACK_WINDOWS = {**TRACK_WINDOWS, "Violins I": (_SUB62, False), "Violins II": (_SUB62, False)}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{"Violins I f62": {"source": "Violins I", "windows": _SUB62, "hold_lanes": True},
                                     "Violins II f62": {"source": "Violins II", "windows": _SUB62, "hold_lanes": True}})
PASS2_TRACKS = tuple(PASS2_TRACKS) + ("Violins I f62", "Violins II f62")

# ---------- c42 stem fix (level only, measured on the c42 main render) ----------
# critic A #1 follow-up: three moved joins came out with new transition bursts or a hole (pass criterion: no new dips
# >= 5 dB or bursts >= 3 dB): Violas 81 (+3.7 dB over the louder body, spike 80.72-80.88) and 650.5 (+4.4, 650.11-650.20)
# notched on this render's spike frames (c41 placement rule); the celli's bar-2 join at 7.5, moved 0.05 s later, let
# the old note's decay open a 6.0 dB hole at -0.26..-0.12 s: a fill over the hole. Bursts of +3.2 dB on Violas 673 and
# celli 211.5 / 216 are left (c41 had 51 viola / 107 celli joins at 3 dB or more)
JOIN_NOTCH["Violas"] = JOIN_NOTCH["Violas"] + [(80.72, 80.88, -2.5), (650.11, 650.20, -2.5)]
# (in score qn: +4 over 7.29-7.35, back to 0 at the envelope's grid point 7.375; the c35 fill ramp at 7.31-7.39 was
# written as a linear ramp 7.375 -> 7.5 in every render, because neither of its points was a breakpoint; any new
# breakpoint there writes it 0.1 qn earlier, where it rose into the new note's onset (+2.8 dB on the first try), so the
# negative tail reproduces the rendered ramp exactly at the new breakpoints)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(7.25, 0.0), (7.29, 4.0), (7.35, 4.0), (7.375, 0.0), (7.3883, -3.4),
                                                               (7.40, -3.1), (7.425, -2.35), (7.45, -1.6), (7.475, -0.85), (7.5, 0.0)]]
# critic C #1 step 5 (burst check on the alias stems): the forte's last eighth swells 4-6 dB over its first half in the
# 0.1 s before the mark, and its release at forte puts a 30-50 ms burst 8.0 / 11.7 dB over the note's body (Violins I /
# II; c41's Violins II burst at the earlier note-off was 7-8 dB) and Violins II's C-sharp4 release then holds at -8..-10
# dB for 0.5 s: master +9.1 / +6.4 / 0.0 / -6.6 dB at 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 s after the beat (fermata
# release -3.2 / -4.8 / -8.4 / -13.0). Fitted on the c42 alias stems (cycles/c42/actor_scripts/relfit42.py): the level
# held at its own -0.35..-0.15 s value up to the note-off, then the fermata release's shape; cuts at most 12 dB, then
# one refinement step on the simulated stems (Violins II's release burst needed up to -14.9 dB over 0.02-0.1 s).
# POST_SHAPES_S (tools, c42): applied after the subito hold, which would overwrite a LEVEL_SHAPES_S row there
ALIAS_TRACKS["Violins I f62"]["tables"] = {"POST_SHAPES_S": [(244.0, [
    (-0.16, 0.0), (-0.14, -1.3), (-0.12, -3.2), (-0.1, -5.8), (-0.08, -5.2), (-0.06, -4.7), (-0.04, -2.6), (-0.02, -3.3),
    (0.0, -5.7), (0.02, -10.0), (0.04, -12.6), (0.06, -10.8), (0.08, -7.8), (0.1, -8.1), (0.12, -9.0), (0.14, -7.1),
    (0.16, -3.4), (0.18, -2.4), (0.2, -1.9), (0.22, -0.2), (0.24, -0.2), (0.26, -2.1), (0.28, -1.7), (0.3, -0.1),
    (0.32, 0.0), (0.34, -0.8), (0.36, -0.9), (0.38, 0.0), (0.44, 0.0), (0.46, -1.2), (0.48, -1.9), (0.5, -1.6),
    (0.52, -1.8), (0.54, -0.9), (0.56, 0.0), (0.58, -0.5), (0.6, -1.5), (0.62, -1.1), (0.64, -0.1), (0.68, 0.0)])]}
ALIAS_TRACKS["Violins II f62"]["tables"] = {"POST_SHAPES_S": [(244.0, [
    (-0.16, 0.0), (-0.14, -3.1), (-0.12, -4.5), (-0.1, -2.9), (-0.08, -4.6), (-0.06, -6.3), (-0.04, -6.4), (-0.02, -6.4),
    (0.0, -8.2), (0.02, -14.0), (0.04, -14.9), (0.06, -14.3), (0.08, -14.2), (0.1, -14.0), (0.12, -13.1), (0.14, -11.5),
    (0.16, -9.6), (0.18, -8.4), (0.2, -7.3), (0.22, -8.3), (0.24, -11.4), (0.26, -13.0), (0.28, -11.6), (0.3, -8.7),
    (0.32, -6.6), (0.34, -5.9), (0.36, -7.1), (0.38, -9.2), (0.4, -10.6), (0.42, -11.7), (0.44, -11.8), (0.46, -11.5),
    (0.48, -11.4), (0.5, -11.5), (0.52, -11.4), (0.54, -10.6), (0.56, -9.8), (0.58, -9.1), (0.6, -7.7), (0.62, -5.2),
    (0.64, -3.2), (0.68, 0.0)])]}

# ======================================================================================================================
# c43 (series 2): critics A (articulation), B (balance), C (tempo/timing) on the c42 render; Dan's S2 first
# ======================================================================================================================
# S2 timing (per-onset tables refitted on pcX: build/leg_leads.json "_c43", entry_leads.json "_c43", the new
# build/retongue_leads.json; cycles/c43/actor_scripts/edit_leads43.py). Horn 2's duet joins after eighths (240, 246,
# 262) sat at the 0.45 cap of the eighth (about 0.06 s): the raised cap on listed onsets only, as for the celli
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{"Horn 2": [(220.0, 268.0, 0.75, "listed")]})
# Horn 1 420 (after the eighth at 419.5) likewise. critic C #5: Violas 428 and celli 594 (behind a slur head that speaks
# about 20 ms early) and the Violins II f62 joins 230 / 231.5 did not move at all: the new LEAD WARNING (tools) showed the
# 0.75 cap of the eighth before them holding them, not LEG_MIN_GAP_S; 0.95 on these listed onsets only (the eighth before
# still sounds 0.11-0.12 s from its own moved onset, over the 0.10 s minimum gap)
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{
    "Horn 1": [(418.0, 421.0, 0.75, "listed")],
    "Violins II": [(229.9, 231.6, 0.95, "listed")] + LEG_CAP_FRAC.get("Violins II", []),
    "Violas": [(427.9, 428.1, 0.95, "listed")] + LEG_CAP_FRAC.get("Violas", []),
    "Violoncellos": [(593.9, 594.1, 0.95, "listed")] + LEG_CAP_FRAC.get("Violoncellos", [])})
# ---- c43 balance (critic B, simulated on the c42 stems first: cycles/c43/actor_scripts/simb43.py) ----
# B #1, bars 70-71 (qn 276-284): the closing theme's tune (Flutes a2, Violins I, Oboe 1) released its crescendo gain
# mid-phrase while the head-motif counter (Clarinets, Horns a2, Violins II) kept its lifts: tune +2, counter -2 / -4
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES.get("Violins I", []) + [[(275.5, 0.0), (276.5, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES.get("Flute 1", []) + [[(275.0, 0.0), (277.0, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Flute 2"] = LEVEL_SHAPES.get("Flute 2", []) + [[(275.0, 0.0), (277.0, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES.get("Oboe 1", []) + [[(275.5, 0.0), (276.25, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [[(277.625, 0.0), (277.875, -4.0), (283.75, -4.0), (284.0, 0.0)]]
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES.get("Clarinet 1", []) + [[(276.75, 0.0), (277.25, -2.0), (283.75, -2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES.get("Horns a2", []) + [[(276.75, 0.0), (277.25, -2.0), (283.75, -2.0), (284.0, 0.0)]]
# B #2, letter F (qn 388-407): Horns a2 and Trombone 1 (f) answer the ff tune with half note + three eighths, 9-17 dB
# under the tune: +3 over the passage, +6 on the first eighth of each figure (it sits on the HO pickup plateau); 394.5 only
# +0.5 (c43 stem fix; +1.5 rendered it 3.0 dB over the next eighth): with +6 the simulation put it 6.4 dB over the next eighth (it was already 1.8 dB over it). Simulated (A, re M):
# brass median -11.7 -> -8.3, tune minus brass +9.8 -> +6.2 dB (B: 5-6); B #1 tune minus counter 276-283 +2.5/+2.4/0.0/-0.7/
# +0.8/+2.7/-1.5/-2.1 -> +3.9/+4.8/+4.2/+3.5/+4.9/+7.1/+2.6/+2.4 dB, master K within +-0.5 dB
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES["Horns a2"] + [[(387.75, 0.0), (388.0, 3.0), (404.25, 3.0), (404.5, 0.0)]]
LEVEL_SHAPES["Trombone 1"] = LEVEL_SHAPES.get("Trombone 1", []) + [[(387.75, 0.0), (388.0, 3.0), (406.25, 3.0), (406.5, 0.0)]]
PICKUP_LIFT["Horns a2"].update({390.5: 6.0, 394.5: 0.5, 398.5: 6.0})
PICKUP_LIFT["Trombone 1"].update({390.5: 6.0, 394.5: 0.5, 398.5: 6.0, 406.5: 6.0})
# critic C #1 step 2 (S2, slow sections): the bass clarinet's soft legato joins (v60, CC11 34; Lento bars 1-3 and coda
# 708 / 710) change pitch on time but dip 2-4 dB around the beat and swell 3-8 dB over the old note at +0.2..+0.4 s, so
# their weight lands 0.25-0.3 s after the beat (no hairpin there). Level shapes fitted on the c42 stem
# (cycles/c43/actor_scripts/bclfit43.py: 50 ms level within +-1.5 dB of the line from the old note's body to the new
# note's body over -0.1..+0.5 s; before -4.7..+7.7 dB, simulated after -1.4..+1.9 dB). No more lead (the crossover is
# on time)
LEVEL_SHAPES_S["Bass clarinet"] = LEVEL_SHAPES_S.get("Bass clarinet", []) + [
    (4.0, [(-0.16, 0.0), (-0.12, 1.8), (-0.08, 2.8), (-0.04, 3.2), (0.0, 2.8), (0.04, 2.0), (0.08, 1.3), (0.12, -0.0), (0.16, -1.7), (0.2, -3.5), (0.24, -4.8), (0.28, -5.6), (0.32, -5.9), (0.36, -6.0), (0.4, -6.0), (0.44, -5.3), (0.48, -4.0), (0.52, -2.4), (0.56, -1.4), (0.6, -0.9), (0.64, 0.0)]),
    (10.0, [(-0.16, 0.0), (-0.12, 0.1), (-0.08, 0.7), (-0.04, 1.6), (0.0, 2.6), (0.04, 3.1), (0.08, 3.3), (0.12, 3.0), (0.16, 2.3), (0.2, 1.0), (0.24, -0.8), (0.28, -2.5), (0.32, -3.9), (0.36, -4.4), (0.4, -3.9), (0.44, -2.7), (0.48, -1.4), (0.52, -0.5), (0.56, -0.1), (0.6, 0.2), (0.64, 0.0)]),
    (708.0, [(-0.16, 0.0), (-0.12, 1.1), (-0.08, 2.2), (-0.04, 3.3), (0.0, 3.7), (0.04, 2.9), (0.08, 1.9), (0.12, 0.6), (0.16, -0.7), (0.2, -2.3), (0.24, -3.9), (0.28, -5.1), (0.32, -5.9), (0.36, -5.9), (0.4, -5.2), (0.44, -4.3), (0.48, -3.1), (0.52, -2.3), (0.56, -1.6), (0.6, -1.1), (0.64, 0.0)]),
    (710.0, [(-0.16, 0.0), (-0.12, 1.1), (-0.08, 1.6), (-0.04, 2.1), (0.0, 2.7), (0.04, 3.2), (0.08, 3.7), (0.12, 3.9), (0.16, 3.6), (0.2, 2.8), (0.24, 1.3), (0.28, -0.1), (0.32, -1.1), (0.36, -1.3), (0.4, -0.7), (0.44, -0.2), (0.48, 0.1), (0.52, 0.2), (0.56, 0.1), (0.6, 0.1), (0.64, 0.0)])]
# S2 follow-up (kit LEARNINGS c30: "after any legato-lead change, re-measure every fill that starts before its target"):
# the notches, level shapes and early fills keyed to a join whose c43 lead moved it are moved with the note by its
# realised change (no render to re-place them before this one; re-measure on c43). Notches and qn shapes by the note's
# qn shift, LEVEL_SHAPES_S rows by its seconds (early_fills.json pre_s / hold_s by edit_leads43.py's second step)
def _c43_move_notch(t_, row_, dq_):
    JOIN_NOTCH[t_] = [(row_[0] + dq_, row_[1] + dq_, row_[2]) if tuple(r_) == tuple(row_) else r_ for r_ in JOIN_NOTCH[t_]]
for t_, row_, dq_ in [("Flute 1", (394.9, 395.24, -6.4), -0.147), ("Oboe 1", (315.45, 315.58, -2.6), -0.1184),
                      ("Clarinet 1", (506.8, 507.13, -2.5), -0.168), ("Bassoon 1", (130.87, 131.18, -6.2), -0.1066),
                      ("Horn 2", (248.97, 249.18, -4.6), -0.0585), ("Trombone 1", (699.96, 700.14, -4.6), -0.144),
                      ("Violins I", (266.74, 266.9, -5.4), -0.0992)]:
    _c43_move_notch(t_, row_, dq_)
LEVEL_SHAPES["Cor anglais"] = [[(q_ - 0.0423, v_) for q_, v_ in sh_] if sh_[0][0] == 23.7 else sh_ for sh_ in LEVEL_SHAPES["Cor anglais"]]
def _c43_move_lss(t_, q0_, ds_):
    LEVEL_SHAPES_S[t_] = [(q_, [(s_ - ds_, v_) for s_, v_ in pts_]) if abs(q_ - q0_) < 0.01 else (q_, pts_)
                          for q_, pts_ in LEVEL_SHAPES_S[t_]]
for t_, q0_, ds_ in [("Cor anglais", 684.0, 0.12), ("Clarinet 1", 422.0, 0.08), ("Violins II", 564.0, -0.05),
                     ("Violoncellos", 3.0, -0.08)]:
    _c43_move_lss(t_, q0_, ds_)

# ---------- c43 stem fix (level only, measured on the c43 main render) ----------
# MANUAL-GAPS #6 (the CC16 round-robin reset, first render with it): with identical data the Leg Slur MAX legato targets
# of Horn 1 (the dolce solos of bars 47-52 and 147-154, bars 103-106) and Trumpet 1 (bars 69-71, 113-114, 161) rendered
# 1-9 dB (Trumpet 1 up to 14.5 dB) louder than in c41 / c42; the 2-5 kHz share moved both ways (other takes, not a
# louder layer). The phrase starts and every other brass track kept their c42 levels. Contours per note back to the c42
# levels (c42 = c41 = the state the balance was fitted on; cycles/c43/actor_scripts/statefix43.py), stepped at each
# moved onset; Violas 654.5 (Leg BC, +5.6 dB, c41 = c42) likewise. If c44 renders the quiet state again (no CC16 effect
# or a different one), these rows must come out (compare per note with c42 first)
# c44 (critic B #1): the c44 render (every Opus instance rebuilt, CC16 reset sent) played these notes in the quiet c42
# state again: Horn 1 / Trumpet 1 / Violas 654.5 came out low by about each row's cut (Horn 1 195 -8.0 against a -9.3
# cut, Trumpet 1 283.5 -16.3 against -14.5, Violas 654.25-654.75 -4.7 against -5.6; the hall change predicts -0.2..-0.8).
# By B's rule the rows come out (restored on the c44 stems by stem fix); kept here, switched off, for the record
_C43_STATEFIX_ROWS = False
if _C43_STATEFIX_ROWS:
    LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES.get("Trumpet 1", []) + [
        [(275.2368, 0.0), (275.3268, -3.0), (275.7869, -3.0), (275.8269, -5.2), (276.7868, -5.2), (276.8268, -6.9), (278.79, -6.9), (278.83, -5.4), (279.895, -5.4), (279.935, -7.1), (281.29, -7.1), (281.33, -7.4), (281.79, -7.4), (281.83, -6.7), (282.79, -6.7), (282.83, -5.7), (283.29, -5.7), (283.33, -14.5), (283.895, -14.5), (283.935, -2.4), (284.7207, -2.4), (284.8207, 0.0)],
        [(451.2333, 0.0), (451.3233, -5.0), (451.8913, -5.0), (451.9313, -5.7), (453.2808, -5.7), (453.3208, -4.9), (453.7802, -4.9), (453.8202, -6.6), (454.7789, -6.6), (454.8189, -4.4), (455.2783, -4.4), (455.3183, -6.8), (455.8888, -6.8), (455.9288, 0.0), (456.7082, 0.0), (456.8082, 0.0)],
        [(642.7833, 0.0), (642.8733, -4.5), (643.3333, -4.5), (643.3733, -2.2), (643.75, -2.2), (643.85, 0.0)],
    ]
    LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [
        [(654.1667, 0.0), (654.2567, -5.6), (654.665, -5.6), (654.765, 0.0)],
    ]
    LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES.get("Horn 1", []) + [
        [(183.8377, 0.0), (183.9277, -1.2), (187.3863, -1.2), (187.4263, 0.0), (187.8484, 0.0), (187.8884, -2.5), (188.8863, -2.5), (188.9263, -2.2), (190.6021, -2.2), (190.6421, -1.4), (191.8295, -1.4), (191.8695, -2.9), (193.388, -2.9), (193.428, -4.8), (193.888, -4.8), (193.928, -3.6), (194.8133, -3.6), (194.8533, -5.6), (195.388, -5.6), (195.428, -9.3), (195.775, -9.3), (195.815, -2.5), (197.888, -2.5), (197.928, -3.2), (199.8454, -3.2), (199.8854, 1.3), (200.6267, 1.3), (200.6667, -5.0), (202.8863, -5.0), (202.9263, 0.0), (203.8295, 0.0), (203.8695, -1.3), (205.3863, -1.3), (205.4263, -2.7), (205.8863, -2.7), (205.9263, -3.0), (207.9242, -3.0), (208.0242, 0.0)],
        [(411.009, 0.0), (411.099, -5.7), (411.874, -5.7), (411.914, -4.3), (412.895, -4.3), (412.935, -2.1), (414.753, -2.1), (414.793, -8.6), (415.8204, -8.6), (415.8604, -4.5), (417.3721, -4.5), (417.4121, -7.1), (417.775, -7.1), (417.815, -5.9), (418.7016, -5.9), (418.7416, -3.3), (419.3721, -3.3), (419.4121, -1.4), (419.625, -1.4), (419.665, -3.2), (421.874, -3.2), (421.914, -4.0), (423.9227, -4.0), (424.0227, 0.0)],
        [(583.8377, 0.0), (583.9277, 0.0), (587.3863, 0.0), (587.4263, -4.1), (587.775, -4.1), (587.815, -3.9), (588.8105, -3.9), (588.8505, -1.9), (590.8295, -1.9), (590.8695, -3.7), (591.8295, -3.7), (591.8695, -4.9), (593.108, -4.9), (593.148, -2.8), (593.888, -2.8), (593.928, -3.4), (594.888, -3.4), (594.928, -6.0), (595.275, -6.0), (595.315, -6.6), (595.888, -6.6), (595.928, -3.7), (597.776, -3.7), (597.816, -1.2), (599.9313, -1.2), (599.9713, 0.0), (600.8008, 0.0), (600.8408, 0.0), (602.8863, 0.0), (602.9263, -3.5), (603.8295, -3.5), (603.8695, -4.2), (605.3863, -4.2), (605.4263, -2.0), (605.8863, -2.0), (605.9263, 0.0), (607.9242, 0.0), (608.0242, 0.0)],
        [(611.8193, 0.0), (611.9093, 0.0), (612.888, 0.0), (612.928, -1.6), (613.888, -1.6), (613.928, -2.6), (614.888, -2.6), (614.928, -3.5), (615.9104, -3.5), (615.9504, 0.0), (617.7387, 0.0), (617.8387, 0.0)],
    ]

# ---------- c44 (ONE_TIME: drier hall, string repeats; critics A, B, C on c43) ----------
# ONE_TIME #4 + critic A #1-#2 + B #5 (Dan's S1, repeated notes audibly separate): STR_REP_NEW_BOW (tools, generic). The
# 49 same-pitch string repeats the legato merge joined into the note before with a 6-14 CC notch (stem dips 2-4 dB,
# master 1.5-3 dB; A's list) become: 13 loud strokes + 2 slur heads at p-mp (Violas 500, celli 656) as fresh Sus MAX
# strokes after a min(0.06 s, 25%) gap with the string re-tongue lead; the 10 slurred portato motif repeats
# (`d''8( des'' c'' | c''4--)`, A #1: the winds already re-tongue them) as strokes after a min(0.05 s, 25%) gap with a
# 6 / 8 CC fall over the eighth's last 0.04 s; the 24 soft (pp-p) re-bows as re-bow points at the printed onsets (Sus MAX
# pieces after 0.03 qn, fitted by fit_rebows.py; target stem dip 3-5 dB). The 24 tremolo common tones stay merged
# A #2 scope: the unmerged Sus MAX -> Sus MAX repeats of 0.4 s or more at mf and louder get the same gap ("sus_min_s")
STR_REP_NEW_BOW = {"gap_s": 0.06, "frac": 0.25, "stroke_cc": DYN["mf"], "stroke_mark": "mp", "head_cc": DYN["p"], "sus_min_s": 0.4,
                   "portato": {"gap_s": 0.05, "frac": 0.25, "fall_cc": 6, "fall_cc_loud": 8, "fall_s": 0.04}}
# c45 (critic A #1, S2): the "sus_min_s" repeats take the string re-tongue lead (tools); the basses have no
# RETONGUE_LEAD_S value, so they take "sus_lead_s" (the other sections' 0.10 s). Residuals per onset in retongue_leads.json
STR_REP_NEW_BOW = dict(STR_REP_NEW_BOW, sus_lead_s=0.10)
# A #2: the frozen automatic re-bows that sat near (not at) the printed bow changes now played by the rule (two bow events
# within a second) come out, with their rebow_fills.json rows; one point stays inside each printed Lento note longer than
# REBOW_MAX_S (Violas 30.034 / 34.694 / 38.65, celli 29.383 / 33.403 / 37.377 / 41.38 / 49.683). The NOTCH_SKIP entries for
# those printed bow changes go too (the soft re-bows take no notch; 164 is a stroke)
_REBOW_OUT_C44 = {"Violins II": [189.62], "Violas": [32.364, 36.856, 39.353, 52.384, 686.694, 699.507],
                  "Violoncellos": [31.393, 39.879, 45.371, 51.87, 152.461, 163.877, 169.146]}
REBOW_AT = dict(REBOW_AT, **{t_: [q_ for q_ in REBOW_AT[t_] if not any(abs(q_ - r_) < 1e-3 for r_ in out_)]
                             for t_, out_ in _REBOW_OUT_C44.items()})
# Violas 36.856 sat 1.0 s after the printed re-bow at 36 (A's own double-event list): moved to 38.65, near the middle of
# the printed 36-40 whole note (4.7 s) and 0.75 s clear of the basses' 38.003; its fill row is dropped and refit
REBOW_AT["Violas"] = sorted(REBOW_AT["Violas"] + [38.65])
NOTCH_SKIP = dict(NOTCH_SKIP, **{"Violoncellos": [q_ for q_ in NOTCH_SKIP["Violoncellos"] if q_ not in (40.0, 52.0, 164.0)],
                                 "Violas": [q_ for q_ in NOTCH_SKIP["Violas"] if q_ != 52.0]})
# critic B #2, bar 170 (qn 676-679, the coda's ff fermata chord): Trombone 1's inner D4 covered the tune's arrival on B in
# Trumpets a2 (4.4-7.0 dB over it, 676.5-677.75): Trombone 1 -3, Trumpet 1 (read by its Trumpets a2 alias) +3 then +1
LEVEL_SHAPES["Trombone 1"] = LEVEL_SHAPES.get("Trombone 1", []) + [[(676.25, 0.0), (676.5, -3.0), (678.875, -3.0), (679.0, 0.0)]]
LEVEL_SHAPES["Trumpet 1"] = LEVEL_SHAPES.get("Trumpet 1", []) + [[(676.375, 0.0), (676.625, 3.0), (677.25, 3.0), (677.75, 1.0), (678.875, 1.0), (679.0, 0.0)]]
# critic B #3, bar 158 (qn 629-632): Horns a2's held E4 bloomed 4.5 dB (sample, flat envelope) while the melody's top
# octave (Violins I, Flutes) faded: horns -2.5 / -3, Violins I +1.5 / +2.5
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES["Horns a2"] + [[(629.25, 0.0), (630.0, -2.5), (630.5, -3.0), (631.75, -3.0), (632.0, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES.get("Violins I", []) + [[(629.75, 0.0), (630.5, 1.5), (631.0, 2.5), (632.0, 2.5), (632.25, 0.0)]]
# critic B #5 (stem fix on the c44 render): the stroke trims in build/note_trims.json step in over 0.1 s
for t_, qs_ in (("Violoncellos", (84.0, 88.0, 152.0, 156.0, 448.0)), ("Violas", (500.0, 372.0, 136.0)), ("Violins II", (108.0,))):
    NOTE_TRIM_RAMP_S[t_] = {**NOTE_TRIM_RAMP_S.get(t_, {}), **{q_: 0.1 for q_ in qs_}}
# critic B #4 re-check (simulated on the stem-fixed c44 main stems): with the drier hall and the horn release cap, letter
# F's tune minus brass rose from +5.4 to +7.0 dB (B's window 5-6; brass re M -8.1 -> -9.1): Horns a2 and Trombone 1 +1 dB
# more over the c43 B #2 span
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES["Horns a2"] + [[(387.75, 0.0), (388.0, 1.0), (404.25, 1.0), (404.5, 0.0)]]
LEVEL_SHAPES["Trombone 1"] = LEVEL_SHAPES["Trombone 1"] + [[(387.75, 0.0), (388.0, 1.0), (406.25, 1.0), (406.5, 0.0)]]
# critic A #1 fallback (test, pass 2, not summed): the Violins I portato repeats dipped 1.5-3.6 dB on the stem
# (A's "dip below the eighth" 3.7-8.9 dB; 108 and 140 under 6): a pre-hall CC7 dip to 90 (about -6 dB on Opus's
# 40 log10 scale) over each gap, from the eighth's note-off to the tenuto's moved onset (CC7 acts before the hall,
# MANUAL-GAPS Results c36). "Vln I portato test" plays Violins I's notes around the four portatos with the dips
_VP_WIN = [(56.0, 64.0), (104.0, 112.0), (136.0, 144.0), (568.0, 576.0)]
ALIAS_TRACKS["Vln I portato test"] = {"source": "Violins I", "windows": _VP_WIN, "tables": {"CC7_POINTS": [
    (59.715, 127), (59.745, 90), (59.846, 90), (59.85, 127), (107.715, 127), (107.745, 90), (107.846, 90), (107.85, 127),
    (139.715, 127), (139.745, 90), (139.846, 90), (139.85, 127), (571.7134, 127), (571.7434, 90), (571.846, 90), (571.85, 127)]}}
PASS2_TRACKS = tuple(PASS2_TRACKS) + ("Vln I portato test",)
TEST_TRACKS = tuple(TEST_TRACKS) + ("Vln I portato test",)
# critic B #3 re-check on the c44 render: with the drier hall and the new horn releases, the B #3 shapes overshot (Horns
# a2 minus Violins I + Flutes over 629-632: c43 -0.5..+3.6, c44 -2.9..-7.0 dB, B's simulation -1.8..-0.3): the Horns a2 cut
# is undone and the Violins I lift halved (stem fix)
LEVEL_SHAPES["Horns a2"] = [s_ for s_ in LEVEL_SHAPES["Horns a2"] if s_ != [(629.25, 0.0), (630.0, -2.5), (630.5, -3.0), (631.75, -3.0), (632.0, 0.0)]]
LEVEL_SHAPES["Violins I"] = [s_ if s_ != [(629.75, 0.0), (630.5, 1.5), (631.0, 2.5), (632.0, 2.5), (632.25, 0.0)] else
                             [(629.75, 0.0), (630.5, 0.75), (631.0, 1.25), (632.0, 1.25), (632.25, 0.0)] for s_ in LEVEL_SHAPES["Violins I"]]
# the portato CC7 test decided (c44 test stem against the Violins I stem, A's measure): dip below the eighth 11.4 / 5.9 /
# 5.9 / 7.0 -> 12.5 / 5.8 / 6.2 / 11.1 dB at 60 / 108 / 140 / 572 (only 572 gained); not adopted, test track removed
ALIAS_TRACKS.pop("Vln I portato test")
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ != "Vln I portato test")
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ != "Vln I portato test")

# ---------------------------------------------------------------------------------------------------------------------
# c45 (series 2), critics A / B / C on the c44 render
# critic A #2 (S1): the portato tenutos of the motif `d''8( des'' c'' | c''4--)` opened at the eighth's level and grew
# 6-8 dB through the beat (fresh Sus MAX swell; body peak +170..+374 ms). Per-tenuto shapes, seconds around the score
# onset: a front from the moved onset (-0.07 s) to +0.10 s, a body from +0.14 s to the next moved onset (A's values, after
# the Violins I 59.5 / 571.5 eighth trims were removed from note_trims.json)
def _portato(front_, body_, end_):
    return [(-0.075, 0.0), (-0.045, front_), (0.10, front_), (0.14, body_), (end_ - 0.036, body_), (end_, 0.0)]
for t_, q_, f_, b_, e_ in (("Violins I", 60.0, 1.7, -3.0, 0.376), ("Violins I", 572.0, 1.8, -2.0, 0.376),
                           ("Violins I", 140.0, 0.0, -2.0, 0.376), ("Violas", 108.0, 1.8, 0.0, 0.448),
                           ("Violas", 668.0, 1.3, 0.0, 0.448), ("Violoncellos", 524.0, 1.2, 0.0, 0.376)):
    LEVEL_SHAPES_S[t_] = LEVEL_SHAPES_S.get(t_, []) + [(q_, _portato(f_, b_, e_))]
# Violas 136 (p): the hole fell after the beat (soft attack about 0.3 s): +0.10 s re-attack lead (retongue_leads.json)
# and a +3 dB fill from the moved onset to the score onset (early_fills.json); its -2.5 note trim is removed
# critic B #4: the c44 stroke trims on celli 152 (+5) / 156 (+5.5) lifted the fresh Sus MAX bloom over the bar: the celli's
# held note was the loudest stem by up to 5.8 dB at 155-159 and the step into the bar-41 sf fell 6.2 -> 3.5 dB. A body cut
# after each stroke's front (B's shape; simulated: celli minus the loudest other stem -2.9..+0.8, step +4.9 dB)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(152.75, 0.0), (153.5, -2.0), (155.75, -2.0), (156.25, 0.0),
                                                                (156.5, 0.0), (157.0, -3.0), (157.5, -5.0), (159.75, -5.0), (160.0, 0.0)]]
# critic B #3 (Dan's timpani rule): bars 127-128, the pp G2 roll covered the celli's repeated pp G2 quarters (same pitch;
# celli minus timpani in 79-125 Hz +4..+18 dB in c43, +1..+8 in c44 after the 150 ms release cap took their tails)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(503.75, 0.0), (503.95, 3.5), (511.75, 3.5), (512.25, 0.0)]]
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES.get("Timpani", []) + [[(503.5, 0.0), (504.0, -2.0), (512.0, -2.0), (514.0, 0.0)]]
# critic C #2 (test, pass 2, not summed): with the hall halved, the patches' release-trail samples (gains 0.58-3.98, i.e.
# -4.7..+12 dB) set each family's early tail (0.15-0.25 s after phrase ends: horns -9.8, strings -13.5, winds -15.4,
# Trumpets 1-3 -16.0 dB re body) and the overlap inside the string sections (Violins II detache old pitch -10 dB 0.254 s
# after the note-off). Three fresh instances play their source's own notes, lanes and leads with every release-trail
# group 6 dB lower (mix.json "rt_gain_db"; build_reaper rt_gain); measured against the main stems on the same notes
_RT45 = {"Vln II rt test": "Violins II", "Vla rt test": "Violas", "Hn1 rt test": "Horn 1"}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": [(0.0, 730.0)]} for n_, s_ in _RT45.items()})
PASS2_TRACKS = tuple(PASS2_TRACKS) + tuple(_RT45)
TEST_TRACKS = tuple(TEST_TRACKS) + tuple(_RT45)
# critic A #4 (optional, test, pass 2, not summed): the slurred 0.20-0.25 s notes that Violins II and the violas share
# with Violins I are re-attacked on Sus MAX against Violins I's Leg Slur targets (Violins II a median 47 ms ahead, 15 of
# 21 onsets more than 30 ms apart; violas robust SD 70 ms, 25 of 36). Two fresh instances play their source's notes with
# SHORT_SUS_LEG_TRACKS including the source (as Violins I since c06-c07; LEG_CAP_FRAC 0.75 is already set for both).
# Judged against the main Violins I stem on pcX (A's target: at most 6 of 57 shared onsets more than 30 ms apart) and
# for joins of 6 dB or more (those go to SHORT_SUS_LEG_SKIP if adopted)
_LEG45 = {"Vln II leg test": "Violins II", "Vla leg test": "Violas"}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": [(0.0, 730.0)],
                                          "globals": {"SHORT_SUS_LEG_TRACKS": tuple(SHORT_SUS_LEG_TRACKS) + (s_,)}}
                                     for n_, s_ in _LEG45.items()})
PASS2_TRACKS = tuple(PASS2_TRACKS) + tuple(_LEG45)
TEST_TRACKS = tuple(TEST_TRACKS) + tuple(_LEG45)
# ---------- c45 stem fix (level only, measured on the c45 render) ----------
# Violas 136 (A #2): with the +0.10 s lead the p eighth before the tenuto gave way to 0.11 s and barely spoke (band
# level -6 dB against c44, the tenuto 11 dB over it); the eighth is lifted +6 dB, the +3 dB early fill comes out and
# the tenuto body takes -2 dB from +0.15 s (front kept)
LEVEL_SHAPES_S["Violas"] = LEVEL_SHAPES_S.get("Violas", []) + [(136.0, [(-0.345, 0.0), (-0.33, 6.0), (-0.215, 6.0), (-0.19, 0.0),
                                                                        (0.08, 0.0), (0.15, -2.0), (0.34, -2.0), (0.376, 0.0)])]
# Clarinet 1 224 (A #3 auto fill): the new fill (+3.8 dB to +0.35 s) lifted the note's front, which had no hole, 3.7 dB
# over the note before; the sag sits at +0.40..+0.55 s (9-10 dB under the body). Fill removed, a shape over the sag
LEVEL_SHAPES_S["Clarinet 1"] = LEVEL_SHAPES_S["Clarinet 1"] + [(224.0, [(0.25, 0.0), (0.38, 6.0), (0.50, 6.0), (0.62, 2.0), (0.72, 0.0)])]
# soft re-bows (STR_REP_NEW_BOW printed bow changes at pp-p) whose pieces were too short for fit_rebows.py (MIN_PIECE_S)
# or whose fit left deep holes: pitch-band dips of 8-13 dB on the c45 stems (Violas / Violins II 580 together, bar 146
# under the oboe's dolce; celli 176 / 180 under the bar-45 clarinet solo; Violins II 192). A shape filling each hole to
# 4 dB under the level before (cycles/c45/actor_scripts/rbshape45.py; A's soft re-bow target 3-5 dB)
LEVEL_SHAPES_S["Violins II"] = LEVEL_SHAPES_S.get("Violins II", []) + [(192.0, [(0.04, 0.0), (0.08, 3.5), (0.12, 4.0), (0.16, 2.6), (0.2, 3.6), (0.24, 3.1), (0.28, 0.0)]), (580.0, [(0.0, 0.0), (0.04, 0.3), (0.08, 4.8), (0.12, 6.1), (0.16, 4.9), (0.2, 3.7), (0.24, 1.5), (0.28, 1.5), (0.32, 1.7), (0.36, 0.6), (0.4, 0.0)])]
LEVEL_SHAPES_S["Violas"] = LEVEL_SHAPES_S.get("Violas", []) + [(580.0, [(0.0, 0.0), (0.04, 1.3), (0.08, 4.0), (0.12, 8.0), (0.16, 8.0), (0.2, 5.3), (0.24, 4.5), (0.28, 5.1), (0.32, 4.7), (0.36, 1.0), (0.4, 0.0)])]
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [(176.0, [(0.04, 0.0), (0.08, 3.4), (0.12, 4.4), (0.16, 4.6), (0.2, 6.3), (0.24, 6.5), (0.28, 2.5), (0.32, 0.2), (0.36, 0.0)]), (180.0, [(0.04, 0.0), (0.08, 1.6), (0.12, 3.4), (0.16, 4.2), (0.2, 3.4), (0.24, 2.4), (0.28, 1.5), (0.32, 0.5), (0.36, 0.0)])]
# the c45 tests decided (test stems against the main stems on the same notes; cycles/c45/CHANGES.md):
# C #2 release-trail gain -6 dB: Violas pass every C criterion that applies (running figures' old pitch at +70 ms -6.2 ->
# -8.4 dB, early tail 0.15-0.25 s -12.1 -> -17.5 dB, tail at 0.4-0.6 s -7.9 -> -8.1, joins of 5 dB or more 14 -> 10 of
# 129, one ending -10.1 dB in 0.05 s against -8.5): adopted on Violas (mix.json rt_gain_db; the test stem, which plays the
# Violas' notes and envelope exactly, replaces the Violas stem). Violins II: detache -10 dB point 0.256 -> 0.243 s (C:
# 0.22) and the tail at 0.4-0.6 s 1.9 dB lower; Horn 1: tail at 0.4-0.6 s 1.6 dB lower: not adopted.
# A #4 legato on the shared slurred eighths: Violins II onsets more than 30 ms from Violins I 26 -> 24 of 34 (target 6 of
# 57), joins of 6 dB or more 3 -> 6; violas 32 -> 31 of 44, 1 -> 7: not adopted. Test tracks removed
for n_ in tuple(_RT45) + tuple(_LEG45):
    ALIAS_TRACKS.pop(n_)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _RT45 and t_ not in _LEG45)
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ not in _RT45 and t_ not in _LEG45)

# ---------------------------------------------------------------------------------------------------------------------
# c46 (series 2), critics A / B / C on the c45 render
# critic B #1: c45's whole-piece test aliases did not play their sources' data (the c10 window-end boost rule carried the
# violas' "espr." to qn 184 and 583: CC1 +40..+55, CC11 +3..+4; the Horn 1 / Violins II aliases also played the Horns a2
# / f62 notes their sources rest in), and the "Vla rt test" stem replaced the Violas stem (violas 3-7 dB too loud in bars
# 34-38, 44, 129, 135-136, 145). Tools: alias_dup() (a test alias plays its source's data), tw_own() (test windows = the
# source's own windows), tools/alias_check.py (run by score_to_parts.py on every TEST_TRACKS alias). The c45 trail-gain
# verdicts on Horn 1 / Violins II and the violas' "pass" are void; Violas keeps rt_gain_db -6 and its c46 main stem is
# compared with c45's render_first/30_Violas.wav (same notes and lanes).
# critic C #1 (A #5): with the c44 150 ms cap at every dynamic, soft string endings stop (final ppp chord -10 dB in 0.07 s;
# references 0.20-0.40 s). Test (pass 2, not summed): every section string track at 150 ms mf-ff / 350 ms pp-p
# (build_reaper.py takes a list of cap specs), each alias playing exactly its source's notes, so a passing test stem can
# replace the main stem. critic C #2 re-test with matched data: Horn 1 and Violins II with rt_gain_db -6
_SC46 = {"Vla softcap test": "Violas", "Vc softcap test": "Violoncellos", "Vln I softcap test": "Violins I",
         "Vln II softcap test": "Violins II", "Cb softcap test": "Double basses"}
_RT46 = {"Hn1 rt test": "Horn 1", "Vln II rt test": "Violins II"}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": tw_own(s_, 0.0, 730.0)} for n_, s_ in {**_SC46, **_RT46}.items()})
PASS2_TRACKS = tuple(PASS2_TRACKS) + tuple(_SC46) + tuple(_RT46)
TEST_TRACKS = tuple(TEST_TRACKS) + tuple(_SC46) + tuple(_RT46)
# critic A #1 (S2): the coda Cello solo's leads were fitted on c40's m37 estimator and never refit on pcX (690 / 694 / 687 /
# 684 +156 / +153 / +89 / +63 ms late, 685 / 691 / 680 -93 / -62 / -93 early; robust SD 70 ms). New lead = realised +
# 0.9 x (pcX - 0.015 s) (685 keeps some anticipation for the glide); its level contour and join shapes move with the moved
# onsets (below, after the leads are set)
ALIAS_TRACKS["Cello solo"]["tables"]["LEG_LEADS"] = {"684.0": -0.03, "685.0": 0.07, "687.0": 0.10, "688.0": -0.02,
                                                     "689.5": 0.05, "690.0": 0.04, "691.0": 0.06, "694.0": 0.03}
ALIAS_TRACKS["Cello solo"]["tables"]["ENTRY_LEADS"] = {"680.0": 0.14}
# critic A #3: exposed unaccented legato spikes (30 ms burst over the louder body, rel > -8 dB): notches over each burst's
# core (frames within 4 dB of the peak), depth peak - 2 dB. Bassoon 1 375: its c45 fill raise is reverted
# (early_fills.json, c44 value), so the notch takes the burst left after that (about +5 dB): -3.0
for t_, rows_ in {"Violins I": [(69.604, 69.793, -5.9), (495.675, 496.167, -5.4)],
                  "Bassoon 1": [(375.011, 375.437, -3.0)],
                  "Violas": [(77.723, 78.112, -4.9), (290.010, 290.147, -2.4)],
                  "Violoncellos": [(415.511, 415.850, -5.5)]}.items():
    JOIN_NOTCH = dict(JOIN_NOTCH, **{t_: JOIN_NOTCH.get(t_, []) + rows_})
assert (80.72, 80.88, -2.5) in JOIN_NOTCH["Violas"]   # Violas 81: the c45 burst peaks at -0.155 s, ahead of the old notch
JOIN_NOTCH["Violas"] = [r_ if r_ != (80.72, 80.88, -2.5) else (80.590, 80.842, -4.2) for r_ in JOIN_NOTCH["Violas"]]
# critic B #2 (Dan's timpani rule): bar 174, the pp G2 roll was the whole master band at 78-250 Hz, 8-14 dB over the
# bassoons' G2 (roles.json [692, 696, 6] -> 2, set for v221); bars 13-14, the p > pp roll 6.2 dB over the celli in its
# band: -3 dB after the printed p onset (it starts at its printed level, then settles under the strings)
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(48.5, 0.0), (49.5, -3.0), (55.3, -3.0), (56.0, 0.0)]]
# critic C #4 (a): three printed crescendo rolls barely grew (+0.3 / +1.8 / +0.2 dB; the roll trims step down as CC1 moves
# into a louder layer): a 0 -> +4 dB ramp over each hairpin, back to 0 before the stroke (its 0.06 s delay)
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(244.0, 0.0), (247.9, 4.0), (248.5, 0.0)],
                                                     [(456.0, 0.0), (459.9, 4.0), (459.98, 0.0)],
                                                     [(556.0, 0.0), (559.9, 4.0), (559.98, 0.0)]]
# critic B #3: letter F (bars 98-102), the Trombone 1 / Horns a2 half notes on each downbeat (f) reached the ff tune
# (tune minus brass +1.5..+4.8 dB K, right channel -0.1..+2.7): the c43 / c44 lift stays on the answering eighths, -4 dB
# on the half notes (simulated: +4.0..+6.9 K, beats 3-4 unchanged)
for b_ in (98, 99, 100, 101, 102):
    q_ = 4.0 * (b_ - 1)
    for t_ in (("Trombone 1", "Horns a2") if b_ < 102 else ("Trombone 1",)):
        LEVEL_SHAPES[t_] = LEVEL_SHAPES[t_] + [[(q_ - 0.30, 0.0), (q_ - 0.20, -4.0), (q_ + 2.10, -4.0), (q_ + 2.25, 0.0)]]
# critic C #3: the Lento's opening pp swell lost a third of its growth (c44's celli bells moved to the loud spans, the drier
# hall): celli and basses shapes over the two swells (simulated: growth 3 -> 6 +5.5 -> +7.6 dB, 8 -> 10 +5.1 -> +5.6)
for t_ in ("Violoncellos", "Double basses"):
    LEVEL_SHAPES[t_] = LEVEL_SHAPES.get(t_, []) + [[(3.8, 0.0), (5.0, 1.5), (6.0, 3.0), (7.0, 3.0), (8.0, 0.5), (8.5, 0.0)],
                                                   [(7.9, 0.0), (9.0, 1.5), (10.0, 2.0), (11.0, 1.0), (12.0, 0.0)]]
# critic C #2: both fff downbeats stepped only about 2 dB (mp3 +1.8 into 160, +2.5 into 122; references' 12 largest
# arrivals 3-8 dB) and the delivery limiter had room (about 0.0 dB): an _all lift from each downbeat. C's +1.0 variant
# (simulated: steps +2.6 / +3.1, limiter 0.6, span 19.1; the +1.5 variant gave span 19.2)
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(635.98, 0.0), (636.02, 1.0), (636.6, 1.0), (637.25, 0.0)],
                                               [(483.98, 0.0), (484.02, 1.0), (484.6, 1.0), (485.25, 0.0)]]
# critic A #6: the Violins I portato tenutos measured on the corrected body window (moved onset + 0.10 s to the next
# moved onset - 0.02 s, next pitch excluded): 60 / 140 / 108 still +3.4 / +3.9 / +2.9 dB over the eighth's peak (target
# -1..+2): body cuts -3.0 -> -4.5 (60), -2.0 -> -4.0 (140), a -1.0 body on 108 (front 0, as 140)
_old60, _old140 = (60.0, _portato(1.7, -3.0, 0.376)), (140.0, _portato(0.0, -2.0, 0.376))
assert _old60 in LEVEL_SHAPES_S["Violins I"] and _old140 in LEVEL_SHAPES_S["Violins I"]
LEVEL_SHAPES_S["Violins I"] = [r_ if r_ not in (_old60, _old140) else
                               ((60.0, _portato(1.7, -4.5, 0.376)) if r_ == _old60 else (140.0, _portato(0.0, -4.0, 0.376)))
                               for r_ in LEVEL_SHAPES_S["Violins I"]] + [(108.0, _portato(0.0, -1.0, 0.376))]
# the Cello solo's level contour (_DIVA_CONTOUR) and join shapes (_DIVA_JOINS) were fitted with crossfades from each
# target's old moved onset to its score onset + 0.05 qn, and the 685 Leg Port shape in seconds from its score onset. They
# move with the new moved onsets (old, new; read from the rebuilt parts.json): inside each target's span [previous score
# onset + 0.05, score onset + 0.05] the contour's times map piecewise linearly old moved -> new moved (values unchanged);
# each join shape moves by its nearest target's change; the 685 seconds shape by its change in seconds
_SOLO_MOVES = {680.0: (679.88, 679.92), 684.0: (683.9391, 683.8904), 685.0: (684.6711, 684.7686),
               687.0: (686.8112, 686.732), 688.0: (687.9208, 687.8782), 689.5: (689.26, 689.296),
               690.0: (689.964, 689.808), 691.0: (690.7, 690.784), 694.0: (693.964, 693.82)}
_SOLO_ONSETS = [680.0, 683.5, 684.0, 685.0, 687.0, 688.0, 689.5, 690.0, 691.0, 691.5, 692.0, 694.0]


def _solo_remap(t_):
    for i_, sq_ in enumerate(_SOLO_ONSETS):
        if sq_ not in _SOLO_MOVES:
            continue
        a_ = _SOLO_ONSETS[i_ - 1] + 0.05 if i_ else sq_ - 1.0
        e_ = sq_ + 0.05
        mo_, mn_ = _SOLO_MOVES[sq_]
        if a_ - 1e-9 <= t_ <= mo_:
            return round(a_ + (t_ - a_) * (mn_ - a_) / (mo_ - a_), 4)
        if mo_ < t_ <= e_ + 1e-9:
            return round(mn_ + (t_ - mo_) * (e_ - mn_) / (e_ - mo_), 4)
    return t_


_c46_contour = [(_solo_remap(t_), v_) for t_, v_ in _DIVA_CONTOUR]
assert all(b_[0] > a_[0] for a_, b_ in zip(_c46_contour, _c46_contour[1:]))


def _solo_join(sh_):
    mid_ = 0.5 * (sh_[0][0] + sh_[-1][0])
    sq_ = min(_SOLO_ONSETS, key=lambda s_: abs(s_ - mid_))
    d_ = _SOLO_MOVES[sq_][1] - _SOLO_MOVES[sq_][0] if sq_ in _SOLO_MOVES else 0.0
    return [(round(t_ + d_, 4), v_) for t_, v_ in sh_]


assert ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] == [_DIVA_CONTOUR] + _DIVA_JOINS
ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] = [_c46_contour] + [_solo_join(s_) for s_ in _DIVA_JOINS]
_d685_s = (_SOLO_MOVES[685.0][1] - _SOLO_MOVES[685.0][0]) * 60.0 / 72.0
assert ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES_S"][0][0] == 685.0
ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES_S"] = [
    (685.0, [(round(t_ + _d685_s, 3), v_) for t_, v_ in ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES_S"][0][1]])]
# critic A #5 (articulation): short Sus MAX slur heads (0.08-0.30 s) before a legato note of another pitch sat 5-10 dB under
# the note they lead into (Violins I median -3.9, celli -4.9 dB; a 0.09-0.12 s note ends before the mf Sus MAX sample
# reaches its body): exact lifts from each head's moved onset to its target's (PICKUP_LIFT, string tail 0.06 / 0.08 s),
# aiming at 2-3 dB under the next note
PICKUP_LIFT["Violins I"].update({259.5: 6.0, 146.5: 5.0, 377.0: 4.0, 66.5: 2.5, 61.0: 2.0, 58.5: 3.0})
PICKUP_LIFT["Violoncellos"].update({419.5: 6.0, 355.5: 5.0, 533.5: 3.5})
# ---------- c46 stem fix (level only, measured on the c46 render) ----------
# Violins I 496 (A #3): the burst is gone (+5.4 -> -0.9 dB), but this render's audio dips 5-6 dB at 496.0-496.1 (c45 held
# +5 dB there), inside the notch's last part, and the join dipped 7.9 dB: the notch ends at 495.96, before that dip
JOIN_NOTCH["Violins I"] = [r_ if r_ != (495.675, 496.167, -5.4) else (495.675, 495.96, -5.4) for r_ in JOIN_NOTCH["Violins I"]]
# Cello solo (A #1 follow-up, measured on the c46 pass-2 stem): with the new leads the 690 -> 691 transition bursts +8.6 dB
# over the louder body at 690.70-690.86 (c45 +2.6), and the 694 transition dips 5.4 dB at 693.97-694.02 (c45 2.2): a
# notch of burst - 2 dB over the burst's core and a 3 dB fill over the hole (alias-only rows)
ALIAS_TRACKS["Cello solo"]["tables"]["JOIN_NOTCH"] = [(690.70, 690.86, -6.6)]
ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] = ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] + [
    [(693.93, 0.0), (693.97, 3.0), (694.03, 3.0), (694.07, 0.0)]]
# the c46 tests decided (test stems against the main stems on the same notes, tools/alias_check.py OK for all seven):
# C #1 soft cap 350 ms at pp / p: adopted on every section string track and the f62 aliases (mix.json); the Violins I / II
# and Violas test stems replace their main stems, the celli and basses test stems are spliced in from the final chord
# (qn 711.7 / 711.85; before it, 8-10 bars differed by 1-2.5 dB from the second instance's round robins).
# C #2 trail gain -6 dB re-tested with matched data: Violins II (early tail -11.4 -> -13.7 dB, but the 0.4-0.6 s tail 2.1 dB
# lower, detache -10 dB point 0.254 -> 0.270 s, legato joins dipping 5 dB or more 26 -> 43 of 125) and Horn 1 (early tail
# -11.8 -> -14.1, late tail 1.0 dB lower, 5 dB joins 1 -> 8 of 47) fail; Violas, re-measured on its own lanes (c46 main
# stem against c45's render_first), pass as before (figures' old pitch -6.2 -> -8.4 dB, early tail -12.1 -> -17.0, late
# tail -7.9 -> -8.1, 5 dB joins 14 -> 12). Test tracks removed
for n_ in tuple(_SC46) + tuple(_RT46):
    ALIAS_TRACKS.pop(n_)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _SC46 and t_ not in _RT46)
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ not in _SC46 and t_ not in _RT46)

# ---------- c47 (series 2), critics A / B / C on the c46 render ----------
# critic B #4: bar 40, the celli's held A-flat3 (f, < to the bar-41 sf) was the loudest stem by 6-7 dB K over the violins'
# and woodwinds' run (the c45 B #4 body cut checked on A weighting, which takes 11 dB off the 208 Hz fundamental): the
# cut deepens to -8 dB over 157.5-159.6 (simulated: celli minus the loudest other K -1.1 / +3.4 / +3.9 / -0.7 / +4.2,
# step into the sf +6.1 -> +6.5 dB)
_c45b4 = [(152.75, 0.0), (153.5, -2.0), (155.75, -2.0), (156.25, 0.0),
          (156.5, 0.0), (157.0, -3.0), (157.5, -5.0), (159.75, -5.0), (160.0, 0.0)]
assert _c45b4 in LEVEL_SHAPES["Violoncellos"]
LEVEL_SHAPES["Violoncellos"] = [s_ if s_ != _c45b4 else _c45b4[:6] + [(157.5, -8.0), (159.6, -8.0), (159.75, -5.0), (160.0, 0.0)]
                                for s_ in LEVEL_SHAPES["Violoncellos"]]
# critic A #2 (S2, legato): the coda cello solo's 687 (A-flat4 -> G4) and 694 (C5 -> B4) sag 8.2 / 6.0 dB right after the
# change of note (the pitch arrives on time, so the notes sound late: pcX +118 / +102 ms; more lead made 687 worse in
# c46): level fills over each hole, additive to the contour and the 694 fill (simulated: dips 2.2 / 2.1 dB, pcX +2 /
# +18 ms, peaks +1.8 / +1.2 dB over the louder body). A's optional rows, same pattern: Bassoon 1 135 (bar 34 solo,
# G3 -> F3) and Clarinet 1 700 (coda espr., E-flat4 -> C5)
ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] = ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] + [
    [(686.99, 0.0), (687.03, 6.0), (687.16, 6.0), (687.29, 4.0), (687.36, 0.0)],
    [(693.985, 0.0), (694.025, 5.0), (694.15, 5.0), (694.26, 2.5), (694.33, 0.0)]]
LEVEL_SHAPES["Bassoon 1"] = LEVEL_SHAPES["Bassoon 1"] + [[(134.84, 0.0), (134.90, 4.5), (135.30, 4.5), (135.42, 0.0)]]
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(700.14, 0.0), (700.20, 5.0), (700.40, 5.0), (700.50, 0.0)]]
# critic A #3: two exposed accents sat under their own lifted pickup (Violins I bar 35: the accented D-flat5's body 5-9 dB
# under the unaccented pickup, its 2-5 kHz "front" the tail of the 12 dB lift; Clarinet 1 bar 127: the accented 505 no
# louder than its pickup): lifts 12 -> 6 and 9.5 -> 6.5 dB (simulated: each accent about 3-4.5 dB over its pickup; the
# Violins I pickup still 4.5 dB under its target's 200 ms peak, the c17 rule)
PICKUP_LIFT["Violins I"].update({136.5: 6.0})
PICKUP_LIFT["Clarinet 1"].update({504.5: 6.5})
# critic B #5: the delivered p10-to-max span was 19.35 dB (target 16-19): the c46 fff lift raised the top and the soft floor
# stayed. Delivery ride trims +0.5 dB over the passages at or under p10 (simulated on the c46 S curve: p10 -30.62 ->
# -30.23, span 18.96, climax untouched); the coda row starts after the 679.95-695.9 cello-solo row
_RT47 = [(0.0, 24.0), (52.0, 56.0), (129.0, 136.0), (168.0, 176.0), (300.0, 304.0), (572.0, 584.0), (612.0, 620.0),
         (656.0, 664.0), (696.0, 728.0)]
RIDE_TRIMS = RIDE_TRIMS + [([(0.0, 0.5)] if a_ == 0.0 else [(a_, 0.0), (a_ + 0.5, 0.5)]) + [(b_ - 0.5, 0.5), (b_, 0.0)]
                           for a_, b_ in _RT47]
# ---- c47 second-pass tests (TEST_TRACKS: rendered in pass 2, not summed; tools/alias_check.py on every alias) ----
# critic C #1 (A #5, coordinator (b)): the final ppp chord and the soft phrase ends still stop in a third of a recording's
# time (master final chord -10 / -20 dB in 0.12 / 0.33 s; Brahms 1/ii 0.40 / 0.79, Brahms 4/ii 0.20 / 0.48). The ppp
# chord plays the Sus MAX "pp" groups, which ship 931 ms; the 350 ms cap removes two thirds of it. Test: no cap on the pp
# groups (350 ms kept at p, 150 ms at mf-ff), every section on its own whole-piece windows (tw_own), so a passing stem
# can be spliced in where the effect is ("<S> ppcap test"). Fallback 700 ms at pp on the coda (696/680-730: the final
# chord and the coda's pp chord changes) for the sections that carry 95% of the final chord ("<S> pp700 test").
# (Violins I, 4% of the final chord's master power and 4 of the 117 pp chord changes, is left out for pass-2 memory: the
# c46 pass 2 settled at 34 GB with 61 loaded rows, this one holds 70; Violins I follows the others' verdict in c48)
_PPC47 = {"Vln II ppcap test": "Violins II", "Vla ppcap test": "Violas",
          "Vc ppcap test": "Violoncellos", "Cb ppcap test": "Double basses"}
_PP747 = {"Vln II pp700 test": ("Violins II", [(696.0, 730.0)]), "Vla pp700 test": ("Violas", [(680.0, 730.0)]),
          "Vc pp700 test": ("Violoncellos", [(696.0, 730.0)]), "Cb pp700 test": ("Double basses", [(696.0, 730.0)])}
# critics A #4 / C #3 (coordinator (c)), S1 / S2: the STR_REP_NEW_BOW strokes still swell in (time with the band 6 dB under
# the body 110-366 ms on celli 47, 156, 448, 456 and Violas 372): the c46 row A/B, now possible with ART_SPANS
# "stroke_row" (tools). Variant A "Stac Leg BC + Slur + Port MAX" (Celli key 90, Violas key 44; HO 2021 p.99) at
# velocity 40-60, variant B "Sus Marc LITE" at 25-45, on exactly the stroke onsets (spans [q, q + 0.01)). Variant A
# rides on the celli / violas ppcap instances (these strokes are mf-f, where both instances cap at 150 ms); "Vc stroke B"
# (the main caps) carries B on the same six celli strokes. Celli 47 (in the pp Lento, where the ppcap instance differs)
# is left out: its stroke holds a later re-bow point, which score_to_parts.py supports only on Sus MAX. Its windows run
# from two notes before each stroke to the note after it (fewer rows loaded: pass-2 memory)
_STR_A = {"art": "Stac Leg BC + Slur + Port MAX", "vel_by_cc": [(60, 40), (90, 50), (120, 60)], "stroke_row": True}
_STR_B = {"art": "Sus Marc LITE", "vel_by_cc": [(60, 25), (90, 35), (120, 45)], "stroke_row": True}
_STROKE_GL = {"STR_STROKE_ROWS": ("Sus MAX", "Sus Marc LITE", "Stac Leg BC + Slur + Port MAX")}


def _spans47(qs_, v_):
    return [dict(v_, **{"from": q_, "to": q_ + 0.01}) for q_ in qs_]


_VC_STROKES = [84.0, 88.0, 152.0, 156.0, 448.0, 456.0]
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": tw_own(s_, 0.0, 730.0)} for n_, s_ in _PPC47.items()})
ALIAS_TRACKS["Vc ppcap test"].update({"tables": {"ART_SPANS": _spans47(_VC_STROKES, _STR_A)}, "globals": _STROKE_GL})
ALIAS_TRACKS["Vla ppcap test"].update({"tables": {"ART_SPANS": _spans47([80.0, 372.0, 500.0], _STR_A)}, "globals": _STROKE_GL})
ALIAS_TRACKS["Vc stroke B"] = {"source": "Violoncellos",
                               "windows": [w_ for a_, b_ in [(80.0, 91.0), (144.0, 160.0), (440.0, 460.0)]
                                           for w_ in tw_own("Violoncellos", a_, b_)],
                               "tables": {"ART_SPANS": _spans47(_VC_STROKES, _STR_B)},
                               "globals": _STROKE_GL}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": [w_ for a_, b_ in ws_ for w_ in tw_own(s_, a_, b_)]}
                                     for n_, (s_, ws_) in _PP747.items()})
# critic C #2 (MANUAL-GAPS #1, coordinator (d)): accents have no edge (2-5 kHz modulation unchanged since c00, brass accent
# fronts -11.6 dB median under the body). The brass "Marc Sus LITE" row (1TB / 1FH KS Masters, read from the patches: a
# Marc Shrt / Marc Lng attack sample, three velocity layers 1-88 / 89-109 / 110-127 on 1TB and 1-62 / 63-109 / 110-127 on
# 1FH, each through a Butterworth low-pass at 423 Hz with velocity modulators, over CC1-crossfaded mp / ff (1FH mf / ff)
# sustain layers that fade in over 174 ms; HO 2021 p.101: velocity sets the attack's filter) has never been tried. Test on
# the accented notes of bars 32-33 and 142-143 at velocity 45-75 (filter mostly closed), the GENTLE_ACCENT swell cut to
# +1 dB (the sample gives the front), on one high and one low part of each patch (Trombone 1, Bass trombone; Horn 1,
# Horn 3), each on its own whole-piece windows
_MARC47 = {"Tbn1 marc test": ("Trombone 1", [124.0, 125.0, 128.0, 564.0, 566.0, 568.0]),
           "BTbn marc test": ("Bass trombone", [124.0, 125.0, 128.0, 568.0]),
           "Hn1 marc test": ("Horn 1", [124.0, 125.0, 128.0, 568.0]),
           "Hn3 marc test": ("Horn 3", [124.0, 125.0, 564.0, 566.0])}
_MARC_V = {"art": "Marc Sus LITE", "vel_by_cc": [(72, 45), (88, 55), (114, 70), (124, 75)]}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": tw_own(s_, 0.0, 730.0),
                                          "tables": {"ART_SPANS": _spans47(qs_, _MARC_V),
                                                     "ACCENT_DB_AT": {q_: 1.0 for q_ in qs_}}}
                                     for n_, (s_, qs_) in _MARC47.items()})
_T47 = tuple(_PPC47) + ("Vc stroke B",) + tuple(_PP747) + tuple(_MARC47)
PASS2_TRACKS = tuple(PASS2_TRACKS) + _T47
TEST_TRACKS = tuple(TEST_TRACKS) + _T47
# critic A #6d: the bar-58 top note's +0.02 s (leg_leads.json Violins II 232.0) was absorbed by the 0.75 cap behind the
# 231.5 eighth (realised 0.211 s, as before): a listed cap of 0.82 there realises 0.231 s (+0.02)
LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{"Violins II": [(231.9, 232.1, 0.82, "listed")] + LEG_CAP_FRAC.get("Violins II", [])})
# critic A #6a: Violas 78 (bar 20): roles.json [77.5, 82.75, 6.5, 0.5] ramped in over 77.0-77.5, on the last half beat of
# the F4 before the A-flat4 join (pre-join swell +7.4 dB over the A-flat4's body). A role row's start ramp is always 0.5
# qn (its 4th value is the end ramp), so A's [77.75, 82.75, 6.5, 0.1] would still ramp from 77.25: the row is removed
# and the lift is an exact shape from the A-flat4's moved onset (77.67), with the old 0.5 qn end ramp
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [[(77.65, 0.0), (77.75, 6.5), (82.25, 6.5), (82.75, 0.0)]]
# ---- the c47 tests decided (test stems against the main stems on the same notes; cycles/c47/CHANGES.md) ----
# C #1 soft cap: no pp cap adopted on Violins II, Violas, Violoncellos and Double basses (mix.json); the test stems replace
# the main stems from qn 695.8 (per bar before the coda 1-6 dB round-robin / test-stroke differences). The coda-only
# pp700 instances are not used (the basses' one stepped 8-11 dB at four final-chord re-bows).
# A #4 / C #3 stroke rows: variant B "Sus Marc LITE" kept on celli 84 and 448 (time with the band 6 dB under the body
# 64 / 124 -> 0 ms, pcX -8 / +52 -> -32 / -4 ms; the c46 front and dip criteria fail on the main strokes too and are no
# worse); variant A ("Stac Leg BC + Slur + Port MAX") swelled in longer on 4 of 6 celli strokes and sped Violas 372 to
# -195 ms: not adopted; B on 152 (0 -> 94 ms under), 156 and 456 (pcX -73 ms: the lead is too long for the row) not kept.
# C #2 brass Marc Sus LITE at v45-75 (MANUAL-GAPS #1): perceived attack +100..+365 ms late, 2-5 kHz front no brighter
# (median -15.1 vs -13.1 dB), step under the plain note: not adopted
ART_SPANS = dict(ART_SPANS, **{"Violoncellos": ART_SPANS.get("Violoncellos", []) + _spans47([84.0, 448.0], _STR_B)})
for n_ in _T47:
    ALIAS_TRACKS.pop(n_)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _T47)
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ not in _T47)

# ---------- c48 (series 2), critics A / B / C on the c47 render ----------
# (json tables: cycles/c48/actor_scripts/apply48.py: B #1-#4 roles / note trims / pitch-trim skips, C #1 per-note leads,
# C #3 Violins I 472.5 / 474.5 entry leads, A #2 celli 156 / 456 stroke leads; mix.json: A #3 basses pp cap 600 ms)
# critic A #1: the bars 85-96 fugato's accented subject heads sat level with or under the staccato eighths after them
# (accent's first 0.3 s minus the loudest following staccato's first 0.14 s: Vc 337 -0.1, Vc 342 -4.9, Vla 349 -2.6,
# Vla 354 -4.1, Bn1 stac 349 -3.4, Vln I 373 -0.2 dB): lifts on 342 / 354 and cuts on the eighths (simulated: +2.4 /
# +2.2 / +1.4 / +1.6 / +2.0 / +2.3 dB; 2-5 kHz fronts unchanged)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(338.45, 0.0), (338.48, -2.5), (339.92, -2.5), (339.95, 0.0)],
    [(341.97, 0.0), (342.0, 4.5), (343.40, 4.5), (343.44, 0.0)],
    [(343.44, 0.0), (343.47, -3.5), (347.6, -3.5), (347.72, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [
    [(350.38, 0.0), (350.42, -4.5), (351.65, -4.5), (351.75, 0.0)],
    [(353.97, 0.0), (354.0, 3.0), (355.36, 3.0), (355.40, 0.0)],
    [(355.40, 0.0), (355.42, -3.0), (355.86, -3.0), (355.88, 0.0)]]
ALIAS_TRACKS["Bassoon 1 stac"]["tables"]["LEVEL_SHAPES"] = ALIAS_TRACKS["Bassoon 1 stac"]["tables"].get("LEVEL_SHAPES", []) + [
    [(348.97, 0.0), (349.0, 2.5), (350.36, 2.5), (350.40, 0.0)],
    [(350.40, 0.0), (350.44, -3.0), (351.9, -3.0), (351.95, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(374.38, 0.0), (374.42, -2.5), (375.9, -2.5), (375.95, 0.0)]]
# critic C #2: coda bars 167-170, the basses' f C2 eighth pedal (Sus MAX, identical data per note) alternates its two
# bow-direction samples (HO 2021 p.91) with the strong one on the off-beats (off-beats -38 ms and 2.9 dB louder,
# downbeats +58 ms after a deeper dip, in c46 and c47): +3 dB on each downbeat, -1.5 dB on each off-beat (simulated:
# downbeat pcX +58 -> +13 ms, off-beat excess 2.9 -> 1.7 dB). The off-beat lead (C's inferred -0.03 s) is not made
for q_ in range(664, 676):
    LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [
        [(q_ - 0.14, 0.0), (q_ - 0.06, 3.0), (q_ + 0.15, 3.0), (q_ + 0.25, 0.0)],
        [(q_ + 0.5, 0.0), (q_ + 0.53, -1.5), (q_ + 0.8, -1.5), (q_ + 0.9, 0.0)]]
# critic C #3: Cello solo 688 (G4 -> F4) sags 4 dB right after an on-time pitch change (pcX +69 ms): a fill (simulated:
# dip 4.0 -> 3.0 dB, peak +0.3 dB over the louder body, pcX +15 ms); the lead stays
ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] = ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"] + [
    [(687.99, 0.0), (688.03, 3.0), (688.17, 3.0), (688.27, 1.5), (688.34, 0.0)]]
# critic A #2 (S1 / S2): celli 156 / 456 strokes swell in for 222 / 364 ms on Sus MAX; Sus Marc LITE cured 84 / 448 in
# c47 and failed on these only by a 40-70 ms longer lead (retongue_leads.json 0.09 / 0.12 -> 0.02 / 0.05)
ART_SPANS = dict(ART_SPANS, **{"Violoncellos": ART_SPANS["Violoncellos"] + _spans47([156.0, 456.0], _STR_B)})
# critic C #1 (b): family entry leads that are off in both renders (pcX against the beat median): Horn 3 entries -20 / -20
# ms (loud and mid values 0.05 -> 0.03; its 317 row in entry_leads.json allows for it), Contrabassoon -27 / -20 ms
ENTRY_LEAD_S = dict(ENTRY_LEAD_S, **{"Horn 3": (0.06, 0.03, 0.03), "Contrabassoon": (0.04, 0.04)})
# critic A #4 (LEG_LEAD_S +0.015 on Violins I / II / Violas) is not made: C #1's per-note table moves the same joins one by
# one (Violins I 16, Violins II 6, Violas 12 legato rows), and a family shift on top would count the late median twice
# critic A #2 (pass-2 test): Violas 372 on Sus Marc LITE with a 0.04 s per-onset lead (variant A at the old 0.12 sped it
# to -195 ms in c47); whole-piece windows (the c46 / c47 lesson: the alias then plays the source's data everywhere but
# 372, and a passing stem can replace the main stem); pass criteria: under <= 90 ms, pcX within +-40 ms of the violas' legato median, front <= -3 dB
ALIAS_TRACKS["Vla stroke B"] = {"source": "Violas", "windows": tw_own("Violas", 0.0, 730.0),
                                "tables": {"ART_SPANS": _spans47([372.0], _STR_B), "RETONGUE_LEADS": {"372.0": 0.04}},
                                "globals": _STROKE_GL}
_T48 = ("Vla stroke B",)
PASS2_TRACKS = tuple(PASS2_TRACKS) + _T48
TEST_TRACKS = tuple(TEST_TRACKS) + _T48
# critic C #4: Clarinet 1 706 (coda espr., C5 -> B4) sags 4-5 dB at an on-time change (crossover +7 ms, pcX +99 ms):
# fitted on the c47 stem (cycles/c48/actor_scripts/cl706_48.py): +2 dB (100 ms level dip 7.1 -> 5.1 dB against the C5,
# peak +1.0 dB over it; +3 dB reached C's +2 dB overshoot limit inside the printed diminuendo)
LEVEL_SHAPES_S["Clarinet 1"] = LEVEL_SHAPES_S.get("Clarinet 1", []) + [(706.0, [(-0.10, 0.0), (-0.05, 2.0), (0.40, 2.0), (0.55, 0.0)])]
# critic C #1 (c), coordinator: level fills for the swell notes (h10 on time, t50 80 ms or more late in c46 and c47, stem
# within 10 dB of the master) in place of more lead: 30 fills simulated on the c47 stems (cycles/c48/actor_scripts/
# swellfit48.py: 2-4 dB from the score onset, held 0.06-0.15 s, 0 before the next note; overshoot over the louder body at
# most +2 dB; t50 moved 36-200 ms earlier, h10 kept within 40 ms of the reference); rows in build/swell_fills48.json
for tn_, rows_ in json.load(open(f"{BUILD}/swell_fills48.json")).items():
    if not tn_.startswith("_"):
        LEVEL_SHAPES_S[tn_] = LEVEL_SHAPES_S.get(tn_, []) + [(float(q_), [tuple(p_) for p_ in ps_]) for q_, ps_ in rows_]
# level rows keyed to notes whose lead changed in c48 move with them by the realised change (c43's rule;
# cycles/c48/actor_scripts/near48.py lists them; early fills in apply48.py): the gap dips before Bassoon 1 136, Horn 2 47 /
# 232 and Horn 3 156, the Clarinet 1 422 accent cut, the Violas 136 / Violins I 60 portato shapes, the Oboe 1 579 join
# fill and the JOIN_NOTCH rows of Horn 2 249, Violas 182 / 650.5 and celli 416. Left in place: the basses' 332 sub. p
# notch (the new onset still falls inside it) and the body-level rows at Violins I 707 / Violins II 388
for t_, q0_, ds_ in [("Bassoon 1", 136.0, -0.035), ("Clarinet 1", 422.0, 0.061), ("Horn 2", 47.0, -0.045),
                     ("Horn 3", 156.0, -0.036), ("Violas", 136.0, 0.036), ("Violins I", 60.0, 0.08)]:
    _n_ = sum(1 for q_, _ in LEVEL_SHAPES_S[t_] if abs(q_ - q0_) < 0.01)
    assert _n_ >= 1, (t_, q0_)
    _c43_move_lss(t_, q0_, ds_)
for t_, old_, new_ in [("Horn 2", [(231.65, 0.0), (231.68, -4.0), (231.83, -4.0), (231.85, 0.0)],
                        [(231.7741, 0.0), (231.8041, -4.0), (231.9541, -4.0), (231.9741, 0.0)]),
                       ("Oboe 1", [(578.90, 0.0), (578.96, 4.0), (579.40, 4.0), (579.55, 0.0)],
                        [(578.9404, 0.0), (579.0004, 4.0), (579.4401, 4.0), (579.59, 0.0)])]:
    assert old_ in LEVEL_SHAPES[t_], (t_, old_)
    LEVEL_SHAPES[t_] = [new_ if s_ == old_ else s_ for s_ in LEVEL_SHAPES[t_]]
for t_, old_, new_ in [("Horn 2", (248.9115, 249.1215, -4.6), (248.8217, 249.0315, -4.6)),
                       ("Violas", (181.508, 181.938, -2.7), (181.5819, 182.0116, -2.7)),
                       ("Violas", (650.11, 650.2, -2.5), (650.1733, 650.2633, -2.5)),
                       ("Violoncellos", (415.511, 415.85, -5.5), (415.5908, 415.9298, -5.5))]:
    assert old_ in JOIN_NOTCH[t_], (t_, old_)
    JOIN_NOTCH[t_] = [new_ if r_ == old_ else r_ for r_ in JOIN_NOTCH[t_]]
# critic B #2: coda bars 175.75-177, Clarinet 1's pp espr. solo 4-11.5 dB over every other pp part (the c07 lift went
# stale): -2 dB from the C5's onset (0.03 qn ramp from the pickup's breakpoint at 700.0) to the B4's first half beat (B simulated -2 dB over 699-706.5: still the top
# voice in every beat). A shape, not the removal of the roles.json [699, 712, 2] row: that row also carries the ramp on
# the 699 pickup, which without it played up to 4.4 dB louder, and the B4's diminuendo after 706.5
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(700.0, 0.0), (700.03, -2.0), (706.4, -2.0), (706.6, 0.0)]]
# ---- c48 second-pass tests added after the main render (TEST_TRACKS) ----
# critic A #3 follow-up: with 600 ms at pp the basses' bars 1-174 chord changes pass the -12 dB old-pitch-re-body check but
# 5 fail -12 dB re the new note (176 / 180 / 224 / 230 -9.8..-11.7; 182 +4.7 and 17.95 +2.0, both already over -12 at
# 350 ms); the coda passes (5 of 5). A's fallback: 450 ms at pp, whole-piece windows ("Cb pp450 test", mix.json)
# critic A #2 follow-up: celli 156 on Sus Marc LITE with the 0.02 s lead lost its swell (under 222 -> 46 ms) but is
# perceived +77 ms late (456 at 0.05 s: under 84 ms, pcX +2, passes): 0.055 s (interpolated between c47's variant B at
# 0.09 extra, -73 ms, and this render's 0.02, +77 ms)
ALIAS_TRACKS["Cb pp450 test"] = {"source": "Double basses", "windows": tw_own("Double basses", 0.0, 730.0)}
ALIAS_TRACKS["Vc stroke 156 test"] = {"source": "Violoncellos", "windows": tw_own("Violoncellos", 0.0, 730.0),
                                      "tables": {"RETONGUE_LEADS": {"156.0": 0.055}}}
_T48B = ("Cb pp450 test", "Vc stroke 156 test")
PASS2_TRACKS = tuple(PASS2_TRACKS) + _T48B
TEST_TRACKS = tuple(TEST_TRACKS) + _T48B
# ---- the c48 tests decided (test stems against the main stems on the same notes; cycles/c48/CHANGES.md) ----
# A #2 Violas 372 on Sus Marc LITE at 0.04 s: worse (time 6 dB under the body 162 -> 338 ms, pcX +88 -> +138 ms, no dip
# before it): Sus MAX kept. Celli 156 at 0.055 s: under 134 ms, pcX +61 (the main render's 0.02 s: 46 ms, +77): the main
# render's 0.02 s kept. A #3 basses 450 ms at pp: bars 1-174 pp chord changes failing -12 dB 7 -> 4 (3 of them already
# failed at 350 ms), but the final release to -20 dB 0.35 -> 0.30 s: the 600 ms cap stays in mix.json; the c48 audio
# takes the 450 ms test stem up to qn 695.8 (swap48.py)
for n_ in _T48 + _T48B:
    ALIAS_TRACKS.pop(n_)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _T48 + _T48B)
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ not in _T48 + _T48B)

# ---------- c49 (series 2), critics A / B / C on the c48 render ----------
# (json tables: cycles/c49/actor_scripts/apply49.py: A #2 celli 156 retongue lead, B #4 roles; mix.json: C #2 / C #3 and
# the test aliases' entries, reverb width (C #1, decided on the hall test in cycles/c49/halltest))
# coordinator / critics A #5, B, C: the basses' pp cap stays 600 ms everywhere (mix.json, as rendered from c49 on): on
# the twelve bars 1-174 pp chord changes the old pitch at +0.35 s sits a median 23.9 dB under the master in its own band
# at 600 ms (27.1 at 450 ms; cycles/c49/actor_scripts/cbcap49.py), and the final release needs 600 ms
# critic A #1 (S1, S2; HO 2021 p.91 bow direction, p.145 round robins kept per note): coda bars 167-169, the basses' f C2
# eighths (Sus MAX) play the strong bow-direction sample on every off-beat (off-beat dip 2.2 / 1.6 dB stem / master,
# pcX -41 ms; level shapes cannot move it, A simulated four variants). A windowed alias resets the round-robin order in
# its pre-roll, so its first C2 plays the first sample of the cycle. The basses play without a rest from 619.9 to 678.9,
# so each test window runs from a rest to a rest (the main track's notes outside it keep their treatment; a window
# starting at 664 or 660 changed the main's 660 note, vel 105 -> 53, and its 676 lead when the main rested there).
# "Cb pedal A" (613.5-680: C2s at 616, 660, 664: 664 plays the first sample) and "Cb pedal B" (618-680: C2s at 660,
# 664: 664 plays the second). The c48 alternation and +3 / -1.5 dB shapes are dropped in both (fitted on the main
# track's samples); STR_REP_DETACH and the +1.5 dB hold row are inherited. Tests in this render (the main track plays
# everything, so both aliases duplicate its data); the winner is spliced into the basses stem over the pedal
_CBP_DROP = [663.97] + [q_ - 0.14 for q_ in range(664, 676)] + [q_ + 0.5 for q_ in range(664, 676)]
ALIAS_TRACKS["Cb pedal A"] = {"source": "Double basses", "windows": [(613.5, 680.0)], "drop": {"LEVEL_SHAPES": _CBP_DROP}}
ALIAS_TRACKS["Cb pedal B"] = {"source": "Double basses", "windows": [(618.0, 680.0)], "drop": {"LEVEL_SHAPES": _CBP_DROP}}
# (after the c49 pass 2: A and B rendered identically, off-beats strong in both; in both windows the 616 C2 is not on Sus
# MAX, so 664 is the second Sus MAX C2 in each, the same parity as the main track's 62nd: a per-note, per-row round-robin
# count gives the same order in all three. "Cb pedal C" (window 664-676, 664 its first Sus MAX C2) is the opposite parity,
# rendered on its own over qn 655-681 in the same pass-2 session)
ALIAS_TRACKS["Cb pedal C"] = {"source": "Double basses", "windows": [(664.0, 676.0)], "drop": {"LEVEL_SHAPES": _CBP_DROP}}
_T49 = ("Cb pedal A", "Cb pedal B", "Cb pedal C")
# critic A #2 (S2): celli 156 on Sus Marc LITE is perceived later than c47's Sus MAX (pcX +77 against +32 ms; t50 +160
# against +84): back to Sus MAX with c47's retongue lead 0.09 (retongue_leads.json); 456 stays on Sus Marc LITE
_VC156 = _spans47([156.0], _STR_B)[0]
ART_SPANS = dict(ART_SPANS, **{"Violoncellos": [s_ for s_ in ART_SPANS["Violoncellos"] if s_ != _VC156]})
# critic B #2 (celli bar-40 body -8 -> -5 dB) is not made: B measured it on the Sus Marc LITE body; on Sus MAX (A #2's
# revert) the c47 render, with the same -8 dB cut, put the celli at -0.5 / -1.9 / +3.4 / +3.7 / -4.0 / +3.4 dB K over the
# loudest other stem per half qn 157-159.5, c47's planned margin; +3 dB there gives -0.5 / +1.1 / +6.4 / +6.7 / -1.0 /
# +6.4, the loudest stem by 6-7 dB again (the c47 B #4 fault; cycles/c49/actor_scripts/vc156_49.py)
# critic A #3: fugato bar 90, the violas' quarter staccato 358 (moved onset 357.916) as loud as the accented head 354:
# -2 dB from its moved onset (A's 357.95 start would leave the attack's first 16 ms untouched)
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(357.88, 0.0), (357.91, -2.0), (358.6, -2.0), (358.7, 0.0)]]
# critic B #1: coda bar 176, Clarinet 1's held C5 swells twice in its first beat (sample bloom at +0.45 s under the c47
# fill's falling edge; peak 5.8 dB over its own body): two cuts (B simulated: peak 5.8 -> 2.6 dB, no new dip)
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES["Clarinet 1"] + [[(700.02, 0.0), (700.06, -3.0), (700.24, -3.0), (700.28, 0.0),
                                                            (700.38, 0.0), (700.44, -4.5), (700.64, -4.5), (700.72, 0.0)]]
# critic B #3: fugato bars 94 / 96, the last subject entry (Violins I + Flute 1, f) starts level with the Violins II
# countersubject (subject over countersubject at 372.5 / 373.0 / 380.5: -0.4 / +0.3 / -1.5 dB): -3 dB on the
# countersubject under the subject's head and its last staccato (B simulated +2.6 / +3.3 / +1.5). The second row ends
# before the 381 ff note's moved onset (380.625), not at B's 380.95, so the stretto entry keeps its attack
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(371.9, 0.0), (372.05, -3.0), (373.6, -3.0), (374.0, 0.0)],
                                                           [(380.2, 0.0), (380.24, -3.0), (380.58, -3.0), (380.62, 0.0)]]
# critic B #5: bars 147-148, the cor anglais's first p dolce answer loses its pickup (peak 11.2 dB under the tune): +3 dB
# as a step on the 586.5 pickup from its moved onset (586.396), out before the next note (586.905)
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [[(586.36, 0.0), (586.39, 3.0), (586.85, 3.0), (586.9, 0.0)]]
# critic C #2 (pass-2 tests): the violas fall 5-13 dB faster than the other strings at every tutti stop (rt_gain_db -6
# removed their trails' room). "Vla send35 test": send 0.25 -> 0.35 (C's fix); "Vla rt3 test": rt_gain_db -3 with send
# 0.30 (C's fallback). Whole-piece windows (tw_own), so a passing stem can replace the main stem (alias_check.py)
ALIAS_TRACKS["Vla send35 test"] = {"source": "Violas", "windows": tw_own("Violas", 0.0, 730.0)}
ALIAS_TRACKS["Vla rt3 test"] = {"source": "Violas", "windows": tw_own("Violas", 0.0, 730.0)}
_T49 = _T49 + ("Vla send35 test", "Vla rt3 test")
# coordinator (C #1, EastWest's own HO REAPER template: strings and brass with Close 4-10 dB under Main, Close panned to
# the seat, Main at full width and never re-panned): pass-2 variant on the four upper string sections and the four
# loudest brass parts in 250 Hz-5 kHz (48% of the strings' and brass's share there in c48): Main at full width
# (width_by_mic Main 2.0 = pan -1 / +1 whatever the seat), Close 0.5 (-6 dB) under Main 1.0 at the track's seat and width.
# Judged on the master with C's correlation and side/mid criteria by replacing these eight stems (the hall is unchanged)
_MW49 = {"Vln I mainw test": "Violins I", "Vln II mainw test": "Violins II", "Vla mainw test": "Violas",
         "Vc mainw test": "Violoncellos", "Tbn1 mainw test": "Trombone 1", "Hn a2 mainw test": "Horns a2",
         "Tpt1 mainw test": "Trumpet 1", "Hn3 mainw test": "Horn 3"}
ALIAS_TRACKS = dict(ALIAS_TRACKS, **{n_: {"source": s_, "windows": tw_own(s_, 0.0, 730.0)} for n_, s_ in _MW49.items()})
_T49 = _T49 + tuple(_MW49)
PASS2_TRACKS = tuple(PASS2_TRACKS) + _T49
TEST_TRACKS = tuple(TEST_TRACKS) + _T49
# ---- the c49 tests decided (pass-2 test stems against the main stems; cycles/c49/CHANGES.md) ----
# A #1 coda pedal: "Cb pedal A" (window 613.5-680), "Cb pedal B" (618-680) and "Cb pedal C" (664-676, 664 its first Sus
# MAX C2) all play the strong stroke on the off-beats, exactly as the main track (downbeat peak 1.4 dB under the
# off-beats, downbeat pcX +57 ms without the c48 shapes): the bow-direction phase does not follow the number of earlier
# notes in the instance, so a windowed alias cannot move it; not adopted (the main track keeps the c48 shapes).
# C #2 violas: send 0.35 closes the +0.6 s stop gap by 0.8-2.9 dB (still 4.3-8.5 dB faster than the other strings),
# trail gain -3 / send 0.30 by 1.1-2.2 dB with the figures' old pitch -8.4 -> -7.4 dB: neither meets C's criteria.
# Coordinator's Main-width variant (EW template): eight stems' 250 Hz-5 kHz correlation 0.45-0.82 -> 0.06-0.40; the master
# with them replaced 250 Hz-5 kHz 0.638 -> 0.457, < 250 Hz 0.572 -> 0.332, side/mid -6.3 -> -4.0 dB (references 0.47-0.56,
# 0.54-0.62, -4.7..-5.4) and seats 1.4-3.4 dB nearer the centre: past the references, not adopted (c50 candidate).
for n_ in _T49:
    ALIAS_TRACKS.pop(n_)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _T49)
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ not in _T49)
# ---------- c49 stem fix (level only, measured on the c49 render) ----------
# critic C #3 follow-up (B's lens): with the coda bell the trumpet / horn melody sat level with the violins on the held
# B4's last beats (melody minus violins K at 677.5 / 678 / 678.5: +0.4 / -0.1 / +0.1 dB; c48 +1.8 / +1.5 / +1.1): +1.5 dB on
# the a2 trumpets over the held note after its attack (the bell stays: a2 2-5 kHz re 0.5-2 kHz -5.6 -> -7.9 dB)
ALIAS_TRACKS["Trumpets a2"]["tables"]["LEVEL_SHAPES"] = ALIAS_TRACKS["Trumpets a2"]["tables"].get("LEVEL_SHAPES", []) + [
    [(676.4, 0.0), (676.6, 1.5), (679.0, 1.5), (679.2, 0.0)]]
# ---------- c50 (series 2): the EastWest template mix (build/mix.json from cycles/c50/actor_scripts/apply50.py) ----------
# The performance data of the main tracks is unchanged (parts.json byte-identical outside the test alias below); the MIDI
# rules of EW-TEMPLATE-PLAN sections 5-10 are c51's.
# critic A #3 (coda bars 167-169, HO 2021 p.91-92, patch read): the basses' f C2 eighth pedal plays the strong bow on the
# off-beats whatever the instance's history (c49: three windowed aliases, same phase). "Marc Sus LITE" (Basses KS Master,
# key 73, loaded by default) adds a decaying Marc Shrt attack over pp / ff sustains that fade in over 368 ms, so the
# twelve downbeats get a defined front whatever bow the sustain plays. Pass-2 test alias over c49's rest-to-rest window
# 613.5-680, the c48 pedal level shapes dropped (as in c49's aliases), velocity in the mp attack zone (1-60)
_CBM_SPANS = [{"from": float(q_), "to": float(q_) + 0.01, "art": "Marc Sus LITE", "vel_by_cc": [(88, 45), (114, 55)]}
              for q_ in range(664, 676)]
ALIAS_TRACKS["Cb pedal M"] = {"source": "Double basses", "windows": [(613.5, 680.0)], "drop": {"LEVEL_SHAPES": _CBP_DROP},
                              "tables": {"ART_SPANS": _CBM_SPANS}}
_T50 = ("Cb pedal M",)
PASS2_TRACKS = tuple(PASS2_TRACKS) + _T50
TEST_TRACKS = tuple(TEST_TRACKS) + _T50
# ---------- c50 stem fix (level only, measured on the c50 main render; cycles/c50/CHANGES.md) ----------
# critic B check "Horns a2 over the loudest other, bars 41-42": -1.7 dB after the template switch (c49 +0.8, pass 0 or
# more; B's simulation -0.8 and its advice "+1 dB there if the render confirms it"): +2 dB over the a2 notes 163-165
LEVEL_SHAPES["Horns a2"] = LEVEL_SHAPES["Horns a2"] + [[(162.75, 0.0), (162.85, 2.0), (165.6, 2.0), (165.8, 0.0)]]
# ---- the c50 test decided (pass-2 test stem against the main basses stem; cycles/c50/CHANGES.md) ----
# critic A #3 "Cb pedal M" (Marc Sus LITE at v45 on the twelve downbeats 664-675): fails A's criteria. Downbeat minus the
# neighbouring off-beat front (40-300 Hz, first 80 ms) -3.5..-9.4 dB, 0 of 12 at +0.5 dB or more (main track -2.0..-7.5,
# 0 of 12); downbeat pcX +58 ms (main +16 with the c48 shapes); peak in the first 0.25 s +0.8 dB over the off-beats (main
# -0.6). The mp attack zone speaks too late under the 368 ms sustain fade-in; not adopted (c51 may retry v61-90 with a lead)
for n_ in _T50:
    ALIAS_TRACKS.pop(n_)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _T50)
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ not in _T50)

# ---------- c51 (series 2): the MIDI rules of EW-TEMPLATE-PLAN sections 5-8 and 10 (critics A, B, C of cycles/c51) ----------
# coordinator item 1, critic A #1 (S1; plan section 8): string repeats separated by a gap instead of 0.02-0.04 qn
# (stem dips 1.4-5.2 dB, master 1.4-4.5): a stroke followed by a same-pitch stroke ends max(0.06, min(0.08, 0.35 x slot))
# s before the next onset at mp or louder (eighths at 126: 158 ms of 238); STR_REP_NEW_BOW gap 0.06 -> 0.08 s
REP_SPLIT = dict(REP_SPLIT, gap_s=0.08, frac=0.35, gap_min_s=0.06, gap_min_cc=DYN["mp"])
STR_REP_NEW_BOW = dict(STR_REP_NEW_BOW, gap_s=0.08)
# the basses' detach dip now falls inside the gap: -5 -> -3 dB on the ff pedals (A #1; the coda pedal 664-676 too, for the
# same reason)
_dd51 = {(104.0, 124.25), (520.0, 536.25), (556.0, 568.0), (664.0, 676.0)}
STR_REP_DETACH = dict(STR_REP_DETACH, at={**STR_REP_DETACH["at"], "Double basses": [
    (sp_[0], sp_[1], {"dip_db": -3.0}) if (len(sp_) == 2 and (sp_[0], sp_[1]) in _dd51) else sp_
    for sp_ in STR_REP_DETACH["at"]["Double basses"]]})
# critic B #5: the gaps cost -0.3..-0.65 dB per slot on those runs: level returned over the spans
_lv51 = lambda a_, b_, d_: [(a_ - 0.1, 0.0), (a_, d_), (b_, d_), (b_ + 0.1, 0.0)]
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [
    _lv51(104.0, 124.0, 0.5), _lv51(324.0, 328.0, 0.5), _lv51(520.0, 536.0, 0.5), _lv51(554.0, 568.0, 0.5), _lv51(664.0, 676.0, 0.5)]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [_lv51(86.0, 100.0, 0.4), _lv51(440.0, 468.0, 0.4), _lv51(552.0, 568.0, 0.4)]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [_lv51(86.0, 100.0, 0.3), _lv51(536.0, 548.0, 0.3)]
# coordinator item 2, critics A #2 / B #2: the celli measured tremolo (bars 117-121) at 55 % of its slot (with the
# Violoncellos Stac-row release cap 120 ms in mix.json, group words "Stac" / "Hrd"), no beat offsets there, +0.5 dB; the
# string short rows with CC11 parked at 120 and the level returned in the volume envelope (B's level-safe form; the
# velocities stay in the zones they play now); metric weight +1.5 / 0 / -1 dB in the envelope on the celli 16ths
# 516-520 and the fugato staccatos
MEAS_TREM = dict(MEAS_TREM, len_frac=0.55)
SHORT_CC11_PARK = {"families": ("string",), "rows": ("Stac", "Staccatissimo", "Spiccato"), "cc": 120,
                   "gg_amp": [(0, 0.0), (8, 0.1875), (9, 0.2), (10, 0.2), (69, 0.5), (127, 0.99152)], "fade_s": 0.12,
                   "beat_db": {"beat": 1.5, "and": 0.0, "sixteenth": -1.0},
                   "beat_spans": {"Violoncellos": [(516.0, 520.0), (336.0, 348.0)], "Violas": [(336.0, 360.0)],
                                  "Violins II": [(336.0, 372.0)], "Violins I": [(336.0, 384.0)]}}
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [_lv51(464.0, 484.0, 0.5), _lv51(512.0, 520.0, 0.5)]
# coordinator item 3, critic C #1 (plan sections 6-8, 10): phrase shapes, the finale's rule with C c50's values and C
# c51's notes (offset in CC1 and CC11 on the CC1_DYN_TRACKS, phrases on score onsets, string phrases broken at rests of
# 0.5 qn and at printed dynamics, strings start at 0)
PHRASE_SHAPE = {"families": ("string", "wind", "brass"), "min_s": 2.0, "gap_s": 0.25,
                "start": {"string": 0, "wind": -8, "brass": -8}, "rise": [(0.4, 2), (0.8, 6)], "peak": (10, 0.44),
                "pre_end": (1.0, 4), "end": -12,
                "scale": {"ppp": 0.6, "pp": 0.8, "p": 1.0, "mp": 1.0, "mf": 1.0, "f": 0.6, "ff": 0.35, "fff": 0.2},
                "floor": 8, "cap": {"brass": 108}, "cc1_floor": 36, "hp_fade_s": 0.25, "step_s": 0.1,
                "both_lanes": True, "str_rest_qn": 0.5, "str_break_marks": True, "family_gain": {"wind": 1.4},
                "types": {"build_cc": 10, "drive": (6, (10, 0.15), -10), "drive_min_bpm": 105,
                          "lyric_spans": [(0, 56), (176, 272), (288, 332), (424, 448), (488, 520), (576, 628), (680, 728)]}}
# coordinator item 4, critic C #4 (plan section 9): hairpin curves; long builds into f or louder and the timpani rolls
# (B #1a: the curve lifted the 492-500 roll over the Horn 1 solo) stay linear
HP_CURVE = {"cresc": (0.4, 0.65), "decresc_last": 0.35, "decresc_held": (0.6, 0.2), "min_qn": 1.0,
            "build_min_qn": 4.0, "build_to": "f", "skip_families": ("timp",)}
# coordinator item 5, critic C c51 #3: bar 121 grows 1.1 dB into the first fff: back off at the crescendo's start, the
# arrival left where it is
for tn_ in ("Violins I", "Violins II", "Violas", "Violoncellos", "Double basses", "Flute 1", "Flute 2", "Oboe 1", "Oboe 2",
            "Clarinet 1", "Clarinet 2", "Bass clarinet", "Bassoon 1", "Bassoon 2"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(479.75, 0.0), (480.0, -1.5), (483.9, 1.5), (484.4, 0.0)]]
for tn_ in ("Horn 1", "Horn 2", "Horn 3", "Horn 4", "Trombone 1", "Trombone 2", "Bass trombone", "Tuba", "Timpani"):
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(479.75, 0.0), (480.0, -1.5), (483.9, 0.5), (484.4, 0.0)]]
# coordinator item 7, critic B #1b: soft timpani rolls (mix.json loud_eq low shelf 160 Hz -3 dB on these spans), +1 dB
for a_, b_ in ((0.0, 58.5), (154.0, 174.5), (242.0, 252.5), (502.0, 514.5), (568.0, 586.5), (716.0, 728.0)):
    LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(max(0.0, a_ - 0.1), 0.0), (a_, 1.0), (b_, 1.0), (b_ + 0.1, 0.0)]]
# coordinator item 8, critic A #3: the Bass clarinet's held G2 (480-491.9) dropped 3.5-4.3 dB at the fff arrival (the
# crescendo's dB gain released on a note held across it): held to the next onset
LEVEL_SHAPES["Bass clarinet"] = LEVEL_SHAPES["Bass clarinet"] + [
    [(483.7, 0.0), (483.75, 3.5), (483.875, 4.2), (483.95, 5.1), (484.02, 3.5), (491.85, 3.5), (491.94, 0.0)]]
# ---- c51 pass-2 tests (coordinator item 12) ----
# critic A #5: the coda pedal (664-675.5) on Marc Sus LITE in the f attack zone (61-102) with a lead: v75 / 0.04 s, v92 /
# 0.03 s (c50's v45 "Cb pedal M" spoke +58 ms late, fronts 3.5-9.4 dB under the off-beats)
_CBF = lambda vel_: [{"from": float(q_), "to": float(q_) + 0.01, "art": "Marc Sus LITE", "vel_by_cc": [(88, vel_), (114, vel_ + 10)]}
                     for q_ in range(664, 676)]
for nm_, vel_, ld_ in (("Cb pedal F1", 75, 0.04), ("Cb pedal F2", 92, 0.03)):
    ALIAS_TRACKS[nm_] = {"source": "Double basses", "windows": [(613.5, 680.0)], "drop": {"LEVEL_SHAPES": _CBP_DROP},
                         "tables": {"ART_SPANS": _CBF(vel_),
                                    "RETONGUE_LEADS": {float(q_): ld_ for q_ in range(664, 676)}}}
# critic A #6 (plan section 5): the template's CC1 macro emulated (CC1 lane = CC11 lane) on the celli, p 136 to the end of
# the mf dolce tune (rest to rest)
ALIAS_TRACKS["Vc macro"] = {"source": "Violoncellos", "windows": [(135.0, 219.3)],
                            "globals": {"CC1_FROM_CC11": {"Violoncellos": None}}}
_T51 = ("Cb pedal F1", "Cb pedal F2", "Vc macro")
PASS2_TRACKS = tuple(PASS2_TRACKS) + _T51
TEST_TRACKS = tuple(TEST_TRACKS) + _T51
# ---- c51 range test (cycles/c51/rangetest/results1.txt, levels1.txt; main project, before the full render) ----
# Lento / second theme: lyric winds rose +1.9 dB by 0.8 s (pass 3) and tapered +2.3 / -0.1 dB (pass 3), brass +3.5..3.8 /
# +6.4..7.6 (pass): the wind offsets x1.4 (C c51: winds' CC11 gives 0.21 dB per unit, brass 0.28-0.30)
# celli measured tremolo (464-484) at 55 % with the 120 ms cap: per-bar level -3.9..-4.5 dB (B predicted -0.6; the strokes
# end before their 90-120 ms attack peak), peak-to-trough dip 7.5 -> 11.4 dB on the stem: +3.7 dB more over the span
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [_lv51(464.0, 484.0, 3.7)]
# ---------- c52 (series 2, third round): critics A, B, C of cycles/c52 on the c51 render; coordinator's decisions ----------
# c51's pass-2 tests are decided (cycles/c51/CHANGES.md): their aliases leave parts.json (the pass-2 project lost them in c51)
for nm_ in ("Cb pedal F1", "Cb pedal F2", "Vc macro"):
    ALIAS_TRACKS.pop(nm_, None)
PASS2_TRACKS = tuple(t_ for t_ in PASS2_TRACKS if t_ not in _T51)
TEST_TRACKS = tuple(t_ for t_ in TEST_TRACKS if t_ not in _T51)
# coordinator 2, critic B #1 / C #4: long diminuendi (over 4 qn: bars 3, 21, 66-67, 74, 123-125, 162-165) linear again (c51
# held 488-500 at f to its last beat: Horn 1's bar-125 "mp espr." entry 6.7 dB under Violins I); the shorter ones reach
# only 20 % of their fall at the last inner onset (C: string / brass diminuendi still fell early, 0.40 / 0.36 at 50 %)
HP_CURVE = dict(HP_CURVE, decresc_max_qn=4.0, decresc_last=0.20)
# coordinator 3, critic C #1: hairpins under 4 qn ride on the phrase arch instead of fading it out (the dolce theme's
# one-bar < hairpins started 7-10 units under the line: Horn 1's six crescendos ended a median 2.6 dB under their start);
# coordinator 5, critic C #2 (finale item 3): no positive phrase offset from a subito or a printed drop of 6 CC or more to
# the next hairpin (Bassoon 2 / Horn 4 sat 5 dB over c50 in the bar-62 p); the guard ("subito_only") is checked below
PHRASE_SHAPE = dict(PHRASE_SHAPE, hp_fade_min_qn=4.0, types=dict(PHRASE_SHAPE["types"], drop={"cc": 6}))
# the guard (C #2): with every printed drop of 6 CC the rule made 283 spans on 33 tracks, many of 16-64 qn (Flute 1 154-218,
# the trumpets 104-168, ...), which zeroes most of the arches it was meant to keep: restricted to the subito marks (bar 62
# qn 244 / 245 and bar 84 qn 332)
PHRASE_SHAPE["types"]["drop"]["subito_only"] = True
# and inside those short crescendos the offset holds its value at the hairpin start (lanes: celli 201 / 601 ended 1 unit
# under their level 0.35 s before, the arch falling faster than the printed rise)
PHRASE_SHAPE["hp_hold_cresc"] = True
# coordinator 4, critic C #3: the phrase offset that SWELL_CC_CAP clamps off CC11 goes into the volume envelope (kit
# LEARNINGS section 4 per-patch dB per CC unit), so the five capped low winds arch like the others
SWELL_CAP_TO_VOL_DB_PER_CC = {"Bassoon 1": 0.32, "Bassoon 2": 0.32, "Bass clarinet": 0.26, "Contrabassoon": 0.21,
                              "Clarinet 2": 0.20}
# coordinator 5, critic C #2 (bar 84, qn 332, Vc / Cb sub. p after the bar-83 ff): the basses' ff G1 ends at 331.45 and
# their -8 dB release cut is back to 0 by 331.80 (it held the new p note at -8 dB to 332.25 and lifted it 8 dB by 332.4: a
# 6.6 dB master re-swell 0.35 s after the beat); the celli / basses bloom shapes of 332.5-334.8 (fitted on series-1
# renders) are removed, the celli's release notch at 335.4-336.26 kept
NOTE_END_AT = dict(NOTE_END_AT, **{"Double basses": {**NOTE_END_AT.get("Double basses", {}), 330.0: 331.45}})
_cb84_old = [(331.45, 0.0), (331.6, -8.0), (332.25, -8.0), (332.4, 0.0)]
assert _cb84_old in LEVEL_SHAPES["Double basses"] and [(332.9, 0.0), (333.15, -3.5), (334.3, -3.5), (334.8, 0.0)] in LEVEL_SHAPES["Double basses"]
LEVEL_SHAPES["Double basses"] = [([(331.45, 0.0), (331.6, -8.0), (331.68, -8.0), (331.80, 0.0)] if s_ == _cb84_old else s_)
                                 for s_ in LEVEL_SHAPES["Double basses"]
                                 if s_ != [(332.9, 0.0), (333.15, -3.5), (334.3, -3.5), (334.8, 0.0)]]
_vc84_old = [(332.5, 0.0), (332.9, -3.0), (333.1, -5.0), (334.0, -5.0), (334.6, -2.0), (335.3, -2.0),
             (335.42, -3.0), (335.48, -9.0), (336.2, -9.0), (336.26, 0.0)]
assert _vc84_old in LEVEL_SHAPES["Violoncellos"]
LEVEL_SHAPES["Violoncellos"] = [([(335.3, 0.0), (335.42, -3.0), (335.48, -9.0), (336.2, -9.0), (336.26, 0.0)] if s_ == _vc84_old
                                 else s_) for s_ in LEVEL_SHAPES["Violoncellos"]]
# coordinator 6, critic A #2 (finale items 2 and 13): the sf at bar 41 (qn 160) and bar 20 (qn 78) start at the mark, so a
# led note's pull reads the spike; FP_VEL 96 for parity (Sus MAX ignores velocity); post-fader sf bumps on Violins I (78,
# 160) and the celli / basses (160), a cut over the Violins I G6 bloom at 160 (its sample rises 9 dB from +50 to +400 ms);
# the celli's sf a fresh Sus Marc LITE stroke (f attack zone) instead of a Leg BC join, with a 0.05 s re-attack lead
# (retongue_leads.json 160.0, as c48's 456 stroke). Starting values (inferred); refit on the render
FP_SPIKE_AT_MARK = True
FP_VEL = 96
POST_SHAPES_S = dict(POST_SHAPES_S)
for tn_, rows_ in (("Violoncellos", [(160.0, [(-0.13, 0.0), (-0.12, 5.0), (0.17, 5.0), (0.25, 0.0)])]),
                   ("Double basses", [(160.0, [(-0.13, 0.0), (-0.12, 5.0), (0.17, 5.0), (0.25, 0.0)])]),
                   ("Violins I", [(78.0, [(-0.07, 0.0), (-0.06, 3.0), (0.17, 3.0), (0.25, 0.0)]),
                                  (160.0, [(-0.07, 0.0), (-0.06, 2.0), (0.12, 2.0), (0.30, -3.0), (0.9, -4.0), (2.0, -2.0),
                                           (3.0, 0.0)])])):
    POST_SHAPES_S[tn_] = POST_SHAPES_S.get(tn_, []) + rows_
ART_SPANS = dict(ART_SPANS, **{"Violoncellos": ART_SPANS["Violoncellos"] + [
    {"from": 159.9, "to": 160.01, "art": "Sus Marc LITE", "vel_by_cc": [(0, 95), (127, 95)]}]})
# (tools, c52: a same-pitch repeat after an ART_SPANS stroke-row note is a STR_REP_NEW_BOW repeat, so 164 stays c51's stroke)
# coordinator 10: the harp's velocity cap (finale item 9; v621's harp tops out at v112, so no note changes)
HARP_VEL_MAX = 123
# coordinator 10, critic A #3 (finale item 8): a round-robin reset (CC16) at each same-pitch segment start of the basses'
# eighth pedals, the coda included (the C2 pedal played strong on the downbeats at 104 and 664, on the off-beats at 520)
RR_RESET_AT = dict(RR_RESET_AT, **{"Double basses": [104.0, 108.0, 112.0, 116.0, 120.0, 122.0, 520.0, 526.0, 528.0, 532.0,
                                                     556.0, 560.0, 562.0, 564.0, 664.0]})
# coordinator 10, critic A #4 (finale item 14): Flute 2 (FL2 KS Master, another player) landed 58-133 ms behind Flute 1 on
# their shared slurred joins: its legato lead 0.05 -> 0.11 s (joins only); the per-onset flute / oboe leads are in
# leg_leads.json, entry_leads.json and retongue_leads.json (cycles/c52/actor_scripts/apply52.py)
LEG_LEAD_S = dict(LEG_LEAD_S, **{"Flute 2": 0.11})
# coordinator 10, critic B #3a: bar 122's held fff arrival lost c50's per-note swell under the phrase shapes (0.5 dB under
# c50 in the mp3): +1 dB over 485-487.25 on every wind, brass and string track (not the tam-tam or timpani)
for tn_, st_, pa_, fam_, pn_ in TRACKS:
    if fam_ in ("wind", "brass", "string"):
        LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [[(484.25, 0.0), (485.0, 1.0), (487.25, 1.0), (488.0, 0.0)]]
# coordinator 10, critic B #3b: Clarinet 1's coda join at 700: the c47 hole fill (fitted when CC1 / CC11 were flat) made a
# +6.4 dB bump under the phrase shape's layer rise: removed; the pickup at 699 (1.7 dB under c50) lifted +2 dB
_cl700 = [(700.14, 0.0), (700.20, 5.0), (700.40, 5.0), (700.50, 0.0)]
assert _cl700 in LEVEL_SHAPES["Clarinet 1"]
LEVEL_SHAPES["Clarinet 1"] = [s_ for s_ in LEVEL_SHAPES["Clarinet 1"] if s_ != _cl700] + [
    [(698.88, 0.0), (698.93, 2.0), (699.4, 2.0), (699.8, 0.0)]]
# coordinator 10, critic B #6 (finale item 15): the 656-664 delivery ride row ended with its step inside the tutti
# crescendo 662-664.5: it ends at 662
_rt656 = [(656.0, 0.0), (656.5, 0.5), (663.5, 0.5), (664.0, 0.0)]
assert _rt656 in RIDE_TRIMS
RIDE_TRIMS = [([(656.0, 0.0), (656.5, 0.5), (661.5, 0.5), (662.0, 0.0)] if r_ == _rt656 else r_) for r_ in RIDE_TRIMS]
# coordinator 10, critic A #6 (EW-TEMPLATE-PLAN section 5): the template's CC1 macro on the celli only, through A's map
# (keeps the dolce vibrato: mf CC11 72 -> CC1 90, Molto Vib about 0.72); legato joins measured on the render, the map
# dropped if any join dip grows 2 dB or more
CC1_FROM_CC11 = dict(CC1_FROM_CC11, **{"Violoncellos": [(0, 0), (58, 58), (72, 90), (127, 127)]})
# the coda solo (alias of Violoncellos on Celli KS Master DIV A) keeps its own CC1 lane (A: the macro on the celli only)
ALIAS_TRACKS["Cello solo"]["globals"] = dict(ALIAS_TRACKS["Cello solo"].get("globals", {}),
                                             CC1_FROM_CC11={k_: v_ for k_, v_ in CC1_FROM_CC11.items() if k_ != "Violoncellos"})
# coordinator 10, critic A #4 (finale item 14): Flute 1 / Flute 2's shared joins at 633 and 639.5 are slur-start joins
# (SOST_JOIN_LEAD_S 0.12 s for both; the leg_leads rows there were inert, LEAD WARNING): their leg_leads rows now add to
# that lead on the flutes only (Flute 1 landed -94 / -70 ms, Flute 2 -32 / +4 ms: Flute 1 -0.09 / -0.07, Flute 2 -0.03)
SOST_JOIN_LEG_LEADS = ("Flute 1", "Flute 2")
# ---------- c52 corrections after the render (level only: tools/stem_fix.py on the c52 stems; cycles/c52/CHANGES.md) ----------
# critic A #2 refit: the celli sf bump started at -0.12 s on the held A-flat (the stroke now leads 0.05 s, not 0.15): a
# pre-echo peak at -0.08 s; it starts at the stroke and carries the weak first 0.1 s of the Sus Marc LITE attack
# (frames -25.5 / -20.2 / -23.6 dB against -17.9 at +0.16 s). Violins I 78: the G6 bloom peaked at +0.12 s, 2.6 dB over
# the first 0.1 s: the bump ends at +0.09 s and holds +0.5 dB over the bloom
POST_SHAPES_S["Violoncellos"] = [r_ for r_ in POST_SHAPES_S["Violoncellos"] if r_[0] != 160.0] + [
    (160.0, [(-0.06, 0.0), (-0.05, 8.0), (0.10, 8.0), (0.14, 3.0), (0.20, 3.0), (0.28, 0.0)])]
POST_SHAPES_S["Violins I"] = [r_ for r_ in POST_SHAPES_S["Violins I"] if r_[0] != 78.0] + [
    (78.0, [(-0.07, 0.0), (-0.06, 3.0), (0.09, 3.0), (0.12, 0.5), (0.18, 0.5), (0.25, 0.0)])]
# critic C #2 (bar 84) on the render: with the celli bloom shape gone the celli's p G2 swelled 12 dB from +0.1 to +0.6 s
# (its slow first-note attack) and the master rose 5 dB from +0.15 to +0.35 s: the shape is back (C's re-swell in c51 was
# the basses' -8 dB release cut lifting at 332.25-332.4, which stays fixed)
LEVEL_SHAPES["Violoncellos"] = [([(332.5, 0.0), (332.9, -3.0), (333.1, -5.0), (334.0, -5.0), (334.6, -2.0), (335.3, -2.0),
                                  (335.42, -3.0), (335.48, -9.0), (336.2, -9.0), (336.26, 0.0)]
                                 if s_ == [(335.3, 0.0), (335.42, -3.0), (335.48, -9.0), (336.2, -9.0), (336.26, 0.0)] else s_)
                                for s_ in LEVEL_SHAPES["Violoncellos"]]
# critic C #1 refit (Horn 1 dolce): the recap's 595-596 crescendo fell 3.8 dB (end against 0.3 s before; the exposition's
# 195 twin has the c39 swell row, the recap none): a rise over the hairpin; the 601 tenuto's note trim -4 -> -1.5 in
# note_trims.json (the 601-603 crescendo rose only 1.2 dB from the bar before)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(594.95, 0.0), (595.15, 1.5), (595.6, 4.5), (595.85, 6.0), (596.05, 5.0),
                                                    (596.35, 0.0)]]
# critic B #1 on the render: Horn 1's bar-125 "mp espr." entry beat sat 1.6 dB under the loudest other (Bassoon 2 /
# Violins I at 497; c50 -0.2, c51 -6.7): +1.5 dB on its first beat (Dan's balance priority)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(496.75, 0.0), (496.85, 1.5), (497.9, 1.5), (498.1, 0.0)]]
# critic A #3 on the render (RR_RESET_AT): the reset fixed the stroke order per segment, but 104 (C2), 520 (C2) and 528
# (A-flat 1) start on the weak stroke (heard front, downbeat minus off-beat -2.8 / -2.1 / -0.3 dB), 664 +0.5, 112 +1.0:
# per-segment level steps on the strokes, downbeats +c / off-beats -c, c = (2.0 - measured) / 2 (the finale's table is
# the same idea; METRIC_BOWED skips REP_SPLIT strokes, so exact rows here)
for a_, b_, c_ in ((104.0, 107.5, 2.4), (112.0, 115.5, 0.5), (520.0, 525.5, 2.05), (528.0, 531.5, 1.15), (664.0, 675.5, 0.75)):
    for i_ in range(int(round((b_ - a_) / 0.5)) + 1):
        q_ = a_ + 0.5 * i_
        d_ = c_ if abs(q_ - round(q_)) < 0.01 else -c_
        LEVEL_SHAPES_S["Double basses"] = LEVEL_SHAPES_S.get("Double basses", []) + [
            (q_, [(-0.09, 0.0), (-0.08, d_), (0.15, d_), (0.16, 0.0)])]

# ---------- c53 ----------
# critic A #1: at qn 292.0 (bar 74) Violins II and Violas start printed whole notes and the Double basses' automatic
# "change bow at will" point sat on the same beat (master dip 4.1 dB, the basses' stem 8.2 dB). The basses hold one
# pitch 286-304: their point moves to 290.9 (0.52 s before the printed changes, 0.84 s after the celli's 289.145 point);
# its fill in build/rebow_fills.json is re-keyed "292" -> "290.9" and refitted (tools/fit_rebows.py --only ... --fine)
assert any(abs(q_ - 292.0) < 1e-3 for q_ in REBOW_AT["Double basses"])
REBOW_AT = dict(REBOW_AT, **{"Double basses": sorted(290.9 if abs(q_ - 292.0) < 1e-3 else q_
                                                     for q_ in REBOW_AT["Double basses"])})
# critic B #6: bar 4, the timpani roll rose against its printed decrescendo (the c13 -3 dB shape let go at 15.6-15.9,
# inside the roll): the shape now holds to the roll's end
_t13 = [(12.4, 0.0), (12.9, -3.0), (15.6, -3.0), (15.9, 0.0)]
assert _t13 in LEVEL_SHAPES["Timpani"]
# (stem fix after the render: quarter 15 still read 0.2 dB over quarter 14, so the cut deepens to -3.6 dB from 15.5)
LEVEL_SHAPES["Timpani"] = [([(12.4, 0.0), (12.9, -3.0), (15.0, -3.0), (15.5, -3.6), (16.5, -3.6), (16.95, 0.0)] if s_ == _t13 else s_)
                           for s_ in LEVEL_SHAPES["Timpani"]]
# critic A #3 (finale technique 19): the tutti sf at qn 160 (bar 41) has no weight in the brass (trumpets, tuba and
# bass trombone play 0.29 s on sustain rows and are still rising at the note's end; Horns 3 / 4 and three winds have a
# weak first 0.1 s): post-fader bumps as the strings have had at 160 since c52, +3 dB (trumpets +4), each starting at
# the track's own moved note-on when that is earlier than -0.07 s (leads: Flute 2 0.10, Trumpet 2 0.09, Trumpet 3 0.07 s)
# The c53 render had A's flat form, (a, 0), (a + 0.01, d), (0.17, d), (0.25, 0) with d = 3 dB (trumpets 4): where the
# stem's peak falls inside the bump (0.10-0.18 s on the trumpets, Horn 4 and the tuba) the peak rose as much as the front
# and A's check (first 0.1 s within 2 dB of the peak) still failed on seven stems. Stem fix after the render
# (cycles/c53/actor_scripts/sfsim53.py on the rendered stems): front-weighted bumps, full to t1 and gone by t2, so the
# front rises and the peak after it does not. Rows: track, dB, start, t1, t2 (s from the score onset)
for tn_, d_, a_, t1_, t2_ in (("Tuba", 6.0, -0.07, 0.02, 0.08), ("Bass trombone", 3.0, -0.07, 0.05, 0.11),
                              ("Horn 3", 4.5, -0.07, 0.08, 0.20), ("Horn 4", 5.0, -0.07, 0.05, 0.17),
                              ("Oboe 1", 4.0, -0.07, 0.08, 0.20), ("Flute 2", 3.0, -0.11, 0.05, 0.11),
                              ("Clarinet 1", 3.0, -0.07, 0.05, 0.11), ("Trumpet 1", 4.0, -0.07, 0.05, 0.11),
                              ("Trumpet 2", 4.0, -0.10, 0.05, 0.11), ("Trumpet 3", 5.0, -0.08, 0.08, 0.14)):
    assert not any(r_[0] == 160.0 for r_ in POST_SHAPES_S.get(tn_, []))
    POST_SHAPES_S[tn_] = POST_SHAPES_S.get(tn_, []) + [(160.0, [(a_, 0.0), (a_ + 0.01, d_), (t1_, d_), (t2_, 0.0)])]
# critic A #5 (MANUAL-GAPS 11, manual p.110): bar 30, the four printed staccato eighths 116.0-117.5 of Flute 1, Oboe 1
# and Clarinet 1 (doubling Violins I) were 84-133 ms slices of sustain samples, uneven by 8-15 dB from note to note:
# the recorded "Stac DblTng RRx9" row on second-pass "... stac" instances, as the fugato has had since c39 (the main
# project loads no row more). The windows hold only the four eighths (score onsets), so the sources keep 115.5 and 118.0
_W30 = (115.9, 117.9)
for t_ in ("Flute 1", "Oboe 1", "Clarinet 1"):
    ART_SPANS = dict(ART_SPANS, **{t_: ART_SPANS.get(t_, []) + [
        {"from": 116.0, "to": 118.0, "art": "Stac DblTng RRx9", "mark": "staccato", "vel_by_cc": _WSTAC}]})
    w_ = sorted((list(TRACK_WINDOWS[t_][0]) if t_ in TRACK_WINDOWS else []) + [_W30])
    assert t_ not in TRACK_WINDOWS or TRACK_WINDOWS[t_][1] is False
    TRACK_WINDOWS = {**TRACK_WINDOWS, t_: (w_, False)}
    if f"{t_} stac" in ALIAS_TRACKS:
        ALIAS_TRACKS[f"{t_} stac"] = dict(ALIAS_TRACKS[f"{t_} stac"], windows=w_)
    else:
        ALIAS_TRACKS = dict(ALIAS_TRACKS, **{f"{t_} stac": {"source": t_, "windows": w_}})
        PASS2_TRACKS = tuple(PASS2_TRACKS) + (f"{t_} stac",)
# c53 after the render (critic A #5): at one velocity the staccato row's level differs by pitch. Rendered peaks, dB:
# Flute 1 stac -37.5 -31.3 -33.5 -38.5 (pitches 82 84 85 82), Oboe 1 stac -30.8 -39.3 -38.0 -31.5 (70 72 73 70),
# Clarinet 1 stac -28.7 -30.9 -31.5 -31.3 (inside A's 4 dB). Per-note levels on the alias tracks only, each note's
# value held to 0.04 qn (about 19 ms) before the next written onset and the step ending 0.01 qn (5 ms) before it (with
# the step at 0.10-0.04 qn before the onset, the raised tail of Oboe 1's first note read as the second note's onset,
# 60 ms early); applied to the c53 stems with tools/stem_fix.py
def _st30(g_):
    pts_ = [(115.9, 0.0), (115.95, g_[0])]
    for i_ in (1, 2, 3):
        pts_ += [(115.96 + 0.5 * i_, g_[i_ - 1]), (115.99 + 0.5 * i_, g_[i_])]
    return pts_ + [(118.2, g_[3]), (118.3, 0.0)]
ALIAS_TRACKS["Flute 1 stac"]["tables"] = dict(ALIAS_TRACKS["Flute 1 stac"].get("tables", {}))
ALIAS_TRACKS["Flute 1 stac"]["tables"]["LEVEL_SHAPES"] = ALIAS_TRACKS["Flute 1 stac"]["tables"].get("LEVEL_SHAPES", []) + [
    _st30((2.3, -3.9, -1.7, 3.3))]
ALIAS_TRACKS["Oboe 1 stac"]["tables"] = {"LEVEL_SHAPES": [_st30((-4.1, 4.4, 3.1, -3.4))]}
# critic A #6: bar 161, Oboe 2's eighth before the printed breath sounded for 109 ms of a written 300 ms
BREATH_GAP_AT["Oboe 2"] = {**BREATH_GAP_AT.get("Oboe 2", {}), 643.5: 0.10}
# critic B #2: bars 115-116 (456-464), the celli's inner voice was the loudest stem in the crescendo (up to +5.9 dB over
# Violins I): a cut that follows the crescendo and hands over to the letter-G role [464, 484, -6] of build/roles.json
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(456.0, 0.0), (457.0, -2.5), (458.0, -6.5), (459.0, -8.6), (460.0, -8.6), (460.1, -6.0), (463.5, -6.0), (464.0, 0.0)]]
# (stem fix after the render: -8.0 dB at 459-460 left Violins I 1.9 dB over the celli in quarter 459, target 2: -8.6 dB)
# critic B #4 (coordinator 8): Oboe 1 at p in bars 124-126 doubles Violins I 3-13 dB under them. B's values (+6 dB over
# 496-498, +8 dB over 500-504) measured on a range render: Oboe 1 minus Violins I -5.1 dB at 496-498 and +0.9 / -0.6 dB
# at 500-502 / 502-504 (coordinator target: 2-5 dB under), so +7 dB and +5 dB (the c44 -3 dB shape at 498.6-499.9
# stays between them)
# (stem fix after the render: with +7 dB quarter 496 read 6.0 dB under Violins I, 497 3.2 dB under: +8.8 dB in 496)
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(495.95, 0.0), (496.0, 8.8), (496.9, 8.8), (497.0, 7.0), (497.9, 7.0), (498.0, 0.0)],
                                                    [(499.9, 0.0), (500.0, 5.0), (503.8, 5.0), (504.0, 0.0)]]
# critic B #3: the cor anglais's note trim at 604 is gone from build/note_trims.json, and its 0.1 s ramp with it
assert 604.0 in NOTE_TRIM_RAMP_S["Cor anglais"]
NOTE_TRIM_RAMP_S["Cor anglais"] = {q_: v_ for q_, v_ in NOTE_TRIM_RAMP_S["Cor anglais"].items() if q_ != 604.0}
# stem fix after the render (finale technique 22): a note trim ramps in over 0.6 s, so the c53 trims of
# build/note_trims.json on short notes were realised in part: Oboe 1 168 +7 dB as +2.7 and Flute 2 168 +6 dB as +2.1
# (the note lasts 0.53 s), Bassoon 1 460 -5 dB as -1.8 in its first quarter. 0.1 s ramps
NOTE_TRIM_RAMP_S["Oboe 1"] = {**NOTE_TRIM_RAMP_S.get("Oboe 1", {}), 168.0: 0.1}
NOTE_TRIM_RAMP_S["Flute 2"] = {**NOTE_TRIM_RAMP_S.get("Flute 2", {}), 168.0: 0.1}
NOTE_TRIM_RAMP_S["Bassoon 1"] = {**NOTE_TRIM_RAMP_S.get("Bassoon 1", {}), 460.0: 0.1}

# ---------------------------------------------------------------------------------------------------------------------
# c54, PRIORITY 1 (Dan, 2026-11-10): "the main theme that comes in at rehearsal mark A, the melody in the strings feels
# choppy and doesn't feel like it's really playing in perfect time/rhythm"
# (1) no unprinted tempo steps inside the first theme and its return: the arcs and pushes below gave 126 -> 121 for one
# beat in bars 17, 20, 29, 131, 138, 140, 143 and 120-128 over the phrase ends (coordinator's measurement). The theme
# runs at the printed 126 from bar 15 to the tutti stop of bar 32 (qn 56-128) and from bar 131 to the printed poco rit.
# of bar 145 (qn 520-576). The Lento, transition, second-theme, development and coda arcs stay.
_C54_FLAT = ((56, 128), (520, 576))
import os as _os54
if _os54.environ.get("C54_SHOW"):
    print("C54 arcs before:", sorted(PHRASE_ARCS), "pushes:", sorted(TEMPO_PUSH), file=__import__("sys").stderr)
PHRASE_ARCS = [x_ for x_ in PHRASE_ARCS if not any(a_ <= x_[0] and x_[1] <= b_ for a_, b_ in _C54_FLAT)]
TEMPO_PUSH = [x_ for x_ in TEMPO_PUSH if not any(a_ <= x_[0] and x_[1] <= b_ for a_, b_ in _C54_FLAT)]
# (2) the theme on one row with one lead (tools/score_to_parts.py STEADY_LINE), on every track that plays it:
#   bars 15-22 Violins I (Violins II double the D-flat and its descent in bars 20-21); bars 23-25 Violins I with Flute 1
#   and Oboe 1; bars 27-32 Violins I / II, Violas, Flute 1, Oboe 1, Clarinet 1; bars 131-134 Violoncellos, Clarinet 1,
#   Bassoon 1, Trombone 1; bars 135-144 Violins I (II from 139), Flute 1, Oboe 1 (Clarinet 1 from 139).
# Strings: Sus MAX on every note (in c53 Sus MAX notes after Sus MAX notes spoke 90 ms after note-on, SD 19 ms; legato
# targets 237-248 ms, SD 50-57 ms, longer than the 238 ms eighth). Slurred notes end at the next note-on (the 150 ms
# release cap carries them into it), unslurred ones 30 ms before it, same-pitch repeats 50 ms before it.
# Winds: the legato row on every note with one lead per track (c53: legato after legato 44-94 ms, SD 14-39 ms; legato
# after a Sus-row slur head 103-224 ms, SD 24-73 ms); a tongued note (not slurred from the note before) leads 20 ms.
# C54_VARIANT / C54_WINDS (environment) select the variants of the c54 range tests; the defaults are what shipped.
_C54_VAR = _os54.environ.get("C54_VARIANT", "marc")
_C54_WINDS = _os54.environ.get("C54_WINDS", "0") == "1"
_C54_SPEC = {
    "sus": {"art": "Sus MAX", "lead_s": 0.09, "overlap_s": 0.0, "gap_s": 0.03, "rep_gap_s": 0.05, "rr_reset": True},
    # shipped (range test 1, Violins I bars 15-22, measure S: SD 22 ms against Sus MAX 44, Slur Runs 40, legato with one
    # lead 57, c53 46). At one 60 ms lead the slurred notes read +25..+50 ms, the notes after a 30 ms gap -14..-4 ms and
    # the entries after a rest +23..+45 ms (pcX), so each class has its lead
    # (range test 4: the same-pitch repeat c''8 c''4-- had its dip 68 ms after the beat at the 50 ms lead and sounded 57 ms early at 110 ms: 85 ms)
    "marc": {"art": "Sus Marc LITE", "lead_s": 0.09, "tongue_lead_s": 0.05, "first_lead_s": 0.10, "rep_lead_s": 0.085,
             "overlap_s": 0.0, "gap_s": 0.03, "rep_gap_s": 0.05, "rr_reset": True},
    "leg": {"art": "Leg Slur MAX", "lead_s": 0.24, "first_lead_s": 0.06, "overlap_s": 0.02,
            "gap_s": -0.02, "rep_gap_s": 0.04, "vel": 124, "rr_reset": True},
    "runs": {"art": "Slur Runs", "lead_s": 0.08, "first_lead_s": 0.05, "tongue_lead_s": 0.05, "overlap_s": 0.02,
             "gap_s": 0.03, "rep_gap_s": 0.04, "vel": 127, "rr_reset": True},
}
_C54_STR_SPANS = {"Violins I": [(56.0, 127.0), (536.0, 576.0)],
                  "Violins II": [(77.9, 82.1), (104.0, 127.0), (552.0, 576.0)],
                  "Violas": [(104.0, 127.0)],
                  "Violoncellos": [(520.0, 536.0)]}
_C54_MARC_OFF = {"Violoncellos": 0.02}
_C54_STR_LEAD = {"Violins I": 0.09, "Violins II": 0.09, "Violas": 0.09, "Violoncellos": 0.11}
# (row, legato lead s)
# (Flute 1 is left as it is: on measure S its c53 lines already read robust SD 6-17 ms)
_C54_WIND = {"Oboe 1": ("Leg Slur MAX", 0.065, [(88.0, 127.0), (536.0, 576.0)]),
             "Clarinet 1": ("Leg Slur", 0.075, [(104.0, 127.0), (520.0, 536.0), (552.0, 576.0)]),
             "Bassoon 1": ("Leg Slur MAX", 0.095, [(520.0, 536.0)]),
             "Trombone 1": ("Leg Slur MAX", 0.095, [(520.0, 536.0)])}
# per-onset rows fitted on the c54 range renders and re-checked on the full render: build/steady54.json
# {track: {score qn: {"lead_s", "end_s", "art"}}}
_C54_AT = json.load(open(f"{BUILD}/steady54.json")) if _os54.path.exists(f"{BUILD}/steady54.json") else {}
# per-note level steps of the spans' notes (cycles/c54/actor_scripts/levels54.py): build/steady_levels54.json
_C54_LV = json.load(open(f"{BUILD}/steady_levels54.json")) if _os54.path.exists(f"{BUILD}/steady_levels54.json") else {}
STEADY_LINE = {}
if _C54_VAR != "off":
    for t_, sp_ in _C54_STR_SPANS.items():
        if _os54.environ.get("C54_ONLY") and t_ not in _os54.environ["C54_ONLY"].split(","):
            continue
        b_ = dict(_C54_SPEC[_C54_VAR])
        if _C54_VAR == "sus":
            b_["lead_s"] = _C54_STR_LEAD[t_]
        elif _C54_VAR == "marc":   # per-track offset on the three leads (fitted on the range renders)
            for k_ in ("lead_s", "tongue_lead_s", "first_lead_s", "rep_lead_s"):
                b_[k_] = round(b_[k_] + _C54_MARC_OFF.get(t_, 0.0), 3)
        STEADY_LINE[t_] = [dict(b_, **{"from": a_, "to": e_, "at": _C54_AT.get(t_, {}), "level_db": _C54_LV.get(t_, {})}) for a_, e_ in sp_]
    if _C54_WINDS:
        for t_, (row_, ld_, sp_) in _C54_WIND.items():
            STEADY_LINE[t_] = [{"art": row_, "lead_s": ld_, "first_lead_s": 0.02, "tongue_lead_s": 0.02, "overlap_s": 0.02,
                                "gap_s": 0.03, "rep_gap_s": 0.06, "rr_reset": True, "from": a_, "to": e_,
                                "at": _C54_AT.get(t_, {}), "level_db": _C54_LV.get(t_, {})} for a_, e_ in sp_]

# ---------------------------------------------------------------------------------------------------------------------
# c54, the coordinator's decisions on critic reports A, B, C (cycles/c54/COORDINATOR-NOTES.md), in its order
# 1. C #2: bar 33 downbeat. The ff C6 after the Slur Runs was a Leg BC target with 64 ms of lead; B5 held the downbeat
# and C6 reached its level at +210 ms. A fresh down-bow stroke as at 160 and 272
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violins I": DOWNBOW_STROKE_AT["Violins I"] + [128.0]})
# 2. C #5: string legato notes after a Sus-row note (robust SD 82 ms, 28 % over 60 ms late). C's exposed rows stay on
# Sus MAX like their predecessors (re-attack lead); Violas 168 (after a tremolo) gets a fill in build/early_fills.json
SHORT_SUS_AT = {**SHORT_SUS_AT, "Violas": SHORT_SUS_AT.get("Violas", []) + [76.0, 368.0, 428.0, 434.0, 436.0],
                "Violoncellos": SHORT_SUS_AT.get("Violoncellos", []) + [356.0],
                "Violins II": SHORT_SUS_AT.get("Violins II", []) + [290.0, 400.0]}
# C #5: Oboe 1 578 (p, bar 145) read +95 / +117 ms late: its +8 dB note trim ramps in over 0.1 s from the score onset
# while the note-on is 0.104 s early. The same +8 dB from the moved onset, handed over to the trim's ramp
LEVEL_SHAPES_S["Oboe 1"] = LEVEL_SHAPES_S.get("Oboe 1", []) + [(578.0, [(-0.125, 0.0), (-0.105, 8.0), (0.0, 8.0), (0.1, 0.0)])]
# 3. C #1: wind and brass slurs that start on a Sus-row note (79 joins, two pitches together for a median 140 ms).
# Range test first (C54_JOIN=1 builds the test variant); the shipped value follows the test (see CHANGES.md)
# Range test (cycles/c54/theme/jbase_* / jtest_*, robust crossover against the beat): Bassoon 1 131 +50 -> +4 ms,
# 133.5 +82 -> +30 ms, Clarinet 1 509.5 +57 -> +26 ms, 507 -3 -> -40 ms (its +0.08 s row halved): shipped
_C54_JOIN = _os54.environ.get("C54_JOIN", "1") == "1"
if _C54_JOIN:
    SLUR_START_SUS = dict(SLUR_START_SUS, head_end_s=0.03)
    SOST_JOIN_LEAD_S = {"default": 0.12, "wind": 0.07, "brass": 0.07}
# 4. C #3: wind entries with long entry leads start early by about the lead (Bassoon 1 14 of 14 loud entries 91-115 ms
# early; the Sustain rows have no slow attack, manual p.109). Tuples are (soft, loud, mid). "Contrabassoon" stands before
# "Bassoon" because by_name() matches substrings in dict order
_el54 = {k_: v_ for k_, v_ in ENTRY_LEAD_S.items() if k_ not in ("Bassoon", "Contrabassoon")}
_el54.update({"Bassoon 1": (0.03, 0.02, 0.02), "Flute 2": (0.0, 0.0, 0.0), "Contrabassoon": (0.01, 0.01),
              "Bassoon": (0.025, 0.02)})
ENTRY_LEAD_S = _el54
# 5. A #1: cor anglais solo, bar 7 (qn 26): the hairpin's top note sat 6-8 dB under for 340 ms and the volume lane fell
# 4.2 dB inside the hole (7.40 dB at 25.93 to 3.23 dB at 26.18). The lane is held to 26.30 (this row is the difference
# to the c53 lane), and build/early_fills.json adds +5 dB over the join
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES["Cor anglais"] + [
    [(25.9323, 0.0), (25.9823, 0.73), (26.0, 0.98), (26.1823, 4.17), (26.3, 4.4), (26.55, 0.0)]]
# A #2 / B #4: Double basses round-robin resets at the final chord and at the start of each pizzicato passage, so the
# bow / take phase there no longer depends on what was played before (the six final-chord fills are refitted)
RR_RESET_AT = dict(RR_RESET_AT, **{"Double basses": sorted(RR_RESET_AT["Double basses"] + [184.0, 408.0, 584.0, 712.0])})
# 6. B #1: the celli's held A-flat 3 / F3 at f and ff as loud as the tune (bars 25, 31, 40, 132, 140): note trims in
# build/note_trims.json with 0.1 s ramps, and two shapes
NOTE_TRIM_RAMP_S["Violoncellos"] = {**NOTE_TRIM_RAMP_S.get("Violoncellos", {}), 97.0: 0.1, 120.0: 0.1, 122.0: 0.1}
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(157.4, 0.0), (158.0, -3.0), (159.75, -3.0), (160.0, 0.0)],
    [(556.75, 0.0), (557.0, -6.0), (558.0, -6.0), (558.25, 0.0)]]
# 7. A #3: Violins I bar 30, the first of four Staccatissimo strokes reaches its level 60-80 ms before the other three
# (another round-robin sample since c52): a build/retongue_leads.json row takes its 45 ms stroke lead away.
# A #5: Flute 1's slurred C6 at 115.5 rang over the first staccato of the "Flute 1 stac" track
BREATH_GAP_AT["Flute 1"] = {**BREATH_GAP_AT.get("Flute 1", {}), 115.5: 0.10}
# 8. B #5 (optional): bar 134, the timpani's eight ff strokes level with the theme group
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES.get("Timpani", []) + [[(531.9, 0.0), (532.0, -2.5), (535.9, -2.5), (536.0, 0.0)]]
# 2 (continued). Violas 368, Violoncellos 356 and Violins II 400 are unslurred Leg BC targets after Sus MAX notes
# (SHORT_SUS_AT reads slurred notes only): fresh Sus MAX strokes. The SHORT_SUS_AT notes get the 0.09 s Sus MAX lead
# through build/retongue_leads.json (they came out with 0 s, Violins II 290 with 0.18 s)
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violas": DOWNBOW_STROKE_AT.get("Violas", []) + [368.0],
                                              "Violoncellos": DOWNBOW_STROKE_AT.get("Violoncellos", []) + [356.0],
                                              "Violins II": DOWNBOW_STROKE_AT.get("Violins II", []) + [400.0]})

# ---------------------------------------------------------------------------------------------------------------------
# c54 after the render (level only; applied to the c54 stems with tools/stem_fix.py, in REAPER with the next build)
# A #2: the Double basses' final-chord pieces read -61.6 -58.0 -55.0 -54.3 -59.4 -62.7 -61.9 dB with the fills refitted on
# the range render (c53: steps up to 10.7 dB). Per-piece steps so that 712-720 lie within 1 dB and nothing rises after 720
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [
    [(711.9, 0.0), (712.0, 3.0), (714.57, 3.0), (714.67, 0.0), (718.07, 0.0), (718.17, -3.0), (719.9, -3.0), (720.0, -4.0),
     (722.57, -4.0), (722.67, 0.0), (725.98, 0.0), (726.08, -1.0), (728.0, -1.0), (728.3, 0.0)]]
# B #1: quarter 159 of bar 40 read melody group minus celli +2.0 dB (target +4); B #5: timpani quarter 535 4.5 dB under
# the theme group (target 6-8)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(158.9, 0.0), (159.0, -2.5), (159.85, -2.5), (160.0, 0.0)]]
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(534.9, 0.0), (535.0, -1.5), (535.9, -1.5), (536.0, 0.0)]]

# ---------------------------------------------------------------------------------------------------------------------
# c55, PRIORITY 1 (coordinator, critics A #1-#3 and B #1 on the c54 render): on Sus Marc LITE every theme note of a
# quarter or longer was a stab followed by a body 8-15 dB lower (Violins I 56-127: front minus tail median 2.9 -> 9.7 dB,
# 12 of 33 long notes sounding under 60 % of their length). Two causes: the accent shapes fitted in c15-c25 for rows
# with a slow front (swell, step trim, body cut) were still stacked on the marcato sample, and the row's own marcato
# sample ends after 0.15-0.25 s and leaves the LITE sustain layer 7-9 dB lower.
# (a) "own_front": no accent swell / fitted accent / accent body cut on the spans' Marc-row notes.
# (b) "body_db" (build/steady_body55.json, fitted by cycles/c55/actor_scripts/fit55.py on the c54 stems with the lane
#     difference applied, then checked on range renders): a per-note body lift from +0.12 s (full at +0.32 s) through
#     the release. C55_LONG=susmax builds the other cure of the range test (notes of 1.5 qn or longer on Sus MAX through
#     `at` rows, keyswitch 0.15 s before the note); see cycles/c55/CHANGES.md for which one shipped and why.
# (c) build/steady_levels54.json refitted (levels55.py: front steps as c54, with the body window printed beside them).
# (d) C55_SLUR=1 builds the slur test (overlap 0.04 s, velocity 60 on slurred targets).
import os as _os55
_C55_OWN = _os55.environ.get("C55_OWN", "1") == "1"
_C55_BODY = json.load(open(f"{BUILD}/steady_body55.json")) if _os55.path.exists(f"{BUILD}/steady_body55.json") \
    and _os55.environ.get("C55_BODY", "1") == "1" else {}
_C55_LONG = _os55.environ.get("C55_LONG", "marc")
_C55_SLUR = _os55.environ.get("C55_SLUR", "0")
_C55_SUSMAX_DB = {"Violins I": 8.0, "Violins II": 8.0, "Violas": 3.0, "Violoncellos": 1.5}   # range-test start values
for t_, sps_ in STEADY_LINE.items():
    for sp_ in sps_:
        if "Marc" not in sp_["art"]:
            continue
        if _C55_OWN:
            sp_["own_front"] = True
        if _C55_BODY.get(t_):
            sp_["body_db"] = {k_: v_ for k_, v_ in _C55_BODY[t_].items() if not k_.startswith("_")}
        # the lift's hold / end after the next note-on: 0.02 / 0.06 s shipped (range test liftb against lift 0 / 0.03:
        # bow-change hole 10.2 -> 9.5 dB, front minus tail 3.5 -> 3.2 dB, S robust SD 9 -> 7 ms)
        sp_["body_off_s"] = tuple(float(x_) for x_ in _os55.environ.get("C55_OFF", "0.02,0.06").split(","))
        if _C55_BODY.get("_tail", {}).get(t_):
            sp_["tail_db"] = dict(_C55_BODY["_tail"][t_])
        if _C55_SLUR in ("1", "2"):
            sp_["overlap_s"] = 0.04
            if _C55_SLUR == "2":
                sp_["slur_vel"] = 60
        if _C55_LONG == "susmax":
            sp_["ks_pre_s"] = 0.15
            sp_["at"] = dict(sp_["at"])
            sp_["level_db"] = dict(sp_["level_db"])
            sp_.pop("body_db", None); sp_.pop("tail_db", None)
            for l_ in open(f"{BUILD}/mockup-events.tsv"):
                c_ = l_.rstrip("\n").split("\t")
                if c_[0] == {"Violins I": "VlnI", "Violins II": "VlnII", "Violas": "Vla", "Violoncellos": "Vc"}[t_] \
                        and c_[3] == "note" and float(c_[5]) >= 1.5 - 1e-6 and sp_["from"] <= float(c_[1]) < sp_["to"]:
                    k_ = "%.3f" % float(c_[1])
                    sp_["at"][k_] = {"art": "Sus MAX", "lead_s": 0.06}
                    sp_["level_db"][k_] = round(float(sp_["level_db"].get(k_, 0.0)) + _C55_SUSMAX_DB[t_], 1)
# C55_LONG=vel: the third cure of the range test: long notes at a low velocity (LEARNINGS c47: the row's marcato sample
# follows velocity on the celli)
if _C55_LONG == "vel":
    for t_, sps_ in STEADY_LINE.items():
        for sp_ in sps_:
            if "Marc" not in sp_["art"]:
                continue
            sp_["at"] = dict(sp_["at"]); sp_.pop("body_db", None); sp_.pop("tail_db", None)
            for l_ in open(f"{BUILD}/mockup-events.tsv"):
                c_ = l_.rstrip("\n").split("\t")
                if c_[0] == {"Violins I": "VlnI", "Violins II": "VlnII", "Violas": "Vla", "Violoncellos": "Vc"}[t_] \
                        and c_[3] == "note" and float(c_[5]) >= 1.0 - 1e-6 and sp_["from"] <= float(c_[1]) < sp_["to"]:
                    k_ = "%.3f" % float(c_[1])
                    sp_["at"][k_] = dict(sp_["at"].get(k_, {}), vel=int(_os55.environ.get("C55_VEL", "45")))

# ---------------------------------------------------------------------------------------------------------------------
# c55, the coordinator's decisions on critic reports A, B, C (cycles/c55/COORDINATOR-NOTES.md), in its order
# 1. C #1 (approved): no unprinted tempo steps in the music printed at 126 outside the Lento: every arc, push and beat
# stretch inside these spans goes (110 of 318 beats were off the printed tempo by more than 1 %; bars 103-110 repeated
# one two-bar shape four times). The second-theme arcs become "sub" (the last two beats x0.98 / x0.95, no push) without
# apex holds (bars 50 and 150 alternated 107.5 / 112 / 107.5 / 103). The Lento, sostenuto (488-504), largamente
# (636-648), Piu lento and Tempo I arcs, the caesura at 636 and the fermata stretch at 679 stay.
# C55_TEMPO=0 builds on the c54 map (the level simulations on the c54 stems need it).
_C55_FLAT = ((128, 176), (270, 448), (464, 480), (664, 679))
if _os55.environ.get("C55_TEMPO", "1") == "1":
    PHRASE_ARCS = [x_ for x_ in PHRASE_ARCS if not any(a_ <= x_[0] and x_[1] <= b_ for a_, b_ in _C55_FLAT)]
    TEMPO_PUSH = [x_ for x_ in TEMPO_PUSH if not any(a_ <= x_[0] and x_[1] <= b_ for a_, b_ in _C55_FLAT)]
    BEAT_STRETCH = {k_: v_ for k_, v_ in BEAT_STRETCH.items() if k_ not in (284.0, 285.0)}
    _c55_sub = ((184, 200), (200, 220), (220, 232), (232, 244), (584, 600), (600, 620))
    PHRASE_ARCS = [(x_[0], x_[1], "sub") if tuple(x_[:2]) in _c55_sub else x_ for x_ in PHRASE_ARCS]
    APEX_SKIP = APEX_SKIP | {a_ for a_, _e in _c55_sub}
# 2. C #3: the one-row treatment on the fast marked string lines outside the theme, with 0a-0c from the start (no accent
# shapes, body lifts, level steps). Notes printed longer than 2.5 qn keep their rows. C55_NEW=0 leaves these spans out.
# Violins I 128.4-158 (bars 33-40; the down-bow C6 of bar 33 and the Slur Runs group at 158 keep their rows), Violins I
# and II 448-480 (bars 113-120), the development 304-384 on Violins I, Violas and Violoncellos.
_C55_NEW = {k_: v_ for k_, v_ in {
    "Violins I": [(128.4, 158.0), (304.0, 384.0), (448.0, 480.0)], "Violins II": [(448.0, 480.0)],
    "Violas": [(304.0, 384.0)], "Violoncellos": [(304.0, 384.0)]}.items()}
# Shipped: Violins I 128.4-158 only. The other spans were range-tested (cycles/c55/CHANGES.md): their dynamics move
# (hairpins on long notes), and the body-lift fit, which levels a note's front and tail, would flatten printed
# diminuendos there; Violins II 448-480 read less steady on the row before any fit (robust SD 32 -> 57 ms).
_c55_new_on = _os55.environ.get("C55_NEW", "128")
if _c55_new_on != "0" and _C54_VAR == "marc":
    for t_, sp_ in _C55_NEW.items():
        b_ = dict(_C54_SPEC["marc"])
        for k_ in ("lead_s", "tongue_lead_s", "first_lead_s", "rep_lead_s"):
            b_[k_] = round(b_[k_] + _C54_MARC_OFF.get(t_, 0.0), 3)
        for a_, e_ in sp_:
            if _c55_new_on != "1" and not any(abs(a_ - float(x_)) < 1 for x_ in _c55_new_on.split(",")):
                continue   # C55_NEW="128,448": only the spans that start there
            STEADY_LINE.setdefault(t_, []).append(dict(
                b_, **{"from": a_, "to": e_, "max_len_qn": 2.5, "at": _C54_AT.get(t_, {}), "level_db": _C54_LV.get(t_, {}),
                       "own_front": _C55_OWN, "body_off_s": (0.02, 0.06), "body_db": {k2_: v2_ for k2_, v2_ in _C55_BODY.get(t_, {}).items()},
                       "tail_db": dict(_C55_BODY.get("_tail", {}).get(t_, {}))}))
# Violas 438.0 (bar 110): a Leg Slur target after a Sus MAX note with lead 0 reached the old pitch's level at +270 ms:
# a Sus MAX note like its predecessors (c54 decision 2), 0.09 s lead through build/retongue_leads.json
SHORT_SUS_AT = {**SHORT_SUS_AT, "Violas": SHORT_SUS_AT.get("Violas", []) + [438.0]}
# 5. B #2: bar 30, the strings' four ff Staccatissimo eighths stood 3-5 dB over the theme's eighths (no accent printed)
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES.get("Violins I", []) + [[(115.90, 0.0), (115.93, -3.5), (117.72, -3.5), (117.75, 0.0)]]
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [[(115.90, 0.0), (115.93, -3.0), (117.72, -3.0), (117.75, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [
    [(115.90, 0.0), (115.93, -4.5), (116.40, -4.5), (116.45, 0.0)], [(117.45, 0.0), (117.48, 2.0), (117.72, 2.0), (117.75, 0.0)]]
# A #4: Flute 1's slurred C6 at 115.5 still covered the first staccato of the "Flute 1 stac" track (the c54
# BREATH_GAP_AT row did nothing on this note): the note ends at 115.8
BREATH_GAP_AT["Flute 1"] = {k_: v_ for k_, v_ in BREATH_GAP_AT.get("Flute 1", {}).items() if k_ != 115.5}
NOTE_END_AT = dict(NOTE_END_AT, **{"Flute 1": {**NOTE_END_AT.get("Flute 1", {}), 115.5: 115.8}})
# B #4: Oboe 1 in unison with Violins I, the four onsets c54 left over -2 dB (build/note_trims.json, 0.1 s ramps)
NOTE_TRIM_RAMP_S["Oboe 1"] = {**NOTE_TRIM_RAMP_S.get("Oboe 1", {}), 97.0: 0.1, 98.0: 0.1, 476.0: 0.1}
# 3. C #4: the lyrical slurred string lines. Range test of three one-row variants on the celli's second theme
# (C55_LYR=leg | sus | marc builds one; unset = as c54): Leg Slur MAX only with one lead, Sus MAX with a 0.06 s overlap
# and one 0.09 s lead, Sus Marc LITE as the first theme. Result and what shipped: cycles/c55/CHANGES.md.
_C55_LYR = _os55.environ.get("C55_LYR", "")
_C55_LYR_SPANS = {"Violoncellos": [(184.0, 244.0)]}
_C55_LYR_SPEC = {
    "leg": {"art": "Leg Slur MAX", "lead_s": 0.20, "first_lead_s": 0.08, "tongue_lead_s": 0.20, "overlap_s": 0.02,
            "gap_s": -0.02, "rep_gap_s": 0.04, "rr_reset": True},
    "sus": {"art": "Sus MAX", "lead_s": 0.09, "first_lead_s": 0.11, "overlap_s": 0.06, "gap_s": 0.02, "rep_gap_s": 0.05,
            "rr_reset": True},
    "marc": dict(_C54_SPEC["marc"], lead_s=0.11, tongue_lead_s=0.07, first_lead_s=0.12, rep_lead_s=0.105, own_front=True)}
if _C55_LYR in _C55_LYR_SPEC:
    for t_, sp_ in _C55_LYR_SPANS.items():
        STEADY_LINE.setdefault(t_, []).extend(
            dict(_C55_LYR_SPEC[_C55_LYR], **{"from": a_, "to": e_, "max_len_qn": 6.0, "at": {}, "level_db": {}}) for a_, e_ in sp_)
# C55_LONGEND (range-test variant; the shipped value is the default below, see CHANGES.md): notes of a quarter or longer
# in the Marc spans end this many seconds after the next moved note-on instead of 0.03 s before it (their release then
# runs under the next attack: the bow-change hole against the lifted body read 9.5-10 dB)
# Shipped: 0.0 (range test liftc against liftb: bow-change hole 9.5 -> 8.2 dB, front minus tail 3.2 -> 2.7 dB, S robust
# SD 7 -> 9 ms, S median +3 -> +8 ms). C55_LONGEND=off builds without it.
_C55_LONGEND = _os55.environ.get("C55_LONGEND", "0.0").replace("off", "")
if _C55_LONGEND != "":
    _st55 = {"Violins I": "VlnI", "Violins II": "VlnII", "Violas": "Vla", "Violoncellos": "Vc"}
    for t_, sps_ in STEADY_LINE.items():
        for sp_ in sps_:
            if "Marc" not in sp_["art"]:
                continue
            sp_["at"] = dict(sp_["at"])
            for l_ in open(f"{BUILD}/mockup-events.tsv"):
                c_ = l_.rstrip("\n").split("\t")
                if c_[0] == _st55[t_] and c_[3] == "note" and float(c_[5]) >= 0.9 and sp_["from"] <= float(c_[1]) < sp_["to"]:
                    k_ = next((k2_ for k2_ in sp_["at"] if abs(float(k2_) - float(c_[1])) < 0.02), "%.3f" % float(c_[1]))
                    sp_["at"][k_] = dict(sp_["at"].get(k_, {}), end_s=float(_C55_LONGEND))

# ---------------------------------------------------------------------------------------------------------------------
# c55 after the render (level only; applied to the c55 stems with tools/stem_fix.py, in REAPER with the next build)
# quarter 159 (bar 40): melody group minus celli read +1.8 dB (target +4; c54 +3.8 after its fix): 2.2 dB more off the celli.
# Also in the json tables: Violoncellos 526 level step +2.5 (the accent stood 0.9 dB over its neighbours with the accent
# shapes gone; target 2-4), cor anglais 24 fill from 0.25 s before the onset.
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(158.9, 0.0), (159.0, -2.2), (159.85, -2.2), (160.0, 0.0)]]

# ---------------------------------------------------------------------------------------------------------------------
# c56 PRIORITY 1 (Dan, 2026-11-11): "the track volume envelope has large peaks and valleys on individual notes, also on
# fast notes; it looks unnatural". c55: 2334 of 5282 notes moved 3 dB or more inside the note, 45 % of them with no
# marking; 5-14 envelope points per second on the strings (reference projects: 0.01-0.36). Coordinator decisions 1a-1e
# (cycles/c56/COORDINATOR-NOTES.md). Everything here is level only; the result was simulated on the c55 stems
# (cycles/c56/actor_scripts/sim56.py) before the render. C56=0 builds the c55 envelope.
import os as _os56
_C56 = _os56.environ.get("C56", "1")
if _C56 != "0":
    # 1a/1b: one level per note. Level layers (trims, metric steps, row trims, pickup lifts, theme level steps, phrase
    # tops) become one value per onset; shapes inside a note (accent swells and bodies, early fills, crescendo fronts,
    # syncopation and pair-release shapes, tenuto weight) stay on notes longer than an eighth, limited to 6 dB per note,
    # and are folded into the level on notes of an eighth or shorter. Config level shapes that lie inside one unmarked
    # note become that note's level (1d). The slow layers, the theme's body and tail lifts, re-bow and loop fills, join
    # notches, breath dips and the repeated-note dips (C56_DIPS) pass unchanged.
    NOTE_LEVEL = {
        "level_tags": ["ptrim", "ntrim", "metric", "pickup", "rowtrim", "steady_level", "ptop", "mt_alt"],
        "shape_tags": ["accent", "acc_body", "marc", "early", "cresc_front", "synco", "pair", "tenuto"]
                      + (["rep_dip", "detach_dip"] if _os56.environ.get("C56_DIPS", "1") == "0" else []),
        "one_note_tags": ["shape"],
        "short_qn": 0.5, "shape_max_db": 6.0, "cross_s": 0.04, "lead_min_s": 0.045, "pre_s": (0.03, 0.008), "rest_s": 0.25,
        "stop_qn": 716.0,
        # spans left as built: the simulation on the c55 stems read a larger note-to-note body step with one level per
        # note (Violins II 104-128 1.5 -> 2.5 dB, 552-576 1.0 -> 1.6, Bassoon 1 520-536 4.6 -> 5.1)
        "skip": {"Violins II": [(104.0, 128.0), (552.0, 576.0)], "Bassoon 1": [(520.0, 536.0)],
                 # after the c56 render (stem fix): lines whose step read more than 0.3 dB worse on the render
                 **({"Cor anglais": [(0.0, 729.0)], "Horn 3": [(0.0, 729.0)], "Trumpet 2": [(0.0, 729.0)],
                     "Violoncellos": [(184.0, 244.0)]} if _os56.environ.get("C56_SKIP2", "1") == "1" else {})},
        # smoothing of the per-note levels over a run (window 2 s) is off: simulated on the c55 stems it raised the
        # note-to-note step on 8-13 of 21 lines (C56_SDEV / C56_LDEV = dB of per-note difference kept, for tests)
        "smooth": {"window_s": float(_os56.environ.get("C56_WIN", "2.0")),
                   "short_dev_db": (None if _os56.environ.get("C56_SDEV", "off") == "off" else float(_os56.environ.get("C56_SDEV"))),
                   "long_dev_db": (None if _os56.environ.get("C56_LDEV", "off") == "off" else float(_os56.environ.get("C56_LDEV")))},
    }
    # 1c: accents. Swell at most +3 dB, swell minus body cut at most 6 dB (the body cut gives way)
    ACCENT_SWELL_CAP_DB = 3.0
    ACCENT_SHAPE_MAX_DB = 6.0
    # lines that measured less even with the fitted accents than without (critic B #2: note-to-note step with / without
    # Oboe 1 88-104 3.21 / 2.36, Clarinet 1 520-536 2.88 / 1.63, Horn 1 400-430 2.01 / 1.41, Trumpet 1 456-496 1.91 / 1.24)
    ACCENT_PLAIN = {"Oboe 1": [(88.0, 104.0, 1.5)], "Clarinet 1": [(520.0, 536.0, 1.5)], "Horn 1": [(400.0, 430.0, 1.5)],
                    "Trumpet 1": [(456.0, 496.0, 1.5)]}
    # 1d (critic A #4): brass join fills at most 4 dB, held at most 0.15 s
    EARLY_FILL_CAP = {"brass": (4.0, 0.15)}
    # 1b (critic A #1): the theme's body and tail lifts end on the next note's score onset (-20 .. +20 ms), not on its
    # moved note-on (which lies 50-110 ms earlier and cut the end of the note before)
    if _os56.environ.get("C56_BODYEND", "1") == "1":
        for t_, sps_ in STEADY_LINE.items():
            for sp_ in sps_:
                if "Marc" in sp_["art"]:
                    sp_["body_end_score"] = (-0.02, 0.02)
    # 1a (critic C #1, variant T): the theme's eighths at one common level. In these spans every note of an eighth or
    # shorter takes the median of the eighths' fitted level steps (build/steady_levels54.json plus PICKUP_LIFT) and the
    # PICKUP_LIFT rows on them go; notes of a quarter or longer keep their fitted steps. Not on Violins I 104-128
    # (simulated there: note-to-note step 2.4 -> 3.8 dB). C56_COMMON=0 keeps the per-note steps.
    _C56_COMMON = {"Violins I": [(56.0, 90.0)], "Violoncellos": [(520.0, 536.0)]}
    _st56 = {"Violins I": "VlnI", "Violins II": "VlnII", "Violas": "Vla", "Violoncellos": "Vc"}
    # Not shipped (default 0): simulated on the c55 stems, Violins I 56-90 body step 1.8 -> 2.2 dB (per-note 1.9) and
    # Violoncellos 520-536 3.0 -> 2.7 (per-note 2.2).
    if _os56.environ.get("C56_COMMON", "0") == "1":
        for t_, sp56_ in _C56_COMMON.items():
            len_ = {}
            for l_ in open(f"{BUILD}/mockup-events.tsv"):
                c_ = l_.rstrip("\n").split("\t")
                if c_[0] == _st56[t_] and c_[3] == "note":
                    len_[round(float(c_[1]), 3)] = float(c_[5])
            for a_, e_ in sp56_:
                for sp_ in STEADY_LINE.get(t_, []):
                    if not (sp_["from"] <= a_ and e_ <= sp_["to"] + 1.0) or not sp_.get("level_db"):
                        continue
                    ks_ = [k_ for k_ in sp_["level_db"] if a_ <= float(k_) < e_ and len_.get(round(float(k_), 3), 9) <= 0.5 + 1e-6]
                    if len(ks_) < 2:
                        continue
                    pl_ = PICKUP_LIFT.get(t_, {})
                    tot_ = sorted(float(sp_["level_db"][k_]) + sum(v_ for q_, v_ in pl_.items() if abs(q_ - float(k_)) < 0.01) for k_ in ks_)
                    med_ = round(tot_[len(tot_) // 2] if len(tot_) % 2 else 0.5 * (tot_[len(tot_) // 2 - 1] + tot_[len(tot_) // 2]), 1)
                    sp_["level_db"] = dict(sp_["level_db"], **{k_: med_ for k_ in ks_})
                    PICKUP_LIFT[t_] = {q_: v_ for q_, v_ in pl_.items() if not any(abs(q_ - float(k_)) < 0.01 for k_ in ks_)}
                    print(f"C56 common level {t_} {a_:g}-{e_:g}: {len(ks_)} eighths at {med_:+.1f} dB (were {tot_[0]:+.1f} .. {tot_[-1]:+.1f})", file=__import__("sys").stderr)
    # 3 (critic C #3): crescendos that fell on their own stem (per-quarter stem levels, cycles/c56/actor_scripts/hpq56.py)
    LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [[(72.0, 0.0), (75.0, 3.2), (76.0, 5.5), (76.95, 6.5), (77.05, 0.0)]]
    LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES.get("Horn 1", []) + [[(410.95, 0.0), (411.0, 5.5), (411.5, 5.5), (411.55, 0.0)],
                                                             [(414.95, 0.0), (415.0, 3.5), (415.9, 3.5), (416.0, 0.0)]]
    LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES.get("Violoncellos", []) + [[(601.0, 0.0), (602.9, 3.0), (603.0, 6.0), (603.5, 6.0), (604.0, 0.0)]]
    LEVEL_SHAPES["Flute 2"] = LEVEL_SHAPES.get("Flute 2", []) + [[(481.95, 0.0), (482.0, 5.5), (482.95, 5.5), (483.0, 1.0), (483.95, 1.0), (484.0, 0.0)]]
    # Violas 612-616: the printed diminuendo rose 4.5 dB on the stem (soft_decresc_keep 0 in mix.json gave 0.4-0.7 dB)
    LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(612.0, 0.0), (615.9, -5.0), (616.4, 0.0)]]

# ---------------------------------------------------------------------------------------------------------------------
# c57: the coordinator's decisions on critic reports A, B, C (cycles/c57/COORDINATOR-NOTES.md, last section), in its
# order. Level-only items were simulated on the c56 stems (cycles/c57/actor_scripts/) before the render. C57=0 builds
# the c56 data from these tables (the json tables of c57 stay).
import os as _os57
if _os57.environ.get("C57", "1") != "0":
    # 1a (critic A #2): the theme's per-note level steps on Violins I over-correct: per join the stem step without the
    # rule is -0.59 x the written step (123 joins). Each value v becomes m + k (v - m), m = the span's median; k 0.55 on
    # 56-160, 0.7 on 536-576. The fitted table build/steady_levels54.json stays as fitted. C57_LVK="0.55,0.7"
    _k57 = [float(x_) for x_ in _os57.environ.get("C57_LVK", "0.55,0.7").split(",")]
    _C57_LV_SPANS = {"Violins I": [(56.0, 104.0, _k57[0]), (104.0, 160.0, _k57[0]), (536.0, 576.0, _k57[1])]}
    for t_, sps57_ in _C57_LV_SPANS.items():
        lv_ = dict(_C54_LV.get(t_, {}))
        for a_, e_, k_ in sps57_:
            ks_ = [x_ for x_ in lv_ if a_ <= float(x_) < e_]
            if not ks_ or k_ == 1.0:
                continue
            vs_ = sorted(float(lv_[x_]) for x_ in ks_)
            m_ = vs_[len(vs_) // 2] if len(vs_) % 2 else 0.5 * (vs_[len(vs_) // 2 - 1] + vs_[len(vs_) // 2])
            for x_ in ks_:
                lv_[x_] = round(m_ + k_ * (float(lv_[x_]) - m_), 2)
        for sp_ in STEADY_LINE.get(t_, []):
            if sp_.get("level_db"):
                sp_["level_db"] = lv_
    # 1b (critic A #3): config level shapes whose fast edge lies inside a sounding string note (table fitted on the c56
    # stems by cycles/c57/actor_scripts/edges57.py; edges that cure a sample step are not in it and stay)
    if _os57.environ.get("C57_EDGES", "1") == "1" and _os57.path.exists(f"{BUILD}/shape_edges57.json"):
        NOTE_LEVEL["edges"] = {"tags": ["shape"], "min_db": 2.5, "max_s": 0.12, "tol_qn": 0.04,
                               "at": json.load(open(f"{BUILD}/shape_edges57.json"))}
    # 1c (critic A #1): Violins II row trims at half (body step off / half / full 2.5 / 1.3 / 2.9 dB); the Violas note
    # trims are removed in build/note_trims.json and build/accent_fits.json
    ROW_TRIM_DB = dict(ROW_TRIM_DB, **{"Violins II": {"Sus MAX": (-2.0, 80)}})
    # 1d (critic A #1): the celli's join fills at half height (82 notes: weak start 2.0 -> 2.7 dB, join holes over 6 dB
    # 8 -> 10 of 76 on the c56 stems; the fills were the largest movement inside 28 celli notes)
    EARLY_FILL_SCALE = {"Violoncellos": float(_os57.environ.get("C57_EF", "0.5"))}
    # 6 (critic B #3): phrases of held notes take no "drive" shape
    if _os57.environ.get("C57_MIDI", "1") == "1":   # C57_MIDI=0: only the level changes (for simulation on the c56 stems)
        PHRASE_SHAPE["types"]["drive_max_mean_qn"] = 2.0
    # 7 (critic B #5): legato targets after a Sus-row note that spoke 0.3-0.6 s late in c56 with the MIDI of c55
    if _os57.environ.get("C57_MIDI", "1") == "1":
        SHORT_SUS_AT = {**SHORT_SUS_AT, "Violoncellos": SHORT_SUS_AT.get("Violoncellos", []) + [408.0],
                        "Violins II": SHORT_SUS_AT.get("Violins II", []) + [404.5]}

# ---------------------------------------------------------------------------------------------------------------------
# c57 method change (Dan through the coordinator, 2026-11-11 16:27 / 16:30 UTC: "i want to nuke all the volume
# adjustments per note"): the track volume envelope carries slow balance only. Every per-note rule's items are left out
# on every track; config level shapes stay only as phrase-level rows (2 s or more over two or more onsets). This makes
# 1a-1d above, the per-pitch / per-note trim tables, the fitted accents, fills, lifts and dips inert in the envelope
# (their tables stay on disk). Faults are fixed on the instrument side or listed (cycles/c57/CHANGES.md). C57_SLOW=0
# builds with the per-note layers.
if _os57.environ.get("C57", "1") != "0" and _os57.environ.get("C57_SLOW", "1") == "1":
    VOL_SLOW_ONLY = {
        "drop": ["accent", "acc_body", "marc", "early", "cresc_front", "synco", "pair", "tenuto", "rep_dip", "detach_dip",
                 "steady_body", "rebow", "loop", "notch", "breath", "swell", "sost", "held_decresc", "keep:note",
                 "keep:bloomv", "ptrim", "ntrim", "metric", "pickup", "rowtrim", "steady_level", "ptop", "mt_alt", "uni",
                 "park", "arrival", "pre", "timp_restrike"],   # the timpani patch has no CC11: its dynamics (tag "timp") stay
        "slow_tags": ["shape"], "slow_min_s": 2.0, "slow_min_onsets": 2}
    NOTE_LEVEL = None
    if _os57.environ.get("C57_KEEP"):   # test builds only: rules left in the envelope (the carry fit keeps "ptrim": the
        VOL_SLOW_ONLY["drop"] = [x_ for x_ in VOL_SLOW_ONLY["drop"] if x_ not in _os57.environ["C57_KEEP"].split(",")]   # pitch trims live in Opus now)
    # the mean level the dropped layers gave each 4-bar block (2 dB or more), fitted on the c56 stems by
    # cycles/c57/actor_scripts/balance57.py: without it the theme stood 14 dB over the celli (its fitted per-note levels
    # averaged -8 dB) and every track with pitch or row trims moved against the others
    if _os57.environ.get("C57_CARRY", "1") == "1" and _os57.path.exists(f"{BUILD}/balance57.json"):
        VOL_SLOW_ONLY["carry"] = {k_: v_ for k_, v_ in json.load(open(f"{BUILD}/balance57.json")).items() if not k_.startswith("_")}
    # repeated notes: a real note-off gap (reference median: winds 60, strings 90, brass 100 ms) in place of the
    # repeated-note dips (C57_GAP=0: off, for the range test)
    if _os57.environ.get("C57_MIDI", "1") == "1" and _os57.environ.get("C57_GAP", "1") == "1":
        REP_MIN_GAP = {"string": 0.09, "wind": 0.065, "brass": 0.10, "frac": 0.4, "min_ioi_s": 0.15}
    # the theme on a row that sustains (the body lifts are gone): C57_THEME=sus plays the Violins I one-row spans on
    # Sus MAX with one lead per class (slurred / new bow / after a rest / same-pitch repeat), fitted in one step on a
    # range render (old lead + median S of the class, the finale's c15 method): build/steady_leads57.json. The per-onset
    # rows of build/steady54.json were fitted for Sus Marc LITE and are not used on it. Shipped value: see CHANGES.md
    _C57_THEME = _os57.environ.get("C57_THEME", open(f"{BUILD}/theme_row57.txt").read().strip() if _os57.path.exists(f"{BUILD}/theme_row57.txt") else "marc")
    if _C57_THEME == "sus":
        _ld57 = {"slur": 0.065, "tongue": 0.035, "first": 0.071, "rep": 0.05}
        if _os57.path.exists(f"{BUILD}/steady_leads57.json") and _os57.environ.get("C57_LEADS", "1") == "1":
            _ld57.update(json.load(open(f"{BUILD}/steady_leads57.json")).get("Violins I", {}))
        # per-onset leads on top of the class leads (second step: lead + 0.8 x S where S is 12 ms or more off, fitted on
        # range renders of all three spans, cycles/c57/actor_scripts/fitat57.py): build/steady57_at.json
        _at57 = json.load(open(f"{BUILD}/steady57_at.json")).get("Violins I", {}) if (_os57.path.exists(f"{BUILD}/steady57_at.json") and _os57.environ.get("C57_AT", "1") == "1") else {}
        STEADY_LINE["Violins I"] = [
            {"art": "Sus MAX", "lead_s": _ld57["slur"], "tongue_lead_s": _ld57["tongue"], "first_lead_s": _ld57["first"],
             "rep_lead_s": _ld57["rep"], "overlap_s": 0.0, "gap_s": 0.03, "rep_gap_s": 0.09, "rr_reset": True,
             "from": sp_["from"], "to": sp_["to"], "at": _at57, "level_db": {},
             **({"max_len_qn": sp_["max_len_qn"]} if "max_len_qn" in sp_ else {})}
            for sp_ in STEADY_LINE.get("Violins I", [])]

# ---------------------------------------------------------------------------------------------------------------------
# c58: the coordinator's decisions on critic reports A, B, C (cycles/c58/COORDINATOR-NOTES.md, last section), in its
# order. Dan's rule, second cycle: no per-note level or shape on the track volume envelope and no level rows fitted to
# earlier renders. C58=0 builds the c57 data (with build/balance57.json restored from cycles/c58/before).
import os as _os58
if _os58.environ.get("C58", "1") != "0":
    _on58 = lambda k_: _os58.environ.get(k_, "1") == "1"
    # 1. The carry rows are deleted (build/balance57.json is no longer in build/; nothing is fitted in their place).
    VOL_SLOW_ONLY.pop("carry", None)
    #    c: kept "slow" shapes with a per-note edge inside (any segment over 3 dB/s) are dropped (decision 3, C #2);
    #    d: timpani and harp have no CC11: their shapes stay by 4 s / one onset. On the CC11 tracks a shape on one held
    #    note and a role row over fewer than three notes leave the envelope; those of 4 s or more become CC11 offsets
    #    (strings 0.30, winds 0.21, brass 0.29 dB per unit: kit LEARNINGS section 4, loop LEARNINGS c51)
    VOL_SLOW_ONLY.update({"slow_max_db_s": 3.0, "slow_no_cc": {"families": ("timp", "harp"), "min_s": 4.0, "min_onsets": 1}})
    if _on58("C58_L2C"):
        LEVEL_TO_CC = {"db_per_cc": {"string": 0.30, "wind": 0.21, "brass": 0.29}, "min_s": 4.0, "max_db_s": 3.0,
                       "min_cc": 12, "role_note_min": 3}
    #    d: the unison boost (+3 dB, two players on one sample) as one span per run of three or more kept notes
    UNI_ROLE = {"min_notes": 3, "rest_s": 0.08, "ramp_qn": 0.5, "slow_s": 1.0}
    #    a: the -3 dB fall of a diminuendo on one held note goes into the hairpin's CC11 end value
    HELD_DECRESC_CC = {"string": 10, "wind": 14}
    #    a: the swell cap's envelope half is gone (rule "pre" is dropped); the cap itself stays (it keeps the low winds
    #    on one sample layer), so the capped swells of Bassoon 1 / 2 stay 2-3 dB short: listed in CHANGES.md
    SWELL_CAP_TO_VOL_DB_PER_CC = {}
    # 2. B #2: the parked CC11 of the string shorts had its level return in the envelope: off, CC11 follows the dynamic
    SHORT_CC11_PARK = None
    # 3. C #2: hairpin-gain release over 4 qn (1.9 s at 126) in place of 1 qn; role ramps out of sounding notes
    HP_REL = 4.0
    ROLE_EDGE = {"rest_s": 0.1, "reach_qn": 2.0, "slow_s": 2.0}
    # 4. C #1, #3: timing
    #    Violins II and Violas play the repeated quarters under the theme (bars 23-25, 135-137) on the c54 Marc spec
    if _on58("C58_MARC"):
        for t_ in ("Violins II", "Violas"):
            STEADY_LINE[t_] = STEADY_LINE[t_] + [dict(STEADY_LINE[t_][0], **{"from": a_, "to": e_})
                                                 for a_, e_ in ((88.0, 100.0), (536.0, 548.0))]
    RETONGUE_LEAD_S = dict(RETONGUE_LEAD_S, **{"Double basses": 0.06})
    #    the theme's same-pitch repeats: 60 ms gap (the 152 ms leads at 60 and 572 are deleted in steady57_at.json)
    STEADY_LINE["Violins I"] = [dict(sp_, rep_gap_s=0.06) for sp_ in STEADY_LINE["Violins I"]]
    # 5. A #2 option N: no split of notes up to 5.2 s (the Lento whole notes of 4.7-5.0 s were cut in two); C #4: the
    #    top voices hold one bow through the last chord, CC11 carries the morendo
    REBOW_MAX_S = 5.2
    REBOW_SKIP_UNDER_S = 5.2
    REBOW_NONE = {"Violins I": [(719.5, 729.0)], "Violins II": [(719.5, 729.0)]}
    FINAL_CC_FADE = {"from": 724.0, "to": 727.0, "cc": 14}
    # 6. A #1: resting ff at CC11 104 (strings, winds) / 100 (brass), made up by the ff dynamic trim in mix.json; an
    #    accent of 0.3 s or more at f or louder is one flat CC11 rise for the note's whole length (values below). Not on the Marc row (it has its own front) or on the velocity rows
    if _on58("C58_ACC"):
        _rm58 = [(88, 88), (114, 104), (124, 124), (127, 127)]
        CC11_REMAP = {"string": _rm58, "wind": _rm58, "brass": [(88, 88), (114, 100), (124, 124), (127, 127)]}
        _sk58 = ("Sus Marc", "Stac", "Spic", "Pizz", "Marc Shrt", "Staccatissimo", "Tremolo", "Trem")
        # Dan on the finale's accents (+2.1 to +4.1 dB): "a little bit over done". Aim here: +1.5 to +2 dB, none over
        # +2.5, from critic A's CC11-to-level table (cycles/c58/reports/A.md): strings f 88 -> 95, ff 104 -> 117; winds
        # f 88 -> 105 (88-98 is a plateau on the winds), ff 104 -> 114; brass f 88 -> 101, ff 100 -> 110
        ACCENT_FLAT = {"string": {"add_by_cc": [(84, 7), (88, 7), (104, 13), (127, 13)], "ceil": 118, "min_s": 0.3, "min_cc": 84, "skip_arts": _sk58},
                       "wind": {"add_by_cc": [(84, 17), (88, 17), (104, 10), (127, 10)], "ceil": 116, "min_s": 0.3, "min_cc": 84, "skip_arts": _sk58},
                       "brass": {"add_by_cc": [(84, 13), (88, 13), (100, 10), (127, 10)], "ceil": 112, "min_s": 0.3, "min_cc": 84, "skip_arts": _sk58}}
        # finale c18: accents on many staves at one onset add up in the family sum (+3 to +4 dB): rise x 0.75 from 9
        # accented staves, x 0.6 from 16
        # per track where critic A's table has the track's own curve: Violins I Sus MAX is flat from 88 to 98 and steeper
        # above 104 than the string family (f 88 -> 101, ff 104 -> 113)
        ACCENT_FLAT["Violins I"] = dict(ACCENT_FLAT["string"], add_by_cc=[(84, 13), (88, 13), (104, 9), (127, 9)])
        for f_ in ACCENT_FLAT:
            ACCENT_FLAT[f_]["tutti_scale"] = [(9, 0.75), (16, 0.6)]
    # 7. A #4: legato overlap in seconds; the tied syncopations of bars 16-21 that follow a gap start on Sus MAX
    if _on58("C58_OVL"):
        LEG_OVERLAP_S = {"string": 0.06, "wind": 0.045, "brass": 0.045}
    SUS_ENTRY_AT = {"Violins II": [62.5, 68.5, 70.5, 76.5, 82.5], "Violas": [62.5, 68.5, 70.5]}
    # 8. A #3: the contrabassoon's remaining Sus MAX repeats on its repetition row
    REP_ROW = dict(REP_ROW, **{"Contrabassoon": REP_ROW.get("Contrabassoon", []) + [(535.9, 544.1, "LegRep RRx4"), (631.9, 632.1, "LegRep RRx4")]})
    # 10. B #6: celli 526 (Marc row) at its neighbours' velocity
    VEL_SET = {**VEL_SET, "Violoncellos": {**VEL_SET.get("Violoncellos", {}), 526.0: 91}}
    #     C #6: Trumpet 2 started 45-69 ms before the tutti at seven arrivals with its 90 ms loud entry lead
    ENTRY_LEAD_S = dict(ENTRY_LEAD_S, **{"Trumpet 2": (0.06, 0.06, 0.05)})
    # 8. A #3 (range test, C58_CB_RR=1): a round-robin reset before every beat of the basses' repeated eighths, so each
    #    beat / off-beat pair plays takes 1 and 2 (the off-beats stood 2-5 dB over the beats). Shipped value: CHANGES.md
    if _os58.environ.get("C58_CB_RR", open(f"{BUILD}/cb_rr58.txt").read().strip() if _os58.path.exists(f"{BUILD}/cb_rr58.txt") else "0") == "1":
        _cb58 = [float(q_) for a_, b_ in ((104, 124), (324, 328), (520, 532), (560, 566), (664, 676)) for q_ in range(a_, b_)]
        RR_RESET_AT = dict(RR_RESET_AT, **{"Double basses": sorted(set(RR_RESET_AT.get("Double basses", [])) | set(_cb58))})
    # 5. A #2 option A on one instance (range test, C58_RBOV=1): the re-bow pieces alternate between MIDI channels 1 and
    #    2 and overlap by 0.4 s. Shipped value: build/rbov58.txt, CHANGES.md
    if _os58.environ.get("C58_RBOV", open(f"{BUILD}/rbov58.txt").read().strip() if _os58.path.exists(f"{BUILD}/rbov58.txt") else "0") == "1":
        REBOW_OVERLAP = {"s": 0.4, "max_frac": 0.45, "leg_ok": _os58.environ.get("C58_RBOV_LEG", "1") == "1"}

# ---------------------------------------------------------------------------------------------------------------------
# c59: the coordinator's decisions on critic reports A, B, C (cycles/c59/COORDINATOR-NOTES.md, last section), in its
# order. Dan's rule, third cycle: the envelope stays as c58 left it (no per-note item, no fitted row); what lost a shape
# is written in the instrument (one CC11 lane or flat offset per phrase, rows, region gains, gaps). C59=0 builds the
# c58 data (with build/mix.json and build/roles.json restored from cycles/c59/before).
import os as _os59
if _os59.environ.get("C59", "1") != "0":
    _on59 = lambda k_: _os59.environ.get(k_, "1") == "1"
    _flat59 = lambda a_, b_, u_: [(a_ - 0.02, 0.0), (a_, u_), (b_, u_), (b_ + 0.02, 0.0)]
    # 1. Cello solo bars 171-174 (B #3, C #1): region gains in mix.json; one CC11 lane for the phrase. Two lanes were
    #    range-rendered (C59_SOLO=B / C); the shipped one is named in build/solo_lane59.txt and CHANGES.md
    _SOLO59 = {
        "B": [(679.90, 62), (683.35, 78), (683.89, 76), (686.73, 76), (687.0, 82), (690.78, 82), (691.86, 88), (692.5, 88),
              (693.0, 80), (693.82, 64), (695.5, 50), (696.0, 50)],
        "C": [(679.90, 56), (683.35, 70), (683.89, 76), (689.81, 76), (691.86, 96), (692.3, 96), (693.82, 70), (696.0, 58)],
        # after the range renders of B and C (cycles/c59/CHANGES.md): see the file for how D was derived
        "D": json.load(open(f"{BUILD}/solo_lane59.json")) if _os59.path.exists(f"{BUILD}/solo_lane59.json") else None}
    _solo59 = _os59.environ.get("C59_SOLO", open(f"{BUILD}/solo_lane59.txt").read().strip() if _os59.path.exists(f"{BUILD}/solo_lane59.txt") else "B")
    if _solo59 in _SOLO59 and _SOLO59[_solo59]:
        ALIAS_TRACKS["Cello solo"]["set"] = dict(ALIAS_TRACKS["Cello solo"].get("set", {}), CC11_LANE=[_SOLO59[_solo59]])
    # 2. Horn 4 (B #2): its p plays above the weak soft layer. The dynamic layers of the horn patch are crossfaded by
    #    CC1, so the printed level is remapped before CC1_DYN_MAP as well as in CC11 (B's map names CC11 only)
    if _on59("C59_HN4"):
        _hn4 = [(8, 8), (22, 44), (34, 50), (46, 56), (58, 62), (72, 72), (88, 88)]   # (8, 8): a morendo still dies away
        CC11_REMAP = dict(CC11_REMAP, **{"Horn 4": _hn4 + [(114, 100), (124, 124), (127, 127)]})
        CC1_BASE_REMAP = {"Horn 4": _hn4}
    # 3. Solo and melody shapes in CC11 (B #1 / #4 tables, C #4). Role rows of one or two notes that start after a rest
    #    or on a printed dynamic are converted from 0.5 s on, on each track's own level curve
    LEVEL_TO_CC = dict(LEVEL_TO_CC, after_rest_min_s=0.5, rest_s=0.1, max_units=12, max_units_down=36, moved_edges=True, ceil={"brass": 116, "wind": 120, "string": 120},
                       curves={k_: v_ for k_, v_ in json.load(open(f"{BUILD}/cccurve59.json")).items() if not k_.startswith("_")})
    CC11_ADD = {
        # Horn 1 bars 103-104 (mf solo with Bassoon 1): +8 units over the phrase; bar 111: the crescendo starts at 52
        "Horn 1": [_flat59(411.86, 415.76, 5),   # 8 units in the first range render: B-flat 4 +6.5, A4 +6.8 dB
                   [(439.8, 0), (439.86, 6), (444.0, 2), (447.8, 0)],
                   # C #4: bars 43-44 (C5 at 171, +2.8 dB), bar 147 (D4 and C4 at 587.5-589, +3.5 dB), flat from the
                   # note-on of the first to the note-on of the note after the last
                   _flat59(170.78, 173.85, 5), _flat59(587.38, 588.79, 7)],
        # Clarinet 1 bars 45-46, 105 and 127: +8 units (the offset starts in the rest before the phrase)
        "Clarinet 1": [_flat59(175.8, 183.02, 8), _flat59(416.3, 418.45, 8), _flat59(504.3, 507.9, 8)],
        # Cor anglais bar 7: the hairpin starts at 74 instead of 66, crest unchanged at 87
        "Cor anglais": [[(23.88, 0), (23.915, 8), (25.9, 0)]],
        # Bass clarinet bar 109: the low F2 pickup (5-8 dB under the middle register at one CC11)
        "Bass clarinet": [_flat59(432.2, 432.88, 16)],
        # B #4 rows that the after-rest rule does not reach. Horn 3 under Horns a2 (bar 42): 100 -> 60 becomes 84 -> 54
        "Horn 3": [[(164.85, 0), (164.87, -16), (167.9, -6), (167.95, 0)]],
        # Trumpet 3 bars 115-116 (a row of -3 dB): 87 -> 100 becomes 80 -> 81 (the trumpets are flat from 88 to 104)
        "Trumpet 3": [[(455.87, 0), (455.89, -7), (459.88, -19), (463.9, -19), (463.92, 0)]],
    }
    # 5. the theme (C #3): the Sus MAX row falls more steeply under CC11 88 than the rows the dynamic map was made
    #    for; the diminuendo of bars 21-22 ends at 84 instead of 73 (62 at the last note's end -> 79)
    #    Range render: with 73 -> 84 the line fell 3.8 dB over 82-86 (c58 12.6, c56 5.7, c53 7.0): the row gives about
    #    0.85 dB per unit here, so the end value is 80 (62 -> 71)
    CC11_FLOOR = {"Violins I": [(82.0, 94.0, [(60, 71), (73, 80), (90, 90), (127, 127)])],
                  # 10. A #4: the tremolo row falls about 15 dB further than the legato row over one CC11 fall
                  "Violas": [(160.0, 167.98, 45)]}
    # 6. Accents (A #1): per-track CC11 targets for an isolated accent of +1.5 to +2 dB (f from 88 / ff from the
    #    resting value), ceilings 120 / 122 / 118, no staff-count scaling, none on a note that carries an sf
    if _on59("C59_ACC"):
        _acc59 = {  # track: (f target from 88, ff target, resting ff)
            "Flute 1": (103, 116, 104), "Flute 2": (103, 115, 104), "Oboe 1": (101, 119, 104), "Oboe 2": (103, 122, 104),
            "Cor anglais": (103, 116, 104), "Clarinet 1": (108, 122, 104), "Clarinet 2": (101, 116, 104),
            "Bass clarinet": (103, 112, 104), "Bassoon 1": (107, 115, 104), "Bassoon 2": (101, 115, 104),
            "Contrabassoon": (99, 112, 104), "Horn 1": (97, 116, 100), "Horn 2": (95, 116, 100), "Horn 3": (105, 107, 100),
            "Horn 4": (98, 116, 100), "Trumpet 1": (98, 116, 100), "Trumpet 2": (105, 116, 100), "Trumpet 3": (108, 116, 100),
            "Trombone 1": (100, 116, 100), "Trombone 2": (93, 116, 100), "Bass trombone": (94, 116, 100), "Tuba": (95, 108, 100),
            "Violins I": (94, 116, 104), "Violins II": (93, 110, 104), "Violas": (93, 116, 104), "Violoncellos": (95, 116, 104),
            "Double basses": (96, 116, 104), "Horns a2": (98, 116, 100)}
        _fam59 = {n_: f_ for n_, _s, _p, f_, *_r in TRACKS}
        _ceil59 = {"string": 120, "wind": 122, "brass": 118}
        for f_ in ("string", "wind", "brass"):
            ACCENT_FLAT[f_] = dict(ACCENT_FLAT[f_], ceil=_ceil59[f_], skip_sf=True)
            ACCENT_FLAT[f_].pop("tutti_scale", None)
        for t_, (f88_, ff_, rest_) in _acc59.items():
            ACCENT_FLAT[t_] = dict(ACCENT_FLAT[_fam59[t_]], add_by_cc=[(84, f88_ - 88), (88, f88_ - 88), (rest_, ff_ - rest_), (127, ff_ - rest_)])
        # sf (78.0 Violins I / II, 160.0 on 20 staves): a top value per family in place of the ff arrival (finished
        # CC11 96 strings, 110 winds, 102 brass; the values here are before CC11_REMAP)
        _sf59 = {"string": 101.0, "wind": 117.0, "brass": 114.8}
        SF_TOP = {s_: _sf59[f_] for n_, st_, _p, f_, *_r in TRACKS if f_ in _sf59 for s_ in st_}
        # fp (128.0 basses): the forte held 0.24 s, at p by 0.43 s (the basses' Sus MAX peaks 140 ms after the note-on)
        FP_SPIKE = ("f", 0.5, 0.9)
    # 7. Re-bows (A #2), config only
    if _on59("C59_RB"):
        # REBOW_NONE would also take the printed bow changes at 32, 36 and 40 out of the violas' tied C4 (one bow of
        # 14 qn in the first build), so the three automatic points inside the whole notes are unlisted instead
        REBOW_NONE = dict(REBOW_NONE, **{"Double basses": [(722.7, 729.0)],
                                         "Violins I": REBOW_NONE.get("Violins I", []) + [(707.5, 715.5)]})
        REBOW_AT = dict(REBOW_AT, **{"Violoncellos": [q_ for q_ in REBOW_AT["Violoncellos"] if not 286.0 < q_ < 300.0] + [295.0],
                                     "Violas": [q_ for q_ in REBOW_AT["Violas"] if not (28.0 < q_ < 42.0 and abs(q_ - round(q_)) > 0.01)]})
        REBOW_AT["Violoncellos"].sort()
        SUS_ENTRY_AT = dict(SUS_ENTRY_AT, **{"Violins I": [720.0]})
    # 8. String shorts (A #3): row volumes in mix.json; celli bars 85-87 velocity 77 -> 68
    VEL_SET = {**VEL_SET, "Violoncellos": {**VEL_SET.get("Violoncellos", {}), **{q_: 68 for q_ in (338.5, 339.0, 339.5, 343.5, 344.0, 345.0, 346.0, 347.0)}}}
    # 9. C #5: a printed same-pitch repeat between two held string notes is a bow change, not a separated repeat
    if _on59("C59_HELD"):
        REP_MIN_GAP = dict(REP_MIN_GAP, held_s=1.0, held_gap={"string": 0.03})
    # 10. Join holes (A #4): a soft tongued wind join keeps 15 ms; Flute 1 634 at its neighbour's velocity; the Violins
    #     II Marc doubling ends at 572
    WIND_DETACH = dict(WIND_DETACH, soft={"max_cc": 60, "gap_s": 0.015, "families": ("wind",)})
    VEL_SET = {**VEL_SET, "Flute 1": {**VEL_SET.get("Flute 1", {}), 634.0: 100}}
    STEADY_LINE["Violins II"] = [dict(sp_, to=572.0) if abs(sp_["from"] - 552.0) < 0.01 else sp_ for sp_ in STEADY_LINE["Violins II"]]

# ---------------------------------------------------------------------------------------------------------------------
# c60: the coordinator's decisions on critic reports A, B, C (cycles/c60/COORDINATOR-NOTES.md, last section), in its
# order. Dan's rule, fourth cycle: no per-note level or shape on the track volume envelope, no fitted level row; an
# accent is one flat CC11 value for the note's length. C60=0 builds the c59 data (with build/mix.json, roles.json,
# entry_leads.json and retongue_leads.json restored from cycles/c60/before).
import os as _os60
if _os60.environ.get("C60", "1") != "0":
    _on60 = lambda k_: _os60.environ.get(k_, "1") == "1"
    _flat60 = lambda a_, b_, u_: [(a_ - 0.02, 0.0), (a_, u_), (b_, u_), (b_ + 0.02, 0.0)]

    def _rm60(t_, x0_, d_):
        """drop the LEVEL_SHAPES row of a track that starts at x0_ and steps to d_ dB"""
        r_ = [s_ for s_ in LEVEL_SHAPES.get(t_, []) if not (abs(s_[0][0] - x0_) < 1e-6 and abs(s_[1][1] - d_) < 1e-6)]
        assert len(r_) < len(LEVEL_SHAPES.get(t_, [])), (t_, x0_, d_)
        LEVEL_SHAPES[t_] = r_
    # 1. Rule breaches still on the envelope (B #2, B #5, C #4)
    #    the two rows fitted to the c26 / c47 renders on the celli's strokes 345-347 (-7.5 dB together), the +1 dB row on
    #    the one tremolo note at 484, the +2.5 dB row on three Cor anglais strokes: deleted
    _rm60("Violoncellos", 343.45, -4.0); _rm60("Violoncellos", 343.44, -3.5); _rm60("Violoncellos", 484.25, 1.0)
    ALIAS_TRACKS["Cor anglais stac"]["tables"]["LEVEL_SHAPES"] = [s_ for s_ in ALIAS_TRACKS["Cor anglais stac"]["tables"]["LEVEL_SHAPES"]
                                                                  if not (abs(s_[0][0] - 367.3) < 1e-6 and abs(s_[1][1] - 2.5) < 1e-6)]
    #    Violas 244.1-248.7 (critic B: -8.7 dB): the fall is the end of the two crescendo ramps (+4, +3) at the printed
    #    subito and the -3 dB row LEVEL_SHAPES["_all"] that every track has over the printed sub. p bar: section
    #    dynamics with its edges on a printed dynamic, kept
    #    Bass clarinet bars 107-108 (+2.5 dB over nine notes): in CC11 on its own curve (0.39 dB per unit at 34-46)
    _rm60("Bass clarinet", 424.4, 2.5)
    #    fugato subject, celli alone, bars 85-87: CC11 flat at the printed mf (the lane fell 72 -> 62 with nothing
    #    printed), the accent at 342 one flat value (+5 units: 0.41-0.45 dB per unit), the strokes by velocity.
    #    C60_FUG = B (critic B's velocities, and the mp C4 at 348 at 68) or C (critic C's): range-rendered, the shipped
    #    one is named in build/fug60.txt
    _fug60 = _os60.environ.get("C60_FUG", open(f"{BUILD}/fug60.txt").read().strip() if _os60.path.exists(f"{BUILD}/fug60.txt") else "B")
    CC11_LANE = dict(CC11_LANE, **{"Violoncellos": CC11_LANE.get("Violoncellos", []) + [
        [(336.36, 72), (341.72, 72), (341.75, 77), (343.40, 77), (343.44, 72), (347.70, 72)]]})
    _fv60 = {"B": {338.5: 60, 339.0: 60, 345.0: 62, 346.0: 62, 347.0: 52}, "C": {345.0: 56, 346.0: 56, 347.0: 50}}[_fug60]
    VEL_SET = {**VEL_SET, "Violoncellos": {**VEL_SET.get("Violoncellos", {}), **_fv60}}
    #    Timpani: the +6 dB attack shape on every f / ff stroke is gone; the stroke's weight is its velocity
    TIMP_LOUD_ATTACK_DB = 0.0
    TIMP_STROKE_VEL = [(22, 52), (34, 56), (46, 64), (58, 72), (72, 80), (88, 112), (114, 127)]
    # 2. Climax order (C #1, B #1): trims and roles in mix.json / roles.json. Violins I tremolo 484-492: the -4 dB
    #    role became CC11 125 -> 99, which costs 7.8 dB on the Tremolo row: +13 units. Timpani roll into bar 160: CC7
    #    end 76 -> 84 (+1.8 dB on the roll's own level, back before the fff stroke)
    TIMP_ROLL_DB_ADD = [[(632.0, 0.0), (635.9, 1.8), (635.97, 0.0)]]
    #    the trumpets' rows over the two whole notes of bars 122-123 (5.5 s) stay on the envelope as slow rows: their
    #    CC11 is at 124 there, so the c59 conversion to CC11 played nothing (Trumpet 1 5 dB under Horns 1-2)
    LEVEL_TO_CC = dict(LEVEL_TO_CC, keep_env={t_: [(484, 492.5)] for t_ in ("Trumpet 1", "Trumpet 2", "Trumpet 3")})
    # 3. A #3: the dynamic trim ramps over a hairpin that joins its arrival (mix.json decresc_ramp); the c59 floor on
    #    the violas' tremolo is removed (C60_VAFL: a floor value for the range test, 0 = none); a diminuendo that runs
    #    into its arrival note ends at the arrival's CC11, not under it
    _vafl60 = int(_os60.environ.get("C60_VAFL", open(f"{BUILD}/vafl60.txt").read().strip() if _os60.path.exists(f"{BUILD}/vafl60.txt") else "0"))
    CC11_FLOOR = dict(CC11_FLOOR, **{"Violas": [r_ for r_ in CC11_FLOOR.get("Violas", []) if abs(r_[0] - 160.0) > 1e-6]
                                     + ([(164.0, 167.98, _vafl60)] if _vafl60 else []),
                                     "Oboe 1": [(166.0, 168.02, 34)], "Bassoon 2": [(262.0, 268.02, 43)],
                                     "Contrabassoon": [(164.0, 168.02, 46)], "Bassoon 1": [(496.0, 500.12, 50)],
                                     "Double basses": [(28.0, 32.02, 40)]})
    # 4. Second theme, bars 47-54 and 147-154 (C #2): one lane per statement on the celli and Horn 1 (the horn's CC1
    #    layer moves with it); the celli's Leg BC MAX row -4 dB in mix.json
    if _on60("C60_TH2"):
        _vc60 = [(184, 72), (187.5, 86), (188, 78), (189, 80), (191, 92), (192, 84), (195, 84), (196, 96), (198, 82), (201, 86),
                 (203, 98), (204, 96), (206, 80), (211.5, 80), (212, 73), (216, 59)]
        _h160 = [(184, 62), (187.5, 76), (188, 68), (189, 66), (191, 80), (192, 74), (195, 74), (196, 82), (198, 72), (201, 76),
                 (203, 78), (204, 80), (206, 66), (208, 58)]
        CC11_LANE = dict(CC11_LANE, **{"Violoncellos": CC11_LANE.get("Violoncellos", []) + [_vc60, [(q_ + 400, v_) for q_, v_ in _vc60]],
                                       "Horn 1": CC11_LANE.get("Horn 1", []) + [_h160, [(q_ + 400, v_) for q_, v_ in _h160]]})
        CC11_LANE_CC1 = ("Horn 1",)
    # 5. Other hairpins (C #3) and balance items (B list), flat offsets or changed hairpin ends
    _add60 = dict(CC11_ADD)
    #    Horn 1 bars 103-104: each hairpin starts 6 units lower and arrives higher (the c59 +5 stays on the D4); bar
    #    111: 52 -> 64 -> 70
    _add60["Horn 1"] = [[(407.90, 0), (407.92, -6), (411.20, 6), (411.84, 6), (411.86, 5), (412.86, 5), (412.88, -1), (414.85, 9), (415.74, 9), (415.78, 0)],
                        [(439.8, 0), (439.86, 6), (444.0, 6), (447.8, 1), (448.4, 0)],
                        _flat59(170.78, 173.85, 5), _flat59(587.38, 588.79, 7)]
    #    Horn 3 under Horns a2 (bar 42): 84 -> 54 becomes 78 -> 54; Trumpet 3 bars 115-116: 80 -> 81 becomes 73 -> 74
    _add60["Horn 3"] = [[(164.85, 0), (164.87, -22), (167.9, -6), (167.95, 0)]]
    _add60["Trumpet 3"] = [[(455.87, 0), (455.89, -14), (459.88, -26), (463.9, -26), (463.92, 0)]]
    #    basses bar 90, printed mf -> f: the hairpin starts at the mf (72) instead of 80
    _add60["Double basses"] = _add60.get("Double basses", []) + [[(357.72, 0), (357.74, -8), (359.74, 0)]]
    #    Clarinet 1 pp F4 bar 145: 12 -> 17; bar 177: the B4 starts at 54 (10. B); Bass clarinet bars 107-108 +6 units
    #    (the deleted +2.5 dB row), D3 in bar 177 34 -> 27 (10. B)
    _add60["Clarinet 1"] = _add60.get("Clarinet 1", []) + [_flat60(575.9, 582.0, 5), [(705.86, 0), (705.88, 6), (707.5, 0)]]
    _add60["Bass clarinet"] = _add60.get("Bass clarinet", []) + [[(424.28, 0), (424.3, 6), (432.16, 6), (432.18, 0)], _flat60(703.93, 707.83, -7)]
    #    Violins I tremolo 484-492 (item 2)
    _add60["Violins I"] = _add60.get("Violins I", []) + [_flat60(483.9, 491.95, 13)]
    #    10. B: Violas tremolo crescendo into bar 82: 84 -> 102 becomes 78 -> 96 (a slower rise from 319, no step)
    _add60["Violas"] = _add60.get("Violas", []) + [[(319.0, 0), (320.5, -6), (324.3, -6), (324.36, 0)]]
    #    B #2: the mp C4 that ends the fugato subject (348) lost its +8 dB shape: +6 units, flat (0.45 dB per unit)
    _add60["Violoncellos"] = _add60.get("Violoncellos", []) + [_flat60(347.73, 349.48, 6)]
    CC11_ADD = _add60
    #    lanes on exposed static long notes (C #5): Clarinet 2 pp D4 bar 145 (21 -> 16 with B, the sample's bulge:
    #    softer start), Violas F4 bar 93, the second piece of the celli's A-flat 3 pedal
    CC11_LANE = dict(CC11_LANE, **{"Clarinet 2": CC11_LANE.get("Clarinet 2", []) + [[(575.9, 15), (577.5, 19), (581.95, 16)]],
                                   "Violas": CC11_LANE.get("Violas", []) + [[(367.81, 88), (369.7, 94), (371.66, 86)]],
                                   "Violoncellos": CC11_LANE.get("Violoncellos", []) + [[(295.0, 34), (303.85, 28)]]})
    #    Cello solo (C #5): the lane's 70 at 683.35 is 64 (the crest C5 over the first note's end); the Port note at
    #    685 starts 0.15 s earlier (its first half beat was 8 dB under the rest of the note: the transition's time).
    #    No CC11 rise inside the note
    _solo60 = [(679.9, 48), (683.35, 64), (683.89, 76), (689.81, 76), (691.86, 96), (692.3, 96), (693.82, 70), (696.0, 58)]
    ALIAS_TRACKS["Cello solo"]["set"] = dict(ALIAS_TRACKS["Cello solo"].get("set", {}), CC11_LANE=[_solo60])
    ALIAS_TRACKS["Cello solo"]["tables"]["LEG_LEADS"] = dict(ALIAS_TRACKS["Cello solo"]["tables"]["LEG_LEADS"], **{"685.0": 0.22})   # 0.07 until c59
    # 7. Sustained tutti chord changes (A #2): the long-note form of the tongued join
    if _os60.environ.get("C60_LONG", open(f"{BUILD}/long60.txt").read().strip() if _os60.path.exists(f"{BUILD}/long60.txt") else "1") == "1":
        WIND_DETACH = dict(WIND_DETACH, long={"min_s": 0.8, "brass": 0.04, "wind": 0.03, "same_pitch_gap_s": 0.025})
    # 8. Re-bows (A #1): pieces up to 5.3 s (the sustain sample's first pass runs to 5.9 s). Listed points replace the
    #    frozen 3.1 s points on the celli (bars 3-4, 7-14, final chord), basses (bars 12-14, 72-76, pedal 116-130, final
    #    chord) and violas (final chord); every change at least 0.6 s from another section's
    if _on60("C60_RB"):
        REBOW_MAX_S, REBOW_SKIP_UNDER_S, REBOW_SEG_S = 5.3, 5.3, 4.6
        _rb60 = {"Violoncellos": ([(10.8, 16.0), (27.8, 56.0), (711.8, 728.1)], [12.7, 715.058, 718.725, 722.384, 725.441]),
                 "Double basses": ([(47.9, 55.0), (286.0, 304.0), (463.7, 520.0), (711.9, 728.1)],
                                   [51.3, 293.6, 474.014, 483.968, 493.012, 501.845, 510.538, 716.225, 720.642, 724.291, 726.491]),
                 "Violas": ([(711.7, 728.1)], [715.642, 719.475, 725.991])}
        for t_, (sp_, new_) in _rb60.items():
            REBOW_AT[t_] = sorted([q_ for q_ in REBOW_AT.get(t_, []) if abs(q_ - round(q_)) < 0.01 or not any(a_ < q_ < b_ for a_, b_ in sp_)] + new_)
        REBOW_AT["Double basses"] = [q_ for q_ in REBOW_AT["Double basses"] if abs(q_ - 720.0) > 0.01]   # the old automatic point of the final chord
        REBOW_NONE = {k_: v_ for k_, v_ in REBOW_NONE.items() if k_ != "Double basses"}
        #    printed same-pitch bow changes on a held pitch: the new bow leads (0.20 s under CC11 60, 0.12 s above)
        REP_MIN_GAP = dict(REP_MIN_GAP, held_lead_s=[(60, 0.20), (127, 0.12)])
    # 9. Timing (A #4, B #4, A #3, A #6)
    RETONGUE_LEAD_S = dict(RETONGUE_LEAD_S, **{"Double basses": 0.12})
    ENTRY_LEAD_S = dict(ENTRY_LEAD_S, **{"Oboe 2": (0.0, 0.05, 0.0), "Trumpet 2": (0.08, 0.08, 0.05)})
    PERC_MAP["Tam-tam"]["tamtam"]["delay_s"] = float(_os60.environ.get("C60_TT", "-0.08"))

# ---------------------------------------------------------------------------------------------------------------------
# c61: the coordinator's decisions on critic reports A, B, C (cycles/c61/COORDINATOR-NOTES.md, last section), in its
# order. Dan's rule, fifth cycle: no per-note level or shape on the envelope, no fitted row. The inner-line role rows
# (decision 1) are in build/roles.json (cycles/c61/actor_scripts/apply61.py); C61=0 builds the c60 data (with
# build/mix.json and build/roles.json restored from cycles/c61/before).
import os as _os61
if _os61.environ.get("C61", "1") != "0":
    _on61 = lambda k_: _os61.environ.get(k_, "1") == "1"
    _flat61 = lambda a_, b_, u_: [(a_ - 0.02, 0.0), (a_, u_), (b_, u_), (b_ + 0.02, 0.0)]
    # 1. (B #4c) Violins II pp moving voice under the violas' espr. tune, bars 107-110: +5 units (0.55 dB per unit at
    #    CC 36 on its own curve, under the p value 46: the pp layer stays)
    CC11_ADD = dict(CC11_ADD, **{"Violins II": CC11_ADD.get("Violins II", []) + [_flat61(423.9, 439.9, 5)]})
    # 2. (C #1-2) delivery ride rows: bar-170 chord, and the soft starts of the crescendos of bars 110-117 and 155-158
    #    (tools/deliver_master.py TOP_RATIO 3.0 -> 2.0)
    if _on61("C61_RIDE"):
        RIDE_TRIMS = RIDE_TRIMS + [[(675.8, 0.0), (676.0, -2.5), (679.0, -2.5), (679.9, 0.0)],
                                   [(435.5, 0.0), (436.0, -3.0), (440.0, -3.0), (448.0, -2.0), (456.0, 0.0)],   # C: (436, 0) -> (440, -3); that ramp inverted the 436-440 crescendo on the c61 mp3 (+2.4 master, -0.3 delivered): in at the printed p
                                   [(616.0, 0.0), (620.0, -2.0), (624.0, -1.0), (627.0, 0.0)]]
    # 3. (C #3, A #5) Oboe 1 bars 42-43: one phrase lane, flat across the tied G5 (no bounce at the F5), the printed
    #    diminuendo 166 -> 168. The E5 region gain (bar 146) is in mix.json
    if _on61("C61_OB"):
        CC11_LANE = dict(CC11_LANE, **{"Oboe 1": CC11_LANE.get("Oboe 1", []) + [[(164.0, 58), (165.85, 58), (167.9, 38), (168.9, 36)]]})
    # 4. (A #2) CC11 rises keyed to the moved note-on (tools/score_to_parts.py CC11_RISE_AT_MOVED, generic)
    if _on61("C61_RISE"):
        CC11_RISE_AT_MOVED = {"min_units": 8, "probe_qn": 0.15, "families": ("string", "wind", "brass")}
    # 5. (A #1) Cor anglais qn 26 G4 -> G#4 legato dip: C61_CA = a (the G#4 on Sus MAX, a soft re-attack under the
    #    slur), b (velocity 115, a faster transition) or 0; range-rendered, the shipped form named in build/ca61.txt.
    #    (A #3) celli qn 286, subito pp after the marcato strokes: Sus MAX entry (the Leg Slur first-note layer faded in
    #    over 0.8 s)
    _ca61 = _os61.environ.get("C61_CA", open(f"{BUILD}/ca61.txt").read().strip() if _os61.path.exists(f"{BUILD}/ca61.txt") else "a")
    if _ca61 == "a":
        ART_SPANS = dict(ART_SPANS, **{"Cor anglais": ART_SPANS.get("Cor anglais", []) + [{"from": 25.8, "to": 26.95, "art": "Sus MAX"}]})
    elif _ca61 == "b":
        VEL_SET = {**VEL_SET, "Cor anglais": {**VEL_SET.get("Cor anglais", {}), 26.0: 115}}
    if _on61("C61_VC286"):
        SUS_ENTRY_AT = dict(SUS_ENTRY_AT, **{"Violoncellos": SUS_ENTRY_AT.get("Violoncellos", []) + [286.0]})
    # 6. (A, fugato drop into bar 88) the celli's fugato-subject rows ended at 348 / 348.5, inside the held mp C4,
    #    while CC11 steps 78 -> 64 there: the mp was taken twice. C61_FUG = 2 (the two +3 rows run on through the
    #    countersubject to the rest at 359.9; the step at 348 is CC11's alone, the +2 row still ends at 348), 1 (only
    #    [338, 348.5, 3] runs on) or 0 (as c60); range-rendered, the shipped form named in build/fug61.txt
    _fug61 = _os61.environ.get("C61_FUG", open(f"{BUILD}/fug61.txt").read().strip() if _os61.path.exists(f"{BUILD}/fug61.txt") else "2")

    def ROLES_HOOK(r_):
        r_ = dict(r_)
        ext_ = {"2": ([336, 348, 3], [338, 348.5, 3]), "1": ([338, 348.5, 3],), "0": ()}[_fug61]
        vc_ = []
        for row_ in r_.get("Violoncellos", []):
            if any(row_ == e_ for e_ in ext_):
                row_ = [row_[0], 360.3, row_[2]]   # the end ramp 360.3-360.8 lies in the rest 359.9-360.87
            vc_.append(row_)
        r_["Violoncellos"] = vc_
        return r_

# ======================================================================================================================
# c62 (coordinator: a narrow cycle on Dan's rule of 2026-11-11, no critics): no per-note level or shape on the track
# volume envelope, on any track, for any reason. The fast moves left inside sounding notes are removed by
# build_reaper's note_slope_guard (mix.json "note_slope_guard"); these are the source changes
# (cycles/c62/edges_c61.md tags every c61 edge with its rule)
# ======================================================================================================================
# 1. POST_SHAPES_S are per-note shapes written after the subito hold (25 of the 354 c61 edges): the bar-41 sf bumps on
#    ten winds / brass and the strings (160), Violins I 78 and the f62 aliases' hall-cut shapes at 244. All removed; the
#    sf at 160 keeps its velocity and rows (the brass front there is weaker: left audible, cycles/c62/CHANGES.md)
POST_SHAPES_S = {}
for _an62 in ("Violins I f62", "Violins II f62"):
    ALIAS_TRACKS[_an62]["tables"] = {k_: v_ for k_, v_ in ALIAS_TRACKS[_an62].get("tables", {}).items() if k_ != "POST_SHAPES_S"}
# 2. Timpani, crash cymbals, tam-tam: their dynamics and ring shapes (vol_db: the timpani's per-stroke and roll levels,
#    the roll settle, the crash's ring fade-in and damp, the tam-tam's ring hold and damp) go into CC7 in the instrument
#    (tools/score_to_parts.py VOL_TO_CC7, the finale's vol_to_cc7), so the guard does not smear a stroke's level over
#    the ring of the stroke before. The shift goes to the track gain
#    The timpani's folded peak is +18.5 dB (0.05-0.25 qn swells into the strokes at 156, 300, 692 and the last roll's top
#    719.9-720); with "auto" the ppp rolls fell to CC7 2-3. Shift 12 clips those few points
VOL_TO_CC7 = {"Timpani": {"shift_db": 12.0}, "Crash cymbals": {"shift_db": "auto"}, "Tam-tam": {"shift_db": "auto"}}
# 3. Delivery under the shared spec (mockup-kit/README.md "Decision: climax margin before loudness range"): bar 122's
#    fff (a rival of the bar-160 summit, 0.25 LU under it on the c61 mp3) 2 dB lower in the delivery ride (-1 gave 0.41 LU on the c62 master); with
#    the c62 values in tools/deliver_master.py the c62 mp3 reads 160 > 122 by 0.61 LU, > 26 by 0.70, > 170 by 1.34
RIDE_TRIMS = RIDE_TRIMS + [[(483.75, 0.0), (484.0, -2.0), (487.75, -2.0), (488.25, 0.0)]]
