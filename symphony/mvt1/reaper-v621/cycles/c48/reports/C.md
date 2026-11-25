# Critic C, cycle 48: tempo, timing and transitions (render c47, score v621), Dan's note S2 first

## Manual notes (cycles 48-51 rule: pages chosen for this lens's top open problems, read in full: 2021 manual PDF pp. 91-92, 99, 101, 105, 109, 144; MANUAL-GAPS.md and DIGEST.md read)

| Manual (PDF page) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.91 | Sustain rows alternate up and down bow by round robin ("Bow Direction") | Every repeated same-pitch Sus MAX string note, most of all the basses' C2 eighths in the coda, bars 167-170 (qn 664-676) | No. The two bow samples differ: on-beat eighths come +58 ms late after a 9 dB deeper dip, off-beats come -38 ms early and 2.9 dB louder, identical in c46 and c47 (finding 2; measured). Nothing in the pipeline evens out the two strokes. |
| p.91-92 | Marcato Sustain adds a marcato sample to the sustain for "extra power at the start of the note" | Slow-swelling fresh string entries in fast music (Violins I pickups 464.5-478.5; celli 84 / 448 move to Sus Marc LITE in c48) | Partly. Used only on the two celli strokes. The Violins I f pickups on Leg Slur MAX v91 rise over about 200 ms (finding 3). |
| p.99 | Legato needs no gap between notes; "the first note of a phrase has no legato effect"; Legato Slur Staccato gives phrase-first notes "a slightly stronger attack" | Fresh entries on Leg rows (phrase-first notes play the slow first-note layer) | Followed as written. The StacSl row was tried in c47 only on repeated-pitch strokes (it swelled in on 4 of 6). It has not been tried on phrase-first pickups after rests (inferred candidate, finding 3). |
| p.101 | Brass Sustain: all 4 layers start together, Mod Wheel sets the level; Sustain Accent: velocity sets the attack | Brass entries and re-attacks | Brass attacks are fast. With the current leads they land early: entries -7 ms and re-attacks -12 ms against the beat median, Horn 3 entries -20 in both renders, Contrabassoon -27 / -20 (finding 1; measured). |
| p.105 | Brass legato: slur only with no gap and within an octave; trombone slide legato | Horn / trumpet Leg Slur MAX joins | Followed. Brass legato sits at -1 ms against the beat median (n 90). |
| p.109 | Woodwind Sustain: 3 layers on the Mod Wheel; "Sus Expressive" has "a slower attack" | Wind entries | Not used, and it should stay unused in the Allegro: wind entries already sit +6 ms after the beat median (inferred). |
| p.144 | True legato: velocity 50-60 gives a longer transition, 110-127 a tighter one, with no loudness change. CC5 "Time" belongs to the emulated Legato script, not to true legato | String and brass targets at v124; winds and the cello solo at the printed velocity (v60-70) | Followed. The soft slow-tempo joins (Clarinet 1 706, Bass clarinet 708 / 710, Cello solo 688, all v60-70) have the longest transitions, and that is where the band envelopes still read late (finding 4). CC5 is not a timing tool for these rows (read). |
| MANUAL-GAPS #6 (p.34, p.143, p.145) | Round-robin reset uses the Preferences controller (CC16), not CC36 | Repeatability, and which bow sample lands on the beat in finding 2 | Still open. Render-to-render repeatability is already high: 4.0% of 4710 unchanged note groups moved more than 30 ms between c46 and c47, but 11-13% on Violins I / II and Trumpet 1 (measured). A working reset at the start of the coda ostinato would set its bow parity (inferred). |
| MANUAL-GAPS #8 (p.144) | Slower transitions on cantabile lines | — | Closed in c42. Nothing new. |

## Method (measured)

Every score note group (chords once; re-bow, tremolo-split and restrike pieces left out by matching against the note onsets in `mockup-events.tsv`) on every delivered c47 stem was measured: 4886 groups, 4720 usable (rise 6 dB or more). The estimator is `tools/pcx.py` (`attack_pcx`: t50 / h10 mean on harmonic bands, with the previous pitch excluded). Timpani use the same t50 / h10 rule on broadband energy. Each group is timed against its score onset on `cycles/c47/rendered_build/parts.json`'s tempo map. Horn 1 is c46's stem, and the c47 Opus states match `rendered_build`.

- "Beat median": the median pcX of the other tracks on the same onset (3 or more).
- "Exposed": the stem within 10 dB of the master over the first 0.3 s.
- The same scan was run on c46 to separate stable timing from render variance. The median change on unchanged leads was 0 ms, with 4.0% of groups over 30 ms and 1.8% over 60 ms.

## Coordinator's question: where the attack centres sit, section by section (measured)

Exposed notes, pcX re the grid and the spread against each beat's median:

| Section (bars) | n | median re grid | per-beat robust SD | > 60 ms off | strings / winds / brass re grid |
|---|---|---|---|---|---|
| Lento 1-14 | 49 | +4 | 53 | 32% | +5 / -7 / +1 |
| Allegro 15-44 | 232 | +16 | 44 | 21% | +18 / +16 / +5 |
| Poco meno mosso 47-61 | 165 | +7 | 37 | 16% | +14 / +16 / +10 |
| animando, rit. 62-68 | 66 | +24 | 53 | 26% | +23 / +35 / +32 |
| closing 68-76 | 44 | +8 | 25 | 12% | -12 / +9 / +18 |
| development 77-112 | 339 | +12 | 39 | 22% | +10 / +20 / -8 |
| stringendo, a tempo 113-120 | 39 | +29 | 46 | 22% | +31 / — / +5 |
| allargando, sostenuto 121-126 | 13 | +4 | 26 | 25% | +15 / +1 / +3 |
| recap 127-144 | 170 | +15 | 39 | 20% | +13 / +24 / -0 |
| Poco meno mosso recap 147-164 | 155 | +7 | 40 | 18% | +3 / +14 / +4 |
| rit. 165-166 | 18 | +55 | 72 | 45% | +60 / — / -8 |
| coda Allegro 167-170 | 32 | +3 | 35 | 10% | +18 / — / +3 |
| Più lento, Tempo I 171-182 | 48 | +4 | 48 | 5% | -2 / +31 / -28 |

- The ensemble sits a constant +4..+29 ms after the grid. Nobody hears a constant offset.
- In the rit. 165-166 the whole group is late together (beat medians +72..+81 at 657-658). That reads as a slightly deeper rit., not as scatter.
- What remains is per-note scatter, and it is a string problem. Robust SD against the beat median, fast tempi: celli 53 ms, violas 52, Violins II 51, Violins I 47, basses 46 (21-28% of notes over 60 ms off). Brass, clarinets, timpani and low winds sit at 18-30 ms (0-11%).
- On tutti onsets (8 or more tracks) the median 10-90% spread is 81 ms. That is about a 32 ms SD, inside the 30-50 ms asynchrony reported for real ensembles (Rasch 1979; the comparison is inferred). So the goal is to remove the stable outliers, not to chase zero.
- **The string "attack centre" is not where pcX puts it.** In the fast music the strings' -10 dB point comes before the beat median (h10 -6..-25 ms) and their half-amplitude point after it (t50 +42..+51 ms). The median t50 - h10 split is 40-53 ms, and 21-30% of string attacks split by more than 80 ms. For winds, brass, timpani and harp the split is 6-22 ms.
  - On t50 alone, against each beat's median t50: strings +9..+11 ms, winds 0, brass -5..-12, harp -16.
  - By section, string t50 runs 15-45 ms after brass t50: Allegro +44 / +18, bars 113-120 +62 / +18, coda 167-170 +53 / +12.
  - This is what Dan heard: the front of a string note is on time, but its weight arrives 40-50 ms later. A lead cannot fix both at once. Leads fix the notes that are shifted as a whole (finding 1); early fills fix the notes that swell (finding 1b).

## Findings, ranked by what a listener would gain

### 1. About 150 stable per-note timing errors, most of them in the strings; plus three small family-level lead changes (S2; measured)

**Where.** All sections. Violoncellos 33 rows, Violins I 24, Violas 24, Violins II 15, basses 8, winds and horns the rest.

**What is wrong.** 311 exposed groups (stem within 10 dB of the master) are more than 50 ms off their reference in c47 and more than 40 ms off in the same direction in c46. The reference is the beat median, or +13 ms when the median is more than 40 ms from that value or missing. From these I kept the rows a lead can fix:
- Legato joins whose pitch crossover (`pcx.pair_window`) is off in the same direction by more than 40 ms in both renders.
- Entries and re-attacks whose t50 and h10 are both off in the same direction by more than 40 ms, so the whole attack is shifted, not swelling.

That leaves 150 rows, 64 late and 86 early. Examples:
- Violins II 396 -108 ms (Leg BC).
- Horn 1 411.5 -189.
- Violas 436 +117.
- Celli 266 +221 (crossover +80).
- Violins I 404 -89.
- Celli 556 -100.
- Violas 216 re-attack -136.
- Violins II 364 re-attack -210.
- Basses 32 / 89 re-attacks +104 / +90.
- Clarinet 1 422 entry +102 (exposed, rel -3.4 dB).
- Flute 1 432 entry +88 (rel -2.5 dB).

Family offsets that hold in both renders (pcX against the beat median, fast tempi):
- Contrabassoon entries -27 / -20 ms.
- Horn 3 entries -20 / -20 ms.
- Celli entries +19 / +21 ms and celli re-attacks +23 / +41 ms.
- Violins II tremolo -27 / -27 ms, but its leads vary from 0 to 0.15 s and its errors have both signs, so the per-onset rows cover it.

**Fix.**
(a) Add these deltas (seconds; a positive value means more lead, i.e. earlier) to the existing values in `build/leg_leads.json`, `build/entry_leads.json` and `build/retongue_leads.json` (create the key where none exists).
- Rule used: legato rows get 0.8 x min(pcX error, crossover error); entry and re-attack rows get 0.6 x the pcX error. Entries transfer more than 1:1 when the attack is a slow ramp (see 472.5 in finding 3). Every row is clamped to ±0.08 s.
- Alias rows are folded into their source (the f62 and stac aliases read the source's tables).
- Left out: celli 84 / 448 / 152 / 156 / 456 and Violas 372 (stroke rows under test) and Trumpets a2.
- Rerun `score_to_parts.py` and check the `LEAD WARNING` lines. The short notes at 270.25-271 and 606.6-606.9 will hit the caps, which is fine.

```
{"leg_leads":{"Bass clarinet":{"305.0":0.038},"Bassoon 1":{"413.0":0.044,"531.5":0.069,"575.5":0.068},"Clarinet 1":{"180.0":-0.054,"421.5":-0.04},"Cor anglais":{"395.0":0.05},"Flute 1":{"296.0":-0.036,"299.0":-0.034,"299.5":-0.049,"643.0":0.05},"Horn 1":{"411.5":-0.071,"418.0":-0.065},"Horn 2":{"249.0":0.046},"Horn 3":{"501.0":0.043,"657.0":0.047},"Oboe 1":{"579.0":-0.048},"Violas":{"76.0":0.069,"113.0":-0.042,"153.0":0.08,"182.0":-0.038,"428.0":0.041,"431.0":0.037,"434.0":0.056,"436.0":0.075,"595.5":0.054,"616.0":0.048,"650.5":-0.038,"710.0":-0.047},"Violins I":{"59.0":-0.034,"81.5":0.038,"93.0":0.041,"97.0":-0.059,"227.0":-0.039,"231.0":0.052,"243.5":-0.051,"245.0":-0.04,"268.0":-0.037,"373.0":-0.043,"404.0":-0.066,"477.0":-0.042,"540.0":-0.049,"620.0":-0.04,"654.0":-0.038,"658.0":0.08},"Violins II":{"28.0":-0.036,"257.5":-0.051,"373.5":-0.049,"396.0":-0.074,"563.0":-0.065,"657.0":0.046},"Violoncellos":{"8.0":-0.041,"97.0":0.047,"182.0":0.035,"204.0":-0.044,"265.5":0.052,"266.0":0.08,"276.0":0.036,"416.0":-0.04,"556.0":-0.07,"613.0":-0.043,"622.5":-0.054,"625.5":-0.042,"637.0":-0.046,"639.5":-0.045}},
 "entry_leads":{"Bass clarinet":{"8.0":-0.032,"372.0":-0.032,"432.5":0.08},"Bassoon 1":{"406.5":-0.039,"533.0":0.046},"Clarinet 1":{"212.0":0.043,"422.0":0.061,"506.5":0.056,"522.5":0.043},"Double basses":{"97.0":0.041,"132.0":-0.067},"Flute 1":{"377.0":0.047,"432.0":0.053},"Horn 1":{"408.0":-0.037,"416.0":-0.05,"620.0":-0.035},"Horn 3":{"317.0":-0.02},"Oboe 1":{"578.0":0.049},"Oboe 2":{"408.5":-0.08,"416.5":-0.059},"Trumpet 3":{"672.0":-0.032},"Violas":{"70.5":0.043,"407.5":0.046,"583.0":-0.052,"606.5":-0.075},"Violins I":{"74.5":-0.036,"106.5":-0.071,"146.5":0.04,"219.0":0.067,"380.5":0.035,"707.0":0.08},"Violins II":{"219.0":0.08,"223.25":-0.059,"290.0":0.08,"388.0":-0.043,"397.5":-0.046},"Violoncellos":{"336.5":-0.052,"350.5":0.042,"387.0":0.08,"419.0":0.043,"504.0":-0.062,"583.0":-0.065,"606.5":-0.06}},
 "retongue_leads":{"Bassoon 1":{"136.0":-0.039,"359.0":0.042},"Double basses":{"32.0":0.062,"89.0":0.054,"320.0":0.057,"332.0":0.08,"521.5":0.036,"571.5":-0.065},"Horn 2":{"47.0":-0.045,"232.0":-0.07},"Horn 3":{"156.0":-0.036},"Violas":{"136.0":0.036,"156.0":-0.08,"216.0":-0.08,"353.5":0.045,"606.625":-0.063,"606.75":-0.059,"606.875":-0.061,"662.0":0.08},"Violins I":{"44.0":0.055,"60.0":0.08,"270.25":-0.036,"270.75":-0.039,"271.0":-0.048,"628.0":-0.059},"Violins II":{"60.5":-0.08,"127.5":-0.039,"310.0":-0.055,"364.0":-0.08,"366.0":0.046,"379.0":-0.037},"Violoncellos":{"340.0":0.046,"341.5":0.053,"355.5":0.04,"514.0":-0.066,"516.5":-0.074,"517.0":-0.061,"517.5":-0.056,"518.75":-0.075,"528.5":0.052,"606.75":-0.033,"606.875":-0.057}}}
```

(b) Family leads in `build/score_config.py`. The ENTRY_LEAD_S tuples are (CC11 50 or less, CC11 over 80, CC11 51-80):
- Add `ENTRY_LEAD_S["Horn 3"] = (0.06, 0.03, 0.03)` (now on the brass default (0.06, 0.05)). The Horn 3 317 row above is already reduced to -0.02 to allow for this.
- Set `ENTRY_LEAD_S["Contrabassoon"] = (0.04, 0.04)` (was (0.06, 0.06)).
- Optional: `RETONGUE_LEAD_S["Violoncellos"]` 0.10 -> 0.12.

(c) Do not add lead to the "swell" rows. In these the h10 point is on time and only t50 is late, by 80 ms or more over the reference. There are 50 such rows, for example:
- Violins I 96 / 99 / 282 / 452 / 539 / 544 / 658.
- Celli 140 / 182 / 276 / 440 / 658.
- Violins II 376 / 379.5 / 650.
- Horn 2 220 / 240 / 245.
- Trombone 1 285 / 522.5.
- Cor anglais 395.
- Oboe 1 396.

They want short level fills from the moved onset: run `tools/auto_fills.py 47 cycles/c47/rendered_build/parts.json` limited to these onsets, or hand rows in `build/early_fills.json` of +2..+4 dB held to about +0.15 s. Fit each against an overshoot of at most +2 dB, as in c47 A #2.

**Check on c48.** Fast-tempo string robust SD against the beat median under 40 ms, and over 60 ms under 15%. Each changed row should end within ±40 ms of its reference.

### 2. Coda, bars 167-170: the basses' f eighth-note pedal limps. The two bow-direction samples alternate, so every off-beat is louder and early and every downbeat is weak and late (p.91; measured and simulated)

**Where.** Double basses qn 664-676, 25 repeated C2 eighths on Sus MAX, each with identical data: v83, lead 0, dur 0.47, the same `str_rep_dips`. The stem is 8-12 dB under the master.

**What is wrong.**
- Timing: on-beat eighths pcX +58 ms, off-beats -38 ms (the same in c46). So the off-beat-to-downbeat gap is about 335 ms and the downbeat-to-off-beat gap about 140 ms, against 238 ms each.
- Level: the off-beat notes peak 2.9 dB higher (band 34.4 vs 31.5), and the dip before each downbeat is 8.5 dB deeper (18.7 vs 27.2).
- The result is a long-short lilt with the weight on the off-beat, under the coda's ff tutti.
- No other repeated-note run shows this: the alternation is -26..+37 ms elsewhere. The same pitch at 520-525 is +8 ms. So it is this run's round-robin parity: the strong stroke falls on the off-beat.

**Fix.** Level shapes, which can also be applied as a stem fix. In `build/score_config.py`, for each beat q = 664, 665, ..., 675 add:
- on the beat: `LEVEL_SHAPES["Double basses"] += [[(q - 0.14, 0.0), (q - 0.06, 3.0), (q + 0.15, 3.0), (q + 0.25, 0.0)]]`;
- on the off-beat: `[(q + 0.5, 0.0), (q + 0.53, -1.5), (q + 0.8, -1.5), (q + 0.9, 0.0)]`.

Simulated on the c47 stem:
- downbeat pcX +58 -> +13 ms;
- the dip before the downbeat 18.7 -> 21.6;
- the off-beat peak 34.4 -> 32.9, so the off-beat excess goes from 2.9 to 1.7 dB.

To bring the off-beats onto the beat as well, add `retongue_leads.json` "Double basses" -0.03 s on the off-beats 664.5, 665.5, ..., 675.5. This is inferred, at about 1:1 transfer. When CC16 RR reset (MANUAL-GAPS #6) is tried, a reset just before 664 may move the strong stroke onto the downbeats instead; measure before keeping both changes.

### 3. Open timing items: the cello solo, and the letter-G Violins I pickups whose overshoot reversed (measured and simulated)

**Cello solo (pass-2 "Cello solo").**
- The c47 fills fixed two notes: 687 went from +118 to +2 ms, 694 from +102 to +18.
- 688 (G4 -> F4, Leg BC MAX v70, lead 0.10 s) is still +69 ms, as in c46.
  - The new pitch arrives on time: h10 +6 ms, crossover at about +0.02 s.
  - Then the line sags: the broadband stem goes from -33 to -37..-40 dB at +0.02..+0.10 s, a dip of 4.0 dB against the bodies on 100 ms windows.
  - Fix: append `[(687.99, 0.0), (688.03, 3.0), (688.17, 3.0), (688.27, 1.5), (688.34, 0.0)]` to `ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"]`.
  - Simulated: dip 4.0 -> 3.0 dB, peak over the louder body +0.3 dB, pcX +69 -> +15 ms. Leave the lead.
- The other solo notes sit at -48..+28 ms. 680 is -48: the solo's first note starts 0.2 s early after the fermata, so its front is in the silence. It can stay.

**Violins I 472.5 / 474.5 (bar 119, f pickups after rests, Leg Slur MAX v91).**
- c47 cut the extra entry lead from 0.10 / 0.09 to 0.05 / 0.04 s (total 0.16 / 0.15 -> 0.11 / 0.10 s). pcX went from -48 / -43 to +68 / +70 ms against beat medians of +26 / -6.
- The attack is a 200 ms ramp: in c47 the band rises from 13 at -0.10 s to 35 at +0.10 s. So pcX moves about 2.3 ms per ms of lead, and c47's change overshot the other way.
- Fix: `entry_leads.json` Violins I 472.5 0.05 -> 0.075 and 474.5 0.04 -> 0.065. By interpolation between the two renders this lands at about +10 ms.
- The same slow ramp affects the other letter-G pickups. 464.5 is +52 against a median of +4, and stable; it is in the swell class.
- An articulation option worth one pass-2 test: these phrase-first pickups on "StacSl Leg BC + Slur + Port MAX" (p.99: "slightly stronger attack" on notes without a legato connection), lead fitted from pcX. It has not been tried on pickups after rests (inferred).

**Violins I 88 and 536.** Leave the leads.
- Their fronts are on time: h10 +34 / +94 ms; A's band arrival -4 / +22 ms.
- The bodies bloom: t50 +132 / +246 ms. 536 sits at rel -12.6 dB.
- If anything, give them swell fills (finding 1c). More lead would make the fronts early.

### 4. The slow sections: one real sag in the coda clarinet, and two places where the estimator reads a timbre change, not lateness (measured)

- **Clarinet 1 706** (Più lento, espr., C5 -> B4, Leg Slur v60, rel -3 dB, one of the most exposed notes of the coda).
  - pcX +99 ms in both renders, but the crossover is on time (+7 ms).
  - The broadband stem drops 4-5 dB at the change: -43 dB before, -45..-48 dB from -0.06 s to +0.4 s. The new pitch's band keeps growing for 0.35 s.
  - Same pattern as 700, which c47 filled. Fix: `LEVEL_SHAPES_S["Clarinet 1"]` row `(706.0, [(-0.10, 0.0), (-0.05, 3.0), (0.40, 3.0), (0.55, 0.0)])` (seconds re the score onset). Fit it on the stem to an overshoot of at most +2 dB. Inferred until simulated.
- **Bass clarinet 708 / 710** (pcX +82 / +46).
  - The c43 level shapes work: the broadband level is flat (-49..-54 dB across the join), and the crossover is early (-70 / -61 ms).
  - The band reading is the new note's harmonics filling in at constant loudness.
  - Do not add lead or more shape.
- **Lento motto basses 4 / 10 / 11** (pcX +62 / +141 / -128, unchanged since c43). The pitch crossovers are -25 / -27 / -15 ms, so the pitch change is on time. Leave them.
- **Violins I 707** (Più lento entry, +153 ms, h10 +56, rel -9) is a real late entry. It is in the finding-1 table (+0.08).

### 5. Tempo map, fermatas, caesura and the attacca: as printed, keep (measured against `global.ily`)

- **Tempo steps.** Every printed tempo and step is in the map:
  - Lento 50 with 44-51.5 agogics.
  - Allegro 126 from qn 56.
  - poco rit. 176-184 ramped 126 -> 112.
  - Poco meno mosso 112.
  - animando 244-252 to 119.4, held to 260.
  - rit. 260-270 to 86.5 (printed 90).
  - Tempo dell'Allegro at 270.
  - stringendo 448-464 ramped 126 -> 139.4 (printed steps 129-138), a tempo 126 at 464.
- **Allargando 480-488.** Ramped 125 -> 101, so the fff downbeat 484 plays at 111 bpm against the printed 106 step. The ramp is the smoother reading. Keep it.
- **The rest of the development and recap:**
  - sostenuto 100 at 488-502, then 98 / 95 into the a tempo at 504 (a small liberty inside a printed sostenuto);
  - poco rit. 576-584 to 112;
  - animando 620-628 to 119.4, then 120 to 636;
  - largamente 100 from 636;
  - rit. 656-664 to 78.4 (printed 81).
- **Coda:** Tempo dell'Allegro 664; fermata 679 at 24 bpm (2.5 s, BEAT_STRETCH; printed MIDI 40 = 1.5 s); Più lento 72; rit. 704-712 to 50.4 (printed 53); Tempo I 50; last bar 30 bpm.
- **Phrase arcs** (PHRASE_ARCS) slow single beats by 4-12% (110.9 bpm at 331 and 407). Inside an Allegro appassionato that is phrase rubato, and nothing in the timing data argues against it (inferred).
- **Fermata 679.** The ff chord stops at 379.5 s, and the master is under -60 dB from 380.6 s to the solo's entry at 381.8 s: a real silence before the Più lento.
- **Caesura 636** (0.15 s, `CAESURA`). The master dips only 4-5 dB for about 0.2 s, because the suspended-cymbal roll (by design, into its stroke) and the timpani roll continue. The breath reads as a short lift before the fff, which is right.
- **Final chord and attacca.** The last bar holds 8 s (30 bpm). All notes end at qn 728. The master falls from -50 dB to -60 dB 0.7 s after the end and to digital silence 1.5 s after it (release, pass-2 soft cap). Nothing is cut off before the release.
- **Keyswitches.** 1143 changes, none at or after its note. 600 come 14-15 ms before the note (the 0.06 qn rule), 0 clashes, attack probe 0 late or holes. No change.

### 6. Section arrivals: the widest tutti attacks, if the actor has time after 1-3 (measured)

The tutti onsets with the widest 10-90% spread (8 or more tracks):
- 536 172 ms, 547 146, 416 145, 460 137, 633 137, 168 136, 454 135, 47 132, 112 132, 660 132, 668 129, 44 126, 88 125.
- At the structural arrivals: 464 (letter G ff): basses -129 ms against Contrabassoon +55. 520 (recapitulation): horns 1-2 -79 / -59 and Contrabassoon -56 against Trumpets a2 +30. 636 (fff): Violas -68 against Flute 2 +64, Tuba +56, celli +58.

Most of these parts sit 12-20 dB under the master, so finding 1's exposure filter left them out. Within 20 dB of the master there are 289 stable non-legato outliers, each more than 45 ms from its onset's median in both renders. To find them: groups with 8 or more tracks, rel -20 dB or more, |pcX - onset median| over 45 ms in c47 and over 35 ms in the same direction in c46. A second pass of the finding-1 rule (0.6 x error, clamp ±0.06 s) on the arrival onsets only (272, 464, 484, 488, 520, 584, 636, 664) would tighten the downbeats a listener hears as "together". Do this only after the c48 render confirms finding 1's transfer.

**Do not touch:**
- the tempo map and RAMP_SPANS, BEAT_STRETCH 679, CAESURA 636 and PHRASE_ARCS;
- the c47 Cello solo fills at 687 / 694, the Bass clarinet 4 / 10 / 708 / 710 level shapes, and the Lento basses' leads;
- the brass legato and timpani timing (brass legato -1 ms against the beat median; timpani robust SD 21 ms; harp 9 ms);
- KS_LEAD and the keyswitch placement;
- c46 / c47 render repeatability (4% of unchanged groups move more than 30 ms): keep the full rebuild of any Solo Horn / Solo Trumpet instance that flips, because Trumpet 1's legato reads -32 / -84 ms between the two states.
