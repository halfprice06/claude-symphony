# Critic B, cycle 1 (render c00): balance and levels

## Manual notes (May 2021 HO manual, PDF pages 137, 140, 150-151)

| Page | What the manual says | Where it applies in this mockup | Does the render follow it? |
|---|---|---|---|
| p.137 | Each KS Master row has a load button and its own volume knob. | `build_reaper.load_articulations()` loads the used rows and unloads the rest. No row volume is set. Rows whose level differs from the sustain rows: Violins I/II "Tremolo" (bars 223-225, 255-262, 273-278) and Trumpet 1 "Mute Sus" (qn 680-792). | Partly. Loading: yes. Row level: not compensated. `ROW_TRIM_DB` covers only Sus/Stac notes near Leg-row notes, so the tremolo rows play 3-9 dB over the sustain rows at the same CC11 (finding 2) and the mute row about 5 dB under them (finding 4). As Movement I c36 found, make the correction in the envelope, not with the row knob: the knob also scales the hall send. |
| p.140 | Master channel gain sets the instrument's output without changing the mic mix. Pan keeps the mics' relative pans. | `apply_mix()` centres the main pan. Track gain goes into the REAPER volume envelope (`vol_points`, `gain_db`). | Yes. |
| p.150 | Velocity sensitivity is linear by default. Velocity picks the sampled dynamic layer and is used mostly on shorts. | Every pizzicato in bars 51-66 and 171-186 plays at velocity 41, which is the pp layer. `vol_points()` then adds the mix.json soft trim from the printed dynamic on top of that, whatever the articulation: Violoncellos pp +6 dB. | Partly. The velocity is right, but the soft trim (meant to lift CC11 sustains at pp) is stacked on a pp layer that velocity already chose (finding 5). |
| p.151 | Send CC1/CC11 before the first note. CC7 sets each track's ceiling; CC11 shapes the line. | The 3 qn pre-roll carries the first CC values. Ceilings are in the envelope; CC11/CC1 follow the printed dynamics (CC11 126 at fff). | Partly. The hairpin dB ramps (`hpgain`) also sit in the post-Opus envelope. They add up to +7.9 dB on the woodwinds and +6.9 dB on the strings at the bar-223 fff, but only +2.9 dB on the brass. So the envelope is doing dynamic shaping and changes the family balance (finding 1). Timpani roll levels use CC7, as in Movement I. |

MANUAL-GAPS: #7 (half-section divisi patches) bears on the Violins II div. tremolo chords at bars 223 and 273-278. The `chord_db` cut (-3 for div., -3 for tremolo) already handles their level, so no new instance is needed for balance. No other open gap is a balance item this cycle.

## Method

- Stems and master are c00 `render/`. Bar times come from the parts.json tempo map.
- Levels are plain RMS and K-weighted (BS.1770 curve applied in an STFT, 4096/2048) per bar and per passage. "re M" is the stem level minus the master over the same span.
- Row levels are per-note bodies (+0.15 s to note end, at most 1.5 s), stem level minus the parts.json `vol_db` at the note. They are grouped by row (from the keyswitch lane) and by CC11 (CC1 on brass). Chords count each note, so the figures for chord rows include the chord sum.
- Simulations scale stem waveforms and re-sum them (exact for level-only changes).
- Score pages read: 2, 3, 4, 10, 13, 14, 15.

## 1. The fff climaxes put woodwinds and violins on top and the brass underneath; bar 223 overshoots by 4-5 dB (measured; cause read)

**Where.** Bar 223 (qn 888-892), the C-major arrival. Also bar 263 (qn 1048) and bars 278-279 (qn 1108-1116).

**What the score has.** A tutti fff chord: Trumpet 1 B to C, the brass chorale's first chord, the string tremolo, crash and bass drum. Bar 224 drops to f in the brass and mf in the violins.

**Evidence (measured).**
- Bar 223 is the loudest bar in the piece: master -8.0 dB RMS (K -3.9). That is 12.5 dB over bar 224 (K 13.8 dB). The master float sum peaks at +6.0 dBFS at 329.36 s (qn 889.5).
- Stems in bar 223, K re M:
  - strings and woodwinds: Violins II -7.5, Violins I -6.8, Flute 2 -8.6, Flute 1 -12.4, Clarinet 1 -12.8
  - brass: Trumpet 1 -16.0, Trumpet 3 -14.2, Trombone 2 -14.9, Horns -17.0 to -22.5, Tuba -16.5
- Family sums in bar 223 (plain RMS): woodwinds -13.1, brass -13.6, strings -12.0 dB. In a real fff tutti arrival the brass lead.
- Cause, read in parts.json `vol_db` at qn 889:
  - every woodwind +7.9 dB, Violins I / Violas / Basses +6.9, every brass +2.9
  - the source is `hpgain` from the chained crescendos mp<f (880-884) and f<fff (884-888): `HP_GAIN_DB` wind 4 / string 3 / brass 2, plus `HP_CHAIN_RISE_FFF` wind 0.75 / string 1.0 / brass 0.5, held by `FFF_HOLD_CAP` 8 qn (tools/score_to_parts.py lines 187, 293, 299)
  - CC11 is already 126 there
  - the same asymmetry recurs at qn 1049 (woodwinds +6.6 to +7.0, brass +1.9) and at qn 1109 (woodwinds +4.0, brass +2.3, strings -4.8)
- Bar 263, K re M: Clarinet 1 -10.0 and Oboe 1 -10.0 against Horn 1 -17.9, Trumpet 1 -11.0, Trombones -13.6. Bars 278-279: Flute 1 -8.2 is the loudest stem.
- S3: at qn 892 the master falls 8.1 dB in 150 ms (-11.4 to -19.5 dB in 50 ms windows). Violins II falls 7 dB. The hpgain release (strings 6.9 to 0.9 dB over 1 qn) is a post-hall volume step, so it cuts the fff's hall ring.
- Simulation of bar 223 (scaling only): woodwinds -4 dB, strings -3 dB, tremolo trims as in finding 2, brass +2 dB. The master goes from -8.0 to -9.6 dB RMS and the peak from +6.0 to +4.2 dBFS. Family sums become woodwinds -17.1, brass -11.6, strings -17.7 (brass on top). The bar is still within 0.2 dB of bars 262-263 and 278, which matches the brief's two climaxes.

**Fix.** In `build/score_config.py`:
- `HP_CHAIN_RISE_FFF = {"wind": 0.0, "string": 0.0, "brass": 0.5}` (Finale value; CC11 is already at 126 at these arrivals).
- Add `"fff": -4` to the `dyn_trim_db` of Flute 1 and Flute 2 in `build/mix.json` (today fff uses the ff -1), and `"fff": -2.5` to Oboe 1/2 (today ff +6).
- Add a roles.json brass row for the arrival chord only: `[888, 892, 2.0]` on Horn 1-4, Trumpet 1-3, Trombone 1-2, Bass trombone and Tuba.

Measure afterwards:
- bar 223 family sums (brass ≥ strings ≥ winds), master peak, and bar 223 against 263 and 278-279 (within about 1 dB)
- the fall at qn 892: under about 4 dB in the first 150 ms. If the string release still steps, `FFF_HOLD_CAP` 8 → 4 gives a slower release.

## 2. The violin tremolo rows play 3-9 dB over the sustain rows, so the accompaniment covers the chorale (measured)

**Where.** Violins I and II tremolo: bars 224-225 (qn 892-900, mf under the brass chorale at f), bars 255-262 (qn 1016-1048, Violins I ff tremolo double stops under the chorale in doubled values in Trumpets 1-2 a2), bars 273-277 (qn 1088-1108).

**Evidence (measured).**
- Row bodies at CC11 110-127, stem minus envelope:
  - Violins II: Tremolo -16.2, Sus MAX -24.7, Leg BC MAX -29.5, Leg Slur MAX -34.9 dB
  - Violins I: Tremolo -21.3, Sus MAX -24.6, Leg BC MAX -28.3 dB
  - Violas and Violoncellos tremolo are not above their Sus (-29.8 against -30.1, and -26.2 against -23.3).
- K re M by passage:
  - bars 224-225: Violins I mf tremolo -7.5, the loudest stem, against Trumpet 1 -9.3, Trombone 1 -9.0, Horn 3 -12.8, Horn 1 -15.6.
  - bars 255-262: Violins I tremolo -6.2, the loudest stem, against the chorale tune Trumpet 1 -9.6 and the espress. countermelody Violins II -14.4 / Violas -17.6.
  - bars 273-277: Violins II tremolo -7.7, against Horn 1 -10.4, Trumpets 1/3 -10.5/-10.8.
- Simulation, Violins I -4 dB in 255-262: Violins I -10.9 against Trumpet 1 -9.3. The tune is on top and the master drops 0.5 dB.
- Simulation, Violins I -3 / Violins II -4 / Violas -3 in 273-277: Violins II -11.2 against brass -8.8 to -10.2.

**Fix.**
- Generic, preferred: in `tools/score_to_parts.py`, add a row offset applied to every note on a row, beside `ROW_TRIM_DB` (which needs a Leg-row neighbour). For example `ROW_GAIN_DB = {track: {art: dB}}`, folded into `vol_parts` like the chord cut, starting at the note's moved onset. Finale values in `build/score_config.py`: `{"Violins I": {"Tremolo": -3.0}, "Violins II": {"Tremolo": -4.0}}`.
- Without a tool change, use `build/roles.json` rows:
  - Violins I `[888, 900, -3]`, `[1016, 1048, -4]`, `[1088, 1096, -3]`, `[1108, 1112, -3]`
  - Violins II `[888, 900, -4]`, `[1088, 1100, -4]`, `[1108, 1112, -4]`
  - Start rows on the tremolo onsets, so no step falls under a sounding chord (S3).

## 3. The Violoncellos are 2-5 dB too loud almost everywhere and sit over the tune (measured)

**Where.** Violoncellos, whole movement. The clearest cases are bars 11-26 (qn 40-104, F1 in Violins I with the horns), bars 239-241 (qn 952-964, the molto cantabile theme in Violins I and Oboe 1 over held bass notes), and bars 43-50 (qn 168-200, pp held div. chord under the motive x solos).

**Evidence (measured).**
- K re M by passage, cellos against the tune:
  - bars 11-26: Violoncellos -4.3 against Violins I -7.3 and Horn 1 -11.2. Per bar the cellos (quarter-note bass line, f) are 1-5 dB over Violins I (bar 12: -31.2 against -36.5; bar 18: -26.1 against -29.7).
  - bars 239-241: Violoncellos held f whole notes -25.6 / -28.2 / -27.9 dB against Violins I -28.8 / -28.2 / -29.6.
- The cellos are the loudest or second-loudest string stem in every section except P and T (K re M: intro -7.4, A -4.3, C -5.4, F -5.3, K -7.3, M -6.5, Q -8.1).
- Metrics table medians: Violoncellos over Violins I at every printed dynamic (p -40.5 against -43.6, f -31.9 against -35.1, ff -27.7 against -28.2).
- The cellos' mix values come straight from Movement I (`gain_db` 0, soft trim pp 6 / p 5 / mf 0.7). Movement I's cellos often carried the tune; here they mostly play the bass.
- Simulation, bars 11-26, cellos -3 dB: -5.4 against Violins I -7.4. That is still over the tune, so -4 dB is needed.

**Fix.** In `build/mix.json` Violoncellos: `gain_db` 0 → -4, `soft_trim_db` pp 6 → 4, p 5 → 3.5. Then lift back with roles where the cellos carry a line:
- bars 67-82 mp espress. counter-melody: `[264, 328, 2]`
- bars 187-198 espress.: `[744, 792, 2]`
- bars 255-258 espress. with Violins II / Violas: `[1016, 1032, 2]`

Check afterwards that the cellos sit 2-4 dB under Violins I in bars 11-26 and 239-241, and the bass (Vc + Cb) stays solid against the 100-250 Hz reference share (mix -9.8 dB against Dvořák -6.6: there is room).

## 4. The soft solos sit level with, or under, their pp accompaniment (measured)

**Where and evidence (K re M, measured).**
- **D, bars 51-66 (qn 200-264).** Trumpet 1 solo, p dolce cantabile: -5.0. Clarinet 1, pp held: -5.2. Pizz cellos, pp: -8.4. Per bar, Clarinet 1 is louder than the solo in 9 of 16 bars (bar 53: -41.0 against -45.1 dB RMS; bar 54: -42.5 against -49.0).
- **C, bars 43-48 (qn 168-192).** The motive x solos (Flute 1 bars 43-44, Clarinet 1 bars 45-46, Oboe 1 bars 47-48, all p) are 2-6 dB under the pp strings:
  - bar 44: Flute 1 -42.6, Violins I -38.1, cellos -41.2 dB
  - bar 45: Clarinet 1 -42.4, cellos -36.7
  - bar 48: Oboe 1 -40.5, cellos -40.4
  - Violins I's pp "harm." B flat is played as an ordinary Leg Slur MAX note (keyswitch at qn 163.6). That is articulation lens A, but it also makes the string pad louder than printed.
- **L, bars 171-183 (qn 680-732).** Trumpet 1 con sordino doubles the cor anglais, both p dolce cantabile. Plain re M over 680-700:
  - cor anglais -4.0, Trumpet 1 -10.1, bass clarinet pp held -5.9, violas pp eighths -10.8
  - the muted trumpet, which gives this passage its colour, is 6 dB under the cor anglais, and the pp bass clarinet is 2 dB under the solo.
  - The Mute Sus row's bodies at CC1 under 60 measure -49.1 dB against -44.4 for Sus Non Vib MAX (different notes, so inferred: about 5 dB quieter).

**Fix (`build/roles.json`).**
- Trumpet 1 `[200, 264, 2.5]`, Clarinet 1 `[200, 264, -4]`. Simulated: Trumpet 1 -3.0, Clarinet 1 -8.5.
- Flute 1 `[168, 176, 4]`, Clarinet 1 `[176, 184, 4]`, Oboe 1 `[184, 192, 4]`, Violins I `[168, 200, -3]`. Cellos as in finding 3. Simulated: solos -7.3 to -10.3 against Violins I -9.7 and cellos -7.1. Go up to +5 on the solos if the cello gain change does less than simulated.
- Trumpet 1 `[680, 792, 3]` (the mute span), Bass clarinet `[680, 744, -4]`. Simulated over 680-700: cor anglais -3.5, Trumpet 1 -6.6, bass clarinet -9.4. Over 712-732: Trumpet 1 -2.9, cor anglais -6.5. That is too high: there use `[712, 732, 0]`, or fit per phrase after one render.

## 5. The pp cello pizzicato is velocity pp plus a +6 dB soft trim, and its attacks reach the solo's level (measured)

**Where.** Violoncellos pizz, bars 51-66 and 171-186 (qn 200-264, 680-744).

**Evidence (measured).**
- Every pizz note is velocity 41 (`Pizzicato RRx4`), the pp layer (p.150). `vol_points()` adds the cellos' soft trim (+6 dB at pp) from the printed dynamic, whatever the row.
- First 250 ms of the low pizz notes: -33 to -41 dB (qn 214: -38.8; 231: -37.3; 709.5: -33.9; 710: -32.6). The trumpet solo's body is -45 to -49 dB, and the cor anglais' is -42 to -46.
- Bar 178 (qn 708-712, pizz eighths with the timpani "near the rim"): cellos -36.3 dB RMS against cor anglais -45.5, the loudest stem in the bar.
- Violins II / violas / basses pizz are not affected (-53 to -62 dB; their soft trims are smaller or their notes higher).

**Fix.**
- Generic: in `tools/build_reaper.py vol_points()`, skip the soft-trim anchors (use 0 dB) on spans where the track's sounding notes are on a velocity-driven pizz row ("Pizz RRx4", "Pizzicato RRx4"; take the row from the parts.json `ks` lane). Use a mix.json key such as `"soft_trim_skip_arts": ["Pizz RRx4", "Pizzicato RRx4"]` so the rule stays generic.
- Without a tool change: Violoncellos roles `[200, 264, -5]` and `[680, 744, -5]`, on top of finding 3. Simulated: cellos -11.7 re M in D and -13.7 to -15.7 in L.

## 6. The harp's mf arpeggios sit over the violins' F2 (measured)

**Where.** Bars 67-82 (qn 264-328): F2 in E flat major in Violins I/II, mf cantabile, over harp arpeggios mf. Also bars 239-242 (qn 952-968).

**Evidence (measured, K re M).**
- Bars 67-82: Harp -5.3 against Violins I -6.6 and Violins II -11.2. The harp is the loudest stem in 12 of the 16 bars (bar 70: -29.2 against -31.4 dB).
- Bars 239-241: Harp -29.5 / -29.7 / -29.9 against Violins I -28.8 / -28.2 / -29.6 dB RMS.
- The harp's mix (`gain_db` -4, dyn f +1) is Movement I's.

**Fix (`build/roles.json`).** Harp `[264, 328, -4]` and `[952, 968, -3]`. Keep the solo of bars 123-134 as it is (-4.3 re M, correct). Simulated for bars 67-82: Harp -7.8, Violins I -7.2.

**Do not touch.**
- Movement II's theme B in the trumpets, bars 211-218: Trumpet 1 -8.1, Trumpet 2 -6.7, Violins I -11.5 K re M.
- The bassoon solo at bar 115: -2.5 re M, accompaniment 5-10 dB under.
- The harp solo, bars 123-134: -4.3.
- The counterstatement, bars 27-34: the bass group carrying F1 sums equal to the violins' countersubject (-20.9 against -20.9 dB). Horn 3 a2 leads at -8.9.
- Crash cymbals at 223, 263 and 278: -10 to -12 dB re M overall, carrying the 5-12 kHz band (heard, not dominant).
- Bass drum at the attacks.
- Timpani under the texture at the arrival and the ending: -24.3 at bar 223, -22.9 at bars 278-279 K re M.
