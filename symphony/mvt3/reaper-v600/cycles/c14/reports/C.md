# Critic C, cycle 14 (dynamics over time), on the c13 render

Lens: hairpins and phrase shapes, the loudness arc against the score, the loudness range of the master and the delivered mp3 (BRIEF item 6), loop pulsing (item 7), timpani rolls (item 5), decays and the final chord. Measured on `cycles/c13/render/` (35 stems, `00_Master.wav`) and `mvt3-mockup-c13.mp3`, on the parts.json tempo map: K-weighted levels per bar, half bar and quarter, BS.1770 short-term and momentary curves, 10 ms stem envelopes, the CC and volume lanes of `build/parts.json`. Delivery changes were simulated by running `tools/deliver_master.py` unchanged on the c13 master with edited `ride_trims` in a scratch copy of parts.json. Score pages 1, 3, 14 were rendered and read; `mockup-events.tsv` gave the printed marks. Research files read: FINDINGS Parts 1-6, EW-TEMPLATE-PLAN, the research sections of BRIEF.

## Manual notes (third round, own pages: May 2021 HO manual PDF p.61-64, 103, 123-125; MANUAL-GAPS.md read)

| Manual (PDF page) | What it says | Where in this mockup | Does the c13 render follow it? |
|---|---|---|---|
| p.64 | On the MAX strings and woodwinds CC11 sets loudness and dynamics and is the lane for "continually changing dynamics"; CC7 is for level between instruments; velocity sets loudness on short rows. | Every printed hairpin. The three-bar diminuendo of bars 39-41 (qn 152-164). | Lane yes, shape no. Violins I/II hold CC11 114 -> 90 until qn 163.4 and drop 90 -> 46 in the last 0.6 quarter (0.22 s), so the printed diminuendo is a 10 dB step at bar 42 (finding 2). Measured. |
| p.63 | Every instrument fades to silence on CC11 (the old "Ni" patches are gone because of this). | "dal niente" at Clarinet 2 qn 184, Clarinet 1 qn 200, Clarinet 2 and Bass clarinet qn 680. | No. CC11 is constant (34) from before each note; the stems are at their full pp level 0.1-0.2 s after the note-on (finding 6). Measured. |
| p.64, p.101 (c10 reading) | CCs change during a note; brass Sustain crossfades four layers on CC1, so a held note can grow or fall. | Long brass and wind notes without a printed hairpin (the chorale 892-936, 1016-1048). | Partly. 42 % of the chorale's 78 long brass notes move less than 1 dB from their first to their last third (finding 6). Measured. |
| p.103 | "Sforzando Crescendo" exists only for the Solo Horn and Solo Tuba; velocity sets the attack and the crescendo. | The sfp < ff of bar 149 (qn 592-596) on trumpets, trombones, timpani, strings. | Not available for these sections, and not needed: master (K, per eighth) sf -15.4, p -24.9 at +0.3 s, ff -12.5 at 596. MANUAL-GAPS "Sfz Cres" stays closed. Measured. |
| p.124-125 | Timpani Rolls: CC1 crossfades 8 dynamic levels for crescendos and decrescendos; CC11 and velocity set loudness. Recorded crescendos (Cresc row) have 2 velocity levels and three fixed speeds. | Crescendo rolls 832-839, 872-888, 970-980, 1040-1048, 1096-1102. | Yes. The CC1 rolls grow about 14 dB from the p after the fp (832-839), 27 dB (872-888, p to fff), 13.7 dB (970-984), each with the texture. The Cresc row is not needed (MANUAL-GAPS #12 stays closed). Measured. |
| p.123-124 | Long hits have up to 16 velocity levels and a x2 round robin; strokes closer than 65 ms trigger double hits. | Timpani strokes and roll heads. | Yes (read in parts.json: the closest two timpani note-ons are 170 ms apart, so no double hit is triggered). |

## State through this lens (measured)

- Master -20.6 LUFS, LRA 23.0 LU, short-term p10 -41.7, max -12.4 (bar 223). mp3 -19.8 LUFS, LRA 14.6 LU, p10 -30.2, max -11.1, span 19.1 dB, limiter 2.3 dB. 203 five-second moves of 3 dB or more, median 81 % kept, 2 inversions by the 3 s measure (bars 114.6 and 170.3; the first is an artefact of the window: at quarter resolution bar 114 falls 4.7 dB in the mp3).
- Climaxes, momentary maximum, master / mp3: bar 223 -10.5 / -9.5, bar 278 -10.4 / -9.3, bar 263 -11.6 / -12.2, bar 150 -12.4 / -13.4. The order is right.
- Timpani rolls (item 5): in 0.5 s windows the timpani stem is the loudest stem in one window only (the first stroke at qn 920, +3.0 dB). Every roll without a hairpin settles (584-592: -29.7 to -35.2 dBFS; 920-933: -32.8 to -41). Bar 278 is the exception: -26.8, -26.4, -25.1 dBFS over its three half seconds, 0.9 dB under the loudest stem, while the master falls 1.8 dB. If one thing is changed there, lower the plateau of the 1108.0 `LEVEL_SHAPES_S` row from +4 to +2.5 dB.
- Loop pulsing (item 7): none. Master autocorrelation at 3.95 s, 100-300 Hz band / centroid: 168-200 -0.01 / -0.17, 888-936 -0.16 / -0.12, 1088-1108 -0.29 / +0.14, 548-584 -0.38 / -0.23, 264-300 +0.10 / +0.14. Only four notes sound longer than 6.5 s (Horn 4 at 168, the timpani roll at 920, two crash rings). Re-bows in the pp pedal 168-200 move single stems 3-5 dB but the master stays within 2 dB.
- Stops and wetness: every tutti stop decays in even steps of 2-3 dB per 50 ms from the release, with no kink where the celli / basses fades act; none is gated or cut off. Master at +0.30 s: bar 2 -14 to -16 dB, bar 6 -17, bar 94 -17, bar 113 -19, bar 166 -16 to -20, bar 204 -15. Bars 113 and 166 are 2-4 dB drier than the 13-17 dB of the recordings; the rest are at the dry edge of that range. The mix is not too wet. Do not dry it further.
- Final chord: one tied chord from qn 1108 to 1113 (every staff, percussion included, is tied over the barline). The sustained stems fall 1-3 dB over its 2.1 s, the master -10.4 to -13.2 dBFS (the crash and bass drum decaying). After the release: -20 dB at 0.45 s, -40 dB at 0.85 s, -60 dB at 1.35 s, smooth to -85 dBFS. The mp3 keeps 2.7 s after qn 1112 and ends at -90 dBFS. Nothing to change.
- Against the Dvořák 9/i reference, short-term percentiles relative to the file's maximum: p25 -20.3 (reference -20.9), p50 -14.4 (-14.5), p75 -8.6 (-4.8), p90 -5.4 (-2.2). The lower half of the distribution matches. The mockup's ordinary ff tuttis sit 3-4 dB further under its peaks than the recording's do. Another piece, so this is context, not a finding.

## Findings

### 1. A hole at the downbeat of bar 222, one bar before the C-major arrival (measured; same in every render from c09 to c13)

**Where:** qn 884.0-885.0 (bar 222: printed f inside the p < mp < f < fff build, allargando). Violins I, Violoncellos, Violins II, Trumpet 1, Horn 1.

**What is wrong:** the crescendo of bars 219-222 rises to the end of bar 221, drops 4-5 dB for half a second at the bar line where f is printed, and then recovers. Master, K-weighted per quarter from qn 880: -28.3, -24.1, -19.7, -18.0, **-21.3**, -17.5, -15.5, -15.1, then -10.7 at 888. Master 100 ms level: -17.6 dBFS before the bar line, -22.2 at +247 ms, -17.9 after. The per-quarter master is within 0.4 dB of these values in c09, c10, c11, c12 and c13, so this is data, not drift.

**Evidence, per stem:**
- Violins I: the unslurred half note B5 at 884.0 repeats a pitch of the bar-221 chord and is played on "Leg Slur MAX" (keyswitch at 883.94), i.e. on the slow first-note layer. Stem -29 dBFS before, -58 at +0.15 s, -47 at +0.5 s, -38 at +0.8 s, -32 at +1.1 s. Per quarter: 883 -28.6, 884 -38.1, 885 -34.9, 886 -35.3, although CC11 goes 86 -> 96 -> 112 -> 117.
- Violoncellos: the whole-note G2 of bar 221 (Sus MAX, CC11 65 -> 86, volume +2.9 -> +5.1 dB) swells to -21.3 dBFS in its last quarter, 8 dB over the same section's fff tremolo at 888 (-32.0). The D3 at 884 is at -32.1, so the cello line falls 10.8 dB at the bar line (finding 5 is the cause).
- Violins II fall from -26 to -36 dBFS at +0.2 s (new-bow gap), Trumpet 1 and Horn 1 enter mf and need 0.5 s to rise from -49 / -45 to -33 / -36.

**Fix (`build/score_config.py`):**
1. Violins I: play the note at 884.0 as a new bow on "Sus MAX": `ART_SPANS["Violins I"] = ART_SPANS.get("Violins I", []) + [{"from": 883.9, "to": 886.0, "art": "Sus MAX"}]`. Check in parts.json that the keyswitch at 883.94 is gone and the 0.09 s plain gap before 884 stays.
2. Violoncellos G2 at 880: the pitch trim of finding 5 (-5 dB). If finding 5 is not taken, a `LEVEL_SHAPES["Violoncellos"]` row `[(881.0, 0.0), (883.0, -5.0), (883.85, -5.0), (884.0, 0.0)]`.
3. Trumpet 1 and Horn 1, fronts at the mf entry: `LEVEL_SHAPES_S` `(884.0, [(-0.05, 0), (-0.03, 4), (0.30, 4), (0.55, 0)])`.

**Targets:** Violins I stem at 884.0-884.5 at or above -36 dBFS (Violins II's level there); master 100 ms level nowhere in 884.0-884.6 more than 2 dB under the mean of 883.0-884.0; master per quarter non-decreasing from 880 to 888 within 1 dB.

### 2. The diminuendo of bars 39-41 is delivered as a 10 dB step at bar 42 (measured). The p of bar 42 is the hairpin's target, not a subito

**Where:** qn 152-164, Violins I, Violins II, Violoncellos, Trombone 1; tool rule `HP_CURVE["decresc_last"]`.

**Score:** every string, wind, horn and trombone staff and the timpani carry a diminuendo hairpin from the ff / f of bar 39 to the p of bar 42 (score page 3; `mockup-events.tsv` decresc starts at 152.0 and 156.0, parts.json `hairpins` [152, 164, "decresc"] on all five string tracks). Earlier reports and HISTORY call bar 42 a "subito p" and protect it. The print does not support that.

**What is wrong:** master, K-weighted per two quarters from 152: -22.1, -25.3, -27.2, -28.5, -28.5, -30.1, then -37.2 and -42.7. Bar 41 does not fall at all (per eighth, 160.5-163.5: -28.5, -26.8, -28.7, -29.8, -30.0, -30.6, -29.9), then the level drops 8 dB within two eighths (164.0 -34.3, 164.5 -38.0). mp3 bar 41 -> 42: 9.6 dB.

**Cause:** `HP_CURVE = {"decresc_last": 0.35}` keeps 65 % of the fall for the hairpin's last onset. On Violins I/II, Violoncellos and Trombone 1 the last onset is the eighth at 163.5, 4 % of the hairpin's length. CC11: Violins 114 -> 90 by 163.375, then 90 -> 46 by 164.0 (44 of 68 CC in 0.22 s); Violoncellos and Trombone 1 88 -> 73, then 73 -> 46. Violins I stem: 162-164 -33.9 dBFS, 164-166 -45.3 (11.4 dB). Violas and basses, whose last onset is 160.0, get a knee at 160 and step only 3.2 dB at 164. The same rule puts 28 of 42 CC into the last 0.18 s at 668-676 (Violoncellos) and 673-676 (Violins I/II); that place is masked by the thinning texture (master 664-680 falls 3-5 dB per bar).

**Fix:**
1. `tools/score_to_parts.py`, the decresc branch near line 2014: two new keys. A hairpin longer than `HP_CURVE["decresc_last_max_qn"]` stays linear; a last onset closer to the stop than `HP_CURVE["decresc_last_min_s"]` seconds is not used (take the previous onset that qualifies, else linear). `build/score_config.py`: `HP_CURVE = {"cresc": (0.4, 0.7), "decresc_last": 0.35, "min_qn": 1.0, "decresc_last_max_qn": 6.0, "decresc_last_min_s": 0.35}`. Linear CC11 is already late-weighted in dB (about 1.2 dB per 10 CC above 88, more below), so a long hairpin needs no knee. All five string tracks then share one curve over 152-164 (research batch 7 item 4).
2. Expected CC11 on the violins: 114 at 152, 91 at 156, 68 at 160, 57 at 162, 46 at 164.
3. Refit the delivery ride for this passage afterwards (finding 4).

**Targets:** master bars 39 / 40 / 41 / 42 about -23.5 / -28.5 / -33.5 / -38.5 (K), each bar 4-6 dB under the one before; no two-quarter step over 5 dB between 152 and 168; Violins I stem 162-164 within 5 dB of 164-166. Record in HISTORY that "bar 42 subito" leaves the do-not-touch list.

### 3. The stringendo of bars 245-246 sags instead of growing into the Più allegro (measured)

**Where:** qn 976-984. Violins I; Horns 1-2, Trumpets 1-2.

**Score (page 14):** every string staff prints "cresc. molto" with dashes from bar 244 to the ff of 247; oboes p < f, clarinets and bassoons mf < f, timpani roll p < f, stringendo.

**What is wrong:** master, K-weighted per quarter from 972: -23.6, -23.6, -22.2, -19.8, -21.5, -20.3, then **-23.9, -22.2, -23.3, -22.7, -21.1, -22.3**, then -20.0 and -18.3 at 984-985. The six quarters before the arrival are 2-4 dB under the two bars before them, and the Più allegro enters with a 3-5 dB step.

**Evidence:**
- Violins I: parts.json has the hairpin as [972, 978] only (the dashed line stops at the rest of 978-980), and the lone-swell rule returns it toward mf. In the unison scale of bar 246 Violins I plays at CC11 79-80, Violins II (the same scale an octave lower) at 107-112. Stems per quarter 980-983: Violins I -40.0, -44.7, -40.0, -37.3; Violins II -35.7, -37.0, -33.8, -30.3.
- Horn 1 and Trumpet 1 hold their last tied note 978-983 while the phrase shape tapers: Trumpet 1 CC1 88 -> 78 over 980.9-982.9, Horn 1 109 -> 105. Stems: Trumpet 1 -34.5, -33.5, -35.4, -39.9; Horn 1 -29.0, -29.1, -28.3, -38.6. The brass fade under the tutti's cresc. molto.
- The local maximum at qn 975 (-19.8) is the cello's G2 again (stem -24.3 dBFS, finding 5).

**Fix (`build/score_config.py`):**
1. `SHARED_HP["Violins I"] = [(978.0, 984.5, "cresc")]` (the table is read like printed hairpins, `tools/score_to_parts.py` line 758). Expected CC11 in 980-984 about 100-112.
2. Horns 1-2 and Trumpets 1-2: cancel the taper on the tied note with `LEVEL_SHAPES` rows `[(978.5, 0.0), (983.3, 3.0), (983.6, 3.0), (983.85, 0.0)]` (back at 0 before the led note of 984).
3. The cello trim of finding 5 removes the bump at 975.

**Targets:** Violins I within 2 dB of Violins II in 980-984; master per quarter from 976 to 984 never more than 1 dB under the quarter before, about -21 at 976 rising to -19.5 at 983; step into 984 at most 2 dB.

### 4. The delivery gain rises during static soft music after two diminuendos (measured; new rows simulated)

**Where:** mp3 only. Bars 42-51 (qn 164-200) and bars 170-176 (qn 676-700). `build/score_config.py` `RIDE_TRIMS`, the rows starting at 163.95 and 679.0. This answers the open item "ride hold over bars 42-50": it is wanted.

**What is wrong:** delivery gain (mp3 minus master, K-weighted): bar 42 +6.5, 43 +6.8, 45 +8.7, 48 +10.4, 50 +11.7, 51 +12.2 dB. Under a held pp string pedal with printed "poco rit." and nothing growing, the mp3 goes from -34.1 (bar 43) to -26.7 (bar 48), +7.4 dB where the master moves +3.9. The pedal itself swells 5.7 dB in 13 s (audibility inferred: a held chord is the worst case for a moving fader). At the recapitulated second theme the gain goes +9.5 (bar 171) to +13.3 (bar 176): the muted trumpet theme's first two bars are the softest music of the mp3 (-34.3, -32.7) and bar 174 is 4.9 dB over bar 171 where the master rises 2.2.

**Fix:** let the gain rise during the printed diminuendos (bars 39-42, 167-170), where it only makes a fall shallower, and hold it through the static passage. Rows simulated on the c13 master (both old rows removed):
- `[(151.95, 0), (152, 0), (156, 1.0), (160, 2.0), (164, 2.6), (166, 3.2), (168, 3.2), (170, 3.1), (172, 2.8), (174, 2.6), (176, 2.1), (178, 1.8), (180, 1.6), (182, 1.5), (184, 1.1), (186, 1.1), (188, 1.0), (190, 0.7), (192, 0.5), (194, 0.3), (196, 0.1), (198, 0), (199.9, 0)]`
- `[(663.95, 0), (664, 0), (668, 1.1), (672, 2.3), (676, 3.4)]` followed by the `deliver_master.py --fit-flat 680 744` row with +1.2 dB on every value (680 4.56, 682 4.18, 684 3.82, 686 3.49, 688 3.17, 690 2.89, 692 2.63, 694 2.4, 696 2.19, 698 2.02, 700 1.88, ..., 743.9 4.06, 744 0).

**Simulated result:** gain 168-198 +10.4 to +10.7 dB, gain 680-698 +12.1 to +12.5; mp3 bars 43-50 -30.5, -28.2, -29.0, -27.5, -29.1, -26.6, -29.8, -31.6 (bar 43 -> 48 +3.9, as the master); bars 166-173 -17.4, -20.8, -21.5, -25.4, -29.0, -31.4, -30.8, -28.6 (monotonic into the pp, no swell after it). LRA 14.5 LU, span 18.9 dB, limiter 2.3 dB, inversions 2 -> 1.

**Order:** the master changes with finding 2, so refit after the c14 render: run `--fit-flat 168 200` and `--fit-flat 680 744` on the new master, keep the ramps from 152 and 664. **Targets:** gain within ±0.75 dB over 168-198 and over 680-740; mp3 bar 43 -> 48 within 1 dB of the master's change; delivered LRA 14-16, limiter under 3 dB.

### 5. The cellos' G2 and A flat 2 are 7-9 dB hot, which makes unprinted swells and puts the cello on top of the texture (measured)

**Where:** Violoncellos, held notes on pitch 43 (G2), 44 (A flat 2) and 42 (F sharp 2), on Sus MAX and Leg BC MAX, at CC11 70 or more. qn 58, 68, 96, 98, 604, 606, 618, 628, 656, 658, 880, 972, 1044 and the A flat notes.

**Evidence:** I regressed the K-weighted stem level (second half of each held note, volume envelope removed) on CC11 for 150 held cello notes. Median residual by pitch: 41 +1.8 dB (n 8), **42 +7.5 (n 2), 43 +8.6 (n 14), 44 +6.8 (n 7)**, 45 +0.3, 46 -0.1, 47 +1.8, 48 -1.3, 50 -1.0. On 13 of the 14 held G2 notes the cello is the loudest dry stem of the orchestra: bar 18 -28.1 against Violins I -31.1 (the first theme), bar 158 -24.8 against Violins I -27.1, bar 221 -24.8 against Violins II -27.1, bar 262 -20.5 against Horn 3 -22.5 and Trumpet 1 -23.3. Effects in this lens: the swell and fall at 880-884 (finding 1), the bump at qn 975 (finding 3), and a bass line that jumps 7-9 dB whenever it touches the dominant.

**Fix:** `build/pitch_trims.json`: `"Violoncellos": {"43": -5.0, "44": -4.0, "42": -4.0, "_all_arts_pitches": [42, 43, 44]}`. The trim for 42 rests on two notes (inferred). Check afterwards the basses-plus-celli sum on the G pedals of bars 147-150 and 199-204 against c13 (31.5-125 Hz share of the master within 1.5 dB), and give part of the trim back there with a role row if the low end thins.

**Target:** residual of pitches 42-44 within +4 dB; the cello no longer the loudest stem on the theme's G2 notes of bars 15-25 and 152-165.

### 6. Long wind and brass notes without a hairpin are static, and the four "dal niente" entries start at full level (measured; benefit inferred)

**Where:** brass and wind notes of 1.5 s or more with no printed hairpin, mainly the chorale (qn 892-936) and its return in doubled values (1016-1048); Clarinet 2 at 184, Clarinet 1 at 200, Clarinet 2 and Bass clarinet at 680.

**Evidence:**
- Stem level by thirds of each long note (attack and release excluded). Share moving less than 1 dB / less than 2 dB: brass in the driving sections 39 % / 70 % (n 129), brass in the lyrical sections 32 % / 56 % (n 50), winds 31 % / 51 % (n 95) and 40 % / 66 % (n 68), strings 14 % / 39 % and 7 % / 33 %. In the chorale 892-936: 42 % / 65 % of 78 brass notes. With a printed hairpin only 0-10 % are static, so the hairpins work.
- In the CC lanes, 52 % of long notes in the driving sections and 33 % in the lyrical sections stay within 2 CC. Research default (FINDINGS §11, §22): 0-13 % of long notes flat in 15 of 20 expert files; lyrical cue 6 %, driving cues 16-39 %; accented brass falls 15-25 CC over a long note. The phrase shape is scaled 0.35 at ff and 0.2 at fff (about ±4 CC) and the per-note `SWELL_DB` contour is dropped inside shaped phrases, so loud long notes get neither.
- "dal niente" (manual p.63: CC11 fades to silence): Clarinet 2 at 184 is at -48 dBFS 0.2 s after the note-on and stays within 0.5 dB for 5 s; Clarinet 1 at 200 -52 at +0.2 s; Bass clarinet at 680 -56 at +0.1 s. No fade-in.

**Fix (`build/score_config.py`), a narrow first step:**
1. Chorale, brass tracks, each whole note of 892-912 and 916-928 and each long note of 1016-1040: a lean-off in the volume envelope, `LEVEL_SHAPES_S` per onset `[(0.35, 0), (0.9, -0.7), (1.7, -2.0)]`, back to 0 before the next note-on. Stay at 2 dB: a deeper fall on every bar would read as an fp on each chord. If the tool can take it as a rule, name it `LONG_NOTE_LEAN = {"families": ("brass",), "min_s": 1.5, "fall_db": 2.0, "from_s": 0.35, "skip_hairpin": True, "spans": [(892, 936), (1016, 1048)]}`.
2. "dal niente": `LEVEL_SHAPES_S` on Clarinet 2 at 184.0, Clarinet 1 at 200.0, Clarinet 2 and Bass clarinet at 680.0: `[(-0.05, -18), (0.0, -18), (0.8, -6), (1.6, 0)]`.

**Targets:** chorale brass notes under 1 dB of movement: 42 % -> under 15 %; each dal niente entry at least 10 dB under its body in the first 0.2 s and within 1 dB of it by 1.6 s. Check items 4 and 7 on the chorale afterwards (no 2-5 kHz jump at note starts, no periodic movement in the master).

## Answers to the coordinator's questions (measured unless marked)

- **Wetness:** right, at the dry edge; no stop sounds cut off or gated (numbers under "State").
- **Bar 150:** release at 599.0 falls 19 dB in 0.35 s on the master in even steps, the basses and celli re-enter cleanly on the G at 600; no glitch. The recapitulation's first bars are 6-7 dB (K) under bar 150 because trumpets, trombones and the roll stop; that is the scoring.
- **Bar 75, level only:** Violins I B flat -34 dBFS, G -41, A flat -38, F -38. The G is 3 dB under the A flat; timing is critic A's.
- **Basses after the pizzicato reset:** pizzicato peaks 200-264 median -50.8 dBFS, sd 2.1; strongest 200 and 224 (-46), weakest 232 (-55.4). Arco 264-400: no held note more than 5 dB from its neighbours at one dynamic (qn 275, the +9.6 dB note, is now level with them at -45). None is audible as a fault (inferred).
- **Bassoon 1 solo:** mp3 bars 115-122 -29.8 to -33.4, clearly audible. Notes 464 (+3.0) and 468 (-2.8) follow the printed mp peak and decrescendo: leave them.
- **Timpani shapes at 223 and 278:** 223 settles (-26.4 to -32.8 dBFS over the bar); 278 rises 1.7 dB (see "State").
- **Horn 1 139-140, crash strokes, Violins II 152, low end 255-256:** nothing against them from this lens (Violins II at 152-154 -28.7 dBFS, level with Violins I -29.7).
- **Solo returns, Trumpet 1 joins, Flute 2 at 618 / 650, C #5 and C #6:** outside this lens, not measured this cycle.
- **Unprinted tempo changes** (render tempo map against the score's own MIDI tempo, beat length in percent): caesuras before qn 72, 104, 392, 632, 664, 816, 1108 (the last quarter of a quarter lengthened 56-96 %, 0.05-0.10 s); phrase arcs in the lyrical sections D-E, L-M, O, P, Q: stretches of up to +5.3 % over 2.5 bars, phrase-end beats +8.7 % (bars 58.5-59.25, 74.5-75.25, 178.5-179.25, 228.5-229), section cadences +13.6 % at most (bars 66.5-67.25, 186.5-187.25, 218.5-219, 242.5-244); pushes of -1.5 % over 841-848 and 889-900; the printed rit. / allargando / stringendo steps are smoothed into ramps (within -6.7..+5.7 % of the stepped values, mean 0). No unprinted change in the Allegro sections apart from the caesuras. All inside the research ranges; the bar-75 stretch (294-297, +8.7 %) ends before the new eighths.
- **Research defaults against the render:** phrase shapes in the lyrical spans start a median 22 CC under the peak, peak at 0.46 of the phrase, range 31 CC (research 30-60): met. In the driving sections the median range is 8 CC and the peak is at the phrase start: consistent with batch 7 item 1 at ff scale. Long notes: not met (finding 6). Curve shape of diminuendos: the Mulan rule fails on long hairpins with a short last note (finding 2).

**Do not touch:** the returns, sends and release fades (every stop decays evenly, none gated; do not dry further); `rise_delay_s` 0.6 and the delivery ratio (LRA 14.6, limiter 2.3 dB); the 592 sfp notch and fronts; the timpani roll shapes at 888 and every roll's settling; the crescendo rolls on CC1; `FINAL_RING` and the final chord; the climax order 223 / 278 / 263; the builds 832-840 and 1096-1108; the re-bow layout (no loop pulsing); the 200-264 and 451-504 ride rows and the final ride row; the phrase shapes of the lyrical sections; the short hairpins' curve (`decresc_last` on hairpins of 6 quarters or less with a last note of 0.35 s or more).
