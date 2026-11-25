# Cycle 08: changes (actor, on the c07 render)

Snapshot in `before/`. Scripts in `actor_scripts/`: `mix08.py` (build/mix.json changes), `apply08.py` (roles, note trims,
pitch-trim skip, leg_leads), `spec08.py` + `eqsim08.py` + `var08.py` (EQ simulation on the c07 stem spectra),
`rolls08.py` (timpani low-end share over the rolls), `tail08.py` (who carries the final chord's tail), `notes08.py`
(notes with rows), `check08.py N` (the c08 checks; `check_c07.txt` is the baseline), `pcx_c07_solo_flute.json`.

STATUS: rendered 2026-11-09 (attempt 3); results in "Render attempt 3" at the end of this file.

## 1. ONE_TIME_c08

| item | status | change and evidence |
|---|---|---|
| 1 brightness | adopted | strings family 4.73 kHz +4 shelf removed (strings and strings_basses); brass shelf +4 -> +1; Violins I 5 kHz shelf -4 -> -6, Violins II 5 kHz -4 (new); critic C's 3 kHz -2 dB bell (1.5 oct) on both violin sections; gains given back from the simulated K-weighted loss: Violins I +1.83, Violins II +1.48, solo +0.44 dB (critic B's "about 0.9" was for the recipe without the 3 kHz bell). Simulated on the c07 stems (non-resonant shelves, as Movement I did; the template's 0.33-oct shelf modelled as an RBJ BW shelf overshoots +5 dB at 4 kHz): master 6-20 kHz -24.2 -> -29.7 dB, 2-6 kHz -8.4 -> -10.7 (targets -28.5..-30 / -10..-11) |
| 2 loud brass tone | adopted | brass family bells 475 Hz -5.4 -> -2.7, 821 Hz -7.8 -> -3.9, new 3.2 kHz -3 dB bell; trumpets' +2.5 dB 4 kHz shelf dropped; gains to keep loudness (simulated): Horn 1 -4.47, Horn 2 -3.49, Horn 3 -3.49, Horn 4 -3.89, Trumpet 1 -1.99, Trumpet 2 -2.85, Trombone 1 -2.97, Trombone 2 -3.29, bass trombone -3.07, tuba -2.75 dB. The 2-5 kHz brass-accent check does not apply (no brass accents in the score) |
| 3 soft-roll shelf | covered by B #1 | the 84 Hz bell off takes the soft rolls' timpani share of the 30-150 Hz from 46 / 91 % to 29 / 81 % (612-625, the codetta's lone pp roll 708-718) and the tutti share of the master's 40-100 Hz from 70 to 47 % (simulated); no extra shelf |
| 4 string shorts parked, beat weight | adopted | Movement I c51's `SHORT_CC11_PARK` ported (Global Group CC11 table checked in all five HS KS Masters: identical to Movement I's); new "downbeat" weight for 3/4: downbeat +1.5, beats 2-3 0, the eighth after a beat -0.5 dB, over the Allegro sections, velocities unchanged. Level-safe check on parts.json: the parked notes keep their level within 0.1 dB except the intended steps |
| 5 wetness limits | adopted (final chord); open (soft end) | the final chord's RT60 is set by Horn 1's pp release-trail sample (one-shot "1FH pp RT" group, -85 dBFS for 1.1 s after the note-off; the master's -35 dB point sits on it, and lowering the returns changed nothing in simulation). Horn release trails on Sus MAX -6 dB (`rt_gain_db`, all four horns): simulated RT60 1.68 -> 1.42 s. The soft end at 444.5 (0.31 s) is the Violins I harmonic, which now plays on the Violins II Harmonics row (A #5); re-measured below |
| 6 deferred c07 items | partly | C #2.4 flute / solo lead: done (below); C #4.2 celli pizz. group trims: done (note trims: third bars -6, bar 297 -4, heads +1.5); Trumpet 2 StacSs: done (A #4 / B #4); C #2.2 pickup longs and the solo CC1 lane: still deferred (no time-safe rule; C #2.2 needs per-join judgement with pcx after a render) |
| 7 make_template_mix.py | keep re-running | `make_template_mix.py`, then `wet_mix07.py`, `width07.py`, `mix07_more.py`, `mix08.py` in that order (README) |

## 2. Critics' findings

| finding | status | change |
|---|---|---|
| A #1 head tails | adopted | `VEL_SET` v85 on the Violins I second eighths (41.5 ... 797.5), v88 / v85 on 287 / 287.5 and the fugato tails (Violins II 197, violas 185 / 881, celli 173 / 869); celli added to `SHORT_SUS_LEAD_TRACKS` (this also leads the celli's other slurred short Sus notes, 71 notes in all) |
| A #2 sfp 900 | adopted | `FP_SPIKE` ("f", 0.45, 0.9); winds v100 at 900; Violins I 900 on Sus Marc LITE (v105, f layer) with a 0.08 s re-attack lead |
| A #3 / C #4 coda pairs | adopted | Violins I pairs 985-998 on Staccatissimo RRx9, Violins II on Stac RRx9 (spans listed first); Oboe 2 and Clarinet 1 staccatos in 984-1005 at 0.35 of their slot (new generic `STAC_LEN_SPANS`) |
| A #4 horn staccatos | adopted | Horns 1-2 printed staccatos on the 1FH "StacSs RRx9" (Trumpet 1's velocity table, 0.02 s lead); Horn 2 re-tongue gap 0.07 s / 12 CC fall |
| A #5 harmonic E6 | adopted | new generic `BORROW_NOTES`: the Violins II track plays VlnI's two tied notes in 419.5-446 on its "Harmonics" row (590 regions), with Violins I's ppp and decrescendo (`SHARED_DYN` / `SHARED_HP`), the re-bow kept on the row (`REBOW_SAME_ROWS`); Violins I leaves them out (`TRACK_WINDOWS` list form); its re-bow fill at 433.167 removed. CC15 (con sord.) moved by itself to 445.3, after the harmonic |
| A #6 port. | adopted | 640 as a Leg Slur MAX target at v55 (`LEG_VEL_SPANS`); Leg Port MAX unloaded (22,428 regions). Answers the c01-c02 do-not-touch item with A's pitch track (no glide at v100) |
| B #1 timpani | adopted | 84 Hz bell off; roles 597 -5, 624 -4 (steps); Surround kept (simulated tutti share 47 %, under B's 50 % threshold) |
| B #2 Violins II | adopted | soft trims p 0 -> +2, mf -0.8 -> +1.2, f -1 -> +1; role 624-660 +2; celli 624-648 -3 / 648-672 -1 |
| B #3 Clarinet 1 108 | adopted | `_skip_onsets` [108] in pitch_trims.json |
| B #4 trumpets, contrabassoon | adopted | Trumpet 2 on StacSs DblTng RRx9 (instead of a role), with Trumpet 1's pp step over 300-309; contrabassoon 309-360 -3; low brass 309-360 +2 |
| B #5 brightness | adopted | item 1 |
| B #6 Horn 1 close | adopted | role 1100.25-1128 +10 -> +6 |
| C #1 reprise copy | adopted | reprise phrases 1 / 3 on "Spiccato RRx9" (7,929 regions), phrases 2 / 4 all on Staccatissimo RRx9; statement pair 49 on Spiccato; `ROW_TRIM_DB` Spiccato (-3, 80) |
| C #2 Clarinet 1 trio | adopted | note trims 461 / 629 +4, 466 / 634 +3.5, 482 / 650 +4, 491 / 659 +2, 493 / 661 -2.5, 494 / 662 +2.5, 498 / 666 -5.5 (steps) |
| C #3 contrabassoon buzz | adopted | 4 kHz -6 dB shelf; f / ff trims -2 |
| C #5 hard sticks | deferred | untested; the bell change already moves the timpani colour this cycle |
| C #6 flute summit | adopted | Flute 1 1005 on Sus MAX at v104 (not the fff v127), 0.02 s lead |
| c07 C #2.4 solo / flute | adopted | pcx on the c07 stems: solo joins +57 ms, Flute 1 -53 ms. Flute 1's soft-legato extra off over 1044-1068 (new generic `LEG_SOFT_EXTRA_SKIP`; a per-onset offset was absorbed by the 0.03 s lead floor); solo per-onset offsets refit by the c07 rule and the solo's lead cap raised to the sections' 0.75 (its c07 offsets had all been capped at 0.45 of the slot) |

Memory: rows -22,428 (V1 Leg Port MAX) +13,820 (horn StacSs) +4,080 (Trumpet 2 StacSs) +7,929 (V1 Spiccato) +590
(V2 Harmonics): 585,238 -> 589,229 regions (+0.7 %).

Opus states changed (full rebuild by `--midi-only`): Violins I, Violins II, Horns 1-4, Trumpet 2.

## Research items

| item | status |
|---|---|
| EW template mix (c06), returns and sends (c07) | adopted, unchanged |
| plan section 6 shorts parked high, dynamics by velocity | adopted this cycle (level-safe form) |
| batch 7 beat-position weight | adopted this cycle in the envelope (+1.5 / 0 / -0.5) |
| timpani Surround / 84 Hz bell (template) | bell rejected with numbers (70 -> 47 % share); Surround kept |
| brass family EQ | bells halved, shelf +1 (Movement I c51 critics) |
| strings family shelf | removed (6-20 kHz -24.8 against references -28.8..-32.2) |
| batch 6 #3 doublings share one curve; CC11 -> CC1 pass-2 test; separate legato tracks | pending (memory / pass 2) |
| 2.3 kHz return low-pass | rejected in c07 (0.0-0.3 dB) |

## Render: NOT DONE (blocked), 2026-11-08 23:33

Everything above is staged in tools/ and build/ (parts.json regenerated with no WARNING; space_rebows run, no moves
changed). Nothing was written to REAPER; the lock was never taken.
- 20:10-21:12 waited behind mvt2 c45 and mvt1 c51; the orchestrator then reported the sample drive hung from about 20:36.
  From 21:15 timed probes (perl alarm 10 s: `ls`, a 100 kB .oib read) all answered.
- From 21:15 the lock is held by "mvt2 c45 actor"; no REAPER process has run since, and nothing in the mvt2 folder or the
  bridge has changed since 21:00 (bridge heartbeat 20:53). mvt3 c09's waiter queued at about 21:50.
- Resume (next attempt, `before/` exists): take the lock when free (after mvt3 if its waiter is older), `reaper_ctl.py
  restart`, `build_reaper.py build/parts.json jobs --midi-only` (fully rebuilds Violins I, Violins II, Horns 1-4,
  Trumpet 2; EQ and gains ride with the MIDI job), restart, audio_init, `render_cycle.py 8`, then
  `actor_scripts/check08.py 8` against `check_c07.txt`. Expected (simulated): 6-20 kHz about -29.7 dB, 2-6 kHz about
  -10.7, tutti timpani 40-100 Hz share about 47 %, final-chord RT60 about 1.42 s. Re-check levels of the brass (gains
  -2..-4.5 dB), Violins I / II (+1.8 / +1.5 plus V2 trims), the V2 harmonic at 420-446 (target within 1 dB of c07's
  Violins I there), the reprise Spiccato phrases (within 1.5 dB of c07) and the Trumpet 2 / horn StacSs rows.
- ONE_TIME_c08.md is not renamed; HISTORY and LEARNINGS get their c08 entries after the render. cycles/c07 WAVs are kept
  (the disk rule applies after this cycle's render).

## Render attempt 2: NOT DONE (Opus cannot open the sample drive), 2026-11-08 23:33 - 2026-11-09 00:05

- The lock was free at 23:33 (no waiters); held 23:33:38-00:05 by "scherzo c08 actor". Nothing was written to REAPER:
  the open never finished, the project file is unchanged (19:44), REAPER was killed both times (no save).
- Two fresh starts (23:34, 00:02). Both Opus logs (`/Library/Application Support/East West/Opus/log/Opus.g3log.20261108-233428.log`,
  `...20261109-000311.log`) show every open on /Volumes/MAC DRIVE blocking for 5-15 s and then failing with
  "Interrupted system call" (errno 4): ProductInfo.ew, Product.res of all five libraries, and the .ews sample files
  (3,958 failures in the first 30 min). REAPER memory crept to 6.5 GB with 0 % CPU and the drive near 0 MB/s; the
  main thread sat in `open()` inside VST3_LoadState. The last clean Opus load was 20:19 (log with 0 failures).
- The same files open and read at once from a shell (perl `open`, `dd` at 185-245 MB/s, 40 parallel opens), so the
  drive answers ordinary probes; only REAPER/Opus opens fail. The volume is exFAT via FSKit (`com.apple.fskit.msdos`).
  No TCC or kernel log lines were found. Likely causes: the drive's FSKit session after the 20:36 hang, or a
  removable-volume permission prompt for REAPER. Needs Dan: unmount and replug (or remount) the drive, or reboot,
  and check System Settings > Privacy & Security > Files and Folders > REAPER > Removable Volumes. Then resume with
  the steps above. A useful pre-build check: start REAPER and grep the newest Opus log for "Interrupted system call"
  within the first 2 minutes; `ls` on the drive is not enough.

## Render attempt 3: DONE, 2026-11-09 07:42 - 08:37

Lock held 07:42:13-08:36:50 (54.6 min) by "scherzo c08 actor (attempt 3)". mp3: `cycles/c08/scherzo-mockup-c08.mp3`.

Steps: restart (Opus log clean: 0 "Interrupted system call" in the first 2 minutes, project open in 2 min); `build_reaper.py
build/parts.json jobs --midi-only` (53 s; full rebuilds as planned: Violins I, Violins II, Horns 1-4, Trumpet 2; no
errors); restart. That reopen hung: one Opus instance constructed in 20 min, REAPER flat at 1.2 GB and 3 % CPU, the main
thread in VST3_LoadState and a second Opus thread both waiting on mutexes, no thread in I/O (`sample`). The quit before it
had saved the built project (07:46:12), so REAPER was killed (no save) and started again: 22 instances in 2.5 min, open
in 4 min, 45 GB settled by 08:17. macOS then compressed 21 GB of it (the Mac had 95 of 96 GB in use with other
processes' memory, not ours to close), so the render ran with `--force-memory` straight after `audio_init` (48000 / 512,
no input). Memory: 45 GB settled with 21 GB compressed before the render, 46 GB with 28 GB compressed after.

### Measured (c07 -> c08; simulated expectation in brackets)

| check | c07 | c08 |
|---|---|---|
| master 6-20 kHz share, whole | -24.8 | -28.9 [-29.7] (target -28.5..-30) |
| master 2-6 kHz share, whole | -8.9 | -9.5 [-10.7] (target -10..-11: 0.5 dB short) |
| tutti 105-120 6-20 kHz / 2-6 kHz | -26.6 / -9.7 | -30.4 / -10.5 |
| timpani share of 40-100 Hz, 312-360 / 912-960 | 70 / 69 % | 49 / 46 % [47] |
| G.P. 1016 drop +0.3/+0.6/+1.0 s, RT60 | 20.9 / 31.2 / 46.1, 1.38 s | 21.1 / 32.1 / 46.9, 1.30 s |
| final chord 1128 drop, RT60 | 19.5 / 28.0 / 34.0, 1.68 s | 21.4 / 32.8 / 41.7, 1.28 s [1.42] |
| soft string ends (s, limit 0.30) | 0.16 / 0.31 / 0.25 | 0.13 / 0.21 / 0.31 (444.5 fixed by the harmonic move; the third end is now 0.01 s over) |
| reprise V1 attacks identical to the statement | 29 of 38 | 2 of 38 |
| coda V1 pair dips (dB) | 2.5 / 7.2 / 3.1 / 3.3 / 6.7 | 5.7 / 3.9 / 7.0 / 8.1 / 10.3 |
| coda master pair dips | 3.1 / 5.1 / 2.1 / 6.1 / 4.3 | 7.1 / 5.8 / 2.0 / 5.2 / 5.7 |
| peak after the beat: Horn 2 / Trumpet 2 / Horn 1 shorts | 219 / 154 / 124 ms | -3 / 51 / 186 ms |
| sfp 900 Violins I peak | -22 ms | 78 ms |
| Flute 1 summit 1005 at +0.1/+0.3/+0.45 s | -2.1 / -5.0 / -8.7 | +2.0 / +2.0 / +0.9 (holds) |
| timpani 597 / 624 first 0.25 s vs rest | -1.6 / +0.4 | -9.8 / -8.1 |
| V1 / V2 balance 45-48, 121-124 | -35.3/-38.2, -39.3/-45.5 | -35.1/-36.2, -39.4/-42.8 |
| Violins II harmonic 420-446 (target: c07's V1 there, -50.7) | - | -56.1 on the render, -50.7 after the stem fix |
| brass whole-stem RMS (Hn1..4, Tp1, Tp2, Tbn1, Tuba) | | -0.2 / 0 / +0.1 / +0.2 / +0.5 / +1.8 / +1.3 / +1.0 dB vs c07 (the gains held loudness; Tp2's StacSs row and the 309-360 low-brass role add the rest) |

Stem fix (level only, LEARNINGS 15): the borrowed harmonic came out 5.4 dB under target, so `build/roles.json` Violins II
[419, 447, +5.4] (no other Violins II note in 405-460), parts.json regenerated (only Violins II vol_db changed, no
WARNING), `stem_fix.py 8 <render data> build "Violins II" --apply` (originals in `cycles/c08/render_first/`),
`build_reaper.py --mix-only` written to REAPER while the lock was held, then `render_cycle.py 8 --measure-only`.

Master -20.7 LUFS, LRA 23.2 LU, true peak -1.6 dBFS. Delivered -19.8 LUFS, LRA 14.9 LU, TP -1.6 dBTP, limiter about
2.6 dB, span 19.6 dB (c07: -19.8 / 14.7 / -1.5 / 2.5 / 19.6).

Attack probe: all ok except Violas legato: window median 115 ms (limit 90; c07 88), pcX median -37 ms (c07 +6), robust
SD 93 ms. The shift sits in four passages (133-162, 390, 582-609, 858: transitions about 0.1 s earlier and the stem about
3 dB louder from 133.6), while the Violas notes, keyswitches, CC1, CC11 and volume envelope are identical to c07's
there (only four fugato-tail velocities changed, at 185 and 881). A Violas-only re-render of the same project
reproduced it (window 104 ms, median -28 ms), so it is not render-to-render variance. Cause open for c09: suspects are
Opus state carried from the parked CC11 120 shorts just before (37-132) or the memory pressure; test by rendering the
c07 Violas data in the c08 project.

Disk: cycles/c07 WAVs other than 00_Master.wav and Backups/*.rpp-bak deleted (2.7 GB + 335 MB); 47 GB free.
