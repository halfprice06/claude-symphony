"""Movement II score config for score_to_parts.py, series 2 (score mvt2/v600).

Series 1 (mvt2/v77, symphony/mvt2/reaper/) kept these tables inline in its tools/score_to_parts.py; at the end of c26
they were moved unchanged into mockup-kit/pipeline/example-config/score_config.py (every table there equals series 1's
c26 value; checked by evaluating both). This file starts from that c26 state and is fitted to v600 (c27 port, 2026-11-06):
every onset-keyed entry was checked against v600's notes (onset, pitch, length, the note before, the printed dynamic and
articulation); entries on missing or changed notes were dropped or moved. "v600 port:" comments below record each change.
Run in score_to_parts.py's namespace (S, W, B, H, P, DYN and the defaults are available)."""
SCORE_END = 304.0
SCORE_TITLE = "mvt2-mockup"   # v600 port: REAPER item names and the mp3 name (cycles/cNN/mvt2-mockup-cNN.mp3, as series 1)

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
# v600 port: Vc "div." now starts at 62 (bar 21 beat 3 is already two notes), so (63, 66) -> (62, 66); Violins II at 114
# play F sharp 4 + B flat 4, both above 64, so the threshold would empty Violins II there: "rank" (every note in the
# window is one of a pair); Violas: v600 adds "div." at 266-269 (bars 80-81) and the coda "con sord., div." runs from
# 279 to the final chord (no "unis." after it; the chord's A flat 3 is the upper voice), so (277, 289) -> (279, 304)
TRACK_SPLITS = {"Violoncellos div": ("Violoncellos", [(51.0, 54.0), (62.0, 66.0)], 55),
                "Violins II div": ("Violins II", [(108.0, 124.0)], "rank"),
                "Violas div": ("Violas", [(66.0, 90.0), (266.0, 269.0), (279.0, 304.0)], "rank")}

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
# v600 port: Tbn1 212.5 has no accent in v600 (an unaccented marcato pickup): v106, the top of the c14 Marc Lng fall
# (it was v96 as a Sus MAX accent); Vc/Cb 286 removed (v600: Vc F2 "tutti" and Cb F1 "4 soli", new pitches and entries)
# c28 (A #1): v600 slurs Tbn1's quotation (e8( c'4.->) b8( bes8 a8 | a4--) gis8( a8) f4.-> e8); the marcato line is now
# legato inside each slur, so the legato targets take firm, fast ff transition velocities (213, 215, 215.5, 217.5);
# slur heads 212.5/214.5/217.0 keep the c14 fall, the 216 portato repeat is re-tongued (WIND_REP_PORTATO)
VEL_SET = {"Trombone 1": {218.0: 92, 212.5: 106, 213.0: 112,   # c26 (item 9): 110/108/105 -> 92/96/96 on Sus MAX
                          214.5: 106, 215.0: 112, 215.5: 112, 216.0: 100, 217.0: 100, 217.5: 112},
           "Violas": {286.0: 60},
           "Oboe 1": {148.0: 100}}   # c08 (C #2c): the bar 47 goal re-attack (Sus MAX, same pitch) was v73

# c12 (A #2): joins (target score onsets) that measured at least 1.5 dB better on Leg BC MAX in c10 than on the BC_SOFT
# Leg Slur MAX join in c11 stay Leg BC MAX (BCSOFT depth stays 0)
# v600 port: Vln II 57 and Vla 159 have no note in v600; Vc 62 (B flat 2 -> E 3 + G sharp 3), 160 (F sharp 3 -> A 2)
# and 220 (now joined from B flat 2 at 219.5) changed: removed
BC_SOFT_SKIP = {"Violins II": [48, 54, 146, 154, 159, 271],
                "Violoncellos": [45, 50, 60, 132, 144]}

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
# v600 port: 212.5 removed here and in ACCENT_ART_AT / ACCENT_SWELL_S_AT (no accent on it in v600)
ACCENT_DB_AT = {"Trombone 1": {213.0: 3.0, 218.0: 6.0}}   # c15 (A #4): 213 (+1.2 dB peak over body)

# c21 (A #3): 218 3.0 -> 4.5 (it measured only 1.5 dB over the marcato eighths, which get +5 dB on their attacks)
# c26 (BRIEF item 9; A #2, B #3, C #2): Dan heard Tbn1's bar 63-64 accents as harsh. Measured on c25: the attacks were a
# 2-5 kHz burst (+7..+13 dB over the note's own body) from three things stacked on 40-80 ms: the Sus Accent MAX sample,
# CC11 122 (ff 114 + ACCENT_BUMP 8, the fff layer) and a 10 ms +3..+4.5 dB step. Now: Sus MAX (ACCENT_ART_AT), no CC11
# bump (ACCENT_BUMP_AT), v96/96/92 (VEL_SET) and a swell in seconds with no front edge: 0 at onset - 0.01 qn, full at
# + rise_s, held to + hold_s, 0 by + end_s (ACCENT_SWELL_S_AT), +4.5/+3.0/+6.0 dB (first c26 render with +3.0/+3.0/+2.5:
# 212.5 and 218 sat +1.2 and -1.8 dB against the bodies of the marcato eighths; raised after the render, gain only)
# c28 (A #1): 213 is now the slurred target of the 212.5 pickup: it stays on Leg Slur MAX (GENTLE_ACCENT brass
# keep_legato) with its swell; 218 (unslurred) keeps Sus MAX
ACCENT_ART_AT = {"Trombone 1": {218.0: "Sus MAX"}}

ACCENT_BUMP_AT = {"Trombone 1": 0}

ACCENT_SWELL_S_AT = {"Trombone 1": {213.0: (0.07, 0.25, 0.6), 218.0: (0.07, 0.25, 0.6)}}

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
# v600 port: AUTO_REBOW is on, and its points for three passages fell together ("no room" in tools/space_rebows.py):
# (1) the opening chord (bars 1-3, held 6-9 qn, 7-10 s): five sections within 0.25-0.8 s of qn 5.2-6.7. Listed here,
# staggered at least 0.63 s apart, every piece 1.9-4.4 s. (2) Bar 66 (qn 220-226): v600 prints a down-bow on the tied
# note at 223 in Vln II, violas and celli; their re-bows are put there (the printed bow change; NOTCH_SKIP drops its
# CC11 notch). (3) The final chord: v600 divides the violas to the end, so "Violas div" holds A flat 3 from 286 under the
# c26 points of the other five sections; its points are the largest-gap choice (at least 0.35 s from every other
# section's re-bow, pieces 1.5-4.5 s; the c26 lists leave no wider gaps)
for t_, v_ in {"Violins I": [2.4, 4.6, 7.35], "Violins II": [5.15, 223.0], "Violas": [5.7, 223.0],
               "Double basses": [6.25], "Violoncellos": [6.8, 223.0],
               "Violas div": [287.3, 288.6, 291.7, 295.3, 298.3, 301.25, 302.95]}.items():
    REBOW_AT[t_] = sorted(REBOW_AT.get(t_, []) + v_)

# c26: CC11 notches removed where a re-bow now plays the bow change (Vln I's printed bowings 295/298/301; Vln II's
# merged repeats at 289/292, "change bow at will")
# c26 (B #2): Horns 3-4's bar 81 decrescendo has no printed target; HP_STEP (14 CC, 87 -> 74) left the held chord over
# the falling tune (Fl1/Vln I fell 5-9 dB, the horns 0-1 dB; their sum 2.5 dB over Vln I at qn 270.5). The tutti
# arrives at p in bar 82; the chord goes there with it. {staff: {hairpin start qn: dynamic}}
# v600 port: bar 58 (qn 188-196) is now < from p to a crest on beat 4 (195), a short > into the breath and f at bar 59.
# The f at 196 closed the < as its target and the > then fell 6 CC under it, holding the f down (curve 82 at 196 on
# Fl1/Ob1/Vln I/Vln II). The f is a fresh level after the breath (SUBITO_AT), and the < goes to the level that v600's
# hidden MIDI marks give the crest at 195: f in the violins, mf in flute 1 and oboe 1
# c28 (B #2): the timpani roll's bar 81 decrescendo (268-271, no printed target) fell 1.8 dB while the master fell 9.4;
# at qn 270 the roll was the loudest stem and 85% of the 50-250 Hz energy. Target: the tutti's p arrival, like Hn3/Hn4
HP_TARGET_AT = {"Hn3": {268.0: "p"}, "Hn4": {268.0: "p"}, "Timp": {268.0: "p"},
                "VlnI": {188.0: "f"}, "VlnII": {188.0: "f"}, "Fl1": {188.0: "mf"}, "Ob1": {188.0: "mf"}}
SUBITO_AT = {"VlnI": [196.0], "VlnII": [196.0], "Fl1": [196.0], "Ob1": [196.0]}
# v600 port (WARN fix; series 1 had it too): Clarinet 2's pp > (295-297) went straight to the ppp printed at 301
# (an untargeted hairpin stops at the next mark), so the morendo > from 298 had nowhere to go: the c06 rule made it fall
# 6 CC under the ppp (CC 16 at 301). The first > now stops halfway (pp- = 28) and the morendo reaches the printed ppp
DYN["pp-"] = 28
HP_TARGET_AT["Cl2"] = {295.0: "pp-"}

NOTCH_SKIP = {"Violins I": [295.0, 298.0, 301.0], "Violins II": [289.0, 292.0, 223.0],
              "Violas": [223.0], "Violoncellos": [223.0]}   # v600 port: 223 (the bar 66 printed down-bow, re-bowed)

# c11 (A #4): Leg Port MAX (portamento) on these legato targets {track: {score onset: velocity}}: the one-string leaps of
# the "espr., sul D" phrase (F5 -> B flat 5) and the "sul A" entry (C5 -> F5). First trial on Violins I only; check the
# f0 glide (target 0.08-0.25 s) before adding Vln II 82 / Vc 83
PORT_TARGETS = {"Violins I": {82.0: 100, 172.0: 100},
                # c12 (A #3): the same leaps in Violins II (unison with Vln I), and the celli's A flat 3 -> D flat 4 in the
                # cantabile (Vln I 82 measured a 0.12-0.15 s glide 12-15 dB under the source note, no hole)
                # v600 port: Vc 83 removed (v600 joins it from F3 at 82, not A flat 3 at 81)
                "Violins II": {82.0: 100, 172.0: 100}}

# c14 (A #1): a printed "marcato" line: unaccented notes of 1 qn or less inside the span play Marc Lng RRx4 (velocity sets
# the dynamic), 0.75 x their written length; accented notes of 1 qn or more inside it end 0.1 qn early. Tbn1 bars 63-64
# played every unaccented note Sus MAX legato-joined (each started 2-5 dB under the previous note's end, no break)
# c28 (A #1): removed. v600 slurs the line, and in_marc() came before every slur rule: each slurred note played Marc
# Lng at 0.75 of its length (breaks of 8-13 dB on the stem inside the slurs, the slurred accent at 213 peaking +0.48 s)
MARCATO_SPANS = {}

# c14 (A #2): a timpani roll tied into a short note ends with a stroke on that note (onsets of the tied notes; the MIDI
# merges the tie into the roll). The stroke's CC7 is the roll level + TIMP_TIE_STROKE_DB (40 log10 CC7 scale); the f/ff
# strokes also get TIMP_LOUD_ATTACK_DB. The pp/ppp tied ends (qn 8, 237) are left as rolls (felt strokes below v53 are
# near silent; v53 would stick out of a ppp roll)
# v600 port: the bar 62 roll (D flat 3 from 208) is tied into a stroke at 209.5 (v77: A flat 2 at 210 tied into 211)
TIMP_TIE_STROKES = [203.0, 209.5]

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
# v600 port: Horn 1 195 (and BREATH_FALL_CC) removed: the note before the 196 breath is now an eighth at 195.5
BREATH_GAP_AT = {}

BREATH_FALL_CC = {}

# c15 (A #4): an accented note of 1 qn or more inside a MARCATO_SPAN ends this many qn early (default 0.1): Tbn1's dotted
# C4 at 213 ended 0.1 qn early and its release filled the break before 214.5 (no level change at the onset)
MARC_ACC_CUT_AT = {}   # c28: with MARCATO_SPANS

# c15 (B #1): unmarked soft swells (< > inside a phrase whose printed peak comes later) that do not get HP_GAIN_SOFT_DB:
# the swell top reached the phrase's printed mp/mf (Horn 1 bar 8 -31.2 against the mp crest -31.6..-32.8 dB)
# v600 port: kept. v600 shortens the < of these swells (Horn 1 < 20-21 > 21-24, violins < 68-69 > 69-70, < 240-241 >);
# their crests carry hidden MIDI-only levels, which build/mockup.ly drops, so they are still unmarked swells
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
# v600 port: Horn 1 176 (now pp < to mp at 182, the line changed) and Flute 1 126 (new notes, pp) removed
HP_SOFT_GAIN_AT = {"Violin I solo": {48.0: 4.5, 60.0: 4.5}, "Horn 1": {32.0: 4.0}}

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
# v600 port: removed where the join changed: Vln I 249.5 (A4 -> F4 now), Vc 182 (now C2 after E flat 2), Vc 203 (no
# note), Vc and Cb 286 (new pitches F2/F1, "tutti"/"4 soli" entries), Vla 162 (no note), Ob1 145 (A4, was A flat 4), Cb 76
# (the E flat 2 at 75 is now E flat 3: v600's basses play bars 23-28 an octave higher), and the three Bass clarinet bar 32
# rows (the solo of bars 31-36 is an octave lower in v600; the E flat 4 register burst they answered is gone)
JOIN_NOTCH = {"Violins I": [(67.86, 68.02, -3.0), (71.90, 72.08, -4.5), (73.37, 73.55, -5.5), (74.90, 74.98, -3.0),
                            (79.86, 80.03, -3.0), (207.80, 207.97, -4.0),
                            (86.38, 86.51, -5.5), (258.85, 258.93, -5.5)],
              "Violoncellos": [(68.37, 68.49, -8.0), (240.37, 240.45, -5.0),
                               (200.52, 200.90, -5.0), (274.70, 275.30, -3.0)],
              "Violins II": [(177.35, 177.52, -4.3), (242.99, 243.05, -3.3), (245.39, 245.47, -3.9),
                             (270.41, 270.50, -5.0), (73.33, 73.42, -4.0), (82.84, 82.91, -3.5),
                             (86.40, 86.50, -4.0), (258.81, 258.98, -4.0)],
              "Violin I solo": [(52.99, 53.15, -4.0), (50.89, 50.93, -2.5)],
              "Horn 1": [(29.88, 30.01, -2.5)],
              "Violas": [(286.00, 286.40, -3.0), (56.81, 56.93, -6.0)],
              "Oboe 1": [(56.97, 57.04, -2.5)],
              "Cor anglais": [(155.41, 155.57, -3.5)],
              "Flute 1": [(258.86, 258.93, -2.0), (266.00, 266.25, -5.0)],
              "Violas div": [(83.82, 83.98, -4.5)],
              "Double basses": [(64.12, 64.50, -4.0), (85.10, 85.62, -6.0)],
              }

# c23 (A #4): untied repeated pp notes that wind players re-tongue: the note before ends 0.06 qn early (the legato-repeat
# gap; the 0.03 qn default gap dipped 0-1.4 dB, filled by the release tail and the hall). {track: [score onsets of the repeat]}
# c24 (C #2c): per-onset CC11 depth of a merged-repeat bow-change notch (default 8/10/14 CC). Violoncellos 148: the
# printed mf arrival of the bar 46-47 oboe/cello unison; the 14 CC dip took about 3 dB off the mf downbeat
# v600 port: Vc 148 removed (printed mp in v600, no longer the mf arrival)
MERGE_NOTCH_AT = {}

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
# v600 port: Cl1 256, Vc 180 and Horns a2 261 removed with their note trims (changed dynamic or pitch)
NOTE_TRIM_RAMP_S = {"Oboe 1": {42.0: 0.1, 54.0: 0.1, 45.0: 2.1, 190.0: 0.1}}

REP_RETONGUE_AT = {"Horn 4": [9.0, 12.0, 15.0], "Bass clarinet": [9.0, 12.0, 15.0], "Horn 3": [292.0],
                   "Bassoon 2": [235.0]}   # v600 port: Bn2 23 removed (the repeat now has a tenuto)

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
# v600 port: Bassoon 1 27 removed from "at" (now preceded by F3 at 26, not A flat 3 at 24)
ABUT_LEAD = {"Bassoon 1": {"lead_s": 0.10, "max_cc": 50, "overlap_qn": 0.0, "at": [35.0, 36.0, 38.0]},
             "Double basses": {"lead_s": 0.16, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}}

# c03 (critic C #4): the printed rit./allargando/animando are realised in the score MIDI as tempo steps (global.ily \mt).
# Inside each span the step values are placed at the midpoints of their own steps and joined linearly (extrapolated to
# the span end), written as 0.25 qn steps. Spans: (start qn, end qn, tempo at the start).
# v600 port: the bar 63-64 allargando now starts at 64 (qn 216: \mt 48 s2 \mt 42 s2); bar 63 (the trombone quotation's
# head) stays in the Largamente tempo 54. Was (212, 220, 54) for v77's \mt 50 s1 \mt 46 s2 \mt 40 s2 from 212
RAMP_SPANS = [(102, 108, 52), (150, 152, 60), (172, 200, 60), (200, 204, 64), (216, 220, 54), (259, 274, 52), (292, 303, 52)]

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
# v600 port: emptied; v600 prints the f at 259 on Bassoon 1's own voice
SHARED_DYN = {}

# v600 port: the generic rules added after movement II (mvt1 c00-c36, defaults in tools/score_to_parts.py) stay on:
# AUTO_REBOW (every string note over 4.5 s re-bowed, Dan's c24 note), GENTLE_ACCENT (brass, wind and string accents on
# the plain sustain with a volume swell, Dan's c24 note), and the rest. REBOW_VEL None: re-bow velocity by printed
# level (REBOW_VEL_BY_CC; about 38-45 at the final chord's ppp-pp, where c26 used 41 for every re-bow)
REBOW_VEL = None

# ---------- c28 (critics on the c27 render) ----------
# A #1: Trombone 1's slurred accent at 213 stays on the legato row with the swell only (movement I c07: slurred brass
# accents re-tongued on Sus stood +2.6..+9.5 dB over their slur); the generic default sets keep_legato for winds only
GENTLE_ACCENT["brass"]["keep_legato"] = True
# A #1, S1: a slurred same-pitch repeat whose second note has a tenuto (Tbn1 215.5 -> 216, "a4--") is re-tongued with
# the WIND_REP_RETONGUE gap and CC11 fall (movement I c34: 12 of 20 such repeats dipped under 3 dB without it)
WIND_REP_PORTATO = True
# A #1: the marcato weight of the line as a swell on the slur heads after the first (0 at the onset, +2 dB at +0.04 s,
# held to +0.15 s, 0 by +0.35 s); the accents 213/218 keep their ACCENT_DB_AT swells
LEVEL_SHAPES_S["Trombone 1"] = LEVEL_SHAPES_S.get("Trombone 1", []) + [
    (214.5, [(-0.01, 0.0), (0.04, 2.0), (0.15, 2.0), (0.35, 0.0)]),
    (217.0, [(-0.01, 0.0), (0.04, 2.0), (0.15, 2.0), (0.35, 0.0)])]
# A #3, C #2: the felt timpani Rls row crossfades eight recorded dynamic layers on CC1 (Timpani Flt KS.oib, read in
# movement I c12: V1 at CC1 0-9 ... V8 at 118-127); with no CC1 lane every roll played V8 (c27: ppp rolls' 1-8 kHz share
# -11.5..-12.7 dB, as bright as the f rolls' -12.8..-13.8). Movement I's final map and the level the layers lose, put
# back on the rolls in the volume envelope (movement I c12 refit; to be refit here per printed dynamic by stem fix)
TIMP_CC1_MAP = [(22, 56), (34, 56), (46, 60), (58, 66), (72, 72), (88, 88), (114, 104), (124, 122)]
TIMP_ROLL_TRIM_DB = [(22, 17.6), (34, 19.0), (46, 18.6), (58, 12.7), (72, 9.5), (88, 7.3), (114, 3.7), (124, 0.0)]
# A #5 (S1): Violins II bars 15-21: three slurred A flats (42, 44 portato, 45 new slur) merge into one 5.5 s note, and
# AUTO_REBOW re-bowed it at 44.34 and 50.35 (stem dips 9.5/9.1 dB between the beats) while the printed new bows at 45
# and 51 were not heard. Re-bow on the printed new slurs instead (the listed point replaces the automatic ones)
REBOW_AT["Violins II"] = sorted(REBOW_AT["Violins II"] + [45.0, 51.0])
NOTCH_SKIP["Violins II"] = NOTCH_SKIP["Violins II"] + [45.0, 51.0]
# A #6, C #6 (test; S2): the violas' sotto voce portato eighths of bars 48-51 (15 off-beat eighths with rests) played the
# Leg Slur MAX first-note layer (no round robin): -6 dB at +0.25 s, peak +0.34..+0.52 s after the onset, at the end of
# a 0.53 s note. Detache (Violas KS Master key 30; manual p.91: no legato connection, "a well defined end"). Pass:
# peak by +0.15 s on 12 of 15 notes, at least 6 dB drop in the rests, peaks 7-9 dB under the cor anglais
ART_SPANS = {"Violas": [{"from": 152.5, "to": 168.0, "art": "Detache"}]}
# the Detache notes take the string entry lead after their rests like the Leg Slur MAX notes they replace (c27: 0.11 qn)
ENTRY_LEAD_ROWS = ENTRY_LEAD_ROWS + ("Detache",)
# A #2: the celli's final-chord piece from 300.6 swells by itself about +7 dB from qn 302.0 (c27 -53 -> -47 dB, the
# same in the refit simulation), which made the master rise 3-5 dB inside the ppp fermata; the 302.35 re-bow fit then
# holds that level. A -5 dB shape over the swell, released before the morendo's last fall (simulated on the c27 stems)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES.get("Violoncellos", []) + [
    [(301.85, 0.0), (302.05, -5.0), (302.9, -5.0), (303.15, 0.0)]]

# ---------- c29 (critics on the c28 render) ----------
# A #2: Trombone 1's ff quotation sank 4-7 dB in its middle at a flat CC11 (weak samples on the slurred transitions):
# 215.0 (B3 -> B flat 3, 6 dB under both neighbours) +4.5 dB over the note; 217.5 (the second note of gis8( a8)) keeps
# its level (no SLUR_PAIR_RELEASE taper into the 218 accent) and +2.5 dB; the slurred accent at 213 bloomed 0.45 s late
# (the sample's own 3-4 dB rise hid the swell): its swell is replaced by an onset-weighted shape gone by the sample's
# peak; the 218 accent 6 -> 4 dB, so it sits 2-4 dB over the raised 217.5
ACCENT_DB_AT["Trombone 1"][213.0] = 0.0
ACCENT_DB_AT["Trombone 1"][218.0] = 4.0
SLUR_PAIR_RELEASE_DB_AT = {"Trombone 1": {217.5: 0}}
LEVEL_SHAPES_S["Trombone 1"] = LEVEL_SHAPES_S["Trombone 1"] + [
    (213.0, [(-0.02, 0.0), (0.03, 4.0), (0.18, 3.5), (0.45, 0.0), (0.7, 0.0)]),
    (215.0, [(-0.02, 0.0), (0.03, 4.5), (0.50, 4.5), (0.60, 0.0)]),
    (217.5, [(0.0, 0.0), (0.08, 2.5), (0.45, 2.5), (0.55, 0.0)])]
# A #3: the violas' pizz. triplets of bars 41-44 at v41-46 fell under the pizz. row's velocity-layer edge (46 -> 47:
# 5-8 dB at one pitch), so the pp beats nearly vanished (16-20 dB under the p beats); floor 48, the hairpin stays in CC11
VEL_SET["Violas"].update({124.0: 48, 124.3333: 48, 124.6667: 49, 125.0: 49, 125.3333: 50, 125.6667: 50,
                          126.0: 50, 126.3333: 50, 126.6667: 51, 127.0: 51,
                          132.0: 49, 132.3333: 49, 132.6667: 49, 133.0: 49, 133.3333: 49, 133.6667: 49,
                          134.0: 49, 134.3333: 49, 134.6667: 48, 135.0: 48, 135.3333: 48, 135.6667: 48,
                          136.0: 48, 136.3333: 48, 136.6667: 48, 137.0: 48, 137.3333: 48, 137.6667: 48})
# A #4: the bar 52 crescendo roll peaked 6-13 dB over the p stroke it leads to (172, the bar 53 a tempo): stroke v64 ->
# 72 plus +4 dB over its first 0.6 s, the roll's top capped -4 dB, so the roll ends about 2 dB under the stroke
# B #3: the ppp roll of bars 67-70 held level over the 4-soli basses and did not play its decrescendo (232-237, no
# target): -2 dB from 226.5, falling to -6 dB at 237 (slow ramps, the hall tail kept), back to 0 after the roll
VEL_SET["Timpani"] = {172.0: 72}
LEVEL_SHAPES_S["Timpani"] = LEVEL_SHAPES_S.get("Timpani", []) + [(172.0, [(-0.02, 0.0), (0.0, 4.0), (0.6, 4.0), (0.9, 0.0)])]
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES.get("Timpani", []) + [
    [(170.5, 0.0), (171.6, -4.0), (171.94, -4.0), (171.95, 0.0)],
    [(226.0, 0.0), (226.5, -2.0), (232.0, -2.0), (237.0, -6.0), (237.6, -6.0), (240.0, 0.0)]]
# A #6: the harmonics' three-note head (274-276, all v58) peaked -51.7 / -46.2 / -55.2 dB: the passing eighth loudest,
# the slur's arrival softest (Harmonics patch about 0.55 dB per velocity step)
VEL_SET["Harp harmonics"] = {275.5: 48, 276.0: 64}
# A #6: the "R.H. etouffez" of bar 83 damped nothing (no ring rule, the patch's 3019 ms release): every harp note rings
# 2 s past its written end with a 200 ms release (mix.json env_release_ms), cut at the damp; "R.H." limits the damp to
# the right-hand staff (the L.H. A flat 1 pedal 271-277 rings on)
HARP_RING_S = 2.0
HARP_DAMP_STAFF["R.H."] = 0
# C S3 note: the Violas Detache cut (c28 stem fix role [152.45,167.98,-13]) acted after the hall and took the previous
# note's tail down 26 dB in 0.42 s; as CC7 (linear amplitude, pre-hall; 127 * 10^(-13/20) = 28) it leaves the hall ring
CC7_POINTS["Violas"] = [(152.2, 28), (167.98, 127)]
# after the c29 render (stem fix, level only): with 217.5 raised the 218 accent's front measured only +0.5 dB over the
# 0.3 s before it (c28 +6.6); 4 -> 6.5 dB for the 2-4 dB of BRIEF item 4
ACCENT_DB_AT["Trombone 1"][218.0] = 6.5

# ---------- c30 (critics on the c29 render) ----------
# ONE_TIME / MANUAL-GAPS #1 (B #5, c28 B #4 and C #3): the Hollywood Brass KS Masters (1FH, 2FH, 1TB, 1TU) and the
# Clarinet KS Master crossfade their dynamic layers with CC1, not CC11 (read again in c30 from the .oib files: every
# sustain/legato layer group ("1FH pp/mf/f/ff", "2FH pp/mf/f/ff", "1Tb p/mp/f/ff", "Tu pp/mf/f/ff", "Cl p/mp/f") has a
# cc 1 MidiController driving its Source volume through a rescaler table; CC11 is only the Global Group volume). With
# the c01 formula (CC1 53-87) every printed dynamic played the middle layers. CC1 now follows the printed dynamic curve
# through the generic CC1_DYN_MAP (movement I c09). "Horn" also matches "Horns 1-2 a2"; the trailing space keeps the
# bass clarinet (BC KS Master, CC11 layers) out. The contrabassoon (CB KS Master): CC11 crossfades its p/mp/f layers,
# CC1 crossfades Non Vib (1.0 to CC1 60, 0 by 80) and Vib (0 to 40, 1.0 from 70); its CC1 53-87 sat in that crossfade:
# held at 40 (Non Vib only), as movement I
CC1_DYN_TRACKS = ("Horn", "Trombone", "Bass trombone", "Tuba", "Clarinet ")
CC1_HOLD = {"Contrabassoon": 40}
# A #4: the passing C5 of the harmonics' three-note head stayed 3.5-5 dB over its neighbours at v48 (ten velocity steps
# bought 1.7 dB); v58 again with a -5 dB level shape that ends before the E flat (0.5 qn = 0.58 s later); arrival v66
VEL_SET["Harp harmonics"] = {275.5: 58, 276.0: 66}
LEVEL_SHAPES_S["Harp harmonics"] = LEVEL_SHAPES_S.get("Harp harmonics", []) + [
    (275.5, [(-0.04, 0.0), (0.0, -5.0), (0.5, -5.0), (0.57, 0.0)])]
# B #4a: the ppp roll of bars 2-3 sat 1-2 dB over the basses and over every string section by bar 3 (the sample grows
# while the printed decrescendo falls): slow ramps under the sounding roll, back to 0 after it ends (8.55)
# B #4b: the bar 52 pp < roll fell 5 dB in its last beat (c29's -4 dB cap ramped across the beat against the sample's
# own 2.3 dB sag): a flat cut that opens over the last beat instead, and the 172 stroke +4 -> +6 dB
LEVEL_SHAPES["Timpani"] = [s_ for s_ in LEVEL_SHAPES["Timpani"] if s_[0][0] != 170.5] + [
    [(3.0, 0.0), (4.5, -3.0), (6.0, -3.0), (8.4, -6.0), (9.2, -6.0), (9.5, 0.0)],
    [(168.0, 0.0), (168.5, -2.5), (170.75, -2.5), (171.5, -0.5), (171.94, -0.5), (171.95, 0.0)]]
LEVEL_SHAPES_S["Timpani"] = [s_ for s_ in LEVEL_SHAPES_S["Timpani"] if s_[0] != 172.0] + [
    (172.0, [(-0.02, 0.0), (0.0, 6.0), (0.6, 6.0), (0.9, 0.0)])]
# C #2: bars 55-58: the strings' mf at 184 was louder than the crescendo to the f at 196 (Violins I bar 56 -32.1, bar 57
# -35.3 dB; the celli cut inside their crescendo by role [188,190,-1.5] and note trim 190 -1.5, both removed in the
# json tables): the mf held back, the crescendo carried 1.5-2 dB more into bar 61 (slow ramps, no tail cut)
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES.get("Violins I", []) + [
    [(183.5, 0.0), (184.25, -2.5), (187.75, -2.5), (188.5, 0.0)], [(190.0, 0.0), (195.0, 2.0), (204.0, 2.0), (206.0, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [
    [(183.5, 0.0), (184.25, -2.5), (187.75, -2.5), (188.5, 0.0)], [(190.0, 0.0), (195.0, 1.5), (204.0, 1.5), (206.0, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(183.5, 0.0), (184.25, -2.5), (187.75, -2.5), (188.0, 0.0)]]
# C #4 (S3): the bar 66 niente (223-226, CC11 33 -> 12) fell only 3.5-4.6 dB on the stems; the rest came with the
# release after 226. CC7 (linear amplitude, before the Opus hall, so the ring fades with the line) falls 0 -> -14 dB
# over 223.5-226 in 0.125 qn steps, holds, and comes back over 230-236.5, before the next notes (236.9-237.9)
def _c30_niente_cc7():
    p_ = [(round(223.5 + 0.125 * i, 3), max(1, round(127 * 10 ** (-14.0 * i / 20 / 20)))) for i in range(21)]
    u_ = [(round(230.0 + 0.25 * i, 3), max(1, round(127 * 10 ** (-14.0 * (26 - i) / 26 / 20)))) for i in range(27)]
    return p_ + u_
for _t in ("Violins II", "Violas", "Violoncellos"):
    CC7_POINTS[_t] = CC7_POINTS.get(_t, []) + _c30_niente_cc7()

# ---------- c31 (critics on the c30 render) ----------
# A #1, B #1 (top priority; both critics): since c30's CC1 dynamics Horn 1's legato notes swelled at the head and then
# collapsed 7-13 dB (bars 7-14, 54-58, 65-70). Read in the 1FH and 2FH KS Masters (c31): the legato transition groups
# ("TLeg <pitch>", cc 1 rescaler) are 0.81-0.91 over CC1 30-46, 0.71 at 54, 0.61 at 60, 0.44 at 70, 0.1 at 90, while the
# sustain layers cross pp -> mf over CC1 20-50 (pp 0.59/mf 0.45 at 30, mf 1.0 at 50-54) and the soft samples are much
# quieter. Measured on the c30 stems (head = loudest 30 ms in 0.03-0.35 s, body = median from 0.45 s): legato targets at
# CC1 28-54 head - body 6-13 dB on most pitches (A flat 3 at 42: 9.8-9.9; G flat 4 at 54: 13.4; Horn 3 C4 at 28: 13.4),
# at CC1 61 6.0, at 72-86 -3..+4; c29 (CC1 63-70 from the vibrato formula) -3..+5. First notes (no transition) were flat
# at every CC1. The soft samples cannot carry a legato line under this transition table, so the horns' soft dynamics go
# back to c29's CC1 (64 + (CC11 - 46) * 0.3: ppp 57, pp 60, p 64, mp 68, mf 72) and keep c30's map from f up (86, 108,
# 120: the brighter f/ff measured in c30). The soft trims go back to c29's values (mix.json), and the four c30 Horn 1
# note trims fitted on the collapsed bodies (27, 39, 178, 37.5) are removed. Timbre cost: the soft horns are the c29
# colour again (1-5 kHz share p about -15 dB, c30 -21)
CC1_DYN_MAP_BY = {"Horn": [(22, 57), (34, 60), (46, 64), (58, 68), (72, 72), (88, 86), (114, 108), (124, 120)]}
# B #4: Bassoon 2's E flat 3 at 256-258 swells 8-10 dB inside the sample (CC11 and vol_db rise 1 dB) and was the loudest
# stem under Violins I's E flat 6 at 257: a slow -7 dB shape inside the note
LEVEL_SHAPES["Bassoon 2"] = LEVEL_SHAPES.get("Bassoon 2", []) + [[(256.9, 0.0), (257.15, -7.0), (257.85, -7.0), (258.05, 0.0)]]
# C #2: the basses' ff downbeat 204 (a 4.49 s note: AUTO_REBOW test), 152 and the Tempo I pedal 220 (followed by same-pitch
# notes) took no ABUT_LEAD and crossed over +0.165..+0.22 s late; listed onsets skip those two tests. 220 left out: its
# lead moves every re-bow of the fitted bars 65-70 pedal (c29-c30 fills, Do-not-touch)
ABUT_LEAD["Double basses"]["force_at"] = [152.0, 204.0]
# C #3: bar 79's triplet run into the ff B flat 6 trailed Flute 1 by 0.05-0.15 s (Sus run notes, the Leg BC lead capped
# at 0.091 s): run and target led together (movement I c20 rule)
GROUP_LEAD_AT = {"Violins I": [(261.5, 262.0, 0.15)], "Violins II": [(261.5, 262.0, 0.15)]}
# C #4: the same interval late every time: Flute 1 F5 -> E flat 5 (111, 118: +0.17..+0.19 s), Bassoon 1 D flat 4 -> B flat 3
# (36, 256: +0.15..+0.17)
LEG_PAIR_EXTRA_S["Flute 1"] = {(77, 75): 0.12}
LEG_PAIR_EXTRA_S["Bassoon 1"] = {(61, 58): 0.12}
# C #5: after a rest, wind first notes on Leg Slur MAX reached body - 6 dB 0.055 s before the beat (n = 15) and brass
# Leg Slur MAX 0.09 s before it (n = 7); wind Sus MAX entries with no lead +0.05 s late. Movement I's c03 extras were
# measured on louder first notes
ENTRY_LEAD_ART_S = {"wind": {"Leg Slur MAX": 0.06, "Leg Slur": 0.11, "Sus Non Vib": 0.07, "Sus MAX": 0.05}, "brass": {},
                    "Bassoon": {}, "Contrabassoon": {}}
# A #3a (S1): wind/brass same-pitch repeats: Bassoon 2's tenuto repeat at 253 dipped 0.5 dB (inside the sample's 4 Hz
# level wobble), bar 80's bassoon/contrabassoon/horn repeats 3.6-4.7 dB on the stems: a longer gap and a deeper fall
WIND_REP_RETONGUE_BY = {"Bassoon": {"gap_s": 0.09, "frac": 0.25, "fall_cc": 12, "fall_s": 0.15},
                        "Contrabassoon": {"gap_s": 0.09, "frac": 0.25, "fall_cc": 10, "fall_s": 0.15},
                        "Horn": {"gap_s": 0.08, "frac": 0.25, "fall_cc": 10, "fall_s": 0.15}}
# A #6: Clarinet 1 dipped 6.5 dB at the bar 81 breath (qn 268) against 16-24 dB for the other winds (the Leg Slur release
# trail fills the 0.12 qn gap): 0.2 qn gap and a CC11 fall (CC11 is only volume on the CL KS Master)
BREATH_GAP_AT["Clarinet 1"] = {266.0: 0.2}
BREATH_FALL_CC["Clarinet 1"] = {266.0: 14}
# (C #2) with the lead the basses' 152 and 204 notes play 4.6-4.7 s and would take a new, unfitted re-bow
AUTO_REBOW_SKIP = {"Double basses": [152.0, 204.0]}
# A #2 (S3): bar 63's sf tremolo: Violins II's vol_db stepped 4.5 dB down in one sample at 212.000 (the role boundary;
# the probe's 'Violins II 212 tremolo dip' since c27) and all four sections fell 7-16 dB over 212-213 after the hall,
# cutting the climax's ring under Trombone 1's entry. The fall below the 211.9 level now goes into CC7 (linear
# amplitude, before the hall) and vol_db holds that level (rises above it stay in vol_db); over 213-214.5 CC7 returns
# to 127 while vol_db takes the same fall slowly, so the product equals the c31 vol_db everywhere (computed from
# build/parts.json by cycles/c31/a2cc7.py; recompute if roles or shapes here change)
_C31_BAR63 = {"Violins I":{"cc7":[[211.9,127],[211.9625,118],[211.99,115],[211.999,118],[212.0,84],[212.025,94],[212.063,112],[212.0875,112],[212.1,111],[212.15,108],[212.2125,104],[212.225,103],[212.25,99],[212.275,94],[212.3375,85],[212.4,76],[212.4625,68],[212.5,64],[212.525,61],[212.54,59],[212.5875,56],[212.6,56],[212.65,54],[212.7125,52],[212.75,51],[212.775,51],[212.8375,49],[212.9,48],[212.9625,46],[213.0,45],[213.125,49],[213.25,54],[213.375,58],[213.5,64],[213.625,69],[213.75,76],[213.875,83],[214.0,90],[214.125,98],[214.25,107],[214.375,117],[214.5,127]],"shape":[[211.85,0.0],[211.9,-0.0],[211.9625,0.62],[211.99,0.89],[211.999,0.61],[212.0,3.58],[212.025,2.59],[212.063,1.08],[212.0875,1.12],[212.1,1.14],[212.15,1.42],[212.2125,1.76],[212.225,1.83],[212.25,2.2],[212.275,2.58],[212.3375,3.52],[212.4,4.46],[212.4625,5.4],[212.5,5.96],[212.525,6.41],[212.54,6.68],[212.5875,7.08],[212.6,7.19],[212.65,7.42],[212.7125,7.7],[212.75,7.87],[212.775,7.98],[212.8375,8.26],[212.9,8.54],[212.9625,8.82],[213.0,8.99],[213.125,8.24],[213.25,7.49],[213.375,6.74],[213.5,5.99],[213.625,5.24],[213.75,4.5],[213.875,3.75],[214.0,3.0],[214.125,2.25],[214.25,1.5],[214.375,0.75],[214.5,0.0]]},"Violins II":{"cc7":[[211.9,127],[211.9625,118],[211.99,115],[211.999,118],[212.0,71],[212.025,74],[212.063,79],[212.0875,74],[212.1,71],[212.15,60],[212.2125,49],[212.225,46],[212.25,42],[212.275,40],[212.3375,36],[212.4,32],[212.4625,29],[212.5,27],[212.525,26],[212.54,25],[212.5875,24],[212.6,23],[212.65,23],[212.7125,22],[212.75,22],[212.775,21],[212.8375,21],[212.9,20],[212.9625,19],[213.0,19],[213.125,22],[213.25,26],[213.375,31],[213.5,36],[213.625,42],[213.75,49],[213.875,58],[214.0,67],[214.125,79],[214.25,93],[214.375,108],[214.5,127]],"shape":[[211.85,0.0],[211.9,-0.0],[211.9625,0.62],[211.99,0.89],[211.999,0.61],[212.0,5.08],[212.025,4.69],[212.063,4.1],[212.0875,4.72],[212.1,5.04],[212.15,6.52],[212.2125,8.36],[212.225,8.73],[212.25,9.7],[212.275,10.08],[212.3375,11.02],[212.4,11.96],[212.4625,12.9],[212.5,13.46],[212.525,13.91],[212.54,14.18],[212.5875,14.58],[212.6,14.69],[212.65,14.92],[212.7125,15.2],[212.75,15.37],[212.775,15.48],[212.8375,15.76],[212.9,16.04],[212.9625,16.32],[213.0,16.49],[213.125,15.12],[213.25,13.74],[213.375,12.37],[213.5,10.99],[213.625,9.62],[213.75,8.25],[213.875,6.87],[214.0,5.5],[214.125,4.12],[214.25,2.75],[214.375,1.37],[214.5,0.0]]},"Violas":{"cc7":[[211.9,127],[211.9625,118],[211.99,115],[211.999,118],[212.0,119],[212.025,127],[212.063,127],[212.0875,127],[212.1,127],[212.15,127],[212.2125,127],[212.225,127],[212.25,121],[212.275,114],[212.3375,99],[212.4,85],[212.4625,74],[212.5,68],[212.525,64],[212.54,62],[212.5875,60],[212.6,59],[212.65,57],[212.7125,55],[212.75,54],[212.775,54],[212.8375,52],[212.9,50],[212.9625,49],[213.0,48],[213.125,52],[213.25,56],[213.375,61],[213.5,66],[213.625,72],[213.75,78],[213.875,85],[214.0,92],[214.125,99],[214.25,108],[214.375,117],[214.5,127]],"shape":[[211.85,0.0],[211.9,-0.0],[211.9625,0.62],[211.99,0.89],[211.999,0.61],[212.0,0.58],[212.025,-0.0],[212.063,-0.0],[212.0875,-0.0],[212.1,-0.0],[212.15,-0.0],[212.2125,-0.0],[212.225,-0.0],[212.25,0.45],[212.275,0.95],[212.3375,2.2],[212.4,3.46],[212.4625,4.71],[212.5,5.46],[212.525,5.91],[212.54,6.18],[212.5875,6.58],[212.6,6.69],[212.65,6.92],[212.7125,7.2],[212.75,7.37],[212.775,7.48],[212.8375,7.76],[212.9,8.04],[212.9625,8.32],[213.0,8.49],[213.125,7.78],[213.25,7.08],[213.375,6.37],[213.5,5.66],[213.625,4.95],[213.75,4.25],[213.875,3.54],[214.0,2.83],[214.125,2.12],[214.25,1.41],[214.375,0.71],[214.5,0.0]]},"Violoncellos":{"cc7":[[211.9,127],[211.9625,118],[211.99,115],[211.999,118],[212.0,119],[212.025,127],[212.063,127],[212.0875,127],[212.1,127],[212.15,127],[212.2125,127],[212.225,127],[212.25,127],[212.275,127],[212.3375,127],[212.4,127],[212.4625,127],[212.5,127],[212.525,121],[212.54,117],[212.5875,112],[212.6,111],[212.65,108],[212.7125,104],[212.75,102],[212.775,101],[212.8375,98],[212.9,95],[212.9625,92],[213.0,90],[213.125,93],[213.25,95],[213.375,98],[213.5,101],[213.625,104],[213.75,107],[213.875,110],[214.0,113],[214.125,117],[214.25,120],[214.375,123],[214.5,127]],"shape":[[211.85,0.0],[211.9,-0.0],[211.9625,0.62],[211.99,0.89],[211.999,0.61],[212.0,0.58],[212.025,-0.0],[212.063,-0.0],[212.0875,-0.0],[212.1,-0.0],[212.15,-0.0],[212.2125,-0.0],[212.225,-0.0],[212.25,-0.0],[212.275,-0.0],[212.3375,-0.0],[212.4,-0.0],[212.4625,-0.0],[212.5,-0.0],[212.525,0.41],[212.54,0.68],[212.5875,1.08],[212.6,1.19],[212.65,1.42],[212.7125,1.7],[212.75,1.87],[212.775,1.98],[212.8375,2.26],[212.9,2.54],[212.9625,2.82],[213.0,2.99],[213.125,2.74],[213.25,2.49],[213.375,2.24],[213.5,1.99],[213.625,1.74],[213.75,1.5],[213.875,1.25],[214.0,1.0],[214.125,0.75],[214.25,0.5],[214.375,0.25],[214.5,0.0]]}}
for _t, _d in _C31_BAR63.items():
    CC7_POINTS[_t] = CC7_POINTS.get(_t, []) + [tuple(x) for x in _d['cc7']]
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[tuple(x) for x in _d['shape']]]

# ---------- c32 (critics on the c31 render) ----------
# A #1 (BRIEF item 9): since c31 removed the brass entry lead, Trombone 1's 212.5 pickup started 0.054 qn later and the
# legato transition into the slurred accent at 213 played a brighter, louder sample (2-5 kHz first 80 ms -11.2 -> -0.8,
# peak -21.3 -> -17.8 dB, then a 13 dB fall); the c31 note trims 213/215 only deepened the fall. The c30 timing is back
# (entry_leads.json 212.5 0.11 s, trims removed). Bar 64: the tenuto 216 sat 4-8 dB under its neighbours (+3.5 dB over
# the note); 217.5's c29 +2.5 dB lift removed (it put the unaccented eighth over the 218 accent); 218 held up after the
# onset, before the printed decrescendo's CC11/CC1 fall (rising post-hall changes cut no tail)
LEVEL_SHAPES_S["Trombone 1"] = [s_ for s_ in LEVEL_SHAPES_S["Trombone 1"] if s_[0] != 217.5] + [
    (216.0, [(-0.02, 0.0), (0.05, 3.5), (1.0, 3.5), (1.1, 0.0)]),
    (218.0, [(0.15, 0.0), (0.25, 1.5), (0.34, 3.0), (0.5, 2.0), (0.7, 0.0)])]
# A #3: the violas' sotto voce portato (bars 48-51, Detache row, level in CC7 since c29): the A3s peaked 3-7 dB over the
# other pitches and level with the cor anglais solo in bar 48. Per-note CC7, written in the rests: A3 -4 dB (CC7 18),
# B3 +1.5 (33), D4 +3 (40), A flat 3 and E flat 4 unchanged (28)
CC7_POINTS["Violas"] = [p_ for p_ in CC7_POINTS["Violas"] if p_ not in ((152.2, 28), (167.98, 127))] + [
    (152.2, 18), (158.0, 33), (159.1, 28), (160.0, 18), (162.1, 40), (163.1, 33), (164.0, 28), (167.98, 127)]
# A #5 (S1): Violins II's merged tenuto repeat at 50 dipped 3.7 dB on the stem (net notch 6 CC): 10 CC net (KIT §6 portato)
# (the merged tenuto's TENUTO_BUMP takes 4 CC back, so 10 measured as 6: 14 for a net 10)
MERGE_NOTCH_AT = {"Violins II": {50.0: 14}}
# C #1: bar 63's sf on Flute 1 (A6, Leg Slur MAX into the top of the range, the sf CC11 spike, CC1 75 -> 110 and the sf
# vol_db weight) rose 11 dB over its own ff A flat 6 and set the delivery limiter (pre-limiter peak at qn 212.20): -7 dB in
# CC7 (before the hall, S3) from the legato onset of the A6 to its end
CC7_POINTS["Flute 1"] = CC7_POINTS.get("Flute 1", []) + [(211.9, 127), (211.96, 57), (213.0, 127)]
# C #3: bar 29's legato joins bumped the master 4-6 dB inside the f > p diminuendo (Violins I 86.0, Violins II 86.0 and
# 87.0, moved onsets 85.853 / 85.792 / 86.792); celli 77.0 (moved 76.817) +3.3 dB on the master
JOIN_NOTCH["Violins I"] = JOIN_NOTCH["Violins I"] + [(85.84, 85.98, -6.0)]
JOIN_NOTCH["Violins II"] = JOIN_NOTCH["Violins II"] + [(85.79, 85.95, -5.0), (86.78, 86.98, -5.5)]
JOIN_NOTCH["Violoncellos"] = JOIN_NOTCH["Violoncellos"] + [(76.82, 76.98, -4.0)]
# C #6: the bars 17-22 solo (1st Violins KS Master DIV A, Leg Slur MAX) at CC1 75-105 sat in the Sus Vib / Molto Vib
# crossfade (read in the .oib, c32: Sus Vib 1.0 to CC1 80, 0.83 at 90, 0.29 at 100; Molto Vib 0.01 at 68, 0.15 at 72,
# 0.43 at 80, 0.74 at 90; Non Vib 0.16 at 68, 0.1 at 72). Held at 72: mostly Sus Vib. Level refit after the render
CC1_HOLD = dict(CC1_HOLD, **{"Violin I solo": 72})

# ---- cycle 33 ----
# A #4 / C #5: the coda "4 soli" celli (qn 274-286, A flat 2 pedal) play on the half-section Violoncellos div track
# (Celli KS Master DIV A, already loaded; Close only) instead of the full section with META_DB; this window has no
# lowest pitch (the pedal is A flat 2). The div track skips META_DB (the patch is the half section). Level by stem fix.
TRACK_SPLITS["Violoncellos div"] = ("Violoncellos", [(51.0, 54.0), (62.0, 66.0), (274.0, 286.0, 0)], 55)
META_SKIP_TRACKS = {"Violoncellos div"}
# A #2b: Trombone 1's slurred 213 and 215 legato targets came back 11 dB brighter in 2-5 kHz in c31-c32 (same MIDI):
# c30's weight on pre-hall CC7 (85 = -3.5 dB, 95 = -2.5 dB), so the hall keeps ringing (S3)
CC7_POINTS["Trombone 1"] = CC7_POINTS.get("Trombone 1", []) + [
    (212.86, 127), (212.9, 85), (213.35, 85), (213.6, 127), (214.86, 127), (214.9, 95), (215.3, 95), (215.38, 127)]
# A #5: the dolce solo's legato targets at v124 (fastest transition); 72-80 = the longer transition (manual p.144);
# leg_leads.json gives these onsets +0.04 s
VEL_SET["Violin I solo"] = {**VEL_SET.get("Violin I solo", {}), **{
    48.5: 80, 49.0: 76, 50.0: 76, 51.0: 72, 53.0: 72, 60.5: 80, 61.0: 76, 62.0: 76, 63.0: 72}}
# A #6: harp D flat 4 sat 3.2 dB under its neighbours in the bars 53-56 triplets, A flat 4 -2.8, G flat 3 +4.1
HARP_PITCH_VEL = {**HARP_PITCH_VEL, 61: 6, 68: 4, 54: -5}
# A #6: the harmonics' passing C5 (275.5) still 1.3-2.1 dB over its neighbours: -5 -> -7 dB, 276 v66 -> 70
LEVEL_SHAPES_S["Harp harmonics"] = [s_ for s_ in LEVEL_SHAPES_S["Harp harmonics"] if s_[0] != 275.5] + [
    (275.5, [(-0.04, 0.0), (0.0, -7.0), (0.5, -7.0), (0.57, 0.0)])]
VEL_SET["Harp harmonics"][276.0] = 70
# the coda pedal entry played Sus MAX on the full section (a wide leap from the 271 C4); on the div track it would follow
# the bars 21-22 Leg Slur MAX row: keep it on Sus MAX like its re-bows
ART_SPANS["Violoncellos div"] = [{"from": 273.5, "to": 286.0, "art": "Sus MAX"}]

# ---------- c34 (critics on the c33 render) ----------
# C #1: the Largamente ff downbeat (204) fell 3-6 dB on Violins I/II and the celli (three envelope releases at 204: role
# [188,204,2], half the hairpin gain, c30's shape); held over bars 61-62 up to the 212 sf. Cadence (bars 79-80) -1.5 dB
# on every track, so the climax stays clearly the loudest after delivery (simulated: master Smax gap 2.3 -> 4.7 LU,
# mp3 1.0 -> 2.3 LU, limiter 2.2 dB). Slow ramps; the cadence fall comes after 267.75, under the decrescendo
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(204.0, 0.0), (204.2, 3.0), (211.6, 3.0), (211.9, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(204.0, 0.0), (204.2, 3.0), (211.6, 3.0), (211.9, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(204.0, 0.0), (204.2, 3.5), (211.6, 3.5), (211.9, 0.0)]]
LEVEL_SHAPES["_all"] = LEVEL_SHAPES.get("_all", []) + [[(261.75, 0.0), (262.25, -1.5), (267.75, -1.5), (268.25, 0.0)]]
# C #6: the soft hairpin gain of 172-178 was released over 178-181 just as the 180-184 crescendo starts (strings fell
# 3-6 dB at its start): held to the c30 mf hold-back at 184
for _t in ("Violins I", "Violins II", "Violoncellos"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES[_t] + [[(179.5, 0.0), (180.5, 2.5), (183.1, 2.5), (184.1, 0.0)]]
# A #3, C #2: Violins II's held pp C sharp 4 (220-223, CC11 34 flat) blooms 8 dB inside the Leg Slur MAX sample before
# the printed niente: a slow shape against it (1 s fall at a constant dynamic, no tail cut); the 223 re-bow fill -4 dB
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [
    [(220.75, 0.0), (221.0, -4.0), (221.75, -4.5), (222.0, -6.5), (222.5, -7.5), (222.85, -7.5), (222.95, 0.0)]]
# C #5: the only fp (bar 47) was a 0.27 s blip: f held 0.2 qn, p by 0.4 qn (CC11, pre-hall)
FP_SPIKE = ("f", 0.2, 0.4)
# C #3 (BRIEF item 8): the bass clarinet's tied pp A flat 2 (6-17, Sus Non Vib, 12.7 s) cycles in colour every 3.6-4.4 s
# (500-1000 Hz autocorrelation 0.94): split into three breaths on its own row (REBOW_ART_BY, new generic option); the
# dead re-tongue points 9/12/15 (the notes are tied in v600) removed
REBOW_AT["Bass clarinet"] = [10.0, 13.5]
REBOW_ART_BY = {"Bass clarinet": "Sus Non Vib"}
REP_RETONGUE_AT["Bass clarinet"] = []
# A #4: Trombone 1's quotation evened: c29's 215 lift +4.5 -> +1.5 dB (215 had the brightest front of the passage and
# sat level with the 213 accent); the new-slur heads 214.5 and 217 +2 -> +4 dB held to 0.40 s; the tenuto repeat 216
# re-tongued with a longer gap and a deeper CC11 fall (S1: dipped 1.5 dB)
LEVEL_SHAPES_S["Trombone 1"] = [s_ for s_ in LEVEL_SHAPES_S["Trombone 1"] if s_[0] not in (214.5, 215.0, 217.0)] + [
    (215.0, [(-0.02, 0.0), (0.03, 1.5), (0.50, 1.5), (0.60, 0.0)]),
    (214.5, [(-0.01, 0.0), (0.04, 4.0), (0.40, 4.0), (0.50, 0.0)]),
    (217.0, [(-0.01, 0.0), (0.04, 4.0), (0.40, 4.0), (0.50, 0.0)])]
# A #6 (S1): repeats not heard as two notes. Cor anglais 271 (slurred repeat, new p): merge notch 8 -> 20 CC; Horn 3
# (muted/soft, 265 and 289): 0.12 s gap with a CC11 fall (kit section 7: soft horns need longer gaps); Violins II 50 14 -> 18
MERGE_NOTCH_AT["Cor anglais"] = {271.0: 20}
MERGE_NOTCH_AT["Violins II"][50.0] = 18
WIND_REP_RETONGUE_BY = {"Horn 3": {"gap_s": 0.12, "frac": 0.25, "fall_cc": 10, "fall_s": 0.15},
                        "Trombone 1": {"gap_s": 0.14, "frac": 0.25, "fall_cc": 16, "fall_s": 0.15},
                        **WIND_REP_RETONGUE_BY}
# A #2: the basses' pedal pieces swelled +4 dB and fell -6 dB at +1.2..+2.4 s, outside fit_rebows' 1.5 s window: those
# pedals refitted with the new --window "Double basses:2.6" (rebow_fills.json, re-levelled to the c29-c33 piece means).
# 273.229 keeps no fill (c29); its +5 dB bump at +1.5..+1.9 s (-49 against -56 dB) taken out by a shape
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [[(274.24, 0.0), (274.38, -5.0), (274.55, -5.0), (274.67, 0.0)]]

# ---------- c35 (critics on the c34 render) ----------
# A #1: bar 63's "trem. sf" entered softer than the bar 62 tenuto it leaves on Violins I (-3.7 dB) and the celli (-1.7):
# c34's climax hold (+3/+3.5 to 211.6) now ends by 211.5 on those two, the c31 CC7 lane's dip at the head of Violins I's
# sf (CC7 84/94/112 at 212.0/212.025/212.063, -3.6..-1.0 dB) is lifted, and a 2.5 dB sf weight falls back with the CC7 fall
for _t, _h in (("Violins I", 3.0), ("Violoncellos", 3.5)):
    LEVEL_SHAPES[_t] = [s_ for s_ in LEVEL_SHAPES[_t] if s_ != [(204.0, 0.0), (204.2, _h), (211.6, _h), (211.9, 0.0)]] + [
        [(204.0, 0.0), (204.2, _h), (211.0, _h), (211.5, 0.0)],
        [(211.98, 0.0), (212.02, 2.5), (212.15, 2.5), (212.5, 0.0)]]
CC7_POINTS["Violins I"] = [(q_, {212.0: 127, 212.025: 127, 212.063: 118}.get(q_, v_)) for q_, v_ in CC7_POINTS["Violins I"]]
# A #2 (BRIEF item 8): the bass clarinet pedal's c28 roles were fitted to the single note's sample swell; since the c34
# split (10/13.5) each new piece starts without it (-3.2..-4.8 dB at 10-12.5). Refit as one shape that lands with each piece
LEVEL_SHAPES["Bass clarinet"] = LEVEL_SHAPES.get("Bass clarinet", []) + [
    [(7.5, 0.0), (8.0, -1.0), (8.45, -1.0), (8.55, -4.0), (8.95, -4.0), (9.05, -9.5), (9.97, -9.5), (10.03, -3.0),
     (12.45, -3.0), (12.55, -5.5), (12.97, -5.5), (13.03, -6.0), (13.47, -6.0), (13.53, -3.0), (16.75, -3.0), (17.25, 0.0)]]
# A #4: the violas' pizz. pp crescendo of bar 41 played as a +9 dB step on beat 3 (role [123.6, 125.95, -4, 0.3]
# ending): a ramp over the bar instead
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [
    [(123.1, 0.0), (123.6, -4.0), (124.0, -4.0), (124.95, -3.0), (125.05, 1.8), (125.9, 1.8), (126.0, -1.5), (127.0, -1.0), (127.9, 0.0)]]
# A #6: the p stroke at 172 (a tempo, bar 53) stood only 1-2 dB over the crescendo roll into it: +3 dB on the stroke
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(171.96, 0.0), (171.99, 3.0), (172.5, 3.0), (172.9, 0.0)]]
# B #2: the violas 5-6 dB under Violins II at the ff of bars 61, 78 and 79 (c34's hold raised the violins and celli only)
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [
    [(204.0, 0.0), (204.2, 2.5), (207.8, 2.5), (208.2, 1.0), (211.6, 1.0), (211.9, 0.0)],
    [(258.6, 0.0), (259.0, 2.5), (265.6, 2.5), (266.0, 1.0), (267.75, 1.0), (268.25, 0.0)]]
LEVEL_SHAPES["Violas div"] = LEVEL_SHAPES.get("Violas div", []) + [[(265.9, 0.0), (266.0, 1.0), (267.75, 1.0), (268.25, 0.0)]]
# B #4: Flute 1's counter-line (bars 41-44, pp < p > pp) ended 11-13 dB under the cor anglais, one printed step louder
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES.get("Flute 1", []) + [[(133.8, 0.0), (134.3, 5.0), (138.0, 5.0), (138.3, 3.0), (139.0, 3.0), (139.5, 0.0)]]
# B #5: Oboe 1's p pickup at 139 masked by the celli's pp legato transition head into 140 (up to 9 dB over it)
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(139.3, 0.0), (139.5, -7.0), (140.15, -7.0), (140.4, 0.0)]]
# C #1 (S2): re-attacks straight after the previous note with no lead (slur breaks, row changes, wide leaps, the tutti
# re-entry) arrived 0.15-0.37 s late against their unison partners: REATTACK_LEAD_AT (new generic option), start values
# = measured body - 6 dB minus about 0.05 s
REATTACK_LEAD_AT = {
    "Violins I": {249.0: 0.18, 72.0: 0.20},
    "Violins II": {218.0: 0.25},
    "Violas": {218.0: 0.12, 252.5: 0.25, 266.0: 0.15},
    "Horn 1": {208.0: 0.20, 210.0: 0.10, 196.0: 0.10},
    "Horn 2": {210.0: 0.15},
    "Horn 3": {210.0: 0.08, 267.0: 0.12},
    "Oboe 1": {210.0: 0.20},
    "Oboe 2": {267.0: 0.25},
    "Flute 1": {116.0: 0.15},
    "Bassoon 1": {144.0: 0.12, 198.0: 0.15, 261.0: 0.12},
    "Clarinet 2": {256.0: 0.12},
}

# ---------- c36 (critics on the c35 render) ----------
# A #2 (S1): Flute 1's slurred repeat E flat 5 at 136 (merged, notch 8 CC) dipped only 3.1 dB under the flute's own
# vibrato troughs since c35 made it the exposed line: 14 CC (c34: 20 on the cor anglais gave a 10-15 dB hole)
MERGE_NOTCH_AT["Flute 1"] = {136.0: 14}
# A #3: the violas' 248 / 252.5 (a slur's last note, merged with the next slur's same-pitch first note) took the new
# slur and started unled on the slow first-note layer (-6..-8 dB for 0.9 s): keep their own slur (new generic option);
# the c35 re-attack lead on 252.5 goes (it is a legato target again)
MERGE_JOIN_OWN_SLUR_AT = {"Violas": [248.0, 252.5]}
REATTACK_LEAD_AT["Violas"] = {k_: v_ for k_, v_ in REATTACK_LEAD_AT["Violas"].items() if k_ != 252.5}
REATTACK_LEAD_AT["Violas"][83.0] = 0.12
# B #1: bar 28: the celli's A flat 3 at 81 (c28 early fill + the sample's own swell) sat 7.8 dB over their printed f
# arrival at 82; the main violas' D flat 4 at 81 re-attacked on Leg Slur MAX's slow first-note layer (13-19 dB hole):
# 81 and its printed repeat at 82 on Sus MAX (a Leg Slur MAX repeat at 82 would hit the same layer); the new slur's F4
# at 83 then starts on Leg Slur MAX after a Sus note (a row change): re-attack lead 0.12 s
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [
    [(80.9, 0.0), (81.1, -5.0), (81.65, -5.0), (81.9, 4.0), (82.6, 4.0), (83.2, 0.0)]]
ART_SPANS["Violas"] = ART_SPANS["Violas"] + [{"from": 80.95, "to": 82.5, "art": "Sus MAX"}]
# B #2: the f roll of bars 61-62 settled 4 dB lower in the envelope than the same f roll of bars 79-80, under a louder
# tutti (100-300 Hz 13-18 dB under the tutti against 8-10): +5 dB over the roll, released before the 209.5 stroke
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(203.98, 0.0), (204.05, 5.0), (209.4, 5.0), (209.47, 0.0)]]
# C #2: Horn 1's bar 61 attack (c33 role [203.95, 208, 4.5, 0.25] lifts the bloom too) was the loudest 50 ms of the piece
# and set the delivery limiter (2.5 dB): the role (build/roles.json) replaced by a shape that keeps the lift off the front
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES.get("Horn 1", []) + [
    [(203.95, 0.0), (204.15, -1.0), (204.6, 0.0), (205.0, 4.5), (207.75, 4.5), (208.0, 0.0)]]

# ---------- c37 (critics on the c36 render) ----------
# A #1 (S1): Flute 1's slurred repeat E flat 5 at 136 stayed inaudible with a 14 CC merge notch (minimum 0.2 dB under
# the flute's own vibrato troughs): no merge; 136 plays the re-tongued repetition sample (LegRep RRx4, manual p.109-110,
# the samples the Leg Slur Rep script uses). 136 is the slur's last note, so no legato join follows the row change
WIND_SLUR_REP_MERGE_SKIP = {"Flute 1": [136.0]}
MERGE_NOTCH_AT.pop("Flute 1", None)
ART_SPANS["Flute 1"] = [{"from": 135.95, "to": 139.5, "art": "LegRep RRx4"}]
# B #2: Clarinet 1's held ff F5 at 204 swells about 4 dB inside the sample (207-208) over Oboe 1 and Horn 1 on the
# same pitch: flatten it pre-hall in CC7 (linear amplitude; 106/90/80 = -1.6/-3.0/-4.0 dB)
CC7_POINTS["Clarinet 1"] = CC7_POINTS.get("Clarinet 1", []) + [
    (205.0, 127), (205.75, 106), (206.5, 90), (207.0, 80), (208.0, 80), (208.75, 101), (209.5, 113), (209.9, 127)]
# B #3: bars 61-62: the brass chord sat 6-8 dB under the strings (horns ff, low brass f) while the bar 79 f horns sit
# level with the violins: brass +3 dB over 204-211.9 (rises only), Horn 1 +3 on its c36 lift only (front kept off),
# and 1 dB back from the c34 string holds (Violins I and celli end at 211.5 since c35)
for _t in ("Horn 2", "Horn 3", "Trombone 2", "Bass trombone", "Tuba"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(204.0, 0.0), (204.15, 3.0), (211.6, 3.0), (211.9, 0.0)]]
LEVEL_SHAPES["Horn 1"] = [s_ for s_ in LEVEL_SHAPES["Horn 1"] if s_[0][0] != 203.95] + [
    [(203.95, 0.0), (204.15, -1.0), (204.6, 0.0), (205.0, 7.5), (207.75, 7.5), (208.0, 3.0), (211.6, 3.0), (211.9, 0.0)]]
for _t, _v in (("Violins I", 3.0), ("Violins II", 3.0), ("Violoncellos", 3.5)):
    LEVEL_SHAPES[_t] = [[(a_, (b_ - 1.0 if b_ == _v else b_)) for a_, b_ in s_]
                        if (len(s_) == 4 and s_[0] == (204.0, 0.0) and s_[1] == (204.2, _v)) else s_
                        for s_ in LEVEL_SHAPES[_t]]
# B #4: bar 28: the main violas' F4 at 83 (Leg Slur MAX after the Sus MAX repeat) sat 6-9 dB over both violin
# sections inside the printed decrescendo: -6 dB pre-hall in CC7 from just after its moved onset (82.90) to just after
# the 84 target's start
CC7_POINTS["Violas"] = CC7_POINTS["Violas"] + [(82.93, 127), (82.98, 64), (83.95, 64), (84.05, 127)]
# A #2: the basses' coda A flat 1 pedal piece from 273.229 swings -6/+7 dB in 3 s, the same in c34-c36 (150 ms windows:
# -59..-62 at 273.5-273.6, 274.0-274.1, 274.7-274.8, 275.1-275.2; -47 at 275.5-275.6 where the next piece attacks):
# a level shape fitted to the c36 stem toward -54 dB (the c34 274.24-274.67 shape kept); the 276.05 fill's front lowered
# in build/rebow_fills.json
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [
    [(273.35, 0.0), (273.5, 4.0), (273.65, 4.5), (273.75, 2.0), (273.85, 1.5), (273.95, 3.0), (274.05, 5.0),
     (274.15, 7.0), (274.25, 3.0), (274.32, 0.0), (274.7, 0.0), (274.75, 3.5), (274.85, 4.0), (274.95, 0.5),
     (275.05, 0.0), (275.12, 3.0), (275.25, 6.0), (275.32, 0.0), (275.4, -3.5), (275.5, -6.0), (275.65, -6.0),
     (275.75, -2.5), (275.85, 0.0)]]
# c37 after the render: the LegRep RRx4 note at 136 played its body 8-11 dB over the merged Leg Slur MAX note it
# replaced (4-6 dB over the cor anglais at pp); its re-attack (+3 dB over the 135 note) is kept, the body brought back
# to about -48 dB (stem_fix + --mix-only)
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES["Flute 1"] + [
    [(136.4, 0.0), (136.52, -3.0), (136.62, -8.5), (137.0, -9.0), (137.4, -8.5), (137.8, -6.5),
     (138.2, -4.0), (138.6, -5.0), (139.0, -6.0), (139.5, -4.0), (139.7, 0.0)]]

# ---- c38 (actor; the hall went drier this cycle: fx_volume 0.19 -> 0.095, hall low cut 160 Hz, so level-only fixes) ----
# B #1: bar 81: the cadence `_all` -1.5 and the strings' [262, 268, -1.5] roles ended at 268, where the printed
# decrescendo ff -> p starts (a 0.7 dB master rise on its first beat; violas/celli over the melody): every non-melody
# track holds the -1.5 to the p chord at 271 (a new onset everywhere, so no tail is cut); roles in roles.json
for _t in ("Flute 2", "Oboe 2", "Cor anglais", "Clarinet 2", "Bass clarinet", "Bassoon 1", "Bassoon 2", "Contrabassoon",
           "Horn 3", "Horn 4", "Horns 1-2 a2", "Timpani", "Violas", "Violoncellos", "Double basses"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(267.75, 0.0), (268.25, -1.5), (270.75, -1.5), (271.0, 0.0)]]
# B #2: bar 56: the celli half notes swell 5 dB inside the sample at +0.75 qn over the mf violin theme: -5 dB pre-hall
CC7_POINTS["Violoncellos"] = CC7_POINTS.get("Violoncellos", []) + [
    (184.35, 127), (184.55, 71), (185.0, 71), (185.2, 127), (186.35, 127), (186.55, 71), (187.0, 71), (187.2, 127)]
# B #3: coda: Clarinet 1's pp solo bumps 4-5 dB at 283 and at 292 (on the violins' C5 entry): pre-hall CC7
CC7_POINTS["Clarinet 1"] = CC7_POINTS["Clarinet 1"] + [
    (282.6, 127), (282.75, 85), (283.1, 85), (283.3, 127), (291.4, 127), (291.9, 85), (292.1, 80), (292.35, 95), (292.5, 127)]
# B #4: bar 80: the cor anglais' inner A flat 4 over the melody: -3 dB pre-hall on top of its -3 note trim
CC7_POINTS["Cor anglais"] = CC7_POINTS.get("Cor anglais", []) + [(265.95, 127), (266.05, 90), (267.9, 90), (268.0, 127)]
# B #5: bars 29-30: the main violas' E flat 4 drops 7 dB at its 86.861 re-bow piece under the div half: rises only
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(86.95, 0.0), (87.1, 6.0), (89.0, 6.0), (90.0, 2.0), (90.3, 0.0)]]
# C #1: bar 66 niente: the basses' pedal rose 5 dB (225.215 piece) while the upper strings died away: slow cut
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [
    [(224.0, 0.0), (224.5, -3.0), (225.0, -4.0), (226.25, -4.0), (226.35, 0.0)]]
# C #2: bars 54-57: c34's 180.5-183.1 hold ended into c30's mf hold-back, a 5-6.5 dB envelope step down at the mf of
# 184: both shapes replaced by one rising shape (simulated monotone 178-196 in the master and the mp3)
_c38_old = ([(183.5, 0.0), (184.25, -2.5), (187.75, -2.5), (188.5, 0.0)], [(183.5, 0.0), (184.25, -2.5), (187.75, -2.5), (188.0, 0.0)],
            [(179.5, 0.0), (180.5, 2.5), (183.1, 2.5), (184.1, 0.0)])
for _t in ("Violins I", "Violins II", "Violoncellos"):
    _n0 = len(LEVEL_SHAPES[_t])
    LEVEL_SHAPES[_t] = [s_ for s_ in LEVEL_SHAPES[_t] if list(map(tuple, s_)) not in [list(o_) for o_ in _c38_old]]
    assert _n0 - len(LEVEL_SHAPES[_t]) == 2, (_t, _n0, len(LEVEL_SHAPES[_t]))
    LEVEL_SHAPES[_t] = LEVEL_SHAPES[_t] + [
        [(179.5, 0.0), (180.5, 2.0), (183.1, 2.0), (184.25, 0.5), (187.75, 1.0), (190.0, 2.0), (193.0, 1.0), (196.0, 0.0)]]
# C #3: the violas' decrescendo into bar 65 turned into a +6 dB jump at the pp (their pp soft trim): held down
# through the niente (the c30 niente CC7 lane still runs on top)
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(219.5, 0.0), (219.85, -5.0), (225.9, -5.0), (226.1, 0.0)]]

# ---- c39 (critics on the c38 render, the first with the drier hall; level and timing changes, no Opus state change) ----
# B #2: bars 61-62: the Violins I melody (C sharp 6 at 204/206) level with or under Horn 1, Violins II, Trombone 2 and the
# celli over 205-207.5: Violins I +3 dB there (a rise), Horn 1's c37 lift 7.5 -> 5.5, Violins II -2.5 dB pre-hall in CC7
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(204.9, 0.0), (205.15, 3.0), (207.6, 3.0), (207.8, 0.0)]]
_c37_hn1 = [(203.95, 0.0), (204.15, -1.0), (204.6, 0.0), (205.0, 7.5), (207.75, 7.5), (208.0, 3.0), (211.6, 3.0), (211.9, 0.0)]
assert _c37_hn1 in [list(map(tuple, s_)) for s_ in LEVEL_SHAPES["Horn 1"]]
LEVEL_SHAPES["Horn 1"] = [s_ for s_ in LEVEL_SHAPES["Horn 1"] if list(map(tuple, s_)) != _c37_hn1] + [
    [(203.95, 0.0), (204.15, -1.0), (204.6, 0.0), (205.0, 5.5), (207.75, 5.5), (208.0, 3.0), (211.6, 3.0), (211.9, 0.0)]]
CC7_POINTS["Violins II"] = CC7_POINTS.get("Violins II", []) + [(205.85, 127), (205.95, 95), (207.0, 95), (207.6, 127)]
# B #1: bars 79-80: Violins II's automatic re-bow at 263.921 blooms 4.6-6.3 dB over the Violins I / Flute 1 B flat 6:
# -4.5 dB pre-hall in CC7 to the 266 note (moved onset 265.81); Violins I's 264.417 re-bow fill +2.5 dB after 0.6 s
# (build/rebow_fills.json)
CC7_POINTS["Violins II"] = CC7_POINTS["Violins II"] + [(263.94, 127), (264.0, 76), (265.75, 76), (265.8, 127)]
# A #1 (BRIEF item 9): Trombone 1's 213 accent and 215 legato target lost 3.5-4 dB in the c38 rebuild with identical
# data (the accent no longer stood over its pickup in the master): the c33 CC7 floors raised 85 -> 110, 95 -> 120
CC7_POINTS["Trombone 1"] = [(q_, {(212.9, 85): 110, (213.35, 85): 110, (214.9, 95): 120, (215.3, 95): 120}.get((q_, v_), v_))
                            for q_, v_ in CC7_POINTS["Trombone 1"]]
# C #2 (S2): bar 25 "tutti": Violins I's C5 re-entry is a Leg Slur MAX target at v63 (the slow transition, manual
# p.144) and lands 0.33 s behind Violins II's v124 on the same pitch: v124 (velocity sets transition speed only)
VEL_SET["Violins I"] = {**VEL_SET.get("Violins I", {}), 72.0: 124}
# A #3 (S1): printed separate repeats rendered as one note. Violins II 289/292 (pp con sord.): notches back (289 also
# keeps its re-bow, its fill's lift scaled by 0.6 in rebow_fills.json), 292 12 CC; violas 62 and Violas div 70/79
# (unslurred, merged with the soft 8 CC notch): 16 CC; basses' Sus MAX repeats re-tongued (0.06 qn gap)
NOTCH_SKIP["Violins II"] = [q_ for q_ in NOTCH_SKIP["Violins II"] if q_ not in (289.0, 292.0)]
MERGE_NOTCH_AT["Violins II"][292.0] = 12
MERGE_NOTCH_AT["Violas"] = {**MERGE_NOTCH_AT.get("Violas", {}), 62.0: 16}
MERGE_NOTCH_AT["Violas div"] = {**MERGE_NOTCH_AT.get("Violas div", {}), 70.0: 16}   # 79 is not merged by this path (open)
REP_RETONGUE_AT["Double basses"] = REP_RETONGUE_AT.get("Double basses", []) + [144.0, 156.0, 168.0, 253.0, 265.0]
# the gap only grows 0.03 -> 0.06 qn, so also a pre-hall CC7 fall (100 = -2.1 dB) over the last 0.12 qn into each onset
for _q in (144.0, 156.0, 168.0, 253.0, 265.0):
    CC7_POINTS["Double basses"] = CC7_POINTS.get("Double basses", []) + [(_q - 0.15, 127), (_q - 0.03, 100), (_q, 127)]
# B #4: bars 66-70: the basses' pp 4-soli E flat pedal 14-18 dB under Horn 1's p-mp solo (one printed step is about
# 5 dB here): +3 dB from Horn 1's entry to the tutti note at 238 (a rise after c38's niente cut; ends on a new onset)
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(226.0, 0.0), (226.5, 3.0), (237.6, 3.0), (238.0, 0.0)]]
# C #1 fallback: the caesura before bar 61 stretched beat 4 of bar 60 to 47 bpm while the strings play straight through
# (only the winds breathe), so the stretch sounded like the crescendo dragging: 0.22 -> 0.10 s. The fresh-stroke test
# (FRESH_AT) is left open: undoing the strings' legato targets at the climax downbeat risks the slow first-note layer
CAESURA[204.0] = 0.10

# ---- c40 (ONE_TIME: Movement I c44's fixes for Dan's "too wet, mushy"; critics A/B/C on the c39 render) ----
# ONE_TIME #3 (Dan's S1): STR_REP_NEW_BOW (generic, ported from movement I c44/c45). Same-pitch string repeats that the
# legato merge joined become new bows: loud / accented / slur-head strokes (fresh Sus MAX after a min(0.06 s, 25%) gap,
# with the 0.10 s re-tongue lead), slurred tenutos as portato strokes, soft repeats a re-bow point at the printed onset
# in place of the CC11 notch. sus_min_s: unslurred Sus MAX -> Sus MAX repeats at mf or more (basses from pp, A #2) get
# the gap and lead
STR_REP_NEW_BOW = {"gap_s": 0.06, "frac": 0.25, "stroke_cc": DYN["mf"], "stroke_mark": "mp", "head_cc": DYN["p"],
                   "sus_min_s": 0.4, "sus_lead_s": 0.10, "sus_cc_by": {"Double basses": DYN["pp"]},
                   "portato": {"gap_s": 0.05, "frac": 0.25, "fall_cc": 6, "fall_cc_loud": 8, "fall_s": 0.04}}
# A #2: the c39 notches that had no measured effect come out (the rule's soft re-bows replace them); Violins II 289
# back into NOTCH_SKIP (it is a re-bow point); the listed points that put three bow events in about 2 qn next to the
# printed ones go (Violins II 290.9/293.0, Violas div 287.3/288.6; their rebow_fills rows removed)
MERGE_NOTCH_AT["Violins II"].pop(292.0, None)
MERGE_NOTCH_AT["Violas"].pop(62.0, None)
MERGE_NOTCH_AT["Violas div"].pop(70.0, None)
NOTCH_SKIP["Violins II"] = NOTCH_SKIP["Violins II"] + [289.0, 292.0]
REBOW_AT["Violins II"] = [q_ for q_ in REBOW_AT["Violins II"] if q_ not in (290.9, 293.0, 45.0, 51.0)]
# (Violins II 45 / 51, c28's re-bows on the printed new slurs: the rule now plays 45 as a stroke (p slur head) and 51 as a
# soft re-bow; a listed point on 45 made it a REBOW_VEL piece with no lead and an unjoined next note)
REBOW_AT["Violas div"] = [q_ for q_ in REBOW_AT["Violas div"] if q_ not in (287.3, 288.6)]
# (Violas div's 292 is not a printed repeat, so 291.7 stays as the loop point of the 289-295.3 piece; 79, merged into
# the 78 note without a notch, gets its printed re-bow)
REBOW_AT["Violas div"] = sorted(REBOW_AT["Violas div"] + [79.0])
# basses: 144 (pp new slur head after the same pitch) is a fresh Sus MAX stroke that 146 joins from; 156/168/253/265 go
# to sus_min_s (gap + lead) instead of REP_RETONGUE_AT; the c39 CC7 falls (no measured effect) are removed
DOWNBOW_STROKE_AT["Double basses"] = [144.0]
REP_RETONGUE_AT["Double basses"] = [q_ for q_ in REP_RETONGUE_AT["Double basses"]
                                    if q_ not in (144.0, 156.0, 168.0, 253.0, 265.0)]
CC7_POINTS["Double basses"] = [p_ for p_ in CC7_POINTS["Double basses"]
                               if not any(abs(p_[0] - (_q + d_)) < 1e-6 for _q in (144.0, 156.0, 168.0, 253.0, 265.0)
                                          for d_ in (-0.15, -0.03, 0.0))]
# A #2: the celli's bar 23 "unis., cantabile" counter-melody head (66) merged into the held E flat 3: a stroke
DOWNBOW_STROKE_AT["Violoncellos"] = [66.0]
# A #3: Violins II sul tasto (bars 37-40, Flautando, pp): the printed half/quarter-note repeats get re-bows at the printed
# onsets; listed points inside a note replace its automatic ones (110.053, 113.7, 116.097, 119.877 and 111.198 removed
# with their rebow_fills rows)
REBOW_AT["Violins II div"] = sorted(REBOW_AT.get("Violins II div", []) + [114.0, 116.0, 119.0, 120.0])
REBOW_AT["Violins II"] = sorted(REBOW_AT["Violins II"] + [112.0, 120.0])
AUTO_REBOW_SKIP["Violins II div"] = [108.0]   # bar 37's printed 4 qn note (4 s) keeps one bow (110.053 removed)
# A #1 (S2): bar 25 "tutti, con sord." is the leader rejoining, not new players: Violins I's C5 at 72 is a Leg BC MAX
# target (BC_NEWP_KEEP, new generic option) with the normal leg lead and its v124; the c35 re-attack lead and the c30
# join notch over the old hole come out
BC_NEWP_KEEP = {"Violins I": [72.0]}
REATTACK_LEAD_AT["Violins I"].pop(72.0, None)
JOIN_NOTCH["Violins I"] = [j_ for j_ in JOIN_NOTCH["Violins I"] if j_ != (71.90, 72.08, -4.5)]
# A #4: Trombone 1 215 sagged 4-5 dB under the 214.5 slur head: head +4 -> +2.5, 215 +1.5 -> +2.5
LEVEL_SHAPES_S["Trombone 1"] = [s_ for s_ in LEVEL_SHAPES_S["Trombone 1"] if s_[0] not in (214.5, 215.0)] + [
    (215.0, [(-0.02, 0.0), (0.03, 2.5), (0.50, 2.5), (0.60, 0.0)]),
    (214.5, [(-0.01, 0.0), (0.04, 2.5), (0.40, 2.5), (0.50, 0.0)])]
# A #5: Horn 2's same-pitch D flat 4 tenuto at 208 (ff, unslurred) re-tongued
REP_RETONGUE_AT["Horn 2"] = REP_RETONGUE_AT.get("Horn 2", []) + [208.0]
# B #3: Trombone 2 (printed f) level with the ff Violins I melody at 208-210: -2.5 dB pre-hall on the 208 note
CC7_POINTS["Trombone 2"] = CC7_POINTS.get("Trombone 2", []) + [(207.90, 127), (207.97, 95), (209.90, 95), (209.97, 127)]
# B #4: coda Horn 4 2-5 dB over Horn 3 at the same pp con sord.: -3 dB, set in its rest (271.1-286)
CC7_POINTS["Horn 4"] = CC7_POINTS.get("Horn 4", []) + [(280.0, 127), (280.1, 90)]

# ---- c41 (coordinator: release caps 300/400 ms in build/mix.json; critics A/B/C on the c40 render) ----
# B #1 (finding 2 of the extra check): c40's +1.5 gain and refitted pedal fills already raised the basses' 4-soli pedal
# about 3 dB over c39, so c39 B #4's +3 at 226-238 is undone (the pedal sat within 0.4-3.2 dB of Horn 1's solo)
_c39_cb = [(226.0, 0.0), (226.5, 3.0), (237.6, 3.0), (238.0, 0.0)]
assert _c39_cb in [list(map(tuple, s_)) for s_ in LEVEL_SHAPES["Double basses"]]
LEVEL_SHAPES["Double basses"] = [s_ for s_ in LEVEL_SHAPES["Double basses"] if list(map(tuple, s_)) != _c39_cb]
# B #2: bars 79-80: c39's Violins II CC7 -4.5 dB now stacks on the c40 refit's fill on the same 263.921 re-bow: -2.0 dB
# (76 -> 101), pre-hall, same times (Violins I's 264.417 fill +2.5 from 0.6 s goes back into build/rebow_fills.json)
CC7_POINTS["Violins II"] = [(q_, 101 if (abs(q_ - 264.0) < 1e-6 or abs(q_ - 265.75) < 1e-6) and v_ == 76 else v_)
                            for q_, v_ in CC7_POINTS["Violins II"]]
# B #3: bars 56-58: Horn 1's mp espr. counter-melody fell 9-17 dB under the violins' theme; the 182 note's body collapses
# 11-13 dB under its head: +5 dB inside the note, back to 0 before the 184 legato target (no tail cut). The soft shelf
# (build/mix.json loud_eq) ramps out by 182
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(182.6, 0.0), (182.95, 5.0), (183.8, 5.0), (183.9, 0.0)]]
# A #2: Trombone 1's slur 214.5 -> 215 (ff marcato quotation) dipped 8 dB in the stem for 0.15 s: the two c40 shapes made
# a 2.5 dB V exactly at the transition; now +2.5 held from 214.54 through 215, and 215's legato velocity 112 -> 124
# (brass legato velocity sets the transition speed, manual p.104-105)
LEVEL_SHAPES_S["Trombone 1"] = [s_ for s_ in LEVEL_SHAPES_S["Trombone 1"] if s_[0] not in (214.5, 215.0)] + [
    (214.5, [(-0.01, 0.0), (0.04, 2.5), (0.60, 2.5)]),
    (215.0, [(-0.02, 2.5), (0.03, 2.5), (0.50, 2.5), (0.60, 0.0)])]
VEL_SET["Trombone 1"][215.0] = 124
# A #3 (S1): the c40 portato strokes (Violins II 44 / 50) fell 12-18 dB to holes inside their louré slur: gap 0.05 ->
# 0.03 s, CC11 fall 6/8 -> 3/4 CC (44's level under the printed cresc.: note_trims.json Violins II 44 +4)
STR_REP_NEW_BOW["portato"] = dict(STR_REP_NEW_BOW["portato"], gap_s=0.03, fall_cc=3, fall_cc_loud=4)
# A #3d: basses 144 (pp, under the B flat minor head) played as a stroke peaked 7.2 dB over its body. Taking it out of
# DOWNBOW_STROKE_AT left it an unled Leg Slur MAX slur head (the slow first-note layer; it is not a sus gap, being on a
# legato row), so it stays a stroke and its peak is levelled after the render (LEVEL_SHAPES_S, fitted on the stem)
# A #1 watch: the basses' pp sus-gap repeats 156 / 168 separated 9-11 dB only because the 150 ms cap emptied the 0.06 s
# gap; with 400 ms at pp the release fills it again (c39, uncapped: -1.8..2.5 dB). A CC11 fall over the last 0.06 s
# before the gap (pre-hall, on the releasing voice; new generic "sus_fall")
STR_REP_NEW_BOW["sus_fall"] = {"Double basses": {"cc": 10, "s": 0.06, "max_cc": DYN["p"]}}
# ---- c41 after the render (level only, post-hall; applied by stem fix and --mix-only) ----
# A #3 re-measured with the 400 ms pp/p caps (stem, pre / min / body): Violoncellos 128 -40 / -53 / -44 and Violas 248.5
# -42 / -55 / -46 still fall 13 dB into the new bow's slow attack, Violas 69 -44 / -53 / -45 for 0.5 s, Violins II 44
# -42 / -52 / -42: fills over the hole (targets 6-9 dB dips). Basses 144 (pp stroke) peaks -44 over a -51 body: -5 dB
# over its attack. Basses 156 / 168 now dip 5.7 / 7.1 dB (c40 9.8 / 8.5), so no more is needed there
for _tr, _q, _sh in (("Violoncellos", 128.0, [(-0.12, 0.0), (-0.06, 5.0), (0.15, 5.0), (0.35, 0.0)]),
                     ("Violas", 248.5, [(-0.12, 0.0), (-0.06, 6.0), (0.20, 6.0), (0.40, 0.0)]),
                     ("Violas", 69.0, [(-0.10, 0.0), (-0.04, 4.0), (0.45, 4.0), (0.65, 0.0)]),
                     ("Violins II", 44.0, [(-0.10, 0.0), (-0.04, 3.0), (0.20, 3.0), (0.35, 0.0)]),
                     ("Double basses", 144.0, [(0.0, 0.0), (0.06, -5.0), (0.22, -5.0), (0.40, 0.0)])):
    LEVEL_SHAPES_S[_tr] = LEVEL_SHAPES_S.get(_tr, []) + [(_q, _sh)]
# delivery: after the stem fix the delivered p10-to-max span read 19.1 dB (limit 19): every track -0.4 dB over the climax
# bars 61-62 (slow ramps, so no tail is cut; the climax stays the loudest by more than 6 dB)
LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(203.5, 0.0), (204.25, -0.4), (211.75, -0.4), (212.25, 0.0)]]

# ---- c42 (coordinator: pp/p release caps 600 ms in build/mix.json; critics A/B/C on the c41 render) ----
# coordinator / A #2 / C #2b (Dan's S1): the longer pp/p caps refill soft repeat gaps, so "sus_fall" (now also on the
# stroke and portato-stroke paths, tools/score_to_parts.py) covers Violins II, violas and celli at p or softer; basses
# 10 -> 12 CC
STR_REP_NEW_BOW["sus_fall"] = {"Double basses": {"cc": 12, "s": 0.06, "max_cc": DYN["p"]},
                               "Violins II": {"cc": 8, "s": 0.06, "max_cc": DYN["p"]},
                               "Violas": {"cc": 8, "s": 0.06, "max_cc": DYN["p"]},
                               "Violoncellos": {"cc": 8, "s": 0.06, "max_cc": DYN["p"]}}
# A #3: violas 69 and 248.5 (soft re-bow pieces with no lead; the c41 post-hall fills started before the beat and lifted
# the old note's release) become fresh strokes; their c41 shapes go. Basses 144: the -5 dB shape over its attack took
# the separation with it; the sus_fall above (12 CC) separates it instead
DOWNBOW_STROKE_AT["Violas"] = DOWNBOW_STROKE_AT.get("Violas", []) + [69.0, 248.5]
LEVEL_SHAPES_S["Violas"] = [s_ for s_ in LEVEL_SHAPES_S["Violas"] if s_[0] not in (69.0, 248.5)]
LEVEL_SHAPES_S["Double basses"] = [s_ for s_ in LEVEL_SHAPES_S["Double basses"] if s_[0] != 144.0]
# B #1: bars 56-58: Horn 1's 182 head was as loud as its own f at 196 (c41's +5 stacked on 9.5-11.7 dB): +5 -> +2;
# then +3 from the 184 legato target to the 195.5 pickup onset (it sank 7-13 dB under the violins' theme)
_c41_hn = [(182.6, 0.0), (182.95, 5.0), (183.8, 5.0), (183.9, 0.0)]
assert _c41_hn in [list(map(tuple, s_)) for s_ in LEVEL_SHAPES["Horn 1"]]
LEVEL_SHAPES["Horn 1"] = [s_ for s_ in LEVEL_SHAPES["Horn 1"] if list(map(tuple, s_)) != _c41_hn] + [
    [(182.6, 0.0), (182.95, 2.0), (183.8, 2.0), (183.9, 0.0)],
    [(183.95, 0.0), (184.1, 3.0), (195.35, 3.0), (195.5, 0.0)]]
# C #5: bars 56-59: the lead violins were flat through the printed crescendo 188-196 and sagged after the f:
# +2 dB from 190 to 194, held to the bar 60 entry (slow ramps under sounding notes)
for _tr in ("Violins I", "Violins II"):
    LEVEL_SHAPES[_tr] = LEVEL_SHAPES.get(_tr, []) + [[(190.0, 0.0), (194.0, 2.0), (199.6, 2.0), (200.2, 0.0)]]
# C #5: bars 75-76: Violins II's F5 (Leg BC target at 251.775) sagged 5-7 dB inside the crescendo: +4 over the sag,
# back to 0 under the 254 attack (C's 253.45 end moved to the next note so no fall sits on the held note)
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(252.25, 0.0), (252.5, 4.0), (253.55, 4.0), (253.78, 0.0)]]
# C #3: the bar 47 fp: Oboe 1's 148 goal note swelled 3.5 dB in its first 0.6 qn under its printed decrescendo (the
# HP_SOFT_DEC gain ramps in over 148-148.59 on top of the role): +4.2 dB at the onset (the note before ends at 147.93),
# back to 0 where the ramp is complete, so the note starts at its full level and only falls
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES.get("Oboe 1", []) + [[(147.97, 0.0), (148.0, 4.2), (148.59, 0.0)]]
# ---- c42 after the render (level only, post-hall; applied by stem fix and --mix-only) ----
# re-bows refit on the c42 stems (600 ms pp/p caps: 18 attack peaks over 3.5 dB with the c41 fills -> 5), basses and
# Violoncellos div re-levelled (relevel41.py), Violins I 264.417 +2.5 from 0.6 s kept (c41 B #2), in build/rebow_fills.json.
# A #4 / C #4: the bar 91 morendo: the refit's holds lift Violas 4-6 dB and Violas div 3.5 dB over their bar 90 level
# exactly where the decrescendo starts (298); slow ramps (0.2-0.5 qn, about 0.3-0.6 s) under the held chord
LEVEL_SHAPES["Violas"] = LEVEL_SHAPES.get("Violas", []) + [
    [(297.75, 0.0), (298.0, -4.5), (298.6, -5.5), (298.8, -3.0), (299.6, -2.0), (300.1, 0.0)]]
LEVEL_SHAPES["Violas div"] = LEVEL_SHAPES.get("Violas div", []) + [
    [(297.6, 0.0), (297.8, -3.5), (298.6, -3.5), (298.9, -2.0), (299.8, -2.0), (300.3, 0.0)]]

# ---------- c43 (critics on the c42 render) ----------
# A #1 (with build/mix.json: basses pp/p cap 600 -> 400 ms; basses' re-bow fills back to c41's final rows, fitted on
# the 400 ms render): 286 (bar 87, A flat 1 -> F 1) followed an auto-re-bowed held note, so abut_cond skipped its
# 0.16 s lead and the old note ran to the beat; force it (the 283.605 piece's note-off moves, no re-bow point moves)
ABUT_LEAD["Double basses"]["force_at"] = [152.0, 204.0, 286.0]
# C #1 (S2): Clarinet 1 (pcX median +56 ms, all 20 joins late at the 0.03 s lead) and the bass clarinet (+72 ms at
# 0.05 s) cross late on every legato join; the leads rise by a little under the measured lag (kit LEARNINGS 5: the
# response to added lead is often more than 1:1). "Clarinet 1" must precede "Clarinet" (by_name takes the first match)
LEG_LEAD_S = {"Clarinet 1": 0.07, **LEG_LEAD_S}
LEG_LEAD_S["Bass clarinet"] = 0.09
# per-onset extras in build/leg_leads.json: Bass clarinet 30 0.15 -> 0.11 (total kept at 0.20 s), 32 +0.12, 108 +0.10,
# 26 +0.06; Clarinet 1 258 / 259 +0.10 (poco allargando, +190 / +171 ms)
# B #1: bar 62 beats 3-4: Horn 2 E4, Horn 3 B4 and the basses' E1 swell 5-6 dB in the samples (CC11 only 119 -> 122),
# reach Violins I's level and set the delivered maximum (limiter peak at qn 210.33): level shapes over 210-212 (post-hall,
# so a stem fix can apply them); the basses' shape ends before c41's +1.5 role at 211.75 and the 212 sf note
LEVEL_SHAPES["Horn 2"] = LEVEL_SHAPES.get("Horn 2", []) + [[(209.95, 0.0), (210.05, -4.0), (212.1, -4.0), (212.6, 0.0)]]
LEVEL_SHAPES["Horn 3"] = LEVEL_SHAPES.get("Horn 3", []) + [[(209.95, 0.0), (210.05, -3.0), (212.0, -3.0), (212.5, 0.0)]]
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [[(209.95, 0.0), (210.05, -4.0), (211.65, -4.0), (211.75, 0.0)]]
# B #5: Horn 1's 182 mp head spiked +3.5 dB over Violins I and its body collapsed 6-9 dB: c42's +2 shape (which rose
# across the head) becomes -1.5 on the head and +3.5 on the body; c42's +3 over 184.1-195.35 stays
_c42_hn = [(182.6, 0.0), (182.95, 2.0), (183.8, 2.0), (183.9, 0.0)]
assert _c42_hn in [list(map(tuple, s_)) for s_ in LEVEL_SHAPES["Horn 1"]]
LEVEL_SHAPES["Horn 1"] = [s_ for s_ in LEVEL_SHAPES["Horn 1"] if list(map(tuple, s_)) != _c42_hn] + [
    [(182.35, 0.0), (182.45, -1.5), (182.85, -1.5), (183.0, 3.5), (183.8, 3.5), (183.9, 0.0)]]
# C #2 (S2): Horn 1's f F sharp 4 after the bar 59 breath (196) swells in over 0.6 s (9 dB), 4-8 dB under Violins I in
# its first 0.4 s: a front-loaded lift that ends inside the note (simulated on the c42 stem: peak 0.5 dB over the body)
LEVEL_SHAPES_S["Horn 1"] = LEVEL_SHAPES_S.get("Horn 1", []) + [(196.0, [(-0.11, 0.0), (-0.08, 5.0), (0.25, 4.0), (0.7, 0.0)])]
# C #3 (S2): bar 71's first viola eighth (238, pp after the niente) swells 20 dB across its whole length (b-6 +0.18 s,
# celli +0.02): a front-loaded lift (simulated: no peak over c42's maximum)
LEVEL_SHAPES_S["Violas"] = LEVEL_SHAPES_S.get("Violas", []) + [(238.0, [(-0.21, 0.0), (-0.17, 8.0), (0.10, 6.0), (0.45, 0.0)])]
# A #4 (S2): the violas' portato E flat 4s at 164.5 / 166.5 (Detache) reach their attack at +0.19 s against +0.01..+0.09
# for their neighbours (a sample, not the lead: 165.5 / 167.5 on the same pitch are on time). They follow rests, so the
# lead is in build/entry_leads.json: 0.08 -> 0.18 s extra (total 0.20 -> 0.30 s, ENTRY_CAP_S)
# A #5 (S3): the timpani crescendo roll into the p stroke at 172 drops 18 dB for 0.05 qn in the post-hall envelope
# (171.95, the stroke's p level before the stroke shapes start), a 15 dB hole that also cuts the roll's hall; and 8.7 dB
# at 261.95 before the f roll at 262: fills over the notches hold the level into the stroke
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [
    [(171.94, 0.0), (171.95, 16.0), (171.96, 16.0), (171.982, 13.5), (171.99, 10.0), (172.0, 0.0)],
    [(261.875, 0.0), (261.95, 8.7), (261.98, 0.0)]]
# A #1 (b): the 286 lead ends the coda pedal (271-286) 0.097 qn earlier, which moved all five automatic re-bow points
# (273.229 -> 273.209 ... 283.605 -> 283.489) off the c41 fills and rebow_moves: the pedal keeps one automatic bow and
# its c41/c42 points are listed instead (the same split as before; only the last piece's note-off moves)
AUTO_REBOW_SKIP["Double basses"] = AUTO_REBOW_SKIP["Double basses"] + [271.0]
REBOW_AT["Double basses"] = sorted(REBOW_AT.get("Double basses", []) + [273.229, 276.05, 278.351, 282.203, 283.605])

# ---- c44 (2026-11-08): EW template mix cycle (loop/ONE_TIME.md); only these score-side items ----
# A #1 (Dan's S1; EW-TEMPLATE-PLAN section 8 repeat gaps 60-100 ms): the printed soft string repeats played as re-bow
# points kept REBOW_GAP_QN (0.03 qn, median 35 ms; own-band dips 0-2.9 dB at Vln II 289/120, Vln II div 114-119, Vla
# 271/81/87/198, Vla div 79): an 80 ms gap with a CC11 fall into it (the track's sus_fall, else 6 CC at mp or softer);
# loud strokes / sus_min_s repeats at CC 72 or louder (basses 265 f, 60 ms gap, -0.8 dB dip): 100 ms and a 6 CC fall
STR_REP_NEW_BOW["soft_gap_s"] = 0.08
STR_REP_NEW_BOW["soft_fall"] = {"cc": 6, "s": 0.06, "max_cc": DYN["mp"]}
STR_REP_NEW_BOW["loud_gap_s"] = 0.10
# the printed repeats listed as REBOW_AT points in c40 (A #3, sul tasto) and c41 (Violas div 79) get the same 80 ms
STR_REP_NEW_BOW["soft_gap_at"] = {"Violins II div": [114.0, 116.0, 119.0, 120.0], "Violins II": [112.0, 120.0],
                                  "Violas div": [79.0]}
# C #2: Horn 1's printed bar 8 swell (qn 20-21, p < >) measured -2.5 dB (reversed) under the series 1 c24 role
# [20.5, 23.5, -2.5] (removed from build/roles.json); a +3 dB soft-hairpin gain on it (the bar 12 crest stays 3 dB over)
HP_SOFT_GAIN_AT["Horn 1"] = {**HP_SOFT_GAIN_AT["Horn 1"], 20.0: 3.0}

# ---- c45 (2026-11-08): performance data (loop/ONE_TIME.md c45; EW-TEMPLATE-PLAN sections 5-10; critics A/B/C on c44) ----
# Phrase shapes (tools/score_to_parts.py apply_phrase_shape). Values: critic A #1's lyrical shape (+1.5 dB at +0.4 s,
# +2 at +0.8 s, the peak at 0.44 of the phrase, the last second tapering), set around zero to critic B's measured depth
# (about 3-4 dB of swing, the phrase mean on the printed dynamic, so solo margins hold); strings take only the taper
# (their sample bloom already swells +7 dB by 0.4 s) and only without a printed decrescendo at the end. The CC1 arch on the
# vibrato patches: woodwinds the plan's 33 / 32 units but never under CC1 77 (LEARNINGS section 3: CC1 55-76 sounds both
# layers and beats; 77-127 is Vib alone); strings 8 / 12 units with floor 55 (on the Hollywood Strings KS Masters CC1
# also selects the louder Molto Vib set from 70, Movement I c32-c33, so the full depth would move the level by several dB).
# Classes: hairpins over half the phrase = a printed swell (skipped, the hairpin is the shape); phrases touching critic A's
# builds (bars 53-60, 75-78) or bars 61-64 (Largamente, tremolos, the accented trombone quotation) skipped; the morendo
# from qn 297 skipped; the rest lyrical.
PHRASE_SHAPE = {
    "gap_s": 0.15, "min_s": 2.5, "max_s": 16.0, "min_onsets": 3, "hairpin_cover": 0.5, "skip_after_qn": 297.0,
    "skip_families": ("harp", "harm", "timp", "perc"),
    "skip_arts": ("Trem", "izz", "Stac", "Spic", "Marc", "Detache", "Rep"),
    # critic A's "build" class: bars 53-60 and 75-78 rise under printed crescendos to f / ff (plus the bars 61-64 climax)
    "skip_spans": {"*": [(172.0, 220.0), (250.0, 262.0)]},
    "ramp_in_s": 0.5, "ramp_out_s": 1.0, "vol_grid_qn": 0.125,
    "level": {"default": [("on", 0.0, -2.0), ("on", 0.4, -0.5), ("on", 0.8, 0.0), ("frac", 0.44, 1.5),
                          ("end", 1.0, 0.0), ("end", 0.0, -2.5)],
              "string": [("on", 0.0, 0.0), ("end", 1.0, 0.5), ("end", 0.0, -1.5)]},
    "scale_by_cc": [(34, 0.6), (46, 0.8), (58, 1.0)],
    "cc1": {k_: {"depth_start": 33, "depth_end": 32, "floor": 77, "peak": 0.44} for k_ in ("Flute", "Oboe", "Cor anglais", "Bassoon")}
           | {k_: {"depth_start": 8, "depth_end": 12, "floor": 55, "peak": 0.44} for k_ in ("Violins", "Violas", "Violoncellos", "Double basses")},
    # critic A #1: doubled lines share one curve, from the top voice's phrases (later entries win where windows overlap)
    "groups": [{"tracks": ["Violins I", "Violins II"], "from": 65.0, "to": 90.0, "leader": "Violins I"},
               {"tracks": ["Violins I", "Violins II"], "from": 171.0, "to": 204.0, "leader": "Violins I"},
               {"tracks": ["Violins I", "Violins II"], "from": 237.0, "to": 262.0, "leader": "Violins I"},
               {"tracks": ["Oboe 1", "Bassoon 1", "Violoncellos"], "from": 139.0, "to": 151.0, "leader": "Oboe 1"},
               {"tracks": ["Bass clarinet", "Bassoon 2", "Double basses"], "from": 188.0, "to": 204.0, "leader": "Bass clarinet"},
               {"tracks": ["Bassoon 1", "Violoncellos"], "from": 250.0, "to": 274.0, "leader": "Bassoon 1"},
               {"tracks": ["Flute 1", "Oboe 1", "Violins I", "Violins II"], "from": 188.0, "to": 204.0, "leader": "Flute 1"},
               {"tracks": ["Flute 1", "Oboe 1", "Clarinet 1", "Violins I", "Violins II"], "from": 256.0, "to": 274.0, "leader": "Flute 1"}],
}
# A #2: wind legato targets by printed dynamic (EW's template plays its KS Master legato rows at v90-95), horns the same
# minus 6 (v80-98; 1FH v80 in the template); strings keep v124 (v108 against v124 gave identical crossovers, c11)
LEG_VEL_BY_CC = {"wind": ([(22, 86), (46, 90), (72, 96), (114, 104)], 0),
                 "Horn": ([(22, 86), (46, 90), (72, 96), (114, 104)], -6)}
# A #3: the violas' sotto voce portato eighths (bars 48-51, Detache, all v37) played two identical takes alternating;
# a seeded pattern within 37 +-5 (Detache crossfades its layers by velocity); leads in build/entry_leads.json
VEL_SET["Violas"].update(dict(zip([152.5, 153.5, 154.5, 156.5, 157.5, 158.5, 159.5, 160.5, 161.5, 162.5, 163.5, 164.5,
                                   165.5, 166.5, 167.5],
                                  [37, 32, 40, 34, 39, 31, 36, 41, 33, 38, 35, 42, 34, 39, 36])))
# A #4 (S1): Violas 87 ran together (gap 80 ms, master dip 2.2 dB): the DOWNBOW_STROKE_AT path (as 69 / 248.5);
# Horn 3 289's re-tongue dipped 10.8 dB in its stem under a tutti re-attack (master 7.6 dB): gap 0.12 -> 0.06 s, fall 10 -> 5
DOWNBOW_STROKE_AT["Violas"] = DOWNBOW_STROKE_AT["Violas"] + [87.0]
WIND_REP_RETONGUE_AT = {"Horn 3": {289.0: {"gap_s": 0.06, "fall_cc": 5}}}
# A #5: timpani strokes sounded 58-60 ms after the beat (Movement I c03's delay for an Allegro); every other attack is
# now led onto the beat (pcX +1..+22 ms), and the plan puts percussion on the grid
TIMP_DELAY_S = 0.0

# ---- c46 (2026-11-08): rubato (loop/ONE_TIME.md c46; EW-TEMPLATE-PLAN sections 8-9; critics A/B/C on the c45 render) ----
# Tempo map: critic C #1's final values (the c44 plan re-measured against Duc's Adagietto, Mulan and Howl's: median beat
# deviation 1.5 -> 3.0 %, breaths -15 -> -25 % median, the slow beats before the pickups, not on them; the depths now
# read here because tools/score_to_parts.py takes them through globals().get), with critic A #2: the breath before the
# violins' theme entry sits at 65 (before their slurred E flat-F pickup), not at 66 inside it
PHRASE_PUSH = 1.03
PHRASE_SLOW = (0.93, 0.84)
PHRASE_SLOW_SUB = (0.97, 0.90)
PHRASE_SLOW_MAIN = (0.88, 0.80)   # C #1: Duc's two-beat section-end broadening
PHRASE_RETURN = 0.98
APEX_AGOGIC = 0.93
PHRASE_ARCS = [(18, 29), (29, 42, "main"), (48, 54, "sub"), (60, 65, "main"), (65, 77), (77, 90, "main"),
               (108, 116, "sub"), (116, 124), (124, 139), (139, 148, "sub"), (152, 160, "sub"), (160, 168),
               (220, 226, "sub"), (226, 237, "main"), (237, 249), (274, 286)]
APEX_LEAD[116] = "Flute 1"
CAESURA = {29.0: 0.22, 42.0: 0.18, 48.0: 0.15, 54.0: 0.10, 60.0: 0.10, 65.0: 0.20, 77.0: 0.15, 90.0: 0.15,
           96.0: 0.15, 102.0: 0.15, 116.0: 0.10, 124.0: 0.22, 139.0: 0.15, 148.0: 0.10, 164.0: 0.20, 171.0: 0.10,
           188.0: 0.12, 196.0: 0.08, 204.0: 0.10, 237.0: 0.18, 249.0: 0.15, 259.0: 0.10, 268.0: 0.15, 286.0: 0.20}
BEAT_STRETCH = {17: 1.04, 18: 0.97, 24: 0.96, 29: 1.04, 30: 0.97, 37: 1.04, 38: 1.04, 39: 0.96, 42: 0.96, 45: 0.96,
                48: 1.04, 51: 0.96, 55: 1.04, 57: 0.96, 60: 1.04, 63: 0.96, 72: 0.96, 77: 1.04, 78: 0.97, 85: 1.04,
                86: 1.04, 87: 0.96, 91: 1.04, 92: 1.04, 93: 0.96, 97: 0.96, 99: 0.96, 108: 0.96, 113: 1.04, 121: 1.04,
                126: 0.96, 131: 1.04, 132: 0.96, 136: 0.96, 140: 0.97, 145: 1.04, 147: 0.97, 148: 0.96, 152: 0.96,
                155: 1.04, 160: 0.96, 164: 0.96, 168: 0.96, 204: 0.94, 208: 0.94, 226: 0.96, 232: 0.96, 237: 1.04,
                238: 0.97, 244: 0.96, 249: 1.04, 250: 0.97, 257: 1.04, 280: 0.96, 283: 0.96, 286: 0.96, 289: 0.96}
BEAT_STRETCH = {float(k_): v_ for k_, v_ in BEAT_STRETCH.items()}
# A #1: at a caesura breath a loud wind/brass note ends at least CAESURA_BREATH_S before it (the short caesuras at 196 and
# 259 would otherwise switch the gap from 0.3 to 0.12 qn); c19's tuned climax breaths keep 0.12 qn. A's 0.24 s left the
# bass clarinet at 196 (240 ms) and Bassoon 1 at 259 (240 ms) under their c45 breaths (284 / 338 ms): 0.34 s keeps every
# listed breath at least as long as in c45 (Horn 1 196 240 ms, bass clarinet 196 340, Bassoon 1 259 340)
CAESURA_BREATH_S = 0.34
CAESURA_BREATH_SKIP = {204.0, 268.0}
# A #3: the strings played legato straight through the new breaths before the theme pickups: a CC11 lift in the last
# 0.25 s (the overlap and the bow-change join are kept; pre-hall, so the room rings on)
CAESURA_LIFT = {"Violins I": {77.0: 9, 249.0: 9}, "Violins II": {65.0: 8, 77.0: 9, 249.0: 9}}
# C #3: the automatic re-bow points are placed in seconds and move with the map; pin c45's points so the fitted fills
# stay on them (the basses' 164 note grows to 4.63 s: keep it one bow)
for _t, _p in {"Violins I": [205.949, 264.417], "Violins II": [165.86, 263.921], "Violas": [169.5, 263.414],
               "Violoncellos": [153.366, 165.293],
               "Double basses": [170.003, 221.8, 225.215, 227.775, 230.393, 233.038, 235.659],
               "Violoncellos div": [275.527, 277.599, 279.67, 281.716, 284.141], "Violas div": [280.439]}.items():
    REBOW_AT[_t] = sorted(set(REBOW_AT.get(_t, []) + _p))
AUTO_REBOW_SKIP["Double basses"] = AUTO_REBOW_SKIP["Double basses"] + [164.0]
# Hairpin shapes (plan section 9; C #4 values): crescendos rise early (Mulan: control point at 34 % of the time, 88 % of
# the rise), diminuendos hold then fall late (Howl's: 68 %, 27 %). CC11 lane only, hairpins of 6 s or less; linear: the
# timpani (Movement I: a curve lifted a fff-pp roll 8 dB over a horn solo), the animando and allargando builds (172-220,
# 250-259), and B #3's accompaniment hairpins under Trombone 1's quotation (212-216) and the bar 47-48 handover (146-152.5)
_lin212 = ["Violins I", "Violins II", "Violas", "Violoncellos", "Double basses", "Violin I solo", "Violoncellos div",
           "Violins II div", "Violas div", "Bass trombone"]
_lin146 = ["Violins II", "Violins II div", "Violas", "Violas div", "Violoncellos", "Violoncellos div", "Double basses"]
HP_CURVE = {"cresc": (0.34, 0.88), "decresc": (0.68, 0.27), "max_s": 6.0, "skip_families": ("timp", "perc"),
            "skip_spans": [(172.0, 220.0), (250.0, 259.0)],
            "linear": {t_: [(212.0, 216.0)] * (t_ in _lin212) + [(146.0, 152.5)] * (t_ in _lin146)
                       for t_ in set(_lin212) | set(_lin146)}}
# C #6 (S3): no post-hall fall in the first 0.5 s after a note-off before a rest (Bassoon 1 at 29: +3 -> -3 dB in 0.12 s)
VOL_TAIL_HOLD = {"s": 0.5, "min_gap_qn": 0.25, "min_fall_db": 1.0}
# B #4: Trombone 1's qn 213 accent: the CC7 dip to 110 sat exactly on the accent (a c33 leftover against brightness, now
# done by the brass 3.2 kHz bell); 215 keeps 120. The role rows are in build/roles.json
CC7_POINTS["Trombone 1"] = [(q_, 127 if q_ in (212.9, 213.35) else v_) for q_, v_ in CC7_POINTS["Trombone 1"]]
# A #4: four JOIN_NOTCH windows written in qn at measured transition peaks moved off them on the new map; each keeps its
# offset in seconds from its target's moved onset (recomputed on the c46 map; equal to A's plan-A windows)
for _t, _o, _n in [("Violins I", (258.85, 258.93, -5.5), (258.889, 258.948, -5.5)),
                   ("Violins II", (258.81, 258.98, -4.0), (258.860, 258.985, -4.0)),
                   ("Flute 1", (258.86, 258.93, -2.0), (258.897, 258.948, -2.0)),
                   ("Violoncellos", (76.82, 76.98, -4.0), (76.890, 76.988, -4.0))]:
    assert _o in JOIN_NOTCH[_t], (_t, _o)
    JOIN_NOTCH[_t] = [_n if j_ == _o else j_ for j_ in JOIN_NOTCH[_t]]

# ---- c47 (2026-11-09): the last cycle before Dan listens; level and timing data only, no Opus state change ----
# Join fills (critic A #1; build/early_fills.json, hand entries): Oboe 1 47/142/142.5/143/146, celli 140/240/248.5,
# Flute 1 113.5 and bass clarinet 92 are full just after their moved onsets (pre_s = lead - 0.04 s), held to the measured
# end of each hole. A #2: Oboe 1's dolce espr. pickup 139 and the eighth 145 sat 6-8 dB under their neighbours (trims
# 6 / 5, as steps: the default 0.6 s ramp never reaches full level on the 0.55 s eighth); B #1: Oboe 1's bar 80 A flat 5
# (266) was the loudest stem in the ff cadence (+9.8 dB over its neighbours): -8 dB as a step
NOTE_TRIM_RAMP_S["Oboe 1"].update({139.0: 0.1, 145.0: 0.1, 266.0: 0.1})
# B #2: the bass clarinet's held A flat 2 (271, p > pp) swelled 6 dB into the coda (layer edge at CC11 34-36 plus the
# decrescendo's dB ramp releasing inside the note): pre-hall CC7 fall, -2 / -3.8 / -7 / -10 dB (no bass clarinet note
# follows, so the return to 127 is silent). Its pp A flat 2s at 18 / 24 / 39 (note_trims.json -4) sat 3-10 dB over its
# other pp notes in the chorale under Horn 1
CC7_POINTS["Bass clarinet"] = CC7_POINTS.get("Bass clarinet", []) + [
    (272.75, 127), (273.0, 101), (273.25, 82), (273.5, 57), (273.75, 40), (275.5, 40), (276.0, 127)]
# B #3: the c46 hairpin curves add the most dB low on the CC11 lane, so a soft accompaniment sharing a hairpin with a lead
# rose faster than the lead: linear under Oboe 1 (bars 15-16), the cor anglais solo (bars 41-44) and Clarinet 1's coda
# solo (bar 85) (c45 measured these places linear: Oboe 1 over Violins II at 46 +6.1, cor anglais over Flute 1 at 133/134
# +3.4, against +3.7 / +2.4 / +1.7 with the curves)
for _t, _w in {"Violins II": (42.0, 47.0), "Violins II div": (42.0, 47.0), "Flute 1": (131.0, 136.0),
               "Violoncellos": (124.0, 132.0), "Violoncellos div": (283.0, 286.0), "Double basses": (283.0, 286.0),
               "Violas div": (283.0, 286.0)}.items():
    HP_CURVE["linear"][_t] = HP_CURVE["linear"].get(_t, []) + [_w]
# B #5: the coda timpani answer (pp E flat-C-A flat): the first stroke (277) peaked 3.2 dB under the second: a +2.5 dB
# step on the stroke, back before the 278.5 stroke (kit section 13 rule for struck notes)
LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(276.96, 0.0), (276.99, 2.5), (278.3, 2.5), (278.45, 0.0)]]
# C #2: woodwind entries have spoken 38 ms (median) before the beat since the c44 Close-led mics (c41 -24 ms; brass and
# strings did not move; leads respond about 1:1, c43): every wind lead -0.03 s (bassoons 0.06 -> 0.03, contrabassoon
# 0.06 -> 0.02); Flute 1, already at -7 ms, keeps its values. The per-onset extras at Clarinet 1 280, Flute 2 262 and
# Bassoon 1 196 / 229 are deleted (build/entry_leads.json)
ENTRY_LEAD_S["Bassoon"] = (0.03, 0.03)
ENTRY_LEAD_S["Contrabassoon"] = (0.02, 0.02)
ENTRY_LEAD_ART_S = {"wind": {"Leg Slur MAX": 0.03, "Leg Slur": 0.04, "Sus Non Vib": 0.04, "Sus MAX": 0.02},
                    "Flute 1": {"Leg Slur MAX": 0.06, "Leg Slur": 0.11, "Sus Non Vib": 0.07, "Sus MAX": 0.05},
                    "brass": {}, "Bassoon": {}, "Contrabassoon": {}}
# C #5: Horn 4's held pp E flat 3 (84-90, 7.6 s): the role step [86, 90, -5.5] (-5.2 dB in 0.5 qn, on top of a loop dip)
# made the note dip 10 dB and swell back within 1 s: the same level reached by a 2 qn fall
LEVEL_SHAPES["Horn 4"] = LEVEL_SHAPES.get("Horn 4", []) + [[(84.5, 0.0), (86.5, -5.5), (90.0, -5.5), (90.5, 0.0)]]
# Final chord (C #4; coordinator: meet the 0.45 s guard): -4 dB over 0.1 qn (0.30 s at the final 20 bpm) after the last
# release on the six string tracks, held to the end; applied after END by the c47 post-END rule in
# tools/score_to_parts.py
for _t in ("Violins I", "Violins II", "Violas", "Violas div", "Violoncellos", "Double basses"):
    LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(304.0, 0.0), (304.1, -4.0)]]
# C #1 (holes in the slurred solo lines; joins C lists beyond A's fills, each simulated on the c46 stems and kept only
# where better): Horn 1's printed decrescendo 229 mp -> 235 pp dropped 6.8 dB at the 230 join and then stayed flat (A-
# weighted per beat 229 -39.4, 230 -46.2, 231 -46.2): +3 dB on the 230 beat gives -39.3 / -43.6 / -46.2 / -47.3.
# The bass clarinet's 92.5 join: early_fills.json (auto_fills). auto_fills proposed nothing at the horn theme's 23 / 35 /
# 37.5 (23 and 35 are level steps into the printed decrescendos, not holes: 0.5 / 1.1 dB below the lower body)
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(229.95, 0.0), (230.1, 3.0), (230.85, 3.0), (231.0, 0.0)]]
# Clarinet 1 283: the c38 CC7 dip (85 over 282.75-283.3) sat on the legato transition, which since c45's v88 is a hole
# (stem 10 dB under at +0.04..+0.4 s), but before the join it still cuts the 280 note's end swell (deleting it lifted
# 282.75-283 by 3.5 dB over the line): the dip now ends at the score onset 283.0 (stem quarter-beat profile 282.5-283.75
# -48.3 / -48.5 / -54.7 / -52.2 -> -48.3 / -48.5 / -51.2 / -51.5)
CC7_POINTS["Clarinet 1"] = [p_ for p_ in CC7_POINTS["Clarinet 1"] if p_ not in ((283.1, 85), (283.3, 127))] + [(283.0, 127)]

# ---- c48 (2026-11-09): the finale's shared techniques (loop/ONE_TIME.md c48) and critics A/B/C on the c47 render ----
# A #1 / B #1 (finale item 2): the bar 47 fp (qn 148; Violins II, Violas, basses) peaked 200-350 ms after the beat: the
# led notes took the p level at their moved note-on (the spike started 0.02 qn after the mark) and Violins II / Violas
# reached 148 as v124 slur transitions from 146, though no slur is printed into 148. FP_SPIKE_AT_MARK (ported from
# mvt3 c09 with its hairpin shift, tools/score_to_parts.py) makes the f a step at the mark, so each led note's pull
# carries it from the note-on; the fp notes on Violins II / Violas become fresh Sus MAX strokes (rows already loaded);
# the spike is shortened to 0.12 / 0.30 qn (125 / 312 ms at bar 47's tempo; the finale's FP_SPIKE_S is 0.10 / 0.30 s).
# FP_VEL stays off: the fp notes play the Sus MAX row, whose velocity is ignored (DIGEST §2, M1 c06; critic B)
FP_SPIKE_AT_MARK = True
FP_SPIKE = ("f", 0.12, 0.30)
DOWNBOW_STROKE_AT["Violins II"] = DOWNBOW_STROKE_AT.get("Violins II", []) + [148.0]
DOWNBOW_STROKE_AT["Violas"] = DOWNBOW_STROKE_AT["Violas"] + [148.0]
# A #2 (finale item 7 not adopted): the post-END fade -4 -> -1 dB (simulated t20 0.40 -> 0.44 s; the chord without a fade
# already takes 0.465 s, so FINAL_RING, which holds the notes longer, would move it the wrong way)
for _t in ("Violins I", "Violins II", "Violas", "Violas div", "Violoncellos", "Double basses"):
    assert [(304.0, 0.0), (304.1, -4.0)] in LEVEL_SHAPES[_t], _t
    LEVEL_SHAPES[_t] = [s_ if s_ != [(304.0, 0.0), (304.1, -4.0)] else [(304.0, 0.0), (304.1, -1.0)]
                        for s_ in LEVEL_SHAPES[_t]]
# B #2: Oboe 1's eighths at 142 / 142.5 sat 4.8-5.8 dB under their neighbours under c47's shorter fill holds: +3 dB over
# 142.10-142.70 (after 142's fill hold, before 143's fill front), not A's note trims (one of the two)
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(142.02, 0.0), (142.10, 3.0), (142.70, 3.0), (142.72, 0.0)]]
# B #3: bar 81: c46's curved decrescendo held the celli's CC11 11 CC over c45 at 269, so their held D flat 4 rose 3.1 dB
# over the tune's descent (transition peak 5.4 dB over Violins I): linear 268-271 on celli and violas, -2 dB on the
# celli's transition peak
for _t in ("Violoncellos", "Violas"):
    HP_CURVE["linear"][_t] = HP_CURVE["linear"].get(_t, []) + [(268.0, 271.0)]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(268.95, 0.0), (269.0, -2.0), (269.4, -2.0), (269.7, 0.0)]]
# A #1 step 4: the basses' fp note (C sharp 2, moved onset 147.8965) carries pitch_trims.json's -2 dB C sharp 2 trim,
# which ramps in over the attack (vol_db -0.63 / -1.33 / -2.62 at 147.897 / 148.0 / 148.147 against the line before
# it): hold it off through the attack (to the end of the f hold, 148.12) and let it back in with the attack's fall to p
# (148.3), so the p after the fp keeps its c47 level (A's release across the whole decrescendo lifted the p body at
# 148.6-149.2 by 1.5-2 dB, which shrinks the fp's drop)
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES["Double basses"] + [
    [(147.8965, 0.0), (148.0, 0.83), (148.12, 2.0), (148.3, 0.0)]]
# Coordinator (finale SHARED-TECHNIQUES item 13), after a range render of qn 143-153 with the changes above: each part's
# own drop met 10 dB (Violins II 11.2, Violas 14.3, basses 13.2) and the master gained an accent from the beat (-39.9 ->
# -34.5 dB on the beat), but every part still peaked 200-235 ms after the beat (CC11's f hold ends at +125 ms; the
# sample's rise and Opus's CC11 response put the level's peak about 100 ms later). A short post-fader bump on the
# attack (seconds re the beat: from the strokes' note-on at -60 ms, full at -40 ms, held to +60 ms, gone at +160 ms;
# +3 dB on Violins II / Violas, +5 dB on the basses, the finale's values), simulated on the range stems: peaks at +100 /
# 0 / +110 ms (basses flat within 0.9 dB over 0-200 ms), drops 11.4 / 14.4 / 13.9 dB, master -35.9 / -31.1 / -31.2 /
# -30.6 dB at -100 / 0 / +100 / +200 ms (peak level unchanged, the accent now starts on the beat). Post-fader sends:
# the returns take it too, and the hall's ring is not cut (S3)
for _t, _d in (("Violins II", 3.0), ("Violas", 3.0), ("Double basses", 5.0)):
    LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [(148.0, [(-0.06, 0.0), (-0.04, _d), (0.06, _d), (0.16, 0.0)])]

# ---- c49 (2026-11-09): critics A/B/C on the c48 render and the finale's techniques 18-23 (loop/ONE_TIME.md c49) ----
# A #1: the Violas' two Detache takes changed places between c47 and c48 on unchanged data (round-robin position at
# 152.5 depends on what the plugin played before the render). RR_RESET_AT (tools/score_to_parts.py) puts a round-robin
# reset (CC16 127, build_reaper.py RR_RESET_CC) just after the Detache keyswitch region starts, before the first eighth
RR_RESET_AT = {"Violas": [152.06]}
# A #3: the sul tasto pad's changes of harmony (Violins II / Violins II div, qn 112-122) were heard 0.4-1.0 s late: the
# new pitch 0.75 s early (still capped at 0.45 of the previous note) and the old pitch held 0.15 qn, not 0.7 qn, past
# the printed onset; the fills that keep the level through the shorter overlap are fitted on a range render
# (build/level_fits.json, written by cycles/c49/actor_scripts/meas49.py flaut --fit; each fill tapers to 0 at 1.2 s
# after the new note-on or at the note's end, so that no fill ends in a step). Result: the new pitch passes the old one
# at +0.15..+0.50 s (c48 +0.38..+1.00 s); a track-level fill raises both pitches alike and does not move that time
FLAUT_LEAD_S, FLAUT_OVERLAP_QN = 0.75, 0.15
# Finale technique 18 (measured at 30-120 Hz on c48: basses 144 / 156 / 168 / 265 dip 8.0-11.5 dB, 253 only 2.7 dB):
# -9 dB in the played gap before the basses' repeat at 253 (note-off -160 ms + 6 ms to the note-on -100 ms - 3 ms)
LEVEL_SHAPES_S["Double basses"] = LEVEL_SHAPES_S.get("Double basses", []) + [
    (253.0, [(-0.160, 0.0), (-0.154, -9.0), (-0.103, -9.0), (-0.097, 0.0)])]
# Finale technique 19: the Bass trombone's sf at 212 started 2.3 dB under the f before it (first 0.1 s; its peak at
# +0.15-0.25 s): +3 dB from the note-on to +0.08 s, gone at +0.15 s (Flute 1's sf starts 2.5 dB over: no bump)
LEVEL_SHAPES_S["Bass trombone"] = LEVEL_SHAPES_S.get("Bass trombone", []) + [
    (212.0, [(-0.02, 0.0), (0.0, 3.0), (0.08, 3.0), (0.15, 0.0)])]
# Finale technique 21 (a repeat on a new bow needs a longer gap than a repeat inside a bow; none of our weak points is
# inside a slur): 0.12 s at the S1 points that dipped under 3.3 dB in their own band in c48 (Violins II 289 kept the
# loop re-bow gap of 35 ms: it is a listed REBOW_AT point that was missing from soft_gap_at)
STR_REP_NEW_BOW["soft_gap_s_at"] = {"Violas": {271.0: 0.12}, "Violins II": {289.0: 0.12, 120.0: 0.12},
                                    "Violas div": {79.0: 0.12}, "Violins II div": {114.0: 0.12, 119.0: 0.12}}
# Finale technique 22 (c48's open item): Oboe 1's +3 dB shape over 142 / 142.5 ended at 142.70, 0.19 qn before the
# 142.5 note does (it gained 1.2 dB, not 2.7); it now runs into the fill front of the 143 note (142.858-142.879)
assert [(142.02, 0.0), (142.10, 3.0), (142.70, 3.0), (142.72, 0.0)] in LEVEL_SHAPES["Oboe 1"]
LEVEL_SHAPES["Oboe 1"] = [s_ if s_ != [(142.02, 0.0), (142.10, 3.0), (142.70, 3.0), (142.72, 0.0)]
                          else [(142.02, 0.0), (142.10, 3.0), (142.858, 3.0), (142.879, 0.0)] for s_ in LEVEL_SHAPES["Oboe 1"]]
# The bar 47 fp (c48 open item): Violins II's stroke at 148 peaked +115 ms after the beat (175 ms after its note-on; the
# Violas' peak 65 ms after theirs) and no bump shape moves that peak (simulated on the c48 stems, actor_scripts/fp49.py).
# The note-on goes 60 ms earlier (build/entry_leads.json "148": 0.06) and the bump moves with it. FP148_V2_EARLY False
# restores c48 (with the entry_leads.json row removed).
# Range render (cycles/c49/rangetest/v1, same take as c48): with the bump (-0.12, 0) (-0.10, 3) (0.0, 3) (0.10, 0) the
# level at the beat rose 5.9 dB, but the stroke's second swell (160-270 ms after the beat) then passed under the CC
# spike's later part and became the peak (-38.6 dB at +195 ms). The shape below holds the +3 dB to +0.06 s and takes
# 2 dB off the second swell: simulated on those stems, peak -39.9 dB at +40 ms, drop to the p body 12.4 dB; range
# render v3: peak -39.6 dB at +60 ms (c48 +115 ms), drops 12.7 / 13.1 dB, master 100 ms before the beat -36.6 (c48 -36.1)
FP148_V2_EARLY = True
if FP148_V2_EARLY:
    assert (148.0, [(-0.06, 0.0), (-0.04, 3.0), (0.06, 3.0), (0.16, 0.0)]) in LEVEL_SHAPES_S["Violins II"]
    LEVEL_SHAPES_S["Violins II"] = [s_ if s_ != (148.0, [(-0.06, 0.0), (-0.04, 3.0), (0.06, 3.0), (0.16, 0.0)])
                                    else (148.0, [(-0.12, 0.0), (-0.10, 3.0), (0.06, 3.0), (0.14, -2.0), (0.27, -2.0), (0.36, 0.0)])
                                    for s_ in LEVEL_SHAPES_S["Violins II"]]

# ---- c50 (2026-11-09): critic A findings 3 and 5 (legato leads). Per-onset leads are in build/leg_leads.json; see
# cycles/c50/CHANGES.md. A "listed" LEG_CAP_FRAC entry raises the share of the previous note that a lead may take only
# for onsets with a per-onset row (the 0.45 default cut these leads short: they read +60 to +300 ms late in c47-c49)
LEG_CAP_FRAC["Violins II"] = LEG_CAP_FRAC.get("Violins II", []) + [(177.0, 187.0, 0.75, "listed")]
LEG_CAP_FRAC["Violins I"] = LEG_CAP_FRAC.get("Violins I", []) + [(181.0, 193.0, 0.65, "listed"), (258.0, 259.0, 0.65, "listed")]
LEG_CAP_FRAC["Violas"] = LEG_CAP_FRAC["Violas"] + [(192.0, 196.0, 0.75, "listed"), (249.5, 257.5, 0.6, "listed")]
LEG_CAP_FRAC["Violoncellos"] = LEG_CAP_FRAC.get("Violoncellos", []) + [(145.0, 146.0, 0.7, "listed"), (68.0, 69.0, 0.5, "listed")]
# A #5: Clarinet 2's row lead 0.03 -> 0.07 s (its joins read 40-70 ms late); the row "244" in leg_leads.json 0.12 -> 0.08
LEG_LEAD_S = {"Clarinet 2": 0.07, **LEG_LEAD_S}
# A #5: Horn 4's note at 268 follows a slur that starts on a tied note (265) and had no lead: +110 ms (pcX) / +170 ms
# (crossover) in c47-c49. SLUR_JOIN_LEAD_AT is the per-onset table added to tools/score_to_parts.py this cycle
SLUR_JOIN_LEAD_AT["Horn 4"] = {268.0: 0.10}
# c50 critic C #1 (bars 58-60): the violins' crescendo to bar 59 was flat (Violins I 197-199 was 1.1 dB under 193-195 in
# c49, Violins II 2.5 dB under). +3 dB from 196.5 to 201, back to 0 at 204 (the level at 204 and bar 61 stay)
for _tr in ("Violins I", "Violins II"):
    LEVEL_SHAPES[_tr] = LEVEL_SHAPES.get(_tr, []) + [[(195.5, 0.0), (196.5, 3.0), (201.0, 3.0), (204.0, 0.0)]]
# c50 critic C #3 (bar 47): Oboe 1's fp note at 148 spoke late (0.15 s after the beat it was 8.2 dB under its maximum in
# c49). The note-on goes 0.15 s earlier (re-attack lead; clamped to 0.45 of the previous note's slot), the 4.2 dB step
# moves with the onset and a 2 dB dip after 148.3 keeps the later swell under the start
REATTACK_LEAD_AT["Oboe 1"][148.0] = 0.15
assert [(147.97, 0.0), (148.0, 4.2), (148.59, 0.0)] in LEVEL_SHAPES["Oboe 1"]
LEVEL_SHAPES["Oboe 1"] = [s_ if s_ != [(147.97, 0.0), (148.0, 4.2), (148.59, 0.0)]
                          else [(147.873, 0.0), (147.903, 4.2), (148.59, 0.0)] for s_ in LEVEL_SHAPES["Oboe 1"]]
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(148.3, 0.0), (148.7, -2.0), (149.3, -2.0), (149.9, 0.0)]]
# c50 critic C #2 (conditional; both thresholds still failed on the range renders after the rebuild: Horn 1 32.4-32.8 was
# 5.4 dB over 33.0-33.8; Cor anglais 127.75-128.75 was 0.7-1.2 dB over 124.25-125.25, need 3). Horn 1 bar 11: the crescendo
# note peaked 0.5 qn after its start and fell back; Cor anglais bars 41-42: the solo's first crescendo was flat
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(32.1, 0.0), (32.3, -2.5), (32.5, -4.5), (32.75, -3.5), (32.95, 0.0), (33.25, 3.0), (34.1, 3.0), (34.4, 0.0)]]
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [[(124.9, 0.0), (127.9, 3.0), (130.9, 3.0), (131.9, 0.0)]]
# c50 critic C #4 (conditional; both thresholds still failed on the range renders after the rebuild). Violins II bars 74-75:
# the c42 shape ended at the top note's onset (254), so the top of the unison crescendo was level with the note before it
# and 6.6 dB under Violins I: the shape now holds through the top note. Violoncellos bars 72-73: the line peaked at
# 245.0-245.5, one beat before the printed peak at 246
assert [(252.25, 0.0), (252.5, 4.0), (253.55, 4.0), (253.78, 0.0)] in LEVEL_SHAPES["Violins II"]
LEVEL_SHAPES["Violins II"] = [s_ if s_ != [(252.25, 0.0), (252.5, 4.0), (253.55, 4.0), (253.78, 0.0)]
                              else [(252.25, 0.0), (252.5, 4.0), (254.5, 4.0), (254.79, 0.0)] for s_ in LEVEL_SHAPES["Violins II"]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(244.6, 0.0), (245.0, -1.5), (245.55, -1.5), (245.75, 4.0), (246.6, 4.0), (247.8, 0.0)]]

# ---- c51 (2026-11-10): printed tempo only (loop lead decision 1; critic A #1, critic C #1-#2) ----
# Dan heard Movement I's theme as out of time; critics A and C measured the same causes here: 103 of 233 a-tempo beats
# 3 % or more off the printed tempo, 13 phrase-end beats 20-42 % long. This is a change of musical character: no rubato
# beyond the print. To reverse it, delete this block (the c46 values above are untouched; cycles/c51/before/ has the
# c50 files). Kept: the printed ramps (RAMP_SPANS), the fermata, CAESURA_BREATH_S, CAESURA_LIFT, and every CAESURA key
# (the breath-gap code and CAESURA_LIFT test membership; a value of 0.0 leaves the tempo unchanged).
# Caesura values: 0.0 where no breath is printed (42, 48, 54, 60, 65, 77, 90, 96, 116, 139, 148, 171, 237, 249) and
# where notes move through a printed breath (164, 188, 196, 204, 259); at the printed breaths that every part holds
# through: critic C's reduced values at the solo breaths 29, 124, 286 and the unchanged 0.15 s at 102 and 268 (both
# inside printed ritardandi).
_C46_TEMPO = {"PHRASE_ARCS": list(PHRASE_ARCS), "TEMPO_PUSH": list(TEMPO_PUSH), "BEAT_STRETCH": dict(BEAT_STRETCH),
              "CAESURA": dict(CAESURA), "APEX_AGOGIC": APEX_AGOGIC}   # the c46 map, for reference only
PHRASE_ARCS = []      # with no arcs the apex loop (APEX_AGOGIC) does nothing
TEMPO_PUSH = []
BEAT_STRETCH = {}
CAESURA = {k_: 0.0 for k_ in CAESURA}
CAESURA.update({29.0: 0.18, 124.0: 0.18, 286.0: 0.16, 102.0: 0.15, 268.0: 0.15})
# The climax breath at 204 (CAESURA_BREATH_SKIP, 0.12 qn) lasted 0.174 s inside c46's slowed quarter beat (41.3 bpm);
# with the caesura's time gone the same 0.174 s is 0.163 qn at 56.25 bpm (new generic CAESURA_BREATH_QN_AT; critic C's
# do-not-touch: the wind and brass breath gaps at 204). 268 keeps its caesura, so its gap is unchanged.
CAESURA_BREATH_QN_AT = {204.0: 0.163}
# Tables written in qn at offsets in seconds from a moved onset, fitted on the c46-c50 map (cycles/c51/actor_scripts/
# qnshift51.py lists every qn-keyed point whose offset from its nearest onset moves by 20 ms or more): the four
# JOIN_NOTCH windows that c46 recomputed go back to their pre-c46 values (the same offsets in seconds on this map);
for _t, _o, _n in [("Violins I", (258.889, 258.948, -5.5), (258.85, 258.93, -5.5)),
                   ("Violins II", (258.860, 258.985, -4.0), (258.81, 258.98, -4.0)),
                   ("Flute 1", (258.897, 258.948, -2.0), (258.86, 258.93, -2.0)),
                   ("Violoncellos", (76.890, 76.988, -4.0), (76.82, 76.98, -4.0))]:
    assert _o in JOIN_NOTCH[_t], (_t, _o)
    JOIN_NOTCH[_t] = [_n if j_ == _o else j_ for j_ in JOIN_NOTCH[_t]]
# Oboe 1's c50 attack shape at 148 (note-on 0.15 s before the beat: 147.85 at 60 bpm) and the basses' c48 pitch-trim
# hold from their fp note's moved onset (147.84)
assert [(147.873, 0.0), (147.903, 4.2), (148.59, 0.0)] in LEVEL_SHAPES["Oboe 1"]
LEVEL_SHAPES["Oboe 1"] = [s_ if s_ != [(147.873, 0.0), (147.903, 4.2), (148.59, 0.0)]
                          else [(147.804, 0.0), (147.85, 4.2), (148.59, 0.0)] for s_ in LEVEL_SHAPES["Oboe 1"]]
assert [(147.8965, 0.0), (148.0, 0.83), (148.12, 2.0), (148.3, 0.0)] in LEVEL_SHAPES["Double basses"]
LEVEL_SHAPES["Double basses"] = [s_ if s_ != [(147.8965, 0.0), (148.0, 0.83), (148.12, 2.0), (148.3, 0.0)]
                                 else [(147.84, 0.0), (148.0, 0.83), (148.12, 2.0), (148.3, 0.0)] for s_ in LEVEL_SHAPES["Double basses"]]

# ---- c51: note starts by critic A's S measure (tools/s_onsets.py; lead decisions 2 and 3) ----
# A #2 (winds and brass): the same pitch pair on one row repeats its latency (note-on to audible start) within 3 ms;
# the 43 per-onset rows (fitted on pcX, which reads slow-swelling targets late) put thematic notes 50-180 ms early.
# One lead per track = the row's median latency, plus a pitch-pair table; every per-onset row of these tracks is
# deleted (build/leg_leads.json) with the stacked extras (LEG_EXTRA_S Horn 1 leaving F4, the old pair extras of Horn 1,
# Oboe 1, Flute 1, Bassoon 1, and Flute 1's soft extra, a tool default)
LEG_EXTRA_S = {k_: v_ for k_, v_ in LEG_EXTRA_S.items() if k_ != "Horn 1"}
LEG_SOFT_EXTRA_S = {k_: v_ for k_, v_ in LEG_SOFT_EXTRA_S.items() if k_ != "Flute 1"}
_c51_row = {"Flute 1": 0.04, "Oboe 1": 0.08, "Cor anglais": 0.06, "Clarinet 1": 0.07, "Clarinet 2": 0.065,
            "Bass clarinet": 0.09, "Bassoon 1": 0.07, "Bassoon 2": 0.075, "Horns 1-2 a2": 0.08, "Horn 1": 0.095,
            "Horn 2": 0.09, "Horn 3": 0.08, "Horn 4": 0.11, "Trombone 1": 0.075}
LEG_LEAD_S = {**_c51_row, **{k_: v_ for k_, v_ in LEG_LEAD_S.items() if k_ not in _c51_row}}   # exact names first
for _t in ("Horn 1", "Oboe 1", "Flute 1", "Bassoon 1"):
    LEG_PAIR_EXTRA_S.pop(_t, None)
LEG_PAIR_EXTRA_S.update({
    "Flute 1": {(72, 73): +0.035, (75, 77): +0.025, (85, 82): +0.035, (90, 89): +0.030, (92, 94): +0.040},
    "Oboe 1": {(68, 67): +0.030, (69, 70): -0.030, (70, 68): +0.065, (70, 72): +0.030, (70, 73): +0.030, (72, 70): -0.035, (73, 72): +0.025, (73, 77): -0.030, (75, 73): +0.030, (77, 78): -0.035, (82, 80): -0.045},
    "Cor anglais": {(58, 60): +0.045, (66, 68): +0.030, (69, 68): +0.025},
    "Clarinet 1": {(75, 74): +0.035},
    "Bass clarinet": {(41, 44): -0.025, (43, 44): +0.030, (44, 37): +0.070, (46, 48): -0.045, (48, 49): +0.055},
    "Bassoon 1": {(53, 51): +0.035, (53, 56): +0.075, (56, 55): -0.030, (60, 61): -0.060},
    "Bassoon 2": {(51, 49): -0.025},
    "Horn 1": {(56, 58): -0.055, (58, 61): +0.075, (60, 65): +0.025, (61, 60): -0.040, (62, 61): -0.050, (63, 61): -0.030, (63, 64): +0.105, (64, 63): +0.075, (65, 63): +0.080, (65, 66): +0.090, (66, 60): -0.040, (68, 66): -0.040, (68, 67): -0.030, (70, 68): -0.040},
    "Horn 2": {(58, 61): +0.030},
    "Horn 3": {(60, 61): +0.030, (61, 60): -0.030, (64, 63): +0.070},
    "Horn 4": {(52, 51): +0.105, (56, 55): -0.080},
    "Trombone 1": {(56, 57): -0.050}})
SLUR_JOIN_LEAD_AT["Horn 4"] = {268.0: 0.05}   # c50's 0.10 overshot (-68 ms)
# A #3 / #4 (strings): 109 per-onset rows in build/leg_leads.json; the bar 55 triplet's rows act only with a higher cap
# (an unconditional entry before the "listed" ones: the first matching window wins)
LEG_CAP_FRAC["Violins I"] = [(181.0, 182.01, 0.75)] + LEG_CAP_FRAC["Violins I"]
LEG_CAP_FRAC["Violins II"] = [(181.0, 182.01, 0.75)] + LEG_CAP_FRAC["Violins II"]
# A #5: Trombone 1's quotation alternated early and late by 59-121 ms (slurred targets led 100 ms against a 74 ms
# latency, re-tongued notes unled); the bar 78 run into 262 started 100-118 ms early at 0.15 s
REATTACK_LEAD_AT["Trombone 1"] = {214.5: 0.04, 216.0: 0.05, 217.0: 0.05, 218.0: 0.04, 219.5: 0.10}
GROUP_LEAD_AT = {"Violins I": [(261.5, 262.0, 0.05)], "Violins II": [(261.5, 262.0, 0.05)]}

# ---- c51: critic B (levels; written for this cycle's map and leads) ----
# B #1: Flute 1's slurred arrival F5 at 108 (new in c50) was 4-6 dB weaker than c49's fresh attack for half a second,
# with a 10.8 dB hole 0.39 s after the beat (lead then 30 ms; now 40 ms, so 10 ms earlier). B's row in seconds from
# the beat (B wrote qn at 1.042 s per qn; this map has 1.000): +3 dB from the beat, +8 dB over the hole
LEVEL_SHAPES["Flute 1"] = LEVEL_SHAPES["Flute 1"] + [
    [(107.96, 0.0), (108.011, 3.0), (108.292, 3.0), (108.344, 8.0), (108.480, 8.0), (108.542, 3.0), (108.636, 3.0), (108.74, 0.0)]]
# B #2: c50's C4 shape put the celli's counter-melody 6-8 dB over the violins' theme at 246 (bar 73): 4.0 -> 0.5,
# the dip before it -1.5 -> -2.5
assert [(244.6, 0.0), (245.0, -1.5), (245.55, -1.5), (245.75, 4.0), (246.6, 4.0), (247.8, 0.0)] in LEVEL_SHAPES["Violoncellos"]
LEVEL_SHAPES["Violoncellos"] = [s_ if s_ != [(244.6, 0.0), (245.0, -1.5), (245.55, -1.5), (245.75, 4.0), (246.6, 4.0), (247.8, 0.0)]
                                else [(244.6, 0.0), (245.0, -2.5), (245.55, -2.5), (245.75, 0.5), (246.6, 0.5), (247.8, 0.0)]
                                for s_ in LEVEL_SHAPES["Violoncellos"]]
# B #3: the bass clarinet's D flat 3 at 108 swelled 4 dB over its body for 0.4 s, level with the flute's arrival:
# -3.5 dB over the swell (B: 0.125-0.375 s after the beat with a 190 ms lead; the lead is 145 ms now, so 45 ms later)
LEVEL_SHAPES["Bass clarinet"] = LEVEL_SHAPES["Bass clarinet"] + [[(108.087, 0.0), (108.17, -3.5), (108.42, -3.5), (108.524, 0.0)]]
# After the range render r1 (S at 0.05 s: Violins I +2, +54, +99, +204 ms; Violins II -18, +50, -11, +91; c50 at
# 0.15 s: -98, -106, -53, +2 and -118, -49, -112, +93): the run's notes 0.08 / 0.06 s, the ff arrival at 262 keeps 0.15
GROUP_LEAD_AT = {"Violins I": [(261.5, 261.9, 0.08), (262.0, 262.0, 0.15)],
                 "Violins II": [(261.5, 261.9, 0.06), (262.0, 262.0, 0.15)]}

# ---- c52 (2026-11-10): string join timing (critic A #1), S1 repeats (A #2), breaths (C #1), level rows (A #5, B #3-#4) ----
# A #1 (the loop lead's test): the string joins that move by 45-112 ms between two renders of identical data are legato
# targets whose row differs from the row of the note they overlap (33 of 163 on the four section tracks; 2 of 276
# same-row joins). _C52_VARIANT chooses the cure (cycles/c52/CHANGES.md has the two-render test of each):
#   "V1": the rows stay; the keyswitch of a row-change legato target is sent 0.15 s before its note-on (new generic
#         KS_ROWCHANGE_LEAD_S; EW's template keyswitches 100-600 ms ahead; ours was 28-38 ms)
#   "V2": every string line stays on Leg Slur MAX (BC_SOFT on all string tracks at any dynamic, BC_SOFT_SKIP empty);
#         the bow change is the CC11 notch only
#   "c51": neither
_C52_VARIANT = __import__("os").environ.get("MVT2_C52_VARIANT", "V2K")   # the environment override is for the test builds only
#   "V2K": V2, and the keyswitch lead of V1 on the row changes that V2 leaves (Sus MAX re-bow pieces into a legato
#         row, into and out of Leg Port MAX)
if _C52_VARIANT in ("V1", "V2K"):
    KS_ROWCHANGE_LEAD_S = 0.15
if _C52_VARIANT in ("V2", "V2K"):
    BC_SOFT = dict(BC_SOFT, tracks=("Violins I", "Violins II", "Violas", "Violoncellos", "Violin I solo",
                                    "Violoncellos div", "Violas div"), max_cc=127)
    BC_SOFT_SKIP = {}
# A #2 (S1). Basses' pp repeats at 144 / 156 / 168: the release of the old note filled the 60 ms gap in c51 (own-band
# dip 1.0 dB at 144; c50 11.3 with the same data in seconds): the -9 dB gap shape of 253 (note-off -160 ms, note-on
# -100 ms at all four)
LEVEL_SHAPES_S["Double basses"] = LEVEL_SHAPES_S["Double basses"] + [
    (_q, [(-0.160, 0.0), (-0.154, -9.0), (-0.103, -9.0), (-0.097, 0.0)]) for _q in (144.0, 156.0, 168.0)]
# Violins II 120 and Violins II div 120 (Flautando, pp; own-band dips 2.6 and 2.0 dB): 6 dB deeper inside the played
# gap (120 ms and 80 ms before the beat)
LEVEL_SHAPES_S["Violins II"] = LEVEL_SHAPES_S.get("Violins II", []) + [(120.0, [(-0.120, 0.0), (-0.100, -6.0), (-0.015, -6.0), (0.0, 0.0)])]
LEVEL_SHAPES_S["Violins II div"] = LEVEL_SHAPES_S.get("Violins II div", []) + [(120.0, [(-0.080, 0.0), (-0.065, -6.0), (-0.010, -6.0), (0.0, 0.0)])]
# Horn 2 208 (ff tenuto repeat of C sharp 4, bar 62; gap 33 ms, no dip, no new attack) and Violas 81 (D flat 4, bar 27;
# played gap 6 ms: the 66 ms cut less the stroke's 60 ms lead): new generic REP_GAP_AT. Horn 2: 0.08 s gap with a CC11
# fall; Violas: 0.15 s before the score onset = 0.09 s before the moved note-on
REP_GAP_AT = {"Horn 2": {208.0: {"gap_s": 0.08, "fall_cc": 8, "fall_s": 0.12}},
              "Violas": {81.0: {"gap_s": 0.15}}}
# A #5: Violins I's pickup at 249 after the rest reached body - 6 dB at +146 ms (Violins II at -30 ms): lead 0.18 -> 0.26 s
REATTACK_LEAD_AT["Violins I"] = {**REATTACK_LEAD_AT["Violins I"], 249.0: 0.26}
# C #1: five printed breaths too short to be heard (Flute 1 / Oboe 1 196: 95 ms; Horn 1 196: 137 ms; Trombone 2 204:
# 74 ms; Bass trombone 204: 24 ms). Keyed by the onset of the note that ends at the breath; min(value, 0.6 x length)
BREATH_GAP_AT.setdefault("Flute 1", {})[195.5] = 0.2
BREATH_GAP_AT.setdefault("Oboe 1", {})[195.5] = 0.2
BREATH_GAP_AT.setdefault("Horn 1", {})[195.5] = 0.3
BREATH_GAP_AT.setdefault("Trombone 2", {})[202.0] = 0.26
BREATH_GAP_AT.setdefault("Bass trombone", {})[200.0] = 0.30
# B #3 (critic B finding 3): the bass clarinet's c51 cut at 108 began 100 ms before the swell (a 2 dB dip, then a
# 4.4 dB bump): 0 dB at 0.215 s after the beat, -5 from 0.275 to 0.385 s, 0 at 0.455 s (1 qn = 1.0 s here)
assert [(108.087, 0.0), (108.17, -3.5), (108.42, -3.5), (108.524, 0.0)] in LEVEL_SHAPES["Bass clarinet"]
LEVEL_SHAPES["Bass clarinet"] = [s_ if s_ != [(108.087, 0.0), (108.17, -3.5), (108.42, -3.5), (108.524, 0.0)]
                                 else [(108.215, 0.0), (108.275, -5.0), (108.385, -5.0), (108.455, 0.0)]
                                 for s_ in LEVEL_SHAPES["Bass clarinet"]]
# B #4 (critic B finding 4, optional): Flute 1's fill over the hole at 108 reached +8 dB at +344 ms, the hole begins at
# +330 ms and is lowest at +375 ms: +9.5 dB from 0.345 to 0.40 s, +8 kept to 0.48 s
_f108 = [(107.96, 0.0), (108.011, 3.0), (108.292, 3.0), (108.344, 8.0), (108.480, 8.0), (108.542, 3.0), (108.636, 3.0), (108.74, 0.0)]
assert _f108 in LEVEL_SHAPES["Flute 1"]
LEVEL_SHAPES["Flute 1"] = [s_ if s_ != _f108 else
                           [(107.96, 0.0), (108.011, 3.0), (108.292, 3.0), (108.345, 9.5), (108.40, 9.5), (108.42, 8.0), (108.480, 8.0), (108.542, 3.0), (108.636, 3.0), (108.74, 0.0)]
                           for s_ in LEVEL_SHAPES["Flute 1"]]

# ---- c53 (2026-11-10): what the one-row string change left (critics A, B, C on the c52 render; lead notes) ----
# B #1: string transition peaks. The JOIN_NOTCH windows of the string legato joins were written in absolute qn; the c51
# tempo map and the c51-c52 lead refits moved the note-ons and left the windows behind (celli 68.5: -3.9 dB at the peak
# instead of -8, the full depth in the hole after it). They move to the new generic JOIN_NOTCH_S (seconds from the
# target's moved note-on; tools/score_to_parts.py), refitted on the c52 stems with every old window taken out
# (cycles/c53/actor_scripts/joinpeak53.py --fit: the span where the 30 ms stem level is more than 2 dB over both note
# bodies, depth = peak excess - 2 dB; kept where the raw peak is 5 dB or more over both bodies with a master bump of
# 2.5 dB or more, or 4 dB or more at a join that had a window). Windows that are not legato joins stay in JOIN_NOTCH.
_c53_drop = {"Violins I": [(67.86, 68.02, -3.0), (73.37, 73.55, -5.5), (74.90, 74.98, -3.0), (79.86, 80.03, -3.0),
                           (207.80, 207.97, -4.0), (86.38, 86.51, -5.5), (258.85, 258.93, -5.5), (85.84, 85.98, -6.0)],
             "Violoncellos": [(68.37, 68.49, -8.0), (240.37, 240.45, -5.0), (200.52, 200.90, -5.0), (76.82, 76.98, -4.0)],
             "Violins II": [(177.35, 177.52, -4.3), (242.99, 243.05, -3.3), (245.39, 245.47, -3.9), (270.41, 270.50, -5.0),
                            (73.33, 73.42, -4.0), (82.84, 82.91, -3.5), (86.40, 86.50, -4.0), (258.81, 258.98, -4.0),
                            (85.79, 85.95, -5.0), (86.78, 86.98, -5.5)],
             "Violin I solo": [(52.99, 53.15, -4.0), (50.89, 50.93, -2.5)],
             "Violas": [(56.81, 56.93, -6.0)]}
for _t, _rows in _c53_drop.items():
    for _r in _rows:
        assert _r in JOIN_NOTCH[_t], (_t, _r)
    JOIN_NOTCH[_t] = [j_ for j_ in JOIN_NOTCH[_t] if j_ not in _rows]
JOIN_NOTCH_S = {
    "Violins I": {
        75: {"shape": [[0.026, 0.0], [0.047, -0.5], [0.067, -1.9], [0.086, -3.1], [0.107, -2.9], [0.127, -0.7], [0.146, 0.0], [0.206, 0.0], [0.227, 0.4], [0.247, 1.4], [0.266, 0.6], [0.286, 0.0]]},   # old: raw peak +5.7 dB over both bodies +0.107 s from the note-on, master +1.8
        86: {"shape": [[-0.011, 0.0], [0.009, -0.9], [0.029, -2.8], [0.049, -3.6], [0.069, -3.0], [0.089, -1.8], [0.109, -1.2], [0.129, -0.5], [0.149, 0.0], [0.169, -0.3], [0.189, -2.2], [0.209, -3.1], [0.229, -1.7], [0.249, -0.9], [0.269, 0.0]]},   # old: raw peak +5.9 dB over both bodies +0.209 s from the note-on, master +1.1
        86.5: {"shape": [[-0.053, 0.0], [-0.033, -0.4], [-0.013, -1.7], [0.007, -3.1], [0.027, -3.5], [0.047, -3.1], [0.067, -2.9], [0.087, -3.6], [0.107, -4.1], [0.127, -3.0], [0.147, -0.9], [0.167, 0.0]]},   # master: raw peak +6.3 dB over both bodies +0.107 s from the note-on, master +4.1
        177.5: {"shape": [[-0.068, 0.0], [-0.048, -0.3], [-0.028, -1.1], [-0.008, -1.3], [0.012, -1.0], [0.032, -0.9], [0.052, -1.2], [0.072, -1.2], [0.092, -0.9], [0.112, -0.3], [0.132, 0.0], [0.152, -1.8], [0.172, -3.5], [0.192, -3.4], [0.212, -1.4], [0.232, 0.0]]},   # master: raw peak +6.0 dB over both bodies +0.182 s from the note-on, master +3.2
        186: {"shape": [[-0.052, 0.0], [-0.032, -0.3], [-0.012, -0.9], [0.008, -1.4], [0.028, -2.3], [0.048, -3.0], [0.068, -3.4], [0.088, -3.5], [0.108, -3.0], [0.128, -1.4], [0.148, 0.0]]},   # master: raw peak +5.5 dB over both bodies +0.078 s from the note-on, master +4.8
        208: {"shape": [[0.046, 0.0], [0.066, -1.5], [0.085, -1.9], [0.106, -0.5], [0.126, 0.0]]},   # old: raw peak +4.4 dB over both bodies +0.085 s from the note-on, master +1.3
        249.5: {"shape": [[-0.092, 0.0], [-0.072, -0.4], [-0.052, -0.8], [-0.032, -1.3], [-0.012, -1.9], [0.008, -2.7], [0.028, -3.9], [0.048, -3.9], [0.068, -2.5], [0.088, -0.7], [0.108, 0.0]]},   # master: raw peak +6.3 dB over both bodies +0.038 s from the note-on, master +3.4
    },
    "Violins II": {
        87: {"shape": [[0.05, 0.0], [0.07, -0.3], [0.09, -1.5], [0.11, -2.1], [0.13, -1.4], [0.15, -0.5], [0.17, 0.0]]},   # old: raw peak +4.3 dB over both bodies +0.110 s from the note-on, master +4.6
        177.5: {"shape": [[0.011, 0.0], [0.031, -0.3], [0.051, -1.2], [0.071, -2.2], [0.091, -2.9], [0.111, -2.4], [0.131, -0.9], [0.151, 0.0], [0.171, -0.5], [0.191, -1.5], [0.211, -1.2], [0.231, -0.8], [0.251, -0.4], [0.271, 0.0]]},   # old: raw peak +5.2 dB over both bodies +0.101 s from the note-on, master -0.8
        190: {"shape": [[-0.03, 0.0], [-0.01, -0.5], [0.01, -1.8], [0.03, -2.8], [0.05, -4.1], [0.07, -5.8], [0.09, -6.5], [0.11, -6.1], [0.13, -5.0], [0.15, -2.8], [0.17, -0.7], [0.19, 0.0]]},   # master: raw peak +8.6 dB over both bodies +0.090 s from the note-on, master +3.7
        245.5: {"shape": [[0.013, 0.0], [0.033, -2.3], [0.053, -4.6], [0.073, -4.2], [0.093, -2.0], [0.113, 0.0]]},   # master: raw peak +7.1 dB over both bodies +0.063 s from the note-on, master +3.6
        259: {"shape": [[-0.009, 0.0], [0.011, -0.7], [0.031, -2.6], [0.051, -3.3], [0.071, -2.9], [0.091, -2.6], [0.111, -1.9], [0.131, -0.4], [0.151, 0.0]]},   # old: raw peak +5.5 dB over both bodies +0.051 s from the note-on, master -0.0
        266: {"shape": [[0.034, 0.0], [0.054, -1.9], [0.074, -4.1], [0.094, -4.3], [0.114, -2.1], [0.134, 0.0]]},   # listed: raw peak +7.0 dB over both bodies +0.094 s from the note-on, master +2.1
    },
    "Violas": {
        57: {"shape": [[0.011, 0.0], [0.031, -0.6], [0.051, -0.9], [0.071, -1.5], [0.091, -2.0], [0.111, -2.2], [0.131, -1.3], [0.151, 0.0]]},   # old: raw peak +4.3 dB over both bodies +0.111 s from the note-on, master -1.0
        116.333: {"shape": [[0.029, 0.0], [0.049, -0.6], [0.069, -1.9], [0.089, -3.1], [0.109, -3.8], [0.129, -3.1], [0.149, -1.9], [0.169, -1.6], [0.189, -0.7], [0.209, 0.0]]},   # master: raw peak +5.9 dB over both bodies +0.109 s from the note-on, master +3.2
        256: {"shape": [[0.048, 0.0], [0.068, -0.8], [0.088, -3.0], [0.108, -4.7], [0.128, -4.7], [0.148, -3.3], [0.168, -1.8], [0.188, -0.4], [0.208, 0.0]]},   # listed: raw peak +7.1 dB over both bodies +0.118 s from the note-on, master +1.9
    },
    "Violoncellos": {
        48: {"shape": [[-0.01, 0.0], [0.01, -0.5], [0.03, -1.9], [0.05, -3.1], [0.07, -3.7], [0.09, -3.6], [0.11, -2.8], [0.13, -2.6], [0.15, -1.9], [0.17, -0.3], [0.19, 0.0]]},   # master: raw peak +5.9 dB over both bodies +0.090 s from the note-on, master +3.2
        68.5: {"shape": [[-0.073, 0.0], [-0.053, -1.1], [-0.033, -2.3], [-0.013, -3.6], [0.007, -5.8], [0.027, -7.6], [0.047, -8.6], [0.067, -9.2], [0.087, -9.6], [0.107, -9.5], [0.127, -8.3], [0.147, -6.1], [0.167, -3.6], [0.187, -1.7], [0.207, -0.4], [0.227, 0.0]]},   # master: raw peak +11.7 dB over both bodies +0.107 s from the note-on, master +6.9
        77: {"shape": [[-0.121, 0.0], [-0.091, -2.9], [-0.071, -3.1], [-0.051, -3.2], [-0.031, -3.9], [-0.011, -4.2], [0.009, -2.6], [0.029, -1.8], [0.049, -3.9], [0.069, -6.3], [0.089, -7.6], [0.109, -7.9], [0.129, -6.8], [0.149, -4.4], [0.169, -2.5], [0.189, -1.5], [0.209, -0.4], [0.229, 0.0]]},   # master: raw peak +10.0 dB over both bodies +0.109 s from the note-on, master +5.4
        174: {"shape": [[0.045, 0.0], [0.065, -1.2], [0.085, -2.9], [0.105, -3.9], [0.125, -3.3], [0.145, -1.6], [0.165, 0.0]]},   # master: raw peak +6.1 dB over both bodies +0.115 s from the note-on, master +3.2
        188: {"shape": [[0.113, 0.0], [0.133, -0.4], [0.153, -2.2], [0.173, -2.8], [0.193, -1.3], [0.213, 0.0]]},   # master: raw peak +5.1 dB over both bodies +0.173 s from the note-on, master +2.9
        193: {"shape": [[-0.124, 0.0], [-0.094, -0.7], [-0.074, -1.2], [-0.054, -1.9], [-0.034, -2.7], [-0.014, -3.0], [0.006, -3.2], [0.026, -3.3], [0.046, -3.7], [0.066, -4.1], [0.086, -4.7], [0.106, -6.3], [0.126, -7.7], [0.146, -8.4], [0.166, -8.0], [0.186, -6.7], [0.206, -4.3], [0.226, -2.2], [0.246, -2.0], [0.266, -0.6], [0.286, 0.0], [0.306, -1.2], [0.326, -1.6], [0.346, -2.2], [0.366, -3.3], [0.396, 0.0]]},   # listed: raw peak +10.6 dB over both bodies +0.156 s from the note-on, master +2.5
        240.5: {"shape": [[-0.068, 0.0], [-0.048, -1.1], [-0.028, -2.8], [-0.008, -5.6], [0.012, -8.6], [0.032, -10.4], [0.052, -11.2], [0.072, -10.0], [0.092, -6.5], [0.112, -3.3], [0.132, -1.4], [0.152, 0.0]]},   # master: raw peak +13.4 dB over both bodies +0.062 s from the note-on, master +9.4
        249: {"shape": [[-0.01, 0.0], [0.01, -1.9], [0.03, -4.3], [0.05, -5.7], [0.07, -5.6], [0.09, -4.1], [0.11, -2.1], [0.13, -0.7], [0.15, 0.0]]},   # master: raw peak +8.0 dB over both bodies +0.060 s from the note-on, master +4.6
    },
    "Violin I solo": {
        51: {"shape": [[0.009, 0.0], [0.029, -0.6], [0.049, -2.2], [0.069, -1.8], [0.089, 0.0]]},   # old: raw peak +4.9 dB over both bodies +0.059 s from the note-on, master +3.6
    },
    "Violas div": {
        71: {"shape": [[-0.118, 0.0], [-0.088, -3.5], [-0.068, -3.9], [-0.048, -2.9], [-0.028, -0.9], [-0.008, 0.0], [0.072, 0.0], [0.092, -1.1], [0.112, -4.4], [0.132, -6.6], [0.152, -6.4], [0.172, -5.7], [0.192, -4.9], [0.212, -3.0], [0.232, -0.4], [0.252, 0.0]]},   # listed: raw peak +9.0 dB over both bodies +0.142 s from the note-on, master -0.1
        286: {"shape": [[-0.121, 0.0], [-0.091, -0.7], [-0.071, -1.2], [-0.051, -1.6], [-0.031, -1.6], [-0.011, -1.8], [0.009, -3.1], [0.029, -3.6], [0.049, -3.5], [0.069, -4.1], [0.089, -5.5], [0.109, -6.6], [0.129, -6.5], [0.149, -5.5], [0.169, -4.2], [0.189, -2.8], [0.209, -0.9], [0.229, 0.0]]},   # master: raw peak +8.8 dB over both bodies +0.129 s from the note-on, master +4.1
    },
}
# residual shapes fitted on the c53 render (build/join_notch_fits.json, cycles/c53/actor_scripts/notchres53.py; stem fix):
# added to the join's row
if __import__("os").path.exists(f"{BUILD}/join_notch_fits.json"):
    for _t, _d in __import__("json").load(open(f"{BUILD}/join_notch_fits.json")).items():
        for _k, _v in ((k_, v_) for k_, v_ in (_d.items() if not _t.startswith("_") else [])):
            _old = JOIN_NOTCH_S.setdefault(_t, {}).pop(next((q_ for q_ in JOIN_NOTCH_S[_t] if abs(q_ - float(_k)) < 0.02), None), None)
            JOIN_NOTCH_S[_t][float(_k)] = ([] if _old is None else _old if isinstance(_old, list) else [_old]) + (_v if isinstance(_v, list) else [_v])
if __import__("os").environ.get("MVT2_C53_NO_NOTCH"):   # for the fitting scan only (cycles/c53/actor_scripts/notchsel53.py)
    JOIN_NOTCH_S = {}
# B #3 (build/note_trims.json Horn 1 190 / 192 / 195.5 / 198): the trim's default 0.6 s ramp realised 0 of +4 dB on the
# 0.285 s pickup at 195.5 and 2.4 of 3.5 dB at 192: short ramps on the three short notes
NOTE_TRIM_RAMP_S["Horn 1"] = {**NOTE_TRIM_RAMP_S.get("Horn 1", {}), 192.0: 0.2, 198.0: 0.2}
# the pickup at 195.5 (B: +4.0; C #3b): +4 dB from just before the score onset to the note-off (0.291 s after it), gone
# 40 ms later, so the lift does not ring on in the breath (as a note trim the gap floor rose from -42.2 to -39.7 dB)
LEVEL_SHAPES_S["Horn 1"] = LEVEL_SHAPES_S.get("Horn 1", []) + [(195.5, [(-0.07, 0.0), (-0.02, 4.0), (0.27, 4.0), (0.31, 0.0)])]
# A #5: Violas 81 (D flat 4 repeat, bar 27): the 90 ms gap dipped 3-4 dB on the stem: -5 dB inside the gap
LEVEL_SHAPES_S["Violas"] = LEVEL_SHAPES_S.get("Violas", []) + [(81.0, [(-0.150, 0.0), (-0.135, -5.0), (-0.070, -5.0), (-0.055, 0.0)])]
# A #3: Violins I 262 (B flat 6, ff, after the Sus MAX run): S +89 ms in two sessions with a 150 ms lead. A's 230 ms
# read -105 ms in the c53 range pass (r1) and its note-on lay before the audible start of the run's last note (A flat 6
# at 261.833: S +11 -> -45 ms, own-band level -1.4 dB): 190 ms, halfway (range pass r2)
assert GROUP_LEAD_AT["Violins I"] == [(261.5, 261.9, 0.08), (262.0, 262.0, 0.15)]
GROUP_LEAD_AT["Violins I"] = [(261.5, 261.9, 0.08), (262.0, 262.0, 0.19)]
# A #5 / B: Horn 2 208 (ff tenuto repeat): the gap's low point lay on the beat (stem -36 dB at 0 to +60 ms, back
# within 3 dB at +200 ms), so the note was heard late: note-on and gap 40 ms earlier (gap_s counts from the score onset)
REP_GAP_AT["Horn 2"] = {208.0: {"gap_s": 0.12, "fall_cc": 8, "fall_s": 0.12}}
REATTACK_LEAD_AT["Horn 2"] = {**REATTACK_LEAD_AT.get("Horn 2", {}), 208.0: 0.04}
# C #5 (finale technique 50): the printed diminuendo 268-271 (ff to p, 3.9 s) put 50-94 % of its fall into the last
# quarter on the eight tracks still on the curve (Violins I 0.0 / -0.4 / -6.4 dB per quarter): linear, as celli and violas
for _t in ("Flute 1", "Oboe 1", "Cor anglais", "Clarinet 1", "Bassoon 1", "Horn 3", "Horn 4", "Violins I"):
    HP_CURVE["linear"][_t] = HP_CURVE["linear"].get(_t, []) + [(268.0, 271.0)]
# A #3 fallback switch for the range pass only (the kept value is the literal above; see cycles/c53/CHANGES.md)
if __import__("os").environ.get("MVT2_C53_VLN1_262"):
    GROUP_LEAD_AT["Violins I"] = [(261.5, 261.9, 0.08), (262.0, 262.0, float(__import__("os").environ["MVT2_C53_VLN1_262"]))]
# C #3 (test only, range pass): Violas div on the section's KS Master (Close + Main) instead of the DIV B patch (Close
# only, a mono source). Not kept unless cycles/c53/CHANGES.md says so; the environment switch builds the test variant
if __import__("os").environ.get("MVT2_C53_DIVTEST"):
    TRACKS = [(n_, st_, (p_.replace("Violas Divisi/06 Keyswitch/Violas KS Master DIV B.oib", "Violas/06 Keyswitch/Violas KS Master.oib") if n_ == "Violas div" else p_), f_, x_)
              for n_, st_, p_, f_, x_ in TRACKS]

# ---- c54 (2026-11-10): critics A, B, C on the c53 render, the lead's merge. Table edits: cycles/c54/actor_scripts/edits54.py
# (level_fits, note_trims, pitch_trims, roles, rebow_fills, leg_leads, early_fills, mix.json) ----
# A #1 (S1): Clarinet 1's slurred tenuto repeat at 289 (D flat 5, bar 88) was an 81 ms silence, a 7.5 dB hole in the
# master, deeper than the printed breath at 286: 30 ms gap, CC11 fall 3 (Horn 3's c45 row stays)
WIND_REP_RETONGUE_AT["Clarinet 1"] = {289.0: {"gap_s": 0.03, "fall_cc": 3}}
# the gap was not set by gap_s: the 286 note is on the legato row and ends 0.01 qn before the keyswitch to Sus Non Vib,
# which lay KS_LEAD = 0.06 qn before 289. New generic KS_LEAD_AT: that keyswitch 0.02 qn (23 ms) before the note, so the
# note ends 0.03 qn (35 ms) before the repeat
KS_LEAD_AT = {"Clarinet 1": {289.0: 0.02}}
# range pass: gap 81 -> 46 ms, but the stem's dip stayed (9.3 -> 10.0 dB): its floor is the legato note's release under
# the slow start of the Sus Non Vib note, not the gap. A fill over the join (fitted after the render on the stem)
LEVEL_SHAPES_S["Clarinet 1"] = LEVEL_SHAPES_S.get("Clarinet 1", []) + [(289.0, [(-0.04, 0.0), (-0.02, 2.5), (-0.005, 5.0), (0.0, 6.5), (0.02, 6.5), (0.03, 4.0), (0.045, 1.5), (0.06, 0.0)])]
# (rendered with +5 dB from -0.05 to +0.04 s: stem dip 4.7 dB but a 4 dB bump 60 ms before the beat and a master dip of
# 6.3 dB; the shape above follows the hole in 20 ms frames, stem fix)
# B #1: three wind notes 5-13 dB under both neighbours inside a slur (note_trims.json): 0.1 s ramps
NOTE_TRIM_RAMP_S["Flute 1"] = {**NOTE_TRIM_RAMP_S.get("Flute 1", {}), 199.0: 0.1, 135.0: 0.1}
NOTE_TRIM_RAMP_S["Bassoon 1"] = {**NOTE_TRIM_RAMP_S.get("Bassoon 1", {}), 199.0: 0.1}   # 201: a row in level_fits.json, up on the beat
# B #1: Flute 1 133.5 (A flat 5 eighth, bar 43) decays inside itself (-48 dB on the beat, -62 at +0.24 s; its neighbours
# -44.5 / -45.4): a shape that follows the decay and is gone at the next note-on (0.46 s after the printed onset; held
# to the note-off it lifted the transition into 134 to 3 dB over the bodies)
LEVEL_SHAPES_S["Flute 1"] = LEVEL_SHAPES_S.get("Flute 1", []) + [(133.5, [(-0.04, 0.0), (0.0, 2.0), (0.10, 6.0), (0.20, 11.0), (0.28, 12.0), (0.38, 10.0), (0.46, 0.0)])]
# B #5: Horn 1's pickup at 195.5 before the breath: the c53 shape of +4 dB left it 5.7 dB under the E flat before it and
# 8.3 dB under the F sharp after it (pickup and breath read as one 390 ms hole): +7.5 dB, same times; the gap is unchanged
assert (195.5, [(-0.07, 0.0), (-0.02, 4.0), (0.27, 4.0), (0.31, 0.0)]) in LEVEL_SHAPES_S["Horn 1"]
LEVEL_SHAPES_S["Horn 1"] = [s_ if s_ != (195.5, [(-0.07, 0.0), (-0.02, 4.0), (0.27, 4.0), (0.31, 0.0)])
                            else (195.5, [(-0.07, 0.0), (-0.02, 7.5), (0.27, 7.5), (0.31, 0.0)]) for s_ in LEVEL_SHAPES_S["Horn 1"]]
# C #4: the ff cadence (bars 79-81). Both violin tracks lost 3 dB across qn 266-267: the hairpin gain of the crescendo
# 261-262 (HP_GAIN_DB, held to the first onset after the arrival, here 266, then released over HP_REL = 1 qn) ran out
# two quarters before the printed diminuendo at 268. The shape cancels that release and lets go at 268, with the dim.
# Violins II let go after pcX's window at 268 (a fall across the note start read 35 ms early, simulated).
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(266.0, 0.0), (267.0, 3.0), (267.85, 3.0), (268.25, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(266.0, 0.0), (267.0, 3.0), (268.36, 3.0), (268.9, 0.0)]]
# The strings were softer at ff (bar 79) than at the f before it (all strings -23.7 against -23.1 dB): Violins I +2 dB
# and Violins II +1.5 dB over 262-268 (C: roles [250, 262, 2] -> [250, 268, 2] and [262, 268, -1.5] removed). As shapes
# that begin 0.45 s after the beat of 262, because the role edits changed the envelope inside the window tools/pcx.py
# reads the attack in (S at 262 +2 -> +34 ms, at 268 -6 -> -41 ms with no change to the notes)
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(262.36, 0.0), (262.7, 2.0), (267.85, 2.0), (268.25, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES["Violins II"] + [[(262.36, 0.0), (262.7, 1.5), (267.6, 1.5), (267.85, 0.0)]]
# Violins II stayed within 1 dB over 268-270 and fell 13.3 dB at the barline of 271 (CC11 84 at 270 against Violins I's
# 69: the track was still on the curved hairpin): linear, as c53 gave the eight other tracks
HP_CURVE["linear"]["Violins II"] = HP_CURVE["linear"].get("Violins II", []) + [(268.0, 271.0)]
# B #4: two peaks that lie on the note before the join (the old note swelling 40-100 ms before the new note-on), and
# the transition into Violins I 86.5 over a weak body: windows in seconds from the target's moved note-on
JOIN_NOTCH_S.setdefault("Violins II", {})[177.0] = (-0.12, -0.02, -4.5)
JOIN_NOTCH_S.setdefault("Violins I", {})[65.5] = (-0.14, -0.05, -3.0)
_n865 = JOIN_NOTCH_S["Violins I"][86.5]
assert isinstance(_n865, dict) and min(d_ for _, d_ in _n865["shape"]) == -4.1
JOIN_NOTCH_S["Violins I"][86.5] = {"shape": [[x_, round(d_ * 6.0 / 4.1, 2)] for x_, d_ in _n865["shape"]]}   # depth -4.1 -> -6.0, same window
# Finale technique 46 (the lead's trial; range passes p1 / p2 without and q1 / q2 with the reset, one session): a
# round-robin reset before the Violins II theme. Two passes agreed to 0 ms either way, but without the reset 9 of the 24
# joins of bars 22-30 lay 15-87 ms from the passes with it, and the passes with it gave the c53 full render's values
# (66 / 72 / 75: -18 / -47 / -3 ms; without: +49 / +40 / -51): with the reset a range pass is a valid base for fitting
RR_RESET_AT = {**RR_RESET_AT, "Violins II": [58.0]}

# ---- cycle 55 (Dan, 2026-11-11, on the track view: "the volume adjustment was adjusted in large peaks and valleys on so
# many individual notes ... To me it seemed unnatural"; critics A, B, C on the c54 render; the lead's merge) ----
# MVT2_C55 (environment, test builds only) switches the stages: g = grid / breakpoints, r = rule layers off, t = trims
# keyed to the score onset, c = start cap. Default: all. The table edits of the cycle are made by
# cycles/c55/actor_scripts/edits55.py from cycles/c55/before/ (early_fills, rebow_fills, roles, mix.json).
_C55 = __import__("os").environ.get("MVT2_C55", "grtc")
if "g" in _C55:
    # Section 4: slow layers as ramps. vol_db sampled on 0.125 qn (the grid build_reaper.py writes), every item's
    # breakpoints written (a shape meant to be up on the beat is up on the beat); mix.json env_simplify_db 0.1 then
    # drops the points that lie on the line between their neighbours
    VOL_GRID_QN = 0.125
    VOL_BP_ALL = True
    VOL_BP_ALL_SKIP = ("timp",)
if "r" in _C55:
    # Section 2: rule layers with no measured benefit leave the envelope (critics A #2, B #4, C #1; each divided out of
    # the c54 stems alone): the long-note swell's dB copy (193 notes: range inside the note 6.2 dB with, 5.5 without;
    # the CC11 swell stays), the sostenuto hold on winds and brass (31 rows: 5 more even, 14 less; kept on the strings,
    # where it holds the violas' line of bars 61-64), the metric steps on harp and pizzicato (113 onsets; the round
    # robins vary by more), the phrase-top contour (31 rows, no line better, four worse), the slur-pair release (15
    # rows, a fall after the note start under a sounding line; no named fault)
    ENV_LAYER = {**ENV_LAYER, "swell_db": "off", "metric_db": "off", "phrase_tops": "off", "slur_pair_release": "off",
                 **{f"{t_[0]}:sost_hold": "off" for t_ in TRACKS if t_[3] in ("wind", "brass")}}
    # the harp of bars 37-44 keeps its metric steps: the only one of the five plucked passages where they measure as a
    # help (median step between consecutive notes 0.83 dB with, 1.30 without; A: 0.6 / 1.1)
    ENV_LAYER["Harp:metric_db"] = "on"
    METRIC_SPANS = [(108, 140)]
REBOW_FILL_SPLIT = 1.0   # critic B #3: the lists' medians are class level (sound unchanged)
LEVEL_ROW_SPLIT = 1.0    # critic C #3: the same for fitted rows that move inside their note (sound unchanged)
if "t" in _C55:
    # Section 3: level trims step at the next note's score onset over 80 ms (see TRIM_KEY in tools/score_to_parts.py)
    TRIM_KEY = "score"
    TRIM_RAMP_KEEP_FITTED = "T" not in _C55
    # where the trims rise across a legato join the window sits half the lead before the beat (simulated on the c54
    # stems: join holes of 6 dB or more 281 at the beat, 266 at half the lead, 257 at the moved note-on; join peaks of
    # 3 dB or more 211 / 224 / 233, c54 234; the full lead also made three more lines rougher)
    TRIM_RISE_LEAD = float(__import__("os").environ.get("MVT2_C55_RISE", "0.5"))
if "c" in _C55:
    # Section 3: the summed start shapes of one note are clipped at +6 dB (16 notes summed to 8 dB or more: an early
    # fill on top of a fitted row). Re-bow and loop fills are not start shapes; join notches are cuts
    START_SHAPE_CAP = {"db": 6.0, "pre_s": 0.15, "post_s": 0.6,
                       "skip_layers": ["rebow_fill", "loop_fill", "loop_profile", "join_notch", "join_notch_s", "start_cap",
                                       "early_fill_rekey"],
                       # skipped: 40 notes whose front is not over the body with the full shapes (front minus body at most
                       # +1 dB on the simulated stems: the shapes fill a measured sag), the timpani strokes, and the printed
                       # attacks (sf tremolo chord at 212, the fp at 148, Trombone 1's accent at 218), and Violoncellos 253
                       # (+11.9, fitted in c54 on its 100 ms steps; capped, S read -22 ms for -4). Capped: Flute 1 134
                       # (+10.6), Oboe 1 57 (+6.9), Violoncellos 132 (+6.1)
                       "skip": {"Flute 1": [108.0, 111.0, 118.0, 130.0, 131.5, 133.5], "Oboe 1": [55.5, 56.0, 140.0, 145.0, 270.0, 270.5],
                                "Cor anglais": [126.0, 129.5, 131.5, 132.0, 133.5, 135.0], "Clarinet 1": [283.0, 289.0],
                                "Bassoon 1": [264.0], "Horn 1": [37.5], "Timpani": [172.0, 262.0], "Violins I": [68.0, 71.0, 212.0],
                                "Violins II": [66.0, 108.0, 154.0, 206.0, 210.0, 212.0], "Violas": [78.0, 238.0, 212.0],
                                "Violoncellos": [139.0, 188.0, 208.0, 248.5, 250.0, 253.0, 265.0, 267.0],
                                "Double basses": [140.0, 148.0], "Violoncellos div": [62.0], "Trombone 1": [218.0],
                                "Bass trombone": [212.0]}}
# Section 2 (critic A #3): the celli's notch at 68.5 cut a hole in front of the burst it was fitted for (stem: 8 dB under
# the bodies 0.26-0.20 s before the beat; without it a 6 dB peak 0.18-0.14 s before the beat, after the c54 lead change
# at 68). The same shape 50 ms later at 0.6 of its depth: the stem stays within -3 / +2 dB of the bodies (simulated)
_n685 = JOIN_NOTCH_S["Violoncellos"][68.5]
assert isinstance(_n685, dict) and min(d_ for _, d_ in _n685["shape"]) == -9.6
JOIN_NOTCH_S["Violoncellos"][68.5] = {"shape": [[round(x_ + 0.05, 3), round(d_ * 0.6, 2)] for x_, d_ in _n685["shape"]]}
# The level the removed layers carried, given back as slow rows (critic C #1: "give the climax its 1.2 dB back"; here
# per track, from the section levels simulated on the c54 stems without the layers): bars 61-62, where the sostenuto
# hold had lifted the winds' and brass's ff long notes, and the ff cadence bars 79-80, where the long-note swell had
if "r" in _C55:
    for _t, _d in (("Flute 1", 0.9), ("Flute 2", 1.2), ("Oboe 1", 0.9), ("Oboe 2", 0.6), ("Bass clarinet", 1.0), ("Bassoon 1", 1.5),
                   ("Bassoon 2", 1.3), ("Contrabassoon", 0.7), ("Horn 1", 0.9), ("Horn 2", 0.6), ("Horn 3", 0.9), ("Trombone 2", 1.2),
                   ("Bass trombone", 0.6), ("Tuba", 0.6)):
        LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(203.5, 0.0), (204.25, _d), (211.75, _d), (212.25, 0.0)]]
    for _t, _d in (("Flute 1", 1.1), ("Flute 2", 1.0), ("Clarinet 1", 1.3), ("Bassoon 1", 1.0), ("Bassoon 2", 0.8), ("Cor anglais", 0.8)):
        LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(261.9, 0.0), (262.1, _d), (267.75, _d), (268.25, 0.0)]]
# Section 3, the join-peak check after the trims moved: seven transition peaks of 5 dB or more over the louder body that
# the old trim ramps had cut by accident (Violins II 82 +6.9, Violas 220 +6.5, Double basses 61 +6.2 and 259 +5.6, Flute
# 1 112 / 113.5 / 200 +5.2..5.5): shapes fitted on the simulated stems (cycles/c55/actor_scripts/notchfit55.py,
# cycles/c55/notchfit.txt), added to any row already at the onset
if "t" in _C55 and __import__("os").path.exists(f"{BUILD}/join_notch_fits_c55.json"):
    for _t, _d in __import__("json").load(open(f"{BUILD}/join_notch_fits_c55.json")).items():
        for _k, _v in _d.items():
            _o = JOIN_NOTCH_S.setdefault(_t, {}).get(float(_k))
            JOIN_NOTCH_S[_t][float(_k)] = _v if _o is None else ((_o if isinstance(_o, list) and (not _o or isinstance(_o[0], (list, tuple, dict))) else [_o]) + [_v])
# Section 7 (critic A #6): Trombone 1 215.0 (the unaccented eighth B flat 3 of the quotation) had velocity 124 since c41
# (for the slur's transition speed) and a 2-5 kHz attack 9.9 dB over its body, where the other eighths and the accented
# 213 read -1.3..+1.0: back to 112 like 215.5. Checked on a range pass before the render (the c41 dip at the slur
# 214.5 -> 215 and the attack band); MVT2_C55_TBN=124 builds the old value for that comparison
VEL_SET["Trombone 1"][215.0] = int(__import__("os").environ.get("MVT2_C55_TBN", "112"))
# Second pass (the lead's direction update, 2026-11-11: default to removing a per-note row; keep it only if its removal
# causes a fault a listener would hear). build/row_off_c55.json lists the LEVEL_SHAPES_S rows of this file and the
# JOIN_NOTCH_S rows whose removal caused no join hole, soft start, dropout, burst or lost repeat on the simulated stems
# (cycles/c55/actor_scripts/prune55.py; the same test removed rows from early_fills, pitch_trims, note_trims, level_fits)
if "p" not in _C55 and __import__("os").path.exists(f"{BUILD}/row_off_c55.json"):
    _off = __import__("json").load(open(f"{BUILD}/row_off_c55.json"))
    for _t, _qs in _off["rows"].items():
        LEVEL_SHAPES_S[_t] = [r_ for r_ in LEVEL_SHAPES_S.get(_t, []) if not any(abs(float(r_[0]) - q_) < 0.003 for q_ in _qs)]
    for _t, _qs in _off["notches"].items():
        JOIN_NOTCH_S[_t] = {k_: v_ for k_, v_ in JOIN_NOTCH_S.get(_t, {}).items() if not any(abs(float(k_) - q_) < 0.003 for q_ in _qs)}
# and the section levels those rows carried, as slow rows per track and section (build/cell_rows_c55.json, written by
# cycles/c55/actor_scripts/comp55.py from the simulated section levels: [from qn, to qn, dB], 0.25 qn ramps each side)
_CELLF = "cell_rows_c56.json" if __import__("os").path.exists(f"{BUILD}/cell_rows_c56.json") and not __import__("os").environ.get("MVT2_C56_OFF") else "cell_rows_c55.json"   # c56: the refitted section rows
if _CELLF == "cell_rows_c56.json" and __import__("os").path.exists(f"{BUILD}/cell_rows_c57.json") and not __import__("os").environ.get("MVT2_C57_OFF"):
    _CELLF = "cell_rows_c57.json"   # c57: the rows by cause (cycles/c57/actor_scripts/edits57.py, cycles/c57/rows_log.txt)
if "p" not in _C55 and __import__("os").path.exists(f"{BUILD}/{_CELLF}"):
    for _t, _rs in __import__("json").load(open(f"{BUILD}/{_CELLF}")).items():
        LEVEL_SHAPES[_t] = LEVEL_SHAPES.get(_t, []) + [[(a_ - 0.25, 0.0), (a_ + 0.25, d_), (b_ - 0.25, d_), (b_ + 0.25, 0.0)] for a_, b_, d_ in _rs]
    ENV_ROW_CLASS = {**ENV_ROW_CLASS, **{_t: ENV_ROW_CLASS.get(_t, []) + [(a_ - 0.25, b_ + 0.25, "slow", "exact") for a_, b_, d_ in _rs]
                                         for _t, _rs in __import__("json").load(open(f"{BUILD}/{_CELLF}")).items()}}
# ---- Dan's decision, 2026-11-11 16:30Z: "i want to nuke all the volume adjustments per note i think they are very not
# helpful, there has to be other ways to fix our problem". Every per-note layer of the track volume envelope is off:
# the classes level and shape whole (re-bow fills and their levels, early fills, join notches, level fits and
# LEVEL_SHAPES rows that are not slow, pitch and note trims, repeated-note dips, start shapes, accent swells, timpani
# attack lifts, unison boost, harp metric steps, the strings' sostenuto hold). No exceptions. The envelope keeps the slow
# class: roles, hairpin gains, slow rows, the timpani roll rules, the divisi chord cut, the final fade (and the mix's
# dynamic trims). The tables and rows stay in the files (switched, not deleted). MVT2_C55 with "n" builds the state
# before this block (the second pass).
if "n" not in _C55:
    ENV_CLASS = {"slow": "on", "level": "off", "shape": "off"}
    ENV_LAYER = {k_: v_ for k_, v_ in ENV_LAYER.items() if v_ == "off"}
    START_SHAPE_CAP = None
    FILL_PRE_KEEP_SUM = None
    ROLE_NOTE_MIN = 3   # role rows over one or two notes (under 6 s) are per-note levels too: off with the level class
# Instrument side, timpani strokes: the fader lifts on the strokes are off with every other per-note move (+6 dB attack
# lift on the f / ff strokes at 203 and 209.5, +7 on the mp stroke at 172, +2.5 at 277). The felt strokes are velocity
# layered (about 3 dB per 22 steps, Scherzo c15): velocity instead. MVT2_C55_TIMPVEL=0 builds without (range test)
if "n" not in _C55 and __import__("os").environ.get("MVT2_C55_TIMPVEL", "1") == "1":
    VEL_SET["Timpani"] = {**VEL_SET.get("Timpani", {}), 172.0: 100, 203.0: 106, 209.5: 96, 277.0: 88}   # first try 112 / 120 / 120 / 74 came out +4.9 / +3.8 / +4.7 / -1.5 dB against c54 (range passes, timpchk.txt)
# Instrument side, the violas' pizzicato triplets of bars 41-44 (lead section 6, critic C #3): the per-pitch fader trims
# (F sharp 3 +4 dB, B flat 3 +3 dB) are off; velocity +8 / +6 on those 16 notes instead (2 steps per dB), adopted or not
# on the range passes of the session (cycles/c55/pizzchk_v.txt). MVT2_C55_VPIZZ=0 builds without
if "n" not in _C55 and __import__("os").environ.get("MVT2_C55_VPIZZ", "1") == "1":
    VEL_SET["Violas"].update({126.0: 66, 126.3333: 62, 127.0: 67, 127.3333: 63, 128.6667: 42, 129.0: 63, 129.6667: 46, 132.0: 65, 132.3333: 61, 133.0: 61, 133.3333: 65, 133.6667: 61, 135.3333: 64, 136.3333: 64, 137.0: 64, 137.6667: 64})   # second set: +16 (F sharp 3), +12 (B flat 3), -10 (F 4), -4 (F sharp 4); the first (+8 / +6 / -16 / -4) gave +1.2 / +1.0 / -13.3 / -0.7 dB


# ---------- c56 (critics on the c55 render, lead_c56.md; Dan's rule: no per-note track volume move in any form) ----------
# Everything here is on the instrument side (CC11 / CC1, CC7 for printed sudden drops, velocity, row, note lengths and
# gaps, row / region volumes in the Opus state: build/mix.json "row_volume_db", "region_gain_db") or a slow row (three
# notes or more, a section, a fade). MVT2_C56_OFF=1 builds without this block (with tools as of c55 the c55 parts.json).
_C56 = not __import__("os").environ.get("MVT2_C56_OFF")
_c56env = lambda k_, d_="1": __import__("os").environ.get(k_, d_) == "1"
if _C56:
    # 1.2 (critics A #1, C #2): bar 63. c31 split the fall after the sf between CC7 lanes and LEVEL_SHAPES rows that
    # gave the difference back; c55 switched the rows off (class shape) and the CC7 lanes alone made Violins II swell
    # 10-11 dB, Violins I 4-6.5 and the violas 5 inside the printed sf > p. The lanes go (CC7 stays 127 through bar 63);
    # Violins II's tremolo row is 7.5 dB lower in the patch (mix.json row_volume_db: the row is used by its four
    # tremolo notes of bars 63-64 only), the [204, 220] section rows end at 212 (build/cell_rows_c56.json)
    for _t in ("Violins I", "Violins II", "Violas", "Violoncellos"):
        CC7_POINTS[_t] = [p_ for p_ in CC7_POINTS[_t] if not 211.85 <= p_[0] <= 214.6]
    # 1.4 (critic B #3): Oboe 1's phrase heads at velocity 53 on Leg Slur MAX sat 4.8-5.5 dB under their line (heads at
    # 83-91 are level with it): the velocity LEG_VEL_BY_CC gives a wind legato target at this CC11
    # (range pass a1: velocity 86 changed nothing, 0.0 dB at 42 and 54: velocity does not act on this row. The heads take
    # CC11 over the note instead: +14 gave +2.9 / +3.0 dB on pass b1 (0.21 dB per unit), +22 is written)
    CC_SHAPES["Oboe 1"] = [(11, [(q_ - 0.06, 0), (q_ - 0.03, 22), (q_ + l_ - 0.15, 22), (q_ + l_, 0)]) for q_, l_ in ((42.0, 1.5), (54.0, 1.0), (139.0, 1.0), (144.0, 0.96), (188.0, 1.0))]
    # 1.4 (critic C #4): the timpani answer of bars 84-85 (E flat - C - A flat, pp): 88 / 60 / 60 gave -34.9 / -45.0 /
    # -46.0 dB; all three on one stick layer at 72 (the coda section row is refitted after the render)
    VEL_SET["Timpani"] = {**VEL_SET.get("Timpani", {}), 277.0: 72}
    TIMP_VEL = {**TIMP_VEL, 278.5: 72, 279.0: 72}
    # 2.4 (critics A #1, C #2): the basses' pizzicato sf at 212 (about 0.15 dB per velocity step upward, c55)
    VEL_SET["Double basses"] = {**VEL_SET.get("Double basses", {}), 212.0: 118}
    # the violas' pizzicato pitch balance of bars 41-44 is in the patch now (mix.json Violas region_gain_db on
    # "Pizz RRx4"); the c55 velocity offsets come out again (critic B #6)
    for _q in (126.0, 126.3333, 127.0, 127.3333, 128.6667, 129.0, 129.6667, 132.0, 132.3333, 133.0, 133.3333, 133.6667, 135.3333, 136.3333, 137.0, 137.6667):
        VEL_SET["Violas"][_q] = VEL_SET["Violas"][_q] - {66: 16, 62: 12, 67: 16, 63: 12, 42: -10, 46: -4, 65: 16, 61: 12, 64: 16}[VEL_SET["Violas"][_q]]
    # 2.4 / 1.2: the sf itself. With the fall out of CC7 the tremolo chord's head came 4-6 dB under c54 (simulated on the
    # c55 stems: Violins I -27.1, Violins II -28.1, Violoncellos -28.4 dB over 212.0-212.5; c54 -21.7 / -21.9 / -23.6).
    # The head's weight is the tremolo row's own volume in the patch (mix.json row_volume_db "Tremolo": Violins I +5.5,
    # Violoncellos +4.8, Violins II -1.5; the row plays only the two tremolo notes 212 and 216 on these tracks), and the
    # printed sf > p takes it back before the hall: CC7 127 over the head, down by the same amount (Violins II 6 dB) in
    # a straight dB line from 212.15 to 212.75, held to the end of the tremolo (CC11 carries the printed diminuendo)
    def _c56_sf_cc7(db_, q_end_):
        pts_ = [(212.15, 127)]
        k_ = 1
        while 212.15 + k_ * 0.03125 < 212.75:
            pts_.append((round(212.15 + k_ * 0.03125, 4), int(round(127 * 10 ** (-db_ * (k_ * 0.03125 / 0.6) / 20))))); k_ += 1
        return pts_ + [(212.75, int(round(127 * 10 ** (-db_ / 20)))), (q_end_, 127)]
    for _t, _db, _qe in (("Violins I", 5.5, 218.3), ("Violins II", 6.0, 217.79), ("Violoncellos", 4.8, 217.97)):
        CC7_POINTS[_t] = CC7_POINTS[_t] + _c56_sf_cc7(_db, _qe)
    # range pass b1 (row gains as region volumes): heads -22.0 / -21.1 / -24.1 dB against c54's -21.7 / -21.9 / -23.6, every
    # fall monotonic; Violins I's tail lay 4 dB over c54: its CC7 goes on to -8 dB by 213.0 and back to -5.5 for the p note
    CC7_POINTS["Violins I"] = CC7_POINTS["Violins I"] + [(212.8125, 64), (212.875, 60), (212.9375, 55), (213.0, 51), (215.95, 67)]
    # Flute 1's CC7 dip at its sf (57 from 211.96 to 213.0, c32) was half of a pair with a level shape that is off: out
    CC7_POINTS["Flute 1"] = [p_ for p_ in CC7_POINTS["Flute 1"] if not 211.85 <= p_[0] <= 213.05]
    # Clarinet 1's CC7 dip before 283 (85 over 282.75-283.0): its fill is off, a 9 dB hole before the note (critic A #1)
    CC7_POINTS["Clarinet 1"] = [p_ for p_ in CC7_POINTS["Clarinet 1"] if not 282.5 <= p_[0] <= 283.05]
    # Bass trombone's sf at 212 (critic C #2): CC11 +10 over the head (96 -> 106; under 108, BRIEF item 9)
    CC_SHAPES["Bass trombone"] = [(11, [(211.98, 0), (212.0, 10), (212.3, 10), (212.6, 0)])]
    # 2.5 (critic A #3): Trombone 1's quotation. With the accent swells off every note of the line rested at CC11
    # 105-118 and the two printed accents (213, 218) were no longer its loudest notes. CC11 contrast (level only on the
    # Hollywood Brass KS Masters; CC1 keeps the layer): unaccented notes 96, accent heads 120 for 0.3 s, then 112
    if _c56env("MVT2_C56_TBN"):
        # (owner's note on the finale's accents, 2026-11-11: "a little bit over done" at +2.1 to +4.1 dB: aim for +1.5 to
        # +2.5 dB here, so 104 / 114 / 110 instead of the critic's 96 / 120 / 112)
        # range pass a1 (104 / 114 / 110): 213 +2.7 dB over its pickup, but 218 4.5 dB under the eighth before it; CC11 gave
        # only about 0.1 dB per unit at 104-114 here. Bar 64's eighths 216-217.5 go to 92 and the heads to 124
        CC_SHAPES["Trombone 1"] = [(11, [(212.44, 104), (212.925, 104), (212.9325, 124), (212.995, 124), (213.13, 112), (214.45, 112), (214.46, 104),
                                         (215.94, 104), (215.955, 92), (217.955, 92), (217.9698, 124), (218.03, 124), (218.15, 112), (218.24, 112)], "set")]
        # pass b1: CC11 92 against 104 changed 217 / 217.5 by +0.5 / -0.2 dB: CC11 hardly acts on this patch near the top.
        # The level is on CC1 (the dynamic layers): CC1 -14 over the three unaccented notes 216-217.5
        if _c56env("MVT2_C56_TBN1"):
            # (pass c1: -14 took 4.2 / 9.5 / 7.0 dB off 216 / 217 / 217.5, about 0.6 dB per unit: -4 on 216, -7 on 217-217.5,
            # which puts the eighths 2-3 dB under the accent's head; not rendered as a range pass)
            CC_SHAPES["Trombone 1"].append((1, [(215.94, 0), (215.955, -4), (216.94, -4), (216.9594, -7), (217.955, -7), (217.9698, 0)]))
    # 2.6 (critic C #5): the tops of the two crescendos of the violins' theme (the long F5s at 68 and 80) sat 4-5 dB
    # under the notes around them once the phrase-top layer was off: the top goes into the CC11 lane (+9; 0.47 dB per
    # unit at CC11 60-80), and the lane's dip at 81.06 inside the note is filled. Violins II 47 (G4 between two A flats,
    # 9-12 dB under them): +10 over the note
    if _c56env("MVT2_C56_TOPS"):
        for _t in ("Violins I", "Violins II"):
            CC_SHAPES[_t] = CC_SHAPES.get(_t, []) + [(11, [(67.9, 0), (68.3, 9), (69.6, 9), (70.0, 0)]),
                                                     (11, [(79.9, 0), (80.2, 9), (81.8, 9), (82.0, 0)]),
                                                     (11, [(81.0, 0), (81.0625, 8), (81.15, 4), (81.19, 0)])]
        CC_SHAPES["Violins II"] = CC_SHAPES["Violins II"] + [(11, [(46.79, 0), (46.85, 10), (47.7, 10), (47.75, 0)])]
    # 2.2 (critics A #2, C #3): re-bows of held soft notes (stem dips of 7-12 dB, master dips of 6 dB or more at 11).
    # a) the 5-7 s notes of bars 2-3 under the winds keep one bow
    #    (their points 5.15 / 5.7 / 6.8 / 6.25 are listed REBOW_AT points since c26: taken out of the list)
    if _c56env("MVT2_C56_SKIP23"):
        for _t, _q in (("Violins II", 5.15), ("Violas", 5.7), ("Violoncellos", 6.8), ("Double basses", 6.25)):
            AUTO_REBOW_SKIP[_t] = AUTO_REBOW_SKIP.get(_t, []) + [3.0]
            REBOW_AT[_t] = [q_ for q_ in REBOW_AT[_t] if q_ != _q]
            # (their fitted fills, off since c55, moved to "_removed_c56" in build/rebow_fills.json)
    # c) every soft new bow starts 7 CC11 units over the lane and returns over 0.45 s (0.6 dB per unit on soft strings);
    #    the basses' last three bows of the final chord bumped instead (+4-6 dB at the start): no lift there, and 3 under
    if _c56env("MVT2_C56_LIFT"):
        REBOW_CC_LIFT = {"cc": 7, "s": 0.45, "max_cc": 46, "pre_fall": 4, "pre_s": 0.15, "families": ("string",),
                         "skip": {"Violins II": [223.0], "Violas": [223.0], "Violoncellos": [223.0]}, "skip_tracks": ("Double basses",)}
        # (range pass a1: on the basses the lift and the fall before it made the dips deeper, median 3.8 -> 4.9 dB, 276.05
        # 3.2 -> 10.1, 299.8 3.3 -> 11.1: no lift on the basses)
        # the printed down-bow at 223 starts the diminuendo to niente from above (it was a 6 dB drop, then flat)
        for _t in ("Violins II", "Violas", "Violoncellos"):
            CC_SHAPES[_t] = CC_SHAPES.get(_t, []) + [(11, [(222.99, 0), (223.0, 7), (223.75, 0)])]
        # Violins II's held pp note of bar 65 bloomed 4.4 dB before it
        CC_SHAPES["Violins II"] = CC_SHAPES.get("Violins II", []) + [(11, [(220.5, 0), (222.9, -6), (222.99, -6), (223.0, 0)])]
    # d) a held note that is a fresh entry starts on the re-bow row, so every piece of it is on one row (the Sus MAX
    #    pieces sat 4.5-5 dB under a Leg Slur MAX first piece: Violins I 0 and 292, Violins II 286)
    if _c56env("MVT2_C56_SUS"):
        ART_SPANS["Violins I"] = ART_SPANS.get("Violins I", []) + [{"from": -0.5, "to": 0.5, "art": "Sus MAX"}, {"from": 291.9, "to": 292.1, "art": "Sus MAX"}]
        # (not Violins II 286: with it the printed repeat at 289 left the re-bow path and re-attacked on Leg Slur MAX)
    # the morendo (bar 91) and the final chord on CC11: 33 at 298.3 to 20 at 301 and on to 15 at 303.5 (the lane read
    # 22 at 301 and stayed there; the chord was flat for 4 s and 3 dB over c54)
    for _t in ("Violins I", "Violins II", "Violas", "Violas div", "Violoncellos", "Double basses"):
        CC_SHAPES[_t] = CC_SHAPES.get(_t, []) + [(11, [(298.3, 33), (301.0, 20), (303.5, 15), (303.75, 12), (303.94, 10), (304.0, 10)], "set")]
    # 1.4 (critic A #6): printed repeats that lost their separation with the gap dips: played gap 0.15 s with a CC11 fall
    REP_GAP_AT["Violas"] = {**REP_GAP_AT.get("Violas", {}), 81.0: {"gap_s": 0.21, "fall_cc": 16, "fall_s": 0.12}}
    STR_REP_NEW_BOW["soft_gap_s_at"] = {**STR_REP_NEW_BOW["soft_gap_s_at"], "Violins II div": {**STR_REP_NEW_BOW["soft_gap_s_at"].get("Violins II div", {}), 120.0: 0.15}}   # (the basses' 144 is a "sus_min_s" repeat: REP_GAP_AT dropped its 0.1 qn lead, soft_gap_s_at does not reach it; left as it is)
    # Clarinet 1's motto tail (critics B #5, C #1): the resolution C5 at 292 stood 6 dB over the three notes before it:
    # CC11 -6 over the note (level only on the CL KS Master); the three notes take a phrase role (roles.json)
    CC_SHAPES["Clarinet 1"] = [(11, [(291.85, 0), (292.0, -6), (295.0, -6), (296.0, -2), (296.9, 0)])]
    # b) the exposed held notes doubled on an idle divisi instance of the same section, bow changes interleaved
    #    (Violins I bars 1-3 and the final chord on "Violin I solo" = 1st Violins DIV A; Violins II's final chord on
    #    "Violins II div" = DIV B; the celli's on "Violoncellos div" = DIV A). MVT2_C56_DBL=0 builds without
    if _c56env("MVT2_C56_DBL"):
        # CC7 per span from range pass a1 (sum of the two stems against c54): Violins I bars 1-3 no cut (the Sus MAX first
        # piece is 4.5 dB under the old Leg Slur MAX one), final chord 100; Violins II 90; the celli's copy is 8 dB louder
        # than the section at equal CC7 (36 on the copy)
        TRACK_DOUBLES = {"Violin I solo": {"src": "Violins I", "spans": [(0.0, 9.0), (292.0, 304.0)], "cc7": [127, 100]},
                         "Violins II div": {"src": "Violins II", "spans": [(292.0, 304.0)], "cc7": 90},
                         "Violoncellos div": {"src": "Violoncellos", "spans": [(292.0, 304.0)], "cc7": 90, "cc7_dst": 36}}
        for _t in TRACK_DOUBLES:
            CC_SHAPES[_t] = CC_SHAPES.get(_t, []) + [(11, [(298.3, 33), (301.0, 20), (303.5, 15), (303.75, 12), (303.94, 10), (304.0, 10)], "set")]
    # the celli's counter-melody of bars 71-78: three long notes stood 5-7 dB over c54 once their trims were off (238 E flat 3
    # -34.1 dB against -41.0, 244 A flat 3 -34.7 / -41.3, 253 A flat 3 -34.3 / -38.8; the other long notes within 1.5 dB).
    # Not a pitch matter (250 E flat 3 and 248.5 A flat 3 are level), so no region gain: CC11 -10 / -10 / -9 over each
    # note (0.6 dB per unit at CC11 50, 0.47 at 70)
    if _c56env("MVT2_C56_VCLONG"):
        CC_SHAPES["Violoncellos"] = CC_SHAPES.get("Violoncellos", []) + [
            (11, [(237.85, 0), (237.9, -10), (239.7, -10), (239.85, 0)]), (11, [(243.85, 0), (243.95, -10), (245.6, -10), (245.75, 0)]),
            (11, [(252.85, 0), (252.95, -9), (254.7, -9), (254.85, 0)])]
    # 2.3 (critic A #4), a test build only (MVT2_C56_LEGVEL=1; default off): string legato velocity by dynamic instead of
    # the fixed 124 (EW's demo plays string legato at 57-124, median 92-98; 25 of the 26 transition bursts are at 124)
    if _c56env("MVT2_C56_LEGVEL", "0"):
        LEG_VEL_BY_CC = {**LEG_VEL_BY_CC, "string": ([(22, 84), (46, 90), (72, 98), (114, 108)], 0)}
    # 2.8 (critic A #5.2): fresh soft string entries on the legato rows and Flautando (20 of them 7-12 dB under their
    # body over the first 0.35 s once the early fills were gone): CC11 +8 at the note-on, back to the lane over 0.5 s
    if _c56env("MVT2_C56_ENTRY"):
        SOFT_ENTRY_CC = {"cc": 8, "s": 0.5, "max_cc": 50, "min_s": 0.6, "gap_s": 0.25, "families": ("string",), "rows": ("Leg Slur MAX", "Flautando")}


# ---------- c57 (critics A, B, C on the c56 render, lead_c57.md; Dan's rule: no per-note track volume move in any form) ----------
# Everything here is on the instrument side (bow-split rule, note gaps, leads, CC11 / CC7, velocity, row choice, region
# volumes in the Opus state: build/mix.json) or removes / re-homes slow section rows. MVT2_C57_OFF=1 builds without this
# block (with build/cell_rows_c56.json and the tables of cycles/c57/before/ that gives the c56 parts.json). Table edits:
# cycles/c57/actor_scripts/edits57.py (cell_rows_c57.json, roles.json, mix.json, leg_leads.json, entry_leads.json) and
# gen_cc57.py (build/cc_shapes_c57.json).
_C57 = _C56 and not __import__("os").environ.get("MVT2_C57_OFF")
if _C57:
    # 1.1 a (critic A #1a): fewer bows. The Sus MAX / Leg Slur MAX samples loop only from 1.93 s to 5.90 s (basses 1.81
    # to 5.78 s; read from the patch files), so a bow of up to 5.6 s plays no repeated material and cannot pulse. A held
    # note is split only above 5.6 s. Every bow change of the movement is a listed point (the c46 pins), so the lists
    # change here: single changes of notes of 4.4-5.0 s go (Violins I 205.95 and 264.42, Violins II 165.86 and 263.92,
    # Violas 169.5 and 263.41, Violoncellos 153.37 and 165.29, basses 170.0, Violas div 280.44), the long pedals and the
    # final chord take pieces of 3.1-5.4 s, staggered across the sections by cycles/c57/actor_scripts/rebow_plan57.py
    # (smallest distance between two sections' changes 0.25 s; 31 changes in the final chord where c56 had 43).
    # Violins I keeps its printed bowings at 295 / 298 / 301 and the change at 302.75 (301-304 is 6.3 s at the rit.)
    REBOW_MAX_S, REBOW_SEG_S = 5.6, 5.0
    _c57_rebow = {   # track: (points removed, points added)
        "Violins I": ([2.4, 4.6, 7.35, 205.949, 264.417], [4.38]),
        "Violins II": ([165.86, 263.921, 295.8, 297.6, 300.2, 302.2, 303.4], [295.72, 298.69, 302.08]),
        "Violas": ([169.5, 263.414, 294.1, 296.9, 299.2, 301.5, 303.1], [295.99, 299.11, 302.23]),
        "Violoncellos": ([153.366, 165.293, 293.6, 296.3, 298.6, 300.6, 302.35], [295.26, 298.42, 301.68]),
        "Double basses": ([170.003, 221.8, 225.215, 227.775, 230.393, 233.038, 235.659, 273.229, 276.05, 278.351, 282.203, 283.605,
                           294.5, 297.2, 299.8, 302.0, 303.3], [224.5, 229.0, 233.5, 273.16, 276.97, 281.28, 295.47, 299.32, 302.43]),
        "Violoncellos div": ([275.527, 277.599, 279.67, 281.716, 284.141], [278.11, 282.14]),
        "Violas div": ([280.439, 291.7, 295.3, 298.3, 301.25, 302.95], [293.03, 296.26, 299.84, 302.92])}
    for _t, (_rm, _add) in _c57_rebow.items():
        for _q in _rm:
            assert any(abs(q_ - _q) < 1e-6 for q_ in REBOW_AT[_t]), (_t, _q)
        REBOW_AT[_t] = sorted([q_ for q_ in REBOW_AT[_t] if not any(abs(q_ - x_) < 1e-6 for x_ in _rm)] + _add)
    # 1.1 b (critic A #1b; Movement I c59 #8): printed same-pitch repeats on held soft notes are a new bow, not a
    # repeated-note stroke: gap 0.05 s where c49-c56 had 0.12-0.15 s, 0.04 s at the others (their stem dips were 10.9-15.5
    # dB against 6.3-7.4 dB at the 33-50 ms splits)
    STR_REP_NEW_BOW["soft_gap_s_at"] = {"Violins II": {289.0: 0.05, 120.0: 0.05, 51.0: 0.04, 112.0: 0.04, 144.0: 0.04, 292.0: 0.04},
                                        "Violas": {271.0: 0.05, 50.0: 0.04, 62.0: 0.04, 71.0: 0.04, 283.0: 0.04},
                                        "Violas div": {70.0: 0.04, 79.0: 0.04, 289.0: 0.04},
                                        "Violins II div": {120.0: 0.05, 114.0: 0.04, 116.0: 0.04, 119.0: 0.04}}
    # 1.1 c (critic A #1c): the re-bow lift is held 0.30 s (the lowest level of a Sus MAX bow change comes 0.1-0.6 s
    # after it), returns over 0.55 s, and has no fall before the change (the fall added about 2 dB to the dip)
    REBOW_CC_LIFT = {"cc": 8, "hold": 0.30, "s": 0.55, "max_cc": 46, "pre_fall": 0, "families": ("string",),
                     "skip": {"Violins II": [223.0], "Violas": [223.0], "Violoncellos": [223.0]}, "skip_tracks": ("Double basses",)}
    # 1.1 d (critic A #1d): Violins II's double starts at 286, so the printed repeats at 289 and 292 fall inside it
    # 1.2 (critic B #4): CC7 of the doubled pairs. Violins I pair's first bow of the final chord at 127 (it entered
    # 3.8 dB under c54), Violins II pair at 115 from 286 (-3.4 / -1.4 / -2.9 dB under c54 over 286-293.5), the celli at
    # 113 / 45 (-2.1 dB); the lanes below take them down again
    TRACK_DOUBLES["Violin I solo"]["cc7"] = [127, 127]
    TRACK_DOUBLES["Violins II div"].update({"spans": [(286.0, 304.0)], "cc7": 115, "cc7_dst": 68})
    # (the copy at 68 over 286-292: Violins II's own envelope is 4.5 dB lower there than in the final chord (its role
    # [286, 292, -2] and the trims), the copy's is flat; at equal CC7 the copy would lead the pair by 4.5 dB and the pair
    # would stand 2-3 dB over c54. The copy's CC7 rises with Violins II's envelope over 291.4-293.6)
    TRACK_DOUBLES["Violoncellos div"].update({"cc7": 113, "cc7_dst": 45})
    # 1.2 (critics B #4, C #1): the morendo and the final chord. Measured per half beat on the c56 stems against c54
    # (cycles/c57/actor_scripts/coda57.py): from 300.5 the Violins I pair lay 3-5 dB over c54, the Violins II pair 2.7
    # from 298, the celli pair 2.4-4.6 from 300.5, the basses 2 dB from 298.5 and 4-6.6 dB from 300.5 (the loudest stem
    # of the chord), Clarinet 2 1-3 dB from 298.5. CC11 does not carry a fall down there (13 units took 0.9 dB off
    # Violins I's printed decrescendo; basses 0.18 dB per unit at 34-17), so the fall is on CC7 (linear amplitude, before
    # the hall), and the CC11 lanes take critic C's values on top.
    _c57_c11 = [(298.3, 33), (301.0, 17), (303.5, 12), (303.75, 10), (303.94, 8), (304.0, 8)]
    for _t in ("Violins I", "Violins II", "Violoncellos", "Violin I solo", "Violins II div", "Violoncellos div"):
        CC_SHAPES[_t] = [it_ for it_ in CC_SHAPES[_t] if not (len(it_) > 2 and it_[2] == "set" and it_[0] == 11 and it_[1][0][0] == 298.3)] + [(11, _c57_c11, "set")]
    CC_SHAPES["Double basses"] = [it_ for it_ in CC_SHAPES["Double basses"] if not (len(it_) > 2 and it_[2] == "set" and it_[0] == 11 and it_[1][0][0] == 298.3)] \
        + [(11, [(298.3, 33), (300.4, 22), (301.0, 13), (303.5, 10), (303.75, 9), (303.94, 8), (304.0, 8)], "set")]
    CC_SHAPES["Clarinet 2"] = CC_SHAPES.get("Clarinet 2", []) + [(11, [(298.3, 0), (300.5, -5), (303.9, -5), (304.0, -5)])]   # -5, not -8: Movement I got -9.5 dB for a -5 dB CC11 offset on Clarinet 1
    for _t in ("Violins I", "Violin I solo"):     # 127 over the first bow, 100 (c56) from 295.2, -2.5 dB from 300.4
        CC_SHAPES[_t] = CC_SHAPES[_t] + [(7, [(294.6, 127), (295.2, 100), (299.8, 100), (300.4, 75), (304.0, 75)], "set")]
    # Violins II pair: 115 to 295.6, 90 (c56) from 296.2, -2.5 dB from 298.6
    CC_SHAPES["Violins II"] = CC_SHAPES["Violins II"] + [(7, [(295.6, 115), (296.2, 90), (298.0, 90), (298.6, 68), (304.0, 68)], "set")]
    CC_SHAPES["Violins II div"] = CC_SHAPES["Violins II div"] + [(7, [(291.4, 68), (293.6, 115), (295.6, 115), (296.2, 90), (298.0, 90), (298.6, 68), (304.0, 68)], "set")]
    CC_SHAPES["Violoncellos"] = CC_SHAPES["Violoncellos"] + [(7, [(300.0, 113), (300.6, 68), (304.0, 68)], "set")]      # 90 (c56) would leave +3 dB
    CC_SHAPES["Violoncellos div"] = CC_SHAPES["Violoncellos div"] + [(7, [(300.0, 45), (300.6, 27), (304.0, 27)], "set")]
    CC_SHAPES["Double basses"] = CC_SHAPES["Double basses"] + [(7, [(298.3, 127), (298.6, 101), (300.2, 101), (300.6, 80), (304.0, 80)], "set")]
    # 1.3 (critic B #1; finale technique 72): the timpani's whole volume envelope is folded into its CC7 lane (track
    # gain +10 dB in mix.json), so a roll's level and the stroke after it switch together (the envelope fell 11 dB
    # 120 ms before CC7 rose 8 dB at 172: a hole before the stroke). Its six section rows (one to three notes each) are
    # per-note levels in the lane ("note_db"); the envelope keeps four levels that change in rests of 6 qn or more
    # ("keep_db": they keep CC7 at 22-122 instead of 9-127)
    ENV_TO_CC7 = {"Timpani": {"ref_db": 10.0,
                              "note_db": [[0, 18, -2.9], [140, 172, -4.6], [172, 204, 1.8], [204, 220, 4.4], [220, 238, -2.7], [238, 262, 1.0]],
                              "keep_db": [[-4, 190, -8.0], [190, 216, 3.0], [216, 250, -10.0], [250, 274, 2.0]]}}
    # the answer of bars 84-85: 72 / 72 / 72 came out -36.3 / -33.7 / -37.0 dB against c54's -38.9 / -38.5 / -39.7 and
    # uneven (0.2-0.4 dB per velocity step here): c54's 60 / 60 on the second and third, 64 on the first
    VEL_SET["Timpani"] = {**VEL_SET.get("Timpani", {}), 277.0: 64}
    TIMP_VEL = {**TIMP_VEL, 278.5: 60, 279.0: 60}
    # 1.4 (critic A #4): the ff B flat of bar 79 arrived 80 ms late in both violin sections (S +80 / +81 ms at leads of
    # 190 / 150 ms). Not A's +75 ms: at 265 ms the run's last note (A flat 6) is cut to 54 ms, and on this join S moved
    # 87 ms for 40 ms of lead in c53 (150 -> 190 ms: +89 -> +2; 230 ms read -105 on a range pass). Violins I 225 ms (the
    # run note keeps 90 ms), Violins II 190 ms
    assert GROUP_LEAD_AT["Violins I"] == [(261.5, 261.9, 0.08), (262.0, 262.0, 0.19)]
    GROUP_LEAD_AT["Violins I"] = [(261.5, 261.9, 0.08), (262.0, 262.0, 0.225)]
    assert GROUP_LEAD_AT["Violins II"] == [(261.5, 261.9, 0.06), (262.0, 262.0, 0.15)]
    GROUP_LEAD_AT["Violins II"] = [(261.5, 261.9, 0.06), (262.0, 262.0, 0.19)]
    # 1.4 (critic C #3): the bar 47 fp peaked 180-210 ms after the beat (the Sus MAX strokes reach their peak 220-340 ms
    # after the note-on): Violins II and Violas start 140 / 130 ms earlier (entry_leads.json), the basses 290 ms before
    # the beat (their 148 follows a note, so it is a re-attack lead). The CC11 spike moves with each note-on
    REATTACK_LEAD_AT["Double basses"] = {**REATTACK_LEAD_AT.get("Double basses", {}), 148.0: 0.29}
    # (critic A #2's leads for Violas 168 and Violas div 79 are not written: 168 follows a 0.125 qn rest and is neither a
    # fresh entry nor a re-attack for the lead rules, 79 is a re-bow piece; both keep their lift from SOFT_ENTRY_CC / the re-bow lift)
    # 1.4 (critic A #2): the soft-entry lift holds to the score onset + 0.15 s (it fell from the moved note-on, 120-300 ms
    # before the beat) and covers Sus MAX entries (basses 140, the copies' first bows)
    SOFT_ENTRY_CC = {"cc": 8, "hold": 0.15, "s": 0.5, "max_cc": 50, "min_s": 0.6, "gap_s": 0.25, "families": ("string",),
                     "rows": ("Leg Slur MAX", "Flautando", "Sus MAX")}
    # 1.6 (critics A #5, C): Trombone 1. The Sus MAX row (216, 218, 219.5) is 2.5 dB up in the patch (mix.json), so the
    # tenuto 216 is level with the eighths and the accent 218 can stand over its pickup; 213 was +3.4 dB over its pickup:
    # head 124 -> 118, pickup 104 -> 110; the p note 219.5 keeps its level (CC11 -4 under the row gain)
    if _c56env("MVT2_C56_TBN"):
        _tb = CC_SHAPES["Trombone 1"][0]
        assert _tb[1][0] == (212.44, 104) and _tb[1][2] == (212.9325, 124)
        CC_SHAPES["Trombone 1"][0] = (11, [(212.44, 110), (212.925, 110), (212.9325, 118), (212.995, 118)] + list(_tb[1][4:]), "set")
        CC_SHAPES["Trombone 1"].append((11, [(219.36, 0), (219.4, -4), (219.98, -4), (220.0, 0)]))
    # 1.7 (critic C #4): Horn 1's theme, bars 11-12: the crescendo 32-34 arrived flat (-1.7 dB; c54 +4.5): +8 on the
    # printed top (B flat 4, 34), -3 on the note before (0.34 dB per unit at CC11 40-60)
    # (written +4 / -2, half the critic's +8 / -3: Movement I measured +6.5 dB for +8 units on Horn 1 at this CC11, 0.8 dB
    # per unit against the family slope of 0.34 used for the +8; the aim is +2.7 / -1 dB)
    CC_SHAPES["Horn 1"] = CC_SHAPES.get("Horn 1", []) + [(11, [(33.9, 0), (33.915, 4), (34.9, 4), (35.05, 0)]),
                                                        (11, [(31.85, 0), (31.89, -2), (33.9, -2), (33.915, 0)])]
    # 1.7 (critic C #6): bar 62's first half sagged 2.7 dB: Violins I's F6 at 208 (tenuto) on Sus MAX like 210 (its top
    # layer on Leg Slur MAX is weak: 1.2 dB from CC11 88 to 122); the basses' G flat 1 +4 dB in the patch (mix.json)
    ART_SPANS["Violins I"] = ART_SPANS.get("Violins I", []) + [{"from": 207.9, "to": 208.1, "art": "Sus MAX"}]
    # (off the legato row the note lost its 210 ms lead and the chord at 210 its 54 ms: re-attack leads)
    REATTACK_LEAD_AT["Violins I"] = {**REATTACK_LEAD_AT.get("Violins I", {}), 208.0: 0.10, 210.0: 0.054}
    # 2.4 (critic B #6): bar 63 sf head of the Bass trombone (3.5 dB under c54, body level; CC11 gives 0.1 dB per unit up
    # there): CC7 headroom. CC7 90 from the rest before its 204 entry with a +3 dB slow level over the same span (both
    # switch in the rest 203.70-203.86), 127 on the head, a straight fall back to 90 over 212.15-212.75. Not on the
    # Violas (no rest between bar 60 and bar 66 to switch the pair in): their head stays 4.3 dB under c54
    if _c56env("MVT2_C57_SF"):
        CC_SHAPES["Bass trombone"] = CC_SHAPES.get("Bass trombone", []) + [(7, [(203.72, 90), (211.97, 90), (211.98, 127), (212.15, 127), (212.75, 90), (223.99, 90), (224.0, 127)], "set")]
        LEVEL_SHAPES["Bass trombone"] = LEVEL_SHAPES.get("Bass trombone", []) + [[(203.70, 0.0), (203.84, 3.0), (221.0, 3.0), (221.5, 0.0)]]
        ENV_ROW_CLASS = {**ENV_ROW_CLASS, "Bass trombone": ENV_ROW_CLASS.get("Bass trombone", []) + [(203.70, 221.5, "slow", "exact")]}
    # 1.5 / 2.1 / 2.3: the CC11 tables that need note times (build/cc_shapes_c57.json, cycles/c57/actor_scripts/gen_cc57.py):
    # flat offsets that replace one- and two-note section rows, half-size flat lifts on the short slurred notes that sit
    # 2-4.6 dB under their line (critic B #2), notches at the 11 legato transitions that burst (critic A #3)
    _cc57 = __import__("json").load(open(f"{BUILD}/cc_shapes_c57.json"))
    _c57kinds = [k_ for k_ in ("short", "burst") if _c56env("MVT2_C57_" + k_.upper())]
    for _t, _its in _cc57["CC_SHAPES"].items():
        if _c56env("MVT2_C57_ROWCC"):
            CC_SHAPES[_t] = CC_SHAPES.get(_t, []) + [(it_[0], [tuple(x_) for x_ in it_[1]], it_[2]) for it_ in _its]
    for _t, _its in _cc57["CC_SHAPES_S"].items():
        CC_SHAPES_S[_t] = CC_SHAPES_S.get(_t, []) + [(it_[0], it_[1], [tuple(x_) for x_ in it_[2]]) for it_ in _its if it_[3] in _c57kinds]
