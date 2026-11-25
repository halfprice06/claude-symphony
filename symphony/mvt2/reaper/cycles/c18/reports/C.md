# Cycle 18, critic C: dynamics over time (on the cycle 17 render)

Lens: the shape of every hairpin and phrase, the loudness arc against the score (climax bars 59-63, return at 65, coda), loudness range, swells and decays on long notes, comparison with real orchestras.

Material: `cycles/c17/render` (master and 29 stems; the stems sum to the master), `cycles/c17/mvt2-mockup-c17.mp3`, `cycles/c17/metrics`, `build/parts.json` (21:47, the data of the c17 render), `build/{roles,note_trims,early_fills,pitch_trims,loop_fills,loop_profiles}.json`, `tools/score_to_parts.py`, `build/mockup-events.tsv`, score pages 1, 4, 5, 7, 8. References: Dvorak 9/i (Columbia MP3) and the stored Brahms 1/ii and 4/ii loudness series.

Scripts and outputs: `/private/tmp/claude-501/mockup-loop/c18-C/`. They are the c14-C set re-pointed at c17, plus `beatL.py` (LUFS per beat), `grp.py` (family sums), `holes2.py`/`holes3.py` (dips inside sustained notes, c16 against c17), `pk.py`/`pkstem.py` (where the master peak comes from), `lra.py` (which bars set the LRA), `simlib.py` and `simA*.py`, `simB.py`, `simC2.py`, `simH.py`, `simAll.py`, `simD.py` (simulations). A simulation adds (gain - 1) x stem to the master for the stems it changes, then runs the unchanged `tools/deliver_master.py` into my scratch folder. With no changes it reproduces the c17 delivery exactly.

## Delivery, c17 (measured)

- Master: -22.5 LUFS, LRA 24.3 LU, sample peak -2.26 dBFS.
- mp3: -19.9 LUFS, LRA 16.3 LU, TP -1.6 dBTP, span from p10 to S max 18.9 dB, limiter 3.4 dB.
- Two targets are missed: LRA (0.3 over 16) and the limiter (0.4 over 3).

## What holds (measured; keep it)

- The large arc. LUFS per bar:
  - Bars 53-61 rise every bar except the printed drop into bar 57: -32.7, -30.0, -27.7, -25.8, -26.4, -22.7, -20.9, -16.0, -13.3.
  - Bar 61 is the loudest bar, 1.5 dB over bar 79 (-14.8). In the mp3 the gap is 1.3 dB (-9.6 / -10.9).
- Bars 57-58: the p to f crescendo rises 7.8 dB per beat (qn 188-196). The bar 60 crescendo rises 4.0 dB (qn 200-203).
- The return: bar 64 -25.7 LUFS, bar 65 -40.6. The trombone's > in bar 64 falls 10 dB (218-219.5).
- The second climax: it holds -14.7..-15.4 per beat over qn 262-266. Bar 81's diminuendo falls 7.2 dB (268-271), and bar 82's p > pp another 6.5 dB.
- The coda: ppp bars 83-84 are 3.8-4.6 dB under the pp bars 86-90 in the mp3. The morendo (298-301) falls 4 dB per beat, and the final ppp chord is under the opening ppp chord.
- Lead-line hairpins: median +4.9 dB on 21 crescendos and -3.8 dB on 18 decrescendos (c13: +1.7). All hairpins shared by 3 or more tracks move the master the printed way, except 295-297 (+0.3). That one is a clarinet/horn > over held strings, so the flat master is correct.

## 1. Theme A's swell still runs backwards in both statements, and the soft decrescendos that follow an mf crescendo get no shaping (measured; fix simulated)

**Where:** Violins I and II, bars 23-24 (qn 68-72) and the reprise, bars 72-73 (qn 240-244). Oboe 1, bar 41-42 (qn 148-151).

**Evidence (measured):**
- Violins I+II summed, RMS per beat, qn 66-73: -38.6, -38.8, -37.9, -39.6, -38.3, -37.9, -37.5, -37.0.
  - The printed < (68-70) falls, and the > (70-72) rises. The loudest moment of the first phrase of the theme is the end of the diminuendo.
  - Stem fits (hp3.py): Vln I 68-70 -3.7 dB and 70-72 +1.2; Vln II -2.6 and +4.3.
  - This has been open since c13 (c14 C #1, c14 HISTORY "Vln I 68-70 crescendo still falls").
- The reprise: Vln II 240-242 -1.7 dB, 242-244 +4.5 dB. Vln I moves +3.1 / -1.6.
- At qn 72 (C5, the end of the >), both sections dip about 5 dB together at +0.9-1.2 s after the onset. The master drops 3 dB there.
- Oboe 1, 148-151 (printed >): per 0.5 qn -40.2, -39.6, -40.2, -40.7, -41.5. That is 1.3 dB over 2.5 qn. The volume envelope rises from +4.5 to +9.5 dB during it: `note_trims` 148 +5 plus the role 2.5, held to 151.1.

**Causes (read from `score_to_parts.py`, the hp_soft block near line 1972, and the build data):**
- `SWELL_NO_SOFT_GAIN` (Violins I/II 68 and 240) skips the crescendo's +3 dB. That rule is c15 B #1, which keeps the swell under the mf arrival at qn 82.
- The paired decrescendo is skipped too, by `not any(k_ == "cresc" and -0.3 <= a - b_ <= 0.3 ...)`. So neither half of the < > gets any volume shaping.
- CC11 moves 61 to 66 (Vln I). At this level that is about 1 dB (0.19 dB per CC, c14 `pres.py`).
- The per-note trims then decide the shape:
  - Vln I: `early_fills` 71 +5 (hold 0.4 s), `note_trims` 68 +4 and 72 -3, `pitch_trims` 72 -2.
  - Vln II: `note_trims` 68 +6, 70 +3.
- The same skip removes Oboe 1's 148 decrescendo, because it follows a crescendo (146-148) that has its own mf hpgain.

**Fix:**
- `tools/score_to_parts.py`, hp_soft block:
  - (a) For a crescendo in `SWELL_NO_SOFT_GAIN`, do not `continue`. Give it a messa di voce with `SWELL_SOFT_GAIN_DB = 2.5`, released across the paired decrescendo to -1.0 dB at its end, back to 0 over 1 qn.
  - (b) Skip a decrescendo only when its start is in `used_dec`. Delete the `not any(k_ == "cresc" ...)` condition, so a decrescendo after an hpgain (mf) crescendo gets the -`HP_SOFT_DEC_DB` ramp.
  - (c) Add `HP_SOFT_DEC_AT = {"Oboe 1": {148.0: 4.0}}` (per-onset depth), because Oboe 1's +5 note trim needs a deeper ramp than 2 dB.
- `build/early_fills.json`: Violins I "71" db 5 -> 2.

**Simulated (`simB.py`; the stems are scaled by exactly this shape):**
- Violins I+II per beat, qn 66-72: -38.6, -38.8, -37.5, -37.6, -36.8, -39.0, -38.5. The swell now goes up 2.0 dB to qn 70 and down 2.2 dB to 71.
- The top at 70 stays 2.2 dB under the printed mf arrival at 82 (-34.6), so c15's constraint still holds.
- Oboe 1's 148.5-150.5 decrescendo: -40.6 to -45.1 dB.
- Delivery unchanged (LRA 16.3, limiter 3.4).

## 2. Horn 1's solo crest (bar 12, Bb4 at qn 34) collapses 10-11 dB half a second after it arrives (measured; fix simulated, needs tuning on the render)

**Evidence (measured):** Horn 1 stem, 100 ms windows from the score onset s:
- c17:
  - Rises to a plateau of -33.8..-34.1 at s+0.15..+0.4 s.
  - Then -40.8 at s+0.5, and -44.9 / -44.5 / -44.4 at s+0.55..+0.65.
  - Then -40..-42 to the end of the note.
- c16, same data: -34.3 down to -43.0 at s+0.45, recovering to -36.3.
- So this is a systematic hole in the legato-to-sustain crossfade of this transition, and it is deeper and longer in c17.
- Master per 0.125 qn: -33.6 at 34.12, then -41.5 at 34.5.
- This note is the top of the solo's climb (printed p < mp). The crest that c14 C #2a rebuilt is audible for 0.4 s, and then it drops out.

**Fix:**
- `build/loop_fills.json` (still read by `score_to_parts.py`, LOOP_FILLS):
  - Add `"Horn 1": {"34": [[0.90, 8, 0.2], [1.25, 4, 0.3]]}`.
  - t is in seconds from the moved start 33.78, which is s - 0.25 s.
- Simulated (`simH.py`, cosine lifts of this size): the trough rises from -44.9 to about -36.5, and the rest of the note from -41 to about -37.
- The c16/c17 difference shows the hole moves by about 0.1 s between renders. So check the next render at 10 ms resolution and retune t.
- Add a dip probe for Horn 1 qn 34 to `tools/probe_attacks.py` (window 0.9 s, limit 6 dB), so a render with the hole is caught.

## 3. Climax: bar 62 sags 2.4 dB into a bar-63 sf that is no arrival, and one Vln I join spike sets the limiter (measured; fix simulated)

**Evidence (measured):**
- LUFS per beat, qn 204-213: -13.6, -14.1, -13.3, -12.6 (peak, bar 61 beat 4), -13.4, -14.6, -14.7, -15.0, -16.3 (sf, qn 212), -17.5.
- Bar 62 is printed ff molto sostenuto with tenuto half notes and no hairpin (page 5). It falls 2.4 dB.
- Causes of the bar 62 fall, per beat 207 to 211:
  - Tuba -26.3 to -38.9
  - Vln I -27.4 to -31.3
  - Violas -32.6 to -34.2
  - Bassoon 1 -32.0 to -36.8
- The `_all` [204,212,-1.4] cut (c17 B #1) is flat across both bars.
- The sf at 212:
  - The strings sum peaks at -21.3 per 0.125 qn, only 1.5-3 dB over their last ff beat.
  - The master at 212 is 2.3 dB under qn 211.
  - CC11 at the sf is 118, below the 122 of the notes before it.
- The master sample peak:
  - It is at qn 207.83 (-2.26 dBFS), 1.9 dB above any other peak (next: 203.38 -4.12, 206.39 -4.23).
  - It is Violins I's legato join into F6 at 208 (moved start 207.80): stem 0.266, the stem's own peak. 40 ms peaks reach -11.4 against -14..-15 around it.
  - This single spike is why the limiter does 3.4 dB (open since c16, "the Vln II 207.94 join peak"; it is Vln I).

**Fix:**
- (a) Violins I: a `vol_bp` notch of -4 dB from qn 207.80 to 207.97 (0.04 qn ramps). A per-onset early-fill entry with a negative db at "208" with pre_s 0.0 and hold_s 0.15 would do it, if negative fills are allowed. Otherwise add an onset-keyed `JOIN_NOTCH = {"Violins I": {208.0: (-4.0, 0.15)}}`.
- (b) `build/roles.json` `_all`: [204,212,-1.4] becomes [204,212,-1.4,3.5]. The end_ramp opens the cut across bar 62, so the bar holds level into the sf.
- (c) Add string roles [211.75,213.0,1.5,0.5] for Violins I, Violins II, Violas, Violoncellos and Double basses, so the sf lands 1.5 dB up and releases into the printed >.
- Do not hold back the divisi cut at 212; c14 showed that variant makes the limiter 5.8 dB.

**Simulated (`simA*.py`, `simAll.py`):**
- Bar 62 per beat: -13.3, -14.0, -13.7, -13.7 (was -13.4..-15.0). The sf is at -15.5 (was -16.3).
- Master peak -3.44 dBFS. Limiter 3.4 -> 2.1-2.4 dB.
- mp3 bar 61 -9.7, bar 62 -9.9, bar 79 -10.8. The climax is still the loudest bar.

## 4. Phrase tops: in the solo and theme phrases, the highest note is the loudest in only 9 of 25 slurs (measured; fix simulated; this is the c14 C #5 item, deferred since c14)

**Evidence (measured, `peaks.py`):**
- 25 lead-line slurs of 4 or more notes. The top note is a median of only +1.3 dB over the others (p25 -1.5), and it is the loudest note in 9.
- Worst cases:
  - Vln II 84-86.5: the top is -6.6 dB, and the loudest note is the last one.
  - Horn 1 226-235: top -5.7.
  - Flute 1 108-114: -3.6.
  - CA 151-159: -2.2.
  - Oboe 1 54-59: -1.9.
- Phrase-scale movement (momentary loudness detrended over 6 s windows, std; `a6s.py`):

  | Source | All windows | Mid | Loud |
  |---|---|---|---|
  | Mockup master | 1.24 | 1.07 | 1.06 |
  | Mockup mp3 | 1.23 | | |
  | Dvorak 9/i | | 2.51 | 1.55 |
  | Brahms 1/ii | | 2.18 | 2.03 |
  | Brahms 4/ii | | 1.73 | 1.42 |

  This is unchanged since c10.

**Fix (`score_to_parts.py`):**
- For notes inside printed slurs of 4 or more notes, on `LEAD_SPANS` tracks inside their spans, add a vol item of clip(0.3 x (pitch - mean pitch of the slur), -1.5, +2.0) dB.
- Step it at each moved onset with 0.1 qn ramps, and apply it after pitch trims and fills.
- For chords, use the top note.

**Simulated (`simC2.py`, 33 slurs shaped):**
- Top note over the others: median +1.3 -> +2.8 dB. Loudest in 9 -> 13 of 25.
- Master phrase-scale std 1.24 -> 1.31 (mid 1.07 -> 1.12).
- mp3 LRA +0.2 (16.5).
- This makes phrase tops right, but it does not close the gap to the references (inferred: the rest of the gap is note-level and accompaniment movement, which the samples' steady sustains do not have). Implement it after findings 1-3, and check that the lead hairpin fits keep their sign.

## 5. Delivery: after findings 1-4 the limiter is at target, but the LRA is 16.5; lift the three softest pp/ppp passages 2 dB in the mix (measured; simulated)

**Evidence (measured, `lra.py` on the mp3):**
- The bottom 10% of gated short-term loudness comes from these bars:
  - 4-6 (wind chord pp)
  - 30, 35-36
  - 65-66 (return pp)
  - 70
  - 83-85 (ppp coda)
  - 91-92
- The top 5% comes only from bars 60-63 and 79-80.
- The ride is at or near its +10 dB cap (9.6-10.0 dB) in bars 1-2, 84-85 and 91-92. Elsewhere it has a 2:1 ratio, so a mix lift passes through only partly. That is why the +2 dB below moves the LRA only 0.3.

**Fix (`build/roles.json` `_all`):** [9,17,2], [220,226,2], [274,280,2] (1 qn ramps). This is the brief's "raise pp/ppp 2-4 dB in the mix". These are volume-envelope moves, so the pp/ppp CC11 timbre stays.

**Simulated with findings 1-4 (`simD.py`):**
- mp3 LRA 16.2, span 18.8, limiter 2.2, TP -1.7.
- Section LUFS in the mp3:
  - Return -30.2 -> -29.0.
  - ppp coda -31.6 -> -30.1, still 3.8 dB under the pp coda (-26.3).
  - Intro -26.9 -> -26.6.
- To reach 16.0 or lower, add [35,36.9,1.5] (bassoons/BCl pp end of the solo) and [298,304,1] (morendo) only after checking that the morendo still falls at least 4 dB.

## Do not touch

- `deliver_master.py` constants.
- The bars 53-61 rise and bar 61 over bar 79.
- `LEAD_SPANS` with `HP_GAIN_SOFT_DB` 3 / `HP_SOFT_DEC_DB` 2.
- The c15 constraint that theme A's mf at qn 82 stays the top of its phrase. Finding 1 keeps it, with 2.2 dB margin.
- `SOST_HOLD_THROUGH` and `swell_sost`.
- The bar 64-65 drop.
- The 268-273 decrescendos.
- The coda's ppp-pp-ppp order and the morendo.
- The tail hold.
- The timpani roll settle.
- The divisi cut at qn 212.
