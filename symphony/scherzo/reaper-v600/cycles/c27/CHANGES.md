# Cycle 27: changes (actor, on the c26 render)

STATUS: **rendered once**, 2026-11-18 08:16-08:23 CST, from a freshly restarted REAPER after a full build of all 31 tracks
(guard 0 stale; memory settled at 44 GB, 0 compressed). Attack probe: late or hole 0. No stem fix.
- mp3: `cycles/c27/scherzo-mockup-c27.mp3`. Data as rendered: `cycles/c27/build_render/`. Records: `cycles/c27/records/`.
- Lock (`phase.log`): taken 07:22 with no other waiter, released 08:27: **65 min** (control ranges, a range-track build, the
  candidate ranges, restart, full build, restart, render, save, rebuild of 6 stale tracks, save, quit).
- REAPER memory: 44 GB settled before the render and **44 GB after it** (0.06 GB compressed); 57 GB during the range pass.
- After the save that followed the render, Bassoon 2, Contrabassoon, Horn 2, Horn 4, Violins I and Violoncellos were stale;
  rebuilt, saved, guard 0 stale (also on the project saved at quit).
- Master -24.2 LUFS, LRA 21.9, true peak -4.1 dBFS, sample peak 0.627; no stem over -1 dBFS.
- Disk: c26's stems deleted (its 00_Master.wav and mp3 kept), my range WAVs deleted; 42 GB free. Backups/ not touched.

## Changes

### Tools (generic, off by default)
- `tools/score_to_parts.py`
  - HP_GAIN_TO_CC11 `hold_until_mark_qn` / `hold_rest_extra_qn` (B #1): a crescendo gain left in the envelope holds as a passage
    level until a printed decrescendo start or softer mark (released there), a louder mark (shrinks by that mark's CC11 rise x
    db_per_unit, then holds on), the first rest of 0.5 qn (released in it) or the cap; at the cap a rest of 0.25 qn within M qn
    takes the release, otherwise a step at the next re-attack (no note sounding across its moved note-on).
  - ACCENT_CC `marc_lift` {cc, s, rows, max_cc, vel_max} (A #1): CC11 rise after a soft marcato-overlay accent, held to the next
    moved note-on.
  - `SOFT_LEG_HEAD_CC` (C #3, finale technique 139): CC11 + add from pre_s before a soft legato head's moved note-on (after a
    rest), held to hold_s, gone by gone_s; keys rows, max_cc, rest_qn, spans, skip. Skips a window / split track's first note
    of its window (its lane follows the source part before it: the first build wrote CC11 112-117 10 ms before the solo
    violin's 51).
  - `UNI_BOOST_ROLE_IN_RESTS` (B #4.1): the unison-boost span rises before the run's first moved note-on and falls in a rest
    within 6 qn after the run, otherwise as a step at the next note's moved note-on.
- `tools/build_reaper.py`
  - `cresc_trim_hold` keys `release_at: "mark"`, `max_hold_qn`, `rest_extra_qn` (B #1): the held trim stays to the next printed
    change after the arrival (cap 8 qn), then is released in a rest within 4 qn or as a 25 ms step at the next re-attack;
    positions go through the CC7 moved-time warp (without it the violas' step landed 0.45 qn early, inside note 632).
  - `note_slew` key `onset_step_s` (B #3): at a re-attack join (previous note ends within 0.03 s before the note-on, nothing
    sounding across it) a written move within onset_step_s stays a step 0.02 s before the note-on.
  - `region_gain_db` spec key `vel_min` (A #4).

### Data (`build/score_config.py` c27 block; `actor_scripts/apply27.py MARC=6` writes roles / mix / entry_leads from `before/`)
1. Arrival fades (B #1-#4): `hold_until_mark_qn` 8 + `hold_rest_extra_qn` 4 on every HP_GAIN_TO_CC11 entry with keep_rel_db_s;
   mix.json `cresc_trim_hold` release_at mark, max_hold_qn 8, rest_extra_qn 4 (B proposed 16 qn: the trio climax celli then
   held +5.4 dB for 13 qn and the cap release still fell inside notes); `note_slew` onset_step_s 0.03, skip_hairpins true;
   UNI_BOOST_ROLE_IN_RESTS on. Coda: Clarinet 2 / Bassoon 1 fff = ff (+1.2 / +4.0 dB); the six woodwind summit rows start at
   984 (contrabassoon 987).
2. Violins I soft heads (A #1): "Sus Marc LITE" vel<66 -4 -> **-6** dB (range-tested -8: overshoot), marc_lift cc 14,
   s (0.10, 0.22) on the nine heads (exactly 39, 51, 69, 75, 285, 759, 771, 789, 795). Eighths at v62 not tried.
3. Accents (C #1, A #2, A #3): no ROW_CHANGE_ACC_ADD_S on Violins I; cor anglais entry_leads back to {900: 0.06}; Clarinet 2
   add_loud 0 -> 8, lead_s 0.06; violas add_loud 20 -> 14.
4. Tutti downbeats (C #2): body_s (0.22, 0.36) -> (0.14, 0.24) on Violins I / II, violas, cor anglais, Clarinet 2, Oboe 1;
   violas' off-beat staccatissimo double stops in 312-359 / 912-959 v95 -> v82 (not the six slurred-pair onsets).
5. Soft legato heads (C #3): SOFT_LEG_HEAD_CC on the strings, spans 456-720 and 1020-1128 (celli skip 564).
6. Smaller: celli RR_RESET_AT 273 / 282 / 291 -> 270 / 279 / 288 (C #4, re-derived from the range test); Violins I Spiccato
   F sharp 5 v90+ regions -3 dB (A #4).

Opus state changes (full rebuild): Violins I (region gains); every track was built in full before the render anyway.

## Range tests (control P0 = c26 project, P1 = candidate on 8 tracks, same starts; WAVs deleted, `records/range_P0.txt`, `range_P1.txt`)
| measure | P0 | P1 | decision |
|---|---|---|---|
| soft heads (median of 8): first 100 ms over ±2 qn neighbours | +3.0 / +1.6 | -2.1 / -3.2 | vel<66 -8 overshoots: **-6** adopted |
| heads 2-5 kHz front over neighbours' fronts | +7.3 / +4.6 | +2.5 / -0.1 | |
| heads hole 0.21-0.39 s (mean; lowest 30 ms) | -7.2 / -13.1 | -7.1 / -11.6 | lift +14 barely helps (kept) |
| bar 23 / 263 figure 83->84 | 9.2 / 20.3 | 13.3 / 22.8 | better |
| violas beats 2-3 (312-360) | -31.9 dB | -37.1 dB | -5.2 dB, a layer step; adopted (basses' downbeat -34.4) |
| celli RR, samples after a reset | -48.4 / -45.8 / -49.9 | (same order) | reset one bar before the heads |
| basses RR heads 273 / 282 / 291 (C's resets) | -48.7 / -48.6 / -47.3 | -49.1 / -49.0 / -48.6 | not adopted |
| soft legato heads, -6 dB point (11 heads, median) | +213 ms | +131 ms | adopted; celli 564 (not late) +5.1 dB peak: skipped |
| Flute 2 slur end 20 ms: figure A median / under +3 | +13.1 / 1 | +11.6 / 2 | **not adopted** (Dan's figure first) |

## Full render: measured (c26 -> c27)

### Figure, first check (`records/fig25.txt`, `fig27w.txt`)
- Strings, every occurrence (pitch-resolved, A's crossover): Violins I bar 23 18.1 / 4.4 / 8.3 / 9.1 -> 18.1 / 4.4 / 8.7 / **12.4**;
  bar 115 last step 9.0 -> 10.8; bar 117 76->79 10.8 -> 14.6; bar 315 9.0 -> 10.1, 317 10.7 -> 14.5; bar 263 21.1 -> 21.8; every other
  value within 0.3 dB except bar 110 / 310 79->78 4.5 / 3.7 -> 2.8 / 2.5. Violins II identical within 0.3 dB.
- Woodwinds (A's +70 ms measure, median / under +3 / worst): Flute 1 +8.5 / 4 / -3.9 -> **+9.3 / 4 / -3.9**; Flute 2 +12.5 / 4 / -6.9 ->
  **+12.3 / 4 / -3.2**; Oboe 1 +17.6 / 0 / +10.6 -> **+16.5 / 0 / +10.6**; Clarinet 2 +18.9 / 0 / +6.1 -> **+22.0 / 0 / +6.3**.
  The c26 woodwind state is unchanged.

### Guard and net in-note moves (`records/guard_c26.txt`, `guard_c27.txt`, `netmoves_c26.txt`, `netmoves_c27.txt`)
| | c26 | c27 |
|---|---|---|
| step 1.5 dB / 0.5 s at > 6 dB/s | 0 (+14 harp) | 1 (celli 524, 1.6 dB at +0.12 s) (+14 harp) |
| first 0.35 s 1.5 dB | 0 | 2 (celli 526 / 624: steps at the note-on, 2.5 dB) |
| B's 2 dB / 20 dB/s | 0 | 0 |
| net moves 1 dB+ inside note bodies (envelope + CC7, 60 ms after the note-on to 25 ms before the next) | 400 (330 in hairpins, **70 outside**) | 398 (350 in hairpins, **48 outside**) |
- Gone: Violins I 1012, Bassoon 1 156 / 162, Bassoon 2 626, celli 626, contrabassoon 993, Horn 3 950 / 957, Violas div 1044 (B #4.3:
  gone with the new trim-hold release; its source was not traced further), the 996 woodwind falls.
- Left outside hairpins (48): mostly 1.0-1.4 dB; larger: the final fades (Horn 1 1101, Violins I 1111, solo 1120; as in c26), harp 238, celli 632 2.2, Violas div 632 2.2, Violas 632 3.1 (trio climax: the cap release at a
  re-attack inside a dotted note), Horn 4 915 / 918 1.3-1.4.
- Coda net levels 993.5 -> 1005.5 (dB): Clarinet 2 4.3 / 3.8 / 0.9 / 0.7 / 4.4 -> 1.8 / 4.4 / 4.4 / 4.8 / 7.7; Bassoon 1 4.1 / 2.7 /
  1.0 / 0.5 / 3.7 -> 1.8 / 3.0 / 3.0 / 4.0 / 7.6: no fall at bar 333, a rise through the crescendo.

### Arrival fades: B's examples now hold: Bassoon 1 156 (6.3 dB held to 165.5, the 3 dB uni-role step at 161.8 gone), celli 626,
contrabassoon 993 (-3.7 -> -2.4 dB over 996-1001, slower), Horn 4 912 (+2 dB hpgain held to the 922.8 rest; the +3 unison boost
ends at the next note-on 914.7).

### Summit (`summit27.py`, mp3 `order_mp3.txt`)
- Stem sum: first 0.5 qn after 1005 over 1004-1005 +1.8 -> **+1.4 dB** (the woodwind bass now grows into 1004); 10 ms peak +0.18 s.
- mp3: summit lead over bar 335 +0.68 -> **+0.57 LU**; summit over the next loudest passage +1.3 -> +1.2 LU.

### Tutti downbeat weight (`records/acc_down.txt`, downbeat 10 ms peak minus beats 2-3)
Master 312-360 +0.3 -> **0.0**, 912-960 +0.7 -> +0.9, theme A 36-84 +2.4 -> +2.3. Violins I -0.7, Violins II +0.7, cor anglais -0.2.
Violas' beats 2-3 -31.9 -> -37.1 dB (basses' downbeat -34.5). C's +2 dB target is not met: the body dip and the violas' cut do
not make a downbeat.

### Accents
- A's measure (first 100 ms over the unaccented notes within ±2 qn, 299-362 / 899-962): Violins I +0.1 / -1.4 -> -1.2 / -1.5;
  Violins II -1.3 / -1.3 -> -1.4 / -1.3; cor anglais +0.9 / +0.2 -> -1.4 / -1.8; Clarinet 2 -1.2 / -1.3 -> -0.6 / -1.0; Oboe 1
  -0.4 / -1.0 -> -1.0 / -1.0. The fronts lost 1-2 dB where the lead went (the window starts at the beat).
- Onset (-6 dB point of the note's peak, from the beat): Violins I tutti +8 -> +33 ms (299-362), cor anglais -55 -> -12 ms.
- acc2 (against the detached note before, `acc2.txt`): Violins I -2.9 -> -3.1 (over +3: 2 -> 0, peak 0.21 -> 0.18 s), violas +0.9
  -> -0.3, Clarinet 2 -5.4 -> -4.0 (peak 0.28 -> 0.27 s), cor anglais -2.3 -> -3.0 (peak 0.22 -> 0.18 s), celli +2.6 -> +1.2.
- Soft heads (9, full render): first 100 ms over neighbours +2.1 -> **-0.9**, 2-5 kHz front +6.3 -> **+3.3**, hole -7.2 -> -5.8, lowest
  30 ms -12.9 -> -10.7, peak 0.15 -> 0.19 s (the marcato spike is lower; the sustain now peaks later).
- Spiccato (`spic.txt`): rerouted notes over neighbours median -0.7 -> -0.9, over +3 8 -> 5, over +5 2 -> 1; F sharp 342 / 942
  -30.8 / -30.9 -> -33.8 / -33.9 dB, but the accented C at 345 / 945 fell more (-29.4 -> -34.6, its lead is gone): the F sharp
  is now 0.8 dB over it.

### Soft legato heads (full render, -6 dB point): Violins I 528 / 576 / 603 +233 / +296 / +186 -> **+128 / +191 / +141 ms**;
Violins II 708 / 1068 +150 / +208 -> +130 / +128; violas 708 / 1020 +260 / +215 -> +210 / -20; celli 504 / 1071 +93 / +244 -> +58 /
+149. Peaks within 1.2 dB.

### Ritmo di tre battute (celli): heads 273 / 282 / 291 -48.4 / -48.5 / -47.2 -> **-45.9 / -46.1 / -45.5 dB**, +3.3 dB over the
two bars after each (264 stays on the first sample, -48.1).

### Envelope table (guard27): points 2,918 -> 2,808; per note 0.52 -> 0.50; per second 10.5 -> 10.1.

### Delivery against the shared spec (`records/deliver.txt`, `order_mp3.txt`)
| | c26 | c27 |
|---|---|---|
| 1. I / TP | -14.0 / -1.4 | **-14.0 LUFS / -1.4 dBTP** |
| 2. summit lead | +0.68 over 335 | **+0.57 over 335** |
| 3. f -> ff | 2.23 | **2.10 LU** |
| 4. p10 short-term | -20.3 | **-20.4** |
| 5. limiter (whole file) | 3.6 | **3.3** |
| 6. LRA | 10.5 | **10.6** |
- Climax order on the mp3: summit -7.2, then 305-320 -8.4, 104 / 105-120 -8.5, bar 304 -8.5, bar 300 -8.6, bar 72 -8.7.
- Crescendo arrivals: 41 +0.9, 72 +0.5, 105 -0.5, 129 +0.1, 197 +0.7, 209 +1.2, 285 +0.6, 300 +1.0, 304 +0.9, 305 -0.4, 329 +2.5, 336 +0.6.
- Quiet means: intro -17.0, theme A -16.9, fugato -22.3 (-21.3), trio dolce -15.8, Meno pp -19.1.
- Hall: master G.P. drop at +0.3 s 18.1 dB, 20 dB fall 0.33 s, RT60 1.42 / fitted 1.44 / late 1.48 s; mp3 17.2 / 0.34 / 1.44-1.49 s;
  soft ends 0.06-0.19 s. Inside Dan's limit, not drier than c26.

### Timing (`timing.txt`, `pcx.txt`): over 25 ms 26 % (c26 28 %), over 60 ms 5 %. Celli joins pcx +27 ms (c26 +30); Violins I +10,
Violins II +8, solo +4 ms.

### Per-bar master against c26 (`bars_c27_vs_c26.txt`, median difference 0.0)
Over +1.5: bars 56 +1.6, 192 +1.6, 210 / 211 +1.9 (crescendo holds before bar 72; the celli fugato bar 192). Under -1.5: bar 58
-3.9 (celli fugato entry: the round robin that swung +3.9 in c26 swung back; no data change there).

## Rejected, deferred, not done
- Flute 2 slur end 20 ms (C): range test worse on Dan's figure (above).
- Basses' RR resets (C #4): no gain in the range test.
- B's 16 qn hold: replaced by 8 qn + rest / re-attack release (celli +5.4 dB for 13 qn at the trio climax with 16).
- Violins I eighths at v62 (A #1c), Violins I staccato ring test (A #5): not run (lock time).
- C #5: celli leg_leads not refitted (frozen, as C asked).
- C's trio Clarinet 1 lead +0.015 s: not done (small).

## Faults still audible (instrument side not found)
- Soft heads' hole behind the marcato (lowest 30 ms -10.7 dB) and their late body peak (0.19 s).
- Tutti downbeats no heavier than beats 2-3 on the master (0.0 / +0.9 dB).
- Accent fronts under their neighbours (-0.6..-1.8 dB on A's measure) now that they start on time.
- Summit step +1.4 dB (target +3); summit lead +0.57 LU.
- Violins I's accented C at 345 / 945 now 0.8 dB under the Spiccato F sharp before it.
- Trio climax 632: a 2-3 dB cap release at a re-attack inside dotted notes (violas, celli, Violas div).

## Research items
| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; net in-note moves outside hairpins 70 -> 48 |
| dynamic trims as CC7 (finale 135), role edges into rests (136) | adopted (unchanged); trim holds now released in rests / at re-attacks |
| soft legato heads CC11 front (finale 139) | **adopted** (11 heads, -6 dB point median 213 -> 131 ms) |
| Marcato Sustain on a chord stroke (finale 140) | adopted (unchanged) |
| accents by the KS Masters' accent rows | adopted: flutes, Oboe 1; marcato layer of Sus Marc LITE cut -6 |
| CC16 resets | adopted; now placed for level on the celli pizzicato |
| shared -14 delivery + room-noise bed | adopted |
| oboe Main lower than -9 dB | pending (not run) |

MANUAL-GAPS: #12 (round-robin reset) used for level; recorded there.
