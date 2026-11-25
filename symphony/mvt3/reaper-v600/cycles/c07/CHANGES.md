# Cycle 7 changes (actor, 2026-11-08): drier returns, brightness, performance data, phrase shape, tempo breaths

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c06 render). Snapshot: `before/`. Scripts: `actor_scripts/`
(`apply07_mix.py` writes build/mix.json from before/mix.json; `check07.py` parts.json checks; `decay07.py` cut-offs,
tails, RT60, return/dry energy; `wetsim07.py` return-level simulation on the stems; `bal07.py` balance on dry stems plus
their share of the returns (critic B #5); `dips07.py` repeat dips; `accjump07.py` 2-5 kHz jump at brass accents).
Coordinator additions during the cycle: research batches 6-7 (phrase shape by music type), the "no wetter than c05"
targets, and Movement I c50 critics' checks. All are answered below.

## Tool code
- `tools/fxchunk.py` (new): Movement I's `template_mix.spaces_set` and the chunk helpers, ported. It edits the
  template `<FXCHAIN>` text before the paste.
- `tools/build_reaper.py returns_job`: a mix.json return entry may carry `"set"` (Spaces II processor JSON values, for
  example `irSetup`) and `"hp_hz"` (band 0 of the return's ReaEQ). Both are read back from REAPER after the paste, and
  the build stops on a mismatch. Read back on all four returns: envelopeMode 2, endPos 0.5, decayLength 0.5; R Strings
  band 0 is a high pass at 160 Hz.
- `tools/score_to_parts.py` (every option defaults to off or the old behaviour):
  - `LEG_VEL_STRONG` list form: legato-target velocity read from the dynamic lane.
  - `LEG_VEL_DYN_ADD`: velocity added to length-rule targets at a set level or above.
  - `LEG_OVERLAP_MIN_S`: legato overlap floor in seconds. It is applied after the re-bow splits and the keyswitch
    guard. It is not applied into a same-pitch note, past a keyswitch, or beyond half the target's length.
  - `ROW_VEL_BY_CC`: velocity by printed level on a row, for printed staccatos only. (`ART_SPANS` would have overridden
    the pizz/tremolo rows.)
  - `STAC_LEAD_S`: brass is now allowed.
  - `ROW_LEAD_S` span form `[(from, to, s)]`, capped at `ROW_LEAD_CAP_FRAC` 0.45 of the abutting note.
  - `TREM_ENTRY_LEAD_SPANS`.
  - `STR_REP_NEW_BOW["chord"]`: the same-pitch voice of a div. chord gets the new-bow gap.
  - `PHRASE_SHAPE`: a phrase contour, typed build / drive / lyric. On `CC1_DYN_TRACKS` it goes into CC1 with a
    `cc1_floor`.
  - `HP_CURVE`: hairpin shapes.
  - An "open" phrase arc no longer prints the ramp WARNING. It does not slow, so it cannot make a ramp start faster.
- `tools/deliver_master.py`: mix.json `"deliver": {"ratio"}`.

## Data
1. Reverb (critic C #1, B #1; research batch 5 item 1). Final return levels:
   - Sends:
     - Violins I/II, violas, celli, horns, trumpets and the upper winds: -10 dB.
     - Basses, trombones, bass trombone, tuba, bassoons and contrabassoon: no send.
     - Timpani -6.41, crash and bass drum -6.41, harp -8.77 dB (unchanged).
   - Return faders: R Strings, R Brass and R Winds -1.97 dB; R Perc -2.34 dB (c06 +1.03 / +0.66).
   - IR envelope: envelopeMode 2, endPos 0.5, decayLength 0.5 on all four returns.
   - R Strings high pass: 87 -> 160 Hz.
2. Brightness (B #3):
   - Family shelves halved: strings +2.0, brass +2.0, winds +2.55 dB.
   - master_eq: the 1.18 kHz bell is removed, and a 6 kHz -3.0 dB shelf replaces the 8 kHz +0.8 shelf.
   - Basses (B #4): bell 180 -> 150 Hz, plus 240 Hz -3 dB (1.39 oct) through a track family_eq.
   - Trumpet 1 solo role at qn 200-264: +2.5 -> +3.2 dB (B #5).
3. MIDI (build/score_config.py c07 block):
   - Repeat gaps (A #1):
     - Trumpets, trombones, bass trombone and tuba re-tongue at 0.10 s, frac 0.3, fall 10 CC. A dead "Trombone 1" key
       was removed; "Trombone" had shadowed it since c03.
     - STR_REP_NEW_BOW strokes, tenuto and portato: 0.09 s, frac 0.3.
     - The celli get the basses' detach dip on the f-ff spans, and RETONGUE_LEAD_ART_S Vc Sus MAX +0.07 is removed.
   - Legato velocity by dynamic (A #2, C #6):
     - Strings and brass: (52:100, 65:106, 80:112, 100:118, 127:124). The floor is 100, as the coordinator asked;
       critic C proposed 96.
     - Extra leads: strings 0.027-0.007 s, brass 0.010-0.002 s.
     - Wind targets at ff: +8 (108).
     - Overlap floors: strings 0.045 s, winds and brass 0.035 s (the median overlap was 14 ms; now 45 / 35 ms).
   - String staccatos (A #3): velocity by printed level (58:66, 72:80, 88:100, 114:118, 124:124); the row is -1.5 dB
     (ROW_GAIN_DB). Trumpet staccato lead 0.02 s.
   - Lead residuals (A #4, C #2, C #4):
     - Entry leads: Oboe 2 (0, 0.11, 0); contrabassoon (0.04, 0.04); Horn 2 (0.04, 0.06, 0.03); Trumpet 1
       (0.10, 0.065); Trombones 1-2 (0.06, 0.09, 0.05); Bassoon 2 0.05.
     - Oboe 1 entry extras -0.01 s.
     - Slur heads on Leg Slur MAX: Vc 0.09, Vln I 0.08, Vln II 0.075.
     - Upper strings Sus MAX: 0.07 s on abutting notes in P and T, and 0.11 s on Vln II / Vla in F.
     - Tremolo entries in T: Vln II 0.12, Vln I 0.10.
   - Div. chord repeats (A #5): Vln I/II 970 -> 972 -> 973 now have an 80 ms gap (it was 11 ms). Not changed: 973 -> 976,
     Vln I 884 (Leg Slur MAX) and Vc 828 -> 832 (the rule is restricted to non-legato rows).
4. Phrase and tempo:
   - PHRASE_SHAPE (c06 C #1-2 / A #2, then research batches 6-7 from the coordinator), with three types:
     - "build" (the printed level rises 10+ CC, or a crescendo ends in the last quarter): -12 at entry, +10 at 0.95,
       no taper.
     - "drive" (outside the lyrical spans D-E, L-M, O and Q): +6 at entry, +10 at 0.15, -10 at the end.
     - "lyric": the centred arch (-12, +3/+8 by 0.4/0.8 s, +10 at 45 %, +4 1 s before the end, -12).
     - Scaling by printed level: pp 0.8, p-mf 1.0, f 0.6, ff 0.35, fff 0.2. Brass CC1 cap 108, CC1 floor 36. The shape
       fades 0.25 s around hairpins and fp/sfp.
     - 21-38 phrases per track. Example, the winds: 13-18 drive, 4-14 build, 2-9 lyric.
   - HP_CURVE (batch 5 item 3): a crescendo reaches 70 % of its rise at 40 % of the hairpin; a diminuendo keeps 65 % of
     its level to the last onset.
   - CAESURA at 72, 104, 392, 632, 664, 816 and 1108 (0.05-0.10 s). PHRASE_ARCS on D-E, L-M, O and Q, 20 arcs (C #5).
   - Beats with a tempo change: 47 / 558 (8.4 %) -> 118 / 558 (21.1 %). Total +1.05 s.
   - space_rebows was rerun and written.
5. Delivery: mix.json `deliver.ratio` 3.0 -> 2.0 (below).

parts.json: 0 WARNING. No row set changed, so all 31 tracks were written with `--midi-only --tempo` (no Opus reload).

## Rejected / deferred, with numbers
- Seeded tutti entry spread: dropped (LEARNINGS). The perceived spread is already 142 ms first to last and 85 ms p10-p90
  (C #3), and 80 ms p10-p90 at 83 onsets of 14+ tracks (A #4). The experts' note-on spread is 36-55 ms.
- Fixed per-track early shifts: dropped (LEARNINGS). Our per-note leads (winds 35-55 ms, brass 50-90 ms) put 24 of 28
  tracks within ±25 ms. Polar's shifts on top would put the flutes 75 ms early and the bassoons 40-85 ms early (A #4).
- Duc's -1.6 / -7 dB celli and bass sends: superseded by batch 5 (celli -10, basses none).
- Duc single hall: not needed. The c07 master meets the -20 dB target, so it remains the fallback for c08 only if a
  later change makes the tails longer.
- CC1-only and narrow-brass A/B tests: not run (memory 44-45 GB; they need pass 2). Left for c08.
- Batch 6/7 ostinato and short-note position velocity, and batch 7 spiccato length: c08.
- Movement I c50 B: timpani EQ, harp HPF and winds/crash make-up were already done in c06. Timpani share of 30-150 Hz
  in rolls, dry + returns: 271-279 18.5 % (c06 20.7), 223-226 7.4 %. Per-instrument / per-dynamic brass make-up: c08.
- Brass accent brightness (Movement I c50 C): the master's 2-5 kHz jump at brass accents (first 80 ms minus the 200 ms
  before) is p90 5.2 dB (c06 5.8; target under +2). c08: the 821 Hz family bell -7.8 -> -4, or a 3.2 kHz -3 dB bell. The
  trumpets' 4 kHz shelf was already removed in c06.
- Not measured this cycle: the celli Sus MAX lead removal (A #1.3) on pcX, and the F/P/T upper-string leads.

## Measured (c07 render; c06 numbers from critics or from the same scripts on the c06 master)
- **Decays, master** (decay07.py; critic C's nominal cut-off times):
  - -20 dB median 0.71 -> 0.52 s.
  - With the cut-off times aligned to the steepest fall (wetsim07.py), per cut-off:

    | | c06 | c07 |
    |---|---|---|
    | -20 dB (s) | 0.61 0.52 0.49 0.66 3.76 0.52 (median 0.57) | 0.39 0.36 0.42 0.48 0.43 0.25 (median 0.41) |
    | drop at +0.3 s (dB) | 12.6 12.9 10.5 7.8 10.6 14.5 | 16.0 17.2 18.5 12.2 13.3 22.9 |
  - The 15 dB drop target is missed at qn 373 and 661. Even with the returns off (simulated -60 dB) they reach only
    16.7 / 18.7 dB, so the dry stems set it there. Simulated return levels of -3 / -6 / -10 dB change the -20 dB median
    only from 0.41 to 0.35 s, so the faders were left where they are.
  - RT60 estimate at the final cut-off: 2.3 -> 1.22 s.
  - Late slope (-20 to -60 dB) at the final cut-off: 1.91 -> 0.95 s.
  - The 60-250 Hz share of each tail's first second fell 1.3-2.9 dB at every cut-off (for example the final one -7.0 ->
    -8.3 dB).
  - Return minus dry energy, whole piece: -12.5 dB (c06 -2.9 dB, critic C's reconstruction, the same measure).
- **Soft ends**, string stem + R Strings, -10 dB:

  | qn | Violins I | Violins II | Violas |
  |---|---|---|---|
  | 198.88 | 0.25 (c06 0.43) | 0.31 (0.50) | 0.36 (0.50) |
  | 454.86 | 0.75 (0.83) | 0.26 (0.97) | 0.29 (0.95) |
  | 455.86 | | | 1.01 (dry 0.28) |
  | 477 | 0.22 (0.44) | | |
  | 679.86 | | 0.30 (0.40) | |

  The 454.86 note is 0.54 s even on the dry Vln I stem, so the hall is not what makes it long.
- **Spectrum:**
  - Master 100-250 Hz share -5.5 -> -8.5 dB (references -6.6..-8.8).
  - Delivered 6-20 kHz: -24.8 -> -27.7 dB (target about -28). The master EQ alone, simulated on c06, gave -27.9.
- **Balance**, dry + returns (bal07.py), c06 -> c07:
  - Trumpet 1 solo 51-66: +3.5 -> +3.9.
  - Brass minus strings: 223-234 +5.3 -> +5.3; 255-264 +5.2 -> +5.6.
  - Horns minus heavy brass: -4.3 / -4.6 -> -4.4 / -4.5.
  - Bass theme 4.1 -> 4.1.
  - Muted Tpt1 minus CA -3.2 -> -2.7.
  - Harp minus Vln I +1.7 -> +1.2.
  - Winds minus strings +1.7 -> +2.1.
- **Repeat dips**, dry + return (dips07.py):
  - Bass trombone 7.9 dB and tuba 12.2 dB, with 0 repeats under 3 dB (c06 5.8 / 5.7 with 6 / 5 under 3).
  - Trumpets 4.9-6.1 dB: unchanged. Trumpet 3 still has 12 of 48 under 3 dB, in the Più allegro.
  - Celli 604-658: dry dips 3.8 / 6.4 / 9.5 / 6.9 / 5.3 dB (c06 1.7-3.9). Celli 828: still 1.5 dB.
- **Legato joins (pcx):**
  - Strings: Vln I +15, Vln II +1, Vla -6, Vc +8 ms; robust SD 46-54 ms (c06 Vc +10 / 40 ms).
  - Horn 1 +21 ms, Trumpet 1 +6 ms.
  - With velocity by dynamic plus the extra leads, every string median stays within ±20 ms.
- **Phrase shapes** (stems):
  - Trumpet 1 solo phrases at sq 200 / 216 / 251 now fall 1.1 / 0.5 / -1.8 dB over the last second. c06 rose 0.4 /
    2.6 / 5.8 dB.
  - The rise from 0.15 s to 0.8 s is +6.4..+7.0 dB.
- **Climaxes:** loudest bars 278 (-13.6), 223 (-14.0), 279, 262 / 263. Master -18.9 LUFS, LRA 23.5 LU (c06 20.5), float
  peak 1.121 (the 24-bit file was replaced by the float sum).
- **Delivery:**
  - At the default ride ratio 3.0: LRA 13.5 LU, under the 14-16 target.
  - Refit to ratio 2.0 (delivery only, no REAPER): -19.7 LUFS, LRA 14.6 LU, TP -1.9 dBTP, limiter 0.5 dB,
    p10-to-max span 18.5 dB.
- **Attack probe:** 1 flag, Violoncellos qn 24 at +0.43 s. It is a probe artefact. The stem starts on time: -69 dB at
  the onset, -56 dB by the beat. The phrase is a "build" whose body then rises about 10 dB, which moves the probe's
  body-relative threshold. The same note was flagged in c00-c02.

## REAPER
- Lock 15:44-16:12 (28 min). MIDI and tempo write (no reload), restart, 44 GB reached at 15:57, render 15:58-16:08.
- Memory: 44 GB settled (5.4 GB compressed) before the render; 45 GB after (28 GB compressed).
- REAPER holds build/parts.json and build/mix.json. The `deliver` key affects only deliver_master.
- c06 stem WAVs were deleted (00_Master.wav kept).
