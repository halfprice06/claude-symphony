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

# c05 (critic C #2): the final ppp chord's held horn notes (12.8 s each, one sample) cycle in colour at the loop period
# (Horn 4: autocorrelation 0.91 at 100-300 Hz, 0.72 centroid; folded swing 19.7 dB at 100-300 Hz) after the c03 level
# profile. Staggered breaths, each piece 3.6-5.0 s (720-724 is 1.2 s/qn, 724-728 2 s/qn), the two horns 0.5-1.0 s apart;
# the Horn 4 loop profile at 720 is removed
BREATH_SPLIT_AT = {"Horn 4": {720.0: [723.0, 725.5]}, "Horn 3": {720.0: [723.5, 726.0]}}

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
