# Cycle 29, critic A: articulation and phrasing (on the c28 render)

Material:
- the `cycles/c28/render` stems and `cycles/c28/build_render/parts.json`, `mix.json` and `roles.json` (the data as rendered);
- `cycles/c28/records/`;
- `cycles/c18/render` with its parts.json as the felt-timpani comparison. c18 is 3 dB hotter (global gain), so I compare within one render or in relative terms.

Tools:
- The actor's scripts, run read-only: `cycles/c28/actor_scripts/ten28.py` (timp, ten), `fig28w.py` logic.
- My own scripts:
  - per-note stem levels;
  - a downbeat-over-beats-2-3 measure on stem groups;
  - the woodwind figure measure with a second harmonic set;
  - a copy of build_reaper's `vol_points` / `cc7_lane`, cut before ENV_LUA and exec'd with my own jobs folder, to split the Oboe 1 lanes into their sources.

"Measured" means a number from the render or from the data. "Inferred" means reasoned from those numbers or from the manual.

## Manual notes

`MANUAL-READING.md` has no row for c29. Two of this cycle's A items were the hard-stick timpani and the tenuto downbeats, so I read these two groups of the May 2021 HO manual in full. I also used `MANUAL-GAPS.md` (#6, #6 c11/c12/c28, #10, the memory plan):
- B3, PDF pages 122-126: the Drums/Timpani folder, felt and hard.
- D2, PDF pages 100-102: brass Long and Short folders.

| page | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| 122-124 | Felt timpani: "the felt coating on the mallets makes each note quite soft"; Felt KS rows C0 long/double, C#0 short, D0 flam, D#0 rolls (CC1, 8 levels), E0 recorded crescendos | the score's "soft sticks" spans (bars 146-224, qn 435-672, and 341-376, qn 1020-1128) and "medium sticks" (225-288, qn 672-864) | **no**: every stroke and roll plays Timpani Hrd KS (finding 1) |
| 124-126 | Hard timpani: "a brighter timbre overall than in the case of felt mallets"; Hard Short gives a damped stroke, "more pronounced than with felt mallets"; same five rows and keys | the Allegro, bars 1-145 and 289-340 ("hard sticks" at bar 1 and bar 289) | yes since c28: the 1-5 kHz share of the first 50 ms is -16.7 (0-435) and -15.2 dB (864-1020) |
| 123, 125-126 | Long hits: two strokes within 65 ms play a damped double hit; LH zone C1-A2, RH zone C3-A4 | motive x's same-pitch strokes (`TIMP_RH_ALT`, +24) | yes: every same-pitch repeat alternates hands (47/71, 40/64, 52/76), and no two strokes fall within 65 ms except the bar 339 E pair, which is intended (Sht, damped) |
| 124, 126 | Rolls: CC1 crossfades 8 dynamic levels; Cresc rolls are "the most realism" | rolls 300, 384, 612, 708, 852, 906, 993, 1005 | rolls on "Rls" with CC1; each roll ends on a stroke (309, 390, 624, 858, 909, 996, 1008), or in a rest before the next entry (708 -> 720). Cresc rows unused (MANUAL-GAPS #7) |
| 100 | Brass "Sustain Accent": "The MIDI Velocity parameter controls the loudness of the attack", CC1 the sustain | the tutti tenuto downbeats in trombones, bass trombone, tuba, Horns 1-2 (bars 105-120) | not used; the tenutos play Sus MAX, whose attack swells (finding 2) |
| 100 | "Sustain Marcato": "not as forceful an attack as in the Sustain Accent"; velocity sets a low-pass on the marcato attack (low velocity = darker front) | the same notes ("Marc Sus LITE" is in 1TB / 1TU / 1FH / Basses KS Masters) | not used (finding 2) |
| 100 | Portato: "holds each note its full length — or close to it — but without tying it to the next note" | c28's portato range test | c28 rejected Portato (later, softer). The definition also supports a tenuto that stops just short of beat 2 (finding 2) |
| 101 | Short notes have no release trails | the trumpets' StacSs quarters in 312-360 | not a fault: they are 0.35 qn with the hall after them |

## First check: Dan's figure at every occurrence

### Strings

Source: `records/fig25.txt` (c27 -> c28).
- Violins I: every rising step at bar 23 and bar 263 is unchanged or better (bar 23 79->81 4.4 -> 5.6).
- Bars 110 / 310, step 79->78: 2.8 / 2.5 -> 3.7 / 4.3.
- Bars 115 / 315, first step 78->79: 22.2 / 22.6 -> 13.3 / 13.5. This is the F sharp back on its c18 row. At 13 dB margin it is still a clean crossover: the eighth's band is 13 dB under its peak when the next pitch takes over. I propose nothing.
- Violins II: within 0.7 dB.

Measured.

### Woodwinds

The c28 "worst" values, and Flute 2 at 948, are an artefact of the measure. Every woodwind crossover is clean (finding 3).

## Findings, ranked by what a listener hears

### 1. The timpani play hard sticks through 50 strokes and 3 rolls that the score gives to soft or medium sticks, not just the "six coda strokes". In the trio the pp strokes are now about as bright as the f strokes of the Allegro (measured; fix inferred, using pipeline features Movement I has run)

Where: the Timpani track (stem 22). The stick texts are in `build/mockup-events.tsv`:

| qn | text |
|---|---|
| 0 | "hard sticks" |
| 435 | "soft sticks" (bar 146) |
| 672 | "G sharp muta in G medium sticks" (bar 225) |
| 864 | "hard sticks" (bar 289) |
| 1020 | "soft sticks" (bar 341) |

The notes on the wrong sticks:
- Soft sticks, trio:
  - pp strokes at 444, 450, 456, 501, 549 (Sht) and 561;
  - f Sht 597;
  - the pp < f roll 612-624 and the f stroke 624;
  - p 669.
- Medium sticks:
  - the pp roll 708-718;
  - the 22 motive-x strokes 720-753 (pp < p) and 778-803;
  - the f roll 852-858 and its stroke 858.
- Soft sticks, coda: the 13 strokes of 1086-1122, among them the ppp "near the rim" strokes of 1110-1112.

CHANGES c28 and score_config's c28 comment count only the six coda strokes; the c11 MANUAL-GAPS entry had found all the texts.

Evidence: c18 (felt) against c28 (hard), from `ten28.py timp`. The 1-5 kHz share is that band's share of the first 50 ms of each stroke; c18 levels are +3 dB global.

| span (sticks) | strokes | c18 felt: peak / 1-5 kHz share | c28 hard: peak / 1-5 kHz share |
|---|---|---|---|
| 0-435 (hard) | 77 | -31.0 / -19.3 | -35.1 / **-16.7** |
| 435-672 (soft) | 9 | -52.1 / -35.4 | -53.6 / **-21.2** |
| 672-864 (medium) | 28 | -46.5 / -27.8 | -48.5 / **-18.4** |
| 864-1020 (hard) | 47 | -27.6 / -17.6 | -30.5 / **-15.2** |
| 1020-1128 (soft) | 13 | -50.4 / -29.0 | -53.9 / **-19.4** |

- The trio's pp strokes (444-561, v56) read -19.2..-21.4 dB on hard sticks against -35.3..-40.1 on felt: 14-19 dB more stick in the attack.
- In c28 the trio's pp strokes are only 2.5-4.5 dB darker than its own f strokes at 597 / 624 (-18.7 / -16.7), and 4.5 dB darker than the Allegro's f strokes. In c18 the contrast was 16 dB.
- The ppp "near the rim" strokes (1110-1112: -18.5..-19.7) are no darker than the pp strokes before them (1086-1100: -16.0..-21.1).
- c28's own learning (LEARNINGS 528) is that the hard layers add +9..+20 dB of 1-5 kHz at soft velocities and only +1..+3 at loud ones. So the swap was right for the Allegro's f / ff strokes and wrong for every soft-stick passage.
- A listener hears the musette trio's drum as a tick under the clarinet's dolce tune, and the coda's last ppp strokes as hard taps (inferred from the band shares).

Fix: the pipeline already has what this needs: the second render pass, `ALIAS_TRACKS` / `PASS2_TRACKS` / `build_reaper.py --pass2` / `render_cycle.py --pass2` (Movement I c39-c46). MANUAL-GAPS "Memory plan" names "a second timpani patch" as a pass-2 candidate, so the 45 GB cap does not apply.
- `build/score_config.py`, c29 block:
  - `ALIAS_TRACKS = {"Timpani soft": {"source": "Timpani", "windows": [(435.0, 864.0), (1020.0, 1128.0)], "patch": ".../Drums/Timpani/Timpani Flt KS.oib", "no_pitch_trims": True}}`
  - `PASS2_TRACKS = ("Timpani soft",)`
  - `TRACK_WINDOWS["Timpani"] = ([(435.0, 864.0), (1020.0, 1128.0)], False)`
  - The source's felt-measured tables carry over unchanged: `TIMP_CC1_MAP`, `TIMP_ROLL_TRIM_DB`, `TIMP_RH_ALT` with its `lh_vel_add`, `TIMP_STAC_ROW = "Timpani Flt Sht"`. They were fitted on felt (MANUAL-GAPS #6), so the alias needs no `drop`. `KS_ALIASES` maps felt names to hard rows only when the patch lacks them, so check in parts.json that the alias's ks lanes name the Flt rows.
- `build/mix.json`: a "Timpani soft" track entry copied from c27's Timpani entry (gain -5.3, seat -0.05, the same eq / side_shelf / mic_db) without c28's hard-stick `region_gain_db`. The Timpani entry keeps its region gains.
- Medium sticks (672-864): the score asks for something in between. Run the range test with that window on felt and on hard. Keep the one whose 1-5 kHz share lands nearer -24 dB (half-way between -28 felt and -18 hard), at a peak within 1.5 dB of c28.
- Check before rendering:
  - Diff the alias against its source's notes and lanes inside the windows. This is mockup-kit LEARNINGS' alias trap. Movement I's `pipeline/alias_check.py` does it; read it and do not import it.
  - The windows start and end in rests: 435 is a full-bar rest before 444; 864 and 1020 follow rolls that end at 858 and the G.P.

Acceptance (pass-2 stem against the c28 stem):
- 1-5 kHz share of the soft spans -30 dB or lower (c18: -35 / -29);
- the soft and medium strokes' peaks within 1.5 dB of c28;
- rolls 612 / 708 / 852 within 1 dB of c28;
- the Allegro (0-435, 864-1020) bit-identical apart from round robins;
- G.P. drop and hall checks unchanged.

### 2. The tutti's tenuto downbeats swell to a peak 130-183 ms into a 227 ms beat and ring into beat 2. The group that carries the downbeat weight is only 2.4 dB louder on the downbeat than on beats 2-3 (measured), and the manual's two attack-by-velocity rows have not been tried (fix inferred; c26's measured Marc LITE result supports one part)

Where:
- Bars 105-120 (qn 312-360): every downbeat in trombones 1-2, bass trombone, tuba, Horns 1-2, contrabassoon and basses (16 printed tenutos each; Horn 1 also has staccato eighths).
- Bars 305-320 (912-960): contrabassoon, basses, Horns 1-2.

Evidence (c28 stems):
- Shape (`ten28.py ten`, median over the 16 downbeats; peak time / -6 dB point / 2-5 kHz front minus body):

| track | peak | -6 dB point | 2-5 kHz front - body |
|---|---|---|---|
| trombone 1 | +170 ms | +25 ms | -4.5 |
| trombone 2 | +183 ms | +30 ms | -1.0 |
| bass trombone | +130 ms | 0 ms | -1.6 |
| tuba | +165 ms | +30 ms | -6.0 |
| Horn 1 | +148 ms | -25 ms | -7.0 |
| basses | +155 / +145 ms | -15 / -20 ms | -1.8 |
| contrabassoon | +130 / +100 ms | -45 ms | -2.0 |

  Each note starts in time but reaches its peak two-thirds of the way through the beat. Peak minus body (60-200 ms) is only 1.3-2.8 dB, so the note is a swell, not a stressed start.
- Length (parts.json): the brass tenutos start 50 ms early with dur 1.22 qn, so the written end is exactly beat 2 (312 -> 313.0). The basses' and contrabassoon's dur 1.264 does the same. The KS release (trombone 237 ms, tuba 372 ms, horn 562 ms; DIGEST) then sounds into beat 2. The manual's portato definition is "its full length — or close to it" (p.100).
- Downbeat 10 ms peak minus beats 2-3, on stem sums of c28 over 312-360:

| sum | downbeat over beats 2-3 |
|---|---|
| master | -0.2 dB |
| all stems | -0.2 |
| without the trumpets | -0.4 (so the trumpets' quarters are not the cause) |
| without the tenuto group | -0.7 |
| the tenuto group alone | **+2.4** |
| trumpets alone | +1.7 |
| Violins I + II | -0.5 |

  The group that plays only on the downbeat measures only +2.4 dB over the two beats on which it is silent: its swell and release fill beat 2.
- c28's range test (LEARNINGS 527) showed "Marc Lng" and "Portato" are no faster, and that removing the Sus MAX lead costs 35-90 ms. So keep the leads.
- c26 (LEARNINGS 505): HS "Sus Marc LITE" on a fresh chord stroke (v92, lead 0.085 s) moved the strings' peak from +0.41..+0.52 s to +0.08..+0.13 s. Every tenuto here is a fresh stroke after a rest of almost two beats, the case c26 found to work, unlike the accented notes inside running lines that c22 rejected.

Fix: one range test on 312-360 / 912-960, three variants against a same-start control.
- a) Length. `build/score_config.py` c29 block:
  - `for q in range(312, 360, 3)`: `NOTE_END_AT[t][float(q)] = q + 0.85` for Trombone 1, Trombone 2, Bass trombone, Tuba, Horn 1, Horn 2, Contrabassoon, Double basses;
  - the same for `range(912, 960, 3)` on Contrabassoon, Double basses, Horn 1, Horn 2.
  - Only notes whose next onset is 2 qn or more away qualify. The sounding note then ends about 34 ms before beat 2 and the release falls in the rest: still full value at this tempo.
- b) Attack row, brass:
  - 1TB / 1TU "Sus Accent MAX" (manual p.100: velocity = attack loudness) at v50 and v70 (two sub-variants), with CC1 unchanged (89) and the 50 ms lead kept;
  - `ART_SPANS[t]` = `{"from": 311.9, "to": 360.0, "art": "Sus Accent MAX", "mark": "tenuto"}` with the c28 `"mark": "tenuto"` filter;
  - Horn 1 / Horn 2 the same on 1FH "Sus Accent MAX" (their staccato eighths stay on StacSs).
  - Alternative row in the same pass if memory allows: "Marc Sus LITE" at v40 (dark marcato front).
- c) Basses: Basses KS Master "Marc Sus LITE" on the tenuto downbeats, at v62 (with a `row_dyn_db` "vel<66" cut like Violins I's) and at v80, lead 0.085 s (c26's setting).
- Acceptance:
  - per track, peak +90 ms or earlier and the -6 dB point within ±30 ms of the beat;
  - 2-5 kHz front minus body 0 dB or lower (weight, not bite: Dan's rule and BRIEF item 9; trombone 2 is at -1.0 now, so watch it);
  - tenuto group downbeat over beats 2-3 at +5 dB or more;
  - master over 312-360 at +1.0 or more (now -0.2), and the mp3 too;
  - level of each track over the bar within 1 dB of c28 (no balance change).
- Adopt a) alone if b) / c) add bite.

### 3. The woodwind figure measure under-reads every upward leap to E6. With the fundamental in the band, all 54 woodwind crossovers in the tutti are clean, Flute 2 at 948 included (measured)

Where: `fig28w.py` (critic A c26's measure), Flute 1 / Flute 2 / Oboe 1 / Clarinet 2, 300-1000.

Evidence:
- The low values in `records/fig28w.txt` are all leaps of a fourth or more up to E6 (pitch 88), the head's top note:

| track | c28 low values (qn: value) |
|---|---|
| Flute 1 | 933: -3.9, 948: -0.8, 348: -0.6, 924: +0.5, 912: +3.0 |
| Flute 2 | 312: -3.2, 912: -1.9, 948: +2.2 |

  Every step of one or two semitones reads +9..+26.
- The measure uses harmonics 2-5 of each pitch:
  - For E6 that band starts at 2.6 kHz, above a flute's strong partials. The old note (F sharp 5 or B5) keeps its strong 2nd-3rd partials in its band.
  - At a fourth or fifth the two bands also share a partial: E6 x3 = B5 x4 = 3.95 kHz; E6 x2 = A5 x3 = 2.64 kHz.
  - The value then depends on the round robin. Flute 1 912 went 9.5 -> 3.0 and Flute 2 948 11.7 -> 2.2 between c27 and c28 with no data change.
- The same crossover with harmonics 1-3 (no shared partial for these pairs; my script, same windows, value at +70 ms):

| c28 | median | under +3 | worst |
|---|---|---|---|
| Flute 1 (15) | +19.9 | 0 | +11.7 (792) |
| Flute 2 (12) | +17.6 | 0 | +9.7 (312) |
| Oboe 1 (14) | +20.4 | 0 | +10.7 (822) |
| Clarinet 2 (13) | +17.3 | 0 | +3.1 (954) |

  - Flute 2 948: +26.9.
  - c18 on the same measure: medians +4.0 / +11.2 / +7.8 / +6.3, with 12 crossovers under +3 (Flute 1 924 / 933 -3.8 / -3.2, Oboe 1 944 -6.1). The c26 woodwind work fixed them.
  - On harmonics 1-3 the old note's band has fallen 12-23 dB by +70 ms at every Flute 1 leap. It is not ringing over the staccato.

Fix (records only, no data change):
- Add the harmonics 1-3 column to `fig28w.py` for pairs 5 semitones or more apart. The change is a harmonic-set argument in place of the fixed `for h in (2, 3, 4, 5)` in `band()`; my scratch copy that did this has been deleted.
- Gate the woodwind figure on it, so the "nothing more than 2 dB worse than c28" rule does not chase round robins.
- Mark the woodwind figure as solved in the open-faults list.

### 4. Oboe 1's "4.6 dB step" at 387 / 855 is mix.json's own CC7 passage level. The trim hold has nothing to do with it, and the stem does not fall there: it rises 5.4 dB (measured; no change proposed)

Where: Oboe 1, bars 129-131 (qn 384-392) and 285-287 (852-860). Score: f at 384 under one slur from 384 to 391, cresc 387-390, decresc 390-391, in unison or octaves with Flute 1 and Violins I / II (same hairpins).

Evidence:
- Lane split (my copy of `vol_points` / `cc7_lane`):
  - The dynamic trim read on moved time is smooth across 387: 3.50 dB at 384-387.05, then 3.64, 3.78 ...
  - No crescendo hold applies: the 372-384 and 840-852 hairpins are in `cresc_trim_hold.skip`.
  - The step is mix.json `tracks["Oboe 1"].cc7_spans_db` `[386.76, 392.89, -4.5, 0, 0]` / `[854.76, 860.89, -4.5, 0, 0]`. That is c25 critic B #4b ("the role fall ... as CC7, so the printed crescendo rises from it"), turned into steps at the moved note-on in c26.
  - The envelope stays at 9.3 dB; CC7 goes 66 -> 39 at 386.76.
- Stem, per note (c28, 60 ms after each note-on to 20 ms before the next):

| note | level |
|---|---|
| 384 B5 | -45.4 |
| 385 C sharp 6 | -39.0 |
| 385.5 B5 | -43.3 |
| 386 A5 | -42.2 |
| **387 G5** | **-36.8** |
| 389 F sharp 5 | -37.9 |
| 391 E5 | -41.5 |

  c18 (no span): 386 -40.3 -> 387 -32.1, a +8.2 dB jump.
- The oboe's G5-E5 on Leg Slur MAX at CC11 88-99 plays 5-9 dB over the B5-A5 before it. The span takes 4.5 dB off that jump, and what remains (+5.4 dB) falls where the crescendo starts.
- Stem against the partners, 384-387 -> 387-388:
  - oboe -41.9 -> -38.3;
  - Flute 1 -37.4 -> -38.4;
  - Violins I -37.1 -> -40.2.
- Without the span the oboe would jump about 10 dB at a slurred note change and stand about 6 dB over the flute.

Recommendation:
- Leave both span rows.
- Take Oboe 1 384 / 852 off the sag list and the "faults still audible" list. `sags28.py` reads lanes, not the stem.
- If the step must go, the instrument-side replacement is a region gain on the hot notes, not a removal. Oboe 1 `region_gain_db` `{"rows": ["Leg Slur MAX"], "pitch_db": {"79": -4.5, "78": -3.0}}` would replace the span; measure the G5 at 136 (-38.4, beside the F sharp 5 at 138 at -38.4) first, because it would fall with it.

## Not ranked

- The ppp "near the rim" strokes (1110-1112, v62 / v52) differ from the pp strokes (1086-1100, v64 / v56) by 2-5 velocity and 2.5 dB of peak. They land in the same Lng layers (60-64; 45-54 against 55-59). Finding 1's felt alias carries them; once on felt, try v52 / v44 there for ppp (inferred).
- Theme-head short rows, read from parts.json: Violins I play a different mix of short rows in each statement:
  - 36-84: Staccatissimo 20 / Stac RRx14 10;
  - 312-360: Stac RRx14 30 / Spiccato 6;
  - reprise 756-804: Spiccato 24 / Staccatissimo 14.
  
  The written lengths are equal everywhere (eighth 0.25 qn, quarter 0.50 qn, Più mosso 0.17 / 0.35 on Violins II and celli). The ring test of these rows (c26 / c28 A) is still not run. Not re-measured.
- Not re-measured (no data change since earlier A reports): pizzicato / arco changes, harp, con sordino, sul A, re-bows, the solo violin, the trio's legato joins (c28 pcx: celli +29 ms).

Do not touch:
- Hard sticks in 0-435 and 864-1020, with c28's per-layer region gains (Allegro 1-5 kHz -16.7 / -15.2 dB, levels matched to felt within 1 dB).
- `TIMP_RH_ALT` and the rolls' stroke ends.
- `STAC_ROW_BY_PITCH_REP_ONLY` on Violins I (110 / 310 step 3.7 / 4.3; 342 F sharp 3.2 dB under the 345 C).
- The c26 woodwind figure state (every crossover +3 dB or more on harmonics 1-3).
- The soft heads' eighths at v62 (2-5 kHz front -0.1 dB).
- The Sus MAX leads on the tutti tenutos (c28: removing them costs 35-90 ms).
- Oboe 1's two cc7_spans_db rows (finding 4).
