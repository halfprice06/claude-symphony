# Cycle 59, critic A: articulation and phrasing (accents, re-bows, string shorts, join holes)

Under review: the c58 render (`cycles/c58/render/`) and `build/` (`build/parts.json` is byte-identical to `cycles/c58/rendered_build/parts.json`). Scripts and caches (25 MB): `cycles/c59/critic_scripts/A/`. Everything is measured on the dry stems or read from the data unless marked inferred. Nobody listened. "Envelope removed" means stem level minus the written track volume envelope (`build_reaper.py` cut before `ENV_LUA`).

Not read this cycle: README.md, HISTORY.md, the LEARNINGS files, EW-TEMPLATE-PLAN.md and FINDINGS.md (I used the coordinator's notes, `cycles/c58/CHANGES.md`, my c58 report and searches of `MANUAL-GAPS.md`). `MANUAL-READING.md` has no row for c59 and I read no manual pages, so there is no "Manual notes" table. `~/.rpr-bridge/libs/ew_ho/ks_maps.json` could not be opened (access denied), so row lists come from `parts.json` `art_counts` only.

Not checked: harp, timpani and percussion technique, pizzicato, breath marks, keyswitch timing, tenuto, the brass and wind long notes for loop pulse.

## 1. Accents per track on isolated accents: spread +0.5 to +3.9 dB; the staff-count scaling removes the tutti accents; sf and fp (all families). Measured.

Method (`acc.py`, `acc_sum.py`, `acc_table.py`, `cccurve.py`, `acc_tutti.py`). Each accented note against unaccented notes of the same track, pitch and row whose CC11 is within 5 units of the accent's resting CC11 (the lane just before the note). Level = median of the 30 ms frames 0.05 to 0.35 s after the score onset, envelope removed. Isolated = neither neighbour within 1.5 qn is accented.

State. 593 accented onsets on pitched tracks; 403 carry a CC11 rise. Without one: 65 under 0.3 s, 82 at a resting CC11 under 84, 37 on Sus Marc LITE, and 78 on sustain rows of 0.3 s or more at 84 or more (the lane is at the ceiling, e.g. 566.0 at 116 on Flute 1, Oboe 1, Clarinet 1; or it falls at the accent, e.g. 548.0 from 104 to 98; or 285.0 on nine tracks). 200 accents with a rise have a match.

- Isolated accents (155): median +1.4 dB, quartiles +0.7 / +2.6, maximum +8.8. Inside +1.5 to +2.0: 16. Over +3: 32. Under +1: 63. Accents in runs (45): +0.7.
- By family and resting dynamic, isolated: strings f +3.8 (quartiles +2.9 / +4.4, n 16) and ff +1.3 (+0.7 / +3.8, n 12); winds f +1.7 (n 18) and ff +1.1 (+0.8 / +1.5, n 49); brass f +2.0 (+0.8 / +3.4, n 44) and ff +0.6 (+0.5 / +0.9, n 16).
- Per track, isolated, both dynamics: Violins I +3.8 (n 15, max +6.9), Violins II +3.8 (4), Tuba +2.7, Trombone 2 +2.7, Bass trombone +2.5, Horn 2 +2.3, Horn 1 +2.3 (max +8.8), Horn 4 +2.1, celli +1.8 (3), Contrabassoon +1.7, Trombone 1 +1.6, Horn 3 +1.5, Flute 1 +1.5, Oboe 1 +1.2, Flute 2 +1.2, Bassoon 1 +1.2, Bassoon 2 +1.1, basses +0.9, Clarinet 1 +0.9 (12), Oboe 2 +0.8, Trumpets 1 / 2 / 3 +0.6 / +0.6 / +0.5. Violas have no isolated match.
- 2-5 kHz front excess of accented notes: strings -0.3, winds -1.7, brass -3.8 dB; over +3 dB: 6 of 170. No bite.

Staff-count scaling. Matched emphasis by the number of accented staves at the onset: 1-8 staves strings +3.7 / winds +1.2 / brass +1.8; 9-15 staves +3.8 / +1.5 / +2.2; 16 or more +1.1 / +0.8 / +0.8 (n 9 / 47 / 60; median rise 5 to 8 units). The predicted rise of the dry stem sum (power-weighted mean of the tracks' matched emphasis, other sounding tracks 0) at the 11 onsets with 16 or more staves is +0.3 dB (median), at the 14 onsets with 9-15 staves +0.1. A sum in which every track rises by E dB rises by E dB, not more, so the 0.75 / 0.6 factors take the tutti accents under +1 dB per track. 260 of the 593 accents are at the 16+ onsets. I recommend `tutti_scale` off; if the coordinator keeps it, the values below must be divided by the factor at those onsets.

CC11 values per track that land an isolated accent at +1.5 to +2 dB. Source "own" = the track's own isolated accents (3 or more); "family" = the family's isolated slope (strings 0.33 dB per unit at f and 0.15 at ff; winds 0.12 and 0.14; brass 0.18 and 0.09). The per-track level fit on CC11 (`cccurve.py`, pitch as a fixed effect) is a second reading; its segments hold 0 to 30 notes per track, so I used it only where noted.

| track | f now (rise, n) | f: 88 -> | ff now (rise, n) | ff: rest -> | source f / ff |
|---|---|---|---|---|---|
| Flute 1 | +8.3 (+18, 1) | 103 | +1.5 (+10, 9) | 104 -> 116 | family / own |
| Flute 2 | none | 103 | +1.2 (+8, 8) | 104 -> 115 | family / own |
| Oboe 1 | +5.3 (+18, 2) | 101 (fit; family 103) | +1.1 (+10, 8) | 104 -> 119 | fit / own |
| Oboe 2 | none | 103 | +0.8 (+10, 3) | 104 -> 122 (expect +1.4) | family / own |
| Cor anglais | none | 103 | none | 104 -> 116 | family |
| Clarinet 1 | +0.7 (+16, 7) | 108 (expect +0.8 to +1.5) | +1.0 (+10, 5) | 104 -> 122 | own / own |
| Clarinet 2 | +1.9 (+13, 1) | 101 | +0.8 (+6, 1) | 104 -> 116 | own / family |
| Bass clarinet | none | 103 | +2.3 (+8, 1) | 104 -> 112 | family / own |
| Bassoon 1 | +1.2 (+13, 3) | 107 | +1.1 (+7, 6) | 104 -> 115 | own / own |
| Bassoon 2 | +1.8 (+13, 2) | 101 | +1.0 (+6, 5) | 104 -> 115 | own / own |
| Contrabassoon | +2.1 (+13, 2) | 99 | +1.3 (+6, 3) | 104 -> 112 | own / own |
| Horn 1 | +2.4 (+12, 3) | 97 | +0.7 (+6, 1) | 100 -> 116 | own / family |
| Horn 2 | +2.5 (+10, 4) | 95 | +0.6 (+6, 1) | 100 -> 116 | own / family |
| Horn 3 | +1.1 (+11, 3) | 105 | +1.6 (+6, 2) | 100 -> 107 | own / own |
| Horn 4 | +2.1 (+12, 2) | 98 | none | 100 -> 116 | own / family |
| Trumpet 1 | +0.2 (+8, 2) | 98 | +0.6 (+6, 3) | 100 -> 116 | family / family |
| Trumpet 2 | +0.8 (+8, 3) | 105 | +0.5 (1) | 100 -> 116 | own / family |
| Trumpet 3 | +0.7 (+12, 3) | 108 (expect +1.1) | +0.5 (+6, 2) | 100 -> 116 | own / family |
| Trombone 1 | +1.8 (+12, 7) | 100 (keep) | +0.6 (+7, 1) | 100 -> 116 | own / family |
| Trombone 2 | +3.4 (+9, 7) | 93 | +0.6 (+6, 1) | 100 -> 116 | own / family |
| Bass trombone | +3.4 (+12, 5) | 94 | +0.5 (+8, 2) | 100 -> 116 | own / family |
| Tuba | +2.7 (+10, 4) | 95 | +1.7 (+8, 2) | 100 -> 108 (keep) | own / own |
| Violins I | +3.9 (+13, 9) | 94 | +1.3 (+9, 6) | 104 -> 116 | own / own |
| Violins II | +4.6 (+8, 1) | 93 | +3.8 (+13, 3) | 104 -> 110 | family / own |
| Violas | none | 93 | none | 104 -> 116 | family |
| Violoncellos | +1.8 (+7, 3) | 95 (keep) | none | 104 -> 116 | own / family |
| Double basses | +1.2 (+5, 3) | 96 | +0.7 (+9, 3) | 104 -> 116 (fit 110; expect +1 to +1.8) | own / own |
| Horns a2 | +1.1 (+13, 1) | 98 | none | 100 -> 116 | family |
| Trumpets a2 | none | none | none | 100 -> 116 | family |

The celli do not read -0.8 on isolated accents (+1.8, n 3, quartiles +0.6 / +4.1); the c58 figure was a mixed median. Trumpets and Clarinet 1 are nearly flat between 88 and 100 (0.07 to 0.10 dB per unit); their f accents cannot reach +1.5 inside the f layer, so the values above enter the next layer for the note. Rows with n under 3 are ± 1 dB.

sf and fp. The score has sf at two onsets (78.0 Violins I and II; 160.0 on 20 staves) and fp once (128.0 basses). `SF_ARRIVAL_AT = {160.0: "ff", 78.0: "ff"}` plays them as an ff arrival, so the lane goes from the f before (86-88) to 104 (strings, winds) or 100 (brass) and then follows the printed diminuendo; Trumpet 1, Trumpet 2 and Tuba also get the accent rise on top (119). By the fits that is +5.2 dB on Violins I, +4.0 strings, +1.8 winds, +2.2 brass, about +4.5 on Trumpets 1 and 2. Measured on the stem: Violins I 78.0 is +5.2 dB over the note before and +4.5 over the note after. Over the +3 limit on strings; the three brass tracks are over too (inferred from the fit).
fp at 128.0 (basses): `FP_SPIKE = ("f", 0.12, 0.25)` holds the forte 57 ms and is at p by 0.12 s. The basses' Sus MAX peaks 140 ms after the note-on, so no forte sounds: body -44.7 dB, 13.2 dB under the note before.

Fix (`build/score_config.py`, the c58 block; `tools/score_to_parts.py` line 4554 for the lookup):
1. `ACCENT_FLAT[track]` per track from the table: `add_by_cc` = [(84, a), (88, a), (rest_ff, b), (127, b)] with a = the f target minus 88 and b = the ff target minus the resting ff; `ceil` 120 strings, 122 winds, 118 brass (now 118 / 116 / 112). Expected: every track with 3 or more isolated accents at +1.5 to +2.0 median (now +0.5 to +3.9); upper quartile under +3 (now +2.6 overall, +4.4 strings at f); 2-5 kHz excess stays under 0.
2. `tutti_scale` removed (or [(9, 1.0), (16, 1.0)]). Expected: per-track emphasis at the 16+ onsets +0.8 -> +1.5 to +2; stem sum at those onsets +0.3 -> about +1.5 (inferred).
3. sf: a top value per family in place of the ff arrival: strings 96 (Violins I +2.5, family +2.6 to +3.5), winds 110 (+2.7), brass 102 (+2.7), with the existing fall after it, and no `ACCENT_FLAT` on a note that carries sf (Trumpets 1, 2, Tuba at 160.0). If `SF_ARRIVAL_AT` only takes a dynamic name, it needs a numeric form. Target +2.5 to +3, none over +3.
4. `FP_SPIKE = ("f", 0.5, 0.9)` (forte held 0.24 s, at p by 0.43 s at q = 126). Expected: the first 0.2 s of basses 128.0 within 3 dB of the note before (now -13). This is the printed fp, not a shape added to a note.
Check after the render with `acc.py` then `acc_table.py` (isolated median, upper quartile and maximum per track).

## 2. Re-bows: the 17 holes by cause and option; loop pulse on the notes no longer split (bars 6-14, 46, 72-76, 123, 179-182). Measured; sizes after are inferred.

`rebow.py` (same definition as `faults58.py`: 80 ms or more lie 6 dB under the lower of the levels before and after), `rebow2.py` (band 0.8 to 5 times the fundamental, master and dry stems), `pulse.py`, `fold.py`, `lastchord.py`. 77 re-bow entries, 17 holes, 60 dips of 3 dB or more.

What the hole is: the lowest frame comes 60 to 270 ms after the bow change on violas and celli and the level is back within 3 dB after 0.3 to 0.9 s; on the basses 10 to 200 ms and 0.10 to 0.16 s. The written note-off gap is 14 to 60 ms. It is the new Sus MAX piece speaking slowly at CC11 21 to 88, as in c57.

| re-bow (qn, bar) | depth dB, time 6 dB under | cause | held pitch | CC11 | master dip in the note's band (scatter before) | option | after |
|---|---|---|---|---|---|---|---|
| Violins I 44.0 (12) | 14.0, 150 ms | printed: tie + downbow, f | 4.8 s | 82 | 4.0 (2.7) | alias, new bow led 0.15 s | 3-5 dB |
| Violas 32.0, 36.0 (9, 10) | 7.6 / 9.2, 220 / 150 | printed whole notes C4 | 4.8 s each | 41 / 59 | 2.7 / 3.2 (5.1 / 2.9) | alias, new bow led 0.2 s | 3-5 |
| Violas 38.65 (10) | 6.9, 90 | automatic, inside the 4.8 s whole note | 4.8 s | 70 | 0.3 (2.3) | no re-bow (`REBOW_NONE` Violas (28, 42)); also drops 30.03 and 34.69 (8.5 dB dip) | 0 |
| Violas 52.0 (14) | 8.1, 90 | printed | 6.1 s | 34 | 2.3 (0.9) | alias | 3-5 |
| Violas 296.0 (75) | 8.4, 120 | printed whole note | 4.7 s | 41 | 6.3 (6.1) | alias | 3-5 |
| Celli 180.0 (46) | 9.7, 230 | printed, after the slur | 2.0 s | 34 | 4.6 (7.0); the celli lead here (others -7 dB in band) | alias, new bow led 0.2 s | 3-5 |
| Celli 289.145, 298.37 (73, 75) | 8.0 / 11.1, 80 / 170 | automatic (`REBOW_AT`): three changes in an 8.5 s note, pieces of 1.5 to 2.6 s | 8.5 s | 34 | 2.6 / 7.5 (1.6 / 2.9) | one change: `REBOW_AT["Violoncellos"]` = [295.0] (two pieces of 4.3 s); then alias | 2 holes -> 1 dip; 0 holes with the alias |
| Celli 713.449, 717.638 (179, 180) | 7.1 / 8.6, 100 / 120 | automatic, 9 pieces of 1.9 to 2.9 s | 22.7 s | 39 | 3.0 / 5.1 (3.1 / 4.4) | pieces of 3.6 to 3.9 s (6 pieces), alias interleaved with the main track | 4-6.5 (scherzo) |
| Basses 47.0 (12) | 9.2, 120 | printed upbow | 4.9 s | 88 | 2.6 (4.0) | alias | 3-5 |
| Basses 297.045 (75) | 16.2, 160 | automatic | 11.4 s | 33 | none (-0.9) | leave, or alias if one is built for 286-304 | 16 on the stem, not in the master |
| Basses 489.716 (123) | 10.1, 80 | automatic, pedal under the tam-tam, fff | 29.3 s | 127 | 4.0 (4.4) | leave (80 ms, back in 0.14 s) | same |
| Basses 714.671, 720.004 (179, 181) | 9.4 / 11.3, 130 | automatic | 22.5 s | 39 | 3.7 / 3.8 (2.6 / 7.1) | alias interleaved | 4-6.5 |
| Basses 724.803 (182) | 9.1, 90 | automatic, last two pieces 1.5 and 2.3 s | 22.5 s | 28 | 4.2 (2.8) | no re-bow: `REBOW_NONE` basses (722.7, 729) merges them (3.8 s, under the loop) | 0 |

Config-only step (no alias): Violas 38.65, celli 289.145 or 298.37, basses 724.803 go: 17 -> 13 or 14 holes, and five dips of 6 to 9 dB go with them (Violas 30.03, 34.69; celli 37.38 and 41.38 if `REBOW_NONE` also covers celli (28, 44), whose pieces are 4.8 s notes). With one alias instance per section on Sus MAX (violas, celli, basses, and Violins I for bar 12) over 28-56, 176-182, 286-304 and 712-728: about 2 holes left (basses 297 if not covered, 489.7). For the seven printed bow changes the alias plays the new bow from 0.15 to 0.2 s before the change while the main track holds the old bow to the change; for the automatic ones it carries every second piece, changes 3 s or more apart.

Pulse on the notes no longer split. 19 string pieces lost a c57 split. Largest departure of the 100 ms level from its 1 s running median: median 4.6 dB, three at 6 dB or more. Control (19 pieces of 2.5 to 3.9 s with flat CC11, which cannot contain a loop repeat): median 4.4 dB, four at 6 dB or more. The measure does not separate the two groups, so raising `REBOW_MAX_S` to 5.2 added no pulse it can see. One exception, which is the last chord's single bow:
- Violins I 719.86 to 728 (13 s, Leg Slur MAX, CC11 26 -> 14): level SD about its trend 3.6 dB, range 11.4 dB; autocorrelation of level at 3.95 s +0.87 and of spectral centroid +0.71, both the largest value between 2 and 6 s. This is the loop pulse of Dan's item 7 on the top voice of the final chord.
- Violins II 717.13 to 728 (16 s, Sus MAX, same span): SD 1.4 dB, autocorrelation at 3.95 s -0.17.
Fix: play the Violins I last note on Sus MAX as Violins II does (`SUS_ENTRY_AT["Violins I"]` = [720.0]); if the slur into it must stay on the legato row, re-bow it once at about 724 on the alias. Expected: level SD 3.6 -> about 1.4 dB, no 3.95 s peak. Raising `REBOW_MAX_S` past 5.2 s is not supported by a measurement: I have no unsplit Sus MAX note between 5.2 and 16 s to read, and the one legato-row note pulses.

## 3. String shorts: the excess is on two rows only; a row volume restores them (bars 30, 85-96). Measured.

`shorts.py`, `shorts2.py`: loudest 30 ms frame in the first 0.2 s of every note on a Stac, Staccatissimo or Stac On Bow row (153 notes), c58 against c56 stems as mixed.

| track, row | passage | n | c58 minus c56 | velocity, CC11 now |
|---|---|---|---|---|
| Violins I, Staccatissimo RRx9 | bar 30 | 4 | +4.7 | 95, 111 |
| Violins I, Staccatissimo RRx9 | bars 94-96 | 7 | +3.2 (min +1.3, max +5.6) | 90, 92 |
| Violas, Stac RRx9 | bar 30 | 4 | +2.4 | 95, 111 |
| Violas, Stac RRx9 | bars 88-90 | 8 | +3.3 (350.5-351.5: +5.3 to +6.2; 356-359: -1.6 to +3.4) | 77, 72 |
| Violas, Stac RRx9 | bar 96 | 1 | +1.5 | 95, 104 |
| Celli, Stac RRx9 | bars 85-87 | 8 | +1.7 (339-344: +2.9 to +6.5; 345-347: -1.6) | 77, 72 |
| Celli, Stac RRx9 / Stac On Bow RRx9 | bars 117-121 | 80 | -0.5 | 96, 92 |
| Celli, Stac RRx9 | bars 129-130 | 28 | +0.1 | 98, 90 |
| Violins II, Stac RRx9 | bars 30, 91-93, 96 | 13 | +0.1 / -1.5 / +0.7 | 87-95 |

The excess is not general: Violins II and the celli's measured tremolo are at the c56 level. The spread inside a passage (SD 3 dB on violas and celli) is the per-note metric and pitch weights of c56, which are gone by rule and should stay gone. The short rows answer CC11 at 0.07 to 0.12 dB per unit on violins and violas (120 -> 72 costs 5 dB), so CC11 is a poor handle; velocity crosses sample layers (the 4.7 dB on Violins I would need 95 -> 53 by the `gg_amp` table).

Fix (`build/mix.json`, `region_gain_db`, the `all_db` form used for Violins II Sus Marc LITE):
- Violins I: `{"rows": ["Staccatissimo RRx9"], "all_db": -3.5}` (all 11 notes of the row). Expected +4.7 / +3.2 -> +1.2 / -0.3.
- Violas: `{"rows": ["Stac RRx9"], "all_db": -2.5}` (all 13 notes). Expected +2.4 / +3.3 / +1.5 -> -0.1 / +0.8 / -1.0.
- Celli: no row volume (108 of its 116 notes are at the c56 level). Bars 85-87 only: velocity 77 -> 68 over 336-348 as one span (`VEL_SET` or the short-row velocity map), -1.5 dB by the table, same layer zone (inferred).
Left audible after this: the first three eighths of each fugato entry (violas 350.5-351.5, celli 339-339.5) 2 to 4 dB over c56.

## 4. Join holes 25 -> 30: twelve are staccato gaps, three are dynamic changes, five are new because an envelope fill is gone. Measured.

`holes.py`, `holes2.py` (the definition of `faults58.py`).

- 12 of 30 are not faults: 11 joins between notes of the Stac DblTng RRx9 rows on the pass-2 stac tracks (written gap 119 ms between staccato eighths; Flute 1 stac 5, Clarinet 1 stac 3, Bassoon 1 stac 2, Oboe 1 stac 1), identical in c57, and celli 464.0 (into Stac On Bow). The detector takes any gap under 120 ms as a join.
- 3 are a dynamic change, not a hole: celli 286.0 (f Marc into pp legato; the lowest frame is 3 dB under the new note's body), Horn 2 266.0 (the earlier note has faded), Violas 168.0 in part (below).
- New in c58 with the same MIDI at the join as c57: Flute 2 560.0 (8.5 -> 14.4 dB, 130 ms), Bassoon 2 268.0 (5.9 -> 15.2, 150 ms), Violas 44.0 (6.4 -> 8.5), Violas 76.0 (7.5 -> 10.1), celli 464.0. The c57 envelope filled them (the "early" and "pre" rules). New from the c58 Marc spans: Violins II 91.0 (9.3 dB, 130 ms: the Marc LITE quarter fades before the next one).
- The real ones, with cause: (a) tongued Sus -> Sus joins of the winds with the 50 ms `WIND_DETACH` gap at pp, where the release is short and the new note speaks slowly: Bassoon 2 268.0 (CC11 33), Oboe 1 168.0 (CC11 33 -> 20, 14.2 dB, 160 ms), Flute 1 47.0 (gap 87 ms, 14.0 dB); (b) legato transitions: Flute 1 634.0 (bar 159, into the climax: 12.3 dB, 140 ms, target velocity 60 after a note at 100, lead 130 ms), Bass clarinet 700.0, Horn 3 422.0; (c) Sus Marc LITE notes of 0.86 to 0.9 s at velocity 52-63: Violins II 574.0 (14.2 dB, 190 ms); (d) Violas 353.0 and 76.0 (a Sus note of 0.16 to 0.38 s into the next).

Fixes:
1. `WIND_DETACH`: a soft form, gap 0.015 s where CC11 at the join is under 60 (new key, e.g. `"soft": {"max_cc": 60, "gap_s": 0.015}`), and the entry lead of the note after it 0.10 s. Expected: Bassoon 2 268.0 and Oboe 1 168.0 from 14-15 dB for 150-160 ms to under 8 dB and under 80 ms (inferred from the level profiles: the new note is at body level 100 ms after its note-on).
2. Flute 1 634.0: target velocity 100 (as the note before; `VEL_SET` Flute 1 634.0) and the default legato lead. Expected under 6 dB (inferred, not tested).
3. Violins II theme doubling: end the Sus Marc LITE span at 572 so that 572-576 (notes of 0.9 s at p) plays Sus MAX with the same lead class. Expected: 574.0 14.2 dB -> a legato-size dip (2-3 dB). This narrows the c58 deviation by one bar; the rest of the doubling stays.
4. Violas 168.0: the tremolo's diminuendo (160-168, CC11 104 -> 26) ends at -66 to -71 dB and the legato p that follows enters at -52: the Tremolo row falls about 15 dB further than the legato row over the same CC11. A CC11 floor for the Tremolo row on that hairpin (end value 45 in place of 26) keeps the line. Expected: step at 168.0 from 15-20 dB to about 6 (inferred).
5. Leave Violins II 91.0 and 105.0 (the row's own decay on quarters) and the staccato gaps. Count after 1 to 4: 18 real joins -> about 13; the script's count 30 -> about 25.

## Do not touch
Accent fronts (2-5 kHz excess under 0 in every family); the brass ceiling under the fff layer (118 at most); Trombone 1 and celli f accents (+1.8) and Tuba ff (+1.7); `REBOW_MAX_S` 5.2 (no added pulse on the 19 unsplit pieces); Violins II's single bow on Sus MAX through the last chord (SD 1.4 dB); Violins II and celli short rows and the celli measured tremolo of bars 117-121 (at the c56 level); the staccato gaps on the stac tracks; `SHORT_CC11_PARK = None`.
