# Manual gaps: what the Hollywood Orchestra manuals offer that the scherzo mockup does not use

Written 2026-11-07 for the c00 port, from Movement II's ranked list (`symphony/mvt2/reaper-v600/loop/MANUAL-GAPS.md`, read it for the full evidence of each item, cited here as `M2 #n`; Movement I's list is `symphony/mvt1/reaper-v621/loop/MANUAL-GAPS.md`, `M1 #n`), re-mapped to the scherzo's bars and tracks, with what the scherzo already uses marked **in use** and the scherzo's own new items. Sources: the May 2021 HO Opus manual (`guides/eastwest-hollywood-orchestra/text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt`, cited `p.N`, PDF pages), the Dec 2025 library manual (`2025 p.N`), the installed `.oib` patch files and keyswitch maps (`~/.rpr-bridge/libs/ew_ho/ks_maps.json`, `build/ks_maps_extra.json`), `build/score_config.py`, `build/parts.json`, `build/mix.json`, `build/mockup-events.tsv`, the tools, and the two movements' `loop/LEARNINGS.md`.

Evidence labels: **measured** (a number from a render, parts.json or a patch file), **read** (read in the code, a patch file or a preference file), **inferred** (reasoned from the manual or other movements; not tested on the scherzo). Bar/qn mapping: bar b starts at qn 3(b-1).

Ranking: expected audible gain for Dan's priorities (articulations; each track's level and the blend; timpani rolls under the texture; S1-S3) in this score, which is mostly short notes at quarter 264. An actor who tries an item records the result in its section (date, cycle, measured effect, kept or reverted).

## Summary

| # | Gap | Manual | Where in the scherzo | Installed | Memory | Evidence | Status |
|---|---|---|---|---|---|---|---|
| 1 | Woodwind staccato rows (Stac DblTng RRx9, StacSs DblTng RRx9) for printed wind staccatos | p.110-111; 2025 p.69-76 | 600+ wind staccatos: Flute 1 121, Oboe 1 137, cor anglais 125, Clarinet 2 79, Flute 2 70, Clarinet 1 35, Bassoon 1 20 (the theme head in every statement, the cor anglais' pp arpeggio bars 95-100) | yes (rows in every woodwind KS Master) | 1 row per track | read (rows); M1 c39 measured the row's attack (peak +0.06..+0.16 s instead of +0.09..+0.33) | not used (c00 plays them as shortened sustains) |
| 2 | Repetition rows for the repeated notes (S1) | p.96-98, p.101, p.106, p.109-110, p.112 | the theme head's repeated staccato eighths (strings: "Repetitions TS", "Spiccato RRx9"; winds: "LegRep RRx4"); the trumpets' repeated quarters (bars 101-120, 301-320; 1TP "LegRep RRx4"); timpani motive x | yes | 1 row per track | rows read; problem inferred | not used |
| 3 | Spiccato for the leggiero staccato theme | p.91-92 | Violins I theme A "leggiero" (bars 13-28, 253-268), the fugato, the counterstatement strings | yes ("Spiccato RRx9" in every string KS Master; "1st Violins Spic RRx9.oib") | 1 row per track | read; gain inferred | not used (Stac rows; Violins I on "Staccatissimo RRx9" = V1 Stac samples) |
| 4 | Brass and clarinet dynamics on CC1 | p.101; 2025 p.61-67 | every horn, trumpet, trombone, tuba and clarinet note | yes | 0 | read (M2 #1; layer groups on cc 1) | **in use from c00** (`CC1_DYN_TRACKS`, horns on Movement II's c31 soft map, `CC1_HOLD` contrabassoon 40) |
| 5 | Hollywood Solo Violin for the bars 349-356 solo | p.75-81, p.222 | Violin I solo, qn 1044-1068 ("dolce, solo (gli altri tacet)") | **no** (not on the drive) | 0 with a separate pass | inferred | DIV A half section in use from c00 (as Movement II's solo) |
| 6 | Timpani hard sticks (Timpani Hrd KS) for bars 1-340 | p.123-126 | the score prints "hard sticks" at bar 1 and "soft sticks" at bar 341; every stroke and roll to bar 340 | yes (`Drums/Timpani/Timpani Hrd KS.oib`, same five rows and keys 24-28 as Flt) | 1 instance for a second patch, or a swap | read (rows, keys); gain inferred | not used: c00 plays Timpani Flt KS (felt) throughout, because Movement I's CC1 roll map, roll trims and right-hand table were measured on it |
| 7 | Recorded crescendo rolls (Crs) for the printed roll crescendos | p.123, p.125 | timpani rolls 101-103 (qn 300-309, into the f/ff tutti), 205-208 (612-624, into the trio's return), 301-303 (900-909, sfp <) | yes | 1 row | inferred (M2 #7) | not used |
| 8 | Expressive rows (Leg Slur Exp, Sus Exp) and slower legato velocities for the cantabile lines | p.109, p.144 | the trio tune: Clarinet 1 dolce (bars 153-168, 209-224), celli arco espress. (169-184), Violins I dolce espress. (177-184) and espress. (209-224); Oboe 1 espress. (185-196); the codetta's dolce woodwinds (225-236); the second idea's espress. lines | yes | 1 row per track | inferred (M2 #5, #6; `LEG_VEL_SPANS` exists, Movement I c40) | not used |
| 9 | Half-section patches for the basses' "div." octaves and Violins II "la metà" | p.89-90, p.222 | basses div. pizz. octaves bars 253-268 (qn 756-804, both notes on the full section); Violins II "la metà" from bar 349 (full section at -3 dB, `META_DB`) | yes (Basses Divisi, 2nd Violins Divisi DIV A/B) | about 0.7 GiB per Close-only instance | inferred | not used (violas div. on DIV B and the solo on DIV A are in use from c00) |
| 10 | Horn and trombone portato rows for tenutos | p.101 | the tutti tenuto countermelody (Hn 3-4, bars 105-120, 305-320), the trio's horn drone (Hn 3-4 tenutos, bars 153-168), Hn 4's bass-clef tenutos (bars 301-304) | yes ("Port Lng"/"Port Shrt" in 1FH, "Portato" in 1TB/1TU) | 1 row per track | inferred (M2 #9) | not used |
| 11 | Portamento legato for the printed "port." | p.97-98 | Violins I bar 214 (qn 639, C sharp 6 to F sharp 6, "port." glissando) | yes ("Leg Port MAX" row) | 1 row | read (row); `PORT_TARGETS` exists | not used |
| 12 | Round-robin reset on CC16 | p.34, p.143, p.145; 2025 p.92 | every track (repeatability; the staccato round robins) | n/a | 0 | read (M2 #10) | CC36 in use; CC16 in use from c07 (`RR_RESET_AT`, section "12. ... c07 result"), extended in c12 |
| 13 | Mid instead of Close mics on the woodwinds and horns | p.138-139 | the counterstatement winds, the trio's clarinet, oboe and horns | yes | about neutral (a swap) | inferred (M2 #4) | not used (woodwind hall send 0.6 from Movement II c29 in use) |
| 14 | A string harmonics sample for Violins I's natural harmonic E6 | p.91 | bars 141-149 (qn 420-445), "harm., change bow freely", ppp | **no row** in the 1st Violins KS Master (rows read: none is a harmonic) | - | read | the note plays as an ordinary ppp Sus/legato note; the harp harmonics (bars 149-152) take over on Harp Harmonics |
| 15 | Fixed-tempo repetition loops ("Rep Fst 170bpm" etc.) | p.109-110 | none fit: the scherzo's repeated eighths run at 528 per minute | yes | - | read | not applicable |

## 1. Woodwind staccato rows

- **Manual.** p.110-111: staccato (and staccatissimo) with double-tongue round robins, velocity = dynamic.
- **Read.** Every woodwind KS Master here has "Stac DblTng RRx9" and "StacSs DblTng RRx9" (FL, FL2, OB, EH, CL, BS, CB; ks_maps). Movement I c39 moved its fugato's wind staccatos onto "Stac DblTng RRx9" in a second pass (alias tracks): harmonic peak +0.09..+0.33 -> +0.06..+0.16 s after the onset, rise 0.18-0.22 -> 0.03-0.09 s, natural decay instead of a slice peaking at its note-off; a 0.03 s lead put the cor anglais within 0.02 s of the string staccatos it doubles; velocity is the layer (mf 82, f 96).
- **Now (c00, read in parts.json).** No wind track plays a staccato row; the printed staccatos are half-length sustains (Flute 2: 162 notes, 92 on Sus MAX and 70 on Leg Slur MAX, 70 of them printed staccato).
- **Change.** `ART_SPANS` per wind track over the staccato passages with `"mark": "staccato"` and `vel_by_cc` (Movement I's config shows the form), `STAC_LEAD_S` per track (Movement I: cor anglais 0.03), loaded as one more row on the main track (no second pass needed: the rows cost far less than an instance). Measure the attack (S2) against the string Stac rows, the level against the doubled strings, and the round-robin spread.
- **Evidence.** Rows read; gain inferred from Movement I's measurements (large: half the movement's woodwind notes).

- **c01 (2026-11-07), tried, kept.** Every printed staccato of Flute 1/2, Oboe 1/2, cor anglais, Clarinet 1/2 and Bassoon 1 on "Stac DblTng RRx9" (`ART_SPANS` 0-1128, `vel_by_cc` (22,44)...(124,118), `STAC_LEAD_S` 0.02, cor anglais 0.03). Same-pitch pair stem dips: Flute 1 3.8 -> 5.0, Oboe 1 4.1 -> 4.9 (p10 2.5 -> 0.0), Clarinet 2 2.4 -> 4.7, cor anglais 3.8 -> 4.7 dB. Level against c00: Oboe 1 +4.9, Clarinet 2 +1.5, Flute 1 -1.1, cor anglais -4.5 dB: tune the velocity table per track next. About 4 GB more memory together with c01's other new rows.

- **c02 (2026-11-07).** The per-track velocity tables (Oboe 1 -12, cor anglais +10) changed the accent-to-staccato relation by only 0.3-0.5 dB: the row's level barely follows velocity. The row was taken off Oboe 2, Bassoon 1 and Clarinet 1 to save memory (few staccatos, all doubled in tuttis).

## 2. Repetition rows (S1)

- **Manual.** Strings repetitions and Legato Slur Staccato (p.96-98); brass Legato Repetitions (p.101, p.106); woodwind Legato Repetitions RRx4 and Legato Slur Repetitions (p.109-110, p.112).
- **Read.** Strings: "Repetitions TS" (time-stretched to the host tempo, CC11 layers, velocity ignored; Movement I c42 measured the Basses' row as a fixed internal rate, check before use); winds and brass: "LegRep RRx4" (re-tongue attack within 200 ms of the previous note, NoteTimer; Movement I c37-c41), "Leg Slur Rep".
- **Where.** The theme head's two repeated staccato eighths (B-B, E-E) in every statement; the trumpets' repeated quarters (bars 101-120, 301-320, at 0.23 s spacing); the horns' repeated drone pairs in the trio.
- **Change.** First measure S1 on the c00 render (dip at each repeat in 30 ms windows, aim 3-6 dB on the master). Where it fails, `REP_ROW` spans (Movement I's form, `REP_ROW_GAP_S` (0.06, 0.15), `REP_ROW_REPEATS_ONLY` brass) on one passage per family.
- **Evidence.** Rows read; problem inferred.

## 3. Spiccato for the leggiero theme

- **Manual.** p.91-92: spiccato, a bouncing bow stroke shorter and lighter than staccato.
- **Read.** "Spiccato RRx9" in all five string KS Masters (rows listed in ks_maps); "1st Violins Spic RRx9.oib" as an individual patch.
- **Change.** `ART_SPANS` on Violins I bars 13-28 (qn 36-84) with "Spiccato RRx9" against the c00 Stac row: separation of the repeated eighths, attack time, level at mp.
- **Evidence.** Inferred.

## 4. Brass and clarinet dynamics on CC1 (in use)

- As M2 #1 and #1's c31 revision: `CC1_DYN_TRACKS = ("Horn", "Trumpet", "Trombone", "Bass trombone", "Tuba", "Clarinet ")`, `CC1_DYN_MAP_BY["Horn"]` = Movement II's soft map (CC1 57-72 at pp-mf, 86/108/120 at f/ff/fff), `CC1_HOLD = {"Contrabassoon": 40}`. The trumpets' CC1 layers were set in Movement I (1TP KS Master; Movement I c39 compared 2TP). The track gains and dynamic trims in `mix.json` are Movement I's, fitted with these maps on its own score: check the scherzo's brass levels per printed dynamic on c00.

## 5. Hollywood Solo Violin

- As M2 #3, for the bars 349-356 solo. Not installed (no Solo Violin folder on the drive). c00 plays it on `1st Violins KS Master DIV A` (`TRACK_WINDOWS`, CC1 held at 72 as Movement II c32, `mix.json` from Movement II's Violin I solo: Close only, send 0.8, width 0.2).

- **c03 (2026-11-08), tried, kept.** Clarinet 1 and 2 play every Leg Slur and Sus Non Vib note on "Leg Slur Rep" (whole-piece `REP_ROW`, the keyswitch only; Leg Slur and Sus Non Vib unload, about +0.7 thousand regions per track). The slurred repeated quarters (bars 50-54, 129, 285) dip 3.6 dB median on the stem (c02 merged, 0.0). The string repeats now use `STR_REP_NEW_BOW` (Movement I c44) instead of a row: loud strokes 6.7 dB, portato 1.5 dB (too smooth).

## 6. Timpani hard sticks

- **Score.** Bar 1: "Timpani: E, G, B, E ... hard sticks"; bar 341: "soft sticks"; bar 371 "near the rim".
- **Read.** `Timpani Hrd KS.oib` has the same rows and keys as `Timpani Flt KS.oib` (Lng 24, Sht 25, Flm 26, Rls 27, Crs 28; ks_maps).
- **Now.** One Timpani track on Timpani Flt KS (felt) for the whole movement; `score_to_parts.py` names the Flt rows directly (`ks_lookup(stem, "Timpani Flt Lng")`, the METRIC_TIMP and TIMP_RH_ALT rules), and `TIMP_CC1_MAP` / `TIMP_ROLL_TRIM_DB` were measured on the felt rolls (Movement I c12, Movement II c28).
- **Change.** Add the Hrd row names to `KS_ALIASES` (or make the timpani row names follow the patch stem), put the Timpani track on Hrd KS and window bars 341-376 onto a second timpani track on Flt KS (or keep one instance and accept hard sticks in the six soft coda strokes), dump the Hrd KS layer and right-hand tables from the .oib before reusing the Flt maps, and refit the roll levels on the first render.
- **Evidence.** Rows read; gain inferred (hard sticks are the printed colour of every stroke and roll in the Allegro).

- **c03 (2026-11-08).** The Flt "Sht" row (KS C#0) now plays the 7 printed staccato strokes that are not tie ends (`TIMP_STAC_ROW`, about 1-2 thousand regions). It did not empty the G.P. at bar 340: the Lng strokes of bars 337-338 ring on.

## 7. Recorded crescendo rolls

- As M2 #7. Read the Crs take lengths from the `.ews` headers first; at quarter 264 the printed crescendo rolls last 2.0 s (101-103) and 2.7 s (205-208, at 228).

## 8. Expressive rows and slower legato for the cantabile lines

- As M2 #5 and #6, on the trio tune and the second idea. `LEG_VEL_SPANS` (Movement I c40) sets the legato velocity per span (about 50-75 plays more of the recorded slide); "Leg Slur Exp" exists in FL, FL2, OB, EH, BS, CB; the Clarinet and Bass clarinet KS Masters have only "Sus Exp".

## 9. Half-section patches for the basses' div. and Violins II "la metà"

- **Now.** The basses' div. octaves (bars 253-268, pizz., E1+E2 etc.) play both notes on the full Basses KS Master: two full sections; Violins II "la metà" (bar 349 on) plays the full section at -3 dB (`META_DB`).
- **Change.** A "Double basses div" track on `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` (check its pizz. row) with `TRACK_SPLITS` (756, 804, "rank"), or `PIZZ` level -3 dB per note on the section; Violins II on a DIV patch from 349 via `TRACK_WINDOWS`. Memory: about 0.7 GiB per Close-only instance (M1 c35); the main project's cap is 45 GB.

## 16. (c02) Accent and slur rows tried or costed against memory

- **Sus Marc LITE** (string KS Masters, 8.5 thousand regions): tried on the nine p/mp Violins I theme heads. It plays +4..+15 dB over the staccato before it; with a per-note level step it lands at +2.0..+2.6 dB, but its 2-5 kHz front is +2..+7 dB over the body. Kept, with the steps.
- **Legato Slur Staccato** ("StacSl Leg BC + Slur + Port MAX", manual p.99; 54 thousand regions on 1st Violins, 55 on 2nd) and **Slur Runs** (p.96-97; 15 / 21 thousand): not tried, because one of them costs as much memory as all c01's new rows together. Try them only after something larger is unloaded.
- **Spiccato RRx9** on the 2nd Violins' tutti repeated eighths (#3): tried. It did not separate the pairs better than StacSs (stem dips 1.3-1.6 dB).

## 11. (c01) Portamento: tried

- c01 (2026-11-07): `PORT_TARGETS = {"Violins I": {640.0: 100}}` (the target F sharp 6 at qn 640; the critic corrected the 639 here). Rendered, not yet measured (glide length and intermediate-semitone energy for the c02 critics).

## 10-13

- As M2 #9 (portato rows), M2 #10 (CC16 reset), M2 #4 (Mid mics). For #11, `PORT_TARGETS = {"Violins I": {639.0: 100}}` loads "Leg Port MAX" (Movement I c05 did the same for its "sul A" sixth).

## Checked and not applicable to the scherzo

- Harp glissando key maps (p.72-74): no harp glissando.
- Horn con sordino: Hn 3-4 print "senza sord." at bar 73 only; no horn mute passage.
- Percussion (p.114-122, 127-132): tacet.
- String tremolo rows: no string tremolo in the score (the 17 tremolo marks are timpani rolls).
- Fixed-tempo repetition loops ("Rep Fst 170bpm" etc. in the woodwind and brass KS Masters): none matches 528 eighths per minute.

## Memory plan

- 31 instances at c00 (Movement II's 32 settled at 44 GB). The cap is about 45 GB, so the main session has room for about one more Close-only instance. Render added instances (Solo Violin if installed, divisi basses, a second timpani patch) in a second REAPER pass (`reaper_ctl.py --pass2`, `build_reaper.py --pass2`, `ALIAS_TRACKS` / `PASS2_TRACKS`, Movement I c39-c41) with the same tempo map, pre-roll, hall IR and send, and sum their stems into the master (`render_cycle.py --pass2`).
- Rows: each added row costs about 0.1-0.3 GB per track (inferred). Mics: swap rather than add.
- c02 (measured): about 4 GB per 92 thousand sample regions (count them per row with `cycles/c02/actor_scripts/rowcost.py`). Legato rows cost 10-27 thousand regions each. `ROW_REMAP` frees rows that play few notes. 31 instances with 577 thousand regions settled at 45 GB.

## 17. (c04) Trumpet double-tongue staccato and brass portato
- Tried (critic A #1, manual p.102-103): Trumpet 1's printed staccatos on 1TP "StacSs DblTng RRx9" (4,080 regions; "Stac DblTng RRx9" has 5,595). Staccato quarters now peak on the beat (+0.0..+0.02 s, Sus slices +0.06..+0.1 s) and the repeated eighths re-attack. At v50 the row plays about 6 dB over the Sus slice, so the pp bars 101-103 got -6 dB. Trumpet 2 is left on Sus slices (memory cap): the next row to add when memory allows.
- Costed, not used (#10, critic A #2): 1FH "Port Shrt" 815 / "Port Lng" 775, 1TB "Portato" 730 (its sample map also points at Solo Horn sustain folders), 1TU "Portato" 600 regions per track. About 0.2-0.3 GB for horns, trombones and tuba. Deferred on the 45 GB cap; c04 used a shorter horn re-tongue instead (Horn 3 tenuto repeats 7-11 -> 5-6 dB).
- #2 (repetition rows) no longer needs the trumpet "LegRep RRx4" idea: the trumpets' repeats are staccato.

## 10 / 17 result (c06): 1FH "Port Lng" on Horn 1
- Tried on Horn 1's slurred tenuto dotted halves, bars 210-222 (626.5-641.5, 647.5-664), velocity by CC (v62-74), with the 0.09 s re-tongue lead as REATTACK_LEAD_AT (5 ms gap). Dips 630 / 633 / 663: 11.2 / 9.4 / 9.1 -> 5.4 / 5.4 / 5.3 dB (target 3-6); 639 / 651: 3.5 / 4.8 -> 7.8 / 12.0 dB; 160-230 ms under -3 dB (shallower but wider holes). Memory unchanged at 45 GB. Keep, refit the deeper two (velocity or lead) in c07.

## 12. Round-robin reset on CC16: c07 result

- **c07 (2026-11-08), tried, kept.** New generic `RR_RESET_AT` sends Opus's reset CC (16) 0.03 qn before listed onsets inside the music: celli and basses at the heads of the "ritmo di tre battute" groups (264, 273, 282, 291) and violas and Violins II at the reprise's pizz. start (756). The celli's pizz. peaks now repeat one pattern per printed group (-49 / -48 / -41 dB). Before, a four-note cycle with an 8 dB spread ran across the groups. Next: trim the loud third member (critic C #4.2).

## 8. (c10) Slower legato velocity on a cantabile line: tried

- 2026-11-09 (c10, critic A #4): the celli's arco espress. trio tune (bars 169-184, qn 504.5-552) on Leg Slur MAX targets at v80 (`LEG_VEL_SPANS`; were 106 / 112 from `LEG_VEL_STRONG`) with 0.03 s more legato lead (`LEG_VEL_EXTRA_S` celli (85, 0.03)). Perceived joins (pcX) median -63 -> -19 ms (IQR -139..+46); probe window 66 -> 65 ms, robust SD 53 -> 49 ms. Kept. Next: the Violins I doubling at 177-184 and Clarinet 1's tune at 80-90 (the clarinet row has no Leg Slur Exp); the ff return stays at 118 / 124.

## 2. (c11) Solo horn "Leg Slur Rep MAX" for the slurred tenuto repeats: read, not used

- 2026-11-09 (c11, critic A #5): the proposal was to put Horn 1's and Horn 2's slurred repeats of bars 209-222 on the Solo Horn "Leg Slur Rep MAX" row (about +0.25 GB). Read in the patch file: the row's re-tongue groups start on RoundRobin only and its Sus Non Vib groups have no start condition, so nothing in the file limits the re-tongue to same-pitch repeats. Movement I c38 measured the same LegRep samples playing the re-tongue on every note of "LegRep RRx4". The manual says a script limits the repeats to their context; the file cannot confirm it. A repeats-only span therefore needs both rows loaded (about 17 thousand more regions per horn, about 1.5 GB for two horns) and REAPER is at the 45 GB cap.
- Not used. Still pending: an isolated test of one horn with only that row (repeat and non-repeat notes, dip at each), in a second REAPER pass or when memory allows.
- Measured on c10 against the note before the repeat: Horn 2's repeats on Sus MAX dip 4.0 / 5.8 / 3.3 dB at qn 627 / 642 / 651 (inside the 3-6 dB target). Horn 1's "Port Lng" repeats had 13-14.5 dB holes at 630 / 633 / 663, about 90-100 ms after the moved onset. c11 closed the gap before those three with `NOTE_END_AT` (63 ms -> about 20 ms); the c11 result is in cycles/c11/CHANGES.md.

## 6. (c11) Timpani stick changes on full-bar rests: found, pending

- 2026-11-09 (c11, ONE_TIME_c11 item 16): the event list now carries texts printed on full-bar rests. The timpani part has "hard sticks" (bar 1), "soft sticks" (the link bar and the coda), "G sharp muta in G / medium sticks" and the retunings. The track still plays Timpani Flt KS (felt) throughout. Candidate: Hrd KS for the Allegro and Flt for the "soft sticks" spans as in section 6 above, with the roll levels refitted. Not tried (a second timpani instance does not fit under the 45 GB cap in one pass).

## 12. (c12) Round-robin reset on CC16 before the reprise of a staccato passage

- 2026-11-09 (c12, ONE_TIME_c12 item 16): the summary row said "CC16 never"; corrected, CC16 has been in use since c07. c12 adds resets at qn 312.0 and 912.0 (the two ff tuttis' woodwind staccato passages) on Flute 1, Flute 2, Oboe 1, Cor anglais and Clarinet 2, so the passage and its reprise start on the same take. Result in cycles/c12/CHANGES.md.

## 6. (c12) Timpani hard sticks: still pending

- 2026-11-09 (c12): not tried. REAPER ends a render at 45-46 GB against the 45 GB cap, so a second timpani instance (Hrd KS for bars 1-340) does not fit in one pass. A one-instance swap to Hrd KS for the whole movement would put hard sticks on the six "soft sticks" coda strokes and needs the roll levels refitted on a first render; it stays a candidate for a cycle with no other timpani change (c12 changed the left-hand stroke velocities and the summit roll's shape).

## c13 results (2026-11-10)
- **Slur Runs** (p.96-97) tried on Violins I's slurred eighth pairs at quarter 264 (114 ms notes; one-track range renders, Leg BC MAX unloaded to pay for it): first eighth +55..+103 ms late and dominant for 0-70 ms, results differed between two renders of the same data. Rejected for this tempo; the manual's "sixteenths at about 125" (120 ms) is not met in practice here.
- **Stereo Double** (p.141; #5): the key is in the instrument's Global Group (class StereoDouble), set by mix.json `"stereo_double"`. On the Violin I solo at spread 0.4: correlation 1.00 -> 0.93, level -2.5 dB. In use on the solo; Violas div and spread 0.6 untested.
- **Velocity-layered short accent** (p.162) not needed (critic A, c13).

## c14 note
No gap was tried in c14 (the lock time went to the one-row refit). The one-row move unloaded Leg BC MAX on Violins I, Violoncellos and the solo (REAPER 45 -> 43 GB settled), which leaves about 2 GB for a gap that costs memory: #6 (Timpani Hrd KS for bars 1-340) is the first candidate. Measured for gap #3's neighbourhood: Hollywood Strings "Sus Marc LITE" does not take its level from velocity (eighths at v56-70 as loud as at v78-94).

## c15 result: per-region and per-row volume in the Opus state (not a manual feature; read in the patch files)
Tried and adopted (2026-11-11): `build_reaper.py region_gain`, `mix.json` `region_gain_db`. Per-pitch corrections on 14 tracks and Violins I's "Sus Marc LITE" row at -8 dB replace volume-envelope trims; numbers in `cycles/c15/CHANGES.md`. Misses: cor anglais A4, legato-joined horn notes. Next from this list for the faults the envelope no longer covers: #2 repetition rows (repeated-note separation), #6 timpani hard sticks, the Marcato MOD short patches (accent by CC1, manual p.93-94), Détaché (p.91).

## c16 result (2026-11-15)
- Tried and adopted, read in the patch files (not a manual feature): per-dynamic-layer and per-velocity-range volume of a row in the Opus state (`region_gain_db` `row_dyn_db`) on Flute 1, Oboe 1, Violins II, violas, celli; numbers in `cycles/c16/CHANGES.md`.
- #7 recorded crescendo rolls ("Timpani Flt Crs"): not loaded; the CC1 ramp 62 -> 104 on the "Rls" row gave +2.3 dB over bar 332 (target 4). First candidate for c17.
- #9 half-section patches: the DIV A instance now also plays the last held G sharp as the second voice of a "change bow freely" note (dips 12-13.5 -> 4-6.5 dB). The basses' div. octaves stay on the full section at velocity 42.
- Not tried: "18 Violins KS Master" (manual p.10; critic C), Legato Slur Staccato / "Leg Slur Accent MAX" for accented slur heads (p.99), SSL Transient Shaper on the timpani (p.208), #2 repetition rows, #6 hard sticks.

- c17 (2026-11-15): no gap tried (no REAPER time: disk under 30 GB). Prepared for #13 and Channel Routing (manual p.141): mix.json track key `channel_map` -> the instrument's `channelMap`; values other than 0 unverified. Stereo Double 0.6 on Violas div and woodwind Main mics: untested.
- c17, resumed (2026-11-16): close-led mics on Horn 1 (the patch's own balance direction, manual p.138-139) cure the G sharp 4 anti-phase of the Main pair; Channel Routing (`channel_map`) was not needed and is still untested.
- c20 (2026-11-17): **Legato Slur Staccato** ("StacSl Leg BC + Slur + Port MAX", p.99) and **Detache** (p.90) range-tested on the 1st Violins' slurred eighth pairs inside staccato lines (12 pairs, same-start control; cycles/c20/CHANGES.md). Pairs with a note 10 dB or more under the detached neighbours: Sus MAX 4, Detache 1, StacSl 3 (the soft pairs -10..-14 dB, the f pairs +6..+14 dB over). Detache adopted on Violins I (4 thousand regions); StacSl rejected (54 thousand regions). On 2nd Violins Detache was no better than Sus MAX. The Detache groups have no MidiVelocity: velocity does not set their level, CC11 does.
- c21 (2026-11-17): #13 Mid mic tried on Horn 3 (range test, Close -6.3 / Mid 0, no channel map): stem correlation 0.97 in the trio drone and the recall (target 0.70-0.88), drone 3.9 dB lower; Horn 1's Close-led mix 0.94-0.97. Rejected, c20 kept. Stereo Double 0.6 on Violas div adopted (correlation 1.00 -> 0.78; 0.4 gave 0.19). Woodwind Main mic offline (Close-only and Main-only range passes summed): Oboe 1 reaches correlation 0.90 at Main -6 dB under Close (now -20.6), cor anglais 0.84 at -6; not changed (250-500 Hz share unmeasured). Oboe KS Master "Sus Accent MAX" adopted on four p accents.

## 16. (c22) Accent rows on more sections: result
- Flute 1 / Flute 2 "Sus Accent MAX" (DIGEST row 240; layers 1-74 / 75-114 / 115-127) on 45 accented half notes, velocity 70 / 90, no CC11 bump: accents -2.2 / -1.4 -> +1.4 / +0.4 dB median on the full render, peak 0.22-0.30 -> 0.06-0.07 s after the beat. Adopted (+0.5 GB for the row).
- 2nd Violins / Violas "Sus Marc LITE" (manual p.91-92) with Violins I's settings: negative on a range test (Violins II's hemiola accents -47 / +49 dB against their neighbours, violas -0.8 -> -2.8 dB). Not adopted; the basses' "Marc Lng" (p.93) is untried.

## 3. (c24) Spiccato for the leggiero theme: adopted on three pitches
- 1st Violins "Spiccato RRx9" (manual p.92; 9 rotating groups, 318 ms release, already loaded) on the staccato eighths at D5, D sharp 5 and F sharp 5 only (new generic `STAC_ROW_BY_PITCH`), where every other short row blurred the same-pitch pairs. Range tests against a same-start control (cycles/c24/records/ranges.txt): separation by pitch 0.8 / 4.3 / -0.4 -> 5.7 / 9.2 / 5.1 dB (bars 16-44), D sharp 5 1.6 -> 6.3 (tutti 313-360), 4.3 -> 8.9 (reprise); 60 ms peaks 5-9 dB higher. The other pitches stay on their rows.
- Not a manual feature (read in the patch file): each 1st Violins short row has one group with no start mode ("V1 Stac rrx9" in "Staccatissimo RRx9", "V1 Stac rrx16" in "Stac RRx14", "V1 stac rrx9" in "Stac On Bow RRx9"; 721-733 ms attack, 1000 ms release) beside its RoundRobin groups. Switched off (`sus_release_cap_ms` spec `orphan_only` + `deactivate`): no note lost (166 notes, three ranges), the isolated staccato quarters' tail at +0.5 s after the peak -44..-50 -> -66..-93 dB. The 2nd Violins and Violas KS Masters have the same kind of group; their 150 ms caps already shorten it.

## c25 result: CC7 as the relative level (manual p.64, p.151)
"Volume (CC7) ... to set a loudness level relative to other instruments": the dynamic trims and several passage levels now live in a CC7 lane per track (pre-hall). The 20·log10 law was measured on one woodwind, one brass and one string KS Master (0.00-0.01 dB median residual). Harp ("Harp Sus RR", not a KS Master) not measured; it stays in the volume envelope.
- c26 (2026-11-18): no gap tried. Related find: the HO woodwind legato rows' release trails (one-shot, CC11-selected pp / mf / f, 1000-1245 ms) are reached only by trail gain, not by an AHDSR cap.

## 12. (c27) Round-robin reset placed for level, not only repeatability
- 2026-11-18 (c27, critic C #4): the celli's pizzicato round robins after a reset play -48.4 / -45.8 / -49.9 dB at the same velocity (range test, same order in two renders). Resets moved one bar before each "ritmo di tre battute" head (celli `RR_RESET_AT` 264, 270, 279, 288): heads 273 / 282 / 291 -48.4 / -48.5 / -47.2 -> -45.9 / -46.1 / -45.5 dB, +3.3 dB over the two bars after them (full render). The basses' order gave no gain (left as they were).

## 6 / 10. (c28) Timpani hard sticks adopted; portato / marcato-long tenutos rejected
- #6 (2026-11-18, critic C #2): the Timpani track plays `Timpani Hrd KS` for the whole movement (one instance; the six "soft sticks" coda strokes stay on hard sticks at v<70 -2 dB). Range test against felt (same starts): soft strokes +1.9..+5.6 dB and +9..+20 dB in the 1-5 kHz share of the first 50 ms, loud strokes -1.0..-3.2 dB and +1..+3 dB; refit by region gain (stroke rows vel<70 -2 / vel>=70 +2, roll row -1.5). Full render: 1-5 kHz share intro -28.1 -> -18.2, tuttis -17.2 -> -15.4, rolls within 1 dB. The Hrd KS velocity layers (Lng): 1-25, 26-35, 36-44, 45-54, 55-59, 60-64, 65-69, 70-74, 75-84, 85-92, 93-98, 99-110, 111-120, 121-124, 125-126, 127.
- #10 (2026-11-18, critic C #1): Basses "Marc Lng RRx4" and trombone / bass trombone / tuba "Portato" on the f tenuto quarters of the tuttis (ART_SPANS "tenuto" filter): range test negative (peaks later, trombones 6 dB softer, bass downbeat weight +1.5 -> +0.3 dB). Not adopted.

## 6 / 10. (c29) Timpani stick changes in the second pass; brass "Sus Accent MAX" and bass "Marc Sus LITE" on tenutos
- #6 (2026-11-18, critics A #1, C #3): the printed soft-stick (bars 146-224, 341-376) and medium-stick (225-288) spans play
  `Timpani Flt KS` on an alias track "Timpani soft" (`ALIAS_TRACKS`, windows 435-864 and 1020-1128) in the second render
  pass (`PASS2_TRACKS`, its own project `scherzo-v600-mockup-pass2.rpp`), so the main project keeps its 45 GB; the main
  Timpani track (hard sticks) rests there. Medium sticks on felt: felt -27.8 dB / hard -18.4 dB 1-5 kHz share of the
  strokes (c18 / c28 full renders) against a half-way target of -24. Results in `cycles/c29/CHANGES.md`.
- #10 (critic A #2, manual p.100): HB 1TB / 1TU / 1FH "Sus Accent MAX" at v70 on the ff tenuto downbeats played a darker,
  later swell than Sus MAX (peak +185..+195 ms against +165, -6 dB point +55..+90 against +25 ms, 2-5 kHz front-body
  -11..-18 dB); HS Basses "Marc Sus LITE" at v80 peaked later (+180 against +128 ms) and 4 dB louder. Rejected. Ending
  the Sus MAX tenutos 0.15 qn early (34 ms before beat 2) gave the downbeat weight (+2.0 -> +3.9 dB over beats 2-3).
