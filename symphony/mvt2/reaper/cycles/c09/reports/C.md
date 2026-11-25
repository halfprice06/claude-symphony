# Cycle 9, critic C: blend and space (on the cycle 8 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets, low-end build-up against reference spectra.

Material: `cycles/c08/render` (master and 27 stems), `cycles/c08/metrics`, `build/mix.json`, `build/parts.json`, `tools/build_reaper.py`, `tools/score_to_parts.py`, the Opus states in `jobs/*.b64` (decoded), the Opus manual (Reverb, Pre and Post Fader), score page 8.

References. Until now the loop has judged the spectrum against one file, the Dvorak 9/i Columbia MP3 (a live student orchestra, a fast movement, 128 kb/s). Two better-matched references are already measured in the repository: Brahms 1/ii and 4/ii (Musopen, lossless, professional orchestra, slow movements), in `symphony/render/critics/c04/ref_brahms{1,4}_ii_musopen/metrics.json`. The audio files are not on disk, so I compare with their stored third-octave spectra, band shares, stereo correlation and final-tail times. Those FLACs are band-limited above about 11 kHz, so I use their bands only up to 10 kHz.

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c09-C/`. All run with `~/.venvs/claude-composes-reaper/bin/python`:
- c05-C's `tails.py`, `tailpan.py`, `lowbands.py`, `lowcontrib.py`, `stems.py`, pointed at c08
- `refcmp.py` and `shares.py`: third-octave spectrum and band shares against the Brahms and Dvorak references
- `contrib2.py` and `hicontrib.py`: which stem makes each band
- `panband.py`: R-L balance and L/R coherence per band and per stem
- `pans.py`: the decoded Opus pans, sends and reverb
- `harm.py`: harmonic levels per note
- `infra.py` and `harpsub.py`: content below 40 Hz
- `ftail.py`, `final.py`, `silence.py`: the final-chord tail
- `taildark.py`: tail spectrum against sustain spectrum
- `chops.py`: vol_db steps that fall during a reverb tail

## 1. The mix is thin at 100-250 Hz and bright above 2 kHz compared with real slow movements. The low-end targets were set by a bass-light reference (measured; audible effect inferred)

**Where:** the whole movement. The low-mid gap is largest in the tutti bars 59-62 and 77-80. The top end is set by Violins I throughout.

**Evidence (measured).** Band shares of total energy, in dB (`shares.py`, `refcmp.py`):

| Band (Hz) | c08 | c04 | Dvorak 9/i (MP3) | Brahms 1/ii | Brahms 4/ii |
|---|---|---|---|---|---|
| 20-100 | -18.9 | -16.5 | -21.7 | -8.5 | -7.9 |
| 100-250 | **-11.2** | -8.2 | -6.6 | -8.8 | -7.6 |
| 250-500 | -6.6 | -6.5 | -6.3 | -6.0 | -6.3 |
| 500-2000 | -2.4 | -2.8 | -3.5 | -3.8 | -4.4 |
| 2000-6000 | -9.2 | -11.6 | -10.5 | -12.4 | -11.8 |

- **100-250 Hz** is 2.6 to 4.6 dB short against all three references, and it has fallen 3 dB since c04. That is consistent with the c05 regression already noted (the Cb Close cut, the timpani mics, the new IR) and the c08 note that the cello trims "did not move" the low-mid band. This finding holds whichever reference is used.
- **20-100 Hz**: the references disagree by 13 dB. The two lossless orchestral recordings have 10 dB more bass than c08; the Dvorak MP3 has 3 dB less. Since c01, every low-end cut (Cb gain, Cb Close 0.94 -> 0.4, low shelf 90 Hz -7, the 63 Hz targets) was justified against the Dvorak alone. That file is the outlier.
- **Third octaves against the mean of the two Brahms recordings, pivoted at 500 Hz** (where all three agree within 0.4 dB):

  | Hz | 49.6 | 62.5 | 78.7 | 99 | 125 | 157 | 1000 | 2000 | 4000 | 6300 | 8000 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | c08 minus Brahms (dB) | -13 | -10 | -12 | -5 | -6 | -6 | +4.5 | +2 | +3 | +5 | +6 |

- **Who makes these bands** (`contrib2.py`, `hicontrib.py`):
  - 100-250 Hz: Double basses and Violoncellos each supply 35% (each is -4.5 dB of the master band). The next stems are 6 dB lower: timpani -10.8 and bass clarinet -11.3.
  - Above 6 kHz: Violins I supply 89% of the master's energy (-0.5 dB), and 70% of 2-6 kHz (-1.5 dB). Violins I's share of 6-20 kHz is 6.5 dB above its share of the total; Violins II's is -1.6 dB. The Vln I stem's 6-12 kHz is -9.6 dB re its own 400-1000 Hz band, against -25.5 for Vln II.
- **The Cb's tone** (`harm.py`, sustained single notes): on C1-B1 (n = 40), H1 is -21 dB and H3/H4 are -14 dB relative to H2. The section's sound sits in one octave (65-125 Hz), with little above it to carry pitch. The cellos run the other way: on G2-C#3 (n = 9), H1 is +16 dB over H2.

**Effect (inferred).** The tutti lacks body: violas, cellos and bassoons do not fill the floor between the bass and the tune. The violins carry an edge that a hall seat 20 m away does not hear. On a slow movement this reads as "samples": bright and hollow.

**Fix (`build/mix.json`, plus a small code change in `tools/build_reaper.py`; ReaEQ only, so `--midi-only` applies it without patch reloads):**
- Violoncellos `eq`: keep `highpass 30` and add `{"band": "bell", "hz": 170, "db": 4, "bw_oct": 1.5}`.
- Double basses `eq`:
  - bell `150 Hz +3, bw 1.4` -> `160 Hz +6, bw 1.4` (lifts H3-H5 of the low notes)
  - low shelf `90 Hz -7` -> `90 Hz -5` (a middle course between the references; do not cut further)
  - leave `gain_db` and the mics alone
- Violins I `eq`: add `{"band": "highshelf", "hz": 5000, "db": -4}`.
  - In `ENV_LUA set_eq`, handle `highshelf` on ReaEQ band 3: `BANDTYPE3 "1"`, `BANDENABLED3 "1"`, frequency param 9, gain param 10, set with `set_by_fmt` as the other bands. The existing read-back lines confirm the type.
  - The 2-4 kHz presence that carries the melody stays.
- `tools/measure.py`: print the band shares and third octaves of the mix next to the two Brahms `metrics.json` rows, as well as the Dvorak row, so later cycles do not tune the bass to one MP3.

**Targets (`shares.py`):**
- 100-250 share ≥ -8.8 (now -11.2)
- 20-100 share between -16 and -12
- 2-6 kHz share ≤ -10.5
- third octaves 6.3/8 kHz ≤ +2.5 dB over the Brahms mean (500 Hz pivot)
- the Vln I melody margin at bars 57-62 and 75-81 within 1 dB of c08

## 2. Every instrument's reverb comes from its own seat: the hall send is post-pan (measured)

**Where:** all 27 tracks. It is most audible on the outer seats (Violins I, Violoncellos, Double basses, Tuba, Bass clarinet) and at every phrase end and caesura (qn 204, 268, the fermata).

**Evidence (measured).**
- `tailpan.py` gives R minus L in dB for the sustain (0.25 s before a cutoff) against the tail (0.35-1.2 s after it):

  | Stem | Sustain R-L | Tail R-L |
  |---|---|---|
  | Violins I | -7.6 | -7.7 |
  | Violins II | -5.4 | -5.1 |
  | Violoncellos | +5.4 | +5.3 |
  | Double basses | +5.6 | +6.5 |
  | Bass clarinet | -6.3 | -6.1 |
  | Cor anglais | +5.3 | +5.5 |
  | Horn 4 | -5.0 | -5.6 |

  In 24 of 27 stems the tail sits within 1.5 dB of the sustain. This is the c05 finding #3, still open.
- Decoded `jobs/21_1st_Violins_KS_Master.b64`: every mic channel's `SendProcessor` has `"post": true`, and the mic channels carry the seat (`panLeft -1.0`, `panRight -0.05`). The Opus manual (Pre and Post Fader, pp. 106-107) says the post switch puts the send after the channel fader. So the hall is fed the panned signal and returns it at the seat.
- In a hall, the reverberant field reaches the listener from all sides whatever the source seat. The Dvorak final-chord tail widens after the release (correlation 0.53 -> 0.26, `ftail.py`). The c08 master's tail barely does (0.69 -> 0.48), and that is a sum of 27 seat-bound tails.

**Effect (inferred).** The sections sound like 27 booths around one microphone: the hall does not connect them, and phrase ends leave each section's room hanging at its own position.

**Fix (`tools/build_reaper.apply_mix`; patch states change, so a full rebuild of all tracks, then restart REAPER before the render):**
- On every mic channel's Reverb Send, set `ins["post"] = False`. This makes the send pre-fader and, inferred, pre-pan, because the insert sits before the fader and pan.
- Set `ins["level"] = m["send"] * c["volume"]`, so the reverb input keeps today's level now that the channel fader no longer scales it (Close 0.5-0.66, Main 0.5-1.0).
- Keep the fx:0 return centred at full width, the shared IR, `wet` 2.0 and `fx_volume` 0.19 for the first render. Re-tune `fx_volume` only if the tail level moves by more than 1 dB.

**Check (`tailpan.py c09`):**
- the sustain R-L of each stem within 1 dB of c08 (the seats do not move)
- the tail R-L within ±3 dB for every stem (Vln I now -7.7)
- master correlation in the tail after the final chord ≤ 0.35

**If the tail still follows the seat:** build the REAPER Hall bus from c05 #3 (Opus reverb `fx_volume` 0, post-fader track sends to one bus with ReaVerb on the CC BY Detmold IRs). A post-fader REAPER send also stops vol_db steps from cutting tails. That matters less than in c05: `chops.py` finds only 11 steps of 3 dB or more inside a tail, and 7 of them are the final fade (#5).

## 3. Several seats are wrong because the patches' own L/R imbalance survives the wide dual pan (measured)

**Where:**
- Harp: bars 7-14, 41-56 and the coda
- Horns 1-4: bars 3-14, 55-62, 67-70, 87-89
- Bass clarinet: bars 3-5, 31-36
- Trombones: bars 59-64
- the low strings' image throughout

**Evidence (measured, `panband.py`: R-L dB / L-R coherence per band, 60-250 | 250-1k | 1-4k Hz; `pans.py` for the Opus pans):**
- **Harp**, seat -0.6 (panLeft -1.0, panRight -0.05, exactly the same as Violins I):
  - harp: -0.3/0.66 | -3.3/-0.01 | -8.7/0.59
  - Violins I: -7.5 | -8.1 | -8.2

  The harp's main bands (its stem is +6 to +12 dB at 90-400 Hz re 400-1000) sit near centre, and its 250-1000 Hz band has zero L/R coherence. The tailpan sustain R-L is 0.0 dB. A harpist seated far left is heard in the middle, spread across the stage.
- **Horns** (seats -0.45, -0.40, -0.35, -0.30), 250-1000 Hz band:
  - R-L: Horn 1 -3.5, Horn 2 -1.0, Horn 3 +0.6, Horn 4 -4.3
  - coherence: 0.48 / 0.24 / 0.22 / 0.53

  Horn 3 sits right of centre, and the order of the four players is scrambled.
- **Bass clarinet**, seat -0.25: -6.0 / -8.1 / -4.1, as far left as Violins I. Clarinets 1 and 2 at seats -0.15/-0.20 measure -2.5 to -5.
- **Trombones 1-2**, seats +0.30/+0.35: 60-250 Hz -2.5 (left of centre), mid bands +3 to +4.
- **Low end**: coherence below 250 Hz is Cb 0.32, Vc 0.27, Tuba 0.34. Master coherence below 250 Hz is 0.35, against 0.60 and 0.62 for the Brahms recordings (`refcmp.py`). The master's mid and high coherence match: 0.54 against 0.48-0.52, and 0.46 against 0.38-0.47.
- **Cause (inferred from the numbers):** `apply_mix` places each patch's left channel at seat - width and its right channel at seat + width, with width 0.5-0.6. Any level or phase difference baked into a patch's stereo recording keeps a full stage-width lever on where the instrument lands.

**Fix (`build/mix.json`; seats and widths are in the Opus state, so this rides on the #2 full rebuild):**
- width 0.3:
  - `groups.harp` (and Harp seat -0.6 -> -0.65)
  - `groups.horn`
  - Bass clarinet, Cor anglais, Trombone 1, Trombone 2, Bass trombone and Tuba (per-track `width`)
- width 0.35: Violoncellos and Double basses (Cb 0.6 -> 0.35)
- Keep all other seats and the violin and viola widths.

**Check (`panband.py`, `stems.py`):**
- Harp R-L ≤ -6 dB in every band
- Horn 1 to Horn 4 R-L monotonic in the seat order, each between -3 and -7 dB
- Bass clarinet within 2 dB of Clarinet 2
- master coherence below 250 Hz 0.5-0.62, master correlation ≤ 0.60 (now 0.515)

## 4. The hall tail is as bright as the dry sound (measured; effect inferred)

**Where:** every cutoff, most audible at the caesuras (qn 204, 268), at the bar 63-64 trombone release and at the final fermata.

**Evidence (measured, `taildark.py`; change of the 2-8 kHz band re 250-1000 Hz from sustain to tail):**
- Stem cutoffs (0.25-1.0 s after the cutoff against the 0.8 s before it): median -1.0 dB over 27 stems. Violins I -1.6, Violins II -1.2.
- Final chord: c08 master -13.4 dB, Dvorak -18.4 dB.
- The shared `ConvolutionReverb` has `filterActive: false` and `highFilterFreq: 18000` (decoded state). In a real hall, high frequencies decay faster than mids (air and seat absorption), so the reverberant tail darkens. Here the hall returns the violins' 6-10 kHz edge (finding 1) at full strength.

**Fix (`tools/build_reaper.apply_mix`, after `rv = shared_reverb()`; same full rebuild as #2):**
- `rv["filterActive"] = True`
- `rv["highFilterFreq"] = 5500`
- `rv["lowFilterFreq"] = 30` (unchanged)
- Opus manual p. 133: Bandpass enables the High Cut (30 Hz-18 kHz) on the reverb only.
- Make the value a mix.json key, `reverb.high_cut_hz`.

**Check:**
- stem tails at least 4 dB darker than the sustain (median of the 2-8 kHz change ≤ -4)
- master 6.3/8 kHz third octaves down by a further 1-2 dB, together with #1
- the 300 ms drop and the final-chord tail times otherwise within 1 dB of c08

## 5. The final ppp fermata chord is faded during its own reverb tail, and the hall rings shorter than in the references (measured)

**Where:** bar 92, from qn 304.0 (Cl2 and Cb release) and 304.26 (strings) to the end. The score (p. 8) has morendo, ppp and a fermata on every part.

**Evidence (measured).**
- The `fade` part in `score_to_parts.py` (about line 1232) is `(303.0, 0) (303.5, -2) (304.0, -10) (304.5, -20)`. The last 0.5 qn of that ramp (-10 -> -20 dB, 0.72 s at the 20 bpm fermata tempo) falls after the last release. The volume envelope sits after Opus, so it fades the hall: the Vln I tail is cut from -16.5 to -20 dB, Clarinet 2 and Cb from -10 to -20, timpani from -21 to -31 (`chops.py`).
- Master decay after the last release (`ftail.py`, the Brahms metrics' definition: t0 = last frame within 12 dB of the final-20 s maximum):

  | Recording | -10 dB to -40 dB | Implied decay time |
  |---|---|---|
  | c08 | 0.9 s | about 1.8 s; about 2.1 s without the fade's share |
  | Brahms 1/ii | 1.24 s | RT60 2.5 s |
  | Brahms 4/ii | 1.52 s | RT60 2.9 s |

  Dvorak: -10 to -30 dB in 0.9 s (about 2.7 s).
- The master reaches digital silence 1.8 s after the last release (349.83 s, `silence.py`).

**Effect (inferred).** The last sound of the movement is a chord whose room is switched off with it: the morendo ends in a studio, not in a hall.

**Fix (`tools/score_to_parts.py`, the `fade` branch):** end the fade at the last note-off and hold it. Use `[(303.0, 0.0), (303.5, -2.0), (304.0, -10.0)]` and hold -10 from 304.0. Remove the 304.5 break from `vbreaks`. The timpani settle part, which reaches -31, should also hold its value from qn 304. The CC11 morendo already takes the notes down to ppp. Do not shorten the hall further (the c05 IR change stays).

**Check (`ftail.py c09`):**
- master -10 to -40 dB in ≥ 1.2 s after the last release
- no audible fade before the release: the level 1 s before the release within 1 dB of c08

## 6. Sub-bass rumble below 30 Hz, mostly from the harp (measured; audibility depends on the playback system)

**Where:** the harp passages (bars 7-14 most), plus the tuba, bass trombone and timpani.

**Evidence (measured; `infra.py`, `harpsub.py`, `lowcontrib.py`):**
- Master 8-16 / 16-25 Hz re 400-1000 Hz: -38.5 / -40.0 dB, against the Dvorak's -50.6 / -48.1. At 25-32 Hz the master is level with the Brahms third octaves.
- In bars 1-14 the master's 25-40 Hz band is -30.2 dB re 400-1000 Hz; the Dvorak's soft frames measure -40.3.
- Sources of the master's 8-25 Hz energy:

  | Stem | Share (dB of master band) |
  |---|---|
  | Harp | -2.3 (59%) |
  | Tuba | -8.6 |
  | Bass trombone | -9.8 |
  | Timpani | -10.5 |

- The harp stem's 10-20 Hz band is -18 dB re its 100-1000 Hz band, peaking at 11.7 Hz. That is more than its 37-55 Hz fundamentals (-30 dB), so it is not music. The harp's lowest note is E flat 1 (38.9 Hz), and the harp has no ReaEQ.
- Bass trombone still contributes with its 30 Hz high-pass. Its lowest note is D2 (73 Hz).

**Fix (`build/mix.json` `eq`, ReaEQ only, `--midi-only`):**
- Harp: add `{"band": "highpass", "hz": 30}`
- Tuba: add `highpass 25`; lowest note E1, 41 Hz (keep its low shelf)
- Bass trombone: `highpass` 30 -> 40
- Timpani: add `highpass 45`; lowest note A flat 2, 104 Hz

**Check:**
- master 8-25 Hz ≤ -46 dB re 400-1000 Hz
- 40-63 Hz unchanged within 0.5 dB

**Do not touch:**
- the shared hall IR (New Hollywood Hall 2.0) and its pre-delay
- the per-group send ordering (strings < wind < low brass/timp < horns)
- the string seat order and the violin and viola widths
- the mic choices (Close + Main; woodwinds Close 0.5 / Main 0.8; Cb Close 0.4; timpani Close 0.2 / Main 0.5; Surround not loaded)
- the 40/30 Hz high-passes already in place
- the master mid/high stereo correlation (0.54/0.46, on the references)
- the 250-500 Hz band (on all three references)
- the attack gate and the restart-before-render routine
