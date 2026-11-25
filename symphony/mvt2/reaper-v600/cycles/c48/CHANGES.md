# Cycle 48 (actor): the finale's shared techniques, the bar 47 fp, final-chord fade, mix EQ and horn width

Rendered 2026-11-09 13:41 (`cycles/c48/mvt2-mockup-c48.mp3`), one render; Trombone 1's stem spliced from c47 afterwards
(below). Snapshot before the changes: `before/`. Data the render was made from: `rendered_build/` (parts.json, mix.json,
score_config.py, the per-note tables, build_reaper.py, score_to_parts.py); `build/` is the same. Scripts:
`actor_scripts/` (`m48.py` checks, `range48.py` range render, `turn_lock.sh`, `_c48_audio_init.lua`; c47 baseline numbers
in `m48_c47.json`, c48 in `m48_c48.json` / `m48_c48_fp_final.json`); `check44.txt` / `check_c48.json`, `s1_c48.txt`,
`pcx_c48.txt`, `state_check.txt`.

## Lock and drive
- Turn rule: no older waiter; waited on the scherzo's c10 render (12:35-13:03). Lock **13:03:17-13:43:37 (40 min)**.
  Disk 49-55 GiB free, `/Volumes/MAC DRIVE` mounted.
- Start + open (36 tracks), settled at 43 GB (28 compressed) in 9 min; `--midi-only` on 9 tracks (Oboe 1, Horn 1, Violins
  I, Violins II, Violas, Violoncellos, Double basses, Violins II div, Violas div; no full rebuild), `--mix-only` on all
  32 (family EQs, horn widths, gains; widths read back: Horns 1-4 and a2 at 0.80); restart, settled at 43 GB / 0
  compressed in 10 min; `_c48_audio_init.lua` (48000 Hz, 512, no input).
- Range render qn 143-153 (17 s of lock; `range48.py fp1`), the fp measured, the item 13 bump simulated on its stems,
  written with `--mix-only` on Violins II / Violas / basses, checked by a second range render (`fp2`), then
  `render_cycle.py 48` (no `--force-memory`, 43 GB / 1.2 GB compressed). **After the render: REAPER 44 GB, 25 GB
  compressed.** Quit, unlock.
- After the unlock: Trombone 1 splice (below) and `render_cycle.py 48 --measure-only` (delivery redone).

## Results (c48 render after the splice; c47 in brackets)
- Master -22.9 LUFS (-22.9), LRA 23.5 (23.4), true peak -3.6 (-3.5), no clipping. Delivered **-19.8 LUFS, LRA 15.3**
  (15.3), TP -1.6, p10-to-max span **18.8** dB (18.8), limiter **2.1** dB (2.0); length 354.70 s. Bars 61 / 62 still the
  loudest. **Attack probe: late or hole 0.**
- **Bar 47 fp** (`m48.py`, 50 ms RMS; peak from the note-on to 148.5, body = mean over 148.6-149.2):

  | part | note-on | peak (time re beat) | own drop | at +0.1 s re peak | p within 3 dB |
  |---|---|---|---|---|---|
  | Violins II | -240 -> -60 ms | -45.8 (+420 ms) -> -39.7 (+115 ms) | 4.2 -> **12.8** | -3.7 -> -0.2 | 455 -> 365 ms |
  | Violas | -225 -> -60 ms | -41.2 (-85 ms, the slur's join) -> -34.3 (+5 ms) | 10.2 -> **14.1** | -6.3 -> -1.2 | 650 -> 400 ms |
  | Double basses | -160 ms | -39.4 (+320 ms) -> -34.1 (+50 ms) | 9.0 -> **13.9** | -4.7 -> -0.6 | 490 -> 440 ms |

  Master at -100 / 0 / +150 / +350 ms: -36.2 / **-39.9** / -37.4 / -34.8 -> -36.1 / **-31.2** / -31.2 / -35.0 dB (the beat
  was the bar's quietest moment; it is now a 5 dB accent from the beat that falls back under Oboe 1). Master tilt jump at
  148 +0.1 -> +3.3 dB (A's ceiling 3.0; the stems' tilt jumps +3.0 / +3.2 / +0.6). Every part's drop is over 10 dB, so
  no p rows. The range render before the bump measured drops 11.2 / 14.3 / 13.2 dB with peaks at +235 / +200 / +225 ms.
- **Final chord** (master, check44): t20 0.404 -> **0.444 s** (A's simulation 0.440; guard 0.45, recordings 0.43-0.55),
  t10 0.249 -> 0.289 s, drop at +0.3 s 14.1 -> 11.1 dB.
- **Oboe 1 142 / 142.5** (stem body, 20-80 % of the note): -49.0 / -49.0 -> -46.4 / -47.8 dB (140 -43.9, 143 -44.8
  unchanged); master +0.6 / +0.4. 142.5 gains less than B's +2.7 because B's shape ends at 142.70, before the note does.
- **Bar 81** (269.0-269.5, RMS): celli -34.2 -> -39.5 against Violins I -40.0 / -40.1 (celli 5.8 -> 0.6 dB over the
  tune); the celli's transition peak -30.8 -> -36.2; violas -39.2 -> -41.9.
- **Horn 1 bar 60** (per beat 201 / 202 / 203): -29.8 / -28.8 / -30.0 -> -28.9 / -27.7 / -28.3 dB (B predicted +1.0 /
  +1.5 at 202 / 203).
- **Mix (C #1-#3)**, master third octaves (shares): 315 Hz hump +3.24 -> **+2.91** dB, bars 23-30 +2.61 -> **+1.44**; 500 Hz
  -10.72 -> -10.35; 49.6 Hz -37.1 -> -35.2, coda pedal -28.3 -> -26.1, bars 45-52 -30.9 -> -28.9. Side/mid bars 7-14
  -5.29 -> **-6.45** dB (C's target -6.0..-6.8), bars 65-70 -4.99 -> -5.75, bars 61-64 -5.34 -> -5.59, whole piece
  -5.45 -> **-5.65** (C's floor -5.7); 250 Hz-5 kHz correlation 0.57 -> 0.68 in bars 7-14. K levels: Horn 1 bars 7-14 /
  65-70 within 0.1 dB of c47; string stems within 0.15 dB in their main passages except Violas div bars 23-30 -0.5 (C
  predicted -0.6) and the basses +0.3 (coda) / +1.5 (bars 45-52, the 35 Hz high-pass and the fp). Band shares: 100-250
  Hz -7.39 -> -7.51, 2-6 kHz -10.01 -> -10.20, 6-20 kHz -29.48 -> -29.63; correlation under 250 Hz 0.63 (unchanged).
- Solo margins (check44): unchanged within 0.3 dB except Oboe 1 bars 45-47 5.8 -> 4.9 (the fp accent now sits under its
  148 entry), Violins I over the celli bars 89-91 5.3 -> 6.3, horns minus strings bars 79-81 -3.8 -> -3.4.
- Wetness (check44 family stops): strings / winds / brass t20 0.381 / 0.304 / 0.253 -> 0.376 / 0.304 / 0.253 s.
- S1 (s1check44, 49 points): own-band median 7.4 -> 7.3 dB, under 3 dB 8 -> 8, master median 3.8 -> 3.7. Changed: Violas
  271 own-band 8.9 -> **3.2** dB (stem 11.0 -> 2.9; the linear 268-271 decrescendo leaves less level before the
  repeat); Oboe 1 / Bassoon 1 148 master dip 4.0 -> -0.5 (their stems unchanged at 7.7 / 7.3: the strings' fp attack now
  fills the master on that beat).
- S2 (pcX joins, median): Violins I +15 -> +20 ms, Violins II +14 -> +20 (one join fewer: 148 is a stroke), Violas +3 ->
  +4, Oboe 1 +39 -> +40 (robust SD 53-69 ms).
- S3: steepest 10 ms master fall over the fp 3.1 -> 3.3 dB, at the breath 195-196 3.5 -> 3.8 dB; the fp's fall is CC11
  (pre-hall) and the bump's release is before the post-fader sends, so R Strings rings through it (steepest 10 ms fall
  5.5 -> 3.6 dB).
- State check (c47 -> c48, `state_check.txt`): no level runs. **Trombone 1 213 / 215 / 215.5 +3.6 / +3.1 / +2.6 dB and
  27-49 ms early** on unchanged data (no build of that track; c46 and c47 were sample-identical there): the flipped
  Leg Slur MAX state Movement I c47 found. Basses' low notes +2-3 dB (the 35 Hz high-pass; state_check removes envelope
  changes, not EQ). The rest within ±1.2 dB (Vc div 63 +4.0, one note).

## Trombone 1 splice
Trombone 1's data, mix and EQ did not change and it sends nothing to the returns, so c47's stem is a render of the same
data in the state its tables were fitted on (Tbn1 213 accent +5.7 dB over its pickup since c46; with the flip about
+9). `render_first/` holds c48's own Trombone 1 stem and master; `render/16_Trombone 1.wav` is c47's, and `00_Master.wav`
= c48 master - c48 Trombone 1 + c47 Trombone 1 (the master is the stems' float sum: c48's differed from it by -109
dB). Then `render_cycle.py 48 --measure-only`. Not a data change: nothing in build/ or REAPER. The next build should
**fully rebuild Trombone 1** (Movement I c47: a full rebuild returned a flipped instance to its earlier state; `--midi-only`
does not protect it) and compare 213-215.5 with c47 by state_check.

## Changes (files and parameters)

No Opus state changed (`cycles/c45/actor_scripts/states45.py`: none), so data tracks took `--midi-only` and every track
`--mix-only` (family EQ, track width, gains, envelopes).

Tools (generic):
- `tools/score_to_parts.py`: `FP_SPIKE_AT_MARK` and `FP_VEL` ported from the finale (mvt3 c09; copied, mvt3 not edited).
  With `FP_SPIKE_AT_MARK` an fp's attack level is a step at the mark, so a led note's pull carries the f from its moved
  note-on, and a hairpin printed at the fp starts where the attack has fallen (`fp_hp`, the finale's hairpin shift;
  without it the decrescendo's own points at the mark would overwrite the step). New: `FP_FALL_AT`, parts.json
  `fp_falls` ([mark, end of the fall]).
- `tools/build_reaper.py`: `track_width()` from the finale (mix.json `track_width`, REAPER D_WIDTH after the plugin; full
  build and `--mix-only`). `vol_points()`: under an fp attack (parts.json `fp_falls`) the soft/dyn trims read the p the
  attack falls to, and a decrescendo printed at the fp takes its soft-trim hold level from after the fall. Before, the f
  trim dipped the envelope 4-6 dB under the attack on score time (Violins II p +3.5 / f -0.5, basses +8.5 / +2.5 dB)
  and rose back over 148.15-148.5, part of the c47 fp's late peak; with the step at the mark the hold would also have read
  the f and kept the p after the fp 2-3 dB under its trim up to the next note.

Config (`build/score_config.py`, c48 block at the end):
- A #1 / B #1 (finale item 2): `FP_SPIKE_AT_MARK = True`, `FP_SPIKE = ("f", 0.12, 0.30)`, `DOWNBOW_STROKE_AT` 148 on Violins
  II and Violas (fresh Sus MAX strokes, 0.06 s entry lead, v105; were v124 slur transitions from 146, no slur printed
  into 148). `FP_VEL` stays off: the fp notes play Sus MAX, which ignores velocity (B; DIGEST §2, M1 c06).
- A #1 step 4: basses `LEVEL_SHAPES` [(147.8965, 0), (148.0, 0.83), (148.12, 2.0), (148.3, 0)]. What A read as the
  crescendo gain's release under the attack is pitch_trims.json's -2 dB C sharp 2 trim ramping in over 147.897-148.147;
  it is held off to the end of the f hold and comes back with the attack's fall (A's release across the whole
  decrescendo lifted the p body at 148.6-149.2 by 1.5-2 dB, which shrinks the drop).
- Coordinator / finale item 13 (after the range render): `LEVEL_SHAPES_S` at 148.0 (seconds re the beat) [(-0.06, 0),
  (-0.04, d), (0.06, d), (0.16, 0)], d = +3 dB Violins II and Violas, +5 dB basses. Simulated on the range stems: peaks
  +100 / 0 / +110 ms, drops 11.4 / 14.4 / 13.9; rendered: above.
- A #2: the post-END fade on the six string tracks -4 -> -1 dB (no FINAL_RING).
- B #2: Oboe 1 `LEVEL_SHAPES` +3 dB over 142.10-142.70 (not A's note trims).
- B #3: `HP_CURVE["linear"]` (268, 271) on Violoncellos and Violas; celli `LEVEL_SHAPES` -2 dB over 269.0-269.4.

Per-note tables: `build/roles.json` Horn 1 [188, 204, 2, 4] -> [188, 203.9, 2, 0.1] (B #5).

Mix (`build/mix.json`, `_c48` note):
- C #1: string family bell 456 -> 315 Hz (-2.2 dB, bw 0.75) in `groups.string` and the basses' own copy; make-up
  `gain_db` Violins I -0.1, Violins II -0.3, Violas +0.2, Violoncellos +0.3, Violin I solo -0.2, Violins II div -0.3,
  Violas div -0.1, Violoncellos div +0.1, basses 0.
- B #4 / C #3: basses' family high-pass 53 -> 35 Hz.
- C #2: `groups.horn` `track_width` 0.8 (Horns 1-4, Horns 1-2 a2); make-up Horn 1 +0.3, Horn 2 +0.3, Horn 3 +0.5, Horn 4
  +0.3, Horns 1-2 a2 +0.4. Trombones unchanged.

Loop files: `loop/MANUAL-GAPS.md` #13 (strings Marcato Sustain rows for the fp, not tried), `loop/LEARNINGS.md` c48,
`loop/HISTORY.md` c48, README "Tool changes after the port" c48; `loop/ONE_TIME.md` appended to `ONE_TIME.done.md`.

## Coordinator's items 13-17 (finale SHARED-TECHNIQUES, sent during the cycle)
- 13 (sf/fp bump): adopted after the range render showed the fp still peaking 200-235 ms late (above).
- 14 (per-track SOST_JOIN_LEAD_S for two players on one line): c47's wind entries spread at most 38 ms on the widest shared
  entry (bar 79, -20..+18 ms; `cycles/c47/entries47.txt`), no 80 ms flam; not needed.
- 16 (full-bar-rest text): `build/mockup.ly` listens only for `text-script-event`, so texts on multi-measure rests are not
  in the event dump: the strings' "via sord." at qn 90, Horn 3's "via sord." after its last note, the timpani's sticks /
  damp / muta, two "mettere sord.". None changes the mockup: every coda mute that sounds is printed on a note and is read
  ("con sord." Violas 279, Horn 3 and Violins II 286, Violins I 292), no string plays between qn 90 and its next
  "senza sord." (VlnI 171, VlnII / Vla 108, Vc 124), and no rule reads timpani damp texts. Left as is.
- 17 (repeat gaps on doubled bass eighths): no such figure in movement II.

## Rejected or deferred
- Finale item 3 (sub. p), item 9 (harp cap 123), item 11 (winds 1 kHz -1.55), FINAL_RING, the winds' phrase offsets
  x1.4, the bass clarinet 265 "dip" (A: a 16.7 Hz-bin estimator artefact for C sharp 3; its 60-300 Hz band dip rose
  7.8 -> 17.4 dB): dropped with the critics' evidence (A #4/#5, B items 3/11, C's item table).
- A #3 note trims on Oboe 1 (B's level shape used instead).
- No horn 315 Hz bell (C: Horn 1's own fundamentals, -2.2..-2.9 dB on its solos), no trombone narrowing (C: bars 61-64
  would go narrower than every reference).
- Horn 4 qn 84 loop fill (A, B: inaudible, 12-15 dB under the master).
- Sus Marc LITE fallback for the fp strokes: needs a row load (Opus state change on three tracks); the lead allowed it
  only without one. The CC11 + stroke + bump route met the drop and timing targets (MANUAL-GAPS #13).

## Open
- Violas 271 repeat: own-band dip 8.9 -> 3.2 dB after the linear 268-271 decrescendo (B #3 was aimed at the celli; the
  violas sat 1.3 dB under the tune in c47). Next: the violas back on the curve over 268-271, or a soft gap at 271.
- Master tilt jump at the fp +3.3 dB (A's ceiling 3.0), from the violins' and violas' Sus MAX strokes (+3.0 / +3.2).
- Oboe 1 142.5 gained 1.2 dB, not 2.7: extend B's shape toward 142.80 only together with the 143 fill front.
- Oboe 1 and Bassoon 1's repeat at 148 no longer dips in the master (the fp attack fills it); their stems keep 7-8 dB.
- Trombone 1: fully rebuild at the next build (state flip above).
- The scherzo's c09 finding (kit README, commit 10fc4ec5): an instance's saved state after playback holds legato
  envelope attacks of 20 ms, and a `--midi-only` build keeps that state. Movement II has built its legato tracks
  `--midi-only` since c45 (full rebuild of all tracks last in c44), so its legato leads were fitted on that state; a full
  rebuild of the legato tracks would make loud joins (v112+) about 80 ms later. Not changed here: it needs its own render
  and a lead refit.
