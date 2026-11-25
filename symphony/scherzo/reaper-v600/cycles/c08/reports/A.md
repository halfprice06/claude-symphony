# Cycle 8, critic A: articulation and phrasing (render c07)

All measurements are on `cycles/c07/render/` (dry stems 01-31, return stems 91-94, `00_Master.wav`), with the rendered data in `cycles/c07/build_render/parts.json` and its tempo map. "Stem" means a dry stem and "master" means `00_Master.wav`. Scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c08-A/` (deleted at the end). The c06 stems are gone, so c06 numbers are quoted from the c07 critic A report.

## Manual notes (cycle 8 slot A: group A1, May 2021 HO manual PDF pp. 89-94, Hollywood Strings sections, divisi, longs, shorts; plus MANUAL-GAPS.md)

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| DIV A / DIV B are one chair per stand (half the section) and have Close mics only. A divisi part is "not much less" loud than the whole section (p.89). For the other mic positions, use the non-divisi patch and adjust the loudness (p.90). | Violin I solo (DIV A, bars 349-356), Violas div (DIV B, 209-224 and 349-356), Violins II "la metà" (full section at -3 dB), basses div. pizz. octaves 253-268 | Mostly. The DIV tracks are Close-only with the c05 shelves and sends. The solo is a half section, not a soloist (MANUAL-GAPS #5). The basses' div. octaves still play as two full sections (MANUAL-GAPS #9, open). |
| Sustain rows: bow-direction round robins, finger position on CC70, three vibrato levels (p.91) | the sul A spans, the held G sharp of bars 1-8 and 364-376, the celli's held notes | Yes. CC70 follows SUL_SPANS. The re-bows show no loop pulse (level and centroid autocorrelation at 3.95 s: Violins I 0-23 -0.10 / -0.22, 1089-1128 +0.03 / +0.04, 420-445 +0.01 / -0.29; measured). |
| Marcato Sustain adds a marcato sample at the start of a sustain for "extra power at the start of the note" (pp.91-92) | the theme-head accents and hemiola strokes (Sus Marc LITE), the tutti sfp of bar 301 | Partly. The heads and the hemiola use Sus Marc LITE. The sfp at qn 900 plays a plain Sus MAX stroke, and its sf arrives late (finding 2). |
| Flautando is only in the 2nd Violins; Sus at pp without vibrato comes close (p.92) | the ppp G sharp 5 of bars 1-8 and 364-376 | Not needed (no flautando or non vib. is printed). CC1 sits at 38-41 there. |
| **Harmonics only in the 2nd Violins**, sounding two octaves above the fundamental (p.92). In the `.oib` (read) the regions are keyed at the sounding pitch, MIDI 79-108, with p and mf layers. | Violins I natural harmonic E6, bars 141-149 (qn 420-445), "harm., change bow freely" | **No.** It plays as an ordinary vibrato note on the 1st Violins KS Master (finding 4). The 2nd Violins KS Master has a "Harmonics" row (590 regions), and the Violins II track is silent over qn 410-460. |
| Pizzicato rows are round robins of 2 or 4 samples (p.92) | celli and basses pizz. throughout, violins and violas 253-272 | Yes. c07 added RR_RESET_AT. The trims for the group heads are scheduled (ONE_TIME_c08 item 6). |
| Spiccato, and Spiccato Marcato MOD (CC1 morphs to marcato) (p.93) | Violins II tutti and coda on Spiccato RRx9 | Spiccato is used. In the coda its pairs merge (finding 3). The MOD patches are not loaded. |
| Staccato types: plain, On Bow (the bow stops on the string), Marcato MOD, Staccatissimo, with 9-16 round robins (pp.93-94) | the theme head in every statement | Yes, by row. On the 1st Violins KS Master, "Staccatissimo RRx9" plays the Stac samples and "Stac RRx14" plays the staccatissimo samples (loop LEARNINGS c01). "Stac On Bow RRx9" (6,260 regions) is not used. |
| Repetitions: a dozen repeated notes with real bow changes and release trails, no round robin (p.94) | the theme's repeated eighth pairs (S1) | Not used, and no longer needed in the soft statements: the stem pair dips there are 5.4-7.6 dB. |

## Findings, ranked by what a listener would hear

### 1. In the soft theme statements and the fugato, the two slurred eighths after the accented half note still sound weak. The second eighth was left at v53 (measured)

Where. These are the head tails (an accented half note slurred to two eighths). Violins I at qn 39, 51, 69, 75 (theme A), 285 (retransition) and 759, 771, 789, 795 (reprise). The fugato's soft tails: Violins II 195, violas 183 and 879, celli 171 and 867.

What c07 did. It applied c07 A #2 in part: a 0.06 s lead and v88 on the first eighth of the eight Violins I tails, and a 120 ms release on Sus Marc LITE. The second eighth stayed at v53-63. Tail 285 and the fugato tails got nothing.

Evidence. "Own-pitch dominance" is the energy at the eighth's harmonics 1-3 against the previous pitch's harmonics, inside the eighth's own slot (2048-point FFT, exclusion bands). "Level" is the eighth slot's RMS against the half note's body.
- Violins I first eighth: -9 to +2 dB (c06: -13 to -27), so it improved. The second eighth is -2 to -9 dB (39 -5, 51 -3, 69 -9, 75 -7, 759 -2, 771 -3, 789 -5, 795 -5). The levels are -7 to -15 dB under the body; at 69 and 789 both eighths are about -15 dB.
- Tail 285 (v53 / v53): -8 / -8 dB.
- Fugato tails at v53. Violins II 195 first eighth -8 dB. Violas 183 -9 and 879 -9. Celli 171 and 867: the second eighth at -18 dB.
- For comparison, the tuttis at v100: first eighths +1.6..+7.3, second +6..+16 dB, levels -3..-10. The winds play the same figure on Leg Slur MAX at v80 or more, and every tail there speaks.

These eighths are melody notes, so the melody loses one or two notes every two bars of theme A and the reprise.

Fix (`build/score_config.py`, existing knobs):
- `VEL_SET["Violins I"]`: add 85 at the second eighths 41.5, 53.5, 71.5, 77.5, 761.5, 773.5, 791.5, 797.5, and 88 / 85 at 287.0 / 287.5.
- `VEL_SET` 88 / 85 on the fugato tails: Violins II 197.0 / 197.5, Violas 185.0 / 185.5 and 881.0 / 881.5, Violoncellos 173.0 / 173.5 and 869.0 / 869.5.
- Add "Violoncellos" to `SHORT_SUS_LEAD_TRACKS`, so the celli get the 0.06 s lead as well.
- The c07 first-eighth change (v53 to v88) moved dominance by about +8 dB, so expect the same here.
- Pass: both eighths at -3 dB dominance or better, and within 8 dB of the half-note body (the tutti v100 tails reach -3.5..-8 dB).
- If the levels stay more than 10 dB under the body, run c07 A #2's A/B on tails 69 and 789: put the whole figure on Leg Slur MAX (`SHORT_SUS_LEG_TRACKS = ("Violins I",)`, `SHORT_SUS_LEG_S = (0.10, 0.25)`), with the accent left to the GENTLE_ACCENT swell.

### 2. The tutti sfp at bar 301 (qn 900): the sf arrives 0.12-0.18 s late in the winds and Violins I, as the curve falls to p (measured)

Where. qn 900, Flute 1, Cor anglais, Clarinet 1 and Violins I. The other woodwinds are entered at the same velocity. The horns print p there, not sfp, and are correct.

Evidence. The table gives the stem peak after the beat (window -0.06..+0.35 s) and the level 30 ms in, against that peak:

| track | row, velocity | peak after the beat | +30 ms against the peak | p body (901-901.8) against the peak |
|---|---|---|---|---|
| Flute 1 | Sus MAX v53 | +148 ms | -10.5 dB | -7.3 dB |
| Cor anglais | Sus MAX v53 | +175 ms | -10.2 | -6.4 |
| Clarinet 1 | Leg Slur Rep v53 | +123 ms | -5.7 | -22.5 |
| Violins I | Sus MAX stroke v105, lead 80 ms | +115 ms | -5.1 | -22.1 |
| Oboe 1 | Leg Slur MAX v53 | +45 ms | -0.9 | -10.9 |

The sfp curve holds the sf level for 0.25 qn and is at p by 0.5 qn: `FP_SPIKE = ("f", 0.25, 0.5)` with `SFP_SPIKE_DYN` "sf", and CC11 120 -> 48 over qn 900.25-900.5. At quarter 264 that is 57 ms and 114 ms. These are Movement I's seconds converted to qn at a tempo twice as fast. The soft attacks (v53 on the winds) reach their peak after the curve is already at p. Flute 1 and the cor anglais therefore play a swell of 6-7 dB, not sf-then-p. On the master the sf is still there (-13.0 dB at 900 against -19 at 900.25 and -26.9 at 901.5), carried by the violas and celli. In the winds and the first violins the attack is soft. c06 C #1 gave the strings v105 strokes. The winds kept the v53 of their p.

Fix (`build/score_config.py`):
- `FP_SPIKE = ("f", 0.45, 0.9)`. It holds about 0.10 s and is at p by about 0.20 s at quarter 264. It is the only fp/sfp mark in the score, so nothing else moves.
- `VEL_SET` 900.0: 100 for Flute 1, Flute 2, Oboe 1, Oboe 2, Cor anglais, Clarinet 1, Clarinet 2, Bassoon 1, Bassoon 2 and Contrabassoon. That velocity speeds up the woodwind attack; this is inferred, so check the peak time.
- Violins I at 900: the Marcato Sustain row the manual describes for "extra power at the start" (pp.91-92). The row is already loaded. Add an `ART_SPANS` entry `{"from": 899.6, "to": 900.1, "art": "Sus Marc LITE", "vel_by_cc": [(58, 74), (72, 80), (88, 84), (100, 88)]}`. Because ART_SPANS bypasses leads (LEARNINGS c06), add `REATTACK_LEAD_AT["Violins I"][900.0] = 0.08`.
- Pass: every wind and Violins I peaks within +60 ms of the beat, and the p body sits at least 10 dB under the peak by qn 901.

### 3. In the coda build (qn 984-1005), the repeated eighths of Violins I and II merge on the master (S1, measured)

Where. The pairs at 985.5, 988.5, 991.5, 994.5 and 997.5. This is the approach to the fff summit.

Evidence (stem dip at the second eighth: maximum of -30..+80 ms minus minimum of -60..+30 ms):
- Violins I on "Stac RRx14" (the staccatissimo samples): 991.5 3.2 dB, 985.5 3.5, 994.5 5.1, 997.5 6.1.
- Violins II on "Spiccato RRx9": 994.5 2.9, 985.5 3.2.
- Master: 991.5 1.7 dB, 985.5 3.0, 988.5 3.4, 997.5 4.9. The tutti statements now measure 4.6-5.4 dB median, after c07 moved their pairs onto Staccatissimo RRx9 / Stac RRx9.
- At 991.5, Oboe 2 (Sus MAX slices, 64 ms) and Clarinet 1 (staccatos on the Leg Slur Rep row) carry 47 % and 19 % of the dry and return stems' energy inside the gap. Both are louder in the gap than in the next note's attack (gap minus peak 1.1 and 0.5 dB).

Fix (`build/score_config.py`; both rows are already loaded, so memory is unchanged):
- Violins I: insert pair spans ahead of the coda span, as c07 did for the tuttis: `{"from": a, "to": a + 1.0, "art": "Staccatissimo RRx9", "mark": "staccato", "poly": True}` for a in 985, 988, 991, 994, 997.
- Violins II: the same with "Stac RRx9" at 985 and 994, plus the -4 dB `ROW_TRIM_DB` that its tutti pairs have. Check `row_trimmed` in parts.json, because ROW_TRIM needs a Leg neighbour (LEARNINGS c05).
- Oboe 2 and Clarinet 1: shorten their staccato eighths in 984-1005 from 0.5 to 0.35 of the slot (they are slices, so the sample's own release does not apply).
- Pass: master dips of 3 dB or more at every coda pair.

### 4. The horns play their staccato quarters in the tuttis as sustain slices that peak 0.12 s late, and their repeated notes merge (S1, S2, measured)

Where. Horn 1 and Horn 2 in bars 105-120 and 305-320 (qn 312-360, 912-960). The figure is tenuto quarter, rest, staccato quarter, then the next bar's tenuto quarter on the same pitch. 36 / 34 staccatos in the movement. The trio ff (bars 209-224) for Horn 2's tenuto repeats.

Evidence:
- Staccato peaks after the beat, in the tuttis: Horn 1 +125 ms, Horn 2 +123 ms (Sus MAX, 0.72 qn = 164 ms). Trumpet 2 on Sus Non Vib slices: +114 ms. Trumpet 1 on "StacSs DblTng RRx9": +43 ms. Violins I staccato rows: +82 ms. At quarter 264 the horns' 0.12 s is about one eighth late.
- Repeated tenuto dips on the stem (staccato followed by tenuto on the same pitch; level across the onset against the neighbouring bodies):
  - Horn 2 tutti: 1.3-1.5 dB (n = 7 in each tutti).
  - Horn 1 tutti: 2.4-4.4.
  - Horn 2 trio ff: 0.1-0.9 dB at 627, 642, 651. There the 70 ms re-tongue gap is filled by the 237 ms release and the slow v63 attack.
- Trumpet 2's StacSs row is already scheduled (ONE_TIME_c08 item 6).

Fix:
- `ART_SPANS` for Horn 1 and Horn 2: `{"from": 0.0, "to": SCORE_END, "art": "StacSs RRx9", "mark": "staccato", "vel_by_cc": _TSTAC}`. The row is in the 1FH KS Master; reuse Trumpet 1's velocity table, and keep the brass `STAC_LEAD_S`.
- Add Horn 2 to `WIND_REP_RETONGUE_BY` with Horn 3/4's tutti-tested values plus a deeper fall: gap 0.07 s, fall 12 CC over 0.12 s.
- Cost: 6,910 regions per horn row, against 4,080 for Trumpet 2's. All three together are about 18 thousand regions, about 0.8 GB at c02's rate. Finding 6 frees 22 thousand.
- Pass: staccato peaks within +60 ms of the beat, and repeated-pair dips of 3 dB or more.

### 5. Violins I's harmonic E6 (bars 141-149) sounds like an ordinary vibrato note; the library has a harmonics row (manual p.92, measured, plus a patch read)

Where. qn 420-445.8, Violins I, ppp, "harm., change bow freely". In the link it is the only high line, over low winds and Horn 1.

Evidence:
- Spectrum: on the stem, the second harmonic of the E6 note stands +1.3 dB over its fundamental. The same section's ordinary G sharp 5 sustains measure -6.3 and -7.0 dB. A natural harmonic is close to a pure tone.
- Pitch: its modulation (standard deviation after slow drift is removed) is 7.0 cents, the same as the vibrato'd G sharp 5 notes (5.2-6.7). The note is a stopped, vibrato sustain.
- What the library has. The manual says only the 2nd Violins have a Harmonics patch (p.92). The 2nd Violins KS Master includes a "Harmonics" row (key 32): 590 regions, keyed at the sounding pitch 79-108 (E6 = 88 is inside), with p and mf layers. Its loop is 85,000-250,000 samples, about 1.8-5.2 s at 48 kHz, so keep the re-bow at 433.2.
- The Violins II track has no notes from qn 410 to 460.

Fix. Play these two notes on the Violins II track's Harmonics row (no new instance; +590 regions):
- Small generic tool change in `tools/score_to_parts.py`: a `BORROW_NOTES = {track: [(staff, from_qn, to_qn)]}` table that adds another staff's notes in a window to a track that keeps its own staves. TRACK_SPLITS cannot do this, because the split track keeps only window notes.
- Settings: `BORROW_NOTES = {"Violins II": [("VlnI", 419.5, 446.0)]}`, `TRACK_WINDOWS["Violins I"]` excluding 419.5-446.0, and `ART_SPANS["Violins II"]` 419.5-446.0 "Harmonics".
- Level: the same CC11 at ppp and the same vol envelope as now. The Violins II seat sits a little right of Violins I, which matters little at ppp.
- Without a tool change, the fallback is a pass-2 `ALIAS_TRACKS` entry on `2nd Violins/01 Long/2nd Violins Harmonics.oib`. It costs a second render pass.
- Pass: H2 at least 10 dB under H1, pitch modulation under 3 cents, and the level within 1 dB of c07's bars 141-149.

### 6. The printed "port." at bar 214 (qn 640) plays as a plain jump. Its row is the most expensive per note in the project (measured)

Where. Violins I, C sharp 6 to F sharp 6 at qn 640, `PORT_TARGETS {"Violins I": {640.0: 100}}`, on "Leg Port MAX".

Evidence:
- Pitch track with a 2048-point window and 10 ms steps: C sharp 6 (+0.16 st) holds until 0.02 s before the beat. Then it reaches +3.97 st within 10 ms and +4.9 st by the beat. No frame shows the slide through the notes in between that the manual describes for portamento legato (p.98).
- Velocity: the row plays at v100. The manual's true-legato timing says 110-127 gives the tightest transitions and 50-60 slower ones (p.144, MANUAL-READING T1). Kit LEARNINGS (LEG_VEL_SPANS, Movement I c40) found that 50-75 plays more of the recorded slide.
- Cost: "Leg Port MAX" costs 22,428 sample regions for this one note (rowcost on c07). That is the largest per-note cost in the project and alone more than finding 4 needs.

Fix:
- First make it audible: `PORT_TARGETS = {"Violins I": {640.0: 55}}`. Optionally add a CC5 (Legato / Portamento Time) point near 100 at 639.3, reset afterwards (the Opus Portamento script uses CC5, p.142-143).
- Measure the glide: at least 60 ms of pitch between C sharp 6 and F sharp 6.
- If it still jumps, play 640 as a Leg Slur MAX target at v55 and unload Leg Port MAX. This port. is on the c01-c02 do-not-touch list, so record the measurement when changing it. The 22 thousand freed regions pay for finding 4's rows.

## Checked and found working (measured)

- Legato: no chord goes to a monophonic legato row on any track, and no same-pitch legato overlap. Every join overlaps 45 ms (winds, brass) or 60 ms (strings). The 35 % cap leaves no join under its floor.
- Accents, weight not bite. The 2-5 kHz front (0-80 ms) against the body (80-300 ms) has a median of -6.5 to -13.6 dB on every string and woodwind track; the maximum is Flute 1 at 1005 (+6.1).
- Staccato lengths: string, row-wind and Trumpet 1 staccatos are 57 ms (eighths) and 114 ms (quarters) in every section, 52 / 104 ms in the faster coda. That is 50 % of the slot, the same in theme A, the counterstatement, the fugato, the tuttis and the reprise. The exceptions are the slice players: Clarinet 1 66 / 149 ms, Oboe 2 68, Bassoon 1 78 / 140-174, Horns 73 / 147-164, Trumpet 2 73 / 147 (findings 3-4).
- Repeated pairs (S1), stem: Violins I theme A 5.4-5.9 dB, reprise 5.4-6.2, tuttis 4.6-5.5 (c06: 0.9-2.6 at 325.5, 331.5, 355.5 and the matching 925-955 pairs). Woodwind Stac DblTng rows 4.0-11 dB. On the master, theme A and the reprise measure 1.9-3.9 dB, held down by the accompaniment rather than by Violins I: the violas carry 26-30 % of the gap energy at 43.5 / 64.5, and the celli 74 / 56 % at 763.5 / 799.5.
- Re-bows of the held notes: no loop pulse (above). Horn 1 trio climax: 651 / 654 now 3.0 / -0.1 dB (c06 11.2 / 12.5).
- Violins II con sord. (CC15 127 at 393.8, before the 501.5 entry; 0 at 552.5 in the rest before the senza sord. at 588).
- Timpani rolls end on a stroke at every roll (309, 390, 624, 720, 858, 909, 996, 1008). The pp roll at 708-718 dips by about 15 dB in its middle (-44 -> -59 -> -45 dB, 1.25-2.0 s after the start) while its envelope is flat. That comes from the Rls sample, whose loops have no crossfade (read). Lower priority; a restrike at 712 would hide it.

## Scheduled c08 items, measured in my area

- Brightness (ONE_TIME_c08 item 1). In my area the top end comes mostly from the Violins I short rows. Violins I stem 2-6 kHz share: -3.0 dB in theme A (Staccatissimo RRx9 at p), -2.2 dB in the coda build. 6-20 kHz: -22.2 in theme A, -15.6 in the coda build on Stac RRx14 at fff, against -23.5 in the trio legato. Violins II reaches -18.1 in the coda. The master's theme-A 2-6 kHz share is -4.7 dB.
  - The planned Violins I 5 kHz -6 / Violins II -4 dB cuts go where this energy is.
  - Finding 3's move of the coda pairs off Stac RRx14 should also lower the coda's 6-20 kHz.
  - After the EQ, re-measure the coda and theme-A pair dips and the staccato peak times. The dips are broadband and should hold, but the attacks will read softer. Do not raise velocities to win the edge back (HO short rows change layer by velocity).
- String shorts, beat weight in the envelope (item 4). Keep the second note of each repeated pair within 1 dB of the first, or the pair dips above shrink. Put the +1.5 / 0 / -1 dB on beat 1 against beats 2-3, not on the eighth after the beat.
- Wetness: c07 is not too dry in my area. The soft master pair dips are still 1.9-3.9 dB (not dry-separated). The sfp fall (900 -> 901.5: -13.0 -> -26.9 dB on the master) keeps a tail under the p.

Do not touch: the c07 tutti pair split (Violins I Staccatissimo RRx9, Violins II Stac RRx9 at -4 dB); the first-eighth v88 and the 0.06 s SHORT_SUS lead (add to them, finding 1); the Sus Marc LITE heads with their level steps and 120 ms release; the legato overlap floors and the 35 % cap; the wind Stac DblTng rows and Trumpet 1's StacSs row; the re-bows and their fills; the Horn 1 Port Lng / Sus MAX split of the trio climax; GENTLE_ACCENT; the CC15 timing; RR_RESET_AT.
