# Cycle 29 (2026-11-18): legato holes on the sustain row, solos over their accompaniment, the muted trumpet / cor anglais unison, delivery rides, horn pans, envelope headroom, net-level cleanup

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c28 render) and the coordinator's rulings 1-8. Snapshot: `before/`. Scripts: `actor_scripts/` (`lockA29.sh` / `lockB29.sh` / `lockC29.sh` the locked sequence, `jt29.py` join dips / onsets / fronts, `ana29.py` the ruled targets, `roles29.py`, `mix29.py`, `envmax.py`, `nd.py`; copies of c28's `guard28.py`, `netdiff28.py`, `deliv24.py`, `stops24.py`, `dynsteps.py`, `pdiff.py`, `rr.py`, `wait_lock.py`). Logs: `logs/` (`guard29_net.txt`, `netdiff_vs_c28.txt`, `envmax.txt`, `ana29_c28.log`, `ana29_c29.log`, `deliv.log`, `stops.log`), `jt_c28.txt` / `jt_CTRL.txt` / `jt_VAR.txt` / `jt_c29.txt`, `phase.log`, `render.log`.

## For Dan

- **Loudness -14 LUFS, final chord still the loudest moment** (0.5 dB over bar 223, 0.7 over bar 263).
- **Smoother slurred melodies.** The trumpets' "molto espressivo" line at bar 243 had a 9-13 dB hole at every note change and arrived late; the cor anglais solo of bars 175-186 had two 8 dB holes; the horns' accented F1 head motive (bars 37, 145, 19) had late, dipping second notes. These notes now play on the plain sustain samples with a short crossfade between notes: the holes are 0-2.5 dB (trumpets), 0-3 dB (cor anglais, two joins 5-6 dB) and gone on the third horn. One spot (first horn, bar 205) got slightly worse in the test and was left as it was.
- **The trumpets' bar-243 line is now 4-6 dB louder than before** on its long notes (they used to sag under the first note; now they are level with it). Listen for whether it now sits too far forward.
- **Wind solos come through.** Flute, clarinet and oboe solos of bars 43-50 now stand 5-15 dB over the strings (were level with them); the first violins' harmonic plays as a soft non-vibrato sound. The oboe solo of bars 95-97 leads its accompaniment by 5-14 dB (was level).
- **Muted trumpet and cor anglais stay together** in bars 171-182: the trumpet no longer drops out on two notes or pops out on the top G (note-to-note spread 10 dB -> 4 dB).
- **Bar 271 arrival is heard again** (+1.9 dB over c28 on the mp3); bars 272-273 are within 0.6-1.3 dB of bar 255.
- **Bar 113 cut-off rings a little longer** (15.3 dB drop, in the target band; was 17.3).
- **Horns are spread a little across the left side** instead of one point (levels unchanged within 0.4 dB).
- **Trumpet pickups in bars 91-92 and 277** are now separate from the accented note that follows (3-6 dB, was 0).
- **Not fixed:** the cut-off of bar 166 now drops 17.6 dB (0.6 over the band; nothing ruled changed there); Trumpet 1's tenuto at bar 248 is 1.3 dB under its neighbours (was 3.5).

## Results (render 11:28-11:42)

- **Delivered (`mvt3-mockup-c29.mp3`):** -14.0 LUFS, LRA 10.8 LU, true peak -1.2 dBTP, p10 short-term -21.4 LUFS, limiter 5.2 dB, room bed -60.0 LUFS.
- **Shared delivery spec on the mp3:** (1) -14.0 LUFS, -1.2 dBTP: met. (2) final -7.6; 223 -8.1 (lead 0.5), 263 -8.3 (0.7), 264 -8.4, 5 / 255 -8.7; 223 / 263 tie (0.1): met. (3) f -> ff +3.7 dB: met. (4) p10 -21.4: met. (5) limiting 5.2 dB: met. (6) LRA 10.8: met.
- **mp3 stops at +0.3 s:** bars 2 / 6 / 94 / 113 / 166 / 204 / final 16.3 / 15.8 / 17.0 / 15.3 / 17.6 / 16.0 / 15.7 dB (c28 16.3 / 15.8 / 16.9 / 17.3 / 16.8 / 16.0 / 15.9). Bar 166 0.6 over the band.
- **Master:** -19.2 LUFS, LRA 24.0, sample peak 1.161 (float stem sum). **Attack probe:** 0 late or holes.
- **REAPER memory:** 45 GB settled before the render (0 compressed), 46 GB after (13 GB compressed).
- **Lock:** 10:47:31-11:43:34, 56 min, no wait (start / settle 12 min, range CTRL 3, `--midi-only --tempo` build (Trumpet 1 fully rebuilt for its region gain) + `--mix-only` 1, range VAR 3, Horn 1 818 revert (one score_to_parts run, 3.5 min) + Horn 1 build, Horn 4 full rebuild (state guard: 16 stale runtime attacks), restart / settle 11, render 13, quit). Disk 36 GB free at the render.

| target (ruling) | c28 | c29 | goal |
|---|---|---|---|
| Trumpet 1 / 2 join dips 970 / 973 / 978 (1; my measure, 100 ms smoothing) | 4.7 / 6.3 / 3.0; 8.5 / 7.7 / 8.2 | 2.5 / 2.0 / 0.6; 1.2 / 2.3 / 1.7 | 5 or less (met) |
| Horn 1 join dips 970 / 973 / 978 (1) | 2.8 / 1.4 / 1.4 | 0.9 / 0.3 / 0.4 | met |
| master dips at 970 / 973 / 978 (1) | 3.0 / 0.8 / 1.4 | 0.8 / -1.2 / 1.9 | under 3 (met) |
| Trumpet 1 / 2 / Horn 1 note p90 970-978 vs head 968 (1) | -2.3..-3.9 / -0.3..-2.7 / -1.1..+2.0 | +1.2..+2.1 / +3.0..+4.8 / +0.3..+3.3 | body +-2 of c28: not met (+4..+7 on the trumpets; the sag under the head is gone) |
| Trumpet 2-5 kHz front - body (1) | -3.0..+24.4 | -10.5..+15.8 | not brighter (met) |
| cor anglais 699-740 stem dips >= 3 dB / master dips >= 3 dB (1) | 5 / 3 (max 5.0) | 3 (701 6.3, 734 5.3, 704 3.0) / 2 (3.3, 3.0) | master under 3: closer (max 5.0 -> 3.3) |
| Horn 3 146 / 578 / 579.5 / 580 dips; Horn 1 74 (1) | 3.9 / 3.1 / 4.2 / 5.5; 4.4 | 0.3 / -1.0 / -3.8 / 0.0; 2.4 | met |
| Horn 1 818 (range VAR vs CTRL) (1) | 3.7 dip, front +10.5 | VAR 4.4, front +15.3 -> rejected, c28 data kept | |
| trumpet minus cor anglais per note 680-728 (3) | median -3.4, range -7.0..+3.1 | median -3.0, range -4.9..-0.9 | range under 6 (met) |
| Flute 1 / Clarinet 1 / Oboe 1 lead per 2 qn, bars 43-48 (2) | -4.2..+7.4 / -3.1..+8.7 / +3.3..+9.8 | -0.3..+11.6 / +1.0..+14.8 / +1.5..+11.8 | B sim +1.4..+11.8 (met but Flute 1 168 -0.3) |
| Oboe 1 lead 376-388 (2) | -5.7 / +1.1 / +8.4 / +10.3 / +3.3 / -3.8 | -3.7 / +5.1 / +11.0 / +14.3 / +6.3 / -1.1 | +2 dB per window (met) |
| Violins I 168-199 (2) | 2.5 | -4.4 (-6.9 dB: role -6, CC1 0 about -0.9) | |
| mp3 271 / 272 / 273 minus 255 (4; in-bar maxima) | -4.0 / -1.4 / -2.4 | -2.1 / -0.6 / -1.3 | within 1.5 (272, 273 met; 271 +1.9 over c28) |
| bar 113 stop (4) | 17.3 | 15.3 | 14.5-17 (met) |
| horn levels, whole piece / bars 9-25 (5) | | Horn 1 +0.06 / +0.17, Horn 2 -0.03 / 0, Horn 3 -0.33 / -0.36, Horn 4 +0.06 / +0.05 dB | within 0.5 (met, no stem fix) |
| horn L/R level difference (5) | 3.5 / 3.2 / 3.2 / 2.8 dB | 2.6 / 3.2 / 4.1 / 4.8 dB | spread |
| Trumpet 1 989 - mean(988, 991) (6) | -3.5 | -1.3 | 0..+3 (closer) |
| Trumpet pickups: quarter separation 362 / 366 / 1106 (6) | -3.6..+4.8 | +3.0..+12.0 | 4 or more (Tpt 1 / 2 met; Tpt 3 at 362 / 366 3.0-3.1) |
| Trumpet 3 1048 over 1046-1047.8 / level at 1048 (6) | +0.5 / 29.8 | +0.6 / 31.3 | +1.5 dB level |
| envelope maximum (7) | 24.0 (Horn 3) | 23.5 (Horn 3 / Trombone 1 / Tuba) | 23.5 or less (met) |

## Gates (before the lock, on the final parts.json)

- **Net level (envelope + CC7, notes ending 25 ms before the next note-on):** entry 13 / inside 2 / inside_dyn 4 (c28 14 / 6 / 8). Of these, 10 are timpani roll shapes (exempt). Left: Flute 1 136 (-1.6, a step at the slur head), Violins I 487.5 / 488 / 892, violas 15 / 16 / 823.5 / 1088 (role / printed steps at note-ons), violas 823.55 (1.7 dB over 0.01 qn). Gone: celli 951.48, basses 951.78, Clarinet 1 135.77, Bassoon 1 320, Violins I 896-899, Horn 3 565.
- **Net-level diff against c28 (`logs/netdiff_vs_c28.txt`, spans of 1 qn or more over 1.5 dB):** 34 spans, all ruled: the roles of ruling 2 (bars 43-50 and 95-97), and four ruling-8 carry conversions: Horn 3 563.9-566.6 +2.9 dB (the role's return now a step at the mf note-on 564, was a 2.8 dB/s rise inside it), Violins I 897-900 -3.7 (the +6 now a step at the 900 note-on), Violins I 474.5-478 -3.3 (the rise now in the rest after 477), Flute 1 164.4-168.2 -3.2 (the held note before the solo no longer swells by +5 dB inside it; the solo's +2 dB starts in the rest at 168).
- **Envelope maximum:** 23.5 dB on Horn 3 (shifted 0.5 dB into CC7), Trombone 1 (0.1) and Tuba.

## Changes (files and values)

- **Ruling 1 (`build/score_config.py` c29 block, parts t243 / ca / hn):** `ART_SPANS` on the sustain row and `INSTR_POST` `onset_lead` 0.10 s `set` on every note after the first (each note keeps its end, so it overlaps the next note-on by 0.10 s), `vel_cap` on the Sus row:
  - Trumpets 1-2 969.4-983.5 "Sus Non Vib MAX", Horn 1 "Sus MAX", leads at 970 / 973 / 978, v95.
  - Cor anglais 698.9-707.0 and 730.9-741.0 "Sus MAX", leads at 699-704, 706, 732-736, 740 (velocity unchanged, v53 like the c27 spans).
  - Horn 1 73.9-75.6 (74, 75.5) and Horn 3 145.9-148.1 (146, 147.5, 148), 577.9-580.1 (578, 579.5, 580) "Sus MAX", v90. Horn 1 817.9-819.6 was in the range test and rejected (below).
  - Horn 3 578: `vol_set` puts the +3 dB step at 577.655, just before the led note-on (it fell inside the head's crossfade tail; vol_guard did this in c28).
- **Ruling 2:** `build/roles.json` (`actor_scripts/roles29.py`): Violins I [167.9, 199, -6]; Violins II / violas / celli / basses [167.9, 199, -3]; Horn 4 [167.9, 186.5, -2]; Flute 1 [168, 176] 5 -> 7, Clarinet 1 [176, 184] 4 -> 6, Oboe 1 [184, 192] 4 -> 6; Violins II / violas / celli [375.9, 391.9, -4], basses -6, Bassoon 2 / Horns 3-4 -2, Clarinet 1 [385.9, 391.9, -3] (edges in rests by ROLE_EDGE_IN_REST). `INSTR_POST["cc_cap"]["Violins I"]` CC1 0 over 167.30-198.90 (manual p.92). Ride row [(166, 0), (168, +1), (198, +1), (199.9, 0)].
- **Ruling 3 (`build/mix.json`):** Trumpet 1 "Mute Sus" `region_gain_db` `pitch_db` {79: -9, 77: -2, 75: -2.5, 74: -1.5, 70: +3, 68: +3.5} (was {79: -4}); Opus state change, Trumpet 1 fully rebuilt.
- **Ruling 4:** the 1079.5 ride row [(1079.5, 0), (1083.5, 0), (1084, -1), (1096, -1), (1104, -3), (1107.8, -3.5), (1107.95, 0)]; `mix.json` `return_rides` bar 113: [[447.5, 0], [448, 3], [449.95, 3], [450.05, 4.5], [451.3, 4.5], [451.4, 0]].
- **Ruling 5 (`mix.json`):** `track_pan` Horn 1 -0.08, Horn 2 -0.16, Horn 3 -0.24, Horn 4 -0.32 (Mono From Left kept); `gain_db` Horn 1 1.2 -> 0.8, Horn 4 1.0 -> 1.8; Horn 3 not compensated (measured -0.33 dB; no stem fix).
- **Ruling 6:** Trumpet 1 989 CC1 offset -12 -> -7; 991 CC11 cut unchanged (991 reads +1.1 dB over c28); `mix.json` Trumpet 3 fff trim 12.6 -> 14.1; trumpet quarters 362 / 366 / 1106 lead 0.02 s (`set`, Sus rows), pickups 361.5 / 365.5 / 1105.5 v95 -> 82 ("Stac DblTng RRx9" layer 76-94).
- **Ruling 7 (generic, `tools/build_reaper.py`):** `ENV_MAX_DB` 23.5: with trims in CC7 the excess over it comes off the whole envelope and goes into the CC7 trim lane (+x, clipped at 0 dB where the trim lane is within x of 0; the remainder stays in the envelope there), `ENV_SHIFTED` records it; an envelope still over 23.5 fails the build.
- **Ruling 8 (generic):**
  - `tools/build_reaper.py` `TRIM_CC7_LEG_PRE_QN` 0.1 / `TRIM_CC7_LEG_POST` 0.003 / `TRIM_CC7_LEG_MIN_DB` 1.0 / `TRIM_CC7_LEG_MAX_OV` 0.12: a trim step of 1 dB or more up to 0.1 qn before a moved note-on, while an earlier note still sounds across it and ends within 0.12 qn after the note-on, moves to 0.003 qn after the note-on (celli 951.55, basses 951.86, Clarinet 1 135.86, Violins II 510.25; the first version without the 1 dB floor and the overlap limit broke the c28 snap in trim ramps and created a celli 892 item).
  - `tools/score_to_parts.py` `ROLE_EDGE_IN_REST` `step_at_note_on` (`step_next_qn` 0.25, `step_held_max_qn` 4.5): a carry that would ramp inside a held note becomes a step just before the note-on of a note starting at the edge; a rise whose held note starts within 4.5 qn before the edge moves into the rest before that note; a held note ending at the edge with a rest after takes the edge in that rest. (The first version also moved falling edges to the held note's start: Horn 3's sf note at 548, Bassoon 1 at 855.9 and Trombones 1-2 at 1015.9 dropped 3-4 dB a whole note early in the net diff; limited to rises.)
  - Bassoon 1 320: `vol_set` reaches the p level in the rest before the led note-on (319.64-319.70) and holds to 320.60.
- **Stale state:** Horn 4's saved Opus state held runtime attacks (16 groups at 20 ms); `state_guard.py` caught it, the track was fully rebuilt during the lock.

## Range test (ruling 1; `jt_CTRL.txt` = the c28 project, `jt_VAR.txt` = c29 data, same session)

- Trumpets / Horn 1 at 243: stem dips 3.8-9.3 -> 0.3-2.5 dB, master 2.4 / 0.4 / 1.3 -> 0.8 / -1.0 / 2.0, fronts lower: adopted.
- Cor anglais: master dips over 3 dB 3 -> 2, max 5.0 -> 3.4 (701 and 734 now 5-6 dB on the stem: the note before is soft on the Sus row): adopted.
- Horn 3 146 / 578 and Horn 1 74: dips 3.0-4.7 -> -4.1..+2.3, fronts lower: adopted. Horn 1 818: dip 3.7 -> 4.4, master 819.5 3.3 -> 4.4, front +10.5 -> +15.3: rejected.
- The full render reproduced the VAR numbers within 0.3 dB on every listed join (`jt_c29.txt`).
- My onset measure (time to post - 6 dB after the minimum) is unreliable on overlapping notes (it jumps by +-250 ms between neighbouring joins), so onset timing is not claimed; the attack probe passed.

## Rejected or deferred

- Horn 1 at 818 on the sustain row (range test above).
- "Leg Slur Accent MAX": not tested (MANUAL-GAPS #1, still open).
- Horn 3 pan-law compensation through `gain_db` (ruling 5): not needed (-0.33 dB measured).
- Not this cycle (coordinator): horn 300-500 Hz EQ, low-brass tenuto downbeats, Trumpet 1 844 / Bassoon 1 482 phrase moves.

## Faults introduced or left

- Trumpets 1-2 at 970-978 now 4-7 dB louder than in c28 on the stem (the legato notes had sagged 2-4 dB under the head; now 1-5 dB over it). Not over the master (master dips under 2 dB), but a listening check is needed.
- Cor anglais joins 701 / 734 dip 5-6 dB on the stem (3.0-3.3 on the master), new; 706 / 740 / 702 / 735 fixed.
- Bar 166 stop 17.6 dB (c28 16.8; no ruled change near it: render variance or the horn pans).
- Flute 1's first solo window (168-170) still -0.3 dB under the loudest other stem.
- Trumpet 3 pickups at 362 / 366 separate by 3.0-3.1 dB (target 4).
