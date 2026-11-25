# Cycle 20, critic B (balance and levels), on the c19 render

Everything here is measured on `cycles/c19/render` (stems and master) and the delivered `scherzo-mockup-c19.mp3`, against `cycles/c18/render` and `cycles/c17/render`, with the data in `cycles/c19/build_render/`. Positions are score quarter notes (qn); bar b starts at qn 3(b-1).

Terms:
- "Level" is the mean power of a stem (mean of the two channels' powers), per bar, per beat, or over the first 0.15-0.3 s of a note.
- "Best band" is the highest ratio, over 1/6-octave bands from 40 Hz to 16 kHz, of a line's power to the power of every other stem plus the four returns. It is averaged over the 21 ms frames in which the line's notes sound. Only bands within 10 dB of the line's own strongest band count. Windows are 2 bars. A line under 0 dB is covered in every band where it has energy.
- "M" and "S" are ffmpeg ebur128 momentary (400 ms) and short-term (3 s) loudness.

Each judgement is marked (m) measured or (i) inferred.

## Manual notes (slot B2: May 2021 HO manual PDF p.194-200; MANUAL-GAPS.md)

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| The Mix page has a strip per instrument, with sub-mixer channels for the mic positions; each mic can be loaded or unloaded and has its own volume and pan (p.194, 196) | `mix.json` `mic_db` per group and track. For example: Flute 1 Close 0 / Main -4.7; Oboe 1 and 2 Close 0 / Main -20.6; horns Close -6.3 / Main 0 | Yes. Levels are set per mic in the state. Only the oboes are nearly Close-only. That changes colour and depth, not level, so it is not the cause of finding 4 (i). |
| Store / Restore Mix and FX Chain presets (p.195-196) | The states are written by `build_reaper.py` from `mix.json` | Not needed. Writing states from a script is the reproducible form of the same thing. |
| FX bus channels with a reverb, fed by Effects Send inserts on the sub-mixer channels (p.196, 198) | `opus_reverb_off` true. The halls are REAPER returns (EW Spaces II, from the template's chunks), and every track sends to them (`send_profiles` "ew") | Yes, done in REAPER rather than inside Opus. The legacy `reverb.send_pre_fader` true is inert while the Opus reverb is off. |
| Effects Send POST switch. For reverb, post-fader is typical, so the main mix and the send carry the same level (p.198) | The template sends are post-fader (`_c50` doc). Role rows, hairpin ramps and fades act after the hall in the track envelope. | Yes (m on the data). Consequence: every role row in this report also moves that track's hall. That is right for balance rows, and is why sudden drops stay in CC11 (S3). |
| EQ inserts: Bass Comp, Channel Equalizer, 6-band Equalizer (p.199-200) | ReaEQ per family (`family_eqs`), per track, and on the master (`master_eq`) | Equivalent. No Opus EQ inserts are needed. No finding below needs an EQ change. |
| MANUAL-GAPS #9: half-section patches for Violins II "la metà" | Bars 349-356: Violins II 8.4 dB under the solo, Flute 1 8.2 under, Violas div 14.3 under (c18: 8.5 / 7.7 / 14.3) | Unchanged and acceptable. Not needed for any finding. |

## Answers to the cycle 20 questions (m unless marked)

- **Hidden inner lines through the whole movement.** I scanned every track in every 2-bar window, flagging lines with 3 or more pitches in passages where the master is under -28 dB.
  - Most low windows are lines doubled at the same onset and pitch class, which are carried by their partner. Examples: Flute 1 / Oboe 1 / Horn 3 in the trio; bassoons and clarinets under the sub. p's.
  - Four places hide a part that the print gives its own role:
    - Violins II's con sord. arpeggios in bars 175-184 (finding 1);
    - the violas' div. thirds in bars 209-224 (finding 2);
    - Oboe 1 in the counterstatement's unison calls, bars 29-40 (finding 4);
    - Clarinet 1's tune crest at bar 214, which covers the violins (finding 3; the reverse case).
  - The rest are printed-softer inner voices inside f-ff tuttis. Examples: Horn 2's held tones at bar 211, best band -16.9; Bassoon 2 in 213-217, -13 to -15. These are covered as a real orchestra would cover them.
- **Theme A** keeps a best band of +10 to +16 dB over the pizzicato bass and timpani in 13-28 and 253-268 (+2.3 in the 263-264 window, where the celli's espress. tune joins).
- **Clarinet 1 and the unrendered ff trim.** The trim is right for bars 72, 300 and 334, but it does not reach bar 214 (finding 3).
- **Violins II over the violas in the fugato.** Close this item. On whole bars the three subject entries now sit within 1 dB of each other:
  - celli bars 58-60: -41.9 / -42.0 / -40.8;
  - violas 62-64: -40.3 / -40.9 / -41.3;
  - Violins II 66-68: -38.4 / -41.3 / -42.6.

  The 2 dB in bar 66 is a natural build as entries accumulate, at one printed p.
- **The summit on the mp3.** Leave it.
  - On S, the coda rises steadily on the mp3: bars 330 to 338 read -15.9, -13.8, -11.4, -10.1, -9.2, -8.3, -7.8, -7.6, -7.5. The summit leads the first tutti by 1.1 LU (-7.5 against -8.6) and bar 72 by 2.0.
  - On M, bars 334-339 sit within 0.4 LU of each other (-7.5 to -7.1), so the 336 downbeat has no step (master: +1.8).
  - The limiter's load at the summit does not come from the bass or the timpani. Over the 400 loudest master samples of bars 332-339, Violins I, violas and Violins II supply 0.22 / 0.15 / 0.14 of the peak amplitude. Timpani, tuba and basses supply 0.04 or less.
  - The summit's crest factor is 11.9-12.6 dB, the same as the tuttis' 11.1-14.8.
  - No per-family trim lowers the summit's peak-to-loudness ratio without lowering the strings' fff itself. With c19's failed ride test, that leaves the -14 LUFS limiter as the only cause. Keep the delivery chain.
- **Timpani in the coda.**
  - Bar 333's f strokes peak at -20.9 to -23.7 dBFS (first 150 ms). Bar 304's f strokes peak at -20.9 to -21.5. The summit strokes (337-339) peak at -18.9 to -21.5.
  - The timpani sit 14-17 dB under the master in rms, as they do in the 105 tutti. Their level is right.
  - The four strokes of bar 335 (qn 1002-1004, printed "<" into the 336 roll) are all velocity 104 and peak flat at -22.0 to -23.3 dB. The printed crescendo does not show on the stem.
  - Optional fix (instrument side): `VEL_SET` Timpani 1002 / 1003 / 1003.5 / 1004 = 100 / 106 / 110 / 114. Keep 114 as the ceiling: c15 found the higher layers harder.
- **Per-bar master against c18 and c17.**
  - Against c18, 15 bars differ by more than 1.5 dB, all from c19's intended changes:
    - 14 / 24 / 26 / 96 / 254 (-1.6 to -2.0): Violins I's Marc halves;
    - 18 / 258 (+4.0 / +2.5): the theme row;
    - 58: celli fugato;
    - 168-173: Violins II trio;
    - 328: the hold;
    - 290 and 365: round-robin and cancellation, unchanged data.
  - Against c17, 22 bars differ. The new ones are bars 18 / 258 at -2.9 / -2.4 (Violins I -3.2: the Marc-row cut) and the bar 72 / 300 woodwinds (+1.5 / +2.1, c18's accents).
  - The theme's best band in those bars stays +13.4 to +14.9, so the bar 18 / 258 drop is an accent-size matter for critic A, not a balance fault.

## Findings, ranked by what a listener would hear

### 1. Trio, bars 175-184 (qn 522-552): Violins II's con sord. arpeggios are still covered once Violins I join (m)

**Print.** Violins II, pp con sord. dolce, play quaver arpeggios under the celli's tune (mp espress.). From bar 177 (qn 528) Violins I double the tune an octave higher (p dolce espress.). The arpeggios are the moving inner line that Dan describes.

**Measured.** c19's +9 units fixed the first half and left the second:

| bars | Violins II best band, c18 | c19 |
|---|---|---|
| 169-174 | -9..-12 | -0.7..+0.3 |
| 175 | -9.0 | -5.4 |
| 179 | -9.3 | -6.7 |
| 181 | -12.6 | -9.3 |
| 183 | -10.4 | -7.4 |

- Frames over: 0.24-0.43.
- Violins II per bar: -41.1 to -41.7 in 170-173, falling to -45.1 / -44.7 / -46.1 / -44.8 / -46.5 in 179-183. Violins I read -37.2 to -40.6 there, celli -35.8 to -39.9.
- The data shows two causes:
  - Violins II's own CC11 drifts down from 54 (qn 519-525) to 50 (543-546) with no printed hairpin, while velocity (41) and the role (+4) stay flat;
  - Violins I's entry in the same register (pitches 63-71 against the arpeggios' 66-78) adds masking in the 500-640 Hz bands where Violins II have their best band.

**Fix** (instrument side, `build/score_config.py`, the c19 `CC11_ADD_SPANS` line for Violins II). Replace (501.3, 551.4, 9, 9) with:
- (501.3, 526.0, 9, 9);
- (526.0, 534.0, 9, 14);
- (534.0, 549.4, 14, 17);
- (549.4, 551.4, 17, 9), so the printed decrescendo of 549.5 stays.

**Expected.** At 0.48 dB per unit (c18 LEARNINGS, Violins II "Sus MAX" at p) that is +2.4 to +3.8 dB in 179-183 (i: the slope was measured senza sord.).
- Target: Violins II 3-4 dB under Violins I in 177-183 (now 2.5-7.9 under), best band -3 dB or better.
- Keep the celli's tune on top. Its best band is now +2.5 to +6.9 in 177-181, at 140-2280 Hz, away from Violins II's 500-640 Hz.
- Read the stem before keeping it. No fader row.

### 2. Trio return, bars 209-224 (qn 624-672): the violas' div. thirds are 7-14 dB under the violins because of two old negative role rows (m)

**Print.**
- Violins I and II: the tune, f espress., rising to ff at 218.
- Violas (two tracks: Violas, and Violas div on the DIV B half section): mf off-beat thirds, a quarter tied into a half on beats 2-3 of every bar. They rise to f with the violins at 217-219.

This is the texture the lens names ("over the violas' div. thirds").

**Measured.**
- The two viola tracks summed, per bar 209-224, against the two violin sections: -10.0, -9.0, -10.2, -11.7, -12.2, -8.5, -8.7, -13.0, -12.2, -7.1, -7.8, -8.5, -9.7, -11.6, -14.4, -12.3 dB. c17 and c18 read the same within 0.7 dB.
- Best band:
  - Violas: -5.1 / -12.8 / -5.7 / -11.6 / -8.7 in bars 211-221, except +2.2 in 217;
  - Violas div: -2.0 / -20.5 / -14.5 / -8.2 / -3.1 / -10.7;
  - frames over 0.02-0.46.
- In bars 213 and 215 the off-beat chords cannot be heard at all. One printed dynamic under the tune should leave them about 4-6 dB under, audible as the pulse of the accompaniment (i: the usual balance of an accompaniment one printed dynamic below the melody; not checked against a book this cycle).

**Cause** (m, `build/roles.json`):
- Violas [624, 672, -3.7] and Violas div [648, 672, -3] are early-cycle rows (c03-c05). They were set before the template mix, the half-section DIV B and the c15 per-note rule.
- No other row or CC11 lowers these notes. The violas' CC11 is 72-77 at the printed mf, and the role row is the only negative layer.
- This matches Movement I c61's finding (ONE_TIME_c20 item 4): inner parts buried by stale negative rows.

**Fix.** Delete both rows from `build/roles.json` (Violas [624, 672, -3.7], Violas div [648, 672, -3]).
- Expected: violas group 4-10 dB under the violins, best band +3 to +3.7 dB higher (i).
- The violins' tune keeps its best band (Violins I +1.7 to +6.3, at 2.3-4.6 kHz; the violas' best band is at 220-360 Hz).
- If bars 218-219 (violins ff) then bring the violas within 3 dB of the violins, replace the deleted rows with Violas [648, 657, -2] only, a phrase-length row over the ff climb. Do not add a per-note row.

### 3. Clarinet 1 against Violins I: the unrendered ff trim is right for bars 72 / 300 / 334, but bar 214 is a hairpin crest it does not reach, and bar 334 is also a weak Violins I half note (m)

**The step in build/** (`dyn_trim_db` ff +1.2 -> -1.0). It acts through the dynamic-curve table, between the f anchor (CC 88, -1.5) and the fff anchor (CC 124, -0.08). On Clarinet 1's `dyn_curve` it gives:

| bar | trim change | Clarinet 1 over Violins I (c19) | after |
|---|---|---|---|
| 72 | -1.1 dB | +1.5 | +0.4 |
| 300 | -2.2 | +1.1 | -1.1 |
| 302 | -0.7 | +3.1 | +2.5 |
| 334 | -2.2 | +3.0 | +0.8 |
| 105 / 305 (tuttis) | -2.2 | -4.3 / -4.2 | -6.5 / -6.4 |
| 336-338 | 0 | | |

- Bar 302 is the sfp crescendo. The tutti values are fine for a doubling clarinet.
- One clarinet against sixteen first violins at ff belongs under them. **Adopt the step.**

**Bar 214 (qn 639-642) is not touched.**
- Clarinet 1 is printed **mf espress.** at 624, where the violins are f. Its `dyn_curve` there is 72-86, under the f anchor.
- Per beat: beat 640 +6.3 over Violins I, beat 641 +4.0. Every other beat of 209-222 reads -0.9 to -10.1.
- Two things meet there:
  - Clarinet 1's notes C sharp 5 / F sharp 5 at 639 / 640 read +5.1 / +7.1 dB over their neighbours (-37.9 / -34.7 against -40 to -43). That is the crest of the printed one-beat hairpin 639-640: the envelope's mf hairpin gain of 2.0 dB (`HP_GAIN_MF_DB` wind) plus CC11 76 -> 80.
  - Violins I's "port." arrival at 640 (Leg Slur MAX at velocity 55, critic A's choice in c18) reads -39.0 against -35..-37 for its neighbours.
- **Fix** (Clarinet 1's side; the portamento is A's):
  - remove Clarinet 1's mf hairpin gains in the trio return, [632-633], [639-640], [644-645], [662-663] (2.0 dB each), with a per-track `HP_GAIN_MF_DB` 0 for Clarinet 1 over 624-672 or the equivalent drop-ends entry;
  - hold its CC11 at 76 through 639-641.
- Expected: about -3 dB at the crest (i), so Clarinet 1 sits about level with Violins I at beat 640 and 2-6 dB under elsewhere, as the print's mf against f asks. These are hairpin rows (slow class), not a note move.

**Bar 334 (qn 999-1002).**
- Violins I's accented half note G6 (pitch 91, "Sus MAX", velocity 96, CC11 113) reads 2.6 dB **under** its own staccatos around it (-32.7).
- The same theme half note in the tuttis reads +0.8 to +3.2 over its staccatos: G5 at 315 / 915, -29.2 / -29.4, the same velocity and CC11.
- So in the coda's octave-higher statement, the crescendo's accented note dips, and the violin stem's bar 334 (-31.8) sits 5 dB under bars 333 and 335.
- **Fix** (Violins I, one note, instrument side; range-test both, then keep the one that reaches +1 to +2 dB over the staccatos):
  - `VEL_SET` Violins I 999 = 112 (the summit's 1005 note at 112 reads +6.1);
  - or `ART_AT` 999 "Sus Marc LITE" with CC1 following CC11, the row whose f-ff accented halves at 302 / 910 read +4.0 / +1.5.

### 4. Counterstatement, bars 29-40 (qn 84-120): Oboe 1's staccatos are 8 dB under Flute 1 in their unison calls (m)

**Print.** Flute 1 and Oboe 1, both "1. leggiero p", play the theme head in unison: bars 29-30, 33-34 and 37-40. The strings answer. The oboe's colour is half of the call.

**Measured.**
- Over the 20 unison staccato notes at velocity under 75 (bars 29-40), Oboe 1 reads a median **8.2 dB** under Flute 1. For example:
  - qn 84: -53.1 against -39.8;
  - qn 96: -52.7 against -40.7;
  - qn 98: -52.8 against -42.7.
- The held and slurred notes of the same calls are within 1-2 dB (87: -47.5 against -45.8; 101.5: -44.9 against -44.8). So the staccato row alone is low.
- Best band: Oboe 1 -1.2 / -2.6 / -18.3 / -16.2 in the windows at bars 29 / 33 / 37 / 39.
- In the f-ff tuttis, Oboe 1's staccatos (velocity 75 or more) sit a median 5.3 dB under Flute 1. That is acceptable there.

**Cause** (m, `build/mix.json`): the two tracks' staccato rows are set in opposite directions.
- Flute 1's "Stac DblTng RRx9" has `row_db` +3, B4 +6, D5 +5, and velocity 75 or more +4. It plays at velocity 64.
- Oboe 1's has `row_dyn_db` velocity under 75 -3 and velocity 75 or more -3, and A5 -3. It plays at velocity 52.

**Fix** (`mix.json` Oboe 1 `region_gain_db`, the `row_dyn_db` entry): "Stac DblTng RRx9" vel<75 -3.0 -> +3.0. That is +6 dB on 25 notes: bars 29-40, and the pp head entries of bars 92-94, which sit alone over pizzicato pp with best band +8.3.
- Target: Oboe 1 about 2 dB under Flute 1 in the calls, as on their held notes.
- Leave the velocity 75 or more value alone.
- If the actor prefers velocity: Oboe 1 staccato velocity 52 -> 64 in 84-120 stays in the same layer and will not give 8 dB (i).

### 5. Role rows (153), sorted by cause (m)

| cause | rows | what to do |
|---|---|---|
| Summit / coda 984-1017 (every family) | 24 | Keep. They set the fff order measured above. Merge Violins I's four rows [987-995.5 +2], [1004.75-1008 +2.5], [1008-1014 +4.5], [1014-1017 +2.5] into phrase-length rows only if a later render shows a step inside a sounding chord at 1008 / 1014. Both are bar downbeats with new notes. |
| Tutti 312-360 / 912-960 | 23 | Keep. The countermelody (celli +4.5, Bassoon 1 +3, Horns 3-4 +2) and the doubling cuts set the tutti order. |
| Positive phrase rows (solo, inner lines, soft entries) | 37 | Keep. These are the lifts Dan asked for: Horn 1's call and last G sharp, the solo, the fugato entries, Violins II's trio +4, the celli's tune. |
| Negative rows inside f-ff passages | 39 | Mostly doubling winds under the strings, correct. Stale: **Violas [624, 672, -3.7] and Violas div [648, 672, -3]** (finding 2). Also look at Horn 1 [756, 864, -1.5] (36 bars) and [1020, 1068, -2.5] (16 bars): both long and quiet. Before deleting either, measure Horn 1's best band where it plays inside them. |
| Negative rows in soft passages | 30 | Mostly accompaniment under the sub. p's and the trio: harp, clarinets, celli bass, Double basses -1.8 / -1.9. The lines they cover are carried by doubling partners (best band of the group 0 dB or better). No change found necessary. Oboe 1 [828, 840, -1.5] and Flute 1 [828, 840, -3.5] sit on the reprise's melody (277-280: Flute 1 -42.4 dB, only 4-6 dB over the pp clarinets and violas). Leave them unless critic C hears the reprise's second idea as weak. |

- No row is shorter than 3 qn. No per-note rows are left.
- Two -0.5 cor anglais rows ([306, 312], [906, 912]) are the summed remainders of c19's merges, not stale rows.

## Do not touch

- The delivery chain:
  - -14 LUFS, loudness loop, 2:1 top ride, the trio ride row ramped over bar 209;
  - the coda still rises on S to the summit, which leads by 1.1 LU (first tutti) and 2.0 LU (bar 72).
- Theme A's margins (best band +10 to +16 over the pizzicato bass and timpani).
- The fugato entries (within 1 dB per bar).
- The solo's margins in 349-356: Flute 1 -8.2, Violins II -8.4, violas -9.0.
- Horn 1's motto (357-360, 8.1 dB over the next stem) and its last G sharp (3.9 over Violins I).
- The celli's +8 fugato lift.
- Violins II's trio +9 in 169-174 (extend it, finding 1).
- The tutti countermelody rows.
- The timpani's levels in the tuttis and the coda.
- The Clarinet 1 ff trim in build/.
