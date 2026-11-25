# Cycle 49 (series 2): changes

## For Dan: what to listen for in c49

This cycle is mostly small balance fixes. Three larger tests did not work and were left out.

- **Bar 40.** The cello note under the violins' run starts on the beat again. In c48 it came about 45 ms late.
- **Fugato (bars 85-96).**
  - The violas' quarter-note staccato in bar 90 is now 2 dB under the accented note that starts their entry. Before, the two were equally loud.
  - In bars 94 and 96 the second violins drop 3 dB under the start of the last subject entry (first violins and flute). The entry is now 1-3 dB over them; before, it was level with them or under.
- **Bar 81.** The double basses, violas and the timpani roll are 2-3 dB lower while the first violins and flute enter. The roll still builds into bar 82.
- **Bar 147.** The cor anglais's first soft answer now starts on its first note, which is 3 dB louder.
- **Coda, bar 176.** The clarinet's long C no longer swells twice in its first beat.
- **Coda, bars 167-170.** The doubled trumpets are less bright in their unison tune. They are lifted 1.5 dB on the last held note, so the tune stays over the violins.

Things that are the same as c48:

- The double basses' repeated Cs in bars 167-169 still put a little more weight on the off-beats. A fix through a second instrument instance was tested and did not change it.
- The hall, the stereo width and the violas' send are unchanged. All three were tested and none met its targets.

## Values for the other movements (Movement II, scherzo, finale)

1. **Do not widen the shared hall (Opus reverb Width, manual p.220).**
   - Test setup: second violins' staccato chords sent only to the hall (send 1.0); tail measured 0.3-1.0 s after each chord stops.
   - At Width 1.0 (factory) the tail's L/R correlation in 250 Hz-5 kHz is already 0.03, so the hall is not what makes the image narrow.
   - Width 1.5 makes the tail anti-phase (-0.37) and 1.9 dB louder. Width 2.0 gives -0.59 and 3.7 dB louder.
   - The narrow image comes from the dry mic pairs. Widen there, not in the hall.
2. **EastWest's template mic setup (Main at full width, Close 6 dB under Main at the seat) goes too far if copied exactly.**
   - Tested on eight stems: Violins I, Violins II, violas, celli, Trombone 1, Horns a2, Trumpet 1, Horn 3.
   - Each stem's 250 Hz-5 kHz correlation fell from 0.45-0.82 to 0.06-0.40. Below 250 Hz three stems went negative: Violins II -0.04, celli -0.13, Trumpet 1 -0.21.
   - With only these eight stems changed, the master is already past the references on every measure:

     | Master measure | c49 | With the eight stems | References (Brahms, Dvořák) |
     |---|---|---|---|
     | Correlation, 250 Hz-5 kHz | 0.638 | 0.457 | 0.47-0.56 |
     | Correlation, below 250 Hz | 0.572 | 0.332 | 0.54-0.62 |
     | Side/mid | -6.3 dB | -4.0 dB | -4.7 to -5.4 dB |

   - Seats moved 1.4-3.4 dB toward the centre (Violins I -8.1 → -4.7 dB R-L, celli +5.8 → +3.4).
   - Use something in between: Main pan about seat ±0.7, and keep the low end correlated with a side-only low cut.
3. **Basses' pp release cap: 600 ms throughout.** On the twelve pp chord changes in bars 1-174, the old pitch at +0.35 s sits a median 23.9 dB under the master in its own band at 600 ms (27.1 dB at 450 ms). The 600 ms cap is needed for the final release (basses reach -20 dB at 0.35 s, the master at 0.53 s).
4. **A fresh instance does not reset Hollywood Strings Sus MAX's bow-direction alternation.**
   - Three windowed copies of the double basses had 61, 1 and 0 earlier C2s on the same row before the passage.
   - All three put the strong stroke on the same eighths as the main track, sample for sample in level and timing.
   - So a windowed alias cannot move which beat gets the strong bow.
5. **Place alias windows from rest to rest.** When the main track rested right after a note, that note's treatment changed: velocity 105 → 53, a longer lead, a cut-off, and the next note's re-tongue lead changed.
6. **Render gates.**
   - After start + open + build + restart, REAPER settled at 44 GB with 37 GB compressed, and render_cycle refused. A second restart came up clean (0 compressed).
   - After that restart REAPER's audio engine was stopped (AirPods are the system default). `reaper.Audio_Init()` through the bridge reopened Mac Studio Speakers at 48000 / 512 with no input.
   - Main pass memory takes about 10 minutes to settle at 44 GB. Pass 2 with 19 instances settled at 41 GB.

## Run

- **Disk.**
  - 12:06: 27 GB free, so I wrote WAITING_FOR_DISK.md and released the lock without starting REAPER.
  - Dan then freed space: 85 GB free at the second lock, 83 GB at the end. This folder holds 5.7 GB.
- **Tools freeze.** Another agent was writing c50 template-mix tools in tools/. I waited for `tools/TOOLS_FROZEN_FOR_C49` (PASS, 12:51) and then checked:
  - Regenerated parts.json is byte-identical to the one I prepared.
  - `tools/build_identity_check.py` against my c49 build_reaper (the c49 snapshot plus the reverb-width edit): 8 modes, 190 Lua / .b64 files plus stdout / stderr, all IDENTICAL.
  - No file in tools/ or build/ changed after the freeze marker.
- **Lock.**
  - First hold 12:06-12:08 (disk).
  - Second hold 13:47-15:12, after the finale's c06 and Movement II's c43; Movement II's waiter was older than mine, so it went first.
  - I waited with a wrapper that defers to any older waiter. It ran `reaper_ctl.py lock` only once the lock was free and no other thread's waiter had waited longer (a scratch script, deleted with the scratch).
- **Main pass.**
  - `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only`. No Opus state changed, so there were no full rebuilds.
  - `restart`, then render_cycle refused (37 GB compressed). `restart` again; memory settled at 44 GB, 0 compressed, after 10 min.
  - Audio engine stopped: `cycles/c49/audio_init.lua` (`Audio_Init`) brought it back.
  - `render_cycle.py 49`: probe 0 late or holes. State check: three Horn 1 runs (see Accepted).
  - Full rebuild of Horn 1 (state flip), then `quit`.
- **Pass 2.**
  - `start`, `--pass2 open`.
  - Hall test: 3 tracks, `cycles/c49/halltest/`; results in `width_results.txt`. Tracks then deleted.
  - `--pass2 --midi-only`: 19 tracks, 12 of them tests; the 12 test tracks were fully built. `--pass2 restart`; memory settled at 41 GB.
  - `render_cycle.py 49 --pass2`.
  - A third pedal alias ("Cb pedal C") was built afterwards and rendered alone with "Cb pedal A" over qn 655-681 (`pedalc_render.lua`).
  - Test tracks deleted (`del_tracks.lua`); saved with 7 tracks; `--pass2 quit`; `unlock`.
- **Stem work (after the lock was released).**
  - `horn1_49.py`: the whole c48 Horn 1 stem (identical data).
  - `stem_fix.py 49 cycles/c49/rendered_build_pass2 build --apply "Trumpets a2"`: the coda lift.
  - `render_cycle.py 49 --measure-only`.
  - Originals are in `render_first/`. Test stems and `render_pass2/` were deleted after measuring (4.4 GB).
- **Records.**
  - Render-time builds: `rendered_build/` (main) and `rendered_build_pass2/` (with the test tracks and their mix entries).
  - What I prepared before the lock: `prepared_build/`.
  - Scripts: `actor_scripts/`.

## Accepted

All json edits are re-applied from `before/` by `actor_scripts/apply49.py`. Everything else is in the score_config c49 block.

- **Coordinator / A #5 / B / C, basses pp cap: 600 ms everywhere** (mix.json as it was; no splice). The decision is by measurement on bars 1-174 (`cbcap49.py`, on the c48 600 ms main stem against the 450 ms test audio):
  - The difference is 0.5-4.5 dB of extra hang on 9 of 12 changes.
  - The old pitch at +0.35 s sits a median 23.9 dB under the master in its own band (27.1 dB at 450).
  - The worst case is 224 → 228 at -10.4 dB (-13.3 at 450).
  - The final release needs 600.
  - B's coda-only alias would add an instance and its own round robins for 2-4 dB on notes 12-19 dB under the celli and violas.
  - On c49: bars 1-174 pp changes failing -12 / -12: 7 (c48's main pass also 7; the -12 check is unreliable at fourths and fifths); coda 0 of 5. Basses' final release -10 / -20 / -30 dB at 0.16 / 0.35 / 0.61 s; master 0.19 / 0.53 / 0.82 s.
  - The delivered audio is now the 600 ms main render throughout, so data and audio agree.
- **A #2, celli 156 back to Sus MAX with retongue lead 0.09:** celli data at qn 148-161 is identical to c47's. pcX +77 → +32 ms (c47 +32). 456 stays on Sus Marc LITE: pcX +19, 30 ms under the body, passes.
- **A #3, violas 358 -2 dB:** applied from the moved onset 357.916 (A's 357.95 would leave the first 16 ms). Head 354 minus the quarter staccatos 357 / 358 / 359: +1.7 / 0.0 / +2.2 → +1.7 / +2.0 / +2.2 dB.
- **B #1, Clarinet 1 C5 at 700:** B's two cuts. On the written envelope (`simenv49.py`) and in the render, the arrival peak over the body goes 5.7 → 2.6 dB, with no new dip (`cl700_49.py`).
- **B #3, Violins II under the last fugato entry:** -3 dB over 372.05-373.6. The second cut ends at 380.62, before the 381 ff note's moved onset (B's 380.95 would have cut that attack by 3 dB). Subject minus Violins II:
  - at 372.5 / 373.0: -2.1 / -1.3 → +0.9 / +1.7 dB;
  - at 380.5-380.62: -2.8 → 0.0 dB.
- **B #4, bar 81:**
  - Basses `[320.75, 324, -2, 0.25]` and the Violas row -1.5 → -3, as B asked.
  - Timpani `[322, 324, -2, 0.25]`, starting at 322 instead of B's 321. Simulated, B's 321 start deepened the roll's dip at 320.5-321.5 into a 3.5 dB fall inside the p<ff. From 322 the dip stays at c48's 0.3 dB, and the bar's growth goes +8.9 → +7.5 dB (the c46 rule needs more than +3; `bar81_49.py`).
  - Motif minus the loudest accompaniment voice (broadband, 1/16-qn peaks) at 322.5 / 323 / 323.5: -0.5 / +0.1 / -4.4 → -0.5 / +2.1 / -3.9 dB. On this broadband measure the basses still lead at 323.5; B's K-weighted measure gave -3.2 → -1.2.
- **B #5, cor anglais 586.5 +3 dB step** from its moved onset 586.396, out by 586.9. Peak minus the loudest tune voice: -13.6 → -10.4 dB; 587.0 unchanged at -8.5.
- **C #3, Trumpets a2 3.2 kHz -4 dB bell also over 664.4-679.7** (mix.json loud_eq, pass 2).

  | Trumpets a2, coda | c48 | c49 |
  |---|---|---|
  | 2-5 kHz re 0.5-2 kHz (median) | -5.6 dB | -7.9 dB (C's Trumpet 3 -9.4: within C's 2.5 dB) |
  | Share of master 2-5 kHz | -4.7 dB | -7.2 dB |
  | Share of master 8-16 kHz | -4.2 dB | -5.3 dB |

  - C's 8-16 kHz target of -7 dB is not met: a 3.2 kHz bell does not reach that band, and the cause is the trumpet group's +2.5 dB 4 kHz shelf (open).
  - B's lens: the trumpet / horn melody minus the violins (K, per beat) went from a median +3.0 to +2.2 dB. The held B4's last beats fell to +0.4 / -0.1 / +0.1 dB.
  - So +1.5 dB on the alias over 676.4-679.2 (LEVEL_SHAPES, applied as a stem fix): +1.0 / +0.8 / +1.1 dB (`tpta2_49.py`).
- **Coordinator, state check:** Horn 1 flipped again on unchanged data.
  - Three runs: qn 189-201, 411.5-420 and 587.5-596; +4.5..+5.3 dB and 26-62 ms early, as in c47.
  - Its parts.json and mix.json are identical to c48's, so the whole c48 Horn 1 stem replaces it. After the swap the state check shows 0 runs on every track.
  - REAPER's Horn 1 was then fully rebuilt; its state is checked again at c50's render.
  - No other track flipped. Data changed on 10 tracks (Cor anglais and its stac alias, Clarinet 1, Timpani, Violins II and its f62 alias, Violas, Violoncellos, Double basses, Trumpets a2); all others matched c48.
- **Tools:**
  - `build_reaper.py` takes `reverb.width` / track `reverb_width` (the ConvolutionReverb's `width`, p.220). Unused in the delivered build.
  - `cycles/c49/halltest/` holds the Width test kit (c44's, with a `width` per variant, plus `measure_width49.py`).

## Rejected or deferred

- **B #2 (celli bar-40 cut -8 → -5 / -3): not made.** B measured it on the Sus Marc LITE body. With A #2's revert to Sus MAX, the c47 render (same data) puts the celli at -0.5 / -1.9 / +3.4 / +3.7 / -4.0 / +3.4 dB K over the loudest other stem per half qn 157-159.5. With +3 dB that becomes up to +6.7, the c47 B #4 fault (`vc156_49.py`).
- **A #1, coda bass pedal aliases: no winner.**
  - A's windows 664 / 662 would have built two identical tracks: no C2 starts at 662 (the 660 C2 runs 659.91-663.97).
  - A window starting at 664 or 660 with the main resting there changed the main's 660 note (velocity 105 → 53, lead, cut-off) and its 676 lead.
  - So the tests were "Cb pedal A" (613.5-680) and "Cb pedal B" (618-680). The c48 shapes were dropped in both.
  - Both rendered identically: off-beats 1.4 dB stronger, downbeat pcX +57 ms, off-beat pcX -30 ms.
  - In both windows the 616 C2 is not on Sus MAX, so 664 was each one's second Sus MAX C2, the same parity as the main's 62nd. "Cb pedal C" (664-676, where 664 is its first) was rendered too and came out identical.
  - So the phase does not follow the earlier note count (`pedal49.py`). The main track keeps the c48 shapes: downbeat pcX +14 ms, off-beat -41.
- **C #1, hall Width 1.5 / 2.0: fails C's test criteria.** The tail correlation falls by 0.39 / 0.62, but to anti-phase (-0.37 / -0.59), and the tail is 1.9 / 3.7 dB louder (C's limit 1 dB). At Width 1.0 the hall's own tail is already uncorrelated (0.03), against C's 0.34-0.59 measured in the master after the stops. Coordinator: no hall change this cycle anyway. The Main-mic fallback (Main 0.7 on Violins II / violas / celli) was not built; it is covered by the template variant below.
- **Coordinator's Main-width variant (EW template): not adopted.** Numbers are in Values 2. It passes C's two thresholds (≤ 0.60, ≥ -5.8 dB) with only 8 of 40 stems changed, but it overshoots every reference and moves seats 1.4-3.4 dB. c50 candidate at an intermediate width.
- **C #2, violas send 0.25 → 0.35: fails** (`vla49.py`):

  | Violas | +0.6 s fall faster than the other strings, bars 14 / 26 / 138 / 170 | Figures' old pitch at +70 ms | Per-bar K re main |
  |---|---|---|---|
  | Main | 9.3 / 9.7 / 10.4 / 6.7 dB | -8.4 dB | — |
  | Send 0.35 | 8.5 / 6.8 / 7.7 / 4.3 dB | -8.3 dB | median +0.01 dB, 5 of 161 bars over 0.5 |
  | Trail gain -3, send 0.30 | 8.2 / 8.0 / 8.6 / 4.5 dB | -7.4 dB (fails ≤ -8) | median +0.03 dB, 5 of 161 bars over 0.5 |

  C's target is within 3 dB. Neither variant gets close, so the fast fall is not mainly the hall share; check the violas' note ends at those stops (open).
- **C #5, Cello solo send:** not requested; not done.

## Open for c50

- **Coda bass pedal:** the strong bow stroke stays on the off-beats. Untested options:
  - Sus Marc LITE stroke rows on the twelve downbeats, as on celli 84 / 448 / 456;
  - a CC16 round-robin reset at 663.9 in a test alias (MANUAL-GAPS #6);
  - a silent extra note before 664 to shift the alternation.
- **Stereo width:** the template variant at an intermediate Main pan (about seat ±0.7), with a side-only low cut so below 250 Hz stays near 0.55. Measure seats, correlation and side/mid together.
- **Violas at tutti stops:** compare their written note ends and cut-offs with the other strings at bars 14 / 26 / 138 / 170 before any further send or trail change.
- **Trumpets a2 8-16 kHz:** the 4 kHz +2.5 dB trumpet-group shelf still applies in the coda span (share -5.3 dB against C's -7).
- **REAPER state:**
  - The main project holds the c49 data, with Horn 1 fully rebuilt after the render.
  - The pass-2 project holds the c49 data except the Trumpets a2 coda lift (a stem fix). c50's `--pass2 --midi-only` writes it.
  - parts.json otherwise matches the rendered data.
- **Master sample peak** 1.347 → 1.469 at qn 636.4 (the fff, from how the stems sum; the component stems are within 0.03 of c48). The delivery limiter goes 0.6 → 1.3 dB, still under the 3 dB limit.
- **Unchanged from c48 Open:** Clarinet 1 706 pcX; C #6 arrivals.

## Measured

- **Master** (float sum of 40 stems): -17.4 LUFS, LRA 23.3 LU, true peak +3.3 dBFS, sample peak 1.469. c48: -17.4 / 23.3 / +2.6 / 1.347.
- **Delivered** `cycles/c49/mvt1-mockup-c49.mp3`: -19.8 LUFS, LRA 14.8 LU, TP -1.8 dBTP, limiter about 1.3 dB, p10-to-max span 19.1 dB. c48: -19.8 / 14.8 / -1.8 / 0.6 / 19.0.
- **Delivered S max:** 160 -11.3 > 122 -12.0 > 167-170 -13.6 > 26 -14.2 dB (c48 -11.4 / -12.1 / -13.5 / -14.3). Climax order unchanged.
- **Stereo** (master, unchanged mix): correlation below 250 Hz 0.572, 250 Hz-5 kHz 0.638, above 5 kHz 0.553; side/mid -6.3 dB.
- **Attack probe:** 0 late or holes. **State check** against c48: 0 runs after the Horn 1 swap.
- **REAPER memory:**
  - Main pass: 44 GB settled (0 compressed); 44 GB with 28 GB compressed after the render.
  - Pass 2 (19 instances): 41 GB settled (0 compressed); 42 GB with 0 compressed after.
