# Cycle 33, critic B: balance and levels (on the c32 render)

**Method.** I used the final stems in `cycles/c32/render/` (the Violin I solo stem is the stem-fixed one) and the tempo map and tables in `build/parts.json`. At c32 that file is identical to `cycles/c32/rendered_build/parts.json`.
- **Level scale.** K-weighted levels (BS.1770 filter applied in the frequency domain), ungated, both channels summed, 4096-point frames every 50 ms. On this scale the master reads about 3 dB under its gated LUFS.
- **Note bodies.** From onset + 0.15 s to 0.05 s before the note's end.
- **Other bands.** Unweighted 20-100 Hz, 100-300 Hz and 2-5 kHz.
- **Accompaniment.** The power sum of every other stem.
- **Labels.** "Measured" means a number from the render, parts.json, a table or a patch state. "Inferred" means a judgement about what a listener hears.

## Manual notes (B6: May 2021 HO manual pp. 32-34, 43, 46, 191-192; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.32 §2.3.1 Streaming: the preload size sets how much of each sample is held in RAM against streamed from disk. "Never preload" streams everything. | All 32 instances. Opus `Preferences.json` has `PreloadSize 1` and `NeverPreload false` (read). | Yes. Unchanged tracks render **bit-identically** from one cycle to the next (measured: Harp c31 and c32 have the same md5; Oboe 1, Cor anglais, Timpani and others differ by 0.0). Each render starts from a fresh restart. So streaming causes no level or take differences, and a level table fitted on one render holds on the next. |
| p.33 Multi-threading (reverb, voice renderer, render threads); output configuration. | Offline 1x render. | The settings are single-threaded: `RenderMultiThreaded2 false`, `UseMultiThreadedReverb false`, `NumVoiceRenderThreads 1`, `PluginStereoOuts 9` (read). This is safe for an offline render, and only the main stereo out is used. It has no effect on balance. |
| p.34 §2.3.3 MIDI: channel assignment, Round Robin reset controller or note, program change to articulation. | Round-robin repeatability; keyswitching. | The preference is `RoundRobinResetCC 16`, but the pipeline sends CC36 in the pre-roll (MANUAL-GAPS #10). Unchanged tracks repeat exactly anyway (row above), so with a fresh restart per render the takes are already deterministic. MANUAL-GAPS #10 therefore has no level benefit for this mockup. `ProgramChangeToArticulation false`: keyswitches only, as built. |
| p.43 Purge and instrument rack: the per-instrument volume slider is the same control as the Play-page channel fader and the Mix-page fader. | Track levels. | Every instrument and channel `volume` in the 32 states is 1.0 (read). Levels come only from CC7, CC11 and REAPER's envelope and gain, so no hidden fader offset distorts the balance. |
| p.46 System usage (voices, CPU, RAM, disk). | REAPER memory record. | Not visible to scripts. CHANGES records 45 GB after the c32 render. |
| p.191 All Instances window: per-instrument purge and the articulation selector. | `UNLOAD_UNUSED_ROWS`. | Equivalent behaviour is already scripted (rows a track does not use are unloaded). |
| p.192 Voice Limit ("raise the Voice Limit" if voices drop), Octave, Key Range. | Divisi chords, harp ring, re-bow overlaps. | Voice limits are 250 (winds, brass, harp, timpani) and 350 (strings), with `InstrumentVoiceLimitMax 1024` (read). The most notes sounding at once, counting a 1 qn release tail, is 10 on the Harp, 8 on the Violas and 6 on each violin section (measured in parts.json). Even with several mics and crossfaded layers per note this is far below the limits, so no chord tone is stolen (inferred). Octave and Key Range are unused, which is correct. |

From MANUAL-GAPS, only #8 (half-section patches for the 4 soli) touches this lens. The -3 dB 4-soli roles from c32 measure as intended (checks below).

## 1. The horns are weak at the bar 61 ff arrival: Horn 1 plays the downbeat 5 dB under its own crescendo peak, and the ff horns sit at the level of a single woodwind (measured; the target ratio is Rimsky-Korsakov's)

**Where.** Bars 60-62 (qn 200-212), Horn 1 and Horn 2. The score prints ff at 204 on Horns 1-2, Violins I and Flute 1, and f on Horns 3-4 and the low brass ("ff molto sostenuto").

**Evidence (measured, 0.5 qn K-weighted means).**
- **Horn 1 through bars 60-62.**
  - In the crescendo: 202.0 -23.4, then 202.5-203.5 -27.0..-28.1.
  - The ff downbeat: 204.0 -22.9 (attack), then **204.5-207.5 -28.0..-30.5**.
  - Bar 62: 208-211.5 -22.8..-27.1.
  - So the ff bar is Horn 1's weakest bar from bar 59 to bar 62.
- **Cause.**
  - vol_db falls from +5.7 at 203.95 to -3.4 at 204.5 and stays at -3.4..-0.9 until 208. It then jumps back to +7.8.
  - CC1 108 (the ff layer) and CC11 122 do not make up for the 9 dB envelope drop.
  - The momentary 202 peak comes from the early fill `"202": {"db": 6.5, "hold_s": 0.35}` (+13.5 dB vol at 202.0-202.35).
  - This repeats the kit rule broken in series 1: a crescendo's arrival must not fall (mockup-kit LEARNINGS §4, "hold that ramp until the first onset after the arrival note").
- **Section balance, qn 204-212 means.**
  - Violins I -20.0.
  - Single woodwinds: Clarinet 1 -24.8, Flute 1 -26.2, Flute 2 -26.1, Oboe 1 -27.3.
  - Horns: **Horn 1 -26.1, Horn 2 -26.5**, Horn 3 (Horns 3+4 in unison, +3 dB unison boost) -27.6.
  - Low brass at f: Trombone 2 -23.5, bass trombone -25.1, tuba -27.1.
  - Group sums: strings -16.5, woodwinds -17.1, **horns -23.0**, low brass -19.7 (bar 61).
  - In 2-5 kHz the horns are 15-16 dB under the strings: horns -40.8, strings -24.9.
- **Rimsky-Korsakov's forte ratios** (`reference-books/text/rimsky-principles.txt` around line 1965): trombone = 2 horns, horn = 2 woodwinds, and one string section = 2 woodwinds.
  - So a ff horn should be about 3 dB over a single ff woodwind and about level with one string section.
  - Measured, Horns 1-2 are level with the single woodwinds (0 dB), 3 dB short of that, and Horn 1 is also 5 dB under its own bar-60 crescendo.

**Why it matters (inferred).** The climax downbeat loses the horn glow. Bar 61 sounds like strings and woodwinds, with the horns arriving only in bar 62.

**Fix.**
- `build/roles.json`:
  - Horn 1: add `[203.95, 208, 4.5, 0.25]`. It ends on the 208 onset, so no step falls under a sounding note.
  - Horn 2: add `[203.9, 212, 2, 0.25]`.
- Simulated (dB arithmetic on the stems, 0.25 qn ramps):
  - Horn 1 bar 61 -23.2 (bar 62 -24.8). Horn 2 -26.0 / -23.3.
  - Master bar 61 -12.27 -> -11.85, bar 62 -12.10 -> -11.82. Bars 79-80 unchanged, so the climax order gets 0.4 dB more margin.
- Alternative: keep the hairpin and role gain held through 204-208 in `score_to_parts.py` (the hold rule), and check whether the 202 early fill (+6.5 dB) is still needed after c31's CC1 map change.
- Level only, so `stem_fix.py` can simulate and apply it.
- Delivery limiter: about +0.3 dB (c32 0.9).

## 2. Violins II plays 4-8 dB under Violins I at the same printed mf-ff, including where both play the theme in octaves or unison: bars 59-62 and 76-77 (measured; partly a mix-table mismatch)

**Evidence (measured).**
- **Median note bodies, Violins II minus Violins I, by printed dynamic.** p -1.1, mp -2.0, **mf -4.2, f -5.1, ff -4.5**.
- **Bars 59-60 (qn 196-200), theme in octaves at f, same CC11 88 and CC1 90.**
  - Violins II bodies -32.8 / -37.7 / -34.5 / -34.2.
  - Violins I -26.1 / -29.2 / -27.6 / -27.5.
  - That is 6-8 dB under. Violins II ranks 7th-10th of the stems there.
- **Bars 61-62 (204-212, ff).** Violins II -23..-27.5 against Violins I -18..-22.
- **Bars 76-77 (250-258, mp <, theme in unison).** Violins II -37..-41 against Violins I -33..-35, ranked 4th-10th.
- **The tables behind it** (`build/mix.json`):
  - Violins I `dyn_trim_db {"f": -1.5, "ff": 1.5}`; Violins II `{"f": -2.5, "ff": -1.5}`. That is 1 dB apart at f and 3 dB at ff.
  - `build/roles.json` gives Violins I `[188, 204, 2]` (bars 57-60) and Violins II nothing there.
  - The rest of the gap is the samples: the lower octave, and the same pitch on a different section patch.
- **Comparisons.** In the soft bars 23-30 the two sections are level (-35.1 / -35.3 at qn 66). With 16 against 14 players the expected difference is under 1 dB (inferred).

**Why it matters (inferred).** In bars 59-60 the lower octave of the tune is nearly gone. The theme group (Violins I+II, Flute 1, Oboe 1) measures only level with the counter-line (Horn 1, celli, bassoon) at 196-203: theme minus rest -0.1..-0.8 dB. So the run into the climax sounds top-thin, carried by Violins I alone.

**Fix.**
- `build/mix.json` Violins II: `dyn_trim_db {"f": -0.5, "ff": 0.5}` (+2 dB at f and ff, nothing at p).
- `build/roles.json` Violins II:
  - add `[188, 204, 2, 0.5]` (the same span as Violins I).
  - add `[249.9, 258.5, 2.5, 0.5]`, which joins the f arrival at 259 under the new dyn trim.
- Simulated:
  - Violins II bar 59 -29.8 (Violins I -27.0). Bar 61 about -22..-23 (Violins I -20.8). Bar 77 -35.8 (Violins I -31.8).
  - Master: bar 59 +0.3, bar 60 +0.5, bars 61-62 about +0.3-0.4, bars 76-78 +0.1-0.3. Bars 79-80 -0.06..+0.09 (Violins II is f-ff there too, but the role spans do not reach it). The climax order holds.
- Level only.

## 3. Bass clarinet solo, bar 31 (qn 91-93): the first two notes are buried under the pp pedal and the third note jumps 9 dB at the same CC11 and envelope (measured)

**Where.** "solo, espr." p, a slurred rising arpeggio E flat 2 - F2 - A flat 2 - C3 (91-92.5) into the crescendo on E flat 3 (93). The accompaniment is Bassoon 2 and contrabassoon on a pp A flat pedal.

**Evidence (measured).**
- **Note bodies.** 91 E flat 2 -45.2, 91.5 F2 -42.9, **92 A flat 2 -33.8**, 92.5 C3 -36.8, 93 (start of the crescendo) -35.1.
- **Controls.** CC11 54 on all four notes; vol +0.5, +0.5, +1.3, +2.5.
- **The pedal.** Bassoon 2 measures -44.2 (0.5 qn frames: 91.0 BCl -45.3 against Bassoon 2 -44.0). So the solo's first beat is level with or under the pp pedal, and the line starts audibly only at the A flat 2.
- **The A flat 2 is this patch's hot pitch.** Series 1 c28 and the roles `[9,13,-7]`, `[13,14,-5]` (bars 4-5) and `[102,105,-5]` (bar 35) already cut it. The bar 31 occurrence has no cut, and the v600 port removed the three old bar 32 rows when the solo moved down an octave (`build/score_config.py` comment above JOIN_NOTCH).

**Fix.**
- `build/note_trims.json` Bass clarinet: `"91": 6, "91.5": 4.5, "92": -4, "92.5": -1.5`. Note trims use the 0.1 s ramp.
- Result (arithmetic): -39.2 / -38.4 / -37.8 / -38.3, then the crescendo from -35.1. That is an even rising line 5-6 dB over the pedal.
- Optional, secondary: the crescendo peaks at -28.7 (95.5-96, printed mf). That is 1-2 dB over the cor anglais's p/mp solo peaks (-29.6..-31.2 p90) and makes bar 32 (-33.0) as loud as the A section's tutti bars 23-25.
  - If the actor wants it lower: `[94.5, 97.5, -2, 1]`. It ramps in late in the crescendo, so the crescendo still grows about 4.5 dB.
- Level only.

## 4. Bars 76-77 (qn 253-258): Bassoon 1's mp counter-line is the loudest stem, over the theme (measured)

**Where.** The theme is in Violins I and II in unison, mp <. The counter-line is Bassoon 1 (mp at 253), the celli (mp) and Horn 2 (p), all in unison.

**Evidence (measured, 1 qn means).**
- Bassoon 1 at 254/255/256: -34.3 / -33.0 / -32.9. It is the top stem at 255 and 256.
- Violins I at the same points: -28.7 / -35.0 / -33.1. Violins II -37.5 / -37.1 / -38.8.
- So the theme pair is level with the single bassoon at 255-256.
- **Rimsky-Korsakov at piano:** one string section = one woodwind, so the two violin sections should be about 3 dB over the bassoon even at equal dynamics.
- **Why the bassoon is hot.**
  - Bassoon 1's median mp body is -35.4, the hottest of the single winds at mp (wind median -36.8).
  - Its `soft_trim_db` p +5.5 tapers toward the f anchor, so most of it still applies at mp (kit LEARNINGS §4: "a p +5 adds +3.6 dB at mp").

**Fix.**
- `build/roles.json` Bassoon 1: add `[252.9, 258, -3, 0.5]`. It ends on Bassoon 1's 258 mf onset.
- With finding 2's Violins II role: Bassoon 1 -36.9 at 253-257, and the violin pair about -30.5. The theme leads by about 5 dB. The counter-line keeps the celli (-33..-35) and Horn 2.
- Generic alternative: give Bassoon 1 an `mp` soft trim of +2 so the p trim stops leaking into mp. Check bars 45-47 and 53-56 after that.

## 5. Bars 23-24 (qn 66-69): the celli's cantabile counter-melody enters under the double basses' p bass line (measured)

**Where.** The violins have the theme, mp. Celli: "unis., cantabile, sul D", p. Basses: p, playing bars 23-28 an octave higher in v600.

**Evidence (measured, 1 qn means).**
- **66/67/68.** Celli -41.8 / -41.7 / -40.0. Basses -41.3 / -39.1 / -38.2.
- The basses are the third stem and the celli the fourth to sixth. In 100-300 Hz the celli lead by only 1.7-3.3 dB in bars 22-23.
- **Celli against each violin section across 66-78.** -6.7 / -6.7 / -7.3 at 66-68, then -1.3..-4.8. So the counter-melody's entry is the weakest point of the line.
- **Tables.**
  - Celli: roles `[66, 78, -1]` and `[72, 77, -2, 0.5]`, and note trim `"72": -3`.
  - Basses: roles `[66, 90, -1]`, plus soft trim p +6.5 and gain -8.

**Fix.**
- `build/roles.json`:
  - Violoncellos: add `[65.8, 72, 2, 0.5]`. This is +1 net with the -1 already there. It releases into c32's 72-77 role, so nothing steps.
  - Double basses: add `[65.8, 72, -3, 0.5]`.
- Simulated:
  - Celli 66-68 about -39.8..-38.0, 2-5 dB over the basses, which drop to about -42..-44.
  - Celli 4-5 dB under each violin section at the entry, close to the -4 dB average for the rest of the phrase.
  - Master change under 0.3 dB.
- Level only.

## 6. The final ppp chord (qn 298-304) is bottom-heavy: the celli's A flat 2 is the loudest stem, and the divided violas sit 6-8 dB under it (measured levels; the target is inferred)

**Evidence (measured, 1 qn means, 301-303).**
- Violoncellos -52.9 / -52.0 / -55.0.
- Violins I (C5, the pitch movement I ended on) -53.6 / -54.6 / -56.6.
- Clarinet 2 -53.6 / -53.4 / -55.8. Violins II -55.9..-58.2.
- Violas -59.2 / -59.4 / -63.2. Violas div -61.6 / -60.9 / -62.0.
- The power sum of the violas is about -57.2, still 4 dB under the celli.
- Through bars 87-91 the violas are 5-9 dB under the celli and 2-5 dB under Violins II at the same printed pp.
- **The vol_db behind it.**
  - Violas div runs at -9..-14.6 dB from 283 on, from stacked roles: `[278.5,286,-5]`, `[286,304,-4]`, `[289,304,-2]`, `[292.5,304,-3.5]`, `[282.25,291.5,-2,0.5]` and `[286,292,-1]`, against `+4`/`+7` at 292-304.
  - Violas run at -3..-10 dB.
- c28's B #5 balanced the two viola halves against each other, and they are level (within 1-3 dB). Nobody balanced the pair against the other sections.

**Why it matters (inferred).** In a ppp final chord the root and fifth in the violas carry the tuning colour. Here the chord reads as low celli plus the high violin C, with a hollow middle.

**Fix.**
- `build/roles.json`:
  - Violas and Violas div: add `[297.9, 304, 2.5, 1]`.
  - Violoncellos: add `[297.9, 304, -2, 1]`. Both ramp across the printed decrescendo at 298, so there is no step under the chord.
- Expected: violas sum about -54.7, celli about -55.
- Low priority. Check the c28/c29 re-bow fits on these pieces afterwards (`fit_rebows.py --stems`): the change is level only, but the fitted re-bow shapes sit on these notes.

## Checks asked for in this lens

All measured unless marked inferred.

**Solos over their accompaniment.** Each entry gives the 1 qn margin over the accompaniment sum (median and minimum), then over the loudest single stem.
- Horn 1, bars 7-14: +1.8 (min -0.6). Over the loudest stem +5.5 (min +3.1).
- Oboe 1, bars 15-16: +5.0 / +7.2.
- Solo violin, bars 17-18: +5.5 / +8.7.
- Oboe 1, bars 19-20: +4.2 (54 entry -2.3 under the celli).
- Solo violin, bars 21-22: +1.4 (64 -2.4, the phrase-end decay against the celli div crescendo; 0.5 qn frames keep it first).
- Bass clarinet, bars 31-36: +7.4 (91 -2.1, finding 3).
- Flute 1, bars 37-40: +3.7 / +8.5.
- Cor anglais, bars 41-44: +4.2 / +8.1.
- Oboe 1, bars 45-47: +2.3 / +7.0.
- Cor anglais, bars 47-50: +4.2 / +6.0.
- Clarinet 1, coda: +3.1 (286 -2.0, the cor anglais's "dolce" entry in duet).

**Dynamic mapping (median note bodies).**
- At pp every family lies within -45..-47: winds -42.6..-47.6, Horns 3/4 -48.7/-46.8, strings -45.3..-46.8, harp -47.2, timpani -46.9.
  - Two exceptions: the basses at -49.8 (inferred acceptable: K-weighting discounts their range, and the 100-300 Hz band is level with the celli), and finding 6.
- At ff: string sections -22.7..-27.8, single winds -26.2..-30.2. That is the forte ratio (one section about 3 dB over one wind).
- Inconsistencies: Violins II at mf-ff (finding 2), Bassoon 1 at mp (finding 4), and the horns at ff (finding 1).
- Clarinets 1/2 measure p ≈ pp (-43.0 against -42.6). This comes from the coda solo trims at pp, not from wrong anchors.

**Divisi and soli tracks.**
- Violins II div against Violins II at pp: -45.9 / -45.3. c32's role change worked.
- Violoncellos div against the celli at pp: -47.1 / -45.8.
- Violas div against the violas: level within 1-3 dB in bars 23-28, 80-81 and the coda.
- 4 soli: basses 220-238 at -47.3 + (-3) as planned. Coda basses at 286-291 -56 against the tutti celli -45..-50.

**Climaxes.**
- Bars 61-62 against 79-80: master -16.0/-16.1 against -18.4/-19.0 (metrics). The order holds.
- Timpani at bars 61-62: the f stroke at 203 is 6 dB under the top. The roll at 204-211 is 12-17 dB under, ranked 20th-22nd. At bars 79-81 it is 6-10 dB under, ranked 11th-20th.
- Low brass at f: 1-4 dB under Violins I in K-weighted level, 13-17 dB under in 2-5 kHz. They are not covering.
- Bars 63-64: Trombone 1's ff quotation leads by 13-20 dB over the sf > p string tremolos. That is as printed.

**Bass.** The 20-100 Hz share against the K-weighted total runs -13..-26 dB by section (the coda is heaviest at -14). The 100-300 Hz share runs -4..-10. No boom. Bars 23-24 are covered in finding 5.

**Repeatability.** Unchanged tracks are bit-identical between c31 and c32 (manual table above).

**S3 scan.** I looked for vol_db falls of 3 dB or more within 0.12 s under a sounding note. There are 9:
- the timpani's roll cut 171.94 (into the 172 stroke, which covers it);
- Flute 1 111.5;
- Oboe 1 190.0;
- Bassoon 1 146.1;
- Violins II 242.95;
- Violas 87.0 and 297.16;
- the Violin I solo 52.95;
- Violoncellos div 62.25.

All are 3-4 dB except the timpani. None is a balance problem, but the actor should not add more of them. Every fix above uses ramps of 0.25 qn or longer, or ends on an onset.

**Do not touch:**
- The climax order and the low-brass and timpani levels at bars 61-64 and 79-82.
- Trombone 1's quotation levels and accents, and Flute 1's CC7 cut at 211.96-213.
- The bar 63 CC7 lanes and the niente CC7 lanes.
- The c32 solo levels: Oboe 1, the Violin I solo with CC1 72 and gain +0.4, Flute 1, the cor anglais, and Clarinet 1's coda.
- The c32 Violins II div level and the 4-soli -3 dB roles.
- The horn CC1 map (soft 57-72) and the soft-horn loud_eq.
- The Cb EQ set.
- The bass clarinet's `[188,204,-5,4]` role.
- Horn 1 bars 54-60 (c32 B #2: now level with or over Bassoon 2; the celli lead it only where they print mf against the horn's mp).
- Unison handling (Horn 3 carries the Horns 3+4 unison at +3 dB).
