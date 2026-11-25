# Cycle 24, critic A: articulation and phrasing (render c23)

Scope: every wind, brass and string note in `cycles/c23/rendered_build/parts.json`, measured on the stem-fixed c23 stems and master (`cycles/c23/render/`), with c22 (`cycles/c22/render/`, `cycles/c22/rendered_build/parts.json`) as the control. Feature caches (5 ms hop: power, 2-5 kHz, 100-300 Hz, centroid) were built for both renders. I reran the c22-A battery on c23 (joins, kscheck, ties, rebow, longloop, acchf, accpk2, accshape, pkr3, ssj, pairs, stacsep, tremj, timp, harp, pz3, breath, ten200, rests2, cutoffs, reltime, relburst2, efchk2, detw2, rrcyc). New scripts: `accx.py` (each accent's 0-0.30 s level against the next two and previous two plain notes on its track), `lvl2.py` (the same window on every note, c22 against c23), `accbr.py` / `mj.py` (2-5 kHz front minus body on the stem, spectral tilt, and the master's 2-5 kHz jump at every accented onset), `ham.py` (accent + down-bow strokes), `hn.py` / `line.py` / `tr2.py` (note and phrase traces), `pk2.py` (slurred pickups). Score pages 3-4 and `mockup-events.tsv` for the marks. Patch rows read with `opus_state.load_oib`.

## Checks that passed (measured, no action)

- Legato: no chord on a legato row; wind and brass joins of 6 dB or more 1 (Clarinet 1 213, 6.1; c22 3.6); string joins of 6 dB or more 7 (Vc 112 8.1, 215 6.3; Vla 361.5 7.9, 378 6.2, 612 6.0; Vln II 637 6.7, 234 6.1). None shows on the master by more than 2 dB.
- Keyswitches: shortest lead 14 ms, none under 4 ms; every switch inside a sounding note is a planned row change. Ties: held.
- Item 7: no held note within 6 dB of the master pulses at the loop period. Bass clarinet C3 at qn 11 (acf 0.58 at 3.95 s, -6.1 re master) is the known one. The final chord: Vln I 720 acf 0.14 / centroid 0.19, Vln II 712 -0.12 / 0.16. The high acf on wind notes at 684 and 48 (Bassoon 2) comes from already re-tongued notes, not one sample.
- Re-bows: unchanged from c22 within 0.4 dB (median dips Vln II -2.0, Vla -2.2, Vc -2.3, Cb -1.2).
- Staccato separation, pizzicato onsets (median -10 dB point +0.005 s), tremolo joins (about -1.5 dB), timpani strokes, harp étouffez, breath marks, tenutos, release bursts: all within 1 dB of c22.
- The c23 swell shape itself works. On the Sus MAX hammer controls (bars 32 and 72, upper strings and violas), front (-0.03..+0.15 s) minus body (+0.30..+0.75 s) moved from -7.4..+0.2 to -5.2..+2.7 dB, and the peak from +0.26..+0.46 to +0.01..+0.20 s, with no Marc LITE row.

## 1. The c23 front-window accent refit overshoots: 13 wind and string accents rose 4-7 dB and now stand 5-9 dB over their line (measured)

**Where.** The first-theme heads and the other slurred accents in the Allegro:
- Oboe 1 105, Clarinet 1 105 (bar 27, ff tutti theme);
- Clarinet 1 151, 273, 505, 521;
- Bassoon 1 382;
- Violins II 325, 381, 525; Violas 325; Violoncellos 382, 521.

**Evidence (measured, `lvl2.py`, `accx.py`, score onset to min(+0.30 s, next onset)).**
- Plain notes: median change c22 -> c23 is 0.0 dB. Accents: winds median +1.5 dB, 18 of 54 rose 3 dB or more; strings median +0.4 dB, 19 of 96 rose 3 dB or more.
- Accents 6 dB or more over the next two plain notes on their own track: winds 3 -> 7, strings 13 -> 19. Brief rule 4 asks for about 2-4 dB.
- The worst, rise c22 -> c23 / level over the next plain notes / over the previous plain note:

  | Note | Rise | Over next | Over previous | Re master |
  |---|---|---|---|---|
  | Oboe 1 105 | +7.1 | +6.2 | +10.5 | -9.0 |
  | Clarinet 1 151 | +7.0 | +6.9 | +9.3 | -7.0 |
  | Bassoon 1 382 | +6.3 | +8.6 | +9.6 | -8.4 |
  | Clarinet 1 521 | +5.4 | +4.6 | +8.7 | -7.9 |
  | Clarinet 1 273 | +5.0 | +6.9 | +6.7 | -6.8 |
  | Violins II 325 | +5.0 | +8.1 | +4.6 | -9.8 |
  | Clarinet 1 505 (p solo) | +4.9 | +4.6 | +2.8 | -0.6 |
  | Violoncellos 521 | +4.5 | +7.5 | -0.1 | -6.4 |
  | Violoncellos 382 | +4.4 | +5.0 | +5.8 | -8.0 |
  | Violins II 381 | +4.2 | +8.7 | +4.5 | -3.4 |
  | Violins II 525 | +4.2 | +7.4 | +3.6 | -9.1 |
  | Violas 325 | +4.1 | +8.1 | +3.1 | -12.2 |
  | Clarinet 1 105 | +4.1 | +6.6 | +8.6 | -9.9 |

- Bar 27 (score page 3, the ff tutti theme in flutes, oboes, clarinets and violins): Oboe 1 105 now sits at -26.3 dB against -32.5..-36.8 for its neighbours. The oboe is the loudest woodwind on that one note (front -9.4 re master; Flute 1 -10.6, Clarinet 1 -10.1, Violins I -10.0). In c22 it sat 6 dB under the flute. The woodwind block jumps 4-7 dB on the theme's first note and falls back on the next.
- The fit values show the cause: accents at the swell+step cap went from 18 to 39 (winds, cap 6 dB) and from 37 to 75 (strings, cap 4.5) between `cycles/c23/before/accent_fits.json` and `build/accent_fits.json`. For example, Oboe 1 105 went from [0.0, -1.83] to [5.0, 1.0] and Clarinet 1 105 from 0 to 3.52.
- Inferred: 9 of the 13 notes are slurred targets of an eighth pickup (104.5, 150.5, 272.5, 381.5, 520.5, 324.5...). Their 0.18 s front window falls in the legato transition sag, so the fitter read them as weak and drove them to the cap. The body then blooms on top of the swell.
- The master's 2-5 kHz jump at accented onsets rose by a median of 0.5 dB. Jumps of 6 dB or more went from 4 to 8, at qn 337, 366, 510 and 568 (`mj.py`). This part is front level, not a brighter sample: on the stems the 2-5 kHz tilt, front minus body, moved only -2.2 -> -1.2 dB for winds and -1.1 -> -1.0 dB for strings.

**Fix.**
1. Level only, by `stem_fix.py` now. On each note in the table, cut by min(rise, over-next - 3.5) dB from the score onset - 0.03 s to +0.35 s, with a 0.03 s ramp in and a 0.15 s ramp out. Values:
   - Oboe 1 105 -2.7; Clarinet 1 151 -3.4, 273 -3.4, 105 -3.1, 521 -1.1, 505 -1.1;
   - Bassoon 1 382 -5.1;
   - Violins II 325 -4.6, 381 -4.2, 525 -3.9; Violas 325 -4.1;
   - Violoncellos 521 -4.0, 382 -1.5.

   Write the same values into `build/accent_fits.json` as reduced swells, so the next build keeps them.
2. Tool (`tools/fit_accents.py`). Add a `--line-max` guard (default 5.0), applied after the front-window iteration:
   - measure the accent and its next two plain notes on [score onset, min(+0.30 s, next onset)];
   - if the accent is more than `--line-max` dB over them, lower the swell by the excess plus 1 dB.

   Lower `--max-total` for winds from 6.0 to 4.5. For a slurred target whose previous note is a pickup of 0.5 qn or less, measure the front from score onset + 0.10 s, past the transition sag.

**Pass.** Accents 6 dB or more over the next plain notes: winds 3 or fewer, strings 13 or fewer, as in c22. The front-body gain of c23 holds: accented minus plain front-body at least +2 dB per family. At bar 27, Oboe 1 105 is no louder than Flute 1 105 on the front.

## 2. The Marc LITE half notes at bar 142 collapse after the stroke, and the Violins I 566 stroke bites (measured)

**Where.** Violins I and II, qn 564 and 566. These are half notes in octave unison, accent + down-bow, in the recapitulation (bar 142). They were on Sus Marc LITE in c23 (the A #2 test).

**Evidence (measured, `hn.py` / `ham.py`).**

| Stroke | Front 0-0.25 s, c22 -> c23 | Body 0.30-0.60 s, c22 -> c23 | Body 0.60 s-end, c22 -> c23 | Body re master, c23 |
|---|---|---|---|---|
| Violins I 566 | -25.7 -> -21.6 | -26.4 -> -32.5 | -28.2 -> -33.8 | -13.7 (c22 -8.8) |
| Violins II 566 | -28.0 -> -24.1 | -29.5 -> -32.5 | -30.7 -> -34.4 | -14.2 (c22 -11.3) |
| Violins I 564 | -23.3 -> -19.0 | -20.3 -> -22.5 | -24.6 -> -25.7 | -7.4 |
| Violins II 564 | -27.6 -> -24.5 | -27.2 -> -29.3 | -27.5 -> -28.1 | -9.8 |

- Violins I 566: front minus body +10.8 dB (c22 +0.6). 2-5 kHz first 80 ms minus body +10.4 dB (c22 -3.1). Over its next note +15.7.
- The half note now sounds as a 0.25 s stab followed by a tail 12 dB down. It reads as sfz-piano, which the score does not print. The tune's top line drops out for the second half of each bar.
- Cause (measured from CHANGES.md and parts.json). Three things stack:
  - the A #2 stem fix put each stroke back to its c22 whole-note level + 0.5 dB, but the Marc LITE note carries its level in the front, so the body went 3-6 dB under c22;
  - `accent_bodies.json` still cuts Violins I 564 by -1.3 and 566 by -3.0 from +0.25 s;
  - 566 has no `accent_fits` entry, so it also takes the default string swell of +3 dB on top of the sample's own marcato front.
- The other test strokes are within the brief: Violins II 328 +0.6 / 2-5 kHz -0.4; Vc 284 / 285 -2.1 / +1.9; Vln II 564 +3.4 / +2.0. Violins I 328 / 330 are +4.6 / +6.2, with 2-5 kHz +4.5 / +4.7. Those two follow a rest at ff, so the jump into the stroke is expected.

**Fix.**
1. Level only, by `stem_fix.py`. Bring the body back to c22 and leave a front of about +2.5 dB.
   - Violins I 566: +5.8 dB from +0.28 s to the end, -2.3 dB over -0.03..+0.25 s.
   - Violins II 566: +3.4 dB from +0.28 s, -2.9 dB on the front.
   - Violins I 564: +1.6 dB from +0.28 s.
   - Violins II 564: +1.3 dB from +0.28 s.

   All ramps 0.05 s.
2. Build (`build/accent_fits.json` and `build/accent_bodies.json`):
   - remove the Violins I 564 and 566 body cuts;
   - set Violins I / II 566 and 564 to swell 0 (the Marc LITE sample supplies the front);
   - in `tools/score_to_parts.py`, make the Marc LITE level step match the body (+0.30 s .. end - 0.03 s), not the whole note.
3. Do not extend Marc LITE to bars 32, 72 and 131. The Sus MAX controls there already reach front-body -0.9..+2.7 dB with peaks at +0.01..+0.20 s under the c23 swell (table above), and their 2-5 kHz fronts are -5..+2 dB. Keep the row only on the strokes that passed (Vln II 328/330/564, celli 284/285). Optionally return Violins I 566 to Sus MAX at the next Violins I rebuild.

**Pass.** Bodies of 564/566 within 1 dB of c22. Front minus body +1..+4 dB. 2-5 kHz first 80 ms minus body +3 dB or less on all four. Whole-bar level of bars 141-142 within 1 dB of c22.

## 3. The a2 trumpet theme (bars 167-170) is one solo trumpet sample raised 3 dB: use the 2 Trumpets KS Master (inferred; patch facts measured)

**Where.** Trumpets 1+2 in unison, ff, slurred with accents:
- 664.5-676 (bars 167-170, the theme's last statement; B measured it as the top stem over the f accompaniment);
- also 520-524 (bar 131), 276 and 628.

**Evidence.**
- Measured from parts.json: `unison_dropped` Trumpet 2 = 21 notes. The kept Trumpet 1 note gets +10·log10(2) dB (kit LEARNINGS 8).
- A doubled melody therefore sounds as one player played louder, with none of the width and slight pitch and timing spread of two players. The horns' a2 passages had the same problem until the `2FH KS Master` track (c13; kit LEARNINGS 8).
- Measured from the patch: `2 Trumpets/06 Keyswitch/2TP KS Master.oib` has Sus MAX (key 24) and Leg Slur MAX (key 26), the two rows this line uses. `libs/ew_ho/dump_ks.py` raises KeyError 'key' on this file; read it with `opus_state.load_oib`.
- The trombones' a2 (520.5-534, 464-480, Trombone 2 dropped 29 notes) has no equivalent: the `2TB KS Master` (2 Trombones EXP) has no legato row, and the line is slurred. Leave the trombones as they are.
- Inferred: memory. The 2FH track took the settled render from 43 to 45 GB (c13). This one would add about 2 GB, to about 47 GB, over the brief's "about 45". That cost is why A5 was deferred in c01.

**Fix (test).** In `build/score_config.py`, follow the "Horns a2" pattern (lines 621-633):
- `TRACKS += [("Trumpets a2", ["Tpt1"], B + "2 Trumpets/06 Keyswitch/2TP KS Master.oib", "brass", <Tpt1 pan>)]`;
- `TRACK_WINDOWS` for Trumpets a2 / Trumpet 1 / Trumpet 2 over 664.4-679.5 (start with this window only);
- copy Trumpet 1's `LEVEL_SHAPES`, `PICKUP_LIFT` (664.5 6.9, 672.5 6.4), `ACCENT_FITS`, the 4 kHz shelf and `ABUT_LEAD` into the window;
- add the 2TP rows to `build/ks_maps_extra.json`;
- gain: start at Trumpet 1's gain + 4.6 dB (the 2FH offset), then set the gain from the render so the summed theme matches c23 within 1 dB.

Record `footprint` after the render. If it is over 46 GB, unload the Trumpet 1 Main mic's unused rows or drop the test.

**Pass.** Theme level in bars 167-170 within 1 dB of c23. GENTLE_ACCENT 2-5 kHz front-body on 665/670/673/676 at -1 dB or less (brass median -8.2). Legato joins under 5 dB. Mean stereo correlation of the trumpet stem in that span below Trumpet 1's c23 value (wider). Listen once against c23.

## 4. Violins I re-bows dip 4-6 dB, the deepest of the five sections (measured)

**Where.** Violins I re-bows at 711.855, 722.781, 724.465 (the pp coda chord) and 48.597 (bar 13).

**Evidence (measured, `rebow.py`, 80 ms minimum from -0.1 to +0.6 s against -0.5..-0.1 s).**
- Violins I median dip -4.5 dB, worst -5.7. The other sections: Vln II -2.0, Vla -2.2, Vc -2.3, Cb -1.2.
- Master at the same times: -3.2 / -2.6 / -1.6 / -4.5. 48.597 also has a -4.5 dB level step. The Violins I stem sits -6.4..-8.4 re master on the coda chord, its top voice.
- According to the `build/rebow_fills.json` doc string, the whole file was last fitted on c10. The later refits covered only basses and violas (c21) and three celli rows (c22), so the Violins I rows date from c10.

**Fix.** `tools/fit_rebows.py` on c23 for Violins I only. Write the six rows into `build/rebow_fills.json` (level only: stem fix now, build later). Keep 48.597's -4.5 step only if a printed diminuendo explains it, otherwise fit it to 0.

**Pass.** Violins I median dip -2.5 dB or shallower, worst -3.5. Master dip at the four coda re-bows -2.0 or shallower. Item 7 on the final chord no worse (Vln I acf 0.14 / 0.19).

## 5. Violins II Leg BC joins got shallower holes but later bodies: set the Leg BC extra back to 0.0 (measured; small)

**Where.** Violins II Leg BC targets 480, 637 and 648. Leg Slur 234, 296 and 626 are in the same groups.

**Evidence (measured, `joins.py`, 30 ms minimum against the bodies).**
- Joins c22 -> c23: 480 2.0 -> 4.8, 648 -5.6 (overshoot) -> 4.5, 234 4.7 -> 6.1, 296 3.4 -> 4.6, 626 3.6 -> 4.6; 637 6.6 -> 6.7.
- Total lead at 480 went 0.170 -> 0.230 s, and the old note's level falls 6 dB at -0.15..+0.10 s.
- The actor's own crossover check (CHANGES "Open for c24") found the same overshoot (cap-free Leg BC -0.033 s, 8 targets at -0.09..-0.12 s).

**Fix.** `build/score_config.py` `LEG_ART_EXTRA_S["Violins II"]["Leg BC MAX"]` +0.03 -> 0.0, as the actor proposed. Re-run `auto_fills.py` for Violins II after the render.

**Pass.** Violins II joins of 4.5 dB or more back to the c22 count. Crossover -0.01..+0.03 s.

## Do not touch

- The c23 GENTLE_ACCENT swell shapes (0.03, 0.15, 0.40) and (0.03, 0.22, 0.50). They moved the hammer controls' weight to the front. Change only the over-cap fits and the listed notes.
- `STAC_LEAD_S`; `STR_REST_SHORT` on the violas.
- The Marc LITE row on Vln II 328/330/564 and celli 284/285.
- `LEG_CAP_FRAC` 0.75 / `LEG_MIN_GAP_S` on violas and celli; the ABUT_LEAD lists and SHORT_SUS_LEAD; Clarinet leg lead 0.05.
- The c22 celli/basses/violas re-bow rows; AUTO_REBOW timing.
- Brass GENTLE_ACCENT (2-5 kHz median -8.2) and the brass 4 kHz shelves.
- PICKUP_LIFT values; the Slur Runs spans; DOWNBOW celli 484 / Vc 321 / Vln I 533.
- The timpani, tam-tam, cymbal and harp settings, and every c22 item listed in HISTORY.
