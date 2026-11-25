# Cycle 38, critic A: articulation and phrasing (on the c37 render)

Inputs: `cycles/c37/render/` (stems after the Flute 1 stem fix, and the master), `cycles/c37/render_first/` (Flute 1 before the fix), the c36 render for comparison, `cycles/c37/CHANGES.md`, `build/parts.json`, `build/score_config.py`, `build/mockup-events.tsv`, the installed `.oib` files in `Flute/01 Long` and `Flute/04 Legato`, `~/.rpr-bridge/libs/ew_ho/ks_maps.json`, `guides/eastwest-hollywood-orchestra/DIGEST.md`, `loop/MANUAL-GAPS.md`, and the May 2021 HO manual, PDF pp.100 and 103-107 (row A5, cycle 38). Levels are plain RMS in dB on the stem (or the master where stated). The window length is given with each figure. Times are score qn on the parts.json tempo map. In bars 41-44 one qn is about 1.0 s.

## Manual notes (A5, PDF pp.100, 103-107: Hollywood Brass)

| Manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Solo French Horn, Solo Trombone, Solo Tuba, 2 French Horns, 2 Trombones, 2 Trombones + Bass Trombone (p.100) | Horns 1-4 (1FH), Horns 1-2 a2 (2FH), Trombones 1-2 and bass trombone (1TB), tuba (1TU) | Yes. The bass trombone still plays the tenor Solo Trombone (MANUAL-GAPS #12, one note at 218). Horn 4 is silent in bars 61-62 because its notes double Horn 3 (unison dropped). That is correct for the patch, since Horn 3's sample is the same player. |
| Repetitions (3 tempos, release trails, CC1 loudness), Triple Performance, Double Tongue (p.103) | none: no fast brass repeats in v600 | Not applicable. |
| Sforzando Crescendo, only on Solo Horn and Solo Tuba: velocity sets the attack and the crescendo (p.103) | no printed brass sfz < | Not applicable. The bass trombone's sf at 212 (decrescendo to p at 216) is played on Sus MAX with CC1 93 -> 43 and a +8 dB envelope front. Measured: rise to -25.2 dB, then a smooth 16 dB fall over two beats. This follows the score. |
| Recorded crescendos (Fast/Medium/Slow; MOD SPEED picks the speed by CC1 1-42/43-85/86-127), rips, flutter, clusters (p.104-105) | the brass crescendos into bars 61 and 79 span several notes | Not used, which is correct: the recorded crescendos are one-note gestures. |
| Legato joins only with no gap and within an octave; trombone slide legato; legato is monophonic, CC22 0-63 makes it polyphonic (p.105) | Horn 1's solos, the horn and a2 legato rows, Trombone 1's quotation | Yes (measured, parts.json). 66 brass legato joins, none wider than 12 semitones, no chord on any Leg row, CC22 not sent. |
| Legato Slur: volume on CC1, a low-pass opens toward overblow near CC1 127; velocity sets the transition speed (p.106) | every brass Leg row | CC1 tops out at 108 (Horns 1-2, a2, Trombone 1), so the overblow range is never reached. That suits Dan's "weight, not bite". Horn 1's solo legato targets play v124 (the fastest transition). Measured crossovers on the bars 7-8 joins are +0.04/+0.05 s, so the transitions arrive on time. A slower velocity is a possible colour test, not a defect. |
| Legato Slur Accent: accent strength by velocity (p.106) | Trombone 1 213 | Not used, correctly (Dan's item 9). 213 measures 2-5 kHz first 80 ms at -10.4 dB against the body, and the master 2-5 kHz jump at 213 is -3.6 dB. |
| Legato Slur Repetitions: re-tongued samples for same-pitch notes played without space (p.106) | Horn 2's D flat 4 repeat at 208 (tenuto, bar 62) | Not used. The repeat is barely re-articulated (finding 3). The 1FH map has no "Leg Slur Rep" row (`ks_maps.json`), so the fix is a re-tongue gap. |
| Slur Runs (p.106) | none | Not applicable. |
| Mutes folder; the stop is the hand mute (p.106-107) | Horn 3 con sord. from 286 | The Solo French Horn has only stopped-horn patches, so the `mute_eq` emulation stays. CC15 is placed in rests (unchanged since c32). |
| Keyswitch Masters (p.107) | every KS track | Yes. Every keyswitch precedes its note. Flute 1's LegRep switch is at 135.94, at the end of the 135 note, and the switch back is at 139.5, after the 136 note ends (139.0). |
| Woodwind Legato Repetitions RRx4 plays a non-vibrato sustain under the re-tongued attack (2021 p.109-110; DIGEST) | Flute 1 136 (c37) | Read in the patch: `FL LegRep RRx4.oib` holds the groups "[[[LegRep RRx1-4]]]" and "[[[Sus Non Vib]]]". Measured: the render follows it, and that is the problem in finding 1. |

## Findings, ranked by what a listener would hear

### 1. Flute 1, bar 44 (qn 136): the repeat now re-articulates, but its sustain is a straight, darker tone after the vibrato notes around it. Move the slur to Leg Slur Rep (extra check; measured, fix inferred)

**Where.** Flute 1, E flat 5 (MIDI 75) at 135 slurred to the dotted half at 136 (pp, the end of the slur 126-136), in the duet with the cor anglais.

**Does it sound like a slurred re-articulation? (measured)**
- **No gap.** The 135 note ends 0.06 qn before 136. The 50 ms minimum at 135.95 is -53.5 dB, which is no deeper than the flute's own vibrato troughs in the 135 note (-55.3 at 135.25, -55.6 at 135.50).
- **Re-attack.** The separation comes from the attack. The re-attack peaks at -43.8 dB at 136.15, which is 5-7 dB over the 135 note (-48..-52) and 4.5 dB over the 136 body. In the master it adds +1.5..+2 dB over c36 at 136.05-136.20 (50 ms, 1-3 kHz band +1.5..+2.7 dB). S1 passes.
- **Attack then sag.** After the attack the level falls to -51.1 dB at 136.35, 3 dB under the body and 7 dB under the attack, for about 0.15 s. It then rises into the body (-47..-49 after the stem fix). The same shape is in `render_first`, so it comes from the sample, not from the c37 level shape.
- **Judgement (inferred).** The profile is attack, sag, swell. That reads closer to a freshly tongued note than to a soft "du" re-tongue inside one breath.

**Does its tone match the legato notes? (measured)**
- **Vibrato.** The 4-6 Hz amplitude modulation of the 20 ms envelope (5-95 percentile, detrended) is:
  - 7.6 dB on the 134 F5 and 7.9 dB on the 135 E flat 5 (both Leg Slur MAX)
  - 8.4/6.7 dB on c36's merged 136
  - 2.0 dB at 136.6-137.4 and 1.1 dB at 137.5-138.9 on c37's LegRep note

  The row's sustain is the Non Vib group (patch read, above). CC1 ramps 65 -> 100 over 136-137.2, but that ramp cannot add vibrato on this row.
- **Colour.** The spectral centroid (200 Hz-12 kHz) is 728 Hz over 136.6-137.4 and 980 Hz later, against 1103 Hz in the 135 note. The second harmonic sits about 10 dB under the fundamental in the first second, against +4 dB in the 135 note.
- **Judgement (inferred).** For three seconds at the end of the phrase the flute changes from a singing vibrato tone to a flat, darker one, exactly where the cor anglais holds its note. A player re-tonguing inside a slur keeps the vibrato.

**Fix.**
1. In `build/score_config.py` (c37 block), replace the LegRep span with the scripted legato-repetition row over the whole slur: `ART_SPANS["Flute 1"] = [{"from": 125.85, "to": 139.5, "art": "Leg Slur Rep"}]`. The FL KS Master's key is 36. Flute 1's previous note ends at 123.75, so the row change falls in a rest, and the next note after 139.0 is far off.
   - Why this row (read): the standalone `FL Leg Slur Rep.oib` contains the same "1Fl pp/mf/f" sustain groups and TLeg transition groups as `FL Leg Slur MAX.oib`, plus one "[[[LegRep RRx1]]]" group. The slurred notes 126-135 should therefore sound and time as they do now, and only the repeat takes the re-tongue attack (inferred).
   - Manual p.112 (woodwinds), like p.106 (brass): the repeat must be played "without space".
2. Keep `WIND_SLUR_REP_MERGE_SKIP = {"Flute 1": [136.0]}`.
3. Add a generic option to `tools/score_to_parts.py` with an empty default, for example `SLUR_REP_ABUT_AT = {}` ({track: [score onsets]}). For each listed onset, end the previous same-pitch note 0.01 qn before the onset instead of the 0.06 qn same-pitch gap. Never let the notes overlap: LEARNINGS §5 measured -18..-33 dB holes when they do. Set `SLUR_REP_ABUT_AT = {"Flute 1": [136.0]}`.
4. In `cc1_fn0`, give a listed repeat `dip = 0`, as for a legato target in the same slur. 136 is not a leg target now, so it gets the 35 CC delayed-vibrato dip (CC1 65 at 136.0). A re-tongued note inside a slur should keep CC1 at 100 from the front.
5. Remove the c37 post-render `LEVEL_SHAPES["Flute 1"]` shape over 136.4-139.7 (-3..-9 dB). It was fitted to the LegRep body, which played 8-11 dB louder than Leg Slur MAX. Refit by stem fix after the render if needed. Keep the c37 B #4 shape (133.8-139.5, +5).

Flute 1 needs a full rebuild: the row set changes (LegRep unloaded, Leg Slur Rep loaded).

**Target.**
- 4-6 dB AM vibrato at 136.6-138.9, as on 134/135.
- A re-articulation 2-4 dB over the 135 note's level with no sag under the body.
- A master rise of 1-2 dB at 136.05-136.2.
- Body about -48 dB (3-5 dB under the cor anglais).

**Fallback** if Leg Slur Rep plays the repeat as a slow first-note attack, or leaves a hole: keep LegRep RRx4 and accept the straight tone. Then fill only the post-attack sag: add a volume-envelope lift of +3 dB over 136.25-136.45 with 0.04 qn ramps, added to the existing Flute 1 level shape. CC7 cannot lift above 127.

### 2. Violas, bar 28-29 (qn 84): the join from F4 into the E flat 4 dotted half leaves an 8-10 dB hole for about 0.45 s on the stem, the same in c35, c36 and c37 (measured; master small)

**Where.** Violas (main track, lower line of the div. pair), 83 F4 (mf decrescendo, Leg Slur MAX, with the c37 CC7 -6 dB) into 84 E flat 4 (Leg BC MAX, v124, 3 qn).

**Evidence (measured).**
- 50 ms windows show:
  - 83's last beat at -38.3..-43.6 (c37)
  - the join at 83.96-84.40 at -49.8..-54.1
  - 84's body from 84.44 at -42..-45
- c35 and c36 have the same hole at the same place, to within 1-2 dB (c36: -45.3..-52.5 after a -32..-37 end of 83).
- In c37 the 83 note is 6 dB softer (the B #4 CC7), so the hole is now 7-10 dB under both neighbours instead of 10-14 dB under 83.
- The master dips 1-2 dB (100 ms: -36.1 at 83.87, -39.5/-39.2 at 83.96-84.05, -38.5 at 84.22), because the violins and celli carry the line.
- This is LEARNINGS §5's Leg BC sag at pp-p, a property of this join, not of the section.

**Fix.** Either of these:
- `build/early_fills.json` "Violas" "84": {db 5.0, pre 0.0, hold 0.42 s, release 0.25 s}, held to the measured end of the hole. Check the 30 ms peak against the body for overshoot (§6).
- Or move this one join to Leg Slur MAX through the per-join list `BC_SOFT_SKIP` (§5: a per-join choice) and re-measure.

Keep the c37 CC7 lane on 83. **Target:** no 200 ms window under the lower of the two bodies by more than 4 dB at 83.9-84.5.

### 3. Horn 2, bar 62 (qn 208): the repeated D flat 4 (tenuto, molto sostenuto) is not re-articulated (measured; S1, masked in the tutti)

**Where.** Horn 2, D flat 4 at 204 (4 qn, tenuto) and again at 208 (2 qn, tenuto). The first note ends at 207.97, a 0.03 qn gap.

**Evidence (measured, 50 ms).** Across the repeat the stem drifts -26.6 -> -27.4 -> -28.2 -> -28.9 (207.93-208.15). There is no new peak: the highest window after the onset (-27.4) is under the note before (-26.1 over 207.4-207.8). The new note's soft-attack sag follows 0.5 s later (-32.4 at 208.48). The other brass tenutos at 208/210 re-articulate 3-6 dB on the stem: Horn 1 210 6.3, Horn 3 210 6.4, Horn 2 210 4.0, Trombone 2 210 4.1. The bass trombone and tuba dip 13 dB at 208 at the printed breath. The master dip at 208 is 1-2 dB.

**Fix.** Re-tongue it like the other wind and brass repeats. In `build/score_config.py`, `REP_RETONGUE_AT["Horn 2"] = [208.0]` (or the generic `WIND_REP_RETONGUE` path if it accepts brass), with the c34 Horn 3 values: a 0.12 s gap and the CC fall. Horn 2 is on the CC1-layered 1FH map, so put the fall in CC1 and CC11 both, or in CC7 (pre-hall, S3), not in the volume envelope.

**Target.** A 3-5 dB dip on the stem in the 0.1 s before 208, with a re-attack back to body level by +0.15 s.

### 4. Trombone 1, bar 64 (qn 218): the second accent has little weight over its neighbours (measured; small)

**Evidence.** Level over the first 0.4 s from the beat:

| Note | qn | Level (dB) | Accent over it |
|---|---|---|---|
| 217 | 217.0 | -26.3 | +2.5 |
| 217.5 | 217.5 | -25.0 | +1.2 |
| 218 (accented) | 218.0 | -23.8 | n/a |

The first accent at 213 stands +5.4 dB over the 212.5 pickup and +2.4 over 214.5. The attack is clean on both: 2-5 kHz over the first 80 ms is -10.4 dB (213) and -16.4 dB (218) under the body, and the master 2-5 kHz jumps are -3.6 and -1.0 dB. The decrescendo from 218 to p at 219.5 is printed, so the accent should be heard as the top of that fall.

**Fix.** Add `LEVEL_SHAPES["Trombone 1"]` [(217.95, 0), (218.05, 1.5), (218.5, 1.5), (218.9, 0)] in the envelope. That is +1.5 dB weight, with no CC1 or velocity change, so the layer and the 2-5 kHz content stay. **Target:** 218 at +2.5..+3 dB over 217.5, with attack minus body still under -8 dB.

### 5. Violas' sotto voce portato, bars 48-51: timing is now within ±0.07 s, but the repeated A3 eighths alternate two identical takes (measured, effect inferred)

**Evidence.**
- **Timing.** The -6 dB arrival against the beat (20 ms windows) is 0.00 s on 152.5, 154.5, 157.5 and 161.5 (c36: +0.08..+0.09, so c37 A #5 worked). It is +0.07 s on 153.5, 156.5 and 160.5, and -0.07..+0.03 s on the rest.
- **Separation.** Rests fall 12-14 dB under the peaks on the repeated A3 and 30+ dB elsewhere.
- **Identical takes.** The seven A3 notes play two samples only. 152.5, 154.5, 157.5 and 161.5 have peak -47.3 dB at +0.17 s and an energy centroid of +0.139..+0.140 s. 153.5, 156.5 and 160.5 have -47.4/-47.5 at +0.31 s and +0.174/+0.175 s. All are identical to 0.1 dB and 1 ms.
- **Judgement (inferred).** Over 16 s at pp this is mild, but it is the kind of mechanical sameness a listener can notice in an exposed accompaniment figure.

**Fix (low priority).** Vary velocity by ±3-4 per note on the Detache row (v33-41 around today's 37), in a fixed pseudo-random order, and re-measure. If the row has no velocity layers, vary only the per-note CC7 (±1 dB) and the leads (±0.02 s). Bring the three +0.07 s notes in by 0.03 s (`entry_leads.json` Violas 153.5/156.5/160.5 +0.03).

### 6. Patch options for passages in this lens (inferred)

- **Basses "4 soli" (bars 65-70, 87-92).** They still play the full Basses KS Master at -3 dB, and are now the only 4-soli passage on a full section. `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` (p.89-90, MANUAL-GAPS #8) remains the one patch change with a timbral gain in this lens. The c37 coda shape holds: Cb 273.3-276.2 range -56.7..-51.8 dB (150 ms), so a refit of the 286-304 fills would not have to touch it.
- **Brass portato rows for the bars 61-62 tenutos (MANUAL-GAPS #9).** Not needed. Every tenuto except Horn 2's 208 re-articulates 3-6 dB, and the master dips 1-4 dB at 208/210.
- **Solo violin, bars 17-22.** The Solo Violin library is still not installed (MANUAL-GAPS #3), so there is no change to propose.

## Checked and fine (measured unless stated)

- **Re-bows.**
  - Loop pulse: the 100-300 Hz and centroid autocorrelation at 3.95 s is at most +0.13 on the basses' pedals (220-238, 286-304), the Vc div 4 soli, the final-chord stems and the master. No loop pulse.
  - Dips and steps: 200 ms re-bow dips are 4 dB or less, except Violins I 7.35 (5.6 dB on the stem, master within 1 dB), Violins I 295.0 (5.2, master under 1.5 dB), Violas 86.86 (into the printed p of bar 30) and Violins II 263.92 (+5.5 step inside the cadence crescendo).
- **Bars 61-62 tenutos.** Re-articulations are as above. Bar 63's bass trombone sf falls smoothly.
- **Timpani.** Rolls at 226-237.5 have a 100 ms step SD of 1.47 dB (c36 1.48). Strokes at 172, 203, 209.5, 277, 278.5 and 279 have the same timing and relative levels as c36 after the c37 rebuild (+0.6 dB overall).
- **Trombone 1's quotation.** No note has 2-5 kHz attack energy over its body except 215.5 (-1.1 dB) and the soft 219.5 (+0.4 dB). The master 2-5 kHz jumps are -1.0..-7.9 dB.
- **Brass legato.** No join over an octave, no chord on a Leg row, CC1 at most 108.
- **Unchanged since c36's checks.** These tracks are sample-exact or unchanged in their MIDI per CHANGES: Oboe 1, cor anglais, harp, Violin I solo, the pizzicato rows, Violins II div sul tasto, CC15 mutes, the bar 61-64 tremolo rows and the sf CC7 lanes.

**Do not touch:**
- Trombone 1's quotation shapes, CC7 lanes and 213 accent (weight without bite).
- The violas' Detache portato with its per-note CC7 and the c37 leads.
- The bars 61-64 tremolo rows, sf lanes and the c37 brass +3 dB.
- The bass trombone's sf shape at 212.
- The final-chord, opening and bar 66 re-bows and their fits.
- The c37 basses coda shape (273.35-275.85).
- CC15 placement.
- The timpani stroke timing.
- `WIND_SLUR_REP_MERGE_SKIP` for Flute 1 136 (keep the repeat a separate note; change only its row, its gap and its CC1).
