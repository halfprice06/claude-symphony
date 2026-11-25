# Cycle 22, critic B: balance and levels (on the c21 render)

Sources: the c21 stems and master, the delivered `mvt3-mockup-c21.mp3`, and the c20 stems for comparison. I read `build/parts.json`, `build/mix.json`, `build/mockup-events.tsv`, score pages 4, 12, 13 and 15, and the two harp `.oib` files. I also ran about ten copies of the unchanged `tools/deliver_master.py` on the c21 master, with edited `ride_trims` in a scratch `parts.json`. The base run reproduces the c21 mp3 exactly: -14.0 LUFS, LRA 12.2, limiter 5.7 / 4.2 / 3.8 dB.

Method notes:
- Bar loudness is the EBU momentary maximum. I count only 400 ms windows that lie wholly inside the bar. c21's `deliv_meas.py` lets each bar's windows run 0.2 s into the next bar, so bar 222 picked up bar 223's attack: it reads -8.0 there, and -9.5 when the windows stay inside the bar.
- Stem levels are RMS over 25 ms frames.
- "Measured" means read from audio or data. "Inferred" means a judgement drawn from those numbers.

## Manual notes

MANUAL-READING.md has no row for cycle 22, so I did not read a page range. The pages below are the ones behind my findings.

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Harp Sustain RR: "CC 11 (Expression) and Note Velocity control overall loudness" (p.69). Every harp Maestro patch says the same (p.68-69). | Harp, all 300 notes. c21 moved it to the Harp KS Master. | **No.** The KS Master's Global Group has no `MidiVelocity` processor and no Velocity->Volume connection. Harp Sus RR has both (sensitivity 0, a square-law table). Velocity now picks only the layer. Finding 1. |
| Note Velocity Sensitivity curve, -100 to +100 (p.150) | Harp | The curve cannot replace the missing processor: it shapes velocity response, and the KS Master has no velocity-to-volume path for it to shape (read in the `.oib`). |
| Velocity sets loudness for short, plucked and percussive sounds; CC11 sets dynamics on sustained ones (p.53, p.64) | Harp (plucked); trumpet staccato off-beats (finding 6) | Harp: no (finding 1). Trumpets: yes, since c21's park. |
| Each KS Master row has its own volume (p.137) | Harp "Harmonics" row (region gain -5 dB) | Yes. It needs a new value once velocity scaling returns (finding 1). |
| MANUAL-GAPS "Checked": Harp Sus RR velocities 46-112, no nail picks (p.69) | Harp | Still true on the KS Master: the highest velocity is 123, under the 124-127 nail zone. |

## 1. The Harp KS Master ignores velocity for loudness: soft harp is 8-9 dB too loud and ff 3.5 dB too soft. The p accompaniment in bars 235-238 now sits over the violins' mf tune (measured)

**Where:**
- Harp, every passage.
- Worst at the p solo, bars 123-128 (qn 488-512).
- Also at the molto cantabile, bars 235-238 (qn 936-952): harp p arpeggios under Violins I/II mf "molto cantabile" and Clarinet 1's p "1." line.

**Evidence (measured).** For every onset with at least 0.24 s before the next, I took the c21 peak minus the c20 peak, grouped by velocity. The velocities are the same in both renders.

| velocity | 52 | 58 | 64 | 70 | 78 | 90 | 96 | 116 | 123 |
|---|---|---|---|---|---|---|---|---|---|
| c21 - c20 (dB) | +10.2 | +9.1 | +8.2 | +7.3 | +2.4 | +1.4 | +0.7 | -4.4 | -3.5 |
| model -4 - 40 log10(v/127) | +11.5 | +9.6 | +7.9 | +6.4 | +4.5 | +2.0 | +0.9 | -2.4 | -0.6 |

The model is c21's gain change (-3.6 -> -7.6 dB) plus the removal of Sus RR's Velocity->Volume table. That table is (v/127)², about 40 log10(v/127) dB. The model fits within 1.5 dB at six of the nine velocities.

**Cause (read in the patch files).**
- `Harp Sus RR.oib`, Global Group: `MidiVelocity` with sensitivity 0, and a connection "Amount Velocity->Volume" to `Source/volume` with the square-law `tableValues`.
- `Harp KS Master.oib`, Global Group: no `MidiVelocity` processor. Its only `Source/volume` modulation is "Amount Controller 1->Volume" from CC11.
- The harp's CC11 is a constant 110 (parts.json), so every harp note now plays at one loudness per layer.

**What a listener hears (measured, per bar):**
- The p solo at 123-128 went from -53.6..-48.4 (c20) to -44.6..-40.6 dB (c21). The ff chord at bar 132 went from -28.6 to -32.1. The harp's printed p-to-ff contrast fell from 25 to 12.5 dB.
- In bar 235 the p harp is the loudest stem (-37.6), 3.3 dB over Violins I (mf, the tune). It is 8 dB over Clarinet 1's p line (-45.6). In c20 the harp was at -46.4 there.
- The "3 dB louder outside the harmonics" in CHANGES is an average over 264-326, where the velocities are 78-96. The p passages moved 8-9 dB.

**Fix:**
- `tools/build_reaper.py`, in the Opus state edit for a track whose mix.json has a new flag `"vel_volume": true` (set it on "Harp"):
  - copy the `MidiVelocity` processor from `Harp Sus RR.oib`'s Global Group into the KS Master's Global Group;
  - copy its connection `{"source": "Midi Velocity/output", "destination": "Source/volume", ... tableValues}` verbatim;
  - keep the CC11->Volume connection.
- Harp `gain_db` -7.6 -> -3.6 (c20's value). The model predicts c20's level at every velocity within ±2 dB.
- Harmonics (vel 46): with velocity scaling they lose 17.7 dB, so `region_gain_db` Harmonics -5 -> +8.5 dB keeps them at c21's level. Alternatively, keep -5 and raise the three harmonic notes to velocity 100.
- The Gliss Technique notes (vel 90-116) land within 1 dB of c21.
- Range-test bars 123-132, 235-242 and 168-184 before the main render. One check is inferred: that Opus multiplies two modulations into `Source/volume`. Sus RR shows one connection; the KS Master's CC11 connection is already there.
- After the fix, if the p solo at 123-128 is more than 5 dB under the other p solos (Bassoon 1 at 115: -48.5; Trumpet 1 at 51-66: -47.2), add `soft_trim_db {"p": 2}` to the harp's mix.json entry. That is a phrase-level row by printed dynamic.

## 2. Delivery: the three fff moments being level is right by the score. The ff bars sitting at the fff level is the real flaw in the shape. Three ride rows fix it (measured, simulated)

**The score.** Bars 223 (qn 888), 263 (qn 1048) and 278 (qn 1108) are all printed fff tutti:
- 223 has crash fff and bass drum ff, and falls to f at 892;
- 263 has crash, then decresc at 1052;
- 278 has crash and bass drum, and holds into the final chord.

Nothing in the print ranks one over another. A 0.3 dB spread (final -7.6, 223 -7.8, 263 -7.9) is under the about 1 dB a listener can detect. It does not contradict the print, so I would not spend limiter on separating them (inferred).

**What is wrong (measured, mp3, windows inside the bar).** Several ff bars reach the fff level:
- bar 272 (ff, allargando) -8.1: 0.5 dB under the final chord;
- bars 147-148 (ff) -8.9 / -9.0;
- bars 199 / 202 (ff, coda 1) -9.1.

On the master the same bars sit 5.6 dB (272) and 5.1 dB (147-148) under the climaxes. The delivery ride's quiet lift raises them 5-6 dB, because their short-term loudness is lower than that of the fff passages, while the fff bars get 0-2 dB. The "loudest ff bar" in c21's check covers bars 1, 5, 94, 113, 131, 132 and 150 only, so it missed 272, 147-148 and 199-210.

**What I tested (all on the c21 master, same tools):**
- `DELIVER_TOP_RATIO=1.5`: bar 272 rises to equal the final chord (-7.6). Rejected.
- Raising the final row back to -3.0: +0.1 dB on the final chord, limiter 6.4 dB. Rejected.
- Variant v4, adopted below:

| | c21 delivered | v4 | goal |
|---|---|---|---|
| I / LRA / TP / p10 | -14.0 / 12.2 / -1.1 / -22.6 | -14.0 / 11.8 / -1.2 / -22.4 | -14 ±0.5 / about 12 / -1.0 / -23 or higher |
| limiter final / 223 / 263 / bar 91 | 5.7 / 4.2 / 3.8 / 3.4 | 5.9 / 4.4 / 4.0 / 3.6 | about 6 at most |
| final / 223 / 263 | -7.6 / -7.8 / -7.9 | -7.6 / -7.7 / -7.9 | |
| bar 272 / 148 / 150 | -8.1 / -8.9 / -9.6 | -10.4 / -10.1 / -9.5 | 1.5 dB or more under fff |
| loudest bar that is not fff | 272 at -8.1 | 277 at -8.6 (the cresc into 278), then 276 -8.9, 259 -9.2 | |
| 223 over 222 / 263 over 262 | +1.7 / +1.7 | +1.6 / +1.6 | |

**Fix.** Add these rows to the c21 block in `build/score_config.py`, written as the existing stab rows `[(a - 0.5, 0), (a, d), (b, d), (b + 0.5, 0)]`:
- -2.5 dB at 1080-1088 (bars 271-272);
- -1.5 dB at 584-596 (bars 147-149; it runs into the existing -2 row at 596-600, so the ramp does not rise into the sfp at 592);
- -1.5 dB at 792-840 (bars 199-210).

Keep the fff rows as they are. Keep `mix.json` deliver.ratio 1.8 and the 2:1 top ride.

**Master clip (measured).** The stems peak at 0.42 at most and are 24-bit. `00_Master.wav` is now 32-bit float (`render_cycle.py` wrote the stem sum), with peak 1.073. Nothing is lost, and the delivery sets its own gain, so the clip is not audible.
- To keep a 24-bit master under full scale without breaking "master = stem sum": have `render_cycle.py` always write the float stem sum as the master. It already does this when the master clips.
- A REAPER master fader at -2 dB would also work, but then the master would no longer equal the stem sum that `stem_fix.py` relies on.

## 3. The muted Trumpet 1 is now 2.8 dB under the cor anglais in their unison (measured)

**Where:** Cor anglais and Trumpet 1 con sordino, both printed p "dolce cantabile", qn 680-696 and 712-731 (bars 171-183).

**Evidence:**
- Over 20 unison note bodies (from onset +0.15 s to the end -0.1 s), Trumpet 1 minus cor anglais has a median of -2.8 dB (c20: -0.8).
- The cor anglais rose 1.6 dB at 680-696 and 1.4 dB at 712-731 on the "Sus MAX" row. Trumpet 1 is unchanged (-52.4 / -49.6).
- Per note the gap runs from +3.9 to -7.0 dB; 11 of 20 notes are 2.5 dB or more under.

**What a listener hears (inferred).** A doubled melody needs both colours. At -3 to -7 dB the muted trumpet blurs into the cor anglais' tone instead of colouring it.

**Fix (instrument side).**
- `build/score_config.py` c22 block: a cc_scale on Trumpet 1, `{"lane": "cc11", "k": 40.0, "pts": [(679.7, 0), (679.73, 2.5), (731.0, 2.5), (731.03, 0)]}`.
- On the 1TP KS Master, CC11 drives only the Global Group volume (c18: 40 log10), so the layer the printed p selects stays the same.
- The CC11 lane there is 46-72, so +2.5 dB (x1.155) stays under 84.
- Target: median Trumpet 1 minus cor anglais within ±1.5 dB.

## 4. F2 in the violins (bars 67-82): the violas' and celli's mp espress. counter-lines swell over the mf tune in bars 73-74, 76 and 79 (measured)

**Where:**
- Violas: qn 288-296 and 300-304.
- Violoncellos: qn 300-304 and 312-316.

**Printed:** Violins I/II mf cantabile, unison. Violas "arco, unis., espress." mp. Celli "arco, espress." mp. Both counter-lines have hairpins in bars 73-76.

**Evidence.** Each stem against Violins I + II summed, per bar, c21 (c20 is within 0.5 dB):

| bar | 71 | 72 | 73 | 74 | 75 | 76 | 79 |
|---|---|---|---|---|---|---|---|
| Violas | -3.0 | -2.6 | -0.4 | **+2.0** | -5.8 | **+1.3** | -6.2 |
| Celli | -2.6 | -0.8 | -5.1 | -1.6 | -6.3 | **+3.2** | +0.7 |

In bars 67-69 the counter-lines sit 5-10 dB under the tune. A counter-line printed one level lower should stay 2-4 dB under the tune at the top of its hairpin (inferred, Adler / Rimsky-Korsakov on balance of melody and inner parts). This is not new; c21 B measured the celli overall at -1.8 dB and suggested -1.5 dB at 296-316.

**Fix (instrument side; CC11 crossfades layers and sets the level on the string KS Masters):**
- `cc_scale` -3 dB on Violas at 287.7-296.3 and 299.7-304.3.
- `cc_scale` -3 dB on Violoncellos at 299.7-304.3 and 311.7-316.3.
- Use the same k as c21's basses row (47, soft strings), and check it on the stems: c21 B measured celli at 0.27-0.47 dB per CC11 unit, so about -8 units.
- Leave bars 67-72 alone.

## 5. Bar 223 low end: the "fall" from bar 222 is a measurement artefact. The low end now rises at the arrival (measured)

**Evidence.**
- `cycles/c21/actor_scripts/meas21.py` `band()` returns sum(|FFT|²) / N. That is energy, not power, so it grows with window length.
- The two windows are 884.5-887.8 (3.3 s at the bar-222 tempo) and 888.05-889.5 (1.45 s). That biases the comparison by 10 log10(3.3/1.45), about 3.6 dB, against bar 223.
- Corrected to power (/N²):

| 30-90 Hz | c20 | c21 |
|---|---|---|
| Double basses, bar 222 -> bar 223 | -36.7 -> -40.8 (-4.2) | -36.7 -> -36.8 (-0.1) |
| master, bar 222 -> bar 223 | -36.9 -> -39.7 (-2.7) | -36.9 -> -35.8 (+1.1) |

- The master's 30-60 Hz band rises about 25 dB at 223: the basses' low C (32.7 Hz) arrives there. The 90-150 Hz band rises 8 dB.
- The bass drum sits 10 dB under the master's 90-150 Hz band at the stroke, so it does not boom.
- The master's 20-100 Hz share (-12.6 dB) is inside the reference range (Dvořák -21.7, Brahms 1/ii -8.5, Brahms 4/ii -7.9).

**Fix:**
- No level change at 223. c21's +4 dB Tremolo region gain on the basses did its job.
- Correct `band()` in the next actor's measuring script (divide by N², or use equal-length windows).
- The basses' stroke p90 at 816-840 uses equal 20 ms windows, so its 3.1 dB shortfall against c19 is real. That is A's to judge; I add nothing to it.

## 6. The trumpets' mf off-beats in bars 159-166 are now level with Horn 3's f off-beats (measured; size of fix inferred)

**Where:** Trumpets 1-3 and Horn 3, qn 636-664. Both are staccato on the same off-beats; the trumpets are printed mf, Horn 3 f.

**Evidence:**
- Note-peak medians: Horn 3 -35.5, Trumpet 1 -37.3, Trumpet 2 -37.4, Trumpet 3 -41.6 dB.
- RMS over the notes: Horn 3 -37.6, Trumpet 1 -38.1.
- Trumpet 1 is 0.5-1.8 dB under Horn 3. One printed level should be about 3 dB, and the trumpet's 2-4 kHz brightness makes it read louder still (inferred).
- c21 moved these notes by +8 velocity and the CC park together (+11 dB), so the velocity slope alone is not separated.

**Fix:**
- `INSTR_POST["vel_add"]` on Trumpets 1-2: +8 -> +4 at 632.9-662.5. My estimate is about 0.5 dB per velocity step on "Stac DblTng RRx9" (inferred), which gives about -2 dB.
- Keep the park, and keep Trumpet 3.
- Target: Trumpet 1 note peaks 2.5-3.5 dB under Horn 3.

## Other checks (no finding)

- **Solos over their accompaniment (measured, RMS over the passage):**
  - Trumpet 1 at 51-66 is 5.4 dB over the next stem (Clarinet 2).
  - Bassoon 1 at bar 115 is 8-9 dB over the next stems.
  - The F1 theme in the basses at 27-34 is the loudest stem.
  - Theme B at 211-218: Trumpets 1-2 lead by 5-9 dB in bars 212-215, but only 2 dB in bar 216 (dim. on a tie).
  - The chorale at 255-264: Trumpet 1 (a2) carries the most 1-4 kHz energy of any stem in 259-261 (-30.6 against Trombone 1 -34.0 and Violins I -33.0), although by RMS Horn 1 and Trombone 1 are 2 dB over it.
- **Arrival and ending (measured):**
  - At bar 223: brass group -14.2, strings -21, timpani -36.1, crash and bass drum -30.1.
  - At bar 278: brass -21..-24, violins -17.7, timpani -30.9.
  - Timpani and low brass do not cover. The crash adds +2.3 dB (223), +5.3 dB (263) and +2.6 dB (278) to the master's 5-12 kHz band: heard, not dominant.
- **Dynamic mapping across families (measured, median per printed dynamic):**
  - At p, strings, winds and brass sit within -46.8..-52.9 dB, except Tuba -56.6 and the second players.
  - From p to ff, strings rise 12, winds 9-12 and brass 14-20 dB. The order (brass widest, winds narrowest) matches real instruments (inferred).
  - Woodwinds that come out 12-20 dB under brass in ff tutti (my scan: Oboe 1, Bassoon 1 and Flute 2 in about 30 bars) are doublings, which is normal in a tutti (Rimsky-Korsakov).
- **The other movements' findings:**
  - Movement II's 2:1 top ride: in place. 1.5:1 made things worse here (finding 2).
  - Movement II's limiter 6.0-6.6 dB: ours is 5.7-5.9.
  - Bow pieces on exposed sections, the Horn 1 A4-G#4 legato hole, the String Leg Slur swell, and wind overlap rows: articulation and timing, not my lens. Not checked.

**Do not touch:**
- the fff ride rows at 222-223 and the final chord (raising them buys 0.1 dB for 0.5 dB more limiter);
- the 2:1 top ride and ratio 1.8;
- the loudness loop;
- the bass drum +6 dB and the basses' Tremolo region +4 dB at 223;
- c21's inner-line lifts (clarinets 151-170, Oboe 1 at 328-344, Horns 3-4 at 843.6-856.7, trombones at 792-816);
- the cor anglais "Sus MAX" row (fix the pair by raising Trumpet 1);
- the timpani and crash levels at 223 / 263 / 278;
- the harp's Harmonics and Gliss Technique rows (only the velocity-to-volume path is missing).
