# Cycle 6 changes (actor)

Snapshot of the tools and build/*.json before this cycle: `cycles/c06/before/`. REAPER was quit and restarted (for ONE_TIME.md, see below), the project reopened, and once it had loaded, all 27 tracks and the tempo map were rebuilt (`build_reaper.py build/parts.json jobs`). Then one render (`render_cycle.py 6`). Event counts in REAPER matched parts.json for every track.

## ONE_TIME.md (Opus PreloadSize): not done, file left in place

Dan's "sure" (2026-10-11 13:21 UTC) is in the project thread, so this time the approval was confirmed in his own message. I saved the project, quit REAPER and tried to set `"PreloadSize": 0` in `/Library/Application Support/East West/Opus/Preferences.json`. Claude Code's permission system blocked the edit. I did not try to get around the block. The file still says `"PreloadSize": 1`, which matches `loop/Opus-Preferences.backup-2026-10-11.json`. REAPER was restarted with the old setting. **Dan has to change this setting himself**, either in Opus's settings (streaming preload: Harddrive) or by allowing the edit. Renders in this cycle used PreloadSize 1.

## Render health: the attack gate failed (10 of 19 checks), cause measured as memory pressure

- Every failing entry is 0.2-0.3 s late. This includes tracks with no timing change this cycle: Timpani 277 (+0.32 s), Cb pizz 108 (+0.22), Vla 124 (+0.24), Vc 108 (+0.21) and Tbn1 212.5 (+0.08). At bar 63 the tremolo arrives about 0.2 s late in Vln I/II/Vc, which leaves holes of 20-30 dB. In c05 all of these were on time.
- After the render, `top` showed REAPER at 57 GB with **42 GB of it compressed** by macOS. 200 MB was free, 2.85 of 4 GB swap was used, and other processes (two chrono-25d Python jobs, Spotlight's mds_stores at 80-120% CPU) were reading the internal disk at about 300 MB/s. Opus's preloaded sample heads were in compressed memory. Inferred: Opus could not get them back in time at 1x.
- **Not rendered a second time.** A second heavy render is what froze the Mac this morning, and memory was tighter now. Musical judgements in this render are fine for level and balance. Its onset timing is not trustworthy (see `metrics/attacks.txt`). The next actor should re-render only once REAPER's compressed memory is low (`top -l 1 -o mem -stats pid,command,mem,cmprs`).

## Accepted

**A #1 / B #4: silent pre-roll** (`score_to_parts.py` PREROLL_QN 3.0 at 60 bpm, written to parts.json as `preroll_qn`/`preroll_bpm`; `build_reaper.py`; `render_cycle.py`).
- parts.json stays on score time.
- build_reaper writes every note, keyswitch, CC, volume point and tempo marker 3 qn later. It adds a 60 bpm 3/4 bar at the start. In that bar it sends each track's first keyswitch and the first value of every CC lane at qn 0.25.
- render_cycle renders 3 qn more and cuts REAPER's own `TimeMap2_QNToTime(0, 3)` worth of samples (3.000 s = 144000 samples) off the master and every stem, so every downstream measurement keeps the old timeline. It warns if the cut part is not silent; it was silent.
- `probe_attacks.py` now checks the opening chord: Hn3, Vln I/II, Vla and Vc each need a 50 ms maximum above -70 dB in the first 1.5 s.
- Measured: Hn3 opening max -75.0 -> **-56.2 dB**. Mean over qn 0-2: -88.3 -> -59.6, level with Horn 4's entry (-63.2). All five opening voices passed.

**A #2: per-pitch trims** (new `build/pitch_trims.json`, applied in vol_db to notes on a Leg articulation, from 0.1 qn before the score onset with a 0.25 qn ramp).
- Hn1 F4 -5, G flat 4 +4, A flat 4 +3. Cl1 G5 -6, A flat 5 +5. CA A4 -5. Fl1 G flat 5 +4.
- Removed `note_trims` Cl1 266 -3, which deepened the A flat 5 sag.
- Measured (note body, 0.3-0.85 qn):
  - Hn1 at qn 180/182/184/190/192/195/196: before -45.1/-38.7/-42.3/-48.3/-39.2/-35.3/-44.6, a 13 dB spread. After -44.3/-42.4/-41.8/-42.3/-42.5/-37.7/-40.2, a 6.6 dB spread.
  - Cl1 at qn 255/256/266/268: before -51.0/-43.2/-42.7/-30.0. After -41.0/-43.6/-34.5/-36.0.

**A #3 (cheap version): Leg -> Sus MAX string notes with no rest between them are treated as entries.** They get ENTRY_LEAD_S, CC11 held at the entry level, and velocity of at least 105 (`score_to_parts.py`). This applies to Vc qn 51 and 63, two notes each.
- Measured: the qn 63 dip went 9.8 -> 6.7 dB. The qn 51 dip went 12.3 -> 17.6 dB, but this render's entries are 0.2 s late, so the result is inconclusive. Open. The full fix is a Celli DIV B track (memory).

**A #4 (partly): `LEG_EXTRA_S = {"Violas": {60: 0.10}}`.** Legato targets after a viola C4 start 0.10 s earlier, still capped at 0.45 of the previous note. Not measured this cycle because of the render timing.

**A #5: printed bow marks.** An up-bow or down-bow inside a held string note adds a bow-change notch: 14 CC above CC 40, 6 at pp and softer. This adds 4 notches in Vln I (265, 292, 295, 298), 1 in Vln II (265) and 1 in Vla (265). Measured: Vln I dips about 2 dB at qn 265.0-265.25 and recovers by 265.375.

**B #1, #2, #3: soft levels** (`mix.json`, `build_reaper.py vol_points`, `roles.json`).
- `soft_trim_db` now has a p anchor at CC 46. The global setting is {ppp -2, pp 0, p +2}; it was {ppp -4, pp -2}.
- Per-track overrides: Cl1 {-4, -3, -1}, Cl2 {-3.5, -1.5, 2}, Bn1 {1, 3, 4}, Bn2 {2, 5, 5}, Cb {-2, 3, 5}, Vla {-2, 2, 2}.
- Cb roles: [66,90] -4 -> -1; [172,188,-2] removed; [108,137.5,+5] added for the pizz. Cl1 [250,258] -4 -> -1.
- Measured Cb minus Vc over 18 soft bars: median -8.1 -> **-2.6 dB**. Range -11.6..-4.3 before, -8.1..+3.6 after.
- Bars 7-14 per bar (BCl / Bn1 / Bn2):
  - Before: Bn1 6-12 dB and Bn2 3-8 dB under BCl.
  - After: -50.3/-58.8/-50.2 ... -50.5/-51.4/-51.9. Bn2 is now within about 3 dB of BCl in most bars. Bn1 is still 1-8 dB under, with the largest gap in bars 7 and 10.
- LRA 25.4 -> **23.9 LU** (target 22-23). Soft bars rose about 2.5 dB: bar 1 -52.8 -> -49.9, bar 66 -55.0 -> -52.2, bar 84 -53.4 -> -51.0. Bar 61 rose 1.3 dB, more than the ±0.5 target, because of C #4 and the hairpin gain.

**B #5: horns under the tune** (roles Hn3 [261.5,271,-4], Hn1 [176,188,-3]).
- Hn3 at qn 262-266: -32.6 -> -36.2, now 3.9 dB under Vln I (was 0.2) and 3.9 over Hn4.
- Hn1 at qn 182-184: -39.3 -> -44.3, now under both violin sections (-40.6 / -41.4).

**B #6: bars 46-47 and bar 84** (roles Vln II [146,152,-4], Vla [146,152,-3]; note_trims Timp 277/278.5/279 +3).
- Oboe / Vln II / Vla at qn 147-149: -47.6/-49.5/-49.0 -> -46.6/-52.4/-51.0.
- Timpani at qn 277-279.5: -62.0 -> -59.1, still 4 dB under the Vc (-55.2). The 277 stroke was 0.32 s late in this render, so this is not judged.

**C #1: crescendos to f or louder rise in dB too** (`score_to_parts.py` `hpgain`: winds +4, strings +3, brass +2, ramped across the hairpin and held to the next onset).
- Changed from C's proposal: the gain is released over HP_REL = 1 qn, not 0.25 qn. A 3-4 dB drop one beat after the climax arrival would sound like fp.
- roles.json rows now take an optional fourth value, end_ramp. The bar 57-60 cuts open over the last 4 qn: Vc -6, BCl -5, Vla -4, Cb -3, Hn1 -2.
- Measured, growth from qn 200.25 to 203: Fl1 -1.0 -> +1.7, Ob1 +0.4 -> +3.1, Cl1 +0.7 -> +3.6, Bn1 +0.7 -> +3.5, Vc -4.1 -> +4.6 dB.
- Jump to qn 204: Vc +9.7 -> +7.7. Fl1 is unchanged at +6.9 (target 4). The master's last beat of bar 60 is now 6.1 dB over its first beat (was 4.0; target 5).
- Cb from qn 250 to 259: not improved (its notes vary by 3-5 dB per beat). Open.

**C #2: the sf in bar 63.** From f or louder, the sf now falls 10 CC (was to mf) and its 0.25 qn point is spike - 4. Measured Vln I per beat, qn 212 -> 216:
- before -33.5/-41.6/-43.3/-45.5/-46.3 (-8.1 dB in the first beat);
- after -33.8/-36.6/-38.4/-41.8/-44.2 (-2.8, then -1.8/-3.4/-2.4).
- Trombone 1 stays 7-9 dB over Vln I. The first 0.45 s of the bar has a tremolo timing hole in this render (see above).

**C #3: hairpin parser edge cases** (`base_points`).
- An untargeted hairpin does not overshoot the next printed mark in its own direction (looked up 1-6 qn after its end).
- A decrescendo whose printed target is not below the current level falls 6 CC, and the mark at its end does not raise the level.
- "niente <" to the current level starts 12 CC lower.
- Changed dynamic curves: Cl2 295-301, Cl1 280-282, Vln I 60-65 (the 68 -> 58 drop is gone) and Vln I/II 242-250 (the decrescendo stops at mp, not 4 under it).
- Measured Cl2 per qn, 297 -> 301: before -64.1/-63.2/-61.2/-59.5/-59.2 (rising). After -58.1/-58.3/-59.3/-60.3/-61.7 (falling 3.4 dB; the 4 dB target was nearly met). The Cl2 ppp at 301 is held at CC 16, and score_to_parts warns about it.

**C #4: the main climax over the second one.** roll_db ff -14 -> -11, fff -12 -> -9. Roles Tbn2, BTbn, Tuba [204,212,+2].
- Measured master bars 61/62 vs 79/80: -22.2/-23.0 vs -23.6/-24.1 (margin 1.4) -> -20.9/-22.6 vs -23.3/-23.9 (margin **2.4 dB**).
- The timpani ff roll at qn 204-205 measured only +0.3 dB over c05 (-36.7; the f roll at 262 is -38.3), against an expected +3. The roll started 0.2 qn late in this render. Open.

**C #5: dB swell on long notes** (`swell_db`: +1.5 dB at 40% of the note, 0 at 80%, -1.5 at the end of a phrase). It applies to the same notes as the CC11 swell. Not measured separately this cycle.

**C #6: Trombone 1 in bars 63-64.** note_trims 214.5 -1 ... 217.5 -2.5. VEL_SET Tbn1 218 -> velocity 105 (was 121). Trombone 1 at qn 213-217: -27.2 -> -29.4 dB.

## Rejected / deferred

- A #4, second part (violas' `short_sus` limit 0.38 s for the triplets): deferred. It needs a `dom.py` check against a render with good timing, and the Sus attack at pp is a risk.
- A #2 flute alternative (no +10 CC1 on the top note of each flute slur): not done; the pitch trim was used instead.
- A #3 full fix (Celli DIV B track) and the other divisi/solo tracks: deferred. REAPER already holds 57 GB, and memory pressure broke this render.
- C #3's rule that a mark after a decrescendo does not raise the level is used only after a decrescendo that was turned downward. As a general rule it would ignore real subito marks.

## Measured overall (c05 -> c06)

- Integrated -25.7 -> **-25.1 LUFS**. LRA 25.4 -> **23.9 LU** (low -43.0, high -19.0). True peak -5.5 -> **-4.2 dBFS**. No clipping. All 27 stems are present.
- Spectrum re 1 kHz: 63 Hz -5.3 -> -4.7 (reference -6.2). 125 Hz -1.1 -> +0.7 (reference +7.0).
- Attack gate: **10 of 19 checks failed.** The 5 opening checks passed. The failures come from render timing under memory pressure (see above).
- mp3: `cycles/c06/mvt2-mockup-c06.mp3`.
