# Cycle 3, critic C: tempo, timing and transitions (render c02)

Method. Everything below was measured on the c02 stems and master (`cycles/c02/render/`, the stem-fixed version), against `build/parts.json` (`sq` = score onset, `qn` = moved onset) on the parts.json tempo map. I used three measures:

- Entries after a rest of 0.1 s or more: the time a stem reaches 6 dB under the note's early peak. This uses a 20 ms window on a 5 ms hop, and a note counts only if it rises at least 10 dB out of the previous tail.
- Pitch changes within one track: the crossover, meaning the first point where the new pitch's harmonics 1-4 hold over the old pitch's for 30 ms, from a 2048-point STFT on a 5 ms hop. Values that sit on the search-window edge are dropped.
- Struck notes: the first 6 dB jump in 20 ms.

"Rel. to attacks" means a value minus the median non-legato arrival of the other tracks at the same score onset. That is what a listener hears as together or not together. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c03-C/`: lib.py, onsets.py, xover.py, align.py, timp.py, first.py, lag2.py, hit.py, dan.py, acc.py.

Brief items 7-8 (measured). Loop pulse on the master is low. The 100-300 Hz level autocorrelation at 3.95 s is +0.02 on the final chord (qn 712-728), -0.20 on bars 73-76, +0.10 on the intro and +0.26 on bars 47-50. The centroid values lie between -0.13 and +0.02. Accent 2-5 kHz over the first 80 ms minus the body: brass median -8.1 dB (p90 +0.8), strings -3.8 (p90 +0.5), winds -6.1 (p90 -0.7). A few outliers of +8 to +12 dB are left for the articulation critic. None of these are timing problems.

## 1. New bow strokes after slurred Sus MAX eighths are joined as slow legato and sound up to an eighth late (strings, Allegro, 41 notes) — measured

Where: these notes are on Leg Slur MAX, and the note before them is a Sus MAX eighth that overlaps them by 0.03 qn. Examples:
- Violins I: qn 70 (bar 18, the g'2 after the d''8 c''8 slur), 78 (bar 20, des'''2 sf), 260, 272, 276, 282, 392, 400, 444, 448, 454, 574.
- Violins II: 172, 260, 375, 392, 400.
- Violas: 76, 138, 363, 368, 428, 434, 436, 454, 460.
- Violoncellos: 286, 351, 356, 420, 534.

The cases cluster in bars 18-20, 66-72, 88-116, 134 and 144.

What is wrong: the fast-slur rule plays the eighths on Sus MAX with a 0.03 qn overlap. The note after the slur stays on Leg Slur MAX as a "first note", and it gets no lead (lead = 0.000 on all 41). The KS Master hears the overlap as a legato transition (kit LEARNINGS 6, `SOST_JOIN_LEAD_S`), so each of these new bow strokes changes pitch late:
- Median crossover +0.165 s, p25 +0.115, p75 +0.215.
- Relative to the other sections' attacks at the same onsets: +0.136 s (n=6).

Bar 18 crosses at +0.225 s and bar 20's sf at +0.215 s. At 126 bpm an eighth lasts 0.238 s, so the half note lands almost an eighth late and the figure sounds dotted. The same family's real legato targets, which do get the lead, cross at -0.03 s (Vln I Leg BC MAX fast, n=46).

Fix in `tools/score_to_parts.py`, in the lead loop (`for n in ns: ... elif n.get("leg_target") ...`). Treat any Leg Slur MAX or Leg BC MAX note whose previous note is an overlapping Sus MAX note from the fast-slur rule (the `qn_to_sec(... ) < 0.25` branch) as a legato target:
- Use `leg_s` with the existing cap `cf_ * (q - pv["qn"])` (0.45 x 0.53 qn ≈ 0.11 s at 126).
- When a slur boundary or new bow lies between the two notes, put the target on Leg BC MAX, the bow-change legato row, which crosses at -0.01..+0.03 s for Vln I/II and Vla here.
- Keep Leg Slur MAX inside one slur.

Expected result is about +0.04..+0.07 s, the same as the other Leg BC joins. Alternative: end the eighth 0.02 qn before the next onset (no overlap) and play the next note on Sus MAX with `ENTRY_LEAD_S["string"][1]` (0.06 s). String Sus MAX f entries measured +0.055 s here.

## 2. Wind slurred first notes after a rest speak 0.15 s late; the flutes and oboes trail the violins on the theme's pickup (about 30 notes) — measured

Where: Flute 1 and Oboe 1 on the motto pickup and theme entries:
- qn 88 (bar 23): Fl1 +0.23, Ob1 +0.265.
- 104.5 and 112.5 (bars 27, 29): Fl1 +0.175/+0.185, Ob1 +0.160/+0.160, while Violins I on the same pickup are at +0.000.
- 146.5 (bar 37): Ob1 +0.145.
- 312.5 (bar 79): Ob1 +0.155, against Vln I +0.065.
- 536 (bar 135): Fl1 +0.225.
- 552.5 (bar 139): Fl1 +0.180, Ob1 +0.165, against Vln I +0.015 and Vln II +0.010.
- 578 (bar 145, p): Ob1 +0.40.
- Also Oboe 2 408.5, Cor anglais 586.5 and Bass clarinet 304.5 (+0.15..+0.24).

What is wrong: winds have no entry lead (`ENTRY_LEAD_S` has only string, brass, Bassoon and Contrabassoon). The first note of a wind slur is played on the Leg Slur MAX row, which is slower. Entry arrival (-6 dB):
- wind Leg Slur MAX: +0.150 s at f+ (n=13) and at p-mf (n=11).
- "Leg Slur" (clarinet row): +0.145 (n=12).
- "Sus Non Vib": +0.113 (n=10).
- wind Sus MAX: +0.055 at f+ (n=53).
- string pickups on Leg Slur MAX, with their 0.06 s lead: +0.055 (n=46).
- brass Sus: +0.005 (n=65).

On a 0.2 s pickup eighth, 0.15 s late means the eighth barely sounds before the downbeat, so the doubled pickup flams.

Fix: add an articulation-specific entry lead in `score_to_parts.py`, a new table `ENTRY_LEAD_ART_S = {"wind": {"Leg Slur MAX": 0.11, "Leg Slur": 0.11, "Sus Non Vib": 0.07}, "brass": {"Leg Slur MAX": 0.06}}` (seconds, added to the family's entry lead). Apply it in the same branch and with the same rest test (`q - pe >= 0.5`) and CC11 pull as the family entry lead. Leave wind Sus MAX entries alone, since they are already within 0.05 s. Brass Leg Slur MAX first notes measured +0.115 (n=8) against Sus MAX +0.005, which is why brass gets a smaller extra. Re-measure the eight pickups listed above against Violins I.

## 3. Timpani strokes land 80 ms ahead of the band in every Allegro tutti (45 strokes); the crash and tam-tam do the same — measured

Where: timpani strokes:
- qn 100-128 (bars 26-33)
- 272-286 (bars 69-72)
- 324-330 (bars 82-83)
- 456-464
- 520-568 (bars 131-143)
- 628-640 (bars 158-161)
- 676 (bar 170)

Also the crash at qn 636 and the tam-tam at qn 484.

What is wrong: a struck sound is at full level within 10 ms of its note-on. The sustained sections reach -6 dB about 80 ms after theirs: brass Sus at ff takes 0.08-0.10 s, for example Trumpet 1 at qn 100 goes from -77 dB at note-on to -20 dB 0.10 s later. The timpani have no lead and the others mostly have none either, so the stroke comes first:
- Timpani stroke minus the median arrival of the other tracks at the same onset: median -0.080 s over 45 strokes. Bar 26 -0.080, bar 33 -0.075, bar 72 -0.065..-0.130, bar 142 -0.120..-0.166, bar 160 -0.055, bar 170 -0.070.
- The crash's first audio is 60 ms ahead of the bar 160 attacks.
- The tam-tam is about 70 ms ahead at bar 122.

At ff an 80 ms gap between a drum and the brass is heard as the timpani anticipating the chord.

Fix in `score_to_parts.py`: add a negative lead for struck percussion. Start timpani notes `TIMP_DELAY_S = 0.06` s after their score onset, converted with `lead_qn`, for strokes and roll starts alike. Add `"delay_s": 0.05` to the crash and tam-tam entries of `PERC_MAP` in `build/score_config.py`. The suspended-cymbal roll's `lead_s` must then grow by 0.05 so its peak still meets the crash. Leave timpani CC and volume shapes on score time. The target is the timpani-minus-others median at about -0.02 s.

## 4. REAPER moved the score's first tempo marker: every event plays 1/6 qn early on the measurement axis, and every shape fitted from a render lands 1/6 qn early — measured (cause read from the .rpp)

Where: the whole project. In `mvt1-v221-mockup.rpp` the tempo envelope reads:

    PT 0.000 60 / PT 4.000 50 / PT 70.200 126 ...

The second marker should be at 3.000 s. `build_reaper.tempo_job` gives the pre-roll marker the score's time signature: `sig.get(0.0, (3, 4))` returns (4, 4), because `parts.json` timesig has [0.0, 4, 4]. The 3 qn pre-roll is therefore an incomplete 4/4 bar, and REAPER snapped the score's 4/4 marker to the next barline at 4.0 s. The later markers were placed by time and are correct. As a result:
- REAPER's qn runs 1/6 ahead of the intended map from score qn 1 on.
- Every note, CC, keyswitch and envelope point written at qn + 3 sounds 1/6 qn early.

Evidence:
- On every stem, the first audio after digital silence comes before the parts.json note-on by -0.0792 s at 126 bpm, -0.0890 at 112, -0.1388 at 72, -0.2000 at 50 and -0.117 at the bar 68 rit. That is 0.1663-0.1667 qn in every case, on all 32 tracks (`first.py`).
- Envelope changes measured as c02 stem minus c01 stem, against the envelope points `vol_points()` actually writes, arrive early by the same amount: Tbn1 -0.080 s, Tpt1 -0.070 and Vla -0.080 at 126 bpm; Harp -0.090 at 112; Vc -0.130 at 72 (`lag2.py`).
- This is the "envelope lead 0.09-0.25 s" left open in c02 CHANGES.md and loop/LEARNINGS.md.
- The movement II project starts in 3/4, its marker is at 3.000 s, and it did not have this fault.

What a listener gets:
- Notes and their planned shapes move together, so accent swells, hairpins and roles are still in step with the notes.
- Anything fitted from a render is placed 1/6 qn early relative to the sound it targets: `rebow_fills.json`, `early_fills.json` (the "dip at -0.07 s" `pre_s` entries), loop profiles and join notches. This is why the c02 loop profiles made the pulse worse, and why re-bow fills now start before their re-bows (Vln I 45.043: +4.8 dB at -0.12 s).
- Every tempo change takes effect 1/6 qn late:
  - Score qn 0-1 runs at 60 bpm, so the first beat is 0.20 s short.
  - The first beat of the Allegro at qn 56 lasts 0.12 s too long (1/6 qn at 50 instead of 126).
  - The bar 170 fermata beat is 0.17 s short (1.33 s instead of 1.50).
  - The cello's Più lento downbeat is 0.11 s late.
  - The final bar loses 0.13 s.

Fix:
- In `tools/build_reaper.py` `tempo_job`, give the pre-roll marker its own meter, for example `"num": int(PRE) if PRE in (2, 3) else 4, "den": 4`, or set `PREROLL_QN = 4.0`.
- Make the returned `mismatches` fatal. It must be empty: today it should list about 330 markers off by 0.1667 qn.
- Rebuild with `--midi-only --tempo` (kit LEARNINGS 15).
- Then shift every render-fitted time in `rebow_fills.json` and `early_fills.json` (`pre_s`, hold ends) later by 1/6 qn, in seconds at the local tempo, or refit them on the c03 render.

After this change all stems sit 1/6 qn later than c02 on the measurement axis. Compare later timing numbers with that in mind.

## 5. Legato leads are too large for movement I's loud Allegro, and movement II's per-pitch lead tables are still active — measured

Where and evidence. Crossovers relative to the other sections' attacks at the same onsets (fast tempo, n in brackets):
- Violoncellos Leg BC MAX: -0.118 s (36). Absolute -0.090 s (63). Examples: qn 86, 106, 192, 200, 204, 260, 272, 276, 392, 536 and 556 cross -0.13..-0.25 s, so the bass moves ahead of the downbeat at section starts (bars 22, 27, 49-51, 66, 69, 70, 99, 135, 139).
- Oboe 1 Leg Slur MAX: -0.098 (12). Absolute -0.085 (39).
- Horn 1: -0.100 (7).
- Clarinet 1: -0.070 (15).
- Cor anglais: -0.066.
- Trumpet 1: absolute -0.100 (9).
- Violins I/II and Violas Leg BC MAX: -0.010 / -0.009 / +0.008. These are fine.

On top of that, `score_to_parts.py` still has movement II's measured tables, which apply to movement I's pitches:
- `LEG_PAIR_EXTRA_S["Oboe 1"][(77, 75)] = 0.10` makes F5 -> E♭5 at qn 92, 96, 540 and 544 (bars 24-25, 136-137) cross -0.125..-0.155 s.
- `LEG_EXTRA_S["Violas"] = {60: 0.10}` plus the viola pair extras push violas leaving C4/B♭3 to leads of 0.325-0.425 s. Crossovers: qn 24 -0.195, 178 -0.25, 182 -0.17, 650.5 -0.145, 690 -0.18, 704 -0.195, 710 -0.22.
- Horn 1 595.5 (F4 extra): -0.146.
- Soft slow Leg Slur MAX joins are also early: Vln II -0.105 (10), Vla -0.142 (8), Vc -0.130 (7).

Fix:
- In `build/score_config.py`, set `LEG_EXTRA_S = {}`, `LEG_PAIR_EXTRA_S = {}` and `LEG_SOFT_EXTRA_S = {}`. They are movement II pitches.
- Set `LEG_ART_EXTRA_S = {"Violoncellos": {"Leg BC MAX": -0.07, "Leg Slur MAX": 0.0}, "Violins II": {"Leg Slur MAX": 0.0, "Leg BC MAX": -0.03}, "Violas": {"Leg Slur MAX": 0.0}}`.
- Set `LEG_LEAD_S` overrides `"Oboe": 0.02, "Cor anglais": 0.03, "Clarinet": 0.0, "Flute": 0.0`.
- Use `"brass": 0.05` at CC11 88 and above. This needs a loud/soft split like `LEG_SOFT_EXTRA_S`; or set brass 0.06 overall.

These cut each early group by about half of its measured lead, and leave room for the slower perceived onset of the attacks they are compared with. Re-measure against the attacks, not against the beat, after fix 4 has moved the axis.

## 6. No time at the phrase ends, the tutti breath or the fermata rest: the Lento and the cantabile sections are metronomic — tempo map measured, musical effect inferred

Where and evidence:
- `PHRASE_ARCS`, `TEMPO_PUSH`, `BEAT_STRETCH` and `CAESURA` are all empty in `build/score_config.py`. The tempo map has one point in the whole Lento: all 56 beats of bars 1-14 are at 50.0. The second theme (qn 184-244) is 60 beats at 112.0, and the coda cello solo (qn 680-704, espr.) is 24 beats at 72.0. Movement II needed its phrase arcs for exactly this (kit c12-c24).
- The printed breath before the bar 160 fff (`\breathe` at qn 636 in Fl1/2, Ob1, Hn1/2, Tpt1/3, Tbn1, BTbn, and at 632 in Tpt2/Tbn2/Tuba) gets only the 0.3 qn note-end gap. The map steps straight from 120.9 to 100, and the master does not dip at all (qn 635.5-636: -7.9..-10.4 dB).
- The bar 170 fermata over a rest after the ff chord (the "denied tutti"): the master decays from -17 to -46 dB in 1.1 s, and the cello's mp solo enters 1.25 s after the release, so the silence is barely heard as a fermata.

Fix in `build/score_config.py`:
- Add `PHRASE_ARCS = [(0, 16, "sub"), (16, 32, "sub"), (32, 48), (48, 56, "main"), (184, 200), (200, 216), (216, 232, "sub"), (232, 244), (584, 600), (600, 620), (680, 696), (696, 704, "sub")]`. The arcs touching `RAMP_SPANS` are skipped by the code.
- Add `BEAT_STRETCH = {679.0: 0.6}`: the fermata beat at 24 bpm, 2.5 s.
- Add `CAESURA = {636.0: 0.15}`. Also reduce the suspended cymbal's `lead_s` by the same 0.15 s (after the change in finding 3) so its peak still meets the crash.

The length change is about +4 s, still under the printed c. 7½ minutes. Check the climax order and the cymbal peak time after the render.

Do not touch:
- The `RAMP_SPANS` realisation of the printed rit./allargando/animando steps. Every span ends at or near its printed tempo (poco rit. into 112 at qn 184 and 584, allargando 125 -> 101 into the sostenuto 100, rit. 85-78 into the a tempo).
- The Violins I/II and Violas Leg BC MAX leads (crossovers within ±0.03 s of the attacks).
- Brass Sus MAX entries (+0.005 s).
- The final bar at 30 bpm (8 s) with its fade.
- Keyswitch placement. All 973 keyswitches precede their notes by 10 ms or more (median 29 ms), and none follows its note.
