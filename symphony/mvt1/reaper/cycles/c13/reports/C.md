# Cycle 13, critic C: blend and space (review of the c12 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets (trumpets and cymbals), and low-end build-up against several references.

## Method

I measured the stem-fixed c12 render (`cycles/c12/render/`). Score qn maps to file time through the tempo map in `cycles/c12/rendered_build/parts.json`.

References:
- the stored third-octave, brightness, stereo and tail metrics of five recordings (Brahms 1/i, 4/i, 1/ii, 4/ii from Musopen, lossless; Dvořák 9/i, lossy MP3), in `symphony/render/critics/c00|c04/ref_*/metrics.json`;
- the Dvořák file itself, decoded and run through the same scripts, for loud-frame and soft-frame spectra and per-band stereo;
- the movement II c26 master (same library and hall).

I also read the Opus states in `jobs/*.b64`.

Scripts and output are in `/private/tmp/claude-501/mockup-loop/mvt1-c13-C/`. They are the c09-C battery pointed at c12, plus new scripts:
- spectra and image: `spec.py`, `loudcmp.py`, `tercile.py`, `share.py`, `low3.py`, `loudpitch.py`, `pan.py`, `stemimg.py`;
- low end and simulations: `barlow.py`, `harm.py`, `klev.py`, `rolesim*.py`, `climsim.py`, `tiltsim.py`, `sidesim.py`;
- percussion: `cym.py`, `cymshare.py`, `crashdec.py`, `susenv.py`;
- unisons, accents, tails and noise: `a2.py`, `acc2.py`, `accspot.py`, `cl422.py`, `tailspec2.py`, `floor.py`.

## Checked and fine (measured)

**Room.**
- All 32 states use the one shared true-stereo hall (fx 0.19, wet 2.0, pre-fader sends). Only Close and Main are loaded.
- Master release drop after cutoffs, at 0.3 / 0.6 / 1.0 s:
  - bar 170: 13.4 / 21.8 / 32.3 dB, so -20 dB at about 0.55 s;
  - bar 33: 13.3 / 17.8 / 23.4 dB.
  - The references reach -20 dB at 0.46-0.79 s.
- Delivered mp3: the quietest 1% of 100 ms windows is at -40.7 dBFS. The quietest frames show no broadband noise (4-12 kHz flatness 0.13, 4-12 kHz 33 dB under 200 Hz-2 kHz).

**Depth.** Early release drop (sustain minus +0.15-0.25 s):

| family | drop |
|---|---|
| trumpets | 7.2-9.9 dB |
| trombones | 7.9-10.9 dB |
| horns | 5.5-9.5 dB (wettest, as bells-back horns should be) |
| winds | 9.6-12.7 dB |
| Violins I | 9.2 dB |
| violas | 8.8 dB |

The c09 trumpet and flute/oboe send changes hold. The trumpets no longer sit in front of the trombones.

**Image.**

| | c12 | references |
|---|---|---|
| correlation | 0.528 | 0.49-0.55 |
| side/mid | -5.1 dB | -4.7..-5.4 dB |
| energy-weighted pan spread | 0.352 | 0.314-0.347 |

- Pan spread is 0.345 for the decoded Dvořák, which matches its stored value, so the method agrees with the stored metrics.
- Stem seats (R-L): Vln I -7.9, horns -7.1..-1.5, trumpets +2.0..+2.8, trombones/tuba +4.9..+6.3, Vc/Cb +4.6/+4.7, percussion +2.0..+3.5 dB.

**Trumpet and brass tone.**
- The f/ff trumpet and trombone bodies are harmonic up to 10 kHz: partial peaks 31-39 dB over the gaps between them, spectral flatness 0.01-0.02. So the brass top is tone, not noise.
- Loud frames against Dvořák's loud frames, each re 400-1600 Hz, are within ±1.8 dB from 1.26 to 12.7 kHz.
- The Violins I loud 3 kHz bell and the brass CC1 layers together do not make the loud tutti too bright against that reference.

**Item 7 on the master.**

| passage | 100-300 Hz autocorrelation at 3.95 s | centroid |
|---|---|---|
| opening roll | -0.03 | -0.10 |
| bars 12-14 | -0.16 | +0.10 |
| bars 117-121 | -0.07 | +0.17 |
| bars 122-126 | -0.37 | -0.43 |
| coda 175-180 | -0.14 | -0.02 |
| final chord | -0.24 | -0.02 |
| control | +0.37 | +0.09 |

- Wind, brass and timpani notes of 5.4 s or longer: all under 0.6 except Bass clarinet qn 11 (centroid +0.71) and qn 464 (100-300 Hz +0.56).
- Both windows are only 5.5-6.5 s, about 1.5 loop periods, and the qn 11 note carries a printed hairpin. I do not count them as loop pulses.

**Item 8.**
- Brass accents, 2-5 kHz in the first 80 ms minus the body, median per track: Tpt1 -3.1, Tpt2 -10.2, Tbn1 -6.3, BTbn -1.7, Hn1 -5.8 dB.
- Exposed exceptions, where the stem is within 10 dB of the master's 2-5 kHz:
  - Tpt1 at 284 (+5.5) and 676 (+4.9), with the stem 7.5 / 8.6 dB under the master;
  - Clarinet 1 at 422 (finding 4).
- The Violas 536 reading (+18.7) is the decay of the ff chord before an mf accent. It is not an attack.

## 1. The main climax (bars 160-162) and the coda tutti (bars 167-170) have the thinnest bottom of any loud passage. The mix loses low end as it gets louder, unlike all five references (measured; the fix is simulated)

**Where.** Bars 160-162 (qn 636-646) and 167-170 (qn 664-680). Tracks: Double basses, Tuba, Contrabassoon, Bass trombone.

**Evidence: how the low end changes with level (measured).**
- 2-s windows, 63-200 Hz re 500-2000 Hz (`tercile.py`):

  | | soft 30% | loud 30% | loud 10% |
  |---|---|---|---|
  | Dvořák | -8.5 | -5.0 | -5.7 |
  | c12 | -3.2 | -6.4 | -8.0 |
  | c00 | | | -8.9 |
  | mvt II c26 | | | -8.9 |

  In the recording the low end grows with level by about 3 dB. In the mockup it shrinks by about 5 dB.
- Loud-minus-soft spectral shape (the stored metric, same method as the references):
  - at 157 Hz the five references give +2.8 / +4.2 / +5.2 / -0.4 / +5.1 dB (median +4.2); c12 gives -3.4 (c08 -2.6);
  - at 79 Hz the references give a median of -0.9; c12 gives -6.2.
- The loud-frame centroid is 1016 Hz against 782-870 in the references. With the top matching (above), this comes from the missing bottom.

**Evidence: by passage (measured).**
- 63-250 Hz re 500-2 kHz (`rolesim.py`, `climsim.py`):

  | passage | 63-250 re 500-2 kHz |
  |---|---|
  | bars 82-83 | -3.3 |
  | bars 131-134 | -4.1 |
  | bars 117-120 | -4.6 |
  | bars 27-32 | -5.6 |
  | bars 159-162 | -7.8 / -8.5 |
  | bars 167-170 | -8.8 / -9.3 |

  The two passages that should weigh most are the lightest, 3-5 dB under the movement's other ff tutti.
- At the climax the celli have the tune in the tenor register: 2% of the master's 63-250 Hz. That band then comes from:
  - the basses, 49%;
  - the timpani, 19%;
  - the tuba, 13%.
- The bass is G1/Ab1 (49/52 Hz) on Cb/Tuba/Cbn (`loudpitch.py`). On Ab1 at qn 636-640 (`harm.py`, re the master's 400-1600 Hz):
  - basses h2 (104 Hz) -13.0 dB, h3/h4 -25.0/-25.4 dB;
  - tuba h1-h4 -47.7 / -20.0 / -22.4 / -19.8 dB;
  - bass trombone h1 (Ab2) -29.9 dB.
- The weak low fundamentals of the Basses KS Master on E1-B♭1 (LEARNINGS section 14) leave the octave above them to a few quiet partials.
- K-weighted at qn 636-644, re the master: basses -17.1, tuba -14.0, contrabassoon -19.6, bass trombone -11.5. The basses are 3-4 dB lower relative to the master here than in bars 117-121 and 131-134 (-14.0 / -13.1).

**Evidence: what EQ can and cannot do (measured by simulation).**
- More EQ on the brass does little. A +3 dB low shelf at 160 Hz on Tuba/BTbn/Cbn plus removing the basses' loud 98 Hz cut moved bars 159-162 by only +1.1 dB. Removing the tuba/contrabassoon 70 Hz shelf moved 20-100 Hz by 0.07 dB.
- A level lift on the bass-octave group does more (`rolesim3.py`, `rolesim4.py`):
  - +2 dB on Cb/Tuba/Cbn/BTbn over qn 636.75-646 (ramp 0.25 qn): bars 160-162 -8.7 -> -7.6 dB, K level +0.3 dB.
  - The master's top peak (1.413 at qn 636.66, the arrival) is not touched; the window's maximum becomes 1.475 (+0.4 dB).
  - Starting the lift on the downbeat (636.0) would raise that peak to 1.539 (+0.75 dB).
  - +1.5 dB over qn 664-680: bars 167-170 -8.8 -> -8.1 dB, K +0.2 dB, peak 1.114 -> 1.180.

**As heard (inferred).** The fff largamente and the coda's f/ff theme sound bright and loud but without the weight underneath that a real orchestra adds at its loudest. The climax reads as violins and brass over a thin bass line.

**Fix** (`build/roles.json`, level only, so it can be done by stem fix).
- Add, in the existing `[q0, q1, dB, ramp]` form:
  - `"Double basses"`, `"Tuba"`, `"Contrabassoon"`, `"Bass trombone"`: `[636.75, 646, 2, 0.25]` and `[664, 680, 1.5, 0.5]`.
- Start the first span after the 636.66 peak (LEARNINGS section 14, c23: start bass-octave rows at the ff arrival, not before). Do not add timpani; its +3 dB at 637-640 already exists.

**Targets** (63-250 Hz re 500-2 kHz, on the render):
- bars 160-162 -7.6 or higher; bars 167-170 -8.1 or higher;
- limiter at most 2.5 dB;
- climax order 160 > 122 > 169 kept;
- Violins I K-level still 2 dB or more over the bass trombone at qn 636-644 (now -9.3 against -11.5).

## 2. Every a2 unison plays one solo sample: two horns, two bassoons, two clarinets, two trombones and two trumpets sound as one player turned up 3 dB, in every climax (exposure measured; the audible effect is inferred)

**Where.**

| unison | notes | time | bars |
|---|---|---|---|
| Horn 1+2 | 86 | 50 s | 28, 41-42, 69-72, 78-79, 96-102, 117-121, 133, 158-161, 167-170 |
| Horn 3+4 | 18 | 13 s | 41-42, 80-82, 158-161 |
| Bassoon 1+2 | 38 | 32 s | 23-25, 32, 131-137, 157-165 |
| Clarinet 1+2 | 59 | 22 s | 69-72, 103-106, 131-134 |
| Trombone 1+2 | 31 | 20 s | 80-81, 117-121, 124, 131-134 |
| Trumpet 1+2 | 21 | 9 s | 131-132, 167-170 |

`a2.py` lists these from `parts.json` against the score events.

**What is wrong.** `find_unisons()` in `tools/score_to_parts.py` drops the second copy and gives the kept note +10·log10(2) dB (`UNI_BOOST`). That is correct for level, and it avoids the coherent doubling of one sample (LEARNINGS section 8).

In these passages, though, the brass and winds are single samples beside string sections of 10-16 players. A recorded pair has two players' small pitch and timing differences and a wider source; a boosted solo has neither. At the climaxes (bars 117-121, 158-161, 167-170) both horn pairs are solos at +3 dB.

**Evidence.**
- HO Brass Diamond has `2 French Horns/06 Keyswitch/2FH KS Master.oib`, plus `2 Trumpets` and `2 Trombones EXP` folders (measured, file listing).
- mvt II used the 2FH KS Master on its own a2 track from c18. Its gain had to be 4.6 dB higher than the solo-horn track it replaced (LEARNINGS section 8). That shows the recorded pair differs from a boosted solo in level as well as in tone.
- Memory, measured: c12 used 43 GB with 32 instances and unused rows unloaded. mvt II c24-c26 rendered 32 instances, including the 2FH track, at 44 GB with nothing compressed.
- This item has been deferred since c01 (HISTORY c01-c12).

**Fix.** A 33rd track "Horns a2" on the 2FH KS Master. Append it at the end so the stem numbers hold. Copy Horn 1's settings:
- rows Sus MAX and Leg Slur MAX only;
- `CC1_DYN_TRACKS` prefix "Horn" already covers it;
- seat -0.42, width 0.3, horn group mics and send;
- gain Horn 1's -4 dB + 4.6 - 3.0 (the dropped UNI boost), so about -2.4 dB, then set from the stems.

Route the Horn 1+2 unison notes to it. `TRACK_WINDOWS` in `score_to_parts.py` takes one window per track: extend it to a list of `(q0, q1)` windows, or route by unison group (notes that `find_unisons` would drop from Horn 2 plus their kept Horn 1 copies). Leave Horns 3+4 (18 notes) and the winds for later cycles.

**Targets:**
- Horn level in the a2 bars within 1 dB of c12 (K-weighted, per bar).
- Settled memory under 45 GB.
- Accent fits refit for the new track (fit_accents rule).
- Item 8 measured on the new track's accents (2FH has its own attack samples).

## 3. The suspended-cymbal roll into the climax is heard only in its last 0.4 s; the printed pp start and most of the crescendo of bar 159 are missing (measured; the fix needs one render test)

**Where.** Suspended cymbal, qn 632-636 (bar 159, "pp <", soft sticks, into the fff crash at qn 636). Bar 159 lasts 2.13 s in the c12 tempo map.

**Evidence (measured, `cym.py`, `cymshare.py`, `susenv.py`).**
- Stem against master:

  | | broadband | 4-12 kHz |
  |---|---|---|
  | qn 632 | -68.0 vs -23.7 dB | absent (-117) |
  | qn 633 | -58.5 vs -22.0 dB | -102 vs -40 dB |
  | qn 634 | -53.5 vs -20.2 dB | -76.5 vs -38.3 dB |
  | qn 635 | -46.1 vs -18.7 dB | -53.9 vs -34.7 dB |
  | qn 636 | -36.4 vs -19.8 dB | -39.7 vs -33.7 dB |

- Share of the master's 8-16 kHz power: 1% at 0.69 s before the crash, 19% at 0.44 s, 50% at 0.29 s.
- The key 64 take (`PERC_MAP["Suspended cymbal"]`, vel 105) rises from silence to its peak in 2.5 s. 6-16 kHz relative to the peak is -76 / -71 / -44 / -11 / -5 dB at -2 / -1.5 / -1 / -0.5 / -0.3 s, identical in c01 and c12.
- So the take's audible swell is under a second long, and its high band about half a second. The timing is right: the peak meets the crash.

**As heard (inferred).** The roll sounds like a short whoosh right before the crash. The listener does not hear a pp roll that grows through the bar, so the crescendo into the main climax loses its percussion line.

**Fix (a test, `build/score_config.py` `PERC_MAP`).**
- Try key 65, the longest of the four recorded crescendo takes (60/62/64/65, shortest first; comment at lines 47-53).
- Measure its peak time from its start on the render, then set `lead_s = peak_time - 2.13 - 0.20` (bar 159 plus the crash delay and the qn-636 caesura), so the peak still meets the crash.
- Keep `vel` 105.
- If key 65's high band also arrives only in the last second, revert to key 64. A level shape cannot help: raising the start by 15 dB leaves 6-16 kHz 55 dB under the peak at -1.5 s.

**Targets:**
- Roll 6-16 kHz within 30 dB of its peak from 1.5 s before the crash, and within 15 dB from 1.0 s.
- At least 15% of the master's 8-16 kHz from 1.0 s before the crash.
- Peak within 0.05 s of the crash onset.

## 4. Clarinet 1's accented G5s in the development (qn 414, 422; bars 104 and 106) are 5 dB over their neighbours and lift the whole mix's 2-5 kHz by 4.6 dB (measured; item 8)

**Where.** Clarinet 1, qn 414.0 and 422.0 (G5, accent; the 422 accent starts a decrescendo).

**Evidence (measured, `acc2.py`, `accspot.py`, `cl422.py`).**
- At 422:
  - 2-5 kHz first 80 ms minus body +4.5 dB, and minus the 0.25 s before +5.7 dB;
  - the clarinet is the master's main 2-5 kHz source there (stem -0.7 dB re master), and the master's 2-5 kHz jumps +4.6 dB at the onset.
- K-weighted body levels against the notes around them:
  - 422: -38.2 dB against -41.6 / -44.6 / -43.6, so +3.4..+5.4;
  - 414: -40.5 against -46.0 / -45.8, so +5.3..+5.5.
  - The rule is 2-4 dB.
- G5 is the Clarinet KS Master's hot pitch (+10 dB at flat CC11, LEARNINGS section 13). `pitch_trims.json` Clarinet 1 has "79": -3 and `note_trims.json` "422.0": -2, so the trims do not yet cover it.

**Fix** (`build/note_trims.json`, Clarinet 1; steps with the 0.1 s ramp of `NOTE_TRIM_RAMP_S`, level only): "414.0": -2 (new) and "422.0": -2 -> -4.

**Targets:** both accents +2..+4 dB over the notes on each side, and the master's 2-5 kHz front minus the 0.25 s before at most +2.5 dB at 422.

## 5. The deep bass is more mono than in the recordings: 20-120 Hz correlation 0.78-0.82 (measured; the fix is simulated)

**Where.** The whole movement, in the 20-120 Hz bands. Tracks: Violoncellos and Double basses (`side_shelf` lowshelf 200 Hz -2 dB, set in c20/c21 on mvt II).

**Evidence (measured, `stereo.py`, `sidesim.py`).** Master L/R correlation at 20-60 / 60-120 / 120-250 Hz:

| | 20-60 | 60-120 | 120-250 |
|---|---|---|---|
| c12 | 0.82 | 0.78 | 0.55 |
| Dvořák | 0.49 | 0.55 | 0.55 |
| mvt II c26 | 0.73 | 0.76 | 0.55 |

- Two Brahms recordings measured about 0.60 under 120 Hz (LEARNINGS section 12, c19).
- The broad low band (20-250 Hz, 0.617) is at the top of the references' 0.54-0.62 only because 120-250 Hz is fine.
- Simulated on the stems: removing the side-only shelf on Vc and Cb gives 0.73 / 0.69 / 0.49 (20-250 Hz 0.55); halving it to -1 dB gives 0.78 / 0.74 / 0.52.

**As heard (inferred).** On headphones the basses sit in a narrow column in the middle of the head instead of filling the hall's width. This is small next to findings 1-3.

**Fix** (`build/mix.json`): Violoncellos and Double basses `side_shelf` -2 -> 0 dB (remove it). Keep it on Tuba, Bass trombone, Contrabassoon and Timpani.

This is a linear side-channel filter, so the stem fix can apply it exactly; apply the same data in REAPER with `--mix-only` if it rebuilds `set_side_shelf`, otherwise `--midi-only` on the two tracks.

**Targets:** master correlation 0.65-0.75 at 20-60 Hz and 0.60-0.72 at 60-120 Hz, with 120-250 Hz at 0.48 or higher. Seats of Vc/Cb within 1 dB of +4.6/+4.7 R-L.

## Notes on cymbals (measured, no change proposed)

- **Crash** at qn 636. Its 8-16 kHz falls 18 dB in 1 s and 35 dB in 2 s, while 2-4 kHz holds +4..+5 dB over the hit to 1.5 s. The crash takes 87% of the master's 8-16 kHz at the hit, 18% at +0.5 s and 4% at +1 s.
  - This is the 9.4 s take's own decay. The level shape already adds +5/+6 dB after qn 638.5 and acts on all bands.
  - I found no mic or level change that would keep the high band longer.
- **Tam-tam** at 484. It blooms as a tam-tam should: 4-12 kHz 23 dB under the master at +0.1 s, 3.7 dB under at +0.5 s, and it holds 33-45% of the master's 4-8 kHz to +1 s.

## Do not touch

- The shared true-stereo hall and its settings (fx 0.19, wet 2.0, 5.5 kHz high cut, pre-fader sends).
- All seats and widths; the side-only shelves except finding 5's Vc/Cb change.
- The c09 trumpet send 0.65 and flute/oboe send 0.5 (depth now ordered).
- The woodwind, horn, trumpet, string and perc mic levels.
- `CC1_DYN_MAP` with the CC1-track trims: the brass top now matches the loud reference.
- The Violins I loud 3 kHz bell. With it the loud 2-5 kHz is within 1.8 dB of Dvořák. Removing it would move 3.15 kHz only from +1.7 to +0.9 dB (simulated).
- The crash patch, its shape and timing.
- The tam-tam damp and roles.
- The suspended-cymbal lead, unless the key 65 test replaces it.
- `UNI_BOOST` for unisons that stay on solo patches.
- The climax order 160 > 122 > 169.
- The master's 636.66 arrival peak handling (`ARRIVAL_WEIGHT_AT`, the Vln I notch).
- AUTO_REBOW rows and shapes, the re-strike plans and the breath splits (master loop autocorrelation under the control everywhere).
