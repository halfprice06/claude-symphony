# Cycle 7, critic A: articulation and phrasing (render c06)

All measurements are on `cycles/c06/render/` (dry stems 01-31, return stems 91-94, `00_Master.wav` = dry + returns, checked: residual -172 dB) with the rendered data in `cycles/c06/build_render/parts.json`. Times come from that tempo map (identical to c05's). "Stem" means a dry stem; "master" means the full sum, or a re-sum of the dry stems with the return stems at trial gains. Scripts: `/private/tmp/claude-501/mockup-loop/scherzo-c07-A/` (deleted at the end).

## Manual notes (cycle 7 slot A: group A3, May 2021 HO manual PDF pp. 75-81, Hollywood Solo Violin; plus MANUAL-GAPS.md)

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| The Solo Violin links dynamics and vibrato on CC1. The HO sections control them separately (p.75). | Violin I solo (1st Violins KS Master DIV A), bars 349-356, qn 1044-1068 | No. The solo's CC1 is held at 72 with no points in 1040-1070, so the vibrato stays the same while CC11 rises 42 -> 64 and falls back. Measured from parts.json. |
| "Long Solo" legato script: overlapping notes blend, and notes that do not overlap re-attack (pp.75-76) | the solo's 18 joins | Yes. Every join overlaps 11 ms. The stem dips at the joins are 0.4-4.4 dB (measured). |
| Leg Slur: velocity sets how tight or loose the transition timing is. The patch "shines at slow to medium tempos" (p.80) | the solo, quarter 228 | Partly. v124 on 1046-1054 (the CC11 > 40 rule), v90 from 1055, in a passage printed "dolce, pp". Pitch crossovers: +0.00..+0.07 s at v124, +0.02..+0.11 s at v90; the two eighths after dotted quarters (1052, 1061.5) cross at +0.16 / +0.17 s (measured). |
| Leg Bow Change: an expressive bow change that accents the second note (p.79) | the slur starts 1049, 1053, 1056, 1065 | Yes. Leg BC MAX sits exactly on the printed slur starts. |
| Leg Runs: legato for runs up to a minor third, "most realistic at fast tempos" (p.80) | the theme's two slurred eighths after the accented half note (finding 2) | Not available. The section KS Masters' nearest row is "Slur Runs" (MANUAL-GAPS #16, 15-21 thousand regions, not loaded). |
| Solo short rows (Marcato, Martelé, Spiccato RRx4) and LegSus (CC1's initial value picks the layer) (pp.78-81) | none: Solo Violin is not installed (MANUAL-GAPS #5) | n/a |

## Findings, ranked by what a listener would hear

### 1. The template returns make the fast articulation mushier than c05; take them down 3-5 dB (measured)

Where: the whole movement, most in the soft staccato statements (theme A bars 13-28, qn 36-84; counterstatement 29-44, qn 84-132; reprise 253-268, qn 756-804) and the trio (153-168, qn 456-504).

Evidence. I re-summed the dry stems with the four return stems at trial gains and measured three things. "Contrast" is the median, over every eighth-note slot in a passage, of the maximum minus the minimum of the 10 ms master envelope. It shows how far the level falls between short notes. "t20" is the time the master takes to fall 20 dB after the last note-off before the bar-340 G.P. "T60" is the late slope from -20 to -40 dB.

| master | G.P. drop at +0.3 s | t20 | T60 | contrast: theme A | counterstatement | reprise | trio |
|---|---|---|---|---|---|---|---|
| c05 (Opus hall, fx 0.095, IR envelope 0.7) | 22.2 dB | 0.25 s | 1.68 s | 6.4 | 4.8 | 5.6 | 3.8 |
| c06 as rendered (returns at template level) | 13.4 | 0.58 | 2.71 | 5.7 | 3.6 | 4.6 | 3.4 |
| all returns -3 dB | 15.0 | 0.51 | 2.48 | 6.1 | 3.7 | 4.8 | 3.7 |
| R Strings / R Winds -5, R Brass / R Perc -3 | 16.1 | 0.40 | 2.41 | 6.1 | 3.7 | 4.8 | 3.7 |
| all returns -6 dB | 17.0 | 0.39 | 2.43 | 6.3 | 3.7 | 4.8 | 3.7 |
| dry stems only | 25.7 | 0.23 | 0.73 | 6.5 | 4.1 | 5.0 | 4.0 |

The c06 returns carry -3.2 dB of the dry stems' energy (R Strings -5.7, R Winds -8.3, R Perc -14.0, R Brass -17.0). At the template level the tail takes 0.58 s to fall 20 dB, which is the slowest end of the references (Brahms 1/i 0.43-0.55 s, Dvořák 0.50-0.58 s; Movement I c45 called 0.45-0.55 s "right"). The late slope is 2.7 s against the brief's 1.5-2 s. Between the soft staccato notes the level now falls 0.4-1.2 dB less than in c05.

Two points limit what a fader can do. First, the late slope stays at 2.4 s whatever the return level: the full 3.3-3.4 s IRs set it, and only a shorter IR or a darker tail changes it. Second, the dry stems by themselves now separate notes less than c05's complete wet master did (counterstatement 4.1 against 4.8, reprise 5.0 against 5.6). Part of the loss is therefore in the dry sound (the full-width Main mics carry the recording room), not in the returns. The repeated-note pair dip barely responds to the return level (V1 soft pairs median 3.6 -> 3.4 dB from 0 to -6). Do not use it as the wetness gauge.

Fix (`build/mix.json` `returns.<name>.fader_db`, or through `tools/make_template_mix.py` so the value survives a regeneration): R Strings 1.03 -> -3.97 dB (-5), R Winds 1.03 -> -3.97 (-5), R Brass 1.03 -> -1.97 (-3), R Perc 0.66 -> -2.34 (-3). This lands the G.P. at 16.1 dB at +0.3 s (S4: 13 or more; recordings 13-17) with t20 0.40 s. Simulated on these stems; the fader is post-Spaces, so the simulation is exact. If Dan still hears mush, go to -6 dB on all four before touching sends. Then run ONE_TIME_c07 items 1-2 (register sends -16 dB on low brass, bassoons, contrabassoon and basses; a 1.8-2.3 kHz low-pass on the returns). Those two shorten and darken the tail, which no fader does. After either change, re-measure t20 so it does not fall below about 0.40 s. Small extra: the basses' short row "Staccato RRx9" (26 notes) is missing from their `send_row_db` (only "Pizz RRx4" is listed). Add it with -5.4 dB, as the celli's Stac row has.

### 2. The theme's two slurred eighths after the accented half note barely sound in the strings (measured; unchanged since c00)

Where: Violins I at every head tail (half note with accent and \dnb, slurred to two eighths, slur ending on a staccato quarter): sq 39, 51, 69, 75 (theme A), 285, 759, 771, 789, 795 (reprise), and the tutti / counterstatement tails 111, 123, 207, 315, 327, 345, 351, 819, 891, 915, 927, 945, 951, 999. Also Violins II (123, 195, 315 ...) and violas (123, 183, 819, 879 ...).

What is wrong. Both eighths go down the "short_sus" path: Sus MAX notes at the score onset (qn 41.000, no lead), velocity 53-63 at p/mp. The half note before them is on Sus Marc LITE (or a Sus MAX down-bow stroke in the tuttis) and ends exactly at the first eighth's onset, with the strings' 350 ms p/pp release cap. A soft Sus MAX attack takes about 0.3 s to speak (kit LEARNINGS 6), while each eighth lasts 0.114 s, so the half note's release covers both eighths.

Evidence. "Own-pitch dominance" is the energy at the eighth's harmonics 1-3 against the louder neighbour pitch, within the eighth's own slot. Violins I stem, soft statements (39, 51, 69, 75, 759, 771, 789, 795): first eighth -13 to -27 dB, second -8 to +3 dB; the two eighths sit 7-15 dB under the half note's body. Tuttis (v100): first eighth -6 to -9 dB. Violins II and violas: first eighth -2.7 to -18 dB. The winds play the same figure on Leg Slur MAX: Flute 1 and Oboe 1 own-pitch +5 to +16 dB on most tails. On the master, where Violins I carries the theme alone over pizzicato, the first eighth reads -10 to -19 dB in every render from c00 to c06 (c00 -6/-19/-17/-14 ... c06 -10/-12/-19/-13 at 39/51/69/75). In theme A and the reprise these eighths are melody notes (G, F sharp, F), and the melody loses one of them every two bars.

Fix (`build/score_config.py`, existing knobs, all strings at once):
- (a) `SHORT_SUS_LEAD_TRACKS = ("Violins I", "Violins II", "Violas")` with `SHORT_SUS_LEAD_S = 0.06` and `SHORT_SUS_LEAD_KEEP_OVERLAP = 0.02`, so each eighth starts early and the half note stops at the moved onset.
- (b) `VEL_SET` 90-100 for the first eighth of each listed tail. The tutti v100 first eighths measured -6..-9 dB own-pitch, against -13..-27 dB at v53; check the level against the half note.
- (c) Violins I `sus_release_cap_ms`: a 120 ms entry for "Sus Marc LITE" at all dynamics. Its 20 notes are exactly these heads and the hemiola strokes, all followed by moving notes.

Pass: on the stem, both eighths' own-pitch dominance at -3 dB or better, and the eighths within 6 dB of the half-note body. As an A/B inside the same render, put two tails (69 and 789) wholly on Leg Slur MAX: half note as the first note, accent by the GENTLE_ACCENT swell, eighths as legato targets through `SHORT_SUS_LEG_TRACKS = ("Violins I",)` and `SHORT_SUS_LEG_S = (0.10, 0.25)`. The winds show that a legato row speaks these eighths; whether the HS legato does at 0.114 s is untested (kit LEARNINGS 5 found 0.16 s sextuplets smeared).

### 3. Repeated eighths in the tutti statements: three parts still merge the pair (S1, measured)

Where: bars 105-120 and 305-320 (qn 312-360, 912-960) and the coda build 329-336.

Evidence (stem dip at the second eighth: the maximum of its first 80 ms minus the minimum from -60 to +30 ms):
- Violins I on "Stac RRx14" (the `_TUTTI_STAC` span): 313.5 7.9, 319.5 9.1, **325.5 0.9**, **331.5 2.4**, 340.5 4.4, 349.5 7.4, **355.5 2.4**; 913.5 7.1, 919.5 9.5, **925.5 0.9**, **931.5 2.6**, 940.5 3.9, 949.5 8.0, **955.5 2.8 dB**. This is the failure c06 A #1 fixed in the soft statements: RRx14 1.5-4.0 dB, Staccatissimo RRx9 5.7-7.3 dB.
- Violins II on "Spiccato RRx9": **313.5 1.1, 319.5 1.1, 913.5 2.5, 919.5 1.2 dB**; the other pairs 4.9-7.1.
- Trumpet 2 plays all 56 printed staccatos as cut "Sus Non Vib MAX" slices of uneven length (0.164 / 0.090 / 0.057 / 0.131 s for one head, against Trumpet 1's 0.114 / 0.057 / 0.057 / 0.114). Its second eighths dip 1.5-3.7 dB (median 2.1; coda 1.3-2.3). Trumpet 1 on "StacSs DblTng RRx9" dips 2.9-8.5 (median 5.6). The two trumpets articulate the same head differently in every tutti.
- Master, Violins I tutti pairs: median 3.8 dB, 10th percentile 2.0.

Fix (`build/score_config.py`):
- (a) Split `_TUTTI_STAC` for Violins I so the pairs at 325-326, 331-332, 355-356, 925-926, 931-932 and 955-956 play "Staccatissimo RRx9", the same form as the c06 `_RR14_OLD` split. Leave the pairs that already dip 7-9.5 dB on RRx14.
- (b) Violins II: pairs 313-314, 319-320, 913-914 and 919-920 on the loaded "Stac RRx9" (an `ART_SPANS` entry ahead of the Spiccato replacement, with its `ROW_TRIM_DB` -4).
- (c) Trumpet 2: the same `ART_SPANS` entry Trumpet 1 has ("StacSs DblTng RRx9", `vel_by_cc=_TSTAC`, the pp -6 dB step of bars 101-103). It costs 4,080 regions, about 0.18 GB at c02's rate. To stay at 45 GB, take an equal count off a row that plays few notes (`rowcost.py`).

Measure the pair dips against these numbers. When ONE_TIME item 1 (repeat gaps) lands, apply its gap to the first note of each pair, not to the slot.

### 4. The dolce solo (bars 349-356) is played with the fastest legato and a fixed vibrato (manual pp.75, 80; partly measured, partly inferred)

Where: Violin I solo track, qn 1044-1068, "dolce, solo (gli altri tacet)", pp with hairpins, quarter 228.

Evidence. Legato velocity is 124 on 1046-1054 and 90 from 1055 (measured). It switches by the CC11 > 40 rule in the middle of one dolce phrase, so the transition speed changes halfway through it. The manual says velocity tightens the Leg Slur transitions (p.80). v124 is the most clipped transition, which suits a tutti line rather than a pp solo (inferred). CC1 is fixed at 72: the vibrato does not follow the phrase, while on the instrument this part imitates, CC1 moves dynamics and vibrato together (p.75). The joins themselves are clean (dips 0.4-4.4 dB). The two eighths after the dotted quarters cross 0.16 / 0.17 s late (1052, 1061.5).

Fix (`build/score_config.py`):
- `LEG_VEL_SPANS` (or `VEL_SET`) for "Violin I solo" over 1043.5-1068: 82 throughout. Raise `LEG_LEAD_S["Violin I solo"]` 0.12 -> 0.15 to keep the crossovers where they are now (v90 measured 0.02-0.04 s later than v124). Add a pair extra of +0.05 s at 1052 and 1061.5.
- When ONE_TIME item 4 draws CC1, give this track a CC1 lane that follows its CC11 hairpins: about 60 at the pp start, 85-90 at the peak of 1049-1050, back to 60-65 by 1067.
- When ONE_TIME item 2 sets the legato overlap, use 45-60 ms here (the solo moves in quarters at 0.26 s, so the template value fits).

Then re-measure the join dips and crossovers.

### 5. Horn 1's tenuto line in the trio climax still has holes on Port Lng at 651 and 654 (measured)

Where: Horn 1, bars 217-219, sq 651 and 654 (and 636 / 639), "Port Lng" span 647.5-664.

Evidence (stem; dip and time spent more than 3 dB under the note bodies): 630 2.5 dB / 0 ms, 633 2.5 / 0, 636 6.7 / 210, 639 5.9 / 160, **651 11.2 / 320**, **654 12.5 / 180**, 657 6.0 / 110, 663 2.3 / 0. The 16.1 dB dip at 648 is the printed breath and is right. c05's Sus MAX re-tongue (0.035 s, 4 CC, lead 0.09 s) measured 639 3.5 and 651 4.8 dB.

Fix (`build/score_config.py`, the c06 Horn 1 `ART_SPANS` block): split the second span so that 650.5-656 returns to Sus MAX with the c05 re-tongue values (the span's REATTACK_LEAD_AT entries removed there). Do the same for 635.5-641.5. Keep Port Lng on 626.5-635.5 and 656-664, where it brought the dips to 2.3-6.9 dB.

## Checked and found working (measured)

- No chord goes to a monophonic legato row on any track.
- No same-pitch overlap on any track.
- Pizz./arco changes: every arco entry after pizzicato reaches its body (-6 dB) within -0.09..+0.12 s.
- The harp's trio chords are simultaneous (non arpegg.). The arpeggios at 708 and 1080 are spread 0.15 qn per note from the bass.
- The "étouffez" at 575.5 damps the harp: -45 -> -60 dB in 0.1 s, silent by 0.2 s.
- Violins II CC15: on at 393.8 before the 501.5 entry, off at 552.3 ("via sord.", bar 185).
- Accents are weight, not bite: the 2-5 kHz front (0-80 ms) minus the body (80-300 ms) has a median of -2.1 to -7.7 dB on every string and woodwind track, maximum +5.0 dB (Flute 2 1014), against the kit's -1..-9 dB target.
- The breath marks give 4-9 dB dips at f (Bassoon 2 at 528, 1.3 dB, is the only soft one).

## Scheduled c07 items: how to tune them for this tempo

- Legato overlap (ONE_TIME item 2): every legato join now overlaps 9-11 ms on every track. At quarter 264 the template's 45-80 ms is 40-70 % of an eighth. Use min(60 ms, 0.35 x the previous note's length) on strings and min(45 ms, 0.3 x) on winds and brass, so fast slurred eighths keep their pitch.
- Short-note velocity by beat position (batch 6/7): c02 measured that the woodwind "Stac DblTng RRx9" rows barely change level with velocity, so that rule will do little on the winds. On the string Stac rows velocity selects the layer. Never lower the second note of a repeated pair by more than about 5 steps against the first, or finding 3's dips shrink; put the 15-25 step contrast between beat 1 and beats 2-3.

Do not touch: the c06 split of the soft-statement repeated pairs onto Staccatissimo RRx9; the Marc LITE heads with their level steps (finding 2 changes only the eighths and the head's release); the wind Stac DblTng rows and Trumpet 1's StacSs row; the solo's Leg BC MAX choice at slur starts; the pizz./arco handling and the harp étouffez; the accent handling (GENTLE_ACCENT swells, Marc LITE fronts under the body); the return chain itself (Spaces II, ReaEQ, post-fader sends). Change only the return faders, per finding 1.
