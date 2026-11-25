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
DYN = {"ppp": 22, "pp": 34, "p": 46, "mp": 58, "mf": 72, "f": 88, "ff": 114, "fff": 124, "sf": 100, "sfz": 100, "fp": 46}
KS_LEAD = 0.06       # keyswitch lead in quarter notes when there is no rest before the note
# mvt2 c52 (critic A #1; EW's own template keyswitches 100-600 ms ahead): KS_ROWCHANGE_LEAD_S > 0 sends the keyswitch
# of a legato target whose row differs from the row of the one note it overlaps this many seconds before the target's
# note-on (default 0: the keyswitch stays 0.02-0.03 qn before it). The keyswitch never moves before the latest earlier
# note-on of the track (+ KS_ROWCHANGE_GUARD_QN), so the note still sounding keeps its own row. Tracks: by family
# (KS_ROWCHANGE_FAMILIES) and not in KS_ROWCHANGE_SKIP. parts.json "ks_rowchange": [target note-on qn, lead in ms]
KS_ROWCHANGE_LEAD_S = 0.0
KS_ROWCHANGE_GUARD_QN = 0.02
KS_ROWCHANGE_FAMILIES = ("string",)
KS_ROWCHANGE_SKIP = ()
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
# mvt2 c45 (ONE_TIME c45; EW-TEMPLATE-PLAN sections 7, 8 and 10, critics A #1 / B extra 2): phrase shapes, applied after
# every track is built (apply_phrase_shape). None = off. See build/score_config.py for movement II's values.
PHRASE_SHAPE = None
CC_GRID_QN = 0.0625   # mvt2 c45 (A #1): CC lane sampling grid (0.125 before c45); 69 ms at 54 bpm, about 14 points/s
# mvt2 c45 (critic A #2; HO manual p.106/p.144: velocity sets the legato transition speed; EW's HO template plays its KS
# Master legato rows at v76-95): legato-target velocity by printed dynamic for tracks whose name starts with a key (or
# whose family is a key): {key: (velocity-by-CC map, offset)}; sostenuto targets and the string rules keep theirs
LEG_VEL_BY_CC = {}
# mvt2 c45 (critic A #4): per-onset overrides of the WIND_REP_RETONGUE values {track: {score qn of the repeat: {...}}}
WIND_REP_RETONGUE_AT = {}
KS_LEAD_AT = {}   # mvt2 c54: per-onset keyswitch lead in qn (see build_track)
REP_GAP_AT = {}   # mvt2 c52: per-onset gap before a same-pitch repeat, any family (see build_track)
LEG_VEL_STRONG = {"string": (124, 124), "brass": (124, 124)}   # c03: legato-target velocity (<0.9 s, longer); v120 was 25-80 ms faster than v105
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
TIMP_LOUD_ATTACK_DB = 6.0   # c10 (B #2): f/ff timpani attacks measured 8-13 dB under the mix in 50-250 Hz   # c03 (B #1): two pp strokes measured about 6 dB under the one at qn 277
EPS = 1e-6
# c04 (C #6): breaths before the two tutti arrivals take time: seconds added in the 0.25 qn before the breath
CAESURA = {}
CAESURA_BREATH_QN = 0.12   # c19 (C #2): loud wind/brass breath gap where the breath has a CAESURA
# mvt2 c46 (critic A #1): at a caesura breath the gap is at least CAESURA_BREATH_S seconds (a short caesura switched the
# gap from 0.3 to 0.12 qn and left Horn 1's f breath 52 ms); CAESURA_BREATH_SKIP: breaths that keep CAESURA_BREATH_QN
CAESURA_BREATH_S = 0.0
CAESURA_BREATH_SKIP = set()
# mvt2 c51: CAESURA_BREATH_QN_AT = {breath qn: gap in qn}: the gap of one listed caesura breath (a breath whose caesura
# time was removed from the tempo map keeps its measured length in seconds)
CAESURA_BREATH_QN_AT = {}
# mvt2 c46 (critic A #3): {track: {target score qn: CC}}: a CC11 fall of CC over CAESURA_LIFT_S before the target's moved
# onset (the legato overlap is kept, so the join stays a bow change; CC11 is before the hall, so the room rings on)
CAESURA_LIFT = {}
CAESURA_LIFT_S = 0.25
# mvt2 c46 (ONE_TIME c46; EW-TEMPLATE-PLAN section 9, critic C #4): printed hairpins bent into a quadratic Bezier on the
# CC11 lane only (sampled into cc11 after every rule has read the linear curve, so no articulation decision moves):
# {"cresc": (cx, cy), "decresc": (cx, cy), "max_s": s, "skip_families": (...), "skip_spans": [(a, b)] (hairpins
# starting inside), "linear": {track: [(a, b)]} (hairpins starting inside stay linear)}. None = off.
HP_CURVE = None
# mvt2 c46 (critic C #6, S3): after a note-off followed by a rest of more than min_gap_qn, a volume-envelope fall of more
# than min_fall_db starts no earlier than s seconds after the note-off (the post-hall envelope cut the release tail)
VOL_TAIL_HOLD = None
# mvt2 c56 (critic A #2: re-bows of exposed soft held notes dip 8-12 dB, and two bows cannot overlap on one channel):
# TRACK_DOUBLES {idle track: {"src": track, "spans": [(q0, q1), ...], "cc7": 90, "art": "Sus MAX", "min_s": 1.2}}: every
# same-pitch chain of the source's held notes (its re-bow pieces) that starts inside a span is also played by the idle
# track (a divisi instance of the same section), with its bow changes at the midpoints of the source's pieces, so one
# of the two always sustains while the other changes bow. Both tracks play the span at CC7 "cc7" (90 = -3 dB, before
# the hall). The copy takes the source's CC11 / CC1 / CC15 / CC70 over the span, its own keyswitch to "art" before it
# and back after it, and its pieces are listed in its `rebows` (so REBOW_CC_LIFT reaches them). parts.json `doubles`.
TRACK_DOUBLES = {}
# mvt2 c56 (Dan's rule, 2026-11-11: no per-note track volume move; critics A #2-#5, C #3-#5): CC lane shapes, applied to
# the finished lanes of a track (after every other rule), so a level correction that used to be a fader shape can be
# written before the hall, on the instrument:
#   CC_SHAPES   {track: [(cc, [(score qn, d), ...])] or (cc, pts, "set")}: d is added to the lane between the first and
#               last point (linear between points, 0 outside); "set": the lane takes the values themselves.
#   CC_SHAPES_S {track: [(cc, score onset, [(seconds from the moved note-on, d), ...])]}: the same, keyed to a note.
#   REBOW_CC_LIFT {"cc", "s", "max_cc", "pre_fall", "pre_s", "families", "skip": {track: [qn]}, "skip_tracks", "only": {track: [qn]}}:
#               every re-bow piece (parts.json `rebows`) whose CC11 at the re-bow is max_cc or lower starts cc units over
#               the lane and returns to it over s seconds (a soft new bow on Sus MAX speaks slowly: stem dips of 7-12 dB
#               at pp once the fader fills were gone; CC11 is 0.6 dB per unit on soft strings); the old piece falls
#               pre_fall units over its last pre_s seconds.
# cc is 11, 1 or 7. Values are clamped to 1..127 and sampled on CC_GRID_QN. parts.json `cc_shapes` counts them.
#   SOFT_ENTRY_CC {"cc", "s", "max_cc", "min_s", "gap_s", "families", "rows"}: a fresh entry (a rest of gap_s seconds or
#               more before it; not a re-bow piece) of min_s seconds or more on one of the listed rows, at CC11 max_cc
#               or lower, starts cc units over the lane and returns over s seconds (soft first notes of the string
#               legato rows and Flautando speak 7-12 dB under their body for the first 0.35 s).
CC_SHAPES = {}
CC_SHAPES_S = {}
REBOW_CC_LIFT = None
SOFT_ENTRY_CC = None
ENV_TO_CC7 = {}   # mvt2 c57: {track: {"ref_db": R}} folds the whole volume envelope into the CC7 lane (see apply_env_to_cc7)
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
HP_REL = 1.0
# c06 (C #5): long-note swell in dB on top of the CC11 swell (+1.5 dB at 40%, 0 at 80%; -1.5 at the end of a phrase)
SWELL_DB = 1.5
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
# mvt2 c28: rows (substrings of the articulation name) that take the entry lead after a rest; a row tested with
# ART_SPANS (e.g. "Detache") must be listed here or its notes start on the score onset with no lead
ENTRY_LEAD_ROWS = ("Sus", "Leg Slur", "Flautando", "Tremolo")
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
NOTCH_SKIP = {}
# c09 (A #2): role spans that meet (B starts within ROLE_CHAIN qn of A's end) crossfade over [B.a - 0.1, B.a + 0.15]
# instead of ramping A out and B in on their own 0.5 qn ramps (both were at full value at the shared qn)
ROLE_CHAIN = 0.5
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
# mvt2 c53 (critic B #1): JOIN_NOTCH_S {track: {score onset: (from s, to s, dB), {"shape": [[s, dB], ...]} (exact
# breakpoints, first and last 0 dB; positive values fill the hole after a burst), or a list of both kinds (added)}}: the same notch keyed
# by the target note's score onset, its window in seconds from that note's MOVED note-on, so the window follows every
# later lead change (a JOIN_NOTCH window in absolute qn went stale when the tempo map and the leads changed: celli 68.5
# -3.9 dB at the peak instead of -8). Ramps JOIN_NOTCH_RAMP_S outside the window. Default: none
JOIN_NOTCH_S = {}
JOIN_NOTCH_RAMP_S = 0.04
# mvt2 c55 (Dan, 2026-11-11: "volume ... adjusted in large peaks and valleys on so many individual notes"; critics A, B, C).
# Every volume-envelope item carries a tag "class:layer" (vol_add). Classes: slow (roles, hairpin gains, timpani roll
# rules, chord cut, final fade), level (one value per note: pitch / note / row trims, plateau rows), shape (moves inside
# a note: fills, notches, accents, dips, fitted start shapes). LEVEL_SHAPES / LEVEL_SHAPES_S / level_fits rows are
# classed by form (row_class: 3 or more onsets inside or over 6 s = slow; a plateau over 70 % of its span = level; else
# shape), or by ENV_ROW_CLASS {track: [(from qn, to qn, class)]} for rows inside a listed span.
# ENV_CLASS {class: mode} and ENV_LAYER {layer or "Track:layer": mode} switch them: "on", "off", or "capN" (the summed
# items' deviation from their mean over each note is clipped to +-N dB; an absolute clip broke lines whose rows carry
# level, critic C #2). Environment for test builds: STP_ENV_CLASS="shape=cap3,level=on", STP_ENV_LAYER="early_fill=off".
# parts.json: `vol_cls` {"level": lane, "shape": lane} (step lanes like vol_db; slow = vol_db minus both, before the
# phrase arch and tail holds), `vol_tags` {tag: items}, `env_off` / `env_capped` (items per tag).
ENV_CLASS = {"slow": "on", "level": "on", "shape": "on"}
ENV_LAYER = {}
ENV_ROW_CLASS = {}
ROLE_NOTE_MIN = 0
# VOL_GRID_QN: the grid vol_db is sampled on besides the items' breakpoints (0.25 = before c55: slow ramps were written as
# 0.25 qn stairs, because build_reaper.py samples the step lane on 0.125 qn). VOL_BP_ALL True: every "env" item's
# breakpoints go to vol_bp (before: only items flagged exact; the others were moved up to 0.125 qn by the grid, so a
# shape meant to be up on the beat was 2 dB or more lower there at 155 of 392 start-shaped notes, critic A #4).
VOL_GRID_QN = 0.25
VOL_BP_ALL = False
VOL_BP_ALL_SKIP = ()   # families left on the old rule (the timpani roll rules abut with 0.03 qn gaps made for the grid:
#                        written exactly, seven roll joins got a 5-9 dB cut 15-125 ms long, simulated in c55)
# TRIM_KEY "score": level trims (pitch trims, note trims) change over one window per join, [the next note's SCORE onset
# - TRIM_XFADE_S / 2, + TRIM_XFADE_S / 2]: the old note's trim ends and the new note's starts there, so two trimmed
# neighbours make one segment from the old value to the new (no return to 0 dB between them) and the old note keeps its
# level to the beat. Before ("moved"): the old trim ended at the next MOVED note-on (the legato lead, 140-350 ms before
# the beat) and the new one ramped over 0.25 qn / 0.6 s inside the note (67 led joins: the old note's last 140 ms 2.0 dB
# under its body; 85 joined pairs swung towards 0 dB across the join, critic A #1). Detached notes closer than
# TRIM_HOLD_GAP_S share a window just before the later note's moved onset; a first note after a longer rest is up
# TRIM_PRE_S before its moved onset. TRIM_RAMP_KEEP {track: [score onsets]}: listed notes keep the old ramp in.
TRIM_KEY = "moved"
TRIM_XFADE_S = 0.08
TRIM_HOLD_GAP_S = 0.5
TRIM_PRE_S = 0.02
TRIM_RAMP_KEEP = {}
TRIM_BODY_EQUIV = True
TRIM_RAMP_KEEP_FITTED = False
TRIM_RISE_LEAD = 0.0
FILL_PRE_KEEP_SUM = 8.0   # dB ceiling of a corrected fill before the beat; None = off
# REBOW_FILL_SPLIT (dB or None): a re-bow fill list whose time-weighted median is at least this far from 0 dB is written
# as two items, its median (class level, layer rebow_level: 48 of movement II's 80 lists carry 2 dB or more of level, up
# to +7.4) and the rest (class shape), so that the shape switch does not move the balance. parts.json `rebow_levels`.
REBOW_FILL_SPLIT = None
# LEVEL_ROW_SPLIT (dB or None): the same for LEVEL_SHAPES / LEVEL_SHAPES_S / level_fits rows of class shape (critic C #3:
# the c52b / c53 rows carry body level, the celli fall 4.6 dB in bars 79-82 without them). parts.json `row_levels`.
LEVEL_ROW_SPLIT = None
# START_SHAPE_CAP {"db": 6.0, "pre_s": 0.15, "post_s": 0.6, "skip_layers": [...], "skip": {track: [score onsets]}}: the
# summed shape-class items (without skip_layers) are clipped at +db over each note start (parts.json `start_capped`
# [[onset, peak before]]). None = off.
START_SHAPE_CAP = None
# c23 (A #4): untied repeated pp notes that wind players re-tongue: the note before ends 0.06 qn early (the legato-repeat
# gap; the 0.03 qn default gap dipped 0-1.4 dB, filled by the release tail and the hall). {track: [score onsets of the repeat]}
# c24 (C #2c): per-onset CC11 depth of a merged-repeat bow-change notch (default 8/10/14 CC). Violoncellos 148: the
# printed mf arrival of the bar 46-47 oboe/cello unison; the 14 CC dip took about 3 dB off the mf downbeat
MERGE_NOTCH_AT = {}
# mvt2 c36 (critic A #3): {track: [score onsets]}: a listed note that absorbs the next slur's same-pitch first note keeps
# its own slur (it stays its slur's legato target; the bow change is the merge notch at the absorbed onset). Default: the
# merged note takes the absorbed note's slur and starts the new slur unled (v600 violas 248, 252.5)
MERGE_JOIN_OWN_SLUR_AT = {}
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
# mvt2 v600 port (c27): held tremolo notes are not re-bowed (the re-bow row is a sustain; mvt2/v600 has 4 qn string
# tremolos at the Largamente, bars 61-64, about 4.5-5 s long). False = the movement I behaviour
AUTO_REBOW_SKIP_TREM = True
# mvt2 c31: {track: [score onsets]} that the automatic re-bow leaves in one bow (listed REBOW_AT points still split them)
AUTO_REBOW_SKIP = {}
# mvt2 v600 port (c27): a held note on a non-legato sustain row other than REBOW_ART (Flautando: v600's sul tasto chords,
# bars 37-40) is re-bowed on its own row, so the re-bow keeps the colour (with REBOW_ART the sul tasto turned ordinario
# at every re-bow). Legato rows still hand over to REBOW_ART (a same-pitch re-attack on Leg Slur plays the slow layer)
REBOW_SAME_ROWS = ("Flautando",)
# mvt2 c34 (critic C #3): {track: row} the listed REBOW_AT points of that track re-attack on (default REBOW_ART), e.g. a
# held wind pedal split into breaths on its own sustain row ("Sus Non Vib") to break the sample loop's colour cycle
REBOW_ART_BY = {}
# mvt1 c04 (critic A #1): written-out unslurred repeated string notes in a fast tempo are separate strokes (build_track)
REP_SPLIT = {"max_qn": 1.5, "min_bpm": 100.0, "stac_s": 0.2,
             "stac_vel": [(34, 56), (46, 64), (58, 72), (72, 80), (88, 96), (114, 110), (124, 118)]}
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
# mvt2 c31 (critics A #1, B #1): per-track-prefix CC1 maps for CC1_DYN_TRACKS (first matching prefix wins; default
# CC1_DYN_MAP). On the 1FH/2FH KS Masters the legato transition groups (TLeg) are near full (rescaler 0.8-0.9) at CC1
# 30-46 and fall to 0.44 at 70, while the soft sustain layers are much quieter: at CC1 28-54 legato targets played the
# transition 6-13 dB over the sustain that followed (the note collapsed about 0.4 s in); at CC1 64-72 they were flat
CC1_DYN_MAP_BY = {}
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
# mvt2 c37 (critic A #1): {track: [score onsets]}: these slurred wind repeats are not merged (the repeat is played as its
# own note, e.g. on a repetition row via ART_SPANS: a CC11 notch does not show through a flute's vibrato)
WIND_SLUR_REP_MERGE_SKIP = {}
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
# mvt2 v600 port (c27): "4 soli" / "soli" on a string part (a few desks of the section, e.g. Cb 220-238 and 286-304,
# Vc 274-286 in mvt2/v600) reads like "metà": META_DB until "tutti"/"unis."/"div."
SOLI_AS_META = True
# mvt2 c33 (A #4, C #5): tracks whose patch already is a half section (DIV A/B KS Masters) ignore "metà"/"soli": the
# patch has the smaller group's sound and level, so the META_DB cut would count the halving twice
META_SKIP_TRACKS = set()
# mvt1 c06 (critic A #1): listed string notes {track: [score qn]} (printed down-bows that LilyPond's line joins as legato,
# e.g. the fff downbeat after a caesura) are fresh Sus MAX strokes: the c06 Leg -> Sus entry path (entry lead, velocity
# 105 or more, the legato note before it cut at the keyswitch); the next note joins from the stroke as a Leg BC MAX
# legato target (as SHORT_SUS_JOIN). On c05 the fff downbeat played a Leg BC transition that sagged 6-7 dB at the beat.
DOWNBOW_STROKE_AT = {}
# mvt2 c40 (critic A #1): BC_NEWP_KEEP = {track: [score qn]}: a "tutti"/"solo" text at these onsets does not stop the
# bow-change legato join (c09's different-players rule). Movement II bar 25: "tutti, con sord." marks only the leader
# rejoining a section that was already playing, and the skipped join put Violins I's C5 on the slow first-note layer
# (body - 6 dB at +0.32 s against Violins II's -0.02 s)
BC_NEWP_KEEP = {}
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
# mvt1 c34 (critic B #1): hairpins printed once on a shared staff that the extraction gives to one voice only, or that
# a track needs added: {track: [(start qn, stop qn, "cresc" | "decresc")]}, read by base_points like printed hairpins
SHARED_HP = {}
FP_SPIKE = ("f", 0.12, 0.25)   # mvt1 c11 (A #5): fp = (dynamic of the attack, held to qn, at p by qn)
# mvt2 c48, ported from mvt3 c09 (critic A #1; mvt3/reaper-v600/tools/score_to_parts.py, unedited there):
# FP_SPIKE_AT_MARK = True: an fp attack level starts at the mark (a step at the score onset) instead of 0.02 qn after it.
# Led notes take the CC at their score onset from their moved note-on (pulls), so with the ramp every led fp note started
# on the p layer and swelled into the f. A hairpin printed at the fp then starts where the attack has fallen (fp_hp in
# base_points), or its own points at the mark would overwrite the step. FP_VEL: the notes starting at an fp mark take at
# least this velocity (short and velocity-sensitive rows only; the KS Master sustain rows ignore velocity, DIGEST §2).
# False / None = the earlier behaviour
FP_SPIKE_AT_MARK, FP_VEL = False, None
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
# mvt2 c49 (critic A #1): RR_RESET_AT {track: [qn, ...]}: extra round-robin reset points inside the music (lane "cc36",
# sent on build_reaper's RR_RESET_CC). For a row with few takes whose alternation changed between renders on unchanged
# data (the Violas' Detache eighths, c47 -> c48): a reset between the last note of the row before and the row's
# keyswitch makes the take order depend only on the notes after it
RR_RESET_AT = {}
# mvt1 c06 (critic C #2a): phrase-top pitch contours (PT_*) are off inside every crescendo, not only inside soft lead
# hairpins (a descending line under an mf < lost 3 dB to the contour, against the hairpin)
PT_OFF_IN_CRESC = True
# mvt1 c06 (critic A #5, test): slurred, monophonic, non-first string notes of SHORT_SUS_LEG_S seconds (min, max) on the
# listed tracks stay on Leg Slur MAX as legato targets instead of Sus MAX (short_sus), unless their own pitch follows
# in the slur (the SLUR_REP_MERGE_SUS case)
SHORT_SUS_LEG_TRACKS, SHORT_SUS_LEG_S = (), (0.20, 0.25)
# mvt1 c07 (critic A #6): per-onset exceptions to SHORT_SUS_LEG_TRACKS {track: [score qn]}: these notes stay Sus MAX
SHORT_SUS_LEG_SKIP = {}
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
# mvt2 c50 (critic A #5): SLUR_JOIN_LEAD_AT = {track: {score onset: seconds}}: with SLUR_START_SUS, PICKUP_SUS and
# PORTATO_TAIL_JOIN off, the note after a `slur_start_sus` note (TIED_SLUR_SUS_WINDS: a wind/brass slur that starts on
# a tied continuation) had no lead branch: Horn 4 268 read +110 ms (pcX) / +170 ms (crossover) in c47-c49. A listed
# onset gets this lead (at most 0.45 of the first note) and keeps its velocity; unlisted notes are unchanged
SLUR_JOIN_LEAD_AT = {}
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
RETONGUE_LEAD_CAP = 0.3
# mvt1 c19 (critic C #2): a "string" entry in RETONGUE_LEAD_S (or a string track key) extends the re-tongue lead to
# string notes on the plain "Sus MAX" row after a played gap under 0.5 qn (fresh strokes after a slur, detached accented
# strokes), except written-out repeated strokes (REP_SPLIT / MEAS_TREM), STR_SHORT_AFTER_SUS stroke runs, notes the automatic re-bow
# splits or that follow such a note, and the Leg -> Sus entry path (a Leg note ending within 0.1 qn). Unled Sus MAX
# string notes arrived +0.09..+0.12 s (sample only) against +0.004 for led string notes
# mvt1 c19 (critic C #4): extra re-tongue lead by articulation, {track or family: {art: s}} (by_name), added to
# RETONGUE_LEAD_S (Oboe 1's Leg Slur re-attacks after slur breaks landed +0.21..+0.23 s)
RETONGUE_LEAD_ART_S = {}
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
# mvt2 c35 (critic C #1): a re-attack straight after the previous note (its written end within 0.10 qn of the onset;
# a new slur after the slur-break gap, a row change, a wide leap, a tutti re-entry) that no other lead branch moved
# plays the slow first-note layer on time and reached body - 6 dB 0.15-0.37 s late. REATTACK_LEAD_AT = {track: {score
# onset: seconds}} starts listed notes that many seconds early (replacing a smaller lead), REATTACK_LEAD_S = {family:
# seconds} every such note at a new pitch of at least REATTACK_MIN_S that has no lead (default off); the lead is at most
# 0.45 of the previous note's played slot, and the notes before end 0.02 qn before the moved onset (the re-attack is
# kept). CC11 holds the note's level from its moved onset. parts.json `reattack_leads`
REATTACK_LEAD_AT, REATTACK_LEAD_S, REATTACK_MIN_S = {}, {}, 0.4
# mvt2 c43 (critic C #4): a wind/brass slur that starts on the tied continuation of a note outside any slur makes that
# note slur_start_sus (it overlaps the slur's next note by LEG_OVERLAP and is joined as a legato transition). False = off
TIED_SLUR_SUS_WINDS = True
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
STR_REP_DETACH = None
# mvt1 c45 (critic B #1; mvt2 c40 port): a re-bow fill list holds its last value until the next list starts, but never
# into a later note: it ends at the end of the note its re-bow belongs to and reaches 0 dB this many seconds later
# (None: the old rule)
REBOW_FILL_END_S = 0.12
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
# mvt1 c45: it also takes the string re-tongue lead (RETONGUE_LEAD_S, or "sus_lead_s" seconds on tracks with none),
# the note before giving way so the gap is kept (c44 without a lead: perceived attack +94 ms median over 23 repeats).
# mvt2 c40 (critic A #2): "sus_cc_by" {track: CC} replaces "stroke_cc" in the "sus_min_s" test for that track (the
# basses' pp-p Sus MAX repeats, which a 0.06 qn gap and a CC7 fall did not open in c39).
# mvt2 c41: "sus_fall" {track: {"cc", "s", "max_cc"}}: those repeats at max_cc or softer also get a CC11 fall of cc over
# the note before's last s seconds (a longer release cap refills the gap). mvt2 c42: also before soft STR_REP_NEW_BOW
# strokes and portato strokes (replacing a smaller portato fall).
# mvt2 c44 (critic A #1, Dan's S1; EW-TEMPLATE-PLAN section 8 repeat gaps 60-100 ms): "soft_gap_s" (seconds, optional):
# the gap before a "soft" repeat's re-bow piece (a point from `rep_rebows` that is not a listed REBOW_AT point; loop
# re-bows keep REBOW_GAP_QN 0.03 qn, about 35 ms, at which 13 of 27 printed repeats dipped under 3 dB in their own band),
# with a CC11 fall into the gap: the track's "sus_fall" spec, else "soft_fall" {"cc", "s", "max_cc"}. "loud_gap_s"
# (optional): "soft_gap_at" {track: [qn]} adds listed REBOW_AT points that are printed repeats. mvt2 c49 (finale
# technique 21: a repeat that starts a new bow needs a longer gap than a repeat inside one bow): "soft_gap_s_at"
# {track: {qn: seconds}} gives a listed point its own gap (default: none, every point uses "soft_gap_s"). "loud_gap_s"
# (optional): the gap of a non-portato stroke or a "sus_min_s" repeat at "loud_cc" (default CC 72) or louder (a loud
# release fills a 0.06 s gap: basses 265 f dipped -0.8 dB), with a "loud_fall_cc" CC11 fall (default 6) over "s" seconds
# parts.json `rep_strokes` [[score onset, class]], `rep_rebows` [score onset], `rep_sus_gaps`. None = off (the c05-c43 merge)
# mvt2 c40 (ONE_TIME #3): ported from mvt1 c44/c45; "sus_lead_s" is also the stroke lead when RETONGUE_LEAD_S
# has no value for the track (movement II sets none)
STR_REP_NEW_BOW = None
# mvt1 c23 (critic A #3): STAC_LEAD_S = {track: seconds} (exact track names): a string note on a row whose name starts
# "Stac" (printed staccato; not the REP_SPLIT / measured-tremolo strokes) starts that many seconds early; a previous
# note of the track that ends at or before the score onset (+0.05 qn) and would overlap the moved onset ends 0.02 qn
# before it; CC11 holds from the moved onset (pulls). The Violins I Stac RRx14 strokes reached -3 dB at +0.10 s and
# peaked at +0.13 s against +0.04..+0.07 s for the winds and the other strings. parts.json `stac_leads`
STAC_LEAD_S = {}
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
HP_GAIN_IN_WINDOW, HP_GAIN_IN_WINDOW_SKIP = True, ()   # mvt1 c35 (critic A #1): see hps_v in build_track
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
# mvt2 v600 port (c27): printed marks that are reached at once, as a "sub." mark, and are never a hairpin's target:
# {staff: [score qn]}. For a mark after a breath that starts a new phrase level, where the hairpin before it is a short
# dip from a crest (mvt2 v600 bar 58 b4: < to the crest, > into the breath, f at bar 59)
SUBITO_AT = {}
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
# mvt2 c49 (critic A #3): build/level_fits.json {track: {"score qn": [[seconds, dB], ...]}}: LEVEL_SHAPES_S entries fitted
# on a render by a script (the fills at the sul tasto pad's joins); keys starting with "_" are notes. No file: none
if __import__("os").path.exists(f"{BUILD}/level_fits.json"):
    for _t, _d in json.load(open(f"{BUILD}/level_fits.json")).items():
        if not _t.startswith("_"):
            LEVEL_SHAPES_S[_t] = LEVEL_SHAPES_S.get(_t, []) + [
                (float(_k), [(float(a_), float(b_)) for a_, b_ in _v])
                for _k, _v in sorted(((k_, v_) for k_, v_ in _d.items() if not k_.startswith("_")), key=lambda kv_: float(kv_[0]))]
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
        anchors.append((e, vb + (vb - va) * (e - qb) / (qb - qa)))

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
# mvt2 c46 (critic C #1, tool step a): the depths read the score config when it sets them (they were overwritten here)
PHRASE_PUSH, PHRASE_SLOW = globals().get("PHRASE_PUSH", 1.015), globals().get("PHRASE_SLOW", (0.96, 0.92))
PHRASE_SLOW_SUB = globals().get("PHRASE_SLOW_SUB", (0.98, 0.95))
PHRASE_SLOW_MAIN, PHRASE_RETURN = globals().get("PHRASE_SLOW_MAIN", (0.95, 0.88)), globals().get("PHRASE_RETURN", 0.97)
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
        if any(abs(e - a2) < 0.01 for a2, e2, _ in RAMP_SPANS):
            # mvt1 c07 (critic C #4): an arc that ends where a printed rit. ramp starts slows its last beats and the
            # ramp then starts from its own (faster) tempo: check that no beat is slower than the beat after it
            print(f"  WARNING phrase arc {a}-{e} ends where a tempo ramp starts: check the tempo does not rise", file=sys.stderr)
        mid = (a + e) / 2
        slow = PHRASE_SLOW_SUB if depth == "sub" else (PHRASE_SLOW_MAIN if depth == "main" else PHRASE_SLOW)
        if depth == "open":   # mvt1 c11 (critic C #1): the push only, no slowing (an arc that leads into an animando)
            slow = (1.0, 1.0)
        push = 1.0 if depth == "sub" else PHRASE_PUSH
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
APEX_AGOGIC = globals().get("APEX_AGOGIC", 0.96)   # mvt2 c46 (critic C #1): config-settable
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
        ns_ = [x for x in ns_ if tw_keep(tn, x[0])]
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
for _st, _qs in SUBITO_AT.items():   # mvt2 v600 port (c27)
    SUBITO[_st].update(round(_q, 3) for _q in _qs)
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


FP_FALL_AT = {}   # mvt2 c48: {fp mark qn: qn where its attack has fallen to p} (FP_SPIKE_AT_MARK; filled by base_points)
_HP_SEGS = []   # mvt2 c46: (start qn, start CC, stop qn, target CC, kind, niente) of the last base_points call


def base_points(staff_list, extra_marks=(), extra_hps=(), niente=False):
    del _HP_SEGS[:]
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
    fp_hp = {}   # mvt2 c48 (from mvt3 c09): FP_SPIKE_AT_MARK: a hairpin printed at an fp starts where the attack has fallen
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
            if data == "fp" and FP_SPIKE:
                # mvt1 c11 (critic A #5): an fp is a short f attack falling to p (DYN["fp"] alone went straight to p:
                # the basses' fp at bar 33 had no attack and bloomed over the bassoon solo)
                hi_, hold_, fall_ = FP_SPIKE
                # mvt2 c48 (from mvt3 c09): FP_SPIKE_AT_MARK: the attack level starts at the mark itself (a step), so a
                # led note's pull (CC held from its moved note-on to the score onset) reads the attack level
                t0_ = q if FP_SPIKE_AT_MARK else q + 0.02
                pts += [(q, level), (t0_, max(DYN[hi_], level)), (q + hold_, max(DYN[hi_], level)), (q + fall_, DYN["fp"])]
                if FP_SPIKE_AT_MARK:
                    fp_hp[q] = q + fall_
                    FP_FALL_AT[round(q, 4)] = q + fall_
                level = DYN["fp"]
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
                hold_after = (stop - 0.01, stop + 1.0)
            elif hk == "cresc" and abs(tgt - level) < EPS:
                start = level - 12   # c06 (C #3): "niente <" to the current level starts 12 CC lower
            tgt = max(10, min(124, tgt))
            q = next((v for k, v in sf_hp.items() if k - EPS <= q <= k + 0.25), q)
            # mvt2 c48 (from mvt3 c09): "fp >": the hairpin starts from the p after the attack (its (q, level) points at
            # the mark would overwrite the attack step: value_at lets the later point at one qn win)
            q = next((v for k, v in fp_hp.items() if k - EPS <= q <= k + 0.25 and v < stop - EPS), q)
            pts += [(q, level), (q, max(10, start)), (stop, tgt)]
            _HP_SEGS.append((q, max(10, start), stop, tgt, hk, nien_ is not None))
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


def _leg_vel_map(tname, family):
    for k_, v_ in LEG_VEL_BY_CC.items():
        if tname.startswith(k_) or k_ == family:
            return v_
    return None


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
    # mvt2 c45 (critic A #1; EW-TEMPLATE-PLAN section 7, CC density 13-44 points/s): grid CC_GRID_QN (was 0.125 qn)
    grid = sorted(set([round(x, 4) for x in breaks] + [round(i * CC_GRID_QN, 4) for i in range(int((END + 4) / CC_GRID_QN))]))
    out, last = [], None
    for q in grid:
        v = int(round(max(1, min(127, fn(q)))))
        if v != last:
            out.append((q, v)); last = v
    return out


# ---------- per-track articulation ----------
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
            # mvt2 c33 (A #4, C #5): a window may be (from, to, lowest pitch) to override the split's lowest pitch
            insp_ = lambda n, w=wins_, p=pmin_: any(a_[0] - EPS <= n["qn"] < a_[1] - EPS and n["pitch"] >= (a_[2] if len(a_) > 2 else p)
                                                    for a_ in w)
        if tname == src_:
            split_away = [n for n in ns if insp_(n)]
        ns = [n for n in ns if insp_(n) == (tname == tsp_)]
    flag_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] == "flageolet"}
    if family == "harp":   # harmonics go to their own track
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
    # mvt2 v600 port (c27): a portato mark (-_ , louré) reads as a tenuto (v600 violas, bars 48-51 sotto voce eighths;
    # before, the script was not read at all)
    ten_q = {q for s in staves for q, k, v in ev[s] if k == "script" and v[0] in ("tenuto", "portato")}
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
    hp_segs = list(_HP_SEGS) if ns else []   # mvt2 c46 (HP_CURVE)

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
        elif TIED_SLUR_SUS_WINDS and family in ("wind", "brass") and n["slur"] is None:
            # mvt2 c43 (critic C #4): a wind/brass slur that starts on a tied continuation left the merged note outside
            # the slur, so it ended exactly at the slur's next onset (no overlap, no gap) and the KS Master joined or
            # re-attacked depending on event order (Horn 4 268 flipped between renders). Mark it slur_start_sus: it
            # overlaps the next note by LEG_OVERLAP and the KS Master joins it as a legato transition
            k_ = next((i_ for i_, (a_, b_) in enumerate(slurs) if q + 0.25 < a_ < n["end"] - EPS), None)
            if k_ is not None and not any(o is not n and o["qn"] < n["end"] - EPS and o["end"] > q + EPS for o in ns):
                n["slur_start_sus"] = True
                tie_slurred.append(round(q, 3))
        if family in ("harp", "harm"):
            n["art"] = None
            continue
        if family == "timp":
            n["art"] = ks_lookup(stem, "Timpani Flt Rls")[0] if q in trem_q else ks_lookup(stem, "Timpani Flt Lng")[0]
            continue
        if n.get("grace") or n.get("grace_target"):   # c03: the run and its target on one legato articulation
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
            continue
        sp_ = next((x_ for x_ in ART_SPANS.get(tname, []) if x_["from"] - EPS <= q < x_["to"] - EPS
                    and (x_.get("mark") != "staccato" or q in stacc_q)), None)
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
                    and not (tname in SHORT_SUS_LEG_TRACKS
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

    # mvt1 c44 (ONE_TIME #4, critics A #1-#2): STR_REP_NEW_BOW, see the default. In score order, so a repeat after a new
    # stroke sees the stroke as its predecessor (a soft repeat then merges into the stroke, a loud one is a stroke too)
    rep_strokes, rep_rebow_q, rep_sus_gaps = [], [], []
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
            if [x_ for x_ in ns if x_ is not o and -EPS < x_["qn"] - o["end"] < 0.1] != [n]:
                continue   # a chord or another onset follows: the merge loop leaves it too
            if not (_lg(o.get("art") or "") or o.get("rep_stroke")
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
                    st_ = dict(n, qn=sq_, art=ks_lookup(stem, "Timpani Flt Lng")[0], tie_stroke=True)
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
                        for tq, t in texts_until(staves, o["qn"])) \
                and not any(abs(o["qn"] - k_) < 0.02 for k_ in BC_NEWP_KEEP.get(tname, []))   # mvt2 c40 (A #1)
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
                if family == "wind" and any(abs(nxt[0]["qn"] - q_) < EPS for q_ in WIND_SLUR_REP_MERGE_SKIP.get(tname, [])):
                    i += 1
                    continue   # mvt2 c37: listed repeats stay separate notes
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
                    own_ = any(abs(q_ - n["qn"]) < EPS for q_ in MERGE_JOIN_OWN_SLUR_AT.get(tname, []))
                    if not (MERGE_KEEP_OWN_SLUR and o["slur"] is None and n["slur"] is not None) and not own_:
                        n["slur"] = o["slur"]   # joins onward as the dropped note did
                    # c32 (A #5): a slurred note merged with an unslurred same-pitch continuation (a tie out of the
                    # slur) keeps its own slur, so it is still the slur's legato target (v621 Vc bar 45: G( A-flat)~
                    # A-flat; the A-flat lost its slur and started unled on the slow first-note layer)
                    for o2 in ns:   # a later note bow-changed from the dropped one now joins from the merged note
                        if o2.get("bc_from") == id(o):
                            o2["bc_from"] = id(n)
                    if own_ and o["slur"] is not None:   # mvt2 c36: the absorbed note's slur still joins on from it
                        for o2 in ns:
                            if o2 is not o and o2.get("slur") == o["slur"] and o2["qn"] > o["qn"] + EPS \
                                    and o2.get("bc_from") is None and o2["pitch"] != n["pitch"]:
                                o2["bc_from"] = id(n)
                                break
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
    cc_falls = []   # c15 (A #6): (start, end, CC): CC11 falls to -CC at end, back to 0 over 0.3 qn
    # mvt2 c44 (critic A #1): STR_REP_NEW_BOW "soft_gap_s" points (see the default) and their CC11 fall into the gap
    soft_gap_pts = set()
    soft_gap_own = {}
    if STR_REP_NEW_BOW and STR_REP_NEW_BOW.get("soft_gap_s"):
        soft_gap_pts = {round(q_, 4) for q_ in rep_rebow_q
                        if not any(abs(q_ - l_) < 0.02 for l_ in REBOW_AT.get(tname, []))}
        # "soft_gap_at" {track: [score qn]}: listed REBOW_AT points that are printed repeats get the soft gap too
        soft_gap_pts |= {round(q_, 4) for q_ in (STR_REP_NEW_BOW.get("soft_gap_at") or {}).get(tname, [])}
        # mvt2 c49 (finale technique 21): "soft_gap_s_at" {track: {score qn: seconds}}: that point's own gap (the point
        # joins the soft gap points)
        soft_gap_own = {round(float(q_), 4): float(v_) for q_, v_ in ((STR_REP_NEW_BOW.get("soft_gap_s_at") or {}).get(tname) or {}).items()}
        soft_gap_pts |= set(soft_gap_own)
        spec_ = (STR_REP_NEW_BOW.get("sus_fall") or {}).get(tname) or STR_REP_NEW_BOW.get("soft_fall")
        for p_ in sorted(soft_gap_pts):
            if spec_ and base(p_) <= spec_.get("max_cc", 127) + EPS:
                fb_ = qn_before(p_, soft_gap_own.get(p_, STR_REP_NEW_BOW["soft_gap_s"]))
                cc_falls.append((qn_before(fb_, spec_.get("s", 0.06)), fb_, spec_["cc"], max(0.01, p_ - fb_)))
    timp_chain_skip = []   # mvt1 c07 (B #4)
    rep_retongued = []   # mvt1 c06 (A #2): onsets re-tongued by WIND_REP_RETONGUE (cc_falls rows carry their return)
    rep_gap_at = []
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
                cq_ = next((c_ for c_ in CAESURA if abs(e0 - c_) < 0.01), None)
                gap_ = 0.3 if cq_ is None else CAESURA_BREATH_QN_AT.get(cq_, CAESURA_BREATH_QN)   # mvt2 c51: per-breath gap
                if cq_ is not None and CAESURA_BREATH_S and not any(abs(e0 - c_) < 0.01 for c_ in CAESURA_BREATH_SKIP):
                    gap_ = max(gap_, lead_qn(e0, CAESURA_BREATH_S))   # mvt2 c46 (critic A #1)
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
        if n.get("detache_t"):
            n["end"] = e0 + 0.01   # c15 (A #5)
        elif same_pitch and any(abs(o0["qn"] - k_) < 0.02 for k_ in REP_GAP_AT.get(tname, {})):
            # mvt2 c52 (critic A #2, S1): REP_GAP_AT {track: {score qn of the repeat: {"gap_s", "fall_cc", "fall_s"}}}:
            # the note before a listed same-pitch repeat ends gap_s seconds before the repeat's score onset (at most
            # 40 % of its length; add the repeat's own lead to gap_s when it has one), with an optional CC11 fall of
            # fall_cc over its last fall_s seconds, back at the onset. Checked before every other same-pitch rule
            rg_ = next(v_ for k_, v_ in REP_GAP_AT[tname].items() if abs(o0["qn"] - k_) < 0.02)
            n["end"] = e0 - min(e0 - qn_before(e0, rg_["gap_s"]), 0.4 * dur)
            if rg_.get("fall_cc"):
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], rg_.get("fall_s", 0.10)))
                cc_falls.append((fa_, n["end"], rg_["fall_cc"], max(0.01, e0 - n["end"])))
            rep_gap_at.append(round(o0["qn"], 3))
        elif same_pitch and family == "string" and o0.get("rep_stroke") and STR_REP_NEW_BOW:
            # mvt1 c44 (ONE_TIME #4, critics A #1-#2): the note before a STR_REP_NEW_BOW stroke ends min(gap_s, frac x
            # its length) before the stroke's score onset; portato repeats add a CC11 fall over its last fall_s
            R_ = dict(STR_REP_NEW_BOW, **(STR_REP_NEW_BOW.get("portato") or {})) if o0["rep_stroke"] == "portato" \
                else STR_REP_NEW_BOW
            loud_ = (o0["rep_stroke"] != "portato" and STR_REP_NEW_BOW.get("loud_gap_s")
                     and base(o0["qn"]) >= STR_REP_NEW_BOW.get("loud_cc", 72) - EPS)   # mvt2 c44 (critic A #1b)
            g_s_ = max(R_["gap_s"], STR_REP_NEW_BOW["loud_gap_s"]) if loud_ else R_["gap_s"]
            n["end"] = e0 - min(e0 - qn_before(e0, g_s_), R_["frac"] * dur)
            fc_ = R_.get("fall_cc_loud", R_.get("fall_cc", 0)) if base(o0["qn"]) > 90 else R_.get("fall_cc", 0)
            fs_ = R_.get("fall_s", 0.04)
            if loud_ and STR_REP_NEW_BOW.get("loud_fall_cc", 6) > fc_:
                fc_, fs_ = STR_REP_NEW_BOW.get("loud_fall_cc", 6), STR_REP_NEW_BOW.get("loud_fall_s", 0.06)
            sf_ = (STR_REP_NEW_BOW.get("sus_fall") or {}).get(tname)
            if sf_ and base(o0["qn"]) <= sf_.get("max_cc", 127) + EPS and sf_["cc"] > fc_:
                # mvt2 c42 (critics A #2-#3, C #2b): "sus_fall" also reaches soft strokes and portato strokes (the
                # longer pp/p release caps refill their gaps); it replaces a smaller portato fall
                fc_, fs_ = sf_["cc"], sf_.get("s", 0.06)
            if fc_:
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], fs_))
                cc_falls.append((fa_, n["end"], fc_, max(0.01, e0 - n["end"])))
        elif n.get("rep_stroke") and not same_pitch and len(nxt) == 1 and _lg((o0.get("art") or "")) \
                and (same_slur(n, o0) or o0.get("bc_from") == id(n)):
            # mvt2 c40: a STR_REP_NEW_BOW stroke joins the next note of its slur as a legato transition (the
            # DOWNBOW_STROKE_AT branch below), also when it carries a tenuto (the tenuto branch caught Violins II's
            # louré slur heads 45/51 and left the slur's second note unled on the first-note layer)
            n["end"] = e0 + LEG_OVERLAP
            o0["leg_target"] = True
            o0["leg_prev"] = n
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
                and not (TENUTO_HEAD_LEGATO and leg_join and same_slur(n, o0)):
            # c03 (A #3): tenuto = full value with weight. Basses 0.02 qn; winds/brass a light re-tongue at mf or louder
            # or under "sostenuto"; 0.06 qn at p and softer
            if family == "string":
                n["end"] = e0 - (0.02 if stem.startswith("Basses") else min(0.06, 0.15 * dur))
            elif base(n["qn"]) >= DYN["mf"] - 2 or text_state(n["qn"], ["sostenuto"], ["a tempo", "tempo i"]):
                n["end"] = e0 - min(0.03, 0.1 * dur)
            else:
                n["end"] = e0 - min(0.06, 0.15 * dur)
        elif n.get("short_sus") and not same_pitch:
            n["end"] = e0 + 0.03   # c03: polyphonic Sus MAX, so the overlap is a crossfade
            if family == "string" and base(n["qn"]) >= SHORT_SUS_DETACH["min_cc"] \
                    and qn_to_sec(e0) - qn_to_sec(n["qn"]) < SHORT_SUS_DETACH["max_s"] and nxt:
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
                and base(o0["qn"]) >= (STR_REP_NEW_BOW.get("sus_cc_by") or {}).get(tname, STR_REP_NEW_BOW["stroke_cc"]) - EPS \
                and qn_to_sec(orig_end[id(o0)]) - qn_to_sec(o0["qn"]) >= STR_REP_NEW_BOW["sus_min_s"] - EPS \
                and not any(sp_[0] - EPS <= o0["qn"] < sp_[1] - EPS
                            for sp_ in ((STR_REP_DETACH or {}).get("at") or {}).get(tname, [])):
            # mvt1 c44 (critic A #2, scope): an unslurred same-pitch Sus MAX repeat at "stroke_cc" or louder, lasting
            # "sus_min_s" or more (REP_SPLIT strokes included), is a new bow with the STR_REP_NEW_BOW gap (it kept
            # min(0.03 qn, 10%) or min(0.04 qn, 10%): 85 such repeats dipped a median 3.5 dB in the stem, 2.3 in the
            # master). Not inside STR_REP_DETACH spans
            loud_ = STR_REP_NEW_BOW.get("loud_gap_s") and base(o0["qn"]) >= STR_REP_NEW_BOW.get("loud_cc", 72) - EPS
            g_s_ = max(STR_REP_NEW_BOW["gap_s"], STR_REP_NEW_BOW["loud_gap_s"]) if loud_ else STR_REP_NEW_BOW["gap_s"]
            n["end"] = e0 - min(e0 - qn_before(e0, g_s_), STR_REP_NEW_BOW["frac"] * dur)
            rep_sus_gaps.append(round(o0["qn"], 3))
            o0["rep_sus_gap"] = True   # mvt1 c45 (critic A #1): it takes the string re-tongue lead (retongue_ok)
            sf_ = (STR_REP_NEW_BOW.get("sus_fall") or {}).get(tname)
            if loud_ and STR_REP_NEW_BOW.get("loud_fall_cc", 6):
                # mvt2 c44 (critic A #1b): a loud repeat's fall into its loud_gap_s gap (no max_cc)
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], STR_REP_NEW_BOW.get("loud_fall_s", 0.06)))
                cc_falls.append((fa_, n["end"], STR_REP_NEW_BOW.get("loud_fall_cc", 6), max(0.01, e0 - n["end"])))
            elif sf_ and base(o0["qn"]) <= sf_.get("max_cc", 127) + EPS:
                # mvt2 c41 (critic A #1 watch): "sus_fall" {track: {cc, s, max_cc}}: a CC11 fall of cc over the note
                # before's last s seconds, back at the repeat (pre-hall, on the releasing voice: a longer release cap
                # refills a 0.06 s gap)
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], sf_.get("s", 0.06)))
                cc_falls.append((fa_, n["end"], sf_["cc"], max(0.01, e0 - n["end"])))
        elif n.get("rep_stac"):
            n["end"] = e0 - 0.02   # mvt1 c04 (A #1): written length minus 0.02 qn
        elif n.get("rep_sus") or n.get("short_stroke"):
            n["end"] = e0 - min(0.04, 0.1 * dur)   # mvt1 c04 (A #1): a short bow change before the next stroke
        elif same_pitch and any(abs(o0["qn"] - r_) < 0.02 for r_ in REP_RETONGUE_AT.get(tname, [])):
            n["end"] = e0 - min(0.06, 0.15 * dur)   # c23 (A #4): a listed untied repeat is re-tongued audibly
        elif same_pitch and WIND_REP_RETONGUE and family in ("wind", "brass") \
                and (not is_leg or (WIND_REP_AFTER_SLUR and n["slur"] is not None)) \
                and not (n["slur"] is not None and o0.get("slur") == n["slur"]
                         and not (WIND_REP_PORTATO and near(o0["qn"], ten_q) and not o0.get("sost")
                                  and not o0.get("sost_rep") and not o0.get("portato_join"))):
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
            R_.update(next((v_ for k_, v_ in WIND_REP_RETONGUE_AT.get(tname, {}).items()
                            if abs(o0["qn"] - k_) < 0.02), {}))   # mvt2 c45 (A #4)
            if WIND_REP_RETONGUE_SHORT and dur <= WIND_REP_RETONGUE_SHORT["max_qn"] + EPS \
                    and gate_bpm(n["qn"]) >= WIND_REP_RETONGUE_SHORT["min_bpm"] - EPS:
                R_.update({k_: v_ for k_, v_ in WIND_REP_RETONGUE_SHORT.items() if k_ not in ("max_qn", "min_bpm")})
            n["end"] = e0 - min(e0 - qn_before(e0, R_["gap_s"]), R_["frac"] * dur)
            if R_.get("fall_cc"):
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], R_["fall_s"]))
                cc_falls.append((fa_, n["end"], R_["fall_cc"], max(0.01, e0 - n["end"])))
            rep_retongued.append(round(o0["qn"], 3))
        elif same_pitch:
            n["end"] = e0 - (min(0.06, 0.15 * dur) if is_leg else min(0.03, 0.1 * dur))
            sf_ = ((STR_REP_NEW_BOW or {}).get("sus_fall") or {}).get(tname) \
                if family == "string" and o0.get("down_stroke") and not o0.get("rep_stroke") else None
            if sf_ and base(o0["qn"]) <= sf_.get("max_cc", 127) + EPS:
                # mvt2 c43 (critic A #3): a same-pitch DOWNBOW_STROKE_AT stroke (not a STR_REP_NEW_BOW stroke) after a
                # legato note also gets the "sus_fall" CC11 fall over the note before's last s seconds (Violoncellos 66
                # re-attacked with no gap or fall: stem dip 2.9 dB)
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], sf_.get("s", 0.06)))
                cc_falls.append((fa_, n["end"], sf_["cc"], max(0.01, e0 - n["end"])))
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
    for n in ns:
        sec = qn_to_sec(n.get("vel_end", orig_end[id(n)])) - qn_to_sec(n["qn"])   # mvt1 c05: vel_end (A #1 merges)
        if n.get("grace"):
            n["vel"] = 127
        elif n.get("leg_target"):   # legato patches: velocity sets transition speed (HO manual 2.1.1); loudness is CC11
            if family == "string" and n["qn"] >= CODA_SOFT["from_qn"] and base(n["qn"]) <= CODA_SOFT["max_cc"]:
                n["vel"] = CODA_SOFT["vel"]   # c08 (C #4): soft coda joins, not the v124 bump
            elif family == "string" and in_sost(n["qn"]):
                n["vel"] = SOST_STR_LEG_VEL   # c10 (C #4d): broad Largamente joins, no 17-19 dB transition peaks
            elif _leg_vel_map(tname, family) and not n.get("sost"):   # mvt2 c45 (A #2): by printed dynamic
                m_, off_ = _leg_vel_map(tname, family)
                v_ = int(round(value_at(m_, base(n["qn"])))) + off_
                if tname == "Cor anglais":   # its c04 values where higher
                    v_ = max(v_, 100 if sec < 0.45 else (90 if sec < 0.9 else 80))
                n["vel"] = max(1, min(127, v_))
            elif family in LEG_VEL_STRONG:   # c02: strings/horns arrived 220-385 ms late at v60-100
                n["vel"] = LEG_VEL_STRONG[family][0] if sec < 0.9 else LEG_VEL_STRONG[family][1]
            elif n.get("sost"):   # c07 (A #1): broad ff portato joins: a firm, quick transition
                n["vel"] = SOST_VEL
            elif tname == "Cor anglais":   # c04 (A #5): its v60/v80 transitions measured 150-185 ms
                n["vel"] = 100 if sec < 0.45 else (90 if sec < 0.9 else 80)
            else:
                n["vel"] = 100 if sec < 0.45 else (80 if sec < 0.9 else 60)
        if family in ("harp", "harm"):   # the harp is velocity-driven; CC11 stays constant (c01)
            v = base(n["qn"])
            n["vel"] = int(round(value_at([(22, 46), (34, 52), (46, 64), (58, 76), (72, 90), (88, 100), (104, 110), (118, 118)], v)))
            if family == "harp" and arp_top(n):   # c04 (A #1): the top note of a rolled chord carries the line
                n["vel"] = min(127, n["vel"] + 4)
            elif family == "harp" and n["pitch"] in HARP_PITCH_VEL:   # c09 (A #6): even out the sample set by pitch
                n["vel"] = max(1, min(127, n["vel"] + HARP_PITCH_VEL[n["pitch"]]))
            if family == "harm":
                n["vel"] -= HARM_VEL_CUT
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
        if FP_VEL and not n.get("leg_target") and any(abs(n["qn"] - q) < 0.01 and d == "fp" for q, d in marks):
            n["vel"] = max(n["vel"], FP_VEL)   # mvt2 c48 (from mvt3 c09): the fp's f attack on velocity-sensitive rows
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

    # keyswitches at articulation changes; the patch state already selects the first one
    ks, cur, first_art = [], None, None
    for n in ns:
        a = n.get("art")
        if a is None or a == cur:
            continue
        key = ks_lookup(stem, a)[1]
        if first_art is None:
            first_art = a
            # c03 (A #4): Tbn1's first two accents played Sus MAX although the state selects Sus Accent MAX; tracks that
            # enter after the start also send their first keyswitch, in the rest before the entry
            if n["qn"] >= 0.5:
                ks.append({"qn": round(early_time(n["qn"]), 4), "pitch": key, "art": a, "note": n})
        else:
            # mvt2 c54 (critic A #1): KS_LEAD_AT {track: {score qn: lead in qn}}: the keyswitch of a listed note this
            # close before it instead of KS_LEAD. A legato note that sounds up to the keyswitch ends 0.01 qn before it,
            # so with the default 0.06 qn a slurred same-pitch repeat on another row had a gap of 0.07 qn (81 ms at 52)
            kl_ = next((v_ for k_, v_ in KS_LEAD_AT.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), None)
            ks.append({"qn": round(early_time(n["qn"]) if kl_ is None else max(0.0, n["qn"] - kl_), 4), "pitch": key, "art": a, "note": n})
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
        + [a + t * bpm_at(a) / 60 for a, b, k in contours if k == "bcsoft" for t in (BCSOFT["t_in"], BCSOFT["t_hold"])]
    dyn_curve = sample(base, [p[0] for p in pts]) if ns else []   # printed dynamics only (measure.py groups stems by it)
    # c03: note-start leads (output only; every controller stays on score time)
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
    sj_at_ = {float(k_): float(v_) for k_, v_ in SLUR_JOIN_LEAD_AT.get(tname, {}).items()}   # mvt2 c50 (A #5)
    sj_lead_ = lambda q_: next((v_ for k_, v_ in sj_at_.items() if abs(k_ - q_) < 0.02), None)
    retongue_leads = []   # mvt1 c15 (C #2)
    stac_leads = []   # mvt1 c23 (A #3)
    rt_s_ = by_name(RETONGUE_LEAD_S) if RETONGUE_LEAD_S else None
    abut_ = by_name(ABUT_LEAD)

    def abut_cond(n):
        q = n["qn"]
        # mvt2 c31 (C #2): ABUT_LEAD[...]["force_at"] lists score onsets that skip the skip_next_same and AUTO_REBOW tests
        # (the basses' ff downbeat 204 was a 4.49 s note; 152 and 220 are followed by same-pitch notes or re-bows)
        if abut_ and any(abs(q - a_) < 0.02 for a_ in abut_.get("force_at", ())):
            return n["art"].startswith("Sus") and final(q) <= abut_["max_cc"] \
                and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 for o in ns) \
                and not any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 and o["pitch"] == n["pitch"]
                            for o in ns)
        return bool(abut_) and n["art"].startswith("Sus") and final(q) <= abut_["max_cc"] and q > 0.5 \
            and ("at" not in abut_ or any(abs(q - a_) < 0.02 for a_ in abut_["at"])) \
            and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 for o in ns) \
            and not any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05 and o["pitch"] == n["pitch"]
                        for o in ns) \
            and not (abut_.get("skip_next_same") and any(o["qn"] > q + EPS and abs(o["qn"] - orig_end[id(n)]) < 0.05
                                                         and o["pitch"] == n["pitch"] for o in ns)) \
            and not (family == "string" and AUTO_REBOW and any(
                (o is n or (o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05))
                and qn_to_sec(orig_end[id(o)]) - qn_to_sec(o["qn"]) > REBOW_MAX_S for o in ns))

    def entry_outer(n):   # the generic entry branch's own condition (below)
        q = n["qn"]
        return not n.get("leg_target") and bool(n.get("art")) and "Accent" not in n["art"] \
            and any(w in n["art"] for w in ENTRY_LEAD_ROWS) and q > -EPS \
            and bool(ent_s or extra_s(q) or ent_art.get(n["art"])) and (q > 0.5 or family == "string" or extra_s(q))

    def poly0(n):   # mvt1 c19: polyphonic on the written lengths (the ends above already carry legato overlaps)
        return any(o is not n and o["qn"] < orig_end[id(n)] - EPS and orig_end[id(o)] > n["qn"] + EPS for o in ns)

    def rt_for(n):
        """the re-tongue lead of this note in seconds (mvt1 c45 / mvt2 c40: a STR_REP_NEW_BOW stroke or "sus_min_s"
        repeat falls back to STR_REP_NEW_BOW["sus_lead_s"] on tracks with no RETONGUE_LEAD_S value)"""
        r_ = rt_s_
        if not r_ and family == "string" and (n.get("rep_sus_gap") or n.get("rep_stroke")):
            r_ = (STR_REP_NEW_BOW or {}).get("sus_lead_s")
        return r_

    def retongue_ok(n):
        """mvt1 c15 (critic C #2): RETONGUE_LEAD_S applies (the previous note's played end, or None)"""
        q, a_ = n["qn"], n.get("art") or ""
        if not rt_for(n) or family not in ("wind", "brass", "string") or q <= 0.5 or n.get("grace") or n.get("run") \
                or extra_s(q):
            return None
        if family == "string":   # mvt1 c19 (critic C #2)
            # mvt1 c44: a STR_REP_NEW_BOW stroke takes the re-tongue lead; mvt1 c45 (critic A #1): so does a "sus_min_s"
            # repeat (REP_SPLIT strokes included: the rule gave them the stroke gap but no lead, and they sounded +94 ms)
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
        # mvt2 c40: STR_REP_NEW_BOW strokes and "sus_min_s" repeats take their lead at any tempo (the mid-tempo gate
        # of the entry leads left every one in this Adagio unled, on the beat)
        srn_ = family == "string" and bool(n.get("rep_stroke") or n.get("rep_sus_gap"))
        if (gate_bpm(q) < ENTRY_MID_MIN_BPM - EPS and not srn_) or (entry_outer(n) and abut_cond(n) and not srn_):
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
        elif STAC_LEAD_S.get(tname) and family == "string" and (n.get("art") or "").startswith("Stac") \
                and not n.get("rep_stac") and not n.get("mt_alt") and q > 0.5:
            # mvt1 c23 (critic A #3): printed staccato strokes start STAC_LEAD_S early
            L = lead_qn(q, STAC_LEAD_S[tname])
            shift[id(n)] = L
            pulls.append((q - L, q))
            stac_leads.append(round(q, 3))
            n["end"] = max(q - L + 0.05, n["end"] - L)   # the stroke keeps its played length
            for o in ns:
                if o is not n and o["qn"] < q - EPS and orig_end[id(o)] <= q + 0.05 and o["end"] > q - L - 0.02:
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
            # c49 (finale technique 20): the row is added to the total (base + extras) before the one clamp; the
            # clamped ls_ is used only where no extras apply (grace targets, no previous note)
            lr_ = leg_s if lx is None else leg_s + lx
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
                tot = ls_ + ex if lx is None else max(LEG_LEAD_CLAMP[0], min(LEG_LEAD_CLAMP[1], lr_ + ex))
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
            shift[id(n)] = lead_qn(q, SOST_JOIN_LEAD_S)
            n["vel"] = max(n["vel"], SOST_VEL)
            sost_joins.append(round(q, 3))
        elif (SLUR_START_SUS or PICKUP_SUS or PORTATO_TAIL_JOIN or sj_lead_(q) is not None) and not n.get("leg_target") and _lg((n.get("art") or "")) \
                and not n.get("subito_fresh") and any((o.get("slur_start_sus") or o.get("portato_tail")) and o["qn"] < q - EPS
                        and abs(orig_end[id(o)] - q) < 0.05 for o in ns):
            # mvt1 c15 (critic A #2): the second note of a slur whose first note was tongued on Sus is joined by the KS
            # Master like the sostenuto join: SOST_JOIN_LEAD_S early (at most 0.45 of the first note), SOST_VEL
            # mvt1 c34 (critic A #2): also the note after a re-tongued portato tenuto (PORTATO_TAIL_JOIN)
            p_ = next(o for o in ns if (o.get("slur_start_sus") or o.get("portato_tail")) and o["qn"] < q - EPS
                      and abs(orig_end[id(o)] - q) < 0.05)
            if sj_lead_(q) is not None and not (SLUR_START_SUS or PICKUP_SUS or PORTATO_TAIL_JOIN):
                shift[id(n)] = min(lead_qn(q, sj_lead_(q)), 0.45 * (q - p_["qn"]))   # mvt2 c50: listed onset, velocity kept
            else:
                shift[id(n)] = min(lead_qn(q, SOST_JOIN_LEAD_S), 0.45 * (q - p_["qn"]))
                n["vel"] = max(n["vel"], SOST_VEL)
            slur_start_joins.append(round(q, 3))
        elif n.get("fresh") and ent_s:
            # c09 (A #3): the section entering after the solo (Vln I qn 65): the family entry lead; the solo's last
            # note is cut 0.03 qn before the moved onset below, so the monophonic legato patch does not join them
            s_ = min(ENTRY_CAP_S, ent_pick(q) + extra_s(q))
            L = lead_qn(q, s_)
            shift[id(n)] = L
            pulls.append((q - L, q))
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
                and (any(w in n["art"] for w in ENTRY_LEAD_ROWS) or n["art"] in LEG_ROWS_EXTRA) \
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
            elif TREM_ENTRY_LEAD_S and family == "string" and n["art"] == "Tremolo" and q > 0.5 \
                    and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 and o.get("art") != "Tremolo" for o in ns):
                # mvt1 c09 (A #4): a tremolo entry straight after a held note on another row (Vln II 304 Leg Slur ->
                # Tremolo dipped 10 dB for 0.2 s; Vln I 664, Vln I/II 484, Vc 464 5-7 dB): the tremolo attack takes
                # 0.1-0.2 s, so it starts TREM_ENTRY_LEAD_S early and the old notes end at the moved start (the c05
                # keyswitch guard: no legato note sounding at the keyswitch)
                L = lead_qn(q, TREM_ENTRY_LEAD_S)
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
                                for o in ns)):
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
    # mvt2 c35 (critic C #1): REATTACK_LEAD_AT / REATTACK_LEAD_S (see the defaults)
    reattack_leads = []
    ra_at_ = {float(k_): float(v_) for k_, v_ in REATTACK_LEAD_AT.get(tname, {}).items()}
    ra_s_ = REATTACK_LEAD_S.get(family, 0.0)
    ra_hit_ = set()
    if ra_at_ or ra_s_:
        for n in ns:
            q = n["qn"]
            sq_ = n.get("sq", q)
            at_ = next((v_ for k_, v_ in ra_at_.items() if abs(k_ - sq_) < 0.02), None)
            if at_ is not None:
                ra_hit_.add(next(k_ for k_ in ra_at_ if abs(k_ - sq_) < 0.02))
            if at_ is None and (not ra_s_ or shift.get(id(n), 0.0) > 1e-6):
                continue
            if q <= 0.5 or n.get("grace") or n.get("run"):
                continue
            pv_ = [o for o in ns if o is not n and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.10]
            if not pv_:
                if at_ is not None:
                    print(f"  warning: {tname} REATTACK_LEAD_AT {sq_}: no note ends at its onset", file=sys.stderr)
                continue
            if at_ is None and (poly0(n) or any(o["pitch"] == n["pitch"] for o in pv_)
                                or qn_to_sec(orig_end[id(n)]) - qn_to_sec(q) < REATTACK_MIN_S):
                continue
            pm_ = max(o["qn"] - shift.get(id(o), 0.0) for o in pv_)
            L = min(lead_qn(q, at_ if at_ is not None else ra_s_), 0.45 * (q - pm_))
            old_ = shift.get(id(n), 0.0)
            if L <= old_ + 1e-6:
                continue
            if old_ > 1e-6:
                pulls = [(q - L, b_) if abs(b_ - q) < EPS and abs(a_ - (q - old_)) < 1e-6 else (a_, b_) for a_, b_ in pulls]
            if not any(abs(b_ - q) < EPS and abs(a_ - (q - L)) < 1e-6 for a_, b_ in pulls):
                pulls.append((q - L, q))
            shift[id(n)] = L
            for o in pv_:
                o["end"] = min(o["end"], max(o["qn"] - shift.get(id(o), 0.0) + 0.02, q - L - 0.02))
            reattack_leads.append([round(q, 3), round(L, 4)])
    for k_ in ra_at_:
        if k_ not in ra_hit_:
            print(f"  warning: {tname} REATTACK_LEAD_AT {k_}: no note", file=sys.stderr)
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

    # mvt2 c46 (critic A #3): CAESURA_LIFT, a CC11 fall into the target's moved onset (the pull window then plays the
    # target's own CC11)
    caesura_lifts = []
    for q_t, cc_l in CAESURA_LIFT.get(tname, {}).items():
        tg_ = [o for o in ns if abs(o["qn"] - q_t) < EPS]
        if not tg_:
            print(f"  WARNING CAESURA_LIFT {tname} {q_t}: no note there", file=sys.stderr)
            continue
        fb_ = round(min(new_on(o) for o in tg_) - PULL_PAD_QN, 4)
        fa_ = qn_before(fb_, CAESURA_LIFT_S)
        if not any(o["qn"] < fa_ and orig_end[id(o)] > fb_ - EPS for o in ns):
            print(f"  WARNING CAESURA_LIFT {tname} {q_t}: no note held into it", file=sys.stderr)
        cc_falls.append((fa_, fb_, cc_l, 0.005))
        breaks += [fa_, fb_, fb_ + 0.005]
        caesura_lifts.append([round(q_t, 3), round(fa_, 4), round(fb_, 4), cc_l])
    # mvt2 c46 (HP_CURVE): Bezier offset against the linear hairpin, added to the CC11 lane only
    hp_curved = []
    hpc_ = HP_CURVE if (HP_CURVE and family not in HP_CURVE.get("skip_families", ())) else None
    if hpc_:
        for a_, v0_, b_, v1_, hk_, nien_ in hp_segs:
            if nien_ or b_ - a_ < 0.25 or abs(v1_ - v0_) < 1 or hk_ not in hpc_:
                continue
            if qn_to_sec(b_) - qn_to_sec(a_) > hpc_.get("max_s", 1e9):
                continue
            if any(x0 - EPS <= a_ < x1 - EPS for x0, x1 in hpc_.get("skip_spans", [])
                   + hpc_.get("linear", {}).get(tname, [])):
                continue
            if any(abs(a_ - x_) < 0.02 for x_ in HELD_DECRESC_SKIP.get(tname, [])):
                continue
            if any(a_ + EPS < pq_ < b_ - EPS for pq_, _ in pts):
                continue   # a mark or another hairpin inside: the base curve is not one straight ramp
            hp_curved.append((a_, v0_, b_, v1_, hpc_[hk_]))

    def hp_delta(q):
        for a_, v0_, b_, v1_, (cx_, cy_) in hp_curved:
            if a_ < q < b_:
                u = (q - a_) / (b_ - a_)   # solve x(t) = u for the Bezier with control x cx_ (monotone for 0 < cx_ < 1)
                lo, hi = 0.0, 1.0
                for _ in range(30):
                    t_ = (lo + hi) / 2
                    if 2 * (1 - t_) * t_ * cx_ + t_ * t_ < u:
                        lo = t_
                    else:
                        hi = t_
                t_ = (lo + hi) / 2
                y_ = 2 * (1 - t_) * t_ * cy_ + t_ * t_
                return (y_ - u) * (v1_ - v0_)
        return 0.0

    def final2c(q):
        for a_, b_ in pulls:
            if a_ - EPS <= q < b_:
                return final(b_) + hp_delta(b_)
        return final(q) + hp_delta(q)
    hp_breaks_ = [a_ + k_ * (b_ - a_) / 12 for a_, _, b_, _, _ in hp_curved for k_ in range(13)]
    cc11 = sample(final2c if hp_curved else final2, breaks + hp_breaks_) if ns else []
    # check: every printed mark is on the curve
    for q, d in marks:
        if d in ("sf", "sfz"):
            continue
        # mvt2 v600 port (c27): an fp is checked after its spike (FP_SPIKE: f, then p by FP_SPIKE[2] qn)
        got = value_at(pts, q + (FP_SPIKE[2] if d == "fp" and FP_SPIKE else 0.0) + 0.001)
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
        if vib_fam and tname in CC1_HOLD:   # mvt2 c32 (critic C #6): a held CC1 on a vibrato-crossfade patch too (the
            return CC1_HOLD[tname]          # Violin I solo's DIV A KS Master: Sus Vib alone instead of Sus/Molto Vib)
        if not vib_fam:
            # mvt1 c09 (C #1): in the Hollywood Brass KS Masters (1FH, 1TP, 1TB, 1TU) and the Clarinet KS Master the
            # dynamic layers are crossfaded by CC1 (each layer group's Source volume rescaler is driven by a cc 1
            # MidiController; CC11 is only the Global Group volume), so the c01 formula (CC1 57-87) played every printed
            # dynamic on the mp-f samples. These tracks take CC1 from the printed dynamic curve (hairpins, no accent or
            # fit shapes, so gentle accents stay off the top layer) through CC1_DYN_MAP
            if any(tname.startswith(p_) for p_ in CC1_DYN_TRACKS):
                map_ = next((m_ for k_, m_ in CC1_DYN_MAP_BY.items() if tname.startswith(k_)), CC1_DYN_MAP)   # mvt2 c31
                return round(value_at(map_, base(q)))
            if tname in CC1_HOLD:   # mvt1 c09 (C #1): e.g. the CB KS Master's Non Vib/Vib overlap (64-72)
                return CC1_HOLD[tname]
            return max(40, min(100, 64 + (v11 - 46) * 0.3))
        n = sounding(q)
        if n is not None and n.get("art") == "Flautando":
            return 20
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
    vol_parts = []   # c02: exact level offsets in dB, written as a track volume envelope by build_reaper.py
    vol_tags = {}    # mvt2 c55: id(item) -> "class:layer" (see ENV_CLASS)

    def vol_add(tag, item):
        vol_tags[id(item)] = tag
        vol_parts.append(item)
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
            vol_add("slow:timp_hairpin", ("env", ps))
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
                    vol_add("slow:timp_roll_trim", ("env", ps))
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
            nxt_on = min([o["qn"] for o in ns if o["qn"] >= ce - EPS] + [ce + 2])
            vol_add("slow:timp_settle", ("settle", c0, ce, nxt_on))
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
                vol_add("slow:timp_soft_flat", ("flat", c0, max(ce, nxt_on - 0.05), -6.0))   # held through the ring, like the settle
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
                vol_add("shape:timp_loud_attack", ("env", [(q - 0.01, 0.0), (q + 0.01 * bpm_at(q) / 60, ad_),
                                          (q + 0.25, ad_), (q + 0.75, 0.0)], True))

    def vol(q):
        v = 0.0
        for item in vol_parts:
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
    def role_tag(a_, b_):
        """mvt2 c55: a role row over fewer than ROLE_NOTE_MIN onsets and under 6 s is a per-note level (class level,
        layer role_note); ROLE_NOTE_MIN 0 = every role is slow (the default)"""
        if not ROLE_NOTE_MIN:
            return "slow:role"
        n_ = len({round(n["qn"], 3) for n in ns if a_ - 0.26 <= n["qn"] < b_ - 0.01})
        return "level:role_note" if n_ < ROLE_NOTE_MIN and qn_to_sec(b_) - qn_to_sec(a_) < 6.0 else "slow:role"
    for a, b2, dbv, er in rows_:
        if er:
            vol_add(role_tag(a, b2), ("span", a, b2, dbv, er))
            continue
        prev_ = [r for r in rows_ if not r[3] and r != (a, b2, dbv, er) and -0.01 <= a - r[1] <= ROLE_CHAIN]
        next_ = [r for r in rows_ if not r[3] and r != (a, b2, dbv, er) and -0.01 <= r[0] - b2 <= ROLE_CHAIN]
        if prev_:
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
            nb += sf_shift(nb)
            pout = [(max(pin[-1][0], nb - 0.1), dbv), (max(pin[-1][0] + 0.01, nb + 0.15), 0.0)]
        else:
            pout = [(max(pin[-1][0], b2), dbv), (max(pin[-1][0], b2) + 0.5, 0.0)]
        vol_add(role_tag(a, b2), ("env", pin + pout))
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
                    vol_add("slow:hpgain", ["hpgain", a, b2, min(nx, arr + HP_HOLD_CAP, b2 + 1.0), g_, 0.0, HP_REL, 0.0, 0.0,
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
                share_ = SOST_HOLD_SHARE
                fff_ = FFF_HOLD_CAP is not None and base(b2 - 0.01) >= DYN["fff"] - 2
                if fff_:   # mvt1 c02 (C #1a): held to the next printed mark or hairpin, at most FFF_HOLD_CAP qn
                    fe_ = min([mq for mq, d_ in marks if mq > arr + 0.05] + [a_ for a_, b_, k_ in hps if a_ > arr + 0.05]
                              + [arr + FFF_HOLD_CAP])
                    if fe_ > max(hold_end, sost_end):
                        sost_end, share_ = fe_, 1.0
                vol_add("slow:hpgain", ["hpgain", a, b2, hold_end, g_, 0.0, HP_REL, sost_end, share_ * g_, mfa, fff_])
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
                    vol_add("slow:hpgain", ("env", [(a, 0.0), (b2, g_), (max(b2, da) + 0.001, g_), (db_, -1.0),
                                              (db_ + 1.0, 0.0)]))
                    used_dec.append(round(da, 3))
                    hp_soft_spans.append((a, db_))
                else:
                    vol_add("slow:hpgain", ("env", [(a, 0.0), (b2, g_), (b2 + HP_REL, 0.0)]))
                    hp_soft_spans.append((a, b2))
                hp_soft.append(round(a, 3))
                continue
            if k == "cresc" and any(abs(a - x_) < 0.3 for x_ in SWELL_NO_SOFT_GAIN.get(tname, [])):
                continue   # c15 (B #1): an unmarked swell under the phrase's printed peak
            if in_lead:
                g_ = next((v_ for k_, v_ in HP_SOFT_GAIN_AT.get(tname, {}).items() if abs(a - k_) < 0.3),
                          HP_GAIN_SOFT_DB[family])
            else:
                if any(abs(a - x_) < 0.3 for x_ in HP_SOFT_ACC_SKIP):
                    continue
                g_ = HP_GAIN_SOFT_ACC_DB
            if k == "cresc":
                dec = [(a_, b_) for a_, b_, k_ in hps if k_ == "decresc" and -0.3 <= a_ - b2 <= 0.3]
                if dec:   # messa di voce: held to the decrescendo, released linearly across it
                    da, db_ = min(dec)
                    vol_add("slow:hpgain", ["hpgain", a, b2, max(b2, da), g_, 0.0, max(0.25, db_ - da),
                                      0.0, 0.0, True])
                    used_dec.append(round(da, 3))
                    if in_lead:
                        hp_soft_spans.append((a, db_))
                        # c22 (C #1): a listed decrescendo depth deeper than the messa di voce's release adds the rest
                        dd_ = next((v_ for k_, v_ in HP_SOFT_DEC_AT.get(tname, {}).items() if abs(da - k_) < 0.3), 0.0)
                        if dd_ > g_:
                            nx = min([n["qn"] for n in ns if n["qn"] > db_ + 0.05], default=db_ + 1.0)
                            vol_add("slow:hpgain", ["hpgain", da, db_, min(nx, db_ + HP_HOLD_CAP), -(dd_ - g_), 0.0, HP_REL,
                                              0.0, 0.0, True])
                else:
                    arr = min([n["qn"] for n in ns if n["qn"] >= b2 - 0.05], default=b2)
                    nx = min([n["qn"] for n in ns if n["qn"] > arr + 0.05], default=arr + HP_HOLD_CAP)
                    hold_end = min(nx, arr + HP_HOLD_CAP)
                    if arr > b2 + 0.25:
                        hold_end = min(arr, b2 + 2.0)
                    vol_add("slow:hpgain", ["hpgain", a, b2, hold_end, g_, 0.0, HP_REL, 0.0, 0.0, True])
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
                vol_add("slow:hpgain", ["hpgain", a, b2, min(nx, b2 + HP_HOLD_CAP), -dd_, 0.0, HP_REL, 0.0, 0.0, True])
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
    # c06 (C #5): the long-note swell in dB (same notes as the CC11 swell)
    for a, b2, k in contours:
        if k.startswith("swell") and k != "swell_sost":
            vol_add("shape:swell_db", ("swell_db", a, b2, k == "swell_taper"))
    # c06 (A #2): per-pitch trims on legato notes, from 0.1 qn before the score onset (legato leads), 0.25 qn ramp
    ptab = PITCH_TRIMS.get(tname, {})
    pt = {int(k): v for k, v in ptab.items() if not k.startswith("_")}
    allart = bool(ptab.get("_all_arts", False))   # c07 (B #1): Sus chords too
    arts_only = ptab.get("_arts")                  # c08 (A #3): only these articulations (pizz.)
    allp = set(ptab.get("_all_arts_pitches", []))  # c08 (B #1): these pitches on every articulation
    pitch_trimmed = 0

    def sec_qn(q0, t):   # t seconds after q0, in qn at the local tempo
        return q0 + t * bpm_at(q0) / 60

    def next_moved(n):
        """c09 (A #2): the moved onset of the note that follows n within 0.1 qn of its score end (None if none)."""
        e_ = orig_end[id(n)]
        nx_ = [new_on(o) for o in ns if o is not n and -EPS < o["qn"] - e_ < 0.1 and o["qn"] > n["qn"] + EPS]
        return min(nx_) if nx_ else None

    def joined_in(n):
        """c09 (A #2): n follows another note without a gap (its trim should start at its moved onset)."""
        return any(o is not n and o["qn"] < n["qn"] - EPS and abs(orig_end[id(o)] - n["qn"]) < 0.1 for o in ns)

    trim_kept = []   # mvt2 c55: score onsets whose trims keep the old ramp in
    trim_pairs = []  # mvt2 c55: (points as written, points with the old keying) of every level trim (FILL_PRE_KEEP_SUM)
    fill_items = []  # mvt2 c55: (early fill item, score onset)
    nt0_ = {float(k): v for k, v in NOTE_TRIMS.get(tname, {}).items() if not k.startswith("_")}

    def trim_total(o):
        """mvt2 c55: the table values of note o's level trims (pitch trim + note trim), for TRIM_RISE_LEAD"""
        t_ = 0.0
        a_ = o.get("art") or ""
        if o["pitch"] in pt and not any(abs(o["qn"] - x) < 0.02 for x in ptab.get("_skip_onsets", [])) \
                and ((a_ in arts_only) if arts_only else (allart or o["pitch"] in allp or _lg(a_))):
            v_ = pt[o["pitch"]]
            t_ += v_["body"] if isinstance(v_, dict) else v_
        t_ += next((v for k, v in nt0_.items() if abs(o["qn"] - k) < 0.02), 0.0)
        return t_

    def trim_shape(n, dbv, ramp, early=None, _legacy=False):
        """c09 (A #2): the dB shape of a note trim. A joined note's trim starts at its moved onset (crossfading in over
        [moved - 0.05, moved + 0.03]); a trim on a note that another note follows ends over [next moved onset - 0.05,
        + 0.03], so the next note's (early) legato transition no longer plays under it."""
        q0, e = n["qn"], orig_end[id(n)]
        if TRIM_KEY == "score" and early is None and not _legacy:
            # a listed note, or (TRIM_RAMP_KEEP_FITTED) a note that also carries a LEVEL_SHAPES_S / level_fits row,
            # keeps its old ramp in (those rows were fitted on top of it); its end is keyed like every other
            keep_in_ = any(abs(q0 - k_) < 0.02 for k_ in TRIM_RAMP_KEEP.get(tname, [])) \
                or (TRIM_RAMP_KEEP_FITTED and any(abs(q0 - float(k_)) < 0.02 for k_, _ in LEVEL_SHAPES_S.get(tname, [])))
            # a same-pitch repeat keeps the old keying on both sides of its join: the dip before the re-attack is what
            # separates the two notes (S1), and a trim held to the beat fills it (Oboe 1 148: 7.0 -> 2.4 dB, simulated)
            rep_in_ = any(p_ is not n and p_["pitch"] == n["pitch"] and p_["qn"] < q0 - EPS and abs(orig_end[id(p_)] - q0) < 0.1
                          for p_ in ns)
            keep_in_ = keep_in_ or rep_in_
            if keep_in_:
                trim_kept.append(round(q0, 3))
            if TRIM_BODY_EQUIV and not keep_in_:
                # the one level is what the old ramped shape gave the note's body (its mean over 20-80 % of the note in
                # seconds), so the fitted body levels and the balance stay where they were measured
                old_ = trim_shape(n, dbv, ramp, None, True)
                tb0_, tb1_ = qn_to_sec(q0), qn_to_sec(e)
                xs_ = [sec_to_qn(tb0_ + (0.2 + 0.6 * (k_ + 0.5) / 24) * (tb1_ - tb0_)) for k_ in range(24)]
                dbv = round(sum(value_at(old_, x_) if old_[0][0] <= x_ < old_[-1][0] else 0.0 for x_ in xs_) / 24, 2)
            # mvt2 c55 (critic A #1, B #5c): see TRIM_KEY. One window per join, shared by the two notes
            hx_ = 0.5 * TRIM_XFADE_S

            def win_in(o):
                """the window over which note o's trim comes in (qn, qn)"""
                oq_ = o["qn"]
                if joined_in(o):
                    # TRIM_RISE_LEAD: where the trims rise across the join the window lies that share of the lead
                    # before the beat (the transition's weak point lies between the moved note-on and the beat: a
                    # rise there fills it, a fall there deepens it)
                    pv_ = [p_ for p_ in ns if p_ is not o and p_["qn"] < oq_ - EPS and abs(orig_end[id(p_)] - oq_) < 0.1]
                    if TRIM_RISE_LEAD and pv_ and trim_total(o) - trim_total(max(pv_, key=lambda p_: orig_end[id(p_)])) > 0.5:
                        c_ = qn_to_sec(oq_) - TRIM_RISE_LEAD * max(0.0, qn_to_sec(oq_) - qn_to_sec(new_on(o)))
                        return sec_to_qn(c_ - hx_), sec_to_qn(c_ + hx_)
                    return sec_qn(oq_, -hx_), sec_qn(oq_, hx_)
                m_ = new_on(o)
                pe_ = [orig_end[id(p_)] for p_ in ns if p_ is not o and p_["qn"] < oq_ - EPS and orig_end[id(p_)] <= oq_ + EPS]
                if pe_ and qn_to_sec(m_) - qn_to_sec(max(pe_)) < TRIM_HOLD_GAP_S:
                    return sec_qn(m_, -TRIM_PRE_S - 2 * hx_ / 2), sec_qn(m_, -TRIM_PRE_S)
                return sec_qn(m_, -TRIM_PRE_S - 0.06), sec_qn(m_, -TRIM_PRE_S)
            a0, a1 = win_in(n)
            if keep_in_:
                a0, a1 = trim_shape(n, dbv, ramp, None, True)[:2]
                a0, a1 = a0[0], a1[0]
            nx_ = [o for o in ns if o is not n and o["qn"] > q0 + EPS and o["qn"] >= e - 0.1 - EPS]
            nx_ = [o for o in nx_ if abs(o["qn"] - min(x_["qn"] for x_ in nx_)) < EPS]
            z0, z1 = e, e + 0.1
            if nx_:
                o_ = min(nx_, key=new_on)
                if o_["qn"] - e < 0.1 and any(x_["pitch"] == n["pitch"] for x_ in nx_):
                    z0, z1 = new_on(o_) - 0.05, new_on(o_) + 0.03   # before a same-pitch repeat: as before c55
                elif o_["qn"] - e < 0.1 or qn_to_sec(new_on(o_)) - qn_to_sec(e) < TRIM_HOLD_GAP_S:
                    z0, z1 = win_in(o_)
            if z0 < a1 + 1e-4 and keep_in_:   # the kept ramp in does not finish before the end window
                pk_ = dbv * max(0.0, min(1.0, (z0 - a0) / max(1e-6, a1 - a0)))
                return [(a0, 0.0), (max(z0, a0 + 0.001), pk_), (max(z1, a0 + 0.002), 0.0)]
            if z0 < a1 + 1e-4:   # a note shorter than the windows
                z0 = a1 + 1e-4
                z1 = max(z1, z0 + 1e-4)
            return [(a0, 0.0), (a1, dbv), (z0, dbv), (z1, 0.0)]
        if joined_in(n) and ramp == 0.25:
            # pitch trims only: from the moved onset over 0.25 qn. Note trims keep their 0.6 s ramp from the score onset:
            # a fast -8 dB step at the moved onset (first c09 render) deepened the transition sag at Ob1 190 (3.0 ->
            # 9.4 dB), CA 152 (3.9 -> 9.7) and Fl1 254 (4.8 -> 7.9)
            m = new_on(n)
            # mvt2 c50 (critic A #2): a positive pitch trim on a joined note starts with the mirror of the previous
            # note's release ramp [m - 0.05, m + 0.03], so two notes with the same lift hold a constant sum through the
            # join (c49: the +3 dB Cor anglais trims with the 0.25 qn ramp dropped 2.7 dB during the transition and
            # moved the joins at 130, 156, 166, 168 later by 61-103 ms). Negative trims and {"early", "body"} shapes
            # keep the 0.25 qn ramp from the moved onset (the c09 evidence concerns them); so do notes that follow
            # another note without being a legato target (Double basses Sus MAX, Horn 4: fitted with that ramp).
            a0, a1 = (m - 0.05, m + 0.03) if (dbv is not None and dbv > 0 and n.get("leg_target")) else (m, m + 0.25)
        else:
            a0, a1 = q0 - 0.1 if ramp == 0.25 else q0, (q0 - 0.1 if ramp == 0.25 else q0) + ramp
        nm = next_moved(n)
        z0, z1 = (nm - 0.05, nm + 0.03) if nm is not None else (e, e + 0.1)
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
        if ("izz" in art_ or n.get("rep_sus") or n.get("rep_stac") or n.get("short_stroke")) and not isinstance(v_, dict):
            # mvt1 c04: repeated strokes (REP_SPLIT) too: the 0.25 qn ramp on each eighth/triplet made a 3 dB sawtooth
            # c12 (A #1): a pizz. trim is a step at full value on the attack (the 0.25 qn ramp from the moved onset,
            # sampled on the 0.125 qn grid, reached full depth just before the next note: F4 -8 sat at -1.8..-2.5 dB on
            # its attack and cut the following note instead); held to the next onset (at most 1.5 s), exact breakpoints
            q0 = new_on(n)
            nx_ = [new_on(o) for o in ns if o["qn"] > n["qn"] + EPS]
            ne_ = min(min(nx_) if nx_ else 1e9, sec_qn(n["qn"], 1.5))
            vol_add("level:pitch_trim_pizz", ("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
                                      (max(qn_before(q0, 0.01) + 0.002, qn_before(ne_, 0.03)), v_),
                                      (max(qn_before(q0, 0.01) + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
        elif isinstance(v_, dict):   # c08 (A #1): {"early", "body"}: the sample's early sag is not cut with the body
            vol_add("shape:pitch_trim_earlybody", ("env", trim_shape(n, None, 0.25, (v_["early"], v_["body"]))))
        else:
            vol_add("level:pitch_trim", ("env", trim_shape(n, v_, 0.25), TRIM_KEY == "score"))
            if TRIM_KEY == "score":
                trim_pairs.append((vol_parts[-1][1], trim_shape(n, v_, 0.25, None, True)))
        pitch_trimmed += 1
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
            vol_add("level:metric_db", ("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
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
            v_ = mtab_.get(kind_, 0.0)
            if not v_:
                continue
            q0 = min(new_on(o) for o in ns if abs(o["qn"] - q_) < EPS)
            nx_ = [o_ for o_ in ons_ if o_ > q_ + EPS]
            nq_ = min(new_on(o) for o in ns if abs(o["qn"] - nx_[0]) < EPS) if nx_ else sec_qn(q_, 1.5)
            ne_ = min(nq_, sec_qn(q_, 1.5))
            vol_add("level:metric_bowed", ("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
                                      (max(qn_before(q0, 0.01) + 0.002, qn_before(ne_, 0.03)), v_),
                                      (max(qn_before(q0, 0.01) + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
            metric_db_n["m_" + kind_] += 1
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
            vol_add("shape:sost_hold", ("env", [(a, 0.0), (x40, 0.0), (nm_ - 0.25, SOST_SUSTAIN_DB),
                                      (max(nm_ + 0.25, na_ + 0.25), SOST_SUSTAIN_DB),
                                      (max(nx40, na_ + 0.26, nm_ + 0.26), 0.0)]))
            sost_held.append(round(b2, 3))
        elif nm_ - 0.25 > x40 + 0.01:
            vol_add("shape:sost_hold", ("env", [(a, 0.0), (x40, 0.0), (nm_ - 0.25, SOST_SUSTAIN_DB), (nm_, 0.0)]))
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
                vol_add("shape:early_fill", ("env", p0 + [(sec_qn(q0, H_), X), (sec_qn(q0, H_ + 0.25), 0.0)], True))
                fill_items.append((vol_parts[-1], q0))
            else:
                vol_add("shape:early_fill", ("env", [(q0 - 0.02, 0.0), (sec_qn(q0, 0.05), hit[0]), (sec_qn(q0, 0.35), hit[0]),
                                          (sec_qn(q0, 0.6), 0.0)]))
            early_n += 1
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
        vol_add("shape:loop_fill", ("env", ps_, True))
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
    if family == "timp" and TIMP_ROLL_RESTRIKE.get("at") and TIMP_ROLL_RESTRIKE.get("dip_db"):
        d0_, d1_, d2_ = TIMP_ROLL_RESTRIKE["dip_s"]
        for n in ns:
            if not (n.get("art") or "").endswith("Rls"):
                continue
            q1_ = round(new_on(n), 4)
            for cq_, _ in restrike_plan(q1_, round(max(0.02, n["end"] - q1_), 4), round(n["qn"], 4), n["pitch"]):
                tc_ = qn_to_sec(cq_)
                vol_add("shape:timp_restrike_dip", ("env", [(cq_, 0.0), (sec_to_qn(tc_ + d0_), TIMP_ROLL_RESTRIKE["dip_db"]),
                                          (sec_to_qn(tc_ + d1_), TIMP_ROLL_RESTRIKE["dip_db"]), (sec_to_qn(tc_ + d2_), 0.0)], True))
    # mvt1 c05 (critic C #2): a dip over each staggered-breath re-entry (BREATH_SPLIT_AT; the split is at the output stage)
    for sq_k, pts_ in BREATH_SPLIT_AT.get(tname, {}).items():
        if not any(abs(n["qn"] - sq_k) < 0.02 for n in ns):
            raise SystemExit(f"BREATH_SPLIT_AT {tname} {sq_k}: no note there")
        for p_ in pts_:
            tp_ = qn_to_sec(p_)
            vol_add("shape:breath_split_dip", ("env", [(qn_before(p_, 0.02), 0.0), (sec_to_qn(tp_ + 0.03), BREATH_SPLIT["dip_db"]),
                                      (sec_to_qn(tp_ + 0.12), BREATH_SPLIT["dip_db"]),
                                      (sec_to_qn(tp_ + BREATH_SPLIT["dip_s"]), 0.0)], True))
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
        vol_add("shape:loop_profile", ("env", ps_, True))
        loop_n += 1
    # c26: re-bow fills (REBOW_FILLS): each list runs from its re-bow to the next one (exact breakpoints, seconds on the
    # real tempo map); its last value holds until the next list starts, and after the last re-bow to the release
    rbf_ = sorted((float(k), v) for k, v in REBOW_FILLS.get(tname, {}).items() if not k.startswith("_"))
    rebow_fill_ends = []   # mvt1 c45: [re-bow qn, hold end qn, last dB] for lists ended at their note's end
    rebow_levels = []      # mvt2 c55: [re-bow qn, level dB] (REBOW_FILL_SPLIT)
    for i_, (p_, pts_) in enumerate(rbf_):
        ps_ = [(sec_to_qn(qn_to_sec(p_) + t_), d_) for t_, d_ in pts_]
        # mvt1 c02: up to the next list's first point (fit_rebows.py now starts a list PRE_FILL_S before its re-bow)
        e_ = sec_to_qn(qn_to_sec(rbf_[i_ + 1][0]) + min(-0.04, rbf_[i_ + 1][1][0][0])) if i_ + 1 < len(rbf_) else END + 0.5
        # mvt2 c53 (critic B #4): a list's points after the next list's first point are dropped (both lists were added
        # there: Violoncellos div 284.021, one point 5.4 dB over its neighbours)
        if i_ + 1 < len(rbf_) and len([p_x for p_x in ps_ if p_x[0] < e_ - 1e-6]) >= 1:
            ps_ = [p_x for p_x in ps_ if p_x[0] < e_ - 1e-6]
        # mvt1 c45 (critic B #1; mvt2 c40 port): a list never holds into a later note. When a note of this track starts
        # after the end of the note the re-bow belongs to and before e_, the last value holds to that note's end and is
        # gone REBOW_FILL_END_S later (mvt1 c44: two lists held +4.1 / -2.0 dB over 26-29 bars of later notes)
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
        if REBOW_FILL_SPLIT and len(ps_) > 2:
            # mvt2 c55 (critic B #3): the list's level (its time-weighted median) is one item of class level, the rest
            # (list minus median) the shape item; their sum is the list as fitted, so nothing changes with both on
            ys_ = sorted(value_at(ps_, ps_[0][0] + (ps_[-1][0] - ps_[0][0]) * (k_ + 0.5) / 200) for k_ in range(200))
            md_ = round(0.5 * (ys_[99] + ys_[100]), 2)
            if abs(md_) >= REBOW_FILL_SPLIT:
                vol_add("level:rebow_level", ("env", [(ps_[0][0], md_), (ps_[-1][0], md_)], True))
                ps_ = [(x_, round(d_ - md_, 3)) for x_, d_ in ps_]
                rebow_levels.append([p_, md_])
        vol_add("shape:rebow_fill", ("env", ps_, True))
    # c18 (C #3a): JOIN_NOTCH: a dB notch over a moved legato join's transition peak, (from qn, to qn, dB) with 0.04 qn
    # ramps, exact breakpoints
    for a_, b_, d_ in JOIN_NOTCH.get(tname, []):
        vol_add("shape:join_notch", ("env", [(a_ - 0.04, 0.0), (a_, d_), (b_, d_), (b_ + 0.04, 0.0)], True))
    # mvt2 c53 (critic B #1): JOIN_NOTCH_S, seconds from the target's moved note-on (see the default)
    join_notch_s = []
    for k_, v_ in sorted(JOIN_NOTCH_S.get(tname, {}).items()):
        n_ = next((o for o in ns if abs(o["qn"] - float(k_)) < 0.02), None)
        if n_ is None:
            print(f"  WARNING {tname}: JOIN_NOTCH_S {k_} has no note", file=sys.stderr)
            continue
        t0_ = qn_to_sec(new_on(n_))
        v_ = [v_] if isinstance(v_, dict) or not isinstance(v_[0], (list, tuple, dict)) else list(v_)
        for w_ in [w_ for w_ in v_ if isinstance(w_, dict)]:   # {"shape": [[s, dB], ...]}: exact breakpoints
            vol_add("shape:join_notch_s", ("env", [(sec_to_qn(t0_ + float(x_)), float(d_)) for x_, d_ in w_["shape"]], True))
            join_notch_s.append([round(n_["qn"], 3), w_["shape"][0][0], w_["shape"][-1][0], min(d_ for _, d_ in w_["shape"])])
        for a_, b_, d_ in [w_ for w_ in v_ if not isinstance(w_, dict)]:
            vol_add("shape:join_notch_s", ("env", [(sec_to_qn(t0_ + a_ - JOIN_NOTCH_RAMP_S), 0.0), (sec_to_qn(t0_ + a_), float(d_)),
                                      (sec_to_qn(t0_ + b_), float(d_)), (sec_to_qn(t0_ + b_ + JOIN_NOTCH_RAMP_S), 0.0)], True))
            join_notch_s.append([round(n_["qn"], 3), round(a_, 3), round(b_, 3), float(d_)])
    # mvt1 c06 (C #2): explicit level shapes from the config (per track and "_all")
    for ps_ in LEVEL_SHAPES.get(tname, []) + LEVEL_SHAPES.get("_all", []):
        vol_add("auto:level_shape", ("env", [(float(x_), float(d_)) for x_, d_ in ps_], True))
    # mvt1 c24: LEVEL_SHAPES_S (seconds around a score onset, converted on the real tempo map)
    for q0_, ps_ in LEVEL_SHAPES_S.get(tname, []):
        t0_ = qn_to_sec(float(q0_))
        vol_add("auto:level_shape_s", ("env", [(sec_to_qn(t0_ + float(x_)), float(d_)) for x_, d_ in ps_], True))
    # mvt1 c36 (critic C #3): CRESC_FRONTS (build/cresc_fronts.json {track: {score onset: [cut dB, peak s, sag s]}}): a
    # held note that starts a printed crescendo blooms over its first 0.1-1 s and sags before the hairpin's CC ramp
    # brings it back (20 of 36 such notes in c35 ended the crescendo under their own attack): a cut from the moved onset,
    # 0 at the onset, -cut at +0.06 s and at +peak s, 0 again at +sag s (seconds, exact breakpoints); fitted on a render
    cresc_fronts = []
    for k_, v_ in CRESC_FRONTS.get(tname, {}).items():
        if k_.startswith("_"):
            continue
        n_ = next((o for o in ns if abs(o["qn"] - float(k_)) < 0.02), None)
        if n_ is None:
            print(f"  WARN {tname}: CRESC_FRONTS {k_} has no note", file=sys.stderr)
            continue
        cut_, pk_, sg_ = (float(x_) for x_ in v_)
        t0_ = qn_to_sec(new_on(n_))
        ps_ = [(0.0, 0.0), (0.06, -cut_), (max(0.07, pk_), -cut_), (max(pk_ + 0.02, sg_), 0.0)]
        vol_add("shape:cresc_front", ("env", [(sec_to_qn(t0_ + x_), d_) for x_, d_ in ps_], True))
        cresc_fronts.append(round(n_["qn"], 3))
    # mvt1 c34 (critic C #3b): HELD_DECRESC_DB (see the default): a decrescendo inside one held note falls in the volume
    # envelope from 0 at its start + 0.2 s to -dB at its end, held to the next moved onset, back to 0 by that onset
    held_decresc = []
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
            vol_add("slow:held_decresc", ("env", [(ta_, 0.0), (b_, -hd_db_), (he_, -hd_db_), (max(he_ + 0.01, nx_), 0.0)], True))
            held_decresc.append([round(a_, 3), round(b_, 3)])
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
            vol_add("level:pickup_sus", ("env", [(a_ - 0.012, 0.0), (a_ - 0.002, pdb_), (b_ - 0.012, pdb_), (b_ - 0.002, 0.0)], True))
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
            vol_add("level:pickup_lift", ("env", [(a_ - 0.01, 0.0), (a_, d_), (sec_qn(b_, tail_[0]), d_),
                                      (sec_qn(b_, tail_[0] + tail_[1]), 0.0)], True))
        else:
            vol_add("level:pickup_lift", ("env", [(a_ - 0.01, 0.0), (a_, d_), (b_, d_), (b_ + 0.02, 0.0)], True))
        pickup_lift.append([round(q_, 3), d_, round(a_, 4), round(b_, 4)])
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
            vol_add("shape:synco_shape", ("env", pts_, True))
            synco_shaped.append(round(q_, 3))
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
            vol_add("shape:slur_pair_release", ("env", [(a_, 0.0), (b_, db_), (stop_ - 0.03, db_), (stop_, 0.0)], True))
            pair_rel.append(round(q2_, 3))
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
                vol_add("shape:detach_dip", ("env", pts_, True))
                detach_dips.append(round(n["qn"], 3))
    # mvt1 c22 (critic A #1): STR_REP_DETACH dips before each eighth of a listed string pedal
    str_rep_dips = []
    if STR_REP_DETACH and family == "string" and STR_REP_DETACH.get("at", {}).get(tname):
        sd_ = STR_REP_DETACH
        for a_, b_ in sd_["at"][tname]:
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
                tb_ = qn_to_sec(min(new_on(o) for o in n1_))
                d_, x_, r_, k_ = sd_["dip_db"], sd_.get("dip_s", 0.08), sd_.get("ramp_s", 0.02), sd_.get("back_s", 0.005)
                vol_add("shape:str_rep_dip", ("env", [(sec_to_qn(tb_ - x_ - r_), 0.0), (sec_to_qn(tb_ - x_), d_),
                                          (sec_to_qn(tb_ + k_), d_), (sec_to_qn(tb_ + k_ + r_), 0.0)], True))
                str_rep_dips.append(round(q1_, 3))
    # mvt1 c15 (critic A #4): the MEAS_TREM alternate-row strokes' level offset (a step per stroke)
    mt_alt_q = [round(n["qn"], 4) for n in ns if n.get("mt_alt")]
    if MEAS_TREM and MEAS_TREM.get("alt_db") and mt_alt_q:
        for n in ns:
            if not n.get("mt_alt"):
                continue
            a_ = new_on(n)
            nx_ = [new_on(o) for o in ns if o["qn"] > n["qn"] + EPS]
            b_ = min(nx_) if nx_ else orig_end[id(n)]
            vol_add("level:meas_trem_alt", ("env", [(a_ - 0.012, 0.0), (a_ - 0.002, MEAS_TREM["alt_db"]),
                                      (b_ - 0.012, MEAS_TREM["alt_db"]), (b_ - 0.002, 0.0)], True))
    # mvt1 c15 (critic C #5): a delayed unison copy fades in under the kept note
    uni_fades = []
    if UNI_DELAY_FADE:
        for n in ns:
            dl_ = UNI_DELAY.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
            if dl_ is None:
                continue
            q1_ = max(new_on(n), dl_)
            vol_add("shape:uni_delay_fade", ("env", [(q1_ - 0.01, 0.0), (q1_, UNI_DELAY_FADE[0]),
                                      (sec_to_qn(qn_to_sec(q1_) + UNI_DELAY_FADE[1]), 0.0)], True))
            uni_fades.append(round(q1_, 3))
    # mvt1 c06 (C #1): arrival weight on the tracks that start a note on the arrival
    arr_w = []
    if family in ("wind", "brass", "string"):
        for qa_, aw_ in sorted(ARRIVAL_WEIGHT_AT.items()):
            pre_, db_ = aw_[0], aw_[1]
            pq_ = aw_[2] if len(aw_) > 2 else 4.0   # mvt1 c08 (critic C #1): the hold-back's length in qn (default 4)
            if not any(abs(n["qn"] - qa_) < 0.05 for n in ns):
                continue
            vol_add("slow:arrival_weight", ("env", [(qa_ - pq_, 0.0), (qa_ - 0.1, pre_), (sec_qn(qa_, 0.05), db_), (qa_ + 0.5, db_),
                                      (qa_ + 1.0, 0.0)], True))
            arr_w.append(qa_)
    # mvt1 c06 (A #3): a slurred string tenuto at f or louder joined as a legato target keeps its weight in dB
    ten_sw = []
    if family == "string" and TENUTO_SWELL_DB:
        for n in ns:
            q0, e_ = n["qn"], orig_end[id(n)]
            if near(q0, ten_q) and n.get("slur") is not None and n.get("leg_target") and base(q0) >= DYN["f"] - 2 \
                    and e_ - q0 >= 0.4:
                t1_ = sec_qn(q0, 0.05)
                vol_add("shape:tenuto_swell", ("env", [(t1_, 0.0), (sec_qn(q0, 0.12), TENUTO_SWELL_DB),
                                          (max(sec_qn(q0, 0.12) + 0.01, e_ - 0.1), TENUTO_SWELL_DB),
                                          (max(sec_qn(q0, 0.12) + 0.02, e_ + 0.05), 0.0)], True))
                ten_sw.append(round(q0, 3))
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
            vol_add("level:phrase_tops", ("env", pts_, True))
            pt_slurs += 1
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
                        vol_add("shape:accent_body", ("env", [(b0_, 0.0), (b1_, bd_), (stop_ - 0.02, bd_), (stop_, 0.0)], True))
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
                    vol_add("shape:accent", ("env", [(q0 - 0.01, 0.0), (sec_qn(q0, sw_[0]), ov), (sec_qn(q0, sw_[1]), ov),
                                              (sec_qn(q0, sw_[2]), 0.0)], True))
                elif ov is not None:   # c11 (A #3)
                    vol_add("shape:accent", ("env", [(q0 - 0.01, 0.0), (q0 + 0.01 * bpm_at(q0) / 60, ov), (q0 + 0.12, ov),
                                              (q0 + 0.3, 0.0)], True))
                else:
                    vol_add("shape:accent", ("env", [(q0 - 0.02, 0.0), (sec_qn(q0, 0.03), ACCENT_DB), (sec_qn(q0, 0.25), ACCENT_DB),
                                              (sec_qn(q0, 0.5), 0.0)]))
                acc_n += 1
    for n in ns:   # c14: marcato body and attack weight (exact breakpoints)
        if n.get("marc"):
            q0, e_ = n["qn"], n["end"]
            t1, t2, t3 = (sec_qn(q0, t_) for t_ in MARC_ATTACK_S)   # c15 (A #4)
            t3 = min(t3, e_ - 0.01)
            vol_add("shape:marc", ("env", [(q0 - 0.01, 0.0), (q0 + 0.01 * bpm_at(q0) / 60, MARC_BODY_DB),
                                      (t1, MARC_BODY_DB + MARC_ATTACK_DB), (t2, MARC_BODY_DB + MARC_ATTACK_DB),
                                      (t3, MARC_BODY_DB), (e_, MARC_BODY_DB), (e_ + 0.05, 0.0)], True))
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
            vol_add("level:note_trim_pluck", ("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
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
            sec = qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"])
            rs_ = next((v_ for k_, v_ in NOTE_TRIM_RAMP_S.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02),
                       0.1 if any(abs(n["qn"] - k_) < 0.02 for k_ in acc_trim_q) else 0.6)
            ramp = rs_ * (orig_end[id(n)] - n["qn"]) / sec   # 0.6 s in qn (c24: per-onset NOTE_TRIM_RAMP_S)
            vol_add("level:note_trim", ("env", trim_shape(n, hit[0], ramp), TRIM_KEY == "score"))   # c09 (A #2); c55: TRIM_KEY
            if TRIM_KEY == "score":
                trim_pairs.append((vol_parts[-1][1], trim_shape(n, hit[0], ramp, None, True)))
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
            if a_ not in rtab_ or (n.get("down_stroke") and not n.get("rep_stroke")) or n.get("rep_sus") or n.get("rep_stac") \
                    or any(a0_ - EPS <= n["qn"] < b0_ for a0_, b0_ in ROW_TRIM_SKIP.get(tname, [])) \
                    or any(o is not n and abs(o["qn"] - n["qn"]) < 0.01 for o in ns) or final(n["qn"]) < rtab_[a_][1] \
                    or (AUTO_REBOW and qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"]) > REBOW_MAX_S) \
                    or not any(o is not n and _lg((o.get("art") or ""))
                               and max(o["qn"] - orig_end[id(n)], n["qn"] - orig_end[id(o)]) <= ROW_TRIM_NEAR_QN + EPS
                               for o in ns):
                continue
            s0_ = new_on(n)
            nm_ = next_moved(n)
            s1_ = nm_ if nm_ is not None else orig_end[id(n)]
            if segs_ and abs(segs_[-1][2] - rtab_[a_][0]) < 1e-6 and s0_ <= segs_[-1][1] + 0.06:
                segs_[-1][1] = max(segs_[-1][1], s1_)
            else:
                segs_.append([s0_, s1_, rtab_[a_][0]])
            row_trimmed.append(round(n["qn"], 3))
        for s0_, s1_, d_ in segs_:
            vol_add("level:row_trim", ("env", [(s0_ - 0.03, 0.0), (s0_ + 0.03, d_), (max(s0_ + 0.04, s1_ - 0.05), d_),
                                      (max(s0_ + 0.05, s1_ + 0.03), 0.0)], True))
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
                vol_add("shape:bloomv", ("bloomv", q0, e))
                bloomv += 1
    for n in ns:   # c04 (A #2): the kept note of a same-patch unison
        b_ = UNI_BOOST.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if b_:
            vol_add("level:uni_boost", ("note", n["qn"], orig_end[id(n)], b_, 0.02))
    # c03 (B #2): divisi chords and double stops play a full-section sample per note. Where k >= 2 notes sound together:
    # -10 log10(k) dB under "div.", -1.5 dB otherwise (non div. double stops); 2-note tremolo chords a further -3 dB.
    # The cut starts 0.1 qn before the chord.
    chord_segs = []
    if family == "string":
        def div_state(q):
            st = None
            for tq, t in sorted(texts_until(staves, q)):
                if META_DB and tname not in META_SKIP_TRACKS and ("metà" in t or has(t, "meta") or (SOLI_AS_META and re.search(r"(?<![a-z])soli\b", t))):
                    st = "half"   # mvt1 c05 (A #5): half the section plays
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
            if k < 2:
                if k == 1 and META_DB and div_state(mid) == "half":
                    chord_segs.append((a_, b_, META_DB))   # mvt1 c05 (A #5): "metà", one note by half the section
                continue
            dbv = -10 * __import__("math").log10(k) if div_state(mid) == "div" else -1.5
            if div_state(mid) == "half":
                dbv = META_DB - 10 * __import__("math").log10(k)
            if all(n.get("art") == "Tremolo" for n in snd):
                dbv -= 3
            chord_segs.append((a_, b_, dbv))
        if chord_segs:
            vol_add("slow:chord", ("chord",))

    def seg_db(q):
        return next((d_ for a_, b_, d_ in chord_segs if a_ - EPS <= q < b_ - EPS), 0.0)

    def chord_db(q):
        # c10 (C #4b): at a printed sf the new chord's cut (divisi / tremolo chord) starts at the sf, not 0.1 qn before
        # it (the held note before the sf fell 3-6 dB ahead of the attack)
        for m_ in sf_q:
            if m_ - 0.1 <= q < m_:
                return seg_db(q)
        return min(seg_db(q), seg_db(q + 0.1))
    if ns and max(orig_end[id(n)] for n in ns) >= END - 0.01:
        vol_add("slow:fade", ("fade",))
    # mvt2 c55: classes, switches and the start cap (see ENV_CLASS)
    _env = __import__("os").environ
    ecls_ = dict(ENV_CLASS, **dict(x_.split("=") for x_ in _env.get("STP_ENV_CLASS", "").split(",") if "=" in x_))
    elay_ = dict(ENV_LAYER, **dict(x_.split("=") for x_ in _env.get("STP_ENV_LAYER", "").split(",") if "=" in x_))
    ons_sc_ = sorted({round(n["qn"], 4) for n in ns})

    def row_class(ps):
        a_, b_ = ps[0][0], ps[-1][0]
        for x0_, x1_, c_, *ex_ in ENV_ROW_CLASS.get(tname, []):   # a fourth element "exact": only the row with that span
            if (abs(a_ - x0_) < 1e-6 and abs(b_ - x1_) < 1e-6) if ex_ else (x0_ - 1e-6 <= a_ and b_ <= x1_ + 1e-6):
                return c_
        if not any(n["qn"] < b_ and orig_end[id(n)] > a_ for n in ns):
            return "slow"
        ins_ = [o_ for o_ in ons_sc_ if a_ + 0.08 < o_ < b_ - 0.08]
        if len(ins_) >= 3 or (ins_ and qn_to_sec(b_) - qn_to_sec(a_) > 6.0):
            return "slow"
        ys_ = [value_at(ps, a_ + (b_ - a_) * (k_ + 0.5) / 100) for k_ in range(100)]
        ext_ = max(ys_, key=abs)
        return "level" if sum(1 for y_ in ys_ if abs(y_ - ext_) < 0.5) >= 70 else "shape"
    for it_ in vol_parts:
        if vol_tags.get(id(it_), "").startswith("auto:"):
            vol_tags[id(it_)] = row_class(it_[1]) + ":" + vol_tags[id(it_)][5:]
    tag_of = lambda it_: vol_tags.get(id(it_), "slow:untagged")

    def mode_of(it_):
        c_, l_ = tag_of(it_).split(":")
        return elay_.get(f"{tname}:{l_}", elay_.get(l_, ecls_.get(c_, "on")))

    def vol_of(items, q):
        saved_ = vol_parts[:]
        vol_parts[:] = items
        try:
            return vol(q)
        finally:
            vol_parts[:] = saved_
    # note spans by moved onset: (moved on, score on, end, next moved on)
    grp_ = {}
    for n in ns:
        g_ = grp_.setdefault(round(n["qn"], 4), [new_on(n), n["qn"], orig_end[id(n)]])
        g_[0], g_[2] = min(g_[0], new_on(n)), max(g_[2], orig_end[id(n)])
    nspans_ = sorted(grp_.values())
    nspans_ = [(m_, q_, e_, nspans_[i_ + 1][0] if i_ + 1 < len(nspans_) else 1e9) for i_, (m_, q_, e_) in enumerate(nspans_)]
    # FILL_PRE_KEEP_SUM (with TRIM_KEY "score"): an early fill that starts before the beat was fitted on the old trim
    # keying, where the trims of the note before were already gone there. Before the beat the fill is changed by minus
    # (trims as written minus trims with the old keying), not under 0 and not over FILL_PRE_KEEP_SUM dB in all, so the
    # fitted sum holds in the transition (Violins II 70: the +6 dB fill from 60 ms before the beat on top of the +5.9 dB
    # trim now held to the beat was a 6 dB spike on the old note's end; simulated S -55 ms)
    fill_rekeyed = []
    if TRIM_KEY == "score" and FILL_PRE_KEEP_SUM and trim_pairs:
        def tdiff_(q):
            return sum((value_at(a_, q) if a_[0][0] <= q < a_[-1][0] else 0.0) - (value_at(b_, q) if b_[0][0] <= q < b_[-1][0] else 0.0)
                       for a_, b_ in trim_pairs)
        for it_, q0_ in fill_items:
            ps_ = it_[1]
            if ps_[0][0] >= q0_ - 1e-6 or mode_of(it_) != "on":
                continue
            # the change is full up to TRIM_XFADE_S / 2 before the beat and fades out linearly to TRIM_XFADE_S / 2 after
            # it (the window in which the trims themselves change), so the sum crossfades from the fitted one to the
            # new keying's without a step
            hx2_ = 0.5 * TRIM_XFADE_S
            ta_, tb_ = qn_to_sec(ps_[0][0]), qn_to_sec(q0_) + hx2_
            ts_ = [ta_ + (tb_ - ta_) * k_ / max(1, int((tb_ - ta_) / 0.01)) for k_ in range(max(1, int((tb_ - ta_) / 0.01)) + 1)]
            cp_ = []
            for t_ in ts_:
                q_ = sec_to_qn(t_)
                f_ = value_at(ps_, q_) if ps_[0][0] <= q_ < ps_[-1][0] else 0.0
                w_ = max(0.0, min(1.0, (tb_ - t_) / (2 * hx2_)))
                cp_.append((q_, round(max(-f_, min(max(0.0, FILL_PRE_KEEP_SUM - f_), -tdiff_(q_) * w_)), 2)))
            if max(abs(d_) for _, d_ in cp_) < 0.5:
                continue
            cp_ = [(cp_[0][0] - 0.002, 0.0)] + cp_ + [(cp_[-1][0] + 0.002, 0.0)]
            vol_add("shape:early_fill_rekey", ("env", cp_, True))
            fill_rekeyed.append([round(q0_, 3), min(d_ for _, d_ in cp_), max(d_ for _, d_ in cp_)])
        if fill_rekeyed:
            print(f"  fills before the beat, changed with the trim keying {tname}: " + ", ".join(f"{q_}({a_:+.1f}..{b_:+.1f})" for q_, a_, b_ in fill_rekeyed), file=sys.stderr)
    # START_SHAPE_CAP: a compensating item where the summed start shapes pass +db
    start_capped = []
    if START_SHAPE_CAP and ns:
        sc_ = START_SHAPE_CAP
        sk_l_ = set(sc_.get("skip_layers", ()))
        its_ = [it_ for it_ in vol_parts if it_[0] == "env" and tag_of(it_).startswith("shape:")
                and tag_of(it_).split(":")[1] not in sk_l_ and mode_of(it_) == "on"]
        for m_, q_, e_, nm_ in nspans_:
            if any(abs(q_ - k_) < 0.02 for k_ in sc_.get("skip", {}).get(tname, [])):
                continue
            t0_ = qn_to_sec(q_)
            ta_, tb_ = t0_ - sc_.get("pre_s", 0.15), min(t0_ + sc_.get("post_s", 0.6), qn_to_sec(min(e_, nm_)))
            loc_ = [it_ for it_ in its_ if it_[1][0][0] < sec_to_qn(tb_) and it_[1][-1][0] > sec_to_qn(max(0.0, ta_))]
            if not loc_ or tb_ <= ta_:
                continue
            ts_ = sorted({round(ta_ + 0.01 * k_, 4) for k_ in range(int((tb_ - ta_) / 0.01) + 1)}
                         | {round(qn_to_sec(x_), 4) for it_ in loc_ for x_, _ in it_[1] if ta_ <= qn_to_sec(x_) <= tb_})
            sv_ = [sum(value_at(it_[1], sec_to_qn(t_)) if it_[1][0][0] <= sec_to_qn(t_) < it_[1][-1][0] else 0.0 for it_ in loc_)
                   for t_ in ts_]
            if max(sv_) <= sc_["db"] + 0.05:
                continue
            ps_ = [(sec_to_qn(t_), round(min(0.0, sc_["db"] - v_), 3)) for t_, v_ in zip(ts_, sv_)]
            k0_ = next(k_ for k_, p_ in enumerate(ps_) if p_[1] < 0)
            k1_ = max(k_ for k_, p_ in enumerate(ps_) if p_[1] < 0)
            ps_ = ([(ps_[k0_ - 1][0], 0.0)] if k0_ > 0 else [(ps_[k0_][0] - 0.002, 0.0)]) + ps_[k0_:k1_ + 1] \
                + ([(ps_[k1_ + 1][0], 0.0)] if k1_ + 1 < len(ps_) else [(ps_[k1_][0] + 0.002, 0.0)])
            vol_add("shape:start_cap", ("env", ps_, True))
            start_capped.append([round(q_, 3), round(max(sv_), 2)])
        if start_capped:
            print(f"  start cap {tname}: " + ", ".join(f"{q_}({v_:+.1f})" for q_, v_ in start_capped), file=sys.stderr)
    # mvt2 c55: LEVEL_ROW_SPLIT, after the start cap (which reads the rows as they were fitted)
    row_levels = []   # [first x, level dB] of the rows split
    for it_ in vol_parts[:]:
        c_, l_ = tag_of(it_).split(":")
        ps_ = it_[1] if it_[0] == "env" else None
        if c_ == "shape" and l_ in ("level_shape", "level_shape_s") and LEVEL_ROW_SPLIT and len(ps_) > 2 and mode_of(it_) == "on":
            # critic C #3: a fitted row that moves inside its note and also carries the note's level: its median
            # over the middle 60 % of its span is one item of class level, the rest the shape item (same sum)
            ys_ = sorted(value_at(ps_, ps_[0][0] + (ps_[-1][0] - ps_[0][0]) * (0.2 + 0.6 * (k_ + 0.5) / 100)) for k_ in range(100))
            md_ = round(0.5 * (ys_[49] + ys_[50]), 2)
            if abs(md_) >= LEVEL_ROW_SPLIT and len(ps_) >= 4 and abs(ps_[0][1]) < 1e-9 and abs(ps_[-1][1]) < 1e-9 \
                    and ps_[1][0] < ps_[-2][0] - 1e-6:
                # the level item keeps the row's own first and last ramps (a plateau between its second and its
                # last-but-one point), so the shape item is 0 at both ends
                k_ = next(i_ for i_, x_ in enumerate(vol_parts) if x_ is it_)
                lp_ = [(ps_[0][0], 0.0), (ps_[1][0], md_), (ps_[-2][0], md_), (ps_[-1][0], 0.0)]
                sh_ = ("env", [(x_, round(d_ - value_at(lp_ + [(lp_[-1][0] + 1e-9, 0.0)], x_), 3)) for x_, d_ in ps_], True)
                lv_ = ("env", lp_, True)
                vol_parts[k_:k_ + 1] = [lv_, sh_]
                vol_tags[id(lv_)], vol_tags[id(sh_)] = "level:" + l_ + "_level", "shape:" + l_
                row_levels.append([round(ps_[0][0], 3), md_])
    vbreaks = [0.0, SE - 1, SE - 0.5, SE]
    env_off, env_capped = collections.Counter(), collections.Counter()
    for it_ in vol_parts:
        if mode_of(it_) == "off":
            env_off[tag_of(it_)] += 1
        elif mode_of(it_).startswith("cap"):
            env_capped[tag_of(it_)] += 1
    vol_parts[:] = [it_ for it_ in vol_parts if mode_of(it_) != "off"]
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
    vbreaks += [x for m_ in sf_q for x in (m_ - 0.1, m_ - 0.001, m_)] if chord_segs else []
    vgrid = sorted(set([round(x, 4) for x in vbreaks] + [round(i * VOL_GRID_QN, 4) for i in range(int((END + 4) / VOL_GRID_QN))]))
    # c10: "env" items flagged exact put their breakpoints into parts.json vol_bp; build_reaper.py adds them to the volume
    # envelope's 0.125 qn grid, so shapes faster than the grid (pre-onset fills, the timpani attack) are written as built
    # mvt2 c55: VOL_BP_ALL: every item's breakpoints (see the default)
    bp_all_ = VOL_BP_ALL and family not in VOL_BP_ALL_SKIP
    vol_bp = sorted({round(x, 4) for item in vol_parts if item[0] == "env" and (bp_all_ or (len(item) > 2 and item[2]))
                     for x, _ in item[1]}
                    | ({round(x, 4) for x in vbreaks if 0 <= x} if bp_all_ else set()))
    # mvt2 c55: "capN" items leave vol_parts and come back as one capped function per (class, N)
    vol_extra = []   # (class, fn)
    capm_ = sorted({(tag_of(it_).split(":")[0], mode_of(it_)) for it_ in vol_parts if mode_of(it_).startswith("cap")})
    for c_, md_ in capm_:
        its_ = [it_ for it_ in vol_parts if tag_of(it_).split(":")[0] == c_ and mode_of(it_) == md_]
        ids_ = {id(it_) for it_ in its_}
        vol_parts[:] = [it_ for it_ in vol_parts if id(it_) not in ids_]
        lim_ = float(md_[3:])
        means_ = []
        for m_, q_, e_, nm_ in nspans_:
            t0_, t1_ = qn_to_sec(q_), qn_to_sec(max(q_ + 0.01, min(e_, nm_)))
            mv_ = sum(vol_of(its_, sec_to_qn(t0_ + (t1_ - t0_) * (k_ + 0.5) / 24)) for k_ in range(24)) / 24
            means_.append((m_, min(nm_, sec_to_qn(qn_to_sec(e_) + 0.5)), mv_))

        def capfn(q, its_=its_, means_=means_, lim_=lim_):
            v_ = vol_of(its_, q)
            for a_, b_, mv_ in means_:
                if a_ <= q < b_:
                    return mv_ + max(-lim_, min(lim_, v_ - mv_))
            return v_
        vol_extra.append((c_, capfn))
    vol_db, last = [], None
    if __import__("os").environ.get("STP_DEBUG_VOL", "").split(":")[0] == tname:   # debug: per-item dB at listed qn
        for q_ in [float(x) for x in __import__("os").environ["STP_DEBUG_VOL"].split(":")[1].split(",")]:
            for it_ in vol_parts:
                d_ = vol_of([it_], q_)
                if abs(d_) > 0.005:
                    print(f"  DBG {tname} {q_}: {d_:+.2f} [{tag_of(it_)}] {str(it_)[:90]}", file=sys.stderr)
    # c26 (A #1, small): after the last release (END) every track holds its level at the release, so the roles and
    # trims that end at END no longer lift the hall tail (Vln I/Vc -16 -> -10 dB over 0.5 qn, Cb -17 -> -11.6 in 0.1 qn)
    has_fade_ = ("fade",) in vol_parts
    # mvt2 c47 (critic C #4): an "env" shape that starts at or after END (a LEVEL_SHAPES fade over the last release)
    # still applies after END, on top of the held level, and holds its last value (before, the hold above dropped it)
    post_end_ = [it_[1] for it_ in vol_parts if it_[0] == "env" and it_[1][0][0] >= END - EPS]

    def lane_of(items, extra):
        """the step lane of some items (+ capped functions) on vgrid, with the hold after END"""
        full_ = lambda q: vol_of(items, q) + sum(f_(q) for f_ in extra)
        ve_ = full_(END - 0.001) if has_fade_ else None
        pe_ = [it_[1] for it_ in items if it_[0] == "env" and it_[1][0][0] >= END - EPS]
        ln_, la_ = [], None
        for q in vgrid:
            v = round(full_(q) if ve_ is None or q < END
                      else ve_ + sum(value_at(ps_, q) for ps_ in pe_ if ps_[0][0] <= q + EPS), 2)
            if v != la_:
                ln_.append((q, v)); la_ = v
        return ln_
    vol_db = lane_of(vol_parts[:], [f_ for _, f_ in vol_extra])
    vol_cls = {c_: lane_of([it_ for it_ in vol_parts if tag_of(it_).split(":")[0] == c_], [f_ for k_, f_ in vol_extra if k_ == c_])
               for c_ in ("level", "shape")}
    vol_tag_n = dict(sorted(collections.Counter(tag_of(it_) for it_ in vol_parts).items()))
    vol_layers = {}
    if _env.get("STP_LAYERS"):   # test builds: one lane per layer
        for t_ in vol_tag_n:
            vol_layers[t_] = lane_of([it_ for it_ in vol_parts if tag_of(it_) == t_], [])
    cc15 = []
    if family == "string" or (family == "brass" and stem.startswith("1FH")):   # c02: Horn 3 con sord. on the 1FH ConSordino script
        state = None
        # c05 (A #3): Horns 3-4 share a staff; Horn 4's own "con sord." is a part-only tag that mockup.ly removes
        sord_staves = staves + (["Hn3"] if tname == "Horn 4" else [])
        for q in sorted({0.0} | {tq for tq, _ in texts_until(sord_staves, END)}):
            s = text_state(q, ["con sord", "gli altri con sord"], ["senza sord", "via sord"], sord_staves)
            # mvt2 v600 port (c27): "via sord." (mutes off) at the last chord prepares the next movement: a change with
            # no later note is not written (it would switch CC15 off under the held chord)
            if s != state and q > 0 and not any(n["qn"] >= q - EPS for n in ns):
                continue
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
    if family == "string" and not stem.startswith("Basses"):
        def sul_state(q):
            st = None
            for tq, t in sorted(texts_until(staves, q)):
                m = re.search(r"sul ([dgca])\b", t)
                if m:
                    st = m.group(1)
                elif has(t, "ord.") or has(t, "unis."):
                    st = None
            return st
        last = 0
        for n in ns:
            st = sul_state(n["qn"])
            val = 0 if st is None else (127 if st in "dgc" else (20 if n["pitch"] <= 74 else 127))
            if val != last:
                cc70.append((round(max(0.0, min(early_time(n["qn"]), new_on(n) - 0.03)), 4), val)); last = val

    # mvt1 c14 (critic A #2): CC36 round-robin resets at the measured-tremolo run starts (MEAS_TREM "rr_runs")
    cc36 = [(round(max(0.0, new_on(n) - 0.02), 4), 127) for n in ns if n.get("rr_start")]
    cc36 = sorted(cc36 + [(round(float(q_), 4), 127) for q_ in RR_RESET_AT.get(tname, [])])   # mvt2 c49 (A #1)

    # c03: apply the note-start leads. A note that overlaps a moved legato target ends LEG_OVERLAP after its new onset;
    # keyswitches stay at least 0.03 qn before their (moved) note.
    out_notes = []
    dropped = 0
    for n in ns:
        if (round(n["qn"], 3), n["pitch"]) in UNI_DROP.get(tname, set()):   # c04 (A #2): same-patch unison copy
            dropped += 1
            continue
        e = n["end"]
        for o in ns:
            if o.get("leg_prev") is n and id(o) in shift and abs(e - (o["qn"] + LEG_OVERLAP)) < 0.01:
                e = new_on(o) + LEG_OVERLAP
        q1 = new_on(n)
        dl_ = UNI_DELAY.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if dl_ is not None:   # c17 (B #6)
            q1 = max(q1, dl_)
        out_notes.append({"qn": round(q1, 4), "dur": round(max(0.02, e - q1), 4), "pitch": n["pitch"], "vel": n["vel"],
                          "sq": round(n["qn"], 4), "_art": n.get("art")})   # sq: score onset (analysis only)
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
    for k_ in ks:
        nn = k_.pop("note")
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
            if a["_art"] == "Tremolo" and AUTO_REBOW_SKIP_TREM:
                continue   # mvt2 v600 port (c27): a Sus MAX re-bow would turn a held tremolo into a sustain
            listed_ = any(q0_ < p_ < e_ for p_ in rebow_pts)   # mvt1 c02: listed points, the keyswitch back below
            if t1_ - t0_ <= REBOW_MAX_S and not listed_:
                continue
            if not listed_ and any(abs(a["sq"] - s_) < 0.02 for s_ in AUTO_REBOW_SKIP.get(tname, ())):
                continue   # mvt2 c31: listed score onsets keep one bow (a new lead lengthened them past REBOW_MAX_S)
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
                if not any(abs(k__["qn"] - kq_) < 0.03 for k__ in ks):
                    ks.append({"qn": kq_, "pitch": ks_lookup(stem, nxt_["_art"])[1], "art": nxt_["_art"]})
            # the next note keeps (or gets) its own keyswitch, so the pieces may switch to REBOW_ART
            a["_rebow_back"] = True
            # mvt2 v600 port (c27): a chord partner that starts with this note and ends with it (or up to 0.15 qn earlier,
            # e.g. cut before a same-pitch onset) is split at the same points, so it needs the same keyswitch back
            for b in out_notes:
                if b is not a and abs(b["qn"] - q0_) < 0.05 and abs(b["qn"] + b["dur"] - e_) < 0.15 and b["_art"] == a["_art"]:
                    b["_rebow_back"] = True
        if auto_:
            print(f"  {tname}: {auto_} automatic re-bow points", file=sys.stderr)
    for p_ in sorted(rebow_pts):
        for a in [a for a in out_notes if a["qn"] + 0.1 < p_ < a["qn"] + a["dur"] - 0.1]:
            e_ = a["qn"] + a["dur"]
            art_ = a["_art"] if a["_art"] in REBOW_SAME_ROWS else REBOW_ART_BY.get(tname, REBOW_ART)   # mvt2 v600 port (c27), c34
            if a["_art"] != art_ and not a.get("_rebow_back") and any(b["_art"] != art_ for b in out_notes if b["qn"] >= e_ - 0.1 and b is not a):
                raise SystemExit(f"REBOW_AT {tname} {p_}: a later note would need a keyswitch back")
            if a["_art"] != art_ and not any(abs(k_["qn"] - (p_ - 0.02)) < 0.001 for k_ in ks):
                ks.append({"qn": round(p_ - 0.02, 4), "pitch": ks_lookup(stem, art_)[1], "art": art_})
            gap_ = REBOW_GAP_QN
            if round(p_, 4) in soft_gap_pts:   # mvt2 c44 (critic A #1): a printed soft repeat's bow change is heard
                gap_ = max(REBOW_GAP_QN, p_ - qn_before(p_, soft_gap_own.get(round(p_, 4), STR_REP_NEW_BOW["soft_gap_s"])))
            a["dur"] = round(p_ - gap_ - a["qn"], 4)
            out_notes.append({"qn": round(p_, 4), "dur": round(e_ - p_, 4), "pitch": a["pitch"], "vel": REBOW_VEL or int(round(value_at(REBOW_VEL_BY_CC, base(p_)))),
                              "sq": round(p_, 4), "_art": art_, "_rebow_back": a.get("_rebow_back")})
            rebow_arts.append(art_)
            # mvt1 c01: for tools/fit_rebows.py; c03: plus the piece's start (the note start or the previous re-bow) and
            # the automatic point before any REBOW_MOVES (None for listed points), for tools/space_rebows.py
            rebow_list.append([round(p_, 4), round(e_, 4), a["pitch"], round(a["qn"], 4), rebow_auto.get(round(p_, 3))])
            rebow_n += 1
    # mvt2 c29 (critic A #1, B #1): data fitted to an earlier set of re-bows. A REBOW_FILLS list with no re-bow at its
    # key (within 0.01 qn) lands on a continuous note (c28: Violins II 44.341/50.352 swelled 8-15 dB into a hole after
    # REBOW_AT moved the points); a LOOP_PROFILES entry on a note that is now re-bowed runs out of phase with the
    # restarted samples (c28: 8-11 dB wobble). Both are warnings: refit (tools/fit_rebows.py) or delete the entry
    rb_q_ = [r_[0] for r_ in rebow_list]
    for k_ in REBOW_FILLS.get(tname, {}):
        if not k_.startswith("_") and not any(abs(float(k_) - q_) < 0.01 for q_ in rb_q_):
            print(f"WARNING {tname}: REBOW_FILLS {k_} has no re-bow", file=sys.stderr)
    for k_ in LOOP_PROFILES.get(tname, {}):
        if not k_.startswith("_") and any(abs(r_[3] - float(k_)) < 0.02 for r_ in rebow_list):
            print(f"WARNING {tname}: LOOP_PROFILES {k_} is on a re-bowed note", file=sys.stderr)
    # mvt2 c32 (critic B #1): a LOOP_FILLS lift timed (seconds after the note's moved start) past the end of the note's
    # first piece (the note end or its first re-bow) lands on a fresh sample start or on the next note (c31: 5-14 dB
    # bumps from series 1 fills after AUTO_REBOW split the notes). Refit (tools/fit_loops.py) or delete the entry
    for k_, lifts_ in LOOP_FILLS.get(tname, {}).items():
        if k_.startswith("_"):
            continue
        pcs_ = sorted((o_ for o_ in out_notes if abs(o_.get("sq", -99) - float(k_)) < 0.02), key=lambda o_: o_["qn"])
        if not pcs_:
            print(f"WARNING {tname}: LOOP_FILLS {k_} has no note", file=sys.stderr)
            continue
        p0_ = pcs_[0]
        len_s_ = qn_to_sec(p0_["qn"] + p0_["dur"]) - qn_to_sec(p0_["qn"])
        for t_, _, w_ in lifts_:
            if t_ + w_ > len_s_ + 0.01:
                print(f"WARNING {tname}: LOOP_FILLS {k_} lift at {t_} s ends after the note's first piece "
                      f"({len_s_:.2f} s)", file=sys.stderr)
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
    ks_cut = 0
    for k_ in ks:
        if _lg(k_["art"]):
            continue
        for a in out_notes:
            if a["_art"] and _lg(a["_art"]) and a["qn"] + EPS < k_["qn"] < a["qn"] + a["dur"] - EPS:
                a["dur"] = round(max(0.02, k_["qn"] - 0.01 - a["qn"]), 4)
                ks_cut += 1
    if ks_cut:
        print(f"  {tname}: {ks_cut} legato notes ended before a keyswitch", file=sys.stderr)
    fresh_on = [(new_on(n), n["qn"]) for n in ns if n.get("fresh") and id(n) in shift]
    if family != "timp" and CC7_POINTS.get(tname):   # mvt1 c36: a CC7 test lane (CC7 127 from qn 0)
        cc7 = [(0.0, 127)] + sorted((round(float(q_), 4), int(v_)) for q_, v_ in CC7_POINTS[tname])
    # mvt1 c36 (critic C #1): where the envelope falls at each subito-softer mark of this track's staves: the moved
    # onset of the track's earliest note on the mark (a fresh entry's lead), else the mark itself (SUBITO_TAIL in
    # build_reaper.vol_points)
    subito_falls = [[round(q_, 3), round(min([new_on(n) for n in ns if abs(n["qn"] - q_) < EPS] + [q_]), 4)]
                    for q_ in sub_soft_q]
    for f_, fsq in fresh_on:   # c09 (A #3); compared on sq and with a 0.001 tolerance (out_notes qn are rounded:
        for a in out_notes:    # the first version cut the fresh note itself to 0.02 qn)
            if a["sq"] < fsq - 0.001 and a["qn"] < f_ - 0.001 and a["qn"] + a["dur"] > f_ - 0.03:
                a["dur"] = round(max(0.02, f_ - 0.03 - a["qn"]), 4)
    ks_rowchange = []
    if KS_ROWCHANGE_LEAD_S > 0 and family in KS_ROWCHANGE_FAMILIES and tname not in KS_ROWCHANGE_SKIP and ks:   # mvt2 c52
        ks.sort(key=lambda k_: k_["qn"])

        def gov_(q_):   # index of the keyswitch that governs a note-on at q_
            i_ = -1
            for j_, k_ in enumerate(ks):
                if k_["qn"] <= q_ + 1e-6:
                    i_ = j_
                else:
                    break
            return i_
        for a in sorted(out_notes, key=lambda a_: a_["qn"]):
            gi_ = gov_(a["qn"])
            if gi_ < 0 or not _lg(ks[gi_]["art"]):
                continue
            snd_ = [b_ for b_ in out_notes if b_ is not a and b_["qn"] < a["qn"] - 1e-4 and b_["qn"] + b_["dur"] > a["qn"] + 1e-4]
            if len(snd_) != 1 or snd_[0]["pitch"] == a["pitch"] or any(b_ is not a and abs(b_["qn"] - a["qn"]) < 0.02 for b_ in out_notes):
                continue
            pi_ = gov_(snd_[0]["qn"])
            if (ks[pi_]["art"] if pi_ >= 0 else first_art) == ks[gi_]["art"] or pi_ == gi_:
                continue
            lo_ = max(b_["qn"] for b_ in out_notes if b_["qn"] < a["qn"] - 1e-4) + KS_ROWCHANGE_GUARD_QN
            if gi_ > 0:
                lo_ = max(lo_, ks[gi_ - 1]["qn"] + 0.01)
            kq_ = round(max(lo_, sec_to_qn(qn_to_sec(a["qn"]) - KS_ROWCHANGE_LEAD_S)), 4)
            if kq_ < ks[gi_]["qn"] - 1e-4:
                ks[gi_]["qn"] = kq_
            ks_rowchange.append([a["qn"], round((qn_to_sec(a["qn"]) - qn_to_sec(ks[gi_]["qn"])) * 1000)])
    phr_src = [[a["qn"], round(a["qn"] + a["dur"], 4), a["sq"], a["_art"] or "", a["pitch"]] for a in out_notes]   # mvt2 c45
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
        "leads": dict(lead_stats), "notches": len(notches), "unison_dropped": dropped, "bloomv": bloomv, "bloomv_skip": bloomv_skip, "timp_hp": timp_hp,
        "pitch_trimmed": pitch_trimmed, "early_fills": early_n, "loop_fills": loop_n, "tie_slurred": tie_slurred, "metric_vel": dict(metric_n), "metric_db": dict(metric_db_n), "div_entries": div_entries, "extra_leads": extra_used, "leg_leads": leg_used, "port": port_done, "bcsoft": bcsoft_n,
        "hpgain": [[round(i[1], 3), round(i[2], 3), i[4]] for i in vol_parts if i[0] == "hpgain"],
        "acc_vel_fixed": acc_vel_fixed, "rep_retongued": rep_retongued, "arrival_weight": arr_w, "tenuto_swell": ten_sw,
        "down_strokes": [round(n["qn"], 3) for n in ns if n.get("down_stroke")],
        **({"rep_strokes": rep_strokes, "rep_rebows": sorted(rep_rebow_q)} if (rep_strokes or rep_rebow_q) else {}),
        **({"rep_sus_gaps": rep_sus_gaps} if rep_sus_gaps else {}),
        "trem_entries": trem_entries,
        "rebows": sorted(rebow_list), "rebow_fill_ends": rebow_fill_ends, "restrikes": restrikes, "breath_splits": breath_splits, "trem_splits": trem_splits, "slur_rep_merged": slur_rep_merged,
        "short_strokes": [round(n["qn"], 3) for n in ns if n.get("short_stroke")],
        "pt_slurs": pt_slurs,
        "hp_chained": hp_chained, "loud_swells": loud_swells, "hp_soft": hp_soft, "hp_soft_acc": hp_soft_acc, "hp_bridged": hp_bridged, "bc_skipped": bc_skipped, "roles_chained": role_chained, "accent_db": acc_n, "accent_on_arrival": acc_on_arr, "detached_accents": det_n,
        "acc_sus": [round(n["qn"], 3) for n in ns if n.get("acc_sus")],
        "timp_chain_skip": timp_chain_skip, "meas_trem": meas_trem, "cc1_fronts": cc1_fronts, "acc_fitted": acc_fitted, "accent_body": acc_body, "acc_trimmed": sorted(round(x_, 3) for x_ in acc_trim_q), "row_trimmed": row_trimmed,
        "_phr": phr_src,
        "ks_rowchange": ks_rowchange,
        "rep_gap_at": rep_gap_at,
        "ks": ks, "cc1": cc1, "cc11": cc11, "cc15": cc15, "cc7": cc7, "cc70": cc70, "cc36": cc36, "pair_release": pair_rel, "detach_dips": detach_dips, "str_rep_dips": str_rep_dips, "meas_trem_alt": mt_alt_q, "uni_fades": uni_fades, "slur_start_sus": sorted(round(n["qn"], 3) for n in ns if n.get("slur_start_sus")), "slur_start_joins": slur_start_joins, "pickup_sus": pickup_sus, "pickup_lift": pickup_lift, "synco_shaped": synco_shaped, "det_lead_clamped": det_lead_clamped, "retongue_leads": retongue_leads, "wide_leg": wide_leg, "held_decresc": held_decresc, "caesura_lifts": caesura_lifts, "hp_curved": [[round(a_, 3), round(b_, 3)] for a_, _, b_, _, _ in hp_curved], "portato_tails": sorted(round(n["qn"], 3) for n in ns if n.get("portato_tail")), "stac_leads": stac_leads, "rest_short": rest_short, "end_at": end_at, "slur_head_leads": slur_head_leads, "group_leads": group_leads, "reattack_leads": reattack_leads, "subito_fresh": subito_fresh, "subito_falls": subito_falls, "cresc_fronts": cresc_fronts, "join_notch_s": join_notch_s, "dyn_curve": dyn_curve, "vol_db": vol_db, "vol_bp": vol_bp, "vol_cls": vol_cls, "vol_tags": vol_tag_n, **({"env_off": dict(env_off)} if env_off else {}), **({"env_capped": dict(env_capped)} if env_capped else {}), **({"start_capped": start_capped} if start_capped else {}), **({"rebow_levels": rebow_levels} if rebow_levels else {}), **({"trim_kept": sorted(set(trim_kept))} if trim_kept else {}), **({"fill_rekeyed": fill_rekeyed} if fill_rekeyed else {}), **({"row_levels": row_levels} if row_levels else {}), **({"vol_layers": vol_layers} if vol_layers else {}), "post_end_shapes": [[[round(x_, 4), round(d_, 2)] for x_, d_ in ps_] for ps_ in post_end_],
        "hairpins": [[round(a, 4), round(b, 4), k] for a, b, k in hps],
        # mvt2 c48: fp marks with FP_SPIKE_AT_MARK, [mark qn, qn where the attack has fallen] (build_reaper's soft-decrescendo
        # trim hold reads a hairpin printed at the mark from after the fall, not from the attack's f)
        "fp_falls": [[round(q_, 4), round(FP_FALL_AT[round(q_, 4)], 4)] for q_, d_ in marks
                     if d_ == "fp" and round(q_, 4) in FP_FALL_AT],
        "range": [min(pitches), max(pitches)] if pitches else None,
        "ks_clash": clash,
        "art_counts": dict(collections.Counter([n.get("art") for n in ns] + rebow_arts)),
    }


# mvt1 c00: unpitched percussion (family "perc"). The notes come from the event list's drum events (mockup.ly logs
# drum-type and length), not from the MIDI: PERC_MAP {track: {drum type: {"key", optional "vel", "lead_s", "min_s"}}}.
# Tied drum notes are one stroke; a stroke rings for at least min_s seconds (default PERC_MIN_S; the cymbal and tam-tam
# samples are let-ring recordings, and a note-off starts their release). Velocity follows the printed dynamic (PERC_VEL)
# unless the map gives one. CC11 is held at 127 (the patches' Controller 11 is a plain volume).
PERC_MAP = globals().get("PERC_MAP", {})   # set in build/score_config.py
PERC_MIN_S = globals().get("PERC_MIN_S", 9.0)
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
            q1 = qn_before(q, spec.get("lead_s", 0.0)) if spec.get("lead_s") else q
            if spec.get("delay_s"):   # mvt1 c03 (critic C #3): a struck note starts this late (lead_s is applied first)
                q1 = sec_to_qn(qn_to_sec(q1) + spec["delay_s"])
            n = {"qn": round(q1, 4), "sq": round(q, 4), "pitch": spec["key"], "vel": vel, "_end": q + ln, "_end_last": q,
                 "_min_s": spec.get("min_s", PERC_MIN_S)}
            out_notes.append(n); last[v[0]] = n
    for n in out_notes:
        e_ = max(n.pop("_end"), sec_to_qn(qn_to_sec(n["sq"]) + n.pop("_min_s")))
        n.pop("_end_last")
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
    return {
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
                        UNI_DELAY[tb][(round(nb["qn"], 3), nb["pitch"])] = keep[1]["end"] - UNI_DELAY_OVERLAP_QN
                    else:
                        UNI_DROP[tb].add((round(nb["qn"], 3), nb["pitch"]))
            UNI_BOOST[keep[0]][(round(keep[1]["qn"], 3), keep[1]["pitch"])] = round(10 * __import__("math").log10(len(grp)), 2)
            print(f"  unison qn {na['qn']:.2f} pitch {na['pitch']}: keep {keep[0]}, drop "
                  f"{[tb for tb, _ in grp if tb != keep[0]]}", file=sys.stderr)


def _step(pts, q, d=0.0):
    v = d
    for q_, v_ in pts:
        if q_ <= q + EPS:
            v = v_
        else:
            break
    return v


def apply_phrase_shape(parts):
    """mvt2 c45 (ONE_TIME c45: EW-TEMPLATE-PLAN sections 7-8 and 10; critic A #1, critic B's measured depth): phrase
    shapes. A phrase is a run of a track's sustained notes with gaps under PS["gap_s"], at least PS["min_s"] long, with at
    least PS["min_onsets"] onsets and two pitches (so held pedals and re-bowed single notes keep their fitted shapes).
    Classes: "skip" when it is longer than PS["max_s"] (a continuous accompaniment), when printed hairpins cover more than PS["hairpin_cover"] of it (a build or a printed swell: the
    hairpin is already the shape), when it ends after PS["skip_after_qn"] or overlaps a PS["skip_spans"] window (accented
    music, fitted passages); "lyrical" otherwise. A lyrical phrase gets
      - a level arch in the volume envelope (vol_db, dB; post-fader sends keep the hall's tail, S3): PS["level"][family]
        or ["default"], knots (anchor, value, dB) with anchor "on" = seconds after the first onset, "frac" = fraction of
        the phrase, "end" = seconds before the last note-off; scaled by PS["scale_by_cc"] at the printed dynamic;
        strings take their own knots (taper only) and only where no decrescendo is printed over the last second;
      - a timbre arch on CC1 for the tracks in PS["cc1"] (vibrato-crossfade patches): -depth_start at the onset, 0 at
        PS["cc1"]["peak"] of the phrase, -depth_end at the end, never below the track's floor (and only where CC1 is at
        or above the floor; Flautando's CC1 20 is untouched).
    Doublings (PS["groups"]: {tracks, from, to, leader}) take the leader's phrases and class inside the window, so every
    track of the group gets the same curve (later groups win). Between phrases the offsets ramp back to 0 over
    PS["ramp_out_s"] after an end and in over PS["ramp_in_s"] before a start."""
    PS = PHRASE_SHAPE
    if not PS:
        for p in parts:
            p.pop("_phr", None)
        return
    bytn = {p["name"]: p for p in parts}

    def phrases_of(p):
        if p["family"] in PS.get("skip_families", ()):
            return []
        src = sorted(x for x in p.get("_phr", []) if not any(k_ in x[3] for k_ in PS.get("skip_arts", ())))
        out, cur = [], []
        for x in src:
            if cur and qn_to_sec(x[0]) - qn_to_sec(max(c[1] for c in cur)) > PS["gap_s"]:
                out.append(cur); cur = []
            cur.append(x)
        if cur:
            out.append(cur)
        res = []
        for ph in out:
            q0, q1 = ph[0][0], max(c[1] for c in ph)
            if qn_to_sec(q1) - qn_to_sec(q0) < PS["min_s"] or len({c[2] for c in ph}) < PS["min_onsets"] \
                    or len({c[4] for c in ph}) < 2:
                continue
            cover = 0.0
            for a_, b_, k_ in p.get("hairpins", []):
                cover += max(0.0, min(b_, q1) - max(a_, q0))
            cls = "lyrical"
            if qn_to_sec(q1) - qn_to_sec(q0) > PS.get("max_s", 1e9):
                cls = "skip:long"   # a continuous accompaniment, not a phrase
            elif cover > PS["hairpin_cover"] * (q1 - q0):
                cls = "skip:hairpin"
            elif q1 > PS.get("skip_after_qn", 1e9):
                cls = "skip:end"
            elif any(a_ < q1 - EPS and q0 < b_ - EPS for a_, b_ in PS.get("skip_spans", {}).get(p["name"], [])
                     + PS.get("skip_spans", {}).get("*", [])):   # any overlap
                cls = "skip:span"
            dec_end = any(k_ == "decresc" and b_ > sec_to_qn(qn_to_sec(q1) - 1.0) - EPS and a_ < q1
                          for a_, b_, k_ in p.get("hairpins", []))
            res.append({"q0": q0, "q1": q1, "cls": cls, "fam": p["family"], "dec_end": dec_end,
                        "cc": _step(p.get("dyn_curve", []), q0 + 0.01, 46), "src": p["name"]})
        return res

    own = {p["name"]: phrases_of(p) for p in parts}
    use = {k: list(v) for k, v in own.items()}
    for g in PS.get("groups", []):
        lead = own.get(g["leader"], [])
        inwin = lambda ph: g["from"] - EPS <= (ph["q0"] + ph["q1"]) / 2 <= g["to"] + EPS
        for t in g["tracks"]:
            if t not in use:
                continue
            use[t] = [ph for ph in use[t] if not inwin(ph)] + [dict(ph, src=g["leader"]) for ph in lead if inwin(ph)]
            use[t].sort(key=lambda ph: ph["q0"])

    def knots_of(ph, fam):
        t0, t1 = qn_to_sec(ph["q0"]), qn_to_sec(ph["q1"])
        L = t1 - t0
        spec = PS["level"].get(fam, PS["level"]["default"])
        if fam == "string" and ph["dec_end"] and PS["level"].get("string_skip_dec_end", True):
            return None
        sc = value_at(PS.get("scale_by_cc", [(0, 1.0)]), ph["cc"])
        ks = []
        for anc, x, db in spec:
            t = t0 + x if anc == "on" else (t0 + x * L if anc == "frac" else t1 - x)
            ks.append((min(max(t, t0), t1), db * sc))
        ks.sort()
        return ks

    def offset_fn(phs, knot_fn):
        segs = [(qn_to_sec(ph["q0"]), qn_to_sec(ph["q1"]), knot_fn(ph)) for ph in phs]
        segs = [s_ for s_ in segs if s_[2]]
        allk = []
        for i, (t0, t1, ks) in enumerate(segs):
            prev_end = segs[i - 1][1] if i else -1e9
            nxt = segs[i + 1][0] if i + 1 < len(segs) else 1e9
            if t0 - PS["ramp_in_s"] > prev_end + PS["ramp_out_s"]:
                allk.append((t0 - PS["ramp_in_s"], 0.0))
            allk += ks
            if t1 + PS["ramp_out_s"] < nxt - PS["ramp_in_s"]:
                allk.append((t1 + PS["ramp_out_s"], 0.0))
        allk.sort()

        def f(q):
            if not allk:
                return 0.0
            t = qn_to_sec(q)
            if t <= allk[0][0] or t >= allk[-1][0]:   # the first and last knots are the 0-valued ramp ends
                return 0.0
            for (ta, va), (tb, vb) in zip(allk, allk[1:]):
                if ta <= t <= tb:
                    return va + (vb - va) * (t - ta) / (tb - ta) if tb > ta else vb
            return 0.0
        spans_ = [(sec_to_qn(max(0.0, s_[0] - PS["ramp_in_s"])), sec_to_qn(s_[1] + PS["ramp_out_s"])) for s_ in segs]
        return f, spans_

    def regrid(lane, fn, spans_, step, conv):
        if not spans_:
            return lane
        qs = {round(q_, 4) for q_, _ in lane}
        for a_, b_ in spans_:
            k = int(a_ / step)
            while k * step <= b_ + step:
                qs.add(round(k * step, 4)); k += 1
        out, last = [], None
        for q in sorted(qs):
            v = conv(_step(lane, q, lane[0][1] if lane else 0), fn(q), q)
            if v != last:
                out.append((q, v)); last = v
        return out

    report = collections.Counter()
    for p in parts:
        phs = use.get(p["name"], [])
        for ph in phs:
            report[(p["name"], ph["cls"])] += 1
        lyr = [ph for ph in phs if ph["cls"] == "lyrical"]
        p["phrase_shape"] = [[round(ph["q0"], 3), round(ph["q1"], 3), ph["cls"], ph["src"]] for ph in phs]
        p.pop("_phr", None)
        if not lyr:
            continue
        fam = p["family"]
        fv, sp = offset_fn(lyr, lambda ph: knots_of(ph, ph["fam"]))   # a doubling takes its leader's family shape
        p["vol_db"] = regrid(p["vol_db"], fv, sp, PS.get("vol_grid_qn", 0.125),
                             lambda old, off, q: round(old + off, 2))
        c1 = next((v_ for k_, v_ in PS.get("cc1", {}).items() if p["name"].startswith(k_)), None)
        if c1 and p.get("cc1") and p["name"] not in PS.get("cc1_skip", ()):
            def kn1(ph, c1=c1):
                t0, t1 = qn_to_sec(ph["q0"]), qn_to_sec(ph["q1"])
                return [(t0, -c1["depth_start"]), (t0 + c1.get("peak", 0.44) * (t1 - t0), 0.0), (t1, -c1["depth_end"])]
            f1, sp1 = offset_fn(lyr, kn1)
            fl = c1["floor"]
            p["cc1"] = regrid(p["cc1"], f1, sp1, CC_GRID_QN,
                              lambda old, off, q, fl=fl: old if old < fl else int(round(max(fl, min(127, old + off)))))
    for (t, c), k in sorted(report.items()):
        print(f"  phrase shape {t}: {k} {c}", file=sys.stderr)


def apply_vol_tail_hold(parts):
    """mvt2 c46 (critic C #6, S3): VOL_TAIL_HOLD {"s", "min_gap_qn", "min_fall_db", "families"}: where a track's notes stop
    for more than min_gap_qn, a volume-envelope fall of more than min_fall_db that starts within s seconds of the
    note-off is held at the note-off level until s seconds after it, then falls over about 0.1 s (before the next onset).
    The volume envelope acts after the hall, so an early fall cut the release tail. parts.json `vol_tail_holds`."""
    VT = VOL_TAIL_HOLD
    if not VT:
        return

    def at(lane, q):
        if not lane:
            return 0.0
        if q <= lane[0][0]:
            return lane[0][1]
        for (qa, va), (qb, vb) in zip(lane, lane[1:]):
            if qa <= q <= qb:
                return va + (vb - va) * (q - qa) / (qb - qa) if qb > qa else vb
        return lane[-1][1]
    for p in parts:
        p["vol_tail_holds"] = []
        if p["family"] not in VT.get("families", ("wind", "brass", "string")) or not p.get("notes") or not p.get("vol_db"):
            continue
        iv = sorted((n["qn"], n["qn"] + n["dur"]) for n in p["notes"])
        runs = []
        for a_, b_ in iv:
            if runs and a_ <= runs[-1][1] + EPS:
                runs[-1][1] = max(runs[-1][1], b_)
            else:
                runs.append([a_, b_])
        lane = [tuple(x) for x in p["vol_db"]]
        for (a0, e), (n_, _) in zip(runs, runs[1:]):
            if n_ - e <= VT.get("min_gap_qn", 0.25):
                continue
            th = min(sec_to_qn(qn_to_sec(e) + VT.get("s", 0.5)), n_ - 0.02)
            if th <= e + EPS:
                continue
            ve = at(lane, e)
            inner = [v for q, v in lane if e < q <= th] + [at(lane, th)]
            if min(inner) >= ve - VT.get("min_fall_db", 1.0):
                continue
            tr = min(n_ - 0.01, sec_to_qn(qn_to_sec(th) + 0.1))
            vr = at(lane, tr)
            lane = [x for x in lane if not (e - EPS < x[0] < tr + EPS)] + [(round(e, 4), round(ve, 2)), (round(th, 4), round(ve, 2)), (round(tr, 4), round(vr, 2))]
            lane.sort()
            p["vol_tail_holds"].append([round(e, 3), round(th, 3), round(ve - min(inner), 2)])
        p["vol_db"] = [list(x) for x in lane]
        if p["vol_tail_holds"]:
            print(f"  vol tail hold {p['name']}: {len(p['vol_tail_holds'])} " + ", ".join(f"{h[0]}(-{h[2]})" for h in p["vol_tail_holds"]), file=sys.stderr)


def apply_track_doubles(parts):
    bytn = {p["name"]: p for p in parts}
    for dst_n, spec in TRACK_DOUBLES.items():
        src, dst = bytn[spec["src"]], bytn[dst_n]
        art = spec.get("art", "Sus MAX"); gap = REBOW_GAP_QN
        kart, kp = ks_lookup(dst["stem"], art)
        dst["doubles"] = []
        for si_, (q0, q1) in enumerate(spec["spans"]):
            cc7v = int(spec["cc7"][si_]) if isinstance(spec.get("cc7"), (list, tuple)) else int(spec.get("cc7", 90))   # per span
            cc7d = spec.get("cc7_dst", cc7v)   # the copy's own value ("cc7_dst": one value or one per span)
            cc7d = int(cc7d[si_]) if isinstance(cc7d, (list, tuple)) else int(cc7d)
            chains = {}
            for n in sorted(src["notes"], key=lambda n: n["qn"]):
                if q0 - 0.5 <= n.get("sq", n["qn"]) <= q1 + 1e-6:
                    chains.setdefault(n["pitch"], []).append(n)
            if not chains:
                raise SystemExit(f"TRACK_DOUBLES {dst_n}: no source note in {q0}-{q1}")
            a = min(c[0]["qn"] for c in chains.values()); b = max(c[-1]["qn"] + c[-1]["dur"] for c in chains.values())
            if any(n["qn"] < b + 0.5 and n["qn"] + n["dur"] > a - 0.5 for n in dst["notes"]):
                raise SystemExit(f"TRACK_DOUBLES {dst_n}: the track is not idle over {a:.2f}-{b:.2f}")
            def step(lane, q, d=None):
                v = d
                for q_, v_ in lane or []:
                    if q_ <= q + 1e-9:
                        v = v_
                return v
            cur_art = dst["first_art"]
            for k_ in sorted(dst["ks"], key=lambda k: k["qn"]):
                if k_["qn"] <= a:
                    cur_art = k_["art"]
            for pitch, ch in chains.items():
                st = [n["qn"] for n in ch]; e = ch[-1]["qn"] + ch[-1]["dur"]
                mids = [0.5 * (x + y) for x, y in zip(st, st[1:] + [e])]
                cuts = [st[0]]
                for m in mids:
                    if qn_to_sec(m) - qn_to_sec(cuts[-1]) >= spec.get("min_s", 1.2) and qn_to_sec(e) - qn_to_sec(m) >= spec.get("min_s", 1.2):
                        cuts.append(m)
                for i, c in enumerate(cuts):
                    ce = cuts[i + 1] - gap if i + 1 < len(cuts) else e
                    srcn = max((n for n in ch if n["qn"] <= c + 1e-6), key=lambda n: n["qn"])
                    dst["notes"].append({"qn": round(c, 4), "dur": round(ce - c, 4), "pitch": pitch,
                                         "vel": ch[min(1, len(ch) - 1)]["vel"] if i else min(srcn["vel"], ch[min(1, len(ch) - 1)]["vel"] if srcn["vel"] >= 80 else 127), "sq": round(c, 4) if i else ch[0].get("sq", ch[0]["qn"])})
                    if i:
                        dst.setdefault("rebows", []).append([round(c, 4), round(e, 4), pitch, round(cuts[i - 1], 4), None])
                dst["doubles"].append([round(a, 3), round(b, 3), pitch, len(cuts)])
            dst["notes"].sort(key=lambda n: n["qn"])
            dst["rebows"] = sorted(dst.get("rebows", []))
            la, lb = a - 0.3, b + 0.5
            at_end = lb > END - 0.01   # a span that runs to the last release: nothing is switched back after it
            for key in ("cc11", "cc1", "cc15", "cc70"):
                sl = [(q_, v_) for q_, v_ in (src.get(key) or [])]
                dl = [(q_, v_) for q_, v_ in (dst.get(key) or [])]
                if not sl and not dl:
                    continue
                dflt_ = {"cc15": 0, "cc70": 0}.get(key, sl[0][1] if sl else 64)
                back = step(dl, lb, dflt_)
                new = [x for x in dl if x[0] < la - 1e-9] + [(round(la, 4), step(sl, la, dflt_))] + [x for x in sl if la < x[0] < lb] \
                      + ([] if at_end else [(round(lb, 4), back)] + [x for x in dl if x[0] > lb + 1e-9])
                out = []
                for q_, v_ in new:
                    if not out or v_ != out[-1][1]:
                        out.append((q_, v_))
                dst[key] = out
            for p in (src, dst):
                l7 = [(q_, v_) for q_, v_ in (p.get("cc7") or [])] or [(0.0, 127)]
                if la <= 0.0:   # a span at the start of the piece: the lane's first point moves in front of it
                    l7 = [(round(la - 0.5, 4), l7[0][1])] + [x for x in l7[1:]] if l7[0][0] <= 0.0 else l7
                if any(la - 0.01 < q_ < lb + 0.01 for q_, _ in l7):
                    raise SystemExit(f"TRACK_DOUBLES {p['name']}: a CC7 point lies inside {la:.2f}-{lb:.2f}")
                back7 = step(l7, lb, 127)
                p["cc7"] = sorted(l7 + [(round(la, 4), int(round((cc7d if p is dst else cc7v) * step(l7, la, 127) / 127.0)))] + ([] if at_end else [(round(lb, 4), back7)]))
            dst["ks"] = sorted([k_ for k_ in dst["ks"] if not a - 0.6 < k_["qn"] < lb] + [{"qn": round(sec_to_qn(qn_to_sec(a) - 0.25), 4), "pitch": kp, "art": kart}]
                               + ([] if at_end else [{"qn": round(lb, 4), "pitch": ks_lookup(dst["stem"], cur_art)[1], "art": cur_art}]), key=lambda k: k["qn"])
            dst["art_counts"][kart] = dst["art_counts"].get(kart, 0) + sum(1 for n in dst["notes"] if a - 1e-6 <= n["qn"] <= b)
        print(f"  doubles {dst_n} <- {spec['src']}: {dst['doubles']}", file=sys.stderr)


def apply_cc_shapes(parts):
    def interp(pts, x):
        if x <= pts[0][0]:
            return pts[0][1]
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if x0 <= x <= x1:
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y1
        return pts[-1][1]
    for p in parts:
        todo = []   # (cc, [(qn, d)], mode)
        for it in CC_SHAPES.get(p["name"], []):
            todo.append((it[0], [(float(q_), float(d_)) for q_, d_ in it[1]], it[2] if len(it) > 2 else "add"))
        for cc_, sq_, pts_ in CC_SHAPES_S.get(p["name"], []):
            n_ = min((n for n in p["notes"] if abs(n.get("sq", n["qn"]) - sq_) < 0.02), key=lambda n: n["qn"], default=None)
            if n_ is None:
                raise SystemExit(f"CC_SHAPES_S {p['name']} {sq_}: no note")
            t0_ = qn_to_sec(n_["qn"])
            todo.append((cc_, [(sec_to_qn(t0_ + x_), float(d_)) for x_, d_ in pts_], "add"))
        RL = REBOW_CC_LIFT
        nl_ = 0
        if RL and p["family"] in RL.get("families", ("string",)) and p["name"] not in RL.get("skip_tracks", ()) and p.get("rebows") and p.get("cc11"):
            for rb in p["rebows"]:
                q_ = rb[0]
                if any(abs(q_ - x_) < 0.02 for x_ in RL.get("skip", {}).get(p["name"], [])):
                    continue
                if RL.get("only") is not None and not any(abs(q_ - x_) < 0.02 for x_ in RL["only"].get(p["name"], [])):
                    continue
                if _step(p["cc11"], q_, 0) > RL["max_cc"]:
                    continue
                t0_ = qn_to_sec(q_)
                # mvt2 c57 (critic A #1c): "hold" seconds at the full lift before the return over "s" (the lowest level of a
                # Sus MAX bow change comes 0.1-0.6 s after it, so a lift that starts falling at the note-on is spent early)
                pts_ = [(sec_to_qn(t0_ - 0.005), 0.0), (q_, float(RL["cc"]))] + ([(sec_to_qn(t0_ + RL["hold"]), float(RL["cc"]))] if RL.get("hold") else []) \
                       + [(sec_to_qn(t0_ + RL.get("hold", 0) + RL["s"]), 0.0)]
                if RL.get("pre_fall"):
                    pts_ = [(sec_to_qn(t0_ - RL.get("pre_s", 0.15)), 0.0), (sec_to_qn(t0_ - 0.01), -float(RL["pre_fall"]))] + pts_
                todo.append((11, pts_, "add")); nl_ += 1
        SE_ = SOFT_ENTRY_CC
        ne_ = 0
        if SE_ and p["family"] in SE_.get("families", ("string",)) and p.get("cc11") and p.get("notes"):
            ksl_ = sorted((k_["qn"], k_["art"]) for k_ in p.get("ks", []))
            rbq_ = [rb[0] for rb in p.get("rebows", [])]
            ends_ = sorted((n["qn"] + n["dur"]) for n in p["notes"])
            for q_ in sorted({round(n["qn"], 4) for n in p["notes"]}):
                ln_ = max(n["dur"] for n in p["notes"] if abs(n["qn"] - q_) < 1e-3)
                prev_end_ = max([e_ for e_ in ends_ if e_ <= q_ + 0.02], default=None)
                row_ = p.get("first_art") or ""
                for kq_, a_ in ksl_:
                    if kq_ <= q_ + 1e-6:
                        row_ = a_
                if row_ not in SE_.get("rows", ("Leg Slur MAX", "Flautando")) or any(abs(q_ - x_) < 0.02 for x_ in rbq_):
                    continue
                if any(n["qn"] < q_ - 1e-3 and n["qn"] + n["dur"] > q_ + 0.02 for n in p["notes"]):
                    continue   # another note of the track is sounding
                if prev_end_ is not None and qn_to_sec(q_) - qn_to_sec(prev_end_) < SE_.get("gap_s", 0.25):
                    continue
                if qn_to_sec(q_ + ln_) - qn_to_sec(q_) < SE_.get("min_s", 0.6) or _step(p["cc11"], q_, 0) > SE_["max_cc"]:
                    continue
                t0_ = qn_to_sec(q_)
                # mvt2 c57 (critic A #2): with "hold" the lift stays up to the SCORE onset + hold seconds and returns over
                # "s" after that (a led note-on lies 120-300 ms before the beat, so a lift that fell from the note-on was
                # spent before the beat); without "hold" the c56 shape (falls from the moved note-on)
                if SE_.get("hold") is not None:
                    ts_ = qn_to_sec(max(n.get("sq", n["qn"]) for n in p["notes"] if abs(n["qn"] - q_) < 1e-3))
                    th_ = max(t0_, ts_) + SE_["hold"]
                    todo.append((11, [(sec_to_qn(t0_ - 0.005), 0.0), (q_, float(SE_["cc"])), (sec_to_qn(th_), float(SE_["cc"])), (sec_to_qn(th_ + SE_["s"]), 0.0)], "add")); ne_ += 1
                    continue
                todo.append((11, [(sec_to_qn(t0_ - 0.005), 0.0), (q_, float(SE_["cc"])), (sec_to_qn(t0_ + SE_["s"]), 0.0)], "add")); ne_ += 1
        if not todo:
            continue
        for cc_, pts_, mode_ in todo:
            key = {11: "cc11", 1: "cc1", 7: "cc7"}[cc_]
            lane = [(float(q_), v_) for q_, v_ in (p.get(key) or [])]
            if not lane:
                if cc_ != 7:
                    continue
                lane = [(0.0, 127)]
            a_, b_ = pts_[0][0], pts_[-1][0]
            qs = {q_ for q_, _ in lane} | {round(a_, 4), round(b_, 4)} | {round(x_, 4) for x_, _ in pts_}
            k = int(a_ / CC_GRID_QN) + 1
            while k * CC_GRID_QN < b_:
                qs.add(round(k * CC_GRID_QN, 4)); k += 1
            out, last = [], None
            for q in sorted(qs):
                v = _step(lane, q, lane[0][1])
                if a_ - 1e-9 <= q < b_ - 1e-9 or (mode_ == "set" and abs(q - b_) < 1e-9):
                    v = interp(pts_, q) if mode_ == "set" else v + interp(pts_, q)
                v = int(max(1, min(127, round(v))))
                if v != last or not out:
                    out.append((round(q, 4), v)); last = v
            p[key] = out
        p["cc_shapes"] = [len(todo), nl_, ne_]
        print(f"  cc shapes {p['name']}: {len(todo)} (re-bow lifts {nl_}, soft entries {ne_})", file=sys.stderr)


def apply_env_to_cc7(parts):
    """mvt2 c57 (critic B #1; finale technique 72): ENV_TO_CC7 {track: {"ref_db": R, "note_db": [[from, to, dB], ...],
    "keep_db": [[from, to, dB], ...]}}: the track's volume envelope (parts.json vol_db: roles, rows, roll settle / trims,
    hairpin halves) is folded into its CC7 lane, so the level of every note is carried by one control before the hall and
    the two halves cannot switch at different times. CC7 is linear amplitude inside Opus:
    CC7' = CC7 * 10 ** ((vol_db + note_db - keep_db - R) / 20); raise the track's mix.json gain_db by R (about the largest
    planned level, so the largest CC7' stays under 127). "note_db" rows are per-note levels (read at the note's score
    onset, one value for the whole note: what a one- to three-note section row used to hold). "keep_db" rows stay in the
    envelope as the only thing left there (a slow section balance that keeps CC7 in a usable range on ppp rolls); each
    edge must lie in a rest of the track. The level of a note is read from its moved note-on (the lane steps 0.02 qn
    before it, where the CC7 lane already steps), follows vol_db inside the note and is held through the rest after it, so
    no level changes on a ringing tail. For tracks whose mix.json adds no trims to the envelope (the timpani)."""
    for p in parts:
        spec = ENV_TO_CC7.get(p["name"])
        if not spec or not p.get("notes"):
            continue
        vol = [(float(q_), float(v_)) for q_, v_ in (p.get("vol_db") or [])]
        c7 = [(float(q_), int(v_)) for q_, v_ in (p.get("cc7") or [(0.0, 127)])]
        ref = float(spec.get("ref_db", 0.0))
        rows_at = lambda rows, q: sum(float(d_) for a_, b_, d_ in rows if a_ - 1e-6 <= q < b_ - 1e-6)
        runs = []
        for n in sorted(p["notes"], key=lambda n: n["qn"]):
            a_, b_ = n["qn"], n["qn"] + n["dur"]
            if runs and a_ <= runs[-1][1] + 0.03:
                runs[-1][1] = max(runs[-1][1], b_); runs[-1][2].append((a_, n.get("sq", a_)))
            else:
                runs.append([a_, b_, [(a_, n.get("sq", a_))]])
        for a_, b_, d_ in spec.get("keep_db", []):
            for e_ in (a_, b_):
                if any(r_[0] - 1.0 < e_ < r_[1] + 1.0 for r_ in runs):
                    raise SystemExit(f"ENV_TO_CC7 {p['name']}: keep_db edge {e_} is not in a rest")
        qs = set()
        for i_, (a_, b_, ons_) in enumerate(runs):
            nx_ = runs[i_ + 1][0] - 0.02 if i_ + 1 < len(runs) else None
            qs |= {round(max(0.0, o_ - 0.02), 4) for o_, _ in ons_}
            k = int(a_ / CC_GRID_QN) + 1
            while k * CC_GRID_QN < b_:
                qs.add(round(k * CC_GRID_QN, 4)); k += 1
            qs |= {round(q_, 4) for q_, _ in c7 if a_ - 0.02 <= q_ < (nx_ if nx_ is not None else 1e9)}
        out, last, peak, raw = [], None, 0.0, []
        for q in sorted(qs):
            i_ = max((k for k, r_ in enumerate(runs) if r_[0] - 0.02 <= q + 1e-9), default=0)
            a_, b_, ons_ = runs[i_]
            o_, sq_ = max([x_ for x_ in ons_ if x_[0] - 0.02 <= q + 1e-9], default=ons_[0])
            qv = min(max(q, o_ + CC_GRID_QN), b_ - 0.002)     # inside the run: vol_db as written; up to one grid step after the note-on: the note's start level; after the end: held
            lv = (_step(vol, qv, 0.0) if vol else 0.0) + rows_at(spec.get("note_db", []), sq_) - rows_at(spec.get("keep_db", []), sq_)
            cv = _step(c7, min(max(q, o_ - 0.0199), b_), c7[0][1])
            raw.append((q, cv * 10 ** ((lv - ref) / 20.0), (i_, o_)))
        # inside one note the lane is a 0.25 qn moving mean of the planned level (the old CC7 steps on 0.25 qn and the
        # envelope half of a roll hairpin on 0.125 qn alternated: a saw-tooth of 1-3 dB inside crescendo rolls)
        for j_, (q, amp, seg_) in enumerate(raw):
            near = [a2_ for q2_, a2_, s2_ in raw[max(0, j_ - 4):j_ + 5] if s2_ == seg_ and abs(q2_ - q) <= 0.125 + 1e-9 and q2_ >= seg_[1] + CC_GRID_QN - 1e-9]
            if q >= seg_[1] + CC_GRID_QN - 1e-9 and len(near) > 1:
                amp = 10 ** (sum(math.log10(max(1e-6, a2_)) for a2_ in near) / len(near))
            peak = max(peak, amp)
            v = int(max(1, min(127, round(amp))))
            if v != last:
                out.append((round(q, 4), v)); last = v
        if peak > 127.5:
            print(f"WARNING: ENV_TO_CC7 {p['name']}: planned CC7 {peak:.0f} over 127 (raise ref_db)", file=sys.stderr)
        p["env_to_cc7"] = {"ref_db": ref, "points": len(out), "max": max(v_ for _, v_ in out), "min": min(v_ for _, v_ in out), "vol_items": len(vol)}
        p["cc7"] = [list(x) for x in out]
        keep = [(e_, rows_at(spec.get("keep_db", []), e_)) for e_ in sorted({-0.25} | {float(x_) for r_ in spec.get("keep_db", []) for x_ in r_[:2] if x_ > -0.25})]
        p["vol_db"], p["vol_bp"] = [[q_, round(v_, 2)] for q_, v_ in keep], []
        if p.get("post_end_shapes"):
            p["post_end_shapes"] = []
        print(f"  env -> CC7 {p['name']}: {len(out)} points, CC7 {p['env_to_cc7']['min']}-{p['env_to_cc7']['max']}, ref {ref:+.1f} dB", file=sys.stderr)


find_unisons()
parts = [build_perc_track(*t) if t[3] == "perc" else build_track(*t) for t in TRACKS]
apply_phrase_shape(parts)   # mvt2 c45
apply_vol_tail_hold(parts)   # mvt2 c46
apply_track_doubles(parts)   # mvt2 c56
apply_cc_shapes(parts)   # mvt2 c56
apply_env_to_cc7(parts)   # mvt2 c57
json.dump({"tpb": TPB, "end_qn": END, "score_end": SE, "title": SCORE_TITLE, "preroll_qn": PREROLL_QN, "preroll_bpm": PREROLL_BPM, "tempo": tempo, "timesig": timesig, "tracks": parts}, open(OUT, "w"), indent=1)
for p in parts:
    print(f'{p["name"]:15s} notes={len(p["notes"]):4d} ks={len(p["ks"]):3d} cc11={len(p["cc11"]):4d} range={p["range"]} clash={p["ks_clash"]} {p["art_counts"]} leads={p["leads"]} notches={p["notches"]} uni_drop={p["unison_dropped"]} bloomv={p["bloomv"]} pitch_trim={p["pitch_trimmed"]} div_ent={p["div_entries"]} extra={p["extra_leads"]} bcsoft={p["bcsoft"]} hpgain={len(p["hpgain"])} hp_chain={p["hp_chained"]} bc_skip={p["bc_skipped"]} roles_chained={p["roles_chained"]} acc_db={p["accent_db"]}')
