# Cycle 61, critic A: articulation and phrasing (coordinator item 3: repeats, sags, doubled attacks, join and re-bow holes, timpani, fugato bar 87, Oboe 1 166-169, horn slurs onto G#4, wind legato velocity)

Under review: the c60 render (`cycles/c60/render/`, pass-2 stems in `render/`) and `cycles/c60/rendered_build/` (`build/parts.json` is byte-identical to it). Comparisons use the c59 and c56 renders (c56 is the last render with per-note volume). Scripts and caches (67 MB): `cycles/c61/critic_scripts/A/` (`liba.py` loads `tools/build_reaper.py` cut before `ENV_LUA`). Levels are 30 ms frames with a 10 ms hop, measured on the dry stems. "Master band" means the master filtered to 0.8-5 times the note's fundamental. "Control" is the same statistic 0.6-1.2 s away from the event. Nobody listened. Every number is measured unless it is marked as inferred. "qn" is the score quarter note; bar = qn/4 + 1.

Not read this cycle: README, HISTORY (only searched), LEARNINGS, EW-TEMPLATE-PLAN, FINDINGS. So I cannot say which template sections are still unapplied. Read: the c61 coordinator notes, the critic prompt, `cycles/c60/CHANGES.md`, the faults table and list, the accent table, `faults60.py` / `lib60.py`, DIGEST.md, and the manual pages below.

## Manual notes (May 2021 HO manual)

| Manual (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.105: brass Legato Slur, "MIDI Velocity is used to control the speed of the legato transitions" | horn and trumpet slurs | yes. Brass legato targets are at velocity 110-127 (63 of 68) and their median dip is 1.0 dB |
| p.111-112: woodwind Legato / Legato Slur. Slur only with no gap and within an octave; the patch plays 3 sustain samples plus slur samples. These pages say nothing about velocity | the finale's proposed floor of about 96 for wind legato velocity | the floor rests on the brass text and on the finale's data. Here the wind dips do not depend on velocity (finding 1) |
| p.124: Timpani Felt Long, "the felt coating on the mallets makes each note quite soft"; velocity gives up to 16 layers. Timpani Hard Long: "a brighter timbre overall" | the f/ff strokes (finding 4) | felt only. Velocity is at 112-127 on every f/ff stroke, so there are no layers left above it |
| p.101-102 (DIGEST): velocity is ignored on KS Master sustain rows | Sus MAX same-pitch repeats, re-bows | the c60 data do not try to separate repeats by velocity: correct |

## 1. Wind legato dips returned where per-note rows were removed. The worst is the opening cor anglais solo, bar 7.5 (G4 -> G#4). Measured; sizes after are inferred.

Script: `legvel.py`, `legvel2.py`, `legvel3.py`. I took every wind and brass note that starts while the previous note on a legato row still sounds (184 targets) and measured its dip: the lowest level from -0.03 to +0.3 s, relative to the lower of the previous note and the new note's body.

- **Cor anglais qn 26 (bar 7.5), G4 -> G#4, velocity 80, CC11 87, Leg Slur MAX.** The stem falls from -33.0 (the G4) to -42.8 dB at +0.16-0.24 s and comes back at +0.5 s. That is a 9.6 dB stem dip, and in the master band it is +8.8 dB over control. c56 measured 1.7 on the stem and -0.2 in the master: the c29 per-note row covered it, and that row is gone. This is the first wind solo of the piece, and the dip is the most audible articulation fault I found.
- Other wind legato dips that show in the master band (over control): Clarinet 1 qn 516 (bar 130) +6.3 (c56 +6.9), Flute 1 qn 439 (bar 110.75) +5.7 (c56 +3.6), Oboe 1 qn 582 (bar 146.5) +3.9, Bass clarinet qn 4 (bar 2) +3.6 (c56 +2.7). Of the 27 targets with a stem dip of 6 dB or more, 22 stay within 2.5 dB of control in the master.
- **Velocity floor (coordinator: finale's floor of 96): do not adopt it here.** The master band dip at wind targets is 2.1 dB at velocity under 70 (n 36), 2.5 at 70-95 (n 67) and 2.5 at 96-127 (n 13). The stem medians are 3.5 / 3.6 / 5.0. Raising velocity would make every slur in a lyrical movement faster (p.105) and buy nothing measurable.
- The faults tool misses these dips. Its join window ends at +0.10 s, and the wind legato dips sit at +0.12-0.26 s (median +0.16).

**Fix.** Range-render two forms for Cor anglais qn 26 and keep the one with the smaller master band dip and no front burst:
- (a) `ART_SPANS["Cor anglais"]` += `{"from": 25.8, "to": 26.95, "art": "Sus MAX"}`. The G#4 becomes a soft re-attack under the slur. This is the finale c21 fix for the cor anglais legato bloom.
- (b) `VEL_SET["Cor anglais"] = {26.0: 115}`, a faster transition.

Do the same for Clarinet 1 516 and Flute 1 439. Expected: the CA 26 master dip goes from +8.8 to 3 dB or less (inferred from c56's 1.7 stem / -0.2 master with the row). In `faults60.py`, extend the join window to +0.30 s for legato targets.

## 2. CC11 steps at printed dynamics stay on the score onset while the note-on moves earlier: 55 notes start 8-38 units under their own level. Measured.

Script: `leadtaper.py`. A note with an entry or legato lead starts up to 0.5 qn early, but the CC11 step for its printed dynamic, and the end of the previous phrase's taper, stay at the score onset. The front of the note therefore plays at the old, lower level. There are 55 such notes (11 at phrase starts): Violins I 13, celli 7, Violins II 5, flutes 9, the rest winds and basses.

- **Celli qn 620 (bar 156), B-flat 2, printed mp with a crescendo.** The note-on is at 619.734 and the CC11 there is 42, still in the taper of the phrase that ends at the printed p. The lane reaches 62 only at 620.125. The note sits at -52.9 to -55.2 dB for 0.25 s, against -41.3 for the next eighth. Master band dip 7.9 dB against 1.6 control. This is the "celli 620" join hole on the coordinator's list.
- Celli qn 183 (bar 46.75): CC11 34 at the moved note-on, 72 at the onset (lead 0.515 qn). Violins I bars 117-119: CC11 104 at the note-on, 116 at the onset (leads 0.21-0.28 qn). The accent arrives after the note has started, which pulls the perceived attack later (S2).

**Fix** (`tools/score_to_parts.py`, the CC11/CC1 lane writer; generic, no per-note values): a rise of 8 units or more within 0.05 qn of a score onset moves to that onset's earliest moved note-on minus 0.01 qn, and a phrase-end taper (`PHRASE_SHAPE` "end") ends at the next phrase's moved note-on. This is the finale c22 rule ("move CC11 falls with any note-on leads") applied to rises. Expected: the celli 620 master dip goes from 7.9 to about 2-3 dB (inferred: 20 units at 0.41-0.45 dB per unit). The 55 fronts reach their printed level at the note-on.

## 3. Celli subito pp, qn 286 (bar 72.5): the Leg Slur MAX first-note layer fades in for 0.8 s after the accented strokes. Measured; size after is inferred.

The marcato strokes at qn 284 and 285 (Sus Marc LITE) are at -29 to -32 dB. The pp G#3 at qn 286 (Leg Slur MAX, velocity 41, CC11 34) measures -47.3 dB at +0.08 s, -53.4 at +0.32 and -59.1 at +0.5, and reaches -46 only at +0.8 s. Master band dip 6.7 dB against 0.7 control. The faults list shows the same note as "hole +16.5", "sag +18.5" and "pulse +10.4". The printed sound is an immediate pp, not a slow swell. **Fix:** `SUS_ENTRY_AT["Violoncellos"]` += `[286.0]` (the existing key: Sus MAX for a note after a gap on a legato row). Expected: Sus MAX at CC11 under 70 is 6-8 dB under its body at 0.2 s and 2-5 dB at 0.3 s (c60 A's rise data), so the master dip falls to about 3 dB (inferred).

## 4. Timpani strokes: in the 50-250 Hz band they still lead the orchestra; the stick sound is 13.5 dB under the master. A brighter mallet is a better instrument-side lift than more level. Measured; size after is inferred.

Script: `timp.py`, `timp_hi.py`, on the 57 f/ff/fff strokes on the Lng row.
- Stroke peaks on the stem: c60 is 4.0 dB under c59 and 2.3 dB under c56 (median). Velocity is already 112-127 (`TIMP_STROKE_VEL`) and CC7 is 127.
- Share of the master's 50-250 Hz band at each stroke (timpani stem against the master): c60 -1.9 dB, c56 -2.0. The drums still carry most of the low band at every stroke, as in c56.
- Stick definition (0.7-3 kHz, first 60 ms): timpani -13.5 dB under the master (c56 -14.6). The strokes are boom without stick. That is where the weight is missing, and more level will not fix it.
- The eighth-note ff strokes at bars 82-83 and 131-134 now alternate strong and weak by velocity (117-120 against 124-127): about 2-3 dB between beats and off-beats, as in c56. Keep it.

**Fix (test both):**
- (a) A pass-2 alias "Timpani hard" on `Timpani Hrd KS.oib` (installed; p.124, "brighter timbre") for the Lng strokes of the ff passages: bars 26-33, 82-83, 131-134, 141-143 and 170. The felt instance keeps every roll and soft stroke.
- (b) Cheaper: `mix.json` Timpani `mic_db.Close` -14 -> -8 (the Close mic carries the stick).

Expected: the stick share goes from -13.5 to about -8 dB with (a) and about -10 with (b), with the low-band share unchanged (inferred). No per-stroke shape.

## 5. Oboe 1 qn 164-169 (bars 42-43): c60 removed the c59 hole, but the lane sags under the held mf and bounces up at the F5. Measured.

Stem median levels, c60 (c59):

| qn | 164.5 | 165.6 | 166 | 167 | 168 |
|---|---|---|---|---|---|
| level, dB | -45.3 (-48.0) | -50.9 (-52.3) | -46.1 (-55.1) | -49.1 (-59.6) | -49.0 (-57.7) |

On the tied G5, CC11 falls 58 -> 51 after the printed mf at 164 (nothing else is printed until the decrescendo at 166). It then jumps to 65 at the F5 (165.75-165.8): a +4.8 dB bounce, which is the "hole 166 +9.5" in the faults list. The printed decrescendo from 166 to the p at 168 is now only 3 dB, and the p E-flat 5 is as loud as the F5's body. That is the +8-10 dB over c59 the coordinator noted: the E-flat 5 soft-layer region gain of +7, on top of the CC11 floor of 34. Master share: Oboe 1 is -45 dB against the master's -34 in 166-168, level with Clarinet 1 (-46.9).

**Fix:** `CC11_LANE["Oboe 1"]` += `[(164.0, 58), (165.85, 58), (167.9, 38), (168.9, 36)]` (a phrase lane, flat across the tie). Keep the floor and the region gains. Expected: the bounce goes from +4.8 to under 1 dB, and the decrescendo 166 -> 168 from 3 to about 5 dB (inferred, 0.3 dB per unit on this stem).

## 6. Verdicts on the remaining coordinator questions (measured unless marked)

- **Same-pitch repeats 49 -> 114: not audible as faults.**
  - The increase is the long-join same-pitch gap of 0.025 s: 72 of 151 long joins fall under the 3 dB threshold.
  - At the 91 long-join same-pitch joins, the master band dip is 1.9 dB (c59 2.75; control 0.7) and the stem dip is 3.1 (c59 6.5). The chorale re-tongue is now a trace, not a gap, and none reaches a hole.
  - Three marked repeats lack a re-attack. Bassoon 2 qn 160 (sf, bar 41): stem rise 0.8 dB. Bassoon 1 qn 548 (accent): rise 0.1. Bassoon 2 qn 676 (accent, ff): rise 0.8. All three sit inside tutti chords and the master shows nothing; they were the same in c59.
  - Change: `faults60.py` should count long-join same-pitch joins separately, or count them only if the master band dip is over 3 dB.
- **Sags 61 -> 68: not a new fault.** In `sags.py` the 68 split as follows:
  - 11: the long-join overlap. The front window holds the old chord tone. This measurement artefact accounts for the +7.
  - 31: CC11 or envelope falls in the data. Most are the "lyric" phrase-end taper (end -12 × wind gain 1.4), plus printed fp (basses bar 33) and the final decrescendo.
  - 15: sample decay at a flat CC: horns at CC1 54 or lower, celli and violas on Leg BC in bars 171-172.
  - 10: the sample's attack peak over its body.
  - Wind phrase ends drop 5.5 dB over the last second (median, q75 9.0, 10 of 25 at 6 dB or more). c56 was the same (5.7). Optional: `PHRASE_SHAPE["end"]` -12 -> -8 brings the wind q75 to about 6 dB (inferred).
- **Doubled attacks at the long-chord joins: none audible.**
  - At 400 pitch-change long joins, the front over max(old note, new body) is +0.6 dB on the stem (c59 -1.4); 26 joins exceed +3 dB.
  - In the master band, those 26 are +0.7 dB median (c59 +0.2). The largest (Horn 3 bar 41 +10.6, bass trombone bar 116 +3.8) were the same in c59 (+9.8 / +4.8).
  - Stem dips of 6 dB or more at these joins fell from 135 to 9.
- **Join and re-bow holes** (`holes.py`, master band over control):
  - Audible: celli 620 (+6.3, finding 2), celli 286 (+6.0, finding 3), celli printed bow change qn 40 (bar 11, +4.8).
  - Under 3 dB over control: Violins II qn 91 (+3.6; marcato quarter notes with their separation, which is correct), basses 310 (+2.6), Flute 2 560 (+1.7), Bass clarinet 700 (+1.7).
  - The other re-bow holes are not in the master.
  - The staccato-alias "holes" (Flute 1 / Clarinet 1 / Oboe 1 stac at bar 30, Bassoon 1 stac 351/356) are staccato separations: drop them from the count.
  - Celli qn 40: the new bow on Sus MAX is 15 dB under for 0.3 s. A same-pitch overlap cannot be played on one channel, and channel 2 is silent in Opus (c58). Only a second instance (an alias) can overlap the bows. List it as left audible unless pass 2 has room.
- **Fugato bar 87: not a fault.**
  - The bar-level gap is staccato quarters against bar 86's held accented note. The note peaks in bar 87 (-37.1 / -38.5 / -37.5 / -33.7) match the staccatos of bars 85-86 (-31.7 to -35.7).
  - The real drop is into bar 88: the mp C4 at qn 348 is at -53.1 (-15 dB under the last staccato). There the two +3 celli roles end at 348 / 348.5 (envelope -7.2 dB over 0.75 qn) and CC11 steps 78 -> 64 at the same time, so the mp step is taken twice. Critic B's inner-line pass should place this: end the roles in the rest at qn 360 and let CC11 take the step.
  - The last staccato (velocity 52) is 3.8-4.8 dB louder than the two before it (velocity 62). That is round-robin spread on Stac RRx9; do not refit velocities on one take.
- **Horn slurs onto G#4 / A-flat 4: no A4 -> G#4 slur in this movement.** Legato slurs onto MIDI 68:
  - Horn 1 qn 196 from F4: no dip.
  - Horn 2 qn 226 from F4 (Leg Slur MAX, CC11 64): 7.1 dB stem dip at +0.1 s, and the note stays 3-4 dB under the F4. Master band 0.2 against 2.7 control: not heard.
  - Horn 2 qn 247 from G4: no dip.
  - The 4.5-7.9 dB dips at Horn 1 122 / 460 / 545 / 562 are tongued same-pitch repeats, correct.
  - Note: the cor anglais's G4 -> G#4 (finding 1) is the woodwind counterpart of the scherzo's horn sample.
- **Wind legato velocity under 96:** see finding 1. No floor.

Do not touch: the WIND_DETACH "long" form (its same-pitch 0.025 s gap and the 0.03/0.04 s pitch-change overlaps: dips 135 -> 9, master re-tongue 1.9 dB); the c60 re-bow re-list (`REBOW_AT`, pieces up to 5.3 s); the timpani beat/off-beat velocity pattern; the fugato B velocities and the flat CC11 lane at 72; the accent values (isolated median +1.8); brass legato velocities 110-127.
