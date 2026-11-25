# Cycle 29, critic A: articulation and phrasing (on the c28 render)

Sources: `cycles/c28/render` stems and master (c27 stems for comparison), `build/parts.json` (equal to `cycles/c28/rendered_build/parts.json` apart from the post-render Violas role), `build/score_config.py`, `build/rebow_fills.json`, `build/mockup-events.tsv`, `build/sections/coda.ily`, `tools/score_to_parts.py`, `tools/fit_rebows.py`, May 2021 HO manual PDF pp. 95-99 (row A2 of `loop/MANUAL-READING.md`), `loop/MANUAL-GAPS.md`, `mockup-kit/LEARNINGS.md` sections 5-9, movement I `loop/LEARNINGS.md` (c11, c35 harp). Times are score qn unless marked s. Levels are stem or master RMS: 30 ms windows for joins and attacks, 0.12 s for re-bows, 0.05-0.3 s for traces.

## Manual notes (A2, PDF pp. 95-99)

| Manual (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Pre-recorded runs, one octave each, 1st Violins, Violas and Celli only (pp.95-96) | No octave runs in v600 | Not applicable. |
| Slur Runs (1st/2nd Violins): fast notes, slurs and sustains in one patch, sustains on CC1 (3 vibrato levels) and CC11 (5 layers), "a minimum speed is sixteenth notes ... at about 125 beats per minute" (pp.96-97) | The three-note triplet run into bar 79, Violins I/II qn 261.5-261.83 (about 0.20 s per note at the local 50 bpm) | Not used: the run plays Sus MAX. The 2nd and 3rd notes (G6, A flat 6) sit 7-10 dB under the previous pitch in their own first 0.05 s on the Violins I stem (measured). The notes are slower than the Slur Runs minimum (0.12 s), so the manual expects a less realistic result there. The flute doubling is clear (own pitch 1.4-8.8 dB over the others), which covers most of it. Not ranked. |
| Unmeasured tremolo: no velocity response, CC11 crossfades dynamics and timbre so long tremolos can swell or fade (p.97) | Violas 204-212, all strings 212-218 (sf, decrescendo) | Yes. The tremolo row carries CC11 114 -> 46 over 212-216 on Violins I. The stems fall 12 dB in the first beat and then decay evenly. There is no re-bow inside a tremolo. |
| Measured tremolo (TS) | Nothing printed: "trem." with 32nd strokes is unmeasured | Not applicable. |
| Repetitions (Violas, Basses only): one note re-played about a dozen times in just over a second, tempo-synced, CC11 over 3 layers (p.98) | No printed repeated-stroke figure. The violas' portato eighths in bars 48-51 are single notes with rests between them. | Not applicable. MANUAL-GAPS #2 does not need this row for the strings. The Detache row chosen in c28 is the right patch (finding 5). |
| Sul ponticello (violas only) (p.98) | Not printed | Not applicable. |
| Legato types: slur, portamento, bow change; the basses have Legato Slur only (p.98) | Vln I/II Leg Port MAX at 82 and 172 (`PORT_TARGETS`); Leg BC MAX for connected unslurred notes (27-37 notes per section); Basses Leg Slur MAX on 6 notes | Yes. |
| A legato transition needs no gap between notes, and the first note of a phrase has no legato; legato patches are monophonic unless CC22 is 64-127 (p.99; the 2025 p.91 polarity applies) | Every Leg row | Yes. parts.json has no chord and no simultaneous onset on any Leg row: 0 cases on 32 tracks (measured). No overlap is longer than 0.12 qn. CC22 is not used, and it is not needed. |
| Legato Slur Staccato: a stronger attack on the first note of each legato phrase (p.99) | Phrase starts after rests in the cantabile string lines | Not used. Soft string phrase starts already take entry leads and fills. Nothing measured asks for it. |
| Legato Bow Change: "the sound of the bow changing direction" inside a legato passage (p.99) | Printed bow changes inside held notes: the re-bows | The re-bows play Sus MAX same-pitch re-attacks with fitted level shapes, not Leg BC transitions. That works where the shapes fit (median stem dip 1.7 dB). It fails where the shapes are stale (finding 1). |
| MANUAL-GAPS #8 (4 soli on DIV patches) | Cb 220-238 and 286-304, Vc 274-286 | Not used, and still open (smaller observations). |

## Findings, ranked by what a listener would hear

### 1. Stale re-bow shapes: Violins II bars 15-17 swell 8-15 dB on a held pp note and then drop into a 15-18 dB hole; the basses' bar 65-66 pedal steps 6 dB

- **Where.** Violins II, qn 42-53 (con sord., pp, under Oboe 1's dolce solo and then the Violin I solo). Double basses, qn 221-224 (the start of the 4 soli pedal, bar 65-66).
- **What is wrong (measured).** c28 ran `fit_rebows.py 27` first and then changed the re-bow points: `REBOW_AT["Violins II"] += [45, 51]` replaced the automatic points 44.341 and 50.352, and `rebow_moves.json` moved the basses' 222.452 to 221.8. `build/rebow_fills.json` still holds the three old keys and has no shape for the three new points. `score_to_parts.py` applies every key whether or not a re-bow is there (line 4046), so:
  - **Violins II 44.34-45.0.** The old shape (+6.5..+8.5 dB at +0.2..+0.6 s) lands on the continuous 42-45 note. The stem rises to -40/-41 dB at 44.5-45.0 (c27: -50/-47), level with Oboe 1's hairpin top (-41/-37 dB). The master is +3 dB at 44.5. c28's simulation had Violins II 6-7 dB under the oboe there. The render has it 0-4 dB under.
  - **Violins II 50.35-51.0.** The old shape (+10 dB at +0.3 s) lifts the held A flat to -41 dB at 50.5 (c27: -56), 2 dB under the Violin I solo (-39).
  - **The new, unfitted re-bows.** The Sus MAX piece at 51.0 then falls to -64 dB at 51.25: a 15.2 dB dip in 30 ms windows, 17.7 dB at 0.12 s, and the piece settles 9.8 dB under the level before it. At 45.0 the dip is 11.5 dB and the step -8.1 dB.
  - **What the listener hears.** Instead of the printed slurred portato (a soft re-articulation at 44, 45, 50 and 51), there is a bulge into the oboe's and the soloist's notes, followed by a hole.
  - **Double basses.** The unfitted re-bow at 221.8 dips 10.5 dB and steps -6.3 dB. The stale 222.452 shape (-5..+2 dB) is applied to the continuous piece after it.
- **Fix.**
  1. Run `tools/fit_rebows.py 28 build/parts.json --write --tracks "Violins II,Double basses" --hold-max-after 301:0` before any other change to these two tracks. It takes the shapes the c28 render carried, including the stale ones, out of the measured level (lines 120-135), so the pre-levels of 45, 51 and 221.8 are measured without the stale bumps. Then check that the keys 44.341, 50.352 and 222.452 are gone from `rebow_fills.json`, and delete them by hand if the tool kept them.
  2. In `tools/score_to_parts.py` at the REBOW_FILLS loop (line 4046), skip every key that has no re-bow in the track's current `rebows` list within 0.01 qn, and print `WARN {track}: REBOW_FILLS {key} has no re-bow`, as CRESC_FRONTS already does.
  3. In the actor's order of work, run `fit_rebows.py` after the last `REBOW_AT`, `rebow_moves.json` or `space_rebows.py` change, never before.
- **Check after the render.**
  - Violins II at 44.5-45.0 and 50.5 within ±2 dB of c27 (-47..-50 and -56).
  - Re-articulation dips of 3-6 dB at 44, 45, 50 and 51 (S1), and steps within ±2 dB.
  - Basses at 221.8: dip at most 4 dB, step within ±2 dB.

### 2. Trombone 1's quotation (bars 63-64, qn 212.5-219.5): the ff line sinks 4-7 dB in its middle, and the accent at 213 still blooms 0.45 s late

- **Where.** Trombone 1, qn 212.5-218. The trombone is the master in bar 64: master -24..-30 dB against the trombone stem -25..-31.
- **What is right now (measured).** c28's legato change worked. Pitch crossovers are at -0.01..+0.09 s. The re-tongued tenuto repeat at 216 dips 4.1 dB (S1 passes). 2-5 kHz front minus body is -5.3..+0.7 dB on every note, so there is no bite.
- **What is wrong (measured).** Everything from 214.5 to 217.95 is printed ff ("marcato"), and the decrescendo starts only at 218. CC11 is flat at 109-114, but the stem sinks:

  | qn | note | level |
  |---|---|---|
  | 214.5 | B3 | -24.4 dB |
  | 215.0 | B flat 3 | -30.8 dB (-29..-32 over 215.07-215.45) |
  | 215.5 | A3 | -27.5 dB |
  | 216.0 | A3 | -28.2 dB |
  | 217.0 | G sharp 3 | -29.2 dB |
  | 217.5 | A3 | -31.2 dB (-33 dB at 217.82-217.95) |
  | 218.0 | F3, accent | -25.2 dB |

  - The B flat at 215.0 is a weak sample on the B3 -> B flat 3 transition, 6 dB under both neighbours.
  - The A at 217.5 is the second note of the two-note slur `gis8( a8)`. The generic `SLUR_PAIR_RELEASE` (-2.5 dB from +0.10 s; the vol_db point -2.5 at 217.578) pulls it down on top of a weak sample. The F accent at 218 then jumps 8 dB over the 0.15 s before it, more than the 2-4 dB of BRIEF item 4.
  - The slurred accent at 213 (on Leg Slur MAX since c28) is on pitch at -0.01 s, but its level climbs from -26.0 (212.95) to a peak of -22.4 dB at 213.45 (+0.45 s) and falls back to -27 by 213.7. The +6 dB vol swell at +0.07 s (`ACCENT_DB_AT` 3 plus the role [212.4,213.6,3]) is hidden under the sample's own 3-4 dB rise, so the emphasis arrives as a late swell, not on the beat. c28's check (peak within +0.25 s) fails.
- **Fix (`build/score_config.py`).**
  - 215.0: `LEVEL_SHAPES_S["Trombone 1"] += [(215.0, [(-0.02, 0.0), (0.03, 4.5), (0.50, 4.5), (0.60, 0.0)])]`.
  - 217.5: `SLUR_PAIR_RELEASE_DB_AT = {"Trombone 1": {217.5: 0}}` (ff marcato, no taper into the accent), plus `(217.5, [(0.0, 0.0), (0.08, 2.5), (0.45, 2.5), (0.55, 0.0)])` in the same LEVEL_SHAPES_S list.
  - 213.0: replace the swell with an onset-weighted shape that counters the bloom. Set `ACCENT_SWELL_S_AT["Trombone 1"][213.0]` to None, or `ACCENT_DB_AT` 213 to 0, and add `(213.0, [(-0.02, 0.0), (0.03, 4.0), (0.18, 3.5), (0.45, 0.0), (0.7, 0.0)])`. Then the front is up while the sample is still low, and the shape is gone by the sample's own peak.
  - 218: `ACCENT_DB_AT` 218 6.0 -> 4.0, so the accent sits 2-4 dB over the raised 217.5.
- **Check after the render.**
  - Note bodies 214.5-217.5 within 3 dB of each other.
  - 213 level peak within +0.2 s of its onset.
  - 218 front 2-4 dB over the 0.3 s before it.
  - 2-5 kHz front minus body still at or under 0 dB.

### 3. Violas' pizzicato triplets, bars 41-44 (qn 124-137.67): the first and last beats fall under a velocity-layer edge and nearly vanish

- **Where.** Violas, Pizz RRx4, pp < p > pp under the cor anglais "solo, dolce cantabile".
- **What is wrong (measured).** The figure's velocities run 41-46 at pp and 47-53 at p. Peak levels on the stem (30 ms windows):

  | qn | notes | velocity | peak level |
  |---|---|---|---|
  | 124.0-125.67 | D flat 3, F3 | 41-45 | -58..-61 dB |
  | 124.0-125.67 | A flat 3 | 41-45 | -50.5..-51.8 dB |
  | 126.0-130.67 | | 47-53 | -38..-47 dB |
  | 134.0-137.67 (falling back to pp) | | 41-44 | -50..-60 dB |

  At one pitch, the step across 46 -> 47 is 5-8 dB: A flat 3 at v46 -50.5 against v48/v49 -42..-46; G flat 3 at v45 -49.4 against v47 -42.7..-44.9.
  - The printed pp < p hairpin becomes a 16-20 dB rise. The bar's first beat is a near-silence, and the low notes of the figure drop out entirely, about 20 dB under the cor anglais.
  - This was noted in c28's report but not acted on.
- **Fix.**
  - `VEL_SET["Violas"]`: set every pizz note at 124.0-125.67 and 133.33-137.67 to at least 48 (for example 48, 48, 49, 49, 50, 50 rising to 126, and 50 falling to 48 over 133.33-137.67), and keep 126-133 as they are.
  - If the low D flat 3/E flat 3/F3 notes are then still more than 6 dB under the A flat 3s, add per-note trims in `note_trims.json` (Violas, keys 124.0, 124.33, 125.0, 125.33, 134.33, 135.0, 137.33) without the 0.6 s ramp-in. Pizz notes need the trim from their onset (kit LEARNINGS 6).
  - Level only after that: a role over 124-126 and 134-138 if pp sits more than 6 dB under the p beats.
- **Check after the render.** Peaks over 124-125.67 within 4-7 dB of those at 126-128, and no note more than 8 dB under the figure's median.

### 4. Timpani, bar 52-53 (qn 168-172): the crescendo roll peaks 6-13 dB over the p stroke it leads to, so the arrival falls away

- **Where.** Timpani, the pp < roll at 168-172 into the printed p stroke on A flat at 172 (the a tempo downbeat of bar 53, the violins' theme entry), then "damp" at 173.
- **What is wrong (measured).**
  - The roll (Rls row, CC1 layers since c28) climbs to -41/-42 dB at 171.75-171.85. The volume envelope carries +14 dB at 171.875: the roll trim plus `timp_hp` 2.42.
  - The stroke (Lng row, v64) then reads -48.3 dB over its first 80 ms and -54.9 dB over +0.1..+0.4 s, against -42.4 dB in the 0.3 s before it.
  - The top of the crescendo sits 0.15 qn before the beat, and the downbeat it leads to is 6 dB softer at its front and 12 dB softer in its body.
  - The other two roll-to-stroke arrivals work. At 203 the f stroke is +8.2 dB over the roll's end, and at 262 the f roll is +3..+6 dB over the 261 crescendo.
- **Fix (`build/score_config.py`).**
  - Raise the stroke: `VEL_SET["Timpani"][172.0] = 72`, plus `LEVEL_SHAPES_S["Timpani"] = [(172.0, [(-0.02, 0.0), (0.0, 4.0), (0.6, 4.0), (0.9, 0.0)])]`.
  - Cap the crescendo's top: `LEVEL_SHAPES["Timpani"] = [[(170.5, 0.0), (171.6, -4.0), (171.94, -4.0), (171.95, 0.0)]]`, so the roll ends about 2 dB under the stroke's front.
  - Keep the dip at 171.95 that separates the roll from the stroke.
- **Check after the render.** The stroke's first 80 ms 2-4 dB over the roll's last 0.3 s. The stroke still under the violins' entry. The damp at 173 unchanged (the stem is -73 dB there now).

### 5. Violas' portato eighths, bars 48-51 (qn 152.5-167.5): Detache separates them, but the A3 eighths still peak in the second half of the note (S2)

- **What c28 achieved (measured).** On Detache the rests between eighths now drop 8-16 dB (c27: 3-10). The round robins alternate: A3 peaks at +0.34 and +0.43 s on alternate notes. The level is -43.4..-43.7 dB on the A3s (the -13 dB role).
- **What is still wrong (measured).**
  - All seven A3 eighths (152.5, 153.5, 154.5, 156.5, 157.5, 160.5, 161.5) reach body - 3 dB at +0.20..+0.24 s after the score onset. Their energy centroid over the first 0.45 s is at +0.19..+0.20 s. The eighth lasts 0.556 s at 54 bpm, so each portato stroke is heard about a third of the way into its own eighth, not on the "and".
  - The E flat 4 eighths depend on the round robin: 165.5 at +0.03 s, but 164.5 and 166.5 at +0.29 s.
  - The B flat 3, A flat 3 and D4 notes (158.5, 159.5, 162.5, 163.5) are at -0.01..+0.11 s, so they are fine.
  - c28's pass mark (body - 3 dB by +0.12 s on 12 of 15) is met on only 6 of 15.
- **Fix (`build/entry_leads.json` "Violas", extra seconds keyed by score onset).**
  - +0.10 s on the seven A3 eighths listed above, and +0.15 s on 164.5 and 166.5.
  - Keep each note's end where it is: the lead lengthens the note, and `ENTRY_LEAD_ROWS` already includes Detache.
  - Do not add a fill. These notes overshoot nothing, and a fill on a short detached stroke would blur the separation that c28 gained.
- **Check after the render.** -3 dB by +0.12 s on at least 12 of 15 eighths, with the rest drops still at least 8 dB.

### 6. Harp harmonics and the étouffez of bar 83 (qn 274-277): the three-note head is 9 dB uneven, and the damped plucked notes ring under it

- **Where.** Harp harmonics, A flat 4 - C5 - E flat 5 (`aes4.( c'8 es'4)`, p dolce, the theme's head). Harp, "R.H. étouffez" at 274.
- **What is wrong (measured).**
  - All three harmonics are at v58. Their peaks are -51.7 dB (A flat 4), -46.2 dB (the passing eighth C5) and -55.2 dB (the slur's arrival E flat 5). So the short passing note is the loudest and the arrival is the softest, a 9 dB spread inside a dolce three-note slur.
  - The R.H. notes plucked at 272-273.5 (A flat 3, C4, E flat 4, F4) still ring at -59.2 dB in the first 0.3 s of the harmonic, 7.5 dB under it. At 274.5 they are only 2.6 dB under (-64.8 against -62.2). The coda comment (c406) says the damp exists to stop exactly this, for example F4 ringing as a sixth over the tonic.
  - Cause: `HARP_RING_S = 0` and no `env_release_ms` in `mix.json`. So the patch's 3019 ms release stands, and a note-off never damps a string. Movement I c11 measured the same and fixed it.
- **Fix.**
  - `VEL_SET["Harp harmonics"] = {275.5: 48, 276.0: 64}`. The Harmonics patch moves about 0.55 dB per velocity step (kit LEARNINGS 9), so this is -5.5 and +3.3 dB, which puts the three notes within about 1 dB with the arrival not under the start.
  - For the damp: `"env_release_ms": 200` on the Harp track in `build/mix.json` (state change, full rebuild of Harp), and `HARP_RING_S = 2.0` in `build/score_config.py`. Then every harp note rings 2 s past its written end, cut at the "étouffez" (HARP_DAMP_TEXT "touffez" already matches it).
  - Check that "R.H." limits the damp to the right-hand staff. `HARP_DAMP_STAFF` keys on "(m.d.)", so add `"R.H.": 0`, or the L.H. A flat 1 pedal (271-277) is damped too.
  - Movement I's measurement: damped pitches fell 15-20 dB within 0.25-0.5 s, undamped ones stayed within ±0.5 dB.
  - The harp's other passages (arpeggios 18-40, 238-272) then ring 2 s past their written length instead of 3 s with the slow release. Compare their between-onset tails before and after.
- **Check after the render.**
  - Harmonic peaks within 2 dB.
  - Plucked harp at least 15 dB under the harmonic by 274.25.
  - The A flat 1 L.H. unchanged through 277.

## Smaller observations (not ranked)

- **Legato joins (measured, same method on both renders).** Joins dipping 6 dB or more fell from 130 to 82 of about 740 (auto fills). The rest are in Violas 20, Flute 1 11 (vibrato: only 3 remain at 6 dB or more on a 200 ms window), Violoncellos 11, Violins I 10. Only three cost the master more than 3 dB:
  - Violins I 177.0: 6.2 dB stem, 5.8 dB master, in the bar 54 "sul A, cantabile" theme.
  - Violoncellos 81.0: 4.7 dB stem, 5.5 dB master.
  - Violas div 283.0: 3.7 dB master.

  The deepest stem dips are hidden by the master: Violins I 67.5 at 10.3 dB (master 1.6), Violas 241.5 at 9.6 (master 0.2). Rerun `auto_fills.py 28` with the overshoot check.
- **Breath at qn 268, bar 81 (measured).** Oboe 1 and Clarinet 1 leave a 0.020-0.024 qn gap (4-8 dB dip), where the other winds leave 0.12 qn (14-26 dB). The next note's legato lead eats the breath. Keep `CAESURA_BREATH_QN` for them, or skip the lead at 268 on those two tracks.
- **Run into bar 79 (Violins I/II 261.5-261.83; measured).** The 2nd and 3rd notes are dominated by the previous pitch for their first 0.05 s (7-10 dB). The flute doubling covers it. The Slur Runs row (p.96) is the untried option, but these notes are slower than its stated minimum. A Leg Slur MAX trial at v127 with a 0.02 qn overlap, on this run only, is cheaper.
- **The 4 soli pedals (measured, inferred cause).** The basses 220-238 and celli 274-286 swing 7-10 dB per 0.5 s in their low band in both renders (p90). The celli's fitted shapes now step up to 12 dB within 0.25 qn (vol_db +3.7 at 280.25, -8.6 at 280.5). With CC11 flat at 20-22, a four-player ppp pedal should not lurch like that. Smooth the fitted shapes on these pedals (`fit_rebows.py` FILL_SMOOTH_S 0.10 -> 0.25 for Violoncellos 274-286 and Double basses 220-238), or put the 4 soli on the Basses/Celli DIV A patches (MANUAL-GAPS #8, memory permitting). The celli band shows a 0.56 correlation at a 4.0 s lag, against 0.34 in c27.
- **Harp arpeggios** (measured on parts.json). Rolled from the bottom, 40 ms per note (30 ms at f, 261), top note +4 velocity, as kit LEARNINGS 9 asks.
- **Better patches considered.**
  - Solo violin for bars 17-22: not installed (gap #3). The DIV A track's joins are all under 6 dB.
  - Con sordino: the Hollywood Strings mute is the CC15 script. CC15 changes fall in rests on every string track, and Horn 3-4's mute EQ starts at 278 before their con sord. entry at 286 (coda.ily line 5 prints Hn 4 con sord. too).
  - Portamento legato: already at 82 and 172.
  - The a2 horn patch: used in bars 79-82.
  - Horn/trombone portato rows for the bars 61-62 tenutos: not needed. The master dips at 206, 208 and 210 are still at most 2.2 dB.

## Do not touch

- The c28 re-bow refit everywhere except the three stale keys: opening chord, bar 66, final chord. The master falls through the ppp fermata with steps of at most +1 dB, the bar 66 master dip is 1.7 dB, and loop correlation at 3.95 s in the master's final chord is -0.06.
- Trombone 1 on Leg Slur MAX with the 216 re-tongue, and the 218 accent on Sus MAX (no 2-5 kHz bite).
- The Violas Detache row in bars 48-51.
- The tremolo rows and CC11 in bars 61-64.
- The pizz rows and timing: basses at +0.00..+0.01 s in the probe.
- The CC15 mute placement.
- The timpani CC1 layers and the 203/262 arrivals.
- The harp roll spacing.
- Keyswitch placement: no keyswitch falls within 0.03 qn after a note it serves, and there are no ks clashes.
- No chords on legato rows.
