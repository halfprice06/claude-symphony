# Cycle 21 (2026-11-17): delivery and climax order, bar 223 low end, basses' eighths, inner lines, trumpet note ends, cor anglais, harp harmonics

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c20 render), plus the coordinator's rulings 1-10 and its note from Movement II c57 (top ride 2:1). Snapshot before this cycle: `before/`. Scripts: `actor_scripts/` (`data21.py --write` makes the mix.json edits; `statechk.py` checks Opus state edits offline; `parkchk.py`, `rana.py`, `meas21.py`, `dips21.py` measure). Logs: `logs/`.

Standing rule (Dan): the track volume envelope holds slow balance only. Every fix below is on the instrument side, a held phrase level, or a delivery ride.

## For Dan

- **Loudness.** The mp3 now plays at -14.0 LUFS, the shared target (c20 was -14.8). Quiet passages sit at about -22.6 LUFS (the quietest tenth of the piece); loud peaks are not louder than before.
- **The limiter works less hard.** It now takes 5.7 dB off the final chord's loudest peaks (c20: 7.8) and 4.2 dB at bar 223 (c20: 6.1).
- **Climaxes keep the printed order, but only just.** The final chord, then bar 223, then bar 263, then the ff bars; bar 263 is now 1.6 dB over the loudest ff bar (c20: 0.9). The final chord, 223 and 263 are within 0.3 dB of each other.
- **Bar 223 has more bottom.** The basses' low octave at the C-major arrival is 4 dB stronger than in c20, and the bass drum is 6 dB louder at 223 and 278. The low end still dips slightly at the arrival instead of growing.
- **Basses' hammered eighths are back up.** They are 3.5-6 dB louder than c20, close to c19's level in three of four passages, and still separate. In the accelerando (bars 205-210) they are 3 dB short of c19.
- **Inner lines you should now hear:**
  - the trumpets' soft off-beats in bars 159-166 (11 dB louder; they were inaudible);
  - the clarinets' broken chords in bars 151-170 (+1.6 / +2.3 dB);
  - the oboe on the theme's head at bar 83 (+2.4 dB);
  - the counter-line in bars 212-215 (+0.6 dB, on target).
- **Trumpet note ends no longer stop dead.** Their notes now fade like the trombones' (-15 dB 0.2 s after the note ends; before: -35 to -41 dB).
- **Cor anglais solo (bars 171-183).** The held notes it shares with the muted trumpet now play on the cor anglais' plain sustain, so they swell less. The cor anglais now sits about 4 dB over the muted trumpet; it was 2 dB.
- **Harp.**
  - The printed harmonics (bars 43-47) now play harmonic samples, at the same level as before.
  - The glissando in bar 277 now plays the harp's glissando technique samples.
  - The harp as a whole is about 3 dB louder than in c20.
- **Not fixed:** the celli's repeated notes on a new bow still run together (4 of 17 separate clearly; c20: 2).

## Results (main render 07:20-07:31)

- **Delivered (`mvt3-mockup-c21.mp3`, the delivery re-run with the adjusted final rides, `logs/deliv_c21.log`):**
  - -14.0 LUFS, LRA 12.2 LU, true peak -1.1 dBTP, p10 short-term -22.6 LUFS.
  - Limiter: 5.7 dB on the final chord, 4.2 at bar 223, 3.8 at bar 263, 3.4 at bar 91, 1.0 at bar 1.
  - Momentary max: final -7.6, bar 223 -7.8, bar 263 -7.9, loudest ff bar -9.5. Bar 222 (-7.8) no longer sits over 263.
- **First delivery** (`mvt3-mockup-c21-first.mp3`, from `render_cycle.py`, with the ruled rides): -14.0 LUFS, LRA 12.2, true peak -1.1, limiter 6.7 / 4.5 / 3.8 dB. The final chord and bar 223 tied at -7.5.
  - Fix, simulated on the c21 master: the final row -2.5 -> -3.5 dB and the bar-223 row -4.5 -> -5.5 dB.
  - The final row alone gave limiter 5.7 dB, but bar 223 came 0.1 dB over the final.
- **Master:** -19.8 LUFS, LRA 22.6, true peak +0.6 dBFS. The WAV clipped and `render_cycle.py` replaced it with the float stem sum, peak 1.073; the delivery normalises it.
- **Checks:**
  - Attack probe: 0 late or holes.
  - Pre-roll messages: the same six as in c18-c20.
  - Every stem is present and within 0.2 dB of c20 overall, except where this cycle changed it: Bass drum +6.0, Double basses +1.5, Harp +0.7.
  - Violins I / II / Violas over bars 1-10: correlation 1.000 / 1.000 / 0.98 with c20, level +0.00 dB. The full rebuild kept c18 / c20's round-robin take.
- **REAPER memory:** 45 GB before the render (0 compressed), 45 GB after (14 compressed).
- **Lock:** taken 06:45:33, released 07:33. Held 48 minutes: start and settle 13 min, builds and two range passes 5 min, a state-guard rebuild of the basses, restart and settle 13 min, render 11 min.

| target | c20 | c21 | goal |
|---|---|---|---|
| delivered I / LRA / TP / p10 | -14.8 / 12.0 / -1.1 / -23.1 | -14.0 / 12.2 / -1.1 / -22.6 | -14 ±0.5 / about 12 / -1.0 / -23 or higher |
| limiter final / 223 / 263 | 7.8 / 6.1 / 2.8 | 5.7 / 4.2 / 3.8 | about 6 at most |
| final / 223 / 263 / loudest ff bar | -7.0 / -7.1 / -8.2 / -9.1 | -7.6 / -7.8 / -7.9 / -9.5 | that order |
| basses' stroke p90 792-816 / 816-840 / 984-1056 / 1056-1088 (c19: -29.7 / -31.7 / -28.8 / -34.1) | -33.9 / -41.0 / -31.7 / -38.8 | -30.4 / -34.8 / -29.0 / -34.8 | within 1.5 dB of c19 (816-840: 3.1 short) |
| basses' 30-90 Hz, f bar before 223 -> arrival | 12.6 -> 4.9 | 12.6 -> 8.9 | +1 over (not met) |
| master 30-90 Hz, same | 12.3 -> 6.0 | 12.3 -> 9.9 | |
| Trumpets 1 / 2 / 3 against Violins I, 636-664 (Horn 3 -8.6) | -20.8 / -21.6 / -25.5 | -9.5 / -10.9 / -15.1 | 3-5 dB under Horn 3 (Trumpet 1 is 0.9 under) |
| Clarinets 1 / 2 against Violins I, 600-680 | -9.5 / -8.8 | -7.9 / -6.5 | about -6 |
| Clarinet 1 / Oboe 1 against Violins I, 328-344 | -3.1 / -5.0 | -2.6 / -2.6 | within 3 |
| counter-line 844-857 under Trumpets 1 + 2 | -6.1 | -5.5 | -5 |
| Trombones 1 / 2 under Trumpets 1 / 2, 792-816 | 2.3 / 3.2 | 1.9 / 2.9 | within 2 |
| trumpets after note-off, +0.20 s (Trombone 1 -14.5) | -35 / -40 / -41 | -14.2 / -15.9 / -15.4 | -15 to -22 |
| cor anglais legato-target rise (`rana.py`, median) | +3.1 | +2.1 | under 2 |
| Trumpet 1 minus cor anglais, unison bodies (median, within ±2 dB of it) | -2.2 (17 of 21) | -4.3 (16 of 24) | ±2 (not met) |
| harp harmonics 168-184: level / B flat 4 minus B flat 5 | -56.6 / +24.9 | -56.7 / +18.4 | within 3 dB of c20 |
| celli stroke-fall re-bows, dip 3 dB or more (`dips21.py`) | 2 of 17 | 4 of 17 | 20 of 26 (not met) |
| violas / basses, same | 17 / 10 of 21 / 12 | 17 / 10 (medians 7.4 -> 8.2, 8.2 -> 9.3 dB) | |

## Range passes (under the lock)

- **R1** (variant A of the cor anglais; Harp KS Master) and **R2** (variant C), in `range/`.
- **Cor anglais.** Rise on the long unison notes 688 / 692 / 720 / 728:
  - c20: +4.5 / +6.4 / +7.6 / +3.1 dB;
  - A (TLeg +4 dB): +5.3 / +6.3 / +7.3 / +2.8 dB;
  - C ("Sus MAX"): +2.4 / +2.2 / +3.9 / +0.7 dB.
  - A did nothing to the rise and made the line 2.4 dB louder, so its region gain was removed. C was adopted.
- **Harp.**
  - The rows switched correctly with the moved trigger keys.
  - The KS Master played 5-9 dB over the old patch: the 264 note +7.3, the glissando +5..+6, the harmonics +9 dB.
  - Fix, without a second range test: gain_db -3.6 -> -7.6 and Harmonics region gain -5 dB.
  - On the render: the harmonics are at c20's level; the 264 note is still +3.3 dB.

## Changes (files and values)

- **Ruling 1 (delivery):**
  - `tools/deliver_master.py`:
    - a loudness loop after the limiter (the shortfall plus 0.05 dB is added to the pre-limiter gain; 3 passes at most; env `DELIVER_LOUD_PASSES`);
    - top ride 3:1 -> 2:1 (coordinator, Movement II c57; on the c20 master LRA 11.5 -> 12.4, limiter 5.8 -> 6.0 dB);
    - env `DELIVER_TOP_RATIO`.
  - `build/mix.json` deliver.ratio 2.0 -> 1.8.
  - `build/score_config.py` c21 block, the w11 rides: the final row -3.5 dB (ruled -2.5, adjusted after the render); bars 222-223 -3 / -5.5 dB (ruled -4.5); bar 263 -1.5 / -2 dB; the ff stabs -3 / -2 / -1.5 dB.
  - The c20 master re-delivered before the lock with the w11 rides at -2.5 / -4.5 and 2:1: `mvt3-mockup-c20-redelivered.mp3` (-14.0 LUFS, LRA 12.4, limiter 6.0 dB).
- **Ruling 2:** basses' Tremolo row pitch 36 +4 dB (region gain); Bass drum gain_db -7.4 -> -1.4.
- **Ruling 3:** basses' "Stac On Bow" all_db -1.5 -> +2.5; CC11 +5 dB (k 47) over 816-840. The muted release extension and the 90 ms release are unchanged.
- **Ruling 4:**
  - Clarinets 600-680: CC1 +6 removed, CC11 +3 dB.
  - Oboe 1: CC11 +2 dB at 328-344.
  - Horns 3-4: CC1 +6 removed, CC11 +3 dB at 843.6-856.7.
  - Trombones 1-2: CC11 +1.5 dB at 792-816.
  - Trumpets 633-662: velocity +8 (88 -> 96).
  - New generic rule `short_cc_park` (`tools/instr_post.py`): CC11 held at 100 and CC1 at 85 or more from 0.05 s before each short-row note to its note-off.
    - On Trumpets 1-3 (`C21_PARK`): +5.7 dB at 633-662 and -0.8 dB at 1105.5; nothing else moves.
    - On all brass it would also have moved Horn 1 bar 140 +13.5 dB, Horns 3-4 bars 11-26 +5.7 and bars 151-166 +2.2 dB (`parkchk.py`). Not applied there.
- **Ruling 5:** `cap_release()` takes `"set": true` (`tools/build_reaper.py`). Trumpets 1-3 sustain groups p / mf / f / ff set to 300 ms on Sus Non Vib MAX, Leg Slur MAX and Mute Sus (Trumpet 1). The c20 release-trail +6 dB is kept.
- **Ruling 6:** the c19 cor anglais note_shape is deleted; "Sus MAX" over 679.9-696 and 711.9-731 (`C21_CA`, default "sus"). The TLeg region gain was tested and removed.
- **Ruling 7:** the Harp moves to the Harp KS Master.
  - ART_SPANS: Harmonics 167.9-191, Gliss Technique 1105.9-1107.9, Sus RR elsewhere.
  - `score_to_parts.py`: a harp track takes ART_SPANS.
  - `build_reaper.py` mix.json `ks_keys` / `ks_unused_off`: Harmonics -> key 112, Gliss Technique -> 113, unused triggers off; the same keys are in `build/ks_maps_extra.json`.
  - Harp gain_db -7.6; Harmonics region gain -5 dB.
- **Ruling 8:** `STR_REP_NEW_BOW["stroke_fall"]` (`score_to_parts.py`, parts.json `stroke_falls`): 10 / 12 units of CC11 over 0.06 s on the "stroke" and "sus_min_s" new bows of every string track.
- **Ruling 1 (crest):** Trombone 1 CC11 -10 units at 1103.9-1106.1.
- **Ruling 9:**
  - Cor anglais at 600: the bar-150 vol_set row now holds 0 dB from 599 to 601.8. Dropping the row alone left a release running through the note. Fader guard: 4 moves inside notes, all from earlier cycles (c20: 5).
  - Violins I / II / Violas rebuilt in full.
- **Builds:**
  - `--midi-only` of 28 tracks, 6 rebuilt in full (Double basses, Trumpets 1-3, Cor anglais, Harp).
  - Full build of Violins I / II / Violas.
  - Cor anglais and Harp again after the range passes.
  - Double basses in full after the state guard reported 8 stale attacks.
- **Checks:** `parts.json` rebuilds from the config identically (checked after the ride edit); score_to_parts.py printed no WARNING.

## Rejected or deferred

- Short-row park on horns and low brass: see ruling 4 above (Horn 1 +13.5 dB at bar 140; the horn off-beats are accompaniment).
- Cor anglais TLeg +4 dB: measured no effect (R1).
- C's loud_eq on ff / fff spans: deferred to c22 by ruling 10. Horns 2 / 4 routing and tremolo region gains: not this cycle (ruling 10).
- B / A: no further lifts for Bassoon 1 / celli on the 212-215 counter-line (it is on target at -5.5 dB).
- Tuba lead 792-840 (A, S2): not done this cycle.

## Faults introduced or left

- The cor anglais is about 4 dB over the muted Trumpet 1 in the unison spans (c20: 2.2). The Sus MAX row plays louder than the legato row at the same CC11.
- Trumpet 1's off-beats at 636-664 are 0.9 dB under Horn 3 (target 3-5 under).
- Harp about 3 dB louder outside the harmonics (the bar-67 note +3.3 dB).
- The final chord / 223 / 263 margins are 0.1-0.3 dB.
- Basses at 816-840 still 3.1 dB under c19.
