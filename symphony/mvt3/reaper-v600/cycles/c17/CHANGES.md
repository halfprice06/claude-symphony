# Cycle 17 (2026-11-11): every per-note level on the instrument side

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c16 render) and the coordinator's rulings 1-10. Snapshot of the tools and data before this cycle: `before/`. Scripts: `actor_scripts/`. Logs: `logs/`.

Standing rule (Dan, 11 Nov): the track volume envelope holds slow balance only. No per-note move, no exceptions.

## Tools

- `tools/instr_post.py` (new, generic; called by `score_to_parts.py` at the end of each track when `INSTR_POST` is set; values in `build/score_config.py`, last block). Rules: `rest_map` (resting CC level by a piecewise-linear map), `accent` (a controller bump per printed accent, in seconds, no stacking), `note_cc` (an offset held per note by pitch, row and dynamic, or chord size), `cc_shape`, `cc_cap`, `gap_floor` (played gap at tongued joins), `row_onset` (onset lead of a row's notes, optionally per round-robin position), `note_end`, `rebow_join` (no gap and a swell at a same-pitch bow change), `vel_pitch`, `vel_db`, `vol_to_cc7` (a track's envelope folded into CC7), `vol_guard` (fast fader moves inside sounding notes moved to the note-on or stretched). parts.json carries a report per track (`instr_post`).
- `tools/score_to_parts.py`: `UNI_BOOST_MIN_QN`, `UNI_BOOST_ONE_LEVEL`, `INSTR_POST` (the hook before the notes are written out).
- `tools/build_reaper.py`: mix.json `region_gain_db` (per-region volume in the Opus state by pitch and row; the scherzo's c15 tool, ported after the coordinator's note).
- `actor_scripts/`: `stepcheck.py` (ruling 1's check on parts.json), `c17meas.py` (separation at tongued joins, the basses' short-row strokes with critic A's half-rise detector, bass-band level per pitch, levels, stops, dips), `timpmeas.py`, `pluckvel.py`, `mixfit.py` / `levfit.py` (the dyn_trim make-ups, written from `before/mix.json`), `pdiff17.py`, lock phases `p1.sh`, `p1r.sh LABEL [--build]`, `p1mic.sh`, `p2.sh`, `after.sh`.

## What changed, by ruling (`build/score_config.py` last block, `build/mix.json`, `build/roles.json`)

1. **Fader (ruling 1).** `UNI_BOOST_MIN_QN` 8 and `UNI_BOOST_ONE_LEVEL`: a held unison level spans a phrase of 8 qn or more at one level, or is dropped (the one- and two-note plateaus are gone). `INSTR_POST["vol_guard"]`: every move of 2 dB or more within 60 ms that lay inside a sounding note is now before that note's moved note-on (hairpin-gain and held-decrescendo releases, role and player-count edges; in a rest where there is one, else a ramp of 20 dB/s over the end of the note before) or, for the falls after an fp / sfp attack and moves deep inside a note, stretched to 20 dB/s where it stood. `INSTR_POST["dyn_step_on"]`: jumps of the printed dynamic curve (which `build_reaper.py` turns into the dynamic trims) stand 0.03 s before the moved note-on instead of at the score onset (Movement I c58's finding, relayed by the coordinator). Timpani: the whole envelope (roll levels, settles, roll hairpins) is folded into CC7 (`vol_to_cc7`; Opus applies CC7 as linear amplitude), the track's `vol_db` is one flat point.
2. **Accents (ruling 2).** `rest_map`: plain notes at ff rest at CC11 105 (strings), 104 (woodwinds; 98 in the first build, raised after Movement I's finding that 88-98 is a plateau on the wind rows), 100 (brass and clarinets, where CC11 is plain volume); `dyn_trim_db` make-ups carry the level back (`actor_scripts/mixfit.py cycles/c17/fit_final.json`, fitted on two range renders by `levfit.py`). `accent`: a bump from 0.02 s before the moved note-on, held 0.15 s, back by 0.45 s (the whole note when shorter than 0.3 s), no stacking: strings +16 at f / +19 at ff (ceiling 124), woodwinds +14 / +20 (soft accents +2..+5: the next layer fades in at CC11 30-38 on the bassoon and clarinet families), brass and clarinets 21 % of the resting CC11 (trumpets 13 %, Horn 1 16 %) plus CC1 +3..+7 (ceiling 112, horns 117) from 0.08 s before. `ACCENT_BUMP_AT` 0 (the 5-unit bump is gone). No accent rows ("Sus Marc LITE", "Marc Sus LITE") were needed.
3. **Row levels (ruling 3).** `note_cc` `row_dyn` on the four upper string tracks: legato rows +6..+8 units at f and +10..+14 at ff, "Sus MAX" -4..-6 at f and -2..-6 at ff. No `row_volume_db` change (the scherzo's warning: a row volume moves every passage on the row). Horns, Trombone 1 and Trumpet 1's sustain notes in 247-262: not done.
4. **Double basses (ruling 4).** (a) Per-pitch levels as per-region volumes in the Opus state (mix.json `region_gain_db` on the "Sus MAX" and legato rows: E flat 2 +8, F sharp 1 +4, F1 +3.5, F2 +2.5, E2 +2.5, E flat 1 +2, B flat 1 +1, C2 -1, G1 -2, C sharp 2 -2.5, A flat 1 -3 dB), the scherzo's c15 technique, in place of the CC11 table first written (CC11 is flat above 114, so it cannot raise a weak pitch at ff). (b) 87.3 Hz bell -12 -> -9 (range test BELL); Close-led mic mix rejected (range test MIC). (c) Short-row eighths: 45 % of the slot, note-on 0.04 s before the score onset on all spans (`row_onset`, with the keyswitch and the CC16 reset moved ahead of the moved first note), beat weight as a CC11 offset of -22 units on the off-beat eighths (velocity 80-100 does nothing on the row). No per-position leads and no pitch table for the short row (two detectors disagree; below).
5. **Tongued joins (ruling 5).** `gap_floor`: unslurred joins on the sustain rows of monophonic lines get a played gap of 0.09 s on trumpets and tuba, 0.12 s on horns and trombones, 0.068 s on woodwinds, 0.085 s on oboes and cor anglais (at most 50 % / 40 % of the onset distance; slurs read from the score's slur spans and the legato-target flag).
6. **Timpani (ruling 6).** Strokes +4.0 dB against the rolls (roll trims 4.0 dB lower, CC7 fold shift 5.0, `gain_db` -7 -> +2.0). The right-hand keys (+24) are 4 dB louder than the left-hand ones at equal velocity and carry the off-beat strokes: right hand -12 velocity steps (`vel_pitch`), bar position +6 / 0 / -4 / -10 (`TIMP_METRIC_VEL`).
7. **Chorale pedal (ruling 7).** Violoncellos out of the `STR_REP_NEW_BOW` skip from qn 912 (bow changes on the bar lines); `rebow_join`: no gap (5 ms) and a swell of 8 units (at most 9 % of the lane) on celli and basses in 912-936, celli 1088-1104 and three re-bow holes elsewhere; `gap_set`: the brass whole notes of 888-936 take a 0.045 s breath (they had 0.09 s and dipped 4-12 dB on every bar line).
8. **Bar 204 (ruling 8).** `note_end`: the celli's G2 and the basses' G1 end 0.075 s early; `cc_shape`: CC11 -32 units from 0.215 s before the stop to 0.44 s after it. Returns untouched.
9. **Violins 271-272 (ruling 9).** `roles.json`: the c16 stem-fix rows of Violins I / II / Violas start at 1088, not 1080. Tremolo row volumes and a chord CC rule: not done.
10. **Smaller.** Cello / bass pizzicato: the c14 per-pluck dB table as velocity (`vel_db`, 6 and 8 steps per dB from the range fit); muted Trumpet 1: CC1 by pitch on "Mute Sus" (`note_cc`); sfp of bar 149: CC11 ceiling 52-54 until 594.5 on the four upper string tracks (`cc_cap`). Violins I 744 and the class leads of 247-270: not done.

Opus states changed: Double basses only (region gains; rebuilt in full by the `--midi-only` build). Every other track: MIDI, envelope and EQ only. State guard after the final build: 0 stale.

## Range tests under the lock (stems deleted after use; logs in `logs/`)

- T1 (first build; ranges 37:138, 198:266, 354:372, 790:842, 838:870, 886:938, 982:1112, each rendered twice, the first discarded): accents in range on strings and woodwinds, high on Horn 1 and the trumpets; separation up at every changed join except the horns; the basses' short row does not answer to velocity 80-100 and the 0.06 s lead read 14-31 ms early by `c17meas.py cb`; bar 204 16.1 dB / 0.36 s; the chorale's bar-line dips unchanged; pizzicato slope 0.16 / 0.12 dB per velocity step; make-ups fitted (`logs/fit_T1.json`).
- MIC (Double basses Close 1.0 / Main 0.4, bell 0 dB; manual p.138-139, MANUAL-GAPS): rejected. F2 +5.8 dB and F sharp 1 +8.1 dB over the median pitch at p / mf in the 30-125 Hz band (limit 3 dB), stem 5-10 dB hotter. The ff notes of that range did not sound right in this render, so the ff half of the test is missing.
- BELL (built mics, bell -9, F2 region gain +3.5): F2 +2.8 dB at p / mf, level with D2 at ff, the basses' stem in bars 215 / 217 / 228 +1.3 / +1.8 / +1.2 dB: adopted with F2 +2.5.
- T2 (second build): every track within 0.3 dB of c16 over the fitted spans; timpani strokes +3.5 dB; Oboe 1 joins 4.8 dB, Trombone 1 4.4; the basses' beat weight 0.8-1.6 dB with -10 units (final -22); bar 204 15.6 dB / 0.41 s; the chorale dips unchanged, because the 0.12 s floor on the trombones and horns had overridden the 0.045 s breath (fixed in the final build, not range-tested).

## Results (render of 17:06-17:17, no stem fix)

Lock 15:59-17:25 (86 min; after the Scherzo, Movement II and Movement I): start, open, `--midi-only` build (Double basses in full), range rounds T1, MIC / BELL, T2, final build, save, state guard 0 stale, restart, one render with `--force-memory` (REAPER 45 GB, 0.2 GB compressed before; 45 GB, 29 GB compressed after), quit, state guard 0 stale, unlock. Disk: 25 GB free before the render (the range renders took 10 GB); the range stems were deleted and the render ran at 33 GB.

Attack probe: 1 flag, Violoncellos qn 24 (+0.43 s). The stem is the same as c16 there (bars 6-7: -53.2 / -53.2 / -47.6 dB against -52.8 / -53.2 / -47.5), so it is the probe's artefact on the pp entry, as in c12.

| | c16 | c17 |
|---|---|---|
| master integrated / LRA / true peak | -20.5 LUFS / 23.4 / -1.8 dBFS | -20.1 / 23.2 / -1.0 |
| delivered integrated / LRA / TP / limiter / span | -19.8 / 14.8 / -1.5 / 1.2 dB / 19.3 dB | -19.7 / 15.0 / -1.5 / 1.6 dB / 19.6 dB |
| envelope points, all tracks (per second) | 6,172 (15) | 6,005 (14) |
| parts.json fader moves of 2 dB or more within 60 ms strictly inside a sounding note, final fade left out (`stepcheck.py`) | 75 | 0 |
| the same at a note-on / in a rest | 121 / 86 | 89 / 49 |
| notes moving 3 dB or more inside the note (`envstats.py`) | 583 | 405 (44 unmarked) |
| S, 29 lines, outside 25 / 60 ms | 681 / 183 of 1,813 (this cycle's count of c16) | 677 / 169 of 1,818 |

Section loudness against c16 (master, dB): bars 1-10 +1.2, 11-34 +0.1, 83-98 +1.4, 271-272 +1.4 (the violins' 8.9 / 9.5 dB are back), every other section within 0.5. The +1.2 and +1.4 dB of bars 1-10 and 83-98 are make-ups fitted on other spans; left as rendered (a level-only fix would have been a bar-length role).

Accent over the mean of its unaccented neighbours, median, and share under +1 dB (`stepmed.py --accents`, whole movement):

| track | c16 | c17 | under +1 dB c16 -> c17 |
|---|---|---|---|
| Flute 1 / Flute 2 | +1.6 / +1.5 | +4.1 / +3.8 | 49 / 40 % -> 36 / 27 % |
| Oboe 1 / Oboe 2 | -0.6 / -4.4 | +0.6 / -2.5 | 62 / 86 % -> 54 / 71 % |
| Clarinet 1 / 2 | +1.1 / +1.6 | +2.7 / +2.9 | 48 / 30 % -> 24 / 20 % |
| Bassoon 1 / 2, Contrabassoon | +0.1 / -0.2 / +0.6 | +2.2 / +2.4 / +2.9 | 68 / 71 / 50 % -> 48 / 21 / 17 % |
| Horn 1 / 2 / 3 / 4 | +2.5 / +0.8 / -0.9 / +2.5 | +3.6 / +2.8 / +0.6 / +3.9 | 32 / 50 / 72 / 0 % -> 25 / 17 / 56 / 0 % |
| Trumpet 1 / 2 / 3 | +0.5 / -0.4 / +2.9 | +2.2 / +0.7 / +3.8 | 54 / 62 / 30 % -> 46 / 50 / 17 % |
| Trombone 1 / 2, Bass trombone, Tuba | +0.4 / +1.6 / 0.0 / +0.2 | +2.4 / +3.6 / +2.2 / +2.2 | 61 / 33 / 86 / 64 % -> 17 / 11 / 14 / 27 % |
| Violins I / II, Violas, Violoncellos | +0.7 / +0.9 / +1.1 / +2.2 | +2.6 / +2.9 / +2.1 / +3.5 | 58 / 50 / 49 / 36 % -> 20 / 14 / 38 / 26 % |
| Double basses | -1.3 | +0.3 | 81 % -> 62 % |

Front against body (first 80 ms against 0.15-0.35 s) of accented notes is within 1 dB of plain notes on every family, so the accents are weight, not a bright front (the 2-5 kHz jump itself was not measured on this render). Targets: medians in +2 to +4 dB on 19 of 28 tracks (not Flute 1 at +4.1, Oboe 1 / 2, Cor anglais +1.8, Bass clarinet +1.6, Horn 3, Trumpet 2, Double basses); under 15 % below +1 dB met on 4 tracks only (Horn 4, Trombone 2, Bass trombone, Violins II).

Separation at tongued joins (the lower of the two bodies minus the lowest 15 ms frame between; `c17meas.py`), at the joins whose gap changed:

| track (joins) | c16 | c17 | still under 3 dB |
|---|---|---|---|
| Horn 1 (23) | 1.2 dB | 5.6 | 7 |
| Horn 3 (7) | -1.1 | 0.4 | 4 |
| Trumpet 1 (10) | 2.9 | 5.4 | 2 |
| Trombone 1 (22) | 2.3 | 4.5 | 6 |
| Tuba (15) | 2.3 | 6.4 | 0 |
| Bassoon 1 (162) | 1.0 | 2.9 | 82 |
| Oboe 1 (61) | 0.5 | 4.3 | 22 |
| Clarinet 1 (129) | 1.0 | 3.8 | 50 |
| Flute 1 (80) | 2.5 | 5.6 | 28 |

Target 4 dB: met on Horn 1, Trumpet 1, Trombone 1, Tuba, Oboe 1, Flute 1. Nine joins each on Horn 1, Trumpet 1 and Trombone 1 still have a played gap of 30-60 ms (eighths, where the gap is capped at half the slot) and separate by 0.3-1.7 dB.

Double basses:
- Pitch levels, broadband (`pitchlev.py`, f or louder): spread of the pitch medians 12.2 -> 8.8 dB. In the 30-125 Hz band (`c17meas.py cbp`): E flat 2 -7.6 -> -0.1 dB at ff and -7.0 -> -0.5 below; F1 -4.1 -> -2.7 at ff; G1 +4.2 -> +2.2; C sharp 2 +6.1 -> +2.1; A flat 1 +6.0 -> +3.3; F2 +1.1 -> +4.6 at ff (5 notes: 1.6 dB over the 3 dB condition of ruling 4b) and -1.9 -> -0.6 below.
- Bass band (`bassband_c17.txt`): 56-112 Hz share -11.3 -> -11.4 dB; bar 228 (the chorale's F chord) -52.7 (c15) -> -48.3 dBFS; loudest bar 262 -22.5 dBFS, 0.2 dB over the limit.
- Short-row eighths: on-beat strokes 2.0-2.7 dB over the off-beat ones (c16 -0.4 to +1.2). Half-rise against the grid by `c17meas.py cb`: +4 / -15 / -10 / +17 ms in 792-816 / 816-840 / 984-1056 / 1056-1108 (c16 +40 / +20 / +10 / +20); spread unchanged (SD 24-27 ms; 27 / 42 / 101 / 55 strokes outside +20..+70 ms). Critic A's detector read the same c16 strokes 40-55 ms later than this one, so whether the strokes are now on the beat is not settled; the target (under 25 of 79 outside 25 ms) is not shown met.

Timpani (stem RMS over 0.25 s per stroke): on-beat strokes -41.7 -> -37.7 dB (bars 11-34), -41.1 -> -36.2 (199-210), -44.1 -> -40.1 (247-270); off-beat -39.2 -> -38.9, -38.5 -> -37.8, -42.9 -> -39.8. The beat is now 1.2-1.6 dB over the off-beat in two passages (it was 2.5 under) and level in 247-270. Stem +3.4 dB over c16 in bars 11-34 (c16 stood 4.5 under c15 there). The 2-5 kHz share of the first 80 ms is unchanged (-22.7 -> -22.9 dB on the T1 range). Rolls: level carried by CC7, same values as the c16 envelope less the stroke lift.

Stops (drop at +0.3 s / time to -20 dB; limits 14.5-17 dB, 0.50 s; `stops13.py`):

| stop | c16 | c17 |
|---|---|---|
| bar 2 | 15.1 dB / 0.38 s | 17.3 / 0.43 |
| bar 6 | 15.4 / 0.45 | 16.9 / 0.42 |
| bar 94 | 15.1 / 0.36 | 14.9 / 0.40 |
| bar 113 | 16.7 / 0.42 | 15.3 / 0.41 |
| bar 166 | 15.4 / 0.41 | 13.7 / 0.41 |
| bar 204 | 12.6 / 0.54 | 17.4 / 0.38 |
| final chord | 15.5 / 0.39, RT60 1.42 / 1.31 s | 15.1 / 0.39, 1.41 / 1.30 |

Bar 204 is fixed in time and now 0.4 dB past the dry limit (the CC11 fall of 32 units can be 24). Bars 2 and 166 moved out of range by 0.3 and 0.8 dB with no change to their rides: the string and bass levels before those stops changed (strings +2.3 to +3.5 dB in bars 1-10, the basses' region gains). The return rides need a refit.

Chorale pedal, master dip at the bar lines of 229-233 (lowest 20 ms frame in the 0.4 s after the bar line against the 0.26 s before): -6.1 / -6.2 / -6.7 / -5.2 / -4.8 -> -5.5 / -3.2 / -5.5 / -3.2 / -2.6 dB. Target 2 dB not met. On the T2 range the celli and basses still dipped 5-10 dB at their own bow changes with no gap and the swell: the hole is the slow start of the new "Sus MAX" note under a 150 ms release, not the gap (Movement I measured the same).

Pizzicato, peak range per passage: Violoncellos 14.4 -> 8.6 dB (bars 51-66) and 17.2 -> 9.4 (171-186); Double basses 11.6 -> 8.6 and 11.8 -> 11.0. Target 5 dB not met: the c14 table was fitted with other layers present and the velocities run into the floor (8).

Step medians (`logs/render/stepmed_table.log`): muted Trumpet 1 171-186 3.19 -> 2.21 dB; Timpani 199-210 4.99 -> 2.59 and 247-270 2.47 -> 1.75; lines with printed accents rise because the accents now sound (Violins I 11-26 1.32 -> 2.04, 199-210 1.35 -> 2.21, Tuba 27-34 1.50 -> 2.52).

## Rejected, deferred, open (for c18)

- Rejected with numbers: the Close-led bass mic mix; per-round-robin-position leads on the basses' short row (a second detector reads the nine positions of the same stem as 95, 82, 58, 102, 22, 66, 47, 64, 98 ms where A read 75, 111, 76, 112, 103, 82, 93, 118, 102); a pitch table for the short row (B's order of the pitches and this cycle's peak measure disagree); velocity as the short row's beat weight.
- Not met: accents on Oboe 1 / 2, Horn 3, Trumpet 2, Double basses, and the 15 % share; separation on Horn 3, Bassoon 1, Clarinet 1 and the eighth-note joins of bars 91-92 / 277 (short rows or re-tongue rows next); the basses' short-row timing (needs one detector agreed with the critics); F2 at ff +4.6 dB (region gain 2.5 -> 0, or the bell back to -12); the chorale dips; pizzicato evenness (refit the per-pluck table on a range render made in the present state); stops of bars 2, 166 and 204; bars 1-10 and 83-98 1.2-1.4 dB over c16; bar 262 0.2 dB over the low-band limit.
- Not done: ruling 3 for horns, Trombone 1 and Trumpet 1 247-262; ruling 9's tremolo row volumes and chord CC rule (the passage roles 1088-1116 and Violins II 888-936 stay); ruling 10's Violins I 744 and class leads 247-270; the dal niente entries and bars 222 / 245 fronts; re-bow no-split limit 4.5 -> 5.2 s (Movement I); a 2-5 kHz measure of the accents on the full render; the sfp of bar 149 was changed (`cc_cap`) but not measured.
- Slow envelope rows that are levels fitted to older states (Movement I counts these as stopgaps): `roles.json` one-row span levels (792-816, 984-1056 on the four upper string tracks), the c16 stem-fix rows (Violins I / II / Violas 1088-1116, Violins II 888-936, Double basses 792-840 and 984-1080), Trumpet 1's per-bar roles 680-732, the ride rows at 164 and 679.
- Keyswitches 7-12 ms before a note are this pipeline's standard (1,260 of 1,656); ten re-bow keyswitches stand 7.1 ms before their note (the scherzo found 7 ms unsafe). Not changed (`KS_LEAD_S` failed its range test in c13).
- `cycles/c16/render` stems were not deleted: the two delete commands were refused by the permission system. The range stems of this cycle are deleted.
