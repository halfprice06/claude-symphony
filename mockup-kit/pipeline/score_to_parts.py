"""Turn the mockup build (mockup.midi + mockup-events.tsv) into per-track part data for REAPER.

Output: parts.json with the tempo map and, per track, notes / keyswitches / CC11 dynamics / CC1 vibrato / CC15 mutes /
CC7 (timpani) in quarter notes from the start of the piece, plus the Opus patch and its starting articulation.
Mix settings (track gain, seat, width, mics, reverb send) live in build/mix.json and are applied by build_reaper.py.

Usage: python score_to_parts.py <build-dir> <ks_maps.json> <out.json>
"""
import collections, json, re, sys
import mido

BUILD, KSMAPS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOL = "/Volumes/MAC DRIVE"
S = VOL + "/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/"
W = VOL + "/EW Hollywood Orchestral Woodwinds Diamond/Hollywood Orch Woodwinds Opus Instruments/"
B = VOL + "/EW Hollywood Brass Diamond/Hollywood Brass Opus Instruments/"
H = VOL + "/EW Hollywood Harp Diamond/Hollywood Harp Opus Instruments/"
P = VOL + "/EW Hollywood Orchestral Percussion Diamond/Hollywood Orch Percussion Opus Instruments/"

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
]
# c10 (A #1): notes by score onset: {track: (from qn, to qn, keep inside?)}; Violins I rests while the solo track plays
TRACK_WINDOWS = {"Violin I solo": (48.0, 65.0, True), "Violins I": (48.0, 65.0, False)}
# c13 (A #1): {split track: (source track, [(from qn, to qn)], lowest pitch)}: source-staff notes with a score onset in
# a window and a pitch at or above the lowest pitch play on the split track and are removed from the source track. The
# source track still counts them for its divisi level cut (it keeps playing a half section's line on a full-section
# patch). Both answers were two-note Sus MAX chords on the full Celli KS Master: 10-15 dB holes, the slur re-attacked.
TRACK_SPLITS = {"Violoncellos div": ("Violoncellos", [(51.0, 54.0), (63.0, 66.0)], 55)}

# c02: ff 104 -> 114 and fff 118 -> 124 (the patches' top dynamic layer runs to 127; f -> ff measured only +2.5 LU)
DYN = {"ppp": 22, "pp": 34, "p": 46, "mp": 58, "mf": 72, "f": 88, "ff": 114, "fff": 124, "sf": 100, "sfz": 100, "fp": 46}
KS_LEAD = 0.06       # keyswitch lead in quarter notes when there is no rest before the note
LEG_OVERLAP = 0.04   # slurred notes overlap the next by this much so Opus plays a legato transition
HP_STEP = 14         # a hairpin with no target dynamic moves about one dynamic level
HP_STEP_SOFT = 22    # c02: untargeted hairpins starting at mp or softer (14 CC measured a median +2.6 dB)
SOLO_BOOST = 8       # CC11 added after "solo" texts, and after "cantabile" / "espr." in winds and brass (about +2.5 dB)
SOFT_BOOST = 3       # c02: "espr." / "cantabile" / "dolce" in string sections, "dolce" alone in winds
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
GRACE_S = 0.09       # c03 (C #2): after-grace notes, each this long, ending on the main note they lead to
TENUTO_BUMP, ACCENT_BUMP = 5, 8
TIMP_VEL = {278.5: 60, 279.0: 60}
TIMP_HP_DB_FACTOR = 1.0     # c13 (A #3): share of the CC7 shortfall in roll hairpins made up in the volume envelope
TIMP_LOUD_ATTACK_DB = 6.0   # c10 (B #2): f/ff timpani attacks measured 8-13 dB under the mix in 50-250 Hz   # c03 (B #1): two pp strokes measured about 6 dB under the one at qn 277
EPS = 1e-6
# c04 (C #6): breaths before the two tutti arrivals take time: seconds added in the 0.25 qn before the breath
CAESURA = {204.0: 0.22, 268.0: 0.15,
           # c08 (C #3): solo breath marks (Hn1 bar 10, Fl1 bar 41, CA bar 50, Cl1 bar 87) and phrase seams
           29.0: 0.12, 124.0: 0.12, 164.0: 0.10, 286.0: 0.10,
           42.0: 0.08, 48.0: 0.10, 66.0: 0.10, 140.0: 0.08, 171.0: 0.10, 237.0: 0.10}
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
LEG_PAIR_EXTRA_S = {"Violoncellos": {(56, 60): 0.15}, "Violas": {(60, 63): 0.10, (65, 61): 0.12}}
# c11 (C #3): build/leg_leads.json {track: {score onset: s}}: per-onset legato lead offsets (may be negative); the total
# legato lead is clamped to LEG_LEAD_CLAMP
LEG_LEAD_CLAMP = (0.03, 0.35)
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
VEL_SET = {"Trombone 1": {218.0: 110, 212.5: 108, 213.0: 105},
           "Violoncellos": {286.0: 60}, "Violas": {286.0: 60}, "Double basses": {286.0: 60},
           "Oboe 1": {148.0: 100}}   # c08 (C #2c): the bar 47 goal re-attack (Sus MAX, same pitch) was v73
# c08 (C #5 interim): no CC11 SOLO_BOOST on these tracks' "solo" texts (Vln I bars 17-22 is a 16-player section; the boost
# put it 6 dB over the oboe it answers); CC1 +SOLO_VIB instead over the span (narrower, vibrato-led)
SOLO_NO_BOOST, SOLO_VIB = ("Violins I",), 10
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
BC_SOFT_SKIP = {"Violins II": [48, 54, 57, 146, 154, 159, 271], "Violas": [159],
                "Violoncellos": [45, 50, 60, 62, 132, 144, 160, 220]}
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
SOSTENUTO_SPANS = [(204.0, 212.0)]
SOST_NOTCH, SOST_VEL, SOST_REP_S = 10, 100, 0.04
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
ACCENT_DB_AT = {"Trombone 1": {212.5: 4.0, 218.0: 3.0}}
# c09 (A #2): role spans that meet (B starts within ROLE_CHAIN qn of A's end) crossfade over [B.a - 0.1, B.a + 0.15]
# instead of ramping A out and B in on their own 0.5 qn ramps (both were at full value at the shared qn)
ROLE_CHAIN = 0.5
# c10 (C #3): a chained second crescendo to f+ rises by this share of HP_GAIN_DB over the first one's gain (it started
# from it and ended at it: bar 60 was flat or falling in every woodwind, then the winds stepped 8-12 dB at bar 61)
# Winds only: the strings and brass already grew 5-15 dB across bar 60, and a string rise put the bar 61 downbeat 2 dB
# over c09's master peak in simulation
HP_CHAIN_RISE = {"wind": 0.75}
# c10 (C #4d): string legato targets inside SOSTENUTO_SPANS (v124 Leg BC transitions peaked 17-19 dB over their body)
SOST_STR_LEG_VEL = 108
# c11 (A #4): Leg Port MAX (portamento) on these legato targets {track: {score onset: velocity}}: the one-string leaps of
# the "espr., sul D" phrase (F5 -> B flat 5) and the "sul A" entry (C5 -> F5). First trial on Violins I only; check the
# f0 glide (target 0.08-0.25 s) before adding Vln II 82 / Vc 83
PORT_TARGETS = {"Violins I": {82.0: 100, 172.0: 100},
                # c12 (A #3): the same leaps in Violins II (unison with Vln I), and the celli's A flat 3 -> D flat 4 in the
                # cantabile (Vln I 82 measured a 0.12-0.15 s glide 12-15 dB under the source note, no hole)
                "Violins II": {82.0: 100, 172.0: 100}, "Violoncellos": {83.0: 100}}
# c11 (C #6): slurred string short_sus notes (< 0.2 s) at CC11 >= 90 end 0.01 qn before the next onset (no overlap) at
# velocity 100 or more: the overlapped v83 viola sextuplets of bars 59-60 (f, CC 88 and up) measured a median dominance
# share of 0.26
SHORT_SUS_DETACH = {"max_s": 0.2, "min_cc": 86, "gap": 0.01, "vel": 100}
# c10 (C #4a): share of HP_GAIN_DB held through a SOSTENUTO_SPAN after a crescendo's arrival (full: simulated master peak
# -2.2 dBFS on the bar 62 legato transitions and a 4.9 dB limiter)
SOST_HOLD_SHARE = float(__import__("os").environ.get("SOST_HOLD_SHARE", "0.5"))

ksmaps = json.load(open(KSMAPS))
# c10 (A #1): keyswitch maps of patches not in the bridge's ks_maps.json, dumped from the .oib with dump_ks.py
if __import__("os").path.exists(f"{BUILD}/ks_maps_extra.json"):
    ksmaps.update(json.load(open(f"{BUILD}/ks_maps_extra.json")))
ROLES = json.load(open(f"{BUILD}/roles.json")) if __import__("os").path.exists(f"{BUILD}/roles.json") else {}
NOTE_TRIMS = json.load(open(f"{BUILD}/note_trims.json")) if __import__("os").path.exists(f"{BUILD}/note_trims.json") else {}
# c06 (A #2): per-pitch level trims for notes on a legato articulation, {track: {midi pitch: dB}} (sample unevenness)
PITCH_TRIMS = json.load(open(f"{BUILD}/pitch_trims.json")) if __import__("os").path.exists(f"{BUILD}/pitch_trims.json") else {}
# c07 (C #2b): extra entry leads in seconds, {track: {score onset: s}}
ENTRY_LEADS = json.load(open(f"{BUILD}/entry_leads.json")) if __import__("os").path.exists(f"{BUILD}/entry_leads.json") else {}
# c08 (A #1): early fills, {track: {score onset: dB}} on the first 0.35 s of sagging legato targets
EARLY_FILLS = json.load(open(f"{BUILD}/early_fills.json")) if __import__("os").path.exists(f"{BUILD}/early_fills.json") else {}
LEG_LEADS = json.load(open(f"{BUILD}/leg_leads.json")) if __import__("os").path.exists(f"{BUILD}/leg_leads.json") else {}


def ks_lookup(patch_stem, *names):
    arts = {a["name"].lower(): a["key"] for a in ksmaps[patch_stem]["articulations"]}
    for n in names:
        if n.lower() in arts:
            return n, arts[n.lower()]
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
RAMP_SPANS = [(102, 108, 52), (150, 152, 60), (172, 200, 60), (200, 204, 64), (212, 220, 54), (259, 274, 52), (292, 303, 52)]


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
PHRASE_ARCS = [(18, 30), (30, 42), (42, 48), (48, 54), (54, 60), (60, 66), (66, 78), (78, 90), (108, 124), (124, 140),
               (220, 226), (226, 238), (238, 250), (274, 286)]
PHRASE_PUSH, PHRASE_SLOW = 1.015, (0.96, 0.92)


def phrase_arcs(steps):
    def val(q):
        v = steps[0][1]
        for tq, b in steps:
            if tq <= q + EPS:
                v = b
        return v
    for a, e in PHRASE_ARCS:
        if any(a < e2 - EPS and e > a2 + EPS for a2, e2, _ in RAMP_SPANS):
            print(f"  phrase arc {a}-{e}: skipped (tempo ramp)", file=sys.stderr)
            continue
        mid = (a + e) / 2
        segs = [(a + 1, mid, PHRASE_PUSH), (mid, e - 2, 1.0), (e - 2, e - 1, PHRASE_SLOW[0]), (e - 1, e, PHRASE_SLOW[1])]
        cuts = sorted({q for q, _ in steps if a + 1 - EPS <= q < e - EPS} | {x for s0, s1, _ in segs for x in (s0, s1)})
        new = [(q, b) for q, b in steps if not (a + 1 - EPS <= q < e + EPS)]
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


def bpm_at(q):
    b = TEMPO[0][1]
    for tq, bpm in TEMPO:
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
GRACE_ROWS = collections.defaultdict(list)   # c03: grace notes, (qn of the event, kind, values, grace offset)
for line in open(f"{BUILD}/mockup-events.tsv", encoding="utf-8"):
    f = line.rstrip("\n").split("\t")
    if len(f) < 4:
        continue
    staff, qn, grace, kind, vals = f[0], float(f[1]), float(f[2]), f[3], f[4:]
    ev[staff].append((qn, kind, vals))
    if grace != 0 and kind == "note":
        GRACE_ROWS[staff].append((qn, kind, vals, grace))
for s in ev:
    ev[s].sort(key=lambda e: e[0])
END = max(n["end"] for ns in notes.values() for n in ns)


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
SHARED_DYN = {"Bassoon 1": [(259.0, "f")]}


def base_points(staff_list, extra_marks=()):
    marks, hps = hairpins_and_marks(staff_list)
    if extra_marks:
        marks = sorted(set(marks) | set(extra_marks))
    first_note = min((n["qn"] for s in staff_list for n in notes[s]), default=0.0)
    level = DYN["p"]
    if marks and marks[0][0] <= first_note + 0.01:
        level = DYN[marks[0][1]]
    pts = [(0.0, level)]
    events = [(q, 0, "mark", d) for q, d in marks] + [(a, 1, "hp", (b, k)) for a, b, k in hps]
    events.sort(key=lambda e: (e[0], e[1]))
    sf_hp = {}   # c02: sf followed by a decrescendo: spike, then the hairpin starts from min(level, mf) at q + 0.5
    hold_after = None
    last_un = None   # c09 (B #3): (stop, start level, kind) of the last untargeted hairpin
    for q, _, kind, data in events:
        if kind == "mark":
            last_un = None
            if data in ("sf", "sfz"):
                hp_here = any(k == "decresc" and q - EPS <= a <= q + 0.25 for a, b, k in hps)
                # c04 (A #3): from f or louder the sf is +8 (ff 114 -> 122), and it holds through the tremolo's attack
                spike = min(124, level + 8) if level >= DYN["f"] else min(124, max(DYN["sf"], level + 12))
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
            if hold_after and hold_after[0] - EPS <= q <= hold_after[1] + EPS and DYN[data] > level:
                continue   # c06 (C #3): a mark just after a decrescendo that was turned downward does not raise it
            pts.append((q, level))   # hold the previous level up to the mark (no ramps between marks)
            level = DYN[data]
            pts.append((q, level))
        else:
            stop, hk = data
            tgt = next((DYN[d] for mq, d in marks if stop - 0.01 <= mq <= stop + 1.0 and d not in ("sf", "sfz")), None)
            start = level
            untargeted = tgt is None
            if tgt is None:
                step = HP_STEP_SOFT if level <= DYN["mp"] + 2 else HP_STEP
                tgt = level + (step if hk == "cresc" else -step)
                mdv = last_un and last_un[2] != hk and abs(q - last_un[0]) <= 0.3
                if mdv:
                    # c09 (B #3): an untargeted < > (or > <) returns to where the first hairpin started (a 22 CC
                    # crescendo followed by a 14 CC decrescendo left the line one level higher). The next-mark limit
                    # below does not apply (Vln I bar 73-75: p < > then mp; it held the line at CC 58 until the mp)
                    tgt = last_un[1]
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
                    nm2 = next((DYN[d] for mq, d in marks if stop + 1.0 < mq <= hz and d not in ("sf", "sfz")), None)
                    # From p or softer only the overshoot is removed (cap at the mark itself): a -8 margin there cut
                    # Hn1's bar 7 p swell from CC 68 to 52 in a trial build
                    if nm2 is not None and nm2 > level:
                        tgt = min(tgt, max(level + 6, nm2 - 8) if level >= DYN["mp"] - 2 else nm2)
            elif hk == "decresc" and tgt >= level:
                # c06 (C #3): a decrescendo whose printed target is not below the current level still falls (6 CC);
                # the mark at its end then does not raise the level again
                tgt = level - 6
                hold_after = (stop - 0.01, stop + 1.0)
            elif hk == "cresc" and abs(tgt - level) < EPS:
                start = level - 12   # c06 (C #3): "niente <" to the current level starts 12 CC lower
            tgt = max(10, min(124, tgt))
            q = next((v for k, v in sf_hp.items() if k - EPS <= q <= k + 0.25), q)
            pts += [(q, level), (q, max(10, start)), (stop, tgt)]
            last_un = (stop, level, hk) if untargeted else None
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
        w0, w1, inside_ = TRACK_WINDOWS[tname]
        ns = [n for n in ns if (w0 - EPS <= n["qn"] < w1 - EPS) == inside_]
    split_away = []   # c13 (A #1)
    for tsp_, (src_, wins_, pmin_) in TRACK_SPLITS.items():
        if tname not in (tsp_, src_):
            continue
        insp_ = lambda n, w=wins_, p=pmin_: n["pitch"] >= p and any(a - EPS <= n["qn"] < b - EPS for a, b in w)
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
        ns.sort(key=lambda n: (n["qn"], n["pitch"]))

    def slur_of(q):
        return next((i for i, (a, b) in enumerate(slurs) if a - EPS <= q <= b + EPS), None)

    trem_q = {q for s in staves for q, k, v in ev[s] if k == "tremolo"}
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

    # c08 (B #4): the harmonics read the dynamics of both harp staves (the bar 82 p is printed on the lower staff)
    dyn_staves = ["HarpR", "HarpL"] if family == "harm" else staves
    pts, marks, hps = base_points(dyn_staves, SHARED_DYN.get(tname, ())) if ns else ([(0.0, DYN["p"])], [], [])
    base = lambda q: value_at(pts, q)

    has_bc = family == "string" and any(a["name"] == "Leg BC MAX" for a in ksmaps.get(stem, {}).get("articulations", []))
    for n in ns:
        q = n["qn"]
        n["slur"] = slur_of(q)
        if family in ("harp", "harm"):
            n["art"] = None
            continue
        if family == "timp":
            n["art"] = ks_lookup(stem, "Timpani Flt Rls")[0] if q in trem_q else ks_lookup(stem, "Timpani Flt Lng")[0]
            continue
        if n.get("grace") or n.get("grace_target"):   # c03: the run and its target on one legato articulation
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
            continue
        if family == "string":
            pizz = text_state(q, ["pizz"], ["arco"])
            tasto = text_state(q, ["sul tasto"], ["ord.", "arco"])
            if pizz:
                n["art"] = ks_lookup(stem, "Pizzicato RRx4", "Pizz RRx4")[0]
            elif q in trem_q:
                n["art"] = ks_lookup(stem, "Tremolo")[0]
            elif q in stacc_q:
                n["art"] = ks_lookup(stem, "Stac RRx14", "Stac RRx9", "Staccato RRx9")[0]
            elif tasto and stem.startswith("2nd"):
                n["art"] = ks_lookup(stem, "Flautando")[0]
            elif n["slur"] is not None and not polyphonic(n) \
                    and qn_to_sec(n["end"], TEMPO_NC) - qn_to_sec(q, TEMPO_NC) < 0.25:
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
        if q in accent_q and base(q) >= DYN["f"] - 4:
            n["art"] = ks_lookup(stem, "Sus Accent MAX", "Sus Accent")[0]
        elif n["slur"] is not None and near(q, ten_q) and family == "wind" and in_sost(q) and not polyphonic(n) \
                and not any(o["pitch"] == n["pitch"] and o["qn"] < q - EPS and abs(o["end"] - q) < 0.05 for o in ns):
            # c07 (A #1): portato under "Largamente / molto sostenuto" is joined: legato (new pitch, or the first note)
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
            n["sost"] = True
        elif n["slur"] is not None and near(q, ten_q):
            # c04 (A #4): a tenuto inside a slur (portato) is tongued: Sus attack, not Leg Slur's slow first-note layer
            n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib")[0]
            if family == "wind" and in_sost(q) and not polyphonic(n) \
                    and any(o["pitch"] == n["pitch"] and o["qn"] < q - EPS and abs(o["end"] - q) < 0.05 for o in ns):
                n["sost_rep"] = True   # c07 (A #1): repeated pitch in the sostenuto span: re-tongued, early and firm
        elif n["slur"] is not None:
            n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")[0]
        else:
            n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib")[0]
            if family == "wind" and in_sost(q) and near(q, ten_q):
                n["sost_sus"] = True   # c07 (A #1): unslurred tenuto under "Largamente" (Cl2): crossfaded, not cut

    # c02: bow-change legato (Leg BC MAX) where a monophonic string line joins without a slur, or where one slur ends
    # and the next begins: the target note is played as a legato bow change instead of a cut and a new attack
    vla_bc_notch = []
    bc_skipped = []
    if has_bc:
        for i, n in enumerate(ns):
            # c03 (A #3): tenuto notes join with Leg BC too (the +5 CC tenuto bump is their weight)
            if n["art"] not in ("Leg Slur MAX", "Leg BC MAX") or near(n["end"], breath_q) or n.get("grace"):
                continue
            nxt = [o for o in ns[i + 1:] if -EPS < o["qn"] - n["end"] < 0.1]
            if len(nxt) != 1 or [o for o in ns[i + 1:] if abs(o["qn"] - nxt[0]["qn"]) < EPS] != nxt:
                continue
            o = nxt[0]
            if o["pitch"] == n["pitch"] or o["art"] not in ("Leg Slur MAX",) or polyphonic(o) or o.get("grace") \
                    or o.get("grace_target"):
                continue
            if n["slur"] is not None and o["slur"] == n["slur"]:
                continue
            # c09 (A #3): no bow-change legato across more than an octave (the HO legato scripts cover an octave; Vc
            # qn 274 C4 -> A flat 2 entered 1 s late) or where a solo ends and the section enters (Vln I qn 65 "tutti"):
            # different players. A wide unslurred step plays Sus MAX (the c06 Leg -> Sus entry path)
            wide = abs(o["pitch"] - n["pitch"]) > 12
            if wide or any(abs(tq - o["qn"]) < EPS and (has(t, "tutti") or has(t, "solo"))
                           for tq, t in texts_until(staves, o["qn"])):
                if wide and o["slur"] is None:
                    o["art"] = ks_lookup(stem, "Sus MAX")[0]
                elif not wide:
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
    if family == "string":
        i = 0
        while i < len(ns):
            n = ns[i]
            if n.get("art") and "Leg" in n["art"] and not near(n["end"], breath_q):
                nxt = [o for o in ns[i + 1:] if -EPS < o["qn"] - n["end"] < 0.1]
                same_on = [o for o in ns[i + 1:] if nxt and abs(o["qn"] - nxt[0]["qn"]) < EPS]
                if len(nxt) == 1 and same_on == nxt and nxt[0]["pitch"] == n["pitch"] and "Leg" in (nxt[0].get("art") or "") \
                        and not polyphonic(n) and not polyphonic(nxt[0]):
                    o = nxt[0]
                    portato = near(o["qn"], ten_q) and n["slur"] is not None and o["slur"] == n["slur"]
                    # c04 (C #5): a bow change at pp (CC11 40 or below) takes 8 CC, not 14
                    notches.append((o["qn"], 10 if portato else (8 if base(o["qn"]) <= 40 else 14)))
                    if near(o["qn"], ten_q):
                        merged_ten.append(o["qn"])
                    n["end"] = o["end"]
                    n["slur"] = o["slur"]   # joins onward as the dropped note did
                    for o2 in ns:   # a later note bow-changed from the dropped one now joins from the merged note
                        if o2.get("bc_from") == id(o):
                            o2["bc_from"] = id(n)
                    ns.remove(o)
                    continue   # the merged note may repeat again
            i += 1

    # c06 (A #5): a printed up-bow/down-bow inside a held (tied) string note is a bow change: the same notch as a merged
    # repeat (14 CC above CC 40, 6 at pp and softer)
    if family == "string":
        bow_q = sorted({q for s_ in staves for q, k, v in ev[s_] if k == "script" and v[0] in ("upbow", "downbow")})
        for bq in bow_q:
            if any(n["qn"] + 0.01 < bq < n["end"] - 0.01 for n in ns) and not any(abs(nq - bq) < EPS for nq, _ in notches):
                notches.append((bq, 14 if base(bq) > 40 else 6))

    # note lengths (c01): breaths, legato joins inside one slur only, bow change / re-tongue between slurs,
    # repeated pitches re-attacked, tenuto as a small separation
    orig_end = {id(n): n["end"] for n in ns}
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
            if family in ("wind", "brass") and base(e0 - 0.01) >= DYN["mf"]:
                n["end"] = e0 - min(0.3, 0.5 * dur)
            else:
                n["end"] = e0 - min(0.25, 0.2 * dur)
            continue
        if not nxt:
            continue
        same_pitch = any(o["pitch"] == n["pitch"] for o in nxt)
        is_leg = bool(n.get("art") and "Leg" in n["art"])
        o0 = nxt[0]
        leg_join = is_leg and not same_pitch and "Leg" in (o0.get("art") or "") and (
            (n["slur"] is not None and o0["slur"] == n["slur"]) or o0.get("bc_from") == id(n))
        if TREM_TIMING_C04 and near(n["qn"], ten_q) and family == "string" and not leg_join and o0.get("art") != n.get("art") \
                and base(n["qn"]) >= DYN["f"]:
            # c04 (A #3): a loud string tenuto into another articulation (bar 62 -> 63 tremolo) crossfades, no hole
            n["end"] = e0 + 0.02
        elif (n.get("sost") or n.get("sost_rep") or n.get("sost_sus")) and same_pitch:
            n["end"] = e0 - 0.01   # c07 (A #1): into a repeated pitch under "Largamente": the shortest break
        elif n.get("sost_rep") or n.get("sost_sus"):
            n["end"] = e0 + 0.03   # c07 (A #1): a Sus note under "Largamente" into a new pitch: 0.03 qn crossfade
        elif near(n["qn"], ten_q) and not (family == "string" and leg_join) and not (n.get("sost") and leg_join):
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
        elif same_pitch:
            n["end"] = e0 - (min(0.06, 0.15 * dur) if is_leg else min(0.03, 0.1 * dur))
        elif is_leg:
            o = nxt[0]
            if (o.get("art") == n["art"] or (family == "string" and "Leg" in (o.get("art") or ""))) \
                    and n["slur"] is not None and o["slur"] == n["slur"]:
                n["end"] = e0 + LEG_OVERLAP
                o["leg_target"] = True
                o["leg_prev"] = n
            elif o.get("bc_from") == id(n):
                n["end"] = e0 + LEG_OVERLAP
                o["leg_target"] = True
                o["leg_prev"] = n
            elif o.get("art") and "Leg" in o["art"]:
                n["end"] = e0 - min(0.05, 0.15 * dur)

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
        if n.get("sost") and n.get("leg_target"):
            notches.append((n["qn"], SOST_NOTCH))

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
    for n in ns:
        sec = qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"])
        if n.get("grace"):
            n["vel"] = 127
        elif n.get("leg_target"):   # legato patches: velocity sets transition speed (HO manual 2.1.1); loudness is CC11
            if family == "string" and n["qn"] >= CODA_SOFT["from_qn"] and base(n["qn"]) <= CODA_SOFT["max_cc"]:
                n["vel"] = CODA_SOFT["vel"]   # c08 (C #4): soft coda joins, not the v124 bump
            elif family == "string" and in_sost(n["qn"]):
                n["vel"] = SOST_STR_LEG_VEL   # c10 (C #4d): broad Largamente joins, no 17-19 dB transition peaks
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
        if n["qn"] in accent_q:
            n["vel"] = min(127, n["vel"] + 10)
        if any(abs(n["qn"] - q) < 0.01 and d in ("sf", "sfz") for q, d in marks):   # c02: sf weight
            n["vel"] = min(127, n["vel"] + 15)
        if family == "timp" and round(n["qn"], 2) in TIMP_VEL:   # c03 (B #1): pp strokes 6 dB under qn 277
            n["vel"] = max(n["vel"], TIMP_VEL[round(n["qn"], 2)])
        if n.get("sost_rep") or n.get("sost_sus"):
            n["vel"] = max(n["vel"], SOST_VEL)
        if n.get("port_vel"):   # c11 (A #4)
            n["vel"] = n["port_vel"]
        if n.get("detach"):     # c11 (C #6)
            n["vel"] = max(n["vel"], SHORT_SUS_DETACH["vel"])
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
            elif any(has(t, w) for w in ("cantabile", "espr")):
                amt = SOFT_BOOST if family == "string" else SOLO_BOOST
            elif has(t, "dolce"):
                amt = SOFT_BOOST
            else:
                continue
            stop = min([x for x, _ in txts[i + 1:] if x > q + EPS] + [r for r in rs if r > q + EPS] + [END])
            if tname in TRACK_WINDOWS and TRACK_WINDOWS[tname][2]:   # c10 (A #1): the solo's boost covers its window
                stop = min([x for x, _ in txts[i + 1:] if x > q + EPS] + [TRACK_WINDOWS[tname][1]])
            boost_spans.append((q, stop, amt))
    bumps = []
    holds = []   # c08 (C #1): (start, end, CC) flat additions
    for n in ns:
        if near(n["qn"], ten_q):
            bumps.append((n["qn"], TENUTO_BUMP, 0.5))
            if in_sost(n["qn"]) and base(n["qn"]) >= DYN["f"]:
                # c08 (C #1): a tenuto arrival under "molto sostenuto" at f+ holds its weight (bump - 1) to the note end
                holds.append((n["qn"], orig_end[id(n)], TENUTO_BUMP - 1))
        if n["qn"] in accent_q:
            bumps.append((n["qn"], ACCENT_BUMP, 0.3))

    # c02: phrase shaping on long notes (C5) and anti-bloom on soft re-struck string chords (B6), in CC11 units
    contours = []   # (start, end, kind)

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
            if e >= END - 3.5 or q0 >= 298:   # the final bars have their own fade
                continue
            inside = [o for o in onsets if q0 + EPS < o < e - EPS]
            in_hp = any(a < e - EPS and b > q0 + EPS for a, b, k in hps)
            sec = qn_to_sec(e) - qn_to_sec(q0)
            prevs = [o for o in ns if abs(orig_end[id(o)] - q0) < 0.05 and o["qn"] < q0 - EPS]
            same_pitch = any(o["pitch"] == n["pitch"] for o in prevs)
            if family == "string" and n.get("art") == "Sus MAX" and base(q0) <= DYN["p"] + 2 and prevs and not inside:
                contours.append((q0, e, "bloom"))
                continue
            if in_hp or inside or same_pitch:
                continue
            # c13 (A #2): a slur's last note is not a phrase end when the next note joins it (Leg BC / BC_SOFT
            # bow change): the line goes on, so no taper into the join
            ends_phrase = (n["slur"] is not None and slurs[n["slur"]][1] <= q0 + EPS and not joined_next(n)) \
                or near(e, breath_q) or round(e, 4) in rest1
            if sec >= 1.8:
                contours.append((q0, e, "swell_taper" if ends_phrase else "swell"))
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
        if q >= 303.5 and v > 8:   # c02: the final ppp chord dies away (with the volume fade in vol_db)
            v += (8 - v) * min(1.0, (q - 303.5) / 0.5)   # c07 (C #5): from 303.5 (was 302 -> 304)
        return v

    breaks = [p[0] for p in pts] + [x for a, b, _ in boost_spans for x in (a, b)] + [x for b0, _, ln in bumps for x in (b0, b0 + ln)] \
        + [x for h0, h1, _ in holds for x in (h0, h0 + 0.1, h1)] \
        + [x for a, b, _ in contours for x in (a, b, a + 0.4 * (b - a), a + 0.5 * (b - a), min(b, a + 1))] + [302, 303.5, 304] \
        + [x for nq, _ in notches for x in (nq - 0.06, nq, nq + 0.25)] \
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
    pulls = []   # (start, end): CC11 holds the entry's own level from the moved onset to the score onset
    div_entries = []
    extra_used = []
    el = {float(k): v for k, v in ENTRY_LEADS.get(tname, {}).items() if not k.startswith("_")}

    def extra_s(q):   # c07 (C #2b)
        return next((v for k, v in el.items() if abs(q - k) < 0.02), 0.0)
    ll = {float(k): v for k, v in LEG_LEADS.get(tname, {}).items() if not k.startswith("_")}
    leg_used = []
    for n in ns:
        q = n["qn"]
        if n.get("leg_target") and not n.get("grace") and not n.get("run") and leg_s > 0:
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
                tot = ls_ + ex if lx is None else max(LEG_LEAD_CLAMP[0], min(LEG_LEAD_CLAMP[1], ls_ + ex))
                L = min(lead_qn(q, tot), 0.45 * (q - pv["qn"]))
            shift[id(n)] = L
        elif n.get("sost_rep") or (n.get("sost_sus") and any(o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.05
                                                              for o in ns)):
            # c07 (A #1): a re-tongued note under "Largamente" (repeated pitch, or an unslurred tenuto): 0.04 s early
            shift[id(n)] = lead_qn(q, SOST_REP_S)   # a same-pitch overlap is cut by the note-end guard below
        elif n.get("fresh") and ent_s:
            # c09 (A #3): the section entering after the solo (Vln I qn 65): the family entry lead; the solo's last
            # note is cut 0.03 qn before the moved onset below, so the monophonic legato patch does not join them
            s_ = min(ENTRY_CAP_S, (ent_s[0] if final(q) <= 50 else ent_s[1]) + extra_s(q))
            L = lead_qn(q, s_)
            shift[id(n)] = L
            pulls.append((q - L, q))
        elif not n.get("leg_target") and n.get("art") and "Accent" not in n["art"] \
                and any(w in n["art"] for w in ("Sus", "Leg Slur", "Flautando", "Tremolo")) and q > -EPS \
                and (ent_s or extra_s(q)) and (q > 0.5 or family == "string" or extra_s(q)):
            # (before qn 0.5 only strings and listed entries: Horn 3's opening measured on time with no lead)
            # c07 (C #2a): qn 0 is included (the lead starts inside the pre-roll); C #2b: entry_leads.json extra
            xs = extra_s(q)
            s_ = min(ENTRY_CAP_S, ((ent_s[0] if final(q) <= 50 else ent_s[1]) if ent_s else 0.0) + xs)
            pe = prev_end(q)
            if pe is not None and (q - pe >= 0.5 - EPS or (xs and q - pe >= 0.2 - EPS)):
                L = min(lead_qn(q, s_), q + PREROLL_QN - 0.5)
                if pe >= 0:
                    L = min(L, q - pe - 0.02)
                shift[id(n)] = L
                pulls.append((q - L, q))
                if xs:
                    extra_used.append(round(q, 3))
            elif ent_s and family == "string" and n["art"] == "Sus MAX" and not n.get("short_sus") \
                    and any(("Leg" in (o.get("art") or "") or tname in DIV_JOIN_TRACKS)
                            and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1 for o in ns) \
                    and (tname not in DIV_JOIN_TRACKS or final(q) < DYN["f"] - 2
                         or any("Leg" in (o.get("art") or "") and o["qn"] < q - EPS and abs(orig_end[id(o)] - q) < 0.1
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
                                and o["pitch"] not in newp and o["end"] < q + 0.03:
                            o["end"] = q + 0.03
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
    pulls = sorted(set(pulls))

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
        got = value_at(pts, q + 0.001)
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
        v11 = final2(q)
        if not vib_fam:
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
            if dip:
                x = (q - n["qn"]) / (e - n["qn"])
                if x < 0.4:
                    return tgt - dip + dip * x / 0.4
            return tgt
        return value_at([(22, 38), (34, 42), (46, 55), (58, 62), (72, 72), (88, 90), (114, 98), (124, 100)], v11)
    vbr = breaks + [x for n in ns for x in (n["qn"], n["qn"] + 0.4 * (orig_end[id(n)] - n["qn"]))]
    cc1 = sample(cc1_fn, vbr) if ns else []
    cc7 = []
    timp_hp = []   # c13 (A #3)
    vol_parts = []   # c02: exact level offsets in dB, written as a track volume envelope by build_reaper.py
    if family in ("harp", "harm"):
        cc11, cc1 = [(0.0, 110)], []
    if family == "timp":  # the timpani patch has no CC11; CC7 per articulation (c01); the roll settle is in vol_db (c02)
        # c02: mf/f/ff +4 (the tutti rolls keep their level after the -4 dB track gain change); ppp/pp drop 4 dB net
        # c06 (C #4): ff -14 -> -11 and fff -12 -> -9 (the bar 61 ff roll was only 1.4 dB over the bar 79 f roll)
        roll_db = [(22, -36), (34, -31), (46, -26), (58, -23), (72, -17), (88, -16), (114, -11), (124, -9)]

        def timp_db(n, q):
            dbv = value_at(roll_db, base(q))
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
        # c10 (B #2): rolls and strokes printed f or louder start at their dynamic: +TIMP_LOUD_ATTACK_DB from the onset
        # (10 ms rise), held 0.25 qn, gone by 0.75 qn (before the settle has fallen 1.3 dB). The roll body is unchanged.
        for n in ns:
            q = n["qn"]
            if base(q + 0.01) >= DYN["f"]:
                vol_parts.append(("env", [(q - 0.01, 0.0), (q + 0.01 * bpm_at(q) / 60, TIMP_LOUD_ATTACK_DB),
                                          (q + 0.25, TIMP_LOUD_ATTACK_DB), (q + 0.75, 0.0)], True))

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
                v += value_at([(303.0, 0.0), (303.5, -2.0), (304.0, -10.0)], q) if q >= 303.0 else 0.0
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
            vol_parts.append(("span", a, b2, dbv, er))
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
        vol_parts.append(("env", pin + pout))
    # c06 (C #1): crescendos to f or louder rise in dB too
    hp_chained = []
    if family in HP_GAIN_DB:
        for a, b2, k in hps:
            mfa = k == "cresc" and DYN["mf"] - 2 <= base(b2 - 0.01) < DYN["f"] - 2   # c11 (B #3)
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
                vol_parts.append(["hpgain", a, b2, hold_end, g_, 0.0, HP_REL, sost_end, SOST_HOLD_SHARE * g_, mfa])
        # c09 (B #1): chain consecutive crescendos to f+ (no softer printed mark between the first arrival and the
        # second start): the first holds its gain to the second's start without a release, the second starts from it
        hpi = sorted([it for it in vol_parts if it[0] == "hpgain"], key=lambda it: it[1])
        for it1, it2 in zip(hpi, hpi[1:]):
            b1, a2 = it1[2], it2[1]
            if not it1[9] and -EPS <= a2 - b1 <= HP_CHAIN and not any(b1 + EPS < mq < a2 - EPS and DYN[d_] < base(b1 - 0.01)
                                                       for mq, d_ in marks if d_ in DYN) \
                    and not any(k_ == "decresc" and b1 - EPS <= a_ < a2 - EPS for a_, b_, k_ in hps):
                it1[3], it1[6] = a2, 0.0
                it2[5] = it1[4]
                # c11: max() so a chain from a smaller mf-arrival gain (HP_GAIN_MF_DB) keeps the f+ crescendo's own gain
                it2[4] = max(it2[4], it1[4] + HP_CHAIN_RISE.get(family, 0.0) * HP_GAIN_DB[family])   # c10 (C #3)
                hp_chained.append(round(a2, 3))
    # c06 (C #5): the long-note swell in dB (same notes as the CC11 swell)
    for a, b2, k in contours:
        if k.startswith("swell"):
            vol_parts.append(("swell_db", a, b2, k == "swell_taper"))
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

    def trim_shape(n, dbv, ramp, early=None):
        """c09 (A #2): the dB shape of a note trim. A joined note's trim starts at its moved onset (crossfading in over
        [moved - 0.05, moved + 0.03]); a trim on a note that another note follows ends over [next moved onset - 0.05,
        + 0.03], so the next note's (early) legato transition no longer plays under it."""
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
    for n in ns:
        if n["pitch"] not in pt:
            continue
        art_ = n.get("art") or ""
        ok = (art_ in arts_only) if arts_only else (allart or n["pitch"] in allp or "Leg" in art_)
        if not ok:
            continue
        # c09 (B #2): the c08 cut of long-note trims at onset + 3 qn is removed (it put +5 dB steps into held pp Cb
        # pedals); the bar 83 Cb lift is a role in roles.json instead
        v_ = pt[n["pitch"]]
        if "izz" in art_ and not isinstance(v_, dict):
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
            vol_parts.append(("env", trim_shape(n, None, 0.25, (v_["early"], v_["body"]))))
        else:
            vol_parts.append(("env", trim_shape(n, v_, 0.25)))
        pitch_trimmed += 1
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
                vol_parts.append(("env", p0 + [(sec_qn(q0, H_), X), (sec_qn(q0, H_ + 0.25), 0.0)], True))
            else:
                vol_parts.append(("env", [(q0 - 0.02, 0.0), (sec_qn(q0, 0.05), hit[0]), (sec_qn(q0, 0.35), hit[0]),
                                          (sec_qn(q0, 0.6), 0.0)]))
            early_n += 1
    # c09 (A #5): loud accents get weight in dB (CC11 hardly moves at the top of its range): +ACCENT_DB, 30 ms rise
    acc_n, acc_done = 0, []
    if family in ("wind", "brass", "string"):
        for n in ns:
            is_sf = any(abs(n["qn"] - m_) < 0.01 for m_ in sf_q) and value_at(pts, n["qn"] - 0.01) >= DYN["f"]
            if ((n["qn"] in accent_q and base(n["qn"]) >= DYN["f"] - 4) or is_sf) \
                    and not any(abs(n["qn"] - x_) < EPS for x_ in acc_done):   # c10 (C #4c): a loud sf too; once per chord
                q0 = n["qn"]
                acc_done.append(q0)
                ov = next((v_ for k_, v_ in ACCENT_DB_AT.get(tname, {}).items() if abs(q0 - k_) < 0.02), None)
                if ov is not None:   # c11 (A #3)
                    vol_parts.append(("env", [(q0 - 0.01, 0.0), (q0 + 0.01 * bpm_at(q0) / 60, ov), (q0 + 0.12, ov),
                                              (q0 + 0.3, 0.0)], True))
                else:
                    vol_parts.append(("env", [(q0 - 0.02, 0.0), (sec_qn(q0, 0.03), ACCENT_DB), (sec_qn(q0, 0.25), ACCENT_DB),
                                              (sec_qn(q0, 0.5), 0.0)]))
                acc_n += 1
    # c03 (B #4): note trims keyed by onset (qn), matched within 0.02 qn, no length cutoff
    nt = {float(k): v for k, v in NOTE_TRIMS.get(tname, {}).items() if not k.startswith("_")}
    for n in ns:
        hit = [v for k, v in nt.items() if abs(n["qn"] - k) < 0.02]
        if hit:
            sec = qn_to_sec(orig_end[id(n)]) - qn_to_sec(n["qn"])
            ramp = 0.6 * (orig_end[id(n)] - n["qn"]) / sec   # 0.6 s in qn
            vol_parts.append(("env", trim_shape(n, hit[0], ramp)))   # c09 (A #2): ends at the next moved onset
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
    for n in ns:   # c04 (A #2): the kept note of a same-patch unison
        b_ = UNI_BOOST.get(tname, {}).get((round(n["qn"], 3), n["pitch"]))
        if b_:
            vol_parts.append(("note", n["qn"], orig_end[id(n)], b_, 0.02))
    # c03 (B #2): divisi chords and double stops play a full-section sample per note. Where k >= 2 notes sound together:
    # -10 log10(k) dB under "div.", -1.5 dB otherwise (non div. double stops); 2-note tremolo chords a further -3 dB.
    # The cut starts 0.1 qn before the chord.
    chord_segs = []
    if family == "string":
        def div_state(q):
            st = None
            for tq, t in sorted(texts_until(staves, q)):
                if "non div" in t:
                    st = "non"
                elif has(t, "div."):
                    st = "div"
                elif has(t, "unis"):
                    st = None
            return st
        bnds = sorted({round(n["qn"], 4) for n in ns} | {round(orig_end[id(n)], 4) for n in ns}
                      | {round(x, 4) for o in split_away for x in (o["qn"], o["end"])})   # c13 (A #1)
        for a_, b_ in zip(bnds, bnds[1:]):
            mid = (a_ + b_) / 2
            snd = [n for n in ns if n["qn"] <= mid < orig_end[id(n)]]
            k = len(snd) + sum(1 for o in split_away if o["qn"] <= mid < o["end"])   # c13 (A #1)
            if k < 2:
                continue
            dbv = -10 * __import__("math").log10(k) if div_state(mid) == "div" else -1.5
            if all(n.get("art") == "Tremolo" for n in snd):
                dbv -= 3
            chord_segs.append((a_, b_, dbv))
        if chord_segs:
            vol_parts.append(("chord",))

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
        vol_parts.append(("fade",))
    vbreaks = [0.0, 303.0, 303.5, 304.0]
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
    vgrid = sorted(set([round(x, 4) for x in vbreaks] + [round(i * 0.25, 4) for i in range(int((END + 4) / 0.25))]))
    # c10: "env" items flagged exact put their breakpoints into parts.json vol_bp; build_reaper.py adds them to the volume
    # envelope's 0.125 qn grid, so shapes faster than the grid (pre-onset fills, the timpani attack) are written as built
    vol_bp = sorted({round(x, 4) for item in vol_parts if item[0] == "env" and len(item) > 2 and item[2]
                     for x, _ in item[1]})
    vol_db, last = [], None
    for q in vgrid:
        v = round(vol(q), 2)
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
        if tname in TRACK_WINDOWS and TRACK_WINDOWS[tname][2]:
            cc15 = [c for c in cc15 if c[0] < TRACK_WINDOWS[tname][1] - 0.5]
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
        out_notes.append({"qn": round(q1, 4), "dur": round(max(0.02, e - q1), 4), "pitch": n["pitch"], "vel": n["vel"],
                          "sq": round(n["qn"], 4), "_art": n.get("art")})   # sq: score onset (analysis only)
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
    # c05 (A #2): a keyswitch to a non-legato articulation must not fall inside a sounding legato-patch note (the
    # monophonic legato voice was still held at the bar 61 tremolo keyswitch). End such a note 0.01 qn before it.
    ks_cut = 0
    for k_ in ks:
        if "Leg" in k_["art"]:
            continue
        for a in out_notes:
            if a["_art"] and "Leg" in a["_art"] and a["qn"] + EPS < k_["qn"] < a["qn"] + a["dur"] - EPS:
                a["dur"] = round(max(0.02, k_["qn"] - 0.01 - a["qn"]), 4)
                ks_cut += 1
    if ks_cut:
        print(f"  {tname}: {ks_cut} legato notes ended before a keyswitch", file=sys.stderr)
    fresh_on = [(new_on(n), n["qn"]) for n in ns if n.get("fresh") and id(n) in shift]
    for f_, fsq in fresh_on:   # c09 (A #3); compared on sq and with a 0.001 tolerance (out_notes qn are rounded:
        for a in out_notes:    # the first version cut the fresh note itself to 0.02 qn)
            if a["sq"] < fsq - 0.001 and a["qn"] < f_ - 0.001 and a["qn"] + a["dur"] > f_ - 0.03:
                a["dur"] = round(max(0.02, f_ - 0.03 - a["qn"]), 4)
    for a in out_notes:
        a.pop("_art")
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
        "pitch_trimmed": pitch_trimmed, "early_fills": early_n, "div_entries": div_entries, "extra_leads": extra_used, "leg_leads": leg_used, "port": port_done, "bcsoft": bcsoft_n,
        "hpgain": [[round(i[1], 3), round(i[2], 3), i[4]] for i in vol_parts if i[0] == "hpgain"],
        "hp_chained": hp_chained, "bc_skipped": bc_skipped, "roles_chained": role_chained, "accent_db": acc_n,
        "ks": ks, "cc1": cc1, "cc11": cc11, "cc15": cc15, "cc7": cc7, "cc70": cc70, "dyn_curve": dyn_curve, "vol_db": vol_db, "vol_bp": vol_bp,
        "hairpins": [[round(a, 4), round(b, 4), k] for a, b, k in hps],
        "range": [min(pitches), max(pitches)] if pitches else None,
        "ks_clash": clash,
        "art_counts": dict(collections.Counter(n.get("art") for n in ns)),
    }


# c04 (A #2): two tracks on the same patch file playing the same pitch together render the identical sample (Hn1+Hn2
# at the climax measured a correlation of 0.999; Cl1+Cl2 at qn 259 partly cancelled). Keep the longer note (the earlier
# track on a tie; a slurred note before both), drop the copies, and raise the kept note by 10 log10(copies) dB.
UNI_DROP, UNI_BOOST = collections.defaultdict(set), collections.defaultdict(dict)


def find_unisons():
    by_patch = collections.defaultdict(list)
    for t in TRACKS:
        if t[3] in ("wind", "brass"):
            by_patch[t[2]].append(t)
    for patch, ts in by_patch.items():
        if len(ts) < 2:
            continue
        allnotes = [(t[0], n) for t in ts for s_ in t[1] for n in notes[s_]]
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
            keep = max(grp, key=lambda x: (slurred(x), x[1]["end"] - x[1]["qn"], -order.index(x[0])))
            if any(x[1]["end"] > keep[1]["end"] + 1.0 + EPS for x in grp):
                # a copy that holds on more than 1 qn after the kept note would leave a hole in its own part
                print(f"  unison qn {na['qn']:.2f} pitch {na['pitch']}: left (a copy holds > 1 qn longer)", file=sys.stderr)
                for tb, nb in grp:
                    seen.add((tb, nb["qn"], nb["pitch"]))
                continue
            for tb, nb in grp:
                seen.add((tb, nb["qn"], nb["pitch"]))
                if tb != keep[0]:
                    UNI_DROP[tb].add((round(nb["qn"], 3), nb["pitch"]))
            UNI_BOOST[keep[0]][(round(keep[1]["qn"], 3), keep[1]["pitch"])] = round(10 * __import__("math").log10(len(grp)), 2)
            print(f"  unison qn {na['qn']:.2f} pitch {na['pitch']}: keep {keep[0]}, drop "
                  f"{[tb for tb, _ in grp if tb != keep[0]]}", file=sys.stderr)


find_unisons()
parts = [build_track(*t) for t in TRACKS]
json.dump({"tpb": TPB, "end_qn": END, "preroll_qn": PREROLL_QN, "preroll_bpm": PREROLL_BPM, "tempo": tempo, "timesig": timesig, "tracks": parts}, open(OUT, "w"), indent=1)
for p in parts:
    print(f'{p["name"]:15s} notes={len(p["notes"]):4d} ks={len(p["ks"]):3d} cc11={len(p["cc11"]):4d} range={p["range"]} clash={p["ks_clash"]} {p["art_counts"]} leads={p["leads"]} notches={p["notches"]} uni_drop={p["unison_dropped"]} bloomv={p["bloomv"]} pitch_trim={p["pitch_trimmed"]} div_ent={p["div_entries"]} extra={p["extra_leads"]} bcsoft={p["bcsoft"]} hpgain={len(p["hpgain"])} hp_chain={p["hp_chained"]} bc_skip={p["bc_skipped"]} roles_chained={p["roles_chained"]} acc_db={p["accent_db"]}')
