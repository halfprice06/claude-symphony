# Cycle 48, critic C (blend and space), on the c47 render

Material: the c47 stems and master (`cycles/c47/render/`, 32 dry stems plus the four returns; the master is their float sum), `cycles/c47/rendered_build/parts.json` (tempo map) and `mix.json`, the c26-c46 masters for history, the Dvořák 9/i MP3 (decoded, measured here) and the stored third-octave and stereo metrics of four lossless Brahms recordings (`symphony/render/critics/c00|c04/ref_*/metrics.json`). Spectra: 8192-point frames, hop 4096, L²+R²; third octaves as shares of the 31 Hz-16 kHz total; "loud" = the master's loudest 10 % of frames. Width: L/R correlation and side/mid from the cross spectra.

Simulations are frame-by-frame and complex: each changed stem's spectrum is multiplied by the RBJ response of the proposed ReaEQ bands (the model the finale's c08 critic used, which predicted its render within 0.3 dB), and the master is rebuilt as master + Σ(new − old). Each return gets the family EQ and the make-up when every track that feeds it changes the same way. This is exact here because the sends are post-FX and post-fader. Pan and width follow REAPER pan mode 5 as I calibrated it on this project (measured): at width 1 the pan acts as a linear balance, with the near side at unity and the far side at 1 − |pan|. On the c44 → c45 horn pan change (−0.18 → −0.28) this predicted the c45 R-L within 0.3 dB on Horn 1 (bars 7-14 and 65-70) and Horn 3 (bars 1-6). A constant-power law missed by 0.3-1.0 dB. Width is modelled as side × w before the balance. The side-EQ part of the model reproduces the c45 trombones within 0.9 dB R-L and 0.07 correlation. Levels use K-weighting (BS.1770 filter applied to the spectrum) unless named.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 48 (its table ends at c47), so I did no assigned reading. `loop/MANUAL-GAPS.md` was read, and the pages below are the ones my findings rely on (PDF pages of the May 2021 HO manual).

| Manual (PDF page) | What it says | Where it applies | Does c47 follow it? |
|---|---|---|---|
| p.138 | Main mics: "placed in what would be the fifth row", "capturing more room reflections than direct sound", a Decca tree with outriggers. | Horns and trombones run Main 1.0 at full width, with Close 0.48 / 0.34 at the seat (c44 template). | Yes. Because of it the brass dry stems are diffuse: Horn 1's L/R correlation (250 Hz-5 kHz) is 0.61 in bars 7-14, the trombones' 0.37-0.48 and Horn 3's 0.08 in bars 61-64 (finding 2). |
| p.140 | Master Channel Pan "adjusts the volume of the left and right audio signal ... while preserving the relative panning of the individual microphones". | The REAPER track pan (mode 5) does the same thing after the plugin. I measured it as a linear balance (above). | Yes. `track_width` (finding 2) narrows all mics together after the plugin. The plan's "Main stays full width" refers to the Opus mic pans, which do not change. |
| p.90 | "The Divisi instruments include only Close mics". | Violin I solo, Violoncellos div, Violins II div, Violas div. | Yes, and their stems stay mono points (correlation 1.00 against 0.34-0.58 for their sections). c45 gave them +6/+8 dB of hall. I propose no change this cycle. |
| MANUAL-GAPS #4, #8 | Mid mics; half-section patches for the basses' 4 soli. | Winds and horns; basses at qn 220-238 and 286-304. | #4 was superseded by the template layout (c44). #8 was deferred for memory (c35). Neither is ranked here. |

## The ONE_TIME items in my area, in short

| Item | Measured on c47 | Decision |
|---|---|---|
| 5, brass `track_width` | The master's image matches the references: side/mid −5.45 dB, 250 Hz-5 kHz correlation 0.55 (Dvořák −5.3 / 0.56; Brahms −4.7..−5.4 / 0.47-0.54). But the two horn solos measure −5.29 / −4.99 dB, as wide as the tutti and 0.8-1.5 dB wider than reference passages at the same loudness. | Horns 0.8 (finding 2). Trombones stay at 1.0: the finale's 0.6 makes bars 61-64 narrower than every reference. |
| 6, 315 Hz | Whole-piece 315 Hz hump +3.0 dB (loud frames +3.1) against −0.4..−2.5 in the five recordings: an excess of 4.6 dB over their mean. 400-500 Hz is 1.3-1.6 dB under them. | Adopt the cut on the strings, by moving the template's 456 Hz string bell to 315 Hz. Drop the horn bell: in Movement II it is Horn 1's own fundamentals (finding 1). |
| 11, family EQ tone | Strings 1 kHz −2.5 and the brass 821 Hz / 3.2 kHz bells are already the finale's values (3.2 kHz −3 against −4 moves the master's 2-4 kHz by ≤0.1 dB, because strings own 78-82 % of that band). | Winds 1 kHz −3.1 → −1.55 not adopted: the master's 1 kHz third octave is already 1.2 dB above the recordings' mean (finding 1). |
| 12, basses' high-pass | The basses' commonest note is A♭1 (51.9 Hz, 30 % of their held time), at the 53 Hz corner. The master's 49.6 Hz band is 7.6-9.1 dB under the lossless recordings. | Adopt 35 Hz (finding 3). |
| "Too wet" | Final chord −15.8 dB at +0.3 s and −20 dB at 0.38 s, measured from the written end. R Strings sits 23.7 dB under the dry strings. | Inside the limit, at the dry end. No change (finding 4). |

## Dan's standing checks (my lens)

- **Loop pulsing (BRIEF 8), measured.** Autocorrelation at 3.95 s on the master (100-300 Hz level / spectral centroid), against a 2.7 s control:
  - opening C5, bars 1-3: −0.09 / −0.21;
  - bars 65-67 pedal: −0.19 / −0.01;
  - bars 66-70: −0.40 / −0.13;
  - coda pedal, qn 286-301: −0.26 / −0.07;
  - final chord, 298-304: −0.52 / −0.37.

  None is positive (the failure case was 0.39-0.63). No pulsing.
- **S3.** Every change below is a static EQ, width or gain. None adds a volume-envelope step. The sends are post-fader, so an envelope drop no longer cuts the hall's tail.
- **S1, S2 and the accents.** These are other lenses and my changes do not touch them: no note, row or controller data changes, and no EQ on the trombones.

## 1. The low mids peak at 315 Hz and dip at 400-500 Hz. The template's string bell sits half an octave above our peak: move it from 456 to 315 Hz. Do not add the finale's horn bell (measured; fix simulated)

**Where.** The whole piece. It is largest where strings carry the texture: bars 23-30 (qn 66-90), 53-64 (172-220) and 79-82 (262-274). Tracks: violoncellos, violas, Violas div and the other string tracks.

**What is wrong (measured).** Master third octaves (share of total, dB), c47 against the mean of the five recordings:

| Hz | 200 | 250 | 315 | 400 | 500 | 630 |
|---|---|---|---|---|---|---|
| c47 | −11.0 | −12.8 | **−9.0** | −11.2 | −10.5 | −10.2 |
| recordings' mean | −14.4 | −15.1 | −14.1 | −9.9 | −8.9 | −12.1 |

- **Shape.** The recordings rise from 315 into 400-500 Hz. The mockup peaks at 315 and dips at 400-500.
- **The hump** (315 minus the mean of 250 and 400) is +3.0 dB over the whole piece and +3.1 in loud frames. The recordings range from −0.4 (Dvořák) to −2.5 (Brahms 4/i), mean −1.6, so the excess is 4.6 dB.
- **Size.** The rms deviation from the recordings' mean over 200-630 Hz is 2.90 dB. Each recording sits 0.30-1.41 dB from that mean.
- **History.** The hump was +1.4 to +1.5 in c26/c27 and rose to +3.0 from c44. Between c43 and c44 the 500 Hz band fell 1.3 dB and 315 rose 0.7 dB, when the template's bells at 447-475 Hz arrived (strings 456 Hz −2.2, winds 447 Hz −5.1, brass 475 Hz −5.4, later −2.7). From c27 to c47: 315 Hz +2.0 dB, 500 Hz −1.1 dB.

**Who makes it (measured, shares of the 315 Hz band, whole piece).**

- By track: violoncellos 24 %, Horn 1 21 %, violas 17 %, Horns 2-4 together 14 %, contrabassoon 5 %, bass clarinet 5 %, tuba 4 %.
- By family: strings 43 %, horns 33 %, winds 14 %.
- In bars 23-30: celli 32 %, Violas div 31 %, violas 25 %.
- In the two horn solos, Horn 1 owns 88-89 % of the band (bars 7-14 and 65-70). There the hump is Horn 1's E♭4-F4 fundamentals (311-349 Hz).

**Simulated options** (whole piece unless named; make-up applied):

| Option | Hump | 315 | 400 | 500 | rms 200-630 | Bars 23-30 hump | Cost to Horn 1, bars 7-14 / 65-70 (K) |
|---|---|---|---|---|---|---|---|
| c47 | +3.0 | −9.0 | −11.2 | −10.5 | 2.90 | +2.0 | – |
| Finale's item 6 (horns 315 −5 +1.0 dB, violas 315 −3 +0.8) | +2.4 | −10.1 | −11.9 | −10.4 | 2.67 | +1.7 | **−2.2 / −2.9 dB** (Horn 3 −1.9 / −2.4) |
| **String bell 456 → 315 Hz (proposed)** | **+2.6** | −9.4 | −11.0 | −10.0 | **2.67** | **+1.0** | 0 |
| The same plus horns 315 −3 | +2.3 | −9.9 | −11.3 | −10.0 | 2.54 | +0.9 | −1.0 / −1.4 dB |

- **The finale's version** lowers 400 Hz further (a 1-octave bell at 315 reaches it). That band is already under the recordings. It also takes 2.2-2.9 dB off Horn 1's two solos even after its +1.0 dB make-up, because a horn's energy there is its fundamental.
- **The string move** reaches the same rms deviation (2.67) and leaves the horns alone. In bars 23-30 the hump falls from +2.0 to +1.0, 315 Hz by 1.2 dB, and 400 / 500 Hz rise 0.6 / 1.1 dB. In bars 61-64 the hump goes from +3.0 to +2.5.
- **Level.** Every string stem stays within ±0.35 dB K, except Violas div in bars 23-30 (−0.6) and violas in the coda (−0.5).

**Fix** (`build/mix.json`; `--mix-only`, no Opus state change):
- **String EQ.** In `groups.string.family_eq` and in `tracks."Double basses".family_eq` (which carries its own copy), replace `{"type": "bell", "hz": 456.0, "db": -2.2, "bw": 0.75}` with `{"type": "bell", "hz": 315.0, "db": -2.2, "bw": 0.75}`. The violas' and violas div's share of the finale's −3 dB viola bell is covered by this.
- **Make-up `gain_db`** (from the simulated K change of each stem over the piece): Violins I −0.1, Violins II −0.3, Violas +0.2, Violoncellos +0.3, Violin I solo −0.2, Violins II div −0.3, Violas div −0.1, Violoncellos div +0.1, Double basses 0.
- **Horns.** No 315 Hz bell.
- **Winds.** Keep the 1 kHz −3.1 dB bell (item 11 not adopted). Measured:
  - the master's 500-1000 / 1000-2000 Hz octave shares are −6.4 / −7.0 dB, inside the recordings' −5.6..−7.0 / −6.1..−7.4;
  - its 1 kHz third octave (−12.0) is already 1.2 dB above their mean (−13.2);
  - halving the bell moves the master by ≤0.2 dB and lifts 1 kHz in the bass clarinet solo (bars 31-36) from −11.6 to −10.6.

**Check on the render.**
- Whole-piece hump +2.6 ± 0.3 dB.
- 500 Hz share −10.0 or higher.
- Bars 23-30 hump at or below +1.2.
- Each string stem's K level within 0.5 dB of c47 in its main passages.

**Left over (measured; not proposed).**
- The 200-250 Hz excess (+2.3..+3.4 dB) is the celli (57 % of 200 Hz) with series 1's 170 Hz +3 dB bell. Halving that bell lowers 200 Hz by 0.5 dB, but takes 160 Hz (already 2.2 dB under) further down.
- The rest of the 315 hump is horn fundamentals and the A♭ major voicing. The finale also recorded that EQ should not chase horn fundamentals.

## 2. The horn solos are as wide as the full orchestra: set `track_width` 0.8 on the horns. Leave the trombones (measured; fix simulated)

**Where.** Horn 1's theme in bars 7-14 (qn 18-42) and its solo in bars 65-70 (qn 220-238). Also the horns in the intro, at bars 79-82 and in bars 61-64.

**What is wrong (measured).** Master side/mid and the 250 Hz-5 kHz correlation in the horn solos are −5.29 dB / 0.57 (bars 7-14) and −4.99 dB / 0.65 (bars 65-70).

- **Against the whole piece.** The tutti average is −5.45 dB, so a single horn with low winds and harp sounds as wide as the full orchestra.
- **Against the references.** Side/mid by loudness quintile, soft to loud (250 Hz-5 kHz):

  | | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | c47 | −6.4 | −6.7 | −6.8 | −5.3 | −5.3 |
  | Dvořák | −6.4 | −6.3 | −5.8 | −5.5 | −5.4 |

  The mockup's soft passages match. The horn solos are 0.8-1.5 dB wider than Dvořák at the same loudness.
- **The horn stems.** Horn 1's dry correlation is 0.61 in bars 7-14. Horn 3's ff A♭4-B4 in bars 61-64 measures 0.08, with side/mid −0.7 dB: as much side as mid.
- **Cause.** The full-width Main pair is mostly room (manual p.138).
- **The default.** The plan's "brass as narrow sources" default (EW-TEMPLATE-PLAN §9; Howl's horns at 15-47 % width) has not been applied here.

**Simulated widths** (horns at their present pans; R Brass not re-simulated):

| Horn `track_width` | Bars 7-14 S/M / corr | Bars 65-70 | Bars 61-64 | Whole piece S/M |
|---|---|---|---|---|
| 1.0 (c47) | −5.29 / 0.57 | −4.99 / 0.65 | −5.34 | −5.45 |
| **0.8** | **−6.52 / 0.68** | **−5.74 / 0.71** | **−5.51** | **−5.62** |
| 0.7 | −7.17 / 0.73 | −6.13 / 0.74 | −5.58 | −5.70 |
| 0.6 | −7.84 / 0.77 | −6.53 / 0.76 | −5.65 | −5.76 |

- At 0.8 the solos land in Dvořák's range for soft and middle passages (−5.7..−6.4). The whole piece moves 0.17 dB, to just past the narrowest recording (−5.4).
- Horn stems at 0.8: Horn 1's correlation 0.61 → 0.74 (bars 7-14), Horn 3's 0.08 → 0.30 (bars 61-64).
- R-L moves 0.2-0.7 dB toward the centre (Horn 1 bars 65-70: −6.9 → −6.2 dB).

**Trombones, not adopted (measured, simulated).** Their stems are diffuse (correlation 0.37-0.48, R-L +1.6..+2.9 dB, at the template seat +0.25 with pan +0.15), but they play almost only in bars 53-64.
- The finale's width 0.6 at pans +0.26/+0.30/+0.34 takes bars 61-64 from −5.34 to −5.91 dB side/mid and 0.54 → 0.60 correlation. That is narrower than every recording (Dvořák's loud quintile −5.2..−5.4; Brahms −4.7..−5.4).
- Width 0.8 at +0.20/+0.22/+0.24 gives −5.69 alone. Together with the horns at 0.8 it gives −5.88 in bars 61-64 and −5.83 over the whole piece.
- The finale needed narrowing because its master's upper band was too wide (0.47) and its muted trumpet had to sit with the cor anglais. Movement II's master is already at 0.55, and it has no such doubling.

**Fix.**
1. `tools/build_reaper.py`: port `track_width()` from `symphony/mvt3/reaper-v600/tools/build_reaper.py` (lines 100-104). Write it where D_WIDTH is now 1: line 915 of the full track build (`reaper.SetMediaTrackInfo_Value(tr, "D_WIDTH", {track_width(mix_for(tr['name']))})`), and `w=1` → `w={track_width(m)}` in `mix_job()` (line 1064), so `--mix-only` applies it.
2. `build/mix.json` `groups.horn`: `"track_width": 0.8`. This covers Horns 1-4 and Horns 1-2 a2; trombones and tuba are in `lowbrass` and stay at 1.0.
3. Make-up `gain_db` for the narrowed side energy (simulated K change −0.25..−0.54 dB): Horn 1 +0.3, Horn 2 +0.3, Horn 3 +0.5, Horn 4 +0.3, Horns 1-2 a2 +0.4. Pans unchanged.

**Check on the render.** Master side/mid in bars 7-14 between −6.0 and −6.8 dB. Whole piece no narrower than −5.7 dB; if it is, use 0.85. Horn 1's K level within 0.3 dB of c47 in bars 7-14 and 65-70.

That the solos will then sound like one player in the hall is inferred.

## 3. Basses' high-pass 53 → 35 Hz: their tonic pedal A♭1 sits on the template's corner (measured; simulated)

**Where.**
- Every basses note under about 60 Hz.
- Most exposed: the A♭1 pedals (51.9 Hz, 30 % of the basses' held time), in the coda's ppp pedal (qn 274-304) and bars 45-52.
- G♭1 / F1 / E1 are another 7 %.

**What is wrong (measured).**
- `tracks."Double basses".family_eq` carries the template's `hp` 53 Hz (bw 2), about −3.5 dB at the corner and more below it, on top of the series 1 `bell2` 80 Hz −6.
- Master third octaves against the lossless Brahms recordings (the 62.5 Hz band skipped for hum):

  | Hz | 49.6 | 78.7 | 99 |
  |---|---|---|---|
  | c47 | −37.5 | −20.9 | −18.2 |
  | Brahms | −28.4..−29.9 | −12.2..−16.8 | −10.7..−13.5 |

- The Dvořák MP3 (−43.8 / −25.3 / −21.5) is under the mockup, but it lacks low end (LEARNINGS §14).
- Boom: bars 61-64 measure −20.7 dB at 78.7 Hz and −21.1 dB at 99 Hz, 4-8 dB under the lossless recordings. Nothing below 125 Hz is over any lossless reference.

**Fix** (`build/mix.json` `tracks."Double basses".family_eq`, `--mix-only`): `{"type": "hp", "hz": 53.0, ...}` → `"hz": 35.0`. The other string tracks keep 53 Hz in the group EQ. No gain change: the basses' K level moves only +0.06..+0.33 dB.

**Simulated result.**
- Master: 49.6 Hz +2.2 dB, 62.5 Hz +1.5, 78.7 Hz +0.7, 99 Hz +0.2.
- Coda pedal: 49.6 Hz −28.7 → −26.3 dB. Bars 45-52: −31.4 → −28.9.
- 20-100 Hz share −17.96 → −17.26 dB. Loud 40-100 Hz −18.23 → −17.49, under the −12.5 limit Movement I set.
- 49.6 Hz is still 5.5-7 dB under the lossless recordings, so "solid but not boomy" holds. The rest of the gap is the samples' weak fundamentals (LEARNINGS §14); do not chase it with gain.

## 4. Wetness: inside Dan's "too wet" limit and at the dry end. Change nothing (measured)

- **Few clean stops.** This movement has almost none: no point where four or more tracks stop together with 0.45 s of silence after, except the final chord.
- **The final chord**, measured from the written end (qn 304) against the 0.3 s before it:

  | Time after the end | +0.15 s | +0.3 s | +0.45 s |
  |---|---|---|---|
  | c47 | −5.5 dB | −15.8 dB | −24.4 dB |
  | c43 (before the template) | | −12.5 dB | |

  It reaches −20 dB at 0.38 s (c43: 0.42 s). The recordings fall 13-17 dB by +0.3 s and take 0.43-0.55 s to fall 20 dB. The returns carry 5 % of the chord's tail energy in the 0.15-0.45 s after the cut-off.
- **Return levels** against their family's dry sum (whole piece):

  | Return | Mockup | Finale (c08 render, after its wetness fix) |
  |---|---|---|
  | R Strings | −23.7 dB | −13.2 dB |
  | R Brass | −13.1 dB in the horn solo | −14.6 dB |
  | R Winds | −12.5 dB | −13.1 dB |
  | R Perc | −7.6 dB | −7.7 dB |

  The strings take their room from their own full-width Main pair (c45 C #2).
- **Raising R Strings does not move the tail much.** Simulated on the final chord: +3 dB → −20 dB at 0.39 s; +6 dB → 0.41 s; +11.5 dB → 0.50 s.
- **For whoever takes item 7.** The return faders are not the means to reach the recordings' 0.43 s; the chord's own release is (FINAL_RING or a shallower fade). Keep within the 0.45 s limit.
- **If Dan hears c48 as dry**, R Strings is the fader to raise. Without his word, leave it.

## Do not touch

- The four returns, their faders, the IR envelope (2 / 0.5 / 0.5) and the 160 Hz return high-pass (final chord −15.8 dB at +0.3 s, −20 dB at 0.38 s).
- No hall sends from trombones, tuba, bassoons, contrabassoon and basses.
- The c45 side EQ on the 14 Main tracks and the basses' 100 Hz −15 side shelf (master side/mid −5.45 dB, correlation below 250 Hz 0.63, 250 Hz-5 kHz 0.55: the references' values).
- The c46 brass bells at 475 / 821 Hz / 3.2 kHz.
- The string 1 kHz −2.5 bell; the winds' 1 kHz −3.1 bell (item 11 measured, not needed).
- Trombone widths and pans at the template seats.
- The DIV tracks' extra hall.
- The re-bow layout (no loop pulsing on any held passage).
