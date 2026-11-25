# Critic A, cycle 56: articulation, joins, attacks on the c55 render (first render with no per-note volume moves)

Data used: the delivered stems and master in `cycles/c55/render/` (after the stem fix) with `cycles/c55/build_fix/parts.json`;
c54 for comparison from `cycles/c54/render/` and `cycles/c54/build_fix/`; the actor's `acc_c55_fix.json`, `acc_c54.json`,
`joinpeak_c55_fix.json`, `S_c54_fix_ref.json`, `S_c55_fix.json`; the patch files read with `opus_state.load_oib` (no REAPER).
Scratch (left in place, under 1 MB, no audio): `/private/tmp/claude-501/mockup-loop/mvt2-c56-A/` (`an1.py`, `an2.py`, `prof.py`,
`rebow2.py`, `dbl.py`, `acc.py`, `refmidi.py`, `rows.json`). No proposal below is a per-note track volume move.

## Manual and reference notes

There is no row for c56 in `loop/MANUAL-READING.md`. These are the pages and reference files the findings rest on.

| source | what it says | where it applies | does c55 follow it |
|---|---|---|---|
| HO manual 2021 p.143-144 (performance scripts) | A "Legato" script (emulated, any articulation) forces monophonic play "with no significant silence between" notes; it is switched by CC. In the string KS Masters' `controllerMap` it is CC68 ("Legato"), CC5 is "Legato Time", CC64 "Repetition: Sustain", CC69 "Repetition" | Sus MAX re-bows and Sus-to-Sus joins (basses) | never tried (kit LEARNINGS line 57: "none of these were tested") |
| p.144 (Monophonic True Legato) | velocity 50-60 gives a longer transition, 110-127 a shorter one; velocity does not change loudness | every string legato target (v124 on 430 of 460 joins) | one end of the range only |
| patch states (`.oib`) | Each legato row has sustain groups that fade in under the transition sample with their own AHDSR attack: oboe `OBs` 440 ms, cor anglais `EHs` 465, flute `1Fls` 738, violins / celli `V1s` 1054-1380, basses `Dbs` 656-1076; the transition groups (`TLeg`) have 54-116 ms. Sus MAX groups have 12-23 ms attacks, so a slow pp re-bow start is in the sample. `Legato3`: FADE_IN 180, FADE_OUT 180, OFFSET 200 | join holes and soft starts (finding 5), re-bows (finding 2) | the shipped values are in use |
| EW HO template (`eastwest-templates/hollywood-orchestra/... study copy.RPP`) | 0 track volume envelopes (`grep -c VOLENV` = 0) | whole method | c55 now 0.44-0.66 points/s on the strings |
| EW demo MIDI (`composercloud-plus/HO EW 2026 TEMPLATE DEMO MIDI.mid`, measured with `refmidi.py`) | String notes are held 4.0-4.6 s at most on 9 of 11 string tracks (one 6.0 s, two 7.9 s); no abutting same-pitch re-bows on the violins, violas or basses; CC1 moves a median 22-80 units inside every long note at 5-18 points/s | held notes | c55 re-bows 79 times at flat CC11 |
| FINDINGS section 8 (line 91), 9 (97-101, 104), 12 (157) | CC flat within 200 ms of a legato onset (no per-note bumps, no dip); string legato velocity 57-124, median 92-98; overlap 41-80 ms; keyswitches 40-800 ms ahead; patch releases left alone (931 ms on string KS Masters); repeated notes get a 60-100 ms gap | findings 4, 5, 6 | velocity 124 fixed; re-bow keyswitches 23 ms ahead; pp/p release capped at 600 / 400 ms |
| Duc, Mahler Adagietto (`bernard-duc/Duc_Bernard_Mahler_adagietto.MID`) | notes held up to 32 s with no re-bows (another library) | held notes | n/a |

## What the 302 / 379 / 613 figures are made of (measured)

- **Join holes, 379.** 45 are pizzicato decays (the script's pizzicato filter reads a note field that does not exist), 74 are
  pairs whose two bodies lie 6 dB or more apart (a level step, not a hole), 66 are same-pitch re-bows and printed repeats.
  Real pitch-change joins: **194 of 806** (c54 155). The rise of 39 sits on four tracks: Cor anglais 4 -> 14 (of 24),
  Violins II 19 -> 29 (of 102), Violoncellos 15 -> 23 (of 82), Oboe 1 9 -> 16 (of 23). Double basses Sus-to-Sus 20 of 40 in
  both renders. Fix in `acc55.py`: take the row from the last keyswitch, and count the three other classes separately.
- **Soft starts, 302.** By row: Leg Slur MAX 198 of 513 long notes (c54 110), string Sus MAX 63 of 164 (27), Flautando 7 of 16.
  String legato targets going up 58 of 116 (50 %), going down 42 of 149 (28 %); winds 48 % up, 25 % down. Thirds 55 %, seconds
  31 %. No dependence on CC11 below 100 (31-42 %); at CC11 100 or more 14 of 22. The median join is small: on 89 steady string
  joins of 1 s or more the level is 2.2-3.1 dB under the two bodies from 0.20 to 0.45 s after the note-on and back by 0.8 s;
  winds 2.5-3.1 dB from 0.10 to 0.30 s, back by 0.4 s; horns 2.5-3.0 dB from 0.15 to 0.30 s. The reference lanes are flat
  through this (FINDINGS line 91), so a 3-4 dB sag of 0.25 s is the library's legato and should stay. The audible part is
  the 71 starts of 6 dB or more (c54 32): 20 fresh soft entries on legato rows and Flautando (7-12 dB), 15 re-bows, and
  legato targets on the celli (7), Violins II (4), cor anglais (3), Bassoon 1 (3).
- **S within 25 ms, 640 -> 613: not a timing change.** The pitch crossover moved by a median 0.0 ms (2 of 727 joins over 5 ms).
  44 joins left the window and 17 entered. 27 left because the new note's level now arrives after its pitch, so S falls back
  to the crossover (+26 to +72 ms: Oboe 1 47, 190, 193.5, 198, Cor anglais 126-133.5, Violoncellos 68, 188-262); 15 because
  the level now reads early (-26 to -72 ms), where a transition burst precedes the beat (Violins I 80 -72 ms, Violins II 80
  -60, Violoncellos 77 -51). At 25 of the 44 the c54 envelope stepped 2 dB or more within 0.12 qn of the score onset
  (up to +10.3 dB), which put the level onset on the beat; c55 does so at four (Violins I 172 +2.3 and 262 -4.7,
  Violins II 220 -3.3, Violoncellos 87 +2.8: slow rows with an edge on the beat). So c54's 640 was partly made by the
  fader. The 27 late crossovers are real and were hidden: they are a lead matter (finding 5).

## Findings, ranked by audibility

### 1. Bar 63 (qn 212-216): the tutti sf arrives 3.7 dB under bar 62, and the upper strings swell again inside the printed sf > p

Where: qn 212.0-216.0, Violins I, Violins II, Violas (also Violoncellos, Double basses, Bass trombone, Flute 1 at 212.0).

Measured. Master, 212.0-212.35 against 211.0-211.9: **-3.7 dB** in c55 (-18.1 against -14.4), +0.3 dB in c54. First 0.35 s
against the note before: Violins I -0.7 dB (c54 +4.8), Violas -1.3 (+0.5), Double basses -0.4 (+4.8), Bass trombone -2.0
(+3.3), Flute 1 -4.3 (+1.4); only Violins II (+7.3) and Violoncellos (+3.7) are over their bar 62 level. After the sf the
printed marks are sf, a diminuendo hairpin from 212 and p at 216. Stem levels per quarter from 212: Violins II -25.6,
-39.8 (213), -33.3 (214), **-28.9 (214.5)**, -32.4, -36.8 (216): the level at 214.5 is 11 dB over 213.25 and within 3.3 dB
of the sf itself. Violins I -28.6, -41.7 (213), -35.2 (214.5): +6.5 dB. Violas -44.8 (213.25) to -39.9 (213.5): +4.9 dB.
c54 fell without a rise on all three. This is also the attack probe's failure (Violins I 212).

Cause (read in `build/score_config.py` lines 585-593, 699-704): c31 split the fall after the sf between a CC7 lane
(`_C31_BAR63[...]["cc7"]`, before the hall) and a `LEVEL_SHAPES` row that added the difference back (up to +9 dB at 213,
0 at 214.5), "so the product equals the c31 vol_db everywhere". c55 switched the shape off as class shape and kept the CC7
lane: CC7 goes to 45 on Violins I (-9.0 dB), 19 on Violins II (-16.5 dB), 48 on the violas (-8.5 dB) at 213 and returns to
127 by 214.5 with nothing left to carry the fall. The sf weight shapes (+2.5 / +3 dB over 212.0-212.15) are off too, and the
role boundary is back as a one-sample step under the chord at 212.000: Violins I -3.0 dB, Violins II -4.5 dB in `vol_db`
(the S3 fault c31 removed: a post-hall step that cuts the ring of bar 62).

Fix (instrument side and slow lane only):
1. `build/score_config.py`: rebuild the four `_C31_BAR63` CC7 lanes with no paired shape. Target per section: a straight
   line in dB from the sf peak to the p level reached at 216. Violins I and violas: CC7 stays 127 from 212.0 (delete the
   points after the head); simulated on the c55 stems this gives Violins I -24.5 (212.25), -29.6, -32.7 (213), -35.0,
   -35.3 (214), -35.2, -37.0 (215), -39.2 (216), monotonic; violas -28.8, -32.4, -33.2, -34.2, -37.2, -40.2. Violins II
   needs a real cut, because with CC7 at 127 its sf peak is -16.4 (12 dB over bar 62): CC7 about 75 at 212.0, 41 at 212.25,
   51 at 212.5, 71 at 213.0, 90 from 213.5 to 215.5, 127 at 216.0 (from the simulated stem against the line -25.6 to -36.8).
2. The role edges at 212.000 on Violins I and II become ramps from 212.0 to 213.0 (inside the printed hairpin and in its
   direction; a slow edge, not a step). Violins I's sf then reads -22.5 at 212.25, 2.5 dB over bar 62.
3. sf weight for the parts still under bar 62, before the hall: CC7 at 101 (-2.0 dB) over 204.0-211.95 with the bar 61-62
   section row raised 2.0 dB (a row of two bars, class slow), CC7 127 from 211.98: Violas, Violoncellos, Bass trombone,
   Flute 1. Double basses' pizzicato sf: velocity 98 -> 115 (the row follows velocity upward by about 0.15 dB per step, c55).

Expected: master 212.0-212.35 at or above 211.0-211.9 (c54 +0.3 dB), no rise of more than 1.5 dB between 212.25 and 216 on
any string stem, no one-sample step at 212.000. Decided offline: CC7 is linear amplitude before the hall (c31 comment), so
`stem x new/old CC7` is exact on the dry stems (my simulation above did this); only the Double basses' velocity needs the
full render. Also check the other half-pairs left by c55: every `CC7_POINTS` / CC11 notch whose `LEVEL_SHAPES` fill is now
off (Timpani 171.95: 8-9 dB hole 50 ms before the stroke, c54 2 dB; Clarinet 1 282.75-283: 9.0 dB, c54 3.3).

### 2. Re-bows of soft held notes: 37 of 79 stand 3 dB or more out of their own note, worst where the strings are exposed

Where: bars 1-3 (Violins I alone to qn 3), the coda and final chord (qn 286-304), Violoncellos div 274-286, Violins II and
div bars 37-40; milder on the basses' pedals (220-238, 271-286).

Measured (250 ms window, lowest level within -0.1..+1.0 s of the re-bow under the median of the two pieces; "own" = median
minus 5th percentile of the pieces away from re-bows; `rebow2.py`): soft re-bows (CC11 60 or less) median dip **7.0 dB**
(c54 2.0), own movement 3.7 dB; 37 of 79 exceed their own movement by 3 dB or more, 21 by 5 dB or more. Violins I bars 1-3:
8.4 / 8.9 / 12.1 dB (c54 2.5 / 2.4 / 3.8), each under -3 dB for 0.5-1.5 s. Final chord: Violins II 9.8, 11.7, 10.8, 8.0,
7.8, 9.3, 11.6; Violins I 9.0, 5.6, 9.2, 8.4; Violoncellos 8.9, 5.6, 8.1, 3.9, 3.8; Violas div 10.4, 6.1, 6.6, 2.1, 10.1;
Violas 4.0-7.2; Double basses 4.1-6.7 (own 3.5-5.8). ff re-bows (CC11 116-122) do not dip (0.1-3.4 dB): the hole is the slow
start of the pp / p Sus MAX sample (group attack 12-23 ms in the patch, so no envelope setting shortens it) after a
release capped at 600 / 400 ms. Second fault: where the first piece is on Leg Slur MAX the Sus MAX piece after it sits a
median 2.2 dB lower (n 11: Violins I 2.4 -4.5 dB, 295 -5.0; Violins II and Violas 223 -6.5 / -6.4); Sus MAX to Sus MAX is
0.0 dB (n 38). Third: the re-bow keyswitch sits 0.02 qn (23 ms) before the note; EW's sit 40-800 ms ahead.

Which option fits each (the three options named by the lead):
- **Double on an idle instance, re-bows interleaved** (the other instance changes bow at the midpoints): Violins I qn 0-9 and
  292-304 on "Violin I solo" (1st Violins KS Master DIV A, idle outside 48-65); Violins II 286-304 on "Violins II div"
  (DIV B, idle after bar 40); Violoncellos 292-304 on "Violoncellos div" (DIV A, idle after 286, Sus MAX already loaded).
  Simulated on the c55 stems with a copy shifted by half a piece (`dbl.py`; inferred for a different patch): median dip
  Violins II 8.4 -> 2.6 dB, Violins I 7.5 -> 3.9 (bars 1-3: 6.6 -> 2.5), Violoncellos 4.9 -> 2.8. Data: a new
  option beside `TRACK_SPLITS` in `build/score_config.py` (for example `TRACK_DOUBLES = {"Violin I solo": ("Violins I",
  [(0.0, 9.0), (292.0, 304.0)]), ...}`) that copies the held note to the idle track instead of moving it;
  `REBOW_AT[that track]` = the midpoints; both tracks at CC7 90 (-3.0 dB, before the hall) over the span; the copy
  carries the source's CC15 (mutes), CC70 and CC11. Two tracks need the Sus MAX row added (two full rebuilds, about 0.1-0.3 GB each; REAPER is at 39 GB).
- **Skip the re-bow** where a note is under two loop lengths and under other parts: bars 2-3 (qn 3-9, 7.0-7.2 s) Violins II
  5.15, Violoncellos 6.8, Double basses 6.25, Violas 5.7 (c55 dips 8.2 / 8.5 / 4.0 / 2.5 dB; the winds enter from qn 6), and
  the 5-7 s notes with one automatic point: `AUTO_REBOW_SKIP` gets these onsets. Keep the printed bow changes (223, Violins I
  295 / 298 / 301, Violins II 289 / 292).
- **Overlap two bows on one track**: not possible as MIDI (same pitch, same channel). The instrument's own form of it is the
  Legato script on the Sus MAX row (CC68 = 127 over the held span; `Legato3` crossfades 180 ms and starts the new note
  200 ms into its sample). Untested here; whether a same-pitch re-attack counts as connected is not known (`EWSO`
  CONNECTED 30: try a re-bow gap of 0.01 qn instead of 0.03). It is the only candidate for the Violas, Violas div and
  Double basses, which have no idle instance (a shifted copy of the basses' own stem made the dips worse, 4.2 -> 5.9 dB).
- Generic, no audio risk: a held note that is a fresh entry starts on `REBOW_ART` (Sus MAX) so every piece shares a row
  (Violins I qn 0 and 292: removes the -4.5 / -5.0 dB steps); re-bow keyswitches 0.15 s ahead (`KS_ROWCHANGE_LEAD_S`
  applied to re-bow pieces); automatic pieces no shorter than 3.4 s where the note allows (Violoncellos div 274-286 has six
  pieces of 1.8-2.8 s: four pieces remove two of five bow changes).

Needs a range pass (three ranges, strings only): qn 0-12, 270-304, and 108-124 for the Legato-script test on Violins II.
Variants: c55 as is; skip; doubled; CC68. Verify with `rebow2.py` on the pass: median soft dip 4 dB or less and no re-bow more
than 3 dB over its note's own movement; on the final chord also the 100-300 Hz and centroid autocorrelation at 3.95 s
(must stay under 0.3, c26's 0.24 / 0.19). Left audible if nothing passes: Violas, Violas div, Double basses.

### 3. Trombone 1's quotation (bars 63-64): the two printed accents are no longer the loudest notes of the line

Where: Trombone 1, qn 212.5-219.5; accents at 213.0 and 218.0.

Measured. Note bodies: 212.5 -25.6, **213 (accent) -23.2**, 214.5 -26.0, 215 -24.7, 215.5 -23.5, 216 -24.5, 217 -22.8,
217.5 -22.3 dB. The unaccented eighths 215.5, 217 and 217.5 rose 2.2-3.0 dB when their trims went (c54 -26.5, -22.0, -25.2)
and now equal or exceed the accent. First 0.35 s against the note before: 213 +2.2 dB (c54 +7.2), **218 -3.6 dB** (c54 +3.2):
the second accent starts 3.5 dB under its pickup. Peak over body in the first 0.25 s: 213 -0.3 dB (c54 +3.5). The 2-5 kHz
share of the first 80 ms against the body is -4.4 dB at 213 and -3.5 at 218, so there is no bite (Dan's note 9 holds).
Cause: the accent swells (`ACCENT_SWELL_S_AT`) are off and CC11 rests at 108-114 on every note of the line, accented or not.

Fix (`build/score_config.py`, CC11 only; on the Hollywood Brass KS Masters CC11 is level and CC1 the dynamic layer, so the
timbre does not change): unaccented notes of the quotation at CC11 96 (212.5, 214.5-217.5), the accents 213 and 218 at 120
for their first 0.30 s, then 112; start the bar 64 diminuendo (CC11 and CC1) at 218.35 instead of 218.06. With the fitted
0.17 dB per unit this is about -2.5 dB on the unaccented notes and +1 dB on the accent heads (inferred from the kit's fit;
the slope near the top of the lane is not measured). Expected: 213 and 218 each 3 dB or more over the note before in the
first 0.35 s, 2-5 kHz attack share no higher than the body's. Needs one range pass of qn 208-220 (Trombone 1 only), which
also gives the slope; if 120 does not give 3 dB, lower the resting value further rather than adding CC1.

### 4. Transition bursts before the beat: 26, all on Leg Slur MAX, 25 of them at velocity 124

Where: Violins I 65.5, 75, 80, 85, 86, 249.5, 252, 271; Violins II 56, 68, 146, 190; Violas 111, 116.33, 144, 255;
Violoncellos 48, 68.5, 77, 140, 142.5, 143, 174, 240.5, 249; Violas div 286. 14 of the 26 are in the two statements of
the theme (qn 65-90 and 237-262).

Measured (`joinpeak_c55_fix.json`): 5.0-13.6 dB over both bodies with a master bump of 2.0-5.1 dB, peak 40-210 ms after the
note-on, which is 43-257 ms before the beat (so they are also 15 of the S readings that now read early). c54 held them
with volume notches (2 with a master bump). Two facts point at the instrument: (a) every string section legato target is at
velocity 124, the fast end of the script (`LegatoSpeed` maps velocity 30-127 to a start offset of 0-4800 samples, so v124
starts the transition sample about 100 ms in); EW's demo plays string legato at 57-124, median 92-98, and the scherzo
measured 0 bumps of 13 on celli joins at 70-90 against 14 of 55 at 91-110; here the DIV A solo at 72-80 has no burst of
5 dB in 9 joins (another patch; indicative only). (b) One transition is hot whatever the context: Violoncellos
A flat 3 -> G 3 bursts on all four occurrences, +6.7, +8.3, +13.6, +11.1 dB (68.5, 77, 240.5, 249).

Fix:
1. `build/score_config.py` `LEG_VEL_BY_CC`: add `"string": ([(22, 84), (46, 90), (72, 98), (114, 108)], 0)` in place of
   the fixed 124 (ff keeps 108 as in bars 61-62; `VEL_SET` exceptions stay), and refit `build/leg_leads.json` on the pass
   with `tools/s_onsets.py` (a longer transition wants about +0.03 to +0.07 s of lead, MANUAL-GAPS item 6).
2. Port `region_gain` from `symphony/mvt3/reaper-v600/tools/build_reaper.py` (line 308) with a filter on the transition
   group's start key, and set in `build/mix.json` for Violoncellos: row "Leg Slur MAX", group start key 56 ("TLeg G#2"),
   region key 55, -7 dB. One Opus state change (Violoncellos full rebuild).

Expected: bursts of 5 dB or more with a master bump of 2 dB or more from 26 to 8 or fewer; the four celli bursts to 0-6 dB.
Needs a range pass of qn 63-90 (strings); accept only if the pitch-change join holes do not rise and the S crossover of
Violins I against II stays within 30 ms on 21 of 24 onsets. Not proposed: a CC11 dip per join (the reference lanes are flat
across joins).

### 5. Join holes and deep soft starts are concentrated on four legato rows and on fresh soft entries

Where: Oboe 1 bars 15-22, 45-47, 53-60 (16 of 23 pitch-change joins with a hole of 6 dB or more, 8 of 9 dB or more; worst
47 11.1 dB, 57, 140, 143); Cor anglais bars 31-36, 41-44, 88 (14 of 24; c54 4); Violins II (29 of 102) and Violoncellos (23
of 82), mostly qn 45-90, 140-152, 238-262; fresh entries: Violins II and div 108 (Flautando, first 0.35 s 12.4 / 10.8 dB under
the body), Violoncellos 238 (11.3), 286 (11.2), 124 (10.0), Double basses 140 (9.9), Violins II and Violas 42 (9.8 / 9.7).

Measured. Median level through the join from the note-on (`prof.py`): oboe -6.1 dB at 0.10 s, -9.8 at 0.15, -8.9 at 0.25,
back by 0.5 s (n 5 steady joins); cor anglais -5.1 / -6.0 / -5.1 at 0.10 / 0.15 / 0.20 s (n 9); flute -3.6; violins -3.5 at
0.25-0.30 s; celli -3.6 at 0.40 s. The hole is the time between the end of the transition sample and the arrival of the
target's sustain group, whose fade-in is a patch value (table above). Movement I c52 measured what that value does: with
it at 20 ms loud joins came 45 ms early and 3-5 dB louder. On the fresh entries the first note of a legato row or of
Flautando blooms slowly at pp and the entry lead is already 120-300 ms.

Fix:
1. New generic state edit in `tools/build_reaper.py` `state_for` (next to `cap_release`): mix.json
   `"leg_sus_attack_scale": {"rows": ["Leg Slur MAX"], "scale": s}` multiplies the AHDSR attack of the groups whose name
   contains the patch's `LegatoSpeed.SUS_GROUP_SUBSTRING` ("OBs", "EHs", "V1s"). Test s = 0.5 and 0.25 on Oboe 1 and Cor
   anglais (440 / 465 ms -> 220 / 110), s = 0.6 on Violins II and Violoncellos (1054-1380 -> 630-830 ms).
   `tools/state_guard.py` compares against the written state, so it keeps working.
2. Fresh soft entries of 0.6 s or more on Leg Slur MAX / Flautando at CC11 50 or less: a CC11 entry shape before the hall,
   +10 units at the note-on falling to 0 over 0.5 s (0.23-0.36 dB per unit on the strings: 2.3-3.6 dB), as a generic rule
   in `tools/score_to_parts.py` (for example `SOFT_ENTRY_CC = {"cc": 10, "s": 0.5, "max_cc": 50}`), not a table of
   onsets. This is a phrase start, where reference lanes do move (FINDINGS line 111, a Spitfire mockup: +14 units by
   0.4 s; in EW's own demo about half of the phrase starts are flat).
3. Leads: the 27 joins whose crossover is now the S reading (+26 to +72 ms) get their excess over 25 ms added in
   `build/leg_leads.json` (Oboe 1 47 +0.02, 190 +0.01, 198 +0.02; Cor anglais 133.5 +0.02; Violoncellos 68 +0.02, 253 +0.05;
   Violins I 172 +0.025; Violins II 146 +0.025), after item 1, which moves the crossover earlier.
4. Leave alone: soft starts of 3-5 dB on legato targets (the median join; the reference does nothing there).

Expected: Oboe 1 and Cor anglais pitch-change holes of 6 dB or more from 30 of 47 to the c54 count (13) or lower; starts of
6 dB or more from 71 to about 40. Needs a range pass (qn 42-66, 124-152, 238-262; two values per track); accept a value
only if bursts (finding 4's measure) do not rise and the crossover shift is taken out of the leads. Offline: only the lead
changes and the corrected counts.

### 6. Printed repeats that lost their separation: three places; the fourth in the actor's list is not a printed repeat

Where and measured (own-band dip, `s1_c55_fix.txt` and CHANGES): Violas 81 (bar 28) 8.9 -> 1.5 dB: gap 90 ms, CC11 69 -> 70
(no fall), mf release 300 ms; Double basses 144 (bar 46) 1.6 dB: gap 60 ms, CC11 26 -> 20 (the lane has no room at pp), pp
release 400 ms; Violins II div 120 (bar 40) 2.6 dB: gap 80 ms, CC11 34 -> 28. Double basses 156 reads 5.0 dB and passes.
Violoncellos 300.6 is a c26 loop re-bow point of the final chord (`REBOW_AT`), not a printed note: its 2.8 dB is the wanted
result and it should leave the S1 list. All 49 repeats: median 8.6 dB, 6 under 3 dB.

Fix (`build/score_config.py`, gaps and CC11 only; EW's experts use 60-100 ms, FINDINGS line 157):
`STR_REP_NEW_BOW["soft_gap_s_at"]`: `"Violas": {81.0: 0.15}` with a CC11 fall of 16 units over the last 0.12 s of the note
before (about 5 dB at 0.31 dB per unit, before the hall); `"Double basses": {144.0: 0.14}` (156 unchanged);
`"Violins II div": {120.0: 0.15}` with its existing fall. Expected 4-6 dB each; target 3-6 dB in the stem's own band and no
hole over 9 dB. Decided on the full render (three notes; no range pass needed); if the basses' 144 stays under 3 dB it is left
audible, since the only other lever is the pp release cap, which c43 set for the soft pitch changes.

## Do not touch

The violas' portato eighths of bars 48-51 on Detache (15 notes, peak a median 176 ms after the onset, 14.4 dB fall after each,
level spread 2.3 dB: identical to c54); the fp of bar 47 (Violins II +16.0, Violas +16.2, Double basses +21.4 dB over the note
before, unchanged); Trombone 1 on Sus MAX / Leg Slur MAX with no CC1 bump (no 2-5 kHz excess on either accent); the printed
bow changes at 223 and Violins I 295 / 298 / 301; the leads' pitch crossovers (unchanged against c54 on 725 of 727 joins);
Violins I's rest from qn 218 (printed); the pre-roll CC36 / CC69 resets; the pizzicato velocity fit of bars 41-44; and the
rule itself: none of the above puts a per-note move back into the track volume envelope.
