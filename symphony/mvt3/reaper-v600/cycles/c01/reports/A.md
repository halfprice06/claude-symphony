# Cycle 1, critic A: articulation and phrasing (render c00, score v600)

Method. Levels are stereo-power dB on the c00 stems and master (`cycles/c00/render`; the master is the float sum of the stems), placed on the tempo map in `build/parts.json`. Note rows come from each track's keyswitch lane, and score marks from `build/mockup-events.tsv`. Patch facts were read from the installed `.oib` files with `opus_state.load_oib` and from `ks_maps.json` / `build/ks_maps_extra.json`. "Measured" means a number from the render, parts.json or a patch file. "Inferred" means reasoned, not tested. One correction to my own method: a first pass of my envelope script summed in float32 and reported false digital silences on about 400 notes. Every number below comes from the float64 rerun, which finds no silent notes on any stem.

## Manual notes (cycle 1, slot A: 2021 manual PDF pages 89-94, strings)

I read Movement I's c36 A table first. The tools carry its answers (the Violins I staccato row swap, pizzicato rows), so the notes below check each page against the Finale.

| Manual (PDF page) | Where it applies in the mockup | Does the render follow it? |
|---|---|---|
| p.89-90: DIV A/B are the left or right chair of each stand, Close mics only, and "the loudness of a divisi part is not much less than if the whole section were playing the part". | Vla div. (from bars 1, 5, 87, 205, 211), Vln I div. (bars 159, 217, 273), Vln II div. (bars 212, 219, 243, 273), the "div. a 3" tremolo chords at 278 (qn 1108), and Vln I "4 soli / gli altri" at 119-122 (qn 473-488). All are played as chords on the section KS Masters with the div. cut (`div_entries`), and "4 soli" through `SOLI_AS_META`. | **Partly.** The levels are handled, but the half-section and four-player colour is missing (MANUAL-GAPS #7, memory). The slurred dolce "4 soli" line is octave chords on Sus MAX, so every eighth is a new bow (boundary dips 0-6 dB, measured). It is short (2 x 1.5 s), so I give it no finding. |
| p.91: Détaché ends cleanly with no legato. Notes short enough to be staccato belong on a staccato row. | Unslurred running notes: Violas 543 Sus MAX notes, Vln II 494. | **No**, as in Movement I. The Detache row is never used. No change proposed. |
| p.91: Sustain alternates bow direction by round robin. The 3 vibrato levels are non-vib, vib and molto, and in the string KS Masters CC1 crossfades them. | Every Sus/Leg string note. In the sul tasto spans CC1 sits at 46-62 on Vla, Vc and Cb. | **Not in the sul tasto spans** (finding 4). Bow direction RR is never reset (MANUAL-GAPS #6, unchanged). |
| p.91-92: Marcato Sustain adds a marcato sample "for extra power at the start". | Movement I used Sus Marc LITE on 14 strokes. The Finale uses it on none. | **n/a so far.** String accents measure front minus body -1.9 to -3.6 dB median (max +6.9 on a Leg Slur target, Vln II qn 1009). That is weight without bite, so no change is needed. |
| p.92: Flautando exists in the 2nd Violins only. "The Sustain patch in other sections, when played pp with no vibrato (Mod Wheel all the way down), achieves a similar sound." | "sul tasto, last 2 desks" at bar 95 (qn 376-392, Vln II, Vla div., Vc, Cb) and Vla "sul tasto" at bars 170-180 and 183-186 (qn 678-720, 728-744). | **Only for 1 Vln II note**, and that one loses Flautando at its hidden re-bow (qn 383.3). Vla, Vc and Cb play full vibrato (finding 4). |
| p.92: Harmonics exist in the 2nd Violins only. They sound two octaves above the fundamental, so the lowest is G4. | Vln I "harm." at bar 43 (qn 168, B flat 5 sounding, pp, 11.4 qn). | **No.** It plays on Leg Slur MAX, an ordinary vibrato tone. Moving it to the 2nd Violins KS Master's Harmonics row would need another instance (Vln II plays a legato note at the same time). Low priority, but it sits beside the missing harp harmonics of finding 5. |
| p.92: Pizzicato is RRx4 in every section. | Bars 51-66, 115-122, 171-186: Vln II 90 notes, Vla 89, Vc 62, Cb 60, all at v41. | **Yes.** v41 falls in each patch's softest layer (Vln II/Vc 1-50, Vla 1-45, Cb 1-55; read from the region maps), and every RR group covers v41 across the range. Vln II attacks peak +0.03..+0.09 s after the score onset. |
| p.93: Bartók, ricochet, col legno, marcato short, spiccato, Spiccato Marcato MOD. | None printed. The basses' hammered eighths (coda, Più allegro) are unmarked. | n/a. Finding 2 keeps them on Sus MAX, as Movement I did. |
| p.94: Staccato types: plain, on the bow, Staccato Marcato MOD, staccatissimo. | Printed string staccatos: Vln I "Staccatissimo RRx9" (which plays the "V1 Stac" samples, Movement I c36), Vln II/Vla/Vc "Stac RRx9", Cb "Staccato RRx9". | **Yes.** -10 dB lengths are Vln I 0.28 s, Vln II 0.27, Vla 0.33, Vc 0.28 and Cb 0.27, against a written quarter of 0.36 s (measured). These are the reference for finding 1. |
| p.94: Repetitions: "more realistic than just playing the same staccato note multiple times because you get the sound of the bow changing direction", with release trails. | The basses' 300 repeated eighths (finding 2). | **Not used.** "Repetitions TS" is tempo-synced and untested (MANUAL-GAPS, Movement I). It is a second option for finding 2 if the dip rule is not enough. |
| MANUAL-GAPS.md items that touch this lens | #11 wind staccato rows ("tried and kept" in Movement I's second pass), #2 repetition rows, #7 divisi, #13 bass trombone B flat 1. | #11 is the basis of finding 1. #2 and #13 are unchanged. |

## 1. Printed staccatos on horns, trumpets, trombones and bassoons ring longer than the written quarter (measured)

**Where.**
- Horns 3-4: the F1 off-beat accompaniment, bars 11-26 (qn 40-104), and the recapitulation, bars 151-166 (qn 600-664). That is 126 staccato quarters, the texture under the whole first theme.
- Bassoon 1 doubles the same off-beats: 55 staccatos (bars 11-26, 28, 32, 100, 146, 208, 250, 266-268).
- Trumpets 1-3, bars 159-166 (qn 632-664).
- Horn 1 (bars 12-24, 140-164, 266-268), Trombone 1 (bars 104-105, 206, 250) and Tuba (bars 28-32).

**What is wrong.** Every wind and brass staccato plays on the Sus or Leg row, cut to half its written length. Wind tracks: Sus MAX/Leg Slur MAX; horns and trombones: Sus MAX; trumpets: Sus Non Vib MAX. A written quarter at sq 41 plays from qn 40.86 to 41.50. The sustain sample holds flat until the note-off and then releases. Measured on the Horn 3 stem at qn 41, 43, 47 and 605: the level stays within 2 dB of its peak for 0.30 s, then falls. The result is a fat, held off-beat, not a detached one.

| track | staccato notes | -10 dB length, median | written quarter |
|---|---|---|---|
| Horn 3 | 67 | 0.48 s | 0.36 s |
| Horn 4 | 59 | 0.48 s | 0.36 s |
| Trombone 1 | 11 | 0.46 s | 0.36 s |
| Bassoon 1 | 55 | 0.40 s | 0.36 s |
| Trumpets 2-3 | 30 | 0.40 s | 0.36 s |
| Trumpet 1 | 25 | 0.36 s | 0.36 s |
| Strings on Stac rows | | 0.27-0.33 s | 0.36 s |

The staccato horn chord rings 0.2 s longer than the staccato string chord it accompanies. The horn and bassoon off-beats of F1 are printed staccato in every bar (mockup-events.tsv). The KS Masters have real short rows: 1FH "StacSs RRx9" (27) and "Marc Shrt RRx4" (28); 1TP "Stac DblTng RRx9" (28); BS "Stac DblTng RRx9" (28); 1TB "Marc Shrt RRx4" (28). Manual p.102 (brass shorts; avoid the top velocities) and p.110 (woodwind staccato; no release trails). Movement I kept "Stac DblTng RRx9" on Bassoon 1, Cor anglais and Flute 1 (MANUAL-GAPS #11, "tried and kept": natural decay instead of a swell to the note-off).

**Fix.** `build/score_config.py` `ART_SPANS` already supports `"mark": "staccato"` (only notes that carry the mark) with `vel_by_cc`. Keep Trumpet 1's mute span in its list.
- Horn 3, Horn 4: `{"from": 40.0, "to": 104.0, "art": "StacSs RRx9", "mark": "staccato", "vel_by_cc": [(60, 70), (90, 88), (110, 98)]}`. As an A/B in the same render, `{"from": 600.0, "to": 664.0, "art": "Marc Shrt RRx4", "mark": "staccato", same velocities}` for the ff recapitulation.
- Bassoon 1: `{"from": 40.0, "to": 132.0, "art": "Stac DblTng RRx9", "mark": "staccato"}`. Add the 0.03 s `STAC_LEAD_S` that Movement I's winds took.
- Trumpets 1-3: `{"from": 632.0, "to": 664.0, "art": "Stac DblTng RRx9", "mark": "staccato"}`.
- Keep velocities under about 100 (p.102). These rows have no CC11 dynamics, so check their level against the Sus notes they replace and set a `ROW_TRIM_DB` entry from the render.
- For the remaining Sus-row staccatos (Horn 1, Trombone 1, Tuba, the winds' coda staccatos), end the note at 0.35 of the written length instead of 0.5 (tools/score_to_parts.py, the wind/brass staccato length).
- Targets: -10 dB length 0.22-0.30 s, matching the strings, and 2-5 kHz front minus body under +3 dB.
- Memory: one more row on 6 tracks, about 1-2 GB (c00 settled at 41 GB).

## 2. The basses' hammered repeated eighths blur into a held note (S1; measured)

**Where.** Double basses, coda bars 199-210 (qn 792-840, ff then f) and Più allegro through the Largamente, bars 247-277 (qn 984-1108, ff/f/fff). These are 303 same-pitch repeated eighths on Sus MAX, each 0.47 qn long with a 0.03 qn gap, about 10 ms at 168-176 qpm. The score's note is that 199-204 is "movement I's hammered layout exactly as at its bars 27-32".

**What is wrong.** No `STR_REP_DETACH` or `METRIC_BOWED` span is set for the Finale (PORT.md lists both as c01 candidates). Movement I needed both for the same layout (its c22 and c37).

**Evidence (measured).**
- Re-attack dip per repeat (peak after the onset minus the minimum in the last 60 ms before it, 10 ms windows), Cb stem: median 4.3 dB at qn 792-816, 4.5 at 816-840, 4.7 at 984-1016, 5.3 at 1016-1048, 4.8 at 1048-1080. The p10 is 2.3 dB, with -0.2 at 1016-1048.
- 67 repeats dip under 3 dB, in runs at qn 793.5-807.5, 984.5-987.5, 1000.5-1007.5, 1016.5-1029.5 and 1081-1104.5.
- Eighth-grid fold of the 30-150 Hz band: Cb stem 1.9-3.1 dB, master 1.7-2.3 dB. Movement I's c42 measures 5.5 and 4.7 at its bars 27-31 (re-attack dip median 8.0, p10 5.0, with `STR_REP_DETACH`). Its c22 found 2.7-3.1 dB before the fix and heard that as "one held note".

**Fix (`build/score_config.py`).**
- `STR_REP_DETACH = {"at": {"Double basses": [(792.0, 840.25), (984.0, 1108.25)]}, "dip_db": -5.0, "dip_s": 0.08, "ramp_s": 0.02, "back_s": 0.005, "max_qn": 0.5, "min_cc": 72}`. This is Movement I's c22 values, with min_cc lowered so the f stretches (816-840, 1016-1032, 1056-1108) are included.
- A +1.5 dB `LEVEL_SHAPES["Double basses"]` hold over the same spans, as Movement I's c22, so the bar level stays.
- `METRIC_BOWED` for Violas, Violoncellos and Double basses over (792, 816) and (984, 1080), Movement I's c37 C #5 form.
- Targets: re-attack dip median 7 dB or more with p10 at least 4 on the stem; master 30-150 Hz fold at least 4 dB.

## 3. The horns' lower octave is missing at bars 249-250 of the Più allegro head (measured)

**Where.** Horns, qn 996-1000 (bar 249, beats 3-4 to bar 250): the octave chords C4+C5 and B3+B4, printed for Horns 1 and 2 (shared staff), with Horn 4 also on C4/B3. This is the ff brass statement over the hammered eighths.

**What is wrong.**
- The unison rule kept Horn 1's copy of both pitches and dropped the same pitches from Horn 2 and Horn 4 (parts.json: Horn 2 and Horn 4 have no note at 996 or 998).
- Horn 1 plays them on Leg Slur MAX, a monophonic patch: C4 at qn 995.824 (v124), then C5 at 996.0 (v91). The patch makes a legato transition from C4 into C5, so C4 ends. The same happens at 998 (B3, then B4).
- This is the only chord on a legato row in parts.json (scan of every Leg row for overlaps over 0.12 qn between different pitches).

**Evidence (measured).**
- Horn 1 stem spectrum over qn 996.3-997.7: the C4 fundamental (262 Hz) is 23.0 dB under the C5 fundamental (523 Hz). Over 998.3-999.7, B3 is 14.2 dB under B4.
- At qn 1000, a single E4, the fundamental is +1.9 dB, so the missing low note is not a filter effect.
- Horn 2's stem has no energy at either pitch. Clarinet 2 and the violas carry only the upper octave.
- For about 1.4 s no horn plays C4 or B3, although three horn parts are written there.

**Fix.**
- Give Horn 2 the chord's lower note and keep only the upper note on Horn 1. Restore Horn 4's C4/B3, as printed.
- Generic rule in `tools/score_to_parts.py` (the unison grouping): when the kept copy is part of a chord on a legato row, do not drop the other tracks' copies of the non-top pitches. Assign them by pitch order, top to the first track, so the chord is split across tracks.
- Check that the split notes play Sus MAX or Leg Slur MAX without overlap, and that the +10·log10(n) unison gain is recomputed for the notes each track now plays (kit §8, c19).

## 4. Sul tasto is not rendered on violas, cellos and basses, and the Vln II flautando changes colour at its hidden re-bow (measured)

**Where.**
- Bars 95-98 (qn 376-392): "sul tasto, last 2 desks" (Vln II), "sul tasto, div., last 2 desks" (Vla), "sul tasto, last 2 desks" (Vc), "sul tasto, last desk" (Cb), mp diminuendo to p.
- Violas "sul tasto", pp, bars 170-180 (qn 678-720) and 183-186 (qn 728-744): about 90 eighths accompanying the cor anglais and muted trumpet solo.

**What is wrong.**
- `score_to_parts.py` maps sul tasto only to the 2nd Violins' Flautando row. The other sections play ordinary Sus MAX with CC1 following the level: Vla, Vc and Cb sit at CC1 55-62 at qn 376-392, and Vla at CC1 45-48 at 678-744. By Movement I's c36 reading of the patch CC1 tables, the non-vibrato layer is gone by CC1 56 on violas.
- Manual p.92 gives the remedy for exactly this case: the Sustain patch at pp "with no vibrato (Mod Wheel all the way down)" is close to flautando. The render is a full-vibrato section where the score asks for a veiled, quarter-section colour.
- Vln II's one Flautando note (qn 375.66, 7.6 qn long) is split by `AUTO_REBOW`, and the second half (qn 383.32) plays Sus MAX. Measured on the Vln II stem, the spectral centroid steps from 568 Hz (qn 381.5-383.2) to 991 Hz (383.6-385.3) and 1304 Hz (386-388), and the level falls 13 dB at the re-bow (-55.4 to -68.5 dB).
- "last 2 desks" / "last desk" get no level cut (`SOLI_AS_META` reads only "N soli"), although the printed ensemble is a quarter of the section or less.

**Fix.**
- New generic option in `tools/score_to_parts.py` beside the Flautando branch: `TASTO_CC1 = {"cc1": 0, "ramp_qn": 0.25}`. For string notes in a sul tasto text span ("sul tasto" until "ord." / "arco"; the Vla span 678-720 ends at the printed "ord." at 720) on sections without Flautando, write CC1 0. Set `TASTO_CC1 = {"cc1": 0, "ramp_qn": 0.25}` in `build/score_config.py`.
- Re-bow splits inside a tasto span keep the row of the note they split (Flautando on Vln II), or the span is listed in a re-bow skip.
- Read "last N desks" / "last desk" like `SOLI_AS_META`, with a -4 dB cut (inferred: a quarter section, softened per p.89-90). As a starting value, use Movement I's sul tasto EQ in `build/mix.json` (Vln II bars 147-155 tremolo, MANUAL-GAPS "checked") on these spans.
- Targets: Vla/Vc centroid over qn 376-392 and 678-720 at least 20% lower than the same notes now; no centroid or level step over 2 dB at the Vln II re-bow.

## 5. Harp: the bar 43 harmonics are silent and the bar 277 glissando is a single held note (measured)

**Where and evidence.**
- Harmonics: HarpL at qn 168, 176 and 184 (bars 43, 45, 47; "harm. (sound 8va)", p). This is the first sound of the transition C, with Fl 1 / Cl 1 / Ob 1's motive x.
  - `score_to_parts.py` removes flageolet notes from the Harp track ("harmonics go to their own track", family "harm"). The port's `TRACKS` has no harmonics track.
  - The three notes are absent from parts.json. The harp stem is at the noise floor from qn 150 to 200.
- Glissando: bar 277 (qn 1106-1108), G3 to G6 over the pentatonic C-D-E-G-A (`finale.ily` c204/c249/c256), f < into the fff landing chord at 278.
  - parts.json has one note: G3 at qn 1106, v94, 6.8 qn long. No glissando notes are written, because `mockup-events.tsv` carries no glissando event.
  - The harp is silent from its étouffez at bar 243 until this entry. The score note says only the basses' eighths sound on beat 4 of 277, so the run should be audible.

**Fix.**
- Harmonics: add a "Harp harmonics" track (family "harm", `Harp Harmonics.oib`, range 48-96, sounding pitch; kit §9), or, to save an instance, route the three notes onto the Harp track at the sounding pitch with `HARM_VEL_CUT`. The harp is silent there, so nothing clashes.
- Glissando: a generic `GLISS_SPANS = {"Harp": [(1106.0, 1108.0, 55, 91, [0, 2, 4, 7, 9])]}` in `build/score_config.py`, expanded in `score_to_parts.py` into 16 notes G3...G6 on the C-D-E-G-A set. Space them evenly from qn 1106 to 1107.9, velocity rising 90 to 112, each ringing to `HARP_RING_S`, with the landing chord unchanged.
- Glissando key maps are in manual p.72-74 (the c6 A reading). If an Opus glissando patch fits, it would need its own instance.

## 6. Trumpet 1's open solo (bars 51-66) uses the fastest legato transitions for a dolce p line (inferred)

**Where.** Trumpet 1, qn 200-264, "solo, dolce cantabile", p. 37 legato targets on Leg Slur MAX at v124.

**What is wrong.** In brass legato, velocity sets the transition speed (manual p.106, the c3 A reading). v124 gives the fastest, most present slur. Measured: the slur joins dip only 1.1 dB median, but the transition attacks sit 2.0 dB median (p90 4.9) over the following note's body. Movement I used v90 for soft string legato targets (kit §5, c08). The leads (brass 0.10 s) were fitted at v124, so a lower velocity needs its lead checked (kit §5: velocity barely moved crossovers on strings).

**Fix.** `build/score_config.py`: a soft legato velocity for brass legato targets at CC11 at or under the p level, e.g. 96. If there is no generic option, add one in `score_to_parts.py` next to the c08 soft string rule. Measure transition peak minus body (target 0-2 dB, p90 under 3) and pcx crossover timing against the c00 values.

Do not touch:
- Pizzicato rows and v41 velocities (bars 51-66, 115-122, 171-186).
- Harp étouffez damping (the stem falls 17 dB within 1 qn after qn 326 and after qn 1113).
- String staccato rows and lengths (-10 dB 0.27-0.33 s), including Violins I's `STAC_ROW`.
- `GENTLE_ACCENT` on brass. 2-5 kHz front minus body, medians: horns -8 to -14 dB, trumpets -10 to -12, trombones -1 to -10, tuba -13; the highest brass accent is +4.6 on a Trombone 1 legato target.
- `AUTO_REBOW` on strings: no string note over 6 s is left unsplit, and the only notes over 6 s are Horn 4 at qn 168 and the timpani roll at 920.
- The Tremolo row arrivals at qn 888, 1016, 1088 and 1108: no hole beyond the written rest at qn 1107.
- Trumpet 1's "Mute Sus" span: joins dip 0.9 dB median, no bright attacks.
