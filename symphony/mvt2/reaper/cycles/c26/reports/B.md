# Critic B, cycle 26: balance and levels (render c25)

Method. I used the c25 stems and master, K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames. I mapped them to score qn with the parts.json tempo map and compared them with the printed marks (`build/mockup-events.tsv`, score pages 2-8) and with the control data in parts.json (notes, cc11, vol_db). Fixes were simulated by applying their dB to the stem frames. Scripts are in `/private/tmp/claude-501/mockup-loop/c26-B/`: the c25-B set (`clim.py`, `over.py`, `viol.py`, `melacc.py`, `famacc2.py`, `melA.py`) plus `win.py` (chosen stems per window), `cc.py` (a track's notes and controllers), `tbn.py` (attack spectra) and `spec2.py` (band shares).

## Delivery, c25 (ffmpeg ebur128 agrees with metrics.md)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.6 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU (target 14-16) |
| True peak | -4.2 dBFS | -1.6 dBTP |
| p10-to-max span | | 18.5 dB |
| Limiter | | 1.6 dB |

Every finding below touches soft passages, or a single loud solo line that is not the climax peak. None of them moves the LRA, span or limiter by more than 0.2 (inferred).

## What holds (measured)

**The c25 B fixes landed.**
- Bar 61 Vc is 1.9 dB under the melody at qn 205. It was 5-7 dB over.
- The a2 pickup at qn 261.75 is now under its f arrival.
- Bar 37: the flute is 3-4 dB over the bass clarinet.
- The ppp rolls sit 3-10 dB under the pp basses. A timpani stem is the loudest only in the printed pp solo figure of bar 84.

**The dynamic map still agrees across families.** Median K of notes by printed dynamic:

| | winds | brass | strings |
|---|---|---|---|
| pp | -47.1 | -47.5 | -47.1 |
| p | -39.3 (mostly solos) | -38.0 (Horn 1 solos) | -42.7 |
| f | -32.4 | -29.8 | -32.4 |

The climax proportions of bars 61-62 are unchanged from c24, and they match Rimsky-Korsakov (`reference-books/text/rimsky-principles.txt`, lines 1965-1990).

## 1. Bar 89: the clarinet's resolution note swells for 3 seconds and ends up louder than the phrase that leads to it, 4-6 dB over the violins' pp entry (measured)

**Where.** Clarinet 1, the C5 at qn 292-297 (bars 89-90). It is printed pp, under the rit. The tie runs into the bar 90 decrescendo. Vln I enters on top of the chord at the same pp (p. 8).

**What, in mean K:**

| | bar 87 (286-289) | bar 88 (289-292) | 292-293.5 | 293.5-295 | 295-296 |
|---|---|---|---|---|---|
| Cl1 | -39.4 | -41.9 | -40.0 | -40.6 | -42.6 |
| Vln I | | | -45.3 | -44.5 | -45.1 |

- The resolution is 1.3-1.9 dB louder than bar 88.
- It is 4-5 dB over Vln I in K, and 7-10 dB over it in A. Cl1 is the loudest stem of bars 89-90.

**Cause, in parts.json.** The c25 trim `"292": 3` with `NOTE_TRIM_RAMP_S` 3.0 s makes vol_db rise from +5.0 at qn 292 to +8.0 at qn 294.34. That is a 3 dB crescendo on a tied pp resolution, in a place where the score prints only a rit. and then a decrescendo. The note is also re-attacked at v60, against v41 for the notes before it. The roles held to 297 (A #1) already give the note the solo lift.

**Fix.**
- `build/note_trims.json`, "Clarinet 1": remove `"292": 3`.
- `tools/score_to_parts.py` `NOTE_TRIM_RAMP_S`: remove `"Clarinet 1"` 292.0.
- Keep the role rows.

**Predicted:**

| | 292-293.5 | 293.5-295 | 295-296 |
|---|---|---|---|
| Cl1 K | about -40.9 | -43.2 | -45.6 |

- The resolution then falls through the bar.
- It is 1-2 dB under its bar 87-88 notes, and 1-4 dB over Vln I. This is the plain-RMS target the actor named in c25 CHANGES ("292 trim +3 -> +1").

## 2. Bar 81: the inner parts do not diminuendo with the tune. Horns 3-4 hold and the oboe's lower octave is lifted, so the ff > p figure of the flute and Vln I ends level with or under its accompaniment (measured)

**Where.** qn 268-271 (bar 81).
- Fl1 and Vln I play the "1." falling figure, ff with a decrescendo to the p of bar 82.
- Ob1 doubles it an octave lower.
- Horns 3-4 hold a chord with a decrescendo, and nothing is printed after it.
- Vc, Bn and the a2 horns play the moving line, with the same hairpin to p (p. 7).

**What, in K per 0.5 qn:**

| qn | 268.5 | 269.0 | 269.5 | 270.0 | 270.5 |
|---|---|---|---|---|---|
| Flute 1 | -27.8 | -33.3* | -36.8* | -34.7 | -36.9 |
| Violins I | -29.7 | -33.3 | -32.5 | -34.0 | -35.0 |
| Oboe 1 | -30.2 | **-29.3** | -36.0 | -35.9 | **-34.2** |
| Horn 4 | -33.5 | -34.4 | -34.5 | -35.2 | -35.2 |
| Horn 3 | -38.0 | -35.0 | -36.6 | -36.8 | -35.5 |
| Violoncellos | | -31.8 | -34.0 | -34.9 | -39.4 |

\* From the 0.25 qn frames.

- From qn 268.5 to 270.5, Fl1 falls 9 dB and Vln I 5 dB. Horns 3-4 fall 0-1 dB.
- Ob1 is the loudest stem at qn 269 and at 270.5.
- At qn 270-270.75 Horns 3+4 sum to about -32.3, which is 2.5 dB over Vln I.

**Cause.**
- **Horns 3-4.** Their decrescendo has no printed target, so `hairpins_and_marks` applies `HP_STEP` (14 CC). Their CC11 runs 87 -> 74. Fl1 and Bn1 run 114 -> 46, and Vc and the a2 horns 88 -> 45.
- **Oboe 1.** The c12 role `[268, 271, 4]` lifts it 4 dB for the whole bar. It was set when bar 81 measured differently.

**Fix.**
1. `tools/score_to_parts.py`: add `HP_TARGET_AT = {"Hn3": {268.0: "p"}, "Hn4": {268.0: "p"}}`. In `hairpins_and_marks`, in the `if tgt is None:` branch, use `tgt = DYN[HP_TARGET_AT[staff][q]]` when a staff of `staff_list` lists the hairpin start. The chord then fades into the soft layer with the rest of the tutti, rather than only losing level. If the actor prefers no code change, replace Horn 3's `[268, 271, -1]` with `[268.5, 271, -5]` and add the same row on Horn 4. That is level only, inferred to be about as effective.
2. `build/roles.json` Oboe 1: `[268, 271, 4]` -> `[268, 271, 0]`, or delete the row. The `[271, 274, -4]` row after it is unchanged.

**Predicted:**
- Ob1: -33.3 / -40.0 / -39.9 / -38.2 at qn 269 / 269.5 / 270 / 270.5, which is 0-5 dB under Vln I.
- Horns 3-4 at qn 270.5: about -40 each (24 CC lower, about 0.2 dB/CC, as the a2 horns measure over the same bar). Their sum is then about 3 dB under Vln I.
- The tune then leads its own decrescendo.

## 3. Bars 63-64: Trombone 1's accented notes (qn 212.5, 213 and 218) play the top CC11 layer, which is 10-27 dB brighter above 3.5 kHz than the marcato notes around them. This is Dan's "too harsh" (measured; the layer cause inferred from CC11)

**Where.** Trombone 1, ff marcato solo, qn 212.5-219.5 (p. 5). The strings are sf > p under it.

**Band shares of the Tbn1 stem (dB of its total):**

| | 3.5-5 kHz | 5-8 kHz |
|---|---|---|
| qn 212.5-214, the Sus Accent notes | -28.1 | -36.3 |
| qn 214.5-217.9, the Marc Lng eighths | -38.3 | -53.1 |
| qn 218-219.4, Sus Accent | **-23.2** | **-26.6** |
| Bass trombone, mf, bars 61-62 | -33.3 | -46.8 |
| Horns a2, f, bars 79-80 | -32.2 | -46.2 |

- In the first 60 ms of the qn 218 attack, Tbn1's 2-5 kHz energy is 5.5 dB over the whole string section (`tbn.py`). At the eighths it is 8-19 dB under.
- In CC11, all three accents sit at 122: ff 114 plus `ACCENT_BUMP` 8 (`score_to_parts.py` line 101/1552). That is the fff layer. The Marc Lng notes take their dynamic from velocity (v94-106).
- `ACCENT_DB_AT` 4.0/3.0/4.5 and velocities 108/105/110 come on top of that.

**Level.** Tbn1 is -18..-24 K, 8-13 dB over Vln I in bar 64. That is right for a ff solo over strings that have fallen to p, and Rimsky's ff trombone equals two string sections. So the problem is the colour of the attacks, not the stem level.

**Fix** (`tools/score_to_parts.py`):
- A per-track accent bump: `ACCENT_BUMP_AT = {"Trombone 1": 0}`. The accents then stay at CC11 114, the ff layer.
- `ACCENT_DB_AT` "Trombone 1": `{212.5: 3.0, 213.0: 2.5, 218.0: 3.0}`, so the weight comes from level with no bright front edge (Dan's 2-4 dB rule).
- `VEL_SET` Tbn1 212.5/213/218: 108/105/110 -> 100/98/100.

Check after the render:
- 3.5-8 kHz share of the 212.5 and 218 notes within 6 dB of the Marc Lng notes.
- Tbn1 bar 63 mean K still 3 dB or more over Vln I.
- If the stem level drops more than 2 dB, raise `dyn_trim_db` ff +4 -> +5.

If critic A proposes Sus MAX with an envelope swell for qn 218 instead (BRIEF item 9), that also removes the fff layer. Use one or the other.

## 4. Bar 30: the pp horn chord stands over the strings' p > pp cadence of theme A (measured)

**Where.** Horns 3-4, the pp chords at qn 84 and 87 (bars 29-30). Violins I/II, Violas div and Vc end theme A with p > pp in bar 30 (p. 2).

**What, in K:**

| qn | 87.5 | 88.0 | 88.5 | 89.0 | 89.5 |
|---|---|---|---|---|---|
| Horn 3 | -48.1 | -46.0 | -50.1 | -51.4 | -47.6 |
| Horn 4 | -46.3 | -47.5 | -48.5 | -50.4 | -51.0 |
| Violins I | -48.3 | -47.8 | -51.4 | -52.3 | -50.4 |
| Violins II | -47.7 | -46.1 | -49.0 | -49.9 | -50.2 |

- Each horn is level with or over each violin section. The pair sums to about -44.5 at qn 88, which is 2-4 dB over either section.
- Horn 3 or Horn 4 is the loudest stem in 4 of the 6 half-beats from qn 87 to 90 (`clim.py`).
- The c19 rows `[86, 90, -3]` on both horns are not enough since the violins' c24/c25 coda work. The theme's cadence should stay on top. The horns are a held pp harmony, two players against full sections.

**Fix.** `build/roles.json`, Horn 3 and Horn 4: `[86, 90, -3]` -> `[86, 90, -5.5]`.

**Predicted.**
- The horns at qn 87.5-89.5 come to -49..-56 each, and their sum to about -47, which is 1-2 dB under the violin sections.
- The pp chord stays audible, level with the pp contrabassoon entry (-47..-49).

## Smaller items (measured, for the actor's judgement)

- **Bar 82, qn 271.** The a2 horns (p) are the loudest stem by 1.5 dB over Vln I for one beat: -37.0 vs -38.5. Fix 2 may reduce this through the shared texture. No change proposed.
- **Bars 57-60.** Violins II sit 3-7 dB under Violins I through the crescendo. Vln II is the lower third with Ob1. The pair (Vln II + Ob1) is 3-4 dB under the upper pair (Vln I + Fl1), which is a normal top-voice lead. No change.
- **Bars 41-44.** The flute counterline is level with the cor anglais solo (median A -1.5 dB). The score has a p < mp > p duet in which the flute enters on top. No change.

## Do not touch

- The cross-family dynamic map (CC11, `soft_trim_db`, family trims).
- The bar 61-63 brass proportions.
- The c25 B fixes: Vc note trims 204 -3 / 265 -4, the timpani ppp rows `[3,8.5,4]` / `[226,237.5,3]` / `[292,304,4]`, the a2 horns 261 trim, BCl 108 -3.
- The Clarinet 1 coda role rows held to 297.
- The Timpani `[277, 280, 10]` row.
- `deliver_master.py`.
