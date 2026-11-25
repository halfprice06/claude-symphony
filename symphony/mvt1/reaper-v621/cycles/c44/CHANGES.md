# Cycle 44 (series 2): changes

## For Dan: what to listen for in c44

The whole movement is drier and clearer. The hall around the orchestra is half as loud and dies away sooner: after a full-orchestra stop the sound falls away about twice as fast as in c43, for example after the fermata chord at bar 170, at the end of the transition (bar 32), at bar 73 and at bar 138. Separately from the hall, the strings and horns no longer keep ringing after each note, so running string figures sound like separate notes rather than a blurred chord. Listen to the violas' eighths and triplets in bars 97-102 and 117-122, the second violins' détaché, and the horns in the tutti chords. Repeated string notes are now played as new bow strokes instead of being tied over:
- the first-theme motif's repeated tenuto note, `d''8( des'' c'' | c''4--)`, in bars 16, 28, 36, 79, 132, 144 and 168, now re-attacks in the strings as it already did in the winds;
- the cellos' repeated half and whole notes in bars 12, 22-23, 39-42, 82, 94, 113-115 and 168, and the violas' in bars 21, 94 and 126;
- the soft repeated notes of the Lento (bars 9-14), bars 43-53, 74-75, 145-146 and 173-176 change bow where the score writes new notes.

The soft passages are a little less bass-heavy, because the cellos' and basses' low boost now applies only in the loud tutti. Two balance points changed. At the coda's fermata chord (bar 170) the trumpets' high B is no longer covered by the first trombone. At bar 158 the violins' top line is no longer swamped by the horns' held E.

## Values for the other movements (Movement II, scherzo, finale)

All measured on Movement I in this cycle. Each change below is an Opus state change, so every track needs a full rebuild in both passes.

1. **Shared hall (build/mix.json `reverb`).**
   - **Settings:**
     - `"fx_volume": 0.095` (was 0.19);
     - `"low_cut_hz": 160`;
     - `"ir_setup": {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}`;
     - every send, the IR, `wet` 2.0, true stereo and `high_cut_hz` 5500 are unchanged.
   - **Code (tools/build_reaper.py `apply_mix`):**
     - the low cut sets `rv["filterActive"] = True` and `rv["lowFilterFreq"] = rv["lowCutFreq"] = low_cut_hz`, as in the kit;
     - the IR envelope copies each `ir_setup` key into the ConvolutionReverb insert's `irSetup` dict (class `ConvolutionSetup`: `envelopeMode`, `simpleDecay`, `startPos`, `endPos`, `attackLength`, `decayLength`, `attackCurve`, `decayCurve`);
     - a track's own `reverb_ir_setup` overrides it, for A/B tests.
   - **Facts:**
     - All 1683 installed .oib patches ship the factory values (envelopeMode 0, simpleDecay 1.0, endPos 1.0).
     - `simpleDecay` 0.3-0.5 changed nothing in envelopeMode 0, 1 or 2.
     - `endPos` with `decayLength` works in envelopeMode 1 and in 2 (identical results).
     - The top-level `"decay"` key is not part of the IR envelope.
   - **Test** (pass-2 tracks of 2nd Violins Stac chords, send 1.0, `cycles/c44/halltest/`):

     | Setting | Late slope (RT -20..-35 dB) | RT -5..-25 dB | Drop at 0.3 s |
     |---|---|---|---|
     | No envelope | 2.61 s | 2.25 s | 15.4 dB |
     | endPos 0.65 | 1.76 s | 1.93 s | 15.4 dB |
     | endPos 0.5 (adopted) | 1.54 s | 1.71 s | 16.6 dB |

     The decayLength for both endPos rows is 0.5.
   - **Full mix (master, c43 -> c44):**
     - Fermata at bar 170 (qn 679), drop at 0.15 / 0.3 / 0.6 / 1.0 s: 8.7 / 14.1 / 20.9 / 31.4 -> 10.3 / 19.6 / 29.6 / 43.9 dB.
     - Its slopes: late RT (-20..-35 dB) 2.13 -> 1.78 s; RT -5..-25 dB 2.42 -> 1.29 s. The recordings give 1.13-1.62 s.
     - Drop at 0.3 s at the other tutti cut-offs: qn 125.9 13.0 -> 19.4 dB, qn 288 13.6 -> 17.8, qn 551 -> 20.8.
     - The target was at least 13 dB at 0.3 s; it is met everywhere.
2. **Release caps (build/mix.json per track, read by `build_reaper.cap_release`).**
   - **Settings:**
     - every section string track, including aliases (Violins I / II, Violas, Violoncellos, Double basses, the f62 aliases): `"sus_release_cap_ms": {"ms": 150, "dyn": ["pp", "p", "mf", "f", "ff"], "rows": ["Sus MAX", "Sus Marc LITE"]}`. The patches ship 323-524 ms at mf-ff and 524-931 ms at p-pp.
     - every horn track (1FH and 2FH): `"sus_release_cap_ms": {"ms": 237, "dyn": ["pp", "mf", "f"], "rows": ["Sus MAX", "LegRep RRx4"]}`. 237 ms is the patches' own ff release; they ship pp 562, mf 394-422, f 316-374.
     - The DIV A solo (Cello solo) keeps its own cap.
   - **Stem drop at +0.15 s after a phrase end (median, c43 -> c44):**
     - Violins II -4.0 -> -9.9 dB, violas -4.9 -> -10.7, celli -5.7 -> -13.0, basses -6.5 -> -8.5, Violins I -9.0 -> -11.5;
     - horns -4.7..-6.2 -> -7.2..-9.2;
     - no string ending falls more than 10 dB in its first 0.05 s, so none sounds clipped.
   - **Violas' running figures:** the old pitch 70 ms into the next note is -3.6 -> -6.2 dB.
   - **Violins II détaché:** the old pitch reaches -10 dB 0.285 -> 0.254 s after the note-off.
   - **Re-bow fills:** they must be refitted afterwards (`tools/fit_rebows.py N parts --write`, level only, by stem fix). Before the refit the re-bow dips deepened from 1.7-4.4 to 5.4-7.7 dB; after it they are 3.1-5.4 dB, with median |step| 0.5-1.2 dB.
3. **Repeated string notes (`STR_REP_NEW_BOW`, generic, tools/score_to_parts.py).**
   - **Settings (build/score_config.py):** `STR_REP_NEW_BOW = {"gap_s": 0.06, "frac": 0.25, "stroke_cc": DYN["mf"], "stroke_mark": "mp", "head_cc": DYN["p"], "sus_min_s": 0.4, "portato": {"gap_s": 0.05, "frac": 0.25, "fall_cc": 6, "fall_cc_loud": 8, "fall_s": 0.04}}`.
   - **The rule.** It applies to a same-pitch string repeat that the legato merge would have joined into the note before.
     - If the repeat is in the same slur and has no tenuto, it stays merged.
     - Otherwise it is a **stroke** when it is accented, or its CC is mf or more, or the last printed mark is mp or louder, or it is a slur head at p or louder. A stroke is a fresh Sus MAX note on the DOWNBOW_STROKE_AT path, with the string re-tongue lead; the note before ends min(0.06 s, 25%) before it, and the gap is kept through the lead.
     - A slurred tenuto (louré) is a **portato** stroke: the same, with a 0.05 s gap and a 6 / 8 CC fall over the eighth's last 0.04 s.
     - Every other repeat is **soft**: it is merged, with a re-bow point at the printed onset (REBOW_AT machinery) in place of the CC11 notch.
     - Strokes take the ROW_TRIM_DB Sus row trims and keep their vibrato.
     - `sus_min_s`: unslurred Sus MAX -> Sus MAX repeats at mf or louder lasting 0.4 s or more get the same gap.
   - **Code sites:**
     - the default;
     - a classification pass after the articulation passes;
     - the merge loop: a stroke absorbs soft repeats; a soft repeat records a re-bow point instead of a notch;
     - a note-length branch;
     - `retongue_ok`: strokes take the re-tongue lead;
     - the row-trim exclusion;
     - the vibrato dip;
     - `rebow_at_t` at the output stage;
     - parts.json `rep_strokes`, `rep_rebows`, `rep_sus_gaps`.
   - **Movement I's counts:** 25 strokes (10 portato, 15 loud or slur heads), 24 soft re-bows, 23 Sus gaps. The 24 tremolo common tones stay merged.
   - **Dips (stem / master median, c43 -> c44):**

     | Class | Stem dip | Master dip |
     |---|---|---|
     | Portato | 2.3 -> 5.0 dB | 2.6 -> 3.6 dB |
     | Strokes | 2.9 -> 7.8 dB | 2.8 -> 4.5 dB |
     | Soft re-bows (target 3-5 dB in the stem) | 2.2 -> 3.9 dB | 1.6 -> 2.2 dB |
     | Sus gaps | 3.9 -> 6.4 dB | 1.3 -> 1.7 dB |

     The re-attack rise is 5.8-6.7 -> 9.4 dB.
   - **Levels.** At CC 68-88 the Sus MAX strokes came out 1.8-5.6 dB under the Leg BC level they replaced, and two viola strokes came out 2.6-6.2 dB over it. Measure each stroke's body against the note before and correct it by note trim with 0.1 s ramps.
   - **Not adopted:** a pre-hall CC7 dip over the portato gaps. It gained 0-1 dB on three of four repeats, 4 dB on one.
4. **Low end in soft passages (build/mix.json).**
   - **Celli:** the static `eq` bells 170 Hz +3 / 1.5 oct and 125 Hz +3 / 1 oct move into a `loud_eq` spec over the loud spans; `soft_trim_db` +1.7 at ppp / pp / p / mf.
   - **Basses:** the static 180 Hz +4 bell moves into a `loud_eq` spec; their soft level is not restored.
   - **Result:**
     - master soft-passage 100-200 Hz share -7.4 -> -9.0 dB (Dvořák -10.1); 157 Hz re 1 kHz -0.4 -> -3.5;
     - loud passages: 125 Hz third-octave re 1 kHz -7.3 -> -7.7, i.e. -0.4 dB, from the hall low cut and the drier hall.

## Run

**REAPER lock.** Movement II held REAPER from 09:59, then the scherzo from 10:50. The lock was held 11:18-12:51 (the turn rule did not apply, since Movement I did not hold REAPER last).

**Hall test (pass-2 project).**
- `reaper_ctl.py start`, `--pass2 open`.
- `build_reaper.py cycles/c44/halltest/parts.json cycles/c44/halltest/jobs --pass2 <6 test tracks>`.
- Two rounds of short renders (`render_halltest.py`) and the measurements above.
- Test tracks deleted, `--pass2 quit`.

**Main pass.**
- `start`, `open`, `build_reaper.py build/parts.json jobs`: tempo map and all 33 tracks fully rebuilt.
- `restart` (33 tracks, Mac Studio Speakers, no input, 48000 / 512), then `render_cycle.py 44`. Probe 0.
- **Stem fix:**
  - Horn 1 / Trumpet 1 / Violas contours out (B #1);
  - re-bow refit;
  - stroke trims (B #5);
  - letter-F brass +1 dB (B #4).
- The same data written with `--midi-only` on the 9 changed tracks, then `quit`.

**Pass 2.**
- `start`, `--pass2 open`, full build of all pass-2 tracks.
- REAPER crashed inside Opus while loading the Cello solo state (EXC_BAD_ACCESS in an Opus worker thread). The project had not been saved, so after a restart all eight pass-2 tracks were rebuilt again; the Cello solo loaded at the second attempt.
- `--pass2 restart`, `render_cycle.py 44 --pass2`: 40 stems summed, the "Vln I portato test" stem kept apart.
- Bar-158 stem fix (Violins I, Horns a2).
- Test track deleted from parts.json and the pass-2 project, Violins I f62 envelope written, `--pass2 quit`.
- Main: `start`, `open`, `--midi-only` Violins I / Horns a2, `quit`, `unlock`.
- `render_cycle.py 44 --measure-only` on the final stems.

**Records.** Snapshot `cycles/c44/before/`. Render-time builds: `rendered_build/` (main) and `rendered_build_pass2/`. Scripts in `cycles/c44/actor_scripts/`, hall test in `cycles/c44/halltest/`.

## Accepted

### ONE_TIME #1-#3 (drier hall)

See "Values" 1. In mix.json: `fx_volume` 0.095, `low_cut_hz` 160, `ir_setup` {envelopeMode 2, endPos 0.5, decayLength 0.5}.

**Exposed note ends.** The early ends that the drier hall could expose (C #5) do not sound clipped.
- Bar 62 (S3), master in the windows 0 / 0.05 / 0.1 / 0.2 s after the subito: c43 -1.9 / -5.1 / -8.3 / -11.7 dB, c44 -1.5 / -5.2 / -8.9 / -12.2 dB. This is the same smooth fall as before, so the f62 release shapes still fit.
- Fermata 679: c43 -3.2 / -4.8 / -8.4 / -13.1, c44 -3.8 / -6.5 / -11.2 / -16.9.
- No first-0.05 s fall exceeds 9 dB, so `CUTOFF_EARLY_S` stays.

### ONE_TIME #4 + A #1-#2 + B #5 (repeated strings)

See "Values" 3. Classification against A's list:
- **Portato:** all 10.
- **Strokes:** the 13 loud strokes plus the slur heads Violas 500 and celli 656. Violas 500, a new p after a decrescendo, counts as a stroke by the slur-head rule (head_cc p), as A asked.
- **Soft:** all 24. Each is a re-bow point at the printed onset.
- **Frozen re-bow points removed**, with their rebow_fills.json rows:
  - Violins II 189.62;
  - Violas 32.364, 39.353, 52.384, 686.694, 699.507;
  - celli 31.393, 39.879, 45.371, 51.87, 152.461, 163.877, 169.146.
- **Violas 36.856 moved to 38.65.** It sat 1.0 s after the printed re-bow at 36 (one of A's own double-event examples). The new point is the middle of the 36-40 whole note, kept 0.75 s clear of the basses' 38.003. A had listed 36.856 to keep, which contradicts its double-event list.
- **NOTCH_SKIP** celli 40 / 52 / 164 and Violas 52 removed.
- **Fill lists closed.** Fill lists that ended on a non-zero hold had held it to the next remaining list (Violas -6 dB from qn 40 to 713). Four lists are now closed where the removed list started (`close_fills44.py`).
- **Re-bow fills** refitted on the c44 stems: `fit_rebows.py 44 cycles/c44/rendered_build/parts.json --write`.
- **Stroke trims (B #5, note_trims.json, `NOTE_TRIM_RAMP_S` 0.1 s):**
  - celli 84 +2.4, 88 +2.8, 152 +5.0, 156 +5.5, 448 +1.8;
  - Violas 500 -6.0, 372 -1.5;
  - portato tenutos Violas 136 and Violins II 108 -2.5.
  - **Measure.** Stroke body minus the note before's body, in the same score windows as c43 so that printed hairpins cancel.
  - **After the trims** (`cycles/c44/bodies44.txt`), the non-accent strokes outside hairpins (Violas 372 / 500, celli 47 / 326 / 668) are within -1.7..+1.6 dB of the note before. Celli 84 (-3.8) and 374 (-5.6) keep c43's planned relation (-3.7 / -4.8), because the note before carries a fitted lift. Of the strokes inside hairpins, celli 152 / 448 / 456 match c43 within 1.4 dB, and the crescendo arrival 156 is 3.5 dB under c43's relation (+1.4 over the note before).
- **A's optional scope** (unmerged mf+ Sus repeats): implemented as `sus_min_s`. It caught 23 repeats (basses 15, violas 8); the others are REP_SPLIT strokes inside STR_REP_DETACH spans, which keep their dips.

### Critic C

- **#1 string release caps, #3 horn release caps:** see "Values" 2.
- **#4 low-mid EQ:** see "Values" 4.

### Critic B

- **#1, the c43 CC16 state.** It did not repeat after the full rebuild. Horn 1 and Trumpet 1's contoured Leg Slur notes and Violas 654.5 came out low by about each row's cut: Horn 1 195 -8.0 against a -9.3 cut, Trumpet 1 283.5 -16.3 against -14.5, Violas -4.7 against -5.6.
  - The "c43 stem fix" rows are switched off (`_C43_STATEFIX_ROWS = False`) and the levels restored by stem fix.
  - Per note against c43 final now: Horn 1 phrase medians -0.6..+0.4 dB, Trumpet 1 -0.8..-1.3. The hall predicts -0.8.
  - Bars 69-71, Trumpet 1 re M: -11.3 / -10.6 / -15.7 / -14.2 (c42 -11.0 / -10.6 / -14.9 / -14.0).
- **#2, bar 170.** Trombone 1 -3, Trumpet 1 (with its Trumpets a2 alias) +3 then +1. Trumpets a2 minus Trombone 1 per 1/4 qn, 676.5-677.75: c43 -6.3..-7.5, now -0.7..-2.4 dB (B simulated -0.4..-1.0).
- **#3, bar 158.** With the drier hall and horn releases, B's shapes overshot: Horns a2 minus (Violins I + flutes) -2.9..-7.0 dB.
  - The horn cut was undone and the Violins I lift halved (+0.75 / +1.25).
  - Result: -2.9 / -2.4 / -3.2 / -3.2 / -0.7 / +1.1 per 1/2 qn (c43 -0.5..+3.6).
- **#4 balance points re-checked after the drier hall (final stems, c43 -> c44):**
  - **Letter F**, tune minus brass: +5.4 -> +7.0 dB, outside B's 5-6 window. Horns a2 / Trombone 1 +1 dB over 388-406.5 gives +6.0.
  - **Bars 70-71**, tune minus counter: held (+4.1..+8.1 per qn).
  - **Bars 56-59**, violins minus counter: K median +4.2 (c43 +4.0).
  - **Horn 1 over Violins I at 498.5-499.5:** +3.5 / +3.9 / +1.7.
  - **Coda**, Trumpets a2 minus Violins I per bar: +4.4 / +7.5 / +9.8; minus Horns a2 +2.2 / +2.9 / +4.0.
  - **Timpani re M**, at 0-8 / 316-324 / 484-492 / 632-636 / 712-720: -6.8 / -12.7 / -16.9 / -14.4 / -14.2 (c43 -8.2 / -12.3 / -15.7 / -13.2 / -13.8). The opening solo is relatively louder because the strings lost more; the rolls are further under.
  - **Tam-tam re M:** -6.8 (fff) / -10.4 (pp).
  - No send was raised.

### c43 carry-over

Violas 78 leg_leads -0.07 s (it overshot by 63 ms in c43).

## Rejected or deferred

- **A #3 (Violins II / violas / celli short slurred notes to Leg Slur)** and **A #4 (divisi):** deferred. A #4 goes to the Blend cycle c45; A #3 needs a pcX refit of 23 shared onsets, which this cycle's state changes would have confounded.
- **C #2 (legato-row caps and release-trail gain as pass-2 tests):** not done. Violins II détaché reaches only 0.254 s (C's target 0.22): the RT trails (+12 dB, 1245-1741 ms) are the next lever. Test them in c45 with the `rt_ms` key or a new trail-gain key.
- **Portato CC7 dip (A #1 fallback):** tested as a pass-2 alias and not adopted.
  - Dip below the eighth at 60 / 108 / 140 / 572: 11.4 / 5.9 / 5.9 / 7.0 -> 12.5 / 5.8 / 6.2 / 11.1 dB.
  - Only 572 gained, and the master dip at 572 is still 3.7 dB (A wants at least 4 where the strings lead).
- **Horn 2 bar 59 on LegRep RRx4:** not done. Its re-attack can be judged on c44's drier tails first (horn repeat stem dips rose 2.4-3.2 dB this cycle).
- **c43 timing carry-overs:** only Violas 78 done. Letter G 468.5 / 474.5 / 476.5, basses 4.0, Bassoon 1, Horn 2 240, the f62 pair and tremolo 453 are left for a timing refit on the c44 render.
- **Not reached:**
  - the master dips of the strokes (median 4.5 dB) and soft re-bows (2.2 dB) are under ONE_TIME's 6 dB, which was written for winds and brass;
  - Violins I portato tenutos are 3.5-5.3 dB over the repeated eighth, which plays only 0.11-0.12 s after its gap and lead (A: at most 2);
  - the loud passages lost 0.8 dB at 100-200 Hz.

## Measured

**Master** (float sum of 40 stems): -17.3 LUFS, LRA 23.5 LU, true peak +2.4 dBFS, sample peak 1.313. c43: -16.9 / 23.5 / +2.3.

**Delivered** `cycles/c44/mvt1-mockup-c44.mp3`: -19.8 LUFS, LRA 14.9 LU, TP -1.8 dBTP, p10-to-max span 19.1 dB, limiter about 0.4 dB. c43: -19.7 / 14.9 / -1.8 / 18.9 / 0.5.

**Delivered S max:** 160 -11.5 > 122 -12.3 > 167-170 -13.5 > 26 -14.3; 158 -15.7, 117 -15.5, 140 -15.1, 131-134 -15.7, 69-72 -16.5. All within 0.3 dB of c43.

**Per-bar master against c43:** median -0.6 dB (p10 -1.4, p90 -0.1).
- Bar 84 is -7.2 dB. The sub. p after the ff of bars 82-83 had held the ff's hall tail. It is now a clean p, 3-4 dB lower, because the basses' soft bell was removed on purpose; there is no hole and no glitch.
- Lento bars 1-3 are -2..-4 dB (the hall and string releases).

**Attack probe:** 0 late or holes. Legato robust SD 49 / 42 / 52 / 50 ms (c43 43 / 40 / 50 / 48).

**Silent notes:** only the two known false alarms (Trombone 1 552, Timpani 727).

**Cut-off tails** (master; drops at 0.15 / 0.3 s, then the 60-250 Hz share of the 0.1-0.6 s tail):

| Cut-off (qn) | c43 drops | c44 drops | 60-250 Hz share c43 -> c44 |
|---|---|---|---|
| 55 | 6.6 / 12.7 | 9.7 / 22.8 | |
| 103 | 11.7 | 14.1 | |
| 125.9 | 7.3 / 13.0 | 12.4 / 19.4 | -6.0 -> -7.4 dB |
| 288 | 8.1 / 13.6 | 12.6 / 17.8 | -6.7 -> -6.3 dB |
| 551 | 9.9 | 14.3 / 20.8 | -7.7 -> -8.6 dB |
| 679 | 8.7 / 14.1 | 10.3 / 19.6 | -9.4 -> -9.8 dB |

**Families' drop at 0.15 s at 679:** wind -10.2 -> -13.1 dB, brass -7.9 -> -10.1, string -9.6 -> -8.8.

**S1 dips** (A's measure, medians, c43 -> c44): see "Values" 3. The per-note tables are `cycles/c44/reps44.txt` and `reps43.txt`. The master column of reps43 is c43's own master.

**pcX of the portato tenutos** against the winds' re-tongues (ms re score onset):
- bar 28 (qn 108): strings -26 / -14 / -5, Clarinet 1 +18;
- bar 79 (qn 314): celli -54, Horns a2 -54;
- bar 132 (qn 524): celli +46, Trumpets a2 +26, Trombone 1 -17;
- bar 168 (qn 668): violas -6, Horns a2 +44, Trumpets a2 +28.

A's ±30 ms target is met at 108 and 314, not at 524 or 668. Violins I 60 (+116) and Violas 136 (+211) are late: refit per onset on pcX in c45.

**Horn same-pitch repeats** (stem dip median, c43 -> c44): Horn 1 4.8 -> 7.2 dB, Horn 2 2.8 -> 5.4, Horn 3 3.3 -> 5.5, Horn 4 3.8 -> 7.0. Master +0.4..+1.0 dB.

**REAPER memory:**
- main project: 27 GB at start, 44 GB settled (0 compressed), 44 GB (18 GB compressed) after the render;
- pass 2 (7 tracks + 1 test): 10 GB at start, 19 GB settled and after (0 compressed).

## For c45

- Refit per onset on pcX: the portato and stroke leads (Violins I 60, Violas 136, celli 524), and the c43 timing carry-overs.
- C #2: the release-trail test on violas / celli (Violins II détaché 0.254 s, violas' figures -6.2 dB against C's -8).
- The per-mic width rebuild (MANUAL-GAPS #4) and A #4 divisi in the Blend cycle.
- The loud 100-200 Hz share: -11.2 dB against the Dvořák's -7.1.
- B's balance list again on c45.
