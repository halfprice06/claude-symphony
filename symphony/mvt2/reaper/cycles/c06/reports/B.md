# Critic B, cycle 6: balance and levels (render c05)

Method. The c05 stems are post-fader, so they include vol_db and the mix.json trims. All levels are K-weighted (BS.1770 filter applied in the frequency domain). Per-note levels run from the score onset (`sq`) + 80 ms to min(note end, onset + 1.5 s). Per-beat levels use the parts.json tempo map. "Margin" means the melody stem minus the loudest single non-melody stem. Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c06-B/`:
- `dyn.py`, `acc.py`: medians by printed dynamic; `acc.py` excludes melody spans.
- `mel.py`: per-bar margins.
- `beats.py`: per-beat tables with CC11 and vol_db.
- `hot.py`: level against CC11 fit.
- `bass.py`, `pizz.py`: Vc against Cb.
- `silent.py`: notes that do not sound.

What c05 fixed (measured):
- Margins in bars 57-60 are +4.2 to +6.3 dB, and in bars 75-78 +5.3 to +6.4.
- Bar 28 margin is +3.8 (was -3.0).
- Final-chord violas are level with Vln II.
- Climax bars 61-62 have Vln I on top by +5.5 to +5.8.
- The Tbn1 solo in bars 63-64 is on top by +7 to +12.
- The Bn1 pickup at qn 261 now sounds.

## 1. The double basses are 5-12 dB under the celli at the same printed soft dynamic, so the soft passages have no bass foundation (measured)

Where: Double basses in the soft passages:
- bars 22-26 (arco p)
- bars 37-44 (pizz. p)
- bars 42-46 (Cb pizz./arco p and pp against Vc pp/p)
- bars 65-66 (pp)
- bars 72-74 (pp)

What:
- Cb minus Vc per bar (K-weighted; raw RMS gives the same within 1 dB):
  - bar 22 -8.6, bar 24 -8.6, bar 25 -6.5, bar 26 -11.2
  - bars 37-40: -4.8, -9.2, -6.0, -4.8
  - bars 42-46: -8.8, -9.0, -12.3, -6.1, -8.7
  - bars 65-66: -8.5, -5.9
  - bars 72-74: -9.9, -6.3, -9.0
- At f and ff the gap is 0 to -3 dB, so the deficit is specific to soft passages.
- Pizzicato in bars 37-40: Vc and Cb play the same p pizz. bass line, both at velocity 53. Per stroke, Vc measures -46.2 to -50.6 and Cb -52.8 to -56.5, which puts Cb 3-10 dB under on every stroke.
- In bars 42-44 the Cb pizz. p (-55 to -56 per stroke) is under the Vc arco pp (-50 to -54).
- At CC11 46, fitted per register, Cb measures -50 to -56 against Vc -47 to -49.

Why: the Cb chain has gain -7, a 90 Hz shelf at -7, and Close at 0.4. On top of that, roles.json still carries the cuts made in c04, when the Cb was boomy: [66,90,-4] and [172,188,-2].

Also measured: the long-term 125 Hz third-octave is -1.1 against the reference's +7.0 (metrics.md). The c05 CHANGES give the 125-180 Hz band as -15.5 against -3.7. The 40-90 Hz boom is gone (63 Hz -5.3 against -6.2), so the low end can take more Cb level in soft music. That music contributes little to the long-term spectrum.

Rimsky-Korsakov (Principles, rimsky-principles.txt about line 1990): sustained groups "easily overpower" pizzicato strings.

Fix:
- `build/roles.json` Double basses:
  - [66,90,-4] → [66,90,-1]
  - delete [172,188,-2]
  - add [108,137.5,+5] (the pizz. span; the Sus keyswitch is at 137.5)
- `mix.json` Double basses: add a per-track `soft_trim_db` (see #2 for the code change and the final numbers).
- Target: Cb within 3 dB of Vc in every soft bar where both play the bass line. In bars 23-27, where the Vc has the cantabile countermelody, Cb sits 2-4 dB under Vc. In the pizz. bars 37-40, Cb is within 2 dB of Vc per stroke. Check 63 Hz stays at -4.5 or lower.

## 2. Wind levels at pp/p depend on the instrument, not the printed dynamic: bassoons sit 5-9 dB under the clarinets at the same pp, which makes the wind chords bottom-heavy (measured)

Where:
- the pp wind chord under the Horn 1 solo (BCl / Bn2 / Bn1), bars 7-14
- Clarinet 1 inner and doubling lines at p/pp: bars 53-56, 75-77

What:
- Accompaniment notes only (`acc.py`):

  | | Cl1 | Cl2 | BCl | Bn1 | Bn2 | strings |
  |---|---|---|---|---|---|---|
  | pp | -48.1 | -50.6 | -51.1 | -55.3 | -57.1 | -52.6 to -55.2 |
  | p | -42.7 | -47.9 | -44.2 | -49.8 | -50.2 | Vla -48.2, Vc -49.7 |

- Bars 7-14, all three chord voices at CC11 34, per 3-beat bar:

  | | bar 7 | bar 8 | bar 9 | bar 10 | bar 11 | bar 12 | bar 13 | bar 14 |
  |---|---|---|---|---|---|---|---|---|
  | BCl | -49.6 | -55.1 | -50.9 | -57.2 | -50.8 | -49.3 | -54.2 | -49.7 |
  | Bn1 (top voice) | -60.4 | -56.3 | -54.5 | -62.7 | -56.7 | -55.3 | -55.6 | -54.4 |
  | Bn2 | -56.3 | -59.9 | -56.0 | -57.0 | -57.8 | -57.4 | -60.5 | -56.8 |

  The bass note leads the chord by about 5 dB, and the top voice is often the softest.
- Bars 54-56 (qn 178-185): Cl1, printed pp/p and doubling Horn 1, measures -40.8 to -44.3. That is 3-6 dB under the violin tune, not a pp doubling.
- Cause: the fitted level/CC slopes are Cl1 0.17, Cl2 0.20 and BCl 0.26 against Bn1 0.30 and Bn2 0.34 dB/CC. The same CC11 34/46 gives different levels per patch. The uniform `soft_trim_db` (pp -2, ppp -4) cannot correct this.
- Rimsky-Korsakov (line 1975): "in piano passages, all wind-instruments, wood or brass are of fairly equal balance."

Fix:
- `tools/build_reaper.py` `vol_points()`: add a p anchor:
  `tbl = [(22, soft.get("ppp", 0)), (34, soft.get("pp", 0)), (46, soft.get("p", 0)), (88, dt["f"]), (114, dt["ff"]), (127, dt["ff"])]`
  Without a "p" key nothing changes.
- `build/mix.json` per-track `soft_trim_db` overrides. An override replaces the global dict, so give every key. These values assume the new global from #3, {"ppp": -2, "pp": 0, "p": 2}:
  - Clarinet 1 {"ppp": -4, "pp": -3, "p": -1}
  - Clarinet 2 {"ppp": -3.5, "pp": -1.5, "p": 2}
  - Bassoon 1 {"ppp": 1, "pp": 3, "p": 4}
  - Bassoon 2 {"ppp": 2, "pp": 5, "p": 5}
  - Double basses {"ppp": -2, "pp": 3, "p": 5}
  - Violas (existing override) {"ppp": -2, "pp": 2, "p": 2}
- If #3 is not taken, subtract 2 from every value above.
- Ease the c05 role Clarinet 1 [250,258,-4] to -1, because the p trim now does that work.
- Target: accompaniment medians of all woodwinds within 3 dB of each other at pp and at p. In bars 7-14, Bn1, Bn2 and BCl within 3 dB of each other per bar.

## 3. The soft-to-loud range is wider than in a real orchestral recording: LRA 25.4 LU, with a third of the bars 25-32 dB under the climax (measured; the target is inferred)

What:
- ffmpeg ebur128 on the c05 master: LRA 25.4 LU (low -45.0, high -19.7 LUFS).
- The Dvorak 9/i Columbia reference measures 21.8 LU (-33.0 / -11.2). That is a fast movement with full-orchestra tuttis, so this Adagio should not exceed it.
- 29 of 92 bars are under -45 dB RMS: bars 1-6, 13-16, 30-31, 35-36, 38-40, 44, 49, 65-66, 69-70, 83-86, 88 and 92.
- Bar 61 is -21.1. At a playback level where the climax is comfortable, the opening and the coda (bar 1 -51.5, 66 -53.8, 84 -52.4) sit near the noise floor of a room (inferred).
- Cause: the CC11 table (ppp 22, pp 34, p 46, f 88, ff 114) at about 0.28 dB/CC gives 19 dB from p to ff. The global soft trims add a further -2/-4 dB at pp/ppp.

Fix:
- `build/mix.json` `soft_trim_db`: {"ppp": -4, "pp": -2} → {"ppp": -2, "pp": 0, "p": 2, "_except": [...unchanged]} (needs the p anchor from #2).
- Keep the CC11 table, so the timbre layers do not change.
- Target: LRA 22-23 LU with bar 61 unchanged (±0.5 dB). The final-bar fade in vol_db keeps the ppp ending dying away.

## 4. Horn 3's opening ppp note (bar 1, beats 1-2) does not sound: the first note of the movement is missing (measured; cause inferred)

What:
- Horn 3 at qn 0 (C4, 2 qn, velocity 31, CC11 22) measures -83.6 dB over the note, peaking at -76 in the first 0.25 s, then decaying.
- Horn 4's identical C at qn 1 (also CC11 22, velocity 31) measures -57 to -61.
- Horn 3 is the only note in the piece under -68 dB (`silent.py`).
- Horn 3 has no keyswitch in parts.json (`ks: []`), while Horn 4 has one at qn 0. The strings at qn 0 do sound (-59 to -52).
- Inferred: an event at exactly qn 0 that Opus does not play. The "qn 0 pre-roll" item was deferred in cycle 3.

Fix (`tools/score_to_parts.py` or `build_reaper.py`):
- Either start the whole project after a one-bar pre-roll (all items, tempo map and render bounds shifted by 3 qn; `render_cycle.py` trims the same time),
- or, as the minimum: send Horn 3's first keyswitch and CC11/CC1 at qn 0, and move its first note to qn 0.05, as was done for late-entering tracks in c03 A4.
- Target: Horn 3 bar 1 within 3 dB of Horn 4's bar 1 entry.

## 5. Horns over the tune: Horn 3's f chord at the second climax and Horn 1's espr. countermelody in bar 55 (measured)

Where and what:
- Bars 79-81 (qn 262-271). Horns 3-4 hold a printed f chord under the ff Vln I tune, with flutes and oboes doubling.
  - Horn 3 (F4/E4/E♭4) measures -28.9 to -30.0 per beat in qn 262-266.
  - Horn 4 on the same chord, CC11 88 and velocity 83, measures -34.6 to -36.2.
  - Horn 3 is level with or above Vln II (-28.0 to -30.5), and only 3.5-4.5 dB under Vln I (-25.5 to -26.1).
  - Rimsky (line 1970): horn = 2 woodwinds in forte, Vln I = 2 woodwinds. So a horn at f should sit under a violin section at ff that carries the tune.
- Bars 54-56 (qn 178-188). Horn 1 "1. espr." p→mp, doubled by Clarinet 1, against Vln I + Vln II unison p→mp→mf.
  - At qn 182-183 Horn 1 measures -36.6 / -35.5 against Vln I -37.5 / -34.2 and Vln II -37.6 / -37.2. It is over each violin section.
  - Bar 55 margin is +1.1 dB.
  - The +8 CC11 boost for "espr." (c01 B6) lifts a countermelody to the level of a tune.

Fix (`build/roles.json`):
- Horn 3 [261.5, 271, -4]
- Horn 1 [176, 188, -3]
- Target: Horn 3 at least 4 dB under Vln I and level with Horn 4 ±2 dB in qn 262-270. Horn 1 at least 2 dB under the louder violin section in qn 176-188.

## 6. Two soft details where an accompanying part covers or matches the line it supports (measured)

- Bars 46-47 (qn 146-152): the oboe "dolce espr." melody, doubled by Vc, rises to mf.
  - The sustained Vln II and Vla chord (printed pp, < mp > pp) measures Vln II -44.4 to -46.6 and Vla -45.4 to -48.3 at qn 147-149, against Oboe 1 -41.5 to -46.7.
  - Vln II is over the oboe at qn 148 (-44.4 against -46.5). Bar 47 margin is -1.5 dB.
  - Fix: roles Violins II [146, 152, -4] and Violas [146, 152, -3].
- Bar 84 (qn 277-279): the timpani pp figure (D♭-C-A♭), the only moving line over ppp Vc/Cb, measures -54.7 to -55.7 in the first 0.3 s, level with Vc -53.9 to -55.4. A printed pp solo figure over ppp should sit about 3 dB over.
  - Fix: `build/note_trims.json` Timpani 277: +3, 278.5: +3, 279: +3 (or velocity 56/60 → 66/68 in the timpani stroke table).

Do not touch:
- Climax bars 61-62 (Vln I on top by +5.5/+5.8) and the c05 B #1-#4 roles that produced margins of +4 to +6 in bars 57-60 and 75-78.
- The horn solo leads in bars 7-14 and 67-70 (+4 to +14 dB).
- Tbn1's ff solo and decrescendo in bars 63-64.
- The timpani roll settle.
- The final-chord viola lifts.
- The Cb 40-90 Hz cut (EQ shelf, highpass, Close 0.4): fix the soft-level deficit with level, not by restoring the boom.
- The volume-envelope scheme (CC11 picks the layer, level trims in the envelope).
