# Cycle 30, critic C: dynamics over time (render of cycle 29)

Material: `cycles/c29/render/` (31 dry stems, 4 return stems, `00_Master.wav`), `cycles/c29/mvt3-mockup-c29.mp3`, `cycles/c29/CHANGES.md`, `cycles/c29/parts_rendered.json`, `cycles/c28/render/` and `cycles/c28/mvt3-mockup-c28.mp3` for comparison, `build/mix.json`, `build/score_config.py`, `build/mockup-events.tsv`, `tools/deliver_master.py`, and the c29 actor's `deliv24.py`, `dynsteps.py` and `stops24.py`. Loudness is BS.1770 through ffmpeg ebur128 (M = momentary 400 ms; mp3 read 0.30 s later for the head). Stem levels are plain RMS on the parts.json tempo map.

Delivery simulations: I ran `tools/deliver_master.py` on the c29 master with copies of `cycles/c29/parts_rendered.json` in which only `ride_trims` was edited (`build/mix.json` linked beside it, `DELIVER_HEAD` = `cycles/c29/render_head/00_Master_head.wav`). The unedited run reproduces the delivered c29 file exactly (-14.0 LUFS, LRA 10.8, TP -1.2, p10 -21.4, limiter 5.2 dB, every bar and stop value the same). These numbers are exact for a re-delivery of the c29 master. After the c30 render they hold only as far as the new master matches c29 in those bars. "Measured" means a number from these files or simulations. "Inferred" means reasoning that no render or simulation has tested.

## Manual notes

MANUAL-READING.md has no row for cycle 30 (the plan ends at c20), so I did no fixed reading. Below are the manual and MANUAL-GAPS points behind this report's findings. I took their page numbers from DIGEST.md and MANUAL-GAPS.md and did not re-read those pages this cycle.

| Source (May 2021 HO PDF page) / gap | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.108-109; DIGEST §woodwinds (English Horn KS Master) | Woodwind sustains are looped. In the Opus KS Masters, CC1 crossfades a Sus Non Vib and a Sus Vib layer (Vib comes in over CC1 55-64), and CC11 sets the dynamic. | Cor anglais solo 699-741 on "Sus MAX" (CC1 100-110, so the vibrato layer; CC11 54-63). | Yes. The F4 (MIDI 65) of that layer plays 4-6 dB under its neighbours at the same CC values (finding 2). That is a weak sample, not a controller fault. |
| p.64, p.151 (CC7); MANUAL-GAPS Finale c26-c28 | CC7 is channel volume, 20 log10(CC7/127) on these patches. | Passage levels and trims in CC7 (`dyn_trim_to_cc7`). | Yes. I left them unchanged. |
| MANUAL-GAPS #12 (p.123, p.125, recorded crescendo rolls) | Felt Cresc rolls end on a stroke. | Timpani crescendo 1096-1108 into the final fff. | Not needed. The roll sits under the brass, and the brass accents at 1104 / 1106 set the delivery's pre-duck (left-for-later item b). |
| MANUAL-GAPS #1 (p.101, p.106, Leg Slur Accent) | Accent rows inside slurs. | Trumpets 1-2 at 968-984. | Not tested. Finding 5 says keep c29's sustain-row data there. |
| No manual page: `mix.json` `region_gain_db` (a patch-state edit of the region volumes, used in c29 on Trumpet 1 "Mute Sus" and earlier on the oboes and flutes) | Per-pitch gain on chosen rows. | Finding 2. | Not used on the cor anglais yet. |

## Answers to the coordinator's items

- **Trumpets 1-2 at bars 243-246 (qn 968-984): keep (measured).** Trumpet 1, mean of 2-qn windows from 970 to 980, c28 -38.6 / -37.7 / -34.8 / -34.0 / -45.2 / -38.1 dB, c29 -34.2 / -34.8 / -32.3 / -33.0 / -36.7 / -36.9. The largest change (+8.5 dB at 978-980) fills c28's hole and is not an overshoot. The doubling Horn 1 (printed ff, molto espr.) reads -31.0 / -33.8 / -32.6 / -34.8 / -32.2 / -33.4 over the same windows, so the f trumpets sit 0-3.5 dB under the ff horn. They sit 1-4 dB over the mf strings (Violins I -36..-52, violas -34..-36). The printed <> on the tied notes is audible: 973-976 rises from -34.8 to -30.8 at 975.5 and falls again. The master changes by +1.4 dB at most (970-972) and by 0..+0.7 elsewhere. Nothing here suggests the line is too far forward, and a trim would bring back the c28 sag under the head.
- **Cor anglais joins 701 / 734: they are weak notes, not join holes (measured).** Both are F4 (MIDI 65), and the deficit lasts the whole note, not only the crossfade. Fix in finding 2.
- **Bar 166 stop 17.6 dB: it is not the horn pans (measured).** In the last 0.15 s before the cut-off at qn 662, Flutes 1-2 came out 1.6 / 1.7 dB louder than in c28 and R Winds 1.3 dB louder. Horns 3-4 changed by 0.4 dB or less and are silent at +0.3 s. The master went from -23.2 to -22.3 dBFS before the cut-off and from -40.7 to -40.2 at +0.3 s. The stop deepened because the level before the cut-off rose, not because the tail changed. Fix in finding 3.
- **Trumpet 3 pickups 362 / 366, Trumpet 1 989, Flute 1 at 168 (measured, mostly outside this lens).**
  - Flute 1, 168-172 in 1-qn windows: -60.4 / -47.1 / -49.6 / -47.7 dB against Horn 4 at -53.3 / -52.5 / -53.3 / -54.8. The -0.3 dB "first window" is beat 1 of bar 43, before the flute's printed entry at 169. From its entry the flute leads by 3.7-7.1 dB, so this is not a fault.
  - Trumpet 1, mean of each note's body after its first 0.1 s: 988 -41.2, 989 -39.2, 991 -41.2. On this measure 989 is 2 dB over its neighbours, not under them, so I would not change it.
  - Trumpet 3: I leave the pickups to critic A.
- **LRA 10.8 and the margins (measured):**
  - f -> ff is +3.7 dB (1.7 to spare) and p10 is -21.4.
  - The final chord leads 223 by 0.5 LU on momentary maxima (final -7.6, 223 -8.1, 263 -8.3), which is exactly the floor.
  - My finding 1 alone takes LRA to 10.7; with finding 4 it is 10.8 again.
  - After the c30 render, if the final's lead over 223 reads under 0.5, re-deliver with the 883.5 ride row's 888.0-891.5 value -5.5 -> -6.0. This is post-render (deliver_master only), so it needs no REAPER time. Inferred from the additive trims; check it on the re-delivered file.
- **Scherzo and other-movement findings, checked against this render:**
  - Kept crescendo gains held to the next decrescendo: not used here, and no arrival sag found in this lens (in-bar steps 223-222 +2.8, 263-262 +1.4, 278-277 +0.9 LU).
  - Hard-stick timpani through soft passages, second instance: not applicable to a last cycle.
  - "Moving delivery ride rows off ff arrivals": the Finale's rows already end in rests or at arrivals. The 1087 / 1079.5 pre-duck before the final fff is needed (left-for-later item b).
  - The top ride eating a master step (scherzo c29): see left-for-later item a.

## Findings, ranked

### 1. Bars 95-98 (qn 376-392) are now the softest music in the delivered file, and they are printed mf -> p (worse than c28)

Where: qn 376-392, all tracks. Oboe 1 mf solo, strings and bassoon mp, decrescendo to p at 384, horns pp at 384.

Evidence (measured):
- **mp3 bar medians.** c29 -29.4 / -24.6 / -26.1 / -28.1 LU against c28 -27.3 / -24.0 / -25.0 / -25.2. Bars 95 and 98 are the two softest bars of the whole file, under the pp end of the transition (bar 50 -26.2), the bassoon solo (114-124: -21.2..-27.9) and p10 (-21.4). They are 4-8 LU under the p / pp trumpet solo of bars 51-66 (-18.8..-23.8), although the master has both passages at the same level (per-bar RMS 95-98 -44.5 / -42.4 / -45.7 / -45.1 dB, 51-60 -42.6..-45.4).
- **Cause.** c29's ruling-2 roles lowered the accompaniment by 2-6 dB (Violins II, violas and celli -4 dB, basses -6, Bassoon 2 and Horns 3-4 -2; the stems moved by exactly those amounts). The oboe stem is unchanged (-50.6 / -44.9 / -51.2 dB per bar), so the oboe now leads as intended. But the master fell 0.6-2.0 dB in these bars, and the delivery ride is already at its ceiling here (mp3 minus master = +12.8..+13.6 dB in both cycles), so the mp3 fell with it. The 4-bar passage sits between the ff codetta (bars 90-94) and the development's entry (bar 99, -17.4). The ride's smoothing cannot lift a 5.7 s gap.
- **Simulation (c29 master, one added row).** `[(376.25, 0.0), (376.75, 3.5), (391.5, 3.5), (391.9, 0.0)]`:
  - bars 95-98 -25.9 / -21.1 / -22.6 / -24.7 (c28 + 1.4 / +2.9 / +2.4 / +0.5);
  - -14.0 LUFS, TP -1.2, p10 -21.4, limiter 5.2 dB, LRA 10.7 (10.8 together with finding 4);
  - f -> ff +3.7, stops unchanged (bar 94 17.0 dB);
  - climax order unchanged.

Fix: in `build/score_config.py`, append to `RIDE_TRIMS` (a delivery ride over a passage, exempt from the per-note rule):

```
RIDE_TRIMS.append([(376.25, 0.0), (376.75, 3.5), (391.5, 3.5), (391.9, 0.0)])
```

It starts at the oboe's entry, 2.4 qn after the bar-94 cut-off (the stop is read at +0.3 s, about 374.7 qn), and ends in the gap before bar 99. Keep the c29 roles, which give the oboe its lead. Risk: low. The change is post-render only and can be checked on the delivered file.

### 2. Cor anglais F4 (MIDI 65) plays 4-6 dB under its neighbours, which makes the 701 / 734 "join dips" and a soft note at 696

Where: Cor anglais, "Sus MAX" and "Leg Slur MAX" rows. Notes at sq 696, 701 and 734 in the solo of bars 175-186. The pitch also occurs at 606-654 (ff tutti) and 868 (f espress.).

Evidence (measured; mean of each note's body after its first 0.1 s; CC1 100 and CC11 flat or rising slowly across each group, velocity 53 for all):
- 699-704 (Sus MAX): 68 -45.1, 67 -47.4, **65 -50.4**, 63 -44.4, 62 -45.5, 63 -43.2.
- 732-736: 68 -44.4, 67 -46.4, **65 -48.6**, 63 -42.6, 62 -43.2.
- 696 (Leg Slur MAX): **65 -49.6**, against 694 -49.3 and 699 -45.1.
- c28 on the legato row had the same pattern (701 -52.6 against 702 -47.9, 734 -50.3 against 735 -52.3). The weakness belongs to the pitch, not to the row change.
- On the master the note sags 2.5 / 3.4 dB for a whole quarter (0.36-0.42 s at Poco meno mosso) in an exposed solo.
- G4 (MIDI 67) is also 2-3 dB low. But Trumpet 1 doubles the cor anglais' G4 at 680 / 687 / 694 / 712 / 719, and c29's Mute Sus pitch gains were fitted against those notes. A +2 dB on G4 would widen trumpet-minus-cor-anglais from -4.9..-0.9 to about -6.9..-0.9 (inferred). Leave G4 alone. Trumpet 1 never doubles an F4.

Fix: `build/mix.json`, track "Cor anglais", add `"region_gain_db": [{"rows": ["Sus MAX", "Leg Slur MAX"], "pitch_db": {"65": 4.0}}]`. This is an Opus state change, so rebuild the Cor anglais track fully and run the state guard, as c29 did for Trumpet 1.

Expected (inferred, 20 log gain): 701 -46.4, 734 -44.6, 696 -45.6, all within the neighbours' range. 868 rises from -42.0 to about -38.0, between 866 (-41.2) and 871 (-34.6) in its f line. The ff tutti notes are masked.

Verify with the per-note body levels above on the c30 stem: no F4 more than 2 dB under the mean of its two neighbours, and the master dips at 701 / 734 under 2 dB.

Risk: low to moderate (one track rebuilt). If the lock budget is short, this is the item to drop; the dip is a 0.4 s sag, not a gap.

### 3. Bar 166 stop 17.6 dB on the mp3 (band 14.5-17)

Where: tutti cut-off at qn 662 (bar 166).

Evidence (measured): mp3 17.6 dB (c28 16.8), master 17.4 (c28 16.7). The cause is the flutes' louder last 0.15 s (see the answers above), not the tail. The bar-113 precedent: c29 raised that stop's return ride by 1.5 dB (3.0 -> 4.5), which took its mp3 stop from 17.3 to 15.3, about 1.3 dB of stop per dB of return.

Fix: `build/mix.json` `return_rides`, the row `{"stop": 662.0, "db": 0.0}` -> `{"stop": 662.0, "db": 1.0}`. Expected mp3 stop about 16.3-16.6 dB (inferred from bar 113's response). It acts on the four return tracks only, so no instrument track changes. Risk: low. If the c30 render's flutes come back at c28's level, the stop may land near 15.5, still inside the band.

### 4. The opening ff (bars 1 and 5) is within 0.6 LU of the fff C-major arrival at bar 223

Where: qn 0-8 and 16-24, the ff German-sixth chords of bars 1-2 and 5-6.

Evidence (measured, mp3 momentary maxima): bar 1 -8.9, bar 5 -8.7, bar 223 -8.1, final -7.6. In-bar maxima: bar 5 -8.7 against 223 -8.4. On the master, 223 is 7 dB over bar 1 (per-bar RMS -11.7 against -18.8). The delivery's top ride and limiter flatten the difference. Delivery spec item 2 asks for the other climaxes in printed order, and an earbud listener hears the first chord of the movement almost as loud as the arrival 6 minutes later.

Simulation (c29 master, with finding 1's row): add -1 dB to the existing bar 1-2 and 5-6 rows.
- Bars 1 / 5 go to -9.5 / -9.4, so 223 leads by 1.3 LU and 263 leads the loudest ff bar by 0.7 (was 0.4).
- -14.0 LUFS, LRA 10.8, p10 -21.4, limiter 5.2.
- Stops of bars 2 / 6 16.4 / 15.9 dB (in the band); f -> ff +3.7.
- Nothing else moved by more than 0.1 LU.

Fix: in `build/score_config.py`, append

```
RIDE_TRIMS += [[(0.0, -1.0), (8.0, -1.0), (8.25, 0.0)], [(15.75, 0.0), (16.0, -1.0), (24.0, -1.0), (24.25, 0.0)]]
```

Risk: low (post-render only).

### 5. Trumpets 1-2 at 243-246: keep the c29 data (measured; numbers in the answers above)

c29 raised the trumpets 1-8.5 dB on the stem and only +0..+1.4 dB on the master. They still sit 0-3.5 dB under the ff Horn 1 they double, and the printed swells on the tied notes are audible. A trim would bring back the c28 sag under the head. Do not revert.

### 6. No new loop pulsing; the final chord's ring is right (measured; no change)

- **Held notes of 6 s or longer:**
  - Horn 4 at 168 (6.5 s): its swings follow its CC11 phrase swells (172-174, 180.5-181.8) and the printed decrescendo at 184.
  - Timpani at 920: the printed settle.
  - Crash cymbals at 888 / 1048: 0.8 / 2.5 dB detrended range, level autocorrelation at 3.95 s +0.06 / +0.05.
  - Bass drum at 888: 1.5 dB.
- **Chorale 224-234:** 100-300 Hz band and spectral-centroid autocorrelation at 3.95 s lie between -0.12 and +0.14 on every string stem and on the master.
- **Largamente 273-278:** the basses' +0.60 band autocorrelation comes from their hammered eighths (a repeating velocity pattern), not from a held note.
- **Final chord:** falls 15.7 dB at +0.3 s on the mp3 (band 14.5-17); RT60 1.28 s (-5..-35) and 1.40 s (-5..-25), inside the recordings' 1.1-1.6 s.
- **sfp at 592:** on the master, ff -14 falls to -22 LUFS within 0.3 s and returns over about 1 s with the crescendo; the mp3 follows it (-10 -> -18 -> -10).

## Left for later (measured, not proposed for the last cycle)

a. **The delivered climaxes are compressed.** The 12 loudest bars of the mp3 lie within 1.3 LU (278 -7.6 ... 147 -8.8): 223, 263, 264, 277, 5, 247, 255, 276, 158 and 147. Most of them are ff or fff, but the arrival at 223 has only +2.8 LU in-bar over bar 222, against a master step of about +6.7 dB (per-bar RMS 222 -18.4, 223 -11.7). Widening this needs a lower top-ride ratio or more limiter headroom. Both move LRA, the limiter and the -14 LUFS target together. Not for a last cycle.

b. **The final crescendo, bars 275-277 (qn 1096-1108).**
- On the mp3 the 2-qn medians run -12.0 / -11.2 / -9.6 / -10.3 / -10.2 / -11.0, then -8.1 at the fff. The master rises 5.5 dB over the same span. The delivery's gain falls from +5.5 to +1.0 dB across it: the 1079.5 and 1087 ride rows add -1 -> -4.5 dB, and the automatic top ride does the rest.
- In-bar maxima still rise (275 -11.0, 276 -9.4, 277 -8.5, 278 -7.6), so it is not a reversal.
- The pre-duck is needed. The accented brass quarters at 1104 and 1106 (Trombones 1-2, Trumpet 2, Tuba at v127) have master sample peaks of -1.9 / -0.3 dBFS, against +0.8 / +1.3 on the final chord, and the limiter already takes 4-5 dB on them.
- Variants tried on the c29 master:
  - Removing the -1 at 1107.8 in the 1087 row raised the limiter to 6.4-6.5 dB (over spec item 5): rejected.
  - Lowering only 1096-1102 (1079.5 row: 1094 -1, 1096 -2.5, 1100 -3.0, 1104 -3.0, 1106.5 -3.0, 1107.8 -3.5) widened the in-bar rise from 275 to 278 from 3.4 to 4.5 LU, with limiter 5.2 and LRA 10.7. But it puts bar 275 1.5 LU under the ff bar 274 where no decrescendo is printed, so it is a musical judgement and not a fix.
- If the brass accents of bar 277 are ever softened (Dan: accents "a little bit over done"), the pre-duck can be shallower.

c. **The Cor anglais at the sub. p of bar 219 (qn 872-880)** sits at -64..-67 dB, 4-12 dB under the other sub. p winds (Flute 1 -55, Bassoon 1 -56, Clarinet 2 -52). It holds an inner chord tone, so this is low priority.

## Worse than c28 (for the actor's revert check; measured, mp3 bar medians)

- Bars 95 / 97 / 98: -2.1 / -1.1 / -2.9 LU. Finding 1 fixes them without reverting the roles.
- Bar 50: -1.9 (pp end of the transition, the ruling-2 roles). It is still above bar 95 and is printed pp: acceptable.
- Bar 116: -1.9, a render difference on one note (Bassoon 1 at 462, -40.5 -> -44.6 dB with identical notes, CCs, keyswitches and envelope; c28's note was the 6.7 dB outlier). No action.
- Bar 246: -1.0, inside the trumpet changes of finding 5.
- Every other bar is within 1 LU of c28, or louder as ruled (176 / 184 cor anglais, 271-275).

Do not touch:
- the trumpets' and horns' sustain-row crossfades at 243 and the cor anglais crossfades;
- the Mute Sus pitch gains;
- the c29 roles under the solos at 43-50 and 95-97 (fix their level in the delivery, finding 1);
- the bar-113 return ride (+4.5);
- the 1087 and 1079.5 ride rows, including the -1 dB at 1107.8, which keeps the limiter at 5.2;
- the 883.5 / 888 row on bar 223;
- the room bed;
- the final chord's ring (15.7 dB, RT60 1.3-1.4 s);
- the timpani roll settles;
- `ENV_MAX_DB`, the trim snaps and the role steps at note-ons.
