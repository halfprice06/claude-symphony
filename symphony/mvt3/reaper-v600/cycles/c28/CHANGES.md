# Cycle 28 (2026-11-18): role-edge carries at the edge (the c27 regression), trims on moved time, the trumpet solo, the Più allegro trumpets and trombone, balance, delivery rides, stops

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c27 render) and the coordinator's rulings 1-8 plus the scherzo notes (trims on moved time, net-level gate, +24 dB envelope limit, fff trims, headroom). Snapshot: `before/`. Scripts: `actor_scripts/` (`guard28.py` the in-note gate on the envelope, the CC7 lane or their sum, `netdiff28.py` the net-level diff gate, `ana28.py` the ruled targets on stems, `roles28.py` the roles.json edits, `parts2.sh`, `lockrun28.sh` the whole locked sequence; copies of c27's `deliv24.py`, `stops24.py`, `dynsteps.py`, `stepcheck.py`, `pdiff.py`). Logs: `logs/` (`guard28_env.txt`, `guard28_net.txt`, `guard28_cc7.txt`, `netdiff_vs_c27.txt`, `netdiff_vs_c26.txt`, `ana28.log`, `deliv.log`, `stops.log`), `phase.log`, `render.log`, `measure2.log` (re-delivery with the c28 rides).

## For Dan

- **Loudness -14 LUFS; the final chord is the loudest moment again** (0.6 dB over bar 223, 0.7 over bar 263; 223 and 263 tie).
- **The big moments got their instruments back.** Last cycle a pipeline change moved some section levels to the wrong note: the first violins lost 5.5 dB on the bar 223 arrival, the strings 3-5 dB on the final chord, the second horn was 8 dB too loud in bar 167. All are back where they were two cycles ago (within 0.6 dB on the stems).
- **The trumpet solo of bars 51-66 now leads.** Each phrase no longer swells on its first note and then drops; the clarinets under it are softer. The solo now stands about 7 dB over the loudest accompanying part (was 3 dB).
- **Più allegro (bar 248):** the trumpets' tenuto note no longer jumps out (Trumpet 2 is now level with its neighbours; Trumpet 1 is now 3.5 dB under them, a little too far), and the trombone's accented dotted quarters are held to their length instead of being clipped to a quarter (the gaps between them dip 4-5 dB instead of 8-10).
- **Balance:** the bass clarinet no longer tops the tutti in bar 261 (4 dB down); the violins' tune of bars 67-82 stands a little more over the violas and cellos.
- **Arrival and close:** bar 223 now stands 2.3 dB over the chorale that follows (was 0.7); the Largamente close (bars 271-273) is 1.4-2.4 dB under bar 255 (was 3-4).
- **The cut-offs of bars 6 and 204 ring a little longer again** (16 dB fall in 0.3 s, inside the target).
- **Not fixed:** the harp's level step at the chord of bar 239 (qn 952; 2.9 dB inside ringing notes); the double basses' soft re-bow dips of bars 43-50 (accepted: only below 150 Hz); the late second note of the accented brass slurs (bars 205, 243): the test of a new patch row was not run this cycle.

## Results (main render 09:15-09:27, re-delivered with the c28 rides)

- **Delivered (`mvt3-mockup-c28.mp3`):** -14.0 LUFS, LRA 11.0 LU, true peak -1.2 dBTP, p10 short-term -21.7 LUFS, limiter 5.2 dB (final chord), room bed -60.0 LUFS. First delivery with the c27 rides (`mvt3-mockup-c28-first.mp3`): the same integrated / LRA / TP / limiter.
- **Shared delivery spec on the mp3:** (1) -14.0 LUFS, -1.2 dBTP: met. (2) final -7.6; 223 -8.2, 263 -8.3 (lead 0.6 / 0.7), ff bars 264 -8.4, 5 / 255 -8.7; bar 277 (the final's own crescendo) -8.3: met. (3) f -> ff +3.4 dB: met. (4) p10 -21.7: met. (5) limiting 5.2 dB: met. (6) LRA 11.0: met.
- **mp3 stops at +0.3 s:** bars 2 / 6 / 94 / 113 / 166 / 204 / final 16.3 / 15.8 / 16.9 / 17.3 / 16.8 / 16.0 / 15.9 dB (c27 16.1 / 17.3 / 17.0 / 17.4 / 17.7 / 17.7 / 16.4). Bar 113 0.3 over the band.
- **Master:** -19.3 LUFS, LRA 23.9, sample peak 1.154 (float stem sum; c27 1.062: the final chord's strings back, +0.8 dB headroom used, the delivery limiter takes it). **Attack probe:** 0 late or holes.
- **REAPER memory:** 45 GB settled before the render (0 compressed), 46 GB after (7.5 GB compressed).
- **Lock:** 08:48:47-09:28:09, 39 min, no wait (start / settle 12 min, `--midi-only --tempo` build of all 31 tracks 1 min, no full rebuilds, state guard 0 stale, restart / settle 11, render 11, quit). Disk 43 GB free at the render.

| target (ruling) | c26 | c27 | c28 | goal |
|---|---|---|---|---|
| Horn 2 664.2-667.5 / Horn 1 same (1), band dB | 15.4 / 18.0 | 23.6 / 18.1 | 15.3 / 18.1 | c26 +-0.7 (met) |
| Violins I 888-892 / 896-899.9 (1) | 30.5 / 18.0 | 25.3 / 20.3 | 31.0 / 17.4 | met |
| Final chord 1108-1112: Vln I / Vln II / Va / Vc / Tpt 1 / Tbn 1 (1) | 32.6 / 34.5 / 31.7 / 30.6 / 34.1 / 33.8 | 27.6 / 32.5 / 27.7 / 27.7 / 31.2 / 32.4 | 32.7 / 34.5 / 31.7 / 30.6 / 34.1 / 33.9 | met |
| 263: Trumpet 1 / Violins II 1048-1050, Horn 3 1048-1052 (1) | 34.2 / 26.4 / 34.7 | 32.5 / 24.3 / 31.6 | 34.2 / 26.3 / 34.6 | met |
| Horn 1 860-863.7 / Horn 3 564-568 / Vln II 788-792 / Flute 1 156-158 (1) | 16.2 / 15.3 / 21.0 / 12.9 | 18.1 / 17.3 / 18.3 / 16.7 | 16.1 / 14.9 / 22.3 / 12.3 | met (Vln II +1.3) |
| master 1108-1112 / 888-892 / 1048-1050 | 45.2 / 44.9 / 43.1 | 44.0 / 44.7 / 42.5 | 45.3 / 45.1 / 43.4 | final back (+1.3 over c27) |
| trumpet solo targets minus head 200 / 216 / 232 (3) | -6.8 / -2.0 / -6.3 | -6.8 / -2.0 / -6.3 | -3.2 / +1.5 / -3.0 | -2..+1 (closer) |
| trumpet solo lead over the loudest other, median / p10 (3) | +3.0 / +0.2 | +3.0 / +0.2 | +7.3 / +4.4 | B sim +7.8 (met) |
| Trumpet 1 / 2 989 minus mean(988, 991) (3) | +3.3 / +4.1 | +2.6 / +3.2 | -3.5 / +0.7 | 0..+3 (Tpt 2 met, Tpt 1 overshot) |
| Trumpet 1 / 2 per-note range 984-998 (3) | 11.5 / 8.0 | 10.1 / 6.9 | 8.5 / 5.7 | 8 or less (Tpt 2 met) |
| Trombone 1 dotted-quarter join dips (3) | 8.0-9.3 | 8.4-10.0 | 2.7-4.9 dB | 5 or less (met) |
| Bass clarinet 1040-1047.8 vs Trumpet 1 (4) | 29.7 / 31.6 | 29.7 / 31.6 | 25.7 / 31.6 | -4 dB (met) |
| bars 67-82 violins over the loudest other, median (4; my band measure) | +0.6 | +0.6 | +2.8 | B sim +5.9 K (closer) |
| mp3 223 minus 228 (5) | | 0.7 | 2.3 | 2 or more (met) |
| mp3 271 / 272 / 273 minus 255 (5) | | -3.8 / -3.1 / -3.3 | -1.9 / -1.4 / -2.4 | within 1.5 (closer) |
| chorale 224 / 225 minus bar 62 (c24 fix) | | +3.9 / +2.7 | +3.1 / +0.8 | over (kept) |
| stops 6 / 204 (6) | 15.0 / 15.1 | 17.3 / 17.7 | 15.8 / 16.0 | 14.5-17 (met) |

## Gates (before the lock, on the final parts.json)

- **guard27 semantics (envelope only, `guard28.py --lane env`):** entry 1 (Oboe 1 851 +2.5: the envelope step stays, CC7 cancels it until the new note-on), inside 0, inside_dyn 0 (c27: 4 / 0 / 5). Listed: entry_hp 47, inside_hp 13.
- **Net level (envelope + CC7, notes ending 25 ms before the next note-on; coordinator / scherzo):** entry 14, inside 6, inside_dyn 8 (c26 data 45 / 3 / 12, c27 37 / 2 / 18). CC7 lane alone: 16 / 7 / 9. What remains: timpani roll CC7 shapes (10 of the 28), role steps at slurred note-ons carried in CC7 (Violins I 487.5 / 488 / 892, violas 15 / 16 / 1088, Flute 1 / Clarinet 1 136), trim steps at legato overlaps 25-40 ms before the new note-on (celli 951.5, basses 951.8, violas 823.5), the rate-limited carries at 3.0-3.2 dB/s inside the note (Violins I 896-899, Horn 3 565: the note is shorter than 2.5 dB/s allows), Bassoon 1 320 (c26 variant C swell).
- **Net-level diff gate (`netdiff28.py`, no span of 1 qn or more over 1.5 dB):** against c27 (`logs/netdiff_vs_c27.txt`, 68 spans) every span is a ruled change of this cycle (the carry corrections, the roles of rulings 3 / 4, Horns 3-4 / Violins II at 263, the bass clarinet CC7, the woodwinds' fff trims). Against c26 (`logs/netdiff_vs_c26.txt`) no span remains at a c27 carry window except Violins I 474.5-476.9 (+2.5: the 477 rise now spread at 2.5 dB/s over the note before), Violins II 788.3-789.5 (+1.9, 1.1 qn), Flute 1 1113-1116 (+2.5 in the final fade: the -2.5 cut's rise now starts 1 s before 1113.5) and the clarinets' fff trims; the other c26 differences are c27's accepted changes (`SOFT_DECRESC_KEEP` 0 decrescendos, passage levels, stopped horns).
- **Envelope range:** gain + role + largest trim reaches 24.0 (Horn 3, 1018), 23.6 (Trombone 1), 23.5 (Tuba), as in c27; REAPER's limit is +24. Not changed this cycle (no headroom loss; listed for c29).
- stepcheck: 0 steps inside notes.

## Changes (files and values)

- **Ruling 1 (role-edge carries, generic, `tools/score_to_parts.py` `ROLE_EDGE_IN_REST`):**
  - `edge_note_qn` 0.05: a note that starts at the edge (up to 0.05 qn after the edge ramp) is the edge's note (c27 left it out and took the note before, sounding across the edge only by its lead).
  - `carry_at_edge_qn` 0.5: the CC7 carry ramp sits on the edge's note-on only when that note starts within 0.5 qn of the edge; otherwise on the row's own edge ramp [x0, x1] (at least `carry_ramp_s` wide). CC7 holds the old level through the note at the edge.
  - `carry_rate_db_s` 2.5: an edge-ramp carry inside a held note moves no faster than 2.5 dB/s (a rise ends at the edge's ramp end, a fall starts at its start), so the carry passes the net-level in-note gate (3 dB/s). Example: Violins I 899.9 (+6) rises over 896-899.9 as c26 did.
  - `build/roles.json` (`actor_scripts/roles28.py`): Horns 3 and 4 [1048, 1056, +3] back; Violins II [1048, 1053.5, +2] (c26 carried +2 into the fff of 263; C's table had Violins II -2.0 there).
- **Coordinator's checks (scherzo notes), `tools/build_reaper.py`:** `TRIM_CC7_ONSET_QN` 0.15 / `TRIM_CC7_ONSET_PRE` 0.003: a change point of the CC7 trim lane within 0.15 qn after a moved note-on moves to 0.003 qn before it (the lane is on a 0.125 qn grid: Horn 1 744 played its first 20 ms 12.5 dB low, Clarinet 1 720 40 ms 8.3 dB low, Flute 1 872 30 ms 8.5 dB low). Net-gate entries 31 -> 15 from this alone.
- **`build/mix.json`:** fff trim raised to the ff trim on Flute 2 (-1.7 -> -0.7), Clarinet 1 (-0.6 -> 1.4), Clarinet 2 (-2.8 -> 1.2) (coordinator: no fff trim under ff on winds). Horn 1 (fff 1.9 < ff 2.6) and Trumpet 3 (12.6 < 14.1) left (CC1-layered brass, mvt1 c09 anchors).
- **Ruling 2 (gate items):** bassoons / contrabassoon 596 vol_set row holds 0 over 599-601.8 (as the cor anglais in c21); Oboe 1 851.46-851.69 and violas 775.26-775.95: CC7 holds the old level through the old note and steps at the new note-on (`_c28_comp`, violas' envelope reaches the mp level by 775.20 via vol_set); celli role [488, 495.9, +3] end ramp 1 -> 3.5 qn (2.4 dB/s, kept as a slow end ramp); celli 15.0 went with the edge fix. Harp 952: tried a printed-dynamic ramp (vol_set), but the pipeline's vol_guard (which reads vol_db only, not the trims) stretched the compensating rise ahead of the trim step; withdrawn (`C28_HARP=1` restores it), the 2.9 dB step at the 952 chord left.
- **Ruling 3 (trumpets, `build/score_config.py` c28 block):** Trumpet 1 solo heads 200 / 216 / 232 CC1 capped at 42 / 43 / 43 (start + 6); legato targets CC1 +4 over 202.5-215, 218.5-231, 234.5-239 (the printed crescendo 239-244 untouched); roles Clarinet 2 [200, 266] +5 -> +1, Clarinet 1 [200, 264] -4 -> -6, Trumpet 1 [200, 264] +3.2 -> +5.2. Più allegro: CC1 lift +12 -> +6 (984.5-999.9), 989's CC11 bump removed, CC1 -12 / -6 on 989 (Trumpet 1 / 2) to the 991 note-on, 991 CC11 -5 dB (k 20, 990.70-991.75). Trombone 1 gap_set 0.05 s (min 0.95 qn) over 984-1080 with the 0.12 s floor skipped there (`skip_long`): the dotted quarters at 985 / 990 / 993 / 1001 / 1006 play 1.21 qn (were 1.00).
- **Ruling 4:** Bass clarinet CC7 81 over 1039.70-1047.87; roles violas [264, 292] 4 -> 1, celli 5 -> 3, Violins II [264, 328] 3 -> 4, Violins I [263.5, 328, +1] added.
- **Ruling 5 (delivery only):** ride row [(899.5, 0), (900, -2), (911.9, -2), (912.5, 0)] (C's v6; B's 892-901 +1 would lower the chorale entry against the trumpet solo of bars 61-62, the c24 fix); the 1079.5 row -3.5 -> -2.0 over 1080-1096.
- **Ruling 6:** celli stop ceilings at bars 6 (20.944) and 204 (813.86) at half depth: 98 -> 85, 97 -> 84 (were 72 / 70).

## Rejected or deferred

- **Ruling 7 (accented slur second notes, "Leg Slur Accent MAX"):** not range-tested. The row is an Opus state change on four brass tracks (full rebuild in, and back out if rejected); with two cycles left the lock budget went to the regression fix and a single safe build. Open for c29 (MANUAL-GAPS #1).
- **Ruling 8 (basses' pp re-bow holes):** accepted as A recommends (master 30-150 Hz dip 5 dB, nothing above 150 Hz); C's drop of the 170.86 re-bow not tried.
- **Harp 952 step:** the instrument-side ramp was undone by the pipeline's vol_guard (it reads vol_db only); velocity alone cannot remove the trim step. Left audible (2.9 dB at a new chord, inside ringing notes) and reported.
- **Phrase arcs in the Allegro (C #6):** not this cycle.
- **fff trims under ff on Horn 1 / Trumpet 3:** left (CC1-layered brass anchors); only the woodwinds changed.

## Faults introduced or left

- Trumpet 1's tenuto 989 now 3.5 dB under its neighbours (CC1 -12 too much; -6 to -8 would land it).
- Bar 113 stop 17.3 dB (0.3 over the band; unchanged from c27).
- Net-level in-note items listed above (14 / 6 / 8), most of them role or trim steps at slurred note-ons.
- Flute 1 +2.5 dB in the last 1.5 qn of the final fade against c26 (the carry's rate limit starts the rise early).
