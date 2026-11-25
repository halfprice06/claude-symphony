# Cycle 24, critic A: articulation and phrasing (on the cycle 23 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c24-A/`. It holds the c23-A set plus these new scripts:
- `det.py`, `det2.py`, `det3.py`: render-to-render comparison of one stem. `det3.py TRACK 22 23` lists the spans where the two renders' audio decorrelates (50 ms frames; a best-gain fit leaves a residual above -30 dB).
- `pkcmp.py TRACK 22 23`: the join spike at every legato join, compared between two renders.
- `who2.py QN`: which stems make up a master peak.
- `b78.py`: per-stem 40 ms level traces.
- The amplitude-domain notch simulation for finding 1 was run inline. It applies the `JOIN_NOTCH` envelope shape to the c23 stems and adds the difference to the c23 master.

`acc.py` was fixed: it had cycle 08 hard-coded.

Run the scripts with `CYC=23 ~/.venvs/claude-composes-reaper/bin/python`.

Delivery numbers, taken from `metrics.md` and CHANGES.md (not re-measured):
- Master: -22.5 LUFS, LRA 23.7 LU, TP -4.0 dBFS.
- mp3: -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, span 18.5 dB, limiter 1.7 dB.

None of the fixes below changes these numbers by more than about 0.1 LU (inferred: the changes are short and local).

## Checked and working (measured, c23)

- **Keyswitches.** Every keyswitch is at least 20 ms ahead of its note, except the known Ob1 207.952 (13 ms).
- **Chords and ties.** No chord goes to a legato patch. All 104 ties are held; the only re-attacks are the timpani tie strokes at 203 and 211.
- **Legato crossover medians** are -0.01..+0.06 s on every legato track.
- **Breath marks and caesuras.** Every one makes a 9-21 dB gap.
- **Tremolo.** Bars 61-64 measure 8-30 Hz shares of 0.42-0.69 on the tremolo spans.
- **Pizzicato.** Peaks spread 2-3 dB note to note.
- **Tbn1 marcato, bars 63-64.**
  - Accented notes peak at -19.6/-19.2/-21.0 dB.
  - The unaccented eighths peak at -23.3..-24.4 dB.
  - The 218 accent is +3.4 dB over the eighth before it, inside Dan's 2-4 dB.
- **The c23 changes** (unison fills, entry leads, `SWELL_CC_CAP` "*", `REP_RETONGUE_AT`) measured as the actor reported.

## 1. A transition burst before the cadence beat in the violin descent of bars 29 and 77-78 gives the master its two largest unwritten accents (+6.0 and +5.0 dB). Measured; the fix is simulated

**Where:** Violins I and Violins II in unison, plus Flute 1 at bar 78. The figure is the same in both places: a descending eighth-note run into the cadence note.
- Bar 29: the C5 to B flat 4 join at qn 86.5, one eighth before the bar 30 cadence.
- Bars 77-78: the B flat to A flat join at qn 259. This is the f arrival at "poco allargando", the end of the slur that started in bar 75.

**What is wrong.** The legato transition sample of the last step fires about 0.07-0.12 s before the beat and stands 6-8 dB over the line. The listener hears a jab just before the arrival instead of an arrival on the beat (inferred).

`pk23.py`, c23, stem peak over the louder of pre and post:

| join | Vln I | Vln II | Fl1 | master |
|---|---|---|---|---|
| 86.5 | +7.4 at -0.071 s (86.387-86.508) | +5.9 at -0.046 s (86.408-86.495) | | **+6.0** |
| 259 | +7.7 at -0.119 s (258.863-258.925) | +5.8 at -0.119 s (258.810-258.983) | +4.0 (258.863-258.930) | **+5.0** |

- `mbumps.py 2.5` puts 259 first (+5.5).
- 86.5 is not on that list because each section carries under 40% of the excess; the two sections add coherently.
- Both joins are the same in c22 and c23, and neither section decorrelates there (see finding 3), so the fix will hold.
- The other joins of the figure are clean: 85, 85.5, 86, 257, 257.5 and 258 are at most +2.1 dB on the master.

A third spot is Flute 1 at qn 266 (bar 80.33, ff, B flat 6 to A flat 6).
- The flute stem is +8.0 for 0.3 s (266.007-266.257), measured the same in c22 and c23.
- The master is +3.9 there, but 46% of that comes from the celli's normal 5-6 dB bow-pulse on their held A flat 3 (median 4.95 dB over all held cello notes). The cello part should not be notched.

**Fix:** `tools/score_to_parts.py` `JOIN_NOTCH`:
- "Violins I": add (86.38, 86.51, -5.5) and (258.85, 258.93, -5.5).
- "Violins II": add (86.40, 86.50, -4.0) and (258.81, 258.98, -4.0).
- "Flute 1": add (258.86, 258.93, -2.0) and (266.00, 266.25, -5.0). This is a new key.

**Simulated on the c23 stems** (amplitude sum, notch with 0.04 qn ramps):

| join | master before | master after | deepest point after |
|---|---|---|---|
| 86.5 | +6.0 | +2.1 | -3.1 |
| 259 | +5.0 | +1.9 | -3.5 |
| 266 | +3.9 | +2.5 | |

None of the notches opens a hole: the deepest point after is -3.1 at 86.5 and -3.5 at 259.

**Leave for now:** the c23 Vln I fill spikes at 74 (+5.1, 73.91-73.97) and 240 (+4.5, master +1.4), and Vln I 72 (+6.1, master +3.2).
- 72 and 74 sit inside a span that decorrelates between renders (finding 3).
- The 72 spike grew from +3.1 to +6.1 with no MIDI or envelope change there.
- Notch them only after finding 3 is settled, or the notch will miss again, as 73.5 did in c23.

**Check:**
- `pk23.py` on c24: master at most +3 dB at 86.5 and 259.
- `mbumps.py 2.5`: 259 drops off the list.

## 2. Horn 1's opening solo (bars 7-14, "dolce espr.") arrives late on the same intervals each time. Measured on two metrics; the stem is identical in c22 and c23

**Where:** Horn 1, Leg Slur MAX.
- The F3 to A flat 3 joins at qn 18 and 30.
- The B flat 3 to A flat 3 joins at qn 26 and 39 (the same motif each time).
- A flat 3 to G3 at 27.
- E flat 4 to E4 at 199 (bar 59.75).

| join | crossover (`leg.py`) | new partials at body -6 (`rise.py`) | old pitch -10 dB |
|---|---|---|---|
| 18 | +0.14 s | +0.13 | +0.21 |
| 26 | +0.18 | +0.16 | +0.17 |
| 27 | +0.05 | +0.15 | +0.13 |
| 30 | +0.14 | +0.14 | +0.21 |
| 39 | +0.19 | +0.12 | +0.20 |
| 199 | +0.20 | +0.27 | +0.40 |
| 22-24 and 229-232 (same solo, for comparison) | -0.04..+0.06 | -0.06..+0.09 | |

At 52 bpm, 0.18 s is 16% of a beat. In the most exposed melody of the opening, the horn lands behind the beat on every repeat of the motif (inferred).

`build/leg_leads.json` has Horn 1 entries only for 193-202. `pkcmp.py` shows Horn 1 is bit-identical between c22 and c23, so this is repeatable.

**Fix:** `build/leg_leads.json`, "Horn 1":
- "18": 0.06
- "26": 0.08
- "27": 0.05
- "30": 0.06
- "39": 0.08
- "199": 0.08

The total stays inside the 0.03-0.35 s clamp (brass `LEG_LEAD_S` 0.10). Note them in `_doc` as "c24 (A #2): opening horn solo, late on crossover and rise".

**Check:**
- `leg.py "Horn 1"` and `rise.py "Horn 1" 4096 -v` on c24: these six joins at crossover +0.10 s or less and rise-6 +0.10 s or less.
- No new Horn 1 entries in `spikescan.py 5`.

## 3. The string stems are not reproducible from render to render, so join spikes move without any change. Measured; the cause and the fix are inferred

**What I measured** (`det3.py`, c22 against c23):

Tracks with no change, or only a gain-envelope change:
- **Bit-identical (diff under -165 dB):** Horn 1, Horn 2, Harp, Trombone 1, Horns 1-2 a2, Violoncellos div.
- **Identical apart from their envelope edits:** Flute 1, Clarinet 1, Bass trombone, Tuba, Timpani, Cor anglais, solo violin.

Violins I had the same notes, keyswitches and CC in c22 and c23; only `vol_db` changed. Even so, 11% of its active 50 ms frames are different audio (residual near 0 dB after a gain fit). The longest spans:
- qn 71.84-74.66 (the a' theme)
- 197.3-199.7
- 212.6-216.6 (tremolo)
- 242.9-244.7
- 248.9-250.1
- 255.8-257.5

The same happens in other string tracks at places where their notes did not change:
- Violins II: 179.8-181.4, 188.7-191.2, 197-204.6.
- Violoncellos: 197.8-200.1, 218.0-218.9.
- Violas: 190-197 and long coda spans.

`pkcmp.py`: of 95 Vln I legato joins, 7 changed by more than 2 dB.
- Some have no envelope cause: 72 +3.1 -> +6.1, 244 +5.4 -> +2.3, 257 +2.2 -> -0.6.
- The c23 actor's 73.5 spike "0.1 qn later with notes and envelope unchanged" is the same effect.

Every `JOIN_NOTCH` and fill tuned on one render of a string legato line can therefore miss on the next. This explains part of why the spike list keeps refilling (35 entries now, 37 in c22).

**Likely cause (inferred).** Opus keeps round-robin and repetition state between plays. The HO manual (`EW-Hollywood-Orchestra-Opus-Edition-User-Manual.txt`, "Round Robin Reset", around line 3447) says playback "will be subtly different" on a second play because "Opus remembers which sample should be played the next time". The same section says the Repetition script uses "randomized effects".

Every string KS Master in this project has:
- a `Repetition3` filter, active, with `RESET_RANDOM_TIME` 60 and `DETUNE_INTENSITY` 50;
- `controller_36` "Repetition: Reset RR";
- `controller_69` "Repetition" in its `controllerMap`.

The brass and wind KS Masters have the same filter but rendered identically, so the string legato or bow-change scripts may carry the variable state. That is not proven.

**Fix:**
1. In `tools/score_to_parts.py` (or `build_reaper.py`), send CC36 = 127 on every track at qn 0.05, ahead of the first keyswitch and note. This is the HO manual's CC 36 "Round Robin Reset, any value triggers reset" (CC table at about line 3357). It is a `--midi-only` change. It does not change the sound, only the starting state.
2. On the string tracks (Violins I/II, Violas, Violoncellos, Double basses and the div/solo tracks), also send CC69 = 0 at qn 0.05. This turns the Repetition script off (CC 69, 0-63 OFF in the same table). The same-pitch string repeats are already merged with a CC11 notch (c03), so the script has nothing musical to do here (inferred).
3. Verify before trusting any new notch in the variable spans:
   - Render once more without changes, either a short time-selection render of bars 22-30 and 57-64 or the next full cycle.
   - Run `det3.py "Violins I" 24 25` (and Vln II, Violas).
   - The target is 0% decorrelated outside edited envelopes.
   - If CC36/CC69 do not make the strings reproducible, the next test is `Repetition3` `active: False` in `state_for()`. That is a state change and needs a full rebuild, so combine it with the finding 4 reload.

After the first reproducible render, re-run `spikescan.py 5` and `mbumps.py 2.5` and re-check the c18-c23 `JOIN_NOTCH` entries in the variable spans: Vln I 71.90/73.37/249.37, Vln II 242.99/245.39, Violas 161.86/286.

## 4. Every KS Master still loads its default rows that this score never plays; unloading them cuts memory without changing a note. Measured on the patch states; the memory saving is inferred

The brief (item 7) requires the render to end below about 45 GB. It ended at 63 GB with 44 GB compressed.

`load_articulations()` in `tools/build_reaper.py` only adds rows. It never unloads the rows a KS Master loads by default.

Dumped from each track's patch plus its `art_counts`/`first_art`, the loaded but unused rows are:

| tracks | unused rows still loaded |
|---|---|
| all winds | Sus Accent (MAX), StacSs DblTng RRx9 (RRx5 BCl/Cbn), Stac DblTng RRx9, Marc (Shrt) DblTng RRx4. Plus Leg Slur MAX on Ob2, Cl2, Bn2 and Cbn, which play Sus only |
| Horns 1-4, Horns 1-2 a2 | Sus Accent MAX, StacSs RRx9, Marc Shrt RRx4, Marc Lng RRx4. Plus Sus MAX on Hn1 and the a2, and Leg Slur MAX on Hn3/Hn4 |
| Tbn2, Bass trombone, Tuba | Sus Accent MAX, Leg Slur MAX, StacSs DblTng RRx9, Marc Shrt RRx4, Marc Lng RRx4. Tbn1: Leg Slur MAX, StacSs, Marc Shrt |
| Violins I/II, Violas, Violoncellos, Double basses, and the four div/solo tracks | Sus Marc LITE, Staccatissimo RRx9/RRx16, Stac On Bow RRx9, Marc Shrt RRx4 (Vln II also Marc Lng RRx4). Plus Sus MAX on the legato-only tracks (Vln I, Vln II, solo, Vc div, Vln II div, Vla div) and Leg Slur MAX on Cb and Vln II div |
| Timpani | Timpani Flt Sht, Flm, Crs (only Rls and Lng play) |

The number of sample files per articulation folder on the drive (Close mic) gives a proxy for the cost. Preload memory is per file (Opus manual, streaming preferences), so this proxy is inferred.
- **Flute.** StacSs 999, Stac DbTg 999 and MarcSh 444 files are unused. The used LegSl has 2,196 and the sustains about 450. Unused is about half of what the flute loads.
- **1st Violins.** Staccatissimo 3,008, Stac 1,692 and Marc Short 564 files are unused, about 30% of the track's load. The used set is LegSl 3,888, LegBc 2,910, LegPt 3,888, the sustains 1,663 and Trem 184.

The RRx9/RRx16 short rows are the largest unused items, and every one of the 32 tracks carries three or four of them.

**Fix:** in `load_articulations(inst, used)`:
- For instruments that have an `articulations` block, set `row["loaded"] = False` and `row["active"] = False` for every row whose name is not in `want`.
- Keep `first_art`.
- Leave the Harp patches (no articulations block) as they are.

Notes for the rebuild:
- It is a state change, so every track needs a full rebuild. Do it in one pass with REAPER restarted.
- Then record the REAPER memory before and after a render in CHANGES.md, as the brief asks.
- The keyswitch positions do not move.
- A keyswitch to an unloaded row is ignored (c02), and none are sent, because `want` is built from the sent keyswitches.

**Second step, only if the render is still over 45 GB:** drop `PORT_TARGETS` (Vln I 82/172, Vln II 82/172, Vc 83).
- Leg Port MAX is the largest legato row: 3,888 files per mic in 1st Violins.
- It is loaded on three tracks for two or three notes each.
- Vln I 172 on Leg Port is late (+0.17 s) and spikes +5.7.
- Those notes would go back to Leg Slur MAX.

**Check:**
- The render memory figure in CHANGES.md: below 45 GB.
- `det.py` on the tracks that are otherwise unchanged (Horn 1, Harp, Tbn1): the audio is still bit-identical to c23, which shows that unloading changed no sound.

## Not findings, checked

- **Repeats.** Horn 4 and bass clarinet repeats at 9/12/15 dip 1.5-2.3 dB after `REP_RETONGUE_AT` (target 2.5). A real re-tongue at pp is small, and the horn's release tail fills the 70 ms gap. Not worth a longer gap.
- **Late joins.** Clarinet 1 252 (+0.25 s) and Violas div 71 (+0.24 s) are single late joins in inner voices. They are not exposed.
- **Celli's bow-pulse.** The celli's 2 Hz, about 5 dB pulse on held notes is the same in c22 and c23 (median 4.95 dB p-p). It is the patch's own bowing and has been handled by the loop profiles since c17.
- **Patches.** Nothing better is on the drive for this lens. There is no muted horn (the Solo and 2 French Horns patches have only stopped-horn rows) and no solo violin library.
  - The individual DIV A/B patches (for example "1st Violins Leg Slur MAX DIV A", "2FH Leg Slur MAX", "2nd Violins Flautando DIV B") would play the same samples as the rows the div/solo/a2 tracks use now.
  - Finding 4 gets the same memory saving without a patch swap.

**Do not touch:**
- The c22 pull pad.
- The c23 entry leads and entry fills.
- The c23 unison fills, except Vln I 74/240, which are on hold until finding 3 is settled.
- `REP_RETONGUE_AT`, `SWELL_CC_CAP` "*" and `SOST_JOIN_LEAD_S`.
- The c21-c23 `JOIN_NOTCH` entries outside the variable spans named in finding 3.
- The Tbn1 accents and marcato.
- The tie handling, keyswitch placement, the CC15/`mute_eq` mutes, the pizz. and harp steps, the timpani tie strokes and the caesura breaths.
- `LEG_LEAD_S` family values and the existing leg_leads.
