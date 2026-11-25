# Cycle 20, critic A: articulation and phrasing (render c19)

Scope: every wind, brass, string, harp, timpani and percussion note in `cycles/c19/rendered_build/parts.json`, measured on the c19 stems and master after the stem fix (`cycles/c19/render/`), with c18 as the before/after control (`cycles/c18/render/`, `cycles/c18/rendered_build/parts.json`).

Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c20-A/`.
- The c19-A battery was rerun on c19. Outputs are `o19_*.txt`; 5 ms feature frames are in `feat_c19/` (c18 in `feat_c18/`).
- New scripts:
  - `heads.py`, `heads2.py`: pitch dominance (harmonics 1-4 of each pitch) for the SLUR_HEAD_LEAD heads;
  - `runscan.py`, `runs.py`, `runs2.py`, `run606.py`: own-pitch dominance per note in every fast figure (3 or more consecutive single notes under 0.3 s), with stem level re master;
  - `acctr.py`, `rtl.py`: accent and re-tongue profiles c18 against c19;
  - `accfill.py`: a simulated front fill on the c18 Leg BC accents;
  - `tasto.py`, `bntr.py`, `tr284.py`, `lv.py`: spectra, traces and levels.

## Checks that passed (measured)

- **Legato.** No chord is sent to a Leg row (`chordleg2`: 0). Wind and brass joins: none at 6 dB or more. String joins at 6 dB or more fell from 12 to 5 (Violins II 637, Violas 612, celli 112/215/689.5). The c19 join fills held: Vc 365 hole 8.6 -> 1.1 dB, Vc 369 8.7 -> 2.7, Violas 72 8.2 -> 3.2, Violas 180 8.7 -> 4.0, Violas 517 5.7 -> 3.2, Violins II 236/296/405 6.3-6.5 -> 3.1-4.4 (`jfill`).
- **Accents (item 8).**
  - 2-5 kHz in the first 80 ms minus the body: brass median -8.2 dB, winds -5.8, strings -3.3, all unchanged from c18.
  - New over +3 dB: Trumpet 1 284 (+6.0). It sits 15 dB under the master, its front is within 1 dB of c18 (+8.8 -> +9.9 on the stem), and the master's 2-5 kHz band does not move at the onset (`tr284`). Leave it.
  - ACC_ART_LEAD worked on the brass: accent front-body median +1.9 -> +3.2 dB, front under body 38% -> 9% (`accshape`).
- **Re-bows and loop pulsing (item 7).** No new re-bow step; the largest are the printed sf > mf (celli 163.9) and the morendo (723.9). No held note within 6 dB of the master pulses at the loop period. Bassoon 2 at 684 and 48 read 6.0/6.6 dB of swing, but the traces show a repeated note (688) and a printed diminuendo with a re-take at 51.4, not a loop (`bntr`).
- **String re-tongue leads (c19 C #2).** Holes before the led notes deepened: Violins I 286 4.7 -> 8.9 dB, celli 125 4.4 -> 7.8, master at 286 1.3 -> 4.1 (`rtl`). Every one of these notes is a printed accented down-bow after another down-bow, so the bow is retaken and a gap is idiomatic (inferred). Leave them.
- **Other techniques.** String staccato separation medians 8.8-14.6 dB. Tremolo joins: median under 1 dB. Pizzicato on time. Detach holes: brass -5.1 dB, winds -5.8 dB. Breath marks dip 3-12 dB. Ties held. The harp traces are unchanged.

## 1. Violins I slurred sixteenth runs (bars 32, 40, 68) are smeared: each pitch arrives 0.08-0.17 s late and most never lead

**Measured** (`runscan.py`, `runs2.py`). Own-pitch dominance = the share of the note's own slot, from 20 ms after its onset to 20 ms after the next onset, in which its pitch (harmonics 1-4) is the strongest of the figure's pitches. "First" = when it first leads, from its score onset.

| Passage | Stem re master | Row | Dominance per note | First |
|---|---|---|---|---|
| Bar 32, qn 127.25-127.75, cresc. to ff | -3.6 (loudest stem) | Sus MAX | 0.52, 0.24, 0.48 | +0.084, +0.119, +0.089 s (notes 0.119 s long) |
| Bar 68, qn 270.25-271.75, p cresc. to f | -6.0 (loudest stem) | Sus MAX | 0.38, 0.15, 0.18, 0.09, 0.68, 0.49, 0.86 | +0.125, +0.168, +0.160, +0.170, +0.079, +0.111, +0.047 |
| Bar 40, qn 158-159.75, into sf | -14.2 | Sus MAX | 0.24, 0.08, 0.00, 0.16, 0.00, 1.00, 0.16, 0.80 | to +0.32 |

- The same sixteenths of bar 40 on Flute 1 and Oboe 1 (Leg Slur MAX) lead for 0.33-1.00 of their slots, median 0.88/0.92.
- Violins II in bar 32, which has SHORT_SUS_LEAD (0.06 s, keep-overlap 0.03), reads 0.16, 0.96, 1.00. The c05/c07 tests measured that lead gaining only 0.015-0.04 s, which is too little for 0.12-0.2 s notes.
- In bar 68 the target f at 272 (Leg BC) also leads only from +0.142 s.

**Inferred.** In bars 32 and 68 the violins carry the line and are the loudest stem, so a listener hears a blurred slide that reaches the top a sixteenth late, not a scale. LEARNINGS section 5 lists the Hollywood Strings "Slur Runs" row as the one articulation for fast slurred notes that has not been tried. The 1st Violins KS Master has it as row "Slur Runs", key 42 (`mockup-kit/opus/ks_maps.json`). It is a legato-type row recorded for runs (manual, Playable Runs).

**Fix (test, one track):**
- `build/score_config.py`: use the STACLEG_SPANS mechanism with a per-span row:
  - `STACLEG_SPANS = {"Violins I": [(127.0, 128.0), (158.0, 160.0), (270.0, 272.0)]}`, with art "Slur Runs" for these spans. `STACLEG_ART` is global, so give the span its own art, as ART_SPANS does.
  - The flags stay as they are: `fast_leg` (FAST_LEG_OVERLAP 0.02 qn, no lead, no merge). Each note keeps its current velocity and CC11.
  - The targets 128, 160 and 272 stay on their current rows. The span ends before them.
- A row load means a full Violins I rebuild. Record the REAPER memory; the c14 Leg Port rows cost 0.1 GB each.
- Violins II bar 32 stays on Sus MAX as the control.

**Pass:**
- In bars 32 and 68, own-pitch dominance median 0.6 or more, and first dominance +0.06 s or earlier.
- Bar RMS of the stem within 1.5 dB of c19.
- 2-5 kHz first 80 ms minus body at most +2 dB on the target notes.

If it fails, revert. These figures then stay on Sus MAX, and the LEARNINGS line about Slur Runs should record the result.

## 2. Bar 152 (recapitulation second theme, qn 606.5-607): the violas' and celli's 32nd-note run blurs, and the F it leads to (the top of the crescendo) arrives 0.17-0.29 s late

**Measured** (`run606.py`). The violas and celli carry the theme here and are the two loudest stems: -6.6 / -5.3 dB re master over 606-609.
- What is played: B-C-D-E at 0.125 qn (0.067 s each) on Sus MAX v72 at the score onset. The A before it (Leg Slur MAX) ends at 606.43. The F (607, tied, cresc.) is Leg Slur MAX joined from the Sus E, led only 0.056 qn (0.03 s): the 0.45 LEG cap of the E's 0.125 qn binds.

| Note | Violas: first leads / share | Celli: first leads / share |
|---|---|---|
| B 606.5 | +0.03 s briefly, 0.46 | never, 0.00 |
| C 606.625 | never, 0.00 | never, 0.00 |
| D 606.75 | +0.19 s, 0.46 | never, 0.00 |
| E 606.875 | +0.24 s, 0.69 | +0.23 s, 0.85 |
| F 607 (score +0.264 s) | +0.44 s, so 0.17 s late | +0.56 s, so 0.29 s late |

- The A keeps the lead until 0.13 s after the run's first note in both sections.
- In the celli the E holds for 0.33 s, past F's score time, because of the slow Sus -> Leg join. LEARNINGS section 6: with no lead that join reaches body - 6 dB only at +0.33 s; with a 0.12 s lead at v100, at +0.10 s.

**Inferred.** The flourish should land on the F with the crescendo. A listener hears the A held, a smear, and a late F under the horns' line.

**Fix:**
- `tools/score_to_parts.py` + `build/score_config.py`: a new per-span group lead, `GROUP_LEAD_AT = {"Violas": [(606.5, 607.0, 0.12)], "Violoncellos": [(606.5, 607.0, 0.12)]}`.
  - Every note with a score onset in [606.5, 607.0] (the four run notes and the F) moves 0.12 s earlier together.
  - The note before (606.0) ends at the first moved onset + 0.03 qn.
  - CC11 and volume stay on score time.
  - The cap is 0.45 × the A's 0.5 qn = 0.225 qn = 0.12 s at 112 bpm, so it fits.
- Keep the run on Sus MAX. The violas and celli KS Masters have no Slur Runs row, and LEARNINGS section 5 measured legato rows holding one pitch on notes of 0.16 s.
- Set the F's velocity to max(vel, SOST_VEL) as in the sostenuto join.

**Pass:**
- F first leads at +0.08 s or earlier (violas) and +0.15 s or earlier (celli).
- At least two of the four run pitches lead for some time in each section.
- No new hole of 5 dB or more on the stems over 606-608.

## 3. The DOWNBOW revert (c19 A #1): keep the two that worked, do not replace the other seven with front fills, refit one pickup

**Measured** (`accshape`, front = score onset..+0.15 s, mid = +0.15..+0.40, body = +0.45..+0.75; c18 -> c19):
- Keep celli 321: front-body -5.9 -> -0.5 dB, mid-body -7.0 -> +1.9.
- Keep Violins I 533: front-body -2.2 -> -0.2 dB, mid-body -1.4 -> +3.0.
- The other seven got worse as the c19 CHANGES table shows: Vc 91 -7.6, Vc 539 -5.3, Vc 317 -4.3, Vln I 154 -4.1, Vln I 100 -2.2 dB. Revert them as planned.
- I simulated the obvious level-only alternative on the c18 stems (`accfill.py`): a volume lift from the moved onset (30 ms rise, held to +0.40 s, gone by +0.65 s) on the seven Leg BC accents. Reaching front-body +2 dB needs 3.5-8 dB (Vc 91: no value up to 8 dB reaches it). It puts 30 ms peaks 4-8 dB over the body: Vc 317 +8.3, Vc 539 +6.2, Vln I 548 +5.1. That is the hard front Dan rejected (item 8). Do not add front fills to these notes.
- One side effect to repair: celli pickup 320.5, into the kept Sus stroke at 321, now sits 6.4 dB under its target (pkr3; c18 was not in the list at -5). It is outside the PICKUP_LIFT pass range (-6..-2).

**Fix:**
- `build/score_config.py` `DOWNBOW_STROKE_AT`: remove celli 91/317/539 and Violins I 100/142/154/548. Keep celli 321 and Violins I 533, and the c06/c11 strokes.
- Restore their accent_fits rows by refitting: `fit_accents.py --family string` with the usual `--skip` list, then `fit_accent_bodies.py`. Do not hand-copy the c18 rows, because the c19 leads changed the neighbours.
- PICKUP_LIFT: refit Violoncellos 320.5 to the -6..-2 band (about +2.5 dB more, measured from the c19 shape).
- These seven accents stay at -2..-5 dB front-body after the revert. That is a known limit of Leg BC targets. No tested row or level shape improves them without a bright front.

**Pass:** the seven notes back within 1 dB of their c18 front-body. Celli 321 and Violins I 533 within 1 dB of c19. Celli 320.5 pickup minus target in -6..-2 dB.

## 4. SLUR_HEAD_LEAD: the heads now start early by a median 0.06 s; a 0.10 s lead puts them on the beat

**Measured** (`heads2.py`, 21 Violins I heads; head pitch harmonics 1-4 leading over the previous and target pitches):

| | c18 | c19 |
|---|---|---|
| Head starts leading, from its score onset (median) | +0.088 s | -0.062 s (range -0.147..+0.083) |
| Head stops leading (target takeover), median | +0.303 s | +0.303 s |
| Dominant length (written 0.238 s) | 0.215 s | 0.370 s |

- The target takeover did not move. It sits 0.065 s after the target's score onset.
- The extra 0.15 s of the head therefore comes entirely before its beat. Seven heads start 0.10-0.15 s early (69, 74.5, 84, 106.5, 152, 554.5, 570.5), which anticipates the upbeat.

**Fix:** add the planned `SLUR_HEAD_LEAD["lead_s"] = 0.10` (string), in place of the target's lead (0.17 s). The note before still ends at the head's moved onset.

Expected: head start about +0.01 s, dominant length about 0.30 s. Do not change the targets' leads; the takeover at +0.065 s matches the rest of the section.

**Pass:** head start median -0.02..+0.04 s, none earlier than -0.06 s. Target takeover unchanged within 0.02 s.

## Patches

- One new test: the 1st Violins "Slur Runs" row for the slurred sixteenth runs (#1).
- No other patch change is indicated.
  - Violas and celli have no Slur Runs row. Their run needs timing (#2).
  - The sul tasto tremolo of bars 147-155 (Violins II, `loud_eq` 2.5 kHz -7 / 1.2 kHz -2 already applied) measured no brighter than the other Violins II tremolos: 2-5 kHz re 200-1000 Hz -7.1 against -6.7..-7.9 dB. Hollywood Strings has no sul tasto tremolo row, so leave it.
- Memory is at the cap (45 GiB), so I am not proposing divisi tremolo tracks or other new instances.

Do not touch:
- ACC_ART_LEAD and the brass/wind accent refit (brass front-body +3.2 dB, 2-5 kHz fronts -8.2/-5.8 dB);
- GENTLE_ACCENT swells;
- the c19 converted join fills (Vc 365/369, Violas 72/180/517, Violins II 236/296/405, Horns a2 311/312.5);
- the string RETONGUE_LEAD_S on the accented down-bow re-takes;
- DOWNBOW strokes celli 321 and Violins I 533;
- accent_bodies.json apart from the refit;
- the c18 Violins I fills and Trumpet 1 279 notch;
- violas release notches;
- PORTATO joins, SYNCO_SHAPE, PICKUP_LIFT (apart from celli 320.5);
- _REBOW_FROZEN/REBOW_AT with rebow_fills.json;
- MEAS_TREM alt_row; WIND_DETACH with the brass dip;
- SLUR_START_SUS; the staccato, pizzicato and tremolo rows;
- harp HARP_RING_S/étouffez; PORT_TARGETS; TIMP_CC1_MAP with TIMP_ROLL_TRIM_DB;
- the percussion keys and timing; the Horns a2 windows, roles and shelves;
- the climax order (160 > 122 > 169).
