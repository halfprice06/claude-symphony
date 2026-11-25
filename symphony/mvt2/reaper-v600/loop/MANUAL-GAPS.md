# Manual gaps: what the Hollywood Orchestra manuals offer that the movement II (v600) mockup does not use

Written 2026-11-06 for the series 2 port (c27), by re-mapping Movement I's ranked list (`symphony/mvt1/reaper-v621/loop/MANUAL-GAPS.md`, written after its c34; read it for the full evidence, cited here as `M1 #n`) to movement II's bars and tracks, and adding what movement II has that movement I has not. Sources: the May 2021 HO Opus manual (`guides/eastwest-hollywood-orchestra/text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt`, cited `p.N`, PDF pages), the Dec 2025 library manual (`2025 p.N`), the installed `.oib` patch files, `build/score_config.py`, `build/parts.json`, `build/mix.json`, `build/mockup-events.tsv`, the tools, Movement I's `loop/LEARNINGS.md` (`M1 cNN`), `mockup-kit/LEARNINGS.md` (`KIT §n`) and series 1's `loop/HISTORY.md` (`S1 cNN`).

Evidence labels: **measured** (a number from a render, parts.json or a patch file), **read** (read in the code, a patch file or a preference file), **inferred** (reasoned from the manual or other measurements; not tested on movement II). Bar/qn mapping: BRIEF.md "The music".

Ranking: expected audible gain for Dan's priorities (articulations; each track's level and the blend; timpani rolls under the texture; S1-S3). An actor who tries an item records the result in its section (date, cycle, measured effect, kept or reverted).

## Summary

| # | Gap | Manual | Where in v600 | Installed | Memory | Evidence | Tried |
|---|---|---|---|---|---|---|---|
| 1 | Brass and clarinet dynamics on CC1 (their KS Masters crossfade the dynamic layers with CC1, not CC11) | p.101; 2025 p.61-67 | every horn, trombone, tuba and clarinet note; Horn 1's solos, the bar 61-64 and 79-82 climaxes, Clarinet 1's coda solo | yes | 0 | read (M1 c09: layer groups' cc1 rescalers); movement II measured CC1 53-87 on all of them (parts.json) | Movement I since c09; **movement II c30: done, kept** |
| 2 | Repeated notes on the library's repetition rows, and the slurred tenuto repeats (S1) | p.96-98, p.101, p.106, p.109-110, p.112 | Vln II portato pairs bars 15-21 (18 tenutos), violas' portato eighths bars 48-51 (15), wind/brass re-tongued repeats (bars 47, 50, 64, 80: 12 notes) | yes | 1 row per track | rows read (M1 #2); problem inferred for movement II | never |
| 3 | Hollywood Solo Violin for the bars 17-22 solo | p.75-81, p.222 | Violin I solo, qn 48-65 ("solo, senza sord., dolce") | **no** (licensed) | 0 with a separate pass | inferred; the DIV A half section plays it now (S1 c10) | DIV A track since S1 c10 |
| 4 | Mid instead of Close mics on the woodwinds and horns | p.138-139, p.222 | Horn 1 bars 7-14, Oboe 1 15-22 and 45-47, bass clarinet 31-36, Flute 1 and cor anglais 37-50, Clarinet 1 85-89 | yes | about neutral (a swap) | inferred (M1 #4) | never |
| 5 | Expressive rows (Leg Slur Exp, Sus Exp) for the espr./dolce wind solos | p.109; 2025 p.69-76 | Oboe 1 "dolce" 42 and "dolce espr." 139, BCl "solo, espr." 91, Fl1 "dolce cantabile" 108, CA "dolce" 93, "solo, dolce cantabile" 124, "solo, espr." 151, "dolce" 286, Cl1 "dolce" 280 | yes | 1 row per track | inferred (M1 #5) | never |
| 6 | Slower legato transitions (target velocity 60-75) on the cantabile string lines | p.144, p.99 | Vc "cantabile, sul D" bars 23-28 (qn 66-84) and 71-74 (238-250); Vln I/II "sul A, cantabile" bars 53-56 (171-188); Vln I/II "espr." bars 71-77 | yes | 0 | script read (M1 #8), gain inferred | v105 vs v120, v108 vs v124 only (S1 c03, c11) |
| 7 | Recorded crescendo rolls (Felt Cresc) for the printed roll crescendos into a stroke | p.123, p.125 | timpani pp < into the p stroke at 172 (bars 52-53), pp < to f at 203/ff 204 (bars 60-61), pp < into f at 262 (bar 78-79) | yes | 1 row | inferred (M1 #12) | never |
| 8 | Half-section divisi patches for the "4 soli" passages | p.89-90, p.222 | Cb 4 soli bars 65-70 (qn 220-238) and 87-92 (286-304); Vc 4 soli bars 83-86 (274-286) | yes (Basses Divisi, Celli Divisi DIV A/B) | about 0.7 GiB per instance, 0 with a separate pass | inferred; the full sections play at -3 dB now (`SOLI_AS_META`, c27) | never |
| 9 | Horn and trombone portato rows for tenutos | p.101 | the tutti tenutos of bars 61-62 (Hn1-4, Tbn2, BTbn, Tuba), Horns 1-2 bars 80-81 (qn 267, 269), Horn 3 con sord. bar 88 (qn 289), Tbn1 216 | yes | 1 row per track | inferred (M1 #9) | never |
| 10 | Round-robin reset on CC16 (the controller Opus is set to) instead of CC36 | p.34, p.143, p.145; 2025 p.92 | every track (repeatability) | n/a | 0 | read (M1 #6) | CC36 since S1 c24; **CC16 in the pre-roll since c45, kept; inside the music since c49 (Violas 152.06), kept** |
| 11 | Trombone 1's two accents (213, 218) on a filtered marcato attack (Marc Sus LITE at low velocity) | p.101, p.62-63 | Trombone 1 bars 63-64 | yes | 1 row | inferred (M1 #1); measured state S1 c26 | Sus Accent (harsh, S1 c24-c25); Sus MAX + swell since S1 c26 |
| 12 | Bass trombone's D2 on the Solo Trombone patch | p.100; 2025 p.63-64 | one note, qn 218 (bar 64) | yes (3TB) | 1 instance or a separate pass | measured (patch roots E2-C5) | never |
| 13 | Marcato Sustain rows (Sus Marc LITE, key 25, on the 2nd Violins / Violas KS Masters; Marc Sus LITE, key 73, on the Basses KS Master) for the bar 47 fp strokes | p.91-92 | Violins II, Violas, basses at qn 148 (fp, down-bow at the frog) | yes | 1 row per track (a state change: full rebuild of 3 tracks) | inferred (critic A c48; Movement I c47: removed a 64-124 ms swell-in on cello strokes) | c48: not tried (the lead allowed it only without an Opus state change). The CC11 step from the note-on + fresh Sus MAX strokes + a post-fader bump met the targets instead (own drops 12.8-14.1 dB, peaks +5..+115 ms; master tilt jump +3.3 dB) |

## 1. Brass and clarinet dynamics on CC1

- **Manual.** p.101: brass sustains: velocity and CC1 (the mod wheel) set the dynamic of the sustained sound, four layers. 2025 p.61-67 lists the same for every Hollywood Brass patch. The woodwind manual text for the clarinets agrees with the patch (below).
- **Read.** Movement I c09 read the KS Masters' layer groups: "1FH pp/mf/f/ff", "1Tb p/mp/f/ff", "Tu pp/mf/f/ff", "Cl p/mp/f" each carry a cc1 rescaler on their Source volume (`symphony/mvt1/reaper-v621/build/score_config.py`, c09 comment). With CC1 57-87 every printed dynamic played the mp-f samples.
- **Now (measured, c27 parts.json).** `CC1_DYN_TRACKS` is empty in this config: every horn, trombone, tuba, Horns 1-2 a2 and clarinet track gets CC1 53-87 from the vibrato rule (CC1 following the level), so the pp horn solo, the ff climaxes and the ppp coda clarinet all play the middle layers; CC11 only changes their volume. The bass clarinet (BC KS Master) uses CC11 and is right as it is. Movement I also holds the contrabassoon's CC1 at 40 (`CC1_HOLD`: its 57-87 sat in the CB KS Master's Non Vib fade).
- **Change.** In `build/score_config.py`: `CC1_DYN_TRACKS = ("Horn", "Trombone", "Bass trombone", "Tuba", "Clarinet ")` (the trailing space keeps the bass clarinet out) and `CC1_HOLD = {"Contrabassoon": 40}`; `CC1_DYN_MAP` stays the generic one (18-120). Every level table fitted on these tracks (pitch trims, note trims, roles, accent swells on Trombone 1, early fills on Horn 1 and Clarinet 1) was fitted on the middle layers and needs a check on the first render (M1 c09 took two cycles to settle).
- **How to measure.** Spectral centroid and 2-5 kHz share per printed dynamic on the horn and clarinet solos against c27; level per bar against the printed dynamics (the pp horn solo should get darker and softer, the ff tuttis brighter); attack probe.
- **Evidence.** Patch read in movement I; movement II's CC1 measured in parts.json; gain inferred (large: it is the timbre of every brass and clarinet note).

- **Tried (c30, 2026-11-06), kept.** Layer tables re-read in the .oib (1FH, 2FH, 1TB, 1TU, CL: every sustain/legato layer group on a cc 1 rescaler; CB: CC11 layers, CC1 Non Vib/Vib). `CC1_DYN_TRACKS = ("Horn", "Trombone", "Bass trombone", "Tuba", "Clarinet ")`, `CC1_HOLD = {"Contrabassoon": 40}`, generic map. Measured on the first render: horns pp -8..-11 dB, p -3.5..-6, f +1.5..+2.5, ff +0.5..+3; clarinets pp -3.6/-5.4, f +2/+3. 1-5 kHz share: Horn 1 pp -14.4 -> -24.2, p -15.0 -> -21.4, f -17.0 -> -14.6; Horns 3/4 pp about -8 dB; Trombone 2 pp -10.6; Clarinet 2 pp -12.7. Levels restored by per-track soft/dyn trims (stem fix) to within about ±1 dB per bucket. Details: `cycles/c30/CHANGES.md`, `cycles/c30/cc1_levels_by_dynamic.txt`.

## 2. Repeated notes and slurred tenuto repeats

- **Manual.** Strings repetitions and Legato Slur Staccato (p.96-98); brass Legato Repetitions and Legato Slur Repetitions (p.101, p.106); woodwind Legato Repetitions RRx4 and Legato Slur Repetitions (p.109-110, p.112).
- **Where (read, mockup-events.tsv).** Violins II bars 15-21: half-note/quarter pairs on one pitch under slurs with tenutos ("aes'2--( aes'4--)", 18 tenutos, upbows), a portato that must be heard as separate bow pressure inside one bow. Violas bars 48-51 (qn 152.5-167.5): 15 portato eighths, sotto voce, mostly repeated pitches (read as tenutos since c27). Wind/brass re-tongued repeats (parts.json `rep_retongued`): Oboe 1 and Bassoon 1 bar 47, cor anglais bar 50, Bass trombone bar 64, Clarinet 2, Bass clarinet, Bassoon 2, Contrabassoon, Horns 3-4 bar 80.
- **Now (read).** Slurred same-pitch repeats merge into one note with a CC11 notch (`SLUR_REP_MERGE_SUS`, `WIND_SLUR_REP_MERGE`, `MERGE_NOTCH_AT`); unslurred ones are re-tongued with a gap and a CC11 fall (`WIND_REP_RETONGUE`); slurred tenutos on winds re-tongue (`WIND_REP_PORTATO`, `PORTATO_TAIL_JOIN`).
- **Change.** First measure S1 on the c27 render at these places (dip at each repeat in 30 ms windows, aim 3-6 dB on the master). Where it fails, A/B the library rows on one passage per family: strings "Leg Slur Rep"/Repetition rows where the KS Master has them (dump the map with `dump_ks.py`), winds/brass "LegRep RRx4" (M1 #2 lists the patches that have them).
- **Evidence.** Rows read (M1); problem inferred for movement II.
- **Tried (c28, render pending).** Violas portato eighths bars 48-51 on the Violas KS Master Detache row (key 30) via `ART_SPANS`, same lead and length as c27's Leg Slur MAX notes; pass criterion: peak by +0.15 s on 12 of 15 notes, at least 6 dB drop in the rests, peaks 7-9 dB under the cor anglais (c27: peaks at +0.34..+0.52 s). Also on: `WIND_REP_PORTATO` (slurred tenuto repeats re-tongued) and Violins II re-bowed on the printed new slurs at 45/51.

- **Tried (c37, 2026-11-07), kept.** Flute 1's slurred pp repeat at 136 (the slur's last note) on "LegRep RRx4" (key 31) via ART_SPANS and the new `WIND_SLUR_REP_MERGE_SKIP` (no merge, 0.06 qn gap). Measured: a re-attack about 5 dB over the end of the 135 note (the merge notch had shown 0.2 dB). The row's body was 8-11 dB louder than Leg Slur MAX at the same CC11 and velocity, so a level shape cuts it to the old level. Leg Slur Rep (the scripted row, for a repeat inside a slur) is still untried.

## 3. Hollywood Solo Violin for the bars 17-22 solo

- **Manual.** p.75-81: the Solo Violin links dynamics and vibrato on CC1, has true legato (slur, bow change), expressive sustains; p.222 recommends separate passes for large setups.
- **Now (read).** "Violin I solo" plays qn 48-65 on `1st Violins KS Master DIV A` (half section, Close mic only; S1 c10), with `TRACK_WINDOWS`, roles [48,65,2], `HP_SOFT_GAIN_AT`, `JOIN_NOTCH` and entry/early-fill entries.
- **Change.** Dan installs Hollywood Solo Violin (licensed) from the Installation Center; then the solo track on its Legato patch with CC1 from the printed dynamic and legato velocity 50-70, Close + Mid, rendered in a second REAPER session (no memory in the main one). Until then, critics in the A3 slot can still improve the DIV A track (CC1, legato velocity, entry lead).
- **Installed.** No (checked: no Solo Violin folder under `/Volumes/MAC DRIVE/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/`).
- **Evidence.** Inferred.

## 4. Mid instead of Close mics on the woodwinds and horns

- **Manual.** p.138: Close mics capture presence; Mid mics give "definition without the sound of close proximity"; Main mics a unified sound. p.139: each mic loads or unloads its samples.
- **Now (read).** `build/mix.json` (series 1 c26): woodwinds Close + Main, horns Close + Main; depth by reverb send only.
- **Change.** One render with `"mics": {"Mid": x, "Main": y}` on Oboe 1, Flute 1, cor anglais, Clarinet 1, bass clarinet and Horn 1 (the exposed solos), gains re-matched to the same K-weighted level; full rebuild of those tracks; level tables fitted on them need a check.
- **How to measure.** Early-tail ratio of the solos against the strings at the same dynamic; 2-5 kHz presence; per-pitch R-L SD; attack probe.
- **Evidence.** Inferred.
- **c29 (2026-11-06), tried first instead of the swap:** critic C measured the wind notes' room 5.5 dB weaker at the cut-off and 7 dB weaker in the hall tail than the strings' (early drop 13.1 dB against 7.5); the wind group's hall send 0.35 -> 0.6 (and Violin I solo 0.5 -> 0.8), plus width 0.05 on the solo winds (movement I c25/c35). Result: see `cycles/c29/CHANGES.md`. The Mid swap stays open if the send does not close the gap.

## 5. Expressive rows for the espr./dolce wind solos

- **Manual.** p.109: Sus Expressive "adds an expressive feel to the notes with a slower attack and a gently increasing vibrato"; 2025 p.69-76 lists Sustain Expressive for most solo woodwinds ("Leg Slur Exp" in FL, FL2, OB, EH, BS, CB; Clarinet and Bass clarinet have only "Sus Exp").
- **Where.** The printed marks in the summary table; the longest are the cor anglais "solo, dolce cantabile" (bars 41-44, qn 124-140) and "solo, espr." (bars 47-50, qn 151-168), the bass clarinet solo (bars 31-36) and Clarinet 1's coda (bars 85-89).
- **Change.** `ART_SPANS` A/B on the cor anglais 124-140 with "Leg Slur Exp"; refit its entry and legato leads for the slower attack.
- **Evidence.** Inferred.

## 6. Slower legato transitions on the cantabile string lines

- **Manual.** p.144: true-legato velocity about 50-60 gives a longer transition, "allowing the melody to breathe more"; 110-127 a shorter one.
- **Read (M1 #8).** The string KS Masters' LegatoSpeed script maps velocity 30-127 to a sample start offset of 0-4800 samples; v124 starts about 4650 samples in, v60 about 1480.
- **Now.** Legato targets at v124 (`LEG_VEL_STRONG`), soft coda targets v90 (`CODA_SOFT`).
- **Change.** A per-span legato velocity of 60-75 on Vc bars 23-28 and Vln I/II bars 53-56, leads raised by the measured difference (about +0.07 s).
- **Evidence.** Inferred.

## 7. Recorded crescendo rolls for the crescendo rolls into strokes

- **Manual.** p.123, p.125: Felt Cresc rolls in three lengths end on a stroke; "the most realism" for a crescendo roll.
- **Where (parts.json).** Timpani 168 (pp <, 4 qn at 60 bpm, into the p stroke at 172), 200 (pp <, 3 qn, into the f stroke at 203 and the ff roll at 204), 261 (pp <, 1 qn, into the f roll at 262). Movement II has three of the score's few timpani gestures here, so the gain is larger than in movement I.
- **Change.** Read the take lengths from the `.ews` headers first; use a take where its length matches the printed roll at the local tempo (about 4 s at 168, 3 s at 200).
- **Evidence.** Inferred.

## 8. Half-section patches for the "4 soli" passages

- **Manual.** p.89-90: DIV A / DIV B are half sections, Close mics only.
- **Now (c27).** v600 prints "4 soli" on the basses (bars 65-70, 87-92) and celli (bars 83-86); `SOLI_AS_META` plays the full section 3 dB lower, as "metà".
- **Change.** A "Double basses soli" track on `Basses Sus MAX DIV A.oib`-family KS Master (check `Basses Divisi/05 Keyswitch/`) for 220-238 and 286-304 via `TRACK_WINDOWS`, or render it in a second session (memory: series 1 settled at 44 GB with 32 instances).
- **Evidence.** Inferred.
- **c33.** The celli 4 soli (274-286) moved to Violoncellos div (DIV A); 2.2 dB louder than the full section at -6 dB.
- **c35 (critic A #5), deferred.** `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` is installed (checked by A). A 33rd instance (about 0.7 GiB Close only) against 44 GB settled, plus a refit of every basses re-bow fill on 220-238 and 286-304 (`fit_rebows.py --window`), was more than this cycle could test alongside its timing changes; the basses' level there is already on target (critic B), so this is timbre only.

## 9. Horn and trombone portato rows for tenutos

- **Manual.** p.101: Portato: each note held its full length or nearly, non-legato.
- **Where.** The tutti tenutos of bars 61-62 (molto sostenuto), Horns 1-2 bars 80-81, Horn 3 bar 88 (con sord.), Trombone 1 qn 216.
- **Installed.** "Port Lng"/"Port Shrt" in 1FH (patch folder `Solo French Horn/01 Long`); "Portato" in 1TB, 1TU, 2FH (M1 #9).
- **Evidence.** Inferred.

## 10. Round-robin reset on CC16

- As M1 #6: Opus's `Preferences.json` has `"RoundRobinResetCC": 16`; the pipeline sends CC36 (a Repetition-script control). Schedule it in a cycle that refits per-note shapes, because the reset changes which take plays.
- **Tried (c45, 2026-11-08), kept.** `tools/build_reaper.py` `RR_RESET_CC = 16` sends CC16 = 127 at the pre-roll reset instead of CC36 (no patch maps CC16; ks_maps.json). Repeated notes still alternate takes (violas' portato A3s peak at +0.17 / +0.25 s in turn). Not yet measured: whether two renders of unchanged data now match (run state_check.py after the next render).
- **Measured (c46-c49).** With the pre-roll reset, unchanged notes rendered level-identical from c45 to c46 (0.0 dB). The pre-roll reset alone does not keep a whole render repeatable: in c48 the Violas' portato eighths at 152-168 came out with the two Detache takes swapped against c47 (peaks at -130 / +320 ms instead of +140 / +50 ms) on unchanged data, and c48's Double basses at 60-80, Violoncellos div 63 and Horn 1 198 also differed from c47 (found in c49 by state_check against c47).
- **Tried (c49, 2026-11-09), kept: a reset inside the music.** `tools/score_to_parts.py` `RR_RESET_AT = {"Violas": [152.06]}` writes a point to the track's `cc36` lane, which `tools/build_reaper.py` sends as CC16 = 127 (after the Detache keyswitch region starts, before the first eighth at 152.5). Two range renders were identical after the reset point (difference -246..-252 dB). In the full c49 render the 15 eighths have c47's take order again: peak times within 5 ms of c47, levels within -1.0..+0.7 dB, 40 ms envelope median difference 0.33 dB (c48 against c47: 1.82 dB). `tools/state_check.py` now prints a "take swap" line for this signature. Add a reset point before any repeated-note passage whose takes differ audibly, and place it after the row's keyswitch region starts.

## 11. Trombone 1's two accents

- As M1 #1, on two notes only (213, 218). The c26 state (Sus MAX, no CC11 bump, swell in seconds) answered Dan's note; change it only if a critic measures the accents as weak or late (series 1 c27 critic A #4 and C #4 found them late on c26).

## 12. Bass trombone's D2

- The Solo Trombone KS Master's sustain roots run E2-C5; the D2 at qn 218 plays an E2 sample two semitones down (as in series 1). Optional: 3TB KS Master in a second pass.

## Checked and not applicable to movement II

- Woodwind staccato rows (M1 #11): v600 prints no wind staccato.
- Timpani alternate hands (M1 #10): no same-pitch stroke runs in v600 (strokes at 172, 203, 209.5, 277, 278.5, 279).
- Brass accent samples in general (M1 #1): only Trombone 1 has accents in v600.
- Horn con sordino (Horn 3, coda): the Solo French Horn folder has only stopped-horn patches (`05 Mutes`: Stop Sus, Stop Sus Accent, Stop Stac), not a straight mute; series 1's `mute_eq` emulation stays (S1 c04).
- Glissando key maps (p.72-74): no harp glissandi in v600.

## Memory plan

- Series 1's 32-instance project settled at 44 GB and rendered at 44 GB (S1 c24-c26). The brief's cap is about 45 GB, so the main session has room for at most one more Close-only instance (0.7 GiB, M1 c35). Render added instances (Solo Violin, 4 soli divisi, 3TB) in a second REAPER session with the same tempo map, pre-roll, hall IR and send, and add their stems to the master before delivery (p.222).
- Rows: each added row costs about 0.1-0.3 GB per track (inferred, M1). Mics: swap rather than add.

- **c31 (2026-11-07), revised for the horns.** The 1FH/2FH legato transition table (TLeg, cc 1: 0.9 at CC1 30-46, 0.44 at 70) makes soft legato targets at CC1 28-54 collapse 6-13 dB after the transition. The horns now take c29's soft CC1 (57-72, `CC1_DYN_MAP_BY`) and keep the CC1 dynamics from f up. The trombones, tuba and clarinets keep the full CC1 map (no head-body effect measured). Horn 1 bodies came back to c29 within 0.5 dB.

- 2026-11-07 (c41): no gap tried (release caps and stereo width this cycle).

**c44 (2026-11-08), #4 superseded:** the EastWest template layout replaced the mic question (woodwinds Close-led with Main under it, strings and brass Close 4-10 dB under a full-width Main). Mid was not tried; it stays the fallback if critics find the Close-led woodwinds too present.

- 2026-11-09 (c48): no gap tried. #13 (strings Marcato Sustain for the bar 47 fp) added and left for a cycle that may change Opus states: the fp met its drop and timing targets on Sus MAX with FP_SPIKE_AT_MARK, fresh strokes and a 0.22 s post-fader bump; the Marcato row would replace the bump if the master tilt jump (+3.3 dB) or the strokes' 0.37-0.44 s fall to p need it.

- c52: no MANUAL-GAPS item tried. Related to the template plan's line on keyswitch timing (EW keyswitches 40-800 ms ahead): a 0.15 s keyswitch lead on row-change legato targets is now in use on the strings (KS_ROWCHANGE_LEAD_S; cycles/c52/CHANGES.md).

## Tried in cycle 53 (item 8 / manual p.89-90: non-divisi mics for a divisi track)
Violas div on the section's `Violas KS Master` (Close 0.5 + Main 1.0) instead of `Violas KS Master DIV B` (Close only), range render of bars 20-30, second pass after the rebuild: stem correlation 1.00 -> 0.51, side/mid -126.5 -> -4.9 dB (the section track: 0.26, -2.3). Level +4.7 dB median; note bodies between +1.1 and +12.3 dB against DIV B (6 of 11 within 1 dB after one trim); legato joins by S +138 / +28 / +1 / +34 -> +29 / +35 / +19 / +66 ms. Not kept (levels not within 1 dB after a trim); it needs a per-note level fit and new re-bow fills first. Layering the section's Main mic under the DIV patch (the manual's own method) would need a second instance. `cycles/c53/divtest.txt`, `cycles/c53/divtest/`.

- c54: no item tried. Item 2 ("Leg Slur Rep", manual p.112) is the named next step for Clarinet 1's slurred tenuto repeat at qn 289: a shorter gap (keyswitch 0.02 qn before the note, `KS_LEAD_AT`) left the stem dip at 9-10 dB, a fitted post-FX fill brought it to 3.3 dB (master 5.6 dB, 4 wanted); cycles/c54/CHANGES.md section 3.

## Tried in cycle 55 (velocity in place of fader moves on plucked and struck notes; KIT lines 59-61, 195-197)
- Violas Pizz RRx4, bars 41-44: per-pitch velocity offsets (+16 / +12 / -10 / -4) in place of the pitch trims: spread of the pitch means 6.10 -> 4.09 dB (trims: 3.86). Adopted. Sensitivity about 0.15 dB per step upward; a layer boundary near velocity 40 downward.
- Timpani Flt Lng strokes: velocity in place of the +6 / +7 dB attack lifts: within 1 dB of the c54 peaks at three strokes on a range pass. Adopted.
- Not tried: CC11 lift in place of early fills, CC1 brass shape, "Leg Slur Rep" row for Clarinet 1 289.
