# Critic C, cycle 43: tempo, timing and transitions (render c42, score v621), Dan's note S2 first

## Manual notes (second round: c37 slot C's pages, 2021 manual PDF pp. 143-149, read again in full; p.143 and p.149 rendered as images; MANUAL-GAPS.md and DIGEST.md read)

| Manual (PDF page) | What it says | Where it applies here | Followed now? (c37 note -> c42 render) |
|---|---|---|---|
| p.143 | Performance-script CCs: CC5 legato/portamento time, CC15 con sordino, CC22 mono/poly, CC36 RR reset, CC57 legato script, CC65 portamento script, CC69 repetitions, CC70 finger position; "if no MIDI CC value is present, the script retains its default setting" | parts.json writes CC1, CC7, CC11, CC15, CC36, CC70 only; the KS Masters' emulated Legato/Portamento scripts are off | Yes, unchanged since c37. New check (missed in c37): the c42 pass-2 aliases are fresh instances with default script states, and their joins reproduce c41's main-track timing to the millisecond (Violins II 230 / 231.5 / 239.5 / 242: +122 / +95 / -110 / +119 ms in both; measured). |
| p.144 | True legato: velocity sets transition time (about 50-60 longer, 110-127 tighter), not loudness | String and brass targets v124; winds at the printed velocity; `LEG_VEL_EXTRA_S` (c37) adds lead to soft wind targets | Partly. Fast tempo: soft (v70 or less) wind legato now sits on the beat median (dev 0 ms, n 37; measured). Slow tempo: v70-or-less wind targets still have a perceived attack +72 ms (n 12); on the Bass clarinet the pitch change is on time and the lateness is a 3 dB dip followed by a +3..+4 dB swell 0.2-0.4 s after the beat, which a lead cannot fix (finding 1). |
| p.144 | v110-127 = shortest transition | v124 on strings and brass | Yes. MANUAL-GAPS #8 is closed (c42: transitions 82-98 ms in every section). |
| p.145 | Repetition script randomises; RR Reset gives "identical" playback; CC36 | CC36 in the pre-roll; Opus's reset controller is CC16 (Preferences; 2025 p.92; MANUAL-GAPS #6) | Not followed, and it now matters for timing. c37 found attack times identical between renders. c41 -> c42 with identical data: winds, brass, timpani and harp identical (median change 0 ms, 1-3% over 30 ms), but strings 5% over 30 ms and Violins I 23 of 245 joins (9%) moved more than 30 ms (max 123 ms) after both violin instances were fully rebuilt in c42 (measured). Per-onset leads on those joins fit one round-robin state. |
| p.145-149 | Finger position on CC70; pp.147-149 are tables (p.149 rendered: celli strings per note for FP 1-4) | `SUL_SPANS`, resting CC70 127 (FP4) | Yes; no timing effect measured (c37, c38). |
| MANUAL-GAPS #2 (repetition rows) | p.101 / p.106: recorded re-tongues | LegRep RRx4 on Horn 1 528 / 624 and Trumpet 2 456 | The rows speak earlier than the Sus re-attacks the leads were fitted for: Horn 1 LegRep -40 / -71 ms and Trumpet 2 456 -76 ms against the beat median with the Sus re-tongue leads 0.09 / 0.08 s, while Horn 1's other re-attacks sit at +20 (measured; in finding 3). |

## Method (measured)

Every score note group (chords once; re-bow, tremolo-split and restrike pieces left out) on every c42 stem, 4662 groups, was measured with the pcX rule from `tools/pcx.py` (t50 / h10 mean on harmonic bands, every bin within 2 FFT bins of a harmonic of any other pitch of the track sounding in the last 0.5 qn left out, FFT 2048-8192 as in pcx.py; broadband for timpani and tam-tam), against the score onset on the render's tempo map. I checked the estimator on synthetic switches at the basses' pitches (G1-C3): error -6..-23 ms. The same scan was run on c41 to separate stable timing from render-to-render variance. "Beat median" = median perceived attack of all tracks on that score onset (3 or more tracks). "Exposed" = stem broadband level within 10 dB of the master over the first 0.3 s. Scripts and data: `/private/tmp/claude-501/mockup-loop/mvt1-c43-C/` (`s2scan.py`, `s2an.py`, `cands.py`, `tables.py`, `vlnfit.py`, `vlnstable.py`).

**S2 state (measured).** Every family and path sits within ±10 ms of the beat median in the Allegro and Poco meno mosso (string legato -0, string re-attacks +0, wind legato +1, wind re-attacks +5, brass legato 0, brass re-attacks -10, entries -4..0, staccato -6..+3, timpani +3, harp -3 ms), except string tremolo (below). The beat median itself sits +8..+14 ms after the grid everywhere, a constant offset nobody hears. So no family-wide lead change is needed. What remains is per-note scatter:

| | exposed notes | per-beat robust SD | > 60 ms off | > 100 ms off |
|---|---|---|---|---|
| Allegro spans (incl. stringendo, allargando) | 761 | 31 ms | 16% | 4% |
| Poco meno mosso | 374 | 29 ms | 14% | 3% |
| Lento (bars 1-14) | 36 | 79 ms | 42% | 14% |
| Più lento / Tempo I (bars 171-182) | 37 | 45 ms | 22% | 16% |
| sostenuto (bars 123-126) | 11 | 36 ms | 27% | 0% |

The c42 refit is confirmed on this reference too: of the 23 joins whose lead changed in c42, 18 came closer to the beat median and 1 moved further; median distance 58 -> 27 ms; transfer 1.01 s of pcX per s of lead (measured). The loop's 0.6 factor therefore closes only 60% of each gap; 0.8 is safe on joins that read the same in two renders.

## 1. The slow sections are where the attacks scatter most: the opening and closing mottos and the Lento chords (measured)

**Where.** Bars 1-3 (qn 3-12), the Lento chords at 20, 36, 40, 44, 47, 50; the sostenuto 488-501; the coda solo 680-694 and the closing motto 696-712 (bars 175-179).

**What is wrong.** In the slowest tempi the same 0.15-0.3 s differences are a large share of a beat, and the lines are exposed octave unisons:
- Opening motto (Vc, Cb, Bass clarinet in octaves, pp), perceived attack re the score onset: qn 4.0 Vc -33, BCl +72, Cb +148 ms; 7.5 Cb -125, Vc -13, BCl +44; 8.0 Vc -35, BCl +84, Cb +123; 10.0 Vc +58, BCl +137, Cb +201; 11.0 Cb -127, BCl -8, Vc -2. Identical in c41.
- The basses' legato direction decides the error: rising steps late (4.0: G1 -> E-flat2, the old pitch stays louder until +0.38 s, t50 +280 ms; 10.0: C2 -> D-flat2, crossover +0.16 s, t50 +342 ms), falling steps early (7.5 -138, 11.0 -140 ms re the grid). Kit LEARNINGS 5 asks for per-direction leads; the basses have one value (0.17 s).
- Bass clarinet (v60, Leg Slur, lead 0.14 s with `LEG_VEL_EXTRA_S`): pcX +72 / +137 ms at 4 / 10 and +95 / +190 / +230 ms at 700 / 708 / 710. Its pitch change is on time (crossover -4..+14 ms at 10 / 708 / 710). Broadband, every one of these joins dips 2-4 dB from -0.1 to +0.1 s and then swells 3-4 dB over the note before it at +0.2..+0.4 s (708: -48.5, -48.9, -51.9, -52.1, -50.0, -46.5, -45.5, -48.3 dB at -0.3..+0.4 s in 0.1 s steps), so its weight lands 0.25-0.3 s after the beat. There is no hairpin there (mockup-events: 704-712 one slur, no cresc.).
- Closing motto: 700 Tbn 1 +180, Vc +137, BCl +95 against Cb -11, BTbn -7, Cl 1 -5; 704 BTbn +179 against Cb -75; 710 BCl +230, Tbn 2 +150 against Tbn 1 -89; 712 Violas +143 against Cb -63 (spreads 190-320 ms).
- Coda solo: Cor anglais 684 +202 against Bassoon 2 -56; Cello solo 690 +155, 694 +152 (crossovers +168 / +214).
- Sostenuto: Violins II 496 re-attack +232 against Violins I -65; Violas 496 / 501 -115 / -80 (they already carry -0.08 / -0.12 s).
(All values: perceived attack re the score onset; the appendix lists pcX - 0.013 s, the distance from the ensemble's median offset.)

**Fix.**
1. Per-onset leads from the slow-section table in the appendix (A1), totals = old + 0.8 x (pcX - 0.013 s), change clamped ±0.12 s, only notes that read the same in c41 and c42 and, for legato joins, whose crossover is off in the same direction by more than 30 ms. Legato -> `build/leg_leads.json`, entries -> `build/entry_leads.json`, re-attacks -> the new table of finding 3; the Cello solo values go into its alias "tables" in `ALIAS_TRACKS`.
2. Bass clarinet 4, 10, 700, 708, 710: no more lead. Add `LEVEL_SHAPES_S` rows (`build/score_config.py`) that fill the dip and cut the swell, starting from `[(-0.12, 0), (-0.04, +2.5), (+0.10, +1.5), (+0.18, -3.0), (+0.42, -3.0), (+0.60, 0)]` re the score onset, fitted per join on the c42 stem by simulation (target: 50 ms broadband level within ±1.5 dB of the line from the old note's body to the new note's body from -0.1 to +0.5 s). Drop `LEG_VEL_EXTRA_S["Bass clarinet"]` for these five joins only if the shapes leave the crossover early.
3. Double basses 4.0: if the +0.12 s clamp leaves the crossover later than +0.15 s, play it as a fresh pp entry (entry lead 0.12 s plus an early fill, kit LEARNINGS 6) rather than a 8-semitone legato.

Check: per-beat spread of the exposed parts at 4, 7.5, 8, 10, 11, 700-712 under 0.12 s; Lento exposed robust SD under 50 ms.

## 2. The violins' lead refit (open from c42): 21 + 9 joins that are off in both renders; 5 more that are render variance must stay out (measured)

**Where.** Violins I / II main tracks and the "Violins II f62" alias (its joins use Violins II's tables).

**Evidence.** `tools/pcx.py` on c42 with critic A's c42 criteria (exposed; more than 60 ms off the section's pcX median, Violins I +18 / Violins II +21 ms; relative crossover the same sign and more than 30 ms): 23 Violins I, 8 Violins II, 6 alias candidates. Run again on c41 (identical data): Violins I 67 / 97 and Violins II 257.5 / 260 / 644 read on time there (+12 / -17 / +12 / +5 / +30 ms against -62 / -80 / -120 / -90 / -87 in c42). They are round-robin variance, not lead errors. The remaining joins read within 12 ms in both renders except Violins I 544 (+54 / +182: kept at the mean). Violins I f62 231 / 232 (+75 ms) are under 60 ms from the Violins I median and stay out. Critic A's c41 list (31) and this one share 10 onsets; A's other joins (e.g. Violins I 268 -102, 444 +134, 496 -92) fail the crossover test on c42: their pitch change is on time and the lateness is the new note's slow rise, which is a fill problem, not a lead problem.

**Fix (`build/leg_leads.json`, new totals in s; factor 0.8 on the mean of c41 and c42, clamped ±0.12):**
- Violins I: 39 -0.10 (now -0.05), 47 +0.04 (now -0.05), 98 -0.06, 137 -0.10, 249 -0.10, 255.5 -0.08, 257.5 -0.06, 260 -0.06, 267 +0.06, 271 -0.07, 277 -0.06, 323 -0.05 (now +0.03), 395 +0.11, 397.5 -0.07, 544 +0.09, 558 -0.10 (now -0.03), 562 +0.06, 647.5 +0.12, 650 +0.08, 657.5 +0.09, 660 -0.07.
- Violins II: 255.5 -0.09, 256 -0.05, 361 -0.07, 404 -0.07, 649.5 -0.10; alias joins (bars 57-61) 230 +0.08, 231.5 +0.06, 239.5 -0.10, 242 +0.08.

Before the render, diff the moved onsets (`cycles/c33/actor_scripts/pdiff.py`) and confirm each lead took effect (finding 5). After it, re-measure with pcx.py and keep only joins that came closer; if CC16 (MANUAL-GAPS #6) goes into the same build, expect about 10% of violin joins to move by more than 30 ms on their own, and refit those on c43 rather than undoing them.

## 3. Outliers in the fast tempi outside the violins' legato: winds, brass, re-attacks and entries (measured)

**Where and what.** 55 exposed notes off the beat median by more than 60 ms in c42 and more than 45 ms in c41, also off the grid by more than 40 ms, robust to 60 ms smoothing (vibrato), and with no same-pitch note or pre-existing own-pitch energy in the 0.3 s before (I removed 12 that failed these checks: e.g. Violins II 364, -216 ms, measures the staccato before it). Legato joins also need the crossover off in the same direction by more than 30 ms. The audible groups:
- Horn 2's second-theme line (bars 57-67): 226 / 239 / 239.5 +78 / +72 / +79 ms late with the horn's 0.06 s legato lead, and 227 / 240 / 262 / 266 +86..+176 ms on pcX with the crossover on time: the new note blooms 7 dB over 0.35 s after an on-time change (240: new band 16 -> 27 dB from +0.05 to +0.40 s).
- Bassoon 1 in the development: entries 316.5 / 360 / 516 early by 62-112 ms with the 0.12 s entry lead; legato 413 late +139 ms.
- Horn 1 411.5 -184 ms (lead 0.21 s; the note speaks at -0.15 s), 420 +193 ms (lead 0.06).
- Re-attacks with no lead path: Violins II 172 (+186, Leg Slur MAX, lead 0), celli 607 (+209), 652 (+126), basses 94 / 97 (+140 / +87), Clarinet 1 234 / 422 (+105 / +94).
- Early re-attacks: Violins I 570.5 -173 (lead 0.10; the band rises at the moved onset), Oboe 1 91 / 396 -99 / -98 (lead 0.14), Horn 3 168 -104, Horn 1 600 -59 and 624 -71 (624 on LegRep RRx4, MANUAL-GAPS #2 note above).

**Fix.**
1. New generic per-onset table for re-attacks: `build/retongue_leads.json` {track: {score onset: s}}, read in `tools/score_to_parts.py` where the re-tongue / slow re-tongue / abut / string-stroke leads are set (`rt_lead_s()` and the `retongue_ok` branch), added to whatever lead the note gets and, as `ENTRY_LEADS` does, enabling a lead on a re-attack that gets none. Values in appendix A2 (factor 0.8, clamped ±0.12).
2. Legato and entry values in A2 into `leg_leads.json` and `entry_leads.json`.
3. Joins whose pitch change is on time but whose pcX is late (Horn 2 227 / 240 / 262 / 266, Bassoon 1 412 / 519 / 531, Oboe 1 540 / 546, Horn 3 501): no lead. Run `tools/auto_fills.py` on them and add a bloom cut where the new note rises more than 4 dB after +0.15 s (a `LEVEL_SHAPES_S` row or `JOIN_NOTCH` over the bloom, -3 dB from +0.15 to +0.45 s), fitted by simulation on the c42 stem.

## 4. String tremolo: chord changes early, tremolo entries late (measured)

**Where.** Joins (lead 0.22 s, `TREM_JOIN_LEAD_S`): Violins II bars 78-80 and the stringendo bars 111-116 (444-460), Violins II / Violas bars 147-151 (588-600), Violas 156. Entries: 144-156, 304, 440, 484, 488 (sostenuto), 664-676.

**Evidence.** Joins at lead 0.22 s: n 24, pcX median -73 ms, beat-median deviation -68 ms; in the stringendo -96..-191 ms (444 -125, 448 -96, 453 -191, 454 -133, 456 -127, 458 -103, 460 -113), so each tremolo chord change sounds about an eighth early under the violas' running eighths (score p.11: Vln II div. tremolo half notes, Vla eighths, poco a poco stringendo 129-138). With the 0.4 qn overlap the old chord also holds past the beat, so the change is smeared over 0.4-0.5 s. Entries: at `TREM_ENTRY_LEAD_S` 0.04 s pcX +30 ms (n 11), with no lead +58 ms (n 12; 488 and 668-676), deviation +37 ms in both. c37 measured these with the old estimator.

**Fix (`build/score_config.py`).** `TREM_JOIN_LEAD_S` 0.22 -> 0.15 (keep `TREM_JOIN_OVERLAP_QN` 0.4); `TREM_ENTRY_LEAD_S` 0.04 -> 0.08; the tremolo first notes with no lead (488 in all four sections, 668-676) +0.06 s in `entry_leads.json` (or an `ENTRY_LEAD_ART_S["string"]["Tremolo"]` of 0.06 if they go through the entry branch). Pass: tremolo joins within ±40 ms of the beat median, no join dip over 4 dB (the c08 reason for the long lead), the probe's tremolo checks pass.

## 5. Leads that the build silently cancels still move their fills: the celli 266 revert, and six slur-head targets held by the gap rules (measured)

**Where.** Violoncellos 266 (bar 67, rit.); Violas 76 / 368 / 428 and Violoncellos 265.5 / 412 / 594.

**Evidence.** c42 added +0.10 s to celli 266, but the note moved 265.6274 -> 265.625 qn (lead 0.220 -> 0.221 s): it is held by the `LEG_CAP_FRAC` 0.75 cap behind the eighth at 265.5 (0.75 of a 0.29 s slot). Its early fill moved anyway (`early_fills.json` pre_s 0.0 -> 0.1 "with the A #1 lead change"), so the 4.1 dB lift now ends 0.10 s earlier on the same note, and pcX went +170 -> +227 ms (crossover +194 -> +179). The lead was inert; the fill change made it worse. The six other targets are late by 74-179 ms behind an eighth (mostly a Sus MAX slur head with no lead: Violas 75.5 +34, 367.5 +83 ms; celli 411.5 +30), so `LEG_MIN_GAP_S` 0.10 s or the cap keeps the target from leading further (c42 set them back).

**Fix.**
1. Revert celli 266: `early_fills.json` pre_s 0.1 -> 0.0 (the operative change) and `leg_leads.json` 266 0.10 -> 0.
2. Generic check in `tools/score_to_parts.py`: print a warning for every `leg_leads.json` / `entry_leads.json` entry whose realised lead differs from the requested one by more than 0.02 s, and do not shift an early fill's pre_s by a lead change that did not happen.
3. For Violas 76 / 368 and celli 412 (heads on time or late): move head and target together with `GROUP_LEAD_AT` (0.06 s), then the A2 target values less 0.06. For Violas 428 and celli 594 (heads at -19 ms): a listed `LEG_MIN_GAP_S` exception of 0.05 s for those targets (a small generic extension: per-onset min gap) and the A2 values.

## 6. Tempo map: correct against the print; the phrase-arc steps from c37 #5 are still in it (map measured, audibility inferred)

**Measured.** Total 432.45 s (printed MIDI 430.04 s). Every bar's mean tempo is within 4% of the printed MIDI step except the arc ends (bars 14, 50, 55, 83, 102, 150, 159, 170, 174, all intended: arcs, the 636 caesura, the 679 fermata of 2.5 s). Keyswitches: all 1110 row changes arrive 9.5 ms or more before their note-on (median 18 ms). Cut-offs: the 679 fermata release spread among exposed parts 0.07 s (c37: 0.32 s); tutti cut-offs at 103 / 126 / 288 / 331 / 551 spread 0.15-0.33 s (c37: 0.30-0.53 s).

**Still open (inferred).** Inside constant printed tempi there are 76 beat-to-beat steps of 4% or more (one is the intended 636 caesura). The "main" arc ends slow the last beat to 88% and the next downbeat returns to 97% (+10.2%): 219 -> 220 (bar 56, the violins' cantabile entry), 331 -> 332 (bar 84), 407 -> 408 (bar 103), 695 -> 696 (+13.6%, bar 175). In the Allegro, arcs 324-332 and 396-408 run under continuous accompaniment, where a 10% jump on one downbeat can read as a hitch. Fix (`build/score_config.py` `PHRASE_ARCS`): change the two Allegro main arcs (324, 332, "main") and (396, 408, "main") to "sub" (`PHRASE_SLOW_SUB` (0.98, 0.95): end beat 95%, return +2%) or "open"; leave the Lento, Poco meno mosso and coda arcs. Diff keyswitches after any map change (kit LEARNINGS 20).

## Appendix A1: slow sections (finding 1), new totals in s, score onsets [pcX - 0.013 s, ms]

- `leg_leads.json`: Cello solo (alias tables) 685 -0.08 [-99], 687 +0.06 [+76], 690 +0.11 [+142], 691 -0.05 [-63], 694 +0.11 [+139]; Cor anglais 684 +0.12 [+189]; Double basses 4 +0.11 [+135], 7.5 -0.11 [-138], 10 +0.12 [+188]; Horn 1 50 +0.04 [+51]; Trombone 1 700 +0.12 [+167], 710 -0.08 [-102]; Trombone 2 710 +0.11 [+137]; Violas 496 -0.18 (now -0.08) [-128], 501 -0.19 (now -0.12) [-93], 684 -0.05 [-66], 696 +0.06 [+77], 712 +0.10 [+130]; Violins I 496 -0.06 [-78], 708 +0.04 [+56]; Violins II 36 +0.04 [+54], 39 -0.13 (now -0.09) [-51]; Violoncellos 44 -0.12 [-156].
- re-attack table: Bass clarinet 8 +0.06 [+71]; Bassoon 2 36 -0.06 [-70], 684 -0.06 [-69]; Clarinet 1 500 +0.04 [+55]; Double basses 8 +0.09 [+110], 20 -0.07 [-87], 36 +0.12 [+205], 40 -0.05 [-61], 712 -0.06 [-76]; Horn 2 488 -0.05 [-66]; Horn 3 48 -0.09 [-113]; Violas 50 +0.12 [+182]; Violins II 492 +0.07 [+90], 496 +0.12 [+219].
- `entry_leads.json`: Cello solo 680 -0.09 [-107]; Horn 1 49 -0.04 [-51]; Violins I 707 +0.22 (now +0.10) [+171; pp espr. entry: add an early fill, kit LEARNINGS 6]; Violins II 20 -0.04 (now +0.08) [-202]; Violoncellos 3 +0.04 (now +0.12) [-106], 20 +0.07 (now +0.12) [-60].

## Appendix A2: fast tempi (finding 3), new totals in s [deviation from the beat median, mean of c41 and c42, ms]

- re-attack table: Bass clarinet 429 -0.06 [-79]; Bassoon 2 250 +0.08 [+102]; Clarinet 1 234 +0.08 [+105], 422 +0.08 [+94]; Double basses 94 +0.11 [+140], 97 +0.07 [+87], 274 -0.06 [-72]; Horn 1 600 -0.05 [-59], 624 -0.06 [-71]; Horn 2 122 -0.06 [-76]; Horn 3 168 -0.08 [-104]; Oboe 1 91 -0.08 [-99], 396 -0.08 [-98]; Violas 440 -0.06 [-75]; Violins I 114.5 +0.05 [+64], 554.5 -0.06 [-72], 570.5 -0.12 [-173]; Violins II 111.5 +0.05 [+66], 172 +0.12 [+186], 277.5 -0.07 [-90], 366 +0.07 [+89], 564 -0.05 [-68]; Violoncellos 419 +0.06 [+81], 530.5 -0.05 [-60], 607 +0.12 [+209], 652 +0.10 [+126].
- `leg_leads.json`: Bass clarinet 435 +0.05 [+67], 435.5 +0.06 [+70]; Bassoon 1 413 +0.11 [+139]; Flute 1 395 +0.09 [+108]; Horn 1 411.5 -0.12 [-184], 419 +0.09 (now +0.04) [+62], 420 +0.12 [+193]; Horn 2 226 +0.06 [+78], 239 +0.06 [+72], 239.5 +0.06 [+79]; Trombone 1 521 -0.08 [-100]; Trumpets a2 665 -0.06 [-74]; Violas 76 +0.12 [+176], 368 +0.12 [+179], 428 +0.10 [+127], 600 -0.10 (now -0.05) [-59]; Violoncellos 183 +0.12 [+180], 265.5 +0.06 [+74], 412 +0.07 [+88], 594 +0.07 [+83] (Violas 76 / 368 / 428 and celli 265.5 / 412 / 594 need finding 5's head move or gap exception first).
- `entry_leads.json`: Bassoon 1 316.5 -0.05 [-62], 360 -0.07 [-89], 516 -0.09 [-112]; Flute 1 432 +0.06 [+69]; Violas 360 +0.07 [+92]; Violins I 464.5 +0.05 [+62]; Violins II 372 +0.01 (now +0.06) [-66], 472.5 -0.06 [-71]; Violoncellos 324 +0.08 [+99].
- Left out after checks: Bass clarinet 428, Horn 1 452, Horn 3 156, Violins I 628, Violins II 109.5 / 364 / 379.5 / 380.5, Violoncellos 517 / 528.5 / 533.5, Bassoon 1 40 / 517, Double basses 32, Violas 492 (a same-pitch note or the note's own pitch already sounding before the onset, or not robust to smoothing).

**Do not touch:** the family legato, entry, re-tongue and staccato leads (every path is within ±10 ms of the beat median); the c42 viola and celli leg_leads and their moved fills and notches (they moved 18 of 23 joins closer to the beat median), except the celli 266 revert; `tools/pcx.py` as the only estimator for string attacks; `CUTOFF_EARLY_S` (fermata spread 0.07 s); keyswitch timing; `TIMP_DELAY_S` 0.02 (timpani +3 ms); `GROUP_LEAD_AT` 270.25 and 606.5; the printed tempo steps, the stringendo, the 636 caesura, the 2.5 s fermata at 679 and the 30 bpm final bar; the f62 aliases' timing (identical to c41 per join); the render conditions that make wind and brass timing repeat note for note.
