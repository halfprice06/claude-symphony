# Cycle 42, critic A: articulation and phrasing (render c41)

Everything was measured on the c41 final stems and master (`cycles/c41/render/`; the stems include their hall share and sum to the master exactly), with c39 and c40 renders for comparison. Each stem is timed against the parts.json of its own render (`cycles/c4x/rendered_build/parts.json`; for c39, `cycles/c40/before/`). Levels are RMS dB in 30 ms windows unless stated otherwise. "Measured" means a number from the audio or the data; "inferred" means reasoning from those numbers or from the manual.

## Manual notes (May 2021 HO manual, A1: PDF pp. 89-94, read in full)

| Manual says (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| A divisi patch records only the left or right chair of each stand, with Close mics only, and "the loudness of a divisi part is not much less than if the whole section were playing" (p.89) | Violin I solo (1st Vln DIV A, bars 17-22), Violoncellos div (DIV A, bars 18 and 21-22, coda 4 soli), Violins II div (DIV B, bars 37-40), Violas div (DIV B) | Yes. The div tracks carry their own gains (+4 to +8.5 dB) and a 0.5 hall send in place of the missing Main mic. The basses' "4 soli" (bars 65-70, 87-92) still plays the full section at -3 dB, although Basses Divisi DIV A is installed (MANUAL-GAPS #8). |
| You can mix the divisi Close mics with the section's other mics by adding the same articulation from the non-divisi patch and adjusting its level (p.90) | the div tracks | Partly. The mockup uses more hall send instead of a Main layer from the section patch. |
| Détaché has no legato connection to the next note, a well-defined end, and works when cut short (p.91) | the violas' portato eighths, bars 48-51, on Detache | Yes (finding list, "Do not touch"). |
| Sustain samples loop; bow direction alternates by round robin; finger position (not on the basses); three vibrato levels (p.91) | every re-bow on Sus MAX; the CC70 and CC1 lanes | Yes. The up/down round robin is visible on the stem of the regularly spaced Violoncellos div coda pedal: band-level autocorrelation 0.75 at a two-piece lag (4.7 s). The master shows nothing at that lag (-0.17). There is no 3.95 s loop pulse anywhere (below). |
| Flautando exists only in 2nd Violins, with no vibrato control and no round robin (p.92) | Violins II div "sul tasto", bars 37-40 | Yes. Re-bows on the same Flautando sample dip -1.0 to 3.9 dB. |
| Pizzicato samples are RR x2/x4 (p.92) | violas, bars 41-44; basses, bars 37-44 | Yes. Peaks fall +0.02 to +0.14 s after the score onset (violas median 0.066 s, basses 0.093 s). |
| Repetitions: about a dozen tempo-synced repeats per sample (p.94) | | Not applicable. No passage in v600 repeats one string note fast enough to use it; every repeat here is 2-3 slow notes (S1 is handled below). |
| Marcato, spiccato and staccato rows (p.93-94) | | Not applicable. v600 prints no string staccato or marcato; the only accents are Trombone 1's. |

MANUAL-GAPS checked: #8 is still the only untried patch gap in this lens (finding 6). #2 (repetition rows) does not fit: see the p.94 row above.

## Findings, ranked by what a listener would hear

### 1. The bar 66 niente no longer fades. The strings hold their level for two beats, then drop in the last beat (measured)

Where: Violins II, Violas, Violoncellos, qn 223-226 (bar 66, the printed down-bow on the tied note and decrescendo to niente, just before Horn 1's retransition).

The re-bow fill lists at 223.0 in `build/rebow_fills.json` were refitted in c40 (after the 150 ms caps) and kept in c41. Their hold, from +1.5 s to the note end, is now Violins II +6.94 dB, Violas +8.56 dB and celli +1.17 dB. In c39's state (`cycles/c40/before/rebow_fills.json`) the holds were +0.86, 0.0 and -4.78 dB. `fit_rebows.py` subtracts only the CC11 plan (0.25 dB per CC) as the planned diminuendo. It does not subtract c30's niente CC7 lane (127 -> 25 over 223.5-226), so the hold cancels the fade the CC7 lane was added to make.

Level per 0.5 qn from qn 222 to 226 (dB):
- Violins II, c39: -49.1 -48.9 -48.4 -49.9 -51.0 -52.2 -58.3 -61.1 -71.3
- Violins II, c41: -49.1 -48.4 **-45.4 -46.2 -44.9 -45.6** -52.0 -55.0 -67.4
- Violas, c39: -54.0 -54.0 -54.5 -56.1 -59.5 -61.7 -70.3; c41: -54.0 -54.2 -54.4 -55.7 -55.3 -54.9 -61.8
- Master, c39: -45.8 -47.1 -48.5 -49.6 -53.0 at 223-225.5; c41: -43.3 -44.2 -43.2 -43.8 -48.9

In c41 the master over 223-225 is 2.5-5 dB louder than in c39 and flat. The whole diminuendo now happens in the last beat. c41's two-point check (223 against 225.5) read 6.4 dB, which hid this shape. There is also a +3 dB step up in Violins II at the re-bow itself, inside a decrescendo.

Fix: in `build/rebow_fills.json`, set the 223.0 lists of Violins II, Violas and Violoncellos from +0.5 s to the end back to c39's holds (+0.9 / 0.0 / -4.8 dB), keeping c41's first 0.5 s, which fills the bow-change hole. That is a level-only change, so stem_fix can apply it. The generic fix is in `tools/fit_rebows.py`: add each note's CC7 lane (in dB) to the planned level beside `PLAN_DB_PER_CC`, so that later refits do not fight a CC7 fade. Check: each stem falls at least 8 dB from 223.25 to 225.0, and the master falls steadily from 223.

### 2. Extra check: release caps. Raise pp/p to 600 ms on every string track and keep mf-ff at 300 ms (measured and inferred)

The phrase ends split into two groups (`m41.py`'s selection: a string note end followed by at least 0.6 s with no note on the track; t20 is the time from the played end until the level is 20 dB under the 0.15 s before it, 20 ms steps).
- **15 ends react to the cap.** All are pp/p (CC11 10-46), Sus-row or Flautando ends: Vln I 7.35; Vln II 5.15/56/87/122/271; Vla 5.7/169.5; Vc 136; Cb 6.25; Vc div 53/284.14; Vln II div 122; Vla div 72/87. Median t20: c39 (uncapped) **0.50 s**, c40 (150 ms) 0.20, c41 (400 ms, or 300 on the div tracks) **0.34**. t10: 0.28 against 0.20. The uncapped ppp ends ran long: Vla 5.7 0.74 s, Vln I 7.35 0.66, Vc div 284.14 0.58, against 0.43-0.58 in recordings.
- **18 ends do not react** (0.35-0.36 s in all three renders): legato-row and Detache ends.
- **Only 2 ends are loud** (Cb 212 pizz, Violas div 266 at CC11 113). The mf-ff cap shapes no phrase end in this movement. Lengthening it would only shorten the gaps of the mp-f strokes (Vc 148, Vla 253, Cb 253, Cb 81 at CC11 58-66).

On the reacting ends, t20 tracks the cap at about 0.85 x the cap: 0.34 s at 400 ms. 600 ms should give about 0.50 s, the middle of the 0.43-0.58 target (inferred). Removing the cap entirely would bring back the 0.6-0.75 s ppp ends, including the final chord's (c39 stems 0.68-0.82 s, although c39 also had the longer hall IR).

Change in `build/mix.json`:
- Violins I, Violins II, Violas, Violoncellos, Double basses: the second `sus_release_cap_ms` spec `{"ms": 400, "dyn": ["pp","p"]}` becomes 600.
- Violin I solo, Violoncellos div, Violins II div, Violas div (now 300 ms on every layer): split into `[{"ms": 300, "dyn": ["mf","f","ff"]}, {"ms": 600, "dyn": ["pp","p"]}]`. The divisi ends are still short (Vla div 87 0.24 s, Vc div 284.14 0.28 s), and Violas div holds the final chord's A flat 3.
- Then refit the re-bows with c41's re-levelling rule (`relevel41.py`; release changes overshoot the old fills: 50 attack peaks in c41's first render), and keep the bar 66 holds from finding 1.

Effect on S1 (inferred from the release slope; measured baselines): at a 0.03-0.06 s gap, the deepest point of a soft stroke's dip falls about 0.1-0.15 s after the old note-off. There, a linear 400 ms release is down 2.3-4.1 dB and a 600 ms release only 1.5-2.5 dB. Expect about 1-1.5 dB less separation on pp/p strokes and soft re-bows, and nothing on mf-ff strokes. Their master dips now are Vln II 44/45/50 3.5/2.8/3.4 dB, Vc 128 4.5, Cb 144/156/168 3.2/3.7/4.1, so Vln II 45 and Cb 144 would fall under about 3 dB. Re-bow dips get shallower, which helps (final chord median 3.6 dB now).

Compensate with the pre-release CC11 fall that worked on the basses (c41: 156/168 dips 5.7/7.1 dB at 400 ms). In `build/score_config.py`, `STR_REP_NEW_BOW["sus_fall"]` adds Violins II, Violas and Violoncellos at `{"cc": 8, "s": 0.06, "max_cc": DYN["p"]}` and raises the basses to 12 CC. In `tools/score_to_parts.py`, apply `sus_fall` to the stroke and portato-stroke paths as well as the sus gaps: Vln II 44/45/50 and Cb 144 are strokes, which the rule does not reach today.

Fresh strokes c41 refilled (stem per 50 ms from -0.25 to +0.6 s against the body, and master minimum at the repeat):
- **Violins II 44.** The stem dip is 11 -> 5 dB; master -3.9 -> -3.5. On time: body -3 dB at about +0.15 s. Keep it.
- **Violoncellos 128.** The stem now sits +4 dB at -0.10..-0.05 s and dips only 2-3 dB after the beat (c40: 10 dB); master -4.5 dB in both renders. Acceptable, because the master separates it.
- **Violas 69 and 248.5, and Double basses 144:** see finding 3.
- **Double basses 156 and 168** (not refilled; `sus_fall`): stem dips about 6 and 7 dB, master -3.7 and -4.1. Keep them.

### 3. Three soft printed repeats now have no audible re-attack: Violas 69 and 248.5 (no lead, fills start before the beat) and Basses 144 (attack cut) (measured)

- **Violas 69** (C4 quarter repeated after the bar 23 chord, p) and **Violas 248.5** (E flat 4 eighth on a new slur after the 248 eighth, p, CC11 34). Both are STR_REP_NEW_BOW soft re-bow pieces: gap 0.036 s, no lead. c41's post-hall LEVEL_SHAPES_S (+4 dB from -0.04 s; +6 dB from -0.06 s) start before the onset, so they lift the old note's release and the gap. The stems now read +3/+4 and +6/+5 dB over the body at -0.05..0 s, and the new note's slow Sus MAX attack only reaches its body at about +0.35..+0.45 s, with a 3-6 dB sag at +0.15..+0.35 s. 248.5 lasts only 0.58 s, so it never gets an attack. Master minimum at the repeat: +0.2 and -0.3 dB (c40 -0.1 and -0.3), so neither repeat can be heard in the mix.
- **Double basses 144** (B flat 1 repeated after the 4-qn 140 note, pp, new slur). The -5 dB shape over +0.06..+0.22 s removed the attack peak, and the separation went with it. The stem never falls more than 0.5 dB under the body (c40 -3 dB); the master minimum (-3.2 dB) comes from other instruments.

Fix:
- `build/score_config.py`: add Violas 69.0 and 248.5 to `DOWNBOW_STROKE_AT` (fresh Sus MAX after the 0.06 s gap with the 0.10 s re-tongue lead, as Violins II 44/45/50 already are), and delete their two c41 `LEVEL_SHAPES_S` entries. Movement I c45 measured fresh p strokes perceived about +90 ms late with 0.07-0.10 s leads. If 248.5 still sounds late, give it +0.08 s more (`REATTACK_LEAD_AT`), but leave the 248 eighth at least 0.2 s long (Movement I c45: a soft eighth shortened to 0.11 s barely sounded).
- Basses 144: replace the -5 dB shape with a CC11 fall into the gap on the 140 note (the `sus_fall` extension of finding 2, 10-12 CC over 0.06 s). If the c40 attack peak (+5 dB at +0.10..+0.25 s) needs taming, cut 3 dB over +0.12..+0.30 s only.

Pass for all three: a stem dip of 5 dB or more inside the gap, the master at least 2.5 dB down at the repeat, and the body -3 dB point before +0.2 s.

### 4. Two viola tracks step up 4-5 dB at the start of the bar 91 morendo (measured)

Where: Violas (piece 296.9-299.2, E flat 3) and Violas div (re-bow 298.3, A flat 3), qn 298 (bar 91 opens with a decrescendo; morendo).

- Violas per 0.25 qn, 297.75 -> 298.75: -55.0 -> **-51.9 -51.5 -50.3** -> -54.2. The vol_db fill moves from -3.0 to -0.6..-1.7 dB at 298.
- Violas div: -57.2 -> **-51.4** at 298.25. Its fill goes from -6.4 to +2.3 dB across the 298.3 re-bow.
- The same bump was in c39 (Violas -55.2 -> -51.3; Violas div -56.0 -> -55.1 -> rise), so it is a fit artefact, not a sample swell.
- The master is flat from 297 to 298 (-43.4, -43.6) where the decrescendo should begin, then falls 7 dB to 301. `--hold-max-after 301:0` covers only the pieces from 301.

Fix: `tools/fit_rebows.py ... --hold-max-after 298:0` (the start of bar 91's hairpin) in the next refit. Or, by hand in `build/rebow_fills.json`, hold Violas 296.9 at -3.0 dB to its end and keep Violas div 298.3 at or under -6 dB. Check that no string stem rises more than 1 dB from 297.5 to 298.75.

### 5. Trombone 1's unaccented 215.0 is now the brightest attack of the quotation, on the stem only (measured; low priority)

2-5 kHz energy over the first 80 ms against the body (stem):
- 212.5: -6.3 dB; 213 (accent): -3.8; 214.5: -1.2; **215.0: +6.4** (c40 +3.4; velocity 112 -> 124 in c41 A #2); 215.5: +3.7; 216: -7.2; 217.5: -0.5; 218 (accent): -10.5.
- The accents carry weight without bite: broadband bodies +3.7 dB (213) and +2.0 dB (218) over their neighbours, which meets brief item 9.
- In the master, the 2-5 kHz jump at 215.0 is -0.8 dB, because the tutti tremolo covers it.

So nothing in the mix shows the bright attack today. If a listener or critic hears 215.0 sticking out, use velocity 118 with c41's held +2.5 shapes (`VEL_SET["Trombone 1"][215.0]`) and check that the 214.875 dip stays under 2 dB. Otherwise leave it.

### 6. Patch choice: the basses' 4 soli is the one passage where a better installed patch exists (inferred)

- I found no better Hollywood Orchestra patch for the other passages in this lens:
  - The bars 17-22 violin solo is already on the half-section DIV A, and Hollywood Solo Violin is not installed.
  - Violins II div sul tasto is on the library's own Flautando row (p.92).
  - The library has no muted string samples, only the CC15 script (DIGEST 5.2, 2021 p.144), so no con sordino patch exists for the strings' coda mutes.
  - Repetitions does not fit slow 2-3 note repeats (p.94).
  - The celli 4 soli already plays on DIV A (c33).
- **Double basses, 4 soli, bars 65-70 (qn 220-238) and 87-92 (286-304).** Here the full section plays at -3 dB. `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` gives four players' colour; per p.89, nearly the section's loudness, so level matching is simple. Cost: one Close-only instance (about 0.7 GiB against the 44-45 GB settled), or a second-session pass (MANUAL-GAPS memory plan), plus a refit of the basses' pedal fills with the c41 re-levelling. It changes timbre only; the pedal's level is on target. Do it only after findings 1-4, and in the same cycle as the release-cap refit, so the basses' fills are refitted once.

## Checked and working (measured)

- Violas portato bars 48-51 on Detache: perceived onsets on the beat (peak -6 dB point at -0.06..+0.04 s), even levels (-47.9 to -50.6 dB over the first 0.4 s), 27-40 dB down between eighths, 7-14 dB under the cor anglais.
- Re-bows of long notes:
  - No sample-loop pulse: 100-300 Hz band and centroid autocorrelation at 3.95 s within ±0.25 on every string stem and the master, over the opening chord, the Cb pedal 220-238, the coda pedal and the final chord.
  - Final chord re-bow dips on the master 3 dB or less (50 ms windows). The deepest stem dip is Violins I 295 (printed down-bow), 9.5 dB in 30 ms windows but 3 dB in 50 ms, with the master at -1 dB.
  - The opening chord and the 4 soli pedals are within 1-5 dB on the stems.
- Keyswitches: none closer than 0.015 qn before its note on any track; no chord on a legato row; no same-pitch overlap.
- Mutes: every CC15 change falls in a rest. The lanes match v600, including Horn 4's part-only "con sord." at 286 and the unmuted celli and basses in the coda.
- Harp arpeggios: rolled from the bottom, 40 ms per note. Tenutos in bars 61-62: under molto sostenuto they are tied or held, and the merged wind ties are correct.
- The bar 63 sf: string stems +1.5..+6 dB over the bar before, master 2-5 kHz +1 dB.

**Do not touch:** violas portato on Detache with its CC7 and leads; pizzicato; Violins II div Flautando re-bows; the final chord and opening re-bow spacing (no loop pulse); Trombone 1's accents (Sus MAX, CC7 110/120, swells) and the 214.5/215 shapes; the CC15 mute lanes and Horn 3/4 mute_eq; the basses' `sus_fall` at 156/168; the Violins II 44 stroke and fill.
