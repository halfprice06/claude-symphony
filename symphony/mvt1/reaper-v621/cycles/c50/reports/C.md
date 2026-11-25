# c50 critic C: dynamics over time (render under review: c49)

Lens: hairpin and phrase shapes, the loudness arc against the score, master and delivered loudness range (BRIEF 6), swells and loop pulsing on long notes (BRIEF 7), decays and subitos (S3, S4), against real recordings. c50 adopts the template mix (`build/mix_template50.json`); c51 applies the performance rules. Each finding says which cycle it belongs to.

Method: c49 master, mp3 and stems; the CC1 / CC11 / `dyn_curve` / `vol_db` lanes of `build/parts.json` (the c49 data, its stem fix included); ffmpeg EBU R128 frame logs (`-v verbose`, `framelog=verbose`); rtk's `cutoff_decays` and `env_db` (`symphony/render/tools/rtk.py`); `cycles/c44/actor_scripts/m44.py tails`, `rebows44.py`, `cycles/c25/actor_scripts/loopscan.py` (path changed to reaper-v621), `tools/motion.py`; references Dvořák 9/i (decoded) and the stored rtk metrics of Brahms 1/i, 4/i, 1/ii, 4/ii. Phrase = notes with played gaps under 0.25 s, at least 2 s long (415 phrases). Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c50-C/` (deleted at the end).

## Manual notes (cycles 48-51: pages behind this lens's top open problems)

| Page | What it says | Where it applies | Render follows it? |
|---|---|---|---|
| p.53 (2.5.7) | Shape lines with CCs the way a player shapes them; velocity for shorts, CCs for long notes, changing mid-note or over a phrase | Every sustained line | Partly. CC11/CC1 follow the printed marks and hairpins exactly, but no phrase is shaped beyond them (finding 2) |
| p.63 | Every Opus instrument fades to silence on CC11 (the old niente patches are gone) | Phrase tapers, HP_NIENTE | Yes for printed niente; the unprinted phrase-end taper is missing (finding 2) |
| p.64, p.151 | CC11 for the moment-to-moment line and swells "over the course of a phrase"; CC7 or fader for the track ceiling; send CCs before the first note | All tracks | Ceilings in the volume envelope, pre-roll CCs: followed. Phrase swells: not followed |
| p.101 | Brass sustains: all 4 dynamic layers play at once, the Mod Wheel (CC1) crossfades them | Brass and clarinet CC1 lanes | Followed for printed dynamics. On 63 % of brass long notes CC1 is flat while CC11 moves (finding 2) |
| p.102 | Brass shorts have no release trails; the main sample carries some room after the note ends | Decays with Opus reverb off | Relevant to c50: with the Opus hall off, the samples' own room plus the full return IR set the tail (finding 1) |
| p.220-221 | The convolution reverb's IR Envelope (Simple decay slider; Full start/end, fade times) shortens an IR | The four Spaces II returns | Spaces II stores the same `ConvolutionSetup` dict (`envelopeMode`, `endPos`, `decayLength`; `ho-mix-fx.json`), so c44's envelope fix carries over (finding 1) |
| p.222 | The recorded room is heard as long as samples play, release trails included; mic mix runs from dry to wet | Close/Main levels, release caps | Applies to finding 1: the returns add to a room the Main mics already carry |

MANUAL-GAPS items in this lens: #12 (Felt Cresc rolls into a stroke) is an option for the bar-121 roll (finding 5); nothing else open.

## EW-TEMPLATE-PLAN sections in this lens: what the c49 render does not yet apply

- Section 2 (returns, full IRs): in `mix_template50.json` for c50. The full IR is the risk in finding 1.
- Section 6 (CC shaped per phrase, not per note; long notes as late swells, centred hairpins or fades): not applied. The per-note "swell"/"taper" contours are still the only long-note motion.
- Section 7 (swell +15 by 0.4 s / +25 by 0.8 s, taper about 20 over the last second, slur lean-off): not applied (finding 2). Lean-off: recommend not applying (about 0.5 dB, and it would fight the fitted legato-sag fills).
- Section 8 (arch peaking at 33-62 %, long notes keep moving): not applied (finding 2).
- Section 9 (crescendo control point 34 % / 88 %, diminuendos hold then fall): not applied, hairpins are linear in CC (finding 4). Section 9's register sends (-10 dB from bassoons, contrabassoon, trombones, tuba, basses; -6 dB trumpets) and the 2.3 kHz low-pass after Spaces II are **not in `mix_template50.json`** (finding 1).
- Section 10 (shape by character; level follows timbre; doublings share one curve): shape by character not applied (finding 2). Level follows timbre: applied on the CC lanes (r(CC1, CC11) per phrase median 0.98-0.99) but not on brass long notes, where CC1 is flat on 63 % (CC11 on 10 %). Doublings share one curve: yes for printed curves (identical marks give identical lanes, roles on top); keep it when phrase shapes come in (finding 2).

## Findings, ranked by what a listener would hear

### 1. Decays with the new hall: the c49 baseline and the limit c50 must meet (c50; baseline measured, risk inferred from the finale)

Where: every tutti stop and subito, master. The finale's first template render (full Spaces II IRs) took 0.62-0.73 s to fall 20 dB against 0.41-0.50 s with the Opus hall, its final cut-off fell only 13.7 dB in 0.3 s, and -3 / -6 dB on the returns moved the -20 dB time only to 0.66 / 0.63 s. Rendering movement I the same way would undo Dan's "too wet, mushy" fix (S4).

c49 baseline (measured, master):
- rtk detector (30 ms / 10 ms envelope, 0.4 s plateau, 15 dB fall within 0.4 s): bar 26 (89.6 s) t20 0.55 s, RT(-5..-20) 1.19 s; bar 138 (311.1 s) 0.50 / 1.06; bar 170 fermata (379.4 s) 0.44 / 1.03; soft bar-14 end 0.46 / 0.86.
- `m44.py tails 49` (drop from the first frame 2 dB under the pre-level): qn 103 -14.1 dB at 0.15 s (next note +0.31 s); 125.9 -11.9 / -18.6 at 0.15 / 0.3 s; 288 -12.4 / -16.3; 551 -14.5 / -20.7; 679 -11.6 / -19.5 / -29.9 / -43.7 at 0.15 / 0.3 / 0.6 / 1.0 s, RT(-5..-25 / -20..-35) 1.32 / 1.81 s; final chord (728) -8.8 / -17.0 / -34.8 at 0.3 / 0.6 / 1.0 s; 60-250 Hz share of the tails -5.2 to -9.7 dB.
- By band, below 250 Hz is already the slow part: from -3 to -20 dB in 0.57-0.81 s at bars 32, 83, 138, against 0.13-0.36 s above 250 Hz.
- Subito bar 62 (qn 244): -5.0 dB at once, -13.1 dB by +0.3 s, largest 0.2 s fall 7.7 dB (c35 had 14 dB). Bar 84 (qn 332) follows the bar-83 stop.
- References: Brahms 1/i, 12 stops, t20 0.43-0.55 s (median 0.485), RT 1.13-1.62 s; Dvořák 0.49-0.50 s, RT 1.32 s; late decay 1.5-2 s in recordings.

Limit for the c50 render (master; run `python cycles/c44/actor_scripts/m44.py tails 49 50` and rtk's `cutoff_decays` on `render/00_Master.wav`):
- rtk t20 at every detected tutti stop 0.58 s or less (top of the references), median 0.55 s or less;
- drop at +0.3 s 15 dB or more at qn 125.9, 288, 551, 679 (c49 16.3-20.7; S4's floor is 13);
- RT(-20..-35) after the bar-170 fermata 2.0 s or less (c49 1.81);
- 60-250 Hz share of each tail no more than 2 dB over c49's;
- final chord -20 dB within 0.8 s of the cut-off (Brahms 1/ii 0.79, 4/ii 0.48 s; c49 about 0.67 on `m44.py`);
- bar-62 subito: 10 dB or more down by +0.3 s, no 0.2 s fall over 9 dB.

Fix, in this order if the limit fails (not by lowering the returns, which the finale showed does almost nothing):
1. Section 9's register sends, a plan default missing from `mix_template50.json`: `send_offset_db` -10 on Bassoon 1, Bassoon 2, Contrabassoon, Trombone 1, Trombone 2, Bass trombone, Tuba, Double basses (and the basses' aliases), -6 on Trumpets 1-3 and Trumpets a2. The template's return high-passes sit at 87-100 Hz against the c44 hall's 160 Hz, so more bass reaches the tail, and the bass is already the slowest band (inferred).
2. The IR envelope on the four returns: `returns.*.fx[1]` `"set": {"irSetup": {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}}` (other keys kept; check the read-back). The same setting took c44's hall from a 2.61 s to a 1.54 s late slope and the +0.3 s drop to 17.8-20.8 dB.
3. Only then profile "duc".
Also from section 9, the 2.3 kHz low-pass after Spaces II darkens the tail but will not shorten t20 much (inferred).

S3 note (inferred from the routing): with post-fader sends the forte's hall keeps ringing on the return when the dry track falls, so `SUBITO_TAIL`'s 0.35 s ramp (built for the post-hall Opus envelope) is no longer needed. Leave it in c50, measure the bar-62 master fall against the dry stems, and in c51 shorten `ramp_s` to about 0.12 s if the master still keeps 10 dB or more of tail under the p.

### 2. No phrase is shaped beyond its printed marks: no swell-in, no taper, lyrical phrases start at their peak, a third of long notes are flat (c51; measured)

Where: every lyrical line (CA espr. bars 5-8, Horn 1 espr. bars 13-14, the second theme 47-68, Fl1 / BCl espr. 73-84, bars 107-112, Horn 1 espr. bar 125, the recapitulation's second theme 145-157, the coda 171-182), and the driving Allegro passages.

Evidence (lanes of 415 phrases; strings and winds CC11, brass and clarinets CC1):
- Swell-in after the first onset: median 0 units at +0.4 s and 0 at +0.8 s in every class (builds +1); only 2 % of lyrical and 4 % of driving phrases rise 10 units or more by 0.8 s. Plan: +15 / +25.
- Taper over the last second: median 0 in every class; 9 % of lyrical, 22 % of driving phrases taper 10 units or more. Plan: about 20.
- Lyrical phrases (89): 18 flat; the others peak at 0.39 of the phrase (IQR 0.17-0.57) but start only 4 units under the peak and end 26 under: they start at the top and fall. Plan: centred arch, peak about 0.44, start 35 and end 32 under.
- Driving phrases (134): 43 flat; the rest peak at 0.41, start 6 under. Plan: start high and fall, or peak at 0.05-0.30.
- Builds (192): peak at 0.86 (IQR 0.62-0.94), start 26 under. Closest to the plan's 0.95.
- Long notes of 1.2 s or more flat within 2 units: 34 % overall; brass CC1 63 % (CC11 10 %), string CC11 19 %, wind CC11 18 %. Plan: 0-13 % (6 % in the lyrical cue).
- On the stems (dB): lyrical winds rise +1.9 / +2.0 dB by 0.4 / 0.8 s, brass +0.9 / +1.6, and taper only 0.7 dB (winds) and 1.1 dB (brass) in the last second; driving brass 0.0 dB. Strings already rise +4.8 / +6.1 dB in their first 0.4 / 0.8 s (sample attack) and taper 2.5 dB. Examples: Horn 1 espr. bars 13-14 (48.9-55) rises -1.3 dB and tapers +0.2 dB; the cor anglais espr. (19-35) gets louder into its last second (-0.4 dB).
- Whole-movement motion is not short (master dS4 p90 11.1 dB / 1s-20s 6.2 dB; mp3 8.8 / 5.0; Dvořák 9.7 / 5.6): the composed dynamics carry it, so the shapes below should reshape inside phrases at moderate depth rather than add range.

Fix (c51): port the finale's rule. In `symphony/mvt3/reaper-v600/tools/score_to_parts.py` (built from this pipeline): the `PHRASE_SHAPE` option block (lines ~200-210), the grouping, type and offset code after the contours (lines ~3299-3420: `phrase_shapes`, `ps_scale`, `ps_weight`, `phrase_off`, dropping the per-note "swell"/"swell_taper"/"taper" contours inside a shaped phrase), its use in the CC11 value (~3476), the CC1 value of `CC1_DYN_TRACKS` with `cc1_floor` (~4064-4069), and the extra lane breakpoints (~3497). Movement I's matching places: the contours block at lines 3120-3170, the CC11 / CC1 value functions after it. Three changes for movement I:
- (a) On `CC1_DYN_TRACKS` put the same offset into CC11 as well as CC1 (the finale puts it only into CC1). That keeps the level lane following the timbre lane (section 10; now r 0.99).
- (b) Group phrases on score onsets and written ends (`sq`), not moved onsets, so doublings get the same curve point for point (section 10). For strings, also break phrases at a written rest of 0.5 qn or more and at a printed dynamic that is not a hairpin target: string phrases now run a median 13.7 s and up to 42 s without a played gap (winds and brass 7.1-7.5 s).
- (c) `start` by family.

Values (lane units, added to the printed level):
```
PHRASE_SHAPE = {"families": ("string", "wind", "brass"), "min_s": 2.0, "gap_s": 0.25,
    "start": {"string": 0, "wind": -8, "brass": -8}, "rise": [(0.4, 2), (0.8, 6)], "peak": (10, 0.44),
    "pre_end": (1.0, 4), "end": -12,
    "scale": {"ppp": 0.6, "pp": 0.8, "p": 1.0, "mp": 1.0, "mf": 1.0, "f": 0.6, "ff": 0.35, "fff": 0.2},
    "floor": 8, "cap": {"brass": 108}, "cc1_floor": 36, "hp_fade_s": 0.25, "step_s": 0.1,
    "types": {"build_cc": 10, "drive": (6, (10, 0.15), -10), "drive_min_bpm": 105,
              "lyric_spans": [(0, 56), (176, 272), (288, 332), (424, 448), (488, 520), (576, 628), (680, 728)]}}
```
- Winds and brass: +10 units by 0.4 s and +14 by 0.8 s, about +3 / +4 dB at p-mf. Strings get a smaller rise (0 → +2 → +6) because their samples already rise 4.8-6.1 dB. Both are under the plan's +15 / +25 for a measured reason: the S2 lead tables and the c48 swell fills put perceived attacks on the beat, and a deep onset dip would move them late (inferred).
- Taper: +4 to -12 over the last second, about 4-5 dB at p-mf.
- Lyrical arch: peak at 0.44, winds and brass starting 18 units and ending 22 units under it.
- Classes:
  - lyric: the spans above (Lento; the second theme with its oboe and clarinet lead-in; Fl1 and BCl espr. 73-83; bars 107-112; sostenuto and a tempo 123-130; the recapitulation's second theme to bar 157; the coda from Più lento).
  - build: detected per phrase (the printed level rises 10 CC or more, or a crescendo covering a quarter of the phrase ends in its last quarter). This picks up bars 9-12, 23-26, 59-63, 111-122, 127-130 and 156-160.
  - drive: everything else at 105 bpm or faster (first theme 56-88, the ff tutti 100-128, transition 128-176, closing 272-288, development 336-424 and 448-488, recapitulation 520-576, coda 664-680).
  - Keep the finale's rule of no taper on accented or crescendo-arrival last notes.

Pass criteria for c51, on the same measures:
- Lanes: lyrical winds/brass median rise 8 units or more by 0.8 s; taper 10 units or more on 60 % of non-build phrases; peak median 0.40-0.50 (lyric), 0.85-0.95 (build), 0.30 or less (drive); flat long notes 15 % or less (brass CC1 too); r(CC1, CC11) 0.95 or more.
- Stems: lyrical wind/brass taper 3 dB or more.
- pcX / t50 of every phrase's first note (`cycles/c48/actor_scripts/scan48.py`) within +20 ms of c49.
- Then refit accents (`fit_accents.py`, 2-4 dB rule) and the swell fills (`swell_fills48.json`, `swellfit48.py` / `simenv48.py`), whose neighbours and contours this changes.
- In c50, port the code with `PHRASE_SHAPE = None` if the actor has time (parts.json must stay byte-identical), so c50's mix is judged on unchanged performance data.

### 3. Loudness through the mix change: the c49 arc matches the score, so these numbers must survive c50 (c50; measured, effects of the mix inferred)

Climax order. The score has two fff tuttis, bar 122 (allargando, tam-tam heavy beater) and bar 160 (largamente after the cymbal roll, the main climax), and two ff tuttis, bars 25-26 and 167-170.
- Delivered S max: 160 -11.3 > 122 -12.0 > 169-170 -13.6 > 25-26 -14.2 (next: 140 -15.0, 116-117 -15.4) LUFS, so the order matches the score.
- Master momentary max: 160 -5.8, 122 -7.3 (1.5 dB), 26 -9.7, 170 -10.1.
- The ff plateau of bars 117-120 sits 3.4-3.6 dB under bar 122 (master S -12.4 / -12.5 against -8.9).
- Builds grow monotonically: bars 113-116 +9.6 dB, 127-131 +17.4, 155-160 +26.3 (master bar power).

Macro dynamics and delivery:
- Bar power against each bar's loudest printed dynamic: correlation 0.87 and 4.6 dB per dynamic step on the master (mp3 0.83, 2.9 dB).
- Master: I -17.4 LUFS, LRA 23.3 LU, S p10 -38.5, S max -7.4.
- mp3: I -19.8, LRA 14.8, span 19.0 dB (top of the 16-19 window), limiter 1.3 dB, TP -1.8 dBTP.
- Swells survive delivery: 2793 frames with a 5 s swell of 3 dB or more, 1 reversed in the mp3 (bar 170); the delivery keeps a median 0.81 of each swell.
- Delivered bar levels: coda mp solo 171-174 -22 to -24.5, pp 175-181 -29 to -31.8, final ppp bar 182 -36.4, opening ppp bar 1 -33.7.
- Against recordings: master S max is 10.0 LU over the integrated loudness (mp3 8.5) against 5.1 (Dvořák), 6.1 (Brahms 1/i) and 7.6 (Brahms 4/i). That is acceptable for an Allegro with two fff, but should not grow.

Expected effects of c50 (inferred, finale c06 measured):
- The family EQ takes 2-8 dB out of the body bands and the brass needed +4 to +6 dB make-up.
- 100 %-wet returns add tail energy to every soft passage, which lowers the master LRA.
- Bars 122 and 160 are brass- and percussion-heavy while bars 25-26 are string-led, so a missed brass make-up can reorder the climaxes and a missed string or wind correction can flatten them.
- The master's sample peak (1.469 at qn 636.4) gains the returns' share.

Fix in c50:
- After the render, set family make-up gains (dry stems) before judging anything else, so that these master differences stay within ±0.7 dB of c49's: 160 minus 122, 122 minus the 117-120 plateau, 122 minus 169-170, 169-170 minus 26.
- Then re-fit `deliver_master.py` only if needed, keeping RIDE_TRIMS.
- Targets for c50 (on `cycles/c39/actor_scripts/smax.py` and the measures above): delivered S max order 160 > 122 > 169-170 > 26 with margins of at least 0.5 / 1.0 / 0.3 dB; LRA 14-16 LU; span 16-19 dB (do not let it pass 19); limiter 3 dB or less; TP -1.5 dBTP or lower; master correlation 0.85 or more and slope 4.3 dB per step or more; reversed 5 s swells 2 or fewer; coda pp 175-181 at least 5 dB under the 171-174 solo and bar 182 at least 4 dB under 181 in the mp3.

### 4. Hairpins are linear in CC: diminuendos fall too early, brass crescendos come late (c51; measured)

Where: all 398 hairpins of 2 qn or more played over a continuous line.

Evidence:
- Lanes: every family reaches 33 % of the CC change at 34 % of the hairpin and 71-72 % at 72 %.
- Realised on the stems (dB, fraction of the hairpin's own change):
  - crescendos: strings 0.39 / 0.59 / 0.75 at 34 / 50 / 72 % (n 112, median +6.3 dB), winds 0.43 / 0.62 / 0.83 (n 85, +7.4 dB), brass 0.21 / 0.54 / 0.88 (n 50, +4.6 dB);
  - diminuendos: strings 0.23 / 0.50 / 0.78 (n 67, -5.9 dB), winds 0.15 / 0.40 / 0.71 (n 47), brass 0.31 / 0.49 / 0.77 (n 37).
- Plan section 9's curves, read as quadratic Bézier segments: crescendos 0.60 / 0.76 / 0.91 at 34 / 50 / 72 %, diminuendos 0.07 / 0.16 / 0.38 (computed from the control points, inferred).
- So our diminuendos have lost three quarters of their level by 72 % instead of holding to the last note, and the brass crescendos rise late. Strings and winds are already front-loaded in dB, because CC11 gives more dB per unit low in its range.
- Reversed: 17 crescendos and 10 diminuendos of 398. 10 of the 17 reversed crescendos sit in the two crescendo bars into the fff arrivals (finding 5).

Fix (c51):
- Port `HP_CURVE` from the finale's hairpin builder (mvt3 lines ~1923-1934; movement I's hairpin code near line 1867) with `HP_CURVE = {"cresc": (0.4, 0.65), "decresc_last": 0.35, "min_qn": 1.0}`.
- Add one key: crescendos of 4 qn or more that end on f or louder stay linear, because builds peak at the end (section 10 overrides section 9 there). Keep the `HP_GAIN_DB` ramps held to the arrival (kit section 4).
- For a diminuendo over one held note (no inner onset), add a point at 60 % of the time with 20 % of the fall.
- Pass in c51 (realised dB): short crescendos 0.50-0.65 of their rise at 34 % (brass included), diminuendos 0.30 or less at 50 % and 0.55 or less at 72 %, no more reversed hairpins than c49, crescendo growth medians not below c49's.

### 5. The crescendo bar into the first fff (bar 121) grows only 1.2 dB, and the violins and woodwinds take no step at 484 (c51, or c50's level pass; measured, fix simulated)

Where: bars 121-122 (qn 480-486), against the parallel bars 159-160.

Evidence (per-beat stem levels):
- Bar 121 (2.05 s) grows +1.2 dB on the master from its first to its last beat. Bar 159 (2.15 s) grows +3.4 dB.
- At 484 the master steps +4.3 dB, carried by the entering brass, the tam-tam, the timpani (+6.8) and the violas (+9.8).
- Steps at 484 (dB): Violins I -0.6, Violins II +0.1, Flute 1 +0.3, Flute 2 -3.1, Oboe 1 -2.5, Clarinet 1 +0.1, Bass clarinet -2.9, Bassoons -0.5 / -2.5. At 636 the strings step +2.8 to +6.2 and the low winds +5.4 to +6.0.
- During the printed crescendo of bar 121, Flute 2 (-1.6), the basses (-2.2) and Horns a2 (-1.0) fall; the timpani roll grows +1.7 dB against +6.2 dB in bar 159.
- Causes (read): `roles.json` Violins I [484, 492, -4] and Violins II [484, 496, -4] (c02, set for v221's Ab6 tremolo "8 dB over every brass stem"; in v621 the violins sit 0-1 dB under Trombone 1 and the tuba at 484-488), Flute 1 [484, 492, -3], Flute 2 [484, 494, -2], Violoncellos [484, 492, -3, 1], `_all` [484, 492, -0.5, 2] and `ARRIVAL_WEIGHT_AT` 484 (-0.5, 1.5, 0.5). Each starts on the arrival and cancels the crescendo's held dB gain there. Series 1 critics already found bar 121 weak (+1.6 dB in c08).
- Simulated on the c49 stems: bar 121 gets +2 dB ramped 480 → 483.9 (held to 486, gone by 487.5) on the strings and the winds with the hairpin; Violins I / II get +2 dB and Fl1, Fl2, Ob1, Cl1, Bn1, Bn2 and BCl +1.5 dB from 484 to 486; brass and timpani get -1.5 dB from 484 to 490. Result: bar 121 grows +2.2 dB (from +1.2), the arrival steps +3.4 dB, and bar 122's momentary max is -6.7 against bar 160's -5.8 (c49 -7.3).

Fix:
- `roles.json` Violins I / II -4 → -2 at [484, 492] / [484, 496].
- Flute 1 / 2 -3 / -2 → -1.5 / -0.5.
- Brass: Trombones 1 / 2 [484, 492.5] +2.5 → +1.0; Tuba +2 → +0.5; Trumpets 1-3 [484, 488.5] +2 → +0.5.
- `LEVEL_SHAPES` rows: -1.5 dB 484-490 on Horns 1-4 and the timpani; the bar-121 ramp above on Vln I/II, Vla, Vc, Cb, Fl1/2, Ob1, Cl1, Bn1/2, BCl.
- It is level-only, so it can go into c50's stem-fix pass once the family make-up is set. Because `HP_CURVE` and the build class touch the same bars, c51 is the cleaner place.
- Check: delivered 160 over 122 at least 0.5 dB (c49 0.7).
- MANUAL-GAPS #12 (Felt Cresc, a recorded roll ending on a stroke) is an alternative for the timpani roll of bar 121 if its CC1 roll still grows under 3 dB.

### 6. Loop pulsing, re-bows and long-note swells pass in c49; re-check them on the first render without the in-patch hall (c50; measured baseline)

Evidence (c49):
- `loopscan.py`: 49 held spans of 6 s or more; none with pieces of 6 s or more reaches 0.40 autocorrelation at 3.95 s. Master passages at 3.95 s: Lento band +0.26 / centroid -0.14, final chord -0.01 / +0.20, bars 160-164 -0.41 / -0.14.
- `rebows44.py`: automatic re-bow dips median Vln I 2.8, Vln II 1.7, Va 2.1, Vc 1.3, Cb 2.0 dB; |step| medians 0.5-1.1 dB; steps of 3 dB or more: basses 7, celli 3, others 1.
- The `rebow_fills.json`, `loop_fills` and `SUBITO_TAIL` shapes were fitted on stems that carried the Opus hall. In c50 the stems are dry and the hall is a separate return, so a dip the in-patch hall smoothed can show (inferred).

Fix (c50 check, c51 refit):
- Run `rebows44.py 50` on the stems and on the master.
- Run loopscan on stems and master. The c25 copy points at series 1 (`R = .../symphony/mvt1/reaper`); set `R` to `reaper-v621`.
- Refit with `fit_rebows.py` in c51 only where the master's dip or step grew 1 dB or more over c49, or a span reaches 0.40 at 3.95 s.

Do not touch:
- The climax order and margins (160 > 122 > 167-170 > 26) and the fff lifts at 636.
- `deliver_master.py` settings (RATIO 3.0, KNEE_BELOW 5, LIFT_SMOOTH_S 5, TOP_RATIO 2.5) and `RIDE_TRIMS`, unless c50's levels force a refit.
- The hairpin dB ramps held to the arrival (HP_GAIN_DB, HP_HOLD_CAP, HP_CHAIN) and the build shapes of bars 113-116, 127-131 and 155-160.
- AUTO_REBOW, `space_rebows`, the re-bow fills and the timpani roll rules.
- SUBITO_FRESH / SUBITO_TAIL until measured with the new hall.
- The coda morendo and the ppp final chord, the tam-tam bloom rows, `swell_fills48.json` (refit, do not delete), and the string release caps (150 ms mf-ff / 350 ms p, basses 600 ms pp).
