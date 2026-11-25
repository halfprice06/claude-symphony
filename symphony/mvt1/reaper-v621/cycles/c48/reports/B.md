# Critic B, cycle 48 (render c47): balance and levels

## Manual notes (second round, cycles 48-51: pages chosen for this lens's open problems; MANUAL-GAPS.md and DIGEST.md read)

Pages read in full from the May 2021 HO manual: p.64, p.91-92, p.97-98, p.124-125.

| Source | What it says | Where it applies here | Followed in c47? |
|---|---|---|---|
| p.64 | CC7 (or the fader) sets each track's level against the others; CC11 shapes the line; velocity sets loudness only on shorts. | Every balance fix below. | Yes. All balance corrections live in the volume envelope (roles, note trims, LEVEL_SHAPES), and CC11 keeps each printed dynamic's layer (read in parts.json). Every fix below is a level change only. |
| p.91-92 | Sustain loops; bow direction alternates by round robin; the Basses have no finger-position choice. Marcato Sustain adds a marcato sample "for extra power at the start of the note". | Finding 1: the basses' low register. Celli 84 / 448 strokes on Sus Marc LITE (c47). | Basses: no finger position exists, so the weak G2 / F2 can only be corrected with level (finding 1). Celli 84: plays 2.2 dB louder than before as an inner voice (c47 CHANGES); its level is not a problem here (measured -10 dB re master). |
| p.97-98 | Tremolo has no velocity response; CC11 changes dynamics and timbre during the note, "because long-held passages, including the possibility of crescendo or decrescendo, are characteristic of tremolo writing". | Finding 4: the Violins II / violas tremolo crescendo in bars 80-81. | Followed: CC11 follows the printed hairpin from 46 to 114 over qn 316-324.5 (read). Because the ramp is linear, the tremolo is already at f (CC11 86) by qn 321, one bar before the ff. The fix is a level shape. |
| p.124-125 | Felt rolls: CC1 crossfades 8 dynamic layers ("crescendos and decrescendos"); CC11 and velocity set overall loudness. Felt Cresc rolls are recorded crescendos ("the most realism"). | Finding 3: the bar-11 roll pp < f. | Partly. CC1 follows `TIMP_CC1_MAP`, which floors ppp-p at 56-60 (the mp layer), and `TIMP_ROLL_TRIM_DB` (pp +19 dB) plus the `timp_hp` lift (+7.45 dB at qn 40) set the level (read). So the pp start plays a louder layer, brought to pp with volume, and the crescendo gains level faster than the strings. MANUAL-GAPS #12 (Felt Cresc for crescendo rolls into a stroke) fits this roll: 4 qn at q=50, 4.8 s, ending on the bar-12 f stroke. |
| MANUAL-GAPS #12 | Recorded crescendo rolls; never tried. | Bar 11 (qn 40-44), the clearest case in the score. | Open. Finding 3 gives a level-only fix that does not depend on it. |

## Method

- Render: `cycles/c47/render/` (40 delivered stems; Horn 1 is the c46 stem; Violins II, violas, celli and basses carry pass-2 audio from qn 695.8). Compared with `cycles/c46/render/`. Data: `build/parts.json` (describes the delivered stems), `build/roles.json`, `build/note_trims.json`, `build/pitch_trims.json`, `build/mix.json`, `build/score_config.py`.
- Frames: 4096-point FFT with a 50 ms hop on every stem and the master: K-weighted (BS.1770 filters applied in the frequency domain), A-weighted, and octave bands. "re M" means the stem minus the master. "Over the loudest other" means the stem minus the loudest other stem in the same window (K).
- Same-dynamic scan: per beat, the tracks whose printed dynamic is flat across the beat and whose notes cover at least 75% of it. Each track is compared with the median of the others at the same dynamic, where four or more share one.
- Simulations scale a stem's frame powers by the proposed shape and add the difference to the master as power.
- Score pages read: 2, 6, 8, 9, 10, 11, 12, 13, 14, 17, 18.

## The coordinator's checks (measured on the c47 stems)

- **Bar 145, Clarinet 1.** Re M at 576-578: -3.8 -> -7.5 dB. Oboe 1 over the loudest other stem per half qn 578.0-581.5: +0.4 / +5.2 / +8.0 / +8.2 / +6.0 / +10.1 / +5.6 / +2.5 (c46 -4.0..+7.3). The nearest voice is now Violins I, not the clarinet. **Done.**
- **Bars 35-38, Violins I.** Over the loudest other per qn 136.5-151.5: +5.5 / +1.5 / +5.3 / +0.4 / +1.6 / +7.5 / +8.1 / +1.8 / +6.3 / +4.6 / +4.9 / +2.6 / +4.8 / +3.9 / +0.1 / +1.6. No beat is under 0 (c46 had 3). **Done.**
- **Bar 40, celli.** Over the loudest other at 157.5-159.5: -1.1 / +3.4 / +3.9 / -0.7 / +4.2 (c46 +1.9..+6.9). Matches the plan.
- **Violas before the bar-20 join.** Re M at 77.25-77.75: -4.6 / -6.4 / -4.7 (c46 -2.9 / -2.0 / -3.2). The swell is gone.
- **Trumpet 1.** Minus Violins I per half qn 275.5-283.5: -3.7..-11.8. The flipped c46 values were -5.2..+11.1. Back to c45. Bars 113-114 (451-456): -5.8..-14.1 under Violins I. Its accents' 2-5 kHz front over the body is now at most -3.3 dB (c46 Trumpet 1 284: +4.4).
- **Splice at qn 695.8.** Violins II, violas, celli and basses all sit within 0.0 dB of c46 per 0.25 qn over 694.5-697.5. The strings start from rest except the violas, which have no step at the splice. Clean.
- **Delivered.** Recomputed from the mp3: p10 -30.24, maximum -11.31 at 356.3 s (bar 160), span 18.93 dB. Climax order unchanged.
- **Timpani rolls (Dan's priority).** Per 1 qn window, the roll's rank among 39 stems and the roll minus the loudest other stem (median / max):

| Roll (bars) | Rank | Minus loudest other |
|---|---|---|
| 11-12, pp < f | 2-13 | -3.6 / -2.5 (finding 3) |
| 13-14 | 6-11 | -17.9 / -11.2 |
| 40-44 | 4-15 | -11.1 / -4.7 |
| 62-63 | 4-9 | -7.8 / -5.2 |
| 80-82 | 4-10 | -6.9 / -2.7 |
| 117-131 | 3-23 | -9.9 / -2.0 |
| 144-146 | 2-10 | -7.7 / -4.3 (c46 -11.2 / -4.3: the bar-145 clarinet cut removed the loudest other part) |
| 158-161 | 4-18 | -5.5 / -2.5 |
| 166-170 | 1-25 | -6.3 / 0.0 (the bar-167 f arrival stroke, 664.0) |
| 174, 181-182 | 3-9 | -18.8 / -8.9 |

  Only the bar-11 roll ranks this high while still held. The bar-144 roll at mp is 3-4 dB under the bassoon's mf figure. In bar 145 the pp roll is level with the pp violas and basses (-14..-20 re M), not over them.
- **Same-dynamic scan (does p sound like p).** At pp, p and mp, almost every track lies within ±3 dB of the median of the others. Violins I runs +4..+8 dB over the median, as the lead.
  - **Exceptions at soft dynamics.**
    - Double basses: pp -3.7 (67 beats), p -4.2, mp -5.7, mf -4.6 (finding 1).
    - Clarinet 1 pp +6.2 (finding 2).
    - Harp p / mp -3.9 / -8.6. In bars 59-63 it is level with the p violas (-16..-20 re M), so it matches its own dynamic.
    - Horn 4 pp -3.4: inner sustained notes.
  - **At f / ff.** Inner winds sit 2-6 dB under the median: Flute 2, Oboe 2 at mf / f, Contrabassoon, Clarinet 2 f. Trombone 1 f +3.0, Trumpet 1 ff +3.8.
  - **Trumpets a2.** +4.7 / +4.4 at f / ff, on only 3 beats each. Bars 131-132: its f rhythm is -12.6..-16.9 re M, 8-11 dB under the ff theme. Bars 167-170: it carries the ff tune with Horns a2 and violas. The tune group is +1.4..+9.5 over the loudest single f part (median +4), which is right for ff over f.
  - **Percussion.** Tam-tam fff is the loudest stem at 484-491 (as printed, heavy beater). The suspended-cymbal stroke at 635-636 supplies about half of the master's 5.7-22 kHz band (-2..-3.5 dB share). The K Crash ring then takes over (-6..-15 dB share over the next 2.4 s). No change.
- **Dan's standing checks.**
  - **Loop pulsing.** 41 held spans of 6 s or more: 100-300 Hz level and spectral centroid, autocorrelation at 3.95 s. No sustained-note span is over 0.45. The one over 0.6 is the decaying harp arpeggio at 247.5, which is not a loop.
  - **Brass accents.** 2-5 kHz energy over the first 80 ms minus the body, 177 accents: medians -5.8..-16.8 dB per track. One note is over +3: Horn 3 124.0 (+3.8).
  - **S1.** Lens A's measures take precedence.
  - **S3.** At bar 62 the master falls 11.4 dB in 0.25 s, the same as c46, and the f62 aliases' release decays under the p.
- **Coda cor anglais.** The counter-line is -4..-9 dB under the mp cello solo (median -5.5 per qn), which is one dynamic step for a p espr. answer. No change.

## Findings, ranked by what a listener would gain

### 1. Bars 6-7 and 13-14: the basses' pp octave sits 8-14 dB under the celli and drops out of the Lento string chords (measured; audibility inferred)

**Where.** Double basses: G2 / F2 at qn 20.0, 22.003, 24.0, 26.003 (bars 6-7) and G2 at 48.0 and 52.92 (bars 13-14), each an octave under the celli.

**Score (p.2).** Bars 6-9: Violins II, violas, celli and basses hold pp chords under the cor anglais espr. solo, with the basses doubling the celli an octave below. Bars 13-14: celli and basses p > pp under the horn solo.

**Evidence (measured).**
- Basses minus celli (K), per qn 20-27: -5.0 / -12.6 / -15.5 / -13.2 / -3.9 / -9.9 / -10.4 / -11.1. Over 19.9-28 as a whole: -10.1 dB.
- Per qn 48-55: -7.1 / -5.8 / -8.5 / -8.3 / -9.9 / -10.7 / -8.4 / -2.7. Over 48-56 as a whole: -7.2 dB.
- Basses re M at 21-23: -19.6..-21.9 dB. At this level they add nothing that can be heard.
- In the same-dynamic scan the basses are the only string section under the median at every soft dynamic: pp -3.7 (67 beats), p -4.2, mp -5.7. The worst pp beats are bars 6 (-10..-12), 14 (-9..-11) and 43 (-7..-12).
- The note's spectrum (octave bands, dB) shows why:
  - G2 at qn 20: fundamental -50, 177-355 Hz -54, 355-710 Hz -63.
  - The bar-5 C2 in the same patch: -56 / -49 / -63.
  - So the G2 sample is thin above its fundamental, which matches LEARNINGS 13-14 (Basses KS Master uneven by pitch).
- At pp the ear also weights 98 Hz below 1 kHz far more than K does (equal-loudness contours), so the real deficit is larger than these numbers (inferred).
- Causes (read):
  - `build/roles.json` Double basses `[16.0, 28.0, -2.0]` and `[48.0, 56.0, -2.0]` (c16 C #2) were set against the bar-5 C2 solo.
  - `build/pitch_trims.json` G2 (43) -6 dB on every articulation: 20.0 and 22.003 skip it, but 48.0 and 52.92 do not.
  - The bar-14 G2 therefore plays at -8 dB.
- RK (Principles, "Comparison of resonance"): in piano one string section balances another. Basses doubling the celli should sit a few dB under them, not 10.

**Fix (level only, can be a stem fix).**
- `build/roles.json` Double basses: change `[16.0, 28.0, -2.0]` to `[16.0, 19.9, -2.0, 0.25]` so the bar-5 C2 keeps its cut.
- `build/note_trims.json` Double basses: add `"20.0": 3, "22.003": 3, "24.0": 3, "26.003": 3`, giving +5 dB in bars 6-7 with the role change.
- `build/pitch_trims.json` Double basses `_skip_onsets`: add `48.0` and `52.92`. Change the roles row `[48.0, 56.0, -2.0]` to `[48.0, 56.0, -4.0]`, giving +4 dB net in bars 13-14.
- Simulated:
  - Basses minus celli per qn 20-27: 0.0 / -7.6 / -10.5 / -8.2 / +1.1 / -4.9 / -5.4 / -6.2 (-5.1 over the span).
  - Per qn 48-55: -3.2 / -1.8 / -4.5 / -4.3 / -5.9 / -6.7 / -4.4 / -1.5 (-3.3 over the span).
  - The cor anglais solo stays 9-14 dB over the basses. Master change under 0.1 dB, so the delivered span is unchanged.
- Check after the render that the bar-5 C2 (16-19, re M -0.8) is unchanged.

### 2. Coda, bars 175.75-177: Clarinet 1's pp espr. solo is 4-11.5 dB over every other pp part and makes up most of the master, a lift that went stale (measured)

**Where.** Clarinet 1 qn 699-706.5 (D5 pickup, C5 held for 6 qn, then B4), over the trombones' pp dolce chorale, the bass clarinet pp and the pp strings.

**Score (p.18).** All parts are pp. The clarinet line is marked "espr.", the trombones "dolce".

**Evidence (measured).**
- Clarinet 1 re M per qn 699-706: -5.4 / -1.7 / -4.0 / -2.6 / -2.3 / -2.9 / -3.2 / -5.4.
- Over the loudest other stem: +4.1 / +10.6 / +3.2 / +6.2 / +9.5 / +6.5 / +6.1 / +1.5. At 700.0-700.5 the margin is +11.3..+11.5, where the c47 fill (`A's optional Clarinet 1 700 fill`) lifted the note's start by a further 1.6-3.7 dB against c46.
- In the same-dynamic scan this is the source of Clarinet 1's pp +6.2: +9..+12 over the median of the other pp parts at 700-705. A pp espr. solo needs about +4-6 dB. +9-12 is the margin of an mp-mf line.
- Cause (read): `build/roles.json` Clarinet 1 `[699, 712, 2]` was set in c07 (B #5), when the solo measured "2-5 dB under the pp strings". Since then the strings' pp trims, the coda chorale rows and the c47 fill have moved the reference by more than 3 dB (LEARNINGS 13: re-check old lifts when the reference has moved).

**Fix (level only).**
- `build/roles.json` Clarinet 1: remove `[699, 712, 2]`. Keep `[705.75, 707.75, 2.5]`, which carries the B4 diminuendo, and keep the 700 fill shape.
- Simulated (-2 dB over 699-706.5): over the loudest other +3.0 / +8.6 / +1.2 / +4.2 / +7.5 / +4.5 / +4.1 / +0.2. It is still the top voice in every beat.
- Master at 700-706 -1.1 dB. The delivery ride takes back about two thirds of that. The c47 ride trim on 696-728 covers this span, so the effect on p10 is under 0.1 dB (inferred).

### 3. Bar 11: the pp < f timpani roll rises faster than the strings' own crescendo and is the third-loudest stem by beat 3 (measured)

**Where.** Timpani roll qn 40.0-43.97 (A-flat2), crescendo to the f stroke at 44.0.

**Score (p.2).** Bar 11: the timpani roll pp < into the f stroke on the bar-12 downbeat. Violins II, violas, celli and basses also play pp < f. Violins I has the rising line, mp <.

**Evidence (measured).**
- Roll re M per qn 40-44: -11.9 / -10.9 / -9.5 / -9.4 / -10.1.
- At the pp start it is level with the violas (-11.9) and 2.5 dB over the basses (-14.4). The brief's target for a pp roll is 3-5 dB under the quietest sustained string section.
- At 42-43 it sits over Violins II (-13.5 / -12.3), violas (-11.6 / -13.5), celli (-10.8 / -9.0) and basses (-11.5). It ranks third of 39 stems, 3.1-3.8 dB under Violins I.
- No other held roll in the movement ranks this high (table above).
- Data (read):
  - CC1 57 -> 88: the mp layer at the pp start, because `TIMP_CC1_MAP` floors pp at 56.
  - Volume +19..+21 dB (`TIMP_ROLL_TRIM_DB` pp 19.0 and the `timp_hp` +7.45 dB), falling to +15 by 43.9 as CC1 rises.
  - The roll therefore gains about 2.5 dB re M over the crescendo, while the strings lose 1-4 dB re M.

**Fix (level only).**
- `build/roles.json` Timpani: add `[40.5, 43.95, -3.5, 0.25]`. The 0.5 qn start ramp makes it full from 41.0, and the f stroke at 44.0 is untouched.
- Simulated: roll re M -11.9 / -14.2 / -12.7 / -10.7 / -10.1. That is 2-5 dB under Violins II and the celli in beats 2-3, still rising into the stroke. Rank at 42: 3 -> 6. Master change under 0.4 dB.
- Alternative if the actor tests MANUAL-GAPS #12: a Felt Cresc take of about 4.8 s ending on the bar-12 stroke. Measure its curve against the strings' crescendo the same way.

### 4. Bar 81: the Violins II tremolo crescendo is the loudest stem a bar early and covers the last motif entry (Violins I and Flute 1 f) (measured)

**Where.** Violins II (E-flat4 tremolo) and violas (C4 tremolo), qn 320-324.5, crescendo p < ff into bar 82.

**Score (p.8).** Bars 80-81: Violins II and violas hold the tremolo with a hairpin from p (bar 80) to ff (bar 82). Over it the f motif passes between groups:
- low winds, Horns a2, Trombones a2 and celli at 316.5 and 320.5;
- oboe, clarinet and Violins I at 318.5;
- Violins I and Flute 1 at 322.5-323.5.

**Evidence (measured).**
- Violins II re M per half qn 320-323.5: -3.8 / -5.5 / -5.6 / -6.3 / -3.4 / -4.0 / -5.3 / -5.7. It is the loudest stem through bar 81, by +1.0..+4.3 over the next.
- At the last entry (322.5-323.5) the motif group (Violins I, oboes, clarinets, flutes, summed) is -6.5 dB re M. Violins II alone is -4.7 and the tremolo pair -3.5: the accompaniment is 1.8-3.0 dB over the f motif.
- The earlier entries are clear: group minus the tremolo pair +0.7 at 320.5 and +1.5 at 318.5.
- Cause (read): CC11 rises linearly from 46 to 114 over 316-324.5, so the tremolo is at f (86) by 321. The Violins II volume is -1.8..-3.3 dB there. No role row covers bars 80-81, and the c05 `[304, 320, -3, 4]` row ends at 320.
- Players grow a two-bar tremolo crescendo mostly in its second half, under entries marked f (inferred).

**Fix (level only).**
- `build/roles.json`: Violins II add `[320.5, 324.25, -3.0, 0.25]`; Violas add `[320.5, 324.25, -1.5, 0.25]`.
- Simulated:
  - Violins II re M at 321-323.5: -7.7 / -8.6 / -5.0 / -5.9 / -7.4 / -6.9.
  - At 323.0 it falls under Violins I (-1.9), and Violins I rises to -5.5 re M.
  - The ff arrival at 324.5 is unchanged. The end ramp brings the tremolo back up into it.

## Do not touch

- The c47 B #2-#5 rows (bar-145 Clarinet 1, bars 35-38 roles, the bar-40 celli shape, RIDE_TRIMS) and the Violas 78 LEVEL_SHAPES row.
- Trumpet 1's c45 state: rebuild it fully if `state_check.py` flags it again.
- The letter-G and bars 131-134 tune balance: tune group +1.8..+11.4 over the loudest accompaniment at letter G.
- The bars 167-170 Trumpets a2 / Horns a2 / violas tune levels.
- The tam-tam, suspended-cymbal and K Crash levels.
- The bar-174 and bars 13-14 timpani shapes, and every other crescendo-roll ramp.
- The oboe's bar-145 role, the cor anglais coda rows, the hall and every send.
- The climax order 160 > 122 > 167-170 > 26.
