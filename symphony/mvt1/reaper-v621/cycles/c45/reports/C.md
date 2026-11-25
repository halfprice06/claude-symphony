# Critic C, cycle 45: blend and space (render c44)

Render under review: c44 (`cycles/c44/render`, master = float sum of 40 stems, `rendered_build/parts.json`), compared with c43 and with the reference recordings: the Dvořák 9/i MP3 (decoded; measured with the same scripts as the mockup) and the stored metrics of Brahms 1/i, 4/i, 1/ii, 4/ii and the Dvořák (`symphony/render/critics/c00|c04/ref_*/metrics.json`, made with `symphony/render/tools/rtk.py`). Scripts were numpy only (STFT 4096, hop 2048 or 4096, 48 kHz). "Loud" = the top 10% of active frames by K-weighted level, "soft" = the bottom 30%. Each judgement below is marked measured, simulated (applied to the c44 stems in the STFT domain, where the master is the exact sum of the stems) or inferred.

## Manual notes (second reading of the c39 slot C row: PDF pp. 138-139, 141-142, 219-223, read in full; p.138 and p.221 also as images; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items in this lens first: **#4 Mid instead of Close** is still open and untried (see the deferred items at the end: not now). **#7 half-section divisi** is still open (deferred items: pass-2 conditions given). **#3 solo cello** is still not installed. The DIV A stand-in in pass 2 measures as a spot-lit soloist: stem correlation 0.96-1.00, and its tail at 0.15-0.25 s after phrase ends is 4.1 dB drier than the celli section's (-18.8 against -14.7 dB re body). That is acceptable for a solo.

| Page | What it says | c39 note | Now (c44) |
|---|---|---|---|
| p.138 | Close = presence; Mid = "definition without the sound of close proximity"; Main = fifth row, Decca tree and outriggers, "big, unified sound"; Surround = depth | Partly followed: on 13 tracks at width 0.05 the Main pair is folded into a point | **Still not followed, and it now matters more.** The hall that used to give those tracks their width is 6 dB lower, so the image narrowed (finding 1). |
| p.139 | Each mic sub-mix has its own volume, **panning**, load and mute | Per-mic panning not used | Still not used. `apply_mix()` gives every mic of a track the same seat ± width (finding 1). |
| p.141 | Channel routing; Stereo Double widens the image (stereo routing only) | Not needed | Still not used. Widen first with the recorded Main pair, which is real decorrelation, before trying an effect whose working is not described (inferred). |
| pp.141-142 | One convolution reverb per instance ("Master"): preset, pre-delay, volume | Followed | Followed. One hall for all instances in both passes: fx 0.095, 30 ms pre-delay, true stereo. |
| p.142 | Envelope: "be careful when changing" the stages | Release caps on the low strings only | c44 caps the string Sus MAX / Sus Marc LITE releases at 150 ms and the horns at 237 ms. No ending falls more than 10 dB in its first 0.05 s (actor's c44 measurement), so the manual's warning is respected. |
| p.219 | Algoverb (early/late, size, stereo) | Not needed | Not needed. |
| p.220 | Reverb insert: true-stereo IRs, IR envelope, Bandpass (high/low cut 30 Hz-18 kHz), **Width 0-200%** (default 100%), wet/dry | Followed (true stereo, high cut 5.5 kHz) | Low cut 160 Hz added in c44. **New note:** the insert's Width is the hall's own stereo-spread control. The state key is `"width": 1.0` and it is unused. It is the fallback lever in finding 1. |
| p.221 | IR envelope: Simple (one Decay slider for end and fade) or Full (start, end, fade times and curves) | Unused | **Now followed** with Full: `envelopeMode` 2, `endPos` 0.5, `decayLength` 0.5. The Simple slider's state key `simpleDecay` does nothing (c44 test). |
| p.222 | Mixing mics runs from "small and dry" to "large and wet"; the room "is heard as long as the samples are playing (**including the release trail samples**)"; one mic for a whole piece is possible; separate passes need less memory | Followed (two mics; pass 2) | **New note:** the release trails carry the recorded room. Their gains differ by patch from -4.7 to +12 dB, and with the drier hall they now set each family's early tail (finding 2). |
| p.223 | Each mic to its own output | Optional | Not needed. |

## Verdict on the hall: c44 is right, at the dry edge of the recordings. Do not dry it further (measured)

- **Decay at tutti stops, on the references' own detector** (rtk `cutoff_decays`: 30 ms frames, a 0.4 s hold, then a fall of at least 15 dB, or 12 dB for the Dvořák, within 0.4 s).

  | Recording | Stops detected | Time to -20 dB | RT60 from the -5..-20 dB slope |
  |---|---|---|---|
  | c44 | 5: bars 14, 26, 72, 138, 170 | 0.45 / 0.54 / 0.55 / 0.45 / 0.53 s (median 0.53) | 0.85 / 1.11 / 1.70 / 1.05 / 0.96 s (median 1.05) |
  | Brahms 1/i | 12 | 0.43-0.55 s (median 0.485) | 1.13-1.62 s (median 1.33) |
  | Dvořák | 1 | 0.50-0.58 s | 1.32-1.34 s |
  | c43 | 1: bar 14 (0.60 s, RT 1.84 s); the other stops did not fall fast enough to pass the detector | | |

- **Do not compare the actor's "drop at 0.3 s" with the recordings.** The actor's 17.8-20.8 dB starts from the first frame 2 dB under the pre-level, which is later than the detector's start. On the same cut-offs, the detector's start gives a 0.3 s drop of 7-14 dB for c44 and 11.1 dB for the Dvořák. The "13-17 dB in recordings" figure was measured another way.
- **Late slope.** At the fermata the -20..-35 dB slope is 1.78 s (actor), against 1.5-1.95 s in recordings (KIT §12).
- **The end of the IR is inaudible.** The IR now stops at 1.65 s (endPos 0.5 of 3.3 s). At 1.4-1.6 s after phrase ends the per-stem tail medians are already -65..-72 dB re body, so the truncation cannot be heard (inferred).
- **Early against late.** In the pass-2 hall test (`cycles/c44/halltest/render_r1`) the envelope leaves the hall at +0.15 s unchanged (-9.5 -> -9.8 dB) and cuts +0.3 / +0.6 / +1.0 s by 1.2 / 3.7 / 7.8 dB. On the master, the early slope is the faster part (RT 1.05 s against the references' 1.33), while the late slope is inside the recorded range. If Dan ever hears c44 as too dry, raise `fx_volume` (0.095 -> 0.12, +2 dB). Do not change endPos.
- **One hall.** The per-family tails at 0.4-0.6 s after phrase ends are within 1.8 dB of each other: winds -26.4, horns -24.6, trumpets -24.9, low brass -25.3, strings -25.9 dB re body. The families still share one late room. The first 0.25 s differs (finding 2).
- **Generic for all movements:** keep `fx_volume` 0.095, `low_cut_hz` 160 and `ir_setup` {2, 0.5, 0.5}. Judge the hall with rtk's detector (target: time to -20 dB of 0.43-0.58 s and RT 1.1-1.7 s), not with a fixed 0.3 s drop.

## Is it still mushy? Where it comes from now (measured)

- **Low-mid build-up: none.**
  - 200-500 Hz share: loud -6.0 / soft -4.2 dB, against the Dvořák's -6.2 / -4.8.
  - 112-224 Hz is short, not heavy (finding 4).
- **The hall: in range** (verdict above).
- **Definition.** Measured as the 3-10 Hz modulation of band envelopes (dB SD, the same method on all three files), in bands 60-200 / 200-500 / 500-1k / 1-2k / 2-5k Hz:

  | | Loud windows | Mid-level windows |
  |---|---|---|
  | c43 | 1.76 / 1.31 / 1.32 / 1.42 / 0.97 | 1.48 / 1.74 / 1.70 / 1.48 / 1.16 |
  | c44 | 1.84 / 1.36 / 1.38 / 1.42 / 1.01 | 1.58 / 1.83 / 1.79 / 1.49 / 1.20 |
  | Dvořák | 2.06 / 1.32 / 1.50 / 1.29 / 1.24 | 2.16 / 1.81 / 1.92 / 1.62 / 1.52 |

  - c44 is clearer than c43 in every band.
  - From 200 Hz to 2 kHz it is within 0.13 of the recording.
  - The two gaps left are 2-5 kHz (-0.23 / -0.32: attack edge; accents are level swells, MANUAL-GAPS #1, lens A) and 60-200 Hz (-0.22 / -0.58).
  - The basses flatten the low band: without their stem, the mid-level 60-200 Hz modulation rises from 1.58 to 1.81. The timpani strokes add definition: without them, the loud value falls from 1.84 to 1.52.
- **Overlap inside the sections.** Violins II détaché still sounds its old pitch at -10 dB 0.254 s after the note-off. Halving the hall moved that point by only 31 ms (0.285 -> 0.254 s, actor c44), so the hall does not set it. The samples' release trails do (finding 2).

## Findings, ranked by what a listener would gain

### 1. The stereo image narrowed outside the range of all five references, most of all below 250 Hz (measured; fix part simulated, part inferred)

**Where.** The whole movement: loud, soft and all frames alike (side/mid -7.4 / -7.3 / -7.3 dB).

**Evidence (measured; same band edges as rtk).**

| | Correlation < 250 Hz | 250 Hz-4 kHz | > 4 kHz | All | Side/mid |
|---|---|---|---|---|---|
| c43 | 0.585 | 0.573 | 0.539 | 0.570 | -5.6 dB |
| c44 | **0.781** | **0.684** | 0.550 | **0.685** | **-7.3 dB** |
| Dvořák (decoded) | 0.560 | 0.562 | 0.412 | 0.547 | -5.3 dB |
| Brahms 1/i, 4/i, 1/ii, 4/ii (stored) | 0.54-0.62 | 0.47-0.54 | 0.38-0.48 | 0.49-0.55 | -4.7..-5.4 dB |

- Finer bands, c43 -> c44: 20-120 Hz 0.71 -> 0.85, 120-250 Hz 0.55 -> 0.76, 250 Hz-1 kHz 0.56 -> 0.69, 1-4 kHz 0.60 -> 0.67.
- c43 matched the references. c44 is narrower than every one of them in every band below 4 kHz.
- Per stem, the winds, horns and Trumpet 1 at width 0.05 now read 0.85-0.97 at 250 Hz-1 kHz (c43 0.36-0.86); celli 0.77 -> 0.87, basses 0.76 -> 0.85.
- **Cause (inferred from c43 against c44).** The dry orchestra is narrow. The true-stereo hall supplied the decorrelated part of the image, and it is now 6 dB lower and has no input below 160 Hz.
- On top of that, six bass tracks still carry the side-only low cuts added in c20-c29 to stop the louder true-stereo hall from decorrelating the bass: Contrabassoon, Bass trombone and Tuba lowshelf 200 Hz -2; Timpani {200, -2}; Violoncellos and Double basses side bell 170 Hz -2. The problem they solved has gone, and they now narrow the bass further.

**What does not work (simulated).** Side-only high shelves on every family, like c21's, do reach side/mid -5.5 dB. But they widen the image by pushing panned seats outward, not by adding spread: Horn 1 R-L -8.4 -> -10.6, Tuba +7.5 -> +9.7, basses +7.2 -> +9.7 dB. Do not use them.

**Fix, step 1 (now; mix only, `--mix-only`; simulated).** In `build/mix.json` `side_shelf`, set the six low cuts to 0 dB instead of deleting them, so the FX stays in place:
- Contrabassoon, Bass trombone, Tuba: drop the `{"band": "lowshelf", "hz": 200, "db": -2}` item and keep the 250 Hz +1.5 high shelf.
- Timpani: `{"hz": 200, "db": 0}`.
- Violoncellos and Double basses: `{"band": "bell", "hz": 170, "db": 0, "bw_oct": 1.0}`. Keep the celli's `side_shelf_switched`.

Simulated result:
- master correlation < 250 Hz 0.781 -> 0.710; 120-250 Hz 0.762 -> 0.678; 20-120 Hz 0.852 -> 0.828;
- above 250 Hz unchanged;
- these stems' low-band seats move 0.1-0.9 dB (Tuba +0.9, celli +0.8, basses +0.8 dB R-L in 30-250 Hz);
- the mid (mono) sum is unchanged by construction.

**Fix, step 2 (now; Opus state change; the per-mic width deferred since c39; memory neutral).**
- In `tools/build_reaper.py apply_mix()`, in the `for c in subs.values():` loop:
  ```python
  wd = max(m["width"], (m.get("width_by_mic") or {}).get(c["label"], 0.0))
  c["panLeft"] = max(-1.0, m["seat"] - wd)
  c["panRight"] = min(1.0, m["seat"] + wd)
  ```
  With `max`, a mic is never narrowed.
- In `build/mix.json`:
  - groups `wind`, `horn`, `trumpet` and `lowbrass`: `"width_by_mic": {"Main": 0.35}`. The groups reach every track and alias of those families, including Horns a2, Trumpets a2 and the three stac aliases;
  - tracks Violoncellos and Double basses: `"width_by_mic": {"Main": 0.45}`;
  - the Close mics keep the track width (0.05 / 0.28 / 0.3 / 0.5), so they still anchor each seat.
- Why the Main mic: at equal volume the two mics measure about the same level (KIT: Main 0.28 measured 11 dB under Close 1.0). So in these stems the Main is +4 dB over Close for the winds (0.8 / 0.5), +6 dB for the horns and trumpets (1.0 / 0.5) and +4.4 dB for the basses (1.0 / 0.6). It carries most of each stem, and today it is folded to the seat.
- Effect (inferred; a stereo pan model fitted to the measured stem correlations, hall ignored): celli 250 Hz-1 kHz 0.87 -> about 0.70, basses 0.85 -> about 0.67; less certain on the 0.05-width winds and horns.
- On the outer seats the wider Main moves the image up to about 1.4 dB toward the centre (Horn 1 at -0.48, constant-power model).
- Rebuild: about 25 main-pass tracks and the 4 pass-2 aliases, fully. Then re-match each track's K level by stem fix, since the coherent sum of the Main changes (expect up to about ±1 dB).
- Accept when:
  - master correlation < 250 Hz ≤ 0.65 and 250 Hz-4 kHz ≤ 0.62;
  - side/mid -6.0 dB or wider;
  - the solo winds' per-pitch R-L SD at 1.25-4 kHz ≤ 1.2 dB (the c35 method; c25 measured 1.7-2.5 dB at width 0.5 on both mics, 0.6-1.6 at 0.05). If it is over, use Main 0.2 on those tracks;
  - each changed stem's R-L within 1 dB of c44. If it is over, move that seat 0.05 outward.

**Fallback if step 2 leaves side/mid under -6.0 dB (a pass-2 test first).**
- Code: `rv["width"] = float(m.get("reverb_width", MIX["reverb"].get("width", 1.0)))` in `apply_mix()` (p.220 Width; state key `width`).
- Test with the c44 hall-test kit (`cycles/c44/halltest/make_halltest.py` variants, send 1.0) at width 1.0 / 1.5 / 2.0.
- Adopt 1.5 for the shared hall if the tail's L/R correlation (0.3-1.0 s) falls by 0.15 or more and the tail's L²+R² level rises 1 dB or less, so the decay stays inside the verdict's range.

**Generic for every movement.** After drying the hall, measure the master's side/mid against the references. Under -6 dB, do step 1 (any side-only low cut kept from the louder hall goes to 0) and step 2 (Main 0.35 on winds and brass, Main 0.45 on celli and basses, Close unchanged).

### 2. The patches' release-trail gains, -4.7 to +12 dB, now decide each family's early tail and the overlap inside the string sections (measured; patch states read; fix to be tested in pass 2)

**What is wrong.** p.222: the room "is heard as long as the samples are playing (including the release trail samples)". With the hall halved, the recorded release trails are the largest thing after each note-off, and the patch makers set their gains very differently. These are the RT groups (`releaseTrail: true`) on the loaded rows, `SourceProcessor.volume`, read from `jobs/*.b64`.

**Evidence (measured).** Tail at 0.15-0.25 s after phrase ends, median per family, dB re body, c43 -> c44, next to the patch's RT gain:

| Family (patch) | RT gain | Early tail c43 -> c44 |
|---|---|---|
| Horns (1FH) | 1.37-3.19, +2.7..+10 dB | -5.9 -> **-9.8** |
| Low brass (1TB) | 1.22-3.98 | -7.9 -> -11.0 |
| Trumpets a2 (2TP) | 2.05-3.98, +6..+12 dB | -8.3 -> -12.3 |
| Strings (1st/2nd Violins, Violas up to 3.98, +12 dB; Celli Sus up to 1.95; Basses 0.96) | see left | -8.9 -> -13.5 |
| Woodwinds | 0.84-1.36 | -10.3 -> -15.4 |
| Trumpets 1-3 (1TP) | 0.58-0.95, -4.7..-0.4 dB | -9.5 -> **-16.0** |

- The spread across families grew from 4.4 to 6.2 dB. The late tail (0.4-0.6 s) stays common (verdict).
- Two seams follow from it:
  - the Trumpets a2 alias (2TP) sounds 4.7 dB roomier than Trumpet 1 (-12.3 against -17.0), and it takes over at 520 and 664.5;
  - the solo trumpets moved from the strings' depth (c43: -9.5 against -8.9) to the driest family, because their own trails are the quietest.
- Inside the string sections, the 2nd Violins' Sus MAX trails play at up to 3.98 (+12 dB at mf). The détaché -10 dB point (0.254 s, against 0.238 s per eighth at 126) did not follow the hall (see "mushy" above), and the violas' figure still has its old pitch at -6.2 dB 70 ms into the next note.
- Capping the trails' AHDSR release does nothing (c22 `rt_ms` 400: rest drop 5.8 -> 5.7 dB), because a trail is a one-shot sample. The lever is the trail's gain.

**Fix (this is the release-trail test deferred from c44 C #2; do it now, in pass 2).**
- New `tools/build_reaper.py` mix key `"rt_gain_db"` {"db": D, "rows": [...] (default every loaded row)}: for every group with `g.get("releaseTrail")` whose regions sit on the listed rows, multiply each `SourceProcessor["volume"]` by 10^(D/20). Full rebuild of the track.
- Three `TEST_TRACKS` aliases in pass 2, each playing the main track's own notes: "Vln II rt test" (Violins II), "Vla rt test" (Violas) and "Hn1 rt test" (Horn 1), all at `rt_gain_db` -6. That costs about 2 GB in pass 2 and nothing in the main pass.
- Measure against the main stems:
  - Violins II détaché old-pitch -10 dB point after note-off ≤ 0.22 s (now 0.254);
  - the violas' figures' old pitch 70 ms into the next note ≤ -8 dB (now -6.2);
  - the early tail (0.15-0.25 s) of strings and horns moves into -13..-17 dB, toward the winds' -15.4;
  - the tail at 0.4-0.6 s within 1 dB of c44 (the hall's part);
  - no ending falls more than 10 dB in its first 0.05 s;
  - no more legato joins with 5 dB dips than in the main stems.
- If it passes, the generic values for every movement are: `rt_gain_db` -6 on the 1st Violins, 2nd Violins, Violas, Celli, 1FH, 2FH and 2TP KS Masters; -3 on 1TB; none on the woodwinds, 1TP and Basses (their trails are already 0 dB or below).
- Expected result: a family spread of about 4 dB instead of 6.2 (inferred). Since the horns may also be rebuilt for step 2 of finding 1, put their trail change into the next rebuild after the test.

### 3. Trumpet 1 still holds 72% of the top octave at bar 161, because one of its two climax shelves stops at 640 (measured; fix simulated)

**Where.** Trumpet 1, qn 642.9-644 (the B4/C5 notes after the fff A-flat5).

**Evidence (measured).**
- Trumpet 1's share of the master's 8-16 kHz: c43 -2.2 dB, c44 **-1.4 dB** (72%). c39's target was -3 dB or lower. The drier hall left the dry trumpet more exposed.
- Of Trumpet 1's two `loud_eq` shelves, 6 kHz -9 runs to 644.5 but 5 kHz -6 ends at 640.05.
- Everywhere else, trumpet and cymbal top-octave shares are within 1 dB of c43:
  - bar 160: trumpet -3.7, crash ring -9.6, suspended cymbal -19.0 dB;
  - the coda a2 trumpets: -5.2 dB.

**Fix (mix only; simulated).** In `build/mix.json` Trumpet 1 `loud_eq`, give the 5 kHz -6 spec the points `[[633.8, 0], [633.9, 1], [644.5, 1], [644.6, 0]]`. Simulated at 642.9-644:
- Trumpet 1 8-16 kHz share -1.4 -> -3.0 dB;
- master 8-16 kHz re 0.5-2 kHz -33.9 -> -36.5 (c43 -36.1);
- 2-5 kHz -8.6 -> -8.9, so the edge is kept.

### 4. Low end: no build-up. The loud 112-224 Hz deficit is the score's voicing, and EQ cannot close it (measured; options simulated). Change nothing

**Evidence (measured).** 112-224 Hz relative to 224-2245 Hz, which is robust to the Dvořák MP3's missing sub-bass:

| | Whole file | Loud | Soft |
|---|---|---|---|
| c44 | -9.4 | -9.8 | -8.1 |
| c43 | -8.5 | -9.35 | -5.8 |
| Dvořák | -5.8 | -5.0 | -8.4 |
| Brahms 4/i, 4/ii, 1/i, 1/ii (whole file) | -5.9, -6.6, -6.8, -9.0 | | |

- Loud-minus-soft at 157 Hz: c44 -1.8 (c43 -3.4); references +2.8 / +4.2 / +5.1 / +5.2 / -0.4.
- **The soft passages now match.** The deficit is only in loud passages.
- **Who fills the band in loud frames:** celli 30%, basses 29%, timpani 20%, Tuba 7%, Contrabassoon 4%, each trombone 2%.
- **Why (from parts.json, in the loud spans 100-104, 464-488, 520-534, 632-644 and 664.5-679).**
  - The celli sit on the G2 pedal: median 98 Hz, only 6% of their notes have a fundamental in 112-224 Hz.
  - The basses and Tuba lie at 49-73 Hz.
  - Only Trombone 2, Horn 4, the Bass trombone (58%) and Bassoon 2 (42%) have fundamentals there.
  - The band therefore comes from harmonics. The Dvořák's E-minor tutti is voiced differently.
- **Options (simulated over the celli's loud_eq spans).**

  | Option | Loud 112-224 Hz | Tutti loudness |
  |---|---|---|
  | +3 dB roles on Violoncellos, Double basses, Tuba, Bass trombone, Contrabassoon, Bassoon 2 | -9.8 -> -8.2 | +0.7 dB |
  | A further +3 dB 150 Hz bell on celli and basses | -8.4 | +0.1 dB |
  | +3 dB 140 Hz bell on trombones and horns | -9.7 | 0 |

  The celli already carry +6 (150 Hz) + 3 (170) + 3 (125) dB in those spans, and the basses +6 (160) + 4 (180).
- The c43 render, with a hall twice as loud and no low cut, was only 0.5 dB fuller here. The hall low cut is not the cause.

**Fix.** None. Keep the loud_eq bells and `low_cut_hz` 160. Do not add low-mid EQ or bass roles to chase the Dvořák's -5.0: the first 1.6 dB would cost 0.7 dB of tutti loudness and change the balance. The low cut's measurable cost is the bass image (finding 1, step 1).

**Generic:** measure 112-224 Hz relative to 224-2245 Hz in loud and soft frames against several references, and check the voicing in parts.json before adding EQ.

## Deferred items: do them now?

- **Per-mic width (deferred since c39): yes, now.** Use finding 1, step 2 (Main 0.35 on winds and brass, Main 0.45 on celli and basses, Close unchanged), with step 1 in the same cycle. It is the one fix for the narrowed image that does not move seats.
- **Release-trail test (c44 C #2): yes, now, as the pass-2 test of finding 2** (`rt_gain_db` -6 on Violins II, Violas and Horn 1 test aliases). Adopt after it passes; it needs no main-pass memory.
- **Viola divisi (c44 A #4): only if A's articulation case stands, and in pass 2.**
  - The DIV patches are Close only (p.89-90). The only Close-only stem rendered so far, the DIV A Cello solo at send 0.5, measures 4.1 dB drier in the early tail than its section and is a point source (correlation 0.96 against the celli's 0.87).
  - If it is done:
    - DIV A at seat 0.10 and DIV B at 0.20 (the left and right chairs around the violas' 0.15), width 0.25 each;
    - send 0.5 (the Close-only convention), gains matched to c44's chord level.
  - Accept only if the pads' early tail (0.15-0.25 s) is within 2 dB of the Violas section's (-13.0 dB re body), and the two DIV stems summed read 0.80 or less at 250 Hz-1 kHz (section now 0.77). If the pads are drier than that, send 0.75 is the next step for these Close-only tracks only. It does not reopen the shared hall.
- **MANUAL-GAPS #4, Mid instead of Close on the solo winds: not now.**
  - The winds are 1.9 dB drier than the strings in the early tail (-15.4 against -13.5). Finding 2 is expected to bring the strings to about -15..-16 (inferred), which closes that gap without a mic swap.
  - Test Mid (`{"Mid": 0.5, "Main": 0.8}` on Flute 1, Oboe 1, Clarinet 1 and Cor anglais aliases, memory neutral) only if, after finding 2, the winds' early tail is still more than 2 dB drier than the strings'.

## Standing checks (measured on c44)

- **Item 7, loop pulsing.** Master 100-300 Hz / centroid autocorrelation at 3.95 s: final chord +0.04 / -0.05 (controls at 2.6 / 3.3 s: +0.06 / -0.03), Lento +0.15 / +0.09, sostenuto 484-500 -0.20 / -0.07. These are c43's values; the drier hall did not expose the loops.
- **Item 8, brass accents.** Data unchanged since c41; not re-measured.
- **S1 to S3 (actor c44).**
  - S1: master dips portato 3.6, strokes 4.5, soft 2.2 dB.
  - S2: probe legato SD 49 / 42 / 52 / 50 ms.
  - S3: bar 62 falls -1.5 / -5.2 / -8.9 / -12.2 dB, as in c43.

Do not touch: the shared hall (fx 0.095, low cut 160 Hz, `ir_setup` envelopeMode 2 / endPos 0.5 / decayLength 0.5, the IR, true stereo, wet 2.0, high cut 5.5 kHz) and every send. The 150 / 237 ms release caps. The seats. Width 0.05 on the Close mics of the solo winds, horns and Trumpet 1 (they hold the per-pitch image still). The celli `side_shelf_switched` and all 250 Hz side high shelves. The loud_eq low-mid bells on celli, basses and low brass. Trumpet 1's 6 kHz climax shelf and the Trumpets a2 3.2 kHz bell. The crash ring under the bar-160 stroke. The Harp's side shelf (300 Hz -8).
