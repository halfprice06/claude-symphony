# Cycle 05, critic C: blend and space (Lens C1), on the c04 render

I ran my scripts on `cycles/c04/render/` (all 31 stems and the master, 48 kHz float), `build/parts.json`, `build/mix.json`, `build/roles.json` and the generated Opus states in `jobs/*.b64`. I read the states with `opus_state.split` and wrote nothing. The time map comes from parts.json `tempo`. The reference is the Dvořák 9/i MP3, decoded with ffmpeg, plus the Brahms band shares stored in `measure.py`. "A" means A-weighted level, and every other level is plain RMS. "Hi-mid tilt" is the 2-8 kHz energy relative to 0.5-2 kHz.

## Manual notes (L2: May 2021 HO Opus manual, PDF pp. 219-223, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.219: Algoverb is an algorithmic stereo reverb insert with pre-delay, size, decay, density, early/late, bandwidth, low/high, stereo and mix controls. | Not used. Every instance carries the convolution Reverb on `fx:0`. | Yes. No algorithmic reverb is needed while one IR is shared. |
| p.220: the convolution Reverb's controls are Input Gain, Pre-Delay, Send Mono, Response (the IR, true stereo available), Bandpass high/low cut, **Width (100% default, up to 200%)**, Wet (-120 to +6 dB) and Dry. | All 31 states read back the same values: IR "S. Cal Hall Perc TS FR 3.3s", trueStereo on, sendMono off, delay 30 ms, high cut 5.5 kHz, low cut 160 Hz, wet 2.0 (+6 dB, the maximum), dry 1e-6 (fully wet, correct for an fx bus), width 1.0, fx return 0.095. | Yes. Width has never been changed, and build_reaper has no key for it (finding 5). |
| pp.220-221: IR Envelope Preprocessing offers No / Simple / Full envelopes. Full sets start and end times plus fade-in and fade-out time and curve, and shortens or shapes the IR. | `reverb.ir_setup` envelopeMode 2, endPos 0.5, decayLength 0.5 (Movement I c44, scherzo c03). | Yes, but the setting is too short for this hall. The G.P. decays at about T60 1.2 s, under the brief's 1.5-2 s (finding 1). |
| p.222: mixing the mic positions moves the sound from dry to wet. The recorded room "is heard as long as the samples are playing (including the release trail samples)". | The release caps (strings 150 ms at mf-ff and 350 ms at pp/p, horns 237 ms) cut the recorded room on the Main mics at every cut-off. After that only the convolution tail rings. | Yes, as designed. It is one reason the G.P. goes quiet so fast (finding 1). The caps are per row, so they cannot be lifted for one chord. |
| pp.222-223: three mic workflows: one mic per pass then mix, several mics at once mixed inside Opus, or several mics routed to separate outputs. | The pipeline uses the second one: Close plus Main per instance, mixed inside Opus. The DIV A solo and DIV B violas load Close only. `--pass2` exists for memory. | Yes. The DIV tracks' Close-only sound is the tone mismatch in finding 2. |

## Findings, ranked by what a listener would hear

### 1. The G.P. after the fff summit (bar 340, qn 1015.8-1020) is dead silence after half a second: the hall now dies faster than any hall (measured)

What is wrong: the brief says "the hall must ring into the silence" of the G.P. The c04 timpani damp did its job: the drum no longer fills the G.P. But it showed that the orchestra's own hall barely rings. The fff cut-off is followed by about 0.5 s of tail and then about 1.3 s of digital silence. The same short tail ends every phrase that stops into a rest (bars 132 and 288).

Evidence (measured):
- Master level relative to the last chord's body, at +0.1 / 0.2 / 0.3 / 0.45 / 0.6 / 0.8 / 1.0 / 1.3 s after the last note-off (qn 1015.81). The slope is fitted over -12..-40 dB.

  | cycle | +0.1 | +0.2 | +0.3 | +0.45 | +0.6 | +0.8 | +1.0 | +1.3 | slope |
  |---|---|---|---|---|---|---|---|---|---|
  | c04 | 10.9 | 16.4 | 21.8 | 31.4 | 37.0 | 43.5 | 50.3 | 58.5 | 50 dB/s (T60 1.2 s) |
  | c03 | 10.4 | 14.8 | 18.5 | 21.1 | 23.5 | 26.8 | 29.5 | 33.8 | 17 dB/s (mostly the drum's ring) |

- From the start of the G.P. (qn 1017) the master sits at -41.5, -55.9, -66.8 and -75.1 dB at 0, +0.3, +0.6 and +1.0 s, against a chord body of -18.1. The loudest remaining stem at +0.3 s is Violins II at -64 dB.
- The c03 actor measured the orchestral late decay without the drum at T60 1.12 s (loop LEARNINGS c03).
- Targets and references:
  - The brief asks for a late decay of 1.5-2 s.
  - In the Dvořák reference, four tutti cut-offs fall 13-17 dB at +0.3 s and 15-24 dB at +0.6 s. The mockup gives 22 and 37 dB.
  - Movement I with endPos 0.5 gave 17.8-20.8 dB at +0.3 s.
  - Movement II had the same problem (late decay 1.17 s after Dan's S4) and moved to endPos / decayLength 0.7 at its c40 (its mix.json `_doc`). With the same 150 ms caps it then measured 21.4 dB at +0.3 s, a hall plateau at -24..-31 dB out to 0.8 s, and a 37 dB/s fall to the floor at 2.0 s (Movement II LEARNINGS).
- Bars 132.2 and 288.2: the master falls 20 dB in 0.3 s into the half-bar rest.

Fix: in `build/mix.json` `reverb.ir_setup`, set endPos 0.5 to 0.7 and decayLength 0.5 to 0.7 (mode 2 unchanged), Movement II's c40 value. Leave fx_volume 0.095, the 160 Hz low cut, the IR, wet, the sends and the release caps alone: this changes the tail's length, not its level. It is an Opus state change, so all 31 tracks need a full rebuild.
- Targets at the G.P.: master at least 13 dB down at +0.3 s (Dan's floor), about 24-31 dB down at +0.6 s, and still audible (no more than 45 dB down) at +1.0 s.
- Then re-check the S1 master pair dips in 105-120, 305-320 and 329-336. Movement I measured only about 1 dB more fill at 0.3 s for endPos 0.65 against 0.5.
- c03 listed ir_setup as do-not-touch because the value is shared with Movement I. Movement II has already left that value for the reason measured here. If the actor will not change a shared value alone, the coordinator should decide.

### 2. The two Close-only DIV tracks are brighter and narrower than the sections they belong to; the violas' div. upper voice is also louder (bars 209-224 and 349-356; Violas div on DIV B, Violin I solo on DIV A) (measured)

What is wrong: in bars 209-224 one viola section plays two voices. The upper voice (DIV B, Close mics only) sounds like a separate, close-miked group in front of a wide, distant section: brighter, near mono and, in bars 217-224, louder. The bar 349-356 solo on DIV A has the same brighter, point-like Close sound against the Violins I section's sound everywhere else.

Evidence (measured, stems):

| window (qn) | track | A level (dB) | hi-mid tilt (dB) | L/R correlation (0.3-8 kHz) |
|---|---|---|---|---|
| 624-648 | Violas div | -50.9 | -9.2 | 0.95 |
| 624-648 | Violas | -51.3 | -12.5 | 0.70 |
| 648-672 | Violas div | -47.0 | -7.8 | 0.95 |
| 648-672 | Violas | -50.5 | -12.6 | 0.70 |
| 1044-1068 | Violas div | | +3.5 dB over the section | 0.93 |
| 1044-1056 | Violin I solo | | -1.9 | 0.95 |
| 1056-1068 | Violin I solo | | -0.7 | 0.95 |
| 528-552 | Violins I section | | -5.2 | 0.46 |
| 1089-1110 | Violins I section | | -4.9 | 0.46 |

- In 648-672 the div upper voice is 3.5 dB over the section.
- c01's fix, Violas div width 0.3 to 0.45 with a side high shelf +3 dB, did not change the correlation (whole-stem 0.97 now, target 0.65-0.70). Panning a near-mono close pair wider does not decorrelate it (inferred from the numbers).
- The solo's tilt is 3.3-4.2 dB over the section's. Both tracks already carry the same 5 kHz -4 dB shelf.

Fix (`build/mix.json`; ReaEQ only, so `--mix-only` is enough):
- **Violas div:** add `{"band": "highshelf", "hz": 2000, "db": -4}` to `eq` (its only band is the highpass). In `build/roles.json`, add Violas div `[648, 672, -3]` (bars 217-224).
- **Violin I solo:** change the eq `highshelf` from 5000 Hz -4 to 2500 Hz -5.5. ReaEQ has one highshelf band per track (build_reaper band 3), so replace it rather than add a second.
- **Targets:** Violas div within -1..+1 dB of the Violas stem (A-weighted) in every two-bar window of 209-224, and hi-mid tilt within 1.5 dB of the section in both tracks.
- **Then re-check the solo against Flute 1:** it is 4.3 dB over the flute now (A -41.2 against -45.5). If the shelf takes it under 3 dB, raise the solo role at 1044-1068 from +7 to +8.
- **Width (optional, inferred):** the only tool left in Opus is Stereo Double on the Close channel (manual p.141, noted by the c01 critic C). Try it only on these two tracks and keep it only if their correlation falls toward 0.75.

### 3. In the ff tutti statements the two flutes a2 are the loudest melodic voice, and the tutti is too bright at 1-4 kHz rather than heavy at 200-500 Hz (bars 105-120, qn 312-357, and 305-320, qn 912-957; Flute 1, Flute 2) (measured)

What is wrong: the theme should come from the full string sections with the flutes adding an octave of colour above. In the render the unison flutes, two point sources (width 0.05, correlation 0.97-0.98), sit on top of the violins. The tutti's treble excess comes from them.

Evidence (measured):
- Flute pair against Violins I, A-weighted, by window:

  | qn | flute pair minus Violins I |
  |---|---|
  | 312-324 | +3.1 dB |
  | 348-358 | +4.1 |
  | 912-924 | +1.8 |
  | 936-948 | +2.5 |
  | 948-958 | +2.7 |
  | 324-336 | -1.1 (the one window where Flute 1 plays 5.7 dB under Flute 2 on the same unison notes) |

- The flutes supply 51% (312-358) and 56% (912-958) of the stem energy at 1-2 kHz, against 23-26% for both violin sections together.
- Master, loudest 10% of frames, band shares against the Dvořák reference's loudest 10%:
  - 120-250 Hz -8.2 against -6.4
  - 250-500 Hz -7.2 against -6.4
  - 1-2 kHz -5.9 against -7.2
  - 2-4 kHz -9.8 against -11.6
- So the loud tutti is 1.3-1.8 dB bright and 0.8-1.8 dB thin in the low mids. There is no 200-500 Hz build-up to cut (the brief's S4 question): the soft 30% of frames match the reference within 0.3 dB at 250-500 Hz.
- Rimsky-Korsakov's forte ratio (a string section about 3 dB over one woodwind, mockup-kit LEARNINGS section 13) puts two flutes in unison at about the level of Violins I, not 2-4 dB over it.

Fix: in `build/roles.json`, Flute 1 and Flute 2 each `[311.5, 357.5, -3]` and `[911.5, 957.5, -3]`. These are the a2 spans read from parts.json, so the bars-121 / 277 sub. p entries are not touched. If the 324-336 window then drops below -3 dB, hold Flute 2 at -2 there.
- Targets: flute pair 0 to -2 dB under Violins I (A-weighted) in each 12-qn window, flute share of 1-2 kHz under 40%, loud-frame 1-2 kHz share within 0.7 dB of the reference.
- Do not cut 200-500 Hz anywhere, and do not raise the treble.

### 4. Below 250 Hz the master is close to mono, and the low mids are narrower than a hall (whole movement; basses, celli, timpani, low winds) (measured; fix inferred)

What is wrong: on headphones the orchestra's foundation sits as one point in the middle of the head, while the recording's bass and body surround the listener.

Evidence (measured, frames within 50 dB of the loudest):

| | 25-60 Hz | 60-120 Hz | 120-250 Hz | 250-500 Hz | 500-1000 Hz |
|---|---|---|---|---|---|
| master correlation | 0.90 | 0.88 | 0.81 | 0.70 | 0.64 |
| Dvořák correlation | 0.50 | 0.57 | 0.55 | 0.52 | 0.58 |
| master side/mid (dB) | -9.4 | -9.0 | -7.8 | -7.5 | |
| Dvořák side/mid (dB) | -4.8 | -5.1 | -5.0 | -4.9 | |

- Stem correlation at 25-250 Hz: Double basses 0.84-0.93, celli 0.83-0.91, timpani 0.92-0.96, contrabassoon and harp 0.99.
- c01's side-shelf reductions (basses to -4, timpani to -4) are in, and the bass is still about as mono as c00's 0.91 / 0.88.
- Cause (inferred): the 160 Hz hall low cut (Dan's S4) removes the true-stereo hall's decorrelation of everything under 160 Hz. What is left is the Main tree, whose L and R are nearly identical at those wavelengths. Wider seats cannot decorrelate them.

Fix: keep the low cut. For the 250-1000 Hz body, which the hall still reaches, add a `reverb.width` key to `tools/build_reaper.py` next to `true_stereo`. It writes the ConvolutionReverb's `width` (manual p.220: 100% default, up to 200%; the state reads 1.0). Set it to 1.5 in `mix.json`, in the same full rebuild as finding 1. It changes no levels and no sends.
- Target: master correlation at 250-500 / 500-1000 Hz of 0.58-0.62, with the seats (R-L at 1-4 kHz, listed below) within 1 dB.
- Below 160 Hz, accept about 0.85. Do not lower the basses' or celli's side shelves further, because Movement I's -6 dB had made the bass more mono than the references.

### 5. The timpani supply a quarter of the tutti's low end with felt sticks where the score prints hard sticks (bars 101-120 and 301-320 at f/ff) (measured share; fix inferred, MANUAL-GAPS #6)

What is wrong: in the tuttis the drum is a soft, boomy low-end layer, while the score asks for the hard sticks' definite stroke from bar 1 to 340. That part of the low mids reads as boom, not pitch, under the celli.

Evidence (measured, tutti 312-358 / 912-958):
- The timpani supply 27% / 26% of 30-100 Hz and 23% / 25% of 100-250 Hz. In the 100-250 Hz band that is more than the basses (14% / 13%) and second only to the celli (50% / 52%).
- Each stroke still decays 17-24 dB before the next (40-250 Hz), so the issue is colour, not ring.
- The patch is "Timpani Flt KS" throughout (read). `Timpani Hrd KS.oib` has the same rows and keys (MANUAL-GAPS #6).

Fix (memory neutral: a patch swap, not an added instance):
- Swap the Timpani track to `Drums/Timpani/Timpani Hrd KS.oib` for bars 1-340. Keep the soft-stick coda (341-376) on Flt through a `TRACK_WINDOWS` second timpani track, or accept hard sticks for its six strokes.
- Make the "Timpani Flt *" row names in `score_to_parts.py` follow the patch stem.
- Re-measure the roll levels (`TIMP_CC1_MAP`, `TIMP_ROLL_TRIM_DB`) and keep `TIMP_DAMP_AT` 1014.5 on whichever patch plays bar 339.
- Target: timpani share of 100-250 Hz in the tuttis 12-18%, with the loss replaced by the celli and basses rather than by EQ.
- This is a large change. If it does not fit this cycle, leave it to the cycle that takes MANUAL-GAPS #6.

## Standing checks (Dan's ears), measured on c04

- **Loop pulsing (item 8):** none at 3.95 s. Autocorrelation of level and spectral centroid:
  - Violins I 1089-1125: 0.06 / 0.01.
  - Horn 3 drone 456-504: -0.12 / 0.09.
  - Violins I 0-23: -0.19 / -0.51.
  - Celli 1070-1090 and Violins I 420-444 are too short to test.
- **S3, sub. p at 121 and 277:** the master steps down over 358-360 (-20.4 to -38.2 dB) and over 826-828 with no sudden cut. The only vol_db step over 3 dB near a subito is Violas at 826.5-827.5 (-4 / 0 dB, inside the rest before 828).
- **Same hall for every family:**
  - Median stem drop 0.3 s after a note end into a rest: woodwinds 21-27 dB, horns 17.5-23, trumpets 22.6-26.2, trombones and tuba 21-25, strings 19-24.
  - At the G.P., from body to +0.3 s, trumpets, horns and trombones all fall 33-35 dB.
  - The trumpets and horns are in one room.
- **Seats** (R-L at 1-4 kHz, coherent left to right): Vln I -8.3, harp -10.4, horns -5.3..-8.1, flutes -4.5, Vln II -4.0, clarinets -3.1, bass clarinet -1.8, timpani +0.5, trumpets +1.2/+1.6, violas +1.6, bassoons +2.3/+3.1, cor anglais +3.9, oboes +4.7/+6.1, trombones +5.4..+6.6, celli +6.6, tuba +7.6, basses +8.1. Master 1-4 kHz correlation 0.65; Dvořák 0.68 at 2-4 kHz.

Do not touch: the shared true-stereo hall (IR, fx_volume 0.095, wet 2.0, 160 Hz low cut, 5.5 kHz high cut, sends; only the IR envelope length in finding 1 and the hall width in finding 4 should change), the seats above, `TIMP_DAMP_AT` 1014.5 (pre-hall), the solo / flute / celli roles at 349-356 (flute 4.3 dB under the solo), Violins II's con sordino window, the re-bow fills (no pulsing), the release caps, and the trumpets' and horns' sends.
