# Cycle 15, critic B: balance and levels (review of the c14 render)

Method. Every number comes from my own scripts on `cycles/c14/render/` (35 stems and the master), the c14 mp3, the c13 master and `cycles/c14/rendered_build/parts.json` (equal to `build/parts.json`). Levels are RMS in dBFS on mono sums. "A" is A-weighted, "Z" unweighted. A note's "slot" level is the A-weighted RMS from its score onset to its score end (capped at 2 qn). Score time uses the c14 tempo map. Nobody listened: every audibility judgement is marked inferred.

## Manual notes

Third round, no fixed pages. I read the pages behind finding 1 (the theme's mixed rows) in full: May 2021 HO manual PDF pp. 64, 91-94, 150-151. `loop/MANUAL-GAPS.md`: summary table, the c36 staccato-row result and the Finale results were read.

| What the manual says (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Note velocity sets loudness and dynamic layer on short instruments (Staccato, Staccatissimo, Marcato); CC11 shapes long instruments and crossfades their layers (p. 64, p. 150-151). | First theme, Violins I / II, Violas, Horn 1 (bars 11-26, 151-170): one melodic line alternates "Leg Slur MAX" / "Leg BC MAX" / "Sus MAX" (CC11) with "Staccatissimo RRx9" / "Stac RRx9" / "Marc Shrt RRx4" (velocity). | No. The two mappings are not matched: at ff the Violins I staccato notes are 8.1 dB over the Sus MAX eighths beside them, at f 5.1 dB (finding 1). |
| Marcato Sustain plays a marcato sample plus the looped sustain: "extra power at the start of the note" (p. 91-92). On LITE instruments CC1 handles dynamics and vibrato together and CC11 only the overall loudness (p. 64, p. 151). | The planned one-row theme (`STEADY_LINE`) on "Sus Marc LITE". | Not built yet. Two consequences for levels: the front-over-body difference is the row's design, so quarters and longer need a level shape; and the row's printed dynamic must be written in CC1, or f and ff will differ only in volume (finding 1, conditions). |
| Staccato On Bow: the bow stays on the string and stops; Staccatissimo is like Staccato but shorter; staccato rows have 9-16 round robins (p. 94). `MANUAL-GAPS` c36: in the 1st Violins KS Master "Staccatissimo RRx9" plays the "V1 Stac" samples (names swapped). | The theme's dotted quarters inside the slurred line. "Stac On Bow RRx9" is a row of all four upper string KS Masters (`ks_maps.json`) and is not used. | Not used. A's choice; from the level side any short row needs the check of finding 1. |
| Sustain alternates up-bow and down-bow samples by round robin (p. 91). | Double basses "Sus MAX" under the second theme, qn 264-300. | The CC16 resets fix the order (c14), so the weak takes are the same in every render and per-note trims hold (finding 3). |
| CC7 sets a track's ceiling against the other tracks; CC11 shapes the line (p. 64, p. 151). Send CC1 and CC11 before the first note (p. 151). | Every track. | Followed: balance is in the volume envelope and mix.json, the pre-roll carries the controllers. |
| Pizzicato has 2 or 4 round-robin samples per note (p. 92). | Celli and basses under the three solos. | Followed since c14: pluck peaks SD 0.5-1.0 dB (celli), 0.5-0.7 dB (basses) in all three passages (measured). |

## Findings, ranked

### 1. First theme: the notes of one line differ by 5-9 dB according to their row and length (measured; "choppy" inferred)

Where: Violins I and II, Horn 1, bars 11-26 (qn 40-104, f) and bars 151-170 (qn 600-680, ff); heads also on Oboe 1 (72, 600, 632), Violoncellos (120, 1064), Clarinet 2 (1056).

What is wrong. Dan heard Movement I's theme as choppy. Besides timing (A's lens), the levels inside the line are uneven in three ways.

(a) Rows. Median slot level by row and note length, Violins I:

| | Sus MAX eighths | Leg Slur MAX quarters | staccato-row notes | Leg BC MAX halves (heads) |
|---|---|---|---|---|
| bars 11-26 (f) | -45.1 (22 notes) | -41.3 (8) | -40.0 (12) | -36.9 (5) |
| bars 151-170 (ff) | -39.8 (46) | -37.1 (5) | -31.7 (16) | -32.7 (4) |

At ff the "Staccatissimo RRx9" notes are 8.1 dB over the bowed eighths next to them and 5.4 dB over the slurred quarters. At f the bowed eighths are 3.8 dB under the slurred quarters and 5.1 dB under the staccato notes. Bar 11-12 on the Violins I stem, note by note (slot, A): -37.3, -44.0, -45.0, -40.3, -46.2, -46.4, -43.6, -40.9; 60 ms peaks -31.9, -41.2, -43.6, -39.4, -44.3, -45.3, -41.0, -39.6. The master follows: -32.1, -38.1, -39.2, -36.3, -38.5, -39.2, -37.9, -36.6. Violins II at ff: "Stac RRx9" -37.9 against Leg Slur quarters -44.7. Horn 1 at f: "Marc Shrt RRx4" eighths -43.2 against its legato notes -47.4 to -47.7 (4.3 dB over); at ff they are level (-38.4 / -37.5 to -39.3).

(b) Heads (open item B #2). Fall from the accented head note to the second note (slot, A): bar 11 Violins I 6.6, Violins II 8.7, Violas 4.5 dB; bar 19 Violins I 6.8, Violins II 7.1; bar 151 Violins I 3.2, Violins II 6.2, Violas 4.2; master bar 11 6.0 dB. The f head of bar 11 (-37.3) is as loud as the ff head of bar 151 (-36.7); the difference between f and ff is only in the notes after it (-44 against -39). Dan's accent rule is 2-4 dB. Other heads: Violoncellos qn 120 8.6 dB and qn 1064 7.0; Clarinet 2 qn 1056 8.5; Horn 1 4.0-5.3 at 40, 72, 600, 1056 and 1064 (1.1 at 632).

(c) Oboe 1 has the accent inverted: its head notes at 72, 600 and 632 ("Sus MAX", -45.0 / -44.1 / -44.0 Z) are 4.4-5.6 dB under the slurred notes that follow (-39.4, -38.5).

Audible (inferred): yes. A listener hears a loud first note, a weak run of bowed eighths and staccato notes that stick out. This is the main theme, stated four times, with Violins I the top stem.

Fix with the present rows (`build/score_config.py`):
- `ROW_TRIM_DB["Violins I"]`: "Staccatissimo RRx9" (-3.0, 80) -> (-6.0, 80); "Sus MAX" (-1.5, 80) -> (0.0, 80). Predicted Violins I medians: f Leg quarters -41.3, Sus eighths -43.6, staccato -43.0 (spread 2.3 dB, now 5.1); ff -37.1, -38.3, -34.7 (spread 3.6, now 8.1). `ROW_TRIM_DB["Violins II"]`: add "Stac RRx9": (-3.0, 100) (the second value is the CC11 floor, so it acts at ff only); "Sus MAX" (-4.0, 80) -> (-2.5, 80).
- Horn 1 "Marc Shrt RRx4" in qn 40-104: velocity 15 lower or a -3 dB trim on the 12 notes.
- Heads, `LEVEL_SHAPES_S` (seconds from the score onset): Violins I and II at 40.0 deepen the c14 shape to `[(0.05, 0), (0.15, -5), (0.70, -5), (0.90, 0)]`; Violins I and II at 72.0 add `[(0.05, 0), (0.15, -3), (0.80, -3), (1.00, 0)]`; Violins II at 600.0 the same with -2.5; Violoncellos at 120.0 -4 and at 1064.0 -3; Clarinet 2 at 1056.0 -4. Do not lift the second note: it is a row-change join with two start states.
- `build/note_trims.json` "Oboe 1": `"72.0": 4.0, "600.0": 4.0, "632.0": 4.0` (heads on "Sus MAX", not legato targets).

Conditions if `STEADY_LINE` is built (A's item, c15's first): run the same table on the range render before the full render. Targets for either route: head 3-4 dB over the median of the phrase's other notes on each string stem (bar 11 and bar 19 now 6.6-8.7); every other note of bars 11-14 and 151-154 within +-2 dB of that median (now -45.0 to -40.3 at f, -41.5 to -35.9 at ff on Violins I); master fall at bar 11 at most 4 dB (now 6.0). On "Sus Marc LITE" write the dynamic into CC1 (manual p. 64), and give each quarter or longer a shape that lowers the first 0.15 s rather than lifting the body after it, so the hall does not carry a louder front (S3).

### 2. Downbeats of bar 222 (qn 884) and bar 245 (qn 976): all strings change bow together and drop 6-16 dB for 0.2-0.3 s under a printed crescendo; before each, the celli's G2 is the loudest stem (measured)

Where: Violoncellos, Violins I, Violins II, qn 880-885 and 972-977. This is the cause of two open items: the bar 222 dip and the uneven stringendo.

Evidence, 40 ms windows around qn 884 (seconds from the beat):
- Violoncellos: -28.7 (-0.3 s), -26.8, -24.3, -24.3 (-0.12 s), -28.5, -35.6 (-0.04 s), then -39.6, -39.4, -40.7, -40.0 (+0.12 s), -37.2, -35.9, -35.1. The printed line is mp crescendo to f. The whole note G2 (qn 880, "Sus MAX") grows from -52.7 to -26.8 over the bar and is the loudest stem of the orchestra in its last 0.3 s (Violins II -30, Trumpet 1 -45.6; the master's 30-150 Hz band is -24.0 against a full-band -22.3). The D3 that follows ("Leg BC MAX", f) has a body of -35 to -36: 7-8 dB under the end of the crescendo it completes.
- Violins II: -30.3 at the beat, then -36.1, -39.7, -41.5, -40.1 (+0.16 s), back to -34 at +0.3 s. Violins I: -35.8, -38.5, -42.8, -43.4, -38.5, back to -34 at +0.3 s. Both are "Sus MAX" notes starting on the beat with no lead.
- Master: -23.2 before, -20.5 / -20.8 at -0.2 to -0.12 s, then -25.3, -25.7, -25.1, -25.1, -25.3, -25.6 over the first 0.3 s after the beat, -23.5 at +0.4 s. That is 2.2 dB under the level before the beat and 5 dB under the peak just before it.
- qn 976 is the same: celli -31.1, -28.7, -27.4 before the beat, then -41.6, -41.4, -42.1, -41.8; master -24.4, -22.8, -22.2, then -26.3, -25.9, -26.7, -27.9, -27.1.
- The celli's volume envelope steps up at the next note's moved note-on, 0.14 s before the beat (883.72: +1.2 -> +5.3 dB; 975.68: -3.1 -> +0.9), while the G2 still sounds. Removing that step alone changes the master by under 1 dB (simulated), so it is a minor part.

Audible (inferred): a swell that peaks just before the barline and a hole on the downbeat, twice, each time on the way into a climax (223 and 247).

Fix:
- Violoncellos, `LEVEL_SHAPES` on the two G2 whole notes: `[(881.0, 0.0), (883.0, -4.0), (883.70, -5.0), (883.72, 0.0)]` and `[(973.0, 0.0), (975.0, -3.0), (975.66, -4.0), (975.68, 0.0)]` (the return to 0 sits where the existing step for the next note already is). And a front on the next note, `LEVEL_SHAPES_S` at 884.0 and 976.0: `[(-0.02, 0), (0.0, 4), (0.25, 4), (0.45, 0)]`.
- Violins I and Violins II at 884.0 (both pitches) and 976.0, Violas at 976.0: start the new bow before the beat. `ROW_LEAD_S` "Sus MAX" 0.08 s with `ROW_LEAD_KEEP_END` (the stroke treatment of c14), plus `LEVEL_SHAPES_S` `[(-0.08, 0), (-0.06, 3), (0.20, 3), (0.40, 0)]`.
- The timpani crescendo roll and the winds are in order and stay.

Targets: master mean over 0-0.3 s after qn 884 and after qn 976 within 1 dB of the mean over the 0.3 s before (now -2.2 / -2.3 dB); no string stem more than 6 dB under its pre-beat level in any 40 ms window after the beat (now 11-16); celli not the loudest stem in 883-884 (within 2 dB under Violins II). For the stringendo's last quarter (qn 983): Horns 1-2 and Trumpets 1-2 have a printed quarter rest there (their note ends at 983.0), so the master's -26.3 against -24.0 at 982 is the score, not a fault. Do not fill it.

### 3. Second theme entry, bars 67-68: almost no bass under the violins (measured)

Where: Double basses "Sus MAX", qn 264-272, and qn 288.

Evidence. Stem levels (Z) of the mp line: 264 -56.4, 268 -54.3, 270 -55.6, then 272 -48.3, 275 -49.3, 276 -47.5, 278 -47.7, 280 -51.4, 284 -49.6, 288 -52.6, 290-298 -46.4 to -49.1. The first three notes are 5-7 dB under the line's median (-49.1). The master's 30-150 Hz band on the same notes: -58.9, -52.2, -59.3, against -39.7 to -51.7 from qn 272 on (median -44.5). The celli play an octave higher at -43 to -50, so the bass octave is carried by the basses alone. c14 trimmed the loud notes (276, 278, 294, 296) down and left these; the actor's log calls 268 / 270 "still the weak ones". The takes are fixed by the reset at 264 (two-valued bow-direction samples, manual p. 91).

Audible (inferred): the violins' cantabile enters over a thin floor and the bass appears in bar 69. On headphones that reads as the bass coming in late.

Fix: `build/note_trims.json` "Double basses": `"264.0": 5.0, "268.0": 4.0, "270.0": 5.0, "288.0": 3.0`. These are "Sus MAX" notes, not legato targets. Targets: every arco note of 264-300 within +-3 dB of the running median of five notes (now -7.3 to +2.7 against the whole line's median); master 30-150 Hz in bars 67-68 within 6 dB of bars 69-71 (now 8-15 under).

### 4. Development call, bars 102 and 106 (qn 406, 422): the accented arrival jumps 10 dB on Flute 1 and Clarinet 1 while Oboe 1 falls (measured)

Where: Flute 1, Oboe 1, Clarinet 1 (each "1.", mf with a crescendo to an accented quarter), qn 401-407 and 417-423. The three winds are alone.

Evidence. Slot levels (A) of the four eighths before the arrival and of the arrival: Flute 1 -50.6, -45.7, -44.8, -44.1 -> -34.0 at 406 (peak -31.0); Clarinet 1 -51.7, -48.4, -51.9, -48.8 -> -38.9; Oboe 1 -48.2, -44.0, -39.1, -40.5 -> -43.9. At 405-405.5 the oboe is 4-13 dB over the other two; at 406 the flute is 9.9 dB over the oboe. The master goes -43.6, -40.5, -38.6, -39.2 -> -32.3: a 6.9 dB step on the accent. Second call: Flute 1 -40.4, -41.0, -40.2 -> -33.8 at 422 (its C6 at 418.5 is also at -34.4 between -37 and -41). The flute's -34.0 at a printed mf equals its fff level (-34.1 median) and the Violins I answer at f in bars 108-109 (-34.2 to -36.2). CC11 moves 84 -> 86 across the jump, so it is the samples (C6 and F6 on "Leg Slur MAX") plus the accent. Dan's rule: an accent is 2-4 dB of weight.

Fix, `build/note_trims.json`: "Flute 1" `"406.0": -5.0, "418.5": -3.0, "422.0": -4.0`; "Clarinet 1" `"406.0": -4.0`; "Oboe 1" `"406.0": 3.0`. They are legato targets: use the short mirror ramp (`LEG_JOIN_TRIM_HOLD`) for the positive one. Remove the c13 `+1.5` on Flute 1 404-408 if it is still in. Targets: each arrival 3-5 dB over the mean of its four eighths; the three winds within 3 dB of each other at 406 (now 9.9); master step into 406 at most 4 dB.

### 5. Bar 272 (qn 1084): the trumpets' A5 is the loudest trumpet note of the movement and the Largamente arrival is not louder than the bar before it (measured)

Where: Trumpet 1 (playing Trumpets 1-2 a2), qn 1084-1086; also Oboe 2 at 888 and 1108.

Evidence. Trumpet 1 note levels (Z) at ff with equal controllers: C5 -31.4, D5 -30.6, E5 -28.0 to -28.8, A5 at 1084 -23.6. The A5 is 1.1 dB over the fff C5 of bar 263 (-24.7, envelope +8.2 dB) and 4.8 over the final chord (-28.4). In the first half of bar 272 Trumpet 1 alone is -24.2 against -22.5 for everything else; by A-weighted bars it is -25.5 against -28.8 for the sum of all other stems, while flutes, oboes, clarinets and both violin sections play the same line. Rimsky-Korsakov's forte table (Trumpet = 2 Horns, Horn = 2 woodwinds, Violins I = 2 woodwinds; book p. 33, `reference-books/text/rimsky-principles/p0051.txt`) puts two trumpets about 6 dB over Violins I; here it is 12.4 dB. Master per bar (Z): 271 -23.5, 272 -21.1, 273 -21.2, 274 -21.6. The printed shape is allargando and crescendo into ff at 273 with the low brass entering.

Fix: `build/note_trims.json` "Trumpet 1": `"1084.0": -4.0` (a "Sus Non Vib MAX" note). Simulated on the stems: bar 272 master -21.1 -> -22.0, its first half -20.1 -> -21.4; bar 273 then stands 0.8 dB over bar 272. Optional: `"1064.0"` to `"1068.0"` -2 (bar 267: Trumpet 1 -27.2 A against a master of -24.6). Oboe 2 at qn 888 and 1108 reads -31.4 / -31.8 A, 7 dB over Oboe 1 and level with Violins II: `note_trims` "Oboe 2" `"888.0": -4.0, "1108.0": -4.0`. Targets: Trumpet 1's A5 within 1 dB of its notes in bar 258 (-26.6 Z bar level); master bar 273 at least 0.5 dB over bar 272; the mp3's 272 -> 273 step (now +2.0 dB from the final ride row) not smaller than now.

### 6. Bar 42 (qn 164-168): the printed p lands at the level of the pp that follows (measured; answers the coordinator's question)

Evidence. Master per bar 39-44 (Z): -28.1, -33.5, -38.3, -44.8, -44.7, -42.9; steps 5.4 / 4.8 / 6.5 dB, so the diminuendo itself is even. Bar 42 (p) equals bar 43 (pp): strings in bar 42 Violins I -56.8, Violins II -58.0, Violas -56.0, Violoncellos -60.8 (A); in bars 43-45 Violins I -60.0, -56.8, -57.1, Violins II -56.8, -54.6, -54.1, Violas -57.2, -56.1, -58.5, Violoncellos -63.2, -60.6, -60.5. The strings' p is 0-3 dB over their pp, and Violins II are louder at pp than at p. Against the c13 master with the same script bar 42 is 3.0 dB lower (-41.8 -> -44.8). In the mp3 bars 41-44 read -29.6, -34.8, -34.4, -32.7: the p bar is under every bar of 43-48 (-34.4 to -30.8). Verdict: the diminuendo is right, bar 42 is about 2 dB too soft.

Fix: `LEVEL_SHAPES` on Violins I, Violins II, Violas, Violoncellos, Double basses: `[(163.9, 0.0), (164.1, 2.0), (167.0, 2.0), (168.0, 0.0)]` (an upward step at the p onset, a ramp down into the pp; nothing cuts a tail). Leave `HP_CURVE` and the 164 ride row. Targets: master bar 42 1.5-2.5 dB over bar 43's string level (bar 42 at about -42.8 Z); master step 41 -> 42 4-5 dB; mp3 step 41 -> 42 3.5-5 dB (now 5.2).

## Answers to the coordinator's items

- B #2 first-theme head: audible, finding 1 (targets there). Bar 222 dip and stringendo: finding 2; the target of 1 dB is reachable only by treating the string bow changes, not by lifting 884 further.
- Bars 39-42: finding 6. Cello pitch trims: no balance fault; in bar 149 the low band is inside the earlier limit by 0.2 dB and I would leave it.
- Basses arco 268 / 270: audible, finding 3. Violins II at 300 and Flute 2 at 618 / 650 are timing items with no level fault (Flute 2 is an inner voice 11-12 dB under the mix).
- Join level holes after the Horn 1 / Trumpet 1 lead changes (measured, 30 ms windows from -0.1 to +0.15 s around each join, against the mean of the two note bodies): Trumpet 1 bars 51-66 median 2.8 dB, deepest 6.1 (246) and 6.0 (208); Horn 1 bars 11-26 median 3.6, deepest 8.9 (65), 7.6 (50); Horn 1 bars 151-170 median 2.3, deepest 7.9 (626); Trumpet 1 bars 265-272 median 3.5, deepest 7.4 (1060); cor anglais bars 171-186 median 3.7, deepest 9.6 (738). No join is deeper than 10 dB and none needs a level fix. The minimum falls 115-165 ms after the beat at Horn 1 43.5, 74, 602, 626, 635.5, Trumpet 1 208 and 1087, cor anglais 708: hand these to A as late joins.
- Pizzicato line: good. Peaks range 2.1 / 2.0 / 5.5 dB (celli, three passages) and 2.2 / 1.6 / 2.9 dB (basses). The summed pizzicato peak (120 ms) is 3.6-7.1 dB under Trumpet 1's bar level in bars 51, 55, 59 and 63. Keep.
- Clarinet "dal niente" entries, harp at 524, Flute 2 against Flute 1: the actor's numbers stand (Flute 2 against Flute 1 +0.4 / -1.8 / -0.1 / -0.3 dB in the four a2 bars); I did not re-measure them, and in my bar tables neither is a top stem where it should not be.
- Trumpets 1-2 in bars 247-250: Trumpet 1 -32.8, -32.1, -35.1, -32.8; Trumpet 2 -34.3, -31.1, -36.0, -36.2; Horn 1 -34.2, -35.9, -35.9, -31.8; Violins I -35.4, -33.1, -38.4, -33.8 (A). Balanced; keep the c14 shapes.
- Ride holds: mp3 minus master is 10.0-10.4 dB over bars 42-50 and 10.6-11.0 over bars 170-177. Flat. Keep.
- Legato entries of bars 67 / 187: at 744 Violins I are within 2 dB of their body from the beat on (-43.5, -41.2, -41.0). At 264 the +5 dB front makes a bulge: -42.9 (0-0.1 s), -40.2, -36.9, -36.1, then -39.1, -40.9; the body is -40.5. End the 264 front earlier: `[(-0.33, 0), (-0.31, 5), (0.02, 5), (0.20, 0)]` on Violins I and II. Small.
- Wetness: not touched by any fix here. No fix adds a fall after the hall; the only downward ramps are before a note change or into a softer dynamic.

## Other checks (measured, in order)

- Solos over accompaniment (A, bar levels): Trumpet 1 bars 51-66 leads the next stem by 4.2-13 dB; Bassoon 1 bars 115-120 by 6-14 dB; cor anglais bars 171-186 is the top stem in every bar with the muted trumpet 2.2-3.5 dB under it; Violins I lead the first non-violin stem in bars 67-76 by 2.8-9.2 dB (smallest in bar 74, against the harp).
- Harp, bars 123-128 (p arpeggios): 3-5 dB under the master (Z) in 123-124, 8-10 dB under in 126-128 where Clarinet 1 enters mf; 80 ms peaks -60 to -56 A. Present as an accompaniment; no change.
- Counterstatement, bars 27-34 (Z): the theme group (Horn 3 playing 3-4 a2, basses, tuba, bass clarinet, celli, violas, bassoons, contrabassoon) holds the three top stems in seven of eight bars; violins' countersubject -36.4 to -38.8 each. In order.
- Trumpets with movement II's theme B, bars 211-216: Trumpet 1 -28.0 to -33.9, Trumpet 2 -29.2 to -35.7, the next stem 4-8 dB under Trumpet 1. In order.
- Chorale: bars 224-225 brass f (Trumpet 1 -40.4 / -36.8, Trombone 1 -40.5 / -36.3, Horn 3 -40.7 / -44.4) over the tremolo (Violins I -44.2, Violins II -46.1); bars 226-228 violins and woodwinds ff over the brass, as printed. Bars 255-264: Trumpet 1 (a2) and Horn 3 (a2) alternate as top stem; in bars 259-260 Trombone 1's D4 (-27.1) and Horns 1-2 (-28.3) carry the chorale tune an octave under the trumpets (-30.6): acceptable, Trombone 1's D4 is 4 dB over its other ff notes.
- Timpani: 18 long notes, each at least 9.5 dB under the master in every 0.5 s window; rolls without a printed crescendo fall after the first stroke (qn 920: -37.1, -42.9, -43.9, -44.2); the roll of 273-276 is 16-19 dB under the master with a 30-150 Hz share of -6.2 dB; arrival 223 share -7.0 dB, final chord -8.4 dB. Crash cymbals: 10-12 dB under the master, 4-12 kHz share -1.3 to -2.4 dB for 0.5 s, -9 to -10 dB after 1 s. Bass drum: 30-100 Hz share -4 to -6 dB for 0.5 s. None covers.
- Dynamic mapping, median slot level (A) of notes of 0.9 qn or longer outside hairpins: p Flute 1 -51.8, Oboe 1 -50.1, Clarinet 1 -49.1, Bassoon 1 -55.1, Horn 1 -54.8, Trombone 1 -56.3, Violas -53.0; f -42.7, -43.6, -43.2, -45.6, -44.2, -40.4, -42.6 (Violins I -39.4, Trumpet 1 -37.2); ff -37.0, -40.6, -36.9, -42.0, -35.5, -35.1, -38.6 (Violins I -36.5, Trumpet 1 -31.0). No family has a reversed pair between p, f and ff. Flute 1's mf (-42.3) equals its f (-42.7); the hot mf notes are those of finding 4.

Not checked this cycle: loop pulsing on held notes, the brass tilt-jump accent check, S2 onsets, repeated-note separation (S1).

Research defaults: no finding here rejects one. Finding 1 applies FINDINGS section 7 (short-note dynamics by velocity, matched against the CC lane) and finding 2 the rule that doubled lines share one curve.

Do not touch: `build/pluck_trims.json` and the resets at 200, 456, 680; the two ride-hold rows and the final ride row; Trumpet 1's solo roles in 200-264 and 680-732; the c14 trumpet shapes at 984-1000; the timpani roll shapes and trims, the first strokes of timpani, bass drum and crash at 223, 263 and 278; the `HP_CURVE` keys; the c13 Bassoon 1 and Horn 1 shapes; Flute 2's c14 trims; the basses' c14 trims at 276, 278, 294, 296, 299; the returns, sends and release fades (wetness); the bars 255-264 roles; `FINAL_RING`; the printed rest of the brass at qn 983.
