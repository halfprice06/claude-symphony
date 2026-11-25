# Cycle 08, critic C: holistic comparison (lens C4), on the c07 render

Data: `cycles/c07/render/` (master, 31 stems, 4 returns), `cycles/c07/build_render/parts.json` and `score_config.py` (as rendered), the delivered `scherzo-mockup-c07.mp3`, the masters and mp3s of c00 and c03 (four cycles back), c05 and c06, Movement I c49/c50 and Movement II c44 masters, the finale c08 master, the Dvořák 9/i reference and the stored Brahms shares. Bar b starts at qn 3(b-1). My scripts read each cycle's own tempo map from its `build_render/parts.json`.

## Manual notes (cycle 8, slot C: group H2, May 2021 HO manual PDF pages 44-45 and 134-136, read in full; MANUAL-GAPS.md read)

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| MIDI channel modes: Multi, MPE, Omni, 1-16. In 1-16 mode CC1, CC11 and pitch bend act on that channel only (p.44) | every track: one Opus instance per track, one channel | Yes. No track layers two patches on one instance, so no mode issue |
| Virtual keyboard: CC1 "commonly" crossfades dynamic and/or vibrato layers; CC11 sets volume, or the dynamics when CC1 sets vibrato (p.45) | strings and woodwinds: CC11 dynamics, CC1 vibrato; brass and clarinets: CC1 dynamics (`CC1_DYN_TRACKS`) | Yes, both uses as the manual describes them |
| Play page: the purge control shows streaming (yellow) and purged instruments (red) (p.134) | memory: 45 GB settled at c07 | Yes. No purging is used; rows are unloaded instead (`UNLOAD_UNUSED_ROWS`) |
| Player window: mood, performance, sensitivity, envelope, Stereo Double, reverb, mic channels (p.135) | all tracks | Partly. Opus reverb is off (template returns), mics are set per track, envelope release caps are on. Stereo Double is not used, which is correct for seated sections |
| Moods: Classic = Main mics with a 3.4 s Southern California hall; Soft = Mid plus Surround/Vintage mics through Abravanel Hall, for "slower, more emotional passages"; Epic = Close + Main + Surround through a 2.8 s cathedral (p.136) | the H2 check: the trio's dolce passages (Clarinet 1 bars 153-168, Oboe 1 185-196, the codetta 225-236) and the Meno mosso (341-363) | No, and it should not be adopted. A mood is a whole-instrument preset. It would bring back the Opus hall that c06 turned off and load Mid/Surround mics (memory at the 45 GB cap). The part of "Soft" that carries over is a more distant colour on soft lyrical lines; the returns and the darker string top end (finding 3) give that without a preset |
| Snapshots store an instrument's Player settings (p.136) | rebuilds | Not needed: `build_reaper.py` writes every setting from `mix.json` |

MANUAL-GAPS items behind the findings: #3 (Spiccato RRx9 for the leggiero theme, not tried on Violins I) in finding 1; #8 (the Clarinet KS Master has only "Sus Exp" as an expressive row) in finding 2; #6 (timpani hard sticks, not used) in finding 5; #12 (round-robin reset, now used on the pizzicato) in finding 1.

## The render as a whole against c00 and c03 (measured)

Section energy (mean of bar RMS, dB), master / delivered mp3:

| section | c00 | c03 | c07 |
|---|---|---|---|
| theme A 13-28 | -38.5 / -28.5 | -37.7 / -27.7 | -38.6 / -28.5 |
| F major episode 73-88 | -29.4 / -24.8 | -33.5 / -26.5 | -35.8 / -28.5 |
| hemiola 101-104 | -17.3 / -16.9 | -17.3 / -16.2 | -18.9 / -18.5 |
| tutti A 105-120 | -20.3 / -20.0 | -20.0 / -19.1 | -20.8 / -18.8 |
| trio tune, Clarinet 1, 153-168 | -32.1 / -24.7 | -39.0 / -27.6 | -37.1 / -27.6 |
| trio climax 209-224 | -25.9 / -22.8 | -28.0 / -22.8 | -28.3 / -24.0 |
| codetta 225-240 | -33.1 / -25.9 | -40.3 / -30.1 | -38.0 / -29.1 |
| coda build 329-335 | -18.6 / -18.3 | -20.0 / -18.3 | -21.0 / -18.3 |
| summit 336-339 | -11.4 / -12.5 | -14.6 / -13.6 | -16.0 / -13.7 |
| Meno mosso and solo 341-356 | -35.3 / -28.8 | -38.1 / -29.1 | -37.6 / -29.7 |

What is now right and was wrong at c00/c03:
- The summit is clearly the loudest moment. In the delivered file bar 337 is -12.5 dB, against bar 304 -17.5, bar 104 -17.1, bar 72 -17.2 and bar 300 -15.5. At c03 the margins were 0.9-1.5 dB; now they are 3.0-5.0 dB.
- The F major episode's harp no longer dominates. The G.P. is now the hall, not the drum. The subitos at 360 and 828 keep their return tails: R Strings stays at -50..-53 dB through the first 0.3 s at 360 while the master drops 3-4 dB.
- No held note pulses at the loop period. Autocorrelation at 3.95 s on the closing Violins I G sharp (qn 1089-1124) is 0.00 for level, 0.05 for 100-300 Hz and 0.01 for the centroid; on the master over 1089-1128 it is -0.13 / 0.16 / -0.26. Horns 3-4 over the trio drone are negative.
- The hall is not drier than c05 at the cut-offs I measured. Master drop 0.3 s after the last peak: bar 56 10.9 dB (c05 9.7), bar 72 11.8 (12.4), bar 320 5.9 (6.0), the G.P. 13.7 (12.4). So c07 sits at c05's level, the dry limit Dan accepted, and is not thinner anywhere in these joins.

What still sounds most like a machine, ranked below.

## Findings

### 1. Theme A's reprise replays the opening statement sample for sample, and the head eighths are stamped inside each statement (bars 13-28 and 253-268, qn 36-84 and 756-804, Violins I) (measured; mechanism inferred)

I cross-correlated the first 60 ms of each note (level-normalised, Violins I stem, max over ±4 ms lag; identical samples read 0.97-1.00, different takes of the same pitch 0.05-0.8):
- **Reprise against statement.** Of the 48 short notes of bars 13-28 that recur at the same position and pitch in bars 253-268 (q + 720), 33 are the identical sample. That is 23 of 28 on "Staccatissimo RRx9" and 8 of 10 on "Stac RRx14". The bar-21 head (qn 60 and 780) is identical on every note.
- **Inside each statement.** The second eighth of the E-headed phrases (qn 37.5, 49.5, 73.5, 757.5, 769.5, 793.5) is the same sample in 5 of 6 phrases (0.98-1.00). The first eighth (49, 73, 769, 793) is the same in 4 of 4 (0.99-1.00).
- **What works.** The c04/c06 row alternation does break most of the rest: only 1 of 10 notes repeats from one four-bar phrase to the next.
- **The rest of the piece is at chance.** Same-pitch short notes within 12 occurrences are identical 4-5 % of the time in the strings, 7 % in the winds and 13-14 % in the basses and Clarinet 2.

So the problem is specific. The head pairs went back to "Staccatissimo RRx9" in c06 (critic A: RRx14 rang through the pair), and every head pair follows a "Sus Marc LITE" head. The row change appears to restart the round robin, so each head pair plays the row's first two takes (the manual, p.145, says Opus continues the cycle, so the restart is inferred from the identical samples). The listener hears the theme's most exposed figure, the p/mp leggiero eighths with nothing covering them, as one recorded stroke pasted in, and then the whole first statement pasted again at the reprise. In a real orchestra the reprise is where players relax into the tune. Here it is a copy.

Fix (one new row; MANUAL-GAPS #3; manual p.91-92: spiccato is the lighter bouncing stroke, the idiom for "leggiero"):
- `build/score_config.py`, `ART_SPANS["Violins I"]`: put "Spiccato RRx9" (V1 KS Master key 35, not loaded now) on every printed staccato of the reprise statement, 753-804, with `"mark": "staccato"`. Add the head pair of the statement's second phrase: 49.0-49.6, both eighths. Keep the Marc LITE heads first in the list, so they win.
- `ROW_TRIM_DB["Violins I"]["Spiccato RRx9"] = (-3.0, 80)`, as for the other V1 short rows. Remember that ROW_TRIM_DB needs a Leg neighbour (c05 learning), so check `row_trimmed` and fit the level by `note_trims.json` if it is untrimmed. Use `STAC_LEAD_S` 0.0-0.02 s for the row (V2's spiccato in the tutti spoke 15 ms late, c05).
- Count the row's regions with `cycles/c02/actor_scripts/rowcost.py` first (string short rows hold 2-8 thousand; about 0.1-0.35 GB).
- If spiccato does not fit, or memory refuses, use "Stac On Bow RRx9" instead (key 28, same cost).
- Checks after the render: reprise-against-statement identical notes 33/48 -> under 8/48; head eighths across phrases under 0.9; V1 stem pair dips in 753-804 at least 5 dB (c07 Staccatissimo pairs 6.7-8.5 dB); level of the spiccato phrases within 1.5 dB of the c07 phrases (B lens).

### 2. The trio tune in Clarinet 1 still does not sing: the same onsets fall out or stick out in both statements (bars 153-168, qn 456-504, and 209-224, qn 624-672) (measured)

Body level of each note (Clarinet 1 stem, 50-400 ms after the moved onset). I subtracted the level the CC11 and volume envelope predict (40·log10(CC11/127) + vol_db), then took the residual against a 5-note running median, which removes the phrase shape:
- Clarinet 1: residual SD 3.3 dB (456-504) and 3.0 dB (624-672), range -6.5..+8.0 and -6.1..+8.7 dB.
- Other lines with the same method: celli 504-552 2.1, Violins I 528-552 1.8 and 624-672 1.5, Violins II 1.4, Oboe 1 (185-196) 1.8, the solo violin 1.1.
- So the clarinet is still the least even legato line in the movement, as at c03 (3.1 / 3.5). c05's pitch trims did not fix it, because the outliers depend on position, not pitch: E5 is weak at 461 and hot at 498.

The same onsets misbehave in both statements (all notes are on "Leg Slur Rep"; residual, first / second statement):

| onset (first / second) | note | residual dB |
|---|---|---|
| 461 / 629 | E5, v100 | -6.3 / -5.7 |
| 466 / 634 | G sharp 4, v80 | -5.4 / -4.9 |
| 482 / 650 | D sharp 5, v100, the climb to the A5 | -6.5 / -6.1 |
| 491 / 659 | A4 | -2.9 / -3.9 |
| 493 / 661 | B4 | +3.4 / +3.8 |
| 494 / 662 | E5 | -3.4 / -4.4 |
| 498 / 666 | E5, the held phrase end, v60, 5.3 qn | +8.0 / +8.7 |

A dolce tune whose notes jump 5-8 dB at the same places in every statement sounds programmed. This is the trio's main melody, and the clarinet has it alone for 16 bars over pp harp and drone.

Fix: `build/note_trims.json`, "Clarinet 1", per score onset, about two thirds of the mean residual (the c03 rule):
- 461 and 629 +4.0;
- 466 and 634 +3.5;
- 482 and 650 +4.0;
- 491 and 659 +2.0;
- 493 and 661 -2.5;
- 494 and 662 +2.5;
- 498 and 666 -5.5.

The last one is the long final E5: apply it as a step at its moved onset, not a ramp, so the hold does not sag after the trim.

Leave `build/pitch_trims.json` "Clarinet 1" as it is (the remaining scatter is not by pitch). Target: residual SD under 2 dB in both statements, and Clarinet 1 still 6-8 dB over the harp (B lens, c07: -7.8 dB). If a note stays off by more than 3 dB after the trim, try `LEG_VEL_SPANS` 70-80 over 456-504 and 624-672 for the whole line (manual p.144: lower legato velocity plays more of the recorded slide), not per note.

### 3. Brightness (scheduled, ONE_TIME_c08 item 1): the recipe fixes the air band but leaves the presence band 1.5-3 dB too bright; add a 3 kHz cut on the violins and quiet the contrabassoon's buzz (measured, by simulation on the c07 stems)

Band shares of the master (dB of total energy):

| | 20-100 | 100-250 | 250-500 | 0.5-2k | 2-6k | 6-20k |
|---|---|---|---|---|---|---|
| scherzo c05 | -19.9 | -7.4 | -6.8 | -3.0 | -10.1 | -29.4 |
| scherzo c06 | -15.5 | -6.7 | -6.1 | -3.9 | -10.2 | -26.2 |
| scherzo c07 | -16.8 | -7.7 | -6.5 | -3.5 | -8.8 | -24.7 |
| Movement I c50 (after its shelf fix) | -15.9 | -7.9 | -6.0 | -3.5 | -9.5 | -28.1 |
| Movement II c44 | -18.9 | -7.3 | -5.3 | -4.4 | -8.6 | -24.6 |
| finale c08 | -15.9 | -9.4 | -5.8 | -2.9 | -10.8 | -26.1 |
| Dvořák 9/i / Brahms 1/ii / Brahms 4/ii | -21.7 / -8.5 / -7.9 | -6.6 / -8.8 / -7.6 | -6.3 / -6.0 / -6.3 | -3.5 / -3.8 / -4.4 | -10.5 / -12.4 / -11.8 | -28.8 / -32.2 / -32.3 |

Who makes the top end (c07 stems): Violins I carries 64 % of the master's 6-20 kHz energy and 55 % of its 2-6 kHz; Violins II 25 % and 22 %. Everything else is under 3 %, except the contrabassoon. It has 2.5 % of the 6-20 kHz band, with its own 6-20 kHz share at -21..-23 dB in bars 52-54, where it plays f/ff as the third-loudest stem (-31.6..-32.8 dB, louder than the f celli at -34..-37). It has no hall send since c07, so its reed buzz arrives dry.

Simulation: I applied each EQ to the stem spectra and summed them incoherently (the sum reproduces the master's shares within 0.2 dB):

| variant | 2-6k | 6-20k |
|---|---|---|
| c07 | -8.7 | -24.7 |
| strings family shelf (+4 dB at 4.73 kHz) off | -9.0 | -27.8 |
| Movement I c50 recipe (shelf off, V1 5 kHz shelf -4 -> -6, V2 5 kHz shelf -4) | -9.1 | -29.4 |
| recipe + 3 kHz bell -2 dB (1.5 oct) on Violins I and II | -10.1 | -29.5 |
| recipe + 3 kHz bell -3 dB (1.5 oct) on Violins I and II | -10.6 | -29.5 |

The recipe brings the air band into the reference range. The presence band stays 1.4-3.3 dB brighter than every reference, and Movement I c50 shows the same pattern: 6-20 kHz -28.1 but 2-6 kHz -9.5. The 2-6 kHz excess is what makes a string section at f sound glassy and close. c07's own note: the string Close mics went to -4.5 dB under Main, and 2-5 kHz rose from -10.4 to -8.7.

Fix in `build/mix.json` (or in the c07 mix scripts that `make_template_mix.py` does not yet fold in, ONE_TIME item 7):
- the ONE_TIME recipe as written;
- plus on Violins I and Violins II `eq` a bell at 3000 Hz, -2 dB, bw_oct 1.5 (try -2 first; -3 only if the 2-6k share stays over -10);
- on the Contrabassoon `eq` a high shelf at 4000 Hz, -6 dB, and gain -2 dB for f and ff (`dyn_trim_db` f 0.7 -> -1.3, ff 1.9 -> -0.1). That leaves it under the celli in bars 49-55 and 299-304.

Targets on the c08 master: 6-20 kHz -28.5..-30, 2-6 kHz -10..-11. Do not go under -30 in the air band: the -32 references are slow movements, and the one fast reference, Dvořák 9/i, is -28.8. Re-check the solo violin (its 2.5 kHz -5.5 shelf was set against the brighter section; it may now sit duller than the section it replaces) and the Violins I harmonic E6 at ppp (141-149).

### 4. The coda build's repeated eighths run together on the way to the summit, the weakest S1 spot of the movement (bars 329-333, qn 985-998) (measured)

Master dip at the second eighth of each Violins I same-pitch eighth pair (10 ms RMS; the lower of the level before and after, minus the minimum around the note-on), median / 10th percentile, c03 -> c07:

| passage | c03 | c07 |
|---|---|---|
| theme A | 3.4 / 2.2 | 2.6 / 2.3 |
| counterstatement | 2.1 / 1.0 | 2.7 / 2.0 |
| tutti 105-120 | 3.1 / 1.4 | 3.7 / 3.3 |
| reprise | 4.0 / 2.8 | 3.0 / 1.4 |
| tutti 305-320 | 2.8 / 2.1 | 3.4 / 1.7 |
| coda build 329-336 | 2.7 / 0.4 | **1.8 / 1.4** |

The two tuttis improved with c07's gaps and rows. The coda build got worse, and it is the passage that leads into the summit.

Stem dips at the coda pairs (985, 988, 991, 994, 997):

| track | row | stem dip median (min) dB |
|---|---|---|
| Violins I | Stac RRx14 | 12.6 (8.7) |
| violas | Staccatissimo RRx16 | 6.2 (3.8) |
| celli | Stac RRx9 | 7.9 (3.7) |
| Violins II | Spiccato RRx9 | 3.7 (2.2) |
| Clarinet 1 | Leg Slur Rep | 12.2 |
| Oboe 2 | Sus MAX | 7.0 |

Violins II is the one string section that does not separate. c02 already measured that the 2nd Violins' "Spiccato RRx9" does not separate ff pairs (1.3-1.6 dB), and c05 found it untrimmed, which is why it is loud. In the gap before the second eighth the master's energy is shared by the celli 13 %, Oboe 2 12 %, Violins I 11 %, Clarinet 1 9 %, Violins II 7 % and the timpani 7 %. So Violins II is not the only filler, but it is the only section whose own notes merge.

Fix: `build/score_config.py`:
- put the coda pairs of Violins II, 985.0-986.0, 988.0-989.0, 991.0-992.0, 994.0-995.0 and 997.0-998.0, on "Stac RRx9" with `"mark": "staccato"` and `"poly": True`, listed before the Spiccato span so they win. That is c07 critic A #3's treatment of 313 / 319 / 913 / 919, which raised those pairs to 4.7-10.4 dB.
- Use `ROW_TRIM_DB["Violins II"]["Stac RRx9"]` -4 dB as there, and give the span notes a `REATTACK_LEAD_AT` (c06 learning: span notes skip the lead rules).
- Oboe 2 plays its staccato eighths on Sus MAX (its staccato row went in c02's memory cut). If the actor has room after finding 1's row, that is the next row to restore. Otherwise leave it: its stem already dips 7 dB.

Targets: Violins II coda stem dips at least 6 dB; master coda pair dips at least 3 dB median, 2 dB at the 10th percentile; the coda build's bar levels still rising bar by bar into 336 (delivered c07: 333 -17.1, 334 -16.4, 335 -15.0, 336 -13.4).

### 5. The timpani play the whole Allegro on felt sticks; the score asks for hard sticks, and this movement's timpani are a solo voice (bars 1-340) (inferred; patch and rows read in MANUAL-GAPS #6)

The model the score names is Beethoven 9/ii, whose timpani strokes in the "ritmo di tre battute" are the movement's signature. Here the timpani motive x is just as exposed:
- In bars 91 and 94 (printed f against pp strings, the "ritmo di tre battute"), the timpani are the loudest stem by 11-22 dB (-30.8 / -30.7 dB against -51..-53 for the strings).
- In bars 9-12 they play alone.
- They lead the hemiola and the summit rolls.

The score prints "hard sticks" at bar 1 and "soft sticks" at bar 341. `Timpani Hrd KS.oib` has the same five rows and keys (Lng 24, Sht 25, Flm 26, Rls 27, Crs 28; ks_maps), so the swap costs no memory and no new row logic. The sound difference is inferred, not measured: a harder, shorter stroke with more 1-3 kHz stick in the attack, which would make the motive x strokes articulate instead of booming, and would shorten the ring that `TIMP_DAMP_AT` has to stop before the G.P.

Fix, as a contained test:
1. Dump the Hrd KS layer, round-robin and right-hand tables from the .oib with `libs/ew_ho/dump_ks.py`.
2. Add the Hrd row names to `KS_ALIASES`, so the rules that name "Timpani Flt Lng" / "Timpani Flt Sht" (METRIC_TIMP, TIMP_RH_ALT, TIMP_STAC_ROW) resolve on the new patch.
3. Point the Timpani track's patch at Hrd KS for the whole piece. The six Meno mosso strokes (bars 341-376, "soft sticks", ppp "near the rim") then play hard sticks; that is an accepted compromise until memory allows a second instance (MANUAL-GAPS memory plan: `--pass2`).
4. Re-fit after the render, before anything else: the roll levels (`TIMP_ROLL_TRIM_DB`, `TIMP_CC1_MAP`; Dan's priority 5: rolls start at the printed level and settle under the texture), the G.P. drop (keep at least 20 dB at +0.3 s; c07 20.9) and the timpani's share of the master's 30-150 Hz in the rolls (c07 12-33 %).

If the hard rolls come out louder or rougher than the felt ones, keep Hrd KS for the strokes and put the rolls back on felt with a `TRACK_WINDOWS` split at the roll spans in pass 2. Only do this if the actor has the lock time; it ranks below 1-4 because it is untested.

### 6. Flute 1's fff summit B6 sags 9 dB within a third of a second (bar 336, qn 1005) (measured)

Flute 1's arrival note at the summit (B6, 3.07 qn, "Leg Slur MAX", CC11 124, moved onset 1004.856) peaks at -24.2 dB 40 ms after the beat. It is -27..-28 at 100-280 ms, -30.0 at 300 ms and -33.0 at 360 ms. The volume envelope moves only from -0.7 to -2.0 dB over that time, so about 7 dB of the fall is the legato sample itself. The same note reads +16 dB "front over body" in the 2-5 kHz accent check because its body collapses, not because its attack is hard. The flute's top note is the highest pitch of the summit chord, and in a real fff tutti it holds and carries over the strings. Here it pokes out and drops away under them.

Fix: `build/score_config.py`, `ART_SPANS["Flute 1"]`: [{"from": 1004.8, "to": 1005.1, "art": "Sus MAX"}] (a fresh fff sustain, not a legato arrival; Sus MAX is loaded on Flute 1, 41 notes), with a `REATTACK_LEAD_AT` 0.02 s (the woodwind staccato lead, `STAC_LEAD_S` 0.02). Remove the `arrival_weight` bump at 1005 for this track if the Sus attack already stands +2 dB over 1004. Check: the B6 holds within 3 dB of its 100 ms level until 0.45 s, and Flute 1 stays at least 1.5 dB under Violins I in bars 336-338 (c06 B #1 / c05 targets for the G6 roles).

## Standing checks (Dan's ears), measured on c07

- Item 8, loop pulsing: none. Figures above under "what is now right".
- Item 9 / accents, 2-5 kHz in the first 80 ms against the body at 150-400 ms:

  | part | median dB | p90 dB |
  |---|---|---|
  | Violins I | -1.6 | 5.8 |
  | Violins II | -2.1 | 0.8 |
  | violas | -0.1 | 1.9 |
  | celli | -0.1 | 3.1 |
  | Oboe 1 | -4.4 | 2.3 |
  | Clarinet 2 | -2.2 | 1.3 |
  | Flute 1 | -0.1 | 3.7 |

  The outliers are the two Marc LITE theme heads 51 / 771 (+11; c03 level-trimmed, front known) and the sfp strokes at 899 (V1 +7, V2 +8). Flute 1's 1005 is finding 6.
- S1: findings 1 and 4. The trumpets' repeated quarters dip 7.5 dB (Trumpet 1) and 6.0 dB (Trumpet 2) on the stems in 105-120 / 305-320.
- S3: the subitos at 360 and 828 keep the return tail (above). The G.P. falls 13.7 dB 0.3 s after the last peak.
- Wetness: at c05's level, inside Dan's limit, not drier (above). The scheduled ONE_TIME item 5 (final chord RT60 1.68 s) is for the actor.

Do not touch: the summit margins and the delivery `RIDE_TRIMS` (bar 337 now 3.0-5.0 dB over every earlier arrival in the delivered file); the returns as built in c07 (fader -6, high-pass 180, IR envelope 0.5 / 0.5, low sends off) and the Main mics at the seat with the side shelves; `TIMP_DAMP_AT` 1014.5; the re-bows and fills of the held G sharps (no loop pulse); the c04/c06 row alternation inside each theme statement (it already breaks phrase-to-phrase repeats: 1 of 10); the Marc LITE heads with their level steps; the clarinets' whole-piece REP_ROW; `RR_RESET_AT` on the pizzicato groups; the solo / flute / celli roles at 349-356; the harp's caps and roles (its onsets no longer stand out in the master: 2-5 kHz first 30 ms against 100-300 ms -1.5..+2.4 dB in the episode, trio and Meno mosso, within c03-c06's range).
