# Cycle 43 (series 2): changes

**For Dan (what to listen for in c43).** This cycle is mostly about notes landing together on the beat (your note S2).
- **Violins and violas:**
  - the first and second violins now start their phrases together at letter G (bars 117-120, the upbeats into each bar) and in the fugato entries (bars 94-96);
  - the violins' tune of bars 55-61 and the violin lines of bars 64-65, 135-141 and 162-165 move more evenly from note to note;
  - the violas' A-flat in bar 20 is now slurred into, as printed.
- **Winds and brass:**
  - the second horn now moves with the first clarinet in their bars 56-67 duet, where it used to trail by up to a tenth of a second;
  - the bassoon solo of bars 33-34 and the bass-clarinet solos of bars 107-109 no longer drag;
  - the bass clarinet's soft notes in the opening (bars 1-3) and in the coda (bars 177-178) no longer swell up after the beat.
- **Opening and stringendo:**
  - in the opening motto (bars 1-3) the double basses no longer arrive late on the rising steps and early on the falling one;
  - the second violins' and violas' tremolo chord changes in the stringendo (bars 111-115) and at bars 41 and 78-80 are no longer an eighth early.
- **Balance:**
  - bars 70-71: the closing tune (flutes, first violins, oboe) now sits above the clarinet and horn counter-motif;
  - letter F (bars 98-102): the horns' and trombone's eighth-note answers can now be heard under the ff tune;
  - bars 56-59: the violins' cantabile tune is a little clearer above the clarinet and horn counter-melody;
  - bars 82-83 are less boomy in the bass.
- **New round-robin reset:** with it, the first horn's solo legato notes (bars 47-52, 147-154) and the first trumpet's (bars 69-71) came out 3-9 dB louder. They have been brought back to their earlier level, so they should sound as before.

Inputs:
- Critics A (articulation), B (balance) and C (tempo / timing) on the c42 render.
- The coordinator's priorities: timing on pcX first, balance second, then the CC16 reset; accents and Repetitions TS optional.

Snapshot: `cycles/c43/before/`.

Scripts (`cycles/c43/actor_scripts/`):
- `edit_leads43.py` and `edit_fills43.py`: the per-onset tables;
- `simb43.py`: B #1-#4 checks, on renders or on stem_fix folders;
- `bclfit43.py`: dip-and-swell level shapes;
- `statefix43.py`: per-note contours back to an earlier render's levels;
- `joins43.py`: legato joins of two renders on pcX, split into unchanged and refitted joins;
- `bars43.py` and `notediff43.py`: per-bar and per-note changes between renders;
- `eval43.py`: moved onsets against their beat reference.

Records: `joins43_c42_c43.json`.

Critic C's scan data was used (`s2rows*.json`, `tables.py`) and deleted at the end, as the coordinator asked.

Run. The lock was held 08:03-08:55. Before that, Movement II, a Movement III port and the scherzo port held REAPER from 06:21.
1. Edits, parts.json regenerated and diffed (`cycles/c33/actor_scripts/pdiff.py`, a keyswitch / same-pitch check, the new lead warnings) and level changes simulated on the c42 stems (`tools/stem_fix.py --out`). Tempo map unchanged.
2. Main pass:
   - `reaper_ctl.py lock`, start, open;
   - `build_reaper.py build/parts.json jobs --midi-only`: all 33 tracks MIDI-only; no Opus state changed, so no full rebuild;
   - `reaper_ctl.py restart`: 33 tracks, Mac Studio Speakers, no input, 48000 / 512;
   - `render_cycle.py 43`. Probe 0.
3. Main stem fix (Horn 1, Trumpet 1, Violas, Trombone 1, Horns a2; below). The same data was written with `--midi-only` on those 5 tracks, then saved, then `reaper_ctl.py quit`.
4. Second pass:
   - start, `--pass2 open`;
   - `build_reaper.py ... --midi-only --pass2`: 7 tracks MIDI-only;
   - `--pass2 restart`, `render_cycle.py 43 --pass2`: 40 stems summed, probe 0;
   - no pass-2 stem fix needed;
   - `--pass2 quit`, `unlock`.

## Accepted

### S2 timing (critics A #1-#3, C #1-#5), all measured with tools/pcx.py

**Tables.** Applied by `edit_leads43.py` and `edit_fills43.py`; values are critic totals and offsets in seconds.

*build/leg_leads.json "_c43" (legato leads):*
- **Violins (C #2's 30 joins at 0.8).**
  - Violins I: 21 joins; Violins II: 5 joins and 4 on the "Violins II f62" alias (230 / 231.5 / 239.5 / 242).
  - C had already removed the joins that read on time in c41 with identical data (Violins I 67 / 97, Violins II 257.5 / 260 / 644).
  - Critic A's 23 + 8 list agrees in sign on every one of them.
- **Winds and brass.** A #1, plus C #3 where both list a join, at the smaller value:
  - Flute 1, Oboe 1, Cor anglais 24 / 684, Clarinet 1 215 / 247, Bass clarinet 425 / 435.5;
  - Bassoon 1: the 131-135 solo, 366, 413, 575.5;
  - Horn 1: 50, 171, 188, 195, 419, 420;
  - Trombone 1: 521, 700, 710; Trombone 2: 710;
  - the Trumpets a2 joins 665 / 673, keyed under Trumpet 1, which the alias inherits.
- **Horn 2 duet (bars 56-67).** Measured per join against Clarinet 1 on c42; the lead was set where both pcX and crossover trail the clarinet:
  - 226 / 227 / 239 / 239.5 / 240 / 246 / 249 / 262 at +0.03..+0.06;
  - 266 left out: its crossover is on time and the late reading is the note's bloom.
- **Slow sections (C #1):**
  - Double basses: 4 +0.11, 7.5 -0.11, 10 +0.12;
  - Violas: 496 / 501 -0.17, 600, 684, 696, 712;
  - Violins I 496 / 708; Violins II 36 / 39; celli 44, 183;
  - celli 266: removed.

*build/entry_leads.json "_c43":*
- **A #2 (Violins I phrase-first notes):** the six letter-G upbeats 464.5-478.5, plus 372.5, 380.5, 72.5; extras +0.03..+0.05 on the 0.06 s loud entry lead.
- **Violas** 360 / 569.5 and **celli** 324 / 552 (A #2, at the value both critics agree on).
- **C #3 / #1:**
  - Bassoon 1 316.5 / 360 / 516 earlier;
  - Flute 1 432;
  - Violins II 472.5, 372, 20;
  - celli 3 / 20 lowered;
  - Horn 1 49.

*New build/retongue_leads.json (re-attacks, C #3 / #1):* 49 onsets, and C #4's tremolo onsets, checked here on the c42 stems:
- **Stringendo chord changes (Violins II 444-460).** The crossover of each moving voice and pcX agreed that they were early by 0.05-0.3 s: -0.07..-0.12.
- **Violas 160 / 308 / 316:** the same, -0.10..-0.12.
- **Tremolo entries** Violins II 148 / 304 / 440 and Violins I 664: +0.06..+0.08.
- **Not changed:**
  - the sul tasto tremolo of 588-616, where the two estimators disagree (crossovers saturating at +-0.3 s);
  - `TREM_JOIN_LEAD_S` / `TREM_ENTRY_LEAD_S`: a global change would make the already-late sul tasto joins later.

**Tools (generic, `tools/score_to_parts.py`).**
- **`RETONGUE_LEADS`** (C #3), from `build/retongue_leads.json`: per-onset lead offsets for re-attacks.
  - The offset is added to whatever lead the note gets; a note with no lead path gets one.
  - The note or chord before it gives way, so played gaps and overlaps keep their length and nothing overlaps into the same pitch.
  - The CC11 falls on that note move with its end.
  - parts.json `retongue_extra`.
- **`LEAD_WARN_S`** (C #5): a "LEAD WARNING" for every listed leg_leads / entry_leads / retongue_leads onset whose realised lead differs from the requested one by more than 0.02 s, or whose note takes another path; parts.json `lead_short`.
  - On the c42 tables it listed 43 absorbed leads, among them **celli 266** (requested 0.32 s, realised 0.221 s) and 351 (0.24 / 0.179).
  - Through this cycle's edits it found that:
    - the six "held" slur-head targets and the Violins II f62 230 / 231.5 were held by the 0.75 lead cap of the eighth before them, not by `LEG_MIN_GAP_S`;
    - 13 entries keyed on notes the pipeline plays as re-tongued slur heads or SLUR_START_SUS joins had never acted. Among them are critic A's Flute 1 115 / 395, Clarinet 1 507, Bass clarinet 435, Bassoon 1 131 and Horns a2 313; those went into `retongue_leads.json` instead.
- **`MERGE_SLUR_OUT`** (A #3): a slur's last note merged with a same-pitch note that starts the next slur keeps its own slur and takes the next one as `slur_out`.
  - Violas qn 78 (bar 20) is now joined from 76 as printed: velocity 124, no phrase-start CC1 dip.
  - This was the one such merge in the score; no other note changed.

**Caps (score_config c43).** `LEG_CAP_FRAC` "listed" raises, on listed onsets only:
- Horn 2 220-268 and Horn 1 418-421: 0.75 (joins after eighths);
- Violas 428, celli 594, Violins II f62 230 / 231.5: 0.95.

**Celli 266 (A #3, C #5):** lead entry removed and its early fill's pre_s 0.1 -> 0.0. The lead never moved the note.

**Fills, notches and shapes moved with their notes.** The 12 early fills on moved joins: pre_s += d, hold_s -= d. Also moved by the note's realised change:
- 7 `JOIN_NOTCH` rows: Flute 1 395, Oboe 1 315.5, Clarinet 1 507, Bassoon 1 131, Horn 2 249, Trombone 1 700, Violins I 267;
- the Cor anglais 23.7 shape;
- 4 `LEVEL_SHAPES_S` rows: Cor anglais 684, Clarinet 1 422 (the bright-state front cut), Violins II 564, celli 3.

**Bass clarinet (C #1 step 2).** The soft joins 4 / 10 / 708 / 710 change pitch on time, then swell 3-8 dB at +0.2..+0.4 s.
- Level shapes were fitted on the c42 stem (`bclfit43.py`) to the line between the two note bodies.
- 50 ms level against that line over -0.1..+0.5 s: c42 -4.7..+7.7 dB; c43 render -1.1..+1.2 dB.

**Results (c42 -> c43; reference = the beat median of the other tracks on that onset, as critic C used).**
- **All 162 moved onsets:**
  - 140 closer to their reference, 9 further, 13 about the same;
  - median distance 89 -> 35 ms; more than 60 ms off 130 -> 37;
  - pcX moved 0.98 s per s of added lead (median).
- **Probe legato robust SD** (Violins I / Violins II / Violas / celli): 52 / 46 / 59 / 48 -> 43 / 40 / 50 / 48 ms.
  - A's violin targets (45 / 42) are met; on the violas, half of the gain is unchanged joins (round robins, below).
  - Every refitted string join came closer to its section median: Violins I 22 of 22, Violins II 7 / 7, violas 7 / 7, celli 3 / 3, basses 3 / 3.
- **Violins II f62:** robust SD 73 -> 28 ms. Shared alias onsets more than 60 ms apart: 5 -> 4 of 17 (A: at most 2). Left: 225 (-161), 236 (+108), 231 (+69), 234 (-64).
- **Letter G, Violins I minus Violins II** at the six upbeats: +79 / +88 / +116 / +77 / +82 / +66 -> +34 / +72 / +31 / +94 / +60 / +36 ms. A's target is +-30; 468.5 / 474.5 / 476.5 are left for c44.
- **Other phrase-first notes:** Violas 360 +77 -> +11, 569.5 +106 -> +55; celli 324 +118 -> +32, 552 +81 -> +31.
- **Horn 2 minus Clarinet 1** at 22 shared joins: median +24 -> +11 ms; over 60 ms: 6 -> 3 (240 +170, 266 +107 bloom, 261.5 -105).
- **Bass clarinet:** legato median +65 -> +43 ms (8 / 425 / 435 / 435.5: +84 / +64 / +101 / +75 -> +19 / +39 / +57 / +37).
- **Bassoon 1 solo:** 131 / 134 +99 / +55 -> +41 / +26; 135 +69 -> +73 (unchanged); 413 +153 -> +63; 575.5 +80 -> +111 (worse).
- **Tremolo:**
  - stringendo chord changes -96..-191 -> -2..-77 ms (453 -77 left);
  - Violas 160 / 308 / 316 -165 / -113 / -119 -> -46 / -14 / -4;
  - entries +83..+108 -> +29..+45.
- **Basses (Lento):**
  - 4.0: +148 -> +54, but its crossover is still +268 ms (C step 3: a fresh pp entry in c44);
  - 7.5: -125 -> -26; 10: +201 -> +84; 36: +218 -> +58.
- **Violas 78:** joined, but its new 0.225 s legato lead overshoots: +138 -> -63 ms (section median +27). For c44 a leg_leads offset of about -0.07.

### Balance (critic B), simulated on the c42 stems first

| Finding | Change | Simulated | Rendered c43 (final stems, A re M) |
|---|---|---|---|
| B #1 bars 70-71 | `LEVEL_SHAPES` tune +2 (Violins I, Flutes, Oboe 1), counter -2 (Clarinet 1, Horns a2) / -4 (Violins II), 275-284 | tune minus counter 276-283: +2.5 / +2.4 / 0.0 / -0.7 / +0.8 / +2.7 / -1.5 / -2.1 -> +3.9 / +4.8 / +4.2 / +3.5 / +4.9 / +7.1 / +2.6 / +2.4 dB | +3.5 / +5.1 / +1.7 / +5.9 / +5.5 / +7.1 / +2.4 / +3.0 dB; master K within +-0.5 |
| B #2 letter F | Horns a2 / Trombone 1 +3 over 388-406.5, `PICKUP_LIFT` +6 on the first eighths; 394.5 +0.5 (with +1.5 it rendered 3.0 dB over the next eighth: stem fix) | brass median -11.7 -> -8.3, tune minus brass +9.8 -> +6.2 | brass -8.1, tune minus brass +5.4 dB (B: 5-6); first eighths -10.8 / -13.7 / -6.4 / -16.2 re M (c42 -19.2 / -16.0 / -14.7 / -22.1), none over 2.2 dB above its neighbour |
| B #4 bars 56-59 | roles Clarinet 1 +3 -> +0.5, Horn 2 +2 -> +1 over 220-244 | violins minus counter K median +2.8 -> +4.4, beats with the counter on top 5 -> 4 | K median +4.0, counter on top 4 beats, Clarinet 1 minus Horn 2 +1.9 -> +0.5 |
| B #5 bars 82-83 | celli second `loud_eq` spec 100 Hz -4 dB 0.5 oct over 323.5-332, accepted after a complex-STFT EQ simulation | master 79-125 minus 157-397 Hz per 2 qn -2.0 / -3.0 / -1.4 / -2.0 -> -3.8 / -3.8 / -4.0 / -3.6 dB; 125-200 Hz body -0.03..-0.09 | rendered |

**B #3** (Trumpet 1 state and Horn 3 at 164; see CC16 below):
- Horn 3 minus Horns a2 over 164-165 is +2.7 dB A, 0.7 dB over B's +2 threshold, inside measurement noise; not trimmed.

### MANUAL-GAPS #6: the round-robin reset on CC16 (done)

**Confirmed before the change.**
- The 2025 HO manual (p.92) says the reset is sent on the CC entered as "Reset Controller" in Opus Preferences / MIDI / Round Robin. The 2021 manual's text says CC36.
- The Opus manual (p.29-30) has the Round Robin options "Reset Controller" and "Reset Note".
- `/Library/Application Support/East West/Opus/Preferences.json` has `RoundRobinResetCC` 16 and `RoundRobinResetNote` -1.
- No installed patch maps CC16 (the controller maps use 1, 5, 7, 10, 11, 15, 22, 36, 57, 64, 65, 68, 69, 70); in every KS Master CC36 is "Repetition: Reset RR".

**Change.** `tools/build_reaper.py` `RR_RESET_CC` is read from that preference file and sent at value 127 in the pre-roll next to CC36. This was MIDI only, so no track needed a full rebuild. The per-mic width rebuild (MANUAL-GAPS #4) was therefore not forced and waits for c45.

**Effect on joins whose data did not change (c42 -> c43, pcX).**

| Track | Unchanged joins moved >30 ms | Note |
|---|---|---|
| Violins I | 21 of 223 (9.4%) | |
| Violins II | 10 of 118 (8.5%) | |
| Violas | 8 of 121 (6.6%) | |
| Celli | 7 of 260 (2.7%) | |
| Violins I f62 / Violins II f62 | 0 of 17 / 1 of 13 | |
| Winds | 1-5% | Bass clarinet 6 of 16 from its new level shapes; Bassoon 1 6 of 40 |
| Horns 3 / 4, Trombone 2, Trumpets a2 | 0 | |
| Horns a2 | 2 of 23 | |
| **Horn 1** | **32 of 41 (78%)** | joins median +19 -> -34 ms |
| **Trumpet 1** | **11 of 15 (73%)** | joins median -11 -> -51 ms |

- **c42's own refit joins (19 celli, 9 violas):** 3 moved by more than 30 ms: celli 184 +63, celli 266 -57 (its fill revert), Violas 81 +42.
- The string figures are about the size of earlier render-to-render variance (c41 -> c42: 9.4% on the rebuilt Violins I). Whether renders now repeat can only be shown by c44 against c43.

**Levels (`notediff43.py`, `bars43.py`).**
- With the reset, the Leg Slur MAX legato targets of Horn 1 (bars 47-52, 103-106, 147-154) and Trumpet 1 (bars 69-71, 113-114, 161) rendered:
  - Horn 1: 1-9 dB louder;
  - Trumpet 1: up to 14.5 dB louder (the c42 "loud state");
  - the 2-5 kHz share moved both ways (other takes, not a louder layer).
- The phrase starts and every other brass track kept their levels.
- Fixed on the stems with per-note contours back to the c42 levels (c42 = c41, the state the balance was fitted on; `statefix43.py`, "c43 stem fix" in score_config):
  - simulated per note within -1.5..+1.0 dB of c42 (median 0.0);
  - Trumpet 1 re M at 276-284: -4.0 / -6.6 / -8.1 / -6.4 before, -9.2 / -11.9 / -14.5 / -13.1 after (c42 -11.0 / -10.6 / -14.9 / -14.0).
- Violas 654.5 (+5.6 dB, c41 = c42) likewise.
- Two c42 outliers came back to c41's level by themselves: Violas 436, Clarinet 1 152.75.
- **Their timing (Horn 1 and Trumpet 1 joins about 50 ms earlier) is left for c44.**

## Rejected or deferred

- **A #4** (Marc Sus LITE accent test, second pass) and **A #5** (Repetitions TS one-note probe): optional; not done.
  - The probe needs an alias whose notes differ from its source (one held note instead of MEAS_TREM strokes), which the alias tool does not do yet.
- **MANUAL-GAPS #4** per-mic width rebuild: deferred to c45 (CC16 forced no full rebuild).
- **Horn 2 fills (A #1 step 3) and C #3's bloom cuts:** the line fit left -3.6..+3.0 dB on Horn 2 172 / 266 (pass +-1.5); not made.
- **Joins left out of the refit:**
  - the Cello solo's per-onset leads (C #1): the DIV A solo as fitted is on the do-not-touch list (A, c40-c41);
  - Violins I 707 (a pp espr. entry that needs a fill, not lead);
  - Violins I 271 (a `GROUP_LEAD_AT` note);
  - Violas 76 / 368 and celli 265.5 / 412 (heads at the cap; a head move is needed);
  - Horn 1 411.5 (estimators disagree).
- **C #6** (two Allegro "main" arcs to "sub"): not in this cycle's list.
- **Inert old entries (no effect, left):** Flute 1 397.5 / 555 / 633, Oboe 1 407, Cor anglais 275 / 281.5, Bassoon 1 523; and 30 partly absorbed string leads in the cap windows.

## For c44

- Compare every stem per note with c43 first (does the CC16 state repeat?).
- If Horn 1 / Trumpet 1 render in c43's state again: keep the contours and refit their legato leads, now about 50 ms early. If not, take the contours out.
- Timing carries:
  - Violas 78 (about -0.07);
  - letter G Violins I 468.5 / 474.5 / 476.5;
  - basses 4.0 as a fresh pp entry;
  - Bassoon 1 575.5 / 413 / 135; Horn 2 240;
  - the f62 225 / 236 / 231 / 234 pair;
  - tremolo 453.

## Measured state (c43 final: main stems + stem fix + second pass; 40 stems)

- **Master** (float stem sum): -16.9 LUFS, LRA 23.5 LU, true peak +2.3 dBFS, sample peak 1.306.
- **Delivered** `cycles/c43/mvt1-mockup-c43.mp3`:
  - -19.7 LUFS, LRA 14.9 LU, TP -1.8 dBTP, p10-to-max span 18.9 dB;
  - limiter about 0.5 dB (top pre-limiter peak 378.73 s, -0.95 dBFS).
- **Delivered S max:**
  - 160 -11.5 > 122 -12.2 > 167-170 -13.3 > 26 -14.4;
  - 158 -15.4, 117 -15.3, 140 -15.1, 131-134 -15.7, 69-72 -16.2 (c42 within 0.2 dB).
- **Attack probe:** 0 late or holes.
- **Silent notes:** only the two known false alarms (Trombone 1 552, Timpani 727).
- **S3 bar 62** unchanged: -1.9 / -5.1 / -8.3 / -11.7 dB at 0-0.3 s.
- **Per-bar master** against c42: -0.8..+0.6 dB.
- **REAPER:**
  - main project 23 GB at start; settled 44 GB (10 GB compressed) before the render; 45 GB (27 GB compressed) after;
  - second pass (7 instances) 9 GB at start, 18 GB settled and after (0 compressed).
