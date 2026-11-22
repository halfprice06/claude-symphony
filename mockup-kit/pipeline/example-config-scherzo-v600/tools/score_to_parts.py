"""Turn the mockup build (mockup.midi + mockup-events.tsv) into per-track part data for REAPER.

Output: parts.json with the tempo map and, per track, notes / keyswitches / CC11 dynamics / CC1 vibrato / CC15 mutes /
CC7 (timpani) in quarter notes from the start of the piece, plus the Opus patch and its starting articulation.
Mix settings (track gain, seat, width, mics, reverb send) live in build/mix.json and are applied by build_reaper.py.

Usage: python score_to_parts.py <build-dir> <ks_maps.json> <out.json>
"""
import bisect, collections, json, re, sys
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
# scherzo c08 (critic A #5): BORROW_NOTES = {track: [(staff, from qn, to qn)]}: the track also plays another staff's notes
# with score onsets in the window (a row only another section's patch has, e.g. the 2nd Violins' Harmonics for a 1st
# Violins natural harmonic). The source track drops them with a TRACK_WINDOWS entry; give the borrowing track the source's
# marks and hairpins there with SHARED_DYN / SHARED_HP, and its row with ART_SPANS
BORROW_NOTES = {}

# c02: ff 104 -> 114 and fff 118 -> 124 (the patches' top dynamic layer runs to 127; f -> ff measured only +2.5 LU)
DYN = {"ppp": 22, "pp": 34, "p": 46, "mp": 58, "mf": 72, "f": 88, "ff": 114, "fff": 124, "sf": 100, "sfz": 100, "fp": 46, "sfp": 46}   # scherzo c00: "sfp" (an fp with an sf attack)
KS_LEAD = 0.06       # keyswitch lead in quarter notes when there is no rest before the note
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
LEG_VEL_STRONG = {"string": (124, 124), "brass": (124, 124)}   # c03: legato-target velocity (<0.9 s, longer); v120 was 25-80 ms faster than v105
# (scherzo c07, ported from mvt3 c07: a LEG_VEL_STRONG value may be a list of (dynamic-lane value at or below, velocity):
# legato velocity follows the dynamic, EW research batch 4)
# scherzo c07 (ported from mvt3 c07; EW research: legato overlaps 45-80 ms strings, 33-58 ms winds / brass): a floor in
# seconds for the overlap of a legato note into its (moved) target {family: s}; LEG_OVERLAP (qn) stays the minimum. The
# floor is at most LEG_OVERLAP_MAX_FRAC of the target's own length (scherzo: fast slurred eighths keep their pitch)
LEG_OVERLAP_MIN_S = {}
LEG_OVERLAP_MAX_FRAC = 0.5
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
# scherzo c02 (critic C #4): hold the roll trim at its crescendo-start value under a printed crescendo (see build_track)
# (the share of the trim's fall that is held: 1.0 holds it all, 0 is off); hairpin starts listed in the SKIP list keep the
# plain table (a pp < f roll that already grows)
TIMP_ROLL_TRIM_HOLD_CRESC = 0.0
TIMP_ROLL_TRIM_HOLD_SKIP = []
TIMP_DELAY_S = 0.06   # mvt1 c03 (critic C #3): see build_track (struck notes start this late; others reach -6 dB late)
# mvt1 c37 (critic A #4, MANUAL-GAPS #10): TIMP_RH_ALT = {"max_gap_s": s, "add": 24}: in a run of single strokes (the
# "Lng" row) on one pitch, each no more than max_gap_s after the previous stroke, every second stroke is sent at pitch +
# add, the right-hand samples of the Timpani Flt KS (RH Lng regions at MIDI 60-81 play the LH pitch 24 below; read from
# the .oib); each run starts on the left hand. Sent at the written pitch only, the same-pitch eighths alternated two
# takes (level steps +-1.4..3.2 dB, spectra correlating 0.985-0.999; c36). parts.json `timp_rh`. None = off
# scherzo c12 (critic A #1): optional "lh_vel_add": [(velocity at or below, steps added), ...] raises the left-hand
# strokes inside an alternating run by their velocity band (the LH regions play softer than the RH regions at soft
# velocities); parts.json `timp_lh_vel` lists (onset, old velocity, new velocity)
TIMP_RH_ALT = None
# scherzo c03 (critics B #2, C #4; manual p.124 "Felt Short": quickly muted short hits, "particularly useful when you
# know that each hit needs to be cut off within a beat or two"): TIMP_STAC_ROW = row name (e.g. "Timpani Flt Sht") for
# strokes with a printed staccato; every rule written for the "Lng" strokes (velocity floor, metric velocity and dB,
# stroke CC7, right-hand alternation) takes the "Sht" row too (same LH 36-57 / RH 60-81 layout, V1-V16). None = off
TIMP_STAC_ROW = None
# scherzo c04 (critics B #4, C #3; manual p.124 "realistic stops and dampening"): TIMP_DAMP_AT = [(from qn, to qn,
# CC7), ...] (score qn): the timpani's CC7 lane falls linearly (0.05 qn steps) from its value at `from` to `CC7` by `to`
# and holds there until the next timpani onset's own CC7 point, so the drum is damped *before* the Opus hall (the hall
# tail keeps ringing; a volume-envelope cut is undone by build_reaper's tail hold and would cut the hall). parts.json
# `timp_damp`. [] = off
TIMP_DAMP_AT = []
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
LEG_MIN_GAP_AT = {}   # scherzo c15: {track: [(from qn, to qn, seconds)]}, see the use
# scherzo c11 (critics A #1, C #1): track names whose legato lead cap (LEG_CAP_FRAC x the previous note's length) is
# measured from the previous note's moved onset instead of its score onset. A target after a slurred eighth was capped at
# 0.375 qn (0.085-0.1 s) while the eighth itself started a full lead early, so the eighth lasted 0.2-0.3 s and the note
# after it came 0.1-0.27 s late. LEG_MIN_GAP_S still keeps the two moved onsets apart. Empty: off.
# A dict {track: N} limits it to targets whose previous note is at most N qn long (None: any length): in runs of
# quarters the same change lets the full requested lead through (it was capped at 0.75 qn), which is wanted only on
# tracks whose capped joins measured late
LEG_CAP_FROM_MOVED = ()
# mvt1 c21 (critic A #4): cap of a listed run-target lead (leg_leads.json on a fast_leg / Slur Runs note), as a fraction of
# the previous note's length
FAST_LEG_LEAD_CAP = 0.75
# c11 (C #3): build/leg_leads.json {track: {score onset: s}}: per-onset legato lead offsets (may be negative); the total
# legato lead is clamped to LEG_LEAD_CLAMP
LEG_LEAD_CLAMP = (0.03, 0.35)
# scherzo c11 (finale c11, critic C #2; SHARED-TECHNIQUES item 20): True: a listed per-onset offset is added to the base
# lead plus the extras (art / velocity / pitch) before the clamp. False (default): the base plus the offset is clamped
# first and the extras are added after, so a negative offset near the base realises less than its value (-0.07 s on a
# 0.06 s base with a 0.09 s extra gave -0.03 s)
LEG_LEAD_CLAMP_TOTAL = False
# c15 (C #1): soft legato targets of the Flute 1 theme (CC11 at the target <= 50) crossed at a median +0.093 s against
# +0.03 at louder levels (the flute solo of bars 37-44 changed notes 0.1-0.23 s after the pizz./harp beats under it):
# {track: (CC11 at or below, extra s)}
LEG_SOFT_EXTRA_S = {"Flute 1": (50, 0.06)}
# scherzo c08 (c07 critic C #2.4): LEG_SOFT_EXTRA_SKIP = {track: [(from qn, to qn)]}: spans where LEG_SOFT_EXTRA_S does not
# apply (a soft doubling line that must keep the lead of the line it doubles)
LEG_SOFT_EXTRA_SKIP = {}
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
# scherzo c02 (critic C #5): velocity caps over spans {track: [(from qn, to qn, max velocity)]} (the harp's p espress.
# hairpins drove its velocity-mapped dynamic to v80-98, louder than the mp theme)
# scherzo c12 (critics A #2, C #5): a fourth value turns a row into a shift: (from qn, to qn, cap, floor) lowers every
# note of the span by (the span's highest velocity - cap), not below the floor. A three-value row clips as before.
# The shift keeps differences only when the span's velocities before the cap span less than cap - floor: on the
# scherzo's harp (hairpins and per-pitch offsets, 12-46 steps wide against 12-13) it put 45 of 53, 30 of 82 ... notes on
# the floor and lowered the usual note by 7-22 steps, so the scherzo kept its clip rows (vel_cap_shift / vel_cap_pre in
# parts.json show the outcome of a shift row). VEL_SET is applied after the caps; a VEL_SET key may be (qn, pitch).
VEL_CAP_SPANS = {}
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
# scherzo c10 (critic C #3): HP_DEC_HOLD_HELD: a lone decrescendo's dB gain whose arrival lies inside a still-sounding
# note (no later onset before that note ends) holds to the note's end instead of releasing 1 qn after the arrival
HP_DEC_HOLD_HELD = False
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
# scherzo c03 (critic C #6): ENTRY_LEAD_LOUD_ART_S = {family or track: {row: s}}: extra entry lead for entries whose
# CC11 is over 80 on that row (loud string entries on Leg Slur MAX's first-note layer arrived +80..+100 ms with the
# 0.06 s loud entry lead, the soft ones were on time). Empty = off
ENTRY_LEAD_LOUD_ART_S = {}
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
# scherzo c11 (critics A #3, C #4): {track: {score onset: (CC11 added, length qn)}}: a listed note starts with CC11 raised
# by the amount (held from its moved onset to the score onset, as the entry level is) and falls linearly to 0 over the
# length after the score onset. For a fresh stroke on a sustain row whose soft layer speaks late: Hollywood Strings Sus
# MAX strokes at CC11 60-74 after an sfp spoke 210-380 ms after the note-on, strokes at CC11 75 or more in 60-110 ms
# (c10 stems, previous pitch excluded), and a volume swell does not change that time. Default: none
ACCENT_CC_AT = {}
# scherzo c16 (critics A #2, C #4; finale c17 #1; Dan 2026-11-11: no per-note volume moves, so an accent's weight must
# come from the instrument). Hollywood Strings and Woodwinds sustain rows gain 0.3-0.5 dB per CC11 unit up to about 106
# and nothing above it, so an accent at a printed ff (CC11 114) had no room: 152 of 321 accents.
# CC11_REST_MAP {track or family: [(printed CC, played CC), ...]} (piecewise linear, start it at (0, 0)) lowers the
# resting CC11 of loud passages (the level it costs goes into the slow dynamic trims, mix.json dyn_trim_db / roles).
# ACCENT_CC {track or family: {"add": units below loud_cc, "add_loud": units at loud_cc or more (resting value),
# "loud_cc", "top": ceiling, "hold_s", "rel_s", optional "skip": [score onsets]}}: each printed accent raises CC11 by
# the amount (never past top) from 0.01 qn before its score onset (and from the moved note-on, through the entry
# pull), holds it hold_s (or to the note's end) and returns over rel_s. Default: none
# scherzo c17 (critic A #2; Dan 2026-11-11 "the accents are little bit over done now"): optional keys of an ACCENT_CC
# entry: "from_moved" (the hold counts from the later of the moved note-on and score onset - "pre_s", default 0.03 s),
# "skip_rows" (rows that get no bump), "scale_staves" [(n staves accented on the same onset, factor), ...],
# "add_at" {score onset: units}.
# scherzo c19 (critic A #3): optional "soft_cc" / "add_soft": where the resting CC11 is under soft_cc the bump is at most
# add_soft units (the strings gain 0.4-0.5 dB per unit at CC11 40-60 and almost nothing at 105: one size of bump read
# +5 dB on a soft accent and 0 on a loud one). "add_at" still wins
# scherzo c27 (critic A #1): optional "marc_lift" {"cc": units, "s": (start, full) seconds from the score onset, "rows":
# (row names), "max_cc": printed CC11}: an accent on a marcato-overlay row (the marcato samples over a sustain that is
# 16+ dB softer at low CC11) gets a CC11 rise after the spike, held to the next moved note-on less 0.02 qn
CC11_REST_MAP = {}
CC11_REST_SFP_ADD = 8
ACCENT_CC = {}
# scherzo c27 (critic C #3; finale technique 139): {track or family: {"rows": ("Leg",), "max_cc": 70, "rest_qn": 0.5,
# "add": 10, "pre_s": 0.06, "hold_s": 0.25, "gone_s": 0.45, "spans": [(q0, q1), ...] or None, "skip": [onsets]}}: a legato-row note after a
# rest of rest_qn or more at a printed CC11 of max_cc or less (a soft legato head: the first-note sample at low CC11
# reaches its level 150-330 ms after the beat, and more lead did not help) gets CC11 + add from pre_s before its moved
# note-on, held to hold_s after it, back by gone_s. Needs an ACCENT_CC entry for the track (built with it). Default: none
SOFT_LEG_HEAD_CC = {}
# scherzo c16 (critic A #2): {track or family: CC}: an accented note that is not inside a slur plays the plain sustain
# (GENTLE_ACCENT arts) when its printed level is this CC or more (default DYN["f"] - 4, the rule since mvt1 c00). An
# accented slur head under f played the legato row's slow first-note layer (Oboe 1 2.6-11.4 dB under its figure)
ACCENT_SUS_MIN_CC = {}
# scherzo c16 (critic A #5; finale c17 #3): {"brass": s, "wind": s, or a track name}: floor of the played gap (note-off
# to the next moved note-on) before a same-pitch repeat on a sustain or legato row; the earlier note ends early (never
# under half its length). Tongued repeats ran together under 60 ms and separated by 5-13 dB at 90 ms. Default: none
REP_GAP_FLOOR_S = {}
# scherzo c18 (critic A #4): {"min_s": s, "gap_s": s}: a same-pitch repeat between two held notes (both min_s or longer
# as played) takes gap_s instead of the REP_GAP_FLOOR_S floor (the floor is for short tongued repeats; held repeats
# dipped the wind-and-brass sum). Default None
REP_GAP_FLOOR_LONG_S = None
# scherzo c16 (critics A #1, C #1; Dan's note 8): {source track: [{"span": (q0, q1), "to": track, "rebow_at": [...],
# "cc11_add": n, "cc1": value or None, "lift": (CC units, rise_s, hold_s, fall_s) or None, "vel": n}]}: a held note of
# the source (score onset in the span) is also played by a second instance (another patch file, so another sample),
# which changes bow at its own points; while one track starts a new bow (a soft sustain needs 1-1.5 s to speak, a
# 9-13 dB hole on one track) the other holds, and "lift" raises the holding track's CC11 over the hole. The copy takes
# the source's CC11 over the span (plus cc11_add). Same-pitch overlap on one instance is not possible (the old
# note-off stops the new note, kit LEARNINGS). Default: none
HELD_DOUBLE = {}
# scherzo c16: {track: {score onset: row}}: the listed note plays this row (set after ROW_REMAP, before the legato and
# lead rules read the rows). For a note whose row a rule chose for another reason: the sf of the tutti sfp on the theme
# head's marcato row, a held note's first piece on a legato row while its re-bows play the sustain row. Default: none
ART_AT = {}
# scherzo c16 (critics B #3, C #5-6): {track: [(q0, q1, units at q0, units at q1), ...]}: CC11 offsets, linear across each
# span (a level a per-note fader fill used to carry, made before the hall: Oboe 1's sub. p octave with Flute 1 started
# at CC11 37 against the flute's 54). Default: none
CC11_ADD_SPANS = {}
# scherzo c17 (critic B, slope guard; ONE_TIME_c17 item 2): seconds, or None. A role row's edge was drawn against the
# score onset (0.5 qn before its start, 0.5 qn after its end) while a led note (a legato target, an entry) starts
# 0.05-0.3 s earlier, so the edge fell inside the sounding note (18 notes over 1.9 dB in c16). With a value, an edge
# on the score onset of a led note is drawn over this many seconds ending on the note's MOVED note-on (in the rest,
# or in the previous note's last moments). Default None: as before
ROLE_EDGE_MOVED = None
# scherzo c30 (critic A #1): ROLE_EDGE_MOVED skipped chained rows (one row ending where the next starts: a crossfade over
# [a - 0.1, a + 0.15] around the score onset), so a role change on a led stroke still landed inside it (Violins II at the
# summit: -5 -> +0.5 dB crossfading 1004.9-1005.15 under a stroke moved to 1004.592). Score onsets listed here draw the
# chained crossfade too over ROLE_EDGE_MOVED seconds ending on the led note's moved note-on. Default (): as before
ROLE_EDGE_MOVED_CHAINED_AT = ()
# scherzo c25 (critic B #4a): seconds, or None. A printed hairpin's dB ramp (hpgain, soft-hairpin env) started at the
# hairpin's score start while the note on that start, when led (a legato target, an entry), sounds 0.05-0.3 s earlier:
# the ramp's first move fell inside the sounding note (15 guard notes in c24). With a value, a hairpin ramp that starts
# on the score onset of a led note starts this many seconds before that note's moved onset. Default None: as before
HP_START_MOVED = None
# scherzo c25 (critic B #4d): qn, or None. A hairpin's dB gain was held to the next onset after its end and released
# over HP_REL from there, inside an arrival note still sounding (Flute 1 / cor anglais 156: 1.4-2 dB given back in the
# note's first 0.35 s). With a value, when a note sounds across the hold's end, the hold runs to that note's end (at most
# this many qn later) and the release falls after it. Default None: as before
HP_HOLD_TO_NOTE_END = None
# scherzo c17 (critic B #2): {track: {"by": {notes sounding together: CC11 units}, "spans": [(q0, q1), ...] or None}}:
# a chord of one string section ("non div." double and triple stops) plays two or three samples of the full section,
# about 1.5 dB per doubling too loud against a single line. The chord's CC11 (the played value, after CC11_REST_MAP)
# is lowered by the units from its (moved) note-on to its end. Replaces the per-note "level:chord" envelope rule.
# Default: none
CHORD_CC11 = {}
# scherzo c17 (critic B #3): {family or track: {"db_per_unit": 0.22, "cap_add": 10, "min_s": 0.25, "rel_s": 0.6,
# "drop_ends": [hairpin ends whose gain is dropped without a CC11 add]}}: a crescendo's dB gain (HP_GAIN_DB, the
# volume envelope) that would be released inside a note which still sounds min_s after the release starts is not
# written (the envelope guard can only hold it to the note's end: +3..+7 dB on held arrival notes for up to a
# second); the same dB go into CC11 instead: a rise across the hairpin, held to the old release point, back over
# rel_s (CC11 acts before the hall, so the return cuts no tail), never past the arrival's played CC11 + cap_add.
# Gains with a sostenuto share or an fff hold stay in the envelope, and so do arrivals whose played CC11 is
# "max_arrival_cc" or more (strings and woodwinds are flat above about 104: the gain would be lost). Default: none
# scherzo c18 (critics B #1-2, C #1): more keys, all optional:
#   "convert": False      the gain is never moved into CC11 (a track whose CC11 slope at its arrivals is under about
#                         0.15 dB per unit: the c17 conversions gave 0.045 dB per unit on the woodwinds, so 10 units
#                         brought 0.5 dB where the envelope gave 4)
#   "keep_rel_db_s": 2.8  a gain left in the envelope (not converted) is released at this rate or slower (its release
#                         over HP_REL qn was 13-30 dB/s); a release that starts inside a printed decrescendo runs to the
#                         decrescendo's end (a printed move)
#   "drop_always": [ends]  scherzo c20: gains of crescendos ending there are dropped whether chained or not
#   "drop_keep_chain": True  a dropped gain ("drop_ends") whose crescendo continues a chained one keeps the earlier gain
#                         (no rise of its own) instead of losing both: the earlier gain was released in 28 ms at the
#                         second hairpin's start (bassoons at 210 / 894: -9.8 dB through a printed f < ff)
#   "drop_only_chained": True  with drop_keep_chain: a gain at a "drop_ends" arrival that is not chained is kept (only
#                         the chained rise is removed)
#   "hold_until_mark_qn": N  scherzo c27 (critic B #1): with keep_rel_db_s, a kept gain holds from the arrival as a
#                         passage level until a printed decrescendo start or softer mark (released there), the first rest
#                         of 0.5 qn (released in it) or N qn (the slow release); at a louder mark it shrinks by that mark's
#                         CC11 rise x db_per_unit and holds on (no fall at a louder mark). Was: released at keep_rel_db_s
#                         from the arrival, a 1-5 dB fade inside the arrival note with nothing printed
#   "hold_rest_extra_qn": M  with hold_until_mark_qn: at the cap, a rest of 0.25 qn or more starting within M qn takes
#                         the release (default 0: the slow release from the cap)
#   "hold_rest_min_qn": R  scherzo c28 (critic B #1, #2): with hold_until_mark_qn, only a rest of R qn or more ends the
#                         hold early (default 0.5: the gap after a staccato quarter released a tutti arrival's gain)
#   "hold_to_dec_qn": D   scherzo c28 (critic B #1): with hold_until_mark_qn, a hold that reaches its cap with no printed
#                         change runs on to a printed decrescendo starting within D qn of the arrival (released across
#                         it) when no softer mark and no rest of hold_rest_min_qn come first (default off)
#   "keep_short_arrivals": True  scherzo c28 (critic B #2a): a gain whose arrival note is too short to convert (min_s)
#                         is held by the rules above too (default: the old HP_REL release, a sag of 3-6 dB)
HP_GAIN_TO_CC11 = {}
# scherzo c18 (critic C #1, finale technique 78): a crescendo gain cut by a subito mark (the gain ends at once at the
# mark) whose mark is an sfp keeps the gain through the sf: held to the mark + HP_SUBITO_SFP_DELAY_S seconds and
# released over HP_SUBITO_SFP_REL_S, with the CC11 fall to the p. Default None: cut at the mark, as before
HP_SUBITO_SFP_DELAY_S = None
# scherzo c18 (critic A #1): {track: {"table": {score onset: units}, "min_lead_s": 0.12, "from_s": 0.03, "fall_s": 0.03,
# "hold_s": -0.02, "ret_s": 0.10}}: a CC11 dip over a legato transition on a "Leg" row. The string legato joins swell
# 98-128 ms before the beat (the transition sample) and sag after it: +3.3..+3.7 dB median over the new note's body. CC11
# falls by the listed units from the moved note-on + from_s (over fall_s), is held to the score onset + hold_s and is
# back by the score onset + ret_s; no pre-fall. Only listed joins (a per-join table from a measurement of the excess),
# only joins whose lead is min_lead_s or more. Default: none
LEG_TRANS_CC = {}
HP_SUBITO_SFP_REL_S = 0.3
# scherzo c16 (critic C #2): {track: seconds}: a legato-row note that follows, without a rest, a note on another row
# (a sustain or short row) is a first note of the legato row: with the keyswitch well ahead (KS_MIN_LEAD_S) it crosses
# to its pitch 190-246 ms after its note-on (inside the row 169-234 ms, but those joins have fitted leads), while its
# lead was 74-170 ms: 23 of 40 such joins sounded over 60 ms late. The note starts this many seconds early (never
# less than its lead from the other rules), at most the previous note's slot less ROW_CHANGE_LEAD_GAP_S; the previous
# note keeps its end (it sounds on its own row under the new note). Default: none
ROW_CHANGE_LEAD_S = {}
ROW_CHANGE_LEAD_GAP_S = 0.02
# scherzo c20 (critic A #2): {track: seconds}: an accented note on a sustain or marcato row (not legato) whose previous
# note starts at most 1 qn before it on a short row ("Stac" / "Spic" in its name) starts this many seconds earlier than the other
# lead rules put it, at most as the ROW_CHANGE_LEAD_S cap allows. The woodwinds' accented half notes after their
# staccato eighths came in 3-6 dB under the eighths for 100-200 ms (a Sus attack needs longer to speak than a staccato).
# Default: none
ROW_CHANGE_ACC_ADD_S = {}
ROW_CHANGE_ACC_SKIP = []   # score onsets left alone (tutti chords, where the sections' leads must stay together)
# scherzo c23 (critic C #2): or a dict {track: [score onsets]} (the onsets left alone on that track only; "_all": every track)
# scherzo c21 (critic A #2a): {track: [row names]}: no ROW_CHANGE_ACC_ADD_S on an accent whose previous note is on one of
# these rows (Violins II's accents after "Stac RRx9" already read +3.2 dB). Default: none
ROW_CHANGE_ACC_SKIP_PREV = {}
# scherzo c17 (critic A #1): seconds. The cap of ROW_CHANGE_LEAD_S and LEAD_SET_AT used the previous note's score slot
# and ignored that the previous note itself starts early (an eighth led 235 ms left its successor 94 ms: eight joins
# of the second idea spoke 128-151 ms late). With a value the cap is measured from the previous note's moved note-on
# and leaves it this long alone. Default None: the c16 cap
PREV_MIN_SOUND_S = None
# scherzo c16: {track: {score onset: seconds}}: the lead of the listed note, set after every other lead rule (and after
# ROW_CHANGE_LEAD_S), at most the previous note's slot less ROW_CHANGE_LEAD_GAP_S. For a refit on a measured pass
# (cycles/c16/actor_scripts/refit16.py: lead + measured lateness), in either direction, without going through the
# rules' caps. When both notes are on a legato row the previous note's end moves with the new note-on (the overlap is
# kept). build/lead_set.json when present. Default: none
LEAD_SET_AT = {}
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
# scherzo c22 (critic C #3): an untargeted crescendo whose own staves print a louder dynamic more than 1 qn but at most
# HP_TARGET_LOOKAHEAD_QN qn after its stop (no other mark or hairpin start between) takes that dynamic as its target and
# reaches it at the hairpin's end (the flute's p < ... ff printed one beat after the hairpin stopped at mp, then stepped
# +46 CC11 units at the ff). Only when the gap to the mark is at most half the hairpin's length (a 0.5 qn basses' hairpin
# would otherwise reach ff 2.5 qn early). 0 = off. Printed in the build log (hp_lookahead_targeted)
HP_TARGET_LOOKAHEAD_QN = 0.0
hp_lookahead_targeted = []
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
# scherzo c03 (critic C #1): SHORT_SUS_TO_LONG_ANY = True applies SHORT_SUS_TO_LONG to any short slurred note, not only
# a slur's first one (the dotted quarter, slurred eighth, long note of a hemiola or a waltz tune at quarter 264: on Sus
# MAX the eighth left the long note a Sus-to-Leg transition with no legato lead, 31 of 45 such string notes arrived
# 0.1-0.26 s late, medians +92..+176 ms). False = slur heads only (mvt1 c01)
SHORT_SUS_TO_LONG_ANY = False
# mvt1 c03 (critic C #1): a string Sus MAX note of a fast slur (short_sus) that overlaps the next note on a legato row
# makes that note a legato target (lead, legato velocity); across a slur boundary the target plays Leg BC MAX
SHORT_SUS_JOIN = True
# mvt1 c03 (critic A #5, #6): articulation tests over listed spans {track: [{"from", "to" (score qn), "art", optional
# "mark": "staccato" (only notes carrying it), "vel_add" or "vel_by_cc" [(CC, vel), ...], "full_len"}]}
ART_SPANS = {}
# scherzo c02 (ONE_TIME, BRIEF item 7: REAPER over the 45 GB cap): ROW_REMAP {track: {row: row}} moves every note
# the rules put on a row to another row the track already loads, so the rarely played row is never loaded (a legato row
# of a KS Master holds 10-27 thousand sample regions; a brass Leg Slur MAX that only played two slur heads cost as much
# as a busy one). A legato row remapped to a Sus row plays the notes as tongued Sus notes; "Leg BC MAX" remapped to
# "Leg Slur MAX" keeps the join as a slur transition with VLA_BC_SOFT's bow-change notch (the BC_SOFT path)
ROW_REMAP = {}
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
# scherzo c14 (Movement II c53's JOIN_NOTCH_S, ported): {track: {score onset: (from s, to s, dB)}}: the notch is timed in
# seconds from the moved note-on of the note at that score onset, so it follows every lead change (a JOIN_NOTCH row in
# absolute qn stays behind when the lead moves: master bump 8.3 dB in Movement II). JOIN_NOTCH_RAMP_S ramps
JOIN_NOTCH_S = {}
# scherzo c15 (Dan, 2026-11-11: "volume peaks up and down every note ... unnatural"; critics A #1-#4, B #1). Every
# vol_parts item carries a tag "class:layer" (vol_add): class slow (roles, hairpin gains, rolls, fade), level (one value
# per note or run: pitch / row / note trims, park return, level rows, chord cut) or shape (moves inside a note: accents,
# fills, notches, dips). parts.json gets the three class lanes (`vol_cls`) next to their sum `vol_db`; build_reaper.py
# can leave the shape class out or cap it (ENV_SHAPE=off / cap3) for the layer test.
# ONE_LEVEL: None = off (the generic default). {"tags": [...], "max_qn": 0.55, "ramp_s": 0.03, "leg_center_s": 0.005,
# "gap_qn": 1.0, "tail_s": 0.25}: every note (chord) whose sounding length or slot is max_qn or less gets ONE value
# of the summed layers in "tags": the mean of the built lane at 20 / 40 / 60 % of the note, held from the join with
# the note before to the join with the note after. Notes closer than gap_qn form one chain; equal neighbours make no
# point. A join's ramp (ramp_s) ends at the next note's moved onset when the note before has ended, and is centred
# leg_center_s after the next note's SCORE onset when it still sounds (a step at the moved onset of a led legato
# target cut the old note's last 60 ms: join holes 6-10 dB, critic A #3). Layers not listed are written as built.
ONE_LEVEL = None
VOL_GRID_QN = 0.25
# scherzo c15 (critic B #3, A #5): TIMP_LOUD_VEL_ADD. The +TIMP_LOUD_ATTACK_DB envelope spike on every stroke printed f or
# louder (86 strokes, 52 % of the timpani's notes with over 3 dB inside the note) carried 3-4 dB of the timpani's tutti
# level after the hall. With TIMP_LOUD_VEL_ADD = (add, cap, dB the full add is worth) single strokes (Lng / Sht rows)
# at f or louder take the velocity instead (tied strokes half) and get no spike; a stroke whose velocity the cap
# clipped gets the missing share as one flat level over the stroke. Rolls keep the attack shape. None = off
TIMP_LOUD_VEL_ADD = None
# scherzo c16 (critic B #1): TIMP_SETTLE_SKIP [roll score onsets]: these rolls do not settle (a one-bar roll under a
# tutti summit is not a long roll); TIMP_CC1_AT {roll score onset: (CC1 at its start, CC1 at its end)}: the roll's CC1
# (the Rls row's eight dynamic layers) runs linearly between the two values instead of following TIMP_CC1_MAP (a
# printed mf < f roll on CC1 73 -> 88 did not grow: -40 dB at its start, -41 at its end)
TIMP_SETTLE_SKIP = []
TIMP_CC1_AT = {}
# ACCENT_SWELL_MAX_DB: cap of a gentle / fitted accent swell (None = no cap). Movement I c56: fitted accents over +3 dB
# were not needed
ACCENT_SWELL_MAX_DB = None
# TRIM_STEP_S: None = the old pitch-trim ramps (0.25 qn from the moved onset, release over [next moved onset - 0.05,
# + 0.03]). {"ramp_s": 0.04, "center_s": 0.01, "pre_s": (0.03, 0.01)}: a pitch trim or row trim is a flat level; where the
# note before still sounds at the note's moved onset the step is centred center_s after the SCORE onset (so two trimmed
# neighbours crossfade from one value to the other without passing 0), otherwise it stands before the moved onset
# (pre_s); it ends the same way at the next note. LEG_JOIN_TRIM_HOLD and PITCH_TRIM_MIRROR do not apply to these.
# "center_by" {track: s} replaces center_s per track (the clarinet's transition carries the old pitch about 40 ms longer:
# with the step 50 ms after the score onset its join holes equal those of the stem without any envelope).
# Note trims listed in NOTE_TRIM_RAMP_S with 0.05 s or less are placed the same way.
TRIM_STEP_S = None
# ROW_TRIM_HOLD_QN: a row-trimmed note followed within this many qn (score end to next score onset) by another note
# on a row with the same trim holds the trim through the gap (0 = the old behaviour: every detached note was its own
# segment, 0 dB between the notes of a staccato run)
ROW_TRIM_HOLD_QN = 0.0
PITCH_TRIM_IN_OPUS = []   # see where pitch_trims.json is loaded
# scherzo c15, Dan's decision (2026-11-11): "i want to nuke all the volume adjustments per note". VOL_CLASSES lists the
# classes that are written into vol_db (the track volume envelope); None = all three (the old behaviour). With
# ("slow",) the envelope carries roles, hairpin gains, roll shapes, held decrescendos and the final fade only; the
# level and shape lanes are still computed and written to parts.json `vol_cls` (the record of what is not played).
# VOL_KEEP_TAGS adds single layers back (analysis builds; STP_KEEP_TAGS="level:pitch_trim,..." does the same).
# LEVEL_ROW_SLOW_QN: a LEVEL_SHAPES row that holds ONE level for at least this many qn is a passage level (slow class,
# "slow:level_row"); a row with several levels or a shorter one is a per-note level (None = every row is per-note level).
# UNI_BOOST_AS_ROLE: the +dB of the kept note of a same-patch unison is written as one role span per run of boosted
# notes (gaps under 1 qn), not per note.
VOL_CLASSES = None
VOL_KEEP_TAGS = ()
LEVEL_ROW_SLOW_QN = None
UNI_BOOST_AS_ROLE = False
# scherzo c27 (critic B #4.1): with UNI_BOOST_AS_ROLE, the span rises before the run's first moved note-on (in the rest
# before it) and falls in the first rest of 0.25 qn or more after the run (it rose and fell inside held notes: Horn 3
# 950 -2.3 dB over its last 0.4 s). Default False: as before
UNI_BOOST_ROLE_IN_RESTS = False
# scherzo c30 (critic B #2): UNI_BOOST_AS_ROLE runs merge across gaps under this many qn (a breath inside one unison
# phrase split Horn 3's run at 348 into two spans whose edges fell inside notes). Default 1.0: as before
UNI_RUN_GAP_QN = 1.0
# scherzo c30 (critic B #2): with UNI_BOOST_AS_ROLE, adjacent runs merge even when their boosts differ (a three-player
# unison note inside a two-player phrase made its own span, and the two spans' edges overlapped and summed inside the
# notes: Horn 3 349.7-353.5 +4.8 dB); the merged span takes the boost its notes hold longest. Default False: as before
UNI_RUN_MERGE_VALUES = False
JOIN_NOTCH_RAMP_S = 0.01
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
PITCH_TRIM_MIRROR = set()   # c12: tracks whose positive pitch trims on legato targets start with the mirror ramp
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
# scherzo c20 (critic A #3, #6): {track: [(q0, q1, CC1)]}: CC1 at most this value over [q0, q1) (score qn; start q0
# before a led note's moved note-on), on any patch: the dynamic layer of a CC1-layered brass note (Horn 1's Sus MAX G sharps
# under a diminuendo read 10-15 dB brighter than the slurred note before them at CC1 65-69), or the vibrato crossfade of
# a woodwind note. Default: none
CC1_SET_SPANS = {}
# scherzo c23 (critic A #1): {track: [(q0, q1, CC1)]}: CC1 at least this value over [q0, q1) (score qn), after
# CC1_SET_SPANS. On the Hollywood Strings sustain rows CC1 crossfades Non Vib / Vib / Molto Vib, and the Molto Vib set is
# recorded louder (Movement I c32: CC1 42 -> 85-105 made a soft 1st Violins line 3-16 dB louder), while the short rows
# carry no CC1 processor: a floor raises a soft slurred pair without raising a staccato neighbour's tail, which a CC11
# lift (Opus's global volume) does. Default: none
CC1_FLOOR_SPANS = {}
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
# scherzo c13 (critic A #1): the same lead per track (SHORT_SUS_LEAD_BY {track: s}) and per score onset
# (SHORT_SUS_LEAD_AT {track: {onset: s}}); both empty = SHORT_SUS_LEAD_S everywhere
SHORT_SUS_LEAD_BY, SHORT_SUS_LEAD_AT = {}, {}
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
# scherzo c03 (critic A #3): WIND_REP_PORTATO_TENUTO = True: a tenuto note into a same-pitch tenuto of its own slur
# (portato repeats) takes the WIND_REP_PORTATO re-tongue (gap_s and CC11 fall) instead of the tenuto rule's 0.06 qn gap,
# which caught it first (at quarter 264 that gap is 14 ms: bass clarinet and bassoon portato dipped 0.4-0.9 dB while the
# first repeat of the same line, with no tenuto before it, dipped 5.3). False = the tenuto rule wins (old behaviour)
WIND_REP_PORTATO_TENUTO = False
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
# scherzo c00 (port): an "sfp" is read like an fp (FP_SPIKE's timing, then p) whose attack reaches this dynamic instead of
# FP_SPIKE[0]. The scherzo prints sfp (tutti, bar 301 under a crescendo); it was an unread dynamic before
SFP_SPIKE_DYN = "sf"
# scherzo c06 (critic C #1): an entry led early onto an fp / sfp starts at the spike's level (see final2); off by default
FP_SPIKE_FROM_ONSET = False
# scherzo c06 (critic C #4): {staff: qn}: a hairpin stays open across a rest of 2 qn or more when its stop or next dynamic
# follows within this many qn of its start and the staff plays after the rest (hairpins_and_marks); off by default
HP_KEEP_ACROSS_REST = {}
# scherzo c00 (port): HARM_ALL_PITCHES = True keeps every note at a harp harmonic's onset on the "harm" track. Movement
# II wrote each harmonic as written + sounding pitch (the track keeps the upper one); the scherzo writes the harmonics
# as chords whose MIDI already sounds an octave up (\transposition c'' in the score's \harmOct), so each note is a
# sounding pitch. False = movement II's rule
HARM_ALL_PITCHES = False
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
# scherzo c24 (critic B #1): None, or qn. The step to +db was full at score qn + 0.05 s, inside every led arrival note
# (2.5-4.5 dB steps in 22 tracks at the scherzo's summit), and fell again at qn + 0.5 while the note sounded. With a
# value: the step ends 5 ms before the track's moved note-on of its arrival note (in the rest, or in the last moments
# of the note before), the +db is held to the end of the arrival note and released over this many qn after it
ARRIVAL_WEIGHT_MOVED = None
# scherzo c25 (critic B #3): True gives the arrival weight only to tracks whose printed dynamic at the arrival is louder
# than at qn - pre_qn (a printed crescendo or a louder mark into it): at the summit the trumpets, printed f with no
# change, stepped +5.7 dB and played over the fff woodwinds. Default False: every track that starts a note there
ARRIVAL_WEIGHT_RISE_ONLY = False
# scherzo c25 (critic B #3): None, or qn: with ARRIVAL_WEIGHT_MOVED the held +db ends at most this many qn after the
# arrival (a 9 qn trombone note carried it to bar 338). Default None: to the arrival note's end
ARRIVAL_WEIGHT_HOLD_CAP = None
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
# scherzo c09 (critic A #1): {track: [score qn]}: listed slurred, monophonic, non-first short notes stay on Leg Slur MAX
# as legato targets whatever their length and whether or not the track is in SHORT_SUS_LEG_TRACKS (a tail of two eighths
# after an accented half note at quarter 264, 0.114 s each, did not speak as Sus MAX re-attacks at p)
SHORT_SUS_LEG_AT = {}
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
# scherzo c03 (critic A #5): ROW_TRIM_WINDS = True lets ROW_TRIM_DB act on wind tracks too, with no Leg-row-neighbour
# test (a woodwind "Stac DblTng RRx9" row plays louder than the track's Sus / Leg rows and barely follows velocity,
# scherzo c02: 12 velocity steps moved Oboe 1 by 0.3-0.5 dB; level is the only handle). False = strings only
ROW_TRIM_WINDS = False
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
# scherzo c11: {track: {target score onset: s}}: a held trim's plateau lasts to s seconds before the listed target's score
# onset when that is later than the hold above. With a long lead the target's note-on comes before the trimmed note's own
# score onset, the plateau ended before it began and the trim reached about half its value (+5.5 dB realised +3.5)
LEG_JOIN_TRIM_HOLD_TO_AT = {}
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
# mvt1 c45: "globals": {NAME: value}: module-level settings replaced during the alias's build only (e.g. a tuple of track
# names such as SHORT_SUS_LEG_TRACKS, which "set" cannot reach), restored afterwards
ALIAS_TRACKS = {}
PASS2_TRACKS = ()
# mvt1 c41: TEST_TRACKS: names of (usually PASS2_TRACKS alias) tracks rendered only to be compared with another
# track (an A/B of a patch or script setting); parts.json "test": true. render_cycle.py --pass2 writes their stems to
# cycles/cNN/test_stems/ and leaves them out of render/ and of the master sum; the tempo arcs' lead line ignores them
TEST_TRACKS = ()
# scherzo c07 (ported from mvt3 c07) (critics C #1-#2 and A #2 of cycles/c06; EW research batches 2-4: a CC swell after the phrase start, an arch,
# a taper over the last second). PHRASE_SHAPE = None (off) or {"families", "min_s" (phrase length), "gap_s" (a played gap
# that ends a phrase), "start" (offset at the first onset), "rise" [(s after the onset, offset)], "peak" (offset, share of
# the phrase, kept in [0.33, 0.62]), "pre_end" (s before the last note-off, offset), "end" (offset at the note-off),
# "scale" {dynamic: factor} (by the printed level at each point), "floor" (lowest CC), "cap" {family: highest CC},
# "hp_fade_s" (the shape fades out this long before a printed hairpin / fp / sfp and back after it), "step_s" (point
# spacing)}, in dynamic-lane units (CC11, or CC1 on CC1_DYN_TRACKS), added to the printed level. A phrase is a run of
# notes with played gaps under gap_s, broken at breath marks. No taper where the last note is an accent or a crescendo's
# arrival. Inside a shaped phrase the per-note "swell" / "swell_taper" / "taper" contours (and their SWELL_DB rows) are
# dropped. parts.json `phrase_shapes` [[start, end]]
# scherzo c10: optional "family_scale" {family: factor} multiplies every offset of that family (Movement I c51: winds
# needed x1.4 to rise about 1 dB); absent = 1.0
# scherzo c11 (critic B #1): optional "family_scale_skip_cc1" (default False): True leaves family_scale off the
# CC1_DYN_TRACKS, where the offsets move the dynamic-layer lane (CC1) and a scale changes the level by whole layers
# (the clarinets rose 2.6-4.5 dB under the winds' x1.4)
PHRASE_SHAPE = None
# scherzo c07 (ported from mvt3 c07) (research batch 5 item 3): HP_CURVE = None (linear hairpins) or {"cresc": (share of the hairpin, share of
# the rise reached there), "decresc_last": share of the fall reached at the hairpin's last onset (the rest falls on that
# last held note), "min_qn": shortest hairpin shaped, "cresc_long": {"min_qn", "pt"} (scherzo c10: long crescendos
# take this point instead of "cresc"; off when absent)}
HP_CURVE = None
# scherzo c07 (research batch 7, Balfe sketches: short-note velocity by position in the beat): SHORT_BEAT_VEL = None (off)
# or {"families", "rows" (row-name prefixes), "beat1" (velocity added on the bar's downbeat), "beat" (on beats 2..),
# "off" (on an off-beat), "rand" (+- seeded random), "seed", "min_bpm" (only where the tempo is at least this),
# "meter_qn" (bar length in qn), "skip" {track: [(a, b)]}}. A same-pitch repeat never ends more than "pair_max" under the
# note before it (S1: the second of a repeated pair keeps its attack). parts.json `beat_vel` (count)
SHORT_BEAT_VEL = None
# mvt1 c51 (EW-TEMPLATE-PLAN section 6 "shorts with the CC parked high"; critic A c51 #2 with critic B c51 #2's level-safe
# form), ported in scherzo c08 (ONE_TIME_c08 item 4): SHORT_CC11_PARK = None or {"families", "rows" (row-name prefixes),
# "cc" (the parked CC11), "gg_amp" [(CC11, amplitude)] (the KS Master's Global Group CC11 table: on the HS short rows CC11
# acts only through it), "fade_s" (Opus's Controller 11 fadeTime, 120 ms in the HS KS Masters), "beat_db" {"beat", "and",
# "sixteenth"} with "beat_spans" {track: [(a, b)]} (metric weight in the volume envelope on the short-row notes of those
# spans; MEAS_TREM strokes never)}: over each run of short-row notes, from its first moved onset to the next other note's
# moved onset, CC11 holds "cc"; the volume envelope takes gg(CC11 the run would have had) - gg(cc) back, both slewed over
# fade_s, so every sounding voice keeps its level. Velocities stay in the zones they play now.
# scherzo c08: "beat_db" may also hold "downbeat" (the bar's first beat, with "meter_qn" the bar length in qn; other beats
# then take "beat"), for triple metre where the weight belongs to beat 1 against beats 2-3.
# parts.json `cc11_park` [[from qn, to qn]], `beat_db_notes` [[score onset, dB]]
SHORT_CC11_PARK = None
# scherzo c08 (critic A #3): STAC_LEN_SPANS = {track: [(from qn, to qn, frac)]}: printed staccatos with a score onset in
# the span end at frac of their written value (players on Sus slices, whose cut has no recorded release of its own).
# scherzo c10 (critic A #1): a 4-tuple (from, to, frac, min_written_qn) lengthens instead: printed staccatos written
# min_written_qn or longer end at least at frac of their value (never past the next onset - 0.02 qn); the woodwind
# "Stac DblTng" rows have no release trail, so a note-off inside the recorded decay cuts it (manual p.110)
STAC_LEN_SPANS = {}
STAC_LEN_NEXT_GAP_QN = 0.5   # scherzo c10: a lengthened staccato ends this far before the next score onset (room for its lead)
# scherzo c23 (critic A #2): {track: seconds}: a note on a short row ("Stac" / "Spic" in the row name) sounds at least this
# long from its moved note-on, but never past the track's next moved note-on less STAC_MIN_SOUND_GAP_S (applied at the
# output, after the leads). 1st Violins "Staccatissimo RRx9" peaks 81-98 ms after its note-on, so eighths written 57 ms
# long had their note-off before the peak and rang on the 524 ms release; with the note-off after the peak a release cap
# (mix.json sus_release_cap_ms any_dyn) can end the tail without cutting the peak (c21: the cap alone cut it). Default: none
STAC_MIN_SOUND_S = {}
# scherzo c26 (critic A #1): SLUR_END_BEFORE_STAC = {track: {"s": seconds, "spans": [(q0, q1), ...], "rows": ("Leg",),
# "min_qn": 0.15}}: a note on a listed row (substring) with its score onset in a span, followed within 0.1 qn of its end
# by a note of another pitch on a staccato row, ends s seconds before that note's moved note-on (applied to the output
# notes, after every lead and overlap rule; never shorter than min_qn). The slurred eighth before a staccato quarter
# rang over it in the woodwinds' tutti statements
SLUR_END_BEFORE_STAC = {}
STAC_MIN_SOUND_GAP_S = 0.02
# scherzo c07 (critic C #4; Opus 2025 manual p.92: Opus counts round robins per note, the reset CC restarts them):
# RR_RESET_AT = {track: [score qn, ...]}: parts.json lane "rr_reset", sent by build_reaper.py on Opus's round-robin reset
# CC 0.03 qn before the earliest (moved) note at each listed onset, so a printed group always plays the same samples
RR_RESET_AT = {}
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
# scherzo c12 (lost horn attacks of the c11 render): LEG_HEAD_MIN_GAP_S (by_name: track keys, then family; seconds). The
# first note on a legato row whose note before is on another row and ends less than this before it: the note before ends
# earlier, so that this much lies between its note-off and the new note-on (never more than a third of its length).
# The default note gap is in quarter notes (0.03 qn is 7 ms at quarter 264): a slur's first note 7-14 ms after a
# note-off was played as a legato-reached note in one render of two (the sustain's slow attack with no tongued
# front, a 9-26 dB hole of 0.5 s) on data that rendered with normal attacks the cycle before. parts.json
# `leg_head_gaps` lists [onset, gap before in ms, gap after in ms]. {} = off
LEG_HEAD_MIN_GAP_S = {}
# scherzo c13 (critic A #2): LEG_HEAD_AFTER_ROW_LEAD_S. A legato-row note that is not a legato target (the note before
# it is on a Sus or short row and ends at its onset) is neither an entry (no rest) nor a join, so no rule led it: it
# started on the beat with the row's slow first-note attack and sounded 30-186 ms late (62 notes of the scherzo's c12
# render: strings median +102 ms, winds +55 ms). {family or track: seconds, "at": {track: {score onset: seconds}},
# "skip": {track: [onsets]}, "gap_s": seconds between the note before and the moved onset (so the legato script cannot
# take the note as joined; a number or {family: seconds}; never under 0.01 qn), "cap_frac": largest share of the
# previous note's written length}. Only notes no other rule
# moved; the head of a run span (STACLEG_SPANS / FAST_LEG) only when listed in "at". parts.json `leg_head_row_leads` lists [onset, lead in qn]. {} = off
LEG_HEAD_AFTER_ROW_LEAD_S = {}
# scherzo c13 (critic A #6): KS_MIN_LEAD_S (by_name: track keys, then family; seconds). A keyswitch sits 0.03 qn before
# its note, which is 6.8 ms at quarter 264, less than one 512-sample audio block (10.7 ms). With a value here it sits
# at least this many seconds before the note, but never before 0.01 qn after the track's previous note-on, and a
# keyswitch to a non-legato row is not moved into a sounding legato-row note (the keyswitch guard would cut that
# note). parts.json `ks_early` counts the moved keyswitches. {} = off
KS_MIN_LEAD_S = {}
# scherzo c12 (state guard test): END_LEG_KS = {track: qn after the score's end}. A track whose last keyswitch left
# its legato row gets that legato row's keyswitch once more, this many qn after the score's last release (no note
# follows it; build_reaper.py's item runs to end_qn + 6). Purpose: tracks that end a render in another row than their
# legato row were the ones whose saved Opus state held the legato sustain groups at the 20 ms attack. parts.json
# `end_leg_ks` holds the added row. {} = off
END_LEG_KS = {}
RETONGUE_LEAD_CAP = 0.3
# scherzo c19 (critic C #4): RETONGUE_LEAD_CAP_AT {track: {score onset: share}} replaces the cap for listed notes (Horn 3
# 510 / 519 asked 0.12 s and got 0.3 x a 1 qn note, 79 ms at quarter 228). {} = off
RETONGUE_LEAD_CAP_AT = {}
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
# scherzo c11 (critic A #2): {track: {score onset: seconds}}: the re-tongue lead of a listed note (replaces the track's
# RETONGUE_LEAD_S value there; the notes ending at the gap still end as much earlier). An entry_leads.json extra does
# not reach these notes: a listed extra takes a note out of the re-tongue rule, and the entry rule needs a rest of
# 0.2 qn. Default: none
RETONGUE_LEAD_AT = {}
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
# scherzo c14 (critic A #3; the finale's ROW_LEAD_KEEP_END, technique 49): REATTACK_KEEP_END = {track: [score qn]}: a
# listed REATTACK_LEAD_AT note does not shorten the note before it when that note has another pitch (the stroke overlaps
# the end of a short Sus / staccato pickup instead of costing it its lead: a 0.06 s lead after a 0.114 s eighth)
REATTACK_KEEP_END = {}
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
# mvt1 c45: it also takes the string re-tongue lead (RETONGUE_LEAD_S, or "sus_lead_s" seconds on tracks with none),
# the note before giving way so the gap is kept (c44 without a lead: perceived attack +94 ms median over 23 repeats).
# parts.json `rep_strokes` [[score onset, class]], `rep_rebows` [score onset], `rep_sus_gaps`. None = off (the c05-c43 merge)
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
SUL_DEFAULT_CC70 = 127   # scherzo c00: 127 (FP4, the patches' own default; mvt1 c38-c41 and the kit say rest at 127)
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
# scherzo c03 (critic C #5): PIZZ_LEAD_S = {track: seconds} (exact track names): string notes on a row whose name starts
# "Pizz" start this early (the section pizz. rows rise over about 0.1 s: perceived +22..+50 ms against the basses' +7 and
# staccato bows' +1..+6 at quarter 264). STAC_LEAD_SPIC = True lets STAC_LEAD_S take rows starting "Spic" (Spiccato) too
PIZZ_LEAD_S = {}
STAC_LEAD_SPIC = False
STAC_LEAD_S = {}   # mvt1 c39: wind tracks too (the woodwind "Stac DblTng" rows; the row's notes otherwise keep the score onset)
# mvt1 c36 (critic A #2): STAC_ROW = {track: row}: the row a listed string track plays printed staccatos on (default the
# first of "Stac RRx14", "Stac RRx9", "Staccato RRx9" the patch has). The 1st Violins KS Master's row names are swapped
# against its samples: "Stac RRx14" holds the "V1 Staccatissimo" folder (StacSs files, 0.51 s for the f G5), and
# "Staccatissimo RRx9" holds "V1 Stac" (0.76 s), while the other sections' "Stac RRx9" rows play their "Stac" folders
STAC_ROW = {}
# scherzo c24 (critic A #1): {track: [(lowest pitch, highest pitch, row)]}: a printed staccato (not pizz., not a chord)
# whose pitch lies in a range plays that row, before ART_SPANS and STAC_ROW (Violins I's same-pitch eighth pairs blur on
# D5, D sharp 5 and F sharp 5 on every short row: 0.2-2.3 dB separation against 5.4-6.4 elsewhere). Default: none
STAC_ROW_BY_PITCH = {}
# scherzo c28 (critic A #1): {track: True}: STAC_ROW_BY_PITCH takes a note only when it is half of a same-pitch staccato
# pair (the previous or the next note of the part has the same pitch, is a printed staccato too, and the two score
# onsets are 0.5 qn or less apart); single staccatos fall through to ART_SPANS / STAC_ROW as before (the Spiccato
# reroute is for the bounced re-attack of a pair, manual p.93; on single notes it put the slur-end landing of bars
# 110 / 310 under the slurred eighth before it). Default: none (every note in the pitch range)
STAC_ROW_BY_PITCH_REP_ONLY = {}
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
# scherzo c11 (critic C #6): in a non-increasing ramp span whose last printed step lasts at least this many qn, the ramp
# ends on that step's value instead of extrapolating its slope to the span end (a rit. to quarter 140 held for two bars
# reached 127 in its last bar). None: extrapolate (the behaviour before)
RAMP_LAST_STEP_HOLD_QN = None
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
# scherzo c15: PITCH_TRIM_IN_OPUS (config; tracks whose per-pitch corrections are written into the Opus state by
# build_reaper.py, mix.json "region_gain_db") get no pitch trims in the envelope; STP_NO_PITCH_TRIM="A,B" adds tracks for a test build
# (STP_PT_IN_ENV=1 keeps them in the envelope's level class: the simulation target of the c15 tests)
for _t in ([] if __import__("os").environ.get("STP_PT_IN_ENV") else list(PITCH_TRIM_IN_OPUS)) \
        + [x_ for x_ in __import__("os").environ.get("STP_NO_PITCH_TRIM", "").split(",") if x_]:
    PITCH_TRIMS.pop(_t, None)
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
# mvt1 c45 (critic B #1): a re-bow fill list holds its last value until the next list starts, but never into a later
# note: it ends at the end of the note its re-bow belongs to and reaches 0 dB this many seconds later (None: old rule)
REBOW_FILL_END_S = 0.12
REBOW_MOVES = json.load(open(f"{BUILD}/rebow_moves.json")) if __import__("os").path.exists(f"{BUILD}/rebow_moves.json") else {}
REBOW_MOVES = {k: v for k, v in REBOW_MOVES.items() if not k.startswith("_")}
LOOP_PROFILES = json.load(open(f"{BUILD}/loop_profiles.json")) if __import__("os").path.exists(f"{BUILD}/loop_profiles.json") else {}
LP_START_S, LP_STEP_S, LP_FADE_S, LP_END_S = 0.8, 0.04, 0.3, 0.3


# mvt1 c00: articulation names that some KS Masters spell differently (the Solo Trumpet KS Master has no "Sus MAX", only
# "Sus Non Vib MAX" and "Sus Vib MAX"); tried after the names asked for
KS_ALIASES = {"sus max": ("Sus Non Vib MAX", "Sus Vib MAX"), "sus accent max": ("Sus Accent MAX",)}
# scherzo c28 (critic C #2, MANUAL-GAPS #6): the timpani rules name the felt patch's rows; on "Timpani Hrd KS" (same five
# rows on the same keys, manual p.125-126) they take the hard-stick rows
KS_ALIASES.update({f"timpani flt {r_.lower()}": (f"Timpani Hrd {r_}",) for r_ in ("Lng", "Sht", "Flm", "Rls", "Crs")})


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
        if RAMP_LAST_STEP_HOLD_QN and len(inner) > 1 and e - inner[-1][0] >= RAMP_LAST_STEP_HOLD_QN - EPS \
                and all(inner[i_][1] >= inner[i_ + 1][1] for i_ in range(len(inner) - 1)):
            anchors.append((e, vb))   # scherzo c11 (C #6): the long last step keeps its printed value to the span end
        else:
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
        # scherzo c07 (critic C #5): the tempo in force at the span's end is written there, so a ramp whose end tempo
        # equals the last printed step (no new step at e) does not hold its own last 0.25 qn value afterwards (the trio
        # played at quarter 226.17 instead of 228)
        if not any(abs(q - e) < EPS for q, _ in out):
            out.append((round(e, 4), step_val(e)))
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


def lane_add_pl(lane, pts, top=None):
    """scherzo c17: a CC step lane [(qn, value), ...] plus a piecewise-linear offset pts [(qn, units), ...] (0 outside),
    resampled every 0.03 s inside pts; raised values never pass top (values already over it stay)"""
    a_, b_ = pts[0][0], pts[-1][0]
    if b_ - a_ < 1e-6 or not lane:
        return lane
    def at_(q_):
        v_ = lane[0][1]
        for c_ in lane:
            if c_[0] <= q_ + 1e-6:
                v_ = c_[1]
            else:
                break
        return v_
    n_ = max(2, int((qn_to_sec(b_) - qn_to_sec(a_)) / 0.03))
    qs_ = sorted({round(a_ + (b_ - a_) * k_ / n_, 4) for k_ in range(n_ + 1)} | {round(c_[0], 4) for c_ in lane if a_ <= c_[0] <= b_})
    new_ = []
    for q_ in qs_:
        v_ = at_(q_)
        w_ = v_ + value_at(pts, q_)
        if top is not None:
            w_ = min(w_, max(v_, top))
        new_.append((q_, int(round(max(1, min(127, w_))))))
    out_ = [tuple(c_) for c_ in lane if c_[0] < a_ - 1e-6] + new_ + [(round(b_ + 0.001, 4), at_(b_ + 0.001))] \
        + [tuple(c_) for c_ in lane if c_[0] > b_ + 0.001]
    res_, last_ = [], None
    for q_, v_ in out_:
        if v_ != last_:
            res_.append((q_, v_)); last_ = v_
    return res_


def lead_qn(q, s):
    return q - qn_before(q, s)


# ---------- events ----------
ev = collections.defaultdict(list)
ACC_STAVES = {}
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

        def close_by_rest(upto, typ_=None):
            nonlocal open_hp
            if open_hp:
                r = [x for x in rs if open_hp[0] + EPS < x < upto - EPS]
                if r:
                    # scherzo c06 (critic C #4): HP_KEEP_ACROSS_REST {staff: qn}: a hairpin whose printed stop or next
                    # dynamic comes within that many qn of its start, with notes of the staff after the rest, stays open
                    # across the rest (the trumpets' pp < f of bars 101-104 restarted at pp after the bar-102 rest)
                    keep_ = HP_KEEP_ACROSS_REST.get(s)
                    if keep_ and typ_ in ("stop", "dynamic") and upto - open_hp[0] <= keep_ + EPS \
                            and any(r[0] - EPS <= n_["qn"] < upto - EPS for n_ in notes[s]):
                        return
                    hps.append((open_hp[0], r[0], open_hp[1])); open_hp = None

        for q, typ, data in evs:
            close_by_rest(q, typ)
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


def base_points(staff_list, extra_marks=(), extra_hps=(), niente=False, curve=True):
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
                hi_, hold_, fall_ = FP_SPIKE
                if data == "sfp":   # scherzo c00: see SFP_SPIKE_DYN
                    hi_ = SFP_SPIKE_DYN
                pts += [(q, level), (q + 0.02, max(DYN[hi_], level)), (q + hold_, max(DYN[hi_], level)), (q + fall_, DYN["fp"])]
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
            if tgt is None and HP_TARGET_LOOKAHEAD_QN and hk == "cresc":   # scherzo c22 (see the default)
                la_ = next(((mq, d) for mq, d in marks if stop + 1.0 < mq <= stop + HP_TARGET_LOOKAHEAD_QN
                            and d in DYN and d not in ("sf", "sfz")), None)
                if la_ and DYN[la_[1]] > level and la_[0] - stop <= 0.5 * (stop - q) \
                        and not any(round(la_[0], 3) in SUBITO[s_] for s_ in staff_list) \
                        and not any(stop + EPS < mq < la_[0] - EPS for mq, d in marks) \
                        and not any(stop + EPS < a_ < la_[0] - EPS for a_, b_, k_ in hps):
                    tgt = DYN[la_[1]]
                    hp_lookahead_targeted.append((",".join(staff_list), round(q, 3), round(stop, 3), la_[1], round(la_[0], 3)))
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
                hold_after = (stop - 0.01, stop + 1.0)
            elif hk == "cresc" and abs(tgt - level) < EPS:
                start = level - 12   # c06 (C #3): "niente <" to the current level starts 12 CC lower
            tgt = max(10, min(124, tgt))
            q = next((v for k, v in sf_hp.items() if k - EPS <= q <= k + 0.25), q)
            pts += [(q, level), (q, max(10, start))]
            if HP_CURVE and curve and stop - q >= HP_CURVE.get("min_qn", 1.0) - EPS:   # scherzo c07: curve=False (HP_CURVE "skip_families", e.g. timpani rolls stay linear)
                # mvt3 c07 (research batch 5 item 3, Mulan / Howl Synchron hairpins): a crescendo rises early, then
                # settles into its target; a diminuendo holds and falls on its last held note
                st_ = max(10, start)
                if hk == "cresc" and HP_CURVE.get("cresc"):
                    fx_, fy_ = HP_CURVE["cresc"]
                    # scherzo c10 (critic B #1): HP_CURVE "cresc_long" {"min_qn", "pt": (share of the hairpin, share
                    # of the rise)}: a crescendo of min_qn or longer (poco a poco over bars) rises late instead, so a
                    # held chord under a theme does not reach its target bars early
                    cl_ = HP_CURVE.get("cresc_long")
                    if cl_ and stop - q >= cl_["min_qn"] - EPS:
                        fx_, fy_ = cl_["pt"]
                    # scherzo c26 (critic C #2): HP_CURVE "cresc_after_fp" {"pt": (share, share), "hold_qn": h}: a
                    # crescendo that starts on an fp / sfp mark holds the p for h qn after the mark, then rises on its own
                    # curve point (the sfp < of bar 301 lasted 1 qn and was 70 % done after 4 qn)
                    caf_ = HP_CURVE.get("cresc_after_fp")
                    q0c_ = q
                    if caf_ and any(abs(mq - q) < 0.05 and d in ("fp", "sfp") for mq, d in marks) \
                            and stop - q > caf_.get("hold_qn", 1.0) + 1.0:
                        q0c_ = q + caf_.get("hold_qn", 1.0)
                        pts.append((q0c_, st_))
                        fx_, fy_ = caf_["pt"]
                    pts.append((q0c_ + fx_ * (stop - q0c_), st_ + fy_ * (tgt - st_)))
                elif hk == "decresc" and HP_CURVE.get("decresc_last"):
                    lo_ = max([o_ for o_ in ons_all if q + 0.25 * (stop - q) <= o_ < stop - 0.25 - EPS], default=None)
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
def build_track(tname, staves, patch, family, pan):
    stem = patch.rsplit("/", 1)[1][:-4]
    ns = sorted([dict(n, staff=s) for s in staves for n in notes[s]], key=lambda n: (n["qn"], n["pitch"]))
    if tname in TRACK_WINDOWS:   # c10 (A #1)
        ns = [n for n in ns if tw_keep(tname, n["qn"])]
    for st_, a_, b_ in BORROW_NOTES.get(tname, []):   # scherzo c08 (critic A #5)
        ns = sorted(ns + [dict(n, staff=st_) for n in notes[st_] if a_ - EPS <= n["qn"] < b_ - EPS],
                    key=lambda n: (n["qn"], n["pitch"]))
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
        if not HARM_ALL_PITCHES:
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
    if not ACC_STAVES:   # scherzo c17: staves with a printed accent per onset (ACCENT_CC "scale_staves")
        for s_ in list(ev):
            for q_ in {round(q, 3) for q, k, v in ev[s_] if k == "script" and v[0] in ("accent", "marcato")}:
                ACC_STAVES[q_] = ACC_STAVES.get(q_, 0) + 1
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
                                  niente=family in ("wind", "brass", "string"),
                                  curve=family not in (HP_CURVE or {}).get("skip_families", ())) if ns else ([(0.0, DYN["p"])], [], [])
    base = lambda q: value_at(pts, q)

    has_bc = family == "string" and any(a["name"] == "Leg BC MAX" for a in ksmaps.get(stem, {}).get("articulations", []))
    tie_slurred = []

    def short_into_long(n):
        """mvt1 c01 (A #1, test): the first note of a slur, short, slurred into a long note (a pickup into its downbeat)
        stays on the legato row with its target. On Sus MAX the pickup sat a median 2.4-3.5 dB over the Leg Slur MAX
        target it led to (the two rows' sustains differ at one CC11), so the theme accented its upbeat."""
        if SHORT_SUS_TO_LONG is None or n["slur"] is None:
            return False
        if not SHORT_SUS_TO_LONG_ANY \
                and any(o is not n and o.get("slur", slur_of(o["qn"])) == n["slur"] and o["qn"] < n["qn"] - EPS for o in ns):
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
            n["art"] = None
            continue
        if family == "timp":
            n["art"] = ks_lookup(stem, "Timpani Flt Rls")[0] if q in trem_q else ks_lookup(stem, "Timpani Flt Lng")[0]
            if TIMP_STAC_ROW and q not in trem_q and q in stacc_q:
                # scherzo c03 (critics B #2, C #4): a printed staccato stroke plays the quickly muted short-hit row
                n["art"] = ks_lookup(stem, TIMP_STAC_ROW)[0]
            continue
        if n.get("grace") or n.get("grace_target"):   # c03: the run and its target on one legato articulation
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
            continue
        # scherzo c24 (critic A #1): STAC_ROW_BY_PITCH (see the default)
        spr_ = [r_[2] for r_ in STAC_ROW_BY_PITCH.get(tname, []) if r_[0] <= n["pitch"] <= r_[1]]
        if spr_ and STAC_ROW_BY_PITCH_REP_ONLY.get(tname):
            # scherzo c28 (critic A #1): only the halves of same-pitch staccato pairs (see the default)
            pv_ = max((o for o in ns if o["qn"] < q - EPS), key=lambda o: o["qn"], default=None)
            nx_ = min((o for o in ns if o["qn"] > q + EPS), key=lambda o: o["qn"], default=None)
            if not any(o is not None and o["pitch"] == n["pitch"] and o["qn"] in stacc_q and abs(o["qn"] - q) <= 0.5 + EPS
                       for o in (pv_, nx_)):
                spr_ = []
        if spr_ and family == "string" and q in stacc_q and q not in trem_q and not polyphonic(n) \
                and not text_state(q, ["pizz"], ["arco"]):
            n["art"] = ks_lookup(stem, spr_[0])[0]
            n["stac_pitch_row"] = True
            continue
        sp_ = next((x_ for x_ in ART_SPANS.get(tname, []) if x_["from"] - EPS <= q < x_["to"] - EPS
                    and (x_.get("mark") != "staccato" or q in stacc_q)
                    and (x_.get("mark") != "tenuto" or near(q, ten_q))), None)   # scherzo c28: a "tenuto" mark filter
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
                    and not (((tname in SHORT_SUS_LEG_TRACKS
                               and not any(abs(q - k_) < 0.02 for k_ in SHORT_SUS_LEG_SKIP.get(tname, []))
                               and qn_to_sec(n["end"], TEMPO_NC) - qn_to_sec(q, TEMPO_NC) >= SHORT_SUS_LEG_S[0] - EPS)
                              or any(abs(q - k_) < 0.02 for k_ in SHORT_SUS_LEG_AT.get(tname, [])))
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
        elif q in accent_q and base(q) >= ACCENT_SUS_MIN_CC.get(tname, ACCENT_SUS_MIN_CC.get(family, DYN["f"] - 4)) \
                and family in GENTLE_ACCENT:   # scherzo c16: ACCENT_SUS_MIN_CC
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
    row_remapped = []
    for n in ns:   # scherzo c02: ROW_REMAP (see the default)
        to_ = ROW_REMAP.get(tname, {}).get(n.get("art"))
        if to_ and not to_.startswith("Leg BC"):
            n["art"] = ks_lookup(stem, to_)[0]
            n["row_remap"] = True
            row_remapped.append(round(n["qn"], 3))
    art_at_used = []
    for n in ns:   # scherzo c16: ART_AT (see the default)
        to_ = next((v_ for k_, v_ in ART_AT.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), None)
        if to_ and n.get("art") != to_:
            n["art"] = ks_lookup(stem, to_)[0]
            art_at_used.append(round(n["qn"], 3))
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
            if ROW_REMAP.get(tname, {}).get("Leg BC MAX", "").startswith("Leg Slur"):
                o["bc_from"] = id(n)   # scherzo c02: ROW_REMAP, the BC_SOFT path (Leg Slur MAX, bow-change notch)
                vla_bc_notch.append((o["qn"], VLA_BC_SOFT["notch"]))
                row_remapped.append(round(o["qn"], 3))
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
    timp_chain_skip = []   # mvt1 c07 (B #4)
    timp_vel_strokes = []   # scherzo c15: [score onset, velocity, flat dB] (TIMP_LOUD_VEL_ADD)
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
        if n.get("detache_t"):
            n["end"] = e0 + 0.01   # c15 (A #5)
        elif same_pitch and family == "string" and o0.get("rep_stroke") and STR_REP_NEW_BOW:
            # mvt1 c44 (ONE_TIME #4, critics A #1-#2): the note before a STR_REP_NEW_BOW stroke ends min(gap_s, frac x
            # its length) before the stroke's score onset; portato repeats add a CC11 fall over its last fall_s
            R_ = dict(STR_REP_NEW_BOW, **(STR_REP_NEW_BOW.get("portato") or {})) if o0["rep_stroke"] == "portato" \
                else STR_REP_NEW_BOW
            n["end"] = e0 - min(e0 - qn_before(e0, R_["gap_s"]), R_["frac"] * dur)
            fc_ = R_.get("fall_cc_loud", R_.get("fall_cc", 0)) if base(o0["qn"]) > 90 else R_.get("fall_cc", 0)
            if fc_:
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], R_.get("fall_s", 0.04)))
                cc_falls.append((fa_, n["end"], fc_, max(0.01, e0 - n["end"])))
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
                and not (WIND_REP_PORTATO_TENUTO and WIND_REP_PORTATO and WIND_REP_RETONGUE and same_pitch
                         and family in ("wind", "brass") and n["slur"] is not None and o0.get("slur") == n["slur"]
                         and near(o0["qn"], ten_q) and not o0.get("sost") and not o0.get("sost_rep")
                         and not o0.get("portato_join")):
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
            o0["rep_sus_gap"] = True   # mvt1 c45 (critic A #1): it takes the string re-tongue lead (retongue_ok)
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
            # scherzo c18 (critic A #4, finale c19 #1, Movement I c60 #6): WIND_DETACH "overlap_s" / "overlap_min_s":
            # a pitch change between two notes of overlap_min_s seconds or more on the same sustain row (polyphonic)
            # does not leave a gap: the old note ends overlap_s after the new note's (moved) note-on (the output
            # stage; 50-90 ms gaps dipped the wind-and-brass sum 4.4 dB against 2.5 at 20 ms or less)
            # scherzo c19 (critic C #1): the row tested is the row the keyswitch plays (after REP_ROW): the clarinets'
            # "Leg Slur Rep" (REP_ROW over every note) is monophonic legato, and an overlap there slurred 34 tongued notes
            def _played_(m_):
                a_ = m_.get("art") or ""
                r_ = rep_row_of(m_) if (a_ and REP_ROW.get(tname)) else None
                if r_ and family in REP_ROW_REPEATS_ONLY:
                    r_ = None   # (pitch changes are not repeats: the brass repetition rows take repeats only)
                if r_ and (a_ in ("Sus MAX", "Sus Max", "Sus Non Vib", "Sus Non Vib MAX", "Sus Vib MAX")
                           or ("Slur" in r_ and _lg(a_))):
                    return r_
                return a_
            if wd_.get("overlap_s") is not None and len(nxt) == 1 and o0.get("art") == n.get("art") \
                    and not _lg(n.get("art") or "") and not _lg(_played_(n)) and not _lg(_played_(o0)) \
                    and not o0.get("grace") \
                    and qn_to_sec(e0) - qn_to_sec(n["qn"]) >= wd_.get("overlap_min_s", 0.4) - 1e-6 \
                    and qn_to_sec(orig_end[id(o0)]) - qn_to_sec(o0["qn"]) >= wd_.get("overlap_min_s", 0.4) - 1e-6:
                n["wd_overlap"] = (o0, wd_["overlap_s"])   # (the gap stays for the lead rules; the output stage moves the end)
            if wd_.get("fall_cc") and dur <= WIND_DETACH_FALL_MAX_QN + EPS:
                # mvt1 c14 (critic A #3): a gap alone does not separate brass eighths (0.06-0.075 s holed -3.1 dB, as
                # slurred): a CC11 fall over the note's last fall_s, back at the next onset
                fa_ = max(n["qn"] + 0.25 * dur, qn_before(n["end"], wd_.get("fall_s", 0.10)))
                cc_falls.append((fa_, n["end"], wd_["fall_cc"], max(0.01, e0 - n["end"])))
        elif family == "string" and not is_leg and nxt and _lg(nxt[0].get("art") or "") and same_slur(n, nxt[0]) \
                and any(abs(nxt[0]["qn"] - k_) < 0.02 for k_ in SHORT_SUS_LEG_AT.get(tname, [])):
            # scherzo c09 (A #1): a SHORT_SUS_LEG_AT target after a slur head on a Sus / Marc row is joined as a legato
            # target (overlap, leg_target, legato lead), not started as a legato first note
            n["end"] = e0 + LEG_OVERLAP
            nxt[0]["leg_target"] = True
            nxt[0]["leg_prev"] = n
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
    # scherzo c08 (critic A #3): STAC_LEN_SPANS (see the default)
    for sp_ in STAC_LEN_SPANS.get(tname, []):
        a_, b_, fr_ = sp_[:3]
        minw_ = sp_[3] if len(sp_) > 3 else None   # scherzo c10 (critic A #1): 4-tuple lengthens (see the default)
        for n in ns:
            if a_ - EPS <= n["qn"] < b_ - EPS and any(abs(n["qn"] - q_) < EPS for q_ in stacc_q):
                w_ = orig_end[id(n)] - n["qn"]
                if minw_ is not None:   # the MIDI note is already the shortened staccato: read the written value
                    w_ = max([float(v_[1]) for s_ in staves for q_, k_, v_ in ev[s_] if k_ == "note" and len(v_) > 1
                              and abs(q_ - n["qn"]) < EPS], default=w_)
                if minw_ is None:
                    n["end"] = min(n["end"], n["qn"] + fr_ * w_)
                elif w_ >= minw_ - EPS:
                    nx_ = min([o["qn"] for o in ns if o["qn"] > n["qn"] + EPS], default=n["qn"] + 2 * w_)
                    n["end"] = max(n["end"], min(n["qn"] + fr_ * w_, nx_ - STAC_LEN_NEXT_GAP_QN))
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
                lvs_t_ = LEG_VEL_STRONG[family]
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
            if family == "harm":
                n["vel"] -= HARM_VEL_CUT
        if family == "timp" and n["art"].endswith(("Lng", "Sht")):   # strokes: below vel 53 the felt patch is near silent
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
        if TIMP_METRIC_VEL and family == "timp" and (n.get("art") or "").endswith(("Lng", "Sht")) and not is_acc_ \
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
        if TIMP_LOUD_VEL_ADD and family == "timp" and (n.get("art") or "").endswith(("Lng", "Sht")) \
                and base(n["qn"] + 0.01) >= DYN["f"]:   # scherzo c15 (see the default)
            want_ = TIMP_LOUD_VEL_ADD[0] * (0.5 if n.get("tie_stroke") else 1.0)
            v0_ = n["vel"]
            n["vel"] = int(round(max(v0_, min(TIMP_LOUD_VEL_ADD[1], v0_ + want_))))
            n["_tlv"] = (want_, n["vel"] - v0_)
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
    # scherzo c02 (critic C #5): VEL_CAP_SPANS. scherzo c12 (critics A #2, C #5): the caps run over whole spans and
    # before VEL_SET (a per-onset velocity inside a capped span is the final word). A row (from, to, cap) clips; a row
    # (from, to, cap, floor) shifts: every note of the span falls by (the span's highest velocity - cap) and stops at
    # the floor (a note already under the floor keeps its velocity), so the differences the earlier rules made
    # (per-pitch offsets, hairpin, beat weight) stay under the cap
    vel_cap_shift, vel_cap_pre = [], []
    for row_ in VEL_CAP_SPANS.get(tname, []):
        span_ = [n for n in ns if row_[0] - EPS <= n["qn"] < row_[1] - EPS]
        if not span_:
            continue
        if len(row_) > 3:
            vel_cap_pre.extend((round(n["qn"], 3), n["pitch"], n["vel"]) for n in span_)
            top_ = max(n["vel"] for n in span_)
            sh_ = max(0, top_ - row_[2])
            for n in span_:
                n["vel"] = min(n["vel"], max(row_[3], n["vel"] - sh_))
            vel_cap_shift.append((row_[0], row_[1], top_, sh_, min(n["vel"] for n in span_),
                                  max(n["vel"] for n in span_), len({n["vel"] for n in span_})))
        else:
            for n in span_:
                n["vel"] = min(n["vel"], row_[2])
    # scherzo c25 (critic A #1b): STAC_ROW_BY_PITCH rows may carry a 4th value vel_add (added to the velocity of the
    # notes the row takes over) and a 5th, vel_below (only notes under that velocity); before VEL_SET
    for n in ns:
        if n.get("stac_pitch_row"):
            for r_ in STAC_ROW_BY_PITCH.get(tname, []):
                if len(r_) > 3 and r_[0] <= n["pitch"] <= r_[1] and (len(r_) < 5 or n["vel"] < r_[4]):
                    n["vel"] = max(1, min(127, n["vel"] + r_[3]))
                    break
    for n in ns:
        # scherzo c12: a key (qn, pitch) sets one note of a chord (a harp tune's top voice); it wins over a plain qn key
        vs = next((v_ for k_, v_ in VEL_SET.get(tname, {}).items()
                   if isinstance(k_, tuple) and abs(n["qn"] - k_[0]) < 0.02 and n["pitch"] == k_[1]),
                  next((v_ for k_, v_ in VEL_SET.get(tname, {}).items()
                        if not isinstance(k_, tuple) and abs(n["qn"] - k_) < 0.02), None))
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
                ks.append({"qn": round(early_time(n["qn"]), 4), "pitch": key, "art": a, "note": n})
        else:
            ks.append({"qn": round(early_time(n["qn"]), 4), "pitch": key, "art": a, "note": n})
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
    # scherzo c16: CC11_REST_MAP and ACCENT_CC (see the defaults)
    rest_map_ = CC11_REST_MAP.get(tname, CC11_REST_MAP.get(family))
    sfp_q_ = [q_ for q_, d_ in marks if d_ == "sfp"]
    # the lead, row and velocity rules below read final() as it was before c16 (their thresholds were set on the printed
    # CC11): the map and the accent shapes are switched on when the CC11 lane is sampled
    cc16_on_ = [False]
    cc11_add_ = CC11_ADD_SPANS.get(tname, [])
    acc_cc_ = ACCENT_CC.get(tname, ACCENT_CC.get(family))
    chord_cc_ = []   # scherzo c17: CHORD_CC11 (see the default): (onset, end, units)
    cc_cfg_ = CHORD_CC11.get(tname)
    if cc_cfg_:
        for q_ in sorted({n["qn"] for n in ns}):
            grp_ = [n for n in ns if n["qn"] == q_ and not n.get("grace")]
            u_ = cc_cfg_["by"].get(min(len(grp_), max(cc_cfg_["by"])), 0) if len(grp_) >= 2 else 0
            if u_ and (cc_cfg_.get("spans") is None or any(a_ - EPS <= q_ < b_ for a_, b_ in cc_cfg_["spans"])):
                chord_cc_.append((q_, max(orig_end[id(n)] for n in grp_), u_))
        if chord_cc_:
            print(f"  {tname}: CHORD_CC11 on {len(chord_cc_)} chords", file=sys.stderr)
    acc_cc_shapes, acc_cc_done = [], set()
    acc_body_shapes = []   # scherzo c26: ACCENT_CC "body_cc"
    acc_lift_shapes = []   # scherzo c27: ACCENT_CC "marc_lift" and SOFT_LEG_HEAD_CC
    soft_leg_heads, marc_lifted = [], []

    def _acc_cc_build(shift_):
        """scherzo c16 / c17: the ACCENT_CC shapes; called once the leads (shift_) are known"""
        for n in ns:
            q_ = n["qn"]
            if q_ not in accent_q or q_ in acc_cc_done or any(abs(q_ - s_) < 0.02 for s_ in acc_cc_.get("skip", ())):
                continue
            acc_cc_done.add(q_)
            ml_ = acc_cc_.get("marc_lift")
            if ml_ and base(q_) <= ml_.get("max_cc", 127) \
                    and any((o.get("art") or "") in ml_.get("rows", ()) and o.get("vel", 0) <= ml_.get("vel_max", 127)
                            for o in ns if o["qn"] == q_):
                # scherzo c27 (critic A #1): "marc_lift" {"cc", "s": (start, full), "rows", "max_cc"}: on an accented
                # note on a marcato-overlay row at a printed CC11 of max_cc or less the marcato spike is followed by a hole (the sustain
                # layer sits 16+ dB under the marcato): CC11 rises cc units from score onset + s[0] to full at + s[1],
                # held to the next moved note-on less 0.02 qn, back at the resting value at that note-on
                e_ml_ = max(orig_end[id(o)] for o in ns if o["qn"] == q_)
                l0_ = sec_to_qn(qn_to_sec(q_) + ml_["s"][0])
                l1_ = sec_to_qn(qn_to_sec(q_) + ml_["s"][1])
                nx_ml_ = min([o["qn"] - shift_.get(id(o), 0.0) for o in ns if o["qn"] > q_ + EPS] + [e_ml_ + 0.02])
                if nx_ml_ - 0.02 > l1_ + 0.01:
                    acc_lift_shapes.append((l0_, l1_, nx_ml_ - 0.02, nx_ml_, ml_["cc"]))
                    marc_lifted.append(round(q_, 3))
            if any((o.get("art") or "") in acc_cc_.get("skip_rows", ()) for o in ns if o["qn"] == q_):
                continue   # c17 (critic A #2): a row with its own accent (the marcato sustain) gets no bump on top
            rb_ = value_at(rest_map_, base(q_)) if rest_map_ else base(q_)
            add_ = acc_cc_["add_loud"] if rb_ >= acc_cc_.get("loud_cc", 999) else acc_cc_["add"]
            if acc_cc_.get("soft_cc") is not None and rb_ < acc_cc_["soft_cc"]:
                add_ = min(add_, acc_cc_.get("add_soft", add_))   # scherzo c19 (critic A #3): a smaller bump at a low resting CC11
            add_ = next((v_ for k_, v_ in acc_cc_.get("add_at", {}).items() if abs(q_ - k_) < 0.02), add_)
            for k_, sc_ in sorted(acc_cc_.get("scale_staves", ()), reverse=True):   # c17: many staves accented together
                if ACC_STAVES.get(round(q_, 3), 0) >= k_:
                    add_ = add_ * sc_
                    break
            if add_ <= 0:
                continue
            e_ = max(orig_end[id(o)] for o in ns if o["qn"] == q_)
            t0_ = qn_to_sec(q_)
            if acc_cc_.get("from_moved"):
                # c17 (critic A #2): the hold is counted from the later of the moved note-on and (score onset - pre_s),
                # so a led note does not carry the bump for its lead plus the hold (Violins I 327: 0.55 s for a 0.45 s note)
                on_ = min(q_ - shift_.get(id(o), 0.0) for o in ns if o["qn"] == q_)
                t0_ = max(qn_to_sec(on_), t0_ - acc_cc_.get("pre_s", 0.03))
            h_ = max(q_ + 0.011, min(sec_to_qn(t0_ + acc_cc_["hold_s"]), e_))
            b0_ = q_ - 0.01
            on_m_ = min(q_ - shift_.get(id(o), 0.0) for o in ns if o["qn"] == q_)
            if acc_cc_.get("lead_s"):
                # scherzo c26 (critic A #2): the bump is up lead_s seconds before the moved note-on, so CC11 is already
                # raised when Opus picks the group at the note-on (it fades a CC11 change over about 120 ms)
                b0_ = min(b0_, sec_to_qn(qn_to_sec(on_m_) - acc_cc_["lead_s"]))
            acc_cc_shapes.append((b0_, h_, sec_to_qn(qn_to_sec(h_) + acc_cc_["rel_s"]), add_, acc_cc_["top"]))
            # scherzo c26 (critic A #2): "body_cc" (units, negative) / "body_s" (start, full; seconds from the moved
            # note-on) / "body_soft" (units where the resting CC11 is under soft_cc): a CC11 dip after the bump on accented
            # notes written body_min_s (0.42 s) or longer that are not legato targets, held to the next moved onset less
            # 0.02 qn (or the note's end) and back at the resting value there: the old envelope accent body, before the hall
            if acc_cc_.get("body_cc") and not any(o.get("leg_prev") for o in ns if o["qn"] == q_) \
                    and qn_to_sec(e_) - qn_to_sec(q_) >= acc_cc_.get("body_min_s", 0.42):
                bc_ = acc_cc_["body_cc"]
                if acc_cc_.get("body_soft") is not None and acc_cc_.get("soft_cc") is not None and rb_ < acc_cc_["soft_cc"]:
                    bc_ = acc_cc_["body_soft"]
                d0_ = sec_to_qn(qn_to_sec(on_m_) + acc_cc_.get("body_s", (0.22, 0.36))[0])
                d1_ = sec_to_qn(qn_to_sec(on_m_) + acc_cc_.get("body_s", (0.22, 0.36))[1])
                nx_ = min([o["qn"] - shift_.get(id(o), 0.0) for o in ns if o["qn"] > q_ + EPS] + [e_ + 0.02])
                e1_ = min(nx_, e_ + 0.02)
                e0_ = e1_ - 0.02
                if e0_ > d1_ + 0.01:
                    acc_body_shapes.append((d0_, d1_, e0_, e1_, bc_))
        # scherzo c27 (critic C #3; finale technique 139): SOFT_LEG_HEAD_CC (see the default)
        sl_ = SOFT_LEG_HEAD_CC.get(tname, SOFT_LEG_HEAD_CC.get(family))
        if sl_:
            done_ = set()
            for n in sorted(ns, key=lambda x_: x_["qn"]):
                q_ = n["qn"]
                if q_ in done_ or not any(r_ in (n.get("art") or "") for r_ in sl_.get("rows", ("Leg",))):
                    continue
                if sl_.get("spans") is not None and not any(a_ - EPS <= q_ < b_ for a_, b_ in sl_["spans"]):
                    continue
                if any(abs(q_ - x_) < 0.02 for x_ in sl_.get("skip", ())):
                    continue
                if any(o is not n and o["qn"] < q_ - EPS and orig_end[id(o)] > q_ - sl_.get("rest_qn", 0.5) + EPS for o in ns):
                    continue
                if base(q_) > sl_.get("max_cc", 70):
                    continue
                done_.add(q_)
                on_ = min(q_ - shift_.get(id(o), 0.0) for o in ns if o["qn"] == q_)
                t_ = qn_to_sec(on_)
                d0_ = sec_to_qn(t_ - sl_.get("pre_s", 0.06))
                wst_ = ([a_ for a_, _ in tw_spans(tname)[0]] if tname in TRACK_WINDOWS and tw_spans(tname)[1] else []) \
                    + ([a_ for a_, _ in TRACK_SPLITS[tname][1]] if tname in TRACK_SPLITS else [])
                if any(a_ - EPS <= q_ < a_ + 3.0 for a_ in wst_) and not any(o["qn"] < q_ - EPS and orig_end[id(o)] > q_ - 3.0 for o in ns):
                    # a window / split track's lane before its window's first note follows the source part's curve (the
                    # c27 first build wrote CC11 112-117 on the solo violin 10 ms before its 51): no lift on that note
                    done_.discard(q_)
                    continue
                e1_ = min(sec_to_qn(t_ + sl_.get("gone_s", 0.45)), max(orig_end[id(o)] for o in ns if o["qn"] == q_))
                e0_ = min(sec_to_qn(t_ + sl_.get("hold_s", 0.25)), e1_ - 0.01)
                if e0_ > d0_ + 0.03:
                    acc_lift_shapes.append((d0_, d0_ + 0.02, e0_, e1_, sl_.get("add", 10)))
                    soft_leg_heads.append(round(q_, 3))
            if soft_leg_heads:
                print(f"  {tname}: SOFT_LEG_HEAD_CC on {len(soft_leg_heads)} heads: {soft_leg_heads}", file=sys.stderr)
        if marc_lifted:
            print(f"  {tname}: ACCENT_CC marc_lift on {len(marc_lifted)} notes: {marc_lifted}", file=sys.stderr)
        return [x for b0, h1, r1, _, _ in acc_cc_shapes for x in (b0, h1, (h1 + r1) / 2, r1)] \
            + [x for d0, d1, e0, e1, _ in acc_body_shapes + acc_lift_shapes for x in (d0, (d0 + d1) / 2, d1, e0, e1)]
    for k_, (amt_, ln_) in ACCENT_CC_AT.get(tname, {}).items():   # scherzo c11: once per listed onset (chords too)
        if any(abs(n["qn"] - k_) < 0.02 for n in ns):
            bumps.append((next(n["qn"] for n in ns if abs(n["qn"] - k_) < 0.02), amt_, ln_))

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
    ps_kind_list = []    # scherzo c21
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
                         or (any(abs(cur_end - x_) < EPS for x_ in breath_q) and n["qn"] >= cur_end - 0.05)):
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
                # scherzo c21 (critic B #3): optional "build_end_s" (default None): a crescendo makes the phrase a build
                # only if its arrival lies within this many seconds of the phrase end (Bassoon 2's 12 s trio phrase,
                # a crescendo to p 2.5 s before its held notes, climbed 10 dB on them with no hairpin); optional
                # "build_rise_lyric" (default True): False skips the printed-rise test inside "lyric_spans"
                # optional "build_rule_spans" [(q0, q1)] (default None: everywhere): the two keys apply only to phrases
                # starting inside these spans
                in_lyr_ = any(la_ - EPS <= a_ < lb_ for la_, lb_ in PS_["types"].get("lyric_spans", []))
                in_rule_ = PS_["types"].get("build_rule_spans") is None or any(
                    ra_ - EPS <= a_ < rb_ for ra_, rb_ in PS_["types"]["build_rule_spans"])
                be_s_ = PS_["types"].get("build_end_s") if in_rule_ else None
                rise_ok_ = PS_["types"].get("build_rise_lyric", True) or not in_lyr_ or not in_rule_
                if (rise_ok_ and base(b_ - 0.05) - base(a_) >= PS_["types"]["build_cc"]) or any(
                        k_ == "cresc" and a_ + 0.75 * (b_ - a_) <= hb_ <= b_ + 0.1 and hb_ - ha_ >= 0.25 * (b_ - a_)
                        and (be_s_ is None or qn_to_sec(b_) - qn_to_sec(hb_) <= be_s_)
                        for ha_, hb_, k_ in hps):
                    kind_ = "build"
                elif "drive" in PS_["types"] and not any(la_ - EPS <= a_ < lb_ for la_, lb_ in PS_["types"].get("lyric_spans", [])) \
                        and bpm_at(a_) >= PS_["types"].get("drive_min_bpm", 0):
                    kind_ = "drive"   # batch 7: driving music starts high and falls, or peaks early
                elif "fanfare" in PS_["types"] and family == "brass" and (
                        g_[0]["qn"] in accent_q or sum(o["qn"] in accent_q for o in g_) * 2 >= len(g_)):
                    kind_ = "fanfare"
            ps_kinds[kind_] = ps_kinds.get(kind_, 0) + 1
            if kind_ == "build":
                # scherzo c24 (critic C #1): optional "build_start" (default: "start"), the build's entry offset
                tp_ = [(0.0, PS_["types"].get("build_start", PS_["start"])), (0.95 * L_, pk_off), (L_, pk_off)]
            elif kind_ == "drive":
                d0_, (dpk_, dat_), d1_ = PS_["types"]["drive"]   # (entry offset, (peak offset, share), end offset)
                tp_ = [(0.0, d0_), (dat_ * L_, dpk_), (L_, d1_ if not no_taper else dpk_)]
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
        # scherzo c21: each phrase's type (parts.json "ps_kinds"), so a type rule change can be diffed
        ps_kind_list[:] = [[round(a_, 3), round(b_, 3), kd_] for a_, b_, _p, kd_ in phrase_shapes]

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

    def phrase_off(q):
        for a_, b_, pts_, kd_ in phrase_shapes:
            if a_ - EPS <= q < b_:
                o_ = value_at(pts_, q)
                bq_ = base(q)
                sc_ = PS_["types"].get("fanfare_scale", 1.0) if kd_ == "fanfare" else ps_scale(bq_)
                if not (ps_cc1 and PS_.get("family_scale_skip_cc1")):   # scherzo c11 (B #1)
                    sc_ *= (PS_.get("family_scale") or {}).get(family, 1.0)   # scherzo c10 (Movement I c51 item 2)
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
        for a_, b_, u0_, u1_ in cc11_add_:   # scherzo c16: CC11_ADD_SPANS
            if a_ - EPS <= q < b_:
                v += u0_ + (u1_ - u0_) * (q - a_) / max(EPS, b_ - a_)
        if rest_map_ and cc16_on_[0]:   # scherzo c16: CC11_REST_MAP (see the default); an sfp's attack keeps its printed level plus
            # CC11_REST_SFP_ADD, so the sf stands over the lowered ff before it
            if FP_SPIKE and any(f_ - EPS <= q < f_ + FP_SPIKE[1] for f_ in sfp_q_):
                v = min(127.0, v + CC11_REST_SFP_ADD)
            else:
                v = value_at(rest_map_, v)
        if chord_cc_ and cc16_on_[0]:
            v -= max([u_ for a_, b_, u_ in chord_cc_ if a_ - EPS <= q < b_ - EPS], default=0)
        for b0, amt, ln in bumps:
            if b0 - EPS <= q < b0 + ln:
                v += amt * (1 - (q - b0) / ln)
        if acc_cc_shapes and cc16_on_[0]:   # scherzo c16: ACCENT_CC (see the default): the largest active shape, not the sum
            av_ = 0.0
            for b0, h1, r1, add_, top_ in acc_cc_shapes:
                if b0 - EPS <= q < r1:
                    w_ = 1.0 if q < h1 else max(0.0, (r1 - q) / max(1e-6, r1 - h1))
                    av_ = max(av_, w_ * max(0.0, min(add_, top_ - v)))
            v += av_
        if acc_body_shapes and cc16_on_[0]:   # scherzo c26: the deepest active accent body dip
            bv_ = 0.0
            for d0, d1, e0, e1, bc_ in acc_body_shapes:
                if d0 - EPS <= q < e1:
                    w_ = min(1.0, (q - d0) / max(1e-6, d1 - d0)) if q < d1 else (1.0 if q < e0 else max(0.0, (e1 - q) / max(1e-6, e1 - e0)))
                    bv_ = min(bv_, w_ * bc_)
            v += bv_
        if acc_lift_shapes and cc16_on_[0]:   # scherzo c27: the largest active marcato lift
            lv_ = 0.0
            for d0, d1, e0, e1, lc_ in acc_lift_shapes:
                if d0 - EPS <= q < e1:
                    w_ = min(1.0, (q - d0) / max(1e-6, d1 - d0)) if q < d1 else (1.0 if q < e0 else max(0.0, (e1 - q) / max(1e-6, e1 - e0)))
                    lv_ = max(lv_, w_ * lc_)
            v += min(lv_, max(0.0, 127.0 - v))
        for h0, h1, amt in holds:   # c08 (C #1): the tenuto bump (TENUTO_BUMP over 0.5 qn) never falls below amt
            if h0 - EPS <= q < h1:
                v += max(0.0, amt - TENUTO_BUMP * max(0.0, 1 - (q - h0) / 0.5))

        v += contour(q)
        if phrase_shapes and not ps_cc1:
            v += phrase_off(q)   # scherzo c07: PHRASE_SHAPE (CC1_DYN_TRACKS: in CC1)
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
        + [x for b0, h1, r1, _, _ in acc_cc_shapes for x in (b0, h1, (h1 + r1) / 2, r1)] \
        + [x for d0, d1, e0, e1, _ in acc_body_shapes for x in (d0, (d0 + d1) / 2, d1, e0, e1)] \
        + [x for a_, b_, _, _ in cc11_add_ for x in (a_, b_)] + [x for a_, b_, _ in chord_cc_ for x in (a_, b_)] \
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
    def by_name(tbl):
        for k_, v_ in tbl.items():
            if k_[0].isupper() and k_ in tname:
                return v_
        return tbl.get(family)
    shift = {}
    leg_s = by_name(LEG_LEAD_S) or 0.0
    ent_s = by_name(ENTRY_LEAD_S)
    ent_art = by_name(ENTRY_LEAD_ART_S) or {}   # mvt1 c03 (C #2)
    ent_loud = by_name(ENTRY_LEAD_LOUD_ART_S) or {}   # scherzo c03 (critic C #6)

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
            and not (family == "string" and AUTO_REBOW and not abut_.get("rebow_ok") and any(
                (o is n or (o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05))
                and qn_to_sec(orig_end[id(o)]) - qn_to_sec(o["qn"]) > REBOW_MAX_S for o in ns))

    def entry_outer(n):   # the generic entry branch's own condition (below)
        q = n["qn"]
        return not n.get("leg_target") and bool(n.get("art")) and "Accent" not in n["art"] \
            and any(w in n["art"] for w in ENTRY_LEAD_ROWS) and q > -EPS \
            and bool(ent_s or extra_s(q) or ent_art.get(n["art"])) and (q > 0.5 or family == "string" or extra_s(q))

    def poly0(n):   # mvt1 c19: polyphonic on the written lengths (the ends above already carry legato overlaps)
        return any(o is not n and o["qn"] < orig_end[id(n)] - EPS and orig_end[id(o)] > n["qn"] + EPS for o in ns)

    rt_slow_ = by_name(RETONGUE_LEAD_SLOW_S) if RETONGUE_LEAD_SLOW_S else None

    def rt_lead_s(q):   # mvt1 c37 (critic C #1.1): the re-tongue lead at this tempo (RETONGUE_LEAD_SLOW_S under 100 bpm)
        return rt_slow_ if gate_bpm(q) < ENTRY_MID_MIN_BPM - EPS else rt_s_

    def rt_for(n):
        """the re-tongue lead of this note in seconds (mvt1 c45: a STR_REP_NEW_BOW "sus_min_s" repeat falls back to
        STR_REP_NEW_BOW["sus_lead_s"] on tracks with no RETONGUE_LEAD_S value)"""
        r_ = rt_lead_s(n["qn"])
        if not r_ and n.get("rep_sus_gap"):
            r_ = (STR_REP_NEW_BOW or {}).get("sus_lead_s")
        return next((v_ for k_, v_ in RETONGUE_LEAD_AT.get(tname, {}).items() if abs(n["qn"] - k_) < 0.02), r_)   # scherzo c11

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
        elif ((STAC_LEAD_S.get(tname) and family in ("string", "wind", "brass")   # scherzo c04: brass staccato rows too
               and (n.get("art") or "").startswith(("Stac", "Spic") if STAC_LEAD_SPIC else "Stac"))
              or (PIZZ_LEAD_S.get(tname) and family == "string" and (n.get("art") or "").startswith("Pizz"))) \
                and not n.get("rep_stac") and not n.get("mt_alt") and q > 0.5:
            # mvt1 c23 (critic A #3): printed staccato strokes start STAC_LEAD_S early
            # scherzo c03 (critic C #5): pizzicato notes start PIZZ_LEAD_S early (same path)
            L = lead_qn(q, PIZZ_LEAD_S[tname] if (n.get("art") or "").startswith("Pizz") else STAC_LEAD_S[tname])
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
            # scherzo c13 (critic A #1): SHORT_SUS_LEAD_BY {track: s} and SHORT_SUS_LEAD_AT {track: {score onset: s}}
            shift[id(n)] = lead_qn(q, next((v_ for k_, v_ in SHORT_SUS_LEAD_AT.get(tname, {}).items() if abs(q - k_) < 0.02),
                                           SHORT_SUS_LEAD_BY.get(tname, SHORT_SUS_LEAD_S)))
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
                if se_ and final(q) <= se_[0] and not any(a_ - EPS <= q < b_ - EPS for a_, b_ in LEG_SOFT_EXTRA_SKIP.get(tname, [])):
                    ex += se_[1]
                ve_ = by_name(LEG_VEL_EXTRA_S) if LEG_VEL_EXTRA_S else None   # mvt1 c37 (critic C #1.3)
                if ve_ and n["vel"] <= ve_[0]:
                    ex += ve_[1]
                    leg_vel_extra.append(round(q, 3))
                tot = ls_ + ex if lx is None else max(LEG_LEAD_CLAMP[0], min(LEG_LEAD_CLAMP[1],
                                                              (leg_s + lx if LEG_LEAD_CLAMP_TOTAL else ls_) + ex))
                # mvt1 c21: an entry (a, b, frac, "listed") applies only to onsets listed in build/leg_leads.json
                cf_ = next((x_[2] for x_ in LEG_CAP_FRAC.get(tname, []) if x_[0] - EPS <= n.get("sq", q) < x_[1]
                            and (len(x_) < 4 or x_[3] != "listed" or lx is not None)), 0.45)
                cm_ = tname in LEG_CAP_FROM_MOVED   # scherzo c11
                if cm_ and isinstance(LEG_CAP_FROM_MOVED, dict) and LEG_CAP_FROM_MOVED[tname] is not None:
                    cm_ = q - pv["qn"] <= LEG_CAP_FROM_MOVED[tname] + EPS
                pcap_ = pv["qn"] - (shift.get(id(pv), 0.0) if cm_ else 0.0)
                L = min(lead_qn(q, tot), cf_ * (q - pcap_))
                mg_ = next((x_[2] for x_ in LEG_MIN_GAP_AT.get(tname, []) if x_[0] - EPS <= q < x_[1]), LEG_MIN_GAP_S.get(tname))
                if mg_:
                    # mvt1 c21 (critic A #3): with a raised cap the target may not start closer than this many seconds
                    # to the previous note's moved onset (the unled head of an arpeggio group keeps an audible start)
                    # scherzo c15: LEG_MIN_GAP_AT {track: [(from qn, to qn, s)]} replaces the track's value in a span
                    pq_ = pv["qn"] - shift.get(id(pv), 0.0)
                    L = max(0.0, min(L, q - pq_ - mg_ * bpm_at(q) / 60.0))
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
        elif (SLUR_START_SUS or PICKUP_SUS or PORTATO_TAIL_JOIN) and not n.get("leg_target") and _lg((n.get("art") or "")) \
                and not n.get("subito_fresh") and any((o.get("slur_start_sus") or o.get("portato_tail")) and o["qn"] < q - EPS
                        and abs(orig_end[id(o)] - q) < 0.05 for o in ns):
            # mvt1 c15 (critic A #2): the second note of a slur whose first note was tongued on Sus is joined by the KS
            # Master like the sostenuto join: SOST_JOIN_LEAD_S early (at most 0.45 of the first note), SOST_VEL
            # mvt1 c34 (critic A #2): also the note after a re-tongued portato tenuto (PORTATO_TAIL_JOIN)
            p_ = next(o for o in ns if (o.get("slur_start_sus") or o.get("portato_tail")) and o["qn"] < q - EPS
                      and abs(orig_end[id(o)] - q) < 0.05)
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
            cap_ = next((v_ for k_, v_ in RETONGUE_LEAD_CAP_AT.get(tname, {}).items() if abs(q - k_) < 0.02), RETONGUE_LEAD_CAP)
            L = min(lead_qn(q, rt_for(n) + rx_), cap_ * (orig_end[id(p_)] - p_["qn"]))   # mvt1 c19: + art extra
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
                     + ent_art.get(n["art"], 0.0)   # mvt1 c03 (C #2): the articulation's extra
                     + (ent_loud.get(n["art"], 0.0) if final(q) > 80 else 0.0))   # scherzo c03 (C #6)
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
    # scherzo c13 (critic A #2): LEG_HEAD_AFTER_ROW_LEAD_S (see the default)
    leg_head_row_leads = []
    if LEG_HEAD_AFTER_ROW_LEAD_S:
        lh_ = LEG_HEAD_AFTER_ROW_LEAD_S
        lh_s_ = by_name({k_: v_ for k_, v_ in lh_.items() if k_ not in ("at", "skip", "gap_s", "cap_frac")})
        lh_at_ = lh_.get("at", {}).get(tname, {})
        for n in sorted(ns, key=lambda n: n["qn"]):
            q = n["qn"]
            if shift.get(id(n), 0.0) > EPS or n.get("leg_target") or n.get("grace") or n.get("run") \
                    or (n.get("fast_leg") and not any(abs(q - float(k_)) < 0.02 for k_ in lh_at_)) \
                    or not _lg(n.get("art") or "") or q <= 0.5 \
                    or any(abs(q - x_) < 0.02 for x_ in lh_.get("skip", {}).get(tname, ())):
                continue
            pv_ = [o for o in ns if o is not n and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05]
            if not pv_ or any(_lg(o.get("art") or "") for o in pv_) \
                    or any(o is not n and o["qn"] < q - EPS and orig_end[id(o)] > q + 0.05 for o in ns):
                continue
            s_ = next((v_ for k_, v_ in lh_at_.items() if abs(q - float(k_)) < 0.02), lh_s_)
            if not s_:
                continue
            # the cap is a share of the previous note's written length (its own lead does not lengthen the cap: an
            # eighth pickup led 60 ms early would otherwise be cut to half of its played length)
            L = min(lead_qn(q, s_), lh_.get("cap_frac", 0.5) * (q - max(o["qn"] for o in pv_)))
            if L <= EPS:
                continue
            gs_ = lh_.get("gap_s", 0.0)
            gs_ = gs_.get(family, 0.0) if isinstance(gs_, dict) else gs_
            g_ = max(0.01, lead_qn(q, gs_)) if gs_ else 0.01
            shift[id(n)] = L
            pulls.append((q - L, q))
            leg_head_row_leads.append([round(q, 3), round(L, 4)])
            for o in pv_:
                e_old_ = o["end"]
                o["end"] = min(o["end"], max(o["qn"] - shift.get(id(o), 0.0) + 0.02, q - L - g_))
                d_ = e_old_ - o["end"]
                if d_ > EPS:
                    for k_, row_ in enumerate(cc_falls):
                        if abs(row_[1] - e_old_) < 1e-6:
                            cc_falls[k_] = (row_[0] - d_, row_[1] - d_, *row_[2:])
                            breaks.extend([row_[0] - d_, row_[1] - d_, row_[1] - d_ + (row_[3] if len(row_) > 3 else 0.3)])
        if leg_head_row_leads:
            print(f"  {tname}: LEG_HEAD_AFTER_ROW_LEAD_S on {len(leg_head_row_leads)} notes: {leg_head_row_leads}", file=sys.stderr)
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
            keep_ = any(abs(k_ - sq_) < 0.02 for k_ in REATTACK_KEEP_END.get(tname, []))   # scherzo c14
            for o in pv_:
                if keep_ and o["pitch"] != n["pitch"]:
                    continue
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
    # scherzo c16: ROW_CHANGE_LEAD_S (see the default)
    row_change_leads = []
    rcl_ = ROW_CHANGE_LEAD_S.get(tname)

    def _prev_room(q, p_):
        """the longest lead of a note at q after p_: scherzo c17 (critic A #1), with PREV_MIN_SOUND_S the previous note
        sounds at least that long alone, counted from its MOVED note-on; without it the c16 cap (score slot less 20 ms)"""
        if PREV_MIN_SOUND_S is None:
            return (q - p_["qn"]) - lead_qn(q, ROW_CHANGE_LEAD_GAP_S)
        return (q - p_["qn"]) + shift.get(id(p_), 0.0) - lead_qn(q, PREV_MIN_SOUND_S)
    if rcl_:
        for n in ns:
            if not _lg(n.get("art") or "") or n.get("grace"):
                continue
            q = n["qn"]
            prevs_ = [o for o in ns if o is not n and o["qn"] < q - EPS and orig_end[id(o)] > q - 0.06]
            if not prevs_:
                continue
            p_ = max(prevs_, key=lambda o: o["qn"])
            if not p_.get("art") or _lg(p_["art"]) or any(_lg(o.get("art") or "") for o in prevs_):
                continue
            want_ = min(lead_qn(q, rcl_), _prev_room(q, p_))
            if want_ > shift.get(id(n), 0.0) + 1e-3:
                row_change_leads.append([round(q, 3), round((qn_to_sec(q) - qn_to_sec(q - shift.get(id(n), 0.0))) * 1000),
                                         round((qn_to_sec(q) - qn_to_sec(q - want_)) * 1000)])
                shift[id(n)] = want_
        if row_change_leads:
            print(f"  {tname}: ROW_CHANGE_LEAD_S {rcl_} s on {len(row_change_leads)} notes: {row_change_leads}", file=sys.stderr)
    # scherzo c20: ROW_CHANGE_ACC_ADD_S (see the default)
    rca_ = ROW_CHANGE_ACC_ADD_S.get(tname)
    if rca_:
        rca_done = []
        for n in ns:
            a_ = n.get("art") or ""
            if _lg(a_) or n.get("grace") or n["qn"] not in accent_q or not any(w_ in a_ for w_ in ("Sus", "Marc")) \
                    or any(abs(n["qn"] - k_) < 0.02 for k_ in (list(ROW_CHANGE_ACC_SKIP.get(tname, [])) + list(
                        ROW_CHANGE_ACC_SKIP.get("_all", [])) if isinstance(ROW_CHANGE_ACC_SKIP, dict) else ROW_CHANGE_ACC_SKIP)):
                continue
            q = n["qn"]
            prevs_ = [o for o in ns if o is not n and q - 1.0 - EPS <= o["qn"] < q - EPS]   # a short note just before
            if not prevs_:
                continue
            p_ = max(prevs_, key=lambda o: o["qn"])
            if not any(w_ in (p_.get("art") or "") for w_ in ("Stac", "Spic")):
                continue
            if (p_.get("art") or "") in ROW_CHANGE_ACC_SKIP_PREV.get(tname, ()):   # scherzo c21
                continue
            old_ = shift.get(id(n), 0.0)
            want_ = min(old_ + lead_qn(q, rca_), _prev_room(q, p_))
            if want_ > old_ + 1e-3:
                rca_done.append([round(q, 3), round((qn_to_sec(q) - qn_to_sec(q - old_)) * 1000),
                                 round((qn_to_sec(q) - qn_to_sec(q - want_)) * 1000)])
                shift[id(n)] = want_
        if rca_done:
            print(f"  {tname}: ROW_CHANGE_ACC_ADD_S {rca_} s on {len(rca_done)} notes: {rca_done}", file=sys.stderr)
    # scherzo c16: LEAD_SET_AT (see the default)
    lead_set = []
    for k_, v_ in sorted(LEAD_SET_AT.get(tname, {}).items()):
        k_ = float(k_)
        for n in [n for n in ns if abs(n["qn"] - k_) < 0.02 and not n.get("grace")]:
            q = n["qn"]
            before_ = [o for o in ns if o is not n and o["qn"] < q - EPS]
            p_ = max(before_, key=lambda o: o["qn"]) if before_ else None
            want_ = lead_qn(q, v_)
            if p_ is not None:
                want_ = min(want_, _prev_room(q, p_))
            old_ = shift.get(id(n), 0.0)
            if abs(want_ - old_) < 1e-4:
                continue
            for o in before_:   # a legato join keeps its overlap
                if _lg(n.get("art") or "") and _lg(o.get("art") or "") and abs(o["end"] - (q - old_)) < 0.2:
                    o["end"] = max(o["qn"] - shift.get(id(o), 0.0) + 0.05, o["end"] + (old_ - want_))
            pulls = [(q - want_, b_) if abs(b_ - q) < EPS and abs(a_ - (q - old_)) < 1e-6 else (a_, b_) for a_, b_ in pulls]
            shift[id(n)] = want_
            lead_set.append([round(q, 3), round((qn_to_sec(q) - qn_to_sec(q - old_)) * 1000), round((qn_to_sec(q) - qn_to_sec(q - want_)) * 1000)])
    if lead_set:
        print(f"  {tname}: LEAD_SET_AT on {len(lead_set)} notes", file=sys.stderr)
    PULL_PAD_QN = 0.01
    pulls = sorted(set((round(a_ - PULL_PAD_QN, 4), b_) for a_, b_ in pulls))

    # scherzo c06 (critic C #1): an entry led early onto a printed fp / sfp held the level the curve had at the score
    # onset itself, before the spike (which starts 0.02 qn after the mark): the bar-301 sfp winds started at p and swelled
    # 35-60 ms later. With FP_SPIKE_FROM_ONSET the pull holds the spike's level (the curve 0.021 qn after the mark), so the
    # attack starts at the moved onset; the hold and the fall to p stay timed from the score qn
    fp_q_ = [q_ for q_, d_ in marks if d_ in ("fp", "sfp")] if FP_SPIKE_FROM_ONSET and FP_SPIKE else []

    def pull_q(b_):
        return b_ + 0.021 if any(abs(b_ - f_) < EPS for f_ in fp_q_) else b_

    def final2(q):
        for a_, b_ in pulls:
            if a_ - EPS <= q < b_:
                return final(pull_q(b_))
        if fp_q_ and pull_q(q) != q and any(abs(b_ - q) < EPS for a_, b_ in pulls):
            return final(pull_q(q))   # scherzo c06: the pull's end on the fp mark itself (no 0.02 qn notch to p)
        return final(q)
    breaks += [x for a_, b_ in pulls for x in (a_, b_)]

    def new_on(n):
        return n["qn"] - shift.get(id(n), 0.0)

    def shifted_on(q):
        return min([new_on(o) for o in ns if abs(o["qn"] - q) < EPS] + [q])

    if acc_cc_:
        breaks += _acc_cc_build(shift)
    cc16_on_[0] = True   # scherzo c16: CC11_REST_MAP and ACCENT_CC from here on (the written lanes)
    cc11 = sample(final2, breaks) if ns else []
    # mvt1 c51: SHORT_CC11_PARK (see the default): CC11 parked over short-row runs, the level returned in vol_db
    cc11_park, cc11_park_env, beat_db_notes, beat_db_env = [], [], [], []
    SP_ = SHORT_CC11_PARK
    if SP_ and family in SP_.get("families", ("string",)) and cc11:
        def _is_short(o_):
            return any((o_.get("art") or "").startswith(r_) for r_ in SP_["rows"])
        on_ = sorted(ns, key=lambda o_: (new_on(o_), o_["pitch"]))
        runs_, cur_ = [], []
        for o_ in on_:
            if o_.get("grace"):
                continue
            if _is_short(o_):
                cur_.append(o_)
            else:
                if cur_:
                    runs_.append((cur_, new_on(o_)))
                    cur_ = []
        if cur_:
            runs_.append((cur_, None))
        pv_ = lambda q_: value_at([(0.0, cc11[0][1])] + cc11, q_) if False else next(
            (v_ for q__, v_ in reversed(cc11) if q__ <= q_ + 1e-9), cc11[0][1])
        gg_ = lambda c_: 20 * __import__("math").log10(max(1e-4, value_at(SP_["gg_amp"], c_)))
        for r_, nx_ in runs_:
            a_ = round(new_on(r_[0]) - 0.02, 4)
            e_last_ = max(o_["end"] - shift.get(id(o_), 0.0) for o_ in r_)
            b_ = round(min(nx_ - 0.01, e_last_ + 2.0) if nx_ is not None else e_last_ + 2.0, 4)
            if SP_.get("pre_s"):
                # scherzo c15: the CC11 step to the parked value (and the envelope's mirror of Opus's 120 ms fade) starts
                # up to pre_s before the run's first note, not before the end of the note before it: the fade then runs
                # in the gap, not through the first stroke
                m0_ = new_on(r_[0])
                pe_ = max([o_["end"] for o_ in on_ if new_on(o_) < m0_ - EPS], default=None)
                a2_ = sec_to_qn(qn_to_sec(m0_) - SP_["pre_s"])
                if pe_ is not None:
                    a2_ = max(a2_, pe_ + 0.01)
                a_ = round(min(a_, max(0.0, a2_)), 4)
            if SP_.get("post_s") is not None and nx_ is not None:
                # scherzo c15: the return to the printed CC11 starts post_s after the run's last note-off (it stood
                # 0.01 qn before the next note, so the first 120 ms of every note after a run carried the envelope's
                # mirror ramp of 5-12 dB)
                b_ = round(min(b_, max(a_ + 0.06, sec_to_qn(qn_to_sec(e_last_) + SP_["post_s"]))), 4)
            if b_ <= a_ + 0.05:
                continue
            cc11_park.append([a_, b_])
        if cc11_park:
            # the CC11 lane: park inside each span, the old value restored at its end
            new_ = []
            for q_, v_ in cc11:
                if not any(a_ - 1e-9 <= q_ < b_ for a_, b_ in cc11_park):
                    new_.append((q_, v_))
            for a_, b_ in cc11_park:
                new_ += [(a_, SP_["cc"]), (b_, pv_(b_))]
            new_.sort(key=lambda x_: x_[0])
            cc11_ = []
            for q_, v_ in new_:
                if cc11_ and abs(cc11_[-1][0] - q_) < 1e-9:
                    cc11_[-1] = (q_, v_)
                elif not cc11_ or cc11_[-1][1] != v_:
                    cc11_.append((q_, v_))
            # the compensation: gg(old, slewed) - gg(new, slewed), sampled every 0.02 s around and inside the spans
            fs_ = SP_.get("fade_s", 0.12)

            def _slewed(lane_, t_):
                q_ = sec_to_qn(t_)
                pts_ = [(qn_to_sec(x_), value_at(SP_["gg_amp"], v_)) for x_, v_ in lane_ if x_ <= q_ + 1e-9]
                if not pts_:
                    return value_at(SP_["gg_amp"], lane_[0][1])
                if len(pts_) == 1:
                    return pts_[-1][1]
                (t1_, a1_), (t0_, a0_) = pts_[-1], pts_[-2]
                x_ = min(1.0, (t_ - t1_) / fs_)
                return a0_ + (a1_ - a0_) * x_
            for a_, b_ in cc11_park:
                ta_, tb_ = qn_to_sec(a_) - 0.02, qn_to_sec(b_) + fs_ + 0.04
                env_, t_, last_ = [], ta_, None
                while t_ <= tb_ + 1e-9:
                    d_ = 20 * __import__("math").log10(max(1e-4, _slewed(cc11, t_)) / max(1e-4, _slewed(cc11_, t_)))
                    d_ = round(d_, 2)
                    if last_ is None or abs(d_ - last_) >= 0.04 or t_ + 0.02 > tb_:
                        env_.append((round(sec_to_qn(t_), 4), d_))
                        last_ = d_
                    t_ += 0.02
                env_[0] = (env_[0][0], 0.0)
                env_[-1] = (env_[-1][0], 0.0)
                cc11_park_env.append(env_)
            cc11 = cc11_
        # metric weight in the envelope (critic B c51 #2 / A #2): beat / "and" / the two sixteenths between
        bdb_ = SP_.get("beat_db") or {}
        for o_ in on_:
            if not _is_short(o_) or o_.get("meas_trem") or not any(
                    a_ - EPS <= o_["qn"] < b_ - EPS for a_, b_ in (SP_.get("beat_spans") or {}).get(tname, [])):
                continue
            fr_ = round((o_["qn"] % 1.0) * 4) / 4.0
            d_ = bdb_.get("beat", 0.0) if fr_ in (0.0, 1.0) else (bdb_.get("and", 0.0) if fr_ == 0.5 else bdb_.get("sixteenth", 0.0))
            mq_ = bdb_.get("meter_qn")   # scherzo c08: the bar's downbeat (triple metre)
            if "downbeat" in bdb_ and mq_ and fr_ in (0.0, 1.0) and min(o_["qn"] % mq_, mq_ - o_["qn"] % mq_) < 0.01:
                d_ = bdb_["downbeat"]
            if abs(o_["qn"] % 0.25) > 0.01 and abs(o_["qn"] % 0.25 - 0.25) > 0.01:
                d_ = 0.0   # triplets and other off-grid strokes: no step
            if abs(d_) < 0.01:
                continue
            m_ = new_on(o_)
            nx2_ = min([new_on(x_) for x_ in on_ if new_on(x_) > m_ + 0.01] + [o_["end"] - shift.get(id(o_), 0.0) + 0.25])
            beat_db_notes.append([round(o_["qn"], 3), d_])
            beat_db_env.append([(round(m_ - 0.012, 4), 0.0), (round(m_, 4), d_), (round(nx2_ - 0.012, 4), d_),
                                (round(nx2_, 4), 0.0)])
    # check: every printed mark is on the curve
    for q, d in marks:
        if d in ("sf", "sfz"):
            continue
        # mvt2 v600 port (c27): an fp is checked after its spike (FP_SPIKE: f, then p by FP_SPIKE[2] qn)
        got = value_at(pts, q + (FP_SPIKE[2] if d in ("fp", "sfp") and FP_SPIKE else 0.0) + 0.001)
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
        v_ = cc1_fn_c(q)
        for a_, b_, c_ in CC1_SET_SPANS.get(tname, []):   # scherzo c20: CC1_SET_SPANS (see the default)
            if a_ - EPS <= q < b_ - EPS:
                v_ = min(v_, c_)
        for a_, b_, c_ in CC1_FLOOR_SPANS.get(tname, []):   # scherzo c23: CC1_FLOOR_SPANS (see the default)
            if a_ - EPS <= q < b_ - EPS:
                v_ = max(v_, c_)
        return v_

    def cc1_fn_c(q):
        # c22 (A #1c): inside a pull, the entry's own vibrato (as final2 does for CC11); it was the previous note's
        q = next((pull_q(b_) for a_, b_ in pulls if a_ - EPS <= q < b_), q)   # scherzo c06: pull_q (fp spikes)
        if fp_q_ and pull_q(q) != q and any(abs(b_ - q) < EPS for a_, b_ in pulls):
            q = pull_q(q)
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
                # scherzo c07 (ported from mvt3 c07): PHRASE_SHAPE goes into the dynamic-layer lane (CC1) on these tracks
                po_ = phrase_off(q) if phrase_shapes else 0.0
                c1_ = value_at(map_, base(q) + po_)
                if po_ < 0 and PS_.get("cc1_floor"):   # no dip into the layer boundaries under cc1_floor
                    c1_ = max(c1_, min(value_at(map_, base(q)), PS_["cc1_floor"]))
                return round(c1_)
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
    vbr += [x for a_, b_, _ in CC1_SET_SPANS.get(tname, []) for x in (a_, b_)]   # scherzo c20
    vbr += [x for a_, b_, _ in CC1_FLOOR_SPANS.get(tname, []) for x in (a_, b_)]   # scherzo c23
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
    timp_damp = []   # scherzo c04
    timp_hp = []   # c13 (A #3)
    vol_parts = []   # c02: exact level offsets in dB, written as a track volume envelope by build_reaper.py
    vol_tags = {}    # scherzo c15: id(item) -> "class:layer" (see ONE_LEVEL)
    hp_start_moved = []   # scherzo c25: HP_START_MOVED
    hp_held_end = []      # scherzo c25: HP_HOLD_TO_NOTE_END
    hp_hold_skipped_dec = []   # scherzo c26: holds skipped under a printed decrescendo

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
            if n["art"].endswith(("Lng", "Sht")):   # strokes: roll level + 16 dB, +20 at pp and below (c02: pp strokes inaudible)
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
        # scherzo c04: TIMP_DAMP_AT (see the option): fall before the hall, held to the next onset's CC7 point
        for fa_, fb_, fv_ in TIMP_DAMP_AT:
            nx_ = min([n["qn"] - 0.02 for n in ns if n["qn"] - 0.02 > fb_] + [END + 1.0])
            v0_ = ([c[1] for c in cc7 if c[0] <= fa_ + EPS] or [127])[-1]
            k_ = max(1, int(round((fb_ - fa_) / 0.05)))
            fall_ = [(round(fa_ + (fb_ - fa_) * j / k_, 4), max(1, int(round(v0_ + (fv_ - v0_) * j / k_)))) for j in range(k_ + 1)]
            cc7 = sorted([c for c in cc7 if not (fa_ - EPS <= c[0] < nx_ - EPS)] + fall_, key=lambda c: c[0])
            timp_damp.append([fa_, fb_, fv_, round(nx_, 3)])
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
            vol_add("slow:timp_roll", ("env", ps))
            timp_hp.append([round(q, 3), round(max(v_ for _, v_ in ps), 2), round(min(v_ for _, v_ in ps), 2)])
        cc11, cc1 = [], []
        # mvt1 c12 (critic A #1): the felt timpani Rls row has eight dynamic layers (V1-V8) crossfaded by CC1 (each
        # group's Source volume is driven by a cc 1 MidiController, fadeTime 120 ms; read with opus_state.load_oib), and
        # the strokes (Lng/Sht) are velocity-layered with no CC1. With no CC1 lane every roll played one bright layer
        # (1-8 kHz share -11.5..-14.9 dB from ppp to fff, against a 20 dB spread on the strokes). CC1 now follows the
        # printed dynamic curve through TIMP_CC1_MAP, TIMP_CC1_PAD_QN ahead (so a roll starts on its own layer)
        rolls_c1_ = [n for n in ns if n["art"].endswith("Rls")]
        if TIMP_CC1_MAP and rolls_c1_:
            c1_at_ = [(n["qn"], orig_end[id(n)], v_) for n in rolls_c1_ for k_, v_ in TIMP_CC1_AT.items() if abs(n["qn"] - k_) < 0.02]

            def timp_cc1_(q):   # scherzo c16: TIMP_CC1_AT
                for a_, e_, (v0_, v1_) in c1_at_:
                    if a_ - TIMP_CC1_PAD_QN - EPS <= q < e_:
                        return v0_ + (v1_ - v0_) * max(0.0, min(1.0, (q - a_) / max(EPS, e_ - a_ - 0.1)))
                return value_at(TIMP_CC1_MAP, base(q + TIMP_CC1_PAD_QN))
            cc1 = sample(timp_cc1_, breaks + [n["qn"] - TIMP_CC1_PAD_QN for n in rolls_c1_]
                         + [x_ for a_, e_, _ in c1_at_ for x_ in (a_ - TIMP_CC1_PAD_QN, e_)])
        # mvt1 c12: per-dynamic level trims on the rolls only (the soft CC1 layers are quieter in themselves), read from
        # the printed curve over each roll, held through its ring to the next onset (like the settle)
        if TIMP_ROLL_TRIM_DB:
            for n in rolls_c1_:
                q, e = n["qn"], orig_end[id(n)]
                nx = min([o["qn"] for o in ns if o["qn"] >= e - EPS and o is not n] + [e + 1.0])
                def rtrim_(qx, q=q, e=e):
                    # scherzo c02 (critic C #4): TIMP_ROLL_TRIM_HOLD_CRESC: under a printed crescendo the trim keeps its
                    # value at the hairpin's start (or the roll's), so the CC1 / CC7 crescendo is heard (the table fell
                    # 11 dB from p to f and cancelled bar 101's p < f roll)
                    hp_ = next((a_ for a_, b_, k_ in hps if k_ == "cresc" and a_ - EPS <= qx and a_ < e - EPS
                                and b_ > q + EPS and not any(abs(a_ - k2_) < 0.05 for k2_ in TIMP_ROLL_TRIM_HOLD_SKIP)),
                               None) if TIMP_ROLL_TRIM_HOLD_CRESC else None
                    v_ = value_at(TIMP_ROLL_TRIM_DB, base(qx))
                    if hp_ is None:
                        return v_
                    v0_ = value_at(TIMP_ROLL_TRIM_DB, base(max(q, hp_)))
                    return v0_ - (1.0 - TIMP_ROLL_TRIM_HOLD_CRESC) * (v0_ - v_)
                ps = [(q - 0.02, rtrim_(q))]
                ps += [(q + 0.125 * j, rtrim_(q + 0.125 * j))
                       for j in range(int((e - q) / 0.125) + 1) if q + 0.125 * j < e - EPS]
                ps += [(max(ps[-1][0] + 0.01, nx - 0.05), ps[-1][1])]
                if max(abs(v_) for _, v_ in ps) >= 0.05:
                    vol_add("slow:timp_roll", ("env", ps))
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
            if any(abs(c0 - k_) < 0.02 for k_ in TIMP_SETTLE_SKIP):   # scherzo c16
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
                vol_add("slow:timp_flat", ("flat", c0, max(ce, nxt_on - 0.05), -6.0))   # held through the ring, like the settle
        # c10 (B #2): rolls and strokes printed f or louder start at their dynamic: +TIMP_LOUD_ATTACK_DB from the onset
        # (10 ms rise), held 0.25 qn, gone by 0.75 qn (before the settle has fallen 1.3 dB). The roll body is unchanged.
        loud_done_ = set()   # scherzo c02 (critic B #3): once per onset (a 2-note stroke at the summit got +12 dB)
        for n in ns:
            q = n["qn"]
            if round(q, 3) in loud_done_:
                continue
            loud_done_.add(round(q, 3))
            mk_ = [DYN[d_] for q_, d_ in marks if abs(q_ - q) < 0.01 and d_ in DYN]
            pm_ = [DYN[d_] for q_, d_ in marks if q_ < q - 0.01 and d_ in DYN]
            arr_ = bool(mk_) and (not pm_ or max(mk_) > pm_[-1])   # a printed arrival louder than the last mark
            if base(q + 0.01) >= DYN["f"] and n in rolls and any(abs(orig_end[id(o)] - q) < 0.05 for o in rolls) \
                    and not arr_ and not any(abs(q - k_) < 0.02 for k_ in TIMP_CHAIN_BUMP_AT):
                timp_chain_skip.append(round(q, 3))   # mvt1 c07 (B #4): a roll continuing a roll is not a new attack
            elif base(q + 0.01) >= DYN["f"] and n.get("_tlv"):
                # scherzo c15: the stroke's weight is in its velocity; what the cap clipped is one flat level
                want_, got_ = n["_tlv"]
                r_ = round(TIMP_LOUD_VEL_ADD[2] * (want_ - got_) / TIMP_LOUD_VEL_ADD[0], 1)
                timp_vel_strokes.append([round(q, 3), n["vel"], r_])
                if r_ >= 0.3:
                    nx_ = [o["qn"] for o in ns if o["qn"] > q + EPS]
                    ne_ = min(min(nx_) if nx_ else 1e9, q + 1.5 * bpm_at(q) / 60)
                    vol_add("level:timp_level", ("env", [(qn_before(q, 0.03), 0.0), (qn_before(q, 0.01), r_),
                                                         (max(q + 0.002, qn_before(ne_, 0.03)), r_),
                                                         (max(q + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
            elif base(q + 0.01) >= DYN["f"]:
                # c14 (A #2): a tied-roll stroke already sits on the roll's hairpin gain: half the bump
                ad_ = TIMP_LOUD_ATTACK_DB * (0.5 if n.get("tie_stroke") else 1.0)
                vol_add("shape:timp_attack", ("env", [(q - 0.01, 0.0), (q + 0.01 * bpm_at(q) / 60, ad_),
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
    for a, b2, dbv, er in rows_:
        if er:
            vol_add("slow:role", ("span", a, b2, dbv, er))
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
        if ROLE_EDGE_MOVED:   # scherzo c17 (see the default)
            def _mv(qe_):
                m_ = min([n["qn"] - shift.get(id(n), 0.0) for n in ns if abs(n["qn"] - qe_) < 0.02], default=None)
                return m_ if m_ is not None and m_ < qe_ - 0.02 else None
            m_ = _mv(a)
            if m_ is not None and len(pin) == 2 and pin[0][1] == 0.0 and abs(pin[-1][0] - a) < 1e-6:
                pin = [(m_ - lead_qn(m_, ROLE_EDGE_MOVED), 0.0), (m_, dbv)]
            m_ = _mv(b2)
            if m_ is not None and not next_ and abs(pout[0][0] - b2) < 1e-6 and m_ > pin[-1][0] + 0.05:
                pout = [(m_ - lead_qn(m_, ROLE_EDGE_MOVED), dbv), (m_, 0.0)]
            # scherzo c30: chained edges on listed onsets (see ROLE_EDGE_MOVED_CHAINED_AT)
            if prev_ and any(abs(a - x_) < 0.02 for x_ in ROLE_EDGE_MOVED_CHAINED_AT):
                m_ = _mv(a)
                if m_ is not None:
                    pin = [(m_ - lead_qn(m_, ROLE_EDGE_MOVED), 0.0), (m_, dbv)]
            if next_:
                nb_ = min(r[0] for r in next_)
                m_ = _mv(nb_) if any(abs(nb_ - x_) < 0.02 for x_ in ROLE_EDGE_MOVED_CHAINED_AT) else None
                if m_ is not None and m_ - lead_qn(m_, ROLE_EDGE_MOVED) > pin[-1][0] + 0.01:
                    pout = [(m_ - lead_qn(m_, ROLE_EDGE_MOVED), dbv), (m_, 0.0)]
        vol_add("slow:role", ("env", pin + pout))
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
                    vol_add("slow:hairpin", ["hpgain", a, b2, min(nx, arr + HP_HOLD_CAP, b2 + 1.0), g_, 0.0, HP_REL, 0.0, 0.0,
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
                vol_add("slow:hairpin", ["hpgain", a, b2, hold_end, g_, 0.0, HP_REL, sost_end, share_ * g_, mfa, fff_])
        # c09 (B #1): chain consecutive crescendos to f+ (no softer printed mark between the first arrival and the
        # second start): the first holds its gain to the second's start without a release, the second starts from it
        hpi = sorted([it for it in vol_parts if it[0] == "hpgain"], key=lambda it: it[1])
        for it1, it2 in zip(hpi, hpi[1:]):
            b1, a2 = it1[2], it2[1]
            if len(it1) > 11 or len(it2) > 11:
                continue   # c32: a loud swell neither chains nor is chained
            # scherzo c02 (critic C #3): a softer mark printed at the second hairpin's start (the tutti sfp of bar 301,
            # read as its p) ends the chain too: the strict test had kept the first crescendo's +3..+7 dB through the p
            if not it1[9] and -EPS <= a2 - b1 <= HP_CHAIN and not any((b1 + EPS < mq < a2 - EPS or abs(mq - a2) <= EPS)
                                                       and DYN[d_] < base(b1 - 0.01)
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
                    vol_add("slow:hairpin", ("env", [(a, 0.0), (b2, g_), (max(b2, da) + 0.001, g_), (db_, -1.0),
                                              (db_ + 1.0, 0.0)]))
                    used_dec.append(round(da, 3))
                    hp_soft_spans.append((a, db_))
                else:
                    vol_add("slow:hairpin", ("env", [(a, 0.0), (b2, g_), (b2 + HP_REL, 0.0)]))
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
                    vol_add("slow:hairpin", ["hpgain", a, b2, max(b2, da), g_, 0.0, max(0.25, db_ - da),
                                      0.0, 0.0, True])
                    used_dec.append(round(da, 3))
                    if in_lead:
                        hp_soft_spans.append((a, db_))
                        # c22 (C #1): a listed decrescendo depth deeper than the messa di voce's release adds the rest
                        dd_ = next((v_ for k_, v_ in HP_SOFT_DEC_AT.get(tname, {}).items() if abs(da - k_) < 0.3), 0.0)
                        if dd_ > g_:
                            nx = min([n["qn"] for n in ns if n["qn"] > db_ + 0.05], default=db_ + 1.0)
                            vol_add("slow:hairpin", ["hpgain", da, db_, min(nx, db_ + HP_HOLD_CAP), -(dd_ - g_), 0.0, HP_REL,
                                              0.0, 0.0, True])
                else:
                    arr = min([n["qn"] for n in ns if n["qn"] >= b2 - 0.05], default=b2)
                    nx = min([n["qn"] for n in ns if n["qn"] > arr + 0.05], default=arr + HP_HOLD_CAP)
                    hold_end = min(nx, arr + HP_HOLD_CAP)
                    if arr > b2 + 0.25:
                        hold_end = min(arr, b2 + 2.0)
                    vol_add("slow:hairpin", ["hpgain", a, b2, hold_end, g_, 0.0, HP_REL, 0.0, 0.0, True])
                    if in_lead:
                        hp_soft_spans.append((a, b2))
                (hp_soft if in_lead else hp_soft_acc).append(round(a, 3))
            elif k == "decresc" and round(a, 3) not in used_dec:
                # c18 (C #1b): a decrescendo after a crescendo is skipped only when that crescendo's messa di voce
                # already releases across it (used_dec); after an hpgain (mf) crescendo it gets its own ramp
                nx = min([n["qn"] for n in ns if n["qn"] > b2 + 0.05], default=b2 + 1.0)
                hold_ = min(nx, b2 + HP_HOLD_CAP)
                if HP_DEC_HOLD_HELD:
                    # scherzo c10 (critic C #3): a decrescendo arriving inside a note that still sounds keeps its
                    # gain to that note's end (Horn 1's last ppp swelled +2.5 dB released mid-note into the fermata)
                    held_ = max([n["end"] for n in ns if n["qn"] < b2 - 0.05 and n["end"] > b2 + 0.05], default=None)
                    if held_ is not None and nx > held_ - 0.05:
                        hold_ = held_
                if in_lead:
                    dd_ = next((v_ for k_, v_ in HP_SOFT_DEC_AT.get(tname, {}).items() if abs(a - k_) < 0.3),
                               HP_SOFT_DEC_DB)
                    hp_soft_spans.append((a, b2))
                else:
                    dd_ = HP_GAIN_SOFT_ACC_DB
                vol_add("slow:hairpin", ["hpgain", a, b2, hold_, -dd_, 0.0, HP_REL, 0.0, 0.0, True])
                (hp_soft if in_lead else hp_soft_acc).append(round(a, 3))
    # scherzo c17: HP_GAIN_TO_CC11 (see the default)
    hp_to_cc11 = []
    hc_ = (HP_GAIN_TO_CC11.get(tname, HP_GAIN_TO_CC11.get(family)) if HP_GAIN_TO_CC11 else None) if cc11 else None
    if hc_:
        snd_ = []   # scherzo c18: the track's sounding spans (score positions), merged
        for n_ in sorted(ns, key=lambda x_: x_["qn"]):
            if snd_ and n_["qn"] <= snd_[-1][1] + EPS:
                snd_[-1][1] = max(snd_[-1][1], n_["end"])
            else:
                snd_.append([n_["qn"], n_["end"]])

        def _rest_after(q_, min_qn=0.5):
            """(start, end) of the first rest of min_qn or more at or after q_ (None)"""
            prev_e_ = None
            for s0_, s1_ in snd_:
                if s1_ <= q_ + EPS:
                    prev_e_ = s1_
                    continue
                if s0_ > q_ + EPS:
                    st_ = max(q_, prev_e_ if prev_e_ is not None else q_)
                    if s0_ - st_ >= min_qn - EPS:
                        return (st_, s0_)
                prev_e_ = s1_
            return None

        def _keep(it, r0_, g_):
            # scherzo c18: a gain left in the envelope is released across a printed decrescendo (from its start or
            # the arrival to its end), by the next softer printed mark, inside the next rest of 0.5 qn or more
            # (held to it), or else at keep_rel_db_s
            if not hc_.get("keep_rel_db_s") or not it[6]:
                return
            sost_ = len(it) > 8 and it[7] and it[7] > it[3] + EPS
            rs_ = it[7] if sost_ else r0_
            gr_ = abs(it[8]) if sost_ else abs(g_)
            if not sost_:
                dec_ = sorted((h_[0], h_[1]) for h_ in hps if h_[2] == "decresc"
                              and (it[2] - 0.3 <= h_[0] <= r0_ + EPS or h_[0] - 0.3 <= r0_ < h_[1]))
                if dec_:
                    it[3] = min(r0_, max(dec_[0][0], it[2]))
                    it[6] = max(0.25, dec_[0][1] - it[3])
                    hp_kept.append([round(it[1], 3), round(it[2], 3), "dec", round(it[3], 2), round(it[6], 2)])
                    return
            hu_ = hc_.get("hold_until_mark_qn")
            if hu_ and not sost_:
                # scherzo c27 (critic B #1): the gain left in the envelope is a passage level: it holds from the arrival
                # until the first of (a) a printed decrescendo start or a softer printed mark (released there), (b) a
                # louder printed mark (the held gain shrinks there by the table's CC11 rise, so the level never falls
                # at a louder mark, then holds on), (c) the first rest of 0.5 qn or more (released inside it), (d) hu_
                # qn after the arrival (the slow release from there). No fade inside the arrival note.
                cur_ = base(it[2] - 0.01)
                lim_ = it[2] + hu_
                dq_ = min([h_[0] for h_ in hps if h_[2] == "decresc" and rs_ + EPS < h_[0] < lim_], default=None)
                sq_ = min([mq for mq, d_ in marks if d_ in DYN and rs_ + EPS < mq < lim_ and DYN[d_] < cur_
                           and not (d_ == "sfp" and HP_SUBITO_SFP_DELAY_S is not None)], default=None)
                lq_ = min([mq for mq, d_ in marks if d_ in DYN and rs_ + EPS < mq < lim_ and DYN[d_] > cur_], default=None)
                r_ = _rest_after(rs_, hc_.get("hold_rest_min_qn", 0.5))
                rq_ = r_[0] if r_ is not None and r_[0] < lim_ else None
                stops_ = [(x_, k_) for x_, k_ in ((dq_, "dec"), (sq_, "soft"), (rq_, "rest"), (lim_, "cap")) if x_ is not None]
                st_, k_ = min(stops_)
                if k_ == "cap" and hc_.get("hold_to_dec_qn"):
                    # scherzo c28 (critic B #1): no printed change within the cap: the hold runs on to a printed
                    # decrescendo starting within hold_to_dec_qn of the arrival when no softer mark and no rest of
                    # hold_rest_min_qn or more comes before it (released across the decrescendo, a printed move)
                    lim2_ = it[2] + hc_["hold_to_dec_qn"]
                    dq2_ = min([h_[0] for h_ in hps if h_[2] == "decresc" and rs_ + EPS < h_[0] < lim2_], default=None)
                    if dq2_ is not None:
                        sq2_ = min([mq for mq, d_ in marks if d_ in DYN and rs_ + EPS < mq < dq2_ and DYN[d_] < cur_
                                    and not (d_ == "sfp" and HP_SUBITO_SFP_DELAY_S is not None)], default=None)
                        if sq2_ is None and not (r_ is not None and r_[0] < dq2_):
                            st_, k_, lim_ = dq2_, "dec", dq2_ + 0.01
                            lq_ = min([mq for mq, d_ in marks if d_ in DYN and rs_ + EPS < mq < lim_ and DYN[d_] > cur_],
                                      default=None)
                gh_ = g_
                if lq_ is not None and lq_ < st_ - EPS:
                    rise_ = max(0.0, (base(lq_ + 0.01) - base(lq_ - 0.01)) * hc_.get("db_per_unit", 0.22))
                    gh_ = max(0.0, abs(g_) - rise_) * (1 if g_ > 0 else -1)
                if k_ == "dec":
                    de_ = min([h_[1] for h_ in hps if h_[2] == "decresc" and abs(h_[0] - st_) < EPS])
                    rel_ = max(0.25, de_ - st_)
                elif k_ == "soft":
                    rel_ = 0.2
                    st_ = max(rs_, st_ - 0.2)
                elif k_ == "rest":
                    rel_ = max(0.1, min(r_[1] - 0.05 - st_, sec_to_qn(qn_to_sec(st_) + hc_.get("rest_rel_s", 0.6)) - st_))
                else:
                    rel_ = max(it[6], sec_to_qn(qn_to_sec(st_) + abs(gh_) / hc_["keep_rel_db_s"]) - st_)
                    r2_ = _rest_after(st_, 0.25)
                    if r2_ is not None and r2_[0] < st_ + hc_.get("hold_rest_extra_qn", 0.0):
                        # a rest of 0.25 qn or more soon after the cap: released inside it
                        st_ = r2_[0]
                        k_ = "cap_rest"
                        mo_ = min([o["qn"] - shift.get(id(o), 0.0) for o in ns if abs(o["qn"] - r2_[1]) < EPS] + [r2_[1]])
                        rel_ = max(0.05, min(mo_ - 0.03 - st_, sec_to_qn(qn_to_sec(st_) + hc_.get("rest_rel_s", 0.6)) - st_))
                    elif hc_.get("hold_rest_extra_qn") and any(
                            st_ - EPS <= o["qn"] < st_ + hc_["hold_rest_extra_qn"]
                            and not any(p is not o and p["qn"] < o["qn"] - EPS and orig_end[id(p)] > o["qn"] - shift.get(id(o), 0.0) + 0.01
                                        for p in ns) for o in ns):
                        # no rest: a step at the next re-attack (no note sounding across its moved note-on), finished
                        # 0.02 qn before that note-on (a passage level at a note-on)
                        o_ = min((o for o in ns if st_ - EPS <= o["qn"] < st_ + hc_["hold_rest_extra_qn"]
                                  and not any(p is not o and p["qn"] < o["qn"] - EPS and orig_end[id(p)] > o["qn"] - shift.get(id(o), 0.0) + 0.01
                                              for p in ns)), key=lambda x_: x_["qn"])
                        mo_ = o_["qn"] - shift.get(id(o_), 0.0)
                        st_ = mo_ - 0.08
                        rel_ = 0.06
                        k_ = "cap_step"
                    elif r2_ is not None and r2_[0] < st_ + rel_:
                        rel_ = max(0.1, r2_[0] + min(r2_[1] - r2_[0] - 0.05, 0.5) - st_)
                if gh_ != g_:
                    # at the louder mark the item is released over 0.1 qn ending 0.05 qn before the mark (the led
                    # note-on) and a second item takes over with gh_ over the same 0.1 qn, held to st_, released there
                    t0_ = max(rs_, lq_ - 0.15)
                    it[3], it[6] = t0_, 0.1
                    if len(it) > 8:
                        it[7], it[8] = 0.0, 0.0
                    if abs(gh_) > 1e-6 and st_ > t0_ + 0.1:
                        vol_add("slow:hairpin", ["hpgain", t0_, t0_ + 0.1, st_, gh_, 0.0, rel_, 0.0, 0.0, False])
                else:
                    it[3] = st_
                    it[6] = rel_
                hp_kept.append([round(it[1], 3), round(it[2], 3), "hold:" + k_, round(st_, 2), round(rel_, 2),
                                round(gh_, 2)])
                return
            rel_q_ = max(it[6], sec_to_qn(qn_to_sec(rs_) + gr_ / hc_["keep_rel_db_s"]) - rs_)
            soft_ = [mq for mq, d_ in marks if d_ in DYN and rs_ + EPS < mq < rs_ + rel_q_ and DYN[d_] < base(it[2] - 0.01)
                     and not (d_ == "sfp" and HP_SUBITO_SFP_DELAY_S is not None)]
            r_ = _rest_after(rs_)
            how_ = "slow"
            if r_ is not None and r_[0] < rs_ + rel_q_ - EPS and (not soft_ or r_[0] < min(soft_)):
                # a rest inside the release: held to it when it starts within 1 qn, released inside it; otherwise the
                # slow release runs from its start and ends in the rest at the latest
                st_ = max(rs_, r_[0]) if r_[0] - rs_ <= 1.0 + EPS else rs_
                rel_q_ = max(0.1, min(rs_ + rel_q_, r_[1] - 0.05) - st_)
                if st_ >= r_[0] - EPS:   # inside the rest: over at most rest_rel_s (a G.P.'s tail falls as before)
                    rel_q_ = min(rel_q_, sec_to_qn(qn_to_sec(st_) + hc_.get("rest_rel_s", 0.6)) - st_)
                if sost_:
                    it[7] = st_
                else:
                    it[3] = st_
                how_ = "rest"
            elif soft_:
                rel_q_ = max(min(it[6], 0.25), min(soft_) - rs_)
                how_ = "mark"
            it[6] = rel_q_
            hp_kept.append([round(it[1], 3), round(it[2], 3), how_, round(it[7] if sost_ else it[3], 2), round(it[6], 2)])
        hp_kept = []
        for it in sorted([it for it in vol_parts if it[0] == "hpgain" and it[4] > 0], key=lambda x_: x_[1]):
            a_, b_, r0_, g_ = it[1], it[2], it[3], it[4]
            if any(abs(b_ - x_) < 0.3 for x_ in hc_.get("drop_always", ())):   # scherzo c20: dropped, chained or not
                vol_parts[:] = [x_ for x_ in vol_parts if x_ is not it]
                hp_to_cc11.append([round(a_, 3), round(b_, 3), 0])
                continue
            if any(abs(b_ - x_) < 0.3 for x_ in hc_.get("drop_ends", ())):
                if hc_.get("drop_keep_chain") and len(it) > 5 and it[5] > 0:
                    it[4] = it[5]   # scherzo c18: hold the chained earlier gain, no rise of its own
                    hp_to_cc11.append([round(a_, 3), round(b_, 3), -1])
                    _keep(it, r0_, it[4])
                    continue
                if not hc_.get("drop_only_chained"):
                    vol_parts[:] = [x_ for x_ in vol_parts if x_ is not it]
                    hp_to_cc11.append([round(a_, 3), round(b_, 3), 0])
                    continue
            if (it[7] and it[7] > r0_ + EPS) or (len(it) > 10 and it[10] is True) or any(h_[0] - 0.3 <= r0_ < h_[1] for h_ in hps):
                _keep(it, r0_, g_)
                continue   # a sostenuto share, an fff hold, or a release across a printed hairpin (a printed move)
            if not hc_.get("convert", True):
                _keep(it, r0_, g_)
                continue
            if not any(n["qn"] - shift.get(id(n), 0.0) < r0_ - EPS
                       and qn_to_sec(n["end"]) - qn_to_sec(r0_) >= hc_.get("min_s", 0.25) for n in ns):
                # scherzo c28 (critic B #2a): a short arrival note keeps the gain in the envelope; it now goes through
                # _keep() like the others (it kept the old HP_REL release: a 3-6 dB sag within 1-3 qn of the arrival)
                if hc_.get("keep_short_arrivals"):
                    _keep(it, r0_, g_)
                continue
            arr_cc_ = value_at(rest_map_, base(b_ + 0.01)) if rest_map_ else base(b_ + 0.01)
            if arr_cc_ >= hc_.get("max_arrival_cc", 999):
                _keep(it, r0_, g_)
                continue   # a loud arrival: CC11 is flat up there (the gain would be lost), it stays in the envelope
            vol_parts[:] = [x_ for x_ in vol_parts if x_ is not it]
            u_ = g_ / hc_.get("db_per_unit", 0.22)
            top_ = arr_cc_ + hc_.get("cap_add", 10)
            r1_ = sec_to_qn(qn_to_sec(r0_) + hc_.get("rel_s", 0.6))
            cc11 = lane_add_pl(cc11, [(a_, 0.0), (b_, u_), (max(b_, r0_), u_), (max(b_, r0_, r1_), 0.0)], top_)
            hp_to_cc11.append([round(a_, 3), round(b_, 3), round(u_)])
        if hp_to_cc11:
            print(f"  {tname}: HP_GAIN_TO_CC11 on {len(hp_to_cc11)} crescendo gains "
                  f"({sum(1 for x_ in hp_to_cc11 if not x_[2])} dropped): {hp_to_cc11}", file=sys.stderr)
        pass
    # scherzo c18: LEG_TRANS_CC (see the default)
    ltc_ = LEG_TRANS_CC.get(tname) if cc11 else None
    leg_trans = []
    if ltc_:
        tab_ = {float(k_): v_ for k_, v_ in ltc_.get("table", {}).items() if not str(k_).startswith("_")}
        for n in ns:
            u_ = next((v_ for k_, v_ in tab_.items() if abs(n["qn"] - k_) < 0.02), 0)
            if not u_ or "Leg" not in (n.get("art") or "") or id(n) not in shift:
                continue
            on_ = n["qn"] - shift[id(n)]
            t_on, t_b = qn_to_sec(on_), qn_to_sec(n["qn"])
            if t_b - t_on < ltc_.get("min_lead_s", 0.12) - 1e-6:
                continue
            f0_ = t_on + ltc_.get("from_s", 0.03)
            f1_ = min(f0_ + ltc_.get("fall_s", 0.03), t_b + ltc_.get("hold_s", -0.02) - 0.005)
            h_ = t_b + ltc_.get("hold_s", -0.02)
            if h_ <= f1_:
                continue
            pts_ = [(sec_to_qn(f0_), 0.0), (sec_to_qn(f1_), -u_), (sec_to_qn(h_), -u_), (sec_to_qn(t_b + ltc_.get("ret_s", 0.10)), 0.0)]
            cc11 = lane_add_pl(cc11, pts_)
            leg_trans.append([round(n["qn"], 3), -u_])
        if leg_trans:
            print(f"  {tname}: LEG_TRANS_CC dips on {len(leg_trans)} legato joins", file=sys.stderr)
    if hc_:
        if hp_kept:
            print(f"  {tname}: HP_GAIN_TO_CC11 kept {len(hp_kept)} gains in the envelope, slow release (start, end, rel qn): "
                  f"{hp_kept}", file=sys.stderr)
    # scherzo c25 (critic B #4a): HP_START_MOVED (see the default)
    if HP_START_MOVED is not None:
        mv_on_ = {}
        for n in ns:
            mv_on_[round(n["qn"], 3)] = min(mv_on_.get(round(n["qn"], 3), 9e9), n["qn"] - shift.get(id(n), 0.0))

        def _hp_mv(a_):
            m_ = mv_on_.get(round(a_, 3))
            return qn_before(m_, HP_START_MOVED) if m_ is not None and m_ < a_ - 0.02 else None
        for it in vol_parts:
            if vol_tags.get(id(it)) != "slow:hairpin":
                continue
            if it[0] == "hpgain":
                m_ = _hp_mv(it[1])
                if m_ is not None and m_ < it[2]:
                    it[1] = m_
                    hp_start_moved.append(round(m_, 3))
            elif it[0] == "env" and it[1] and abs(it[1][0][1]) < 1e-9:
                m_ = _hp_mv(it[1][0][0])
                if m_ is not None and len(it[1]) > 1 and m_ < it[1][1][0]:
                    it[1][0] = (m_, it[1][0][1])
                    hp_start_moved.append(round(m_, 3))
    # scherzo c25 (critic B #4d): HP_HOLD_TO_NOTE_END (see the default)
    if HP_HOLD_TO_NOTE_END is not None:
        for it in vol_parts:
            if it[0] != "hpgain" or vol_tags.get(id(it)) != "slow:hairpin" or not it[6] or abs(it[4]) < 1e-6:
                continue
            nx_ = it[3]
            snd_ = [orig_end.get(id(n), n.get("end", n["qn"])) for n in ns
                    if n["qn"] - shift.get(id(n), 0.0) < nx_ - EPS and orig_end.get(id(n), n.get("end", n["qn"])) > nx_ + EPS]
            if not snd_:
                continue
            e_ = max(snd_)
            if e_ > nx_ + HP_HOLD_TO_NOTE_END or (len(it) > 7 and it[7] > nx_):   # too long, or a sostenuto span after
                continue
            # only when a rest follows (no note starts within 0.25 qn after e_ or sounds across it): the release then
            # falls in the rest, not inside the next joined note
            if any(e_ - 0.05 < n["qn"] - shift.get(id(n), 0.0) < e_ + 0.25
                   or (n["qn"] - shift.get(id(n), 0.0) < e_ - EPS and orig_end.get(id(n), n.get("end", n["qn"])) > e_ + 0.05)
                   for n in ns):
                continue
            # scherzo c26 (critic C #3): never hold a gain through a printed decrescendo of the track that overlaps the
            # held span (bar 72's ff > into the pp lost 3-9 dB of its fall); the gain then releases across it as before
            if any(k_ == "decresc" and a_ < e_ - EPS and b_ > nx_ + EPS for a_, b_, k_ in hps):
                hp_hold_skipped_dec.append(round(nx_, 3))
                continue
            it[3] = e_
            hp_held_end.append([round(nx_, 3), round(e_, 3)])
    # mvt1 c01 (B #1): a subito mark to a softer level ends every dB gain at once (no hold or release across it)
    sub_q = sorted({q_ for s_ in staves for q_ in SUBITO[s_]})
    sfp_q = sorted({round(mq, 3) for mq, d_ in marks if d_ == "sfp"}) if HP_SUBITO_SFP_DELAY_S is not None else []
    for it in vol_parts:
        if it[0] != "hpgain" or it[4] <= 0:
            continue
        for sq_ in sorted(set(sub_q) | set(sfp_q)):
            if it[2] - 0.05 <= sq_ <= max(it[3], it[7]) + it[6] + EPS and base(sq_ + 0.01) < base(sq_ - 0.05):
                if sq_ in sfp_q:   # scherzo c18 (see HP_SUBITO_SFP_DELAY_S)
                    h_ = sec_to_qn(qn_to_sec(sq_) + HP_SUBITO_SFP_DELAY_S)
                    e_ = sec_to_qn(qn_to_sec(h_) + HP_SUBITO_SFP_REL_S)
                    if it[3] >= sq_ - EPS or sq_ - it[2] <= HP_HOLD_CAP + EPS:   # held through the sf
                        it[3], it[6] = h_, e_ - h_
                    else:   # already releasing: the release ends with the sfp's fall
                        it[6] = min(it[6], max(0.05, e_ - it[3]))
                    it[7] = 0.0
                    break
                it[3], it[6], it[7] = min(it[3], sq_ - 0.001), 0.001, 0.0
                break
    # c06 (C #5): the long-note swell in dB (same notes as the CC11 swell)
    for a, b2, k in contours:
        if k.startswith("swell") and k != "swell_sost":
            vol_add("shape:swell", ("swell_db", a, b2, k == "swell_taper"))
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

    def next_note(n):
        """scherzo c15: the note that follows n within 0.1 qn of its score end (the earliest moved onset), or None"""
        e_ = orig_end[id(n)]
        nx_ = [o for o in ns if o is not n and -EPS < o["qn"] - e_ < 0.1 and o["qn"] > n["qn"] + EPS]
        return min(nx_, key=new_on) if nx_ else None

    def snd_end(o):
        """scherzo c15: where o's MIDI note ends after the leads (a note joined into a moved legato target ends
        LEG_OVERLAP after the target's moved onset)"""
        e_ = o["end"]
        for t_ in ns:
            if t_.get("leg_prev") is o and id(t_) in shift and abs(e_ - (t_["qn"] + LEG_OVERLAP)) < 0.01:
                e_ = new_on(t_) + LEG_OVERLAP
        return e_

    def join_ramp(e_prev, m_, k_, r_s, c_s, g_s=0.06):
        """scherzo c15 (critic A #3, C's rule): where a level step into a note stands. m_ its moved onset, k_ its score
        onset, e_prev the MIDI end of the note before (None = after a rest). The note before ended g_s or more before
        m_: the ramp ends at m_. Otherwise it still sounds (an overlap, or a wind legato's gap of a few ms: the
        transition sample carries the old pitch to about the score onset; Clarinet 1's MIDI ends 11 ms before the
        next note-on): the ramp is centred c_s after the score onset."""
        r_ = r_s * bpm_at(k_) / 60.0
        if e_prev is None or m_ - e_prev >= g_s * bpm_at(k_) / 60.0:
            x0_ = m_ - r_ if e_prev is None else max(e_prev, m_ - r_)
            return (min(x0_, m_ - 0.004), m_)
        c_ = k_ + c_s * bpm_at(k_) / 60.0
        return (c_ - r_ / 2, c_ + r_ / 2)

    def step_join(n, prev=None):
        """scherzo c15: TRIM_STEP_S ramp (from qn, to qn) of a level step into note n (prev: the note before, when known)"""
        m_ = min(new_on(o) for o in ns if abs(o["qn"] - n["qn"]) < EPS)
        if prev is None:
            pv_ = [o for o in ns if o["qn"] < n["qn"] - EPS and snd_end(o) > m_ - 0.1]
            prev = max(pv_, key=snd_end) if pv_ else None
        if prev is None:
            return (qn_before(m_, TRIM_STEP_S["pre_s"][0]), qn_before(m_, TRIM_STEP_S["pre_s"][1]))
        return join_ramp(snd_end(prev), m_, n["qn"], TRIM_STEP_S["ramp_s"],
                         TRIM_STEP_S.get("center_by", {}).get(tname, TRIM_STEP_S["center_s"]))

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

    def trim_shape(n, dbv, ramp, early=None, tgt_trim=None, step=False):
        """c09 (A #2): the dB shape of a note trim. A joined note's trim starts at its moved onset (crossfading in over
        [moved - 0.05, moved + 0.03]); a trim on a note that another note follows ends over [next moved onset - 0.05,
        + 0.03], so the next note's (early) legato transition no longer plays under it.
        mvt1 c39 (critic A #2): LEG_JOIN_TRIM_HOLD moves the end of a positive trim on a note joined into a legato target
        past the transition (tgt_trim(o): the target's own trim in the same table)."""
        q0, e = n["qn"], orig_end[id(n)]
        if TRIM_STEP_S and (ramp == 0.25 or step) and early is None:   # scherzo c15 (see the default)
            a0, a1 = step_join(n)
            nx_ = next_note(n)
            z0, z1 = step_join(nx_, n) if nx_ is not None else (e, e + 0.1)
            if a1 > z0:
                z0, z1 = a1 + 0.002, max(z1, a1 + 0.004)
            return [(a0, 0.0), (a1, dbv), (z0, dbv), (z1, 0.0)]
        if joined_in(n) and ramp == 0.25:
            # pitch trims only: from the moved onset over 0.25 qn. Note trims keep their 0.6 s ramp from the score onset:
            # a fast -8 dB step at the moved onset (first c09 render) deepened the transition sag at Ob1 190 (3.0 ->
            # 9.4 dB), CA 152 (3.9 -> 9.7) and Fl1 254 (4.8 -> 7.9)
            m = new_on(n)
            # scherzo c12 (mvt2 c50, critic A #2): on the tracks in PITCH_TRIM_MIRROR a positive pitch trim on a legato
            # target starts with the mirror of the previous note's release ramp [m - 0.05, m + 0.03]; with the 0.25 qn
            # ramp the level dropped during the transition and the join read 60-100 ms late there
            a0, a1 = (m - 0.05, m + 0.03) if (tname in PITCH_TRIM_MIRROR and dbv is not None and dbv > 0
                                              and n.get("leg_target")) else (m, m + 0.25)
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
                ht_ = next((v_ for k_, v_ in LEG_JOIN_TRIM_HOLD_TO_AT.get(tname, {}).items() if abs(t_["qn"] - k_) < 0.02), None)
                if ht_ is not None:   # scherzo c11
                    z0 = max(z0, sec_qn(t_["qn"], -ht_))
                    z1 = max(z1, z0 + 0.002)
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
        if ("izz" in art_ or n.get("rep_sus") or n.get("rep_stac") or n.get("short_stroke")) and not isinstance(v_, dict):
            # mvt1 c04: repeated strokes (REP_SPLIT) too: the 0.25 qn ramp on each eighth/triplet made a 3 dB sawtooth
            # c12 (A #1): a pizz. trim is a step at full value on the attack (the 0.25 qn ramp from the moved onset,
            # sampled on the 0.125 qn grid, reached full depth just before the next note: F4 -8 sat at -1.8..-2.5 dB on
            # its attack and cut the following note instead); held to the next onset (at most 1.5 s), exact breakpoints
            q0 = new_on(n)
            nx_ = [new_on(o) for o in ns if o["qn"] > n["qn"] + EPS]
            ne_ = min(min(nx_) if nx_ else 1e9, sec_qn(n["qn"], 1.5))
            vol_add("level:pitch_trim", ("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
                                      (max(qn_before(q0, 0.01) + 0.002, qn_before(ne_, 0.03)), v_),
                                      (max(qn_before(q0, 0.01) + 0.004, qn_before(ne_, 0.01)), 0.0)], True))
        elif isinstance(v_, dict):   # c08 (A #1): {"early", "body"}: the sample's early sag is not cut with the body
            vol_add("level:pitch_trim_eb", ("env", trim_shape(n, None, 0.25, (v_["early"], v_["body"]), tgt_trim=ptrim_of)))
        else:
            vol_add("level:pitch_trim", ("env", trim_shape(n, v_, 0.25, tgt_trim=ptrim_of)))
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
                if not art_.endswith(("Lng", "Sht")) or n.get("tie_stroke") or base(q_) < mtab_.get("min_cc", DYN["f"]) - EPS:
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
            vol_add("level:metric_db", ("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
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
            vol_add("shape:sostenuto", ("env", [(a, 0.0), (x40, 0.0), (nm_ - 0.25, SOST_SUSTAIN_DB),
                                      (max(nm_ + 0.25, na_ + 0.25), SOST_SUSTAIN_DB),
                                      (max(nx40, na_ + 0.26, nm_ + 0.26), 0.0)]))
            sost_held.append(round(b2, 3))
        elif nm_ - 0.25 > x40 + 0.01:
            vol_add("shape:sostenuto", ("env", [(a, 0.0), (x40, 0.0), (nm_ - 0.25, SOST_SUSTAIN_DB), (nm_, 0.0)]))
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
        vol_add("shape:bump", ("env", ps_, True))
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
                vol_add("shape:timp_restrike", ("env", [(cq_, 0.0), (sec_to_qn(tc_ + d0_), TIMP_ROLL_RESTRIKE["dip_db"]),
                                          (sec_to_qn(tc_ + d1_), TIMP_ROLL_RESTRIKE["dip_db"]), (sec_to_qn(tc_ + d2_), 0.0)], True))
    # mvt1 c05 (critic C #2): a dip over each staggered-breath re-entry (BREATH_SPLIT_AT; the split is at the output stage)
    for sq_k, pts_ in BREATH_SPLIT_AT.get(tname, {}).items():
        if not any(abs(n["qn"] - sq_k) < 0.02 for n in ns):
            if tname in TRACK_WINDOWS and not tw_keep(tname, sq_k):
                continue   # mvt1 c39: the note plays on another track (TRACK_WINDOWS / ALIAS_TRACKS)
            raise SystemExit(f"BREATH_SPLIT_AT {tname} {sq_k}: no note there")
        for p_ in pts_:
            tp_ = qn_to_sec(p_)
            vol_add("shape:breath", ("env", [(qn_before(p_, 0.02), 0.0), (sec_to_qn(tp_ + 0.03), BREATH_SPLIT["dip_db"]),
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
        vol_add("shape:loop_fill", ("env", ps_, True))
        loop_n += 1
    # c26: re-bow fills (REBOW_FILLS): each list runs from its re-bow to the next one (exact breakpoints, seconds on the
    # real tempo map); its last value holds until the next list starts, and after the last re-bow to the release
    rbf_ = sorted((float(k), v) for k, v in REBOW_FILLS.get(tname, {}).items() if not k.startswith("_"))
    rebow_fill_ends = []   # mvt1 c45: [re-bow qn, hold end qn, last dB] for lists ended at their note's end
    for i_, (p_, pts_) in enumerate(rbf_):
        ps_ = [(sec_to_qn(qn_to_sec(p_) + t_), d_) for t_, d_ in pts_]
        # mvt1 c02: up to the next list's first point (fit_rebows.py now starts a list PRE_FILL_S before its re-bow)
        e_ = sec_to_qn(qn_to_sec(rbf_[i_ + 1][0]) + min(-0.04, rbf_[i_ + 1][1][0][0])) if i_ + 1 < len(rbf_) else END + 0.5
        # mvt1 c45 (critic B #1): a list never holds into a later note. When a note of this track starts after the end
        # of the note the re-bow belongs to and before e_, the last value holds to that note's end and is gone
        # REBOW_FILL_END_S later (c44: two lists at qn 576 held +4.1 / -2.0 dB over 26-29 bars of later notes)
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
        vol_add("shape:rebow_fill", ("env", ps_, True))
    # c18 (C #3a): JOIN_NOTCH: a dB notch over a moved legato join's transition peak, (from qn, to qn, dB) with 0.04 qn
    # ramps, exact breakpoints
    for a_, b_, d_ in JOIN_NOTCH.get(tname, []):
        vol_add("shape:join_notch", ("env", [(a_ - 0.04, 0.0), (a_, d_), (b_, d_), (b_ + 0.04, 0.0)], True))
    for k_, (a_, b_, d_) in sorted(JOIN_NOTCH_S.get(tname, {}).items()):   # scherzo c14 (see the default)
        n_ = next((o for o in ns if abs(o["qn"] - float(k_)) < 0.02), None)
        if n_ is None:
            print(f"  WARNING {tname}: JOIN_NOTCH_S {k_} has no note", file=sys.stderr)
            continue
        t0_ = qn_to_sec(new_on(n_))
        vol_add("shape:join_notch", ("env", [(sec_to_qn(t0_ + a_ - JOIN_NOTCH_RAMP_S), 0.0), (sec_to_qn(t0_ + a_), float(d_)),
                                  (sec_to_qn(t0_ + b_), float(d_)), (sec_to_qn(t0_ + b_ + JOIN_NOTCH_RAMP_S), 0.0)], True))
    # mvt1 c06 (C #2): explicit level shapes from the config (per track and "_all")
    for ps_ in LEVEL_SHAPES.get(tname, []) + LEVEL_SHAPES.get("_all", []):
        lv_ = {round(float(d_), 2) for _, d_ in ps_ if abs(float(d_)) > 1e-6}
        slow_ = LEVEL_ROW_SLOW_QN is not None and len(lv_) == 1 and float(ps_[-1][0]) - float(ps_[0][0]) >= LEVEL_ROW_SLOW_QN - EPS
        vol_add("slow:level_row" if slow_ else "level:level_shape", ("env", [(float(x_), float(d_)) for x_, d_ in ps_], True))
    for ps_ in cc11_park_env:   # mvt1 c51: SHORT_CC11_PARK level return and metric steps (exact breakpoints)
        vol_add("level:park_return", ("env", ps_, True))
    for ps_ in beat_db_env:   # scherzo c15: the metric steps are a shape layer of their own
        vol_add("shape:beat_db", ("env", ps_, True))
    # mvt1 c24: LEVEL_SHAPES_S (seconds around a score onset, converted on the real tempo map)
    for q0_, ps_ in LEVEL_SHAPES_S.get(tname, []):
        t0_ = qn_to_sec(float(q0_))
        vol_add("level:level_shape", ("env", [(sec_to_qn(t0_ + float(x_)), float(d_)) for x_, d_ in ps_], True))
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
        vol_add("shape:cresc_front", ("env", [(sec_to_qn(t0_ + x_), d_) for x_, d_ in ps_], True))
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
            if hit_:
                hits_.append(f"{nm_} {r_[0]:.2f} (target {hit_[2]:g}, moved {hit_[0]:.2f})")
        if hits_:
            print(f"  WARN {tname}: {len(hits_)} level rows ramp inside a led legato transition: " + "; ".join(hits_),
                  file=sys.stderr)
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
            vol_add("level:pickup", ("env", [(a_ - 0.012, 0.0), (a_ - 0.002, pdb_), (b_ - 0.012, pdb_), (b_ - 0.002, 0.0)], True))
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
            vol_add("level:pickup", ("env", [(a_ - 0.01, 0.0), (a_, d_), (sec_qn(b_, tail_[0]), d_),
                                      (sec_qn(b_, tail_[0] + tail_[1]), 0.0)], True))
        else:
            vol_add("level:pickup", ("env", [(a_ - 0.01, 0.0), (a_, d_), (b_, d_), (b_ + 0.02, 0.0)], True))
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
            vol_add("shape:synco", ("env", pts_, True))
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
            vol_add("shape:release", ("env", [(a_, 0.0), (b_, db_), (stop_ - 0.03, db_), (stop_, 0.0)], True))
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
                vol_add("shape:wind_detach", ("env", pts_, True))
                detach_dips.append(round(n["qn"], 3))
    # mvt1 c22 (critic A #1): STR_REP_DETACH dips before each eighth of a listed string pedal
    str_rep_dips = []
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
                vol_add("shape:rep_detach", ("env", [(sec_to_qn(tb_ - x_ - r_), 0.0), (sec_to_qn(tb_ - x_), d_),
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
            vol_add("level:meas_trem", ("env", [(a_ - 0.012, 0.0), (a_ - 0.002, MEAS_TREM["alt_db"]),
                                      (b_ - 0.012, MEAS_TREM["alt_db"]), (b_ - 0.002, 0.0)], True))
    # mvt1 c15 (critic C #5): a delayed unison copy fades in under the kept note
    uni_fades = []
    if UNI_DELAY_FADE:
        for n in ns:
            dl_ = UNI_DELAY.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
            if dl_ is None:
                continue
            q1_ = max(new_on(n), dl_)
            vol_add("shape:uni_fade", ("env", [(q1_ - 0.01, 0.0), (q1_, UNI_DELAY_FADE[0]),
                                      (sec_to_qn(qn_to_sec(q1_) + UNI_DELAY_FADE[1]), 0.0)], True))
            uni_fades.append(round(q1_, 3))
    # mvt1 c06 (C #1): arrival weight on the tracks that start a note on the arrival
    arr_w, arr_w_skipped = [], []
    if family in ("wind", "brass", "string"):
        for qa_, aw_ in sorted(ARRIVAL_WEIGHT_AT.items()):
            pre_, db_ = aw_[0], aw_[1]
            pq_ = aw_[2] if len(aw_) > 2 else 4.0   # mvt1 c08 (critic C #1): the hold-back's length in qn (default 4)
            if not any(abs(n["qn"] - qa_) < 0.05 for n in ns):
                continue
            if ARRIVAL_WEIGHT_RISE_ONLY and not base(qa_ + 0.01) > base(qa_ - pq_) + EPS:   # scherzo c25 (see the default)
                arr_w_skipped.append(qa_)
                continue
            if ARRIVAL_WEIGHT_MOVED:   # scherzo c24 (see the default)
                na_ = [n for n in ns if abs(n["qn"] - qa_) < 0.05]
                mo_ = min(n["qn"] - shift.get(id(n), 0.0) for n in na_)
                me_ = max(orig_end.get(id(n), n.get("end", n["qn"])) for n in na_)
                if ARRIVAL_WEIGHT_HOLD_CAP is not None:   # scherzo c25
                    me_ = min(me_, qa_ + ARRIVAL_WEIGHT_HOLD_CAP)
                r0_ = min(qa_ - 0.1, sec_qn(mo_, -0.03))
                vol_add("slow:arrival", ("env", [(qa_ - pq_, 0.0), (r0_, pre_), (sec_qn(mo_, -0.005), db_),
                                          (max(qa_ + 0.5, me_), db_), (max(qa_ + 0.5, me_) + ARRIVAL_WEIGHT_MOVED, 0.0)], True))
            else:
                vol_add("slow:arrival", ("env", [(qa_ - pq_, 0.0), (qa_ - 0.1, pre_), (sec_qn(qa_, 0.05), db_), (qa_ + 0.5, db_),
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
                vol_add("shape:tenuto", ("env", [(t1_, 0.0), (sec_qn(q0, 0.12), TENUTO_SWELL_DB),
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
            vol_add("level:contour", ("env", pts_, True))
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
                if ov is not None and ACCENT_SWELL_MAX_DB is not None and gentle_:
                    ov = min(ov, ACCENT_SWELL_MAX_DB)   # scherzo c15
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
            vol_add("shape:marc_body", ("env", [(q0 - 0.01, 0.0), (q0 + 0.01 * bpm_at(q0) / 60, MARC_BODY_DB),
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
            vol_add("level:note_trim", ("env", [(qn_before(q0, 0.03), 0.0), (qn_before(q0, 0.01), v_),
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
            # scherzo c15: a note trim listed with a ramp of 0.05 s or less is a step: placed like the pitch trims
            vol_add("level:note_trim", ("env", trim_shape(n, hit[0], ramp,   # c09 (A #2): ends at the next moved onset
                                                tgt_trim=lambda o: next((v_ for k_, v_ in nt.items() if abs(o["qn"] - k_) < 0.02), 0.0),
                                                step=rs_ <= 0.05 + 1e-9)))
    # mvt1 c07 (critic A #1): ROW_TRIM_DB. In a line that mixes rows, loud Sus MAX / Stac notes sat 2-6 dB over the Leg
    # rows at the same CC11 (Violins II +4.7, Violas +5.6 median), so accented Leg notes sat under the Sus eighths after
    # them. Consecutive trimmed notes are one step (no bump at each join); accented notes on the row are trimmed too
    # (their swell stays on top), so an accent keeps its relation to the Sus notes around it
    row_trimmed = []
    rtab_ = ROW_TRIM_DB.get(tname, {}) if (family == "string" or (family == "wind" and ROW_TRIM_WINDS)) else {}
    if rtab_:
        segs_ = []
        for n in sorted(ns, key=lambda o: o["qn"]):
            a_ = n.get("art") or ""
            if a_ not in rtab_ or (n.get("down_stroke") and not n.get("rep_stroke")) or n.get("rep_sus") or n.get("rep_stac") \
                    or any(a0_ - EPS <= n["qn"] < b0_ for a0_, b0_ in ROW_TRIM_SKIP.get(tname, [])) \
                    or any(o is not n and abs(o["qn"] - n["qn"]) < 0.01 for o in ns) or final(n["qn"]) < rtab_[a_][1] \
                    or (AUTO_REBOW and qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"]) > REBOW_MAX_S) \
                    or (family == "string" and not any(o is not n and _lg((o.get("art") or ""))
                               and max(o["qn"] - orig_end[id(n)], n["qn"] - orig_end[id(o)]) <= ROW_TRIM_NEAR_QN + EPS
                               for o in ns)):
                continue
            s0_ = new_on(n)
            nm_ = next_moved(n)
            s1_ = nm_ if nm_ is not None else orig_end[id(n)]
            if ROW_TRIM_HOLD_QN and nm_ is None:   # scherzo c15: hold to the next note of the run
                nx_ = [o for o in ns if o["qn"] > n["qn"] + EPS and o["qn"] - orig_end[id(n)] <= ROW_TRIM_HOLD_QN + EPS]
                if nx_:
                    s1_ = max(s1_, min(new_on(o) for o in nx_))
            if segs_ and abs(segs_[-1][2] - rtab_[a_][0]) < 1e-6 and s0_ <= segs_[-1][1] + 0.06:
                segs_[-1][1] = max(segs_[-1][1], s1_)
                segs_[-1][4] = n
            else:
                segs_.append([s0_, s1_, rtab_[a_][0], n, n])
            row_trimmed.append(round(n["qn"], 3))
        for s0_, s1_, d_, nf_, nl_ in segs_:
            if TRIM_STEP_S:   # scherzo c15: flat, the steps placed by step_join (see TRIM_STEP_S)
                a0_, a1_ = step_join(nf_)
                nx_ = [o for o in ns if o["qn"] > nl_["qn"] + EPS and abs(new_on(o) - s1_) < 0.002]
                z0_, z1_ = step_join(nx_[0], nl_) if nx_ else (s1_ - 0.05, s1_ + 0.03)
                if a1_ > z0_:
                    z0_, z1_ = a1_ + 0.002, max(z1_, a1_ + 0.004)
                vol_add("level:row_trim", ("env", [(a0_, 0.0), (a1_, d_), (z0_, d_), (z1_, 0.0)], True))
                continue
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
    ub_runs_ = []
    for n in sorted(ns, key=lambda o: o["qn"]):   # c04 (A #2): the kept note of a same-patch unison
        b_ = UNI_BOOST.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if b_ and UNI_BOOST_AS_ROLE:   # scherzo c15 (see the default)
            if ub_runs_ and (UNI_RUN_MERGE_VALUES or abs(ub_runs_[-1][2] - b_) < 0.01) \
                    and n["qn"] - ub_runs_[-1][1] < UNI_RUN_GAP_QN:
                ub_runs_[-1][1] = max(ub_runs_[-1][1], orig_end[id(n)])
                ub_runs_[-1][3][b_] = ub_runs_[-1][3].get(b_, 0.0) + orig_end[id(n)] - n["qn"]
            else:
                ub_runs_.append([n["qn"], orig_end[id(n)], b_, {b_: orig_end[id(n)] - n["qn"]}])
        elif b_:
            vol_add("level:uni_boost", ("note", n["qn"], orig_end[id(n)], b_, 0.02))
    # scherzo c30: a merged run takes the boost its notes hold longest (one span per unison phrase)
    ub_runs_ = [[a_, b2_, max(w_.items(), key=lambda kv: (kv[1], -kv[0]))[0]] for a_, b2_, d_, w_ in ub_runs_]
    if __import__("os").environ.get("STP_DEBUG_UB") == tname:
        print("DEBUG ub_runs", tname, ub_runs_, file=sys.stderr)
    for a_, b2_, d_ in ub_runs_:
        if UNI_BOOST_ROLE_IN_RESTS:
            # scherzo c27 (critic B #4.1): the span's edges in rests: in at the run's first moved note-on (from the end
            # of the note before it, at most 0.5 qn earlier), out in the first rest of 0.25 qn or more after the run
            n0_ = [o for o in ns if abs(o["qn"] - a_) < EPS]
            on_ = min([o["qn"] - shift.get(id(o), 0.0) for o in n0_] + [a_])
            pe_ = max([orig_end[id(o)] for o in ns if o["qn"] < a_ - EPS and orig_end[id(o)] <= on_ + EPS], default=on_ - 0.5)
            i0_ = max(on_ - 0.5, min(pe_, on_ - 0.03))
            # out: in a rest of 0.25 qn or more that starts within 6 qn after the run; otherwise a step at the next
            # note's moved note-on (the notes after the run are not doubled)
            nx_u_ = sorted((o["qn"], o["qn"] - shift.get(id(o), 0.0), orig_end[id(o)]) for o in ns if o["qn"] > b2_ - 0.5 and o["qn"] >= a_ + EPS
                           and not any(o["qn"] - EPS <= x_ <= b2_ for x_ in [o["qn"]] if UNI_BOOST.get(tname, {}).get((round(o["qn"], 3), o["pitch"]))))
            r0_ = b2_
            for s_, m_, e_ in nx_u_:
                if s_ > r0_ + 0.25 - EPS or s_ > b2_ + 6.0:
                    break
                r0_ = max(r0_, e_)
            if r0_ <= b2_ + 6.0 + EPS:
                nxt_ = min([m_ for s_, m_, e_ in nx_u_ if s_ > r0_ - EPS] + [r0_ + 0.6])
                pts_ = [(r0_ + 0.02, d_), (max(r0_ + 0.04, min(r0_ + 0.5, nxt_ - 0.05)), 0.0)]
            else:
                m0_ = min([m_ for s_, m_, e_ in nx_u_ if s_ >= b2_ - EPS] + [b2_])
                pts_ = [(m0_ - 0.03, d_), (m0_ - 0.005, 0.0)]
            vol_add("slow:uni_role", ("env", [(i0_, 0.0), (on_ - 0.02, d_)] + pts_))
            continue
        vol_add("slow:uni_role", ("env", [(a_ - 0.5, 0.0), (a_ - 0.1, d_), (b2_, d_), (b2_ + 0.5, 0.0)]))
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
            vol_add("level:chord", ("chord",))

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
    # scherzo c15: ONE_LEVEL (see the default)
    ol_chains, ol_notes = [], 0
    q_items_, rest_items_ = [], list(vol_parts)

    def vol_of(items, q):
        saved_ = vol_parts[:]
        vol_parts[:] = items
        try:
            return vol(q)
        finally:
            vol_parts[:] = saved_
    if ONE_LEVEL and ns:
        OL_ = ONE_LEVEL
        q_items_ = [it for it in vol_parts if vol_tags.get(id(it)) in set(OL_["tags"])]
        rest_items_ = [it for it in vol_parts if vol_tags.get(id(it)) not in set(OL_["tags"])]
        qe_ = sorted([it for it in q_items_ if it[0] == "env"], key=lambda it: it[1][0][0])
        qo_ = [it for it in q_items_ if it[0] != "env"]
        qe_a_ = [it[1][0][0] for it in qe_]
        qe_len_ = max([it[1][-1][0] - it[1][0][0] for it in qe_], default=0.0)

        def q_at(q):   # the built sum of the ONE_LEVEL layers at q
            i0_, i1_ = bisect.bisect_left(qe_a_, q - qe_len_ - 1e-6), bisect.bisect_right(qe_a_, q + 1e-6)
            return vol_of(qe_[i0_:i1_] + qo_, q)
        grp_ = {}
        for n in ns:
            if not n.get("grace"):
                grp_.setdefault(round(n["qn"], 3), []).append(n)
        G_ = []
        for k_, g_ in sorted(grp_.items()):
            G_.append({"k": k_, "m": min(new_on(o) for o in g_), "e": max(snd_end(o) for o in g_), "g": g_})
        for i_, x_ in enumerate(G_):
            slot_ = G_[i_ + 1]["k"] - x_["k"] if i_ + 1 < len(G_) else 1e9
            x_["short"] = bool(q_items_) and min(x_["e"] - x_["m"], slot_) <= OL_["max_qn"] + EPS
            if x_["short"]:
                d_ = x_["e"] - x_["m"]
                x_["v"] = round(sum(q_at(x_["m"] + f_ * d_) for f_ in (0.2, 0.4, 0.6)) / 3.0, 2)
                ol_notes += 1
        r_s_, c_s_ = OL_["ramp_s"], OL_["leg_center_s"]
        cur_ = None
        for i_, x_ in enumerate(G_ + [None]):
            pv_ = G_[i_ - 1] if i_ else None
            conn_ = x_ is not None and pv_ is not None and x_["m"] - pv_["e"] < OL_["gap_qn"]
            if cur_ is not None and not (conn_ and x_["short"]):
                # close the chain after its last short note pv_: into a connected longer note, or after a tail
                if conn_:
                    z0_, z1_ = join_ramp(pv_["e"], x_["m"], x_["k"], r_s_, c_s_)
                else:
                    z0_ = sec_qn(pv_["e"], OL_["tail_s"])
                    if x_ is not None:
                        z0_ = min(z0_, x_["m"] - 0.07 - 2 * r_s_ * bpm_at(x_["m"]) / 60.0)
                    z1_ = z0_ + r_s_ * bpm_at(pv_["e"]) / 60.0
                z0_ = max(z0_, cur_[-1][0] + 0.002)
                z1_ = max(z1_, z0_ + 0.002)
                cur_ += [(z0_, pv_["v"]), (z1_, round(q_at(z1_), 2))]
                ol_chains.append(cur_)
                cur_ = None
            if x_ is None or not x_["short"]:
                continue
            x0_, x1_ = join_ramp(pv_["e"] if conn_ else None, x_["m"], x_["k"], r_s_, c_s_)
            if cur_ is not None:
                x0_ = max(x0_, cur_[-1][0] + 0.002)
                cur_ += [(x0_, pv_["v"]), (max(x1_, x0_ + 0.002), x_["v"])]
            else:
                xl_ = min(x0_, x_["m"] - 0.06) - 0.002
                if ol_chains and xl_ < ol_chains[-1][-1][0] + 0.002:
                    xl_ = ol_chains[-1][-1][0] + 0.002
                    x0_ = max(x0_, xl_ + 0.002)
                vl_ = round(q_at(xl_), 2)
                cur_ = [(xl_, vl_), (x0_, vl_), (max(x1_, x0_ + 0.002), x_["v"])]
        ol_chains = [[(round(a_, 4), b_) for a_, b_ in c_] for c_ in ol_chains]
    ol_starts_ = [c_[0][0] for c_ in ol_chains]

    def ol_at(q):   # the chain's value at q, or None outside the chains
        j_ = bisect.bisect_right(ol_starts_, q + 1e-9) - 1
        if j_ >= 0 and ol_chains[j_][0][0] <= q < ol_chains[j_][-1][0]:
            return value_at(ol_chains[j_], q)
        return None
    vbreaks = [0.0, SE - 1, SE - 0.5, SE] + [x_ for c_ in ol_chains for x_, _ in c_]
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
    # scherzo c15 (critic B #2): VOL_GRID_QN (0.25 was the grid; build_reaper.py samples on 0.125, so every slow ramp was
    # written as stairs of 0.25 qn; on 0.125 the written envelope is the ramp itself and the simplification pass in
    # build_reaper.py removes its collinear points)
    vgrid = sorted(set([round(x, 4) for x in vbreaks] + [round(i * VOL_GRID_QN, 4) for i in range(int((END + 4) / VOL_GRID_QN))]))
    # c10: "env" items flagged exact put their breakpoints into parts.json vol_bp; build_reaper.py adds them to the volume
    # envelope's 0.125 qn grid, so shapes faster than the grid (pre-onset fills, the timpani attack) are written as built
    keep_tags_ = set(VOL_KEEP_TAGS) | {x_ for x_ in __import__("os").environ.get("STP_KEEP_TAGS", "").split(",") if x_}

    def vol_kept(it):   # scherzo c15: is this item written into vol_db (VOL_CLASSES / VOL_KEEP_TAGS)?
        t_ = vol_tags.get(id(it), "slow:untagged")
        return VOL_CLASSES is None or t_.split(":")[0] in VOL_CLASSES or t_ in keep_tags_
    vol_bp = sorted({round(x, 4) for item in vol_parts if item[0] == "env" and len(item) > 2 and item[2] and vol_kept(item)
                     for x, _ in item[1]})
    # mvt1 c42: POST_SHAPES_S (see the default), converted on the real tempo map
    vol_post = []
    for q0_, ps_ in POST_SHAPES_S.get(tname, []):
        t0_ = qn_to_sec(float(q0_))
        vol_post.append([[round(sec_to_qn(t0_ + float(x_)), 4), float(d_)] for x_, d_ in ps_])
    vol_bp = sorted(set(vol_bp) | {p_[0] for sh_ in vol_post for p_ in sh_}
                    | ({x_ for c_ in ol_chains for x_, _ in c_} if VOL_CLASSES is None or "level" in VOL_CLASSES else set()))
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
    # scherzo c15: the lanes are summed per item over the item's own support (the old loop evaluated every item at
    # every grid point), once per class; inside a ONE_LEVEL chain the chain replaces the built sum of its layers and
    # counts as class "level". parts.json: `vol_db` (the sum, as before), `vol_cls` (the three class lanes; step lanes
    # like vol_db), `vol_tags` (items per layer). STP_LAYERS=1 also writes one lane per layer as built (`vol_layers`)
    def lane_of(items):
        acc = [0.0] * len(vgrid)
        for it in items:
            if it[0] == "env":
                ps = it[1]
                for i_ in range(bisect.bisect_left(vgrid, ps[0][0] - 1e-6), bisect.bisect_left(vgrid, ps[-1][0] + 1e-6)):
                    if ps[0][0] <= vgrid[i_] < ps[-1][0]:
                        acc[i_] += value_at(ps, vgrid[i_])
            else:
                saved_ = vol_parts[:]
                vol_parts[:] = [it]
                for i_, q in enumerate(vgrid):
                    acc[i_] += vol(q)
                vol_parts[:] = saved_
        return acc
    cls_of_ = lambda it: vol_tags.get(id(it), "slow:untagged").split(":")[0]
    in_q_ = {id(it) for it in q_items_}
    lanes_ = {c_: lane_of([it for it in vol_parts if cls_of_(it) == c_ and id(it) not in in_q_]) for c_ in ("slow", "level", "shape")}
    lq_ = {c_: lane_of([it for it in q_items_ if cls_of_(it) == c_]) for c_ in ("slow", "level", "shape")} if q_items_ else {}
    for i_, q in enumerate(vgrid):
        cv_ = ol_at(q) if ol_chains else None
        for c_ in lq_:
            lanes_[c_][i_] += lq_[c_][i_] if cv_ is None else (cv_ if c_ == "level" else 0.0)
    has_fade_ = ("fade",) in vol_parts
    ie_ = bisect.bisect_left(vgrid, round(END, 4))
    if has_fade_:   # c26: held at the release value from END on. The value at END - 0.001:
        for c_ in lanes_:
            ci_ = [it for it in vol_parts if cls_of_(it) == c_ and id(it) not in in_q_]
            cv_ = ol_at(END - 0.001) if ol_chains else None
            ve_ = vol_of(ci_, END - 0.001) + ((vol_of([it for it in q_items_ if cls_of_(it) == c_], END - 0.001) if cv_ is None
                                                else (cv_ if c_ == "level" else 0.0)) if q_items_ else 0.0)
            for i_ in range(ie_, len(vgrid)):
                lanes_[c_][i_] = ve_
    if VOL_CLASSES is None:
        wr_ = [lanes_["slow"][i_] + lanes_["level"][i_] + lanes_["shape"][i_] for i_ in range(len(vgrid))]
    else:
        wr_ = [sum(lanes_[c_][i_] for c_ in VOL_CLASSES) for i_ in range(len(vgrid))]
        kt_ = [it for it in vol_parts if cls_of_(it) not in VOL_CLASSES and vol_tags.get(id(it)) in keep_tags_]
        if kt_:
            lk_ = lane_of(kt_)
            wr_ = [a_ + b_ for a_, b_ in zip(wr_, lk_)]
    for i_, q in enumerate(vgrid):
        v = round(wr_[i_], 2)
        if v != last:
            vol_db.append((q, v)); last = v
    vol_cls, vol_tag_n, vol_layers = {}, {}, {}
    for it_ in vol_parts:
        vol_tag_n[vol_tags.get(id(it_), "slow:untagged")] = vol_tag_n.get(vol_tags.get(id(it_), "slow:untagged"), 0) + 1
    for c_ in ("slow", "level", "shape"):
        ln_, last = [], None
        for i_, q in enumerate(vgrid):
            v = round(lanes_[c_][i_], 2)
            if v != last:
                ln_.append((q, v)); last = v
        vol_cls[c_] = ln_
    if __import__("os").environ.get("STP_LAYERS"):
        for t_ in sorted(vol_tag_n):
            la_ = lane_of([it for it in vol_parts if vol_tags.get(id(it), "slow:untagged") == t_])
            ln_, last = [], None
            for i_, q in enumerate(vgrid):
                v = round(la_[i_], 2)
                if v != last:
                    ln_.append((q, v)); last = v
            vol_layers[t_] = ln_
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
    rr_reset = sorted({round(max(0.0, min([new_on(n) for n in ns if abs(n["qn"] - q_) < 0.01] or [q_]) - 0.03), 4)
                       for q_ in RR_RESET_AT.get(tname, [])})   # scherzo c07 (critic C #4)

    # c03: apply the note-start leads. A note that overlaps a moved legato target ends LEG_OVERLAP after its new onset;
    # keyswitches stay at least 0.03 qn before their (moved) note.
    out_notes = []
    wd_overlaps = []   # scherzo c18
    ov_ext = []   # scherzo c07 (ported from mvt3 c07): (note dict, dur now, dur with the LEG_OVERLAP_MIN_S floor)
    dropped = 0
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
                    want_ = min(on_ + ovf_ * bpm_at(on_) / 60.0, on_ + LEG_OVERLAP_MAX_FRAC * max(0.0, o["end"] - on_))
                    if want_ > e + EPS:
                        ov_to_ = want_
        if n.get("wd_overlap"):   # scherzo c18: WIND_DETACH "overlap_s", from the next note's moved note-on
            o_, s_ = n["wd_overlap"]
            on_ = new_on(o_)
            e = max(min(e, on_), sec_to_qn(qn_to_sec(on_) + s_)) if on_ > new_on(n) + EPS else e
            wd_overlaps.append(round(n["qn"], 3))
        q1 = new_on(n)
        dl_ = UNI_DELAY.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if dl_ is not None:   # c17 (B #6)
            q1 = max(q1, dl_)
        out_notes.append({"qn": round(q1, 4), "dur": round(max(0.02, e - q1), 4), "pitch": n["pitch"], "vel": n["vel"],
                          "sq": round(n["qn"], 4), "_art": n.get("rep_row") or n.get("art")})   # sq: score onset (analysis only); mvt1 c37: REP_ROW row
        if ov_to_ is not None:
            ov_ext.append((out_notes[-1], out_notes[-1]["dur"], round(max(0.02, ov_to_ - q1), 4)))
    if wd_overlaps:
        print(f"  {tname}: WIND_DETACH overlap on {len(wd_overlaps)} pitch changes", file=sys.stderr)
    # scherzo c23: STAC_MIN_SOUND_S (see the default)
    sms_ = STAC_MIN_SOUND_S.get(tname)
    if sms_:
        ons_ = sorted({a["qn"] for a in out_notes})
        sms_n = []
        for a in out_notes:
            if not any(w_ in (a["_art"] or "") for w_ in ("Stac", "Spic")):
                continue
            nx_ = next((o_ for o_ in ons_ if o_ > a["qn"] + 1e-3), None)
            want_ = sec_to_qn(qn_to_sec(a["qn"]) + sms_)
            if nx_ is not None:
                want_ = min(want_, sec_to_qn(qn_to_sec(nx_) - STAC_MIN_SOUND_GAP_S))
            if want_ > a["qn"] + a["dur"] + 1e-4:
                sms_n.append(round(a["sq"], 3))
                a["dur"] = round(want_ - a["qn"], 4)
        print(f"  {tname}: STAC_MIN_SOUND_S {sms_} s lengthened {len(sms_n)} short notes", file=sys.stderr)
    # scherzo c26 (critic A #1): SLUR_END_BEFORE_STAC (see the default)
    sbs_ = SLUR_END_BEFORE_STAC.get(tname)
    if sbs_:
        srt_ = sorted(out_notes, key=lambda a: a["qn"])
        sbs_n = []
        for i_, a in enumerate(srt_):
            if not any(w_ in (a["_art"] or "") for w_ in sbs_.get("rows", ("Leg",))) \
                    or not any(q0_ - EPS <= a["sq"] < q1_ for q0_, q1_ in sbs_["spans"]):
                continue
            nx_ = next((b for b in srt_[i_ + 1:] if b["qn"] > a["qn"] + 1e-3), None)
            if nx_ is None or nx_["pitch"] == a["pitch"] or "Stac" not in (nx_["_art"] or "") \
                    or nx_["qn"] > a["qn"] + a["dur"] + 0.1:
                continue
            want_ = sec_to_qn(qn_to_sec(nx_["qn"]) - sbs_["s"])
            if want_ < a["qn"] + a["dur"] - 1e-4 and want_ - a["qn"] >= sbs_.get("min_qn", 0.15):
                a["dur"] = round(want_ - a["qn"], 4)
                sbs_n.append(round(a["sq"], 3))
        print(f"  {tname}: SLUR_END_BEFORE_STAC {sbs_['s']} s on {len(sbs_n)} slur ends", file=sys.stderr)
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
    ksm_ = by_name(KS_MIN_LEAD_S) if KS_MIN_LEAD_S else None   # scherzo c13 (critic A #6; see the default)
    ks_early = 0
    for k_ in ks:
        nn = k_.pop("note")
        k_["qn"] = round(max(0.0, min(k_["qn"], new_on(nn) - 0.03)), 4)
        if nn.get("sost_rep"):   # c07 (A #1): the keyswitch just before the re-tongued note (the legato note it cuts
            k_["qn"] = round(new_on(nn) - 0.012, 4)   # ends 0.01 qn before it), so the break stays about 0.05 s
        elif ksm_ and new_on(nn) > 0.5:
            on_ = new_on(nn)
            # (c17: 1e-3, not EPS: the note's own rounded note-on could count as the previous one, which left the keyswitch
            # 0.03 qn before its note: three row-change joins of Violins II and two others after the lead-cap change)
            pon_ = max((a["qn"] for a in out_notes if a["qn"] < on_ - 1e-3), default=None)
            new_ = max(sec_to_qn(qn_to_sec(on_) - ksm_), 0.0 if pon_ is None else pon_ + 0.01)
            if new_ < k_["qn"] - 1e-4 and (_lg(k_["art"]) or not any(
                    a["_art"] and _lg(a["_art"]) and a["qn"] + EPS < new_ < a["qn"] + a["dur"] - EPS for a in out_notes)):
                k_["qn"] = round(new_, 4)
                ks_early += 1
    if ks_early:
        print(f"  {tname}: KS_MIN_LEAD_S {ksm_} s: {ks_early} of {len(ks)} keyswitches moved earlier", file=sys.stderr)
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
            a["dur"] = round(p_ - REBOW_GAP_QN - a["qn"], 4)
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
    # mvt1 c37 (critic A #4): TIMP_RH_ALT (see the default): alternate hands on repeated single strokes
    timp_rh, timp_lh_vel = [], []
    if family == "timp" and TIMP_RH_ALT:
        prev_, hand_ = None, 0
        strokes_ = []
        for a in sorted(out_notes, key=lambda a: a["qn"]):
            if not (a["_art"] or "").endswith(("Lng", "Sht")):
                continue
            if prev_ is not None and prev_["pitch"] == a["pitch"] and abs(a["qn"] - prev_["qn"]) > EPS \
                    and qn_to_sec(a["qn"]) - qn_to_sec(prev_["qn"]) <= TIMP_RH_ALT["max_gap_s"] + EPS:
                hand_ = 1 - hand_
            elif prev_ is None or abs(a["qn"] - prev_["qn"]) > EPS:
                hand_ = 0
            prev_ = dict(a)
            strokes_.append((a, hand_, a["pitch"]))
            if hand_ and a["pitch"] + TIMP_RH_ALT.get("add", 24) <= 81:
                a["pitch"] += TIMP_RH_ALT.get("add", 24)
                timp_rh.append(a["sq"])
        # scherzo c12 (critic A #1): "lh_vel_add": [(velocity at or below, steps added), ...]: the left-hand strokes
        # of an alternating run play softer samples than the right-hand strokes at the same velocity (B2 at v56-63:
        # 8 dB), so the stroke that opens each group was the weakest. A left-hand stroke next to a right-hand stroke
        # of its pitch (within max_gap_s) gets the steps of its velocity band; a stroke above the last band and a
        # single stroke outside a run keep their velocity
        for i_, (a, h_, bp_) in enumerate(strokes_):
            if h_ or not TIMP_RH_ALT.get("lh_vel_add"):
                continue
            nb_ = [strokes_[j_] for j_ in (i_ - 1, i_ + 1) if 0 <= j_ < len(strokes_)]
            if not any(o_[1] == 1 and o_[2] == bp_ and abs(qn_to_sec(o_[0]["qn"]) - qn_to_sec(a["qn"]))
                       <= TIMP_RH_ALT["max_gap_s"] + EPS for o_ in nb_):
                continue
            add_ = next((d_ for c_, d_ in TIMP_RH_ALT["lh_vel_add"] if a["vel"] <= c_), 0)
            if add_:
                timp_lh_vel.append((a["sq"], a["vel"], min(127, a["vel"] + add_)))
                a["vel"] = min(127, a["vel"] + add_)
    # scherzo c07: SHORT_BEAT_VEL (research batch 7): metric velocity on short rows
    bv_n_ = 0
    if SHORT_BEAT_VEL and family in SHORT_BEAT_VEL["families"]:
        BV_ = SHORT_BEAT_VEL
        rng_ = __import__("random").Random(f'{BV_.get("seed", 7)}{tname}')
        prev_ = None
        for a in sorted(out_notes, key=lambda o_: (o_["sq"], o_["pitch"])):
            art_ = a.get("_art") or ""
            if not any(art_.startswith(r_) for r_ in BV_["rows"]) or bpm_at(a["sq"]) < BV_.get("min_bpm", 0) \
                    or any(x_ - EPS <= a["sq"] < y_ for x_, y_ in BV_.get("skip", {}).get(tname, [])):
                prev_ = None
                continue
            pos_ = a["sq"] % BV_.get("meter_qn", 3.0)
            if abs(pos_) < 0.02 or abs(pos_ - BV_.get("meter_qn", 3.0)) < 0.02:
                d_ = BV_["beat1"]
            elif abs(pos_ - round(pos_)) < 0.02:
                d_ = BV_["beat"]
            else:
                d_ = BV_["off"]
            d_ += rng_.uniform(-BV_["rand"], BV_["rand"])
            v_ = max(1, min(127, int(round(a["vel"] + d_))))
            if prev_ is not None and prev_["pitch"] == a["pitch"] and 0 < a["sq"] - prev_["sq"] <= 0.55:
                v_ = max(v_, prev_["vel"] - BV_.get("pair_max", 5))
            if v_ != a["vel"]:
                a["vel"] = v_
                bv_n_ += 1
            prev_ = a
        if bv_n_:
            print(f"  {tname}: SHORT_BEAT_VEL on {bv_n_} notes", file=sys.stderr)
    # scherzo c07 (ported from mvt3 c07) (critic A #2): the legato overlap floors (LEG_OVERLAP_MIN_S), on notes whose end nothing changed since
    ov_n_ = 0
    for a_, d0_, d1_ in ov_ext:
        if abs(a_["dur"] - d0_) < 1e-4 and any(b_ is a_ for b_ in out_notes) and not any(
                b_ is not a_ and b_["pitch"] == a_["pitch"] and a_["qn"] < b_["qn"] < a_["qn"] + d1_ + 0.01 for b_ in out_notes) \
                and not any(a_["qn"] + d0_ - EPS <= k_["qn"] <= a_["qn"] + d1_ + 0.01 for k_ in ks):
            a_["dur"] = d1_
            ov_n_ += 1
    if ov_n_:
        print(f"  {tname}: {ov_n_} legato overlaps raised to {LEG_OVERLAP_MIN_S.get(family)} s", file=sys.stderr)
    # scherzo c12: LEG_HEAD_MIN_GAP_S (the gap in seconds before a legato row's first note; see the default)
    leg_head_gaps = []
    lhg_ = by_name(LEG_HEAD_MIN_GAP_S) if LEG_HEAD_MIN_GAP_S else None
    if lhg_:
        seq_ = sorted(out_notes, key=lambda a: a["qn"])
        for b_ in seq_:
            if not (b_.get("_art") and _lg(b_["_art"])):
                continue
            bef_ = [a for a in seq_ if a is not b_ and a["qn"] < b_["qn"] - EPS]
            if not bef_:
                continue
            a_ = max(bef_, key=lambda a: a["qn"] + a["dur"])   # the note that ends last before it
            if a_.get("_art") and _lg(a_["_art"]):
                continue   # inside a legato row: the script joins or re-tongues there as before
            g_ = qn_to_sec(b_["qn"]) - qn_to_sec(a_["qn"] + a_["dur"])
            if not 0 < g_ < lhg_ - 1e-4:
                continue
            e_ = sec_to_qn(qn_to_sec(b_["qn"]) - lhg_)
            e_ = max(e_, a_["qn"] + a_["dur"] * 2.0 / 3.0)
            if e_ < a_["qn"] + a_["dur"] - 1e-4:
                a_["dur"] = round(e_ - a_["qn"], 4)
                leg_head_gaps.append([b_["qn"], round(g_ * 1000, 1),
                                      round((qn_to_sec(b_["qn"]) - qn_to_sec(a_["qn"] + a_["dur"])) * 1000, 1)])
        if leg_head_gaps:
            print(f"  {tname}: LEG_HEAD_MIN_GAP_S {lhg_} s before {len(leg_head_gaps)} legato-row first notes", file=sys.stderr)
    # scherzo c16: REP_GAP_FLOOR_S (see the default)
    rep_gap_floor = []
    rgf_ = REP_GAP_FLOOR_S.get(tname, REP_GAP_FLOOR_S.get(family)) if REP_GAP_FLOOR_S else None
    if rgf_:
        seq_ = sorted(out_notes, key=lambda a: a["qn"])
        for b_ in seq_:
            prev_ = [a for a in seq_ if a is not b_ and a["pitch"] == b_["pitch"] and a["qn"] < b_["qn"] - EPS]
            if not prev_:
                continue
            a_ = max(prev_, key=lambda a: a["qn"])
            if not any(w_ in (a_.get("_art") or "") for w_ in ("Sus", "Leg", "Port")):
                continue
            g_ = qn_to_sec(b_["qn"]) - qn_to_sec(a_["qn"] + a_["dur"])
            fl_ = rgf_
            if REP_GAP_FLOOR_LONG_S and min(qn_to_sec(a_["qn"] + a_["dur"]) - qn_to_sec(a_["qn"]),
                                            qn_to_sec(b_["qn"] + b_["dur"]) - qn_to_sec(b_["qn"])) >= REP_GAP_FLOOR_LONG_S["min_s"]:
                fl_ = REP_GAP_FLOOR_LONG_S["gap_s"]   # scherzo c18 (see the default)
            if not -0.02 < g_ < fl_ - 1e-4:
                continue
            e_ = max(sec_to_qn(qn_to_sec(b_["qn"]) - fl_), a_["qn"] + a_["dur"] * 0.5)
            if e_ < a_["qn"] + a_["dur"] - 1e-4:
                a_["dur"] = round(e_ - a_["qn"], 4)
                rep_gap_floor.append([round(b_["qn"], 3), round(g_ * 1000, 1),
                                      round((qn_to_sec(b_["qn"]) - qn_to_sec(a_["qn"] + a_["dur"])) * 1000, 1)])
        if rep_gap_floor:
            print(f"  {tname}: REP_GAP_FLOOR_S {rgf_} s before {len(rep_gap_floor)} same-pitch repeats", file=sys.stderr)
    for a in out_notes:
        a.pop("_art")
        a.pop("_rebow_back", None)
    lead_stats = collections.Counter("leg" if n.get("leg_target") else "entry" for n in ns if id(n) in shift)
    end_leg_ks = None
    if tname in END_LEG_KS and ks:   # scherzo c12: back to the legato row after the last note (see END_LEG_KS)
        rows_ = sorted(ks, key=lambda k_: k_["qn"])
        legs_ = [k_ for k_ in rows_ if (k_["art"] or "").startswith("Leg")]
        leg_ = ({"pitch": legs_[-1]["pitch"], "art": legs_[-1]["art"]} if legs_ else
                {"pitch": ks_lookup(stem, first_art)[1], "art": first_art} if (first_art or "").startswith("Leg") else None)
        if leg_ and not (rows_[-1]["art"] or "").startswith("Leg"):
            end_leg_ks = {"qn": round(SE + END_LEG_KS[tname], 4), **leg_}
            if any(n_["qn"] + n_["dur"] > end_leg_ks["qn"] - 0.5 for n_ in out_notes):
                raise SystemExit(f"END_LEG_KS {tname}: a note sounds within 0.5 qn of {end_leg_ks['qn']}")
            ks.append(dict(end_leg_ks))
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
        "acc_vel_fixed": acc_vel_fixed, "rep_retongued": rep_retongued, "arrival_weight": arr_w, **({"arrival_skipped": arr_w_skipped} if arr_w_skipped else {}), "tenuto_swell": ten_sw,
        "down_strokes": [round(n["qn"], 3) for n in ns if n.get("down_stroke")],
        **({"rep_strokes": rep_strokes, "rep_rebows": sorted(rep_rebow_q)} if (rep_strokes or rep_rebow_q) else {}),
        **({"rep_sus_gaps": rep_sus_gaps} if rep_sus_gaps else {}),
        "trem_entries": trem_entries,
        "rebows": sorted(rebow_list), "rebow_fill_ends": rebow_fill_ends, "restrikes": restrikes, "breath_splits": breath_splits, "trem_splits": trem_splits, "slur_rep_merged": slur_rep_merged,
        "short_strokes": [round(n["qn"], 3) for n in ns if n.get("short_stroke")],
        "pt_slurs": pt_slurs,
        "hp_chained": hp_chained, "loud_swells": loud_swells, "hp_soft": hp_soft, "hp_soft_acc": hp_soft_acc, "hp_bridged": hp_bridged, "bc_skipped": bc_skipped, "roles_chained": role_chained, "accent_db": acc_n, "accent_on_arrival": acc_on_arr, "detached_accents": det_n,
        "acc_sus": [round(n["qn"], 3) for n in ns if n.get("acc_sus")],
        "timp_chain_skip": timp_chain_skip, **({"timp_vel_strokes": timp_vel_strokes} if timp_vel_strokes else {}), "meas_trem": meas_trem, **({"cc11_park": cc11_park} if cc11_park else {}), **({"beat_db_notes": beat_db_notes} if beat_db_notes else {}), "cc1_fronts": cc1_fronts, "acc_fitted": acc_fitted, "accent_body": acc_body, "acc_trimmed": sorted(round(x_, 3) for x_ in acc_trim_q), "row_trimmed": row_trimmed,
        **({"end_leg_ks": end_leg_ks} if end_leg_ks else {}),
        "ks": ks, "cc1": cc1, "cc11": cc11, "cc15": cc15, "cc7": cc7, **({"timp_damp": timp_damp} if timp_damp else {}), "cc70": cc70, "cc36": cc36, **({"rr_reset": [(q_, 127) for q_ in rr_reset]} if rr_reset else {}), "pair_release": pair_rel, "detach_dips": detach_dips, "str_rep_dips": str_rep_dips, "meas_trem_alt": mt_alt_q, "uni_fades": uni_fades, "slur_start_sus": sorted(round(n["qn"], 3) for n in ns if n.get("slur_start_sus")), "slur_start_joins": slur_start_joins, "pickup_sus": pickup_sus, "pickup_lift": pickup_lift, "synco_shaped": synco_shaped, "det_lead_clamped": det_lead_clamped, "retongue_leads": retongue_leads, "wide_leg": wide_leg, "row_remapped": row_remapped, "held_decresc": held_decresc, "portato_tails": sorted(round(n["qn"], 3) for n in ns if n.get("portato_tail")), "stac_leads": stac_leads, "rest_short": rest_short, "end_at": end_at, "cutoff_early": cutoff_early, **({"ps_kinds": ps_kind_list} if ps_kind_list else {}), "rep_row": sorted(round(n["qn"], 3) for n in ns if n.get("rep_row")), "rep_row_reps": rep_row_reps, "slur_head_rep": slur_head_rep, "sul_notes": sul_notes, "rep_after_stac": sorted(round(n["qn"], 3) for n in ns if n.get("rep_after_stac")), "timp_rh": timp_rh, **({"leg_head_gaps": leg_head_gaps} if leg_head_gaps else {}), **({"rep_gap_floor": rep_gap_floor} if rep_gap_floor else {}), **({"row_change_leads": row_change_leads} if row_change_leads else {}), **({"lead_set": lead_set} if lead_set else {}), **({"hp_to_cc11": hp_to_cc11} if hp_to_cc11 else {}), **({"chord_cc11": [[round(a_, 3), round(b_, 3), u_] for a_, b_, u_ in chord_cc_]} if chord_cc_ else {}), **({"art_at": art_at_used} if art_at_used else {}), **({"leg_head_row_leads": leg_head_row_leads} if leg_head_row_leads else {}), **({"ks_early": ks_early} if ks_early else {}), **({"timp_lh_vel": timp_lh_vel} if timp_lh_vel else {}), **({"vel_cap_shift": vel_cap_shift, "vel_cap_pre": vel_cap_pre} if vel_cap_shift else {}), "leg_vel_extra": leg_vel_extra, **({"leg_vel_span": leg_vel_span} if leg_vel_span else {}), "slur_head_leads": slur_head_leads, "group_leads": group_leads, "reattack_leads": reattack_leads, "subito_fresh": subito_fresh, "subito_falls": subito_falls, "cresc_fronts": cresc_fronts, **({"cresc_front_shift": cresc_front_shift} if cresc_front_shift else {}), **({"leg_join_holds": leg_join_holds} if leg_join_holds else {}), "dyn_curve": dyn_curve, "vol_db": vol_db, "vol_bp": vol_bp, **({"hp_start_moved": hp_start_moved} if hp_start_moved else {}), **({"hp_held_end": hp_held_end} if hp_held_end else {}), **({"hp_hold_skipped_dec": hp_hold_skipped_dec} if hp_hold_skipped_dec else {}), "vol_cls": vol_cls, "vol_tags": vol_tag_n, "accent_q": sorted(round(x_, 3) for x_ in accent_q), **({"vol_layers": vol_layers} if vol_layers else {}), **({"one_level": [ol_notes, len(ol_chains)]} if ol_chains else {}), **({"vol_post": vol_post} if vol_post else {}),
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
    keep_gl_ = {k_: globals()[k_] for k_ in as_.get("globals", {})}   # mvt1 c45 (see the default)
    globals().update(as_.get("globals", {}))
    try:
        CUR_ALIAS = an_
        p_ = build_track(src_[0], src_[1], as_.get("patch", src_[2]), src_[3], src_[4])
    finally:
        CUR_ALIAS = None
        globals().update(keep_gl_)
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
# scherzo c16: HELD_DOUBLE (see the default)
def _lane_at(lane_, q_, default_=None):
    v_ = default_ if default_ is not None else (lane_[0][1] if lane_ else 0)
    for c_ in lane_:
        if c_[0] <= q_ + 1e-6:
            v_ = c_[1]
        else:
            break
    return v_


def _lane_lift(lane_, p_, lift_):
    """CC lane (step points) with +units over a hole that starts at qn p_: rise, hold, fall in seconds"""
    u_, rise_, hold_, fall_ = lift_[:4]
    lead_ = lift_[4] if len(lift_) > 4 else 0.0   # scherzo c17 (critic A #3): the lift is complete ON the other's bow change
    t0_ = qn_to_sec(p_)
    a_, b_ = sec_to_qn(t0_ - max(0.02, lead_)), sec_to_qn(t0_ + rise_ + hold_ + fall_)
    def w_(t_):
        t_ -= t0_
        if lead_ > 0:
            if t_ < -lead_:
                return 0.0
            if t_ < 0:
                return 1.0 + t_ / lead_
            if t_ < rise_ + hold_:
                return 1.0
            return max(0.0, 1.0 - (t_ - rise_ - hold_) / fall_)
        if t_ < 0:
            return 0.0
        if t_ < rise_:
            return t_ / rise_
        if t_ < rise_ + hold_:
            return 1.0
        return max(0.0, 1.0 - (t_ - rise_ - hold_) / fall_)
    n_ = max(2, int((qn_to_sec(b_) - qn_to_sec(a_)) / 0.04))
    qs_ = sorted({round(a_ + (b_ - a_) * k_ / n_, 4) for k_ in range(n_ + 1)} | {round(c_[0], 4) for c_ in lane_ if a_ <= c_[0] <= b_})
    new_ = [[q_, int(round(max(1, min(127, _lane_at(lane_, q_) + u_ * w_(qn_to_sec(q_))))))] for q_ in qs_]
    end_v_ = _lane_at(lane_, b_)
    out_ = [list(c_) for c_ in lane_ if c_[0] < a_ - 1e-6] + new_ + [[round(b_ + 0.001, 4), end_v_]] + [list(c_) for c_ in lane_ if c_[0] > b_ + 0.001]
    res_, last_ = [], None
    for q_, v_ in out_:
        if v_ != last_:
            res_.append([q_, v_]); last_ = v_
    return res_


for src_n_, rows_ in HELD_DOUBLE.items():
    ps_ = next(p_ for p_ in parts if p_["name"] == src_n_)
    for row_ in rows_:
        pd_ = next(p_ for p_ in parts if p_["name"] == row_["to"])
        q0_, q1_ = row_["span"]
        pcs_ = sorted((n_ for n_ in ps_["notes"] if q0_ - 1e-6 <= n_["sq"] < q1_), key=lambda n_: n_["qn"])
        if not pcs_ or len({n_["pitch"] for n_ in pcs_}) != 1:
            raise SystemExit(f"HELD_DOUBLE {src_n_} {row_['span']}: needs the pieces of one held pitch")
        a_, e_ = pcs_[0]["qn"], max(n_["qn"] + n_["dur"] for n_ in pcs_)
        if any(n_["qn"] + n_["dur"] > a_ - 0.5 and n_["qn"] < e_ + 0.5 for n_ in pd_["notes"]):
            raise SystemExit(f"HELD_DOUBLE {src_n_} -> {row_['to']}: the target track plays in the span")
        bnd_ = [a_] + sorted(row_.get("rebow_at", [])) + [e_]
        new_notes_ = []
        for k_ in range(len(bnd_) - 1):
            end_ = bnd_[k_ + 1] - (REBOW_GAP_QN if k_ < len(bnd_) - 2 else 0.0)
            new_notes_.append({"qn": round(bnd_[k_], 4), "dur": round(end_ - bnd_[k_], 4), "pitch": pcs_[0]["pitch"],
                               "vel": row_.get("vel", pcs_[0]["vel"]), "sq": round(pcs_[0]["sq"] if k_ == 0 else bnd_[k_], 4)})
        pd_["notes"] = sorted(pd_["notes"] + new_notes_, key=lambda n_: n_["qn"])
        if row_.get("art"):
            pd_["art_counts"][row_["art"]] = pd_["art_counts"].get(row_["art"], 0) + len(new_notes_)   # c17: the row is loaded
            pd_["ks"] = sorted(pd_["ks"] + [{"qn": round(a_ - 1.0, 4), "pitch": ks_lookup(pd_["stem"], row_["art"])[1], "art": row_["art"]}],
                               key=lambda k_: k_["qn"])
        # CC11: the source's lane over the span (plus cc11_add), set 1 qn before the copy starts
        add_ = row_.get("cc11_add", 0)
        src11_ = [list(c_) for c_ in ps_["cc11"]]
        cp_ = [[round(a_ - 1.0, 4), _lane_at(src11_, a_)]] + [c_ for c_ in src11_ if a_ < c_[0] <= e_ + 0.01]
        cp_ = [[q_, int(max(1, min(127, v_ + add_)))] for q_, v_ in cp_]
        pd_["cc11"] = [list(c_) for c_ in pd_["cc11"] if c_[0] < a_ - 1.0 - 1e-6] + cp_
        if row_.get("cc1") is not None:
            old1_ = _lane_at([list(c_) for c_ in pd_["cc1"]], a_)
            pd_["cc1"] = [list(c_) for c_ in pd_["cc1"] if c_[0] < a_ - 1.0 - 1e-6] + [[round(a_ - 1.0, 4), row_["cc1"]], [round(e_ + 2.0, 4), old1_]]
        if row_.get("lift"):
            for p__ in bnd_[1:-1]:                       # the copy re-bows: the source holds and lifts
                ps_["cc11"] = _lane_lift([list(c_) for c_ in ps_["cc11"]], p__, row_["lift"])
            for n_ in pcs_[1:]:                          # the source re-bows: the copy lifts
                pd_["cc11"] = _lane_lift(pd_["cc11"], n_["qn"], row_["lift"])
        # the source's final fade (vol_db from SE - 6 on, relative to its value there) on the copy
        if e_ > SE - 6:
            v0_ = _lane_at(ps_["vol_db"], SE - 6, 0.0)
            d0_ = _lane_at(pd_["vol_db"], SE - 6, 0.0)
            pd_["vol_db"] = [list(c_) for c_ in pd_["vol_db"] if c_[0] <= SE - 6] + [[c_[0], round(d0_ + c_[1] - v0_, 2)] for c_ in ps_["vol_db"] if c_[0] > SE - 6]
        pd_.setdefault("held_double", []).append({"from": src_n_, "span": [round(a_, 4), round(e_, 4)], "rebows": bnd_[1:-1]})
        ps_.setdefault("held_double_src", []).append({"to": row_["to"], "span": [round(a_, 4), round(e_, 4)]})
        print(f"  HELD_DOUBLE {src_n_} {a_:.3f}-{e_:.3f} also on {row_['to']} ({len(new_notes_)} pieces)", file=sys.stderr)
for p_ in parts:
    if p_["name"] in PASS2_TRACKS:
        p_["pass"] = 2
    if p_["name"] in TEST_TRACKS:   # mvt1 c41 (see the default)
        p_["test"] = True
json.dump({"tpb": TPB, "end_qn": END, "score_end": SE, "title": SCORE_TITLE, "preroll_qn": PREROLL_QN, "preroll_bpm": PREROLL_BPM, "tempo": tempo, "timesig": timesig, **({"ride_trims": [[[float(q_), float(d_)] for q_, d_ in r_] for r_ in RIDE_TRIMS]} if RIDE_TRIMS else {}), "tracks": parts}, open(OUT, "w"), indent=1)
for p in parts:
    print(f'{p["name"]:15s} notes={len(p["notes"]):4d} ks={len(p["ks"]):3d} cc11={len(p["cc11"]):4d} range={p["range"]} clash={p["ks_clash"]} {p["art_counts"]} leads={p["leads"]} notches={p["notches"]} uni_drop={p["unison_dropped"]} bloomv={p["bloomv"]} pitch_trim={p["pitch_trimmed"]} div_ent={p["div_entries"]} extra={p["extra_leads"]} bcsoft={p["bcsoft"]} hpgain={len(p["hpgain"])} hp_chain={p["hp_chained"]} bc_skip={p["bc_skipped"]} roles_chained={p["roles_chained"]} acc_db={p["accent_db"]}')
if hp_lookahead_targeted:   # scherzo c22: HP_TARGET_LOOKAHEAD_QN hits (staves, start, stop, mark, mark qn)
    print(f"HP_TARGET_LOOKAHEAD: {sorted(set(hp_lookahead_targeted))}", file=sys.stderr)
if hp_sf_targeted:   # mvt1 c38: HP_SF_TARGET hits (hairpin start, end), once per hairpin
    print(f"HP_SF_TARGET: {sorted(set(hp_sf_targeted))}", file=sys.stderr)
