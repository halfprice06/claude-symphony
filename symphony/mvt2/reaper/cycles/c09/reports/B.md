# Critic B, cycle 9: balance and levels (render c08)

Method. Levels are K-weighted (BS.1770 filter as a zero-phase FIR) in 10 ms frames, taken from the c08 post-fader stems on the c08 parts.json tempo map. Per-note levels run from the score onset (`sq`) + 80 ms. c07 comparisons use critic B c08's frames of the c07 render on the c07 tempo map (`cycles/c08/before/build/parts.json`). The renders are deterministic: wherever c08 changed nothing, the c07 and c08 numbers agree to 0.1 dB. Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c09-B/`:
- `prep.py`, `lib.py`
- `beats.py` (per-beat stems with CC11 and vol_db)
- `share.py` (Vln I share of the mix)
- `inv.py` (pairs of stems whose printed dynamic and measured level are in the wrong order)
- `steps.py` (vol_db steps inside held notes)
- `cmp78.py` (c07 vs c08)
- `bands.py`, `refb.py`, `stemb.py` (1/3-octave bands, loud frames)
- `dyn.py`, `mel.py`, `bass.py`

What holds (measured):
- Solo entries marked p land within 6 dB of each other across families:
  - Horn 1, bars 7-14: -38 to -43
  - Oboe, bars 15-16 and 45-47: -42 to -44
  - Flute, bars 37-40: -41 to -48
  - Cor anglais, bars 41-51: -39 to -44
- pp medians: winds -50.0, horns -50.1, strings -51.3.
- At the bar 61 climax, low brass at mf sits 2-6 dB under the woodwinds' ff. This fits Rimsky's ratio of one trombone to two horns to four woodwinds at the same dynamic (rimsky-principles p51), two printed levels down.

## 1. The winds and strings drop 4-8 dB in the middle of the build to the main climax (bar 59 beat 3 to bar 60), because the bar 59 hpgain is released before the bar 60 crescendo starts (measured)

Where: qn 197.5-202, bars 59-60. All winds, Vln I/II, Vla, Vc, Cb.

What:
- Winds are printed f at qn 196, with a crescendo from qn 200 to ff at qn 204. Strings follow the same shape.
- The first hairpin's hpgain (+4 winds, +3 strings) is held to the next onset, released over 1 qn, and is back to 0 by about qn 198.5. The next hairpin then starts again from 0.
- Fl1 vol_db goes +5.0 (qn 198.25) → -2.8 (200.25). It returns to +0.8 only at 203.75.
- Per beat, wind section: 196 **-24.3**, 197 -23.5, 198 -28.3, 199 **-30.8**, 200 -28.7, 201 -27.2, 202 -25.3, 203 -25.3, then 204 -20.1.
  - The winds' f in bar 59 is louder than any point of their bar 60 crescendo to ff.
  - qn 199-200 sits below the bar 58 p crescendo (qn 193: -28.1).
- Per stem, arrival beat → two beats later, at the same printed f: Fl1 -30.0 → -34.7, Ob1 -30.8 → -37.0, BCl -37.0 → -41.7, Vc -32.6 → -39.5, Vln I -25.9 → -29.0.
- Mix: -20.6 (196) → -25.2 (199) → -13.3 (204). A listener hears the build arrive at bar 59, sag, and then jump 12 dB into bar 61.
- This is the only place where two crescendos to f+ follow each other. At the other arrivals (204, 259) the median change after the arrival is -0.1 and +2.0 dB.

Fix: `tools/score_to_parts.py`, the c06/c08 hpgain block (about line 1241) and `vol()` (about line 1193).
- After the per-track hpgain items are built, chain them. If the next crescendo-to-f+ hairpin on the track starts within `HP_CHAIN = 6.0` qn of an arrival `b1`, and no printed mark between `b1` and the next start `a2` is lower than the arrival dynamic:
  - set the first item's `hold_end` to `a2`
  - give the second item a start value equal to the first item's gain
- In `vol()`, ramp from that start value instead of from 0: `v += s + (g - s) * (q - a) / (b2 - a)`, where `s` is the optional 6th field (default 0).
- At bar 59-60 this holds +4 (winds) / +3 (strings) from 196 to 204. The ff arrival at 204 is unchanged (still +4/+3).
- Target, measured on the new render:
  - wind section at qn 199-201 within 2 dB of qn 196-197 (now 5-7 dB under)
  - Fl1 and Ob1 at 199-201 at -33 or louder
  - the mix never falls more than 2 dB between qn 196 and 204
  - bar 61 unchanged (mix -14.2 K)

## 2. The c08 B #5 change (pitch trims on notes over 4 qn end at onset + 3 qn) puts a sudden +5 dB step into three held double-bass pedals, against the printed dynamic (measured; regression)

Where: Double basses. Ab1 pedal qn 3-9 (step at qn 6, bar 3), qn 271-286 (step at 274, bar 83, where ppp begins), qn 292-304 (step at 295, bar 90, pp >).

What:
- vol_db holds -5 and jumps to 0 inside 0.1 qn: (292.15, -5) → (295.1, 0). `steps.py` finds these three +5.0 steps, all with printed pp/ppp.
- c07 vs c08 Cb per beat: identical before each step and exactly +5.0 after it.
  - qn 6: -52.6 → -47.7
  - qn 274-285: -57.9..-54.1 → -53.2..-49.1
  - qn 295-303: -49.6..-61.4 → -44.8..-56.4
- Bar 90 downbeat: Cb -52.2 (qn 294) → -44.8 (qn 295), a 7.4 dB rise inside a tied pp > ppp pedal. It is the loudest stem of the beat.
- This is the "Cb 4.5 dB over Vc in bars 89-92" left open in c08. It is not the Vc role.
  - Cb minus Vc, bars 89 / 90 / 91 / 92: -0.6 / **+4.7** / **+3.5** / +2.0.
  - Bar 3: Cb +4.9 over Vc, and the loudest string at qn 6 (-47.7).
- Bars 83-86 needed the lift. Cb minus Vc there is now -0.2 / -1.2 / -2.8 / -0.8 (c07 -5 to -8). Bars 89-92 already have the c08 Vc role [292, 304, -4], so the same lift overshoots there.

Fix:
- `tools/score_to_parts.py`, the pitch-trim loop (about line 1274): remove `if e - q0 > 4: e = q0 + 3`. Trims run to the note end again, as in c07.
- `build/roles.json`, Double basses: add `[274, 286, 4]`. Its 0.5 qn ramp from 273.5 replaces the step with a ramp into bar 83.
- Expected values (c08 numbers minus the step, plus the role):
  - Cb minus Vc, bars 83-86: about -1 to -4
  - Cb minus Vc, bars 89-92: about -0.5 / -0.3 / -1.5 / -3.0
  - bar 3 back to c07 (Cb -52.6 at qn 6)
- Target: no vol_db step of 3 dB or more inside a held Cb note (`steps.py`). Cb minus Vc between -3 and +1 in bars 83-86 and 89-92.

## 3. Untargeted < > swells ratchet the level up: the decrescendo falls 14 CC after a 22 CC crescendo, so the line ends about one dynamic level above where it started (measured)

Where:
- Vln I and Vln II bars 71-74 (qn 240-244 swell, then 244-250)
- Vln I/II bars 23-24 (qn 68-72)
- Oboe 1 bars 15-16 (42-47)
- Horn 1 bars 7-8 (20-24)

What:
- `base_points()` gives an untargeted crescendo from mp or below HP_STEP_SOFT = 22 CC.
- The decrescendo that follows starts above mp + 2, so it falls only HP_STEP = 14 (or less).
- CC11 before → peak → after:
  - Vln I/II bar 73: 46 → 68 → 58 (+12)
  - Vln I/II bar 23: 58 → 80 → 66 (+8)
  - Ob1 bar 15: 46 → 68 → 54 (+8)
  - Hn1 bar 7: 46 → 68 → 54 (+8)
- Measured, Vln I: -39.1 at qn 238-239 (p) → -32.8..-35.8 at qn 244-249, still printed p. The printed mp at bar 75 (qn 250-252: -33.0) is then no louder than the p before it.
- Vln II rises -41 → -37.5 the same way.
- In bars 72-74 Vln I is 61-69% of the mix energy and 14-16 dB over the pp violas. In the parallel bars 23-26 the gap is 8-10 dB.
- A messa di voce (< >) returns to its starting dynamic (inferred from performance practice; the score marks no new dynamic after it).

Fix: `tools/score_to_parts.py`, `base_points()` (about line 414).
- Keep `last_un = (stop, start_level, kind)` for the last untargeted hairpin.
- When an untargeted hairpin of the opposite direction starts within 0.3 qn of `last_un[0]`, set `tgt = last_un[1]`. The existing "do not overshoot the next mark" rule still applies after this.
- Target:
  - Vln I at qn 244-249 within 1.5 dB of qn 238-239
  - Vln I at bar 75 (mp) 2-4 dB over bar 74
  - Ob1 at qn 46-48 back to its qn 42 level (CC 46)

## 4. At the bar 61 climax the theme is in octaves (Vln I / Vln II / Vc, with Fl2), but Vln I sits 7-8 dB over its own octave doublings and takes 37% of the mix energy (measured levels; norm inferred)

Where: qn 204-208, bar 61. Vln I plays Db6-F6-E6. Vln II plays the same line an octave lower, Vc two octaves lower (all ff, molto sostenuto). Fl2 joins the Vln I octave.

What:
- Per beat, qn 204 / 205 / 206 / 207:
  - Vln I -16.6 / -19.0 / -19.2 / -19.6
  - Vln II -25.0 / -27.5 / -23.6 / -26.2
  - Vc -23.2 / -25.2 / -28.2 / -31.7
  - Fl1 (Ab6 pedal above) -24.6 / -25.8 / -25.6 / -23.4
  - whole brass section -24.0 / -23.6
- In bar 61 Vln I is 6.3 dB over the next stem and holds 37% of the mix energy. At bars 79-80, the same printed ff and the same kind of tune, its margin over Vln II is 3.3 / 3.8.
- Rimsky (rimsky-principles p51): in forte, one string department equals two woodwinds, and departments are equal to each other. A melody doubled by the second violins at the octave should thicken, with the top octave leading by register. Here the octave doublings sit as an accompaniment, 7-8 dB down.
- The lift comes from:
  - Vln I gain +5
  - dyn_trim ff +1.5 (Vln II -1.5)
  - the [188, 204, +2] role ramping out over qn 204-204.5
  - hpgain +3 and the sostenuto tenuto hold

Fix: `build/roles.json`:
- Violins I: add `[204, 208, -2]`
- Violins II: add `[204, 212, 2]`
- Leave the Vc [204, 212, -3] role. Vln I minus Vc goes from 4.6 to about 2.6, so if the actor wants to keep c08 C #6's "at least 3" exactly, use -1.5 on Vln I.
- Target, qn 204-208:
  - Vln I 3-5 dB over Vln II
  - Vln I share of the mix energy at or below 30%
  - bar 61 still at least 3 dB over bar 79 in the mix (now 4.9 K; the change costs about 0.6)

## 5. The harp harmonics (printed p) now sit under the ppp strings (measured; c08 overshoot, already open)

Where: qn 273-277, bars 82-83.

What:
- Harmonics -49.4 (272.5), then -56.4 / -56.6 (qn 274-277).
- Against them: Vc ppp -56.7 / -51.3, Cb ppp -53.3 / -53.6.
- The harmonics are 0-5 dB under strings printed two levels softer. c08's v58 measured -57.7, against -47.7 at v76 (about 0.55 dB per velocity step).

Fix: `build/mix.json` Harp harmonics `gain_db` -2 → +6. This keeps the softer v58 layer that suits the colour, and should give about -49.5. The alternative is HARM_VEL_CUT 6 → -8 (v72).
- Target: -47 to -50 per half beat in qn 273-277, 2-5 dB over the Vc/Cb ppp and under the harp's p chords (-44.7 / -46.4).

## 6. Bassoon 2's f arrival in bar 78 is the loudest woodwind, over the melody flute, then falls 9 dB at the ff (measured)

Where: qn 259-261, Bassoon 2 E3 (bass line, doubling Vc/Cb). The melody is Vln I + Fl1, with Cl1 a third below.

What:
- Bn2 vol_db reaches +5.5 at qn 259.8: hpgain +4 held, plus the long-note swell +1.5, plus mix.json dyn_trim f +2.
- Per beat, qn 259 / 260:
  - Bn2 -29.8 / -31.1
  - Fl1 -34.2 / -35.9
  - Cl1 -38.2 / -37.5
  - Cb -39.0 / -39.2
  - Vln I -26.1 / -27.4
- At the ff (qn 262-265) Bn2 falls to -39.6..-41.0, under the Db3 -5 pitch trim. So its bar 78 f is 9-10 dB louder than its bar 79 ff, and it is the second-loudest stem of bar 78 (metrics).

Fix: `build/note_trims.json`, Bassoon 2: add `"259": -5`.
- Target: Bn2 at qn 259-261 between -34 and -36, under Fl1, and no more than 4 dB over its bar 79 level.

Do not touch:
- The soft-trim table and per-track overrides (pp and p agree across families).
- The p solo levels (Horn 1, Oboe, Flute, Cor anglais, Vln I solo).
- The hpgain hold at the ff arrivals (qn 204, 262: no fall after the arrival).
- The low-brass mf levels at bar 61 (2-6 dB under the woodwinds' ff).
- The Tbn1 solo in bars 63-64.
- The bars 83-86 Cb/Vc balance (keep its level through the role in finding 2).
- The bar 57-62 and 75-81 melody margins (+4 to +6) outside qn 204-208.
- The volume-envelope scheme.
