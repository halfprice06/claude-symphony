# Cycle 25, critic C: blend and space (on the cycle 24 render)

Lens: one room. Reverb, seating and panning, mic positions (Close/Main/Surround column volumes), tone matching between sample sets, low-end build-up against the reference spectrum.

Under review: `cycles/c24/render` (master and 32 stems), `cycles/c24/metrics`, `cycles/c24/CHANGES.md`, `build/parts.json`, `build/mix.json`, `tools/build_reaper.py` (`config_eq`, `mute_lua`, `set_side_shelf`), the built Opus states in `jobs/*.b64` (mic columns, pans, sends, hall insert), score pages 2-3 and `build/mockup-events.tsv`.

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c25-C/`:
- `cbpitch.py`: per-pitch fundamental vs harmonics 2-4 on sustained notes of any stem (`F=file.wav` to run it on a simulated stem)
- `loudblocks.py`: the loud-third 2 s blocks of the master, with their 30-100 Hz share and the Cb pitches sounding in each
- `eqsim.py`: RBJ bell/shelf responses applied by FFT to a stem
- `cbsim2.py` to `cbsim6.py`: Cb EQ variants, master = (master - Cb) + new Cb
- `barcmp.py`, `cbh.py`: per-passage results
- `lowpow.py`, `lowdist.py`, `lowbars.py`, `lowcontrib.py`, `bands.py`: the c21 tools rerun on c24
- `refbands.py`, `leansim.py`, `hfsim.py`, `bodyshare.py`, `ltas.py`, `rtband.py`, `states.py`, `irs.py`, `divtone.py`

Delivery numbers (c24 metrics; this lens does not move them):
- master: -22.5 LUFS, LRA 23.7 LU, TP -3.9 dBFS
- mp3: -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, span 18.4 dB, limiter 1.9 dB
- The proposed change lowers the master's plain integrated RMS by 0.05 dB and the sample peak from 0.636 to 0.627. K-weighting almost ignores the band it acts on, so LUFS, LRA and the mp3 ride should not move.

## Where the room stands (measured)

The c21 changes landed as simulated. Master L/R correlation per band, with the Dvorak reference (`refbands.py`):

| | 25-60 | 60-120 | 120-250 | 250-500 | 500-2k | 2-6k | 6-16k |
|---|---|---|---|---|---|---|---|
| c20 | 0.90 | 0.88 | 0.71 | 0.63 | 0.62 | 0.51 | 0.48 |
| c24 | 0.72 | 0.76 | 0.56 | 0.56 | 0.55 | 0.50 | 0.47 |
| Dvorak 9/i | 0.48 | 0.56 | 0.56 | 0.52 | 0.57 | 0.66 | 0.31 |

- Mids are 0.55, against Brahms 0.48/0.52.
- Seats read as intended at 500 Hz-2 kHz. In R-L dB: Vln I -7.5, Vln II -3.6, Violas +1.7, Vc +5.2, Cb +7.3, horns -3 to -4.5, trombones +4.6 to +6.6, Fl1 -2.5, Ob1 +3.7, CA +5.2, harp -8.3.
- Every patch uses one hall: `S. Cal Hall Perc TS FR 3.3s`, true stereo, low cut 30 Hz, high cut 5.5 kHz, read from the built states. It is the only true-stereo IR in the 1683 HO patch files (`irs.py`), so there is no per-section true-stereo IR to switch to.
- The Close/Main/send ratios still run front to back, as in c21.

What is left is the low end, and it is a matter of one sample set's pitch response.

## 1. The double basses boom on C2-G2: on those notes the fundamental is as loud as harmonics 2-4, while E1-Bb1 sit 12-30 dB under. Loud passages carry 5.6 dB more 30-100 Hz than the reference. Add a static 80 Hz cut to the Cb and retune the two passage EQs it would stack on. Measured; fix simulated on the c24 stems. That a real section is not this uneven is inferred.

**Where:** Double basses wherever they hold Db2, D2, F2, Gb2 or G2:
- bars 23-29 (con sord., p < mf)
- bars 53-59 (the p-mp-mf-f crescendo into the climax)
- bars 65-66 (the pp Eb2 pedal, "change bow at will")
- bars 75-77 and 87-88

The Cb supplies 87-91% of the master's 30-100 Hz in both the soft and the loud thirds (`lowcontrib.py`).

**What is wrong:** the c21 `loud_eq` fixed the ff climaxes. Bars 60-62 now read -15.6 to -27.5 dB (master 30-100 Hz re 250 Hz-2 kHz, per bar). The boom moved to the passages around them, and it follows pitch, not dynamic.

**Per pitch (`cbpitch.py`, Cb arco sustains, f0 re harmonics 2-4, median):**

| pitch | E1 | F#1 | Ab1 | A1 | Bb1 | B1 | C2 | Db2 | D2 | Eb2 | F2 | Gb2 | G2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f0 Hz | 41 | 46 | 52 | 55 | 58 | 62 | 65 | 69 | 73 | 78 | 87 | 92 | 98 |
| dB | -31.6 | -15.9 | -18.1 | -22.0 | -11.6 | +3.9 | 0.0 | -0.1 | +8.6 | -5.1 | +9.5 | -7.0 | +6.7 |

In the same render, the tuba, bass trombone and contrabassoon fundamentals in this range sit 11-24 dB under their harmonics. So the hall is not the cause. The hall's final-tail decay at 63 Hz (1.7 s) is the shortest of the octaves 31.5 Hz-2 kHz (1.7-2.8 s, `rtband.py`).

**Loud-third blocks (`loudblocks.py`):** every block above -10 dB holds one of these pitches:
- bar 53.1 (Db2/C2): -4.4
- bar 54.6 (Eb2 after F#1): -4.9
- bar 57.1 (F2/Gb2): -5.6
- bar 23.8 (F2): -5.7
- bar 28.4 (Db2): -10.0
- bar 59.2 (Gb2/G2): -9.1

Blocks with only Ab1/A1/Bb1/E1 read -19 to -29. Effect (inferred): the bass line swells and thins as it moves by step. A muted p section in bars 24-29 is the heaviest low end in the first half.

**Against the reference (`lowdist.py`, `lowpow.py`, 2 s blocks, 30-100 Hz re 250 Hz-2 kHz):**

| | soft median | mid median | loud median | loud p90 | loud 60-100 (energy) | top 10% 60-100 | loud 100-250 |
|---|---|---|---|---|---|---|---|
| Dvorak 9/i | -17.8 | -20.0 | -22.6 | -16.6 | -21.0 | -23.2 | -4.5 |
| c24 | -22.9 | -19.4 | -17.0 | -9.0 | -15.4 | -15.8 | -6.3 |

In the real orchestra the low end falls relative to the mids as the music gets louder; in the render it rises. The long-term 63 Hz octave is +6.3 dB over Dvorak (measure.py LTAS: +0.3 vs -6.0). A level-following EQ does not help: a `loud_eq` whose wet follows the Cb's CC11 (50-80) moves the loud median by 0.1 dB (`cbsim3.py`), because the boomy blocks sit at CC 46-72.

**Simulation (`cbsim2/5/6.py`, `barcmp.py`):** master 60-100 Hz re 250 Hz-2 kHz per passage:

| | 23-29 | 37-44 pizz | 53-59 | 60-62 | 65-66 | 75-81 | 84-92 |
|---|---|---|---|---|---|---|---|
| c24 | -11.9 | -14.0 | -10.9 | -17.1 | -9.7 | -15.8 | -17.1 |
| bell 80 Hz -6 only | -17.3 | -18.0 | -15.1 | -21.3 | -15.5 | -20.5 | -21.7 |
| proposed (below) | -16.9 | -15.5 | -13.8 | -19.2 | -15.1 | -18.1 | -21.4 |

The bell alone stacks on the existing pizz and climax shelves (bars 37-44 to -18, which is past c21's -11 to -13 target), and it takes another 0.5 dB off 100-250 Hz. The proposed set compensates both. Whole-movement results for the proposed set:
- loud median -17.0 -> -20.0; loud p90 -9.0 -> -12.6
- loud 60-100 energy -15.4 -> -17.8; top 10% -15.8 -> -17.9
- loud 100-250 -6.3 -> -6.4
- soft median -22.9 -> -25.2
- LTAS 63 Hz +0.3 -> -2.3 (Dvorak -6.0)
- master corr 60-120 0.76 -> 0.76

Per pitch after the fix: Db2 -0.1 -> -5.1, Eb2 -5.1 -> -11.0, B1 +3.9 -> +0.8, F2 +9.5 -> +4.0. E1-Bb1 move by at most 1.5 dB.

Cb 120-400 Hz (pitch definition) moves +0.3 to +0.6 dB in every passage (`cbh.py`), so the bass line keeps its definition. Its plain RMS falls 0.1-2.8 dB because RMS is dominated by the fundamental. Check the per-dynamic medians with that in mind.

**Fix:** all in `build/mix.json` "Double basses"; all are ReaEQ changes, so `--mix-only`.
1. Add a static bell at 80 Hz, -6 dB, 1.0 oct.
   - No code change: append a third `loud_eq` spec `{"points": [[-2.9, 1], [310, 1]], "bands": [{"band": "bell", "hz": 80, "db": -6, "bw_oct": 1.0}]}`. This is a wet-automated ReaEQ that ramps to wet 1 inside the silent pre-roll and stays there.
   - Do not add it to the track's static `eq`. `config_eq` maps every non-shelf band to ReaEQ band 1, where the 160 Hz bell already is, so the second bell would overwrite it.
   - A cleaner alternative: in `config_eq` map `"bell2"` to band 2, set `BANDTYPE2` to "8", and put the bell in `eq`.
2. Static `eq` 160 Hz bell: +3 -> +4.5 dB (bw 1.4 unchanged). This restores the 100-250 Hz body the cut removes.
3. Remove the second `loud_eq` spec (bars 37-44 pizz, lowshelf 90 Hz -5). The bell now does that job; with both, the pizz loses 4 dB at 60-100.
4. First `loud_eq` spec (climaxes): lowshelf 100 Hz -6 -> -3. Keep its points and its 150 Hz +4 bell.

**Check (c25 master, the scripts above):**
- `lowdist.py`: loud median -19 to -21, p90 at -12.5 or lower
- `lowpow.py`: loud 100-250 at -6.6 or higher; top 10% 60-100 at -17 to -19.5
- `barcmp.py`: bars 23-29 and 65-66 at -15 to -17.5; bars 37-44 at -14.5 to -16.5; bars 60-62 at -18 to -20.5
- `cbpitch.py`: Db2 and Eb2 within 1.5 dB of the simulated -5.1 and -11.0
- `cbh.py`: Cb 120-400 Hz per passage within ±1 dB of c24
- master LUFS, LRA and mp3 limiter within 0.2 of c24; master corr 25-60/60-120 within 0.03 of c24 (0.72/0.76)

Residual (measured, open): F2 (bars 24, 57, 72; 3 notes) stays +4 dB, and D2/G2 are single notes at +3. If bar 57.1 still reads over -9 after the fix, a Cb `pitch_trims.json` entry for pitch 41 (-2 dB, `_all_arts`) is the next step.

## Measured, no action proposed

- **Very low bass leans right.** Master R-L at 25-60 Hz is +7.4 dB (Dvorak -0.4); 60-120 and 120-250 match the reference (+3.9/+2.6 against +3.5/+3.2).
  - Source: the Cb (+9.1 dB in that band). Its samples are already right-heavy, and Opus pans both of its channels right of centre ([0.22, 0.78]).
  - A side low shelf at 70 Hz -6 on the Cb halves the lean (+3.7), but raises the 25-60 Hz correlation from 0.72 to 0.83, against 0.48 in the reference (`leansim.py`).
  - The band carries the weak fundamentals of E1-Bb1 (12-30 dB under their harmonics), so I expect little audible gain. Leave it.
- **Top octave leans left.** 6-16 kHz R-L is -6.5 dB (Dvorak -2.3). Vln I supplies 72% of the band, and above the hall's 5.5 kHz cut only the dry seat image remains.
  - A side high shelf on Vln I (6 kHz -4/-6) moves the lean only to -5.1/-4.4, while the Vln I correlation there rises 0.47 -> 0.65/0.70 (`hfsim.py`).
  - Raising the hall's high cut would need a full rebuild, and the 5.5 kHz cut is a c21 do-not-touch. Leave it.
- **Close-only divisi tracks.** In bars 37-40, Vln II div is 2.5-3 dB brighter than Vln II at 1.6-4 kHz and 4.5 dB quieter. In bars 23-30, Violas div matches the Violas within 1 dB at 1.6-4 kHz (`divtone.py`). This is small; no action.
- **The Violin I solo** (bars 17-22) is 5-9 dB brighter at 2.5-4 kHz than Vln II. The score marks it "solo, senza sord." against muted sections, so it is meant to stand out.
- **The loud tutti** is 2 dB under the reference at 100-250 Hz (-6.3 vs -4.5; top 10% -6.4 vs -3.9). Vc (40%) and Cb (31%) supply that band; trombones and horns add under 2.5% each (`bodyshare.py`). Fix 1 step 2 keeps it from getting worse. The reference is in another key, so I do not propose more.

## Do not touch

- The hall: the true-stereo IR, `fx_volume` 0.19, pre-delay 0.0303, low cut 30 Hz, high cut 5.5 kHz.
- The Close/Main columns and sends of every group; Surround and Mid stay unloaded (memory is at 44 GB of the 45 GB ceiling).
- Every seat and width.
- The c21 side shelves:
  - bass tracks -2 at 200 Hz
  - winds/brass +1.5 at 250 Hz
  - divisi +3
  - harp -8 at 300 Hz
  They now give master correlations within 0.05 of the references at 120 Hz-6 kHz.
- The Vc `loud_eq`, the Vln II `loud_eq`, and `METRIC_DB`.
- The Cb pizz. role and the climax `loud_eq` points. Only the band values change in fix 1.
