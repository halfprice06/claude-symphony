# Cycle 18, critic A: articulation and phrasing (render c17)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c17 build after its stem fix), measured on the c17 stems and master (`cycles/c17/render/`). For before/after checks I used c16 (`mvt1-c17-A/feat_c16`, parts in `cycles/c17/before/parts.json`).

Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c18-A/`.
- The c17-A battery was rerun on c17, with 5 ms feature frames in `feat_c17/`. Outputs are `o17_*.txt`; `o16_*.txt` are the c16 controls.
- New scripts:
  - `accshape.py`: the internal shape of long accents against unaccented long notes;
  - `jfill.py`: string join holes, timed from the moved onset;
  - `ten200.py`: tenuto/portato joins on a 200 ms window;
  - `multi.py`, `tr18.py`, `fine.py`: traces;
  - `relburst.py`, `relburst2.py`, `vla.py`, `vla2.py`: level after note-off on short notes;
  - `lown.py`: low brass and wind range check.

## Checks that passed (measured)

- **Legato.**
  - No chord is sent to a Leg row.
  - Wind and brass joins: no join at 6 dB or more. Medians are -0.8..3.1 dB per track.
  - String join medians: 1.4-2.4 dB per section.
- **Tenuto/portato joins** (Flute 1 393/400/405, Oboe 1 277/393/400/405, Flute 2 277, Trumpet 1 277, Horn 1 589/601).
  - On a 200 ms window (one vibrato cycle, LEARNINGS 6), the dip against the quieter neighbour is -2.9..+1.9 dB.
  - The 40 ms measure in `ten2.py` reads the flute and oboe vibrato as 6-8 dB holes. Leave these joins alone.
- **Accent fronts (item 8).** 2-5 kHz in the first 80 ms minus the body: brass median -8.1 dB, winds -5.6, strings -3.0.
  - The new worst wind value, Bassoon 1 536 at +7.6, is not a bright attack. The previous G3's brighter tail falls in the window, and the accented C3 sits 9 dB under that G3, at its printed mf.
- **Re-bows and loop pulsing (item 7).**
  - No new re-bow step. The largest steps are printed hairpins (Vln I 48.6 is inside the bar-13 decrescendo; celli 163.9 is the sf > mf).
  - No held note within 6 dB of the master pulses at the loop period with more than 3 dB of level swing.
- **Other techniques.**
  - String staccato separation: medians 11.7-14.5 dB.
  - Tremolo joins: median -0.8 dB, 1 of 33 at 4 dB or more.
  - Pizzicato reaches -3 dB of its peak at a median +0.015-0.065 s.
  - Breath marks dip 3-15 dB.
  - Ties on the timpani and basses are held.
  - Detach holes: brass -5.0, winds -5.6, slurred joins -3.3/-4.1 dB.
  - No release burst after short notes on any track except the one in #3.
- **Ranges.** Bass trombone C2-D2 and tuba F1 sound at their fundamentals on the tenor/solo patches (`lown.py`).

## 1. Accented long string notes have the same shape as unaccented ones. The accent is heard only as a louder note, not as weight at the start.

**Measured** (`accshape.py`). The test set is every string note at least 0.75 s long whose stem is within 12 dB of the master: 30 accented notes and 447 unaccented ones. For each note I compared three levels, measured from the score onset: the front (0 to 0.15 s), the middle (0.15 to 0.4 s) and the body (0.45 to 0.75 s).

| Family | Accented front-body | Unaccented front-body | Accented mid-body | Accented peak time | Front under body |
|---|---|---|---|---|---|
| Strings | -1.1 dB | -0.9 dB | 0.0 | 0.38 s | 18 of 30 |
| Brass | +1.4 dB | +0.2 dB | +4.4 | 0.23 s | |
| Winds | +0.8 dB | -1.9 dB | +2.6 | 0.30 s | |

- Brass and wind accents have a weighted start: the gentle swell does its job there.
- String accents do not. 18 of 30 start quieter than they continue, as unaccented notes do, and the median peak comes 0.38 s after the beat.

**Why** (measured from `build/accent_fits.json`):
- The fitter sets the swell to 0 when the note already stands over its neighbours. Swell medians: Violoncellos 0.0, Violas 0.4, Violins II 1.9, Violins I 2.2.
- Accents with a fitted swell of 2.5 dB or more have front-body +4.3 dB (n=5).
- Accents with a swell under 0.5 dB have -2.3 dB (n=9). 13 accents have no fit entry at all.
- Most of the affected notes are bow-change legato targets (Leg BC MAX, moved 0.11-0.17 s early) in the first theme and recapitulation. Their transition sag lands on the front.

Worst cases, front-body / mid-body in dB:

| Track | Note (bar) | Row | Front-body | Mid-body |
|---|---|---|---|---|
| Violoncellos | 321 (81) | Leg BC | -5.9 | -7.0 |
| Violins II | 100 (26) | Sus | -5.4 | -1.9 |
| Violins I | 533 (134) | Leg BC | -5.2 | -3.8 |
| Violoncellos | 91 (23) | Leg BC | -4.9 | -3.6 |
| Violins I | 330 (83) | Sus | -4.2 | 0.0 |
| Violins II | 564 (142) | Sus | -4.0 | -2.8 |
| Violoncellos | 539 (135) | Leg BC | -3.3 | -2.3 |
| Violins I | 154 (39) | Leg BC | -3.1 | -2.4 |
| Violins I | 548 (138) | Leg BC | -2.3 | -1.9 |
| Violins I | 100 (26) | Leg BC | -1.8 | -1.5 |

These also explain the open "string long-accent excess" item (+3.7 dB, 18-30 notes over 6 dB). The accent's peak lands late in the body, so the whole note is raised instead of its start.

**Inferred.** A player accents a long note with bow weight and speed at the start, then relaxes. A note that swells to its peak at 0.4-0.6 s sounds like a small hairpin. In the Allegro theme this blurs the accented bow changes that drive the line.

**Fix:** a shape objective in `tools/fit_accents.py`, string family only.
1. Add `--front-min 2.0`. For each string accent of 1 qn or longer, measure on the render:
   - front: score onset to +0.15 s;
   - body: +0.45 to +0.75 s (capped at the note's end - 0.05 s).
2. If front-body is under +2 dB, write a body cut instead of raising the swell:
   - `body_db = -(2.0 - (front-body))`, capped at -4 dB;
   - it ramps from 0 at score onset +0.25 s to full at +0.45 s;
   - it holds to the next onset's moved start - 0.02 qn.
3. Keep the swell only where the peak-over-preceding measure is under +2 dB, as now.
4. New `accent_fits.json` form: `[swell, step, body_db]`. In `score_to_parts.py`, write `body_db` as an exact level shape (parts.json key `accent_body`), not on the envelope grid.
5. Exempt:
   - notes inside a printed crescendo or arriving at one (the c10 rule);
   - sf/fp notes;
   - the hand values Violins I 62/65/82 and Trombone 1 521/529 (`--skip`).
6. On the c17 render this touches about 22 of the 30 notes, with cuts of 1.5-4 dB. It lowers the late peaks, so the "excess" measure should fall as well.

Optional test, one section only (Violins II 100/564/566 and Violins I 330/564/566: Sus MAX accents):
- the `Marc Sus LITE` row, which every Hollywood Strings section has (`01 Long/<section> Marc Sus LITE.oib`; the 2nd Violins KS Master loads it by default). It has a recorded marcato start on a sustain, and this loop has never tried it.
- Accept it only if 2-5 kHz front minus body stays at +2 dB or less (item 8) and front-body reaches +2..+4 dB with no envelope shape.
- It is a row load (a full rebuild of that track). Do not combine it with the body cut on the same notes.

**Pass** (`accshape.py`):
- String accents: front-body median at least +2.0 dB, and at most 6 of 30 under 0.
- Unaccented long string notes unchanged (front-body -0.9 ±0.5).
- Strings 2-5 kHz front-body median at most -2.5 dB (`acchf.py`).
- Peak minus preceding notes (`accpk2.py`), strings: median at most +4.7 dB (now +4.7), over 6 dB fewer than 30.

## 2. Two legato holes in the Violins I top line, and the bar-70 melody sinking on beat 4

**Measured** (`jfill.py`, `multi.py`, `tr18.py`; levels in 50 ms windows).

Violins I is not in `build/auto_fills.json` `tracks`, so its joins never get fills. Its two worst joins sit on the top line:

| Note (bar) | Row | Hole, re the quieter body | Span, from the moved onset | Stem re master |
|---|---|---|---|---|
| 279 (70, F6 -> E-flat6, slurred) | Leg Slur | 5.4 dB; 9.8 dB on `joins.py` | +0.27..+0.47 s | -11.4 dB |
| 720 (181, C-sharp5 -> C5, final ppp) | Leg BC | 8.1 dB | +0.21..+0.50 s | -8.1 dB (Vln I is the top voice) |
| 626 (157, poco animando) | Leg Slur | 6.1 dB | +0.01..+0.41 s | -6.4 dB |

All three are the same in c16 (9.4 / 8.6 dB), so they repeat from render to render.

Bar 70 is more than one hole: the doubled melody falls apart on beat 4 (qn 279). Score page 7: Violins I, Flute 1-2, Oboe 1 and Trumpet 1 play the tenuto half on beat 2 slurred into the beat-4 quarter. All at f, with no hairpin.
- **Violins I.** The E-flat6 settles 6 dB under the F6 (-37.9 against -31.9 dB). The volume envelope adds +1.5 dB on the half and -2.5 dB on the quarter (279.0-279.643 in `vol_db`). The legato hole comes on top of that.
- **Trumpet 1.** The 277 -> 279 join plays a transition spike 9 dB over the F5's body (-26.3 against a -35.5 median, peak 0.15 s before the score onset). The E-flat5 then settles 4 dB under the F5 (-39.7).
- **Master.** It peaks at -19.5 dB 0.1 s before beat 4, then sits at -23.1..-24.6 for the first 0.25 s of beat 4: a 3.5-5 dB fall where the score has one f line.
- The same figure in the coda (bar 168, qn 671) has no such fall: the master stays within 2.2 dB.

**Fix** (all measured on c17; refit after the render):
- `build/early_fills.json`, Violins I (hand entries, listed in auto_fills `--exclude` so the pass leaves them alone):
  - `"279": {"db": 4.5, "pre_s": 0.0, "hold_s": 0.47}`
  - `"720": {"db": 5.0, "pre_s": 0.0, "hold_s": 0.50}`
  - `"626": {"db": 4.0, "pre_s": 0.0, "hold_s": 0.41}`
  - Times are from the moved onset. Check each fill against the 30 ms peak (LEARNINGS 6: no fill on a transition spike).
- `build/score_config.py` `JOIN_NOTCH`: add `"Trumpet 1": [(278.45, 278.92, -6.0)]`, over the spike (score qn; it covers the positions seen in c16 and c17).
- Find what writes Violins I -2.5 dB on 279.0-279.643 (it is not in `note_trims.json`). Reduce it to -1. The E-flat6 is a passing step inside a slur at one dynamic.
- After this render, add Violins I to `auto_fills.json` `tracks` so later passes cover its other 5 dB joins (480 at 3.5 dB, 626).

**Pass:**
- The three Violins I holes at 4 dB or less, with no 30 ms peak over the following body by more than 2 dB.
- Trumpet 1: peak 0.3 s before 279 at most +3 dB over the F5 body.
- Master over beat 4 of bar 70 (279.0-279.5) within 2 dB of the half note's last 0.25 s.

## 3. Recapitulation violas, bars 132-134: every second off-beat dyad thumps after its note-off

**Measured** (`vla.py`, `vla2.py`, `relburst2.py`).

In bars 131-134 the violas play off-beat eighth dyads (D4/F4, then E-flat4/G4). The notes are identical in MIDI: v91, Sus MAX, 0.626 qn moved 0.126 qn early, no keyswitch, a regular -0.5/-2 dB envelope sawtooth. Yet:
- the dyads at 526.5, 528.5, 530.5, 532.5 and 534.5 rise to a burst 0.03-0.09 s after their note-off. In 30 ms frames:
  - burst -24.8..-25.0 dB;
  - body peaks -28..-30.
- The dyads in between have no burst.
- c16 is identical to within 0.2 dB, so the burst is deterministic.
- The burst's energy is at the F4 (325-375 Hz bins).
- This is the only place in the movement where a short note's level after its note-off exceeds its own body by more than 3 dB. Other notes: string Sus MAX median +0.6 dB; brass and winds -1.2..-1.5.

**Inferred.** This is the release sample of one of the patch's alternating release recordings, louder than a 0.3 s note that never reached full level.
- Every second viola off-beat now ends with a thump on the following beat, at -10 dB re master in an f tutti.
- It is the "rise 7-9 dB, peak at +0.24 s" that the c17-A report measured on these notes. The c17 actor kept them outside `SYNCO_SHAPE` because they are 0.5 qn.

**Fix:**
- `build/score_config.py` `LEVEL_SHAPES` for Violas: a notch of -5 dB, from each burst note's moved note-off - 0.01 qn to +0.20 qn, ramps 0.02 qn. Apply it at sq 526.5, 528.5, 530.5, 532.5 and 534.5 only (note-offs at qn 527.0, 529.0, 531.0, 533.0, 535.0).
- Do not change the note lengths. Shortening them moves which release plays (inferred).
- If a generic rule is wanted later, add `REL_NOTCH` to `score_to_parts.py`, keyed by a measured list like `loop_fills.json`, rather than a blanket rule: no other note shows the effect.

**Pass** (`vla.py`): every dyad's post-off 30 ms peak at most +1 dB over its own body peak; the dyads in between unchanged within 0.5 dB.

## Patches

Patch findings this cycle:
- The only new patch recommendation is the `Marc Sus LITE` test in #1.
- The deferred second-staff Horns 3-4 a2 routing (bars 80-81) is still open; I did not re-measure it.
- I checked these and they do not need a different patch:
  - The Vln II "metà" pedal (bars 47-54, qn 184-216): pp whole notes 13-20 dB under the master, so a DIV A track would not be heard.
  - The "div. sul tasto" tremolo (bars 147-155): no sul tasto tremolo patch exists in Hollywood Strings, and the c03 EQ stands.
  - Tuba and contrabassoon have no slurs, so their Sus MAX-only rows are complete.
  - Bass trombone low C2-D2 on the Solo Trombone KS Master sounds.

Do not touch:
- brass and wind `GENTLE_ACCENT` swells (accented front-body +1.4/+0.8 dB, 2-5 kHz fronts -8.1/-5.6 dB);
- the portato/tenuto joins (`PORTATO_JOIN_AT`, `PORTATO_JOIN_NOTCH`; no hole on 200 ms);
- `SYNCO_SHAPE`;
- `PICKUP_LIFT`;
- `_REBOW_FROZEN`/`REBOW_AT` with `rebow_fills.json`;
- `MEAS_TREM` alt_row;
- `TREM_JOIN`/`TREM_SPLIT`;
- `WIND_DETACH` with the brass dip;
- `SLUR_START_SUS` and `RETONGUE_LEAD_S`;
- the staccato, pizzicato and tremolo rows;
- harp `env_release_ms` 200 with `HARP_RING_S` and the étouffez note-offs;
- `PORT_TARGETS`;
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`;
- the tam-tam / suspended-cymbal keys and timing;
- the Horns a2 windows, roles and shelves;
- the climax order (160 > 122 > 169).
