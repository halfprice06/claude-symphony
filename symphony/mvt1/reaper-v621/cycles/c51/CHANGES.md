# Cycle 51 changes (actor, 2026-11-08 / 2026-11-09): the MIDI rules of EW-TEMPLATE-PLAN sections 5-10

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c50 render). Snapshot: `before/`. The first attempt (2026-11-08)
stopped at about 20:36 when `/Volumes/MAC DRIVE` stopped answering; it had made the tool and config changes and a range
test (`rangetest/results1.txt`, `levels1.txt`). The resumed attempt (2026-11-09, 07:42-10:00) rebuilt parts.json, rendered
main and pass 2, corrected levels on the stems and measured. Scripts: `actor_scripts/` (`apply51.py` mix changes;
`rangetest51.py` range renders; `post51.py` phrase shapes / climax tone / bar 121; `post51b.py` celli tremolo and S1 dips
on full renders; `kres51.py` net per-track level change per printed dynamic (40 dB window, so the soft brass is counted);
`softfix51.py` the brass / wind soft-trim correction; `rebow51.py` the listed re-bows on stem and master; `pedal51.py`
critic A #5's pedal criteria; `macro51.py` critic A #6's CC1-macro criteria). Builds: `prepared_build/` (before the
render), `rendered_build/` (main render; `parts_after_fix.json` after the first stem fix), `rendered_build_pass2/` (pass 2
and the final data).

## What changed

Tools (`tools/score_to_parts.py`, generic, off by default; with every c51 option off parts.json is byte-identical to c50's):
`PHRASE_SHAPE` (+ `family_gain`), `HP_CURVE`, `REP_SPLIT` gap keys (+ basses plain repeats), `MEAS_TREM["len_frac"]`,
`SHORT_CC11_PARK`, `CC1_FROM_CC11`. Details in README (c51).

Config (`build/score_config.py` c51 block, `build/roles.json` `_c51`, `build/mix.json` via `apply51.py` and `softfix51.py`):
1. S1 string repeats (coordinator 1, A #1): a stroke into a same-pitch stroke ends max(0.06, min(0.08, 0.35 x slot)) s
   early at mp or louder; STR_REP_NEW_BOW gap 0.08 s; basses detach dip -5 -> -3 dB on the ff pedals; B #5 level returns
   (+0.3..+0.5 dB) over the runs.
2. Celli measured tremolo 117-121 (coordinator 2, A #2 / B #2): strokes at 55 % of the slot, Stac-row release cap 120 ms,
   +0.5 dB, and after the range test +3.7 dB more over 464-484 (the strokes lost 3.9-4.5 dB per bar). String short rows:
   CC11 parked at 120 with the Global Group gain returned in the volume envelope (B's level-safe form); metric weight
   +1.5 / 0 / -1 dB on the listed spans.
3. Phrase shapes (coordinator 3, C #1): the finale's arch / build / drive rule, offset in CC1 and CC11, string phrases
   broken at rests >= 0.5 qn and at printed dynamics; after the range test the wind offsets x1.4 (`family_gain`).
4. Hairpin curves (C #4): crescendo control point (0.4, 0.65), diminuendo held to its last inner onset; long builds into f
   and the timpani lanes linear (B #1a).
5. Bar 121 (C #3): -1.5 dB at 480 rising to +1.5 (strings, winds) / +0.5 (brass, timpani) at 483.9.
6. Brass family EQ (C #2): bells 475 Hz -2.7 / 821 Hz -3.9, a 3.2 kHz -3 dB bell, gains -1.8..-4.0 dB.
7. Timpani soft rolls (B #1b): 160 Hz -3 dB low shelf on the soft-roll spans only, +1 dB there.
8. Bass clarinet held G2 at 484 (A #3) held to the next onset; Bass clarinet 2.5 kHz -4 dB shelf back (A #4).
9. B #3 / #4: pp/ppp trims (trombones -1.5, tuba -0.5, horns -0.5, winds -1.0), chorale [698, 716, -1.2], Horns a2
   [664.5, 679, +0.6], violas / celli [56, 88, -0.5], tam-tam -2 -> -1 dB.
10. Pass-2 tests: Cb pedal F1 (Marc Sus LITE v75, lead 0.04 s) and F2 (v92, 0.03 s) on the coda pedal; "Vc macro" (CC1 lane
    = CC11 lane) on the celli 135-219.3.

Note: the wind `family_gain` also moved one entry lead: Bassoon 1's F3 at 72 starts 0.12 qn earlier (71.76, c50 71.88).

## Corrections after the render (stem fix, `tools/stem_fix.py --apply`; originals in `render_first/`)
- **Brass soft levels per dynamic** (`softfix51.py`, from `kres51_50_51.txt`, c50 -> c51 net per printed dynamic, at least 6
  one-qn windows, |change| >= 1 dB). The range test's "+3.7 dB at pp" was the Lento trombones only (2 windows); over the
  whole movement the brass at pp-mf moved -2.0..+3.4 dB. soft_trim_db changes: Horn 1 mf -3.4; Horn 2 mp +1.9; Horn 3 pp
  (and ppp) +2.0, mp -1.7; Horn 4 ppp +1.2, pp +1.7, mp -1.4; Trombone 1 mf -1.5; Trombone 2 pp -1.5, mf -2.2; Bass trombone
  pp -1.1, mf -2.2. Wind pp: Bass clarinet, Bassoons 1-2 +1.0 (B #3's -1 dB overshot: -1.1..-1.6 dB). After: every brass
  row at ppp-ff within -0.9..+0.9 dB of c50 except Horn 3 ppp +1.2 (7 windows) and the 3-4-window rows (`kres51_after_fix.txt`).
- **Re-bows** (A #3): `fit_rebows.py 51 ... --tracks "Violoncellos,Violins I,Violas,Double basses" --write`, merged only
  Violins I 44.0, Violas 700.0, Double basses 38.003 and 47.0 into `build/rebow_fills.json` (every other row kept). The
  fitter has no row for Violoncellos 180.0 (a printed re-bow, which it leaves out).
- **Two balance rows** (roles.json): Horn 3 [163.75, 168.0, -4] (its held Bb3 under the Horns a2 tune came out +4..+6.6 dB
  over c50, partly the held diminuendo of HP_CURVE; Horns a2 over the loudest other read -3.7); Cor anglais [584, 608, +1.5]
  (CA minus Horn 1, 147-152, -6.6; c50 -4.5; the phrase starts lower under the shapes).
- The returns were not re-simulated (post-fader sends; R Brass is about 25 dB under the brass).
- REAPER: the soft trims and re-bow fills were written with `--mix-only` before pass 2; the two roles rows are not yet in
  REAPER (`loop/ONE_TIME.md` for c52).

## Measured (final render: main stems after the stem fix, pass-2 stems, returns)

**Critic B's check table** (`bal50.py`; `actor_scripts/bal51_final.txt`), c50 -> c51:

| Check | c50 | c51 |
|---|---|---|
| Brass minus strings 25-32 / 115-122 / 123-126 / 158-161 | -0.4 / +0.9 / +1.6 / -0.1 | -0.8 / +0.2 / +1.0 / -0.8 |
| Horns minus trumpets+trombones+tuba 123-126 | -5.0 | -4.7 |
| Horns a2 over loudest other 41-42 | +0.3 | +0.3 (-3.7 before the Horn 3 row) |
| Trumpets a2 minus Violins I / minus Horns a2 167-170 | +1.5 / +2.8 | +0.5 / +1.8 (now inside 2.5) |
| Trumpet 1 minus Violins I 82-83 | -1.6 | -1.6 |
| Horn 1 solo over loudest other 13-14 | +11.3 | +9.4 |
| Violins I theme over loudest other 15-22 | +3.5 | +4.3 |
| Celli tune over loudest other 47-55 | +4.5 | +5.1 |
| Harp minus celli 47-55 | -7.6 | -8.7 |
| Winds minus strings 25-32 / 158-161 | -1.5 / -1.9 | -1.5 / -2.2 |
| Cor anglais minus Horn 1 147-152 | -4.5 | -5.1 (-6.6 before the CA row) |
| Tam-tam fff minus all others 484-491 | -7.6 | -6.3 (now inside -6..-7.5) |
| Sus. cymbal + crash minus all others 636-640 | -16.8 | -16.6 |
| pp chorale minus strings 175-178 | -1.8 | -2.2 |
| Clarinet 1 over loudest other 699-706 (min / median) | +3.1 / +3.7 | +0.6 / +6.6 |
| Cello solo over loudest other 680-696 | +7.5 | +7.5 |
| Timpani ppp minus violas 181-182 | -9.3 | -10.1 |

Rolls (median / max re the loudest other; timpani share of the dry 30-150 Hz): bar 11 -7.8 / -5.0, 19 % (c50 25 %);
40-43 -9.7 / -4.6, 42 % (50 %); 13-14 22 % (32 %); 166-169 -6.9 / +0.1 (c50 -6.8 / -0.1). Same-dynamic: pp trombones and
tuba -4.0, pp horns -2.1, pp winds -0.9. Master 100-250 Hz share (loudest 10 %) -8.6 dB.

**S1 repeat dips** (`dips_50_51.txt`, dips50 method; stem / master band, c50 -> c51): basses 104-124 2.3 / 2.7 -> 5.1 / 3.5,
520-536 4.4 / 4.2 -> 7.6 / 8.3, 554-568 4.1 / 2.8 -> 9.0 / 3.0, 664-676 3.2 / 2.7 -> 3.0 / 2.1; violas 86-100 4.7 / 2.5 ->
8.1 / 2.8, **440-468 3.9 / 1.4 -> 6.5 / 1.3**, 552-568 3.6 / 1.6 -> 8.8 / 1.0; Violins II 86-100 4.5 / 2.2 -> 7.5 / 2.3,
536-548 3.7 / 1.7 -> 7.3 / 1.6; celli 504-520 3.2 / 1.3 -> 5.1 / 0.8. Gaps 14-19 ms -> 77-80 ms. The stems separate the
repeats clearly; in the master the violas' and upper strings' band dips did not improve (1.0-2.8 dB): the other parts and
the returns fill the gap. The basses' do (master 520-536 +4.1 dB).

**Celli tremolo 117-121** (`post51b.py trem`; peak-to-trough per stroke on 5 ms frames): stem 5.2 -> 10.0 dB, master
100-800 Hz band 5.1 -> 5.1 dB; per-bar level -30.9 / -31.9 / -31.3 / -31.3 / -27.9 -> -31.4 / -32.1 / -31.9 / -32.2 / -27.5
(the +3.7 dB kept the level within 0.9 dB). dips50's body measure reads 1.6 -> 0.6 dB here and is not valid for strokes
shorter than their attack.

**Phrase shapes** (`phrases_50_51.txt`, dry stems; rise from +0.15 to +0.8 s / taper over the last 1.0-0.2 s):
wind lyric +0.2 / +1.4 -> **+1.1 / +2.7 dB** (n 55); brass lyric +0.9 / +1.6 -> +2.7 / +4.5 (n 35); string lyric +1.6 /
+0.2 -> +1.6 / +1.5 (n 29); builds and drives within 0.4 dB of c50 except brass drive rise +0.6 -> -0.9. Named: Flute 1 42
rise -1.7 -> -0.4, taper -2.8 -> +2.8; Horn 1 49 rise -1.6 -> +2.7; Clarinet 1 207 +1.8 / -2.5 -> +4.2 / +0.4; Cor anglais
608 +4.5 / -3.3 -> +12.8 / +2.5. The winds now rise and taper, but their lyric rise by 0.8 s is still the smallest (+1.1).

**Bar 121** (`bar121_50_51.txt`, K per beat 480-485): growth 480->483 +1.5 -> **+3.3 dB** (pass 2.5), step into 484 +4.0
-> **+3.1** (pass 3).

**Climax order** (delivered mp3, S max): 160 -11.4 > 122 -12.4 > 167-170 -13.4 > 26 -14.2 (c50 -11.2 / -11.9 / -13.4 /
-14.1). Order kept; bar 122 is 0.5 dB lower (C's limit +-0.3, the range test predicted 0.4-0.9); 160 over 122 1.0 dB (pass
0.5); 167-170 over 26 0.8 dB.

**Climax tone** (`tone_50_51.txt`, master, loudest 25 % of frames): centroid 121-126 1240 -> 1126 Hz (-114), 160-166
1226 -> 1162 (-64, short of the -80..-100 target), 167-170 1040 -> 963 (-77); whole movement loudest 10 % 1057 -> 985 Hz
(C: 1000 or lower); 2-4 kHz share -9.1 -> -10.2 dB (C: -10 or lower); 500 Hz-1 kHz -7.6 -> -6.8.

**Decays** (`rtk_50_51.txt`, `tails_50_51.txt`): rtk tutti stops 0.48 / 0.46 / 0.47 / 0.50 s to -20 dB (c50 0.49-0.51):
no wetter. Drops at +0.3 s: 125.9 16.0, 288 16.8, 551 20.6, 679 20.6 dB (c50 15.7 / 17.2 / 20.1 / 20.3); fermata RT(-20..-35)
1.89 s (1.84); final chord -20 dB at about the c50 time (drop 1.0 s -32.4, c50 -32.1). One change: the bar-14 Horn 1 ending
(qn 55) drops 14.1 dB at +0.3 s (c50 19.2) from a pre-level 1.7 dB lower; the phrase taper lowers the level before the cut,
so the release and hall make up more of what follows (the tail itself is no longer than c50's, RT -5..-25 1.21 s vs 1.51).

**Width and brightness:** correlation < 250 Hz 0.563, 250 Hz-5 kHz 0.483, > 5 kHz 0.404, side/mid -4.66 dB (c50 0.584 /
0.483 / 0.433 / -4.71; references 0.54-0.62, 0.47-0.56, -4.7..-5.4); master 6-20 kHz share -29.2 dB (c50 -27.8;
references -28.8..-32.3).

**Loudness** (delivered `mvt1-mockup-c51.mp3`): -19.8 LUFS, LRA 14.6 LU, TP -1.8 dBTP, limiter about 0.0 dB, p10-to-max
span 18.8 dB (c50 -19.8 / 14.7 / -1.8 / 0.2 / 19.1). No refit of deliver_master.py. Master -20.3 LUFS, LRA 23.6 LU, true
peak -0.7 dBFS, sample peak 0.926.

**Other:** attack probe 0 late or holes (main and pass 2). State check: 11 runs of 3-5 brass notes +3.1..+4.3 dB on
unchanged MIDI (Horn 2 406, Horn 3 316 / 720, trombones 284 / 316 / 381, Horns a2 381 / 670, Trumpets a2 670): sample-state
flips of the kind c49 met on Horn 1; not chased this cycle. Re-bows (`rebows_51_final.txt`): Violins I 44.0 stem 5.7 /
master band 5.6 dB, Violas 700.0 2.1 / 3.7, Violoncellos 180.0 5.0 / 6.4 (the celli sit 12 dB under the master band there),
basses 38.003 step -6.2, 47.0 dip 8.4 (20 dB under the master band). Automatic dip medians Vln I 3.3, Vln II 2.2, Va 1.1,
Vc 1.6, Cb 1.9 dB; steps >= 3 dB: basses 8, others 1-3.

## Pass-2 tests (critic A #5, #6)
- **Cb pedal F1 / F2** (`pedal51.txt`): downbeat front minus off-beats (40-300 Hz, 80 ms) F1 -1.8..-3.6 (0 of 12 at +0.5),
  F2 -3.1..+2.2 (1 of 12); downbeat 2-5 kHz front minus body 8.2 / 4.7 dB under the off-beats'. Both fail; not adopted.
  The c51 **main** basses track now passes the first criterion: +0.8..+4.0 dB on 11 of 12 downbeats (c50 -1.5..-6.6, same
  script). The REP_SPLIT gaps and the -3 dB detach dip, not a layer change, fixed the weak downbeats; the main track still
  misses the 2-5 kHz (downbeats +3.4 dB brighter than the off-beats, limit 2) and adjacent off-beat (max 3.3 dB, limit 1.5)
  criteria.
- **Vc macro** (`macro51.txt`, 18 notes of 0.9 s or more): AM p95-p5 4.7 -> 4.4 dB (max +0.7 over main), 4-7.5 Hz share
  0.34 -> 0.34 (dolce tune 0.39 -> 0.34, ratio 0.87), level -0.1 dB with a spread of -2.3..+1.6 after the offset, centroid
  -1 Hz. Passes A's "no worse" criteria except one note at -2.3 dB (limit 1.5); joins not measured. Not adopted on the main
  track (A: adoption belongs to the next round). The CA macro aliases were not built.

## Rejected / not adopted, with numbers
- Cb pedal F1 / F2 and Vc macro (above). Test tracks and the test return deleted from the pass-2 project.
- Violoncellos 180.0, 41.38, 37.377, 26.516, Violas 725.52 and basses 506.408 re-bow rows: not refit (the coordinator's list
  named only 180.0 / 44.0 / 700 / 38.003 / 47.0; 180.0 is not fittable). The refit did not bring 44.0 or 180.0 under 3 dB in
  the master band: their dips fall in the first 0.1-0.25 s, inside the attack, where a fill clamps.
- A brass +0.5 dB at 488-504 (B #4's fallback): not needed, brass minus strings 123-126 reads +1.0.
- deliver_master refit: not needed (LRA 14.6 LU, limiter 0.0 dB).

## EW-TEMPLATE-PLAN sections
Applied this cycle: 5 (CC1 macro, as a test only), 6 (string shorts with CC11 parked, level-safe), 7, 8 and 10 (phrase
shapes; beat weights in the envelope on the listed spans), 9 (hairpin curves). Not yet applied: 8's tutti entry spread and
room-noise bed; 10's beat-position velocity outside the listed spans; the CC1 macro on the main tracks.

## REAPER
- Lock 08:46-09:40 (54 min), after the scherzo's c08 and the finale's c09 (wait from 07:42). Drive answered at every check.
- Main: start, open (37 tracks = 33 + 4 returns), `--midi-only` of the 11 wind tracks and Violoncellos (all fully
  rebuilt: Opus state changed), restart, settle 9 min at 43 GB (0 compressed; no audio-device drop), render 08:59-09:11,
  `--mix-only` (brass / wind soft trims, re-bow fills), save, quit. Memory after the render 44 GB / 27 GB compressed.
- Pass 2: start, open (10), full `--pass2` build (10 tracks + returns), restart, render (23 GB settled, 0 compressed), test
  tracks and R Strings test deleted, saved with 10 tracks, quit, unlock.
- Disk: render_pass2, test-stem and range-test audio deleted; 35 GB free at the end.
