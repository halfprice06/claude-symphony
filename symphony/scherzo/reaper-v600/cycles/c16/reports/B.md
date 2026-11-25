# Cycle 16, critic B: balance and levels (on the c15 render)

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are mean-square dB of the stem (mono sum) unless "A-weighted" is stated. "Note level" is the window from 30 ms to 300 ms after the score onset (or to the note's end). Every number below was measured on `cycles/c15/render/` and `cycles/c14/render/` with `cycles/c15/build_render/parts.json` unless marked inferred. No proposal below uses the track volume envelope for a single note or figure.

## Manual notes (May 2021 HO manual, group B4: PDF pages 49-52, 202-204, 208)

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| "Load with Effects off" removes the Opus reverb from every instrument so the hall can be a DAW bus (p.49) | all 31 tracks | yes: `opus_reverb_off`, four REAPER returns |
| Each mic position can go to its own output pair, and each mic can send a different amount to the reverb bus (p.50-51) | every track with Close + Main (`mic_db`); the Close-only DIV tracks (Violin I solo, Violas div) | not used: mics are summed inside Opus and each track has one send, so Close and Main feed the hall in the same proportion. No balance fault traced to it this cycle |
| One Opus instance can hold up to 16 instruments on separate MIDI channels (p.52) | a second copy of a row at another level (finding 4: "Sus Marc LITE" needs two levels), Timpani Hrd next to Flt | not used: 31 single instances. It adds no plugin, but the samples still cost memory |
| Level Amp, Limiter, Limiting Amp, SSL Bus Compressor as inserts inside Opus, before the output (p.202-204) | bass and timpani peaks | not used, and I do not propose them: they would flatten printed dynamics per stem |
| SSL Transient Shaper on the instrument or a mic channel; "Invert" subtracts the detected attack and leaves the body unchanged (p.208) | Timpani: the 2-5 kHz share of the first 80 ms rose 5.6 dB with the c15 velocities (finding 1) | not used. It is a static setting in the Opus state, before the hall, and it is not a volume move. Worth one range test if the velocity cap of finding 1 is not enough |
| MANUAL-GAPS #7: recorded crescendo rolls ("Crs" row, p.123, 125) | the timpani roll of bar 332 (mf < f), which does not grow (finding 1) | not used |
| MANUAL-GAPS #9: half-section patches for "div." | basses' div. pizzicato octaves, bars 253-268 (finding 5): both notes play on the full section | not used |

## What the removal of the per-note levels did to balance (the actor's list, measured)

- Sections: every stem is within 1.0 dB of c14 in the 29 passages I measured, except the ones in the findings below (Oboe 1 bars 277-280 -4.5 dB A-weighted, Double basses bars 253-268 +3.1, cor anglais bars 101-104 / 301-304 +2.7 / +3.1, Violins I bars 301-304 -2.4, Violas bars 349-356 +2.6).
- Note-to-note evenness did not get worse on most tracks. For each note I took its level minus the median of its neighbours within 9 qn on the same row and the same printed dynamic (within 6 CC units). Standard deviation c14 -> c15: Flute 1 3.6 -> 3.5, Oboe 1 3.3 -> 3.6, Clarinet 1 4.1 -> 3.8, Clarinet 2 2.8 -> 3.2, Horns 1-4 unchanged (3.3, 2.6 -> 2.5, 2.7 -> 2.6, 4.3 -> 4.0), Violins I 2.6 -> 2.4, Violins II 3.0 -> 3.0, Violas 3.4 -> 3.1, Violoncellos 3.6 -> 3.7, Double basses 2.8 -> 3.2. Notes 4 dB or more off their neighbours: 77 -> 78 (Flute 1), 61 -> 45 (Clarinet 1), 68 -> 55 (Violas), 80 -> 68 (celli), 28 -> 45 (Double basses). Only the basses are clearly worse.
- Horns' legato-joined notes: not a fault on the stems. Horn 1-4 notes differ from c14 by -0.5..+0.5 dB (10th..90th percentile); notes 3 dB or more away: 1, 0, 1, 0. The "2-5 dB under target" in CHANGES.md was against the simulation, not against c14's sound.
- Clarinet 1's 12 former skip onsets: real (624, 634, 638, 639: +4.0, +3.9, +4.5, +4.6 dB against c14). They lie in bars 209-224, where Clarinet 1 doubles the violins' tune at ff and sits 4.3 dB (A-weighted) under Violins I. Leave them.
- Cor anglais A4, basses by pitch, the timpani and the steps inside notes: findings 1, 2, 5, 6.

## Findings

### 1. Timpani: the two coda rolls lost their level, and the loud strokes are harder for no gain in level (measured)

Where: Timpani, roll of bar 336 (qn 1005-1008, printed ff under the fff summit), roll of bar 332 (qn 993-996, mf <), loud single strokes in bars 105-120, 301-324, 325-339.

Rolls. In bar 336 the stem falls from -30 dB at the roll's start to -46 / -49 dB just before the stroke at qn 1008 (50 ms frames: -30 -31 -33 -36 -38 -38 -39 -38 -40 -41 -44 -46 -49). c14 held -29..-35. The roll plays "Timpani Flt Rls" at a flat CC1 of 104 (no CC1 point after qn 1004.98), and the slow lane falls from +3.7 dB to -0.3 by qn 1007.4, -5.1 at 1007.9 and -9.0 at 1008.0, then steps back to -4. c14 held the roll with a level row (+5 / +8 dB, `LEVEL_SHAPES["Timpani"]`, score_config.py line 509), which is no longer played. The fall from -5 to -9 dB in 0.1 qn (23 ms) before the stroke at 1008 is a notch keyed to a note; it is in the "slow" class. In bar 332 the roll is flat (-40 dB at its start, -41 at its end; c14 -40 -> -38 / -35) although CC1 runs 73 -> 88: that CC1 range gives no audible growth on this row. This is the -1.6 dB of bars 325-340 in CHANGES.md.

Strokes. 84 strokes changed velocity (+22). Their level over 20-170 ms moved -0.7 dB (median; section medians: bars 105-120 -0.1, 301-324 -0.4, 325-340 -0.5), and the 2-5 kHz share of the first 80 ms rose 5.6 dB (median; bars 105-120 +9.6, 301-324 +5.4, 325-340 +5.4). By pitch and velocity in c15: E2 (key 40) -31.6 dB share at velocity 80 and -17 at 113-120; right-hand B2 (key 71) -25.1 at 80, -18.6 at 111-115, -14.9 at 125; c14's strokes at velocities 89-96 read -23 to -31. The top sample layer starts between velocity 96 and 111 and is much brighter. Level against velocity: E2 -43.5 dB at 80 and about -35 at 116-118, which is 0.24 dB per step, as the finale measured.

Balance. The timpani are not covering anything: bars 105-120 -32.9 dB against Violins I -25.2; bars 305-320 -33.1 against -25.1; bars 333-335 -29.5 against -24.1. No roll is the loudest stem in bars 101-103, 129-130, 205-208, 237-240, 285-286, 301-303, 332 or 336.

Fix (instrument side and roles):
- `build/score_config.py` `TIMP_LOUD_VEL_ADD = (8, 104, 0.0)`: add 8, cap 104, so no f stroke enters the top layer. Range-test velocities 98, 102, 106, 110 on E2 and B2 under the lock to place the layer boundary, and set the cap 2 under it. Keep `TIMP_METRIC_VEL` as it is; with the cap at 104 the downbeat / off-beat spread of 9 velocity steps (about 2 dB) is no longer clipped at the top.
- The level that velocity 116 -> 104 gives up (12 steps, about 2.5 dB) goes into `build/roles.json` as whole-passage rows: Timpani [312, 360, +2.5], [912, 960, +2.5], [996, 1004.9, +2.5].
- Roll of bar 336: in the roll CC1 lane hold CC1 at 118 from qn 1005 to 1007.9 (now 104; printed ff, `TIMP_CC1_MAP` ff 104 -> use the fff value 122 less 4 for this roll), and take the settle off this roll (the `slow:timp_settle` item at 1005; a roll under the summit does not settle, the brief's rule 5 applies to long rolls). Remove the -9 dB point at qn 1007.95-1008.0 from the roll shape; if the roll must clear the stroke, end the roll's MIDI note at qn 1007.8 instead (0.045 s earlier).
- Roll of bar 332: CC1 ramp 62 -> 104 over qn 993-996 (now 73 -> 88) so the roll crosses two of the row's CC1 layers, or play it on the recorded crescendo row "Timpani Flt Crs" (MANUAL-GAPS #7, one row). Check on the stem that the last 0.2 s is at least 4 dB over the first 0.2 s.
- Only if the strokes still read more than 3 dB over c14 in the 2-5 kHz share: Opus "SSL Transient Shaper" with Invert on the Timpani instrument channel (manual p.208), one range test.

### 2. Hairpin gains and role edges still step 3-6 dB inside sounding notes (measured)

Where: the "slow" lane of 14 tracks; 26 places where the lane moves 2 dB or more within half a quarter note (0.10-0.14 s) under a note that started more than 40 ms earlier and goes on sounding, with no printed hairpin over the move (13 further places are inside printed hairpins). These were in c14 too, but they are now most of what is left of fast fader movement, and they break the acceptance check in ONE_TIME_c16 item 5.

Cause 1, the hairpin-gain release (`HP_GAIN_DB` wind 4, string 3; held for `HP_HOLD_CAP` 4 qn after the arrival; released over `HP_REL` 1.0 qn, which is 0.23 s at quarter 264). The gain that helped the crescendo is taken away inside the arrival chord:
- qn 124.1-125.0 (bar 42), Clarinet 1, Bassoons 1-2: lane +4 -> 0 dB in 0.2 s inside the f chord held from qn 120. Clarinet 1's stem: -32 dB before, -38 after 0.25 s (c14 the same).
- qn 160.1-161.0 (bar 54), Bassoon 1, Contrabassoon: -32 -> -37 dB (Contrabassoon).
- qn 388.1-389.0 (bar 130) and 856.1-857.0 (bar 286), Bassoons 1-2, Contrabassoon: Bassoon 1 -36 -> -41 dB.
- qn 592.1-593.0 (bar 198), Clarinet 2: -3.4 dB of lane inside its f note; stem -37 -> -41.
- qn 1013.1-1014.0 (bar 338), Violins II, Violas, Flute 2: lane -5.3 dB (Violins II) inside the fff chord of the summit; Violins II stem -23 -> -28.5 while the chord is still printed fff.
- qn 216.1-217.0 (bar 73), Bassoon 1: lane +6.1 -> 0 inside the first note of the F major section; stem -51 -> -55.

Cause 2, role edges with the 0.5 qn ramp that fall inside a note:
- Horn 1 qn 1080.0-1080.5: the solo role +3 (1068-1080) ends inside the G sharp held from qn 1077 for 20 qn. The note is already falling (printed >), and the edge adds 3 dB in 0.13 s.
- Violas div qn 1052.1-1053.0 (bar 351): lane +8.25 -> +3 inside the note held from 1050.
- Flute 1 qn 1049.5-1050.0: -2.6 dB inside the note from 1049 ("col Vl. solo").
- Oboe 1 qn 386.3-386.8 and 854.3-854.8: -4 dB in 0.11 s inside the note from 386 / 854; qn 1041.0-1041.5: +4 -> 0 inside the note from 1040.
- Double basses qn 95.4-95.9: -3 dB inside the B1 held from 93.

Fix:
- `build/score_config.py`: `HP_REL = 12.0` (4 bars, 2.7 s at Tempo I: 1.5 dB per second for the winds' 4 dB) and let the release start at the arrival (`HP_HOLD_CAP = 0.0`), so a hairpin gain leaves as a slow ramp and no part of it is keyed to "the first onset after the arrival note". If a 12 qn release reaches into a printed softer dynamic, end it at that mark.
- Better where it can be done: carry the crescendo's depth in CC11 (start the hairpin 6-8 CC units lower, arrive at the printed value) and set the hairpin gain of these winds to 0, so there is nothing to release.
- Role rows: move each edge to the nearest rest or to the start of the next note of that track, or lengthen its ramp to 3 qn or more (the fourth value of the roles.json row): Horn 1 [1068, 1080, 3] -> end ramp 6 qn; Violas div [1044, 1068, 3] and the +5 that ends at 1052 -> one constant for 1044-1068; Flute 1's step at 1049.5 -> at 1044; Oboe 1's -4.5 from 386.4 / 854.4 -> from the rest before 384 / 852.
- Acceptance check for the actor: rerun the count (2 dB within 0.5 qn under a sounding note, outside printed hairpins); it should be 0.

### 3. Oboe 1 sinks at the reprise's sub. p, bars 277-280 (measured)

Where: Oboe 1, qn 828-832 (B4, A4, G sharp 4), the second idea in E minor, printed "sub. p espress." with an accent, the same marks as Flute 1 in unison rhythm.

What: against c14 the three notes are -11.3, -8.7 and -7.0 dB (-59.4, -58.9, -51.2 dB; c14 -48.1, -50.2, -44.2). For the first 0.6 s the oboe is at -58 to -61 dB. Over bars 277-280, A-weighted: Flute 1 -37.9, Oboe 1 -44.8 (c14 -40.3), Violas (pp accompaniment) -46.9, Clarinet 1 (pp) -49.0. The espress. oboe is 7 dB under the flute it shares the line with and 2 dB over a pp accompaniment. The first sub. p (bar 121) is fine (Violins I -36.1, Violins II -41.3, accompaniment -45 and lower).

Why: Oboe 1's CC11 is 37 at qn 827.75 and reaches 46 (printed p) only at qn 836.6, while Flute 1 starts at 54 and rises to 73. The role row [828, 840, -4] comes on top. c14 covered this with a per-note fill of +7.5 dB, which is gone.

Fix: `build/parts` data through score_to_parts: give Oboe 1 the printed p at the subito, CC11 46 at qn 827.75 rising to 56 at 832 (take qn 828 out of the soft-hairpin start-lower rule, `hp_soft_acc`, for Oboe 1, or list the onset in the table that sets a hairpin's start value), keep the fall itself in CC11 (S3). In `build/roles.json` change Oboe 1 [828, 840, -4] to [828, 840, -1.5]. Target on the stem: Oboe 1 within 3 dB (A-weighted) of Flute 1 over bars 277-280.

### 4. The tutti sfp of bar 301 has lost its sf (measured)

Where: qn 900, strings and woodwinds; Violins I above all.

What: master, 50 ms frames from qn 898.5: c14 -17 -17 -16 -18 -21 -22 **-15 -18 -17 -18 -17** -18; c15 -16 -17 -16 -20 -23 -25 **-17 -21 -22 -22 -19** -18. The sf is 2 dB lower at its peak and 4-5 dB lower for the next 0.2 s; it is now 1 dB under the ff upbeat at qn 899 and its body is 5 dB under it. Violins I's sf note is -8.0 dB against c14 (-31.4 against -23.4; frames -29 -31 -30 -32, c14 -20 -22 -22 -28) and is softer than its own upbeat (-25). Violins II, violas and celli at 900 read -32.7, -32.9, -32.3, each 2-3 dB under its upbeat.

Why: Violins I's note plays "Sus Marc LITE" (keyswitch at 899.01), and that row is now -8 dB in the Opus state (`region_gain_db` `row_db`) for the theme head. A row gain cannot tell the theme head from the sf. The other strings play "Sus MAX" at CC11 120 after an upbeat at 112-115, so they have 5-8 CC units of headroom, worth about 1 dB.

Fix:
- `build/mix.json` Violins I `row_db` "Sus Marc LITE" -8.0 -> -4.0, and lower the theme head's notes on that row by 4 dB through CC11 instead (they are mp: about 10 CC units at 0.4 dB per unit; put the offset in the rule that writes CC11 for the pair and the hemiola strokes, so the level moves with the note before the hall). The sf at 900 then gets 4 dB back at CC11 127 for its first 0.15 s.
- Strings and woodwinds at 899-900: lower the accented upbeat at qn 899 to CC11 106 (now 112-115) and play the sf at 124-127 for 0.15 s before the fall to p (ONE_TIME_c16 item 7.1: accents need CC headroom). The fall stays in CC11.
- Target: master frame at qn 900 at least 2 dB over the upbeat's frames; Violins I's sf note at least 3 dB over its upbeat.

### 5. Pizzicato basses and celli are uneven by pitch again; the div. octaves of bars 253-268 are at the theme's level (measured)

Where: Double basses "Pizz RRx4" (126 onsets) and "Sus MAX" (110), Violoncellos "Pizzicato RRx4" (53); worst in bars 253-268 (qn 756-804, basses div. pizz. octaves under Violins I's leggiero theme).

What: with the printed dynamic removed (level minus the slow lane, fitted against velocity: 0.27 dB per velocity step on the basses' pizzicato, 0.28 on the celli's), the residual by pitch is:
- Double basses pizz.: E1 -1.5 dB (15 notes), F sharp 1 +4.4 (5), G sharp 1 -1.6 (5), A1 +1.0 (14), B1 +0.6 (39), C sharp 2 +3.6 (4), E2 -2.7 (21); the div. octaves E1+E2 +1.7 (7), A1+A2 +4.8 (4, up to +7.5), B1+B2 +1.7 (4). Spread 7 dB between single pitches.
- Double basses arco "Sus MAX" (fitted against CC11, 0.22 dB per unit): G1 +3.5 (4), G sharp 1 +2.6 (5), A1 +1.8 (18), E1 -1.5 (23), E2 -2.3 (8).
- Violoncellos pizz.: A2 +6.1 (5 notes, +4.3..+7.5), D3 -6.2 (3, velocity 83), B2 -0.7 with a range of -7.0..+7.7 over 25 notes.
- In bars 253-268 the basses' stem is +3.1 dB against c14 and 5.5 dB under Violins I (bars 13-28: 10 dB under). The A octaves at qn 780 and 786 read -36.7 and -41.1 dB against -46.7 for the E octave at 777 (c14: -44.3, -46.4, -49.7) and against Violins I at -36 to -38: single bass notes are as loud as the theme. A-weighted the basses stay 20 dB under the theme, so this is heard as a boom on single notes, not as a covered melody.

Why: the region gains cover only A1 -6 and G sharp 1 -5 on the pizzicato row; c14 added note trims of up to -8.6 dB on the octaves. Two notes on the full section also sound about 3 dB over one.

Fix:
- `build/mix.json` Double basses `region_gain_db`: rows ["Pizz RRx4"], pitch_db add "30": -4.0, "37": -3.5, "40": +2.5, "28": +1.5, "45": -4.0, "44": -3.0, keep "32": -5.0 and "33": -6.0. A second entry for "Sus MAX" needs `region_gain` to take one pitch table per row (now one table for all listed rows): G1 -3.0, G sharp 1 -2.5, A1 -1.5, E2 +2.0. Violoncellos pizz.: add "45": -5.0, "50": +5.0.
- Div. octaves, bars 253-268: velocity 53 -> 42 on both notes of each octave (11 steps, 3 dB), in the rule that writes the div. chord's velocity, or the half-section patch for one of the two voices (MANUAL-GAPS #9; memory first).
- Check after the build with the same fit: residual by pitch within 2 dB, and the basses' stem in bars 253-268 within 1 dB of c14.

### 6. Single notes that vanish or stick out for reasons inside the instrument (measured; cause of the first item inferred)

- Violas, same-pitch long notes that enter "Leg Slur MAX": qn 579 (A3 after A3, bar 194) is at -70 dB for its first 0.5 s (c14 -58 -> -46), qn 585 (B3 after B3, bar 196) is -15.7 dB against c14 (-59..-68 for 0.5 s, then it rises), qn 840 (E4 after E4, bar 281) is at -68..-74 for 0.3 s in both renders, and c14's silent note was qn 828 instead. MIDI, CC and envelope are identical in c14 and c15 at 579 and 585, so this changes from render to render. In each case the keyswitch to the legato row is 0.03 qn (7 ms, under one 512-sample block) before a note that repeats the previous pitch. The violas' espress. crescendo into the f of bar 197 loses its two long notes. Fix: a note that repeats the pitch before it has no legato interval; keep it on "Sus MAX" (the `REBOW_ART` hand-over that `score_to_parts.py` already uses at re-bows) and place the "Leg Slur MAX" keyswitch before the next changing note; give every keyswitch at least 0.02 s (`KS_MIN_LEAD_S` for Violas and Violins II, pending from c15). Inferred: the short keyswitch lead is the cause; the repeat on the legato row's slow first-note layer (BRIEF, established facts) is the other candidate, and the fix covers both.
- Cor anglais A4 on "Sus MAX": the -3.5 dB region gain has no effect. qn 302, 310, 327, 399, 402 read +4.6, +4.2, +3.5, +2.9, +3.4 dB against c14, equal to the envelope trim that was removed, although the build log reports 420 regions changed. At f and ff the A4 stands 8-11 dB over its neighbours (qn 310: -27.7 dB against B4 at 308 -39.2; qn 327: -29.1 against the staccatos at -39 to -43), which puts the cor anglais sixth in the tutti of bars 101-104 (-30.3 dB, +2.7) and 301-304 (-30.6, +3.1). Fix: range-test A4 on the cor anglais "Sus MAX" row with the gain at 0 and -8 dB to find which regions sound (the key range test `keyMin <= 69 <= keyMax` in `tools/build_reaper.py region_gain` matches 420 regions that are not the ones heard at this dynamic; check the regions' velocity or CC layer and the root key), then set "69": -8.0 for "Sus MAX" and keep -3.5 for "Leg Slur MAX" (its A4 is +1.2 dB against neighbours).
- Double basses qn 93-97 (bars 32-33, B1 held, A1 staccato): -5.5 and -12.2 dB against c14 (-52.6, -53.0 dB) with a higher lane than c14's (-2.9 / -5.8 against -4.3 / -7.6). The basses of bars 29-36 are -4.1 dB against c14. Not explained by the envelope; check the "Sus MAX" B1 region at CC11 40 after the region-gain build.

## Do not touch

The section balance of c15 (master within 0.3 dB of c14 per section; melodies over accompaniment: Violins I's theme A 10 dB over the pizzicato bass and 20 dB over the timpani in bars 13-28; Clarinet 1's trio tune 13-17 dB A-weighted over the harp and the horn drone; the celli's tune 6 dB over Violins II's arpeggios; the solo violin 7-8 dB over Flute 1 and 10-12 over Violins II "la metà"; Hn 1 over the Violins I ppp by 1.4-2.4 dB at the close; brass 5-6 dB under the strings at the summit; trumpets 9 dB under Violins I in bars 105-120). The horns' region gains (stems equal to c14). Trombone 2's level from c15. `VOL_CLASSES = ("slow",)` and the roles that carry section balance. The timpani's levels in the tuttis (only the stroke hardness and the two coda rolls need work). The first sub. p (bar 121). The hall settings.
