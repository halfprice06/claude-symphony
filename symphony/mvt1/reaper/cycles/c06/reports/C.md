# Cycle 6, critic C: dynamics over time (render c05)

Lens: the loudness shape of every hairpin and phrase, the arc of the whole movement against the score, the two fff climaxes (bar 122 with the tam-tam, bar 160 after the suspended-cymbal roll), the recapitulation at 131, the coda, the delivered mp3 (BRIEF item 6), loop pulsing on long notes (item 7), accents (item 8) and decays.

Method. I measured the stem-fixed c05 render (`cycles/c05/render/`, the master is the float stem sum) and `mvt1-mockup-c05.mp3`. Score qn maps to file time through the `build/parts.json` tempo map, with no shift. Loudness is ffmpeg ebur128 at 10 Hz: M (400 ms) and S (3 s, centred). Stem levels are plain stereo power. All simulations were done on the c05 stems: I applied dB envelopes, summed the stems and ran a copy of `tools/deliver_master.py`. A no-change run reproduces c05 exactly (LRA 15.6 LU, span 20.3 dB, limiter 3.0 dB). Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c06-C/` (`bars.py`, `hp.py`, `moves.py`, `ride.py`, `arr2.py`, `hpstem.py`, `loops.py`, `acc.py`, `sim1.py`-`sim5.py`, `simlift.py`).

State of the arc (measured). The master has LRA 21.8 LU, the same as the Dvořák 9/i reference. The delivered file measures -19.8 LUFS, LRA 15.6 LU, p10-to-max span 20.3 dB (target 16-19) and a 3.0 dB limiter. Its 5-second moves keep a median share of 0.82 of the source change, with 0 inversions. The climax order holds: delivered S max is 160 -9.6, 122 -10.3, then 169/158 -12.1, 82 -12.8 and 26 -13.9. The diminuendo after the tam-tam is well shaped: master bars 123/124/125/126 measure -8.8/-14.2/-23.0/-28.6 dB, so p arrives on time. The recapitulation arrival at 131 rises 2.2 dB in momentary maximum over the beat before it, and the ff that follows is level with the exposition's ff theme (bars 131-134 -16 dB against 27-32 -14..-16.5). The accents are not harsh (item 8): 2-5 kHz energy in the first 80 ms minus the body has a median of -8..-16 dB on every brass, Vln I, Vc, Fl1, Ob1 and Cl1 accent, and the worst is +3.2 dB (Horn 1 at qn 285).

## 1. The main climax lands with no step: bar 160's fff downbeat is no louder than the end of the crescendo (measured)

Where: qn 632-640 (bars 159-160), all pitched tracks. The same problem, smaller, at qn 484 (bar 122).

Evidence. I compared the momentary (M) maximum in the first 0.4 s after each arrival with the M maximum over the 0.8 s before it. At 636 the step is +0.4 dB on the master and +0.3 dB delivered. Other arrivals measure: qn 484 (bar 122 fff) +2.5/+2.4, qn 100 (bar 26 ff) +4.7/+4.5, qn 676 (bar 170) +3.2/+3.4, qn 664 (bar 167) +6.4/+6.2. The main fff climax therefore has the weakest arrival in the movement.

Per-beat master M: bar 159 runs -11.3, -9.6, -8.8, -7.6 and bar 160 runs -7.8, -6.6, -6.4, -7.6. In the delivered file the last beat of 159 is -10.1 and the downbeat of 160 is -10.3, so the downbeat is lower. The crescendo has already arrived before the downbeat. CC11 reaches 124 at qn 635.875 on Vln I, Vc, Vla and Horn 1, and the hairpin chain's dB ramp reaches its full value at 636 (Vln I vol +6.75 at 635 to +7.5 at 636; Vc +5.8 to +6.0). Nothing is left for the arrival.

In addition, the string mass arrives late. In 0.1 s frames, Vln I measures -24 dB at the onset and -18 at +0.2 s, and Vc measures -25 at 0..+0.2 s and -21 at +0.3 s. Vln I's 636 note is played as a legato target (lead 0.155 qn, no keyswitch change) although the part prints a new downbow there. In a real orchestra the cymbal crash, the timpani and fresh bow strokes make this downbeat the loudest instant of the movement (inferred).

Fix (level part, can be done by stem fix): add a generic rule in `tools/score_to_parts.py`, `ARRIVAL_WEIGHT_AT = {qn: (pre_db, db)}`, set in `build/score_config.py` to `{636.0: (-2.5, 2.5), 484.0: (-1.5, 1.5)}`. It applies to every non-percussion track:
- (a) The crescendo's dB ramp is scaled so that it ends `pre_db` lower at the arrival, as a linear ramp from 0 at qn-4 to `pre_db` at the moved onset. This lowers the slope; it is not a dip.
- (b) At the moved onset, a `db` step full by +0.05 s, held to qn+0.5 and gone by qn+1.0, back to the FFF hold value.

Simulated on the c05 stems (`sim2.py`): the 636 step goes +0.4 -> +3.8 dB on the master and +0.3 -> +3.1 delivered; the 484 step goes +2.5 -> +4.4 / +4.3. Bar 159 still rises every beat (-11.5, -10.4, -10.2, -9.6), and the downbeat of 160 becomes the loudest beat of the bar (-6.7). The limiter stays at 3.0 dB because the top peak, 1.519 at qn 637.9, lies outside the step; the 636.0-636.5 window peaks at 1.12 now. Delivered 160-over-122 margin 0.72 dB (unchanged), span 20.4 dB.

Articulation part, for critic A and the actor to decide: let Vln I/II and Vc start 636 (and the fff 484) as fresh Sus MAX strokes with the entry lead, not legato targets. The downbow is printed in Vln I.

Criterion: M step at 636 at least +3 dB delivered; climax order 160 > 122 kept; limiter at most 3.0 dB.

## 2. Bars 60-62: the crescendo plays backwards, and the subito p is only 3 dB (measured)

Where: qn 236-248. Hairpin `< ` 236-244 on Vln I, Vln II, Vla, Cl1, Bn2, Hn2, Hn3, Hn4 and Cb (mf), then "sub. p" on every part at 244. HISTORY has listed this as open since c02.

Evidence:
- **The tune falls through the crescendo.** Vln I per-note levels (onset+0.08 s to min(end, +1.5 s)) are 236 -30.7, 239.5 -35.8, 240 -35.1, 242 -38.2, 243 -37.5 and 243.5 -37.5 dB, a fall of 7 dB.
- **The volume envelope works against the hairpin.** Vln I's envelope falls from +4.0 at 236 to +1.0 at 242-243, against the hairpin's +2 dB hpgain. The steps fall at note onsets (-0.6 dB each at 239.5, 241.7, 242.7) and there is a -2.2 dB slide over 239.7-240.5. This is the LEAD_SPANS (220, 244) phrase-top contour by pitch on a descending line. The c22 rule turns that contour off only inside soft hairpins, and this one starts at mf.
- **The master does not rise.** Beats read 60: -25.0 -24.1 -24.5 -26.4; 61: -26.2 -25.7 -25.4 -26.1; 62: -28.4 -28.6 -28.8 -27.9. The delivered file shows the same drop of about 2 dB.
- **The subito p is shallow.** Over qn 242-244 to 244-246 the master falls only 3.3 dB. Horn 3 rises +3.5 dB at the sub. p and becomes the loudest stem (-37.4). Vln II falls 0.5 dB and Vln I 3.0 dB.

Fix:
- (a) In `score_to_parts.py`, switch the lead-line pitch contour off inside every crescendo hairpin, not only soft ones (extend the c22 rule).
- (b) In `build/score_config.py`, raise the 236-244 hairpin gain to about +4 dB more on every track carrying it. Use a hpgain override or a ramped role on the nine tracks that rises from 0 at 236 to +4 at 244 and falls to 0 at the sub. p onset (0.03 s).
- (c) In `build/roles.json`, add an `_all` row [244, 247.5, -3] (release by 248) for the sub. p, plus Horn 3 [244, 247.5, -3] extra.

Simulated with (b) and (c) as levels (`sim4.py`): bar 61 beats go to -24.8 -23.3 -22.9 -23.0 (61 is now louder than 60), and bar 62 to -27.9 -32.4 -32.1 -30.9. The step into the sub. p becomes 5-9 dB. The contour change (a) adds to this; I did not simulate it.

Criterion: Vln I's last two notes of bar 61 at or above its 236 note; master beat 4 of 61 at least 1 dB over beat 2 of 60; at least 6 dB from 243-244 to 244.5-246.

## 3. The mf fugato of bars 85-87 is in the quietest 10% of the delivered file, under the pp coda; the span cannot be fixed by the ride (measured; one judgement inferred)

Where: qn 336-352. Violoncellos subject mf with Cb pizz. mf; Vla and Bn1 enter mf at 348.

Evidence:
- **Delivered levels.** Delivered bar M for 85/86/87 is -29.4/-31.2/-30.7 dB. The pp coda chorale (bars 175-178) measures -26.6/-26.5/-26.2/-25.8, so the printed mf passage sits 4.5 dB under the pp passage. On the master the gap is 85-87 -32.6/-35.9/-36.0 against 175-178 -32.6..-31.8.
- **The subject loses level.** The Vc stem falls 4.5-5 dB from the subject's head to its continuation (bar 85 -35.5, 86 -40.0, 87 -40.6). The Vc's own mf median is -37.2.
- **Bottom decile.** Bars 85-87 make up about 6 of the 43 s in the delivered p10 decile. The rest are bars 1, 4, 5, 14, 34, 108, 127-128 and 182.
- **The ride is not at its cap here.** Its gain is 5.9-7.8 dB in bars 85-87, because the ff of 82-83 is inside its 3 s smoothing. The cap matters only in bars 1-6 and 180-182. Raising `CAP_DB` 10 -> 12/14 gives a span of 20.0/19.8 dB, so the cap is not the lever.
- **Real orchestra (inferred).** A cello section's mf subject should not be quieter than a pp brass, clarinet and string chorale.

The pp-to-mf range is narrow across the movement. By printed dynamic, the median master bar M is pp -33.9, p -32.2, mp -33.5, mf -31.1, f -26.5, ff -16.3 dB. The ride also compresses the long crescendos: bars 9-12 +13.1 -> +7.9 dB, 111-117 +12.1 -> +7.4, 156-158 +6.0 -> +3.8. Further ride compression to reach the 19 dB span would cost those crescendos, so the remaining span work belongs in the mix.

Fix (`build/roles.json`, level only):
- Violoncellos [338, 348, +3] on top of the existing [336, 358, +3], so the continuation of the subject keeps the head's level.
- Double basses [336, 348, +2].
- Violas and Bassoon 1 [348, 358] +3 -> +5.

Simulated as +3 dB on the master over 336-352 (`simlift.py simA`): span 20.3 -> 19.9 dB, LRA 15.1 LU, limiter 3.0 dB. Adding +3 dB on bars 1-5 and 14 (`simB`) gives 19.6 dB, but it flattens the ppp opening. I do not recommend it before a listener confirms the opening is too quiet.

Criterion: delivered bars 85-87 at or above the bar 175-178 level; the Vc stem in bars 86-87 within 2 dB of bar 85.

## 4. Final chord: the Horn 3 fundamental pulses at the breath-split spacing and sets a 4.5 s period in the master (measured; item 7)

Where: qn 720-728 (bars 181-182), Horn 3 (C4) and Horn 4 (G3), `BREATH_SPLIT_AT` in `build/score_config.py`.

Evidence:
- **Master.** I folded 50 ms frames over 720.8 s-727.7 s, detrended over 6 s. The master's 250-274 Hz band has an autocorrelation of 0.63 at 4.50 s and p95-p5 of 13.4 dB. In that band Horn 3 is the largest contributor (band mean 11.2 against the celli at 6.0). The master's 100-300 Hz broadband autocorrelation reads only 0.30, so the c05 check missed this.
- **Horn stems.** Horn 3 and Horn 4 show 100-300 Hz p95-p5 of 17.6 and 15.8 dB, with autocorrelation 0.91 at 4.6 and 4.2 s.
- **Where the troughs come from.** The time series shows a fundamental trough of 12-14 dB 1.1-1.5 s after each piece's onset (Horn 4 troughs at 1.5, 5.2 and 9.2 s). The splits are about 4.2-4.6 s apart (Horn 3 at 723.5/726.0, Horn 4 at 723.0/725.5), so each split restarts the same sample shape and recreates the period. The overall level moves only ±2 dB, so this is a slow change of tone colour, the kind Dan heard on movement II's final chord.

Fix: in `BREATH_SPLIT_AT`, use three splits per horn at irregular spacing, with no piece over 4.5 s and no two equal. Example: Horn 3 at [722.3, 724.6, 726.6], about 2.8 / 3.2 / 4.0 / 2.8 s. Offset Horn 4 by half a trough, for example [721.6, 723.8, 725.9]. Keep the -3 dB dip, and check that the dips (up to 8.9 dB on the stem in c05) do not stack.

Criterion: master 250-274 Hz detrended autocorrelation at 3.9-4.7 s under 0.35, and Horn 3's C4 band p95-p5 under 10 dB.

## 5. Bars 126-129: the tam-tam rings past its printed "damp", and the clarinet's p< does not grow (measured)

Where: Tam-tam qn 504 onward. Clarinet 1 504-512 (solo p <, to mf at 129).

Evidence:
- **The tam-tam is not damped.** The note ends at 504.19, but the stem decays only about 2 dB per qn: 504 -39.0, 505 -40.7, 506 -42.7, 507 -43.3, 508 -45.2, 509 -47.3 dB. At 505 it is as loud as the entering Cl1 solo (-37.0) and 7-8 dB under the master. The c05 role [487, 512, +4] holds the release tail up by +6 dB until qn 512. "Damp" is printed at bar 127.
- **The clarinet does not crescendo.** Cl1 measures -39.3 -> -39.7 dB over its printed p< (504-512), while the pedal under it grows (Hn4 +6.5, Timp +10.1, Cb +6.0). The master's 127-128 beats are flat to falling (-32.1 ... -32.1), against the score's pp/p < mf.
- **Damping alone is not enough.** Simulated alone (`sim5.py`: -24 dB over 0.5 s from 504.2), the damp lowers the bar 127 beats by only 0.4-1.0 dB.

Fix:
- Tam-tam roles in `build/roles.json`: end both rows at 504.2 ([484, 504.2, 2], [487, 504.2, 4]).
- Add a damp: a `PERC_MAP` "Tam-tam" option `damp_at: [504.2]` in `build_perc_track`, a volume fade of -24 dB over 0.5 s, so the sample's slow release does not ring on.
- Clarinet 1: add (504, 512) to `HP_SOFT_EXTRA_SPANS` with a +4 to +5 dB ramp, and turn off the pitch contour there (same rule as finding 2).

Criterion: tam-tam stem at least 15 dB under the master by 505.5; Cl1 at 511-512 at least 4 dB over 504.5-505.5.

## 6. Smaller: the subito p at bar 84 and the end of the movement keep their shape; the delivered limiter has no headroom left (measured)

I checked these and they hold:
- The sub. p at 84 drops 14 dB in the master (-14.7 -> -28.7).
- The coda's final ppp bar is 5 dB under bars 179-180 in the delivered file (-27.5/-26.7 -> -31.9). The SCORE_END fade (-2 at 727.5, -10 at 728) ends the fermata without a click.

Any loudness added to the climaxes must stay outside qn 637.5-638 (peak 1.519: Vln I Ab6, Horn 1, Violas, Trombone 1), or the limiter goes past 3 dB. The finding 1 step was placed with this in mind. If the actor wants margin, a -1 dB notch on Vln I over 637.6-638.1 (the single join peak, as in movement II c18) would lower the limiter, but it is not needed for the findings above.

Do not touch:
- The bar 123-126 diminuendo shape and the p arrival at 126.
- The climax order (160 > 122 > 169) and FFF_HOLD_CAP.
- The sub. p at 84.
- The suspended-cymbal timing into the crash (it peaks at the downbeat) and CAESURA 636.
- GENTLE_ACCENT on brass, winds and strings (accent 2-5 kHz attack minus body at most +3.2 dB).
- The delivery chain settings (ratio 2.5, cap 10). Changing the cap does not help, and more ratio costs the long crescendos.
- The AUTO_REBOW rows and fitted shapes, and the re-strike plans.
