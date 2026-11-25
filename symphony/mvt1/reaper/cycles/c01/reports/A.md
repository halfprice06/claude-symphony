# Cycle 1, critic A: articulation and phrasing (render c00)

Scope: every wind, brass and string note in build/parts.json, with the articulation taken from each track's keyswitch lane, measured on the c00 post-fader stems (stereo power) against score onsets (`sq`) on the parts.json tempo map. Scripts and data are in /private/tmp/claude-501/mockup-loop/mvt1-c01-A/ (lib.py, s2l.py, joincat.py, rebow2.py, trans.py, acc.py, acc2.py, uni.py, masteracf.py).

Structural checks that passed (measured): no chord or simultaneous divisi note reaches a legato row on any track, there are no same-pitch overlaps on any track, no note is silent (every note peaks above -75 dB), and the held-note-to-tremolo arrivals dip 4.7 dB or less.

## 1. The theme's pickup-to-accent motif lands under its own pickup (strings; Allegro throughout)

Where: the head motif of the first theme (an eighth rest, then an eighth slurred to an accented long note), for example Violins II qn 110, 278 and 282, Violas 105, 536, 665 and 670, Violins I 105, 110 and 113, and Violoncellos 521 and 529.

What is wrong (measured): the slurred eighth is shorter than 0.25 s, so `score_to_parts.py` plays it on Sus MAX (the `short_sus` rule in the string block, "c03 (C #3)"). The accented note it slurs into is then a Leg Slur MAX target. Sus MAX and Leg Slur MAX sustains sit at different levels at the same CC11 (kit LEARNINGS 6), so the accent ends up quieter than the pickup:
- All 93 string joins from a Sus row into a legato row: the new note's body (0.25-0.8 s) minus the previous note's body has a median of -1.6 dB. For 308 joins between two legato notes the median is +1.8 dB.
- The 43 accented targets of these joins have a median of -2.7 dB.
- The pickup-to-accent cases with the CC11 accent bump in place (+5 CC) are much worse. Violins II at qn 110 is -10.2 dB, at 278 and 282 -8.7 dB, Violas at 105 -8.1 and at 665 -9.6, Violins I at 113 -5.3.
- Per track, the eighth-to-target pairs have medians of Violins II -3.5, Violas -2.5 and Violins I -2.4 dB.
- 50 ms envelopes show the shape at Violins II qn 110: -22 dB on the pickup, then -34 to -39 dB for the rest of the accented half note. This also makes these accents the largest front-edge spikes in the movement (Violins II 110 measures +14.1 dB of 10 ms peak over body, the highest of any accent).
- Timing: these targets get no legato lead (qn equals sq). After the dip they reach body - 3 dB at a median of +0.40 s, against +0.23 s for legato targets with leads. That is almost a beat at q=126.

As heard (inferred): every statement of the main theme accents the upbeat instead of the downbeat.

Fix: run it as a test with a control. In `score_to_parts.py`'s string articulation block, stop applying the `short_sus` Sus MAX rule to a slurred note shorter than 0.25 s when the next note in the same slur is 1 qn or longer. That keeps the pickup and its target on Leg Slur MAX, so both use the same sustain layer. Keep `short_sus` for runs, where the next note is also short. Give the target the normal legato lead (strings 0.17 s, Violins II and Violas 0.20 s).
- If the pickup then speaks too slowly as a disconnected Leg Slur note, use the fallback for accented targets only: play the target on Sus MAX as a fresh bow stroke with the entry lead and the brass-style swell (the `GENTLE_ACCENT` shape, +3 dB, rise 0.07 s, held to 0.25 s, gone by 0.6 s).
- Pass criterion: on the 12 listed onsets, the target body minus the pickup body is at least +1 dB, and the target reaches body - 3 dB by +0.15 s.

## 2. Re-bow seams: celli and second violins dip and step at most re-bows

Where: Violoncellos, 29 re-bow seams, and Violins II, 13. The worst ones are Violoncellos qn 37.37 (bar 10, intro, where the celli are the loudest stem), 21.44 (bar 6), 163.78 (bar 41), 298.37 and 508.16, and Violins II 189.62, 714.52 and 719.91 (final chord).

Evidence (measured on an 80 ms envelope):
- Celli: median seam dip 6.9 dB against 4.2 dB at control points in the middle of unsplit 2.5-4.6 s notes. 17 of 29 seams dip 6 dB or more, and 17 of 29 show a level step of 3 dB or more between 1-2 s after the seam and the 0.4 s before it (median +1.9 dB, new Sus MAX piece louder).
- Celli examples: 37.37 dips 14.5 dB and steps +3.9 dB. 163.78 steps -8.5 dB.
- Violins II: median 6.4 dB against a 3.2 dB control, 7 of 13 at 6 dB or more.
- Violas and basses seams are close to their controls (4.1 against 4.6, 3.9 against 5.5), but have 7 and 12 steps of 3 dB or more.

The stagger itself works (measured). On the final chord (qn 712-728) the master's 100-300 Hz level and spectral-centroid autocorrelations at 3.95 s are -0.14 and -0.07. No stem has a string note longer than 6 s on one sample, and per-stem autocorrelations are -0.23 to +0.11.

Fix: fit `build/rebow_fills.json` on the c00 stems by the movement II c26 method (kit LEARNINGS 6, the `_doc` in symphony/mvt2/reaper/build/rebow_fills.json):
- Over the first 1.5 s after each re-bow, follow the level before it.
- Then hold the offset to the next re-bow, clamped -6 to +9 dB.
- Do the celli and Violins II first, then the violas' and basses' steps.

Keep `REBOW_SEG_S`, `REBOW_TRACK_JITTER` and the re-bow times unchanged in the same cycle, or the fit no longer matches.

## 3. Woodwind accents have a sharp front edge (Dan's rule 4)

Where: every loud woodwind accent, 165 notes. The most audible are Flute 1 (36, bars 26-31, 93-96, 117-120, 160-170), Clarinet 1 (43; worst qn 381, 465 and 417) and Flute 2 (worst 286).

What is wrong (measured): `GENTLE_ACCENT` covers only brass. Woodwind accents at f and louder still play the `Sus Accent MAX` sample with the +8 CC11 bump (fff layer) and +10 velocity.

Peak of a 10 ms window in the first 120 ms minus the body (0.2-0.7 s):

| Track or group | Accents, median (p90) | Plain notes, median |
|---|---|---|
| Flute 1 | +6.2 (+9.4) dB | +0.8 dB |
| Bassoon 2 | +5.0 (+8.8) | |
| Contrabassoon | +4.8 (+7.0) | |
| Flute 2 | +4.7 (+7.7) | |
| Bassoon 1 | +4.1 (+7.4) | |
| Clarinet 1 | +3.2 (+9.4) | |
| Oboe 1 | +3.2 (+6.7) | |
| Brass on `GENTLE_ACCENT` | +1.2 to +3.6 | |
| Woodwind plain notes overall | | -2 to +1 dB |

In the first 250 ms against the nearest unaccented notes, Flute 2's accents are +8.0 dB (p90 +13.6), Clarinet 1's +5.7 (p90 +11.6) and Cor anglais +7.3. The target is 2-4 dB.

2-5 kHz energy in the first 80 ms minus the body is -3.6 to -7 dB (Contrabassoon -0.7, p90 +2.0). This is not the c25 trombones' 2-5 kHz burst. The problem is a click-like front edge and too much emphasis.

Fix: in `score_to_parts.py`, add `"wind": {"arts": ("Sus MAX", "Sus Max", "Sus Non Vib"), "db": 3.0, "soft_db": 2.0, "swell_s": (0.07, 0.25, 0.6)}` to `GENTLE_ACCENT`. This removes the accent sample, the CC11 bump and the extra velocity on winds.
- Accents inside a slur that are now Leg Slur targets keep their row. Give them the swell only.
- Measure afterwards: the 10 ms peak minus the body should be under +3 dB, and the first 250 ms should sit 2-4 dB over the unaccented neighbours.

## 4. The suspended-cymbal roll peaks 1.4 s before the crash it leads into (bar 159 into 160)

Where: Suspended cymbal, qn 632-636 (pp < with soft sticks, into the fff crash cymbals and largamente at qn 636, the movement's climax).

Evidence (measured):
- The roll is one note on key 60, the shortest of the four recorded crescendo lengths, at velocity 105 with no `lead_s`.
- On the stem it peaks at qn 633.4 (0.71 s after its start) at -28.1 dB, falls to -38.8 dB by 1.5 s and is about 22 dB down at qn 636.
- The crash peaks exactly at qn 636 (-25.1 dB).
- Bar 159 lasts 1.98 s on the tempo map.

As heard (inferred): the crescendo arrives and dies away before the downbeat it should lead into.

Fix: in `build/score_config.py` `PERC_MAP["Suspended cymbal"]["ridecymbal"]`:
- Choose the key (62, 64 or 65) whose recorded crescendo reaches its peak at or after 1.98 s. Read the peak time from the .oib region lengths or from a one-note test render.
- Set `lead_s` to that time-to-peak minus 1.98 s, so the peak lands on qn 636 (`build_perc_track` already applies `lead_s`).
- Keep velocity at 90 or more (the f take); the roll ends fff.

## 5. Unisons and "metà" played on one solo sample where HO has recorded ensemble patches

Where (measured from the score against parts.json):
- `find_unisons` drops 97 of Horn 2's 189 notes and plays them on Horn 1's solo-horn sample with +3 dB. Bars 24-25, 28, 41-42, 62-64, 66-72, 78-79, 96-102, 117-121, 158-161 and 166-170, including the printed "a2" at bar 28.
- Trombone 2 loses 32 notes (bars 80-81, 117-121, 131-134) and Trumpet 2 loses 23 (131-132, 167-170).
- Violins II "metà" at bars 47-54 (pp held notes under the cello and horn dolce tune) plays on the full-section KS Master. `score_to_parts.py` has no rule for "metà".

Inferred: a doubled solo sample sounds like one louder player, not two. At the ff tuttis of bars 117-121 and 158-161 this thins the horn section exactly where it should be widest.

The library has the recorded patches:
- 2 French Horns/06 Keyswitch/2FH KS Master.oib (used in movement II c18; it needed a track gain 4.6 dB over the solo-horn track, kit LEARNINGS 8)
- 2 Trombones EXP/04 Keyswitch/2TB KS Master.oib
- 2 Trumpets/06 Keyswitch/2TP KS Master.oib
- 2nd Violins KS Master DIV B (in ks_maps.json)

Fix:
- Append a "Horns 1-2 a2" track on the 2FH KS Master and route the a2 windows to it with `TRACK_WINDOWS` (taken from Horn 1 and Horn 2, as in the movement II example config). Start with bars 62-72, 96-102, 117-121 and 158-170.
- Add a `TRACK_WINDOWS` entry that sends Violins II qn 184-216 to a 2nd Violins DIV B track (Close mic only, so a reverb send of about 0.5).
- Trombones and trumpets on 2TB/2TP can follow in a later cycle, depending on memory (each new Opus instance counts against the 45 GB budget).

## 6. Smaller articulation items

1. **Legato join holes (measured, 30 ms window, from the score onset).**
   - Celli have 18 joins that dip 6 dB or more under the lower of the two bodies (bars 17, 29, 38, 50, 52, 67-68, 105, 116, 122, 140, 159-160, 166, 168-169, 172-173). Bars 50 and 52 are inside the dolce cello tune.
   - Oboe 1 has 7 (bars 23-24, 45-46, 125, 135, 146) and Bassoon 1 has 4.
   - Every other track's median join dip is 1.4-3.3 dB.
   - Fix: run `tools/auto_fills.py` on c00 with c00's parts.json (kit LEARNINGS 6 rules: dB = dip - 3, cap 6, the overshoot rule).
2. **Woodwind staccato is played on Sus MAX at half length (0.25 qn = 0.12 s).** This covers Flute 1 (11 notes), Oboe 1 (4), Cor anglais (8), Clarinet 1 (5) and Bassoon 1 (8).
   - Measured: in about half of these notes the highest 10 ms frame in the first 0.25 s falls at +0.22-0.245 s, which is the next note's attack. The staccato note never reaches its own peak.
   - The string Stac RR rows peak at +0.02-0.06 s.
   - Fix: map printed staccato on winds to `Stac DblTng RRx9` (`RRx5` on the contrabassoon and bass clarinet). Velocity sets the level, as on other short articulations. Write the row name into the keyswitch lookup at `elif q in stacc_q` for the wind branch.
3. **Harp "étouffez" (qn 244, 650, 654, 727) is not read.**
   - Measured: at qn 650 the chord from 648 is still at -47 dB after 0.25 s and -51 dB after 1 s.
   - Inferred: the effect is mostly masked under the tutti. A damped end (a fast volume-envelope cut to -30 dB over 0.1 s at the étouffez point) is cheap to add.
4. **Loud breath marks before the climax downbeat (qn 632-636, ten wind and brass parts) leave 0.15 s gaps.**
   - Measured: the master dips 2.0 dB at qn 635.
   - Inferred: that is barely audible. Kit LEARNINGS 7 gives a 0.5 qn gap with a 10 CC fall for an audible loud breath, or a short tempo-map caesura. Leave this to the tempo lens if the lift is wanted.

Do not touch: `AUTO_REBOW` stagger and timing (no loop pulse on the final chord: master 100-300 Hz and centroid autocorrelation at 3.95 s are -0.14 and -0.07); `GENTLE_ACCENT` on brass (2-5 kHz attack minus body -3.4 to -9.7 dB median, master 2-5 kHz median change at accent onsets -2.9 dB); string Stac RR rows; tremolo hand-overs; the Leg BC / Leg Slur keyswitching inside phrases; the unload of unused rows.
