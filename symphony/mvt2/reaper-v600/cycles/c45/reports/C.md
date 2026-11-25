# Cycle 45, critic C: blend and space (on the c44 render, the first EastWest template mix)

Material: the c44 stems and master (`cycles/c44/render/`, dry stems 01-32 plus returns 33-36; the master is their float sum), `cycles/c44/rendered_build/` and `build/mix.json` (the delivered state), the c43 render for comparison, and the Dvořák 9/i recording (decoded from the MP3; the stored Brahms metrics for band shares). Simulations: every stem's L/R spectrum was taken with one full-length FFT, the proposed EQ bands were applied as RBJ magnitude responses (the `biquad_h` code of `tools/deliver_master.py`; ReaEQ shelves modelled at bw 2.0 oct, so give `bw_oct` explicitly), and the master was re-summed from the changed stems. The simulation reproduces the c44 master exactly (side/mid -2.2 dB, corr 0.01 at 120-250 Hz). The returns are left unchanged in the simulation; the sends are post-fader, so they carry the side EQ, but the true-stereo halls make their own width.

## Manual notes (L1: May 2021 HO manual PDF pp. 138-139, 141-142, read in full, p.138 also as an image; `loop/MANUAL-GAPS.md` read)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 138 | Main mics sit at about the fifth row and capture "more room reflections than direct sound": a Decca tree above the orchestra plus outriggers on both sides. | Strings and brass play Main 1.0 at full width (pan_by_mic) with Close 0.34-0.5 under it. | Yes, and this is the cause of finding 1: a spaced tree with wide outriggers is decorrelated below 250 Hz (celli stem corr -0.11, tuba -0.07, Trombone 2 -0.06 at 120-250 Hz). |
| 138 | Close mics capture direct sound with "room to breathe"; Mid mics give "definition without the sound of close proximity"; Surround and Vintage give depth without definition. | The DIV A/B tracks (Violin I solo, Vc div, Vln II div, Vla div) load only Close. The harp is Main-led (Close 0.6 / Main 1.0); the template runs the harp Close 0 / Main -9 / Mid 0 dB. | Partly. The DIV tracks get no room of their own and c44 dropped their extra hall (finding 4). The harp does not follow the template (finding 6). Mid is not used anywhere. |
| 139 | Mic list (Main = three Neumann M50 in a Decca tree with Brauner outriggers); each mic sub-mix has its own volume, pan, on/off and mute/solo. | `apply_mix` sets per-mic volumes and pans (pan_by_mic). | Yes. |
| 141 | Channel Routing: Stereo, Mono, Mono from Left/Right, Swap. Stereo Double widens a source (only with a stereo channel source). Reverb on/off; "Load with Effects Off". | Every track routes Stereo. The DIV stems are a panned mono signal: side/mid is the same at every frequency (Vln II div -15.6 dB, Violin I solo -10.8, Vc div -7.5 to -9.8) and Violas div, at seat 0, is exactly mono (side/mid -106 dB). | Routing yes. Stereo Double is not used; I do not recommend it for the DIV tracks (a delayed copy, inferred to sound phasey); more hall does the job (finding 4). Opus reverb is off on every track (`reverb.opus_off`), as the template does. |
| 142 | Reverb presets, pre-delay, volume, master reverb; the 5-stage envelope ("all instruments are programmed with envelope values to achieve a natural result, so please be careful when changing them"). | Returns carry the hall; release caps on string and horn rows (`sus_release_cap_ms`). | Yes. The caps were checked for clipped endings in c40-c43 (none over 10 dB in 0.05 s). |

Dan's standing checks for this lens (measured on the c44 master): no loop pulsing (100-300 Hz band and centroid autocorrelation at 3.95 s: opening C5 -0.18 / +0.12, bars 65-67 pedal +0.12 / +0.09, coda pedal +0.08 / 0.00, final chord +0.05 / -0.05). Trombone 1's accents stay soft (c44's own measure: 2-5 kHz first 80 ms 10.0 and 15.7 dB under the body). S1 and S3 were measured by the c44 actor and critic A; the post-fader sends let a return's tail ring on after a volume-envelope drop, which helps S3.

## 1. The image is about 3 dB too wide at every frequency and uncorrelated at 120-250 Hz. Fix: a side EQ (bell at 200 Hz plus a high shelf) on the 14 full-width Main tracks (measured; fix simulated)

**Where.** Every passage with strings or brass. The worst passages are the tutti: below 250 Hz the master's L/R correlation is -0.02 in bars 23-30, -0.03 in bars 61-62 and 0.16 in bars 79-81 (c43: 0.53 / 0.61 / 0.65).

**Evidence (measured).** Master side/mid in dB, with L/R correlation after the slash:

| band | c43 | c44 | Dvořák 9/i | after the fix (simulated) |
|---|---|---|---|---|
| 60-120 Hz | -12.1 / 0.89 | -6.8 / 0.66 | -5.0 / 0.56 | -8.3 / 0.74 |
| 120-250 Hz | -5.5 / 0.61 | **-0.1 / 0.01** | -5.0 / 0.56 | -5.2 / 0.53 |
| 250-500 Hz | -6.7 / 0.65 | -2.7 / 0.30 | -4.9 / 0.52 | -6.0 / 0.60 |
| 500-2000 Hz | -6.1 / 0.61 | -3.0 / 0.33 | -5.5 / 0.57 | -5.4 / 0.55 |
| 2-6 kHz | -4.3 / 0.52 | -2.2 / 0.25 | -6.1 / 0.66 | -4.5 / 0.47 |
| 6-20 kHz | -3.3 / 0.44 | -1.6 / 0.18 | -2.7 / 0.31 | -3.9 / 0.42 |
| full band | -6.1 | **-2.2** | -5.3 | **-5.4** |

- **Who owns the side signal below 250 Hz.** Violoncellos 57 %, Tuba 14 %, Double basses 13 %, Trombone 2 4 %, Bass trombone 2 %; the four returns together 5 %.
- **Why.** Each of these stems now has more side than mid at 120-250 Hz: Violoncellos +0.9 dB, Tuba +0.3, Trombone 2 +0.5, Double basses +0.2. In c43 they were at -5 to -8 dB.
- **Not only the bass.** Above 250 Hz the strings and brass stems sit at -0.3 to -2.9 dB side/mid. Violins I has 59 % of the master's side at 2-6 kHz. The celli's c29 side high shelf (+4 dB at 1.5 kHz, added when the celli were too mono) now puts them at +2.5 dB side/mid at 2-6 kHz. The brass's c21 side high shelf (+1.5 dB at 250 Hz, added for narrow pairs) widens Main pairs that are already full width.

**Fix (`build/mix.json`, `side_shelf` lists; existing tool, applied by `--mix-only`).**

- On Violins I, Violins II, Violas, Violoncellos, Horn 1-4, Horns 1-2 a2, Trombone 1, Trombone 2, Bass trombone and Tuba, set:

  `"side_shelf": [{"band": "bell", "hz": 200, "db": -6, "bw_oct": 1.2}, {"band": "highshelf", "hz": 350, "db": -2, "bw_oct": 2.0}]`

  This replaces their present entries: the celli's lowshelf 200 Hz 0 dB and highshelf 1500 Hz +4; the brass highshelf 250 Hz +1.5 dB; the bass trombone's and tuba's lowshelf 200 Hz 0 dB.
- On Double basses (keep c41's deep-bass cut):

  `[{"band": "lowshelf", "hz": 100, "db": -15}, {"band": "bell", "hz": 200, "db": -6, "bw_oct": 1.2}, {"band": "highshelf", "hz": 350, "db": -2, "bw_oct": 2.0}]`

- Leave the woodwinds (Close-led, side/mid -7 to -18 dB), the DIV tracks, the harp and the timpani as they are.
- Make-up `gain_db`, from the simulated A-weighted stereo-power loss of each stem: Violins I +0.7, Violins II +0.7, Violas +0.8, Violoncellos +1.5, Double basses +1.2, Horn 1 +1.0, Horn 2 +0.9, Horn 3 +1.6, Horn 4 +1.0, Horns 1-2 a2 +0.9, Trombone 1 +1.2, Trombone 2 +1.4, Bass trombone +1.4, Tuba +1.5 dB. Add finding 3's make-up to these where both apply.

**Result (simulated).**
- Full-band side/mid -5.4 dB and per-band correlation 0.47-0.60 from 120 Hz to 6 kHz, the reference's values.
- Below 250 Hz, by passage: bars 7-14 0.58 -> 0.67, bars 23-30 -0.02 -> 0.52, bars 37-44 0.40 -> 0.65, bars 61-62 -0.03 -> 0.51, bars 65-70 0.46 -> 0.72, bars 79-81 0.16 -> 0.57, coda 0.48 -> 0.71.
- Seats move by at most 0.8 dB (Violins I R-L -4.5 -> -4.2 dB at 0.5-2 kHz, Violoncellos +3.6 -> +3.3, Horn 1 -4.0 -> -3.2).

**Alternatives not chosen.**
- Narrowing the Main pair in Opus (a `pan_by_mic` width under 1.0) narrows all frequencies alike. It needs a tool change and 14 state rebuilds, and it moves the seats.
- Raising Close against Main changes the template's tone and leaves the Main pair's own decorrelation in place.
- A low shelf at 250 Hz (first try, I1 in my runs) over-narrowed 60-120 Hz (-9.2 dB / 0.79). The bell keeps that band near c44.

**Check after the render.** Master corr 0.50-0.65 in each band from 120 Hz to 2 kHz; full-band side/mid -4.5 to -5.5 dB; stem levels within 0.5 dB of c44 after the make-up.

## 2. The horns' hall is 10-15 dB hotter, relative to the dry sound, than the strings', and the soft horn passages are thick at 250-500 Hz. Fix: the c38 160 Hz low cut on the returns, R Brass -4 dB, and the soft horn shelf halved (measured; cause of the thickness inferred)

**Where.** Horn 1's theme in bars 7-14 (qn 18-42) and 67-70 (qn 226-238), and the brass under the violin theme in bars 23-30.

**Evidence (measured).** Each return against its family's dry stems (dB):

| return re dry | 125-250 Hz | 250-500 | 500-2000 | 2-6 kHz |
|---|---|---|---|---|
| R Brass, bars 7-14 | -5.2 | -8.0 | -10.2 | -17.6 |
| R Brass, bars 23-30 | -6.6 | -6.0 | -8.3 | -17.4 |
| R Brass, bars 67-70 | -8.1 | -5.7 | -9.4 | -18.8 |
| R Strings, bars 23-30 | -16.2 | -20.0 | -22.2 | -32.0 |
| R Strings, whole piece | -16.0 | -20.2 | -23.2 | -32.7 |
| R Winds, bars 7-14 | -9.4 | -11.1 | -12.9 | -16.3 |

- **The mismatch.** Horns and strings use the same mic layout (Main 1.0 at full width, Close under it), so each already carries its Main room. Yet the horns' return is 10-15 dB hotter than the strings' return, relative to the dry sound. R Brass is the second-loudest stem in bars 7, 8, 11, 12 and 13 (metrics.md).
- **Why.** The c44 wetness fix fitted each return fader to the family's tail time at stops: strings -18 dB, brass -2, winds -4 against the template. The template itself runs brass 3 dB under strings. Tail time hides this: the 0.5 IR envelope makes the brass tail short (t20 0.34 s), while the hall's level during held notes stays high.
- **The master in bars 7-14.**
  - 250-500 Hz share -1.5 dB and 500-2000 Hz share -9.2 dB. In c43 these were -2.4 and -5.1; Dvořák 9/i has -6.3 and -3.4.
  - So the horn theme is 7.7 dB heavier at 250-500 than at 500-2000, where the reference is 2.9 dB lighter.
  - Horn 1's own stem: 500-2000 Hz share -4.8 dB in c43, -9.6 dB in c44. The brass family EQ (-7.8 dB at 821 Hz) now stacks on the c37 soft shelf (800 Hz -8, kept by c44 B #6).
- **The c38 low cut was lost.** Dan's mush fix of c38 was a 160 Hz low cut on the hall input. The template returns high-pass at only 87-100 Hz (`ho-mix-fx.json`: STRING VERB 87 Hz, the other three 100 Hz).

**Fix.**
- `build/mix.json` `returns`: add `"hp_hz": 160` to R Strings, R Brass, R Winds and R Perc. The existing key edits band 0 of each return's pre-Spaces ReaEQ and reads it back (`tools/build_reaper.py` `returns_job`).
- R Brass `fader_db` -0.97 -> -4.97. The horns are the only brass that send; trombones and tuba send nothing.
- On Horns 1-4 and Horns 1-2 a2, `loud_eq` band highshelf 800 Hz -8 -> 800 Hz -4. The family bell now does the other half.

**Targets.**
- R Brass at 125-500 Hz -10 to -13 dB re dry in bars 7-14 and 67-70.
- Master 250-500 Hz share in bars 7-14 at -3 dB or lower, and 500-2000 Hz at -6.5 dB or higher.
- Horn 1's 1-5 kHz share at p no higher than -18 dB (c30's measured real soft layers -19 to -20).
- Brass family t20 0.28-0.40 s, and no family wetter than c43.

**Risk.** If the horn theme then sounds dry next to the winds (t20 under 0.28 s), give back 1-2 dB on R Brass. Keep the low cut. The level ratios are measured; that the 250-500 Hz excess is what Dan heard as "mushy" is inferred.

## 3. Too bright: 6-20 kHz share -24.6 dB. Halving the family shelves only reaches -25.9; the string shelf has to go and the violins need their own top cut (measured; fix simulated)

**Evidence (measured).** On the dry stems, Violins I supplies 61 % of the master's 6-20 kHz and 53 % of its 2-6 kHz, Violins II 15 % and 17 %, Trombone 1 7 % and 4 %. The rest is under 3 % each.

Simulated master shares (6-20 kHz / 2-6 kHz, dB):

| change | 6-20 kHz | 2-6 kHz |
|---|---|---|
| c44 | -24.6 | -8.6 |
| string and brass family shelves halved (critic B's plan) | -25.9 | -8.9 |
| plus 5 kHz -4 dB on Violins II | -26.2 | -9.0 |
| string family shelf removed, brass shelf halved | -27.0 | -9.1 |
| **as above, plus Violins I and Violin I solo 5 kHz -4 -> -6 and Violins II 5 kHz -4** | **-28.1** | **-9.4** |
| references | -28.8 to -32.3 | -10.5 to -12.4 |

The 500-2000 Hz share is unchanged (-4.3 dB).

**Fix (`build/mix.json`).**
- In the `string` group `family_eq` and the Double basses' own `family_eq`, set the `hshelf` 4730 Hz band to 0 dB.
- In the `horn` and `lowbrass` group `family_eq`, set `hshelf` 7490 Hz +4 -> +2 dB.
- Violins I and Violin I solo `eq`: highshelf 5000 Hz -4 -> -6 dB.
- Violins II `eq`: add `{"band": "highshelf", "hz": 5000, "db": -4}`.
- Make-up `gain_db` (A-weighted, simulated): Violins I +0.8, Violins II +0.6, Violas +0.2, Violin I solo +0.7. Brass under 0.1.
- Combined with finding 1 the totals are Violins I +1.6, Violins II +1.3, Violas +1.0, Violoncellos +1.6, Double basses +1.2, Violin I solo +0.7, and the brass values of finding 1 plus 0.1 on Trombone 1.

**Why not the template's shelf.** The template's +4 dB at 4.7 kHz assumes a dry close library and a brighter hall return. Here the returns are low-passed at 2.3 kHz, and the strings' 1 kHz is cut 5 dB, so every lift above it shows. Duc's variant (a 9-11 kHz lift, FINDINGS §14) would add top, which the numbers do not support.

**Checks after the render.**
- 6-20 kHz share -28 to -31 dB; 2-6 kHz -9 to -12 dB.
- Re-check the brass 2-5 kHz accent jump (p90 under +2 dB; the halved shelf lowers it).
- If the share is still above -28, add 5 kHz -2 dB on Violas before touching the body bands.

## 4. The DIV and solo tracks are dry mono points next to full-width sections: c44 dropped their extra hall, and the Vc div sits 4 dB further right than its section (measured)

**Where.**
- Violin I solo: bars 17-22, qn 48-65.
- Violoncellos div: bars 18 and 21-22, and the coda 4 soli at qn 274-286.
- Violins II div: bars 37-40, qn 108-124.
- Violas div: bars 23-30, 80-81 and 84-92.

**Evidence (measured).**
- **Width.** The DIV patches load only the Close mic, and their stems are a panned mono signal. L/R correlation at 250 Hz-4 kHz is 1.00 on all four DIV tracks in their passages (Vc div 0.99). Their sections in the same passages measure 0.00-0.36.
- **Dryness.** Dry-stem drop 0.3 s after the stops (median):

  | DIV track | drop | its section | drop |
  |---|---|---|---|
  | Violin I solo | 21.1 dB | Violins I | 11.6 dB |
  | Violas div | 16.0 dB | Violas | 9.5 dB |
  | Violoncellos div | 13.7 dB | Violoncellos | 11.0 dB |

  The sections carry their own Main-mic room; the DIV tracks do not.
- **Lost compensation.** Series 1 c10/c13/c29 compensated with Opus sends of 0.5, and 0.8 on the solo, against the sections' 0.25: +6 and +10 dB of hall. Since c44 these `send` values are dead (`opus_off`). The DIV tracks inherit the string group's R Strings send of -5.56 dB, the same as a section with a Main pair.
- **Seat.** R-L at 0.5-2 kHz: Violoncellos div +7.8 dB against the celli's +3.6, so the coda 4 soli and the bar 18/21 answers jump right. Violin I solo (-5.1 against -4.5), Violins II div (-3.3 against -3.1) and Violas div (centre against +0.3) match their sections.
- **Tone.** Within ±3.4 dB of the section per octave, except one spot. Violins II div against Violins II in bars 37-40 is 5.4 dB low at 500-1000 Hz, because its c29 highshelf 1 kHz -10 dB now stacks on the family's -5 dB at 1 kHz.

**Fix (`build/mix.json`).**
- Track `return` entries:
  - Violin I solo `[{"to": "R Strings", "db": 2.4}]` (+8 over the sections).
  - Violins II div and Violas div `[{"to": "R Strings", "db": 0.4}]` (+6).
  - Violoncellos div `[{"to": "R Strings", "db": -1.2}]` (+6 over the celli's -7.16).
- Violoncellos div: `seat` 0.33 -> 0.15 and `track_pan` 0.15 -> 0.05 (an Opus state change on one track). Target: R-L within 1 dB of the Violoncellos stem.
- Violins II div `eq`: highshelf 1000 Hz -10 -> 1500 Hz -6 (c29's original value).
- The `side_shelf` +3 dB at 250 Hz on Violas div does nothing (its side signal is zero at seat 0); leave it or delete it.

**Checks.**
- Each DIV track's dry + R Strings drop at +0.3 s within 3 dB of its section's.
- Strings family t20 0.55 s or less, the c43 limit; c44 is already at 0.55. If it is over, take R Strings `fader_db` down 1 dB.

The dryness and width are measured; that more hall is the right remedy rather than a wider image is inferred.

## 5. Seating is about 3 dB weaker than c43, and the two violin sections are only 1.4 dB apart (measured; target inferred)

**Evidence (measured).** R-L at 0.5-2 kHz on the dry stems:

| stem | c43 | c44 |
|---|---|---|
| Violins I | -7.8 | -4.5 |
| Violins II | -3.7 | -3.1 |
| Violas | +1.7 | +0.3 |
| Violoncellos | +5.6 | +3.6 |
| Double basses | +7.0 | +5.0 |
| Horns 1-4 | -2.4 to -6.8 | -0.4 to -6.0 (Horn 1 -6.6 -> -4.0) |
| Tuba | +8.6 | +6.8 |

- **Cause.** The full-width, centred Main pair carries more of each stem than the seated Close mic.
- **Why it matters.** The kit's c07 render matched the reference image with Violins I near -8 dB (`mockup-kit/LEARNINGS.md` section 12). With Violins I and II 1.4 dB apart, the antiphonal answers of the theme (bars 23-30 and 71-78) come from almost one place.

**Fix (`build/mix.json` `track_pan`; REAPER pan, no state change).**
- Violins I -0.10 -> -0.22.
- Violoncellos 0.15 -> 0.25.
- Double basses 0.23 -> 0.30.
- Horns 1-4 and a2: each 0.10 further left (Horn 1 -0.28).
- Keep Violins II at -0.21 and the violas at 0.
- I could not read REAPER's pan law for pan mode 5 from the project (`PANLAW 1`, flags 3), so set the values by measurement. Targets at 0.5-2 kHz after finding 1: Violins I -6.5 ± 1 dB, Violins II -3 ± 1, Violoncellos +5 ± 1, Double basses +6.5 ± 1, Horn 1 -5.5 ± 1.

## 6. The harp did not get the template's Close-led mic mix, and its harmonics are a diffuse wide image (measured; benefit inferred)

**Evidence.**
- The plan (EW-TEMPLATE-PLAN §1) gives the harp Close 0 dB / Main -9 / Mid 0. c44 kept Close 0.6 / Main 1.0, Main 4.4 dB over Close, on Harp and Harp harmonics (group `harp`). No reason is recorded.
- Harp harmonics L/R correlation at 250 Hz-4 kHz in the coda (qn 274-292) is 0.12. That is a wide, unplaced image for a near-pure tone from one harp. The harp in bars 7-14 measures 0.47.
- The harp's own R-L is -5.3 dB at 0.5-2 kHz (seat -0.72), so most of its sound comes from the centred Main pair.

**Fix (`build/mix.json` `groups.harp.mics`).** `{"Close": 1.0, "Main": 0.355}`, that is Main -9 dB, without Mid: Mid would add a mic (memory) and the Main mic stays loaded, so the memory is unchanged. This is two full rebuilds (Harp, Harp harmonics). Re-level both with the A-weighted stem level of c44 in their passages (harp bars 7-14, harmonics bars 83-86, where critic B's margin over Vc div + Cb is -0.1 to +2.1 dB).

**Check.** Harp harmonics correlation 0.6 or higher; harp R-L at 0.5-2 kHz -7 to -9 dB (c43 -9.5).

## Do not touch

- The returns' IR envelope (envelopeMode 2, endPos / decayLength 0.5), the 2.3 kHz return low pass, and no hall send from trombones, tuba, bassoons, contrabassoon and basses.
- The R Strings, R Winds and R Perc faders. Only R Brass moves, in finding 2.
- The basses' 100 Hz -15 dB side shelf (kept inside finding 1's list).
- The timpani's mics (no Surround) and its reduced family EQ; the harp HPF 80 Hz.
- The woodwinds' Close-led mix and their 0.05 widths.
- The re-bows and fills that keep the held notes free of loop pulsing (master autocorrelation 0.12 or lower at the loop period).
- Trombone 1's accent handling.
- The release caps.
