# Cycle 19, critic C: tempo, timing and transitions (lens C3), on the c18 render

Material: `cycles/c18/render/` (31 stems, master), `cycles/c18/scherzo-mockup-c18.mp3`, `cycles/c18/build_render/` (parts.json, leg_trans.json, lead_set.json, score_config.py), `build/score_config.py` (the two unrendered fixes), `tools/score_to_parts.py`, `tools/deliver_master.py`, `cycles/c18/CHANGES.md`, `loop/ONE_TIME_c19.md`, the c15 C report (this lens on c14).

Methods. I ran `cycles/c13/actor_scripts/timing13.py` (copied to scratch, unchanged) on c17 and c18: 16 tracks over the Allegro sections (2,679 readings each), and a second copy over the trio and the Meno mosso (qn 456-720 and 1020-1128, 11 tracks, 707 readings). "pc" is `pcx.attack_pcx` (perceived attack on the new note's harmonic bands, the old pitch's bands excluded on joins), "xr" the crossover of the old and new pitch bands, both in ms from the score onset; S is the smaller. As in c15, I call a note late only where pc and xr agree, or where I compare the same estimator on both renders. On every track the joins that c18 did not touch read identically on both renders (median change 0 ms), so the differences below come from the c18 changes. I compared the mp3 with the master after aligning them (the mp3 lags by 239 samples).

## Manual notes (T1: May 2021 HO manual, PDF pages 143-146, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.143: CC table: CC5 legato/portamento time, CC15 con sordino, CC22 mono/poly, CC36 round-robin reset, CC57 legato script, CC65 portamento script, CC69 repetition script, CC70 finger position | the lanes in parts.json: CC1, CC7, CC11, CC15 (7 tracks), CC70 (2 tracks); CC22 and the reset in the pre-roll, CC16 resets inside the piece (Opus's preference, MANUAL-GAPS #12) | Yes for what is used. CC5 and CC69 are not used (see below) |
| p.144: Monophonic True Legato: a note that starts while the previous one sounds plays a legato transition; velocity sets the transition time (50-60 slower, 110-127 tighter) and not the loudness | (a) the clarinets' "Leg Slur Rep" row, which REP_ROW puts under every clarinet note: c18's 0.04 s wind overlap now joins 34 tongued pitch changes on it (finding 1); (b) Horn 3's legato notes after the pickup eighths at 512 / 524 (finding 4) | No for (a): the overlap rule was meant for polyphonic rows only and reads the row name from before REP_ROW. (b) open since c15 |
| p.144: Con Sordino on CC15, on/off at 64 | Violins II con sord. from bar 168 (qn 501.5): CC15 127 at 445.29, 0 at 552.54 ("via sord." bar 185), between notes | Yes |
| p.144: Legato / Portamento "Time" on CC5 (0-127) | the legato transition length on every string legato row; an alternative to lead and velocity for the late soft joins | Not used. Not proposed this cycle: velocity already moves the transition (c10, c15) and is per note |
| p.145: Repetition script (CC69) detunes or borrows a neighbouring sample on each repeat, randomly; the manual itself contrasts it with RR reset, which gives the same result on every playback | the theme head's repeated eighths, the trumpets' repeated quarters (S1) | Not used, correctly: renders must repeat (ONE_TIME_c19 item 6.8: round-robin takes already move single levels 1-2 dB between renders) |
| p.145: Round Robin Reset on CC36, any value; reset at important positions for consistent playback | the pre-roll reset; CC16 resets at 264 / 273 / 282 / 291, 312, 756, 912 | Yes |
| p.145-146: Finger position CC70 (FP1 0-38 ... FP4 115-127), a preference only | `SUL_SPANS` (Violins I 0-23, 528-538, 1089-1125; Violins II three spans), lanes at 127 elsewhere | Yes (unchanged since the c15 check) |

## Findings, ranked by what a listener would gain

### 1. The new 0.04 s wind overlap makes the clarinets slur their tongued notes and arrive 30 ms late, and puts the hemiola half notes of bars 101-104 and 301-304 up to 180 ms late (measured; the slurring is inferred from the patch behaviour on p.144)

Where: Clarinet 1 and 2 throughout (34 joins), and the woodwind half notes of the "ritmo di quattro battute" hemiola, qn 302-310 and 902-910 (Flute 1, cor anglais, both clarinets), plus 987-1012 in the coda.

Evidence:
- c18 added 146 overlapped pitch changes (parts.json, c17 against c18): Bassoon 2 53, Clarinet 2 19, Bassoon 1 16, Clarinet 1 15, cor anglais 15, Flute 1 13, Contrabassoon 7, Oboe 1 3, Oboe 2 2, Horn 3 2, bass clarinet 1. The 34 clarinet joins sound on "Leg Slur Rep", a monophonic legato row. `score_config.py` line 321 puts every clarinet note on it by `REP_ROW` ("the keyswitch only: every rule still sees the old rows"), and the overlap test in `score_to_parts.py` (lines 3268-3269, `not _lg(n.get("art"))`) reads that old row name. So an overlap meant for polyphonic sustain rows reaches a legato row, where p.144 says the new note plays a legato transition: these tongued, unslurred notes are now slurred.
- Timing on the same estimator (pc with the old pitch excluded, run on both renders): Clarinet 1 median +5 -> +41 ms (9 of 14 later by more than 25 ms), Clarinet 2 0 -> +33 (10 of 13); xr on c18 +33 / +29. In c17 these notes were on time.
- The hemiola (each half note is 0.455 s at quarter 264, just over `overlap_min_s` 0.4): Clarinet 1 304 -7 -> +29, 306 +15 -> +41, 904 -1 -> +54, 906 +15 -> +43; Clarinet 2 308 / 310 / 908 / 910 -6..0 -> +30..+33; cor anglais 306 +55 -> +140 (xr +75), 308 +1 -> +47, 902 -13 -> +156, 906 +63 -> +139, 908 +1 -> +45; Flute 1 304 -1 -> +181, 908 -14 -> +71. On the polyphonic rows the new note's attack starts under the old note, still at full level for 40 ms plus its release.
- The woodwind stems' sum rises less at the hemiola onsets (the rise from the 150 ms before the beat to the 120 ms after it; c17 -> c18): 304 2.1 -> 1.7, 306 7.0 -> 5.8, 308 4.0 -> 3.4, 310 3.8 -> 1.7, 902 4.8 -> 4.0, 904 5.3 -> 4.7, 906 3.4 -> 2.4, 908 4.5 -> 4.1, 910 2.8 -> 2.2 dB (302 rose 4.3 -> 6.9). Those half notes are what makes the hemiola heard against the 3/4 bar.

Fix:
- `tools/score_to_parts.py`, the `overlap_s` condition: test the row the note is played on, after `REP_ROW` and `ROW_REMAP` (the row its keyswitch selects), with `_lg`, and skip the overlap when that row is a legato row. On the c18 data this removes the 34 clarinet overlaps and restores c17's gaps there. It is a generic fix: no default changes.
- `build/score_config.py` `WIND_DETACH["by"]["wood"]`: `overlap_min_s` 0.4 -> 0.6 s, so the 2-quarter notes of the Allegro (0.455 s) keep their c17 gap and the long notes keep the overlap. Measured cost: the woodwind joins with a note under 0.6 s are Flute 1 13 of 13, cor anglais 14 of 15, the clarinets 7 + 7, Bassoon 2 32 of 53, Oboe 1 2, Oboe 2 1, Contrabassoon 2, Bassoon 1 1. Check the wind-and-brass bar-line dips (critic A's measure) on 302-310, 902-910 and Bassoon 2's 362-382 before and after. If the dips there come back over 4 dB, use `overlap_s` 0.015 s on those notes instead of 0.04.
- Target: the hemiola notes within +-30 ms on pc as in c17; the clarinets' pc median within 10 ms of c17.

### 2. LEG_TRANS_CC did not change the join swell, but it made string legato attacks read later; take it out (measured)

Where: the 255 joins of `build/leg_trans.json` on Violins I and II, violas, celli, the solo and Violas div. The celli are affected most: 315, 324, 588, 792, 924, 933, 948 in the Allegro, 518, 546, 588, 597, 647 in the trio. Also Violins II's codetta (672-708) and the violas' 591-632 and 1032-1035.

Evidence:
- Allegro sections, joins in the table against the same joins on c17 (S): celli 57 measured, median +4 ms, mean +10.5, 7 later by more than 25 ms, none earlier; violas 22, median +1.5, mean +2.8, 3 later and 1 earlier; Violins I and II median 0. Joins outside the table with unchanged leads: median 0 on every track.
- Trio and Meno mosso, the same comparison: violas 24 joins, pc median +13, 6 later by more than 25 ms; celli 43, pc +20, 7 later; solo 9, pc +14; Violins II 34, 6 later. xr is unchanged (median 0): the pitch changes at the same moment, but the new note reaches its level later. Single notes: celli 588 pc +20 -> +152, 315 -42 -> +18 (xr +102 -> +112), 924 +19 / -1 -> +55 / +31; Violins II 678 +14 -> +98, 681 +31 -> +120; violas 591 -12 -> +76, 146 +14 -> +54. Per passage: celli trio tune median S +12 -> +21, celli 197-208 +16 -> +32, Violins II codetta +22 -> +58.
- Mechanism, read in parts.json: at celli 588 (moved note-on 587.335) CC11 goes 85 -> 77 at 587.56, holds 77 to the beat and returns to 86 at 588.25. The new note's body is held down until about 0.1 s after the beat, so its perceived attack moves later. The swell it was meant to remove did not change (c18 CHANGES: join excess median 3.2 -> 3.1 dB, 91 of 429 over 6 dB).

Fix: `build/score_config.py` line 1642: `LEG_TRANS_CC = {}` (or `C18_LTC` empty). Leave `build/leg_trans.json` as a record. Critic A is looking for the source of the swell in the patch; whatever replaces this dip must not hold the new note under its level past the beat. Test any CC11 shaping of joins on a range render with pc and xr before and after.

### 3. The half-step lead corrections: two celli notes overshot, one violin note did not move at all (measured)

Evidence (c17 -> c18, pc / xr, lead in ms):
- Better: violas 594 -71 / -29 -> +20 / +18 (265 -> 230); Violins II 133.5 -107 / -54 -> -63 / -3 (200 -> 147); violas 1056 +88 / +135 -> +43 / +89 (225 -> 269); Violins I 361.5 +62 / +94 -> +40 / +97 (80 -> 111, only partly).
- Overshot: celli 933 -69 / +44 -> +30 / +74 (180 -> 146), celli 948 -70 / -3 -> +26 / +106 (155 -> 120). In c17, xr already put both on time (948 at -3). The change followed S, which takes the earlier of the two estimates, so it acted on pc alone. Celli 348 now disagrees in sign (-78 / +75).
- Not realised: Violins I 597. `lead_set.json` asks 0.178 s; the render plays 132 ms, as in c17, so the reading is unchanged at +92 / +92. The cap is `PREV_MIN_SOUND_S` 0.06 behind the Sus MAX pickup 596.5 (moved to 596.272), and the keyswitch to Leg Slur MAX at 596.282 makes 597 the first note on the legato row (manual p.99; c15 finding 1's class).

Fix:
- `build/lead_set.json` Violoncellos: 933 -> 0.18, 948 -> 0.155 (their c17 values).
- Rule for the next fits: change a lead only where pc and xr agree in sign and both pass 45 ms.
- Violins I 597: delete its `lead_set.json` row (it does nothing) and make it a Sus MAX stroke: `DOWNBOW_STROKE_AT` with `REATTACK_LEAD_AT` 0.085 s, as c14 did for 157.5 / 385.5 / 853.5. Refit the joins after it to the end of the slur.
- For every lead row, print the realised lead next to the requested one.

### 4. Horn 3's trio tune still limps on four notes, 60-140 ms behind the celli it doubles (measured)

Where: Horn 3 with the celli, bars 169-176 (qn 510-524), and Horn 3's recall at 1028.

Evidence (c18 pc / xr; realised lead):
- Horn 3 510 +79 / +63 (79 ms), 519 +73 / +87 (79 ms), 512 +12 / +127 (59 ms), 524 +88 / +139 (59 ms), 1028 +172 / +155.
- c17 read the same (510 +97 / +83, 519 +78 / +147, 524 +70 / +121), so "Mono From Left" did not change the timing.
- `RETONGUE_LEAD_AT` asks 0.12 s at 510 and 519 (score_config line 1352) and gets 79 ms; 516 and 522 get their 0.12. 512 and 524 follow the pickup eighths 511.5 / 523.5 at velocity 100.
- The celli on the same notes: 510 +49 / -8, 512 +83 / +51, 519 +84 / +8.

Fix:
- Find what caps 510 and 519 (print the realised lead; the notes before them, 509 and 518, are 1.07 qn long at velocity 100, so suspect the `PREV_MIN_SOUND_S` cap or the re-tongue gap) and let them reach 0.12 s.
- 512 and 524: legato velocity 100 -> 120 (`VEL_SET`; p.144: 110-127 tightens the transition and does not change the loudness), with a legato lead of 0.10 s.
- Target: within +60 ms on both estimators and within 40 ms of the celli.

### 5. The tuttis have no downbeat weight; the delivery takes a little more off the beat (measured; the cause is inferred)

Evidence:
- Downbeat peak (0-90 ms) minus the mean of beats 2 and 3, median over bars, master / mp3: tutti 105-120 -0.3 / +0.1 dB, tutti 305-320 +0.1 / +0.2, coda 329-336 -0.3 / -0.2. Against that, theme A p (bars 13-28) +3.1 / +3.0, reprise 253-268 +1.5 / +1.6.
- In the tuttis beat 3 of the theme head (a staccato quarter before the accented downbeat of the next bar) is louder than beat 1 on Violins I (-25.3 against -26.2 dB) and Trumpet 1 (-30.7 against -31.5). The velocities are flat: trumpets 95 / 96 / 96, Violins I 95 / 96 / 96 by beat.
- The delivery: the 2-5 kHz beat contrast (beat peak against the minimum between beats) master -> mp3: tutti 105-120 9.3 -> 8.4, tutti 305-320 9.6 -> 9.1, coda 8.2 -> 7.6 dB. The peak compressor (2 ms attack, 60 ms release) and the limiter (5.5 dB on the summit) do this. 60 ms is half an eighth here.
- The quiet passages lose nothing: beat contrast changes by at most 0.1 dB on all nine quiet passages I measured.

Fix:
- `METRIC_DB` and `METRIC_BOWED` are track-envelope steps, which Dan's rule forbids. Test velocity instead, on a range render of 312-330: `METRIC_VEL` limited to 312-360, 912-960 and 984-1008, Trumpet 1 / 2 and the Violins I / II staccato rows only, downbeat +6, beat 3 -4.
- Adopt it only if the downbeat-minus-beats-2-3 figure reaches +1 to +2 dB without moving the accent median (c16's global `METRIC_VEL` on the pizzicato failed, which is why this test is narrow).
- Delivery: try `DELIVER_PEAK_COMP` release 60 -> 120 ms (`tools/deliver_master.py` line 94) and keep it only if the mp3's beat contrast in the tuttis comes within 0.3 dB of the master at the same LUFS and limiter figures. This is low priority.

## The two build/ fixes not yet rendered

- Violins I 51 / 771 back to the theme row: right, for timing too. On "Sus MAX" with the theme row's 120 ms lead these notes read pc -219 / -203 ms: early, as well as 7-8 dB down. On Sus Marc LITE in c17 they read -14 / -11.
- Violins II fugato +30 -> +24: plausible. At the measured 0.48 dB per unit it gives about -39.4 dB against the violas' -40.9 (critic B's lens).

Overall S outside 25 / 60 ms, Allegro sections: c17 25 % / 5 %, c18 26 % / 5 %. The 1-point rise is findings 1 and 2.

Do not touch:
- The tempo map. parts.json `tempo` (321 points) is identical in c15, c18 and build/. c15 checked the bar averages against every printed tempo, the fermatas and the G.P., and no `BEAT_STRETCH`, `CAESURA`, `PHRASE_ARCS` or `TEMPO_PUSH` has been added since.
- Keyswitch placement: 1,162 keyswitches, none under 3 ms before its note (median 45 ms, 5th percentile 6.8 ms).
- Short-note timing in the theme statements and tuttis is unchanged from c17 (S medians for short entries): Violins I +3, Violins II -9, violas -4, celli +2, Flute 1 +9, Flute 2 +17, Oboe 1 -6, cor anglais -6, Clarinet 2 -10, trumpets -9.
- Clarinet 1's trio tune (+14..+23 median in every passage) and the harp's off-beat chords.
- The "ritmo di tre battute" grouping: head bars over the bar after by 3.4 / 8.0 / 2.1 dB (89 / 92 / 95), the f timpani bars as printed, the same on the mp3.
- The phrase end before the G.P.: strings and winds stop on beat 2 of bar 339 (qn 1015), brass at 1015.8, all within 155-310 ms to -20 dB (celli 540). The mp3's G.P. falls 26 dB 0.3 s after the cut, the master's 33 dB, measured against the loudest point of the last 0.5 s.
- The final fermata's taper (CC11 29 -> 8 over the last 0.46 s).
- The quiet-passage lift (5 s smoothing does not touch the pulse).
- `RR_RESET_AT`, CC15 and CC70 lanes, CC22.
