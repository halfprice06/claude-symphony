# Critic B, cycle 7: balance and levels (render c06)

Method. The c06 stems are post-fader, so they include vol_db and the mix.json trims. All levels are K-weighted (BS.1770 filter, applied as a zero-phase FIR by overlap-add) in 10 ms frames. Per-note levels run from the score onset (`sq`) + 80 ms to min(note end, onset + 1.5 s). Per-beat levels use the parts.json tempo map. "Margin" means the melody stem minus the loudest single non-melody stem. The c06 render has entries 0.2-0.3 s late (CHANGES.md). Per-beat and per-bar levels are not affected by that; a few per-note levels may be up to about 1 dB low. Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c07-B/`: `prep.py` (frames), `dyn.py`/`acc.py` (medians by printed dynamic), `mel.py` (margins), `beats.py` (per-beat tables with CC11 and vol_db), `hot.py` (level against a CC11 fit per track), `bass.py`, `fam.py` (family sums), `cbp.py` (per-note level, CC11 and vol_db).

What c06 fixed (measured):
- Cb minus Vc in soft bars: median -0.7 dB (it was -8.1 in c05).
- pp now sounds like pp in every family. Accompaniment medians: winds -50.0, strings -51.3, horns -50.1/-51.1, harp -51.9.
- Bars 7-14: BCl, Bn1 and Bn2 are within 3 dB of each other in most bars.
- Melody margins: bars 57-62 +3.4 to +6.4 dB, bars 71-81 +2.2 to +6.1 dB.

## 1. The Solo Horn F4 sample is 6-7 dB hot, and the fix covers only Horn 1's legato notes. Horn 2 is the second-loudest stem at the bar 61 climax, and Horn 3 still sticks out at bar 79 (measured)

Where:
- Horn 2, bars 61-62 (qn 204-212)
- Horn 3, bars 79-80 (qn 262-267)

What:
- `pitch_trims.json` has Horn 1 F4 -5 (with G flat 4 +4 and A flat 4 +3). `score_to_parts.py` (about line 1097) applies it only to notes whose articulation contains "Leg". Horns 2-4 use the same Solo French Horn KS Master and play their chords on Sus MAX, so they get no trim.
- Bar 61, qn 204. Horn 2 holds F4 (65) at CC11 88, vol 0, and measures -27.9 / -28.1 per beat. That is:
  - 6-7 dB over Horn 3 (-34.5) and Horn 4 (-34.9) on the same chord
  - over Vln II (-28.7) and Tbn2 (-31.9)
  - the second-loudest stem in the bar after Vln I (`mel.py`: "2nd Horn 2 -28.0")
- At qn 208 Horn 2 moves to G flat 4 and then A flat 4 while CC11 rises from 88 to 93. Its level falls to -36.2 / -34.9, which is an 8 dB step down at a pitch change during a crescendo.
- `hot.py` residuals over the track's CC11 fit: Horn 2 F4 at 204 +7.2, Horn 3 F4 at 262 +6.8 and at 265 +6.3, Horn 1 F4 at 182 +6.8 (before its trim). That is the same pitch on the same patch every time.
- Bar 79. Horn 3 (F4) measures -32.6 / -32.4 against Horn 4 (A flat 3) -35.5 / -33.5, even with the c06 role of -4. When Horn 3 moves F4 to E4 at qn 267, its level drops 3.5 dB at a flat CC11 and flat vol.
- Rimsky-Korsakov (rimsky-principles.txt, about line 1965): in forte, horn = 2 woodwinds and trombone = 2 horns. At bar 61 the Horn 2 sample alone does the work of a trombone.

Fix:
- `tools/score_to_parts.py`, the c06 (A #2) block: apply a track's pitch trims to every articulation when the track's entry has `"_all_arts": true`:
  ```python
  pt = {...}
  allart = PITCH_TRIMS.get(tname, {}).get("_all_arts", False)
  if n["pitch"] in pt and (allart or "Leg" in (n.get("art") or "")):
  ```
  Keep the `k.startswith("_")` filter, and skip the bool value when building `pt`.
- `build/pitch_trims.json`: add Horn 2, Horn 3 and Horn 4, each `{"65": -5, "66": 4, "68": 3, "_all_arts": true}` (Horn 1's measured table). Set `"_all_arts": true` on Horn 1 as well.
- `build/roles.json`: Horn 3 [261.5, 271, -4] → [261.5, 271, -1]. With the pitch trim, -4 would put Horn 3 about 2 dB under Horn 4.
- Target:
  - qn 204-212: Horns 2-4 within ±2 dB of each other, and each horn at least 3 dB under Vln II.
  - qn 262-267: Horn 3 within ±2 dB of Horn 4, and at least 6 dB under Vln I.
  - The level step at qn 208 (Horn 2) and qn 267 (Horn 3) is under 2 dB.

## 2. At both climaxes the bass and tenor lines are carried by single reeds: the double basses sit 3-7 dB under the contrabassoon alone, and the celli sit 6-8 dB under the one bassoon on their line (measured)

Where:
- Bars 61-62 (qn 204-212). Bass line: Cb, Cbn, Bn2, BCl, Tuba, BTbn.
- Bars 79-81 (qn 262-270). Bass line: Cb, Cbn, Bn2, BCl. Tenor line (C sharp 4, C4, B flat 3, A flat 3): Vc, Bn1, Hn1.

What, per beat:
- qn 204-207: Cb -33.2 / -33.9; Cbn -30.6 / -31.6; Bn2 -30.5 / -31.2; BCl -30.2 / -30.0.
- qn 208-211 (G flat 1, E1): Cb -36.5 / -38.4; Cbn -31.7 / -31.3.
- qn 262-267:
  - Cb -36.1 / -37.0 / -38.4 / -37.8 / -38.2 / -36.8
  - Cbn -31.1 / -30.4 / -31.9 / -31.8 / -32.0
  - Bn2 -32.1 / -30.9 / -31.3 / -33.0
  - BCl -32.7 / -30.2 / -30.4 / -33.4
- Tenor line, qn 262-264: Vc -39.4 / -39.9 / -40.1; Bn1 -34.1 / -34.1 / -32.4; Hn1 -32.0 / -32.6 / -36.3.
- Family sums, bar 79: winds -21.4, strings -22.6.

Rimsky-Korsakov (line 1985): in forte one string department equals two wind instruments, which is about +3 dB over one reed. The measured Cb and Vc are 6-11 dB off that ratio, in the direction that makes the climax sound like a wind band over a light string bass. (Inferred.)

Cause: the trims stack against the strings and in favour of the reeds.
- Vc: `dyn_trim_db` ff -4.5, plus the role [250, 274, -5], which was set in c04 when the Vc countermelody was too loud in bars 75-78.
- Cb: ff -1, plus the role [262, 276, -2].
- Reeds: Bn2 ff +3, Bn1 ff +1.5, Cbn f +2.5 / ff +1.

Fix (`build/mix.json` and `build/roles.json`):
- Violoncellos role [250, 274, -5] → [250, 262, -5] and [262, 274, -1].
- Double basses: delete the role [262, 276, -2]. `dyn_trim_db` ff -1 → +1.
- Contrabassoon `dyn_trim_db` {"f": 2.5, "ff": 1} → {"f": 0.5, "ff": -2}.
- Bassoon 2 ff 3 → 0. Bass clarinet ff -1 → -3. Bassoon 1 ff 1.5 → -0.5.
- These are ff-weighted trims (0 at p), so the soft bars do not change.
- Target, per beat in qn 204-212 and 262-268:
  - Cb at least level with Cbn.
  - Vc at least level with Bn1 on the tenor line.
  - Vln I margin still at least +4 at bars 61-62 and 79-80.
  - Long-term 63 Hz band no higher than -4.5 (now -4.7 against the reference's -6.2). Removing reed bass should offset the Cb gain. The 125 Hz band should rise toward the reference (+0.7 against +7.0). (Inferred.)

## 3. At both climaxes Flute 2's inner note is louder than Flute 1 on the tune (measured)

Where: bars 61-62 (qn 204-212) and bars 79-80 (qn 262-267). Flute 1 doubles the Vln I tune (A flat 6, B flat 6). Flute 2 holds the harmony a third or fourth below.

What:
- qn 206 / 208 / 210: Fl2 -27.6 / -26.1 / -29.5; Fl1 -27.9 / -28.5 / -29.8.
- qn 262-265: Fl2 -27.4 / -25.0 / -30.1 / -29.5; Fl1 -27.6 / -33.8 / -36.2 / -37.5.
- At bar 79 the tune flute fades by beat 2 and the inner flute stays. Fl1 carries -8 dB at qn 262 (roles [262, 270, -2] plus note_trims 262 -6, from c04, when Fl1 was 3 dB over Vln I). Fl2 has no trim and plays at velocity 91.
- Vln I at qn 262-265 is -25.4 / -24.4 / -24.7 / -27.3, so Fl1 is now 9-12 dB under Vln I. Rimsky's forte ratio (Vln I = 2 flutes) puts a doubling flute about 3 dB under.

Fix:
- `build/note_trims.json`:
  - Flute 1 262: -6 → -3
  - add Flute 2 {"262": -6}
- `build/roles.json`: add Flute 2 [204, 212, -3].
- Target: Fl1 at least 2 dB over Fl2 in every beat of qn 204-212 and 262-267. Fl1 5-8 dB under Vln I at qn 262-265.

## 4. The double basses' A flat 1 is 5-9 dB hot, so the soft bass is lumpy, and in bar 30 the basses are the loudest stem (measured)

Where: bars 23, 25, 27, 30, 51-52 and 82 (Cb A flat 1, MIDI 32, arco Sus).

What:
- In qn 66-90, all notes at CC11 51 and vol -1:
  - A flat 1 at qn 66 / 72 / 78 / 87: -41.7 / -41.8 / -40.9 / -43.5
  - E flat 2 at qn 71 / 75: -49.7 / -51.2
  - B flat 1 at qn 70: -45.1
  - F2 at qn 69: -47.6
- In bars 48-52 at CC11 39: A flat 1 at qn 164 / 168: -47.6 / -46.8. D2 is -52.7 to -54.6 and B1 -50.7 / -54.7.
- `hot.py` residuals for A flat 1: +7.8 at 250, +7.7 at 78, +7.5 at 66, +7.4 at 72, +6.5 at 271, +6.4 at 87.
- Per bar, Cb minus Vc: +5.2 (bar 23), +4.0 (28), **+10.7 (30)**, +7.2 / +8.8 (51-52), +6.6 (82). Other soft bars are about 0.
- Bar 30, qn 87-90: Cb -43.0 / -47.0 / -46.0 against Vln I, which ends the phrase, at -44.3 / -48.1 / -49.4. Cb is the loudest stem in the bar (margin -1.7).
- Bars 51-52: Cb is printed pp under the cor anglais solo. It measures -44.5 to -47.2, which is 2-4 dB over Vln II and 7-9 dB over Vc.
- Inferred cause: a strong sample at that pitch. Its third harmonic (156 Hz) also falls on the Cb's +3 dB bell at 150 Hz. A flat is the tonic, so the note recurs.

Fix:
- `build/pitch_trims.json`: add Double basses {"32": -5, "_all_arts": true}. This needs the code change from #1.
- Target:
  - A flat 1 within 2 dB of the neighbouring notes at the same CC11.
  - Cb minus Vc between -3 and +2 dB in bars 23, 28, 30, 51, 52 and 82.
  - Cb at least 2 dB under Vln I in bar 30.
- Do not change the soft trim table to get this; the other notes are right.

## 5. Bassoon 2's D flat 3 is 5 dB hot: in bar 69 its pp chord note covers the end of the horn solo (measured)

Where: bar 69 (qn 232-237). Horn 1 "1. solo" holds B flat 3 mp > pp. The bassoons enter pp: Bn1 G3, Bn2 D flat 3 (49).

What:
- Per beat, qn 232-236:
  - Bn2 -45.8 / -41.9 / -44.5 / -47.7 / -44.9
  - Bn1 -49.9 / -52.1 / -55.2 / -54.9 / -54.5
  - Horn 1 -44.8 / -45.6 / -47.7 / -49.2 / -48.5
- Bn2 is 5-8 dB over Bn1 at the same printed pp and CC11 34, and 1-4 dB over the solo horn. The bar 69 margin is -2.1.
- The same pitch has been trimmed one note at a time four times already: note_trims Bn2 172 -7, 182 -7, 252 -6, 253 -6, all D flat 3.
- `hot.py` residuals: 253 +5.5 even after its -6 trim.

Fix:
- `build/pitch_trims.json`: add Bassoon 2 {"49": -5, "_all_arts": true}.
- `build/note_trims.json` Bassoon 2: 172 -7 → -2, 182 -7 → -2, 252 -6 → -1, 253 -6 → -1, so the net trims stay the same.
- Target: in qn 232-237, Bn2 within 3 dB of Bn1 and at least 2 dB under Horn 1 until qn 235.

## 6. Two soft spots where an accompanying part outweighs what it supports (measured)

- **Bar 47 (qn 148-151).** The oboe "dolce espr." arrives at mf with a decrescendo; Vc doubles it.
  - Per beat at qn 148-150: Cb (mp) -43.4 / -43.2 / -49.3 and Bn2 (mp) -43.8 / -46.2 / -46.8, against Oboe 1 -45.6 / -45.6 / -47.3.
  - The mp bass is 1-2 dB over the mf solo.
  - Cause: the c06 per-track soft trims taper linearly from the p anchor (CC 46) to the f trim (CC 88). At CC 58 (mp), Cb and Bn2 still get about +3.6 dB from their "p": 5 (`build_reaper.py vol_points`).
  - Fix: `build/roles.json` add Double basses [146, 151, -3] and Bassoon 2 [146, 151, -3].
  - Target: Oboe 1 at least 2 dB over Cb and Bn2 in qn 148-150.
- **Bars 87-89 (qn 286-292), muted horn pair, pp.** This has been open since c05.
  - Horn 4 measures -47.7 / -46.4 / -46.7 / -50.5. Horn 3 measures -53.4 / -52.4 / -55.6 / -55.9.
  - The lower voice is 5-7 dB over the upper voice.
  - `hot.py`: Horn 4 F3 (53) at 286 +6.7 over its fit.
  - Fix: `build/note_trims.json` Horn 4 {"286": -5, "289": -3}.
  - Target: Horn 4 within ±2 dB of Horn 3 in qn 286-292.

Do not touch:
- The soft-trim scheme and its overrides: pp medians agree across winds, strings, horns and harp within about 2 dB, and Cb minus Vc in soft bars has a median of -0.7.
- The B #1-#4 / c06 B #5 roles, which give melody margins of +3 to +6 in bars 55-62 and 71-81.
- Bars 7-14: the horn solo is on top by +4 to +13 and the reed chord is even.
- The Tbn1 solo in bars 63-64 (+3.4 / +9.8).
- The timpani roll settle.
- The Cb 40-90 Hz EQ.
- The volume-envelope scheme (CC11 picks the layer, level trims in the envelope).
