# Critic B, cycle 56: balance and levels (c55 render)

Under review: `cycles/c55/render` (dry stems, returns, master), `build/parts.json`, `build/mix.json`, `tools/score_to_parts.py` (the `vol_parts` items), `tools/build_reaper.py vol_points`. `cycles/c56/COORDINATOR-NOTES.md` was read first. Scripts and their outputs: `cycles/c56/critic_scripts/B/` (`low.py` → `low.txt`, `cbpitch.py`, `shares.py`, `sim2.py`, `env.py` → `env.txt`, `bal.py` → `bal.txt`, `chk.py`). Nothing was rendered; REAPER, the lock, `build/`, `tools/` were not touched. I cannot hear the render; every judgement is marked measured or inferred.

Method. Low-frequency spectra are whole-passage averaged FFTs (65536 points, 0.73 Hz) of the files; third-octave bands and shares are relative to the 20 Hz-20 kHz total, the same definition as the reference `metrics.json` files. EQ changes are simulated exactly on the stems: the stem's whole-file FFT is divided by the complex response of the bands to be removed (RBJ biquads, bandwidth in octaves, `eqlib.py` of c52), the difference is passed through `master_eq` and added to the master. The reverb returns are not changed in the simulation (each holds under 6 % of the bands concerned). Levels per note and per quarter are K-weighted, 4096-point frames, hop 1024.

## Manual notes

No row for c56 in `loop/MANUAL-READING.md` (third round, critics pick). Read: May 2021 HO manual section 3.2.5 "How to Produce Realistic Performances" (printed p.64), `MANUAL-GAPS.md`, `EW-TEMPLATE-PLAN.md` sections 3 and 8.

| Reading | Where it applies here | Does the render follow it |
|---|---|---|
| "Volume should be used to set a loudness level relative to other instruments, while Expression should be used to shape the continually changing dynamics and expressiveness of each instrument individually" (p.64) | The track volume envelope carries both: the slow relative levels (roles, dynamic trims, hairpin gain) and 2250-4200 points of per-note shape per string track | Half. The slow layers are what the manual assigns to volume. The per-note layers are shape, which the manual assigns to CC11; finding 2 measures that they do not move balance |
| CC11 "controls overall loudness and dynamics" on the strings and woodwinds; on the LITE rows CC1 sets dynamics and vibrato together (p.64) | Sus Marc LITE theme rows (146 Violins I notes) | Followed since c54; the body lift on these notes has to stay in the envelope because CC11 on this row cannot hold a body over a decaying marcato sample (finding 2, keep list) |
| Template plan section 3: timpani +8.6 dB at 84 Hz; master HPF 42 Hz, -1.6 dB at 167 Hz | `mix.json` `family_eqs.timpani`, `master_eq` | The timpani boost is absent (HPF 44, -6 at 385 Hz, shelf only), the soft rolls carry a -3 dB 160 Hz shelf, and the master has an added -1.5 dB bell at 260 Hz. With the basses' bells this is why the octave below 112 Hz is thin (finding 1) |
| Template plan section 8: basses -2.4..-3.6 dB at 205-250 Hz | `Double basses` `eq` bell 230 Hz -3 | Applied |

Plan sections not applied that this lens touches: section 3 timpani 84 Hz boost and strings 4.7 kHz shelf (set to 0); section 8 tutti entry spread and reverb sends by register were not checked this cycle.

## Answers to the coordinator's questions

**Bottom octave and low-mid against a reference (measured).** No Brahms audio is on disk; the third-octave spectra of four Musopen Brahms movements are (`symphony/render/critics/c00/ref_brahms{1,4}_i_musopen/metrics.json`, first movements, and `c04/ref_brahms{1,4}_ii_musopen`). The Dvorak 9/i Columbia mp3 was measured with the same script.

| | 62 Hz | 79 Hz | 99 Hz | 125 Hz | 157 | 198 | 250 | 315 | share 70-112 | share 56-112 | share 140-355 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Brahms 1/i (C minor) | -12.3 | -16.8 | -10.7 | -11.8 | -14.4 | -14.5 | -17.1 | -14.8 | -9.7 | -7.8 | -9.1 |
| Brahms 4/i | -12.7 | -13.2 | -13.5 | -11.2 | -13.0 | -14.4 | -14.9 | -14.8 | -10.4 | -8.3 | -8.2 |
| Dvorak 9/i (Columbia) | -37.8 | -24.7 | -21.4 | -13.7 | -10.4 | -12.3 | -13.8 | -12.4 | -19.7 | -19.7 | -6.0 |
| c55 master | -26.7 | -25.7 | -16.0 | -17.2 | -14.8 | -12.0 | -12.9 | -10.6 | -15.5 | -15.2 | -6.3 |

Movement I is 5-6 dB short of the Brahms recordings at 70-112 Hz (9-12 dB in the 79 Hz band), 5.5 dB short at 112-140 Hz, and 2-4 dB over them at 198-315 Hz (+4.2 at 315 Hz). It sits within 0.3 dB of the Dvorak recording at 140-355 Hz and 4 dB above it at 70-112 Hz. The low end of this mix was fitted to the Dvorak file in c05-c44 (`mix.json` `_doc`), and that file has almost no content under 100 Hz. The Brahms 62 Hz band is not used as a target: it reads -11.3 to -12.7 in four movements in three keys with the 50 Hz band 17 dB lower, so it may hold hum; the 79 and 99 Hz bands are the comparison. Second theme 184-244: 70-112 Hz share -18.6, 112-140 Hz share -24.7 dB.

**Removing the note-cut bells (simulated on the stems).** Finding 1. The celli have no static note-cut bell in `mix.json` (`eq` is empty; their only cut is the `loud_eq` 100 Hz -4 over 324-332), so nothing was simulated for them. The tuba's bell and shelf change no band by more than 0.1 dB.

**Which envelope layers balance needs.** Finding 2.

## Routine checks that pass (measured)

- Timpani: the loudest dry stem in 5 quarters (0, 1, 2, 328, 384; c54: 7). Every roll of 3 s or more is 8-26 dB under the sum of the other stems after its first quarter (bars 1-4 -10 to -18; 40-47 -8 to -15; 464-521 -10 to -20; 662-679 -11 to -19; 720-728 -14 to -17).
- Tutti group levels (K, dry): strings lead or tie in every tutti span; trumpets under Violins I by 0.6 dB at 636-644 (fff), 2.3-4.6 dB elsewhere; low brass 2-7 dB under the strings; Tam-tam leads only its fff stroke (484-492); Trombone 1 is the loudest stem in 11 quarters, of which 696-698 is the pp dolce chorale it leads.
- Dynamic mapping, K-weighted body medians of notes of 0.6 s or more on a flat mark: every track rises from p to f to ff to fff. At f: woodwinds -36.4 to -40.7, horns -36.4 to -38.2, trombones -31.7 to -34.8, tuba -35.0, strings -33.4 to -33.9 (basses -40.8). At p: clarinets -42.7 / -45.7, Violins II -45.7, Violas -43.6, celli -43.7, basses -44.9, Horn 1 -45.8, Horn 2 -43.0, Horns 3 and 4 -48.9 / -49.1 (finding 4).
- Melody margins against the sum of all other dry stems per quarter: Violins I 56-88 median +1.6, lower quartile +0.8; celli 184-216 +2.4 / +0.4; Violas and celli 584-620 +3.2 / +1.5.

## Findings

### 1. The three bells on the Double basses overlap into one 6-7 dB cut from B flat 1 to E2, the octave of this movement's tonic (measured on the stems; the filter shape is modelled)

Where. `build/mix.json` "Double basses": `eq` `bell2` 87.3 Hz -10 dB / 0.15 oct (c24, for F2) and `mute_eq` 61.7 Hz -6 / 0.25 oct and 73.4 Hz -5 / 0.25 oct (c27, for B1 and D2; static). The basses supply 46 % of the master's 70-112 Hz energy, the timpani 29 %, the celli 12 %.

Evidence.
- Summed response of the three bells at the basses' fundamentals: B flat 1 -5.0, B1 -7.3, **C2 -6.3**, D flat 2 -6.2, D2 -7.2, **E flat 2 -6.1**, E2 -6.8, F2 -11.4, G flat 2 -5.4, G2 -2.5 dB. The bells were set for three notes of v221; they now cut every note the basses play between 58 and 92 Hz.
- What the basses play in v621 (seconds): C2 84, G1 57, E flat 2 36, A flat 1 26, F2 24, D2 22, D flat 2 19, G2 18, B flat 1 16. C2 is the most played note and lies between the two `mute_eq` bells.
- Fundamental against the same note's partials above 3.5 x f0 (median per pitch, on the c55 stem → with the bells removed): C2 +1.0 → +7.5; E flat 2 -0.2 → +6.0; D2 +2.1 → +9.2; B1 +3.0 → +10.1; E2 -2.2 → +4.9; D flat 2 +9.1 → +15.4; F2 +3.4 → +14.7; untouched neighbours G2 +13.4, A flat 2 +16.0. With the bells, C2 and E flat 2 have 12-16 dB less fundamental than G2 and A flat 2; without them the F2 (+14.7) is no higher than G2 or A flat 2, so a 10 dB cut on it is not supported by the v621 stem. A small cut is kept because F2 stands 7-10 dB over E2 and E flat 2.
- Simulation, master bands 79 / 99 Hz and shares 70-112 / 140-355 Hz, whole movement: now -25.7 / -16.0, -15.5 / -6.3. (A) all three bells removed: -19.5 / -14.5, -13.3 / -6.4; master K level per bar +2.2 dB in bar 84 (the basses' G1 alone), +1.2 in bar 111, +1.1 in bar 91 (held F2), under 0.9 elsewhere; sample peak 0.917 → 0.948. (B) `mute_eq` removed and the F2 bell at -4 dB: **-21.1 / -14.9, -14.0 / -6.3**; bar 84 +1.6 dB, every other bar +0.6 or less; peak 0.940; integrated K level +0.04 dB. By passage (70-112 Hz share, now → B): bars 1-14 -14.5 → -10.9; theme 56-88 -15.4 → -13.0; second theme 184-244 -18.6 → -15.7; 584-636 -14.9 → -12.5; ff 104-128 -19.1 → -17.4; coda 680-728 -21.0 → -19.8. The 140-355 Hz share does not move, so this is added weight, not a trade.
- Tuba: removing its 84 Hz bell and 70 Hz shelf changes no master band by more than 0.1 dB; leave it.

Fix (level only, `--mix-only`; it can be previewed on the stem with the inverse bells before any render).
- `mix.json` "Double basses": delete `mute_eq` (61.7 and 73.4 Hz bells); `eq` `bell2` 87.3 Hz `db` -10 → **-4** (keep 0.15 oct). Leave the `loud_eq` rows (80 Hz shelf -5, 98 Hz -4 over the tutti spans): they guard the loud bars, and the gain here is in the soft and medium passages.
- Optional second step, to be judged by ear on an A/B clip because it reaches the template's own timpani EQ only half way: `family_eqs.timpani` add bell 84 Hz +4 dB / 1.0 oct (template: +8.6). Simulated with B: 70-112 Hz share -13.3, 99 Hz band -14.1, peak unchanged. Check rule 5 on the rolls afterwards (their margin today is 8 dB or more).
- Not recommended: a celli cut at 290 Hz (-3 dB, 1 oct) was simulated: 140-355 Hz share -6.3 → -6.5 for a loss of 0.9-1.5 dB of celli level in 184-216, 520-536 and 584-620. As in the Adagio, the low-mid weight is in many stems (celli 20 %, violas 12 %, tuba 8 %, Clarinet 1 7 % of 223-355 Hz), not in an EQ.

Acceptance: master 79 Hz band at -21.5 dB or higher and 70-112 Hz share at -14.2 or higher over the whole movement; no bar's K level up by more than 1.8 dB; `cbpitch.py` on the new basses stem: C2 and E flat 2 fundamentals within 8 dB of G2 on that measure, F2 not above G2. The ReaEQ bell shape is modelled, not measured: if the range render of bars 1-14 shows less than +2.5 dB at 70-112 Hz, the real bells are narrower than the model and the change is smaller than stated, not harmful.

Judgement: spectra, pitch table and simulation measured; filter shape modelled; that more weight at 60-110 Hz answers "mushy" is inferred (the same inference as Adagio c54 critic B finding 2).

### 2. Balance does not depend on the per-note layers of the volume envelope; half of the measured passages are less even with them (measured)

Method. Each track's `vol_db` is split into a slow part (running median over 1.2 s: roles, hairpin gain, dynamic trims, divisi cuts, timpani settle, final fade pass through it) and the per-note remainder (everything written as an `("env", ...)` item in `score_to_parts.py`: accent swells and fitted accents, accent bodies, marcato shapes, note trims, row trims, pickup lifts, steady-line level steps and body lifts, join notches, re-bow / loop / early fills, plus `("note", ...)` unison boosts). The remainder is subtracted in dB from the stem's frame levels. "Step" is the median absolute level difference between consecutive note fronts (first 0.35 s), the coordinator's measure.

Evidence.
- The remainder is 0.0 dB in the median on every track, over 3 dB for 4-10 % of the sounding time on strings, Oboe 1 and Clarinet 1, and up to 12-15 dB on single notes.
- Net level of each track over all its notes, with minus without the remainder: Violins I +0.01, Violins II -0.02, Violas -0.14, celli +0.12, basses +0.29, Flute 1 +0.02, Oboe 1 +0.19, Clarinet 1 +0.32, Horn 1 +0.26, Trumpet 1 +0.29, Trombone 1 +0.23, Tuba +0.18, Timpani +1.17 dB. Per passage the change is 0.0-0.8 dB (largest: Clarinet 1 520-536 -0.8, Oboe 1 88-104 -0.7, Cor anglais bars 1-14 -1.2).
- Melody margins with → without the melody's remainder (median / lower quartile): Violins I 56-88 +1.6 / +0.8 → +2.0 / +0.2; celli 184-216 +2.4 / +0.4 → +2.5 / 0.0; Oboe 1 88-104 -11.1 → -11.2; Clarinet 1 520-536 -9.2 → -9.5; Violins I 536-552 -5.4 → -5.2; Violas and celli 584-620 +3.2 / +1.5 → +4.1 / +2.1. No section's place in the balance rests on these layers.
- Step with / without / capped at +-3 dB with nothing on notes of 0.5 qn or less:

| passage | with | without | capped | long notes, front minus tail with / without |
|---|---|---|---|---|
| Violins I 56-90 | 1.63 | 1.22 | 1.25 | 0.7 / 5.1 (7 notes) |
| Violins I 104-128 | 1.61 | 1.77 | 1.57 | 0.5 / 4.1 |
| Violins I 304-384 | 3.06 | 2.44 | 2.29 | -1.3 / -1.3 |
| Violins I 536-576 | 1.78 | 1.72 | 1.42 | 0.3 / 2.3 |
| Violins II 104-128 | 2.76 | 2.09 | 2.07 | 0.2 / 0.9 |
| Violoncellos 184-244 | 2.05 | 2.17 | 1.93 | 0.2 / -1.8 |
| Violoncellos 520-536 | 2.43 | 1.89 | 1.74 | 1.5 / 1.6 |
| Violas 584-636 | 1.69 | 1.68 | 1.68 | |
| Oboe 1 88-104 | 3.21 | 2.36 | 1.89 | |
| Clarinet 1 520-536 | 2.88 | 1.63 | 2.85 | |
| Horn 1 400-430 | 2.01 | 1.41 | 1.68 | |
| Trumpet 1 456-496 | 1.91 | 1.24 | 1.91 | |
| Double basses 56-128 | 2.19 | 2.78 | 2.95 | |

- Which entries sit on the notes with a mean remainder of 2 dB or more, or a swing of 6 dB or more: Violins I 114 notes (`steady_line` 87, `steady_body` 44, `retongue_leads` 10, `pickup_lift` 9, `acc_fitted` 9, `row_trimmed` 8); Violoncellos 110 (`rebows` 26, `str_rep_dips` 13, `steady_line` 12, 37 with no listed key); Oboe 1 44 (`acc_fitted` 16, `acc_trimmed` 13, `accent_body` 12); Clarinet 1 50 (`acc_fitted` 19, `retongue_leads` 14, `accent_body` 10, `acc_trimmed` 8); Horn 1 16.

Verdict for balance.
- Needed, keep in the envelope: `gain_db`, `soft_trim_db` / `dyn_trim_db`, role spans (`roles.json`), hairpin gain (`hpgain`), divisi and chord cuts, timpani roll settle, final fade, `ride_trims`. These are the manual's "loudness level relative to other instruments".
- Per-note, keep because they cure a measured fault: `steady_body` and the tail rows on the Sus Marc LITE theme (without them the long notes fall 4-5 dB from front to tail again, c54's fault); re-bow and loop fills on held notes (BRIEF item 7); the basses' note and pitch trims (step 2.19 against 2.78 without); the plucked note trims (harp, pizzicato), which CC11 cannot reach.
- Per-note, no balance benefit and a worse step, remove or move to CC11 / velocity: fitted accents, accent trims and accent bodies on the woodwinds (`build/accent_fits.json`, `accent_bodies.json` for Oboe 1 and Clarinet 1: step 3.21 → 2.36 and 2.88 → 1.63 without them); the same on Horn 1 400-430 and Trumpet 1 456-496; `steady_levels54.json` front steps on Violins II 104-128 and celli 520-536 (2.76 → 2.09, 2.43 → 1.89); the per-note rows of Violins I 304-384 (3.06 → 2.44).
- The +-3 dB cap with nothing on notes of an eighth or shorter is as good as removal or better in 9 of 13 passages and keeps the body lifts; it fails on Clarinet 1 520-536 and Trumpet 1 456-496, where the harm is in steps under 3 dB (fitted accents), and on the basses, which need their full trims.

Fix. In the c56 range test use three states per passage: all per-note items off except `steady_body` / tail rows and re-bow fills; capped (+-3 dB, none on notes of 0.5 qn or less, basses and plucked trims exempt); current. Adopt per passage the state with the lowest step whose long-note front minus tail stays under 4 dB and whose melody margin (table above) does not fall by more than 0.5 dB. Where an accent is printed, give it as +6 to +10 CC11 units over the first 0.25 s of the note on the wind KS Masters rather than as a volume swell (verify the 2-5 kHz front against the body, BRIEF item 8, stays under 7 dB).

Judgement: measured on the c55 stems by subtraction; a sample responds linearly to the volume envelope, so the subtraction is exact for level; how the envelope will look in REAPER after the change was not measured.

### 3. The 112-140 Hz band is 5.5 dB under the Brahms recordings and 3.5 dB under the Dvorak; in the second theme it is 24.7 dB under the total (measured)

Where. Whole movement, worst in 184-244. Sources of this band: basses 28 %, timpani 27 %, celli 20 %, tuba 10 %. The celli's 125 Hz +3 dB and 170 Hz +3 dB bells and the basses' 160 / 180 Hz bells have played only over the loud spans since c44, a decision taken against the Dvorak file.

Evidence: 125 Hz band -17.2 dB (Brahms -11.2 / -11.8, Dvorak -13.7). Simulated with finding 1's change: a static bell 120 Hz +3 dB / 0.8 oct on the celli and the basses gives 125 Hz band -15.7, 99 Hz -14.1, 70-112 Hz share -13.2, 140-355 Hz share -6.4 (unchanged), second theme 112-140 Hz -24.7 → -22.5, celli K level +0.1 to +0.8 dB per passage, peak 0.908.

Fix: `mix.json` "Violoncellos" and "Double basses" `eq`: add `{"band": "bell", "hz": 120, "db": 3, "bw_oct": 0.8}`; in the celli `loud_eq` row that holds the 125 Hz +3 bell set that band to 0 so the loud spans do not get it twice. Rank this after finding 1 and listen to it separately; it moves the celli line by under 1 dB.

Judgement: measured and simulated; the benefit is inferred.

### 4. Horns 3 and 4 at p are 3-6 dB under the woodwinds and inner strings at the same mark (measured, low priority)

Evidence: K-weighted body medians at p: Horn 3 -48.9 (11 notes), Horn 4 -49.1 (10), Horn 1 -45.8, Horn 2 -43.0, Clarinet 1 -42.7, Clarinet 2 -45.7, Violins II -45.7, Violas -43.6. At f the four horns are within 1.8 dB of each other (-36.4 to -38.2). Rimsky-Korsakov's rule of thumb puts one horn at piano level with one woodwind or one string group.

Fix: `mix.json` Horn 3 and Horn 4 `soft_trim_db` "p" +2.0 dB each (pp unchanged: -49.9 / -51.3 already sits 1-2 dB under p). Check first what the 21 notes are: if they are held pedals under a solo, leave them.

Judgement: measured; the need is inferred.

Do not touch: the timpani levels and roll settle; trumpet and trombone `dyn_trim_db`; the theme's `steady_body` body lifts and tail rows (front minus tail 0.7 dB on Violins I 56-90); the role spans and soft trims (they are the balance); the basses' `loud_eq` rows and the 230 Hz bell; the tuba's EQ; no celli low-mid cut.
