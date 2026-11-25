# Critic B, cycle 46 (render c45): balance and levels

## Manual notes (second reading of the c40 B row: May 2021 HO manual PDF pages 114-115, 154-155 and 158-159, read again in full, 158-159 also as images; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items that touch these pages come first, then the c40 B notes checked against the c45 render, then what the first reading missed.

| Source | What it says | Where it applies here | Followed in c45? |
|---|---|---|---|
| MANUAL-GAPS #12 (open; p.114 lists the kits' timpani and cymbal rows) | Recorded crescendo rolls ending on a stroke. | The 19 timpani roll spans. | **Still open, not needed for balance.** No roll covers a part because of its crescendo shape (finding 2 table, measured). |
| MANUAL-GAPS #6 follow-up (p.158 lists "Round Robin Reset" as an automatable parameter) | A second route to reset round robins. | Render-to-render repeatability. | **Followed in effect.** CC16 is sent in the pre-roll (c43). The 25 instances fully rebuilt in c45 for `width_by_mic` rendered within 0.15 dB of c44, and the main Violas stem matched c44 to 0.1 dB per beat outside its edited spans (measured). The large Violas difference in c45 is not a round-robin or state effect: it comes from different CC lanes (finding 1). |
| p.114-115 | Percussion sets; in the kits, velocity selects the dynamic layer ("up to 16" / "up to 12" levels), and CC11 plus velocity set loudness. | Velocities of the four percussion patches and the timpani. | **Followed, unchanged since c40** (read in parts.json). Tam-tam fff v124 = layer 11 of 12 and pp v60 = layer 4. Suspended cymbal v105 = upper of 2 layers. K Crash v124 = layer 6 of 7. Timpani strokes: pp v62 (layer 6); f v88-113; ff v99-112; accents v121; one v127. On the new measurement (K-weighted, finding 2 checks), the fff tam-tam is still the loudest stem for two bars (-7.1 / -7.3 dB re M at bars 122-123), with the brass sum 2.4-4.4 dB over it. The top layer (v126-127) is not needed. |
| p.154 | Humanizer: random note-on/off delay, velocity, tuning, volume, pan. | Not used. | **Followed** (read). None of the saved Opus states in `jobs/` holds a MIDI-tool `filters` entry. |
| p.154-155 | MIDI Compressor on velocity or one CC; notes under the threshold are not played. | Not used. | **Followed** (read, same check). |
| p.158 | Automation window, macro parameters. | Not used. | Not needed (unchanged). |
| p.159 | Remap a patch's CCs, "avoid conflicting MIDI CC messages"; MIDI Learn. | Every CC the pipeline sends: 1, 11, 15, 70 (5 string tracks), 7 (Timpani only), 36, 16, and 69 (strings). | **Followed** (read from every main-project state's `MidiControllerMap`). Each sent CC maps to its own number. No state maps CC16. The only remap is 1TU "Legato" 68 -> 57, which is not sent. The c36 CC7 test lane on Trombone 1, still present at c40, is gone: the Timpani carry the only CC7 lane. |
| New (p.159 picture) | String states also map CC5 "Legato Time". | Not sent, so the patch default applies. | Consistent. Legato timing is set by leads and velocity, as in every cycle. |

## Method

- **Data.** The final c45 stems (40) and master, against the final c44 stems. Build data: `build/` (= final c45), `cycles/c45/before/` (= final c44), `cycles/c45/rendered_build_pass2/parts.json`, `cycles/c45/render_first/` (c45 main-pass stems before the stem fix) and `cycles/c45/render_pass2/` (the test stems).
- **Frames.** 4096-point FFT, 50 ms hop. Each frame stores A-weighted power for L, R, mid and side, K-weighted (BS.1770) stereo power, and 1/3-octave band power.
- **Notation.**
  - "re M" means stem minus master over the same window.
  - The f62 aliases are summed into Violins I / II, Cello solo into Violoncellos, and the stac aliases into their sources.
  - I use K for balance across registers and A where earlier reports did, and say which in each case.
- **Simulations.** Each simulation scales a stem's frame powers by the proposed shape and adds the change to the master as power.
- **Delivered mp3.** Short-term loudness: K-weighted power in 3 s windows on the decoded mp3.
- **Score.** Pages 2, 3, 4, 5, 9, 10, 11, 12, 14, 17 and 18 read.
- **Scratch.** Scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c46-B/` and are deleted at the end.

## Findings, ranked by what a listener would gain

### 1. The c45 Violas stem is a test alias with different CC1 / CC11 lanes: the violas are 3-7 dB too loud in bars 34-38, 44, 129, 135-136 and 145, and in bar 34 they cover the Bassoon 1 solo (measured; cause read in the data and code)

**What happened (measured).**
- c45 replaced the Violas stem with the pass-2 "Vla rt test" stem, which was supposed to play the Violas' own notes and envelope with release-trail gain -6.
- Per bar against the c45 main-pass Violas stem (`render_first`), the test stem is:
  - median -0.03 dB (p10 -0.5, p90 +0.8: the trail gain);
  - +6.7 / +5.8 / +3.0 / +2.6 / +2.8 dB in bars 34-38;
  - +3.9 in bar 44, +2.2 in bar 129, +3.4 / +2.7 in bars 135-136, and +6.3 in bar 145.
- The main-pass stem itself matched c44 to 0.0 dB everywhere except the intended fill-end change (bars 146-172, -4.1 dB). So the rise does not come from the render or the instance.

**Cause (read).**
- In `rendered_build_pass2/parts.json` the alias has the same notes, keyswitches, CC70 and `vol_db` as Violas, but not the same CC1 and CC11:
  - CC1 is +40..+55 over qn 128.5-157.3, 162.75-183.75, 507-549 and 573.9-582.75 (17.5% of the track). The alias gets 95-105, the vibrato target of a boost span; Violas gets 55-66.
  - CC11 is +3..+4 over 132.25-149.6, 165-183.75, 507-513.7 and 573.25-582.75.
- The source of the difference is `tools/score_to_parts.py`, in the boost-span loop (about line 3024):
  `if tname in TRACK_WINDOWS and tw_spans(tname)[1]: stop = min(txt_stops_ + [tw_end(tname, q)])`.
  - c10 added this so that a solo alias's boost covers its window. For an alias whose window is the whole piece, it carries the violas' "espr." at qn 72 to the next text (qn 184) and the "espr." at 424 to qn 583.
  - The source track stops each boost at the next rest of 3 qn.
- The same rule touched the other c45 test aliases:
  - **Hn1 rt test:** CC11 +8 over 55-96 and 176-184, and up to +42 over 218.8-272.4 (24.6% of the track).
  - **Vla leg test:** the same lanes as Vla rt test.
  - **Vln II rt test and Vln II leg test:** about 1% only.

  So the c45 decisions "trail gain not adopted on Horn 1" and "A #4 not adopted on violas" were judged on test stems whose lanes did not match their sources (inferred: the bias depends on whether the measured notes fall inside those spans).

**What the listener hears in c45 (measured, A per qn re M, c44 -> c45).**
- **Bar 34**, the Bassoon 1 "Solo espr." (f > mf) against the violas' mp answer:
  - Bassoon 1 minus Violas per qn 132-135: +4.6 / +4.0 / +6.8 / +6.6 -> -2.9 / +4.0 / +1.4 / -4.8.
  - Bassoon 1 minus the loudest other stem over 132-136: +5.4 -> -0.9.
  - Bar 34 (K): Violas -6.7 -> -2.6 re M, Bassoon 1 -1.6 -> -3.7. The violas are now the loudest stem of the bar.
  - In the F4 band, the eighth and tenuto at 135.3-136.5 are 12-16 dB over c44. The c45 +6 dB eighth lift was fitted on the main-lane render and lands on top of the louder test stem.
- **Bar 35**, Violins I mf enters with the motif: Violins I minus Violas per qn 136 / 137: +11.1 / +9.2 -> +1.5 / +2.1.
- **Bar 44, beat 4 (pp pickup):** violas -4.6 -> -2.6 re M, the loudest stem.
- **Bar 145**, the pp chord before the oboe's dolce: violas level with Violins I (-0.0 / -0.6 dB at 576-577; c44 +5.7 / +5.7).

**Fix.**
- **(a) Tools, `score_to_parts.py`.** Apply the window-end boost rule only to solo aliases: skip it for names in `TEST_TRACKS`, and for any alias whose window covers its source's whole note range. Those aliases then stop boosts at rest starts, as their source does.
  - Rebuild parts.json and diff the production tracks against the current build (`cycles/c45/actor_scripts/pdiff45.py`). Cello solo, the f62 aliases, Trumpets a2 and the stac aliases should come out byte-identical; if one changes, list it in a `BOOST_TO_WINDOW_END` set that keeps the old rule.
- **(b) Process.** Before a test stem replaces a main stem, diff the alias's parts.json track against its source:
  - notes, ks, cc1, cc11, cc70, cc7 and vol_db must be equal, apart from the key under test;
  - the stems must agree per bar to within 1 dB outside the tested effect.
- **(c) Check on the c46 render.** The c46 main pass plays Violas on its own lanes (the instance was rebuilt with the trail gain), so I expect bars 34-38 / 44 / 145 back at the `render_first` level (inferred). Check per bar against `cycles/c45/render_first/30_Violas.wav`: within ±1 dB outside 146-172 and outside 135.2-136.5, where the eighth lift and tenuto shape apply. Keep the c45 eighth row, which was fitted on these lanes.
- **(d) Fallback,** only if c46 still shows the violas 2 dB or more over `render_first` in bars 34-35. Add to `build/score_config.py`:
  ```
  LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(132.1, 0.0), (132.2, -6.0), (135.9, -6.0), (136.3, -4.0), (137.9, -4.0), (138.2, 0.0)],
                                                     [(174.8, 0.0), (175.0, -3.0), (175.9, -3.0), (176.1, 0.0)],
                                                     [(575.4, 0.0), (575.6, -3.0), (577.9, -3.0), (578.2, 0.0)]]
  ```
  This is level only, so it can go in as a stem fix.
  - Simulated on the c45 stems (with the eighth lift also removed, since there the lift sits on the alias):
    - Bassoon 1 minus Violas at 132-135: +3.1 / +10.0 / +7.4 / +3.9.
    - Bassoon 1 over the loudest other stem at 132-136: +6.0.
    - Violins I minus Violas at 136 / 137: +5.8 / +6.1.
    - Bar 145: +3.0 / +2.3.
- **(e) Re-test.** If lens C still wants the trail-gain test on Horn 1 (or A the shared-eighth legato test), run it again after (a).

### 2. Every timpani roll checked (Dan's priority): none covers the texture except in the bass band at bars 13-14 and bar 174 (measured; fix simulated)

Per 1-qn window over each of the 19 roll spans (K re M, rank among 34 stems, and the roll minus the loudest other stem in its band f0/1.26..2.52 f0; c45):

| Roll (bars, printed) | Max K re M | Best rank | Max band margin |
|---|---|---|---|
| 1-4, ppp, solo opening | 0 (alone in bar 1) | 1, then 3-4 once celli and bass clarinet enter | (alone) |
| 11-12, pp < f | -9.1 | 2 | +2.1 |
| **13-14, p > pp** | -15.0 | 3 | **+7.6 over basses / celli** |
| 40, pp < f | -11.3 | 4 | -5.2 |
| 41-43, ff > pp | -14.0 | 5 | -0.2 |
| 62-63 | -12.5 | 5 | +2.6 |
| 71 | -14.1 | 12 | -0.1 |
| 76, ppp | -9.4 | 5 | -3.3 |
| 80-81, p < ff | -8.3 | 4 | -1.2 |
| 115 | -17.7 | 20 | -3.3 |
| 117-130, G pedal | -10.3 | 3 (bars 124-125 decrescendo only) | +4.6 at 497 |
| 140 | -15.3 | 12 | -4.2 |
| 144-146, mp > pp | -7.3 | 2 (only at 572-572.5, then decays) | +2.1 |
| 158-161 | -10.9 | 4-5 | +1.7 |
| 166-169, p < f | -10.3 | 1 (only at the bar-167 arrival, 664-664.5) | +0.1 |
| **174, pp** | -13.5 | 3 | **+13.8 over the bassoons** |
| 181-182, ppp | -12.7 | 7 | -4.0 |

The roll is never the loudest stem while another part leads. The c45 B #3 fix holds: celli minus roll at 79-125 Hz is +6.3..+13.5 dB at bars 127-128. Two places remain where the roll, at the same printed level, takes over the bass band from a part playing the same pitch.

**Bar 174 (qn 692-696).**
- *Score.* Under the end of the cello solo, Bassoons 1-2 hold G3 / G2 pp and the timpani hold a pp G2 roll.
- *Measured.*
  - The roll is the whole master band from 78 to 250 Hz (re M 0.0 / +0.3 / -0.8 / -1.5 dB per qn).
  - It is 8-14 dB over the louder bassoon there.
  - K re M -16.4, rank 3, after the solo cello and the cor anglais.
- *Cause (read).* The roll carries `build/roles.json` Timpani `[692, 696, 6]`. c04 B #2 set it for v221, when the roll measured 10-12 dB under the violas.
- *Fix.* `roles.json` Timpani `[692, 696, 6]` -> `[692, 696, 2]`.
  - Simulated: K re M -20.3, rank 6; band margin over the bassoons +10.4 -> +6.4 dB on the bar; master -0.06 dB.
  - The roll stays the low layer, but it no longer replaces the bassoons' G2.

**Bars 13-14 (qn 48-55).**
- *Score.* The timpani p > pp roll on G under the Horn 1 solo, with celli and basses p > pp on the same chord.
- *Measured.*
  - Bar 14: the roll is +6.2 dB over the celli in its band; the timpani take 69% of the master's 50-250 Hz (-1.6 dB re M).
  - K: the roll -15.7, celli -14.3, basses -24.0.
- *Fix.* After the printed p onset:
  ```
  LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(48.5, 0.0), (49.5, -3.0), (55.3, -3.0), (56.0, 0.0)]]
  ```
  This is level only, so it can be a stem fix.
  - Simulated: bar 14 band margin +6.2 -> +3.2 dB; roll K -18.6; master -0.06 dB.
  - The roll still starts at its printed p and then settles under the strings, as rule 5 asks.

### 3. Letter F (bars 98-102): on each downbeat the trombone and horn half notes (printed f) reach the level of the ff tune; the c43 / c44 lift meant for their answering figure also covers the half notes (measured; fix simulated)

**Score (p.9).**
- The tune is ff in Flute 1, Oboe 1, Cor anglais, Violins I / II and celli.
- Horns a2 and Trombone 1 (f) answer with a half note on beat 1, then three eighths.

**Current data (read).**
- `build/score_config.py` lifts Horns a2 and Trombone 1 over the whole passage: +3 dB (c43 B #2) plus +1 dB (c44 B #4), and `PICKUP_LIFT` +6 on the first eighth.
- The point was that the answering eighths should be heard.

**Evidence (measured; tune = power sum of the six tune tracks, brass = horns, Horns a2, Trombones 1-2, Bass trombone; per 2 qn from 388).**

| Measure | Beats 1-2 (half notes) | Beats 3-4 (eighths) |
|---|---|---|
| Tune minus brass, K | +2.1 / +1.5 / +2.4 / +4.8 / +2.2 | +5.8 / +7.1 / +2.0 / +2.9 / +7.3 |
| Tune minus brass, right channel (the trombones sit right) | +1.8 / -0.1 / +0.7 / +2.7 / +0.4 | |

- At 388, Trombone 1 alone is 1.6 dB over Violins I (K).
- The bar-averaged A margin, which c44 B tuned to its 5-6 dB window, hides this. On my tune set it is +4.6.
- The c45 width change did not alter it: per channel within 1 dB of c44.

**Fix.** Keep the lift on the figure and take it off the half notes. Add for each bar:
```
for b_ in (98, 99, 100, 101, 102):
    q_ = 4.0 * (b_ - 1)
    for t_ in (("Trombone 1", "Horns a2") if b_ < 102 else ("Trombone 1",)):
        LEVEL_SHAPES[t_] = LEVEL_SHAPES[t_] + [[(q_ - 0.30, 0.0), (q_ - 0.20, -4.0), (q_ + 2.10, -4.0), (q_ + 2.25, 0.0)]]
```
The ramp starts before the moved onsets (Trombone 1 387.851, Horns a2 387.893). It is level only, so it can be a stem fix.

**Simulated.**
- Downbeat tune minus brass (K): +5.1 / +4.0 / +4.9 / +6.9 / +4.1. Right channel: +5.1 / +2.2 / +3.6 / +5.1 / +2.9. Beats 3-4 are unchanged.
- The bar-median A margin is 6.3, in c44 B's window.
- Master K -0.4..-0.7 dB on the downbeats only.

**Optional.** `PICKUP_LIFT` 398.5 6.0 -> 3.0 on both tracks. Bar 100's figure is the one beat-3-4 window left at +2.0 dB.

## Checks with no change proposed (measured on the final c45 stems)

**The c45 level edits against their printed dynamic and role** (the coordinator's question). The only edit that sits above its role is the Violas stem swap, together with the eighth lift on top of it (finding 1). Every other edit is in line:

| Edit | Measured result |
|---|---|
| `REBOW_FILL_END_S` | Violins II +2 dB over bars 147-175 stays accompaniment: -17..-10 dB A re M under the bars 147-155 tune, and Violins I over Violins II +1.1..+3.5 at 160-166. Violas minus celli 147-150 +0.1 dB. |
| Celli +3.5 / timpani -2 at bars 127-128 | Celli minus roll +6.3..+13.5 dB at 79-125 Hz. The clarinet solo margin is still +13.9 dB A. |
| Celli body cut at bars 39-40 | Celli minus the loudest other stem -4.6..+1.2 dB. Step into the bar-41 sf +7.0 dB. |
| Celli / basses `loud_eq` spans | Celli + basses -13.6..-21.7 dB A re M in those spans. The Violins I theme margin at 69-72 is +4.3 dB (c44 +4.2). |
| 34 fill entries and the portato shapes | All are holes filled within 0.5 s. No stem is louder than c44 by 1.5 dB in any bar outside the violas bars and the intended spans, apart from two quiet bars 24-30 dB under the master (Horn 1 bar 135 +3.0, Horns a2 bar 80 +3.2). |
| Trumpet 1 shelf to 644.5 | Melody at 636-640 over the loudest other stem +0.4 -> +1.0 dB. |

**Width (`width_by_mic`), balance by role per passage (A; mid and L / R separately).**
- In 24 melody passages (bars 5-8 through 175-177), the melody's margin over the loudest other stem moved by 1 dB or less in stereo, in mid and in each channel. The exceptions are the violas bars of finding 1 and the 147-150 trio, which lost the violas' intended -4.
- The solos' side/mid rose 2-4 dB:

  | Solo | Side/mid, c44 -> c45 (dB) |
  |---|---|
  | Cor anglais, bars 5-8 | -10.9 -> -8.7 |
  | Clarinet 1, bars 45-46 | -12.0 -> -8.2 |
  | Oboe 1, bar 145 | -9.6 -> -6.6 |
  | Flute 1, bars 73-75 | -11.1 -> -9.3 |

  The solos are wider but still focused, and no margin changed. Main 0.2 on the solo tracks (lens C's c46 item) would not affect balance.
- Master L-R per section is within 0.2 dB of c44. Bars 55-68 lean left by 3-6 dB because the cantabile violins sit left; that is the seating, not a level fault.

**Dynamic mapping (K; beats where at least four tracks share one flat printed dynamic, each track minus the beat median).**
- Each family is within ±2 dB at every dynamic from pp to fff:
  - winds -1.3..+2.0;
  - horns -1.7..+0.4;
  - trumpets +0.3..+1.8 (Trumpet 1 +1.1 / +4.0 / +3.2 at f / ff / fff as the lead, Trumpets 2-3 -0.4..+0.6);
  - trombones and tuba -1.7..+1.7;
  - timpani -0.8 at pp, +1.8 at f;
  - strings 0.0..+2.6.
- Percussion: tam-tam pp -6.0 (soft stick, l.v.) and fff +7.7.
- Second winds sit 3-6 dB under the firsts at f (Clarinet 2 -6.3, Oboe 2 -4.5, Flute 2 -3.0). These are inner and lower voices, as in c44.

**Rimsky-Korsakov's ratios (Principles, "Comparison of resonance").**
- At f a horn should equal two woodwinds and a trumpet or trombone two horns, about +3 / +6 dB over one woodwind.
- Here, over the woodwind median at f: horns +0.9, trumpets +1.5, trombones +1..+4. The brass are on the light side.
- Most f brass beats in this score accompany an ff theme, where c39-c40 measured brass lifts covering the tune. No general change; finding 3 is the one place where the balance tips the other way.

**Climax order (delivered mp3, 3 s K windows).** 160: 0.0 > 122: -0.7 > 167-170: -2.0 > 26: -2.7 (dB re bar 160). Findings 2 and 3 change the master by -0.06 dB and by -0.4..-0.7 dB at letter F only.

**Low end.** Loudest 10% of master frames, re 250 Hz-2 kHz: 40-100 Hz -15.5 dB (c44 -15.8), 100-250 Hz -8.8 (c44 -9.4). The c45 bells added low-mid, not boom.

**Do not touch:**
- the c45 B #1-#4 data: `REBOW_FILL_END_S`, the bars 127-128 celli / timpani shapes, the bars 39-40 celli body cut, and the `loud_eq` spans;
- the Violas 136 eighth row (it fits the main lanes; it only compounds on the alias stem);
- Violas `rt_gain_db` -6 (judged on running figures outside the mismatched spans);
- `width_by_mic` and the zeroed side low cuts;
- the hall values and every send;
- the 150 / 237 ms release caps;
- the tam-tam fff / pp and the suspended-cymbal and K Crash rings;
- every timpani roll level outside bars 13-14 and 174, `TIMP_CC1_MAP` and `TIMP_RH_ALT`;
- the letter-F beats 3-4 lift and `PICKUP_LIFT` (apart from the optional 398.5);
- the climax set, and the Trumpets a2 coda fit;
- plus every c45 and earlier do-not-touch item.
