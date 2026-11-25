# Critic A, cycle 53: articulation and phrasing (on the c52 render)

Data used: `cycles/c52/rendered_build/` (parts.json, score_config.py, mockup-events.tsv, leg_leads.json, level_fits.json), the delivered stems and master in `cycles/c52/render/` (after the stem fix), the pre-fix stems in `cycles/c52/render_first/`, the c51 and c50 stems for comparison, and the actor's `S_c52.json`, `S_V2Ka/b/c/w.json`, `S_c51b.json`, `bc_lost.txt`, `rebow_c52.txt`. c51 and c52 share one tempo map, so their stems compare sample time for sample time. No REAPER, no audio setting changed, nothing deleted. Scratch folder left in place: `/private/tmp/claude-501/mockup-loop/mvt2-c53-A/` (under 1 MB, no audio; scripts `bc.py`, `early.py`, `deficit.py`, `sag.py`, `env.py`, `look.py`; results `bc.json`).

Scope: the loop lead put the one-row string lines, the lost bow changes and the remaining timing misses first. Those were measured, with the two repeat gaps that c52 left unmeasured. Not examined this cycle: tremolo, pizzicato, sul tasto tone, mutes, harp, timpani, wind and brass articulation, the solo-violin patch question, the coda and final-chord re-bows (the actor's `rebow_c52.txt` is quoted, not re-measured).

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 53. Pages read for the lead's question:

| Source | What it says | Where it applies | Does the render follow it |
|---|---|---|---|
| HO manual May 2021, p.98-99 (Legato Bow Change) | Players change bow direction inside a legato passage "out of necessity" or "for the effect"; the bow change "has a characteristic sound independent of any slur or portamento" | the 116 string notes in `bc_lost.txt`, all of them slur starts or unslurred notes (a printed new bow) | Not since c52: they play the slur transition. Their start is now the same as a join inside a slur (finding 1) |
| p.98 | A legato transition plays only between two notes with no gap; the first note of a phrase has none | all string lines on Leg Slur MAX | Followed; 268 same-row joins keep their transition |
| p.98 (Legato Slur Staccato) | Patches that give a slightly stronger attack to the first note of each phrase | phrase entries after a rest | Not used; not needed for finding 1, which concerns joined notes |
| `mockup-kit/README.md`, "Steady rhythm in fast string themes" | One row per line cures unrepeatable joins | Movement II strings since c52 | Followed, and repeatable (CHANGES.md). The cost is finding 1 |
| mvt3 `SHARED-TECHNIQUES.md` 49 | A slurred string note after a Sus MAX eighth played as a Sus MAX stroke 0.06 s early; not for soft entries | a possible alternative for the ff new-bow notes of bars 61-62 and 79 | Not used; it adds row changes, so finding 1 proposes a level fix first |

## Findings

### 1. New-bow notes on Leg Slur MAX start with a sag: 16 long notes are 3.4-7.4 dB softer than c51 for their first half second and reach their body 0.2-0.7 s after the beat (measured)

Where: the notes of `bc_lost.txt` (Leg BC MAX in c51, Leg Slur MAX with a 3-4 CC notch in c52). Worst: Violoncellos 84 (bar 29), 256 (77), 269 (81), 253 (76), 176 (54), 208 (62); Violins II 262 (bar 79), 154 (48), 210, 204, 208 (bars 61-62), 54, 48, 146; Violins I 200 (bar 60), 71 (24).

Evidence:
- Level of each string note over +0.03 to +0.55 s after the beat and over the rest of the note, c52 against c51 (`early.py`, 383 notes of 0.6 s or longer on six string tracks). The 286 notes that kept their row: 0.0 dB in both windows, none beyond 3 dB. The 97 notes that changed row: rest of the note +0.0 dB median (the stem fix restored the bodies), first half second -1.0 dB median, 16 notes at -3.4 dB or lower, 3 notes at +3.6 dB or more (Violas div 72, 87, 286).
- The 16, c52 minus c51 in 100 ms steps from the beat to +0.7 s (`deficit.py`): Violoncellos 84: -5.9 -9.5 -7.8 -6.7 -6.7 -3.6; 256: -5.1 -9.9 -8.4 -6.6 -6.7 -5.0; 269: -1.9 -2.7 -5.4 -9.8 -7.6; 253: -0.7 -0.8 -4.0 -7.4 -7.9 -7.5 -4.2; Violins II 262: -1.7 -4.8 -8.1 -6.4 -6.7 -6.6 -3.2; 154: 0.0 -4.8 -9.6 -7.3 -5.6 -4.1; 210: -4.6 -4.7 -5.5 -6.9 -2.9 -3.9; 204: -3.3 -4.0 -3.8 -7.0 -2.9 -3.3 -3.9; 208: -4.5 -3.6 -5.0 -5.3 -2.9 -3.3 -3.3; Violins I 200: -3.6 -3.8 -3.6 -5.3 -4.5 -4.2 -3.5; 71: 0.0 -5.7 -6.3 -4.0 -2.1.
- Time at which the stem stays within 3 dB of the note's body (30 ms level, body = median after +0.6 s): Violins I 200 +150 ms in c51, +690 ms in c52; Violins II 210 -45 to +570; 208 -45 to +265; 204 -45 to +180; Violoncellos 208 +35 to +400; 176 +85 to +400; 256 +40 to +255; 84 -45 to +215; Violins I 71 -45 to +355. S reads these joins on time because it follows the pitch change. The level arrives late, which is the S2 case (attack centre against the beat).
- Shape of the start (cello 188, 60 ms steps from -0.3 s): c51 -34 -35 -37 -38 -38 -38 -37 -36 -36 -35 -32 -31; c52 -34 -34 -35 -31 -34 -35 -34 -35 -38 -38 -37 -38 -37 -38 -38 -36 -35 -34. The c52 note has a 3-4 dB peak 0.1 s before the beat (the transition at the early note-on) and then lies 3-4 dB under its body until +0.6 s.
- Class comparison, notes of 1.2 s or longer, body minus the level over +0.1 to +0.5 s (`sag.py`): joins inside a slur +2.1 to +2.6 dB in both renders (the slur's own swell). New-bow notes: Violins II -1.0 dB in c51 (start above the body), +3.0 in c52; Violoncellos -1.2 to +1.1; Violins I +0.1 to +1.8. A printed new bow now starts like the middle of a slur or weaker.
- By the join measure (20 ms level, dip against the lower neighbouring body, `bc.py`): the 116 new-bow joins dip 4.4 dB (c51 4.7), the 268 joins inside slurs 4.2 dB. The join itself did not get smoother or rougher; what changed is the half second after it.
- In the master (c52 minus c51, 100 ms steps): bar 24 (qn 71) -4.0 and -3.0 dB; bar 29 (qn 84) -2.5 to -3.8 dB over 0.6 s; bar 76 (253) -2.7; bar 77 (256) -2.3; bar 54 (176) -2.1; bar 79 (262) -1.9 dB, summed string stems -2.9. Bars 61-62 lose 1.3 dB or less in the master (brass and winds cover; summed strings -2.9). The string-led theme A and A' phrases are the audible cases.
- The stem fix did not touch these starts: Violins II 262, 154, 146 and Violoncellos 188, 250 are identical in `render_first` and `render`.

Fix (level only, by stem fix; `build/level_fits.json`, read as `LEVEL_SHAPES_S`): extend `cycles/c52/actor_scripts/rowlevel52.py` from one body row per note to a start shape. For every note in `bc_lost.txt` of 0.6 s or longer, take c51 minus c52 on the stems in 100 ms steps from the beat to +0.7 s; where two or more steps exceed 2.5 dB, add points at the step centres with that gain, capped at +6 dB, with 50 ms ramps from 0 dB at the beat and back to 0 dB at +0.75 s. Example from the numbers above, Violoncellos 84: `[[0.0, 0.0], [0.05, 5.9], [0.15, 6.0], [0.25, 6.0], [0.35, 6.0], [0.45, 6.0], [0.55, 3.6], [0.70, 0.0]]`. Simulate on the stems before writing. For Violas div 87 (bar 30, the pp closing chord: 50 ms levels -44 at +0.05 s against a body of -51, then -58 to -61 from +0.75 to +1.0 s) add `[[-0.05, 0.0], [0.02, -5.0], [0.12, -5.0], [0.20, 0.0], [0.68, 0.0], [0.78, 6.0], [0.98, 6.0], [1.10, 0.0]]`. Violas div 286 needs nothing: c51 had an 8 dB hole there that c52 does not have.
If the lifted starts still read weak at ff (Violins II 204, 208, 210, 262), the next step is technique 49 of mvt3's SHARED-TECHNIQUES on those four notes only, tested in a range render twice; it adds four row changes.

Acceptance: `early.py` (first half second against c51) no string note below -2.5 dB or above +2.5 dB; every one of the 16 within 3 dB of its body by +150 ms; master at qn 71, 84, 253, 256 within 1.5 dB of c51 in each 100 ms step from the beat to +0.7 s.

### 2. Violins II, bars 22-27: five joins still sit on the unfitted 240 ms row lead and play 50-128 ms early in every pass (measured)

Where: Violins II 66, 72, 74, 75, 78 (the quarter-note arrivals of theme A). These are the five of 24 outside 60 ms, and five of the six onsets where Violins I and II are over 60 ms apart.

Evidence (`S_c52.json` against the four range passes, S in ms, all with a 240 ms lead): 66: -52, -52, -80, -93, -93; 72: -62, -62, -54, -127, -128; 74: -72, -72, -48, -74, -74; 75: -125, -125, -60, -76, -76; 78: -48, -48, -85, -82, -82. They move 30-70 ms between sessions but are never later than -48 ms. Their neighbours that got a row in the second refit read -8 to +21 ms (67.5, 73.5, 77, 77.5, 79.5; leads 140-160 ms). Violins I at the same five onsets carries 120-170 ms and reads -25 to +6 ms. `build/leg_leads.json` has no Violins II row for these five, so they were among the 12 left out of the refit.

Fix: `build/leg_leads.json`, Violins II: rows that shorten the played lead (`sq - qn` in parts.json) of 66, 72, 74, 75, 78 from 240 ms to 165, 155, 175, 165, 165 ms (as offsets from the row lead: -0.075, -0.085, -0.065, -0.075, -0.075, if the table is additive as the rows at 65 and 67.5 suggest). With these every reading above lies between -60 and +31 ms except 75 in the V2Ka/b pass (-50) and 72 in the last two (-43). Also 68: 20 ms shorter than now (260 to 240 ms) (readings -58, -58, -14, -20, -30). MIDI change, so it needs the render. Do not refit 65 (+2, +2, -22, -48, -46: it moves across zero).

Acceptance: Violins II theme A, bars 22-30, at most 1 of 24 outside 60 ms; Violins I against II over 60 ms apart on at most 2 of 24.

### 3. Bar 79: the top note of Violins I arrives 89 ms late in two sessions and sags 5-8 dB at +0.2 s, on the downbeat where Violins II are 6 dB weak (measured)

Where: Violins I 262 (B flat 6, ff, after the Sus MAX run; one of the row changes that remain), also Violins I 80 (F5, bar 27).

Evidence: Violins I 262 S +89 ms in V2Kw and in the full render (lead 150 ms; crossover +118). Stem, 30 ms steps from the beat: c51 -25 -26 -27 -29 -30 -30 -31 -32 -31 -29; c52 -25 -27 -29 -31 -33 -33 -33 -33 -33 -35 -38 -36 -34 (back to -30 at +0.5 s). With Violins II 262 (finding 1) the bar 79 downbeat is the weakest string arrival of the cadence. Violins I 80: lead 260 ms read -98 ms (two passes), lead 170 ms reads +70 and +72 ms.

Fix: `build/leg_leads.json` Violins I `"262"`: raise the played lead from 150 to 230 ms (the row is 0.09 now; I did not trace how that value maps to 150 ms, so set it by the resulting `sq - qn` in parts.json) and `"80"`: a value that gives a 210 ms lead (halfway; the two readings are 170 ms apart for a 90 ms change, so check it in a range pass before the render). Violins I 262 also takes a start shape as in finding 1, fitted on c51: about +3 dB from +0.10 to +0.45 s.

Acceptance: Violins I 262 and 80 within 40 ms by S in two passes; Violins I cadence line 0 outside 60 ms apart from 264.417.

### 4. Readings in the open list that are not start errors, and one that is a level hole (measured)

- Violoncellos 148 (+153 ms): a same-pitch repeat (D flat 4 from 146, fp, Sus MAX after a 60 ms gap). S has no pitch change to find. The stem (30 ms steps from -0.45 s) runs -39 -39 -40 -41 -44 -44 -47 -48 at the beat, then -48 -50 -51 -52 -51 -48 -46 -45 at +0.1 to +0.3 s: there is no fp spike on the cello stem, and the note is 4-6 dB softer in c52 than in c51 from +0.1 to +0.3 s (c51 -46 -45 -44 -44 -45). The fp at bar 47 is printed for Violins II, violas and basses, so no spike is owed; the hole after the beat belongs to finding 1's stem fix (+4 dB from +0.08 to +0.30 s). Take 148 out of the S line table.
- Violins I 264.417 (+63 ms): a re-bow piece of the held B flat 6, not a printed start. Take it out of the line table.
- Violins I 216 (+229 ms) and 205.949: tremolo continuation and re-bow piece, as last cycle. No change.
- Violins I 210 (+65 ms, entry): the stem is at its body from +90 ms (-25 against -22 to -24 later) after a 5 dB dip that starts 120 ms before the beat. A printed new bow at ff; acceptable. No change.
- Violin I solo 48 and 60 (+109, +72 ms): unchanged since c51, soft entries on time by level (c52 critic A). No change.

### 5. The two repeats c52 left unmeasured (measured)

- Horn 2 208 (C sharp 4, ff tenuto, bar 62): 20 ms stem level -26 before, -36 and -35 in the gap at -40 to -20 ms, -32 at the beat, -30 by +0.12 s. Dip 10 dB, re-attack present. Passes. The first 100 ms after the gap are 3-4 dB under the note before; if the horns' tenuto pair should match, lift 208 by 2 dB over 0 to +0.15 s (stem fix), otherwise leave it.
- Violas 81 (D flat 4, bar 27): -39 before, -42 and -43 at -110 to -90 ms, -41 to -43 up to -20 ms, -39 at the beat. Dip 3-4 dB (c51 2-3 dB). At the limit of S1. Fix by stem fix: `LEVEL_SHAPES_S["Violas"]` add `(81.0, [(-0.150, 0.0), (-0.135, -5.0), (-0.070, -5.0), (-0.055, 0.0)])`.

Acceptance: own-band dip at Violas 81 of 6 dB or more; Horn 2 208 unchanged.

## Do not touch

One legato row per string line and the 0.15 s keyswitch lead on the 30 row changes that remain (the 286 string notes of 0.6 s or longer that kept their row: first half second and remainder 0.0 dB median against c51, none beyond 3 dB). The 66 body level rows of the c52 stem fix (rest-of-note level of the moved notes +0.0 dB median against c51). The leads refitted in c52 for Violins I and II bars 53-60 and 70-78 and the celli (0 outside 60 ms). Horn 2 208's `REP_GAP_AT` gap. The -9 dB gap shapes at Double basses 144, 156, 168. The printed-tempo map and its five breaths.
