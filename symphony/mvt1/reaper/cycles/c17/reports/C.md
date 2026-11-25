# Cycle 17, critic C: blend and space (review of the c16 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets (trumpets, cymbals and, since c13, the 2FH a2 horns), and low-end build-up against several references.

## Method

I measured the stem-fixed c16 render (`cycles/c16/render/`). Score qn maps to file time through the tempo map in `cycles/c16/rendered_build/parts.json`. I also read the Opus states in `jobs/*.b64` and the layer groups in `2FH Sus MAX.oib`, `1FH Sus MAX.oib` and `18in Zildjian Sus Cymbal Cres.oib`.

References:
- the stored stereo, brightness and band metrics of five recordings: Brahms 1/i, 4/i, 1/ii, 4/ii (Musopen, lossless) and Dvořák 9/i (lossy MP3), in `symphony/render/critics/c00|c04/ref_*/metrics.json`;
- the decoded Dvořák file, run through the same scripts;
- the movement II c26 master.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c17-C/`. The c13-C battery is pointed at c16, plus these new scripts:
- tone by pitch and dynamic: `pitchbright.py`, `a2match.py`, `bnd.py`, `hfenv.py`, `hfharm.py`, `tshare.py`;
- EQ and width simulations: `eqlib.py`, `a2grid.py`, `a2sim.py`, `tptsim.py`, `sidesimhi.py`, `sidesim3.py`, `sidesim4.py`, `percseat.py`;
- band shares, band balance and band stereo per stem: `stemband.py`, `histereo.py`, `balband.py`, `passlow.py`;
- layer groups: `grp3.py`, `grp4.py`, `zones.py`;
- other checks: `topband.py`, `a2depth.py`.

Brightness is band power relative to the same stem's 500 Hz-2 kHz power, measured on the note body (+0.1/0.12 s to at most +1.0 s).

## Checked and fine (measured)

**Room.**
- All 33 states share the true-stereo hall (fx 0.19, wet 2.0, pre-fader sends). Close and Main are loaded, with the group mic levels in `mix.json`.
- Horns a2 has the same mics (Close 0.5 / Main 1.0) and send (0.5) as the 1FH horns.
- Release drops at 0.3 / 0.6 / 1.0 s after the cutoffs:

  | cutoff | c16 | c12 |
  |---|---|---|
  | bar 170 | 14.1 / 22.3 / 33.0 dB | 13.4 / 21.8 / 32.3 dB |
  | bar 33 | 13.0 / 16.9 / 21.1 dB | |

**Depth of the a2 track.** L/R correlation (300 Hz-1 kHz / 1-4 kHz) in the four a2 windows:

| | Horns a2 | Horns 3-4 |
|---|---|---|
| 300 Hz-1 kHz | 0.51-0.68 | 0.42-0.92 |
| 1-4 kHz | 0.76-0.83 | 0.71-0.91 |

The a2 track is not drier than the solo horns. The larger release drop in `depth2.py` (9.1 against 4.8-8.0 dB) rests on 6 notes and is not confirmed.

**Image.**

| | c16 | c12 | references |
|---|---|---|---|
| correlation | 0.521 | 0.528 | 0.49-0.55 |
| side/mid | -5.0 dB | -5.1 dB | -4.7..-5.4 dB |
| pan spread | 0.354 | | 0.314-0.347 |
| below 250 Hz | 0.530 | 0.617 | 0.54-0.62 |

- Below 120 Hz the correlation is 0.74 / 0.67 at 20-60 / 60-120 Hz (c12 0.82 / 0.78). The c13 Vc/Cb side-shelf removal holds.
- Band balance R-L over the movement, against Dvořák:
  - 60-250 Hz: +3.8 dB (Dvořák +3.3);
  - 2-4 kHz: -1.9 dB (Dvořák -3.7).
  - In the fff tutti (bars 122-124, 160-170), 2-8 kHz moves to between -1 and +1.5 dB R-L, because the trombones on the right carry 23% of the master's 4-8 kHz. This is small.

**Low end.**
- 2 s windows, 63-200 Hz re 500 Hz-2 kHz:

  | | loud 30% | loud 10% |
  |---|---|---|
  | c16 | -5.5 | -6.4 |
  | c12 | -6.4 | -8.0 |
  | Dvořák | -5.0 | -5.7 |

- The loud-frame centroid is 931 Hz (c12 1016; references 782-870).
- The c13 #1 target is met. Bars 160-162, 63-250 Hz re 500 Hz-2 kHz: about -7.0 dB (63-125 Hz -9.6, 125-250 Hz -10.4), against the -7.6 target. Bars 167-170: 63-125 Hz -15.9, 125-250 Hz -7.5.
- The 125-250 Hz band at bars 160-162 is still the lowest of the loud passages (others -4.9..-7.5 dB). The cause is the voicing: celli on the tune at C4-Ab4, and the bass on G1/Ab1, with the basses 47% and the tuba 24% of that band. I propose no change.
- Band shares against the target: 20-100 Hz -13.45 dB (target -14.5..-12.5), 100-250 Hz -8.6 dB (Brahms -8.75/-7.55).

**Item 7 on the master** (100-300 Hz / centroid autocorrelation at 3.95 s):

| passage | 100-300 Hz | centroid |
|---|---|---|
| opening roll | -0.04 | -0.09 |
| bars 12-14 | -0.19 | -0.13 |
| bars 117-121 | +0.05 | -0.06 |
| bars 122-126 | -0.34 | -0.23 |
| coda 175-180 | -0.05 | +0.04 |
| final chord | -0.34 | -0.03 |
| control | +0.33 | -0.05 |

All passages are at or under the control.

**Item 8.**
- Brass 2-5 kHz, first 80 ms minus body, median per track: Tpt1 -2.5, Tpt2 -10.7, Tbn1 -7.6, BTbn -7.7, Hn1 -6.4, Horns a2 -3.3 dB.
- Exposed exceptions: Tpt1 284/676 (+5.8 / +3.7, stem 6 dB under the master), as in c13.
- Clarinet 1 at 414 reads +8.1 on the stem. On the master the 2-5 kHz front is only about +1.5 dB over the body, and the stem's body swings 10 dB with vibrato. This is not a harsh attack.

**Crash and tam-tam.** Unchanged from c13:
- crash 4-12 kHz 3 dB under the master at the hit, 7 dB under at +1 s;
- tam-tam 4-12 kHz within 4 dB of the master at +0.5-1 s.

## 1. The a2 horns (2FH) are 5-15 dB brighter than the 1FH horns at the same pitch and CC1, so at f and louder the horn section plays in two tone colours (measured; the fix is simulated)

**Where.** Horns a2 against Horns 3-4 (and Horn 1/2 outside the windows), at:
- bars 41-42 (qn 163-165.5);
- letter G, bars 117-121 (qn 464-480.5);
- the climax, bars 158-161 (qn 628-643.75);
- the coda theme, bars 167-170 (qn 664.5-676.5).

These are the a2 windows where CC1 is 108-120.

**Evidence (measured).**
- Matched notes (`a2match.py`): each a2 note against the 1FH horn notes within 2 semitones and 8 CC1, third-octave re 500 Hz-2 kHz, median a2 minus 1FH:

  | CC1 | notes | 1.6-2.5 kHz | 3.2-5 kHz | 6.3-12.7 kHz | above 5 kHz |
  |---|---|---|---|---|---|
  | 100-127 | 35 | +5.8 / +5.1 / +7.2 dB | +7.8 / +8.6 / +9.4 dB | +11.2 / +7.6 / +11.3 / +15.0 dB | |
  | 80-100 | 27 | +3..+4 dB (1.25-4 kHz) | | | about 0 |

- The same note at the same time and the same CC1 (`bnd.py`, 2-5 kHz re 500 Hz-2 kHz):

  | qn | a2 | 1FH horn |
  |---|---|---|
  | 464 | G3 -6.9 | Horn 4 G3 -21.8 (both CC1 108) |
  | 642 | D4 -6.6 | Horn 3 G4 -15.5 (CC1 120) |
  | 637 | Ab4 -9.1 | Horn 3 C5 -27.4 |
  | 668 | C4 -9.2 | Horn 3 C4 -25.6 (CC1 86 there) |

  5-10 kHz is 10-25 dB apart in the same pairs.
- The a2 G3 at ff (-6.9) is as bright as the trombones' G3 at ff (Tbn1 -6.5).
- Shares of the master's 2-5 kHz at letter G: a2 7.2%, Horn 3 1.0%, Horn 4 under 0.9%. In the coda theme the a2 track has 15.9%.
- The layer tables are not the cause. 2FH and 1FH crossfade the same four layers at nearly the same CC1 points (f layer full at 84 / 81, ff at 117 / 117). The 2FH ff layer adds a CC1-driven lowpass that is fully open only at CC1 124. The difference is in the recorded samples.

**As heard (inferred).** In every loud horn chord, the two players on the a2 line sound brassy and forward, close to trombone colour, while Horns 3-4 underneath stay round and dark. The section does not blend into one horn sound. At each window edge (464, 480.5, 643.75, 676.5) the horn line changes colour between neighbouring notes.

**Fix** (`build/mix.json`, "Horns a2"; ReaEQ only, no Opus change, `--mix-only` on track 33):
- Static `eq`: add `{"band": "highshelf", "hz": 1250, "db": -3}` (keep the 40 Hz high-pass). This covers the mf/f windows (272.5-314.5, 381.5-404.5).
- `loud_eq`: one spec with points `[[162.9,0],[163.0,1],[165.5,1],[165.7,0],[463.9,0],[464.0,1],[480.5,1],[480.7,0],[627.9,0],[628.0,1],[643.75,1],[644.0,0],[664.4,0],[664.5,1],[676.5,1],[676.7,0]]` and bands `[{"band": "highshelf", "hz": 1600, "db": -8}]`.

Simulated on the stem with RBJ shelves (`a2grid.py`, `a2sim.py`; ReaEQ's shelf slope may differ, so measure on the render):
- the a2 residual against 1FH at CC1 ≥ 100 goes to -2.6..+1.8 dB from 1.25 to 10 kHz, and to -1.4..+3.2 dB at mf/f (except -6 dB at 8 kHz);
- a2 2-5 kHz re 500 Hz-2 kHz in the loud windows goes from -8.5..-10.1 to -17..-18.6, against -16..-18 for Horns 3-4 there;
- the a2 K-weighted level falls 1.4-1.9 dB in the loud windows and 0.3 dB in the mf windows.

Put the level back so the c16 horn balance holds: `roles.json` "Horns a2" `+1.7` over each loud window (ramp 0.25 qn), as a stem fix after the render if needed. The accents on the track keep their level shape. Re-run `fit_accents.py` on it afterwards, under the existing rule.

**Targets:**
- a2 minus matched 1FH within ±3 dB from 1.6 to 6.3 kHz at CC1 ≥ 100;
- a2 K-level per loud window within 0.5 dB of c16;
- master 2-5 kHz re 500 Hz-2 kHz in the loud windows within 0.5 dB of c16 (it falls about 0.3 dB in the simulation).

## 2. Trumpet 1's G5 and A-flat5 at the climax carry a 8-16 kHz band 15-25 dB brighter than its other notes. For 2.5 s after the crash, one trumpet makes 75% of the master's top octave (measured; the fix is simulated)

**Where.** Trumpet 1:
- G5 at qn 634 (bar 159, beat 3; CC1 115-120);
- Ab5 at qn 637-639.5 (bar 160, the fff largamente top note, CC1 120);
- G5 at 639.5.

The F5s at 633 and 640 and the C5 at 636 are not affected.

**Evidence (measured).**
- 8-16 kHz re the note's own 500 Hz-2 kHz at CC1 ≥ 95, per pitch (`pitchbright.py`):

  | pitch | 8-16 kHz | 5-8 kHz |
  |---|---|---|
  | Ab5 | -12.8 | -13.6 |
  | G5 | -21.2 | -13.7 |
  | G4 | -27.7 | -18.8 |
  | every other Trumpet 1 pitch Ab4-F5 | -36..-49 | -23..-35 |

  Trumpets 2 and 3 are at -30..-54 at 8-16 kHz.
- It is harmonic, not noise: on Ab5, h10-h13 (8.3-10.8 kHz) are at -19..-34 dB re 500 Hz-2 kHz, 43-60 dB over the gaps. The F5 one beat later, at the same CC1 120, has h10-h12 at -39..-44 (`hfharm.py`). It is a pitch zone of the 1TP samples.
- Trumpet 1 share of the master's 8-16 kHz (`tshare.py`): 75% on the Ab5 and 57% on the G5. Over the whole movement Trumpet 1 makes 32.5% of the master's 8-16 kHz, more than the crash (16%).
- The stem's L/R correlation at 8-16 kHz is 0.97, so the top octave is a point source near the centre.
- Master 8-16 kHz re 500 Hz-2 kHz (`topband.py`):
  - 637-639.5: -24.6 dB, against Dvořák's loudest 5% of 1 s windows (median -30.6, max -24.3);
  - 640-642: -32.0 dB.
  - The master's top therefore drops 7.4 dB in one beat, when the trumpet steps from G5 to F5, while the crash ring should be decaying smoothly. The crash itself has only 16% of that band at 637-639.

**As heard (inferred).** At the main climax the first trumpet's top A-flat has a fizzy edge that stands out of the tutti and covers the cymbal ring. The trumpet's tone then turns dull on the next note.

**Fix** (`build/mix.json`, "Trumpet 1"; ReaEQ only, `--mix-only`):
- Add `"loud_eq": [{"points": [[633.8,0],[633.9,1],[639.95,1],[640.05,0]], "bands": [{"band": "highshelf", "hz": 5000, "db": -14}]}]`.
- The G5's moved onset is about 633.9. The F5 at 640 must be outside the window.

Simulated (`tptsim.py`):
- Ab5 8-16 / 5-8 kHz -13.9 / -14.4 -> -26.3 / -23.9 dB;
- G5 at 634 -23.0 -> -35.8 dB;
- master 8-16 kHz at 637-639.5 -24.5 -> -29.6 dB (step to 640-642: 2.4 dB instead of 7.5);
- Trumpet 1 share of the top octave 74% -> 14%;
- Trumpet 1 K-level -0.7 / -0.9 dB at 634 / 637-639.5. That is level-only, and the B/climax margins can absorb it or a +0.8 role can restore it.

**Targets:**
- Ab5 and G5 8-16 kHz re their 500 Hz-2 kHz within 6 dB of Trumpet 1's G4/C5 at the same CC1 (-28..-36);
- master 8-16 kHz at 637-639.5 between -31 and -28 dB;
- no master top-octave step over 3 dB at 639.5-640;
- climax order 160 > 122 > 169 and limiter unchanged within 0.2 dB.

## 3. The master's top octave is narrower than every reference, because the brass and cymbal stems are nearly mono above 4 kHz (symptom measured; the mechanism is inferred; the fix is simulated)

**Where.** The whole movement, 4-16 kHz; loudest in the brass tutti and at the cymbals (bars 122-126, 159-162).

**Evidence (measured).**
- Master L/R correlation above 4 kHz is 0.590, against 0.378 / 0.480 / 0.525 / 0.378 / 0.465 for Brahms 1/i, 4/i, Dvořák, Brahms 1/ii, 4/ii. It has risen since c12 (0.527).
- Per band:

  | | 4-8 kHz | 8-16 kHz |
  |---|---|---|
  | c16 | 0.58 | 0.77 |
  | c12 | 0.52 | 0.73 |
  | Dvořák | 0.42 | 0.31 |

  The 250 Hz-4 kHz bands are within the references (0.50-0.57).
- Stem correlation at 8-16 kHz (`histereo.py`): Trumpet 1 0.97, Trombone 1 0.93, Horns a2 0.94, Trombone 2 0.92, crash 0.89, suspended cymbal 0.89, bass trombone 0.88. Violins I is 0.42 and Violins II 0.68.
- The high-band pan spread (0.394) is wider than the references. So the top is made of panned point sources, not diffuse sound.

**Mechanism (inferred).**
- The shared hall's high cut is 5.5 kHz, so above about 5 kHz little decorrelated reverb return is left.
- The brass (width 0.3) and percussion (width 0.4) mic pairs are narrowed to near-coherent signals.
- The c13-c16 changes added a coherent bright source (the a2 track, 0.94) and took 2-5 kHz out of the decorrelated violins (the c16 2.5 kHz shelf, the c15 bell removal). That fits the rise from 0.527.

**As heard (inferred).** On headphones the cymbals and the brass edge sit as narrow spots inside the head, without the spread of air a hall gives them. Cymbals and the tam-tam are the largest radiators on stage and should sound the widest at the top.

**Fix.**
- Finding 2 alone: >4 kHz 0.590 -> 0.580, 8-16 kHz 0.76 -> 0.69 (simulated).
- Then `build/mix.json` "groups" "perc" width 0.4 -> 0.7 (Crash cymbals, Suspended cymbal, Tam-tam). This is an Opus pan change on three percussion instances, which hold under 0.01 GB each (c14).
- To keep the seats, lower each seat by about 0.08 (crash 0.2 -> 0.12, suspended cymbal 0.3 -> 0.22, tam-tam 0.2 -> 0.12). The widening moved the simulated R-L balance +1.0..+1.8 dB (`percseat.py`).
- Simulated (side × 1.75, plus finding 2, `sidesim4.py`):
  - >4 kHz 0.590 -> 0.550;
  - 8-16 kHz 0.76 -> 0.63;
  - 4-8 kHz 0.58 -> 0.55;
  - 1-2 / 2-4 kHz 0.564 / 0.507 -> 0.556 / 0.492;
  - crash and tam-tam stem correlation 0.81 -> 0.49.
- Side boosts on the brass are not proposed. They move each panned brass stem further out instead of decorrelating it: brass side × 1.4 pulled 1-2 kHz to 0.47.
- Raising the hall high cut (5.5 -> 8 kHz) would act on the cause, but it is an Opus state change on all 33 tracks and needs refits. Leave it unless this cycle's result falls short.

**Targets:**
- master >4 kHz correlation ≤ 0.555 and 8-16 kHz ≤ 0.65;
- 1-4 kHz within 0.02 of c16;
- percussion stem R-L within 1 dB of c16 (crash +2.5, suspended cymbal +3.5, tam-tam +2.1 dB);
- crash/tam-tam levels within 0.5 dB.

## Notes (no change proposed)

- **Suspended-cymbal roll, bar 159** (measured, unchanged since c13).
  - The stem is 33 dB under the master at qn 634 (1.06 s before the crash) and 16 dB under at 4-12 kHz at qn 635. The printed pp start and most of the crescendo are still inaudible.
  - The patch has p (vel 1-89) and f (vel 90-127) takes for each of keys 60/62/64/65, in Chk and LtRg groups. Only the f takes have been tried, and every f take swells only in its last second (c13 key 65 test).
  - Whether the p takes start earlier is unknown and would need a render test. I am not ranking it above findings 1-3.
- **Trumpet 1 G4** (qn 124, 125, 324.5, 564) is also bright (8-16 kHz -27.7), but the master's top there is normal (-37..-43 re 500 Hz-2 kHz). Leave it.

Do not touch:
- the shared true-stereo hall (fx 0.19, wet 2.0, 5.5 kHz high cut, pre-fader sends);
- the group mic levels and sends;
- all non-percussion seats and widths, and the side shelves (Vc/Cb off, the low brass/timpani 200 Hz -2 dB, the wind/brass 250 Hz +1.5 dB);
- the c13 bass-octave rows from 637.25 and the basses' EQ (the c13 low-end targets are met);
- `CC1_DYN_MAP` and the CC1-track trims;
- the Violins loud 2.5 kHz shelf;
- the crash patch, timing and shape;
- the tam-tam damp and roles;
- the suspended-cymbal key 64 / lead 0.25;
- the Horns a2 windows and per-window roles (finding 1 adds EQ and a level restore only);
- `ARRIVAL_WEIGHT_AT` and the 641.7 notch;
- the climax order 160 > 122 > 169;
- AUTO_REBOW rows and shapes, the re-strike plans and the breath splits (master loop autocorrelation is at or under the control everywhere).
