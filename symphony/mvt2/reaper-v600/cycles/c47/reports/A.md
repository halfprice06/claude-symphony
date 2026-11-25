# Cycle 47, critic A (articulation and phrasing), on the c46 render

## Sources and method

- **Render and data.** `cycles/c46/render/` (dry stems 01-32, returns 33-36, `00_Master.wav`) and `cycles/c46/rendered_build/parts.json`, which equals `build/parts.json`. Seconds come from the parts.json tempo map (`tools/pcx.py` `TM`); the stems are on score time.
- **Measures.**
  - Legato joins (the joins `pcx.legato_joins` finds) on 50 ms RMS of the stem. Hole = the minimum over [moved onset − 0.05 s, score onset + 0.3 s], below the lower of two levels: the previous note's body (up to 0.35 s before the moved onset) and the new note's body (from +0.25 s).
  - Overshoot = the 200 ms peak minus the louder body.
  - `tools/pcx.py` for S2; `cycles/c44/actor_scripts/rbdip44.py` for re-bow dips; `cycles/c45/actor_scripts/s1check44.py` for S1.
  - 2-5 kHz over the first 80 ms against the body, for accents.
  - Folded 100-300 Hz and centroid autocorrelation at 3.95 s, for the final chord.
- **Fill simulations.** Fill changes were simulated by multiplying the c46 dry stems by the difference of the volume-envelope shapes, using the formula of `score_to_parts.py` (early-fill code near line 4333). This is exact for the dry stem because the envelope acts after Opus. The returns were not re-simulated; they sit about 15 dB under the dry stems.
- **Scratch.** `/private/tmp/claude-501/mockup-loop/mvt2-c47-A/`, deleted at the end.

## Manual notes (MANUAL-READING c47 / A: group A6, May 2021 HO manual PDF pp. 68-71, Hollywood Harp, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| p.68: the harp library's mics are set up for a solo instrument (vintage close and mid alternatives instead of surround). Maestro patches choose articulations by velocity, or by CC1 in the "MOD" patches. A KS Master exists. | Harp (`01 Maestro Patches/Harp Sus RR.oib`) and Harp harmonics (`02 Individual Articulation Patches/Harp Harmonics.oib`). | Yes. No MOD patch, no CC1 sent, CC11 held at 110 (kit LEARNINGS §3: the harp's dynamic is in velocity). |
| p.69: the plain Maestro patch maps velocity to articulation: Double Hit at 1-60, Gliss Technique at 61-102, Nail Picks at 103-127. Sustain RR alternates Pluck Long (RR1) and Thumb Pick (RR2) at velocity 1-123, five levels each, and plays Nail Pick at 124-127. | The harp's 158 notes. | Yes. The track uses Sus RR (not Maestro) at v44-104, so no note reaches a nail pick (measured in parts.json). The `.oib` layer edges are Pluck 57/85/107/117 and Thumb 42/70/97/115. So at v71-85 alternate notes change both technique and layer, one source of the per-pitch spread in kit LEARNINGS §9 (inferred; no change proposed). |
| p.70: Harmonics have no fundamental, only upper partials, and two dynamic levels by velocity. CC11 and velocity set loudness. Pluck has five levels; Thumb Pick is more guitar-like. | The three coda harmonics at qn 274, 275.5, 276 ("dolce, harm., sound 8va"). | Yes. The `.oib` puts the loud layer at v72-127, and the notes play v58/58/70, so all three stay on the soft layer and sound alike. They sound at A flat 4, C5, E flat 5 as printed: spectral peaks at 828/522/622 Hz, where the A flat 4 shows its second partial, as the manual's missing fundamental predicts. |
| p.71: Repetition Rep lets earlier notes ring when a pitch is struck again. | The repeated pitches in the bars 53-56 broken chords (D flat 4 at 172.33, 173, 173.67). | Not needed (inferred). Sus RR alternates its takes, the notes ring by `HARP_RING_S`, and no machine-gun effect shows: the broadband peaks of those notes stay within about 6 dB, with the metric steps as planned. |
| pp.70-71: FX and Gliss key maps. | None (v600 has no glissandi). | n/a |
| (Not in A6; harp practice) Rolled chords and "R.H. étouffez". | Every printed arpeggio (bars 7-14, 71-78) and the damping at qn 274. | Yes. Rolls go bottom-up at 40 ms per note (soft) and 30 ms (f, bar 78). At 274 the plucked notes of 273/273.5 stop while the low A flat 1/E flat 2 ring on, as printed (measured). |

MANUAL-GAPS:
- #5 (Leg Slur Exp on the espr./dolce wind solos) is the library's other route for the oboe's transition sag in finding 1. It changes transition timing, so every lead on that track would need a refit. Not for the last cycle.
- #2, #8 and #9 also need new rows and refits. Not for the last cycle.

## Findings, ranked by what Dan will hear

### 1. Exposed solo legato joins drop 6-12 dB because their fills start after the transition (measured; fix simulated on the stems)

**Where.**
- Oboe 1: bar 16 (qn 47) and the "dolce espr." head in bars 44-46 (142-146).
- Flute 1: bar 39 (113.5).
- Bass clarinet: bar 31 (92, the solo's second join).
- Celli: bar 45 (140, with the oboe's head) and bars 74-75 (240, 248.5, "cantabile").

**What is wrong (measured).** Median hole per track:

| track | median hole | notes |
|---|---|---|
| Oboe 1 | 4.2 dB | 12 of 32 joins ≥ 6 dB, 3 ≥ 9 dB |
| Flute 1 | 3.0 dB | |
| cor anglais | 3.1 dB | |
| Clarinet 1 | 2.3 dB | |
| Violin I solo | 2.1 dB | |
| Horn 1 | 1.9 dB | |

The exposed joins:
- Oboe 1 143: 9.4 dB. The stem falls from −40 to −56 dB for 0.1 s, sits at −51 for 0.15 s, and reaches −45 only at +0.12 s.
- Oboe 1 146: 7.1 dB; 142: 6.4; 47: 6.3.
- Flute 1 113.5: 6.7 dB.
- Bass clarinet 92: 6.3 dB (11 dB in 10 ms frames).
- Celli 140: 12.2 dB, with a second sag at +0.18 s; 240: 9.1; 248.5: 7.3.

Where these instruments lead, the master dips at the joins:

| join | master dip |
|---|---|
| Oboe 1 143 | 3.9 dB |
| Oboe 1 146 | 3.6 dB |
| celli 140 | 4.0 dB |
| Flute 1 113.5 | 3.1 dB |
| bass clarinet 92 | 7.6 dB (a 50 ms notch) |

The oboe is the loudest stem in bars 45-47 by 5-6 dB, so its line sounds note by note rather than slurred (the inferred effect).

**Cause (read in parts.json and the early-fill code).** A fill with `pre_s` 0, or a plain number, reaches full level at the score onset. These targets are led 0.06-0.26 s, so the transition sag starts before the fill, while the previous note's fill is still releasing:
- Oboe 1: vol_db 7.1 dB at 142.875 → 3.7 at 142.98 → 8.9 at 143.0, with the moved onset at 142.848.
- Bass clarinet: 5.65 dB at 91.87 → 1.17 at 91.95 → 4.33 at 92.0, with the moved onset at 91.919.

250 of the 300 `early_fills.json` entries start more than 50 ms after their note's moved onset. The c46 +0.04 s Oboe 1 leads pushed six transitions further ahead of their fills (142: hole 5.1 → 6.4 dB).

This also settles the open Oboe 1 S2 item. The pitch crossovers are on time (142 +16 ms, 140 −26 ms, 146 −22 ms). pcX reads the slow recovery from the hole as lateness (142 +208 ms, median +45). More lead cannot fix it.

**Fix (`build/early_fills.json`; seconds re the score onset; level only).** Every track that changes needs `--midi-only` (no Opus state change), or the change can be applied by stem fix.

| track | key | now | new |
|---|---|---|---|
| Oboe 1 | "47" | 4 | {"db": 4.0, "pre_s": 0.14, "hold_s": 0.08} |
| Oboe 1 | "142" | 4 | {"db": 4.0, "pre_s": 0.06, "hold_s": 0.08} |
| Oboe 1 | "142.5" | {5, 0, 0.28} | {"db": 3.0, "pre_s": 0.0, "hold_s": 0.15} |
| Oboe 1 | "143" | {5.5, 0, 0.1} | {"db": 6.0, "pre_s": 0.12, "hold_s": 0.10} |
| Oboe 1 | "146" | none | {"db": 4.6, "pre_s": 0.09, "hold_s": 0.10} |
| Violoncellos | "140" | {4.3, 0, 0.25} | {"db": 8.0, "pre_s": 0.18, "hold_s": 0.32} |
| Violoncellos | "240" | none | {"db": 6.6, "pre_s": 0.26, "hold_s": 0.19} |
| Violoncellos | "248.5" | none | {"db": 4.8, "pre_s": 0.13, "hold_s": 0.14} |
| Flute 1 | "113.5" | none | {"db": 4.2, "pre_s": 0.0, "hold_s": 0.17} |
| Bass clarinet | "92" | {3.0, 0, 0.1} | {"db": 4.0, "pre_s": 0.09, "hold_s": 0.10} |

Rule used: `pre_s` = lead − 0.04 s, so the fill is full just after the moved onset; hold to the measured end of the hole. Add the onsets to `_auto` as hand entries so a later `auto_fills.py` run does not resize them.

**Simulated result (all ten together).**

| track | onset | stem hole (dB) | master dip (dB) |
|---|---|---|---|
| Oboe 1 | 47 | 6.3 → 3.7 | 2.4 → 1.9 |
| Oboe 1 | 142 | 6.4 → 4.7 | 1.7 → 3.0 (the one cost) |
| Oboe 1 | 142.5 | 4.9 → 4.3 | 1.9 → 1.6 |
| Oboe 1 | 143 | 9.4 → 1.8 | 3.9 → 1.9 |
| Oboe 1 | 146 | 7.1 → 2.5 | 3.6 → 2.5 |
| Violoncellos | 140 | 12.2 → 6.5 | 4.0 → 2.5 |
| Violoncellos | 240 | 9.1 → 3.2 | 3.5 → 3.6 |
| Violoncellos | 248.5 | 7.3 → 2.5 | 2.0 → 1.2 |
| Flute 1 | 113.5 | 6.7 → 3.7 | 3.1 → 2.0 |
| Bass clarinet | 92 | 6.3 → 2.5 | 7.6 → 5.2 |

- The 200 ms overshoot over the louder body stays at +2.0 dB or less on all ten; Oboe 1 143 goes from +3.1 to +1.3.
- The 142/142.5/143 entries only work as a set. With 143 changed alone, 143 reaches only 4.0 dB and overshoots +4.1.
- After the render, re-measure the listed joins by the method above. Targets: stem hole ≤ 5 dB, overshoot ≤ 2 dB.

**Not proposed.**
- The same holes in the tutti (Oboe 1 193.5-200 and 269.5-271, 7.5-10 dB on the stem), and Flute 1 129-133.5 and cor anglais 97/108/131.5. Fills there moved the master by 0.4 dB or less (masked), so the last cycle gains nothing from them.
- A wholesale `auto_fills.py` run. Its c46 plan has 125 changes, and its 200 ms oboe window reads 143 as 5.2 dB, so it sizes these fills too small.
- A generic "start every fill at the moved onset" rule. Simulated, it cut Oboe 1's joins ≥ 6 dB only from 12 to 8, and raised celli overshoots over 2.5 dB from 15 to 26.

### 2. Oboe 1's low notes sit 6-8 dB under its dolce espr. phrase in bars 44-46 (measured; fix is level only, effect inferred as linear)

**Where.** Oboe 1, qn 139 (the A flat 4 pickup, "p, dolce espr.") and 145 (the A 4 eighth).

**What is wrong.** Note bodies (median 50 ms RMS over the middle 60 % of each note):

| qn | 139 | 140 | 142 | 142.5 | 143 | 144 | 145 | 145.5 | 146 | 148 |
|---|---|---|---|---|---|---|---|---|---|---|
| dB | −53 | −44 | −47 | −49 | −45 | −46 | −52 | −47 | −42 | −38 |

- p is printed constant until the crescendo at 146.
- 139 is 7.9 dB and 145 is 6.2 dB under the median of their neighbours.
- Across the part, the oboe's A flat 4 measures 8-11 dB under its neighbours (139, 188, 271) and its long D flat 5 5-7 dB over: the samples' per-pitch level (kit LEARNINGS §6).
- The existing trim on 139 (+2 dB) is too small, and 145 has none.
- Heard as: a weak pickup, then an accent on the downbeat 140, and a hole on the eighth before the crescendo (inferred).

**Fix.**
- `build/note_trims.json` "Oboe 1": "139": 2 → 6, and add "145": 5.
- `build/score_config.py`: `NOTE_TRIM_RAMP_S["Oboe 1"]` add `139.0: 0.1, 145.0: 0.1`. The default 0.6 s ramp would never reach full level on the 0.55 s eighth.
- Expected: 139 about 4 dB under the 140 note (a pickup), and 145 within about 1 dB of its neighbours.
- Leave 188 (−11 dB): the first note of bar 57, doubled by Flute 1 and the violins, and masked.

### 3. Open item: the string lifts before the pickups (CAESURA_LIFT at 65, 77, 249) have nothing audible left to gain (measured); leave them as rendered

**Violins I 77.**
- The stem rises from −45 to −38 dB at score onset −0.15 s.
- Cause: early fill "77" {6.0, pre_s 0.18, hold 0.35} comes in at the moved onset together with the Leg BC transition bump, so it covers the 0.25 s CC11 fall.
- Simulated {3.0, 0.18, 0.25} and {2.0, 0.10, 0.25}: the bump is mostly the sample's own transition. The pickup's body dropped 3-4 dB and the master moved 1 dB or less.

**Violins I 249.** The stem dips 4.7 dB. The master does not dip, because violas, celli, basses and harp continue (master −38.9 dB against Violins I −44.4 over 249-250.5).

**Verdict.** What the listener hears at these seams is the c46 caesura's time and the bow change. Keep `CAESURA_LIFT` as it is: it costs nothing, and S3 falls at the breaths stay at 1.2 dB or less.

### 4. Open items that do not reach the listener (measured): Violas 249.5 and Horn 4 at qn 84; leave both

**Violas 249.5** (+55 ms by pcX, crossover +40 ms):
- These are inner p eighths at −49 dB under a −38.9 dB master. The neighbouring joins read 249.0 +142 and 250.0 +68 ms.
- The violas' join median is +7 ms with a robust SD of 67 ms, so +55 ms is inside the estimator's spread.
- C's `LEG_CAP_FRAC["Violas"] += [(249.0, 250.0, 0.55)]` is harmless but buys nothing audible. Skip it in the last cycle.

**Horn 4 qn 84** (7.6 s, pp):
- The stem dips 9 dB at +1.75..+2.75 s. Part of that is the role step at 85.75-86 (−5.2 dB); the rest is the sample.
- The horn sits 10-12 dB under the master there, and the master stays at −39..−42 dB with no dip.
- Inaudible.

## Checks that passed (measured; not findings)

- **Legato rows.** No two different pitches overlap more than 0.15 s, and no same-pitch overlap, on any legato row of the 32 tracks.
- **Keyswitches.** No keyswitch clash, and none lands less than 12 ms before its note.
- **Ties.** Only printed bow marks split tied notes: Violins I 295/298/301, the bar 66 down-bow at 223, and the timpani roll-to-stroke joins at 203 and 209.5.
- **S1.** 49 repeat points: median own-band dip 8.2 dB, master 3.7. The Violins II portato pairs of bars 15-21 dip 4.5-10.4 dB on the stem and 2.4-5.6 dB in the master.
- **S2.** Non-legato wind attacks, medians: Oboe 1 −8, Flute 1 +9, cor anglais −4, Clarinet 1 −8, bass clarinet +10, Horn 1 +22, Bassoon 1 +22 ms. Attack probe 0.
- **Accents (BRIEF 9).** Trombone 1 213 is +5.7 dB over its pickup's body, with 2-5 kHz attack −6.6 dB re its body and a master 2-5 kHz jump of −1.8 dB. 218 has a +3.8 dB front over its body at −9.2 dB. The slurred 215/215.5 transitions are brighter (+5 dB) but move the master's 2-5 kHz by at most +2.4 dB.
- **Bars 61-64.**
  - The molto sostenuto tenutos re-articulate 2.1/0.6/3.2 dB in the master at 206/208/210.
  - The bass trombone and tuba breathe at 208 as printed.
  - The strings' sf at 212 falls 15 dB over the first beat, then decrescendos evenly to p at 216.
- **Mutes.** Every CC15 change falls in a rest.
- **Final chord (BRIEF 8).** Master 100-300 Hz autocorrelation at 3.95 s is −0.17 and the centroid's is −0.12: no pulse. The step at 297 is the winds' printed release.
- **Re-bows.** 85 re-bow points, median dip 3.8 dB. The bass 4-soli pedal (bars 65-70) holds within ±2 dB except at 235.659, which dips 6 dB on the stem for 0.3 s. A test reshaping of that fill closed only the part before the bow change, so leave it ("change bow at will" is printed).

## Do not touch

- The c46 Oboe 1 leads (add no more lead; finding 1 fixes the fills instead).
- The 0.04 qn legato overlap.
- Trombone 1's Sus MAX accents, CC7 points and v112.
- The harp setup: Sus RR at v44-104, harmonics at v58-70 on the soft layer, rolls at 30-40 ms bottom-up, the étouffez at 274.
- The CC15 mute placement.
- The bars 61-64 tenutos, tremolos and sf shapes.
- The Violins II portato pairs (bars 15-21) and the violas' portato (bars 48-51).
- The final-chord and coda re-bow points and their fills.
- CAESURA_LIFT and the c46 caesuras.
