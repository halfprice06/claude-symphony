"""Movement II (mvt2/v77) score config for score_to_parts.py: the tables that were inline in score_to_parts.py
through c26. Run in score_to_parts.py's namespace (S, W, B, H, P, DYN and the defaults are available)."""
SCORE_END = 304.0

# track name, source staves, patch file, family, pan (-1..1; superseded by the seat in build/mix.json)
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
    ("Trombone 1", ["Tbn1"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.35),
    ("Trombone 2", ["Tbn2"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.4),
    ("Bass trombone", ["BTbn"], B + "Solo Trombone/06 Keyswitch/1TB KS Master.oib", "brass", 0.45),
    ("Tuba", ["Tuba"], B + "Solo Tuba/06 Keyswitch/1TU KS Master.oib", "brass", 0.5),
    ("Timpani", ["Timp"], P + "Drums/Timpani/Timpani Flt KS.oib", "timp", 0.0),
    # c01: Harp Maestro has no samples below MIDI 48; Harp Sus RR covers 24-103 (group ranges read from the .oib)
    ("Harp", ["HarpR", "HarpL"], H + "01 Maestro Patches/Harp Sus RR.oib", "harp", -0.55),
    ("Violins I", ["VlnI"], S + "1st Violins/06 Keyswitch/1st Violins KS Master.oib", "string", -0.6),
    ("Violins II", ["VlnII"], S + "2nd Violins/06 Keyswitch/2nd Violins KS Master.oib", "string", -0.3),
    ("Violas", ["Vla"], S + "Violas/06 Keyswitch/Violas KS Master.oib", "string", 0.15),
    ("Violoncellos", ["Vc"], S + "Celli/06 Keyswitch/Celli KS Master.oib", "string", 0.4),
    ("Double basses", ["Cb"], S + "Basses/05 Keyswitch/Basses KS Master.oib", "string", 0.6),
    # c01: the harp harmonics at 82-83 on their own patch (appended last so the other stems keep their numbers)
    ("Harp harmonics", ["HarpR"], H + "02 Individual Articulation Patches/Harp Harmonics.oib", "harm", -0.55),
    # c10 (A #1): the Violin I solo (bars 17-22, "solo, senza sord.") on the half-section DIV A KS Master (the closest to a
    # solo violin on the drive); appended last so the other stems keep their numbers. TRACK_WINDOWS routes the notes.
    ("Violin I solo", ["VlnI"], S + "1st Violins Divisi/06 Keyswitch/1st Violins KS Master DIV A.oib", "string", -0.6),
    # c13 (A #1): the upper half of the celli's "div." answers to the solo violin (bars 18 and 22) on the half-section
    # DIV A KS Master; appended last (stem 29). TRACK_SPLITS routes the notes.
    ("Violoncellos div", ["Vc"], S + "Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib", "string", 0.35),
    # c18 (A #2): the upper voice of the divisi passages on half-section DIV B KS Masters (stems 30-31); TRACK_SPLITS
    # routes the notes. Before, each voice was a full-section sample 3 dB down (2 x 12 players instead of 2 x 6)
    ("Violins II div", ["VlnII"], S + "2nd Violins Divisi/06 Keyswitch/2nd Violins KS Master DIV B.oib", "string", -0.3),
    ("Violas div", ["Vla"], S + "Violas Divisi/06 Keyswitch/Violas KS Master DIV B.oib", "string", 0.15),
    # c18 (A #4): the Horns 1-2 a2 of bars 79-82 (one printed line) on the two-horn KS Master (stem 32), instead of one
    # solo horn raised 4 dB; TRACK_WINDOWS routes the notes (Horn 2's copies were dropped as unisons)
    ("Horns 1-2 a2", ["Hn1"], B + "2 French Horns/06 Keyswitch/2FH KS Master.oib", "brass", -0.45),
]

# c10 (A #1): notes by score onset: {track: (from qn, to qn, keep inside?)}; Violins I rests while the solo track plays
TRACK_WINDOWS = {"Violin I solo": (48.0, 65.0, True), "Violins I": (48.0, 65.0, False),
                 "Horns 1-2 a2": (261.0, 272.0, True), "Horn 1": (261.0, 272.0, False), "Horn 2": (261.0, 272.0, False)}

# c13 (A #1): {split track: (source track, [(from qn, to qn)], lowest pitch)}: source-staff notes with a score onset in
# a window and a pitch at or above the lowest pitch play on the split track and are removed from the source track. The
# source track still counts them for its divisi level cut (it keeps playing a half section's line on a full-section
# patch). Both answers were two-note Sus MAX chords on the full Celli KS Master: 10-15 dB holes, the slur re-attacked.
# c18 (A #2): the lowest pitch may be "rank": a note goes to the split track when another source note starts with it
# (within 0.01 qn) at a lower pitch (the viola voices cross at 61 and 63, so no pitch threshold separates them)
TRACK_SPLITS = {"Violoncellos div": ("Violoncellos", [(51.0, 54.0), (63.0, 66.0)], 55),
                "Violins II div": ("Violins II", [(108.0, 124.0)], 64),
                "Violas div": ("Violas", [(66.0, 90.0), (277.0, 289.0)], "rank")}

TIMP_VEL = {278.5: 60, 279.0: 60}

# c04 (C #6): breaths before the two tutti arrivals take time: seconds added in the 0.25 qn before the breath
CAESURA = {204.0: 0.22, 268.0: 0.15,
           # c08 (C #3): solo breath marks (Hn1 bar 10, Fl1 bar 41, CA bar 50, Cl1 bar 87) and phrase seams
           29.0: 0.12, 124.0: 0.12, 164.0: 0.10, 286.0: 0.10,
           42.0: 0.08, 48.0: 0.10, 66.0: 0.10, 140.0: 0.08, 171.0: 0.10, 237.0: 0.10}

# c06 (A #4): extra legato lead (s) when the previous legato note has this pitch (Violas leaving C4: takeover 0.22-0.37 s)
# c11 (C #1): Horn 1 leaving F4 crossed +0.19..+0.31 s late (median of its other transitions +0.028)
LEG_EXTRA_S = {"Violas": {60: 0.10}, "Horn 1": {65: 0.15}}

# c11 (C #5): extra legato lead (s) for one interval (previous pitch, target pitch) that crossed 0.15-0.23 s late every time
# c19 (C #1): Horn 1 F4 -> Bb4 landed 0.13-0.16 s early with the full F4 extra (-0.12 here); Oboe 1 Db5 -> C5 and F5 -> Eb5
# crossed +0.13..+0.16 s late every time. c19 (C #3): Violas Bb3 -> Db4 and A3 -> C4 in the bars 37-40 triplets +0.13..+0.22
LEG_PAIR_EXTRA_S = {"Violoncellos": {(56, 60): 0.15},
                    "Violas": {(60, 63): 0.10, (65, 61): 0.12, (58, 61): 0.10, (57, 60): 0.10,
                               # c23 (C #5): falling steps crossed 0.07-0.17 s early with the C4 extra (rising-step fix)
                               (60, 58): -0.10, (65, 64): -0.08, (52, 51): -0.08},
                    "Horn 1": {(65, 70): -0.12}, "Oboe 1": {(73, 72): 0.10, (77, 75): 0.10}}

# c19 (C #3): {track: [(from qn, to qn, fraction)]}: the legato lead cap is this fraction of the previous note's length
# (default 0.45) for score onsets in a window; the viola triplets sat at the 0.15 qn cap, so no extra lead acted
LEG_CAP_FRAC = {"Violas": [(108.0, 124.0, 0.75), (186.0, 192.0, 0.75)]}

# c06 (C #6): fixed velocities {track: {score onset: velocity}}
# c09 (A #5): Tbn1 218 105 -> 110 (+0.5 dB over its neighbours at v105; v118 with ACCENT_DB 3 measured +8)
# c10 (B #3, C #2): Tbn1 212.5/213 121 -> 108/105 (peaks 19-21 dB over their body; the master's loudest samples)
# c10 (C #5): the coda pp arrival at qn 286 (Vc/Vla/Cb v41-53 Leg Slur re-attacks decayed 5-11 dB) at v60
# c14 (A #1): the Marc Lng notes of Tbn1's marcato line fall from v106 to v94 (the c06 note trims -1..-2.5 dB that made
# this fall ramped in over each note and are removed)
VEL_SET = {"Trombone 1": {218.0: 92, 212.5: 96, 213.0: 96,   # c26 (item 9): 110/108/105 -> 92/96/96 on Sus MAX
                          214.5: 106, 215.0: 104, 215.5: 102, 216.0: 100, 217.0: 96, 217.5: 94},
           "Violoncellos": {286.0: 60}, "Violas": {286.0: 60}, "Double basses": {286.0: 60},
           "Oboe 1": {148.0: 100}}   # c08 (C #2c): the bar 47 goal re-attack (Sus MAX, same pitch) was v73

# c12 (A #2): joins (target score onsets) that measured at least 1.5 dB better on Leg BC MAX in c10 than on the BC_SOFT
# Leg Slur MAX join in c11 stay Leg BC MAX (BCSOFT depth stays 0)
BC_SOFT_SKIP = {"Violins II": [48, 54, 57, 146, 154, 159, 271], "Violas": [159],
                "Violoncellos": [45, 50, 60, 62, 132, 144, 160, 220]}

# c08 (C #4): from this qn on, soft (CC11 <= 40) string legato targets do not take the v124 legato velocity (coda bars
# 87-92 grew 4 dB at qn 292 on Vc/Vla Leg BC v124)
CODA_SOFT = {"from_qn": 280.0, "max_cc": 40, "vel": 90}

# c07 (A #1): "Largamente" bars 61-62 (strings "molto sostenuto"): wind portato (tenuto under a slur) is joined, not
# re-tongued. Inside these spans a slurred tenuto wind note to a new pitch plays Leg Slur (legato target, velocity 100,
# CC11 notch 10); a repeated pitch is re-tongued on Sus with a 0.04 s lead, velocity 100 or more.
SOSTENUTO_SPANS = [(204.0, 212.0)]

# c11 (A #3): per-onset accent weight in dB with the timpani loud-attack shape (10 ms rise, held 0.12 qn, 0 by 0.3 qn):
# Tbn1's ff marcato pickup measured -1.7 dB attack over its body at v108 (the c10 velocity cut removed the peak and the
# emphasis with it); ACCENT_DB's 0.25 s hold covered half the note, so attack and body rose together
ACCENT_DB_AT = {"Trombone 1": {212.5: 4.5, 213.0: 3.0, 218.0: 6.0}}   # c15 (A #4): 213 (+1.2 dB peak over body)

# c21 (A #3): 218 3.0 -> 4.5 (it measured only 1.5 dB over the marcato eighths, which get +5 dB on their attacks)
# c26 (BRIEF item 9; A #2, B #3, C #2): Dan heard Tbn1's bar 63-64 accents as harsh. Measured on c25: the attacks were a
# 2-5 kHz burst (+7..+13 dB over the note's own body) from three things stacked on 40-80 ms: the Sus Accent MAX sample,
# CC11 122 (ff 114 + ACCENT_BUMP 8, the fff layer) and a 10 ms +3..+4.5 dB step. Now: Sus MAX (ACCENT_ART_AT), no CC11
# bump (ACCENT_BUMP_AT), v96/96/92 (VEL_SET) and a swell in seconds with no front edge: 0 at onset - 0.01 qn, full at
# + rise_s, held to + hold_s, 0 by + end_s (ACCENT_SWELL_S_AT), +4.5/+3.0/+6.0 dB (first c26 render with +3.0/+3.0/+2.5:
# 212.5 and 218 sat +1.2 and -1.8 dB against the bodies of the marcato eighths; raised after the render, gain only)
ACCENT_ART_AT = {"Trombone 1": {212.5: "Sus MAX", 213.0: "Sus MAX", 218.0: "Sus MAX"}}

ACCENT_BUMP_AT = {"Trombone 1": 0}

ACCENT_SWELL_S_AT = {"Trombone 1": {212.5: (0.07, 0.25, 0.6), 213.0: (0.07, 0.25, 0.6), 218.0: (0.07, 0.25, 0.6)}}

# c26 (BRIEF item 8; A #1, C #1): the final chord (qn 292-304, 18.7 s) held one sample per string section, so each
# section replayed its 3.93-3.97 s sustain loop 4-5 times in step with the others (c25 master 100-300 Hz folded swing
# 4.8 dB, autocorrelation 0.58; stem centroid autocorrelation 0.39-0.63): a synchronized slow bow cycle. REBOW_AT splits
# the held note at these score qn into abutting same-pitch notes (the first ends REBOW_GAP_QN early, the Double basses'
# bar 88 re-bow shape that dipped 3-5 dB with no hole); each new note is a fresh REBOW_ART note at REBOW_VEL with no lead
# and no notch. The points are irregular and staggered across the sections (A's list, segments 1.8-4.6 s), so no
# sample plays much more than one loop and no two sections change bow together. Sus MAX, not Leg Slur MAX: a same-pitch
# re-attack on the legato patch plays its slow first-note layer (c03: 7-15 dB holes)
REBOW_AT = {"Violins I": [295.0, 298.0, 301.0, 302.75],
            "Violins II": [289.0, 290.9, 293.0, 295.8, 297.6, 300.2, 302.2, 303.4],
            "Violas": [294.1, 296.9, 299.2, 301.5, 303.1],
            "Violoncellos": [293.6, 296.3, 298.6, 300.6, 302.35],
            "Double basses": [294.5, 297.2, 299.8, 302.0, 303.3]}

# c26: CC11 notches removed where a re-bow now plays the bow change (Vln I's printed bowings 295/298/301; Vln II's
# merged repeats at 289/292, "change bow at will")
# c26 (B #2): Horns 3-4's bar 81 decrescendo has no printed target; HP_STEP (14 CC, 87 -> 74) left the held chord over
# the falling tune (Fl1/Vln I fell 5-9 dB, the horns 0-1 dB; their sum 2.5 dB over Vln I at qn 270.5). The tutti
# arrives at p in bar 82; the chord goes there with it. {staff: {hairpin start qn: dynamic}}
HP_TARGET_AT = {"Hn3": {268.0: "p"}, "Hn4": {268.0: "p"}}

NOTCH_SKIP = {"Violins I": [295.0, 298.0, 301.0], "Violins II": [289.0, 292.0]}

# c11 (A #4): Leg Port MAX (portamento) on these legato targets {track: {score onset: velocity}}: the one-string leaps of
# the "espr., sul D" phrase (F5 -> B flat 5) and the "sul A" entry (C5 -> F5). First trial on Violins I only; check the
# f0 glide (target 0.08-0.25 s) before adding Vln II 82 / Vc 83
PORT_TARGETS = {"Violins I": {82.0: 100, 172.0: 100},
                # c12 (A #3): the same leaps in Violins II (unison with Vln I), and the celli's A flat 3 -> D flat 4 in the
                # cantabile (Vln I 82 measured a 0.12-0.15 s glide 12-15 dB under the source note, no hole)
                "Violins II": {82.0: 100, 172.0: 100}, "Violoncellos": {83.0: 100}}

# c14 (A #1): a printed "marcato" line: unaccented notes of 1 qn or less inside the span play Marc Lng RRx4 (velocity sets
# the dynamic), 0.75 x their written length; accented notes of 1 qn or more inside it end 0.1 qn early. Tbn1 bars 63-64
# played every unaccented note Sus MAX legato-joined (each started 2-5 dB under the previous note's end, no break)
MARCATO_SPANS = {"Trombone 1": [(212.5, 219.0)]}

# c14 (A #2): a timpani roll tied into a short note ends with a stroke on that note (onsets of the tied notes; the MIDI
# merges the tie into the roll). The stroke's CC7 is the roll level + TIMP_TIE_STROKE_DB (40 log10 CC7 scale); the f/ff
# strokes also get TIMP_LOUD_ATTACK_DB. The pp/ppp tied ends (qn 8, 237) are left as rolls (felt strokes below v53 are
# near silent; v53 would stick out of a ppp roll)
TIMP_TIE_STROKES = [203.0, 211.0]

LEAD_SPANS = {"Horn 1": [(17, 40), (226, 236)], "Oboe 1": [(42, 60), (139, 152)], "Violin I solo": [(48, 65)],
              "Violins I": [(65, 90), (237, 262)], "Violins II": [(65, 90), (237, 262)], "Bass clarinet": [(90, 109)],
              "Cor anglais": [(124, 171)], "Flute 1": [(124, 129)], "Clarinet 1": [(280, 292)]}

# c20 (C #1): long notes starting inside ARRIVAL_HOLD_SPANS (score qn) take the swell_sost contour (+4 CC by 40%, held, and
# the SOST_SUSTAIN_DB rise into the next note) instead of the swell/taper arc. The bar 78 f arrival (poco allargando, into
# the ff of bar 79) rose to CC 92 and then fell to 83-87, under the printed f (88), inside the arrival bar
ARRIVAL_HOLD_SPANS = [(258.9, 259.1)]

METRIC_SPANS = [(18, 42), (108, 140), (172, 188)]

# c15 (A #6): per-onset breath gap in qn for a note that ends at a printed breath (default 0.3 qn at mf+), plus a CC11
# fall of that many CC over the note's last 0.2 qn (Hn1 qn 195: the 0.28 s gap dipped only 1.9 dB under the release)
BREATH_GAP_AT = {"Horn 1": {195.0: 0.5}}

BREATH_FALL_CC = {"Horn 1": {195.0: 10}}

# c15 (A #4): an accented note of 1 qn or more inside a MARCATO_SPAN ends this many qn early (default 0.1): Tbn1's dotted
# C4 at 213 ended 0.1 qn early and its release filled the break before 214.5 (no level change at the onset)
MARC_ACC_CUT_AT = {"Trombone 1": {213.0: 0.25}}

# c15 (B #1): unmarked soft swells (< > inside a phrase whose printed peak comes later) that do not get HP_GAIN_SOFT_DB:
# the swell top reached the phrase's printed mp/mf (Horn 1 bar 8 -31.2 against the mp crest -31.6..-32.8 dB)
SWELL_NO_SOFT_GAIN = {"Horn 1": [20.0], "Violins I": [68.0, 240.0], "Violins II": [68.0, 240.0]}

# c18 (C #1): these swells get a smaller messa di voce instead (checked before SWELL_NO_SOFT_GAIN); HP_SOFT_DEC_AT gives
# per-onset decrescendo depths (Oboe 1's bar 41-42 > sits on a +5 note trim and a +2.5 role: 1.3 dB over 2.5 qn)
# c24 (C #1): 68 removed (the bar 24 swell top stood 1.3 dB under the bar 28 mf crest); 68 falls to SWELL_NO_SOFT_GAIN
SWELL_SOFT_GAIN_AT = {"Violins I": [240.0], "Violins II": [240.0]}

HP_SOFT_DEC_AT = {"Oboe 1": {148.0: 4.0, 57.0: 5.0}}   # c22 (C #1): Ob1 57 (bar 20 >) measured -1.0 dB with the default 2

# c22 (C #1): per-onset soft crescendo gains in lead lines (in place of HP_GAIN_SOFT_DB[family]); these six solo hairpins
# measured -2.1..+2.0 dB (stem, last third minus first third), because note/pitch trims, phrase tops and sample sags
# cancelled the +3 dB ramp (the working solo hairpins measure +4..+10)
# (Violin I solo 48: 6 -> 4.5, because removing its phrase tops (C #1d) adds about 2 dB to the same crescendo)
HP_SOFT_GAIN_AT = {"Violin I solo": {48.0: 4.5, 60.0: 4.5}, "Horn 1": {32.0: 4.0, 176.0: 5.0}, "Flute 1": {126.0: 6.0}}

# c22 (C #1b): spans that get the lead-line soft hairpin ramp without being LEAD_SPANS (LEAD_SPANS also steers phrase
# tops, metric steps and the tempo apexes, so the bar 54-56 horn/clarinet line is added here only)
HP_SOFT_EXTRA_SPANS = {"Horn 1": [(174, 184)]}

# hairpin starts the accompaniment rule skips: the bar 91 morendo has its own _all role ramp held through the fermata
# (the rule's release after the decrescendo made the final ppp chord rise 2.3 dB)
HP_SOFT_ACC_SKIP = [298.0, 283.0]   # c24 (B #2): 283 the coda strings ppp < pp under the clarinet solo

# c22 (B #1): a CC11 ceiling on the long-note swell for listed pitches whose next dynamic layer is much louder. In the
# Bassoon KS Master the f layer fades in over CC11 33-38 (patch table: 0.12 at 34, 0.37 at 36, 0.6 at 38) under the full
# mp layer; Bassoon 2's B flat 2 measured -51.9 dB at CC 34, -49.5 at 36 and -41.4 at 37, so its pp swells (34 -> 38)
# rose 11 dB to within 2-3 dB of the horn and oboe solos. Applied only while the printed level is at or under the cap
# c23 (B #1): the cap at 36 left the f layer at 0.37 (Bn2 B flat 2 still rose 13 dB). Key "*": every swelling long note
# that starts at CC11 <= SWELL_CAP_MAX_CC is capped at its own starting CC11 + the value (0: no CC rise; the volume
# envelope's SWELL_DB still shapes it). Patch tables (CC11 rescalers): Bassoon "Bs f" 0.12 at 34 / 0.37 at 36; Bass
# clarinet "BC mp" 0.09 at 30 / 0.37 at 34; Contrabassoon "CB mp" 0.13 at 34 / 0.35 at 36; Clarinet "Cl mp" 0.02 at 32
# / 0.32 at 36: the printed pp/p (CC 32-36) sits where the next layer enters in all four
SWELL_CC_CAP = {"Bassoon 1": {"*": 0}, "Bassoon 2": {"*": 0, 46: 34}, "Bass clarinet": {"*": 0},
                "Contrabassoon": {"*": 0}, "Clarinet 2": {"*": 0}}

# c18 (C #3a): Violins I's legato join into F6 at qn 208 (moved start 207.80) peaked 1.9 dB over every other peak of the
# master (-2.26 dBFS at 207.83) and set the delivery limiter to 3.4 dB
# c21 (A #1): transition spikes of 5-12 dB (repeatable in c19 and c20, also with the volume envelope removed) on these
# joins; depth = 2 dB less than the smaller of the two spikes, capped at 6 (Vc 68.5: 8; Vln I 68: broad and shallow,
# because that spike moved between renders)
# c22 (A #2): Vln I 72 widened (the spike moved 0.1 s earlier between renders), Vln I 249.5, Vln II 73.5/83 (the unison
# partner of the Vln I 72/73.5 notches), Ob1 145 (the spike precedes the fill: the transition sample)
# c22 (B #2): Double basses E flat 2 sustain swells +5..+8 dB at moved start + 1.40-1.95 s (qn 63/75/84 notes), not joins:
# placed for the c21 tempo map and the 0.16 s ABUT_LEAD; move them if either changes
# c22 (B #3): Violoncellos bar 60 Leg Slur transition into F3 (11 dB swell, 7 dB K over the melody) and beat 3
# c22 (C #3a): the coda pp arrival attacks at qn 286 (Vc/Vla/Cb at v60), -3 dB
# c23 (A #3): CA 155.5 (+5.6, c21 +4.5), Vla 57 (+8.2, BC_SOFT join), Ob1 57 (+4.6, a 50 ms peak on the fill onset),
# Vla div 84 (+6.7), solo violin 51 (+4.7): depth = spike - 2
# c23 (after the render): Vln I 73.5's transition peak moved 0.1 qn later (73.48-73.53, +8 dB on the stem, +4 on the
# master) with unchanged notes and envelope; the notch now covers both positions at -5.5 (was 73.37-73.45, -6)
# c24 (A #1): the descending-run transition bursts before the cadence beats at 86.5 (bar 29) and 259 (bar 78) in Vln I/II
# (+7.4/+7.7 and +5.9/+5.8 on the stems, +6.0/+5.0 on the master), and Flute 1 259/266 (ff B flat 6 -> A flat 6, +8.0)
# c24 (B #4): Violoncellos ppp A flat 2 pedal swells 6 dB at qn 274.75 (sample, under the harp harmonics)
# c25 (A #2): Bass clarinet 93 (bar 32 solo arrival E flat 4, printed crescendo): a 0.35 s register-change burst, then a
# 13 dB trough where the B role [93.5,99,-6,2.5] ramps in on top of the 93 -4 note trim; cut the burst, fill the trough
# (positive values fill), step back to the current envelope
JOIN_NOTCH = {"Violins I": [(67.86, 68.02, -3.0), (71.90, 72.08, -4.5), (73.37, 73.55, -5.5), (74.90, 74.98, -3.0),
                            (79.86, 80.03, -3.0), (207.80, 207.97, -4.0), (249.37, 249.44, -3.5),
                            (86.38, 86.51, -5.5), (258.85, 258.93, -5.5)],
              "Violoncellos": [(68.37, 68.49, -8.0), (181.85, 181.99, -3.5), (240.37, 240.45, -5.0),
                               (200.52, 200.90, -5.0), (202.84, 202.97, -3.0), (285.75, 286.30, -3.0),
                               (274.70, 275.30, -3.0)],
              "Violins II": [(177.35, 177.52, -4.3), (242.99, 243.05, -3.3), (245.39, 245.47, -3.9),
                             (270.41, 270.50, -5.0), (73.33, 73.42, -4.0), (82.84, 82.91, -3.5),
                             (86.40, 86.50, -4.0), (258.81, 258.98, -4.0)],
              "Violin I solo": [(52.99, 53.15, -4.0), (50.89, 50.93, -2.5)],
              "Horn 1": [(29.88, 30.01, -2.5)],
              "Violas": [(161.86, 161.96, -3.9), (286.00, 286.40, -3.0), (56.81, 56.93, -6.0)],
              "Oboe 1": [(144.81, 144.92, -4.0), (56.97, 57.04, -2.5)],
              "Cor anglais": [(155.41, 155.57, -3.5)],
              "Flute 1": [(258.86, 258.93, -2.0), (266.00, 266.25, -5.0)],
              "Violas div": [(83.82, 83.98, -4.5)],
              "Double basses": [(64.12, 64.50, -4.0), (76.10, 76.62, -5.0), (85.10, 85.62, -6.0),
                                (285.95, 286.30, -3.0)],
              "Bass clarinet": [(93.03, 93.33, -4.5), (93.39, 93.85, 4.0), (93.89, 94.15, 1.5)]}

# c23 (A #4): untied repeated pp notes that wind players re-tongue: the note before ends 0.06 qn early (the legato-repeat
# gap; the 0.03 qn default gap dipped 0-1.4 dB, filled by the release tail and the hall). {track: [score onsets of the repeat]}
# c24 (C #2c): per-onset CC11 depth of a merged-repeat bow-change notch (default 8/10/14 CC). Violoncellos 148: the
# printed mf arrival of the bar 46-47 oboe/cello unison; the 14 CC dip took about 3 dB off the mf downbeat
MERGE_NOTCH_AT = {"Violoncellos": {148.0: 3}}

# c26 (C #1 fix 2, scaled): the lower strings' legato crossfade valley 0.6-1.0 s after the 292 chord change. C measured
# 3.4 dB in the string sum with the 292 loop profiles in place (they added -2..-4 dB over it); with the profiles removed
# a simulation on the c25 stems leaves Vla -3.5, Vc -4.5, Cb -5 dB for 0.3 qn; these fills take about half of C's dB
for t_, v_ in {"Violas": (292.62, 292.98, 2.5), "Violoncellos": (292.60, 293.00, 3.0),
               "Double basses": (292.48, 292.95, 3.0)}.items():
    JOIN_NOTCH.setdefault(t_, []).append(v_)

# c24 (B #5): per-onset note-trim ramp in seconds (default 0.6 s): the Oboe 1 entries at 42/54 spoke under the
# re-articulating pp strings for 0.25-0.5 qn because the trim arrived after the strings' attack
# c25 (A #3): old negative trims on crescendo notes become steps (Ob1 190, Cl1 256), Ob1 45 (printed decrescendo) falls
# over 2.1 s, Vc 180 over 1.8 s; (A #1) Cl1 292 +3 over 3 s against the sample's decay; (B #3) Horns a2 261 pickup step.
# Keys are score onsets (n["qn"] before the move), not the moved parts.json qn
NOTE_TRIM_RAMP_S = {"Oboe 1": {42.0: 0.1, 54.0: 0.1, 45.0: 2.1, 190.0: 0.1},
                    "Clarinet 1": {256.0: 0.1},   # c26 (B #1): 292.0 removed with its trim
                    "Violoncellos": {180.0: 1.8},
                    "Horns 1-2 a2": {261.0: 0.1}}

REP_RETONGUE_AT = {"Horn 4": [9.0, 12.0, 15.0], "Bass clarinet": [9.0, 12.0, 15.0], "Horn 3": [292.0],
                   "Bassoon 2": [23.0, 235.0]}

# c15 (C #4): a Sus note of these tracks that follows the previous note without a gap (within 0.05 qn) at another pitch,
# at CC11 <= max_cc, starts lead_s early; the previous note ends overlap_qn after the moved start (the pp bassoon chord
# changes under the horn solo reached body - 3 dB only at +0.17..+0.32 s; the bass clarinet at +0.00..+0.10)
# c16: off. The c15 render gave mixed arrivals and new 9-15 dB holes on the same-pitch repeats after a led note (Bn1 22,
# 32, Bn2 21)
# c19 (C #6): back on for listed onsets only ("at"): Bn1 27/35/36/38 under the horn theme (body - 3 dB at +0.25..+0.32 s;
# the bass clarinet on the same chords +0.00..+0.06). None of them is followed by a same-pitch repeat (the c15 failure)
# c20 (A #1): every arco Double basses pitch change that abuts the previous note (Sus MAX, no lead) crossed over a median
# +0.20 s after the score (celli -0.00; Cb - Vc +0.165 s at 46 shared changes): the old pitch takes +0.46 s to fall 10 dB.
# skip_next_same: no lead on a note followed by a same-pitch re-attack (the c15 holes)
ABUT_LEAD = {"Bassoon 1": {"lead_s": 0.10, "max_cc": 50, "overlap_qn": 0.0, "at": [27.0, 35.0, 36.0, 38.0]},
             "Double basses": {"lead_s": 0.16, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}}

# c03 (critic C #4): the printed rit./allargando/animando are realised in the score MIDI as tempo steps (global.ily \mt).
# Inside each span the step values are placed at the midpoints of their own steps and joined linearly (extrapolated to
# the span end), written as 0.25 qn steps. Spans: (start qn, end qn, tempo at the start).
RAMP_SPANS = [(102, 108, 52), (150, 152, 60), (172, 200, 60), (200, 204, 64), (212, 220, 54), (259, 274, 52), (292, 303, 52)]

# c12 (C #3): phrase-scale rubato inside the a-tempo stretches, which were exactly metronomic (bars 1-34: 101 of 102 beats
# at 52.0). For each phrase (start qn, end qn): x PHRASE_PUSH from start + 1 to the midpoint, then x 1.0 to end - 2,
# x 0.96 over [end - 2, end - 1) and x 0.92 over [end - 1, end) (phrase-final lengthening of roughly 8% of the last
# beat). Steps sit on whole qn only, so none falls inside a caesura's slowed 0.25 qn. Phrases touching RAMP_SPANS are
# skipped, and so is (90, 102), whose end runs straight into the printed rit. at 102 (the tempo would jump back up).
# c15 (C #5): an arc may carry a depth: "sub" (2-bar sub-phrases with the pulse running through: PHRASE_SLOW_SUB, no
# push) or "main" (section cadences: PHRASE_SLOW_MAIN). Every arc slowed x0.96/x0.92 and jumped back 8-17% on the next
# downbeat, so bars 15-22 hitched every two bars and the section ends had no more weight than the sub-phrases. An arc
# that starts where another ends takes its first beat at PHRASE_RETURN, so the tempo comes back over a beat.
# c16 (C #3): (42, 48) and (54, 60) removed: bars 15-22 slowed the same way every two bars (52/51/46, 52/51/49 ...);
# only the bar 18 sub-phrase keeps its arc, and bars 19-22 run to the cadence at qn 66 as one phrase
# c24 (C #5): (152, 160, "sub"), (160, 168): the cor anglais solo of bars 48-51 ran 18 of 20 beats at exactly 54.0
PHRASE_ARCS = [(18, 30), (30, 42, "main"), (48, 54, "sub"), (60, 66, "main"), (66, 78),
               (78, 90, "main"), (108, 124), (124, 140), (152, 160, "sub"), (160, 168), (220, 226, "sub"),
               (226, 238, "main"), (238, 250), (274, 286)]

# c16 (C #3): forward motion into crescendos and time at phrase apexes (whole-beat steps only, applied after the phrase
# arcs and before the caesuras). TEMPO_PUSH (start, end, factor): x factor from start + 1 to end, skipped where a
# RAMP_SPAN overlaps: bar 8 (21-24), bars 27-28 (78-84) and bars 75-77 into the bar 78 poco allargando (250-259; C wrote
# 244-253, but bars 75-77 are qn 250-259). APEX_AGOGIC: in each phrase arc, the beat holding the highest note of the lead
# line (the LEAD_SPANS track whose span started last at the arc's second beat) x APEX_AGOGIC, unless it is one of the
# arc's last two beats. BEAT_STRETCH: single beats (the Largamente downbeats of bars 61 and 62).
# c20 (C #4): pushes into the BCl/CA duet's mf crest (bars 32-33) and the oboe/cello p< of bars 45-46, with a held beat
# on each crest (97 x0.96, 147 x0.97 before the poco rit. of bar 47), in BEAT_STRETCH
TEMPO_PUSH = [(21, 24, 1.015), (78, 84, 1.02), (250, 259, 1.025), (93, 99, 1.02), (140, 147, 1.02)]

APEX_LEAD = {108: "Flute 1"}   # the flute solo of bars 37-40 has no LEAD_SPANS entry

BEAT_STRETCH = {204.0: 0.94, 208.0: 0.94, 97.0: 0.96, 147.0: 0.97}

# c05 (A #4): dynamics printed once on a shared staff that the extraction gives to one voice only: {track: [(qn, mark)]}
SHARED_DYN = {"Bassoon 1": [(259.0, "f")]}

# rules added after movement II (mvt1 c00), off or at the movement II values here so this config reproduces mvt II c26
REBOW_VEL = 41
AUTO_REBOW = False
GENTLE_ACCENT = {}
