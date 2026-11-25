# Cycle 41, critic C: blend and space (one room), on the c40 render

Render under review: `cycles/c40/render` (master and 32 stems after the c40 stem fix), `cycles/c40/rendered_build/` (parts.json, mix.json), compared with c36-c39 and with the reference recordings: the Dvořák 9/i MP3 (decoded and measured with the same scripts) and the stored metrics of Brahms 1/i, 4/i, 1/ii, 4/ii (`symphony/render/critics/c00|c04/ref_*/metrics.json`, made with `symphony/render/tools/rtk.py`). I used rtk's own functions (`stereo_stats`, `env_db`, `cutoff_decays`, `decay_fit`) through `/usr/bin/python3` (the project venv has no scipy), so the mockup and the references are measured with the same code. Scripts were in `/private/tmp/claude-501/mockup-loop/mvt2-c41-C/` (deleted at the end). Each judgement below is marked measured, simulated (applied to the c40 stems, whose sum is the master) or inferred.

## Manual notes (cycle 41, slot C: L2, May 2021 HO manual PDF pages 219-223)

| Page | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.219 | Algoverb: an algorithmic stereo reverb with a Stereo control (50% default, 100% wider) | not used; the shared hall is the convolution Reverb | n/a |
| p.220 | Reverb (convolution): Input Gain, Pre-Delay, Send Mono, Response (IR), IR Envelope, Bandpass with High Cut / Low Cut (30 Hz-18 kHz), **Width 100% default, up to 200%**, Wet, Dry | `mix.json reverb`: true-stereo "S. Cal Hall Perc TS FR 3.3s", wet 2.0, high cut 5.5 kHz, **low cut 160 Hz**, width left at default | Yes. The 160 Hz Low Cut means the hall gets no input in the band where the master's image is now narrowest (finding 2). Width 150-200% is the untried fallback for side/mid (finding 2). |
| p.221 | IR Envelope: Simple (one Decay slider) or Full (start, end, fade-in, fade-out) | `reverb.ir_setup` {envelopeMode 2, endPos 0.7, decayLength 0.7} (c40) | Yes. The envelope shortened the wind tails only a little (detector t-20 0.49 -> 0.46 s, c39 -> c40); the large change in c40 came from the release caps (finding 1). |
| p.222 | The room "is heard as long as the samples are playing (including the release trail samples)"; one mic (Main is the common choice) or a blend; each mic can be bounced in its own pass | the string sections' Main-mic release trails, now capped at 150 ms (`sus_release_cap_ms`); the Close-only DIV tracks (no recorded room at all) | Partly. The caps cut most of the recorded room from the section patches' note ends, so the sections now decay faster than the Close-only divisi halves that sit inside them (findings 1 and 3). |
| p.223 | Each mic to its own output; several instruments can share an output pair | optional | Not needed. |

MANUAL-GAPS.md read. #4 (Mid instead of Close on the winds and horns) is still untried; the ONE_TIME Main-width change (finding 2) comes before it. The memory plan is unchanged: nothing here adds an instance or a mic.

## Verdict on the hall: c40 is now drier than the recordings, not too wet (measured)

The detector rtk uses on the recordings (30 ms frames, a 0.4 s hold, then a fall of at least 15 dB within 0.4 s) finds **no tutti stop** in this Adagio, in c37-c40 alike. The same is true of the two Brahms slow movements (n = 0). I therefore ran it on every stem: each stem carries its own share of the shared hall, because the hall is inside each Opus instance. Pooled per family, with median time to -20 dB and RT60 from the -5..-20 dB slope:

| | strings | winds | horns |
|---|---|---|---|
| c37 (fx 0.19, before Dan's note) | 0.52 s / 1.66 s (n 10) | 0.58 / 1.91 (21) | 0.57 / 1.29 (4) |
| c39 (fx 0.095, 160 Hz low cut) | 0.47 / 1.15 (15) | 0.49 / 1.11 (38) | 0.46 / 1.04 (8) |
| **c40** (+ ir_setup 0.7, release caps) | **0.37 / 0.68** (29) | 0.46 / 0.88 (38) | 0.435 / 0.95 (8) |
| Brahms 1/i tutti stops (12) | 0.43-0.55 s (median 0.485) / 1.13-1.62 s (median 1.33) | | |
| Dvořák 9/i (1) | 0.49 / 1.32 | | |
| Movement I c44 tutti stops (judged right by its c45 critic C) | 0.45-0.55 / 0.85-1.70 | | |

At every phrase end followed by at least 1 s of rest (median per family, from the note-off; strings n 47, winds 56, horns 17, low brass 4):

| drop at +0.15 / +0.3 / +0.6 s; time to -20 dB | strings | winds | horns |
|---|---|---|---|
| c37 | 4.6 / 9.8 / 18.4; 0.62 s | 7.4 / 12.5 / 18.9; 0.63 | 5.4 / 11.8 / 20.0; 0.60 |
| c39 | 5.7 / 10.7 / 21.5; 0.51 | 11.5 / 17.3 / 24.0; 0.42 | 6.9 / 18.5 / 25.5; 0.36 |
| c40 | **15.0 / 21.4 / 29.1; 0.24** | 11.8 / 18.9 / 26.9; 0.34 | 10.9 / 20.6 / 28.5; 0.30 |

- c37 sat at the long end of the recordings, which fits Dan's "too wet". c39 was inside the recorded range. c40's strings are under it (0.37 s against 0.43-0.58), and their RT 0.68 s is half the recordings' 1.33.
- The winds hardly moved from c39 to c40 (0.49 -> 0.46), so the IR envelope did little. The strings fell from 0.47 to 0.37: the 150 ms release caps did that.
- Movement I's caps took the stem drop at +0.15 s to 8.5-13 dB. Here the string sections fall 15-21 dB at +0.15 s (Violins I 21.0, Violins II 20.1, violas 16.0, celli 16.1), beyond Movement I's result.
- Mush, the other half of Dan's note: no low-mid build-up (see "Low end" below), and the repeated-note dips are up (c40 S1 stem median 6.9 dB). The overlap problem is solved. The tails are now too short.

So the answer to "too dry or still too wet": **too dry at the string phrase ends and at the final chord; the winds and horns are at the dry edge of the recordings.** Finding 1 gives the fix. It is a release change, not a hall change, so the ONE_TIME's "keep the hall" still holds.

## Stereo width (ONE_TIME #2): the numbers for the actor (measured)

Master, whole movement, rtk `stereo_stats` band edges:

| | corr < 250 Hz | 20-120 | 120-250 | 250 Hz-4 kHz | > 4 kHz | all | side/mid | side/mid loud / soft | R-L < 250 Hz |
|---|---|---|---|---|---|---|---|---|---|
| c37 | 0.631 | 0.819 | 0.615 | 0.532 | 0.509 | 0.542 | -5.3 dB | -5.3 / -5.5 | +1.8 dB |
| c38 | 0.778 | 0.901 | 0.777 | 0.631 | 0.527 | 0.643 | -6.6 | -6.6 / -7.6 | +2.6 |
| c39 | 0.789 | 0.902 | 0.779 | 0.639 | 0.517 | 0.650 | -6.7 | -6.8 / -7.6 | +2.7 |
| **c40** | **0.800** | **0.901** | **0.788** | **0.642** | 0.514 | **0.657** | **-6.8** | -6.9 / -7.9 | +2.9 |
| Dvořák (decoded) | 0.550 | 0.605 | 0.548 | 0.561 | 0.525 | 0.546 | -5.3 | -5.2 / -6.4 | +3.2 |
| Brahms 1/i, 4/i, 1/ii, 4/ii (stored) | 0.541 / 0.583 / 0.601 / 0.624 | | | 0.47-0.54 | 0.38-0.48 | 0.49-0.55 | -4.7..-5.4 | | |

- Both of the ONE_TIME's conditions are met: correlation below 250 Hz is 0.80 against 0.54-0.62, and side/mid is -6.8 dB against -4.7..-5.4. The 250 Hz-4 kHz band is also narrower than every reference. **Act on ONE_TIME #2.**
- The step came with c38's drier hall and its 160 Hz low cut. The hall had been the decorrelated part of the low end, and below 160 Hz it now gets no input.
- At 35-63 Hz the Dvořák measures correlation 0.50 with R-L -0.1 dB (diffuse and centred). c40 measures 0.96 / +0.75 dB (centred but nearly mono).

## Findings, ranked by what a listener would gain

### 1. The string sections stop dead at phrase ends and at the final chord: the 150 ms release caps removed the samples' recorded room (measured; fix inferred)

**Where.** Every string-section phrase end and breath, worst on Violins I and II. Examples: the ends of the bar 23-30 theme (qn 66-90), bars 53-60, the A' phrases (bars 71-78), the coda and the final chord (qn 301-304). Tracks: Violins I, Violins II, Violas, Violoncellos, Double basses.

**Evidence.**
- Per track, c40 phrase ends, median time to -20 dB from the note-off: Violins I 0.14 s, Violins II 0.15, violas 0.22, celli 0.24, basses 0.26. The divisi and solo tracks on the same 150 ms cap but with hall send 0.5: 0.34-0.44 s (Violins II div 0.44, Violas div 0.34, Violoncellos div 0.34, Violin I solo 0.34). Winds 0.24-0.43, horns 0.23-0.47 (measured).
- Final chord, from its note-off at qn 304: master drop 18.7 / 25.5 / 35.7 dB at +0.15 / +0.3 / +0.6 s; -20 dB at **0.18 s**. c37/c38 took 0.66-0.68 s (measured).
- With rtk's `decay_fit` on the final release (the references' "tails.final"): c40 reaches -20 / -30 / -40 dB at 0.95 / 1.07 / 1.42 s, with the 10 dB from -20 to -30 in 0.12 s. Recorded endings: Brahms 1/ii 0.79 / 1.23 / 1.64, Brahms 4/ii 0.48 / 1.15 / 1.72, Dvořák 0.61 / 0.87. Their -20 to -30 dB takes 0.26-0.67 s. The movement's last sound (ppp, fermata, morendo, "via sord.") ends with a cut where the recordings ring (measured).
- p.222: the room is heard through the release trails. The section KS Masters' releases (Main mic 1.0, 323-931 ms as shipped) carried that room; the Close-only DIV patches never had it, which is why they now decay slower than their own sections (read; inferred).
- The c40 actor measured the string legato-join dip at 2.4 dB with no caps and 2.7 dB with 150 ms. So the joins barely depend on the cap, and raising it gives up little of the clarity gain (measured by c40).

**Fix (Opus state change: full rebuild of 5 tracks; mix-only data).**
- In `build/mix.json`, raise `sus_release_cap_ms.ms` from 150 to **300** on Violins I, Violins II, Violas, Violoncellos and Double basses. Keep the rows and dynamics as they are. Keep 150 on Violin I solo, Violoncellos div, Violins II div and Violas div, whose tails are already 0.34-0.44 s.
- The c40 do-not-touch on "150 ms caps on the string legato rows" rested on the joins (+0.3 dB). This change keeps the joins and fixes what the caps overshot.
- Accept when, with rtk's detector on the string stems, t-20 is 0.43-0.50 s (median) and RT is 1.0 s or more; string-section phrase ends fall 8.5-13 dB at +0.15 s (Movement I c44's range); the final chord reaches -20 dB 0.45-0.65 s after its note-off; the legato-join dip median is within 0.5 dB of c40 (2.7); and the S1 stem dip median (c40 6.9 dB) stays at or above 5 dB.
- Expected (inferred, interpolated between c39 with full releases at 0.47 s and c40 at 0.37 s): about 0.43-0.45 s.
- Knock-on: the c40 re-bow fills were refitted on 150 ms tails. Longer releases fill part of each re-bow dip, so refit after the render with `tools/fit_rebows.py 41 ... --write` plus stem_fix on those five tracks, as c40 did. Check the Cb coda scaling (276.05, 278.351, 282.203, 283.605) again.
- If the actor would rather not touch the caps: Movement I's own fallback is `reverb.fx_volume` 0.095 -> 0.12 (+2 dB on every hall return, all 32 tracks rebuilt). But at +0.15 s the strings' drop is release, not hall, so +2 dB of hall moves the string t-20 only to about 0.30 s (inferred). The cap is the targeted fix.

### 2. The image is narrower than every reference, most of all below 250 Hz (measured; step 1 simulated, step 2 inferred from Movement I's result)

**Where.** The whole movement, loud and soft alike. Numbers in the table above.

**Which stems carry the low band (c40; share of < 250 Hz power, correlation, R-L).** Violoncellos -4.0 dB / 0.85 / +4.5; Double basses -5.2 / 0.79 / +3.5; Tuba -12.8 / 0.81 / +5.8; Timpani -13.8 / 0.97 / +0.3; Bass clarinet -14.8 / 0.98 / -1.0; violas -15.0 / 0.75; Bass trombone -15.6 / 0.82. In 250 Hz-4 kHz the winds read 0.85-0.95 (width 0.05) and the horns 0.68-0.83.

**Step 1, side-only low cuts (simulated by undoing each shelf on the stem's side channel; RBJ shelves, so approximate).**

| Variant | corr 35-63 Hz / R-L | corr 20-120 | corr 120-250 | corr < 250 / side/mid / R-L |
|---|---|---|---|---|
| c40 | 0.960 / +0.75 dB | 0.901 | 0.788 | 0.800 / -8.6 / +2.93 |
| the -2 dB cuts at 0 (Contrabassoon, Bass trombone, Tuba, Violoncellos) | 0.955 / +0.83 | 0.892 | 0.759 | 0.777 / -8.0 / +3.24 |
| those plus Bass clarinet 250 Hz -6 at 0 | 0.954 / +0.82 | 0.888 | 0.757 | 0.775 / -8.0 / +3.20 |
| those plus Timpani 300 -9 and both harps 300 -8 at 0 | 0.948 / +0.75 | 0.882 | 0.739 | 0.760 / -7.8 / +3.16 |
| every side low cut at 0 (including the basses' 100 Hz -15) | 0.817 / **+7.26** | 0.755 | 0.696 | 0.702 / -6.4 / +4.25 |

- Do **not** zero the basses' side shelf (100 Hz -15). It is a seat fix from c33 (35-63 Hz R-L +14 -> +2 dB), not a decorrelation fix. Without it the deep bass leans 7.3 dB right; the Dvořák measures -0.1.
- Keep the harp's shelf too: undoing it moves the harp's low image from -2.8 to -6.4 dB R-L.
- Set to 0 dB (leave each FX in place): Contrabassoon, Bass trombone and Tuba `lowshelf 200 -2`, Violoncellos `lowshelf 200 -2`, Bass clarinet `lowshelf 250 -6`.
- Timpani's 300 Hz -9 is optional. Undoing it takes the timpani stem from 0.97 to 0.80 below 250 Hz, with its seat moving 0.6 dB. It was set in c36 to steady an image the old, wetter hall had smeared (0.39), so re-check that stem's correlation if it goes.
- Step 1 alone gains only 0.02-0.04. The rest has to come from the mics.

**Step 2 (ONE_TIME as written).**
- Copy `width_by_mic` from `mockup-kit/pipeline/build_reaper.py apply_mix` (the `max(width, width_by_mic[label])` rule) into `tools/build_reaper.py` at line 131-134. Then in `build/mix.json`: groups `wind`, `horn` and `lowbrass` `"width_by_mic": {"Main": 0.35}`; Violoncellos and Double basses `{"Main": 0.45}`; Clarinet 1 and Horn 1 `{"Main": 0.2}`.
- Movement I's result with the same change: correlation below 250 Hz 0.78 -> 0.57, side/mid -7.3 -> -6.3 dB, stem levels unchanged within 0.15 dB.
- Expect less below 120 Hz here: the basses' -15 dB side shelf removes whatever side the wider Main adds under 100 Hz (inferred).
- Accept when correlation below 250 Hz is 0.65 or less, 250 Hz-4 kHz 0.60 or less, side/mid -6.0 dB or wider, and each rebuilt stem's R-L within 1 dB of c40. Also check 35-63 Hz R-L stays within ±2 dB.
- If the basses' Main at 0.45 centres the deep bass by itself (R-L under +1 dB at 35-63 Hz), try the basses' side shelf at -9 instead of -15 in the same cycle (mix only).
- Finding 1 helps here too (inferred): longer string releases bring back Main-mic room, which is decorrelated. Measure after both changes.

**Fallback if side/mid is still under -6.0 dB.** The hall's Width (p.220; state key `width`, default 1.0) at 1.5, as Movement I c45 proposed: a pass-2 test first, adopted only if the tail's L/R correlation falls by 0.15 or more and its level rises 1 dB or less. It cannot help below 160 Hz (the low cut).

### 3. The divisi halves sit in a different room from their sections, and as narrow points (measured; fix part inferred)

**Where.** Violins II div with Violins II, bars 37-40 (qn 108-124, sul tasto); Violas div with Violas, bars 23-30 (qn 66-90), 80-81 (262-268) and 84-92 (279-304); Violoncellos div with the celli, bars 18 and 21-22 (51-54, 62-66).

**Evidence (c40, same windows, both tracks playing).**
- Image, correlation at 250 Hz-4 kHz:
  - Violins II 0.58 against Violins II div 0.93;
  - violas 0.62-0.75 against Violas div 0.91-0.96;
  - celli 0.84-0.90 against Violoncellos div 0.89-0.92.
  The DIV halves (Close mic only, width 0.3) are near-mono points at the centre of their section's spread. A real half section of five or six players covers about half the section's width.
- Room: the DIV phrase ends take 0.34-0.44 s to -20 dB, against 0.15-0.22 s for Violins II and the violas (finding 1). They are wetter than the section around them, because their send is 0.5 against 0.25.
- Tone: within 2 dB of the section in 1-2 kHz and 2-5 kHz re 300 Hz-1 kHz in most windows: Violins II div -2.1 / -1.1; Violas div bars 26-30 -0.7 / +1.9; coda -0.4 / +0.6. Two windows differ by more:
  - Violas div bars 23-25: -5.8 / -4.4 dB darker;
  - bars 80-81 ff: -5.0 / -2.5, centroid 799 against 1136 Hz.
  The voices differ there (the div part plays other notes), so this is inferred, not a sample-set mismatch.
- Muted against open is consistent across the sections. On the same pitch, open bars 1-3 against the muted coda, 2-5 kHz re 300 Hz-1 kHz falls by 5.5 dB on Violins I (C5) and 6.6 dB on Violins II (A flat 4). The con sordino script is doing its job; no change.
- Harp harmonics against the harp: the same band profile (2-5 kHz -31.6 dB both) and the same correlation (0.58 against 0.59). Matched.

**Fix.**
- First make finding 1's change and re-measure. If the sections reach about 0.43 s, the DIV halves (0.34-0.44) match without a send change. Leave c40's deferred C #5, div sends 0.5 -> 0.35, unless the sections are still more than 0.1 s faster after finding 1.
- Widen the two half-section DIV B tracks: `build/mix.json` Violins II div and Violas div `width` 0.3 -> 0.45 (Opus state change, 2 tracks rebuilt). Keep Violin I solo (a soloist, correctly a point) and Violoncellos div (4 soli) at 0.2.
- Accept when the DIV B stems' 250 Hz-4 kHz correlation falls to about 0.80, with R-L within 1 dB of now (Violins II div -4.3 dB, Violas div +2.7).

## Checked and needing no change

- **Low end against the references (measured).** All frames, band shares 20-100 / 100-250 / 250-500 / 500-2k / 2-6k Hz:
  - c40: -19.0 / -8.2 / -5.6 / -3.2 / -10.6;
  - Dvořák: -22.2 / -6.7 / -6.5 / -3.3 / -10.4;
  - Brahms 1/ii and 4/ii: 100-250 -8.75 / -7.55, 250-500 -5.95 / -6.34.

  The 250-500 Hz band is 0.4-1.3 dB heavier than the references (loud frames -5.5 against the Dvořák's -6.8). Celli, violas and Horns 1-3 supply 59% of it, and Horn 1/3 already carry c40's 300 Hz -2 bell. Soft frames are 2 dB heavier at 100-250 Hz than the Dvořák. That is the scoring: the celli/basses pedal, the bass clarinet chalumeau and the harp's low notes in the opening, the retransition and the coda give 75% of it. There is no low-mid build-up to fix in the mix. 112-224 Hz re 224-2245 Hz: loud -7.9 against -5.3, soft -6.6 against -8.0.
- **Seating (measured, 250 Hz-4 kHz R-L per stem).** Violins I -7.9, Violins II -3.6, violas +1.8, celli +5.8, basses +6.8, horns -7.4..-2.7, trombones +4.8..+6.5, tuba +5.6, harp -3.5, timpani 0.0, winds within ±3.6 dB; master balance -0.1 dB. Coherent American seating.
- **S3 (measured, master 30 ms envelope).** No cut tails at the fp of qn 148, the breath at 195-196 or the bar 66 niente (223-226); the level falls at most 2-4 dB per 0.1 s there.
- **ONE_TIME #1 records (measured).**
  - The final chord's release is in finding 1.
  - The "breath at 268" is not a tutti stop: only Flutes 1-2 breathe (a 0.23 s gap from qn 267.88) while everything else sounds, and the master falls only 3-4 dB. On the flute stems the drop at +0.15 s is 15.5 / 12.0 dB in c40 (14.5 / 12.0 in c39). The winds have no cap, so the c40 change did not touch them.
  - The detector finds no tutti stop anywhere in the movement, so use the per-stem detector numbers above as the hall record.
- **Loop pulsing (item 8).** The c40 actor measured autocorrelation at 3.95 s of -0.15..-0.04 on the long string notes; not re-measured. After finding 1, check the final chord again, since longer releases overlap the re-bow joins differently.

Do not touch: the true-stereo hall, `fx_volume` 0.095, the 160 Hz hall low cut and `ir_setup` 0.7 (the hall itself is in range; the dryness is in the string releases); the basses' 100 Hz -15 dB side shelf (it centres the deep bass: 35-63 Hz R-L +0.75 dB, +7.3 without it); the harps' 300 Hz side shelves; the 150 ms caps on the four divisi/solo tracks; the horn caps at 237 ms; the con sordino behaviour (5.5-6.6 dB darker in 2-5 kHz, as wanted); the current seats.
