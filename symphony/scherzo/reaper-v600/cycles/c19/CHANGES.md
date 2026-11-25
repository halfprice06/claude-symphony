# Cycle 19: changes (actor, on the c18 render)

STATUS: **rendered once**, 2026-11-17 09:04-09:11 CST, from a freshly restarted REAPER (state guard 0 stale before the render).
- mp3: `cycles/c19/scherzo-mockup-c19.mp3` (re-delivered from the c19 master after the render with the delivery changes
  below; md5 56dd62aa63f9a8697da28af012e836e8). The first delivery (2.5:1 top ride, old trio ride row) read -14.1 LUFS,
  LRA 11.8.
- Data as rendered: `cycles/c19/build_render/`. Data of the delivered mp3: `cycles/c19/build_fix/` (ride rows only).
- `build/` is one unrendered step ahead: Clarinet 1 `dyn_trim_db` ff +1.2 -> -1.0 (critic B #3 fallback, below).
- Lock: queued 07:15 behind mvt3 and mvt1; held 08:35:08-09:12:21 (37 min): open, settle, full build of 31 tracks,
  range tests (celli 504-552 twice, Horn 1 at 1068 / 436 / 592), string rebuild, restart, settle, Horn 3 rebuild (stale
  after the restart's save), save, guard 0 stale, audio_init, render, quit, unlock.
- REAPER memory: 43 GB settled after the open; 44 GB with 0 GB compressed after the render.
- After quit the saved project holds 6 stale Opus states (`state_guard_final.txt`): c20 must rebuild first.
- Disk: c18's stems were not deleted (the coordinator's c19 note: do not delete c16-c18 stems or render_first). My
  range-test files are deleted.

## Result

| | c18 | c19 |
|---|---|---|
| master | -21.5 LUFS, LRA 22.6, TP -2.7 | -21.5 LUFS, LRA 22.5, TP -3.1 dBFS, sample peak 0.696, no clipping |
| attack probe | late or hole 0 | late or hole 0 |
| delivered (mp3) | -14.1 LUFS, LRA 12.0, TP -1.3 | **-14.0 LUFS, LRA 12.2, TP -1.4 dBTP** (2 loudness passes) |
| short-term p10 / span | -21.7 / 14.2 dB | -21.6 / 14.1 dB |
| limiter per passage (look-ahead aligned) | summit 5.5, tutti 105-120 3.9, 305-320 2.8, bar 72 2.8, bar 300 2.4, final chord 0.1 | summit 5.6, tutti 105-120 3.8, 305-320 2.8, bar 72 3.0, bar 300 1.9, final chord 0.1 |
| climax order, master (M max) | summit leads by 1.6 LU | summit -11.6, bar 304 -12.8, bar 300 -13.5, tutti -13.6 / -13.7, bar 72 -15.0: leads by 1.3 LU |
| climax order, mp3 | summit leads by 0.7 LU | summit -7.1, bar 72 -7.7, bar 300 -7.7, bar 53 -7.9, tutti 305-320 -7.9, bar 333 -8.0, trio ff -8.0, tutti 105-120 -8.1, bar 304 -8.3: leads by 0.6 LU. Every bar: the five loudest are 338, 335, 339, 336, 337; 334-335 (the crescendo into the fff) within 0.5 LU |
| crescendo arrivals on the mp3 (M max over the bar before) | 209: +0.9 (first c19 delivery: -0.0) | 41 +1.3, 72 +0.6, 129 +0.4, 197 +1.6, **209 +1.2**, 285 +0.4, 300 +1.7, 304 +0.3, 329 +2.2. Not reaching the master's step: 336 (master +1.8, mp3 0.0; the limiter) and 105 / 305 (-0.4 / -0.5, -0.8 on the master too: the ff arrives at 104 / 304) |
| hall (`hall17.py`) | G.P. drop 18.4 dB, 20 dB fall 0.33 s, RT60 1.38 s | the same: 18.4 dB, 0.33 s, RT60 1.38 s |
| envelope points / per note / per second | 4,852 / 0.84 / 17.5 | 4,831 / 0.84 / 17.4; slope guard 9 notes (6 over 3 dB: celli 312 / 912 4.3, 362 4.0, Horn 2 1005 3.2, Horn 3 953 3.0, harp 708 3.0; all printed-hairpin edges, unchanged from c18); per-note rows 0 new |
| string legato join excess (`legx18.py`) | median +3.1, 91 of 429 over 6 dB | median +3.2, 96 of 429 over 6 (unchanged: neither fix was kept, see 1) |
| Horn 1 hole under the body (0.12-0.40 s after the note-on) at 442 / 598 / 1077 | 11.6 / 9.9 / 11.3 dB | **3.4 / 1.6 / 3.2 dB**; the G sharp's body 1.1-1.8 dB lower |
| Violins II trio arpeggios under the celli, bars 169-176 / 177-184 | -8.6 / -9.8 dB | **-4.2 / -5.7 dB** (celli still loudest) |
| fugato held notes 171 / 183 / 195 (0.1-0.6 s after the note-on) | -42.9 / -40.0 / -35.3 | -40.7 / -39.2 / -37.0 (spread 7.6 -> 3.7 dB; Violins II still 2.2 over the violas) |
| tutti countermelody under the loudest, bars 105-111 / 305-320 | celli -2.9 / -2.2 | celli -2.6 / unchanged |
| Clarinet 1 over Violins I, bars 41 / 214 / 300 / 302 / 334 | +1.7 / +3.8 / +2.2 / +1.6 / +3.9 | +0.0 / +3.6 / +1.2 / +3.1 / +3.0: under 1.5 dB at ff, so the ff trim -1.0 is in build/ for c20 |
| isolated accents, first 100 ms (`acc19.py`): median / p90 / over +3 | -0.9 / +3.0 / 15 | -1.1 / +2.8 / 14 (Violins II 4, Clarinet 2 2, Violins I 2) |
| Violins I "Sus Marc LITE" accented halves (0-0.3 s) | +4.1..+6.9 over neighbours | 39 / 69 / 75 / 285 / 759 / 789 / 795: -2.7..-3.8 dB on c18; 51 / 771 back on the row (+7.2 / +7.6 on c18's "Sus MAX") |
| timing outside 25 / 60 ms (Allegro, 16 tracks) | 26 % / 5 % | 26 % / 5 %; trio and Meno mosso (6 tracks) 38 % / 7 % -> 36 % / 6 % |
| hemiola half notes (pc) | Clarinet 1 304 / 306 / 904 / 906 +27..+43, Flute 1 304 +39 | -15 / +9 / -7 / +7, Flute 1 304 -1; Clarinet 2 308-910 -6..-1; cor anglais 306 +68, 906 +58 (c18 +75 / +27) |
| clarinet median S (Allegro) | Clarinet 1 +14, Clarinet 2 -4 | +7 / -6 |
| per-bar master against c18 (`records/bars_c19_vs_c18.txt`) | | 10 bars over +1.5, 5 under -1.5. Intended: 18 / 258 +4.0 / +2.5 (Violins I back on its theme row), 58 (celli fugato +8), 168-173 (Violins II trio), 328 (+1.9, the hold back), 14 / 24 / 26 / 96 / 254 -1.6..-2.0 (the Marc halves -4 dB). 290 +1.7 (celli, unchanged data: the c18 round-robin take came back) and 365 +2.2 (Horn 1 and Horn 3 stems within 0.4 dB of c18: the hand-off's partial cancellation differs, unchanged data) |
| timpani strokes against c16 | | bars 3-5, 91, 94, 97, 105, 113, 305, 313, 329, 336 equal to c16 within 0.1 dB; 333-335 -2.5 dB (c18's role deletion, as intended) |

## Changes made

### Tools (all generic options off by default)
- `tools/score_to_parts.py`:
  - WIND_DETACH `overlap_s` tests the row the keyswitch plays (after REP_ROW), not the row the rules see. Fix, always on;
    on this data it removes the 34 clarinet overlaps on "Leg Slur Rep" (C #1).
  - ACCENT_CC keys `soft_cc` / `add_soft`: under `soft_cc` resting CC11 the bump is at most `add_soft` (A #3).
  - `RETONGUE_LEAD_CAP_AT` {track: {score onset: share}}: per-note cap of the re-tongue lead (C #4).
- `tools/build_reaper.py`: `region_gain_db` layer `"group:PREFIX"` (regions of groups whose name starts with PREFIX, e.g.
  "group:TLeg"). Tested, not used in the data.
- `tools/deliver_master.py`:
  - loudness loop and true-peak retry (the shared method from the finale c21 / Movement I);
  - top ride 2.5:1 -> 2:1. On the c19 master this gave LRA 11.8 -> 12.3 with the same limiter and order.

### `build/score_config.py` (c19 block at the end)
- `LEG_TRANS_CC = {}` (A #1, C #2).
- Woodwind `overlap_min_s` 0.4 -> 0.6 s (C #1). `REP_GAP_FLOOR_LONG_S` kept: A called it a no-op, but removing it
  changed 40 held same-pitch repeats (Horn 2, Horn 4, low brass, Bassoon 2) in parts.json. Those repeats are a
  do-not-touch item.
- `CC11_ADD_SPANS`:
  - Violins II (501.3, 551.4) +9 (B #1);
  - Violoncellos (170.9, 174.0) +8 (B #4);
  - Trumpets 1 / 2 -14 / -16 over 993.85-995, back by 995.6;
  - Horns 3 / 4 -14 over 989.5-995, back by 995.8 (these replace the role rows, B #6).
- Horn 1 (A #2):
  - `ART_AT` 442 / 598 / 1077 "Sus MAX";
  - `REATTACK_LEAD_AT` 0.05 s;
  - the A4 ends 0.02 qn before the G sharp's moved note-on;
  - VEL_SET 1077 72 removed.
- Violins I 597 (A #4, C #3):
  - a Sus MAX stroke (`DOWNBOW_STROKE_AT`, `REATTACK_LEAD_AT` 0.085 s);
  - 600 `ART_AT` "Leg Slur MAX" at velocity 100 (without these it fell to Sus MAX at velocity 52 with no lead).
- Horn 3 (C #4):
  - `RETONGUE_LEAD_CAP_AT` 510 / 519 0.46 (lead 79 -> 120 ms);
  - VEL_SET 512 / 524 at 120.
- `CC1_DYN_MAP_BY["Clarinet 1"]` with f / ff / fff 6-10 units lower (B #3).
- ACCENT_CC: `soft_cc` 60, `add_soft` 6 on the string entries. Only the celli, basses, solo and Violas div change:
  the per-track entries of Violins I / II and violas already add 2-5 units.
- `RIDE_TRIMS`: the trio row ramps over bar 209 (625 -> 627) instead of reaching -2 dB on its ff arrival.

### `build/roles.json`, `build/mix.json`, `build/lead_set.json` (`actor_scripts/apply19.py`, rerunnable from `before/`)
- Roles 164 -> 153:
  - the per-note rows of the timpani [300, 300.5, -12], trumpets [994, 995.5] and Horns 3-4 [990, 995.8] deleted;
  - 9 rows under 1 dB deleted (Violins I [1089, 1128, -0.5] kept);
  - 6 overlapping pairs merged into non-overlapping rows with the summed values. The other 8 pairs were the deleted
    -0.7 / -0.8 rows.
- Mix:
  - Violins I "Sus Marc LITE" `vel<66` -4 dB (A #3);
  - Horn 3 E4 region gain -3 -> -1 dB (B #5);
  - Violins II has its own `cresc_trim_hold` with [981, 984]; the top-level skip no longer has it (B #2);
  - after the render: Clarinet 1 `dyn_trim_db` ff -1.0 (not rendered).
- Leads: celli 933 0.18 / 948 0.155 (their c17 values); Violins I 597's row deleted.

## Range tests (lock held, first render after each rebuild discarded)
- Celli 504-552 with "TLeg" groups -2 dB on "Leg Slur MAX":
  - join excess median +3.5 (c18 +3.9);
  - over 6 dB: 8 (c18 6);
  - single joins moved -2..+2 dB both ways: round-robin scatter, no fall;
  - one join (510) read -9.4 (a hole), against +1.3.
  - Not adopted (target: 1 dB or more lower, no hole). All six string tracks rebuilt with no TLeg gain.
  - The finale's alternative ("Sus MAX" on held arrivals) is not tried. It turns slurred notes into re-bows and needs
    its own test.
- Horn 1 "Sus MAX" G sharps: the hole fell to 1.3-3.8 dB, so it was adopted.
  - The last keyswitch before the first note in each range was Sus MAX at 441.75 / 597.78 / 1076.78. Each was the
    track's own keyswitch.

## Rejected, deferred, not done
- TLeg region gains (A #1): no measurable effect, above. The string legato swell is still audible.
- Downbeat weight by velocity in the tuttis (C #5): not tested (low priority, no lock time).
- Horn 1 / Horn 3 hand-off at 1092: not tested. Bar 365 is +2.2 dB on unchanged data (the cancellation differs).
- Celli pizzicato round-robin (ONE_TIME 1.85 / 5.91): not done.
- The 54 role rows on tutti / summit spans: not moved into `dyn_trim_db`.
- Violins II accents over +3 dB (123, 195, 372, 819, 840): these are DOWNBOW_STROKE "Sus MAX" strokes after short
  notes. The ACCENT_CC add is 2 units there, and `soft_cc` does not reach them. Open.
- Wind legato velocity floor (finale c22): our targets at 71-90 have too few measurable long notes on c18 (1-6 per
  track). Movement I found no gain, so it is skipped.
- Brass short rows on ff CC11 and trumpet 300 ms releases (finale c21): optional, not done.
- Faults still audible:
  - the string legato join swell;
  - the summit has no step over bar 335 on the mp3, because the limiter takes 5.6 dB there (master +1.8 LU). A
    -1.5 / -3 dB ride on bars 334-335 moved them 0.1 LU, so it was not kept;
  - Clarinet 1 over Violins I in bars 214 / 302 / 334 (+3.0..+3.6 dB; the ff trim is waiting in build/);
  - Violins II's fugato note 2.2 dB over the violas'.

## Research items

| item | status |
|---|---|
| EW template mix, returns, EQ, seats, wind send, return pans | adopted (unchanged) |
| no volume automation per note (Dan 2026-11-11) | adopted; 0 new per-note rows, 5 removed; slope guard 9 notes |
| accents by controller | adopted; first-100 ms p90 +2.8 |
| one legato row per string line, keyswitch 0.15 s ahead | adopted |
| per-region / per-row volume in the Opus state | adopted; TLeg group gain rejected (range test, above) |
| shared -14 LUFS delivery with loudness loop, 2:1 top ride | adopted (-14.0 LUFS, LRA 12.2, TP -1.4) |
| unprinted tempo, Slur Runs, Close + Main on divisi | rejected earlier |
| CC16 resets everywhere, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |
