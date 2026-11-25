# Cycle 13, critic C: blend and space (on the cycle 12 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets, low-end build-up against the reference spectra.

Material: `cycles/c12/render` (master and 28 stems), `cycles/c12/metrics`, `build/mix.json`, `build/parts.json`, `tools/build_reaper.py` (`apply_mix`, `shared_reverb`), the Opus states in `jobs/*.b64` (decoded), the Opus manual (Reverb, pp. 132-133), score `v77/sections/aOne.ily`. References: the Dvorak 9/i MP3, plus the stored Brahms 1/ii and 4/ii spectra and tail metrics in `symphony/render/critics/c04/ref_brahms*_musopen/metrics.json`.

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c13-C/`. Run them with `~/.venvs/claude-composes-reaper/bin/python`. They are the c09-C set pointed at c12, plus these new ones:
- `common.py` now reads `PARTS=<path>`
- `pans.py`: decoded Opus pans, sends and reverb
- `tsscan.py` / `tsfind.py`: which reverb IRs the HO patches use
- `solo.py` / `vtilt.py`: solo-violin and section spectra by register
- `harmx.py`: Cb harmonic levels in any cycle
- `eqsim.py`: Cb EQ changes simulated on the master
- `corr.py`: L/R correlation of each stem
- `rel.py`: master decay after the final release

Delivery numbers for c12, from metrics.md (measured): master -23.6 LUFS, LRA 23.9 LU, TP -3.9 dBFS. mp3 -19.8 LUFS, LRA 15.7 LU, TP -1.6 dBTP, p10-to-max span 18.4 dB, limiter 3.0 dB. None of the findings below is a level change, except #2, which can move the reverb level. If #2 is taken, re-check these numbers after the render.

## 1. The solo violin in bars 17-22 sits at the far left wall, and so does its reverb: the Opus master channel of the DIV A patch is panned -0.74, and `apply_mix` never resets it (measured)

**Where:** Violin I solo (track 28), bars 17-18 and 21-22. This is the "solo, senza sord." dialogue with Oboe 1 (`aOne.ily` line 62) over the muted strings.

**Evidence (measured):**
- `panband.py`, R-L per band (60-250 / 250-1k / 1-4k / 4-12k Hz):
  - Violin I solo: -21.1 / -20.2 / -21.7 / -22.1 dB
  - Violins I section, same seat (-0.55): -7.1 / -8.3 / -8.2 / -8.3
- `tailpan.py`: solo sustain R-L -21.0 dB, tail -20.8 dB. Its hall comes back from the same place.
- `pans.py` on `jobs/27_1st_Violins_KS_Master_DIV_A.b64`: the `main` channel has `"pan": -0.738`. Every other state has main pan 0.0. The patch preset seats DIV A on the left.
- `apply_mix` resets `pan` only on the `sub:` channels and on `fx:0`. The main channel pans after the reverb return is mixed in, which explains why the tail is just as far left. The REAPER pan for the track is centre (rpp VOLPAN 1 0).
- Tone, inferred: from the same register (pitches 72-77), the solo is 7 dB brighter at 4-10 kHz and 4 dB brighter at 2-4 kHz than the Violins I section (`vtilt.py`), and it has only the Close mic. Some of that is right for a soloist senza sord. over muted strings. With the hard pan, though, it reads as a spot mic in another room.

**Effect (inferred).** A listener hears the oboe slightly right of centre and the violin answering from the far left edge, outside the first-violin section and with a dry, left-only room. The dialogue does not sound like two players in one orchestra.

**Fix (`tools/build_reaper.py` `apply_mix`, plus `build/mix.json`; this changes the state of track 28 only, so rebuild that track fully):**
- In `apply_mix`, after the sub-channel loop, centre the main channel:
  `main = next(c for c in chans if c["channelId"] == "main"); main["pan"] = 0.0; main["panLeft"], main["panRight"] = -1.0, 1.0`
- `mix.json` "Violin I solo": `seat` -0.55 -> -0.4 (the concertmaster's front desk, inside the section towards the podium). Keep width 0.2.
- Optional, only if it still stands out after the re-pan: `send` 0.5 -> 0.6, and the highshelf 5000 Hz -4 -> -6.

**Check (`panband.py c13`, `tailpan.py`):**
- Solo R-L between -7 and -4 dB in every band; tail R-L within 2 dB of the sustain.
- Solo level in bars 17-22 within 1 dB of c12. The re-pan changes power, so re-trim `gain_db` if needed.

## 2. Every instrument's reverb still comes back from its own seat. The cause is a stereo (not true-stereo) IR, and the library ships a true-stereo hall that the reverb can load (measured; fix inferred, needs one test)

**Where:** all tracks; most audible at phrase ends and on the outer seats (Violins I, Cb, Vc, Tuba, Bass clarinet). This has been open since c05. The c09 pre-fader send had no effect.

**Evidence (measured):**
- `tailpan.py`, sustain R-L against tail R-L:

  | Stem | Sustain R-L (dB) | Tail R-L (dB) |
  |---|---|---|
  | Violins I | -7.9 | -8.3 |
  | Violins II | -4.3 | -5.5 |
  | Bass clarinet | -6.2 | -6.2 |
  | Horn 1 | -5.6 | -5.1 |
  | Violoncellos | +5.0 | +4.5 |
  | Double basses | +7.5 | +5.7 |
  | Cor anglais | +4.2 | +3.9 |

  In 24 of 28 stems the tail sits within 2 dB of the sustain.
- Master after the final release (`rel.py`): L/R correlation 0.56 before the release and 0.47 in the tail. Dvorak goes from 0.53 to 0.26 (`ftail.py`). Master mid-band coherence, 250 Hz-4 kHz: 0.595, against 0.48 and 0.52 for Brahms 1/ii and 4/ii (`refcmp.py`). The image is narrower and less diffuse than a hall's.
- Cause. The decoded hall insert is `ConvolutionReverb` with `"trueStereo": false` and `"sendMono": false`, on `//ir/latest PLAY impulses final/New Hollywood Hall 2.0`.
  - A stereo IR convolves L with L and R with R, so a left-panned input gives a left tail. That is why the c09 pre/post switch changed nothing.
  - A true-stereo IR has four paths (L->L, L->R, R->L, R->R), so a left source also excites the right side of the hall.
- `tsscan.py` over 1683 HO `.oib` files: 74 percussion patches already use a true-stereo IR:
  - `"impulseA": "//ir/HOP True Stereo/S. Cal Hall Perc TS FR 3.3s", "trueStereo": true`
  - for example `/Volumes/MAC DRIVE/EW Hollywood Orchestral Percussion Diamond/Hollywood Orch Percussion Opus Instruments/Cymbals/Cymbal Pairs/12in - 22in Crash Combo.oib`
  - It is the same S. Cal. Hall that 756 HO string/wind patches use by default ("S. Cal. Hall strings LR Rear"), recorded true-stereo. The manual (p. 133) says the Reverb unit "adds the ability to load true stereo reverbs".
- The decay is right now and must stay. Final release drop at 0.3 / 0.6 / 1.0 / 1.5 s: 9.2 / 16.4 / 27.7 / 37.7 dB (`rel.py`). That is about -10 dB at 0.33 s, -20 at 0.75 s and -30 at 1.1 s. Brahms 1/ii and 4/ii measure -10 at 0.2-0.4 s, -20 at 0.48-0.79 s and -30 at 1.15-1.23 s.

**Fix (`build/mix.json` `reverb`, a few lines in `build_reaper.apply_mix`; full rebuild of every track and a REAPER restart, as in c09):**
- `reverb.from_patch` -> the Crash Combo `.oib` above. `shared_reverb()` copies the whole insert, including `trueStereo` and `irSetup`.
- After `rv = shared_reverb()`, set:
  - `rv["delay"] = 0.0303` (keep today's pre-delay; the percussion patch has 0)
  - `rv["wet"] = 2.0`
  - the existing `high_cut_hz` 5500
- First pass: `fx_volume` 0.19 and `irSetup.simpleDecay` 1.0. This IR is 3.3 s long, against the 2.5 s late slope of the current hall. If the final-release drop at 1.0 s comes out more than 3 dB shallower than c12's 27.7 dB, set `rv["irSetup"]["simpleDecay"]` to 0.8 (Opus manual p. 134, Simple envelope).
- Fallback if the TS IR does not load or the test fails: keep the current IR and set `rv["sendMono"] = True`. The manual's wording ("collapse the separate left and right channels") is ambiguous, so accept it only if the checks below pass and the tail correlation stays under 0.8. A mono tail would be worse than today.
- Test on a short range render (bars 15-30 and 89-92) before the full render.

**Check (`tailpan.py`, `rel.py`, `refcmp.py`):**
- Vln I, Vc, Cb and BCl tail R-L within ±3 dB, while each stem's sustain R-L stays within 1 dB of c12.
- Final-release tail correlation ≤ 0.35.
- Master 250 Hz-4 kHz coherence ≤ 0.53.
- Final-release drops at 0.3 / 0.6 / 1.0 s within 2 dB of c12.
- mp3 LRA, span and limiter within 0.5 of c12. A louder hall raises the soft passages less than it raises the climaxes.

## 3. The double basses have lost their fundamentals: the bass line sounds an octave higher and merges with the cellos (measured; the musical effect is inferred)

**Where:** Double basses, all through. Most exposed:
- the Ab1 pedal: pitch 32 is the section's most common note, 64 qn of 219
- bars 21-30 and 37-56 under the solos
- the coda 83-92, where the cellos play Ab2 an octave above

**Evidence (measured):**
- `harmx.py`, median harmonic levels relative to H2 on sustained single notes, C1-B1 (n = 40):

  | Render | H1 re H2 (dB) | Note |
  |---|---|---|
  | c00 | -6.3 | raw samples, no EQ, default mics |
  | c04 | -11.9 | |
  | c12 | -20.2 | |

  Since c00, the mix has removed 14 dB of fundamental relative to the octave above it. The cello notes (G#2-C#3) keep H1 +15 dB over H2.
- The Cb's main pitches are Ab1 52 Hz, Eb2 78 Hz, Db2 69 Hz and Bb1 58 Hz (`parts.json`). Those fundamentals fall exactly where the master is lowest. Third octaves against the Brahms mean, pivoted at 500 Hz (`refcmp.py`): 49.6 Hz -10.7, 62.5 Hz -7.9, 78.7 Hz -9.6. There is a bump at 198 Hz (+3.3), where the Cb bell (160 Hz +6) and the Vc bell (170 Hz +3) stack.
- Band shares: 20-100 Hz -16.3 dB. Dvorak MP3 is -21.7; Brahms are -8.5 and -7.9. The references disagree, which is why the earlier cuts followed the Dvorak. The harmonic comparison above does not depend on any reference.
- `eqsim.py` (zero-phase EQ difference applied to the c12 Cb stem and summed into the master):

  | Cb EQ change | 20-100 Hz share | 62.5 Hz third | 100-250 Hz share |
  |---|---|---|---|
  | low shelf 90 Hz -5 -> 0, bell 160 +6 -> +3 | -16.3 -> -13.9 | +3.0 dB | -9.1 -> -9.5 |
  | low shelf -5 -> -2 only | -16.3 -> -14.5 | | |

**Effect (inferred).** On the Ab1 pedal the ear takes Ab2 as the bass note, and the cellos' Ab2 doubles it in unison instead of an octave above. The tutti loses the floor of a real bass section and sounds lighter and more "sampled" than a hall orchestra.

**Fix (`build/mix.json` "Double basses"; ReaEQ and mic volume):**
- Remove the `lowshelf` 90 Hz -5 band (or set it to -1).
- `bell` 160 Hz +6 -> +3 (bw 1.4).
- `mics.Close` 0.4 -> 0.6.
- `gain_db` -7 -> -8, to hold the section level. Re-trim after the render to B's bar-level targets.
- Keep everything else, including the Cbn/Tuba 70 Hz shelves and every high-pass.

**Check (`harmx.py`, `refcmp.py`, metrics):**
- Cb H1 re H2 on C1-B1 ≥ -12 dB.
- 20-100 Hz share between -14.5 and -12.5.
- 62.5/78.7 Hz thirds within 6 dB of the Brahms mean.
- 100-250 Hz share ≥ -9.5.
- Cb stem bar levels in bars 83-92 within 1 dB of c12; the c09 Cb-Vc check still holds.
- The mp3 limiter does not rise by more than 0.3 dB. The bass is not at the climax peaks.

## 4. The bass clarinet sits as far left as the first violins, 6 dB left of the other clarinets, during its own solo (measured)

**Where:** Bass clarinet, bars 3-5 and its solo in bars 31-36 (the loudest stem in every one of those bars).

**Evidence (measured, `panband.py`):**
- R-L, 250-1k Hz band: BCl -7.2 dB, Clarinet 2 -1.3, Clarinet 1 -2.4, Violins I -8.3. Other bands: BCl -5.7 / -3.6 / -5.1.
- The BCl stem's coherence is 0.90-0.94. It is a narrow source pinned to the left.
- c09 set a target of "BCl within 2 dB of Cl2". After the c09 width change (0.3) it is still 5.9 dB off. The patch's own left-heavy recording sets the position, not the seat (-0.25).

**Effect (inferred).** The bars 31-36 solo comes from the first-violin desks rather than from the clarinet row.

**Fix (`build/mix.json` "Bass clarinet"):**
- `seat` -0.25 -> -0.05, keeping width 0.3.
- Rides on the #2 full rebuild. Without #2, rebuild this track only.

**Check:** BCl R-L in 250 Hz-1 kHz between -4 and -2 dB (within 2 dB of Cl2). Its level unchanged within 0.5 dB.

## 5. The harp moves 4-5 dB towards the centre when its harmonics enter at bar 82 (measured)

**Where:** Harp (bars 81-82) and Harp harmonics (bars 82-83). The same player is on two tracks.

**Evidence (measured, `panband.py`):**
- R-L, 250-1k / 1-4k / 4-12k Hz:
  - Harp: -8.1 / -10.0 / -9.4 dB
  - Harp harmonics: -3.8 / -4.9 / -5.6 dB
- Seats in `mix.json`: Harp -0.65, harmonics -0.35 (set in c05, before the c09 harp seat move).
- The harmonics stem's L/R correlation is 0.24, the lowest of all stems (`corr.py`).

**Fix (`build/mix.json` "Harp harmonics"):**
- `seat` -0.35 -> -0.65 (same as Harp).
- Its group width (0.3) is already the harp's.

**Check:** harmonics R-L within 2 dB of the harp in every band above 250 Hz.

## Ranking rationale

#1 is a clear, audible misplacement of a featured solo, and the fix is cheap. #2 is the largest remaining "one room" defect. It touches every phrase end, but it needs a reverb change and a test. #3 is a tone/low-end issue for the whole movement, with ReaEQ and mic changes only. #4 and #5 are seat corrections. I did not find a sub-bass, high-frequency or decay-time problem worth ranking:
- 8-25 Hz is at the reference.
- 2-6 kHz share is -10.5 (target met).
- The final decay matches Brahms.

Do not touch:
- the reverb decay time and level (final-release drop matches Brahms)
- the 5.5 kHz hall high cut
- pre-delay 30 ms
- the send order (strings 0.25 < winds 0.35 < low brass/timp 0.45 < horns 0.5)
- the string, horn, trombone and woodwind seats (horns are now monotonic -5.5 to -3.7 dB; the strings are in order)
- the widths from c09
- all high-passes and the sub-bass result (8-25 Hz at the reference)
- the Vln I 5 kHz shelf (2-6 kHz share at target)
- the Vc 170 Hz bell
- Close + Main on every patch, with no Surround or Mid (the memory cost is too high)
- the Cbn/Tuba 70 Hz shelves
- the `mute_eq` on Horns 3-4
