# Cycle 03 (actor), on the c02 render and the critics' reports A, B, C

Resumed attempt. The first c03 actor (2026-11-07 11:40-13:28) snapshotted `before/`, made most of the critics' edits and then waited about 18 hours for the REAPER lock without rendering (`lock.log`). This attempt (2026-11-08) kept its edits that match the critiques, replaced one (the clarinet row change, below), added critic C #6, and did the ONE_TIME task (Movement I c44's three shared changes). Every track was fully rebuilt. Scripts: `cycles/c03/actor_scripts/` (`decay.py`, `gpdecay.py` hall decay; `repdips.py` S1 dips; `lv.py` helpers).

## ONE_TIME (Movement I c44): drier hall, release caps, repeated string notes

1. **Shorter hall tail.** `build/mix.json` `reverb.ir_setup` `{"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}`; sends, IR, wet, fx_volume 0.095, low cut 160 and high cut 5500 unchanged. `tools/build_reaper.py` `apply_mix` got the kit's irSetup block (commit 86b70270: each key copied into the ConvolutionReverb insert's `irSetup`, unknown keys stop the build, a track's `reverb_ir_setup` overrides).
2. **Release caps.** `tools/build_reaper.py`: `sus_release_cap_ms` may now be a list of specs (the kit's c46 form). Strings (Violins I, Violins II, Violas, Violoncellos, Double basses, Violas div): 150 ms at mf/f/ff and 350 ms at pp/p on Sus MAX and Sus Marc LITE. This replaces c00's 250 ms mf-ff cap on violas, celli and basses. **Deviation from ONE_TIME.md**, which says 150 ms at all five dynamics: mockup-kit README item 11 (Movement I c46, after c44) records that 150 ms at pp/p made soft endings stop (final ppp chord -10 dB in 0.07 s against 0.20-0.40 s in recordings) and sets at least 350 ms at pp/p. The Violin I solo (DIV A) keeps no cap, as Movement I's Cello solo. Horns 1-4: 237 ms at pp/mf/f on Sus MAX and LegRep RRx4 (row names checked in the 1FH KS Master; the patch ships pp 562, mf 394, f 316, ff 237).
3. **STR_REP_NEW_BOW** (Dan's S1). Ported from Movement I's tools: the c44 rule (classification pass, merge loop, note-length branch, re-tongue lead, row-trim exclusion, vibrato dip, re-bow points, parts.json `rep_strokes` / `rep_rebows` / `rep_sus_gaps`), plus c45's fixes (the "sus_min_s" repeats take the re-tongue lead, `sus_lead_s`; `REBOW_FILL_END_S` 0.12 so a re-bow fill never holds into a later note). Patched from the Movement I c44->c45 and c45->c46 snapshot diffs (both applied cleanly). Settings in `build/score_config.py` as Movement I's. Counts: Violas 24 strokes (6 loud, 18 portato), Violas div 15 portato, celli 4 (2 portato), Violins II 0; soft re-bows Violins II 1, Violas 7, celli 8; sus gaps celli 10, basses 13. The old automatic celli re-bow at 1078.442 is replaced by the printed bow changes at 1074/1077/1080, so its `rebow_fills.json` row was removed. Notches: Violas 70 -> 39, celli 28 -> 16, Violas div 17 -> 2.

Measured (c02 -> c03; `gpdecay.py`, `decay.py`, `repdips.py`, `phrase_ends.py`):
- **Late decay.** Master at the G.P. (bar 339 cut-off): RT(-5..-25 dB) 2.46 -> 1.31 s, late RT(-20..-35) 3.33 -> 2.81 s, T60(-20..-40) 3.43 -> 3.27 s. The master's late part is the timpani still ringing (below); the sum of all stems but the timpani: RT(-20..-35) 1.33 -> 1.12 s, T60(-20..-40) 1.76 -> 1.12 s. After the last note (Horn 1 alone): T60 2.0 -> 2.03 s. c01's 3.5-3.7 s T60 was measured on the master at the G.P., so it also included the drum.
- **Tutti cut-offs, master drop at 0.3 s:** qn 393 17.4 -> 19.6 dB, qn 861 15.4 -> 16.2, G.P. 6.6 -> 15.5 (all over the 13 dB target).
- **Repeated notes (S1), stem dip median (master):** strokes 0.9 -> 6.7 dB (2.0 -> 1.6), sus gaps 2.9 -> 7.5 (1.7 -> 2.7), portato -0.5 -> 1.5 (2.8 -> 2.0), soft re-bows 3.7 -> 4.2 (3.2 -> 3.1); clarinet slurred repeats (A #2) 0.0 -> 3.6 (3.5 -> 3.6). The portato repeats (violas and Violas div, bars 209-224) are still too smooth on the stem (target 3-5).
- **Phrase endings** (note of 0.4 s or more followed by 0.75 qn rest): no string or horn ending falls more than 10 dB in its first 0.05 s (max 4.9 strings, 8.7 Horn 3). Drop at +0.15 s: Violins II 4.0 -> 7.6, basses 4.1 -> 9.1, Violins I 11.6 -> 12.8, violas and celli unchanged (11.5, 9.7); horns 6.4-10.0 (no c02 horn stems kept).
- **Re-bow refit** (`fit_rebows.py 3 build/parts.json --write`, applied by stem fix): Violins I 1116.4 dip 9.2 -> 5.6 dB, Violas 1080 11.3 -> 3.1, celli 1080 4.4 -> 1.5. Celli 1074 (8.1 dB) and the other short soft re-bow pieces were too short to fit (MIN_PIECE_S).

## Critics' findings

KEPT from the first attempt (checked against the reports and the code):
- A #1: Sus Marc LITE heads inside the mp marcato band, `vel_by_cc` (34,50) (46,56) (58,61) (72,64).
- A #3: new generic `WIND_REP_PORTATO_TENUTO` (the tenuto rule's 0.06 qn gap no longer pre-empts the portato re-tongue).
- A #4a: clarinet pitch trims (Clarinet 1 G#4 +4, B4 +3, A4 -2.5, C5 -2; Clarinet 2 C#4 +4).
- A #5: new generic `ROW_TRIM_WINDS`; Oboe 1 "Stac DblTng RRx9" -5 dB from CC11 72.
- B #1 celli roles (362-396 -4, 576-612 -7, 624-672 -3, 828-864 -3); B #3 summit (Violins II 1004.75-1008 -3, Flute 1 1005-1007 -2); B #4 harp (552-576, 672-711 -3); B #5 timpani 612-618 -3; B #6 basses' A1 at 96 -6 dB as a LEVEL_SHAPES step.
- B #2 / C #4: new generic `TIMP_STAC_ROW` = "Timpani Flt Sht" for printed staccato strokes (7 onsets, 8 notes; the strokes at 12, 165, 393, 861 are tie ends of held notes, not new strokes).
- C #1: new generic `SHORT_SUS_TO_LONG_ANY` (a slurred eighth before a long note stays on the legato row).
- C #2: `ABUT_LEAD` 0.08 s for Violins I/II and violas at the hemiola and summit strokes (violas 904/906 keep their Leg->Sus entry path).
- C #3: `leg_leads.json` offsets for the trio tune (Violins I/II, celli); `entry_leads.json` for bar 209.
- C #5: new generic `PIZZ_LEAD_S` (Violas 0.045, Violins II 0.035, celli 0.035); C #6 (last item): `STAC_LEAD_SPIC` (Spiccato takes the staccato lead).

CHANGED in this attempt:
- A #2 (clarinets' slurred repeats, manual p.112 "Leg Slur Rep"): the first attempt used `ROW_REMAP` Leg Slur -> Leg Slur Rep. ROW_REMAP renames the row before the rules run, so rules keyed on "Leg Slur" stopped applying: the clarinets lost their entry leads (131.758 -> 132.0, 239.758 -> 240.0, 359.758 -> 360.0) and some notes were shortened. Replaced by critic A's first form: a whole-piece `REP_ROW` span (0, 1128, "Leg Slur Rep") on Clarinet 1 and 2 (the keyswitch only; every rule still sees Leg Slur / Sus Non Vib; Leg Slur and Sus Non Vib unload). Clarinet 1 now loads one row; the entry leads are back.
- C #6 (loud string entries on Leg Slur MAX +80..+100 ms): new generic `ENTRY_LEAD_LOUD_ART_S` (extra entry lead above CC11 80 by row), `{"string": {"Leg Slur MAX": 0.06}}`. Read in parts.json: most of the late entries the critic listed (Violins II 708, Violas 643/1020, solo 1044) are at CC11 80 or under and already had the 0.12 s lead, so the option moves few notes; the bar-209 extra for Violins I was dropped (now covered), Violins II keeps 0.06.

Rejected / deferred:
- A #3(b) LegRep RRx4 rows for bass clarinet / Bassoon 2: deferred until the WIND_REP_PORTATO_TENUTO fix is measured.
- A #4b auto_fills for the clarinet and bassoon joins: next cycle (the pitch trims move the bodies first, as the critic says).
- C #6 smaller items: the Trio's ramp ending at 226.17 instead of 228 (0.8 %), the final rit. shape, the probe's harp references: not done this cycle.

Measured on c03 (c02 -> c03):
- A #1: the heads with the mp attack sit +2.4..+3.7 dB over the staccato before them and lost the bright front (2-5 kHz front minus body, my 130 ms measure, about +6 -> -1.9 dB). Two heads (51, 771) came out +6.5 / +6.3 dB with a bright front (round robin): -3 dB more by stem fix.
- A #2: clarinet slurred repeats dip 3.6 dB median on the stem (target 3-6).
- B #1: celli minus the loudest upper string, bars 193-200: +9.5 -> +0.2 dB; 209-224: 0.0 -> -6.2 (target -2..-4: now too low; the role should be about -1); 121-132: +4.5 -> -2.3; 277-288: +2.0 -> -2.8. The celli fell 2-4 dB more than the roles alone (release caps, new strokes).
- B #3: Violins I at the first 0.4 qn of 1005 is 1.1 dB under Violins II (was 3.4 under). The master's first half of 1005 is now 0.9 dB under 1004 (target: 1 dB over); bar 337 is 1.0 dB over bar 304 (c02 2.1). Open.
- B #4: harp under Oboe 1, 552-564 2.3 dB (target 3-5), codetta 672-684 5.1 dB.
- B #5: the roll at 612-618 is 2.4 dB under Horn 1 (target 2-3).
- B #6: basses' A1 at 96 is 3.6 dB under Flute 1 (target 3).
- B #2 / C #4: **not fixed.** The Sht row plays the bar-339 stroke, but the long strokes of bars 337-338 (Lng, v121) still ring: timpani stem -42 / -51 dB in qn 1017-1019 against the master's -41 / -51 and Violins I's -60 / -87. A volume-envelope cut is undone by build_reaper's tail hold (rests keep the last note's level). Next: a pre-hall CC7 fall on the timpani from qn 1015 (or Sht on 1012 too).
- C #1-#3, #5: not measured with pcx this cycle; the attack probe's legato spread improved (Violins I 88 -> 75 ms window median, limit 75, still flagged; Violins II 90 -> 80, ok).

## Render

- Lock: waited from 06:28 behind Movement I (held from 06:18) and Movement II's waiter, which had waited longer (turn rule); held 08:20:02-08:48:48 (28.8 min). Full build of all 31 tracks (Opus states changed on every track: ir_setup), restart, render with `--force-memory` (45 GB settled, 14 GB compressed), stem fix, `--midi-only` of Violins I, violas and celli with the same data, quit, unlock.
- Disk: 30 GB free before the render; freed 1.9 GB by deleting this folder's old REAPER backups (Nov 7, all but the newest two), `cycles/c02/render_first/` and the c02 stems other than the master and the string sections.
- **REAPER memory**: 45 GB settled before the render (14 compressed), 45 GB after (29 compressed).
- **Master** (after the stem fix): -20.0 LUFS integrated, LRA 23.4 LU, true peak -0.9 dBFS, sample peak 0.903 (no clipping).
- **Delivered** `cycles/c03/scherzo-mockup-c03.mp3`: -19.9 LUFS, LRA 14.6 LU, TP -1.6 dBTP, limiter about 2.5 dB, p10-to-max span 19.5 dB.
- **Attack probe**: all 20 attacks and the opening ok; legato spread Violins I flagged (75 ms window median at the 75 ms limit; c02 88), Violins II 80 (limit 75; c02 90 flagged), violas and celli ok.
- Stem fix (`tools/stem_fix.py 3 cycles/c03/build_render build --apply`; originals in `render_first/`): re-bow refit (Violins I, violas, celli) and the two head trims (Violins I 51, 771 -3 dB).

Open for c04: the timpani ring in the G.P. (CC7 fall); celli 209-224 role -3 -> about -1; summit 1005 under 1004 again (Violins II / Flute 1 cuts took power from the arrival); string portato repeats only 1.5 dB on the stem; celli 1074 re-bow 8 dB dip; harp 552-564 1 dB more; refit the clarinet / bassoon joins (A #4b); measure C #1-#3 and #5 with pcx.
