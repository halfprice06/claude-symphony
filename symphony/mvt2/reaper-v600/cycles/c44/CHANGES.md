# Cycle 44: changes (actor; critics A/B/C on the c43 render; loop/ONE_TIME.md: the EastWest template mix)

- Snapshot before the changes: `before/`. Scripts and logs: `actor_scripts/` (`apply44.py` writes build/mix.json from
  before/mix.json; `check44.py` tails, balance and spectrum; `s1check44.py` repeat dips; `turn_lock.sh`).
- Pass-2 copy of the old c43 layout (ONE_TIME): the c43 stems themselves (`cycles/c43/render`, Opus hall, old mics),
  measured with the same scripts (`actor_scripts/check_c43.json`, `s1_c43.txt`). No A/B excerpt render: a second
  32-instance project does not fit the 45 GB limit.

## Tools (from the finale's REAPER-verified c06 build_reaper.py; Movement I's offline-tested tools not used)

- `tools/build_reaper.py`: the finale's c06 template hunks (its c06/before -> c07/before diff) applied to this folder's
  copy (this folder's list-form release caps and other code kept): mix.json `pan_by_mic`, `track_pan`,
  `reverb.opus_off`, `returns` + `returns_job`, group/track `return` sends (post-fader), `family_eq` ("FAMILY EQ" ReaEQ
  loaded from a chunk and read back).
  - New here: `return` may be a list of `{to, db}`; a return's `post_eq` [bands] adds a ReaEQ after Spaces II (the
    2.3 kHz tail low pass, plan section 9; loaded and read back like the family EQ); the finale's c07 `set` / `hp_hz`
    chunk edits (`tools/fxchunk.py`, copied from the finale's c07 work; string values added for impulses), read back.
- `tools/render_cycle.py`: mix.json `test_returns` stems go to `cycles/cNN/test_stems/` and `00_Master.wav` is rebuilt
  as the float sum of `render/` (REAPER's own master kept as `test_stems/00_Master_reaper.wav`).
- `tools/deliver_master.py`: mix.json `master_eq` applied before the ride (the finale's code; reads build/mix.json).
- `tools/stem_fix.py`: `--return-gain` (the finale's).
- `tools/score_to_parts.py`: `STR_REP_NEW_BOW` `soft_gap_s`, `soft_fall`, `soft_gap_at`, `loud_gap_s` (critic A #1).

## Data

- `build/mix.json` (written by `actor_scripts/apply44.py --final --stemfix` from `before/mix.json`):
  - Mics (plan item 1): strings Close 0.5 / Main 1.0 (patches shipped Close 0.65-0.94 / Main 1.0); div / solo tracks
    (Close only) keep their patch Close level; horns 0.48 / 1.0; trombones 0.34 / 1.0 (patch 0.486); tuba 0.31 / 1.0;
    woodwinds Close-led by the template's dB (Fl -4.7, Fl2/Cl -3.4, Ob -20.6, CA -11.6, Bn/Cbn -8.6, BCl -9.8), scaled to
    the old group's mic power (as the finale). Harp keeps Close 0.6 / Main 1.0. **Timpani keeps its old Close 0.2 / Main
    0.5 with no Surround mic** (the template's Surround at 0 dB makes rolls drown other parts; Movement I) and the
    finale's reduced EQ (HPF 44, -6 dB 385 Hz, +4.5 dB shelf 6.96 kHz), **not the template's +8.6 dB at 84 Hz** (critic B
    #1 predicted the timpani's share of 30-150 Hz going to 58-80 % on the rolls with it).
  - `pan_by_mic` (Close at the seat, Main full width); seats: the template's Close pans for strings and brass (Vln I
    -0.31, Vln II -0.07, Va 0, Vc +0.33, Cb +0.62, horns -0.25, trombones +0.25, tuba +0.35; div/solo tracks as their
    section); `track_pan` from the plan (Vln I -0.10, Vln II -0.21, Va 0, Vc +0.15, Cb +0.23, Hn1-4 -0.18/-0.16/-0.15/-0.13,
    a2 -0.16, trombones +0.15, tuba +0.23). `width_by_mic` removed.
  - Opus hall off on every track; returns R Strings / R Brass / R Winds / R Perc (template chains; see "Wetness" for the
    adopted IR envelope and faders), each with a ReaEQ low pass at 2.3 kHz after Spaces II (plan section 9).
  - Sends (post-fader): strings -5.56, celli and Vc div -7.16 (Duc -1.6), horns -8.77, winds -8.36, timpani -6.41, harp
    -8.77 dB; **trombones, tuba, bassoons, contrabassoon and basses send nothing** (finale c07; the -10 dB register sends
    of the render were not enough, see below).
  - Family EQs (FAMILY EQ ReaEQ): strings, brass, woodwinds from the template; harp with HPF 80 Hz (B #4, not 183);
    timpani as above; basses + Duc's -3 dB at 228 Hz, their body bell 160 Hz bw 1.4 -> 140 Hz bw 1.0 (B #6). Master EQ
    (HPF 42, -1.6 dB 167 Hz, -1.9 dB 1.18 kHz, +0.8 dB shelf 8 kHz) in deliver_master.
  - Removed as duplicates of the family EQ (B #6): high passes on every string, brass, harp, harp harmonics and timpani
    track; the bass clarinet's 2.5 kHz -4 shelf; Horn 1 / Horn 3's c40 300 Hz -2 bell and Horn 1's c40 +1 soft trims.
    Kept (B #6): Violins I / Violin I solo 5 kHz -4, Vln II div 1 kHz -10, Vln II 3 kHz loud_eq, celli / basses body bells
    and climax loud_eq, Cbn / tuba 70 Hz shelves, Trombone 1 accent shelf, horn 800 Hz soft shelves, Horns 3-4 mute_eq,
    side shelves, woodwind 30-40 Hz high passes. (No trumpets in this movement, so no trumpet shelf to remove.)
  - Make-up gains (B #2 per-track values with the finale's measured corrections): winds B minus 2.9 (Fl1/Fl2/CA/Cl2
    +0.4, Ob1 +0.2, Ob2 -0.2, Cl1 +0.1, BCl -0.1, Bn +0.5, Cbn -0.7), horns B minus 0.5 (Hn1 +6.5, Hn2 +5.0, Hn3 +7.0, Hn4
    +7.5, a2 +6.5), trombones/tuba B plus 0.8 (Tbn2/BTbn/Tuba +6.8; Trombone 1 +4.9 only, rule 9), harp +2.2, harp
    harmonics +1.0, timpani 0. After the render (stem fix): Bass clarinet +1.5, Oboe 1 -1.5, Flute 1 -1.0, Timpani +1.0.
- `build/roles.json`: Horn 1 [20.5, 23.5, -2.5] removed (C #2) with `HP_SOFT_GAIN_AT["Horn 1"][20.0] = 3.0`; Harp
  [17.9, 44.0, -2.0] removed (B #4); Clarinet 1 +2 over 279.9-292 (C #4) added, then removed after the render (the
  template mix had already put the coda solo 6.5 dB over the cor anglais; now 4.5).
- `build/score_config.py` c44 block: `STR_REP_NEW_BOW` soft_gap_s 0.08, soft_fall 6 CC at mp or softer (the track's
  sus_fall where it has one), soft_gap_at (the listed printed repeats Vln II div 114/116/119/120, Vln II 112/120, Vla div
  79), loud_gap_s 0.10 (critic A #1). parts.json against c43: only those repeat pieces (Vln II, Vla, Vla div, Vln II div,
  Cb 262) and the three role tracks changed; 0 WARNING. Every track's Opus state changed (hall off, mics): all 32 fully
  rebuilt, plus 9 returns.
- `tools/deliver_master.py`: RATIO 2.2 -> 2.4 (re-fit to the dry + returns master: 2.2 gave span 19.1 dB).

## Render and the wetness fix (coordinator / critic C targets, measured against c43)

The render carried, in parallel, the template returns (R *: full IR, faders +1.03 / +0.66 dB, register sends -10 dB),
the same returns with the Spaces II IR envelope (RE *: irSetup envelopeMode 2, endPos 0.5, decayLength 0.5, low-
instrument sends off) and Duc's 2.3 s hall (R Duc, fader -5.5, sends 0 / register -10 / celli -1.6), the last two as
test stems (`test_stems/`). The template returns are kept in `test_stems/ew_template/` with their master.

Family tails (family dry stems + own return; at family stops with 1.2 s of rest; median time to -20 dB, smallest drop
at +0.3 s; `check44.py`):

| | c43 (Opus hall) | c44 template returns | c44 adopted | target |
|---|---|---|---|---|
| strings t20 / min drop at 0.3 s | 0.52 s / 8.1 dB | 0.72 / 6.3 | 0.55 / 7.5 | 0.40-0.55, >= 13 |
| winds | 0.35 / 15.3 | 0.49 / 12.5 | 0.35 / 16.8 | 0.30-0.50, >= 13 |
| brass | 0.37 / 15.5 | 0.55 / 11.5 | 0.34 / 15.3 | 0.30-0.50, >= 13 |
| master, final chord t20 / drop at 0.3 s | 0.45 / 11.0 | 0.83 / 8.4 | 0.44 / 11.4 | |

- The template returns made every family wetter than c43. The register sends alone could not fix it; return level
  barely moved the time (EW strings at -10 dB still 0.57 s at bar 36, final chord 0.70 s). The IR envelope did: strings
  at bar 36 0.46 s at -10 dB, final chord 0.63 / 0.51 / 0.46 s at -10 / -14 / -18 dB. Duc's hall at -6 / -10 / -14 dB gave
  a final chord of 0.62 / 0.54 / 0.50 s, no better than the envelope.
- Adopted (exact, from the rendered RE stems scaled): IR-envelope returns, low-instrument sends off, return faders
  strings -18 dB (now -16.97), winds -4 (-2.97), brass -2 (-0.97), perc -3 (-2.34) against the template. Written into
  REAPER with `--mix-only`; R Duc and the RE tracks remain in the project with no sends (silent; the c45 actor can delete
  them).
- What stays above target is set by the dry stems, not the hall: the strings' bar 3/4 stop (Vln I's ppp C5 at qn 10.4)
  falls 20 dB in 0.67 s dry (c43 0.665) with 7.4 dB at +0.3 s, and the final chord's morendo falls only 9 dB dry by +0.3 s
  (c43 11.0). The strings' bar 36 stop is 0.42 s dry, 0.44 s with the return (c43 0.38).
- Harp and timpani family tails read 1.9-18 s because R Perc carries both (one keeps sounding when the other stops);
  their dry tails equal c43's (harp 0.17 s, timpani 0.25 s).

## Measured (c43 -> c44 delivered; `check44.py`, `s1check44.py`, `accent44.py`, `rbdip44.py`)

- Master (dry + returns): -22.9 LUFS, LRA 22.6 LU, TP -3.8 dBFS, peak 0.642 (c43 -20.4 LUFS, LRA 24.1, TP -1.3).
  Delivered: **-19.8 LUFS, LRA 15.3 LU, TP -1.6 dBTP, span 18.9 dB, limiter 1.9 dB** (c43 -19.8 / 15.5 / -1.6 / 18.6 /
  2.1). Attack probe: 0 late or hole.
- Spectrum and image (the numbers for Movement I): master band shares 100-250 Hz -8.7 -> -7.4 dB, 200-500 -4.8 -> -4.5,
  500-2000 -3.1 -> -4.3, 2-6 kHz -10.5 -> -8.6, **6-20 kHz -30.1 -> -24.6** (references -28.8 to -32.3; the template-return
  version -25.9). **Side/mid -6.1 -> -2.2 dB, L/R correlation below 250 Hz 0.66 -> 0.06** (references -4.7..-5.4 and
  0.54-0.62): the full-width Main pairs are decorrelated in the bass (Violoncellos -0.09, Tuba -0.03, Trombone 2 -0.06,
  Horn 3 0.08 per stem; c43 strings 0.54-0.76). 315-500 Hz re 1 kHz over bars 7-30 5.7 -> 8.9 dB and 2-4 kHz re 1 kHz
  -11.1 -> -6.0 (the family EQs cut 1 kHz itself, so this ratio no longer measures "mush"; the 200-500 Hz share rose
  0.3 dB).
- Balance, A-weighted on the dry stems (c43 on its wet stems), family minus strings, whole piece: winds -2.9 -> -3.0,
  brass -2.4 -> -2.4, timpani -20.9 -> -22.4; bars 61-62 brass -1.3 -> -0.9, bars 79-81 horns minus strings -4.2 -> -4.1.
  Lead over all other stems: Horn 1 bars 7-14 7.0 -> 6.0, bars 67-70 4.1 -> 7.0; Oboe 1 bars 15-16 7.7 -> 8.2, bars 45-47
  3.9 -> 5.7; Flute 1 bars 37-40 6.6 -> 7.4; bass clarinet bars 31-36 2.6 -> 2.4; cor anglais bars 41-44 1.8 -> 1.3;
  Clarinet 1 coda 0.7 -> 1.9, over the cor anglais 1.8 -> 4.5; Violins I over the celli bars 89-91 5.4 -> 5.3; Trombone 1
  over strings + bass trombone 11.3 -> 10.1 (my measure; B's method differs).
- Timpani share of 30-150 Hz: bars 1-3 10.6 -> 14.9 %, qn 168-172 25.2 -> 32.1, bars 60-62 8.2 -> 7.7, bars 67-70 15.9 ->
  18.4, bars 78-81 8.5 -> 9.4, bars 84-85 16.9 -> 18.5 (before the +1 dB stem fix: 12.4 / 27.4 / 6.5 / 15.2 / 8.4 / 15.4).
- S1 (A's method, 50 printed / rule repeats): own-band dip median 6.2 -> **7.4 dB**, under 3 dB **14 -> 6**, master 3.3 ->
  3.9. Fixed: Vla 271 0.1 -> 7.5, Vla 71 6.2 -> 16.6, Vln II 51 2.8 -> 5.8, 144 4.1 -> 7.3, Vln II div 114 0.0 -> 2.3, 116
  2.1 -> 4.1, 119 2.1 -> 4.2, Vla div 79 2.5 -> 5.9, Cb 265 stem 1.2 -> 8.0. Still under 3: Vln II 289 (0.4), Vln II 120
  (0.3), Vla 87 (2.5).
- S2: probe 0; Violins I legato pcX median +22 ms, robust SD 66 (c43 +23 / 70); joins 257 / 262 / 266 flipped back to
  -49 / +97 / -60 ms (c43 +57 / -3 / +36, c42 -47 / +101 / -49): render variation, as critic A said; no lead change.
- S3: fastest 50 ms master fall at the fp (148) 2.7 -> 2.3 dB, at 195-196 2.3 -> 2.7, in the bar 66 niente 3.2 -> 2.6;
  the niente falls steadily (per 0.5 qn from 222.5: -45.3 -44.7 -47.0 -49.4 -50.1 -53.3 -52.9).
- Brass accents (A #6, rule 9): Trombone 1 2-5 kHz first 80 ms minus body 213 -9.9 -> -10.0 dB, 218 -14.0 -> -15.7;
  master 2-5 kHz jump at 213 / 218 / 214.875 -5.8 / -4.8 / -4.7 dB (all under +2). Level over the note before: 213 6.7 ->
  2.1 dB (less weight), 218 1.0 -> 5.0: open for c45.
- Re-bows (string re-bow points, stem): dip median 3.1 -> 3.6 dB (the wider soft-repeat gaps are part of it), dips
  over 8 dB 4 -> 5, peaks over 3.5 dB 18 -> 19. Not refit: the fills were not measurably worse on the dry stems.
- State check against c43 (`state_check.py`; `actor_scripts/state_check.txt`, `state_check_residual.txt`): every track
  shifts by the mix change (strings -2 to -4 dB, winds -3 to -5.5, brass -7 to -9.6 on the dry stems); after removing
  each track's median shift, one small run (Bassoon 1 near qn 21, 3 notes -3.9 dB) and no state flips. No test aliases
  exist in this movement, so alias_check did not apply (the test stems are returns).
- Dan's item 8 (loop pulsing) not re-measured; held-note data and re-bow points unchanged apart from the soft gaps.

## REAPER

- Lock 16:12:48-17:13:40 (61 min), after the turn rule (Movement I c49, the scherzo c06 and the finale c07 went first;
  my first lock call was withdrawn because the scherzo had waited longer). Start + open (32 tracks, settled 44 GB),
  full build of 32 tracks + 9 returns (the first try stopped on a presetName read-back; dropped), restart (settled 43 GB
  in 14 min, 0 compressed), disk 75 GiB, audio 48000 / 512 / no input after `_c44_audio_init.lua`, `render_cycle.py 44`
  without `--force-memory`. After the render: **44 GB, 26 GB compressed**; stem fix + `--mix-only`; save; quit; unlock.
- Project: 41 tracks (32 + R Strings, R Brass, R Winds, R Perc, R Duc, RE Strings, RE Brass, RE Winds, RE Perc).
- `rendered_build/` = the data the render was made from; `delivered_build/` = build/ now (adopted returns, stem-fix
  gains, Clarinet 1 role removed). `render_first/` holds the five stems the stem fix replaced.

## Rejected / deferred

- Deferred to c45 by the brief: plan sections 5-9 performance data, critic A #2-#4 (A #3 bass clarinet leads, A #4
  viola portato velocities), critic C #1 rubato (c46) and C #2's other swells (Vln I 240, Flute 1 108), A #1 (c) Horn 2
  208 and (d) bass clarinet 33 LegRep.
- Brightness (B #3): 6-20 kHz -24.6 dB, over B's -27 threshold. B's next step (halve the strings' and brass shelves, then
  a 5 kHz -4 shelf on Vln II / Vln II div) is an EQ change, not a stem fix: c45.
- Image: correlation below 250 Hz 0.06 and side/mid -2.2 dB with the template's full-width Main pairs. Candidates for
  c45: side low shelves (the existing `side_shelf`) on strings and brass, or Main width under 1.0 below 250 Hz.
- Timpani +1 dB (stem fix) raised the rolls' share of 30-150 Hz to 15-32 %; revert it if c45's critics find the rolls
  heavy (rule 5).
- Pass-2 items: the 2.3 kHz return low pass is in (default); narrow brass (batch 5) is in through the template seats and
  width 0.3; the ALGO GLUE return was not tried.
- Movement I's send-envelope fix (template_mix.py) does not apply: these tools have no send envelopes.
