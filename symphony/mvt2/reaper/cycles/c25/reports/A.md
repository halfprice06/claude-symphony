# Cycle 25, critic A: articulation and phrasing (on the cycle 24 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c25-A/`: the c24-A set plus these new ones.
- `dropscan.py`: long notes whose first 0.35 s stands far over their own body and is followed by a trough.
- `trimshape.py`: the shape of every negative note trim.
- `trimsim.py TRACK QN RAMP_S [DB]`: compares a note trim's current 0.6 s ramp with no trim and with another ramp or depth.
- `simenv.py TRACK '[[qn,dB],...]' Q0 Q1`: applies a dB delta envelope to a stem and adds the difference to the master.
- `simnotch.py`: the same for `JOIN_NOTCH`-shaped rows.
- `envstep2.py`: steep `vol_db` changes inside held notes.
- `noteoff.py`, `entryatt.py`, `pizzrr.py`.
- `who2.py` now reads `CYC`.

Run them with `CYC=24 ~/.venvs/claude-composes-reaper/bin/python`. Every simulation is an amplitude-domain change on the c24 stems, with the master rebuilt as master + (new stem - old stem).

Delivery numbers, from c24 `metrics.md` and CHANGES.md (not re-measured):
- Master: -22.5 LUFS, LRA 23.7 LU, TP -3.9 dBFS.
- mp3: -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, span 18.4 dB, limiter 1.9 dB.

The fixes below are local (at most 5 s each, at p/pp) and change the simulated master by at most 1 dB where they act. I infer no measurable change to these figures.

## Checked and working (measured, c24)

- **Keyswitches.** All are at least 20 ms ahead of their note, except the known Ob1 207.952 (13 ms).
- **Chords and ties.** No chord goes to a legato patch. All 104 ties are held; the only re-attacks are the timpani tie strokes at 203/211.
- **Note-offs.** Notes before a rest end on the printed value (median 0.00 s early). The only exception is Fl1 122, which ends 0.39 s early before its breath.
- **Mutes.** CC15 matches the score: strings con sord. from bar 15 (Vln I tutti from 65), off before the bar 37 "senza sord.". Hn3/4 are muted from 271.5 for bar 87.
- **Legato crossover medians.** -0.01..+0.06 s on every legato track; p90 at most 0.15 s.
- **Breaths, tremolo, pizz.**
  - Breaths and caesuras make 9-21 dB gaps.
  - Tremolo 8-30 Hz shares are 0.48-0.69, except Violas bar 62 at 0.24, which is unchanged since c22.
  - Pizz. samples rotate. Only Vc/Cb 110 and 118 reuse one sample, 8 qn apart, which is inaudible.
- **c24 changes.** `UNLOAD_UNUSED_ROWS` and the CC36/CC69 pre-roll did not change the pizz. or articulation data: the pizz. correlations are identical to c23. The c24 notches and Horn 1 leads measured as the actor reported.
- **Join spikes.** The largest master bump at a legato join is now +4.4 dB (`mbumps.py`). The spike scan finds 33 of 606 joins at 5 dB or more on their stem.

## 1. Coda, bar 89: the clarinet's last note (the C5 that resolves the final statement of the tune) drops under every other voice, including Clarinet 2. Measured; the fix is simulated

**Where.** Clarinet 1, qn 292-295. The note is the tied C5 at the end of the slur that starts at 286. The score marks pp from 286 and no decrescendo until bar 90 (qn 295).

**What is wrong.** All three Clarinet 1 lifts in `roles.json` end exactly at 292, inside this slur:
- [280,292,3] (c10)
- [286,292,2.5]
- [283,292,1.5,1] (c24 C #4)

`vol_db` falls from +3.5 at 292.0 to -2.0 at 292.5, a 5.5 dB step on the resolution note at its downbeat. The sample also decays about 2.5 dB over the bar at flat CC11.

Stem levels (RMS):

| qn | 289-292 | 292-293.5 | 293.5-295 | 295-296 |
|---|---|---|---|---|
| Clarinet 1 | -45.8 | -50.1 | **-54.5** | -55.6 |
| Clarinet 2 | -52.1 | -50.0 | -48.5 | -50.0 |
| Violins I (pp entry at 292) | | -48.1 | -47.5 | -48.0 |
| Master | -42.0 | -40.6 | -40.3 | -41.1 |

The solo was 3.8 dB under the master in bar 88. In bar 89 it is 14 dB under the master, 6 dB under Clarinet 2's inner E flat 4 and 7 dB under the Vln I pp entry. The listener loses the last note of the tune just before the morendo (inferred). The c24 C #4 check measured only up to 291, so it did not catch this.

**Fix** (`build/roles.json`, "Clarinet 1"):
- [280,292,3] -> [280,297,3,2]
- [286,292,2.5] -> [286,297,2.5,2]
- [283,292,1.5,1] -> [283,297,1.5,2]

The lift is then held through bar 89 and released across the printed bar 90 decrescendo.

Add `note_trims.json` "Clarinet 1" "292": +3 with `NOTE_TRIM_RAMP_S` {"Clarinet 1": {292.0: 3.0}}. This holds the pp against the sample's decay.

Optional (inferred): "Clarinet 2" [286,292,-2] -> [286,295,-2], so Cl2's new E flat 4 at 292 does not rise 2 dB under the clarinet's last note.

**Simulated** (roles plus trim):
- Cl1 292.5-295: -46.0..-47.2, flat. That is about 1.5 dB over Vln I and 2 dB over Cl2.
- Bar 90 then falls -46.8 -> -61.6, the printed decrescendo.
- Master +0.6..+1.0 dB in bar 89.

**Check:** Cl1 minus Vln I and Cl1 minus Cl2 at 292.5-295 are both at least 0; the Cl1 stem falls less than 2 dB from 292.5 to 295.

## 2. Bar 32, bass clarinet solo ("solo, espr."): the arrival E flat 4 is a 0.35 s accent and then falls 13 dB, at the start of a printed crescendo. Measured; the fix is simulated

**Where.** Bass clarinet, qn 93.0-94.0. It is the arrival of the mp rising line from bar 31 (F-A flat-C-E flat). The score marks a crescendo from 93 to the mf at 96. The cor anglais enters p dolce at 93.

**What is wrong.** Stem at 40 ms resolution:
- Approach C4 at 92.6-92.9: -36.2.
- Arrival plateau at 93.05-93.33: -32..-34 (the transition burst into the upper register).
- Crash to -45.0 at 93.43, then -41.5..-42.7 until 93.8.
- Rising slowly from there: -39.6 at 93.6-94.5, -35.7 at 95-96.

The master follows: -31.4 at 93.1, then -39..-41.5 at 93.4-93.8. It is the top entry of `mbumps.py` (+4.4) and of `dropscan.py` (master attack-to-trough 9.7 dB). This shape has been the same in every render since c15, while it was smooth in c10 (peak -37.0, minimum -40.1).

Inferred effect: an unwritten accent and then a subito piano, where the score asks the line to grow.

The envelope drives it (`parts.json` vol_db): +7.6 at 92.5, +3.4 at 93.0, -1.3 at 93.25, -6.0 at 93.5. That is 9.6 dB of envelope fall in 0.5 qn, from the B role [93.5,99,-6,2.5] (c19) ramping in over 93.0-93.5 on top of the note trim 93 -4 (0.6 s ramp).

**Fix** (`tools/score_to_parts.py` `JOIN_NOTCH`, new key "Bass clarinet"): [(93.03, 93.33, -4.5), (93.39, 93.85, 4.0), (93.89, 94.15, 1.5)]. This cuts the burst, fills the trough, and steps back to the current envelope. The role and the trim stay, so B's balance against the cor anglais after 94 is unchanged.

**Simulated:**
- Stem 93.06-94.25 now lies in -34.8..-39.3. Before, it spanned -32.1..-45.0.
- Master 93.1: -31.5 -> -35.3. Master 93.4-93.8: -38.6..-41.5 -> -36.2..-38.0.
- BCl stays 9 dB or more over the cor anglais on the arrival and +3..+5 in 93.4-93.8 (was +1.4).

**Check:**
- `dropscan.py`: BCl 93 master attack-to-trough under 5 dB.
- `mbumps.py`: BCl 93 under 2.5 dB.

## 3. Old negative note trims (c03-c09) ramp to full depth 0.6 s after the onset. They now turn printed hairpins into an early drop or a mid-note hole. Measured; the fixes are simulated

These trims were set against sample swells measured in c03-c09. `trimsim.py` shows that with the present CC shaping the swells are mostly gone. The 0.6 s ramp now lets the attack through at full level and then pulls the body down.

Stem RMS by window after the onset, in seconds (`trimshape.py`, `trimsim.py`):

| note | printed | current 0-0.3 / 0.3-0.6 / 0.6-0.9 / 0.9-1.3 / 1.3-1.8 | no trim | proposed | proposed shape |
|---|---|---|---|---|---|
| Oboe 1 45 (bar 16, the crest of the solo's p < >), trim -7 | > over 45-47 | -37.8 / -40.0 / -42.8 / -42.1 / -42.9 | -35.9 / -34.7 / -35.8 / -35.1 / -35.9 | -7, ramp 2.1 s | -36.5 / -36.2 / -38.2 / -38.6 / -40.9 (-43.0 at 1.8-2.4) |
| Oboe 1 190 (bar 57.5, p cresc), trim -8 | < | -42.2 / -42.6 / -46.7 / -45.3 / -43.0 | -39.8 / -36.7 / -38.7 / -37.3 / -35.0 | -4, ramp 0.1 s (a step) | -43.3 / -40.7 / -42.7 / -41.3 / -39.0 |
| Clarinet 1 256 (bar 77, the bars 75-78 crescendo), trim -5 | < | -38.9 / -42.9 / -42.8 / -39.7 | -37.5 / -39.2 / -37.8 / -34.7 | -2, ramp 0.1 s | -39.4 / -41.2 / -39.8 / -36.7 |
| Violoncellos 180 (bar 55, mp cresc), trim -7 | < | -38.4 / -39.5 / -43.4 / -43.4 / -42.7 | -36.7 / -34.2 / -36.4 / -36.4 / -35.7 | -2, ramp 1.8 s | -36.8 / -34.7 / -37.2 / -37.6 / -37.4 |

What each change does:
- **Oboe 1 45.** The only exposed one (the oboe is the loudest stem there, stem minus master -0.3 dB). The printed 2-qn decrescendo is now 75% done in the first 0.5 s and then flat. A real player would let it fall across the bar (inferred). The proposed ramp keeps the -7 depth, so the bar 17 level does not change.
- **Oboe 1 190 and Clarinet 1 256.** Each has a 4-5 dB hole in the middle of a printed crescendo. The changes raise their bodies by 2-4 dB. Both are inner winds 10-14 dB under the master, so the effect on balance is small.
- **Violoncellos 180.** The cello falls 7 dB inside a printed crescendo. With -2 it holds about 1-3 dB over the violins' theme at bar 55 (Vln I -40.6 at 180.5-181.8). If B judges that too high, lower the whole phrase from 178 with a role instead of restoring the old trim.

**Fix:**
- `build/note_trims.json`:
  - "Oboe 1" "190": -8 -> -4.
  - "Clarinet 1" "256": -5 -> -2.
  - "Violoncellos" "180": -7 -> -2.
- `NOTE_TRIM_RAMP_S` in `tools/score_to_parts.py`:
  - "Oboe 1": add 45.0: 2.1 and 190.0: 0.1.
  - "Clarinet 1": {256.0: 0.1} (merged with the 292 entry from finding 1).
  - "Violoncellos": {180.0: 1.8}.
- Note them in the `_doc`.

**Check:** `trimshape.py` on c25: each listed note's "att -> 0.5-0.9" no more negative than -2 dB on the crescendo notes. Oboe 1 45 falls at least 4 dB from 0.5-0.9 s to 1.8-2.4 s.

**For the loop** (inferred): `trimshape.py` lists 30 more negative trims. Before adding any new note trim, compare the note with no trim (`trimsim.py`). Prefer a step (ramp 0.1 s) on crescendo notes, and a ramp as long as the hairpin on decrescendo notes.

## Not findings, checked

- **Violins at bars 53-56** (Leg Port 172, Leg Slur 176-182). `rise.py` puts the new pitch at body -6 dB +0.18..+0.53 s late. But the crossover (`leg.py`) is +0.13..+0.23 s, and the `rise.py` p90 over the whole movement is +0.47 s. Too noisy to justify more leads. The portamento at 172 ("sul A") may arrive late by nature.
- **Horn 1 bar 54.5** (Bb4, 178-180). There is a 6-9 dB dip mid-note at 179.2 under the printed crescendo. The c24 B #1 role [179.25,180.75,-6.5] explains only about 1 dB of it (simulated); the rest is in the sample. Not worth a reshaped role.
- **Double bass pizz. bars 39-40** (116 E flat 2, 120 A1). They are 3-6 dB over their neighbours, and 120 makes the master's +7.8 dB peak in this pp/p passage. This is the pizz. pitch-trim domain (c12), and real low pizz. varies too. Low priority: a pitch trim A1 (33) -3 on Pizz only, if B agrees.
- **Flute 1 bars 76-77** (Bb6 254 +9.1, Ab6 255 +7.6 on the stem). These reach the master as only +1.3..+1.5 dB under the violins; leave them.
- **Patches.** Nothing better exists on the drive for this lens.
  - The horn mutes folders hold only stopped-horn rows.
  - There is no solo violin library.
  - The strings con sordino comes from the Opus CC15 script, which the project already uses.
  - Timpani use the felt (soft-stick) patches, as printed.
- **The viola sextuplets bars 58.5-61** play on Sus MAX (44 slurred notes not on a legato row). This item is closed after three failed tests (c14, c15, c16); I do not reopen it.

**Do not touch:**
- The c22 pull pad.
- The c23 entry leads, entry fills and unison fills.
- The c24 `JOIN_NOTCH` entries and Horn 1 leads.
- `UNLOAD_UNUSED_ROWS` and the CC36/CC69 pre-roll, until `det3.py` has compared c24 and c25.
- The Tbn1 accents and marcato.
- The tie handling, keyswitch placement, CC15 mute timing, pizz. and harp steps, harp roll timing (ARP_S, bottom note on the beat), timpani tie strokes and caesura breaths.
- B's BCl [93.5,99,-6,2.5] and CA [93,98.5,2] balance after qn 94.
