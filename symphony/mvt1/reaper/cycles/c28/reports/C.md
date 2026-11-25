# Cycle 28, critic C: holistic comparison (render c27)

## Method

I compared the stem-fixed c27 render (`cycles/c27/render/`, `cycles/c27/rendered_build/parts.json`, `mvt1-mockup-c27.mp3`) with c00 (first build, tempo map from `cycles/c01/before/parts.json` with `rendermap.wrap`), with c22 (five cycles back), with the Dvořák 9/i recording (lossy MP3, decoded to 48 kHz) and with the stored Brahms 1/i and 4/i measurements (musopen, lossless; `symphony/render/critics/c00/ref_brahms*_i_musopen/metrics.json`). Whole-file measures come from `symphony/render/tools/measure.py`, the tool that made the reference metrics. Delivered-file loudness and motion come from `tools/motion.py`. "K" levels are K-weighted power over 2 qn windows; band levels are 0.4 s frames, "loud" = top 10% of active frames, "soft" = bottom 30%. Each cycle's own tempo map is used. Delivery simulations: stems times a dB envelope, summed, then `tools/deliver_master.py` on the result. Score pages 2, 3, 4, 5, 9, 11 and 12 were read. The scratch scripts were throwaway and the scratch folder is deleted; each finding states its windows so the actor can repeat it.

## State of the render

**What has improved since c00 (measured).**
- The main climax now stands out. Bar residuals against a fit of bar level to the printed dynamic and the number of staves playing: bar 160 +1.8 (c00) -> +5.6 dB, bar 161 +0.7 -> +4.9. The recapitulation's second theme is +2.7 dB.
- Delivered file: LRA 17.3 -> 15.0 LU; motion (dS4 p90 / 1 s-20 s) 9.55/5.00 (c00), 8.55/4.48 (c22), 8.69/4.54 (c27), against Brahms 1/ii 8.55/4.56.
- Brightness follows loudness: centroid slope 0.24 (c00) -> 0.296 octave per 10 LU (Brahms 4/i 0.297, Brahms 1/i 0.462).
- Loud tutti 160-250 Hz re 250-2000 Hz: -12.9 (c00) -> -10.3 dB (Dvořák -7.7).

**The large-scale shape has not moved (measured).**
- Section power means (master RMS dB), c00 / c22 / c27: Lento -31.0 / -30.7 / -30.8; first theme -20.7 / -20.5 / -21.0; second theme -30.7 / -30.2 / -30.1; development -21.2 / -20.3 / -20.6; recapitulation second theme -20.8 / -17.9 / -18.1; Tempo I (179-182) -41.4 / -40.7 / -42.7.
- Bar-level fit: 2.61 / 2.62 / 2.66 dB per dynamic step, residual SD 3.04 / 3.12 / 3.16 dB.
- Since c22 the work has been note-level (joins, accents, fugato steps, leads). The one passage where the full orchestra still does something the score does not ask for is letter G (finding 1).

**BRIEF item 7 passes (measured).** Master autocorrelation at 3.95 s, 100-300 Hz band / spectral centroid:

| Passage | c22 | c27 |
|---|---|---|
| Lento 5-12 | -0.10 / 0.00 | -0.10 / 0.01 |
| Second theme 47-55 | 0.22 / 0.07 | 0.18 / 0.05 |
| 160-164 | -0.09 / 0.45 | 0.15 / 0.14 |
| 175-178 | -0.03 / 0.37 | -0.01 / 0.37 |
| Tempo I 179-182 | -0.34 / -0.12 | -0.34 / -0.12 |

The 175-178 centroid value comes from the bass clarinet (0.49 / 0.58 on its stem) and the celli in unison with it. They change pitch every 4 qn, which is 3.33, 3.33, 3.57 and 4.30 s on the c27 map, so the period is the note rate and not a sample loop (inferred). No change asked.

**BRIEF item 8 passes (measured).** 2-5 kHz from -10 to +80 ms against +120 to +400 ms on the 563 printed accents with a body above the stem's floor (median / p90): strings -1.3 / +1.8, winds -2.7 / +1.0, brass -4.2 / +0.5 dB (c22: -3.1 / -5.2 / -4.8).

## 1. Letter G, bars 117-120 (qn 464-480): the ff tutti lands and then sags 2-2.5 dB for three bars, because every held bass and harmony note swells and fades together (measured; fix simulated as a level equivalent)

**Where.** Every staff is ff from bar 117 (score p. 10), with no hairpin until the allargando of bar 121 and the fff of bar 122. The bassoons, contrabassoon, bass clarinet, tuba, bass trombone, Trombones a2 and the horns hold whole or tied notes; violins and Flute 1/Oboe 1 have the accented tune.

**Evidence: master K, 2 qn windows.**

| qn | 462 | 464 | 466 | 468 | 470 | 472 | 474 | 476 | 478 | 480 |
|---|---|---|---|---|---|---|---|---|---|---|
| c00 | -20.9 | -18.6 | -19.8 | -19.7 | -21.1 | -21.5 | -22.0 | -20.8 | -21.8 | -20.0 |
| c22 | -19.1 | -18.1 | -18.5 | -19.1 | -20.2 | -20.6 | -20.6 | -19.9 | -20.2 | -18.0 |
| c27 | -19.1 | -18.6 | -19.4 | -19.2 | -20.7 | -20.5 | -21.2 | -20.4 | -20.7 | -18.7 |

- The arrival is only +0.5 dB over bar 116, and the plateau then sits 2.0-2.6 dB under the arrival. It has been this way since c00.
- Stems, 468-476 minus 464-466: Contrabassoon -5.2, Bassoon 2 -5.0, Bassoon 1 -4.2, Bass trombone -4.0, Oboe 1 -3.9, Violas -3.5, Horn 4 -3.3, Horn 3 -2.7, Violins I -2.6, Bass clarinet -2.5 dB.
- **Cause (measured in parts.json).** The long-note swell on held notes. Bassoon 2, Contrabassoon, Tuba and Bass clarinet share one CC11 curve, 114 at 464 -> 118 at 468 -> 109 at 474. The volume follows it: Bassoon 2 +8.8 dB at 468 -> +3.2 at 474, Contrabassoon +8.3 -> +3.6. The notes from 468 (Bassoon 1, Trombone 1, Bass trombone, Horns a2) fall 2.7-3.6 dB-equivalent in the same way.
- I scanned every held note of 2.5 s or more at CC11 100 or more. This is the only place in the movement where three or more tracks fall 2.5 dB or more with no printed decrescendo. Bars 41 and 162 also fall, but there the decrescendo is printed.
- Inferred effect: the strongest ff before bar 122 deflates as a block, with all held voices swelling and fading in step. That sounds like one machine envelope, not players holding a ff, and it takes away the build into the allargando.

**Fix.** `build/score_config.py`: `ARRIVAL_HOLD_SPANS = [(464.0, 480.0)]`. This is the generic c20 mechanism in `score_to_parts.py` (line 337). It is empty in movement I. Long notes starting in the span take the swell_sost contour (+4 CC by 40%, held, rising into the next note) instead of the swell and taper. Keep the c26 letter-G roles (Horn 3 -3.5, Horn 4 -2, Tuba -3) as they are. B's Flute 1/Oboe 1 roles for the same bars (B #2) act on other tracks and are compatible with this fix.

**Simulated level equivalent.** I could not simulate the CC11 change itself. I approximated it as +1.5 dB on all non-percussion stems, ramped in 466-470 and held to 484 (delivered file):

| | bar 116 | 117 | 118-120 | 121 | S max 122 | S max 160 |
|---|---|---|---|---|---|---|
| c27 (M median) | -14.9 | -14.9 | -16.8 | -14.8 | -11.05 | -10.02 |
| simulated | -15.4 | -15.2 | -14.6 | -14.5 | -11.36 | -10.11 |

- Limiter 2.3 -> 1.9 dB; LRA 15.0 -> 15.1 LU; span 19.9 -> 19.8 dB; motion 8.69/4.54 -> 8.56/4.47 (-0.13, inside the 0.2 rule).
- A version that returned to 0 at 480 put bars 118-120 0.6 dB over bar 121. That is a reversed crescendo into the allargando. The hold must therefore run into bar 121, or the allargando must rise from the held level.

**Targets.**
- Master K 468-480 within 1 dB of 464-466.
- Bar 121 at or above the plateau, and bar 122 above bar 121.
- 160 > 122 > 167-170 in the delivered file; limiter 3 dB or less.
- Re-measure the melody (Violins I) over the held horns with B's method.
- If the swell_sost +4 CC rise overshoots on the contrabassoon or tuba, cut them with `LEVEL_SHAPES` on those two tracks instead of dropping the span.

## 2. Letter F, bars 97-102 (qn 384-408): the violas' f eighth-note motor has no beat (measured; audibility inferred)

**Where.** Violas, 48 unslurred, unaccented f eighths under the ff tutti tune (score p. 8).

**Evidence.**
- Stem level, first 80 ms of each note: beats 1 and 3 minus the other eighths is -0.02 dB, and the residual SD is 1.56 dB. The violas sit -16.4 dB re master.
- The same measure inside the existing `METRIC_BOWED` spans: violas 552-567.5 +1.1, 272-284 +0.75; basses 104-124 +2.41, 520-536 +1.64.
- Bars 97-102 are outside every `METRIC_BOWED` span. The figure therefore plays as an even row of samples: round-robin scatter with no grouping.

**Fix.** `build/score_config.py`, after line 334: `METRIC_BOWED["Violas"] = METRIC_BOWED["Violas"] + [(384.0, 408.0)]`, with the existing `METRIC_BOWED_DB` (down +1.0, mid +0.5, off -0.5). The notes are eligible: no slur or accent events in `mockup-events.tsv` for Vla 384-408. In mvt I c08 this took the violas' downbeat contrast from +0.61 to +0.92 dB.

**Targets.**
- Beats 1/3 minus the other eighths +0.7 dB or more.
- Violas' mean level over 384-408 within 0.3 dB of c27. The steps average about zero; check this.
- No new join or detach dips. Re-run A's stroke checks on these bars.

## 3. The loud tutti still lacks 160-250 Hz body, and the band now has only three owners (measured; fix is a test)

**Evidence.**
- **Loud frames, re 250-2000 Hz:**

  | Band | c00 | c22 | c27 | Dvořák |
  |---|---|---|---|---|
  | 160-250 Hz | -12.9 | -10.7 | -10.3 | -7.7 |
  | 100-160 Hz | -15.6 | -12.7 | -12.9 | -12.3 |

  Loud minus soft at 160-250 Hz: c27 -0.3 dB, Dvořák +4.9.
- **Third-octaves re 1 kHz, 125 / 158 Hz:** c27 -5.5 / -4.1; Brahms 1/i +1.6 / -1.0 (same key, C minor); Brahms 4/i +2.1 / +0.4.
- **Loud-minus-soft at 157 Hz** (`measure.py`): c27 -3.9, Brahms 1/i +2.8, Brahms 4/i +4.2.
- **Who supplies 160-250 Hz in loud frames:** celli 43%, basses 22%, timpani 18%, tuba 5%, contrabassoon 4%, violas 4%, trombones 4%. The rest have almost nothing there. Their own 160-250 Hz re their own 250-2000 Hz: bass trombone -19.3, bassoons -18/-19, Trombone 1 -15.4, Horn 4 -16.5 dB.

**The c24 C #5 plan does not work (simulated).** In the existing loud-EQ windows I applied:
- bells on violas 170 +3, bassoons 150 +3, trombones 160 +3, bass trombone 140 +3, horns 3/4/a2 160 +2.

Loud 160-250 rose only +0.14 dB, because those tracks hardly carry the band. Do not spend a cycle on it.

**The only effective option (simulated, test).** A second band in the loud-EQ windows (the shared `loud_eq` points, qn 92-104 ... 660-680):

| Change | Loud 160-250 Hz | Loud 100-160 Hz | 60-100 Hz | Stem energy | Window level | Master sample peak |
|---|---|---|---|---|---|---|
| Celli bell2 200 Hz +3 (1 oct), added to the existing `loud_eq` spec (one free band, no new FX) | -10.27 -> -9.17 | | | celli +1.8 dB | +0.18 dB | 1.541 -> 1.628 |
| Plus basses 180 Hz +3 (1 oct) | -10.27 -> -8.39 | +0.6 dB | +0.2 dB | basses +1.9 dB | +0.31 dB | 1.639 |

- Soft frames are unchanged in both.

**Caution (inferred).**
- Both tracks already carry large low-mid boosts: celli static 170 +3 (1.5 oct) and 125 +3, loud 150 +6; basses static 180 +4, loud 160 +6. A third boost risks a boxy tone.
- Part of the gap is the voicing (LEARNINGS 14: the climaxes leave 90-180 Hz to the basses' second harmonic and the timpani).
- Run it only as a test with the celli alone first, in a cycle without other celli or basses changes.

**Targets.**
- Loud 160-250 Hz at least +1 dB; soft unchanged.
- 60-100 Hz +0.3 dB or less.
- Celli K over the melody passages they do not lead (bars 27-31, 117-120) +0.5 dB or less, offset with a role if needed.
- Limiter re-measured (the peak rises 0.5 dB at 636).

## 4. The delivered p10-to-max span is 19.9 dB, over the 16-19 dB target, and the frames under p10 have moved to Tempo I (measured; fix simulated)

**Evidence.**
- Delivered short-term loudness frames under the 10th percentile, by bar:
  - c22: 179-182 had 137 frames, bars 1-5 had 75, bar 14 had 42.
  - c27: 179-182 have 203 frames, bars 1-5 have 102, bar 14 has 41.
- Tempo I S median: -29.5 LUFS (c22) -> -31.2 (c27), from c26's -2 dB `_coda26`. That is 11.4 LU under the integrated level.
- Bars 175-178 went from -26.6 to -28.0.

**Fix (small).** `LEVEL_SHAPES["_all"]` += `[(711.0, 0.0), (712.0, 1.0)]`, held to the end (Tempo I only). It does not change c26's solo/chorale relation in 171-178.
- Simulated: span 19.9 -> 19.5 dB; Tempo I S median -31.2 -> -30.2 LUFS; LRA 15.0 -> 14.7 LU; limiter unchanged.
- +1.5 gave 19.4 dB: the rest of the excess is bars 1-5 and 14, the printed ppp/pp of the Lento. Leave those.
- Target: span 19.5 or less with 160 > 122 > 167-170 unchanged.

## Smaller items (measured; no change proposed)

- **Bars 26-31.** After the bar-26 ff chord the ff tune of bars 27-30 sits 3.7-5.3 dB under it (c00 4.0-7.5). The brass are printed f there and the chord is a full tutti stroke, so this is in the score. B's balance work covers the tune.
- **Clarinet 1 at letter G** plays the oboe's notes in unison, printed f against the oboe's ff, and sits 13 dB under Oboe 1. It is printed and inaudible as a separate line. B #2 raises Oboe 1.
- **Cutoff decay.** The one tutti cut-off `measure.py` finds falls 20 dB in 0.59 s (references 0.485-0.49 s). The c20 C #5 hall `fx_volume` test (0.19 -> 0.16) is still open. It would need every fit redone, so it is not worth it this late.

## Do not touch

- Item 7: the re-bow, breath-split and loop work.
- Item 8: the accent swells and their fits.
- The delivery settings with MOM_CAP_ABOVE 6 and the top ride; the climax order 160 > 122 > 167-170 > 26.
- The c26 letter-G roles; the c27 fugato steps, arcs and leads.
- The basses' low bells (61.7/73.4/87.3 Hz) and the loud-EQ windows.
- `_coda26` over 175-178.
- Every do-not-touch item in HISTORY.md for c27 and earlier.
