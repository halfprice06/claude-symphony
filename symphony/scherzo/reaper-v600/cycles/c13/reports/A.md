# Critic A, cycle 13: articulation and phrasing (on the c12 render)

Data: `cycles/c12/render/` stems and `cycles/c12/build_render/parts.json` (byte-identical to `build/parts.json` today), printed lengths and marks from `build/mockup-events.tsv`, `sections/*.ily`. Positions are score quarter notes (qn); bar b starts at qn 3(b-1). An eighth lasts 114 ms at quarter 264, 131 ms at 228 and 104 ms at 288. No REAPER step, no file changed outside this report. The scratch folder is deleted as instructed, so the estimators are described here in full.

This cycle's priority was the timing of the thematic lines. I did not re-measure the items the c12 actor lists as open (timpani first strokes, Violins I re-bows 1116 / 1125, the summit roll, trumpet level, Flute 1 under the solo), the harp, or the pizzicato level edges.

## Manual notes (slot A7: May 2021 manual, PDF p.160-162 and 188-190, read in full; `loop/MANUAL-GAPS.md` read)

| Manual says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| p.160: each articulation cell of a KS Master has its own load switch; a row is in memory only while it is switched on | every KS Master track; `UNLOAD_UNUSED_ROWS`, `ROW_REMAP` | Yes. Read from the 1st Violins patch file: Violins I loads Sus MAX 11.8, Sus Marc LITE 8.5, Leg Slur MAX 27.3, Leg BC MAX 27.2, Staccatissimo 8.3, Stac RRx14 13.0, Spiccato 7.9 thousand regions. Leg BC MAX plays 32 notes for 27.2 thousand regions; "Slur Runs" costs 15.1 thousand (finding 1) |
| p.161, p.189: a keyswitch is a note outside the playing range; "play or program an articulation's Keyswitch Trigger to select it"; a row plays only while its keyswitch is the active one | every row change; at quarter 264 the pipeline's 0.03 qn keyswitch lead is 6.8 ms | Followed in order, with very little time. Keyswitch to the next note-on: median 6.8 ms on Violins I (120 of 182 keyswitches under 8 ms), Violins II 51 of 91, Violas 61 of 120, Violoncellos 115 of 146, Horn 3 17 of 26, Flute 1 36 of 86; minimum 4.5 ms. One 512-sample audio block is 10.7 ms. EastWest's own template puts keyswitches 40-800 ms ahead (`RESEARCH-FINDINGS.md` section 9). Finding 6 |
| p.162, p.190: a Velocity trigger can layer a short row over a sustain (the manual's example: a staccato restricted to velocities 110-127 over Violin Sustain) so that hard notes get a short accent | the 321 accents; the nine p / mp theme heads on Sus Marc LITE | Not used, and not needed. 2-5 kHz energy of the first 80 ms minus the note's body (100-250 ms), accented notes of 0.25 s or longer: Violins I median -1.8 dB (n 45; worst +4.7 at 771 and +4.6 at 51, both Sus Marc LITE), Violins II -1.5, Violas -1.2 (902: +5.3), Violoncellos -1.8 (902: +5.2), Flute 1 -0.9 (302: +5.0), Oboe 1 -3.9, Cor anglais -5.8, Clarinets -2.8 / -4.3. No accent is near the +7..+13 dB that Dan heard as harsh in Movement II. A velocity-layered staccato would add bite, against BRIEF item 9 |
| p.188: Voice Limit is per instrument; dropped voices mean the limit was reached | the "non div." double stops (bars 72, 105-120, 300, 305-320, 339) and the tutti | No dropped note found in the measured lines (2,815 notes). 58 have no separate attack by the estimator: same-pitch repeats that dip under 3 dB (finding 5), staccatos tied over from the note before, and two octave leaps the band method cannot read (Violoncellos 362, 830) |
| p.188-189: Group, Octave, Key Range | none used | Not applicable |
| p.96-97 (read for finding 1): "Slur Runs", 1st and 2nd Violins only, holds the fast notes, the slurs between them and the long notes of a run; CC11 sets the level, velocity does not; "a minimum speed is sixteenth notes at about 125 beats per minute" (120 ms per note) | the theme head's two slurred eighths (114 ms each) | Not used: they play on Leg Slur MAX (Violins I, soft statements) or Sus MAX. Finding 1 |
| p.99: "the first note of a phrase has no legato effect"; a legato transition needs the note before on the same patch with no gap | every legato-row note that follows a note on another row | The data gives these notes no lead although they start with the row's slow first-note attack. Finding 2 |

## Timing of the thematic lines: method and totals (measured)

Estimator S, as Movement II's c51 critic A defined it: for a note joined to a different pitch, the earlier of pcX (`tools/pcx.py attack_pcx`, previous pitch excluded) and the robust crossover of the two exclusion bands (the last moment the old band is 3 dB over the new one, then the first moment the new band reaches it; copied from `mvt2-c51-A/onsets.py`). For entries S is pcX. pcX fails on the second of two same-pitch staccato eighths: it finds the first eighth's attack and reads -110..-137 ms. For same-pitch repeats I used a wide-band envelope instead (1024-point FFT, 2 ms hop, bins from 0.8 f0 to 8 kHz; floor searched from the previous note's peak; same t50 / -10 dB definition as pcX). On synthetic bursts on a 113.6 ms grid with a 4 ms attack it reads -1 ms (range -4..-1). The same envelope gives the dip between the two notes of a pair (S1). All times are against the score beat on the parts.json tempo map.

2,815 notes on 16 tracks over the Allegro's thematic sections (bars 13-72, 89-140, 253-339):

| Class | n | Median | 5th..95th percentile | Over 25 ms | Over 60 ms |
|---|---|---|---|---|---|
| Strings, short rows (staccato, spiccato, pizzicato) | 871 | -3 | -33..+29 | 135 (16 %) | 9 (1 %) |
| Winds and brass, short rows | 610 | -7 | -26..+18 | 43 (7 %) | 4 (1 %) |
| Strings, legato joins that have a lead | 242 | 0 | -64..+78 | 111 (46 %) | 33 (14 %) |
| Winds and brass, legato joins that have a lead | 472 | +10 | -21..+65 | 132 (28 %) | 30 (6 %) |
| Strings, legato-row note after a note on another row, lead 0 | 17 | +102 | -11..+182 | 14 (82 %) | 10 (59 %) |
| Winds, the same | 45 | +55 | +30..+92 | 44 (98 %) | 14 (31 %) |
| Strings, legato-row phrase heads | 18 | +42 | -142..+118 | 16 | 10 |
| Strings, Sus / Marc notes joined to the note before (slurred shorts, strokes) | 170 | -22 | -52..+65 | 106 (62 %) | 16 (9 %) |
| Strings, Sus / Marc entries | 92 | +6 | -48..+75 | 37 | 15 |
| Winds and brass, Sus entries, Sus joins and legato heads | 278 | | -52..+78 | 117 | 18 |

Of the 2,757 notes with a reading, 755 (27 %) are more than 25 ms off and 159 (6 %) more than 60 ms.

What this says:
- The staccato theme is on the beat. Row medians: Oboe 1 -6 (robust SD 3), Clarinet 2 -9 (4), Cor anglais -6 (7), Flute 1 +9 (10), Flute 2 +15 (6), Horn 1 -15 (4), Trumpets -13 / -10 (9 / 7), Violins I Staccatissimo +1 (16), Stac RRx14 +9 (15), Spiccato -22 (9), Violins II Stac -3 (15), Spiccato -8 (10), Violas Stac -1 (16), Staccatissimo RRx16 -9 (15), Violoncellos Stac +7 (19). The staccato quarters are 114 ms and the eighths 57 ms long in every section (104 / 52 in the coda); the flutes' quarters before rests are 193 ms (c10). Leave these leads alone.
- What is off the beat is slurred: the two slurred eighths of the theme head (finding 1), legato-row notes with no lead (finding 2) and single fitted joins of the espressivo lines (finding 3). The second idea is the worst passage: at common onsets the instruments are 60-270 ms apart (bar 49 beat 1: 135 ms; qn 372: 225; qn 382: 211; qn 850: 270), with the winds inside +-50 ms and the strings between -98 and +186.
- Trio and coda lines (306 notes): Clarinet 1's tune bars 153-168 -28..+43 (median +16, none over 60: good); the cellos' tune bars 169-184 -141..+155 (7 of 31 over 60); Violins I bars 177-184 -64..+135; Violins I bars 209-224 -70..+97 (18 of 31 over 25); Violin I solo -48..+139; Horn 3 bars 341-348 -38..+100.
- No note of these lines is swallowed in the sense of making no sound. Eight of the nine second eighths of Violins I's soft theme heads sound for under 40 ms (finding 1).
- State guard question: the seven tracks that were stale on the post-render save show no stale signature in the audio. Legato joins with a lead, median S: Violins I +10 (n 103), Violas -6 (48), Violoncellos -6 (133), Bassoon 2 +8 (23), Contrabassoon +23 (5), Horn 2 +38 (18), Horn 4 +4 (19); a stale state would put them near -45. The c10 and c11 stems are deleted, so a stem comparison was not possible.
- Horn 1's staccato at 165: Horn 1 minus Horn 2 is +3.1 dB there by my measure (first 0.2 s, unweighted); on the 30 staccato quarters the two share it runs from -4.0 to +7.3 (median +1.8), and at 165 Horn 1 (-44.5 dB) is under ten other stems (Violins I -35.8, clarinets -42 / -43, bassoons -42 / -43). It does not stand out. No row needed.

Unprinted tempo changes: the tempo map has 22, all from `BEAT_STRETCH` in `build/score_config.py` (line 579); nothing else departs from the printed tempos and the three `RAMP_SPANS`. Each makes the third beat of one bar longer; together they add 0.53 s. See finding 4.

## Findings

### 1. The theme head's two slurred eighths are not played as two notes in any soft string statement (measured; the cure is inferred)

Where: the appoggiatura figure of theme A, accented half note slurred to two eighths and a staccato quarter (bar 14: G5 half, F sharp 5, F natural 5, E5). Violins I bars 14, 18, 24, 26, 96, 254, 258, 264, 266 (qn 41, 53, 71, 77, 287, 761, 773, 791, 797; `SHORT_SUS_LEG_AT`, Leg Slur MAX). Fugato entries: Violoncellos bars 58 and 290 (qn 173, 869), Violas 185, 881, Violins II 197 (Sus MAX).

Violins I, the nine soft statements. Sounding start of each eighth against its beat, and how long each is heard before the next note starts (printed 114 ms each):

| qn of the first eighth | first eighth S | second eighth S | staccato after S | first heard | second heard | second eighth's own-pitch peak under the staccato after it |
|---|---|---|---|---|---|---|
| 41 | +6 | +53 | -45 | 161 | 16 | 7 dB |
| 53 | -24 | +69 | -43 | 207 | 2 | 15 |
| 71 | -20 | +27 | -13 | 161 | 74 | 12 |
| 77 | -22 | +48 | -39 | 184 | 27 | 15.5 |
| 287 | -26 | +30 | -45 | 170 | 39 | 7 |
| 761 | +2 | +45 | -47 | 157 | 22 | 11 |
| 773 | -12 | +64 | -43 | 190 | 7 | 8 |
| 791 | +2 | +32 | -51 | 144 | 31 | 5 |
| 797 | -1 | +55 | -45 | 170 | 14 | 8 |

The second eighth is heard for 2-74 ms (median 22) and the first for 144-207. The listener hears G, F sharp, a blip, E. Cause (measured): the Leg Slur MAX transition takes 186-240 ms from note-on to the new pitch, longer than the 114 ms note. The first eighth gets a 210 ms lead; the second is capped at 148-165 ms (`LEG_CAP_FRAC` 0.75) and arrives 27-69 ms late; at 287.5, where the cap did not bite (lead 210), it is still +30 because the pair F sharp to F is slower than G to F sharp. The c08 render, which played these pairs on Sus MAX, was no better in time (second eighth heard -3..47 ms) and its eighths were 7-18 dB lower, so neither row can play the figure. The reading of the staccato after the pair (-13..-51) is less certain than the eighths: with that note exactly on its beat the second eighth would still last only 45-87 ms.

Lower strings, fugato (cellos alone at bar 57): on Sus MAX at p the first eighth's slot is nearly empty and the second is late. Violoncellos 173 / 173.5: slot level -60.0 / -51.4 dB against the half note's -48.2 and the next quarter's -45.5; second eighth S +101 ms. The same at 869 / 869.5 (-58.8 / -51.3 against -48.4; +102 ms). Violas 185.5 and 881.5 are -42 / -44 ms early and 11 / 10 dB under the staccato after them; Violins II 197 / 197.5 are -31 / +40.

In the two ff tuttis the violins' pair (Sus MAX, `SHORT_SUS_LEAD_S` 0.06) is even but early: first eighth -5..-42 (median -33), second -25..-48 (median -36), heard 81-130 and 124-169 ms.

Fix:
1. Violins I, the nine soft pairs on the "Slur Runs" row, which the manual describes for exactly this speed (p.96-97) and which Movement I c20 measured on slurred sixteenths of 119 ms (own-pitch share 0.52 to 0.68 and 0.36 to 0.83, onset +0.05..+0.06 s, at v127, 0.02 qn overlap, no lead; `mockup-kit/LEARNINGS.md` section 20). In `build/score_config.py`: `STACLEG_SPANS = {"Violins I": [(41.0, 42.0, "Slur Runs"), (53.0, 54.0, "Slur Runs"), (71.0, 72.0, "Slur Runs"), (77.0, 78.0, "Slur Runs"), (287.0, 288.0, "Slur Runs"), (761.0, 762.0, "Slur Runs"), (773.0, 774.0, "Slur Runs"), (791.0, 792.0, "Slur Runs"), (797.0, 798.0, "Slur Runs")]}` (Movement I's form; `LEG_ROWS_EXTRA` already names the row), and take these 18 onsets out of `SHORT_SUS_LEG_AT` and the eight `VEL_SET` rows at v88. The row ignores velocity for level (p.97), so the pair's level comes from CC11: check it against the half note. Seven of the nine pairs move by semitones, for which the row has recorded half-step samples; 71.5 and 791.5 fall a fourth and use the row's slur transition, so measure those two separately.
2. Memory for it: `ROW_REMAP["Violins I"] = {"Leg BC MAX": "Leg Slur MAX"}`, as Violins II, Violas and Violas div have had since c02. Leg BC MAX is 27,163 regions for 32 notes; Slur Runs is 15,125. Net about -12 thousand regions (about -0.5 GB at c02's 4 GB per 92 thousand). It also puts Violins I and Violins II, who double the second idea in octaves, on the same row there.
3. Test before the full render with a range render of bars 13-28 (Movement I c53's range-render rules), Slur Runs against the present data. Accept if both eighths are heard for 114 +-35 ms, the second eighth's S is within +-30 ms and its level within 4 dB of the first. If it fails, the fallback is the present row with both targets at velocity 124 (manual p.143-144: 110-127 gives the shortest transition; they are at 85-100 now) and the second eighth's note end moved to 0.02 qn before the staccato's note-on.
4. Violoncellos 173 / 869 (the half note before is already on Leg Slur MAX, so the first eighth can be a true legato target with the row's lead): add `SHORT_SUS_LEG_AT["Violoncellos"] = [173.0, 869.0]`, keep 173.5 / 869.5 on Sus MAX with 0.10 s more lead (`entry_leads.json` or a `REATTACK_LEAD_AT` row) and +4 dB (`note_trims.json`, `NOTE_TRIM_RAMP_S` 0.1). Accept if the first eighth's slot is within 6 dB of the half note's and the second eighth's S is within +-40 ms. The celli and violas have no runs row (p.96).
5. Tutti pairs: `SHORT_SUS_LEAD_S` 0.06 to 0.03 for Violins I and II (per-track if the tool allows; the violas' soft pairs need the 0.06). Predicted starts -5..+0 ms.

### 2. Sixty-two legato-row notes that follow a note on another row have no lead and sound 30-186 ms late; they include the downbeat of bar 49 in three string sections and the winds' first slurred eighth in every loud theme head (measured)

Cause: such a note is not an entry (no rest before it), so it gets no entry lead, and not a legato target (the note before is on a Sus or staccato row), so it gets no legato lead. It starts on the beat with the legato row's first-note attack (manual p.99: no legato effect on a phrase's first note).

Strings (17 notes, median +102 ms):
- Bar 49 beat 1 (qn 144), the accented start of the second idea's second phrase, f espress.: Violins I +143, Violins II +135, Violas +142, Violoncellos +48, against Flute 1 +8, Oboe 1 +24, Cor anglais +10, Clarinet 2 +35. Checked a second way: own-pitch band level in 50 ms steps from the beat, Violins I -13.6, +2.8, 14.2, 19.2, 22.4 dB (body 22); Flute 1 18.0, 17.9, 18.1. The strings reach their level 150 ms after the winds. The note before (the eighth pickup 143.5) is on Sus MAX.
- Violas 382 +181, 387 +120, 850 +186, 855 +143, 618 +145, 840 +61 (after same-pitch Sus MAX notes); Violoncellos 840 +164, 853 +102, 192 +144; Violins I 157.5 +92, 385.5 / 853.5 +45.

Winds (45 notes, median +55 ms): where the accented half note of the theme head is f or louder it plays on Sus MAX (`GENTLE_ACCENT`) and the first slurred eighth after it starts the legato row with lead 0. Flute 1 +30..+47 (125, 209, 317, 329, 347, 353, 821, 893, 947, 1001), Oboe 1 +32..+96 (the same and 917, 929, 953), Cor anglais +30..+78, Clarinet 2 +56..+62, Flute 2 +15..+85. On the same notes the violins are 14-42 ms early (finding 1), so in both tuttis the woodwinds change note 50-130 ms after the violins, and the first eighth is heard for at most 93 ms in the oboe (median 62) and 68 ms in the cor anglais (median 41). In the soft counterstatement (89, 101, 113) the half note is on the legato row and Oboe 1 reads -14..-16: that is the comparison.

Fix: give these notes the lead of a legato-row phrase head. `ABUT_LEAD` exists for the abutting case (`{"lead_s", "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": False, "at": [...]}`, with `force_at` if the skip tests block a row); where one track needs different values use `entry_leads.json`. Values (0.85 of the measured lateness; `LEG_HEAD_MIN_GAP_S` keeps the winds' 32 ms gap):
- Violins I: 144.0 0.12, 157.5 0.08, 385.5 and 853.5 0.04. Violins II: 144.0 0.115.
- Violas: 144.0 0.12, 382.0 0.15, 387.0 0.10, 618.0 0.12, 840.0 0.05, 850.0 0.155, 855.0 0.12.
- Violoncellos: 192.0 0.12, 840.0 0.14, 853.0 0.085, 144.0 0.04.
- Winds, one value per track at the first slurred eighth of each loud head: Flute 1 0.035, Oboe 1 0.055, Cor anglais 0.05, Clarinet 2 0.055, Flute 2 0.05, at the onsets listed above for each track (125, 209, 317, 329, 347, 353, 821, 893, 917, 929, 947, 953, 1001 where the track plays the figure).
Better as a generic rule in `tools/score_to_parts.py` (off by default), because the same class will appear in any score: a legato-row note whose predecessor ends within 30 ms of it on a non-legato row takes `LEG_HEAD_AFTER_ROW_LEAD_S = {"string": 0.12, "wind": 0.05}`, per-onset rows on top. Movement I's c54 coordinator notes report the same class there as the worst (string legato after Sus-row notes, SD 82 ms).
Accept if every listed note reads within +-40 ms and, at 144, the four string sections are within 60 ms of each other and of Flute 1.

### 3. Thirty-four fitted string joins are still 60-180 ms off, most of them in the cellos' tunes; Flute 2 trails Flute 1 in the second tutti (measured)

Strings, legato joins that have a lead: 401 measured, 34 fail by both estimators (late: S and both parts over +40; early: S under -60 and the other under -25). The other 367 stay as they are: per-onset rows work on the strings (Movement II c51).

Proposed `build/leg_leads.json` values (seconds; existing row plus 0.9 S, change limited to 0.1 per pass; "new" = no row now):
- Violoncellos, trio tune bars 171-177 (leads of 227-350 ms, the notes arrive up to a third of a beat early): 511.5 S -141, row 0.001 to -0.099; 518 S -114, 0.083 to -0.017; 523.5 S -108, -0.053 to -0.150; 528 S -119, 0.034 to -0.066. Also early: 345 and 945 S -69 / -68, -0.05 to -0.11; 844 S -70, 0.094 to 0.031. Late: 171 +87 new 0.078; 180 +72 new 0.065; 207 +99 new 0.089; 350 +60 new 0.054; 855 +104 new 0.094; 867 +85 new 0.076; 880 +82 new 0.074; 891 +141 new 0.10.
- Violins II: 134 +77 new 0.07; 159 +76, 0.078 to 0.146; 374 +98, 0.11 to 0.199; 387 +88, 0.088 to 0.167; 819 +125 new 0.10; 840 +66 new 0.06; 855 +88 new 0.079; 646 +64, -0.086 to -0.028; 594 -64 new -0.058; 848 -98 new -0.088.
- Violas: 150 S -91, 0.052 to -0.030; 831 +97 new 0.087. Violins I: 146 +66 new 0.059; 536 S -64, 0.025 to -0.032.
- Three joins come after a slurred eighth and are held by the cap, so a row alone will not move them: Violins II 372 (+180 with a 74 ms lead), Violin I solo 1052 (+87) and 1061.5 (+107) with 99 ms leads although their rows ask for +0.134 / +0.15. Lift the cap there: `LEG_CAP_FRAC["Violin I solo"]` add `(1051.9, 1052.1, 1.0)` and `(1061.4, 1061.6, 1.0)`; `LEG_CAP_FROM_MOVED["Violins II"]` leaves 372 out (or a `LEG_CAP_FRAC` row `(371.9, 372.1, 1.0)`), then rows 372 0.13, 1052 0.08 and 1061.5 0.10 more.
- Flute 1 at 1061 / 1061.5 (with the solo): -78 and +161. 1061 has a 120 ms lead against 30 ms on its neighbours; find the rule that gives it (there is no Flute 1 row in `leg_leads.json`), return it to 30 ms and measure 1061.5 again.

Flute 2, bars 305-320 (qn 912-960), running slurred eighths in unison or octaves with Flute 1: 10 of 43 joins are 65-114 ms late (918.5 +65, 919.5 +92, 920 +114, 922.5 +93, 931.5 +97, 940 +85, 943.5 +100, 944.5 +92, 947.5 +88, 954.5 +65), all with the same 51 ms lead; 941 reads -125, probably the estimator on an A-B-A figure. Flute 2's joins there have a median of +30 ms against Flute 1's +6 on the same notes. Movement II c51 found wind transition time fixed per pitch pair, so do not add per-onset rows: raise Flute 2's legato lead by 0.03 s (`LEG_ART_EXTRA_S["Flute 2"] = {"Leg Slur MAX": 0.03}`, the form Violins II uses), and give the pairs that stay over +60 a `LEG_PAIR_EXTRA_S` entry after the next render.

Late readings that are not on the actor's open list: entries Violins I 528 +135 (the trio tune's dolce entry, lead 120) and Violins I 624 +97 (the ff return); wind and horn joins Horn 3 1022 +100 and 1025 +78 (trio recall), Bassoon 1 134 +221, 146 +107, 327 / 927 +95. The entries rest on pcX alone, which reads slow swells late, so check each by level (time to body minus 6 dB) before adding to `entry_leads.json`; the wind joins belong in a pitch-pair table, not in per-onset rows.

Accept: no join of the cellos' trio tune outside +-60 ms and at most a third outside +-25; Flute 2 minus Flute 1 within 40 ms on 9 of 10 shared onsets in bars 305-320.

### 4. Twenty-two beats are stretched by 6-18 % without a printed mark (measured; how audible, inferred)

All are `BEAT_STRETCH` rows (c07, "tempo breaths"): the third beat of a bar before a phrase joint.

| qn | bar | factor | that beat | onsets inside the beat |
|---|---|---|---|---|
| 35 | 12 | 0.92 | 247 ms (227) | none |
| 167 | 56 | 0.94 | 242 | none (the horn link is gone) |
| 359 | 120 | 0.88 | 258, +13.6 % | Horn 1, Violas on the beat |
| 827 | 276 | 0.90 | 253, +11.1 % | Cor anglais, Violins I, Violins II, Violas on the beat |
| 863, 971 | 288, 324 | 0.94 | 242 | none; Violoncellos at 971 |
| 479, 503, 527, 551, 575, 587, 599, 611, 647, 695 | 160-232 | 0.92 | 286 ms (263), +8.7 % | Violins II's con sord. eighths at 503, 527, 551 (143 ms each instead of 131), Clarinet 1's eighths at 587, six tracks at 647 |
| 671 | 224 | 0.85 | 310, +17.6 % | Violas, Violas div |
| 1031, 1043, 1055, 1079 | 344-360 | 0.92 | 286 | harp at 1031 / 1043; Flute 1, Violins II and the solo at 1055 |
| 1067 | 356 | 0.85 | 310 | none |

Nothing else in the map is unprinted. These are far smaller than Movement II's (20-42 %), but each is a single beat 6-18 % long followed by a return to tempo, and in the trio it recurs every four or eight bars under running eighths. Movement I and Movement II both removed their unprinted changes after Dan's note. Fix: in `build/score_config.py` drop the scherzo's additions (the assignment at lines 579-582, or `BEAT_STRETCH = {}` after it) (keep the `RAMP_SPANS` and `RAMP_LAST_STEP_HOLD_QN`). If the orchestrator wants to keep a breath, keep only the three with no onset inside or after them at a section joint (35, 167, 1067). The map shifts by up to 0.53 s after qn 35, so run `fit_rebows.py` / the re-bow checks as after any tempo change.

### 5. Same-pitch staccato pairs that do not separate on the stem: trumpets, cellos, Violins II in the coda (measured; cure inferred)

Dip between the two eighths of a same-pitch pair on the stem (wide-band envelope, previous peak or new peak, whichever is lower, minus the trough; S1 asks for 3-6 dB):

| Track, row | pairs | median | under 3 dB | worst |
|---|---|---|---|---|
| Trumpet 1, StacSs DblTng | 10 | 3.4 | 5 | 337.5: 0.3, 301.5: 1.0, 325.5: 1.0 |
| Trumpet 2, StacSs DblTng | 10 | 2.6 | 7 | 313.5: 1.8, 355.5: 2.2 |
| Violoncellos, Stac RRx9 | 20 | 3.6 | 9 | 967.5: 0.1, 91.5: 0.8, 997.5: 0.9, 979.5: 1.0, 973.5: 1.2 |
| Violins II, Stac RRx9 | 18 | 5.1 | 5 | 991.5: -0.3, 994.5: 0.6, 985.5: 0.8, 121.5: 1.3 |
| Violins I, Staccatissimo | 35 | 5.5 | 5 | 91.5 and 811.5: -0.2, 127.5 / 823.5: 1.8 |
| Violas, Stac RRx9 | 9 | 4.7 | 3 | 976.5: 0.0, 121.5: 0.1 |
| Oboe 1, Flute 1, Flute 2, Clarinet 2, Cor anglais (Stac DblTng) | 88 | 5.5-9.2 | 3 | Flute 1 115.5: -0.9, 997.5: 0.8 |

The woodwind row separates well. The trumpets' pairs in both tuttis and the low strings' pairs in the coda (eighth 104 ms) mostly do not. A negative value means the second eighth is weaker than the first one's decay: Violins I 91.5 and 811.5, Flute 1 115.5, Violins II 991.5.

Fix: shorter staccatos in the passages where the pairs fail, with the tool c08 added for this (it acts on every printed staccato in the span). `STAC_LEN_SPANS` 3-tuples (the fraction is of the staccato's MIDI length, which is already half the written value, so 0.7 gives 40 ms eighths and 80 ms quarters at quarter 264; the 0.35 on Oboe 2 and Clarinet 1 gives 18 ms eighths): `"Trumpet 1"` and `"Trumpet 2"`: `[(300.0, 360.0, 0.7), (900.0, 960.0, 0.7), (984.0, 1008.0, 0.7)]`; `"Violoncellos"`: `[(972.0, 1008.0, 0.7)]`; `"Violins II"`: `[(984.0, 996.0, 0.7)]`. For the four notes whose second eighth is weak, +3 dB on that note alone (`note_trims.json` with `NOTE_TRIM_RAMP_S` 0.1: Violins I 91.5, 811.5; Flute 1 115.5; Violins II 991.5). Whether the trumpet and string short rows end at the note-off like the woodwind row is not known (inferred from c08's Oboe 2 / Clarinet 1 result and c10's flute lengthening), so range-render bars 105-108 first. Accept: trumpet pair dips median 4 dB or more with none under 2, cellos' coda pairs none under 2, and the quarter notes' level within 1 dB of c12.

### 6. Keyswitches sit 4.5-7.9 ms before the note they switch, less than one audio block (read in the data; effect inferred)

Where: every track with row changes; 600 of 1,263 keyswitches are under 8 ms before the next note-on (table in the manual notes). The manual sets no minimum (p.161), and the order is correct in the data. But EastWest's own template never does this (40-800 ms ahead), and the two notes the c12 actor found changed between renders on identical data both follow a keyswitch closely: Horn 1 at 642 (keyswitch 641.628, note-on 641.658: 6.8 ms; 13-23 dB apart between c11 and c12) and Violins II at 852 (keyswitch 851.94, note 852.0: 13.6 ms; 6.8 dB apart). That is two cases, not proof.

Fix (cheap, generic): in `tools/score_to_parts.py` place a keyswitch at least 0.04 s before its note wherever the track's previous note-on is earlier than that point (a held note keeps its row, so the keyswitch may fall inside it; c12's own data already does this at legato-to-staccato changes), and keep the 0.03 qn only where the previous note-on is closer. Then compare the horn stems and Violins II 852 with c12 as the actor did with c11. Accept: no note-level differences over 3 dB on unchanged data at notes that follow a row change.

## Do not touch

The staccato leads and lengths of every short row (row medians -22..+15 ms, 16 % of string and 7 % of wind short notes outside 25 ms; quarters 114 ms, eighths 57 ms, the same in every section); the woodwind "Stac DblTng RRx9" pairs (dips 5.5-9.2 dB); Clarinet 1's trio tune and Clarinet 1 / 2's legato lead (bars 153-168: -28..+43, none over 60); the 367 string legato rows not listed in finding 3, including c12's 45 refits; the accent swells and the Sus Marc LITE heads (2-5 kHz fronts at most +5 dB over the body); Horn 1's staccato at 165 as it is; the printed tempo ramps (`RAMP_SPANS`), the bar-2 fermata, the G.P. and the last bar; `LEG_HEAD_MIN_GAP_S` 0.032; the counterstatement's soft wind heads on the legato row (Oboe 1 89 / 101 / 113 within -16 ms).
