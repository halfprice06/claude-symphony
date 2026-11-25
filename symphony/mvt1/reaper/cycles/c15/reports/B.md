# Cycle 15, critic B: balance and levels (render c14)

## Method

All numbers come from the stem-fixed c14 render (`cycles/c14/render/`, 33 stems), mapped through `build/parts.json` (16:39, the stem-fixed state). Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c15-B/`. They are the c14-B set plus these:
- `hres2.py`, `hotscan.py`, `pitchlist.py`: per-pitch residuals.
- `trraw.py`, `tpair.py`, `simtpt.py`: trumpet levels.
- `dimsoft2.py`, `cressoft.py`: hairpins against soft trims.
- `cover.py`, `rev2.py`, `marg2.py`, `loudacc.py`: covering checks.
- `acc15.py`, `loopchk.py`: Dan's two checks.
- `simall.py`: audio simulation of findings 1-3.

Definitions:
- **Level:** K-weighted power in 10 ms hops.
- **re master:** a stem minus the master over the same window.
- **raw:** a note body minus the track's volume envelope at that point (gain + vol_db + dyn/soft trim), which leaves the sample's own level.
- **Neighbour residual:** a note body minus the median of the same track's notes within ±8 CC11 and ±5 semitones.
- **Simulation:** the c14 master plus Σ stem × (gain - 1), sample-exact, then run through `tools/deliver_master.py`. On the c14 master the baseline is LRA 14.8 LU, span 19.5 dB, limiter 1.5 dB.

## What holds (measured)

- **Section ratios against Rimsky-Korsakov.** Pair medians at the same printed dynamic (f / ff / fff):

  | Pair | Measured | RK |
  |---|---|---|
  | Horn - single woodwind | +3.0 / +3.2 / +4.4 | +3 |
  | Trumpet - woodwind | +6.5 / +4.7 / +5.3 | +6 |
  | Low brass - woodwind | +6.5 / +5.3 / +5.2 | +6 |
  | Trumpet - horn | +2.2 / +2.2 / +1.0 | |
  | String section - woodwind | +4.4 / +4.4 / +4.8 | |

- **The c14 string soft trims worked.** String pp minus wind/brass pp is now -0.4 dB (c13 +1.9).
- **Percussion is in proportion:**
  - The tam-tam fff is the loudest stem for the first 4 beats of bar 122 (-7.7..-10.9 re master). It settles to -15 under the pp of bar 126.
  - Crash cymbals: -11.5 re master (K) at the hit.
  - The suspended-cymbal crescendo peaks in 5-20 kHz at qn 635.5.
- **Timpani:** never the loudest stem outside the opening solo. The most is -6.3..-8.7 re master, in bars 2-4 and 80-81.
- **Climax order** on the delivered mp3 is unchanged (160 > 122 > 167-170).
- **Accent attacks** (2-5 kHz over the first 80 ms minus the body, all printed accents):

  | Family | Median | Notes over +3 dB |
  |---|---|---|
  | Brass | -7.2 | 2 of 145 (Tpt1 284 +4.2, Tpt1 676 +3.9) |
  | Winds | -6.2 | 8 of 220 |
  | Strings | -4.3 | 8 of 192 |

  The worst wind and string values (+6..+16) are the known qn 536 ff-to-mf tail artefact.
- **Loop pulsing:**
  - Master autocorrelation at 3.95 s, 100-300 Hz band / centroid: 464-500 -0.24 / -0.19, 696-728 +0.01 / -0.05, 712-728 -0.13 / +0.09.
  - Only 8 unsplit notes last 6 s or longer, all under 7.3 s, so the lag overlap is 3.3 s at most.
  - Horn 4 at 289 reads 0.59 / 0.64, but on that overlap the reading is unreliable.

## 1. Every horn plays F4 about 5 dB hot, and movement I has no F4 trim (measured)

**Where:** all horn tracks, wherever F4 (MIDI 65) appears below ff. The places it is heard:
- Bar 57 (qn 224-228).
- Bars 156-157 (620, 624).
- Bars 164-165 (652, 656).
- Bars 132-137 (526, 528, 545).

**What is wrong.** The 1FH KS Master's F4 is louder than its neighbours at the same CC11:

| Track | F4 neighbour residual | Notes | Next to it |
|---|---|---|---|
| Horn 1 | +5.1 dB median | 15 | E4 -2.4, G4 -2.8 |
| Horn 2 | +5.3 | 20 | at every dynamic, ff included (+5.2..+5.7) |
| Horn 3 | +6.0 | 2 | |
| Horns a2 | +3.0 | 3 | |

Movement II measured the same pitch (+5.0) and trimmed it on all four horns, `{"65": {"early": 1, "body": -5}, "_all_arts": true}` (kit LEARNINGS section 13). In `build/pitch_trims.json` here, Horn 1 and Horn 3 have only `72: -5`, and Horns 2, 4 and a2 have nothing.

**What a listener hears:**
- **Bar 57, qn 224.** Horn 2's p countermelody F4 is -3.3 re master. That is the loudest stem, 5.9 dB over the Violins I melody (-9.2). The F4s at 228 and 236 are level with the melody.
- **Bars 164-165.** Horn 1's p whole-note F4s are the loudest stem at -5.5..-8.8 re master. They sit 1-4 dB over the Clarinet 1 mp line (F-A♭-B♭-D, -7.6..-12.4) and over the Violins I mp line, both printed louder.
- **Bar 157, qn 624.** The F4 is +9.3 over the CC fit, at -6.9 re master.

**Fix:**
- `build/pitch_trims.json`:
  - Horn 1: add `"65": {"early": 1, "body": -4.5}` (it already has `_all_arts`) and `"_skip_onsets": [97.0, 189.0, 206.0, 592.0]`. Those four F4s already carry note trims (-4, -6, -2, +1) and now sit at -2..-6.
  - Horn 2 and Horn 3: the same entry, with `"_all_arts": true`.
  - Horns a2: `"65": {"early": 1, "body": -3}`, `"_all_arts": true`.
  - Horn 4 never plays F4.
- Optional, the same kind of problem: Horn 3 D4 (62) is +3.4 (n 18) at mp-f and about 0 at ff. Add `"62": -2.5` with `_skip_onsets` `[100, 328, 330, 484, 488, 676]`.
- Refit `accent_fits.json` only for accents on F4 (the brass fit is keyed to the old level).

**Expected:**
- Bar 57: Horn 2 F4 about -7.8 re master, under Violins I.
- Bars 164-165: Horn 1 about -10..-13, under the clarinet.

## 2. The soft trims rise into pp, so printed decrescendos into pp do not fall (measured; fix simulated)

**Where:**
- Bar 14 (qn 52-55): Horn 1's solo ends while Bassoon 2 holds its p > pp.
- Bar 44 (172-176): Horns 1-2, p > to nothing, before the oboe solo.
- Bar 106 (420-424): the decrescendo of horns, bassoons and celli into the viola solo.
- Every soft decrescendo on a horn, trombone, bassoon or Clarinet 1.

**What is wrong.** `tools/build_reaper.py` `vol_points` reads the soft trim from the interpolated `dyn_curve`. The trims are larger at pp than at p (`build/mix.json`):

| Track | pp | p | mp | mf |
|---|---|---|---|---|
| Horn 1 | 15.8 | 10.6 | 7.2 | 2.0 |
| Horn 4 | 16.7 | 12 | 6.7 | |
| Bassoon 2 | 12 | 8 | | |
| Clarinet 1 | 7.7 | 3.3 | | |
| Trombones | about 4 dB more at pp than at p | | | |

So across a decrescendo the envelope rises by 2-9 dB and cancels most of CC11's fall.

Measured on 31 soft decrescendos (starting at mf or softer, the note held through):

| Group | Count | Median fall | Falling less than 2 dB |
|---|---|---|---|
| Trim rises ≥ 2 dB across the hairpin | 20 | -1.7 dB | 10 |
| The others | 11 | -4.1 dB | 3 |

Worst cases:
- **Bar 44.**
  - Horn 1 rises +5.3 dB through its printed decrescendo; its trim rises +5.5.
  - Its B♭4 at 174 becomes the loudest stem (-1.2 re master).
  - The master jumps +4.1 dB at 174, inside the p >.
  - Horn 2 falls only 1.2 dB.
- **Bar 106.** Horns 1/3/4 +0.2/+0.1/+0.2 dB, bassoons +1.2/+1.5, celli -0.5. Their trims rise +5.2/+7.3/+9.2/+1.8/+2.0/+2.3.
- **Bar 14.**
  - Horn 1's last note falls only 0.7 dB.
  - Bassoon 2 holds level (-47.6/-48.4 dB abs) through its p > pp.
  - Bassoon 2 ends 1.7-3 dB over the end of the horn solo.

Crescendos are not affected (median +3.6 dB with falling trims), because the hairpin dB ramps carry them.

**Fix:** in `tools/build_reaper.py` `vol_points`, for each decrescendo in `tr["hairpins"]` that starts at CC 72 or lower:
- From the hairpin start to the first moved onset after its end, use `min(trim(cc), trim(cc at the hairpin start))` in place of `trim(cc)`.
- In other words, the trim may fall but never rise inside a decrescendo. The next note picks up its own trim.

No CC11 change.

**Simulated** (`simall.py` B, audio-exact):
- Bar 44: the master step at 174 goes from +4.1 to +1.4 dB; 173-175 falls 1.1-3.8 dB.
- Bar 14: beats 52-54 fall 1.6-2.4 dB more, so the end of the solo is no longer under the bassoon.
- Bar 106: -0.4/-0.8 dB.

With findings 1 and 3 included:
- Delivered LRA 14.8 -> 15.0 LU.
- Span 19.5 -> 19.7 dB.
- Limiter 1.5 -> 1.4 dB.

The span rises because the decrescendo tails now get softer; take it back in `deliver_master.py`, not by restoring the trims.

## 3. The second and third trumpets play over the first at ff and fff (measured; fix simulated)

**Where:**
- Bar 140 (qn 556-559).
- Bar 141.
- Bar 158 (629).
- Bars 122-123 (484-491).
- Bar 160 (637).
- Bars 113-115 (451-458).

**What is wrong.**
- The ff/fff dynamic trims are Trumpet 1 7.3/6.6, Trumpet 2 10.5/10.4, Trumpet 3 12.1/11.6 dB.
- They make up for the lower register's weaker samples: on the 1TP KS Master, raw level rises 0.35 dB per semitone (fit on 126 f-fff notes, residual sd 2.4).
- When Trumpet 1 plays in the same register as the others, the extra 3-5 dB puts the lower parts on top. Trumpet 2 minus Trumpet 1 is +0.4 dB at ff and 0.0 at fff, and Trumpet 3 minus Trumpet 1 is +1.5 at fff. The first trumpet never leads its section.

The spots:
- **Bar 140.**
  - Trumpet 2's F4 is -10.7 re master, the second-loudest stem, 6.0 dB over Trumpet 1's A♭4 in the same chord.
  - Their raw levels are equal (-33.4 / -33.6); only the envelope differs (+9.5 against +3.3).
- **Bar 158.** Trumpet 2's held G4 (-7.8 re master) is 6.7 dB over Trumpet 1's E5 as Trumpet 1 enters with the tune. The trumpet section has the theme there with the oboe and the violins.
- **Bar 122 (fff).** Trumpets 2/3 are +2.5/+3.1 over Trumpet 1. Trumpet 3's B3 runs at +17.3 dB of envelope.
- **Bars 113-115.** Trumpet 1's slurred crescendo figure sits 4-7 dB under Trumpet 2's and Trumpet 3's held notes.

**Fix:**
- `build/mix.json` `dyn_trim_db`:
  - Trumpet 2 `{"f": 6.2, "ff": 8.5, "fff": 8.4}`.
  - Trumpet 3 `{"f": 7.7, "ff": 11.1, "fff": 9.6}`.
- `build/roles.json`:
  - Trumpet 1: change `[556, 568, -3]` to `[556, 568, -1]`, and add `[451, 456, 3, 0.5]`.
  - Trumpet 2: add `[628, 631, -3, 0.25]`.

**Simulated:**

| Measure | Now | After |
|---|---|---|
| Trumpet 2 - Trumpet 1, ff | +0.4 | -1.4 |
| Trumpet 2 - Trumpet 1, fff | 0.0 | -2.0 |
| Trumpet 3 - Trumpet 1, fff | +1.5 | about -0.5 |
| Trumpet 3 - Trumpet 1, ff | -1.9 | about -2.7 |
| Bar 140, Trumpet 2 over Trumpet 1 | +6.4 | about +2.4 (with the Trumpet 1 role) |
| Bar 158 | +6.7 | about +1.7 |
| Bar 122, Trumpet 2 / Trumpet 3 over Trumpet 1 | +3.6 / +3.1 | +1.6 / +1.1 |

The section stays within RK: trumpet minus horn drops by about 1 dB, from +2.2 to about +1.5.

## 4. The loud tutti is thin at 100-300 Hz and bright at 1-5 kHz (measured; cause partly inferred)

**Where:** the loudest 10% of frames (every ff/fff tutti).

**Evidence.** Band share of total energy, loud frames, mix against the Dvořák 9/i reference:

| Band | Mix | Dvořák |
|---|---|---|
| 100-160 Hz | -15.3 | -10.9 |
| 160-300 Hz | -9.8 | -7.3 |
| 1-2 kHz | -5.6 | -7.0 |
| 2-5 kHz | -9.4 | -11.1 |

In the mid and soft frames, 100-300 Hz matches within 1 dB (mid: -12.8/-7.5 against -13.8/-7.6). Over the whole file the mix is also the thinnest and the brightest of the three references:

| Band | Mix | Dvořák | Brahms 1/ii | Brahms 4/ii |
|---|---|---|---|---|
| 100-250 Hz | -9.9 | -6.6 | -8.8 | -7.6 |
| 2-6 kHz | -10.1 | -10.5 | -12.4 | -11.8 |

Inside the loud frames:

| Group | Band | Loud | Mid |
|---|---|---|---|
| Strings | 2-5 kHz | -6.6 | -9.8 |
| Brass | 160-300 Hz | -11.8 | -6.9 |

The brass change follows the c09 CC1 dynamic layers. Violins I alone supply 39% of the loud frames' 2-5 kHz.

The `loud_eq` bell on Violins I (3 kHz +2 dB, bw 1.5) dates from c05. At that point the loud tutti was 2-3 dB darker than the references at 2-4 kHz, and the CC1 brass brightening had not yet happened. Inferred: that bell is now stale (kit section 13, on old level changes going stale).

**Fix:**
- `build/mix.json` Violins I: delete the 3 kHz `loud_eq` spec (keep the other EQ). Estimated from the band share: master 2-5 kHz in the loud frames -0.7 dB, and Violins I K level in the tutti about -0.5 dB. Then check the Violins I margins at bars 27-31, 117-121 and 158-161.
- For the 100-300 Hz body, no cheap fix was found. A band simulation of a 200 Hz +3 dB `loud_eq` bell on Trombones 1-2 and all horns moved the loud 160-300 Hz share only +0.4 dB. The celli supply 24% of that band. Treat this as open and do not add more low-end EQ to the basses.

## 5. Smaller items (measured)

- **Double basses F2 (41) booms.**
  - Its 20-100 Hz band is -0.3 dB re its own K level, against -3.8/-3.7 on E2/G2.
  - Its body is +2.2 over its neighbours (n 14). The worst notes are bars 7 and 147-152 at pp/p (+3.6..+8.6).
  - Fix: `build/pitch_trims.json` Double basses, add `"41": -2` (the c25 kit proposal that was never made).
- **Trumpet 2's pp G4 at bar 113 (448).** It enters 7 dB under Trumpets 1 and 3 (raw -56.2 against -49), so the pp brass chord has a hole for its first bar. Fix: `build/note_trims.json` Trumpet 2 `{"448.0": 4}`, with the step ramp, inside the crescendo.

## Do not touch

- The section ratios at f/ff/fff.
- The c14 string soft trims.
- Percussion gains, roles, patches and timing (tam-tam fff and pp, crash, sus. cymbal).
- The Trumpet 1 coda a2 lift (+3 note trims at 664.5-675.5). It leads the a2 theme by 2.4-3.4 dB over Horns a2, as the a2 marking implies.
- The climax order with `FAST_CAP_ABOVE` 4 / top ride 1.6.
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`.
- The Horns a2 windows and roles.
- The second-theme fills and `HP_TARGET_AT` set.
- `_REBOW_FROZEN`.
- `accent_fits.json`, except refits after finding 1.
