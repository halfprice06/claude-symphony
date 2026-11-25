# Cycle 29, critic C (blend and space): the c28 render

Material: `cycles/c28/render/` (31 dry stems, 4 return stems, master; the master is the exact sum of the 35 stems, residual -inf dB), `cycles/c28/mvt3-mockup-c28.mp3`, `build/parts.json`, `build/mix.json`, the Opus states decoded from `mvt3-v600-mockup.rpp` (read only), `build/mockup-events.tsv`, the Dvořák 9/i reference, the stored Brahms 1/ii and 4/ii shares (`metrics.json`), and Movement I's c62 stems and mp3. Scripts were my own (numpy / soundfile / ffmpeg) in the scratch folder, which has been deleted. "Measured" means a number from the files. "Inferred" means reasoned, not tested.

## Manual notes

MANUAL-READING.md has no row for cycle 29, so there was no assigned reading. I read the pages behind my findings and used MANUAL-GAPS.md.

| Manual (PDF page) | What it says | Where it applies here | Followed? |
|---|---|---|---|
| p.141, 4.2.6 Channel Routing | "Mono From Left outputs the left channel to a dual mono output, discarding the right channel." | Horns 1-4 run with `channel_map` 2 (c19 / c25: against mono-sum losses of up to 7.7 dB on B flat 4). | Yes, as set. The side effect is finding 1: the four horns are one mono point. |
| p.141, 4.2.7 Stereo Double | Widens the stereo spread. It "only works when 'Stereo' is selected" as the channel source. | It could widen the mono horns. | Not used. It is untested with Mono From Left and is an Opus state change, so it is not proposed for the last cycle. |
| MANUAL-GAPS #4 (p.138-139) | Mid instead of Close mics on the winds, then the horns. | Exposed wind solos. | Still untried. Not proposed: it needs a full rebuild and a re-level. |
| MANUAL-GAPS #7 (p.89-90) | Half-section DIV patches for soft divisi. | Violins I "4 soli" at qn 485-511 play on the full 1st Violins KS Master. | Not followed (memory). It cannot land safely in one cycle. |
| MANUAL-GAPS #13 (p.100) | The bass trombone uses tenor-trombone samples. | The Bass trombone is on the 1TB KS Master. The library has no solo bass trombone, only "2 Trombones and 1 Bass Trombone". | No change possible. |

## Where the room stands (measured; nothing below needs changing)

- **Wet and dry, family by family.** For each return stem, minus the dry stems of the tracks that feed it:
  - Horns alone in bars 9-25 and 68-83: -11.5 dB (p10-p90 -13.7..-9.9).
  - Trumpets alone: -11.5 dB.
  - Strings without the basses: -12.6 dB.
  - Winds: -10..-13 dB.
  - Percussion and harp: -7..-9 dB.

  So winds and brass sit a little further back than the strings, which is a plausible seating. The brass family as a whole reads -16..-18 dB only because trombones and tuba have no send (the Mulan / Howl rule).
- **Width.** Side/mid on the mp3, quietest quarter / middle / loudest tenth:
  - c28: -4.9 / -4.6 / -5.7 dB.
  - Dvořák: -6.4 / -5.8 / -5.2 dB.
  - Movement I c62: -5.2 / -5.3 / -5.4 dB.

  The image is as wide as the references.
- **Low end.** mp3 band shares, 20-150 / 150-500 / 500-2k / 2-5k / 5-10k Hz:

  | file | frames | 20-150 | 150-500 | 500-2k | 2-5k | 5-10k |
  |---|---|---|---|---|---|---|
  | c28 | quietest quarter | -10.8 | -4.0 | -3.3 | -12.7 | -30.6 |
  | Dvořák | quietest quarter | -12.7 | -4.0 | -3.0 | -13.7 | -33.1 |
  | c28 | loudest tenth | -10.6 | -5.6 | -2.7 | -10.3 | -25.2 |
  | Dvořák | loudest tenth | -10.8 | -4.2 | -3.4 | -10.9 | -24.9 |

  Against the stored Brahms shares the mix is lighter at 20-100 Hz (-12.7 against -8.5 / -7.9). The scherzo's "quiet passages 5 dB heavy at 20-150 Hz" does not apply here (+1.9 dB against Dvořák, lighter than Brahms).
- **Contributors to the low end.**
  - Double basses: 54-97 % of 20-60 Hz in every section.
  - Bass drum: 60-64 % of 20-60 Hz at 223 and the final chord.
  - Timpani: at most 16 % of 60-150 Hz (the final chord), 7 % at 223. That is under Movement I c50's 31 % fault level.
  - The bass drum does not set the master's peaks: removing it changes the peak at 888 / 1108 by +0.01 / +0.06 dB.
- **Percussion against the orchestra.** The crash pair (22in K Crash from the Cymbal Pairs folder) at 888 / 1048 / 1108 is 1.6 / 0.8 / 1.9 dB under the master in 6-16 kHz over its first 0.3 s. It decays 11 dB by 1 s and 20 dB by 2 s, as sampled. It is heard, it does not dominate, and it leaves the chorale entry clean.
- **Timpani: hard sticks are playing (coordinator check).** The decoded Opus state is "Timpani Hrd KS". The rows loaded are "Timpani Hrd Lng" (160 notes) and "Timpani Hrd Rls" (19 rolls). No felt row is loaded. The scherzo's felt-stick fault does not apply.

## 1. The four horns are one mono point: the section and its inner lines have no width (measured; listener effect inferred)

**Where.** Horns 1-4, the whole movement. The horn lines that matter most are the F1 off-beats (bars 11-26), the counterstatement (27-42), bars 68-83, the chorale (223-234, 255-264) and theme B at 211-218.

**What is wrong.** Since c19 / c25 all four horns use Opus Channel Routing "Mono From Left" (`build/mix.json` `channel_map` 2; manual p.141). That makes each horn a dual-mono signal: the Main pair (1.0, full width) becomes a centred mono image. The REAPER track pans then put all four in one place: -0.18 / -0.16 / -0.15 / -0.13.

**Evidence (measured).**
- **Correlation.** L/R correlation of the horn stems is 0.98-0.99 in every passage, and side/mid is -12.3 to -15.7 dB. Every other brass stem measures 0.69-0.86, the strings 0.21-0.45, and the oboes 0.99.
- **Position.** The four horns sit 2.8 / 3.2 / 3.2 / 3.5 dB louder on the left: one spot, the same spot as the flutes and clarinets (+2.4..+3.9 dB).
- **Movement I.** On the same 1FH samples without Mono From Left, the c62 horns measure correlation 0.68-0.70 and side/mid -6.0 dB.
- **The template.** It seats horns -0.13..-0.18 but leaves Main in stereo.

**Listener effect (inferred).** The four horns fuse into one close source left of centre. Where Horns 1-2 and 3-4 play different lines, which is most of the inner harmony, nothing in space separates them. That is part of Dan's "inner lines hidden" on AirPods.

**Fix.** Mix-only, no Opus state change, no rebuild: spread the track pans (`build/mix.json` tracks, `track_pan`):
- Horn 1 -0.08, Horn 2 -0.16, Horn 3 -0.24, Horn 4 -0.32 (section centre -0.20; the template's horns span -0.13..-0.18). Keep `channel_map` 2 (the mono-sum fix stays).
- **Level compensation.** The project pan law is `PANLAW 1` on PANMODE 5 tracks. If the stereo pan acts as a linear balance, the moves change each horn's power by +0.4 / 0.0 / -0.4 / -0.8 dB. Set `gain_db` Horn 1 1.2 -> 0.8 and Horn 4 1.0 -> 1.8. Do not raise Horn 3's `gain_db`: its envelope already peaks at exactly +24.0 dB, REAPER's limit (see the coordinator checks). Give Horn 3 its +0.4 dB with `stem_fix.py` after the render instead. These values are an estimate from the pan law.
- **Check after the render.** Measure each horn's level in the horn-only bars (9-25, 68-83) against c28. Correct any difference over 0.5 dB with `stem_fix.py` (level only).
- **Not proposed for this cycle.** Removing Mono From Left: it brings back the 7.7 dB mono-sum loss on B flat 4 and the per-pitch image wander of c19. Stereo Double: untested, and a state change.

## 2. The muted trumpet and the cor anglais do not stay fused in their unison: the lead swaps by up to 10 dB from note to note (measured)

**Where.** Bars 171-182 (qn 680-728): Trumpet 1 "con sord., dolce cantabile" doubles the Cor anglais note for note, both p, with the printed crescendo 719-724 (mf) and decrescendo 725-728.

**What is wrong (measured).** Trumpet minus cor anglais body level per note (0.12 s after the score onset to the next note, at most 0.8 s):
- The median is -3.4 dB, but the range is -7.3 to +3.2.
- The trumpet drops out of the pair on A flat 4 / B flat 4 (691: -6.8, 692: -7.3).
- It jumps 3.2 dB over the cor anglais on the top G5 at 724, even with the existing -4 dB region gain on G5. That is 6.6 dB over its own median: the muted trumpet pops out at the top of the phrase.
- The repeated pitches are consistent: E flat 4 at 683 / 686 / 715 / 718 measures -4.0 / -3.6 / -5.6 / -5.7. The deviations therefore come from per-pitch sample levels, not from round robin.

The tone match is reasonable: the trumpet's 1.5-3 kHz is 10 dB over the cor anglais, which is the mute's nasal band.

The Mute Sus row plays only in this solo (keyswitches at 662 / 679.8, back to "Sus Non Vib MAX" at 731.5). A per-pitch region gain on that row changes nothing else. It is an instrument-side static level, not a level move inside a note, so it falls within Dan's 11 Nov rule.

**Fix.** `build/mix.json` Trumpet 1 `region_gain_db`, the "Mute Sus" spec. Its `pitch_db` goes from {"79": -4.0} to:
- {"79": -9.0, "77": -2.0, "75": -2.5, "74": -1.5, "70": 3.0, "68": 3.5}.
- Each value is the measured deviation from the -3.4 dB median, rounded toward zero. G5 is left about 1.5 dB above the median because it is the phrase's top.

This is an Opus state change on one track: a full rebuild of Trumpet 1 only. **Check after the render:** per-note trumpet minus cor anglais over 680-728, range under 6 dB, median -3.4 +-1.

## 3. The bar-113 cut-off is 0.3 dB drier than the delivery band (measured; simulated)

**Where.** The tutti stop at qn 450.0 (bar 113), with the rest to 451.47.

**What is wrong.** On the mp3 the level falls 17.3 dB by +0.3 s (band 14.5-17; the other stops measure 15.8-16.9). The return-ride row `mix.json` `return_rides` [[447.5, 0], [448, 3], [451.3, 3], [451.4, 0]] gives only +3 dB to the hall at this stop (c26 cut it from +6.5).

**Evidence (simulated on the c28 stems).** The four return stems were scaled by the ride change and summed with the master, with the drop measured at +0.3 s as `stops24.py` does it:

| ride row | master drop |
|---|---|
| +3 (as rendered) | 17.9 dB |
| +4.5 from the cut-off | 16.9 dB |
| +5 from the cut-off | 16.6 dB |

-20 dB is still reached at 0.34 s in each case. The mp3 measured 0.6 dB under the master (17.3 against 17.9), so +4.5 dB should land at about 16.3 dB on the mp3.

**Fix.** `build/mix.json` `return_rides`: replace the 447.5 row with [[447.5, 0], [448, 3], [449.95, 3], [450.05, 4.5], [451.3, 4.5], [451.4, 0]].
- The extra 1.5 dB starts at the cut-off, so the chord's own hall before the stop is unchanged.
- The row still ends before the 451.47 entry (c26's reason for the cut).
- Mix-only, return faders only.

## 4. The family EQs carve 300-500 Hz out of the horns twice: the inner voice loses body (measured; the size of the fix is a judgement)

**Where.** Horns 1-4: family EQ bells at 315 Hz -5 dB (bw 1, the c09 addition) and 475 Hz -5.4 dB (bw 1.92, from the template), plus 821 Hz -4.

**What is wrong.** The horn's fundamental and second-partial region, about 250-700 Hz, is cut 5-8 dB, more than any other family. The wind cut is 447 Hz -5.1, the strings' 456 Hz -2.2. Against Dvořák (1/3-octave LTAS, normalised at 1 kHz) the master shows a dip at 400-500 Hz in every loudness class:
- loudest tenth: 400 Hz -5.3, 500 Hz -2.4;
- quietest quarter: -4.3 / -3.1.

Against both stored Brahms references the 250-500 Hz share is 1.1-1.5 dB low (-7.4 against -6.0 / -6.3) and the 100-250 Hz share 0.9-2.1 dB low. The single reference is lossy, but all three point the same way.

**Simulated (zero-phase, on the c28 stems).**
- **Halving all brass and wind cuts.** Horns 315 +5 or +2.5 dB, brass 475 +2.7, winds 447 +2.55, violas 315 +1.5. The master gains +0.9 to +1.1 LU, nearly all of it brass. This shifts the family balance too much for the last cycle. **Rejected.**
- **Halving only the horns' c09 bell** (315 Hz -5 -> -2.5). Horn 1 +0.9 dB and Horn 3 +1.0 dB broadband. That is the size of change this lens can recommend.

**Fix (optional; lower priority than 1-3).** `build/mix.json` groups.horn `family_eq` bell 315 Hz -5.0 -> -2.5 (mix-only, ReaEQ), with `gain_db` -0.5 on Horns 1-4 to keep the level change to about +0.5 dB. Check that the stops' 60-250 Hz tail share does not rise more than 2 dB (BRIEF, Movement I c50). It should not, since the bell is centred on 315 Hz.

Do this together with finding 1 only if the actor can check the horn levels against c28 after the render. Otherwise skip it.

## 5. The Largamente close still sits 1.4-2.4 dB under bar 255 on the mp3 (measured; coordinator item)

**Where.** Bars 271-273 (qn 1080-1092).

**Evidence.** Momentary maxima per bar on the mp3 (0.30 s head):
- 255: -8.7; 263: -8.3; 223: -8.2; final bar 278: -7.6.
- 271 / 272 / 273: -10.6 / -10.1 / -11.1. That is -1.9 / -1.4 / -2.4 against bar 255; the target is within 1.5.

**Fix.** The delivery ride row from 1079.5 (`parts.json` `ride_trims`, written by `score_config.py`): -2.0 -> -1.0 dB over 1080-1096. This is a delivery ride, which Dan's rule exempts. Expected:
- 271 / 272 / 273 at -9.6 / -9.1 / -10.1, i.e. -0.9 / -0.4 / -1.4 against bar 255.
- The final still leads 272 by 1.5 LU, 263 by 0.7 and 223 by 0.6.
- Do not go to 0 dB: bar 272 would come within 0.5 LU of the final chord.

Re-run `deliver_master.py` and check all six spec items.

## 6. Mono point winds: the scherzo's oboe / cor anglais finding applies, but leave it (measured)

**What was measured.**
- Oboe 1 / Oboe 2 / Cor anglais L/R correlation: 0.99 / 0.99 / 0.95. The bassoons measure 0.94-0.97.
- Each track's Close mic sits at its seat with width 0.05, and the oboes' Main is at 0.088 (-21 dB), as in the EW template (Ob Main -20.6 dB under Close).
- Movement I c62 measures the same (Oboe 1 0.99, Cor anglais 0.91).
- The winds' depth comes from R Winds, which is decorrelated (side/mid about 0 dB) and runs -10..-12 dB under the winds.

**Recommendation.** No change in the last cycle. Widening the Close mics (`width` 0.05 -> 0.15) is an Opus state change on several tracks, and nothing shows it is heard as a fault.

## Coordinator checks (only what this lens measured)

- **Envelope at +24 dB.** The volume-envelope maxima in the .rpp are 24.0 dB on Horn 3 (391 s, qn about 1018), 23.6 on Trombone 1 and 23.5 on Tuba. These are the values the build asked for, so nothing is clipped now, but the margin is zero.
  - Do not lower levels for it.
  - Add a build-time check in `tools/build_reaper.py` `vol_points` that fails the build when any envelope point exceeds 24.0 dB. Any later raise on these three tracks would then be caught instead of clipped silently.
  - That is why finding 1 gives Horn 3 its +0.4 dB through `stem_fix.py` and not through `gain_db`: in `gain_db` the envelope would ask for 24.4 dB.
- **Tenuto downbeats on Sus MAX (the scherzo c28 finding).** It partly applies.
  - Tuba tenutos at qn 112-122 (bars 29-31) peak 110-250 ms after the onset (a quarter is 357 ms). The downbeats still stand 5.5 dB over beat 2 (112 -28.2, 113 -33.7 dB).
  - Basses' tenutos at qn 976-983 peak 140-440 ms late, rising into the stringendo.
  - This is lens A's (the Portato / Marc Lng test). Not re-measured further here.
- **Bar-113 stop.** Finding 3.
- **Bars 271-273.** Finding 5.
- **Not measured by this lens.** The net-level gate list, Trumpet 1 989, the harp step at 952, the Horn 1 / Trumpet 3 fff trims and the accented slur second notes.

**Do not touch:**
- the return levels and send profile (horns / trumpets / strings -10, low brass / basses no send, perc and harp on R Perc), which measure family wet ratios of -10..-13 dB;
- the master width, which matches the references;
- the low end: basses' 72 Hz bell, 87 Hz notch, region gains, and the 40in bass drum at -4.4;
- the crash pair and its seat;
- the Timpani Hrd KS rows;
- the timpani's reduced EQ (at most 16 % of 60-150 Hz in a roll);
- the Mono From Left routing itself (keep it, only spread the pans);
- the c26 / c28 stop ceilings and the other return rides;
- the cor anglais crossfades and the trumpet's Mute Sus bandpass 250-8000 Hz.
