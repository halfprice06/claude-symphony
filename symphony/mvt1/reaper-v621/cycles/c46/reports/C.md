# Critic C, cycle 46: dynamics over time (render c45, score v621)

Render under review: c45 (`cycles/c45/render`, master = float sum of 40 stems; `cycles/c45/mvt1-mockup-c45.mp3`; `cycles/c45/rendered_build/parts.json` and `mix.json`). Comparison renders: c43 (the last render with the old hall) and c44. The tempo maps of c43 and c45 are identical, so every window below is the same score span in all three. Levels are stereo power unless marked K (ffmpeg ebur128 momentary M or short-term S at 10 Hz). Arrival steps use M energy over the windows named. References: the Dvořák 9/i MP3 (decoded, same scripts) and the stored loudness series and metrics of Brahms 1/i, 4/i, 1/ii, 4/ii (`symphony/render/critics/c00|c04/ref_*/`). Simulations apply a gain to the c45 master (exact for `_all` level shapes, which act after the hall on every stem) or to single stems, then run an unchanged copy of `tools/deliver_master.py` with the c45 parts.json. Score pages 4, 7, 8, 11, 12, 14, 16, 17 and 18 were rendered and read. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c46-C/` and are deleted.

## Manual notes (second reading of the c40 slot C row: PDF pp. 68-71, read in full; also p.142 and p.125 for findings 1 and 4; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items in this lens first.

| Manual (PDF page) | What it says | Where it applies here | Followed now? |
|---|---|---|---|
| p.123, p.125 (MANUAL-GAPS #12, open) | Felt Cresc (KS E0): live-recorded crescendo rolls ending in a strong stroke, three lengths on three key ranges (EW C1-A2, C3-A4, C5-A6 = MIDI 36-57, 60-81, 84-105), two velocity layers; "the most realism" | c40 said the only candidate (bar 159) runs into a roll, not a stroke. That missed two: the mf < roll at 456-460 into the f stroke at bar 116, and the f < roll at 556-560 into the accented ff stroke at bar 141 (1.8-1.9 s each) | Not tried. Both rolls barely grow now (+1.8, +0.2 dB). Finding 4 (measured problem, inferred gain). |
| p.109 (MANUAL-GAPS #5, open) | Sus Exp / Leg Slur Exp: slower attack, growing vibrato | espr. wind swells (c42 C #2 cor anglais) | Not tried; no new evidence this cycle. |
| p.142 (read for finding 1) | Envelope RELEASE "determines how long the sound remains audible after a note is released"; the instruments are programmed "to achieve a natural result, so please be careful when changing them" | c44's 150 ms Sus MAX / Sus Marc LITE release cap on the strings at all dynamics; the patches ship 524-931 ms at p-pp (mix.json `_c44` note) | Not followed at pp/p: soft string releases now fall faster than loud ones. Finding 1 (measured). |
| p.68 | Harp mic set: Vintage Close and Vintage Mid replace Surround and Vintage Surround | Harp group: Close 0.6, Main 1.0, send 0.3, width 0.3 | Still followed. Nothing calls for the Vintage mics. |
| p.68-69 | Angels / Maestro choose the articulation by velocity zone; MOD patches by CC1 | Harp plays `Harp Sus RR` | Still the right choice (Maestro has no samples under MIDI 48). |
| p.69 | Sustain RR: Pluck Long (RRx1) and Thumb Pick (RRx2) alternate by round robin at velocity 1-123, 5 dynamic layers each; 124-127 is a Nail Pick; CC11 and velocity set loudness | All 184 harp notes | Still not followed (c40 C #4, deferred in c41). Measured in c45 parts.json against the read splits (Thumb p 1-42 / mp 43-70 / mf 71-97; Pluck p 1-57 / mp 58-85 / mf 86-107): printed p, 66 notes, v52-110, none can reach Thumb p (56 Thumb mp, 9 Thumb mf); printed mp, 72 notes, 46 would play Thumb mf; the ppp final chord (v46) plays Thumb mp. The level order holds: 10 ms peaks ppp -46.0, p -41.0, mp -37.9, mf -31.0, f -25.3 dB (c43 within 0.5 dB). Finding 5. |
| p.70 (new note) | Gliss Technique notes "can also be played normally, producing a softer articulation than normal notes" (3 levels) | The p arpeggios of bars 56-63 and 163-166 | Not used. An alternative to finding 5's velocity remap if the Thumb p layer is still too hard (inferred). |
| p.70 | Single-articulation patches (Pluck, Thumb, Près de la table, Harmonics, Nail Pick, Double Hit, Bisbigliando) | The part has 15 arpeggios, 9 étouffez marks, none of these techniques | Nothing printed needs them. |
| p.71 | Repetition Rep; FX and Gliss | One repeat (259-260); no glissandi | Not needed. |
| DIGEST §10 (patch facts) | Sus RR decays to 0.001 over 5990 ms, release 3019 ms; c35 set `env_sustain` 1.0 and `env_release_ms` 200 | Arpeggios under the melody, the final ppp chord | Still followed. Bars 47-55: harp minus the louder of celli / Horn 1 per beat, median -6.7 dB, p90 -2.0 (c40: -6.5 / -0.7). The final chord's first 2 s is -55.2 dB, 8.9 dB under the master (c40 -54.7 / 8.5). |

## State through this lens: what the drier room did (c43 -> c45, measured)

- **Loudness arc.** Per bar, K level against the bar's loudest printed dynamic: master r 0.836 -> 0.838, slope 4.21 -> 4.28 dB per step; mp3 r 0.791 -> 0.793, slope 2.64 -> 2.71. The master fell a median 0.5-0.7 dB in every loudness band (bars under -36 dB -0.67, louder than -20 dB -0.54); the mp3 is unchanged (median -0.2 to 0.0). The bars that changed most: bar 84 -6.4 dB (the bar-83 chord's hall tail no longer fills the beat of rest before the sub. p), bars 1-4 -1.4 to -3.8 (finding 3), and soft bars where the old hall carried a tutti's tail or a held pp chord (73, 76, 86, 144) -2.0 to -2.3.
- **Crescendos still build.** Master growth from the first to the last two beats, c43 -> c45: bars 10-12 +8.9 -> +9.4; 23-26 +12.0 -> +11.6; 37-41 +5.8 -> +5.4; 59-61 +9.0 -> +9.0; 78-83 +10.8 -> +10.9; 89-102 +15.2 -> +15.2; 109-116 +21.6 -> +21.6; 117-122 +3.8 -> +4.1; 127-131 +15.3 -> +15.5; 155-160 +25.9 -> +26.1; 166-167 +15.1 -> +14.8. The mp3 moves the same way, within 0.3 dB. The dips inside each beat (50 ms p10 minus the beat's energy) deepened only 0.1-0.4 dB. On the stems, hairpins by family (last third minus first third) are within 0.4 dB of c43: crescendos strings +4.4, winds +5.4, brass +4.3, timpani +6.1; decrescendos -5.6 / -5.7 / -6.4 / -5.4; wrong way 0-11%. The hall was not carrying the crescendos.
- **Climaxes.** Arrival steps (M, 0.5 s after minus 0.9 s before) are within 0.4 dB of c43 at every tutti arrival, except bar 41 (+5.0 -> +4.0, from c45 B #4's celli body cut). The two fff downbeats are still the weak ones (finding 2). Delivered S max: 160 -11.5 > 122 -12.2 > 167-170 -13.5 > 26 -14.2, as in c43.
- **Diminuendos.** The long ones keep their shape: bars 122-127 fall -25.1 -> -26.6 dB, smoothly, with no beat falling more than 3.3 dB; bars 162-166 are within 1 dB of c43 per beat, and bars 42-46 within 2 dB (the whole span about 1 dB lower, same shape). The coda morendo (179-182) falls -10.7 dB against c43's -12.6, because c45's final-chord re-bow refinements raised the last beats by 0.2-1.1 dB. What changed is the release after each soft note-off (finding 1).
- **Soft body.** See finding 3. Elsewhere the soft passages lost 0.5-0.7 dB in the master, which the ride restores (mp3 median -0.2 dB in bars under -36 dB). c45 C's band ratios (soft 112-224 Hz relative to 224-2245 Hz, -8.1 against the Dvořák's -8.4) still apply.
- **Real recordings.** Delivered S distribution: p50-p10 7.2 dB, max-p75 7.1 dB (references 5.9-11.1 and 4.4-7.5); unchanged from c43. The median of the master's 12 largest loud arrivals is 3.8 dB (c43 3.9). References: Brahms 1/i 5.1, Brahms 4/i 5.6, Dvořák 5.2, Brahms 1/ii 4.2, Brahms 4/ii 3.4. The mockup's arrivals sit with the slow movements, not with the first movements.
- **loud_eq spans moved in c45 (coordinator check).** On the stems, the celli 170/125 Hz and basses 180 Hz loud bells add +2.5 to +2.8 dB at each new span start and take 1.5 to 4.4 dB away at each end (c45 minus c44, so other changes cancel). Two ends fall inside held notes: bar 72-73 (287.75-288, the celli's and basses' pp half note tied over the bar line: celli -4.4, basses -1.5 dB) and bar 33 (the basses' fp whole note 128-131.74 carries +2.8 dB to the bar-34 note change). The rest fall on note changes in the printed direction (41, 69, 98, 104, 136, 143). In the master every 0.1 s frame around both held-note ends is within 1 dB of c44: the tutti cut-off at 288 covers the first one, and at bar 33 the basses stay 13.4 dB under the master, 5 dB under the bassoon solo. width_by_mic is static and adds no steps. Finding 6 (optional).

## Findings, ranked by what a listener would gain

### 1. Soft endings now stop abruptly: the final ppp chord and the strings' soft phrase ends lose 10 dB in about 0.07 s after the note-off (measured; fix to be tested in pass 2)

**Where.** The last sound of the movement, qn 728 (all five string sections). Also every soft string phrase end before a rest: bar 4 (celli 15.96), bar 14 (the Lento's closing chord, 54.96), bar 55 (217.9), bar 76 (303.9), bar 146 (581.9), and others.

**What is wrong.** At pp and p the strings' release is now shorter than at f. Soft endings therefore cut off instead of dying away into the room. This happens where the score asks for the softest, most sustained endings: the morendo final chord marked attacca, and the chords that close the introduction and the exposition.

**Evidence (measured).**
- Master at the final note-off, relative to the 0.3 s before it (windows 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 / 0.3-0.5 / 0.5-0.8 s):
  - c43: -1.4 / -3.9 / -5.9 / -7.6 / -10.4 / -18.7;
  - c45: -5.6 / -11.4 / -14.6 / -17.8 / -23.8 / -29.8.
  - Time to -10 / -20 / -30 dB: c43 0.40 / 0.67 / 0.97 s; c44 0.07 / 0.33 / 0.51; c45 0.07 / 0.32 / 0.67.
- Per stem, time to -10 dB at that note-off, c43 -> c45: Violins I 0.45 -> 0.07, Violins II 0.13 -> 0.04, Violas 0.20 -> 0.06, celli 0.57 -> 0.09, basses 0.21 -> 0.06 s. In the same render and the same hall, the timpani roll (no cap) takes 0.18 s and Horn 3 (237 ms cap) 0.22 s. So the hall is not what cuts the strings; the cap is.
- Across 19 soft string phrase ends (ppp-p, track rests at least 1.5 qn after), median drop at 0.05-0.1 / 0.1-0.2 / 0.2-0.3 / 0.3-0.5 s:
  - c43: -1.7 / -3.9 / -9.2 / -15.7 dB;
  - c45: -9.5 / -16.6 / -23.5 / -27.8 dB.
  - The 8 loud string ends (f-fff) in c45 are slower: -6.4 / -10.8 / -11.9 / -19.8. Soft horn ends: -3.7 / -7.3 / -12.5 / -21.4.
  - Examples at 0.05-0.1 / 0.1-0.2 s: Violas bar 14 +2.4 / +0.2 -> -10.6 / -18.1; celli bar 4 +0.9 / +1.1 -> -10.5 / -19.1; Violins II bar 55 -0.4 / -3.8 -> -10.5 / -20.8; Violins II bar 146 -0.2 / -2.8 -> -13.4 / -20.4.
- References with soft endings (rtk final tails): Brahms 1/ii -10 dB at 0.40 s, -20 at 0.79; Brahms 4/ii 0.20 / 0.48. c43 (0.40 / 0.67) sat inside that range; c45 (0.07 / 0.32) is three to six times faster at -10 dB. The methods differ in their start point (rtk takes the last frame within 12 dB of the final maximum), so take this comparison as inferred.
- In the master, the final chord shows it most. The other soft ends are mostly covered by the next entry. At the close of the Lento (bar 14) the master's tail at 0.3-0.5 s is -22.5 dB against -12.1 in c43. That stop is largely the drier hall on Horn 1, which is not to be reopened, and the rtk detector gives it the movement's fastest decay (RT 0.86 s; Brahms 1/i 1.13-1.62).
- Cause (read): c44 C #1 set `sus_release_cap_ms` {"ms": 150, "dyn": ["pp", "p", "mf", "f", "ff"], "rows": ["Sus MAX", "Sus Marc LITE"]} on all five string tracks and the f62 aliases. The patches ship 524-931 ms at p-pp and 323-524 ms at mf-ff, so the cap removed far more of the soft samples' release. c45's Violas `rt_gain_db` -6 adds to it on the violas. c44 -> c45 changed nothing at the final note-off.

**Fix.**
1. `tools/build_reaper.py`, where `apply_mix()` calls `cap_release` (`if m_.get("sus_release_cap_ms") is not None:`): accept a list of specs:
   ```python
   caps_ = m_["sus_release_cap_ms"]
   for spec_ in (caps_ if isinstance(caps_, list) else [caps_]):
       cap_release(inst, spec_, tr["name"])
   ```
   Key `_CAP_PRINTED` by `(name, spec["ms"])` so that both lines are printed.
2. `build/mix.json`, Violins I, Violins II, Violas, Violoncellos, Double basses, Violins I f62, Violins II f62:
   `"sus_release_cap_ms": [{"ms": 150, "dyn": ["mf", "f", "ff"], "rows": ["Sus MAX", "Sus Marc LITE"]}, {"ms": 350, "dyn": ["pp", "p"], "rows": ["Sus MAX", "Sus Marc LITE"]}]`.
   The 150 ms at mf-ff keeps what c44 C #1 gained: tutti cut-offs and the viola figures.
3. Test first in pass 2, as c45 tested `rt_gain_db`. Two `TEST_TRACKS` aliases at 350 ms:
   - "Vla softcap test" (Violas, windows 50-56, 214-220, 578-584, 710-728);
   - "Vc softcap test" (Violoncellos, windows 12-17, 296-305, 574-584, 710-728).
   If 350 ms fails the test, make a second pair at 500 ms.
4. Pass criteria:
   - on the test stems, the final note-off reaches -10 dB at 0.15 s or later;
   - on the test stems, the soft ends' median drop at 0.05-0.1 s lies between -3 and -6.5 dB (no faster than the loud ends' -6.4);
   - after adoption, the master's final release reaches -10 dB at 0.2 s or later and -20 dB at 0.5 s or later;
   - mf-ff ends unchanged.
5. After adoption, refit the pp/p re-bow fills, as the c44 do-not-touch rule asks for any release change. The longer soft release may also close the soft re-bow holes c45 A #5 measured (inferred).

**Generic for every movement.** String Sus MAX / Sus Marc LITE release caps: 150 ms at mf/f/ff and 350 ms at pp/p (confirm with the test). After any release change, check that soft phrase ends fall no faster than loud ones in the 0.05-0.1 s after the note-off, and that the final soft chord's master release takes at least 0.2 s to fall 10 dB.

### 2. Both fff downbeats still step only about 2 dB, and the limiter now has room for more (measured; fix simulated)

**Where.** Bar 160 (qn 636, the single fff, cymbal stroke, largamente) and bar 122 (qn 484, fff with the tam-tam). All tracks.

**What is wrong.** The movement's two highest points arrive with less contrast than the ff arrivals around them (bar 33 +10.0, bar 41 +4.9, bar 26 +4.8 dB). The drier hall did not cause this, but it slightly lowered the step at 636.

**Evidence (measured).**
- mp3, 635-635.75 -> 636-637: c43 +2.2, c45 +1.8 dB. Bar 122, 483-484 -> 484-485: +2.7 -> +2.5.
- Master: +2.3 -> +1.9 and +2.6 -> +2.3.
- Of the master's 12 largest loud arrivals, 635 ranks 10th and 484 11th (2.5 dB each). The smallest of each reference's 12 largest arrivals is 4.5 (Brahms 1/i), 4.0 (Brahms 4/i), 3.9 (Dvořák) and 3.0-3.2 dB (Brahms slow movements).
- Per stem at 636 (635-635.75 against 636-637): the strings step only +1.5 to +2.0 dB, while Horns a2 (-0.8), Clarinet 1 (-1.1) and Flute 2 (-1.5) fall. Their envelopes rise 5-6 dB there (vol_db, e.g. Clarinet 1 +4.3 -> +10.0), so the new notes after the breath come out of Opus quieter than the held crescendo notes before them.
- The c45 delivery limiter is about 0.0 dB (c42-c44: 0.4-0.6). The reason the c06 and c40 lifts were kept small, the limiter, no longer applies.

**Fix (level only, stem-fixable, `build/score_config.py`).** Add two rows to `LEVEL_SHAPES["_all"]`. Keep the existing 636 lift row `[(635.98, 0.0), (636.02, 1.5), (636.4, 1.5), (637.0, 0.0)]` and c41 B #3's hold-back rows.
- `[(635.98, 0.0), (636.02, 1.5), (636.6, 1.5), (637.25, 0.0)]`
- `[(483.98, 0.0), (484.02, 1.5), (484.6, 1.5), (485.25, 0.0)]`

**Simulated** on the c45 master with the unchanged delivery chain (the baseline copy reproduces c45: step +1.8, S max 160 -11.5, limiter 0.0):
- step into 160: +1.8 -> +3.0 dB; into 122: +2.5 -> +3.5;
- limiter 0.0 -> 1.1 dB (the peak is at qn 636.39);
- LRA 14.9 (unchanged); span 19.0 -> 19.2 (0.2 over the 16-19 target, as in c42);
- S max 160 -11.3 > 122 -12.0 > 167-170 -13.5 > 26 -14.2, order kept.
- A smaller variant, +1.0 dB on each row, gives +2.6 / +3.1, limiter 0.6, span 19.1.

**Generic.** A delivered fff or ff arrival should rise at least 3 dB from the last beat before it to the first beat (in the references' largest arrivals, 3-8 dB). When the delivery limiter is under 1 dB, spend the headroom on an `_all` lift of +1.5 dB from the downbeat, held about 0.6 qn and gone by +1.25 qn.

### 3. The Lento's opening pp swell lost a third of its growth, and the ride, at its cap there, passes the loss straight into the mp3 (measured; fix simulated)

**Where.** Bars 1-4 (qn 3-12): celli, basses and bass clarinet pp < > over the timpani's ppp roll (hairpins 4-7 <, 7-8 >, 8-10 <, 10-16 >). This is the first phrase the listener hears.

**Evidence (measured).**
- Master K per beat: growth from qn 3 to the swell's top at qn 6 is c43 +7.7, c45 +5.5 dB (mp3 the same). The top fell from -29.9 to -34.7 dB in the master and from -22.1 to -26.3 in the mp3.
- The second swell (8 -> 10) is +5.8 -> +5.1.
- The mp3 bars 1-4 are 0.9-3.3 dB lower than c43, the deepest losses anywhere outside bar 84. The delivery ride sits at its cap there (lift 8.3 dB, as in bars 177-182), so it cannot make up the loss.
- Cause, per stem (c45 minus c43, qn 4 / 5 / 6):
  - the celli's E-flat3 (3.82-7.4) -4.9 / -6.1 / -5.7 dB; over bars 1-4 the celli stem lost 5.6 dB at 100-250 Hz and gained 1.4 dB at 2-8 kHz;
  - basses -3.7 / -2.5 / -3.4;
  - bass clarinet -0.8 / -2.1 / -2.5 and timpani -1.7 / -1.6 / -1.6 (no EQ change on either, so this part is the drier hall).
  - The celli's extra 3-4 dB comes from c44 C #4: the static 170 / 125 Hz bells were moved to the loud spans. The +1.7 dB soft trim restores the K level only on average, and less than that for notes near the bells' centres.

**Fix (level only, stem-fixable, `build/score_config.py`).** Add to `LEVEL_SHAPES["Violoncellos"]` and `LEVEL_SHAPES["Double basses"]`:
- `[(3.8, 0.0), (5.0, 1.5), (6.0, 3.0), (7.0, 3.0), (8.0, 0.5), (8.5, 0.0)]`
- `[(7.9, 0.0), (9.0, 1.5), (10.0, 2.0), (11.0, 1.0), (12.0, 0.0)]`

**Simulated** on the c45 stems (master sum, K): growth 3 -> 6 is +7.6 dB (c43 +7.7), with the top at -32.6 (2.1 dB over c45, still 2.7 under c43); 8 -> 10 is +5.6 (c43 +5.8). The start level at qn 3 is unchanged. The celli stay about 6-8 dB over the timpani roll at qn 5-6 (now 3.9-5.2).

**Generic.** After moving a low-mid EQ off the soft passages, or drying the hall, re-measure soft low-string swells beat by beat against the previous render and restore each swell's growth with level shapes. Where the delivery ride sits at its cap (long pp introductions and codas), any master loss reaches the mp3 1:1.

### 4. Three printed timpani crescendo rolls do not grow; two of them end on a stroke, the Felt Cresc row's use case (measured problem; level fix computed; MANUAL-GAPS #12 test inferred)

**Where.** Timpani:
- 244-248 (bar 62, pp <, into a roll);
- 456-460 (bar 115, mf < into the f stroke at bar 116, end of the stringendo);
- 556-560 (bar 140, f < into the accented ff stroke at bar 141).

**Evidence (measured; c43 the same, so not a hall effect).**
- Stem growth, last third minus first third: +0.3, +1.8, +0.2 dB (c43 -0.4, +1.6, +0.5). The other ten timpani crescendos grow +3.2 to +11.0 dB.
- Read in parts.json: across these three hairpins the volume envelope falls (vol_db +14.0 -> +11.8, +9.5 -> +8.2, +9.2 -> +6.5), presumably the roll trims stepping down as CC1 moves into a louder layer. CC7 rises only +3.9, +0.4 and +1.9 dB. The bar-131 roll (516-520), whose envelope rises (+0.8 -> +3.0), grows +6.7.
- The rolls sit 13-17 dB under the master before the stroke. A +3 dB growth keeps them under the texture, as Dan's rule 5 asks; the rule also says that a printed crescendo makes a roll grow.

**Fix.**
- (a) Now, level only. Add to `LEVEL_SHAPES["Timpani"]`:
  - `[(244.0, 0.0), (247.9, 4.0), (248.5, 0.0)]` (into the decrescendo at 248);
  - `[(456.0, 0.0), (459.9, 4.0), (459.98, 0.0)]`;
  - `[(556.0, 0.0), (559.9, 4.0), (559.98, 0.0)]`.
  The strokes keep their level: the envelope is back to 0 before the 0.06 s stroke delay. A linear 0 -> 4 dB ramp adds about 2.7 dB to the last third over the first, so growth becomes about +3.0 / +4.5 / +2.9 dB (computed, inferred).
- (b) MANUAL-GAPS #12, pass 2. A "Timp cresc test" alias of Timpani over 455-461 and 555-561 on the Felt Cresc row (KS E0).
  - Choose the take whose length matches the roll (1.8-1.9 s). Read the lengths from the `.ews` frame counts, as c01 did for the cymbal, under `HP * Timp Flt Crs p|f`.
  - Use velocity for its two layers.
  - Compare the growth, the stroke's level and its 2-5 kHz front with the main stem. Adopt if the roll grows at least 3 dB and the stroke lands within 1 dB of the current stroke.

**Generic.** Every printed timpani crescendo roll should grow at least 3 dB on the stem. Check that a roll-trim step at a CC1 layer change does not cancel the CC7 rise, and ramp such steps over the hairpin.

### 5. The harp's soft notes still play one dynamic layer too hard on the thumb picks (manual p.69; layers measured in parts.json; audibility inferred)

c40 C #4, deferred in c41 and unchanged since: p.69 says velocity selects one of five layers in each round-robin group.
- Printed p (66 notes, v52-110, median 64): none can reach Thumb p.
- Printed mp: 46 of 72 would play Thumb mf on a thumb pick.
- The ppp final chord (v46) plays Thumb mp.
The level order is right (Manual notes); what is off is the attack and timbre on alternate notes of the soft arpeggios in bars 47-63 and 163-166 and on the last chord.

**Fix (as c40).** Read all five splits per group from `Harp Sus RR.oib` (`opus_state.load_oib`). Set each printed level's velocity inside both groups' layer for it (p and softer 40-42, mp 58-70, mf 86-97). Move the level difference into `mix.json` Harp `soft_trim_db` / `dyn_trim_db` or into exact level steps, and keep the `VEL_SET["Harp"]` fits only as level steps. Check that each printed level's median 10 ms peak stays within 1 dB of c45 (p -41.0, mp -37.9, mf -31.0) and that the harp stays a median 6 dB or more under the melody in bars 47-55 (now -6.7). If Thumb p is still too hard, try Gliss Technique (p.70) on the p arpeggios.

### 6. Optional: end two loud_eq spans where the dynamic changes, not inside held notes (measured; master unaffected)

**Where.** `build/mix.json`.
- Violoncellos `loud_eq[2]` (170 / 125 Hz bells) and Double basses `loud_eq[3]` (180 Hz bell) end at 287.75-288, inside the pp half note tied over bar 72-73. Change `[287.75, 1], [288, 0]` to `[285.9, 1], [286.0, 0]`, so the bells leave as the celli and basses go to pp on beat 3.
- Double basses `loud_eq[3]` covers the bar-33 fp note (128-131.74). Change `[110, 1], [131.75, 1], [132, 0]` to `[110, 1], [128.0, 1], [128.4, 0]` for the basses only; the celli rest there.

**Evidence.** See "loud_eq spans" above: stem steps of -4.4 dB (celli) and +2.8 / -2.7 dB (basses). Both are masked in the master today (within 1 dB of c44 per 0.1 s frame), so this is housekeeping. It matters only if the tutti or the bassoon solo around them is later lowered.

**Generic.** Switch span EQs at the dynamic change or at a note change, never inside a held note.

## Standing checks (BRIEF 6-8, S1-S3), through this lens (measured)

- **BRIEF 6.**
  - mp3 -19.8 LUFS, LRA 14.9 LU, span p10-to-max 19.0 dB (target 16-19), TP -1.9 dBTP, limiter about 0.0 dB.
  - Master LRA 23.4 LU (c43 23.5; Dvořák 21.8).
  - 5 s moves of 3 dB or more: median 81% kept, 2 inversions (c43: 81%, 2).
  - Climax order 160 > 122 > 167-170 > 26.
- **BRIEF 7.** `cycles/c25/actor_scripts/loopscan.py` (path changed to this folder), master at 3.95 s, band / centroid:
  - Lento bars 1-14 +0.28 / -0.14 (c43 +0.40 / -0.08); final chord 179-182 -0.05 / +0.17; bars 175-178 -0.02 / +0.07; bars 160-164 -0.39 / -0.06.
  - Stems: Bass clarinet 492 +0.68 / +0.68 (c43 +0.84 / +0.71, the known breath-split artefact); Bass clarinet 11 +0.66 / +0.26 on a 6.2 s window flagged short. No new pulsing.
  - Held swells: hairpins by family as in "State" above.
- **BRIEF 8.** 19 long fitted brass accents: 2-5 kHz in the first 80 ms minus body, median -9.1 dB, p90 -5.0, max -1.5 (c43 -9.3 / -5.6 / -4.0).
- **S3.**
  - Bar 62 still decays like a release (master re the forte at 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 / 0.3-0.5 s: c43 -3.1 / -5.6 / -9.1 / -12.1 / -13.1, c45 -3.0 / -6.4 / -9.8 / -12.7 / -14.4).
  - Bar 84: the bar-83 ff chord ends at 330.9, a beat before the sub. p. In c45 its tail decays within that beat and reaches the p level by about 332.2, where c43's hall still filled the rest. The p now enters on a near-silent beat. That is the drier hall, not a cut.
- **S1 / S2.** Not re-measured (c45 actor: strokes +42 ms median, sus gaps +24 ms; probe legato SD 45 / 42 / 55 / 49 ms).

## Also measured (no change proposed)

- Bar 117 (letter G, a tempo): the stringendo crescendo tops out on bar 116 beat 3, and the ff downbeat of 117 is 0.9 dB under it (c43 0.8). The score has the trumpets and clarinets at ff in bar 116, and the trumpets rest at 117 (Trumpet 1 -17.7 dB there), so I read this as written.
- Tam-tam (484, 696), suspended cymbal and crash ring at 636, levels relative to the master at +0 to +8 s: within 1.5 dB of c43.

Do not touch: the shared hall (fx 0.095, low cut 160, `ir_setup`) and every send. The crescendo machinery, which still builds as in c43: hpgain, chained crescendos, soft hairpin gains, the c41 B #3 hold-back rows into 484 and 636 and the existing 636 lift (finding 2 adds to them). SUBITO_FRESH, SUBITO_TAIL and the f62 aliases with their release fit (bar 62 still decays like a release). The delivery settings (RATIO 3.0, KNEE_BELOW 5, LIFT_SMOOTH_S 5, TOP_RATIO 2.5, FAST_CAP_ABOVE 4, MOM_CAP_ABOVE 6) and RIDE_TRIMS. The 150 ms caps at mf-ff and the horns' 237 ms. width_by_mic. The coda morendo shapes, the final-chord re-bow refinements and the harp's `env_sustain` / `env_release_ms`. TIMP_CC1_MAP with its roll trims, outside the three hairpins of finding 4.
