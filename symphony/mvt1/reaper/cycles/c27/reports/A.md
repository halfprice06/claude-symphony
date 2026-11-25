# Cycle 27, critic A: articulation and phrasing (render c26)

Scope: every wind, brass and string note in `build/parts.json` (c26 after its stem fixes), measured on the c26 stems and master, with c25 (`cycles/c25/rendered_build/parts.json`, identical notes, keyswitches and CC lanes on every track) as the control, and older renders (c00-c24 stems) where a note's history mattered. I reran the c22-c26 battery on c26 (kscheck, ties, chordleg2, joins, acchf, stacsep, tremj, timp, harp, pz3, breath, ten200, cutoffs, rebow, longloop, reltime, relburst2, rests2, accpk2, accshape, pairs, rrcyc, detw2, efchk2, sstart, ssj, pkr3, xall). New scripts in `/private/tmp/claude-501/mockup-loop/mvt1-c27-A/`: `repscan2.py` (per-note c26 minus c25 on identical data), `cl1hist.py` / `prof.py` (one note's attack across all renders), `kspat.py` (keyswitch timing against render-to-render change), `stacrel.py` (staccato peak against the line's other notes), `afterstac.py` / `discon.py` (legato-row notes after staccatos or gaps), `holes.py` (master holes where the score sounds), `slurcov.py` (slurred transitions not on legato rows). Score pages 8-10 and 17 checked.

## Checks that passed (measured, no action)

- Keyswitches: shortest lead 14 ms; no chord on a legato row (chordleg2 empty); every keyswitch inside a sounding note is a planned row change. Ties: only the timpani re-strikes and the basses' re-bows re-attack. All as in c25.
- Slurs: every slur-internal pitch change on the winds and brass is on a legato row except Flute 1 393, Oboe 1 405 and Horn 1 413 (the c06 portato re-tongues, kept on purpose). The string ones on Sus MAX are the short_sus eighths (0.24 s at 126) and the divisi passages, as designed (c03/c06 tests).
- Legato joins: stem dip medians 1.6-2.5 dB (Vln I 2.0, Vln II 2.5, violas 1.8, celli 1.6); the 6 dB+ joins (Vln II 637/393/234, violas 361.5/378/612, celli 112/215) are the same as c25 and masked on the master.
- Item 8, brass: 2-5 kHz first 80 ms minus body median -8.3 dB (n 83); the four over +3 are Trumpet 1 284/670 and Horn 3 317/321, as in c25. Strings median -3.3; the 536 outliers are the previous f dyads' release (c26 A).
- Item 7: re-bow dip medians Vln I -3.0, Vln II -2.0, violas -2.6, celli -2.6, basses -1.4 dB; the two large steps are printed diminuendos (celli 163.877, 727.116). The final chord (712-728) master falls smoothly through the morendo, 1-2 dB steps at the staggered re-bows.
- Staccato separation (winds 8-11.6, strings 9-14 dB), pizzicato (-10 dB point +0.007 s), tremolo arrivals, breath gaps, tenutos, release bursts and tutti cut-offs all within 0.5 dB / 0.02 s of c25.

## 1. Fugato, bars 84-93: the string staccatos play 4-11 dB over the subject's legato notes and its accent, and the celli's mp C of bar 88 leaves a 10 dB hole (measured)

**Where.** Violoncellos qn 336.5-348.5 (subject, bars 85-88, the only sounding voice: celli = master within 0.1 dB), Violas 348.5-360 (with Bassoon 1), Violins II 362.5-372 (with Cor anglais). Score page 9: mf, accent on the subject's long note, staccato eighths and quarters, then the C at 348 marked mp as the next entry comes in mf.

**Evidence (measured).**
- Celli body levels (score onset +0.03 to +0.25 s): accent 337 -28.6, staccatos 338.5 / 339 / 339.5 -32.1 / -26.1 / -27.0, the unmarked quarter 340 -36.1, slur 341 / 341.5 -34.4 / -35.8, the accent 342 -31.8, staccatos 343.5 / 344 / 345 / 346 / 347 -27.9 / -28.0 / -29.8 / -31.6 / -34.3, the C 348 -45.4. The second accent (342) sits 4 dB under the staccatos that follow it.
- `stacrel.py` (staccato 50 ms peak minus the median peak of the non-staccato notes within 2.5 qn): celli at CC11 72 median +5.6 dB (max +16.2 at 346, +11.0 at 347, +7.6 at 339). Violas +2.2 median (358 +5.0). Violins II 367.5 +9.6 (louder than the accent at 366: -27.9 against -29.9 dB). The doubling winds' staccatos (played Sus, shortened) sit -2.4 (Bassoon 1) to -6.4 dB (Oboe 1) under their neighbours, so each doubled entry is out of balance between its two instruments.
- Cause: `ROW_TRIM_DB` (score_config.py line 239) trims Stac RRx9 by -4 dB only at CC11 >= 80. The fugato is mf (CC11 72), so the Stac row plays untrimmed, 5-8 dB over the Leg rows at the same CC11 (kit LEARNINGS section 8 / mvt1 c04 note).
- Bar 88 hole: the C at 348 is a disconnected Leg Slur MAX first note (moved to 347.761, v63, CC11 58), the slow first-note layer. The celli's +3 role [338,348] and the +1.5 LEVEL_SHAPES ramp (line 1178, ending (348.0,1.5),(348.3,0.0)) both end on it. Master 348.0-348.5 -43.9 dB against -34.3 (347.0-347.4) and -36.1 (348.5-349.2). The hole has been there since c11 (c11-c26 master 348.0-348.5: -43.0 to -44.6). `holes.py` finds it as the deepest master hole with notes sounding in the score. The rest of the celli countersubject (349.5-351) stays at -45.8 to -50.1, 7-9 dB under the mf violas and bassoon, more than the printed mp/mf step.

**Fix.** Level steps plus one row change. Simulate the trims on the c26 stems with `stem_fix.py` first.
- `build/note_trims.json`, as steps (add the onsets to `NOTE_TRIM_RAMP_S` at 0.1, as in the c03 `_steps` block):
  - Violoncellos: -4 dB at 339.0, 339.5, 343.5, 344.0, 345.0, 346.0, 347.0, and -2 at 338.5.
  - Violas: -2.5 at 350.5, 351.0, 351.5, 356.0, 358.0.
  - Violins II: -5 at 367.5.
- Do this with note trims, not by lowering the `ROW_TRIM_DB` threshold. ROW_TRIM needs a Leg-row note within `ROW_TRIM_NEAR_QN` (3 qn), so 344 would stay untrimmed. If 348 becomes Sus MAX (below), none of 343.5-347 would be trimmed either.
- Celli 348: add 348.0 to `DOWNBOW_STROKE_AT["Violoncellos"]`, so it is a fresh Sus MAX stroke at the score onset. The bow does change after the staccato.
  - Extend the line-1178 shape to `(348.0, 1.5), (348.5, 1.5), (348.8, 0.0)`.
  - Extend the role `[338, 348, 3]` to `[338, 348.5, 3]`, so the printed mp comes from CC11 alone.
  - Fallback, if the Sus MAX stroke measures under target: keep the row and add a +5 dB step note trim at 348.

**Pass.**
- Celli staccato peaks minus the non-staccato neighbours: median between -2 and +2 dB, max at most +6.
- Violas median +1 or less; Violins II 367.5 at most +3.
- The accent 342 at or over the staccatos 343.5-344.
- Celli 348 body (score onset +0.03..+0.4 s) at -39.5 dB or higher.
- Master 348.0-348.5 at -40 dB or higher.
- Celli 349.5-351 within 6 dB of the violas.
- Master per bar 85-92 within 1.5 dB of c26 (C's fugato lifts of c06/c17 stay).

## 2. Clarinet 1, bars 103-106 (and 626): the re-tongued accents render in one of two attack states at random; c26 drew the bright one (measured; cause inferred)

**Where.** Clarinet 1 (the a2 line, with Oboe 2, f), qn 414 and 422 (`g4.->` after a two-note slur, score page 10). Also 626, 250 and 282, in the same pattern: Sus Non Vib re-tongue after a Leg Slur note, keyswitch 5 ms after the previous note-off and 29 ms before the note.

**Evidence (measured).**
- **Identical data.** Clarinet 1's notes, keyswitches, CC11, CC1 and volume envelope over 405-424 are byte-identical in c25 and c26. Over the whole track, only the c26 retransition envelope at 504.75-513.2 and the coda shape differ.
- **c26 against c25.**
  - First 80 ms: 414 +4.3 dB louder and +6.8 dB at 2-5 kHz; 422 +5.8 / +5.8; 626 +3.6 / +6.8.
  - Stem 2-5 kHz front-minus-body: 414 +6.4 (c25 -2.4); 422 +4.0 (c25 -4.3).
  - Attack profile at 20 ms: the bright state reaches full level and its 2-5 kHz peak at once. The other state comes in slowly, with the 2-5 kHz rise 0.08-0.16 s late.
- **Master.** 2-5 kHz first 80 ms over the 0.3 s before:
  - 414 +7.4 dB (13.5 against 6.1) and 422 +5.7 (14.1 against 8.4), against +4.4 / +1.9 in c25.
  - Clarinet 1 is the top 2-5 kHz source in both windows.
  - These are the brightest wind accents on the c26 master. Item 8's cap is about +3.5.
- **History.** 414 front-minus-body over c14-c26:
  - Bright (+1.2..+6.4) in c16, c17, c19 and c26.
  - Dull (-10..-15) in c14, c15, c18 and c20-c22, and -2..-5 in c23-c25.
  - c18 -> c19 -> c20 had identical local data (same hashes) and went dull -> bright -> dull.
  - The state does not follow the data.
- **Keyswitch timing is not the cause.**
  - Of 130 wind/brass re-tongues with the keyswitch 0-30 ms after the previous note-off, 6 changed by more than 3 dB between c25 and c26; 5 of those are Clarinet 1.
  - Many Clarinet 1 notes with the same 5/29 ms timing are identical to 0.0 dB (106.5, 110, 114.5, 228, 418.5, 421).
  - So the timing is not what decides it; the flips cluster in regions (410-422, 506-534, 250-282). Cause unknown: possibly Opus sample streaming or a random sample choice (inferred).
- **The per-note tables are chasing it.**
  - `note_trims.json` Clarinet 1 414 -6.5, 417 -3, 422 -4 (set from c13 on, "stood 5 dB over their neighbours", and refitted since).
  - `accent_fits.json` 414/417/422 at the [5.0, 1.0] cap.
  - `early_fills.json` 411.5 +8 dB.
  - Result in c26: the a2 line (Clarinet 1 + Oboe 2 power sum per note) swings from -29.2 to -37.7 dB within an f phrase. The slur pair 413/413.5 sits 5-6 dB under the quarter before it, and the accents land +4.5 / +6 dB over the pair before them, in the bright state.

**Fix.**
- (a) **Post-render state check, every cycle.** Measure Clarinet 1's stem 2-5 kHz front (0-80 ms) minus body (+0.15..+0.5 s) at 414, 422 and 626 against c25 (dull) and c26 (bright).
  - If a note is bright (front-body over 0 dB), apply a level-only stem fix through `LEVEL_SHAPES_S["Clarinet 1"]`: -5 dB from the score onset to +0.12 s, back to 0 by +0.30 s.
  - Simulated on c26: master front-pre 414 +7.4 -> +4.9 and 422 +5.7 -> +2.6. The body and the accent's weight stay.
  - If dull, leave it.
- (b) **Freeze the per-note tables.** Do not refit accent_fits, note_trims or early_fills for Clarinet 1 at 408-424 and 620-628 from a single render. A fit made in one state is wrong in the other.
- (c) **Record it.** Add to `loop/LEARNINGS.md`: identical-data renders flip Clarinet 1's re-tongue attacks between two states.

**Pass.**
- The c27 render is classified at all three notes.
- Where bright: after the fix, master 2-5 kHz front-minus-pre at +3.5 dB or less at 414 and 422.
- No table entry at these onsets changed by a fit.

## 3. Doubled brass lines still play one player at +3 dB (patch; inferred, carried, short)

- `unison_dropped` is unchanged:
  - Trombone 2 29 notes (bars 80-81, 117-121, 131-134).
  - Trumpet 2 21 (the coda theme 167-170, and 131-132).
  - Horn 4 18 (41-42, 80-82, 158-161).
- The coda theme (Trumpets 1-2 a2 + Horns a2 + violas, ff) is the most exposed of these.
- The fix and memory route are as in c26 A #2: `2 Trumpets/04 Legato/2TP Leg Slur MAX.oib` for 664.4-676.5, and `2 Trombones` Leg Slur MAX for 520-536. Do this only if the settled footprint stays at 45 GB or less.
- No new measurement separates two players from one louder player. Leave it for a cycle with its own render if memory allows.

## Do not touch

- Keyswitch, legato lead and cap tables; short_sus and SHORT_SUS_LEG_TRACKS (Vln I only); PORTATO_JOIN_AT re-tongues; ABUT_LEAD and STAC_LEAD_S.
- The re-bow times with rebow_fills (including the final chord); the brass GENTLE_ACCENT swell timing; the Marc LITE strokes; Leg Port 225/685.
- The timpani, harp étouffez, pizzicato, tremolo and MEAS_TREM settings; the Violins II sul tasto EQ.
- The c26 dolce-theme shapes (celli 595.65-599.6 and 193.2-199.6, Horn 1 596.1-599.6 and 196.1-199.6).
- The fugato roles of c06/c17. Only the staccato trims and the 348 changes in finding 1.
