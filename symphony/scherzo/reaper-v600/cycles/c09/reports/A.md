# Cycle 9, critic A: articulation and phrasing (render c08)

All measurements are on `cycles/c08/render/` (stems 01-31 after the c08 stem fix, `00_Master.wav`) with `build/parts.json` (identical to what c08 rendered except the Violins II stem-fix role) and its tempo map. "Stem" means a dry stem and "master" means `00_Master.wav`. pcX is `tools/pcx.py` (perceived attack on harmonic bands, ms against the score beat). Only c08 still has stems (c00-c07 keep their masters only), so comparisons with earlier cycles use their `metrics/attacks.txt` and parts.json. Scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c09-A/` (deleted at the end).

## Manual notes (cycle 9 slot A: group A2, May 2021 HO manual PDF pp. 95-99, string effects and legato; plus MANUAL-GAPS.md)

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Pre-recorded runs, one octave, in 1st Violins, Violas and Celli only (p.95-96) | nothing: the scherzo has no scale runs | n/a |
| Repetitions Runs script: velocity ignored, CC11 sets loudness, the samples are repetitions (p.96) | nothing | n/a |
| Slur Runs (1st and 2nd Violins): the fast notes, the slurs and the sustained notes of a run in one patch; CC1 picks 3 vibrato levels, CC11 picks 5 dynamics, velocity does not set loudness; for speeds of sixteenths at about 125 bpm or faster (p.96-97) | the Violins I theme-head tails (accented half note slurred into two eighths, `g''2->( fis''8 f''8 \| e''4-.)`): the eighths at quarter 264 run as fast as sixteenths at 132 | Not used (15 thousand regions on 1st Violins, MANUAL-GAPS #16). It is a fallback for finding 1. |
| Spiccato Runs, 2nd Violins only, steps of a whole tone or less (p.97) | nothing (Violins II's con sord. quaver arpeggios of 168-196 leap) | n/a |
| Unmeasured and measured (TS) tremolo; CC11, not velocity (p.97-98) | no string tremolo is printed | n/a |
| Trills (p.98) | none | n/a |
| Repetitions, Violas and Basses only: about a dozen tempo-synced pulses in a little over 1 s, CC11 crossfades 3 layers (p.98) | the repeated-eighth pairs are only two notes | Not used, correctly. The pairs separate on the short rows (master pair dips: theme A median 3.7 dB, counterstatement 4.5, fugato 5.7, tuttis 5.0 / 4.8, reprise 4.3, coda 5.1; measured). |
| Sul ponticello, Violas only (p.98) | not printed | n/a |
| Legato Slur and Portamento: slur legato jumps over the intervening notes, portamento slides through them; a transition needs "no significant time gap"; Basses have Legato Slur only (p.98-99) | every slurred string line; Violins I "port." at bar 214 (qn 639-640) | Slur: yes. Port.: since c08 it is a Leg Slur MAX target at v55, because Leg Port MAX was unloaded for memory. So the printed glide plays as a slur. This partly follows the manual and is a known memory trade. |
| "By default, all legato instruments are monophonic"; CC22 switches mono/poly (p.99 says 64-127 is poly; 2025 p.91 and 2021 p.105, p.112, p.144 say 64-127 is mono, 0-63 poly) | every Leg row; the violas' legato passages (finding 3) | The pipeline never sends CC22, so each instance runs in whatever mono/poly state it loaded or saved (finding 3). |
| Legato Slur Staccato adds a slur-staccato accent to notes with no legato connection (p.99) | the first note of each legato phrase; the theme heads | Not used (54 thousand regions on 1st Violins, MANUAL-GAPS #16). |
| Legato Bow Change, alone or with slur / portamento; Opus picks the component from the MIDI (p.99) | Leg BC MAX on Violins I and celli; violas and Violins II remapped to Leg Slur plus a notch (c02 `ROW_REMAP`) | Follows. |
| Keyswitch Masters switch articulations by key (p.99) | all 31 tracks | Follows. No keyswitch lands within 3 ms before or after a note-on on any track (measured: 0 cases), and no Leg row receives a chord. |

## Findings, ranked by what a listener would hear

### 1. Violins I: the two slurred eighths after the accented half note still disappear in 6 of 9 soft theme heads (measured)

Where: theme A and the reprise, Violins I. The heads are the half notes at qn 39, 51, 69, 75, 285, 759, 771, 789 and 795, and the tails are the eighths at head + 2 and head + 2.5. The score is `g''2->( fis''8 f''8 | e''4-.)`, so the tails are slurred, non-first notes in the half note's bow.

What is wrong: c08 A #1 raised the tails' velocity to 88 / 85. They still play as Sus MAX re-attacks of 0.114 s at CC11 53-65. At p a Sus MAX attack has not reached its body by the time the next note starts. The melody therefore drops one or two notes every two bars.

Evidence (stem RMS over each eighth slot against the half note's body from +0.15 s to its end; the c08 pass mark was within 8 dB):

| head qn | 39 | 51 | 69 | 75 | 285 | 759 | 771 | 789 | 795 |
|---|---|---|---|---|---|---|---|---|---|
| first eighth (dB) | -8.4 | -7.1 | **-16.9** | -8.4 | -3.9 | -8.8 | -6.7 | **-14.3** | -8.6 |
| second eighth (dB) | -10.6 | -2.9 | **-14.0** | -10.1 | -6.0 | -3.3 | -9.8 | **-11.9** | -10.6 |

At bar 24 (qn 69-72) the stem reads -25..-34 dB on the half note, -45..-54 on the tails, and -34..-40 on the staccato quarter after them. The tails are 10-15 dB under the note that follows them, not only under the accent before them. The same figure on the violas (183 / 879: -1.6..-2.9 dB) and in the tuttis at v100 (-3.5..-8) speaks.

Fix (c08 A #1's planned fallback; `build/score_config.py`): play the tails as legato targets of the half note.
- `SHORT_SUS_LEG_TRACKS = ("Violins I",)` and `SHORT_SUS_LEG_S = (0.10, 0.25)`. At quarter 264 an eighth lasts 0.114 s, under the default 0.20 minimum.
- Limit the change to the soft heads. The Sus MAX eighths at f/ff in 113-143, 209, 317-371, 589-596, 821-953 and 980-1005 measure fine. Put every Violins I eighth onset in those spans into `SHORT_SUS_LEG_SKIP["Violins I"]`, or test `SHORT_SUS_LEG_SKIP` with only the 18 tail onsets left out: 41/41.5, 53/53.5, 71/71.5, 77/77.5, 287/287.5, 761/761.5, 773/773.5, 791/791.5, 797/797.5.
- Keep the tails' v88 / v85, which now also sets the legato speed.
- Inferred risk: the half note plays on Sus Marc LITE, and it is not measured whether the KS Master's legato script joins a Leg Slur target to a note on another row. If the first tail still reads under -8 dB, move the whole figure (half note and tails) to Leg Slur MAX for heads 69 and 789 only, and leave the accent to the GENTLE_ACCENT swell (c07 A #2's A/B).
- Pass: both eighths within 8 dB of the half-note body, and not more than 6 dB under the staccato quarter that follows.

### 2. Celli: legato sags of 8-13 dB in the trio tune and the tenor lines (measured); `auto_fills.py` finds them, but c04 dropped its celli fills

Where (Violoncellos, Leg Slur MAX joins): 542 (bar 181, trio tune T, at the top of a crescendo) 13.2 dB, 645 10.7, 576 10.4, 573 8.9, 768 8.4, 507 7.9, 588 7.0, 600 6.5, 626 6.3, 390 6.0, 317 5.9, 917 5.9, 546 5.8, 939 5.7, 339 5.4, 777 7.3, 794 7.2, 1053 7.6. These are `tools/auto_fills.py 8 build/parts.json` (plan only, no `--write`) on the c08 stems: 17 celli joins of 5 dB or more. On the same pass the wind lines had already been filled (only a few raises left).

Evidence: at 542 the stem reads -38.6 / -41.3 dB before the join and -38.9 / -37.8 after it, against -50.2 dB at 542.375-542.5, about 0.15 s long. CC11 and vol_db rise through the join (CC11 68 -> 79, vol +0.5 -> +2.0), so the hole comes from the transition sample, not from the envelope. On the master it is a 4.9 dB hole (-36.0 at 541.5-541.75, -40.9 at 542.375) in bar 181. At that point the celli carry the tune, with Violins I doubling it an octave up from bar 177 and Violins II muted. At 576 the master dips 3-4 dB. Celli joins elsewhere measure a median 1-2.5 dB.

Fix: `tools/auto_fills.py 8 build/parts.json --write`, after the parts.json for c09 is otherwise final. "Violoncellos" is in the default TRACKS, and `build/auto_fills.json` is `{}`. The tool proposes fills of 2.4-6 dB held 0.12-0.35 s (542: 6 dB, hold 0.14 s; 645: 6 dB, 0.16 s; 576: 6 dB, 0.35 s). c04 did not keep its 17 celli fills and recorded no reason. If a reason was a transition spike under a fill (LEARNINGS section 5), check each new celli fill against the 30 ms peak after the render, as the tool's overshoot rule does for existing fills. The same plan also raises Oboe 1 681 (+5.3), Clarinet 1 598 (+6.8) and Horn 1 598 (+7.9), and removes Clarinet 1 578 and Horn 1 1077 (Horn 1 1077's existing fill stands +12.6 dB over the previous body - 1.5 dB in the motto tail's decrescendo). Accept those too.

### 3. Violas legato probe (window 115 ms): the early joins are all the loud ones, at v118-124 (measured). Neither the parked CC11 nor the data explains it (measured); the likely cause is the instance's legato state (inferred)

Where: Violas Leg Slur MAX joins in 133-162, 390, 582-598 and 858.

Evidence:
- pcX by target velocity (c08 stems):
  - v112 and above: n = 31, median **-86 ms**, window 122 ms.
  - v96-111: n = 17, +14 ms.
  - v95 and below: n = 19, +13 ms.
  - Every join gets the same lead: 0.225 s (`LEG_LEAD_S` 0.20 + `LEG_ART_EXTRA_S` 0.025).
  - Violins I, Violins II and celli at v112 and above read +36, +1 and +23 ms. Their leads at those velocities are 0.150-0.167 s, refined by 42-61 per-onset `leg_leads.json` entries each; the violas have 7.
- In the early joins the new pitch reaches 6 dB under its peak 0.04-0.18 s after the moved note-on (145.5: 0.058 s, 146: 0.042, 152: 0.074, 161: 0.054). At v90-100 that takes 0.17-0.56 s. The old pitch is still within 10 dB of its level until +0.17..+0.34 s, so both pitches sound together for 0.1-0.2 s. That fits the actor's "about 3 dB louder" for two voices summing, and it reads more like overlapped separate notes than a slurred transition.
- 390 and 858 (the same bars in the statement and the reprise) read identically: pcX -142 ms, crossover -65 ms, window 166 ms. Within a render this is deterministic.
- Not the CC11 park: 582-609 is early as well, and the violas' last park before it ends at 395.1, 187 qn earlier.
- Not the data: in 132-163, c08's notes, keyswitches, CC11 and CC1 equal c07's rendered parts.json. vol_db differs only by the beat weight at 132.0-132.4.
- The same flip happened before: c04 read 116 ms (pcX -22) with unchanged data; c05-c07 read 92 / 88 / 88.
- In c08 the Violas instance was not rebuilt, so it carried its saved Opus state from c07. Violins I and II were rebuilt.
- The violas' LegatoSpeed velocity offset is at most 2,173 samples (Violas KS Master .oib, VELO 41-127 -> START 0-2173), about 45 ms between v41 and v127. That is about 13-17 ms between v100 and v124, too small to explain a shift of about 100 ms.
- The manual's mono/poly switch (p.99; polarity per 2025 p.91) is the one legato control the pipeline never sets.

Fix:
- (a) Pin the true-legato mode. Add a generic `LEGATO_MONO_CC22 = True` that writes a "cc22" lane `[[0.0, 127]]` (mono, per 2025 p.91 and 2021 p.144) in the pre-roll on every track that loads a Leg row. build_reaper writes it like cc15 / cc70, and the lane ends on its resting 127. This costs nothing if the state is already mono.
- (b) Test it with the one-track test render (loop LEARNINGS c08, about 5 min) before the full render. Pass: the v112+ violas joins come within ±40 ms of the v96-111 joins, and the window median is 90 ms or less.
- (c) If (b) does not move them, the cause is the f/ff transition speed itself. Fit violas per-onset entries in `build/leg_leads.json` from these c08 pcX values with half the usual gain: `total = old + 0.5 × (pc - 0.02 s)`, clipped to ±0.12 s, only for joins with |pc| > 0.06 s (for example 145.5, 146, 148, 150, 154, 390, 582, 588, 590, 591, 594, 598, 600, 609, 858 at -0.05..-0.08 s). Half gain is chosen because the state has flipped back before (c04 -> c05), and a full refit would then leave these joins about 40 ms late.

### 4. Celli trio-tune entry at bar 169 (qn 504) is perceived +287 ms late. The basses' soft arco entries at 504 and 1071 are +144 ms (measured)

Where: Violoncellos 504.0 (arco, espress., p, the first note of T in the celli, Leg Slur MAX first note, v63). Double basses 504.0 and 1071.0 (arco, pp, Sus MAX v41).

Evidence:
- pcX: celli 504 +287 ms. Basses 504 +144 and 1071 +144.
- At quarter 228 an eighth lasts 0.13 s, so the celli tune starts more than an eighth late.
- Every other arco entry after pizz. is within -44..+80 ms: celli 90 -13, 300 +32, 756 +29, 828 +7; basses 90 -44, 300 +12, 576 -33, 624 +80, 840 +63. The pizz. entries read -7..+51 ms.
- The celli note sounds from its moved onset 0.165 s early, but grows slowly. Its harmonic band level rises +5 dB at the beat, +14 at +0.1 s, +22 at +0.3 s and peaks at +0.45 s.
- The note already carries `entry_leads` 0.06 and `note_trims` +5 (c06).
- The kit (LEARNINGS section 6, Movement I c23) found that lead alone only makes the quiet part earlier. Lead plus a short fill brought soft string entries to +0.1..+0.3 s.

Fix:
- `build/early_fills.json` Violoncellos `"504.0": {"db": 4.0, "pre_s": 0.10, "hold_s": 0.35}`, and `build/entry_leads.json` Violoncellos 504.0 0.06 -> 0.12 (total lead about 0.225 s, under the kit's 0.30 s cap).
- Basses 504.0 and 1071.0: `entry_leads` 0.06 each, and `VEL_SET["Double basses"]` 53 at both. The basses' soft arco entry at 576, at v53, reads -33 ms, against +144 ms for the two at v41. That velocity is the speed of attack is inferred, not measured on these notes.
- Pass: pcX under +100 ms for the celli and under +80 for the basses, with no overshoot over the second note's body (kit section 6 overshoot rule).

### 5. Reprise: two of the theme's repeated-eighth pairs are masked by celli transition spikes (S1, measured)

Where: qn 763.5 (bar 255) and 799.5 (bar 267), Violins I's B-B pairs in the reprise, against the celli's espress. arco line from 756.

Evidence:
- Master pair dips at these two pairs are 2.5 and 2.0 dB. The reprise median is 4.3 dB and the theme A median 3.7.
- In the 40 ms gap before the second eighth the celli carry 25 % / 31 % of the dry stems' energy, and they are louder in the gap than at the eighth's attack (+4.4 / +2.1 dB).
- The celli stem shows a transition peak exactly there:
  - At 763.0-763.5 the stem reads -36.3..-37.1 dB, against -40.0 before and -42.4..-42.7 after. This is the join into 764 (moved to 763.032).
  - At 799.1-799.6 it reads -36.9..-38.8, against -44.8 and -42.3 (the join into 800, moved to 799.032).
  - Both joins are on time (pcX -29 / -24 ms). The peaks are the sample's transition spikes (LEARNINGS section 5: about 1 join in 10).

Fix (`build/score_config.py`, the existing generic `JOIN_NOTCH`): `JOIN_NOTCH = {"Violoncellos": [(763.05, 763.55, -4.0), (799.05, 799.6, -4.5)]}`. Its 0.04 qn ramps are part of the rule. Spike minus 2 dB is the kit's depth.

Pass: master dips of 3 dB or more at 763.5 and 799.5, and the celli joins with no new hole over 5 dB. Check this against finding 2's fill at 794 / 768: no fill should overlap these notches.

### 6. Horn 1's printed breath at bar 217 (qn 648) is not played (measured)

Where: qn 648, the trio's return (ff). The breath is printed in Clarinet 1, bass clarinet, Bassoon 2, Horn 1 and Horn 2.

Evidence:
- Gaps before the note after the breath: Clarinet 1 86 ms, Bassoon 2 86, bass clarinet 57, Horn 2 72, Horn 1 **11 ms**.
- The Horn 1 stem has no dip: it reads -53.3 dB at 647.875 and -50.4 at 648.0, rising.
- Cause: Horn 1's 647.5-664 notes sit in the 1FH "Port Lng" `ART_SPANS` span with a `REATTACK_LEAD_AT` re-tongue lead (0.09 s, c05-c06). That lead ends the previous note 0.02 qn before the moved onset and replaces the breath gap (LEARNINGS c05, c06). The other 21 breath marks have gaps of 57-86 ms, or a rest.

Fix:
- End Horn 1's 646 note at 647.45 (`NOTE_END_AT = {"Horn 1": {646.0: 647.45}}`, the generic mvt1 c35 table, which never makes a note end later), or take 648.0 out of the Port Lng span's lead so the breath rule applies.
- Keep `BREATH_FALL_BY` Horn 10 CC.
- Pass: a gap of 0.1 s or more and a stem dip of 4 dB or more at 648. The kit's loud breath needs both a gap and a fall.

## Checked and fine (measured)

- Staccato lengths: every string and wind short row plays its quarters at 114 ms and eighths at 57 ms in every Allegro statement (104 / 52 ms in the Più mosso), so quarters and eighths are the same length everywhere.
  - Exceptions: Clarinet 1 (Leg Slur Rep slices, 149 / 66 ms), Bassoon 1 (Sus MAX, 140-174 / 78 ms) and Oboe 2 (Sus MAX, 30-68 ms), which play their few staccatos on sustain rows (c02 memory remap).
  - Their perceived attacks are on time (-7..-39 ms), but their notes fall only 4.6-6.8 dB in the 50 ms after the note end, against 8-14 dB for Flute 1 and Oboe 1 on Stac DblTng.
- Accents: 2-5 kHz energy over the first 80 ms against the body is -7..+1 dB median per track and row, and accents are +1.5..+4.5 dB over the note before (strings and winds).
  - Outliers: Violins I Sus Marc LITE heads 51 / 771 (+7.4 / +7.2 dB, the known c02 Marc LITE front) and the basses' non div. chord 213 / 897 (+8.6 / +6.9).
  - Flute 1's readings follow its pitch, not a bite.
- Pizz./arco:
  - The pizz. entries are on time (-7..+51 ms), and the harp's "étouffez" at 575.5 damps the harp by 30 dB in 0.25 s.
  - Violins II's CC15 goes on at 445.3, before 501.5, and off at 552.5. Violins II rests from 552.5 to 588, so the switch happens in a rest.
- Timpani: every roll that ends on a new note has its stroke (309, 390, 624, 858, 909, 996, 1008).
- Re-bows: Violins I's held G sharp (6.5, 1103.9, 1116.4, 1125.1) dips 2.3-5.8 dB at worst and settles within -1.9..+0.5 dB.
- Legato joins elsewhere have medians of 1-2.5 dB: Clarinet 1's trio tune, Violins I / II 624-672, the solo 1044-1068, and the second idea in Violins I.
- Not dry: the tutti staccatos still ring through the release and hall (Violins I falls only 3.1 dB in the 50 ms after the note end), and the Violins I stem pair dips stay at 5.8 dB or more in theme A and 4.6 or more in the reprise.

Do not touch: the short-row lengths and leads (quarters 114 ms and eighths 57 ms on every Stac / Staccatissimo / Spiccato / Stac DblTng / StacSs row, `STAC_LEAD_S`, `PIZZ_LEAD_S`); the c08 reprise row split and the coda pair spans (master coda pair median 5.1 dB); `SHORT_CC11_PARK` and the downbeat weight; the harp's étouffez and off-beat chords; the timpani roll-end strokes and `TIMP_DAMP_AT`; the Violins I re-bow fills; the c08 head-tail velocities (v88 / v85, kept in finding 1); every item in HISTORY's c08 do-not-touch list.
