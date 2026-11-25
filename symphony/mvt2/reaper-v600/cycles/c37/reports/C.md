# Cycle 37, critic C (blend and space): the c36 render of v600

Lens: one room. This report covers reverb, seating and panning, mic positions, tone matching between sample sets, and the low end against reference recordings.

Material:
- the c36 master and stems;
- the c31 and c32 horn stems, for the effect of c32's soft-horn shelf;
- `cycles/c36/rendered_build/parts.json` and `mix.json`;
- the Opus states in `jobs/*.b64`, decoded (loaded mics, volumes, pans, sends);
- the Dvořák 9/i mp3, decoded and analysed with the same code;
- the stored metrics of Brahms 1/ii and 4/ii (`symphony/render/critics/c04/ref_brahms*_musopen/metrics.json`).

Method: 4096-point FFT frames every 21 ms, summed into third-octave bands per channel, with the L·R cross term kept for correlation and R-L. qn are mapped to seconds through the parts.json tempo map. EQ changes are simulated as band gains on the stem band powers. Side-channel changes are simulated in M/S form with the M·S cross term kept. As a check, the simulation reproduces c32's horn shelf on the c31 stem within 0.13 dB (predicted -15.19, rendered -15.06 dB).

Labels: "measured" means a number from these files. "Inferred" means reasoned from those numbers, the manual or earlier cycles.

## Manual notes (L1: PDF pages 138-139 and 141-142 of the May 2021 HO Opus manual; page 138 also viewed as an image; MANUAL-GAPS.md read)

| Page | What it says | Where it applies here | Render follows it? |
|---|---|---|---|
| 138 | Close mics sit in front of each section, close enough for presence and far enough "to breathe". Mid mics sit at the stage edge: definition without close proximity. Main mics are a Decca tree with outriggers at about row 5: mostly room, "a big, unified sound". Surround and Vintage add depth but lack definition. The stage picture places flutes and clarinets left of centre, oboes and bassoons right, horns back left, trombones and tuba back right, the harp far left, strings first violins to basses left to right. | Decoded states: winds Close 0.5 / Main 0.8; horns 0.5 / 1.0; trombones 0.49 / 1.0; tuba 0.45 / 1.0; timpani 0.2 / 0.5; harp and harmonics 0.6 / 1.0; strings 0.66 / 1.0 (basses 0.6 / 1.0); DIV tracks Close only. Mid, Surround and Vintage are unloaded on all 32 states. | Yes for the unified room. Measured now: the families' tails match (Checks). MANUAL-GAPS #4's reason for a Mid swap (winds drier than strings, c29) no longer holds. Seats follow the stage picture, except that the woodwinds sit within ±2 dB of centre (finding 4). |
| 139 | Each mic sub-mix loads or unloads its samples. Lists the microphone models. | Memory: only two mics loaded per instance. | Yes. |
| 141 | Channel routing (stereo, mono, swap). Stereo Double width works only on a stereo source. Convolution reverb per instrument; "Load with Effects Off". | Widths come from the mic-channel pans (seat ± width), not Stereo Double. All 32 states hold one shared true-stereo IR at fx volume 0.19. | Yes. Pans are clipped at -1 on the harp, harp harmonics (seat -0.72, width 0.3: -1.00..-0.42) and Violins I (-1.00..-0.05). |
| 142 | Reverb preset, pre-delay and volume; MASTER reverb shares one reverb per instance. The AHDSR envelope ships with "natural" values; change with care. | Envelopes are factory except the harp pair (`env_sustain` 1.0, release 200 ms). | Yes. |

MANUAL-GAPS items that touch this lens:
- #4 (Mid mics): not needed for depth now. It stays open only as a timbre experiment.
- #8 (4 soli on DIV patches): the celli are done (c33); the basses are still open (timbre only).
- #3 (Solo Violin): not installed.

## Findings, ranked by what a listener would hear

### 1. The soft horns still have the mf colour turned down, and Horn 3 never got the soft shelf: its ppp opening is brighter than Horn 1's p theme (measured; fix simulated)

**Where:**
- Horn 3 bars 1-6 (qn 0-18, ppp/pp, the C-D flat-C of the introduction);
- Horn 1 bars 7-14 (qn 18-42, the dolce theme) and bars 67-70 (qn 226-238);
- Horns 1-2 a2 bar 82 (qn 271-274, p).

**What is wrong.** c31 put the soft horns back on CC1 57-72 (mf samples) because the 1FH legato table collapses soft targets. c32 C #4 added a -4 dB high shelf at 1.2 kHz to Horns 1, 2 and 4 as the soft colour. That shelf moved the colour only 1.4-1.5 dB. Horn 3 and the a2 track were left out.

**Evidence (measured).** 1-5 kHz share of the energy above 60 Hz:

| Passage | c31 | c32 / c36 | c30 soft layers (c32 C table) |
|---|---|---|---|
| Horn 1 bars 7-10 | -13.7 | -15.0 | -19.4 |
| Horn 1 bars 11-14 | -12.3 | -13.8 | -17.6 |
| Horn 1 bars 67-70 | -14.5 | -15.9 | -19.9 |

- Horn 3 bars 1-6: -13.0 dB in c31, c32 and c36 (no shelf). Horn 4 in the same bars: -14.9 dB.
- So the ppp Horn 3 is 2 dB brighter than the p theme. Its own pair is darker. The softest horn passage is the brightest.
- Horns 1-2 a2 bar 82 (p): -11.1 dB.
- For comparison, the f/ff horns: Horn 1 ff -9.1, Horn 3 bars 61-62 -10.0, a2 bars 79-81 -10.0.
- The whole colour range from ppp to ff is 4 dB. The score asks ppp-pp-p-f-ff of the same instruments (inferred listener effect: a turned-down mf, not a soft horn).

**Fix** (`build/mix.json`, ReaEQ only, `--mix-only`/`--midi-only`, no Opus state change):
- Horns 1, 2 and 4: change the existing soft `loud_eq` band from `{"band":"highshelf","hz":1200,"db":-4}` to `{"band":"highshelf","hz":800,"db":-8}`. Keep the points.
- Horn 3: add the same `loud_eq` with Horn 4's points `[[0,1],[186,1],[194,0],[220,0],[221,1],[258,1],[261,0],[277,0]]`. That keeps wet 0 over its f passages 204-212 and 261-271, and over the coda, where `mute_eq` takes over.
- Horns 1-2 a2: add `loud_eq` `{"points": [[0,0],[270,0],[271,1],[304,1]], "bands": [{"band":"highshelf","hz":800,"db":-8}]}` for bar 82.

**Simulated on the c36 stems:**

| Passage | c36 | With the fix | Target (c30's real soft samples) |
|---|---|---|---|
| Horn 1 bars 7-10 | -15.0 | -18.3 | -19.4 |
| Horn 1 bars 11-14 | -13.8 | -17.0 | -17.6 |
| Horn 1 bars 67-70 | -15.9 | -19.6 | -19.9 |
| Horn 3 bars 1-6 | -13.0 | -17.7 | — |
| a2 bar 82 | -11.1 | -15.8 | — |

- Levels: Horn 1 -0.7..-1.1 dB, Horn 3 -1.1 dB, a2 -1.5 dB. Add +1 dB to these horns' `soft_trim_db` ppp/pp/p (Horn 1 and Horn 3: 3/3/3.5 -> 4/4/4.5), or check by stem fix.
- A gentler alternative is 900 Hz -6 dB. It gives -16.9 / -15.6 / -17.9 on Horn 1, -16.2 on Horn 3, and about -0.5 dB of level.

**Check:** shares as above; f/ff passages unchanged (wet 0); horn levels per bar within ±0.5 dB of c36 after the trim.

### 2. The coda's harp harmonics (bar 83) have an unstable, phasey image: each of the three notes sits somewhere else (measured; fix from movement I, inferred)

**Where:** Harp harmonics (stem 27), qn 274-277: A flat 4, C5, E flat 5, dolce. They are the top voice over the ppp pedal and the first sound of the coda.

**Evidence (measured).**
- At each note's fundamental (first 0.6 s):
  - R-L -11.4 / -7.8 / -9.0 dB;
  - L/R correlation +0.02 / +0.39 / +0.35.
- In 0.2 s steps the correlation swings from -0.49 to +0.68 and R-L from -16 to -1.6 dB within the three notes.
- Over the passage, correlation at 250-1000 Hz is 0.22 and at 1-4 kHz 0.14. The harp just before it measures 0.45 / 0.72, the solo winds 0.54-0.81 and the string sections 0.43-0.79.
- Cause (inferred): the patch is nearly a pure tone. Its two mic pairs are panned -1.00 to -0.42 (seat -0.72, width 0.3, clipped at -1), and a sinusoid's L/R phase from spaced pairs is arbitrary per pitch.
- Movement I (c21, c35) measured the same effect on the solo woodwinds: width 0.05 took the per-pitch image SD from 4.2-6.0 to 2.4-3.7 dB, and note-to-note steps from 8.2 to 1.4 dB, at under 0.3 dB of level.

**Fix:**
- `build/mix.json` "Harp harmonics": `"width": 0.05`, seat kept at -0.72. This is an Opus pan change, so the track's state is rewritten; the patch is small.
- Keep `side_shelf` 300 Hz -8.

**Check:**
- per-note fundamental R-L within ±2 dB of each other and near the harp's 1-4 kHz image (-9..-10 dB);
- correlation at 250-4000 Hz above 0.5;
- level within 0.5 dB.

### 3. The soft timpani rolls are spread across the stage and nearly uncorrelated at 120-250 Hz (measured; fix simulated for the shelf part)

**Where:** Timpani (stem 20):
- the ppp rolls of bars 67-70 (qn 226-238, under Horn 1 alone and the basses' 4 soli);
- the rolls of bars 78-81 (qn 261-271);
- less so bars 60-62.

**Evidence (measured).**
- Timpani stem correlation at 120-250 Hz: 0.32 in bars 67-70, 0.25 in bars 79-81 and 0.46 in bars 60-62. At 40-120 Hz it is 0.93-0.96, because c33's 150 Hz side shelf works there.
- The timpani are 15-16% of the master's 120-250 Hz in those bars.
- The master's 120-250 Hz correlation in bars 67-70 is 0.34 (250-500 Hz: 0.37). Brahms 1/ii and 4/ii measure 0.60 / 0.62 below 250 Hz over the whole piece.
- The decoded state pans the single timpanist from -0.65 to +0.55 (width 0.6), wider than any section except Violins I and Violas.
- Inferred listener effect on headphones: the soft roll becomes a diffuse rumble around the head instead of a low layer behind the orchestra.

**Fix** (`build/mix.json` "Timpani"):
- `"side_shelf": {"hz": 300, "db": -9}` instead of 150 Hz. This extends c33's shelf upward; below 150 Hz nothing changes.
- `"width": 0.3` instead of the group's 0.6. This is an Opus pan change; rebuild the track's state.

**Simulated (shelf only)** on the c36 stem:

| Timpani at 120-250 Hz | c36 | With the shelf |
|---|---|---|
| Bars 67-70 correlation | 0.32 | 0.57 |
| Bars 79-81 correlation | 0.25 | 0.51 |
| Bars 60-62 correlation | 0.46 | 0.67 |

- At 250-500 Hz: 0.57-0.61 -> 0.75-0.77.
- The image is unchanged (R-L within 0.5 dB).
- Level -0.8 dB at 120-250 Hz and -0.5 dB at 250-500 Hz. The rolls already sit under the texture (BRIEF item 5); no level fix is needed.
- The width change is not simulated (inferred to add to it).

**Check:** master 120-250 Hz correlation in bars 67-70 at 0.5 or above; timpani roll levels per bar within 1 dB of c36.

### 4. The woodwinds sit at one point in the centre; the stage picture spreads them (measured image, benefit inferred)

**Where:** the exposed wind dialogues:
- Flute 1 and cor anglais, bars 41-44 (qn 124-140);
- Oboe 1 against the celli, bars 45-47;
- Clarinet 1 against the cor anglais and horns in the coda, bars 85-89.

**Evidence (measured).**
- Measured images at 1-4 kHz, R-L:
  - Flute 1 -1.1 dB;
  - Oboe 1 +1.6..+1.9;
  - cor anglais +1.6;
  - Clarinet 1 -2.4..-2.8;
  - bass clarinet -0.6.
- The strings span -8.2 (Violins I) to +7.9 dB (basses), and the horns sit at -5..-8.
- Seats (mix.json) run from -0.2 to +0.25. The rendered images give about 12-15 dB of R-L per unit of seat.
- The Flute 1 / cor anglais duet is 2.7 dB apart.
- p.138's stage places flutes and clarinets left of centre and oboes and bassoons right.
- The c29 width 0.05 steadied each wind's image; this finding is only about where each image sits.

**Fix** (`build/mix.json` seats, Opus pans, rebuild the wind states; keep width 0.05):
- Flute 1 -0.2, Flute 2 -0.25;
- Oboe 1 +0.2, Oboe 2 +0.25, cor anglais +0.3;
- Clarinet 1 -0.25, Clarinet 2 -0.3, bass clarinet -0.15;
- Bassoon 1 +0.25, Bassoon 2 +0.3, contrabassoon +0.3.

Expected: about ±3-4.5 dB R-L, still well inside the strings (inferred). Do it in the same rebuild as findings 2-3. Lower priority than 1-3.

## Checks for this lens, and what not to chase

**Room and depth (measured; the c29/c33 sends worked).** Level after the note-off, relative to the last 0.3 s, 500 Hz-4 kHz, on every note at least 0.5 qn long followed by 0.6 s or more of rest. Values are medians at +0.2 s / +0.47 s:

| Family | Notes | +0.2 s | +0.47 s |
|---|---|---|---|
| Winds | 57 | -12.1 | -18.7 |
| Horns | 17 | -10.6 | -19.6 |
| Trombones/tuba | 4 | -12.4 | -19.5 |
| Strings | 43 | -10.7 | -18.4 |
| DIV tracks | 12 | -8.0 | -18.0 |

- All families decay together within about 1.5 dB at +0.47 s. The DIV tracks are 2-3 dB wetter at +0.2 s.
- In the final chord, Violas div and Violas decay alike: -9.4 / -9.6 dB at 0.2 s and -17.5 / -18.3 dB at 0.5 s. No change is needed.

**Tone matches (measured, each relative to its own 250 Hz-1 kHz band, same frames):**
- Violas div / Violas coda (279-304): 1-4 kHz -13.7 / -13.8, 4-10 kHz -35.1 / -35.4.
- Violas div / Violas bars 80-81: -7.5 / -8.4.
- Violoncellos div / Violoncellos in bars 18 and 21-22: +1.7..+2.7 dB.
- Violins II div / Violins II (sul tasto, 108-124): 5.3 dB brighter at 1-4 kHz, down from 11.3 in c28 and 9 in c32. The div voice is a fourth higher; leave it.
- Muted against open Violins II: 1-4 kHz -6.4 (42-66) and -9.7 (coda) against -2.2 open (238-250); 4-10 kHz 10 dB darker. The mutes are audible as colour.
- Violin I solo (senza sord.) is 3-4 dB brighter at 1-4 and 4-10 kHz than its muted section, as printed.
- The CC15 lanes sit in rests before every con sord. entry.

**Low end against the references (measured; do not chase with EQ).**
- Octave sums relative to 178 Hz-2.2 kHz, 250 Hz octave minus 125 Hz octave:
  - c36 +5.3 dB over all frames (c28: +4.2), +6.0 in the loudest 10% of frames, +1.5 in the softest 30%;
  - Dvořák +0.1, Brahms 1/ii -0.7, Brahms 4/ii -1.8.
- The deficit is the loud tutti (bars 59-64 and 78-81):
  - celli are 47% of the loud frames' 112-224 Hz, basses 31%, low brass together 8%;
  - at bars 79-81 the celli play the tune on A flat 3-D flat 4, above that band.
- Simulated EQ options, each on top of the last:

  | EQ option | Loud-frame tilt |
  |---|---|
  | c36 | +6.0 |
  | Celli loud bell to 120 Hz and -3 dB at 300 Hz, violas -3 dB at 300 Hz | +5.3 |
  | Plus horns -2.5 dB at 300 Hz | +4.8 |
  | Plus basses' loud bell 150 +4 -> 125 +5 | +4.1 |
  | Plus +3 dB at 140 Hz on the low brass, bassoon 2 and contrabassoon | +4.0 |

- The full set costs the celli -1.8 dB. That is about a third of the gap at the cost of the tune's level. The rest is the voicing (KIT §14).
- The soft passages match the references' loud-soft brightness swing: centroid 916 / 475 Hz loud / soft against Brahms 4/ii 782 / 507, and loud-minus-soft at 2.5 / 5 / 10 kHz +5.9 / +10.9 / +12.7 dB against +5.8 / +10.4 / +10.6.
- In the loud frames the bass clarinet is 20% of 40-112 Hz. In bar 60 its A flat 2 fundamental equals the whole bass section's 40-112 Hz (29.8 against 30.1 dB). That is a balance question for B.

**Stereo (measured).**
- Master correlation, loud / soft frames:
  - 25-120 Hz 0.87 / 0.91;
  - 120-250 Hz 0.63 / 0.67;
  - 250 Hz-1 kHz 0.54 / 0.49;
  - 1-4 kHz 0.55 / 0.61;
  - above 4 kHz 0.51 / 0.77.
- References: Dvořák loud 0.65 / 0.54 / 0.52 / 0.59 / 0.54; Brahms below 250 Hz 0.60, 250 Hz-4 kHz 0.48.
- The bass below 120 Hz is more mono than the references since c33's side shelves. It is central, which was the aim; keep it.
- The harp's fundamentals image at -2..-3 dB R-L and its overtones at -9 dB. Lowering its 300 Hz side shelf does not move the fundamentals (simulated: -2.2 -> -2.9 dB). It only drops the 250-500 Hz correlation to about 0, so leave the shelf.

**Item 8, loop pulsing (measured).** 100-300 Hz level and spectral-centroid autocorrelation at 3.95 s, master:
- bars 1-6: +0.00 / -0.06;
- bars 65-70: +0.03 / +0.17;
- bars 83-86: +0.20 / -0.00;
- bars 87-91: -0.11 / +0.03.

The highest stems are Violoncellos +0.26 / +0.21 and Violins II +0.25 in bars 87-91. All are under 0.3.

**Item 9 (measured).** Trombone 1, 2-5 kHz first 80 ms minus body: 212.5 -0.7, 213 -2.8, 215 -2.7, 218 +1.0 dB. The master's 2-5 kHz jump at these notes is -4.5 / -1.6 / -3.2 / +0.6 dB.

**S3 (measured).** No stem falls more than 24 dB within 0.3 s of a note-off into a rest of 1 s or more. The only one at -24.1 dB is Violoncellos at qn 87, the full close of bar 30, which ends a printed decrescendo. The fast vol_db falls under sounding notes are onset fills and re-bow shapes, not subito drops.

**S1, S2:** left to the articulation and timing lenses (not measured here).

**Do not touch:**
- the shared true-stereo hall (IR, 30 ms pre-delay, fx volume 0.19, wet 2.0, 5.5 kHz high cut);
- the family sends (wind 0.6, horn 0.5, low brass 0.45, string 0.25, DIV 0.5, Violin I solo 0.8): depth now matches across families;
- width 0.05 on the solo winds;
- the string seats in concert order;
- the con sordino lanes and the muted/open colour difference;
- the Violas div and Violoncellos div tone matches;
- the Violins II div 1 kHz shelf;
- the Cb 100 Hz side shelf, the Cb EQ set and the Violoncellos side shelves;
- harp env_sustain 1.0, release 200 ms, and the harp's 300 Hz side shelf.
