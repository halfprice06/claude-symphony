# Critic B, cycle 8: balance and levels (render c07)

Method. The c07 stems are post-fader (vol_db, roles, trims and mix.json gains included). Levels are K-weighted (BS.1770 filter as a zero-phase FIR) in 10 ms frames. Per-note levels run from the score onset (`sq`) + 80 ms to min(note end, onset + 1.5 s). Per-beat levels use the parts.json tempo map. "Residual" is a note's level minus its track's robust level-against-CC11 fit, with vol_db removed. c06 comparisons use critic B c07's frames of the c06 render. Scripts and outputs: `/private/tmp/claude-501/mockup-loop/c08-B/` (`lib.py`, `prep.py`, `beats.py`, `cbp.py`, `mel.py`, `bass.py`, `hot.py`, `pitchres.py` residuals by pitch, `cmp.py` c06-vs-c07 per-note segments, `fam.py`).

What c07 fixed (measured): Horn 2 at qn 204-207 is now -32.2 to -33.7 (it was -27.9). At bars 79-80, Cb is level with or above Cbn, and Vc is level with Bn1 on the tenor line. The bar 69 horn margin is +2.8. pp medians still agree across families: winds -50.0, horns -50.1, strings -51.3, harp -52.0. Melody margins: +4.2 to +6.2 at bars 57-62, and +3.3/+3.5 at bars 79-80.

## 1. Flute 1's top octave (G6-B flat 6) is 2-5 dB hot on every articulation, so the flute equals or tops the Vln I tune it doubles at the three peak moments (measured)

Where: bar 58 (qn 191.5-196), bar 79 (qn 262), bar 81 (qn 268). Flute 1 plays in unison with Vln I in all three places.

What:
- `pitchres.py`, Flute 1 residual by pitch:
  - MIDI 84: +4.2
  - 89: +2.0
  - 90: +3.5
  - 91: +3.8
  - 94: +4.6
  - From 70 to 87 the residual is -4.2 to +1.5.
- Bar 58 is printed p < f, and the hairpin reaches f at bar 59.
  - Per beat, qn 193 / 194 / 195: Fl1 -29.7 / -30.4 / -28.1. Vln I -30.6 / -29.4 / -29.2.
  - Then at the printed f (qn 196-199), Fl1 falls to -32.1 / -32.5 / -34.4 / -37.4 while Vln I is at -26.8 to -29.3.
  - So the flute is loudest inside the crescendo and 4-8 dB softer when the f arrives: the printed shape runs backwards. The cause is the B flat 6 at qn 193, residual +5.3.
- Bar 79, qn 262 (B flat 6, ff): Fl1 -26.0 against Vln I -25.4. This was open in c07.
- Bar 81, qn 268 (G6, ff >): Fl1 -23.9 against Vln I -26.0. The flute is 2.1 dB over the violins and is the loudest stem of the beat.
- Rimsky-Korsakov (rimsky-principles p0051): in forte, Vln I = 2 flutes. A flute doubling the violin tune at f/ff therefore belongs about 3 dB under it.

Fix:
- `build/pitch_trims.json`, Flute 1: add `"84": -3, "89": -2, "90": -3, "91": -4, "92": -2, "93": -2, "94": -4`.
- These are mostly Sus notes, so they need all articulations. The existing `"78": 4` must stay legato-only, because Fl1 78 on Sus has a residual of -1.0.
- `tools/score_to_parts.py`, the c06/c07 pitch-trim block (about line 1204): accept `"_all_arts_pitches": [84, 89, 90, 91, 92, 93, 94]`. A pitch in that list is trimmed on every articulation; other pitches keep the Leg-only rule.
- `build/note_trims.json`: Flute 1 262 -3 → 0, and 254 -8 → -4. The pitch trim now covers these notes. Check the numbers after the render.
- Target:
  - Fl1 2-4 dB under Vln I per beat at qn 193-195, 262 and 268.
  - Fl1 level at qn 196-199 (the f) at least as high as at qn 193-195.

## 2. The Vc "cantabile" countermelody in bars 71-74 is buried under the second violins' harmony line by two old cuts (measured)

Where: bars 71-74 (qn 238-250), Violoncellos. The score marks Vc "cantabile", p, against Vln I (tune, p espr.) and Vln II (thirds under the tune, p). Violas and Cb are pp.

What:
- Per bar, Vc -47.4 / -44.9 / -42.7 / -45.5 against Vln II -41.4 / -39.2 / -37.7 / -39.8 and Vln I -38.3 / -34.0 / -32.9 / -33.7.
- So the counterline is 4-6 dB under the harmony line and 9-11 dB under the tune.
- The entry at qn 238 (E flat 3) measures -48.4, under the violas' pp (-48.8) at the same moment.
- Vc vol_db over bars 71-74 is -3 throughout (role [238,250,-3]) and -12 to -13 from qn 238.4 to 239.6 (note trim 238 -10 on top). Both date from c04, when the Vc stood 2 dB under Vln I. Since then:
  - Vln I gained the [244,262,+2] role.
  - The c06 soft-trim table changed the p levels.
- Bars 23-26, the other Vc "cantabile" line, sit level with Vln II (Vc -44.3 / -43.2 / -41.0 / -44.0, Vln II -43.6 / -44.5 / -42.1 / -45.5). This shows the intended balance.
- Inferred: a listener hears bars 71-74 as tune + harmony + bass, with no countermelody.

Fix:
- `build/roles.json` Violoncellos: [238, 250, -3] → [238, 250, 0].
- `build/note_trims.json` Violoncellos: 238 -10 → -6.
- Target: per bar in 71-74, Vc within 2 dB of Vln II, and 4-7 dB under Vln I. The qn 238 entry at least 2 dB over the violas.

## 3. Clarinet 1's A flat 5 legato boost (+5, c06) fires at ff: in bars 79-80 the clarinet's harmony note is the second-loudest stem (measured)

Where: bar 80 (qn 266-268), Clarinet 1, A flat 5 (MIDI 80, Leg). The same pitch is doubled by Vln II and Oboe 1.

What:
- `pitch_trims.json` Clarinet 1 `"80": 5` was set for a soft legato sag. At qn 266 its vol_db reads +4.2 to +6.5 dB (the pitch trim plus the long-note swell).
- Per beat, qn 266 / 267:
  - Cl1 -26.8 / -28.6
  - Vln II (same pitch) -27.1 / -29.3
  - Oboe 1 (same pitch) -31.7 / -34.1
  - Vln I (tune) -23.1 / -25.8
- In qn 264-267 Cl1 is the loudest stem after Vln I. Its residual at 266 is +0.5 *after* the boost, so the boost is not making up for a weak sample there.
- This also explains why the bar 79-80 melody margin (+3.3 / +3.5) is the smallest of the climaxes.

Fix:
- `build/note_trims.json` Clarinet 1: add `"266": -5`, which cancels the pitch trim on this note only.
- Keep `"80": 5` for the soft legato notes it was made for (Cl1 255 residual +4.3 at CC 72 shows the sample is not weak there either; re-check `80` in a later cycle).
- Target: at qn 266-267, Cl1 within 2 dB of Oboe 1, at least 5 dB under Vln I, and the bar 80 melody margin at +4.5 or more.

## 4. The harp harmonics (bars 82-83) play at mp instead of the printed p and are the loudest stem at the start of the coda (measured; the cause is a code bug)

Where: qn 273-277, track Harp harmonics.

What:
- The harp's p in bar 82 is printed on the lower staff (`HarpL 271.0 dynamic p` in mockup-events.tsv).
- The Harp harmonics track reads only the `HarpR` staff (parts.json `staves: ['HarpR']`). Its last dynamic there is mp, so all five harmonics get velocity 76, the mp value. The Harp track's own p chords at 271-272 get 64/68.
- Per half beat, qn 273-276.5: harmonics -41.4 / -38.9 / -42.0 / -48.6 / -55.1 / -43.9 / -40.4 / -50.8.
- Against that:
  - the harp's p chords at 271-272: -44.7 / -46.4
  - Vc ppp: -51 to -55
  - Cb ppp: -56 to -61
  - Violas: silent until 276.5
- The harmonics are 3-6 dB over the harp's ordinary p notes and 8-12 dB over the ppp strings. Metrics "loudest three" puts them first in bars 82 and 83.
- A real harp harmonic is a soft, distant sound, weaker than an ordinary pluck at the same dynamic. This is inferred, from Adler's harp chapter and Rimsky's note on harmonics as a pp colour.

Fix:
- `tools/score_to_parts.py`, the harp/harm velocity block (about line 743): for family `"harm"`, take `base()` from the Harp track's staves (`HarpR` + `HarpL`). One way is to give the harmonics track `staves: ["HarpR", "HarpL"]` for the dynamic curve only, keeping the flageolet note filter on HarpR.
- Then subtract 6 from the harmonics' velocity (`n["vel"] -= 6` for `family == "harm"`). That gives about v58 at p.
- Leave mix.json gain_db at -2.
- Target: harmonics -47 to -50 per half beat in qn 273-277. That is 2-4 dB under the harp's p chords and 2-4 dB over the Vc ppp.

## 5. The c07 A flat 1 trim on the double basses (-5 dB, all articulations) also cuts the two long tonic pedals of the coda, so the basses drop 5-8 dB under the celli at ppp (measured)

Where:
- Cb qn 271 (A flat 1, 15 qn, bars 82-86, p > ppp)
- Cb qn 292 (A flat 1, 12 qn, bars 89-92, pp > ppp)

What:
- Cb minus Vc per bar:

| Bars | c06 | c07 |
|---|---|---|
| 83 / 84 / 85 / 86 | -1.6 / -1.2 / -2.7 / -0.7 | -5.1 / -6.2 / -7.8 / -5.7 |
| 89 / 90 / 91 / 92 | +0.3 / +0.7 / -0.5 / -1.4 | -4.6 / -4.3 / -5.5 / -7.0 |

- In soft bars elsewhere the median is -0.7 to -1.5, so the coda is the exception.
- `cmp.py`, Cb 271, segments 0-1.5 / 1.5-4 / 4-8 / 8-15 s:
  - c06 -44.5 / -50.7 / -54.9 / -53.2
  - c07 -47.2 / -53.7 / -58.6 / -58.2
- The hot A flat 1 was measured on notes of 1-4 qn at CC 39-52 (qn 66, 72, 78, 87, 164, 168, 238, 244, 250). Those are fixed: bar 30 Cb-Vc +10.7 → +5.8, bar 51-52 +7.2 / +8.8 → +3.1 / +4.8. The long ppp sustains were never hot. In c06 the bass in bars 83-86 sat level with the celli.
- Inferred: the final tonic loses its floor, and the last chord sounds cello-bottomed.

Fix:
- `tools/score_to_parts.py`, pitch-trim block (about line 1208): for notes longer than 4 qn, end the trim at onset + 3 qn instead of at the note end:
  ```python
  end = orig_end[id(n)] if orig_end[id(n)] - n["qn"] <= 4 else n["qn"] + 3
  vol_parts.append(("note", n["qn"] - 0.1, end, pt[n["pitch"]], 0.25))
  ```
  This keeps the attack cut that fixed bar 82, where Cb-Vc is now -0.2.
- Target:
  - Cb minus Vc between -3 and +1 in bars 83-86 and 89-92.
  - Bar 82 stays within ±2.
  - Bar 30 and bars 51-52 unchanged.

## 6. Soft viola chords cover the oboe solo entries in bars 15 and 45 (measured)

Where:
- Bar 15 (qn 42-45): Oboe 1 "1." p < > against Violas, Vln II and Vc pp con sord.
- Bar 45 (qn 140-144): Oboe 1 dolce espr. p against Violas pp arco, Vln II pp, Cb pp.

What:
- Bar 15, per beat, qn 42 / 43 / 44: Oboe -52.6 / -47.9 / -40.7; Violas -50.9 / -45.8 / -46.2. The violas are 2 dB over the solo on beat 2.
- Bar 45, qn 141 / 142 / 143: Oboe -40.6 / -44.5 / -44.5; Violas -44.9 / -43.6 / -43.5. The violas are 1 dB over the solo on beats 3-4.
- The viola F3 at qn 140 (6 qn, CC 34-38) measures -47.2 per note and rises to -43 by beat 3 (the long-note swell, +1.5 dB in vol_db, plus the CC11 swell). Violas' pp median is -51.8.
- Rimsky (p0051): in piano a whole string department equals one wind instrument. A pp department under a p solo wind therefore belongs at least one level (about 4 dB) under it.

Fix (`build/roles.json`, Violas):
- add [42, 48, -3]
- add [140, 146, -4] (the existing [146, 152, -3] continues it)
- Optional: exclude violas from the long-note dB swell when the printed dynamic is pp (`score_to_parts.py`, c06 C #5 swell).
- Target: Oboe 1 at least 3 dB over Violas on every beat of qn 43-44 and 141-144.

Do not touch:
- The soft-trim table and its overrides (pp medians agree within 2 dB across winds, horns, strings and harp).
- The c07 horn pitch trims (Horn 2 at bar 61 now -32 to -34).
- The c07 climax bass-line trims (Cb level with Cbn, Vc level with Bn1 at bars 79-80).
- The Cb A flat 1 trim on short notes (bars 30, 51, 52).
- The bar 57-62 melody margins (+4.2 to +6.2).
- The Tbn1 solo in bars 63-64 (+4.2 / +9.8).
- The timpani roll settle.
- The volume-envelope scheme.
