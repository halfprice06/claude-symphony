# Cycle 01, critic A: articulation and phrasing (render c00)

Material: `cycles/c00/render/` stems and master, `build/parts.json`, `build/mockup-events.tsv`, `build/score_config.py`, `tools/score_to_parts.py`, `tools/pcx.py` (run on c00), and the May 2021 HO manual pages 89-94 (group A1). Times are on the parts.json tempo map, with qn 0 at 0 s of the rendered files. Levels are plain RMS in dB on the stems unless the text says master. Each judgement is marked **measured** or **inferred**.

## Manual notes (A1, PDF pages 89-94, read in full; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 89 | DIV A / DIV B record one chair of each desk. A divisi part is "not much less" loud than the whole section. | Violin I solo (DIV A, bars 349-356), Violas div (DIV B, 209-224, 349-356) | Partly. The solo sits 5-6 dB under Violins I at the same printed dynamic (stem medians: pp -50.3 vs -43.9, p -47.9 vs -42.7). That is right for "solo (gli altri tacet)", but the manual does not support it as a property of the patch: it comes from the mix. The Violas div at mf/f sits 3.7 dB over the section (-40.5/-36.5 vs -44.2/-40.2). That is lens B's area. |
| 90 | DIV patches have Close mics only. For the other mic positions, mix in the same articulations from the non-divisi patch and adjust the loudness. | The same two tracks | Not followed. They get only the shared hall send (`mix.json`). Lens C1's area. |
| 91 | Sustain has bow-direction round robins, finger position (not on the basses) and three vibrato levels. Détaché is not held indefinitely, and notes short enough to be staccato belong on a staccato row. | Re-bows on Sus MAX, CC70 "sul A" spans, the staccatos | Followed. The staccatos are on Stac rows, not Détaché. The re-bow level steps are finding 2. |
| 92 | Only the 2nd Violins have a Harmonics patch. All its harmonics sound two octaves above the fundamental, lowest note G4. | Violins I harmonic E6 ppp, bars 141-149 (qn 420-445, "harm., change bow freely") | Not followed. It plays an ordinary Leg Slur/Sus note. The 2nd Violins KS Master **has** a "Harmonics" row (key 32, `ks_maps.json`), and Violins II is silent over qn 410-460. MANUAL-GAPS #14 ("no row") only checked the 1st Violins master. See finding 6. |
| 92 | Pizzicato in every section, with 2 or 4 round robins | Celli and basses throughout; Violins II and violas 253-272 | Followed (Pizz RRx4). The per-pitch level is uneven: finding 5. |
| 93 | Marcato: short with a strong accent (RRx4). Spiccato: very short and bounced (RRx9). Spiccato Marcato MOD crossfades on CC1. | The "leggiero" theme; the accents after staccatos | Not used. The leggiero theme plays Stac samples (Violins I's "Staccatissimo RRx9" holds the V1 Stac samples, mvt1 c36). See findings 1 and 3. |
| 94 | Staccato, Staccato On Bow, Staccato Marcato MOD (CC1 brings in an accent), and Staccatissimo, "with notes of even shorter duration". 9-16 round robins. | The tutti repeated eighths; accents inside staccato lines | Staccatissimo samples are unused (Violins I "Stac RRx14", violas and celli "Staccatissimo RRx16"). See finding 3. |
| 94 | Repetitions: about a dozen repeats per sample, no round robin, with release trails | The theme head's two repeated eighths | Correctly not used: a dozen repeats at the sample's own rate does not fit a pair of eighths. |

MANUAL-GAPS corrections: in #11 the portamento target is the F sharp 6 at **qn 640** (bar 214 beat 2), not 639. The glissando starts on the C sharp 6 at 639 (`tC.ily`). In #14 the row exists in the 2nd Violins KS Master (above).

## Findings, ranked by what a listener would gain

### 1. Every string accent and down-bow after staccatos opens on Leg Slur MAX's slow first-note layer, so the accent arrives as a hole. This includes the theme head's accented G5 and the fff summit downbeat.

- **Where.** The accented half note of the theme head after "quarter, two staccato eighths, quarter". In Violins I: qn 39, 51, 69, 75, 111, 123, 207, 213, 285, 300, 315, 327, 345, 351, 759, 771, 789, 795, 819, 891, 897, 915, 927, 945, 951, 999 and **1005 (bar 336, fff, accent and down-bow: the summit)**. In Violins II: 132, 195, 315, 327, 345, 351, 915, 927, 945, 951, 981, 999, 1005. In violas: 123, 132, 183, 267, 723, 819, 879, 978, 999, 1005. In celli: 975, 999, 1005 (down-bow E2).
- **What is wrong (measured).** Each of these notes follows a Stac-row note but plays Leg Slur MAX. As a disconnected first note, that row plays its slow sustain layer (kit LEARNINGS 5-6). The 2-5 kHz bite is not the problem: attack minus body is -11.5 dB median on these Violins I notes, so they are soft, not harsh. The problem is weight and timing.
- **Evidence (measured).**
  - Mean level over the first 150 ms of the accent, minus the 50 ms peak of the staccato note before it. Violins I: median -3.1 dB over 27 notes. A plain staccato quarter after a staccato quarter reads -1.6 dB on the same measure (130 notes), so the accents land about 1.5 dB *under* an unaccented staccato instead of 2-4 dB over it.
  - The p/mp statements are the worst. qn 39, 75 and 285 (vel 73): -14.3 dB. 759: -8.2. 789: -9.9. 795: -7.8. 819: -7.0. The Violins I stem at bar 14 sits at -54..-55 dB for 0.4 s after the downbeat against -39..-41 for the staccatos, and reaches -44 only 0.7 s later. On the master the bar 14 downbeat dips to -46/-48 dB from -39..-41.
  - At the summit, qn 1005: Violins I -15.0 dB, Violins II -7.6, violas -11.1, celli -10.0. The master at the bar 336 downbeat (50 ms windows) is -14.2/-14.3 dB against -12..-13 for the staccato quarter before it, and reaches -9 dB only about 0.7 s later. That is why bar 337 (-9.5) measures louder than bar 336 (-11.5) in metrics.md. The fff arrival is late and soft in the strings.
  - The GENTLE_ACCENT swell (+2 dB at 39, +3 dB at 1005 in `vol_db`) cannot fill a 10-15 dB hole.
  - For comparison, Sus MAX accents after Sus notes (qn 144, 372) read +5.1 and +0.5 dB on the same measure.
- **Why (read in score_to_parts.py).** `STR_ACC_AFTER_SUS` already counts Stac rows as "sus-like" (`sus_like`). It excludes slurred notes, though, and notes followed by a same-pitch repeat. The theme head's accent starts a slur (G5 slurred to F sharp-F eighths), and the summit A6 is followed by the down-bow A6 at 1008. Both fall through to the "unslurred notes stay on Leg Slur MAX" branch.
- **Fix.**
  - Now, config only: in `build/score_config.py`, `DOWNBOW_STROKE_AT = {"Violins I": [39, 51, 69, 75, 111, 123, 207, 213, 285, 300, 315, 327, 345, 351, 759, 771, 789, 795, 819, 891, 897, 915, 927, 945, 951, 999, 1005], "Violins II": [132, 195, 315, 327, 345, 351, 915, 927, 945, 951, 981, 999, 1005], "Violas": [123, 132, 183, 267, 723, 819, 879, 978, 999, 1005], "Violoncellos": [975, 999, 1005]}`.
  - What that does: each note becomes a fresh Sus MAX stroke (entry lead, velocity from `REBOW_VEL_BY_CC`, no delayed-vibrato dip at f and louder through `STROKE_NO_VIB_DELAY`), and the next slurred note joins from it as a Leg BC target.
  - Generic alternative in `tools/score_to_parts.py`: let `STR_ACC_AFTER_SUS` also take a slur's first note when it is accented or printed down-bow and the note before is on a Stac row. Keep the same-pitch exclusion for unaccented notes only.
  - After the render, check two things. (1) The accent sits 2-4 dB over the staccato before it (first 150 ms) and its 2-5 kHz attack minus body stays under 0 dB. (2) The p strokes at 39/75/285 do not come out bright. If they do, lower `REBOW_VEL_BY_CC` at CC 46-58 for these onsets, or give them a soft swell instead.

### 2. The re-bows of the ppp held G sharp 5 and the harmonic E6 dip 8-12 dB and leave level steps. In the ppp coda the master dips 5-7 dB at each one.

- **Where.** Violins I re-bows at qn 6.54 (2.85 s), 433.17 (99.81 s), 1103.88 (267.58 s), 1116.39 (271.31 s) and 1125.14 (275.05 s). Also celli 1078.44.
- **Evidence (measured).** Stem dip is the lowest 100 ms level within 1.2 s of the re-bow, minus the 0.75 s before it. Step is the mean from 1 s after the re-bow to the next one, minus the same level before.

  | Re-bow (qn) | Stem dip | Step | Master dip |
  |---|---|---|---|
  | 6.54 | -9.1 | -4.6 | +3.4 (the horn call enters) |
  | 433.17 | -11.6 | -7.6 | -2.5 |
  | 1103.88 | -9.7 | -3.8 | -5.3 |
  | 1116.39 | -8.2 | +0.3 | -4.9 |
  | 1125.14 | -11.1 | -3.3 | -7.2 |
  | Celli 1078.44 | -11.0 | -1.5 | -4.8 |

  In bars 364-376 Violins I and Hn 1 are nearly all there is, so each re-bow is a one-second hole in the close (inferred: audible). The loop pulse is not the problem: on Violins I over 1089-1124 the level autocorrelation at 3.95 s is +0.26, the centroid's -0.02, and the master's -0.01.
- **Fix.** Run `tools/fit_rebows.py` on c00 and write `build/rebow_fills.json` (kit LEARNINGS 6, mvt1 c26: follow the level before the re-bow over the first 1.5 s, then hold the offset, clamped -6..+9 dB). On the next render, check that every listed re-bow stays within 0..-2 dB of the level before it on the stem and within -2 dB on the master.

### 3. In the ff tuttis the repeated staccato eighths blur into one note on the master (S1).

- **Where.** The theme head's repeated eighths at bars 105-120 (qn 313, 319, 325, 331, 340, 349, 355) and 305-320 (913 ... 955), in all the strings and the winds that double them.
- **Evidence (measured).**
  - Master dip between the two eighths of each pair (10 ms windows, between the two peaks): bars 105-120 median 2.7 dB (0.2-3.5; 325: 0.2), bars 305-320 median 1.9 dB (1.2-3.3).
  - The p statement at bars 13-28 gets 3.6-4.4 dB, and the reprise 2-6.6.
  - Stems in the tutti: Violins II 0.0-2.8 dB at 313, 319, 325, 349, 913, 919, 925, 949. Violins I 3-5 dB. Clarinet 2 2.8-3.8 dB on all 15 of its eighth pairs.
  - The Violins I and II stems hold their full level through the whole first eighth (319.0-319.5) and dip only at the second onset. At ff the Stac sample lasts longer than the 0.114 s eighth.
  - The strings carry the largest share of energy in the gap (Violins I 13 %, Violins II 11 %, violas 9 %).
- **Fix.**
  - Use shorter stroke rows for the printed staccatos in the two tutti statements: `ART_SPANS` entries with `"mark": "staccato"`, `"from": 312, "to": 360` and `"from": 912, "to": 960`.
    - Violins I: "Stac RRx14". By mvt1 c36's swap it should hold the real Staccatissimo samples; verify which samples it plays.
    - Violins II: "Spiccato RRx9" (it has no Staccatissimo row).
    - Violas and celli: "Staccatissimo RRx16".
  - Use the `vel_by_cc` form of Movement I's config so the level at ff matches the Stac rows.
  - The manual (p.93-94) describes both rows as shorter than staccato. Their real lengths at ff are not measured (inferred).
  - Target: master dip of at least 3.5 dB at every tutti eighth pair, with no new attack bite (2-5 kHz attack minus body under 0 dB).

### 4. Woodwind staccatos play as cut Sus MAX notes; the eighths are slices of the attack (MANUAL-GAPS #1).

- **Where.** About 600 printed wind staccatos: the counterstatement at bars 29-44 (Flute 1 and Oboe 1 leggiero, qn 84-132), the tuttis 105-120 and 305-320, the reprise and the coda build (329-336), and the cor anglais' pp arpeggio (bars 95-100).
- **Evidence (measured in parts.json).** Played lengths of printed staccato eighths: Flute 1 0.052-0.080 s (median 0.067), Oboe 1 0.068, Clarinet 2 0.066, **cor anglais 0.036-0.057 s (median 0.046)**. Staccato quarters: 0.114-0.154 s. Every one is on Sus MAX / Sus Non Vib, and some quarters are on Leg Slur MAX.
- **Evidence (inferred from mvt1 c39).** A Sus note ended at 46-67 ms is cut inside its attack, so what sounds is the cut-off attack plus the release. Movement I c39 measured "Stac DblTng RRx9" with a rise of 0.03-0.09 s against 0.18-0.22 s for this approach, and a natural decay.
- **What is fine (measured).** The perceived attack centroids already agree with the strings (winds +0.05..+0.07 s, string Stac +0.055..+0.083 s), and so does the sounding length to -12 dB (about 0.2-0.25 s with the hall). The gain is in the colour and articulation of the attack.
- **Fix.**
  - `ART_SPANS` on Flute 1, Flute 2, Oboe 1, Oboe 2, cor anglais, Clarinet 1, Clarinet 2 and Bassoon 1 over the staccato passages (start with qn 84-132, 312-360, 756-840, 912-960 and 984-1008), with `"art": "Stac DblTng RRx9"`, `"mark": "staccato"` and `vel_by_cc` (Movement I: mf 82, f 96).
  - `STAC_LEAD_S` per wind track (Movement I: cor anglais 0.03).
  - It is one more row per track, not an extra instance.
  - Measure the attack against the string Stac rows (S2) and the level against the doubled strings.

### 5. The pizzicato basses are lumpy by pitch: A and G sharp sit 7-9 dB over E.

- **Where.** Double basses pizz throughout. Most audible in the reprise's div. pizz. octaves, bars 253-268 (qn 756-804), where the basses carry the bass line under the leggiero theme.
- **Evidence (measured).** Peak level of 126 isolated pizz. strokes, regressed on velocity. Residuals by pitch: A1 (33) +6.6 dB (14 strokes), the A1+A2 octave +5.7 (4), G sharp 1 (32) +5.4 (5), against E1 (28) -2.0 (15), the E octave -2.4 (7), E2 (40) -2.4 (21) and B1 (35) -1.0 (39). In bars 253-268 at one printed p and velocity 53, the A octaves peak at -37.6..-40.2 dB and the E octaves at -46.5..-50.1. Celli pizz. are less even than the arco sections too (residual SD 5.0 dB; D3 -7.7 on 3 strokes, too few to act on).
- **Fix.** `build/pitch_trims.json`: `{"Double basses": {"_arts": ["Pizz RRx4"], "32": -5.0, "33": -6.0, "44": -5.0, "45": -5.0, "28": 2.0, "40": 2.0}}`. The `_arts` filter (c08) applies the trims to pizz. notes only. Check that the trim ramp does not cut the pluck's front edge (kit section 13: ramps written for sustains are wrong for plucked notes). If it does, use velocity offsets per pitch the way `HARP_PITCH_VEL` does.

### 6. Two printed string colours are not played: the "port." at bar 214, and the natural harmonic at bars 141-149.

- **Port. (measured in parts.json).** Violins I C sharp 6 (qn 639, Leg BC MAX) to F sharp 6 (qn 640, Leg Slur MAX, v124) is printed with a glissando line and "port." (`tC.ily` c538: "the trio return's one marked shift"). It plays a plain legato. **Fix:** `PORT_TARGETS = {"Violins I": {640.0: 100}}` in `build/score_config.py` (loads "Leg Port MAX"; mvt1 c11-c12 measured the intermediate semitones +17-21 dB for a violin fourth). Check the glide length (0.08-0.25 s) against the quarter's 0.26 s at quarter 228.
- **Harmonic (read; gain inferred).** Violins I E6 ppp, qn 420-445, is an ordinary Leg Slur note re-bowed at 433.2 (finding 2). The manual says the 2nd Violins Harmonics patch sounds two octaves above the fundamental, lowest G4 (p.92). The 2nd Violins KS Master already loaded on the Violins II track has that row, and Violins II has no notes over qn 410-460. **Fix:** route the two Violins I notes into the Violins II track for qn 420-446 (a small `TRACK_WINDOWS` / staff-routing addition in `score_to_parts.py`; `TRACK_WINDOWS` takes one window per track today). Add an `ART_SPANS` entry `{"from": 420, "to": 446, "art": "Harmonics"}` on Violins II and `AUTO_REBOW_SKIP` for it: a harmonic row has no bow round robin to hide a re-bow, and the score says "change bow freely". First check which key plays which sounding pitch (`cycles/c00/port/range_check.py` on the Harmonics row). This also removes the -11.6 dB re-bow dip at 433.2. It adds no Opus instance.

## Also measured (not ranked)

- **Legato timing spread (S2, lens C3's area).** pcx.py on c00: Violins I joins robust SD 80 ms, Violins II 96, violas 77, celli 68. The 10th-90th percentile spans about -100..+140 ms in the Allegro: more than an eighth at quarter 264. Allegro leads are 0.15-0.25 s median (`LEG_LEAD_S` string 0.17, Violins II and violas 0.20, plus per-articulation extras), set at quarter 126.
- **The trio's legato lines join cleanly (measured).** Median join dips: Clarinet 1 2.4 dB (bars 153-168) and 2.7 (209-224); celli 2.7 dB on 50 ms windows (169-184); Violins I 1.8 / 3.5; Violin I solo 2.6; Flute 1 "col Vl. solo" 1.9 dB on 200 ms windows.
- **No problems found in these checks (measured).** No chord is sent to a monophonic legato row on any track. Every arco entry after pizz. has at least 0.64 s. No keyswitch lands within 5 ms of its note except two on Violins I. The timpani motive x alternates hands (61 `timp_rh` strokes). Sections hold their loop pulse low.

## Do not touch

- The string Stac rows and the 0.025-0.045 s `STAC_LEAD_S` in the soft statements. Bars 13-28: Violins I repeated eighths dip 5.5 dB on the stem and 3.6-4.4 on the master. Attack centroids are +0.055..+0.083 s across sections and match the winds.
- The trio's legato settings, and the Violin I solo / Flute 1 legato at bars 349-356.
- GENTLE_ACCENT's no-bite rule: every family's accents read 2-5 kHz attack minus body -3..-13 dB. Keep it when fixing finding 1.
- The pizz./arco handling, `TIMP_RH_ALT`, and the CC70/CC15 lanes.
