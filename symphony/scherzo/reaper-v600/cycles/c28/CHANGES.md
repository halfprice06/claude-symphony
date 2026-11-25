# Cycle 28: changes (actor, on the c27 render)

STATUS: **rendered once**, 2026-11-18 10:14-10:23 CST, from a freshly restarted REAPER after a full build of all 31 tracks
(guard 0 stale; memory settled at 44 GB, 0 compressed). Attack probe: late or hole 0. No stem fix. The mp3 was delivered a
second time from the same master after a delivery-only change (ride rows moved off two ff arrivals; item 8).
- mp3: `cycles/c28/scherzo-mockup-c28.mp3`. Data as rendered: `cycles/c28/build_render/` (its parts.json differs from the
  rendered one only in `ride_trims`, the delivery rows). Records: `cycles/c28/records/`.
- Lock (`phase.log`): taken 09:28 (after the finale's c28 actor released it; no other waiter), released 10:25: **57 min**
  (control ranges, range-track build, restart, candidate ranges, restart, full build, restart, render, save, rebuild of 4
  stale tracks, save, guard 0 stale, quit).
- REAPER memory: 43-44 GB settled before each pass, **44 GB after the render** (0 compressed).
- Master -23.8 LUFS, LRA 21.7, true peak -3.1 dBFS, sample peak 0.702; no stem over -7.7 dBFS.
- Disk: c27's stems and returns deleted (00_Master.wav and mp3 kept); my range WAVs deleted; 41 GB free.

## Changes

### Tools (generic, off by default)
- `tools/score_to_parts.py`
  - `STAC_ROW_BY_PITCH_REP_ONLY = {track: True}` (A #1): the pitch reroute takes a note only when the previous or next note
    has the same pitch, is a printed staccato and is 0.5 qn or less away.
  - ART_SPANS `"mark": "tenuto"` filter (C #1).
  - HP_GAIN_TO_CC11 keys (B #1, #2): `hold_rest_min_qn` (only a rest this long ends a hold early), `hold_to_dec_qn` (a hold
    that reaches its cap with no printed change runs to a printed decrescendo within D qn, released across it, when no
    softer mark and no long rest come first), `keep_short_arrivals` (the bare `continue` for short arrival notes now calls
    `_keep()`).
  - `KS_ALIASES`: the timpani rules' felt row names map to the `Timpani Hrd KS` rows.
- `tools/build_reaper.py`
  - `cresc_trim_hold` keys `hold_to_dec_qn`, `rest_min_qn` (B #1, as above for the held trim) and `hold_through_rise`
    (a new crescendo is not a release point; tried on the lanes, not adopted: the Oboe 1 384 fall did not come from it and
    the coda woodwinds got a 3.4 dB step at 1008).
  - Envelope ceiling check (finale c29 note): the build stops if any volume-envelope point passes mix.json
    `env_ceiling_db` (default +23.5; REAPER clips at +24). The trims' excess already goes to CC7 (`env_max_db` 23.0); the
    current data peaks at +23.0 (trombones), so the check changes nothing in this build.

### Data (`build/score_config.py` c28 block; `cycles/c28/actor_scripts/apply28.py` writes roles.json / mix.json from `before/`)
1. Dan's figure (A #1): `STAC_ROW_BY_PITCH_REP_ONLY = {"Violins I": True}`: 30 single staccatos back to their c18 rows and
   velocities (Spiccato 90 -> 60 notes; 782 / 786 stay on Spiccato through ART_SPANS).
2. Arrival sags (B #1, #2): every HP_GAIN_TO_CC11 entry with keep_rel_db_s gets `hold_to_dec_qn` 32, `hold_rest_min_qn` 2.0,
   `keep_short_arrivals`; the 300-310 / 900-910 crescendos into the ff tuttis drop their gain on woodwinds and strings
   (`drop_always` 309 / 310 / 909 / 910; B proposed `drop_ends`, which keeps an unchained wind gain; brass unchanged);
   mix.json `cresc_trim_hold` hold_to_dec_qn 32, rest_min_qn 2.0.
3. Summit (B #3): ARRIVAL_WEIGHT_AT 1005 removed; roles.json +2.5 dB passage level 1005-1017 on the 15 tracks that had it
   (new row [1005, 1017, 2.5] on 10 tracks; +2.5 added to the rows already starting at 1004.75 on Violins I / II, violas,
   celli).
4. Tutti downbeats (C #1, A #3): tenuto rows range-tested and **not adopted** (below). Accent body dip back to (0.22, 0.36)
   on Violins I / II only; Violins II add_loud 6 -> 10, Violins I 12 -> 14.
5. Timpani hard sticks (C #2): the Timpani track plays `Timpani Hrd KS` (whole movement, see "Faults"); mix.json
   region_gain_db refit from the range test: stroke rows (Lng, Sht) vel<70 -2 dB, vel>=70 +2 dB, roll row -1.5 dB.
6. Inner lines (C #4, B #5): Violins I `cc7_spans_db` [755.6, 804, +2.0] (CC7 reached 127 on 41 points: +1.9 dB net);
   Horn 3 / Horn 4 countermelody roles 313 -> 311.5, 913 -> 911.5.
7. Soft heads' eighths (A #2, variant a): v62 on the nine pairs. The 0.02 qn overlap could not be written (NOTE_END_AT is
   clipped to the next moved onset - 0.02 qn), so the test and the render are v62 alone. Variant b, Leg BC on the celli
   trio tune, the RR reset at 909 and Stac On Bow: not run (lock time).
8. Delivery (finale c29 note): three ride rows that stepped down at an ff arrival moved: the 305 tutti's -1.0 row starts at
   914.6 (was 911.0), the rows over bars 104 / 304 end before them (308.6-309.0, 908.6-909.0).

Opus state changes (full rebuild): Timpani (patch, region gains); range-only: Double basses, Tuba, Bass trombone, Trombones
(rows; reverted). Every track was built in full before the render.

## Range tests (control P0 = c27 project, P1 = candidate on 9 tracks, same starts, restart between; `records/range_P0.txt`, `range_P1.txt`)
| measure | P0 | P1 | decision |
|---|---|---|---|
| basses tenuto (312-360) peak / -6 dB point / downbeat over beats 2-3 | +175 / -15 ms / +1.5 dB | Marc Lng: +155 / +65 ms / +0.3 | rejected |
| tuba | +165 / +30 ms / +2.8 dB | Portato: +188 / +65 ms / -0.2 | rejected |
| trombones / bass trombone peak level | -35.5..-36.7 dB | Portato: -42.1..-42.4 (later) | rejected |
| Violins I accents (A's measure, peak, -6 dB) | -0.4, 0.163 s, +33 ms, 1 over +3 | -0.4, 0.163 s, +1 ms, 0 over +3 | adopted |
| Violins II accents | -1.2, 0.279 s | -0.5, 0.184 s | adopted |
| cor anglais accents | -1.3, 0.151 s | -1.3, 0.249 s | not adopted (c27 dip kept) |
| timpani strokes 264-362: peak / 1-5 kHz share | -30.8 / -17.4 | -33.2 / -16.2 | hard sticks + refit |
| timpani intro strokes 0-40 | -42.3 / -28.4 | -40.5 / -18.2 | (v50-69 +1.9..+5.6 dB, v70-109 -1.0..-3.2) |
| timpani roll 300 | -36.8 | -35.4 | roll row -1.5 |
| soft-head eighth 1: 2-5 kHz over the staccato before / level | +6.8 / +1.0 | +1.0 / -3.1 | v62 adopted |
| bar 110 79->78 / 342 F sharp vs 345 C | 3.0 / +0.8 over | 3.2 / 2.0 under | adopted |

## Full render: measured (c27 -> c28)

### Figure, first check (`records/fig25.txt`, `fig28w.txt`)
- Violins I bars 110 / 310 step 79->78 **2.8 / 2.5 -> 3.7 / 4.3** (target 3.7 met), 78->75 11.8 / 11.7 -> 14.0 / 13.9.
  Bars 115 / 315 first step 78->79 22.2 / 22.6 -> **13.3 / 13.5** (the F sharp is now on its c18 row; still a clean
  crossover, but 9 dB less margin than c27). Bar 23 79->81 4.4 -> 5.6, other steps unchanged; bar 263 within 1.4 dB; every
  other occurrence within 0.3 dB. Violins II unchanged (within 0.7 dB).
- Woodwinds (A's +70 ms measure, median / under +3 / worst): Flute 1 +9.3 / 4 / -3.9 (same); Flute 2 +12.3 / 4 -> +8.5 / 5
  (948: 11.7 -> 2.2 with no Flute 2 data change there; 318 and 344 rose 4-5 dB); Oboe 1 +16.5 -> +20.6; Clarinet 2 +22.0 ->
  +20.5. The c26 woodwind state is unchanged.
- Spiccato (`spic.txt`): rerouted notes 68 -> 38, over neighbours median -0.8 dB, over +3 5 -> 1; **F sharp 342 now 3.2 dB
  under the accented C at 345** (was 0.8 over).

### Guard and net in-note moves (`records/guard_c28.txt`, `netmoves_c28.txt`)
| | c27 | c28 |
|---|---|---|
| step 1.5 dB / 0.5 s at > 6 dB/s | 1 (+14 harp) | 1 (celli 524) (+14 harp) |
| first 0.35 s 1.5 dB | 2 | 2 (celli 526 / 624) |
| B's 2 dB / 20 dB/s | 0 | 0 |
| net moves 1 dB+ inside note bodies (envelope + CC7) | 398 (350 in hairpins, **48 outside**) | 405 (371 in hairpins, **34 outside**) |
- Gone: celli 632 / 634, violas 632, Violas div 632, Bassoon 2 632, Flute 1 156 / 384, cor anglais 156, Clarinet 2 1005 tail.
- Left outside hairpins: the 3 final fades, harp 238 (x3; moving the role into the decrescendo was tried on the lanes:
  harp steps 14 -> 18, not adopted), Clarinet 1 / Bassoon 2 1005 1.1-1.2 dB (not from the arrival weight: the fall after
  the fff step, source not traced), and 1.0-1.5 dB slow ramps on held tutti chords (B's class "not heard").

### Arrival sags (B's measure on the lanes, `records/sags.txt`)
Falls of 1.5 dB or more after a printed crescendo: **35 -> 7** (3 dB or more: 18 -> 2). Left: Oboe 1 384 / 852 4.6 dB (a CC7
step at the next crescendo's start, 387; not from the trim hold; open), Flute 1 / 2 309-310 1.8, Violins I 910 1.5,
Bassoon 1 / Clarinet 2 1005 2.2 / 3.6 (the coda woodwinds' own fall at the end of their 1005 hold).
- Trio climax (B #1), master per bar 209-217: c27 -30.1 -29.9 -30.3 -30.7 -32.4 -32.7 -34.2 -32.6 -30.2 -> c28 -30.1 -29.6
  -30.1 -29.4 -30.9 -31.0 -32.0 -30.5 -28.5: the sag into bar 215 is 2.6 dB (was 4.3), the 648 crescendo still rises
  2.0 dB to bar 217. Celli net +2.6 dB held 624-654 (c27 -2.8 from 635): **the celli stay 5.4 dB louder for 14 qn**, as B
  asked; critic C / Dan should judge whether that is too long (c27's objection).

### Summit (`records/summit.txt`, `spec_final.txt`)
- Stem sum: step into 1005 +1.4 -> **+1.1 dB**, 10 ms peak +0.18 -> +0.39 s (the single-note weight is gone); bars 337-340
  +1.8..+2.1 dB on the master.
- mp3: summit lead over bar 335 +0.57 -> **+0.67 LU**; over the next loudest passage +1.2 -> +1.1 LU.

### Tutti downbeat weight (`records/extra.txt`, downbeat 10 ms peak minus beats 2-3)
Master / mp3: 312-360 -0.2 / 0.0 -> **-0.3 / -0.1**; 912-960 +0.9 / +0.6 -> +1.2 / +0.7; theme A +2.3 / +2.3 -> +2.9 / +2.6.
C's +2 dB target is not met: the tenuto rows failed (range test) and nothing else moved the bass downbeat.

### Timpani stick sound (`records/extra.txt`; 1-5 kHz share of the first 50 ms, stroke peak)
| passage | c27 | c28 |
|---|---|---|
| intro 0-40 | -28.1 / -42.3 dB | **-18.2** / -41.5 |
| ritmo 264-300 | -19.3 / -34.2 | -17.3 / -35.9 |
| tutti 300-362 | -17.2 / -29.9 | -15.4 / -30.3 |
| reprise tutti 900-962 | -17.5 / -30.4 | -15.2 / -29.9 |
| coda 990-1020 | -15.9 / -31.0 | -14.7 / -30.7 |
| Meno mosso 1020-1128 ("soft sticks") | -29.0 / -53.4 | -19.4 / -53.9 |
Rolls within 1 dB of c27 (300 -36.9, 906 -39.0, 1005 -35.1, 708 -52.8). C's -12 dB front target is not met in the loud
passages; the soft strokes gain the most colour. G.P. drop on the master 18.7 dB.

### Inner lines (item 6)
- Reprise per bar 261-267, Violins I / Flute 1 (dB): c27 -43.4/-41.8 -44.4/-39.3 -40.1/-38.2 -41.1/-37.9 -45.7/-42.5
  -44.6/-41.0 -48.3/-43.6 -> c28 -40.8/-41.8 -42.4/-41.8 -37.7/-38.1 -40.8/-37.8 -43.9/-43.8 -44.3/-40.3 -46.2/-44.6: the theme
  is over or level with the flute in 4 of 7 bars (was 0 of 7), still 3-4 dB under in 264 and 266.
- Horn 3 net level at the countermelody head 312: +1.9 -> +3.9 dB (lanes).

### Accents
- A's measure (first 100 ms over the unaccented notes within ±2 qn, 299-362): Violins I -1.2 -> -1.2 (max +10.3 -> +2.6);
  Violins II -1.4 -> -0.9 (peak 0.263 -> 0.213 s); cor anglais -1.4 -> -1.5. Still under Dan's +1..+2.
- acc2 (against the detached note before): Violins I -3.1 -> -3.8, Violins II -2.7 -> -2.3, violas -0.3 -> +0.2 (over +3:
  5 -> 3), celli +1.2 -> +0.8 (5 -> 3). No track's median over +3.
- Soft heads' eighths (9): eighth 1 2-5 kHz over the staccato before +5.6 -> **-0.1 dB**; the join (trough against the
  eighth) unchanged; landing -0.6 -> +0.3.

### Envelope table: points 2,808 -> 2,547; per note 0.50 -> 0.46; per second 10.1 -> 9.2.

### Delivery against the shared spec (`records/deliver_final.txt`, `spec_final.txt`; first delivery `deliver_first.txt`)
| | c27 | c28 first | **c28 final** |
|---|---|---|---|
| 1. I / TP | -14.0 / -1.4 | -14.0 / -1.4 | **-14.0 LUFS / -1.4 dBTP** |
| 2. summit lead | +0.57 over 335 | +0.67 | **+0.67 over 335** |
| 3. f -> ff | 2.10 | 1.77 | **1.88 LU (under the 2.0 target)** |
| 4. p10 short-term | -20.4 | -20.6 | **-20.6** |
| 5. limiter (summit) | 3.3 | 3.7 | **3.7** |
| 6. LRA | 10.6 | 10.8 | **10.9** |
- f -> ff fell because bars 104 / 304 (in the ff set) lost their crescendo gain (item 2, B #2c: -0.6 / -0.9 LU on the mp3).
- Climax order on the mp3: summit -7.2, 305-320 -8.3, 105-120 -8.5, bar 300 -8.5, bar 72 -8.7, bar 304 -9.1.
- Crescendo arrivals: 41 +1.7, 72 +0.4, 105 -0.4, 129 +0.5, 197 +0.6, 209 +0.5, 285 +0.6, 300 +1.2, 304 +1.2, **305 +0.4
  (was -0.4)**, 329 +3.1, 336 +0.7. 105 is still reversed (the brass chord of bar 104 against the trumpets' quarters).
- Quiet means: intro -17.0, theme A -17.3 (-16.9), fugato -21.8 (-22.3), trio dolce -16.0, Meno pp -19.4 (-19.1).
- Hall: master G.P. drop at +0.3 s 18.7 dB, 20 dB fall 0.33 s, RT60 1.42 / fitted 1.45 / late 1.46 s; mp3 17.9 dB / 0.36 s /
  1.40-1.51 s; soft ends 0.06-0.19 s. Inside Dan's limit.
- Ride rows against arrivals (finale note): of the 16 rows, 13 change near a printed crescendo end; the three that cut the
  ff arrivals of 104 / 304 / 305 were moved (item 8); the others are falls into soft passages after the arrival or lift
  rows (72 / 213 has two -1.5 rows starting at 211.5-212.5: not moved, arrival +0.4).

### Timing (`timing.txt`, `pcx.txt`): over 25 ms 27 % (c27 26 %), over 60 ms 5 %; celli joins +29 ms, Violins I +9, II +6.

### Per-bar master against c27 (`bars_c28_vs_c27.txt`, median 0.0)
Over +1.5: 9 / 91 / 94 (hard-stick strokes), 42-43 and 136 (holds), 214-217 (trio plateau), 337-340 (summit level), 58 +3.9
(the celli fugato round robin swung back; no celli data change there). Under -1.5: 104 -1.6, 304 -2.4, 305 -1.8 (no
crescendo gain at the tutti arrivals), 12 -1.6 (timpani).

### Coordinator's finale c29 notes
- Timpani after bar 340: **cannot switch** in one instance (the patch is per Opus instance; a second timpani instance would
  break the 45 GB cap, MANUAL-GAPS #6). The six "soft sticks" strokes of 341-376 play hard sticks at v<70 with -2 dB; their
  1-5 kHz share is -19.4 dB (felt -29.0), peak -53.9 dB.
- Horns: no "Mono From Left" routing here (stereo patches); pans -0.18 / -0.16 / -0.15 / -0.13 (Horns 1-4). Section L/R
  correlation in 312-360 0.961 (c27 0.957), Horn 1 alone 0.910. Not spread this cycle.
- Envelope ceiling: check added (above); current maximum +23.0 dB.
- Exposed brass legato holes: not checked (time).

## Rejected, deferred, not done
- C #1 tenuto rows (Marc Lng / Portato): range test, later and softer (table).
- C27_BODY off on the cor anglais (peak later); violas not tested, left on the c27 dip.
- hold_through_rise (lanes: no gain on Oboe 1 384, a new step at 1008); harp role into the decrescendo (more harp steps).
- A #2 variant b (eighths on Sus MAX), A #1 Stac On Bow variant, C #3 Leg BC on the celli tune, C #5 RR reset at 909, the
  Violins I staccato ring test: not run (lock time).
- Delivery row at 211.5-213.5 (bar 72 arrival): not moved (two overlapping rows; arrival +0.4).

## Faults still audible (instrument side not found)
- Tutti downbeats no heavier than beats 2-3 (-0.1 / +0.7 dB on the mp3).
- f -> ff 1.88 LU (bars 104 / 304 lower without the crescendo gain).
- Summit step +1.1 dB (target +3), lead +0.67 LU.
- Accent fronts under their neighbours (-0.9..-1.5 dB on A's measure).
- Hard sticks on the coda's soft-stick strokes; tutti strokes' 1-5 kHz share -15 dB (target -12).
- Oboe 1 384 / 852: 4.6 dB CC7 step at the next crescendo's start (387 / 855).
- Bars 115 / 315 first figure step 22 -> 13 dB margin.

## Research items
| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; net in-note moves outside hairpins 48 -> 34; arrival weight at 1005 replaced by a passage level |
| dynamic trims as CC7 (finale 135), role edges into rests (136) | adopted (unchanged); holds to the printed decrescendo |
| soft legato heads CC11 front (finale 139) | adopted (unchanged) |
| Marcato Sustain on a chord stroke (finale 140) | adopted (unchanged) |
| accents by the KS Masters' accent rows | adopted (unchanged) |
| tenuto quarters on Portato / Marcato Long rows (MANUAL-GAPS #10) | **rejected** (range test: +23-65 ms later, trombones -5.4..-6.6 dB) |
| timpani hard sticks (MANUAL-GAPS #6) | **adopted** (whole movement; 1-5 kHz share +2..+10 dB) |
| CC16 resets | adopted (unchanged) |
| shared -14 delivery + room-noise bed | adopted; ride rows off three ff arrivals |
| oboe Main lower than -9 dB | pending (not run) |
