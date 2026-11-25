# Cycle 26: changes (actor, on the c25 render)

STATUS: **rendered once**, 2026-11-18 06:10-06:21 CST, from a freshly restarted REAPER after a full build of all 31 tracks
(guard 0 stale; memory settled at 44 GB, 0 compressed). Attack probe: late or hole 0. No stem fix. The mp3 was delivered a
second time from the same master after a delivery-only change (fugato ride lifts, LRA), with no new REAPER render.
- mp3: `cycles/c26/scherzo-mockup-c26.mp3`. Data as rendered: `cycles/c26/build_render/`. Records: `cycles/c26/records/`.
- Lock (`phase.log`): taken 05:17 with no other waiter, released 06:25: **68 min** (control ranges, a variant build, two
  variant range passes, restart, full build, restart, render, save, rebuild of 4 stale tracks, save, quit).
- REAPER memory: 44 GB settled before the render and **44 GB after it** (0 compressed); 59 GB during the range passes.
- After the save that followed the render, Bassoon 2, Contrabassoon, Horn 4 and Violins I were stale; rebuilt, saved,
  guard 0 stale (also on the project saved at quit).
- **Every track is 3 dB lower from this cycle** (`global_gain_db` -3): stems and master read 3 dB under c25 at equal
  balance. Master -24.4 LUFS, LRA 21.9, sample peak 0.725 (-2.8 dBFS); no stem over -1 dBFS; the master did not clip.
- Disk: c25's stems deleted (its 00_Master.wav and mp3 kept), my range WAVs deleted; 42 GB free. Backups/ not touched.

## Changes

### Tools (generic, off by default)
- `tools/score_to_parts.py`
  - `HP_HOLD_TO_NOTE_END`: never holds through a printed decrescendo that overlaps the held span (C #3; always on with the
    rule). parts.json `hp_hold_skipped_dec`. Exactly C's six holds are skipped: Flute 1 549, Clarinet 1 / 2, Bassoon 1 / 2,
    contrabassoon 213.
  - `SLUR_END_BEFORE_STAC` {track: {s, spans, rows, min_qn}}: a legato-row note followed within 0.1 qn by a staccato of
    another pitch ends s seconds before the staccato's moved note-on (output stage, after every lead / overlap rule).
  - ACCENT_CC keys `lead_s` (the bump is up that long before the moved note-on), `body_cc` / `body_s` / `body_soft` /
    `body_min_s` (a CC11 body dip after the bump on accented notes of 0.42 s or more that are not legato targets, held to the
    next moved onset).
  - HP_CURVE `cresc_after_fp` {pt, hold_qn}: a crescendo starting on an fp / sfp holds the p hold_qn, then rises on its own
    curve point.
- `tools/build_reaper.py`
  - `stretch_cc7(tr, grid, vals)` (mix.json `dyn_trim_to_cc7.stretch_cc7` {max_qn, floor_db, except}), applied to the
    finished envelope after note_move_guard / note_slew: inside each sounding stretch of 16 qn or less the envelope holds the
    stretch's highest level (from the end of the tail hold before it to the stretch's end) and CC7 carries the difference
    (ramps resampled every 10 ms, explicit points at the stretch ends); in longer stretches only falls in the last 16 qn are
    held. Final-fade stretches are left alone. Net level against the c25 envelope + CC7: median 0.00, p99 0.08-0.33 dB per
    track (`actor_scripts/net26.py`).
  - `sus_release_cap_ms` key `tleg` (caps the TLeg transition groups too); `rt_gain_db` key `dyn` (only "<dyn> RT" groups);
    top-level mix.json `global_gain_db`.
- `tools/render_cycle.py`: prints `WARNING peak over -1 dBFS` for the master or any stem (B #6).

### Data (`build/score_config.py` c26 block; `actor_scripts/apply26.py` writes roles / mix / leg_leads / entry_leads from `before/`)
1. **Dan's figure in the woodwinds** (A #1, coordinator item 1): Flute 1 / 2, Oboe 1, Clarinet 2 in 312-360 / 912-960:
   - slur end 35 ms before the staccato's moved note-on (`SLUR_END_BEFORE_STAC`; 9-10 notes per track);
   - release cap 120 ms on the legato row's f sustain groups and all TLeg groups (shipped 177-237 ms), f release trails
     -6 dB (one-shot, 1000-1245 ms; read with load_oib);
   - Oboe 1's ten tutti staccato quarters v100 -> v118 (Stac DblTng layers 1-74 / 75-114 / 115-127).
2. **HP_HOLD_TO_NOTE_END** regression fixed (C #3).
3. **Guard notes** (B #1 / #3 / #4): `stretch_cc7` on; Oboe 1 spans as steps [386.76, 392.89, -4.5, 0, 0] / [854.76, 860.89,
   -4.5, 0, 0]. Horn 3 950's UNI_BOOST edge needed no score_to_parts change (its rise and fall now sit in the rests).
   Clarinet 1's fall at 900.0-900.5 is in CC7 (no envelope point in 899-901.5).
4. **Summit** (B #2, C #1): roles Trumpet 1 / 2 [1005, 1016.5, +2] and Horn 1 [1004.75, 1014, -1.5] deleted; the 1005 stroke on
   "Sus Marc LITE" on Violins I / II and violas (v92, lead 0.06 -> 0.085 s through entry_leads +0.025; REATTACK_LEAD_AT does
   not apply after a rest); CC11 counter-shape (1005.35-1006 0 -> -10, -10 to 1007.3, back by 1007.5).
5. **Accent fronts** (A #2): strings `lead_s` 0.06, `body_cc` -8 (`body_soft` -4 under CC11 60), `body_s` (0.22, 0.36); cor
   anglais, Clarinet 2, Oboe 1 `body_cc` -6.
6. **sfp < at bar 301** (C #2): `cresc_after_fp` {pt (0.6, 0.3), hold 1 qn}; ACCENT_CC_AT 902 +22 -> +12 (Violins II, violas,
   celli); ride row ends at (899.6, -2) / (900.0, 0).
7. **Spiccato** (A #3): STAC_ROW_BY_PITCH split into three rows per pitch range (vel add -13 / -20 / -33 below 67 / 80 / 90).
8. **Smaller**: global gain -3 dB (B #6); celli leg_leads per A #5 (511.5 -0.025, 512 +0.04, 510 / 514 / 519 +0.06, 528 / 544
   +0.07, 542 -0.07); Flute 2 213 v110 (C #5b); violas / Violas div lifts 636.5-672 removed (B #5).
9. **Delivery**: fugato ride lifts +1.5 -> +0.5 dB (first delivery LRA 10.4; +1.0 also 10.4; +0.5 10.5).

Opus state changes (full rebuild): Flute 1 / 2, Oboe 1, Clarinet 2 (caps, trail gain), Violins II and violas ("Sus Marc LITE"
row loaded). The final build wrote all 31 tracks in full.

## Range tests (`rangetest/` WAVs deleted; numbers here)
P0 control (c25 project), P1 the c26 candidate on 8 tracks, P2 = P1 without the slur-end change (winds). Memory settled and a
discard before each batch.

Woodwind figure, staccato over the old pitch at +70 ms (dB), qn 318 / 330 / 344 / 348 / 354:

| track | P0 | P2 (cap, trails, vel) | P1 (adopted) |
|---|---|---|---|
| Flute 1 | -7.2 / -5.1 / -3.2 / -8.8 / -6.6 | +0.3 / +3.6 / +5.3 / -2.4 / +0.4 | **+27.0 / +12.1 / +28.2 / +17.5 / +27.7** |
| Flute 2 | +1.0 / +3.4 / +13.0 / -9.4 / +8.0 | +16.0 / +9.8 / +14.4 / -1.8 / +15.9 | +13.1 / +14.1 / +13.4 / +4.0 / +13.1 |
| Oboe 1 | +7.9 / -6.0 / -8.9 / +14.1 / +8.0 | +12.7 / +5.1 / +5.5 / +20.9 / +12.8 | +23.5 / +13.9 / +13.3 / +30.4 / +20.9 |
| Clarinet 2 | -5.1 / +7.7 / +3.3 / +14.8 / -4.9 | +1.8 / +23.0 / +10.0 / +22.3 / +16.6 | +26.1 / +30.8 / +30.9 / +24.1 / +12.3 |

- Legato joins (old note against the lowest 10 ms in the first 60 ms): unchanged within 0.5 dB on all four (one improved).
- The slurred eighth's peak fell 0-2.4 dB net of the global -3 dB on Oboe 1 / Clarinet 2 / Flute 2 except Flute 2 344 and
  Flute 1 318 (-5 dB): A's "within 1 dB" is not met everywhere. Much of the old "peak" was the trail ringing into the staccato.
- Accents P0 -> P1 (312-362): Violins I first 100 ms vs neighbours -1.7 -> -0.2, front-body -0.7 -> +0.6, peak 0.34 -> 0.18 s;
  Violins II -4.6 -> -3.6, peak 0.27 -> 0.23 s; cor anglais -3.5 -> -2.7, peak 0.24 -> 0.19 s.
- Summit, strings sum: 10 ms peak +0.52 -> +0.12 s after 1005 (Violins I +0.08, Violins II +0.13 s); step over 1004-1005 +4.3 /
  +4.3 dB (unchanged).

## Full render: measured

### Figure, first check (`records/fig25.txt`, `fig26w.txt`, `fig24_old.txt`)
- Woodwinds, every slur-to-staccato pair 300-960, A's +70 ms measure (median / under +3 / worst), c25 -> c26:
  Flute 1 -5.3 / 13 of 15 / -17.1 -> **+8.5 / 4 / -3.9**; Flute 2 +0.2 / 8 of 12 / -10.0 -> **+12.5 / 4 / -6.9**;
  Oboe 1 +8.1 / 4 of 14 / -11.6 -> **+17.6 / 0 / +10.6**; Clarinet 2 +3.8 / 5 of 13 / -4.9 -> **+18.9 / 0 / +6.1**.
  Still under +3: Flute 1 348 (-0.7; B column +7.2), 924, 933, 948; Flute 2 312, 912 (downbeats, not the figure), 924, 933
  (924 / 933 are outside the rule's spans' figure: slur ends on Sus rows).
- Strings (pitch-resolved): Violins I every occurrence within 0.6 dB of c25 (bar 23 18.1 / 4.4 / 8.3 / 9.1). Violins II within
  0.1 except the B -> C at bar 115 17.2 -> 16.0 and bar 315 17.3 -> 14.3 (-3.0; still 14 dB).

### Guard (`records/guard_c25.txt`, `guard_c26.txt`)
| | c25 | c26 |
|---|---|---|
| step 1.5 dB / 0.5 s at > 6 dB/s | 9 (+14 harp) | **0** (+14 harp) |
| first 0.35 s 1.5 dB | 9 (+6 harp) | **0** (+6 harp) |
| B's 2 dB / 20 dB/s | 0 | 0 |
| steps inside printed hairpins (exempt) | 18 | 0 |

The harp stays in the envelope (its notes ring; not counted, as before).

### CC7 moves of 1 dB or more inside notes (`records/cc7moves_c25.txt`, `cc7moves_c26.txt`)
- c25 284 (263 in printed hairpins, 21 outside) -> **c26 535 (383 in hairpins, 152 outside)**.
- The 152 are the envelope moves stretch_cc7 moved before the hall: role edges, hold releases and the note_slew ramps that
  were already in the c25 envelope at up to 4 dB/s (the c25 guard counted only those over 6 dB/s). Median 1.7 dB, p90 4.0,
  largest 6.3 (contrabassoon 315; Clarinet 2 84 6.0, Bassoon 2 635 5.8, Violins II 420 5.6); Bassoon 1 17, Bassoon 2 14, Violins II 11, Horn 3 10. None is a
  note-by-note pattern: they are passage edges with the c25 shape. The level heard is the same as c25's.

### Summit (`summit26.py` on the master and the mp3)
| | c25 master | c26 master | c25 mp3 | c26 mp3 |
|---|---|---|---|---|
| first 0.5 qn after 1005 over 1004-1005 | +1.0 dB | **+1.8** | +0.8 | +1.0 |
| 10 ms peak after the downbeat | +0.52 s | **+0.18 s** | +0.45 s | +0.39 s |
- Summit lead on the mp3 +0.56 -> **+0.68 LU** over bar 335. C's +3 dB step target is not met.

### Accents (`records/acc2.txt`, against the detached note before; median, peak time)
Violins I -3.2 -> -2.9 (0.25 -> 0.21 s), Violins II -3.2 -> -2.8 (0.27 -> 0.23 s), violas -0.4 -> +0.9 (0.14 -> 0.10 s), cor anglais
-2.3 -> -2.3 (front-body -2.0 -> -1.3), Clarinet 2 -5.4 unchanged, Oboe 1 -2.5 -> -2.9, Flute 1 -0.1 -> -1.9, celli +1.0 -> +2.6.
Over +3: unchanged or one fewer. Dan's median +1..+2 is met by violas and celli only.

### Spiccato (`records/spic.txt`): rerouted notes over neighbours median +1.4 -> **-0.7 dB**, over +3 15 -> 8, over +5 6 -> 2;
F sharp 342 / 942 -30.8 / -30.9 under the accented C -29.4 / -29.6. Separation (`stac.txt`) unchanged within 0.3 dB.

### Envelope table: points 2,683 -> 2,918; per note 0.48 -> 0.52; per second 9.7 -> 10.5 (the stretch-end points).

### Delivery against the shared spec (second delivery, `records/deliver_final.txt`, `order_mp3.txt`)
| | c25 | c26 |
|---|---|---|
| 1. I / TP | -14.0 / -1.3 | **-14.0 LUFS / -1.4 dBTP** |
| 2. summit lead | +0.56 over 335 | **+0.68 over 335** |
| 3. f -> ff | 2.31 | **2.23 LU** |
| 4. p10 short-term | -20.3 | **-20.3** |
| 5. limiter summit / 105-120 / 305-320 / 72 / 300 / final | 3.7 / 1.8 / 1.8 / 0.8 / 0.9 / 0.1 | **3.6** / 1.5 / 1.9 / 1.3 / 1.0 / 0.1 |
| 6. LRA | 10.5 | **10.5** (first delivery 10.4) |
- Climax order on the mp3: summit -7.1, then 105-120 -8.3, bar 300 -8.4, 305-320 -8.5, bar 72 -8.6, bar 304 -8.8.
- Crescendo arrivals: 41 +0.7, 72 +0.6, 105 -0.4, 129 +0.2, 197 +0.7, 209 +1.1, 285 +0.5, 300 +1.1, 304 +0.6, 305 0.0,
  329 +2.3, 336 +0.7.
- Quiet means: intro -17.0, theme A -16.6, fugato -21.3, trio dolce -15.9, Meno pp -19.2 (as c25 within 0.2). The ppp ride cuts
  of C #4 were not adopted (Dan's -14 / inner-lines note).
- Hall: master G.P. drop at +0.3 s 18.9 dB, 20 dB fall 0.33 s, RT60 1.40 / late 1.48 s; mp3 19.0 / 0.35 / 1.42; hall14 17.3 dB,
  t20 0.35, RT60 1.50, returns -12.78 dB re dry. Inside Dan's limit, not drier than c25.

### Timing (`records/timing.txt`): over 25 ms 28 %, over 60 ms 5 % (c25 27 / 5). Celli joins (pcx) +30 ms / 25 % over 60 ms
(c25 +30 / 26 %); Violins I +9, Violins II +8, solo +6 ms.

### Per-bar master against c25 (`records/bars_c26_vs_c25.txt`, after removing the -3.0 dB median)
- Over +1.5: bar 58 +3.9 (celli fugato entry; no data change there besides CC7 moves of identical net level: round robin, as
  bar 58's ±2.9 dB swings in c24).
- Under -1.5: bars 302 -3.9 and 303 -3.4: the sfp < now holds the p (intended; C's target).

## Rejected, deferred, not done
- C #4 (ppp ride cuts -2.5 dB): rejected by the coordinator's note (Dan, 2026-11-17).
- A #4 / item 7b (Violins I STAC_MIN_SOUND_S 0.14 + 220 ms cap): not done (lock time; needs a range test).
- C #5a (Violins I bar 200 re-attack), C #5c (timpani roll 237-240): not done.
- B #1's 2.8 dB/s release rate for Flute 1 / cor anglais 156 / 384: the release keeps its c25 shape (4 dB over 0.45 s), now in
  CC7 before the hall instead of the envelope.
- B #3's rising halves (Clarinet 2 210 / 894, Bassoon 1 1001): now in CC7 too (short stretches), not left as envelope ramps.
- A's acceptance "slurred eighth's peak within 1 dB" not met on Flute 1 318 / Flute 2 344 (-5 dB): adopted anyway for the
  figure's +12..+31 dB.

## Faults still audible (instrument side not found)
- Accents still under their neighbours on Violins I / II, cor anglais, Clarinet 2, Oboe 1 (medians -2.3..-5.4 dB).
- Summit downbeat step +1.8 dB on the master (target +3).
- Celli trio joins +30 ms median.
- Flute 1 / cor anglais fade 4 dB in 0.45 s after the f arrivals at 156 / 384 (now pre-hall).
- Violins II bar 315 B -> C 14.3 dB (c25 17.3).

## Research items
| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; guard 9 / 9 -> **0 / 0** (stretch_cc7) |
| dynamic trims as CC7 (finale 135) | adopted |
| role / passage edges into rests with CC7 (finale 136) | **adopted generically** (every stretch of 16 qn or less) |
| Marcato Sustain on a chord stroke (finale 140) | **adopted** at the summit (Violins I / II, violas) |
| accents by the KS Masters' accent rows | adopted: flutes, Oboe 1; rejected: cor anglais, Clarinet 2, Violins II / violas inside lines |
| shared -14 delivery + room-noise bed | adopted |
| one legato row per string line | adopted (unchanged) |
| per-region / per-row volume and release in the Opus state | adopted (+ woodwind TLeg caps, f trail gain) |
| CC16 resets | adopted on the celli fugato; recorded crescendo rolls pending |
| oboe Main lower than -9 dB | pending (not run) |

MANUAL-GAPS: no gap tried this cycle.
