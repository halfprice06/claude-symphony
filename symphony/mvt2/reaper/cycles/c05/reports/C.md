# Cycle 5, critic C: blend and space (on the cycle 4 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets, low-end build-up against the reference spectrum.

Material: c04 `render/` master and 27 stems, `build/parts.json`, `build/mix.json`, the Opus states actually sent to REAPER (`jobs/*.b64`, decoded), the `.oib` patch files, the HO and Opus manuals, and the Dvorak 9/i reference. The reference is a live student recording at 128 kb/s MP3 (assets README), so I use it for decay and the low-band balance, with a few dB of allowance. The two Brahms slow-movement FLACs listed in the assets README are not on disk.

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c05-C/`:
- `stems.py`: per-stem L/R balance, correlation and band spectrum.
- `tails.py` + `decay.py`: decay after each note cutoff, per stem and for the master.
- `tailpan.py`: L/R balance of the sustained sound against its reverb tail.
- `lowbands.py`, `lowcontrib.py`: low bands against the reference, and which stem makes each band.
- `mics.py`: the mic and send settings decoded from the `.b64` states.
- `irsetup.py`: every impulse response used across the 1683 `.oib` files.

## 1. The hall is about 1 s too long: a 3.4 s Hollywood-hall IR on top of the Main mic's own room (measured; audible effect inferred)

**Where:** every track, all 92 bars. It matters most where chords change on each beat at 52-56 bpm (bars 15-30, 41-52, 65-92), and at the cutoffs in bars 63 and 81-82.

**Evidence (measured):**
- Every Opus instance runs `impulseA = "//ir/QL SPACES TEASER/S. Cal. Hall strings LR Rear"`, taken from `reverb.from_patch` (1st Violins KS Master). The HO manual (Moods, Classic) describes this hall as having "a long, 3.4 second decay time". The Main mic adds the studio's own reflections on top of it (HO manual, Microphone Positions: the Main mic captures "more room reflections than direct sound").
- Decay after cutoffs, from fitted slopes:
  - c04 stems: the late slope (-20 to -40 dB) has a median of 3.1 s across 27 stems (range 2.4-4.7). The early slope (-5 to -25 dB) is 2.1-3.8 s.
  - c04 master after the final chord: 2.3-2.7 s in the 250 Hz-2 kHz octaves.
  - Reference, final chord at 573.1 s: 1.5 s early, 1.95 s late. Its other cutoffs (54-58 s) measure 1.2-1.5 s.
  - The Detmold Konzerthaus IRs in `assets/ir/` (a real concert hall) are documented at RT30 of about 1.6 s.
- Level drop after the final chord, at 0.3 / 0.6 / 1.0 s:
  - mockup master: 9.9 / 16.3 / 28.2 dB
  - reference: 16 / 28 / 43 dB
- Per-stem drop 300 ms after a cutoff: median about 10 dB. The reference drops 16-19 dB.

**Effect (inferred):** each chord is still sounding 10-15 dB louder than in the reference when the next one arrives. The adagio is smeared into the "sample library in a big hall" wash, and the harmonic changes lose definition.

**Fix (`build/mix.json` only; `tools/build_reaper.py` needs no change):**
- Set `reverb.from_patch` to `/Volumes/MAC DRIVE/EW Hollywood Orchestral Woodwinds Diamond/Hollywood Orch Woodwinds Opus Instruments/3 Bassoons/01 Long/3BS Sus MAX.oib`.
  - Its `fx:0` ConvolutionReverb uses `//ir/latest PLAY impulses final/New Hollywood Hall 2.0` with a 30 ms pre-delay.
  - `irsetup.py` found this IR in 87 patches, and also found "New Hollywood Hall 2.6". It is an EW hall that ships with Opus, so no file has to be loaded.
  - `shared_reverb()` copies the whole insert, including `impulseA` and `delay`.
- Keep `wet` 2.0 and the group sends. Re-tune `reverb.fx_volume`, starting at 0.151, so that the reverb level during sustained tutti stays within 1 dB of c04.
- Patch states change, so every track needs a full rebuild, not `--mix-only`. No new samples load.

**Targets, checked with `tails.py c05`:**
- median late slope of the stems 1.8-2.3 s
- median 300 ms drop of 13-17 dB
- master drop 0.6 s after the final chord of at least 22 dB

If 2.0 s turns out too dry once the Main mic room is added, try "New Hollywood Hall 2.6". It appears in `Drums/12in Lefima Tambourine.oib`, whose pre-delay of 0.5 s must be overridden to 0.03.

## 2. Low-end build-up: the double-bass Close mic makes the 40-90 Hz band, and the upper strings add sub-40 Hz rumble (measured; the mic cause is inferred)

**Where:** the whole movement. It is worst at the climaxes (bars 59-62, 77-80) and in the soft string passages (bars 23-28, 65-66).

**Evidence (measured; master, octave sub-bands re 400-1000 Hz, loudest 20% of 1 s frames):**

| | 25-40 | 40-63 | 63-90 | 90-125 | 125-180 |
|---|---|---|---|---|---|
| c04 | -39.5 | -25.3 | -13.0 | -11.7 | -9.5 |
| reference | -45.5 | -36.8 | -21.8 | -11.8 | -3.7 |

- The mockup has 9-11 dB too much at 40-90 Hz and 6 dB too little at 125-180 Hz. The c04 metrics show the same in octave bands: 63 Hz +1.1 against -6.2, 125 Hz +3.8 against +7.0.
- `lowcontrib.py`: the double basses alone make the master's 40-63 and 63-90 Hz bands (within 0.5 dB) in every window tested. The Cb stem's own 40-90 Hz is +12.7 dB re its 400-1000 Hz.
- The Basses KS Master runs with its default mic mix (`groups.string.mics` is null): Close 0.94 and Main 1.0, i.e. Close only 0.5 dB under Main. Violins and violas run Close 0.66 (-3.6 dB) and Celli 0.65. Inferred: the close pair in front of the basses gives a fundamental-heavy proximity sound that a hall listener never hears. That is the "boom without body" shape above.
- The 25-40 Hz band (-38.5 overall against the reference's -45.3) is mostly not the basses. In bars 23-28, Violins II alone is within 3.1 dB of the master's 25-40 Hz energy, and Violins I and Violas are next. Their stems carry room rumble peaking at 16-29 Hz, 34-40 dB under their total level, summed over every Main-mic instance.

**Fix:**
- `build/mix.json` `tracks."Double basses"`: add `"mics": {"Close": 0.4, "Main": 1.0}` (full rebuild of that track). Raise `gain_db` from -9 to about -7 so the 200-1000 Hz bar levels stay within 1 dB of c04, then re-measure before touching the EQ.
- If 40-90 Hz is still more than 4 dB over the reference, change the Cb EQ:
  - low shelf: 90 Hz -7 → 80 Hz -9
  - bell: 150 Hz +3 → 140 Hz +4, bw 1.2
- `tools/build_reaper.py` ENV_LUA eq code: support `{"band": "highpass", "hz": N}` by enabling ReaEQ band 4 (now disabled) as a high-pass. Then in `mix.json`:
  - 40 Hz on Violins I/II, Violas, Flutes, Oboes, Cor anglais, Clarinets, Horns 1-4, Trombones 1-2 and Harp harmonics
  - 30 Hz on Violoncellos, Bassoons, Bass clarinet and Bass trombone
  - nothing on Cb, Cbn, Tuba, Timpani and Harp (low E flat 1 = 39 Hz)

**Targets (`lowbands.py`, loud frames):**
- 25-40 Hz ≤ -43
- 40-63 Hz ≤ -32
- 63-90 Hz ≤ -18
- 125-180 Hz ≥ -7

## 3. Each instrument carries its own reverb, panned and narrowed with it: 27 small rooms instead of one hall (measured; audible effect inferred)

**Where:** all tracks. It shows most on the outer seats (Violins I, Horn 2, Violoncellos, Double basses, Harp harmonics) and at every phrase end.

**Evidence (`tailpan.py`, R minus L in dB, sustained sound 0.25 s before a cutoff → reverb tail 0.35-1.2 s after it):**
- Violins I -10.0 → -9.2
- Violins II -5.0 → -5.1
- Violoncellos +4.0 → +6.0
- Double basses +6.7 → +6.2
- Horn 2 -9.6 → -12.6
- Bass clarinet -5.8 → -5.9
- Tuba +5.3 → +4.8
- Harp harmonics -14.7 → -11.7
- Tail correlation is 0.5-0.97 (Harp 0.93, Flute 2 0.97).

The cause is in the signal chain. The hall is the `fx:0` convolution inside each Opus instance. REAPER's stereo pan (`I_PANMODE 5`, `seat`, `width` 0.5-0.6) comes after the plugin, so it moves and narrows the dry sound and its reverb together.

In a hall the reverberant field reaches the listener from everywhere, whatever the source position. The reference's final-chord tail gets wider after the cutoff (correlation 0.58 → 0.44, side/mid -5.3 → -3.6 dB). The mockup's does not (0.51 → 0.53).

A second consequence of the same chain (inferred): every `vol_db` move (role trims, note trims, sf weight, timp settle, final fade) changes the tail of notes already sounding, because the envelope sits after the reverb.

**Fix (`tools/build_reaper.py`):**
- In `apply_mix`, pan inside Opus instead of in REAPER. For each loaded `sub:` channel set `panLeft = max(-1, seat - width)` and `panRight = min(1, seat + width)` (keep `pan` 0). Set the REAPER track to `D_PAN 0`, `D_WIDTH 1`.
- The `SendProcessor` to `fx:0` is an insert on the mic channel. So the reverb input should be the unpanned mic signal (inferred), and the `fx:0` return stays centred at full width (`panLeft -1`, `panRight 1`).
- Patch states change, so this needs a full rebuild. It can share one rebuild with #1.

**Targets (`tailpan.py`):**
- sustained R-L within 1.5 dB of c04 for each stem, so the seats stay where they are
- tail R-L within ±4 dB for every stem
- median tail correlation ≤ 0.6
- master correlation 0.58-0.68 (c04 0.64, reference 0.60)

**Fallback if the tail still follows the seat** (the Opus send turns out to be post-pan): build a REAPER "Hall" bus. Opus reverb off (`fx_volume` 0). A JSFX volume after Opus carries the `vol_db` envelope. Each track sends post-FX/pre-fader (`I_SENDMODE 3`) to the bus at the group send level, and the bus runs one stereo convolution. This also fixes the envelope-rides-the-reverb problem.

## 4. Depth is inverted for the back of the orchestra: timpani and tuba are close-miked, the violins in front are not (settings measured; the effect partly measured, partly inferred)

**Where:** timpani throughout, especially the soft rolls (bars 52, 67-70, 82-84, 92); tuba in bars 57-63 and 77-81.

**Evidence:**
- Decoded `jobs/19_Timpani_Flt_KS.b64`: Close 0.43, Main 0.24. That is Close 5.1 dB over Main, set explicitly in `groups.timp.mics`.
- `jobs/18_1TU_KS_Master.b64`: Close 1.0, Main 1.0 (`groups.lowbrass.mics` is null, so the patch default applies). The trombones in the same group default to Close 0.486.
- Violins run Close 3.6 dB under Main, horns and trombones 6 dB under.
- HO manual, Microphone Positions: Close mics are "placed in front of each section to capture the sound coming directly from the instruments". So the instruments furthest from the listener carry the most direct sound.
- Measured: in bar 52 (timp pp roll with a printed cresc. to p, cor anglais p solo) the timpani is the loudest stem (-48.1 dB against cor anglais -49.5). This contradicts Dan's rule 5. The timpani stem also has the lowest stereo correlation of any track (0.54): its close pair is wide and near.

**Fix (`build/mix.json`, full rebuild of the two tracks):**
- `groups.timp.mics`: `{"Close": 0.2, "Main": 0.5}`. This keeps roughly the same summed amplitude, with Close about 8 dB under Main.
- `tracks.Tuba`: add `"mics": {"Close": 0.45, "Main": 1.0}`, and raise Tuba `gain_db` by about 2 dB so its f/ff medians stay where they are.
- Do not load the Surround mics: they add sample memory, and the c04 render froze the Mac.

**Targets:**
- timpani at least 2 dB under the cor anglais in bar 52, and never the loudest stem during a pp/p roll
- timpani tail drop at 300 ms closer to the strings' value than now
- tuba stem f/ff medians within 1 dB of c04

## 5. Harp harmonics come from a different place than the harp (measured)

**Where:** bars 82-83 (Harp harmonics track, mp).

**Evidence:**
- Whole-piece R-L: Harp harmonics -9.5 dB, Harp -4.2 dB.
- At cutoffs: -14.7 against -3.3.
- Both use seat -0.6, width 0.55, Close 0.6 / Main 1.0. The Harmonics patch's own stereo image sits further left, so one harpist appears 5-11 dB apart depending on the articulation.

**Fix:**
- `build/mix.json` `tracks."Harp harmonics".seat`: -0.6 → -0.35 (`--mix-only` is enough if #3 is not done; with #3, the same seat goes into the Opus pans).
- Target: R-L within 2 dB of the Harp's (`stems.py`).

## What works (measured)

- Overall width matches the reference: median frame correlation 0.64 against 0.60, side/mid -6.0 against -5.9 dB.
- The seating order reads correctly: Violins I -8.7 dB R-L, Violins II -3.8, Violas +1.1, Violoncellos +5.8, Double basses +5.2, horns left (-4 to -7), low brass right (+1.6 to +7.3).
- The top end matches the reference within 1.5 dB at 2, 4 and 8 kHz.
- Every patch already shares one IR, so the colour of the room is uniform; only its length, its panning and the mic balance are wrong.

Do not touch: the seat order and the c04 widths (master correlation is on target; only move the panning into Opus as in #3, with the same values); the per-group send ordering (strings 0.25 < wind 0.35 < lowbrass/timp 0.45 < horns 0.5); the shared-IR mechanism in `shared_reverb()`; the ReaEQ scheme (extend it, do not replace it); the 2-8 kHz balance.
