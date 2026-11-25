# Cycle 9, critic C (blend and space), on the c08 render

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets, and the low end against the references. All numbers come from my own scripts on the c08 stems and master (4096-point frames, hop 2048, unless named), on `rendered_build/parts.json`'s tempo map. References: the Dvořák 9/i MP3 (converted, measured here) and the stored metrics of four lossless Musopen recordings (Brahms 1/i, 4/i, 1/ii, 4/ii: `symphony/render/critics/c00|c04/ref_*/metrics.json`). Each judgement is marked measured, simulated (a stem-level model of a change, not a render) or inferred.

## Manual notes (MANUAL-READING cycle 9 row C = the c1 C row, second reading: May 2021 HO manual PDF p.138-139, 141-142, 219-223; cycles/c01/reports/C.md re-checked; MANUAL-GAPS.md read)

| Manual (PDF page) | What it says | Where it applies here | Does c08 follow it? |
|---|---|---|---|
| p.138 | Close: presence. Mid (stage edge): "definition without the sound of close proximity". Main (5th row, Decca tree + outriggers): room reflections, "big, unified sound". Surround / Vintage: lush, no definition. | Every track. | Partly. Strings and brass: Close at the seat, Main full width (the template). Woodwinds: Close-led, Main 11-21 dB under (oboes 0.088). No Mid anywhere (MANUAL-GAPS #4, never tried). c01's note "woodwinds are the driest stems" still holds: dry-stem tail drop 19-28 dB on the winds against 12.5-13 dB on the violins (finding 5). |
| p.139 | Each mic position loads and unloads its samples. | Memory. | Yes. Only listed mics load; no Surround (the timpani's template Surround stays off, per Movement I c50 B). |
| p.141 | Channel routing (Stereo default); Stereo Double widens only a Stereo source. | All tracks. | Yes, all Stereo; Stereo Double unused. Width comes from the Opus mic pans, and that is where the image problems are: trumpets and trombones are diffuse and near the centre (L/R correlation 0.20-0.45, R-L +1.4..+3.5 dB), winds are single points (0.86-0.99) (findings 2, 5). |
| p.141-142 | Per-patch convolution reverb (preset, pre-delay, volume, Master). 5-stage envelope: "be careful when changing them". | All tracks. | The Opus reverb is off since c06 (`opus_off`); the Spaces II returns replace it. The envelope edits are the release caps (strings 150 ms at f/ff). At the tutti stops the violins' dry stems reach -20 dB in 0.10-0.23 s, the celli in 0.36-0.66 s (the G2 release trail; it carries 58-67 % of the master's 90-125 Hz in the 0.15-0.45 s after the stops at bars 2 and 6). I did not rank it: a real hall also holds the bass longest after a stop. |
| p.219 | Algoverb insert. | None. | Not used; not needed. |
| p.220 | Reverb insert: true stereo, Width, Low/High Cut, Wet/Dry. | The returns are their equivalent. | Yes in kind: Spaces II true stereo, a ReaEQ before each (HP 87-160 Hz, LP 5.6-8.5 kHz), then the M/S side shelf. |
| p.221 | IR envelope pre-processing. | Returns `set.irSetup` 2 / 0.5 / 0.5. | Yes. Final stop: RT from the -5..-25 dB slope 1.25 s, late slope (-20..-35) 1.82 s (measured; ceiling 1.5 s / 2.0 s). |
| p.222-223 | One mic for the whole piece (Main usual), several at once, or separate passes per mic. | All tracks. | Close + Main at once. No change needed. |

MANUAL-GAPS items still open in this lens: #4 (Mid on the woodwinds) and #7 (half-section divisi for the "4 soli" at 473-511). Neither is ranked: #4 needs 11 full rebuilds and has no measured gain yet, #7 needs memory.

## Coordinator checks (answers first)

**Wetness ceiling (measured: holds).** I used an independent stop detector: 7 or more tracks end within 0.12 s, nothing starts for 0.55 s, and the stop is aligned to the steepest 50 ms fall.
- The six stops (qn 5, 21, 102, 662, 814, 1114) reach -20 dB in 0.21-0.36 s, median **0.33 s**. The actor's 0.39 s came from another detector. Dan's ceiling is 0.50 s; the recordings take 0.43-0.58 s.
- The drop at +0.3 s is 17.6-19.3 dB, against 13-17 dB in the recordings.
- RT is **1.25 s** (final stop, -5..-25 dB slope). The other stops have music within 0.55 s, so their slopes cannot be fitted.
- The returns are 13.2 dB (strings), 14.6 dB (brass), 13.1 dB (winds) and 7.7 dB (percussion) under their family's dry sum.
- So c08 is drier at stops than the recordings and inside the ceiling. Nothing below raises a family return by more than about 0.4 dB in the tutti tails.

**Width (measured, and simulated per option).** I used Movement I's `width49.py` on the c08 master and on Dvořák.
- c08: correlation below 250 Hz **0.724**, 250 Hz-5 kHz 0.469, above 5 kHz 0.364; side/mid -4.74 dB.
- Dvořák: 0.560 / 0.561 / 0.365, side/mid -5.33 dB. Brahms (stored): below 250 Hz 0.54-0.62, 250 Hz-4 kHz 0.47-0.54, side/mid -4.7..-5.4.
- Per octave in the loudest 10 % of frames (31 Hz-8 kHz):
  - c08: 0.85 0.83 0.72 0.60 0.40 0.42 0.37 0.38
  - Dvořák: 0.54 0.69 0.55 0.53 0.57 0.58 0.70 0.47
- The coordinator's "side shelf -8 -> about -4 dB" **overshoots**. Simulated on the stems (the c08 side shelves replaced by the new filter on all 13 tracks and returns that carry one):

| side filter on the 13 tracks | <250 | 62-125 | 125-250 | 250-5k | side/mid |
|---|---|---|---|---|---|
| now (low shelf 400 Hz -8) | 0.724 | 0.870 | 0.666 | 0.469 | -4.74 |
| low shelf 400 Hz -6 | 0.620 | 0.806 | 0.547 | 0.461 | -4.51 |
| low shelf 400 Hz -5 | 0.552 | 0.763 | 0.471 | 0.456 | -4.37 |
| low shelf 400 Hz -4 (coordinator) | 0.474 | 0.712 | 0.384 | 0.450 | -4.20 |
| Movement I's 200 Hz -6 | 0.474 | 0.786 | 0.362 | 0.433 | -4.05 |
| **bell 180 Hz -7 dB, 1.5 oct** | **0.604** | **0.664** | **0.588** | 0.456 | -4.44 |

  Finding 3 gives the recommendation.

**Open items.**
- 125-250 Hz share: -10.6 dB in loud frames on my edges (c08's -11.3 used other edges). Finding 3's side filter gives back +0.15 dB and finding 4 touches the low end. The low-mid problem that matters is at 315 Hz (finding 1).
- 4-8 kHz: -20.9 dB in loud frames against Dvořák -21.7, so 0.8 dB over. Against lossless Brahms, the 5.7-11 kHz octave is 4-6 dB over (-24.9 against -29.3..-31.1, whole length).
  - In loud frames, brass carry 61 % of the master's 4-8 kHz (Trumpet 1 15 %, Trombone 1 13 %), the crash 14 %, violins 17 %, returns 1.0 %.
  - Simulated: brass family shelf off -0.4 dB; plus a trumpet 5 kHz -3 dB shelf -0.8; plus the string shelf off -1.1 dB at 4-8 kHz.
  - That is B's choice. I would not touch master_eq.
- Horns against Trumpet 1 in the chorale, K-weighted (BS.1770 filter, dry stems): over qn 900-928, Horn 1 +1.0, Horn 2 +0.7, Horn 3 -3.7, Horn 4 -0.7 dB re Trumpet 1. Per span:
  - 900-912: +0.3 / +1.8 / -5.8 / -0.4;
  - 920-928: +2.0 / -1.3 / -2.1 / -0.5.
  - So horns 1-2 are still level with or over Trumpet 1, short of B's 2-4 dB under. Finding 1 takes 1.3-1.7 dB (A-weighted) off the horns' low-mid if the make-up stays partial.
- Sub. p 219 and sfp 149: these are A/B's measures, but my lens changes how they can be fixed (finding 6).
- Brass accents: no change from my lens.

**Standing checks.**
- Loop pulsing (BRIEF 7): autocorrelation at 3.95 s of the 100-300 Hz level and of the centroid stays within -0.44..+0.23 on the master, the five string stems, Horn 1, Trombone 1 and Trumpet 1, over 888-936 and 1088-1112 (failure case 0.39-0.63). **None (measured).**
- Timpani rolls (BRIEF 5): the timpani is 8.3-13.7 dB under the loudest stem (200 Hz-5 kHz) in every roll span. Its share of 30-150 Hz is 2-16 %, but **22.8 % at 273-277** (c07 18.5 %). Not the loudest stem, so the rule holds. B should watch the T section.
- Percussion at 888 / 1048 / 1108:
  - The crash is 9.9-11.9 dB (A) under the master in the first 0.4 s and carries 54-64 % of 4-16 kHz.
  - The crash's -3 dB point is 36-43 ms after the beat, the bass drum's 11 ms.
  - The bass drum's dry stem falls 13 dB by +0.3 s and 23 dB by +1 s (Felt Long, key 38). A struck 36 in drum may ring longer; inferred, no reference.
- Template default not applied: the 2.3 kHz low-pass after Spaces II (EW-TEMPLATE-PLAN §9, batch 5 item 2). **I propose to reject it here, with numbers.**
  - In loud frames the returns carry 1.7 % of the master's 2-4 kHz and 1.0 % of 4-8 kHz. The tail centroids at the stops are 450-1020 Hz. The template's pre-Spaces low-pass at 5.6-8.5 kHz is already in place.
  - So the low-pass would move the master's brightness by under 0.1 dB, and the tails are already dark. Record this in LEARNINGS if the actor agrees.

## Findings, ranked by what a listener would hear

### 1. A low-mid hump at 280-355 Hz: the master's 315 Hz third-octave stands 4-7 dB over every reference. Horns and violas make it (measured; fix simulated)

**Where.** The whole piece, worst where the horns lead:
- J 135-150: +8.3 dB over its neighbours;
- R 247-270 and F 83-98: +6.5;
- P 223-234: +6.1.

Tracks: Horns 1-4 (and their R Brass hall) and violas.

**What is wrong (measured).** Third-octave shares of total energy, whole length:

| | 200 | 250 | 315 | 400 | 500 |
|---|---|---|---|---|---|
| c08 | -14.0 | -15.0 | **-8.2** | -12.6 | -11.3 |
| c05 (before the template EQ) | -12.7 | -15.8 | -9.8 | -11.9 | -9.9 |
| Dvořák | -12.4 | -14.3 | -12.3 | -9.6 | -9.8 |
| Brahms 1/i, 4/i, 1/ii, 4/ii | -14.4..-16.1 | -14.5..-17.1 | -13.8..-14.8 | -9.6..-10.2 | - |

- The mix has a +5.4 dB peak at 315 Hz over the mean of its 250 and 400 Hz bands. The references have a 1-2 dB dip there.
- 400-500 Hz is 1.5-3 dB under the references.
- Brahms 1/i is in C minor with four horns too, so the hump is not the key.
- The template EQ made it worse: c05 → c08, 315 Hz +1.6 dB and 500 Hz -1.4 dB. The brass family bell sits at 475 Hz (bw 1.92), above the hump, and cuts the 400-500 Hz band that is already low.

Who makes it:
- Shares of the master's 315 Hz band over the whole piece: Horn 3 18 %, violas 18 %, Horn 1 18 %, Horn 2 10 %, R Brass 4 %. Horns plus R Brass are 52 % in loud frames.
- Each of these stems peaks at 315 Hz over its own 250 and 400 Hz bands: horns +3.3 to +11.4 dB, R Brass +11.7, violas +4.8.
- The horns' pitches there are D4-F4 (Horn 2 35 %, Horn 3 31 % of their held time).
- Per pitch, Horn 1's C4-F4 notes are +1.8..+3.6 dB over their time-neighbours, G4 -1.2. The bulge covers a register, not one hot note.

Movement I trimmed its horns' F4 (body -4.5 dB), C5 (-5) and Horn 3's D4 (-2.5) by pitch (`symphony/mvt1/reaper-v621/build/pitch_trims.json`). The Finale has no horn pitch trims.

Audible effect (inferred): a boxy, thick middle in every horn-led tutti, the "mushy" Dan named. BRIEF's clarity note asks for exactly this: look for 200-500 Hz build-up against the references and prefer cuts there.

**Fix** (`build/mix.json`; mix-only, no Opus state change):
- `groups.horn.family_eq`: add `{"type": "bell", "hz": 315.0, "db": -5.0, "bw": 1.0}`. It goes on Horns 1-4 only, not on the trumpet / lowbrass / Tuba lists.
- `tracks.Violas.eq`: add `{"band": "bell", "hz": 315, "db": -3, "bw_oct": 1.0}`.
- Simulated on the stem band energies (horn bell also applied to R Brass as an upper bound):
  - the 315 Hz share -8.4 → -10.8 dB (stem-sum basis; about -7.9 → -10.3 on the real master);
  - 400 Hz -12.5 → -13.3, 500 Hz unchanged, 1 kHz +0.5.
- A-weighted cost: horns -1.0..-1.7 dB, violas -0.8 dB.
- `gain_db`: horns +1.0 (not the full 1.4, which also moves Horns 1-2 toward B's chorale target), violas +0.8.
- Target on the render: the 315 Hz band within 3 dB of the mean of its 250 and 400 Hz neighbours in the loud sections J, P, R, T (now +6.1..+8.3), with no section's A-weighted horn level moving more than 0.5 dB.
- If the hump is still over +3 dB, use the horn pitch trims instead of a deeper bell (Movement I's F4 early +1 / body -4.5 and D4 -2.5).

### 2. The trumpets and trombones are diffuse sources near the centre. The muted Trumpet 1 sits apart from the cor anglais it doubles (measured; fix simulated)

**Where.** Every brass passage. Most exposed: L, qn 680-696 and 712-731 (bars 171-174, 179-183), where Trumpet 1 con sord. and the cor anglais play the same p dolce line.

**What is wrong (measured).** Dry stems, 250 Hz-5 kHz, over the frames where each plays:

| | L/R correlation | R-L |
|---|---|---|
| Trumpets 1-3 | 0.20-0.33 | +1.4 / +2.2 / +2.9 dB |
| Trombones and bass trombone | 0.33-0.45 | +2.2..+3.5 dB |
| Horns | 0.60-0.64 | -2.0..-3.2 dB |
| Cor anglais | 0.93 | +4.6 dB |

- The trumpets' Close is at seat +0.31, but at 0.31 it sits about 10 dB under the full-width Main. So the trumpets come out as a wide, centred cloud, not a section on the right.
- In the doubling (qn 680-696):
  - The cor anglais is a point at R-L +4.5 dB (correlation 0.93).
  - Trumpet 1 is spread around the centre (R-L -1.3 dB, correlation 0.25).
  - Trumpet 1 has less hall: R Brass is 13.9-14.0 dB under Trumpet 1, R Winds 9.0-10.6 dB under the winds.
  - A listener hears two instruments in two places, not one doubled line (inferred).
- Batch 5 item 4 ("brass as narrow sources", EW-TEMPLATE-PLAN §9, a default) was never applied. c07-c08 deferred its pass-2 A/B for memory. A REAPER track width needs no new Opus instance, so memory is not the obstacle.

**Fix** (`tools/build_reaper.py` + `build/mix.json`; mix-only):
1. Add a mix.json key `"track_width"` (group or track, default 1.0). Write it where `D_WIDTH` is set to 1 now: line 977 in the full track build, and `w=1` in `mix_job()` (line 1123, read at line 1131), so `--mix-only` can apply it. The tracks are in pan mode 5 (stereo pan), so D_WIDTH narrows the whole post-FX signal, Main included. The post-fader sends then feed the halls from the narrowed signal.
2. Values:
   - Trumpets 1-3: `track_width` 0.5, `track_pan` +0.30 / +0.33 / +0.36 (now +0.03 / +0.06 / +0.10).
   - Trombone 1, Trombone 2, Bass trombone: `track_width` 0.6, `track_pan` +0.26 / +0.30 / +0.34.
   - Horns and tuba unchanged. Narrowing them as well (0.4-0.5) overshot in simulation: 250 Hz-5 kHz 0.617, side/mid -6.4 dB.
3. Simulated (constant-power stereo pan on the stems, stem energy kept):
   - Trumpet 1 R-L +1.4 → +4.4 dB, next to the cor anglais at +4.6;
   - trumpets' correlation 0.71-0.80, trombones 0.68-0.77;
   - master 250 Hz-5 kHz 0.469 → 0.557, above 5 kHz 0.364 → 0.511, side/mid -4.74 → -5.70 dB;
   - **with finding 3: below 250 Hz 0.618, 250 Hz-5 kHz 0.543, side/mid -5.34 dB, all inside the references.**
4. Check on the render: Trumpet 1 within 1.5 dB R-L of the cor anglais over 680-696 and 712-731; master side/mid -4.7..-5.6 dB. If the master goes over -5.6, use trumpet width 0.6.

### 3. The bass is too mono below 250 Hz. A side bell at 180 Hz matches the references per octave; the coordinator's -4 dB shelf overshoots (measured; simulated)

**Where.** Whole piece. Tracks with `side_shelf` (low shelf 400 Hz -8): celli, basses, tuba, trombones 1-2, bass trombone, contrabassoon, timpani, and the four returns. The harp has 300 Hz -8.

**What is wrong (measured).**
- Below 250 Hz the master's correlation is 0.724 (refs 0.54-0.62). The 31-62 / 62-125 Hz octaves are at 0.85 / 0.83 in loud frames, against Dvořák 0.54 / 0.69.
- Per stem below 250 Hz (loud frames), with each stem's share of the master's energy there: celli 0.78 (30 %), basses 0.69 (18 %), tuba 0.89 (9.6 %), timpani 0.82 (9.5 %).
- The shelf cuts deepest at the bottom, where the image is already more mono than the references, and least at 125-250 Hz, where the references are near 0.55.
- It also discards side energy. Removing the shelf entirely would raise the master's 125-250 Hz share by 1.9 dB.

**Fix** (`build/mix.json`; the list form of `side_shelf` already passes any band through `config_eq`; mix-only):
- On all 13 entries that now carry `[{"band": "lowshelf", "hz": 400, "db": -8}]` (12 tracks' `side_shelf` plus `returns[*].side_shelf`), and on the harp (`{"hz": 300, "db": -8}`), replace it with `[{"band": "bell", "hz": 180, "db": -7, "bw_oct": 1.5}]`.
- Simulated (RBJ shelves and bells, applied to the c08 stems' side signal as the ratio of new to old):
  - below 250 Hz 0.604;
  - 62-125 Hz 0.664, 125-250 Hz 0.588 (Dvořák 0.62-0.69 / 0.55);
  - side/mid -4.44 dB;
  - 125-250 Hz share +0.15 dB.
- If ReaEQ's bell bandwidth differs from the model: aim for below 250 Hz 0.54-0.62 and no octave below 125 Hz over 0.75, and adjust the depth (-6 to -8 dB).
- Seats should not move. The mid is untouched, so check celli and basses R-L against c08's +1.8 / +4.5 dB (below 250 Hz).

### 4. The bass under 125 Hz is 4-12 dB thinner than the lossless references; the template's 53 Hz high-pass also cuts the basses' lowest fundamentals (measured; partly simulated)

**Where.** Every forte bass line. Most exposed: the C extension notes (bars 75-76, 166, 174-183, 189; D1 and E flat 1) and the basses' G1 / A flat 1 / B flat 1, 29 % of their held time.

**What is wrong (measured).**
- Third-octave shares (whole length), mix against the four Brahms:
  - 49.6 Hz: -34.3 against -28.4..-29.9;
  - 78.7 Hz: -24.4 against -12.2..-16.8;
  - 99 Hz: -16.1 against -10.7..-13.5;
  - 125 Hz: -18.5 against -11.2..-14.4.
  - 157-250 Hz match within 1-2 dB. The references' 62.5 Hz band holds hum, so I skip it.
- The Dvořák MP3 matches the mix at 79 Hz (-24.6), but it is lossy and the kit records that it lacks 13 dB of 20-100 Hz (LEARNINGS §14).
- The basses carry 63-68 % of the master's 35-90 Hz.
- Their fundamental against harmonics 2-4, per pitch:
  - B1-F2: -1.0..-4.5 dB;
  - B flat 1 -9.5; A1 -21.0; A flat 1 -16.4; G1 -17.1; F1 -21.8;
  - E flat 1 / D1 -35.7.
- Most of that weakness is in the samples (Movement I measured E1-B flat 1 12-30 dB under, §14).
- But the Finale adds the template's string high-pass at 53 Hz (`groups.string.family_eq` and the basses' own `family_eq`). Movement I c50 uses 35 Hz on its basses ("strings_cb"). Modelled as ReaEQ's 2-pole high-pass with bw 2 oct, 53 Hz costs C1 -9.2, E1 -6.2, G1 -4.2, C2 -2.0 dB; 35 Hz costs -4.1 / -2.4 / -1.2 / -0.4 (simulated).

**Fix** (`build/mix.json` `tracks."Double basses".family_eq`; mix-only):
- `{"type": "hp", "hz": 53.0, ...}` → `"hz": 35.0`. The other string tracks keep 53 Hz.
- Simulated on the stem bands: master 50 Hz +2.3 dB, 39 Hz +1.7, 62 Hz +1.4, the 20-100 Hz share -15.25 → -14.96 dB. The loud 40-100 Hz share rises 0.25 dB.
- Check that the loud 20-100 Hz share stays under -12.5 dB (the Movement I band) and that the master's float peak stays under 1.0.
- This closes only part of the gap. The rest is the samples and the score's voicing (inferred). Do not chase it with the basses' gain, which would bring back the c21 boom.

### 5. The woodwinds are point sources with the driest tails in the orchestra: they sit in front of the strings (measured; fix inferred)

**Where.** All winds, most audible in the exposed solos and the wind-led passages (C 168-200 motive x, the bassoon solo at 456, the oboe solo at 376, the cor anglais in L).

**What is wrong (measured).**
- Dry-stem tail drop is the body (0.4-0.1 s before a phrase end) minus the level 0.15-0.25 s after it, on notes followed by 0.8 s of silence on that track:
  - flutes 20-28 dB;
  - oboes 24;
  - clarinets 23-26;
  - bassoons and contrabassoon 19-23;
  - violins 12.5-13;
  - horns 9-16;
  - trombones 13.5-17.5.
- The winds' family return is no larger than the others' (R Winds 13.1 dB under the winds' dry sum, R Strings 13.2, R Brass 14.6). So the winds keep less room overall, because their Main mic is 11-21 dB under Close (the template's woodwind layout, FINDINGS §1) while the strings and horns take their room from a full Main.
- Their images are points (correlation 0.86-0.99, width 0.05) next to diffuse strings (0.20-0.27). On a real stage the winds sit behind the strings (manual p.138 diagram) and sound further away, not nearer (inferred).

**Fix** (`build/mix.json` `tracks.*.return.db` for the eleven winds; mix-only):
- Flutes, oboes, cor anglais, clarinets, bass clarinet: R Winds send -10 → **-7 dB**.
- Bassoons and contrabassoon have no send (batch 5): leave them.
- Wetness cost: R Winds is 2-6 % of the master's tail energy at the tutti stops (+0.15..0.45 s), so +3 dB adds at most 0.4 dB there. The -20 dB median stays near 0.33 s (estimated from the measured shares).
- Target: the winds' combined (dry + R Winds) tail within 3 dB of the violins' at phrase ends, with no wind solo's 2-5 kHz presence over the strings falling more than 1 dB.
- MANUAL-GAPS #4 (Mid in place of Close on the solo winds) is the larger version of this fix. It needs full rebuilds, so it is not proposed this cycle.

### 6. Since c06 the volume envelope sits before the halls, so a fast envelope drop no longer cuts the tail. The S3 rule can be relaxed for the subito fixes (measured)

**Where.** The open subitos: sfp at bar 149 (qn 592), sub. p at bar 219 (qn 872), and every role or trim that ends with a step under a chord.

**What changed.**
- BRIEF S3 says REAPER's volume envelope acts after the hall and cuts the tail. That was true while the hall sat inside Opus.
- Since c06 the Opus reverb is off (`opus_off`). The halls are REAPER returns fed by post-fader, post-pan sends (`build_reaper.py` line 762: `I_SENDMODE` 0), and the envelope is the fader's "Volume" envelope (line 646).
- So an envelope drop now reaches the hall's input, and the hall keeps ringing at the louder level.

**Evidence (measured).**
- At qn 592, in 50 ms frames, the dry stems' sum falls from the sf (592.73, -14.2 dB) to the p (593.27, -21.7 dB): 7.5 dB in 0.27 s.
- Over the same frames the four returns fall from -31.1 to -31.4 dB.
- At 872 neither the dry sum nor the returns drop at all (-30..-31 dB across the mark). That subito is still missing, as A/B reported.

**Fix** (rule, then data):
1. In BRIEF S3 and in the actor's notes: on the template mix a sudden drop may be written in the volume envelope (roles, trims, HELD_DECRESC steps, a subito step), because the hall carries the louder level over it. CC11/CC1 remain the way to change the timbre layer.
2. For qn 592: a volume-envelope step of -8 dB at 592.6-592.7 on the 26 sfp tracks, held to the next crescendo, gives the 10 dB p under the sf that c02-c08 have not reached with CC alone.
3. For qn 872: the same kind of step, -5 dB at 871.95-872.05 on the "sub. p" tracks, with `HELD_DECRESC_CARRY` keeping it.
4. `tail_hold` (holding the envelope through rests) is now unnecessary but harmless. Leave it.

## Do not touch

- The four returns, their faders, the irSetup envelope, the register sends and the R Strings 160 Hz high-pass (tutti stops -20 dB median 0.33 s, drop at +0.3 s 17.6-19.3 dB, RT 1.25 s, late 1.82 s: drier than the recordings and inside Dan's ceiling).
- The template's pre-Spaces low-passes (returns are 1 % of the master's 4-8 kHz).
- The timpani's reduced EQ with no Surround (never the loudest stem in any roll).
- The re-bow layout (no loop pulsing in 888-936 or 1088-1112).
- The c08 family-EQ bell changes at 821 Hz / 1 kHz / 3.2 kHz.
- The crash and bass drum timing (crash -3 dB point +36..+43 ms, bass drum +11 ms).
- The cor anglais and Trumpet 1 mute bandpass.
- Climax order (223 and 278 the loudest bars).
