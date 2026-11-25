# Critic B, cycle 2 (render c01): balance and levels

## Manual notes (May 2021 HO manual, PDF pages 194-200, Chapter 6 "Mix")

Movement I read the same pages in its c37 (`symphony/mvt1/reaper-v621/cycles/c37/reports/B.md`). The pipeline carries that mix over, so each note below is checked against the Finale's `build/mix.json` and the c01 render.

| Page | What the manual says | Where it applies in this mockup | Does the render follow it? |
|---|---|---|---|
| p.194, p.196 | Each instrument has a master channel plus one sub-mixer channel per mic position. Each channel has volume, pan, mute, solo and a load button, and loading a mic loads its samples. | `build_reaper.apply_mix()` writes the `sub:` channels from mix.json `mics`. Winds: Close 0.5 / Main 0.8. Horns and trumpets: 0.5 / 1.0. Timpani: 0.2 / 0.5. Harp: 0.6 / 1.0. Crash and bass drum: 0.3 / 1.0. Basses: 0.6 / 1.0. Tuba: 0.45 / 1.0. Strings and trombones keep the factory mix. Unlisted mics are unloaded. | Yes (read). Nothing in the Finale needs a new mic for balance this cycle. MANUAL-GAPS #4 (Mid mics on the winds) would change depth, not the level findings below. |
| p.195 | "Store Mix" and "Restore Mix" save the Master, Sub Mixer and FX Bus settings. | Not used. The pipeline writes the whole state, so a rebuild reproduces the mix. | Not applicable. |
| p.196, p.198 | An Effects Send on a sub-mixer channel has a level slider and a Post switch. For reverb the manual calls post-fader typical, so the dry mix and the send keep the same level. | mix.json `reverb.send_pre_fader` is true, but the send level is the group send times the mic volume, so it follows the mic level as a post-fader send would. Group sends: strings 0.25, harp 0.3, winds 0.35 (flutes, oboes and cor anglais 0.5), low brass, timpani and percussion 0.45, horns 0.5, trumpets 0.65. Shared hall: fx_volume 0.095 from c01, with a 160 Hz low cut. Every roles, trims and dyn_trim value acts in the REAPER envelope after Opus, so it scales a track's dry sound and its hall together. | Equivalent in level (read). The strings are the driest family, which adds to their presence (inferred). This bears on finding 1: the violins sit on top in ff even where the printed balance gives the brass the lead. The fix there is a level trim, not a send change: Dan asked for less hall, and sends are not to be raised to win depth back. |
| p.199-200 | Opus has insert EQs: Bass Comp (32-256 Hz), a 3-band Channel EQ and a 6-band Equalizer. On a sub-mixer channel they act on the dry mic signal, before the FX-bus reverb. | The mockup uses ReaEQ after Opus, so each EQ also shapes the track's own hall return. In the 13 loud tutti spans (c01 C #1), `loud_eq` adds +3 to +6 dB bells at 140-160 Hz on Cb, Vc, Bn2, Cbn, BTbn, Tuba and Timpani. The bass-octave roles add +3 dB over the same spans. | Consistent with the target "bass solid, not boomy" (measured). In the loud spans the master's 20-100 Hz share is -12.9 to -21.8 dB (Dvořák -21.7, Brahms 1/ii -8.5) and the 100-300 Hz share is -5.4 to -11.3 dB (references -6.6 to -8.8). The basses and cellos supply most of the 20-100 Hz band, never the tuba or timpani. The tuba's problem is its mid-range level (finding 5), not boom. |

MANUAL-GAPS: #7 (half-section divisi patches) leaves balance unchanged: `chord_db` already handles the div. levels. #4 is noted above. No open gap is a balance item this cycle.

## Method

- Stems and master are the c01 render (`cycles/c01/render/`, after the stem fix). `build/parts.json` is the c01 state. There is no `render_shift.json`, so the plain parts.json tempo map applies.
- Analysis frames: a 4096-point STFT with a 25 ms hop, stereo power, K-weighted (the BS.1770 filters applied as a power response), plus the bands 20-100, 100-300, 300-1k, 1-2k, 2-5k and 5-12k Hz. "re M" means a stem minus the master over the same span.
- Co-sounding pairs: for each score beat (1 qn), take every pair of tracks from different families that both sound at least 0.75 of the beat at the same printed dynamic (named from the parts.json `dyn_curve`), and record the level difference. Medians are over beats. Rimsky-Korsakov's resonance table (`reference-books/text/rimsky-principles.txt`, "Comparison of resonance") is the norm, with "twice as strong" read as +3 dB:
  - at forte: trumpet = trombone = tuba = 2 horns, horn = 2 woodwinds, and one violin section = 2 woodwinds (so one horn);
  - at piano: all winds equal, and one violin section = 1 wind.
- Simulations scale the stem frames by the planned envelope change (dyn_trim re-evaluated on the dyn curve, plus roles) and add the difference to the master. This is exact for level-only changes, apart from the 0.5 qn role ramps.
- Score pages read: 9, 13, 14, 15. Events from `build/mockup-events.tsv`.
- Dan's standing checks through this lens:
  - Loop pulsing: only 2 notes are held over 6 s, the timpani at sq 920 and Horn 4 at sq 168. The 100-1000 Hz level folded at 3.95 s varies 4.8 and 4.3 dB, against 4.9 and 6.3 dB at control periods, so there is no pulsing (measured).
  - Accents (item 4): the trombones' accents at 984-1048 measure 2-5 kHz over the first 80 ms 2.0 dB under the body, and Horn 3's 8.5 dB under. The roles proposed below therefore add no harsh bursts (measured).
  - S3: every role proposed here starts and ends on a note onset or in a rest, so no role step falls under a sounding chord's tail.

## 1. In the f-fff tutti the violins sit 3-5 dB over the Rimsky norm and the horns and violas 2-4 dB under it (measured)

**Where.** Every ff and fff tutti: bars 1-8, 27-34, 91-94, 145-168, 199-210, 223, 226-230, 247-279. Track tables `build/mix.json` `dyn_trim_db`.

**Evidence (co-sounding medians, same printed dynamic, dB).**

| pair | norm | f | ff | fff |
|---|---|---|---|---|
| violin minus horn | 0 | +1.8 | +4.5 [605] | +3.3 |
| violin minus trumpet | -3 | -2.1 | -0.5 | 0.0 |
| violin minus low brass | -3 | 0.0 | 0.0 | +1.1 |
| violin minus woodwind | +3 | +3.4 | +5.2 [3004] | +6.0 |
| horn minus woodwind | +3 | +2.2 | +1.0 | +2.7 |
| horn minus trumpet | -3 | -3.0 | -4.0 | -3.2 |
| horn minus low brass | -3 | -1.7 | -4.6 | -2.9 |
| Violas minus Violins I | 0 | -5.5 | -7.3 | -7.7 |
| Violas minus Violins II | 0 | -2.8 | -5.2 | -6.1 |
| Violas minus a solo woodwind (Fl1, Ob1, Cl1, Bn1) | +3 | -0.2 | -0.9 | -0.2 |

- At f the families match the norm within 1-2 dB. From ff up, the violins gain about 3 dB and the horns and violas lose about 2-4 dB.
- Over 29 four-bar blocks at ff/fff, violin minus brass is positive in 76 % of them. It is worst in the intro (bars 1-8, +5.4) and the recapitulation (bars 149-168, +2.6 to +6.9).
- In the recap (bars 151-166) F1 is doubled in Vln I, Fl 1-2, Ob 1, Violas and Horns 1-2 a2, all ff. Measured re M: Vln I -6.9, Horn 1 (a2, with the +3 dB unison boost) -11.4, Violas -16.6. The horns, which give the tune its weight an octave below the violins, sit 4.5 dB under one violin section. The violas on the same line sit 9.7 dB under it.
- Cause (read): Violins I `gain_db` +5 with `dyn_trim_db` ff +1.5, and Violins II +6 / ff +1.0. Violas carry f -2 / ff -3. The horns carry ff -1.0 / -2.1 / -0.4 / +2.0 and fff -3.7 / -3.7 / -0.2 / +2.0. All are Movement I's values, fitted on a score with fewer brass tuttis.

**Fix (`build/mix.json` `tracks`).** Leave every f anchor of the violins alone (bars 11-26: the cellos would rise over the F1 tune again). Change:
- Violins I `dyn_trim_db` to `{"f": 0.0, "ff": -1.0, "fff": -1.5}`.
- Violins II to `{"f": -1.0, "ff": -1.0, "fff": -1.5}`.
- Violas to `{"f": 0, "ff": 0}`.
- Horns 1-4: ff +1.5 and fff +1.5 each, giving Horn 1 ff 0.5 / fff -2.2, Horn 2 ff -0.6 / fff -2.2, Horn 3 ff 1.1 / fff 1.3, Horn 4 ff 3.5 / fff 3.5.

**Simulated.**
- At ff: violin minus horn +0.4, violin minus trumpet -2.6, violin minus low brass -2.2, violin minus woodwind +2.9, horn minus woodwind +2.5, horn minus trumpet -2.2, horn minus low brass -2.8. Violas minus Violins I -1.7. All are within 1 dB of the norm.
- Recap 151-166: Vln I -9.1, Horn 1 -9.6, Violas -13.3.
- Bar 223: Vln I -14.3 and Vln II -15.2 (from -11.3 / -12.6), with Horn 3 -12.4 and Trumpet 3 still on top.
- Bars 273-277: Horn 1 -9.0 on top, with the tremolo Vln II at -12.2.
- The master falls 0.0-0.4 dB in these spans, so the climaxes stay the loudest bars: 223 -5.8, 263 -7.4, 278-279 -9.5 K.
- Bars 11-26 are unchanged: Vln I -5.7, Vc -7.7.

## 2. Bars 255-262: movement I's theme (Hn 3-4, Vln II, Vla, Vc ff espress.) is 8 dB under the chorale's whole notes (measured)

**Where.** Letter S, qn 1016-1048. The score combines the two ideas. The theme is in Horns 3-4 a2, Violins II, Violas and Violoncellos, all marked "ff espress." with a hairpin swell. The chorale in doubled values is in Trumpets 1-2 a2 ff, Horns 1-2 f, Trombones mf, Bass trombone and Tuba ff, with Vln I holding ff chords. From bar 259 the theme goes on in Vln II's eighths and Horns 3-4's accented halves.

**Evidence (re M, qn 1016-1032).**
- Chorale: Trumpet 1 -6.2 (the a2 copy, +3 dB unison boost) and Violins I -6.5, both whole notes, are the two loudest stems.
- Theme: Horn 3 -14.8, Violins II -14.1, Violas -17.5, Violoncellos -17.5. The cellos already carry the c01 role of +2.
- Bars 259-262 (qn 1032-1048): Vln I chords -9.3 against Vln II's theme figures -13.4 and Horn 3 -17.6.
- A listener hears a held chord with the theme as an inner murmur. Inferred: the point of the passage is that both ideas are heard.

**Fix (`build/roles.json`, added rows).**
- Trumpet 1 and Trumpet 2 `[1016, 1032, -3]`.
- Violins I `[1016, 1048, -2]`.
- Violins II `[1016, 1048, 2]`.
- Violas `[1016, 1032, 2]`.
- Horn 3 and Horn 4 `[1016, 1048, 3]`.

All start at the bar-255 onset after a rest and end at a new onset (1032, 1048). Together with finding 1 the simulation gives:
- 255-258: Horn 3 -9.8, Violas -12.0, Violins II -12.9 against Trumpet 1 -8.4 and Violins I -10.2.
- 259-262: Horn 3 -13.2, Violins II -13.7, Violins I -14.1, Trombone 1 -8.5 (chorale) on top.
- The master falls 0.8 dB over 255-258 and is unchanged over 259-262.

## 3. Bars 247-254: the "full brass" of the Più allegro sits under the winds and violins (measured)

**Where.** Letter R, qn 984-1016. Movement I's cantabile head is in Fl, Ob and Cl ff, Horns 1-2 ff and Trumpets 1-2 f (Trumpets at 984-1000 only). F1's dotted head is in Vln I/II, Vc and Bn ff and Trombones 1-2 a2 f, with accents.

**Evidence (re M, qn 984-1000).**
- Cantabile: Flute 1 -8.9, Horn 1 -10.9, Oboe 1 -11.6, Clarinet 1 -13.2, Trumpet 2 -14.1, Trumpet 1 -15.4.
- Dotted head: Violins I -9.1, Violins II -11.4, Violoncellos -12.4, Bassoon 1 -17.9, Trombone 1 -18.0. Trombone 2's notes are merged into Trombone 1 by the unison rule.
- So the a2 trombones on F1's head sit 9 dB under one violin section on the same figure, and the f trumpets 6.5 dB under Flute 1.
- By the norm, a trumpet at f is worth four woodwinds and an a2 trombone pair four horns. At this tempo, inferred, the passage sounds like a woodwind-and-strings tutti with brass colour.
- The accents measure 2-5 kHz 2 dB under the body, so a level lift adds weight without bite.

**Fix (`build/roles.json`).** Trombone 1 and Trombone 2 `[984.5, 1016, 4]`, starting at the first note after the rest. Trumpet 1 and Trumpet 2 `[984, 1000, 3]`; they rest from 1000. Simulated with finding 1, over 984-1000: Trombone 1 -14.5, Trumpet 1 -12.7, Horn 1 -9.8, Flute 1 -9.2, Violins I -11.9. Over 1000-1016: Trombone 1 -11.2. The master is 0.3 dB louder.

## 4. At mf the oboes, clarinets and violas play 2-4 dB under their p balance (measured; contexts differ between dynamics)

**Where.** Every printed mf for Oboe 1-2, Clarinet 1-2 and Violas: bars 67-82, 159-166 (Cl 1-2 mf espress.), 187-198, 235-246, the development. Tables: mix.json `soft_trim_db`.

**Evidence.**
- Each track minus the co-sounding strings and brass at the same printed dynamic (Vln I/II, Vc, Hn 1-4, Tbn 1, Tpt 1):

| track | p | mp | mf | f |
|---|---|---|---|---|
| Clarinet 1 | +0.8 | +0.8 | -3.5 | -3.1 |
| Oboe 1 | -3.2 | +1.2 | -4.5 | -2.4 |
| Violas | +1.2 | +0.5 | -1.9 | -2.4 |
| Flute 1 | +1.1 | -1.6 | +0.9 | -2.8 |

  Flute 1 has no mf drop, which shows the drop is in the reeds' and violas' mapping, not in the passages.
- Each track's own median level minus its roles (vol_db), p / mp / mf / f:
  - Clarinet 1: -40.2 / -39.3 / -39.9 / -37.5, only 2.7 dB from p to f.
  - Oboe 1: -43.8 / -41.3 / -41.7 / -36.0.
  - Violas: -40.3 / -39.6 / -39.7 / -35.0.
  - For comparison, Violins I -39.7 / -35.3 / -32.3 / -30.4 and Trumpet 1 -44.8 / -40.0 / -34.9 / -30.4.
- Cause (read in `vol_points()`):
  - Clarinet 1's soft trim falls from p +5.0 to mf +0.1, and Clarinet 2's from +7.1 to +1.0.
  - The oboes go from p +5 to mf +3.1.
  - The violas have no mf anchor, so the trim falls linearly from p +5 to f -2, about +0.7 at mf.
  - CC11's growth from p to mf is largely cancelled, as Movement I c02 found for the flutes before it added their mf anchors.

**Fix (`build/mix.json` `soft_trim_db`).**
- Clarinet 1: mf 0.1 -> 2.5, mp 2.2 -> 3.0.
- Clarinet 2: mf 1.0 -> 3.0.
- Oboe 1 and Oboe 2: mf 3.1 -> 5.5.
- Violas: add `"mf": 3.0`, keeping pp 6 / p 5 (with finding 1's f 0 / ff 0).

**Simulated, mf pair medians.** Clarinet 1 -1.6, Oboe 1 -2.6, Violas +0.3, with p unchanged. In the passages:
- Bars 67-82: Violas -11.3 and Oboe 1 -16.3 under Vln I's F2 at -5.3.
- Bars 159-166: Clarinet 1 -21.2 under the ff tune.
- No solo is overtaken.
- This also lifts the middle of the loudness range slightly; the delivered LRA is 17.0 LU against the 14-16 target. The loudness arc itself is left to critic C (dynamics) this cycle.

## 5. The tuba is the loudest stem in the final chord and in several ff tuttis (measured; harm inferred)

**Where.** Bars 278-279 (qn 1108-1116), also 91-94, 27-34 and 251-254. Tables: `build/roles.json` Tuba, mix.json Tuba.

**Evidence.**
- K re M: bars 278-279 Tuba -10.2, the top stem. The trombones are at -12.7 / -13.2 and the bass trombone at -15.1.
- Codetta 91-94: Tuba -10.3, the second loudest. Bars 251-254: Tuba -8.7, the top.
- Tuba minus trombones (same dynamic): -1.0 at f, -0.6 at ff, +2.6 at fff. The norm is 0.
- Its band shares show the excess is in the 300 Hz-2 kHz harmonics, not in the 20-100 Hz band: the basses and cellos supply that band (manual notes, p.199-200).
- Source: c01's bass-octave role, Tuba `[1032, 1116, 3.0]`, sits on top of `loud_eq` (140 Hz +4) and Tuba `gain_db` +2. A final C-major chord led by the tuba's mid-range sounds thick rather than bright (inferred).

**Fix (`build/roles.json`).** Split the last Tuba row into `[1032, 1088, 3.0]` and `[1088, 1116, 1.0]`. Rows that meet crossfade at 1088, which is an onset after the allargando. Simulated: Tuba -12.0 at bars 278-279, level with the trombones (-12.6 / -13.1), with Horn 1 (after finding 1) at -10.8 on top. Leave the counterstatement (27-34) as it is: there the tuba carries F1 in the bass, as written.

## 6. Bars 224-225: the violins' mf chords sit level with the f brass chorale (measured; small)

**Where.** qn 892-900, the first two chorale bars after the arrival. Brass are marked f, with whole notes in trumpets, horns and trombones. Vln I/II have mf chords, Violas and Cellos f.

**Evidence.**
- Re M: Trombone 1 -7.7, Trumpet 1 -8.6, Violins I -9.6, Trumpet 2 -10.5, Horn 3 -11.2.
- The norm for a violin section at mf against a trumpet at f is about -5 dB. Here the gap is -1.
- Finding 1 does not reach these bars (mf trims are unchanged).

**Fix (`build/roles.json`).** Violins I and Violins II `[892, 900, -2]`, from the bar-224 onset to the ff entry at bar 226. That entry is a new onset, so the role ends under a fresh attack. Simulated: Vln I -11.3 against Trombone 1 -7.5 and Trumpet 1 -8.3.

## Do not touch

- The solos and accompaniment from c01, re-measured on c01 (K re M):
  - Trumpet 1, bars 51-66: -2.5 over Clarinet 1 at -9.2.
  - Motive x solos, bars 43-48: Flute 1 -4.8, Clarinet 1 -3.3, Oboe 1 -3.4, each 3-5 dB over the pp strings.
  - Bassoon solo, bar 115: -2.0.
  - Harp solo, bars 123-134: -4.1.
  - Cor anglais with muted Trumpet 1, bars 171-186: -3.3 / -6.5.
  - Harp under the violins' F2, bars 67-82: -7.9 against -5.3.
  - Trumpets on movement II's theme B, bars 211-218: -6.8 / -8.0 on top.
- The family order at bar 223 (brass on top), the tremolo row gains, and the bass-octave roles and `loud_eq` on the basses and cellos (bass solid, not boomy).
- The timpani under the texture: rank 20-26 of 25-29 stems at bars 147-150, 223, 261-264 and 278-279, and never the loudest stem in a roll.
- The crash at -9 to -10 dB re M in its first 0.3 s at 888, 1048 and 1108, carrying the 5-12 kHz band (heard, not dominant).
- Bars 11-26, where the cellos sit level with the F1 tune and no longer above it: keep the violins' f anchors.
