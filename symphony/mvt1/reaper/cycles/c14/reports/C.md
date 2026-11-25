# Cycle 14, critic C: dynamics over time (render c13)

Lens: the shape of hairpins and phrases, the loudness arc of the movement against the score (the bar 121-126 allargando, fff and sostenuto with the tam-tam, the fff at 160 after the cymbal roll, the recapitulation at 131, the ppp coda), the loudness range of the master and the delivered mp3 (BRIEF item 6), swells and loop pulsing on held notes (item 7), decays, and comparison with references.

## Method

I measured the stem-fixed c13 render (`cycles/c13/render/`, master = float stem sum) and `mvt1-mockup-c13.mp3` against `build/parts.json` (14:40, the stem-fixed state that matches the render). Score qn maps to file time through the parts.json tempo map.
- Loudness: ffmpeg ebur128 at 10 Hz. M is the 400 ms window shifted 0.2 s to centre it; S is the 3 s window shifted 1.5 s. Stem levels are plain stereo power in 10 ms frames.
- Simulations: piecewise dB shapes in qn applied to the c13 stems and summed (`simshape.py`), then the unchanged `tools/deliver_master.py` run on the sum. With no shapes this reproduces c13 exactly (LRA 14.2 LU, span 18.5 dB, limiter 2.3 dB, peak 1.600).
- Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c14-C/`:
  - from c10-C, pointed at c13: `bars.py`, `hp.py`, `hptrack.py`, `win.py`, `notes.py`, `loops.py`, `loops2.py`, `msweep.py`;
  - new: `mw.py` (master M and family power per window), `climax.py`, `quiet.py`, `swell.py` (unmarked swells and fades on held notes), `tail.py`, `dec.py` (decays), `band.py`/`band2.py` (band levels), `simshape.py` (now accepts `_all`), `simstem.py`, `ev.py`/`ev2.py`;
  - `A/acchf.py` is critic A's item 8 check, run on A's c13 feature files.

## State of the arc (measured)

- **Master:** -16.1 LUFS, LRA 21.8 LU (the Dvorak 9/i reference measures 21.8). Bar level against the bar's loudest printed dynamic has a correlation of 0.88 (c09: 0.84).
- **Delivered:** LRA 14.2 LU, p10-to-max span 18.5 dB, limiter 2.3 dB, -1.6 dBTP: all inside the brief's targets. LRA sits at the bottom of the 14-16 LU range, so nothing should compress the file further.
- **Climax order holds on S:** delivered S max is -10.15 at bar 160, -10.83 at bar 122 and -12.87 at bars 167-170. On M the margins are thin: bar 160 is only 0.28 dB over bar 122 and 1.24 dB over bar 170 (c10 target 1.5).
- **Bars 121-126:** the bar 121 crescendo arrives with a step of +3.8 dB on M at the fff and tam-tam (483 -10.6 -> 484 -6.8 dB). The sostenuto bar 123 holds within 1.2 dB of bar 122. The diminuendo over 124-125 reaches the p at 126: master per bar -7.4 / -8.6 / -16.1 / -24.1 / -29.3. Bar 124 drops faster because the trumpets and Horns 1-2 stop there, as printed.
- **Recapitulation:** bars 127-131 build -32.3 / -30.3 / -27.8 / -19.7 / -14.7 dB. The ff theme at 131-134 sits 1.5 dB under the exposition's on M max (-13.5 against -11.8..-12.0).
- **Decays:** after the bar 170 fermata chord the master falls 60 dB in about 2.2 s, which matches a concert-hall reverb time, and the hall tail is not cut off. The bar 33 cutoff falls 14 dB in 0.5 s, then the bassoon solo takes over. The tam-tam is damped as printed at 504.2.
- **Item 7 on the master (measured):** sliding 10 s windows, autocorrelation at 3.85-4.05 s (`msweep.py`). The Lento, bars 122-126, the coda and the final chord all stay under 0.35. The windows flagged in the Allegro sit on 2-bar rhythmic patterns (8 qn = 3.8 s at q=126).
- **Item 7 on the stems** (every same-pitch run of 6 s or more): the string re-bows and the timpani re-strikes stay at or under 0.35. Flags above 0.35 are:
  - repeated-attack patterns, not loops: Tuba and Contrabassoon whole notes at 664, the celli quarters at 504;
  - stems masked 12-20 dB under the master: Bassoon 2 at 476, Bass clarinet at 464/492, Horn 4 at 289;
  - Cor anglais at 27, centroid 0.38, 9-11 dB under the master. I leave all of these.
- **Item 8** (A's `acchf.py` on c13): brass accents have a median 2-5 kHz front-minus-body of -8.2 dB, maximum +3.8 (Trumpet 1, 676). The outliers are wind and string accents at qn 536 (Violas +15.2, Bassoon 1 +9.7, celli +5.2). These are accents whose body decays at the start of the bar 135 crescendo, which is critic A's lens.

## 1. Bar 51, second theme: the dolce horn and celli phrase jumps 7 dB on one quarter note and becomes as loud as the f climax of the section (measured, simulated)

**Where:** qn 203 (bar 51 beat 4): Horn 1 dolce with the Violoncellos in unison, a 2-beat `<` from 201 that arrives on 203, then `>` over bar 52.

**Evidence: master M per half beat.**

| qn | 201.5 | 202.0 | 202.5 | 203.0 | 203.5 | 204.0 | 204.5 |
|---|---|---|---|---|---|---|---|
| dB | -30.5 | -29.7 | -26.5 | -23.3 | -24.0 | -27.1 | -30.2 |

- From 202-202.75 to 203-203.75 the master steps +7.1 dB. Horn 1 steps +7.6 dB (-36.5 -> -28.9) and the celli +4.7 dB.
- **Delivered M max per bar:** bars 47-50 are -22.1 / -23.1 / -22.4 / -24.5 and bar 51 is -18.0. Bar 51 is the loudest moment of the whole second theme (bars 47-68): it matches the printed f crest of bar 61 (-18.1) and comes within 1.6 dB of the f closing at bar 69 (-16.4).
- **The recapitulation is correct:** at 601-603 the arrival is +1.7 dB, and bar 151 measures -23.4.
- **Horn 1 notes:**
  - 201 (C5) has a body of -36.1. The 203 note (B-flat4, v124, CC11 70, CC1 64) has a body of -28.7, 7.4 dB over every other note of the phrase (-34.2..-41).
  - Its volume envelope steps from -1.2 to +5.5 dB at 202.92, the same +5.5 as the recapitulation's 603. The 203 pitch plays about 5 dB hotter on the CC1 layers at that envelope (603, a D4, measures -34.1).
  - The celli carry the c10 C #3a hold `[(201.0, 0.0), (202.95, 3.0), (204.2, 3.0), (204.7, 0.0)]` (score_config.py line 390). That puts +3 dB on their 203 note, and they step +4.7 dB there.
- **Real orchestra (inferred):** a p dolce phrase crests 2-3 dB on a small hairpin; it does not reach the section's f.

**Fix** (`build/score_config.py`, `LEVEL_SHAPES`):
- Horn 1 `[(202.8, 0.0), (203.0, -5.0), (204.0, -5.0), (204.2, 0.0)]`.
- Violoncellos `[(202.8, 0.0), (203.0, -3.0), (204.0, -3.0), (204.2, 0.0)]`. This cancels the hold over the arrival note. Equivalently, end the line-390 hold as `[(201.0, 0.0), (202.95, 3.0), (203.05, 0.0)]`; the recapitulation's 601 has no such hold and arrives at +1.7 dB.
- The note is a legato target; the cut starts at its moved onset, 202.886. If the join sags, start the Horn 1 shape at 202.95 instead.

**Simulated:**
- Master M 202.0-205.5: -29.7 -29.1 -27.3 -27.0 -28.0 -30.2 -32.0. The arrival is now +2.4..+2.7 dB, about the same as the recapitulation.
- Delivered bar 51 M max -18.0 -> -21.5, in line with the phrase crests of bars 47/49 (-22.0/-22.2).
- LRA 14.2, limiter 2.4 dB.

**Criterion:**
- Master arrival at 203 within +1.5..+3.5 dB of 202-202.75.
- Delivered bar 51 M max under bar 61's.

## 2. Bar 159-160: the fff largamente arrives no louder than the top of the crescendo, because the violins' E6 fill also lifts their crescendo notes (measured, simulated)

**Where:** qn 632-640. The bar 159 `ff <` leads to a breath, then the fff largamente on Violins I/II (C6 down-bow at 636, then the A-flat6 climax note at 637-639).

**Evidence (master M per half beat):**

| qn | 633 | 634 | 634.5 | 635 | 635.5 (breath) | 636 | 636.5 | 637 | 637.5 |
|---|---|---|---|---|---|---|---|---|---|
| dB | -9.6 | -7.7 | -6.4 | -6.2 | -7.8 | -6.3 | -6.0 | -6.0 | -5.8 |

- The crescendo grows +4.1 dB, but the fff arrival is 0.0..+0.4 dB over the crescendo's last beat. `hp.py`: 632-636, 30 tracks, arrival minus start +3.4 = end minus start +3.4.
- **Delivered:** bar 159 M max -9.82 against bar 160 -9.47 (0.35 dB).
- **Compare bar 122:** the bar 121 crescendo is followed by a +3.8 dB step at the fff.
- **Violins I by quarter:** the G6 at 634.75-635.25 measures -18.9 / -15.4 / -15.5. The fff C6 stroke and A-flat6 at 636-639 measure -22.5 / -19.6 / -17.9 / -21.3 / -24.8 / -23.8 / -21.5 / -21.7. The tune's climax note sits 4-6 dB under the note that leads to it. Violins II do the same. Strings as a family measure -12.7 dB at 635.0 and -14.7 / -13.1 / -15.5 at 636-637.5.
- **Cause:** the c08 `_e6fill` (score_config.py line 294), `[(629.5, 0), (631.5, 4), (633.0, 4), (635.4, 4), (635.9, 0)]` on both violin sections.
  - It was written for the held E6 of 629-633, which decayed 6-9 dB at flat CC11.
  - It also holds +4 dB over the F6 (633) and G6 (634-635.4), while CC11 rises 117 -> 123.
  - Violins I's envelope reads +8.75..+9.05 dB at 635.0-635.4 against +1.8..+4.8 dB on the fff notes (after the c06 stroke shapes and the arrival weight).

**Fix** (`build/score_config.py`):
- (a) Keep the fill over the E6 and let it go across the crescendo: `_e6fill = [(629.5, 0.0), (631.5, 4.0), (633.9, 4.0), (634.6, 2.0), (635.0, 0.0), (635.9, 0.0)]`.
- (b) Lift the climax note on both violin sections: `[(636.6, 0.0), (636.9, 2.0), (639.2, 2.0), (639.6, 0.0)]`.
- The arrival weight, the 0.5 qn hold-back and the c06 stroke shapes stay as they are. This changes the E6 fill that HISTORY lists as do-not-touch, but only from 633.9 on, after the E6 has ended.

**Simulated (a)+(b):**
- Master M 633-638.5: -9.6 -9.0 -8.2 -7.5 -7.3 -8.0 -6.2 -5.8 -5.7 -5.2 -6.1 -6.1. The crescendo still grows +2.3 dB. The fff stands +1.5 dB over the crescendo's top at the downbeat and +2.1 dB on the A-flat6.
- Delivered bar 160 M max -9.47 -> -8.91: 2.06 dB over bar 159, 0.92 over bar 122 (was 0.28) and 1.80 over bar 170 (was 1.24). S max margin over bar 122 0.68 -> 0.92 dB.
- Limiter 2.3 dB unchanged, master peak 1.600 -> 1.609.
- If (b) is not wanted, (a) alone gives the same crescendo top and bar 160 -9.33 (0.34 dB over bar 122 on M).

**Criterion:**
- Master M at 636.5-638 at least 1.5 dB over 634.5-635.5.
- Delivered bar 160 M max at least 0.8 dB over bar 122 and 1.5 dB over bar 170.
- Limiter at or under 2.5 dB.

## 3. The ppp morendo final chord swells inside its fermata and then stops in 1 s, instead of dying away (measured, simulated)

**Where:** bar 182, qn 724-728 (q=30, 8 s): ppp, `morendo` on the violas and `>` in bar 181 on every string part; Horns 3-4 ppp, timpani roll ppp, harp ppp étouffez.

**Evidence: master M per half qn.**

| qn | 724.0 | 724.5 | 725.0 | 725.5 | 726.0 | 726.5 | 727.0 | 727.5 | 728.0 |
|---|---|---|---|---|---|---|---|---|---|
| dB | -40.3 | -40.1 | -39.9 | -38.9 | -39.1 | -39.2 | -39.3 | -45.5 | -60.3 |

- The bar 181 diminuendo reaches the ppp at 724, then the chord rises 1.4 dB and holds for 6 s. Only the last 0.5 qn (1 s) fades, through the generic end fade (score_to_parts.py line 2780: 0 at SE - 1, -2 at SE - 0.5, -10 at SE).
- **The rise is in the strings** (plain power, 724.5-725 against 726.5-727): Violins I -49.1 -> -46.6, violas -50.7 -> -47.0, celli -53.2 -> -50.7, basses -56.5 -> -52.2.
  - This is where the bar 182 re-bows and their fitted re-bow shapes sit, for example the violas +9.8 dB at 725.6 and +12.0 at 726.94.
  - CC11 is flat at 22 from 723.875 to 727.625.
- **Delivered:** -32.5 -> -31.1..-31.5 -> -37.6 -> -52.3.
- **Real orchestra (inferred):** a morendo fermata keeps getting quieter until the release. Here the listener hears the last chord grow slightly and then switch off.

**Fix** (`build/score_config.py`): `LEVEL_SHAPES["_all"] = LEVEL_SHAPES["_all"] + [[(724.25, 0.0), (726.0, -3.0), (727.5, -7.0), (729.0, -7.0)]]`.
- The last point must lie past SE, because a shape returns to 0 after its last point.
- The generic end fade stays on top, so the total is -9 dB at 727.5 and -17 dB at 728.
- The c13 re-bow shapes and roles are unchanged, so the re-bow balance between sections stays the same.

**Simulated:**
- Master M 724-728: -40.5 -41.0 -41.7 -41.6 -42.9 -44.4 -45.7 -52.5 -67.3.
- Delivered: -32.5 -33.0 -33.8 -33.7 -34.9 -36.4 -37.8 -44.5 -59.2. The ride's +7.8 dB stays constant over these seconds, so the fade arrives intact.
- LRA 14.2, span 18.5, limiter 2.4 dB.

**Criterion:** no 1 s window of 724-728 louder than the one before it; master 727.0 at least 4 dB under 724.0.

## 4. Bars 117-120 (letter G): the ff after the six-bar crescendo sags 2.5 dB, and the basses lose 8-10 dB in bar 118 (measured, simulated)

**Where:** qn 464-480.
- `mp cresc.` from bar 111 to ff at 117 on every part, ff held until the bar 121 allargando crescendo.
- Brass and low winds hold ff whole notes and ties; the basses hold a tied G1 ("change bow at will"), re-bowed at 470.813 and 477.615.

**Evidence.**
- **Master M per bar:**

  | bar | 116 | 117 | 118 | 119 | 120 | 121 |
  |---|---|---|---|---|---|---|
  | master | -13.0 | -12.7 | -14.1 | -15.2 | -14.7 | -12.1 |
  | delivered | -15.3 | -15.2 | -16.7 | -18.0 | -17.8 | -15.4 |

  Plain power: bar 117 -15.6, bars 118-120 -18.0 dB.
- **It is the held ff notes that fall** (117 -> 118-120): Horn 4 -2.7, Horn 3 -2.9, Violins II -2.7, Bass trombone -2.8, Tuba -2.7, Contrabassoon -4.1, Bass clarinet -5.3 dB.
- **The basses:**
  - The 464 piece blooms to -22.3 dB at 465-466, then falls to -33.5 by 469 inside the note.
  - The re-bow pieces sit at -34.0 / -30.8.
  - Their 30-120 Hz band falls from +6..+12 dB (464-467) to -2..-7 dB (469-480).
  - The master's 30-120 Hz band falls from +7.7..+13.6 to -4.5..+8.5 dB.
- **Comparison:** the other ff plateaus hold. Bars 27-32 vary within 1.6 dB, bars 131-134 within 0.9 dB, and bars 167-168 hold and then rise into 169.
- **Real orchestra (inferred):** a brass chorale and a bass pedal marked ff do not fade 3 dB in the bars before an allargando; here the floor drops out under the violin tune one bar after the arrival at G.

**Fix** (`build/score_config.py`, `LEVEL_SHAPES`):
- On the held parts (Horn 3, Horn 4, Horns a2, Bass trombone, Tuba, Contrabassoon, Violins II, Bassoon 1, Bassoon 2, Bass clarinet): `[(467.6, 0.0), (468.6, 2.5), (479.6, 2.5), (480.4, 0.0)]`.
- On the Double basses, take back the bloom and fill the tail and the re-bow pieces: `[(464.2, 0.0), (464.8, -4.0), (467.4, -4.0), (468.4, 2.0), (469.0, 5.0), (470.7, 5.0), (470.95, 3.0), (483.6, 3.0), (484.0, 0.0)]`.
- Both are level-only, so a stem fix can apply them. The re-bow rows stay frozen.

**Simulated:**
- Master M per bar 116-121: -13.0 -12.9 -12.7 -13.9 -13.3 -12.0. Delivered: -15.4 -15.6 -15.6 -17.0 -16.6 -15.5.
- The largest sag after G goes from 2.8 to 1.4 dB. The bar 121 crescendo still rises 4.7 dB into 122.
- Basses per qn after 469: -28.5..-31.5 instead of -32.2..-34.5.
- Bar 122 margins unchanged; LRA 14.2, limiter 2.3 dB.

**Criterion:**
- Master bars 118-120 within 1.5 dB of bar 117.
- Basses within 3 dB of their 467 level from 469 to 484.
- Bar 122 still at least 4 dB over bar 120 on M.

## 5. Bar 43: the pp Violins II chord note blooms 10-13 dB unmarked and makes the master swell inside the pp (measured, simulated)

**Where:** Violins II, D-flat4 at qn 167.75-172 (bar 43, pp after the bar 41-42 diminuendo, no hairpin). It is the loudest stem in the bar.

**Evidence:**
- **Violins II per half qn, 168-172.5:** -46.4 -42.3 -42.0 -39.7 -40.1 -39.1 -37.2 -33.6 -36.2 -41.6. That is +12.8 dB at flat CC11 (32-34) and a flat envelope (0.0..+0.1 dB). It is the sample's own bloom after the 16-semitone drop from F5.
- **Master (plain power):** -34.5 at 169 rises to -32.3 at 171.5, so the bar swells about 2.5 dB in the middle of the printed pp, with the horns p.
- `swell.py`: of 458 held notes of 2 s or more without a hairpin, this is the largest unmarked swell on a stem within 10 dB of the master (harp arpeggios aside). The next is Violins I 576 at +4.1.

**Fix** (`build/score_config.py`): `LEVEL_SHAPES["Violins II"] += [[(168.4, 0.0), (169.5, -3.0), (171.0, -6.0), (171.9, -7.5), (172.25, -5.0), (172.6, 0.0)]]`. It ends inside the next note's first quarter, which also starts hot at -36.2. This is level-only.

**Simulated:**
- Violins II per half qn: -46.4 -43.2 -44.2 -43.1 -44.6 -44.6 -43.6 -40.8 -41.6 -41.9.
- Master (plain power) 169-172: -34.8 -35.0 -37.1 -37.5 -37.0 -36.2 -34.6. The diminuendo now continues into the pp.

**Criterion:** Violins II within 4 dB from 168.5 to 172.5; master 170-172 no higher than 169.

## 6. Recapitulation bar 148: the `<` of 589-591 still arrives under its start, because the celli sag 4-5 dB on the arrival note's legato join (measured, simulated)

**Where:** qn 589-592, Horn 1 dolce with the Violoncellos.

**Evidence.**
- **Master M per half qn, 589-592:** -26.7 -26.0 -25.6 -26.9 -27.9 -27.1. The arrival (591) is 1.2 dB under the crescendo's crest (`hp.py`: 589-591 arrival minus start -0.6 dB). The exposition's 189-191 arrives +1.2 dB.
- **What is already there:** the c10 hold `[(589.0, 0.0), (590.95, 2.5), (591.9, 2.5), (592.2, 0.0)]` (score_config.py line 389) and Horn 1's 591 trim of +3 dB with a 0.25 s ramp (envelope +5.5 -> +10.0 dB).
- **The sag:** the celli per eighth of a qn measure -31.1 at 590.75, then -35.1 / -35.5 / -35.4 / -36.9 / -35.2 over 591.0-591.5, then -32.1..-30.3 from 591.6. That is a legato-transition sag 4-5 dB deep that the hold does not fill. Horn 1 stays at -33.8..-35.6 through 591, under its own 589.25 crest of -31.5.

**Fix** (`build/score_config.py`; or add an entry in `build/early_fills.json` if the actor prefers the fill table):
- Violoncellos sag fill `[(590.95, 0.0), (591.05, 4.0), (591.5, 4.0), (591.75, 0.0)]`.
- Horn 1 `[(590.9, 0.0), (591.05, 2.5), (591.9, 2.5), (592.1, 0.0)]`.

**Simulated:**
- Celli 591.0-591.5: -31.9 / -31.5 / -31.4 / -32.9 / -32.0, no step against 590.75.
- Master M 588-593.5: -27.6 -27.0 -26.7 -26.0 -25.6 -25.9 -25.8 -26.2 -26.2 -26.6 -28.2 -28.1. The arrival is now level with the crest.

**Criterion:** 591-592 within 0.5 dB of 590-590.5 on the master.

## All six together (simulated on the c13 stems)

The combined run used an earlier finding 6 variant: +2.5 dB on both the celli and Horn 1 over 591.05-591.9. Its master result at 591 is within 0.3 dB of the fix above.

- Delivered: LRA 14.2 LU, span 18.8 dB, limiter 2.3 dB, -19.8 LUFS, motion 8.75 / 4.53 (c13: 8.74 / 4.53).
- Climax on M max: bar 160 -8.91 > bar 122 -9.83 > bar 170 -10.71. On S max: -9.91 > -10.91 > -12.87.

## Do not touch

- The bar 121 approach and the +3.8 dB fff arrival at 484 with the tam-tam, its damp at 504.2, and the bar 124-126 diminuendo to p.
- ARRIVAL_WEIGHT_AT with its 0.5 qn hold-backs and the c06 stroke shapes at 636. Finding 2 changes only the E6 fill after 633.9.
- The climax order (160 > 122 > 169) and the delivery settings: ride ratio 2.5, cap 10, 3 s smoothing, top ride 1.6, FAST_CAP_ABOVE 4. LRA is at 14.2 and should not drop.
- The AUTO_REBOW rows and frozen re-bow times, the re-bow shapes, and the timpani re-strike plans: item 7 passes on the master everywhere music is held.
- The bar 170 and bar 33 decays, and the 1.0 s mp3 tail.
- The second-theme exposition shapes at 184-191 and the c12 HP_TARGET_AT set. Findings 1 and 6 only add to them.
