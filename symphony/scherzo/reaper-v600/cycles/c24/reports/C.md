# Cycle 24, critic C (holistic): the c23 render and its delivered mp3

## Manual notes

MANUAL-READING.md has no row for c24, so I picked pages for what this render shows (the cantabile lines and repeatability), and read MANUAL-GAPS.md in full.

| Page (May 2021 PDF) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.143 | Monophonic True Legato: velocity sets only the transition time (50-60 slower, 110-127 tighter). "When Note Velocity is used to control Legato Speed, it does not affect loudness." | the first notes of the trio's and the Meno mosso's legato phrases (v41-v63) | Yes. Velocity is not why the entries are soft. CC11 is (finding 1). |
| p.144 | Round Robin Reset (CC36) makes every playback identical. Without it, Opus carries on from wherever the round-robin cycle stopped, so a passage plays different takes on each pass. | every RR row; bar 58 (fugato) | Partly. Bar 58 moves ±2.9 dB from render to render on unchanged data (finding 5). |
| p.108 | Woodwind sustains: 3 dynamic layers crossfaded on the controller. "Sus Expressive" has "a slower attack and a gently increasing vibrato". | woodwind phrase entries in the trio, codetta and Meno mosso | Not used. Sus Exp is the library's own way to swell into a phrase, where the render uses a CC11 ramp (finding 1; MANUAL-GAPS #8). |
| p.109 | Legato Repetitions (LegRep RRx4): retongued repeats inside a sustained phrase | the clarinets' REP_ROW | Yes (in use). |
| p.78-79 | Solo cello legato types (Leg Bow Change, Fast, Smooth) | the library is not installed | Not applicable. The section KS Masters' "Leg BC" row is the nearest (finding 2). |
| MANUAL-GAPS #6 | Timpani Hrd KS for bars 1-340 (score: "hard sticks"; "soft sticks" from 341) | every stroke and roll before bar 341 | Pending since c03 (finding 4). |
| MANUAL-GAPS #8 | Expressive rows and slower legato velocities on the cantabile lines | trio tune, Oboe 1 185-196, Violin I solo | Only the celli's v80 (c10). The rest is not used. |

## How the movement sounds as a whole (delivered mp3s, measured)

Mean momentary loudness per section (LUFS; c00 is the undelivered port baseline at -20 LUFS):

| section | c00 | c18 | c20 | c22 | c23 |
|---|---|---|---|---|---|
| integrated / LRA / p10 short-term | -20.0 / 13.9 / -29.8 | -14.1 / 12.0 / -21.7 | -14.1 / 12.3 / -21.7 | -14.0 / 10.6 / -20.2 | -14.0 / 10.5 / -20.2 |
| intro 1-12 | -26.0 | -18.4 | -18.6 | -17.1 | -17.1 |
| theme A 13-28 | -25.5 | -17.3 | -17.6 | -16.2 | -16.2 |
| F major 73-88 | -21.9 | -17.6 | -17.8 | -17.1 | -17.1 |
| ritmo di tre battute 89-100 | -27.6 | -19.6 | -19.8 | -18.9 | -18.9 |
| link 141-152 | -25.2 | -20.1 | -20.8 | -18.8 | -18.8 |
| trio, clarinet tune 153-168 | -22.3 | -17.1 | -17.4 | -16.0 | -16.0 |
| trio, celli tune 169-184 | -23.6 | -16.1 | -15.5 | -14.4 | -14.4 |
| trio ff 209-224 | -19.6 | -13.8 | -13.7 | -13.6 | -13.8 |
| codetta 225-240 | -23.5 | -18.9 | -19.0 | -17.6 | -17.6 |
| tutti 101-120 / 301-320 | -16.0 / -15.4 | -9.8 / -10.3 | -9.5 / -9.8 | -9.6 / -9.8 | -9.6 / -9.8 |
| summit 336-339 | | -7.5 | -7.5 | -7.9 | -7.9 |
| Meno mosso 341-348 / solo 349-356 | -26.9 / -25.0 | -20.2 / -17.2 | -20.4 / -17.1 | -19.3 / -15.9 | -19.3 / -15.9 |
| close 364-376 | -30.3 | -20.5 | -20.7 | -18.7 | -18.7 |

- **What improved since c18 / c20 (measured).**
  - Every quiet section is 1.0-2.0 LU louder on the mp3. The median bar is +0.9 against c18, and short-term p10 went from -21.7 to -20.2. This is the part of Dan's "too soft" note that level can fix, and it is done: the quietest sections now sit 5-5.7 LU under the -14 integrated level. Real recordings of this repertoire are mastered at -18 to -23 LUFS integrated. The Dvořák reference reads -14.8 with p10 -35.7 and LRA 21.8.
  - The coda now builds into the summit: bars 333-335 read -10.0 / -9.6 / -9.8 and bar 336 reads -7.9, a 1.9 LU step. On c18 the build was flat (-8.4 / -7.8 / -7.9 / -7.3).
  - The coda stretto (bars 326-328) is +3.2..+4.1 LU, and the counterstatement (bars 29-36) +2.8..+4.2.
  - Tutti downbeats on the master reach -3 dB of their 2-5 kHz peak at a median of 23-29 ms after the beat (39 ms on c18). The tuttis do not sound late as a whole, even though the string stems' accent weight still arrives late (critic A's area).
- **What got worse since c18 (measured).**
  - LRA fell from 12.0 to 10.5, which is the spec's floor.
  - The summit's lead over the first tutti fell from +2.3 to +1.7 LU (means of bars 336-339 against bars 105-120).
  - The trio's ff climax (bars 218-219, the A6) is 2.2 / 2.3 dB lower than on c18. It now leads bars 214-217 by 3.5-4.4 LU instead of 5.5, because of two stacked ride rows ([625-671] -2 and [645-659] -1.5) plus the Flute 1 -4 role row.
  - Listened as a whole, c23 differs from c22 by more than 0.5 LU only in bars 58 (-2.9: round robins, finding 5), 208, 218 and 219 (-0.6..-0.9). So a listener will hear c23 much as c22, apart from the bar 23 figure.
- **The room-noise bed (measured).** The bed is about 40 dB under the quietest music. The quietest momentary reading inside the music is now -60 LUFS (c22: -80.7), and it occurs at the very end of the G.P. at bar 340 (t = 244.4 s), where c22 fell into digital silence for about 0.3 s before bar 341. The file tail is now -63.8 dBFS RMS (c22: -92). Everywhere else the music is louder than -35 LUFS. So the bed is audible only in the last 0.3 s of the G.P. and after the final G sharp, at a high playback volume. There it helps: no drop-out to silence. It does nothing for the quiet passages (it makes them no louder or clearer) and costs nothing (hall readings unchanged: G.P. drop 18.9 dB, RT60 1.38 s).
- **Spectrum (measured, the whole mp3 against references).** 20-150 / 150-500 / 500-2k / 2-5k / 5-10k Hz shares: c23 -10.3 / -3.9 / -3.8 / -10.7 / -26.6 dB, Dvořák 9/i -12.1 / -4.1 / -3.4 / -10.5 / -25.3, Movement I c61 -10.3 / -4.5 / -3.4 / -10.2 / -27.8. The whole is neither dull nor boomy. The **quietest quarter** (by short-term loudness) is different: 20-150 Hz is -8.4 dB against -13.9 in the Dvořák's quietest quarter, so the quiet passages carry 5.5 dB more low bass than the reference's (finding 3).
- **Weakest passages now** (inferred from the measurements below):
  - the trio and Meno mosso cantabile lines: every phrase enters too soft and then scoops up (finding 1), and the tunes jump 7-9 dB from note to note (finding 2);
  - theme A's quiet first statement, which sits on a pizzicato bass 7 dB over the celli (finding 3);
  - the ritmo di tre battute timpani on felt sticks (finding 4).
  The bar 23 figure is critic A's.

## Ranked findings

### 1. Lyrical phrases enter 7-12 dB too soft and then scoop up: PHRASE_SHAPE's entry offset buries the first note of the trio's and coda's inner lines (measured)

**Where.** Every "lyric" or "build" phrase in the lyrical spans (bars 45-56, 121-140, the trio 153-240, 277-288, the Meno mosso 341-376). The worst cases, as entry note body minus the median of the next three notes:

| track, qn (bar) | marking | entry deficit |
|---|---|---|
| Oboe 1 132 (45) | | -11.2 |
| Bassoon 1 696 (233) | p dolce | -10.8 |
| violas 670 (224) | | -9.1 |
| Oboe 1 1032 (345) | p dolce | -9.1 |
| basses 576 (193) | | -9.0 |
| Oboe 1 372 (125) | | -8.7 |
| Horn 2 648 (217) | | -8.7 |
| celli 564 (189) | | -8.3 |
| Flute 1 648 (217) | | -8.2 |
| Horn 1 612 (205) | | -8.0 |
| Violins I 576 (193) | | -7.9 |
| Oboe 1 552 (185) | p espress. | -7.7 |
| Flute 1 588 (197) | mp | -7.5 |
| violas 576 (193) | | -7.5 |

23 of the 108 such phrases enter more than 6 dB under their next three notes. The median is -2.3.

**What is wrong.** A player starts a dolce phrase at the printed level and shapes it from there. Here the first note, the one that tells the ear a new voice has come in, sounds as a soft scoop. In a texture that is exactly how an inner line gets lost: Dan's "instruments with interesting internal lines that are hidden behind the melody". Most of the phrases listed are counter-lines and inner voices (violas, bassoon, horns, the oboe's middle part, the Violins I's answer at 576). Because every phrase does the same unprinted swell, the trio also sounds mannered, like a machine.

**Evidence.**
- Oboe 1 at 1032 (p dolce; its first printed hairpin is at 1035): CC11 is 32 at the entry, 36 a quarter later, and 54 on the second note. Bassoon 1 696 (p dolce, crescendo only from 699): 32 / 36, then 54. Flute 1 588 (mp): 41 / 45, then 53-64. Oboe 1 552 (p espress., crescendo from 558): 37, then 39-43, rising to 73 at 560.
- The source is `build/score_config.py` `PHRASE_SHAPE`: "start": -12 at the first onset, "rise" [(0.4 s, +3), (0.8 s, +8)], "peak" +10, scale 1.0 at p / mp, and `family_scale` {"wind": 1.4}. On a wind at p that is -16.8 units at the attack, rising to +11.2 by 0.8 s: 28 units of CC11 inside the first note or two.
- Velocity is not the cause: manual p.143 says legato velocity sets the transition time and "does not affect loudness".
- The research (FINDINGS parts 4 and 22) measured the experts' swell on CC1, which in most of their libraries crossfades dynamic layers. In HO woodwinds and strings CC11 sets level and layer together, so the same unit swing is much louder here: measured, 22 CC11 units took Oboe 1 from -50.9 to -40.2 dB.

**Fix** (`build/score_config.py`, `PHRASE_SHAPE`; instrument side, no envelope):
- "start" -12 -> -4, "rise" [(0.4, 2), (0.8, 4)], "peak" (6, 0.45), "end" -12 -> -8. This keeps the research's centred arch with the peak at 0.45, but at 10 units deep instead of 22.
- For the winds, keep `family_scale` 1.4 on the peak only, or set it to 1.0. On CC11 the winds do not need the boost that Movement I's CC1 test asked for.
- Builds keep "build_cc" but enter at -6 instead of -12. That needs a "build_start" key, a three-line change in `score_to_parts.py` where `tp_` is built for kind "build".
- Alternative to test on two phrases (Oboe 1 1032-1044, Bassoon 1 696-707): the woodwind "Sus Exp" row (manual p.108; in the OB / BS KS Masters, MANUAL-GAPS #8) for the entry note, with the arch left flat.
- Targets: entry deficit median -1..+1 dB; none under -5 dB unless a crescendo is printed from the entry (Flute 1 648 and Violins I 576 have one); bar 23 and the Allegro "drive" phrases unchanged (their type has its own offsets); master per bar within ±0.5 dB outside the lyric spans.
- This also raises the trio's inner lines by 3-8 dB at their entries without any role row, which helps Dan's AirPods case (inferred).

### 2. The trio tune and the Violin I solo still do not sing evenly: half-step legato joins swell 7-9 dB and the Sus MAX re-attacks after ties drop 9 dB (measured; unchanged since c18)

**Where and measurements** (note bodies, 0.1 s after the note-on to 0.05 s before the next one):
- Celli bars 169-184 (qn 504-552, "arco, espress."), c18 -> c23: range 12.7 -> 13.9 dB, std 2.6 -> 2.9, p90 step 6.1 -> 6.8 dB.
  - Steps over 6 dB: 506 +8.6 (A3 after G sharp 3), 507 -6.1, 516 +7.1 (A3 after G sharp 3 again), 526 +7.9.
  - Holes: 512 (v112, -42.7 against -40.9 / -40.6 around it) and 524 (v112, -47.5 against -42.2 / -39.6). Both are slur starts after a tie, played as a "Sus MAX" re-attack (keyswitch at 523.5) whose attack does not reach its body inside 0.5 s.
- Violin I solo bars 349-356 (qn 1044-1068, "dolce, solo"): range 13.9 dB, std 3.9. Steps: 1046 +7.1, 1053 -8.3 (C sharp 6 after the held A6), 1064 -7.0.
- Oboe 1's middle part 185-196: 555 +12.2 dB over the entry, which is partly finding 1.
- Clarinet 1 bars 153-168: std 2.6, one step of 6.9 dB at 464 (unchanged).
- Violins I trio ff (bars 209-224) is even: std 2.1, no step over 6 dB.

**What is wrong.** The phrase's printed hairpins move CC11 by 5-15 units, but the notes jump by more than that, and always at the same places: the half-step joins (the HS legato transition sample is hot) and the cold re-attacks. A cellist or a solo violinist does not leap 8 dB onto an A3 that the score marks inside one slur at mp. Of everything in the movement, this is the clearest "machine" in the slow music (inferred). It is the "string legato swell" the c20 / c21 actors left open after their envelope- and attack-based tries failed.

**Fix** (instrument side, allowed by Dan's rule; range-test on qn 500-552 and 1040-1068, one start, control from the same start):
- (a) A CC11 counter-shape on the hot joins, the way finale technique 121 handled the basses' re-bow blooms: -8 units from the transition's note-on, held to 0.35 s, back by 0.8 s. Apply it at celli 506, 516, 526 and solo 1046, as a `CC11_SHAPE_AT` / LEVEL_SHAPES-in-CC11 table row per onset. It is CC11, not vol_db, so the hall tail is not cut.
- (b) Celli 512 and 524: play the note after the tie on the KS Master's "Leg BC MAX" row (bow-change legato), so the new bow sounds as a transition and not a cold attack. If that row is not loaded, use "Sus MAX" with `REATTACK_LEAD_AT` 0.085 s and velocity 80 (the c19 Violins I 597 recipe).
- Target: celli note-body std 2.0 or less and no step over +4 dB that is not printed; solo std under 3.0.

### 3. Theme A's quiet first statement sits on a pizzicato bass 7.4 dB louder than the celli on the same notes; the quiet passages carry 5.5 dB more low bass than the reference (measured; balance by role rows, slow)

**Where.** Bars 13-30 (qn 36-90), Violins I's p leggiero theme over celli and basses pizz., both printed p. Also the Meno mosso's pizz. bass (bars 341-357).

**Evidence.**
- At the 17 onsets where both play (an octave apart, E2 / E1 at velocity 53), the basses' first 0.2 s is a median 7.4 dB over the celli's: basses -44.9, celli -52.4, Violins I -41.6 dB.
- In the ritmo di tre battute (89-100) and the reprise (253-268) the same pair reads -1.8 and +0.5 dB. So theme A alone is off.
- Theme A's master has a 20-150 Hz share of -6.8 dB, and the basses' stem makes up all but 0.8 dB of it. The quietest quarter of the mp3 has a 20-150 Hz share of -8.4 dB, against -13.9 in the Dvořák's quietest quarter. The low bass is one more layer the ear has to listen past to reach the theme's 1-5 kHz, and at a moderate AirPods volume that makes the quiet passages sound woollier and softer than their LUFS (inferred).
- The cause is in `build/roles.json`: celli [36, 84, -2]; the basses have no row.

**Fix** (`build/roles.json`, slow section rows only): celli [36, 84, -2] -> [36, 84, 0], and add Double basses [36, 90, -3]. Target: basses minus celli -1..+2 dB on the shared onsets, the master's 20-150 Hz share in bars 13-28 near -10 dB, Violins I's theme 1-2 dB clearer in its 1-5 kHz band (inner23.py), and no change to theme A's mp3 loudness beyond -0.5 LU. Then check the basses' pizz. in bars 341-357 (the master's low band there is all basses, -0.3 dB) and apply the same -2..-3 dB row if they read more than 2 dB over the harp's left hand.

### 4. The Allegro's timpani play felt sticks where the score prints hard sticks: the motive x and the ritmo di tre battute strokes are woolly (measured spectrum; benefit inferred; MANUAL-GAPS #6, pending since c03)

**Where.** Every stroke and roll in bars 1-340. The model the score names is Beethoven 9/ii, where the ritmo di tre battute is carried by hard-stick timpani. The exposed strokes are bars 3-12 (motive x, p), 91 and 94 (qn 270-272, 279-281, printed f), 97-100, and the tutti rolls.

**Evidence.**
- First 80 ms of each stroke on the Timpani stem:
  - the f strokes at 270-281: spectral centroid 214-303 Hz, share above 1 kHz -13.0 to -24.9 dB;
  - the p strokes of bars 9-12: centroid 104-225 Hz, above 1 kHz -23.6 to -33.9 dB.
- In bars 89-100 the timpani make up all but 1.2 dB of the master's 20-150 Hz energy. So the strokes take a large share of the loudness without the stick's attack that a listener needs to count the three-bar groups (inferred).
- `Timpani Hrd KS.oib` has the same rows and keys (24-28) as the Flt patch (MANUAL-GAPS #6, read in c03).

**Fix** (as MANUAL-GAPS #6):
- Put the Timpani track on `Drums/Timpani/Timpani Hrd KS.oib` and add its row names to `KS_ALIASES` (or make the row names follow the patch stem).
- Keep one instance for now, which costs no memory and accepts hard sticks in the six soft coda strokes. A second instance on Flt for bars 341-376 can come later.
- Dump the Hrd layer and right-hand tables before reusing `TIMP_CC1_MAP` and `TIMP_ROLL_TRIM_DB`, and refit the roll levels on the first render. Dan's roll rule (BRIEF 5) applies.
- Target: the f strokes' share above 1 kHz over the first 80 ms 5 dB or more higher than now, the rolls no louder than c23 on the stem, and the 20 dB fall after the summit unchanged.

### 5. Bar 58 changes by ±2.9 dB from render to render on unchanged data: the fugato's round robins are not reset (measured)

**Where.** Bar 58 (qn 171-174), the fugato's first bars. c22 read +2.9 dB over c21 there, and c23 reads -2.9 dB under c22, with the same parts data (c23 CHANGES: "celli round robins on unchanged data").

**What is wrong.** Manual p.144: without a reset, Opus picks up the round-robin cycle wherever it stopped, so the take order depends on what played before. A 3 dB swing in a fugato entry means each render balances the fugato differently. It also means every critic's per-bar comparison in that passage measures noise.

**Fix** (`build/score_config.py` `RR_RESET_AT`, CC16 as extended in c12):
- add a reset on the celli (and on every string track that plays in bars 57-60) on the last rest before qn 168;
- check the other bars where c21 / c22 / c23 differ on unchanged data (`cycles/c23/records/bars_c23_vs_c22.txt`) and give each such passage a reset on its own rest.
- Target: bar 58 within ±0.5 dB between two renders of the same data.

### 6. The dynamic arc is at its floor: no more lift from the delivery; give the trio climax back what the stacked ride rows took (measured / inferred)

**Where.** The delivery's `RIDE_TRIMS` and the whole-movement arc.

**Evidence.**
- LRA is 10.5, exactly the spec's minimum (c18 12.0).
- The summit's lead over the first tutti is down from +2.3 to +1.7 LU.
- The trio's ff A6 (bars 218-219) is 2.2 dB lower than c18 and now -11.1 against the tutti's -9.6.
- Two ride rows overlap on the climax: [625-671] -2.0 and [645-659] -1.5, so -3.5 dB at the A6. On top of them sits the Flute 1 [648, 660, -4] role row, which since c23 already keeps the flute from covering Violins I (+0.8..+1.4 dB).

**Fix.**
- (a) Do not raise the quiet passages any further through the delivery. Each LU of lift there costs LRA, which would fail spec item 6. The extra presence Dan asks for should come from findings 1-3, which act inside the mix.
- (b) Delete the [645, 647, -1.5, 656, -1.5, 659] ride row. Its job (the flute over Violins I at the A6) is now done by the role row.
- Run `tools/deliver_master.py` on the c23 master before and after (b). Targets: bars 218-219 lead 214-217 by 4.5 LU or more, LRA 10.5 or more, summit lead over every rival 0.5 LU or more, bar 218 still under the summit by 2 LU or more.

## Do not touch

- The -14 LUFS delivery chain with its loudness loop, peak compressor and the room-noise bed. The bed fills only the end of the G.P. and the tail, and the hall readings are unchanged.
- The woodwind summit rows from 996 with celli and Horn 1 at 1004.75: they give the 1.9 LU step into bar 336.
- The coda stretto rows (bars 326-328).
- The hall (RT60 1.38 s, G.P. drop 18.9 dB).
- The bar 23 state, and the bar 38 / 263 CC11 lifts.
- No release cap on the Violins I short rows.
- The Violins I trio ff tune (bars 209-224, note-body std 2.1): leave its rows and velocities alone when fixing finding 2.
