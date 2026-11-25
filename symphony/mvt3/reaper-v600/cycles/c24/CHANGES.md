# Cycle 24 (2026-11-17): CC11 law, string marcato chords, celli bass line, fff re-attack, inner voices, delivery

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c23 render), the coordinator's rulings 1-12 and its later notes (scherzo c21 / c22, the shared delivery spec "climax margin before loudness range"). Snapshot before this cycle: `before/`. Scripts: `actor_scripts/` (`meas24.py` the ruled targets, `holes24.py` legato holes with 200 ms windows on flutes, oboes, cor anglais, Bassoon 1, Clarinet 1 and celli (ruling 12), `deliv24.py` delivered-file checks, `dynsteps.py` printed-dynamic medians on an mp3, `simdeliv.sh`, `rstart.py` range starts, `notes.py`, `cfgdump.py`, `marcread.py` / `cc11law.py` patch reads; lock phase `auto1.sh`, `p1.sh`, `pa.sh`, `ana.sh`, `p2.sh`, `p3.sh`, `wait_lock.py`, `rr.py`). Logs: `logs/`, `phase.log`.

Standing rule (Dan): no per-note move in the track volume envelope. Every change is on the instrument side, a held passage level, a tempo change or a delivery ride. `stepcheck.py`: fader moves of 2 dB or more within 60 ms inside a note 31 -> 30; the basses' 2.5 dB ramp inside the pedal of bars 43-50 is gone.

## For Dan

- **Loudness unchanged at -14 LUFS.** The final chord is now the loudest moment (0.6 dB over bar 223 and 0.7 over bar 263; before, final and 223 were tied). The quietest music (bars 97-98, 171-180) is 2 dB louder.
- **Loud passages are louder than the medium-loud ones.** The delivery squeezes the ff passages less: ff passages are 3.7 dB over f passages on the mp3 (c23: 2.9 by the same measure).
- **The brass chorale after bar 223 (bars 224-225, printed f) is no longer softer than the soft trumpet solo of bars 61-62.** It is 2-4 dB over it now (c23: 2-3 dB under).
- **The opening chords strike sooner.** The first violins play the accented ff chords with a marcato attack. The loudness peak of the chord now comes 0.1-0.25 s sooner in bars 1, 5, 147 and 277 (for example +0.375 -> +0.225 s in bar 5). The attack is not brighter than the held tone. The other string sections still swell into these chords.
- **The fff chord of bar 223 has a fresh attack.** The brass and winds now lift for 0.08-0.1 s before it. Most of them now dip 4-9 dB before the chord (c23: 1-4 dB).
- **Trombone accents in bars 247-251 no longer bite.** They are now tongued like the neighbouring accents. The 2-5 kHz burst went from 5-11 dB over the held tone to 1-6 dB under it.
- **Inner voices:**
  - Horn 3's soft upper note in bars 235-237 is now 3.4 dB under Horn 4 (c23: 8.0).
  - Clarinet 1's pp echo in bar 121 is now 5.6 dB under the bassoon solo (c23: level with it).
  - Trombone 2 in the bar 223 chord is now level with Trombone 1 (c23: 3.9 dB over).
  - The woodwinds at the three fff arrivals are 2 dB closer to the brass.
- **Two notes that entered late now enter on time:** the second violins at bar 128 and the cellos at bar 239. They had started soft and swelled.
- **The violins are less bright:** 2-3 dB less energy above 6 kHz.
- **Not fixed:**
  - The cellos' half-note bass line under the first theme still swells late on each note. Its low-mid pulse in the master is smaller (worst note +9 -> +6 dB).
  - Oboe 1 in bars 143-144 is still level with the clarinet. The range test said this would work and it did not.
  - Trumpet 3's accents in bars 257-262 are still only 0.5 dB over the plain notes.
  - Each new bow on the basses' soft pedal in bars 43-50 still swells in, by 8-10 dB over about a second.

## Results (main render 16:26-16:36)

- **Delivered (`mvt3-mockup-c24.mp3`, re-delivered after the render with the refitted ride rows; the file starts 0.30 s before qn 0):** -14.0 LUFS, LRA 11.8 LU, true peak -1.1 dBTP, p10 short-term -22.3 LUFS, limiter 5.8 dB (final chord), 3.9 (223), 2.8 (263). First delivery (`mvt3-mockup-c24-first.mp3`, rows written before the render): -14.0, LRA 12.1, p10 -22.6, limiter 5.8, final tied with 223 (-7.5 / -7.5).
- **Shared delivery spec, the six criteria on the c24 mp3:**
  1. -14.0 LUFS, -1.1 dBTP: met.
  2. Summit (final, bars 278-279) leads every rival by 0.5 or more: final -7.5. Bar 223 is -8.1 (+0.6), 263 -8.3 (+0.7), and the loudest ff bars are 227 -8.1 (+0.6), 277 -8.2 and 264 -8.2. Met. Order final > 223 > 263 holds (223 over 263 by 0.1).
  3. f -> ff 2 LU or more: medians f -15.6, ff -11.9 (+3.7). Met.
  4. p10 -23 or higher: -22.3. Met.
  5. Limiting on climaxes 6 dB or less: final 5.8. Met.
  6. LRA 10.5 or more: 11.8. Met.
- **Arrival steps on the mp3:** 223 over 222 +3.1 dB, 263 over 262 +0.6 (c23 +1.2), final over 277 +0.9 (c23 +1.1). Bar 5 is 1.0 dB under bar 223 (c23 0.8).
- **mp3 stops:** bars 2 / 6 / 94 / 113 / 166 / 204 / final 17.0 / 16.9 / 14.9 / 14.4 / 16.9 / 16.3 / 16.3 dB at +0.3 s. Bar 113 is 0.1 under the 14.5 floor; bars 2 / 6 are at the 17 ceiling.
- **Master:** -19.4 LUFS, LRA 22.1, sample peak 1.202 (float stem sum). 6-20 kHz share -24.6 -> -25.1 dB. Violins I stem 6-20 kHz share -21.0 -> -22.9 dB, Violins II -23.6 -> -26.7.
- **Attack probe:** 0 late or holes. Every one of the 36 files sounds. State guard after the final build: 1 stale (Trombone 2), rebuilt in full, then 0.
- **REAPER memory:** 45 GB before the render (0 compressed), 46 GB after (0 compressed).
- **Lock:** 15:40:33-16:38:10, 58 min. The scherzo actor held it until 15:40. Start and settle 12 min, CTRL range 4 min, T1 build 1 min, T1 range 5 min, final parts and build 9 min, stale-track rebuild, restart and settle 14 min, render 10 min.

| target (ruling) | c23 | c24 | goal |
|---|---|---|---|
| celli half notes 40-104 / 600-664, back - front median, n over +4 (5) | +2.6, 12 | +2.9, 11 | +2 or less (not met) |
| master 100-400 Hz back - front 612-628, worst (5) | +9.0 | +6.3 | +3 or less (not met) |
| master peak after the beat, qn 4 / 16 / 20 / 584 / 1104 (2) | +275 / +375 / +275 / +425 / +375 ms | +175 / +225 / +175 / +325 / +275 | about 150 (partly) |
| Violins I 2-5 kHz front - body, qn 16 / 584 (2) | -7.1 / -3.5 | -0.4 / +0.5 | not brighter than body (met) |
| brass / wind dips before 888 (4) | Hn 4.7/2.2/1.7/2.2, Tpt -1.0/3.7/3.5, Tbn 4.1/2.7, Tuba 5.1, Ob1 5.5, Cl1 5.3, Bn1 2.5 | Hn 3.1/6.8/1.7/4.5, Tpt 1.6/7.2/6.9, Tbn 4.3/4.1, Tuba 6.4, Ob1 8.7, Cl1 9.0, Bn1 6.0 | 5 or more on brass (partly: Horn 1, Horn 3, Trombones, Trumpet 1 under) |
| Trombone 1 accent 2-5 kHz - body, 985 / 993 / 1001 (8) | +10.9 / +5.7 / +8.6 | -1.3 / -4.7 / -6.2 | 0 or less (met) |
| master 2-5 kHz jump at 993 (8) | -1.0 (A: +2.8) | -0.7 | +2 or less (met) |
| Violins II 511 / celli 952 at +0.1..0.2 s re body (9) | -13.8 / -21.2 | -5.5 / -3.9 | within 3 dB (celli nearly, Violins II not) |
| Horn 3 - Horn 4 936-948 (7) | -8.0 | -3.4 | -1 to -3 (0.4 short) |
| Oboe 1 - Clarinet 1 568-576 (7) | -1.2 | -1.4 | -4 to -5 (not met; range T1 at +2 dB read -7.8) |
| Clarinet 1 - Bassoon 1 481-484 (7) | -0.5 | -5.6 | -4 to -6 (met) |
| Trombone 2 - Trombone 1 888-891.7 (7) | +3.9 | +0.8 | level (met) |
| upper winds - brass 888 / 1048 / 1108 (7) | -9.1 / -10.0 / -11.1 | -6.8 / -8.0 / -8.9 | about -8 (met) |
| Trumpet 3 accented - plain 1016-1048 (7) | +0.5 | +0.5 | +2 to +3 (not met) |
| basses' pedal re-bow rises 170.9 / 181.7 / 190.5 (6) | +17.8 / +3.9 / +11.4 | +9.8 / +7.5 / +10.2 | flat (not met) |
| legato holes 200 ms, Fl1 / Fl2 / Ob1 / CA / Cl1 / Bn1 / Hn1 / Vc (12) | 2 / 2 / 1 / 1 / 0 / 0 / 0 / 9 of 112 | 2 / 3 / 1 / 1 / 0 / 0 / 0 / 2 of 78 | (celli: 352 and 876 no longer listed) |

## Range pass (under the lock)

CTRL is the c23 project as saved. T1 is the c24 data with marcato chords A/B (bars 1-2 top layer v111, bars 5-6 middle layer v92), the celli bass-line spans on "Detache", and everything else. Both use the same starts: -3, 263.25, 455.75, 535.25, 839.5. Each start is where the measured tracks are silent and have a keyswitch before their first note (`rstart.py`).

- **Marcato chords.**
  - On Violins I the peak came +225 ms at qn 16 (CTRL +475). The middle layer put the 2-5 kHz front at body level (-0.4 / 0.0 dB), where the top layer put it +3.1 / +6.7 dB over.
  - On Violins II, Violas and Celli the held chords started 13-25 dB under their peak and peaked +375-575 ms.
  - Adopted on Violins I only, at velocity 92.
- **Celli bass line.**
  - Correction: by an error in the toggle, T1 played *both* statements on "Detache", not one on each row.
  - Detache: the ff statement (600-664, v91) was flat (median -0.4 dB, every note -3.8..+1.6). The f statement (40-104, v83) swelled 9-23 dB on three notes.
  - "Sus MAX" was not range-tested. It was adopted on the critic's (a) and measured only in the full render: no gain per note (above).
  - The celli Detache release groups ("1V mp" / "1V ff", 700 / 528 ms) were capped to 300 / 150 ms for the test (the coordinator's scherzo note).
- **Celli sags (A #2).**
  - 352 6.0 dB -> no longer listed, 876 8.1 -> 4.7: kept.
  - 286 8.3 -> 9.8 dB: back to its c23 row.
  - 860 fixed, but the legato note after it (864) opened a 14.6 dB hole: back to its c23 row.
- **Horn 3 CC1 +12:** -8.0 -> -3.4 dB under Horn 4. Adopted.
- **Oboe 1 +2 dB (k 33):** -7.8 dB under the clarinet, so +3.5 was written. The full render read -1.4: the range result did not transfer. Open.
- **888 lift:** the T1 dips equalled CTRL. The c18 chorale breath rows (`gap_set` from 888) had reset the gap. Fixed with `skip_at` 888; the full render shows the 0.08-0.10 s gaps.
- **Range variance:** 1562 of 2508 notes within 0.5 dB, CTRL against T1 (`logs/T1_eq.log`).

## Changes (files and values)

- **Ruling 1 (CC11 law, B #2):**
  - `tools/instr_post.py`: new key `cc_scale_k` and a corrected comment (20 log10 on brass and clarinets). `loop/LEARNINGS.md` line 352 corrected.
  - `build/score_config.py` c24 block: `cc_scale_k` 20 on Horns 1-4, Trumpets 1-3, Trombones 1-2, Bass trombone, Tuba, Clarinets 1-2.
  - Rows that were planned as dB keep their dB, now at k 20, so each delivers twice what it did:
    - fp of bar 209 (832.75): Horn 1 -1.5, Horn 2 -3.5, Horn 3 -1.5, Horn 4 -3.5, Trombone 2 -1.5, Tuba -5.0, Clarinet 1 -7.0, Clarinet 2 -5.5;
    - sub. p of bar 219 (871.2): -4 on Horns 3-4, Trumpets 1-3, Trombones 1-2, Bass trombone;
    - unison of bar 138 (547.5): Horn 3 +10.5, Horn 4 +7.5;
    - Horn 1 264-300 +4 and its final chord -3.5 (1107);
    - Horn 3 328-344 -2;
    - Horns 3-4 844-857 +3;
    - Trombones 1-2 791-815 +2 / +1.5;
    - Clarinet 1 328-344 +3;
    - Clarinets 1-2 600-680 +3.
  - Rows whose delivered level was fitted or confirmed keep their lane (dB halved at k 20):
    - counterstatement rows 103.5 / 103.7: Horn 3 +1.6 -> +0.8, Horns 3-4, Bass trombone, Tuba -2 -> -1;
    - muted Trumpet 1 at 679.7: +2.5 -> +1.25;
    - Horn 4's fill at 171.
  - Accent sizes (`amt_rel`) were fitted on measured medians and are unchanged, apart from Trumpet 3.
  - Checked, not changed: woodwind and string KS Masters. CC11 also switches their layers (start-mode ranges read from the oboe and 1st Violins .oib), so their fitted k values stay.
- **Ruling 2 (C #1):**
  - `ART_SPANS` Violins I "Sus Marc LITE" at qn 0, 4, 16, 20, 372, 584, 1104. qn 1088 is printed tremolo and stays on its row.
  - Velocity 92; `onset_lead` 0.085 s; no CC11 accent bump (new accent key `skip_rows`).
  - `cc_shape` `from_note` moves the ff step of 16 / 584 to the moved note-on (+17 / +19 units from -0.06 s).
  - mix.json Violins I `region_gain_db` {"rows": ["Sus Marc LITE"], "groups": [" f", " mf", " p"], "all_db": 4}.
  - Brass "Marc Sus LITE" was not tried.
- **Ruling 3:**
  - `tools/deliver_master.py`: mix.json `deliver` `top_above` (env `DELIVER_TOP_ABOVE`). mix.json `deliver` `top_above` -6, `ratio` 1.8 -> 2.1.
  - `RIDE_TRIMS`: chorale row `[892 0, 893 +3, 899.5 +3, 901 0]`; AirPods rows +2 dB on 680-720 and 384-392.
  - After the render, re-delivered on the c24 master (variant g): bar 223 arrival -5.0 -> -7.4 with bars 221-222 -5.0 -> -5.8; bars 261-262 -2.5 -> -3.3; a new row -2.0 dB on bar 263.
- **Ruling 4:** `INSTR_POST note_end` `gap_next_s` at 888: 0.10 s on Horns, Trombones, Bass trombone, Tuba, Trumpets 2-3; 0.08 s on Trumpet 1, Oboes, Clarinets, Bassoons, Contrabassoon. The c18 breath `gap_set` rows now skip 888. The 6 dB master-dip target is dropped.
- **Ruling 5:**
  - `_C15_SPANS["Violoncellos"]` adds (40, 72), (72, 104), (600, 632), (632, 664) on "Sus MAX" (env `C24_VC`).
  - Celli 352 / 876 on "Sus MAX", lead 0.307 s (c23 lead + 0.06), 0.03 s overlap (`gap_set` `allow_leg`).
- **Ruling 6:** `HP_SOFT_ACC_SKIP` takes `(qn, track)` (`tools/score_to_parts.py`); `(164, "Double basses")` removes the 2.5 dB release ramp inside the pedal. The re-bow swell was not treated (no interleaved-instance tool here).
- **Ruling 7:**
  - Horn 3 CC1 +12 (`note_cc` add, 935.6-947.75). Horn 3 CC11 +4.0 dB at k 20 (as c23 delivered it). Horn 4 -1.5 at k 20.
  - Oboe 1 567.5-575.75 +5 -> +3.5 dB (k 33).
  - Clarinet 1 480.8-486 -5 dB (k 20).
  - Trumpet 3 accents `amt_rel` 0.20 -> 0.33.
  - Trombone 2 887.9-891.7 -3 dB (k 20).
  - mix.json woodwinds fff trims +2: Flute 1 -4.1 -> -2.1, Flute 2 -3.7 -> -1.7, Oboes 1-2 +5.3 -> +7.3, Clarinet 1 -2.6 -> -0.6, Clarinet 2 -4.8 -> -2.8, Bassoon 1 +4.1 -> +6.1, Bassoon 2 +7.6 -> +9.6, Bass clarinet +3.5 -> +5.5. The last three had no fff key; it was taken from ff.
- **Ruling 8:** Trombone 1 985 / 993 / 1001 on "Sus MAX" (velocity 103, as the generator gives the tongued neighbours); the pickups end 0.02 s before (`gap_next_s`).
- **Ruling 9:** `cc_shape` `from_note` Violins II 511 (+39 for 0.27 s), celli 952 (+45 for 0.217 s).
- **Ruling 10:** `BEAT_STRETCH` {375: 0.90, 451: 0.90, 167: 0.95} (+0.10 s). The basses' re-bow moved, so `space_rebows.py --write` and a second `score_to_parts.py` were run. No phrase arcs (c25).
- **Ruling 11:** mix.json Violins I high shelf 5 kHz -4 -> -6 dB; Violins II -4 dB (new).
- **Ruling 12:** `holes24.py` uses 200 ms windows for Bassoon 1, Clarinet 1 and the celli.

## Rejected or deferred

- Marcato chords on Violins II, Violas and Celli: range test negative (above).
- Celli "Detache" for the bass line: flat at ff but 9-23 dB swells at f (range). Detache by velocity layer, or the f statement on "Sus MAX" with the ff statement on Detache, is the c25 candidate.
- Celli 286 / 860 on "Sus MAX": worse or moved the hole (range).
- AirPods rows: kept, since LRA stays 11.8.
- The 263 ride row's -0.3 refit (C): replaced by the summit refit.
- Basses' pedal re-bow swell: not treated (the interleaved divisi doubling of the scherzo / Movement II is not in these tools).
- Brass "Marc Sus LITE" (MANUAL-GAPS #1) and an oboe "Sus Accent MAX" (coordinator's scherzo note): not tried.

## Faults introduced or left

- Bar 263 over 262 on the mp3 +1.2 -> +0.6 dB: the summit refit lowered bar 263.
- Bar 113's stop 14.4 dB at +0.3 s, 0.1 under the 14.5 floor (c23 14.8).
- The celli bass line still swells late on each half note. "Sus MAX" did not fix it.
- Oboe 1 568-576 is still level with the clarinet.
- Horn 1, Horn 3 and Trumpet 1 dip only 1.6-3.1 dB before 888 (Horn 3 and Bass trombone have no note ending there).
- An error in the toggle sent both celli statements in range T1 to "Detache" (see the range pass). It does not affect the render.
