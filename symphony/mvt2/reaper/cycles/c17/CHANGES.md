# Cycle 17 changes (actor)

Snapshot of the c16 tools and build/*.json: `before/` (its `parts.json` is the data of the c16 render). Scratch and analysis: `/private/tmp/claude-501/mockup-loop/c17-actor/`:
- `sim.py`: the level simulation on the c16 stems (volume envelopes, tail hold, Vln II shelf).
- `checks.py CYC`: stereo correlation, pan histogram, tail pan, the flute's presence-band modulation, climax and coda levels, final release. Run on c16 and c17 (`checks_c16.txt`, `checks_c17.txt`).
- `vcchk.py`: envelope around single joins.

## Process

1. Edited `tools/score_to_parts.py`, `tools/build_reaper.py`, `tools/auto_fills.py` and `build/{roles,pitch_trims,early_fills,loop_fills,mix}.json`; added `build/loop_profiles.json`. Regenerated parts.json (tempo map unchanged).
2. Simulated the level changes on the c16 stems: mp3 LRA 16.2 LU, limiter 3.0 dB, span 18.9 dB.
3. `build_reaper.py build/parts.json jobs --midi-only`: every Opus state changed (new hall IR), so all 29 tracks were fully rebuilt. REAPER went from 57 GB (35 GB compressed) to 46 GB (25 GB) during the rebuild.
4. Saved and quit. The first `-new` start deadlocked inside Opus `VST3_LoadState` while opening the project (412 MB, 0% CPU; `sample` showed `Main_openProject -> FxDsp::LoadState -> VST3_LoadState -> Opus`). Killed it, started `-new` again and opened the project with a bridge job.
5. One render (`render_cycle.py 17`). It started at 37 GB with 0 GB compressed; while the samples streamed in, macOS compressed REAPER to 57 GB with 40-41 GB compressed (REAPER itself held about 20 GB resident; most of the rest was file cache from the sample drive). Attack gate 18 of 19: Violins I qn 171 "start +0.34 s" (limit 0.15). The Vln I stem around qn 171 matches c16 within 1-2 dB per 50 ms frame from the first sound, so this is the probe's peak-20 dB threshold on a soft entry, not a late note. No second render.

## Accepted

- **Reverts (c16 plan).** `STACLEG_SPANS = {}` (Violas no longer load the Stac Leg row) and `METRIC_VEL = {}`.
- **A #1, loop profiles.** New `build/loop_profiles.json` (critic A's folded inverse profiles from the c16 stems). `score_to_parts.py` `LOOP_PROFILES`: from the note's moved start + 0.8 s to its end - 0.3 s, every 0.04 s, it adds `corr_db` at phase (t - t0) mod `period_s`, faded in and out over 0.3 s, as exact `vol_bp` points. Applied to Vln I 0/292, Vln II 286, Vla 292, Vc 164/274/292, Cb 220/271/292. Their entries were removed from `loop_fills.json` (now empty). The loop-fill dedupe bug (each point compared with the previous point instead of the last kept one) is fixed.
- **A #2, fill overshoot.** `tools/auto_fills.py`:
  - (a) Flute 1, Oboe 1 and Cor anglais are measured on a 200 ms window (`WIN_TRACK`) with a 4 dB threshold.
  - (b) An overshoot rule for every track: the 200 ms peak from max(moved onset - 0.1 s, the fill's own start) to score onset + 0.4 s, minus the louder body; over 2 dB lowers the entry by (over - 1) dB or deletes it, and such an entry is never raised in the same pass. I added the "fill's own start" limit after Vc 140, where a transition peak before the fill would have deleted a fill that the hole after it needs.
  - (c) `_auto` lists "lowered"/"removed".
  - All windows are now centred.
  - Run on c16 with `--exclude` Ob1 140/189 (critic A: hole and peak) and Ob1 271 (c16 B #1 do-not-touch): 33 entries; 26 lowered (e.g. Fl1 190 8 -> 3.6, Fl1 256 8 -> 4.0, Cl1 266 8 -> 1.7, CA 152 6 -> 1.7, Ob1 143 8 -> 5.3), 3 removed (Fl1 200/255/266, Vc 210), 4 new (Cl1 256/258.5, Vc 60/271), 2 raised (Ob1 145, Cl1 269.5). These match critic A's hand values within about 1 dB except Fl1 252 (6.0 against 2.9) and CA 152 (1.7 against removal).
- **A #3, test (failed, see below).** `WIND_VIB_CAP`: woodwind Sus notes of 3 s or more at CC11 100+ get CC1 capped. I checked the patch files first: in the FL/OB/EH/BS/CB KS Masters CC1 is not a depth control but a crossfade between a "Sus Non Vib" and a "Sus Vib" layer (Vib fades in over CC1 55-64, Non Vib fades out over 64-76; from 77 up only Vib sounds). The proposed cap of 80 would have changed nothing, so the cap is 67 (Vib full, Non Vib about 0.8). Not applied to the clarinets (their KS Masters have no Vib layer).
- **B #1, horns at the climaxes.** roles: Hn2/Hn3/Hn4 [204,212] 2 -> 5; Hn3 [261.5,268,2,0.5] + [268,271,-1]; Hn4 [262,268,5,0.5]; Hn1 [262,268,4,0.5]; `_all` [204,212] -1 -> -1.4.
- **B #2.** pitch_trims Bassoon 2 `_skip_onsets` [256, 261, 268].
- **B #3.** roles Flute 1 [262.6,263.5,3], [263.5,265.9,7].
- **B #4.** roles Clarinet 1 [286,292,2.5], Violins II [286,292,-2], Violas [286,292,-1].
- **B #5.** roles Oboe 1 [55.5,58.5,-3].
- **B #6.**
  - `find_unisons`: a same-patch copy that outlasts the kept note by more than `UNI_OUTLAST_QN` (0.25) is no longer dropped. It starts where the kept note ends, minus `UNI_DELAY_OVERLAP_QN` (0.1), via `UNI_DELAY`. Letting it play from the start (B's literal fix) would have put Horns 1, 2 and 4 on the identical Ab3 sample at qn 265. Only that pair changed: Horn 4 now plays Ab3 from qn 266.9.
  - roles Horn 4 [86,90,-3].
- **C #1, true-stereo hall.** mix.json `reverb.impulse` = `//ir/HOP True Stereo/S. Cal Hall Perc TS FR 3.3s`, `true_stereo` true. `apply_mix` sets them on the shared hall insert. Verified in the patch files: the Timpani Flt KS hall differs from the 3BS one only in `impulseA`, `trueStereo`, `delay` (0 vs 0.0303) and `wet`; the delay, wet, 5.5 kHz high cut and fx volume 0.19 were kept. Full rebuild of all 29 tracks.
- **C #2, tail hold.** `build_reaper.py vol_points`: in every rest of 0.5 s or more (the end of the sounding notes to the next moved onset), the envelope holds the value it had just before the last note ended, until 0.35 s before the next onset; not after qn 303.5. Note bodies are unchanged. mix.json `tail_hold` (global or per track, default true) can switch it off.
- **C #3.** mix.json Harp and Harp harmonics seat -0.72, width 0.12.
- **C #5.** mix.json Violins II `loud_eq` {points [[139,0],[140,1],[168,1],[170,0]], 3 kHz high shelf -5 dB}.

## Rejected or deferred

- **A #4 (Violas div track): deferred.** It adds a patch and a track, and this cycle already changed every track's hall. Doing both at once would confound the measurements and add memory to a full rebuild. Next cycle, if memory allows.
- **C #4 (bass width, Cb low shelf): deferred by its own rule** (decide after C #1's render). Its condition now holds: master corr below 250 Hz fell to 0.37 (below), so narrowing Vc/Cb 0.35 -> 0.28 is due next cycle.
- **A #3 failed.** The flute's 1.5-4 kHz modulation at qn 204.5-211.5 rose from 10.5 to 16.9 dB p95-p5, and the stem from -31.7 to -29.5 dB RMS. The master's rose from 5.7 to 6.5 dB. Inferred cause: the Non Vib and Vib layers, summed, beat against each other. The cap is still on in this render and in the tools. Next cycle, set `WIND_VIB_CAP = None` (remove the cap; `--midi-only` is enough). If the vibrato is still to be reduced, test CC1 54 or lower (Non Vib layer only) on one note.

## Measured, c16 -> c17

**Delivery**

| | c16 | c17 |
|---|---|---|
| Master integrated | -23.0 LUFS | -22.5 LUFS |
| Master LRA | 23.6 LU | 24.3 LU |
| Master true peak | -2.9 dBFS | -2.3 dBFS |
| mp3 integrated | -19.8 LUFS | -19.9 LUFS |
| mp3 LRA | 16.1 LU | 16.3 LU (target 14-16) |
| mp3 true peak | -1.6 dBTP | -1.6 dBTP |
| mp3 span | 18.9 dB | 18.9 dB |
| Limiter | 3.2 dB | 3.4 dB |

No clipping, and all 29 stems are present. Bar levels match c16 within ±1 dB except:
- bars 19-20: -1.8/-2.0 (B #5);
- bars 38/40: -1.8/-1.9;
- bar 79: +1.3 (B #1/B #3);
- bars 90-92: -1.1..-1.3 (the profiles' fade-out and their mean offset).

The simulation predicted LRA 16.2 and a 3.0 dB limiter; the flute's CC1 layer (+2.2 dB at the climax) is not in it.

**Findings** (`checks.py`, critic A's `loops.py` and `fljoin.py`, run on both renders)

- **C #1, hall.** The tails moved toward the centre:

  | Stem | Tail R-L, c16 | Tail R-L, c17 |
  |---|---|---|
  | Vln I | -3.9 | +0.3 |
  | Vln II | -3.6 | +0.2 |
  | Oboe 1 | -2.0 | +0.3 |
  | Bassoon 2 | +4.8 | -0.6 |
  | Tuba | +2.7 | -0.8 |
  | Horn 1 | +0.4 | +1.9 |

  - The sustain pans are within 1 dB of c16, apart from Cb (+3.4 -> +1.8).
  - The pan-energy share in the centre two bins rose from 68% to 76% (my 50 ms method).
  - Master corr 250 Hz-4 kHz 0.615 -> 0.606 (target 0.55 not met). Corr below 250 Hz fell from 0.504 to 0.372, a wider and more diffuse bass image, which triggers C #4.
  - Tail-to-sustain levels are within 1.5 dB, except Cb (-13.9 -> -17.6).
  - Final release: -9.2 / -15.2 / -28.7 dB at 0.3/0.6/1.0 s re the last 0.3 s (c16 -9.5 / -16.9 / -26.3).
- **A #1, loop pulse** (resid p95-p5 dB / autocorrelation, c16 -> c17):

  | Note | c16 | c17 |
  |---|---|---|
  | Vln I 0 | 11.6 / 0.43 | 8.6 / 0.35 |
  | Vln I 292 | 10.2 / 0.62 | 7.5 / 0.59 |
  | Vln II 286 | 8.1 / 0.48 | 5.9 / 0.32 |
  | Vla 292 | 8.5 / 0.40 | 6.5 / 0.33 |
  | Vc 164 | 10.2 | 9.0 |
  | Vc 274 | 7.3 / 0.55 | 4.5 / 0.26 |
  | Vc 292 | 7.7 / 0.60 | 5.1 / 0.40 |
  | Cb 220 | 5.8 / 0.74 | 3.7 / 0.62 |
  | Cb 271 | 11.7 / 0.64 | 5.3 / 0.46 |
  | Cb 292 | 9.7 / 0.59 | 6.6 / 0.41 |

  Every note is better by 1-6 dB, but only five reach the 6 dB target. The profiles were fitted on the old hall. Refit them on the c17 stems.
- **A #2, wind joins** over +2.5 dB at 200 ms (fljoin): 13 -> 8.
  - Fl1 190 +5.4 -> +1.2, Fl1 256 +3.8 -> -1.5, CA 152 +6.7 -> under 2.5, Cl1 266 +7.1 -> under 2.5.
  - Left: Fl1 252 +4.9; CA 132/134 +3.1/+3.3; Ob1 143 +3.1; Cl1 256 +4.9 (a new auto fill); Cl1 258.5 +2.9; Cl1 178 +2.8.
- **B #1, horns** (dB RMS, c16 -> c17):

  | Span | Horn 2 | Horn 3 | Horn 4 | Horn 1 |
  |---|---|---|---|---|
  | 204-208 | -32.2 -> -32.6 | -32.7 -> -32.7 | -34.2 -> -31.5 | |
  | 208-212 | -32.2 -> -30.9 | -31.5 -> -30.0 | -34.4 -> -31.3 | |
  | 262-265 | | | -35.1 -> -32.0 | -32.0 -> -29.2 |

  The master at 204-212 is +0.2 dB. Horns 2 and 3 at 204-208 did not rise (inferred: their onset samples or a hairpin dominate that span; open).
- **B #2.** Bn2 at 256-262 went from -31.8 to -35.0, now 2.2 dB under Vln I (was 1.1 over).
- **B #3.** Fl1 at 262-266 per qn: -30.5/-35.1/-37.6/-38.6 -> -28.5/-29.8/-29.9/-31.2. The step into 266 went from 8.5 to 3.0 dB.
- **B #4.** Coda Cl1 -49.9 -> -46.9 against Vln II -52.5 and Vla -51.3 (was level with them).
- **B #5.** Ob1 swell peak -35.3 -> -38.4 (qn 56).
- **B #6.**
  - Hn4 at 265-268: -52.7 -> -38.5 (the Ab3 is back).
  - Hn4 at bar 30: -47.6 -> -50.1, now under Vln I (-49.6).
- **C #5.** Vln II 2-6 kHz at 144-168: -55.9 -> -57.6, still 4.6 dB over the cor anglais (was 6.4). Broadband -0.5 dB. The 3 kHz shelf leaves 2-3 kHz untouched; next, try a 2 kHz shelf.
