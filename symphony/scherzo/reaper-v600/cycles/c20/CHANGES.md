# Cycle 20: changes (actor, on the c19 render)

STATUS: **rendered once**, 2026-11-17 ~13:00-13:15 CST, from a freshly restarted REAPER (state guard 0 stale before the
render).
- mp3: `cycles/c20/scherzo-mockup-c20.mp3`. Data as rendered: `cycles/c20/build_render/`.
- `build/` is one step ahead of the render: Horn 1's CC1 cap removed (below, item 9). The same data is in REAPER, saved,
  and the guard read 0 stale after the save.
- Lock: queued 09:37 behind mvt3 and mvt1. Held 12:26:11-13:22:46 (56 min): open, settle, guard and control build,
  three range-test passes plus a control pass (Violins I / II, violas, celli, Clarinet 1, Violins I 999), final build,
  restart, settle, guard 0, audio_init, render, Horn 1 rebuild, save, stale rebuild, save, guard 0, quit, unlock.
- REAPER memory: 43 GB settled after the restart, 44 GB after the render (14 GB compressed). During the range tests it
  reached 52 GB (36 GB compressed) after about 25 track rebuilds. The restart brought it back to 43 GB.
- Disk: 25 GB free at 12:26 (other threads), 30 GB at 12:37, 50 GB before the render. My request to delete c17's stems
  was refused by the permission check, so I did not retry it. c19's stems (35 WAVs) are deleted, and c19's
  00_Master.wav and mp3 are kept. My range-test WAVs and my scratch folder are deleted. 49 GB free at the end.

## Result

| | c19 | c20 |
|---|---|---|
| master | -21.5 LUFS, LRA 22.5, TP -3.1 | -21.3 LUFS, LRA 22.7, TP -3.1 dBFS, sample peak 0.696, no clipping |
| attack probe | late or hole 0 | late or hole 0 |
| delivered (mp3) | -14.0 LUFS, LRA 12.2, TP -1.4 | **-14.1 LUFS, LRA 12.3, TP -1.4 dBTP** (1 loudness pass, shortfall 0.1) |
| short-term p10 / span | -21.6 / 14.1 dB | -21.7 / 14.0 dB |
| limiter per passage (look-ahead aligned) | summit 5.6, tutti 105-120 3.8, 305-320 2.8, bar 72 3.0, bar 300 1.9, final chord 0.1 | summit 5.5, tutti 105-120 3.8, 305-320 2.7, bar 72 2.8, bar 300 1.7, final chord 0.1 |
| climax order, mp3 (M max) | summit -7.1, leads by 0.6 LU; 334-335 within 0.5 LU | summit -7.1, leads by 0.7 LU (bar 72 -7.8, 318 / 300 -7.9); no bar outside 336-339 within 0.5 LU |
| summit arrival on the mp3 | 336 over 335: 0.0 | **+0.9** (over 333: +2.3); bars 331-339: -11.9, -10.4, -9.4, -9.8, -8.0, -7.1, -7.3, -7.1, -7.2 (334 is 0.4 under 333, as on the master: -14.9 / -15.7) |
| crescendo arrivals on the mp3 | 41 +1.3, 72 +0.6, 129 +0.4, 197 +1.6, 209 +1.2, 285 +0.4, 300 +1.7, 304 +0.3, 329 +2.2 | 41 +1.2, 72 +0.7, 129 +0.5, 197 +1.6, 209 +1.6, 285 +0.6, 300 +1.8, 304 +0.3, 329 +2.2, 336 +0.9. 105 / 305 -0.5 (unchanged: the ff arrives at 104 / 304). No new inversion |
| hall (`hall17.py`) | G.P. drop 18.4 dB, 20 dB fall 0.33 s, RT60 1.38 s | the same: 18.4 dB, 0.33 s, RT60 1.38 s |
| envelope points / per note / per second | 4,831 / 0.84 / 17.4 | 4,812 / 0.84 / 17.3; slope guard 9 notes, the same 9 as c19 (6 over 3 dB: celli 312 / 912 4.3, 362 4.0, Horn 2 1005 3.2, Horn 3 953 3.0, harp 708 3.0; all printed-hairpin edges). New per-note rows: 0. Envelope changes: Clarinet 1 four hairpin gains removed, Violas / Violas div role rows deleted |
| timing outside 25 / 60 ms (Allegro, 16 tracks) | 26 % / 5 % | 27 % / 6 % (winds sus entry median -2 -> -8 ms, from the accent lead) |
| per-bar master against c19 (`records/bars_c20_vs_c19.txt`) | | 3 bars over +1.5, 4 under -1.5. Intended: 23 +4.4 / 263 +1.8 (the Detache pairs), 21 -2.0 (Violins I 60 out of its hot sample). Round-robin takes on unchanged data: 58 +3.0 and 290 -2.1 (the celli stems; the celli data are unchanged). 363 / 364 -1.8 / -2.5: Horn 1 -7.4 / -5.3 from the CC1 cap. That cap is removed in build/ |

## Changes made

### Tools (generic options off by default)
- `tools/score_to_parts.py`:
  - `ROW_CHANGE_ACC_ADD_S` {track: s} with `ROW_CHANGE_ACC_SKIP`: an accented Sus / Marc note whose previous note,
    at most 1 qn before, is on a short row starts this much earlier (A #2).
  - `CC1_SET_SPANS` {track: [(q0, q1, cc)]}: caps CC1 over a span, on any patch (A #3, #6).
  - `HP_GAIN_TO_CC11` key `drop_always`: hairpin gains ending at the listed points are dropped, chained or not (B #3).
- `tools/build_reaper.py`:
  - `sus_release_cap_ms` spec key `"any_dyn": true` caps every non-RT, non-TLeg group of the listed rows (A #4).
  - The cap's print key includes rows and any_dyn. A second spec with the same ms printed nothing before, although it
    was applied.

### `build/score_config.py` (c20 block at the end; range-test switches C20_PAIRS, C20_V999, C20_CL1ROW, C20_LEGSUS)
1. Inner lines:
   - a. Violins II trio: the c19 add (501.3, 551.4, 9, 9) becomes 9 / 9 -> 14 (526-534) -> 17 (534-549.4) -> 9 (551.4).
   - c. Oboe 1: in mix.json, below.
2. Slurred eighth pairs: Violins I's 18 Sus MAX pairs in the Allegro are now on "Detache" (`DETACHE_SPANS`). The soft
   pairs (67, 113, 787) are at velocity 62 / 66 / 69, the loud ones at 100. Their lead is the staccato lead (0.045 s,
   `LEAD_SET_AT`). Violins II's pairs stay on Sus MAX.
3. `RIDE_TRIMS` + [(990, 0), (993, -2), (996, -4), (1004.6, -4.5), (1005.1, 0)] (delivery only).
4. Accents:
   - `_ACC_BY` cor anglais and Flute 1 (6, 6, 116);
   - `ROW_CHANGE_ACC_ADD_S` 0.04 s on Flute 1 (12 notes), Oboe 1 (15) and cor anglais (12), skipping the sf chords
     213 / 897, the hemiola f at 300 and the fff at 1005.
7. Clarinet 1:
   - hairpin gains ending at 633 / 640 / 645 / 663 dropped (`drop_always`);
   - Violins I 999 on "Sus Marc LITE" (vel_by_cc up to 96).
9. Smaller items:
   - cor anglais CC1 at most 45 on 302 / 306 / 902 / 906;
   - timpani bar 335 velocities 98 / 104 / 106 / 110. These are inside the "Timpani Flt Sht" layers 93-98, 99-104,
     105-110 and under the accents' 111-115. The coordinator's 112 would have put 1004 in the accents' layer;
   - VEL_SET Violins I 60 -> 52, Violins II 957 -> 78 and 988.5 -> 94, each into the next velocity layer.
   - Horn 1 CC1 at most 51 on 442 / 598 / 1077: rendered, then removed (below).

### `build/roles.json`, `build/mix.json` (`actor_scripts/apply20.py`, rerunnable from `before/`)
- Roles 153 -> 151: Violas [624, 672, -3.7] and Violas div [648, 672, -3] deleted (B #2).
- Mix:
  - Oboe 1 "Stac DblTng RRx9" velocity layer 1-74 (the p calls play velocity 52): -3 -> +3 dB (B #4);
  - Violins II `sus_release_cap_ms` + {"ms": 150, "rows": ["Stac RRx9"], "any_dyn": true} (749 ms in the patch).

## Measured before / after (c19 -> c20, full renders; `records/base_c19.txt`, `records/meas_c20.txt`)

Inner lines (item 1). Best band = the line against every other stem plus the returns, and against the loudest single
stem in that band (critic B's measure; `inner20.py`):

| line | bars | c19 all / loudest | c20 all / loudest |
|---|---|---|---|
| Violins II arpeggios | 179 | -5.5 / -1.6 (Bassoon 2) | -3.8 / +0.5 |
| | 181 | -7.2 / -3.5 (Violins I) | -4.3 / -0.5 |
| | 183 | -9.7 / -7.1 (Bassoon 2) | -7.1 / -4.1 |
| Violas + Violas div | 211 | -1.2 / +4.2 | -0.5 / +3.3 |
| | 213 | -3.5 / +1.1 (celli) | -1.5 / +3.3 |
| | 215 | -4.9 / +3.5 | -1.2 / +7.2 |
| | 221 | -9.0 / -3.1 | -6.1 / +0.8 |
| Oboe 1 under Flute 1, unison p staccatos bars 29-40 (first 100 ms, 23 notes) | | -9.0 dB median | -4.3 dB median (target about -2) |

Slurred pairs (item 2), each pair note's 10 ms peak against the median of its detached neighbours:
- Violins I bar 23: -13.5 / -13.2 -> -3.4 / -7.6 dB.
- Violins I tutti pairs 317-353: worst-of-pair median -4.8 -> -3.2 dB.
- Violins II is unchanged: -6.7.

Accents (item 4), first 100 ms against the two neighbours, isolated (`acc20.py`):

| | c19 median / p90 / over +3 | c20 |
|---|---|---|
| Flute 1 | -1.7 / +0.6 / 1 | +0.1 / +1.7 / 1 |
| cor anglais | -4.8 / -0.3 / 0 | -2.4 / +1.4 / 1 |
| Oboe 1 | -1.1 / +2.0 / 1 | -1.5 / +1.5 / 1 |
| Violins I | -1.6 / +1.8 / 2 | -1.9 / +0.8 / 2 |
| Violins II | +0.3 / +3.4 / 4 | +0.6 / +3.9 / 5 |
| all (144) | -1.1 / +2.8 / 14 | -0.8 / +3.0 / 15 |

Not at Dan's +1..+2 median yet. No track median is over +3.

Other items:
- Clarinet 1 over Violins I:
  - bar 72 +1.5 -> +0.3;
  - beat 640 (bar 214) +6.5 -> +5.1;
  - bar 300 +1.2 -> -0.9;
  - bar 302 +3.1 -> +2.2;
  - bar 334 +3.0 -> +1.8.

  The ff trim and the dropped gains together give only 1.4 dB at 640.
- Violins I 999 against its neighbours: -3.7 -> -4.9 dB. "Sus Marc LITE" did not lift it, so the fault stays.
- Violins II repeated staccato eighths, bars 104-120: dip median 1.7 -> 2.8 dB. The master's G.P. fall is unchanged.
- Timpani bar 335 (first 150 ms):
  - c19: -35.9 / -32.3 / -33.3 / -33.8;
  - c20: -37.7 / -32.3 / -33.0 / -33.5.
  - It rises 4.2 dB from the first stroke to the last, but 1003 is still the loudest stroke (that stroke's own sample).
- Cor anglais hemiola notes, swing at +0.1..+0.4 s: 13.4 / 10.3 / 8.5 / 10.1 -> 1.7 / 3.7 / 6.9 / 3.9 dB. The front of
  302 / 306 / 906 rose 3-4 dB.
- Horn 1 G sharps:
  - brightness (1.5-5 kHz over 0.3-1.5 kHz) -12.2 / -12.7 / -12.5 -> -15.9 / -16.6 / -16.0 dB, against -27..-32 on
    the A4;
  - bodies -6.3 / -6.9 / -6.3 dB.
  - The target (within 5 dB of the A4) was not met and the note lost level, so the cap is removed in build/ and in
    REAPER (not rendered).
- String legato swell (the critics' both-neighbours form, joins with a body of 0.3 s or more): unchanged. Violas
  median +1.5 (6 over 6 dB), celli +1.8 (3), Violins II +2.4 (1), solo +6.1, Violas div +6.6. No string legato data
  changed.
- Trio tune note bodies: celli 504-552 std 2.5 dB, range 12.1; Clarinet 1 456-504 std 2.6 dB, range 11.6. Both
  unchanged.

## Range tests (lock held; same start for every pass; the order discard, R1 ... R6 kept the same in every pass)

Ranges: R1 Violins I + II 57-72, R1b 107-128, R2 309-361, R3 violas 714-746, R4 celli 501-555, R5 Clarinet 1 453-505,
R6 Violins I 993-1004. Passes:
- control (c20 data);
- A: Violins I / II pairs on Detache, Violas TLeg -6, celli RELEASE 200, Violins II Stac cap 150, Violins I 999
  velocity 112, Clarinet 1 "Leg Slur";
- B: Violins I pairs on StacSl and 999 on Marc; the other tracks back on control, so B is a second control for them;
- C: "Sus MAX" on 9 long legato arrivals.

The last keyswitch before each range's first note was the track's own row, except Clarinet 1. Its "Leg Slur" keyswitch
sits at 408.5, before R5's start (453), so R5 played the control row in every pass. The clarinet test is void
(identical numbers in all passes).

- Control-to-control scatter (control against B): celli join excess median +1.6 / +0.9, body std 4.6 / 3.7 dB;
  violas +/-2 dB on 2 joins.
- Item 2:
  - holes (a pair note 10 dB or more under its neighbours), Violins I, 12 pairs: Sus MAX 4, Detache 1, StacSl 3;
  - StacSl put the soft pairs -10..-14 dB under and the f pairs +6..+14 over, and costs 54 thousand regions;
  - Violins II on Detache: second notes -15 / -8 / -5 dB at 343 / 353 / 347, against a control of -12 at 347. No better.
  - Adopted: Detache on Violins I only.
- Item 5:
  - a. Violas TLeg -6: excess +5.5 against the controls' -0.5 / +1.8, and a 10.8 dB hole at 726. Rejected.
  - b. Celli RELEASE 200: excess +2.1, std 5.0, inside the controls' scatter. Rejected.
  - c. Sus MAX arrivals: the celli 516 body fell 4 dB (the swell gone), but the slurred 514 before it fell 14 dB over
    its whole length, and the violas' 726 body was unchanged. Rejected.
- Item 8: Violins II Stac cap 150 ms: dip median 0.4 -> 3.3 dB, 60 ms peaks -1.4 dB, stem 20 dB fall after 357
  0.19 -> 0.15 s. Adopted.
- Item 7: Violins I 999. Its neighbours read -45.9 / -27.6 / -32.8 dB in the three passes (the range start's
  controller state), so neither variant could be judged. "Sus Marc LITE" was taken on B's reading of that row's
  accented halves; the full render shows no gain (above).
- The coordinator's check (finale c22): the 1st Violins KS Master's Detache groups carry no MidiVelocity. Their level
  follows CC11, like Sus MAX, so the test is valid at the track's own CC11 (`records/velocity_paths.txt`).
- The coordinator's check (finale c23): the celli LegatoSpeed SUS_GROUP_SUBSTRING 'V1s' matches 52 groups, so there is
  no case mismatch.

## Rejected, deferred, not done
- Item 6, Clarinet 1 "Leg Slur" against "Leg Slur Rep": void (keyswitch before the range). Not adopted. Retest with
  the range starting before 408.5.
- Item 6, wider hairpin CC11 swing on the trio tunes: not done (the celli join fix failed first).
- Item 7, Clarinet 1 CC11 held at 76 through 639-641: not done. The dropped gains gave 1.4 dB.
- Item 9: Oboe 1 279 (cold, velocity 42; the next layer is at 75, +33) and Violins II 984 (a printed mf) are left alone.
- Audit of section-wide negative role rows (finale c23 note; `records/role_audit_negative.txt`): 62 rows of 12 qn or
  more. Only the two violas rows were stale under a line with its own role. The rest are doublings or accompaniment
  under the sub. p's and the trio, as B found. The celli at 362-396 double the basses (best band +0.6..+13 dB).
- Faults still audible (Dan's rule, no envelope fix):
  - the string legato join swell;
  - Violins II's arpeggios in bars 181-183, -4..-7 dB in their best band;
  - Clarinet 1 at beat 640, +5.1 over Violins I;
  - Violins I's 999 half note, -4.9 under its staccatos;
  - Oboe 1 still 4.3 dB under Flute 1 in the p calls;
  - accents' median under +1.

## Research items

| item | status |
|---|---|
| EW template mix, returns, EQ, seats, wind send, return pans | adopted (unchanged) |
| no volume automation per note (Dan 2026-11-11) | adopted; 0 new per-note rows; slope guard 9 notes (unchanged) |
| accents by controller | adopted; first-100 ms median -0.8, p90 +3.0 |
| one legato row per string line, keyswitch 0.15 s ahead | adopted |
| per-region / per-row volume in the Opus state | adopted (Oboe 1 stac layer +6); TLeg group gain rejected again (-6 dB, range test) |
| shared -14 LUFS delivery with loudness loop, 2:1 top ride, ride rows | adopted (-14.1 LUFS, LRA 12.3, TP -1.4; summit row +0.9 LU) |
| KS Master articulation rows for figures (Detache, Legato Slur Staccato) | Detache adopted on Violins I's slurred pairs; StacSl rejected (numbers above) |
| unprinted tempo, Slur Runs, Close + Main on divisi | rejected earlier |
| CC16 resets everywhere, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |
