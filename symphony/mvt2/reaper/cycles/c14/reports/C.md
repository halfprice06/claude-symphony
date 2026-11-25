# Cycle 14, critic C: dynamics over time (on the cycle 13 render)

Lens: the shape of every hairpin and phrase, the loudness arc against the score, loudness range, swells and decays on long notes, comparison with real orchestras.

Material: `cycles/c13/render` (master and 29 stems; the stems sum to the master), `cycles/c13/mvt2-mockup-c13.mp3`, `cycles/c13/metrics`, `build/parts.json` (unchanged since the render), `build/{roles,note_trims,pitch_trims,early_fills,mix}.json`, `tools/score_to_parts.py`, `build/mockup-events.tsv`. References: the Dvorak 9/i MP3 and the stored Brahms 1/ii and 4/ii loudness series (`symphony/render/critics/c04/ref_*_musopen/`).

Scripts and outputs: `/private/tmp/claude-501/mockup-loop/c14-C/`, run with `~/.venvs/claude-composes-reaper/bin/python`. They are the c10-C set pointed at c13, plus new ones: `hp3.py`/`hp3b.py` (every hairpin, lead lines separately), `win.py` (stem level, CC11 and vol_db per window), `notelev.py`, `pres.py` (per-pitch residuals), `peaks.py` (phrase tops), `sost.py`, and simulations `hpsim.py`/`hpsim2.py` (findings 1-2), `lvsim.py` (finding 3), `sostsim.py` (finding 4), `sfsim.py` (bar 63). Simulations scale the stems by the proposed dB change on the score-time grid, sum them and run the unchanged `tools/deliver_master.py`. Levels are plain RMS per stem or master unless marked LUFS (energy mean of momentary loudness per bar).

## Delivery, c13 (measured)

- Master: -23.3 LUFS, LRA 23.9 LU, TP -3.6 dBFS. Short-term p10 to max 26.7 dB. Climax rise over the 15-20 s before it: 12.5 dB.
- mp3: -19.8 LUFS, LRA 15.8 LU, TP -1.6 dBTP, span 18.2 dB, limiter 3.1-3.2 dB, ride at its +10 dB cap in bars 1, 83-84 and 92. Climax rise 10.6 dB. 5 s moves kept: median 0.80. Inversions: 0 of 144.
- All delivery targets are met, except that the limiter is 0.1-0.2 dB over 3 dB. None of the fixes below makes the delivery worse in simulation.

## What holds (measured)

- The large-scale arc. Bars 53-61 rise every bar except the printed subito p at bar 57 (LUFS -32.6, -29.6, -28.0, -25.7, -26.6, -23.0, -21.2, -17.1, -14.8). Bar 61 is the loudest bar, 1.5 dB over bar 79.
- The bar 60 crescendo: the master rises 5.9 dB across it, and the ff arrives 1.3 dB higher.
- The bar 64 to 65 return: -26.0 to -40.9 LUFS.
- The bars 81-82 decrescendo: -8.0 dB over qn 268-271 and -5.1 dB over 271-273.
- The morendo, qn 298-301: -4.7 dB. The final ppp chord is 1.8 dB under the opening ppp chord.
- Ensemble hairpins: all 21 hairpins shared by three or more tracks move the master in the printed direction except one (qn 124-128, -1.4 dB, inside finding 1).

## 1. Soft hairpins in the solo and melody lines barely move: median +1.7 dB on 20 crescendos, and 7 are flat or falling (measured; fix simulated)

**Where:** every exposed p/mp hairpin.
- Horn 1 solo, bars 7-12 and 67-70.
- Oboe 1, bars 15-20 and 47-50.
- Violin I solo, bars 17-21.
- Violins I/II theme A, bars 23-28 and 71-76.
- Bass clarinet solo, bars 31-36.
- Cor anglais and Flute 1, bars 41-56.
- Clarinet 1 in the coda.

**Evidence (measured, `hp3.py`):**
- A lead line here is a stem within 6.5 dB of the master over the hairpin. Each hairpin's level change is a linear fit of the stem's 50 ms RMS from onset + 0.2 s to end - 0.4 s, which excludes attacks and breaths.
- The 20 lead-line crescendos have a median of +1.7 dB. One printed level in this render is about 5 dB: Violins I stem medians are p -43.2, mp -38.3, mf -35.5 (`metrics.md`).
- Flat or falling crescendos:
  - Hn1 32-34: -9.5 dB
  - Vln I solo 48-51: -2.4
  - Fl1 126-128: -2.7
  - Vln I 68-70: -1.9
  - BCl 93-96: -1.5
  - Vln I solo 60-62: +0.3
  - Vln I 240-242: +1.0
- Flat or rising decrescendos: Vln I 70-72 +1.2, Ob1 57-59 +0.6, BCl 102-105 0.0, Ob1 148-151 -0.6. So the theme A messa di voce (bar 23, < >) comes out > <.
- Cause: `hpgain` (the dB ramp) exists only for crescendos that arrive at mf or louder (`HP_GAIN_DB`, `HP_GAIN_MF_DB`). Soft hairpins get CC11 only.
  - At soft levels, CC11 moves little level. Regressed over each track's notes (`pres.py`): Violins I 0.19 dB per CC, Horn 1 0.11 dB per CC.
  - Hn1's p < mp is CC 54 to 65, worth about 1.2-2 dB.
  - Theme A's untargeted < > is capped at +5 CC (61 to 66) by the c11 rule that keeps the mf goal at qn 82 on top, worth about 1 dB.
  - Sample and pitch unevenness of 2-4 dB (finding 2) then decides the direction.

**Fix (`tools/score_to_parts.py`, in the hpgain block after `HP_GAIN_MF_DB`):**
- Add `HP_GAIN_SOFT_DB = {"wind": 3.0, "string": 3.0, "brass": 3.0}` and `HP_SOFT_DEC_DB = 2.0`.
- Add `LEAD_SPANS` (track: list of qn spans):
  - Horn 1 [(17,40), (226,236)]
  - Oboe 1 [(42,60), (139,152)]
  - Violin I solo [(48,65)]
  - Violins I and Violins II [(65,90), (237,262)]
  - Bass clarinet [(90,109)]
  - Cor anglais [(124,171)]
  - Flute 1 [(124,129)]
  - Clarinet 1 [(280,292)]
- Rule for a hairpin inside a lead span that starts at CC11 66 or lower and has no hpgain:
  - A crescendo gets an `hpgain` item: 0 at its start, +3 dB at its end.
  - If a decrescendo starts within 0.3 qn of the crescendo's end (a messa di voce), hold the gain to that point and release it linearly across the whole decrescendo, back to 0 at its end. Otherwise hold it to the next onset and release over `HP_REL`.
  - A decrescendo that does not follow such a crescendo ramps 0 to -2 dB, held to the next onset, released over 1 qn.
  - These are volume-envelope moves, so the timbre stays at the printed level.

**Simulated (stems scaled by exactly this shape, `hpsim.py`):**
- Lead crescendos: median +1.7 to +3.6 dB. Lead decrescendos: median -3.9 to -4.1 dB.
- Theme A 70-72 turns the right way (+1.2 to -1.0), and 240-244 goes +3.2 / -6.6.
- Delivery: mp3 LRA 16.0, span 18.3, limiter 3.1, inversions 0 of 161, 5 s moves kept 0.83.
- Hn1 32-34, Vln I 68-70 and the solo's 48-51 stay flat because note-level trims work against them. Finding 2 fixes those.

## 2. Inside those phrases, trims and fills make the pickup or the attack louder than the phrase's top note (measured; partly simulated)

29 lead-line slurs of four or more notes were measured (`peaks.py`). The highest note is a median of only +1.1 dB over the other notes, and it is the loudest note in only 11 of the 29. The clearest cases follow, each with its cause in the build data.

**a. Horn 1, bars 11-12 (qn 31.5-34), the solo's climb to its top note (p < mp).**
- Measured per 0.25 qn:
  - C4 pickup -39.5.
  - F4 attack -37.8.
  - F4 body -43.0, -45.9, -45.3, -46.1 under the crescendo.
  - Bb4 arrival (mp, the top) -41.9.
- Causes:
  - The F4 pitch trim `{"early": 1, "body": -5}` steps 6 dB down 0.35 s into the note.
  - Horn 1 C4 (60) is hot: median residual +2.1 dB over 9 notes (`pres.py`). This also affects qn 19.5, 31.5 and 38.0.
- Fix:
  - `build/note_trims.json` Horn 1 `"32": 2.5` (net body -2.5 on this note only).
  - `build/pitch_trims.json` Horn 1 `"60": -2`. The track already has `_all_arts`.
- Simulated with finding 1: the F4 body rises from -41.8 to -38.1 into a Bb4 at -39.0. The F4 attack spike is still there. If the next render shows it, set this note's early value to -2.

**b. Bass clarinet solo, bar 32 (qn 93), the "solo, espr." crescendo.**
- The early fill `{"db": 5, "hold_s": 0.45}` sits on an attack that is already hot. It makes a 0.4 s plateau at -31 to -33 dB (master -31.6, the loudest moment of bars 31-36).
- The body then drops to -40.4 under the 0.6 s ramp of the note trim -6, and climbs only to -36.3 at the crescendo's peak (qn 96).
- Fix:
  - Delete `early_fills.json` Bass clarinet `"93"`.
  - Set `note_trims.json` Bass clarinet `"93"` from -6 to -4.
- Simulated: the 93-96 fit goes from -1.5 to +2.5 dB, and the attack is no longer the phrase peak.

**c. Violins I, theme A bar 23 (qn 67.5-68.5).**
- The fill `"67.5": 5` boosts the C5 pickup, which is itself a hot pitch (pitch 72 median residual +1.8 dB over 9 notes). The pickup ends at -34.4 dB per 0.125 qn.
- The Eb5 phrase top then lands at -42.1 and reaches -39.5 only at 68.25, when the `note_trims` 68 +4 has ramped in. That is a 7.7 dB drop onto the top note of the phrase.
- Fix:
  - `early_fills.json` Violins I `"67.5"`: 5 to 0.
  - Add Violins I `"68": {"db": 3, "pre_s": 0.05, "hold_s": 0.35}`.
  - `pitch_trims.json` add `"Violins I": {"72": -2}` (legato only). This also lowers the C5s at 0, 72, 79.5, 86, 171, 184 and 292.
  - The 184 C5 is the bar 56 mf arrival, which spikes to -29.7 and decays 7.5 dB.

**d. Violin I solo, bars 17-18 (qn 48-53).**
- Bb5 at 48.5 has a body of -42.7, 2.5-4 dB over the other notes.
- The crescendo's top, Eb5 at 51, is -47.2.
- The Db5 at 53, after the decrescendo, is -44.3: 3 dB over the top.
- Fix: `note_trims.json` add `"Violin I solo": {"48.5": -2, "53": -3}`.
- Simulated with finding 1: the 48-51 fit goes from -2.4 to +1.5 dB. The phrase peaks at 50.5-51 (-43.5) and ends at -46.0.

## 3. The soft half of the movement sits at one level: the pp coda is as loud as the p solos (measured; fix simulated)

**Where:** bars 1-22 (ppp/pp opening, then p horn, oboe and solo violin), bars 67-70 (p horn solo), bars 83-92 (ppp-pp-ppp coda).

**Evidence (measured, LUFS energy mean per section, master / mp3):**

| Section | Master | mp3 |
|---|---|---|
| Intro, bars 1-6 (ppp/pp) | -40.4 | -26.2 |
| Horn solo, bars 7-14 (p) | -37.8 | -25.2 |
| Oboe/solo violin, bars 15-22 (p) | -37.3 | -25.2 |
| Horn solo, bars 67-70 | -37.9 | -25.4 |
| Coda, bars 83-85 (ppp) | -42.7 | -29.0 |
| Coda, bars 86-91 (pp) | -37.6 | -25.0 |

- The pp coda (bar 87, -36.1 LUFS) is louder than every bar of the opening and level with the p solos.
- In the mp3, the opening is only 1.0 dB under the solos. The ride compresses the master's 2.6 dB to 1.0, because it sits at its cap there.
- c12 C #2 found the same (target: coda about 2 dB under the solos), and it is still open.
- The c12 coda horn lift (+5/+3) and the c10/c11 soft-trim raise both pushed the coda up.

**Fix (`build/roles.json`):**
- Add +2 on the exposed p solos. This is also the brief's item 6 ("exposed soft solos +2-3 dB"):
  - Horn 1 [17,40,2], [226,236,2]
  - Oboe 1 [42,48,2], [54,60,2] (outside its existing [139,151,2.5])
  - Violin I solo [48,65,2]
  - Bass clarinet [90,108,2]
  - Cor anglais [124,137,2], [151,171,2]
- Add `"_all"` [283.5, 304, -2].
- pp keeps its CC11 layer, so the coda's timbre does not change.

**Simulated (with findings 1-2, `lvsim.py`), mp3:**
- Solos -24.3 LUFS. Intro -26.4. pp coda -26.4 (now 2.1 dB under the solos). ppp coda -28.2.
- LRA 16.0, span 18.4, limiter 3.0, inversions 0 of 168, climax rise 10.8 dB.
- Nothing soft gets quieter in the mp3 except the coda, by 1.4 dB.

## 4. Bars 61-62, ff "molto sostenuto": every half-bar note decays, so the climax pulses 2.5-3.7 dB every two beats (measured; fix simulated)

**Where:** qn 204-212, all strings, winds and horns.

**Evidence (measured):**
- Attack (+0.15-0.5 s) to the last 0.45 s of each long note (`sost.py`):
  - Vln I -3.2 / -2.0 / -3.5
  - Vln II -2.1 / -4.0 / -2.2 / -4.1
  - Vla -3.1 / -3.7 / -1.8
  - Vc -2.4 / -2.4 / -1.2
  - Hn2 -7.0 on all three notes
  - Bn1 208 -6.1, Tuba 210 -7.1, Cl1 206 -12.3
- Master per 0.25 qn has a dip before every note change:
  - qn 205.5-206: -20.0 / -20.3, against -17.6 at 205.0
  - qn 207.5: -21.8, against -18.1 at 206.5
  - qn 209.25-209.5: -21.4 / -21.6, against -18.7 at 208.25
- A sostenuto played by a real section holds the bow and breath level to the change (inferred).
- Cause in the plan (parts.json): these notes get the long-note "swell" shapes. The CC11 contour rises +4 at 40% and falls to -2 at the end, so Vln I CC11 cycles 119-122-120-117 every 2 qn. `swell_db` rises +1.5 at 40% and falls to 0 at 80%. Both add to the samples' own decay.

**Fix (`tools/score_to_parts.py`):**
- For a note whose onset lies inside `SOSTENUTO_SPANS`:
  - (a) In `contour()`, `swell` holds +4 after 40% instead of falling to -2.
  - (b) Replace its `swell_db` item with a hold: 0 at 40% of the note, rising to +`SOST_SUSTAIN_DB` = 2.5 dB at (next moved onset - 0.25 qn), then back to 0 at the moved onset, so the next legato attack is not lifted.
- Apply this to the string, wind and brass families.

**Simulated (+2.5 dB on that shape, `sostsim.py`):**
- The dips shrink to -19.5/-19.9 (205.5-206), -19.9 (207.5) and -20.0/-19.8 (209.25-209.5): 1-2 dB.
- Master peak -3.55 dBFS (was -3.64). Limiter 3.0 dB. mp3 LRA 16.0, span 18.5.

## 5. Phrase-level movement is still 30-45% flatter than a real orchestra's (measured; fix inferred, lower priority)

**Evidence (measured):**

Momentary loudness, linearly detrended in 6 s windows, standard deviation (`a6.py`), soft / mid / loud passages:

| Source | Soft | Mid | Loud |
|---|---|---|---|
| Mockup master | 1.34 | 1.28 | 1.04 |
| Dvorak 9/i | 1.80 | 2.51 | 1.55 |
| Brahms 1/ii | 2.62 | 2.18 | 2.03 |
| Brahms 4/ii | 2.11 | 1.73 | 1.42 |

- 90th percentile of the 1 s change in short-term loudness: mockup 1.85 dB, references 2.26-3.13 (`a1.py`).
- This is unchanged since c10, which measured 1.05-1.43.
- Findings 1-4 together raise the mp3's mid-level value only from 1.32 to 1.41 (simulated).
- With finding 2's phrase-top numbers (+1.1 dB median), this points at the missing note-to-note shaping: in a lead line, higher notes are not played louder.

**Fix (inferred):**
- In `score_to_parts.py`, for legato notes on the `LEAD_SPANS` tracks, inside slurs of four or more notes, add a vol item of clip(0.3 dB x (pitch - mean pitch of the slur), -1.5, +2.0).
- Apply it after the pitch trims (which remove sample unevenness, so the two do not fight), with a 0.1 qn ramp at each moved onset.
- Do it only after findings 1-2 are rendered, and check that the hairpin fits do not reverse.

## Measured, not proposed

**Bar 63 sf (qn 212):**
- At beat level it is 0.8 dB under the last ff beat of bar 62. Per 0.125 qn it peaks at -17.4 against -18.3 at qn 211.1, for about 0.15 s.
- Holding the strings' chord/divisi cut back to 212.25 and adding 2 dB (`sfsim.py`) makes the Vln II sf attack the master peak (-0.9 dBFS) and the limiter 5.8 dB. c10 rejected this for the same reason. Leave it.

## Do not touch

- `deliver_master.py` constants (0 inversions, climax rise 10.6 dB).
- The bars 53-61 rise and bar 61 over bar 79 by 1.5 dB.
- `HP_CHAIN` / `HP_CHAIN_RISE` (bar 60 now +5.9 dB at the master).
- `SOST_HOLD_SHARE` 0.5.
- No gain on the bar 63 sf.
- The bar 64-65 drop and the 268-273 decrescendos.
- The coda's ppp-pp-ppp order and the morendo (-4.7 dB).
- The c11 cap that keeps theme A's mf goal (qn 82) over its first swell. Finding 1 changes the volume envelope, not that CC rule.
- The timpani roll factor.
