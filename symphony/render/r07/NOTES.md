# r07: timpani rolls written as several notes become one roll, Iowa and Philharmonia brass, cor anglais and contrabassoon, bass drum for movement III

Actor 7. Built from r06 and critic 6's plan (critics/c06.md, section 9). Test inputs (TESTSET.md, refreshed for this
cycle): movement I `mvt1/v203`, movement II `mvt2/v82`. Before = r06 rendered unchanged on these inputs
(r07/meas/r06-on-new/: MP3s and MIDIs; tables from the same scripts in r07/meas/r06-on-new/m1 and m2; a re-render on
2026-10-12 decoded bit-identical to those MP3s). After = the final r07 renders (r07/out-m1.mp3, out-m2.mp3; MIDIs
r07-m1.midi, r07-m2.midi; tables in r07/meas/m1 and m2, r07/meas/mixtable.md, r07/meas/mixonsets.md).
Tags: [measured] read from those tables; [inferred] reasoned, not measured. Nobody listened.

This cycle ran over several sessions (2026-10-10 to 2026-10-12); the first ones were cut off before writing notes. On
2026-10-12 each inherited change was checked against r06 by measurement (test renders A, B, C in /tmp, section 5)
before it was kept. The movement III percussion item was added on 2026-10-12.

## 1. What changed, by plan item

### Item 1. One roll is one roll, however it is written: done (Dan's timpani rule)
- lib/marks.py `roll_chains()`: timpani tremolo notes that follow each other with no gap (a new untied note each bar, or
  a change of drum) form one roll. The merged roll carries the printed dynamics and hairpins of all its notes as inner
  events (`_hp_state`), so `roll_curve` (settle, soft cap, hairpins followed at 3 dB per step) runs once over the whole
  chain. `marks.rolls(..., tpb=)` and the balance roll rule use the chains (render.py passes the tick grid).
- articulate.py: the chain's first note plays the whole chain, with one start stroke. Notes of the chain on the same drum
  become one held note. At a change of drum, the earlier drum ends on a new roll channel 2
  (sfz/timpani-roll-r07-cont.sfz: the roll loop without the closing stroke) with a 30 ms overlap, and the new drum's roll
  continues under the same CC11 curve. The later notes no longer restart the dynamic trims. Bug fixed in roll_curve: the
  last grid point belonged to no segment, so every roll ended with a 0 dB jump held through the 0.5 s release.
- lib/balance.py: a roll longer than a bar may lead only where the timpani is printed louder than every sounding stem.
  Where it is printed softer than the loudest printed stem, it sits a further `roll_margin_step_dB` (1.5) under that
  stem for each printed step. `roll_margin_cresc_dB` 0.5 -> 1.5.
- Sources: critic 6 section 8.5 (https://forum.vsl.co.at/topic/53560/best-practices-to-get-dynamic-timpani-rolls-in-sychron-sound-nice ;
  https://forum.vsl.co.at/post/250901 ; https://forum.vsl.co.at/post/288710 ; https://forums.steinberg.net/t/timpani-roll-dynamic/107904).
- Result: v203 has 8 chains (3 with a change of drum) and v82 has 2 [measured, articulate report]. Timpani minus the
  loudest other stem in roll bars (meas/scripts/rollcheck.py): m1 max +4.8 -> -1.0 dB, timpani loudest in 6 -> 0 of 47
  bars; m2 max +2.0 -> -2.9 dB, loudest in 4 -> 0 of 15 bars [measured]. Printed crescendos inside chains still rise
  (v203 40-43, 166-169) [measured, rollcheck].

### Item 2. Brass off FluidR3: done (trumpets, trombones, bass trombone and tuba from Iowa; horns from Philharmonia)
- Trumpets 1-2, trumpet 3, trombones 1-2, bass trombone, tuba: University of Iowa MIS pre-2011 chromatic runs pp/mf/ff,
  cut by build_iowa.py `--pitch-onset --fade-in 0.005 --pan-spread 35` (assets/iowa/*-r07). They use the same player
  maps (L/R/a2) as the winds. Levels are matched to the FluidR3 stems per printed dynamic with meas/scripts/engcal.py.
- Horns: the Iowa horn set has gaps in the instrument's core range (critic 6), so the horns use the Philharmonia Orchestra
  samples instead (one file per pitch and dynamic, p/mf/ff, 1.5 s notes, complete from A#1 to F5). A new script,
  r07/build_phil.py, prepares them: decode, onset, pitch tune, cut at 45 dB down, level the layers, sustain loop. It
  writes the same SFZ format and L/R/a2 maps as build_iowa.py.
- Calibration [measured, engcal on v203]: at the first gain, Philharmonia minus FluidR3 horns was p -3.9, mp -2.4,
  f -1.7, ff -2.0 dB. The gain was set so that f/ff sit about 0.5 dB under the FluidR3 level, because the horns were
  critic 6's top inversion offender. The p/mf trims (and pp for horns 3-4) were raised again after test B, where the
  v82 opening horn solos (bars 4-14, pp/p) had become 2-8 dB quieter than in r06.
- Tuning of the new sets in the rendered stems (critic 5's pitchcheck.py, dry): every brass stem's median is within
  -5.1..+3.9 c, p90 |deviation| <= 7.6 c, and no note is more than 15 c out [measured].
- dB per printed step, m1 (stemcmp): Horns 1-2 1.69 -> 1.88, Horns 3-4 2.29 -> 2.51, Trumpets 1-2 1.36 -> 2.27,
  Trumpet 3 2.19 -> 3.01, Trombones 2.29 -> 2.79, Bass trombone 2.64 -> 3.20, Tuba 2.11 -> 2.75 [measured].
- Sources: https://theremin.music.uiowa.edu/MIS.html ; https://theremin.music.uiowa.edu/MISBbtrumpet.html ;
  https://theremin.music.uiowa.edu/MIStenortrombone.html ; https://theremin.music.uiowa.edu/MISbasstrombone.html ;
  https://theremin.music.uiowa.edu/MIStuba.html ; https://philharmonia.co.uk/audio-sound-samples/ ;
  https://github.com/skratchdot/philharmonia-samples/

### Item 3. Cor anglais and contrabassoon off FluidR3: done
- Philharmonia cor anglais (pp/mf/ff layers) and contrabassoon (p/mf/ff), built with build_phil.py, with engcal gains
  (cor anglais -4 dB and contrabassoon -3.5 dB from the first guess) and the `src2` two-position room (item 8). Cor
  anglais p +1.5 dB after test C, where v203 espr. 171-173 had dropped to -2.2 dB against the cellos.
- dB per step, m1: cor anglais 1.76 -> 1.84, contrabassoon 1.97 -> 2.70. Tuning: cor anglais median -1.1 c,
  contrabassoon +0.1 c [measured].
- Melodies (melody.md, vs the loudest other stem): m2 cor anglais solos 41-44 +3.6 -> +3.7 dB and 47-53 +6.3 -> +3.9 dB;
  m1 5-7 +3.4 -> +2.8 dB and 171-173 -0.4 -> -0.6 dB [measured].

### Item 4. Note lengths: investigated, not changed
- The extra length comes from the room, not from the notes. On the dry synthesis stage the detached audible ratio is
  0.99 (oboes) and 1.06 (Vln I); with the room it is 1.53 and 1.32 [measured, meas/scripts/artq.py on v203 r06 stems].
  Oboes without r06's two-IR room (src2) give 1.35, and src2 with the send 2 dB lower gives 1.48 [measured]. So r06's
  lengthening is the tail of the second source IR. Removing it would undo the wind width critic 6 accepted (oboe L/R
  0.78 -> 0.87). Kept; listed under section 4.

### Item 5. Exposed soft solos (spot microphone): done
- lib/balance.py `spot_lift`: where a marked melody is printed <= mf and at most 4 stems sound, all sounding stems in
  the bar rise together, keeping their relative levels. The target is the median loudness of bars printed at the same
  loudest dynamic, minus 1 dB; the lift is at most 3 dB and goes through the 1.5 s faders. Bars lifted: m1 5, 34, 73-75,
  107-108, 171-174; m2 6, 8, 31-36, 68-69, 85-86 [measured, balance report].
- Source: critic 6 section 8.4 (https://imusician.pro/en/resources/blog/how-to-record-mix-and-master-classical-music ;
  https://beatkitchen.io/guides/orchestral/11-orchestral-mixing/).
- m2 LRA 20.5 -> 20.6; the target of 19.5 was not reached. The soft horn solos on the new samples had pushed it to 21.2
  in test A, and the horn trims brought it back [measured].

### Item 6. Section players not on the same millisecond: partly done
- build_iowa.py and build_phil.py write player 2 (the -R map) 8 ms late and the second a2 player 12 ms late. This is a
  fixed offset per player, as in critic 6 section 8.3
  (https://vi-control.net/community/threads/how-precise-in-terms-of-milliseconds-and-db-are-professional-musicians-vs-the-score.90243/post-4513796 ;
  https://forum.vsl.co.at/post/290360). String divisi offsets were not done (the strings are VPO).
- Steepest mix onsets, median: m1 2.44 -> 2.49 dB/ms (p90 3.71 -> 3.49), m2 2.10 -> 2.22 (p90 3.74 -> 3.61). Onset crest
  m1 2.3 -> 1.9 dB, m2 3.2 -> 2.7 dB [measured, mixonsets.md]. The target median of <= 2.2 dB/ms is not met in m1.

### Item 7. Accent outliers and sf: done
- Per-stem accent weight: violas 0.5; cellos and basses 1.0 + bump 0.5; bass clarinet 0.5 + 0.5; Vln II 2.5;
  bassoons 1.5. The new sample sets cross into the ff layer on an accent, so they get less: trombones, bass trombone,
  tuba and contrabassoon 0.5 + 1.0; horns 3-4 and trumpet 3 1.0 + 1.0.
- sf: `sf_mode weight` (the plain-note base velocity + `sf_level_dB` 1.0, plus a 3.0 dB CC11 bump with the accent's
  rise and fall) replaces the velocity boost and dip. The first setting (level 4 dB) held +4 dB through whole sf >
  decresc notes: in test B, v203 bars 41-42 (a tutti sf) rose 4 dB and became the movement's loudest moment (S max
  +8.2 LU). Level 1 + bump 3 keeps the sf an attack.
- Accents vs the neighbouring plain notes (critic 6's accents2.py, wet, m1): all stems +2.6 -> +2.3 dB peak, crest
  +1.4 -> +1.3 dB. Violas +5.0 -> +3.6, cellos +4.0 -> +2.3 (crest 3.0 -> 2.3), bass clarinet crest 2.9 -> 1.6. Brass
  +1.8 to +3.0, trumpets +2.8. Timpani +4.7 (r06 +5.0; strokes, not changed) [measured]. m2 has no usable accent pairs.

### Item 8. Width and depth: partly done
- `src2` for bass clarinet (S7), cor anglais and contrabassoon (S6), trombones (S7) and trumpets (S8); width 1.0.
- Mix L/R correlation m1 0.64 -> 0.63, m2 0.58 -> 0.59 [measured]. Per-family early reflections were not done.

### Extra item (2026-10-12). Movement III: drum chords, \tweak, ties, bass drum: done
- perc.py drops `\tweak <property> #'<value>` (it only affects the printed page) and plays a drum chord such as
  `<cymc bd>1` as one stroke per drum. A tie (`cymc~`, also inside a chord) continues the stroke: there is no new
  stroke, the written lengths add up, and the sound stops at the end of the tied length (damped) instead of after the
  l.v. time. The same tie rule changes movement I: the tam-tam tied over 5 bars (v203 dev; the score's comment says the
  written length shows where the sound stops) was struck 5 times in r06. It is now struck once and damped at the end of
  its written length [measured, render.midi drum notes]. Source:
  https://lilypond.org/doc/v2.24/Documentation/notation/common-notation-for-percussion
- Bass drum (`bd`, key 36): the VSCO 2 CE concert bass drum (CC0; soft and loud hits, 2 round robins each) in
  sfz/perc-r07.sfz, logged in assets/README.md (https://versilian-studios.com/vsco-community/ ; VPO 3.2 archive on archive.org).
- mvt3/v14 (2/2) renders end to end into /tmp, with 9 percussion strokes. The bass drum sounds at bar 223 and at
  bar 247 + 23 (the drums stem's energy below 120 Hz is -31/-34 dB there, against -66 dB at strokes with cymbal only)
  [measured]. I -20.0 LUFS, LRA 19.7, true peak -1.5 dBTP, no crash. Not measured further, because it is not a test input.

## 2. Before / after (r06 on the new inputs -> r07)

### Movement I (v203)
| measure | r06 | r07 | tag |
|---|---|---|---|
| LRA LU | 17.5 | 17.7 | [measured] |
| short-term p10 / p50 / p95 / max rel I | -13.4 / -4.8 / 4.1 / 6.7 | -13.4 / -4.7 / 4.4 / 7.1 | [measured] |
| Spearman bar loudness vs printed | 0.82 | 0.83 | [measured] |
| balance inversions all / outside hairpins | 348 / 179 | 279 / 121 | [measured] |
| inversions, worst stems | Hn12 61, Timp 35, Cl 34, Hn34 32 | Hn12 56, Hn34 38, Cl 31, Vla 30, Timp 25 | [measured] |
| bars printed <= mf louder than the median f bar | 12 | 13 | [measured] |
| melodies >= 0 dB vs loudest / >= -6 dB vs sum (of 20) | 11 / 16 | 10 / 17 | [measured] |
| timpani in roll bars: loudest / within 1 dB / max | 6 / 7 / +4.8 | 0 / 0 / -1.0 | [measured] |
| accents vs neighbours, all stems: peak / crest dB | +2.6 / +1.4 | +2.3 / +1.3 | [measured] |
| brass dB per printed step (Hn12 / Tpt12 / Tbn12) | 1.69 / 1.36 / 2.29 | 1.88 / 2.27 / 2.79 | [measured] |
| mix onsets steepest median / p90 dB/ms; crest dB | 2.44 / 3.71; 2.3 | 2.49 / 3.49; 1.9 | [measured] |
| 1/3 oct vs Brahms mean 62 / 79 / 794 / 6350 / 8000 Hz | -2.4 / -4.4 / +2.1 / -0.2 / +0.7 | -2.3 / -5.2 / +2.6 / +0.8 / +2.5 | [measured] |
| mix L/R correlation | 0.64 | 0.63 | [measured] |
| detached audible ratio Fl / Ob / Cl / Vln I (wet) | 1.51 / 1.53 / 1.32 / 1.32 | 1.51 / 1.53 / 1.34 / 1.32 | [measured] |

### Movement II (v82)
| measure | r06 | r07 | tag |
|---|---|---|---|
| LRA LU (target <= 19.5) | 20.5 | 20.6 | [measured] |
| short-term p10 / p50 / p95 / max rel I | -13.3 / -8.1 / 7.2 / 9.5 | -13.4 / -8.3 / 7.3 / 9.6 | [measured] |
| Spearman | 0.72 | 0.72 | [measured] |
| inversions all / outside hairpins | 53 / 12 | 48 / 13 | [measured] |
| melodies vs loudest / vs sum (of 15) | 10 / 13 | 10 / 13 | [measured] |
| timpani in roll bars: loudest / max | 4 / +2.0 | 0 / -2.9 | [measured] |
| mix onsets steepest median / p90; crest | 2.10 / 3.74; 3.2 | 2.22 / 3.61; 2.7 | [measured] |
| 1/3 oct 62 / 79 / 794 / 6350 / 8000 Hz | +0.2 / +0.5 / -0.8 / +1.0 / +2.5 | +0.3 / -0.2 / -0.6 / +1.4 / +3.2 | [measured] |
| mix L/R correlation | 0.58 | 0.59 | [measured] |

Both outputs are clean: both MP3s are full length (434.5 s and 350.3 s, as in r06), I -20.0 / -20.1 LUFS, true peak
-1.6 / -1.5 dBTP, 0 clipped samples [measured]. The largest sample-to-sample jump in m1 is the crash cymbal's own attack
at bar 160; the raw VSCO sample has a jump larger than its peak [measured].

## 3. What got worse
- Premaster "isolated HF spikes" (critics/c02/scripts/clicks2.py): m1 0 -> 6, m2 0 -> 81. Of these, 80 are in the ff
  trombone / bass trombone bars near 230-240 s or in the contrabassoon [measured]. The same detector finds 80-830 such
  spikes in the raw Iowa trombone and bass trombone samples, and 4-39 in the Philharmonia contrabassoon files: they are
  the lip-buzz and reed pulses of close-miked low brass and reeds, not render discontinuities. An air shelf on the
  stems did not reduce the count [measured]. The four Brahms references give 3-13. Inferred: at ff the low brass
  sounds more rasping than in a hall recording. Open.
- m1 melodies at or above the loudest other stem: 11 -> 10 of 20. In bars 55-62, Vln I, clarinets and horns are all
  marked melodies at p and swap places [measured]. Bars printed <= mf louder than the median f bar 12 -> 13 (bar 39 is
  new) [measured].
- m1 S max +6.7 -> +7.1 LU; 79 Hz -4.4 -> -5.2 dB; 6.3-8 kHz +0.7 -> +2.5 dB over the Brahms mean (the Iowa brass is
  brighter) [measured].
- Soft brass on the new sets: trombones at p -6.4 dB, and bass trombone/tuba at f -4 to -5 dB, against Violins I at the
  same printed dynamic (stemcmp; few bars) [measured]. These levels come with fewer inversions.
- m2 LRA 20.5 -> 20.6, and the median mix onset is slightly steeper in both movements [measured].

## 4. Open
- Plan 4: the long detached notes come from the second IR's tail (src2), not from the notes. Still to do: a shorter src2
  pre-tail, or measuring on the direct sound only. Flute and Vln I staccato 1.99 (n 11).
- m2 LRA 20.6 (target 19.5); m2 Spearman 0.72; exposed soft lines in m2 53-64 still -8 to -11 dB vs the sum.
- Low-brass pulse spikes (section 3); m1 high band +2.5 dB at 8 kHz.
- Horns are still the top inversion stems in m1 (56 + 38); their f/ff trims could be refit with invsim.py.
- String divisi timing offsets and per-family early reflections (plan 6, 8); timpani stroke accents +4.7 dB.
- build_phil could not measure the pitch of the contrabassoon F1 and D4 samples, so no tune was applied to them (the
  rendered median is +0.1 c).

## 5. Tuning history (test renders in /tmp, all deleted)
- A (all inherited r07 code + Philharmonia + percussion): m1 inversions 283, rolls 0 loudest; m2 inversions 48 but
  LRA 21.2; brass/contrabassoon accents +5 to +8 dB; soft brass 4-8 dB under Vln I.
- B: brass accent weights lowered, soft brass trims raised: m1 inversions 270, accents <= +3.6 dB. Found the sf +4 dB
  whole-note problem (S max 8.2) and m2's quiet horn solos.
- C: sf level 1 + bump 3, horn soft trims: m1 inversions 279, S max 7.1; m2 LRA 20.6, inversions 47. Final = C +
  cor anglais p +1.5 dB.
- Oboe stem A/B for item 4 (src2 on/off, send -2 dB), and an air-shelf test on the trombone stems for the spike count
  (no effect, not kept).

## 6. Generality
- meas/scripts/generality.sh (r07 paths, chains): mvt1/v221 22 melodies / 13 rolls, mvt2/v169 20 / 4, mvt3/v14 11 / 8.
  No staff lacks a config entry and no notes are unmatched [measured]. Nothing depends on bar numbers.

## 7. Rebuild
```
cd /mnt/project-files/symphony/render
# sample sets (only if missing): Iowa brass, Philharmonia horn / cor anglais / contrabassoon
python3 r07/build_iowa.py Trumpet assets/iowa/src/trumpet assets/iowa/trumpet-r07 r07/sfz/trumpet-iowa.sfz --pitch-onset --fade-in 0.005 --pan-spread 35
#   (the same for trombone, basstrombone, tuba)
python3 r07/build_phil.py "French horn" assets/philharmonia/src/french-horn assets/philharmonia/horn-r07 r07/sfz/horn-phil.sfz --prefix french-horn --dyns piano,mezzo-forte,fortissimo --pan-spread 35
python3 r07/build_phil.py "Cor anglais" assets/philharmonia/src/cor-anglais assets/philharmonia/coranglais-r07 r07/sfz/coranglais-phil.sfz --prefix cor-anglais --dyns pianissimo,mezzo-forte,fortissimo
python3 r07/build_phil.py Contrabassoon assets/philharmonia/src/contrabassoon assets/philharmonia/contrabassoon-r07 r07/sfz/contrabassoon-phil.sfz --prefix contrabassoon --dyns piano,mezzo-forte,fortissimo --vel 35,52
# renders (one at a time; check ps aux | grep render.py first)
python3 r07/render.py --score /mnt/project-files/symphony/mvt1/v203 --out r07/out-m1.mp3 --work /tmp/render-07-m1
python3 r07/render.py --score /mnt/project-files/symphony/mvt2/v82 --out r07/out-m2.mp3 --work /tmp/render-07-m2
cp /tmp/render-07-m1/render.midi r07/r07-m1.midi; cp /tmp/render-07-m2/render.midi r07/r07-m2.midi
# measurements: meas.sh, then extra.sh (accents2 wet, rollcheck, rollchains, inversions by stem, no-hairpin, pitch, summary)
bash r07/meas/scripts/meas.sh /tmp/render-07-m1 r07/out-m1.mp3 r07/meas/m1 r07-m1
bash r07/meas/scripts/extra.sh /tmp/render-07-m1 r07/meas/m1 r07-m1
python3 critics/c05/scripts/mixtable.py r06-m1=r07/meas/r06-on-new/m1 r07-m1=r07/meas/m1 ... > r07/meas/mixtable.md
python3 r07/meas/scripts/engcal.py WORK STEM_BASENAME "STAFF" CONFIG_A CONFIG_B   # level calibration between engines
# movement III check (not a test input)
python3 r07/render.py --score /mnt/project-files/symphony/mvt3/v14 --out /tmp/m3.mp3 --work /tmp/render-07-m3
```
