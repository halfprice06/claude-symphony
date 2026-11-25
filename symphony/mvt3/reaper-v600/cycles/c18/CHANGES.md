# Cycle 18 (2026-11-15): accents halved and moved to the front, the fader guard at 3 dB/s, subito levels in CC11

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c17 render) and the coordinator's rulings 1-12. Snapshot of the tools and data before this cycle: `before/`. Scripts: `actor_scripts/`. Logs: `logs/`.

Dan after c17: "The accents are little bit over done now". Standing rule: the track volume envelope holds slow balance only; no per-note move.

## For Dan

Fixed or better in this render:
- Accents are about half as strong as in c17 and sit at the start of the note instead of swelling for half a second after it. Typical accent: about 1 dB over its neighbours (c17: 2.5 dB). At the big tutti accents the front of the chord stands 1.1 dB over its body (c17: 2.0).
- The sfp of bar 149 now has an sf: its front is level with the ff before it (c17: 1 to 2 dB under), the p after it is 12 dB down, and the strings are back at ff on the downbeat of bar 150 (c17: half a second late). The soft half of this mark and of the fp / sub. p in bars 209 and 219 is now made inside the instruments, not with the fader.
- The fader no longer moves quickly inside held notes: 74 such moves in c17, 4 left (three are 30 ms steps just before a note starts, one is on the harp). 130 of the 267 level rows are gone.
- The introduction: the string figure of bars 3-4 is 2 dB louder and the ff chords 1.3 to 2 dB softer, so the jump between them is back near c16.
- Pizzicato basses are even again (range 4 to 6 dB, c17 9 to 13), and the bassoon solo of bars 115-122 leads by 4 dB again (c17: 0.3).
- Oboes: the weak C5 and the loud E5 / F5 are within 2 dB of the other notes (c17: -4 and +9 to +11). Basses: every pitch within 3.6 dB (c17: +5 / -6.6).
- Bassoons' tongued notes separate more (Bassoon 1 3.6 -> 5.6 dB). The stops of bars 2, 6 and 166 are in range. The timpani's half-bar stroke in bars 247-270 is no longer the weakest. The clarinets' three "dal niente" entries now start 5 to 7 dB under their level.

Still wrong (left audible, as the rule asks):
- The chorale's bar lines (bars 225-233) still dip 2.3 to 5 dB: unchanged. The dips are the woodwinds and brass starting each new whole note (oboes -8 to -12 dB, clarinet -6), not the pedal: spreading the breaths and tying the pedal over two bars did not change the sum.
- Bar 222's downbeat still has a 3.6 dB hole (c17: 5.3).
- Pizzicato celli are still uneven (7 to 12 dB): the same pitch differs by 5 dB between its round-robin samples.
- Muted Trumpet 1, bar 182: the first quarter is 5 dB over the line. Its fader row was deleted as ruled and the replacement CC1 values are too high there.
- Horn 3 is still the loudest stem in bars 27-34 (-0.6 dB only): the switch that should have removed its +3.5 dB did not act.
- The stop of bar 204 now drops 19.2 dB in 0.3 s (limit 17).
- Accent medians are under the +1.5 dB target on several tracks (oboes, Horn 3, trombones, bass clarinet, basses: 0 to +1), and a tenth to a quarter of the accents still stand 5 dB out, from sample level by pitch, not from the bump.


## Tools (generic; values in `build/score_config.py`, block "mvt3 c18")

- `tools/instr_post.py`:
  - `accent`: `tutti_scale` [(staves, factor)] (the number of staves that print an accent on the onset; `score_to_parts.py` passes the count), `max_step` (the bumped value at most N units over the note before on the same row), and the bump is back before the note ends.
  - `note_cc` `add` (one offset over a span), `cc_shape` `from_note` (seconds from the moved note-on), `cc_scale` (a passage level in dB as a factor on a lane: `10^(dB / k)`; exact on brass and clarinets, where CC11 is the volume at 40 log10), `note_merge` (a printed note tied to the same-pitch note before it), `onset_lead` (listed notes start earlier, keep their end; a same-pitch note before them is shortened), `note_end` `pitch`, `gap_floor` `skip_long`, `vel_cap`.
  - `vol_guard`: `hairpin_ok` (a move under a printed hairpin is printed), `max_iter`, `rate_short_db_s` / `short_s` (a ramp that must cross running notes before a note-on may be fast; over a held note it runs at `rate_db_s`), `skip`.
- `tools/score_to_parts.py`: `HP_REL_MAX_DB_S` (the release of a hairpin's dB gain is no faster than this).
- `tools/build_reaper.py`: mix.json `region_gain_db` may be a list of specs (different rows, different tables).
- `actor_scripts/data18.py --write` writes `build/roles.json` and `build/mix.json` from `before/`. `guard18.py` (the new guard, on the envelope that `build_reaper.py` writes), `envdiff18.py` (written envelope of two builds per track and bar), `meas18.py` (the targets below, on a full render or one range folder).

## What changed, by ruling

1. **Accents.** Bump amounts about half of c17: strings +8 at f / +10 at ff (Violins I and Violoncellos +7 at f), woodwinds +7 / +10 (flutes +6 / +8), brass and clarinets 10 % of the resting CC11 (Horn 1 8 %, trumpets and tuba 6 %, Trumpet 3 5 %), CC1 part +2 (horns and clarinets +3; none on trumpets, tuba, Trombone 2 and Bass trombone). Shape: from 0.03 s before the moved note-on, held 0.06 s, back by 0.22 s (c17: 0.15 s / 0.45 s). The scale for doubled beats (0.75 / 0.6) was built and then taken out before the render on the coordinator's later note (Movement I c59: a scale only makes tutti accents weaker than solo ones); the key `tutti_scale` stays in the tool. Step cap 12 units against the note before on the same row. Resting values and make-ups unchanged. Nothing was raised on the oboes, Horn 3, Trumpet 2 or the basses.
2. **Fader.** (a) `HP_REL_MAX_DB_S` 2.8: a hairpin's dB gain is given back at 2.8 dB/s at most (it was 2-4 dB over one quarter, on the held arrival note). (b) `vol_guard` now acts on every unprinted move of 1.5 dB or more steeper than 3 dB/s inside a sounding note (c17: 2 dB within 60 ms): into the rest before the note, or a ramp of 2.8 dB/s. (c) `roles.json` 267 -> 137 rows: deleted the sfp / fp / sub. p rows (593-596, 833.25-839, 871.7-878, 872-880; 36 rows, now CC11: item 3), Trumpet 1's eight per-bar rows 680-732 (one row [680, 732, +2]; the printed diminuendo to 728 is a CC1 ceiling, G4 / A flat 4 +4 units in the pitch table), Horns 3 / 4 [548, 552] (CC11), the 79 "+3 dB" tutti rows of Bass trombone, Tuba, Contrabassoon, Bassoon 2, Double basses and Bass clarinet (`dyn_trim_db` ff +3, Bass clarinet +2, Double basses +2; f +1.4 to +2 on Bass trombone, Tuba and Double basses, whose rows also covered f passages), Double basses [792, 840, -4] and [984, 1080, -2] (`row_volume_db` "Stac On Bow RRx9" -1.5, one row [820, 840, -4] kept), and five passage levels whose edge fell on a held note with no rest (Violins I 168-200 -8, Flute 1 304-320 -7 / 952-964 -3 / 1012-1016 -4, Horn 1 264-300 +4: `cc_scale` on CC11). (d) Horn 3's held unison level over 105-136 is off (`VOL_RULE_OFF`). Not moved: the one-row span levels of the four upper string tracks (40-104, 600-680, 792-816, 984-1056), the tremolo / chord rows (Violins I / II / Violas 1088-1116, Violins II 888-936; left for c19 with the chord CC rule), and the phrase decisions.
3. **sfp of bar 149, fp 209, sub. p 219.** The sf: the fall starts 0.22 s after the mark (`SFP_SPIKE_S` (0.22, 0.42); 0.10 s on the range test left the front 2 dB under the ff before) and CC11 +10 units from 0.03 s before the moved note-on, back by 0.32 s, on all 25 sfp staves (brass and clarinets CC1 +4 as well). The strings' ceiling now reaches 105 at qn 596 (c17: 106 at 597.5), and the same ceiling shape holds the p of the woodwinds and brass (floors 40-50 by track; brass and clarinets on CC1 too) in place of the fader rows. The fp of 209 and the sub. p of 219 are `cc_scale` shapes of the same depth as the old rows.
4. **Chorale and bar 222.** Whole-note breaths spread per player (woodwinds 0.035-0.077 s, brass 0.045-0.085 s; the woodwind gap floor no longer applies to these notes). The pedal C is two-bar notes: celli change bow at 916, 924, 932, basses at 920, 928 (`note_merge`), with c17's 5 ms join and 8-unit swell, now held 0.30 s and back over 0.55 s. Bar 222 (qn 884): Violins I / II and Violas start 0.12 s before the bar line, Trumpet 1 and Horn 1 0.15 s (CC1 +10 over the first 0.35 s); Violins II and Violas hold their bar-221 notes 0.12 s across (not the viola F4 that is struck again); Violoncellos CC11 +12 over the first 0.35 s of their D3.
5. **Pizzicato.** The per-pluck velocity table is deleted (velocity 41 everywhere again, ceiling 47 celli / 52 basses); per-pitch region volumes on the Pizz rows, fitted on the c16 stems (flat velocity; `logs/pizz_pitch_c16.json`): celli G2 -6.0, A flat 2 -4.6, F sharp 2 -3.6, G3 -4.7, C3 +5.8, B flat 2 +3.0, E flat 2 +2.7; basses E flat 2 -3.9, G2 +2.3, G1 +2.0.
6. **Double basses.** Region volumes on the sustain / legato rows: E flat 2 +8 -> +5, F2 +2.5 -> +1.0, A flat 1 -3 -> -4.5, C sharp 2 -2.5 -> -4, F1 +3.5 -> +5, G1 -2 -> -3.5, A flat 2 / B flat 2 +3, C3-G3 +6. Bell unchanged (-9). No lead change on the short row.
7. **Row and region levels.** Oboes: region volumes on "Sus MAX" (C5 +6, D5 +4.5, E flat 5 +2, E5 -5, F5 -7) and "Leg Slur MAX" (C5 +3, D5 +1.5, E5 -3.5, F5 -4). Legato rows against sustain rows by CC11 offsets at f / ff: Trumpet 1 legato -6 / -9, sustain +5 / +8; Trumpet 2 -5 / -7, +5 / +7; Horn 1 -5 / -7, +4 / +6; Oboe 1 legato -5 / -8; Oboe 2 -8 / -12; Violoncellos legato +10 -> +4 at ff; Violas legato +10 -> +16 and sustain -2 -> -6 at ff.
8. **Timpani.** Right-hand keys -12 -> -24 velocity steps (floor 40); bar position "beat" -4 -> +2, "off" -10 -> -8.
9. **Introduction.** CC11 +5 on the f figure of bars 3-4 (four upper string tracks), -3 / -2 / -1 / -4 on the ff chords of bars 1-2 / 5-6 (Violins I / II, Violas, Violoncellos). C's values (+7; -10 / -10 / -4 / -14) were range-tested first: the chords fell 7 to 11 dB.
10. **Stops.** Bar 166: return ride 3.0 -> 0 dB. Bar 204: CC11 fall 32 -> 24 units. Bar 2 untouched.
11. **Joins.** Bassoon 1 / 2 and Contrabassoon gap floor 0.068 -> 0.095 s.
12. **dal niente.** Clarinet 2 at 184 and 680, Clarinet 1 at 200: CC11 from -18 units at the note-on to the lane's value over 1.2 s.

Opus states changed (rebuilt in full by the `--midi-only` build): Double basses, Violoncellos, Oboe 1, Oboe 2.

## Range test under the lock (I1, ranges -1:24, 534:602, 838:940, 454:490, rendered twice, the first discarded; stems deleted)

- Introduction with C's values: figure +4 dB, chords -7 dB (Violins I) and -11 dB (Violins II), master chord -2 dB. "Sus MAX" loses about 0.7 dB per CC11 unit under 100 and nothing above about 103. Values reduced (item 9).
- sfp with a 0.10 s attack: front 2.0 dB under the ff before (c17 3.1 under). Attack lengthened to 0.22 s (item 3).
- Bar 222: hole 4.8 -> 3.7 dB; the celli's stem fell 10.5 dB for 0.3 s at their bow-change legato. CC11 lift added.
- Chorale bar lines: unchanged against c17 (916: -5.2 against -5.3). Per stem at 916: Oboe 2 -11.6, Oboe 1 -7.5, Clarinet 1 -6.2, Violoncellos -5.6 dB. Left.
- Bassoon solo 456-488: lead +4.1 dB, basses' stem -58.8 dB (c17 -50.3).

## Results (render of 19:42-19:55, no stem fix)

Lock 18:57-20:01 (64 min; after the Scherzo, Movement I and Movement II; waited from 15:15): start, open, `--midi-only` build (4 full rebuilds), range round I1, final `--midi-only` build, save, state guard 0 stale, restart, one render with `--force-memory` (REAPER 45 GB, 0 GB compressed before; 45 GB, 29 GB compressed after), quit, state guard 0 stale, unlock. Disk: 25 GB free at the lock; the c16 and c17 stems were deleted (masters and mp3s kept; the c17 comparison numbers were saved first, `logs/render/c17_*`), 36 GB at the render.

Attack probe: 0 flags.

| | c16 | c17 | c18 |
|---|---|---|---|
| master integrated / LRA / true peak | -20.5 LUFS / 23.4 / -1.8 dBFS | -20.1 / 23.2 / -1.0 | -20.2 / 23.3 / -1.4 |
| delivered integrated / LRA / TP / limiter / span | -19.8 / 14.8 / -1.5 / 1.2 dB / 19.3 dB | -19.7 / 15.0 / -1.5 / 1.6 / 19.6 | -19.8 / 15.1 / -1.4 / 1.5 / 19.6 |
| role rows | | 267 | 137 |
| unprinted fader moves of 1.5 dB or more steeper than 3 dB/s strictly inside a sounding note (`guard18.py`, on the written envelope) | | 74 | 4 |
| the same across a note edge / in a rest / printed (under a hairpin, after fp / sfp) | | 328 / 224 / 503 | 212 / 212 / 460 |
| envelope points per second, strings (written envelope) | | 0.62-0.78 | 0.62-0.78 |
| S, 29 lines, outside 25 / 60 ms | | 677 / 169 of 1,818 | 661 / 177 of 1,817 |

The 4 moves left: three steps of the dynamic trim that stand 0.03 s before a note-on while the note before still sounds (Clarinet 1 135.8, Violas 823.5, Violoncellos 951.5), and Harp 952 (-3.5 dB in 0.12 s under ringing notes). Detector for this count: `guard18.py` docstring.

Accents (`meas18.py`: first 0.3 s of the accented note against the unaccented neighbours within 3 notes at the same printed dynamic; "isolated" = no other accent within 2 notes):

| family | c16 median (over +5 dB) | c17 | c18 | c18 isolated |
|---|---|---|---|---|
| woodwinds | +0.4 (16 %) | +2.4 (27 %) | +1.0 (16 %) | +0.8 (17 %) |
| brass | +1.0 (7 %) | +2.3 (19 %) | +1.3 (14 %) | +0.8 (7 %) |
| strings | +0.6 (9 %) | +2.8 (22 %) | +1.3 (11 %) | +0.5 (3 %) |

Per track, c17 -> c18 median: Flute 1 / 2 +3.0 / +3.8 -> +1.7 / +2.2; Oboe 1 / 2 +0.7 / -3.2 -> +0.5 / 0.0; Clarinet 1 / 2 +2.0 / +3.1 -> +0.8 / +2.0; Bassoon 1 / 2, Contrabassoon +2.5 / +2.1 / +2.3 -> +1.2 / +0.7 / +0.4; Horn 1-4 +3.4 / +2.7 / +1.0 / +4.0 -> +2.0 / +1.2 / -0.3 / +2.7; Trumpet 1-3 +1.9 / +1.9 / +4.1 -> +1.2 / +1.2 / +3.1; Trombone 1 / 2, Bass trombone, Tuba +1.9 / +2.3 / +2.4 / +2.5 -> +0.9 / +1.4 / +0.5 / +0.6; Violins I / II, Violas, Violoncellos +2.3 / +2.8 / +3.0 / +3.6 -> +1.0 / +1.2 / +2.2 / +2.1; Double basses -0.2 -> -0.1. Targets: no track median over +3 except Trumpet 3 (+3.1; +3.7 in c16 with no bump); medians of +1.5 to +2 met on 6 tracks, under it on the rest; share over +5 dB under 8 % not met (11-16 %; c16 itself 7-16 %). Master front at accents (first 0.2 s minus 0.45-0.65 s later): 16 or more staves +0.6 (c16) / +2.0 (c17) / +1.1 (c18; target 1.2), 9-15 staves -0.2 / +1.2 / +0.6. Bars 91-94, accent window over the surrounding 3 s: 3.8, 2.5, 1.6, 1.7, 1.5, 2.2, 2.0 (c17 4.0, 2.7, 1.9, 1.9, 1.8, 2.4, 2.2; c16 3.6, 2.3, 1.7, 1.4, 1.4, 1.8, 1.6): the first is over the +3 target in all three renders.

sfp of bar 149 (master, 0.1 s frames from qn 592; before = -17.9 dBFS): c17 -21.0, -21.0, -18.7, then floor -30.1; c18 -19.9, -18.7, -17.5, floor -29.7 (11.8 dB under the ff), -16.0 at qn 596 (c17 -17.3). Stems at 596: Violins I -29.4 (c17 -35.0), Violas -31.5 (-36.9). Brass p 0.5-0.9 s after the mark: Horn 1 -49.5 (c17 -44.6), Trombone 1 -49.9 (-38.9).

Chorale bar lines 896-932 (master, lowest 30 ms frame in [-0.25, +0.2] s against the 0.3 s before): c17 -1.5, +0.5, -3.8, -4.6, -2.6, -5.3, -3.0, -3.8, -3.1, -1.8; c18 -2.6, -0.3, -3.7, -4.6, -2.3, -5.0, -3.8, -4.4, -3.9, -2.7. Target 2 dB not met. Bar 222: lowest 50 ms frame 3.6 dB under the mean of 883-884 (c17 4.8; c16 the same as c17); target 3 not met.

Pizzicato peak range (200-264 / 456-488 / 680-744): Violoncellos 12.5 / 6.2 / 9.5 -> 11.8 / 7.3 / 11.0 dB; Double basses 8.9 / 13.4 / 11.5 -> 3.7 / 6.4 / 5.8. Bassoon solo 456-488: lead over the sum of the other dry stems +0.3 -> +4.1 dB; basses' stem -50.3 -> -58.8 dB.

Pitch levels on the sustain row at f or louder (note body against the track median): Oboe 1 C5 -4.0 -> -0.2, E5 +8.8 -> +1.8, F5 +10.6 -> +1.6; Oboe 2 F5 +9.3 -> +1.4, C5 -2.2 -> +0.6, A4 -10.0 -> -10.8 (not in the table); Double basses G1 +4.4 -> +0.7, A flat 1 +5.0 -> +2.4, E flat 2 +2.6 -> -1.3, F2 -2.7 -> -3.6, A flat 2 -6.6 -> -3.5, B flat 2 -5.7 -> -3.0, C sharp 3 -6.1 -> -3.2 (broadband; spread 11.6 -> 6.7 dB).

Introduction (my per-bar RMS; bars 1 / 2 / 3): c16 -21.3 / -28.2 / -36.7, c17 -20.2 / -26.0 / -38.9, c18 -21.0 / -27.7 / -37.3; bar 1 to bar 3 15.4 / 18.7 / 16.3 dB. Violins I chords -34.8 / -31.5 / -32.8, figure -39.2 / -42.5 / -40.6.

Stops (drop at +0.3 s / time to -20 dB; `stops13.py`: 20 ms RMS, reference the 0.16 s before the release): bar 2 17.3 / 0.43 -> 15.4 / 0.46; bar 6 16.9 -> 15.2; bar 94 14.9 -> 15.8; bar 113 15.3 -> 15.0; bar 166 13.7 -> 15.7; bar 204 17.4 / 0.38 -> 19.2 / 0.31 (out of range: the basses' ff level before the stop rose with the +2 dB trim); final chord 15.1 / 0.39 unchanged.

Tongued joins at 60-100 ms played gap (`c17meas.py sep`): Bassoon 1 3.6 -> 5.6 dB (under 3 dB 72 -> 36 of 156), Bassoon 2 3.1 -> 4.6, Contrabassoon 3.8 -> 6.8.

Timpani 247-270 by bar position (stroke RMS 0.25 s, velocity): downbeat -39.6 (100), eighth before beat 2 -39.7 (85), beat 2 -40.2 (99), last eighth -42.0 (62); critic A on c17: downbeat -36.6, beat 2 -40.9. The half-bar stroke is 0.6 dB under the downbeat and over the last eighth.

dal niente (first 0.2 s against 1.5-2.5 s): Clarinet 2 at 184 -0.9 -> -6.5 dB, Clarinet 1 at 200 +0.9 -> -4.7, Clarinet 2 at 680 -1.5 -> -7.1 (target 8).

Bars whose master level moved 1.5 dB or more against c17 (`barcmp18.py`): 7 (3 up, 4 down). Bars 2 and 6 -1.7 (string chords), bar 3 +1.6 (the figure), bar 97 +1.8 (Oboe 1 region gains, +3.0), bars 120 and 122 -4.0 / -5.0 (bass plucks back to c16's level, -16 dB), bar 182 +1.9 (muted Trumpet 1 +7.6 without its -6.5 dB row). Section levels per stem (`logs/render/lev.log` against `c17_lev.log`) are within 1 dB except Oboe 1 (-2 to -4 dB in 984-1112, its F5).

## Rejected, deferred, open (for c19)

- Not met: chorale bar-line dips; bar 222 (3.6 dB); celli pizzicato (round-robin spread of one pitch about 5 dB: a region gain cannot fix it; try CC16 resets per passage or velocity by round-robin position); accent medians under +1.5 dB on most tracks and the share over +5 dB (sample level by pitch: region gains per track are the next step, as on the oboes and basses); bar 204's stop (19.2 dB: lower the basses' ff before it or restore part of the old fall); dal niente 5-7 dB (target 8).
- Faults made by this cycle: muted Trumpet 1 bar 182 first quarter +5 dB over the line (CC1 ceiling at 724.0-725.0 should be about 52, not 58; the +4 units on G4 / A flat 4 should go); Horn 3 in bars 27-34 unchanged (-33.8 dB, c17 -33.2): `VOL_RULE_OFF` "uni_boost" [(103, 137)] did not remove its +3.5 dB (find the rule that writes it: `vol_parts.rule` tags).
- Not done: the calibration range of the basses' short rows (two threads were waiting for the lock); re-tongue rows (LegRep, Stac DblTng) for the eighths of 91-92 and 277; tremolo row volumes and the chord CC rule (rows 1088-1116 and Violins II 888-936 stay); class leads 247-270; the one-row span rows of the upper strings; the ten re-bow keyswitches at 7 ms; a longer no-split limit (5.0-5.6 s, Movement II c57).
- Rejected with numbers: C's introduction values (range test above); the staff-count accent scale (not rendered; coordinator's note).
- Row volume: Movement II measured no effect of the Opus row volume knob on a range pass. Here `row_volume_db` "Stac On Bow RRx9" -1.5 was not checked separately; compare the basses' eighths in c19 and move the value to region volumes if it did nothing.
- Notes relayed for c19: Horn 1 G sharp 4 and B flat 4 are in anti-phase between L and R in the 1FH Main pair (mono sum loses 5-11 dB); upper-woodwind stems fall 28-41 dB within 0.2 s of a note end; cap a legato lead against the previous note's moved note-on; keep soft-entry shapes to score onset + 0.15 s; gains per dynamic layer in region tables.

