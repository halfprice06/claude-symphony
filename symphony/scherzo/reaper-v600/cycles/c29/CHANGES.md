# Cycle 29: changes (actor, on the c28 render)

STATUS: **rendered once in two passes**, 2026-11-18. Main pass 12:38-12:48 CST from a freshly restarted REAPER after a
full build of all 31 main tracks (guard 0 stale, memory settled at 44 GB, 0 compressed); second pass 12:53-13:02 (the
felt timpani alias alone in `scherzo-v600-mockup-pass2.rpp`, 1.2 GB). Attack probe: late or hole 0. No stem fix.
- mp3: `cycles/c29/scherzo-mockup-c29.mp3`. Data as rendered: `cycles/c29/build_render/`. Records: `cycles/c29/records/`.
- Lock (`phase.log`): taken 11:43 (after the finale's c29 actor released it; no other waiter), released 13:05: **82 min**
  (open + settle 10 min, control ranges, P1 build, restart, P1 ranges, P2 build, restart, P2 ranges, full build,
  restart, main render, guard, pass-2 open / build / restart / render, save, guard, quit).
- REAPER memory: **44 GB after the main render** (0 compressed); pass-2 project 1.2 GB.
- Master -23.9 LUFS, LRA 21.4, true peak -3.1 dBFS, sample peak 0.702 (float sum of 36 stems).
- Disk: c28's stems and returns deleted (00_Master.wav and mp3 kept); my range WAVs deleted; 35 GB free. `Backups/` not
  touched (the coordinator's note: that deletion was refused before).

## Changes

### Tools
- `tools/deliver_master.py`: TOP_ABOVE -6 -> **-3** (critic B #3; scherzo comment with B's simulation).
- No other tool change. The second render pass (`ALIAS_TRACKS` / `PASS2_TRACKS`, `build_reaper.py --pass2`,
  `render_cycle.py --pass2`, ported from Movement I in c00) is used for the first time here; README updated.
- Actor scripts `cycles/c29/actor_scripts/`: `apply29.py` (roles / mix / lead_set from `before/`), `gate29.py` (finale
  technique 144 net-level gate), `snap29.py` (technique 145 check), `h3.py`, `trio29.py`, `vla29.py`, `ten29.py gdown|lev`,
  `fig29w.py` (A #3: harmonics 1-3 column and gate), the c28 scripts renamed.

### Data (`build/score_config.py` c29 block; `apply29.py HN3G=-3.4 HN3P68=8.5`)
1. **Delivery f -> ff** (B #3): TOP_ABOVE -3; coda ride row `[(990,0),(993,-2),(996,-4),(1002,-5),(1004.6,-5.5),(1005.1,0)]`;
   Violins I theme A +1.5 dB as a roles.json passage row [35.6, 84, +1.5] (as CC7 the build warned of the 127 cap on 19
   more points: B's fallback, edges in the rests before 35.80 and after 81.30).
2. **Trio climax** (B #1): celli role [623.6, 648] -1.5 -> -3.5; Violas and Violas div [624.4, 648.5, -3.0].
3. **Timpani sticks** (A #1, C #3): alias "Timpani soft" on Timpani Flt KS, windows 435-864 and 1020-1128, pass 2;
   `TRACK_WINDOWS["Timpani"]` rests the main (hard-stick) track there; mix.json "Timpani soft" = c27's felt Timpani entry
   (no hard-stick region gains), added to `soft_trim_db._except` and `note_slew.skip_tracks`. Medium sticks (672-864)
   on felt without a range test: felt -27.8 / hard -18.4 dB 1-5 kHz share (c18 / c28 full renders) against A's -24.
   Alias check: notes, CC1, vol_db and keyswitches equal to the source's inside the windows (rows Hrd -> Flt); CC7 one
   extra start point (443.98, 67, the value already in force).
4. **Horn 3** (C #1): Stereo routing (`channel_map` 0, written explicitly), Horn 1's mics (Close -1.4 / Main -5.2), pan
   -0.18; gain -3.4 dB and G sharp 4 region gain 3.5 -> 8.5 dB from the range test (Stereo was +3.4 dB in 312-360 and
   +3.8 at the recall but -2.9..-3.7 dB on the G sharp 4, the only pitch at 1026 / 1092).
5. **Celli countermelody heads 312 / 912** (B #2): ART_SPANS "Sus MAX"; lead_set 312 / 912 deleted; the head then had
   no lead at all (it follows the B2's written end), so `REATTACK_LEAD_AT` 0.06 s; the B2 ends 0.02 qn before it.
6. **Tutti tenutos** (A #2, B #4): NOTE_END_AT q + 0.85 on trombones, bass trombone, tuba, Horns 1-2, contrabassoon,
   basses (312-360; contrabassoon, basses, Horns 1-2 also 912-960), 15-16 notes each, every next onset 3 qn away.
7. Item 7 (1005 woodwinds, oboe Main mic): not done (time; see Open).

Opus state changes (full rebuild): Horn 3 (routing, mics); range-only: brass / horns (Sus Accent MAX), basses (Marc
Sus LITE) - reverted, rebuilt. New instance: Timpani soft (pass 2). Every main track was built in full before the render.

## Range tests (312-360 start 155.4, relay 1016-1106; same starts; restart between; `records/range_P0/P1/P2.txt`)
| measure | P0 (c28) | P1: a) end q+0.85, violas v88, Horn 3 Stereo | P2: a) + b) Sus Accent v70 + c) basses Marc LITE v80 + violas v92 |
|---|---|---|---|
| tenuto group downbeat over beats 2-3 | +2.0 dB | **+3.9** | +0.5 |
| master (range) | +0.1 | +0.5 | -0.1 |
| trombone 1 peak / -6 dB / 2-5k front-body | +168 / +25 ms / -4.5 | same | +195 / +90 ms / -12.3 |
| tuba | +165 / +30 / -6.4 | same | +183 / +70 / -17.6 |
| basses | +170 / -20 / -1.8, -38.4 dB | +128 / -20 / -1.8, -38.9 | +180 / -8 / -0.2, **-34.8** |
| track levels | | -0.3..-0.8 dB | brass -1.3..-3.4 dB |
| violas off-beat ff shorts (first 150 ms) | -41.2 | -40.7 (v88) | -35.4 (v92; 1 dB over the basses' downbeat) |
| Horn 3 corr 312-360 / G sharp 1092 300-1k corr / mono loss | 0.99 / +1.00 / -0.2 | 0.97 / **+0.58 / -1.3** | |
Decisions: a) adopted; b), c) rejected (later, darker swell; basses later and +4 dB); violas v88 (no layer step) and v92
(fails B's own gate) rejected, c27's v82 kept; Horn 3 Stereo adopted with the gain refit.

## Full render: measured (c28 -> c29)

### Figure, first check (`records/fig25.txt`, `fig29w.txt`)
- Violins I / II: all 111 steps at every occurrence within 1.0 dB of c28 (bar 23 78->79 17.1, 79->81 5.6; bars 110 / 310
  79->78 3.7 / 4.3; bars 115 / 315 13.3 / 13.5).
- Woodwinds, gate (A13 on leaps of 5+ semitones, else A, +70 ms): Flute 1 median +14.7, under +3 **0**, worst +9.3;
  Flute 2 +15.8 / 0 / +7.0; Oboe 1 +20.2 / 0 / +10.6; Clarinet 2 +23.4 / 0 / +6.3 (c28 on the same gate: 0 under +3 on
  all four). The old harmonics 2-5 column still reads Flute 2 948-type leaps at -6.9 (round robin). Solved; c26 state kept.

### Guard, net in-note moves, gates (`records/guard_render.txt`, `netmoves_build.txt`, `gate_build.txt`, `snap.txt`)
| | c28 | c29 |
|---|---|---|
| step 1.5 dB / 0.5 s at > 6 dB/s | 1 (celli 524) (+14 harp) | 1 (same) (+14 harp) |
| first 0.35 s 1.5 dB | 2 (celli 526 / 624) | 2 (same; celli 624 2.5 -> 3.5 dB: the deeper trio role edge at its arrival) |
| B's 2 dB / 20 dB/s | 0 | 0 |
| net moves 1 dB+ in note bodies, outside hairpins | 34 | 32 (celli 312 / 912 gone; celli 317 / 917 1.5 dB slow ramps now cross 1 dB) |
- Net-level gate against c28 (1 qn spans, 1.5 dB): only the intended spans - Horn 3 -3.4 dB everywhere (gain against
  the routing's +3.4), Violins I 35-82 +1.5, violas / Violas div 624-648 -3.0, celli 624-651 -2.9.
- Technique 145 check: 33 notes with a CC7 change of 1.5 dB+ in their first 50 ms - the same 33 as in c28 (none new);
  listed in `records/snap.txt` for c30 (e.g. coda 993 brass -1.7..-2.5, 1005 strings +2..+3.9, 900 sfp winds).
- Envelope: points 2,547 -> 2,540, per note 0.46, per second 9.1.

### Trio climax (`records/trio_heads.txt`, 300 Hz-5 kHz)
| bar | 212 | 213 | 214 | 215 | 216 |
|---|---|---|---|---|---|
| celli minus Violins I, c28 -> c29 | -3.4 -> **-5.4** | -2.7 -> -4.7 | +0.8 -> **-1.2** | 0.0 -> -2.0 | -1.6 -> -3.9 |
| tune minus celli + Bsn 2 | +4.2 -> +5.2 | +4.2 -> +5.2 | +2.9 -> +4.0 | +2.5 -> +3.8 | +2.5 -> +3.3 |
| tune minus celli alone (c29) | +9.4 | +8.4 | +7.1 | +6.2 | +8.8 |
| tune minus violas | +7.9 -> +10.9 | +10.4 -> +13.7 | +4.6 -> +8.5 | +2.5 -> +6.3 | +10.4 -> +13.4 |
| master | -32.0 -> -32.3 | -33.0 -> -33.5 | -33.1 -> -33.6 | -34.0 -> -34.8 | -33.7 -> -33.7 |
Violins I alone over the celli in every bar 212-216; the tune leads the celli by 6.2 dB or more in 213-216 (target 5);
master plateau 209-216 within 2.5 dB (212 -> 215 fall 2.5 dB, c28 2.0 dB on this measure: 0.5 dB more sag). Bar 217 (crescendo) celli -1.8 dB.

### Timpani sticks by passage (`records/timp.txt`; 1-5 kHz share of the first 50 ms, stroke peak; c18 levels +3 dB global)
| passage (printed sticks) | c18 felt | c28 hard | **c29** |
|---|---|---|---|
| 0-435 (hard) | -19.3 / -31.0 | -16.7 / -35.1 | -16.7 / -35.1 |
| 435-672 (soft) | -35.4 / -52.1 | -21.2 / -53.6 | **-35.3 / -54.9** |
| 672-864 (medium, on felt) | -27.8 / -46.5 | -18.4 / -48.5 | **-27.8 / -49.5** |
| 864-1020 (hard) | -17.6 / -27.6 | -15.2 / -30.5 | -15.2 / -30.5 |
| 1020-1128 (soft) | -29.0 / -50.4 | -19.4 / -53.9 | **-29.3 / -52.0** |
Rolls 612 -45.4 (c28 -44.6), 708 -53.8 (-52.8), 852 -44.9 (-45.0); Allegro strokes and rolls identical. Coda soft
strokes 1.9 dB louder than c28 (A's 1.5 dB limit; still 1.6 dB under c18's felt level): open for c30 (alias region gain).

### Horn 3 (`records/` via h3.py on the full render)
| span | corr | L-R | harmonics 3-8 / 1-2 | level c28 -> c29 |
|---|---|---|---|---|
| Horn 1 1083-1092 | 0.68 | +1.0 | -8.3 | |
| Horn 3 1094-1097 (relay) | 1.00 -> **0.74** | +4.1 -> **+1.9** | -14.9 -> **-9.0** | -48.5 -> -49.8 |
| Horn 3 1097.5-1100.5 | 1.00 -> 0.87 | +4.1 -> +0.2 | -12.9 -> -9.9 | -50.7 -> -51.0 |
| Horn 1 1103-1110 | 0.80 | +1.1 | -10.0 | |
| Horn 3 312-360 / 456-504 / 1020-1032 | 0.99 / 1.00 / 1.00 -> 0.97 / 0.95 / 0.97 | | | -34.2 / -55.6 / -44.1 -> -34.2 / -57.0 / -43.3 |
G sharp 4 at 1092: 300-1000 Hz corr +0.58, mono loss 1.3 dB (no cancellation). The relay now matches Horn 1 in width and
colour within 1-2 dB. The countermelody (312-360) stays near mono at 0.97 (C's 0.80-0.95 window not met; stereo_double
not tried). Per-bar master: bar 365 -1.7 dB (the relay's G sharp), bar 342 +1.5 (recall).

### Celli countermelody heads (`records/trio_heads.txt`)
Head 312-315 / 912-915 against 318-321 / 918-921: gap 6.0 / 6.0 -> **5.3 / 5.7 dB** (target 2-3). The Sus head did not
lift the line's first bar; c18's 2 dB came from an envelope ramp Dan's rule removed. Open.

### Tutti downbeat weight (`records/extra.txt`; downbeat 10 ms peak minus beats 2-3)
- Tenuto group sum: 312-360 +2.3 -> **+4.4 dB**; 912-960 (4 tracks) +1.7 -> **+3.9**.
- Master / mp3: 312-360 -0.3 / -0.1 -> **+0.3 / +0.3**; 912-960 +1.2 / +0.7 -> +1.0 / +0.5; theme A +2.8 / +2.4.
  The +1.5 dB mp3 target is not met: the tenuto group is not what fills beats 2-3 on the master (strings and woodwinds).

### Accents (`records/acc2.txt`, against the detached note before)
Strings unchanged (Violins I -3.8, Violins II -2.3, violas +0.2, celli +0.8; no data change). Woodwinds moved with round
robins only (Flute 2 -2.5 -> -0.9, Clarinet 2 -4.7 -> -3.2). No track's median over +3; still under Dan's +1..+2 for
the violins.

### Delivery against the shared spec (`records/spec_final.txt`, metrics.md)
| | c28 | **c29** |
|---|---|---|
| 1. I / TP | -14.0 / -1.4 | **-14.1 LUFS / -1.2 dBTP** |
| 2. summit lead | +0.67 over 335 | **+0.60 over bar 318** (305-320 tutti -8.2 -> -8.0) |
| 3. f -> ff | 1.88 | **2.23 LU** (met) |
| 4. p10 short-term | -20.6 | **-21.0** |
| 5. limiter (summit) | 3.7 | **3.9** (tuttis 1.7-1.8) |
| 6. LRA | 10.9 | **11.4** |
- Climax order on the mp3: summit -7.4, 305-320 -8.0, 105-120 -8.3, bar 300 -8.3, bar 72 -8.8, bar 304 -8.9.
- Crescendo arrivals: 41 +1.8, 72 +0.5, 105 -0.5 (still reversed), 129 +0.3, 197 +0.6, 209 +1.1, 285 +0.6, 300 +1.2, 304
  +0.9, 305 +0.3, 329 +3.1, 336 +0.7.
- Quiet means: intro -17.4, theme A **-16.8** (c28 -17.3), counterstatement -19.1, fugato -22.1, trio dolce -16.3, Meno pp -19.6.
- Hall: master G.P. drop at +0.3 s 18.7 dB, 20 dB fall 0.33 s, RT60 1.42 / fitted 1.45 / late 1.46 s; mp3 17.8 dB / 0.36 s
  / 1.40-1.50 s; soft ends 0.06-0.19 s; returns re dry -12.8 dB. Inside Dan's limit.
- Master sample peak 0.702 (-3.1 dBFS); no clipping.

### Timing (`timing.txt`, `pcx.txt`): over 25 ms 26 %, over 60 ms 5 %; celli joins +29 ms, Violins I +9, II +6 (unchanged).

### Per-bar master against c28 (`bars_c29_vs_c28.txt`, median 0.0)
Over +1.5: bar 342 +1.5 (Horn 3 recall, Stereo). Under -1.5: bar 365 -1.7 (Horn 3's G sharp in the relay). No other bar
moved 1.5 dB; the trio climax bars 212-216 -0.3..-0.8 dB.

## Rejected, deferred, not done
- A #2 b) brass "Sus Accent MAX" v70 and c) basses "Marc Sus LITE" v80 (range test above); B #4 violas v88 / v92.
- C #2 (celli drop_always 624 + trim skip): the coordinator chose B's roles; C's targets met by the role change.
- A's ppp near-the-rim velocities (v52 / v44) on felt, the coda soft strokes' -1.9 dB, Horn 3 stereo_double: not tried.
- Item 7: Clarinet 1 / 2 and Bassoon 2 in-note moves at 1005 (1.1-1.2 dB; source not traced), oboe / cor anglais Main
  mic (C #4): not done (lock time went to the pass-2 render).
- Pre-existing score_to_parts WARN (celli early fills 582 / 600 / 780 ramp inside led legato transitions; also in c28):
  not fixed.

## Faults still audible (instrument side not found)
- Tutti downbeats only +0.3 / +0.5 dB on the mp3 (the tenuto group itself +4.4).
- Celli countermelody head 5.3-5.7 dB under its second bar.
- Summit lead +0.60 LU (over the 305-320 tutti); arrival 105 reversed (-0.5).
- Accent fronts under their neighbours on the violins.
- 33 notes with a 1.5 dB+ CC7 change in their first 50 ms (pre-existing; `records/snap.txt`).

## Research items
| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; net in-note moves outside hairpins 34 -> 32 |
| dynamic trims as CC7, role edges in rests | adopted; Violins I theme A row edges in rests |
| accents by the KS Masters' accent rows | adopted (unchanged) |
| tenuto quarters on Portato / Marcato Long (c28) / **Sus Accent MAX, Marc Sus LITE (c29)** | **rejected** (range test: +20-30 ms later peaks, -6 dB point +30-65 ms later, 2-5 kHz front -8..-11 dB darker; basses +4 dB) |
| tenuto ends 34 ms before the next beat (manual p.100 portato definition) | **adopted** (tenuto group downbeat +2.3 -> +4.4 dB) |
| timpani hard sticks (MANUAL-GAPS #6) | adopted where printed; **felt alias in pass 2 for soft / medium spans** (1-5 kHz share -35 / -28 / -29 dB) |
| second render pass (Movement I c39) | **adopted** (one instance, 1.2 GB, outside the 45 GB) |
| Mono From Left routing (c18) | **dropped on Horn 3** (relay width / colour, G sharp corr +0.58) |
| CC16 resets | adopted (unchanged) |
| shared -14 delivery + room-noise bed | adopted; TOP_ABOVE -3, coda ride row deeper |
| oboe Main lower than -9 dB | pending (not run) |
