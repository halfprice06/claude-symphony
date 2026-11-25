# Cycle 8 changes (actor, 2026-11-08): final ring, metric basses, tone and width, subito, balance fixes

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c07 render). Snapshot: `before/`. Data as rendered:
`rendered_build/` (parts.json, mix.json, score_config.py before the stem-fix refit). Scripts in `actor_scripts/`:
- `m08.py`: all of this cycle's before/after checks on one render. Its results are `m_c07.json` and `m_c08.json`.
- `apply08_mix.py`: writes build/mix.json from before/mix.json.
- `eqsim08.py`: the family-EQ simulation on the c07 stems.

## Tool code (each option defaults to off)
- `tools/score_to_parts.py`:
  - `FINAL_RING` (A #1). The last chord's wind, brass and string notes skip `CUTOFF_EARLY_S` and are held `ring_s`
    past the written end. The volume envelope falls from the level at the end through the listed points, and the last
    point is held. Recorded in parts.json `final_ring`.
  - `METRIC_BOWED_DB_SPANS` (A #2, C #4): a per-span table for METRIC_BOWED.
  - The metric kind treats the half bar of an even-numbered bar as "mid". In 2/2, beat_kind called it "weak", so the
    second minim beat took the plain-beat step. This also moves the timpani half-bar strokes from -2 to -1 dB
    (METRIC_TIMP_DB).
  - `RR_RESET_AT` / `RR_RESET_CC` (MANUAL-GAPS #6): round-robin resets on Opus's configured controller (CC16), written
    to parts.json lane `cc16`.
  - `UNI_OUTLAST_PLAY` (A #3): an outlasting unison copy whose delayed start would come more than `min_delay_qn` late
    now plays from its own onset. It sits at `db` until the kept note ends, then ramps to 0. Recorded in parts.json
    `uni_played`.
  - `HELD_DECRESC_CARRY` (C #3.1): a held-decrescendo step is not released at a subito-softer or fp/sfp onset. It is
    held to the next crescendo and released across it. Recorded in parts.json `held_decresc_carry`.
- `tools/build_reaper.py`:
  - writes the `cc16` lane, with no pre-roll copy;
  - a mix.json return may carry `side_shelf`: the M/S chain goes after its FX, and the read-back checks only the
    return's own (first) ReaEQ.
- `tools/stem_fix.py`: passes `__file__` to the exec'd build_reaper source. It failed since c07's fxchunk import.

## Data
1. **Final chord (A #1).** `FINAL_RING` {at 1112, end 1113, ring_s 0.45, pts (0.15 s -8, 0.30 s -16, 0.45 s -24 dB)},
   on 27 tracks. The release caps and return levels are unchanged.
2. **Metre in the hammered eighths (A #2 and C #4, one table).**
   - `METRIC_BOWED_DB`: down +2.0, mid +1.0, beat 0, off -1.5.
   - Spans: violas / celli / basses 792-840 and 984-1080; basses to 1088.
   - Basses span tables, refit on the render (see the stem fix): 984-1056 (1.0, 0.5, 0, -0.5), 1056-1088 (0.5, 0.5, 0,
     -0.5).
   - CC16 reset before the basses' 1056 eighths.
   - No velocity table: velocity does not move the KS Master Sus MAX rows.
   - No seeded jitter: the round robins already scatter 3-6 dB SD per position.
3. **Unison stubs (A #3).** `UNI_OUTLAST_PLAY` {min_delay_qn 0.3, -6 dB, ramp 0.25 qn}: Oboe 2 at 844 and 856,
   Horn 1 at 118, Horn 2 at 122.
4. **Portamento (A #5).** `PORT_TARGETS` 941 v80 -> v45 on Violins I and II, with leg_leads +0.04 s. Violins II had
   the key "941" (0.07), now 0.11; the duplicate "941.0" key is removed.
5. **Repeats (A #6).** The celli detach span 824-836 now takes repeats up to a whole note (`max_qn` 4.0).
6. **Subito and sfp (C #3).**
   - `HELD_DECRESC_CARRY` {max_qn 8}: 10 tracks hold their steps through 872 and release them over 876-880.
   - Timpani roles -4 dB at 832-836 and 872-876.
   - `SFP_SPIKE_S` (0.15, 0.35) and `SFP_VEL` 110.
   - String sfp leads at 592, +0.06 s: entry_leads.json for violas and celli. For Violins I / II and basses, which
     are abutting re-attacks that entry_leads does not reach, a `ROW_LEAD_S` span (591.9-592.1, 0.06).
7. **Balance (B).** roles.json:
   - #1: Violins I 892-899.9 -2 -> -6 dB; Horns 1-4 892-928 +2 dB with a 4 qn end ramp.
   - #2: celli 488-495.9 +3.
   - #4: Violins I soli -4 at 472.5-477 and 484.5-488.

   note_trims.json:
   - #2: harp 488-495.5 -4.
   - #4: Clarinet 1 481 / 483 / 484 -4.
8. **Mix** (`apply08_mix.py`; no Opus state change, so `--midi-only` on all 31 tracks plus `--mix-only`):
   - C #1: brass 821 Hz bell -7.8 -> -4, plus a 3.2 kHz -4 dB bell (1 oct); strings and basses 1005 Hz -5 -> -2.5;
     winds 1000 Hz -3.1 -> -1.55.
   - C #1 gains: horns -1.0, trumpets -0.8 (Trumpet 3 -1.6), trombones -1.0, tuba -1.7, strings -0.5, winds -0.8.
     Simulated A-weighted change after EQ plus gain: horns +0.6..+1.0, tuba -0.6, all others within ±0.35 dB.
   - B #5: tuba family EQ plus a 143 Hz -4.3 dB bell.
   - C #2: the side high shelf (250 Hz +1.5) is removed from 22 wind and brass tracks. A side low shelf at 400 Hz
     -8 dB is added on celli, basses, tuba, the trombones, contrabassoon, timpani and all four returns.
   - C #5: trombone pp / ppp soft trims 8.0; Horn 1 pp / ppp -3.

parts.json: 0 WARNING; re-bows unchanged (no space_rebows run). No track's Opus state changed (art rows, first
keyswitch, mute and mix state inputs are identical), so there was no full rebuild.

## Rejected / deferred
- **Brass-accent 2-5 kHz jump target**: rejected with numbers (LEARNINGS "Measurement: brass accent brightness"). The
  check is replaced by the tilt jump, the jump on sounding brass, and front minus body (m08.py `accents`).
  - c08: tilt p90 3.4 dB (c07 3.6; target under 3).
  - Sounding-brass jump p90 -1.6.
  - Front minus body median -8.0 dB.
- **821 Hz bell -4**: chosen by C's band shares, not by the accent metric (that metric is withdrawn). The c08
  old-style jump p90 went 5.2 -> 4.4 anyway.
- **Coordinator's Movement I c50 width fix** (Main at the seat ±0.8, side 200 Hz -6 dB): compared by measurement
  rather than built, because it changes the Opus state of about 20 tracks (full rebuilds).
  - On width49's measure, C #2 matched it at 250 Hz-5 kHz (0.469 vs 0.483) and on side/mid (-4.74 vs -4.71).
  - It overshoots below 250 Hz: 0.724 against 0.584 (refs 0.54-0.62).
  - c09: side low shelf -8 -> about -4 dB (mix-only), or take Movement I's layout if that misses.
- **4-8 kHz** is still 2.5 dB over the references (-19.4 vs -21.9). C's next step is the brass and string shelves +2
  -> 0. It is an EQ change, not level-only, so it is left for c09.
- **A #4 per-accent fixes** (Trumpets 1-2 at 360 v111 -> 95; Horn 1 1058 / 1066): deferred. The tilt p90 is near
  target.
- **A #6 Vc 832 and Vln I 884**: these need a new-bow rule for slur heads and for div-chord-to-legato repeats, which
  is deferred.
  - Vc 832 dip 1.2 -> 4.1 dB (a side effect of the 828 detach).
  - Vln I 884 still 0.3 dB.
- **Violas' soft end at 455.86**: a measurement artefact, no change. The violas stop at 454.86. The 455.86 window
  holds the celli and basses entering in R Strings (+7.5 dB at +0.2 s) and the violas' pizz at 457. The violins' own
  soft ends (stem + R Strings) are 0.22-0.40 s.
- **C #5 premise**: the trombones' only pp (568) is a pp < f crescendo over two bars. At 568.3-570 they sit 9-10 dB
  under Horn 1 in both renders, so the pp trim change has almost no effect. It is kept as harmless.
- **Spiccato length (batch 7)**: already met. Every short-row note is 0.50 of its slot (A). The hammered détaché
  eighths stay as they are (C).
- **Pass-2 A/Bs** (CC1-only, narrow brass): not run, for memory (44-45 GB settled).
- **sfp at 592**: not fixed.
  - The master's sf peak is now in the 592.75 frame at -19.1 dB (ff before -18.5; c07 592.5 at -20.4).
  - The p after it is 3-7 dB under, against the 10 dB target.
  - The longer spike moved the peak later. c09: a shorter hold and the timpani roll's fall.

## Measured (c07 -> c08; m08.py unless named)
- **Final chord** (master at fixed times after the written end 1113, re the 0.25 s before):
  - c07: -12.4 at 0.10 s, -21.9 at 0.30 s (20 dB in about 0.25 s).
  - c08: -7.2 / -9.7 / -15.3 at 0.10 / 0.15 / 0.30 s, -20 at about 0.42 s.
  - Targets: 14-17 dB at +0.3 s and -20 dB in 0.40-0.50 s. Met.
  - No stem step at 1113 over 1.7 dB.
  - Stems at +0.3 s re the master before: Trumpet 1 -59 -> -25, violas -65 -> -30 dB.
- **Wetness ceiling** (wetsim07, aligned):
  - tutti -20 dB median 0.39 s (c07 0.41);
  - drop at +0.3 s 13.4-21.0 dB;
  - RT60 1.26 s;
  - returns -13.7 dB under the dry sum.
  - Held.
- **Metre, basses** (first 120 ms of each eighth, after the stem fix), downbeat minus off-beat and beat minus
  off-beat, per-position SD unchanged:
  - 792-840: +1.0 / +0.6 -> +3.4 / +1.7 dB.
  - 984-1056: +3.5 / +2.8 -> +3.5 / +2.7 dB.
  - 1056-1088: -1.4 / -2.3 -> +3.9 / +3.3 dB.
- **Tone**, octave shares of the loudest 10 % of master frames (125-250, 500-1k, 2-4k, 4-8k):
  - c07: -8.5 / -7.9 / -9.3 / -18.3 dB.
  - c08: -11.3 / -6.2 / -10.7 / -19.4 dB.
  - Centroid 1007 -> 993 Hz.
- **Width**:
  - L/R correlation per octave, 31 Hz-8 kHz: c07 0.20 0.47 -0.04 0.42 0.34 0.35 0.25 0.32; c08 0.85 0.88 0.71 0.62
    0.42 0.42 0.35 0.40.
  - Side/mid -3.2 -> -4.5 dB (loud frames); -2.61 -> -4.74 dB (all frames, width49).
- **Subito 872**:
  - master 869-871 -> 872-874: c07 -32.9 -> -33.2; c08 -32.5 -> -34.2 dB.
  - winds: c07 -49.6 -> -40.2; c08 -49.2 -> -45.2.
  - strings: c07 -40.7 -> -37.3; c08 -40.3 -> -37.9.
  - Better, but short of the 5 dB drop.
- **Repeat dips** (dry stem): Vc 828 1.5 -> 5.3 dB, Vc 832 1.2 -> 4.1, Vln I 884 0.3 -> 0.3.
- **Balance** (dry stem RMS):
  - Chorale 892-900: Violins I 6.1 dB under Trumpet 1 (c07 1.8). Target 4-6.
  - Horns 1-4 re Trumpet 1 over 900-928: +3.7 / +3.6 / -1.8 / +1.5 dB (c07 +2.2 / +2.3 / -4.0 / -0.3).
    Plain RMS counts the horns' low end; B's K-weighted target was 2-4 under. Critics should re-check.
  - Cello tune minus harp 488-496: -9.3 -> -2.6 dB.
  - Bassoon solo over the Violins I soli: 4.7 -> 8.0 dB.
  - Bassoon solo over Clarinet 1 (481-485): 4.1 -> 4.8 dB.
  - Horn 1 pp at 264-300: -2.8 dB.
  - Timpani p rolls: -3.2 dB at 832, -3.6 dB at 872.
  - Unison stubs: Oboe 2 856 +4.9, Horn 1 118 +1.6, Horn 2 122 +5.0 dB. None is left in the silent-note list.
- **Loudness**:
  - Master -19.6 LUFS, LRA 23.5 LU, peak -0.6 dBFS (0.931; no float replacement needed).
  - Delivered -19.8 LUFS, LRA 14.6 LU, TP -1.6 dBTP, limiter about 0.1 dB, p10-to-max span 18.5 dB.
  - Loudest bars 278 and 223 (-14.4), then 279, 262, 263.
- **Attack probe**: 1 flag, Violoncellos qn 24 +0.43 s, the same build-shape artefact as c00-c07.
- **Pre-roll**: strings sound in the pre-roll, as in c06 and c07 (first notes led before qn 0).

## Stem fix
- The CC16 reset flipped the basses' bow cycle, so A's 1056-1088 table overshot (down minus off +6.9 dB) and C's
  table gave 984-1056 +5.5. Both span tables were refit (Data 2) and applied with `stem_fix.py 8 rendered_build build
  "Double basses" --apply`: envelope change -1.0..+2.0 dB, originals in `render_first/`.
- The same data was written to REAPER with `--mix-only "Double basses"` while the lock was held.
- The mp3 was delivered again from the fixed master (`deliver_stemfix.log`).

## REAPER
- Lock 18:32-19:04 (32 min). Before that: mvt2 held it until 17:13, then mvt1 c50's older waiter until 18:32.
- Steps: start, open, `--midi-only` (31 tracks, no reload), `--mix-only`, restart, settle to 44 GB (9 min, 0
  compressed), Audio_Init (48000 / 512 / no input), render.
- REAPER memory after the render: 44-45 GB, 28-40 GB compressed.
- c07 stem WAVs deleted (00_Master.wav kept).
