# r06: softer accents, clean bassoon/oboe starts, rebalanced Iowa winds, rolls keep their printed shape

Actor 6. Built from r05 and critic 5's plan (critics/c05.md, section 9). Dan's accent note (BRIEF.md, "Dan on accents":
"Accented notes have too much attack") was the top priority, together with the 3/4 bar length in the roll fade.
Test inputs: movement I mvt1/v156, movement II mvt2/v30. Before: r04 (Dan's listening copy, measured by critic 4) and
r05 (measured by critic 5). All r06 numbers come from the final renders made with the brief's commands, measured with
r06/meas/scripts/meas.sh plus critic 5's scripts (critics/c05/scripts). Tables: r06/meas/m1, r06/meas/m2,
r06/meas/mixtable.md, r06/meas/mixonsets.md, r06/meas/m1/accents.txt and accents_nohp.txt.
Tags: [measured] read from those tables; [inferred] reasoned, not measured.

## 1. What changed, by plan item

### Item 1. Bassoon and oboe sample starts: done
- Cause (critic 5): many Iowa MIS chromatic-run files begin with the tail of the previous semitone, which build_iowa.py
  kept as part of the note.
- r06/build_iowa.py gets an FFT YIN pitch tracker (`yin_f0`, de Cheveigné and Kawahara 2002) and `pitch_onset()`:
  a note's start moves only when at least 3 frames before it sit -60 to -140 cents under its steady pitch (the previous
  semitone of the run); the new start steps back to the level minimum within 20 ms and gets a 5 ms squared fade-in.
  New options `--pitch-onset --fade-in 0.005`.
- Rebuilt assets/iowa/bassoon-r06 (`--vel 35,52`), oboe-r06 and bassclarinet-r06 (with -L/-R/-a2 maps), all
  `--pan-spread 35`. 105 bassoon and 13 oboe samples moved; 0 lead-ins remain [measured, iowa_onset_pitch.py].
  The flute set needed no change.
- Rendered bassoons m1: median tuning -84 -> -0.7 cents, time to pitch 0.30 -> 0.00 s, notes starting a semitone low
  89 % -> 0 % [measured, pitchcheck.py].
- Sources: https://doi.org/10.1121/1.1458024 (YIN); https://theremin.music.uiowa.edu/MIS.html ;
  https://theremin.music.uiowa.edu/MIS-Pitches-2012/MISBassoon2012.html

### Item 2. Softer accents (Dan): done
- LilyPond's MIDI already adds velocity for articulations (ly/script-init.ly, 2.24: accent +20, marcato +40), and r05
  added 8-10 more plus an accent layer and a CC11 dip. That was the "too much attack".
  Sources: https://gitlab.com/lilypond/lilypond/-/raw/master/ly/script-init.ly ;
  https://lilypond.org/doc/v2.24/Documentation/internals/music-properties
- r06/articulate.py `accent_mode: weight`: an accented note starts from the velocity a plain note would have there
  (the plain-note curve inside a hairpin, else the staff's median plain velocity at that printed dynamic, else the
  LilyPond velocity minus 20/40), then gets `accent_level_dB` 2.0 over the whole note (x1.5 for marcato) and a soft
  CC11 bump of 1.5 dB (40 ms rise, 300 ms cosine fall). Accents are weight, not a spike.
  Iowa winds: level 1.0 + bump 2.0 dB. Timpani keep a velocity step (+6). The r05 string accent layer is off.
- Accented notes no longer pull the unit's dynamic curve up (they enter it at the plain median).
- Sources (critic 5's list): https://vi-control.net/community/threads/changing-lass-i-attacks.30193/ ;
  https://www.garritan.com/?p=8025 ;
  https://forums.steinberg.net/t/help-to-export-midi-with-accents-converted-to-velocity-not-cc/1035550 ;
  https://depositonce.tu-berlin.de/items/b919b35f-45ca-4a73-9536-77570c603359/full

### Item 3. Iowa woodwind balance: done
- r06/meas/scripts/windcal.py recalibrates each wind stem's `printed_trim_dB` from stemcmp's "vs string median"
  (dead band +-2 dB at pp-mp and +-1 dB at mf-ff, gain 0.5 / 0.8, pp/p trim capped at +2), then +0.5 dB at mf-fff so
  printed ff winds stay above printed f brass (r06/meas/scripts/invsim.py simulates inversion counts for a trim set).
- Brass: printed_trim p/mp/mf -1, f -2 (chosen by invsim). `dynamics.printed_trim_all_dB` ff/fff -1 for all stems.
  (f -1 was tested and dropped: m1 LRA 17.9 and soft-louder-than-f bars 12 -> 15.)
- New hairpin velocity cap (`hairpin_cap_steps` 2): inside a hairpin a note's velocity may not exceed the staff's
  plain median two printed steps above its dynamic (or the next printed dynamic). Capped notes: m1 153, m2 10.
  The v156 bar 3 bass clarinet swell goes from velocity 64 to 44.
- Sources: https://vi-control.net/community/threads/balancing-instruments-across-dynamics.51339/ ;
  https://vi-control.net/community/threads/volume-balancing-an-orchestral-template.109030/page-2

### Item 4. Rolls keep their printed shape; 3/4 bar length fixed: done
- `roll_curve` took its bar length from 4/4; it now reads the bar from the MIDI time-signature grid
  (`TempoMap.bar_ticks`), so the "-1 dB per bar" settle is per real bar in 3/4 (m2) and any meter.
- After a hairpin reaches its printed target the roll settles at most -2 dB; rolls printed pp or softer settle at most
  -6 dB; roll step 3.5 -> 3.0 dB per printed dynamic.
- lib/balance.py `roll_carry_cut`: the largest segment cut carries into later segments of the same roll unless a
  crescendo segment starts there (fixes m2 2-3 ending above its printed level).
- Timpani roll channel attack 5 ms (smoother sample-step fronts).
- Source: https://freepercussionlessons.com/how-to-play-timpani-rolls-from-soft-to-loud-and-back-to-soft ;
  https://forum.vsl.co.at/post/288710

### Item 5. Legato for the Iowa winds: partly done
- stem.py `legato_env`: a note that starts while the previous note of the same channel still sounds skips the first
  part of the sample's attack (-3 dB start, at most 0.3 s) with a 60 ms attack. Bassoon slurred-boundary dip
  -3.4 -> -0.9 dB [measured, render D]. Slurred vs detached contrast is still under critic 5's 8 dB [measured].
- Sources: https://sfzformat.com/tutorials/legato/ ; https://sfzformat.com/opcodes/offset/

### Item 6. Brass from the Iowa MIS: not done
- Downloaded assets/iowa/src/horn (12 pre-2011 AIFFs; logged in assets/README.md) but the site has no pp C2-B3 and
  no mf C3-B3 horn files (404), so a horn set would have holes. Not used.

### Item 7. Width for the mono winds: done
- stem.py `src2`: flutes/clarinets (Detmold S7) and oboes/bassoons (S6) convolve the left and right halves with two
  source IRs (each x sqrt(0.5)); width 1.0. Wind stem L/R correlation m1 Fl/Ob/Cl/Bn 0.83/0.86/0.80/0.84 ->
  0.76/0.79/0.75/0.79 [measured, stems_summary]; m2 0.84/0.85/0.84/0.85 -> 0.77/0.78/0.77/0.81. Bass clarinet
  (no src2) 0.85 / 0.88.
- Sources: https://forum.vsl.co.at/post/143166 ;
  https://vi-control.net/community/threads/early-reflections-positioning-and-panning.148432/

### Item 8. Movement II range and the master EQ: partly done
- m2 LRA 22.1 -> 21.0, p50 -10.6 -> -9.1 (from items 2-3; no m2-only change was kept).
- Master EQ: 720 Hz bell -2.0 -> -2.6 dB, 90 Hz low shelf +2 -> +3 dB.

## 2. Before / after

### Movement I (v156)
| measure | r04 | r05 | r06 | tag |
|---|---|---|---|---|
| LRA LU | 19.2 | 19.2 | 18.2 | [measured] |
| short-term p10 / p50 / p95 rel I | -15.0 / -5.5 / 4.2 | -15.1 / -5.3 / 4.1 | -14.1 / -4.7 / 4.1 | [measured] |
| short-term max LU | 7.1 | 6.8 | 6.5 | [measured] |
| Spearman bar loudness vs printed (all / no-hairpin) | 0.82 / 0.89 | 0.81 / 0.88 | 0.81 / 0.88 | [measured] |
| inversions all / outside hairpins | 365 / 250 | 359 / 208 | 337 / 167 | [measured] |
| bars printed <= mf louder than median f bar | 10 | 8 | 12 | [measured] |
| melodies >= 0 dB vs loudest / >= -6 dB vs sum (of 20) | 12 / 14 | 11 / 16 | 12 / 15 | [measured] |
| accent peak boost, median over stems (range) | - | 7.0 (2.2-11.9) | 3.8 (1.3-4.8; Horns 1-2 9.0 *) | [measured] |
| accent onset crest re plain notes | - | +4 to +12 dB | mostly within 3 dB | [measured] |
| mix onsets: steepest median dB/ms / onset crest | - | 2.45 / 3.1 | 2.43 / 2.0 | [measured] |
| bassoon tuning / time to pitch | - | -84 c / 0.30 s | -0.7 c / 0.00 s | [measured] |
| 1/3 oct vs Brahms mean 62 / 79 / 794 Hz | -5.0 / -4.6 / +2.6 | -4.1 / -4.0 / +3.3 | -2.3 / -3.9 / +2.2 | [measured] |
| wind stems vs string median at f/ff | - | +2.6 to +4.1 | about -1 to +1 | [measured] |
| roll 41-43: bar 43 re bar 41 | -4.4 | -17.0 | -14.5 | [measured] |
| roll 117-121 / 167-169 crescendo | -4 / -4 | +8.0 / +4.1 | +7.2 / +3.9 | [measured] |
| timpani loudest in roll bars | 0 | 0 of 31 | 0 of 31 | [measured] |
| roll 1-4 in-band audible share | - | 0.38 | 0.56 (end still masked) | [measured] |
| Vln I 55-62 / Violas 107-114 melody vs loudest | +0.7 / - | -1.3 / -2.7 | -1.0 (render D) / -0.7 | [measured] |
| mix L/R correlation | 0.61 | 0.66 | 0.63 | [measured] |

\* Horns 1-2: its mp accents sit in crescendos and are compared with solo plain notes; without hairpin notes the
boost is 2.7 dB (accents_nohp.txt). Clarinets' accent edge 20.2 dB/ms is one note starting from digital silence
(bar 23), not a click [measured].

### Movement II (v30)
| measure | r04 | r05 | r06 | tag |
|---|---|---|---|---|
| LRA LU (target <= 19.5) | 20.9 | 22.1 | 21.0 | [measured] |
| short-term p10 / p50 / p95 rel I | -14.0 / -9.6 / 6.9 | -15.3 / -10.6 / 6.8 | -13.9 / -9.1 / 7.1 | [measured] |
| short-term max LU | 9.7 | 9.2 | 9.4 | [measured] |
| Spearman | 0.74 | 0.66 | 0.67 | [measured] |
| inversions all / outside hairpins | 19 / 12 | 30 / 12 | 33 / 14 | [measured] |
| melodies vs loudest / vs sum (of 14) | 7 / 11 | 7 / 10 | 7 / 10 | [measured] |
| roll settle 2-3 / 67-70 / 89-92 dB | -2.1 / - / - | -0.7 / - / - | -3.9 / -3.1 / -3.0 | [measured] |
| timpani loudest in roll bars | - | 0 | 0 of 10 | [measured] |
| mix onsets steepest median dB/ms / crest | - | - | 2.17 / 3.2 | [measured] |
| 1/3 oct 62 / 79 / 794 Hz vs Brahms mean | -1.7 / -1.5 / +0.7 | -0.9 / -1.1 / +1.1 | +0.1 / -0.2 / +0.5 | [measured] |
| mix L/R correlation | 0.57 | 0.61 | 0.58 | [measured] |

m2 has no accent pairs that pass accents.py's clean-onset filter (as in r05).

## 3. What got worse
- m1 bars printed <= mf louder than the median f bar: 8 -> 12 (r04 10) [measured]; lower wind ff/fff and brass f
  trims narrow the top.
- m1 LRA 19.2 -> 18.2, at the bottom of critic 5's 18-20.5 band [measured].
- m2 inversions 30 -> 33 (r04 19) [measured]: the top offender is the timpani (19 pairs), single strokes in bars 60 (p)
  and 80-81 (f) that now stand over winds/strings printed louder since the wind ff came down. Not rolls.
- m1 melodies vs sum 16 -> 15 of 20 [measured].
- Oboe/clarinet dB per printed step lower (about 0.9-1.6 dB) after the calibration [measured, stemcmp].
- m2 Spearman 0.67 is still well under r04's 0.74 [measured].

## 4. Open
- Brass, cor anglais, contrabassoon still FluidR3; Iowa horn set has gaps (item 6).
- m2 LRA 21.0 vs target 19.5; m2 Spearman; timpani single strokes in m2 (60, 80-81).
- Mix front edges: steepest median 2.43 dB/ms in m1 vs target <= 2.2.
- Legato contrast (slurred vs detached) under 8 dB; real legato transitions need interval samples.
- Opening roll 1-4 still masked at its end; pitch-51 roll stroke autocorrelation; rollfront "steps" at m1 12, 13, 41,
  63, 81, 122, 141, 159-161, 167 are contiguous rolls (the previous roll still sounding), largest one-sample jump
  <= 4 % of peak, so not clicks [measured].

## 5. Tuning history (test renders, all full renders in /tmp, now deleted)
- A: first accent recipe (2.5 dB CC11 bump + 3 velocity steps): accented passages fell (accented ff cellos -5.7 dB)
  and inversions rose; replaced by accent_level_dB + 1.5 dB bump.
- B, C: wind calibration to -2 dB vs strings raised inversions (brass f over winds ff); +0.5 dB at mf-fff and brass
  trims by invsim.
- D: legato_env, src2 width, hairpin cap. E: roll_carry_cut, roll caps. F: printed_trim_all f -1 (dropped).
  G: final (= r06/out-m*.mp3).

## 6. Generality
- r06/meas/scripts/generality.sh on mvt1/v196 and mvt2/v74: both parse, no config gap; 20 melodies / 9 rolls and
  16 melodies / 3 rolls; 9 unmatched MIDI notes in m2 (as in r05) [measured]. No bar lists anywhere; the hairpin cap,
  plain medians and roll bar lengths are computed from each score.

## 7. Rebuild
```
cd /mnt/project-files/symphony/render
# Iowa sets (only if assets/iowa/*-r06 are missing; sources in assets/iowa/src)
python3 r06/build_iowa.py --help          # bassoon: --vel 35,52; all: --pan-spread 35 --pitch-onset --fade-in 0.005
# renders (one at a time; check ps aux | grep render.py first)
python3 r06/render.py --score /mnt/project-files/symphony/mvt1/v156 --out r06/out-m1.mp3 --work /tmp/render-06-m1
python3 r06/render.py --score /mnt/project-files/symphony/mvt2/v30 --out r06/out-m2.mp3 --work /tmp/render-06-m2
cp /tmp/render-06-m1/render.midi r06/r06-m1.midi; cp /tmp/render-06-m2/render.midi r06/r06-m2.midi
# measurements
bash r06/meas/scripts/meas.sh            # writes the m1/m2 tables
python3 critics/c05/scripts/accents.py /tmp/render-06-m1 r06-m1
python3 r06/meas/scripts/windcal.py ...  # WINDCAL_TARGET / WINDCAL_STEMS env overrides; prints new printed_trim_dB
python3 r06/meas/scripts/invsim.py ...   # inversion counts for trim offsets on stem_bars.csv
bash r06/meas/scripts/generality.sh
```
