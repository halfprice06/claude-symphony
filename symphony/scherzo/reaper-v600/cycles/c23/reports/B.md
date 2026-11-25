# Cycle 23, critic B (balance and levels), on the c22 render

Measured on `cycles/c22/render` (stems, returns, master), `cycles/c22/scherzo-mockup-c22.mp3` and `cycles/c22/build_render/` (parts.json, roles, mix). Stems are compared with `cycles/c18/render` (c21's stems are deleted). Masters and mp3s are compared with c21. Positions are score quarter notes (qn); bar b starts at qn 3(b-1).

Measures used:
- **Stem level.** Power of a stem over a window: mean of the two channels' powers, summed over 1/6-octave bands from 40 Hz to 16 kHz, 2048/1024 frames. "A-wtd" means A-weighted. Values are dB on a common arbitrary scale.
- **Note-wise masking.** For each note of a line, take the 0.3 s after its moved note-on. In a 1/3-octave band around each of harmonics 1 to 4, compute the line's power against the sum of every other stem and the four returns. Keep the best harmonic. Report the median and p25 over the notes in a 2-bar window. Tracks that double the line (same pitch class at the same onset for 70 % of its notes) count as part of the line.
- **Best band.** c20-c22's measure, used only for comparison with their numbers.
- **M.** Momentary loudness from ffmpeg ebur128. A bar's value is its median M.

Each judgement is marked (m) measured or (i) inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for c23, so I skipped the page reading. I used `loop/MANUAL-GAPS.md`, and for finding 1 the Sustain Accent paragraph of the May 2021 manual.

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Sustain Accent: "The MIDI Velocity parameter controls the loudness of the attack"; the sustained part follows the mod wheel (p.101) | Flute 1 / 2 accented halves on "Sus Accent MAX" at velocity 90 (CC11 at least 80) since c22 | Yes in method. The attack overlay at velocity 90 is now the loudest thing in several tutti bars (finding 1). |
| MANUAL-GAPS #13 (Mid mics on woodwinds and horns) | | Not reopened. No balance fault below needs a mic change. |
| MANUAL-GAPS #10 (horn portato rows for tenutos) | Horns 1-2's tenuto chord quarters at 105-120 / 305-320 | Not needed. Their level is the printed f (see "Inner lines"). |
| Region volume per row, layer and pitch in the Opus state (c15-c17 LEARNINGS; `region_gain_db` / `row_dyn_db` in mix.json) | findings 1 and 2 | This is the tool proposed for finding 1. |

## Answers to the cycle 23 questions

**Clarinets, bars 37-43: no longer over the tune.** c22's inner-line table measured the tune as Flute 1 + Oboe 1 only. But Violins I plays the same tune in unison (qn 108-114) and an octave lower (114-129) (m, parts.json). It was counted as a masker, so the table read the tune at -4.4 / +0.3 in bars 39-40. With Violins I counted as part of the tune (and Flute 2, Oboe 2, cor anglais and Violins II from 120, where they join it) (m):

| bar | 37 | 38 | 39 | 40 | 41 | 42 | 43 |
|---|---|---|---|---|---|---|---|
| tune over the clarinets, median of the tune's own bands (dB) | +27.0 | +22.0 | +10.3 | +8.5 | +13.6 | +14.7 | +9.2 |
| tune best band over everything (dB) | +12.4 | +8.1 | +8.0 | +6.9 | +10.4 | +11.7 | +2.0 |
| c18, tune over the clarinets | +22.1 | +14.5 | +4.8 | +6.2 | +7.4 | +15.1 | +2.1 |

A-wtd stem levels in bar 38: Clarinet 1 16.2, Flute 1 17.6, Violins I 15.8, Oboe 1 13.4 (c18: Clarinet 1 22.2, Flute 1 17.1). In bar 41 (f everywhere): Clarinet 1 20.7, Flute 1 22.8, Oboe 1 24.0, Violins I 26.3.
- The c22 rows (Clarinet 1 [108, 129, -6], Clarinet 2 [108, 129, -4]) did their job. Do not cut the clarinets further. Their chromatic chord is a printed p < f crescendo, one notch under the tune, as it should be.
- The mp3 crescendo 36-42 reads -18.9, -15.3, -13.4, -12.1, -13.0, -11.4, -10.0 M. Bar 40's dip is as in c21 (-1.6 there).
- Change the actor's inner-line script so that a line includes its doublings. Otherwise every doubled tune reads as masked.

**Hidden inner lines through the movement (Dan, 2026-11-17).** I ran the note-wise masking scan over every track with 3 or more onsets and 2 or more pitches per 2 bars (m).
- Only accompaniment layers fall under -6 dB. No independent moving line does. All the melodies lead clearly:
  - Clarinet 1's trio tune +20..+34;
  - the celli's trio tune +8..+17 (with Horn 3);
  - Violins I at 177 +9..+18;
  - Oboe 1 at 185 +38..+41;
  - the solo violin with Flute 1 +20..+29.
- Lines between -2.5 and -6, accompaniment by role:
  - Clarinet 1's second-idea syncopations, bars 49-53, -3.0..-7.2;
  - Violins II, bars 43 / 275, -3.8 / -5.5;
  - violas' double stops, bars 107-113, -3..-4.4;
  - Bassoon 1's inner half notes, bar 125, -2.9 (p25 -5.8);
  - Horn 3's mf tenuto fragment, bars 129 / 285, -5.2 / -3.7;
  - violas div thirds, 213-221, -2.7..-6.3.
- **Horns 1-2's tenuto chord quarters in the ff tuttis** (105-120, 305-320) read -9..-12. They are printed f under Horn 3's ff espress. countermelody, which plays a2 for Horn 4 in 105-120: Horn 4's 28 notes are `unison_dropped`. Unweighted onset level at 309-360: Horn 1 20.0 against Trombone 1 22.7 and Trumpet 1 25.5; Horn 2 19.9 against Trombone 2 24.2. Rimsky-Korsakov's forte equivalence (2 horns = 1 trombone = 1 trumpet) puts one horn about 3 dB under a trombone. So the horns follow the print and the norm. No change.
- **Violas div, 213-216.** -6.3 against -2.8 in c18. The div stem itself moved only 1.4 dB. The bass clarinet, whose role row c22 deleted, now reads 20.2 against 15.6 at 636, and the violas' lower voice is up 3.5 dB. This is a side effect of a wanted change, on an accompaniment, so accept it.
- What still covers inner material is the woodwinds in two tutti places, at the expense of the strings (findings 2 and 3), plus Flute 1's accents (finding 1).

**Per-bar master and mp3, c22 against c21 (m).**
- Master: median 0.00.
  - Over 1.5 dB: 38 -1.9, 43 -2.0 (clarinet rows); 58 +2.6 (celli round robins); 333 / 334 / 335 +1.6 / +2.0 / +1.9.
- mp3: median +0.9 (quiet lift 2.1).
  - Intro, link, codetta and Meno mosso bars +1.6..+2.2.
  - Counterstatement 28-37 +2.0..+3.3 (ride row).
  - 38 -0.2, 43 -1.1, 54 -1.6 (bar 53 ride row), 218-219 -1.4 / -1.2 (trio A6 ride row).
- The mp3's p10 bar is -22.2 M and its median -16.3.
- On the master the summit's step over bar 335 is now 1.4 dB (335 -12.8, 336 -11.4; c21 2.7). On the mp3 it is 1.1 dB. Bars 333-335 are the cause: findings 1 and 2.

**Role rows by cause.**
- The c22 rows hold: clarinets above; Violins II / violas coda; Horn 4.
- Two rows act where something else now does the work:
  - the woodwind summit cuts no longer cover 996-1004.75 (finding 2);
  - Flute 1 has no row in the trio climb where its hairpin gain overshoots (finding 3).
- Horn 1 [756, 864, -1.5] and [1020, 1068, -2.5] remain inert, as c22's B reported. They are harmless.

**Sub. p at 121 / 277.** Unchanged data and unchanged master bars (S3 passed in c22's B).

## Findings, ranked by what a listener would hear

### 1. Flute 1's accented half notes on "Sus Accent MAX" now stand over Violins I in the tuttis (bars 42, 106, 118, 264, 274, 302-303, 334) (m)

**Print.** Flute 1 doubles the theme one or two octaves over Violins I. The accented half notes are the theme's second beat (G6 at 315, 351, 999; C6 at 819; D sharp 6 at 306).

**Measured.** First 0.3 s of each accented note, unweighted, c18 -> c22:

| qn (bar) | pitch / vel / CC11 | Flute 1 level | Flute 1 - Violins I | over the note before |
|---|---|---|---|---|
| 315 (106) | G6 / 90 / 103 | 26.9 -> 31.7 | -3.6 -> **+0.7** | -1.0 -> +3.7 |
| 351 (118) | G6 / 90 / 103 | 27.1 -> 31.8 | -2.8 -> **+1.6** | -0.8 -> +3.9 |
| 999 (334) | G6 / 90 / 100 | 24.5 -> 33.8 | -2.2 -> **+6.5** | -1.3 -> +4.0 |
| 819 (274) | C6 / 90 / 91 | 19.6 -> 25.8 | -2.1 -> **+3.5** | -2.4 -> +3.8 |
| 789 (264) | C6 / 70 / 68 | 21.1 -> 26.7 | -4.1 -> **+5.3** | -3.9 -> +1.7 |
| 306 (103) | D#6 / 90 / 98 | 22.3 -> 26.8 | -8.9 -> -4.4 | +6.2 -> +7.8 |
| 904 / 908 (302-303) | | +7.3 / +10.8 dB | -7.2 -> +0.1 / -16.3 -> -5.4 | |

- The G6s (pitch 91) are hot at every occurrence.
- The other C6s are not (123 +2.8, 207 +1.2, 345 -3.4, 945 +0.1 over the note before).
- At 999 the flute's accent is the loudest sound in bar 334. With the summit-cut change (finding 2) it adds 9.3 dB to that note.
- c22's actor lists bar 264's +1.8 on the master as this row.

**Cause.** "Sus Accent MAX" at velocity 90 plays the middle attack layer (75-114) at full CC11 (manual p.101: velocity sets the attack). G6 is the hottest region of that layer.

**Fix** (`build/mix.json`, Flute 1 `region_gain_db`, Opus row volume, not the fader): add `{"rows": ["Sus Accent MAX"], "pitch_db": {"91": -3.5}}`.
- Leave velocity 70 / 90 and the other pitches as they are: they give the +1..+2 dB median Dan asked for.
- Then rerun this table for Flute 2, whose p90 is +8.1 per critic A's brief. If its hot notes share a pitch, apply the same pitch gain.

**Expected** (i):
- 315 / 351 over Violins I +0.7 / +1.6 -> about -2.8 / -1.9;
- 999 +6.5 -> +3.0, and about +1 with finding 2;
- 315 / 351 / 999 about +0.5 over the note before, within Dan's +1..+2 band.

### 2. Bars 333-335 (qn 996-1004.75, ff before the fff): the woodwinds now lead the strings, and the summit's step shrank (m)

**Print.** Everything ff at 996, with a crescendo from 1002 into fff at 1005. Strings and woodwinds play the theme head; brass plays f/ff with no accents.

**Measured.** Family sums, unweighted:

| window | c18 winds - strings | c22 winds - strings |
|---|---|---|
| 996-1004.75 | -0.1 dB | **+2.9 dB** |
| 1005-1011 (summit) | -1.8 | -1.0 |

- Loudest stems at 996-1004.75: Flute 1 32.7, Violins I 30.7, Clarinet 2 30.5 (its held B4), Horn 1 29.0, Clarinet 1 28.6. In c18 the first three were Violins I, violas, Clarinet 1.
- On the master, bars 333-335 rose 1.6-2.0 dB against c21 while the summit rose only 0.6.

**Cause** (data). c22 moved the twelve woodwind and celli summit cuts from 996 to 1004.75 and halved them. That was right for the celli (their fff now exceeds their ff), but the woodwinds lost their cuts over the ff bars too.

**Fix** (`build/roles.json`, slow role rows, the c22 values).
- Start the woodwind rows at 996 again:
  - Flute 1 [996, 1017, -2.0], Flute 2 [996, 1017, -2.0];
  - Clarinet 2 [996, 1017, -2.5], Clarinet 1 [996, 1017, -1.0];
  - cor anglais [996, 1017, -1.5], Oboe 2 [996, 1017, -2.0];
  - Bassoon 1 [996, 1017, -2.35], Bassoon 2 [996, 1017, -0.75];
  - Oboe 1 [996, 1017, -0.5], Contrabassoon [996, 1017, -1.5].
- Keep Violoncellos [1004.75, 1016, -3.0] and Horn 1 [1004.75, 1014, -1.5] where they are.
- Each row replaces the track's [1004.75, 1017] row, so the level does not step at 1004.75.

**Simulated on the c22 stems** (m):
- winds - strings +2.5 / +2.4 / +3.3 -> +0.8 / +0.7 / +1.5 dB in bars 333 / 334 / 335;
- sum of all stems -0.63 / -0.68 / -0.78 dB there, summit unchanged.

So the master step into bar 336 grows by about 0.7 dB, more with finding 1. Critic C should confirm the mp3 summit lead (spec item 2).

### 3. Trio climax, bars 217-219 (qn 648-660): Flute 1, printed mf < f in unison with Violins I's ff, is 5-7 dB over Violins I (m)

**Print.**
- Violins I: B5 - C sharp 6 ... A6 (653) ... A5, cresc. to ff at 653.
- Flute 1: the same notes in unison, mf at 648, < f at 653, > after.
- Violins II and Clarinet 1 also carry the tune (ff).

**Measured.** Flute 1 minus Violins I per 1.5 qn from 648: -3.8, +1.9, +5.2, +4.8, **+6.8** (654), +3.0, -0.1, -0.3. Over 648-660 Flute 1 equals the sum of Violins I + Violins II + Clarinet 1 (-0.3 dB). It is the loudest stem at 654-660 (A-wtd 28.7 against Violins I 25.7). The c18 numbers are the same, so this has been present all along.

**Cause** (data). The flute's printed mf -> f hairpin carries +3.9 dB of volume gain (vol_db 0.1 -> 3.9 at 648-653) on top of CC11 72 -> 91. Violins I's ff arrival carries +3.0. A one-dynamic-lower doubling ends louder than the line it doubles.

**Fix** (`build/roles.json`, role: colour doubling under the ff violins). Flute 1 [648, 660, -4.0], joining the existing [660, 669, -2] (one row stepping -4 -> -2 at the 660 note boundary, 0.5 qn ramp). The hairpin itself stays printed.

**Expected** (i):
- Flute 1 -1.0..+2.8 dB against Violins I at 651-656, with Violins I leading the A6;
- the flute about -4.3 dB under the three tune sections together;
- mp3 bar 218 about -0.3 M (the ride row already lowers it).

### 4. Do not lower the counterstatement clarinets further, and fix the inner-line measure (m)

See the first answer above. The remaining "clarinets over the tune" reading in bars 38-39 and 41 is an artifact of the measure. Every bar 37-43 has the tune ahead of the clarinets in its own bands by a median of +8.5 dB or more. Change the line definition in the actor's measure (`cycles/c20/actor_scripts/inner20.py` and its successors) so that doubling tracks join the line. Otherwise the next cycle will cut the accompaniment of every doubled tune.

## Not ranked
- Trumpets' repeated quarters, 101-120. Onset level 25.4 / 24.6 against Violins I's ff theme at 29.4. Per 24 qn they sit 9 dB under Violins I (A-wtd 21.4 against 30.8): present, not on top (m).
- Summit brass. The brass family is 5.1 dB under the strings at 1005-1011, as printed (f/ff under fff) (m).
- Solo violin, 349-356. 5.4-11 dB over Flute 1's "sempre pp, col Vl. solo" and over Violins II, with Horn 1's motto tail following (m).

Do not touch:
- the c22 clarinet rows [108, 129];
- the coda-build Violins II -3 / violas +5;
- the celli summit row from 1004.75;
- Horn 4 [648, 669, +3] and the deleted bass clarinet row (its line now leads at 633-651);
- the delivery chain and its ride rows;
- Flute 1 / 2 on "Sus Accent MAX" at velocity 70 / 90 (only the G6 region gain changes).
