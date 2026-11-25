# Cycle 42 (series 2): changes

Inputs: critics A (articulation), B (balance), C (dynamics) on the c41 render, and the coordinator's notes (A #1-#3
first, with my own run of A's synthetic test before acting; B #1-#3 and C #2 simulated on the c41 stems; the leftover
CC7 lane; C #1 bar 62 with C's recommended fix; REP_TS optional; B #4 CC16 deferred to c43; the shared lock).
Snapshot: `cycles/c42/before/`. Scripts: `cycles/c42/actor_scripts/` (`c42check.py`: b1, b2, b3, c2, sub, f62, s1, on a
render, a folder or simulated stems; `c42joins.py`: A #1's pass criteria on pcX; `jf42.py`: join frames; `relfit42.py`:
the bar-62 release fit; `splice42.py`). Records: `c42check_final.txt`, `c42joins_final.txt`. New tool: `tools/pcx.py`.

Run (lock held 04:31-05:30; Movement II had it until 04:31):
1. Edits; parts.json regenerated and diffed (`cycles/c33/actor_scripts/pdiff.py`, envelope comparisons): tempo map
   identical; only the intended onsets, keyswitches, CC lanes and envelope spans moved (details below).
2. `reaper_ctl.py lock`, start, open; `build_reaper.py build/parts.json jobs --midi-only` (31 tracks MIDI-only; Violins I
   and II fully rebuilt: the Leg Port MAX row they used only in bars 55-61 is now unloaded). `reaper_ctl.py restart`; 33
   tracks; Mac Studio Speakers, no input, 48000 / 512.
3. `render_cycle.py 42` (no --force-memory: 0 GB compressed). Probe 0.
4. Main stem fix (Violas, Violoncellos), same data written (`--midi-only Violas Violoncellos`), `reaper_ctl.py quit`.
5. Second pass: start, `--pass2 open`, `build_reaper.py ... --midi-only --pass2` (5 tracks MIDI-only, "Violins I f62" /
   "Violins II f62" new), `--pass2 restart`, `render_cycle.py 42 --pass2` (7 instances, 40 stems summed). Probe 0. Alias
   release fit by stem fix and written (`--midi-only --pass2` on the two aliases); `--pass2 quit`; `unlock`.
6. Trumpet 1 splice (below), then `render_cycle.py 42 --measure-only` for the final metrics and mp3.

## Coordinator #1: did critic A's claim hold? (paragraph for the report to Dan)

Critic A's claim held. I repeated A's test on my own: for every legato join in the c41 render (128 viola, 263 cello,
262 first-violin and 142 second-violin joins) I built a synthetic note change between the same two pitches that switches
instantly on the beat, and measured it with each method. The method behind the c41 figure of 174-236 ms reported a
median of 15 ms (violas) and 44 ms (celli) of "both pitches sounding" on these perfect switches, with a quarter of them
reading more than 0.4 s, while on the violins it read 8-11 ms: below about 220 Hz each pitch's measuring band also holds
the other pitch's harmonics. With bands that leave out the other pitch's harmonics (`tools/pcx.py`, which reads 8 ms on
the synthetic switches), the real transitions last a median 94 ms on the violas, 98 ms on the celli, 82 ms on the first
violins and 97 ms on the second violins: the same length in all four sections, so there is no long viola or cello slide.
The spread of perceived attack times around each section's median (robust standard deviation) was 65 ms for the violas,
54 ms for the celli and 49 ms for both violin sections, with 37%, 28%, 24% and 24% of joins more than 60 ms from the
median; the old method had reported 117, 96, 66 and 87 ms (62%, 53%, 35%, 49%), and it put 28-29% of the perfect
lower-string attacks more than 60 ms off. After this cycle's per-note lead refit the violas are at 59 ms (30% more than
60 ms off) and the celli at 48 ms (22%); the violins were not refitted and measure 52 / 46 ms on their main tracks.

## Accepted

- **A #1, the estimator (tool, generic).** `tools/pcx.py`: perceived attack ("pcX", the m37 t50 / h10 rule unchanged) and
  the both-within-6-dB window on harmonic bands with every bin within 2 FFT bins of any harmonic of the other pitch left
  out; FFT 2048 when at least 2 harmonics of the measured pitch survive, else 4096, else 8192; `synth_switch` for
  calibration. My check (`pcx.attack_m37` / `pair_window(exclude=False)` reproduce the old method), c41 render:

  | | Violins I | Violins II | Violas | Celli |
  |---|---|---|---|---|
  | old window, real / synthetic median (p75), ms | 94 / 8 (10) | 132 / 11 (58) | 164 / 15 (428) | 213 / 44 (399) |
  | exclusion window, real / synthetic median (p75), ms | 82 / 8 (8) | 97 / 8 (8) | 94 / 8 (8) | 98 / 8 (10) |
  | old pc: real robust SD (>60 ms off) / synthetic >60 ms off true 0 | 66 (35%) / 12% | 87 (49%) / 20% | 117 (62%) / 28% | 96 (53%) / 29% |
  | pcX: real robust SD (>60 ms off) / synthetic robust SD | 49 (24%) / 2 | 49 (24%) / 3 | 65 (37%) / 2 | 54 (28%) / 3 |

  `probe_attacks.py` now reads `probe.json` "legato" [[track, limit ms]] (limits 75 / 75 / 90 / 80 ms) and fails a string
  section whose pcX robust SD over all its monophonic legato joins exceeds it; it runs in every render (c42: 52 / 46 / 59
  / 48 ms, ok). The c37 refit, re-measured with pcX on c36 -> c37, moved pcX 0.89-0.98 s per s of lead (median ratio;
  celli 0.89, violas 0.92, Violins I 0.98, Violins II 0.87; 76-91% in the intended direction): the c37 note that the
  violas "do not follow leads" was the old estimator.
- **A #1, the refit (`build/leg_leads.json` "_c42").** Exposed joins (stem within 10 dB of the master over +0..0.3 s)
  more than 60 ms off the section's pcX median (celli +8, violas +23 ms) whose relative crossover agreed in sign by more
  than 30 ms: total = old + 0.6 x (pcX - median), change clamped +-0.12 s. 22 celli and 13 viola candidates; Violas 613
  left out (its c41 lateness was its own -6.8 dB notch; it reads +32 ms this render with unchanged data); six targets
  after eighths (celli 265.5 / 412 / 594, violas 76 / 368 / 428) did not move (held by `LEG_MIN_GAP_S` 0.10 s) and were
  set back. 19 celli + 9 viola leads changed; the 8 celli early fills on moved joins moved with them (pre_s + the lead
  change; `early_fills.json` "_auto"); the Violas 182 notch moved 0.168 qn with its spike. Result (c41 -> c42, main
  stems after the stem fix below): violas pcX robust SD 65 -> 59 ms, >60 ms off 37 -> 30%; celli 54 -> 48 ms, 28 ->
  22%. Every moved viola join and 17 of 19 celli joins came closer to the median (e.g. Violas 650.5 194 -> 73 ms, celli
  654 152 -> 28, 351 146 -> 48, 7.5 83 -> 21); celli 601 unchanged (64 -> 66) and **celli 266 moved the wrong way (162
  -> 221 ms later after +0.10 s of lead): revert it in c43** (lead 0.10 -> 0, its fill pre_s 0.10 -> 0). A's pass
  criteria: robust SD violas <= 50 / celli <= 45 not reached (59 / 48); moved joins further from the median: celli 266
  only; new dips >= 5 / bursts >= 3 dB on moved joins: Violas 81 (+3.7), 650.5 (+4.4), 673 (+3.2), celli 7.5 (dip 6.0),
  372 (dip 4.3 -> 5.1), 211.5 / 216 / 266 (+3.2..+3.8). Fixed by stem fix: Violas 81 / 650.5 notched on this render's
  spike frames (-2.5 dB; bursts -> +1.2 / +1.9), celli 7.5 filled (dip 6.0 -> 1.6, burst 3.3 -> 3.0); the +3.0..+3.8
  bursts left. Joins with fills or notches re-measured (`c42joins_final.txt`): celli 10 / 36 / 216 / 372 / 601 / 654
  dips -0.3..5.1, bursts -1.1..+3.2 (654 pcX -144 -> +34 ms); celli 72 still late (+194 -> +142 ms) with its old +6.8
  burst; celli 596 (c26 notch) unchanged; Violas 182 pcX -130 -> -48 ms, dip 3.0 -> -0.3, burst +1.9 -> -0.7. New dips /
  bursts on joins whose data did not change (celli 400 / 600 dips 5.1-5.2, celli 412 / 558 bursts +6.1 / +5.4, Violas
  439 dip 5.3) are render-to-render variance (B #4), left for the c43 CC16 cycle.
- **B #1** (`build/roles.json`): Horn 1 [583, 607] +2.5 -> -1.0, [183, 207] +2.5 -> +0.5; Violas [584, 606, +2, 0.5].
  Rendered (re M, A): Horn 1 at 586 / 588 / 590 -3.1 / -3.8 / -3.6 -> -6.1 / -6.5 / -5.9, violas -8.0 / -7.5 / -8.0 ->
  -5.5 / -4.1 / -4.0, celli -5.7 / -9.0 / -5.1 -> -5.0 / -8.1 / -3.9; Horn 1 the loudest stem nowhere in 584-606;
  exposition Horn 1 minus celli K median -1.3 -> -3.0 dB (A -1.4 -> -3.3); master 584-606 -0.3 dB K. Matches the
  simulation within 0.3 dB.
- **B #2** (`LEVEL_SHAPES` Violins I 36.3-39.45 up to +4, Violoncellos 35.9-39.9 down to -4): master K steps per qn
  35-40 +2.1 / -0.3 / +2.0 / -0.7 / +1.3 -> +1.0 / +0.8 / +0.8 / +0.3 / +1.2 (rises every beat); Violins I minus celli
  per half qn K -3.7..-8.7 -> -1.0..+1.6 (A +5.9..+7.9).
- **B #3**: Horn 4 453 fill and Bassoon 1 364 fill deleted, Horn 4 453 trim -2 (stepped). Horn 4 453.0-455.5 K re M
  -9.0 / -8.6 / -7.7 / -11.7 / -13.3 -> -14.3 / -14.3 / -11.8 / -13.6 / -15.2 (Violins I -7.4..-9.1 on top); Bassoon 1
  364 / 364.5 -3.2 / -3.4 -> -6.1 / -8.8 against Violins II -6.5 / -6.9.
- **C #2** (`LEVEL_SHAPES` Cor anglais): C's row gave +3.2 dB in simulation with the peak 1.4 dB over bar 6's; the
  crescendo's first half beat 1 dB lower as well (24.35-24.6 -1, 25.9 +2.5): swell 25.6-26.0 minus 24.1-24.5 +1.1 ->
  +3.8 dB (C's target 4), decrescendo to 28 -5.5 -> -7.6 dB, swell peak 1.4 dB over the bar-6 peak (limit 1.5).
- **C manual note**: the c36 CC7 test lane on Trombone 1 removed (`CC7_POINTS = {}`); Trombone 1 stem unchanged (per-bar
  median 0.00 dB).
- **C #1, bar 62 (Dan's S3): C's recommended fix.** The bar 55-61 forte phrase (score onsets 219-243.5) of Violins I and
  II plays on its own instances in the second pass, "Violins I f62" / "Violins II f62" (`ALIAS_TRACKS`, `_SUB62` =
  218.5-243.9; Violins I / II rest there, `TRACK_WINDOWS`; mix copied), so the forte's last eighth ends at its written
  end (244.0, was cut at 243.746) and rings under the p. Tools (generic): `build_reaper.vol_points` `SUBITO_SILENT_QN` (a
  track with no note on a subito mark or across it holds its level from the fall to TAIL_HOLD_LEAD_S before its next
  onset instead of falling), `LEADIN_HOLD` "alias" (before an alias's first note the envelope holds the value at that
  note's moved onset: a soft-decrescendo trim hold that ended at the source's next note had run on to the alias's first
  note, 2.3 / 3.5 dB low for 0.09 qn), alias key `"hold_lanes"` (CC11 / CC1 keep their value after the alias's last
  note-off; 549 / 674 CC11 points dropped), and `POST_SHAPES_S` (level shapes applied after the tail and subito holds;
  parts.json "vol_post"). Violins II's p note keeps c41's onset 243.776 (`entry_leads.json` -0.06: as an entry after a
  rest its lead was no longer capped). Checks: the alias envelopes equal c41's sources from the first onset to 243.776;
  the alias stems match c41's Violins I / II per 1 s frame over 219-243.5 (median 0.00 dB, p10 -0.24 / 0.00, p90 +0.34 /
  0.00). As rendered, the held forte exposed two things: the last eighth swells 4-6 dB in its final 0.1 s, and its
  release at forte bursts 8.0 / 11.7 dB over the note body for 30-50 ms (Violins II's C-sharp4 release then holds -8..-10
  dB for 0.5 s): master +9.1 / +6.4 / 0.0 / -6.6 dB at 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 s, max 20 ms frame +10.2.
  C's step 5 (burst check) applied as a fitted release (`relfit42.py`, `POST_SHAPES_S` on the aliases, one refinement on
  the simulated stems, cuts up to 12.6 / 14.9 dB in the first 0.15 s): level held at its own value to the note-off, then
  the fermata release's shape. Final, re -0.35..-0.15 s before the beat:

  | s re beat | -0.15..-0.1 | -0.1..-0.05 | -0.05..0 | 0..0.05 | 0.05..0.1 | 0.1..0.2 | 0.2..0.3 | 0.3..0.5 | 0.5..0.8 | 0.8..1.2 | 1.2..1.6 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | c41 | +3.1 | -1.0 | -4.5 | -7.8 | -10.2 | -13.0 | -15.2 | -15.3 | -12.9 | -11.9 | -13.0 |
  | c42 | -0.3 | +0.6 | -1.7 | -2.0 | -5.1 | -8.5 | -11.8 | -13.2 | -12.7 | -12.2 | -13.1 |
  | fermata release 679 | -0.7 | -0.6 | -1.5 | -3.2 | -4.8 | -8.4 | -13.0 | -16.1 | -21.4 | -30.4 | -39.9 |

  C's pass criteria: 0-0.3 s within 2 dB of -3.3 / -4.9 / -8.8 / -13.2 (met: -2.0 / -5.1 / -8.5 / -11.8); no 20 ms frame
  in -0.3..+0.05 s more than 2 dB over the reference (met: +1.2, c41 +4.7); from +0.5 s within 1 dB of c41 (met: within
  0.3); alias stems within 1 dB of c41 over 219-243.5 (met). The c41 hole under the p level (-15.3 at 0.3-0.5 s, then
  rising) is gone. The CC7 variant was not used (coordinator). Memory: the second pass settled at 18 GB with 7 instances.
- **Trumpet 1 splice (found by the per-bar check, no critic).** With identical notes, keyswitches, CC lanes and envelope,
  Trumpet 1 rendered 4-15 dB louder than in c39, c40 and c41 (which matched each other to 0.1 dB) on three Leg Slur MAX
  phrases, each from the first legato target after a held note to the keyswitch back to Sus Non Vib MAX: 275.29-284.1,
  451.28-456.0, 642.88-644.0 (re M at 276-280 -10.9 -> -4.9 dB A; at the bar-161 climax +4 dB). Its saved state was not
  rebuilt this cycle ("same"), so the cause is not known (render-to-render variance, MANUAL-GAPS #6). The stem takes c41's
  audio of the same data back over those spans (`splice42.py`, linear crossfades where the renders agree within 1.5 dB);
  now Trumpet 1 minus c41 per 0.5 qn median 0.00 dB, max 0.7 dB.

## Rejected or deferred

- **A #1 violins**: their 31 candidates wait for c43, now that the lower sections show the transfer (and with the CC16
  rebuild, where every fit gets re-measured anyway).
- **A #2 REP_TS (optional) deferred.** The manual (2021, "Repetitions") and the patch disagree with A's reading on the
  internal rate: the Basses / Violas KS Masters' row (Basses key 87; patch `tempo` 120, `tempoSync` true, elastique)
  follows the host tempo, but the manual describes about a dozen pulses in a little more than one second (about 10 per
  second; eighths at 126 bpm are 4.2 per second); the controller map lists "Repetition" CC69, "Repetition: Sustain"
  CC64, "Repetition: Reset RR" CC36. A one-note probe on the row is the first step (MANUAL-GAPS, Results c42). A's S1
  measure by the re-attack rise is adopted as a check (`c42check.py s1`): master band rise median celli 3.9 dB, basses
  3.7 (stems 7.4 / 7.8), the same as A's c41 numbers (no repeat data changed).
- **A #3** (viola divisi patches): lower priority, not done; the second pass has room (18 GB).
- **B #4** (CC16 round-robin reset): deferred to c43 with the per-mic width rebuild of both passes (coordinator). Its
  symptom is in this render: Trumpet 1 (spliced), celli 412 / 558 bursts, Violas 439 dip, Violas bar 110 +3 dB (436, c41
  notch), celli bar 41 +1.8 dB.
- **C #1 CC7 variant**: not used (coordinator).

## Measured state (c42 final: main stems + stem fix + Trumpet 1 splice + second-pass stems with the alias fit; 40 stems)

- Master (float stem sum): -16.9 LUFS, LRA 23.6 LU, true peak +2.3 dBFS, sample peak 1.306.
- Delivered `cycles/c42/mvt1-mockup-c42.mp3`: -19.7 LUFS, LRA 14.9 LU, TP -1.7 dBTP, limiter about 0.6 dB (top
  pre-limiter peak 378.73 s, -0.92 dBFS), p10-to-max span 19.0 dB.
- Delivered S max: 160 -11.4 > 122 -12.2 (+0.8) > 167-170 -13.3 > 26 -14.4; 140 -15.0, 117 -15.3, 158 -15.6, 131-134
  -15.7, 69-72 -16.2.
- Attack probe: 0 late or holes; legato pcX robust SD Violins I 52 / Violins II 46 / Violas 59 / celli 48 ms (limits 75 /
  75 / 90 / 80). Silent notes: only the two known false alarms (Trombone 1 552, Timpani 727). Every stem present;
  per-bar levels against c41 differ only where the data changed, plus the variance listed under B #4.
- REAPER: main project 22 GB at start, settled at 44 GB (0 compressed) before the render, 44 GB with 14 GB compressed
  after. Second pass (7 instances): 8 GB at start, 18 GB settled and after (0 compressed).
