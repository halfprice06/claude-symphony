# Cycle 27 (2026-11-18): Dan's no-fader rule (role edges, trims in CC7, gate), the muted second theme, string chord fronts and soft heads, stopped horns, inner lines, bar 263, brass legato, wind solos

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c26 render) and the coordinator's rulings 1-8, the disk update (47 GB free) and the Movement I c62 notes (room bed, ramp-move limit). Snapshot: `before/`. Scripts: `actor_scripts/` (`guard27.py` the extended gate, `ana27.py` the ruled targets on ranges / renders, `cc7test.py` the CC7 range test, `simlev27.py` level-only simulation on stems, `roles27.py` the roles.json edits, `merge27.py`, `q27.py` / `notes27.py` / `rests27.py` data views; lock phase `lockrun.sh`, `p2.sh`, `p3.sh`, `after.sh`). Logs: `logs/` (`ana_CTRL.log`, `ana_T1.log`, `ana_T2.log`, `cc7test_T1.log`, `guard27_final.txt`, `render/`), `phase.log`, `role_moves_over_1qn.txt`.

## For Dan

- **Loudness is still -14 LUFS and the final chord is still the loudest moment** (0.5 dB over bar 223 and 0.6 over bar 263; bars 223 and 263 tie, both printed fff).
- **No more fader moves on single notes from the dynamic markings.** The level differences we give each printed dynamic now happen inside the instrument (its volume controller) instead of on the mixer fader, and the passage-level changes no longer start on a note: they sit in the rest before it, or the instrument carries them across a slur. Levels are the same as before (measured within 0.4 dB). Four small fader moves at note starts and five at slurred dynamic changes remain (1.5-3.5 dB, listed below).
- **The muted second theme (bars 171-186) is smoother.** The cor anglais now crossfades each slurred note into the next instead of starting each one fresh: the dips at the joins in the full mix went from 3 joins over 3 dB (largest 5.1 dB) to 2 (largest 3.9 dB).
- **The accented string chords (bars 1, 5, 147, 276) now hit together.** The second violins play the same accented sample as the firsts and arrive with them (before: 75-165 ms late, with a soft front). Violas and cellos are led in earlier too.
- **The soft string themes start on time.** The violin / viola / cello entries of bars 67, 107, 123 and 187 were 140-220 ms behind the harp and basses; now mostly 0-115 ms (cellos at 488 and violas at 937 still 140 / 210 ms late).
- **The stopped horns now fade where the score says** (bars 138 and 168: they fall 7-14 dB; before they stayed flat or swelled). The soft trombone and clarinet crescendos now grow 3-4 dB on the held note (before about 1 dB).
- **Inner lines:** the Horn 1 counter-line in bars 67-74 is 3 dB more present, the running figure under the last chorale (bars 259-262) 2 dB more, the countersubject of bars 159-165 about 1.5 dB more, and the cellos' line in bars 235-237 4 dB more against the basses.
- **Smaller:** the flute run of bar 43 lost three of its four holes; the bassoon's join at bar 129 no longer dips; the trumpet notes in bar 213 and the horn at bar 255 are on time; the cellos ring less after the stop of bar 204; theme B at bar 212 is no longer among the twelve loudest bars (c26: 0.12 LU under bar 223).
- **Not fixed:** the double basses' soft pedal of bars 43-50 still dips at each new bow (neither fix helped); bar 263 still steps only 0.9 dB over bar 262 (three wind parts get softer at the fff, and the cure tried on them did little); four of the cut-offs are now a little drier than the target (17.3-17.7 dB fall in 0.3 s, target 14.5-17).

## Results (main render 01:19-01:34)

- **Delivered (`mvt3-mockup-c27.mp3`, rides refit on the render master, see below):** -14.0 LUFS, LRA 11.0 LU, true peak -1.1 dBTP, p10 short-term -21.7 LUFS, limiter 4.4 dB (final chord), room bed -60.0 LUFS (Movement I's implementation). First delivery (`mvt3-mockup-c27-first.mp3`, the rides as built): -14.0 / LRA 11.1 / -1.1 dBTP; final over 223 only +0.4 and bar 39 tied with 223.
- **Shared delivery spec on the mp3:** (1) -14.0 LUFS, -1.1 dBTP: met. (2) Final -8.0; 223 -8.5, 263 -8.6 (lead 0.5 / 0.6; 223 / 263 tie), next ff bars 264 / 255 -8.7: met (bar 277, the final's own crescendo, -8.3 as in c26). (3) f -> ff +3.5 LU (f -15.2, ff -11.7): met. (4) p10 -21.7: met. (5) climax limiting 4.4 dB: met. (6) LRA 11.0: met.
- **mp3 stops at +0.3 s:** bars 2 / 6 / 94 / 113 / 166 / 204 / final 16.1 / 17.3 / 17.0 / 17.4 / 17.7 / 17.7 / 16.4 dB (c26 15.3 / 15.0 / 16.3 / 16.8 / 15.7 / 15.1 / 15.9). Four are 0.3-0.7 dB over the 17 dB top of the band (fault left).
- **Master:** -19.6 LUFS, LRA 23.4, sample peak 1.062 (float stem sum). **Attack probe:** 0 late or holes.
- **Gate (`guard27.py` on the rendered parts.json, `logs/render/guard27.log`):** inside unprinted 0; entry-window unprinted 4 (Oboe 1 851 +3.0, Harp 951.5 -3.5, celli 15.0 -2.4 (the role step 4 ms before the quarter's note-off), celli 496 -1.8); inside_dyn 5 (Bassoons 1-2 / contrabassoon 600 -1.7, harp 951.9 -3.5, violas 775.4 +1.9). Listed, not gated (printed hairpins, ruling 1): entry_hp 52, inside_hp 17. On the c26 data the same gate gave entry 187, inside 2, inside_dyn 10, inside_hp 131. stepcheck: 0 inside-note steps. The gate still exits 1: the render went ahead with these nine left (not fixed in time under the lock; next cycle).
- **REAPER memory:** 45 GB settled before the render (0 compressed), 46 GB after (1.5 GB compressed).
- **Lock:** 00:18:35-01:36:40, 78 min (waited 32 min behind Movement I). Start / settle 12, CTRL range 9, T1 build (Violins II full rebuild) + range 12, T2 build + range 6, final parts run 3, final build (Violins II full rebuild), state guard 2 stale (Horn 4, Violoncellos: attack values rewritten on save) rebuilt in full, restart / settle 11, render 15, quit. Range stems deleted after use (9.5 GB). Disk 47 GB at the render.

| target (ruling) | c26 | c27 | goal |
|---|---|---|---|
| gate entry-window unprinted / inside / inside_dyn (1) | 187 / 2 / 10 | 4 / 0 / 5 | 0 (not met) |
| printed-hairpin moves in notes, inside_hp (1) | 131 | 17 | listed |
| stopped horns fall over the decrescendo, Hn 3 / 4 / 1 / 2 (1) | 3.1 / -1.0 / 3.5 / 5.1 | 14.2 / 7.4 / 10.8 / 11.8 dB | 7-10, no rise (met; Hn 3 deeper) |
| soft crescendo change on the held note, Tbn 1 / 2, Cl 304 / 540 / 942, Hn 1 324, Tpt 1 720 (1) | +1.3 / +1.5, +1.0 / +0.6 / -3.6, -1.3, -1.0 | +4.0 / +4.3, +3.1 / +1.8 / -1.2, +1.3, +0.3 | +3 (trombones, Cl 304 met) |
| cor anglais join dips, stem >= 3 dB / master >= 3 dB (max) (2) | 7/22 / 3/22 (5.1) | 4/22 / 2/22 (3.9) | 0 / under 2.5 (closer) |
| Violins II -3 dB time re beat at 0 / 16 / 584 / 1104 (5) | +95 / +165 / +75 / +80 ms | 0 / -20 / -45 / -10 | within 40 of Violins I (met) |
| Violins II front minus body (5) | -5.8 / -8.6 / -3.7 / -5.8 | +1.6 / -1.8 / -1.1 / -1.2 | -2 or higher (met) |
| soft heads pc 264 VlnI/VlnII/Va/Vc | +189 / +146 / +202 / +197 | +164 / +115 / +94 / +21 | under +90 (partly) |
| soft heads pc 424 / 744 (VlnII, Va) / 488 / 937 | +138..+214 / +161, +168 / +219 / +240 | -2..+115 / +67, +24 / +139 / +213 | under +90 (partly) |
| Horn 1 minus violins 264-296 per 8 qn, 300-6000 Hz (4) | -15.3 / -10.5 / -10.1 / -11.2 | -12.3 / -7.4 / -7.0 / -8.0 | +3 dB (met) |
| running figure minus chorale 1036-1048 (3) | -8.7 / -5.8 / -10.7 | -6.8 / -3.7 / -8.7 | +2 (met) |
| countersubject minus tune 632-656 (4) | -6.8 / -8.7 / -7.2 | -5.5 / -7.0 / -5.9 | closer (met) |
| celli minus basses 936-948 (my band; B's K measure differs) (4) | +5.8 / +4.5 / +5.6 | +9.9 / +8.5 / +9.6 | +4 (met) |
| master 263 first quarter minus loudest of 262 (3) | +0.2 | +0.6 | +2 (not met) |
| Bassoon 1 / Flute 2 / Bcl / celli at 263 (3) | -6.5 / -4.5 / -4.0 / -4.3 | -5.4 / -3.5 / -3.1 / -0.5 | no fall (celli met) |
| Trumpet 1 legato pc 850 / 851 / 852 / 973 (6) | +34 / +62 / +90 / +70 | -10 / -4 / -30 / +16 | under +50 (met; 970 +152 left) |
| Horn 1 pc 818 / 819.5 / 821.5 / 1014 (6) | +132 / +88 / +101 / +44 | +130 / +46 / +75 / 0 | under +50 (partly) |
| Trumpet 1 / 2 per-note range 984-998 (6) | 12.6 / 7.1 | 10.9 / 6.9 dB | 6 (closer; 989 / 991 now +5 over 988) |
| basses re-bow dip / rise 170.9 / 181.7 / 190.5 (7) | 16.4 / 6.5 / 5.3; +2.8 / +1.8 / +6.7 | 16.2 / 6.5 / 5.3; +3.1 / +1.8 / +6.7 | under 4 (not met; c26 data kept) |
| celli stop +0.3 s drop at 5 / 21 / 813.9, stem (8) | 10.1 / 10.0 / 9.3 | 14.4 / 14.3 / 18.8 dB | lower ring (met) |
| Flute 1 run join dips >= 3 dB (8) | 4/9 (max 7.8) | 1/9 (170.0 7.1) | none (closer) |
| Bassoon 1 joins 320 / 514 (8) | 8.9 / 7.9 | 8.9 / 2.1 | 5 (514 met) |

## Range pass (under the lock)

CTRL = the c26 project as saved; T1 = all c27 data with cor anglais variant a, Violins II on "Sus Marc LITE", basses variant a (lead), trims in CC7 on Flute 1 and Trombone 1 only; T2 = T1 with cor anglais variant b, Violins II on Sus MAX with a 0.12 s lead, basses variant b (CC7 counter-shape), trims in CC7 on every track. Same starts as c26 (-3, 263.25, 455.75, 535.25, 679.25, 831.25, 967.75; T2 four of them). CTRL matched the c26 render within 0.3 dB on every measure above.
- **CC7 law (ruling 1, B #5):** Flute 1 and Trombone 1 with their trims in CC7 (envelope at gain + largest trim, up to +16.6 dB): per-note level change against the envelope + CC7 model, residual median 0.00 dB, p90 0.44 / 0.39 dB, the same as tracks left on the envelope (Flute 2 0.21, Oboe 1 0.33). Passed: `dyn_trim_to_cc7` all.
- **Cor anglais (ruling 2):** a (Leg Slur MAX, Sus MAX on long notes): stem 10/22 joins over 3 dB (max 7.0), master 5/22 (max 5.8): worse. b (Sus MAX, 0.10 s crossfades): stem 4/22 (max 4.1), master 2/22 (max 3.9). Adopted b.
- **Violins II chords (ruling 5):** marc: -3 dB points -80 / -20 / -45 / -10 ms, front minus body +1.4 / -1.8 / -1.1 / -1.3; sus + 0.12 s lead: -10 / -150 / +120 / +30 ms, front -4.2 / -6.0 / -5.4 / -2.5. Adopted marc.
- **Basses re-bows (ruling 7):** a (0.10 s lead): dips 16.1 / 6.4 / 4.9, rises +3.1 / +4.4 / +7.2; b (CC7 counter-shape 127 -> 74 / 93 / 60 over +0.45..+1.6 s): dips 16.2 / 7.6 / 6.3, rises +3.3 / +3.3 / +5.2; CTRL 16.4 / 6.5 / 5.3, +2.8 / +1.8 / +6.7. Neither is better: the c26 data kept (`C27_CB` "0"). The release cap critic A blamed is already 500 ms at pp / p in mix.json.
- Every other T1 result carried to the render within 0.5 dB / 20 ms (`logs/ana_T1.log` against `logs/render/ana27.log`).
- The final parts.json is a fresh score_to_parts run of the config defaults (CA b, V2 marc, CB 0); after the lock a second fresh run gave identical tracks, and its ride rows (the refit) are in build/parts.json.

## Changes (files and values)

- **Ruling 1 (Dan's rule):**
  - `tools/score_to_parts.py` `ROLE_EDGE_IN_REST` (generic, default on, `{"min_gap_s": 0.012, "max_ramp_qn": 0.5, "carry_qn": 16, "carry_ramp_s": 0.25}`): each roles.json edge ramp that overlaps a sounding note moves into the rest before the note nearest the edge (within 1 qn of it); with no rest there, the envelope edge moves to the nearest rest within 16 qn of that note (before a rise, after a fall) and CC7 carries the difference between that rest and the edge (a 0.25 s CC7 ramp centred on the edge's note-on). Played note spans come from the previous run's parts.json (env `STP_ROLE_SPANS`); run score_to_parts twice after note changes. End-ramp rows become shapes (slow end ramps of 2.5 dB/s or less kept). Not on timpani / percussion / harp. parts.json `role_edge_moved` (18 moves over 1 qn, all but one CC7-compensated: `role_moves_over_1qn.txt`), `role_edge_join` (edges left in place: 1113.5 final-fade edges and some legato edges with no rest within 16 qn). The Movement I kit warning (uncompensated moves of up to 19 qn) applies to moves without CC7: those are limited to 1 qn here; a first build with an unlimited carry wanted CC7 holds up to 154 qn (harp), so the carry is capped at 16 qn and the harp left out.
  - `tools/build_reaper.py`: mix.json `dyn_trim_to_cc7` (`TRIM_CC7`, `cc7_lane()`; envelope = gain + vol_db + largest trim, CC7 = lane x 10^((trim - largest) / 20), held in rests); `SOFT_DECRESC_KEEP` 0.5 -> 0 (env `BUILD_DECRESC_KEEP`). `build/mix.json` `dyn_trim_to_cc7` {"tracks": "all"} (families timp / perc / harp / harm excepted).
  - `build/score_config.py` c27 block: CC11 -4 dB (k 20) at the start of the soft crescendos Horn 1 324, Trombones 1-2 880, Trumpet 1 719-724, Clarinet 1 304 / 540 / 942 (`cc_scale`); stopped-horn CC11 ceilings Horns 3-4 127 -> 50 over 548.25-551.6/551.88, Horns 1-2 87 -> 35 over 668.2-671.9, held to the note end; celli 15.9 role window (15.640, 15.660) in the new rest.
  - Gate `actor_scripts/guard27.py` (entry window and no-edge inside moves; fp / sfp falls only exempt).
  - Celli 870.4 and 951.5: carried by the trims in CC7 (they were trim steps); neither appears in the final gate.
- **Ruling 2:** cor anglais variant b: `INSTR_POST onset_lead` 0.10 s on every note after the first of each span (683-694, 715-728), ends kept (score_config `C27_CA` "b").
- **Ruling 3:** roles.json Horns 3-4 [1032, 1048] 3 -> 0, Violins II 2 -> 4, Clarinets 1-2 +2 over 1031.85-1047.85 (`roles27.py`); celli CC7 95 over 1033-1047.84 (in over 1032.33-1033); mix.json celli loud_eq [1030, 0], [1032, 1] -> [1046, 0], [1047.85, 1]; Bassoon 1 / Flute 2 / bass clarinet CC11 +8 for the first 0.5 s of the 1048 note (little effect: -6.4 -> -5.4 dB on Bassoon 1).
- **Ruling 4:** roles.json Horn 1 [263.72, 295.75] 4 -> 7, Clarinets 1-2 +2 over 631.0-659.86 (the c25 clarinet cc_scale there removed); CC7 passage levels basses 90 (263.4-319.65) and 80 (935.35-951.854), Horn 1 90 and violas 101 (631.3-659.80 / 659.69); ride -1 dB over 840.5-856.
- **Ruling 5:** Violins II on "Sus Marc LITE" at 0 / 16 / 584 / 1104 (v92, v108 at 1104, lead 0.085 s, CC11 step 0.06 s ahead, `no_pre_cap`); violas and celli onset_lead 0.12 s at 16 / 584 / 1104; the quarter at 15 ends 0.13 s early on Violins II / violas / celli; CC11 fronts (+10 units, -0.06..+0.25 s, gone by +0.45 s) on the slur heads 264 / 424 (Violins I, II, violas, celli), 744 (Violins II, violas), 488 (celli), 937 (violas). StacSl row not tried (MANUAL-GAPS c27).
- **Ruling 6:** leg_leads.json Trumpet 1 851 / 973 +0.06, 850 / 852 / 970 / 996 +0.04, 989 +0.06 (Trumpets 1-2); Horn 1 818 / 821.5 / 1014 +0.06, 819.5 / 994 / 1010 +0.04; Trumpets 1-2 CC1 +12 over 984.5-999.9 (ceiling 110); 989's CC11 bump +24 -> +12.
- **Ruling 7:** both variants range-tested, neither adopted.
- **Ruling 8:** celli CC11 ceilings at the stops of bars 2, 6, 204 (C's values); Flute 1 variant C (169.5 / 170 / 173 on Sus MAX, 0.06 s early, 0.011 s overlap); Bassoon 1 320 added to variant C; Bassoon 1 514 v100, 0.06 s lead, the half note ending 0.09 s later.
- **Delivery:** `tools/deliver_master.py` room bed replaced by Movement I c62's implementation (same -60 LUFS; ours had a Butterworth low cut -3 dB at 84 Hz and seed 20261118, theirs (f/84)^4 / (1 + (f/84)^4), -6 dB at 84 Hz, seeds 6201-6203; sample peak -48.8 -> -49.1 dBFS, no delivery figure moved). Ride refit on the c27 master (score_config): the 888 arrival -8.4 -> -8.8, bars 39 and 248 -0.6 dB.

## Rejected or deferred

- Cor anglais variant a, Violins II Sus MAX + 0.12 s lead, basses variants a and b: range numbers above.
- Rate-limiting the printed hairpins: not done (ruling 1; B: stems follow the print).
- "StacSl Leg BC + Slur + Port MAX" on the soft heads: deferred (MANUAL-GAPS c27).
- The nine gate items left (4 entry, 5 inside_dyn): not fixed this cycle.
- Trumpet 1 at 970 (+152 ms) and Horn 1 818 (+130 ms): the leads did not move them.

## Faults introduced or left

- Stops at bars 6 / 113 / 166 / 204 fall 17.3-17.7 dB at +0.3 s (0.3-0.7 over the band; c26 15.0-16.8).
- Trumpets 1-2 989 / 991 now about +5 dB over 988 / 992 in the Più allegro slur (the CC1 +12 lifted the targets 7-9 dB, and the tenuto with them).
- Horn 3's stopped decrescendo at 548 falls 14 dB (target 7-10).
- The gate's nine remaining items, the basses' re-bow holes, the 263 step.
