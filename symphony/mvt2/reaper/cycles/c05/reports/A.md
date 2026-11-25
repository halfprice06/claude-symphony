# Cycle 5, critic A: articulation and phrasing (on the cycle 4 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c05-A/` and run with `~/.venvs/claude-composes-reaper/bin/python`:
- `lib.py`: tempo map, bar numbers, stem envelopes.
- `fine.py q0 q1 step "Track,Track" [cycle]`: stem levels on a qn grid.
- `arts.py`, `ksfirst.py`: the articulation in force at each note, and the first note after each keyswitch.
- `entries2.py`, `cmp34.py`: delay to sound start for every entry after a rest, compared between c03 and c04.
- `probe.py <render dir> [parts.json]`: a pass/fail attack-timing probe (finding 1).
- `cc1groups.py <oib> <group>`: start conditions and controllers of an Opus patch's sample groups.

In this report, "sound start" means the first 10 ms frame after the score onset (`sq`) that reaches the higher of (peak over the next 1.5 s minus 20 dB) and (level just before plus 6 dB). For a pizzicato or a tremolo, anything later than about 0.06 s is engine lateness, not a slow bow.

Before c03 and c04 are compared at qn 204 or later, c03 must be converted with its own tempo map (`cycles/c04/before/parts.json`), because c04 added the caesuras. Before qn 203.75 the two tempo maps are identical.

## 1. String attacks are late in c04 even where the MIDI is identical to c03: the timing problem is in the render, not in parts.json

**Measured.** Three renders of the same notes give three different results.

Cello pizzicato, bars 37-39 (qn 108-116): notes, keyswitches and CC11 are byte-identical in c03 and c04, and no CC1 point falls in the window.

| Attack | c03 | c04 pass1 (before the freeze) | c04 final |
|---|---|---|---|
| Vc pizz. qn 108 | 0.00 s | 0.13 s | 0.45 s |
| Vc pizz. qn 112 | 0.01 | 0.10 | 0.25 |
| Vc pizz. qn 114 | 0.01 | 0.23 | 0.48 |
| Vc pizz. qn 116 | 0.01 | 0.09 | 0.48 |
| Vla pizz. qn 124 (bar 41) | 0.01 | 0.24 | 0.65 |
| Vln I qn 171 (bar 52.75, p entry) | 0.04 | 0.15 | 0.52 |
| Vln II qn 42 (bar 15, pp entry) | 0.15 | 0.23 | 0.61 |
| Cb pizz. qn 108 | 0.00 | | 0.00 |

The cellos' Pizz RRx4 groups in `Celli KS Master.oib` have only round-robin start conditions: no CC1, no CC11 (`cc1groups.py`). No controller change can make them late.

Entries after a rest, qn below 203 (the same tempo map in both cycles), median sound start:

| Group | n | c03 | c04 |
|---|---|---|---|
| String legato-patch entries | 15 | 0.15 s | 0.37 s (13 of 15 over 0.15 s) |
| Celli pizzicato | 7 | 0.01 s | 0.25 s |
| Wind and brass Leg Slur entries | 19 | 0.02 s | 0.02 s |
| Wind and brass Sus entries | 23 | 0.07 s | 0.05 s |
| Harp | 13 | 0.01 s | 0.01 s |
| Timpani | 3 | 0.00 s | 0.00 s |

The same happens at the two climax arrivals. The probe measures the drop below the level of the preceding beat in the first 0.45 s after the downbeat:

| Arrival | c03 | c04 pass1 | c04 final |
|---|---|---|---|
| Vla tremolo, qn 204 (bar 61) | 4 dB | 17 dB | 23 dB |
| Vln I tremolo, qn 212 (bar 63) | 3 dB | 23 dB | 25 dB |
| Vln II tremolo, qn 212 | 2 dB | 22 dB | 26 dB |
| Vc tremolo, qn 212 | 6 dB | 9 dB | 16 dB |

In the final render the bar-63 tremolo sounds only at about qn 212.45. Trombone 1's entry at 212.5 and the basses' Sus note at 212 are on time.

**Inferred.**
- Only the large Hollywood Strings instances get later; winds, harp and timpani do not. That fits sample streaming falling behind (preload or disk), not anything in parts.json.
- The c04 CHANGES "Open" explanations do not hold:
  - "Tremolo does not sound at CC11 above 110": Vla tremolo notes at qn 208 and 212 play at the same CC11 (114-122) and start on the beat. The Vln I Trem groups have no start conditions, only CC11 to volume.
  - "The delayed-vibrato CC1 dip": the cello pizz has no CC1 dependence and is late as well.
- Whoever listens hears gaps at both climax downbeats, a ragged pizzicato bass line in bars 37-44, and soft string entries a quarter to half second behind the winds.

**Fix.**
- **Gate every render on attack timing.** Copy `/private/tmp/claude-501/mockup-loop/c05-A/probe.py` to `tools/probe_attacks.py`. Call it at the end of `tools/render_cycle.py` on `cycles/cNN/render` and write its output to `metrics/attacks.txt`.
  - It checks 10 isolated attacks with limits of 0.06-0.20 s and 4 tremolo arrivals with a 6 dB dip limit.
  - c03 passes all 14 checks; c04 fails 11.
  - If the probe fails, render again before judging anything else. Note in CHANGES.md how many attempts it took.
- **This cycle's REAPER restart (ONE_TIME.md, PreloadSize 0).**
  - After REAPER reopens, run a full `build_reaper.py build/parts.json jobs`, not `--mix-only`, so that every Opus instance gets a fresh state and loads its rows. c03, the last on-time render, was rendered from tracks built in that same session.
  - Then wait for the memory to settle, and render with nothing else heavy running.
  - When I measured, two Python processes from `~/sandbox/chrono-25d` held about 3.2 GB each.
- **Do not test the CC11-cap theory for the bar-63 tremolo** (CHANGES Open, cycle 4) until an unchanged render passes the probe.

## 2. Bar 61: the caesura turned the violas' last sextuplet note into a legato note that holds through the Tremolo keyswitch

**Measured (parts.json, c03 against c04).**
- c03: Vla qn 203.8333 (E flat 4, pitch 66) is a short slurred note on Sus MAX (`short_sus`). It ends at 204.03, the Tremolo keyswitch is at 203.94, and the tremolo chord at 204 is on time (4 dB dip).
- c04: the caesura slows the 0.25 qn before qn 204 to 30.8 bpm, so the same note now lasts longer than 0.25 s and fails the `short_sus` test in `build_track()`. It becomes a Leg Slur MAX legato target:
  - a new keyswitch to Leg Slur MAX at 203.6067;
  - velocity 124, moved early to qn 203.7583;
  - it ends at 204.0, so it is still sounding when the Tremolo keyswitch fires at 203.94.
- c04 final: the viola stem falls from -38 dB to -45..-66 dB between qn 204.1 and 204.8. The violas carry the tremolo harmony at the arrival of bar 61 (f, "non div., molto sostenuto").

**Inferred.** A monophonic True Legato voice that is still held when the articulation switches is a likely cause of the late tremolo, on top of finding 1. It is in the data either way, and c03's version worked.

**Fix (`tools/score_to_parts.py`, `build_track()`, string articulation branch).**
- Measure the `short_sus` duration without the caesura. Either:
  - compute `qn_to_sec(end) - qn_to_sec(q)` from the tempo steps before `add_caesuras()`; or
  - keep `short_sus` for any note whose end falls within 0.3 qn before a `CAESURA` key.
- Add a general guard after the note-length loop. When a note on a Leg articulation is still sounding at a later keyswitch of the same track, end it at `ks_qn - 0.01`. A keyswitch must never fall inside a sounding legato note.
- **Check:** `probe.py` reports a Vla dip at qn 204 of 6 dB or less, and parts.json shows Vla 203.8333 on Sus MAX again.

**Fallback, if bar 63 still fails the probe after finding 1.** Vln I/II/Vc at qn 212 are identical in c03 and c04 data, so there is nothing to fix in the data there. If the problem stays, take the keyswitch out of the arrival: give the tremolos their own patches. Append four tracks last, so the stem numbers stay:
- `1st Violins/03 Effects/1st Violins Tremolo.oib`
- `2nd Violins/03 Effects/2nd Violins Trem.oib`
- `Violas/03 Effects/Violas Trem.oib`
- `Celli/03 Effects/Celli Trem.oib`

All four are under `/Volumes/MAC DRIVE/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/`. Each new track carries only that section's Tremolo notes (qn 204-220) with the section's CC11, chord cut and mix entry. The KS Master tracks then rest there and never switch to Tremolo.

## 3. Horn 4 plays open in bars 87-89 while Horn 3 is muted

**Measured.**
- Horns 3-4 share a staff, and the score prints "mettere sord." (bar 82) and "con sord." (bar 87) for both.
- Horn 4's own "con sord." is `-\tag #'part` in `sections/coda.ily` line 56. `mockup.ly` removes part tags (`\removeWithTag #'part`, line 45), so Horn 4 never sees it.
- In parts.json, Horn 3 has CC15 = 127 from qn 271.5; Horn 4 has no CC15 lane.
- In bars 87-89 (qn 286-294, pp), Horn 4 measures -50.2 / -52.8 / -56.6 dB against Horn 3's -55.0 / -56.7 / -56.8. The open horn is the louder of the pair, and the muted colour that the score keeps for these last two bars (the only muted brass in the symphony, coda.ily line 53) is half lost.

**Fix (`tools/score_to_parts.py`, CC15 block near line 1061).**
- Let Horn 4 read Horn 3's mute texts: `sord_staves = staves + (["Hn3"] if tname == "Horn 4" else [])`.
- Give `text_state()` an optional staff list (`texts_until(st_list or staves, q)`).
- In the CC15 loop, iterate over `texts_until(sord_staves, END)` and call `text_state(q, [...], [...], sord_staves)`.
- Horn 4 then gets CC15 127 at qn 271.5, like Horn 3. HO has no real con-sordino horn samples (Solo French Horn/05 Mutes holds only stopped horn), so the CC15 script is the right tool.
- **Check:** Horn 4 has a CC15 lane in parts.json, and Horn 3 and Horn 4 are within 2 dB of each other in bars 87-89.

## 4. Bassoon 1's slurred pickup into the bar 79 ff plays at pp, 17 dB under Bassoon 2

**Measured.**
- Bar 78 prints f once on the shared Bn 1-2 staff (beat 1). Bassoon 1 enters on beat 3 (qn 261) with a C4 pickup, slurred on into the ff line of bar 79 (D flat 4-C4-B flat 3; page 6 of the score).
- The extraction gives the f only to Bassoon 2's voice. Bassoon 1's pickup has CC11 34 (its old pp) and velocity 41.
- Over qn 261-261.5 it measures -62.0 dB against Bassoon 2's -45.1, then jumps to -41 at qn 262.
- A check of every paired wind and brass track found no other place where one player is 20 or more CC11 under the other while both sound.

**Inferred.** The pickup that leads the woodwinds into the second climax is missing, and Bassoon 1 enters at qn 262 as a sudden step instead of the end of a crescendo phrase.

**Fix (`tools/score_to_parts.py`, `base_points()` or `build_track()`).** Add a small table for dynamics printed on a shared staff that reach only one voice in the extraction: `SHARED_DYN = {"Bassoon 1": [(259.0, "f")]}`. Merge it into that track's marks before the curve is built, so that Bassoon 1 has f (88) at qn 261 and ff at 262.

**Check:** Bassoon 1 over qn 261-262 is within 4 dB of Bassoon 2.

## 5. Divisi and solo lines still play on full-section patches (fourth report; lower priority than 1-4)

**Measured.**
- **Vc div., bars 18 and 22 (qn 51-54, 63-66).** Both voices are on Sus MAX (11 notes), so the slurred upper answer is not legato. At each div. entry the stem drops 8-10 dB in the first 0.2 s: qn 63 goes -55.7 → -66.2 dB in c04 and -61.2 → -66.5 in c03.
- **Vln I "solo, senza sord.", bars 17-22.** The whole section plays it, with +8 CC.

**Fix.**
- Use `Celli Divisi/06 Keyswitch/Celli KS Master DIV B.oib` as a new track (appended last) for the upper notes at qn 51-54 and 63-66. It plays on Leg Slur MAX with the normal slur logic, and the main Vc track keeps a single line there.
- Use `1st Violins Divisi/06 Keyswitch/1st Violins KS Master DIV A.oib` (half section, the closest thing on the drive to a solo player) as a track for Vln I qn 48-66, with Vln I's mix entry at -3 dB.
- Alternative for the cellos only: CC22 below 64 makes the True Legato script polyphonic (HO manual p. 91). The manual warns that this can produce unwanted transitions between the two voices, so a DIV B track is the cleaner fix.

## Do not touch

- **Chords never reach a monophonic legato patch.** No legato-patch note overlaps another note on its track by more than 0.1 qn except its own legato target (checked over all tracks).
- **The pizz velocity scheme and the basses' pizz.** Cb pizz is on time in every render.
- **Harp roll timing and the Harp harmonics track.** Harp entries start in 0.01 s.
- **Timpani articulation, roll and stroke scheme.** Strokes are on time; qn 277 is present in the final render.
- **Trombone 1's Sus Accent marcato entry at qn 212.5.** On time, 0.01 s.
- **Wind and brass legato leads and velocities.** Leg Slur entries median 0.02 s, unchanged from c03.
- **The same-pitch merge, the unison drop and the caesura timing itself.** Only the `short_sus` side effect in finding 2 needs fixing.
