# Cycle 52 changes (actor, 2026-11-09): stale legato state, the finale's techniques, the coordinator's ten decisions

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c51 render); coordinator notes in the actor brief decide where they
differ. Snapshot: `before/`. Scripts: `actor_scripts/` (`apply52.py` all json edits incl. the post-render rows;
`widthtest52.py` brass width range test; `bal52.py` B's check table with B's c52 rows; `post52.py` joins / sf / sub / dolce /
lowwinds / pedal / flutes; `joindips52.py` legato join dips of two renders; `turnlock52.py` the lock by the longest-waiter
rule). Builds: `rendered_build/` (main render), `rendered_build_pass2/` (pass 2; `*_after_fix` = the data after the stem
fix, = build/). Measurements: `actor_scripts/*.txt`.

## What changed (all generic code off by default; movement I values in the `build/score_config.py` c52 blocks)

1. **Stale Opus state (A #1, B #5; coordinator 1).** New `tools/state_guard.py` decodes every Opus block of a saved .rpp
   and compares each group's AHDSR attack with `jobs/NN_*.b64`. On the c51 saves: Horn 1 (16 groups), Horn 3 (16),
   Trumpet 1 (24), Trumpet 2 (24) at 20 ms instead of 267-1076 ms, pass-2 Bassoon 1 stac (18 groups, 438 ms) — exactly
   A's list. `build_reaper.py --midi-only` (`STALE_GUARD`) now fully rebuilds every stale track of the pass, listed or not
   (the scherzo's `MIDI_ONLY_REBUILD_LEGATO` is kept as an option, off); `render_cycle.py` refuses a stale project
   (`--force-stale`). The c52 build rebuilt those four fully (29 others MIDI-only); pass 2 was a full build. The c51 soft
   trims fitted on the stale audio are reverted (Horn 1 mf -1.4 -> 2.0, Horn 3 mp 6.7 -> 8.4); the two ONE_TIME roles
   rows were not written and were removed from roles.json (re-measured below). `state_check.py` removes the EQ change
   (new `tools/eqresp.py`; on c50 -> c51 the "11 brass state runs" vanish, Trumpet 1's stale joins stay).
2. **Long diminuendi (coordinator 2).** HP_CURVE `decresc_max_qn` 4.0 (longer ones linear again) and `decresc_last`
   0.35 -> 0.20 for the shorter ones.
3. **Phrase shape over short hairpins (C #1; coordinator 3).** PHRASE_SHAPE `hp_fade_min_qn` 4.0 and a new
   `hp_hold_cresc` (inside such a crescendo the offset does not fall below its value at the hairpin start; the arch's
   descent still cancelled the celli's 201 / 601 rise on the lanes). Lane check over 184-216 / 584-616 / 680-696:
   crescendos ending at or under the lane 0.35 s before 13 -> 2 (cor anglais 586.5 is a printed drop; Cello solo 685
   equal). Horn 1 portato rows refit on the render (below).
4. **Low winds (C #3; coordinator 4).** `SWELL_CAP_TO_VOL_DB_PER_CC` (Bassoons 0.32, Bass clarinet 0.26, Contrabassoon
   0.21, Clarinet 2 0.20 dB per unit): the clamped part of the phrase offset goes into the volume envelope (parts.json
   `swell_cap_vol`: peaks 2.2-3.6 dB on 8 phrases).
5. **Subito (C #2; coordinator 5).** Ported `ps_drops` and the "drop" phrase type with `"drop": {"cc": 6}`. Guard: with
   every printed 6-CC drop the rule made 283 spans on 33 tracks, many 16-64 qn long (most arches zeroed), so it runs with
   the new `"subito_only": True` (16 spans: bar 62 Clarinet 1, Bassoon 2, Horns 2-4, strings; bar 84 celli / basses).
   Bar 84: basses' ff G1 `NOTE_END_AT` 331.45, its -8 dB release cut back to 0 by 331.80, the basses' 332.9-334.8 bloom
   shape removed; the celli bloom shape was removed too and restored after the render (below).
6. **sf at qn 78 / 160 (A #2; coordinator 6).** `FP_SPIKE_AT_MARK` ported and extended to sf and SF_ARRIVAL_AT (CC11 at
   the moved note-on of every led sf note now the spike: 114 instead of 86-90; Violins II at 78 now 0.06 s lead on the
   ff layer instead of 0.12 s on mp), `FP_VEL` 96, POST_SHAPES_S bumps (celli / basses +5 dB, Violins I 78 +3, Violins I
   160 +2 then -3..-4 over the bloom), the celli sf a Sus Marc LITE stroke (v95, `retongue_leads.json` 0.05 s) — tools:
   STR_REP_NEW_BOW treats an ART_SPANS stroke-row note as a stroke, else the mf G at 164 became a same-pitch Leg Slur join.
   FINAL_RING stays off (C #6).
7. **Low-end width (C #5; coordinator 7).** Side 200 Hz -6 dB shelf -> side 60 Hz -3 dB shelf + 180 Hz -4.5 dB bell
   (1.5 oct) on the 19 tracks that carried it (the celli / basses' 0 dB 170 Hz placeholder replaced), not on the returns.
8. **315 Hz (B #2; coordinator 8).** Horns 1-4 and Horns a2 bell 315 Hz -5 dB, violas -3 dB (1 oct), B's per-track
   make-up (gain +1.2..+3.3 dB, soft trims +0.4..+1.6 / mp-mf -0.4..+0.9; Horn 3 ppp 13.5 -> 12.0 before it). Celli cut not
   made (optional; deferred).
9. **Brass seating (B #4; coordinator 9).** Ported `track_width`; trumpets 0.5 at pans 0.30 / 0.33 / 0.36 (Trumpets a2
   0.315), trombones 0.6 at 0.26 / 0.30 / 0.34. **Range test** (main project, bars 82-83 and 167-170, brass stems, repeat
   render 0.00 dB): REAPER's width costs K level like B's model A — Trumpets 1-3 -2.82 / -2.23 / -2.60 (-2.28), trombones
   -1.58 (-1.03) / -1.63 (-1.89) / -1.66 (-1.66) dB; make-up gain_db +2.8 / +2.2 / +2.45 / +1.3 / +1.75 / +1.65; with it
   every stem within -0.28..+0.27 dB of the no-width render in both ranges; Trumpets a2 (pass-2 range test, +2.5) +0.16 dB.
   Kept. Stem correlation 250 Hz-5 kHz 0.19-0.50 -> 0.67-0.90; R-L trumpets +1.3..+2.0 -> +3.6..+4.3 dB.
10. **Smaller items (coordinator 10).** Basses `RR_RESET_AT` (15 segment starts incl. the coda; parts.json `cc16`, ported
    with `METRIC_BOWED_DB_SPANS`); Flute 2 `LEG_LEAD_S` 0.05 -> 0.11; A's flute / oboe per-onset leads (633 / 639.5 are
    slur-start joins whose leg_leads rows were inert: new `SOST_JOIN_LEG_LEADS` on the flutes, Flute 1 -0.09 / -0.07,
    Flute 2 633 -0.03 from A's measured landings; Oboe 2 122 / 556 as re-attacks, 628 entry); bar 122 +1 dB row
    484.25-488 on every wind / brass / string track; Clarinet 1's c47 700 fill removed, +2 dB on the 699 pickup; the
    656-664 ride row ends at 662; `HARP_VEL_MAX` 123 (no note changes); `CC1_FROM_CC11` Violoncellos with A's map (Cello
    solo excluded); Violins I re-bow 44.0 fill 0.04 s earlier, peak 8.6 -> 4.6 dB. Not applied: finale item 11 (B #6); the
    violin / viola repeat blur accepted (A #5); re-bow 180.0 not chased.
11. **Also:** `build/mockup.ly` dumps `multi-measure-text-event` (finale item 16; 13 new timpani / percussion / harp texts,
    parts.json byte-identical). `score_to_parts.py` refuses an empty `mockup-events.tsv` (a "%" comment inside the Scheme
    listener list truncated the dump to 0 bytes while testing item 16, and score_to_parts built an empty-dynamics
    parts.json without complaint).

## Corrections after the render (stem fix, `tools/stem_fix.py --apply`; originals in `render_first/`)
- Celli sf bump: started at -0.12 s on the held A-flat (the stroke now leads 0.05 s): pre-echo peak at -0.08 s. Now
  -0.05..+0.10 s +8 dB, +0.14..+0.20 s +3 dB. Violins I 78: bump ends at +0.09 s, +0.5 dB over the bloom.
- Bar 84: the celli bloom shape restored (without it the p G2 swelled 12 dB from +0.1 to +0.6 s).
- Horn 1 dolce: a rise over the recap's 595-596 hairpin (to +6 dB at 595.85); note trim 601 -4 -> -1.5.
- Horn 1 bar-125 entry beat +1.5 dB (496.85-497.9).
- Roles re-measured on the clean state: Horns a2 over the loudest other 41-42 -1.9 (Horn 3's held B-flat over it at
  166-167) -> Horn 3 [165.5, 168, -3.5]; cor anglais minus Horn 1 147-152 -6.9 -> Cor anglais [584, 608, +1.5].
- Basses pedals (RR reset result, heard front downbeat minus off-beat): 104 -2.8, 520 -2.1, 528 -0.3, 664 +0.5, 112 +1.0
  dB -> per-segment steps on the strokes (LEVEL_SHAPES_S, downbeats +c, off-beats -c, c = (2 - measured) / 2).
- These rows are in build/; they reach REAPER with the next build (every track's envelope is rewritten by --midi-only).

## Measured (final: main stems after the stem fix, pass-2 stems, returns)

**Pass criteria**
| Item | c51 | c52 | Pass |
|---|---|---|---|
| 1 Legato joins vs c50, pcX median (Horn 1 / Horn 3 / Trumpet 1 / Trumpet 2) | -45 / -18 / -45 / -45 ms | +1 / 0 / -2 / -8 ms | yes (±15) |
| 1 legato minus other level residual vs c50 (Horn 1 / Horn 3 / Trumpet 1; Horn 2 ref) | +4.1 / +2.6 / +5.6 (+0.2) | +1.6 / 0.0 / +0.4 (0.0) | Horn 1 0.1 over 1.5 (the dolce lanes rose, item 3) |
| 1 decoded pre-render state | 4 + 1 stale | 0 stale (main and pass 2) | yes |
| 2 Horn 1 bar-125 over loudest other, median / min (c50 +2.9 / -0.2) | +1.6 / -6.7 | +5.1 / -0.1 (with +1.5 dB row) | yes |
| 2 strings per qn 492-498 minus c50 | +2.9..+9.7 | -0.2..+0.2 dB | yes |
| 2 master K steps bars 122-126 (C's even fall) | -3.9 / -7.0 / -6.2 / -6.7 | -4.7 / -8.6 / -7.6 / -2.6 | no: c50's shape again (Horn 1 wins) |
| 3 Horn 1 dolce crescendos, end minus 0.3 s before (189/195/201/589/595/601) | -0.6/+3.0/+3.4/-1.7/-3.8/+0.6 | +2.6/+3.8/+7.0/+6.3/+1.9/+2.9 | yes (none reversed, all >= 1.5) |
| 3 brass short crescendos reversed | 3 | 1 | partly |
| 4 low-wind lyric peaks, effective units (lane + envelope / dB per unit) | +0..+11 | +11.1..+21.9 (others' median +17.0 on this measure; C's +11.3) | yes on C's measure; stems arch +8..+14 dB over +0.15 s (Bassoon 2 48 +0.1, no clamp there) |
| 5 bar 62: first 50 ms / steepest 0.2 s / 0.5-1.0 s / returns 0.3-0.6 s | -4.8 / 10.9 / -12.7 / -6.8 | -5.3 / 11.1 / -13.9 / -7.0 dB | yes |
| 5 bar 62 part drops Bn2 / Hn2 / Hn4 / Cl1 (c50 -12.5 / -8.2 / -10.8 / -7.3) | -7.2 / -7.9 / -4.7 / -7.0 | -12.4 / -9.8 / -9.7 / -7.0 | yes but Clarinet 1 (= c50) |
| 5 bar 84: master rise +0.15 -> +0.35 s / Vc+Cb range +0.3..+1.2 s / under bar 83 | +6.6 / 5.7 / 23.9 dB | +4.4 / 5.8 / 22.6 dB | partly (the basses' p G1 decays inside its note) |
| 6 sf peak time after the mark (Vln I 78, Vln I / Vln II / Vla / Vc / Cb 160) | +0.50, +0.56 / +0.02 / +0.06 / +0.28 / +0.26 s | +0.14, +0.04 / +0.02 / +0.10 / +0.06 / +0.06 s | yes but Vln I 78 (+0.14, 1.1 dB over the first 0.1 s) |
| 6 first 0.1 s within 2 dB of the peak | 5.6, 7.3 / 2.0 / 2.2 / 6.8 / 3.3 | 1.1, 1.4 / 1.8 / 1.4 / 2.3 / 1.2 dB | yes |
| 7 correlation < 250 Hz / 250 Hz-5 kHz / side-mid | 0.563 / 0.483 / -4.66 | 0.589 / 0.566 / -5.53 dB | <250 yes; the other two 0.006 / 0.13 dB past the reference edge (side EQ + brass width add: C's -4.5 bell alone predicted 0.509 / -4.95, B's width alone 0.529 / -5.10) |
| 8 master 315 Hz third-octave share / hump | -9.6 / +2.9 | -10.3 / +2.4 dB | yes |
| 9 trumpets / trombones level under width (range test) | | within ±0.28 dB | yes |
| 10 basses pedals, heard downbeat minus off-beat front | -2.8..+5.3 | +2.0..+6.0 every segment | yes |
| 10 basses 520-536 master repeat dip | 8.3 | 8.3 dB | yes |
| A #4 Flute 2 minus Flute 1, shared joins | +58..+133 ms | 633 +3, 640 +28, 642 +75, 280 +85, 636 +118, 643 -155 | no: per-onset leads open |
| A #6 celli CC1 macro: join dips grown >= 2 dB | | 8 of 147 (violas, no macro, 3 of 71); dolce vibrato share 0.39 -> 0.35 | fails A's rule: drop the map in c53 |

**B's check table** (`bal52_c52_final.txt`; c51 -> c52): brass minus strings -0.8/+0.2/+1.0/-0.8 -> -0.6/+0.3/+2.1/-0.9;
horns minus heavy brass 123-126 -4.7 -> -4.0; Horns a2 41-42 +0.3 (with c51's row) -> +1.6; Trumpets a2 minus Violins I /
Horns a2 +0.5/+1.8 -> +0.6/+2.0; Trumpet 1 minus Violins I 82-83 -1.6 -> -1.7; Horn 1 solo 13-14 +9.4 -> +13.0; Violins I
theme +4.3 -> +3.5; celli tune +5.1 -> +4.5; winds minus strings -1.5/-2.2 -> -1.2/-2.0; cor anglais minus Horn 1 -5.1 ->
-5.6; tam-tam -6.3 -> -6.6; cymbals -16.6; chorale -2.2 -> -2.3; Clarinet 1 coda min/median +0.6/+6.6 -> +1.9/+4.8; its
arrival over body +6.0 -> +1.2; Horn 3 minus Horn 4 ppp +4.4 -> +2.0; Cello solo +7.5 -> +8.3. Same-dynamic: p horns
-3.2 -> -3.7, f horns -3.4 -> -3.9, pp winds -0.9 -> +0.7 (the low-wind arches), others within 0.4. Per-dynamic K change
c51 -> c52 (`kres_51_52.txt`): horns and violas within ±0.6 dB except Horn 1 p -1.2 (26 windows), Horn 3 ppp -1.6 (the
intended -1.5), Horns a2 mf -1.0 (6), violas ppp -0.9 (4); trumpets / trombones within ±0.7.

**Other:** climax order (delivered S max) 160 -11.5 > 122 -12.0 > 167-170 -13.6 > 26 -14.3 (c51 -11.4 / -12.4 / -13.4 /
-14.2; 122 over 167-170 1.6 dB). Tutti stops (rtk) 0.48 / 0.40 / 0.50 / 0.50 s to -20 dB (c51 0.46-0.50). 6-20 kHz share
-28.9 dB. Hairpins (`post51.py`, c51 -> c52, 34/50/72 % shares): string diminuendi 0.21/0.40/0.57 -> 0.26/0.52/0.61 (the
linear long ones), brass 0.17/0.36/0.48 -> 0.20/0.28/0.49, winds 0.17/0.22/0.57 -> 0.21/0.28/0.59; reversed diminuendi
5 -> 6. Phrase rise / taper (`phrases_51_52.txt`): wind lyric +0.9/+2.7 -> +1.9/+3.8, string lyric rise +1.6 -> +2.6,
string drive rise +0.9 -> +0.4, the rest within 0.4 dB. Attack probe 0 late or holes (main and pass 2). State check
c51 -> c52 (EQ-aware): Trumpet 1 275-284 / 451-460 -7.6 / -7.1 dB, +56 / +27 ms (the stale joins gone); trumpet runs of
-3.3..-3.7 dB are the width's level loss, which the check does not model; basses 198-212 and 569.5-572 +3.4 dB (round
robins moved by the new resets).

**Loudness** (delivered `mvt1-mockup-c52.mp3`): -19.8 LUFS, LRA 14.4 LU, TP -1.7 dBTP, limiter about 0.4 dB, p10-to-max
18.7 dB. Master -20.6 LUFS, LRA 23.5 LU, true peak -0.6 dBFS.

## Rejected / deferred
- PHRASE_SHAPE "drop" on every 6-CC drop (283 spans; guard) -> subito marks only.
- Celli 315 Hz cut (optional): deferred; the targets pass without it.
- Side bell -3.5 dB (C's variant) would put 250 Hz-5 kHz / side-mid inside the references (simulated by C: -0.009 /
  +0.18 dB) with <250 Hz at 0.540: left for c53, since the coordinator set -4.5.
- Celli 201 / 601 dolce stems (end minus 0.3 s before -4.4 / -0.4 dB): their lanes now rise; the stems' "before" window
  falls on the previous note's attack bloom. Not chased.

## EW-TEMPLATE-PLAN sections not yet applied
Section 5 legato overlap (19-21 ms against 45-80) and legato velocity by dynamic; section 6 two tracks per string
section; section 7 per-note lean-off; section 8 tutti entry spread and room bed; section 10 beat-position short velocity
outside the listed spans. Section 9's "brass as narrow sources" is applied from this cycle; the CC1 macro (section 5) ran
on the celli and fails A's join rule.

## REAPER
- Lock 14:25-15:37 (72 min), after Movement II's c48 and the finale's c11 (our waiter started at 13:44, once no other
  thread was waiting, by the longest-waiter rule). Drive answered at every check.
- Main: start, open (warm-ish cache, 37 tracks), `--midi-only` (state_guard: 4 stale -> full rebuilds), samples settled
  at 44 GB after about 15 min (36 GB compressed by then), brass width range test, save, state guard 0 stale, restart.
  First render attempt refused: REAPER had closed its audio device (fixed with `reaper.Audio_Init()`, `audio_init.lua`);
  rendered with `--force-memory` (21 GB compressed after the settle; kit LEARNINGS 11 / c36: fresh sessions render on
  time compressed; probe 0). Memory after the render 44 GB / 28 GB compressed.
- Pass 2: full `--pass2` build (Bassoon 1 stac stale -> rebuilt), Trumpets a2 range test, restart, render (18 GB, 0
  compressed), quit, unlock. render_pass2 and the range-test audio deleted; 37 GB free at the end.
