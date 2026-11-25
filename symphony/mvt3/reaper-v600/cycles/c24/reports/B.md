# Cycle 24, critic B: balance and levels (on the c23 render)

Sources:
- the c23 stems, master and `render_head/`, the delivered `mvt3-mockup-c23.mp3`, and the c22 stems for before/after;
- `build/parts.json` (the c23 data with the post-render ride rows), `build/mockup-events.tsv`, `sections/arrival.ily`, `sections/finale.ily`;
- score pages 7 and 14;
- the 1FH, 1TP, 1TB, 1TU, CL and OB KS Master `.oib` files, read with `opus_state.load_oib` (nothing written).

I ran copies of the delivery on the c23 master: the unchanged `tools/deliver_master.py`, a scratch `parts.json` with edited `ride_trims`, and the c23 head. The base run (sim0) reproduces the c23 mp3 exactly: -14.0 LUFS, LRA 11.6, TP -1.1, limiter 5.9 dB.

Method notes:
- Stem levels are mean power in 10 ms frames on the score's tempo map, taken only while the track has a note sounding.
- "K" means a K-like weighting (60 Hz high-pass plus a +4 dB shelf at 1.5 kHz, from ffmpeg) on a mono sum.
- Bar loudness on the mp3 is the EBU momentary maximum over 400 ms windows lying wholly inside the bar. The mp3 times are shifted by 0.30 s for the head.
- "Measured" means read from audio, data or patch files. "Inferred" means a judgement from those numbers.

## Manual notes

MANUAL-READING.md has no row for cycle 24, so I read no page range. These are the pages and patch reads behind the findings, and the MANUAL-GAPS items they touch.

| what the manual or patch says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| "Volume should be used to set a loudness level relative to other instruments, while Expression should be used to shape the continually changing dynamics" (p.64). Brass and clarinet KS Masters: the Global Group's CC11 controller (fadeTime 120 ms) drives `Source/volume` through a linear connection (rescaler mode 0, intensity 1.0). This holds for 1FH, 1TP, 1TB, 1TU and CL (patch read). | Every brass CC11 balance change (`INSTR_POST["cc_scale"]` rows, accent bumps, `short_cc_park`) | Partly. The lane is used for level, but the tool sizes it as 40 log10 (CC11) while the patch is linear amplitude, 20 log10. Finding 2. |
| Brass dynamics on CC1, 4 layers (p.101). Measured here: CC1 86 -> 120 plus CC11 88 -> 112 plus fff trims of +5 to +8 dB give 14-17 dB per brass stem from f to fff. | Brass fff 223 / 263 / 279 against the chorale's f | The layers are used as the manual says. The size of the step is a mapping question (finding 1 and "other checks"). |
| MANUAL-GAPS #2 (LegRep RRx4 for brass repeats) | Chorale repeats | Still not needed. c23's 0.12 s gaps hold (not re-measured here). |
| MANUAL-GAPS #13 (bass trombone's lowest notes are transposed tenor samples) | Bars 113-115 | Not in my findings. No change. |

## 1. On the mp3, the chorale's f entry (bars 224-225) is as soft as the p trumpet solo. The cause is the delivery top ride after the fff of bar 223. A +3 dB ride row fixes it with no other change (measured, by simulation)

**Where:** delivery `RIDE_TRIMS` (`build/score_config.py`), qn 892-901 (bars 224-225).

**Evidence (measured):**

| bar | 11-26 (F1, f) | 61 / 62 (Tpt 1 solo, p to mf) | 223 (fff) | 224 / 225 (chorale, brass f) | 226 / 227 (ff) | 230-233 (f) |
|---|---|---|---|---|---|---|
| master, momentary max | -22.3..-29.4 | -34.5 / -34.5 | -7.5 | -24.6 / -23.5 | -21.1 / -16.9 | -22.0..-23.4 |
| mp3, momentary max | -10.9..-17.0 | -14.3 / -14.7 | -7.5 | **-17.7 / -16.3** | -13.2 / -8.9 | -12.5..-13.3 |
| delivery gain | +11.4..+13.2 | +20.2 / +19.8 | 0.0 | **+6.9 / +7.2** | +7.9 / +8.0 | +9.3..+10.1 |

- In the mix, bars 224-225 are as loud as the F1 f and 10-11 dB over bar 62.
- On the mp3 they are 4-5 dB under the F1 f and 2-3 dB under bar 62.
- The top ride is smoothed over 3 s (`SMOOTH_S`). It reacts to the fff chord and is still turned down through the next two bars: those bars get +7 dB, against +9-10 dB for bars 230-233 at the same printed f.
- So a brass chorale marked f sits under a p trumpet solo marked p < mf. This inverts the printed dynamics across the movement, which the shared target forbids (printed shapes and climax order on the delivered file).
- Inside the chorale the balance is right: brass family 6-8 dB over the violins' mf tremolo in bars 224-225 (brass -27.6 / -25.7, upper strings -34.9 / -33.1).

**Fix (simulated on the c23 master):** add `[[892.0, 0.0], [893.0, 3.0], [899.5, 3.0], [901.0, 0.0]]` to `RIDE_TRIMS`. It starts in the printed breath after the fff chord (the brass notes end at 891.71-891.82).

| variant | 224 / 225 / 226 / 227 | 223 (step over 222) | LRA / p10 / limiter | fff -> f drop on the mp3 at +0.3 s |
|---|---|---|---|---|
| c23 (sim0) | -17.7 / -16.3 / -13.2 / -8.9 | -7.5 (+3.5) | 11.6 / -22.4 / 5.9 | 9.7 dB |
| **sim2 (row above)** | **-15.4 / -13.3 / -13.2 / -8.9** | -7.5 (+3.5) | 11.6 / -22.4 / 5.9 | 8.0 dB |
| sim1 (row held to 904, released at 910) | -15.4 / -13.3 / -10.3 / -7.9 | -7.5 | 11.7 / - / 5.9 | |

- sim1 put bar 227 within 0.4 dB of the arrival. Do not use it.
- sim2 leaves every other bar unchanged.

**Optional, for Dan's AirPods note (sim3 = sim2 plus two rows):** `[[679.5,0],[680,2],[719.5,2],[720.5,0]]` (bars 171-180, muted trumpet with cor anglais) and `[[383.5,0],[384,2],[391.8,2],[392,0]]` (bars 97-98, the closing's pp).
- These are the quietest stretches on the mp3: momentary max -23.0..-25.3. The lift is already at its 10 dB cap there (ride max +10.0).
- Result: those bars rise 2.1 dB (176 -24.4 -> -22.3, 98 -25.3 -> -23.2), p10 -22.4 -> -21.9, LRA 11.6 -> 11.2, limiter 6.0.
- Bars 181-182's crescendo and bar 99's ff entry still rise over them.
- Adopt sim3 only if Dan's "near-max volume" complaint outranks the LRA of about 12.

## 2. Brass CC11 is linear amplitude (20 log10), not 40 log10. Every brass `cc_scale` row and CC11 bump since c18 delivered half its planned dB. Horn 3 is still 6-9 dB under Horn 4 in bars 235-237 (measured)

**Where:**
- `tools/instr_post.py` `cc_scale` (default `k` 40, comment near line 455);
- `loop/LEARNINGS.md` line 352 (c18);
- `build/score_config.py` c23 block: Horn 3 / Horn 4 rows over 935.6-947.75, Trumpet 3 accents 1016-1048.

**Evidence (measured):**
- The patch read is in the Manual notes: CC11 drives `Source/volume` linearly in the 1FH, 1TP, 1TB, 1TU and CL KS Masters.
- c22 to c23, same notes and same CC1 (36), only CC11 changed:

| track, bars 235-237 | CC11 c22 -> c23 | measured change (three bars) | 20 log10 | 40 log10 |
|---|---|---|---|---|
| Horn 3 | 46 -> 73 (`cc_scale` +8 dB, k 40) | +4.0 / +4.0 / +4.0 dB | +4.0 | +8.0 |
| Horn 4 | 46 -> 39 (-3 dB, k 40) | -1.4 / -1.4 / -1.5 dB | -1.4 | -2.9 |

- The c18 LEARNINGS line gives the formula as 40 log10, but its own numbers are 20 log10 values: a 10 % bump is +0.83 dB at 20 log10 against +1.66 dB at 40 log10, and the line says +0.8.
- The tool's default `k` of 40 therefore delivers half of every planned brass dB.
- The same cause explains:
  - Trumpet 3's accents stopping at +1.3 dB (target 2-3): the bump is CC11 88 -> 106, which is +1.6 dB at 20 log10.
  - Horn 3's residual gap. Now (K): Horn 3 -49.8 / -50.2 / -49.3 against Horn 4 -43.6 / -41.6 / -40.5, so 6.2 / 8.6 / 8.8 dB under (target 1-3). Both play p chord voices: G3 / A3 over E3 / F3, velocity 53, "Sus MAX".
- Woodwinds are different, because their CC11 also crossfades layers: Oboe 1's CC11 61-69 -> 86-98 gave +11.3 dB (c22 -54.4 -> c23 -43.05 raw).

**Fix:**
- In `tools/instr_post.py`, use `k` 20 for `cc_scale` on the brass and clarinet tracks, where CC11 is pure volume. Woodwind and string rows keep their fitted `k`, because their CC11 also crossfades layers. Correct LEARNINGS line 352 and the comment.
- Horn 3, 935.6-947.75: target CC11 about 120. Write it as `cc_scale` +8.3 dB with k 20 from the c22 base of 46, or the equivalent row on the current lane: 73 -> 120 is +4.3 dB.
- Horn 4: CC11 46 -> 31, which is -3.4 dB with k 20 (now 39).
- Expected (inferred from the measured slope): Horn 3 0.5-3 dB under Horn 4 (K +4.3 and -2.0 on the two stems). CC1 stays at 36, so the p timbre is kept.
- Trumpet 3 accents 1016-1048: `amt_rel` 0.20 -> 0.33. The bump becomes CC11 88 -> 117, which is +2.5 dB. The resting value leaves room up to 127.
- Before the actor reuses any brass offset planned at k 40 (for example c23 B's earlier "`short_cc_park` 100 -> 127 = +4.2 dB", really +2.1), it should halve the expectation or double the dB.

## 3. The fff arrivals: no breath or caesura is printed before bar 223 or bar 263. The printed breath comes after the fff chord, and the render plays it. Drop the 6 dB pre-arrival dip target (measured from the score and data)

**Where:** qn 887-888 and 1047-1048, `CAESURA` 888 / 1048 and the 1048 string `note_end` `gap_next_s` rows in `build/score_config.py`.

**Score (`mockup-events.tsv`, `sections/arrival.ily`):**
- Bar 222 is f / mf with a crescendo into the fff of 223. Bar 221-222 carries the printed allargando, with only Bn 1 and Cbn breathing at 884 (the start of bar 222).
- Trumpet 1 B -> C, Horn 1, Tbn 1 and Tuba change note at 888 with no breath mark.
- The breath (`\breathe`, c136 in `arrival.ily`) is printed after the fff chord, before the chorale's f at 892, in Tpt 1-2, Hn 1-4 and Tbn 1-2.
- At 1048 every wind and brass note changes pitch into a tie (crescendo from 1024, no breath). Only Fl 1 breathes, at 1044. Violins I carry a printed down-bow at 1048, which supports their c23 lift.

**Render (measured):**
- The printed breath at 892 is there: brass gaps of 45-65 ms (Tpt 1 891.82 -> 891.91, Hn 1 891.71 -> 891.83). The master falls 16 dB from the fff to the f (-8.1 -> -24.2 in 50 ms frames) and the mp3 9.7 dB at +0.3 s.
- Before 888 the master dips 1.7 dB, then steps +5.5 dB onto the arrival (-13.5 -> -8.0).

**Judgement (inferred):**
- A real orchestra plays the leading-tone resolution into 223 and 263 without a breath. The arrival is made by attack and level, and the render has both: +3.5 / +1.2 dB in-bar steps on the mp3.
- A 6 dB silence before an unmarked tie or resolution would contradict the score.
- Keep the 888 caesura: it sits inside the printed allargando. The 1048 caesura (0.05 s, 176 -> 111 bpm) has no printed rit. at 262 and is a liberty, but small. Keep the Violins I lift (down-bow) and add no wind or brass lift.
- Treat the dip target as met.

## 4. Two soft inner voices sit level with the line they accompany: Oboe 1 in bars 143-144 (the c23 overshoot) and Clarinet 1's pp in bar 121 over the end of the bassoon solo (measured)

**Oboe 1, qn 568-576.**
- Score: Ob 1 F5 mf and Cl 1 D5 mf, under Fl 1 G5 / A flat 5 mf and Vln I f.
- Measured (K): Oboe 1 -38.5 / -38.4, Clarinet 1 -38.9 / -38.7, Flute 1 (top voice) -43.8 / -45.2. The oboe is level with the clarinet and 5-7 dB over the flute that carries the top note.
- Fix: in the c23 `cc_scale` row (Oboe 1, k 33), +5 -> +3.2 dB, so CC11 86-98 -> about 76-87.
  - c22's 61-69 measured -54.4 raw and c23's 86-98 -43.05 raw. Interpolating, 76-87 gives about -47 raw, 4-5 dB under the clarinet (inferred: the woodwind CC11 response is not linear).

**Clarinet 1, qn 480.8-486 (bars 121-122).**
- Score: Cl 1 "1." pp < > on D6 / C sharp 6, while Bassoon 1 ends its "solo, espress." p with a decrescendo (page 7).
- Measured (K): Clarinet 1 -44.7 / -43.2 against Bassoon 1 -43.8 / -43.3 over 481.2-482.9 / 483.1-484. The pp echo is as loud as the solo it answers.
- Data: CC11 34-40, CC1 28-35, vol -2..-4 (the printed hairpin). The level comes from the register (altissimo samples).
- Fix: Clarinet 1 `cc_scale` -5 dB, k 20, over 480.8-486 (CC11 34-40 -> 19-22). The CL KS Master's CC11 is linear volume (patch read). CC1 keeps the pp layer.
- Expected (inferred): 4-6 dB under the bassoon.

## 5. The fff mapping differs by family. From f to fff, brass and strings rise 12-17 dB per stem and the woodwinds 3-6 dB. Inside the fff chord, the lower voices of identical-data pairs are 3-5 dB over the upper ones (measured; fix inferred)

**Evidence (measured).** Median K body level of held notes of 1.4 qn or more, outside hairpins, by printed dynamic:

| | f | ff | fff | f -> fff |
|---|---|---|---|---|
| Trumpet 1 / Horn 1 / Trombone 1 | -34.1 / -38.8 / -35.2 | -26.4 / -27.1 / -27.7 | -19.1 / -21.8 / -22.8 | +15.0 / +17.0 / +12.4 |
| Violins I / Violins II / basses | -33.8 / -35.8 / -39.2 | -30.1 / -31.6 / -32.8 | -20.3 / -19.7 / -22.2 | +13.5 / +16.1 / +17.0 |
| Flute 1 / Oboe 1 / Bassoon 1 / Bass clarinet | -38.6 / -37.7 / -39.0 / -33.5 | -34.6 / -35.5 / -34.4 / -31.7 | -28.6 / -34.1 / -34.9 / -34.1 | +10.0 / +3.6 / +4.1 / -0.6 |

- Family sums, upper woodwinds against brass: ff (bars 91-94, 211-214) -7.2 / -6.3 dB; fff (223 / 263 / 278) -10.4 / -10.2 / -11.5 dB.
- At p the families agree within about 5 dB (winds -44..-50, brass -46..-51, strings -45..-48). The divergence is only at the top.

**Within the 223 chord, identical data** (CC1 120, CC11 112, vol +5, velocity 127, "Sus MAX"):
- Trombone 2 (E3) -19.2 against Trombone 1 (G3) -23.8;
- Horn 4 (C4) -18.8 against Horn 1 (C5) -21.8.
- These are sample levels by pitch.

**Judgement (inferred):**
- Woodwinds have a small real dynamic range, and brass at fff covers them. The fff arrival is now the climax Dan asked for, so do not lower the brass.
- Two cheap instrument-side corrections:
  - Woodwinds `dyn_trim_db` fff +2 dB (Flutes, Oboes, Clarinets, Bassoons, Bass clarinet; the CC11 is already 112-117). That brings the upper winds back to their ff relation (about -8 dB under the brass) at the three arrivals.
  - Trombone 2 CC11 -3 dB (k 20: 112 -> 79) over 887.9-891.7 only.
- This is lower priority than findings 1-4.

## 6. Other movements' findings, checked on this render (measured unless marked)

- **Scherzo c20, pre-arrival delivery ride:** applies and is in place since c23 (+3.5 / +1.2 / +1.1 dB steps). Finding 1 adds the release side.
- **Scherzo c20, Detaché row for slurred staccato pairs, and the any_dyn release cap:** articulation lens. c23 found that any_dyn does not apply here. Not re-checked.
- **Scherzo c20, keyswitches missed by range renders:** process note for the actor's range pass (c23 already chose its range starts by it).
- **Scherzo c21, wetter tail after loud stops at -14:** c23's mp3 stops are 14.8-16.1 dB at +0.3 s, within 14.5-17. The final chord's tail row works (15.6).
- **Scherzo c21, quietest music against AirPods:** bars 97-98, 124 and 171-180 are the quietest at -23.0..-25.5 momentary max on the mp3, and the lift is at its 10 dB cap there. sim3 in finding 1 lifts them 2.1 dB.
- **Scherzo c21, phrase shapes swelling long bass notes:** the basses' printed pp B flat pedal (bars 43-50, re-bowed at 164 / 170.9 / 181.7 / 190.5) rises 14-20 dB from each re-bow to a peak about 1 s later. CC11 is flat (33 -> 27), so this is the slow pp attack at each re-bow, not a phrase rule. There is also a fader ramp of -5.5 -> -3 dB inside the 170.9 note (172-174.5), which is no printed hairpin and breaks the standing rule. Hand both to the actor's re-bow / data check.
- **Swapping rows carries region gain:** nothing swapped this cycle.

Other checks:
- **Solos over accompaniment** (K, active frames):
  - Trumpet 1, bars 51-66: 7-9 dB over the pizzicato strings and clarinets.
  - Bassoon solo, 115-122: 8-10 dB over the strings.
  - Muted Trumpet 1 with cor anglais, 171-186: within 1-3 dB of each other as a doubling, 6-12 dB over the strings.
  - Violins' F2, 67-82: Vln I 1.3-3 dB over the celli's counter-melody, 6-9 dB over the harp.
  - Trumpets' theme B, 211-218: 5.5 dB over the next stem.
  - Counterstatement 27-34: the bass theme group about 6 dB over the violin countersubject.
  - Violins II in 230-233: 0.1 / 5.3 / 2.3 / 2.5 dB under the violas (c23 target met). The cellos' melody in 123-127 is only 1 dB over the harp's arpeggios (acceptable).
- **Timpani:** never the loudest stem in any roll (rank 13-24 of 21-29). Its share of the dry sum is -15 to -24 dB, and the rolls settle (920-933: -38 -> -43, then the printed decrescendo).
- **Arrival and ending low end:** in 30-150 Hz the basses carry -1 to -3 dB of the master, the bass drum -6 at its strokes, the timpani -9.5 to -17 and the tuba -8 to -11. The low brass and drums do not cover.
- **Crash:** -6..-9 dB of the master's 2-8 kHz in the first 0.5 s, then -13..-17 dB. It is heard and is not dominant.
- **Loop pulsing:** only three notes over 6 s survive the re-bows (timpani roll 920, crash 888 / 1048). They are shaped by printed hairpins and ring, not loops.

**Do not touch:**
- the c23 ride rows (223, 263, final with its tail row, bar 130);
- the solo-against-accompaniment levels listed above;
- the chorale's internal brass-over-tremolo balance;
- the timpani CC7 fold and the roll levels;
- the basses' low-end share and the crash level;
- Violins II's role split at 899.9 and the trumpets' v95 off-beats.
