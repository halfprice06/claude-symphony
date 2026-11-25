# Cycle 44, critic B: balance and levels (on the c43 render, ahead of the EastWest template mix)

**Method.** All 32 stems and the master of `cycles/c43/render/` (built from `cycles/c43/rendered_build/`, equal to `build/`). For each stem I computed 1/6-octave band powers of the mid and side signals in 8192-point frames (hop 85 ms) on the parts.json tempo map. I also summed the stems by family: strings = Vln I, Vln II, Vla, Vc, Cb, Violin I solo and the three div tracks; winds = 01-11; brass = 12-19 plus Horns 1-2 a2; harp = Harp + Harp harmonics; timpani. For the family EQ predictions I applied the template's ReaEQ bands (`symphony/mockup-research/ew-template-2026-11-08/ho-mix-fx.json`, decoded bands) to those band powers. I used the RBJ biquad code from the finale's `tools/deliver_master.py` (`biquad_h`) and measured the result A-weighted per track and per passage. I also computed what make-up gain would restore each family's c43 level relative to the strings.

Caveats:
- The c43 stems include each patch's own Opus hall. The predictions treat the family EQ as acting on the wet stem, which is also roughly true after the switch, because the sends are post-fader and post-EQ.
- The predictions leave out the mic-layout change and the new returns. The finale measured the Close-led woodwind layout at +2.9 dB hotter than its estimate (`symphony/mvt3/reaper-v600/cycles/c06/CHANGES.md`).
- The strings' 4.73 kHz shelf decodes as bw 0.33 oct. Taken literally, an RBJ shelf with that bandwidth has a -5.4 dB dip at 4 kHz and a +8.6 dB bump at 6 kHz. The finale's c06 Violins II stem shows no such notch: from 2.5 to 10 kHz it is a smooth +3 to +6.6 dB above our c43 Violins II. So I modelled that shelf at bw 2.0. That choice moves the strings' A-weighted change from -2.4 to -1.4 dB. Neither value changes the ranking below.

"Measured" means a number taken from the render or the data. "Predicted" means arithmetic on measured spectra. "Inferred" means a judgement about what a listener hears.

## Manual notes (B5: May 2021 HO manual pp. 114-115, 154-155, 158-159; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.114-115: percussion categories. In the Perc Basics kits "CC 11 (Expression), and Note Velocity control overall loudness, and Note Velocity controls dynamics (up to 16 levels)". | Timpani track (Timpani Flt KS, not a kit) | **Consistent.** The 16 timpani notes use 7 velocities (31-96) for the strokes, CC1 (56 up to the 60s at the crescendo rolls) for the roll layers, and CC7 for the roll level. There is no CC11 lane, so nothing conflicts with the kit's CC11/velocity model. The template EQ question for the timpani is finding 1. |
| p.154: Humanizer (random note on/off 0-100 ms, velocity up to 50%, tuning, volume, pan) | every track | **Not used, correctly.** Random timing and volume would break render-to-render repeatability, which the stem fixes and fitted fills depend on. The tutti spread in plan section 8 is seeded and fixed, which is the right way to get that effect. |
| p.154-155: MIDI Compressor (threshold, ratio, makeup; "notes below the selected threshold are not played") | soft CC11 and velocity values | **Not used, correctly.** A threshold would drop ppp notes, and level range is already handled by the soft trims and deliver_master. |
| p.158: Macro Parameter: one knob drives several automation targets, each with its own depth and scaling graph | the template's "Mod + Expression Combo" on CC1 (plan section 5, c45) | **Not used yet.** This page is where c45's CC1-only test will be set up: the macro's per-target graph is the non-linear spline the plan's section 6 caveat asks for, to cross the 55-76 CC1 zone quickly. No effect on c44 levels. |
| p.159: MIDI Controller Mapping: re-map a CC; "Be careful to avoid conflicting MIDI CC messages" | CC1, CC7, CC11, CC15, CC36, CC69/CC70 sent by the pipeline | **No conflict found in the data.** The pipeline does not re-map anything. One consequence of the switch: CC7 and CC11 now act before the track fader and the post-fader sends, and so does REAPER's volume envelope. A volume-envelope drop no longer cuts a hall tail, because the return keeps ringing. That changes BRIEF S3 and how stem fixes behave (finding 6). |

MANUAL-GAPS read. #4 (Mid mics) is superseded this cycle by the plan's mic layout. #7 (Felt Cresc rolls) and #8 (4 soli on DIV A) are unaffected. No other gap touches the c44 mix work.

## Extra check 1: c43 baseline numbers to compare after the switch (measured)

**Spectral balance, share of total energy (dB).** "Family" means the family's stem sum. After the switch, compare each family's dry stems plus its own return stem with these. The "R Perc" return carries the harp and the timpani together.

| | 200-500 Hz | 250-500 | 100-250 | 2-6 kHz | 6-20 kHz | side/mid dB | L/R corr < 250 Hz |
|---|---|---|---|---|---|---|---|
| master | **-4.91** | -5.67 | -8.75 | -10.43 | **-30.01** | **-6.08** | 0.66 |
| strings | -5.22 | -6.61 | -6.70 | -8.17 | -27.45 | -5.02 | 0.64 |
| winds | -6.64 | -6.78 | -14.74 | -13.64 | -37.49 | -9.40 | 0.83 |
| brass | -3.87 | -4.27 | -12.95 | -15.38 | -34.61 | -6.10 | 0.68 |
| harp | -3.63 | -5.35 | -1.91 | -34.14 | -49.45 | -8.08 | 0.96 |
| timpani | -2.37 | -6.15 | -1.81 | -35.72 | -60.93 | -16.80 | 0.97 |
| Dvořák 9/i (mp3) | -5.66 | -6.31 | -6.61 | -10.53 | -28.82 | -5.32 | |
| Brahms 1/ii, 4/ii | | -5.95, -6.34 | -8.75, -7.55 | -12.43, -11.78 | -32.24, -32.26 | (-4.7..-5.4) | (0.54-0.62) |

**Family balance, A-weighted, each family's sum minus the strings' sum.**

| | winds | brass | harp | timpani |
|---|---|---|---|---|
| whole piece | -2.3 | -2.7 | -25.5 | -20.8 |
| bars 53-60 | -4.9 | -7.9 | | -17.8 |
| bars 61-62 | -2.2 | -1.4 | | -22.2 |
| bars 63-64 | -8.8 | +3.3 | | |
| bars 79-81 | +1.4 | -5.3 | -33.0 | -17.7 |

**Solo margins, A-weighted, lead minus the sum of its accompaniment.** These are the margins to keep after the make-up. Horn 1 bars 7-14 +6.2; Oboe 1 bars 15-16 +7.2; solo violin bars 17-22 +4.4; bass clarinet bars 31-36 +2.8; Flute 1 bars 37-40 +6.6; cor anglais bars 41-44 +2.4 and bars 47-50 +5.8; Oboe 1 bars 45-47 +4.6; Trombone 1 bars 63-64 +2.4 over the strings plus bass trombone; Horn 1 bars 67-70 +4.4; Clarinet 1 bars 85-89 +2.4; Violins I over the celli bars 89-91 +6.4. In bars 61-62 the strings sit +1.4 over the brass and +22.2 over the timpani. In bars 79-81 they sit +5.1 over the horns and +17.6 over the timpani.

**Tutti stops (master).** This movement has only one clean tutti stop: the final chord, which falls 20 dB in **0.50 s** (10 dB in 0.34 s, -7.7 dB at +0.3 s, -28 dB at +0.6 s). At the other large cut-offs, the parts that keep playing hold the master up. Bar 30 to 31 (qn 90; Bn2 and Cbn continue) drops 4.2 dB at +0.3 s. Bar 82 to 83 (qn 274) drops 4.6 and 6.1 dB at +0.3 and +0.6 s. Bar 63 (qn 212, 14 tracks stop under the trombone quotation) drops only 3.7 dB at +0.6 s. The stems that stop at each point fall 20 dB in 0.34 s (qn 90, 8 stems), 0.28 s (qn 212, 14 stems) and 0.22 s (qn 274, 7 stems). The reference recordings measure 0.43-0.58 s (mockup-kit LEARNINGS, "too wet"). The finale's first template render measured 0.62-0.73 s.

**Family tails: time from the start of the fall to -20 dB, on the family stem sums, at every stop with at least 2.5 s of rest after it.**

| family | stops | each t20 (s) | median t20 | median t10 |
|---|---|---|---|---|
| strings | 3 | bar 3/4 0.68, bar 30 0.28, final 0.52 | **0.52** | 0.36 |
| winds | 5 | 0.42, 0.20, 0.52 (bar 63), 0.22, 0.18 | **0.22** | 0.08 |
| brass | 6 | 0.16, 0.34, 0.20 (bar 64 end), 0.26, 0.32, 0.20 | **0.23** | 0.08 |
| harp | 4 | 0.12, 0.14, 0.28, 0.12 | **0.13** | 0.07 |
| timpani | 5 | 0.18, 0.72, 1.10 (bar 62 ff stroke), 0.18, 0.30 | **0.30** | 0.14 |

Measure the same way after the switch: dry family stems plus their own return. If the strings go over about 0.6 s or the winds and brass over about 0.4 s, it will sound wetter than c43, which Dan called right after "too wet".

**Delivered c43 file (measured with ffmpeg and metrics.md).** -19.8 LUFS, LRA 15.5 LU (low -28.8, high -13.2 LUFS), TP -1.6 dBTP, p10-to-max short-term span **18.6 dB**, limiter **2.1 dB** on the loudest sample peak (pre-limiter +0.64 dBFS at 234.43 s, qn about 211.3, bar 62; the next peaks are at 225.4, 228.5, 232.9 and 226.6 s, all in bars 60-62). The ride reaches +10.0 dB maximum and -4.3 dB minimum.

## Extra check 3: span and limiter after the switch (predicted)

With the family EQs, the make-ups below and the master EQ, the K-weighted level change is nearly the same everywhere. It is -2.0 dB in the ppp opening, -2.0 at bars 61-62, -2.2 at bars 79-80, -2.1 at bars 65-66, -1.9 at bars 83-84 and -2.1 at bars 91-92. The exceptions are the wind passages: bar 30-31 -1.0 and bars 35-36 +0.2, because the woodwind make-up slightly over-restores the bass clarinet. The five pre-limiter peaks are strings-led (Vln II, Vc, Vln I and Vla carry 50-80%) and all fall 1.9-2.4 dB together. So the EQ alone should leave the span within about 0.5 dB and the limiter at about 2 dB once deliver_master is renormalised.

What will move them is the returns. Longer tails after bars 64 and 82 raise the soft frames in bars 65-66 and 83-84, which hold about 40% of the frames at or under p10. That narrows the span from below (inferred: by roughly 0.5-1.5 dB if the strings' t20 reaches 0.6-0.7 s). Re-fit deliver_master after measuring. Do not pre-empt it by changing the ride.

## Findings, ranked by what a listener would hear

### 1. The template's timpani EQ would make the timpani the bass of the orchestra at every roll (predicted from measured spectra; Dan's rule 5)

- **Where.** Timpani, every roll and stroke: bars 1-3 ppp, the crescendo roll at bars 52-53 (qn 168-172), bars 60-62, the ppp rolls of bars 67-70, bars 78-81 and the coda answer at bars 84-85.
- **Evidence.**
  - The template timpani EQ adds +8.6 dB at 84 Hz (bw 1.39), -11.5 dB at 385 Hz and a +9.1 dB shelf at 7 kHz. It loses 6.8 dB A-weighted overall, so restoring the timpani's c43 level against the strings would take +5.4 dB of make-up. With that make-up, its 20-100 Hz band rises **+12.1 dB**.
  - The timpani's share of the master's 30-150 Hz then goes from 12 to 58% in bars 1-3, 25 to 80% at qn 168-172, 7 to 28% at bars 60-62, 8 to 36% at bars 67-70, 8 to 27% at bars 78-81, and 18 to 68% at the coda answer. The finale's critic target is at most 18%.
  - The finale's version (no 84 Hz bell, -6 dB at 385 Hz, +4.5 dB shelf) loses 4.4 dB A. With a full A-weighted make-up of +3.0 dB the shares become 19 / 41 / 8 / 14 / 10 / 29%. Even that over-lifts the bass, because A-weighting under-counts 40-150 Hz.
  - The template's timpani carries a Surround-led mic mix (plan section 1: Close -8 / Main -7 / Surround 0 dB; our Close 0.2 / Main 0.5, no Surround). Its low bell was tuned for a different signal, as the finale's critic B also inferred.
- **Fix.** `build/mix.json` timpani `family_eq` = the finale's bands: HPF 44 Hz, bell 385 Hz -6 dB bw 2.54, high shelf 6.96 kHz +4.5 dB bw 1.39. Keep `gain_db` -7 with **at most +1 dB** of make-up (not the A-weighted +3), and keep TIMP_CC1_MAP and the CC7 roll shapes. Drop the per-track 45 Hz high-pass (the family HPF 44 does it).
- **Check.** Timpani share of the master's 30-150 Hz at most 18% at each roll window above. In K-weighting the ppp rolls stay 3-5 dB under the quietest sustained string section (kit LEARNINGS §13). At bars 61-62 the timpani rank stays where c43 had it, 11-23 dB K under the master.

### 2. Brass make-up must be per track, not one family value: the soft horns lose 2-3 dB more than the trombones (predicted)

- **Where.** Horn 1's solos (bars 7-14, 67-70, the bar 56-60 counter-melody), the horns at bars 79-81, and Trombone 1's quotation at bars 63-64.
- **Evidence (A-weighted change from the family EQ, whole piece; soft half in brackets).**
  - Horns: Horn 1 -8.2 (-8.8), Horn 2 -6.7 (-8.9), Horn 3 -9.0, Horn 4 -9.7, Horns 1-2 a2 -8.6.
  - Low brass: Trombone 1 -5.9, Trombone 2 -7.6, Bass trombone -7.7, Tuba -7.4.
  - For comparison: winds -3.6 to -4.8, strings -1.0 to -2.6, harp -6.6, harp harmonics -4.4.
  - Why the horns lose most: their energy sits at 300-1000 Hz, where the brass EQ takes 5.9-11.5 dB. The soft horns also already carry c32/c37's 800 Hz -8 shelf.
  - With a single brass make-up that restores the family sum against the strings (+5.9 dB):
    - Horn 1's bars 7-14 margin goes **+6.2 to +4.3** (with no make-up at all, +1.6);
    - Horn 1 at bars 67-70 goes +4.4 to +3.7;
    - the horns fall from 5.1 to 6.7 dB under the strings at bars 79-81;
    - Trombone 1 over the strings rises from +2.4 to +3.7. Rule 9 says weight, not bite, so the quotation should not gain level.
- **Fix.** `build/mix.json` `gain_db` make-up on top of the family EQ. These values restore each track's c43 level against the strings (-1.4 dB): Horn 1 +7.0, Horn 2 +5.5, Horn 3 +7.5, Horn 4 +8.0, Horns 1-2 a2 +7.0, Trombone 1 +4.5, Trombone 2 +6.0, Bass trombone +6.0, Tuba +6.0. Winds: Fl1/Fl2/CA/Cl2 +3.3, Ob1 +3.1, Ob2 +2.7, Cl1 +3.0, BCl +2.8, Bn1/Bn2 +3.4, Cbn +2.2. Harp +5.2 with the template HPF 183 or +4.2 with HPF 80 (finding 4). Harp harmonics +3.0. Then measure the dry stems against the c43 family and solo numbers in extra check 1, and correct the mic-layout difference as a level-only stem fix, as the finale did (its winds were 2.9 dB hot). The template's own bus faders (brass +2.93, woodwinds +3.36 dB) are part of the same make-up. Do not add them on top.
- **Check.** Horn 1 over its accompaniment in bars 7-14 between +5 and +8 dB A. Horn 1 bars 67-70 at least +4. Trombone 1 bars 63-64 no more than +3 over the strings plus bass trombone. Horns at bars 79-81 4-6 dB under the strings.

### 3. The mix will come out about 6 dB too bright at 6-20 kHz, and the return low-pass cannot fix it (predicted)

- **Where.** The master's top octave over the whole piece, most of all in the string passages.
- **Evidence.**
  - Applying the family EQs, the make-ups of finding 2 and the master EQ to the c43 spectra moves the master's 6-20 kHz share from **-29.4 to -23.1 dB** (the references sit at -28.8 to -32.3; the finale measured -25.1 after its switch). It moves 2-6 kHz from -10.5 to -8.0 and 500-2000 Hz from -3.05 to -4.55 (references -3.5 to -4.4). It leaves 200-500 Hz about unchanged (-5.0 to -4.7).
  - After the EQ, 71% of the master's 6-20 kHz comes from the strings and 23% from the brass. Most of the top is in the dry stems, so the 2.3 kHz low-pass on the returns (plan section 9) darkens only the tails.
  - Most of the rise comes from cutting the 0.5-2 kHz body (strings -5 dB at 1 kHz, brass -7.8 dB at 821 Hz). The shelves add the rest. Halving every family shelf only gets to -24.4, and removing the string shelf entirely to -25.0.
  - Removing Violins I's 5 kHz -4 dB shelf as a "duplicate" would make it worse (-21.5).
- **Fix.**
  - Keep `Violins I` and `Violin I solo` `eq` highshelf 5000 Hz -4. They are not duplicates: they cancel the family shelf on the brightest section, which is what c09 put them there for.
  - Use the 2.3 kHz return low-pass as the plan says.
  - After the render, if the master's 6-20 kHz share is above -27 dB, halve the strings' and brass family shelves (+2 dB). If it is still above -27, add the same 5 kHz -4 shelf to Violins II and Violins II div. Do this before touching the body bands, which carry the template's tone.
  - This is a pass-2 decision on measured numbers, not a reason to delay the template.
- **Check.** Master 6-20 kHz share between -28 and -31 dB; 2-6 kHz between -10 and -12; 500-2000 Hz no lower than -4.5.

### 4. Harp: the template's 183 Hz high-pass removes the bars 7-14 bass line; c43's -2 dB harp role then duplicates it (predicted)

- **Where.** Harp bars 7-14 (qn 18-42, pp, left hand 8va bassa E flat 1 to C3, 39-131 Hz), and the harp's other low dyads.
- **Evidence.**
  - With HPF 183 the harp loses 6.8 dB A and 7.8 dB in 40-200 Hz in bars 7-14. With the finale's HPF 80 it loses 4.9 dB A and 3.9 dB in 40-200 Hz.
  - c43's role `[17.9, 44.0, -2.0, 0.5]` (c43 B #3) was set because the harp carried 68% of that band under the horn solo. After the family EQs the harp carries 36%, the bass clarinet 48% and Horn 1 9%.
  - In the same passage the horn's share of 2-4 kHz rises from 59 to 82% and the bass clarinet's falls from 39 to 16%, because the woodwind EQ's -4.7 dB at 2.2 kHz stacks on the bass clarinet's own 2.5 kHz -4 shelf.
- **Fix.**
  - `build/mix.json` harp `family_eq` with HPF 80 Hz in place of 183, as the finale did. A 183 Hz high-pass takes the fundamentals out of a bass line the score prints 8va bassa (inferred).
  - `build/roles.json`: remove the Harp `[17.9, 44.0, -2.0, 0.5]` row.
  - Remove the bass clarinet's static `eq` highshelf 2500 Hz -4. Keep its bars 7-14 `loud_eq` (1.2 kHz -3 over qn 0-44). With the static shelf gone, its share of 2-4 kHz under the horn rises to about 30%, still under c40's 73% problem.
  - Remove the per-track harp high-pass (30 Hz) and the Harp harmonics high-pass (40 Hz); the family HPF covers both.
- **Check.** Bars 7-14: harp within 1 dB K of the bassoons (the c43 target); the harp's share of master 88-177 Hz between 50 and 70%; Horn 1 margin as in finding 2.

### 5. Coda: the string EQ costs Violins I's C5 more than the celli's A flat, and the harp harmonics and timpani answer rise (predicted)

- **Where.** Bars 83-92 (qn 274-304).
- **Evidence (A-weighted margins, c43 vs the switch with the finding 2 make-ups).**
  - Violins I over the celli at bars 89-91: **+6.4 to +5.1**. The -5 dB 1 kHz bell sits on C5's second harmonic (1046 Hz), while the celli's A flat 2 lies below it.
  - Harp harmonics over the celli div and basses at bars 83-86: **-0.1 to +2.1** (harp family shelf +8 dB at 7.7 kHz, -8.6 dB at 1.27 kHz).
  - Timpani over the soft strings at bars 84-85: **-6.2 to -2.7** with the template timpani EQ, about -5 with the finale's.
  - Clarinet 1 at bars 85-89: +2.4 to +2.6 (unchanged).
  - Bars 15-22 solos rise slightly: Oboe 1 +1.0, solo violin +1.2.
  - This undoes about half of c43 B #4 (the celli -2.5 role was set so that Violins I's C5, the pitch movement I ended on, leads).
- **Fix (after the render, by measurement).**
  - `build/roles.json`: if Violins I over the celli at 292-301 falls under +5.5 dB A, deepen the Violoncellos `[291.9, 300.9, -2.5, 1.0]` row to -3.5.
  - Cut c43 B #2's +2 dB coda role on Harp harmonics `[273.9, 283.0, 2.0, 1.0]` back to 0 if the harmonics measure more than 1.5 dB over the celli div.
  - Leave the timpani answer to finding 1's EQ choice.
- **Check.** Violins I is the loudest string stem at 292-301. Harp harmonics are 0-2 dB A over the celli div at 274-283. The timpani at 277-283 is still the loudest stem at its strokes, as the answer.

### 6. EQs and trims that only duplicate the family EQ, and the level workflow after the switch (data; measured where stated)

- **Remove, because the family EQ already does it.**
  - The 40 Hz high-passes on Violins I/II, violas, Violin I solo, Violins II div and Violas div; the 30 Hz ones on Violoncellos and Violoncellos div; and the basses' 25 Hz. The strings' HPF 53 supersedes all of them.
  - The 40 Hz high-passes on Horns 1-4, Horns 1-2 a2, Trombones 1-2 and bass trombone, and the tuba's 25 Hz. The brass HPF 41 supersedes them.
  - Timpani 45 Hz, harp 30 Hz, harp harmonics 40 Hz.
  - Horn 1's and Horn 3's `loud_eq` 300 Hz -2 dB bell (c40 B #1, set for 300 Hz build-up). The brass EQ's -5.4 dB at 475 Hz (bw 1.92) already takes 3-6 dB there. Remove with it Horn 1's c40 "+1 to keep the level" in `soft_trim_db`, which compensated for the bell.
  - The bass clarinet's static 2.5 kHz shelf (finding 4).
  - The harp role in bars 7-14 (finding 4).
- **Keep, because each fixes something the family EQ does not.**
  - The horns' soft `loud_eq` 800 Hz -8 shelf. The family EQ leaves Horn 1's soft 1-5 kHz share where it was (-18.3 to -18.0 dB in bars 7-14, -21.3 to -21.6 in bars 67-70) and does not darken soft playing; c30 measured that the real soft layers sit near -19 to -20.
  - Violins I and solo 5 kHz -4 (finding 3).
  - Violins II div 1 kHz -10 (single Close mic).
  - Violins II's 3 kHz `loud_eq` at 140-170.
  - Vc 170 Hz +3, Cb 160 Hz +4.5 and 80 Hz -6, and both climax `loud_eq` rows. The family EQ is at -0.4 dB at 200 Hz, so it does not touch the body bands.
  - Contrabassoon 70 Hz -4, Trombone 1's accent 2 kHz shelf, the Horns 3-4 `mute_eq`, every `side_shelf`, and the woodwinds' 30-40 Hz high-passes (the woodwind family EQ has none).
- **Conflict to resolve.** Duc's basses cut (-2.4 to -3.6 dB at 205-250 Hz, plan section 8) overlaps the basses' 160 Hz +4.5 bell (bw 1.4, about 105-250 Hz). At 230 Hz they nearly cancel (+2.4 - 3 = -0.6). If the Duc cut goes in, move the body bell to 140 Hz +4.5 bw 1.0, so the c25 body (C2-G2 harmonics) stays and the 205-250 Hz band falls as Duc intended (inferred).
- **Low end (predicted).**
  - The strings' HPF 53 plus the master HPF 42 takes 10.0 dB at E1 (41 Hz), 7.8 at F sharp 1, 5.1 at A1 and 3.4 at C2. That lands on the basses' lowest notes, the 4 soli E flat 1 pedal region of bars 65-70 and the coda pedal.
  - Overall the master's 20-100 Hz share still rises from -18.4 to -17.0 dB, because the body bands fall more than the bass. Dvořák is -21.7 and Brahms -8 to -8.5, so this is not a problem in itself.
  - Check the bars 65-70 E flat 1 pedal against Horn 1. c41 needed it at +1.5 over the c39 means.
- **Level workflow.**
  - With post-fader sends, a track's volume envelope (roles, trims, LEVEL_SHAPES, fills) now feeds its return.
  - Sudden drops in the envelope will leave the hall ringing. That is good for S3: the bar 66 niente and the qn 195-196 dip no longer need CC7 for that reason.
  - A stem fix on a dry stem no longer changes the matching part of the return stem. For level-only fixes after the render, scale the return stems by each family's mean change (as the finale's `stem_fix.py --return-gain` does), and say in CHANGES.md which numbers are dry-stem and which master.
  - `tail_hold` matters less but still governs the dry stems. Keep it.

## Also measured, no change

- **Side and mid.** The master is at -6.08 dB side/mid with L/R correlation 0.66 below 250 Hz; the references are -4.7 to -5.4 and 0.54-0.62. Strings -5.0, winds -9.4, brass -6.1, harp -8.1, timpani -16.8. pan_by_mic (Close at the seat, Main full width) should widen the image. Re-measure before changing any side shelf. Strings at -4.5 to -5.5 and the master at -5 to -5.5 would match the references.
- **Peaks.** The bar 62 limiter peaks are strings-led (Vln II 30%, Vc 22%, Vln I 18%, Vla 10% at 234.43 s). The c43 Horn 2/Horn 3/basses shapes at 210-212 still hold. The brass make-up in finding 2 does not change that ranking.
- **Bass solid, not boomy.** The c43 20-100 Hz share is -19.3 dB (metrics), between the references.

**Do not touch:**
- c43's Horn 2/Horn 3/basses LEVEL_SHAPES at 210-212 (limiter);
- Horn 1's bars 7-14 +4.5 role and the -1.5 on the bassoons and bass clarinet (re-check them only after the per-track make-up);
- c42's +3 on Horn 1 at 184.1-195.35;
- the c39/c41 bars 61-62 balance and `_all` -0.4 at 204-212;
- Trombone 1's CC7 110/120 and its accent shapes;
- TIMP_CC1_MAP and the timpani CC7 roll shapes;
- the violas' -5 at 219.85-225.9 and the bar 66 niente in CC7;
- the basses' pedal re-levelling (relevel41.py) and the 400 ms pp/p cap;
- the coda Clarinet 1/cor anglais duet levels;
- the divisi and soli track gains;
- the horns' soft 800 Hz shelf;
- Violins I's 5 kHz -4 shelf;
- the side shelves, until side/mid is re-measured with pan_by_mic.
