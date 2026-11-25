# Cycle 52, critic C: holistic comparison (review of the c51 render)

## Method

I measured the c51 master, its stems and the delivered mp3 with my own numpy scripts and read the note data from `cycles/c51/rendered_build/` (parts.json, score_config.py, mockup-events.tsv). Every position was converted on each render's own tempo map: c51 and c50 from their `rendered_build/parts.json`, c27 from `cycles/c28/before/parts.json` (its map ends at 348.23 s; the c27 master is 356.23 s, the map plus the 8 s tail), c26 from `symphony/mvt2/reaper/build/parts.json` (348.87 s against a 356.87 s file). I did not use REAPER, changed no audio setting and deleted nothing.

- Delivery: a replica of `tools/deliver_master.py` (same constants, same ffmpeg filters) that also returns the ride gain. On the c51 master it gives LRA 14.7 LU, span 18.6 dB, limiter 0.99 dB, which matches the actor's figures (14.7, 18.5, 1.0). Variants were run on the same master.
- Printed marks: every `breathe`, tempo word, fermata and text mark of `mockup-events.tsv` against the map, the note data and the stems.
- Comparison renders: per-bar master level from each cycle's `metrics.json`; phrase joints and the string theme measured on the c27, c50 and c51 files.
- Recordings: the two Brahms slow movements exist here only as loudness curves (`symphony/render/critics/c04/ref_brahms*_ii_musopen/loudness_series.csv`, 0.1 s steps); Bernard Duc's Adagietto file (`mockup-reference-cn1rc0/mockup-kit/reference/bernard-duc/`) gives a tempo map that follows a recording.

Each judgement is marked measured, simulated or inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 52 (its last row is cycle 47), so there was no page range to read. Items of `loop/MANUAL-GAPS.md` that touch this lens (pages as cited there; I did not re-read the PDF pages this cycle):

| Manual (May 2021 HO manual, PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| Legato velocity sets the transition length (p.144, p.99; MANUAL-GAPS 6) | The cantabile string lines, bars 23-28, 53-56, 71-77 | Not tried. The c51 string rows were fitted at the present velocities; a change would undo that fit. Not asked |
| Expressive rows for espr./dolce wind solos (p.109; MANUAL-GAPS 5) | Oboe 1 42 and 139, bass clarinet 91, Flute 1 108, cor anglais 124 and 151, Clarinet 1 280 | Not used. With the tempo now fixed, the level contour is the only shaping these solos have (5.0-10.9 dB per phrase, table in the answer to open item 2). Not asked this cycle; it is the first thing to try if a listener finds the wind solos plain |
| Round-robin reset on CC16 (p.34, p.143, p.145; MANUAL-GAPS 10) | Repeatability of string joins (the lead's first open item) | In the pre-roll since c45 and at Violas 152.06 since c49. Slot A's question; not measured here |

## Answer to the lead's second open item: is anything mechanical without rubato, and is any printed mark under-realised?

**Printed tempo words (measured on the map).** All are realised. Beat values in bpm: poco rit. bars 35-36 51.0, 49.1, 47.7, 46.3, 45.0, 43.7 (printed steps 49, 45); Poco più mosso 60.0 from its first beat (c50 57.6); poco rit. bar 47 57.5, 55.0; poco sostenuto 54.0; animando 60.0 to 64.5; poco allargando bar 60 63.0, 61.0, 59.0, 57.0; Largamente 54.0 on all twelve beats of bars 61-63; allargando bar 64 50.9, 46.5, 43.5, 40.5; Tempo I 52.0; poco allargando bars 78-82 51.3 falling to 43.3; a tempo 52.0; rit. bars 89-92 50.7 falling to 35.2, fermata beat 20.0 (3.00 s).

**The five breaths that kept time (measured).** 29, 102, 124, 268, 286. All the added time is in the last quarter of the beat before (288, 288, 288, 468 ms at 29; 250, 250, 250, 430 ms at 124). No track has a note onset inside any of the five stretched beats, so no figure is made uneven: the listener hears the next entry 0.15-0.18 s late and nothing else. Master dip at each: 6.5, 10.4, 10.7, 3.7, 3.7 dB.

**The fermata (measured; the comparison is inferred).** Bar 92 lasts 6.34 s after a bar 91 of 4.52 s; the chord sounds at -54 to -58 dB (master, 0.1 s frames) for 6.0 s and is gone 0.7 s later. The two Brahms slow movements end on chords that hold for about 6 s (Symphony 1) and about 8 s (Symphony 4) on their momentary-loudness curves (0.5 s reading accuracy; I cannot hear where the chord starts, so this is inferred). Ours is at the short end of that range and not outside it. No change asked: a longer last beat needs a new re-bow on every string track (the Violoncellos' last segment, from 302.35, is already 4.1 s; the loop period is 3.95 s), and the evidence does not justify that.

**Printed breath marks (measured).** 46 marked parts at 20 positions. 41 have a data gap of 116 ms or more, and their stems dip 10 dB or more under the level before (Bassoon 2 at 204: 6.3 dB). Five do not; they are finding 1.

**Phrase shape with the tempo fixed (measured on the stems, level of each note against the loudest note of the phrase).** Every thematic phrase still has a level contour:

| Phrase | Range, dB | Printed hairpins followed |
|---|---|---|
| Horn 1, bars 7-10 and 11-14 | 8.6, 9.4 | yes (peak on the hairpin's top, 20 and 32) |
| Oboe 1 15-16, Violin I solo 17-18 | 5.6, 5.9 | yes |
| Violins I 23-26, 27-30 | 10.2, 18.2 | yes |
| Bass clarinet 31-36 | 8.6 | yes |
| Flute 1 37-40, cor anglais 41-44 | 7.2, 10.9 | yes |
| Cor anglais 47-52 | 5.5 | yes |
| Violins I 53-56, 57-60 | 13.1, 9.5 | yes |
| Violins I 71-74, 75-78 | 4.7, 14.4 | yes (the 240-241 hairpin is +3 to +5 dB, the same size as at 68) |
| Clarinet 1 85-88 | 5.0 | yes |

**Section joints with no printed breath (measured).** Qn 42, 90, 139, 148 and 237 pass at the full tempo with a master dip of -0.1, -2.3, 0.4, 0.3 and 2.1 dB. The dips were the same size in c27 (-0.8, -0.3, 3.8, 0.9, 0.9 dB) and in c50, so the sound at these joints has not changed; only the time has (c27 played the beat before them at 43.1, 45.8, 57.6, 58.2 and 45.6 bpm, c50 at 37-48). Evidence on practice: Duc's Adagietto map, which follows a recording, has a tempo change on 98 % of beats and phrase-end beats 15-30 % slower (FINDINGS part 4, section 13). I read that map bar by bar and confirm its character (for example bars of 4.05 to 6.57 s within nine consecutive bars), but I have no score-aligned reading of where its printed marks fall, so it does not meet the lead's condition (practice at printed marks). **I ask for no unprinted tempo change.** If Dan finds the movement stiff, these five joints are where c27's map differed most from c51's, and c27's values (12-17 % on one beat at 42, 90 and 237) are the smallest version that has been heard and accepted ("It's ok").

**Accompaniment figures (measured).** With triplets now even within 0.0 %, I checked whether the repeated figures also repeat in level. They do not: Violas triplets 108-124 SD 1.6-2.5 dB per beat position, pizzicato triplets 124-140 SD 2.8-4.9 dB, sextuplets 196-204 SD 2.7-3.4 dB, bass pizzicati 108-140 SD 3.4 dB (round-robin and pitch differences; the velocities are constant at 124, 100 and 53). `METRIC_VEL` was tried and withdrawn in series 1 c16-c17. No change asked.

**Verdict.** No phrase is mechanical by any measure I can take, and no printed tempo mark is under-realised. The printed marks that are under-realised are five breaths (finding 1).

## Holistic comparison

**Against c46 and c50 (measured).** Bar levels are within 1.0 dB of c50 in 91 of 92 bars (bar 86 -1.1) and within 1.9 dB of c46 in all bars. Band shares are unchanged since c46 (2-6 kHz -10.0 dB; 20-100 Hz -17.3 against -18.0). What c51 changed is time: 346.0 s against 353.3 s, note starts, and the breath gaps of finding 1.

**Against the c27 port baseline and series 1's c26 (measured).** The soft passages are 2-5 dB lower in the master than in c27 (bars 4-5 -5.4, 16 -4.8, 34-35 -4.0 and -4.6, 50 -5.1, 65 -4.7, 69-70 -4.4, 84-86 -3.3 to -6.0, 90-92 -4.1 to -6.3) and the ff cadence of bars 79-80 is 6.8-7.1 dB lower, while the climax (bars 61-62) is unchanged (-0.3, -1.3 dB). The cadence now sits 5.8 dB under the climax in the master and 2.2 LU under it in the delivery; in c27 the two were equal. The mix is 1.3 dB brighter than c27 in the 2-6 kHz share and 2.1 dB fuller under 100 Hz.

**Against recordings (measured on the shares in metrics.md).** 2-6 kHz share -10.0 dB: Dvořák 9/i -10.5, Brahms 1/ii -12.4, Brahms 4/ii -11.8. 20-100 Hz -17.3 dB: between the Dvořák (-21.7, lossy) and the Brahms pair (-8.5, -7.9). Nothing here asks for a change.

**The weakest passages now** (the first four from the actor's S tables and re-bow file; I did not re-measure them, they belong to slot A):
1. Bars 71-78, theme A' in both violin sections: 7 of 28 doubled onsets over 60 ms apart (up to 115 ms), Violins I 7 and Violins II 11 notes outside 25 ms.
2. Bars 61-64, Violins I: one start +229 ms, unchanged from c50.
3. Bars 17-22, Violin I solo: +109 ms on one note, 4 of 11 outside 25 ms.
4. Bars 83-86, Violoncellos div: re-bow dip 6.2 dB at 275.527 (c50 2.5).
5. Bars 58-61, the breaths before the animando's last phrase and before the climax: finding 1.

## Findings

### 1. Five printed breaths before bars 59 and 61 are too short to be heard as breaths; three of them were shortened by the c51 tempo change

**Where.** Qn 196 (bar 59): Flute 1, Oboe 1, Horn 1. Qn 204 (bar 61): Trombone 2, Bass trombone.

**What is wrong (measured).** Data gap from note end to the next note-on, and the stem's lowest 20 ms frame against the last 0.3 s of the note before:

| Part, breath | c50 gap / dip | c51 gap / dip | Cause |
|---|---|---|---|
| Flute 1, 196 | 127 ms / 12.9 dB | **95 ms** / 15.5 dB | the gap is 0.2 x the eighth before it, in qn; c50's caesura stretched that quarter beat |
| Oboe 1, 196 | 127 ms / 7.8 dB | **95 ms** / 7.8 dB | same |
| Horn 1, 196 | 217 ms / 13.8 dB | **137 ms** / 8.4 dB | note ends 237 ms before the beat (c50 317); the next note-on is 100 ms early |
| Trombone 2, 204 | 76 ms / 4.7 dB | **74 ms** / 3.6 dB | note ends 174 ms before the beat; the next note-on is 100 ms early |
| Bass trombone, 204 | 29 ms / 2.4 dB | **24 ms** / 1.0 dB | same, with a 150 ms lead |

For comparison, the other parts marked at 204 have 134-174 ms and 10.9-23.0 dB, the bass clarinet at 196 has 340 ms, and the repeated-note gaps the plan asks for are 60-100 ms (EW-TEMPLATE-PLAN section 8). A 95 ms gap is the size of a re-tongued repeat, so Flute 1 and Oboe 1 re-articulate at 196 without breathing, and the two low brass parts play their crescendo straight into the f of bar 61. Horn 1's breath at 196 has lost 80 ms and 5.4 dB since c50 (the comment at `score_config.py` lines 1162-1165 gives 240 ms as the value the c46 rule was set to keep). The c51 critic C's do-not-touch list named the breath gaps at 196, 204 and 268; the 196 gaps changed anyway because they are defined in qn.

**Fix.** `build/score_config.py`, in the c52 block (the table is keyed by the onset of the note that ends at the breath, as the existing Clarinet 1 266.0 row is; the code takes `min(value, 0.6 x the note's length)`):

```python
BREATH_GAP_AT.setdefault("Flute 1", {})[195.5] = 0.2
BREATH_GAP_AT.setdefault("Oboe 1", {})[195.5] = 0.2
BREATH_GAP_AT.setdefault("Horn 1", {})[195.5] = 0.3
BREATH_GAP_AT.setdefault("Trombone 2", {})[202.0] = 0.26
BREATH_GAP_AT.setdefault("Bass trombone", {})[200.0] = 0.30
```

Expected from the map (63.2 bpm at 195-196, 57.0 at 203-204): Flute 1 and Oboe 1 190 ms; Horn 1 note end 285 ms before the beat, gap 185 ms; Trombone 2 274 ms before the beat, gap 174 ms; Bass trombone 316 ms before the beat, gap 166 ms (the tuba, with no lead, has 174 ms now). Five tracks `--midi-only`. No tempo change, no change to `CAESURA_BREATH_QN_AT` or `CAESURA_BREATH_SKIP`.

**Acceptance.** Stem dip under the note before: at least 10 dB for Flute 1 and Horn 1 at 196, at least 8 dB for Oboe 1 (its release is slower), at least 6 dB for Trombone 2 and Bass trombone at 204. Master dip at 204 not over 4 dB (it is 2.4; series 1 c19 found a 0.54 s wind hole there too large) and at 196 not over 5 dB (3.5). The notes after the breaths must keep their c51 starts (Horn 1 196, Trombone 2 and Bass trombone 204: check with `tools/s_onsets.py`).

### 2. Delivery: add the finale's rise delay (technique 35); leave the level and the ratios alone; technique 36 does not apply

**Where.** `tools/deliver_master.py`, `build/mix.json`. No render needed; it can be run on the c51 master.

**What is measured.** The master has two places where the level falls 9 dB or more within half a second: qn 218.3 (bar 64, the end of Trombone 1's ff under the p tremolo and the dim. to pp) and the printed breath at 102. It has no tutti stop into silence. So the finale's two stop techniques have little to act on:

- Technique 35 (delay the rises of the ride gain). The gain rises 2.8 dB between qn 218 and 219 and 1.9 dB between 268 and 269, while the printed diminuendos are still falling. Simulated with a 0.6 s delay on the c51 master: mp3 level over qn 219-220 -34.0 -> -34.7 dB, over 269-271 -22.3 -> -23.2 dB, bar 65 (220-223) -34.4 -> -34.8; LUFS -19.5, LRA 14.7, span 18.5 dB all unchanged, limiter 0.99 -> 0.91 dB. A 1.0 s delay gives -35.5 and -23.8 with the same totals. The effect is 0.7-0.9 dB at two places and costs nothing.
- Technique 36 (post-hall fade on celli and basses at stops). Not applicable (read from parts.json): the celli and basses are resting at the breaths at 29 and 102; at 124 and 204 they play a new note on the beat with no rest; at 268 the celli hold through (267 to 269) and the basses re-enter on the beat; at 218-220 the celli are tied into the pp. There is no stop for a fade to shorten.

**The limiter's room (simulated on the c51 master).** The limiter is not the constraint; the span is (18.6 dB against the 16-19 target).

| Variant | LUFS | LRA | span | limiter | climax minus bar 79, LU |
|---|---|---|---|---|---|
| c51 as delivered | -19.5 | 14.7 | 18.6 | 0.99 | 2.2 |
| `TARGET_I` -19.0 | -19.0 | 14.7 | 18.5 | 1.49 | 2.1 |
| `TOP_RATIO` 1.6 | -19.6 | 14.9 | **19.2** | 1.38 | 2.7 |
| `TOP_RATIO` 1.0 (top ride off) | -19.7 | 15.6 | **21.3** | 2.87 | 4.2 |
| `TOP_RATIO` 1.6, `RATIO` 2.6, rise delay 0.6 | -19.5 | 14.6 | 19.0 | 1.36 | 2.7 |

Giving the room to the climax (a weaker top ride) pushes the span past its limit, and buying the span back with a higher `RATIO` takes it from the slow crescendos that c30 tuned the ratio for. Raising `TARGET_I` to -19.0 is free in shape (0.5 dB more limiting, still half the 3 dB limit), but Movement I and the finale deliver at -19.5, so it would make this movement 0.5 dB louder against its neighbours. **Recommendation: keep `TARGET_I`, `RATIO` and `TOP_RATIO`.** The lower limiter figure is a gain in itself.

**Fix.** Port the finale's lines (`symphony/mvt3/reaper-v600/tools/deliver_master.py`, "mvt3 c13") into `tools/deliver_master.py`:

```python
RISE_DELAY_S = 0.0   # with the other constants; then, after _MIXJ is defined:
if os.path.exists(_MIXJ):
    RISE_DELAY_S = float((_j0.load(open(_MIXJ)).get("deliver") or {}).get("rise_delay_s", RISE_DELAY_S))
RISE_DELAY_S = float(os.environ.get("DELIVER_RISE_DELAY_S", RISE_DELAY_S))
# directly after "gdb = lift - top":
if RISE_DELAY_S > 0:
    _d = max(1, int(round(RISE_DELAY_S * 10)))
    gdb = np.minimum(gdb, np.concatenate([np.full(_d, gdb[0]), gdb[:-_d]]))
```

(`_j0` is imported only inside the `master_eq` block; import json at the top instead.) In `build/mix.json`: `"deliver": {"rise_delay_s": 0.6}`.

**Acceptance.** Delivered LRA 14-16, span not over 19.0, limiter not over 1.5 dB, no reversed crescendo or diminuendo; mp3 level over qn 219-220 at least 0.5 dB lower than without the delay on the same master.

### 3. Report the breath gaps in seconds after any tempo-map change (process; inferred from finding 1)

**What is wrong.** c51's parts diff reported "note ends moved only where a gap is defined in qn" as a side effect and did not list which gaps. Three of them were printed breaths on a protected list. The same will happen at every later change of `RAMP_SPANS` or `CAESURA`.

**Fix.** In the actor's parts diff (c51 `actor_scripts/pdiff51.py`, or a small addition to `tools/state_check.py`): for every `breathe` event of `mockup-events.tsv`, print the gap in ms from the marked part's note end to its next note-on in the old and the new parts.json, each on its own map, and flag a change of 25 ms or more or a gap under 120 ms. My table for c50 and c51 is in the scratch folder (`b1.py`, `b3.py`).

## Checked, no finding (measured)

- **Kept breaths.** No part moves inside a stretched beat (see above).
- **The delivered ending.** The mp3 ends 1.36 s after the score end; the final chord holds -36 to -42 dB for 6.0 s and falls about 40 dB in the next 1.5 s. The total gain (ride plus make-up) is flat at +17.6 to +18.0 dB from bar 86 to the end, so the morendo falls in the mp3 as in the master (bar 91: 2.1, 3.3 dB per beat in both).
- **Ride gain across the kept breaths.** It moves less than 0.02 dB across 29, 102 and 124; the rise delay changes nothing there.
- **The string theme and its return.** Bars 23-26 and 71-74 realise the same printed hairpin by the same amount (+3 to +5 dB at 68 and at 240) in c51 and in c27. The return is flatter overall (4.7 against 10.2 dB) because the print gives it p throughout and the first statement has a diminuendo to its last notes.

## Not measured by me

Wetness (the lead's third open item), string join repeatability and round-robin, S1 dips, loop pulsing and the re-bow dips. The S and re-bow figures quoted in the comparison are the actor's.

Scripts and cached data are in `/private/tmp/claude-501/mockup-loop/mvt2-c52-C/` (1.6 GB, of which 1.5 GB are the simulated delivery files in `tmp/`). I left the folder in place, as the lead's rules say not to delete files.

**Do not touch:** the printed tempo map of c51 (every `RAMP_SPANS` value, the five kept caesuras and their sizes, the fermata beat); `CAESURA_BREATH_S` 0.34, `CAESURA_BREATH_SKIP` and `CAESURA_BREATH_QN_AT` 204; the breath gaps of the other 41 marked parts (among them the woodwinds' 134 ms and the tuba's and Horn 1's 174 ms at 204, the bass clarinet's 340 ms at 196, the nine wind parts at 268); `TARGET_I` -19.5, `RATIO` 2.4, `TOP_RATIO` 2.0, `MOM_CAP_ABOVE` 3.0; the level of the ff cadence against the climax (5.8 dB under it in the master); the final chord's length and its re-bows.
