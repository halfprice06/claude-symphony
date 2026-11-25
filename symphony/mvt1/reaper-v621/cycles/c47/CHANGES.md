# Cycle 47 (series 2): changes

## For Dan: what to listen for in c47

In c46 the first trumpet was too loud and came in early on its slurred notes in bars 69-71 (the closing theme), bars 113-114 and bar 161. In bars 69-71 it stood out over the violins' tune. In c47 it sits under the tune again, 4-11 dB below the first violins, as in c45. The movement's last chord now dies away instead of stopping. It takes about twice as long to fade, close to soft endings in real recordings. In bar 145 the first clarinet's held pp note no longer covers the oboe's soft solo. In bars 35-38 the first violins' answer to the bassoon now sits clearly above the held bassoon and the soft clarinet chord. In bar 40 the cellos' held note no longer covers the violins' and woodwinds' run up to bar 41. In the coda cello solo (bars 172 and 174) two notes no longer sag right after the change of pitch, so they no longer sound late. Two accented notes no longer start softer than the note before them: the first violins' D-flat in bar 35 and the clarinet's note in bar 127. The violas' small swell before their note change in bar 20 is gone. The softest passages are 0.5 dB louder in the mp3.

## Values for the other movements (Movement II, scherzo, finale)

1. **c46's Trumpet 1 was too loud in bars 69-71, 113-114 and 161, and c47 fixes it.** It was 4-15 dB louder and 40-65 ms early on its Leg Slur MAX notes, with data identical to c45. A full rebuild of the Opus instance (`build_reaper.py parts.json jobs "Trumpet 1"`) brought c45's state back. Trumpet 1 minus Violins I per quarter at qn 276-283 now equals c45's to 0.1 dB (-4.3..-11.4 dB K). This time Horn 1 flipped (+4.5..+4.9 dB, 32-62 ms early, on three Leg Slur phrases). Horn 1 had a MIDI-only build, and its data and mix were identical to c46. Its c46 stem was used instead.
   - **Rule:** after each render, compare every unchanged note with the previous render. The new generic `tools/state_check.py` does this (README c47 entry), and `render_cycle.py` runs it. Fully rebuild any Solo Horn / Solo Trumpet instance that flips. A MIDI-only build of those KS Masters can render in either state: 4 of the last 6 renders flipped one of them.
2. **Soft string release (C #1).** Removing the release cap on the Sus MAX / Sus Marc LITE pp groups (shipped 931 ms) works. The 350 ms cap stays at p and the 150 ms cap at mf-ff.
   - Pass-2 test of Violins II, Violas, Violoncellos and basses on their own data. The master's final chord fell 10 / 20 dB in 0.12 / 0.33 s before and 0.21 / 0.61 s now. The references are 0.20-0.40 / 0.48-0.79 s.
   - Soft and loud phrase ends otherwise unchanged; no ending fell more than 10 dB in 0.05 s.
   - pp chord changes where the old pitch is still within 10 dB at +0.35 s: Violins II 12 -> 11, Violas 14 -> 15, celli 13 -> 13, basses 1 -> 6. The basses' long pp notes overlap, so check them in Movement II.
   - Movement II measured 600 ms at pp/p; on these numbers 600-931 ms is the useful range.
3. **Stroke rows (A #4, C #3).** On fresh Sus MAX strokes repeating a pitch:
   - "Sus Marc LITE" at velocity 25-45 removed the slow swell on two of six celli strokes (time with the band 6 dB under the body 64 / 124 -> 0 ms) and helped two more. It made one worse.
   - "Stac Leg BC + Slur + Port MAX" at velocity 40-60 swelled in longer on 4 of 6. Not used.
4. **Brass Marc Sus LITE at low velocity (MANUAL-GAPS #1, C #2): fails.**
   - At velocity 45-75 the attack is perceived 100-365 ms late: the sustain layer fades in over 174 ms under a low-pass marcato attack, read from the patch.
   - The 2-5 kHz front is no brighter than the plain sustain (median -15.1 against -13.1 dB), and the step over the note before is smaller.
   - Do not use it on accents at low velocity.
5. **Windowed pass-2 test tracks** need three pipeline guards, now in Movement I's `score_to_parts.py` (README c47):
   - hairpin gains only from hairpins inside the alias's own windows (a coda-only alias had carried +9 dB from the bars 122 / 160 crescendos);
   - no re-bow fill list whose note the alias does not play (+4.1 dB over 26 bars);
   - the CC70 lane starts at the source's value.
   - Even so, the coda-only basses pp700 instance rendered 8-11 dB level steps at four final-chord re-bows that the whole-piece instance did not. Prefer whole-piece test aliases.

## Run

- **Disk.** The first attempt stopped before step 5 (22-25 GB free, `WAITING_FOR_DISK.done.md`). Resumed 2026-11-08 with 41 GB free.
- **Lock.** Free and no waiter at 06:18; held until 07:34. Movement II's waiter had been waiting 76 min when I released it, so I skipped the post-render rebuild in REAPER (see Open).
- **Main pass.** `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only` (the five string tracks were fully rebuilt: Opus state changed), then a full build of "Trumpet 1" and "Horn 3", `restart` (33 tracks, 48000 / 512, no input), `render_cycle.py 47` (probe 0 late or holes). The state check found Trumpet 1 back in c45's state and Horn 1 flipped. `actor_scripts/horn1swap47.txt` records the Horn 1 stem swap. `quit`.
- **Pass 2.** `start`, `--pass2 open`, `--pass2 --midi-only` (f62 aliases fully rebuilt, 13 test tracks built), `--pass2 restart`, `render_cycle.py 47 --pass2`. 20 instances: 22 GB at start, 39 GB settled, 41 GB after. Every stem was full length.
- **Decisions and splices.** `actor_scripts/softcap47.py`, `strokes47.py`, `marc47.py`, then `swap47.py`:
  - Violins II, Violas, celli and basses from their no-cap test stems from qn 695.8 to the end. Before the coda, the test and main stems differed by 1-6 dB in 4-8 bars (round robins, and the variant-A strokes on the celli / violas tests).
  - Celli 84 and 448 from "Vc stroke B".
  - Originals of the replaced stems in `render_first/`.
  - Then `render_cycle.py 47 --measure-only`.
- **Clean-up.** Test tracks deleted from the pass-2 project (`del_tracks.lua`), saved with 7 tracks, `--pass2 quit`, `unlock`. Test stems and `render_pass2/` deleted after measuring (4.7 GB). The cycle folder holds 6.1 GB.

## Accepted

- **Coordinator (a), Trumpet 1 / Horn 3:**
  - Full rebuilds. Trumpet 1's two runs moved by -6.6 / -5.6 dB and +41 / +46 ms against c46, which is c45's state. Horn 3 164 moved -5.5 dB / +95 ms, also back to c45.
  - The splice script `actor_scripts/splice47.py` was not needed.
  - New generic `tools/state_check.py`, run by `render_cycle.py`. Tested on c45 -> c46: it lists exactly the critics' notes.
- **C #1 / A #5, soft cap:** no pp cap on Violins II, Violas, Violoncellos and Double basses (mix.json; Values 2).
  - Re-bow dips (rebows44.py), c46 -> c47: automatic medians 2.8 / 1.6 / 2.1 / 2.2 / 2.4 -> 2.8 / 1.7 / 2.1 / 1.3 / 1.8 dB (Violins I / II, violas, celli, basses). Steps of 3 dB or more 1 / 1 / 1 / 2 / 6 -> 1 / 2 / 1 / 2 / 6. The basses' median |step| went 1.0 -> 1.5 dB. The final-chord fills were not refit: the longer releases fill the dips, and a refit would only cut.
  - Violins I keeps 350 ms. It was left out of the test for pass-2 memory, and it carries 4% of the final chord.
- **A #4 / C #3, strokes:**
  - Tools: ART_SPANS `"stroke_row"`; strokes keep a stroke-row span, are never merged, and keep the stroke lead.
  - Celli 84 and 448 now play "Sus Marc LITE" (`ART_SPANS` in score_config.py). Time with the band 6 dB under the body went 64 / 124 -> 0 ms, and pcX -8 / +52 -> -32 / -4 ms.
  - The c46 front and dip criteria fail on the main strokes too, and these two are no worse there.
  - The 84 span plays 2.2 dB louder than before (an inner voice at rel about -10 dB).
- **B #2:** Clarinet 1 [575.75, 582, -5]. Clarinet 1 under the master at 576-578 went -3.8 -> -7.4 dB K. The oboe minus the loudest other stem at 578.0 went -3.3 -> +0.9 dB, then +3.1..+11.8.
- **B #3:** bars 35-38 roles. Violins I minus the loudest other stem: median +1.2 -> +3.4 dB, beats under 0 3 -> 1, beats under +3 15 -> 8. Bassoon 1 under the master -9.1..-11.0 dB (still heard).
- **B #4:** celli -8 dB at 157.5-159.6. Celli minus the loudest other stem (K) +1.7 / +5.6 / +6.4 / +2.4 -> -1.3 / +2.6 / +3.4 / -0.6. The step into bar 41 went +5.4 -> +5.6 dB.
- **B #5:** RIDE_TRIMS +0.5 dB on nine soft spans. Delivered span 19.3 -> 18.9 dB.
- **A #2:** Cello solo fills. The 687 / 694 dips went 8.6 / 6.2 -> 2.6 / 1.2 dB, with peaks +1.4 / +1.3 dB. A's optional Bassoon 1 135 and Clarinet 1 700 fills were added as simulated by A.
- **A #3:** pickup lifts Violins I 136.5 12 -> 6 dB and Clarinet 1 504.5 9.5 -> 6.5 dB. Each accent's first 0.3 qn is now 3.4 / 2.1 dB over its pickup (before -0.2 / -0.5).
- **A #6:**
  - (a) Violas 78: an exact LEVEL_SHAPES row from the A-flat4's moved onset. A roles row's start ramp is always 0.5 qn (its 4th value is only the end ramp), so A's proposed row would still have ramped from 77.25. The peak before the join over the A-flat4's body went +8.1 -> +2.4 dB.
  - (b) Violins I 472.5 / 474.5 entry leads 0.05 / 0.04.
  - (d) leg_leads 232.0: Violins I +0.04, Violins II +0.02, with a listed cap of 0.82 so it takes effect. Realised: 231.698 -> 231.628, 231.625 -> 231.59.

## Rejected or deferred

- **C #2 Marc Sus LITE brass:** fails (Values 4). MANUAL-GAPS #1 records the result.
- **Variant A stroke row:** not kept. Violas 372 lost its swell (230 -> 10 ms under) but was perceived 195 ms early with the Sus MAX stroke's lead; worth a retest with less lead.
- **Variant B on celli 152, 156, 456:** not kept. 152 got worse (0 -> 94 ms under). 456 was 73 ms early: the row needs less lead.
- **Celli 47:** not tested. Its stroke holds a later re-bow point, which the pipeline supports only on Sus MAX.
- **Violins I soft cap:** not tested (memory).
- **The coda pp700 tests:** not used.

## Open for c48

- **REAPER was not rebuilt with the post-render data** (a thread was waiting). c48's `--midi-only` fully rebuilds Violins II, Violas, Violoncellos and Double basses itself (Opus state changed). **Fully rebuild Horn 1 as well** (`build_reaper.py build/parts.json jobs "Horn 1"`): its instance is in the flipped state. Celli 84 / 448 get their new row from the MIDI.
- The c47 audio has the no-pp-cap releases only from qn 695.8. Bars 1-174 get them in the c48 render, and the critics should check the pp chord changes there, the basses' above all (6 changes over -10 dB at +0.35 s).
- Variant B's lead on 456; Violas 372 on variant A with less lead.

## Measured

- **Master** (float sum of 40 stems): -17.3 LUFS, LRA 23.4 LU, true peak +2.5 dBFS, sample peak 1.339. c46: -17.3 / 23.3 / +3.1 / 1.423.
- **Delivered** `cycles/c47/mvt1-mockup-c47.mp3`: -19.8 LUFS, LRA 14.7 LU, TP -1.7 dBTP, p10-to-max span 18.9 dB, limiter about 0.5 dB. c46: -19.7 / 14.9 / -1.8 / 19.3 / 1.0.
- **Delivered S max:** 160 -11.3 > 122 -12.0 > 167-170 -13.5 > 26 -14.2.
- **Attack probe:** 0 late or holes.
- **State check** (final): only Trumpet 1's return to the c45 state.
- **Master final chord:** -10 / -20 dB at 0.21 / 0.61 s (c46 0.12 / 0.33).
- **REAPER memory:** main project 18 GB at start, 44 GB settled, 44 GB (24 GB compressed) after the render. Pass 2 (20 instances): 22 / 39 / 41 GB.
