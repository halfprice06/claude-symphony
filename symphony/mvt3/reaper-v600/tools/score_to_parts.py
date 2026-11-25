"""Turn the mockup build (mockup.midi + mockup-events.tsv) into per-track part data for REAPER.

Output: parts.json with the tempo map and, per track, notes / keyswitches / CC11 dynamics / CC1 vibrato / CC15 mutes /
CC7 (timpani) in quarter notes from the start of the piece, plus the Opus patch and its starting articulation.
Mix settings (track gain, seat, width, mics, reverb send) live in build/mix.json and are applied by build_reaper.py.

Usage: python score_to_parts.py <build-dir> <ks_maps.json> <out.json>
"""
import collections, json, math, re, sys
import mido

BUILD, KSMAPS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOL = "/Volumes/MAC DRIVE"
S = VOL + "/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/"
W = VOL + "/EW Hollywood Orchestral Woodwinds Diamond/Hollywood Orch Woodwinds Opus Instruments/"
B = VOL + "/EW Hollywood Brass Diamond/Hollywood Brass Opus Instruments/"
H = VOL + "/EW Hollywood Harp Diamond/Hollywood Harp Opus Instruments/"
P = VOL + "/EW Hollywood Orchestral Percussion Diamond/Hollywood Orch Percussion Opus Instruments/"

# track name, source staves, patch file, family, pan (-1..1; superseded by the seat in build/mix.json)
TRACKS = []
# c10 (A #1): notes by score onset: {track: (from qn, to qn, keep inside?)}; Violins I rests while the solo track plays
TRACK_WINDOWS = {}
# mvt1 c13 (critics A #3, C #2): a TRACK_WINDOWS value may also be ([(from qn, to qn), ...], keep inside?): several
# windows on one track (the a2 horn passages are scattered through the movement)


def tw_spans(tn):
    """(list of windows, keep inside?) for a TRACK_WINDOWS entry, either form"""
    w = TRACK_WINDOWS[tn]
    if isinstance(w[0], (list, tuple)):
        return [tuple(x) for x in w[0]], w[1]
    return [(w[0], w[1])], w[2]


def tw_keep(tn, q):
    """True when the note with score onset q stays on track tn under TRACK_WINDOWS"""
    if tn not in TRACK_WINDOWS:
        return True
    wins, ins = tw_spans(tn)
    return any(a - EPS <= q < b - EPS for a, b in wins) == ins


def tw_end(tn, q):
    """end of the window of tn that contains q (or the last window end)"""
    wins, _ = tw_spans(tn)
    return next((b for a, b in wins if a - EPS <= q < b - EPS), max(b for a, b in wins))
# c13 (A #1): {split track: (source track, [(from qn, to qn)], lowest pitch)}: source-staff notes with a score onset in
# a window and a pitch at or above the lowest pitch play on the split track and are removed from the source track. The
# source track still counts them for its divisi level cut (it keeps playing a half section's line on a full-section
# patch). Both answers were two-note Sus MAX chords on the full Celli KS Master: 10-15 dB holes, the slur re-attacked.
# c18 (A #2): the lowest pitch may be "rank": a note goes to the split track when another source note starts with it
# (within 0.01 qn) at a lower pitch (the viola voices cross at 61 and 63, so no pitch threshold separates them)
TRACK_SPLITS = {}

# c02: ff 104 -> 114 and fff 118 -> 124 (the patches' top dynamic layer runs to 127; f -> ff measured only +2.5 LU)
DYN = {"ppp": 22, "pp": 34, "p": 46, "mp": 58, "mf": 72, "f": 88, "ff": 114, "fff": 124, "sf": 100, "sfz": 100, "fp": 46, "sfp": 46}
KS_LEAD = 0.06       # keyswitch lead in quarter notes when there is no rest before the note
# mvt3 c13 (critic A #3): KS_LEAD_S (seconds; None = off, the rule above). With it a keyswitch that is not placed in a
# rest goes KS_LEAD_S before the moved note-on of its note, and not earlier than KS_AFTER_PREV_ON_S after the track's
# previous moved note-on; a keyswitch placed in a rest stays there and is at least KS_LEAD_S before the moved note-on.
# The fixed 0.06 qn (0.03 qn before a led note) gave gaps of 7-21 ms, and 28 of the 35 notes whose level moved 2-7 dB
# between two renders of equal data had such a keyswitch 10-23 ms before their note-on (3.3 % of the long notes after a
# short gap against 0.19 % after a longer one). A keyswitch to a non-legato row that would fall inside a sounding
# legato-row note keeps its KS_LEAD time (or goes just after that note's end), so no note is shortened by KS_LEAD_S
KS_LEAD_S = None
KS_AFTER_PREV_ON_S = 0.005
KS_LEAD_SPANS = {}   # mvt3 c15: see the keyswitch timing loop
LEG_OVERLAP = 0.04   # slurred notes overlap the next by this much so Opus plays a legato transition
HP_STEP = 14         # a hairpin with no target dynamic moves about one dynamic level
HP_STEP_SOFT = 22    # c02: untargeted hairpins starting at mp or softer (14 CC measured a median +2.6 dB)
# mvt1 c09 (A #1): an untargeted hairpin lasting HP_SHORT_S seconds or less (real tempo map; the 1 qn hairpins of a
# slow Lento are not caught) is a nuance, not a change of level: it moves at most HP_STEP_SHORT CC. A short > after a
# long < (the "mdv" return) falls only that far; it no longer undoes the whole swell inside half a beat (Horn 1's
# second theme fell 9-10 dB on the quarter after a 0.27 s >, then surged 12-16 dB on the tenuto)
HP_SHORT_S = 0.6
HP_STEP_SHORT = 6
HP_SHORT_KINDS = ("decresc",)   # short crescendos keep the full step (no lurch was measured on them)
HP_SHORT_RET_QN = 2.0   # an untargeted < starting this many qn after such a short > returns to the crest before it
# c32 (critics B #4a, C #2): swells inside one printed dynamic. v621 writes many short untargeted < > inside a printed
# p or ff; the short-decrescendo clamp beat the messa-di-voce return, the next < went back to the crest, and the line
# ratcheted one level up and stayed there (Violins I ff -> CC 124 held 395-408, p molto cantabile -> CC 72).
# HP_MDV_FIRST: an untargeted > straight after an untargeted < (messa di voce) returns to the <'s start even when short.
# HP_SWELL_CEIL: an untargeted < never goes over the last printed mark + one step (HP_STEP_SOFT from mp or softer,
# HP_STEP louder), nor over "max" unless the printed mark itself is louder.
# HP_LOUD_SWELL_DB: an untargeted < that starts at f - 2 or louder is a swell, not an arrival: this dB gain per family
# (None = the HP_GAIN_DB arrival gain), never chained, no fff hold.
HP_MDV_FIRST = True
# c32 (A #5): a tenuto on a wind/brass slur's first note keeps the slur head (no portato re-tongue, no tenuto gap)
TENUTO_HEAD_LEGATO = True
# c32 (A #5): a same-pitch string note that starts a new slur is not merged into the held note before it (a new bow:
# the slur's next note then joins it as a legato target; merged, it started unled on the slow first-note layer)
MERGE_KEEP_OWN_SLUR = True
STR_MERGE_KEEP_SLUR_START = False   # c32: tried on, changed c30-tuned joins (Vla 80/372/500, Vc 656) and did not join Vc 178
# HP_LONE_RETURN: an untargeted < of at most max_qn with no hairpin or printed mark starting within ret_qn after it
# returns to the printed level (or its own start, if higher) over [stop + ret_qn / 2, stop + ret_qn].
# HOLD_AFTER_KEEP_CRESC_START: a printed mark that starts a crescendo is kept after a decrescendo that was turned
# downward (v621 bar 59: p swells, > into the mf that opens the crescendo to bar 61; the mf was dropped).
HP_LONE_RETURN = {"max_qn": 3.0, "ret_qn": 1.0}
HOLD_AFTER_KEEP_CRESC_START = True
HP_SWELL_CEIL = {"max": 120}
HP_LOUD_SWELL_DB = {"wind": 2.0, "string": 1.5, "brass": 1.0}
SOLO_BOOST = 8       # CC11 added after "solo" texts, and after "cantabile" / "espr." in winds and brass (about +2.5 dB)
SOFT_BOOST = 3       # c02: "espr." / "cantabile" / "dolce" in string sections, "dolce" alone in winds
LEG_VEL_STRONG = {"string": (124, 124), "brass": (124, 124)}
# mvt3 c07 (critic A #2): a velocity added to the length-rule legato targets (families not in LEG_VEL_STRONG) at or above
# a dynamic-lane value {track/family: (min_cc, add)}
LEG_VEL_DYN_ADD = {}
# mvt3 c07 (critic A #2, EW research: legato overlaps 45-80 ms strings, 33-58 ms winds / brass): a floor in seconds for
# the overlap of a legato note into its (moved) target {family: s}; LEG_OVERLAP (qn) stays the minimum
LEG_OVERLAP_MIN_S = {}   # c03: legato-target velocity (<0.9 s, longer); v120 was 25-80 ms faster than v105
# c07 (C #3b): brass long notes 112 -> 124 (Hn1 at v112 crossed at +0.16..+0.31 s in the climb to bar 61; v124 median +0.028)
# c03 (A #2, C #1): legato transitions arrive 190-290 ms after the MIDI onset in strings and horns (deterministic); legato
# targets start this many seconds early (instrument name first, then family). The crossover marks the middle of the
# transition, so the aim is a measured crossover of about 80-110 ms.
# c04 (A #5): cor anglais 0.08 s, flutes and clarinets 0.03 s (woodwind crossovers measured 90-160 ms)
# c07 (C #3a): Violins II and Violas 0.20 (median crossover +0.063 s against Vln I's +0.013 at the same lead). by_name
# matches by substring, so there is deliberately no "Violins I" key (it would also match "Violins II").
# c11 (C #4): Violin I solo (DIV A patch) 0.12: at 0.17 its crossovers were median -0.027 s, up to 0.10 s early
LEG_LEAD_S = {"Violin I solo": 0.12, "Violins II": 0.20, "Violas": 0.20, "string": 0.17, "brass": 0.10,"Oboe": 0.06, "Bassoon": 0.06, "Bass clarinet": 0.05, "Cor anglais": 0.08,
              "Flute": 0.03, "Clarinet": 0.03, "wind": 0.0}
# c03 (C #5): soft sustained entries bloom in 300-800 ms (repeatable, so sample attack): start them early, in seconds,
# by family: (CC11 <= 50, louder)
ENTRY_LEAD_S = {"string": (0.12, 0.06), "brass": (0.10, 0.05), "Bassoon": (0.06, 0.06), "Contrabassoon": (0.06, 0.06)}
# mvt1 c03 (critic C #2): extra entry lead (s) by articulation, added to the family's entry lead (same rest test and
# CC11 pull). After a rest, wind first notes on Leg Slur MAX reached -6 dB +0.150 s after the score (n=24), "Leg Slur"
# (clarinets) +0.145, "Sus Non Vib" +0.113, wind Sus MAX +0.055, brass Leg Slur MAX +0.115 against brass Sus +0.005:
# doubled pickups flammed against the violins. Bassoons keep their own measured entry lead (no extra)
ENTRY_LEAD_ART_S = {"wind": {"Leg Slur MAX": 0.11, "Leg Slur": 0.11, "Sus Non Vib": 0.07}, "brass": {"Leg Slur MAX": 0.06},
                    "Bassoon": {}, "Contrabassoon": {}}
GRACE_S = 0.09       # c03 (C #2): after-grace notes, each this long, ending on the main note they lead to
TENUTO_BUMP, ACCENT_BUMP = 5, 8
TIMP_VEL = {}
TIMP_HP_DB_FACTOR = 1.0     # c13 (A #3): share of the CC7 shortfall in roll hairpins made up in the volume envelope
# mvt1 c12 (critic A #1): CC1 for the felt timpani rolls (dynamic layers V1-V8 of the Rls row). Empty = no CC1 lane.
# TIMP_ROLL_TRIM_DB: [(cc, dB)] level trims on rolls by printed dynamic (empty = none)
TIMP_CC1_MAP = []
# mvt1 c12 (critic A #2): tongued (unslurred) wind/brass note changes get a short gap: {"gap_s", "frac", "by": {family:
# {...}}}; None = off
WIND_DETACH = None
TIMP_CC1_PAD_QN = 0.02
TIMP_ROLL_TRIM_DB = []
TIMP_DELAY_S = 0.06   # mvt1 c03 (critic C #3): see build_track (struck notes start this late; others reach -6 dB late)
# mvt1 c37 (critic A #4, MANUAL-GAPS #10): TIMP_RH_ALT = {"max_gap_s": s, "add": 24}: in a run of single strokes (the
# "Lng" row) on one pitch, each no more than max_gap_s after the previous stroke, every second stroke is sent at pitch +
# add, the right-hand samples of the Timpani Flt KS (RH Lng regions at MIDI 60-81 play the LH pitch 24 below; read from
# the .oib); each run starts on the left hand. Sent at the written pitch only, the same-pitch eighths alternated two
# takes (level steps +-1.4..3.2 dB, spectra correlating 0.985-0.999; c36). parts.json `timp_rh`. None = off
TIMP_RH_ALT = None
TIMP_LOUD_ATTACK_DB = 6.0   # c10 (B #2): f/ff timpani attacks measured 8-13 dB under the mix in 50-250 Hz   # c03 (B #1): two pp strokes measured about 6 dB under the one at qn 277
EPS = 1e-6
# c04 (C #6): breaths before the two tutti arrivals take time: seconds added in the 0.25 qn before the breath
CAESURA = {}
CAESURA_BREATH_QN = 0.12   # c19 (C #2): loud wind/brass breath gap where the breath has a CAESURA
ARP_S = (0.040, 0.030)   # c04 (A #1): harp roll, seconds between notes (mp or softer, louder)
TREM_LEAD_S = 0.05       # c04 (A #3): tremolo after a sounding note on another articulation
# c04: both A #3 timing changes are OFF. Rendered twice (c04 pass2 and a third render), the tenuto crossfade plus the
# tremolo lead put a 0.4-0.5 qn hole (-15 to -25 dB) into Vln I/II and Vc on the bar 63 downbeat: the tremolo sounded
# about 0.5 s late. With both off the timing is c03's (old note ends 0.06 qn early, keyswitch there, tremolo on the beat),
# which measured the Vln II sf peak 0.06 qn after the beat. The sf CC shape (+8 from f, held 0.25 qn) stays.
TREM_TIMING_C04 = False
# c06 (A #1, B #4): a silent pre-roll before qn 0 in REAPER (build_reaper.py shifts everything by it, render_cycle.py cuts
# it off the render). Opus dropped notes and controllers on the first block of an offline render (Horn 3's opening note
# in c05, Vln II and Vla in c04). parts.json stays on score time; the pre-roll is 3 qn at PREROLL_BPM (3.0 s exactly).
PREROLL_QN, PREROLL_BPM = 3.0, 60.0
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
LEG_CAP_FRAC = {}
# mvt1 c21 (critic A #3): {track: s}: a legato target never starts closer than this to the previous note's moved onset
LEG_MIN_GAP_S = {}
# mvt1 c21 (critic A #4): cap of a listed run-target lead (leg_leads.json on a fast_leg / Slur Runs note), as a fraction of
# the previous note's length
FAST_LEG_LEAD_CAP = 0.75
# c11 (C #3): build/leg_leads.json {track: {score onset: s}}: per-onset legato lead offsets (may be negative); the total
# legato lead is clamped to LEG_LEAD_CLAMP
LEG_LEAD_CLAMP = (0.03, 0.35)
# c15 (C #1): soft legato targets of the Flute 1 theme (CC11 at the target <= 50) crossed at a median +0.093 s against
# +0.03 at louder levels (the flute solo of bars 37-44 changed notes 0.1-0.23 s after the pizz./harp beats under it):
# {track: (CC11 at or below, extra s)}
LEG_SOFT_EXTRA_S = {"Flute 1": (50, 0.06)}
# mvt1 c37 (critic C #1.3): extra legato lead by target velocity, {track or family: (velocity at or below, extra s)}
# (by_name: track keys first). The HO LegatoSpeed script starts a soft-velocity transition later (HO manual p.144;
# the wind KS Masters keep the printed dynamic's velocity): wind targets at v70 or less crossed +0.066 s (slow tempo) /
# +0.058 (fast) against about +0.01 above, bass clarinet +0.148 against +0.047 (c36)
LEG_VEL_EXTRA_S = {}
# c15 (C #2): per-articulation extra legato lead, exact track names. Leg Slur MAX crossed 0.05-0.08 s later than Leg BC
# MAX on the same lead (Vln II +0.063 / -0.017, Vla +0.043 / -0.007, Vc +0.068 / -0.007)
LEG_ART_EXTRA_S = {"Violins II": {"Leg Slur MAX": 0.04, "Leg BC MAX": -0.03},
                   "Violoncellos": {"Leg Slur MAX": 0.05},
                   "Violas": {"Leg Slur MAX": 0.025}}
# c06 (C #1): dB gain ramped across every crescendo to f or louder (CC11 moves only ~1.2 dB per 10 CC above CC 88)
HP_GAIN_DB = {"wind": 4.0, "string": 3.0, "brass": 2.0}
# c11 (B #3): crescendos that arrive on a printed mf (not f) get this dB ramp, same hold and release (the p/mp -> mf
# arch of bars 23-28 measured flat: the soft-trim taper took 1.7-2 dB off a 14 CC crescendo)
HP_GAIN_MF_DB = {"wind": 2.0, "string": 2.0, "brass": 1.0}
# mvt3 c22 (critic C #3a): {hairpin start qn: {family or track: dB}}: the arrival gain of the crescendo hairpins that start
# there (a long printed crescendo into a final fff whose instruments already sit in their top layer)
HP_GAIN_AT_DB = {}
HP_REL = 1.0
HP_REL_MAX_DB_S = None   # mvt3 c18: dB per second, the fastest release of a hairpin gain (None: HP_REL as written)
HP_END_AT_TARGET = None   # mvt3 c25: see build_track (a crescendo's dB gain gone by the printed mark it ends on)
# c06 (C #5): long-note swell in dB on top of the CC11 swell (+1.5 dB at 40%, 0 at 80%; -1.5 at the end of a phrase)
SWELL_DB = 1.5
# mvt3 c07 (critics C #1-#2 and A #2 of cycles/c06; EW research batches 2-4: a CC swell after the phrase start, an arch,
# a taper over the last second). PHRASE_SHAPE = None (off) or {"families", "min_s" (phrase length), "gap_s" (a played gap
# that ends a phrase), "start" (offset at the first onset), "rise" [(s after the onset, offset)], "peak" (offset, share of
# the phrase, kept in [0.33, 0.62]), "pre_end" (s before the last note-off, offset), "end" (offset at the note-off),
# "scale" {dynamic: factor} (by the printed level at each point), "floor" (lowest CC), "cap" {family: highest CC},
# "hp_fade_s" (the shape fades out this long before a printed hairpin / fp / sfp and back after it), "step_s" (point
# spacing)}, in dynamic-lane units (CC11, or CC1 on CC1_DYN_TRACKS), added to the printed level. A phrase is a run of
# notes with played gaps under gap_s, broken at breath marks. No taper where the last note is an accent or a crescendo's
# arrival. Inside a shaped phrase the per-note "swell" / "swell_taper" / "taper" contours (and their SWELL_DB rows) are
# dropped. parts.json `phrase_shapes` [[start, end]]
PHRASE_SHAPE = None
# mvt3 c07 (research batch 5 item 3): HP_CURVE = None (linear hairpins) or {"cresc": (share of the hairpin, share of
# the rise reached there), "decresc_last": share of the fall reached at the hairpin's last onset (the rest falls on that
# last held note), "min_qn": shortest hairpin shaped, "skip_staves" (mvt3 c09): staves kept linear (timpani rolls: Movement I
# c51, a curved roll hairpin rose up to 8 dB over a mp solo), "decresc_last_max_qn" / "decresc_last_min_s" (mvt3 c14):
# diminuendos longer than max_qn stay linear; a last onset less than min_s before the hairpin's end is not used}
HP_CURVE = None
# c06 (C #6): fixed velocities {track: {score onset: velocity}}
# c09 (A #5): Tbn1 218 105 -> 110 (+0.5 dB over its neighbours at v105; v118 with ACCENT_DB 3 measured +8)
# c10 (B #3, C #2): Tbn1 212.5/213 121 -> 108/105 (peaks 19-21 dB over their body; the master's loudest samples)
# c10 (C #5): the coda pp arrival at qn 286 (Vc/Vla/Cb v41-53 Leg Slur re-attacks decayed 5-11 dB) at v60
# c14 (A #1): the Marc Lng notes of Tbn1's marcato line fall from v106 to v94 (the c06 note trims -1..-2.5 dB that made
# this fall ramped in over each note and are removed)
VEL_SET = {}
# c08 (C #5 interim): no CC11 SOLO_BOOST on these tracks' "solo" texts (Vln I bars 17-22 is a 16-player section; the boost
# put it 6 dB over the oboe it answers); CC1 +SOLO_VIB instead over the span (narrower, vibrato-led)
SOLO_NO_BOOST, SOLO_VIB = ("Violins I",), 10
# c32 (B #5a): texts that never end a solo/espr./dolce boost span (any other text does)
BOOST_STOP_SKIP = ("breathe",)
# c08 (A #2): Violas' soft short slur-to-slur joins stay on Leg Slur MAX (Leg BC MAX dipped 8-9 dB there against 4-5 dB
# inside a slur) with an 8 CC bow-change notch: target shorter than this many seconds, CC11 at or below p + 6
# c13 (A #2): notch 8 -> 4 and notch_soft 6 -> 3: the sample's own bow-change sag (about 4.4 dB in the celli) marks the
# bow change; the plan's notch, taper and bloomv stacked a further 2.4-5.2 dB dip on the same instant
VLA_BC_SOFT = {"max_s": 0.8, "max_cc": 46 + 6, "notch": 4}
# c11 (A #1): the rule above for Violins II, Violas and Violoncellos at any length (soft Leg BC MAX targets with the
# BCSOFT dip measured 7.5-10 dB holes about 0.5 s long; Leg BC MAX soft joins median 5.2-5.8 dB against 3.4 on Leg Slur);
# notch 6 CC where CC11 <= 40 (about 0.57 dB per CC there), else VLA_BC_SOFT's 8
BC_SOFT = {"tracks": ("Violins II", "Violas", "Violoncellos"), "max_s": 99.0, "max_cc": 46 + 6, "notch_soft": 3,
           "soft_cc": 40}
# c12 (A #2): joins (target score onsets) that measured at least 1.5 dB better on Leg BC MAX in c10 than on the BC_SOFT
# Leg Slur MAX join in c11 stay Leg BC MAX (BCSOFT depth stays 0)
BC_SOFT_SKIP = {}
# c08 (C #4): from this qn on, soft (CC11 <= 40) string legato targets do not take the v124 legato velocity (coda bars
# 87-92 grew 4 dB at qn 292 on Vc/Vla Leg BC v124)
CODA_SOFT = {"from_qn": 280.0, "max_cc": 40, "vel": 90}
# c08 (C #1): arrivals of crescendos to f+ hold their hpgain until the first onset after the arrival note (cap 4 qn), and
# tenuto arrivals at f or louder inside SOSTENUTO_SPANS keep their tenuto bump (minus 1 CC) to the note end
HP_HOLD_CAP = 4.0
HARM_VEL_CUT = 6   # c08 (B #4): harp harmonics 6 velocity under the harp's own dynamic (a soft, distant colour)
# c07 (A #1): "Largamente" bars 61-62 (strings "molto sostenuto"): wind portato (tenuto under a slur) is joined, not
# re-tongued. Inside these spans a slurred tenuto wind note to a new pitch plays Leg Slur (legato target, velocity 100,
# CC11 notch 10); a repeated pitch is re-tongued on Sus with a 0.04 s lead, velocity 100 or more.
SOSTENUTO_SPANS = []
SOST_NOTCH, SOST_VEL, SOST_REP_S = 10, 100, 0.04
SOST_JOIN_LEAD_S = 0.12   # c23 (C #3): lead of a sostenuto legato note joined from a re-tongued Sus note
# c07 (A #2): Sus MAX chords that follow a sounding note without a rest get the soft entry lead (the c06 A #3 rule
# widened from "after a legato note" to "after any note"), on these tracks only (Cb joins measured fine)
DIV_JOIN_TRACKS = ("Violas", "Violoncellos")
# c07 (A #3): soft Leg BC MAX targets (CC11 <= 40, 1.4 s or longer) bump 5-8 dB at +0.3-0.4 s at v124: CC11 dip
# c11 (A #1): depth 7 -> 0. The dip landed inside the transition sag (+0.15..+0.5 s) and deepened it; BC_SOFT now keeps
# those joins on Leg Slur MAX, so this only guards against the dip coming back
BCSOFT = {"depth": 0, "t_in": 0.15, "t_hold": 0.5, "t_out": 0.9, "max_cc": 40, "min_s": 1.4}
ENTRY_CAP_S = 0.30   # c07 (C #2b): cap on family entry lead + entry_leads.json extra
# c09 (A #6): Harp Sus RR per-pitch velocity offsets (bars 53-58 broken chords: B flat 3 4-7 dB under the line, F4 +5 over
# it at one velocity; 0.3-0.6 dB per velocity step); not applied to the top note of a rolled chord
HARP_PITCH_VEL = {58: 12, 57: 7, 60: 5, 63: 5, 65: -8, 66: -4}
# c09 (B #1): a crescendo to f+ whose arrival is followed within HP_CHAIN qn by another crescendo to f+ (no softer mark
# between) keeps its hpgain to the second hairpin, which starts from it (bars 59-60 fell 4-8 dB between the two)
HP_CHAIN = 6.0
# c09 (A #5): accents at f or louder (where CC11 moves ~1.2 dB per 10 CC): +ACCENT_DB in the volume envelope, 30 ms rise,
# held to 0.25 s, gone by 0.5 s
ACCENT_DB = 2.0   # first c09 render: 3 dB gave Tbn1 213 +5.6 dB over the eighths around it
# c11 (A #3): per-onset accent weight in dB with the timpani loud-attack shape (10 ms rise, held 0.12 qn, 0 by 0.3 qn):
# Tbn1's ff marcato pickup measured -1.7 dB attack over its body at v108 (the c10 velocity cut removed the peak and the
# emphasis with it); ACCENT_DB's 0.25 s hold covered half the note, so attack and body rose together
ACCENT_DB_AT = {}
# c21 (A #3): 218 3.0 -> 4.5 (it measured only 1.5 dB over the marcato eighths, which get +5 dB on their attacks)
# c26 (BRIEF item 9; A #2, B #3, C #2): Dan heard Tbn1's bar 63-64 accents as harsh. Measured on c25: the attacks were a
# 2-5 kHz burst (+7..+13 dB over the note's own body) from three things stacked on 40-80 ms: the Sus Accent MAX sample,
# CC11 122 (ff 114 + ACCENT_BUMP 8, the fff layer) and a 10 ms +3..+4.5 dB step. Now: Sus MAX (ACCENT_ART_AT), no CC11
# bump (ACCENT_BUMP_AT), v96/96/92 (VEL_SET) and a swell in seconds with no front edge: 0 at onset - 0.01 qn, full at
# + rise_s, held to + hold_s, 0 by + end_s (ACCENT_SWELL_S_AT), +4.5/+3.0/+6.0 dB (first c26 render with +3.0/+3.0/+2.5:
# 212.5 and 218 sat +1.2 and -1.8 dB against the bodies of the marcato eighths; raised after the render, gain only)
ACCENT_ART_AT = {}
ACCENT_BUMP_AT = {}
ACCENT_SWELL_S_AT = {}
# c26 (BRIEF item 8; A #1, C #1): the final chord (qn 292-304, 18.7 s) held one sample per string section, so each
# section replayed its 3.93-3.97 s sustain loop 4-5 times in step with the others (c25 master 100-300 Hz folded swing
# 4.8 dB, autocorrelation 0.58; stem centroid autocorrelation 0.39-0.63): a synchronized slow bow cycle. REBOW_AT splits
# the held note at these score qn into abutting same-pitch notes (the first ends REBOW_GAP_QN early, the Double basses'
# bar 88 re-bow shape that dipped 3-5 dB with no hole); each new note is a fresh REBOW_ART note at REBOW_VEL with no lead
# and no notch. The points are irregular and staggered across the sections (A's list, segments 1.8-4.6 s), so no
# sample plays much more than one loop and no two sections change bow together. Sus MAX, not Leg Slur MAX: a same-pitch
# re-attack on the legato patch plays its slow first-note layer (c03: 7-15 dB holes)
REBOW_AT = {}
REBOW_GAP_QN, REBOW_VEL, REBOW_ART = 0.03, None, "Sus MAX"   # mvt II c26 used 41 (pp)
# c26: CC11 notches removed where a re-bow now plays the bow change (Vln I's printed bowings 295/298/301; Vln II's
# merged repeats at 289/292, "change bow at will")
# c26 (B #2): Horns 3-4's bar 81 decrescendo has no printed target; HP_STEP (14 CC, 87 -> 74) left the held chord over
# the falling tune (Fl1/Vln I fell 5-9 dB, the horns 0-1 dB; their sum 2.5 dB over Vln I at qn 270.5). The tutti
# arrives at p in bar 82; the chord goes there with it. {staff: {hairpin start qn: dynamic}}
HP_TARGET_AT = {}
# mvt1 c38 (critic A #3): HP_SF_TARGET = {"staves": (...) or None (all), "to": "f", "from_f": "ff"}: an untargeted
# crescendo that ends on an sf/sfz (within 0.25 qn of its end) targets "to", or "from_f" when it starts at f or louder,
# instead of rising one hairpin step. None = off. Printed in the build log (hp_sf_targeted)
HP_SF_TARGET = None
hp_sf_targeted = []
NOTCH_SKIP = {}
# c09 (A #2): role spans that meet (B starts within ROLE_CHAIN qn of A's end) crossfade over [B.a - 0.1, B.a + 0.15]
# instead of ramping A out and B in on their own 0.5 qn ramps (both were at full value at the shared qn)
ROLE_CHAIN = 0.5
# mvt3 c27 (critic C #1, ruling 1; Dan's no-per-note-fader rule): a roles.json edge ramp (start, chained edge or end) that
# overlaps a sounding note of the track is moved into the rest before the note nearest the edge: from max(previous note
# end + 0.002 qn, note-on - max_ramp_qn) to note-on - 0.005 qn, when that rest is min_gap_s or longer. Where there is no
# such rest (a legato join, or the note is held across the edge), the envelope edge moves to the nearest rest within
# carry_qn (before the edge when the level rises, after it when it falls) and CC7 carries the change between that rest
# and the edge (a ramp of carry_ramp_s centred on the edge's note-on; CC7 is 20 log10 in Opus: manual p.64, Finale c26),
# so the level still changes at the edge, inside the instrument. Edges with neither are listed in parts.json
# role_edge_join. None = off
# mvt3 c28: edge_note_qn (a note starting this far after the ramp's end is the edge's note), carry_at_edge_qn (the CC7
# carry ramp sits on the edge's note-on when that note starts within this of the edge, else on the edge's own ramp,
# stretched to carry_rate_db_s inside the held note)
ROLE_EDGE_IN_REST = {"min_gap_s": 0.012, "max_ramp_qn": 0.5, "carry_qn": 16.0, "carry_ramp_s": 0.25,
                     "edge_note_qn": 0.05, "carry_at_edge_qn": 0.5, "carry_rate_db_s": 2.5,
                     "step_at_note_on": True, "step_next_qn": 0.25, "step_held_max_qn": 4.5}
# mvt3 c29: "step_at_note_on" / "step_next_qn": see _edge_fix (a carry that would ramp inside a held note is a step at a
# note-on instead)
# the played note spans the rule reads: the previous run's parts.json (env STP_ROLE_SPANS, default build/parts.json), whose
# notes carry every lead, cut and instr_post change; a track missing there uses an estimate. So after a change of notes
# run score_to_parts.py twice (the second run reads the first run's notes); a ROLE_EDGE_XF window is taken as given
_RS_PATH = __import__("os").environ.get("STP_ROLE_SPANS", f"{BUILD}/parts.json")
try:
    ROLE_SPANS_PREV = {t_["name"]: sorted((n_["qn"], n_["qn"] + n_["dur"]) for n_ in t_["notes"])
                       for t_ in json.load(open(_RS_PATH))["tracks"]} if __import__("os").path.exists(_RS_PATH) else {}
except Exception:
    ROLE_SPANS_PREV = {}
# c10 (C #3): a chained second crescendo to f+ rises by this share of HP_GAIN_DB over the first one's gain (it started
# from it and ended at it: bar 60 was flat or falling in every woodwind, then the winds stepped 8-12 dB at bar 61)
# Winds only: the strings and brass already grew 5-15 dB across bar 60, and a string rise put the bar 61 downbeat 2 dB
# over c09's master peak in simulation
HP_CHAIN_RISE = {"wind": 0.75}
# mvt1 c02 (C #1b): a chained second crescendo that arrives at fff rises by this share instead (bar 159 -> 160: the
# strings and brass got no added gain, so the fff arrived only 2 dB over the ff bar)
HP_CHAIN_RISE_FFF = {"wind": 0.75, "string": 1.0, "brass": 0.5}
# mvt1 c02 (C #1a): an arrival at fff (printed level >= fff - 2) holds its whole hpgain to the track's next printed mark
# or hairpin start after the arrival, at most this many qn, then releases over HP_REL (the HP_HOLD_CAP release one beat
# after the arrival took 3-4 dB off bars 160-161 and bar 123 while they were still marked fff). None: off
FFF_HOLD_CAP = 8.0
# mvt1 c02 (C #3): the untargeted-crescendo look-ahead (c11 nm2) stops at a softer or subito mark
NM2_STOP_SOFT = True
# mvt1 c02 (C #2): an accent swell on a crescendo's arrival note adds only max(0, swell - the hpgain there): the accent is
# weight over the notes around it, and the arrival already carries the crescendo's gain (bar 170: winds +4 + 3.5)
ACCENT_MINUS_HPGAIN = True
# mvt1 c02 (A #1): repeated accented unslurred notes (a hammer-stroke figure) are detached: a note in accent_q whose next
# onset follows without a rest and is also an unslurred accent ends gap_qn early. Strings need a printed down-bow on both notes (a retaken
# bow) and play both on Sus MAX (fresh strokes, no bow-change legato, no legato lead). None: off
# Notes of written length min_len_qn..max_len_qn only (the bars 23-25 syncopated 3-beat wind accents are held notes);
# each ends gap_qn early (kit LEARNINGS 7: 0.25 qn gave a 13 dB break, 0.1 qn none)
DETACH_ACCENTS = {"gap_qn": 0.25, "min_len_qn": 1.0, "max_len_qn": 2.0}
# mvt1 c02 (A #2): an accented unslurred string note whose predecessor abuts it (within 0.06 qn) on Sus MAX, a Stac row
# or Tremolo plays Sus MAX (a fresh stroke): as a disconnected Leg Slur MAX note it sat a median 3.5 dB (up to 10.5)
# under the Sus MAX eighths before it
STR_ACC_AFTER_SUS = True
# c10 (C #4d): string legato targets inside SOSTENUTO_SPANS (v124 Leg BC transitions peaked 17-19 dB over their body)
SOST_STR_LEG_VEL = 108
# c11 (A #4): Leg Port MAX (portamento) on these legato targets {track: {score onset: velocity}}: the one-string leaps of
# the "espr., sul D" phrase (F5 -> B flat 5) and the "sul A" entry (C5 -> F5). First trial on Violins I only; check the
# f0 glide (target 0.08-0.25 s) before adding Vln II 82 / Vc 83
PORT_TARGETS = {}
# c11 (C #6): slurred string short_sus notes (< 0.2 s) at CC11 >= 90 end 0.01 qn before the next onset (no overlap) at
# velocity 100 or more: the overlapped v83 viola sextuplets of bars 59-60 (f, CC 88 and up) measured a median dominance
# share of 0.26
SHORT_SUS_DETACH = {"max_s": 0.2, "min_cc": 86, "gap": 0.01, "vel": 100}
# mvt1 c01 (A #1, test): a slur's short first note (< 0.25 s) whose next note in the slur is this many qn or longer stays
# on Leg Slur MAX with it (None: off, the c03 short_sus rule for every short slurred note)
SHORT_SUS_TO_LONG = 1.0
# mvt1 c03 (critic C #1): a string Sus MAX note of a fast slur (short_sus) that overlaps the next note on a legato row
# makes that note a legato target (lead, legato velocity); across a slur boundary the target plays Leg BC MAX
SHORT_SUS_JOIN = True
# mvt1 c03 (critic A #5, #6): articulation tests over listed spans {track: [{"from", "to" (score qn), "art", optional
# "mark": "staccato" (only notes carrying it), "vel_add" or "vel_by_cc" [(CC, vel), ...], "full_len"}]}
ART_SPANS = {}
# mvt3 c16 (critic C #4): further ART_SPANS keys for a short-row test of repeated strokes: "max_qn" (only notes of this
# written length or less), "unslurred" (only notes outside slurs), "len_frac" (played length = this share of the written
# value), "vel_metric" {"down", "mid", "beat", "off"} (velocity by position in the bar, instead of vel_by_cc) and
# "vel_jit" (a seeded +-n on it)
# c10 (C #4a): share of HP_GAIN_DB held through a SOSTENUTO_SPAN after a crescendo's arrival (full: simulated master peak
# -2.2 dBFS on the bar 62 legato transitions and a 4.9 dB limiter)
SOST_HOLD_SHARE = float(__import__("os").environ.get("SOST_HOLD_SHARE", "0.5"))
# c14 (A #1): a printed "marcato" line: unaccented notes of 1 qn or less inside the span play Marc Lng RRx4 (velocity sets
# the dynamic), 0.75 x their written length; accented notes of 1 qn or more inside it end 0.1 qn early. Tbn1 bars 63-64
# played every unaccented note Sus MAX legato-joined (each started 2-5 dB under the previous note's end, no break)
MARCATO_SPANS = {}
MARC_ART, MARC_LEN, MARC_VEL = "Marc Lng RRx4", 0.75, {114: 104, 88: 96, 72: 88}
# c14 (after the render): the Marc Lng bodies sat 2-3 dB under the c13 Sus MAX notes and their attacks rose over 0.1 s
# with no peak: +MARC_BODY_DB over each note and +MARC_ATTACK_DB more on its attack (10 ms rise, held 0.08 qn, gone by
# 0.25 qn), ending 0.05 qn after the note
MARC_BODY_DB, MARC_ATTACK_DB = 2.0, 3.0
# c15 (A #4): the Marc Lng samples reach their level at +0.08..+0.11 s, so the c14 bump (held 0.08 qn) was mostly over
# before the sample spoke: +MARC_ATTACK_DB from onset + 0.04 s, held to + 0.16 s, gone by + 0.30 s (seconds)
MARC_ATTACK_S = (0.04, 0.16, 0.30)
# c14 (A #2): a timpani roll tied into a short note ends with a stroke on that note (onsets of the tied notes; the MIDI
# merges the tie into the roll). The stroke's CC7 is the roll level + TIMP_TIE_STROKE_DB (40 log10 CC7 scale); the f/ff
# strokes also get TIMP_LOUD_ATTACK_DB. The pp/ppp tied ends (qn 8, 237) are left as rolls (felt strokes below v53 are
# near silent; v53 would stick out of a ppp roll)
TIMP_TIE_STROKES = []
TIMP_TIE_STROKE_DB = 4.0
# c14 (A #3): a test inside one render. Violas' slurred sextuplets of bar 59 on Leg Slur MAX (v127, 0.02 qn overlap, no
# lead, no same-pitch merge); bar 60 stays on Sus MAX as the control (Sus MAX measured a dominance share of 0.24-0.27)
# c14 render: failed (bar 59 own share 0.33 -> 0.03: the legato voice held one pitch per group), so the test is off
FAST_LEG = {}
FAST_LEG_VEL, FAST_LEG_OVERLAP = 127, 0.02
# c14 (C #1): soft hairpins (starting at CC11 66 or lower, no hpgain of their own) in exposed lead lines get a dB ramp:
# crescendos +HP_GAIN_SOFT_DB (a messa di voce holds it to the decrescendo, then releases across it); a lone decrescendo
# -HP_SOFT_DEC_DB. 20 lead-line soft crescendos measured a median +1.7 dB (CC11 moves 0.11-0.19 dB per CC at p), 7 flat
# or falling
HP_GAIN_SOFT_DB = {"wind": 3.0, "string": 3.0, "brass": 3.0}
HP_SOFT_DEC_DB = 2.0
LEAD_SPANS = {}
# c14 (C #4): long notes inside SOSTENUTO_SPANS hold their CC11 swell (+4 after 40%, no fall) and, instead of swell_db,
# rise from 0 at 40% to +SOST_SUSTAIN_DB 0.25 qn before the next moved onset, 0 at it (the bar 61-62 notes decayed
# 2-4 dB each, so the master dipped 2.5-3.7 dB before every change)
SOST_SUSTAIN_DB = 2.5
# c15 (A #1): a swell_sost note followed without a rest by another swell_sost note holds +SOST_SUSTAIN_DB through the
# next onset (to +0.25 qn) and releases to 0 at 40% of the next note, where that note's own ramp starts (the c14 drop to
# 0 at the next moved onset made every bar 61-62 chord swell into the bar line and fall back: median step -1.6 dB)
SOST_HOLD_THROUGH = True
# c20 (C #1): long notes starting inside ARRIVAL_HOLD_SPANS (score qn) take the swell_sost contour (+4 CC by 40%, held, and
# the SOST_SUSTAIN_DB rise into the next note) instead of the swell/taper arc. The bar 78 f arrival (poco allargando, into
# the ff of bar 79) rose to CC 92 and then fell to 83-87, under the printed f (88), inside the arrival bar
ARRIVAL_HOLD_SPANS = []
# c15 (A #5): an A/B test inside one render: Violas' slurred sextuplets of bar 59 on the KS Master's Detache row (key 30,
# one note per bow with a defined attack), velocity DETACHE_VEL, written length + 0.01 qn, no lead; bar 60 stays on Sus
# MAX as the control (Sus MAX own-pitch share 0.29-0.33, Leg Slur MAX 0.03)
# c16: the c15 render failed the test (own share 0.32 = control, pitch takeover later), so the spans are empty (the
# Violas state no longer loads the Detache row: a full rebuild)
DETACHE_SPANS = {}
DETACHE_VEL = 100
# c16 (A #3): an A/B test inside one render: Violas' slurred sextuplets of bar 59 on the KS Master's "Stac Leg BC + Slur +
# Port MAX" row (key 44; the KS version of "Violas Stac Leg Slur + Port MAX", a legato patch with a stac-on-bow attack
# row for short connected notes). Inside each slur the notes overlap by FAST_LEG_OVERLAP (0.02 qn), velocity STACLEG_VEL,
# no lead, no same-pitch merge; bar 60 stays on Sus MAX as the control. Pass: own-pitch share 0.5 or more in bar 59, first
# dominance no later than +0.06 s, bar RMS within 1.5 dB of bar 60
STACLEG_SPANS = {}   # c17: emptied (c16 test failed: share 0.39, bar RMS 3.3 dB under the control)
STACLEG_ART, STACLEG_VEL = "Stac Leg BC + Slur + Port MAX", 110
# c16 (C #4): metric weight on plucked lines: velocity added on the downbeat, on beat 3 of a 4/4 bar ("mid") and on every
# other onset ("weak"), for pizzicato notes and the harp. Not on accents or sf, inside LEAD_SPANS, or on the inner notes of
# a rolled harp chord. The pizz./harp attacks of bars 37-52 measured beat 1 only -0.6..+0.7 dB over the line's mean
# (0.3-0.6 dB per velocity step: about +2..3 dB on the downbeat)
# c17 (A #3, test): in the woodwind KS Masters CC1 is a crossfade between a Non Vib and a Vib layer, not a depth control
# (FL/OB KS Master tables: Vib fades in over CC1 55-64, Non Vib fades out over 64-76; at 77+ only Vib sounds, so the
# proposed cap of 80 would change nothing). 67 keeps Vib at full and Non Vib at about 0.8 amplitude
# c18 (A #1): off. The c17 render: Flute 1's 1.5-4 kHz modulation at bars 61-62 10.5 -> 16.9 dB p95-p5 (irregular, the two
# layers beating), stem +2.2 dB
WIND_VIB_CAP, WIND_VIB_CAP_CC11, WIND_VIB_CAP_S = None, 100, 3.0
# c20 (C #3): metric weight on plucked lines as a level step instead (velocity changes the sample): dB on each onset of a
# pizz. note or a Harp note inside METRIC_SPANS (score qn), at full value on the attack and held to the next onset of the
# track (the c12 pizz. trim shape). "down" = bar's first beat, "mid" = beat 3 of 4/4, "off" = off the quarter-note beat,
# other beats 0. Not on accents/sf or inside LEAD_SPANS. c19 measured downbeat minus the rest of the bar -1.6..+1.3 dB
METRIC_DB = {"down": 1.5, "mid": 0.5, "off": -1.0}
METRIC_SPANS = []
# mvt1 c08 (critics C #5, A #6): METRIC_BOWED {track: [(from qn, to qn)]} puts these steps on unslurred, unaccented
# bowed notes of METRIC_BOWED_MAX_QN or shorter (not REP_SPLIT strokes); METRIC_TIMP_DB on Timpani Flt Lng strokes at
# min_cc or louder ("beat" = beats 2 and 4). Empty = off.
METRIC_BOWED = {}
METRIC_BOWED_DB = {"down": 1.0, "mid": 0.5, "beat": 0.0, "off": -0.5}
METRIC_BOWED_MAX_QN = 0.5
METRIC_BOWED_REP = False   # True: REP_SPLIT strokes take the steps too
# mvt3 c08 (critics A #2, C #4; research batch 7 item 2): METRIC_BOWED_DB_SPANS = {track: [(from qn, to qn, table)]}:
# inside a listed span the track's METRIC_BOWED steps come from this table (same keys as METRIC_BOWED_DB) instead of
# METRIC_BOWED_DB (e.g. a stronger off-beat cut where the Sus MAX bow-direction round robin puts the strong stroke on the
# off-beats). The span must also lie inside a METRIC_BOWED span. parts.json metric_db counts "m_<kind>"
METRIC_BOWED_DB_SPANS = {}
# mvt3 c15 (port of Movement I c54's STEADY_LINE; Dan, 2026-11-10: the string melody "feels choppy"): a line played on
# one row with one lead per class. STEADY_LINE {track: [{"from", "to" (score qn), "art": row, "lead_s": s or {row: s}
# (note-on this long before the score onset), "first_lead_s" (a note after a rest; default lead_s), "tongue_lead_s" (a
# note the previous note is not slurred into), "rep_lead_s" (a same-pitch repeat), "overlap_s" (a slurred note ends this
# long after the next moved note-on), "gap_s" (an unslurred note ends this long before it: a new bow), "rep_gap_s"
# (before a same-pitch note), "min_len_s", optional "vel", "poly": True (chords too), "stacc": True (printed staccatos
# too), "max_len_qn" (longer notes keep their own rows), "rr_reset": True (a CC16 reset before each note after a rest),
# "level_db": {score qn: dB} (a level step per note, volume stage), "level_all": True (mvt3 c15: the "level_db" steps
# also act on the span's notes that are not on the row: the staccato quarters inside the line),
# "at": {score qn: {"art", "lead_s", "end_s" (end relative to the next moved note-on), "vel"}} per-onset rows}]}.
# Monophonic notes in a span that are not staccato, tremolo or pizzicato take the row at the articulation stage and
# their note-on and note end after every other lead rule (the other rules' leads, caps and per-onset tables do not act
# on them). parts.json `steady_line` [[score qn, row, lead s, end minus next note-on s or None]]
STEADY_LINE = {}
# mvt3 c08 (MANUAL-GAPS #6, critic A #2 fallback): RR_RESET_AT = {track: [score qn]}: a round-robin reset inside the music on
# the controller Opus's Preferences.json names (RoundRobinResetCC 16; CC36 is the Repetition script's "Reset RR"), value
# 127, 0.02 qn before the moved onset of the track's first note at that score qn (parts.json lane "cc16").
# mvt3 c13: percussion tracks (build_perc_track) take it too; there a qn without a stroke is sent as given
RR_RESET_AT = {}
RR_RESET_CC = 16
# mvt3 c14 (critic A #4 (b); manual p.145): RR_RESET_ALL_AT = [score qn, ...]: a reset on every pitched track whose family
# is not in RR_RESET_ALL_SKIP, 0.02 qn before the moved onset of the track's first note at or after each listed qn (the
# section starts). The round-robin position inside a section then no longer depends on the data of the sections before
# it, and a range render that starts before the reset plays the takes of the full render. A qn that RR_RESET_AT already
# lists for the track is not doubled
RR_RESET_ALL_AT = []
RR_RESET_ALL_SKIP = ("harp", "harm")
RR_RESET_KS_RESTATE = True   # the row in force is keyswitched again before each RR_RESET_ALL_AT reset that lies in a rest
METRIC_TIMP_DB = {}
METRIC_VEL = {}   # c17: emptied (c16 test failed: lean 0.5-1.2 dB, Cb pizz. std 1.7 -> 3.3); was {"downbeat": 6, "mid": 3, "weak": -3}
# c15 (A #3): Violins II sul tasto (Flautando) chords that follow a Flautando chord without a rest: common tones are held
# as one note (no re-attack), the moving voices start FLAUT_LEAD_S early and the old chord's moving notes end at the new
# score onset + FLAUT_OVERLAP_QN (Flautando is polyphonic, so the overlap is a crossfade). Each half-note change left a
# 7-11 dB trough 0.4-0.55 s after the beat (the sample blooms over about 1.2 s)
FLAUT_JOIN_TRACKS = ("Violins II", "Violins II div")
# c16 (A #2): 0.15 -> 0.45 s and 0.35 -> 0.7 qn: after qn 112/114/120 the pad still troughed 9-11 dB for about 1 s (the new
# voice reaches its body at +1.1-1.3 s; the old one had released by +0.9 s)
FLAUT_LEAD_S, FLAUT_OVERLAP_QN = 0.45, 0.7
# mvt1 c08 (critic A #4): tremolo chords inside TREM_JOIN spans {track: [(from qn, to qn)]} join like FLAUT_JOIN (common
# tones held as one note, moving voices TREM_JOIN_LEAD_S early, old moving notes ending at the new score onset +
# TREM_JOIN_OVERLAP_QN); a held tremolo note longer than TREM_SPLIT["max_s"] is split at the output stage into abutting
# same-pitch tremolo pieces of seeded TREM_SPLIT["seg_s"] seconds that never start within TREM_SPLIT["clear_qn"] of
# another onset or a barline (so no single sample loops, and the pieces do not re-attack in step with the bars)
TREM_JOIN = {}
TREM_JOIN_LEAD_S, TREM_JOIN_OVERLAP_QN = 0.3, 0.4
# mvt1 c09 (critic A #4): seconds of entry lead for a tremolo note that follows a held note on another row with no rest
# (0 = off); the old notes end at the moved start
TREM_ENTRY_LEAD_S = 0.0
TREM_SPLIT = {"max_s": 4.4, "seg_s": (2.5, 3.3), "clear_qn": 0.3, "gap_qn": 0.005}
# c15 (A #6): per-onset breath gap in qn for a note that ends at a printed breath (default 0.3 qn at mf+), plus a CC11
# fall of that many CC over the note's last 0.2 qn (Hn1 qn 195: the 0.28 s gap dipped only 1.9 dB under the release)
BREATH_GAP_AT = {}
BREATH_FALL_CC = {}
# c15 (A #4): an accented note of 1 qn or more inside a MARCATO_SPAN ends this many qn early (default 0.1): Tbn1's dotted
# C4 at 213 ended 0.1 qn early and its release filled the break before 214.5 (no level change at the onset)
MARC_ACC_CUT_AT = {}
# c15 (B #1): unmarked soft swells (< > inside a phrase whose printed peak comes later) that do not get HP_GAIN_SOFT_DB:
# the swell top reached the phrase's printed mp/mf (Horn 1 bar 8 -31.2 against the mp crest -31.6..-32.8 dB)
SWELL_NO_SOFT_GAIN = {}
# c18 (C #1): these swells get a smaller messa di voce instead (checked before SWELL_NO_SOFT_GAIN); HP_SOFT_DEC_AT gives
# per-onset decrescendo depths (Oboe 1's bar 41-42 > sits on a +5 note trim and a +2.5 role: 1.3 dB over 2.5 qn)
# c24 (C #1): 68 removed (the bar 24 swell top stood 1.3 dB under the bar 28 mf crest); 68 falls to SWELL_NO_SOFT_GAIN
SWELL_SOFT_GAIN_AT = {}
SWELL_SOFT_GAIN_DB = 2.5
HP_SOFT_DEC_AT = {}
# c22 (C #1): per-onset soft crescendo gains in lead lines (in place of HP_GAIN_SOFT_DB[family]); these six solo hairpins
# measured -2.1..+2.0 dB (stem, last third minus first third), because note/pitch trims, phrase tops and sample sags
# cancelled the +3 dB ramp (the working solo hairpins measure +4..+10)
# (Violin I solo 48: 6 -> 4.5, because removing its phrase tops (C #1d) adds about 2 dB to the same crescendo)
HP_SOFT_GAIN_AT = {}
# c22 (C #1b): spans that get the lead-line soft hairpin ramp without being LEAD_SPANS (LEAD_SPANS also steers phrase
# tops, metric steps and the tempo apexes, so the bar 54-56 horn/clarinet line is added here only)
HP_SOFT_EXTRA_SPANS = {}
# c22 (C #4): soft hairpins (CC11 66 or lower at the start, no hpgain of their own) outside the lead lines get a smaller
# dB ramp: +HP_GAIN_SOFT_ACC_DB on crescendos (held to the arrival, released over HP_REL; a < > pair as a messa di voce),
# -HP_GAIN_SOFT_ACC_DB on a lone decrescendo. 131 such hairpins changed only through CC11 (0.11-0.19 dB per CC at p:
# 1.3-2.3 dB); simulated phrase-scale movement 1.253 -> 1.306 (references 1.73-2.51)
HP_GAIN_SOFT_ACC_DB = 2.5
# hairpin starts the accompaniment rule skips: the bar 91 morendo has its own _all role ramp held through the fermata
# (the rule's release after the decrescendo made the final ppp chord rise 2.3 dB)
HP_SOFT_ACC_SKIP = []
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
SWELL_CAP_MAX_CC = 40
# c22 (C #2a): an mf-arrival hpgain whose track starts another crescendo within HP_CHAIN qn (no softer mark or
# decrescendo between) holds its gain to that crescendo's start and releases it over HP_MF_BRIDGE_REL qn while the new
# ramp rises (bar 56 -> 57: the strings released the +2 dB mf gain and the Vc cut stepped in, a 5.8 dB sag in 2 beats)
HP_MF_BRIDGE_REL = 1.5
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
JOIN_NOTCH = {}
# c23 (A #4): untied repeated pp notes that wind players re-tongue: the note before ends 0.06 qn early (the legato-repeat
# gap; the 0.03 qn default gap dipped 0-1.4 dB, filled by the release tail and the hall). {track: [score onsets of the repeat]}
# c24 (C #2c): per-onset CC11 depth of a merged-repeat bow-change notch (default 8/10/14 CC). Violoncellos 148: the
# printed mf arrival of the bar 46-47 oboe/cello unison; the 14 CC dip took about 3 dB off the mf downbeat
MERGE_NOTCH_AT = {}
# c26 (C #1 fix 2, scaled): the lower strings' legato crossfade valley 0.6-1.0 s after the 292 chord change. C measured
# 3.4 dB in the string sum with the 292 loop profiles in place (they added -2..-4 dB over it); with the profiles removed
# a simulation on the c25 stems leaves Vla -3.5, Vc -4.5, Cb -5 dB for 0.3 qn; these fills take about half of C's dB
# c24 (B #5): per-onset note-trim ramp in seconds (default 0.6 s): the Oboe 1 entries at 42/54 spoke under the
# re-articulating pp strings for 0.25-0.5 qn because the trim arrived after the strings' attack
# c25 (A #3): old negative trims on crescendo notes become steps (Ob1 190, Cl1 256), Ob1 45 (printed decrescendo) falls
# over 2.1 s, Vc 180 over 1.8 s; (A #1) Cl1 292 +3 over 3 s against the sample's decay; (B #3) Horns a2 261 pickup step.
# Keys are score onsets (n["qn"] before the move), not the moved parts.json qn
NOTE_TRIM_RAMP_S = {}
REP_RETONGUE_AT = {}
# c18 (C #4): phrase-top shaping in lead slurs (see build_track)
PT_MIN_NOTES, PT_DB_PER_ST, PT_CLIP = 4, 0.3, (-1.5, 2.0)
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
# mvt1 c37 (critic C #1.2): "rebow_ok": True also leads into and out of notes that AUTO_REBOW splits (the re-bow
# points are frozen in REBOW_AT since c11, so a lead no longer moves them; the last piece of the note before simply
# ends at the moved onset). The Lento basses' bar changes next to 2-bar re-bowed notes took over +0.09..+0.34 s late
# mvt3 c03 (critic C #3): optional "min_qn": only notes of at least this written length (the hammered short pitch
# changes are in time and must not move)
ABUT_LEAD = {}

# mvt1 c00 (kit LEARNINGS 7, Dan's c24 note): gentle accents by family, from the first build. A loud accent (printed f
# or louder, base CC11 >= f - 4) on these families plays `art` (not the bright accent sample), gets no CC11 bump and no
# extra velocity, and takes its weight from a volume swell in seconds: 0 at the onset, +db at rise_s, held to hold_s,
# 0 by end_s. Softer accents get the same swell at soft_db. Per-onset ACCENT_*_AT entries still override.
# mvt1 c01 (A #3): woodwinds too. On c00 the wind Sus Accent MAX notes (with the +8 CC11 bump and +10 velocity) peaked
# a median +3.2..+6.2 dB over their body in the first 120 ms (p90 up to +9.4) against -2..+1 dB for plain notes, and sat
# +5.7..+8 dB over their unaccented neighbours (target 2-4). "keep_legato": an accent on a note joined inside its slur
# stays on the legato row (an accent under a slur is breath weight, not a new tongued attack) and takes the swell only.
GENTLE_ACCENT = {"brass": {"arts": ("Sus MAX", "Sus Max", "Sus Non Vib MAX", "Sus Vib MAX", "Sus Non Vib"), "db": 4.0,
                           "soft_db": 2.5, "swell_s": (0.07, 0.25, 0.6)},
                 "wind": {"arts": ("Sus MAX", "Sus Max", "Sus Non Vib"), "db": 3.5, "soft_db": 2.0,
                          "swell_s": (0.07, 0.25, 0.6), "keep_legato": True},
                 # mvt1 c02 (A #2): strings too: no +8 CC11 bump into the fff layer (Vln II qn 110: a 10 ms peak 14.5 dB
                 # over the body, 2-5 kHz level with the body) and no +10 velocity; the weight is the swell. The string
                 # branch picks its own articulation (STR_ACC_AFTER_SUS, DETACH_ACCENTS), so "arts" is not used there
                 "string": {"arts": ("Sus MAX",), "db": 3.0, "soft_db": 2.0, "swell_s": (0.07, 0.25, 0.6)}}
# mvt1 c00 (kit LEARNINGS 6, Dan's c24 note): automatic staggered re-bows. A string note longer than REBOW_MAX_S seconds
# (on Sus MAX, or on a legato row when nothing joins out of it) is split into same-pitch REBOW_ART pieces of about
# REBOW_SEG_S seconds; each track gets its own phase and piece length (REBOW_TRACK_JITTER), so sections never change bow
# together. Points listed in REBOW_AT are kept; AUTO_REBOW = False turns the rule off.
AUTO_REBOW, REBOW_MAX_S, REBOW_SEG_S, REBOW_TRACK_JITTER = True, 4.5, 3.1, 0.45
# mvt1 c04 (critic A #1): written-out unslurred repeated string notes in a fast tempo are separate strokes (build_track)
REP_SPLIT = {"max_qn": 1.5, "min_bpm": 100.0, "stac_s": 0.2,
             "stac_vel": [(34, 56), (46, 64), (58, 72), (72, 80), (88, 96), (114, 110), (124, 118)]}
# mvt1 c51 (critic A c51 #1; ported mvt3 c10, critic A #1): optional REP_SPLIT keys "gap_s", "frac", "gap_min_s",
# "gap_min_cc": a REP_SPLIT / STR_SHORT_AFTER_SUS / STR_REP_AFTER_STAC stroke followed by a same-pitch stroke, or an
# unslurred monophonic same-pitch Sus MAX repeat of at most "max_qn" on a patch without Leg BC (the Basses KS Master),
# ends max(gap_min_s, min(gap_s, frac x slot seconds)) before the next onset, where the next onset's printed level is
# gap_min_cc or more. Absent: the c04 ends (0.02 qn on Stac, min(0.04 qn, 10%) on Sus MAX; 0.03 qn on the basses).
# parts.json `rep_split_gaps`
# mvt1 c13 (critic A #1): a measured tremolo (a tremolo value of MEAS_TREM["max_value"] or less: two slashes = 16, one
# = 8) whose subdivision 4/value qn lasts MEAS_TREM["min_s"] seconds or more at the local tempo is written-out repeated
# notes (Adler: a shorthand for repeated detache strokes). The note is expanded at the input stage into abutting
# same-pitch notes of 4/value qn, which then take the REP_SPLIT stroke path. Unmeasured tremolos (32) stay on the
# Tremolo row. {} = off
MEAS_TREM = {"max_value": 16, "min_s": 0.1}
# mvt1 c04 (critic A #3, C #4): long timpani rolls loop (3.3-3.9 s): the colour cycles with the loop even after a level
# profile (centroid autocorrelation 0.7-0.95 at the period). A roll whose score onset is listed in "at" and that lasts
# over "min_s" seconds is split at output into abutting same-pitch roll notes of irregular length (seg_s range, seeded
# per note), velocity +-vel_jit per piece; CC7 and the volume envelope stay those of the whole roll.
TIMP_ROLL_RESTRIKE = {"at": [], "min_s": 6.0, "seg_s": (2.5, 3.3), "vel_jit": 3, "dip_db": -1.5, "dip_s": (0.03, 0.14, 0.22)}
# (c04 render: each new piece rose a mean +2 dB over the roll from +0.02 to +0.18 s; level steps -1.5..+0.8 dB)
# mvt1 c04 (critic A #2): listed slurred tenutos (track: [score qn]) are joined as legato targets on the legato row
# (velocity SOST_VEL, a SOST_NOTCH portato notch, normal legato lead) instead of re-tongued on Sus
PORTATO_JOIN_AT = {}
# mvt1 c09 (A #1): CC11 depth of the portato notch on a joined tenuto, per track (default SOST_NOTCH); a soft dolce horn
# tenuto after a short > lost 6 CC more to the notch than the line needed
PORTATO_JOIN_NOTCH = {}
# mvt1 c09 (C #1): tracks (name prefixes) whose patch crossfades its dynamic layers with CC1, and the CC1 value per printed
# CC11 level (the brass layer tables put pp on the p/pp layer, mf on mp + f, f on f, ff on ff 0.75 + f 0.4, fff on ff);
# CC1_HOLD: constant CC1 per track
CC1_DYN_TRACKS = ()
CC1_DYN_MAP = [(22, 18), (34, 28), (46, 42), (58, 54), (72, 68), (88, 86), (114, 108), (124, 120)]
CC1_HOLD = {}
# mvt1 c04 (critic C #5): an sf listed here is an arrival at this dynamic: the spike reaches it and the level after the
# spike is that dynamic - 8 CC (instead of the current level - 10), so the printed decrescendo carries the fall
SF_ARRIVAL_AT = {}
# re-bow velocity by the printed level (CC11 of the dynamic curve) when REBOW_VEL is None: soft attacks, as a bow change
REBOW_VEL_BY_CC = [(22, 38), (46, 52), (72, 66), (88, 80), (114, 96)]
# mvt1 c03 (critic A #2): the per-track phases alone let sections re-bow together (final chord: five sections within
# 0.34 s at qn 726.4, master dips 2.5-5.2 dB). build/rebow_moves.json {track: {"automatic point (qn, 3 decimals)": new
# qn}} is written by tools/space_rebows.py from parts.json; it moves automatic points so that no two string tracks
# re-bow within REBOW_MIN_SEP_S (pieces kept 1.5 s or longer). The fitted shapes move with their points.
REBOW_MIN_SEP_S = 0.6
# mvt1 c05 (critic A #1): a slurred same-pitch repeat (the last eighth of a slur and the note after it, same pitch, same
# slur, no tie) is merged into one note with a CC11 notch. Strings: the short_sus eighth (Sus MAX) takes the arrival
# note's length, notch SLUR_REP_NOTCH (CC11 up to 90, above 90); winds: a Leg Slur note and its repeat inside the slur
# (no tenuto, no breath), notch WIND_SLUR_REP_NOTCH.
SLUR_REP_MERGE_SUS, SLUR_REP_NOTCH = True, (6, 8)
WIND_SLUR_REP_MERGE, WIND_SLUR_REP_NOTCH = True, 8
# mvt1 c05 (critic A #2): an unslurred, monophonic short string note (under "max_s" seconds on the tempo map without
# caesuras) whose predecessor ends within "abut_qn" of its onset on a non-legato row (Sus MAX, a repeated stroke, Stac,
# Tremolo) is a fresh Sus MAX stroke: on Leg Slur MAX the KS Master played a slow legato transition from the Sus note
# (pitch crossover a median +0.205 s on 22 notes). Velocity REBOW_VEL_BY_CC, the end min(0.04 qn, 10%) early.
STR_SHORT_AFTER_SUS = {"max_s": 0.3, "abut_qn": 0.06}
# mvt1 c05 (critic A #3, test): short_sus notes that are not the first of their slur start SHORT_SUS_LEAD_S early on the
# listed tracks (the previous note's end stays, so the crossfade overlap grows by the lead). Empty: off.
SHORT_SUS_LEAD_S, SHORT_SUS_LEAD_TRACKS = 0.05, ()
# mvt1 c05 (critic C #2): staggered breaths on long held wind/brass notes {track: {score onset: [split qn, ...]}}: the
# note is split at output into abutting same-pitch pieces on its own articulation (the earlier piece ends
# BREATH_SPLIT["gap_qn"] before the split; the new piece at the note's velocity + "dvel"); CC11 continues, and the volume
# envelope dips "dip_db" at the split, gone by "dip_s" seconds, so the re-entry stays under the chord.
BREATH_SPLIT_AT = {}
BREATH_SPLIT = {"gap_qn": 0.05, "dvel": -8, "dip_db": -3.0, "dip_s": 0.4}
# mvt1 c05 (critic A #5): "metà" (half the section) on a string part: single notes until "tutti"/"unis."/"div." are
# played this many dB lower (half the players)
META_DB = -3.0
SOLI_AS_META = True   # mvt3 port (from mvt2 c27): "N soli" on a string part is played like "metà" (one line, half-section cut)
# mvt3 c01 (critic A #4): LAST_DESK_DB = dB (None = off): a string text "last desk" / "last N desks" plays the part this
# many dB lower until "tutti" / "unis." / "ord." (a quarter section or less); chords in such a span keep their divisi cut
LAST_DESK_DB = None
# mvt3 c01 (critic B #2): ROW_GAIN_DB = {track: {row: dB}}: a level offset on every stretch where all of a string
# track's sounding notes play that row (folded into the chord/divisi cut, so it starts 0.1 qn before the stretch). The
# Hollywood Strings Violins I/II "Tremolo" rows play 3-9 dB over Sus MAX at the same CC11 (c00 bodies), and the
# ROW_TRIM_DB rule only trims notes with a Leg-row neighbour
ROW_GAIN_DB = {}
# mvt3 c07 (critic A #3): ROW_VEL_BY_CC = {track: {row: [(CC, vel), ...]}}: printed staccatos that play this row take
# their velocity from the printed level (the row's velocity layers carry the dynamic; EW parks CC high on shorts)
ROW_VEL_BY_CC = {}
# mvt3 c01 (critic A #4): TASTO_CC1 = CC1 value (None = off): string notes inside a "sul tasto" text span (until "ord." /
# "arco") on sections without a Flautando row get this CC1 (the KS Masters' CC1 crossfades Non Vib / Vib / Molto Vib;
# manual p.92: "the Sustain patch in other sections, when played pp with no vibrato (Mod Wheel all the way down),
# achieves a similar sound" to flautando)
TASTO_CC1 = None
# mvt3 c01 (critic A #4): rows whose AUTO_REBOW pieces keep the row instead of REBOW_ART (a Flautando note split at a
# re-bow played its second half on Sus MAX: centroid 568 -> 991 Hz, level -13 dB at the re-bow, Vln II c00 qn 383.3)
REBOW_KEEP_ARTS = ("Flautando",)
# mvt3 c01 (critic A #5): HARM_ON_TRACK = {harp track: semitones}: flageolet notes stay on that track, transposed to their
# sounding pitch, HARM_VEL_CUT under the harp's dynamic (no separate harmonics instance). Default: they need a "harm"
# track and vanish from the harp track
HARM_ON_TRACK = {}
# mvt3 c01 (critic A #5): GLISS_SPANS = {staff: [(a, b, low pitch, high pitch, pitch classes, vel_from, vel_to)]}: a
# printed glissando the event list does not carry, written out as notes from low to high (inclusive) on the listed pitch
# classes, evenly spaced over [a, b), velocity rising vel_from -> vel_to; a note of the staff at a on the low pitch is
# replaced by the run
GLISS_SPANS = {}
# mvt3 c01 (critic A #3): UNI_CHORD_SPLIT: when two or more tracks on one patch play the same chord at once (a shared
# "a2" staff written as octaves), the unison rule splits the chord by pitch (top note to the first such track in TRACKS
# order, the next to the second) instead of keeping the whole chord on one track. On a legato row a kept chord plays
# only one note (Horn 1 Leg Slur MAX at mvt3 qn 996: C4 23 dB under C5)
UNI_CHORD_SPLIT = True
# mvt1 c06 (critic A #1): listed string notes {track: [score qn]} (printed down-bows that LilyPond's line joins as legato,
# e.g. the fff downbeat after a caesura) are fresh Sus MAX strokes: the c06 Leg -> Sus entry path (entry lead, velocity
# 105 or more, the legato note before it cut at the keyswitch); the next note joins from the stroke as a Leg BC MAX
# legato target (as SHORT_SUS_JOIN). On c05 the fff downbeat played a Leg BC transition that sagged 6-7 dB at the beat.
DOWNBOW_STROKE_AT = {}
# mvt1 c06 (critic B #1): an accented note on a GENTLE_ACCENT family plays the velocity of an unaccented note at the same
# printed level plus GENTLE_ACCENT[family]["vel_add"] (LilyPond adds 20 for an accent and 40 for a marcato; the HO
# velocity sets loudness: Horn 1 / Trumpet 1 / Trombone 1 accents measured 3.6-6.1 dB over plain Sus at one dynamic before
# the swell). The plain velocity is the median source velocity of this track's unaccented notes within ACC_PLAIN_WIN qn
# at the same printed level (+-4 CC); without such notes, the source velocity minus the script's extra (capped at 127).
ACC_SRC_EXTRA = {"accent": 20, "marcato": 40}
ACC_PLAIN_WIN = 8.0
# mvt1 c06 (critic A #2): unslurred, untied same-pitch repeats on wind and brass Sus notes are re-tongued audibly: the
# note ends min(gap_s, frac x its length) before the next onset and CC11 falls fall_cc over its last fall_s seconds,
# back at the next onset. On c05 (0.03 qn gap) 197 of 228 such repeats dipped under 3 dB (pedals and repeated chords
# sounded tied). None: off; REP_RETONGUE_AT still lists per-onset exceptions.
WIND_REP_RETONGUE = {"gap_s": 0.06, "frac": 0.25, "fall_cc": 6, "fall_s": 0.12}
WIND_REP_AFTER_SLUR = True   # mvt1 c11: see build_track (a repeat after a slur's last legato note is re-tongued too)
# mvt1 c34 (critic C #4): a slurred same-pitch repeat whose second note has a tenuto (portato on a repeated pitch, e.g.
# a motif "eighth, eighth, tenuto quarter" slurred with the last two on one pitch) is re-tongued like an unslurred
# repeat (WIND_REP_RETONGUE gap and CC11 fall). Before, it took the plain same-pitch gap (0.06 qn, no fall): 12 of 20
# such repeats in mvt1 v621 dipped under 3 dB (the kit's c06 measure: a repeat needs 3-7 dB). False = off.
WIND_REP_PORTATO = False
# mvt1 c34 (critic A #2): a wind/brass tenuto inside a slur, re-tongued on the Sus row (portato), whose next note is in
# the same slur at a new pitch, without a tenuto, on a legato row: the tenuto overlaps that note by LEG_OVERLAP and the
# note is joined from it like a SLUR_START_SUS second note (SOST_JOIN_LEAD_S lead, at most 0.45 of the tenuto, SOST_VEL).
# Before, the tenuto ended 0.03 qn early and the next note started on Leg Slur's slow first-note layer: 30 ms dips of
# 4.3-9.7 dB (median 6.6) at nine such joins, against 2.0 at slurred tenutos joined on the legato row. parts.json
# `portato_tails`. False = off.
PORTATO_TAIL_JOIN = False
# mvt1 c34 (critic A #3a): a DOWNBOW_STROKE_AT stroke at f or louder takes no delayed-vibrato CC1 dip (a phrase start's
# 35-point dip): on the 1st Violins KS Master the Sus Vib set at the start of the dip is far quieter than the Molto Vib
# set, so the c33 272 stroke opened 10 dB under its body. False = the c33 behaviour.
STROKE_NO_VIB_DELAY = True
# mvt1 c34 (critic C #3a): HP_NIENTE = {"steps": n, "rest_qn": r}: an untargeted decrescendo after which the line has
# no note onset for r qn (it ends into a rest) falls n hairpin steps instead of one (no short-hairpin cap, no next-mark
# limit); when the line comes back before any printed mark, the level returns to the one-step value at its next onset,
# so the phrase after the rest is not lowered further. Only wind, brass and string tracks. Measured on mvt1 c33: 37
# such decrescendos fell a median 3.9 dB (17 under 3). None = off.
HP_NIENTE = None
# mvt1 c34 (critic C #3b): HELD_DECRESC_DB = {family: dB}: a decrescendo that lies inside one held note gets a volume
# fall from 0 at the hairpin start + 0.2 s to -dB at its end, held to the next moved onset (then back to 0). The HO
# sustains bloom for 0.3-1 s and cancelled a 6-14 CC fall (mvt1 c33: winds median 1.9 dB, 27% rose; strings 2.1 dB,
# 26% rose). parts.json `held_decresc`. None = off.
HELD_DECRESC_DB = None
HELD_DECRESC_MIN_S = 0.8   # mvt1 c34: shorter decrescendos are left to CC11
HELD_DECRESC_SKIP = {}   # {track: [hairpin start qn]}: hairpins whose level is set by a fitted shape
# mvt3 c08 (critic C #3): HELD_DECRESC_CARRY = {"max_qn": qn}: when the next note after a held decrescendo starts on a
# subito-softer mark or an fp / sfp, the held-decrescendo level is not released at that onset (which stepped twelve
# tracks up by 3-6 dB at bar 219's "sub. p", so the master did not drop) but held to the start of the next crescendo
# hairpin (within max_qn) and released across it. parts.json `held_decresc_carry`. None = off
HELD_DECRESC_CARRY = None
# mvt3 c26 (ruling 1; critics A #5, B #6, C #3): HELD_DECRESC_LED_RELEASE = True: when the next note after a held
# decrescendo is led (its moved onset at or before the hairpin end + 0.01 qn), the -dB ramp ends 0.03 qn before that moved
# onset is reached at that moved onset and released from there over 0.25 s (critic A c26 #5), not 0.01 qn after the
# hairpin end inside the led note (22 fader steps of +2.5..+2.9 dB inside led notes; master +3 dB at 932, +3.3 at 913.9).
# A dict {track/family: release seconds} sets other release times (a note tied on through the onset: about 1.1 s, under
# 3 dB/s). False = the c34 behaviour
HELD_DECRESC_LED_RELEASE = False
# mvt1 c34 (critic B #1): hairpins printed once on a shared staff that the extraction gives to one voice only, or that
# a track needs added: {track: [(start qn, stop qn, "cresc" | "decresc")]}, read by base_points like printed hairpins
SHARED_HP = {}
FP_SPIKE = ("f", 0.12, 0.25)   # mvt1 c11 (A #5): fp = (dynamic of the attack, held to qn, at p by qn)
SFP_SPIKE_HI = "sf"   # mvt3 port: the attack level of an sfp (see FP_SPIKE)
# mvt3 c03 (no WARNING rule): two hairpin shapes that missed a printed mark.
# HP_DIM_RESTATE: a decrescendo whose printed target at its stop equals the current level still falls (c06 C #3), but
# when the track has a note onset at the stop the mark restates the printed level there (Vln mf > mf at bar 75, sf > p
# at bar 138: the new note came in 6 CC under its printed dynamic). False = the c06 behaviour (the mark does not raise).
# HP_SWELL_AT_MARK: a crescendo that starts on a printed mark and whose target equals that level ("ff < > ff",
# "pp < > pp") is a swell above the mark (one untargeted step, short-hairpin and HP_SWELL_CEIL caps), not a
# "niente <" that dropped 12 CC under the printed mark at its start. False = the c06 behaviour
HP_DIM_RESTATE, HP_SWELL_AT_MARK = False, False
ACC_HEAD_JOIN = False   # mvt3 c03 (critic C #1a): see build_track
RAMP_END_CLAMP = False   # mvt3 c03 (critic C #6a): see smooth_tempo
# mvt3 c25 (critic C c25 #2, ruling 5): [(score qn of a roll at a printed arrival, end qn)]: the roll's CC7 (after the
# vol_to_cc7 fold) runs as one dB-linear ramp from the level just before the arrival to the level the track played at the
# last earlier mark equal to the mark printed at the end (or to the lane's own value there). See build_track
TIMP_ARRIVAL_RAMP = []   # mvt3 c26: a row (at, to, cc7_start, cc7_end) gives both ends of the ramp
TIMP_SETTLE_SKIP = []   # mvt3 c03 (critic B #2): score qn of timpani roll chain starts that take no settle (-5 dB)
# mvt3 c03 (critic C #1b): a detached loud short_sus eighth (SHORT_SUS_DETACH) whose next note is a legato-row note of
# the same slur joins it (SHORT_SUS_JOIN: legato target, lead, overlap) instead of ending 0.01 qn before it; the long
# note after slurred eighths was an unled Leg Slur MAX first note, +118 ms late (80 notes). False = off
SHORT_SUS_DETACH_JOIN_LEG = False
FP_CHECK_AT = {}   # mvt3 c03: {fp/sfp mark qn: qn where the curve reaches the printed p} (filled by base_points)
# mvt3 c02 (critic C #3): SFP_SPIKE_S = (hold_s, fall_s): an sfp's attack level is held hold_s seconds and reaches
# DYN["sfp"] fall_s seconds after the mark, on the real tempo map (FP_SPIKE's qn values, fitted on Movement I's slower
# fp, gave 43 ms at 168 qpm: no sf heard). SFP_VEL: the notes starting at an sfp mark take at least this velocity (the
# attack belongs to velocity, manual p.53; they had the p value). None = off
SFP_SPIKE_S, SFP_VEL = None, None
# mvt3 c09 (critic A #1): FP_SPIKE_AT_MARK = True: an fp / sfp attack level starts at the mark (a step at the score onset)
# instead of 0.02 qn after it. Led notes take the CC at their score onset from their moved note-on (pulls), so with the
# ramp every led sfp note started on the p layer and swelled into the sf (c08: 23 of 24 tracks at CC 46 at the note-on)
FP_SPIKE_AT_MARK = False
# mvt3 c09: FP_SPIKE_S = (hold_s, fall_s) for "fp" as SFP_SPIKE_S is for "sfp" (None: FP_SPIKE's qn values); FP_VEL: the
# notes starting at an fp mark take at least this velocity
FP_SPIKE_S, FP_VEL = None, None
# mvt3 c09 (critic B #1): HARP_VEL_MAX: the harp's final velocity is capped here (Harp Sus RR plays a Nail Pick group at
# 124-127, manual p.69; an accented ff chord at v126-127 stood 10 dB over the orchestra). None = no cap
HARP_VEL_MAX = None
# mvt3 c09 (critic A #3): families whose GENTLE_ACCENT swell starts at the moved note-on of a led (non-legato) accent
ACCENT_SWELL_FROM_MOVED = ()
# mvt3 c16 (Dan, 11 Nov: "the volume adjustment was adjusted in large peaks and valleys on so many individual notes";
# critics A / B / C #1). Every volume-envelope item carries the name of the rule that wrote it (vol_parts.rule).
# VOL_PER_NOTE: "on" (every rule), "off" (the VOL_PER_NOTE_RULES are left out, except VOL_PER_NOTE_KEEP), "off_shape" /
# "off_level" (one class of them, below) or "cap3" (their
# sum is limited to +-VOL_PER_NOTE_CAP_DB; the kept rules are not capped). Env STP_VOL_PER_NOTE overrides it, so the
# three states can be built from one config. The slow layers (roles, hairpin gains, held decrescendos, long-note swells,
# divisi cuts, timpani roll levels, the final fade; the dynamic trims are build_reaper.py's) are never switched.
VOL_PER_NOTE = "on"
VOL_PER_NOTE_CAP_DB = 3.0
VOL_PER_NOTE_RULES = ("pitch_trim", "metric", "early_fill", "join_notch", "level_shape", "steady_level", "level_shape_s",
                      "cresc_front", "pickup", "synco", "pair_rel", "wind_detach", "str_rep_dip", "mt_alt", "uni_fade",
                      "arrival", "tenuto_swell", "phrase_top", "accent", "accent_body", "marc", "note_trim", "row_trim",
                      "bloomv", "uni_boost", "timp_attack", "rebow_fill", "loop_fill", "restrike", "breath")
VOL_PER_NOTE_KEEP = ()
# (coordinator, from the scherzo's c15 critics) the per-note rules fall into two classes: levels (one value per note:
# balance can depend on them) and shapes (movement inside or between notes). "off_shape" leaves out the shape class
# only, "off_level" the level class only
VOL_PER_NOTE_LEVEL_RULES = ("pitch_trim", "metric", "steady_level", "note_trim", "row_trim", "uni_boost", "mt_alt")
# VOL_RULE_OFF = {track: {rule: True or [(from_qn, to_qn), ...]}}: a rule's items are left out on a track (items that
# start inside a listed span, or all of them)
VOL_RULE_OFF = {}
# VOL_LIN: vol_db is written as a piecewise-linear lane (parts.json "vol_lin": build_reaper.py interpolates), with a
# point pair at each step, so a ramp is a ramp in REAPER and not a stair of grid points
VOL_LIN = False
# LEVEL_STEP_AT_SCORE: a level step between two notes (STEADY_LINE level_db, stepped pitch and note trims, metric steps,
# row trims, short flat accents) on a led note that follows a sounding note crosses over 30 ms centred on the note's
# SCORE onset instead of 30 ms before its moved note-on: the note before keeps its own level to its end (c15: the old
# note's last 40-125 ms played at the next note's level; holes over 6 dB at 15 of 21 falling steps, 6 without)
LEVEL_STEP_AT_SCORE = False
LEVEL_STEP_MIN_LEAD_S = 0.03
# accents (critic A #2): families in ACCENT_FRONT take a front-weighted swell: from the moved note-on (legato targets:
# the score onset), the plateau end and the fall counted from the score onset, ended by the next moved note-on - 0.01 s
# and the note's end. ACCENT_NO_STACK: running accent shapes combine by the larger value, not the sum. ACCENT_CAP_DB:
# the largest gentle accent. ACCENT_SHORT_FLAT_QN: an accented note this long or shorter takes one level
# (ACCENT_SHORT_FLAT_SHARE x the accent) from its note-on to the next note-on, no shape inside
ACCENT_FRONT = ()
ACCENT_NO_STACK = False
ACCENT_CAP_DB = None
ACCENT_SHORT_FLAT_QN = None
ACCENT_SHORT_FLAT_SHARE = 0.67
# SHORT_ONE_LEVEL_QN: pitch trims, note trims on notes this long or shorter are steps (one level per note), and the
# slur-pair release is left out on them
SHORT_ONE_LEVEL_QN = None
# ROW_TRIM_HOLD_QN: see the ROW_TRIM_DB loop (None = each run of abutting trimmed notes is its own step)
ROW_TRIM_HOLD_QN = None
# CHORD_CUTS (mvt3 c16; Dan, 11 Nov: no per-note volume moves): False leaves out the cuts by the number of notes
# sounding (divisi chords, double stops, tremolo chords) and ROW_GAIN_DB; the printed player-count marks ("meta",
# "N soli", "last N desks") keep their level for as long as they are in force
CHORD_CUTS = True
# UNI_BOOST_HOLD_QN (critic B #4): the unison boost of a kept note is held as one phrase level across the track's
# unboosted notes while the next boosted note starts within this many qn after the last one's end (ramps of
# UNI_BOOST_RAMP_QN before the first and after the last; a lone boosted note shorter than 0.5 qn takes half). None =
# the boost switches on and off note by note (c04)
UNI_BOOST_HOLD_QN = None
UNI_BOOST_RAMP_QN = 0.25
# mvt3 c26 (ruling 1; critic B #6): UNI_HOLD_END_REST = True: a held unison phrase level whose next note starts led (moved
# onset before the group's score end + the ramp) is released in the rest before that moved onset (from the last played
# note-off, at most 0.25 s before it, to 0.01 s before it), or just before the moved onset when there is no rest, not over
# the 0.25 qn after the score end inside the led note (Trombone 2 at 152: -3.5 dB inside the note). False = off
UNI_HOLD_END_REST = False
# mvt3 c26 (ruling 1; critic B #6, C): CHORD_SEG_EDGE_REST = True: a printed player-count level ("metà", "N soli", "last N
# desks") that starts on a led note after a rest steps in that rest (0.15 s to 0.02 s before the moved onset, not before
# the last played note-off), not 0.1 qn before the score onset inside the led note (Violins II / Violas / Violoncellos at
# 375.9 -4 dB, Violins I at 484.9 -3 dB). False = off
CHORD_SEG_EDGE_REST = False
# mvt3 c17 (coordinator's ruling 1; critics A #6, B #2): a held unison level must span a whole phrase or be dropped.
# UNI_BOOST_MIN_QN: groups shorter than this (first note-on to last note end) get no fader boost. UNI_BOOST_ONE_LEVEL:
# one level per group (the duration-weighted mean of its notes' boosts), no step between its notes
UNI_BOOST_MIN_QN = None
UNI_BOOST_ONE_LEVEL = False
# mvt3 c17: INSTR_POST = {rule: {...}}: the instrument-side post-pass (tools/instr_post.py: accents, per-pitch / per-row
# / chord controller offsets, resting levels, tongued gaps, row onsets, CC shapes, the timpani envelope folded into CC7,
# and the guard that keeps fast fader moves out of sounding notes). None = off
INSTR_POST = None
# ROW_VEL_SPANS = {track: {row: [(from_qn, to_qn, velocity), ...]}}: notes on a row inside a span take this velocity
# (the level of a short row belongs in velocity, manual p.53 / p.150, not in a fader step per note)
ROW_VEL_SPANS = {}
# mvt3 port: the timpani KS rows by patch ("Timpani Flt KS" -> "Timpani Flt Lng", "Timpani Hrd KS" -> "Timpani Hrd Lng")
TIMP_ROW = lambda stem_, kind_: stem_.replace(" KS", "") + " " + kind_
# mvt1 c11 (A #4): the Harp Sus RR groups release over 3019 ms (AHDSR in the .oib), so a note-off never damped a string.
# With the release shortened in the patch state (mix.json "env_release_ms", build_reaper.py), each harp note rings
# HARP_RING_S seconds past its written end, cut at the next damp mark (text containing HARP_DAMP_TEXT; "(m.d.)" damps
# the right-hand staff only, "(m.s.)" the left) and before the next same-pitch onset
HARP_RING_S, HARP_DAMP_TEXT = 0.0, "touffez"
HARP_DAMP_STAFF = {"(m.d.)": 0, "(m.s.)": 1, "(m.g.)": 1}   # index into the track's staves (c32 A #4: French m.g.)
# mvt1 c06 (critic A #3): a slurred string tenuto at f or louder that is a legato target keeps its weight: +TENUTO_SWELL_DB
# from 0.05 s after its onset to 0.1 qn before its end (no CC11 bump: level shaping into the join sag deepens it)
TENUTO_SWELL_DB = 1.5
# mvt1 c06 (critic C #1): arrivals {score qn: (pre_db, db)}: on every wind, brass and string track the level falls
# linearly from 0 at qn - 4 to pre_db just before the arrival (the crescendo's top is held back) and steps to +db at the
# arrival (full by +0.05 s, held to qn + 0.5, gone by qn + 1), so a downbeat that the crescendo has already reached
# still reads as the arrival. On c05 the fff downbeat of bar 160 rose only +0.3 dB (momentary max) over the beat before.
# mvt1 c08: an optional third value (pre_qn) sets the hold-back's length (default 4 qn: it cancelled a printed
# crescendo bar's gain; 0.5 makes it a breath before the downbeat)
ARRIVAL_WEIGHT_AT = {}
# mvt1 c06 (critic C #2): explicit level shapes {track or "_all": [[(qn, dB), ...], ...]} (piecewise linear, 0 outside
# the points, exact breakpoints), for hairpin gains and subito steps that a role row's 0.5 qn ramps would blur
LEVEL_SHAPES = {}
# mvt1 c24 (critic A #1/#2): level shapes in seconds around a score onset {track: [(score qn, [(s, dB), ...]), ...]}
# (piecewise linear, 0 outside, exact breakpoints; s relative to the score onset on the real tempo map), for per-note
# corrections measured in seconds (accent fronts and bodies) that must keep their length through tempo changes
LEVEL_SHAPES_S = {}
# mvt1 c42 (critic C #1): POST_SHAPES_S = {track: [(score qn, [(s, dB), ...]), ...]}: level shapes in seconds around a
# score onset like LEVEL_SHAPES_S, but applied by build_reaper.vol_points AFTER the tail hold and SUBITO_TAIL (which
# overwrite vol_db in rests and at subito marks): a shape on a release tail (the envelope is after the Opus hall).
# parts.json "vol_post" [[[qn, dB], ...], ...] (breakpoints also in vol_bp)
POST_SHAPES_S = {}
# mvt1 c14 (critic A #1): the release of a two-note slur. The second note of a slur of exactly two onsets (wind, brass,
# string; second note at most max_qn written, not accented, tenuto or sf, not a hairpin's end, no crescendo or rising
# printed level between the onsets) falls to db: 0 at its moved onset + from_s (after any legato sag), db at + full_s,
# held to the next note's moved onset (or its own end + 0.05 qn), then back to 0. On the c13 render the second notes of
# about 60 such slurs sat a median -0.3/+0.5/-0.2 dB (strings/winds/brass) against the first. None = off
SLUR_PAIR_RELEASE = {"db": -2.5, "from_s": 0.10, "full_s": 0.20, "max_qn": 1.0}
# mvt1 c18 (critic A #2): per-onset release depth {track: {second note's score qn: dB}} (0 = no release on that note);
# for a passing step inside a slur at one dynamic that the generic -2.5 dB sinks under a doubled line
SLUR_PAIR_RELEASE_DB_AT = {}
# mvt1 c18 (critic A #1): build/accent_bodies.json {track: {score qn: body_db}}: a cut of body_db (< 0) on an accented
# note's body, 0 at the score onset + ACCENT_BODY_S[0] s, full at + ACCENT_BODY_S[1] s, held to the next note's moved
# onset - 0.02 qn (or the note's end), back to 0 at that onset (exact breakpoints; parts.json "accent_body"). Long string
# accents peaked a median 0.38 s after the beat and 18 of 30 started under their body, so the accent read as a louder
# note, not weight at the start; tools/fit_accent_bodies.py fits body_db from a render
ACCENT_BODY_S = (0.25, 0.45)
# mvt1 c14 (critic A #3): WIND_DETACH (and its "by" overrides) may carry "fall_cc" and "fall_s": a CC11 fall of fall_cc
# over the note's last fall_s seconds, back at the next onset (as WIND_REP_RETONGUE), on notes of at most
# WIND_DETACH_FALL_MAX_QN
WIND_DETACH_FALL_MAX_QN = 0.6
# mvt1 c14 (critic A #2): MEAS_TREM may carry "rr_runs": run lengths used in turn; a CC36 (round-robin reset) point at
# value 127 goes 0.02 qn before the first stroke of each run (parts.json lane "cc36"), so the row's round robins do not
# repeat one fixed cycle through a long measured tremolo
# mvt1 c06 (critic C #2a): phrase-top pitch contours (PT_*) are off inside every crescendo, not only inside soft lead
# hairpins (a descending line under an mf < lost 3 dB to the contour, against the hairpin)
PT_OFF_IN_CRESC = True
# mvt1 c06 (critic A #5, test): slurred, monophonic, non-first string notes of SHORT_SUS_LEG_S seconds (min, max) on the
# listed tracks stay on Leg Slur MAX as legato targets instead of Sus MAX (short_sus), unless their own pitch follows
# in the slur (the SLUR_REP_MERGE_SUS case)
SHORT_SUS_LEG_TRACKS, SHORT_SUS_LEG_S = (), (0.20, 0.25)
# mvt1 c07 (critic A #6): per-onset exceptions to SHORT_SUS_LEG_TRACKS {track: [score qn]}: these notes stay Sus MAX
SHORT_SUS_LEG_SKIP = {}
# mvt3 c15 (critics A #4, C #1): SHORT_SUS_LEG_SPANS {track: [(from_qn, to_qn)]}: inside a span the track is treated as a
# SHORT_SUS_LEG_TRACKS track (a cantabile line whose slurred eighths of 0.20-0.25 s stay on the legato row, so the line
# has no "Sus MAX" notes inside it: a legato-row note after a "Sus MAX" note took one of two start times, c14)
SHORT_SUS_LEG_SPANS = {}
# mvt1 c25 (ONE_TIME #2): {track: [score qn]}: listed slurred, monophonic notes take the short_sus path (Sus MAX, overlapping
# the next note) whatever their length on the shaped tempo map. A phrase arc or ramp that stretches an eighth past 0.25 s
# otherwise turns it into a Leg Slur target (c24: Violins I/II 259.5 at 118 bpm)
SHORT_SUS_AT = {}
# mvt1 c25 (ONE_TIME #2): tempo gates (gate_bpm) read the map before phrase arcs and pushes. False: the shaped map (<= c24)
GATE_BPM_PRE_ARC = True
# mvt1 c07 (critic C #3): ENTRY_LEAD_S tuples may carry a third value, used for entries at CC11 51-80 at this tempo or
# faster (the mf layer of the string rows rises about 0.1 s slower than the f layer)
ENTRY_MID_MIN_BPM = 100.0
# mvt1 c07 (critic C #2): with SHORT_SUS_LEAD_TRACKS, the previous slurred note ends at the moved onset + this many qn
# (the c05 test kept the old note's end, so the old pitch sounded at full level over the whole lead). None: old rule
SHORT_SUS_LEAD_KEEP_OVERLAP = None
# mvt1 c07 (critic A #1): string row level offsets {track: {articulation: (dB, min_cc)}}. On a string track whose line
# mixes Sus/Stac rows with the Leg rows, a note on a listed row with CC11 >= min_cc at its onset that has a Leg-row note
# within ROW_TRIM_NEAR_QN gets a step trim (one step over consecutive trimmed notes). Down-bow strokes, re-bowed notes and the
# REP_SPLIT strokes are excluded (they carry their own fitted levels); accents and STR_SHORT_AFTER_SUS strokes are
# trimmed (c07 render: excluding the strokes left an accented Sus note trimmed under the untrimmed stroke after it).
ROW_TRIM_DB = {}
ROW_TRIM_STROKES = {}   # mvt3 c14: see the ROW_TRIM_DB block in build_track
# score-qn spans {track: [(start, end)]} with no row trim (where a fitted role already corrects the row's level)
ROW_TRIM_SKIP = {}
ROW_TRIM_NEAR_QN = 3.0   # the Leg-row note's interval within this many qn of the note's (a phrase that mixes rows)
# mvt1 c07 (critic A #2): WIND_REP_RETONGUE overrides by track name prefix or family {"Horn": {...}} (keys as in
# WIND_REP_RETONGUE), and for short repeats (a note of at most "max_qn" at "min_bpm" or faster) a further override
WIND_REP_RETONGUE_BY = {}
WIND_REP_RETONGUE_SHORT = None
# mvt1 c07 (critic A #2): CC11 fall (CC over the note's last 0.2 qn) at loud wind/brass breaths (mf or louder), by track
# name prefix or family; BREATH_FALL_CC per onset still wins
BREATH_FALL_BY = {}
# mvt1 c07 (critic B #4): a timpani roll that continues another roll (onset within 0.05 qn of its end) takes no
# TIMP_LOUD_ATTACK_DB bump unless a printed dynamic louder than the last one starts on it, or its score onset is listed
# here (the chained crescendo roll of bars 80-81 played as two hits)
TIMP_CHAIN_BUMP_AT = []
# mvt1 c07 (critic A #5): metric velocity on loud timpani strokes (Timpani Flt Lng, printed level >= min_cc, not
# accents): offsets by position {"down", "mid" (beat 3 of 4/4), "beat" (beats 2, 4), "off" (off-beat eighths and
# pickups)}, plus a seeded +-jit. Empty: off
TIMP_METRIC_VEL = {}
# mvt1 c07 (ONE_TIME, Dan's item 8): per-accent fitted swell levels, build/accent_fits.json {track: {score qn: swell dB
# or [swell dB, step trim dB]}} written by tools/fit_accents.py from a render. A fitted accent on a GENTLE_ACCENT family
# takes this swell (the family's swell shape, no ACCENT_MINUS_HPGAIN: the fit measured the result) and the trim as a
# step note trim (0.1 s ramp, held to the next onset)
# mvt1 c15 (critic A #2): a slur's short first note after a tongued note. A disconnected first note on Leg Slur plays
# the row's slow sustain layer (2-10 dB under the note before on 50 wind/brass notes, median -2.2 dB, against +0.8 for
# tongued Sus notes). With SLUR_START_SUS = {"families": (...), "max_qn": written length cap, "after_qn": another note
# of the track ends at most this long before it}, the first note of a slur (monophonic, not accented or tenuto, the
# slur's second note at a new pitch) plays the Sus row and overlaps the second note by LEG_OVERLAP; the second note
# stays on the legato row and is joined from it like the sostenuto join (SOST_JOIN_LEAD_S lead, at most 0.45 of the
# first note, velocity SOST_VEL). parts.json `slur_start_sus`. None = off
SLUR_START_SUS = None
# mvt1 c16 (critic A #1): a short pickup after a rest, into a new pitch that plays a legato row, plays the Sus row.
# After a rest the Leg rows play their sustain layer, which grows over 0.3-0.4 s, so an eighth pickup at 112-126 bpm
# (cut to 0.12-0.27 s by the target's legato lead) sat a median 3-9 dB under its target (worst 21 dB) and the accented
# target then swelled in late. PICKUP_SUS = {"families": (...), "max_qn": written length cap, "rest_qn": nothing of the
# track sounds this long before it (by score), "min_target_qn": the target's written length at least, "level_db":
# {family: dB}}: the pickup (monophonic, not accented or tenuto) whose next note starts at its written end (+-0.02 qn)
# at a new pitch (monophonic, in the same slur, or both unslurred on a string track) plays the Sus row and is joined to
# the target like SLUR_START_SUS (overlap LEG_OVERLAP; target led by min(SOST_JOIN_LEAD_S, 0.45 x the pickup) at
# SOST_VEL). level_db is an exact level shape from the pickup's moved onset to the target's moved onset (the Sus rows
# sit over the Leg rows at one CC11 on strings). parts.json `pickup_sus`. None = off
PICKUP_SUS = None
# mvt1 c17 (critic A #1): a pickup after a rest sits on its sample's quiet first-note plateau (4-18 dB under its target,
# on either row, same within 1.7 dB on the Leg and Sus rows), so a lead cannot bring it up. PICKUP_LIFT = {track:
# {pickup score qn: dB}}: an exact level shape from the pickup's moved onset (0.01 qn ramp in) to its target's moved
# onset, released over 0.02 qn after it (the target: the note starting at the pickup's written end). parts.json
# `pickup_lift`
PICKUP_LIFT = {}
# mvt1 c35 (critic A #4): the lift ended 0.02 qn after the target's moved onset, but on the wind and brass KS Masters the
# pickup's sample still sounds for the first 20-45 ms of the legato transition, so the join fell by about the lift (2-12
# dB within 10 ms; Clarinet 1 505 dip 9.9 dB). PICKUP_LIFT_TAIL_S = {family: (hold s, release s)}: the lift is held that
# many seconds past the target's moved onset, then released over the second value. Families not listed keep the 0.02 qn
# release. {} = off
PICKUP_LIFT_TAIL_S = {}
# mvt1 c39 (critic A #2): on a legato join the old note's sample carries the sound for 0.1-0.3 s after the target's
# moved onset, but a positive note trim or pitch trim on the old note ended over [next moved onset - 0.05, + 0.03] qn:
# 5-11 dB holes in slurred solo lines (Clarinet 1 226 -> 227 +5 pitch trim, Oboe 1 578 -> 579 +8 note trim).
# LEG_JOIN_TRIM_HOLD = {family or track: (hold s, release s)}: a positive trim on a note joined into a legato target is
# held to the target's moved onset + hold, then released to 0 by the later of moved onset + hold + release and the
# target's score onset + LEG_JOIN_TRIM_REACH_S. Not when the target has a positive trim of its own in the same table
# (the two would add into a bump). parts.json `leg_join_holds` [old note sq, target sq, dB]. {} = off
LEG_JOIN_TRIM_HOLD = {}
LEG_JOIN_TRIM_REACH_S = 0.06
# LEG_JOIN_TRIM_HOLD_AT = {track: {target score qn: share}}: per join, the share of the trim that is held (0 = not held:
# the c09 end; 0.5 = the trim falls to half at the c09 end and that half is held as above). For joins where the hold
# put a burst over the louder body instead of filling a hole (measured on a render)
LEG_JOIN_TRIM_HOLD_AT = {}
# mvt1 c39 (second render pass): ALIAS_TRACKS = {new track: {"source": track, "windows": [(a, b), ...], "patch": .oib
# (default: the source's), "no_pitch_trims": bool}}: the new track is built by build_track under the source track's
# name, with TRACK_WINDOWS[source] = (windows, keep inside), so every per-track rule and table of the source applies to
# its notes there; then renamed. The source keeps its own TRACK_WINDOWS entry for its own build (set it to (windows,
# False) in the config so it rests there). "no_pitch_trims": the source's pitch trims (fitted on its own samples) are
# left out. Appended after TRACKS in this order (stem numbers follow). PASS2_TRACKS: names of tracks that
# build_reaper.py builds only with --pass2 (a second REAPER project rendered after the main one; render_cycle.py
# --pass2 sums its stems into the master). parts.json "pass": 2, "alias_of"
# mvt1 c40: two more alias keys, used during the alias's build only. "drop": {TABLE: None | [onsets]}: the source's
# entries in that per-track table are left out (None: all of them; a list: dict keys at those onsets, or list rows
# whose first number is one of them), so a track on another patch can be fitted fresh instead of inheriting fits made
# on the source's samples. "set": {TABLE: value}: TABLE[source] = value (scalar or by-name tables such as LEG_LEAD_S)
# mvt1 c42: "hold_lanes": True: the alias's CC11 / CC1 lanes hold their value after its last note-off (see the build loop)
ALIAS_TRACKS = {}
PASS2_TRACKS = ()
# mvt1 c41: TEST_TRACKS: names of (usually PASS2_TRACKS alias) tracks rendered only to be compared with another
# track (an A/B of a patch or script setting); parts.json "test": true. render_cycle.py --pass2 writes their stems to
# cycles/cNN/test_stems/ and leaves them out of render/ and of the master sum; the tempo arcs' lead line ignores them
TEST_TRACKS = ()
# mvt1 c40 (critic A #1, MANUAL-GAPS #8): LEG_VEL_SPANS = {track: [(a, b, velocity)]}: legato targets whose score
# onset lies in [a, b) take this velocity (the HO true-legato scripts read velocity as transition speed: about 50-75
# plays more of the recorded slide, 110-127 the shortest; manual p.144). Applied after the family rules; a
# PORT_TARGETS velocity still wins on its own note. parts.json `leg_vel_span`. {} = off
LEG_VEL_SPANS = {}
# mvt1 c40 (critic A #2): CRESC_FRONTS on a led legato target start at the score onset (peak and sag keep their absolute
# times; a cut whose sag ends within 0.1 s of the score onset is left out). parts.json `cresc_front_shift`. False = the
# c36 behaviour (from the moved onset). LEG_RAMP_WARN: print a warning for every LEVEL_SHAPES / LEVEL_SHAPES_S row and
# early fill whose first ramp starts inside a led legato target's [moved onset, score onset + 0.06 s] (it lands in the
# transition, where the old note still sounds)
CRESC_FRONT_LEG_SCORE = True
# mvt1 c40 (critic C #3): RIDE_TRIMS = [[(score qn, dB), ...], ...]: score-timed trims added to the delivery ride's gain
# (tools/deliver_master.py, after lift - top), for passages where the slow zero-phase ride interpolates between loud and
# soft neighbours and writes a crescendo or diminuendo the score does not print. Copied into parts.json "ride_trims";
# deliver_master.py converts qn to file seconds on the parts.json tempo map. [] = none
RIDE_TRIMS = []
LEG_RAMP_WARN = True
# mvt3 c13: LEG_RAMP_OK = {track: [score qn of the led legato target]}: rows meant to act inside that target's
# transition (a measured dip at the join itself) are not reported by LEG_RAMP_WARN
LEG_RAMP_OK = {}
# mvt1 c17 (critic A #3): syncopated accompaniment notes swell through the note and crest on the next beat (Hollywood
# Strings Leg Slur / Sus MAX at mf: +8 dB from the start to the last 0.2 s). SYNCO_SHAPE = {"families": (...),
# "min_bpm", "rest_qn": a written rest of at least this before it in its own track, "len_qn": (min, max) written
# length, "pts": [(seconds from the score onset, dB), ...]}: a note starting on an off-beat eighth (sq mod 1 = 0.5),
# not accented and not slurred from the note before, takes the exact shape (0 just before the first point, the last
# value held to the written end, back to 0 by the next moved onset of the track or 0.25 s later). parts.json
# `synco_shaped`. None = off
SYNCO_SHAPE = None
# mvt1 c16 (critic A #5): a detached accented string stroke (DETACH_ACCENTS) that follows another one keeps at least
# this many qn of its detach gap when a lead moves it early (the basses' entry lead had closed bar 72's 0.25 qn gap to
# 0.011 qn). None = off
DETACH_LEAD_KEEP_QN = None
# mvt1 c16 (critic A #3): SLUR_PAIR_RELEASE may carry "short_s" (a second note written shorter than this many seconds
# starts its release at its moved onset, full at min(full_short_s, half its length)) and "join_db" (the depth on a
# second note joined from a SLUR_START_SUS / PICKUP_SUS first note, whose v100 join pushes it); pairs whose second
# note is such a join are measured from 0.25 qn notes up
# mvt1 c15 (critic C #2): re-tongue lead. A wind/brass note on a Sus row (or a Leg row note that is not a legato target)
# that starts under 0.5 qn after the track's previous note ends (gap > 0), at ENTRY_MID_MIN_BPM or faster, and that no
# other rule moved, starts RETONGUE_LEAD_S seconds early (by_name: track keys, then family); the previous note ends the
# same amount earlier (the tongued gap is kept), the lead is at most RETONGUE_LEAD_CAP x the previous note's written
# length, and CC11 holds the new note's level from the moved onset. Unled re-attacks landed 0.08-0.10 s (median) behind
# the strings. parts.json `retongue_leads`. Empty = off
RETONGUE_LEAD_S = {}
RETONGUE_LEAD_SPANS = {}   # mvt3 c15: see rt_for
RETONGUE_LEAD_CAP = 0.3
# mvt1 c19 (critic C #2): a "string" entry in RETONGUE_LEAD_S (or a string track key) extends the re-tongue lead to
# string notes on the plain "Sus MAX" row after a played gap under 0.5 qn (fresh strokes after a slur, detached accented
# strokes), except written-out repeated strokes (REP_SPLIT / MEAS_TREM), STR_SHORT_AFTER_SUS stroke runs, notes the automatic re-bow
# splits or that follow such a note, and the Leg -> Sus entry path (a Leg note ending within 0.1 qn). Unled Sus MAX
# string notes arrived +0.09..+0.12 s (sample only) against +0.004 for led string notes
# mvt1 c19 (critic C #4): extra re-tongue lead by articulation, {track or family: {art: s}} (by_name), added to
# RETONGUE_LEAD_S (Oboe 1's Leg Slur re-attacks after slur breaks landed +0.21..+0.23 s)
RETONGUE_LEAD_ART_S = {}
# mvt1 c37 (critic C #1.1): re-tongue leads below ENTRY_MID_MIN_BPM, {track or family: s} (by_name). The c15 rule gave
# no lead under 100 bpm, so in the Lento / Piu lento the re-attacks after short gaps played on the note-on: strings
# +0.081 s, winds +0.048, brass about +0.06, wind repeats t50 +0.15 (c36, perceived attack). Same tests and cap as
# RETONGUE_LEAD_S (a track with no entry here keeps no slow lead). None = off
RETONGUE_LEAD_SLOW_S = None
# mvt1 c19 (critic C #1): GENTLE_ACCENT notes (acc_art, plain Sus rows) take the lead rules like any other note; only
# real accent samples ("Accent" in the row name, which attack fast) keep the score onset. False = the c26 behaviour (every
# acc_art note unled: loud wind/brass accents arrived +0.10..+0.11 s, a sixteenth behind the led parts at 126)
ACC_ART_LEAD = True
# mvt1 c19 (critic C #3): {family: True}: a string slur head on Sus MAX (the slur's first note, 0.5 qn or shorter) whose next note is a led legato target joined from it starts as early as that target (its written length
# kept); the note before it ends at the head's moved onset (Sus) or 0.04 qn before it (other rows: the keyswitch guard),
# and CC11 holds the head's level from its moved onset. The first-theme heads sounded 0.065-0.08 s before the next pitch
SLUR_HEAD_LEAD = {}
# mvt1 c20 (critic A #4): SLUR_HEAD_LEAD["lead_s"] (seconds) sets the head's own lead, at most its target's (the full
# 0.17 s target lead put the Violins I heads at -0.062 s, 0.06 s early; about 0.10 s lands them on the beat)
# mvt1 c20 (critic A #2): {track: [(a, b, lead_s)]}, see the lead stage
GROUP_LEAD_AT = {}
# mvt1 c15 (critic A #3): WIND_DETACH (or its "by" overrides) may carry "dip_db" (and "dip_fall_s", default 0.05): a
# brass/wind note at a tongued change (the next note starts at its written end, a new pitch, outside its slur; no
# other note held across) at a printed level of "dip_min_cc" or more, whose played gap to the next moved onset is under WIND_DETACH_DIP_MAX_GAP_S gets a
# volume-envelope dip: 0 dB at its end - dip_fall_s, dip_db at its end, held to the next moved onset - 0.005 s, back to
# 0 at + 0.005 s (the c14 CC11 fall moved the holes 0.4 dB; CC11 at f/ff is about 1 dB per 10 CC). parts.json `detach_dips`
WIND_DETACH_DIP_MAX_GAP_S = 0.07
# mvt1 c33 (critic C #3): WIND_WIDE_LEG = semitones (None = off): a wind note on a legato row joined from (or re-tongued
# within WIND_WIDE_LEG_GAP_QN after) a note more than this many semitones away plays the Sus row, re-tongued with the
# RETONGUE_LEAD_S lead (the HO legato scripts join only within an octave, kit LEARNINGS section 5). parts.json `wide_leg`
WIND_WIDE_LEG, WIND_WIDE_LEG_GAP_QN = None, 0.1
# mvt1 c22 (critic A #1): STR_REP_DETACH = {"at": {track: [(a, b), ...]}, "dip_db", "dip_s", "ramp_s", "back_s",
# "max_qn", "min_cc"}: inside each listed score-onset span [a, b), an unslurred string note of max_qn or less that runs
# into the next onset of the track (written end within 0.05 qn of it) at a printed level of min_cc or more gets a volume
# dip before the next moved onset: 0 dB at onset - dip_s - ramp_s, dip_db at onset - dip_s, held to onset + back_s, 0 at
# onset + back_s + ramp_s (exact breakpoints). The Hollywood Strings Sus MAX eighths of a ff pedal swell to mid-note and
# run together (Marc Shrt c03 and Detache c13 separated no better); the dip gives each eighth a front. parts.json
# `str_rep_dips`. None = off
# mvt1 c37 (critic A #1): a span may be (a, b, opts): opts override "dip_db", "dip_s", "ramp_s", "back_s", "max_qn" and
# "min_cc" for that span, and add "frac" (the dip length is min(dip_s, frac x the seconds between the two moved
# onsets), so sixteenths keep a body) and "same_pitch_only" (dip only before a same-pitch repeat). Abutting unslurred
# same-pitch string repeats (330 on Sus MAX in c36) dipped a median 1.9 dB on the stem: the Sus MAX release (524-931 ms)
# covers a 0.01-0.02 s bow change, and the string legato rows have no same-pitch transition samples
STR_REP_DETACH = None
# mvt1 c37 (critic A #2): STR_REP_AFTER_STAC = {"max_qn": q}: an unslurred, monophonic string note of at most q (written)
# whose predecessor (the latest onset before it) is a same-pitch note on a "Stac" row (not a REP_SPLIT / MEAS_TREM
# stroke) is a fresh Sus MAX stroke
# (the DOWNBOW_STROKE_AT path: velocity REBOW_VEL_BY_CC, the next note joins from it as a Leg BC target), and takes the
# string re-tongue lead ("max_gap_qn", default 1.0: the staccato starts at most this long before it; its played end
# is the half-length staccato end). On Leg Slur MAX (no legato connection from a Stac stroke) it played the first-note layer: the
# fugato subject's quarter after its staccato eighth started 6-12 dB under the eighth and reached its body at
# +0.26..+0.36 s (c36). parts.json `down_strokes`, `rep_after_stac`. None = off
STR_REP_AFTER_STAC = None
# mvt1 c44 (ONE_TIME #4; critics A #1-#2, B #5; Dan's S1 "repeated notes must be heard as separate notes"):
# STR_REP_NEW_BOW = {...}: a monophonic same-pitch string repeat that the legato merge would join into the note before
# (one note with a 6-14 CC CC11 notch: 49 merges in v621, stem dips 2-4 dB, master 1.5-3 dB) is played as a new bow
# when it is not inside the note before's slur (or both are unslurred), or when it is a slurred tenuto (louré):
#  - "stroke": accented, or base CC >= "stroke_cc", or the last printed mark at it >= "stroke_mark", or a slur head at
#    "head_cc" or louder: a fresh Sus MAX stroke on the DOWNBOW_STROKE_AT path (the next note of its slur joins from
#    it), the string re-tongue lead (RETONGUE_LEAD_S / RETONGUE_LEADS) with the note before giving way so its gap is
#    kept; the note before ends min("gap_s", "frac" x its length) before the score onset (never a new unled Leg Slur
#    note: the c05 7-17 dB first-note hole). The ROW_TRIM_DB Sus row trims apply (B #5), and no delayed-vibrato dip;
#  - "portato" (same slur, tenuto on the repeat; A #1): the same stroke with the "portato" gap / frac and a CC11 fall
#    of "fall_cc" ("fall_cc_loud" above CC 90) over the note before's last "fall_s" seconds (WIND_REP_PORTATO values);
#  - "soft" (any other new bow, e.g. pp-p held notes): the merge stays, and the bow change becomes a re-bow point at
#    the printed onset (the REBOW_AT machinery: a Sus MAX piece after REBOW_GAP_QN, fitted by tools/fit_rebows.py)
#    instead of the CC11 notch. A soft repeat after a stroke merges into the stroke.
# Repeats inside one slur without a tenuto stay merged; tremolo / flautando common tones are not affected.
# "sus_min_s" (optional): an unslurred same-pitch repeat between two Sus MAX notes (not REP_SPLIT strokes, not inside
# STR_REP_DETACH spans), at "stroke_cc" or louder and lasting this many seconds, gets the same gap (it kept 0.03 qn).
# parts.json `rep_strokes` [[score onset, class]], `rep_rebows` [score onset], `rep_sus_gaps`. None = off (the c05-c43 merge)
# mvt3 c03: "tenuto" {gap_s, frac, fall_cc, fall_s} (optional): an unslurred same-pitch repeat carrying a tenuto is
# a new bow at any dynamic and length (outside STR_REP_DETACH spans)
# mvt3 c02: "skip" {track: [(a, b), ...]}: repeats with a score onset in [a, b) keep the merge (e.g. "change bow at will"
# chorale notes and slurred portato accompaniment that should stay one sound)
STR_REP_NEW_BOW = None
# mvt1 c37 (critic A #3, MANUAL-GAPS #2): REP_ROW = {track: [(a, b, row), ...]}: in each score-onset span [a, b), notes
# on a plain sustain row (Sus MAX, Sus Non Vib, Sus Non Vib MAX, Sus Vib MAX), and notes on a legato row when `row` is a
# legato row (e.g. "Leg Slur Rep"), are played on `row` (the keyswitch only: every other rule still sees the old row).
# A same-pitch repeat into a span note that WIND_REP_RETONGUE / WIND_REP_PORTATO would re-tongue is not shortened by
# their gap and gets no CC11 fall: the note before ends REP_ROW_GAP_S before the next onset (at most half its length).
# The HO repetition rows (LegRep RRx4, Leg Slur Rep) play a recorded re-tongue attack over the sustain on a note that
# starts within 200 ms of the previous one (group start mode NoteTimer, 200 ms; read from the .oib). parts.json `rep_row`
# mvt1 c38 (critics A #1, C #2): REP_ROW_GAP_S may be (min, max): the repeat keeps the WIND_REP_RETONGUE gap, frac and
# CC11 fall of its track (with WIND_REP_RETONGUE_BY / _SHORT), the gap clamped to [min, max]. With the c37 0.03 s gap
# and no fall the rows separated less than the emulation (Contrabassoon 4.4 -> 2.9, Horn 4 6.0 -> 3.2, Bassoon 1 132
# 5.0 -> 1.4 dB), and Clarinet 1's 640 fell inside the "Leg Slur Rep" 30 ms VoiceTimer and did not sound; the one
# repeat with a long gap (Bassoon 1 352, 0.119 s) improved (6.8 -> 8.6 dB). Inferred from Bassoon 1 132: the 200 ms
# NoteTimer counts from the previous note-off, so gaps up to about 0.15 s keep the re-tongue.
# REP_ROW_REPEATS_ONLY: families whose repetition rows play the re-tongue on every note (the Hollywood Brass LegRep
# RRx4 groups start on RoundRobin only, no timer; read from the .oib): only same-pitch repeats go on the row, so phrase
# entries keep their Sus attack (Horn 4 entries on the row: front -1.0..-2.4 dB, sag 1.8-3.6 dB deeper, c37)
REP_ROW = {}
REP_ROW_GAP_S = 0.03
REP_ROW_REPEATS_ONLY = ()
# mvt1 c38 (critic C #2): SLUR_HEAD_REP_SUS = {"families": (...), "gap_qn": q[, "at": {track: [score qn]}]}: a slur
# head that repeats the pitch of the note before it plays the Sus row (see the rule); "at" restricts it to listed heads.
# None = off
SLUR_HEAD_REP_SUS = None
# mvt1 c38 (critic C #3): SUL_SPANS = {track: [(a, b, "g"|"d"|"a"|"c"|"e"), ...]}: printed "sul X" spans (score qn of
# note onsets, inclusive) that the event list does not carry (the score sets them as TextSpanner texts). With
# SUL_FP_FROM_PATCH the CC70 value of each note in a span comes from the patch's finger-position table (fp_strings),
# and the lane holds SUL_DEFAULT_CC70 outside the spans (20 = FP1, the FingerPosition script's value for the patch
# state's fingerPosition 0; inferred to be the default the renders played). parts.json `sul_notes`
SUL_SPANS = {}
SUL_FP_FROM_PATCH = True
SUL_DEFAULT_CC70 = 20
# mvt1 c39: the CC70 value sent for FP4 inside a span (None: the script's 120). c39 rendered Violins I, whose lane began
# at 120 (its first notes are in a sul D span) and returned to 127, exactly as the c38 render with the lane at 20 (FP1)
# outside the spans (median 0.00 dB), while Violins II (lane from 127) and the celli (20 -> 55 -> 127) matched the
# renders that sent no CC70. 120 and 127 are the same FP4 band in the patches' start modes; the cause is not known
# (inferred: the value a lane starts at). 127 makes every FP4 note send the resting value, so no lane starts at 120
SUL_FP4_CC70 = None
# mvt1 c23 (critic A #3): STAC_LEAD_S = {track: seconds} (exact track names): a string note on a row whose name starts
# "Stac" (printed staccato; not the REP_SPLIT / measured-tremolo strokes) starts that many seconds early; a previous
# note of the track that ends at or before the score onset (+0.05 qn) and would overlap the moved onset ends 0.02 qn
# before it; CC11 holds from the moved onset (pulls). The Violins I Stac RRx14 strokes reached -3 dB at +0.10 s and
# peaked at +0.13 s against +0.04..+0.07 s for the winds and the other strings. parts.json `stac_leads`
# mvt3 c05 (critic A #5): PIZZ_LEAD_S = {track: seconds}: the same lead for string notes on a pizzicato row (name contains
# "Pizz"); the Celli "Pizzicato RRx4" plucks reached their onset 39 ms after the Basses' "Pizz RRx4" on shared notes
PIZZ_LEAD_S = globals().get("PIZZ_LEAD_S", {})
# mvt3 c05 (critic A #4): ROW_LEAD_S = {track: {row: seconds}}: every note on that row that abuts the note before it starts
# that many seconds early, the previous note ending 0.02 qn before the moved onset (muted Trumpet 1 "Mute Sus" butted
# notes trailed the cor anglais they double by 35 ms)
ROW_LEAD_S = globals().get("ROW_LEAD_S", {})
# mvt3 c07 (critic C #2): a ROW_LEAD_S value may be a list of (from_qn, to_qn, seconds) spans; such a lead is capped at
# this share of the abutting note's played slot. TREM_ENTRY_LEAD_SPANS {track: [(from_qn, to_qn, s)]} overrides
# TREM_ENTRY_LEAD_S inside the spans
ROW_LEAD_CAP_FRAC = 0.45
# mvt3 c12 (critic A #3): ROW_SLUR_OVERLAP_S = {track: {row: seconds}}: at a ROW_LEAD_S join under one printed slur the
# note before ends this long after the moved onset (instead of 0.02 qn before it), so its release covers the new attack
# on a polyphonic sustain row. Default: none.
# mvt3 c13 (critic A #2): the value may be a list of (from_qn, to_qn, seconds) spans (first match wins), because one
# overlap did not serve every join of a row; in a span 0.0 ends the note before exactly at the moved onset, and an onset
# in no span keeps the 0.02 qn gap
ROW_SLUR_OVERLAP_S = globals().get("ROW_SLUR_OVERLAP_S", {})
# mvt3 c12 (critic A #4): ROW_LEAD_KEEP_END = {track: {row: [(from_qn, to_qn), ...]}}: a ROW_LEAD_S stroke in a listed span
# keeps its note end (it sounds longer by the lead) instead of keeping its played length, so the played gap before the
# next stroke does not grow by the lead. Default: none.
ROW_LEAD_KEEP_END = globals().get("ROW_LEAD_KEEP_END", {})
ROW_LEAD_KEEP_GAP = {}   # mvt3 c15: {track: {row: [(from_qn, to_qn)]}}, see the ROW_LEAD_S branch
TREM_ENTRY_LEAD_SPANS = {}
STAC_LEAD_S = {}   # mvt1 c39: wind tracks too (the woodwind "Stac DblTng" rows; the row's notes otherwise keep the score onset)
# mvt1 c36 (critic A #2): STAC_ROW = {track: row}: the row a listed string track plays printed staccatos on (default the
# first of "Stac RRx14", "Stac RRx9", "Staccato RRx9" the patch has). The 1st Violins KS Master's row names are swapped
# against its samples: "Stac RRx14" holds the "V1 Staccatissimo" folder (StacSs files, 0.51 s for the f G5), and
# "Staccatissimo RRx9" holds "V1 Stac" (0.76 s), while the other sections' "Stac RRx9" rows play their "Stac" folders
STAC_ROW = {}
# mvt1 c23 (critic A #4): STR_REST_SHORT = {"at": {track: [(a, b)]}, "frac", "max_qn", "min_bpm"}: inside a listed
# score-onset span, an unslurred string note of max_qn or less (written) followed by a written rest (the track's next
# onset at least 0.05 qn after its written end), at min_bpm or faster, ends at frac x its written length after the score
# onset (the moved onset keeps its lead). Hollywood Strings Sus MAX notes hold their level for about 0.06 s after the
# note-off and then a release trail fades in, so ff off-beat eighths filled their eighth rests (drop 1.9-8.4 dB).
# parts.json `rest_short`. None = off
STR_REST_SHORT = None
# mvt1 c35 (critic A #3): NOTE_END_AT = {track: {score onset: end score qn}}: listed notes end at the given score qn
# (never later than they would have). For a long note before a rest whose release trail (0.1-0.4 s on the Hollywood
# Strings legato rows) would otherwise sound under the level step of the next entry: the celli's sub. p G2 of bar 84
# released 0.12-0.2 s after its note-off, under the next phrase's +14 dB boost, 10 dB over both sides. parts.json `end_at`
NOTE_END_AT = {}
# mvt1 c37 (critic C #4): CUTOFF_EARLY_S = {track or family: s} (by_name): a note followed in its track by a written rest
# of at least CUTOFF_EARLY_REST_QN (or by nothing before SCORE_END), not staccato, not pizz., not listed in NOTE_END_AT,
# written at least CUTOFF_EARLY_MIN_S long, ends s seconds before its written end (never later than other rules set).
# The Hollywood Strings and Brass releases are longer than the winds': -6 dB 0.145 s (strings) / 0.135 (brass) / 0.095
# (winds) after the written end, so tutti cut-offs spread 0.3-0.55 s (c36). Notes ending at SCORE_END are left to the
# final fade. parts.json `cutoff_early`. None = off
CUTOFF_EARLY_S = None
CUTOFF_EARLY_REST_QN, CUTOFF_EARLY_MIN_S = 1.0, 0.4
# mvt3 c08 (critic A #1): FINAL_RING = {"at": score qn, "end": score qn, "ring_s": s, "pts": [(s after end, dB)],
# "families": (...)}: the notes of these families that sound at "at" and reach "end" (the last chord) skip CUTOFF_EARLY_S,
# are held ring_s seconds past "end", and the volume envelope falls from 0 dB at "end" through pts (the last one held):
# a release ring instead of a dead stop when release caps and the dry hall make the last chord fall 20 dB in 0.27 s.
# The sends are post-fader, so the returns follow the fall and keep their own tails (not a subito: S3 does not apply).
# parts.json `final_ring`. None = off
FINAL_RING = None
HP_GAIN_IN_WINDOW, HP_GAIN_IN_WINDOW_SKIP = True, ()   # mvt1 c35 (critic A #1): see hps_v in build_track
CUR_ALIAS = None   # mvt1 c40: the ALIAS_TRACKS name being built (HP_GAIN_IN_WINDOW_SKIP may list an alias by its own name)
# mvt1 c35 (critic A #1, the fallback without a solo track): a "tutti"/"solo" entry straight after a legato note (gap
# under 0.1 qn) was marked fresh (entry lead, the old note cut before it) only when the step was an octave or less; a
# wider step that is slurred got nothing (an unslurred one goes to Sus MAX) and started unled on the slow first-note
# layer of Leg Slur MAX (the celli's "Tutti" pp G2 at the end of the coda's "Solo espr." B4: -61 dB at +0.3 s, body - 3
# dB only at +0.7 s, the other sections on the beat). True: such a slurred wide step is fresh too
FRESH_WIDE_SLURRED = True
# mvt1 c36 (critic C #1, Dan's note on bar 62): a note whose score onset carries a subito mark softer than the level
# before ("sub. p" after a crescendo) was a legato target of the loud note before it: it started 0.2 s early under the
# crescendo's CC11 and dB ramp (a +9 dB blip in the master), then the post-hall volume envelope fell 11-16 dB at the
# score onset and cut the forte's hall tail ("sounds like a glitch"). True: such a note is a fresh entry (not a legato
# target, the note before ends with a short gap, the family entry or re-tongue lead, its own CC11/CC1 from its moved
# onset), and parts.json `subito_falls` [[score qn, fall qn]] tells build_reaper.vol_points where the envelope falls
# (SUBITO_TAIL there)
SUBITO_FRESH = True
# mvt1 c36: CC7 (MIDI Volume) points for listed tracks other than the timpani {track: [(score qn, CC7)]}, with CC7 127
# at qn 0. A test lane: does Opus apply CC7 before or after its own hall (the subito fall could then be pre-hall)?
CC7_POINTS = {}
# mvt1 c23 (critic A #1): the ACCENT_BODY_S ramp for accented notes shorter than ACCENT_BODY_SHORT_MAX_S (a 1 qn note at
# 126 bpm is 0.476 s, too short for the 0.25-0.45 s ramp). None = ACCENT_BODY_S for every note
ACCENT_BODY_S_SHORT = None
ACCENT_BODY_SHORT_MAX_S = 0.8
# mvt1 c23 (critic A #2): an ART_SPANS entry may carry "poly": True, so chords (double stops) in the span take the row too
# (a sustain row such as "Sus Marc LITE" plays chords; legato rows do not)
# mvt1 c23: string sustain rows that take the Sus MAX stroke leads (the string re-tongue lead and the Leg -> Sus entry
# path); an ART_SPANS row on these keeps the timing of the Sus MAX stroke it replaces
STR_STROKE_ROWS = ("Sus MAX", "Sus Marc LITE")
# mvt1 c23: SHORT_SUS_LEAD_S is capped at this share of the previous slurred note's slot (from its moved onset), so a
# 0.10 s lead meant for eighths does not swallow a sixteenth. None = no cap. An ABUT_LEAD entry may carry "cap_frac"
# (the same cap against the abutting note)
SHORT_SUS_LEAD_CAP_FRAC = None
# mvt1 c15 (critic C #5): a UNI_DELAY copy (a unison copy that outlasts the kept note) overlaps the kept note by
# UNI_DELAY_OVERLAP_QN and, with UNI_DELAY_FADE = (dB, s), fades in from dB to 0 over s seconds from its delayed start,
# so the held note does not sound re-attacked (Oboe 2 at bar 158 and Horn 3 at bar 105 re-attacked 0.45 s after the beat)
UNI_OUTLAST_QN, UNI_DELAY_OVERLAP_QN, UNI_DELAY_FADE = 0.25, 0.1, None
# mvt3 c08 (critic A #3): UNI_OUTLAST_PLAY = {"min_delay_qn": qn, "db": dB, "ramp_qn": qn}: an outlasting unison copy
# whose delayed start would come more than min_delay_qn after its own onset (a held note that would only speak as a late
# 0.25-0.8 qn stub behind the fade: Oboe 2 under Oboe 1's slurred line, a horn chord note) plays from its own onset
# instead, db under from there to the kept note's end, then ramps to 0 over ramp_qn. parts.json `uni_played`. None = off
UNI_OUTLAST_PLAY = None
# mvt1 c15 (critic A #4): MEAS_TREM may carry "alt_row" (an articulation name) with "alt_share" (0..1), "alt_seed" and
# "alt_max_run": the expanded strokes alternate between the stroke row and alt_row in a seeded irregular order (no row
# more than alt_max_run strokes in a row), so the two rows' round robins no longer repeat one 9-stroke cycle (CC36 inside
# the music does not reset it, c14). "alt_db": a step level offset on the alt_row strokes. parts.json `meas_trem_alt`

# ---------- SCORE CONFIG ----------
# Movement-specific tables (track table, routing windows, tempo spans, per-onset rules) start empty here and are set in
# build/score_config.py, a Python file run in this module's namespace (it can use S, W, B, H, P, DYN and every default
# above). SCORE_END is the score qn of the last release (the final fade and the pre-render end use it).
RAMP_SPANS = []
PHRASE_ARCS = []
TEMPO_PUSH = []
APEX_LEAD = {}
APEX_SKIP = set()   # mvt1 c24: arc start qns whose apex beat is not held (an arc added only for its end)
BEAT_STRETCH = {}
SHARED_DYN = {}
SCORE_END = None
SCORE_TITLE = "mockup"   # item names in REAPER and the mp3 name (render_cycle.py)
_CFG = f"{BUILD}/score_config.py"
if __import__("os").path.exists(_CFG):
    exec(compile(open(_CFG).read(), _CFG, "exec"))
if not TRACKS:
    sys.exit(f"no TRACKS: write {_CFG} (see mockup-kit/pipeline/example-config/score_config.py)")

ksmaps = json.load(open(KSMAPS))
# c10 (A #1): keyswitch maps of patches not in the bridge's ks_maps.json, dumped from the .oib with dump_ks.py
if __import__("os").path.exists(f"{BUILD}/ks_maps_extra.json"):
    ksmaps.update(json.load(open(f"{BUILD}/ks_maps_extra.json")))
# mvt3 c23 (ruling 4): {track: {edge qn: (x0, x1)}}: where two roles.json rows of a track meet at edge qn (chained), the
# crossfade runs over [x0, x1] instead of [edge - 0.1, edge + 0.15] (a role step placed in a short rest between notes)
ROLE_EDGE_XF = globals().get("ROLE_EDGE_XF", {})
ROLES = json.load(open(f"{BUILD}/roles.json")) if __import__("os").path.exists(f"{BUILD}/roles.json") else {}
NOTE_TRIMS = json.load(open(f"{BUILD}/note_trims.json")) if __import__("os").path.exists(f"{BUILD}/note_trims.json") else {}
# mvt1 c36 (critic C #3): crescendo-front cuts (see CRESC_FRONTS in build_track)
CRESC_FRONTS = json.load(open(f"{BUILD}/cresc_fronts.json")) if __import__("os").path.exists(f"{BUILD}/cresc_fronts.json") else {}
# c06 (A #2): per-pitch level trims for notes on a legato articulation, {track: {midi pitch: dB}} (sample unevenness)
PITCH_TRIMS = json.load(open(f"{BUILD}/pitch_trims.json")) if __import__("os").path.exists(f"{BUILD}/pitch_trims.json") else {}
# c07 (C #2b): extra entry leads in seconds, {track: {score onset: s}}
ENTRY_LEADS = json.load(open(f"{BUILD}/entry_leads.json")) if __import__("os").path.exists(f"{BUILD}/entry_leads.json") else {}
ACCENT_FITS = json.load(open(f"{BUILD}/accent_fits.json")) if __import__("os").path.exists(f"{BUILD}/accent_fits.json") else {}
ACCENT_FITS = {k: v for k, v in ACCENT_FITS.items() if not k.startswith("_")}
# c08 (A #1): early fills, {track: {score onset: dB}} on the first 0.35 s of sagging legato targets
ACCENT_BODIES = json.load(open(f"{BUILD}/accent_bodies.json")) if __import__("os").path.exists(f"{BUILD}/accent_bodies.json") else {}
ACCENT_BODIES = {k: v for k, v in ACCENT_BODIES.items() if not k.startswith("_")}
EARLY_FILLS = json.load(open(f"{BUILD}/early_fills.json")) if __import__("os").path.exists(f"{BUILD}/early_fills.json") else {}
LEG_LEADS = json.load(open(f"{BUILD}/leg_leads.json")) if __import__("os").path.exists(f"{BUILD}/leg_leads.json") else {}
# c16 (A #1): loop-seam fills, {track: {score onset: [[t_s, dB, width_s], ...]}}: the HO string sustain samples loop with
# a 3.95 s period and dip 4-12 dB at the seam; t_s is measured from the note's moved start (the stem time of its onset)
LOOP_FILLS = json.load(open(f"{BUILD}/loop_fills.json")) if __import__("os").path.exists(f"{BUILD}/loop_fills.json") else {}
# c17 (A #1): folded loop-seam profiles {track: {onset: {period_s, corr_db[] (20 ms phase bins)}}} replace the bump fills
# for those notes: the 3.97 s string sustain loop is a whole-cycle swell and sag, not a row of notches
# c26: per-re-bow level shapes for the REBOW_AT notes, fitted on the first c26 render (build/rebow_fills.json, see its _doc)
REBOW_FILLS = json.load(open(f"{BUILD}/rebow_fills.json")) if __import__("os").path.exists(f"{BUILD}/rebow_fills.json") else {}
# mvt1 c45 (critic B #1; ported mvt3 c04): a re-bow fill list holds its last value until the next list starts, but never
# into a later note: it ends at the end of the note its re-bow belongs to and reaches 0 dB this many seconds later
# (None: old rule)
REBOW_FILL_END_S = 0.12
REBOW_MOVES = json.load(open(f"{BUILD}/rebow_moves.json")) if __import__("os").path.exists(f"{BUILD}/rebow_moves.json") else {}
REBOW_MOVES = {k: v for k, v in REBOW_MOVES.items() if not k.startswith("_")}
LOOP_PROFILES = json.load(open(f"{BUILD}/loop_profiles.json")) if __import__("os").path.exists(f"{BUILD}/loop_profiles.json") else {}
LP_START_S, LP_STEP_S, LP_FADE_S, LP_END_S = 0.8, 0.04, 0.3, 0.3


# mvt1 c00: articulation names that some KS Masters spell differently (the Solo Trumpet KS Master has no "Sus MAX", only
# "Sus Non Vib MAX" and "Sus Vib MAX"); tried after the names asked for
KS_ALIASES = {"sus max": ("Sus Non Vib MAX", "Sus Vib MAX"), "sus accent max": ("Sus Accent MAX",)}


# mvt1 c20 (critic A #1): articulation rows that play as monophonic legato although "Leg" is not in their name (the
# Hollywood Strings "Slur Runs" row: Leg Slur transitions plus half-/whole-step scale samples). Every legato test in this
# module goes through _lg()
LEG_ROWS_EXTRA = ("Slur Runs",)


def _lg(art):
    return bool(art) and ("Leg" in art or any(art.lower() == x_.lower() for x_ in LEG_ROWS_EXTRA))


def ks_lookup(patch_stem, *names):
    arts = {a["name"].lower(): a["key"] for a in ksmaps[patch_stem]["articulations"]}
    for n in names:
        if n.lower() in arts:
            return n, arts[n.lower()]
    for n in names:
        for al in KS_ALIASES.get(n.lower(), ()):
            if al.lower() in arts:
                return al, arts[al.lower()]
    raise KeyError(f"{patch_stem}: none of {names} in {sorted(arts)}")


# ---------- MIDI ----------
mid = mido.MidiFile(f"{BUILD}/mockup.midi")
TPB = mid.ticks_per_beat
notes = collections.defaultdict(list)
tempo, timesig = [], []
for tr in mid.tracks:
    name, tick, on = None, 0, {}
    for x in tr:
        tick += x.time
        if x.type == "track_name":
            name = x.name.split(":")[0]
        elif x.type == "set_tempo":
            tempo.append((tick / TPB, round(mido.tempo2bpm(x.tempo), 3)))
        elif x.type == "time_signature":
            timesig.append((tick / TPB, x.numerator, x.denominator))
        elif x.type == "note_on" and x.velocity > 0:
            on.setdefault(x.note, []).append((tick, x.velocity))
        elif x.type in ("note_off", "note_on"):
            if on.get(x.note):
                t0, v = on[x.note].pop(0)
                notes[name].append({"qn": t0 / TPB, "end": tick / TPB, "pitch": x.note, "vel": v})
# mvt3 c01 (critic A #5): GLISS_SPANS (see the default) written out as notes
for gst_, gls_ in GLISS_SPANS.items():
    for ga_, gb_, glo_, ghi_, gpc_, gv0_, gv1_ in gls_:
        gp_ = [p_ for p_ in range(glo_, ghi_ + 1) if p_ % 12 in gpc_]
        notes[gst_] = [n_ for n_ in notes[gst_] if not (abs(n_["qn"] - ga_) < 1e-6 and n_["pitch"] == glo_)]
        gd_ = (gb_ - ga_) / len(gp_)
        for k_, p_ in enumerate(gp_):
            notes[gst_].append({"qn": round(ga_ + k_ * gd_, 4), "end": round(ga_ + (k_ + 1) * gd_, 4), "pitch": p_,
                                "vel": 64, "gliss_vel": round(gv0_ + (gv1_ - gv0_) * k_ / max(1, len(gp_) - 1))})
        notes[gst_].sort(key=lambda n_: (n_["qn"], n_["pitch"]))
        print(f"  gliss {gst_} {ga_}-{gb_}: {len(gp_)} notes {gp_[0]}..{gp_[-1]}", file=sys.stderr)
TEMPO = sorted(tempo)

# c03 (critic C #4): the printed rit./allargando/animando are realised in the score MIDI as tempo steps (global.ily \mt).
# Inside each span the step values are placed at the midpoints of their own steps and joined linearly (extrapolated to
# the span end), written as 0.25 qn steps. Spans: (start qn, end qn, tempo at the start).
# RAMP_SPANS: defined before the score config is read (see SCORE CONFIG below)


def smooth_tempo(steps):
    def step_val(q):
        v = steps[0][1]
        for tq, b in steps:
            if tq <= q + EPS:
                v = b
        return v
    out = [(q, b) for q, b in steps if not any(a - EPS <= q < e - EPS for a, e, _ in RAMP_SPANS)]
    for a, e, t0 in RAMP_SPANS:
        inner = [(q, b) for q, b in steps if a - EPS <= q < e - EPS]
        bounds = [q for q, _ in inner] + [e]
        anchors = [(a, t0)] + [((bounds[i] + bounds[i + 1]) / 2, b) for i, (q, b) in enumerate(inner)]
        anchors = [p for i, p in enumerate(anchors) if i == 0 or p[0] > anchors[i - 1][0] + EPS]
        if len(inner) > 1 and all(inner[i_][1] >= inner[i_ + 1][1] for i_ in range(len(inner) - 1)):
            # mvt1 c07 (critic C #4): a printed rit. never speeds up: when the ramp starts under its first printed step
            # (a phrase arc slowed the beat before), hold the start tempo until the printed steps fall below it
            run_ = t0
            for i_, (q_, v_) in enumerate(anchors):
                run_ = min(run_, v_)
                anchors[i_] = (q_, run_)
        (qa, va), (qb, vb) = anchors[-2], anchors[-1]
        end_v_ = vb + (vb - va) * (e - qb) / (qb - qa)
        if RAMP_END_CLAMP and inner and all(inner[i_][1] >= inner[i_ + 1][1] for i_ in range(len(inner) - 1)) \
                and step_val(e) <= inner[-1][1] + EPS:
            # mvt3 c03 (critic C #6a): a slowing ramp that ends on a printed tempo at or under its last step does not
            # extrapolate under that tempo (allargando 124, 112 -> Maestoso 112 reached 106.4 at 887.75, then the fff
            # downbeat was 5% faster than the beat before it)
            end_v_ = max(end_v_, step_val(e))
        anchors.append((e, end_v_))

        def lin(q):
            for (q0, v0), (q1, v1) in zip(anchors, anchors[1:]):
                if q0 - EPS <= q <= q1 + EPS:
                    return v0 + (v1 - v0) * (q - q0) / (q1 - q0)
            return anchors[-1][1]
        k = 0
        while a + 0.25 * k < e - EPS:
            q = a + 0.25 * k
            out.append((round(q, 4), round(lin(q + 0.125), 3)))
            k += 1
        # report: span length with steps vs ramp
        sec_steps = sum(0.25 * 60 / step_val(a + 0.25 * j + 0.1) for j in range(k))
        sec_ramp = sum(0.25 * 60 / lin(a + 0.25 * j + 0.125) for j in range(k))
        print(f"  tempo ramp {a}-{e}: {sec_steps:.2f} s stepped -> {sec_ramp:.2f} s ramped", file=sys.stderr)
        # mvt3 port: a span whose end has no step of its own (the printed tempo after it equals the last step inside,
        # e.g. allargando 124, 112 -> Maestoso 112) returns to the stepped value at the span end instead of holding the
        # ramp's extrapolated value until the next step
        if not any(abs(q_ - e) < EPS for q_, _ in steps):
            out.append((e, step_val(e)))
    return sorted(out)


TEMPO = smooth_tempo(TEMPO)

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
# PHRASE_ARCS: defined before the score config is read (see SCORE CONFIG below)
PHRASE_PUSH, PHRASE_SLOW = 1.015, (0.96, 0.92)
PHRASE_SLOW_SUB, PHRASE_SLOW_MAIN, PHRASE_RETURN = (0.98, 0.95), (0.95, 0.88), 0.97
# mvt3 c15 (critics A, C #6): arc depth "light": like "sub" (no push) with the last two quarters at PHRASE_SLOW_LIGHT, for
# phrase ends that have no printed breath mark in a passage the score keeps at the main tempo (under 3 % per beat)
PHRASE_SLOW_LIGHT = (0.99, 0.975)
# mvt1 c27 (critic C #2): False = an "open" arc (push only, no slowing) does not give the arc after it a PHRASE_RETURN
# beat (there is nothing to return from: an open (384, 396) put a 3% slower beat on the next arc's first beat)
PHRASE_RETURN_AFTER_OPEN = globals().get("PHRASE_RETURN_AFTER_OPEN", True)   # set in build/score_config.py (run before this line)


def phrase_arcs(steps):
    def val(q):
        v = steps[0][1]
        for tq, b in steps:
            if tq <= q + EPS:
                v = b
        return v
    ends_done = []
    for arc in PHRASE_ARCS:
        a, e = arc[0], arc[1]
        depth = arc[2] if len(arc) > 2 else None
        if any(a < e2 - EPS and e > a2 + EPS for a2, e2, _ in RAMP_SPANS):
            print(f"  phrase arc {a}-{e}: skipped (tempo ramp)", file=sys.stderr)
            continue
        if depth != "open" and any(abs(e - a2) < 0.01 for a2, e2, _ in RAMP_SPANS):
            # (mvt3 c07: an "open" arc does not slow its last beats, so it cannot make the ramp start faster)
            # mvt1 c07 (critic C #4): an arc that ends where a printed rit. ramp starts slows its last beats and the
            # ramp then starts from its own (faster) tempo: check that no beat is slower than the beat after it
            print(f"  WARNING phrase arc {a}-{e} ends where a tempo ramp starts: check the tempo does not rise", file=sys.stderr)
        mid = (a + e) / 2
        slow = PHRASE_SLOW_SUB if depth == "sub" else (PHRASE_SLOW_MAIN if depth == "main" else (PHRASE_SLOW_LIGHT if depth == "light" else PHRASE_SLOW))
        if depth == "open":   # mvt1 c11 (critic C #1): the push only, no slowing (an arc that leads into an animando)
            slow = (1.0, 1.0)
        push = 1.0 if depth in ("sub", "light") else PHRASE_PUSH
        segs = [(a + 1, mid, push), (mid, e - 2, 1.0), (e - 2, e - 1, slow[0]), (e - 1, e, slow[1])]
        first = a + 1
        if any(abs(a - x_) < 0.01 for x_ in ends_done):   # c15 (C #5): the tempo returns over one beat
            segs = [(a, a + 1, PHRASE_RETURN)] + segs
            first = a
        if depth != "open" or PHRASE_RETURN_AFTER_OPEN:
            ends_done.append(e)
        cuts = sorted({q for q, _ in steps if first - EPS <= q < e - EPS} | {x for s0, s1, _ in segs for x in (s0, s1)})
        new = [(q, b) for q, b in steps if not (first - EPS <= q < e + EPS)]
        for q in cuts:
            if q >= e - EPS:
                continue
            f = next(f_ for s0, s1, f_ in segs if s0 - EPS <= q < s1 - EPS)
            new.append((q, round(val(q) * f, 3)))
        new.append((e, val(e)))
        steps = sorted(new)
        print(f"  phrase arc {a}-{e}: +{(qn_to_sec_steps(e, steps) - qn_to_sec_steps(a, steps)) - (qn_to_sec_steps(e, TEMPO_PRE_ARC) - qn_to_sec_steps(a, TEMPO_PRE_ARC)):.3f} s", file=sys.stderr)
    return steps


def qn_to_sec_steps(q, steps):
    t, lq, lb = 0.0, 0.0, steps[0][1]
    for tq, bpm in steps[1:]:
        if tq >= q:
            break
        t += (tq - lq) * 60 / lb; lq, lb = tq, bpm
    return t + (q - lq) * 60 / lb


TEMPO_PRE_ARC = list(TEMPO)
TEMPO = phrase_arcs(TEMPO)

# c16 (C #3): forward motion into crescendos and time at phrase apexes (whole-beat steps only, applied after the phrase
# arcs and before the caesuras). TEMPO_PUSH (start, end, factor): x factor from start + 1 to end, skipped where a
# RAMP_SPAN overlaps: bar 8 (21-24), bars 27-28 (78-84) and bars 75-77 into the bar 78 poco allargando (250-259; C wrote
# 244-253, but bars 75-77 are qn 250-259). APEX_AGOGIC: in each phrase arc, the beat holding the highest note of the lead
# line (the LEAD_SPANS track whose span started last at the arc's second beat) x APEX_AGOGIC, unless it is one of the
# arc's last two beats. BEAT_STRETCH: single beats (the Largamente downbeats of bars 61 and 62).
# c20 (C #4): pushes into the BCl/CA duet's mf crest (bars 32-33) and the oboe/cello p< of bars 45-46, with a held beat
# on each crest (97 x0.96, 147 x0.97 before the poco rit. of bar 47), in BEAT_STRETCH
# TEMPO_PUSH: defined before the score config is read (see SCORE CONFIG below)
APEX_AGOGIC = 0.96
# APEX_SKIP: defined before the score config is read (see SCORE CONFIG below)
# APEX_LEAD: defined before the score config is read (see SCORE CONFIG below)
# BEAT_STRETCH: defined before the score config is read (see SCORE CONFIG below)


def mult_span(steps, a, e, f):
    """Multiply the tempo over [a, e) by f (step points inside are scaled; points at a and e are added)."""
    def val(q):
        v = steps[0][1]
        for tq, b in steps:
            if tq <= q + EPS:
                v = b
        return v
    keep = [(q, b) for q, b in steps if not (a - EPS <= q < e - EPS) and abs(q - e) > EPS]
    inner = [(q, round(b * f, 3)) for q, b in steps if a + EPS < q < e - EPS]
    return sorted(keep + inner + [(a, round(val(a) * f, 3)), (e, val(e))])


def lead_track_notes(a):
    """The notes (score onset, pitch) of the lead line at arc start a (LEAD_SPANS track whose span started last)."""
    order = list(LEAD_SPANS)
    c_ = [(s0, -order.index(tn), tn) for tn, sp in LEAD_SPANS.items() for s0, e0 in sp if s0 <= a + 1 + EPS < e0]
    if a in APEX_LEAD:
        c_ = [(0, 0, APEX_LEAD[a])]
    if not c_:
        return None, []
    _, _, tn = max(c_)   # the span that started last; on a tie the first in LEAD_SPANS (Violins I before Violins II)
    tr_ = next(t for t in TRACKS if t[0] == tn)
    ns_ = [(n["qn"], n["pitch"]) for st in tr_[1] for n in notes[st]]
    if tn in TRACK_WINDOWS:
        # mvt1 c40: a note the track hands to one of its ALIAS_TRACKS (another instance, same line) is still the lead line
        al_ = [tuple(w_) for an_, a_ in ALIAS_TRACKS.items() if a_["source"] == tn and an_ not in TEST_TRACKS
               for w_ in a_["windows"]]   # mvt1 c41: not a TEST_TRACKS alias
        ns_ = [x for x in ns_ if tw_keep(tn, x[0]) or any(w0 - EPS <= x[0] < w1 - EPS for w0, w1 in al_)]
    return tn, ns_


def tempo_shaping(steps):
    for a, e, f in TEMPO_PUSH:
        if any(a < e2 - EPS and e > a2 + EPS for a2, e2, _ in RAMP_SPANS):
            print(f"  tempo push {a}-{e}: skipped (tempo ramp)", file=sys.stderr)
            continue
        steps = mult_span(steps, a + 1, e, f)
        print(f"  tempo push {a + 1}-{e}: x{f}", file=sys.stderr)
    for arc in PHRASE_ARCS:
        a, e = arc[0], arc[1]
        if any(a < e2 - EPS and e > a2 + EPS for a2, e2, _ in RAMP_SPANS):
            continue
        if a in APEX_SKIP:
            print(f"  apex {a}-{e}: skipped (APEX_SKIP)", file=sys.stderr)
            continue
        tn, ns_ = lead_track_notes(a)
        ns_ = [x for x in ns_ if a + 1 - EPS <= x[0] < e - 2 - EPS]   # not the arc's first beat or its last two
        if not ns_:
            print(f"  apex {a}-{e}: no lead line", file=sys.stderr)
            continue
        top = max(p for _, p in ns_)
        q_ = min(q for q, p in ns_ if p == top)
        b_ = float(int(q_ + EPS))
        steps = mult_span(steps, b_, b_ + 1, APEX_AGOGIC)
        print(f"  apex {a}-{e}: {tn} pitch {top} at qn {q_:.2f}, beat {b_} x{APEX_AGOGIC}", file=sys.stderr)
    for b_, f in BEAT_STRETCH.items():
        steps = mult_span(steps, b_, b_ + 1, f)
        print(f"  beat stretch {b_}: x{f}", file=sys.stderr)
    return steps


_t0 = qn_to_sec_steps(SCORE_END or 0.0, TEMPO)
TEMPO = tempo_shaping(TEMPO)
print(f"  tempo shaping: {qn_to_sec_steps(SCORE_END or 0.0, TEMPO) - _t0:+.3f} s", file=sys.stderr)


def add_caesuras(steps):
    """c04 (C #6): the 0.25 qn before each breath in CAESURA is slowed so that it lasts extra_s longer."""
    steps = list(steps)
    for q0, extra in CAESURA.items():
        def val(q):
            v = steps[0][1]
            for tq, b in steps:
                if tq <= q + EPS:
                    v = b
            return v
        a = q0 - 0.25
        b_in, b_at = val(a + 0.01), val(q0)
        if any(a + EPS < tq < q0 - EPS for tq, _ in steps):
            sys.exit(f"caesura at {q0}: tempo changes inside the slowed span")
        new = 15 / (15 / b_in + extra)
        steps = [(tq, b) for tq, b in steps if abs(tq - a) > EPS and abs(tq - q0) > EPS]
        steps += [(a, round(new, 3)), (q0, b_at)]
        steps.sort()
        print(f"  caesura {q0}: {b_in} -> {new:.3f} bpm over {a}-{q0} (+{15 / new - 15 / b_in:.3f} s)", file=sys.stderr)
    return steps


TEMPO_NC = list(TEMPO)   # c05 (A #2): the tempo map without the caesuras, for note-length tests
TEMPO = add_caesuras(TEMPO)
tempo = [list(t) for t in TEMPO]


def qn_to_sec(q, steps=None):
    steps = TEMPO if steps is None else steps
    t, lq, lb = 0.0, 0.0, steps[0][1]
    for tq, bpm in steps[1:]:
        if tq >= q:
            break
        t += (tq - lq) * 60 / lb; lq, lb = tq, bpm
    return t + (q - lq) * 60 / lb


def sec_to_qn(t):
    """c16 (A #1): the score qn at t seconds on the real tempo map (inverse of qn_to_sec; before 0 the pre-roll)."""
    if t < 0:
        return t * PREROLL_BPM / 60
    lo, hi = 0.0, END + 50
    for _ in range(60):
        mid = (lo + hi) / 2
        if qn_to_sec(mid) < t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def beat_kind(q):
    """c16 (C #4): "downbeat", "mid" (beat 3 of 4/4) or "weak", from the MIDI time signatures."""
    ts_ = [t for t in sorted(timesig) if t[0] <= q + EPS] or [(0.0, 4, 4)]
    q0, num, den = ts_[-1]
    pos = (q - q0) % (num * 4.0 / den)
    if pos < 0.01 or pos > num * 4.0 / den - 0.01:
        return "downbeat"
    if num == 4 and den == 4 and abs(pos - 2.0) < 0.01:
        return "mid"
    return "weak"


def bpm_at(q):
    b = TEMPO[0][1]
    for tq, bpm in TEMPO:
        if tq <= q + EPS:
            b = bpm
    return b


def gate_bpm(q):
    """mvt1 c25: the tempo that tempo-gated rules test (re-tongue / entry-mid leads, REP_SPLIT, short re-tongues, rest
    shortening, syncope shapes). With GATE_BPM_PRE_ARC it is read on the map before the phrase arcs and pushes (printed
    tempi and rit. ramps), so an arc's apex hold (x0.96 at 100 bpm) does not switch a rule off on one beat (c24: the
    clarinets' 637 re-tongue lead was lost at 96 bpm)."""
    steps = TEMPO_PRE_ARC if GATE_BPM_PRE_ARC else TEMPO
    b = steps[0][1]
    for tq, bpm in steps:
        if tq <= q + EPS:
            b = bpm
    return b


_FP_CACHE = {}


def fp_strings(patch, row_name="Sus MAX"):
    """mvt1 c38 (critic C #3): {MIDI key: [string at FP1, FP2, FP3, FP4]} read from a Hollywood Strings KS Master: the
    groups on `row_name` select their samples by CC70 start-mode ranges (0-38, 39-76, 77-114, 115-127), and each
    sample's path carries its string ("... S2 66.ews"; S1 = the lowest string). Keys with no CC70 condition play one
    string at every FP. None when the patch has no such groups."""
    if patch in _FP_CACHE:
        return _FP_CACHE[patch]
    import os
    sys.path.insert(0, os.path.expanduser("~/.rpr-bridge/libs/ew_ho"))
    import opus_state
    inst = opus_state.load_oib(patch)
    rows = [r["name"].lower() for r in inst.get("layerMatrix", {}).get("rows", [])]
    if row_name.lower() not in rows:
        _FP_CACHE[patch] = None
        return None
    ri = rows.index(row_name.lower())
    tab, any70 = {}, False
    for g in inst.get("groups", []):
        regs = [r for r in (g.get("regionMap") or {}).get("regions", []) if r.get("row") == ri and r.get("column") == 0]
        if not regs:
            continue
        rng = None
        for m in (g.get("startModes") or {}).get("modes", []):
            if m.get("type") == "Controller" and m.get("controller") == 70:
                rng = (m["min"], m["max"])
        for r in regs:
            mm = re.search(r" S(\d) ", (r.get("sample") or {}).get("relativePath", ""))
            if not mm:
                continue
            for k in range(r["keyMin"], r["keyMax"] + 1):
                row = tab.setdefault(k, [None] * 4)
                for i, (lo, hi) in enumerate(((0, 38), (39, 76), (77, 114), (115, 127))):
                    if rng is None or (rng[0] <= lo and hi <= rng[1]):
                        row[i] = int(mm.group(1))
            any70 |= rng is not None
    tab = {k: v for k, v in tab.items() if None not in v}
    _FP_CACHE[patch] = tab if any70 else None
    return _FP_CACHE[patch]


class _VP(list):
    """mvt3 c16: the volume-envelope item list; append() records the current rule name per item (VOL_PER_NOTE)."""
    rule = "other"

    def __init__(self, *a):
        super().__init__(*a)
        self.tags = {}

    def append(self, it):
        self.tags[id(it)] = self.rule
        super().append(it)


def qn_before(q, s):
    """c07 (C #4): the qn lying s seconds before q on the real tempo map (caesuras included). Leads were converted at the
    onset's own tempo, which made them up to 0.13 s too long after a slower span or a caesura. Before qn 0 the pre-roll
    runs at PREROLL_BPM."""
    t = qn_to_sec(q) - s
    if t < 0:
        return -(-t) * PREROLL_BPM / 60
    lo, hi = 0.0, q
    for _ in range(50):
        mid = (lo + hi) / 2
        if qn_to_sec(mid) < t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def lead_qn(q, s):
    return q - qn_before(q, s)


# ---------- events ----------
ev = collections.defaultdict(list)
SUBITO = collections.defaultdict(set)   # mvt1 c01: {staff: score qn of subito marks} (never a hairpin's target)
GRACE_ROWS = collections.defaultdict(list)   # c03: grace notes, (qn of the event, kind, values, grace offset)
for line in open(f"{BUILD}/mockup-events.tsv", encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    if len(f) < 4:
        continue
    staff, qn, grace, kind, vals = f[0], float(f[1]), float(f[2]), f[3], f[4:]
    # mvt1 c01 (B #1): "sub. p" (subito) is the dynamic itself, reached at once; DYN has no "sub. ..." keys, so every
    # subito mark was dropped and the line kept its previous level (bar 62 played loud, bar 84 ff on a printed sub. p)
    if kind == "dynamic" and vals and re.match(r"sub(ito|\.)\s*", vals[0]) and re.sub(r"^sub(ito|\.)\s*", "", vals[0]) in DYN:
        vals = [re.sub(r"^sub(ito|\.)\s*", "", vals[0])] + vals[1:]
        SUBITO[staff].add(round(qn, 3))
    # c32 (critics A #1, B #1, C #1): a compound dynamic markup ("pp espr.", "p dolce", "sub. pp molto", "molto p") is
    # the DYN word it contains plus words that are an expression text. Only exact DYN keys were read, so v621's coda
    # "pp espr." was dropped and Violins I played the pp line at the ff before it (15-27 dB loud). The dynamic word is
    # kept as the dynamic; the other words become one text event at the same qn (the event list logs each dynamic twice).
    if kind == "dynamic" and vals and vals[0] not in DYN:
        words_ = vals[0].split()
        dw_ = [w for w in words_ if w in DYN]
        if dw_:
            if any(re.match(r"^sub(ito|\.)$", w) for w in words_):
                SUBITO[staff].add(round(qn, 3))
            rest_ = " ".join(w for w in words_ if w != dw_[0] and not re.match(r"^sub(ito|\.)$", w))
            vals = [dw_[0]] + vals[1:]
            if rest_ and (qn, "text", [rest_]) not in ev[staff]:
                ev[staff].append((qn, "text", [rest_]))
        else:
            print(f"WARNING: unread dynamic {vals[0]!r} on {staff} at {qn}")
    ev[staff].append((qn, kind, vals))
    if grace != 0 and kind == "note":
        GRACE_ROWS[staff].append((qn, kind, vals, grace))
for s in ev:
    ev[s].sort(key=lambda e: e[0])
END = max(n["end"] for ns in notes.values() for n in ns)
SE = SCORE_END if SCORE_END is not None else END   # the score's last release


def spans(staff_list, kind):
    """Open/close spans (slurs) per staff -> list of (start, stop). stop = onset of the slur's last note."""
    out = []
    for s in staff_list:
        start = None
        for qn, k, v in ev[s]:
            if k != kind:
                continue
            if v[0] == "-1":
                start = qn if start is None else start
            elif v[0] == "1" and start is not None:
                out.append((start, qn)); start = None
    return out


def texts_until(staff_list, qn):
    return [(q, v[0].lower()) for s in staff_list for q, k, v in ev[s] if k == "text" and q <= qn + EPS]


def rest_starts(staff, min_rest):
    """Ends of notes followed by at least min_rest quarter notes of silence on this staff."""
    ns = sorted(notes[staff], key=lambda n: n["qn"])
    out = []
    for i, n in enumerate(ns):
        later = [o["qn"] for o in ns if o["qn"] > n["qn"] + EPS]
        nxt = min(later) if later else END + 100
        busy = any(o["qn"] < n["end"] - EPS and o["end"] > n["end"] + EPS for o in ns)
        if not busy and nxt - n["end"] >= min_rest - EPS:
            out.append(n["end"])
    return sorted(set(out))


# ---------- dynamics ----------
def hairpins_and_marks(staff_list):
    """c01: one pass per staff in time order. A hairpin closes at its own stop (either kind), at a later dynamic mark,
    at a new hairpin start, or at the next rest of 2 qn or more; every printed mark is kept."""
    marks, hps = [], []
    for s in staff_list:
        rs = rest_starts(s, 2.0)
        order = {"stop": 0, "dynamic": 1, "start": 2}
        evs = []
        for q, k, v in ev[s]:
            if k in ("cresc", "decresc") and v:
                evs.append((q, "stop" if v[0] == "1" else "start", k))
            elif k == "dynamic" and v and v[0] in DYN:
                evs.append((q, "dynamic", v[0]))
        evs.sort(key=lambda e: (e[0], order[e[1]]))
        open_hp = None

        def close_by_rest(upto):
            nonlocal open_hp
            if open_hp:
                r = [x for x in rs if open_hp[0] + EPS < x < upto - EPS]
                if r:
                    hps.append((open_hp[0], r[0], open_hp[1])); open_hp = None

        for q, typ, data in evs:
            close_by_rest(q)
            if typ == "stop":
                if open_hp:
                    hps.append((open_hp[0], q, open_hp[1])); open_hp = None
            elif typ == "dynamic":
                if open_hp and q > open_hp[0] + EPS:
                    hps.append((open_hp[0], q, open_hp[1])); open_hp = None
                if not marks or marks[-1] != (q, data):
                    marks.append((q, data))
            else:
                if open_hp:
                    hps.append((open_hp[0], q, open_hp[1]))
                open_hp = (q, data)
        if open_hp:
            r = [x for x in rs if x > open_hp[0] + EPS]
            hps.append((open_hp[0], r[0] if r else END, open_hp[1]))
    marks = sorted(set(marks))
    hps = sorted(set(h for h in hps if h[1] > h[0] + EPS))
    return marks, hps


# c05 (A #4): dynamics printed once on a shared staff that the extraction gives to one voice only: {track: [(qn, mark)]}
# SHARED_DYN: defined before the score config is read (see SCORE CONFIG below)


def base_points(staff_list, extra_marks=(), extra_hps=(), niente=False):
    marks, hps = hairpins_and_marks(staff_list)
    if extra_marks:
        marks = sorted(set(marks) | set(extra_marks))
    if extra_hps:   # mvt1 c34 (B #1): SHARED_HP
        hps = sorted(set(hps) | {(float(a_), float(b_), k_) for a_, b_, k_ in extra_hps})
    ons_all = sorted(n_["qn"] for s_ in staff_list for n_ in notes[s_])   # mvt1 c34: HP_NIENTE
    first_note = min((n["qn"] for s in staff_list for n in notes[s]), default=0.0)
    level = DYN["p"]
    if marks and marks[0][0] <= first_note + 0.01:
        level = DYN[marks[0][1]]
    pts = [(0.0, level)]
    events = [(q, 0, "mark", d) for q, d in marks] + [(a, 1, "hp", (b, k)) for a, b, k in hps]
    events.sort(key=lambda e: (e[0], e[1]))
    sf_hp = {}   # c02: sf followed by a decrescendo: spike, then the hairpin starts from min(level, mf) at q + 0.5
    fp_hp = {}   # mvt3 c09: FP_SPIKE_AT_MARK: a hairpin printed at an fp / sfp starts where the attack has fallen
    hold_after = None
    anchor = level   # c32: the level of the last printed mark (HP_SWELL_CEIL)
    last_un = None   # c09 (B #3): (stop, start level, kind) of the last untargeted hairpin
    short_ret = None   # mvt1 c09 (A #1): (stop, crest) of the last short mdv decrescendo
    for q, _, kind, data in events:
        if kind == "mark":
            last_un = None
            if data in ("sf", "sfz"):
                hp_here = any(k == "decresc" and q - EPS <= a <= q + 0.25 for a, b, k in hps)
                # c04 (A #3): from f or louder the sf is +8 (ff 114 -> 122), and it holds through the tremolo's attack
                spike = min(124, level + 8) if level >= DYN["f"] else min(124, max(DYN["sf"], level + 12))
                arr_ = next((DYN[d_] for k_, d_ in SF_ARRIVAL_AT.items() if abs(q - k_) < 0.02), None)
                if arr_ is not None and arr_ > level:
                    # mvt1 c04 (C #5): an sf arrival (bar 41: f < sf > mf): spike to the arrival dynamic, then arrival - 8
                    post = arr_ - 8
                    pts += [(q, level), (q + 0.02, arr_), (q + 0.25, arr_ - 4), (q + 0.75, post)]
                    level = post
                    if hp_here:
                        sf_hp[q] = q + 0.75
                    continue
                if hp_here:
                    # c06 (C #2): from f or louder the sf falls 10 CC (was to mf: ff 114 -> 72 in 0.75 qn, -8 dB in one
                    # beat), so the printed decrescendo carries the rest of the fall across the bar
                    loud = level >= DYN["f"]
                    post = level - 10 if loud else min(level, DYN["mf"])
                    pts += [(q, level), (q + 0.02, spike), (q + 0.25, spike - (4 if loud else 6)), (q + 0.75, post)]
                    level = post
                    sf_hp[q] = q + 0.75
                else:
                    pts += [(q, level), (q + 0.02, spike), (q + 0.75, level)]
                continue
            if data in ("fp", "sfp") and FP_SPIKE:
                # mvt1 c11 (critic A #5): an fp is a short f attack falling to p (DYN["fp"] alone went straight to p:
                # the basses' fp at bar 33 had no attack and bloomed over the bassoon solo)
                # mvt3 port: sfp (the Finale's bar 149) is the same with an SFP_SPIKE_HI attack, falling to DYN["sfp"]
                hi_, hold_, fall_ = FP_SPIKE
                if data == "sfp":
                    hi_ = SFP_SPIKE_HI
                    if SFP_SPIKE_S:   # mvt3 c02 (critic C #3): seconds, not qn
                        hold_ = sec_to_qn(qn_to_sec(q) + SFP_SPIKE_S[0]) - q
                        fall_ = sec_to_qn(qn_to_sec(q) + SFP_SPIKE_S[1]) - q
                elif FP_SPIKE_S:   # mvt3 c09 (critic A #1): the fp's hold and fall in seconds too (0.12 / 0.25 qn = 41 / 86 ms at 168 qpm)
                    hold_ = sec_to_qn(qn_to_sec(q) + FP_SPIKE_S[0]) - q
                    fall_ = sec_to_qn(qn_to_sec(q) + FP_SPIKE_S[1]) - q
                # mvt3 c09 (critic A #1): FP_SPIKE_AT_MARK: the attack level starts at the mark itself (a step), so a
                # led note's pull (CC held from its moved note-on to the score onset) and the timpani's first CC7 point
                # read the attack level; with the old 0.02 qn ramp they read the level after the fall (the p layer)
                t0_ = q if FP_SPIKE_AT_MARK else q + 0.02
                pts += [(q, level), (t0_, max(DYN[hi_], level)), (q + hold_, max(DYN[hi_], level)), (q + fall_, DYN[data])]
                FP_CHECK_AT[round(q, 3)] = q + fall_   # mvt3 c03: the mark's level is checked after the attack
                if FP_SPIKE_AT_MARK:
                    fp_hp[q] = q + fall_
                level = DYN[data]
                anchor = level
                continue
            if hold_after and hold_after[0] - EPS <= q <= hold_after[1] + EPS and DYN[data] > level \
                    and not (HOLD_AFTER_KEEP_CRESC_START and any(k_ == "cresc" and abs(a_ - q) < 0.02 for a_, b_, k_ in hps)):
                continue   # c06 (C #3): a mark just after a decrescendo that was turned downward does not raise it
            pts.append((q, level))   # hold the previous level up to the mark (no ramps between marks)
            level = DYN[data]
            anchor = level
            pts.append((q, level))
        else:
            stop, hk = data
            tgt = next((DYN[d] for mq, d in marks if stop - 0.01 <= mq <= stop + 1.0 and d not in ("sf", "sfz")
                        and not any(round(mq, 3) in SUBITO[s_] for s_ in staff_list)), None)
            start = level
            if tgt is None:   # c26 (B #2): a listed untargeted hairpin goes to this dynamic
                hta_ = next((d_ for s_ in staff_list for k_, d_ in HP_TARGET_AT.get(s_, {}).items() if abs(q - k_) < 0.02),
                            None)
                tgt = DYN[hta_] if hta_ else None
            if tgt is None and HP_SF_TARGET and hk == "cresc" \
                    and (HP_SF_TARGET.get("staves") is None or any(s_ in HP_SF_TARGET["staves"] for s_ in staff_list)) \
                    and any(stop - 0.01 <= mq <= stop + 0.26 and d in ("sf", "sfz") for mq, d in marks):
                # mvt1 c38 (critic A #3): a crescendo into an sf has no printed target (sf is skipped above), so it rose one
                # hairpin step: the trombones' p < sf at bar 40 reached CC1 64 (about mf) and grew 2.8-5.6 dB while the
                # master grew 0.3 dB into the bar-41 sf. It now targets "to" (f), or "from_f" (ff) when it starts at f
                tgt = DYN[HP_SF_TARGET.get("from_f", "ff") if level >= DYN["f"] - 2 else HP_SF_TARGET.get("to", "f")]
                hp_sf_targeted.append((",".join(staff_list), round(q, 3), round(stop, 3)))
            untargeted = tgt is None
            nien_ = None   # mvt1 c34 (C #3a): HP_NIENTE target, and the one-step level the line returns to
            if tgt is None:
                step = HP_STEP_SOFT if level <= DYN["mp"] + 2 else HP_STEP
                tgt = level + (step if hk == "cresc" else -step)
                mdv = last_un and last_un[2] != hk and abs(q - last_un[0]) <= 0.3
                if niente and HP_NIENTE and hk == "decresc" and not mdv \
                        and not any(stop - 0.01 <= o_ <= stop + HP_NIENTE["rest_qn"] for o_ in ons_all):
                    nien_ = (max(10, level - HP_NIENTE["steps"] * step), max(10, level - step))
                if mdv:
                    # c09 (B #3): an untargeted < > (or > <) returns to where the first hairpin started (a 22 CC
                    # crescendo followed by a 14 CC decrescendo left the line one level higher). The next-mark limit
                    # below does not apply (Vln I bar 73-75: p < > then mp; it held the line at CC 58 until the mp)
                    tgt = last_un[1]
                short_hp = HP_SHORT_S is not None and hk in HP_SHORT_KINDS and qn_to_sec(stop) - qn_to_sec(q) <= HP_SHORT_S
                if HP_MDV_FIRST and mdv:
                    short_hp = False   # c32: the messa di voce returns to its start
                if short_hp:   # mvt1 c09 (A #1)
                    tgt = max(tgt, level - HP_STEP_SHORT) if hk == "decresc" else min(tgt, level + HP_STEP_SHORT)
                    if hk == "decresc":
                        short_ret = (stop, level)   # the level the short > came down from
                elif short_ret and hk == "cresc" and q - short_ret[0] <= HP_SHORT_RET_QN:
                    # mvt1 c09 (A #1): the next untargeted < after a short > goes back to that crest, not a full step
                    # over the lowered level (Horn 1 bar 48: 75 -> 88, over the first swell's 81)
                    tgt = min(tgt, max(level, short_ret[1]))
                # c06 (C #3): an untargeted hairpin does not overshoot the next printed mark in its own direction
                # (Cl2 bar 90: pp -> CC 12, under the ppp printed two bars later)
                nm = None if mdv else next((DYN[d] for mq, d in marks if stop + 1.0 < mq <= stop + 6.0
                                            and d not in ("sf", "sfz")), None)
                if nm is not None and hk == "decresc" and nm < level:
                    tgt = max(tgt, nm)
                elif nm is not None and hk == "cresc" and nm > level:
                    tgt = min(tgt, nm)
                elif nm is None and not mdv and hk == "cresc":
                    # c11 (B #3): a louder mark further on (up to the next rest of 2 qn or more, at most 16 qn): the
                    # untargeted swell stays 8 CC under it (Vln I/II bar 23: CC 58 -> 80, over the printed mf goal at
                    # qn 82, which then sounded no louder than the phrase's start)
                    hz = min([stop + 16.0] + [x for s_ in staff_list for x in rest_starts(s_, 2.0) if x > stop + EPS])
                    # mvt1 c02 (C #3): the look-ahead stops at the first later mark that is softer than the current
                    # level or subito: the f four bars on, past a sub. p, capped the bars 60-61 crescendo at CC 80 and
                    # it measured -5.4 dB (backwards) on Violins I
                    if NM2_STOP_SOFT:
                        hz = min([hz] + [mq for mq, d in marks if stop - 0.01 <= mq <= hz and d in DYN and d not in ("sf", "sfz")
                                         and (DYN[d] < level or any(round(mq, 3) in SUBITO[s_] for s_ in staff_list))])
                    nm2 = next((DYN[d] for mq, d in marks if stop + 1.0 < mq <= hz and d not in ("sf", "sfz")), None)
                    # From p or softer only the overshoot is removed (cap at the mark itself): a -8 margin there cut
                    # Hn1's bar 7 p swell from CC 68 to 52 in a trial build
                    if nm2 is not None and nm2 > level:
                        tgt = min(tgt, max(level + 6, nm2 - 8) if level >= DYN["mp"] - 2 else nm2)
                if HP_SWELL_CEIL is not None and hk == "cresc":
                    # c32: no ratchet: at most one step over the last printed mark, and under "max" unless printed louder
                    ceil_ = anchor + (HP_STEP_SOFT if anchor <= DYN["mp"] + 2 else HP_STEP)
                    if HP_SWELL_CEIL.get("max") is not None:
                        ceil_ = min(ceil_, max(HP_SWELL_CEIL["max"], anchor))
                    tgt = min(tgt, max(level, ceil_))
                if nien_ is not None:
                    tgt = nien_[0]   # no short-hairpin cap, no next-mark limit
            elif hk == "decresc" and tgt >= level:
                # c06 (C #3): a decrescendo whose printed target is not below the current level still falls (6 CC);
                # the mark at its end then does not raise the level again
                tgt = level - 6
                restate_ = HP_DIM_RESTATE and any(abs(mq - stop) < 0.011 and d not in ("sf", "sfz") for mq, d in marks) \
                    and any(abs(o_ - stop) < 0.011 for o_ in ons_all)
                if not restate_:   # mvt3 c03: HP_DIM_RESTATE (the mark at the stop restates on a new note)
                    hold_after = (stop - 0.01, stop + 1.0)
            elif hk == "cresc" and abs(tgt - level) < EPS and HP_SWELL_AT_MARK \
                    and any(abs(mq - q) < 0.011 and d not in ("sf", "sfz") for mq, d in marks):
                # mvt3 c03: HP_SWELL_AT_MARK: a swell from the printed mark at the hairpin's start
                step_ = HP_STEP_SOFT if level <= DYN["mp"] + 2 else HP_STEP
                if HP_SHORT_S is not None and qn_to_sec(stop) - qn_to_sec(q) <= HP_SHORT_S:
                    step_ = min(step_, HP_STEP_SHORT)
                tgt = level + step_
                if HP_SWELL_CEIL is not None and HP_SWELL_CEIL.get("max") is not None:
                    tgt = min(tgt, max(HP_SWELL_CEIL["max"], level))
            elif hk == "cresc" and abs(tgt - level) < EPS:
                start = level - 12   # c06 (C #3): "niente <" to the current level starts 12 CC lower
            tgt = max(10, min(124, tgt))
            q = next((v for k, v in sf_hp.items() if k - EPS <= q <= k + 0.25), q)
            # mvt3 c09: "sfp <": the crescendo starts from the p after the attack (its (q, level) points at the mark
            # overwrote the attack step, so every led note still started on the p layer)
            q = next((v for k, v in fp_hp.items() if k - EPS <= q <= k + 0.25 and v < stop - EPS), q)
            pts += [(q, level), (q, max(10, start))]
            if HP_CURVE and stop - q >= HP_CURVE.get("min_qn", 1.0) - EPS \
                    and not any(s_ in HP_CURVE.get("skip_staves", ()) for s_ in staff_list):   # mvt3 c09: e.g. timpani rolls stay linear
                # mvt3 c07 (research batch 5 item 3, Mulan / Howl Synchron hairpins): a crescendo rises early, then
                # settles into its target; a diminuendo holds and falls on its last held note
                st_ = max(10, start)
                if hk == "cresc" and HP_CURVE.get("cresc"):
                    fx_, fy_ = HP_CURVE["cresc"]
                    pts.append((q + fx_ * (stop - q), st_ + fy_ * (tgt - st_)))
                elif hk == "decresc" and HP_CURVE.get("decresc_last") \
                        and stop - q <= HP_CURVE.get("decresc_last_max_qn", 1e9) + EPS:
                    # mvt3 c14 (critic C #2): "decresc_last_max_qn": a longer diminuendo stays linear (linear CC11 is
                    # already late-weighted in dB); "decresc_last_min_s": a last onset closer to the stop than this is
                    # not used (the previous onset that qualifies, else linear). A 12 qn diminuendo whose last onset
                    # was an eighth before its end kept 65 % of the fall for the last 0.22 s (a 10 dB step)
                    ms_ = HP_CURVE.get("decresc_last_min_s", 0.0)
                    lo_ = max([o_ for o_ in ons_all if q + 0.25 * (stop - q) <= o_ < stop - 0.25 - EPS
                               and (not ms_ or qn_to_sec(stop) - qn_to_sec(o_) >= ms_ - 1e-6)], default=None)
                    if lo_ is not None:
                        pts.append((lo_, st_ + HP_CURVE["decresc_last"] * (tgt - st_)))
            pts.append((stop, tgt))
            if nien_ is not None:
                # mvt1 c34 (C #3a): the line comes back before any printed mark or hairpin: it re-enters at the one-step
                # level (as before HP_NIENTE), not two steps down
                nx_ = next((o_ for o_ in ons_all if o_ > stop + EPS), None)
                if nx_ is not None and not any(stop + EPS < e_[0] < nx_ + 0.01 for e_ in events):
                    pts += [(nx_ - 0.06, tgt), (nx_ - 0.05, nien_[1])]
                    last_un = None
                    level = nien_[1]
                    continue
            last_un = (stop, level, hk) if untargeted else None
            if HP_LONE_RETURN and untargeted and hk == "cresc" and tgt > anchor and stop - q <= HP_LONE_RETURN["max_qn"] + EPS:
                # c32 (C #2): a lone untargeted swell (no hairpin or mark within ret_qn after it) returns to the printed level
                r_ = HP_LONE_RETURN["ret_qn"]
                if not any(stop - EPS <= e_[0] <= stop + r_ + EPS for e_ in events):
                    pts += [(stop + r_ / 2, tgt), (stop + r_, max(anchor, start))]
                    last_un = None
                    level = max(anchor, start)
                    continue
            level = tgt
    pts.sort(key=lambda p: p[0])   # stable: points at the same qn keep their order
    return pts, marks, hps


def value_at(pts, q):
    """Piecewise-linear curve through pts (later points at the same qn win)."""
    v = pts[0][1]
    for (q0, v0), (q1, v1) in zip(pts, pts[1:]):
        if q1 <= q + EPS:
            v = v1
            continue
        if q0 <= q + EPS < q1:
            return v0 + (v1 - v0) * (q - q0) / (q1 - q0) if q1 - q0 > EPS else v1
    return v


def sample(fn, breaks):
    grid = sorted(set([round(x, 4) for x in breaks] + [round(i * 0.125, 4) for i in range(int((END + 4) / 0.125))]))
    out, last = [], None
    for q in grid:
        v = int(round(max(1, min(127, fn(q)))))
        if v != last:
            out.append((q, v)); last = v
    return out


# ---------- per-track articulation ----------
_ACC_STAVES = {}
_HP_REL_CACHE = {}


def _accent_staves():
    """mvt3 c18: {score qn: number of staves that print an accent / marcato there} (INSTR_POST accent tutti_scale)"""
    if not _ACC_STAVES:
        for s_, l_ in ev.items():
            for q_ in {round(q, 3) for q, k, v in l_ if k == "script" and v[0] in ("accent", "marcato")}:
                _ACC_STAVES[q_] = _ACC_STAVES.get(q_, 0) + 1
        _ACC_STAVES[-1] = 0
    return _ACC_STAVES


def build_track(tname, staves, patch, family, pan):
    stem = patch.rsplit("/", 1)[1][:-4]
    ns = sorted([dict(n, staff=s) for s in staves for n in notes[s]], key=lambda n: (n["qn"], n["pitch"]))
    if tname in TRACK_WINDOWS:   # c10 (A #1)
        ns = [n for n in ns if tw_keep(tname, n["qn"])]
    split_away = []   # c13 (A #1)
    for tsp_, (src_, wins_, pmin_) in TRACK_SPLITS.items():
        if tname not in (tsp_, src_):
            continue
        ns0_ = list(ns)
        if pmin_ == "rank":
            insp_ = lambda n, w=wins_: any(a - EPS <= n["qn"] < b - EPS for a, b in w) and any(
                o is not n and abs(o["qn"] - n["qn"]) < 0.01 and o["pitch"] < n["pitch"] for o in ns0_)
        else:
            insp_ = lambda n, w=wins_, p=pmin_: n["pitch"] >= p and any(a - EPS <= n["qn"] < b - EPS for a, b in w)
        if tname == src_:
            split_away = [n for n in ns if insp_(n)]
        ns = [n for n in ns if insp_(n) == (tname == tsp_)]
    flag_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] == "flageolet"}
    if family == "harp" and tname in HARM_ON_TRACK:   # mvt3 c01 (critic A #5): harmonics on the harp track, sounding pitch
        for n in ns:
            if any(abs(n["qn"] - q) < EPS for q in flag_q):
                n["pitch"] += HARM_ON_TRACK[tname]
                n["harm_on"] = True
    elif family == "harp":   # harmonics go to their own track
        ns = [n for n in ns if not any(abs(n["qn"] - q) < EPS for q in flag_q)]
    if family == "harm":   # only the sounding (upper) pitch of each harmonic; the written pitch is an octave lower
        ns = [n for n in ns if any(abs(n["qn"] - q) < EPS for q in flag_q)]
        ns = [n for n in ns if n["pitch"] == max(o["pitch"] for o in ns if abs(o["qn"] - n["qn"]) < EPS)]
    slurs = spans(staves, "slur")

    # c03 (C #2): after-grace notes (event rows with a negative grace offset) come out of the MIDI a quarter beat before
    # their main note with a gap after them. Re-place them so that they end on the main note, GRACE_S each.
    if family in ("wind", "brass", "string"):
        gev = collections.defaultdict(list)
        for s_ in staves:
            for line_q, kind, vals, gr in GRACE_ROWS.get(s_, []):
                gev[line_q].append((gr, int(vals[0])))
        for gq, rows in gev.items():
            rows = sorted(set(rows))
            targets = [n for n in ns if n["qn"] >= gq - EPS and n["end"] - n["qn"] > 0.2]
            if not targets:
                continue
            tgt = min(targets, key=lambda n: n["qn"])
            g = GRACE_S * bpm_at(tgt["qn"]) / 60
            used = []
            for k, (gr, pitch) in enumerate(rows):
                cand = [n for n in ns if n["pitch"] == pitch and gq - 1 < n["qn"] < tgt["qn"] and n["end"] - n["qn"] < 0.2
                        and id(n) not in used]
                if not cand:
                    continue
                gn = cand[0]
                used.append(id(gn))
                gn["qn"] = tgt["qn"] - (len(rows) - k) * g
                gn["end"] = gn["qn"] + g
                gn["grace"] = id(tgt)
                gn["vel"] = 127
            if used:
                tgt["grace_target"] = True
        ns.sort(key=lambda n: n["qn"])

    def slur_of(q):
        return next((i for i, (a, b) in enumerate(slurs) if a - EPS <= q <= b + EPS), None)

    def same_slur(n, o):   # c16 (A #4): o is in n's slur, or in the slur that starts on n's tied continuation
        return o["slur"] is not None and (o["slur"] == n["slur"] or o["slur"] == n.get("slur_out"))

    trem_q = {q for s in staves for q, k, v in ev[s] if k == "tremolo"}
    meas_trem = []   # mvt1 c13 (A #1): score onsets of measured tremolos expanded into strokes
    if MEAS_TREM and family == "string":
        tv_ = {q: int(v[0]) for s in staves for q, k, v in ev[s] if k == "tremolo" and v and str(v[0]).isdigit()}
        out_ = []
        mt_next_ = [0, 0]   # stroke index (within the current note) of the next run start, run counter
        mt_rng_ = [None, []]   # mvt1 c15 (A #4): alternation generator, rows so far (True = alt_row)
        for n in ns:
            val_ = next((v_ for q_, v_ in tv_.items() if abs(q_ - n["qn"]) < EPS), None)
            sub_ = 4.0 / val_ if val_ else None
            if val_ and val_ <= MEAS_TREM["max_value"] and sub_ * 60.0 / bpm_at(n["qn"]) >= MEAS_TREM["min_s"] - EPS \
                    and n["end"] - n["qn"] >= 2 * sub_ - EPS:
                k_ = int(round((n["end"] - n["qn"]) / sub_))
                for i_ in range(k_):
                    st_ = dict(n, qn=round(n["qn"] + i_ * sub_, 6),
                               end=round(n["end"] if i_ == k_ - 1 else n["qn"] + (i_ + 1) * sub_, 6), meas_trem=True)
                    if MEAS_TREM.get("rr_runs") and i_ == mt_next_[0]:   # mvt1 c14 (A #2): a CC36 reset starts a run
                        st_["rr_start"] = True
                        mt_next_[0] += MEAS_TREM["rr_runs"][mt_next_[1] % len(MEAS_TREM["rr_runs"])]
                        mt_next_[1] += 1
                    if MEAS_TREM.get("alt_row"):   # mvt1 c15 (A #4): seeded irregular row alternation
                        if mt_rng_[0] is None:
                            mt_rng_[0] = __import__("random").Random(MEAS_TREM.get("alt_seed", 464))
                        alt_ = mt_rng_[0].random() < MEAS_TREM.get("alt_share", 0.45)
                        run_ = mt_rng_[1]
                        if len(run_) >= MEAS_TREM.get("alt_max_run", 3) and all(r_ == alt_ for r_ in run_[-MEAS_TREM.get("alt_max_run", 3):]):
                            alt_ = not alt_
                        run_.append(alt_)
                        st_["mt_alt"] = alt_
                    out_.append(st_)
                mt_next_[0] -= k_   # runs continue across the expanded notes of one tremolo passage
                trem_q = {q_ for q_ in trem_q if abs(q_ - n["qn"]) > EPS}
                meas_trem.append(round(n["qn"], 3))
            else:
                out_.append(n)
        ns = sorted(out_, key=lambda n: (n["qn"], n["pitch"]))
    accent_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] in ("accent", "marcato")}
    stacc_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] in ("staccato", "staccatissimo")}
    ten_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] == "tenuto"}
    breath_q = sorted({q for s in staves for q, k, v in ev[s] if k == "breathe"})
    near = lambda q, qs: any(abs(q - x) < EPS for x in qs)

    def has(t, w):
        return re.search(r"(?<![a-z])" + re.escape(w), t) is not None

    def text_state(q, on_words, off_words, st_list=None):
        st = False
        for tq, t in sorted(texts_until(st_list or staves, q)):
            if any(has(t, w) for w in off_words): st = False
            if any(has(t, w) for w in on_words): st = True
        return st

    def polyphonic(n):
        return any(o is not n and o["qn"] < n["end"] - EPS and o["end"] > n["qn"] + EPS for o in ns)

    def in_sost(q):
        return any(a - EPS <= q < b - EPS for a, b in SOSTENUTO_SPANS)

    def in_fast_leg(q):   # c14 (A #3)
        return any(a - EPS <= q < b - EPS for a, b in FAST_LEG.get(tname, []))

    def in_stacleg(q):   # c16 (A #3); mvt1 c20 (critic A #1): a span may name its own row, (a, b, art)
        for sp_ in STACLEG_SPANS.get(tname, []):
            if sp_[0] - EPS <= q < sp_[1] - EPS:
                return sp_[2] if len(sp_) > 2 else STACLEG_ART
        return None

    def in_detache(q):   # c15 (A #5)
        return any(a - EPS <= q < b - EPS for a, b in DETACHE_SPANS.get(tname, []))

    def in_marc(q):   # c14 (A #1)
        return any(a - EPS <= q < b - EPS for a, b in MARCATO_SPANS.get(tname, []))

    # c08 (B #4): the harmonics read the dynamics of both harp staves (the bar 82 p is printed on the lower staff)
    dyn_staves = ["HarpR", "HarpL"] if family == "harm" else staves
    pts, marks, hps = base_points(dyn_staves, SHARED_DYN.get(tname, ()), SHARED_HP.get(tname, ()),
                                  niente=family in ("wind", "brass", "string")) if ns else ([(0.0, DYN["p"])], [], [])
    base = lambda q: value_at(pts, q)

    has_bc = family == "string" and any(a["name"] == "Leg BC MAX" for a in ksmaps.get(stem, {}).get("articulations", []))
    tie_slurred = []

    def short_into_long(n):
        """mvt1 c01 (A #1, test): the first note of a slur, short, slurred into a long note (a pickup into its downbeat)
        stays on the legato row with its target. On Sus MAX the pickup sat a median 2.4-3.5 dB over the Leg Slur MAX
        target it led to (the two rows' sustains differ at one CC11), so the theme accented its upbeat."""
        if SHORT_SUS_TO_LONG is None or n["slur"] is None:
            return False
        if any(o is not n and o.get("slur", slur_of(o["qn"])) == n["slur"] and o["qn"] < n["qn"] - EPS for o in ns):
            return False
        nx_ = [o for o in ns if o is not n and abs(o["qn"] - n["end"]) < 0.05 and slur_of(o["qn"]) == n["slur"]]
        return len(nx_) == 1 and nx_[0]["end"] - nx_[0]["qn"] >= SHORT_SUS_TO_LONG - EPS
    # mvt1 c02 (A #1): repeated accented unslurred notes (hammer strokes) are detached; strings need a down-bow on both
    down_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] == "downbow"}
    det_cut, det_str = set(), set()
    if DETACH_ACCENTS and family in ("wind", "brass", "string"):
        for n in ns:
            q = n["qn"]
            if q not in accent_q or slur_of(q) is not None or n["end"] - q < DETACH_ACCENTS["min_len_qn"] - EPS \
                    or n["end"] - q > DETACH_ACCENTS["max_len_qn"] + EPS:
                continue
            nx_ = [o for o in ns if abs(o["qn"] - n["end"]) < 0.01]
            if not nx_ or not all(o["qn"] in accent_q and slur_of(o["qn"]) is None for o in nx_):
                continue
            if family == "string" and not (near(q, down_q) and all(near(o["qn"], down_q) for o in nx_)):
                continue
            det_cut.add(id(n))
            if family == "string":
                det_str.add(id(n)); det_str.update(id(o) for o in nx_)
    sus_like = lambda a_: bool(a_) and (a_ == "Sus MAX" or a_ == "Tremolo" or a_.startswith("Stac"))

    def slur_start_ok(n):
        """mvt1 c15 (critic A #2): n is a short first note of a slur after another note of the track (SLUR_START_SUS)"""
        q, s_ = n["qn"], slur_of(n["qn"])
        if s_ is None or polyphonic(n) or near(q, ten_q) or q in accent_q or n["end"] - q > SLUR_START_SUS["max_qn"] + EPS:
            return False
        sn_ = sorted([o for o in ns if o is not n and slur_of(o["qn"]) == s_], key=lambda o: o["qn"])
        if any(o["qn"] < q - EPS for o in sn_) or not sn_:
            return False
        n2_ = sn_[0]
        if abs(n2_["qn"] - n["end"]) > 0.02 or n2_["pitch"] == n["pitch"] or polyphonic(n2_) \
                or near(n2_["qn"], ten_q) or n2_["qn"] in accent_q:
            return False
        return any(o is not n and o["qn"] < q - EPS and q - SLUR_START_SUS["after_qn"] - EPS <= o["end"] <= q + EPS
                   for o in ns)
    # mvt1 c04 (critic A #1): written-out unslurred repeated notes in a fast tempo (the celli's accelerando G of bars
    # 127-130: quarters, eighths, triplets, sixteenths) are separate bow strokes. On the legato row they were merged
    # into one held note with CC11 notches (48 notes -> 3, the sixteenths 1.1 dB per note). A run is two or more
    # same-pitch unslurred monophonic notes that abut, each REP_SPLIT["max_qn"] or shorter (a longer last note joins the
    # run), at REP_SPLIT["min_bpm"] or faster; its notes play Sus MAX fresh strokes (Stac under "stac_s" seconds: triplets
    # and sixteenths at 126; unslurred eighths of a detache accompaniment, 0.24 s, stay Sus MAX).
    rep_ids = set()
    if REP_SPLIT and family == "string" and has_bc:
        def _rep_ok(n_):
            return slur_of(n_["qn"]) is None and not polyphonic(n_) and n_["qn"] not in trem_q \
                and not text_state(n_["qn"], ["pizz"], ["arco"]) and gate_bpm(n_["qn"]) >= REP_SPLIT["min_bpm"] - EPS
        for n_ in ns:
            if n_["end"] - n_["qn"] > REP_SPLIT["max_qn"] + EPS or not _rep_ok(n_):
                continue
            for o_ in ns:
                if o_ is not n_ and o_["pitch"] == n_["pitch"] and (abs(o_["qn"] - n_["end"]) < 0.01
                                                                     or abs(o_["end"] - n_["qn"]) < 0.01) \
                        and _rep_ok(o_) and (o_["end"] - o_["qn"] <= REP_SPLIT["max_qn"] + EPS or o_["qn"] > n_["qn"]):
                    rep_ids.add(id(n_))
                    rep_ids.add(id(o_))
    # mvt1 c16 (critic A #1): pickups after a rest into a legato-row note (PICKUP_SUS)
    pickup_ids = set()
    if PICKUP_SUS and family in PICKUP_SUS["families"]:
        dstr_ = {k_ for k_ in DOWNBOW_STROKE_AT.get(tname, [])}
        for n in ns:
            q = n["qn"]
            s_ = slur_of(q)
            if q < 0.5 or polyphonic(n) or near(q, ten_q) or q in accent_q or q in trem_q or near(q, stacc_q) \
                    or n.get("grace") or n.get("grace_target") or n["end"] - q > PICKUP_SUS["max_qn"] + EPS:
                continue
            if family == "string" and text_state(q, ["pizz"], ["arco"]):
                continue
            if any(o is not n and o["qn"] < q - EPS and o["end"] > q - PICKUP_SUS["rest_qn"] + EPS for o in ns):
                continue
            nx_ = [o for o in ns if o is not n and abs(o["qn"] - n["end"]) <= 0.02 + EPS]
            if len(nx_) != 1:
                continue
            o = nx_[0]
            so_ = slur_of(o["qn"])
            if o["pitch"] == n["pitch"] or polyphonic(o) or o["qn"] in trem_q or near(o["qn"], stacc_q) \
                    or near(o["qn"], ten_q) or o["end"] - o["qn"] < PICKUP_SUS.get("min_target_qn", 0.5) - EPS \
                    or id(o) in det_str or id(o) in rep_ids or any(abs(o["qn"] - k_) < 0.02 for k_ in dstr_):
                continue
            if s_ is not None:
                if so_ != s_:
                    continue
            elif not (family == "string" and has_bc and so_ is None and not o["qn"] in accent_q):
                continue
            pickup_ids.add(id(n))
    for n in ns:
        q = n["qn"]
        n["slur"] = slur_of(q)
        if id(n) in pickup_ids:
            # mvt1 c16 (critic A #1): the pickup is tongued / bowed on the Sus row and joined into its target
            n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib", "Sus Non Vib MAX")[0]
            n["slur_start_sus"] = True
            n["pickup_sus"] = True
            continue
        if family == "string":
            # c16 (A #4): a slur that starts on a tied continuation (the MIDI merges the tie into this note) is this
            # note's outgoing slur, so the join to the slur's next note is inside the slur (Vln I/II bar 80:
            # bes4~ | bes4( aes2) played the A flat as a Leg BC slur-to-slur join)
            k_ = next((i_ for i_, (a_, b_) in enumerate(slurs) if q + 0.25 < a_ < n["end"] - EPS), None)
            if k_ is not None:
                # only the outgoing join: setting n["slur"] itself turned the violas' unslurred ff entry at qn 262 (a
                # 14-semitone leap, played Sus MAX) into a first Leg Slur MAX note, 6-9 dB under its c15 level (c16)
                n["slur_out"] = k_
                tie_slurred.append(round(q, 3))
        if family in ("harp", "harm"):
            # mvt3 c21 (critic A c21 #4): a harp on a KS Master takes its rows from ART_SPANS (Harmonics, Gliss Technique;
            # the whole piece on "Sus RR" by a last span); without spans the harp keeps no articulation
            sp_ = next((x_ for x_ in ART_SPANS.get(tname, []) if x_["from"] - EPS <= q < x_["to"] - EPS), None)
            n["art"] = ks_lookup(stem, sp_["art"])[0] if sp_ is not None and stem in ksmaps else None
            continue
        if family == "timp":
            n["art"] = ks_lookup(stem, TIMP_ROW(stem, "Rls"))[0] if q in trem_q else ks_lookup(stem, TIMP_ROW(stem, "Lng"))[0]
            continue
        if n.get("grace") or n.get("grace_target"):   # c03: the run and its target on one legato articulation
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
            continue
        st_ = next((x_ for x_ in STEADY_LINE.get(tname, []) if x_["from"] - EPS <= q < x_["to"] - EPS), None)
        if st_ is not None and (st_.get("poly") or not polyphonic(n)) and q not in trem_q \
                and (st_.get("stacc") or q not in stacc_q) \
                and (st_.get("max_len_qn") is None or n["end"] - q <= st_["max_len_qn"] + EPS) \
                and not (family == "string" and text_state(q, ["pizz"], ["arco"])):
            # mvt3 c15 (mvt1 c54): STEADY_LINE (see the default): one row here, note-on and end after the lead rules
            row_ = next((v_ for k_, v_ in st_.get("at", {}).items() if abs(q - float(k_)) < 0.02), {})
            n["art"] = ks_lookup(stem, row_.get("art", st_["art"]))[0]
            n["steady"] = st_
            n["steady_row"] = row_
            n["steady_wend"] = n["end"]
            continue
        sp_ = next((x_ for x_ in ART_SPANS.get(tname, []) if x_["from"] - EPS <= q < x_["to"] - EPS
                    and (x_.get("mark") != "staccato" or q in stacc_q)), None)
        if sp_ is not None and ((sp_.get("max_qn") is not None and n["end"] - q > sp_["max_qn"] + EPS)
                                or (sp_.get("min_qn") is not None and n["end"] - q < sp_["min_qn"] - EPS)   # mvt3 c19: only held notes
                                or (sp_.get("unslurred") and n.get("slur") is not None)):
            sp_ = None   # mvt3 c16
        if sp_ is not None and (sp_.get("poly") or not polyphonic(n)):
            # mvt1 c03 (critic A #5, #6): an articulation test over a listed span (velocity and length below)
            n["art"] = ks_lookup(stem, sp_["art"])[0]
            n["art_span"] = sp_
            continue
        if family == "string":
            pizz = text_state(q, ["pizz"], ["arco"])
            tasto = text_state(q, ["sul tasto"], ["ord.", "arco"])
            if pizz:
                n["art"] = ks_lookup(stem, "Pizzicato RRx4", "Pizz RRx4")[0]
            elif q in trem_q:
                n["art"] = ks_lookup(stem, "Tremolo")[0]
            elif q in stacc_q:
                n["art"] = ks_lookup(stem, *([STAC_ROW[tname]] if tname in STAC_ROW else []),
                                     "Stac RRx14", "Stac RRx9", "Staccato RRx9")[0]
            elif tasto and stem.startswith("2nd"):
                n["art"] = ks_lookup(stem, "Flautando")[0]
            elif any(abs(q - k_) < 0.02 for k_ in DOWNBOW_STROKE_AT.get(tname, [])) and not polyphonic(n):
                n["art"] = ks_lookup(stem, "Sus MAX")[0]   # mvt1 c06 (A #1): a listed down-bow, a fresh stroke
                n["down_stroke"] = True
            elif STR_REP_AFTER_STAC and id(n) not in rep_ids and n["slur"] is None and not polyphonic(n) \
                    and n["end"] - q <= STR_REP_AFTER_STAC["max_qn"] + EPS \
                    and (lambda p_: p_ is not None and p_["pitch"] == n["pitch"] and p_["end"] <= q + EPS
                         and (p_.get("art") or "").startswith("Stac") and id(p_) not in rep_ids
                         and q - p_["qn"] <= STR_REP_AFTER_STAC.get("max_gap_qn", 1.0) + EPS)(
                        max((o for o in ns if o is not n and o["qn"] < q - EPS), key=lambda o: o["qn"], default=None)):
                # mvt1 c37 (critic A #2): a same-pitch note after a staccato stroke is a fresh stroke (see the default)
                n["art"] = ks_lookup(stem, "Sus MAX")[0]
                n["down_stroke"] = True
                n["rep_after_stac"] = True
            elif id(n) in det_str:   # mvt1 c02 (A #1): a retaken down-bow, a fresh stroke
                n["art"] = ks_lookup(stem, "Sus MAX")[0]
                n["det_acc"] = True
            elif id(n) in rep_ids:   # mvt1 c04 (A #1): a written-out repeated stroke
                if qn_to_sec(n["end"], TEMPO_NC) - qn_to_sec(q, TEMPO_NC) < REP_SPLIT["stac_s"] and any(
                        a_["name"].startswith("Stac RR") for a_ in ksmaps.get(stem, {}).get("articulations", [])):
                    n["art"] = ks_lookup(stem, "Stac RRx14", "Stac RRx9")[0]
                    if n.get("mt_alt"):   # mvt1 c15 (A #4): the alternate stroke row
                        n["art"] = ks_lookup(stem, MEAS_TREM["alt_row"])[0]
                    n["rep_stac"] = True
                else:
                    n["art"] = ks_lookup(stem, "Sus MAX")[0]
                    n["rep_sus"] = True
            elif STR_ACC_AFTER_SUS and q in accent_q and n["slur"] is None and not polyphonic(n) and any(
                    o is not n and o["qn"] < q - EPS and abs(o["end"] - q) < 0.06 and sus_like(o.get("art")) for o in ns) \
                    and not any(o["pitch"] == n["pitch"] and abs(o["qn"] - n["end"]) < 0.06 for o in ns):
                # (not when a same-pitch repeat follows: the legato merge keeps those one note, Vla 536)
                n["art"] = ks_lookup(stem, "Sus MAX")[0]   # mvt1 c02 (A #2): an accent after Sus eighths
                n["acc_sus"] = True
            elif STR_SHORT_AFTER_SUS and has_bc and n["slur"] is None and not polyphonic(n) \
                    and qn_to_sec(n["end"], TEMPO_NC) - qn_to_sec(q, TEMPO_NC) < STR_SHORT_AFTER_SUS["max_s"] \
                    and any(o is not n and o["qn"] < q - EPS and abs(o["end"] - q) < STR_SHORT_AFTER_SUS["abut_qn"]
                            and sus_like(o.get("art")) for o in ns):
                # mvt1 c05 (A #2): a short unslurred note after a Sus MAX / stroke note is a fresh stroke (in order, so a
                # neighbour note's return after a new stroke becomes one too)
                n["art"] = ks_lookup(stem, "Sus MAX")[0]
                n["short_stroke"] = True
            elif n["slur"] is not None and not polyphonic(n) and in_fast_leg(q):
                n["art"] = ks_lookup(stem, "Leg Slur MAX")[0]   # c14 (A #3): the bar 59 test
                n["fast_leg"] = True
            elif n["slur"] is not None and not polyphonic(n) and in_stacleg(q):
                n["art"] = ks_lookup(stem, in_stacleg(q))[0]   # c16 (A #3): the bar 59 test
                n["fast_leg"] = True   # no lead, no merge, FAST_LEG_OVERLAP
                # mvt1 c20: a span with its own row keeps the fast_leg velocities (targets FAST_LEG_VEL, heads their own)
                n["stacleg"] = in_stacleg(q) == STACLEG_ART
            elif n["slur"] is not None and not polyphonic(n) and in_detache(q):
                n["art"] = ks_lookup(stem, "Detache")[0]   # c15 (A #5): the bar 59 test
                n["detache_t"] = True
            elif n["slur"] is not None and not polyphonic(n) \
                    and (qn_to_sec(n["end"], TEMPO_NC) - qn_to_sec(q, TEMPO_NC) < 0.25
                         or any(abs(q - k_) < 0.02 for k_ in SHORT_SUS_AT.get(tname, []))) \
                    and not short_into_long(n) \
                    and not ((tname in SHORT_SUS_LEG_TRACKS or any(a_ - EPS <= q < b_ - EPS for a_, b_ in SHORT_SUS_LEG_SPANS.get(tname, [])))
                             and not any(abs(q - k_) < 0.02 for k_ in SHORT_SUS_LEG_SKIP.get(tname, []))
                             and qn_to_sec(n["end"], TEMPO_NC) - qn_to_sec(q, TEMPO_NC) >= SHORT_SUS_LEG_S[0] - EPS
                             and any(o is not n and slur_of(o["qn"]) == n["slur"] and o["qn"] < q - EPS for o in ns)
                             and not any(o["pitch"] == n["pitch"] and abs(o["qn"] - n["end"]) < 0.06
                                         and slur_of(o["qn"]) == n["slur"] for o in ns)):
                # (mvt1 c06 A #5 test: SHORT_SUS_LEG_TRACKS keep slurred non-first eighths of 0.20-0.25 s on Leg Slur MAX)
                # c05 (A #2): measured without the caesuras; the bar 60 breath had turned the violas' last sextuplet
                # note into a Leg Slur MAX target still sounding at the bar 61 tremolo keyswitch
                # c03 (C #3): fast slurred figures (viola sextuplets, bars 59-60) smear on the legato patch (transitions
                # of 160-320 ms); Sus MAX notes overlapping by 0.03 qn keep them connected and in time
                n["art"] = ks_lookup(stem, "Sus MAX")[0]
                n["short_sus"] = True
            elif n["slur"] is not None and not polyphonic(n):
                n["art"] = ks_lookup(stem, "Leg Slur MAX")[0]
            elif has_bc and not polyphonic(n):
                # c02: unslurred notes of a monophonic line stay on Leg Slur MAX (it plays its sustain layer for
                # disconnected notes, HO manual 2.1.3); connected ones get Leg BC below
                n["art"] = ks_lookup(stem, "Leg Slur MAX")[0]
            else:
                n["art"] = ks_lookup(stem, "Sus MAX")[0]
            continue
        # winds and brass: accents keep the accent patch only at f or louder (c01); softer accents are weight on CC11
        if in_marc(q) and q not in accent_q and n["end"] - q <= 1.0 + EPS:
            n["art"] = ks_lookup(stem, MARC_ART)[0]   # c14 (A #1)
            n["marc"] = True
        elif q in accent_q and base(q) >= DYN["f"] - 4 \
                and any(abs(q - k_) < 0.02 for k_ in ACCENT_ART_AT.get(tname, {})):
            # c26 (item 9): a listed loud accent plays this articulation (weight from the volume swell instead)
            n["art"] = ks_lookup(stem, next(v_ for k_, v_ in ACCENT_ART_AT[tname].items() if abs(q - k_) < 0.02))[0]
            n["acc_art"] = True
        elif q in accent_q and family in GENTLE_ACCENT and GENTLE_ACCENT[family].get("keep_legato") \
                and n["slur"] is not None and not near(q, ten_q) \
                and any(o is not n and o.get("slur") == n["slur"] and o["qn"] < q - EPS for o in ns):
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]   # mvt1 c01 (A #3): accent inside a slur
        elif q in accent_q and base(q) >= DYN["f"] - 4 and family in GENTLE_ACCENT:
            n["art"] = ks_lookup(stem, *GENTLE_ACCENT[family]["arts"])[0]   # mvt1 c00: no accent sample
            n["acc_art"] = True
        elif q in accent_q and base(q) >= DYN["f"] - 4:
            n["art"] = ks_lookup(stem, "Sus Accent MAX", "Sus Accent")[0]
        elif n["slur"] is not None and near(q, ten_q) and family == "wind" and in_sost(q) and not polyphonic(n) \
                and not any(o["pitch"] == n["pitch"] and o["qn"] < q - EPS and abs(o["end"] - q) < 0.05 for o in ns):
            # c07 (A #1): portato under "Largamente / molto sostenuto" is joined: legato (new pitch, or the first note)
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
            n["sost"] = True
        elif n["slur"] is not None and near(q, ten_q) and not polyphonic(n) \
                and any(abs(q - k_) < 0.02 for k_ in PORTATO_JOIN_AT.get(tname, [])) \
                and any(o is not n and o["qn"] < q - EPS and abs(o["end"] - q) < 0.05 and o["pitch"] != n["pitch"]
                        and slur_of(o["qn"]) == n["slur"] for o in ns):
            # mvt1 c04 (A #2): a listed slurred tenuto joins from the previous note of its slur (Horn 1's dolce solo:
            # re-tongued on Sus MAX it rose 8-9 dB over the Leg Slur note before it)
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
            n["portato_join"] = True
        elif n["slur"] is not None and near(q, ten_q) and not (
                TENUTO_HEAD_LEGATO and family in ("wind", "brass")
                and not any(o is not n and o.get("slur") == n["slur"] and o["qn"] < q - EPS for o in ns)):
            # c04 (A #4): a tenuto inside a slur (portato) is tongued: Sus attack, not Leg Slur's slow first-note layer
            # c32 (A #5, TENUTO_HEAD_LEGATO): not a slur's first note: it stays the slur's head (the tenuto is CC11
            # weight) and the next note joins it as a legato target (Clarinet 1's dolce solo, bars 45-46, had a gap
            # after its tenuto head and a disconnected Leg Slur note after it: a 12.5 dB spread over five notes)
            n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib")[0]
            if family == "wind" and in_sost(q) and not polyphonic(n) \
                    and any(o["pitch"] == n["pitch"] and o["qn"] < q - EPS and abs(o["end"] - q) < 0.05 for o in ns):
                n["sost_rep"] = True   # c07 (A #1): repeated pitch in the sostenuto span: re-tongued, early and firm
        elif SLUR_START_SUS and family in SLUR_START_SUS["families"] and slur_start_ok(n):
            # mvt1 c15 (critic A #2): a slur's short first note after a tongued note is tongued on the Sus row; the
            # slur's second note joins from it (lengths and lead below)
            n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib", "Sus Non Vib MAX")[0]
            n["slur_start_sus"] = True
        elif n["slur"] is not None:
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
        else:
            n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib")[0]
            if family == "wind" and in_sost(q) and near(q, ten_q):
                n["sost_sus"] = True   # c07 (A #1): unslurred tenuto under "Largamente" (Cl2): crossfaded, not cut

    # mvt3 c03 (critic C #1a): ACC_HEAD_JOIN. An accented slur head played on the Sus row (GENTLE_ACCENT / accent row)
    # is not a SLUR_START_SUS head (slur_start_ok rejects accents and heads over max_qn), so the slur's second note was a
    # disconnected Leg Slur note at the printed velocity: the slow first-note layer, +87..+137 ms late (F1's head motive).
    # With ACC_HEAD_JOIN the head is marked slur_start_sus when the slur's next note abuts it, has another pitch, is
    # monophonic and on a legato row: the head overlaps it (LEG_OVERLAP) and the second note takes the SOST join (lead
    # min(SOST_JOIN_LEAD_S, 0.45 x head), SOST_VEL). The head keeps its accent row and swell. False = off
    acc_head_joins = []
    if ACC_HEAD_JOIN and family in ("wind", "brass"):
        for n in ns:
            if not n.get("acc_art") or n.get("slur_start_sus") or n.get("slur") is None or polyphonic(n):
                continue
            sn_ = sorted([o for o in ns if o is not n and o.get("slur") == n["slur"]], key=lambda o: o["qn"])
            if not sn_ or any(o["qn"] < n["qn"] - EPS for o in sn_):
                continue
            n2_ = sn_[0]
            if abs(n2_["qn"] - n["end"]) < 0.05 and n2_["pitch"] != n["pitch"] and not polyphonic(n2_) \
                    and _lg(n2_.get("art") or "") and not n2_.get("grace"):
                n["slur_start_sus"] = True
                acc_head_joins.append(round(n["qn"], 3))
    # mvt1 c33 (critic C #3): WIND_WIDE_LEG. A monophonic wind note on a legato row whose previous note (written end
    # within WIND_WIDE_LEG_GAP_QN of its onset, slurred to it or a slur break) is more than WIND_WIDE_LEG semitones away
    # plays the Sus row as a re-tongued note: the HO legato scripts join only within an octave, and a short slur-break
    # gap (0.05 qn) still played a legato transition (Flute 1 F-sharp6 -> E5 at qn 396: crossover +0.34 s, E5 at its body
    # only at +0.57 s; c30's F-sharp6 -> E6 +0.065 s). The note before ends early (below) and the re-tongue lead applies
    wide_leg = []
    if WIND_WIDE_LEG and family == "wind":
        for n in ns:
            if not _lg(n.get("art") or "") or n.get("grace") or polyphonic(n):
                continue
            pv_ = [o for o in ns if o is not n and o["qn"] < n["qn"] - EPS
                   and -EPS < n["qn"] - o["end"] < WIND_WIDE_LEG_GAP_QN + EPS]
            if len(pv_) != 1 or polyphonic(pv_[0]) or pv_[0].get("grace"):
                continue
            if abs(pv_[0]["pitch"] - n["pitch"]) > WIND_WIDE_LEG:
                n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib", "Sus Non Vib MAX")[0]
                n["wide_leg"] = True
                wide_leg.append(round(n["qn"], 3))
                # its own slur goes on legato: the next note of the slur joins from it like a SLUR_START_SUS head
                # (overlap, SOST_JOIN_LEAD_S lead); without this the slur broke at the next note (a re-attack)
                nx_ = [o for o in ns if o is not n and abs(o["qn"] - n["end"]) < 0.05]
                if len(nx_) == 1 and n["slur"] is not None and nx_[0].get("slur") == n["slur"] \
                        and nx_[0]["pitch"] != n["pitch"] and _lg(nx_[0].get("art") or "") and not polyphonic(nx_[0]):
                    n["slur_start_sus"] = True

    # mvt1 c38 (critic C #2): SLUR_HEAD_REP_SUS. A monophonic wind/brass slur head on a legato row that repeats the
    # pitch of the note just before it (another slur's end or an unslurred note, ending within "gap_qn" of its onset) is
    # re-tongued on the Sus row; the next note of its slur joins from it like a SLUR_START_SUS head. On Leg Slur MAX the
    # same-pitch re-attack plays the slow first-note layer (kit section 6): Bassoon 1's F3 at 136 (bar 35, espr. solo)
    # was listed as re-tongued (gap and fall) and still dipped -0.2 dB, against 5.4-8.0 dB for the other re-tongued
    # repeats. Notes in a REP_ROW span are left to that row. parts.json `slur_head_rep`
    slur_head_rep = []
    if SLUR_HEAD_REP_SUS and family in SLUR_HEAD_REP_SUS.get("families", ("wind", "brass")):
        for n in ns:
            if not _lg(n.get("art") or "") or n.get("grace") or polyphonic(n) or n["slur"] is None \
                    or any(a_ - EPS <= n["qn"] < b_ - EPS for a_, b_, r_ in REP_ROW.get(tname, [])):
                continue
            if any(o is not n and o.get("slur") == n["slur"] and o["qn"] < n["qn"] - EPS for o in ns):
                continue   # not the slur's first note
            if "at" in SLUR_HEAD_REP_SUS and not any(abs(n["qn"] - q_) < 0.02 for q_ in SLUR_HEAD_REP_SUS["at"].get(tname, [])):
                continue   # an "at" list {track: [score qn]} restricts the rule to listed heads
            pv_ = [o for o in ns if o is not n and o["qn"] < n["qn"] - EPS
                   and -EPS < n["qn"] - o["end"] < SLUR_HEAD_REP_SUS.get("gap_qn", 0.25) + EPS]
            if len(pv_) != 1 or pv_[0]["pitch"] != n["pitch"] or polyphonic(pv_[0]) or pv_[0].get("grace") \
                    or pv_[0].get("slur") == n["slur"]:
                continue
            n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib", "Sus Non Vib MAX")[0]
            n["slur_head_rep"] = True
            slur_head_rep.append(round(n["qn"], 3))
            nx_ = [o for o in ns if o is not n and abs(o["qn"] - n["end"]) < 0.05]
            if len(nx_) == 1 and nx_[0].get("slur") == n["slur"] and nx_[0]["pitch"] != n["pitch"] \
                    and _lg(nx_[0].get("art") or "") and not polyphonic(nx_[0]):
                n["slur_start_sus"] = True

    # mvt1 c44 (ONE_TIME #4, critics A #1-#2): STR_REP_NEW_BOW, see the default. In score order, so a repeat after a new
    # stroke sees the stroke as its predecessor (a soft repeat then merges into the stroke, a loud one is a stroke too)
    rep_strokes, rep_rebow_q, rep_sus_gaps = [], [], []
    stroke_falls = []   # mvt3 c21: STR_REP_NEW_BOW "stroke_fall" (parts.json "stroke_falls")

    def _stroke_fall_ok():
        F_ = (STR_REP_NEW_BOW or {}).get("stroke_fall")
        return bool(F_) and (not F_.get("tracks") or tname in F_["tracks"])
    chord_head_gaps, chord_loure_gaps = [], []   # mvt3 c11: STR_REP_NEW_BOW["chord"]["head_gap_s"] repeats (parts.json `chord_head_gaps`)
    if STR_REP_NEW_BOW and family == "string":
        SB_ = STR_REP_NEW_BOW
        for n in sorted(ns, key=lambda o: o["qn"]):
            if not _lg(n.get("art") or "") or polyphonic(n) or n.get("fast_leg") or n.get("grace"):
                continue
            pv_ = [o for o in ns if o is not n and o["qn"] < n["qn"] - EPS and -EPS < n["qn"] - o["end"] < 0.1]
            if len(pv_) != 1:
                continue
            o = pv_[0]
            if o["pitch"] != n["pitch"] or polyphonic(o) or o.get("fast_leg") or o.get("grace") or near(o["end"], breath_q):
                continue
            if any(a_ - EPS <= n["qn"] < b_ - EPS for a_, b_ in (SB_.get("skip") or {}).get(tname, [])):
                continue   # mvt3 c02: listed spans keep the merge
            if [x_ for x_ in ns if x_ is not o and -EPS < x_["qn"] - o["end"] < 0.1] != [n]:
                continue   # a chord or another onset follows: the merge loop leaves it too
            # mvt3 c02: a DOWNBOW_STROKE_AT stroke (Sus MAX) before a same-pitch slurred repeat: the repeat was left as an
            # unled Leg Slur MAX first note (Violas 892 -> 893); it is classed like the others
            if not (_lg(o.get("art") or "") or o.get("rep_stroke") or (o.get("down_stroke") and same_slur(o, n))
                    or (SLUR_REP_MERGE_SUS and o.get("short_sus") and o["slur"] is not None and n["slur"] == o["slur"])):
                continue   # the merge loop would not join these two
            same_ = n["slur"] is not None and same_slur(o, n)
            if same_ and not (SB_.get("portato") and near(n["qn"], ten_q)):
                continue   # one bow: the merge (and its notch) stays
            if same_:
                cls_ = "portato"
            else:
                mk_ = next((d_ for q_, d_ in sorted(marks, reverse=True) if q_ <= n["qn"] + 0.01 and d_ in DYN), None)
                mv_ = DYN[mk_] if mk_ else 0
                lv_ = base(n["qn"])
                head_ = n["slur"] is not None and not any(x_ is not n and x_.get("slur") == n["slur"]
                                                          and x_["qn"] < n["qn"] - EPS for x_ in ns)
                loud_ = n["qn"] in accent_q or lv_ >= SB_["stroke_cc"] - EPS or mv_ >= DYN[SB_["stroke_mark"]] \
                    or (head_ and max(lv_, mv_) >= SB_["head_cc"] - EPS)
                cls_ = "stroke" if loud_ else "soft"
            if cls_ == "soft":
                n["rep_rebow"] = True
                continue
            n["art"] = ks_lookup(stem, "Sus MAX")[0]
            n["down_stroke"] = True   # velocity, Leg BC join of the next note, no vibrato restart at f
            n["rep_stroke"] = cls_
            rep_strokes.append([round(n["qn"], 3), cls_])

    # c14 (A #2): a roll tied into a short note (the MIDI merges the tie) ends on a stroke at the tied note
    if family == "timp":
        for n in list(ns):
            if not n["art"].endswith("Rls"):
                continue
            for sq_ in TIMP_TIE_STROKES:
                if n["qn"] + 0.5 < sq_ < n["end"] - 0.1:
                    st_ = dict(n, qn=sq_, art=ks_lookup(stem, TIMP_ROW(stem, "Lng"))[0], tie_stroke=True)
                    n["end"] = sq_ + 0.03
                    ns.append(st_)
        ns.sort(key=lambda n: n["qn"])

    # mvt1 c36 (critic C #1): SUBITO_FRESH. A note on a subito-softer mark that another note joins into (its end within
    # 0.1 qn of the onset) is a fresh entry; legato targets are undone after the note-end pass below
    sub_soft_q = sorted(q_ for q_ in {q_ for s_ in staves for q_ in SUBITO[s_]} if base(q_ + 0.01) < base(q_ - 0.05) - EPS)
    subito_fresh = []
    if SUBITO_FRESH and sub_soft_q and family in ("wind", "brass", "string"):
        for n in ns:
            if n.get("grace") or not any(abs(n["qn"] - q_) < EPS for q_ in sub_soft_q):
                continue
            if any(o is not n and o["qn"] < n["qn"] - EPS and abs(o["end"] - n["qn"]) < 0.1 for o in ns):
                # strings: a fresh bow stroke; winds and brass only when the note would be a legato target (post-pass
                # below), so tongued re-attacks keep their re-tongue gap and lead
                n["fresh"] = family == "string"
                n["subito_fresh"] = True

    # c02: bow-change legato (Leg BC MAX) where a monophonic string line joins without a slur, or where one slur ends
    # and the next begins: the target note is played as a legato bow change instead of a cut and a new attack
    vla_bc_notch = []
    bc_skipped = []
    if has_bc:
        for i, n in enumerate(ns):
            # c03 (A #3): tenuto notes join with Leg BC too (the +5 CC tenuto bump is their weight)
            # mvt1 c03 (critic C #1): also the last Sus MAX eighth of a fast slur (short_sus) into a new bow
            # mvt1 c06 (A #1): and a DOWNBOW_STROKE_AT stroke into the note after it
            # mvt1 c20 (critic A #1): and the last note of a run span on its own legato row (Slur Runs) into a new bow
            if (n["art"] not in ("Leg Slur MAX", "Leg BC MAX") and not (SHORT_SUS_JOIN and n.get("short_sus"))
                    and not n.get("down_stroke") and not (n.get("fast_leg") and not n.get("stacleg") and _lg(n["art"]))) \
                    or near(n["end"], breath_q) or n.get("grace"):
                continue
            nxt = [o for o in ns[i + 1:] if -EPS < o["qn"] - n["end"] < 0.1]
            if len(nxt) != 1 or [o for o in ns[i + 1:] if abs(o["qn"] - nxt[0]["qn"]) < EPS] != nxt:
                continue
            o = nxt[0]
            if o["pitch"] == n["pitch"] or o["art"] not in ("Leg Slur MAX",) or polyphonic(o) or o.get("grace") \
                    or o.get("grace_target") or o.get("subito_fresh"):
                continue
            if same_slur(n, o):
                continue
            # c09 (A #3): no bow-change legato across more than an octave (the HO legato scripts cover an octave; Vc
            # qn 274 C4 -> A flat 2 entered 1 s late) or where a solo ends and the section enters (Vln I qn 65 "tutti"):
            # different players. A wide unslurred step plays Sus MAX (the c06 Leg -> Sus entry path)
            wide = abs(o["pitch"] - n["pitch"]) > 12
            newp_ = any(abs(tq - o["qn"]) < EPS and (has(t, "tutti") or has(t, "solo"))
                        for tq, t in texts_until(staves, o["qn"]))
            if wide or newp_:
                if wide and o["slur"] is None:
                    o["art"] = ks_lookup(stem, "Sus MAX")[0]
                elif not wide or (FRESH_WIDE_SLURRED and newp_):   # mvt1 c35: FRESH_WIDE_SLURRED (see the default)
                    o["fresh"] = True   # a new player's entry: entry lead, the old note cut before it (below)
                bc_skipped.append(round(o["qn"], 3))
                continue
            if tname in BC_SOFT["tracks"] and base(o["qn"]) <= BC_SOFT["max_cc"] \
                    and qn_to_sec(o["end"]) - qn_to_sec(o["qn"]) < BC_SOFT["max_s"] \
                    and not any(abs(o["qn"] - x_) < 0.01 for x_ in BC_SOFT_SKIP.get(tname, [])):
                # c08 (A #2): stays Leg Slur MAX, joined (bc_from) with a pp bow-change notch
                # c11 (A #1): Violins II and Violoncellos too, any length
                o["bc_from"] = id(n)
                vla_bc_notch.append((o["qn"], BC_SOFT["notch_soft"] if base(o["qn"]) <= BC_SOFT["soft_cc"]
                                     else VLA_BC_SOFT["notch"]))
                continue
            o["art"] = "Leg BC MAX"
            o["bc_from"] = id(n)

    # c11 (A #4): portamento targets
    port_done = []
    for n in ns:
        pv_ = next((v_ for k_, v_ in PORT_TARGETS.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), None)
        if pv_ is not None and n.get("art") in ("Leg Slur MAX", "Leg BC MAX") and not polyphonic(n):
            n["art"] = ks_lookup(stem, "Leg Port MAX")[0]
            n["port_vel"] = pv_
            port_done.append(round(n["qn"], 3))

    # c03 (A #1): a repeated pitch in a legato string line (portato pulse, bow change at a barline) was cut and
    # re-attacked on the legato patch's slow sustain layer: 7-15 dB holes. Merge the two notes and mark the bow change
    # with a CC11 notch instead (portato 10 CC, bow change 14 CC, about 3 dB).
    notches = list(vla_bc_notch)   # (qn, depth)
    merged_ten = []
    slur_rep_merged = []   # mvt1 c05 (A #1)
    # mvt1 c05 (critic A #1): a same-pitch note at the end of a slur (`d''8( des''8 c''8 | c''4)`, no tie) was cut and
    # re-attacked: on strings the short_sus eighth (Sus MAX) into a new Leg Slur MAX note, which with nothing sounding
    # before it plays the slow first-note layer (the arrival fell 7-17 dB under the eighth over +0.2..+0.5 s); on winds a
    # Leg Slur re-tongue after a 0.06 qn gap (8-12 dB hole in the first 0.2 s). A slurred repeat is one bow / one breath
    # with a light pulse: merge it into the note before with a small CC11 notch (strings keep the eighth's Sus MAX)
    wind_rep_merge = WIND_SLUR_REP_MERGE and family == "wind"
    if family == "string" or wind_rep_merge:
        i = 0
        while i < len(ns):
            n = ns[i]
            slur_rep_ = family == "string" and SLUR_REP_MERGE_SUS and n.get("short_sus") and n["slur"] is not None
            # mvt1 c44: a STR_REP_NEW_BOW stroke takes the soft repeats after it (their bow changes are re-bow points)
            str_rep_ = family == "string" and bool(n.get("rep_stroke"))
            if ((n.get("art") and _lg(n["art"])) or slur_rep_ or str_rep_) and not near(n["end"], breath_q):
                nxt = [o for o in ns[i + 1:] if -EPS < o["qn"] - n["end"] < 0.1]
                same_on = [o for o in ns[i + 1:] if nxt and abs(o["qn"] - nxt[0]["qn"]) < EPS]
                in_slur_ = len(nxt) == 1 and n["slur"] is not None and nxt[0]["slur"] == n["slur"]
                if family == "wind" and not (in_slur_ and not near(nxt[0]["qn"], ten_q)):
                    i += 1
                    continue   # winds: only a same-pitch note inside the same slur, without a tenuto (portato paths)
                if family == "wind" and any(a_ - EPS <= nxt[0]["qn"] < b_ - EPS for a_, b_, r_ in REP_ROW.get(tname, [])):
                    # mvt1 c39 (critic A #3): a slurred repeat into a REP_ROW note is left to the repetition row (it
                    # re-tongues with the row's own attack; merged, Clarinet 1 310 dipped 1.4 dB)
                    i += 1
                    continue
                if slur_rep_ and not (_lg((n.get("art") or ""))) and not in_slur_:
                    i += 1
                    continue
                o_starts_slur_ = STR_MERGE_KEEP_SLUR_START and family == "string" and nxt and nxt[0]["slur"] is not None \
                    and nxt[0]["slur"] != n["slur"] \
                    and not any(o_ is not nxt[0] and o_.get("slur") == nxt[0]["slur"] and o_["qn"] < nxt[0]["qn"] - EPS for o_ in ns)
                if len(nxt) == 1 and same_on == nxt and nxt[0]["pitch"] == n["pitch"] and _lg((nxt[0].get("art") or "")) \
                        and not polyphonic(n) and not polyphonic(nxt[0]) and not o_starts_slur_ \
                        and not n.get("fast_leg") and not nxt[0].get("fast_leg"):   # c14 (A #3): no merge in the test
                    o = nxt[0]
                    if str_rep_ and not o.get("rep_rebow"):
                        i += 1
                        continue   # mvt1 c44: a stroke absorbs only STR_REP_NEW_BOW "soft" repeats
                    portato = near(o["qn"], ten_q) and n["slur"] is not None and o["slur"] == n["slur"]
                    # c04 (C #5): a bow change at pp (CC11 40 or below) takes 8 CC, not 14
                    dep_ = 10 if portato else (8 if base(o["qn"]) <= 40 else 14)
                    if family == "wind" or (slur_rep_ and not _lg((n.get("art") or ""))):
                        dep_ = SLUR_REP_NOTCH[1] if base(o["qn"]) > 90 else SLUR_REP_NOTCH[0]
                        if family == "wind":
                            dep_ = WIND_SLUR_REP_NOTCH
                        slur_rep_merged.append(round(o["qn"], 3))
                        n.setdefault("vel_end", n["end"])   # the legato velocity keeps the eighth's own length
                    dep_ = next((v_ for q_, v_ in MERGE_NOTCH_AT.get(tname, {}).items() if abs(q_ - o["qn"]) < EPS), dep_)
                    if o.get("rep_rebow"):
                        rep_rebow_q.append(round(o["qn"], 4))   # mvt1 c44: STR_REP_NEW_BOW "soft": a re-bow, no notch
                    else:
                        notches.append((o["qn"], dep_))
                    if near(o["qn"], ten_q):
                        merged_ten.append(o["qn"])
                    n["end"] = o["end"]
                    if not (MERGE_KEEP_OWN_SLUR and o["slur"] is None and n["slur"] is not None):
                        n["slur"] = o["slur"]   # joins onward as the dropped note did
                    # c32 (A #5): a slurred note merged with an unslurred same-pitch continuation (a tie out of the
                    # slur) keeps its own slur, so it is still the slur's legato target (v621 Vc bar 45: G( A-flat)~
                    # A-flat; the A-flat lost its slur and started unled on the slow first-note layer)
                    for o2 in ns:   # a later note bow-changed from the dropped one now joins from the merged note
                        if o2.get("bc_from") == id(o):
                            o2["bc_from"] = id(n)
                    ns.remove(o)
                    continue   # the merged note may repeat again
            i += 1

    # c15 (A #3): Violins II Flautando chords joined without a rest: flag the new chord's notes, then hold common tones
    flaut_merged = 0
    # mvt1 c08 (critic A #4): tremolo chords inside TREM_JOIN spans join the same way (common tones held as one note,
    # moving voices early with an overlap); the held notes are split again at the output stage (TREM_SPLIT)
    def join_art(o):
        if o.get("art") == "Flautando" and tname in FLAUT_JOIN_TRACKS:
            return True
        return o.get("art") == "Tremolo" and any(a_ - EPS <= o["qn"] < b_ - EPS for a_, b_ in TREM_JOIN.get(tname, []))
    if tname in FLAUT_JOIN_TRACKS or tname in TREM_JOIN:
        fl = [n for n in ns if join_art(n)]
        for n in fl:
            if any(o is not n and o["qn"] < n["qn"] - EPS and abs(o["end"] - n["qn"]) < 0.05 for o in fl):
                n["flaut_join"] = True
        changed = True
        while changed:
            changed = False
            for n in sorted([o for o in ns if join_art(o)], key=lambda o: o["qn"]):
                m_ = [o for o in ns if o is not n and join_art(o) and o.get("art") == n.get("art") and o["pitch"] == n["pitch"]
                      and abs(o["qn"] - n["end"]) < 0.05]
                if m_:
                    n["end"] = m_[0]["end"]
                    ns.remove(m_[0])
                    flaut_merged += 1
                    changed = True
                    break

    # c06 (A #5): a printed up-bow/down-bow inside a held (tied) string note is a bow change: the same notch as a merged
    # repeat (14 CC above CC 40, 6 at pp and softer)
    if family == "string":
        bow_q = sorted({q for s_ in staves for q, k, v in ev[s_] if k == "script" and v[0] in ("upbow", "downbow")})
        for bq in bow_q:
            if any(n["qn"] + 0.01 < bq < n["end"] - 0.01 for n in ns) and not any(abs(nq - bq) < EPS for nq, _ in notches):
                # c16 (A #4): 6 CC at f or louder (a held ff note's bow change is nearly inaudible in a section; the
                # 14 CC notch cost 1.7-4.2 dB for 0.7 s at bar 80)
                notches.append((bq, 6 if base(bq) >= DYN["f"] else (14 if base(bq) > 40 else 6)))
    if NOTCH_SKIP.get(tname):   # c26: the re-bow replaces these CC11 bow-change notches
        notches = [(nq, d_) for nq, d_ in notches if not any(abs(nq - s_) < 0.02 for s_ in NOTCH_SKIP[tname])]
    # mvt1 c44: the listed re-bow points plus the STR_REP_NEW_BOW "soft" bow changes at their printed onsets
    rebow_at_t = sorted(set(REBOW_AT.get(tname, [])) | set(rep_rebow_q))

    # note lengths (c01): breaths, legato joins inside one slur only, bow change / re-tongue between slurs,
    # repeated pitches re-attacked, tenuto as a small separation
    orig_end = {id(n): n["end"] for n in ns}
    rep_split_gaps = []   # mvt1 c51 (ported mvt3 c10): score onsets of strokes whose predecessor took the REP_SPLIT gap

    def _rep_stroke(x_):   # mvt1 c51: REP_SPLIT, STR_SHORT_AFTER_SUS and STR_REP_AFTER_STAC strokes
        return bool(x_.get("rep_sus") or x_.get("rep_stac") or x_.get("short_stroke") or x_.get("rep_after_stac"))

    _PR_ARTS = ("Sus MAX", "Marc Sus LITE", "Sus Marc LITE")

    def _plain_rep(a_, b_):
        # mvt1 c51: an unslurred monophonic same-pitch Sus MAX repeat of at most REP_SPLIT["max_qn"] on a patch without
        # Leg BC (the Basses KS Master: REP_SPLIT needs has_bc, so its ff eighth pedals kept 0.03 qn, 8-12 ms)
        return family == "string" and not has_bc and a_.get("art") in _PR_ARTS and b_.get("art") in _PR_ARTS \
            and a_["slur"] is None and b_.get("slur") is None and not polyphonic(a_) and not polyphonic(b_) \
            and orig_end[id(a_)] - a_["qn"] <= REP_SPLIT["max_qn"] + EPS
    cc_falls = []   # c15 (A #6): (start, end, CC): CC11 falls to -CC at end, back to 0 over 0.3 qn
    timp_chain_skip = []   # mvt1 c07 (B #4)
    rep_retongued = []   # mvt1 c06 (A #2): onsets re-tongued by WIND_REP_RETONGUE (cc_falls rows carry their return)
    rep_row_reps = []   # mvt1 c37 (A #3): repeats into a REP_ROW span note (short gap, no fall)

    def rep_row_of(n_):   # mvt1 c37 (critic A #3): the REP_ROW row of a note's score onset, or None
        return next((r_ for a_, b_, r_ in REP_ROW.get(tname, []) if a_ - EPS <= n_["qn"] < b_ - EPS), None)
    for i, n in enumerate(ns):
        e0, dur = orig_end[id(n)], orig_end[id(n)] - n["qn"]
        nxt = [o for o in ns[i + 1:] if abs(o["qn"] - e0) < EPS]
        bc = [o for o in ns[i + 1:] if o.get("bc_from") == id(n)]
        if bc and not nxt:
            nxt = bc
            e0 = bc[0]["qn"]
        if near(orig_end[id(n)], breath_q):
            # c13 (A #5): a loud wind/brass note (CC11 72 or more) ends 0.3 qn before the breath (at most half its
            # length): Hn1's f breath at qn 196 (0.2 qn gap) dipped only 4.4 dB under the release and hall tail
            bg_ = next((v_ for k_, v_ in BREATH_GAP_AT.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), None)
            if bg_ is not None:   # c15 (A #6)
                n["end"] = e0 - min(bg_, 0.6 * dur)
                bf_ = next((v_ for k_, v_ in BREATH_FALL_CC.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), 0)
                if bf_:
                    cc_falls.append((n["end"] - 0.2, n["end"], bf_))
            elif family in ("wind", "brass") and base(e0 - 0.01) >= DYN["mf"]:
                # c19 (C #2): at a breath that also has a CAESURA (204, 268) the caesura already gives the pause; 0.3 qn
                # made a 0.54 s wind hole (25-33 dB) just before the ff while the strings played on
                gap_ = CAESURA_BREATH_QN if any(abs(e0 - c_) < 0.01 for c_ in CAESURA) else 0.3
                n["end"] = e0 - min(gap_, 0.5 * dur)
                bfb_ = next((v_ for k_, v_ in BREATH_FALL_BY.items()
                             if (k_[0].isupper() and tname.startswith(k_)) or k_ == family), 0)
                if bfb_:   # mvt1 c07 (A #2): horn breaths dipped 0.3-3 dB with the gap alone
                    cc_falls.append((max(n["qn"] + 0.25 * dur, n["end"] - 0.2), n["end"], bfb_))
            else:
                n["end"] = e0 - min(0.25, 0.2 * dur)
            continue
        if not nxt:
            continue
        same_pitch = any(o["pitch"] == n["pitch"] for o in nxt)
        is_leg = bool(n.get("art") and _lg(n["art"]))
        o0 = nxt[0]
        leg_join = is_leg and not same_pitch and _lg((o0.get("art") or "")) and (
            same_slur(n, o0) or o0.get("bc_from") == id(n))
        # mvt3 c11 (critic A #4, S1): the STR_REP_NEW_BOW "chord" condition is computed before the chain, so the generic
        # string tenuto rule (0.06 qn) no longer takes a tenuto chord repeat at a new slur first (violas 846-866: 25 ms gaps)
        chord_rep_ = bool(same_pitch and family == "string" and STR_REP_NEW_BOW and STR_REP_NEW_BOW.get("chord") \
                and (polyphonic(n) or len(nxt) > 1) and not n.get("rep_stac") \
                and not any(w_ in (n.get("art") or "") for w_ in ("Trem", "Pizz", "Stac", "Flaut")) \
                and (lambda o_: o_ is not None and not same_slur(n, o_) and not _lg(o_.get("art") or "")
                     and not any(w_ in (o_.get("art") or "") for w_ in ("Trem", "Pizz", "Stac", "Flaut"))
                     and base(o_["qn"]) >= STR_REP_NEW_BOW["stroke_cc"] - EPS
                     and not any(a_ - EPS <= o_["qn"] < b_ - EPS for a_, b_ in (STR_REP_NEW_BOW.get("skip") or {}).get(tname, []))
                     and not any(sp_[0] - EPS <= o_["qn"] < sp_[1] - EPS
                                 for sp_ in ((STR_REP_DETACH or {}).get("at") or {}).get(tname, [])))(
                    next((o_ for o_ in nxt if o_["pitch"] == n["pitch"]), None)))
        if n.get("detache_t"):
            n["end"] = e0 + 0.01   # c15 (A #5)
        elif same_pitch and family == "string" and o0.get("rep_stroke") and STR_REP_NEW_BOW:
            # mvt1 c44 (ONE_TIME #4, critics A #1-#2): the note before a STR_REP_NEW_BOW stroke ends min(gap_s, frac x
            # its length) before the stroke's score onset; portato repeats add a CC11 fall over its last fall_s
            R_ = dict(STR_REP_NEW_BOW, **(STR_REP_NEW_BOW.get("portato") or {})) if o0["rep_stroke"] == "portato" \
                else STR_REP_NEW_BOW
            # mvt3 c21 (critic A c21 #5): "stroke_fall" {fall_cc, fall_cc_loud, fall_s, "tracks": [...] optional}: the
            # "stroke" class takes a CC11 fall as the portato class does (the celli's re-bowed repeats dipped a median
            # 2.2 dB: the old note's capped release still sounded under the slow start of the new "Sus MAX" note)
            if o0["rep_stroke"] == "stroke" and _stroke_fall_ok():
                R_ = dict(R_, **{k_: v_ for k_, v_ in STR_REP_NEW_BOW["stroke_fall"].items() if k_ != "tracks"})
                stroke_falls.append(round(o0["qn"], 3))
            n["end"] = e0 - min(e0 - qn_before(e0, R_["gap_s"]), R_["frac"] * dur)
            fc_ = R_.get("fall_cc_loud", R_.get("fall_cc", 0)) if base(o0["qn"]) > 90 else R_.get("fall_cc", 0)
            if fc_:
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], R_.get("fall_s", 0.04)))
                cc_falls.append((fa_, n["end"], fc_, max(0.01, e0 - n["end"])))
        elif same_pitch and family == "string" and STR_REP_NEW_BOW and STR_REP_NEW_BOW.get("tenuto") \
                and near(o0["qn"], ten_q) and len(nxt) == 1 and not polyphonic(n) and not polyphonic(o0) \
                and not same_slur(n, o0) and not o0.get("rep_stroke") \
                and not any(sp_[0] - EPS <= o0["qn"] < sp_[1] - EPS
                            for sp_ in ((STR_REP_DETACH or {}).get("at") or {}).get(tname, [])):
            # mvt3 c03 (critic A #1): STR_REP_NEW_BOW "tenuto" {gap_s, frac, fall_cc, fall_s}: an unslurred same-pitch
            # repeat carrying a tenuto is a new bow at any dynamic and length (Vc 980-983 kept 0.06 qn = 22 ms under the
            # string tenuto rule and dipped 0.5-1.9 dB; Vc 325-327 at mp were under stroke_cc)
            T_ = STR_REP_NEW_BOW["tenuto"]
            n["end"] = e0 - min(e0 - qn_before(e0, T_["gap_s"]), T_["frac"] * dur)
            if T_.get("fall_cc"):
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], T_.get("fall_s", 0.04)))
                cc_falls.append((fa_, n["end"], T_["fall_cc"], max(0.01, e0 - n["end"])))
            rep_sus_gaps.append(round(o0["qn"], 3))
        elif TREM_TIMING_C04 and near(n["qn"], ten_q) and family == "string" and not leg_join and o0.get("art") != n.get("art") \
                and base(n["qn"]) >= DYN["f"]:
            # c04 (A #3): a loud string tenuto into another articulation (bar 62 -> 63 tremolo) crossfades, no hole
            n["end"] = e0 + 0.02
        elif (n.get("sost") or n.get("sost_rep") or n.get("sost_sus")) and same_pitch:
            n["end"] = e0 - 0.01   # c07 (A #1): into a repeated pitch under "Largamente": the shortest break
        elif n.get("sost_rep") or n.get("sost_sus"):
            n["end"] = e0 + 0.03   # c07 (A #1): a Sus note under "Largamente" into a new pitch: 0.03 qn crossfade
        elif n.get("slur_start_sus") and not same_pitch:
            n["end"] = e0 + LEG_OVERLAP   # mvt1 c15 (A #2): the KS Master joins the slur's second note from it
        elif PORTATO_TAIL_JOIN and family in ("wind", "brass") and near(n["qn"], ten_q) and n["slur"] is not None \
                and not is_leg and not same_pitch and len(nxt) == 1 and same_slur(n, o0) \
                and not near(o0["qn"], ten_q) and _lg((o0.get("art") or "")) and not o0.get("leg_target") \
                and not o0.get("grace"):
            # mvt1 c34 (critic A #2): a re-tongued portato tenuto joins the next note of its slur (see the default)
            n["end"] = e0 + LEG_OVERLAP
            n["portato_tail"] = True
        elif near(n["qn"], ten_q) and not (family == "string" and leg_join) and not ((n.get("sost") or n.get("portato_join")) and leg_join) \
                and not (TENUTO_HEAD_LEGATO and leg_join and same_slur(n, o0)) \
                and not chord_rep_:
            # c03 (A #3): tenuto = full value with weight. Basses 0.02 qn; winds/brass a light re-tongue at mf or louder
            # or under "sostenuto"; 0.06 qn at p and softer
            lg_ = ((STR_REP_NEW_BOW or {}).get("chord") or {}).get("loure_gap_s")
            if family == "string" and lg_ and same_pitch and (polyphonic(n) or len(nxt) > 1) and same_slur(n, o0) \
                    and near(o0["qn"], ten_q):
                # mvt3 c11 (critic A #4, S1): "loure_gap_s" (optional): a tenuto chord repeat inside one slur (louré)
                # gets this gap (at most 0.3 of the note) instead of 0.06 qn (25 ms at 144 qpm: violas 842-870 stem
                # dip 3.6 dB); shorter than the chord rule's gap at a new slur
                n["end"] = e0 - min(e0 - qn_before(e0, lg_), 0.3 * dur)
                chord_loure_gaps.append(round(e0, 3))
            elif family == "string":
                n["end"] = e0 - (0.02 if stem.startswith("Basses") else min(0.06, 0.15 * dur))
            elif base(n["qn"]) >= DYN["mf"] - 2 or text_state(n["qn"], ["sostenuto"], ["a tempo", "tempo i"]):
                n["end"] = e0 - min(0.03, 0.1 * dur)
            else:
                n["end"] = e0 - min(0.06, 0.15 * dur)
        elif n.get("short_sus") and not same_pitch:
            n["end"] = e0 + 0.03   # c03: polyphonic Sus MAX, so the overlap is a crossfade
            join_ok_ = SHORT_SUS_JOIN and family == "string" and len(nxt) == 1 and _lg((o0.get("art") or "")) \
                and not any(x_ is not o0 and x_ is not n and x_["qn"] < o0["end"] - EPS and x_["end"] > o0["qn"] + EPS
                            for x_ in ns) \
                and not o0.get("grace") and (same_slur(n, o0) or o0.get("bc_from") == id(n))
            if family == "string" and base(n["qn"]) >= SHORT_SUS_DETACH["min_cc"] \
                    and qn_to_sec(e0) - qn_to_sec(n["qn"]) < SHORT_SUS_DETACH["max_s"] and nxt \
                    and not (SHORT_SUS_DETACH_JOIN_LEG and join_ok_ and same_slur(n, o0)):
                n["end"] = e0 - SHORT_SUS_DETACH["gap"]   # c11 (C #6)
                n["detach"] = True
            elif SHORT_SUS_JOIN and family == "string" and len(nxt) == 1 and _lg((o0.get("art") or "")) \
                    and not any(x_ is not o0 and x_ is not n and x_["qn"] < o0["end"] - EPS and x_["end"] > o0["qn"] + EPS
                                for x_ in ns) \
                    and not o0.get("grace") and (same_slur(n, o0) or o0.get("bc_from") == id(n)):
                # mvt1 c03 (critic C #1): the KS Master joins the overlapping Sus eighth into the next Leg note as a
                # legato transition (41 notes crossed a median +0.165 s late, bar 18 +0.225 s: an eighth at 126). Make
                # it a legato target, so it gets the legato lead; across a slur boundary it is on Leg BC MAX (bc pass)
                o0["leg_target"] = True
                o0["leg_prev"] = n
                o0["short_sus_join"] = True
                n["end"] = e0 + LEG_OVERLAP   # the output moves this end with the target's lead
        elif n.get("down_stroke") and not same_pitch and len(nxt) == 1 and _lg((o0.get("art") or "")) \
                and (same_slur(n, o0) or o0.get("bc_from") == id(n)):
            n["end"] = e0 + LEG_OVERLAP   # mvt1 c06 (A #1): the stroke joins the next note as a legato transition
            o0["leg_target"] = True
            o0["leg_prev"] = n
        elif same_pitch and family == "string" and STR_REP_NEW_BOW and STR_REP_NEW_BOW.get("sus_min_s") and not is_leg \
                and n.get("art") in STR_STROKE_ROWS and o0.get("art") in STR_STROKE_ROWS and len(nxt) == 1 \
                and not o0.get("rep_stac") \
                and not polyphonic(n) and not polyphonic(o0) and not same_slur(n, o0) \
                and base(o0["qn"]) >= STR_REP_NEW_BOW["stroke_cc"] - EPS \
                and qn_to_sec(orig_end[id(o0)]) - qn_to_sec(o0["qn"]) >= STR_REP_NEW_BOW["sus_min_s"] - EPS \
                and not any(sp_[0] - EPS <= o0["qn"] < sp_[1] - EPS
                            for sp_ in ((STR_REP_DETACH or {}).get("at") or {}).get(tname, [])):
            # mvt1 c44 (critic A #2, scope): an unslurred same-pitch Sus MAX repeat at "stroke_cc" or louder, lasting
            # "sus_min_s" or more (REP_SPLIT strokes included), is a new bow with the STR_REP_NEW_BOW gap (it kept
            # min(0.03 qn, 10%) or min(0.04 qn, 10%): 85 such repeats dipped a median 3.5 dB in the stem, 2.3 in the
            # master). Not inside STR_REP_DETACH spans
            n["end"] = e0 - min(e0 - qn_before(e0, STR_REP_NEW_BOW["gap_s"]), STR_REP_NEW_BOW["frac"] * dur)
            rep_sus_gaps.append(round(o0["qn"], 3))
            if _stroke_fall_ok():   # mvt3 c21 (critic A c21 #5): the "sus_min_s" class takes the stroke fall too
                F_ = STR_REP_NEW_BOW["stroke_fall"]
                fc_ = F_.get("fall_cc_loud", F_.get("fall_cc", 0)) if base(o0["qn"]) > 90 else F_.get("fall_cc", 0)
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], F_.get("fall_s", 0.04)))
                cc_falls.append((fa_, n["end"], fc_, max(0.01, e0 - n["end"])))
                stroke_falls.append(round(o0["qn"], 3))
            o0["rep_sus_gap"] = True   # mvt1 c45 (critic A #1; ported mvt3 c04): it takes the string re-tongue lead
        elif chord_rep_:
            # mvt3 c07 (critic A #5, S1): a same-pitch repeat of one voice inside a div. chord (the other voice moving or
            # repeating), not under one slur, at "stroke_cc" or louder: the voice's note before ends with the
            # STR_REP_NEW_BOW "chord" gap (it kept the 0.03 qn chord re-bow gap: Vln I / II 972-976 dipped 1.6-3.8 dB)
            C_ = dict(STR_REP_NEW_BOW, **STR_REP_NEW_BOW["chord"])
            # mvt3 c11 (critic A #4): "head_gap_s" (optional): a repeat that starts a new slur (a new bow after a slur)
            # takes this longer gap, so it breaks more clearly than a louré repeat inside a slur (the portato gap)
            o_r_ = next((o_ for o_ in nxt if o_["pitch"] == n["pitch"]), o0)
            if C_.get("head_gap_s") and o_r_.get("slur") is not None and not any(
                    x_.get("slur") == o_r_["slur"] and x_["qn"] < o_r_["qn"] - EPS for x_ in ns):
                C_["gap_s"] = C_["head_gap_s"]
                chord_head_gaps.append(round(e0, 3))
            n["end"] = e0 - min(e0 - qn_before(e0, C_["gap_s"]), C_["frac"] * dur)
            rep_sus_gaps.append(round(e0, 3))
        elif REP_SPLIT.get("gap_s") and family == "string" and same_pitch and len(nxt) == 1 \
                and ((_rep_stroke(n) and _rep_stroke(o0)) or _plain_rep(n, o0)) and not n.get("meas_trem") \
                and gate_bpm(n["qn"]) >= REP_SPLIT["min_bpm"] - EPS \
                and base(o0["qn"]) >= REP_SPLIT.get("gap_min_cc", 0) - EPS:
            # mvt1 c51 (critic A c51 #1, S1; ported mvt3 c10, critic A #1): a stroke followed by a same-pitch stroke
            # ends max(gap_min_s, min(gap_s, frac x slot)) before the next onset (the Finale's basses' eighths kept
            # 0.03 qn, 8-12 ms: master band dips median 2.2-3.1 dB, half under 3 dB)
            slot_ = qn_to_sec(e0) - qn_to_sec(n["qn"])
            g_ = max(REP_SPLIT.get("gap_min_s", 0.0), min(REP_SPLIT["gap_s"], REP_SPLIT.get("frac", 1.0) * slot_))
            n["end"] = max(n["qn"] + 0.25 * dur, qn_before(e0, g_))
            rep_split_gaps.append(round(o0["qn"], 3))
        elif n.get("rep_stac"):
            n["end"] = e0 - 0.02   # mvt1 c04 (A #1): written length minus 0.02 qn
        elif n.get("rep_sus") or n.get("short_stroke"):
            n["end"] = e0 - min(0.04, 0.1 * dur)   # mvt1 c04 (A #1): a short bow change before the next stroke
        elif same_pitch and any(abs(o0["qn"] - r_) < 0.02 for r_ in REP_RETONGUE_AT.get(tname, [])):
            n["end"] = e0 - min(0.06, 0.15 * dur)   # c23 (A #4): a listed untied repeat is re-tongued audibly
        elif same_pitch and WIND_REP_RETONGUE and family in ("wind", "brass") \
                and (not is_leg or (WIND_REP_AFTER_SLUR and n["slur"] is not None)) \
                and ((family == "wind" and rep_row_of(o0) is not None)   # mvt1 c39 (A #3): a slurred repeat on the row
                     or not (n["slur"] is not None and o0.get("slur") == n["slur"]
                             and not (WIND_REP_PORTATO and near(o0["qn"], ten_q) and not o0.get("sost")
                                      and not o0.get("sost_rep") and not o0.get("portato_join")))):
            # mvt1 c34 (critic C #4): WIND_REP_PORTATO also takes a same-slur repeat whose second note has a tenuto
            # mvt1 c11 (critic A #5): also when the note is a slur's last note on the legato row (Tbn1/Hn4 453 -> 456:
            # 0.028 s gap, dips +0.4 / -2.1 dB): the unslurred repeat after a slur is a new tongue stroke too
            # mvt1 c06 (A #2): an unslurred wind/brass repeat is a new tongue stroke: a gap of gap_s (at most frac of
            # the note) measured back from the next onset, and a CC11 fall over the note's last fall_s, back at the onset
            R_ = dict(WIND_REP_RETONGUE)
            for k_, v_ in WIND_REP_RETONGUE_BY.items():   # mvt1 c07 (A #2): horns' release and hall fill 0.06 s
                if (k_[0].isupper() and tname.startswith(k_)) or k_ == family:
                    R_.update(v_)
                    break
            if WIND_REP_RETONGUE_SHORT and dur <= WIND_REP_RETONGUE_SHORT["max_qn"] + EPS \
                    and gate_bpm(n["qn"]) >= WIND_REP_RETONGUE_SHORT["min_bpm"] - EPS:
                R_.update({k_: v_ for k_, v_ in WIND_REP_RETONGUE_SHORT.items() if k_ not in ("max_qn", "min_bpm")})
            if rep_row_of(o0) is not None:
                # mvt1 c37 (critic A #3): the repetition row re-tongues by itself. mvt1 c38 (critics A #1, C #2): the
                # c37 0.03 s gap and no fall separated less than the emulation; the repeat now keeps the re-tongue's own
                # gap and CC11 fall (R_), with the gap clamped to REP_ROW_GAP_S (min, max): clear of the clarinet
                # "Leg Slur Rep" 30 ms VoiceTimer and inside the 200 ms NoteTimer of the re-tongue groups
                if isinstance(REP_ROW_GAP_S, (tuple, list)):
                    g_ = min(REP_ROW_GAP_S[1], max(REP_ROW_GAP_S[0], R_["gap_s"]))
                    n["end"] = e0 - min(e0 - qn_before(e0, g_), R_["frac"] * dur)
                    if R_.get("fall_cc"):
                        fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], R_["fall_s"]))
                        cc_falls.append((fa_, n["end"], R_["fall_cc"], max(0.01, e0 - n["end"])))
                else:   # c37: a fixed short gap (at most half the note), no fall
                    n["end"] = e0 - min(e0 - qn_before(e0, REP_ROW_GAP_S), 0.5 * dur)
                rep_row_reps.append(round(o0["qn"], 3))
                continue
            n["end"] = e0 - min(e0 - qn_before(e0, R_["gap_s"]), R_["frac"] * dur)
            if R_.get("fall_cc"):
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], R_["fall_s"]))
                cc_falls.append((fa_, n["end"], R_["fall_cc"], max(0.01, e0 - n["end"])))
            rep_retongued.append(round(o0["qn"], 3))
        elif same_pitch:
            n["end"] = e0 - (min(0.06, 0.15 * dur) if is_leg else min(0.03, 0.1 * dur))
        elif WIND_DETACH and family in ("wind", "brass") and not is_leg \
                and not (n["slur"] is not None and o0.get("slur") == n["slur"]):
            # mvt1 c12 (critic A #2): an unslurred wind/brass note into a new pitch is tongued: it ends min(gap_s, frac
            # x its length) before the next onset (it kept its written end and crossfaded, so tongued lines sounded as
            # smooth as the slurs: brass holes -3.0 dB abutting vs -3.3 slurred, winds -3.6 vs -4.2). An ABUT_LEAD on
            # the next note ends this note the same distance before the moved onset (wind_detach_qn)
            wd_ = dict(WIND_DETACH, **WIND_DETACH.get("by", {}).get(family, {}))   # per-family override
            cut_ = min(e0 - qn_before(e0, wd_["gap_s"]), wd_["frac"] * dur)
            n["end"] = e0 - cut_
            n["wind_detach_qn"] = cut_
            if wd_.get("fall_cc") and dur <= WIND_DETACH_FALL_MAX_QN + EPS:
                # mvt1 c14 (critic A #3): a gap alone does not separate brass eighths (0.06-0.075 s holed -3.1 dB, as
                # slurred): a CC11 fall over the note's last fall_s, back at the next onset
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], wd_.get("fall_s", 0.10)))
                cc_falls.append((fa_, n["end"], wd_["fall_cc"], max(0.01, e0 - n["end"])))
        elif is_leg:
            o = nxt[0]
            # c14 (A #3); mvt1 c20: a run span's last note into a target outside the span overlaps by LEG_OVERLAP (the
            # output stage then moves its end with the target's lead)
            ov_ = FAST_LEG_OVERLAP if (o.get("fast_leg") or (n.get("fast_leg") and n.get("stacleg"))) else LEG_OVERLAP
            if (o.get("art") == n["art"] or (family == "string" and _lg((o.get("art") or "")))) \
                    and same_slur(n, o):
                n["end"] = e0 + ov_
                o["leg_target"] = True
                o["leg_prev"] = n
            elif o.get("bc_from") == id(n):
                n["end"] = e0 + ov_
                o["leg_target"] = True
                o["leg_prev"] = n
            elif o.get("art") and _lg(o["art"]):
                n["end"] = e0 - min(0.05, 0.15 * dur)
            elif o.get("wide_leg"):
                # mvt1 c33 (critic C #3): into a WIND_WIDE_LEG re-tongue: the slur-break gap, so the re-tongue lead
                # (RETONGUE_LEAD_S) applies and the keyswitch to the Sus row falls in the gap
                n["end"] = e0 - min(0.05, 0.15 * dur)

    # mvt1 c36 (critic C #1): SUBITO_FRESH, the legato joins into a subito-softer note are undone: no legato target, the
    # note before it ends with the slur-break gap (min(0.05 qn, 15% of its length)); the lead pass gives the "fresh" entry
    # lead (or the re-tongue lead) and the output stage cuts the old note 0.03 qn before the moved onset
    for o in ns:
        if not o.get("subito_fresh"):
            continue
        if not (o.get("fresh") or o.get("leg_target") or o.get("bc_from") is not None):
            continue   # a tongued wind/brass re-attack: unchanged
        o["fresh"] = True
        subito_fresh.append(round(o["qn"], 3))
        o["leg_target"] = False
        o.pop("leg_prev", None)
        o.pop("short_sus_join", None)
        o.pop("bc_from", None)
        for p_ in ns:
            if p_ is not o and p_["qn"] < o["qn"] - EPS and p_["end"] > o["qn"] - 0.1 and orig_end[id(p_)] <= o["qn"] + 0.1:
                d_ = orig_end[id(p_)] - p_["qn"]
                p_["end"] = min(p_["end"], o["qn"] - min(0.05, 0.15 * d_))

    # mvt1 c03: ART_SPANS notes with "full_len" play their full written value (a same-pitch repeat still gets 0.005 qn
    # at the output guard)
    for n in ns:
        if n.get("art_span", {}).get("full_len"):
            n["end"] = orig_end[id(n)]
        if n.get("art_span", {}).get("len_frac"):   # mvt3 c16
            n["end"] = n["qn"] + n["art_span"]["len_frac"] * (orig_end[id(n)] - n["qn"])
    # c14 (A #1): marcato: the unaccented notes at MARC_LEN of their written value; accented notes of 1 qn or more end
    # 0.1 qn early, so each new note has a break before it
    for n in ns:
        if n.get("marc"):
            n["end"] = n["qn"] + MARC_LEN * (orig_end[id(n)] - n["qn"])
        elif in_marc(n["qn"]) and n["qn"] in accent_q and orig_end[id(n)] - n["qn"] >= 1.0 - EPS:
            c_ = next((v_ for k_, v_ in MARC_ACC_CUT_AT.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), 0.1)
            n["end"] = min(n["end"], orig_end[id(n)] - c_)   # c15 (A #4): per-onset cut

    # mvt1 c02 (A #1): the detached hammer strokes
    det_n = 0
    for n in ns:
        if id(n) in det_cut:
            d_ = orig_end[id(n)] - n["qn"]
            n["end"] = min(n["end"], orig_end[id(n)] - DETACH_ACCENTS["gap_qn"])
            n["det_cut"] = True
            det_n += 1

    # c03 (C #2): the after-grace run: main note held into the first grace, each grace overlapping the next, the last
    # overlapping the target; all on one legato articulation at velocity 127 (fastest transitions)
    for tgt in [n for n in ns if n.get("grace_target")]:
        gs = sorted([n for n in ns if n.get("grace") == id(tgt)], key=lambda n: n["qn"])
        if not gs:
            continue
        chain = gs + [tgt]
        mains = [n for n in ns if n["qn"] < gs[0]["qn"] - EPS and not n.get("grace") and orig_end[id(n)] > gs[0]["qn"] - 0.5]
        if mains:
            m = max(mains, key=lambda n: n["qn"])
            m["end"] = gs[0]["qn"] + LEG_OVERLAP
            chain = [m] + chain
        for a_, b_ in zip(chain, chain[1:]):
            a_["end"] = b_["qn"] + LEG_OVERLAP
            b_["leg_target"] = True
            b_["leg_prev"] = a_
            b_["run"] = id(tgt)
        tgt.pop("run", None)

    for n in ns:   # c07 (A #1): the portato pulse on joined Largamente notes
        # c16 (A #5): not with SOST_HOLD_THROUGH (Flute 2, the only track with these joins, fell 122 -> 109 CC at every
        # onset of bars 61-62, 0.8-6.7 dB; the hold-through ramp carries the line, the portato is in the legato join)
        if n.get("sost") and n.get("leg_target") and not SOST_HOLD_THROUGH:
            notches.append((n["qn"], SOST_NOTCH))
        if n.get("portato_join") and n.get("leg_target"):   # mvt1 c04 (A #2): the portato pulse of a joined tenuto
            notches.append((n["qn"], PORTATO_JOIN_NOTCH.get(tname, SOST_NOTCH)))


    # c04 (A #1): printed arpeggios (rolled chords), per staff; a roll marked on both staves is one roll from the bottom
    arp_marks = collections.defaultdict(set)
    if family == "harp":
        for s_ in staves:
            for q_, k_, v_ in ev[s_]:
                if k_ == "arpeggio":
                    arp_marks[round(q_, 4)].add(s_)

    def arp_chord(n):
        st = arp_marks.get(round(n["qn"], 4))
        if not st or n.get("staff") not in st:
            return []
        return sorted([o for o in ns if abs(o["qn"] - n["qn"]) < EPS and o.get("staff") in st], key=lambda o: o["pitch"])

    def arp_top(n):
        ch = arp_chord(n)
        return len(ch) >= 2 and ch[-1] is n

    # velocities
    metric_n = collections.Counter()
    # mvt1 c06 (B #1): source velocities before any rule, for the plain velocity of a gentle accent
    src_vel = {id(n): n["vel"] for n in ns}
    marc_only_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] == "marcato"}

    def plain_vel(n):
        q_ = n["qn"]
        ref_ = sorted(src_vel[id(o)] for o in ns if o["qn"] not in accent_q and abs(o["qn"] - q_) <= ACC_PLAIN_WIN
                      and abs(base(o["qn"]) - base(q_)) <= 4 and not o.get("grace") and id(o) in src_vel)
        if ref_:
            return ref_[len(ref_) // 2]
        ex_ = ACC_SRC_EXTRA["marcato"] if q_ in marc_only_q else ACC_SRC_EXTRA["accent"]
        return max(1, src_vel[id(n)] - ex_)
    acc_vel_fixed = []
    leg_vel_span = []   # mvt1 c40 (critic A #1)
    for n in ns:
        sec = qn_to_sec(n.get("vel_end", orig_end[id(n)])) - qn_to_sec(n["qn"])   # mvt1 c05: vel_end (A #1 merges)
        if n.get("grace"):
            n["vel"] = 127
        elif n.get("leg_target"):   # legato patches: velocity sets transition speed (HO manual 2.1.1); loudness is CC11
            if family == "string" and n["qn"] >= CODA_SOFT["from_qn"] and base(n["qn"]) <= CODA_SOFT["max_cc"]:
                n["vel"] = CODA_SOFT["vel"]   # c08 (C #4): soft coda joins, not the v124 bump
            elif family == "string" and in_sost(n["qn"]):
                n["vel"] = SOST_STR_LEG_VEL   # c10 (C #4d): broad Largamente joins, no 17-19 dB transition peaks
            elif family in LEG_VEL_STRONG:   # c02: strings/horns arrived 220-385 ms late at v60-100
                lvs_t_ = LEG_VEL_STRONG.get(tname, LEG_VEL_STRONG[family])   # mvt3 c15: a track key overrides its family
                if isinstance(lvs_t_, list):
                    # mvt3 c07 (critic A #2, EW research batch 4: legato velocity follows the dynamic): a list of
                    # (dynamic-lane value at or below, velocity), read on the target's dynamic lane; the last entry
                    # covers everything above
                    n["vel"] = next((v_ for c_, v_ in lvs_t_ if base(n["qn"]) <= c_), lvs_t_[-1][1])
                else:
                    n["vel"] = lvs_t_[0] if sec < 0.9 else lvs_t_[1]
            elif n.get("sost"):   # c07 (A #1): broad ff portato joins: a firm, quick transition
                n["vel"] = SOST_VEL
            elif tname == "Cor anglais":   # c04 (A #5): its v60/v80 transitions measured 150-185 ms
                n["vel"] = 100 if sec < 0.45 else (90 if sec < 0.9 else 80)
            else:
                n["vel"] = 100 if sec < 0.45 else (80 if sec < 0.9 else 60)
            ldd_ = (next((v_ for k_, v_ in LEG_VEL_DYN_ADD.items() if k_[0].isupper() and k_ in tname), None)
                    or LEG_VEL_DYN_ADD.get(family)) if LEG_VEL_DYN_ADD and family not in LEG_VEL_STRONG else None
            if ldd_ and base(n["qn"]) >= ldd_[0] and not n.get("sost") and not (
                    family == "string" and (n["qn"] >= CODA_SOFT["from_qn"] or in_sost(n["qn"]))):
                n["vel"] = min(127, n["vel"] + ldd_[1])   # mvt3 c07 (critic A #2): loud wind targets change cleanly
            lvs_ = next((v_ for a_, b_, v_ in LEG_VEL_SPANS.get(tname, []) if a_ - EPS <= n["qn"] < b_ - EPS), None)
            if lvs_ is not None:   # mvt1 c40 (critic A #1): LEG_VEL_SPANS
                n["vel"] = lvs_
                leg_vel_span.append(round(n["qn"], 3))
        if family in ("harp", "harm"):   # the harp is velocity-driven; CC11 stays constant (c01)
            v = base(n["qn"])
            n["vel"] = int(round(value_at([(22, 46), (34, 52), (46, 64), (58, 76), (72, 90), (88, 100), (104, 110), (118, 118)], v)))
            if family == "harp" and arp_top(n):   # c04 (A #1): the top note of a rolled chord carries the line
                n["vel"] = min(127, n["vel"] + 4)
            elif family == "harp" and n["pitch"] in HARP_PITCH_VEL:   # c09 (A #6): even out the sample set by pitch
                n["vel"] = max(1, min(127, n["vel"] + HARP_PITCH_VEL[n["pitch"]]))
            if family == "harm" or n.get("harm_on"):
                n["vel"] -= HARM_VEL_CUT
            if n.get("gliss_vel"):   # mvt3 c01 (critic A #5): a written-out glissando keeps its own velocity rise
                n["vel"] = int(n["gliss_vel"])
        if family == "timp" and n["art"].endswith("Lng"):   # strokes: below vel 53 the felt patch is near silent
            v = base(n["qn"])
            n["vel"] = max(n["vel"], int(round(value_at([(22, 52), (34, 56), (46, 64), (58, 72), (72, 80), (88, 96), (104, 110)], v))))
        if n.get("rep_sus") or n.get("short_stroke") or n.get("down_stroke"):   # mvt1 c04 (A #1): repeated strokes at the printed level (c06: down-bow strokes)
            n["vel"] = int(round(value_at(REBOW_VEL_BY_CC, base(n["qn"]))))
        elif n.get("rep_stac"):
            n["vel"] = int(round(value_at(REP_SPLIT["stac_vel"], base(n["qn"]))))
        is_acc_ = n["qn"] in accent_q or any(abs(n["qn"] - q) < 0.01 and d in ("sf", "sfz") for q, d in marks)
        if METRIC_VEL and (family == "harp" or "izz" in (n.get("art") or "")) and not is_acc_ \
                and not any(a_ - EPS <= n["qn"] < b_ for a_, b_ in LEAD_SPANS.get(tname, [])) \
                and not (family == "harp" and arp_chord(n) and not arp_top(n)):
            n["vel"] = max(1, min(127, n["vel"] + METRIC_VEL[beat_kind(n["qn"])]))   # c16 (C #4)
            metric_n[beat_kind(n["qn"])] += 1
        if TIMP_METRIC_VEL and family == "timp" and (n.get("art") or "").endswith("Lng") and not is_acc_ \
                and not n.get("tie_stroke") and base(n["qn"]) >= TIMP_METRIC_VEL.get("min_cc", DYN["f"]) - EPS:
            # mvt1 c07 (critic A #5): pickups and off-beats lighter than the beats they lead to
            bk_ = beat_kind(n["qn"])
            if bk_ == "weak":
                bk_ = "beat" if abs(n["qn"] - round(n["qn"])) < 0.01 else "off"
            else:
                bk_ = {"downbeat": "down"}.get(bk_, bk_)
            jit_ = __import__("random").Random(int(round(n["qn"] * 1000)) + 7).randint(
                -TIMP_METRIC_VEL.get("jit", 0), TIMP_METRIC_VEL.get("jit", 0))
            n["vel"] = max(56, min(127, n["vel"] + TIMP_METRIC_VEL.get(bk_, 0) + jit_))
            metric_n["timp_" + bk_] += 1
        if n["qn"] in accent_q and family not in GENTLE_ACCENT:
            n["vel"] = min(127, n["vel"] + 10)
        elif n["qn"] in accent_q and GENTLE_ACCENT.get(family, {}).get("vel_add") is not None \
                and n["vel"] == src_vel.get(id(n)) and not n.get("leg_target") and not n.get("grace"):
            # mvt1 c06 (B #1): only notes still at their source velocity (rules that set a velocity keep theirs)
            pv_ = min(src_vel[id(n)], plain_vel(n) + GENTLE_ACCENT[family]["vel_add"])
            if pv_ != n["vel"]:
                acc_vel_fixed.append((round(n["qn"], 3), n["vel"], pv_))
                n["vel"] = pv_
        if any(abs(n["qn"] - q) < 0.01 and d in ("sf", "sfz") for q, d in marks):   # c02: sf weight
            n["vel"] = min(127, n["vel"] + 15)
        if family == "timp" and round(n["qn"], 2) in TIMP_VEL:   # c03 (B #1): pp strokes 6 dB under qn 277
            n["vel"] = max(n["vel"], TIMP_VEL[round(n["qn"], 2)])
        if n.get("sost_rep") or n.get("sost_sus"):
            n["vel"] = max(n["vel"], SOST_VEL)
        if n.get("portato_join") and n.get("leg_target"):   # mvt1 c04 (A #2): a firm portato join
            n["vel"] = SOST_VEL
        if n.get("port_vel"):   # c11 (A #4)
            n["vel"] = n["port_vel"]
        if n.get("detach"):     # c11 (C #6)
            n["vel"] = max(n["vel"], SHORT_SUS_DETACH["vel"])
        if n.get("fast_leg") and n.get("leg_target"):   # c14 (A #3)
            n["vel"] = FAST_LEG_VEL
        if n.get("detache_t"):   # c15 (A #5)
            n["vel"] = DETACHE_VEL
        if n.get("stacleg"):   # c16 (A #3)
            n["vel"] = STACLEG_VEL
        if n.get("marc"):   # c14 (A #1): short articulation, dynamic from velocity
            n["vel"] = int(round(value_at(sorted(MARC_VEL.items()), base(n["qn"]))))
        if n.get("art_span"):   # mvt1 c03: ART_SPANS velocity: "vel_by_cc" table, else the note's velocity + "vel_add"
            sp_ = n["art_span"]
            n["vel"] = int(round(value_at(sp_["vel_by_cc"], base(n["qn"])))) if sp_.get("vel_by_cc") \
                else max(1, min(127, n["vel"] + sp_.get("vel_add", 0)))
            if sp_.get("vel_metric"):   # mvt3 c16: velocity by position in the bar, seeded variation
                bk_ = beat_kind(n["qn"])
                kd_ = "down" if bk_ == "downbeat" else ("mid" if bk_ == "mid" or abs(n["qn"] % 4.0 - 2.0) < 0.01
                                                        else ("beat" if abs(n["qn"] - round(n["qn"])) < 0.01 else "off"))
                jr_ = __import__("random").Random(int(round(n["qn"] * 1000)) + n["pitch"])
                n["vel"] = max(1, min(127, int(sp_["vel_metric"].get(kd_, n["vel"])) + jr_.randint(-sp_.get("vel_jit", 0), sp_.get("vel_jit", 0))))
        rv_ = (ROW_VEL_BY_CC.get(tname) or {}).get(n.get("art") or "")
        if rv_ and n["qn"] in stacc_q and not n.get("art_span") and not n.get("rep_stac") and not n.get("mt_alt"):
            n["vel"] = int(round(value_at(rv_, base(n["qn"]))))   # mvt3 c07 (critic A #3): ROW_VEL_BY_CC
        rvs_ = next((v_ for a_, b_, v_ in (ROW_VEL_SPANS.get(tname) or {}).get(n.get("art") or "", [])
                     if a_ - EPS <= n["qn"] < b_ - EPS), None)
        if rvs_ is not None:
            n["vel"] = int(rvs_)   # mvt3 c16: ROW_VEL_SPANS
        if SFP_VEL and not n.get("leg_target") and any(abs(n["qn"] - q) < 0.01 and d == "sfp" for q, d in marks):
            n["vel"] = max(n["vel"], SFP_VEL)   # mvt3 c02 (critic C #3)
        elif FP_VEL and not n.get("leg_target") and any(abs(n["qn"] - q) < 0.01 and d == "fp" for q, d in marks):
            n["vel"] = max(n["vel"], FP_VEL)   # mvt3 c09 (critic A #1): the fp's f attack (it played v53, the p velocity)
        vs = next((v_ for k_, v_ in VEL_SET.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), None)
        if vs is not None:   # c06 (C #6)
            n["vel"] = vs

    # last note's end, for rest detection
    def prev_end(q):
        ends = [o["end"] for o in ns if o["qn"] < q - EPS and o["end"] <= q + 0.05]
        busy = any(o["qn"] < q - EPS and o["end"] > q + 0.05 for o in ns)
        return None if busy else (max(ends) if ends else -1.0)

    def early_time(q):
        """c01: controller changes before an entry go into the preceding rest, not on the note."""
        pe = prev_end(q)
        if pe is None:
            return max(0.0, q - KS_LEAD)
        if pe < 0:
            return 0.0 if q > 0.5 else max(0.0, q - KS_LEAD)
        gap = q - pe
        if gap >= 0.3:
            return pe + min(0.5, gap * 0.25)
        return max(0.0, q - KS_LEAD)

    def ks_in_rest(q):
        """mvt3 c13: True when early_time(q) lies in a rest before q (not the fixed KS_LEAD before the note)"""
        pe = prev_end(q)
        return pe is not None and ((pe < 0 and q > 0.5) or (pe >= 0 and q - pe >= 0.3))

    # keyswitches at articulation changes; the patch state already selects the first one
    ks, cur, first_art = [], None, None
    for n in ns:
        a = n.get("art")
        rr_ = rep_row_of(n) if (a and REP_ROW.get(tname)) else None
        if rr_ and family in REP_ROW_REPEATS_ONLY and round(n["qn"], 3) not in rep_row_reps:
            rr_ = None   # mvt1 c38 (critic A #1): brass rows play the re-tongue on every note: repeats only
        if rr_ and (a in ("Sus MAX", "Sus Max", "Sus Non Vib", "Sus Non Vib MAX", "Sus Vib MAX")
                    or ("Slur" in rr_ and _lg(a))):
            a = rr_   # mvt1 c37 (critic A #3): REP_ROW (the keyswitch only)
            n["rep_row"] = rr_
        if a is None or a == cur:
            continue
        key = ks_lookup(stem, a)[1]
        if first_art is None:
            first_art = a
            # c03 (A #4): Tbn1's first two accents played Sus MAX although the state selects Sus Accent MAX; tracks that
            # enter after the start also send their first keyswitch, in the rest before the entry
            if n["qn"] >= 0.5:
                ks.append({"qn": round(early_time(n["qn"]), 4), "pitch": key, "art": a, "note": n, "rest": ks_in_rest(n["qn"])})
        else:
            ks.append({"qn": round(early_time(n["qn"]), 4), "pitch": key, "art": a, "note": n, "rest": ks_in_rest(n["qn"])})
        cur = a

    # CC11: printed dynamics + solo/cantabile/espr. boost + tenuto/accent weight
    # c02: string sections get +3 for espr./cantabile/dolce (+8 only for "solo"); winds/brass keep +8 for solo/espr./
    # cantabile and get +3 for "dolce" alone. The boost fades out between mp and f (none at f and above).
    boost_spans = []
    if family not in ("timp", "harp", "harm"):
        txts = sorted((q, t) for s in staves for q, k, v in ev[s] if k == "text" for t in [v[0].lower()])
        rs = sorted(set(r for s in staves for r in rest_starts(s, 3.0)))
        for i, (q, t) in enumerate(txts):
            if "tutti" in t and not has(t, "espr"):
                continue
            if has(t, "solo") and "tutti" not in t:
                amt = 0 if tname in SOLO_NO_BOOST else SOLO_BOOST   # c08 (C #5): CC1 instead (cc1_fn)
                # c32 (A #6): "Solo espr." on a section track listed in SOLO_NO_BOOST keeps the section's espr. boost
                if amt == 0 and family == "string" and any(has(t, w) for w in ("cantabile", "espr", "dolce")):
                    amt = SOFT_BOOST
            elif any(has(t, w) for w in ("cantabile", "espr")):
                amt = SOFT_BOOST if family == "string" else SOLO_BOOST
            elif has(t, "dolce"):
                amt = SOFT_BOOST
            else:
                continue
            # c32 (B #5a): a breathing indication ("(breathe ad lib.)") is not an expression change and does not end a boost
            txt_stops_ = [x for x, t_ in txts[i + 1:] if x > q + EPS and not any(w in t_ for w in BOOST_STOP_SKIP)]
            stop = min(txt_stops_ + [r for r in rs if r > q + EPS] + [END])
            if tname in TRACK_WINDOWS and tw_spans(tname)[1]:   # c10 (A #1): the solo's boost covers its window
                stop = min(txt_stops_ + [tw_end(tname, q)])
            boost_spans.append((q, stop, amt))
    bumps = []
    holds = []   # c08 (C #1): (start, end, CC) flat additions
    for n in ns:
        if near(n["qn"], ten_q):
            bumps.append((n["qn"], TENUTO_BUMP, 0.5))
            if in_sost(n["qn"]) and base(n["qn"]) >= DYN["f"]:
                # c08 (C #1): a tenuto arrival under "molto sostenuto" at f+ holds its weight (bump - 1) to the note end
                holds.append((n["qn"], orig_end[id(n)], TENUTO_BUMP - 1))
        acc_bump_ = ACCENT_BUMP_AT.get(tname, 0 if family in GENTLE_ACCENT else ACCENT_BUMP)
        if n["qn"] in accent_q and acc_bump_:
            bumps.append((n["qn"], acc_bump_, 0.3))   # c26: per-track bump

    # c02: phrase shaping on long notes (C5) and anti-bloom on soft re-struck string chords (B6), in CC11 units
    contours = []   # (start, end, kind)
    swell_caps = []   # c22 (B #1): (start, end, CC11 ceiling) for SWELL_CC_CAP pitches
    swell_cap_tab = SWELL_CC_CAP.get(tname, {})

    def joined_next(n):
        """c13 (A #2): the next note joins n (a bow-change legato target, or a legato target overlapped by n)."""
        return any(o is not n and (o.get("bc_from") == id(n) or (o.get("leg_target") and o.get("leg_prev") is n))
                   for o in ns)
    if family in ("wind", "brass", "string"):
        onsets = sorted({n["qn"] for n in ns})
        by_on = {}
        for n in ns:
            if n["qn"] not in by_on or orig_end[id(n)] > orig_end[id(by_on[n["qn"]])]:
                by_on[n["qn"]] = n
        rest1 = set(round(r, 4) for s in staves for r in rest_starts(s, 1.0))
        for q0, n in sorted(by_on.items()):
            e = orig_end[id(n)]
            if e >= END - 3.5 or q0 >= SE - 6:   # the final bars have their own fade
                continue
            inside = [o for o in onsets if q0 + EPS < o < e - EPS]
            in_hp = any(a < e - EPS and b > q0 + EPS for a, b, k in hps)
            sec = qn_to_sec(e) - qn_to_sec(q0)
            prevs = [o for o in ns if abs(orig_end[id(o)] - q0) < 0.05 and o["qn"] < q0 - EPS]
            same_pitch = any(o["pitch"] == n["pitch"] for o in prevs)
            if family == "string" and n.get("art") == "Sus MAX" and base(q0) <= DYN["p"] + 2 and prevs and not inside \
                    and not any(k_ == "cresc" and abs(b_ - q0) < 0.1 for a_, b_, k_ in hps):
                # c22 (C #3b): not on a crescendo's arrival note (the coda pp arrival at 286: Cb CC11 34 -> 40 -> 32,
                # an attack bump and a 5 dB fall after the printed < ; the bloomv rule already skips these, c10)
                contours.append((q0, e, "bloom"))
                continue
            if in_hp or inside or same_pitch:
                continue
            # c13 (A #2): a slur's last note is not a phrase end when the next note joins it (Leg BC / BC_SOFT
            # bow change): the line goes on, so no taper into the join
            ends_phrase = (n["slur"] is not None and slurs[n["slur"]][1] <= q0 + EPS and not joined_next(n)) \
                or near(e, breath_q) or round(e, 4) in rest1
            if n.get("marc") or n.get("flaut_join") or n.get("detache_t"):
                continue   # c14 (A #1): a marcato note decays by itself; c15: joined sul tasto chords, the detache test
            if sec >= 1.8:
                k_sw = "swell_taper" if ends_phrase else ("swell_sost" if in_sost(q0) else "swell")   # c14 (C #4)
                if any(a_ <= q0 < b_ for a_, b_ in ARRIVAL_HOLD_SPANS):   # c20 (C #1)
                    k_sw = "swell_sost"
                contours.append((q0, e, k_sw))
                if n["pitch"] in swell_cap_tab:
                    swell_caps.append((q0, e, swell_cap_tab[n["pitch"]]))
                elif "*" in swell_cap_tab and base(q0) <= SWELL_CAP_MAX_CC:   # c23 (B #1)
                    swell_caps.append((q0, e, base(q0) + swell_cap_tab["*"]))
            elif ends_phrase and sec >= 0.6:
                contours.append((q0, e, "taper"))
    phrase_shapes = []   # mvt3 c07: [(a, b, [(qn, offset), ...])]
    ps_cc1 = any(tname.startswith(p_) for p_ in CC1_DYN_TRACKS)
    ps_kinds = {}
    ps_hp = []           # intervals (qn) where the phrase shape fades out (printed hairpins, fp / sfp / sf)
    PS_ = PHRASE_SHAPE
    if PS_ and family in PS_["families"] and ns:
        for a_, b_, k_ in hps:
            ps_hp.append((a_, b_))
        for q_, d_ in marks:
            if d_ in ("fp", "sfp", "sf", "sfz"):
                ps_hp.append((q_, q_ + 1.0))
        groups_, cur_, cur_end = [], [], None
        for n in sorted(ns, key=lambda o: o["qn"]):
            if n.get("grace"):
                continue
            if cur_ and (qn_to_sec(n["qn"]) - qn_to_sec(cur_end) > PS_["gap_s"]
                         or (near(cur_end, breath_q) and n["qn"] >= cur_end - 0.05)):
                groups_.append(cur_)
                cur_ = []
            if not cur_:
                cur_end = orig_end[id(n)]
            cur_.append(n)
            cur_end = max(cur_end, orig_end[id(n)])
        if cur_:
            groups_.append(cur_)
        for g_ in groups_:
            a_ = g_[0]["qn"]
            b_ = max(orig_end[id(o)] for o in g_)
            if b_ >= END - 3.5 or a_ >= SE - 6:
                continue   # the final bars have their own fade
            t0_, t1_ = qn_to_sec(a_), qn_to_sec(b_)
            L_ = t1_ - t0_
            if L_ < PS_["min_s"]:
                continue
            last_ = max(g_, key=lambda o: o["qn"])
            no_taper = last_["qn"] in accent_q or any(k_ == "cresc" and abs(hb_ - last_["qn"]) < 0.1 for ha_, hb_, k_ in hps)
            pk_off, pk_at = PS_["peak"]
            # mvt3 c07 (research batch 6, Balfe sketches): the shape by music type. "build": the printed level rises
            # by build_cc or more over the phrase, or a crescendo ends in its last quarter: enter low, peak at 0.95, no
            # taper. "drive" (research batch 7, superseding batch 6's "fanfare"): outside the listed lyrical spans at
            # drive_min_bpm or faster: enter high, peak early, fall to the end. "fanfare" (optional): accented brass.
            # Otherwise "lyric": the centred arch
            kind_ = "lyric"
            if PS_.get("types"):
                if base(b_ - 0.05) - base(a_) >= PS_["types"]["build_cc"] or any(
                        k_ == "cresc" and a_ + 0.75 * (b_ - a_) <= hb_ <= b_ + 0.1 and hb_ - ha_ >= 0.25 * (b_ - a_)
                        for ha_, hb_, k_ in hps):
                    kind_ = "build"
                elif "drive" in PS_["types"] and not any(la_ - EPS <= a_ < lb_ for la_, lb_ in PS_["types"].get("lyric_spans", [])) \
                        and bpm_at(a_) >= PS_["types"].get("drive_min_bpm", 0):
                    kind_ = "drive"   # batch 7: driving music starts high and falls, or peaks early
                    # mvt3 c09 (critic B #3, S3): a driving phrase that enters on a subito-softer mark, or on a printed
                    # level drop_cc or more under the level just before it, takes no positive offset ("drop": held at the
                    # printed level, then the drive's end fall); the +6 entry and +10 peak put the strings about 11 CC
                    # over the sub. p at bar 219 and the master fell 1.7 dB
                    dr_ = PS_["types"].get("drop")
                    if dr_ and (any(abs(a_ - x_) < 0.02 for x_ in sub_soft_q)
                                or base(a_ + 0.01) <= base(a_ - 0.05) - dr_.get("cc", 6)):
                        kind_ = "drop"
                elif "fanfare" in PS_["types"] and family == "brass" and (
                        g_[0]["qn"] in accent_q or sum(o["qn"] in accent_q for o in g_) * 2 >= len(g_)):
                    kind_ = "fanfare"
            ps_kinds[kind_] = ps_kinds.get(kind_, 0) + 1
            if kind_ == "build":
                tp_ = [(0.0, PS_["start"]), (0.95 * L_, pk_off), (L_, pk_off)]
            elif kind_ == "drive":
                d0_, (dpk_, dat_), d1_ = PS_["types"]["drive"]   # (entry offset, (peak offset, share), end offset)
                tp_ = [(0.0, d0_), (dat_ * L_, dpk_), (L_, d1_ if not no_taper else dpk_)]
            elif kind_ == "drop":
                d1_ = PS_["types"]["drive"][2]
                tp_ = [(0.0, 0.0), (PS_["types"]["drive"][1][1] * L_, 0.0), (L_, d1_ if not no_taper else 0.0)]
            elif kind_ == "fanfare":
                ft_ = PS_["types"]["fanfare"]   # (offset at entry, offset at the end)
                tp_ = [(0.0, ft_[0]), (L_, ft_[1])]
            else:
                pk_t = L_ * min(0.62, max(0.33, pk_at))
                tp_ = [(0.0, PS_["start"])] + [(t_, v_) for t_, v_ in PS_["rise"] if t_ < pk_t] + [(pk_t, pk_off)]
                pe_t, pe_v = PS_["pre_end"]
                if no_taper:
                    tp_ += [(L_, pk_off)]
                else:
                    if L_ - pe_t > pk_t:
                        tp_ += [(L_ - pe_t, pe_v)]
                    tp_ += [(L_, PS_["end"])]
            phrase_shapes.append((a_, b_, [(sec_to_qn(t0_ + t_), v_) for t_, v_ in tp_], kind_))
        if phrase_shapes:   # no double shaping: the per-note swells / tapers inside a shaped phrase are dropped
            contours[:] = [c_ for c_ in contours if not (c_[2] in ("swell", "swell_taper", "taper")
                                                          and any(a_ - EPS <= c_[0] < b_ for a_, b_, *_ in phrase_shapes))]
            for n in ns:
                if n["pitch"] in swell_cap_tab and any(a_ - EPS <= n["qn"] < b_ for a_, b_, *_ in phrase_shapes):
                    swell_caps.append((n["qn"], orig_end[id(n)], swell_cap_tab[n["pitch"]]))

    if phrase_shapes:
        print(f"  {tname}: PHRASE_SHAPE on {len(phrase_shapes)} phrases {ps_kinds}", file=sys.stderr)

    def ps_scale(v_):
        sc_ = PS_["scale"]
        for nm_, hi_ in (("ppp", 28), ("pp", 40), ("p", 52), ("mp", 65), ("mf", 80), ("f", 100), ("ff", 119)):
            if v_ <= hi_:
                return sc_.get(nm_, 1.0)
        return sc_.get("fff", 0.2)

    def ps_weight(q):
        w_ = 1.0
        fq_ = PS_["hp_fade_s"] * bpm_at(q) / 60.0
        for ha_, hb_ in ps_hp:
            if ha_ - fq_ < q < hb_ + fq_:
                d_ = (ha_ - q) if q < ha_ else ((q - hb_) if q > hb_ else 0.0)
                w_ = min(w_, max(0.0, d_ / fq_))
        return w_

    # mvt3 c09 (critic B #3, S3): inside a shaped phrase, from a subito-softer mark or a printed drop of "drop" cc or more
    # to the next hairpin start, the phrase offset is not positive (a held chord into the sub. p at bar 219 kept the
    # lyric arch's +12 and the strings sat about 11 CC over the p)
    ps_drops = []
    if PS_ and phrase_shapes and (PS_.get("types") or {}).get("drop"):
        dcc_ = PS_["types"]["drop"].get("cc", 6)
        for x_ in sorted({q_ for q_, d_ in marks if d_ not in ("sf", "sfz", "fp", "sfp")}):
            if any(abs(x_ - y_) < 0.02 for y_ in sub_soft_q) or base(x_ + 0.01) <= base(x_ - 0.05) - dcc_:
                nh_ = min([ha_ for ha_, hb_, k_ in hps if ha_ > x_ + 0.01] + [x_ + 64.0])
                ps_drops.append((x_, nh_))

    def phrase_off(q):
        for a_, b_, pts_, kd_ in phrase_shapes:
            if a_ - EPS <= q < b_:
                o_ = value_at(pts_, q)
                if o_ > 0 and any(x_ - EPS <= q < y_ for x_, y_ in ps_drops):
                    o_ = 0.0
                bq_ = base(q)
                sc_ = PS_["types"].get("fanfare_scale", 1.0) if kd_ == "fanfare" else ps_scale(bq_)
                o_ *= sc_ * ps_weight(q)
                cap_ = (PS_.get("cap") or {}).get(family)
                if cap_ is not None and o_ > 0:
                    o_ = min(o_, max(0.0, cap_ - bq_))
                return max(o_, PS_["floor"] - bq_) if o_ < 0 else o_
        return 0.0

    bcsoft_n = 0
    if family == "string":   # c07 (A #3): CC11 dip under the v124 Leg BC bump on soft long notes
        for n in ns:
            q0, e = n["qn"], orig_end[id(n)]
            if n.get("art") == "Leg BC MAX" and n.get("leg_target") and base(q0) <= BCSOFT["max_cc"] \
                    and qn_to_sec(e) - qn_to_sec(q0) >= BCSOFT["min_s"] \
                    and not any(k_ == "cresc" and abs(a_ - q0) <= 0.25 for a_, b_, k_ in hps):
                # c09 (A #2 #4): not where a crescendo starts (Vla/Vln II qn 146 dipped 8-11 dB into the pp < mp)
                contours.append((q0, q0 + BCSOFT["t_out"] * bpm_at(q0) / 60, "bcsoft"))
                bcsoft_n += 1

    def contour(q):
        v = 0.0
        for a, b, k in contours:
            if not (a - EPS <= q < b):
                continue
            x = (q - a) / (b - a)
            if k == "bcsoft":   # c07 (A #3): 0 -> -depth by t_in, held to t_hold, back to 0 at t_out (seconds)
                t = (q - a) * 60 / bpm_at(a)
                B_ = BCSOFT
                if t < B_["t_in"]:
                    v -= B_["depth"] * t / B_["t_in"]
                elif t < B_["t_hold"]:
                    v -= B_["depth"]
                else:
                    v -= B_["depth"] * max(0.0, (B_["t_out"] - t) / (B_["t_out"] - B_["t_hold"]))
            elif k == "bloom":   # +6 at the onset, -2 by 1 qn, back to 0 at the end
                t = q - a
                v += 6 - 8 * t if t < 1 else -2 + 2 * min(1.0, (t - 1) / max(0.25, b - a - 1))
            elif k == "swell_sost":   # c14 (C #4): +4 at 40%, held to the end
                v += 4 * x / 0.4 if x < 0.4 else 4.0
            elif k.startswith("swell"):   # +4 at 40% of the note, -2 at its end
                sw = 4 * x / 0.4 if x < 0.4 else 4 - 6 * (x - 0.4) / 0.6
                if k == "swell_taper" and x > 0.5:
                    sw = min(sw, -6 * (x - 0.5) / 0.5)
                v += sw
            elif k == "taper":
                v += -6 * (x - 0.5) / 0.5 if x > 0.5 else 0.0
        return v

    def notch(q):
        v = 0.0
        for nq, depth in notches:
            if nq - 0.06 <= q < nq:
                v -= depth * (q - (nq - 0.06)) / 0.06
            elif nq <= q < nq + 0.25:
                v -= depth * (1 - (q - nq) / 0.25)
        return v

    for mq in merged_ten:   # c03: the portato / tenuto weight stays on merged notes
        bumps.append((mq, TENUTO_BUMP, 0.5))

    def final(q):
        v = base(q) + notch(q)
        boost = max([amt for a, b, amt in boost_spans if a - EPS <= q < b - EPS], default=0)
        v += boost * max(0.0, min(1.0, (DYN["f"] - base(q)) / 30))
        for b0, amt, ln in bumps:
            if b0 - EPS <= q < b0 + ln:
                v += amt * (1 - (q - b0) / ln)
        for h0, h1, amt in holds:   # c08 (C #1): the tenuto bump (TENUTO_BUMP over 0.5 qn) never falls below amt
            if h0 - EPS <= q < h1:
                v += max(0.0, amt - TENUTO_BUMP * max(0.0, 1 - (q - h0) / 0.5))

        v += contour(q)
        if phrase_shapes and not ps_cc1:
            v += phrase_off(q)   # mvt3 c07: PHRASE_SHAPE (CC1_DYN_TRACKS: in CC1, cc1_fn0)
        for ca_, cb_, cap_ in swell_caps:   # c22 (B #1)
            if ca_ - EPS <= q < cb_ and base(q) <= cap_:
                v = min(v, cap_)
        for fa, fb, fd, *fr_ in cc_falls:   # c15 (A #6); mvt1 c06: an optional return length (qn)
            rl_ = fr_[0] if fr_ else 0.3
            if fa <= q < fb:
                v -= fd * (q - fa) / (fb - fa)
            elif fb <= q < fb + rl_:
                v -= fd * (1 - (q - fb) / rl_)
        if q >= SE - 0.5 and v > 8:   # c02: the final ppp chord dies away (with the volume fade in vol_db)
            v += (8 - v) * min(1.0, (q - (SE - 0.5)) / 0.5)   # c07 (C #5): from 303.5 (was 302 -> 304)
        return v

    breaks = [p[0] for p in pts] + [x for a, b, _ in boost_spans for x in (a, b)] + [x for b0, _, ln in bumps for x in (b0, b0 + ln)] \
        + [x for h0, h1, _ in holds for x in (h0, h0 + 0.1, h1)] \
        + [x for a, b, _ in contours for x in (a, b, a + 0.4 * (b - a), a + 0.5 * (b - a), min(b, a + 1))] + [SE - 2, SE - 0.5, SE] \
        + [x for nq, _ in notches for x in (nq - 0.06, nq, nq + 0.25)] \
        + [x for fa, fb, _, *fr_ in cc_falls for x in (fa, fb, fb + (fr_[0] if fr_ else 0.3))] \
        + [a + t * bpm_at(a) / 60 for a, b, k in contours if k == "bcsoft" for t in (BCSOFT["t_in"], BCSOFT["t_hold"])] \
        + [x for a_, b_, pts_, _k in phrase_shapes for x in [p_[0] for p_ in pts_] + list(
            __import__("numpy").arange(a_, b_, max(0.05, PS_["step_s"] * bpm_at(a_) / 60.0)))] \
        + [x for ha_, hb_ in ps_hp for x in (ha_, hb_)]
    dyn_curve = sample(base, [p[0] for p in pts]) if ns else []   # printed dynamics only (measure.py groups stems by it)
    # c03: note-start leads (output only; every controller stays on score time)
    def row_lead(art_, q_):
        """mvt3 c07 (critic C #2): ROW_LEAD_S value for this track and row at score qn q_ (seconds or None); a value may
        be a list of (from_qn, to_qn, seconds) spans"""
        v_ = (ROW_LEAD_S.get(tname) or {}).get(art_)
        if isinstance(v_, list):
            return next((s_ for a_, b_, s_ in v_ if a_ - EPS <= q_ < b_ - EPS), None)
        return v_

    def by_name(tbl):
        for k_, v_ in tbl.items():
            if k_[0].isupper() and k_ in tname:
                return v_
        return tbl.get(family)
    shift = {}
    leg_s = by_name(LEG_LEAD_S) or 0.0
    ent_s = by_name(ENTRY_LEAD_S)
    ent_art = by_name(ENTRY_LEAD_ART_S) or {}   # mvt1 c03 (C #2)

    def ent_pick(q):   # mvt1 c07 (critic C #3): a third value for CC11 51-80 at ENTRY_MID_MIN_BPM or faster
        if final(q) <= 50:
            return ent_s[0]
        if len(ent_s) > 2 and final(q) <= 80 and gate_bpm(q) >= ENTRY_MID_MIN_BPM - EPS:
            return ent_s[2]
        return ent_s[1]
    pulls = []   # (start, end): CC11 holds the entry's own level from the moved onset to the score onset
    div_entries = []
    extra_used = []
    el = {float(k): v for k, v in ENTRY_LEADS.get(tname, {}).items() if not k.startswith("_")}

    def extra_s(q):   # c07 (C #2b)
        return next((v for k, v in el.items() if abs(q - k) < 0.02), 0.0)
    ll = {float(k): v for k, v in LEG_LEADS.get(tname, {}).items() if not k.startswith("_")}
    leg_used = []
    flaut_joins, abut_used = [], []   # c15 (A #3, C #4)
    trem_entries = []   # mvt1 c09 (A #4)
    sost_joins = []   # c23 (C #3)
    slur_start_joins = []   # mvt1 c15 (A #2)
    retongue_leads = []   # mvt1 c15 (C #2)
    leg_vel_extra = []   # mvt1 c37 (C #1.3)
    stac_leads = []   # mvt1 c23 (A #3)
    row_slur_ov = []   # mvt3 c12 (A #3): ROW_SLUR_OVERLAP_S joins (score onsets)
    rt_s_ = by_name(RETONGUE_LEAD_S) if RETONGUE_LEAD_S else None
    abut_ = by_name(ABUT_LEAD)

    def abut_cond(n):
        q = n["qn"]
        return bool(abut_) and n["art"].startswith("Sus") and final(q) <= abut_["max_cc"] and q > 0.5 \
            and ("at" not in abut_ or any(abs(q - a_) < 0.02 for a_ in abut_["at"])) \
            and (abut_.get("min_qn") is None or orig_end[id(n)] - q >= abut_["min_qn"] - EPS) \
            and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 for o in ns) \
            and not any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 and o["pitch"] == n["pitch"]
                        for o in ns) \
            and not (abut_.get("skip_next_same") and any(o["qn"] > q + EPS and abs(o["qn"] - orig_end[id(n)]) < 0.05
                                                         and o["pitch"] == n["pitch"] for o in ns)) \
            and not (family == "string" and AUTO_REBOW and not abut_.get("rebow_ok") and any(
                (o is n or (o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05))
                and qn_to_sec(orig_end[id(o)]) - qn_to_sec(o["qn"]) > REBOW_MAX_S for o in ns))

    def entry_outer(n):   # the generic entry branch's own condition (below)
        q = n["qn"]
        return not n.get("leg_target") and bool(n.get("art")) and "Accent" not in n["art"] \
            and any(w in n["art"] for w in ("Sus", "Leg Slur", "Flautando", "Tremolo")) and q > -EPS \
            and bool(ent_s or extra_s(q) or ent_art.get(n["art"])) and (q > 0.5 or family == "string" or extra_s(q))

    def poly0(n):   # mvt1 c19: polyphonic on the written lengths (the ends above already carry legato overlaps)
        return any(o is not n and o["qn"] < orig_end[id(n)] - EPS and orig_end[id(o)] > n["qn"] + EPS for o in ns)

    rt_slow_ = by_name(RETONGUE_LEAD_SLOW_S) if RETONGUE_LEAD_SLOW_S else None

    def rt_lead_s(q):   # mvt1 c37 (critic C #1.1): the re-tongue lead at this tempo (RETONGUE_LEAD_SLOW_S under 100 bpm)
        return rt_slow_ if gate_bpm(q) < ENTRY_MID_MIN_BPM - EPS else rt_s_

    def rt_for(n):
        """the re-tongue lead of this note in seconds (mvt1 c45, ported mvt3 c04: a STR_REP_NEW_BOW "sus_min_s" repeat
        falls back to STR_REP_NEW_BOW["sus_lead_s"] on tracks with no RETONGUE_LEAD_S value)"""
        r_ = rt_lead_s(n["qn"])
        # mvt3 c15 (critic C #5): RETONGUE_LEAD_SPANS {track: [(from_qn, to_qn, seconds)]} replaces the track's value there
        r_ = next((s_ for a_, b_, s_ in RETONGUE_LEAD_SPANS.get(tname, []) if a_ - EPS <= n["qn"] < b_ - EPS), r_)
        if not r_ and n.get("rep_sus_gap"):
            r_ = (STR_REP_NEW_BOW or {}).get("sus_lead_s")
        return r_

    def retongue_ok(n):
        """mvt1 c15 (critic C #2): RETONGUE_LEAD_S applies (the previous note's played end, or None)"""
        q, a_ = n["qn"], n.get("art") or ""
        if not rt_for(n) or family not in ("wind", "brass", "string") or q <= 0.5 or n.get("grace") or n.get("run") \
                or extra_s(q):
            return None
        if family == "string":   # mvt1 c19 (critic C #2)
            # mvt1 c44: a STR_REP_NEW_BOW stroke takes the re-tongue lead; mvt1 c45 (critic A #1, ported mvt3 c04): so does a
            # "sus_min_s" repeat (REP_SPLIT strokes included: the rule gave them the stroke gap but no lead: +94 ms)
            sg_ = bool(n.get("rep_sus_gap"))
            rs_ = bool(n.get("rep_stroke")) or sg_
            if a_ not in STR_STROKE_ROWS or n.get("leg_target") or (n.get("rep_sus") and not sg_) or n.get("rep_stac") \
                    or n.get("short_sus") or (n.get("short_stroke") and not sg_) \
                    or (n.get("down_stroke") and not rs_) or poly0(n) or any(abs(q - r_) < 0.02 for r_ in rebow_at_t):
                return None
            if AUTO_REBOW and not rs_ and any((o is n or (o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.5))
                                              and qn_to_sec(orig_end[id(o)]) - qn_to_sec(o["qn"]) > REBOW_MAX_S for o in ns):
                return None   # (a STR_REP_NEW_BOW stroke's re-bow points are listed, so a lead does not move them)
            if not rs_ and any(_lg((o.get("art") or "")) and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 for o in ns):
                return None   # the Leg -> Sus entry path below
        elif not (a_.startswith("Sus") or (a_.startswith("Leg") and not n.get("leg_target"))) or "Accent" in a_:
            return None
        if entry_outer(n) and abut_cond(n):   # (mvt1 c37: the tempo gate is rt_lead_s)
            return None
        pe = prev_end(q)
        if pe is None or pe < 0 or not (EPS < q - pe < 0.5 - EPS):
            return None
        return pe
    for n in ns:
        q = n["qn"]
        if n.get("fast_leg") and (n.get("leg_target") or n.get("stacleg") or tname in FAST_LEG):
            # c14 (A #3): no lead in the test bar; mvt1 c20: a run span's first note takes the usual leads
            # mvt1 c21 (critic A #4): a listed run target (build/leg_leads.json, score onset) starts that many seconds
            # early, at most FAST_LEG_LEAD_CAP of the note before it (a step the run row has no scale sample for, e.g.
            # a third from the head, plays the slow legato transition and was never heard)
            lx = next((v for k, v in ll.items() if abs(q - k) < 0.02), None)
            pv = n.get("leg_prev") or max((o for o in ns if o["qn"] < q - EPS and o["end"] > q - 0.05), key=lambda o: o["qn"],
                                          default=None)
            if lx is not None and lx > 0 and pv is not None:
                shift[id(n)] = min(lead_qn(q, lx), FAST_LEG_LEAD_CAP * (q - pv["qn"]))
                leg_used.append(round(q, 3))
        elif n.get("acc_art") and ("Accent" in (n.get("art") or "") or not ACC_ART_LEAD):
            pass   # c26: listed accent articulations keep the score onset (no lead, as Sus Accent had); mvt1 c19: samples only
        elif ((STAC_LEAD_S.get(tname) and family in ("string", "wind", "brass") and (n.get("art") or "").startswith("Stac"))
              or (PIZZ_LEAD_S.get(tname) and family == "string" and "Pizz" in (n.get("art") or ""))
              or (row_lead(n.get("art") or "", q)
                  and any(o is not n and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 for o in ns))) \
                and not n.get("rep_stac") and not n.get("mt_alt") and q > 0.5:
            # mvt1 c23 (critic A #3): printed staccato strokes start STAC_LEAD_S early (mvt3 c05: pizzicato PIZZ_LEAD_S)
            a_l_ = n.get("art") or ""
            L = lead_qn(q, row_lead(a_l_, q) or (PIZZ_LEAD_S.get(tname) if "Pizz" in a_l_ else None)
                        or STAC_LEAD_S[tname])
            if isinstance((ROW_LEAD_S.get(tname) or {}).get(a_l_), list) and row_lead(a_l_, q):
                # mvt3 c07: a span-form row lead takes at most ROW_LEAD_CAP_FRAC of the abutting note's played slot
                pm_ = max([o["qn"] - shift.get(id(o), 0.0) for o in ns if o is not n and o["qn"] < q - EPS
                           and abs(orig_end[id(o)] - q) < 0.05] or [q - 1.0])
                L = min(L, ROW_LEAD_CAP_FRAC * (q - pm_))
            shift[id(n)] = L
            pulls.append((q - L, q))
            stac_leads.append(round(q, 3))
            if not any(a_ - EPS <= q < b_ - EPS for a_, b_ in (ROW_LEAD_KEEP_END.get(tname) or {}).get(a_l_, [])):
                n["end"] = max(q - L + 0.05, n["end"] - L)   # the stroke keeps its played length
            if any(a_ - EPS <= q < b_ - EPS for a_, b_ in (ROW_LEAD_KEEP_GAP.get(tname) or {}).get(a_l_, [])):
                # mvt3 c15 (critic C #4): ROW_LEAD_KEEP_GAP: the note before a led stroke ends earlier by the lead (at
                # least 0.05 s long), so the played gap before the stroke stays what the repeat rules made it
                for o in ns:
                    if o is not n and o["qn"] < q - EPS and orig_end[id(o)] <= q + 0.05 and o["end"] > q - L - 0.5:
                        o_on_ = o["qn"] - shift.get(id(o), 0.0)
                        o["end"] = max(sec_to_qn(qn_to_sec(o_on_) + 0.05), o["end"] - L)
            ov_ = (ROW_SLUR_OVERLAP_S.get(tname) or {}).get(a_l_)
            if isinstance(ov_, list):   # mvt3 c13 (A #2): (from_qn, to_qn, seconds) spans; first match; 0.0 = no gap
                ov_ = next((s_ for a_, b_, s_ in ov_ if a_ - EPS <= q < b_ - EPS), None)
            elif not ov_:
                ov_ = None
            for o in ns:
                if o is not n and o["qn"] < q - EPS and orig_end[id(o)] <= q + 0.05 and o["end"] > q - L - 0.02:
                    if ov_ is not None and n.get("slur") is not None and o.get("slur") == n["slur"]:
                        # mvt3 c12: slurred join, the old note overlaps the new one; mvt3 c14: a negative value is a
                        # gap (the old note ends that long before the moved onset, at the earliest 0.02 qn after its start)
                        o["end"] = q - L + lead_qn(q, ov_) if ov_ >= 0 else \
                            max(o["qn"] - shift.get(id(o), 0.0) + 0.02, q - L - lead_qn(q - L, -ov_))
                        row_slur_ov.append(round(q, 3))
                    else:
                        o["end"] = max(o["qn"] - shift.get(id(o), 0.0) + 0.02, q - L - 0.02)
        elif SHORT_SUS_LEAD_S and n.get("short_sus") and tname in SHORT_SUS_LEAD_TRACKS and n["slur"] is not None \
                and any(o is not n and o.get("slur") == n["slur"] and o["qn"] < q - EPS for o in ns):
            # mvt1 c05 (critic A #3, test): a slurred Sus MAX eighth starts early (the old note's end stays: a longer
            # crossfade); the strings changed pitch 0.06-0.1 s after the winds doubling them
            shift[id(n)] = lead_qn(q, SHORT_SUS_LEAD_S)
            if SHORT_SUS_LEAD_CAP_FRAC:   # mvt1 c23: at most this share of the previous slurred note's slot
                pm_ = max([o["qn"] - shift.get(id(o), 0.0) for o in ns if o is not n and o["qn"] < q - EPS
                           and abs(orig_end[id(o)] - q) < 0.05 and o.get("slur") == n["slur"]] or [q - 1.0])
                shift[id(n)] = min(shift[id(n)], SHORT_SUS_LEAD_CAP_FRAC * (q - pm_))
            if SHORT_SUS_LEAD_KEEP_OVERLAP is not None:
                # mvt1 c07 (critic C #2): the previous slurred note ends with the moved onset, so the old pitch fades
                # under the new one instead of sounding at full level over the whole lead
                for o in ns:
                    if o is not n and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 and o.get("slur") == n["slur"]:
                        o["end"] = min(o["end"], q - shift[id(n)] + SHORT_SUS_LEAD_KEEP_OVERLAP)
        elif n.get("leg_target") and not n.get("grace") and not n.get("run") and leg_s > 0:
            lx = next((v for k, v in ll.items() if abs(q - k) < 0.02), None)   # c11 (C #3)
            ls_ = leg_s if lx is None else max(LEG_LEAD_CLAMP[0], min(LEG_LEAD_CLAMP[1], leg_s + lx))
            if lx is not None:
                leg_used.append(round(q, 3))
            L = lead_qn(q, ls_)   # c07 (C #4): seconds measured back on the real tempo map
            pv = n.get("leg_prev")
            if n.get("grace_target"):
                gs = sorted([o for o in ns if o.get("grace") == id(n)], key=lambda o: o["qn"])
                m = gs[0].get("leg_prev")
                if m is not None:
                    L = min(L, 0.45 * (gs[0]["qn"] - m["qn"]))
                for o in gs:
                    shift[id(o)] = L
            elif pv is not None:
                ex = LEG_EXTRA_S.get(tname, {}).get(pv["pitch"], 0.0)   # c06 (A #4)
                ex += LEG_PAIR_EXTRA_S.get(tname, {}).get((pv["pitch"], n["pitch"]), 0.0)   # c11 (C #5)
                ex += LEG_ART_EXTRA_S.get(tname, {}).get(n.get("art") or "", 0.0)   # c15 (C #2)
                se_ = LEG_SOFT_EXTRA_S.get(tname)   # c15 (C #1)
                if se_ and final(q) <= se_[0]:
                    ex += se_[1]
                ve_ = by_name(LEG_VEL_EXTRA_S) if LEG_VEL_EXTRA_S else None   # mvt1 c37 (critic C #1.3)
                # mvt3 c04 (critic A #1): a list of (velocity at or below, extra s) pairs, checked from the lowest
                # velocity up (the v80 / v90 wind targets kept the v100 lead and arrived 100-190 ms late); a plain
                # tuple keeps the old meaning
                if ve_ and not isinstance(ve_, list):
                    ve_ = [ve_]
                ve_hit = next((x_ for x_ in sorted(ve_ or [], key=lambda x_: x_[0]) if n["vel"] <= x_[0]), None)
                if ve_hit is not None and ve_hit[1]:
                    ex += ve_hit[1]
                    leg_vel_extra.append(round(q, 3))
                # mvt3 c11 (critic C #2): the row adds to the base lead plus the extras before the clamp (the base alone
                # was clamped first, so a -0.07 s row on a 0.06 s base with a 0.09 s v80 extra realised only -0.03 s)
                tot = ls_ + ex if lx is None else max(LEG_LEAD_CLAMP[0], min(LEG_LEAD_CLAMP[1], leg_s + lx + ex))
                # mvt1 c21: an entry (a, b, frac, "listed") applies only to onsets listed in build/leg_leads.json
                cf_ = next((x_[2] for x_ in LEG_CAP_FRAC.get(tname, []) if x_[0] - EPS <= n.get("sq", q) < x_[1]
                            and (len(x_) < 4 or x_[3] != "listed" or lx is not None)), 0.45)
                L = min(lead_qn(q, tot), cf_ * (q - pv["qn"]))
                if LEG_MIN_GAP_S.get(tname):
                    # mvt1 c21 (critic A #3): with a raised cap the target may not start closer than this many seconds
                    # to the previous note's moved onset (the unled head of an arpeggio group keeps an audible start)
                    pq_ = pv["qn"] - shift.get(id(pv), 0.0)
                    L = max(0.0, min(L, q - pq_ - LEG_MIN_GAP_S[tname] * bpm_at(q) / 60.0))
            shift[id(n)] = L
        elif n.get("sost_rep") or (n.get("sost_sus") and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05
                                                              for o in ns)):
            # c07 (A #1): a re-tongued note under "Largamente" (repeated pitch, or an unslurred tenuto): 0.04 s early
            shift[id(n)] = lead_qn(q, SOST_REP_S)   # a same-pitch overlap is cut by the note-end guard below
        elif family == "wind" and n.get("sost") and not n.get("leg_target") \
                and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 and (o.get("sost_rep") or o.get("sost_sus"))
                        for o in ns):
            # c23 (C #3): a sostenuto legato note after an overlapping re-tongued Sus note (Ob1 210, bar 62 E5) is joined
            # by the KS Master like a legato transition; with no lead it reached body - 6 dB at +0.33 s
            shift[id(n)] = lead_qn(q, SOST_JOIN_LEAD_S if not isinstance(SOST_JOIN_LEAD_S, dict) else
                                   (by_name(SOST_JOIN_LEAD_S) if by_name(SOST_JOIN_LEAD_S) is not None
                                    else SOST_JOIN_LEAD_S.get("default", 0.12)))
            n["vel"] = max(n["vel"], SOST_VEL)
            sost_joins.append(round(q, 3))
        elif (SLUR_START_SUS or PICKUP_SUS or PORTATO_TAIL_JOIN) and not n.get("leg_target") and _lg((n.get("art") or "")) \
                and not n.get("subito_fresh") and any((o.get("slur_start_sus") or o.get("portato_tail")) and o["qn"] < q - EPS
                        and abs(orig_end[id(o)] - q) < 0.05 for o in ns):
            # mvt1 c15 (critic A #2): the second note of a slur whose first note was tongued on Sus is joined by the KS
            # Master like the sostenuto join: SOST_JOIN_LEAD_S early (at most 0.45 of the first note), SOST_VEL
            # mvt1 c34 (critic A #2): also the note after a re-tongued portato tenuto (PORTATO_TAIL_JOIN)
            p_ = next(o for o in ns if (o.get("slur_start_sus") or o.get("portato_tail")) and o["qn"] < q - EPS
                      and abs(orig_end[id(o)] - q) < 0.05)
            # mvt3 c10 (critic A #2): SOST_JOIN_LEAD_S may be a per-track dict (by_name; "default"), and a
            # build/leg_leads.json row at this onset adds to it (Flute 1 landed -36 ms, Flute 2 +45 ms on one value)
            sj_ = SOST_JOIN_LEAD_S if not isinstance(SOST_JOIN_LEAD_S, dict) else \
                (by_name(SOST_JOIN_LEAD_S) if by_name(SOST_JOIN_LEAD_S) is not None else SOST_JOIN_LEAD_S.get("default", 0.12))
            lx_ = next((v for k, v in ll.items() if abs(q - k) < 0.02), None)
            if lx_ is not None:
                sj_ = max(0.0, sj_ + lx_)
                leg_used.append(round(q, 3))
            shift[id(n)] = min(lead_qn(q, sj_), 0.45 * (q - p_["qn"]))
            n["vel"] = max(n["vel"], SOST_VEL)
            slur_start_joins.append(round(q, 3))
        elif n.get("fresh") and ent_s:
            # c09 (A #3): the section entering after the solo (Vln I qn 65): the family entry lead; the solo's last
            # note is cut 0.03 qn before the moved onset below, so the monophonic legato patch does not join them
            s_ = min(ENTRY_CAP_S, ent_pick(q) + extra_s(q))
            L = lead_qn(q, s_)
            shift[id(n)] = L
            pulls.append((q - L, q))
        elif n.get("rep_after_stac") and rt_lead_s(q) and prev_end(q) is not None and prev_end(q) >= 0 \
                and q - prev_end(q) > 0.03:
            # mvt1 c37 (critic A #2): the stroke after a same-pitch staccato takes the string re-tongue lead, at most up
            # to 0.02 qn after the staccato's note-off (its played length is kept: never overlap into the same pitch)
            L = min(lead_qn(q, rt_lead_s(q)), q - prev_end(q) - 0.02)
            shift[id(n)] = L
            pulls.append((q - L, q))
            retongue_leads.append(round(q, 3))
        elif retongue_ok(n) is not None:
            # mvt1 c15 (critic C #2): a wind/brass re-attack after a short gap starts RETONGUE_LEAD_S early; the notes
            # ending at the gap end as much earlier (the tongued gap is kept), and their CC11 falls move with them
            pe_ = retongue_ok(n)
            pv_ = [o for o in ns if o is not n and o["qn"] < q - EPS and abs(o["end"] - pe_) < 0.003]
            p_ = max(pv_, key=lambda o: o["qn"])
            rx_ = (by_name(RETONGUE_LEAD_ART_S) or {}).get(n.get("art") or "", 0.0) if RETONGUE_LEAD_ART_S else 0.0
            L = min(lead_qn(q, rt_for(n) + rx_), RETONGUE_LEAD_CAP * (orig_end[id(p_)] - p_["qn"]))   # mvt1 c19: + art extra
            shift[id(n)] = L
            pulls.append((q - L, q))
            retongue_leads.append(round(q, 3))
            for o in pv_:
                e_old_ = o["end"]
                o["end"] = max(o["qn"] - shift.get(id(o), 0.0) + 0.02, e_old_ - L)
                d_ = e_old_ - o["end"]
                for k_, row_ in enumerate(cc_falls):
                    if abs(row_[1] - e_old_) < 1e-6:
                        cc_falls[k_] = (row_[0] - d_, row_[1] - d_, *row_[2:])
                        breaks.extend([row_[0] - d_, row_[1] - d_, row_[1] - d_ + (row_[3] if len(row_) > 3 else 0.3)])
        elif not n.get("leg_target") and n.get("art") and "Accent" not in n["art"] \
                and (any(w in n["art"] for w in ("Sus", "Leg Slur", "Flautando", "Tremolo")) or n["art"] in LEG_ROWS_EXTRA) \
                and q > -EPS \
                and (ent_s or extra_s(q) or ent_art.get(n["art"])) and (q > 0.5 or family == "string" or extra_s(q)):
            # (before qn 0.5 only strings and listed entries: Horn 3's opening measured on time with no lead)
            # c07 (C #2a): qn 0 is included (the lead starts inside the pre-roll); C #2b: entry_leads.json extra
            xs = extra_s(q)
            s_ = min(ENTRY_CAP_S, (ent_pick(q) if ent_s else 0.0) + xs
                     + ent_art.get(n["art"], 0.0))   # mvt1 c03 (C #2): the articulation's extra
            pe = prev_end(q)
            # c19 (C #2): after a caesura breath the rest is only CAESURA_BREATH_QN, so a listed extra lead still applies
            cb_ = xs and any(abs(q - c_) < 0.01 for c_ in CAESURA) and q - (pe or 0) >= CAESURA_BREATH_QN - EPS
            if pe is not None and (q - pe >= 0.5 - EPS or (xs and q - pe >= 0.2 - EPS) or cb_):
                L = min(lead_qn(q, s_), q + PREROLL_QN - 0.5)
                if pe >= 0:
                    L = min(L, q - pe - 0.02)
                shift[id(n)] = L
                pulls.append((q - L, q))
                if xs:
                    extra_used.append(round(q, 3))
            elif n.get("flaut_join") and q > EPS:
                # c15 (A #3): the moving voices of a joined sul tasto chord start early and overlap the old chord's
                # moving notes by FLAUT_OVERLAP_QN (common tones were merged into held notes)
                trem_ = n.get("art") == "Tremolo"   # mvt1 c08 (A #4): TREM_JOIN uses its own lead and overlap
                L = min(lead_qn(q, TREM_JOIN_LEAD_S if trem_ else FLAUT_LEAD_S),
                        0.45 * min([q - o["qn"] for o in ns if o["qn"] < q - EPS
                                    and abs(orig_end[id(o)] - q) < 0.1] or [1.0]))
                shift[id(n)] = L
                pulls.append((q - L, q))
                flaut_joins.append(round(q, 3))
                newp = {o["pitch"] for o in ns if abs(o["qn"] - q) < EPS}
                for o in ns:
                    if o.get("art") == n.get("art") and join_art(o) and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 \
                            and o["pitch"] not in newp:
                        o["end"] = max(o["end"], q + (TREM_JOIN_OVERLAP_QN if trem_ else FLAUT_OVERLAP_QN))
            elif (TREM_ENTRY_LEAD_S or TREM_ENTRY_LEAD_SPANS.get(tname)) and family == "string" and n["art"] == "Tremolo" and q > 0.5 \
                    and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 and o.get("art") != "Tremolo" for o in ns):
                # mvt1 c09 (A #4): a tremolo entry straight after a held note on another row (Vln II 304 Leg Slur ->
                # Tremolo dipped 10 dB for 0.2 s; Vln I 664, Vln I/II 484, Vc 464 5-7 dB): the tremolo attack takes
                # 0.1-0.2 s, so it starts TREM_ENTRY_LEAD_S early and the old notes end at the moved start (the c05
                # keyswitch guard: no legato note sounding at the keyswitch)
                L = lead_qn(q, next((s_ for a_, b_, s_ in TREM_ENTRY_LEAD_SPANS.get(tname, []) if a_ - EPS <= q < b_ - EPS),
                                    TREM_ENTRY_LEAD_S))   # mvt3 c07 (critic C #2): span override
                shift[id(n)] = L
                pulls.append((q - L, q))
                trem_entries.append(round(q, 3))
                for o in ns:
                    if o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 and o.get("art") != "Tremolo":
                        o["end"] = min(o["end"], q - L)
            elif abut_cond(n):
                # (mvt1 c07: not into or out of a re-bowed note: its re-bow points and fitted shapes are keyed to its start)
                # c15 (C #4): an abutting soft re-attack at a new pitch (bassoons under the horn solo)
                L = lead_qn(q, abut_["lead_s"])
                if abut_.get("cap_frac"):   # mvt1 c23: at most cap_frac of the abutting note's played slot
                    pm_ = max([o["qn"] - shift.get(id(o), 0.0) for o in ns
                               if o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05] or [q - 1.0])
                    L = min(L, abut_["cap_frac"] * (q - pm_))
                shift[id(n)] = L
                pulls.append((q - L, q))
                abut_used.append(round(q, 3))
                for o in ns:
                    if o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05:
                        o["end"] = min(o["end"], q - L + abut_["overlap_qn"] - o.get("wind_detach_qn", 0.0))
            elif ent_s and family == "string" and n["art"] in STR_STROKE_ROWS and not n.get("short_sus") and not n.get("short_stroke") \
                    and not (n.get("rep_sus") and not any(_lg((o.get("art") or "")) and o["qn"] < q - EPS
                                                          and abs(orig_end[id(o)] - q) < 0.1 for o in ns)) \
                    and any((_lg((o.get("art") or "")) or tname in DIV_JOIN_TRACKS)
                            and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 for o in ns) \
                    and (tname not in DIV_JOIN_TRACKS or final(q) < DYN["f"] - 2
                         or any(_lg((o.get("art") or "")) and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1
                                for o in ns)
                         or extra_s(q)):   # mvt1 c40 (critic A #3): a listed entry_leads.json onset takes this path at f too
                # c06 (A #3): Leg -> Sus MAX without a rest (celli div. in bars 18 and 22): the legato note is cut at the
                # keyswitch and the soft Sus attack blooms (8-10 dB hole); treat it as an entry, velocity 105 or more
                # c07 (A #2): on Violas and Violoncellos also after a Sus MAX chord (viola div. bars 23-29, 4-8 dB
                # holes at +0.2 s), below f; the old chord's notes then end 0.03 qn after the new chord's score onset
                L = min(q, lead_qn(q, s_))
                shift[id(n)] = L
                pulls.append((q - L, q))
                n["vel"] = max(n["vel"], 105)
                div_entries.append(round(q, 3))
                if tname in DIV_JOIN_TRACKS:
                    newp = {o["pitch"] for o in ns if abs(o["qn"] - q) < EPS}
                    for o in ns:
                        if o.get("art") == "Sus MAX" and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 \
                                and o["pitch"] not in newp and o["end"] < q + 0.03 and not o.get("det_cut"):
                            o["end"] = q + 0.03
    # mvt1 c23 (critic A #4): STR_REST_SHORT (see the default): short unslurred string notes before a written rest end early
    rest_short = []
    if STR_REST_SHORT and family == "string" and STR_REST_SHORT.get("at", {}).get(tname):
        rs_ = STR_REST_SHORT
        for n in ns:
            q = n["qn"]
            wl_ = orig_end[id(n)] - q
            if not any(a_ - EPS <= q < b_ - EPS for a_, b_ in rs_["at"][tname]) or n.get("grace") \
                    or n.get("slur") is not None or n.get("slur_out") is not None or wl_ > rs_.get("max_qn", 0.5) + EPS \
                    or gate_bpm(q) < rs_.get("min_bpm", 0.0) - EPS:
                continue
            nx_ = [o["qn"] for o in ns if o["qn"] > q + EPS]
            if nx_ and min(nx_) < orig_end[id(n)] + 0.05:
                continue   # no written rest after it
            e_new_ = q + rs_.get("frac", 0.6) * wl_
            if n["end"] > e_new_ + EPS:
                n["end"] = e_new_
                rest_short.append(round(q, 3))
        rest_short = sorted(set(rest_short))
    # mvt1 c35 (critic A #3): NOTE_END_AT (see the default)
    end_at = []
    for q_, e_ in sorted((float(k_), float(v_)) for k_, v_ in NOTE_END_AT.get(tname, {}).items()):
        hit_ = [n for n in ns if abs(n["qn"] - q_) < 0.01]
        if not hit_:
            print(f"  warning: {tname} NOTE_END_AT {q_}: no note", file=sys.stderr)
        for n in hit_:
            if n["end"] > e_ + EPS:
                n["end"] = e_
                end_at.append([round(q_, 3), round(e_, 4)])
    # mvt1 c37 (critic C #4): CUTOFF_EARLY_S (see the default)
    cutoff_early = []
    ce_s_ = by_name(CUTOFF_EARLY_S) if CUTOFF_EARLY_S else None
    if ce_s_:
        ne_ = {round(float(k_), 3) for k_ in NOTE_END_AT.get(tname, {})}
        for n in ns:
            q, oe_ = n["qn"], orig_end[id(n)]
            if near(q, stacc_q) or n.get("grace") or round(q, 3) in ne_ or text_state(q, ["pizz"], ["arco"]) \
                    or (SCORE_END is not None and oe_ >= SCORE_END - 0.01) \
                    or (FINAL_RING and family in FINAL_RING["families"] and q <= FINAL_RING["at"] + 0.01
                        and oe_ >= FINAL_RING["end"] - 0.01) \
                    or qn_to_sec(oe_) - qn_to_sec(q) < CUTOFF_EARLY_MIN_S:
                continue
            nx_ = [o["qn"] for o in ns if o["qn"] > q + EPS]
            if nx_ and min(nx_) < oe_ + CUTOFF_EARLY_REST_QN - EPS:
                continue
            e_new_ = sec_to_qn(qn_to_sec(oe_) - ce_s_)
            if n["end"] > e_new_ + EPS:
                n["end"] = e_new_
                cutoff_early.append(round(q, 3))
    # mvt1 c16 (critic A #5): a detached stroke after a detached stroke keeps DETACH_LEAD_KEEP_QN of its gap
    det_lead_clamped = []
    if DETACH_LEAD_KEEP_QN is not None and det_str:
        maxL_ = max(0.0, DETACH_ACCENTS["gap_qn"] - DETACH_LEAD_KEEP_QN)
        for n in ns:
            q = n["qn"]
            if id(n) not in det_str or shift.get(id(n), 0.0) <= maxL_ + 1e-6 or round(q, 3) in retongue_leads:
                continue   # (mvt1 c19: a re-tongue lead moved the stroke before it as much earlier, so the gap is kept)
            if not any(id(o) in det_cut and abs(orig_end[id(o)] - q) < 0.01 for o in ns):
                continue
            old_ = shift[id(n)]
            shift[id(n)] = maxL_
            pulls = [(q - maxL_, b_) if abs(b_ - q) < EPS and abs(a_ - (q - old_)) < 1e-6 else (a_, b_) for a_, b_ in pulls]
            det_lead_clamped.append(round(q, 3))
    # mvt1 c19 (critic C #3): SLUR_HEAD_LEAD (see the default): the slur head starts with its led legato target
    slur_head_leads = []
    if SLUR_HEAD_LEAD.get(family):
        for n in ns:
            q = n["qn"]
            if n.get("art") != "Sus MAX" or n["slur"] is None or poly0(n) or n.get("rep_sus") or n.get("rep_stac") \
                    or orig_end[id(n)] - q > 0.5 + EPS or q <= 0.5 \
                    or any(o is not n and o.get("slur") == n["slur"] and o["qn"] < q - EPS for o in ns):
                continue
            tg_ = [o for o in ns if o.get("leg_prev") is n and o.get("leg_target") and id(o) in shift]
            if len(tg_) != 1:
                continue
            S_ = shift[id(tg_[0])]
            if SLUR_HEAD_LEAD.get("lead_s") is not None:   # mvt1 c20 (critic A #4): the head's own lead (s), at most the target's
                S_ = min(S_, q - sec_to_qn(qn_to_sec(q) - SLUR_HEAD_LEAD["lead_s"]))
            if shift.get(id(n), 0.0) >= S_ - 1e-6:
                continue
            d_ = S_ - shift.get(id(n), 0.0)
            pv_ = [o for o in ns if o is not n and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05]
            if any(new_on0_ + 0.02 > q - S_ - (0.0 if o.get("art") == n.get("art") else 0.04)
                   for o in pv_ for new_on0_ in [o["qn"] - shift.get(id(o), 0.0)]):
                continue   # the note before is too short to give way
            if id(n) in shift:   # already led (re-tongue): the rest of the target's lead on top, and the pull widened
                pulls = [(q - S_, b_) if abs(b_ - q) < EPS and abs(a_ - (q - shift[id(n)])) < 1e-6 else (a_, b_)
                         for a_, b_ in pulls]
            else:
                pulls.append((q - S_, q))
            shift[id(n)] = S_
            for o in pv_:
                o["end"] = min(o["end"], q - S_ - (0.0 if o.get("art") == n.get("art") else 0.04))
            slur_head_leads.append(round(q, 3))
    # mvt1 c20 (critic A #2): GROUP_LEAD_AT {track: [(a, b, lead_s)]}: every note with a score onset in [a, b] moves lead_s
    # earlier together (the lead converted at a); the notes before b keep their played lengths (their ends move with
    # them), the note at b keeps its end; notes before the group end by the first moved onset + 0.03 qn. CC11 is held
    # from each moved onset as for any lead. A fast run into a legato target: the run notes and the target arrive together
    group_leads = []
    for a_g, b_g, l_g in GROUP_LEAD_AT.get(tname, []):
        L_ = a_g - sec_to_qn(qn_to_sec(a_g) - l_g)
        grp_ = [n for n in ns if a_g - EPS <= n["qn"] <= b_g + EPS]
        if not grp_:
            continue
        dl_ = {id(n): L_ - shift.get(id(n), 0.0) for n in grp_}
        for n in grp_:
            q = n["qn"]
            pulls = [(a_, b_) for a_, b_ in pulls if abs(b_ - q) >= EPS]
            pulls.append((q - L_, q))
            if q < b_g - EPS and not any(o.get("leg_prev") is n and abs(n["end"] - (o["qn"] + LEG_OVERLAP)) < 0.01
                                         for o in ns):
                # the end moves with the next group note's onset (a legato overlap into a led target is moved at the
                # output stage, from the target's moved onset)
                nx_ = [o for o in grp_ if o["qn"] > q + EPS]
                n["end"] = n["end"] - dl_[id(min(nx_, key=lambda o: o["qn"]))] if nx_ else n["end"] - dl_[id(n)]
                if nx_:
                    # mvt1 c21: a non-legato group note ends at most 0.03 qn after the next group note's moved onset
                    # (a fresh stroke as the group's target already had its entry lead, so dl_ was 0 and the run's last
                    # Sus note overlapped it by 0.26 qn)
                    n["end"] = min(n["end"], min(o["qn"] for o in nx_) - L_ + 0.03)
            group_leads.append(round(q, 3))
        for n in grp_:
            shift[id(n)] = L_
        q0_ = min(n["qn"] for n in grp_) - L_
        for o in ns:
            if o["qn"] < a_g - EPS and o["end"] > q0_ + 0.03:
                o["end"] = q0_ + 0.03
    # mvt1 c03 (critic C #3): timpani strokes and roll starts sound TIMP_DELAY_S after their score onset (negative lead),
    # ends moved with them; CC7 and the volume shapes stay on score time. A felt stroke is at full level within 10 ms,
    # while sustained sections reach -6 dB 0.08-0.10 s after their note-on: in every Allegro tutti the timpani sounded
    # a median 0.080 s ahead of the other tracks (45 strokes)
    if family == "timp" and TIMP_DELAY_S:
        for n in ns:
            shift[id(n)] = -(sec_to_qn(qn_to_sec(n["qn"]) + TIMP_DELAY_S) - n["qn"])
            n["end"] = sec_to_qn(qn_to_sec(n["end"]) + TIMP_DELAY_S)
    # c04 (A #1): harp rolls: note k of a rolled chord (k = 0 lowest) sounds k * step after the beat (negative lead)
    if family == "harp":
        done = set()
        for n in ns:
            ch = arp_chord(n)
            if len(ch) < 2 or id(ch[0]) in done:
                continue
            step = (ARP_S[0] if base(n["qn"]) <= DYN["mp"] else ARP_S[1]) * bpm_at(n["qn"]) / 60
            for k_, o in enumerate(ch):
                shift[id(o)] = -k_ * step
                done.add(id(o))
    # c04 (A #3): a tremolo entering straight after a note on another articulation starts TREM_LEAD_S early
    if family == "string" and TREM_TIMING_C04:
        for n in ns:
            if n.get("art") != "Tremolo" or id(n) in shift:
                continue
            prevs_ = [o for o in ns if o["qn"] < n["qn"] - EPS and abs(orig_end[id(o)] - n["qn"]) < 0.1]
            if prevs_ and all(o.get("art") != "Tremolo" for o in prevs_):
                shift[id(n)] = TREM_LEAD_S * bpm_at(n["qn"]) / 60
    # mvt3 c15 (mvt1 c54): STEADY_LINE (see the default): the span's notes take their note-on and end here, after every lead rule
    steady_line = []
    sn_ = sorted((n for n in ns if n.get("steady")), key=lambda n: (n["qn"], n["pitch"]))
    if sn_:
        def _t_on(o_):
            return qn_to_sec(o_["qn"] - shift.get(id(o_), 0.0))
        for n in sn_:
            sp_, row_, q = n["steady"], n["steady_row"], n["qn"]
            if (n.get("art") or "") != ks_lookup(stem, row_.get("art", sp_["art"]))[0]:
                print(f"  STEADY_LINE WARNING {tname} {q:g}: another rule put the note on {n.get('art')}", file=sys.stderr)
            rest_ = not any(o is not n and o["qn"] < q - EPS and n["qn"] - 0.2 < o.get("steady_wend", orig_end[id(o)])
                            for o in ns)
            L = sp_["lead_s"].get(n["art"], 0.0) if isinstance(sp_["lead_s"], dict) else sp_["lead_s"]
            pv_ = [o for o in ns if o is not n and o["qn"] < q - EPS and not o.get("grace")
                   and abs(o.get("steady_wend", orig_end[id(o)]) - q) <= 0.06]
            if rest_ and "first_lead_s" in sp_:
                L = sp_["first_lead_s"]
            elif not rest_ and "tongue_lead_s" in sp_ and not any(same_slur(o, n) and o["pitch"] != n["pitch"] for o in pv_):
                L = sp_["tongue_lead_s"]   # a new bow / tongue: no legato transition into this note
                if "rep_lead_s" in sp_ and any(o["pitch"] == n["pitch"] for o in pv_):
                    L = sp_["rep_lead_s"]   # a same-pitch repeat speaks through the release of the note before it
            if rest_ and sp_.get("rr_reset"):
                n["steady_reset"] = True
            L = row_.get("lead_s", L)
            n["steady_lead"] = L
            n["steady_class"] = "first" if rest_ else ("slur" if any(same_slur(o, n) and o["pitch"] != n["pitch"] for o in pv_)
                                                        else ("rep" if any(o["pitch"] == n["pitch"] for o in pv_) else "tongue"))
            shift[id(n)] = lead_qn(q, L) if L >= 0 else -(sec_to_qn(qn_to_sec(q) - L) - q)
            pulls[:] = [p_ for p_ in pulls if abs(p_[1] - q) > 1e-6]
            if rest_ and L > 0:
                pulls.append((q - shift[id(n)], q))
            if row_.get("vel", sp_.get("vel")) is not None:
                n["vel"] = row_.get("vel", sp_.get("vel"))
        for n in sn_:
            sp_, row_, q = n["steady"], n["steady_row"], n["qn"]
            nx_ = [o for o in ns if o["qn"] > q + EPS and not o.get("grace")]
            nq_ = min((o["qn"] for o in nx_), default=None)
            rel_ = None
            if nq_ is not None and nq_ - n["steady_wend"] <= 0.05 + EPS:
                nx_ = [o for o in nx_ if abs(o["qn"] - nq_) < EPS]
                t1_ = min(_t_on(o) for o in nx_)
                if "end_s" in row_:
                    rel_ = row_["end_s"]
                elif any(o["pitch"] == n["pitch"] for o in nx_):
                    rel_ = -sp_.get("rep_gap_s", 0.05)
                elif any(same_slur(n, o) for o in nx_):
                    rel_ = sp_.get("overlap_s", 0.03)
                else:
                    rel_ = -sp_.get("gap_s", 0.03)
                t_end_ = max(t1_ + rel_, _t_on(n) + sp_.get("min_len_s", 0.08))
                if any(o["pitch"] == n["pitch"] for o in nx_):
                    t_end_ = min(t_end_, t1_ - 0.012)
                rel_ = round(t_end_ - t1_, 4)
                n["end"] = sec_to_qn(t_end_)
            steady_line.append([round(q, 3), n["art"], round(n["steady_lead"], 4), rel_, n["steady_class"]])
    # c22 (A #1): the pull starts PULL_PAD_QN before the moved note-on, rounded to the 4-decimal grid that sample() uses.
    # Before, a moved onset that rounded down (228.94722 -> 228.9472) put the grid point just before the pull's start,
    # so 26 entries started on the previous phrase's CC11 (Bn1 229 pp: CC 114 for 0.06 s, +14.8 dB attack)
    PULL_PAD_QN = 0.01
    pulls = sorted(set((round(a_ - PULL_PAD_QN, 4), b_) for a_, b_ in pulls))

    def final2(q):
        for a_, b_ in pulls:
            if a_ - EPS <= q < b_:
                return final(b_)
        return final(q)
    breaks += [x for a_, b_ in pulls for x in (a_, b_)]

    def new_on(n):
        return n["qn"] - shift.get(id(n), 0.0)

    def shifted_on(q):
        return min([new_on(o) for o in ns if abs(o["qn"] - q) < EPS] + [q])

    cc11 = sample(final2, breaks) if ns else []
    # check: every printed mark is on the curve
    for q, d in marks:
        if d in ("sf", "sfz"):
            continue
        # mvt3 c03: an fp / sfp is checked where its attack has fallen to the printed level (it read the spike's ramp)
        got = value_at(pts, (FP_CHECK_AT.get(round(q, 3), q) if d in ("fp", "sfp") else q) + 0.001)
        if abs(got - DYN[d]) > 2:
            print(f"  WARN {tname}: {d} at qn {q} -> curve {got:.0f}", file=sys.stderr)
    # c04 (C #3): vibrato. Flutes, oboes, cor anglais, bassoons and strings: melody spans (solo/cantabile/espr./dolce, and
    # every slurred note of a flute, oboe or cor anglais, since the oboe solo of bars 15-20 carries no text) at
    # CC1 100 (strings 95), delayed on phrase starts of 0.8 s or longer (target - 35 at the onset, target at 40% of the note; -20 on legato notes of 1.8 s or longer), +10 on
    # the highest note of each slur; elsewhere CC1 follows the level (pp about 42, p 55, f 90, ff 98); flautando 20.
    # Horns, trombones, tuba, clarinets, bass clarinet and contrabassoon keep the c01 formula.
    vib_fam = family == "string" or (family == "wind" and any(w in tname for w in ("Flute", "Oboe", "Cor anglais", "Bassoon"))
                                     and not tname.startswith("Contra"))
    slur_top = {}
    for n in ns:
        if n["slur"] is not None:
            slur_top[n["slur"]] = max(slur_top.get(n["slur"], 0), n["pitch"])

    def sounding(q):
        c = [n for n in ns if n["qn"] <= q + EPS and q < orig_end[id(n)] - EPS and not n.get("grace")]
        return max(c, key=lambda n: (n["qn"], n["pitch"])) if c else None

    def cc1_fn(q):
        # c22 (A #1c): inside a pull, the entry's own vibrato (as final2 does for CC11); it was the previous note's
        q = next((b_ for a_, b_ in pulls if a_ - EPS <= q < b_), q)
        v = cc1_fn0(q)
        # c17 (A #3, test): woodwind Sus notes of WIND_VIB_CAP_S or longer at CC11 WIND_VIB_CAP_CC11 or more: CC1 capped at
        # WIND_VIB_CAP (inside the patch's Vib/Non Vib crossfade, so part of the sound is the non-vibrato layer); the ff
        # flute's 4.4 Hz vibrato swung the tutti's 1.5-4 kHz band by 5.9 dB at bars 61-62
        if WIND_VIB_CAP is not None and family == "wind" and "larinet" not in tname and final2(q) >= WIND_VIB_CAP_CC11:   # the CL/BC KS Masters have no Vib layer
            n = sounding(q)
            if n is not None and (n.get("art") or "").startswith("Sus") \
                    and qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"]) >= WIND_VIB_CAP_S:
                return min(v, WIND_VIB_CAP)
        return v

    def cc1_fn0(q):
        v11 = final2(q)
        if not vib_fam:
            # mvt1 c09 (C #1): in the Hollywood Brass KS Masters (1FH, 1TP, 1TB, 1TU) and the Clarinet KS Master the
            # dynamic layers are crossfaded by CC1 (each layer group's Source volume rescaler is driven by a cc 1
            # MidiController; CC11 is only the Global Group volume), so the c01 formula (CC1 57-87) played every printed
            # dynamic on the mp-f samples. These tracks take CC1 from the printed dynamic curve (hairpins, no accent or
            # fit shapes, so gentle accents stay off the top layer) through CC1_DYN_MAP
            if any(tname.startswith(p_) for p_ in CC1_DYN_TRACKS):
                # mvt3 c07: PHRASE_SHAPE goes into the dynamic-layer lane (CC1) on these tracks, not into CC11
                po_ = phrase_off(q) if phrase_shapes else 0.0
                c1_ = value_at(CC1_DYN_MAP, base(q) + po_)
                if po_ < 0 and PS_.get("cc1_floor"):   # no dip into the layer boundaries under cc1_floor
                    c1_ = max(c1_, min(value_at(CC1_DYN_MAP, base(q)), PS_["cc1_floor"]))
                return round(c1_)
            if tname in CC1_HOLD:   # mvt1 c09 (C #1): e.g. the CB KS Master's Non Vib/Vib overlap (64-72)
                return CC1_HOLD[tname]
            return max(40, min(100, 64 + (v11 - 46) * 0.3))
        n = sounding(q)
        if n is not None and n.get("art") == "Flautando":
            return 20
        if TASTO_CC1 is not None and family == "string" and n is not None and "izz" not in (n.get("art") or "") \
                and text_state(n["qn"], ["sul tasto"], ["ord.", "arco"]):
            return TASTO_CC1   # mvt3 c01 (critic A #4): sul tasto without a Flautando row, the non-vibrato layer
        melodic_wind = family == "wind" and not tname.startswith("Bassoon") and n is not None and n["slur"] is not None
        if melodic_wind or any(a - EPS <= q < b - EPS for a, b, _ in boost_spans):
            tgt = 95 if family == "string" else 100
            if tname in SOLO_NO_BOOST and any(a - EPS <= q < b - EPS and amt == 0 for a, b, amt in boost_spans):
                tgt += SOLO_VIB   # c08 (C #5)
            if n is None:
                return tgt
            if n["slur"] is not None and n["pitch"] == slur_top.get(n["slur"]):
                tgt = min(120, tgt + 10)
            e = orig_end[id(n)]
            sec = qn_to_sec(e) - qn_to_sec(n["qn"])
            # delayed vibrato on phrase starts (not legato targets) of 0.8 s or more, and a smaller dip on long legato notes
            dip = 35 if (not n.get("leg_target") and sec >= 0.8) else (20 if sec >= 1.8 else 0)
            pv_ = n.get("leg_prev")
            if n.get("leg_target") and pv_ is not None and same_slur(pv_, n) \
                    and base(n["qn"]) >= DYN["f"]:
                dip = 0   # c16 (A #4): no vibrato restart on a loud note slurred to the previous one
            if STROKE_NO_VIB_DELAY and n.get("down_stroke") and base(n["qn"]) >= DYN["f"] - 2:
                dip = 0   # mvt1 c34 (critic A #3a): a loud down-bow stroke keeps its vibrato from the front
            if n.get("rep_stroke"):
                dip = 0   # mvt1 c44: a re-bowed repeat (STR_REP_NEW_BOW) keeps its vibrato
            if dip:
                x = (q - n["qn"]) / (e - n["qn"])
                if x < 0.4:
                    return tgt - dip + dip * x / 0.4
            return tgt
        return value_at([(22, 38), (34, 42), (46, 55), (58, 62), (72, 72), (88, 90), (114, 98), (124, 100)], v11)
    vbr = breaks + [x for n in ns for x in (n["qn"], n["qn"] + 0.4 * (orig_end[id(n)] - n["qn"]))]
    # mvt1 c12 (critic C #2, test): a short CC1 lift at the front of loud brass accents on the CC1-layered brass KS
    # Masters (GENTLE_ACCENT["brass"]["cc1_front"] = (CC, hold_s, ramp_s[, pre_s])): +CC from pre_s (default PULL_PAD_QN)
    # before the moved onset (the patch's CC1 MidiController fades over 120 ms, so the lift must start early) to hold_s
    # after it, back over ramp_s. Accents on the Sus rows only (slurred legato accents keep their transition).
    # No accent sample, no CC11 bump, no velocity (the harsh parts of movement II's c24 accents)
    cf_ = GENTLE_ACCENT.get(family, {}).get("cc1_front") if family == "brass" else None
    fronts_ = []
    if cf_ and any(tname.startswith(p_) for p_ in CC1_DYN_TRACKS):
        ga_arts_ = GENTLE_ACCENT["brass"]["arts"]
        for n in ns:
            if n["qn"] in accent_q and base(n["qn"]) >= DYN["f"] - 4 and (n.get("art") or "") in ga_arts_ \
                    and not any(abs(new_on(n) - f_[0]) < EPS for f_ in fronts_):
                m_ = new_on(n)
                h_ = sec_to_qn(qn_to_sec(m_) + cf_[1])
                r_ = sec_to_qn(qn_to_sec(m_) + cf_[1] + cf_[2])
                a_ = sec_to_qn(qn_to_sec(m_) - cf_[3]) if len(cf_) > 3 else m_ - PULL_PAD_QN   # optional pre_s
                fronts_.append((m_, a_, h_, r_))
        vbr = vbr + [x for f_ in fronts_ for x in f_[1:]]

    def cc1_fn_f(q):
        v = cc1_fn(q)
        for m_, a_, h_, r_ in fronts_:
            if a_ - EPS <= q < h_:
                return v + cf_[0]
            if h_ <= q < r_:
                return v + cf_[0] * (r_ - q) / (r_ - h_)
        return v
    cc1 = sample(cc1_fn_f if fronts_ else cc1_fn, vbr) if ns else []
    cc1_fronts = [round(f_[0], 3) for f_ in fronts_]
    cc7 = []
    timp_hp = []   # c13 (A #3)
    vol_parts = _VP()   # c02: exact level offsets in dB, written as a track volume envelope by build_reaper.py
    vol_parts.rule = "timp_roll"   # mvt3 c16: each item is tagged with the rule in force when it is appended
    if family in ("harp", "harm"):
        cc11, cc1 = [(0.0, 110)], []
    if family == "timp":  # the timpani patch has no CC11; CC7 per articulation (c01); the roll settle is in vol_db (c02)
        # c02: mf/f/ff +4 (the tutti rolls keep their level after the -4 dB track gain change); ppp/pp drop 4 dB net
        # c06 (C #4): ff -14 -> -11 and fff -12 -> -9 (the bar 61 ff roll was only 1.4 dB over the bar 79 f roll)
        roll_db = [(22, -36), (34, -31), (46, -26), (58, -23), (72, -17), (88, -16), (114, -11), (124, -9)]

        def timp_db(n, q):
            dbv = value_at(roll_db, base(q))
            if n.get("tie_stroke"):   # c14 (A #2): the stroke that ends a tied roll, a little over the roll
                return min(0.0, dbv + TIMP_TIE_STROKE_DB)
            if n["art"].endswith("Lng"):   # strokes: roll level + 16 dB, +20 at pp and below (c02: pp strokes inaudible)
                # c03 (B #1): p strokes +12 (qn 271 was the loudest stem in bar 82)
                # c11 (B #5): p strokes 12 -> 16 (qn 172 and 271 measured 6-11 dB under the p strings and oboe)
                return min(0.0, dbv + (20 if base(q) <= DYN["pp"] + 4 else 16))
            return dbv
        for n in ns:
            q, e = n["qn"], orig_end[id(n)]
            pts7 = [max(0.0, q - 0.02)] + [q + 0.25 * k for k in range(1, int((e - q) / 0.25) + 1) if q + 0.25 * k < e - 0.05]
            for t in pts7:
                val = int(round(127 * 10 ** (timp_db(n, max(t, q)) / 40)))
                cc7.append((round(t, 4), max(1, min(127, val))))
        cc7.sort(key=lambda c: c[0])
        cc7 = [c for i, c in enumerate(cc7) if i == 0 or c[1] != cc7[i - 1][1]]
        # c13 (A #3): Opus treats CC7 as linear amplitude (measured slopes 1.10 and 0.79 against 20 log10 CC7), so the
        # 40 log10 CC7 scale above delivers half of each roll hairpin's planned dB change. The other half goes into the
        # volume envelope, relative to the roll's start level (the static roll_db levels stay as measured): sampled on
        # the 0.125 qn grid, held to the roll's end, released by the next onset
        for n in ns:
            if not n["art"].endswith("Rls"):
                continue
            q, e = n["qn"], orig_end[id(n)]
            if not any(a < e - EPS and b > q + EPS for a, b, k in hps):
                continue
            d0 = value_at(roll_db, base(q))
            ps = [(q + 0.125 * j, TIMP_HP_DB_FACTOR * 0.5 * (value_at(roll_db, base(q + 0.125 * j)) - d0))
                  for j in range(int((e - q) / 0.125) + 1) if q + 0.125 * j < e - EPS]
            if max(abs(v_) for _, v_ in ps) < 0.1:
                continue
            nx = min([o["qn"] for o in ns if o["qn"] >= e - EPS] + [e + 0.5])
            ps += [(e, ps[-1][1]), (max(e + 0.01, nx - 0.02), 0.0)]
            vol_parts.append(("env", ps))
            timp_hp.append([round(q, 3), round(max(v_ for _, v_ in ps), 2), round(min(v_ for _, v_ in ps), 2)])
        cc11, cc1 = [], []
        # mvt1 c12 (critic A #1): the felt timpani Rls row has eight dynamic layers (V1-V8) crossfaded by CC1 (each
        # group's Source volume is driven by a cc 1 MidiController, fadeTime 120 ms; read with opus_state.load_oib), and
        # the strokes (Lng/Sht) are velocity-layered with no CC1. With no CC1 lane every roll played one bright layer
        # (1-8 kHz share -11.5..-14.9 dB from ppp to fff, against a 20 dB spread on the strokes). CC1 now follows the
        # printed dynamic curve through TIMP_CC1_MAP, TIMP_CC1_PAD_QN ahead (so a roll starts on its own layer)
        rolls_c1_ = [n for n in ns if n["art"].endswith("Rls")]
        if TIMP_CC1_MAP and rolls_c1_:
            cc1 = sample(lambda q: value_at(TIMP_CC1_MAP, base(q + TIMP_CC1_PAD_QN)),
                         breaks + [n["qn"] - TIMP_CC1_PAD_QN for n in rolls_c1_])
        # mvt1 c12: per-dynamic level trims on the rolls only (the soft CC1 layers are quieter in themselves), read from
        # the printed curve over each roll, held through its ring to the next onset (like the settle)
        if TIMP_ROLL_TRIM_DB:
            for n in rolls_c1_:
                q, e = n["qn"], orig_end[id(n)]
                nx = min([o["qn"] for o in ns if o["qn"] >= e - EPS and o is not n] + [e + 1.0])
                ps = [(q - 0.02, value_at(TIMP_ROLL_TRIM_DB, base(q)))]
                ps += [(q + 0.125 * j, value_at(TIMP_ROLL_TRIM_DB, base(q + 0.125 * j)))
                       for j in range(int((e - q) / 0.125) + 1) if q + 0.125 * j < e - EPS]
                ps += [(max(ps[-1][0] + 0.01, nx - 0.05), ps[-1][1])]
                if max(abs(v_) for _, v_ in ps) >= 0.05:
                    vol_parts.append(("env", ps))
        # roll settle: a roll (or a chain of one-bar rolls) of 3 qn or more falls 5 dB over 3 qn unless a crescendo is
        # printed (c01's 4-unit CC7 settle measured only 0.6-1.5 dB); the level returns before the next note
        rolls = [n for n in ns if n["art"].endswith("Rls")]
        for n in rolls:
            if any(abs(orig_end[id(o)] - n["qn"]) < 0.05 for o in rolls):
                continue   # not a chain start
            c0, ce = n["qn"], orig_end[id(n)]
            while True:
                nx = [o for o in rolls if abs(o["qn"] - ce) < 0.05]
                if not nx:
                    break
                ce = orig_end[id(nx[0])]
            if ce - c0 < 3 or any(k == "cresc" and a < ce - EPS and b > c0 + EPS for a, b, k in hps):
                continue
            if any(abs(c0 - k_) < 0.02 for k_ in TIMP_SETTLE_SKIP):
                continue   # mvt3 c03 (critic B #2): listed roll chains keep their level (no settle)
            nxt_on = min([o["qn"] for o in ns if o["qn"] >= ce - EPS] + [ce + 2])
            vol_parts.append(("settle", c0, ce, nxt_on))
        # c03 (B #1): soft rolls (p or softer) sat level with or above the pp strings and the horn/cor anglais solos:
        # a flat -6 dB on every soft roll chain, under the settle
        for n in rolls:
            if any(abs(orig_end[id(o)] - n["qn"]) < 0.05 for o in rolls):
                continue
            c0, ce = n["qn"], orig_end[id(n)]
            while True:
                nx = [o for o in rolls if abs(o["qn"] - ce) < 0.05]
                if not nx:
                    break
                ce = orig_end[id(nx[0])]
            if max(base(c0 + 0.125 * j) for j in range(int((ce - c0) / 0.125) + 1)) <= DYN["p"] + 2:
                nxt_on = min([o["qn"] for o in ns if o["qn"] >= ce - EPS] + [ce + 2])
                vol_parts.append(("flat", c0, max(ce, nxt_on - 0.05), -6.0))   # held through the ring, like the settle
        vol_parts.rule = "timp_attack"
        # c10 (B #2): rolls and strokes printed f or louder start at their dynamic: +TIMP_LOUD_ATTACK_DB from the onset
        # (10 ms rise), held 0.25 qn, gone by 0.75 qn (before the settle has fallen 1.3 dB). The roll body is unchanged.
        for n in ns:
            q = n["qn"]
            mk_ = [DYN[d_] for q_, d_ in marks if abs(q_ - q) < 0.01 and d_ in DYN]
            pm_ = [DYN[d_] for q_, d_ in marks if q_ < q - 0.01 and d_ in DYN]
            arr_ = bool(mk_) and (not pm_ or max(mk_) > pm_[-1])   # a printed arrival louder than the last mark
            if base(q + 0.01) >= DYN["f"] and n in rolls and any(abs(orig_end[id(o)] - q) < 0.05 for o in rolls) \
                    and not arr_ and not any(abs(q - k_) < 0.02 for k_ in TIMP_CHAIN_BUMP_AT):
                timp_chain_skip.append(round(q, 3))   # mvt1 c07 (B #4): a roll continuing a roll is not a new attack
            elif base(q + 0.01) >= DYN["f"]:
                # c14 (A #2): a tied-roll stroke already sits on the roll's hairpin gain: half the bump
                ad_ = TIMP_LOUD_ATTACK_DB * (0.5 if n.get("tie_stroke") else 1.0)
                vol_parts.append(("env", [(q - 0.01, 0.0), (q + 0.01 * bpm_at(q) / 60, ad_),
                                          (q + 0.25, ad_), (q + 0.75, 0.0)], True))

    _vp_cache = {}

    def _vp_split():
        """mvt3 c16: (slow items, kept per-note items, other per-note items, accent items when ACCENT_NO_STACK)"""
        key_ = (len(vol_parts), id(vol_parts[-1]) if vol_parts else 0)
        if _vp_cache.get("key") != key_:
            off_ = VOL_RULE_OFF.get(tname, {})

            def dropped(it_, r_):
                sp_ = off_.get(r_)
                if not sp_:
                    return False
                if sp_ is True:
                    return True
                x0_ = it_[1][0][0] if it_[0] == "env" else (it_[1] if len(it_) > 1 and isinstance(it_[1], (int, float)) else None)
                return x0_ is not None and any(a_ - 0.5 <= x0_ < b_ for a_, b_ in sp_)
            slow_, keep_, pn_, acc_ = [], [], [], []
            for it_ in vol_parts:
                r_ = vol_parts.tags.get(id(it_), "other")
                if dropped(it_, r_) or r_ in _off_env:   # env STP_VOL_OFF=rule,rule: left out on every track (tests)
                    continue
                if ACCENT_NO_STACK and r_ == "accent":
                    acc_.append(it_)
                elif r_ not in VOL_PER_NOTE_RULES:
                    slow_.append(it_)
                elif r_ in VOL_PER_NOTE_KEEP:
                    keep_.append(it_)
                else:
                    pn_.append(it_)
            _vp_cache.update(key=key_, parts=(slow_, keep_, pn_, acc_))
        return _vp_cache["parts"]
    _vpn_mode = __import__("os").environ.get("STP_VOL_PER_NOTE") or VOL_PER_NOTE
    _off_env = set(filter(None, __import__("os").environ.get("STP_VOL_OFF", "").split(",")))

    def vol(q):
        slow_, keep_, pn_, acc_ = _vp_split()
        v = _vol_items(q, slow_) + _vol_items(q, keep_)
        a_ = 0.0
        if acc_:   # ACCENT_NO_STACK: the larger of the running accent shapes
            a_ = max((_vol_items(q, [it_]) for it_ in acc_ if it_[1][0][0] <= q < it_[1][-1][0]), default=0.0)
        acc_keep_ = "accent" in VOL_PER_NOTE_KEEP or "accent" not in VOL_PER_NOTE_RULES
        if _vpn_mode == "off":
            return v + (a_ if acc_keep_ else 0.0)
        if _vpn_mode in ("off_shape", "off_level"):
            lv_ = [it_ for it_ in pn_ if vol_parts.tags.get(id(it_)) in VOL_PER_NOTE_LEVEL_RULES]
            if _vpn_mode == "off_shape":
                return v + _vol_items(q, lv_) + (a_ if acc_keep_ else 0.0)
            return v + _vol_items(q, [it_ for it_ in pn_ if vol_parts.tags.get(id(it_)) not in VOL_PER_NOTE_LEVEL_RULES]) + a_
        p_ = _vol_items(q, pn_) + (0.0 if acc_keep_ else a_)
        if _vpn_mode == "cap3":
            p_ = max(-VOL_PER_NOTE_CAP_DB, min(VOL_PER_NOTE_CAP_DB, p_))
        return v + p_ + (a_ if acc_keep_ else 0.0)

    def _vol_items(q, items):
        v = 0.0
        for item in items:
            if item[0] == "settle":
                _, c0, ce, nx = item
                # c05 (B #5): held 0.5 qn past the roll's end (or to the next onset) so a stroke at the roll's end does
                # not lift the f roll's ring back to 0 dB
                # c09 (C #5): a roll that ends the piece holds its settle through the tail
                if c0 <= q < (1e9 if ce >= END - 0.01 else max(ce + 0.5, nx - 0.05)):
                    v += -5 * min(1.0, (q - c0) / 3.0)
            elif item[0] == "span":
                _, a, b2, dbv = item[:4]
                r = 0.5
                if len(item) > 4 and item[4]:
                    # c06 (C #1): the cut opens linearly over the last end_ramp qn and is 0 at b2
                    er = item[4]
                    if a - r <= q < b2:
                        v += dbv * max(0.0, min(1.0, (q - (a - r)) / r, (b2 - q) / er))
                elif a - r <= q <= b2 + r:
                    v += dbv * max(0.0, min(1.0, (q - (a - r)) / r, ((b2 + r) - q) / r))
            elif item[0] == "hpgain":
                # c06 (C #1): 0 at the hairpin start, g at its end, held to the next onset, released over HP_REL qn
                # (C proposed 0.25 qn; a 3-4 dB drop a beat after the arrival would read as fp, so it settles over 1 qn)
                # c09 (B #1): s = start value (a chained second hairpin starts from the first one's gain); rel = 0 for
                # a chained first hairpin (held to the second's start, no release)
                _, a, b2, nx, g = item[:5]
                s0 = item[5] if len(item) > 5 else 0.0
                rel = item[6] if len(item) > 6 else HP_REL
                if HP_REL_MAX_DB_S and rel >= 0.01 and abs(g) > 0.01:
                    # mvt3 c18: the release of a hairpin's dB gain is no faster than this (it falls inside the notes
                    # after the arrival: 2-4 dB over one quarter was 5-12 dB/s on a held arrival chord)
                    k_ = (round(nx, 4), round(abs(g), 3))
                    if k_ not in _HP_REL_CACHE:
                        _HP_REL_CACHE[k_] = sec_to_qn(qn_to_sec(nx) + abs(g) / HP_REL_MAX_DB_S) - nx
                    rel = max(rel, _HP_REL_CACHE[k_])
                se, gh = (item[7], item[8]) if len(item) > 8 else (0.0, 0.0)
                if a <= q < b2:
                    v += s0 + (g - s0) * (q - a) / (b2 - a)
                elif b2 <= q < nx:
                    v += g
                elif rel and se > nx and nx <= q < se:   # c10 (C #4a): falls to gh over rel, held to the span end
                    v += gh + (g - gh) * max(0.0, 1 - (q - nx) / rel)
                elif rel and se > nx and se <= q < se + rel:
                    v += gh * (1 - (q - se) / rel)
                elif rel and se <= nx and nx <= q < nx + rel:
                    v += g * (1 - (q - nx) / rel)
            elif item[0] == "swell_db":
                # c06 (C #5): +SWELL_DB at 40% of a long note, 0 at 80%; on phrase ends -SWELL_DB at the end
                _, a, b2, taper = item
                if a <= q < b2:
                    x = (q - a) / (b2 - a)
                    if x < 0.4:
                        v += SWELL_DB * x / 0.4
                    elif x < 0.8:
                        v += SWELL_DB * (0.8 - x) / 0.4
                    elif taper:
                        v -= SWELL_DB * (x - 0.8) / 0.2
            elif item[0] == "note":
                _, a, b2, dbv, ramp = item
                if a <= q < b2 + 0.1:
                    v += dbv * min(1.0, (q - a) / ramp, max(0.0, (b2 + 0.1 - q) / 0.1))
            elif item[0] == "flat":
                _, a, b2, dbv = item
                if a - 0.05 <= q < b2:
                    v += dbv
            elif item[0] == "chord":
                v += chord_db(q)
            elif item[0] == "env":   # c08: a piecewise-linear dB shape, 0 outside its points
                ps = item[1]
                if ps[0][0] <= q < ps[-1][0]:
                    v += value_at(ps, q)
            elif item[0] == "bloomv":
                _, a, b2 = item
                if a <= q < b2 + 0.1:
                    v += -4.5 * min(1.0, (q - a) / 2.0) * min(1.0, max(0.0, (b2 + 0.1 - q) / 0.1))
            elif item[0] == "fade":
                # c07 (C #5): the ppp chord holds through the fermata (it was -20 dB from 301.5 to 304, so the 3 s
                # fermata beat sounded at -61..-74 dB): 0 to 303, -2 at 303.5, -10 at 304, -20 by 304.5 (release)
                # c09 (C #5): held at -10 from 304 (the last release) instead of -20 by 304.5, which faded the hall tail
                v += value_at([(SE - 1, 0.0), (SE - 0.5, -2.0), (SE, -10.0)], q) if q >= SE - 1 else 0.0
        return v
    vol_parts.rule = "role"
    # c09 (A #2): role spans as explicit dB shapes. Spans that meet (B starts within ROLE_CHAIN qn after A ends, A without
    # end_ramp) crossfade from A's value to B's over [B.a - 0.1, B.a + 0.15]; a span that starts on a legato target ramps
    # in after the join, over [a, a + 0.25]; other spans keep the 0.5 qn ramps. end_ramp spans keep the "span" item.
    # c12 (C #1): roles.json "_all" rows apply to every track (bars 61-62 -1 dB)
    rows_ = sorted([(r[0], r[1], r[2], r[3] if len(r) > 3 else 0) for r in ROLES.get(tname, []) + ROLES.get("_all", [])])
    sf_q = [q_ for q_, d_ in marks if d_ in ("sf", "sfz")]

    def sf_shift(x):
        """c10 (C #4b): a level cut that starts at a printed sf starts on it (crossfade [sf, sf + 0.25]) instead of
        0.1 qn before it. (Starting it after the attack, +0.35 qn, simulated the Vln I/II tremolo-chord sf 10-14 dB
        louder than c09 and the master peak at +2 dBFS.)"""
        return 0.1 if any(abs(x - m_) <= 0.1 for m_ in sf_q) else 0.0
    leg_on = [n["qn"] for n in ns if n.get("leg_target")]
    role_chained = 0
    role_cc7 = []          # mvt3 c27: CC7 carries of role edges ([(qn, dB)] shapes, 0 outside)
    role_edge_moved, role_edge_join = [], []
    _rer = ROLE_EDGE_IN_REST if family not in ("timp", "perc", "harp", "harm") else None

    def _played_end(n_):
        """the note's end as played (approximate, before the out_notes pass): a note followed at its score end by a led
        note ends 0.03 qn before that note's moved onset (the fresh-entry cut), or overlaps it when it is a legato
        target"""
        nx_ = [o_ for o_ in ns if o_ is not n_ and o_["qn"] > n_["qn"] + EPS and abs(o_["qn"] - n_["end"]) < 0.02]
        if not nx_:
            return n_["end"]
        on2_ = min(new_on(o_) for o_ in nx_)
        if on2_ >= n_["end"] - 1e-6:
            return n_["end"]
        if any(o_.get("leg_target") or o_.get("leg_prev") is n_ for o_ in nx_):
            return max(on2_ + 0.05, n_["end"] - 0.0) if family not in ("string",) else on2_ + 0.05
        return max(new_on(n_) + 0.01, on2_ - 0.03)
    _snd = sorted(((new_on(n_), max(_played_end(n_), new_on(n_) + 0.01)) for n_ in ns), key=lambda x_: x_[0])
    if ROLE_SPANS_PREV.get(tname) and CUR_ALIAS is None:
        _snd = list(ROLE_SPANS_PREV[tname])

    def _gap_s(q0_, q1_):
        return qn_to_sec(q1_) - qn_to_sec(q0_)

    def _rest_before(on_):
        """the end of the sounding notes before onset on_ (the rest before it runs from there to on_)"""
        pe_ = [e_ for o_, e_ in _snd if o_ < on_ - 1e-4]
        return max(pe_) if pe_ else -3.0

    def _edge_fix(pts_, e_):
        """mvt3 c27 ROLE_EDGE_IN_REST: pts_ = [(x0, v0), (x1, v1)] an edge ramp at nominal edge e_ -> new points"""
        (x0_, v0_), (x1_, v1_) = pts_
        if not _rer or abs(v1_ - v0_) < 0.05:
            return pts_
        # mvt3 c28 (ruling 1): a note that starts at the edge (up to 0.05 qn after the ramp) counts too; c27 left it out
        # and took the note before it, which sounds across the edge only by its lead
        hit_ = [(o_, en_) for o_, en_ in _snd if o_ < x1_ + _rer.get("edge_note_qn", 0.05) and en_ > x0_ + 1e-4]
        if not hit_:
            return pts_
        on_, en_ = min(hit_, key=lambda h_: abs(h_[0] - e_))
        pe_ = _rest_before(on_)
        if _gap_s(pe_, on_) >= _rer["min_gap_s"] and on_ - e_ <= 1.0 and e_ - on_ <= 1.0:
            a_ = max(pe_ + 0.002, on_ - _rer["max_ramp_qn"])
            b_ = max(a_ + 0.001, on_ - 0.005)
            if not any(o_ < b_ - 1e-4 and en2_ > a_ + 1e-4 for o_, en2_ in _snd):
                role_edge_moved.append([round(e_, 3), round(a_, 4), round(b_, 4)])
                return [(a_, v0_), (b_, v1_)]
        # no rest at the edge: CC7 carry from the nearest rest (before when rising, after when falling)
        up_ = v1_ > v0_
        rests_ = []
        ce_ = -3.0
        for o_, en2_ in _snd:
            if o_ > ce_ + 1e-4 and _gap_s(ce_, o_) >= _rer["min_gap_s"]:
                rests_.append((ce_, o_))
            ce_ = max(ce_, en2_)
        rests_.append((ce_, ce_ + 8.0))
        if up_:
            cand_ = [r_ for r_ in rests_ if r_[1] <= on_ + 1e-4 and on_ - r_[1] <= _rer["carry_qn"]]
            r_ = cand_[-1] if cand_ else None
        else:
            cand_ = [r_ for r_ in rests_ if r_[0] >= on_ + 1e-4 and r_[0] - on_ <= _rer["carry_qn"]]
            r_ = cand_[0] if cand_ else None
        if r_ is None or family == "timp":
            role_edge_join.append([round(e_, 3), round(v1_ - v0_, 2)])
            return pts_
        a_ = max(r_[0] + 0.002, r_[1] - _rer["max_ramp_qn"])
        b_ = max(a_ + 0.001, r_[1] - 0.005)
        hw_ = 0.5 * (sec_to_qn(qn_to_sec(on_) + _rer["carry_ramp_s"]) - on_)
        d_ = abs(v1_ - v0_)
        # mvt3 c28 (ruling 1; critics A #1, B #1, C #1): the CC7 change sits on the edge itself, on the row's own ramp
        # [x0, x1] (at least carry_ramp_s wide), unless the edge's note starts within carry_at_edge_qn of the edge (then
        # on that note-on, as in c27). c27 always used the note-on, up to 5.6 qn from the edge, so the role step played
        # at the start of a held note (bar 223 Violins I -5.5 dB, the final chord -3..-5 dB in the strings)
        nxt_ = min((o_ for o_, _ in _snd if e_ - 1e-4 <= o_ <= e_ + _rer.get("step_next_qn", 0.0)), default=None)
        # mvt3 c29: the end of the notes sounding at the edge, and the next note-on after it (a rest right after the edge)
        ce2_ = max([en2_ for o_, en2_ in _snd if o_ < e_ and en2_ > e_ - 1e-4] or [e_])
        no2_ = min([o_ for o_, _ in _snd if o_ > ce2_ - 1e-4] or [ce2_ + 8.0])
        if abs(e_ - on_) <= _rer.get("carry_at_edge_qn", 0.5):
            r0_, r1_ = on_ - hw_, on_ + hw_
        elif _rer.get("step_at_note_on") and (nxt_ is not None or (up_ and _gap_s(pe_, on_) >= _rer["min_gap_s"] and on_ <= e_ <= on_ + _rer.get("step_held_max_qn", 4.5))):
            # mvt3 c29 (ruling 8; critic A c29 #6): the rate-limited carry inside a held note (Violins I 896-899.9 +6 dB,
            # Horn 3 564-568 +4 dB at 2.8 dB/s) becomes a step at a note-on: the note that starts at the edge (within
            # step_next_qn after it) takes the change just before its note-on; else the held note itself takes it in the
            # rest before its note-on (the envelope edge moves there, no CC7 carry)
            if nxt_ is not None:
                r0_, r1_ = nxt_ - 0.006, nxt_ - 0.003
            else:
                a_ = max(pe_ + 0.002, on_ - _rer["max_ramp_qn"])
                b_ = max(a_ + 0.001, on_ - 0.005)
                role_edge_moved.append([round(e_, 3), round(a_, 4), round(b_, 4), "step"])
                return [(a_, v0_), (b_, v1_)]
        elif _rer.get("step_at_note_on") and nxt_ is None and ce2_ <= e_ + 0.1 and _gap_s(ce2_, no2_) >= _rer["min_gap_s"]:
            # mvt3 c29: the held note ends at the edge and a rest follows (Flute 1 156-168 before its solo at 168.85): the
            # envelope edge goes in that rest, no CC7 carry inside the held note
            a_ = ce2_ + 0.002
            b_ = max(a_ + 0.001, min(no2_ - 0.005, ce2_ + _rer["max_ramp_qn"]))
            role_edge_moved.append([round(e_, 3), round(a_, 4), round(b_, 4), "rest_after"])
            return [(a_, v0_), (b_, v1_)]
        else:
            r0_, r1_ = min(x0_, x1_), max(x0_, x1_)
            if r1_ - r0_ < 2 * hw_:
                m_ = 0.5 * (r0_ + r1_); r0_, r1_ = m_ - hw_, m_ + hw_
            # inside a held note the carry moves no faster than carry_rate_db_s (under the in-note gate's 3 dB/s): a rise ends
            # at the edge's ramp end, a fall starts at its ramp start
            if _rer.get("carry_rate_db_s"):
                w_ = d_ / _rer["carry_rate_db_s"]
                if qn_to_sec(r1_) - qn_to_sec(r0_) < w_:
                    if up_:
                        r0_ = sec_to_qn(qn_to_sec(r1_) - w_)
                    else:
                        r1_ = sec_to_qn(qn_to_sec(r0_) + w_)
        if up_:   # envelope up in the rest before; CC7 holds -d through to the edge, then ramps back
            r0_ = max(r0_, b_ + 0.001); r1_ = max(r1_, r0_ + 0.001)
            role_cc7.append([(a_, 0.0), (b_, -d_), (r0_, -d_), (r1_, 0.0)])
        else:     # CC7 ramps down at the edge and holds -d until the rest after, where the envelope falls
            r1_ = min(r1_, a_ - 0.001); r0_ = min(r0_, r1_ - 0.001)
            role_cc7.append([(r0_, 0.0), (r1_, -d_), (a_, -d_), (b_, 0.0)])
        role_edge_moved.append([round(e_, 3), round(a_, 4), round(b_, 4), "cc7", round(v1_ - v0_, 2)])
        return [(a_, v0_), (b_, v1_)]
    for a, b2, dbv, er in rows_:
        if er and _rer:
            # mvt3 c27: an end_ramp row as an "env" shape: the 0.5 qn ramp in through ROLE_EDGE_IN_REST, the slow
            # end ramp kept where it moves 2.5 dB/s or less, else moved into a rest as well
            pin = _edge_fix([(a - 0.5, 0.0), (a, dbv)], a)
            pout = [(b2 - er, dbv), (b2, 0.0)]
            if abs(dbv) / max(1e-6, _gap_s(b2 - er, b2)) > 2.5:
                pout = _edge_fix(pout, b2)
            if pout[0][0] < pin[-1][0]:
                pout = [(pin[-1][0], pout[0][1]), (max(pin[-1][0] + 0.001, pout[1][0]), pout[1][1])]
            vol_parts.append(("env", pin + pout))
            continue
        if er:
            vol_parts.append(("span", a, b2, dbv, er))
            continue
        prev_ = [r for r in rows_ if not r[3] and r != (a, b2, dbv, er) and -0.01 <= a - r[1] <= ROLE_CHAIN]
        next_ = [r for r in rows_ if not r[3] and r != (a, b2, dbv, er) and -0.01 <= r[0] - b2 <= ROLE_CHAIN]
        xf_ = next((v_ for k_, v_ in ROLE_EDGE_XF.get(tname, {}).items() if abs(a - k_) < 0.005), None)
        if prev_ and xf_:   # mvt3 c23 (ruling 4): the crossfade of a chained edge placed in a listed window (a rest)
            pin = [(xf_[0], 0.0), (xf_[1], dbv)]
            role_chained += 1
        elif prev_:
            pin = [(a - 0.1 + sf_shift(a), 0.0), (a + 0.15 + sf_shift(a), dbv)]
            role_chained += 1
        elif any(abs(a - x) < 0.02 for x in leg_on):
            pin = [(a, 0.0), (a + 0.25, dbv)]
        elif sf_shift(a):
            pin = [(a, 0.0), (a + 0.25, dbv)]
        else:
            pin = [(a - 0.5, 0.0), (a, dbv)]
        if next_:
            nb = min(r[0] for r in next_)
            xo_ = next((v_ for k_, v_ in ROLE_EDGE_XF.get(tname, {}).items() if abs(nb - k_) < 0.005), None)
            nb += sf_shift(nb)
            pout = [(max(pin[-1][0], nb - 0.1), dbv), (max(pin[-1][0] + 0.01, nb + 0.15), 0.0)]
            if xo_:   # mvt3 c23: see ROLE_EDGE_XF
                pout = [(max(pin[-1][0], xo_[0]), dbv), (max(pin[-1][0] + 0.001, xo_[1]), 0.0)]
        else:
            pout = [(max(pin[-1][0], b2), dbv), (max(pin[-1][0], b2) + 0.5, 0.0)]
        if _rer:   # mvt3 c27: ROLE_EDGE_IN_REST (an edge with a ROLE_EDGE_XF window is left as given)
            if not (prev_ and xf_):
                pin = _edge_fix(pin, a)
            if not (next_ and xo_):
                pout = _edge_fix(pout, min(r[0] for r in next_) if next_ else b2)
            if pout[0][0] < pin[-1][0]:   # a short row whose two edges collided: keep the order
                pout = [(pin[-1][0], pout[0][1]), (max(pin[-1][0] + 0.001, pout[1][0]), pout[1][1])]
        vol_parts.append(("env", pin + pout))
    vol_parts.rule = "hairpin"
    # c06 (C #1): crescendos to f or louder rise in dB too
    hp_chained = []
    loud_swells = []   # c32: untargeted crescendos from f - 2 or louder (HP_LOUD_SWELL_DB)

    def hp_untargeted(a_, b_):
        """c32: no printed mark (sf excepted, subito excepted) at the hairpin's end and no HP_TARGET_AT entry
        (the base_points rule)."""
        if any(b_ - 0.01 <= mq <= b_ + 1.0 and d_ not in ("sf", "sfz")
               and not any(round(mq, 3) in SUBITO[s_] for s_ in dyn_staves) for mq, d_ in marks):
            return False
        return not any(abs(a_ - k_) < 0.02 for s_ in dyn_staves for k_ in HP_TARGET_AT.get(s_, {}))
    # mvt1 c35 (critic A #1): a TRACK_WINDOWS track takes hairpin volume ramps (hpgain, soft-hairpin dB) only from hairpins
    # that start or end where it plays. The staff's hairpins outside its windows had held their arrival gain to the
    # track's next note: the coda solo track (first note 680) carried the +9 dB of a crescendo ending at 676 through its
    # first phrase (to 683.5). HP_GAIN_IN_WINDOW = False restores the old behaviour everywhere, HP_GAIN_IN_WINDOW_SKIP for
    # listed tracks (whose fitted levels were made on it)
    hps_v = [h_ for h_ in hps if not HP_GAIN_IN_WINDOW or tname not in TRACK_WINDOWS or tname in HP_GAIN_IN_WINDOW_SKIP
             or (CUR_ALIAS is not None and CUR_ALIAS in HP_GAIN_IN_WINDOW_SKIP)   # mvt1 c40: by the alias's own name
             or tw_keep(tname, h_[0]) or tw_keep(tname, h_[1] - EPS)]
    if family in HP_GAIN_DB:
        for a, b2, k in hps_v:
            mfa = k == "cresc" and DYN["mf"] - 2 <= base(b2 - 0.01) < DYN["f"] - 2   # c11 (B #3)
            if HP_LOUD_SWELL_DB is not None and k == "cresc" and base(a + 0.01) >= DYN["f"] - 2 and hp_untargeted(a, b2):
                # c32 (B #4a, C #2): a swell inside f/ff: a small gain, released at the next onset after its top; it does
                # not chain and takes no fff hold (each of v621's 388-405 swells took the ff arrival gain, chained to
                # +7 dB and held the fff gain to 408)
                arr = min([n["qn"] for n in ns if n["qn"] >= b2 - 0.05], default=b2)
                nx = min([n["qn"] for n in ns if n["qn"] > arr + 0.05], default=arr + HP_HOLD_CAP)
                g_ = HP_LOUD_SWELL_DB.get(family, 0.0)
                if g_ > 0:
                    vol_parts.append(["hpgain", a, b2, min(nx, arr + HP_HOLD_CAP, b2 + 1.0), g_, 0.0, HP_REL, 0.0, 0.0,
                                      False, False, True])
                loud_swells.append(round(a, 3))
                continue
            if k == "cresc" and (base(b2 - 0.01) >= DYN["f"] - 2 or mfa):
                # c08 (C #1): held to the first onset *after* the arrival note (it was the arrival itself, so the gain
                # was released over the arrival: falls of 3-6 dB in its first beat at bars 60, 61 and 78-79)
                arr = min([n["qn"] for n in ns if n["qn"] >= b2 - 0.05], default=b2)
                nx = min([n["qn"] for n in ns if n["qn"] > arr + 0.05], default=arr + HP_HOLD_CAP)
                hold_end = min(nx, arr + HP_HOLD_CAP)
                if arr > b2 + 0.25:   # no note lands on the arrival (a held note): release at the next onset, as before
                    hold_end = min(arr, b2 + 2.0)
                # c10 (C #4a): an arrival inside a SOSTENUTO_SPAN (ff "molto sostenuto", no hairpin) keeps HP_GAIN_DB to the
                # span's end and releases over HP_REL after it (Vln I/Vla/Cb fell 5-6 dB across bars 61-62)
                sost_end = next((e_ for a_, e_ in SOSTENUTO_SPANS if a_ - EPS <= arr < e_ - EPS), 0.0)
                g_ = HP_GAIN_MF_DB[family] if mfa else HP_GAIN_DB[family]
                for x_, by_ in HP_GAIN_AT_DB.items():   # c22 (critic C #3a): per-hairpin arrival gain by family / track
                    if abs(a - x_) < 0.05 and not mfa:
                        g_ = by_.get(tname, by_.get(family, g_))
                share_ = SOST_HOLD_SHARE
                fff_ = FFF_HOLD_CAP is not None and base(b2 - 0.01) >= DYN["fff"] - 2
                if fff_:   # mvt1 c02 (C #1a): held to the next printed mark or hairpin, at most FFF_HOLD_CAP qn
                    fe_ = min([mq for mq, d_ in marks if mq > arr + 0.05] + [a_ for a_, b_, k_ in hps if a_ > arr + 0.05]
                              + [arr + FFF_HOLD_CAP])
                    if fe_ > max(hold_end, sost_end):
                        sost_end, share_ = fe_, 1.0
                vol_parts.append(["hpgain", a, b2, hold_end, g_, 0.0, HP_REL, sost_end, share_ * g_, mfa, fff_])
        # c09 (B #1): chain consecutive crescendos to f+ (no softer printed mark between the first arrival and the
        # second start): the first holds its gain to the second's start without a release, the second starts from it
        hpi = sorted([it for it in vol_parts if it[0] == "hpgain"], key=lambda it: it[1])
        for it1, it2 in zip(hpi, hpi[1:]):
            b1, a2 = it1[2], it2[1]
            if len(it1) > 11 or len(it2) > 11:
                continue   # c32: a loud swell neither chains nor is chained
            if not it1[9] and -EPS <= a2 - b1 <= HP_CHAIN and not any(b1 + EPS < mq < a2 - EPS and DYN[d_] < base(b1 - 0.01)
                                                       for mq, d_ in marks if d_ in DYN) \
                    and not any(k_ == "decresc" and b1 - EPS <= a_ < a2 - EPS for a_, b_, k_ in hps):
                it1[3], it1[6] = a2, 0.0
                it2[5] = it1[4]
                # c11: max() so a chain from a smaller mf-arrival gain (HP_GAIN_MF_DB) keeps the f+ crescendo's own gain
                rise_ = (HP_CHAIN_RISE_FFF if len(it2) > 10 and it2[10] else HP_CHAIN_RISE).get(family, 0.0)   # mvt1 c02
                it2[4] = max(it2[4], it1[4] + rise_ * HP_GAIN_DB[family])   # c10 (C #3)
                if len(it2) > 10 and it2[10] and it2[7]:
                    it2[8] = it2[4]   # mvt1 c02: the fff hold keeps the chained gain
                hp_chained.append(round(a2, 3))
    # c22 (C #2a): an mf-arrival hpgain (it does not chain) whose track starts another crescendo within HP_CHAIN qn of the
    # arrival, with no softer mark or decrescendo between, holds its gain to that crescendo's start and releases it over
    # HP_MF_BRIDGE_REL while the new ramp rises (a hold only: the gains are not added into a chain)
    hp_bridged = []
    if family in HP_GAIN_DB:
        for it1 in [it for it in vol_parts if it[0] == "hpgain" and it[9]]:
            b1 = it1[2]
            nxt_ = sorted([(a_, b_) for a_, b_, k_ in hps if k_ == "cresc" and b1 + 0.05 < a_ <= b1 + HP_CHAIN])
            if not nxt_ or it1[3] >= nxt_[0][0]:
                continue
            a2 = nxt_[0][0]
            if any(b1 + EPS < mq < a2 - EPS and DYN[d_] < base(b1 - 0.01) for mq, d_ in marks if d_ in DYN) \
                    or any(k_ == "decresc" and b1 - EPS <= a_ < a2 - EPS for a_, b_, k_ in hps):
                continue
            it1[3], it1[6] = a2, HP_MF_BRIDGE_REL
            hp_bridged.append(round(a2, 3))
    # c14 (C #1): soft hairpins in lead spans (after the chaining, so they never chain)
    # c22 (C #4): and, with HP_GAIN_SOFT_ACC_DB, soft hairpins outside the lead lines; C #1: HP_SOFT_GAIN_AT per onset,
    # HP_SOFT_EXTRA_SPANS; hp_soft_spans (lead branch) keeps the phrase tops off these hairpins
    hp_soft, hp_soft_acc, hp_soft_spans = [], [], []
    if family in HP_GAIN_SOFT_DB:
        have = [(it[1], it[2]) for it in vol_parts if it[0] == "hpgain"]
        used_dec = []
        lead_sp = LEAD_SPANS.get(tname, []) + HP_SOFT_EXTRA_SPANS.get(tname, [])
        for a, b2, k in sorted(hps_v):   # mvt1 c35: hps_v (see above)
            in_lead = any(s_ - EPS <= a < e_ for s_, e_ in lead_sp)
            after_mf_ = k == "decresc" and any(abs(a - y) < 0.3 for x, y in have)   # c18 (C #1b): after an mf hpgain
            if (base(a + 0.01) > 66 and (not after_mf_ or not in_lead)) \
                    or any(abs(a - x) < EPS and abs(b2 - y) < EPS for x, y in have):
                continue
            if k == "cresc" and any(abs(a - x_) < 0.3 for x_ in SWELL_SOFT_GAIN_AT.get(tname, [])):
                if not in_lead:
                    continue
                # c18 (C #1): theme A's < > (both statements) ran backwards (Vln I 68-70 -3.7 dB, 70-72 +1.2): a small
                # messa di voce, +SWELL_SOFT_GAIN_DB at the top, released across the decrescendo to -1 dB at its end,
                # back to 0 over 1 qn (the top stays 2.2 dB under the printed mf at 82, the c15 constraint)
                dec = [(a_, b_) for a_, b_, k_ in hps if k_ == "decresc" and -0.3 <= a_ - b2 <= 0.3]
                g_ = SWELL_SOFT_GAIN_DB
                if dec:
                    da, db_ = min(dec)
                    vol_parts.append(("env", [(a, 0.0), (b2, g_), (max(b2, da) + 0.001, g_), (db_, -1.0),
                                              (db_ + 1.0, 0.0)]))
                    used_dec.append(round(da, 3))
                    hp_soft_spans.append((a, db_))
                else:
                    vol_parts.append(("env", [(a, 0.0), (b2, g_), (b2 + HP_REL, 0.0)]))
                    hp_soft_spans.append((a, b2))
                hp_soft.append(round(a, 3))
                continue
            if k == "cresc" and any(abs(a - x_) < 0.3 for x_ in SWELL_NO_SOFT_GAIN.get(tname, [])):
                continue   # c15 (B #1): an unmarked swell under the phrase's printed peak
            if in_lead:
                g_ = next((v_ for k_, v_ in HP_SOFT_GAIN_AT.get(tname, {}).items() if abs(a - k_) < 0.3),
                          HP_GAIN_SOFT_DB[family])
            else:
                # mvt3 c24 (critic B c24 #6): an entry may be (qn, track): that track only (the basses' pp pedal of bars
                # 43-50: the -2.5 dB gain of the 164-168 decrescendo was released at 2.8 dB/s inside a held re-bowed
                # note, a fader ramp of 2.5 dB with no printed hairpin)
                if any(abs(a - x_) < 0.3 if not isinstance(x_, (tuple, list)) else (abs(a - x_[0]) < 0.3 and x_[1] == tname)
                       for x_ in HP_SOFT_ACC_SKIP):
                    continue
                g_ = HP_GAIN_SOFT_ACC_DB
            if k == "cresc":
                dec = [(a_, b_) for a_, b_, k_ in hps if k_ == "decresc" and -0.3 <= a_ - b2 <= 0.3]
                if dec:   # messa di voce: held to the decrescendo, released linearly across it
                    da, db_ = min(dec)
                    vol_parts.append(["hpgain", a, b2, max(b2, da), g_, 0.0, max(0.25, db_ - da),
                                      0.0, 0.0, True])
                    used_dec.append(round(da, 3))
                    if in_lead:
                        hp_soft_spans.append((a, db_))
                        # c22 (C #1): a listed decrescendo depth deeper than the messa di voce's release adds the rest
                        dd_ = next((v_ for k_, v_ in HP_SOFT_DEC_AT.get(tname, {}).items() if abs(da - k_) < 0.3), 0.0)
                        if dd_ > g_:
                            nx = min([n["qn"] for n in ns if n["qn"] > db_ + 0.05], default=db_ + 1.0)
                            vol_parts.append(["hpgain", da, db_, min(nx, db_ + HP_HOLD_CAP), -(dd_ - g_), 0.0, HP_REL,
                                              0.0, 0.0, True])
                else:
                    arr = min([n["qn"] for n in ns if n["qn"] >= b2 - 0.05], default=b2)
                    nx = min([n["qn"] for n in ns if n["qn"] > arr + 0.05], default=arr + HP_HOLD_CAP)
                    hold_end = min(nx, arr + HP_HOLD_CAP)
                    if arr > b2 + 0.25:
                        hold_end = min(arr, b2 + 2.0)
                    vol_parts.append(["hpgain", a, b2, hold_end, g_, 0.0, HP_REL, 0.0, 0.0, True])
                    if in_lead:
                        hp_soft_spans.append((a, b2))
                (hp_soft if in_lead else hp_soft_acc).append(round(a, 3))
            elif k == "decresc" and round(a, 3) not in used_dec:
                # c18 (C #1b): a decrescendo after a crescendo is skipped only when that crescendo's messa di voce
                # already releases across it (used_dec); after an hpgain (mf) crescendo it gets its own ramp
                nx = min([n["qn"] for n in ns if n["qn"] > b2 + 0.05], default=b2 + 1.0)
                if in_lead:
                    dd_ = next((v_ for k_, v_ in HP_SOFT_DEC_AT.get(tname, {}).items() if abs(a - k_) < 0.3),
                               HP_SOFT_DEC_DB)
                    hp_soft_spans.append((a, b2))
                else:
                    dd_ = HP_GAIN_SOFT_ACC_DB
                vol_parts.append(["hpgain", a, b2, min(nx, b2 + HP_HOLD_CAP), -dd_, 0.0, HP_REL, 0.0, 0.0, True])
                (hp_soft if in_lead else hp_soft_acc).append(round(a, 3))
    # mvt1 c01 (B #1): a subito mark to a softer level ends every dB gain at once (no hold or release across it)
    sub_q = sorted({q_ for s_ in staves for q_ in SUBITO[s_]})
    for it in vol_parts:
        if it[0] != "hpgain" or it[4] <= 0:
            continue
        for sq_ in sub_q:
            if it[2] - 0.05 <= sq_ <= max(it[3], it[7]) + it[6] + EPS and base(sq_ + 0.01) < base(sq_ - 0.05):
                it[3], it[6], it[7] = min(it[3], sq_ - 0.001), 0.001, 0.0
                break
    # mvt3 c25 (critic B c25 #3, ruling 1): HP_END_AT_TARGET {"spans": [(from, to)], "within_qn": q, "max_dyn": "ff"}: a
    # crescendo's dB gain (hpgain) whose hairpin starts inside a listed span and ends within within_qn of a printed mark
    # no louder than max_dyn is gone by that mark's onset (0.02 qn before it) instead of being held into the arrival and
    # released after it (the accompaniment hit its printed ff 2-4 dB over its own ff and covered the entering tune, bar
    # 211). The fall is no faster than HP_REL_MAX_DB_S (default 2.8 dB/s), so the gain peaks earlier inside the hairpin
    # (research batch 5: crescendos rise early, then settle) while CC11 keeps rising to the printed level. Default off.
    hp_end_tgt = []
    if HP_END_AT_TARGET and family in HP_GAIN_DB:
        for it in [it_ for it_ in vol_parts if it_[0] == "hpgain" and it_[4] > 0]:
            a_, b_ = it[1], it[2]
            if not any(s0_ - EPS <= a_ < s1_ for s0_, s1_ in HP_END_AT_TARGET.get("spans", [])):
                continue
            mk_ = sorted(mq for mq, d_ in marks if d_ in DYN and b_ - EPS <= mq <= b_ + HP_END_AT_TARGET.get("within_qn", 1.0)
                         and DYN[d_] <= DYN[HP_END_AT_TARGET.get("max_dyn", "ff")])
            if not mk_:
                continue
            e_ = mk_[0] - 0.02
            rate_ = HP_REL_MAX_DB_S or 2.8
            pk_ = max(a_ + 0.5 * (e_ - a_), sec_to_qn(qn_to_sec(e_) - it[4] / rate_))
            s0_ = it[5] if len(it) > 5 else 0.0
            vol_parts.remove(it)
            vol_parts.rule = "hairpin"
            vol_parts.append(("env", [(a_, s0_), (pk_, it[4]), (e_, 0.0)]))
            hp_end_tgt.append([round(a_, 3), round(pk_, 3), round(e_, 3), it[4]])
    vol_parts.rule = "swell"
    # c06 (C #5): the long-note swell in dB (same notes as the CC11 swell)
    for a, b2, k in contours:
        if k.startswith("swell") and k != "swell_sost":
            vol_parts.append(("swell_db", a, b2, k == "swell_taper"))
    vol_parts.rule = "pitch_trim"
    # c06 (A #2): per-pitch trims on legato notes, from 0.1 qn before the score onset (legato leads), 0.25 qn ramp
    ptab = PITCH_TRIMS.get(tname, {})
    pt = {int(k): v for k, v in ptab.items() if not k.startswith("_")}
    allart = bool(ptab.get("_all_arts", False))   # c07 (B #1): Sus chords too
    arts_only = ptab.get("_arts")                  # c08 (A #3): only these articulations (pizz.)
    allp = set(ptab.get("_all_arts_pitches", []))  # c08 (B #1): these pitches on every articulation
    pitch_trimmed = 0

    def sec_qn(q0, t):   # t seconds after q0, in qn at the local tempo
        return q0 + t * bpm_at(q0) / 60

    def lvl_step(n_):
        """mvt3 c16 (LEVEL_STEP_AT_SCORE): (start qn, full qn) of a level step onto note n_: 30 ms centred on its score
        onset when it is led and follows a sounding note, else 0.03 / 0.01 s before its moved note-on (as before)."""
        m_ = new_on(n_)
        if LEVEL_STEP_AT_SCORE:
            lead_ = qn_to_sec(n_["qn"]) - qn_to_sec(m_)
            if lead_ >= LEVEL_STEP_MIN_LEAD_S - 1e-9 and any(o is not n_ and o["qn"] < n_["qn"] - EPS and o["end"] > m_ - 0.02
                                                              for o in ns):
                ts_ = qn_to_sec(n_["qn"])
                return sec_to_qn(ts_ - 0.015), sec_to_qn(ts_ + 0.015)
        return qn_before(m_, 0.03), qn_before(m_, 0.01)

    def step_env(n_, v_):
        """mvt3 c16: one level v_ for note n_: a step onto it (lvl_step) held to the step onto the next onset (at most
        1.5 s), exact breakpoints. With LEVEL_STEP_AT_SCORE off this is the c12 pizz.-trim shape."""
        a0_, a1_ = lvl_step(n_)
        nx_ = [o for o in ns if o["qn"] > n_["qn"] + EPS]
        cap_ = sec_qn(n_["qn"], 1.5)
        if nx_:
            o_ = min(nx_, key=lambda o: (o["qn"], new_on(o)))
            o_ = min((o for o in nx_ if abs(o["qn"] - o_["qn"]) < EPS), key=new_on)
            e0_, e1_ = lvl_step(o_) if new_on(o_) < cap_ else (qn_before(cap_, 0.03), qn_before(cap_, 0.01))
        else:
            e0_, e1_ = qn_before(cap_, 0.03), qn_before(cap_, 0.01)
        return [(a0_, 0.0), (a1_, v_), (max(a1_ + 0.002, e0_), v_), (max(a1_ + 0.004, e1_), 0.0)]

    def next_moved(n):
        """c09 (A #2): the moved onset of the note that follows n within 0.1 qn of its score end (None if none)."""
        e_ = orig_end[id(n)]
        nx_ = [new_on(o) for o in ns if o is not n and -EPS < o["qn"] - e_ < 0.1 and o["qn"] > n["qn"] + EPS]
        return min(nx_) if nx_ else None

    def joined_in(n):
        """c09 (A #2): n follows another note without a gap (its trim should start at its moved onset)."""
        return any(o is not n and o["qn"] < n["qn"] - EPS and abs(orig_end[id(o)] - n["qn"]) < 0.1 for o in ns)

    leg_join_holds = []   # mvt1 c39 (critic A #2)

    def leg_next(n):
        """mvt1 c39 (critic A #2): the legato target that joins n (starts within 0.1 qn of n's score end), or None"""
        e_ = orig_end[id(n)]
        c_ = [o for o in ns if o is not n and -EPS < o["qn"] - e_ < 0.1 and o["qn"] > n["qn"] + EPS
              and o.get("leg_target") and _lg(o.get("art") or "")]
        return min(c_, key=new_on) if c_ else None

    def trim_shape(n, dbv, ramp, early=None, tgt_trim=None):
        """c09 (A #2): the dB shape of a note trim. A joined note's trim starts at its moved onset (crossfading in over
        [moved - 0.05, moved + 0.03]); a trim on a note that another note follows ends over [next moved onset - 0.05,
        + 0.03], so the next note's (early) legato transition no longer plays under it.
        mvt1 c39 (critic A #2): LEG_JOIN_TRIM_HOLD moves the end of a positive trim on a note joined into a legato target
        past the transition (tgt_trim(o): the target's own trim in the same table)."""
        q0, e = n["qn"], orig_end[id(n)]
        if joined_in(n) and ramp == 0.25:
            # pitch trims only: from the moved onset over 0.25 qn. Note trims keep their 0.6 s ramp from the score onset:
            # a fast -8 dB step at the moved onset (first c09 render) deepened the transition sag at Ob1 190 (3.0 ->
            # 9.4 dB), CA 152 (3.9 -> 9.7) and Fl1 254 (4.8 -> 7.9)
            m = new_on(n)
            a0, a1 = m, m + 0.25
        else:
            a0, a1 = q0 - 0.1 if ramp == 0.25 else q0, (q0 - 0.1 if ramp == 0.25 else q0) + ramp
        nm = next_moved(n)
        z0, z1 = (nm - 0.05, nm + 0.03) if nm is not None else (e, e + 0.1)
        lj_ = LEG_JOIN_TRIM_HOLD.get(tname, LEG_JOIN_TRIM_HOLD.get(family))
        end_v_ = dbv if early is None else early[1]
        if lj_ and nm is not None and end_v_ is not None and end_v_ > 0:
            t_ = leg_next(n)
            sh_ = next((v_ for k_, v_ in LEG_JOIN_TRIM_HOLD_AT.get(tname, {}).items() if t_ is not None
                        and abs(t_["qn"] - k_) < 0.02), 1.0)
            if t_ is not None and abs(new_on(t_) - nm) < 1e-6 and not (tgt_trim and (tgt_trim(t_) or 0) > 0) and sh_ > 0:
                z0o_, z1o_ = z0, z1
                z0 = max(z0, sec_qn(nm, lj_[0]))
                z1 = max(sec_qn(nm, lj_[0] + lj_[1]), sec_qn(t_["qn"], LEG_JOIN_TRIM_REACH_S), z0 + 0.002)
                leg_join_holds.append([round(n["qn"], 3), round(t_["qn"], 3), round(end_v_, 2)] + ([sh_] if sh_ < 1 else []))
                if sh_ < 1 and early is None and z0 > z1o_ and a1 <= z0o_:
                    # a partial hold: down to sh_ x the trim over the c09 end, that share held and released as above
                    return [(a0, 0.0), (a1, dbv), (z0o_, dbv), (z1o_, sh_ * dbv), (z0, sh_ * dbv), (max(z1, z0 + 0.002), 0.0)]
        if early is not None:   # {"early", "body"} shape
            ea, bo = early
            pts_ = [(a0, 0.0), (a1, ea), (sec_qn(q0, 0.35), ea), (max(sec_qn(q0, 0.6), sec_qn(q0, 0.35) + 0.01), bo)]
            pts_ = [p_ for p_ in pts_ if p_[0] < z0] or [(a0, 0.0)]
            pts_ += [(max(z0, pts_[-1][0] + 0.001), value_at(pts_ + [(1e9, bo)], z0) if len(pts_) > 1 else bo),
                     (max(z1, pts_[-1][0] + 0.002), 0.0)]
            return pts_
        if a1 > z0:   # short note: the ramp in does not finish before the ramp out
            peak = dbv * max(0.0, min(1.0, (z0 - a0) / max(1e-6, a1 - a0)))
            return [(a0, 0.0), (max(z0, a0 + 0.001), peak), (max(z1, a0 + 0.002), 0.0)]
        return [(a0, 0.0), (a1, dbv), (z0, dbv), (z1, 0.0)]
    pskip = [float(x) for x in ptab.get("_skip_onsets", [])]   # c14: onsets that keep no pitch trim

    def ptrim_of(o):   # mvt1 c39 (A #2): the pitch trim o would get from this table (body value; 0 if none)
        if o["pitch"] not in pt or any(abs(o["qn"] - x) < 0.02 for x in pskip):
            return 0.0
        a_ = o.get("art") or ""
        if not ((a_ in arts_only) if arts_only else (allart or o["pitch"] in allp or _lg(a_))):
            return 0.0
        v0_ = pt[o["pitch"]]
        return v0_["body"] if isinstance(v0_, dict) else v0_
    for n in ns:
        if n["pitch"] not in pt or any(abs(n["qn"] - x) < 0.02 for x in pskip):
            continue
        art_ = n.get("art") or ""
        ok = (art_ in arts_only) if arts_only else (allart or n["pitch"] in allp or _lg(art_))
        if not ok:
            continue
        # c09 (B #2): the c08 cut of long-note trims at onset + 3 qn is removed (it put +5 dB steps into held pp Cb
        # pedals); the bar 83 Cb lift is a role in roles.json instead
        v_ = pt[n["pitch"]]
        short1_ = SHORT_ONE_LEVEL_QN is not None and orig_end[id(n)] - n["qn"] <= SHORT_ONE_LEVEL_QN + EPS
        if short1_ and not isinstance(v_, dict) and "izz" not in art_:
            vol_parts.append(("env", step_env(n, v_), True))   # mvt3 c16: one level per short note
        elif ("izz" in art_ or n.get("rep_sus") or n.get("rep_stac") or n.get("short_stroke")) and not isinstance(v_, dict):
            # mvt1 c04: repeated strokes (REP_SPLIT) too: the 0.25 qn ramp on each eighth/triplet made a 3 dB sawtooth
            # c12 (A #1): a pizz. trim is a step at full value on the attack (the 0.25 qn ramp from the moved onset,
            # sampled on the 0.125 qn grid, reached full depth just before the next note: F4 -8 sat at -1.8..-2.5 dB on
            # its attack and cut the following note instead); held to the next onset (at most 1.5 s), exact breakpoints
            q0 = new_on(n)
            nx_ = [new_on(o) for o in ns if o["qn"] > n["qn"] + EPS]
            ne_ = min(min(nx_) if nx_ else 1e9, sec_qn(n["qn"], 1.5))
            vol_parts.append(("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
                                      (max(qn_before(q0, 0.01) + 0.002, qn_before(ne_, 0.03)), v_),
                                      (max(qn_before(q0, 0.01) + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
        elif isinstance(v_, dict):   # c08 (A #1): {"early", "body"}: the sample's early sag is not cut with the body
            vol_parts.append(("env", trim_shape(n, None, 0.25, (v_["early"], v_["body"]), tgt_trim=ptrim_of)))
        else:
            vol_parts.append(("env", trim_shape(n, v_, 0.25, tgt_trim=ptrim_of)))
        pitch_trimmed += 1
    vol_parts.rule = "metric"
    # c20 (C #3): METRIC_DB steps on plucked onsets (one per onset; a chord counts once)
    metric_db_n = collections.Counter()
    if METRIC_DB and family != "harm":
        acc_q_ = set(round(x, 3) for x in accent_q) | {round(q_, 3) for q_, d_ in marks if d_ in ("sf", "sfz")}
        ons_ = sorted({n["qn"] for n in ns})
        done_ = set()
        for n in sorted(ns, key=lambda o: o["qn"]):
            q_ = n["qn"]
            if q_ in done_ or not any(a_ - EPS <= q_ < b_ for a_, b_ in METRIC_SPANS):
                continue
            if not (family == "harp" or "izz" in (n.get("art") or "")):
                continue
            done_.add(q_)
            if round(q_, 3) in acc_q_ or any(a_ - EPS <= q_ < b_ for a_, b_ in LEAD_SPANS.get(tname, [])):
                continue
            bk_ = beat_kind(q_)
            if bk_ == "downbeat":
                kind_ = "down"
            elif bk_ == "mid":
                kind_ = "mid"
            elif abs(q_ - round(q_)) > 0.01:
                kind_ = "off"
            else:
                continue
            v_ = METRIC_DB.get(kind_, 0.0)
            if not v_:
                continue
            q0 = min(new_on(o) for o in ns if abs(o["qn"] - q_) < EPS)
            nx_ = [o_ for o_ in ons_ if o_ > q_ + EPS]
            nq_ = min(new_on(o) for o in ns if abs(o["qn"] - nx_[0]) < EPS) if nx_ else sec_qn(q_, 1.5)
            ne_ = min(nq_, sec_qn(q_, 1.5))
            vol_parts.append(("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
                                      (max(qn_before(q0, 0.01) + 0.002, qn_before(ne_, 0.03)), v_),
                                      (max(qn_before(q0, 0.01) + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
            metric_db_n[kind_] += 1
    # mvt1 c08 (critics C #5, A #6): the same level steps on short unslurred bowed notes inside METRIC_BOWED spans and on
    # loud felt timpani strokes (METRIC_TIMP_DB): velocity does not move the KS Master sustain rows (c06) and moves the
    # felt strokes less than their round robins (c07). One step per onset, at full value on the attack, held to the next
    # onset; not on accents, sf, REP_SPLIT strokes, tied strokes, tremolo or pizz.
    def metric_kind(q_):
        bk_ = beat_kind(q_)
        if bk_ == "downbeat":
            return "down"
        if bk_ == "mid":
            return "mid"
        # mvt3 c08: in 2/2 (and any even-numbered bar) the half bar is the second strong beat; beat_kind calls it "weak"
        # (only 4/4 has a "mid"), so its eighths took the plain "beat" step
        ts_ = [t for t in sorted(timesig) if t[0] <= q_ + EPS] or [(0.0, 4, 4)]
        bl_ = ts_[-1][1] * 4.0 / ts_[-1][2]
        if ts_[-1][1] % 2 == 0 and abs((q_ - ts_[-1][0]) % bl_ - bl_ / 2) < 0.01:
            return "mid"
        return "beat" if abs(q_ - round(q_)) < 0.01 else "off"
    mtab_, mspans_ = None, []
    if family == "string" and METRIC_BOWED.get(tname):
        mtab_, mspans_ = METRIC_BOWED_DB, METRIC_BOWED[tname]
    elif family == "timp" and METRIC_TIMP_DB:
        mtab_, mspans_ = METRIC_TIMP_DB, [(-1.0, 1e9)]
    if mtab_:
        acc_q2_ = set(round(x, 3) for x in accent_q) | {round(q_, 3) for q_, d_ in marks if d_ in ("sf", "sfz")}
        ons_ = sorted({n["qn"] for n in ns})
        done_ = set()
        for n in sorted(ns, key=lambda o: o["qn"]):
            q_ = n["qn"]
            if q_ in done_ or not any(a_ - EPS <= q_ < b_ for a_, b_ in mspans_):
                continue
            art_ = n.get("art") or ""
            if family == "timp":
                if not art_.endswith("Lng") or n.get("tie_stroke") or base(q_) < mtab_.get("min_cc", DYN["f"]) - EPS:
                    continue
            else:
                if n.get("slur") is not None or ((n.get("rep_sus") or n.get("rep_stac")) and not METRIC_BOWED_REP) \
                        or n.get("grace") \
                        or art_ in ("Tremolo",) or "izz" in art_ or orig_end[id(n)] - q_ > METRIC_BOWED_MAX_QN + EPS:
                    continue
            if round(q_, 3) in acc_q2_ or any(abs(o["qn"] - q_) < EPS and round(o["qn"], 3) in acc_q2_ for o in ns):
                continue
            done_.add(q_)
            kind_ = metric_kind(q_)
            tab_q_ = mtab_
            if family == "string":   # mvt3 c08: a per-span table
                tab_q_ = next((t_ for a_, b_, t_ in METRIC_BOWED_DB_SPANS.get(tname, []) if a_ - EPS <= q_ < b_), mtab_)
            v_ = tab_q_.get(kind_, 0.0)
            if not v_:
                continue
            q0 = min(new_on(o) for o in ns if abs(o["qn"] - q_) < EPS)
            nx_ = [o_ for o_ in ons_ if o_ > q_ + EPS]
            nq_ = min(new_on(o) for o in ns if abs(o["qn"] - nx_[0]) < EPS) if nx_ else sec_qn(q_, 1.5)
            ne_ = min(nq_, sec_qn(q_, 1.5))
            # mvt3 c11 (critic A #1): inside a STR_REP_DETACH span with "beat_gap_db", the step starts at the moved onset
            # (0 -> full over 10 ms) instead of 0.03 s early, so it does not lift the stroke before's tail in the gap
            at_on_ = family == "string" and any(
                len(sp_) > 2 and sp_[2].get("beat_gap_db") and sp_[0] - EPS <= q_ < sp_[1] - EPS
                for sp_ in ((STR_REP_DETACH or {}).get("at") or {}).get(tname, []))
            p0_, p1_ = (q0, sec_qn(q0, 0.010)) if at_on_ else (qn_before(q0, 0.03), qn_before(q0, 0.01))
            if LEVEL_STEP_AT_SCORE and not at_on_ and family == "string":
                vol_parts.append(("env", step_env(min((o for o in ns if abs(o["qn"] - q_) < EPS), key=new_on), v_), True))
            else:
                vol_parts.append(("env", [(p0_, 0.0), (p1_, v_),
                                          (max(p1_ + 0.002, qn_before(ne_, 0.03)), v_),
                                          (max(p1_ + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
            metric_db_n["m_" + kind_] += 1
    vol_parts.rule = "sost"
    # c14 (C #4): sostenuto long notes: a hold that rises into the next note instead of the swell_db arc
    sost_held = []
    for a, b2, k in contours:
        if k != "swell_sost":
            continue
        n_ = max([o for o in ns if abs(o["qn"] - a) < EPS], key=lambda o: orig_end[id(o)])
        nm_ = next_moved(n_)
        nm_ = b2 if nm_ is None else nm_
        x40 = a + 0.4 * (b2 - a)
        nxc = [c_ for c_ in contours if c_[2] == "swell_sost" and abs(c_[0] - b2) < 0.1] if SOST_HOLD_THROUGH else []
        if nm_ - 0.25 > x40 + 0.01 and nxc:   # c15 (A #1): held through the next onset, released at its 40%
            na_, nb_ = nxc[0][0], nxc[0][1]
            nx40 = na_ + 0.4 * (nb_ - na_)
            vol_parts.append(("env", [(a, 0.0), (x40, 0.0), (nm_ - 0.25, SOST_SUSTAIN_DB),
                                      (max(nm_ + 0.25, na_ + 0.25), SOST_SUSTAIN_DB),
                                      (max(nx40, na_ + 0.26, nm_ + 0.26), 0.0)]))
            sost_held.append(round(b2, 3))
        elif nm_ - 0.25 > x40 + 0.01:
            vol_parts.append(("env", [(a, 0.0), (x40, 0.0), (nm_ - 0.25, SOST_SUSTAIN_DB), (nm_, 0.0)]))
    vol_parts.rule = "early_fill"
    # c08 (A #1): early fills on sagging legato targets
    ef = {float(k): v for k, v in EARLY_FILLS.get(tname, {}).items() if not k.startswith("_")}
    early_n = 0
    for n in ns:
        hit = [v for k, v in ef.items() if abs(n["qn"] - k) < 0.02]
        if hit:
            q0 = n["qn"]
            if isinstance(hit[0], dict):
                # c10 (A #2, #4): {"db", "pre_s"}: the hole starts before the score onset (the target's transition runs
                # from its moved onset): 0 at onset - pre_s - 0.03 s, +db at onset - pre_s, held to + 0.10 s, 0 by + 0.35 s
                # c11 (A #2, C #2): optional "hold_s" (default 0.10): held to onset + hold_s, 0 by + hold_s + 0.25 s
                X, P_ = hit[0]["db"], hit[0].get("pre_s", 0.0)
                H_ = hit[0].get("hold_s", 0.10)
                p0 = [(qn_before(q0, P_ + 0.03), 0.0), (qn_before(q0, P_), X)] if P_ > 0 else [(q0 - 0.02, 0.0), (q0, X)]
                if P_ < 0:   # mvt1 c03: a negative pre_s starts the fill after the onset (fills moved 1/6 qn later)
                    p0 = [(sec_qn(q0, max(0.0, -P_ - 0.03)), 0.0), (sec_qn(q0, -P_), X)]
                vol_parts.append(("env", p0 + [(sec_qn(q0, H_), X), (sec_qn(q0, H_ + 0.25), 0.0)], True))
            else:
                vol_parts.append(("env", [(q0 - 0.02, 0.0), (sec_qn(q0, 0.05), hit[0]), (sec_qn(q0, 0.35), hit[0]),
                                          (sec_qn(q0, 0.6), 0.0)]))
            early_n += 1
    vol_parts.rule = "loop_fill"
    # c16 (A #1): loop-seam fills: a raised-cosine lift (0 at t - w, full from t - w/2 to t + w/2, 0 at t + w) at each
    # measured seam dip, seconds after the note's moved start; exact breakpoints
    lf_ = {float(k): v for k, v in LOOP_FILLS.get(tname, {}).items() if not k.startswith("_")}
    loop_n = 0
    for n in ns:
        hit = [v for k, v in lf_.items() if abs(n["qn"] - k) < 0.02]
        if not hit:
            continue
        t0 = max(0.0, qn_to_sec(new_on(n))) if new_on(n) >= 0 else 0.0
        bumps_ = [(t0 + t_, dbv, w_) for t_, dbv, w_ in hit[0]]

        def bump(t, c_, dbv, w_):
            d_ = abs(t - c_)
            if d_ <= 0.5 * w_:
                return dbv
            if d_ >= w_:
                return 0.0
            return dbv * 0.5 * (1 + __import__("math").cos(__import__("math").pi * (d_ - 0.5 * w_) / (0.5 * w_)))
        # overlapping bumps take the larger value, not the sum; sampled every 0.025 s inside each bump
        ts_ = sorted({round(c_ + w_ * (-1 + k_ / 20), 4) for c_, _, w_ in bumps_ for k_ in range(41)}
                     | {round(c_ + x_, 4) for c_, _, w_ in bumps_ for x_ in (-w_, -0.5 * w_, 0.5 * w_, w_)})
        # c17 (A #1): compare with the last kept point (the c16 test against the previous point dropped every inner point
        # of a bump narrower than 0.4 s, so 14 of the 43 fills never reached the envelope)
        kept_ = []
        for i_, t_ in enumerate(ts_):
            if not kept_ or t_ - kept_[-1] >= 0.02 or i_ == len(ts_) - 1:
                kept_.append(t_)
        ts_ = kept_
        # mvt1 c10 (critic A #2): a negative bump cuts a sample bloom; overlapping bumps take the value of larger size
        ps_ = [(sec_to_qn(t_), round(max((bump(t_, c_, d_, w_) for c_, d_, w_ in bumps_), key=abs), 3)) for t_ in ts_]
        vol_parts.append(("env", ps_, True))
        loop_n += len(bumps_)
    # mvt1 c04 (critic A #3, C #4): TIMP_ROLL_RESTRIKE plan for a roll note as written at the output stage (moved onset
    # and length rounded to 4 places): [(piece onset qn, velocity offset)], seeded per note. The output stage splits the
    # note with it; here each new piece gets a short dip over the re-strike bump (+2 dB from +0.02 to +0.18 s, c04 render)
    def restrike_plan(qn_, dur_, sq_, pitch_):
        import random as _r
        if not any(abs(sq_ - k_) < 0.02 for k_ in TIMP_ROLL_RESTRIKE.get("at", [])):
            return []
        t0_, t1_ = qn_to_sec(qn_), qn_to_sec(qn_ + dur_)
        if t1_ - t0_ <= TIMP_ROLL_RESTRIKE["min_s"]:
            return []
        rng_ = _r.Random(int(round(sq_ * 1000)) + pitch_)
        lo_, hi_ = TIMP_ROLL_RESTRIKE["seg_s"]
        cuts_, t_ = [], t0_
        while t1_ - t_ > hi_ + lo_:
            t_ += rng_.uniform(lo_, hi_)
            cuts_.append(t_)
        if t1_ - t_ > hi_:   # the remainder is split in two pieces of at least lo_
            cuts_.append(t_ + (t1_ - t_) / 2)
        return [(round(sec_to_qn(c_), 4), rng_.randint(-TIMP_ROLL_RESTRIKE["vel_jit"], TIMP_ROLL_RESTRIKE["vel_jit"]))
                for c_ in cuts_]
    vol_parts.rule = "restrike"
    if family == "timp" and TIMP_ROLL_RESTRIKE.get("at") and TIMP_ROLL_RESTRIKE.get("dip_db"):
        d0_, d1_, d2_ = TIMP_ROLL_RESTRIKE["dip_s"]
        for n in ns:
            if not (n.get("art") or "").endswith("Rls"):
                continue
            q1_ = round(new_on(n), 4)
            for cq_, _ in restrike_plan(q1_, round(max(0.02, n["end"] - q1_), 4), round(n["qn"], 4), n["pitch"]):
                tc_ = qn_to_sec(cq_)
                vol_parts.append(("env", [(cq_, 0.0), (sec_to_qn(tc_ + d0_), TIMP_ROLL_RESTRIKE["dip_db"]),
                                          (sec_to_qn(tc_ + d1_), TIMP_ROLL_RESTRIKE["dip_db"]), (sec_to_qn(tc_ + d2_), 0.0)], True))
    vol_parts.rule = "breath"
    # mvt1 c05 (critic C #2): a dip over each staggered-breath re-entry (BREATH_SPLIT_AT; the split is at the output stage)
    for sq_k, pts_ in BREATH_SPLIT_AT.get(tname, {}).items():
        if not any(abs(n["qn"] - sq_k) < 0.02 for n in ns):
            if tname in TRACK_WINDOWS and not tw_keep(tname, sq_k):
                continue   # mvt1 c39: the note plays on another track (TRACK_WINDOWS / ALIAS_TRACKS)
            raise SystemExit(f"BREATH_SPLIT_AT {tname} {sq_k}: no note there")
        for p_ in pts_:
            tp_ = qn_to_sec(p_)
            vol_parts.append(("env", [(qn_before(p_, 0.02), 0.0), (sec_to_qn(tp_ + 0.03), BREATH_SPLIT["dip_db"]),
                                      (sec_to_qn(tp_ + 0.12), BREATH_SPLIT["dip_db"]),
                                      (sec_to_qn(tp_ + BREATH_SPLIT["dip_s"]), 0.0)], True))
    vol_parts.rule = "loop_fill"
    # c17 (A #1): periodic inverse loop profile: from t0 + LP_START_S to the note's end - LP_END_S, every LP_STEP_S, add
    # corr_db at the phase (t - t0) mod period_s, faded in and out over LP_FADE_S; t0 = max(0, moved start) in score seconds
    lp_ = {float(k): v for k, v in LOOP_PROFILES.get(tname, {}).items() if not k.startswith("_")}
    for n in ns:
        hit = [v for k, v in lp_.items() if abs(n["qn"] - k) < 0.02]
        if not hit:
            continue
        per_, cor_ = hit[0]["period_s"], hit[0]["corr_db"]
        t0 = max(0.0, qn_to_sec(new_on(n))) if new_on(n) >= 0 else 0.0
        ta_, tb_ = t0 + LP_START_S, qn_to_sec(orig_end[id(n)]) - LP_END_S
        if tb_ - ta_ < 2 * LP_FADE_S:
            continue
        ps_, t_ = [], ta_
        while t_ <= tb_ + 1e-9:
            f_ = min(1.0, (t_ - ta_) / LP_FADE_S, (tb_ - t_) / LP_FADE_S)
            ps_.append((sec_to_qn(t_), round(f_ * cor_[min(len(cor_) - 1, int(((t_ - t0) % per_) / 0.02))], 3)))
            t_ += LP_STEP_S
        vol_parts.append(("env", ps_, True))
        loop_n += 1
    vol_parts.rule = "rebow_fill"
    # c26: re-bow fills (REBOW_FILLS): each list runs from its re-bow to the next one (exact breakpoints, seconds on the
    # real tempo map); its last value holds until the next list starts, and after the last re-bow to the release
    rbf_ = sorted((float(k), v) for k, v in REBOW_FILLS.get(tname, {}).items() if not k.startswith("_"))
    rebow_fill_ends = []   # mvt1 c45 (ported mvt3 c04): [re-bow qn, hold end qn, last dB] for lists ended at their note's end
    for i_, (p_, pts_) in enumerate(rbf_):
        ps_ = [(sec_to_qn(qn_to_sec(p_) + t_), d_) for t_, d_ in pts_]
        # mvt1 c02: up to the next list's first point (fit_rebows.py now starts a list PRE_FILL_S before its re-bow)
        e_ = sec_to_qn(qn_to_sec(rbf_[i_ + 1][0]) + min(-0.04, rbf_[i_ + 1][1][0][0])) if i_ + 1 < len(rbf_) else END + 0.5
        # mvt1 c45 (critic B #1): a list never holds into a later note. When a note of this track starts after the end
        # of the note the re-bow belongs to and before e_, the last value holds to that note's end and is gone
        # REBOW_FILL_END_S later (Movement I c44: two lists at qn 576 held +4.1 / -2.0 dB over 26-29 bars of later notes)
        own_ = [n for n in ns if n["qn"] + 0.05 < p_ < n["end"] - 0.05]
        if REBOW_FILL_END_S is not None and own_ and abs(pts_[-1][1]) > 1e-3:   # (a list ending on 0 dB keeps its points)
            ne_ = max(n["end"] for n in own_)
            if any(ne_ - 0.1 <= n["qn"] < e_ for n in ns if n not in own_):
                h_ = max(ne_, ps_[-1][0])
                z_ = sec_to_qn(qn_to_sec(h_) + REBOW_FILL_END_S)
                if z_ < e_:
                    if h_ > ps_[-1][0] + 1e-4:
                        ps_.append((h_, pts_[-1][1]))
                    ps_.append((z_, 0.0))
                    rebow_fill_ends.append([p_, round(h_, 4), pts_[-1][1]])
                    e_ = None
        if e_ is not None and e_ > ps_[-1][0] + 1e-4:
            ps_.append((e_, pts_[-1][1]))
        vol_parts.append(("env", ps_, True))
    vol_parts.rule = "join_notch"
    # c18 (C #3a): JOIN_NOTCH: a dB notch over a moved legato join's transition peak, (from qn, to qn, dB) with 0.04 qn
    # ramps, exact breakpoints
    for a_, b_, d_ in JOIN_NOTCH.get(tname, []):
        vol_parts.append(("env", [(a_ - 0.04, 0.0), (a_, d_), (b_, d_), (b_ + 0.04, 0.0)], True))
    vol_parts.rule = "level_shape"
    # mvt1 c06 (C #2): explicit level shapes from the config (per track and "_all")
    for ps_ in LEVEL_SHAPES.get(tname, []) + LEVEL_SHAPES.get("_all", []):
        vol_parts.append(("env", [(float(x_), float(d_)) for x_, d_ in ps_], True))
    vol_parts.rule = "steady_level"
    # mvt3 c15 (mvt1 c54): STEADY_LINE "level_db" {score qn: dB}: a per-note level step on the span's notes, fitted on a
    # render: each note's value from 0.03 s before its moved note-on (reached 0.008 s before it) to the same point of
    # the next note; back to 0 after a note with no listed successor. "level_all": the span's other notes too
    def _sl_sp(n):
        if n.get("steady"):
            return n["steady"] if (n["steady"].get("level_db") or n["steady"].get("level_default")) else None
        return next((x_ for x_ in STEADY_LINE.get(tname, []) if x_.get("level_all") and (x_.get("level_db") or x_.get("level_default"))
                     and x_["from"] - EPS <= n["qn"] < x_["to"] - EPS), None)
    sl_ = sorted((n for n in ns if not n.get("grace") and _sl_sp(n) is not None), key=lambda n: (n["qn"], n["pitch"]))
    if sl_:
        # "level_default" {row: dB}: the step of a span note that "level_db" does not list (the row's start level)
        lv_ = lambda n: next((float(v_) for k_, v_ in _sl_sp(n)["level_db"].items() if abs(n["qn"] - float(k_)) < 0.02),
                             float(_sl_sp(n).get("level_default", {}).get(n.get("art") or "", 0.0)))
        ps_, cur_, end_ = [], 0.0, None
        for n in sl_:
            t_ = qn_to_sec(new_on(n))
            # mvt3 c16: span key "level_rest_qn" (default 0.3): a shorter gap holds the level (c15: the level fell
            # to 0 dB and came back between the staccato quarters of a run, 6.8 dB up and down per note)
            if end_ is not None and new_on(n) > end_ + _sl_sp(n).get("level_rest_qn", 0.3) and cur_ != 0.0:   # a rest: release the last value
                ps_ += [(end_ + 0.02, cur_), (end_ + 0.07, 0.0)]
                cur_ = 0.0
            v_ = lv_(n)
            if v_ != cur_:
                if LEVEL_STEP_AT_SCORE:   # mvt3 c16
                    a0_, a1_ = lvl_step(n)
                    a0_ = max(a0_, ps_[-1][0] + 0.001) if ps_ else a0_
                    ps_ += [(a0_, cur_), (max(a1_, a0_ + 0.001), v_)]
                else:
                    ps_ += [(sec_to_qn(t_ - 0.03), cur_), (sec_to_qn(t_ - 0.008), v_)]
                cur_ = v_
            end_ = max(n["end"], end_ or 0.0)
        if cur_ != 0.0:
            ps_ += [(end_ + 0.02, cur_), (end_ + 0.07, 0.0)]
        if ps_:
            vol_parts.append(("env", ps_, True))
    vol_parts.rule = "level_shape_s"
    # mvt1 c24: LEVEL_SHAPES_S (seconds around a score onset, converted on the real tempo map)
    for q0_, ps_ in LEVEL_SHAPES_S.get(tname, []):
        t0_ = qn_to_sec(float(q0_))
        vol_parts.append(("env", [(sec_to_qn(t0_ + float(x_)), float(d_)) for x_, d_ in ps_], True))
    vol_parts.rule = "cresc_front"
    # mvt1 c36 (critic C #3): CRESC_FRONTS (build/cresc_fronts.json {track: {score onset: [cut dB, peak s, sag s]}}): a
    # held note that starts a printed crescendo blooms over its first 0.1-1 s and sags before the hairpin's CC ramp
    # brings it back (20 of 36 such notes in c35 ended the crescendo under their own attack): a cut from the moved onset,
    # 0 at the onset, -cut at +0.06 s and at +peak s, 0 again at +sag s (seconds, exact breakpoints); fitted on a render
    cresc_fronts = []
    cresc_front_shift = []   # mvt1 c40 (critic A #2): [score onset, lead s, [cut, peak, sag] after the shift or None]
    for k_, v_ in CRESC_FRONTS.get(tname, {}).items():
        if k_.startswith("_"):
            continue
        n_ = next((o for o in ns if abs(o["qn"] - float(k_)) < 0.02), None)
        if n_ is None:
            if not (tname in TRACK_WINDOWS and not tw_keep(tname, float(k_))):   # mvt1 c40: played on another track
                print(f"  WARN {tname}: CRESC_FRONTS {k_} has no note", file=sys.stderr)
            continue
        cut_, pk_, sg_ = (float(x_) for x_ in v_)
        t0_ = qn_to_sec(new_on(n_))
        lead_ = qn_to_sec(n_["qn"]) - t0_
        if CRESC_FRONT_LEG_SCORE and n_.get("leg_target") and lead_ > 0.01:
            # mvt1 c40 (critic A #2): on a led legato target the old note still carries the sound until about the score
            # onset; a cut from the moved onset reached full depth inside the transition (8 of 18 fronts: dips 3.2-11.2
            # dB). The cut starts at the score onset; its peak and sag keep their absolute times (the bloom it was
            # fitted to); a cut whose sag ends within 0.1 s of the score onset lies inside the transition and is left out
            if sg_ - lead_ < 0.1:
                cresc_front_shift.append([round(n_["qn"], 3), round(lead_, 3), None])
                continue
            t0_, pk_ = t0_ + lead_, max(0.07, pk_ - lead_)
            sg_ = max(pk_ + 0.02, sg_ - lead_)
            cresc_front_shift.append([round(n_["qn"], 3), round(lead_, 3), [cut_, round(pk_, 3), round(sg_, 3)]])
        ps_ = [(0.0, 0.0), (0.06, -cut_), (max(0.07, pk_), -cut_), (max(pk_ + 0.02, sg_), 0.0)]
        vol_parts.append(("env", [(sec_to_qn(t0_ + x_), d_) for x_, d_ in ps_], True))
        cresc_fronts.append(round(n_["qn"], 3))
    if LEG_RAMP_WARN:
        # mvt1 c40 (critic A #2): a level row whose first ramp (0.3 s or shorter) moves inside a led legato target's
        # transition (from its moved onset to 0.06 s before its score onset), where the old note still carries the sound
        led_ = [(new_on(o), sec_qn(o["qn"], -0.06), o["qn"]) for o in ns
                if o.get("leg_target") and qn_to_sec(o["qn"]) - qn_to_sec(new_on(o)) > 0.08]
        def _ramp0(pts_):
            for i_ in range(1, len(pts_)):
                if abs(pts_[i_][1]) > 1e-6:
                    return (pts_[i_ - 1][0], pts_[i_][0])
            return None
        rows_ = [("LEVEL_SHAPES", _ramp0([(float(x_), float(d_)) for x_, d_ in ps_])) for ps_ in LEVEL_SHAPES.get(tname, [])]
        rows_ += [("LEVEL_SHAPES_S", _ramp0([(sec_to_qn(qn_to_sec(float(q0_)) + float(x_)), float(d_)) for x_, d_ in ps_]))
                  for q0_, ps_ in LEVEL_SHAPES_S.get(tname, [])]
        for k_, v_ in ef.items():
            if isinstance(v_, dict) and v_.get("pre_s", 0.0) > 0:
                rows_.append((f"early fill {k_:g}", (qn_before(k_, v_["pre_s"] + 0.03), qn_before(k_, v_["pre_s"]))))
            else:
                rows_.append((f"early fill {k_:g}", (k_ - 0.02, k_)))
        hits_ = []
        for nm_, r_ in rows_:
            if r_ is None or qn_to_sec(r_[1]) - qn_to_sec(r_[0]) > 0.3:
                continue   # a gradual ramp (over 0.3 s) barely moves inside a transition
            hit_ = next((x_ for x_ in led_ if r_[0] < x_[1] - EPS and r_[1] > x_[0] + EPS), None)
            if hit_ and not any(abs(hit_[2] - float(q_)) < 0.01 for q_ in LEG_RAMP_OK.get(tname, [])):
                hits_.append(f"{nm_} {r_[0]:.2f} (target {hit_[2]:g}, moved {hit_[0]:.2f})")
        if hits_:
            print(f"  WARN {tname}: {len(hits_)} level rows ramp inside a led legato transition: " + "; ".join(hits_),
                  file=sys.stderr)
    vol_parts.rule = "held_decresc"
    # mvt1 c34 (critic C #3b): HELD_DECRESC_DB (see the default): a decrescendo inside one held note falls in the volume
    # envelope from 0 at its start + 0.2 s to -dB at its end, held to the next moved onset, back to 0 by that onset
    held_decresc = []
    held_decresc_carry = []
    held_decresc_led = []   # mvt3 c26
    hd_db_ = (HELD_DECRESC_DB or {}).get(family)
    if hd_db_:
        for a_, b_, k_ in hps:
            if any(abs(a_ - x_) < 0.02 for x_ in HELD_DECRESC_SKIP.get(tname, [])):
                continue
            if k_ != "decresc" or any(a_ + 0.05 < o["qn"] < b_ - 0.05 for o in ns):
                continue   # a note starts inside the hairpin: not one held note
            if not any(o["qn"] <= a_ + 0.05 and orig_end[id(o)] >= b_ - 0.05 for o in ns):
                continue
            ta_ = sec_to_qn(qn_to_sec(a_) + 0.2)
            if qn_to_sec(b_) - qn_to_sec(a_) < HELD_DECRESC_MIN_S:
                continue   # a short swell's fall: the sample's bloom does not cancel it
            nx_ = min([new_on(o) for o in ns if o["qn"] > b_ - 0.05] + [END + 0.5])
            he_ = max(b_, nx_ - 0.03)
            nxs_ = min([o["qn"] for o in ns if o["qn"] > b_ - 0.05] + [END + 0.5])
            carry_ = None
            if HELD_DECRESC_CARRY and (any(abs(nxs_ - x_) < 0.02 for x_ in sub_soft_q)
                                       or any(abs(nxs_ - q_) < 0.02 and d_ in ("fp", "sfp") for q_, d_ in marks)):
                carry_ = next(((c0_, c1_) for c0_, c1_, ck_ in sorted(hps) if ck_ == "cresc" and nxs_ - 0.05 <= c0_
                               < nxs_ + HELD_DECRESC_CARRY["max_qn"]), None)
            if carry_:   # mvt3 c08 (C #3): held through the subito, released across the next crescendo
                vol_parts.append(("env", [(ta_, 0.0), (b_, -hd_db_), (carry_[0], -hd_db_), (carry_[1], 0.0)], True))
                held_decresc_carry.append([round(a_, 3), round(nxs_, 3), round(carry_[0], 3), round(carry_[1], 3)])
            elif HELD_DECRESC_LED_RELEASE and nx_ <= b_ + 0.01:   # mvt3 c26: the release at the led note's moved onset
                rs_ = HELD_DECRESC_LED_RELEASE.get(tname, HELD_DECRESC_LED_RELEASE.get(family, 0.25)) \
                    if isinstance(HELD_DECRESC_LED_RELEASE, dict) else 0.25
                pe_ = max([o["end"] for o in ns if o["qn"] < b_ - 0.05 and o["end"] <= nx_ + EPS] + [-1e9])
                w1_ = qn_before(nx_, 0.01)
                if w1_ - pe_ >= 0.15 and pe_ > ta_ + 0.05 and rs_ < 1.0:   # a rest before the next note: the release lies in it
                    # (0.15 qn or more: later passes still move note ends by up to about 0.1 qn)
                    vol_parts.append(("env", [(ta_, 0.0), (pe_, -hd_db_), (w1_, 0.0)], True))
                    held_decresc_led.append([round(nx_, 3), "rest"])
                else:
                    e_ = max(sec_to_qn(qn_to_sec(ta_) + 0.05), nx_)
                    vol_parts.append(("env", [(ta_, 0.0), (e_, -hd_db_), (sec_to_qn(qn_to_sec(e_) + rs_), 0.0)], True))
                    held_decresc_led.append([round(nx_, 3), rs_])
            else:
                vol_parts.append(("env", [(ta_, 0.0), (b_, -hd_db_), (he_, -hd_db_), (max(he_ + 0.01, nx_), 0.0)], True))
            held_decresc.append([round(a_, 3), round(b_, 3)])
    vol_parts.rule = "pickup"
    # mvt1 c16 (critic A #1): PICKUP_SUS level offset, exact, from the pickup's moved onset to its target's moved onset
    pickup_sus = []
    if PICKUP_SUS:
        pdb_ = PICKUP_SUS.get("level_db", {}).get(family, 0.0)
        for n in ns:
            if not n.get("pickup_sus"):
                continue
            pickup_sus.append(round(n["qn"], 3))
            if not pdb_:
                continue
            nx_ = [o for o in ns if o is not n and abs(o["qn"] - orig_end[id(n)]) <= 0.02 + EPS]
            a_ = new_on(n)
            b_ = min([new_on(o) for o in nx_] or [orig_end[id(n)]])
            if b_ - a_ < 0.03:
                continue
            vol_parts.append(("env", [(a_ - 0.012, 0.0), (a_ - 0.002, pdb_), (b_ - 0.012, pdb_), (b_ - 0.002, 0.0)], True))
    # mvt1 c17 (critic A #1): exact level lift on listed pickups (PICKUP_LIFT), moved onset to the target's moved onset
    pickup_lift = []
    for q_, d_ in sorted((float(k_), v_) for k_, v_ in PICKUP_LIFT.get(tname, {}).items()):
        pn_ = [n for n in ns if abs(n["qn"] - q_) < 0.01]
        if not pn_:
            print(f"  warning: {tname} PICKUP_LIFT {q_}: no note")
            continue
        n = max(pn_, key=lambda n_: n_["pitch"])
        nx_ = [o for o in ns if o is not n and abs(o["qn"] - orig_end[id(n)]) <= 0.02 + EPS]
        a_ = min(new_on(o) for o in pn_)
        b_ = min([new_on(o) for o in nx_] or [orig_end[id(n)]])
        if b_ - a_ < 0.03:
            continue
        tail_ = PICKUP_LIFT_TAIL_S.get(tname, PICKUP_LIFT_TAIL_S.get(family))   # mvt1 c35 (A #4)
        if tail_:
            vol_parts.append(("env", [(a_ - 0.01, 0.0), (a_, d_), (sec_qn(b_, tail_[0]), d_),
                                      (sec_qn(b_, tail_[0] + tail_[1]), 0.0)], True))
        else:
            vol_parts.append(("env", [(a_ - 0.01, 0.0), (a_, d_), (b_, d_), (b_ + 0.02, 0.0)], True))
        pickup_lift.append([round(q_, 3), d_, round(a_, 4), round(b_, 4)])
    vol_parts.rule = "synco"
    # mvt1 c17 (critic A #3): off-beat syncopated notes after a rest (SYNCO_SHAPE)
    synco_shaped = []
    if SYNCO_SHAPE and family in SYNCO_SHAPE["families"]:
        so_ = SYNCO_SHAPE
        ons_ = sorted({round(n["qn"], 4) for n in ns})
        for q_ in ons_:
            if abs((q_ % 1.0) - 0.5) > 0.01 or gate_bpm(q_) < so_["min_bpm"] - EPS or near(q_, accent_q):
                continue
            grp_ = [n for n in ns if abs(n["qn"] - q_) < EPS]
            w_ = max(orig_end[id(n)] for n in grp_) - q_
            if not (so_["len_qn"][0] - EPS <= w_ <= so_["len_qn"][1] + EPS):
                continue
            if any(o["qn"] < q_ - EPS and orig_end[id(o)] > q_ - so_["rest_qn"] + EPS for o in ns):
                continue
            si_ = slur_of(q_)
            if si_ is not None and slurs[si_][0] < q_ - EPS:
                continue
            t0_ = qn_to_sec(q_)
            e_ = q_ + w_
            nxt_ = [new_on(o) for o in ns if o["qn"] > q_ + EPS]
            pts_ = [(sec_to_qn(t0_ + so_["pts"][0][0] - 0.02), 0.0)]
            pts_ += [(sec_to_qn(t0_ + t_), d_) for t_, d_ in so_["pts"] if sec_to_qn(t0_ + t_) < e_ - 0.01]
            pts_.append((e_, so_["pts"][-1][1] if sec_to_qn(t0_ + so_["pts"][-1][0]) < e_ else pts_[-1][1]))
            r_ = sec_to_qn(qn_to_sec(e_) + 0.25)
            if nxt_:
                nx0_ = min(nxt_)
                # the next shape starts 0.02 s before its first point: end the return there
                r_ = min(r_, sec_to_qn(qn_to_sec(nx0_) - 0.02)) if nx0_ > e_ + EPS else e_ + 0.005
            pts_.append((max(r_, e_ + 0.005), 0.0))
            vol_parts.append(("env", pts_, True))
            synco_shaped.append(round(q_, 3))
    vol_parts.rule = "pair_rel"
    # mvt1 c14 (critic A #1): the release of two-note slurs (SLUR_PAIR_RELEASE)
    pair_rel = []
    if SLUR_PAIR_RELEASE and family in ("wind", "brass", "string"):
        spr_ = SLUR_PAIR_RELEASE
        by_slur_ = collections.defaultdict(list)
        for n in ns:
            if n["slur"] is not None and not n.get("grace"):
                by_slur_[n["slur"]].append(n)
        sf_on_ = [q_ for q_, d_ in marks if d_ in ("sf", "sfz")]
        for si_, sn_ in sorted(by_slur_.items()):
            ons_ = sorted({round(n["qn"], 4) for n in sn_})
            if len(ons_) != 2:
                continue
            q1_, q2_ = ons_
            n2_ = max((n for n in sn_ if abs(n["qn"] - q2_) < EPS), key=lambda n: n["pitch"])
            n1_ = max((n for n in sn_ if abs(n["qn"] - q1_) < EPS), key=lambda n: n["pitch"])
            w2_ = orig_end[id(n2_)] - q2_
            # mvt1 c16 (critic A #3): a second note joined from a tongued/bowed first note (slur_start_joins) counts
            # from 0.25 qn notes up (the first notes of those slurs are 0.25-0.6 qn)
            sj_ = any(abs(q2_ - x_) < 0.01 for x_ in slur_start_joins)
            min_ = 0.25 if sj_ and spr_.get("join_db") is not None else 0.5
            if w2_ > spr_["max_qn"] + EPS or orig_end[id(n1_)] - q1_ < min_ - EPS or w2_ < min_ - EPS:
                continue
            if near(q2_, accent_q) or near(q2_, ten_q) or near(q2_, sf_on_):
                continue
            if SHORT_ONE_LEVEL_QN is not None and w2_ <= SHORT_ONE_LEVEL_QN + EPS:
                continue   # mvt3 c16: no shape inside a note of an eighth or less
            if any(abs(h_[1] - q2_) < 0.05 for h_ in hps) or base(q2_ + 0.01) > base(q1_ + 0.01) + 0.5 \
                    or any(h_[2] == "cresc" and h_[0] < q2_ - EPS and h_[1] > q1_ + EPS for h_ in hps):
                continue
            m2_ = new_on(n2_)
            nm_ = next_moved(n2_)
            stop_ = nm_ if nm_ is not None else orig_end[id(n2_)] + 0.05
            db_ = spr_["join_db"] if sj_ and spr_.get("join_db") is not None else spr_["db"]
            ov_ = next((v_ for k_, v_ in SLUR_PAIR_RELEASE_DB_AT.get(tname, {}).items() if abs(q2_ - k_) < 0.02), None)
            if ov_ is not None:   # mvt1 c18 (A #2): a listed depth
                if ov_ >= 0:
                    continue
                db_ = ov_
            d2s_ = qn_to_sec(orig_end[id(n2_)], TEMPO_NC) - qn_to_sec(q2_, TEMPO_NC)
            if spr_.get("short_s") and d2s_ < spr_["short_s"]:
                # mvt1 c16 (critic A #3): on short notes the release starts at the moved onset (0.10 s left 0.04 s)
                a_, b_ = m2_, sec_qn(m2_, min(spr_.get("full_short_s", 0.12), 0.5 * d2s_))
            else:
                a_, b_ = sec_qn(m2_, spr_["from_s"]), sec_qn(m2_, spr_["full_s"])
            if stop_ - 0.03 <= b_ + 0.01:
                continue
            vol_parts.append(("env", [(a_, 0.0), (b_, db_), (stop_ - 0.03, db_), (stop_, 0.0)], True))
            pair_rel.append(round(q2_, 3))
    vol_parts.rule = "wind_detach"
    # mvt1 c15 (critic A #3): WIND_DETACH dips on tongued note changes with a short played gap (one per note end)
    detach_dips = []
    if WIND_DETACH and family in ("wind", "brass"):
        wd_ = dict(WIND_DETACH, **WIND_DETACH.get("by", {}).get(family, {}))
        if wd_.get("dip_db"):
            done_ = set()
            for n in ns:
                # a tongued change: the next note starts at this note's written end at a new pitch, outside its slur
                # (WIND_DETACH notes, and slur ends into a tongued note)
                nx_ = [o for o in ns if o is not n and abs(o["qn"] - orig_end[id(n)]) < 0.01]
                if not nx_ or any(o["pitch"] == n["pitch"] for o in nx_) \
                        or any(n["slur"] is not None and o.get("slur") == n["slur"] for o in nx_) or n.get("grace"):
                    continue
                nm_ = min(new_on(o) for o in nx_)
                e_ = n["end"]
                if any(o is not n and o not in nx_ and new_on(o) < nm_ - EPS and o["end"] > e_ + 0.01 for o in ns):
                    continue   # another note of the track sounds across the gap (a chord tone held on)
                if round(e_, 4) in done_ or e_ > nm_ + 0.01 or nm_ - n["qn"] < 0.1 \
                        or base(orig_end[id(n)] - 0.01) < wd_.get("dip_min_cc", 0):
                    continue
                gap_ = qn_to_sec(nm_) - qn_to_sec(e_)
                if gap_ >= WIND_DETACH_DIP_MAX_GAP_S - 1e-6:
                    continue
                done_.add(round(e_, 4))
                te_ = qn_to_sec(e_)
                pts_ = [(sec_to_qn(te_ - wd_.get("dip_fall_s", 0.05)), 0.0), (e_, wd_["dip_db"])]
                if gap_ > 0.006:
                    pts_.append((qn_before(nm_, 0.005), wd_["dip_db"]))
                pts_.append((sec_to_qn(max(qn_to_sec(nm_), te_) + 0.005), 0.0))
                vol_parts.append(("env", pts_, True))
                detach_dips.append(round(n["qn"], 3))
    vol_parts.rule = "str_rep_dip"
    # mvt1 c22 (critic A #1): STR_REP_DETACH dips before each eighth of a listed string pedal
    str_rep_dips, beat_gaps = [], []
    if STR_REP_DETACH and family == "string" and STR_REP_DETACH.get("at", {}).get(tname):
        for sp_ in STR_REP_DETACH["at"][tname]:
            a_, b_ = sp_[0], sp_[1]
            sd_ = dict(STR_REP_DETACH, **(sp_[2] if len(sp_) > 2 else {}))   # mvt1 c37 (critic A #1): per-span options
            ons_ = sorted({round(n["qn"], 4) for n in ns if a_ - EPS <= n["qn"] < b_ - EPS and not n.get("grace")})
            for q0_, q1_ in zip(ons_, ons_[1:]):
                n0_ = [n for n in ns if abs(n["qn"] - q0_) < EPS]
                n1_ = [n for n in ns if abs(n["qn"] - q1_) < EPS]
                if any(orig_end[id(n)] - n["qn"] > sd_.get("max_qn", 0.5) + EPS or abs(orig_end[id(n)] - q1_) > 0.05
                       for n in n0_):
                    continue
                if any(n["slur"] is not None and o.get("slur") == n["slur"] for n in n0_ for o in n1_):
                    continue
                if base(q0_ + 0.01) < sd_.get("min_cc", 0):
                    continue
                if sd_.get("same_pitch_only") and not any(n["pitch"] == o["pitch"] for n in n0_ for o in n1_):
                    continue
                tb_ = qn_to_sec(min(new_on(o) for o in n1_))
                d_, x_, r_, k_ = sd_["dip_db"], sd_.get("dip_s", 0.08), sd_.get("ramp_s", 0.02), sd_.get("back_s", 0.005)
                if sd_.get("frac"):
                    x_ = min(x_, sd_["frac"] * max(0.0, tb_ - qn_to_sec(min(new_on(n) for n in n0_))))
                vol_parts.append(("env", [(sec_to_qn(tb_ - x_ - r_), 0.0), (sec_to_qn(tb_ - x_), d_),
                                          (sec_to_qn(tb_ + k_), d_), (sec_to_qn(tb_ + k_ + r_), 0.0)], True))
                str_rep_dips.append(round(q1_, 3))
                # mvt3 c11 (critic A #1, S1): "beat_gap_db" (optional): before a stroke on a beat (down, mid or plain beat),
                # a further dip that lies only in the played gap (from the stroke before's note-off + 6 ms to the next
                # moved onset - 3 ms), so an up-bow off-beat stroke that swells through its note-off does not run into
                # the downbeat (basses 1056-1088: on-beat dip 2.3 dB against 12.0 off-beat, 30-120 Hz)
                bg_ = sd_.get("beat_gap_db")
                if bg_ and metric_kind(q1_) in ("down", "mid", "beat"):
                    te0_ = qn_to_sec(max(n["end"] for n in n0_))
                    if tb_ - te0_ > 0.02:
                        vol_parts.append(("env", [(sec_to_qn(te0_), 0.0), (sec_to_qn(te0_ + 0.006), bg_),
                                                  (sec_to_qn(tb_ - 0.009), bg_), (sec_to_qn(tb_ - 0.003), 0.0)], True))
                        beat_gaps.append(round(q1_, 3))
    vol_parts.rule = "mt_alt"
    # mvt1 c15 (critic A #4): the MEAS_TREM alternate-row strokes' level offset (a step per stroke)
    mt_alt_q = [round(n["qn"], 4) for n in ns if n.get("mt_alt")]
    if MEAS_TREM and MEAS_TREM.get("alt_db") and mt_alt_q:
        for n in ns:
            if not n.get("mt_alt"):
                continue
            a_ = new_on(n)
            nx_ = [new_on(o) for o in ns if o["qn"] > n["qn"] + EPS]
            b_ = min(nx_) if nx_ else orig_end[id(n)]
            vol_parts.append(("env", [(a_ - 0.012, 0.0), (a_ - 0.002, MEAS_TREM["alt_db"]),
                                      (b_ - 0.012, MEAS_TREM["alt_db"]), (b_ - 0.002, 0.0)], True))
    vol_parts.rule = "uni_fade"
    # mvt1 c15 (critic C #5): a delayed unison copy fades in under the kept note
    uni_fades = []
    if UNI_DELAY_FADE:
        for n in ns:
            dl_ = UNI_DELAY.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
            if dl_ is None:
                continue
            q1_ = max(new_on(n), dl_)
            vol_parts.append(("env", [(q1_ - 0.01, 0.0), (q1_, UNI_DELAY_FADE[0]),
                                      (sec_to_qn(qn_to_sec(q1_) + UNI_DELAY_FADE[1]), 0.0)], True))
            uni_fades.append(round(q1_, 3))
    uni_played = []   # mvt3 c08 (A #3): UNI_OUTLAST_PLAY
    for n in ns:
        ke_ = UNI_PLAY.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if ke_ is None:
            continue
        q0_ = new_on(n)
        vol_parts.append(("env", [(q0_ - 0.04, 0.0), (q0_ - 0.01, UNI_OUTLAST_PLAY["db"]), (ke_, UNI_OUTLAST_PLAY["db"]),
                                  (ke_ + UNI_OUTLAST_PLAY["ramp_qn"], 0.0)], True))
        uni_played.append(round(n["qn"], 3))
    vol_parts.rule = "arrival"
    # mvt1 c06 (C #1): arrival weight on the tracks that start a note on the arrival
    arr_w = []
    if family in ("wind", "brass", "string"):
        for qa_, aw_ in sorted(ARRIVAL_WEIGHT_AT.items()):
            pre_, db_ = aw_[0], aw_[1]
            pq_ = aw_[2] if len(aw_) > 2 else 4.0   # mvt1 c08 (critic C #1): the hold-back's length in qn (default 4)
            if not any(abs(n["qn"] - qa_) < 0.05 for n in ns):
                continue
            vol_parts.append(("env", [(qa_ - pq_, 0.0), (qa_ - 0.1, pre_), (sec_qn(qa_, 0.05), db_), (qa_ + 0.5, db_),
                                      (qa_ + 1.0, 0.0)], True))
            arr_w.append(qa_)
    vol_parts.rule = "tenuto_swell"
    # mvt1 c06 (A #3): a slurred string tenuto at f or louder joined as a legato target keeps its weight in dB
    ten_sw = []
    if family == "string" and TENUTO_SWELL_DB:
        for n in ns:
            q0, e_ = n["qn"], orig_end[id(n)]
            if near(q0, ten_q) and n.get("slur") is not None and n.get("leg_target") and base(q0) >= DYN["f"] - 2 \
                    and e_ - q0 >= 0.4:
                t1_ = sec_qn(q0, 0.05)
                vol_parts.append(("env", [(t1_, 0.0), (sec_qn(q0, 0.12), TENUTO_SWELL_DB),
                                          (max(sec_qn(q0, 0.12) + 0.01, e_ - 0.1), TENUTO_SWELL_DB),
                                          (max(sec_qn(q0, 0.12) + 0.02, e_ + 0.05), 0.0)], True))
                ten_sw.append(round(q0, 3))
    vol_parts.rule = "phrase_top"
    # c18 (C #4): phrase tops. In LEAD_SPANS, inside printed slurs of PT_MIN_NOTES or more onsets, each onset gets
    # clip(PT_DB_PER_ST x (top pitch - mean top pitch of the slur), PT_CLIP) dB, stepped at the moved onsets (0.1 qn
    # ramps), from 0.1 qn before the first moved onset to 0.1 qn after the slur's last note ends (c17: the top note was
    # the loudest in 9 of 25 lead slurs, median +1.3 dB over the others)
    pt_slurs = 0
    if tname in LEAD_SPANS and family in ("wind", "brass", "string"):
        by_slur = collections.defaultdict(list)
        for n in ns:
            if n.get("slur") is not None and not n.get("grace") \
                    and any(s_ - EPS <= n["qn"] < e_ for s_, e_ in LEAD_SPANS[tname]):
                by_slur[n["slur"]].append(n)
        for si_, sn_ in by_slur.items():
            ons_ = sorted({round(n["qn"], 3) for n in sn_})
            if len(ons_) < PT_MIN_NOTES:
                continue
            top_ = {q_: max(n["pitch"] for n in sn_ if abs(n["qn"] - q_) < 0.002) for q_ in ons_}
            mean_ = sum(top_.values()) / len(top_)
            val_ = {q_: max(PT_CLIP[0], min(PT_CLIP[1], PT_DB_PER_ST * (top_[q_] - mean_))) for q_ in ons_}
            # c22 (C #1d): onsets inside a soft lead hairpin take the printed shape, not the pitch contour (the solo
            # violin's bar 17 crescendo falls Bb5 -> Eb5: the phrase tops took 2.1 dB off it)
            val_ = {q_: (0.0 if any(a_ - EPS <= q_ <= b_ + EPS for a_, b_ in hp_soft_spans)
                         or (PT_OFF_IN_CRESC and any(k_ == "cresc" and a_ - EPS <= q_ <= b_ + EPS for a_, b_, k_ in hps))
                         else v_)
                    for q_, v_ in val_.items()}
            mov_ = {q_: min(new_on(n) for n in sn_ if abs(n["qn"] - q_) < 0.002) for q_ in ons_}
            end_ = max(orig_end[id(n)] for n in sn_)
            pts_ = [(mov_[ons_[0]] - 0.1, 0.0), (mov_[ons_[0]], val_[ons_[0]])]
            for q1_, q2_ in zip(ons_, ons_[1:]):
                m_ = max(mov_[q2_], pts_[-1][0] + 0.06)
                pts_ += [(m_ - 0.05, val_[q1_]), (m_ + 0.05, val_[q2_])]
            pts_ += [(max(end_, pts_[-1][0] + 0.01), val_[ons_[-1]]), (max(end_, pts_[-1][0] + 0.01) + 0.1, 0.0)]
            vol_parts.append(("env", pts_, True))
            pt_slurs += 1
    vol_parts.rule = "accent"
    # c09 (A #5): loud accents get weight in dB (CC11 hardly moves at the top of its range): +ACCENT_DB, 30 ms rise
    acc_n, acc_done, acc_on_arr, acc_fitted, acc_body = 0, [], [], [], []
    if family in ("wind", "brass", "string"):
        for n in ns:
            is_sf = any(abs(n["qn"] - m_) < 0.01 for m_ in sf_q) and value_at(pts, n["qn"] - 0.01) >= DYN["f"]
            gentle_ = GENTLE_ACCENT.get(family)
            if ((n["qn"] in accent_q and (base(n["qn"]) >= DYN["f"] - 4 or gentle_)) or is_sf) \
                    and not any(abs(n["qn"] - x_) < EPS for x_ in acc_done):   # c10 (C #4c): a loud sf too; once per chord
                q0 = n["qn"]
                acc_done.append(q0)
                # mvt1 c13 (critic A #2): an accent played as a legato target takes the family's "swell_s_leg" shape (held
                # through the transition sag) when one is set
                gsw_ = (gentle_.get("swell_s_leg") if gentle_ and str(n.get("art") or "").startswith("Leg") else None) \
                    or (gentle_["swell_s"] if gentle_ else None)
                ov = next((v_ for k_, v_ in ACCENT_DB_AT.get(tname, {}).items() if abs(q0 - k_) < 0.02), None)
                sw_ = next((v_ for k_, v_ in ACCENT_SWELL_S_AT.get(tname, {}).items() if abs(q0 - k_) < 0.02), None)
                fv_ = next((v_ for k_, v_ in ACCENT_FITS.get(tname, {}).items() if abs(q0 - float(k_)) < 0.02), None)
                bv_ = next((v_ for k_, v_ in ACCENT_BODIES.get(tname, {}).items() if abs(q0 - float(k_)) < 0.02), None)
                if gentle_ and bv_ is not None and float(bv_) < 0:
                    # mvt1 c18 (critic A #1): a body cut after the accent's front (ACCENT_BODY_S)
                    ln_ = max([o for o in ns if abs(o["qn"] - q0) < EPS], key=lambda o: orig_end[id(o)])
                    nm_ = next_moved(ln_)
                    stop_ = nm_ if nm_ is not None else orig_end[id(ln_)]
                    bs_ = ACCENT_BODY_S
                    if ACCENT_BODY_S_SHORT and qn_to_sec(orig_end[id(ln_)]) - qn_to_sec(q0) < ACCENT_BODY_SHORT_MAX_S:
                        bs_ = ACCENT_BODY_S_SHORT   # mvt1 c23 (critic A #1)
                    b0_, b1_ = sec_qn(q0, bs_[0]), sec_qn(q0, bs_[1])
                    if stop_ - 0.02 > b1_ + 0.01:
                        bd_ = float(bv_)
                        vol_parts.rule = "accent_body"
                        vol_parts.append(("env", [(b0_, 0.0), (b1_, bd_), (stop_ - 0.02, bd_), (stop_, 0.0)], True))
                        vol_parts.rule = "accent"
                        acc_body.append([round(q0, 3), round(bd_, 2)])
                if gentle_ and ov is None and sw_ is None and fv_ is not None:
                    # mvt1 c07 (ONE_TIME): a fitted swell (tools/fit_accents.py), the family's shape
                    ov = float(fv_[0] if isinstance(fv_, list) else fv_)
                    sw_ = gsw_
                    acc_fitted.append(round(q0, 3))
                    if ov <= 0:
                        acc_n += 1
                        continue
                elif gentle_ and ov is not None and sw_ is None:
                    sw_ = gsw_   # mvt1 c07: a per-onset level on a gentle family keeps the gentle shape
                if gentle_ and ov is None and sw_ is None:   # mvt1 c00: the family's gentle swell
                    ov = gentle_["db"] if base(q0) >= DYN["f"] - 4 else gentle_["soft_db"]
                    sw_ = gsw_
                    if ACCENT_MINUS_HPGAIN:   # mvt1 c02 (C #2): on a crescendo's arrival, only what the gain lacks
                        hg_ = max([it_[4] for it_ in vol_parts if it_[0] == "hpgain" and it_[4] > 0
                                   and it_[2] - 0.05 <= q0 <= it_[2] + 0.3], default=0.0)
                        if hg_ > 0:
                            ov = max(0.0, ov - hg_)
                            acc_on_arr.append(round(q0, 3))
                    if ov <= 0:
                        acc_n += 1
                        continue
                if ov is not None and sw_ is not None:   # c26 (item 9): a swell in seconds, no front edge
                    # mvt3 c09 (critic A #3): ACCENT_SWELL_FROM_MOVED families start the swell at the led note's moved
                    # note-on (not the score onset), so the weight lands on the attack (horn fronts were 8-10 dB duller
                    # than unaccented notes: the swell peaked 70 ms after a 90 ms lead). Legato targets keep the old start
                    sq_ = new_on(n) if (family in ACCENT_SWELL_FROM_MOVED and gentle_ and not n.get("leg_target")) else q0
                    grp_ = [o for o in ns if abs(o["qn"] - q0) < EPS]
                    lna_ = max(grp_, key=lambda o: orig_end[id(o)])
                    if gentle_ and ACCENT_CAP_DB is not None and not is_sf:
                        ov = min(ov, ACCENT_CAP_DB)   # mvt3 c16 (A #2, C #1)
                    if gentle_ and ACCENT_SHORT_FLAT_QN is not None and orig_end[id(lna_)] - q0 <= ACCENT_SHORT_FLAT_QN + EPS:
                        # mvt3 c16: a note of an eighth or less takes one level, no shape inside
                        vol_parts.append(("env", step_env(min(grp_, key=new_on), round(ACCENT_SHORT_FLAT_SHARE * ov, 2)), True))
                    elif gentle_ and family in ACCENT_FRONT:
                        # mvt3 c16 (A #2): front-weighted: up over sw_[0] from the moved note-on (legato target: the
                        # score onset), held to score onset + sw_[1], gone by score onset + sw_[2], the next moved
                        # note-on - 0.01 s or the note's end, whichever is first
                        sq_ = q0 if n.get("leg_target") else min(new_on(o) for o in grp_)
                        nma_ = next_moved(lna_)
                        te_ = min(qn_to_sec(q0) + sw_[2], qn_to_sec(orig_end[id(lna_)]),
                                  qn_to_sec(nma_) - 0.01 if nma_ is not None else 1e9)
                        tr_ = qn_to_sec(sq_) + sw_[0]
                        tp_ = max(tr_ + 0.005, min(qn_to_sec(q0) + sw_[1], te_ - 0.03))
                        te_ = max(te_, tp_ + 0.02)
                        vol_parts.append(("env", [(qn_before(sq_, 0.01), 0.0), (sec_to_qn(tr_), ov), (sec_to_qn(tp_), ov),
                                                  (sec_to_qn(te_), 0.0)], True))
                    else:
                        vol_parts.append(("env", [(sq_ - 0.01, 0.0), (sec_qn(sq_, sw_[0]), ov), (sec_qn(sq_, sw_[1]), ov),
                                                  (sec_qn(sq_, sw_[2]), 0.0)], True))
                elif ov is not None:   # c11 (A #3)
                    vol_parts.append(("env", [(q0 - 0.01, 0.0), (q0 + 0.01 * bpm_at(q0) / 60, ov), (q0 + 0.12, ov),
                                              (q0 + 0.3, 0.0)], True))
                else:
                    vol_parts.append(("env", [(q0 - 0.02, 0.0), (sec_qn(q0, 0.03), ACCENT_DB), (sec_qn(q0, 0.25), ACCENT_DB),
                                              (sec_qn(q0, 0.5), 0.0)]))
                acc_n += 1
    vol_parts.rule = "marc"
    for n in ns:   # c14: marcato body and attack weight (exact breakpoints)
        if n.get("marc"):
            q0, e_ = n["qn"], n["end"]
            t1, t2, t3 = (sec_qn(q0, t_) for t_ in MARC_ATTACK_S)   # c15 (A #4)
            t3 = min(t3, e_ - 0.01)
            vol_parts.append(("env", [(q0 - 0.01, 0.0), (q0 + 0.01 * bpm_at(q0) / 60, MARC_BODY_DB),
                                      (t1, MARC_BODY_DB + MARC_ATTACK_DB), (t2, MARC_BODY_DB + MARC_ATTACK_DB),
                                      (t3, MARC_BODY_DB), (e_, MARC_BODY_DB), (e_ + 0.05, 0.0)], True))
    vol_parts.rule = "note_trim"
    # c03 (B #4): note trims keyed by onset (qn), matched within 0.02 qn, no length cutoff
    nt = {float(k): v for k, v in NOTE_TRIMS.get(tname, {}).items() if not k.startswith("_")}
    acc_trim_q = []   # mvt1 c07 (ONE_TIME): fitted accent trims, as step note trims (added to any listed trim)
    if family in GENTLE_ACCENT:
        for k_, v_ in ACCENT_FITS.get(tname, {}).items():
            if isinstance(v_, list) and len(v_) > 1 and v_[1]:
                kq_ = next((x_ for x_ in nt if abs(x_ - float(k_)) < 0.02), float(k_))
                nt[kq_] = nt.get(kq_, 0.0) + float(v_[1])
                acc_trim_q.append(kq_)
    nt_pluck_done = set()
    for n in ns:
        hit = [v for k, v in nt.items() if abs(n["qn"] - k) < 0.02]
        if hit and (family in ("harp", "harm") or "izz" in (n.get("art") or "")):   # c24 (B #3): harmonics too
            # c21 (B #5): a plucked note trim is a step at full value on the attack (the c12 pizz. pitch-trim shape;
            # the 0.6 s ramp missed the pluck), held to the next onset (at most 1.5 s), once per onset (a chord counts once)
            if round(n["qn"], 3) in nt_pluck_done:
                continue
            nt_pluck_done.add(round(n["qn"], 3))
            q0, v_ = new_on(n), hit[0]
            nx_ = [new_on(o) for o in ns if o["qn"] > n["qn"] + EPS]
            ne_ = min(min(nx_) if nx_ else 1e9, sec_qn(n["qn"], 1.5))
            vol_parts.append(("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
                                      (max(qn_before(q0, 0.01) + 0.002, qn_before(ne_, 0.03)), v_),
                                      (max(qn_before(q0, 0.01) + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
            continue
        if hit:
            # mvt1 c08: once per onset (the track's envelope is shared: a trim on a 2-note chord applied twice); the
            # longest note at the onset carries it
            if round(n["qn"], 3) in nt_pluck_done:
                continue
            nt_pluck_done.add(round(n["qn"], 3))
            n = max([o for o in ns if abs(o["qn"] - n["qn"]) < EPS], key=lambda o: orig_end[id(o)])
            if SHORT_ONE_LEVEL_QN is not None and orig_end[id(n)] - n["qn"] <= SHORT_ONE_LEVEL_QN + EPS \
                    and not isinstance(hit[0], dict):
                vol_parts.append(("env", step_env(min((o for o in ns if abs(o["qn"] - n["qn"]) < EPS), key=new_on), hit[0]), True))
                continue   # mvt3 c16: one level per short note
            sec = qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"])
            rs_ = next((v_ for k_, v_ in NOTE_TRIM_RAMP_S.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02),
                       0.1 if any(abs(n["qn"] - k_) < 0.02 for k_ in acc_trim_q) else 0.6)
            ramp = rs_ * (orig_end[id(n)] - n["qn"]) / sec   # 0.6 s in qn (c24: per-onset NOTE_TRIM_RAMP_S)
            vol_parts.append(("env", trim_shape(n, hit[0], ramp,   # c09 (A #2): ends at the next moved onset
                                                tgt_trim=lambda o: next((v_ for k_, v_ in nt.items() if abs(o["qn"] - k_) < 0.02), 0.0))))
    vol_parts.rule = "row_trim"
    # mvt1 c07 (critic A #1): ROW_TRIM_DB. In a line that mixes rows, loud Sus MAX / Stac notes sat 2-6 dB over the Leg
    # rows at the same CC11 (Violins II +4.7, Violas +5.6 median), so accented Leg notes sat under the Sus eighths after
    # them. Consecutive trimmed notes are one step (no bump at each join); accented notes on the row are trimmed too
    # (their swell stays on top), so an accent keeps its relation to the Sus notes around it
    row_trimmed = []
    rtab_ = ROW_TRIM_DB.get(tname, {}) if family == "string" else {}
    if rtab_:
        segs_ = []
        for n in sorted(ns, key=lambda o: o["qn"]):
            a_ = n.get("art") or ""
            # mvt3 c14: ROW_TRIM_STROKES = {track: [score qn]}: listed DOWNBOW_STROKE_AT strokes that stand inside a line
            # (a legato-row note turned into a stroke) take the row trim like the notes around them and count as the
            # Leg-row neighbour of those notes, so the line's levels stay as they were with the legato note
            rts_ = ROW_TRIM_STROKES.get(tname, [])
            lst_ = any(abs(n["qn"] - k_) < 0.02 for k_ in rts_)
            if a_ not in rtab_ or (n.get("down_stroke") and not n.get("rep_stroke") and not lst_) or n.get("rep_sus") or n.get("rep_stac") \
                    or any(a0_ - EPS <= n["qn"] < b0_ for a0_, b0_ in ROW_TRIM_SKIP.get(tname, [])) \
                    or any(o is not n and abs(o["qn"] - n["qn"]) < 0.01 for o in ns) or final(n["qn"]) < rtab_[a_][1] \
                    or (AUTO_REBOW and qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"]) > REBOW_MAX_S) \
                    or not (lst_ or any(o is not n and (_lg((o.get("art") or "")) or any(abs(o["qn"] - k_) < 0.02 for k_ in rts_))
                                        and max(o["qn"] - orig_end[id(n)], n["qn"] - orig_end[id(o)]) <= ROW_TRIM_NEAR_QN + EPS
                                        for o in ns)):
                continue
            s0_ = new_on(n)
            nm_ = next_moved(n)
            s1_ = nm_ if nm_ is not None else orig_end[id(n)]
            nxo_ = [o for o in ns if o is not n and -EPS < o["qn"] - orig_end[id(n)] < 0.1 and o["qn"] > n["qn"] + EPS]
            nxo_ = min(nxo_, key=new_on) if nxo_ else None
            if segs_ and abs(segs_[-1][2] - rtab_[a_][0]) < 1e-6 and s0_ <= segs_[-1][1] + 0.06:
                if s1_ >= segs_[-1][1]:
                    segs_[-1][1], segs_[-1][4] = s1_, nxo_
            else:
                segs_.append([s0_, s1_, rtab_[a_][0], n, nxo_])
            row_trimmed.append(round(n["qn"], 3))
        if ROW_TRIM_HOLD_QN is not None and segs_:
            # mvt3 c16 (coordinator, from the scherzo's c15 critics): trimmed notes separated by a gap of at most
            # ROW_TRIM_HOLD_QN are one chain: the level is held across the gap and steps from one row's value to the
            # next (it fell back to 0 dB between the detached notes of a run: 4-5 dB up and down in every gap)
            chains_ = [[segs_[0]]]
            for sg_ in segs_[1:]:
                if sg_[0] - chains_[-1][-1][1] <= ROW_TRIM_HOLD_QN + EPS:
                    chains_[-1].append(sg_)
                else:
                    chains_.append([sg_])
            for ch_ in chains_:
                a0_, a1_ = lvl_step(ch_[0][3])
                pts_ = [(a0_, 0.0), (a1_, ch_[0][2])]
                for pv_, sg_ in zip(ch_, ch_[1:]):
                    if abs(sg_[2] - pv_[2]) > 1e-6:
                        x0_, x1_ = lvl_step(sg_[3])
                        x0_ = max(x0_, pts_[-1][0] + 0.002)
                        pts_ += [(x0_, pv_[2]), (max(x1_, x0_ + 0.002), sg_[2])]
                s1_, nx0_ = ch_[-1][1], ch_[-1][4]
                e0_, e1_ = lvl_step(nx0_) if nx0_ is not None else (s1_ - 0.05, s1_ + 0.03)
                pts_ += [(max(pts_[-1][0] + 0.002, e0_), ch_[-1][2]), (max(pts_[-1][0] + 0.004, e1_), 0.0)]
                vol_parts.append(("env", pts_, True))
            segs_ = []
        for s0_, s1_, d_, n0_, nx0_ in segs_:
            if LEVEL_STEP_AT_SCORE:   # mvt3 c16: both edges are level steps between notes
                a0_, a1_ = lvl_step(n0_)
                e0_, e1_ = lvl_step(nx0_) if nx0_ is not None else (s1_ - 0.05, s1_ + 0.03)
                vol_parts.append(("env", [(a0_, 0.0), (a1_, d_), (max(a1_ + 0.002, e0_), d_), (max(a1_ + 0.004, e1_), 0.0)], True))
            else:
                vol_parts.append(("env", [(s0_ - 0.03, 0.0), (s0_ + 0.03, d_), (max(s0_ + 0.04, s1_ - 0.05), d_),
                                          (max(s0_ + 0.05, s1_ + 0.03), 0.0)], True))
    vol_parts.rule = "bloomv"
    # c04 (C #5): a soft string note that re-attacks on Leg Slur MAX after a short gap and lasts 2 qn or more swells in the
    # sample (Vln II qn 220: +14 dB at a flat CC11); level only: 0 dB at the onset to -4.5 dB at 2 qn, held
    bloomv, bloomv_skip = 0, []
    if family == "string":
        for n in ns:
            q0, e = n["qn"], orig_end[id(n)]
            if n.get("art") != "Leg Slur MAX" or n.get("leg_target") or base(q0) > DYN["p"] + 2 or e - q0 < 2:
                continue
            if any(k_ == "cresc" and abs(b_ - q0) < 0.1 for a_, b_, k_ in hps):
                continue   # c10 (C #5): a crescendo's arrival note decays rather than blooms (coda qn 286, Vc/Vla -5..-11 dB)
            if any(o["qn"] < q0 - EPS and q0 - 0.3 <= orig_end[id(o)] <= q0 + EPS for o in ns):
                if joined_next(n):
                    bloomv_skip.append(round(q0, 3))   # c13 (A #2): its -4.5 dB ramp ended exactly on the join
                    continue
                vol_parts.append(("bloomv", q0, e))
                bloomv += 1
    vol_parts.rule = "uni_boost"
    for n in ns:   # c04 (A #2): the kept note of a same-patch unison
        b_ = UNI_BOOST.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if b_ and UNI_BOOST_HOLD_QN is None:
            vol_parts.append(("note", n["qn"], orig_end[id(n)], b_, 0.02))
    if UNI_BOOST_HOLD_QN is not None:
        # mvt3 c16 (critic B #4): one level per doubled phrase (see the default)
        vol_parts.rule = "uni_hold"
        uni_hold_rest = []   # mvt3 c26
        ub_ = [(n, UNI_BOOST.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))) for n in sorted(ns, key=lambda o: (o["qn"], o["pitch"]))]
        ugr_ = []
        for n, b_ in ub_:
            if not b_:
                continue
            if ugr_ and n["qn"] - ugr_[-1]["end"] <= UNI_BOOST_HOLD_QN + EPS:
                ugr_[-1]["end"] = max(ugr_[-1]["end"], orig_end[id(n)])
                ugr_[-1]["rows"].append((n, b_))
            else:
                ugr_.append({"end": orig_end[id(n)], "rows": [(n, b_)]})
        if UNI_BOOST_MIN_QN is not None:   # mvt3 c17
            ugr_ = [g_ for g_ in ugr_ if g_["end"] - g_["rows"][0][0]["qn"] >= UNI_BOOST_MIN_QN - EPS]
        if UNI_BOOST_ONE_LEVEL:
            for g_ in ugr_:
                w_ = [(max(0.05, orig_end[id(r_[0])] - r_[0]["qn"]), r_[1]) for r_ in g_["rows"]]
                lv_ = round(2 * sum(a_ * b_ for a_, b_ in w_) / sum(a_ for a_, _ in w_)) / 2
                g_["rows"] = [(r_[0], lv_) for r_ in g_["rows"]]
        for g_ in ugr_:
            n0_, b0_ = g_["rows"][0]
            if len({round(r_[0]["qn"], 3) for r_ in g_["rows"]}) == 1 and g_["end"] - n0_["qn"] < 0.5 - EPS:
                b0_ = round(0.5 * b0_, 2)
                g_["rows"] = [(n0_, b0_)]
            m0_ = min(new_on(r_[0]) for r_ in g_["rows"] if abs(r_[0]["qn"] - n0_["qn"]) < EPS)
            pts_, cur_, lastq_ = [(m0_ - UNI_BOOST_RAMP_QN, 0.0), (m0_ - 0.02, b0_)], b0_, n0_["qn"]
            for n, b_ in g_["rows"][1:]:
                if abs(b_ - cur_) > 0.01 and n["qn"] > lastq_ + EPS:
                    a0_, a1_ = lvl_step(n)
                    a0_ = max(a0_, pts_[-1][0] + 0.001)
                    pts_ += [(a0_, cur_), (max(a1_, a0_ + 0.001), b_)]
                    cur_ = b_
                lastq_ = max(lastq_, n["qn"])
            e_ = max(g_["end"], pts_[-1][0] + 0.01)
            nxg_ = [o for o in ns if abs(o["qn"] - g_["end"]) < 0.02]
            m_ = min([new_on(o) for o in nxg_] or [e_ + 1.0])
            if UNI_HOLD_END_REST and m_ < e_ + UNI_BOOST_RAMP_QN and m_ > pts_[-1][0] + 0.02:   # mvt3 c26: see the default
                pe_ = max([o["end"] for o in ns if o["qn"] < g_["end"] - 0.02 and o["end"] <= m_ + EPS] + [pts_[-1][0] + 0.005])
                w1_ = qn_before(m_, 0.01)
                w0_ = max(pe_, qn_before(m_, 0.25), pts_[-1][0] + 0.005)
                if w1_ - w0_ < 0.01:
                    w0_ = max(pts_[-1][0] + 0.005, qn_before(m_, 0.03))
                pts_ += [(w0_, cur_), (max(w0_ + 0.002, w1_), 0.0)]
                uni_hold_rest.append([round(g_["end"], 3), round(w0_, 4), round(w1_, 4)])
            else:
                pts_ += [(e_, cur_), (e_ + UNI_BOOST_RAMP_QN, 0.0)]
            vol_parts.append(("env", pts_, True))
    vol_parts.rule = "chord"
    # c03 (B #2): divisi chords and double stops play a full-section sample per note. Where k >= 2 notes sound together:
    # -10 log10(k) dB under "div.", -1.5 dB otherwise (non div. double stops); 2-note tremolo chords a further -3 dB.
    # The cut starts 0.1 qn before the chord.
    chord_segs = []
    if family == "string":
        def div_state(q):
            st = None
            for tq, t in sorted(texts_until(staves, q)):
                if META_DB and ("metà" in t or has(t, "meta") or (SOLI_AS_META and re.search(r"(?<![a-z])soli\b", t))):
                    st = "half"   # mvt1 c05 (A #5): half the section plays; mvt3 port: "4 soli" reads like "metà" (mvt2 c27)
                elif LAST_DESK_DB is not None and re.search(r"last (\d+ )?desks?\b", t):
                    st = "desk_div" if has(t, "div.") else "desk"   # mvt3 c01 (A #4)
                elif st in ("desk", "desk_div") and (has(t, "tutti") or has(t, "ord.")):
                    st = None
                elif "non div" in t:
                    st = "non"
                elif has(t, "div."):
                    st = "div"
                elif has(t, "unis"):
                    st = None
                elif st == "half" and has(t, "tutti"):
                    st = None
            return st
        bnds = sorted({round(n["qn"], 4) for n in ns} | {round(orig_end[id(n)], 4) for n in ns}
                      | {round(x, 4) for o in split_away for x in (o["qn"], o["end"])})   # c13 (A #1)
        for a_, b_ in zip(bnds, bnds[1:]):
            mid = (a_ + b_) / 2
            snd = [n for n in ns if n["qn"] <= mid < orig_end[id(n)]]
            k = len(snd) + sum(1 for o in split_away if o["qn"] <= mid < o["end"])   # c13 (A #1)
            rg_ = ROW_GAIN_DB.get(tname, {})   # mvt3 c01 (B #2): a row's own level offset
            rgv = rg_.get(snd[0].get("art"), 0.0) if rg_ and snd and all(n.get("art") == snd[0].get("art") for n in snd) else 0.0
            if not CHORD_CUTS:   # mvt3 c16: only the printed player-count marks ("meta", "last N desks") stay
                rgv = 0.0
            dst_ = div_state(mid)
            if k < 2:
                if k == 1 and META_DB and dst_ == "half":
                    chord_segs.append((a_, b_, META_DB + rgv))   # mvt1 c05 (A #5): "metà", one note by half the section
                elif k == 1 and dst_ in ("desk", "desk_div"):
                    chord_segs.append((a_, b_, LAST_DESK_DB + rgv))   # mvt3 c01 (A #4): "last N desks"
                elif k == 1 and rgv:
                    chord_segs.append((a_, b_, rgv))
                continue
            dbv = -10 * __import__("math").log10(k) if dst_ in ("div", "desk_div") else -1.5
            if dst_ == "half":
                dbv = META_DB - 10 * __import__("math").log10(k)
            if not CHORD_CUTS:   # mvt3 c16: no cut by the number of notes sounding, no tremolo-chord cut
                dbv = META_DB if dst_ == "half" else (LAST_DESK_DB if dst_ in ("desk", "desk_div") else 0.0)
                if not dbv:
                    continue
                chord_segs.append((a_, b_, dbv))
                continue
            if dst_ in ("desk", "desk_div"):
                dbv += LAST_DESK_DB
            if all(n.get("art") == "Tremolo" for n in snd):
                dbv -= 3
            chord_segs.append((a_, b_, dbv + rgv))
        if chord_segs:
            vol_parts.append(("chord",))
    seg_rest = []   # mvt3 c26 (CHORD_SEG_EDGE_REST): [(w0, w1, a)] edges moved into the rest before a led note
    if CHORD_SEG_EDGE_REST and chord_segs:
        cs_ = sorted(chord_segs)
        add_ = []
        for i_, (a_, b_, d_) in enumerate(cs_):
            prev_d_ = cs_[i_ - 1][2] if i_ and abs(cs_[i_ - 1][1] - a_) < EPS else 0.0
            if abs(prev_d_ - d_) < 0.01:
                continue
            on_ = [o for o in ns if abs(o["qn"] - a_) < EPS]
            if not on_:
                continue
            m_ = min(new_on(o) for o in on_)
            if m_ > a_ - 0.01:
                continue   # not led: the c10 edge stays
            pe_ = max([o["end"] for o in ns if o["qn"] < a_ - EPS] + [-1e9])
            w1_ = qn_before(m_, 0.02)
            w0_ = max(pe_, qn_before(m_, 0.15))
            if w1_ - w0_ < 0.01:
                continue   # no rest before the led note
            add_.append((w1_, a_, d_))
            seg_rest.append((w0_, w1_, a_))
        chord_segs = sorted(cs_ + add_)

    def seg_db(q):
        return next((d_ for a_, b_, d_ in chord_segs if a_ - EPS <= q < b_ - EPS), 0.0)

    def chord_db(q):
        # c10 (C #4b): at a printed sf the new chord's cut (divisi / tremolo chord) starts at the sf, not 0.1 qn before
        # it (the held note before the sf fell 3-6 dB ahead of the attack)
        for m_ in sf_q:
            if m_ - 0.1 <= q < m_:
                return seg_db(q)
        for w0_, w1_, a_ in seg_rest:   # mvt3 c26: the step lies in [w0, w1] (exact breakpoints), no look-ahead
            if w0_ - 0.1 - EPS <= q < w1_:
                return seg_db(q)
        return min(seg_db(q), seg_db(q + 0.1))
    vol_parts.rule = "fade"
    if ns and max(orig_end[id(n)] for n in ns) >= END - 0.01:
        vol_parts.append(("fade",))
    ring_pts = None   # mvt3 c08 (A #1): FINAL_RING
    if FINAL_RING and family in FINAL_RING["families"] and any(
            n["qn"] <= FINAL_RING["at"] + 0.01 and orig_end[id(n)] >= FINAL_RING["end"] - 0.01 for n in ns):
        re_ = float(FINAL_RING["end"])
        ring_pts = [(re_, 0.0)] + [(round(sec_to_qn(qn_to_sec(re_) + float(x_)), 4), float(d_)) for x_, d_ in FINAL_RING["pts"]]
    vbreaks = [0.0, SE - 1, SE - 0.5, SE] + ([x for x, _ in ring_pts] if ring_pts else [])
    for item in vol_parts:
        if item[0] == "settle":
            vbreaks += [item[1], item[1] + 3, max(item[2] + 0.5, item[3] - 0.05)]
        elif item[0] == "span":
            vbreaks += [item[1] - 0.5, item[1], item[2], item[2] + 0.5] + ([item[2] - item[4]] if item[4] else [])
        elif item[0] == "hpgain":
            vbreaks += [item[1], item[2], item[3], item[3] + HP_REL] + ([item[7], item[7] + HP_REL] if len(item) > 8 and item[7] else [])
        elif item[0] == "swell_db":
            vbreaks += [item[1], item[2]] + [item[1] + f_ * (item[2] - item[1]) for f_ in (0.2, 0.4, 0.6, 0.8, 0.9)]
        elif item[0] == "note":
            vbreaks += [item[1], item[1] + item[4], item[2], item[2] + 0.1]
        elif item[0] == "flat":
            vbreaks += [item[1] - 0.05, item[2]]
        elif item[0] == "bloomv":
            vbreaks += [item[1], item[1] + 2, item[2], item[2] + 0.1]
        elif item[0] == "env":
            vbreaks += [x for x, _ in item[1]]
    vbreaks += [x for a_, b_, _ in chord_segs for x in (a_ - 0.1, a_, b_)]
    vbreaks += [x for w0_, w1_, _ in seg_rest for x in (w0_, w1_)]   # mvt3 c26
    vbreaks += [x for m_ in sf_q for x in (m_ - 0.1, m_ - 0.001, m_)] if chord_segs else []
    vgrid = sorted(set([round(x, 4) for x in vbreaks] + [round(i * 0.25, 4) for i in range(int((END + 4) / 0.25))]))
    # c10: "env" items flagged exact put their breakpoints into parts.json vol_bp; build_reaper.py adds them to the volume
    # envelope's 0.125 qn grid, so shapes faster than the grid (pre-onset fills, the timpani attack) are written as built
    vol_bp = sorted({round(x, 4) for item in vol_parts if item[0] == "env" and len(item) > 2 and item[2]
                     for x, _ in item[1]})
    # mvt1 c42: POST_SHAPES_S (see the default), converted on the real tempo map
    vol_post = []
    for q0_, ps_ in POST_SHAPES_S.get(tname, []):
        t0_ = qn_to_sec(float(q0_))
        vol_post.append([[round(sec_to_qn(t0_ + float(x_)), 4), float(d_)] for x_, d_ in ps_])
    vol_bp = sorted(set(vol_bp) | {p_[0] for sh_ in vol_post for p_ in sh_})
    if ring_pts:
        vol_bp = sorted(set(vol_bp) | {round(x, 4) for x, _ in ring_pts})
    vol_db, last = [], None
    if __import__("os").environ.get("STP_DEBUG_VOL", "").split(":")[0] == tname:   # debug: per-item dB at listed qn
        for q_ in [float(x) for x in __import__("os").environ["STP_DEBUG_VOL"].split(":")[1].split(",")]:
            for it_ in vol_parts:
                saved_ = vol_parts[:]
                vol_parts[:] = [it_]
                d_ = vol(q_)
                vol_parts[:] = saved_
                if abs(d_) > 0.005:
                    print(f"  DBG {tname} {q_}: {d_:+.2f} {str(it_)[:90]}", file=sys.stderr)
    # c26 (A #1, small): after the last release (END) every track holds its level at the release, so the roles and
    # trims that end at END no longer lift the hall tail (Vln I/Vc -16 -> -10 dB over 0.5 qn, Cb -17 -> -11.6 in 0.1 qn)
    v_end_ = vol(END - 0.001) if ("fade",) in vol_parts else None
    def _vol_out(q):
        v = round(vol(q) if v_end_ is None or q < END else v_end_, 2)
        if ring_pts and q >= ring_pts[0][0]:   # mvt3 c08: FINAL_RING fall from the level at "end"
            v0_ = v_end_ if v_end_ is not None else vol(ring_pts[0][0] - 0.001)
            v = round(v0_ + (value_at(ring_pts, q) if q < ring_pts[-1][0] else ring_pts[-1][1]), 2)
        return v
    if VOL_LIN:
        # mvt3 c16: a piecewise-linear lane. Every item is linear between the breakpoints in vgrid; a step at a grid
        # point gets a second point 0.001 qn before it. Points equal to both neighbours are dropped
        raw_, pq_ = [], None
        for q in vgrid:
            v = _vol_out(q)
            if pq_ is not None and q - pq_ > 0.002:
                vb_ = _vol_out(q - 0.001)
                if abs(vb_ - v) > 0.05 and abs(vb_ - (raw_[-1][1] + (v - raw_[-1][1]) * (q - 0.001 - pq_) / (q - pq_))) > 0.05:
                    raw_.append((round(q - 0.001, 4), vb_))
            raw_.append((q, v)); pq_ = q
        vol_db = [p_ for i_, p_ in enumerate(raw_) if i_ in (0, len(raw_) - 1) or p_[1] != raw_[i_ - 1][1] or p_[1] != raw_[i_ + 1][1]]
    else:
        for q in vgrid:
            v = _vol_out(q)
            if v != last:
                vol_db.append((q, v)); last = v
    cc15 = []
    if family == "string" or (family == "brass" and stem.startswith("1FH")):   # c02: Horn 3 con sord. on the 1FH ConSordino script
        state = None
        # c05 (A #3): Horns 3-4 share a staff; Horn 4's own "con sord." is a part-only tag that mockup.ly removes
        sord_staves = staves + (["Hn3"] if tname == "Horn 4" else [])
        for q in sorted({0.0} | {tq for tq, _ in texts_until(sord_staves, END)}):
            s = text_state(q, ["con sord", "gli altri con sord"], ["senza sord"], sord_staves)
            if s != state:
                nxt = min([n["qn"] for n in ns if n["qn"] >= q - EPS], default=q)
                cc15.append((round(max(0.0, min(early_time(nxt), shifted_on(nxt) - 0.03)), 4) if q > 0 else 0.0, 127 if s else 0)); state = s
        if family == "brass" and len(cc15) <= 1 and not (cc15 and cc15[0][1]):
            cc15 = []
        # c10 (A #1): two changes at the same time keep the last (Violins I rests until qn 65, so its senza at 48 and con
        # sord. at 65 both fell at qn 0); a windowed solo track keeps no mute change after its window (its last note
        # sounds to the window's end, where the section's "gli altri con sord." applies to the others)
        cc15 = [c for i, c in enumerate(cc15) if i + 1 == len(cc15) or abs(cc15[i + 1][0] - c[0]) > EPS]
        if tname in TRACK_WINDOWS and tw_spans(tname)[1]:
            cc15 = [c for c in cc15 if c[0] < max(b for a, b in tw_spans(tname)[0]) - 0.5]
    # c02: finger position (CC70) for "sul D/G/C" (FP4 keeps the line on the lower string) and "sul A" (FP1 up to
    # MIDI 74, FP4 above); HO manual pp. 92-95. Ends at "ord." or a later "unis." without a new "sul".
    cc70 = []
    sul_notes = []   # mvt1 c38: (score qn, pitch, printed string, CC70, string played)
    if family == "string" and not stem.startswith("Basses"):
        def sul_state(q):
            for a_, b_, s_ in SUL_SPANS.get(tname, []):   # mvt1 c38 (critic C #3): printed spans from the config
                if a_ - EPS <= q < b_ + EPS:
                    return s_
            st = None
            for tq, t in sorted(texts_until(staves, q)):
                m = re.search(r"sul ([dgca])\b", t)
                if m:
                    st = m.group(1)
                elif has(t, "ord.") or has(t, "unis."):
                    st = None
            return st
        fpt_ = fp_strings(patch) if SUL_FP_FROM_PATCH else None
        if fpt_ is None:
            last = 0
            for n in ns:
                st = sul_state(n["qn"])
                val = 0 if st is None else (127 if st in "dgc" else (20 if n["pitch"] <= 74 else 127))
                if val != last:
                    cc70.append((round(max(0.0, min(early_time(n["qn"]), new_on(n) - 0.03)), 4), val)); last = val
        else:
            # mvt1 c38 (critic C #3): the CC70 value that puts each note on the printed string, from the patch's own
            # finger-position table (the Sus MAX row's CC70 start-mode ranges and each sample's string tag S1-S4); a
            # note the printed string cannot play takes the nearest string. Outside the spans the lane holds
            # SUL_DEFAULT_CC70; the lane starts with it in the pre-roll whenever any span is printed
            strings_ = {"c": 1, "g": 2, "d": 3, "a": 4} if stem.startswith(("Violas", "Celli")) else {"g": 1, "d": 2, "a": 3, "e": 4}
            fpv_ = (20, 55, 90, 120)   # the FingerPosition script's own CC70 value per FP (read from FingerPosition.osb)
            if SUL_FP4_CC70 is not None:   # mvt1 c39: see SUL_FP4_CC70
                fpv_ = fpv_[:3] + (SUL_FP4_CC70,)
            last = SUL_DEFAULT_CC70
            for n in ns:
                st = sul_state(n["qn"])
                if st is None:
                    val = SUL_DEFAULT_CC70
                else:
                    want_ = strings_.get(st, 1)
                    row_ = fpt_.get(n["pitch"])
                    if not row_:
                        val = last
                    else:
                        best_ = min(range(4), key=lambda i_: (abs(row_[i_] - want_), abs(fpv_[i_] - last), -i_))
                        val = fpv_[best_]
                        sul_notes.append((round(n["qn"], 3), n["pitch"], st, val, row_[best_]))
                    if not cc70:   # the lane is explicit from the pre-roll on (its first value is sent there)
                        cc70.append((0.0, val if n["qn"] < 0.5 else SUL_DEFAULT_CC70))
                        last = cc70[-1][1]
                if val != last:
                    cc70.append((round(max(0.0, min(early_time(n["qn"]), new_on(n) - 0.03)), 4), val)); last = val
            # two values at one tick arrive in no guaranteed order (c35): keep the later one
            cc70 = [c for i, c in enumerate(cc70) if i + 1 == len(cc70) or abs(cc70[i + 1][0] - c[0]) > EPS]

    # mvt1 c14 (critic A #2): CC36 round-robin resets at the measured-tremolo run starts (MEAS_TREM "rr_runs")
    cc36 = [(round(max(0.0, new_on(n) - 0.02), 4), 127) for n in ns if n.get("rr_start")]
    cc16 = []   # mvt3 c08: RR_RESET_AT
    for q_ in RR_RESET_AT.get(tname, []):
        at_ = [new_on(n) for n in ns if abs(n["qn"] - float(q_)) < 0.01]
        if not at_:
            print(f"  warning: {tname} RR_RESET_AT {q_}: no note", file=sys.stderr)
            continue
        cc16.append((round(max(0.0, min(at_) - 0.02), 4), 127))
    rr_all_t = []   # the reset times that belong to RR_RESET_ALL_AT points (for RR_RESET_KS_RESTATE)
    if family not in RR_RESET_ALL_SKIP:   # mvt3 c14: RR_RESET_ALL_AT
        for q_ in RR_RESET_ALL_AT:
            after_ = [n for n in ns if n["qn"] >= float(q_) - 0.01]
            if not after_:
                continue
            f_ = min(n["qn"] for n in after_)
            t_ = round(max(0.0, min(new_on(n) for n in after_ if n["qn"] <= f_ + 0.01) - 0.02), 4)
            near_ = [c_[0] for c_ in cc16 if abs(t_ - c_[0]) < 0.011]
            if not near_:
                cc16.append((t_, 127))
            if near_[:1] != [None] and (near_[0] if near_ else t_) not in rr_all_t:
                rr_all_t.append(near_[0] if near_ else t_)

    # mvt3 c15 (mvt1 c54): STEADY_LINE "rr_reset": a round-robin reset before each note of a span that follows a rest
    for n in ns:
        if n.get("steady_reset"):
            t_ = round(max(0.0, new_on(n) - 0.02), 4)
            if not any(abs(t_ - c_[0]) < 0.011 for c_ in cc16):
                cc16.append((t_, 127))

    # c03: apply the note-start leads. A note that overlaps a moved legato target ends LEG_OVERLAP after its new onset;
    # keyswitches stay at least 0.03 qn before their (moved) note.
    out_notes = []
    dropped = 0
    ov_ext = []   # mvt3 c07: (note dict, dur now, dur with the LEG_OVERLAP_MIN_S floor)
    for n in ns:
        if (round(n["qn"], 3), n["pitch"]) in UNI_DROP.get(tname, set()):   # c04 (A #2): same-patch unison copy
            dropped += 1
            continue
        e = n["end"]
        for o in ns:
            if o.get("leg_prev") is n and id(o) in shift and abs(e - (o["qn"] + LEG_OVERLAP)) < 0.01:
                e = new_on(o) + LEG_OVERLAP
        # mvt3 c07 (critic A #2): the legato overlap is at least LEG_OVERLAP_MIN_S[family] seconds (not into a same-pitch
        # target, at most half the target's own length)
        # (applied after the re-bow splits, to the note dict if its end is unchanged by then: ov_ext)
        ovf_ = LEG_OVERLAP_MIN_S.get(family)
        ov_to_ = None
        if ovf_:
            for o in ns:
                if o.get("leg_prev") is n and o["pitch"] != n["pitch"] and abs(e - (new_on(o) + LEG_OVERLAP)) < 0.01:
                    on_ = new_on(o)
                    want_ = min(on_ + ovf_ * bpm_at(on_) / 60.0, on_ + 0.5 * max(0.0, o["end"] - on_))
                    if want_ > e + EPS:
                        ov_to_ = want_
        q1 = new_on(n)
        dl_ = UNI_DELAY.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if dl_ is not None:   # c17 (B #6)
            q1 = max(q1, dl_)
        if family == "harp" and HARP_VEL_MAX is not None and n["vel"] > HARP_VEL_MAX:   # mvt3 c09 (critic B #1)
            n["vel"] = HARP_VEL_MAX
        out_notes.append({"qn": round(q1, 4), "dur": round(max(0.02, e - q1), 4), "pitch": n["pitch"], "vel": n["vel"],
                          "sq": round(n["qn"], 4), "_art": n.get("rep_row") or n.get("art")})
        if ov_to_ is not None:
            ov_ext.append((out_notes[-1], out_notes[-1]["dur"], round(max(0.02, ov_to_ - q1), 4)))   # sq: score onset (analysis only); mvt1 c37: REP_ROW row
    if family == "harp" and HARP_RING_S:
        damps_ = []
        for si_, s_ in enumerate(staves):
            for q_, k_, v_ in ev[s_]:
                txt_ = " ".join(str(x_) for x_ in v_) if isinstance(v_, (list, tuple)) else str(v_)
                if k_ == "text" and HARP_DAMP_TEXT in txt_:
                    only_ = next((staves[i_] for m_, i_ in HARP_DAMP_STAFF.items() if m_ in txt_ and i_ < len(staves)), None)
                    damps_.append((q_, only_))
        ring_n = 0
        for a, n in zip(out_notes, [n for n in ns if (round(n["qn"], 3), n["pitch"]) not in UNI_DROP.get(tname, set())]):
            e0_ = a["qn"] + a["dur"]
            e1_ = sec_to_qn(qn_to_sec(e0_) + HARP_RING_S)
            for dq_, only_ in damps_:
                if a["qn"] < dq_ - EPS and (only_ is None or n.get("staff") == only_):
                    e1_ = min(e1_, max(e0_, dq_)) if dq_ >= e0_ - EPS else min(e1_, dq_)
            if e1_ > e0_ + EPS:
                a["dur"] = round(e1_ - a["qn"], 4)
                ring_n += 1
            elif e1_ < e0_ - EPS:
                a["dur"] = round(max(0.02, e1_ - a["qn"]), 4)
        print(f"  {tname}: {ring_n} notes ring {HARP_RING_S} s past their written end; damps at {[d_ for d_, _ in damps_]}", file=sys.stderr)
    # c04 (actor, after the first c04 render): a note must end before a later note starts on the same track when that
    # later note is a tremolo moved early (TREM_LEAD_S) or has the same pitch. The bar 62 tenuto crossfade (A #3) plus the
    # tremolo lead made Vln I/II's E6/E5 overlap their own tremolo re-attack (end 212.02, new onset 211.955): the
    # note-off of the old note cut the new one and Vln II lost the bar 63 sf for 0.4 qn (-15 to -20 dB).
    trem_on = [o["qn"] for o, n in zip(out_notes, [n for n in ns if (round(n["qn"], 3), n["pitch"]) not in
                                                    UNI_DROP.get(tname, set())]) if n.get("art") == "Tremolo"]
    cut = 0
    for a in out_notes:
        ea = a["qn"] + a["dur"]
        for b in out_notes:
            if a["qn"] + EPS < b["qn"] < ea - EPS and (b["pitch"] == a["pitch"] or (ea - b["qn"] < 0.1 and any(abs(b["qn"] - t) < EPS for t in trem_on))):
                ea = b["qn"] - 0.005
        if ea < a["qn"] + a["dur"] - EPS:
            a["dur"] = round(max(0.02, ea - a["qn"]), 4)
            cut += 1
    if cut:
        print(f"  {tname}: {cut} notes ended before a same-pitch or tremolo onset", file=sys.stderr)
    ks_timed = 0
    ks_old = {}   # mvt3 c13: id(keyswitch) -> its time by the KS_LEAD rule (used where KS_LEAD_S would cut a legato note)
    for k_ in ks:
        nn = k_.pop("note")
        rest_ = k_.pop("rest", False)
        # mvt3 c15 (Movement II c52): KS_LEAD_SPANS {track: [(from_qn, to_qn, seconds)]} sets the lead for the keyswitches
        # of notes inside a span (one row per line plus the keyswitch 0.15 s before each remaining row change: 0 of 127
        # joins moved 25 ms between two renders there)
        ksl_ = next((s_ for a_, b_, s_ in KS_LEAD_SPANS.get(tname, []) if a_ - EPS <= nn["qn"] < b_ - EPS), KS_LEAD_S)
        if ksl_ and not nn.get("sost_rep"):
            # mvt3 c13 (critic A #3): see KS_LEAD_S
            on_ = new_on(nn)
            lim_ = on_ - lead_qn(on_, ksl_)
            ks_old[id(k_)] = round(max(0.0, min(k_["qn"], on_ - 0.03)), 4)
            if rest_:
                k_["qn"] = round(max(0.0, min(k_["qn"], lim_)), 4)
            else:
                po_ = max((new_on(o) for o in ns if o is not nn and new_on(o) < on_ - 0.01), default=None)
                if po_ is not None and po_ >= 0:
                    lim_ = max(lim_, min(sec_to_qn(qn_to_sec(po_) + KS_AFTER_PREV_ON_S), on_ - 0.01))
                k_["qn"] = round(max(0.0, lim_), 4)
                ks_timed += 1
        else:
            k_["qn"] = round(max(0.0, min(k_["qn"], new_on(nn) - 0.03)), 4)
        if nn.get("sost_rep"):   # c07 (A #1): the keyswitch just before the re-tongued note (the legato note it cuts
            k_["qn"] = round(new_on(nn) - 0.012, 4)   # ends 0.01 qn before it), so the break stays about 0.05 s
    # c26 (BRIEF item 8): staggered re-bows of the held final chord (REBOW_AT), split here at the output so that CC11,
    # CC1 and the volume envelope stay exactly those of the held note (split earlier, each segment took its own long-note
    # swell and entry shape: a CC11 rise at every re-bow). The first piece ends REBOW_GAP_QN before the re-bow; the new
    # piece is REBOW_ART at REBOW_VEL at the score qn; the keyswitch sits between them (0.02 qn before the re-bow), so it
    # does not fall inside the legato note
    rebow_n, rebow_arts, rebow_list, rebow_auto = 0, [], [], {}
    rebow_pts = list(rebow_at_t)
    if AUTO_REBOW and family == "string" and ksmaps.get(stem) and any(
            a_["name"].lower() == REBOW_ART.lower() for a_ in ksmaps[stem]["articulations"]):
        import zlib as _z
        h_ = _z.crc32(tname.encode()) / 2 ** 32   # a fixed per-track phase and piece length
        seg_s = REBOW_SEG_S * (1 - REBOW_TRACK_JITTER / 2 + REBOW_TRACK_JITTER * h_)
        auto_ = 0
        for a in sorted(out_notes, key=lambda a: a["qn"]):
            q0_, e_ = a["qn"], a["qn"] + a["dur"]
            t0_, t1_ = qn_to_sec(q0_), qn_to_sec(e_)
            if a["_art"] == "Tremolo" and any(x_ - EPS <= a["sq"] < y_ for x_, y_ in TREM_JOIN.get(tname, [])):
                continue   # mvt1 c08: joined tremolo notes are split by TREM_SPLIT below, on the tremolo row
            listed_ = any(q0_ < p_ < e_ for p_ in rebow_pts)   # mvt1 c02: listed points, the keyswitch back below
            if t1_ - t0_ <= REBOW_MAX_S and not listed_:
                continue
            later_ = [b for b in out_notes if b is not a and b["qn"] >= e_ - 0.1]
            nxt_ = min(later_, key=lambda b: b["qn"]) if later_ else None
            # a note joined into the next one (legato) is re-bowed too: the last Sus piece hands over to the next note's
            # articulation with a keyswitch 0.02 qn before its note-on (the KS Master joins an overlapping Sus note into a
            # Leg Slur note as a legato transition, mvt II c23)
            joined_ = nxt_ is not None and nxt_["qn"] < e_ + 0.05
            if any(b is not a and b["qn"] < e_ - 0.1 and b["qn"] + b["dur"] > q0_ + 0.1 and b["_art"] != REBOW_ART
                   and b["_art"] and _lg(b["_art"]) for b in out_notes):
                continue   # a legato chord partner sounds over it
            n_ = 1 if listed_ else max(2, round((t1_ - t0_) / seg_s))
            step_ = (t1_ - t0_) / n_
            for k_ in range(1, n_):
                t_ = t0_ + step_ * (k_ + (h_ - 0.5) * 0.5)
                if t_ - t0_ > 1.5 and t1_ - t_ > 1.5:
                    pa_ = round(sec_to_qn(t_), 3)
                    # mvt1 c03 (critic A #2): REBOW_MOVES (build/rebow_moves.json, tools/space_rebows.py) moves an
                    # automatic point so that no two sections change bow within REBOW_MIN_SEP_S of each other
                    pm_ = REBOW_MOVES.get(tname, {}).get(f"{pa_:.3f}")
                    rebow_pts.append(round(pm_, 3) if pm_ is not None else pa_)
                    rebow_auto[round(rebow_pts[-1], 3)] = pa_
                    auto_ += 1
            if nxt_ is not None and a["_art"] != REBOW_ART and nxt_["_art"] and nxt_["_art"] != REBOW_ART:
                kq_ = round(nxt_["qn"] - 0.02 if joined_ else max(e_ + 0.01, nxt_["qn"] - 0.05), 4)   # back to the next note's art
                # mvt3 c13: with KS_LEAD_S the next note's own keyswitch lies up to KS_LEAD_S earlier; it counts when no
                # keyswitch to another row follows it before kq_ (else the row was sent twice, 7 ms before the note)
                w_ = 0.03 + lead_qn(nxt_["qn"], KS_LEAD_S) if KS_LEAD_S else None
                if not any(abs(k__["qn"] - kq_) < 0.03 or (w_ is not None and k__["art"] == nxt_["_art"] and kq_ - w_ <= k__["qn"] <= kq_
                                                          and not any(k__["qn"] < k2_["qn"] <= kq_ and k2_["art"] != nxt_["_art"] for k2_ in ks))
                           for k__ in ks):
                    ks.append({"qn": kq_, "pitch": ks_lookup(stem, nxt_["_art"])[1], "art": nxt_["_art"]})
            # the next note keeps (or gets) its own keyswitch, so the pieces may switch to REBOW_ART
            a["_rebow_back"] = True
        if auto_:
            print(f"  {tname}: {auto_} automatic re-bow points", file=sys.stderr)
    for p_ in sorted(rebow_pts):
        for a in [a for a in out_notes if a["qn"] + 0.1 < p_ < a["qn"] + a["dur"] - 0.1]:
            e_ = a["qn"] + a["dur"]
            keep_row_ = a["_art"] in REBOW_KEEP_ARTS   # mvt3 c01 (critic A #4): the piece keeps the row (Flautando)
            if not keep_row_ and a["_art"] != REBOW_ART and not a.get("_rebow_back") and any(b["_art"] != REBOW_ART for b in out_notes if b["qn"] >= e_ - 0.1 and b is not a):
                raise SystemExit(f"REBOW_AT {tname} {p_}: a later note would need a keyswitch back")
            if not keep_row_ and a["_art"] != REBOW_ART and not any(abs(k_["qn"] - (p_ - 0.02)) < 0.001 for k_ in ks):
                ks.append({"qn": round(p_ - 0.02, 4), "pitch": ks_lookup(stem, REBOW_ART)[1], "art": REBOW_ART})
            a["dur"] = round(p_ - REBOW_GAP_QN - a["qn"], 4)
            out_notes.append({"qn": round(p_, 4), "dur": round(e_ - p_, 4), "pitch": a["pitch"], "vel": REBOW_VEL or int(round(value_at(REBOW_VEL_BY_CC, base(p_)))),
                              "sq": round(p_, 4), "_art": a["_art"] if keep_row_ else REBOW_ART, "_rebow_back": a.get("_rebow_back")})
            rebow_arts.append(a["_art"] if keep_row_ else REBOW_ART)
            # mvt1 c01: for tools/fit_rebows.py; c03: plus the piece's start (the note start or the previous re-bow) and
            # the automatic point before any REBOW_MOVES (None for listed points), for tools/space_rebows.py
            rebow_list.append([round(p_, 4), round(e_, 4), a["pitch"], round(a["qn"], 4), rebow_auto.get(round(p_, 3))])
            rebow_n += 1
    if rebow_n:
        out_notes.sort(key=lambda a: a["qn"])
        ks.sort(key=lambda k_: k_["qn"])
        print(f"  {tname}: {rebow_n} re-bows", file=sys.stderr)
    # mvt1 c04 (critic A #3, C #4): listed long timpani rolls re-struck as abutting same-pitch roll pieces of irregular
    # length, so no single roll sample plays through its loop more than once (TIMP_ROLL_RESTRIKE)
    restrikes = []
    if family == "timp" and TIMP_ROLL_RESTRIKE.get("at"):
        for a in sorted(out_notes, key=lambda a: a["qn"]):
            if not (a["_art"] or "").endswith("Rls"):
                continue
            plan_ = restrike_plan(a["qn"], a["dur"], a["sq"], a["pitch"])
            e_ = a["qn"] + a["dur"]
            prev_ = a
            for cq_, dv_ in plan_:
                prev_["dur"] = round(cq_ - 0.002 - prev_["qn"], 4)   # the old piece ends just before the new one
                nn_ = {"qn": cq_, "dur": round(e_ - cq_, 4), "pitch": a["pitch"], "vel": max(1, min(127, a["vel"] + dv_)),
                       "sq": cq_, "_art": a["_art"]}
                out_notes.append(nn_)
                restrikes.append([round(a["sq"], 3), cq_])
                prev_ = nn_
        if restrikes:
            out_notes.sort(key=lambda a: a["qn"])
            print(f"  {tname}: {len(restrikes)} roll re-strikes", file=sys.stderr)
    # mvt1 c08 (critic A #4): held tremolo notes of the TREM_JOIN spans split into abutting same-pitch tremolo pieces of
    # seeded irregular length, never starting within clear_qn of another onset or a barline (same row: no keyswitch)
    trem_splits = []
    if family == "string" and TREM_JOIN.get(tname):
        import random as _r
        all_on_ = sorted({a["qn"] for a in out_notes} | {a["sq"] for a in out_notes})
        for a in sorted(out_notes, key=lambda a: a["qn"]):
            if a["_art"] != "Tremolo" or not any(x_ - EPS <= a["sq"] < y_ for x_, y_ in TREM_JOIN[tname]):
                continue
            t0_, t1_ = qn_to_sec(a["qn"]), qn_to_sec(a["qn"] + a["dur"])
            if t1_ - t0_ <= TREM_SPLIT["max_s"]:
                continue
            rng_ = _r.Random(int(round(a["sq"] * 1000)) + a["pitch"])
            lo_, hi_ = TREM_SPLIT["seg_s"]
            cl_ = TREM_SPLIT["clear_qn"]

            def ok_(q_):
                return not any(abs(q_ - o_) < cl_ for o_ in all_on_) and \
                    min(q_ % 4.0, 4.0 - q_ % 4.0) >= cl_
            cuts_, t_ = [], t0_
            while t1_ - t_ > hi_ + lo_ * 0.8:
                tt_ = t_ + rng_.uniform(lo_, hi_)
                q_ = sec_to_qn(tt_)
                k_ = 0
                while not ok_(q_) and k_ < 40:   # slide later in 0.05 qn steps to a clear spot
                    q_ += 0.05; k_ += 1
                if not ok_(q_) or qn_to_sec(q_) > t1_ - lo_ * 0.8:
                    break
                cuts_.append(round(q_, 4))
                t_ = qn_to_sec(q_)
            e_ = a["qn"] + a["dur"]
            prev_ = a
            for cq_ in cuts_:
                prev_["dur"] = round(cq_ - TREM_SPLIT["gap_qn"] - prev_["qn"], 4)
                nn_ = {"qn": cq_, "dur": round(e_ - cq_, 4), "pitch": a["pitch"], "vel": a["vel"], "sq": cq_, "_art": a["_art"]}
                out_notes.append(nn_)
                trem_splits.append([round(a["sq"], 3), cq_, a["pitch"]])
                prev_ = nn_
        if trem_splits:
            out_notes.sort(key=lambda a: a["qn"])
            print(f"  {tname}: {len(trem_splits)} tremolo splits", file=sys.stderr)
    # mvt1 c05 (critic C #2): staggered breaths on listed long wind/brass notes (BREATH_SPLIT_AT), split here at the output
    # so CC11 and the volume envelope stay those of the held note; same articulation, so no keyswitch
    breath_splits = []
    for sq_k, pts_ in BREATH_SPLIT_AT.get(tname, {}).items():
        for a in sorted(out_notes, key=lambda a: a["qn"]):
            if abs(a["sq"] - sq_k) > 0.02:
                continue
            e_ = a["qn"] + a["dur"]
            prev_ = a
            for p_ in sorted(pts_):
                if not prev_["qn"] + 0.5 < p_ < e_ - 0.5:
                    raise SystemExit(f"BREATH_SPLIT_AT {tname} {sq_k}: split {p_} outside the note")
                prev_["dur"] = round(p_ - BREATH_SPLIT["gap_qn"] - prev_["qn"], 4)
                nn_ = {"qn": round(p_, 4), "dur": round(e_ - p_, 4), "pitch": a["pitch"],
                       "vel": max(1, min(127, a["vel"] + BREATH_SPLIT["dvel"])), "sq": round(p_, 4), "_art": a["_art"]}
                out_notes.append(nn_)
                breath_splits.append([round(sq_k, 3), round(p_, 4)])
                prev_ = nn_
            break
    if breath_splits:
        out_notes.sort(key=lambda a: a["qn"])
        print(f"  {tname}: {len(breath_splits)} breath splits", file=sys.stderr)
    # c05 (A #2): a keyswitch to a non-legato articulation must not fall inside a sounding legato-patch note (the
    # monophonic legato voice was still held at the bar 61 tremolo keyswitch). End such a note 0.01 qn before it.
    # mvt3 c13: with KS_LEAD_S such a keyswitch does not cut the note earlier than the KS_LEAD rule did: it goes after
    # the note's end, at the latest to its KS_LEAD time (so KS_LEAD_S changes keyswitch times only, no note length)
    ks_cut = 0
    for k_ in ks:
        if _lg(k_["art"]):
            continue
        for a in out_notes:
            if a["_art"] and _lg(a["_art"]) and a["qn"] + EPS < k_["qn"] < a["qn"] + a["dur"] - EPS:
                o_ = ks_old.get(id(k_))
                if o_ is not None and o_ > k_["qn"] + EPS:
                    k_["qn"] = round(min(o_, a["qn"] + a["dur"] + 0.01), 4)
                    if not a["qn"] + EPS < k_["qn"] < a["qn"] + a["dur"] - EPS:
                        continue
                a["dur"] = round(max(0.02, k_["qn"] - 0.01 - a["qn"]), 4)
                ks_cut += 1
    if ks_cut:
        print(f"  {tname}: {ks_cut} legato notes ended before a keyswitch", file=sys.stderr)
    fresh_on = [(new_on(n), n["qn"]) for n in ns if n.get("fresh") and id(n) in shift]
    if family != "timp" and CC7_POINTS.get(tname):   # mvt1 c36: a CC7 test lane (CC7 127 from qn 0)
        cc7 = [(0.0, 127)] + sorted((round(float(q_), 4), int(v_)) for q_, v_ in CC7_POINTS[tname])
    if role_cc7 and family != "timp":   # mvt3 c27: ROLE_EDGE_IN_REST CC7 carries, multiplied into the lane
        b7_ = sorted((float(c_[0]), int(c_[1])) for c_ in cc7) or [(0.0, 127)]

        def _b7(q_):
            v_ = 127
            for t_, x_ in b7_:
                if t_ > q_ + 1e-9:
                    break
                v_ = x_
            return v_

        def _sh7(q_):
            t_ = 0.0
            for sh_ in role_cc7:
                if sh_[0][0] <= q_ <= sh_[-1][0]:
                    t_ += value_at(sh_, q_)
            return t_
        qs_ = {t_ for t_, _ in b7_}
        for sh_ in role_cc7:
            for (p0_, d0_), (p1_, d1_) in zip(sh_, sh_[1:]):
                qs_ |= {p0_, p1_}
                if abs(d1_ - d0_) > 0.2:
                    k_ = max(1, int((p1_ - p0_) / 0.03))
                    qs_ |= {p0_ + (p1_ - p0_) * j_ / k_ for j_ in range(1, k_)}
            qs_.add(sh_[-1][0] + 0.001)
        out7_ = []
        for q_ in sorted(qs_):
            v_ = int(round(max(1, min(127, _b7(q_) * 10 ** (_sh7(q_) / 20)))))
            if not out7_ or out7_[-1][1] != v_:
                out7_.append((round(q_, 4), v_))
        if out7_ and out7_[0][0] > 0.0:
            out7_.insert(0, (0.0, _b7(0.0)))
        cc7 = out7_
    # mvt1 c36 (critic C #1): where the envelope falls at each subito-softer mark of this track's staves: the moved
    # onset of the track's earliest note on the mark (a fresh entry's lead), else the mark itself (SUBITO_TAIL in
    # build_reaper.vol_points)
    subito_falls = [[round(q_, 3), round(min([new_on(n) for n in ns if abs(n["qn"] - q_) < EPS] + [q_]), 4)]
                    for q_ in sub_soft_q]
    for f_, fsq in fresh_on:   # c09 (A #3); compared on sq and with a 0.001 tolerance (out_notes qn are rounded:
        for a in out_notes:    # the first version cut the fresh note itself to 0.02 qn)
            if a["sq"] < fsq - 0.001 and a["qn"] < f_ - 0.001 and a["qn"] + a["dur"] > f_ - 0.03:
                a["dur"] = round(max(0.02, f_ - 0.03 - a["qn"]), 4)
    # mvt1 c37 (critic A #4): TIMP_RH_ALT (see the default): alternate hands on repeated single strokes
    timp_rh = []
    if family == "timp" and TIMP_RH_ALT:
        prev_, hand_ = None, 0
        for a in sorted(out_notes, key=lambda a: a["qn"]):
            if not (a["_art"] or "").endswith("Lng"):
                continue
            if prev_ is not None and prev_["pitch"] == a["pitch"] and abs(a["qn"] - prev_["qn"]) > EPS \
                    and qn_to_sec(a["qn"]) - qn_to_sec(prev_["qn"]) <= TIMP_RH_ALT["max_gap_s"] + EPS:
                hand_ = 1 - hand_
            elif prev_ is None or abs(a["qn"] - prev_["qn"]) > EPS:
                hand_ = 0
            prev_ = dict(a)
            if hand_ and a["pitch"] + TIMP_RH_ALT.get("add", 24) <= 81:
                a["pitch"] += TIMP_RH_ALT.get("add", 24)
                timp_rh.append(a["sq"])
    # mvt3 c07 (critic A #2): the legato overlap floors (LEG_OVERLAP_MIN_S), on notes whose end nothing changed since
    ov_n_ = 0
    for a_, d0_, d1_ in ov_ext:
        if abs(a_["dur"] - d0_) < 1e-4 and any(b_ is a_ for b_ in out_notes) and not any(
                b_ is not a_ and b_["pitch"] == a_["pitch"] and a_["qn"] < b_["qn"] < a_["qn"] + d1_ + 0.01 for b_ in out_notes) \
                and not any(a_["qn"] + d0_ - EPS <= k_["qn"] <= a_["qn"] + d1_ + 0.01 for k_ in ks):
            a_["dur"] = d1_
            ov_n_ += 1
    if ov_n_:
        print(f"  {tname}: {ov_n_} legato overlaps raised to {LEG_OVERLAP_MIN_S.get(family)} s", file=sys.stderr)
    # mvt3 c09 (critic A #2, S1): STR_REP_NEW_BOW "plain" {gap_s, frac, min_cc, rows}: an unslurred same-pitch string
    # repeat on a sustained row whose played gap (after every lead) is under min(gap_s, frac x the onset distance) gets
    # that gap before the next note's moved note-on. The other rules measure their gap back from the score onset, so a
    # lead on the next note closed it (violas 820-832: 2 ms, dips 2.1-6.5 dB; Vln I 884 10 ms, 2.5 dB). Not into re-bow
    # pieces or other split pieces, not inside STR_REP_DETACH spans (they have the dip) or the "skip" spans
    plain_gaps = []
    PL_ = (STR_REP_NEW_BOW or {}).get("plain") if family == "string" else None
    if PL_:
        src_ = {}
        for n in ns:
            src_.setdefault((round(n["qn"], 3), n["pitch"]), n)
        rb_q_ = {round(x_[0], 3) for x_ in rebow_list}
        rows_ok_ = tuple(PL_.get("rows", ("Sus MAX", "Sus Marc LITE", "Leg")))
        det_ = ((STR_REP_DETACH or {}).get("at") or {}).get(tname, [])
        skip_ = (STR_REP_NEW_BOW.get("skip") or {}).get(tname, []) + (PL_.get("skip") or {}).get(tname, [])
        # mvt3 c12 (critic A #1): "force" {track: [score onsets]}: listed repeats take the gap at any dynamic, under a
        # slur, and inside STR_REP_DETACH / skip spans (sites that kept 10-24 ms gaps)
        force_ = {round(q_, 3) for q_ in (PL_.get("force") or {}).get(tname, [])}
        forced_done_, forced_why_ = set(), {}
        byp_ = {}
        for a in out_notes:
            byp_.setdefault(a["pitch"], []).append(a)
        for p_, l_ in byp_.items():
            l_.sort(key=lambda a: a["qn"])
            for a, b in zip(l_, l_[1:]):
                na_, nb_ = src_.get((round(a["sq"], 3), p_)), src_.get((round(b["sq"], 3), p_))
                fz_ = round(b["sq"], 3) in force_
                if na_ is None or nb_ is None or na_ is nb_ or round(b["sq"], 3) in rb_q_ or round(a["sq"], 3) in rb_q_:
                    if fz_:
                        forced_why_[round(b["sq"], 3)] = "a re-bow or split piece"
                    continue
                if not (str(a["_art"] or "").startswith(rows_ok_) and str(b["_art"] or "").startswith(rows_ok_)):
                    if fz_:
                        forced_why_[round(b["sq"], 3)] = f"rows {a['_art']} -> {b['_art']}"
                    continue
                if not fz_ and (same_slur(na_, nb_) or base(nb_["qn"]) < PL_.get("min_cc", DYN["mp"]) - EPS):
                    continue
                if not fz_ and (any(sp_[0] - EPS <= nb_["qn"] < sp_[1] - EPS for sp_ in det_)
                                or any(x_ - EPS <= nb_["qn"] < y_ - EPS for x_, y_ in skip_)):
                    continue
                if fz_:
                    forced_done_.add(round(b["sq"], 3))
                want_ = min(b["qn"] - qn_before(b["qn"], PL_["gap_s"]), PL_["frac"] * (b["qn"] - a["qn"]))
                if a["qn"] + a["dur"] > b["qn"] - want_ + 1e-4:
                    a["dur"] = round(max(0.02, b["qn"] - want_ - a["qn"]), 4)
                    plain_gaps.append(round(b["sq"], 3))
        if plain_gaps:
            print(f"  {tname}: {len(plain_gaps)} plain repeat gaps (STR_REP_NEW_BOW plain)", file=sys.stderr)
        if force_ - forced_done_:
            print(f"WARNING {tname}: STR_REP_NEW_BOW plain force: not applied at "
                  f"{[(q_, forced_why_.get(q_, 'no same-pitch repeat')) for q_ in sorted(force_ - forced_done_)]}", file=sys.stderr)
    # mvt3 c14: RR_RESET_KS_RESTATE: at each RR_RESET_ALL_AT reset that lies in a rest (no note of the track sounding),
    # the keyswitch in force is sent again 0.01 qn before the reset. REAPER does not chase keyswitches into a time
    # selection and Opus keeps the row of the last playback, so without it the first notes of a range render that
    # starts before the reset can play another row than in the full render. Entries carry "restate": True
    if RR_RESET_KS_RESTATE and RR_RESET_ALL_AT and family not in RR_RESET_ALL_SKIP and ks:
        ks.sort(key=lambda k_: k_["qn"])
        add_ = []
        for t_ in rr_all_t:
            if any(a["qn"] - 1e-6 <= t_ < a["qn"] + a["dur"] + 0.02 for a in out_notes) or t_ < 0.05:
                continue
            cur_ = [k_ for k_ in ks if k_["qn"] <= t_ + 1e-6]
            pit_, art_ = (cur_[-1]["pitch"], cur_[-1].get("art")) if cur_ else (ks_lookup(stem, first_art)[1] if first_art else None, first_art)
            if pit_ is None or any(abs(k_["qn"] - (t_ - 0.01)) < 0.05 for k_ in ks):
                continue
            add_.append({"qn": round(t_ - 0.01, 4), "pitch": pit_, "art": art_, "restate": True})
        ks.extend(add_)
        ks.sort(key=lambda k_: k_["qn"])
    final_ring = []   # mvt3 c08 (A #1): FINAL_RING notes held ring_s past "end"
    if ring_pts:
        e1_ = sec_to_qn(qn_to_sec(float(FINAL_RING["end"])) + float(FINAL_RING["ring_s"]))
        for a in out_notes:
            if a["qn"] <= FINAL_RING["at"] + 0.01 and a["qn"] + a["dur"] >= FINAL_RING["end"] - 0.15:
                a["dur"] = round(e1_ - a["qn"], 4)
                final_ring.append(a["sq"])
    instr_post_rep = {}
    if INSTR_POST:   # mvt3 c17: the instrument-side post-pass (see the default and tools/instr_post.py)
        import instr_post as _ip
        ctx_ = {"cfg": INSTR_POST, "tname": tname, "family": family, "out_notes": out_notes, "ns": ns, "cc11": cc11,
                "cc1": cc1, "cc7": cc7, "cc16": cc16, "vol_db": vol_db, "accent_q": accent_q, "base": base,
                "same_slur": same_slur, "qn_to_sec": qn_to_sec, "sec_to_qn": sec_to_qn, "first_art": first_art,
                "dyn_curve": dyn_curve, "ks": ks, "vol_bp": vol_bp, "hairpins": [(h_[0], h_[1], h_[2]) for h_ in hps],   # c22: with the kind (instr_post cresc_mono)
               
                "accent_staves": _accent_staves()}
        instr_post_rep = _ip.apply(ctx_)
        ks.sort(key=lambda k_: k_["qn"])
        vol_bp = sorted(set(ctx_["vol_bp"]))
        cc11, cc1, cc7, vol_db, dyn_curve = ctx_["cc11"], ctx_["cc1"], ctx_["cc7"], ctx_["vol_db"], ctx_["dyn_curve"]
        if instr_post_rep:
            print(f"  {tname}: instr_post " + ", ".join(f"{k_}={(len(v_) if isinstance(v_, list) else v_)}" for k_, v_ in instr_post_rep.items() if k_ != "vol_guard")
                  + (f", vol_guard fixed={instr_post_rep['vol_guard']['fixed']} left={instr_post_rep['vol_guard']['left']}" if "vol_guard" in instr_post_rep else ""), file=sys.stderr)
    # mvt3 c25 (critic C c25 #2, ruling 5): TIMP_ARRIVAL_RAMP. At a printed arrival louder than the crescendo before it
    # the crescendo's hairpin gain (+8 dB at bar 223) stood over the static fff roll level, so the roll fell 8 dB within a
    # quarter of a beat (CC7 96 -> 38) and the fff timpani sat 17-26 dB under the master while the printed decrescendo
    # lasts the bar. The roll's CC7 from 0.03 qn before its moved note-on to 0.04 qn before "to" becomes one ramp, linear
    # in dB (CC7 is linear amplitude in Opus), from the CC7 0.1 qn before the note-on to the CC7 the track played at the
    # last earlier mark equal to the mark printed at "to" (no mark there: the lane's own value at "to")
    timp_arr = []
    if family == "timp" and TIMP_ARRIVAL_RAMP and cc7:
        c7s_ = sorted((float(c_[0]), int(c_[1])) for c_ in cc7)

        def c7_at(q_):
            v_ = c7s_[0][1]
            for t_, x_ in c7s_:
                if t_ > q_ + 1e-9:
                    break
                v_ = x_
            return v_
        for row_ in TIMP_ARRIVAL_RAMP:
            at_, to_ = row_[0], row_[1]
            on_ = [a["qn"] for a in out_notes if abs(a["sq"] - at_) < 0.02]
            if not on_:
                continue
            q_on = min(on_)
            sv_ = c7_at(q_on - 0.1)
            if len(row_) >= 4:   # mvt3 c26 (critic B #4a): (at, to, CC7 at the note-on, CC7 at "to") given
                sv_ = int(row_[2])
            mk_to = [d_ for mq, d_ in marks if abs(mq - to_) < 0.01 and d_ in DYN]
            ev_ = None
            if mk_to:
                prev_ = [mq for mq, d_ in marks if d_ == mk_to[0] and mq < at_ - 0.01]
                if prev_:
                    pon_ = [a["qn"] for a in out_notes if abs(a["sq"] - prev_[-1]) < 0.02]
                    ev_ = c7_at((min(pon_) if pon_ else prev_[-1]) + 0.05)
            if ev_ is None:
                ev_ = c7_at(to_ - 0.06)
            if len(row_) >= 4:
                ev_ = int(row_[3])
            q0_, q1_ = q_on - 0.03, to_ - 0.04
            d0_, d1_ = 20 * math.log10(max(1, sv_) / 127.0), 20 * math.log10(max(1, ev_) / 127.0)
            keep_ = [c_ for c_ in c7s_ if c_[0] < q0_ - 1e-6 or c_[0] > q1_ + 1e-6]
            n_ = max(2, int((q1_ - q0_) / 0.125))
            ramp_ = [(round(q0_ + (q1_ - q0_) * j_ / n_, 4),
                      int(round(127 * 10 ** ((d0_ + (d1_ - d0_) * j_ / n_) / 20)))) for j_ in range(n_ + 1)]
            c7s_ = sorted(keep_ + ramp_)
            timp_arr.append([at_, to_, sv_, ev_])
        cc7 = [list(c_) for i_, c_ in enumerate(c7s_) if i_ == 0 or c_[1] != c7s_[i_ - 1][1]]
    for a in out_notes:
        a.pop("_art")
        a.pop("_rebow_back", None)
    lead_stats = collections.Counter("leg" if n.get("leg_target") else "entry" for n in ns if id(n) in shift)
    pitches = [n["pitch"] for n in ns]
    ks_keys = sorted({a["key"] for a in ksmaps[stem]["articulations"]}) if stem in ksmaps else []
    clash = sorted({p for p in pitches if p in ks_keys})
    return {
        "name": tname, "staves": staves, "patch": patch, "stem": stem, "family": family, "pan": pan,
        "first_art": first_art,
        "first_ks": ks_lookup(stem, first_art)[1] if first_art else None,
        "notes": out_notes,
        "leads": dict(lead_stats), "notches": len(notches), "unison_dropped": dropped, "bloomv": bloomv, "bloomv_skip": bloomv_skip, "timp_hp": timp_hp, "timp_arrival": timp_arr, "hp_end_tgt": hp_end_tgt,
        "pitch_trimmed": pitch_trimmed, "early_fills": early_n, "loop_fills": loop_n, "tie_slurred": tie_slurred, "metric_vel": dict(metric_n), "metric_db": dict(metric_db_n), "div_entries": div_entries, "extra_leads": extra_used, "leg_leads": leg_used, "port": port_done, "bcsoft": bcsoft_n,
        "hpgain": [[round(i[1], 3), round(i[2], 3), i[4]] for i in vol_parts if i[0] == "hpgain"],
        "acc_vel_fixed": acc_vel_fixed, "rep_retongued": rep_retongued, "arrival_weight": arr_w, "tenuto_swell": ten_sw,
        "down_strokes": [round(n["qn"], 3) for n in ns if n.get("down_stroke")],
        **({"rep_strokes": rep_strokes, "rep_rebows": sorted(rep_rebow_q)} if (rep_strokes or rep_rebow_q) else {}),
        **({"rep_sus_gaps": rep_sus_gaps} if rep_sus_gaps else {}),
        **({"stroke_falls": stroke_falls} if stroke_falls else {}),
        **({"rep_split_gaps": rep_split_gaps} if rep_split_gaps else {}),
        "trem_entries": trem_entries,
        "rebows": sorted(rebow_list), "plain_gaps": plain_gaps, "rebow_fill_ends": rebow_fill_ends, "restrikes": restrikes, "breath_splits": breath_splits, "trem_splits": trem_splits, "slur_rep_merged": slur_rep_merged,
        "short_strokes": [round(n["qn"], 3) for n in ns if n.get("short_stroke")],
        "pt_slurs": pt_slurs,
        "hp_chained": hp_chained, "loud_swells": loud_swells, "hp_soft": hp_soft, "hp_soft_acc": hp_soft_acc, "hp_bridged": hp_bridged, "bc_skipped": bc_skipped, "roles_chained": role_chained, **({"role_edge_moved": role_edge_moved} if role_edge_moved else {}), **({"role_edge_join": role_edge_join} if role_edge_join else {}), "accent_db": acc_n, "accent_on_arrival": acc_on_arr, "detached_accents": det_n,
        "acc_sus": [round(n["qn"], 3) for n in ns if n.get("acc_sus")],
        "timp_chain_skip": timp_chain_skip, "meas_trem": meas_trem, "cc1_fronts": cc1_fronts, "acc_fitted": acc_fitted, "accent_body": acc_body, "acc_trimmed": sorted(round(x_, 3) for x_ in acc_trim_q), "row_trimmed": row_trimmed,
        **({"steady_line": steady_line} if steady_line else {}), "ks": ks, "cc1": cc1, "cc11": cc11, "cc15": cc15, "cc7": cc7, "cc70": cc70, "cc36": cc36, "cc16": sorted(cc16), "rr_reset_cc": RR_RESET_CC, "pair_release": pair_rel, "detach_dips": detach_dips, "str_rep_dips": str_rep_dips, "beat_gaps": beat_gaps, "meas_trem_alt": mt_alt_q, "uni_fades": uni_fades, "uni_played": uni_played, "slur_start_sus": sorted(round(n["qn"], 3) for n in ns if n.get("slur_start_sus")), "slur_start_joins": slur_start_joins, "acc_head_joins": acc_head_joins, "pickup_sus": pickup_sus, "pickup_lift": pickup_lift, "synco_shaped": synco_shaped, "det_lead_clamped": det_lead_clamped, "retongue_leads": retongue_leads, "wide_leg": wide_leg, "held_decresc": held_decresc, "held_decresc_carry": held_decresc_carry, **({"held_decresc_led": held_decresc_led} if held_decresc_led else {}), "portato_tails": sorted(round(n["qn"], 3) for n in ns if n.get("portato_tail")), "stac_leads": stac_leads, **({"row_slur_overlaps": row_slur_ov} if row_slur_ov else {}), "rest_short": rest_short, "end_at": end_at, "cutoff_early": cutoff_early, "final_ring": final_ring, "rep_row": sorted(round(n["qn"], 3) for n in ns if n.get("rep_row")), "rep_row_reps": rep_row_reps, "slur_head_rep": slur_head_rep, "chord_head_gaps": chord_head_gaps, "chord_loure_gaps": chord_loure_gaps, "sul_notes": sul_notes, "rep_after_stac": sorted(round(n["qn"], 3) for n in ns if n.get("rep_after_stac")), "timp_rh": timp_rh, "leg_vel_extra": leg_vel_extra, **({"leg_vel_span": leg_vel_span} if leg_vel_span else {}), "slur_head_leads": slur_head_leads, "group_leads": group_leads, "subito_fresh": subito_fresh, "subito_falls": subito_falls, "cresc_fronts": cresc_fronts, **({"cresc_front_shift": cresc_front_shift} if cresc_front_shift else {}), **({"leg_join_holds": leg_join_holds} if leg_join_holds else {}), "dyn_curve": dyn_curve, **({"instr_post": instr_post_rep} if instr_post_rep else {}), "vol_db": vol_db, **({"vol_lin": True} if VOL_LIN else {}), "vol_bp": vol_bp, **({"vol_post": vol_post} if vol_post else {}),
        "hairpins": [[round(a, 4), round(b, 4), k] for a, b, k in hps],
        "range": [min(pitches), max(pitches)] if pitches else None,
        "ks_clash": clash,
        "art_counts": dict(collections.Counter([n.get("rep_row") or n.get("art") for n in ns] + rebow_arts)),
    }


# mvt1 c00: unpitched percussion (family "perc"). The notes come from the event list's drum events (mockup.ly logs
# drum-type and length), not from the MIDI: PERC_MAP {track: {drum type: {"key", optional "vel", "lead_s", "min_s"}}}.
# Tied drum notes are one stroke; a stroke rings for at least min_s seconds (default PERC_MIN_S; the cymbal and tam-tam
# samples are let-ring recordings, and a note-off starts their release). Velocity follows the printed dynamic (PERC_VEL)
# unless the map gives one. CC11 is held at 127 (the patches' Controller 11 is a plain volume).
PERC_MAP = globals().get("PERC_MAP", {})   # set in build/score_config.py
PERC_MIN_S = globals().get("PERC_MIN_S", 9.0)
# mvt3 c05 (critic A #3): PERC_END_AT {track: {stroke score qn: end qn}}: the listed strokes end at that qn (a printed
# cut-off, e.g. a tied stroke that stops with the orchestra's last quarter), overriding min_s; the patch obeys the note-off
PERC_END_AT = globals().get("PERC_END_AT", {})
PERC_VEL_ADD = globals().get("PERC_VEL_ADD", {})   # mvt3 c20: see build_perc_track
PERC_VEL = globals().get("PERC_VEL") or [(22, 30), (34, 40), (46, 55), (58, 70), (72, 85), (88, 100), (114, 114), (124, 124)]


def build_perc_track(tname, staves, patch, family, pan):
    stem = patch.rsplit("/", 1)[1][:-4]
    marks, hps = hairpins_and_marks(staves)
    lvl = lambda q: next((DYN[d_] for q_, d_ in reversed(marks) if q_ <= q + EPS and d_ in DYN), DYN["mf"])
    ties = {round(q, 3) for s_ in staves for q, k, v in ev[s_] if k == "tie"}
    out_notes, last = [], {}
    for s_ in staves:
        for q, k, v in ev[s_]:
            if k != "drum" or v[0] not in PERC_MAP.get(tname, {}) or v[0].startswith("_"):
                continue
            spec, ln = PERC_MAP[tname][v[0]], float(v[1])
            # c32 (critics A #4, C #3): "only_at" [score qn]: this track plays only the strokes at these qns (a second
            # instrument doubling one stroke, e.g. a let-ring cymbal under a crescendo roll's peak); tied continuations
            # of that stroke still extend it
            if "only_at" in spec and not any(abs(q - o_q) < EPS for o_q in spec["only_at"]):
                prev = last.get(v[0])
                if prev is not None and abs(prev["_end"] - q) < EPS and round(prev["_end_last"], 3) in ties:
                    prev["_end"] = q + ln; prev["_end_last"] = q
                continue
            # v621 port: "skip_at" [score qn]: strokes the previous sample already plays (the sus-cymbal roll's let-ring
            # crescendo sample peaks on the printed fff stroke and rings on; a second roll sample there would be wrong)
            if any(abs(q - s_q) < EPS for s_q in spec.get("skip_at", [])):
                prev = last.get(v[0])
                if prev is not None:
                    prev["_end"] = max(prev["_end"], q + ln); prev["_end_last"] = q
                continue
            prev = last.get(v[0])
            if prev is not None and abs(prev["_end"] - q) < EPS and round(prev["_end_last"], 3) in ties:   # tied on
                prev["_end"] = q + ln; prev["_end_last"] = q
                continue
            vel = spec.get("vel") or int(round(value_at(PERC_VEL, lvl(q))))
            vel = max(vel, spec.get("vel_min", 0))   # mvt1 c01 (B #4): a floor where the softest layers are dark and quiet
            # mvt3 c20: PERC_VEL_ADD {track: [(from score qn, to, add)]}: a velocity offset on the strokes in a span (the
            # crash and bass drum of the final chord are the master's sample peaks under the delivery limiter)
            vel = int(max(1, min(127, vel + sum(d_ for a_, b_, d_ in PERC_VEL_ADD.get(tname, []) if a_ - EPS <= q < b_))))
            q1 = qn_before(q, spec.get("lead_s", 0.0)) if spec.get("lead_s") else q
            if spec.get("delay_s"):   # mvt1 c03 (critic C #3): a struck note starts this late (lead_s is applied first)
                q1 = sec_to_qn(qn_to_sec(q1) + spec["delay_s"])
            n = {"qn": round(q1, 4), "sq": round(q, 4), "pitch": spec["key"], "vel": vel, "_end": q + ln, "_end_last": q,
                 "_min_s": spec.get("min_s", PERC_MIN_S)}
            out_notes.append(n); last[v[0]] = n
    for n in out_notes:
        e_ = max(n.pop("_end"), sec_to_qn(qn_to_sec(n["sq"]) + n.pop("_min_s")))
        n.pop("_end_last")
        for eq_, ee_ in PERC_END_AT.get(tname, {}).items():
            if abs(n["sq"] - eq_) < EPS:
                e_ = ee_
        n["dur"] = round(e_ - n["qn"], 4)
    out_notes.sort(key=lambda n: n["qn"])
    dyn_curve = [(round(q, 4), DYN[d_]) for q, d_ in marks if d_ in DYN]
    # mvt1 c05: roles.json rows apply to the percussion tracks too (build_perc_track wrote a flat envelope, so the c02
    # Tam-tam [696,712,+8] row never took effect): the same shape as build_track's span rows (0.5 qn ramp in before the
    # start, out after the end; with an end_ramp the cut opens linearly over it and is 0 at the end)
    rows_ = [(r[0], r[1], r[2], r[3] if len(r) > 3 else 0) for r in ROLES.get(tname, [])]
    # mvt1 c06 (critic C #5): PERC_MAP[track]["_damp"] = [(score qn, dB, seconds)]: a printed damp (the sample rings on
    # after its note-off): the level falls linearly from 0 at qn to dB over the seconds and stays there until the next
    # stroke of the track starts
    damps_ = []
    for dq_, ddb_, ds_ in PERC_MAP.get(tname, {}).get("_damp", []):
        nx_ = min([n["qn"] for n in out_notes if n["qn"] > dq_ + EPS] + [SE + 8])
        damps_.append((dq_, sec_to_qn(qn_to_sec(dq_) + ds_), ddb_, nx_))

    # mvt1 c07 (critic B #1): LEVEL_SHAPES apply to the percussion tracks too (piecewise linear, exact breakpoints)
    shapes_ = [[(float(x_), float(d_)) for x_, d_ in ps_] for ps_ in LEVEL_SHAPES.get(tname, [])]

    def role_db(q):
        v = 0.0
        for ps_ in shapes_:
            if ps_[0][0] <= q <= ps_[-1][0]:
                v += value_at(ps_, q)
        for d0_, d1_, ddb_, nx_ in damps_:
            if d0_ <= q < nx_ - 0.05:
                v += ddb_ * min(1.0, (q - d0_) / (d1_ - d0_))
        for a, b2, dbv, er in rows_:
            if er:
                if a - 0.5 <= q < b2:
                    v += dbv * max(0.0, min(1.0, (q - (a - 0.5)) / 0.5, (b2 - q) / er))
            elif a - 0.5 <= q <= b2 + 0.5:
                v += dbv * max(0.0, min(1.0, (q - (a - 0.5)) / 0.5, (b2 + 0.5 - q) / 0.5))
        return v
    vol_db, last_ = [], None
    if rows_ or damps_ or shapes_:
        grid_ = sorted({round(i * 0.25, 4) for i in range(int((SE + 4) / 0.25))}
                       | {round(x_, 4) for ps_ in shapes_ for x_, _ in ps_}
                       | {round(x, 4) for a, b2, _, er in rows_ for x in (a - 0.5, a, b2 - er if er else b2, b2 if er else b2 + 0.5)}
                       | {round(x, 4) for d0_, d1_, _, nx_ in damps_ for x in (d0_, d1_, nx_ - 0.05, nx_ - 0.04)})
        for q in grid_:
            v = round(role_db(q), 2)
            if v != last_:
                vol_db.append((q, v)); last_ = v
    vol_db = vol_db or [(0.0, 0.0)]
    # mvt3 c13 (critics C #4 / A #4, MANUAL-GAPS #6): RR_RESET_AT on percussion tracks. A reset at a score qn where a
    # stroke starts is sent 0.02 qn before that stroke's moved onset; at any other qn it is sent at that qn (a reset
    # inside a rest, before the next stroke)
    cc16 = []
    for q_ in RR_RESET_AT.get(tname, []):
        at_ = [n["qn"] for n in out_notes if abs(n.get("sq", n["qn"]) - float(q_)) < 0.01]
        cc16.append((round(max(0.0, (min(at_) - 0.02) if at_ else float(q_)), 4), 127))
        if any(abs(n["qn"] - cc16[-1][0]) < 0.005 for n in out_notes):
            print(f"  WARN {tname}: RR_RESET_AT {q_} falls on a note-on (no guaranteed order)", file=sys.stderr)
    return {
        "cc16": sorted(cc16), "rr_reset_cc": RR_RESET_CC,
        "name": tname, "staves": staves, "patch": patch, "stem": stem, "family": family, "pan": pan,
        "first_art": None, "first_ks": None, "notes": out_notes,
        "leads": {}, "notches": 0, "unison_dropped": 0, "bloomv": 0, "bloomv_skip": 0, "timp_hp": 0, "pitch_trimmed": 0,
        "early_fills": 0, "loop_fills": 0, "tie_slurred": 0, "metric_vel": {}, "metric_db": {}, "div_entries": [],
        "extra_leads": [], "leg_leads": [], "port": [], "bcsoft": 0, "hpgain": [], "pt_slurs": 0, "hp_chained": [],
        "hp_soft": 0, "hp_soft_acc": 0, "hp_bridged": 0, "bc_skipped": [], "roles_chained": 0, "accent_db": 0,
        "ks": [], "cc1": [], "cc11": [(0.0, 127)] if out_notes else [], "cc15": [], "cc7": [], "cc70": [],
        "dyn_curve": dyn_curve, "vol_db": vol_db,
        "vol_bp": sorted({round(x, 4) for d0_, d1_, _, nx_ in damps_ for x in (d0_, d1_)}
                         | {round(x_, 4) for ps_ in shapes_ for x_, _ in ps_}),
        "hairpins": [[round(a, 4), round(b, 4), k] for a, b, k in hps],
        "range": [min(n["pitch"] for n in out_notes), max(n["pitch"] for n in out_notes)] if out_notes else None,
        "ks_clash": [], "art_counts": {},
    }


# c04 (A #2): two tracks on the same patch file playing the same pitch together render the identical sample (Hn1+Hn2
# at the climax measured a correlation of 0.999; Cl1+Cl2 at qn 259 partly cancelled). Keep the longer note (the earlier
# track on a tie; a slurred note before both), drop the copies, and raise the kept note by 10 log10(copies) dB.
UNI_DROP, UNI_BOOST = collections.defaultdict(set), collections.defaultdict(dict)
UNI_DELAY = collections.defaultdict(dict)   # c17 (B #6); UNI_OUTLAST_QN / UNI_DELAY_OVERLAP_QN are defaults above
UNI_PLAY = collections.defaultdict(dict)   # mvt3 c08 (A #3): UNI_OUTLAST_PLAY copies {track: {(qn, pitch): kept end}}


UNI_BY_DYN = True   # mvt1 c10 (critic B #3): rank the kept copy by printed dynamic first
UNI_MARKS = {}


def find_unisons():
    for t in TRACKS:
        if t[3] in ("wind", "brass"):
            UNI_MARKS[t[0]] = hairpins_and_marks(t[1])[0]
    by_patch = collections.defaultdict(list)
    for t in TRACKS:
        if t[3] in ("wind", "brass"):
            by_patch[t[2]].append(t)
    for patch, ts in by_patch.items():
        if len(ts) < 2:
            continue
        # c19 (A #1): leave out notes that TRACK_WINDOWS moves to another track (Horn 1's bars 79-82 play on the a2 track,
        # so Horn 4's Ab3 at 265 was grouped with a note Horn 1 no longer plays and lost its first two beats)
        def _owned(tn, q):
            return tw_keep(tn, q)
        allnotes = [(t[0], n) for t in ts for s_ in t[1] for n in notes[s_] if _owned(t[0], n["qn"])]
        seen = set()
        for i, (ta, na) in enumerate(allnotes):
            if (ta, na["qn"], na["pitch"]) in seen:
                continue
            grp = [(ta, na)] + [(tb, nb) for tb, nb in allnotes[i + 1:] if tb != ta and nb["pitch"] == na["pitch"]
                                and abs(nb["qn"] - na["qn"]) < 0.01
                                and min(na["end"], nb["end"]) - max(na["qn"], nb["qn"]) > 0.25]
            if len(grp) < 2:
                continue
            order = [t[0] for t in ts]
            staves_of = {t[0]: t[1] for t in ts}
            slurred = lambda x: any(a - EPS <= x[1]["qn"] <= b + EPS for a, b in spans(staves_of[x[0]], "slur"))
            # a slurred note (part of a line) first, then the longer note, then the earlier track
            # mvt1 c10 (critic B #3): the printed dynamic first (the last printed mark at the onset on the copy's own
            # staves): Horn 4's f chord tone took the a2 horns' ff theme note at qn 670 (Horn 1 -18 dB re master there,
            # -7.4..-9.3 on the theme notes around it), Horn 3's mp chord note Horn 1's mf solo E4 at 418
            def printed(x):
                mk_ = [d_ for q_, d_ in UNI_MARKS[x[0]] if q_ <= x[1]["qn"] + EPS]
                return DYN[mk_[-1]] if mk_ else 0
            keep = max(grp, key=lambda x: (printed(x) if UNI_BY_DYN else 0, slurred(x), x[1]["end"] - x[1]["qn"],
                                           -order.index(x[0])))
            if UNI_CHORD_SPLIT:
                # mvt3 c01 (critic A #3): tracks of the group that play the same chord at this onset share it out by
                # pitch (top note to the first track in TRACKS order)
                def chord_of(tn_, q_):
                    return sorted({n_["pitch"] for s_ in staves_of[tn_] for n_ in notes[s_]
                                   if abs(n_["qn"] - q_) < 0.01 and _owned(tn_, n_["qn"])}, reverse=True)
                kc_ = chord_of(keep[0], keep[1]["qn"])
                if len(kc_) > 1:
                    ct_ = [x for x in sorted(grp, key=lambda x: order.index(x[0])) if chord_of(x[0], x[1]["qn"]) == kc_]
                    rk_ = kc_.index(na["pitch"])
                    if len(ct_) >= 2 and rk_ < len(ct_):
                        keep = ct_[rk_]
                        print(f"  unison chord qn {na['qn']:.2f} {kc_}: pitch {na['pitch']} to {keep[0]}", file=sys.stderr)
            if any(x[1]["end"] > keep[1]["end"] + 1.0 + EPS for x in grp):
                # a copy that holds on more than 1 qn after the kept note would leave a hole in its own part
                print(f"  unison qn {na['qn']:.2f} pitch {na['pitch']}: left (a copy holds > 1 qn longer)", file=sys.stderr)
                for tb, nb in grp:
                    seen.add((tb, nb["qn"], nb["pitch"]))
                continue
            for tb, nb in grp:
                seen.add((tb, nb["qn"], nb["pitch"]))
                if tb != keep[0]:
                    if nb["end"] > keep[1]["end"] + UNI_OUTLAST_QN + EPS:
                        # c17 (B #6): a copy that outlasts the kept note (Hn4 Ab3 at 265 held 1 qn past Horn 1, and the f
                        # horn chord lost its Ab3 on bar 80 beat 3) starts where the kept note leaves, overlapping it by
                        # UNI_DELAY_OVERLAP_QN, instead of being dropped (playing it from the start would double the
                        # identical sample)
                        if UNI_OUTLAST_PLAY and keep[1]["end"] - UNI_DELAY_OVERLAP_QN - nb["qn"] > UNI_OUTLAST_PLAY["min_delay_qn"]:
                            UNI_PLAY[tb][(round(nb["qn"], 3), nb["pitch"])] = keep[1]["end"]   # mvt3 c08 (A #3)
                        else:
                            UNI_DELAY[tb][(round(nb["qn"], 3), nb["pitch"])] = keep[1]["end"] - UNI_DELAY_OVERLAP_QN
                    else:
                        UNI_DROP[tb].add((round(nb["qn"], 3), nb["pitch"]))
            UNI_BOOST[keep[0]][(round(keep[1]["qn"], 3), keep[1]["pitch"])] = round(10 * __import__("math").log10(len(grp)), 2)
            print(f"  unison qn {na['qn']:.2f} pitch {na['pitch']}: keep {keep[0]}, drop "
                  f"{[tb for tb, _ in grp if tb != keep[0]]}", file=sys.stderr)


find_unisons()
parts = [build_perc_track(*t) if t[3] == "perc" else build_track(*t) for t in TRACKS]
# mvt1 c39: ALIAS_TRACKS (see the default): built under the source's name with its windows kept, then renamed
for an_, as_ in ALIAS_TRACKS.items():
    src_ = next(t for t in TRACKS if t[0] == as_["source"])
    keep_tw_, keep_pt_ = TRACK_WINDOWS.get(src_[0]), PITCH_TRIMS.get(src_[0])
    TRACK_WINDOWS[src_[0]] = ([tuple(w_) for w_ in as_["windows"]], True)
    if as_.get("no_pitch_trims"):
        PITCH_TRIMS.pop(src_[0], None)
    # mvt1 c40: "drop" and "set" (see the default), applied before "tables" so alias-only rows are kept
    keep_tb_ = {}
    def _first_num(r_):
        while isinstance(r_, (list, tuple)) and r_:
            r_ = r_[0]
        try:
            return float(r_)
        except (TypeError, ValueError):
            return None
    for tbn_, sel_ in as_.get("drop", {}).items():
        tab_ = globals()[tbn_]
        if tbn_ not in keep_tb_:
            keep_tb_[tbn_] = tab_.get(src_[0])
        cur_ = tab_.get(src_[0])
        if cur_ is None:
            continue
        if sel_ is None:
            tab_[src_[0]] = type(cur_)()
        elif isinstance(cur_, dict):
            tab_[src_[0]] = {k_: v_ for k_, v_ in cur_.items() if str(k_).startswith("_")
                             or not any(abs(float(k_) - float(s_)) < 1e-3 for s_ in sel_)}
        else:
            tab_[src_[0]] = [r_ for r_ in cur_ if _first_num(r_) is None
                             or not any(abs(_first_num(r_) - float(s_)) < 1e-3 for s_ in sel_)]
        print(f"  alias {an_}: {tbn_} {'all' if sel_ is None else len(sel_)} of the source's entries dropped "
              f"({len(cur_)} -> {len(tab_[src_[0]])})", file=sys.stderr)
    for tbn_, v_ in as_.get("set", {}).items():
        tab_ = globals()[tbn_]
        if tbn_ not in keep_tb_:
            keep_tb_[tbn_] = tab_.get(src_[0])
        tab_[src_[0]] = v_
    # "tables": {TABLE: rows}: alias-only entries for per-track tables, used during its build only: a list table gets the
    # rows appended to the source's list, a dict table its keys set over the source's (keys as strings when the source's
    # keys are, as in the json tables); e.g. levels fitted on the alias's own render
    for tbn_, rows_ in as_.get("tables", {}).items():
        tab_ = globals()[tbn_]
        if tbn_ not in keep_tb_:
            keep_tb_[tbn_] = tab_.get(src_[0])
        cur_ = tab_.get(src_[0])
        if isinstance(rows_, dict):
            strk_ = cur_ is not None and any(isinstance(k_, str) for k_ in cur_)
            new_ = dict(cur_ or {})
            for k_, v_ in rows_.items():   # replace a source key of the same onset ("670" / "670.0" / 670.0)
                old_k_ = next((ok_ for ok_ in new_ if not str(ok_).startswith("_") and abs(float(ok_) - float(k_)) < 1e-6), None)
                new_.pop(old_k_, None)
                new_[str(k_) if strk_ else k_] = v_
            tab_[src_[0]] = new_
        else:
            tab_[src_[0]] = list(cur_ or []) + list(rows_)
    try:
        CUR_ALIAS = an_
        p_ = build_track(src_[0], src_[1], as_.get("patch", src_[2]), src_[3], src_[4])
    finally:
        CUR_ALIAS = None
        if keep_tw_ is None:
            TRACK_WINDOWS.pop(src_[0], None)
        else:
            TRACK_WINDOWS[src_[0]] = keep_tw_
        if keep_pt_ is not None:
            PITCH_TRIMS[src_[0]] = keep_pt_
        for tbn_, v_ in keep_tb_.items():
            if v_ is None:
                globals()[tbn_].pop(src_[0], None)
            else:
                globals()[tbn_][src_[0]] = v_
    # mvt1 c42 (critic C #1): alias key "hold_lanes": True: CC11 and CC1 keep their value at the alias's last note-off
    # (points from there on dropped). Both act on the voices (CC7-like, before the Opus hall), so a lane that follows the
    # source's later dynamics (here a sub. p) cuts the release voices of the alias's last note, which a player would
    # let ring; parts.json "lanes_held" [note-off, CC11 points dropped, CC1 points dropped]
    if as_.get("hold_lanes") and p_["notes"]:
        off_ = max(n_["qn"] + n_["dur"] for n_ in p_["notes"])
        dropped_ = []
        for ln_ in ("cc11", "cc1"):
            keep_ = [c_ for c_ in p_[ln_] if c_[0] < off_ - 1e-6]
            dropped_.append(len(p_[ln_]) - len(keep_))
            p_[ln_] = keep_
        p_["lanes_held"] = [round(off_, 4)] + dropped_
    p_["name"], p_["alias_of"] = an_, src_[0]
    parts.append(p_)
for p_ in parts:
    if p_["name"] in PASS2_TRACKS:
        p_["pass"] = 2
    if p_["name"] in TEST_TRACKS:   # mvt1 c41 (see the default)
        p_["test"] = True
json.dump({"tpb": TPB, "end_qn": END, "score_end": SE, "title": SCORE_TITLE, "preroll_qn": PREROLL_QN, "preroll_bpm": PREROLL_BPM, "tempo": tempo, "timesig": timesig, **({"ride_trims": [[[float(q_), float(d_)] for q_, d_ in r_] for r_ in RIDE_TRIMS]} if RIDE_TRIMS else {}), "tracks": parts}, open(OUT, "w"), indent=1)
for p in parts:
    print(f'{p["name"]:15s} notes={len(p["notes"]):4d} ks={len(p["ks"]):3d} cc11={len(p["cc11"]):4d} range={p["range"]} clash={p["ks_clash"]} {p["art_counts"]} leads={p["leads"]} notches={p["notches"]} uni_drop={p["unison_dropped"]} bloomv={p["bloomv"]} pitch_trim={p["pitch_trimmed"]} div_ent={p["div_entries"]} extra={p["extra_leads"]} bcsoft={p["bcsoft"]} hpgain={len(p["hpgain"])} hp_chain={p["hp_chained"]} bc_skip={p["bc_skipped"]} roles_chained={p["roles_chained"]} acc_db={p["accent_db"]}')
if hp_sf_targeted:   # mvt1 c38: HP_SF_TARGET hits (hairpin start, end), once per hairpin
    print(f"HP_SF_TARGET: {sorted(set(hp_sf_targeted))}", file=sys.stderr)
