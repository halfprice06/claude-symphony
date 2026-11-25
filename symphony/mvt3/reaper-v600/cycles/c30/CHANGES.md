# Cycle 30 (2026-11-18, last cycle): bassoon solo joins, bars 95-98 delivery ride, opening ff under bar 223, bar-166 stop, cor anglais F4

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c29 render), and the coordinator's rulings 1-6. Snapshot: `before/`. Scripts: `actor_scripts/`:
- `lock30.sh`: the whole locked sequence; `lockC30.sh`: quit and unlock.
- `jt30.py` (jt29 plus a bassoon group), `ana30.py` (per-note body levels), `dsim.sh` (delivery simulation).
- Copies of the c29 gates and measures.

Logs (`logs/`):
- `pdiff_vs_c29.txt`, `netdiff_vs_c29.txt`, `guard30_net.txt`;
- `dsim_base29.log`, `dsim_sim30.log`, `dsim_sim30_888.log`;
- `jt_c29.txt` / `jt_c30.txt`, `bn_notes_*`, `ca_*`;
- `deliv.log`, `dynsteps.log`, `stem_bar_diff_vs_c29.txt`.

Plus `phase.log` and `render.log` in this folder.

## For Dan

- **This is the version to keep.** Loudness is -14 LUFS and the final chord is still the loudest moment: 0.5 dB over bar 223, 0.7 over bar 263.
- **Bassoon solo, bars 116-119:**
  - The A at the mp climax of the phrase (bar 117) no longer sags. Its dip went from 7 dB to 1.4 dB, on the solo track and in the full mix.
  - The E flat in bar 119 is 4.6 dB louder than before. It is still about 5 dB under the next note, but its dip in the full mix is now 2.3 dB (was 5.1).
- **Bars 95-98** (the oboe solo, mf to p) were the softest music in the whole file. They are now 3.5 dB louder, between the levels of the other soft passages.
- **The opening ff chords** (bars 1 and 5) are 0.6-0.7 dB softer. The C-major arrival at bar 223 now clearly outranks them: 1.3 dB over, was 0.6.
- **The cut-off in bar 166** rings slightly longer: 16.5 dB drop, was 17.6, now inside the target band.
- **The cor anglais F (F4)** no longer drops 4-6 dB in its solo (bars 175-186) or anywhere else it plays that note. The F notes now sit within 1.5 dB of their neighbours. That pitch is 4 dB louder everywhere.
- **Nothing else was changed.** Everything else in the data is as in c29. A few single notes came out 2-4 dB different, as happens on every render.
  - The one you may notice: the bassoon's B flat in bar 116 is 4 dB louder than its neighbours this time. In c28 it was 6.5 dB over and in c29 it was level, with identical data.

**The whole run c16-c30, in short:**

On 11 Nov you asked to remove every per-note volume adjustment. Since then the level of each note comes from the instrument itself:
- **Controllers:** CC11 for dynamics, CC7 for passage levels and section balance.
- **Sample choice:** the plain sustain samples with a short crossfade where a legato transition dropped out.
- **Per-pitch gains inside the sampler** for notes that are weak in the library.
- **Delivery rides** over whole passages.

Envelope points fell from about 54,000 to about 6,000. The remaining fader moves are printed hairpins, fp / sfp, the cut-offs and the timpani roll shapes, and a gate checks this before every render.

Over the same cycles:
- Accents became weight rather than bite.
- The chorale's repeated notes and bar lines join cleanly.
- Wind and trumpet solos stand over their accompaniment.
- The muted trumpet and cor anglais stay together.
- The cut-offs ring for 15-17 dB.
- The delivered file meets the shared spec: -14 LUFS, final chord loudest, LRA 10.7, limiter 5.2 dB.

**Left for later** (details below):
- The opening chords are still string-heavy.
- Two trumpet accents in bars 91-92 speak late.
- One trumpet legato hole in bar 212.
- Every other repeat of the basses' ff repeated G arrives late.
- "Legato Slur Accent" is untested.
- The loud climaxes are squeezed within about 1.3 dB of each other by the delivery.

## Results (render 16:59-17:11)

**Delivered (`mvt3-mockup-c30.mp3`):** -14.0 LUFS, LRA 10.7 LU, true peak -1.2 dBTP, p10 short-term -21.4 LUFS, limiter 5.2 dB, room bed -60.0 LUFS.

**Shared delivery spec on the mp3:**
1. -14.0 LUFS and -1.2 dBTP: met.
2. Final chord -7.62 against bar 223 -8.14 (lead 0.52) and bar 263 -8.35 (0.73). Every other bar is at -8.5 or lower; bars 1 / 5 are at -9.5 / -9.4: met. 223 over 263: +0.2.
3. f -> ff +3.7 dB (mf -> f +3.4): met.
4. p10 -21.4: met.
5. Limiting 5.2 dB: met.
6. LRA 10.7: met (c29 10.8; C's simulation predicted 10.8).

**Ruling 6** was not needed: the final leads 223 by 0.52 LU, unrounded. Kept for the record: on the live 879.5 row, 888-891.5 from -8.8 to -9.3 gave +0.6 and 223 over 263 +0.0 on the c29 master.

**mp3 stops at +0.3 s:**

| bar | 2 | 6 | 94 | 113 | 166 | 204 | final |
|---|---|---|---|---|---|---|---|
| c29 | 16.3 | 15.8 | 17.0 | 15.3 | 17.6 | 16.0 | 15.7 |
| c30 | 16.4 | 15.9 | 16.9 | 16.7 | 16.5 | 16.0 | 15.7 |

- All stops are in 14.5-17 dB.
- Bar 113 is 1.4 dB deeper. It is render variance before the cut: Violins I's last note is +5.7 dB and Trumpet 1's -5.4 dB over the last 0.15 s, with identical data, and the master stop went 15.9 -> 17.6.

**mp3 bar medians** (c29 -> c30):
- bars 95-98: -29.4 / -24.6 / -26.3 / -29.1 -> -25.9 / -21.1 / -23.5 / -25.5;
- bars 1 / 5: -9.1 / -9.2 -> -9.8 / -9.9;
- bar 50: -26.0 (now the softest bar, printed pp).

**Master:** -19.2 LUFS, LRA 24.0, sample peak 1.161 (float stem sum).

**Attack probe:** 0 late or holes.

**REAPER memory:** 46 GB settled before the render (0 compressed); after it 46 GB, 14 GB compressed.

**Lock** (the coordinator ran `lock30.sh` / `lockC30.sh`):
- Attempt 1: 14:34:47-15:01:34, 27 min. Midi-only build, with the Cor anglais fully rebuilt; saved; state guard 0 stale. It stopped at the disk gate (27 GB free) and quit / unlocked. The coordinator then deleted the c25-c26 stems; the masters are kept.
- Attempt 2: 16:33:54-17:12:49, 39 min. No full rebuild was needed (the state was already saved); state guard 0 stale; 34 GB free; render 12 min.

### Ruled targets (c29 -> c30)

| target (ruling) | c29 | c30 | goal |
|---|---|---|---|
| Bassoon 1 464: stem / master dip (1) | 7.0 / 7.2 | 1.4 / 1.4 | 4 / 3 (met) |
| Bassoon 1 475: stem / master dip (1) | 10.5 / 5.1 | 7.7 / 2.3 | 4 / 3 (master met, stem not) |
| Bassoon 1 475 body: level / minus 476 (1) | -56.4 / -10.5 | -51.8 / -5.2 | within 4 of 476 (not met; +4.6 dB) |
| Bassoon 1 466 / 476 stem dip (1) | 1.5 / 6.9 | 3.1 / 7.4 | 4 or less (466 met, 476 not) |
| Other notes in 456-496 within 1 dB (1) | | all 0.0..0.2, except 462 +4.1 (render variance, see Faults), 464 +1.7, 476 -0.7, 477 +5.6 (now level with 476) | |
| mp3 bars 95-98 (2) | -29.4 / -24.6 / -26.3 / -29.1 | -25.9 / -21.1 / -23.5 / -25.5 | C sim -25.9 / -21.1 / -22.6 / -24.7 (met) |
| 223 over bars 1 / 5, momentary max (3) | 0.8 / 0.6 | 1.4 / 1.3 | C sim 1.3 (met) |
| bar 166 mp3 stop (4) | 17.6 | 16.5 | 15.5-16.8 (met) |
| cor anglais F4 body 696 / 701 / 734 (5) | -49.6 / -50.4 / -48.6 | -45.6 / -46.9 / -45.1 | |
| F4 minus mean of its neighbours (5) | -2.4 / -4.5 / -4.1 | +1.6 / -1.2 / -0.7 | within 2 (met) |
| master dip 701 / 734 (5) | 3.3 / 3.0 | 3.5 / 2.6 | under 2 (not met) |
| other cor anglais F4 notes (5) | 606 / 625.5 / 636 / 644 / 654 / 868 | +3.8..+4.0 dB each | 868 -38.0, between 866 -41.2 and 871 -34.6 |
| trumpet minus cor anglais per note, 680-728 (5) | +0.9..+4.7 | identical | no F4 in the unison; Trumpet 1 never doubles an F4 |

On the cor anglais master dips: the window dip still holds the G4 -> F4 change of attack, but the F4 note bodies are fixed.

## Gates (before the lock, on the final parts.json)

- **pdiff against c29:** only Bassoon 1 changed: 6 notes, 4 key switches, one envelope point moved by 0.14 dB. The Cor anglais change is in the Opus state, not the MIDI.
- **Net-level diff against c29:** 0 spans, also at 0.3 dB / 0.05 qn. Only the ruled spans move, and those are in the delivery and the patch state, not in the faders.
- **In-note net gate:** entry 13 / inside 2 / inside_dyn 4 / entry_hp 115 / inside_hp 146, identical to c29.
- **Delivery simulation on the c29 master** (`dsim_sim30.log`): -14.0 LUFS, LRA 10.8, TP -1.2, p10 -21.4, limiter 5.2. The baseline run reproduced the c29 delivery exactly.
- **Stem per-bar diff after the render** (`stem_bar_diff_vs_c29.txt`): moves of 1.5 dB or more appear only on:
  - ruled spans: Bassoon 1 bar 116; cor anglais bars 160 / 162 / 164 / 175 / 218, which are F4 notes;
  - single notes that also varied c28 -> c29 with identical data: Flute 1 106-107, Bass trombone 103, Violins II 133, violas 265, Bass clarinet 33, Horn 1 21 / 217, celli 89 / 261-262, Trumpet 1 113.
## Changes (files and values)

- **Ruling 1 (`build/score_config.py`):** `_C26_RUNS["Bassoon 1"]` weak targets (459, 460, 499, 507) -> (459, 460, 464, 475, 499, 507): variant C puts 464 and 475 on "Sus MAX" (ART_SPANS +-0.1 qn), leads them 0.06 s (`onset_lead` set, Sus rows) and overlaps the note before by 0.011 s (`gap_set` only_at). In the c26 "bn" block 464.0 left `_bnq` (its 0.06 s lead and the Leg v100 cap) and the `note_end` entry 463.678 was removed. parts.json: 464 v100 -> v63 (mp), 475 v100 -> v53 (p), both at 463.832 / 474.832 with key switches to Sus MAX at 463.772 / 474.772 and back to Leg Slur Exp at 465.94 / 475.94; the notes after (466, 476) now start on the beat (they had led 0.168 qn), v63 / v53, as 461 after the 460 target. CC1 / CC11 / CC7 identical; one envelope point moved 466.168 -> 466.03 (0.33 -> 0.47 dB). Bassoon 1 MIDI-only.
- **Ruling 2 (`build/score_config.py`, c30 block):** `RIDE_TRIMS` row [(376.25, 0), (376.75, 3.5), (391.5, 3.5), (391.9, 0)].
- **Ruling 3 (same block):** rows [(0, -1), (8, -1), (8.25, 0)] and [(15.75, 0), (16, -1), (24, -1), (24.25, 0)] (rows add: bars 1-2 and 5-6 now -3.5 dB in all).
- **Ruling 4 (`build/mix.json` `return_rides`):** {"stop": 662.0, "db": 0.0} -> 1.0.
- **Ruling 5 (`build/mix.json`, Cor anglais):** `region_gain_db` [{"rows": ["Sus MAX", "Leg Slur MAX"], "pitch_db": {"65": 4.0}}] (EH KS Master: 30 sustain / RT regions per row plus 15 TLeg regions per interval into F4 on Leg Slur MAX; the "EH pp RT" regions keyed 65-66 also lift F sharp 4's pp release trail by 4 dB). Opus state change: Cor anglais fully rebuilt.
- Env switch: `C30_OFF="rides"` turns rulings 2-3 off; `C26_OFF` / earlier switches unchanged.

## Left for later (critics' measurements on the c29 render)

- Opening ff chords string-heavy (B #5): Violins I / II / celli at -23.6 / -22.0 / -23.8 dB against their own ff medians -29.7 / -29.9 / -31.1 (6-8 dB over); horns -28.6..-33.7 and low brass -28.1..-31.7 at their ff medians; section rel to the sum: violins -3.2, horns -10.9, low brass -8.9. Possible fix: a -3 dB role on Violins I / II and celli over the three chords (touches c24-c27 values, p10, LRA).
- Trumpets' ff accented quarters at 362 / 366 (A #3): body minus 3 dB reached at +100 / +120 / +140 ms (Trumpets 1 / 2 / 3); a lead of 0.035-0.05 s with the v82 pickups is untested.
- Trumpet 1 at qn 844 (A #4): 10 dB, 0.2 s hole on the Leg Slur MAX join C sharp 5 -> F5 (master dip 4.3); the sustain-row crossfade would need a CC refit (trumpets already 5-9 dB over the next stem).
- Basses' ff repeated G at 600-608 / 654-658 (A #5): 604 / 608 / 658 dip 11-13 dB; 602 / 606 / 630 / 656 rise over 0.25-0.35 s (250-350 ms late); a round-robin reset would move every later take.
- "Leg Slur Accent MAX" (MANUAL-GAPS #1): untested.
- Basses' pp re-bow holes: accepted.
- Delivered climaxes compressed (C left-for-later a): the 12 loudest bars lie within 1.3 LU; bar 223's in-bar step +2.8 LU against a master step of about +6.7 dB.
- Final crescendo 275-277 pre-duck (C b): needed for the limiter (removing the -1 dB at 1107.8 gave 6.4-6.5 dB).
- Cor anglais at the sub. p of bar 219 (C c): -64..-67 dB, 4-12 dB under the other sub. p winds.

## Rejected or deferred

- Ruling 6 (the 888 row): not needed (lead 0.52).
- Ruling 1's 475 note: kept, though its stem target was not met. Its master dip passes and the note is 4.6 dB louder. The variant-C sustain row cannot lift it further, because the E flat 4 is weak on that row as well.
- The cor anglais pp release trail on F sharp 4 also takes +4 dB, because the region is shared with F4 (65-66). This is inaudible: F sharp 4 occurs at 871 only, at f.

## Faults introduced or left

- Bassoon 1's 462 (bar 116) plays 4.1 dB louder than in c29 (-40.5 against neighbours -47..-48) with identical data. It was +6.5 dB in c28 and level in c29: one round-robin take of that note varies between renders.
- Bassoon 1 475 / 476 stem dips 7.7 / 7.4 (master 2.3 / 3.9).
- Bassoon 1 466: its master dip went 3.9 -> 6.0. The note's own level is unchanged; the measure's "before" window now holds the louder 464.
- Cor anglais master dips 701 / 734: 3.5 / 2.6.
- Bar 113 stop: 16.7 dB, render variance, inside the band.
