# Cycle 8, critic C: holistic comparison (on the cycle 7 render)

Under review: `cycles/c07/render` (master and 27 stems) and `cycles/c07/metrics`, compared with `cycles/c00` (first mockup), `cycles/c02` (five cycles back) and the Dvorak 9/i Columbia reference. Also read: `build/parts.json`, `tools/score_to_parts.py`, `build/roles.json`, `build/mix.json`, `build/mockup-events.tsv`, and score pages 5 and 8. Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c08-C/` (`an1.py` to `an10.py`, using the c07-C `lib.py`). Levels are plain RMS dB, measured against score onsets (`sq`) on the parts.json tempo map.

## Where the render stands after seven cycles

- **c00 to c07.** The first mockup had heavy bass bloom: 63 Hz was +14.1 dB against 1 kHz (reference -6.2). It is now -2.7. In c00 the soft passages were not soft: bars 65-70 (pp/p) measured -27 to -30 dB and now measure -42 to -52.
- **Bar level against the loudest printed dynamic** (my `an9.py`):

  | Render | Correlation | Slope | Residual SD |
  |---|---|---|---|
  | c00 | 0.63 | 2.9 dB/step | 5.0 dB |
  | c02 | 0.89 | 4.5 dB/step | 3.2 dB |
  | c07 | 0.85 | 4.1 dB/step | 3.6 dB |

  The macro dynamics have been right since c02. Since then, the cycles have fixed entries, legato joins, balance, and timing. The large residuals left in c07 are bars 76-77, which sit inside the crescendo to ff, plus bars 47, 69 and 83, discussed below.
- **What still sounds made by a machine** sits at the scale of a phrase and a single note, not the bar:
  - Arrivals fade right after they land.
  - The peaks of crescendos sag.
  - The pulse never moves except where a tempo change is printed.
  - A solo is played by sixteen players.
  - The coda gets louder where it should recede.
  - The tutti has little low-mid weight.

## 1. Every crescendo arrival to f/ff fades within a beat, including the main climax (bar 61, all sections). Measured.

**Where:** qn 196 (bar 60), 204 (bar 61, Largamente ff, molto sostenuto, tenuto), 259/262 (bars 78-79). These are winds, strings and horns.

**What is wrong:** the `hpgain` ramp is supposed to hold to the next onset. The code sets `nx = min(onsets >= b2)`, which is the arrival note itself. The +3/+4 dB is therefore released from the arrival over `HP_REL` = 1 qn: the note lands and immediately falls back. That is the fp shape the c06 note set out to avoid.

**Evidence (measured):**
- 33 of the 37 `hpgain` spans in parts.json end on a note onset.
- On those arrival notes, the level from +0.1..0.4 s to qn+1.0..1.5 falls by a median of 2.2 dB. At the bar 61 climax:

  | Track | Fall (dB) |
  |---|---|
  | Fl1 | 6.3 |
  | Cb | 5.2 |
  | Vla | 4.4 |
  | Vln I | 4.2 |
  | Bn2 | 3.7 |
  | Ob1 | 3.1 |

  Vln II at qn 196 falls 5.6 dB, and Vc at 259 falls 4.4 dB.
- The Vln I tune at qn 204-206, per half beat: -24.8, -25.7, -29.6, -30.1, -30.1, and -32.8 by beat 4.
- The master peaks at -19.7 on the downbeat and settles about 2.5 dB lower. The melody therefore loses about 3-5 dB of margin within its own arrival note.
- The printed marks are ff, *molto sostenuto* and tenuto: the note should bloom and hold.

**Fix:** in `tools/score_to_parts.py`, where the `hpgain` parts are added (about line 1196):
- Set `nx` to the first onset strictly after the arrival note: `min(n["qn"] for n in ns if n["qn"] > b2 + 0.05)`, capped at `b2 + 4.0`. Keep `HP_REL = 1.0` after that point.
- Also remove the CC11 decay after the arrival on tenuto and *molto sostenuto* notes at ff. Vln I goes 119, 118, 117, 116, 115 within 0.5 qn of qn 204. Hold the arrival value minus 1 CC to the note end. The sf rule at qn 212 is a separate case and keeps its fall.
- This changes the c06 "hpgain release 1 qn" do-not-touch item only in where the release starts, not in its length.

**Check:** the arrival notes at 196/204/259/262 should fall no more than 1.5 dB over their first 1.5 qn, and the Vln I margin at bar 61 should stay at +4 dB or more.

## 2. Crescendo peaks sag at the most exposed melodic moments. Measured.

**Where:**
- Bar 27, Vln I/II/Vc, qn 78-82: the first statement of the violin theme, rising to its mf high point.
- Ob1 bars 19-20 (qn 54-57).
- Fl1 bars 42-43 (qn 126-128).
- Ob1/Vla/Bn2 bar 47 (qn 146-148): the C sharp 7 goal of the 45-47 group.

**What is wrong:** the note on which a crescendo arrives sounds softer than the note before it. A listener hears the phrase collapse just before its peak.

**Evidence (measured):**
- Across all 75 crescendo hairpins, the median rise is +4.2 dB. The 78-82 crescendo is the worst: Vln I -4.9 dB and Vln II -6.8 dB (start of the hairpin to its end).
- Vln I per note in bar 27:

  | qn | Level (dB) |
  |---|---|
  | 78 | -42.6 |
  | 79.5 | -39.5 |
  | 80 (F5, 2 beats) | -46.6 |
  | 82 (B flat 5, the mf arrival) | -42.0 |

  The cause: CC11 rises only from 66 to 72 over the crescendo (mp to mf, about +2 dB on the curve in LEARNINGS), while the long Leg BC MAX note at qn 80 decays 4.6 dB after its bow-change bump.
- 7 of the 26 "<>" swells have the goal 1.5 dB or more under the beat before it:

  | Swell | Goal vs beat before (dB) | Cause |
  |---|---|---|
  | Fl1, goal qn 128 | -5.4 | |
  | Ob1, goal qn 57 (Ab4, Leg Slur goal) | -5.2 | |
  | Ob1, goal qn 148 | -4.9 | The goal is a re-attack of the same pitch on Sus MAX at velocity 73, after the Leg Slur note at the same CC |
  | Bn2, goal qn 148 | -2.0 | |
  | Vla, goal qn 148 | -1.9 | |
  | Vc, goal qn 82 | -1.8 | |
  | Ob1, goal qn 45 | -1.6 | |

- In the bar table, bar 47 is printed mf and measures -43.0, the level of the p bars around it (residual -9.6 dB).

**Fix:** in `score_to_parts.py`:
- (a) For a crescendo ending on a note onset, reach the target CC 0.25 qn before the goal and hold it until goal + max(0.5 qn, 25% of the following decrescendo) before the decrescendo starts. This applies only to "<>" pairs (`hairpins_and_marks` / `base_points`).
- (b) Give every crescendo whose target is mp or mf a minimum rise of 12 CC, measured from the level at the hairpin start.
- (c) Same-pitch wind re-attacks on Sus MAX at a hairpin goal get velocity 100 or more, the c07 re-tongue rule.
- (d) Add a `goal_db` vol_db part: +2 dB on the goal note (0.25 qn ramp in, released over the decrescendo). If (a)-(d) are not done this cycle, use `build/note_trims.json` instead: Vln I 80 +3 / 82 +2, Vln II 80 +3, Ob1 57 +4, Ob1 148 +5, Fl1 129 +3, 129.5 +3.

**Check:** every goal note is at least as loud as the beat before it, and the 78-82 crescendo rises 3 dB or more in Vln I/II.

## 3. The pulse is metronomic: no breathing at the printed breath marks or at phrase seams. Tempo map measured; effect inferred.

**Where:** the whole movement. The longest stretches are bars 1-35 at a constant 52 (34 bars), 37-47 at 60, and 65-78 at 52.

**What is wrong:** the tempo map has 288 points. All of them come from the printed rit./allargando steps, plus the two caesuras at qn 204 and 268. Phrase endings and solo breath marks get no time.
- Breath marks in solo melodies currently only shorten the note: Hn1 qn 29 (bar 10, the horn theme), Fl1 qn 124 (bar 41), CA qn 164 (bar 50), Cl1 qn 286 (bar 87).
- In a real Adagio, the conductor waits for the solo wind to breathe, and new phrases start after a small comma.
- This is the most general difference between this render and a recording. The brief allows it ("breath before a breath mark"). It is inferred, because no tool here can hear the difference.

**Fix:** extend `CAESURA` in `score_to_parts.py`. `add_caesuras` already slows the 0.25 qn before each point, and `qn_before` already converts the leads correctly.
- Solo breath marks: `{29.0: 0.12, 124.0: 0.12, 164.0: 0.10, 286.0: 0.10}`.
- Phrase seams with an upbeat or new entry: `{42.0: 0.08, 48.0: 0.10 (solo violin entry), 66.0: 0.10, 140.0: 0.08, 171.0: 0.10, 237.0: 0.10}`.
- Keep each value at 0.12 s or less. Together they add about 1 s to a 346 s movement.
- Optionally add a 3% slower last beat on the cadence bars 14, 22 and 30, as an `\mt`-like step in `smooth_tempo`, never more than 4%.
- Rebuild all tracks with `--midi-only` (the tempo map moves items).

**Check:** confirm that the attack gate still passes, and that the entry leads after each new caesura are 0.17 s or less (the c07 C #4 issue).

## 4. The coda gets louder at bar 89, where everything is pp/ppp under a rit. and a morendo. Measured.

**Where:** bars 87-92 (qn 286-304); Vc, Vln I, Vla.

**What is wrong:** the bar levels are 87 -42.9, 88 -44.3, **89 -40.3**, 90 -40.7, 91 -43.2, 92 -47.2. The last bars of the movement are louder than bar 87.

**Evidence (measured):**
- Vc rises from -57 to -50/-51 dB at qn 292. The cause is a new Leg BC MAX note on A flat 2 at velocity 124 (the legato-target rule), with a pp mark.
- Vln I enters at qn 292 on its 12-beat C5 at -46 to -47 dB, 4-5 dB over Vln II/Vla/Cb (-51 to -53).
- Vla also takes Leg BC at velocity 124 at qn 289 and 292.
- The printed ending (page 8): every string is pp in bar 89, decrescendos to ppp in 91-92, and the clarinet is marked *morendo*.

**Fix:**
- In `score_to_parts.py`, do not use Leg BC velocity 124 for soft (CC 40 or less) string notes at or after qn 280. Use the Sus MAX entry rule at velocity 60-70, or velocity 90 if the legato join must stay.
- roles.json: Violoncellos [292, 304, -4]; Violins I [292, 304, -3]; Violas [289, 304, -2].

**Check:** each of bars 89-92 is at or below bar 88, and the bar 92 chord remains audible (above -50 dB through the fermata).

## 5. The Vln I "solo, senza sord." (bars 17-22) is still a 16-player section, 6 dB over the oboe that answers it. Level measured, timbre inferred.

**Where:** qn 48-65, Vln I (solo) against Ob1 (bars 15-16 and 19-20).

**What is wrong:** this is the only printed string solo, set in a dialogue with the solo oboe. The section patch plus `SOLO_BOOST` +8 CC makes it the loudest line in the B section:
- Vln I: -40.0 / -39.3 dB in bars 17-18.
- Ob1: -46.5 / -45.6 in bars 19-20.
- The other strings: 9-15 dB under.

A real solo violin over muted strings would sit about level with the oboe and sound thinner and closer. Critic A raised this in c07 (#4); it was deferred for memory.

**Fix:**
- Interim (no new patch): in `score_to_parts.py`, do not apply `SOLO_BOOST` to Violins I for the "solo" text at qn 48. Add roles.json Violins I [48, 65, -5], and CC1 +10 over the same span for a narrower, more vibrato-led sound. That brings it to about Ob1 + 1 dB.
- Full fix, when the session has memory headroom after the restart rule: append a "Violins I solo" track using the 1st Violins Divisi Leg Slur MAX patch (`/Volumes/MAC DRIVE/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/1st Violins Divisi/04 Legato Slur + Port/`). Give it Close mic only, at the Vln I seat, and silence Vln I over qn 48-65.

**Check:** Vln I in bars 17-18 is within ±1.5 dB of Ob1 in bars 19-20.

## 6. The tutti climaxes are thin at 90-350 Hz compared with the reference. Measured against the reference; cause partly inferred.

**Where:** bars 60-62 and 79-80.

**What is wrong:** in the loudest 15% of frames, the c07 mix measures (dB against 1 kHz):

| Band | c07 | Reference | c00 | c02 |
|---|---|---|---|---|
| 125 Hz | -9.8 | -0.7 | +0.7 | -5.5 |
| 250 Hz | -6.1 | -2.5 | | |

The 125 Hz band has fallen in every cycle. In the soft frames, c07 is already at or above the reference (125 Hz -4.4 against -6.1). The deficit is specific to f/ff.

**Evidence (measured, per stem in bars 60-62):**
- Vc supplies most of the 250 Hz band (13.3 of the master's 21.3 dB). Yet Vc carries `dyn_trim_db` f -3 / ff -4.5, plus roles -6 (188-204, opening by end_ramp 4) and -5/-1 (250-274).
- At bars 79-80 the score leaves the 90-180 Hz octave to the Cb second harmonic and the timpani (Vc on A flat 3 and above, Cb on D flat 2). Part of the gap is the voicing and cannot be fixed by mixing (inferred).
- The cello cuts date from c01-c02, when the celli were loudest in 26 bars. That problem is gone: the melody margins are now +4 to +6 dB.

**Fix:** in mix.json, Violoncellos `dyn_trim_db` ff -4.5 → -2.5 and f -3 → -2. In roles.json, Vc [250,262,-5] → -3. Keep the Cb and Cbn settings.

**Check:** the 125/250 Hz loud-frame bands rise by 2 dB or more, and the Vln I margin over Vc stays at +3 dB or more at bars 57-62 and 79-80.

**Do not touch:**
- The macro dynamic scheme: soft trims, ff/fff CC, and the timp roll table. The bar-level fit has been r 0.85-0.89 since c02.
- The pre-roll and the compression gate.
- `qn_before` leads and the existing caesuras at 204/268.
- The c07 legato leads and wind portato joins.
- The pitch trims.
- The Cb 40-90 Hz cut and the seats and widths. Master correlation is 0.52 against the reference's 0.55, and side/mid is -4.9 against -5.3 dB.
- The fermata hold.
