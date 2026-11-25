# Cycle 14 changes (actor)

Snapshot of the c13 tools and build/*.json: `before/`. Scratch and analysis: `/private/tmp/claude-501/mockup-loop/c14-actor/` (`pdiff.py` diffs two parts.json files per track; `chk.py`, `sec.py` and `cC/hp3.py` (critic C's hairpin fit pointed at any cycle) measure the findings; `fix.py` is the post-render stem fix; `orig/` holds the render's own stems, master, mp3 and metrics before that fix).

## Process

1. Edited `tools/score_to_parts.py` and `build/{roles,note_trims,pitch_trims,early_fills}.json`, regenerated parts.json and diffed it against `before/build/parts.json`. No Opus state changed (the Trombone KS Master already loads the Marc Lng row), so `build_reaper.py --midi-only` updated all 29 tracks in place.
2. Saved, quit and reopened REAPER (`open -a REAPER --args -new`, project opened by a bridge job): 17 GB at open, 56 GB loaded, 0 GB compressed.
3. One render (`render_cycle.py 14`). Attack gate 18 of 19. The one failure is the known marginal Violoncellos qn 212 tremolo probe: 7.0 dB against a limit of 6 (c12 and c13 6.6). The new sostenuto hold ramps the celli 2.5 dB up into qn 212 and back to 0 at the moved onset, so the frame before the tremolo is higher. Not re-rendered.
4. After the render, two fixes went into the stems, and the master was rebuilt as the stem sum. Before the fixes the stems summed to the master within -121.6 dBFS. measure.py, the probe and deliver_master.py were then run again.
   - Trombone 1: level only, exact. The Marc Lng bodies were 2-3 dB under c13. I added `MARC_BODY_DB` 2 + `MARC_ATTACK_DB` 2 (see A #1) and applied the new-minus-rendered volume envelope to the stem (linear in dB between breakpoints, max +3.8 dB).
   - Violas, bar 59: the A #3 test failed (below), so it is reverted in the tools. I replaced the stem's qn 195.4-202.08 with the c13 Violas stem, using 30 ms equal-power crossfades. c13 rendered the same MIDI, CC and volume data as the reverted build in that window, so this is a valid render of the reverted data, but not sample-identical: two renders of the same viola data differ by about -10 dB relative, from round robins.
   - REAPER was updated to match (`--midi-only "Trombone 1" "Violas"`) and saved.

## Accepted

**A #1: Trombone 1 marcato line** (`MARCATO_SPANS` {Trombone 1: [(212.5, 219)]})
- The six unaccented notes of 1 qn or less (214.5-217.5) play `Marc Lng RRx4` (1TB KS Master key 29) at 0.75 x their written length.
- Their velocities fall v106, 104, 102, 100, 96, 94 (`VEL_SET`). The c06 note trims (-1 to -2.5 dB, ramped in over each note) are removed.
- The accented notes of 1 qn or more (213, 218) end 0.1 qn early. The `ACCENT_DB_AT` shapes are unchanged.
- After the render: each Marc Lng note gets +2 dB over its length plus +2 dB on its attack (10 ms rise, held 0.08 qn, gone by 0.25 qn).

**A #2: timpani rolls tied into a stroke** (`TIMP_TIE_STROKES` [203, 211])
- The roll ends at the tied note + 0.03 qn, and a Timpani Flt Lng stroke starts on the tied note: v96 at f (qn 203), v110 at ff (qn 211).
- The stroke's CC7 is the roll level + 4 dB on the 40 log scale.
- It gets half of `TIMP_LOUD_ATTACK_DB` (3 dB), because it already sits on the roll's hairpin gain (+5 dB). Without that cut, the plan put +11 dB on the 203 attack.
- The pp/ppp tied ends (qn 8, 237) stay rolls.

**B #1 + C #3: soft solos up**
- roles.json: Horn 1 [16.5, 42, 2.5], [226, 238, 2] and the crest [33.5, 38.5, 1.5, 1.0]. These are B's horn values; C's +2 was not added on top.
- Oboe 1 [42, 48, 2], [54, 60, 2]; Violin I solo [48, 65, 2]; Bass clarinet [90, 108, 2]; Cor anglais [124, 137, 2], [151, 171, 2].
- `"_all"` [283.5, 304, -2] for the coda.

**B #2:** note_trims Violoncellos 72 -3, 74 +4, 244 -3, 246 +4.

**B #3:** note_trims Oboe 1 42: 5 -> 6, not 8, because C's +2 role now covers the same note. roles Violins II [42, 44.5, -2].

**B #4:** pitch_trims Clarinet 2 B flat 4 (70) -3; Clarinet 1 70 -3, added to `_all_arts_pitches`.

**B #5:** roles Violins I [292, 304, -6] -> -4. With the `_all` -2, the net is unchanged for Vln I and -2 for Vln II.

**C #1: soft hairpins in lead lines** (`LEAD_SPANS`, `HP_GAIN_SOFT_DB` 3, `HP_SOFT_DEC_DB` 2)
- Applies to hairpins in the listed lead spans that start at CC11 66 or lower and have no hpgain of their own.
- A crescendo ramps +3 dB. In a messa di voce (a decrescendo starting within 0.3 qn of the crescendo's end), the gain is held to the decrescendo and released linearly across it. Otherwise it is held to the next onset and released over 1 qn.
- A lone decrescendo ramps to -2 dB.
- These items are added after the hpgain chaining, so they never chain.

**C #2 (a-d):**
- Horn 1: note_trims 32 +2.5; pitch_trims 60 (C4) -2.
- Bass clarinet: early fill at 93 deleted; note trim 93 -6 -> -4.
- Violins I: fill 67.5 deleted, new fill 68 {db 3, pre_s 0.05, hold_s 0.35}, pitch trim 72 (C5) -2. A new pitch_trims key `_skip_onsets` [0, 292] keeps the trim off the opening chord and the final chord, where it would have undone B #5.
- Violin I solo: note trims 48.5 -2, 53 -3.

**C #4: sostenuto hold** (`SOSTENUTO_SPANS` notes, `SOST_SUSTAIN_DB` 2.5)
- Long notes in bars 61-62 that are not phrase ends get the contour "swell_sost": the CC11 swell holds +4 after 40% instead of falling to -2.
- Their swell_db is replaced by a volume ramp: 0 at 40% of the note, +2.5 dB at 0.25 qn before the next moved onset, 0 at that onset.

## Rejected or deferred

- **A #3 (viola sextuplets of bar 59 on Leg Slur MAX, v127, no lead, 0.02 qn overlap): tried and reverted.** `FAST_LEG` is now empty.
  - Own-pitch dominance in bar 59 fell from 0.33 (c13) to 0.03. The legato voice held one pitch per group, and only one note in two reached its pitch.
  - Bar 60 (the Sus MAX control) measured 0.29.
  - The delivered stem carries c13's bar 59 (Process 4). The item is closed: Leg Slur MAX does not play this figure. A fast-legato or run patch is the remaining option.
- **A #4 (a2 horn track):** deferred. It needs a 30th Opus instance and its gain set from a render.
- **C #5 (pitch-following note shaping):** deferred until findings 1-2 have been heard, as C asked.
- **C #2c pitch trim at the opening and final chords:** excluded (see `_skip_onsets`).

## Measured, c13 -> c14 (plain RMS on stems unless noted)

**Delivery** (after the stem fix)

| | c13 | c14 |
|---|---|---|
| Master integrated | -23.3 LUFS | -23.8 LUFS |
| Master LRA | 23.9 LU | 23.5 LU |
| Master true peak | -3.6 dBFS | -4.5 dBFS |
| mp3 integrated | -19.8 LUFS | -19.8 LUFS |
| mp3 LRA | 15.8 LU | 16.0 LU |
| mp3 true peak | -1.6 dBTP | -1.7 dBTP |
| mp3 span (p10 to max) | 18.2 dB | 18.2 dB |
| Limiter | 3.2 dB | 2.0 dB |

**mp3 section loudness** (LUFS, energy mean of momentary loudness, `sec.py`)

| | c13 | c14 |
|---|---|---|
| Intro, bars 1-6 | -26.3 | -26.4 |
| Horn solo, bars 7-14 | -25.2 | -23.6 |
| Oboe and solo violin, bars 15-22 | -25.3 | -24.2 |
| Horn solo, bars 67-70 | -25.5 | -24.0 |
| Coda ppp, bars 83-85 | -29.1 | -28.8 |
| Coda pp, bars 86-91 | -25.0 | -26.1 |

- The intro sits 2.8 LU under the first horn solo (c12 target 1.5-2.5).
- The pp coda sits 2.5 LU under the first horn solo (target about 2).

**Findings**

- **A #1, Trombone 1** (10 ms frames, `c14-A/tbn.py`):
  - Bodies -26..-29 dB (c13 -25..-29).
  - Every note now has a break before the next: dips to -35..-37 before 215.5 and 216, and to -49 before 217.
  - The Marc Lng attacks still rise over about 0.1 s with no peak over the body. The marcato reads as separation, not as attack weight.
- **A #2, timpani:**
  - At qn 203 the stroke peaks at -27.9 dB against the roll's -34.3: +6.4 dB within 0.1 s, then a decay. The roll then stops (c13 had no event).
  - At qn 211: +3 dB, falling into the caesura.
  - The ff roll at 204 (-29) is still louder than the 203 stroke's body.
- **B #1, horn over its summed accompaniment, median per beat:**
  - Bars 7-14: +0.2 -> +3.8 dB (minimum -5.6 -> -2.6).
  - Bars 67-70: +0.8 -> +2.6.
  - Per bar, bar 12 (-34.2) is now level with bar 8 (-34.8); in c13 it was 0.7 dB under.
  - Per beat, the crest (qn 34-35, -37.3) is still 2.4 dB under the bar 8 swell (qn 22, -34.9), because the soft hairpin gain also lifted that swell.
- **C #2a:** the Horn F4 body at qn 32.5-34 rose from -45.6/-44.3 to -35.9/-34.5. There is no more drop under the crescendo.
- **B #2, Vc:** qn 72/74/75 -39.1/-47.3/-43.1 -> -41.6/-43.3/-42.9. qn 244/246/247 -37.8/-46.1/-42.0 -> -40.4/-42.3/-41.7. The largest step went from 8.2 to 1.9 dB.
- **B #3:** Oboe 1 minus Violins II at qn 42-44.5, per half beat: -3.2..-1.4 -> +1.9..+6.3 dB.
- **B #4:**
  - Cl1 minus Hn1 at qn 178: +1.7 -> 0.0.
  - Cl2 minus Cl1 at qn 190: +4.1 -> +1.1. At qn 196: +2.3 -> -1.2.
- **B #5:** Vln I minus Vln II at qn 297-303, per beat: median -1.6 -> +0.75 (range -0.3..+2.2).
- **C #1, lead-line hairpins** (`cC/hp3.py`):
  - The 22 lead crescendos have a median of +5.3 dB (c13 +1.7). The decrescendo median is -4.8 (c13 -3.9).
  - These turned the right way: Vln I solo 48-51 (-2.4 -> +0.3), Vln I 70-72 (+1.2 -> -1.4), Ob1 57-59 (+0.6 -> -3.8), BCl 93-96 (-1.5 -> +6.0), BCl 102-105 (0 -> -1.2), Vln I 240-242 (+1.0 -> +4.0).
  - Better but still flat or wrong: Fl1 126-128 cresc (-2.7 -> -0.7) and Vln II 242-244 decresc (+4.5 -> +0.8).
  - Still wrong: Vln I 68-70 (-1.8) and Ob1 148-151 (-0.2).
- **C #2b:** BCl qn 93: the 0.4 s attack plateau is gone (-33.2 peak -> -35.1). The phrase climbs to -32.2 at qn 96.
- **C #2c:** Vln I pickup qn 67.5-67.75 -38.6/-34.7 -> -44.2/-40.1. The Eb5 top at qn 68-68.5 is -38.9/-37.6, now over the pickup (c13 -41.0/-40.2).
- **C #2d, solo violin:** 48.5 -43.6 -> -41.4; 51 -46.9 -> -42.1; 53 -43.0 -> -42.0. The crescendo top is now level with the end of the phrase, but not over it.
- **C #4, master per 0.25 qn in bars 61-62:**
  - The dip before qn 207.5 went from -21.8 to -18.7 dB.
  - qn 209.25-209.5 went from -21.4/-21.6 to -20.3/-19.8.
  - qn 205.5-206 is unchanged at about -20.0.
  - Bar 61 is -17.7 dB (c13 -18.0) and bar 62 is -19.2 (-19.0).
  - Bar 61 is still the loudest bar, 2.4 dB over bar 79.

## Open
- The horn solo's mp crest (qn 34-35) is still under the bar 8 swell, per beat.
- Tbn1 marcato attacks have no peak. Next: try `Marc Shrt RRx4` with a longer note, or a +3-4 dB attack bump at onset + 0.05 s.
- Vln I 68-70 crescendo is still falling (the C5 trim and fill changes moved the pickup, not the crescendo body). Ob1 148-151 decrescendo is flat.
- C #5 note-to-note shaping.
- The true-stereo hall IR (c13 C #2) is still deferred.
