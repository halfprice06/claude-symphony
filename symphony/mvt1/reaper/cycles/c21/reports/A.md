# Cycle 21, critic A: articulation and phrasing (render c20)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the stem-fixed c20 build), measured on the c20 stems and master (`cycles/c20/render/`), with c19 as the control. Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c21-A/`. I reran the c20-A battery on c20 (outputs `o20_*.txt`), after changing `joins.py` and `chordleg2.py` so that they count "Slur Runs" as a legato row. New scripts: `reltime.py` (time to fall 3 and 10 dB after the note-off, per track and row), `cutoffs.py` / `cutsim.py` (tutti cut-offs per stem, and a simulation with shorter celli and basses releases), `rests2.py` (lowest level inside a short rest, against the note before it), `kscheck.py` (keyswitch timing), `rel.py` / `rel2.py` / `rel3.py` (AHDSR release values read from the `.oib` files), and `tr.py` (traces).

## Checks that passed (measured)

- **Legato.** No chord goes to a legato row. Wind and brass joins: none at 6 dB or more. String joins at 6 dB or more: 4. These are celli 112, 215 and 689.5 and violas 612; the same four were there in c19, and none shows on the master. The c19 join fills held.
- **Accents (item 8).** 2-5 kHz in the first 80 ms minus the body: brass median -8.1 dB, winds -5.8, strings -3.0, all unchanged from c19. The string outliers (violas 536 +13.0, celli 536 +10.6) are not attacks. That beat is a subito mf after ff, and the trace shows the release of the ff eighth before it. Trumpet 1 284 reads +7.7 dB, but it sits 15 dB under the master, as in c20.
- **Re-bows and loop pulsing (item 7).** No new re-bow step. The largest dip, Violins I 48.597 (-5.3 dB), falls inside the printed decrescendo of bar 13, and the trace is smooth through the re-bow. On the longloop table, no held note within 6 dB of the master pulses at the loop period.
- **Keyswitches.** The shortest lead to a note is 14 ms, with no lead under 4 ms. Every keyswitch that falls inside a sounding legato note is a planned switch between legato rows (Leg Slur and Leg BC) or a slur-start join.
- **Other techniques.** Pizzicato is on time (median -10 dB point +0.005 s). Tremolo joins: median dip -1.1 dB, one at 4 dB or more. Stem staccato separation: median 8.8-15.1 dB. Tenuto portato joins: 3 dB or less. Breath marks dip 3-15 dB. Ties are held. The timpani strokes and rolls and the harp étouffez are unchanged from c19.

## 1. Strings on Sus MAX hold their release 2-4 times longer than the same sections on Leg Slur, so rests and tutti cut-offs in the low strings do not stop (measured; fix inferred, test)

**Where.** Every string note on the Sus MAX row (1,100 notes: violas 488, basses 331, Violins II 134, celli 94, Violins I 54) that ends before a rest or a new attack. The clearest places:
- the violas' off-beat dyads, bars 131-134 (qn 520.5-535);
- the basses' ff repeated eighths, bars 27-31 (qn 104-124) and 131-134;
- the tutti cut-offs at qn 103, 126, 331 and 551.

**Evidence: release times (measured, `reltime.py`).** Time for the stem to fall 10 dB after the note-off, for notes followed by at least 0.9 s of silence on that track:

| Track | Sus MAX | Leg Slur MAX, same stem |
|---|---|---|
| Violoncellos | 0.47 s (3 dB down at 0.26 s) | 0.12 s |
| Double basses | 0.35 s | |
| Violas | 0.30 s | 0.15 s |
| Violins I | 0.22 s | 0.17 s |

- Woodwinds take 0.10-0.21 s and brass 0.16-0.30 s.
- The cause is in the patch files (`rel3.py`):
  - Celli KS Master sustain groups "Vc mf/f/ff": AHDSR release 524 ms; "Vc p" 700 ms; "Vc pp" 931 ms.
  - Basses KS Master: "Db f/ff" 524 ms, "Db mf" 700 ms, "Db pp" 931 ms. The Detache row is 700 ms.
  - The legato transition groups (TLeg) of the same patches: 100-237 ms.
  - The 1st Violins sustain groups: 133-316 ms. This matches the order measured above.
- The recorded release trails are separate groups (for example "Vc ff RT", 131-165 ms), so a shorter sustain release does not remove the natural release.

**Evidence: rests (measured, `rests2.py`).** In the Allegro, take every short string note before a rest (median rest 0.18 s) and find the lowest point inside the rest:
- On Sus MAX the stem falls only 4.1 dB under the note before (median), and 36 of 41 cases fall less than 6 dB.
- The violas' off-beat dyads in bars 131-134 fall 1.8-5.7 dB (median 4.1 dB, n 26). Each written eighth plus eighth rest plays as 0.626 qn including the 0.126 qn entry lead, so the real rest is 0.18 s, shorter than the release.
- Woodwinds over rests of the same length fall 9.6 dB (3 of 22 under 6 dB).

**Evidence: repeated eighths (measured, `repsep.py`).** The basses' ff repeated eighths in bars 27-31 re-attack with a median dip of 0.5 dB (n 34), against 3.9 dB for the contrabassoon in the same bars. In bars 131-134 the basses dip 1.8 dB. A 524 ms release is still about -5 dB when the next eighth starts 0.22 s later, so the eighths run together into one held note with small bumps. This also explains why the c13 Detache test failed: that row's release is 700 ms.

**Evidence: cut-offs (measured, `cutoffs.py`).** Time to -10 dB after the written end:

| Cut-off (qn) | Celli | Basses | Woodwinds | Master |
|---|---|---|---|---|
| 103 | 0.34 s | 0.23 s | 0.04-0.22 s | 0.20 s |
| 126 | 0.47 s | 0.31 s | | 0.30 s |
| 331 | 0.25 s | | | 0.23 s |
| 551 | 0.47 s | 0.44 s | | 0.28 s |

- At qn 126 the celli hold full level for about 0.25 s after the note-off. The rest there is half a beat (0.238 s), so it never sounds in the bass.
- Celli and basses carry 35%, 54%, 34% and 52% of the master's energy 0.1-0.4 s after these four cut-offs (`cutsim.py`).
- Simulation: with the celli and basses falling 10 dB faster, the master reaches -10 dB at 0.15/0.19/0.18/0.21 s instead of 0.20/0.30/0.23/0.28 s.
- Critic C (c20 #5) measured hall-recording tutti stops at 0.08-0.14 s. LEARNINGS section 6 records the same slow release as the reason the basses needed ABUT_LEAD 0.16 s on pitch changes (old pitch -10 dB only after 0.46 s).

**Fix (test on Violoncellos, Double basses and Violas; full rebuild of these three tracks).**
- `tools/build_reaper.py` `state_for()`: a new per-track mix key next to `env_release_ms`, for example `"sus_release_cap_ms": {"ms": 250, "dyn": ["mf", "f", "ff"]}`.
  - It lowers the AHDSR `release` to 250 ms, but only on the sustain groups of the Sus MAX row. These are the groups under the `[[[Non Vib]]]` / `[[[Sus Vib]]]` / `[[[Molto Vib]]]` folder groups (type 3), with names ending in mf, f or ff (e.g. "Vc ff", "Db f", "Dbs mf").
  - It leaves alone the RT groups, the TLeg groups, the groups under `****sus looped****` (legato sustains) and every short-note row (Stac, Spic, Marc, Pizz, Detache, Trem, Runs).
  - Leave the pp/p groups as they are, so that soft endings (Lento, morendo) keep their long fade.
  - Before writing, print the list of matched group names per patch and check it.
- `build/mix.json`: add the key to Violoncellos, Double basses and Violas.
- Refit after the render, because each of these items assumed the long release:
  - `fit_rebows.py` for the three tracks. The old re-bow piece ends 0.03 qn early, and its 524 ms tail now covers the gap.
  - `auto_fills`.
  - `ABUT_LEAD` Double basses 0.12/0.16 and Hn3-4: re-measure the takeover and reduce it if the new pitch now arrives early.
  - The coda basses attack steps (c20 C #2).
  - The accent fits for those tracks.
- If the stems show no change, the instrument-level `envelope.releaseTime` (931 ms in all four string KS Masters) is the operative one. Set it too, and then check the pizzicato rows: basses 38 notes, celli 4.

**Pass.**
- Sus MAX -10 dB after the note-off at 0.22 s or less on all three tracks (currently 0.30-0.47 s).
- Violas, bars 131-134: rest minimum at least 7 dB under the note.
- Basses, bars 27-31: re-attack dip median at least 2 dB.
- Master -10 dB at 0.20 s or less at qn 126 and 551.
- String joins at 6 dB or more: not more than 4. Re-bow dip medians within 0.5 dB of c20 after the refit.
- pp endings (celli 52, violas 720-728) unchanged.

**Fallback if the patch change fails.** Use MIDI only: end Sus MAX string notes of 0.75 qn or less 0.12 s early when they are followed by a rest in the Allegro. LEARNINGS 7: a note ended 0.25 qn early left a 13 dB break. For the basses' ff eighths, test the Basses `Marc Lng RRx4` row (key 78, release 316 ms) on bars 27-31.

## 2. Bar 152 (qn 606.5-607.5): the top F of the crescendo comes in under the run that leads to it (measured; fix inferred)

**What the score has.** The violas' and celli's 32nd-note run (B-C-D-E) and the tied F are unslurred: there is no slur event for Violas or Violoncellos between 605.5 and 611. The F is therefore a new bow at the top of a crescendo.

**What is played (measured).**
- The F is a Leg Slur MAX target joined from the Sus MAX E, with GROUP_LEAD 0.12 s.
- Violas stem: the run sits at -39..-40 dB. The F then falls to -41..-43.6 dB from its onset to 607.6, and only reaches -38 dB at 607.74. The top of the crescendo is 3-4 dB under the run before it.
- The F first leads at +0.11 s (violas) and +0.21 s (celli) (c20 CHANGES, same render).
- LEARNINGS 6: a Sus-to-Leg join plays the slow first-note layer.

**Fix.**
- `build/score_config.py`: play the F as a fresh Sus MAX stroke, as with STR_ACC_AFTER_SUS / DOWNBOW_STROKE_AT. Add `("Violas", 607.0)` and `("Violoncellos", 607.0)` to that list:
  - CC11 held at the entry level from the moved onset;
  - velocity at least 105;
  - keep the GROUP_LEAD 0.12 s;
  - the run's E ends at the F's moved onset.
- The F still joins 609 E as a legato transition, with SOST_JOIN_LEAD_S on the join.

**Pass.**
- F within 3 dB of its body by +0.10 s from its score onset in both sections.
- F body (607.1-607.6) at least 1 dB over the run.
- No hole of 5 dB or more on either stem over 606-608.

## 3. Bars 55-63 (qn 220-252): the celli's slurred arpeggios arrive late on their rising leaps (measured)

**Measured** (`xall.py`, `runs2.py`).
- 16 of the 49 slurred steps in the exposition second-theme accompaniment cross over more than 0.12 s after the score onset (median +0.085 s, p75 +0.150).
- For comparison, the celli second-theme melody (bars 47-54) has a median of +0.062 s.
- The late steps are rising fourths to sixths out of the low first note of each group: 224.5 (+5 semitones) +0.21 s with dominance 0.09; 239.0 +0.157; 243.0 +0.179; 233.5 +0.17; 221.5 +0.153.
- Each eighth is 0.268 s long, so these pitches sound for less than half their length.
- The cause is the cap. The targets are led 0.225 qn (0.12 s), which is the LEG cap (0.45 × the 0.5 qn note before). A lead from the tables cannot add anything here.
- The celli sit -9.5..-10 dB under the master in bars 56-59 and carry the harmony under the violins' melody.
- The recapitulation has the same figure: 620.5 +0.20, 621.0 +0.14, 626.0 +0.155 s.

**Fix.**
- `build/score_config.py`: LEG_CAP_FRAC 0.75 for Violoncellos over [219, 252] and [616, 632]. This is the c19 violas-triplet mechanism (LEARNINGS 5).
- Add a per-interval extra of +0.06 s for rising steps of 5 semitones or more on those spans (`build/leg_leads.json` pair extras).

**Pass.**
- Median first lead at +0.07 s or earlier; none later than +0.15 s.
- Note-on spacing at least 0.2 s.
- Celli joins of 6 dB or more not increased.
- Check the falling steps from the same pitches in both directions (LEARNINGS 5).

## 4. Violins I slurred runs: the first step of bar 68 and the sf arrival of bar 40 are still late (measured)

**Measured** (`runs2.py` on c20, Slur Runs row).
- Bar 32 passes: dominance 0.60-0.80, first lead +0.047..+0.072 s.
- Bar 68 (qn 270-272):
  - The first step, A♭4 (head, v53) to C5 (270.25), is a major third. The row has only half-step and whole-step scale samples, so this step plays the slow LegSl transition. C5 first leads at +0.217 s and has dominance 0.00 in its 0.119 s, so it is never heard. The rest of the run passes (0.71-0.97).
  - Violins I is the loudest stem here (-6.0 dB re master in c19).
- Bar 40 (158-160):
  - 158.25 has dominance 0.00 and 159.0-159.5 have 0.44-0.52.
  - The sf target 160 (Leg BC) leads only at +0.206 s.
  - Violins I sits 14 dB under the master there, under the flute and oboe doubling, so this is the lower priority.

**Fix.**
- For 270.25: give the head 270.0 the LEG_CAP_FRAC 0.75 exception and add a per-onset extra of +0.10 s for Violins I 270.25 (`leg_leads.json`), so that C5 starts about 0.1 s earlier.
- For 160: add a per-onset leg lead extra of +0.10 s (Violins I 160, Leg BC).
- Leave bar 32 unchanged.

**Pass.**
- 270.25 first lead +0.08 s or earlier, with dominance at least 0.4.
- 160 first lead +0.10 s or earlier.
- No new 6 dB join hole at 272 or 160.

## Patches

- One patch-state test (#1: shorter sustain release on the Sus MAX row of three string tracks). It needs full rebuilds of Violoncellos, Double basses and Violas but no new rows, so memory is unchanged.
- The Basses `Marc Lng RRx4` row is the fallback for the ff eighths.
- No other patch change is indicated:
  - Hollywood Strings has no sul tasto tremolo (c20-A).
  - The violas and celli KS Masters have no Slur Runs row.
  - The Solo French Horn `Leg Slur Rep MAX` row is not needed while WIND_REP_RETONGUE holds (horn repeat dips 4-5 dB).

**Do not touch:**
- GENTLE_ACCENT, ACC_ART_LEAD and the brass/wind/string accent fits (brass 2-5 kHz front -8.1 dB, front-body +3.6 dB);
- the Slur Runs spans for bars 32 and 68, and `_lg()`;
- SLUR_HEAD_LEAD lead_s 0.10;
- the c19 converted join fills and the c18 Violins I fills;
- the AUTO_REBOW rows and shapes, apart from the refit that #1 requires;
- TREM_JOIN/TREM_SPLIT;
- MEAS_TREM alt_row;
- WIND_DETACH, RETONGUE_LEAD_S and WIND_REP_RETONGUE;
- breath splits and CAESURA_BREATH_QN;
- harp env_release_ms 200 with HARP_RING_S;
- TIMP_CC1_MAP / TIMP_ROLL_TRIM_DB and the re-strike plans;
- the sus. cymbal key 64 / lead 0.25.
