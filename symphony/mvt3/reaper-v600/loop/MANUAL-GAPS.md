# Manual gaps for the Finale mockup

Started 2026-11-07 (mvt3 c00) as a copy of Movement I series 2's list (symphony/mvt1/reaper-v621/loop/MANUAL-GAPS.md, as of its c42), which ranks what the Hollywood Orchestra manuals offer and records what was tried and measured on Movement I. Bar and qn references below the line are Movement I's (v621) unless a Finale entry says otherwise: check each gap against the Finale's score before acting on it, and add Finale-specific gaps and results here (a "Finale" note under the item, or a new item). Already relevant to the Finale from the port: #13 (the bass trombone's low notes: v600 has a B flat 1 below the 1TB KS Master's lowest sample key, 36), #6 (round-robin reset on CC16), #2 (repetition rows: the Finale's hammered eighths and brass repeats), #12 (recorded crescendo rolls: the Finale has many timpani crescendo rolls), #1 (brass accents), and the Finale's own percussion (crash cymbal pairs p.116-117, bass drum p.121-122: not in Movement I's list).

---

# Manual gaps: what the Hollywood Orchestra manuals offer that the v621 mockup does not use

Written 2026-11-06 (after c34; c35 was rendering). Sources: the May 2021 HO Opus manual (`guides/eastwest-hollywood-orchestra/text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt`, cited as `p.N`, PDF pages), the Dec 2025 library manual (`2025 p.N`), the Oct 2025 Opus manual (`Opus p.N`), the installed `.oib` patch files, Opus's `Preferences.json`, `build/score_config.py`, `build/parts.json`, `build/mix.json`, `build/mockup-events.tsv`, `tools/score_to_parts.py`, `tools/build_reaper.py`, `loop/HISTORY.md`, `loop/LEARNINGS.md` (cited `M1 cNN`), `mockup-kit/LEARNINGS.md` (cited `KIT §n`) and the c35 critic reports. The library digest is `guides/eastwest-hollywood-orchestra/DIGEST.md`.

Evidence labels: **measured** (a number from a render, from parts.json or from a patch file), **read** (read in the code, a patch file or a preference file), **inferred** (reasoned from the manual or from other measurements; not tested). Bar b starts at qn 4(b-1).

Ranking: expected audible gain for Dan's priorities (articulations; each track's level and the blend; timpani rolls under the texture). Items 6 and 12-13 are lower because their gain is indirect or local.

## Summary

| # | Gap | Manual | Where in v621 | Installed | Memory | Evidence | Tried before |
|---|---|---|---|---|---|---|---|
| 1 | Brass accents: a filtered marcato attack (Marc Sus LITE at low velocity) instead of a plain sustain plus a volume swell | p.101, p.62-63 | 200 marked brass accents (162 measured in c35); bars 23-26, 32-33, 41, 69-72, 80-83, 131-138, 142-143, 167-170 | yes | 1 row per track | problem measured, row read, gain inferred | Sus Accent at high velocity (harsh); CC1 front lift (failed); Marc Sus LITE never on brass |
| 2 | Repeated wind/brass notes on the sampled re-tongue rows (LegRep RRx4, Leg Slur Rep) | p.101, p.106, p.109-110, p.112 | about 340 re-tongued repeats (Cbn bars 27-32, 131-138; Horns 3-4 bars 20-22, 69-72, 118-126, 131-142; Bn2 bar 82); motif repeats into tenutos (bars 27, 127, 160) | yes | 1 row per track | measured (c37-c38) | c37 A/B on 4 tracks; c38 with the re-tongue gap and fall on 5 tracks: kept (Results c38); c41 Horn 1, Trumpet 2 (Results c41) |
| 3 | Hollywood Solo Cello for the coda "Solo espr." | p.82-88, p.222 | Vc qn 680-696, bars 171-174 | **no** (licensed) | 0 with a separate pass | problem measured, gain inferred | DIV A section solo removed for memory (c35) |
| 4 | Mid instead of Close mics on the woodwinds (then horns, trumpets) | p.138-139, p.222 | every wind solo; blend everywhere | yes | about neutral (a swap) | inferred | never |
| 5 | Expressive rows (Leg Slur Exp, Sus Exp) for espr./dolce wind solos | p.109; 2025 p.69-76 | 12 marked solos, bars 5-8 ... 175 | yes | 1 row per track | inferred | never |
| 6 | Round-robin reset on CC16 (the controller Opus is set to) instead of CC36 | p.34, p.143, p.145; 2025 p.92; Opus p.29-30 | every track (repeatability), celli stroke runs | n/a | 0 | read; symptom measured | CC36 since mvt II c24; CC16 never |
| 7 | Half-section divisi patches for soft div. passages | p.89-90, p.222 | Vla bars 47-68; Vln II bars 107-117, 147-155; Vln I/II bars 167-177 | yes | ~0.7 GiB per instance, 0 with a separate pass | inferred | deferred c01 (memory); worked in mvt II |
| 8 | Slower legato transitions (target velocity 60-75) on cantabile string lines | p.144, p.99 | Vc dolce bars 46-54; Vln I/II molto cantabile bars 56-61; coda bars 171-178 | yes | 0 | script read, gain inferred | v105/v108 vs v120/v124 only; v70 on the DIV A solo (c40); LegatoSpeed START_MAX / RELEASE on Vla / Vc: a lead shift, no shorter slide (Results c41); the slide premise was an estimator artefact, transitions 82-98 ms in all sections (Results c42) |
| 9 | Horn portato rows for tenutos | p.101 | Horn 1 bars 48, 51, 148, 151 and 19 more brass tenutos | yes | 1 row per track | inferred | never |
| 10 | Timpani: alternate left- and right-hand samples on repeated strokes | p.123-124 | 20 repeated strokes, bars 27, 30, 32, 82, 131-134 | yes | 0 | read; gain inferred | done c37 (Results c37) |
| 11 | Woodwind staccato rows for printed staccatos | p.110 | 36 notes: Fl1 bars 30, 94-96; Bn1 88-90; CA 91-93; Ob1, Cl1 bar 30 | yes | 1 row per track | inferred | Bn1 test c03, judged on speed only, reverted |
| 12 | Recorded crescendo rolls (Felt Cresc) for printed roll crescendos into a stroke | p.123, p.125 | timpani crescendo hairpins (13) | yes | 1 row | inferred | never |
| 13 | Bass trombone's three lowest notes are transposed tenor-trombone samples | p.100; 2025 p.63-64 | qn 451.78, 455.89, 459.89 (bars 113-115) | yes (3TB) | 1 instance or a separate pass | measured (patch) | never |

## Finale results (c01)
- #11 (staccato rows), extended to brass, c01: Horns 3/4 "StacSs RRx9" (qn 40-104) -10 dB length 0.15 s, "Marc Shrt RRx4" (600-664) 0.31 s; Bassoon 1 "Stac DblTng RRx9" 0.24 s; Trumpets 1-3 "Stac DblTng RRx9" 0.29 s (Sus slices were 0.36-0.44 s). Levels 3.6-8.6 dB under the Sus notes at the printed-level velocities (stem fix +2.5..+5 dB). Kept; c02: Marc Shrt for the horns' F1 span too.
- Manual p.92 (sul tasto as Sustain with no vibrato), c01: TASTO_CC1 0 on Vla/Vc/Cb; the viola line fell 7.6 dB (stem fix +4).

## 1. Brass accents: a filtered marcato attack instead of a plain sustain plus a volume swell

- **Manual.** p.101: Sustain Accent: velocity = loudness of the attack, CC1 = loudness of the sustained note. Sustain Marcato Long/Short (KS row "Marc Sus LITE"): a marcato attack "not as forceful an attack as in the Sustain Accent patch"; velocity sets the cutoff of a low-pass filter on the marcato samples, so a soft velocity gives a darker attack. p.102: brass shorts at the highest velocities add an overblown attack (avoid the top velocities). p.106: Legato Slur Accent: velocity = accent strength. p.62-63: LITE rows have about half the dynamic layers of MAX.
- **Where.** Brass accents in v621 (mockup-events.tsv, 200 marks): Horn 1 24, Horn 2 24, Horn 3 22, Horn 4 20, Trumpets 17/16/10, Trombones 21/20, Bass trombone 13, Tuba 13. Most are in bars 23-26, 32-33, 41, 69-72, 80-83, 131-138, 142-143 and 167-170.
- **Now (read).** `tools/score_to_parts.py`, wind/brass articulation branch: an accent at f-4 or louder plays `GENTLE_ACCENT["brass"]["arts"]` (Sus MAX / Sus Non Vib MAX), no velocity add, no CC11 bump, and a volume swell (`build/score_config.py`: brass `db` 2.5, `swell_s` (0.03, 0.15, 0.40), `swell_s_leg`, `keep_legato` True), fitted per accent in `build/accent_fits.json` by `tools/fit_accents.py`.
- **Measured state.** Brass 2-5 kHz in the first 80 ms minus the body: median -9.1 dB, p90 -1.2, over 162 accents (c35 critic B). In c12 the stems' median was -14.5 dB against -4.2 dB measured on a real orchestra (comment in `build/score_config.py`, c12 block). The accents carry weight by level only; their attack has no more edge than an unaccented note.
- **Tried.** Sus Accent MAX at v105-110 with an 8 CC11 bump into the fff layer: a 2-5 kHz burst 7-13 dB over the body, heard as harsh by Dan (mvt II c24-c26; KIT "What a listener noticed"). A CC1 lift on the front of brass accents: +1..+2 dB only, because the CC1 layer fade is 120 ms (M1 c12; reverted c13). Strings "Sus Marc LITE" (c23): front minus body -1.9 -> +2.4 dB but 2-8 dB louder and 2-5 kHz +4.2/+6.7 dB on two Violins I notes; kept on 14 strokes. Marc Sus LITE on brass and Sus Accent MAX at low velocity without a CC11 bump: never.
- **Change.** A/B in one render with `ART_SPANS` in `build/score_config.py` on two passages: Trombones 1-2, Bass trombone and Horns 1-4 in bars 32-33 (qn 124-132) and 142-143 (qn 564-572), art "Marc Sus LITE", velocity from the printed dynamic in the 40-75 range (filter mostly closed), CC1 from `CC1_DYN_MAP`, no CC11 bump, the swell cut to about +1 dB (the sample now gives the front). Every other brass accent keeps GENTLE_ACCENT. If the fronts land in range, extend family by family and refit `accent_fits.json`. A second option for accents inside slurs: "Leg Slur Accent MAX" at low velocity instead of the swell on Leg Slur MAX.
- **Installed.** Yes: "Marc Sus LITE" is an unloaded row in 1FH, 2FH, 1TP, 1TB and 1TU KS Masters; "Leg Slur Accent MAX" in all five (patch). `build_reaper.py load_articulations()` loads a row when parts.json uses it.
- **Memory.** One more row on each test track: about 0.1-0.3 GB per track and row (inferred: c24 freed 18 GB by unloading 3-4 default rows on each of 32 tracks; c14: three one-note legato rows cost 0.12 GB). Test on the 6-7 tracks above first and read `footprint` after the settle.
- **How to measure.** Per accent: 2-5 kHz first 80 ms minus body (target -6..-2 dB; never over +3 dB) and the master's 2-5 kHz jump at the attack (under +3 dB); level over same-dynamic neighbours 2-4 dB (`fit_accents.py`); attack-peak time against Sus MAX (attack probe); for the LITE row, level steps across CC1 (fewer layers).
- **Evidence.** Problem measured; rows read in the patches; the gain and the safe velocity range are inferred.
- **c24 (strings, Marcato Sustain p.91-92, the string half of this gap).** "Sus Marc LITE" (key 25) on the accented ff chords (qn 0, 4, 16, 20, 372, 584, 1104), lead 0.085 s, no CC11 accent bump, +4 dB region gain on the row's sustain groups (not the "Marc Shrt" group). Range test: 1st Violins peak +475 -> +225 ms at qn 16; marcato velocity 92 (middle layer 66-108) put the 2-5 kHz front at body level (-0.4 / 0.0 dB), the top layer (v111) +3.1 to +6.7 dB over it. 2nd Violins, Violas, Celli: the held chords started 13-25 dB under their peak and peaked +375-575 ms (no gain): adopted on Violins I only. Full render: master peak at qn 4 / 16 / 20 / 584 / 1104 +275 / +375 / +275 / +425 / +375 -> +175 / +225 / +175 / +325 / +275 ms (target about 150). Brass "Marc Sus LITE" still untried.

- **Finale c29 (not tried).** "Leg Slur Accent MAX" was again not range-tested (four brass tracks would need a full rebuild in the last cycle that can change the render). Instead the notes after the accented Sus-row head went to the sustain row with 0.10 s crossfades: Horn 3 at 146 / 578 join dips 3.1-5.5 -> -3.8..+0.3 dB (range VAR against CTRL and the full render), Horn 1 at 74 4.4 -> 2.4, but Horn 1 at 818 3.7 -> 4.4 with a front 5 dB brighter (rejected there). The Leg Slur Accent test stays open.

## 2. Repeated wind and brass notes on the sampled re-tongue rows

- **Manual.** Brass Legato Repetitions: re-tongued repetitions for repeated notes inside a legato phrase (p.101). Brass Legato Slur Repetitions: same-pitch notes played without space use a re-tongued sample (p.106). Woodwind Legato Repetitions (LegRep RRx4): each note plays a non-vibrato sustain plus a short re-tongued attack with 4 round robins (p.109-110). Woodwind Legato Slur Repetitions (p.112).
- **Where (measured, parts.json `rep_retongued`, 341 notes in all).** Contrabassoon 41 (bars 27-32, 131-138), Horn 4 36 and Horn 3 28 (bars 20-22, 28, 31-32, 59-72, 98-101, 115-126, 131-142, 157-170), Bassoon 2 26 (7 in bar 82), Trumpet 2 19, Bassoon 1 18, Horns 1-2 16 each, Clarinets 1-2 15 each, Trombones 13-14, Trumpets 1/3 13, Oboe 2 13, Bass trombone 10, Oboe 1 9, Bass clarinet 8, Flutes 4/6, Tuba 5. Also the slurred motif repeats into tenutos (`WIND_REP_PORTATO`, 28 notes; e.g. Clarinet 1 at qn 107.5, 507.5, 639.5 = bars 27, 127, 160).
- **Now (read).** `tools/score_to_parts.py` `WIND_REP_RETONGUE` (+ `_BY`, `_SHORT`; config: Horn gap 0.10-0.14 s, fall_cc 12-14), `WIND_REP_PORTATO`, `PORTATO_TAIL_JOIN`, `WIND_SLUR_REP_MERGE`: the previous note ends early with a CC11 fall, then a fresh note on the Sus row; slurred repeats merge into one note with a CC11 notch.
- **Measured state.** c34 open list: 11 of 20 motif eighths more than 2 dB from their tenutos; c07: Horn 4 repeats 2.8 dB, other horns 4.3-5.1 dB after the fall changes; c34: the horn gap dips needed stem-fix lifts.
- **Tried.** The emulation rules only (mvt II, M1 c06-c34). The LegRep and Leg Slur Rep rows: never.
- **Change.** A/B spans with a new generic option in `score_to_parts.py` beside `WIND_REP_RETONGUE`, e.g. `REP_ROW = {track: [(a, b, row)]}`: (a) Contrabassoon bars 27-32 and Horns 3-4 bars 118-126 on "LegRep RRx4", each repeat its own note ending at the next onset, CC11 at the printed level, no early end and no CC11 fall; (b) Clarinet 1 / Oboe 2 motif repeats (bars 27, 127, 160) on "Leg Slur Rep", same-pitch notes overlapping so the script picks the re-tongue sample.
- **Installed.** Yes. LegRep RRx4: FL, FL2, OB, EH, CL, BC, BS, CB, 1FH, 2FH, 1TP, 1TB, 1TU. Leg Slur Rep: FL, FL2, OB, CL, CB, 1FH, 2FH, 1TP, 1TU (not EH, BC, BS, 1TB) (patch; all unloaded by default).
- **Memory.** One row per test track, about 0.1-0.3 GB each (inferred as in item 1); LegRep has 4 round-robin attacks per note, so expect the high end.
- **How to measure.** Per repeat: the dip at the re-tongue (30 ms windows, the c34 method; aim 3-6 dB) and each repeat's level against the first (within ±1.5 dB); motif eighth minus tenuto (within 2 dB); 2-5 kHz in the first 80 ms of each re-tongue; the loop check on repeated long notes.
- **Evidence.** Rows read; problem measured; gain inferred.

## 3. Hollywood Solo Cello for the coda "Solo espr." (qn 680-696, bars 171-174)

- **Manual.** p.82: Solo Cello links dynamics and vibrato depth on CC1 (the orchestral strings keep them apart); its new "Legato Sus Slur" combines legato and sustain in one sample layer. p.86-88: Legato Slur, Legato Bow Change Smooth (soft non-slurred attack), LegSus Slur (CC1 picks the dynamic layer at the note start, no crossfade; CC11 and CC1 change loudness during the note); legato up to an octave; velocity sets transition timing. p.83-84: Lyrical Vibrato and Sustain Expressive (molto vibrato) patches. p.82: vintage alternatives for the Close and Mid mics. p.222: rendering a part on its own pass "requires a smaller computer system".
- **Now (read).** The Violoncellos section (Celli KS Master) plays the 12 solo notes; `HP_TARGET_AT["Vc"]`, `PORT_TARGETS {"Violoncellos": {685.0: 100}}`, `LEVEL_SHAPES` rows at 687-694 in `build/score_config.py`.
- **Measured state.** c35 critic A #1: the celli stem is within 0-1.5 dB of the master over 681-695 and has an L/R correlation of 0.70 (cor anglais 0.85), i.e. a section's width; the tutti G2 at 696 starts 0.05 qn after the solo with no lead (-61 dB at +0.3 s). c35 memory test: a 34-track project (solo on Celli KS Master DIV A, Close only) settled at 46.55 GiB; the solo instance held 0.68-0.75 GiB (`cycles/c35/memory_test.txt`).
- **Tried.** c32 A #6 rejected (memory); c34 A #1 deferred; c35 DIV A track built, measured and removed (memory).
- **Change.** Dan installs Hollywood Solo Cello (licensed) from the Installation Center. Then a "Cello solo" track as in c35 (`TRACK_WINDOWS` with Violoncellos excluded over 679.5-696) on the Solo Cello KS Master: "Legato Slur" (crossfades into a light/lyrical vibrato sustain) or "LegSus Slur"; CC1 from the printed dynamic (add the track to `CC1_DYN_TRACKS`; for LegSus Slur set CC1 before each note because it is read at the note start); CC11 for the hairpins; legato velocity 50-70 for slower, singing transitions (p.86-87, p.144) with leads refitted; Close + Mid. Render it in a second REAPER session holding only this track (same tempo map, pre-roll, hall IR and send), then add the stem to the master before `deliver_master.py`.
- **Installed.** No (Hollywood Solo Cello and Solo Violin are licensed, not on the drive).
- **Memory.** 0 in the main session with the separate pass. Inside the main session at least 0.7 GiB (c35's Close-only DIV A instance; a solo legato patch with two mics likely more, inferred).
- **How to measure.** Solo-note levels against the cor anglais in 200 ms windows (c35 A: celli -30..-34 dB, CA -34..-44 now); L/R correlation of the solo stem (aim near the CA's 0.85); join dips and crossover times; vibrato rate and depth from a pitch track; the 696 tutti entry (level at +0.3 s; with the solo on its own track the section gets an ordinary entry lead).
- **Evidence.** Problem measured; not installed (checked with `ls`); gain inferred.

## 4. Mid instead of Close mics on the woodwinds (then horns and trumpets)

- **Manual.** p.138: Close mics capture presence; Mid mics sit at the edge of the stage and give "definition without the sound of close proximity"; Main mics in about the fifth row give "a big, unified sound". p.139: each mic loads or unloads its samples. p.222: a single mic position (usually Main) for the whole piece is possible.
- **Now (read).** `build/mix.json` groups: wind Close 0.5 / Main 0.8, horn 0.5 / 1.0, trumpet 0.5 / 1.0; strings and trombones at the factory mix (strings Close 0.66 / Main 1.0); `tools/build_reaper.py apply_mix()` loads only the listed mics. The factory woodwind Main sits 11-40 dB under Close, and "woodwinds then sound nearer than the strings" (KIT §12); depth is set only by reverb send (wind 0.35, flutes/oboes 0.5).
- **Tried.** Never. Surround was not considered because of memory (c35 critic C); Mid is not mentioned anywhere in the records.
- **Change.** For one render set `"mics": {"Mid": x, "Main": y}` on Flute 1, Oboe 1, Clarinet 1 and Cor anglais (the exposed solos), with gains re-matched to the same K-weighted level; if it helps, the whole wind group, then horns and trumpets. These tracks need a full rebuild (state change), and level-only tables fitted on them (soft_trim_db, accent fits) need a check.
- **Installed.** Yes (every KS Master has an unloaded Mid column; patch).
- **Memory.** A swap loads Mid and unloads Close: about neutral (inferred; read `footprint` after the settle).
- **How to measure.** Early-tail ratio (body minus the level 0.15-0.25 s after each note end; KIT c09 method) for the winds against the strings at the same dynamic; the solos' 2-5 kHz presence relative to the strings; per-pitch R-L SD (c35 critic C #1 method); attack timing (attack probe).
- **Evidence.** Inferred.

## 5. Expressive rows for the espr./dolce wind solos

- **Manual.** p.109: Sus Expressive "adds an expressive feel to the notes with a slower attack and a gently increasing vibrato". 2025 p.69-76 lists Sustain Expressive for most solo woodwinds.
- **Where.** Cor anglais espr. bars 5-8 (qn 19-31); Bassoon 1 espr. bar 33 (128.5); Clarinet 1 dolce bars 45-46 (176-184) and espr. bars 56-61 (220-244); Flute 1 espr. bars 73-76 (291-304); Bass clarinet "Solo espr." bars 77 (304.5) and 107 (424.5); Flute 1 "1. espr." bar 109 (432); Oboe 1 dolce bar 145 (578); Cor anglais dolce bar 147 (586.5) and espr. bars 171-174 (683-695); Clarinet 1 espr. bar 175 (699).
- **Now (read).** Leg Slur MAX / Sus MAX (Clarinets: Leg Slur / Sus Non Vib); CC1 written by score_to_parts.py crossfades the Non Vib and Vib layers (KIT §3); espr. level boosts (`SOFT_BOOST`, `SOLO_NO_BOOST`).
- **Tried.** Never.
- **Change.** `ART_SPANS` A/B on Flute 1 qn 432-440 and Cor anglais 683-695 with "Leg Slur Exp" (present in FL, FL2, OB, EH, BS, CB); "Sus Exp" / "Sus Exp Vib" for held unslurred notes (Clarinet and Bass clarinet have only Sus Exp). Refit the entry and legato leads for the slower attack.
- **Installed.** Yes (rows unloaded; patch). **Memory.** One row per test track (inferred 0.1-0.3 GB).
- **How to measure.** Vibrato onset (pitch-modulation depth over the first second of each held note), attack rise time (to -6 dB of the body), join dips, level against the accompaniment in 200 ms windows (c35 critic B #4 method).
- **Evidence.** Inferred.

## 6. Round-robin reset on CC16 instead of CC36

- **Manual.** p.34 (Preferences > MIDI > Round Robin: Reset Controller / Reset Note), p.143 and p.145 (CC36 listed as Round Robin Reset). 2025 p.92 and Opus p.29-30: the reset is sent on the CC entered as the Reset Controller in Preferences. The 2025 manuals win.
- **Read.** `/Library/Application Support/East West/Opus/Preferences.json` has `"RoundRobinResetCC": 16`. In every installed KS Master CC36 is mapped as "Repetition: Reset RR", a control of the Repetition script (patch).
- **Now (read).** `tools/build_reaper.py` `RR_RESET_QN` sends CC36 = 127 in the pre-roll (and CC69 = 0 on the strings); `tools/score_to_parts.py` `MEAS_TREM["rr_runs"]` writes a `cc36` lane at measured-tremolo run starts.
- **Measured symptoms.** CC36 inside the music did not reset the Celli Stac RRx9 cycle (M1 c14); two renders of identical data differed by 4-9 dB on some viola notes (M1 c26); winds differed in 12-20% of 50 ms frames between renders (KIT §3).
- **Tried.** CC36 since mvt II c24; CC16 never.
- **Change.** Send CC16 = 127 wherever CC36 is sent now (pre-roll and run starts); keep CC36 for the Repetition script. One constant in `build_reaper.py` and the lane in `score_to_parts.py`.
- **Caveat.** The reset changes which take plays on many notes, so per-note fits (rebow_fills, accent_fits, loop_fills, single-note LEVEL_SHAPES) can move by a few dB once (as after the v621 port, M1 c32-c33). Schedule it in a cycle that refits.
- **Memory.** 0.
- **How to measure.** Compare unchanged tracks between two consecutive renders: share of identical 50 ms frames per stem; the Celli measured-tremolo strokes' lag-9 autocorrelation with a reset at each run start (c14: 0.73/0.85/0.92 without an effective reset).
- **Evidence.** Read (preference file, patches); effect inferred, consistent with the c14 measurement.

## 7. Half-section divisi patches for soft div. passages

- **Manual.** p.89-90: DIV A / DIV B are the left or right chair of every stand, Close mics only; "the loudness of a divisi part is not much less than if the whole section were playing the part". p.222: separate passes.
- **Where (mockup-events.tsv).** Violas div. bars 47-60 (qn 184-236.5) and 62-68 (245-272); Violins II div. bars 107-117 (424-464) and div. sul tasto bars 147-155 (584-619, tremolo); Violins I and II div. bars 167-177 (664-707); Violoncellos div. bars 124-126 (492-504).
- **Now (read).** Chords on the section KS Master with a level cut of -10·log10(k) dB under "div." (KIT §8; `div_entries` in parts.json), `META_DB` for "metà".
- **Tried.** mvt1 c01 deferred (A5, memory). In mvt II, DIV A/B tracks worked (KIT §8: a DIV A solo track fixed a 6-7 dB hand-over hole).
- **Change.** For the longest soft passage, Violas bars 47-60, route the upper voice to a Violas DIV A track and the lower to DIV B (`TRACK_SPLITS` / `TRACK_WINDOWS`, as Horns a2), Close only, send 0.5, rendered in the second-pass session of item 3.
- **Installed.** Yes. **Memory.** About 0.7 GiB per Close-only DIV instance (c35 measured 0.68-0.75); 0 in the main session if rendered separately.
- **How to measure.** Level per chord note against the c34 section render; spectral centroid and 2-5 kHz share (half sections are thinner); join dips; loop pulsing (DIV patches loop too).
- **Evidence.** Inferred.

## 8. Slower legato transitions on the cantabile string lines

- **Manual.** p.144: with true legato, velocity about 50-60 gives a longer transition, "allowing the melody to breathe more", and 110-127 a shorter one; velocity then does not change loudness. p.99: slur vs portamento vs bow change.
- **Read.** The string KS Masters' LegatoSpeed script maps velocity 30-127 to a sample start offset of 0-4800 samples (patch). v124 starts about 4650 samples into the transition and v60 about 1480, so a v60 target plays about 65-70 ms more of the recorded slide (inferred arithmetic).
- **Where.** Violoncellos dolce tune bars 46-54 (qn 182-216); Violins I/II "molto cantabile" bars 56-61 (220-244); Violas espr. bars 19 (qn 72) and 107 (424); coda, Più lento, bars 171-178.
- **Now (read).** Legato targets at v124 (`LEG_VEL_STRONG`; parts.json: 240 Violins I and 270 Violoncellos notes at v124); timing set by leads (0.17-0.20 s) and per-pair tables.
- **Tried.** v105 against v120 (25-80 ms faster, c03); v108 against v124 on Violins I (identical crossovers, c11). These were 15-16 velocity steps, about 15 ms of offset. 50-75 never.
- **Change.** A per-span legato velocity (e.g. `LEG_VEL_SPANS = {track: [(a, b, vel)]}`) of 60-75 in those spans, with leads raised by the measured difference (about +0.07 s, to fit).
- **Installed.** Yes. **Memory.** 0.
- **How to measure.** Crossover time and transition length (pitch track between notes); join dips (c35 critic A #5: cello master holes 189 5.1 dB, 182 4.7, 201 5.0); arrival time of the new pitch.
- **Evidence.** Script parameters read; gain inferred.

## 9. Horn portato rows for tenutos

- **Manual.** p.101: Portato: each note held its full length or nearly, without being tied: non-legato, but not staccato.
- **Where (mockup-events.tsv).** Horn 1 tenutos bars 48, 51, 79, 104, 148, 151, 158, 160, 168; Horn 2 bars 59, 79, 158, 160, 168; Horns 3-4 bar 161; Trumpet 1 bars 70, 158, 160, 168; Trumpet 2 bar 168; Trombones 1-2 bar 132.
- **Now (read).** Slurred tenutos join on Leg Slur MAX with a CC11 notch (`PORTATO_JOIN_AT`: Horn 1 qn 189, 201, 589, 601; `PORTATO_JOIN_NOTCH`) or re-tongue on Sus MAX (`PORTATO_TAIL_JOIN`, `WIND_REP_PORTATO`).
- **Measured state.** On Sus MAX a re-tongued horn tenuto rose 8-9 dB over the Leg Slur note before it (M1 c04); joins across 8-9 semitones dip 7-12 dB (M1 c04, c06).
- **Tried.** Never with a portato row.
- **Change.** `ART_SPANS` A/B with "Port Lng" (1FH) on Horn 1's tenutos in bars 48-51 and 148-151; "Portato" exists in 1TB, 1TU, 2FH; Solo Trumpet has no portato row (patch).
- **Installed.** Yes. **Memory.** One row per track (inferred 0.1-0.3 GB).
- **How to measure.** Each tenuto's level against the note before; the dip at each change (30 ms windows); 2-5 kHz first 80 ms.
- **Evidence.** Inferred.

## 10. Timpani: alternate left- and right-hand samples on repeated strokes

- **Manual.** p.123-124 (and the KS description p.124-125): long hits have left-hand variations on MIDI 36-57 (C1-A2 in EW names) and right-hand variations on MIDI 60-81 (C3-A4), round robin x2 each; notes within 65 ms of each other play a damped double hit.
- **Read.** Timpani Flt KS has "RH Lng" regions at MIDI 60-81 (patch). `tools/score_to_parts.py` (timp branch) sends every stroke at its written pitch (MIDI 43-51), i.e. the left-hand samples only.
- **Where (measured, parts.json).** 63 strokes on the Lng row; 20 same-pitch strokes come within 0.6 s of the previous one, in bars 27, 30, 32, 82 and 131-134. No two strokes lie within 65 ms.
- **Now.** `TIMP_METRIC_VEL` / `METRIC_TIMP_DB` level steps; metric velocity alone failed because the round robins vary more than the step (M1 c07).
- **Tried.** Never.
- **Change.** In the timpani note output, send alternate strokes of a same-pitch run at pitch + 24 (right hand), starting each run on the left hand. Trim the right hand if its takes sit at a different level.
- **Installed.** Yes. **Memory.** 0 (same row; its regions are already loaded, inferred).
- **How to measure.** Per run: peak spread and spectral-centroid spread of consecutive strokes; the correlation of consecutive stroke spectra (identical takes read near 1); right- against left-hand level.
- **Evidence.** Patch read; gain inferred.

## 11. Woodwind staccato rows for printed staccatos

- **Manual.** p.110: staccato, staccatissimo and double-tongue rows; shorts have no release trails, so hold the notes long enough for the room to ring.
- **Where (mockup-events.tsv).** Flute 1 bars 30, 94-96; Oboe 1 bar 30; Clarinet 1 bars 30, 96; Bassoon 1 bars 88-90; Cor anglais bars 91-93 (36 notes).
- **Now (read).** The Sus or Leg row with the note shortened (written eighths play 0.25 qn on Sus MAX, e.g. Bassoon 1 qn 350.5-351.5, Flute 1 116.5-117.5; parts.json); KS envelope release 177 ms (patch).
- **Tried.** c03: Bassoon 1 on "Stac DblTng RRx9" peaked at +0.073 s against +0.060 s for Sus MAX at half length, judged "not faster", reverted in c04 (M1 c03). Judged on speed only, not timbre or decay. Wind staccato row deferred in c01-c02 (A6.2, A #5).
- **Change.** A/B on Bassoon 1 bars 88-90 and Cor anglais bars 91-93: "Stac DblTng RRx9" (loaded by default, unloaded by `UNLOAD_UNUSED_ROWS` because unused), note-off at about 0.6-0.8 of the written length, a lead like `STAC_LEAD_S`.
- **Installed.** Yes. **Memory.** One row per test track (inferred 0.1-0.3 GB).
- **How to measure.** Decay shape (level at +0.1/+0.2/+0.3 s after onset), 2-5 kHz front, level against neighbours, onset timing.
- **Evidence.** Inferred.

## 12. Recorded crescendo rolls for printed roll crescendos into a stroke

- **Manual.** p.123, p.125: Felt Cresc are recorded crescendo rolls in three lengths (three key ranges) that end on a hard final stroke, "the most realism" for a crescendo roll; Felt Rolls with CC1 give "more control over length".
- **Now (read).** Rolls on the Rls row with CC1 from the printed curve (`TIMP_CC1_MAP`), seeded re-strikes (`TIMP_ROLL_RESTRIKE`), `TIMP_ROLL_TRIM_DB`. The timpani part has 13 crescendo hairpins (mockup-events.tsv).
- **Measured state.** No roll is the loudest stem except in the solo opening bar; in tuttis the rolls sit 10-18 dB under the master (c35 critic B). Dan's roll rule is met.
- **Change.** Only where a printed crescendo roll ends on a stroke and lasts about as long as one of the three takes (read the take lengths from the `.ews` headers first).
- **Installed.** Yes. **Memory.** One row. **Tried.** Never.
- **How to measure.** Level curve of the roll against the printed hairpin; the arrival stroke's level and 2-5 kHz front against the c34 stroke.
- **Evidence.** Inferred; low gain.

## 13. Bass trombone's lowest notes

- **Measured (patch).** The Solo Trombone KS Master's sustain and legato samples have roots E2-C5 (MIDI 40-72); its key map stretches the sustain down to C2. The bass trombone's three notes MIDI 36-38 at qn 451.78, 455.89 and 459.89 (bars 113-115, 3-4 qn each, in the stringendo) are E2 samples transposed down 2-4 semitones.
- **Manual.** HO has no solo bass trombone; the bass trombone is part of "2 Trombones and 1 Bass Trombone" (p.100; 2025 p.63-64).
- **Change.** Optional: play those three notes from the 3TB KS Master in the second-pass session, or leave them.
- **Evidence.** Measured range; audible effect inferred and small.

## Memory plan

- **Now (measured).** The 33-instance project settles at 45.80 GiB, the 34-instance one at 46.55 GiB; renders add 1-2 GiB (c35 `memory_test.txt`, c24-c34). The brief's cap is about 45 GB, so the main session has no room for another instance.
- **Second render pass.** Render any added instance (Solo Cello, divisi tracks, 3TB) in a second REAPER session that holds only those tracks, with the same tempo map, pre-roll, hall IR and send, and add their stems to the master before delivery. The manual recommends separate passes for exactly this reason (p.222). One Opus instance with several instruments (multi-timbral, p.52) does not reduce sample memory (inferred).
- **Rows in the main session.** Each added row costs about 0.1-0.3 GB per track (inferred from c24 and c14). Add rows on test spans first and read `footprint` after the settle; drop rows a test does not keep.
- **Mics.** Swap mics (item 4) rather than add them; Surround/Vintage stay off (p.139, 2025 p.86).
- **Preload.** Keep `PreloadSize` 1. The manual says a hard drive needs more preload, not less (p.32-33; Opus p.27-28); the samples stream from a USB drive reported as a Seagate "Expansion Desk" (diskutil), and late entries in earlier cycles came from memory pressure (KIT §11). Only Dan can change Opus preferences (KIT §11). Purge, Quick Load and Never Preload (p.32, p.43, p.59) load samples as they play and are not safe for a 1x offline render from that drive (inferred).

## Checked and consistent with the manual (no change)

- Legato joins within an octave (p.105, p.112): no legato join wider than 12 semitones on any track (measured in parts.json).
- CC1 and CC11 sent before the first note (p.151): the 3 qn pre-roll carries each track's first values (KIT §11).
- CC7/track level vs CC11 shaping (p.64, p.151): levels in the volume envelope, CC11 for the line.
- Brass dynamics on CC1 (p.101): `CC1_DYN_TRACKS`, `CC1_DYN_MAP` 18-120; CC1 stops at 120 at fff, below the last of the overblow range (p.106).
- Timpani rolls on CC1's 8 layers (p.124-125): `TIMP_CC1_MAP` since c12.
- Harp Sus RR velocities 46-112: no nail picks (p.69 puts them at 124-127; measured in parts.json); the decay envelope fixed in c35.
- Tam-tam on the 32in long hit (key 36, 12 velocity layers, p.118) with a velocity floor of 60; suspended cymbal on the crescendo-sustain takes (MIDI 60-65, p.119).
- Con sordino is not printed in v621 (the CC15 lane holds one "off" point).
- Sul tasto: only Violins II bars 147-155, and that passage is a tremolo. No Hollywood Strings section has a sul tasto tremolo (p.92; 2025 p.53-58), so Tremolo plus the EQ in mix.json is the available route; non-tremolo sul tasto on 2nd Violins already goes to Flautando in score_to_parts.py.
- Finger position (CC70, p.145-149): ~~no sul G/D/C/A is printed in v621~~ [Edit c38: seven sul G/D/A spans are printed as TextSpanner texts, which mockup-events.tsv does not carry; tried in c38, see Results (c38)].
- Moods, Movie Mixes, SSL strips: not applied; the patches' SSL strips are inactive and no Movie Mix data was found in the installed patches (read).
- String shorts: the KS envelope release (931 ms on 1st Violins) lets staccato samples finish after the note-off, as p.102/p.110 ask (read). Corrected in c36 (critic A): the short rows carry their own group envelopes (1st Violins Stac RRx14 release 333 ms, Staccatissimo RRx9 sustain 1.0 / release 524 ms, Celli Stac RRx9 decay to 0.001 over 1.78 s / release 372 ms), so a 0.12 s note-off ends a 0.5-0.8 s staccato file early; the -10 dB lengths still measure 0.17-0.29 s.

## Considered and ranked low

- 18 Violins instead of 1st Violins (p.10-11): no bow-change legato row (patch), and every Violins I fit would need redoing.
- Brass crescendo patches and Sforzando Crescendo (p.103-104): fixed lengths; the CC1 crossfade already follows printed hairpins.
- Layering a short articulation on accented notes with velocity-range triggers (p.162, p.189-190; Opus p.86-87): two rows sounding at once and more memory; the fitted swells already meet the 2-4 dB rule.
- Measured Tremolo TS / Repetitions TS rows (p.97-98): `MEAS_TREM` strokes measured better than the Tremolo row (M1 c13); the TS rows are untested and tied to the host tempo.
- Opus Humanizer and MIDI Compressor (p.154-155): random humanizing would break repeatable renders; levels are set in the pipeline.

## Results (c36)

- **Staccato rows (p.94, strings).** The 1st Violins KS Master's row names are swapped against its samples: "Stac RRx14" plays the "V1 Staccatissimo" folder, "Staccatissimo RRx9" plays "V1 Stac" (read from the region sample paths; the 2nd Violins "Stac Slur RRx6" plays "V2 Stacattissimo"). Violins I's printed staccatos moved to "Staccatissimo RRx9" (`STAC_ROW`, full rebuild, memory neutral: one row replaces another). Measured: peak +0.075 -> +0.065 s after the score onset, -10 dB length 0.17 s unchanged (other sections 0.28-0.29 s), dip between notes 14.8 -> 15.1 dB. The staccato recording of the 1st Violins decays faster than the other sections' in itself.
- **CC7 (p.64, p.151; "Checked and consistent" above).** CC7 does not act after Opus's hall (measured), and since it moves the timpani roll levels it is a pre-hall, voice-stage control (inferred): a -12 dB CC7 drop 0.8 s after a ff trombone cut-off left the hall tail unchanged within 0.1 dB, and the default CC7 is 127 (a lane at 127 changed nothing). A pre-hall level step (subito, a cut while a note rings) can use CC7; the post-hall REAPER envelope cannot (Dan's c35 note on bar 62).
- **Crescendo rows (ranked low above).** Not tried: the sustain bloom before printed crescendos was cut in the volume envelope instead (`CRESC_FRONTS`, 18 notes, growth by thirds median about +2.4 -> +5.2 dB). The "Cres Slw" row on the bar-11 horn crescendo (critic C) remains a possible test.

## Results (c37)

- **#2 Repetition rows (p.101, p.106, p.109-110, p.112): tried as an A/B, per track** (`REP_ROW`, `REP_ROW_GAP_S` 0.03 s; control Contrabassoon 520-548 on the old re-tongue, unchanged within 0.0 dB / 0 ms). Medians per repeat, c36 (emulation: gap + CC11 fall) -> c37 (row):
  - Contrabassoon, "LegRep RRx4", bars 27-32 ff quarters (15 repeats): dip 4.4 -> 2.9 dB, perceived attack +0.013 -> 0.000 s, 2-5 kHz first 80 ms minus body -8.1 -> -6.9 dB; repeat body re the run's first note -2.2..+1.6 dB (round robins; c36 +-0.6). Kept.
  - Horn 4 (1FH KS Master), "LegRep RRx4", bars 117-125 whole-note G3 at ff-fff-p (7 repeats): dip 6.0 -> 3.2, attack +0.065 -> +0.050, 2-5 kHz -11.0 -> -5.3 (the recorded re-tongue is heard as an attack). Kept.
  - Bassoon 1, "LegRep RRx4", 132 (bar 34 motif) / 352 (bar 88 fugato): dip 5.0 / 6.8 -> 1.4 / 8.6, attack +0.058 / +0.107 -> -0.061 / -0.019; 132's body 3-4 dB lower (the row's sustain fades in under the attack). Kept for the listener; 132 needs a longer gap or a level step.
  - Clarinet 1, "Leg Slur Rep", motif repeats 108 / 508: dip 9.5 / 5.3 -> 3.0 / 4.0, attack +0.009 / -0.013 -> -0.026 / +0.097. Kept. **640 (bar 160, fff) failed**: the repeat did not sound (VoiceTimer 30 ms: the 639.5 release trail started 30 ms before it; inferred from the start modes); reverted, c36 audio spliced.
  - Memory: four rows (one per track) cost about 1 GB at `top`'s resolution (46 GB settled with 27 GB compressed, against 45 / 20 in c36).
  - Verdict: the rows give a real tongued front where the emulation gave a swell after a hole, at the cost of shallower separation with a 0.03 s gap. Next: gap 0.05-0.06 s (inside the 200 ms NoteTimer, clear of the 30 ms VoiceTimer), re-test Clarinet 1 640, then extend to Contrabassoon 520-548 and the other horn pedals.
- **#10 Timpani hands (p.123-124): done** (`TIMP_RH_ALT`, 18 strokes on the RH Lng regions at pitch + 24): stroke-to-stroke 1/3-octave spectral SD 1.0-1.7 -> 2.6-2.7 dB in the eighth runs of bars 82 and 133-134, right minus left within 0.6 dB, no memory cost.

## Results (c38)

- **#2 Repetition rows, second pass** (`REP_ROW_GAP_S` (0.06, 0.15): each repeat keeps its track's re-tongue gap, frac and CC11 fall; `REP_ROW_REPEATS_ONLY` brass). Medians per repeat, c37 (row, 0.03 s, no fall) -> c38; the c36 emulation in brackets:
  - Contrabassoon bars 27-32 (15): dip 2.9 -> 5.3 dB (4.4), 2-5 kHz front -6.9 (kept). Horn 4 bars 117-125 (7, repeats only): dip 3.2 -> 7.2 (6.0), front -8.7, perceived attack +0.095 s (c36 +0.065); its three phrase entries back on Sus MAX (front minus body -4.3 -> -2.3 dB). Bassoon 1 132: 1.4 -> 5.0 (5.0); 352 unchanged 8.6. Clarinet 1 108 / 508: 3.0 / 4.0 -> 9.0 / 5.5; **640 (fff) now sounds** on "Leg Slur Rep" with a 0.10 s gap (dip 7.6, front -1.5). Bass clarinet 308 / 428 (new, BC LegRep RRx4): 6.4 / 4.3 -> 6.0 / 5.1, attack -0.069 -> -0.007 s at 308, front +2.4 / -2.8 dB.
  - Memory: one more row (Bass clarinet); the project still settled at 45.92 GiB.
  - Verdict: keep; the rows give the recorded re-tongue front and, with the emulation's gap and fall, the deepest separation of the three variants. Next candidates: the Contrabassoon 520-548 control span and Horns 3-4 pedals (bars 20-22, 69-72, 131-142) on the same settings.
- **Finger position (CC70, p.145-149)**: `SUL_SPANS` with the CC70 value per note from the patch's own table (`fp_strings`: the Sus MAX row's CC70 start modes and each sample's string tag). Read: the start modes sit on the Sus MAX / Detache rows and the legato rows' sustain groups, not on the TLeg transitions or the short rows; the patch's table is narrower than the manual's pictures. Measured: with no CC70 the renders play FP4 (default 127), not the FP1 the FingerPosition parameter suggests; a c38 render with CC70 20 as the resting value moved 160-313 notes per section to a higher string (Violins I +1.1 dB, brighter) and was spliced back. With FP4 as the default the printed spans change only a few notes (Violins I / II 219 E-flat4 to the D string; the celli's open G2 at qn 3, 5.3 dB softer, lifted +4.5 dB); slurred notes did not change. Kept (resting value 127).
- **#9 Horn portato rows**: not tried; the four Horn 1 tenutos were evened in level instead (critic A #2 fix A).
- **#12 crescendo rows** (Cres Slw for the bar-11 horns, Cres Fst for the bar-40 trombones): not tried; level shapes and an sf-target hairpin rule used instead (Horn 4 growth +4.7 dB, trombones +6.4..+11.2 dB).

## Results (c39)

- **Second render pass (Memory plan): built.** `ALIAS_TRACKS` / `PASS2_TRACKS`, `build_reaper.py --pass2`, `reaper_ctl.py --pass2`, `render_cycle.py N --pass2` (README "Second render pass"). Four instances settled at 6.0 GiB; the main project stays at 45.6 GiB. Items #3 (solo cello, once its samples are installed), #7 (half-section divisi) and #13 (3TB) can go there at no cost to the main project.
- **a2 brass (A #5 / C #2):** "2 Trumpets" (2TP) for the Trumpet 1-2 unisons (21 notes): about +6 dB at ff / +2 at f and 5 dB brighter in 2-5 kHz at f than 1TP at the same controllers; fitted per dynamic and per note (CHANGES c39). "2 Trombones EXP" not used (no legato row, Close + Stage without Main, Stage / Edge column mismatch, 700 ms release).
- **#11 Woodwind staccato rows: tried and kept** (second pass; Bassoon 1, Cor anglais, Flute 1 fugato windows on "Stac DblTng RRx9"): peaks 0.06-0.16 s, rise 0.03-0.09 s, natural decay instead of a swell to the note-off; pc within about 0.03 s of the doubled strings after a 0.03 s Cor anglais lead. Oboe 1 / Clarinet 1 bar 30 not tried.

## Results (c40)

- **#3 Solo cello (p.82-88): the DIV A route, in the second pass.** Hollywood Solo Cello is still not installed, so the coda "Solo espr." (680-696) was played by "Cello solo" on Celli KS Master DIV A (Close only), A/B against the section patch on the same notes in the same pass. DIV A kept: no join hole (max dip 3.4 dB; section 6.4, c39 11.2), image correlation 0.85 (section 0.74; cor anglais 0.84), level fitted to the section's contour (cor anglais margin 5.4 dB). Its Leg Port MAX target at 685 blooms and arrives +0.28 s late; with Solo Cello installed, play 685 as a slow Legato Slur (p.86-87) and put CC1 on the printed dynamic (p.82).
- **#8 Slower legato transitions (p.144): tried on the DIV A solo only** (`LEG_VEL_SPANS` velocity 70). The transitions did not follow one lead: per-onset leads of 0.03-0.25 s brought the perceived attacks to -0.04..+0.09 s. Not separable from the patch change; a section-line test (celli dolce bars 46-54) is still open.

## Results (c41)

- **#8 (script side): the LegatoSpeed script's START_MAX / RELEASE on Violas and Celli, tested and not adopted.** Critic C
  #1 read that the violas' and celli's KS Masters cap the velocity-to-start-offset map at START_MAX 2173 / 2709 samples
  (1st Violins 4800), so at v124 they play 40-55 ms more of each recorded slide, and proposed shortening the slide. Four
  fresh instances in the second pass (`TEST_TRACKS`, mix key `legato_speed`) played the main tracks' own notes, lanes and
  leads: A = START_MAX at BUMPRED (3890 / 3130), B = START_MAX 4800 with RELEASE 300 ms (patch 510 / 443). Away from
  the transitions they matched the main stems (per 1 s frame median 0.00 dB). Measured on every monophonic legato join
  (124 viola, 263 celli; `cycles/c41/actor_scripts/legtest.py`): the both-pitches-within-6-dB window did not shrink (per
  join median change +0 ms in all four; violas 98 / 98 / 94 ms median, p75 133 / 134 / 134; celli 108 / 110 / 108, p75
  146 / 148 / 148, main / A / B; the violins measure 86-101, p75 112-120 with the same method); the crossover moved
  earlier as a whole (violas -20 / -34 ms, celli -2 / -9 ms median), so START_MAX acts as a lead, as the c38 actor
  predicted; crossover and perceived attack agreed within 30 ms on 22-29% of joins in every variant; joins with dips of
  5 dB or more rose (violas 9 -> 13 / 18, celli 24 -> 24 / 33). Variant B narrowed the celli's perceived-attack spread
  (robust SD 96 -> 81 ms, 53% -> 44% more than 60 ms off) only together with nine more 5 dB holes. The remaining lever
  for these joins is the per-onset lead tables, fitted with an estimator that agrees with the crossover (C's step 5).
- **#2 Repetition rows on two more brass tracks (critic A #5):** Horn 1 (452, 528, 624) and Trumpet 2 (124, 456) on
  "LegRep RRx4" with the c38 gap rules. The gap minimum did not change (the dip measured against the lower body stayed
  1.8 / 3.2 / -1.3 dB on Horn 1), but the re-attack came in 2-5 dB louder than the Sus repeat over its first 0.5 s
  (re-attack over the gap Horn 1 452 4-5 -> 8-10 dB) with a brighter front (2-5 kHz front minus body 452 / 624 -11.5 /
  -15.5 -> -8.6 / -9.2 dB). Kept on Horn 1 and Trumpet 2 456 with the body excess past 0.1 s trimmed; Trumpet 2's
  accented ff 124 (+4..+6 dB, dip 1.0 -> -0.4) went back to Sus. The settled main project stayed at 45 GB (top).

## Results (c42)

- **#8 Slower legato transitions: its premise did not hold.** The c41 reading that the violas' and celli's slides last
  174-236 ms against the violins' 112-126 came from an estimator whose harmonic bands shared the two pitches' partials
  under 220 Hz (critic A #1, checked by the actor with a synthetic instant switch per join: that method reads a median
  15 / 44 ms and p75 428 / 399 ms of overlap on perfect viola / cello switches). With exclusion bands (`tools/pcx.py`)
  the transitions last 94 / 98 ms (violas / celli) against 82 / 97 ms (Violins I / II). There is no long slide to
  shorten; a slower legato (velocity 60-75) remains a colour choice for cantabile lines, not a timing fix. The lower
  sections' remaining timing spread is per join and is handled by per-onset leads fitted on pcX (c42).
- **Repetitions TS (p.97-98; ranked low above), read for a later test (critic A #2).** The Basses and Violas KS Masters
  have it (Basses key 87). The patch has `tempo` 120, `tempoSync` true, `elastiqueType` 1, and the manual says the
  repetitions "adjust the speed of the internal beats to the current tempo"; CC11 crossfades three dynamics, velocity is
  ignored; the controller map lists "Repetition" CC69, "Repetition: Sustain" CC64, "Repetition: Reset RR" CC36. The
  internal rate is unclear: the manual describes about a dozen pulses in a little more than one second (about 10 per
  second, faster than eighths at 126 bpm, 4.2 per second), critic A read 2.5 s samples recorded at 120 bpm (about ten
  eighths). Before an A/B on the basses' eighth pedals, render one held note on the row at 126 bpm and measure the
  inter-onset interval of its internal strokes (A's step 4). Not done in c42 (optional; the second pass carried the
  bar-62 aliases).

## Finale results (c02)
- p.98-99 portamento (Leg Port MAX), c02: the printed "port." at bar 236 (Vln I/II C5 -> A5, qn 941) on Leg Port MAX at velocity 100 (`PORT_TARGETS`); the row loaded for both violin sections (full rebuild). Violins I 936-944 span level -38.5 -> -37.5 dB. The glide itself is not yet measured (critic A's target: +10 dB at the intermediate semitones 73-80 over the Leg Slur version).
- #11 (staccato rows), c02: Horns 3/4 F1 on Marc Shrt (was StacSs) and Horn 1's 38 staccatos on Marc Shrt; level refit by stem fix (-5.6 / -6.9 dB on the c01 roles).

## Finale results (c03)
- p.106-107 stopped horn ("Stop Sus", 1FH KS key 80, keys 36-76), c03: the five printed "+" notes (Horn 1 qn 192 and 668, Horn 2 668, Horns 3/4 548) on the row via `ART_SPANS` (full rebuild of Horns 1-4). Measured on the stems: 2-5 kHz minus 0.5-1 kHz +27 to +40 dB over the open notes (the nasal stopped colour), but K-weighted level re master 2.2-12.8 dB lower (the sf chord at 548 lost the most); refit by stem fix with `roles.json` rows (+2.5 / +8.5 / +10.5 / +7.5 dB), now 2.3-3.3 dB under the open c02 notes. Kept.
- Opus p.133-134 IR envelope, c03: `ir_setup` envelopeMode 2, endPos 0.5, decayLength 0.5 (Movement I c44). Final fermata RT(-5..-25 dB) 1.58 -> 1.31 s, late RT(-20..-35) 2.51 -> 1.98 s, drop at 1.0 s 35.1 -> 36.7 dB.

## Finale results (c04)
- #11 p.110 woodwind staccato rows, c04: every printed staccato of Flute 1 (45 notes), Flute 2 (22), Oboe 1 (38), Clarinet 1 (26) on "Stac DblTng RRx9" (key 28), velocity 72-104 from CC11, 0.03 s lead; Bassoon 1's c01 span extended to the whole piece (55). Harmonic-band peak after the score onset +135 / +162 / +165 / +148 ms -> +70 / +97 / +57 / +85 ms (Bassoon 1 +75), peak level within -1.3..+1.4 dB of the c03 slices (median), no refit. Memory 44 -> 45 GB settled. Kept; Oboe 2, Clarinet 2, Bassoon 2 and the cor anglais are next if their staccatos are exposed.

## Finale results (c08)
- #6 (round-robin reset on CC16), c08, one reset inside the music: a CC16 = 127 event 0.02 qn before the basses' first eighth at qn 1056 (tools: `RR_RESET_AT`, parts.json lane `cc16`, written by build_reaper.py without a pre-roll copy). It worked: the Hollywood Strings Basses KS Master's Sus MAX bow-direction cycle restarted there. In 1056-1088 the raw off-beat strokes (stem level minus the written metric step) went from 1.0-2.3 dB over the beats (c07) to 3.3 dB under them; per-position SD stayed 0.4-0.9 dB. So a mid-music reset on Opus's configured controller (Preferences.json RoundRobinResetCC 16) does move which stroke is strong, where CC36 inside the music did not (M1 c14, c49). Not yet tried: CC16 in the pre-roll of every track (the full item; per-note fits would move once).

## Finale results (c09)
- p.103 Sforzando Crescendo ("Sfz Cres" row in the 1FH, 1TB and 1TU KS Masters; critic A #1's A/B for the brass "sfp <" at bar 149): not tried. c09 first fixes the cause measured in the data (every led sfp note started on the p layer because the CC pull read the level after the spike; tools `FP_SPIKE_AT_MARK`). Each row costs a full rebuild and about 0.1-0.3 GB per track on 8 tracks, with REAPER at 44-45 GB settled. Next step if the brass sf at 592 still measures more than 1 dB under the ff before on the c09 stems.
- #1 / p.106 Legato Slur Accent (critic A #3's A/B for the 10 accents inside brass slurs): not tried, same memory reason; c09 moves the gentle-accent swell to the moved note-on first (`ACCENT_SWELL_FROM_MOVED`). Also unknown and worth a short range test first: whether a keyswitch from Leg Slur MAX to Leg Slur Accent MAX inside a slur keeps the legato transition.

## Finale results (c10)
- #5 p.109 expressive rows, c10 (first try in any movement): Bassoon 1's "solo, espress." (qn 455.9-496, 18 legato joins) on the BS KS Master's "Leg Slur Exp" (key 77), CC1/CC11 lanes unchanged, full rebuild of the track. Joins pcx median +14 -> +10 ms (IQR -42..+20, none over +80 ms); attack to -6 dB of the body 20 -> 35 ms; level +2.2 dB K (stem fix -2 dB); 4-7.5 Hz share of the amplitude modulation 0.46 -> 0.18 (pitch vibrato not measured). REAPER stayed at 45 GB settled. Kept for the critics' ears; the cor anglais (680-744) and Oboe 1 (376-392, 744-760) solos are next if it is judged better.

## Finale results (c11)
- p.101 Sustain Accent ("Sus Accent MAX", 1FH / 1TP / 1TB key 25, 1TU key 61) for the brass sfp at 592 (critics A #2, C #1; velocity sets the sf, CC1 the p): not tried. The coordinator's condition was REAPER under about 44 GB settled, and c10 / c11 settle at 45 GB (32 GB compressed). The no-memory fallback, a +3 / +4 dB post-fader bump on Horn 1, Horn 3, Trombone 1, Clarinet 1 and Bassoon 1, put their fronts within -1.6..+1.9 dB of the ff before and four peaks at +0.00..+0.09 s; the master's peak is still +0.27 s (Trumpets 1-2's ff accents, the tuba, Horn 3). Try the row on Horn 3 and the tuba when memory allows. p.103 "Sfz Cres" is the wrong shape for an sfp (a strong crescendo after the attack), so it is off the list for 592.
- #5 p.109 expressive rows: Bassoon 1 kept on "Leg Slur Exp" (critics A, B, C). Its five early joins were lead errors, not the row's: with the leads trimmed the solo's joins are -24..+19 ms except 464 (+134 ms, inferred estimator effect of a level trim). Cor anglais (680-744) and Oboe 1 (376-392, 744-760) deferred for memory.

## Finale results (c12)
- No gap was tried in c12.
- p.101 Sustain Accent ("Sus Accent MAX") for the brass sfp at 592: the three critics dropped it for this cycle, and the level-only route met the target without a new row. A volume notch 0.11-0.40 s after the mark (-3 to -5 dB on Horn 1, Horn 3, Trombones 1-2, Bass trombone and Tuba) plus the c11 +3 dB front on the low brass moved the master's peak from +0.235 s to +0.020 s after the mark and put its first 0.1 s 0.2 dB over the ff before; the p after it is unchanged (-7.3 dB). The row stays untried in this movement. Memory is as before: 44 GB settled, 45 GB after the render.
- #5 p.109 expressive rows on the cor anglais (680-744) and Oboe 1 (376-392, 744-760): closed by the coordinator for c12. Bassoon 1 stays on "Leg Slur Exp".
- #6 CC16 round-robin reset: Movement II's reset table for further spans (`RR_RESET_AT`) was not added (coordinator: a later cycle).
- 1TP KS Master "Mute Sus" (Trumpet 1's muted solo, 680-792), measured this cycle: the row plays a fresh attack on every note, and its held notes carry an amplitude flutter of about ±6 dB with a period near 120 ms. Overlapping slurred notes by 30 ms on this row doubled the time in which both pitches sound (median 34 -> 70 ms), so it does not stand in for a legato row. The 1TP KS Master has no muted legato row (`build/ks_maps_extra.json`: "Mute Sus", "Mute Sus Accent", "Mute StacSs DblTng RRx9"), so the choices left are a shorter overlap or none.

## Finale results (c13)
- #6 CC16 round-robin reset on a percussion patch, c13: `RR_RESET_AT` now also acts on percussion tracks. "22in Zildjian K Crash" (groups "Long RRx1/2/3") with CC16 = 127 half a quarter before each of its three strokes: first 0.5 s -26.5 / -26.8 / -26.8 dBFS and the 4-12 kHz band within 0.4 dB (c12, without resets and with a -3 dB row on the second stroke: -26.5 / -29.8 / -27.1, 3.4 dB apart in the band). The second stroke is the c12 sample (exactly +3.0 dB, the deleted row); the third changed by 0.3-0.4 dB. No memory cost.
- #6, the same controller at a pizzicato entry (CC16 before qn 200 / 201 on the four lower string tracks): every later round-robin choice on those tracks changed. 73 long notes after the reset moved by 2 dB or more against c12 (Double basses 52, single notes up to +9.6 dB). A reset is therefore a data change for the rest of the track, up to the next reset; add resets at fixed places once, then leave them.
- Range test of an earlier keyswitch (`KS_LEAD_S` 0.045 s instead of 0.06 qn before the note-on): no effect on the notes that change level between renders; not adopted. The same test showed those notes at two levels in two renders of one unchanged project, which fits round-robin position and not keyswitch timing. Not tried yet: CC16 in the pre-roll of every track.
- #6 (manual p.145), c14: CC16 in the pre-roll of every track and before each section's first note. Two range renders of one project: 2036 of 2123 notes equal within 0.5 dB, pizzicato to 0.00 dB. Round-robin takes are now repeatable; the notes that still differ are row-change legato joins (a keyswitch effect, not round robin). Closed as a gap; the Repetition script (CC69) on winds and brass stays untested.

## Finale results (c15)
- Sustain (manual p.91) as the one row of a fast theme: tried in c15 on the first theme (Violins I / II, Violas, Violoncellos, Double basses), with the staccato rows (p.94) kept for printed staccatos. Result: no legato-side row change left, notes outside 25 / 60 ms on the nine lines of bars 11-34 181 / 42 -> 140 / 30, lines repeat between renders. Marcato Sustain (p.91-92) and Détaché were not needed. Keyswitch placement (p.99): 0.15 s early works between sustain and staccato rows, not on the legato rows of the second theme (joins 36-45 ms later).
- #8 (p.144, legato velocity): a cap at 112 on Horn 1 / Trumpet 1 gave no clear gain in join spread (c15 range test); closed.

## Finale results (c16)
- New item (critics A / B / C, manual p.53-54, 64, 137, 150-151): "level shaping of a line belongs in CC11 / CC1 and velocity; Volume sets a track's level against the others". State after c16: the track envelope holds no rule keyed to a single note (Dan's decision of 11 Nov). Used now: velocity for the theme's staccato rows (`ROW_VEL_SPANS`; the rows answer to velocity, 3-11 dB for 16-22 steps), the per-row volume knob (p.137; mix.json `row_volume_db`, tremolo and staccato rows), a CC11 / CC1 bump of 5 units on printed accents (`ACCENT_BUMP_AT`), "Stac On Bow RRx9" with velocity by position for the basses' repeated eighths (p.93). Not yet moved to the instrument side (each was a fader rule until c15, now absent): per-pitch and per-note level differences on the sustain rows (CC11 step per note), re-bow fills (overlap or a CC11 fill), same-pitch separation on winds and brass (gap length, repetition rows), divisi chord levels (CC11 per chord), pizzicato per-pluck levels (velocity), timpani stroke weight (velocity; the scherzo measured about 3 dB per 22 steps), sagging long notes (CC1 / CC11 rise).
- #1 (filtered marcato attack for brass accents, p.101, 62-63): still open; with the fader swell gone the brass accents rest on the CC1 bump alone.
- Basses "Marc Lng RRx4" / "Marc Shrt RRx4" (p.93): "Marc Shrt RRx4" tested on the repeated eighths (range render): separation median 8.0-11.0 dB, 8 / 12 / 2 repeats under 3 dB; "Stac On Bow RRx9" was better in two of three spans and is used.

## Finale results (c17)
- Mic positions (p.138-139; related to #4): Double basses Close 1.0 / Main 0.4 with the 87.3 Hz bell at 0 dB, range render of bars 11-34, 211-217, 223-234: F2 +5.8 dB and F sharp 1 +8.1 dB over the median pitch at p / mf (30-125 Hz), stem 5-10 dB hotter. Rejected; the F2 peak is not a Main-pair resonance alone.
- Controllers on the sustain rows (p.53, 64, 150-151): accents, row levels and the timpani roll levels now live in CC11 / CC1 / CC7 (`tools/instr_post.py`); the accent rows of #1 ("Marc Sus LITE", "Sus Marc LITE") were not needed for medians of +2 to +4 dB and stay untried.
- Staccato On Bow (p.92-93): velocity 80-100 gives no level change on the basses' row; CC11 does.
- Timpani Hard Long (p.125-126): left- and right-hand samples differ by 4 dB at equal velocity (#10's alternation therefore needs a velocity offset per hand).
- #2 (re-tongue rows): still untried; the joins that stay under 3 dB after the gap floors (Horn 3, Bassoon 1, eighths of bars 91-92 and 277) are the candidates.

## Finale results (c18)
- Region volumes (Opus regionMap `volume`; p.137 lists only the row volume): used per row group on the oboes ("Sus MAX" and "Leg Slur MAX" tables) and on the pizzicato rows of celli and basses. Oboe pitch levels within 2 dB; pizzicato basses 3.7-6.4 dB peak range; pizzicato celli not evened (round-robin spread).
- Sustain rows and CC11 (p.91, p.109): strings "Sus MAX" has a knee near CC11 100-103 (flat above, about 0.7 dB per unit below).
- #2 (re-tongue rows LegRep RRx4 / Stac DblTng RRx9, p.109-110) and the basses' short rows (Marc Shrt, Staccatissimo, Spiccato, p.92-94): not tried this cycle (no calibration range: two threads were waiting for REAPER). Still the candidates for the eighths of bars 91-92 / 277 and for the chorale's re-tongued whole notes.

## Finale results (c21)
- Harp KS Master "Harmonics" and "Gliss Technique" (p.70; new item, critic A c21 #4): used through ART_SPANS for the printed harmonics (qn 168 / 176 / 184) and the bar-277 glissando, the rest on "Sus RR". The KS Master's triggers sit on keys 21-35, where the harp plays (26-35 here): the Harmonics / Gliss Technique triggers were moved to keys 112 / 113 in the Opus state (mix.json `ks_keys`, `ks_unused_off`; first time a trigger key was moved) and it worked on the range render (the note at 264 after the harmonics played on Sus RR; no row switches from the low notes). Measured (R1): the harmonics' spectrum changed (B flat 4 minus B flat 5 +24.9 -> +18.4 dB, centroid 480 Hz) and they came 9 dB over the plucks; the KS Master's Sus RR plays 5-7 dB over the Harp Sus RR patch (bar 264 +7.3, glissando +5..+6, final chord +1..+2): gain -4 dB and Harmonics -5 dB set without a second range test.
- Cor anglais "Leg Slur MAX" legato bloom (A c21 #2): a +4 dB region gain on the "TLeg" transition groups did nothing to the rise (legato-target median +2.8 against c20's +3.1 dB) and raised the line 2.4 dB against Trumpet 1; "Sus MAX" over the unison spans (C's variant) took the long unison notes' rise from +4.5..+7.6 to +0.7..+3.9 dB and was adopted.

## Finale results (c22)
- Harp KS Master velocity (p.69: "CC 11 and Note Velocity control overall loudness"): the KS Master's patch lacks the Velocity->Volume path the Maestro patch has; copied into the state (`vel_volume`), measured as above (CHANGES c22).
- #8-like (legato transition speed by velocity, p.144) on the woodwinds: a velocity floor of 96-116 did not change the transition-to-sustain holes (range test). The sustain groups' AHDSR attack (438-738 ms) capped at 200 ms made them worse. The holes are in the samples' crossfade; candidates left: "Leg Slur Exp" rows (#5) or playing held targets on "Sus MAX" as on the cor anglais (c21) and Horn 1 (c22).
- #2 (re-tongue rows for brass repeats): still untried; after the failed CC11-fall emulation in the chorale (c22) it is the next candidate for the chorale's repeated whole notes.

## Finale results (c23)
- Woodwind LegatoSpeed script `SSOFFSET` (new item; the script's connected-sustain start offset; ships 1956 on oboe / clarinet, 0 elsewhere; on the OB / CL KS Masters `SUS_GROUP_SUBSTRING` is "Obs" / "CLs" while the groups are "OBs" / "Cls"): SSOFFSET 11025 (0.25 s) with the corrected substrings on Flute 1, Flute 2, Oboe 1, Cor anglais, Clarinet 1, Bassoon 1, range test against a control range from the same starts: on the legato targets that stayed legato, 6 dB holes (200 ms window on flutes / oboe / cor anglais, 30 ms on clarinet / bassoon) 4 -> 6 (Flute 1 330 7.7 -> 5.7, Flute 2 602 / 650 closed; cor anglais 650 5.7 -> 7.5, Clarinet 330 new 7.2, Bassoon 850 5.2 -> 9.1). Not adopted.
- TLeg hold / decay (mix.json `tleg_env`, hold 550 / decay 250 ms; critic C c23 #4a): not measured. REAPER deadlocked (bridge heartbeat stopped) while the first variant track (Flute 1) loaded its new state in the range pass; killed and dropped this cycle. Still the untested candidate.
- Woodwind legato targets with an early hole (0.1-0.25 s) played on the sustain row 0.06 s early with no overlap (Horn 1's c22 fix): Oboe 1 384 / 964 / 1014, cor anglais 708 / 738, Clarinet 1 606 / 998 / 1014: all 8 under 6 dB on the range test and in the full render (e.g. Oboe 1 384 9.6 -> under 4, Clarinet 1 606 7.7 -> under 4). Adopted.
- #2 (re-tongue rows): not needed for the chorale this cycle: a 0.12 s gap with no CC11 fall gave brass repeat dips 5-11 dB (below).

## Finale results (c25)
- Celli "Detache" (p.90; critic A c25 #1): adopted for the bass line of bars 11-26 and 151-166. Patch read: velocity does not pick a layer on this row (groups cover 1-127, no velocity processor); CC11 crossfades the mp and ff groups. Played at the ff group's CC11 with the f level as a passage level: back-minus-front median +2.8 -> +0.9 / -0.8 dB (range test). Releases capped at 300 / 150 ms (shipped 700 / 528).
- 40in Ludwig Bass Drum (p.122; critic C c25 #3b): adopted in place of the 36in (same key map). On the same notes it gave 6.7 dB more in 30-90 Hz at the fff stroke of bar 223; gain -3 dB to sit level with the basses.
- Channel Routing "Mono From Left" (p.141) extended from Horns 1 / 3 to Horns 2 / 4 (critic C c25 #4); result in the c25 CHANGES.
- Not tried this cycle: Half-section divisi patch (#7) for the Violins I "4 soli" (C c25 #5, ruled out of this cycle); "Marc Lng RRx4" for the lower strings' chord fronts (scherzo note: 6 ms attack, but a short row, which cannot hold the printed half and whole notes).

## Finale results (c26)
- "Leg Slur Runs" (manual p.112; FL / OB / CL KS Master keys 37 / 37 / 36; not in the BS KS Master), critic A c26 #1, range-tested with CC1 copied from CC11 (dynamics come from the Mod Wheel on this row): Oboe 1's p run of bar 47 (all seconds) became even (weak note 187.5 -8.1 dB and the 6.3 dB dip at 188 gone; no note more than 4 dB under its neighbours). Adopted on Oboe 1. Flute 1's run of bar 43 got worse (dips of 5.3-11.0 dB at five joins, weak notes -7.2 / -7.8): rejected on the flute. The row is a new Opus state row: full rebuild, and memory stays at 45-46 GB.
- Legato velocity of a run's first note (v53 -> v90; manual p.144: velocity sets the transition, not the level): no change in the holes after it (Clarinet 1 177.5 -8.7 -> -8.4 dB). Rejected.
- Round Robin Reset (p.34, p.145) placed to choose the take of a same-pitch repeat on the celli "Detache" row: a reset before the first note of a pair puts the repeat on the second take, which re-articulates (rises 7.2 / 7.3 dB at 98 / 658, against 1.6 / 1.0). In a chain of five repeats, 0.10 s gaps plus a -12 unit CC11 notch before each repeat lifted the first-take repeats from 1.1-1.4 to 5.3-5.4 dB.
- CC7 as a passage level (p.64, p.151), as the timpani already use it: Violins I CC7 80 (-4 dB) over bars 159-165 moved Violins II minus Violins I by +4.0 dB on average (measured -4 dB shift as written); violas CC7 90 (-3 dB) with a CC11 ceiling moved violas minus Trumpet 1 by 3.4-5.3 dB. CC7 behaves as 20 log10 on these string patches.

## Finale results (c27)
- CC7 on the woodwind and brass KS Masters (p.64, p.151; critic B c27 #5): range-tested by moving Flute 1's and Trombone 1's dynamic trims from the volume envelope into CC7 (`dyn_trim_to_cc7`, envelope at gain + largest trim, CC7 down to 27 = -13.5 dB): per-note level change against the envelope + CC7 model, median residual 0.00 dB, p90 0.44 / 0.39 dB, the same as tracks left on the envelope. CC7 is 20 log10(CC7 / 127) on these patches too, and REAPER does not clip a volume envelope at +16.6 dB. Adopted on every pitched track except timpani / harp.
- "StacSl Leg BC + Slur + Port MAX" (p.99; violas / celli "Stac Leg BC + Slur + Port MAX"), critic C c27 #2 for the late soft slur heads: not tried. The manual's text names a "Combinations" section for how Opus picks bow change / slur / portamento on the combination rows, and that section is not in the text, so the row could add portamento or bow-change noises on the joins; memory is at 45-46 GB. A CC11 front (+10 units from -0.06 to +0.25 s) was used instead (range T1: heads +140..+220 -> -12..+139 ms).

## Finale results (c28)
- "Leg Slur Accent MAX" (p.106; gap #1) for the late second note of accented brass slurs (Trumpets 1-2 970 +170 / +200 ms, Horn 1 818 +160, Horn 3 578 +140): planned as a range test (ruling 7), not run: it adds an articulation row on four brass tracks (full rebuilds in and out) and the cycle's lock budget went to the role-carry regression. Still untried; next candidate.
- CC7 (p.64, p.151): the c27 law holds; c28 measured that CC7 carries placed on the score point restore the reference levels within 0.6 dB on held notes (Violins I 888-892 30.5 / 31.0, final-chord strings within 0.1 dB of c26).
