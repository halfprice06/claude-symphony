# Critic B, cycle 2: balance and levels (render c01)

Method. Levels are K-weighted (BS.1770 filter, LUFS-style dB) unless marked RMS. metrics.md uses plain RMS, which counts the celli and basses a few dB higher than a listener hears them, so every balance judgement below was rechecked with K-weighting. Per-note levels: each note from onset+80 ms to min(end, onset+1.5 s), paired with the track's actual CC11 at the onset. I fitted level against CC11 for each track. Per-bar and per-beat levels come from the stems. Scripts and data: `/private/tmp/claude-501/mockup-loop/c02-B/` (`an.py` per-note levels, `fit.py` dB-per-CC fit, `trim.py` targets, `kbars.py` K-weighted bar levels, `seg.py` per-beat levels, `swellw.py`/`swell.py` level growth inside notes, `low.py`/`bspec.py` low-end spectra).

What works (measured): at p (CC46) every track lands within -46 to -52, so families match at p, as Rimsky-Korsakov says they should (all winds equal in piano; a string section equals one wind). The horn solo in bars 7-14 leads harp and bass clarinet by 3-8 dB. Bars 53-56 are balanced. The f/ff timpani rolls sit 4-6 dB under the strings.

Fitted per-note level against CC11 (measured):

| track | dB per CC | at p (46) | at f (88) | at ff (104) |
|---|---|---|---|---|
| Flute 1 | 0.364 | -47.8 | -32.5 | -26.7 |
| Oboe 1 | 0.175 | -47.0 | -39.7 | -36.9 |
| Clarinet 1 | 0.237 | -47.6 | -37.7 | -33.9 |
| Bassoon 2 | 0.240 | -52.0 | -41.9 | -38.0 |
| Horn 1 | 0.264 | -49.5 | -38.4 | -34.2 |
| Trombone 1 | 0.173 | -45.1 | -37.8 | -35.1 |
| Bass trombone | 0.241 | -51.7 | -41.6 | -37.8 |
| Violins I | 0.300 | -48.0 | -35.4 | -30.6 |
| Violins II | 0.317 | -47.4 | -34.1 | -29.0 |
| Violoncellos | 0.358 | -49.0 | -33.9 | -28.2 |
| Double basses | 0.236 | -49.4 | -39.5 | -35.7 |

## 1. The celli counter-line covers the violin melody in three passages (measured)

Where: bars 23-28, 57-60 and 75-80 (Violoncellos against Violins I/II, and against Flute 1 in 57-60 and 75-77).

What: in each passage the violins carry the tune and the celli play a slower counter-line at the same printed dynamic or one level lower. The celli measure 5-10 dB above the tune.
- Bar 27: Vc -36, Vln I -42, Vln II -43. Bar 28: Vc -32, Vln -43/-41. Printed: Vln mp-mf, Vc p cresc.
- Bar 57: Vc -32, Vln I -39, Vln II -38, Fl -42, Ob -39. All of them are printed p cresc.
- Bar 58: Vc -28, Vln II -35, Fl -33.
- Bar 75: Vc -33, Vln I -38, Vln II -41, Fl -43. Printed: Vc mp, Vln mp, Fl p.
- Bar 80: Vc -27 against Vln I/II -29. The celli are printed f inside a ff tutti.

Causes (measured from parts.json):
- (a) The +8 CC11 solo boost fires on "cantabile" and "espr." and lasts until the next text on the staff. The celli's "unis., cantabile" at qn 66 runs to qn 108. "espr." at qn 190 runs to 204. "cantabile" at qn 238 runs to qn 274. That boosts the whole counter-line in all three passages, for example Vc 81/89 against Vln 81/81 in bar 58 and Vc 60/68 against Vln II 60/60 in bar 75.
- (b) The celli patch rises 0.358 dB per CC, the steepest of all strings (see table and finding 2).
- (c) Nothing makes an accompanying line sit under a melody at the same printed dynamic. Adler and Rimsky-Korsakov both expect the player to do this.

Fix:
- `tools/score_to_parts.py`, solo-boost block (`boost_spans`): keep SOLO_BOOST = 8 only for texts that contain "solo" (excluding "tutti").
- For "espr.", "cantabile" and "dolce" without "solo", use +3. The boost ends at the first of: the next printed dynamic, the end of the next hairpin, or a rest of 1 qn or more.
- Add `build/roles.json`, holding `{track: [[qn_start, qn_end, dB], ...]}` spans that `score_to_parts.py` (or `build_reaper.py`) turns into a level offset by the same mechanism as finding 2:
  - Violoncellos: [66, 90, -3], [188, 204, -3], [238, 274, -3].
  - Harp: [124, 140, -3]. In bars 41-43 the p harp chords measure -43 to -47, as loud as the cor anglais solo (-43 to -46) and Flute 1 (-46.5).
- Target for the next render: celli 2-4 dB under the louder violin section in bars 27-28, 57-59 and 75-77, and harp 3 dB under the cor anglais in 41-43.

## 2. The same CC11 step gives 0.17 to 0.36 dB per CC, so the balance drifts as the music gets louder (measured; targets from Rimsky-Korsakov)

Where: every forte passage, mainly 57-63 and 75-81.

What: from the p levels, which match, the tracks spread out as CC11 rises (table above):
- At ff the single Flute 1 measures -26.7, about 10 dB over the oboe (-36.9) and level with or above the first violins. In bar 79 the flute is the loudest stem in the mix (-26 against Vln I -29).
- The celli (-28.2) are 5-8 dB over the oboe, clarinet and bassoons.
- The trombones (-35.1, bass trombone -37.8) are under the violins (-30.6) and only level with a single clarinet.

Rimsky-Korsakov, Principles, "Comparison of resonance" (reference-books/text/rimsky-principles.txt, lines 1961-1990 and 1508-1515), gives the forte balance as 1 trombone = 2 horns, 1 horn = 2 woodwinds, 1 string section = 2 woodwinds, and in piano everything equal. In dB that is roughly horn and string section +3 over one woodwind, trombone and tuba +6, at f and ff. Take the median single woodwind (Ob, CA, Cl, BCl, Bn) as W: -40.1 at f and -36.6 at ff. The trim each track needs (`trim.py`):

| track | trim at f (88) dB | trim at ff (104) dB |
|---|---|---|
| Flute 1 | -5 | -7 (leaves the flute about +1 over W for its high register) |
| Clarinet 1, Bass clarinet | -2.5 | -3 |
| Bassoon 2, Contrabassoon | +1.5 | +2 |
| Horn 2, Horn 4 | +1 | +2 |
| Trombone 1 | +2 | +4 |
| Bass trombone, Trombone 2 | +5 | +6 |
| Violins I | -2.5 | -3 |
| Violins II | -3.5 | -4.5 |
| Violas | -0.5 | -1 |
| Violoncellos | -4 | -5.5 |
| Double basses | +1 | +1 |
| others | 0 | 0 |

Fix:
- Add a `dyn_trim_db: {"f": x, "ff": y}` entry per track in `build/mix.json`. The trim is 0 dB at CC46 and below, rises linearly to x at CC88, and to y at CC104 and above. It is computed from the printed `dyn_curve`, not from cc11, so accents and boosts do not move it.
- Apply it as a level control that does not change timbre, so CC11 keeps choosing the dynamic layer. Preferred: a track volume envelope written by `build_reaper.py`, which is exact in dB and rebuildable from the config.
- Alternative: a CC7 lane from `score_to_parts.py`. The Opus manual (EW-Opus-Software-Manual.txt, lines 583 and 973) says CC7 is global Volume. Its curve is not documented. The timpani data suggest it is shallower than 40·log10 at low values (inferred). So if CC7 is used, start every track at CC7 100 with D_VOL compensation, then calibrate against a measurement.
- Check after the render: re-run the fit. Every wind and string track should fall within 0.24-0.28 dB/CC, brass within 0.28-0.32, and the p column should stay where it is.

## 3. The timpani ppp rolls cover the horn solo in bars 69-70 and are the loudest stem at the end; the pp strokes in bars 84-85 cannot be heard (measured)

Where: bars 67-70, 89-92 (ppp rolls) and 84-85 (pp strokes, qn 277-279).

What:
- The ppp rolls measure -45 to -47 in every bar. In bars 69-70 the roll (-46.0, -46.6) is louder than the "1. solo" horn it accompanies (-47.5, -50.1, printed mp dim. to pp).
- In bars 89-92 the roll is -45.6, -46.2, -46.2, -46.2, against Vln II -49 to -53 and Vla -53 to -57. In bar 92 it is the loudest stem (Vln I -47.7).
- The "settle" (CC7 16 to 13) moves the level by only about 0.6 dB, not the 4 dB intended. BRIEF rule 5: a roll starts at its dynamic and then settles under the texture.
- The pp strokes at qn 277, 278.5 and 279 (CC7 54, velocity 56) measure -53.8, -62.7 and -60.5, under the ppp strings (-51 to -53). The p strokes at qn 172 and 271 (CC7 71, velocity 64) measure -47.0 and -44.5. The 8-16 dB step comes mostly from the velocity layer between 56 and 64 (inferred; it matches c01-B's finding of a step in this region).

Fix:
- `build/mix.json`: Timpani `gain_db` -6 → -10, an exact dB cut.
- `score_to_parts.py`, timp block: `roll_db` gets +4 on mf, f and ff only (mf -17, f -16, ff -14), so the tutti rolls keep their level. ppp and pp stay at -36 and -31, so they drop 4 dB net.
- Roll settle: -8 dB (table units) over 3 qn instead of 4 over 2. The measured result must be at least 3 dB.
- Strokes: minimum velocity 64 for pp and p. For pp strokes, use the roll level + 20 instead of + 16.
- Targets: ppp rolls at -50 to -52 and at least 3 dB under the horn in 69-70. The pp strokes at qn 277-279 between -48 and -51, so they are just audible over the ppp strings.

## 4. Bar 63: the strings hold ff for most of a beat after their sf and cover the ff marcato trombone solo (measured)

Where: bar 63, qn 212-216. The strings are printed sf with a hairpin to p at bar 64. Trombone 1 is "1. marcato ff" from qn 212.5.

What, per beat: Vln II -28.2/-24.3/-29.9, Vc -26.7/-25.6/-36.4, Vln I -26.9/-27.9/-32.9, against Trombone 1 -46.4 (before its entry)/-32.5/-32.7. For the first two beats of its solo the trombone is 5-8 dB under the strings. It only leads once the strings have faded (qn 216 on: Tbn -31.7 against strings -44 to -48).

Cause: in `base_points()`, an sf restores the previous level (ff, 104) after 0.75 qn. The hairpin from qn 212 is sorted before the restore point, so the curve holds 104 until 212.75 and only then ramps to p. The decrescendo is played as ff held, then a diminuendo.

Fix:
- `base_points()`: when a decresc hairpin starts within 0.25 qn of an sf/sfz, make the post-spike level `min(previous level, DYN["mf"])` (72), reached at q+0.5. The hairpin then starts from that level, not from the old one.
- With finding 2's Trombone 1 trim (+4 at ff), the trombone should lead the strings by 4-6 dB from qn 213.

## 5. Long solo-wind notes swell by 8-17 dB at constant CC11, against printed p and diminuendi (measured; cause inferred)

Where:
- Oboe 1 F5 at qn 45 (bar 16, first oboe solo) and qn 190 (bar 58).
- Cor anglais A4 at qn 152-155.5 (bar 48, "solo, espr." p).
- Flute 1 B flat 6 at qn 254 (bar 77).

What, per half beat:
- Cor anglais in bar 48: -49, -44, -37, -33, -35, -32, -32 at constant CC11 54 and CC1 66. A held p note becomes the loudest thing in the bar, 17 dB over the strings (-49 to -56) and louder than the cor anglais's own ff-equivalent.
- Oboe at qn 45: rises from -40 to -31.8 while CC11 falls from 60 to 53 under a printed decrescendo. Bar 16 measures -36 against pp strings at -52. At qn 190: rises to -33.7.
- Per-note residuals against the CC fit: Oboe F5 +9.8 and +9.2, cor anglais A4 +8.2 and +6.2, Flute B flat 6 +10.2 and +7.3. No other wind note is more than 6 dB off.
- Inferred cause: these are the vibrato sustain layers of the MAX legato patches (CC1 at 64-68 sits in the vibrato crossfade; HO manual 2.1.3), whose recorded notes bloom.

Fix:
- Add `build/note_trims.json`: `{"Oboe 1": {"77": -7}, "Cor anglais": {"69": -8}, "Flute 1": {"94": -4}}`. `score_to_parts.py` applies each entry as a level dip through the same mechanism as finding 2, ramped from 0 dB at the onset to the full trim at onset + 0.6 s and held to the note end.
- A trial worth one render: CC1 at 45 for wind notes longer than 2 s at p or softer, to test whether the lighter vibrato layer removes the swell.
- Check after the render: no wind note more than +5 dB over its CC prediction.

## 6. Soft sustained string chords swell 6-9 dB inside each note, so the accompaniment pulses (measured; cause inferred)

Where: mostly pp/p unslurred Sus MAX chords in Violas, Violins II and Violoncellos, for example bars 49-51 (qn 156-164), bars 1-3 and bar 85 onward. 61 string notes of 2 s or longer rise more than 6 dB after the first 0.6 s with CC11 moving 4 or less (`swell.py`).

What: at constant CC11 34, Violas measure -56 at each onset, -47 a beat later, then -54 at the next note (qn 156-160). Vln II and Vc follow the same pattern. Each new chord dips and then blooms, so a pp accompaniment that should be level pulses at the harmonic rhythm. Inferred cause: the slow pp attack and bloom of the Sus MAX samples, re-triggered on every unslurred chord.

Fix:
- `score_to_parts.py`: for string notes in Sus MAX at p or softer, with no rest before them (the previous note ends within 0.05 qn), add a CC11 contour of +6 at the onset falling to -2 by 1 qn, then back to the base level by note end. This counteracts the bloom without changing the printed level. Apply it to accompaniment only, not to slurred legato lines.
- The bow-change legato (Leg BC) that cycle 1 deferred would solve the same problem for connected lines, if it is available.
- Target: a level range inside each note of 4 dB or less for these chords.

Do not touch: the matched p levels across all families (every track -46 to -52 at CC46); the hairpin parser and level holds; the horn solo lead in bars 7-14; the f/ff timpani rolls 4-6 dB under the strings in tuttis; the Harp harmonics level (-47 to -48 against strings at -50 to -58); the one-hall reverb and mic scheme. When adding the trims in findings 1, 2 and 5, keep CC11 as the dynamic-layer control and make the corrections with volume (envelope or CC7) only, so the timbre of each printed dynamic is kept.
