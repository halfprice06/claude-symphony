# Cycle 58: changes (actor)

Render: `cycles/c58/render/` (main pass, then pass 2; no stem fix). Delivered: `cycles/c58/mvt1-mockup-c58.mp3`.
Nobody listened. Every figure is measured on dry stems or the master unless marked. The work stopped on 11 Nov at a
usage limit with the data built and was resumed on 15 Nov; nothing had touched REAPER before the stop.

## Rule
Dan: no per-note level or shape on the track volume envelope, on any track; this cycle also no level rows fitted to
earlier renders. Result, read from a rule dump of the shipped build (`actor_scripts/tags58.py`): envelope items from a
per-note rule 0 on every track; fitted level rows 0. The c57 carry rows are deleted (`build/balance57.json` moved to
`cycles/c58/balance57.deleted.json`), nothing was fitted in their place and no stem was changed after the render.

## 1. Envelope (decisions 1 and 3)
- Carry rows: all 368 deleted. Replacements: `roles.json` Violins I `[128, 160, 3]`, Violoncellos `[56, 88, -2]` ->
  `-3.5`; region gains per critic B #4 (29 entries, per row where rows differ); unison boost as one span per run of
  three or more notes (`UNI_ROLE`, 14 spans; shorter runs get nothing, cost -3 dB on one or two notes); held-note
  diminuendo -3 dB as a CC11 fall (`HELD_DECRESC_CC` strings 10, winds 14 units); `SWELL_CAP_TO_VOL_DB_PER_CC = {}`.
- Deviation from decision 1a: the Violins II theme doubling (77.9-82.1, 104-127, 552-576) stays on Sus Marc LITE with
  its fitted leads (critic C's do-not-touch); its level comes from a row gain of -4 dB in the Opus state
  (`mix.json` Violins II `region_gain_db` `"all_db"`). Bar 21 Violins II: c57 -27.8, c58 -37.4 dB (c56 -41.3).
- Role rows over fewer than three notes count as per-note (Adagio rule) and leave the envelope on tracks with CC11:
  17 of 4 s or more became flat CC11 offsets, 62 shorter ones were dropped (`LEVEL_TO_CC`; list in parts.json
  `vol_slow_only.to_cc`). Config shapes on one held note: 26 became CC11 offsets, the rest stay dropped as in c57.
- Kept "slow" shapes with a segment over 3 dB/s inside are dropped; shapes whose only fast segments are the first or
  last edge are kept (220 of c57's 263) with those edges moved (`ROLE_EDGE`). Role and shape edges: 110 moved into a
  rest within 2 qn, 171 became 2 s ramps; an edge on a printed dynamic stays.
- `ONSET_KEY` (build_reaper): level steps of entries after a rest lie wholly in the rest (Trombone 1 448: +15.5 dB
  now between 60 ms before the note-on and the note-on). Note interiors are unchanged by it (0 notes differ by more
  than 0.8 dB). `HP_REL` 1.0 -> 4.0 qn.
- Table (`envelope_table.md`): points 6962 -> 4515; strings 0.49-0.73 points per second (c57 0.9-1.35; the 0.4
  target is not met: Violins I 0.50, Violins II 0.61, Violas 0.64, celli 0.73, basses 0.49), winds and brass
  0.18-0.55; notes with 3 dB or more inside 720 -> 365; fast edges (3 dB/s, 3 dB or more inside a note) 531 -> about
  262, what is left is the dynamic trim on legato targets and through printed hairpins, and the timpani.
- Timpani, harp, tam-tam and cymbals keep their envelope dynamics (no CC11); their slow shapes stay from 4 s.

## 2. Parked shorts (decision 2)
`SHORT_CC11_PARK = None`. Celli 338.5-340: c56 -41.6, c57 -31.6, c58 -36.7 dB; Violas 350.5-352: -46.5 / -37.4 /
-41.8. Still 4-5 dB over c56. Other CC + envelope pairs checked: swell cap (envelope half gone, the cap stays: Bassoon
1 / 2 capped swells 2-3 dB short), timpani CC7 + envelope (intact), theme accent removal + level steps (inert).

## 3. Timing (decision 4), range renders twice, second kept, then the full render
| | c57 | c58 |
|---|---|---|
| Violins I 56-87.9 S robust SD / over 40 ms (guard 12 ms) | 9 / 1 | 9 / 4 |
| Violins I 56-87.9 long notes front minus tail (guard 3 dB) | -1.9 | -2.1 |
| Violins I 56-127 S robust SD / over 40 | 12 / 6 | 13 / 7 |
| Violins I 536-576 S robust SD / over 40 | 17 / 7 | 17 / 7 |
| Violins II quarters 88-100, within 6 dB of own maximum | +220 ms | +9 ms |
| Violas quarters 88-100 | +160 ms | +51 ms |
| Violins II / Violas quarters 536-548 | not measured | +13 / +14 ms |
| Basses' eighths 104-124, peak after the beat (range render) | 138 ms | 83 ms |
Done: Marc spans 88-100 and 536-548 on Violins II and Violas; basses' repeat lead 0.06 s; `steady57_at.json` rows of
critic C #3; theme repeat gap 0.06 s; Violas 136 and Violins I 456 leads cut to about 0.10 s; Oboe 2 160 -0.10 s;
Trumpet 2 loud lead 0.09 -> 0.06 s. Span 536-576 did not improve (17 ms, 7 over 40).

## 4. Re-bows and the last chord (decision 5)
- Option N: `REBOW_MAX_S` 4.5 -> 5.2, frozen automatic points inside notes of 5.2 s or less dropped (printed bow
  changes kept): re-bow pieces 87 -> 62.
- Last chord: one bow on Violins I and II, CC11 falls to 14 by 727. Master per second over the fermata: c57 -48.8
  -48.7 -46.1 -44.5 -46.8 -47.2 -46.1 -51.8; c58 -46.1 -46.5 -48.6 -48.6 -48.2 -47.8 -51.2 -52.5 (largest rise +2.5 ->
  +0.5 dB). Violins I alone still moves 4 dB inside the held note (-52.2 / -56.5 / -51.8).
- Option A failed. Tested as re-bow pieces on alternating MIDI channels with 0.4 s overlap (`REBOW_OVERLAP`, range
  render): notes on channel 2 do not sound in Opus as loaded (Violins II silent through the last chord). Not shipped.
  The alias-instance form was not built.
- Holes of 6 dB for 80 ms (faults58): 16 of 87 -> 17 of 62.

## 5. Accents (decision 6, as changed by the coordinator on 11 and 15 Nov)
Resting ff CC11 104 (strings, winds) / 100 (brass) through `CC11_REMAP`, made up by the ff dynamic trim (+0.7
strings, +2.0 Violins I, +1.7 winds, +2.5 brass; fff anchors unchanged). `ACCENT_FLAT`: one flat CC11 rise for the
whole note, 0.3 s or longer, f or louder: strings 88 -> 95 / 104 -> 117, Violins I 88 -> 101 / 104 -> 113, winds 88
-> 105 / 104 -> 114, brass 88 -> 101 / 100 -> 110; x 0.75 from 9 accented staves at the onset, x 0.6 from 16.
Accent minus unaccented (same track, pitch, row, printed dynamic; first 0.3 s, envelope removed; `acc58.py`):
| family | c57 | c58 at f | c58 at ff | 2-5 kHz front excess |
|---|---|---|---|---|
| strings | +0.1 / +0.4 | +2.6 (quartiles 0.0 / +4.5, n 21) | +1.7 (+0.5 / +3.4, n 26) | -0.3 dB |
| winds | 0.0 | +1.2 (n 42) | +0.9 (n 71) | -1.6 |
| brass | +0.1 / 0.0 | +0.9 (n 51) | +0.5 (n 23) | -3.0 |
Per track (median, 3 or more matched): Violins I +3.3 (over the +3 limit), Violas +2.1, Contrabassoon +1.8, Violins
II +1.5, Oboe 1 +1.4, basses +1.3, Trombone 1 +1.2, Bassoon 2 +1.2, Clarinet 1 +1.0, Oboe 2 +1.0, the other winds
and brass +0.5 to +0.8, Bass clarinet +0.3, celli -0.8. Winds and brass are under the +1.5 aim (the staff scaling
acts on most of their accents); the string spread is as wide as the unaccented spread was in c57. sf / sfp marks do
not take the rule. Marc rows for string accents: not done.

## 6. Legato (decision 7)
`LEG_OVERLAP_S` strings 0.06, winds and brass 0.045 s. `SUS_ENTRY_AT` Violins II 62.5 / 68.5 / 70.5 / 76.5 / 82.5
and Violas 62.5 / 68.5 / 70.5 on Sus MAX. Legato velocity 96: not tested.

## 7. Other decisions
- 8: round-robin reset on every beat of the basses' eighths: range test identical to the shipped build to 0.1 dB
  (off minus on +1.0 dB, separation 6.5 dB, 2 of 28 under 3 dB); not adopted. Stac On Bow alias: not tested.
  Contrabassoon 536-544 and 632 on LegRep RRx4.
- 9: Horn 4 pp-layer region gain C3-F3 (`region_gain_db` `"dyn": ["pp"]`, 40 regions) did not work: F3 bars 19-20
  -40.1 dB against G3 bars 21-22 -52.0 (c57 -48.5 / -53.6). `soft_trim_db` Horn 4 mp 9.0, Clarinet 1 mp 3.5 / mf
  3.0, Violins II mf 1.0, Double basses pp 6.5.
- 10: Oboe 2 160, Trumpet 2 lead, celli 526 velocity 91 done. Keyswitch lead 0.15 s: not done.

## 8. Faults, c57 render -> c58 render (`faults_c57.txt`, `faults_c58.txt`, same script)
| | c57 | c58 |
|---|---|---|
| join holes (6 dB for 80 ms) | 25 | 30 |
| same-pitch repeats under 3 dB | 82 of 406 | 50 of 252 (the script skips led repeats: only 8 of the basses' are counted) |
| re-bow holes | 16 of 87 | 17 of 62 |
| long notes sagging 6 dB | 62 | 62 |
| pulse on a held note | 17 | 13 |
| pitches 4 dB out of line | 23 | 7 |
Master bars against c57: 23 more than 1.5 dB over (bar 172 +4.7, 74 +4.4, 179 +4.2, 171 +3.7, 15 +3.0), 17 more
than 1.5 dB under (bar 7 -7.8, 47 -4.0, 21 -3.2). Against c56: 39 over, 10 under.
Theme over the celli bars 15-22 per quarter: median +9.3, lower quartile +5.9 (c57 +4.4 / +1.7; target 3.9).

## Left audible (not patched with volume)
- Re-bow holes, 17 (Violins I 44 11.6 dB and 576 9.9; Violas, celli and basses in bars 6-13, 72-76 and the last
  chord, 7-13 dB).
- Horn 4 F3 12 dB over G3 at p (bars 19-22).
- Cor anglais bar 7 8.4 dB under c57 (-37.8 dB; master bar 7 -7.8): a +13 dB / +6.7 dB shape and row are gone.
- Horn 1 bar 111 -9.4 dB against c57 (a +13 dB shape on one p note).
- Basses' pedal bars 125-129 +5.3 dB over c57.
- Violins I recap theme bars 136-139 +3.7 dB over c57; theme now 9 dB over the celli at the median.
- String shorts still 4-5 dB over c56 (celli 338.5-340, Violas 350.5-352).
- Bars 171-174 and 179-180 +3 to +4.7 dB over c57 (Cello solo: its per-note shapes are gone, no CC11 phrase shape
  was written in their place).
- Capped swells of Bassoon 1 / 2 2-3 dB short; 62 short role rows dropped (1-5 dB on one or two notes each).
- Violins I accents +3.3 dB; wind and brass accents under +1.5 dB.

## Render conditions
- Lock: new waiter 15 Nov 15:02, held 15:29 to the end of `p8.sh`; nothing taken by hand.
- State guard: 0 stale at the start, after the build and before the render; Double basses stale after the range
  renders (rebuilt in full); after the render saves Trumpet 1 (main) and three pass-2 tracks were stale and were
  rebuilt in full (`p8.log`).
- Memory: the first render attempt was refused (21 GB of REAPER's 44 GB compressed). After a restart the render ran
  with `--force-memory` at 15 GB compressed; attack probe late or hole 0 (main and pass 2). REAPER 44 GB after the
  main render, 19 GB in pass 2. Disk 28 GB free after the render.
- Delivery: -19.8 LUFS integrated, LRA 14.9 LU, true peak -1.7 dBTP, limiter about 0.2 dB, p10-to-max span 18.1 dB,
  433.60 s. Master: -19.8 LUFS, LRA 23.2 LU, true peak -1.2 dBFS. No clipping.

## For Dan
`cycles/c58/ab/`: c57 then c58, bars 15-23 and bars 23-26, master and Violins I stem, one gain for both halves.

## Tools (all new keys off by default; with none set parts.json is byte-identical to c57's, checked)
`score_to_parts.py`: `VOL_SLOW_ONLY` `slow_max_db_s` / `slow_no_cc`, `LEVEL_TO_CC`, `ROLE_EDGE`, `UNI_ROLE`,
`HELD_DECRESC_CC`, `CC11_REMAP`, `ACCENT_FLAT`, `LEG_OVERLAP_S`, `SUS_ENTRY_AT`, `REBOW_SKIP_UNDER_S`, `REBOW_NONE`,
`REBOW_OVERLAP` (failed test, off), `FINAL_CC_FADE`. `build_reaper.py`: `ONSET_KEY`, region gain `"dyn"` and
`"all_db"`, a note's optional MIDI channel. `cycles/c58/actor_scripts/`: `lib58.py`, `tags58.py`, `env58.py`,
`envdiff58.py`, `rtmeas58.py`, `acc58.py`, `bars58.py`, `faults58.py`, `table58.py`, `abclips58.py`, `p1.sh`-`p8.sh`.

## Not done
Re-bow option A on an alias instance; Marc rows with row volumes for string accents; sf / sfp accents; legato
velocity test; Stac On Bow test on the basses; brass soft entry lead 0.045 s test; keyswitch lead 0.15 s; Cello solo
CC11 phrase shape and Main-mic alias; horn and trombone tongued-gap floor 0.12 s; Violins I mf trim; per-track accent
refit other than Violins I; MANUAL-GAPS (none tried).

## Not verified
The mp3 and clips by ear; whether the render at 15 GB compressed memory changed anything the probe does not see; loop
pulsing on the notes no longer split (4.7-5.0 s) and on the last chord's single bow beyond the level figures above;
the level of each CC11 offset that replaced a role or shape (slopes 0.30 / 0.21 / 0.29 dB per unit are family
values); entries of the brass after `ONSET_KEY` (expected 12-18 ms earlier); Oboe 1's accent rise under the staff
scaling; the 2 s role ramps by passage; the same-pitch repeat count on led notes.
