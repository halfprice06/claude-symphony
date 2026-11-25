# Critic B, cycle 3 (render c02): balance and levels

## Manual notes (May 2021 HO manual, PDF pages 116-117 and 121-126: crash cymbal pairs, bass drums, timpani)

Movement I has no percussion beyond the timpani on felt, so its reports do not cover the crash, the bass drum or the hard-stick patch. Each note is checked against the Finale's `build/score_config.py` (TRACKS, PERC_MAP, TIMP_*), `build/parts.json` and the c02 stems.

| Page | What the manual says | Where it applies in this mockup | Does the render follow it? |
|---|---|---|---|
| p.116-117 | Crash pairs: each has three lengths (long, short, even shorter) on white keys, each with 3 round robins. CC11 and velocity set loudness; velocity selects 7 dynamic layers. Sizes are described by tone (the 20in Zildjian has a soft attack, the 16/19in Sabians are harsh, the 17in Istanbul is "all-purpose"). The 22in K is listed only as part of the Combo (p.116). | Crash cymbals track: `22in Zildjian K Crash.oib`, key 60 (Long), velocity 124 at qn 888, 1048, 1108 (all fff), `min_s` 9 s (let ring). | Yes. The long length matches the printed let-ring whole notes, and velocity 124 is the top layer for fff. Measured: in the first second the crash is -9.2 to -11.1 dB K re master and carries the master's 5-12 kHz band (-0.5 to -1.0 dB re master). It ranks 10-12 of 29 stems by K-weighted level at 888 and 1108. It is heard but does not dominate. No change. |
| p.121-122 | Bass drums (32/36/40in): C1 felt short, D1 felt long, E1/F1 felt rolls, felt and hard-mallet recorded crescendos. CC11 and velocity set loudness; velocity selects up to 12 dynamic layers; 4 round robins. The 36in Ludwig has "a deep, rumbling quality with a strong woody hit on the attack". | Bass drum track: `36in Ludwig Bass Drum.oib`, key 38 (felt long), at qn 888 and 1108. The score prints **ff** for both strokes (the crash is fff). | Partly. The patch and length are right. The velocity is not: both strokes play at 124, the fff layer (finding 5). |
| p.123, p.125-126 | Timpani Long (C0): single strokes; two strokes within 65 ms trigger a damped double hit. Left hand on C1-A2, right hand on C3-A4. Velocity selects up to 16 layers; 2 round robins. | 160 strokes on "Timpani Hrd Lng". `TIMP_RH_ALT` sends 51 of them at pitch +24 (right hand). | Yes. The closest pair of strokes is 170 ms apart, so no stroke triggers the 65 ms double hit by accident. Strokes span 25 dB from pp to ff (first 150 ms: pp -50.2, mf -42.4, f -30.0, ff -25.1 dB), so the velocity layers keep the printed dynamics apart. |
| p.124, p.125-126 | Timpani Rolls (D#0): CC1 crossfades 8 dynamic layers, for crescendos and diminuendos. Hard-mallet rolls have "clear individual hits". | 19 roll notes (13 chains) on "Timpani Hrd Rls". CC1 comes from `TIMP_CC1_MAP`; level comes from CC7 (`roll_db` in `score_to_parts.py`) plus `TIMP_ROLL_TRIM_DB`. Both maps are Movement I's **felt-stick** fit, and the TRACKS comment says they still need a check on hard sticks. | Partly. CC1 does move the layers (measured on c02, hard sticks: CC1 56-63 at -39.2, 88-95 at -28.8, 120-127 at -22.6 dB, with CC7 and the envelope removed). But the felt trims cancel almost all of that difference, so a p roll plays nearly as loud as an f roll (finding 1). |
| p.124-125 | Short hits (C#0): quickly muted hits, for stops within a beat or two. Flams (D0): 2 layers. | Not used. The Finale's quarter strokes followed by rests (bars 265-272) let ring on Lng. | Not a balance question. Short hits belong to the articulation lens. |
| p.123, p.125 | Recorded crescendo rolls (E0, Hard Cresc): three chromatic ranges with crescendos of different lengths, 2 velocity layers. | Not used (MANUAL-GAPS #12). Candidates are the printed roll crescendos into an arrival: qn 1040-1048 (f to fff into the 263 crash, 2.7 s), 1096-1102 and 872-888 (p to fff, 6.6 s, probably longer than any recording). | Open gap. With finding 1's trims the CC1 rolls grow by about 22 dB through the 872-888 crescendo, so no balance finding needs the recorded rows this cycle. |

MANUAL-GAPS read. #10 (timpani hands) is done here as well (`TIMP_RH_ALT`). #12 is noted above. The other items are not balance items for these pages.

## Method

- Data: the c02 stems and master after the stem fix, with `build/parts.json` (c02 state) and its tempo map.
- Frames: a 4096-point STFT with a 25 ms hop and stereo power, K-weighted (BS.1770 curve applied as a power response), plus six unweighted bands (20-100, 100-300, 300-1k, 1-2k, 2-5k and 5-12k Hz). "re M" means a stem minus the master over the same span. A stem's rank counts all stems except crash and bass drum, unless stated otherwise.
- Hard-stick roll layer curve: for each 0.25 qn frame inside a roll, the timpani stem level minus vol_db minus 20 log10(CC7/127), grouped by CC1. Opus treats CC7 as linear amplitude (Movement I c13).
- Cross-family pairs: for each beat, take tracks from different families that both sound for at least 0.75 of the beat at the same printed dynamic, and record their level difference. Medians are taken over beats. The norms are Rimsky-Korsakov's resonance table as previous B reports used it: at piano all winds are equal and a violin section equals one wind; at forte a violin section equals two woodwinds (about +3 dB).
- Simulations scale the timpani frames by the planned envelope change (trim difference on the printed dynamic curve, held to the roll's end plus 0.5 qn, and the removed settle) and add the difference to the master. Other changes are level-only and are worked out by arithmetic.
- Score: `sections/arrival.ily` and `finale.ily` comments and notes for bars 219-234 and 271-279; `build/mockup-events.tsv` for every timpani and percussion mark.
- Dan's checks through this lens:
  - Item 5 (rolls): findings 1-2.
  - Item 7 (loop pulsing on long timpani rolls, 5-6.6 s at 584, 872, 920 and 1088): the 50-300 Hz level has an SD of 1.5-2.5 dB and the centroid an SD of 30-41 Hz, with autocorrelation at most 0.26 at lags of 0.4-5 s. No periodic pulsing (measured).
  - Item 4: none of the proposed changes touches an accent's front.
  - S3: every role proposed below starts and ends on a note onset of its own track. The timpani trims act at roll onsets and are held through each roll's ring, as now.
  - Peaks: the master's float-sum peak at 888 (1.655) is made mostly of Tuba (+0.42), Trombone 2 (+0.25) and the basses (+0.16). The bass drum contributes nothing at that sample. At 1108 (1.567) the peak is Violins II (+0.38) and Horn 1 (+0.33).

## 1. The hard-stick timpani rolls have almost no dynamic range: a p roll is the 5th-loudest stem, and an fff roll sits near the bottom (measured)

**Where.** Every roll on the Timpani track (13 chains). The clearest cases:
- the sub. p roll at bars 219-220 (qn 872-880);
- the p and mp roll ends at 156-159, 668-671 and 930-933;
- the fff rolls at 888, 1048 and 1108.

Tables: `build/score_config.py` `TIMP_ROLL_TRIM_DB` (and `TIMP_CC1_MAP`), with the `roll_db` CC7 table in `tools/score_to_parts.py`.

**Evidence.**
- Steady roll level (layer + trim + CC7, with no attack bump and no settle), from the measured hard-stick layer curve, `TIMP_ROLL_TRIM_DB` and `roll_db`/2:

  | dynamic | pp | p | mp | mf | f | ff | fff |
  |---|---|---|---|---|---|---|---|
  | level (dB) | -35.7 | -33.6 | -35.6 | -35.4 | -29.5 | -28.7 | -27.1 |

  - The span from p to fff is 6.6 dB, and pp through mf are flat.
  - Cause: the felt trims add +18.6 dB at p against +7.3 at f and 0 at fff. The hard layers differ by 16.6 dB (CC1 60 against 122), and the CC7 table cuts p only 8.6 dB under fff.
- The strokes on the same patch span 25 dB, and the p roll at 872-876 (-37.4 dB) is louder than the mf strokes' attacks (-42.4 dB, first 150 ms).
- Cross-family pairs at printed p (median over beats). Norm: about 0, and a soft roll should sit under the sustained instruments.

  | timpani minus | horns | low brass | low strings | violins | woodwinds | trumpets |
  |---|---|---|---|---|---|---|
  | dB | +3.8 | +4.0 | +2.0 | +3.0 | +5.6 | +6.2 |

  Every other pair of families at p falls within -4.6 to +5.2 dB.
- Bars 219-220, the sub. p after the trumpets' theme B: the roll is -11.2 / -12.3 re M and ranks 5th / 6th of 29. Only the cor anglais, Clarinet 2, Oboe 1, Clarinet 1 and the violins are louder.
- At fff the order reverses: the roll ranks 17th of 29 at 888 (-18.1 re M), 16th at 1048 (-16.2) and 23rd at 1108 (-20.2).
- Through the p-to-fff crescendo at 872-888 the roll grows only 12.2 dB while the master grows 16.4 dB, so the crescendo printed into the arrival fades relative to the orchestra. The score's own note (arrival.ily c146) wants the 223 roll to start fff and diminish so that the strings sound through. The start of that roll is the part that is missing.

**Fix (`build/score_config.py`, Finale value, hard sticks).** Refit the trims so that the steady roll levels fall at f-20, f-16, f-12, f-9, f-6, f, f+3 and f+5 for ppp through fff. This keeps f and mf as they are:

`TIMP_ROLL_TRIM_DB = [(22, 7.7), (34, 9.2), (46, 10.7), (58, 9.8), (72, 9.4), (88, 7.3), (114, 5.9), (124, 2.6)]`

`TIMP_CC1_MAP` stays, because its layer choice per dynamic is right: the layer step between 80-87 and 88-95 falls between mf and f.

Update the TRACKS comment to say the hard-stick trims were fitted on c02 (finding 1).

**Simulated** (with finding 2; timpani re M, rank of 29):
- 872-876: -11.2 -> -18.8 (5th -> 20th). 876-880: -12.3 -> -17.3 (6th -> 15th).
- 930-933: -15.4 -> -19.2 (13th -> 20th). 156-159: -17.5 -> -22.2. 970-974 (p): -17.3 -> -21.1.
- 886-888: -15.4 -> -13.3 (15th -> 8th). 888-889: -18.1 -> -15.7. 1048-1049: -16.2 -> -13.7 (16th -> 10th). The f rolls at 600 and 1088 do not change.
- The 872-888 crescendo now grows about 22 dB. The timpani is never in the top 7, and the master moves by -0.3 to +0.1 dB.
- At p, timpani minus horns goes from +3.8 to about -4 dB.

## 2. The final fff roll (bars 278-279, qn 1108-1113) falls 5 dB under the settle rule and drops out of the last chord (measured)

**Where.** Timpani, 1108-1113: c1:32 fff, tied into the final quarter. The score's note (finale.ily c314) has the roll crescendo from 275 to the fff at 278.

**Evidence.**
- The chain lasts 5 qn, so the generic settle applies: -5 dB over 3 qn, held to the end because the roll ends the piece. On top of that the c10 attack bump (+6 dB) falls away after 0.75 qn.
- vol_db goes from +6.0 at 1108.02 to -5.0 at 1111.
- Timpani re M: 1108-1109 -20.2, 1109-1112 -23.6, 1112-1113 -25.8, ranking 23rd to 25th of 29. In the 100-300 Hz band it is -16.4 dB re master (about 2% of that band's energy).
- In absolute terms the fff roll is only 2.8 dB over the f roll at 1088.
- Brief item 5 has the settle keep long rolls under the texture. This roll lasts 2.1 s at Largamente, and the score asks for the timpani to arrive at fff with the last chord.

**Fix.**
- Option 1 (Finale only): add a skip list to the settle loop in `tools/score_to_parts.py` (roll settle block, the `vol_parts.append(("settle", ...))` line). The new setting is `TIMP_SETTLE_SKIP = []`, default empty, and the Finale sets `[1108.0]`.
- Option 2 (generic): change the settle's 3 qn threshold to seconds, with `TIMP_SETTLE_MIN_S = 3.0`. This would also free the 1.4-2.5 s rolls at 16, 136, 152, 600 and 664. I recommend option 1.

**Simulated** (with finding 1's fff trim +2.6): 1108-1109 -17.0, 1109-1112 -17.3, 1112-1113 -18.3 re M, ranking 18th of 29, under all brass and the violins. The master changes by +0.06 dB.

## 3. Bar 223: Trumpet 1's resolution B to C does not rise and sits 3 dB under Trumpet 3 (measured, identical in c00, c01 and c02)

**Where.** Trumpet 1, qn 884-892: B4 mf with a crescendo, then C5 fff at 888. This is the motto's resolution at the C-major arrival (arrival.ily, bar 223).

**Evidence.**
- Stem levels in 0.25 qn frames:
  - Trumpet 1: -18.0 at 887, -18.3 at 888, -17.9 at 889.
  - Trumpet 3 (E4): -21.6 at 887, then -15.4 to -15.1 from 888.25.
- Re M over 888-892: Trumpet 1 -13.0, below Trumpet 3 -10.0, Trombone 2 -10.5, Tuba -11.0 and the horns (-12.1 to -12.8). Over 884-888, Trumpet 1's B4 is the loudest stem (-9.9).
- So the leading tone is louder than its resolution. The same data rendered the same way three times: B4 to C5 measures +0.3 / +0.6 / +0.6 dB in c00 / c01 / c02, with Trumpet 3 3 dB above. This is not render variance.
- Both notes are on Sus Non Vib MAX. CC1 reaches 120 at 887.90, and vol_db goes from 2.8 to 5.0. Inferred: the 1TP C5 sample at CC1 120 is weaker than the E4 played by Trumpet 3 at the same settings.

**Fix (`build/roles.json`).**
- Trumpet 1 row `[888, 892, 2.0]` becomes `[888, 892, 5.0]`. 888 is an onset, and 892 is the next onset after the printed breath.
- To keep the arrival peak, the Tuba row `[888, 892, 2.0]` becomes `[888, 892, 0.5]`.

**Expected (arithmetic).**
- Trumpet 1 -10.0 re M, level with Trumpet 3 at the top. Tuba -12.5.
- The master's float peak at 888 changes from 1.655 to about 1.636 (Trumpet 1 adds +0.05 at the peak sample, the tuba removes 0.07), so the limiter is not pushed harder.

## 4. The clarinets play fff 5-11 dB over the other woodwinds, and Clarinet 1 is the loudest stem in the canon at bars 226-230 (measured)

**Where.**
- fff beats at qn 888-892, 1048-1052 and 1108-1112 (13 beats).
- The ff canon in Vln I-II, Fl 1, Ob 1 and Cl 1 (qn 900-920).
- The fff span 1052-1080.

Tables: `build/mix.json` `dyn_trim_db` for Clarinet 1-2 and Oboe 1-2.

**Evidence.**
- Co-sounding pairs at the same printed dynamic (median over beats):

  | pair | f | ff | fff |
  |---|---|---|---|
  | Clarinet 1 - Flute 1 | +0.7 | -0.9 | +4.6 |
  | Clarinet 1 - Oboe 1 | +1.1 | +0.9 | +10.8 |
  | Clarinet 1 - Violins I | -4.6 | -0.3 | +2.1 |
  | Clarinet 2 - Flute 2 | -1.3 | +0.5 | +7.5 |
  | Oboe 1 - Violins I | -4.1 | -2.8 | -9.1 |

- The jump at fff comes from the trims (read): Clarinet 1 fff -0.8 and Clarinet 2 -1.9, against Flute 1-2 fff -5 and Oboe 1-2 fff +2.0 with gain -5.3. The clarinets play on their CC1 dynamic layers (`CC1_DYN_TRACKS`), and fff puts them in the top layer.
- Re M in the canon 900-920: Clarinet 1 -8.2 (the top stem), Oboe 1 -9.7, Violins I -10.2, Flute 1 -13.8. At bar 263, Clarinet 1 is -11.3, over Horn 1 -15.3 and Violins II -14.5.
- By the norm a violin section is worth two woodwinds, and the canon's woodwinds double the violins, so Clarinet 1 should sit about 2-3 dB under Violins I and level with Flute 1 (inferred from the norm).

**Fix.**
- `build/mix.json` `dyn_trim_db`:
  - Clarinet 1 fff -0.8 -> -4.0.
  - Clarinet 2 fff -1.9 -> -6.0.
  - Oboe 1 and Oboe 2 fff 2.0 -> 4.0.
- `build/roles.json`: Clarinet 1 `[900, 920, -2.5]`. 900 and 920 are Clarinet 1 onsets, and the note at 920 starts the f plagal close.

**Expected.**
- fff: Clarinet 1 - Flute 1 +1.4, Clarinet 1 - Violins I -1.1, Clarinet 1 - Oboe 1 +5.6, Clarinet 2 - Flute 2 +3.4.
- Canon: Clarinet 1 -10.7, under Oboe 1 -9.7 and Violins I -10.2.
- Bar 263: Clarinet 1 -14.5, Oboe 1 about 2 dB higher.
- The master falls about 0.1-0.2 dB at fff, and 223 and 278 stay the loudest bars.

## 5. The bass drum plays the crash's fff velocity instead of its printed ff (read; level effect inferred)

**Where.** Bass drum at qn 888 and 1108. `tools/score_to_parts.py` `build_perc_track`, `build/score_config.py` `PERC_MAP`.

**Evidence.**
- The Perc staff carries both instruments. At 888 and 1108 its marks are "fff" (crash) and "ff" (bass drum) at the same position.
- `lvl(q)` takes the last mark at or before q on the staff, whichever instrument it belongs to, and both strokes come out at velocity 124 (PERC_VEL fff). Velocity selects among up to 12 layers on this patch (p.121-122).
- The composer marked the bass drum ff on purpose (arrival.ily c146, citing Adler and Piston: a loud bass drum can obliterate the tutti), so that the string tremolo and the violins' C7 sound through.
- Measured: in the first 0.3 s the bass drum is the master's 20-100 Hz band: -0.3 dB re master at 888 and +0.1 dB at 1108. It is -14.6 / -15.3 dB K re master.

**Fix (`build/score_config.py`).** `PERC_MAP["Bass drum"]["bassdrum"]["vel"] = 114`. The `spec.get("vel")` path already exists. Generic alternative: read the dynamic attached to each drum's own voice in `build_perc_track`.

**Expected (inferred).** One or two layers lower: a darker attack and a few dB less sub at both arrivals. Measure the 20-100 Hz share in the first 0.3 s; it should fall to about -2 to -4 dB re master.

## 6. Bars 47-50 (qn 184-200): Clarinet 2's held pp "dal niente" is 11-15 dB under the pp strings, the quietest of the 8 sounding stems (measured)

**Where.** Clarinet 2, the A flat 3 held from 184 to 199.1 (pp, "dal niente"), under Oboe 1's motive x and the pp strings. Tables: `build/roles.json`.

**Evidence.**
- Re M in 2 qn frames: Clarinet 2 -18.8 to -21.6, Violins II -4.7 to -12.1. Over the span: Oboe 1 -3.3, Violins I -8.9, Violas -10.1, Cellos -10.6, basses -11.4, harp -15.4, Clarinet 2 -20.1.
- CC1 is flat at 28 throughout, and the envelope adds only 0-1.5 dB. The note neither emerges from niente nor reaches the pp level of the strings.
- At pp the norm puts a wind level with a violin section. Across the movement the pp pairs read violins minus woodwinds +5.9; in these bars it is +9.5 to +13.2.

**Fix (`build/roles.json`).** Clarinet 2 `[184, 200, 6.0]`. 184 is the note's onset and 200 its next onset. The "dal niente" shape (a CC1 rise from about 10 to 28 over the first 2 qn) is for the articulation lens.

**Expected.** Clarinet 2 about -14 re M, 5 dB under the violins and 10 dB under Oboe 1's solo.

## Do not touch

- Solos over their accompaniment (K re M):
  - Trumpet 1 at bars 51-66: -2.5 against Clarinet 1 -9.4.
  - Violins I's F2 at bars 67-82: -5.6, with the harp -8.0 and the cellos -9.7.
  - Bassoon solo at 115-122: -2.0.
  - Harp solo at 123-134: -4.2.
  - Cor anglais -3.4 with muted Trumpet 1 -6.7 at 171-186.
  - F1 in the bass at 27-34: Tuba -7.3 and Horn 3 -7.8 on the theme over the violins' countersubject (-9.3).
  - The trumpets' theme B at 211-218: -6.6 / -7.9 on top.
  - The chorale at 224-225 and 231-234: brass on top of the string tremolo.
- c02's B changes, now measured on the render:
  - recap 151-166: Vln I -9.3, Horn 1 -9.4, Violas -13.5.
  - 255-258: Tpt 1 -8.5, Horn 3 -9.8, Violas -11.6.
- The crash's level and length (first second -9 to -11 dB K re M, carrying 5-12 kHz, ranked 10-12 of 29 at 888 and 1108).
- Timpani strokes (25 dB from pp to ff on velocity alone), `TIMP_RH_ALT`, `TIMP_CC1_MAP`.
- The hall settings, the bass-octave roles and `loud_eq`.
