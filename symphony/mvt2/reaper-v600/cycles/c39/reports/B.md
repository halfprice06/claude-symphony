# Cycle 39, critic B: balance and levels (on the c38 render, the first with the drier hall)

**Method.** Stems and master from `cycles/c38/render/` (after the c38 stem fix), compared with `cycles/c37/render/`. Note data from `cycles/c38/rendered_build/parts.json`, time base the parts.json tempo map. Levels: 4096-point Hann spectra, 2048 hop, both channels' power summed, 1/3-octave bands, and an approximate K-weighting (38 Hz high-pass plus a +4 dB shelf above 1.5 kHz). K values have an arbitrary offset, so only differences matter. A-weighted figures are given where low instruments are compared with high ones. Simulations apply dB gains to stem frames and re-sum the master; they ignore the hall, so trust them to about 1 dB. "Measured" means a number from the render or parts.json; "inferred" means a judgement about what a listener hears.

## Manual notes (B6: May 2021 HO manual pp. 32-34, 43, 46, 191-192; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.32-33 Streaming: preload size by drive type, "Never Preload" streams everything | Render-to-render level changes on unchanged tracks; the samples must be in RAM before the render | Yes. `render_cycle.py` waits for the samples and renders 1x offline. c38 rebuilt every track (hall change), so no unchanged-track comparison exists this cycle. |
| p.33 Multi-threading; output configuration (1-16 stereo busses per plugin instance) | One instance per track, one stereo output, the hall inside each instance | Yes. Every stem is self-contained, so the master is the stem sum, which the simulations below rely on. |
| p.34 MIDI preferences: Round Robin Reset Controller / Reset Note | Repeatability of per-note levels (pizz. and harp round robins differ by up to about 6 dB, kit LEARNINGS 13) | Not followed. Opus is set to CC16 and the pipeline sends CC36 (MANUAL-GAPS #10, still open). Not a level fault this cycle. |
| p.43 Purge states; the instrument Volume slider is the same control as the Mix page fader | Where track level lives | Followed. Levels live in REAPER track gain, the volume envelope, CC7 and mix.json mic volumes; the Opus instrument fader stays at the patch default, so a rebuild reproduces it. |
| p.46 System usage (voices, CPU, RAM, disk) | REAPER memory record | Followed: c38 CHANGES records 44 GB settled and 45 GB at quit. |
| p.191 All Instances window: purge per articulation of a KS Master | Unused rows | Followed in script by `UNLOAD_UNUSED_ROWS`. |
| p.192 Voice Limit per instrument ("raise the Voice Limit" if voices drop); Octave; Key Range | Two-note chords on one track: Violins I div. at 210 (bar 62), violas 262-269 and the coda | No sign of dropped voices (measured): Violins I at 210-211.5 is 6-8 dB under the master, its loudest point in bar 62; violas 266-268 stay within 2 dB of 262-265; in the coda the two viola halves and both cello tracks stay within 2.5 dB of each other on every 2 qn step. Octave and Key Range are not used and not needed. |

## 1. Bars 79-80 (qn 263.9-265.9): the melody's top octave drops 2-6 dB under Violins II at the ff cadence (measured)

**Where.** Violins I and Flute 1 hold B flat 6 from 262 (tied into 265, up-bow printed at 265), Violins II, Oboe 1 and Clarinet 1 the same line an octave lower. All ff.

**Evidence (measured).**
- K level per 0.25 qn: from 262.0 to 263.75 Violins I is 1.5-6.5 dB over Violins II (for example 263.75: 40.9 against 37.4). Violins II's automatic re-bow starts at 263.921 (Sus MAX, v96) with no fill. Its level jumps to 41.2-44.2 and stays there to 265.75. Violins I re-bows at 264.417, and its fitted fill (`build/rebow_fills.json` Violins I "264.417") falls to its -6.0 dB floor from +0.76 s to +1.12 s and sits at -4.4 dB to +1.76 s. Over 264.75-265.75 Violins I reads 37.9-39.1 against Violins II 42.3-44.2: **4.6 to 6.3 dB under**.
- Group sums against the master at 265: top octave (Violins I + Flute 1) -9.0 dB, lower octave (Violins II + Oboe 1 + Clarinet 1) -4.7 dB.
- Violins II's vol_db also steps from -2.58 to -0.31 dB at 265 (role end), adding to the bloom.
- c37 shows the same pattern (Violins I -10.9 against Violins II -6.0 at 265). This is not a hall effect.

**Why it matters (inferred).** On the downbeat of bar 80, the high point of the second climax, the listener hears the lower octave of the melody and loses the B flat 6.

**Fix (level only).**
- Violins II: CC7 lane (pre-hall, so no tail is cut) 127 to 76 (-4.5 dB) over 263.95-264.0, held to 265.75, back to 127 at 265.80 (the 266 note starts at 265.81). Use the `CC7_LANES`/CC7 table that c38 used for the celli at 184 and 186.
- Violins I: in `build/rebow_fills.json` "264.417", add +2.5 dB to every point from 0.6 s to 1.763 s (the -6.0 floor becomes -3.5, the -4.4 tail becomes -1.9). Keep the first 0.56 s, which levels the re-bow attack.
- Simulated (K, re master): 264.75-265.5 Violins I -6.0 to -8.4, Violins II -9.2 to -10.5, so Violins I is now 1-4 dB over Violins II. The master falls 0.3-0.6 dB over 264-265.5, which only widens the gap below bar 61 (the climax order holds).
- Better, if the articulation critic agrees: move both re-bows to the printed up-bow at 265.0 (`REBOW_AT`, removing the automatic points 264.073 and 263.897 from `rebow_moves.json`), then refit with `fit_rebows.py`, levelling each new piece to its section's 262-263.9 body. The players change bow there anyway.
- **Check:** Violins I at least 1 dB over Violins II on every 0.25 qn from 262 to 265.75.

## 2. Bars 61-62 (qn 205.0-207.75): at the ff climax the Violins I melody is level with or under five other parts for two and a half beats (measured)

**Where.** The melody is Violins I: C sharp 6 at 204, repeated at 206, then E sharp 6 at 208 and the divided chord at 210. Under it are Horn 1 and 2 (ff), Trombone 2 (f, a tenor counter-line), bass trombone, celli and Bassoon 1.

**Evidence (measured, K, each part re master, per 0.5 qn).**

| qn | Vln I | Vln II | Horn 1 | Tbn 2 | B. tbn | Vc |
|---|---|---|---|---|---|---|
| 204.0 | -6.7 | -8.8 | -13.0 | -12.0 | -11.1 | -12.0 |
| 205.0 | -9.3 | -11.1 | **-9.0** | -10.5 | -9.8 | -9.2 |
| 205.5 | -10.4 | **-9.0** | -10.6 | -9.7 | -9.6 | -10.3 |
| 206.0 | -11.2 | **-6.9** | -9.3 | -9.1 | -11.2 | -10.3 |
| 207.0 | -9.5 | -9.2 | -10.7 | -9.7 | -12.3 | -13.9 |
| 207.5 | -8.6 | -9.6 | -8.7 | -8.7 | -16.7 | -12.7 |
| 208.0 | -7.5 | -12.6 | -13.4 | -8.9 | -12.6 | -10.3 |

- The repeated C sharp 6 at 205.949 plays Sus MAX at v96 (the other melody notes are at v105-108) and enters 4.5 dB under the 204 note.
- Horn 1's c37 shape (`build/score_config.py` l.784) lifts it +7.5 dB from 205.0 to 207.75, exactly the span where the melody sags.
- Violins II's 206 note (moved to 205.775) blooms 4 dB over its 204 note.
- The timpani and low brass do not cover: the roll is 14-24 dB under the master, the tuba 11-18 dB under. The c37 brass +3 is not the cause (Trombone 2 and bass trombone are 1-2 dB under Violins I outside 205-207.5).

**Why it matters (inferred).** For two and a half beats of the movement's one Largamente ff the tune disappears into the middle voices. It returns at 208.

**Fix (`build/score_config.py`).**
- `LEVEL_SHAPES["Violins I"] += [[(204.9, 0.0), (205.15, 3.0), (207.6, 3.0), (207.8, 0.0)]]`. This is a rise, so it is safe for S3. Alternative: raise the 205.949 re-attack's velocity to 105, in line with its neighbours, and re-check its level.
- Line 784, Horn 1: 205.0 7.5 -> 5.5 and 207.75 7.5 -> 5.5. Its front (c36) and the 208-211.6 +3 stay.
- Violins II: CC7 127 -> 95 (-2.5 dB) over 205.85-207.0, back to 127 by 207.6.
- **Simulated.** Over 205.0-207.5 Violins I goes to -6.6 to -8.1 dB re master, 1.0-3.5 dB over the next part on every half beat. The master changes by -0.2 to +0.3 dB, so the limiter is unchanged within 0.3 dB.
- **Check:** Violins I is the loudest stem (K) on every 0.5 qn from 204 to 211.5 except the Violins II attack at 205.8 (at most 1 dB over).

## 3. The ff tutti has too little bass: at bars 61-62 the 56-225 Hz region is 2-4 dB under the most bass-light reference, and the low E/F sharp fundamentals are almost missing (measured; the judgement of "solid" is inferred)

**Evidence (measured; band level relative to the 450-1800 Hz band).**

| | 56-140 Hz | 112-225 Hz | 35-56 Hz |
|---|---|---|---|
| c38 bars 61-62 | -11.5 | -7.5 | -37.3 |
| c38 bars 79-80 | -11.8 | -7.6 | -35.4 |
| Dvorak 9/i, loudest 10% of frames (lossy MP3, known to be light below 100 Hz) | -9.2 | -3.3 | |
| Brahms 1/ii, 4/ii (lossless, whole movement) | -3.9 / -2.1 | -7.4 / -4.8 | |

- Over the whole movement the mix's 125-200 Hz is 1.8 dB under the mean of the three references, and 3.8 dB under Dvorak in its loud frames.
- The drier hall did not cause this: c37 bars 61-62 read -12.5 / -7.3. The hall return carries little energy, and the master fell only 0.6 dB K when it was halved.
- Who supplies 56-225 Hz in bars 61-62: basses 46%, celli 24%, tuba 15%, bass trombone 6%. The basses play C sharp 2, F sharp 1, E1 here, the pitches whose fundamental the Basses KS Master records 12-30 dB under the harmonics (kit LEARNINGS 14). On top of that, the basses' `loud_eq` has a 100 Hz -3 dB low shelf, which series 1 c21 added when the basses stood 7.5 dB over Dvorak below 100 Hz. That is no longer the case.

**Fix (`build/mix.json`, the loud spans only, so soft passages keep their spectrum).**
- Double basses `loud_eq`: lowshelf 100 Hz -3 -> 0 dB (or remove the band); keep the 150 Hz +4 bell and the static 80 Hz -6 bell2, which handles D2/F2 boom and is not needed on these pitches.
- Violoncellos `loud_eq` bell 150 Hz +4 -> +5.5.
- Tuba: `LEVEL_SHAPES["Tuba"]` +1.5 dB over 204.15-211.6 (on top of c37's +3). Rimsky-Korsakov's forte ratio (tuba = two horns) allows it, and the tuba is 11-18 dB under the master there.
- Expected: about +1.5 to +2.5 dB at 56-140 Hz and +1.5 dB at 112-225 Hz at the climaxes only.
- **Check:** 56-140 Hz at bars 61-62 between -10 and -8 dB re 450-1800 Hz; 63 Hz third-octave not over Dvorak's loud frames by more than 2 dB; delivery limiter still at or under about 2.5 dB.

## 4. Bars 66-70 (qn 226-238): the basses' 4-soli E flat pedal sits 14-18 dB under Horn 1's p-mp solo, 19.5 dB A-weighted (measured; audibility inferred)

**Where.** Horn 1 enters at 226 (p dolce, cresc. to mp at 229). The basses hold the pp E flat pedal ("4 soli, sul A"); the timpani play a ppp roll near the rim.

**Evidence (measured).**
- K per qn, 226-235: Horn 1 26.5-31.5, basses 12.5-14.8, timpani 6.4-12.0.
- 226.2-229.8: Horn 1 23.9 dB A-weighted against basses 4.4 (flat 29.5 against 13.1).
- The basses are played by the full section at -3 dB (`SOLI_AS_META`) plus c32's 4-soli -3 dB. pp against p/mp is one to one and a half printed steps, about 5-8 dB on this mockup's scale (about 4.8 dB per step), not 14-18.

**Why it matters (inferred).** The pedal that holds the retransition together is close to inaudible at headphone level. The passage reads as a horn alone, and the bass reappears only at 238.

**Fix.**
- `build/score_config.py`: `LEVEL_SHAPES["Double basses"] += [[(226.0, 0.0), (226.5, 3.0), (237.6, 3.0), (238.0, 0.0)]]`. It starts with Horn 1's entry, after c38's niente cut (224.5-226.25), so that shape is unchanged. It ends on the tutti note at 238, which is a new onset, so no tail is cut.
- Expected: basses 11-15 dB under Horn 1 (K), timpani 4-8 dB under the basses. Dan's roll rule (BRIEF 5) still holds.
- **Check:** in the master the bar 66 niente still falls at least 7 dB (223 -> 225.5).

## 5. Extra check: 200-500 Hz build-up after the drier hall (measured; recommendations inferred)

**Result: no master-wide build-up.** 200-500 Hz relative to 450-1800 Hz:

| | all frames | loudest 10% | soft frames (p10-p50) |
|---|---|---|---|
| c38 | -2.4 | -2.3 | -1.3 |
| c37 | -2.2 | -2.0 | -1.6 |
| Dvorak 9/i | -2.5 | -2.8 | -2.9 |
| Brahms 1/ii / 4/ii | -4.0 / -2.8 | | |

- The drier hall left this band within 0.3 dB.
- The one single-band peak is the 315 Hz third-octave: -5.9 against -8.8 (Dvorak) and -11.2/-9.9 (Brahms). That band covers E flat 4 to F4, the dominant of A flat major with its neighbours, so it is mostly the key, not the mix.
- The soft frames are 1.6 dB heavier at 200-500 Hz and 1.7 dB lighter at 2-5 kHz than Dvorak's soft frames.

**Where the low-mid weight concentrates (measured, 200-500 Hz re 450-1800 Hz per passage).**
- Horn 1's solos: bars 7-14 +1.6 (c37 +0.7), bars 65-70 +2.7, against -2.2 to -6.5 elsewhere. Their 2-4.5 kHz sits at -24 / -13 dB. Horn 1 supplies 73-75% of the band there.
- This comes from the soft-horn `loud_eq` high shelf (800 Hz -8 dB, c37 C #1) on top of CC1's soft layers. The fundamental (E flat 4 to A flat 4) is left to dominate.
- The other heavy contributors are low pedals whose harmonics fall in the band, which is normal for these voicings: coda celli div +13 and Clarinet 2 +9, violas +3 to +5.5, harp +8 to +12.

**Recommendation.**
- Make no master or bus cut at 200-500 Hz. The band matches the references, and the 125-225 Hz region below it is already light (finding 3).
- If Dan still hears the horn solos as thick or muffled, do not undo the 800 Hz shelf. Instead add a 300 Hz -2.5 dB bell (1 oct) to Horn 1's soft `loud_eq` spans (the same points as the existing shelf). Simulated on the c38 stems (Gaussian bell, about 1 octave wide), it brings bars 7-14 from +1.6 to +0.4 and bars 65-70 from +2.7 to +1.3, and leaves 1-5 kHz where c37 put it. This follows Dan's request: a cut in the low mids, not a treble boost.

## 6. Exposure without the hall: the wind and horn phrase ends now decay faster than a real hall, and 6-8 dB faster than the strings (measured; "exposed" inferred)

**Evidence (measured; drop from the last 50 ms of a note to +0.30 s, median per stem, notes followed by at least 1.4 s of silence, c37 -> c38).**
- Flute 1 11.3 -> 16.3, Oboe 1 12.7 -> 18.2, cor anglais 13.7 -> 19.4, Clarinet 1 11.3 -> 16.1, bass clarinet 16.3 -> 22.9, Bassoon 1 14.8 -> 18.8, Horn 1 16.5 -> 21.5, Horn 3 14.5 -> 20.3, tuba 15.5 -> 22.4, harp 14.7 -> 22.0, Violin I solo 14.9 -> 19.2.
- Against those, Violins II 12.1, celli div 13.6 and violas div 9.7 (the strings' own release samples carry them).
- The recordings measured 13-17 dB.
- Exposed phrase ends over near-silence:
  - Horn 1 end of bar 14 (qn 39): 22 dB;
  - bass clarinet 39 and 271: 23 dB;
  - cor anglais end of bar 36 (108): 22 dB;
  - solo violin 53: 21 dB;
  - Oboe 1 47 and 59: 17-18 dB.
- c29 critic C measured a 5.5 dB wind/string depth gap and closed it with the wind send (0.35 -> 0.6). With the hall return halved, the gap is back at about the same size.
- The levels themselves held: no solo lost more than 1.8 dB K, and every solo margin in the lens list is within 1 dB of c37.

**Why it matters (inferred).** Phrase ends of the solo winds and horn stop short and dry while the strings still have their room. This is most audible in bars 7-14 and 31-36 (no strings) and at bar 36 into the B section.

**Fix.** The c38 do-not-touch line rules out raising sends, and Dan asked for less hall. So use the Opus mics, which carry the stage room's own short reverberation rather than the 3.3 s convolution tail:
- `build/mix.json` groups: `wind.mics` Close 0.5 -> 0.35, Main 0.8 -> 1.0; `horn.mics` Close 0.5 -> 0.4 (Main stays 1.0).
- Re-match each track's gain to its c38 K level on its solo bars (expect about -1 to -1.5 dB).
- Cost: an Opus state rebuild of 11 wind and 5 horn tracks (mic volumes only, no new mics loaded, memory neutral). Fitted fills on those tracks need the usual overshoot check after the render.
- If the actor's cycle is already full, ask Dan first whether he hears the solo phrase ends as clipped; he asked for drier, and this is a matter of degree.
- **Check:** wind and horn median drop at +0.3 s 14-17 dB, master RT60 (-20..-40) still under 2 s.

## Other lens checks (measured, no action)

- Solo margins over the accompaniment sum (K, per bar):
  - Horn 1 bars 7-14 +0.5..+4.7, nearest single part 4.6 dB under;
  - Oboe 1 / solo violin bars 15-21 +2.6..+6.8;
  - bass clarinet 31-36 +1.4..+6.2, with the cor anglais' p dolce counter-line 2.9-4.2 dB under;
  - Flute 1 37-40 +1.7..+4.0;
  - cor anglais 41-44 +0.5..+1.8, with Flute 1's counter-line 3-5.5 dB under (c37 B #5 as intended) and the strings 6-8 dB under;
  - Oboe 1 45-47 +0.3..+1.7 (strings 6.6+ dB under);
  - cor anglais 48-51 +1.4..+4.8;
  - Clarinet 1 85-86 +3.2/+4.0. In bars 87-88 Clarinet 1 sits level with the cor anglais' pp dolce chromatic line (within 1.4 dB). Both print pp dolce and the moving voice is the cor anglais', so this is acceptable. Bar 89 hands its C5 to Violins I.
- Timpani never above rank 9 in bars 61-64 or 79-82, 14-24 dB under the master in bars 61-62. The bar 63-64 trombone quotation is 9-20 dB over the strings' printed sf > p, as printed.
- Divisi and soli tracks: the viola halves (bars 23-30, 80-81, coda), the celli div pedal against the celli, and Violins II div are within 2.5 dB of their partner sections at the same dynamic.
- Fast vol_db falls under held notes: only fill tails right after attacks were found (scan of every track, drops of 3 dB or more within 0.15 qn). No new S3 cut.

**Do not touch:**
- fx_volume 0.095 and the 160 Hz hall low cut;
- the c38 bar 81 holds to 271 and the bar 54-57 string shape;
- c37's bars 61-62 brass +3, except Horn 1's 205-207.75 lift as in finding 2;
- the Violin I solo level and CC1 72;
- the coda divisi balance;
- the timpani roll levels in bars 61-62 and 67-70;
- the Clarinet 1 coda CC7 cuts;
- Flute 1's bars 42-44 counter-line level.
