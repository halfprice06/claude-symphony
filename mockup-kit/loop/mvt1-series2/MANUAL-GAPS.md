# Manual gaps: what the Hollywood Orchestra manuals offer that the v621 mockup does not use

Written 2026-11-06 (after c34; c35 was rendering). Sources: the May 2021 HO Opus manual (`guides/eastwest-hollywood-orchestra/text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt`, cited as `p.N`, PDF pages), the Dec 2025 library manual (`2025 p.N`), the Oct 2025 Opus manual (`Opus p.N`), the installed `.oib` patch files, Opus's `Preferences.json`, `build/score_config.py`, `build/parts.json`, `build/mix.json`, `build/mockup-events.tsv`, `tools/score_to_parts.py`, `tools/build_reaper.py`, `loop/HISTORY.md`, `loop/LEARNINGS.md` (cited `M1 cNN`), `mockup-kit/LEARNINGS.md` (cited `KIT §n`) and the c35 critic reports. The library digest is `guides/eastwest-hollywood-orchestra/DIGEST.md`.

Evidence labels: **measured** (a number from a render, from parts.json or from a patch file), **read** (read in the code, a patch file or a preference file), **inferred** (reasoned from the manual or from other measurements; not tested). Bar b starts at qn 4(b-1).

Ranking: expected audible gain for Dan's priorities (articulations; each track's level and the blend; timpani rolls under the texture). Items 6 and 12-13 are lower because their gain is indirect or local.

## Summary

| # | Gap | Manual | Where in v621 | Installed | Memory | Evidence | Tried before |
|---|---|---|---|---|---|---|---|
| 1 | Brass accents: a filtered marcato attack (Marc Sus LITE at low velocity) instead of a plain sustain plus a volume swell | p.101, p.62-63 | 200 marked brass accents (162 measured in c35); bars 23-26, 32-33, 41, 69-72, 80-83, 131-138, 142-143, 167-170 | yes | 1 row per track | problem measured, row read, gain inferred | Sus Accent at high velocity (harsh); CC1 front lift (failed); Marc Sus LITE never on brass |
| 2 | Repeated wind/brass notes on the sampled re-tongue rows (LegRep RRx4, Leg Slur Rep) | p.101, p.106, p.109-110, p.112 | about 340 re-tongued repeats (Cbn bars 27-32, 131-138; Horns 3-4 bars 20-22, 69-72, 118-126, 131-142; Bn2 bar 82); motif repeats into tenutos (bars 27, 127, 160) | yes | 1 row per track | problem measured, rows read, gain inferred | never |
| 3 | Hollywood Solo Cello for the coda "Solo espr." | p.82-88, p.222 | Vc qn 680-696, bars 171-174 | **no** (licensed) | 0 with a separate pass | problem measured, gain inferred | DIV A section solo removed for memory (c35) |
| 4 | Mid instead of Close mics on the woodwinds (then horns, trumpets) | p.138-139, p.222 | every wind solo; blend everywhere | yes | about neutral (a swap) | inferred | never |
| 5 | Expressive rows (Leg Slur Exp, Sus Exp) for espr./dolce wind solos | p.109; 2025 p.69-76 | 12 marked solos, bars 5-8 ... 175 | yes | 1 row per track | inferred | never |
| 6 | Round-robin reset on CC16 (the controller Opus is set to) instead of CC36 | p.34, p.143, p.145; 2025 p.92; Opus p.29-30 | every track (repeatability), celli stroke runs | n/a | 0 | read; symptom measured | CC36 since mvt II c24; CC16 never |
| 7 | Half-section divisi patches for soft div. passages | p.89-90, p.222 | Vla bars 47-68; Vln II bars 107-117, 147-155; Vln I/II bars 167-177 | yes | ~0.7 GiB per instance, 0 with a separate pass | inferred | deferred c01 (memory); worked in mvt II |
| 8 | Slower legato transitions (target velocity 60-75) on cantabile string lines | p.144, p.99 | Vc dolce bars 46-54; Vln I/II molto cantabile bars 56-61; coda bars 171-178 | yes | 0 | script read, gain inferred | v105/v108 vs v120/v124 only |
| 9 | Horn portato rows for tenutos | p.101 | Horn 1 bars 48, 51, 148, 151 and 19 more brass tenutos | yes | 1 row per track | inferred | never |
| 10 | Timpani: alternate left- and right-hand samples on repeated strokes | p.123-124 | 20 repeated strokes, bars 27, 30, 32, 82, 131-134 | yes | 0 | read; gain inferred | never |
| 11 | Woodwind staccato rows for printed staccatos | p.110 | 36 notes: Fl1 bars 30, 94-96; Bn1 88-90; CA 91-93; Ob1, Cl1 bar 30 | yes | 1 row per track | inferred | Bn1 test c03, judged on speed only, reverted |
| 12 | Recorded crescendo rolls (Felt Cresc) for printed roll crescendos into a stroke | p.123, p.125 | timpani crescendo hairpins (13) | yes | 1 row | inferred | never |
| 13 | Bass trombone's three lowest notes are transposed tenor-trombone samples | p.100; 2025 p.63-64 | qn 451.78, 455.89, 459.89 (bars 113-115) | yes (3TB) | 1 instance or a separate pass | measured (patch) | never |

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
- Finger position (CC70, p.145-149): no sul G/D/C/A is printed in v621.
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
