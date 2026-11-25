# c56 critic C: dynamics over time (render under review: c55)

Lens: hairpin and phrase shapes, the loudness arc against the score, loudness range of master and mp3 (BRIEF 6), swells and loop pulsing on long notes (BRIEF 7), decays, comparison with recordings. Coordinator additions: the per-note volume envelope (Dan, 2026-11-11), a count of crescendos that do not rise on their own stem, winds against strings in crescendos into f.

Method. c55 master, 42 dry stems, 4 return stems and the delivered mp3; `cycles/c55/rendered_build/parts.json` and `mix.json` (the data as rendered). The envelope is rebuilt as `build_reaper.vol_points` writes it (parts.json `vol_db` + `vol_post` on the 0.125 qn grid and `vol_bp`, plus the `dyn_trim_db` / `soft_trim_db` table read from `dyn_curve`), without the tail hold and SUBITO_TAIL. Stem levels are stereo power on 10 ms frames. "Without the envelope" is stem dB minus envelope dB: the track fader sits after Opus and before the hall sends, so this is exact, except on Violoncellos 159 / 526 and Cor anglais 24, which carry a stem fix. Loudness is ffmpeg ebur128. Scripts and their outputs are in `cycles/c56/critic_scripts/C/` (`env56.py`, `within56.py`, `sim56.py`, `simT56.py`, `hp56.py`, `arc56.py`, `long56.py`, `unmarked56.py`, `layers56.py`, `stops56.py`; the loop scan is `cycles/c50/actor_scripts/loopscan50.py` run on c55). Nobody heard anything: every judgement below is marked measured, simulated or inferred.

## Manual notes (pages chosen for the envelope question)

| PDF page | What it says | Where it applies | Does the render follow it? |
|---|---|---|---|
| p.53 (2.5.7) | Shape lines as a player does. Velocity for short notes (it cannot change mid-note); CCs for sustained notes, mid-note or over a phrase. | Every within-note level change | No. 74 % of the fader's travel is inside single notes, and 443 of the 1280 notes of an eighth or less carry 3 dB or more of fader movement (finding 1). The manual's tool for a short note is one value per note. |
| p.64 (3.2.5), p.151 | Volume (CC7 / fader) sets a track's level relative to the others and its ceiling. Expression (CC11) shapes "the continually changing dynamics", swells inside a note and over a phrase. | The split between `vol_db` and the CC11 / CC1 lanes | Partly. Printed hairpins are in CC11 (crescendos gain a median 2.5-3.1 dB per 10 CC on the stem; the fader adds 0.5-1.3 and the trim takes 0.2-1.3). The accent, bloom, fill and fitted-level layers are all in the fader. |
| p.64 | On the strings' LITE rows CC11 is loudness only and CC1 carries dynamics and vibrato together. | Sus Marc LITE: 146 Violins I notes (the theme), 51 Violins II, 21 violas, 25 celli | Yes. CC1 follows the printed curve on those notes (Violins I r = 0.93, 66-99 for curve 72-114; celli r = 0.98). |
| p.91-92 | Marcato Sustain adds a marcato sample at the start "for extra power"; Sustain loops. | The theme's long notes; re-bows | The front-heavy sample is why c55 needed a body lift on the Marc row: without the envelope the theme's long notes read front minus tail +3.5 dB (median, bars 15-22), with it -0.3. That within-note movement cures a measured fault and stays (finding 1). |
| p.101 | Brass Sustain: CC1 crossfades four dynamic layers; crescendo and diminuendo inside a note belong to CC1. | Horn and trombone long notes | Not where the fader does it instead: 29 of 254 long unmarked brass notes have a fader front 3 dB or more over the body (finding 2). |

MANUAL-GAPS in this lens: #12 (Felt Cresc rolls) still untried and not needed. #9 (horn portato rows) still open; not re-measured.

## EW-TEMPLATE-PLAN / FINDINGS sections in this lens

- Section 5 (and FINDINGS line 91): in EastWest's own template MIDI the dynamics lane is flat across legato note changes (change 0 at the median within ±200 ms, IQR -3..+1: "no per-note bumps and no dip before an onset"). Not applied: this mockup's fader moves 3 dB or more inside 2353 of 5282 notes.
- Section 8 (expert mixes): I read the track volume envelopes of the reference REAPER projects in `mockup-kit/reference/` (measured). EastWest's HO and ComposerCloud+ templates: no track volume envelope on any of 59 / 86 tracks. Duc's Mahler Adagietto: 12 envelopes, 0.01-0.26 points per second (40-120 points per string track over 8 minutes). Duc's LOTR: 16 envelopes, at most 0.36 points per second. Movement I c55: Violins I 2250 points, Violins II 2815, Violas 2925, Violoncellos 4206, Double basses 4060 over 432 s, that is 5.2-9.7 points per second in parts.json before the 0.125 qn grid. The expert projects ride the fader at phrase rate; this mockup moves it 20-100 times as often.
- Sections 7, 8, 10 (phrase arch) and 9 (hairpin curve): applied in c51-c52; shares at 34 / 50 / 72 % not re-measured this cycle.
- Section 2 (delivery): met, see "Arc and delivery".

## Answers to the coordinator

- **Slow against within-note envelope movement (measured).** Over all pitched tracks the envelope travels 26,900 dB inside notes and 9,400 dB between successive note means: 74 % is inside single notes (strings 78 %, winds 67 %, brass 71 %, timpani 77 %). The level SD between note means is still larger (2.2-5.3 dB per track) than inside notes (0.8-2.1 dB): the slow part sets the balance, the within-note part is small in level and large in activity. The dynamic-trim table is not the source: it alone moves 3 dB or more inside only about 220 notes.
- **Does the within-note part follow a printed marking (measured)?** 2353 notes swing 3 dB or more (950 of them 6 dB or more). 442 lie under a printed hairpin and move its way; 435 lie under a hairpin and do not move its way (flat within 0.5 dB or opposite); 425 carry an accent, tenuto, staccato, sf or a dynamic change; 1051 (45 %) carry no marking at all.
- **Crescendos that do not rise on their own stem: 20 of 252 (8 %), against the scherzo's 40 of 215 (measured; finding 3).** The trim table is the cause in 3. 11 start at ff or louder, where the sample has no headroom. Diminuendos that do not fall: 8 of 123, 4 of them only on the arrival note.
- **Winds against strings in crescendos into f (measured): no general loss.** 12 tutti crescendos end at f or louder with two or more wind and string parts. Winds minus strings, first quarter of the hairpin to the arrival: bars 9-12 -3.5 dB, 98 -2.7, 156-158 -2.0, 159-160 -1.8, 23-26 -1.8, 121-122 -1.7; 37-40 +3.0, 95-97 +4.0, 135-138 +1.3, 139-140 +0.9, 169-170 +7.3, 99 -1.1. Where the trim falls 4 dB or more (52 crescendos) the stems still rise a median 9.9 dB; only Horn 4 248-252 (-0.9) and Horn 3 536-548 (+3.0) rise under 3 dB. `CRESC_TRIM_HOLD` is not needed as a general rule here.

## Findings, ranked by what a listener (and Dan's eye on the envelope) would notice

### 1. Three quarters of the fader's movement is inside single notes, almost half of it on notes with no marking, and on short notes it buys nothing (measured; the fix is simulated on the c55 stems)

**Where.** Every pitched track; densest on the strings. Notes of an eighth or less with 3 dB or more of movement inside: Double basses 122 of 148, Violas 115 of 308, Violoncellos 38 of 197, Violins I 36 of 120, Timpani 27 of 29, Trombone 1 18 of 19, Horns a2 19 of 21. Rehearsal A, Violins I: the eighths at 58.5 / 59 / 59.5 run -7.6 → -10.1, -5.2 → -8.4, -6.9 → -5.4 dB; the tenuto quarter at 60 holds -3.5 for 0.1 s, drops to -9.7 and returns to -5.2; the eighth at 61 goes -7.9 → -3.1.

**What the movement does to the sound (measured, stem with against without the envelope).**
- Note-to-note level step between abutting notes outside hairpins (body level, first 0.35 s), with / without: strings 2.27 / 2.17 dB median (759 pairs), winds 2.67 / 2.59 (674), brass 2.06 / 1.99 (119). Steps over 6 dB: strings 69 / 81, winds 90 / 111, brass 9 / 7. The whole per-note machinery removes about one large step in seven and leaves the typical step unchanged.
- By track it helps the Double basses (1.8 / 3.2), Flute 1 (2.9 / 3.5) and Trombone 1 (1.5 / 2.0), and hurts Violins I (2.6 / 1.7), Cor anglais (2.5 / 1.5) and Horns a2 (2.2 / 1.6).
- Theme, Violins I 56-90: step 1.8 dB median / 4.6 at the 90th percentile with the envelope, 0.9 / 2.3 with none. The only thing the envelope buys there is the long notes' shape: front minus tail -0.3 dB with, +3.5 without (the c55 body lift).
- Level range inside notes of 0.35 s or more with 3 dB or more of fader movement and no hairpin: on strings the fader lowers the range in 172 notes and raises it in 70 (it flattens the sample: re-bow fills, body lifts). On winds it lowers 61 and raises 119; on brass it lowers 33 and raises 86 (finding 2).

**Simulation on the c55 stems (level only; `sim56.py`, `simT56.py`).**

| Variant | Notes with 3 dB or more of fader movement inside (Vn I / Vn II / Vla / Vc / Cb) | Step median, whole movement (same order) | Theme Violins I 56-90: step median / p90, front minus tail |
|---|---|---|---|
| A as rendered | 170 / 174 / 267 / 242 / 234 | 1.9 / 2.2 / 1.9 / 2.4 / 3.1 | 1.8 / 4.6, -0.3 |
| B one level per note on notes of 0.5 qn or less | 137 / 161 / 155 / 206 / 122 | 2.0 / 2.1 / 1.9 / 2.4 / 3.0 | 2.2 / 5.3, -0.3 |
| C = B and ±3 dB cap inside longer notes outside hairpins | 137 / 163 / 154 / 205 / 122 | 2.0 / 2.1 / 1.9 / 2.5 / 3.2 | 2.2 / 5.4, +0.2 |
| D one level per note on every note outside a hairpin | 73 / 84 / 76 / 120 / 60 | 2.0 / 2.1 / 1.9 / 2.5 / 3.5 | 2.2 / 5.8, +2.7 |
| T (theme spans only) short notes at one common level for the span, long notes keep their envelope | 14 of 41 in 56-90 (A: 25) | — | 1.8 / 4.0, -0.3 |

Variant T on the other one-row spans: Violins I 536-576 1.3 / 4.0 → 1.4 / 3.5; Violins II 104-128 2.6 → 2.3; Violas 104-128 2.1 → 1.4; Violoncellos 520-536 2.6 / 5.1 → 1.9 / 3.8 (the span that fails S). It fails on Violins I 104-128 (2.4 → 3.8), where the printed level changes inside the span; use B there.

**Fix.**
1. `tools/build_reaper.py` `vol_points`, a new pass before the tail hold: `NOTE_FLAT = {"short_qn": 0.5, "ramp_s": 0.015}` (None = off). For every note of `short_qn` or less, set all envelope points from its moved note-on to the next moved note-on (or its end, if a rest of 0.25 s or more follows) to the time mean of the envelope over the note, drop the `vol_bp` points inside it, and write one point `ramp_s` before the note-on. Skip notes at or after qn 724 (final fade) and timpani roll pieces. Simulated effect: variant B.
2. `build/score_config.py`, the STEADY_LINE spans Violins I 56-104 and 536-576, Violins II 104-128 and 552-576, Violas 104-128, Violoncellos 520-536: drop the `steady_levels54.json` rows and PICKUP_LIFT rows on notes of 0.5 qn or less (keep the `steady_body55.json` body and tail rows and the level rows on notes of a quarter or longer). Simulated effect: variant T. Keep the eighth-note rows in Violins I 104-128.
3. Longer notes: do not cap blindly. Keep, by evidence: re-bow and loop fills (BRIEF 7), the c55 body lift, the hairpin gain (`hpgain`), printed accents (2-4 dB, BRIEF 4). Review by name: the 168 LEVEL_SHAPES rows that lie inside one note (109 of them 3 dB or more; `layers56.py` lists the counts), and the layers in finding 2.

**Pass limits (actor's own measures plus these).** Notes of 0.5 qn or less with 3 dB or more of envelope movement inside: 0 (c55: 443). Whole-movement step medians within 0.2 dB of c55 per string track. Theme Violins I 56-90: step p90 4.6 dB or less, front minus tail under 4 dB, S robust SD 15 ms or less with at most 2 notes over 40 ms (c55: 9 ms, 2). Violoncellos 520-536 step p90 under 5.1. The fitted fronts were measured on attack windows and my step measure uses the body (0.05-0.35 s); run both before deleting a row that the front measure defends.

### 2. Winds and brass: the fader adds an accent-shaped front to long notes that carry no accent (measured)

**Where.** Long notes (0.8 s or more) with no hairpin, no accent / tenuto / staccato / sf and no dynamic mark on the note: 29 of 254 brass and 27 of 217 wind notes have a fader front 3 dB or more over the body. Horn 3 256 (+10.5 dB), Horn 1 206 (+9.9), Horn 4 224 (+8.0), Horn 4 76 / 80 / 416 (+7.0), Horn 2 120 (+6.3), Horn 1 108 / 528 / 656 and Horn 2 112 / 228 / 532 / 556 (+5.5: -2 at the note-on, +2 from 0.1 to 0.45 s, -3.5 from 0.8 s); Oboe 1 582 and Bassoon 1 280 (+7.5), Bassoon 1 558, Bassoon 2 560, Contrabassoon 560 (+7.0), Bassoon 1 142 (+6.9), Clarinet 1 665 (+5.8). The fff chord at 484: Horn 2's fader goes -0.9 → +7.6 by 0.2 s and back to +0.4 by 0.8 s (ARRIVAL_WEIGHT plus a level shape).

**Evidence.** On these notes the stem's level range inside the note is larger with the envelope than without: Horn 1 108 7.3 / 2.4 dB, Horn 2 112 7.5 / 2.6, Horn 2 484 6.8 / 1.9, Horn 1 528 9.7 / 4.6, Horn 2 552 8.8 / 3.6, Oboe 1 558 7.7 / 3.6, Bassoon 2 692 7.1 / 3.2. Family totals for long notes outside hairpins: range over 6 dB on 45 brass notes with the envelope, 34 without; winds 34 / 28; strings 100 / 120 (there the fader helps).

**Why it matters.** A horn or bassoon note that swells 5-7 dB in its first half second and then sits back is heard as an accent or a fp. None is printed. In the ff tuttis of bars 28-31 and 133-141 these rows put such a front on the held horn notes bar after bar (inferred from the stem ranges above; not heard).

**Fix.** In `build/score_config.py`, delete the LEVEL_SHAPES / LEVEL_SHAPES_S rows that cover the notes listed above (`unmarked56.py` prints the 25 largest per family; rerun it for the full list) unless the row's comment names a fault it cured; where it does, replace it with one level for the whole note (the mean of the shape). Lower the 484 front on Horns 1-4 to at most +3 dB over the note's body. Pass: on long unmarked wind and brass notes, no fader front 3 dB or more over the body (c55: 56); horns' bar levels in 28-31 and 133-141 within 1 dB of c55.

### 3. 20 of 252 crescendos do not rise on their own stem and 4 diminuendos do not fall; one is in the theme's second phrase (measured)

Measure: stem level 0.08-0.45 s after the first note sounding in the hairpin against the same window on the arrival note (or the last 0.4 s inside the hairpin when the arrival falls on an opposite printed mark); "does not rise" is under +0.5 dB. Median rise 7.2 dB (strings 6.3, winds 7.5, brass 8.1); median fall 6.2 dB.

- **Violas 72-76 (bar 19, mf < f under the theme): -5.4 dB.** The stem reads -39.7, -41.0, -41.4, -41.0, -43.7 dB per quarter from 72 to 76 and jumps to -35.3 at 77. The per-note layers run +2.3 → -2.0 across the hairpin and +7.5 at 78; the trim gives -2.3. Fix: remove the negative rows on 75-77 and spread the +7.5 at 78 as a ramp from 72 (`score_config.py`, Violas rows in 72-78). Pass: each quarter of 72-76 at or above the one before, 76 at least 2 dB over 72.
- **Horn 1 408-411.5 and 413-415 (bars 103-104): -4.3 and -3.6 dB.** Per quarter -34.4, -36.6, -36.9, -38.3 while CC11 goes 80 → 91; the layers start at +4.6 on 408 and fall to -0.6. Fix: move the +4.6 from the first note to the end of the hairpin. This is next to the open "Horn 1 415" item.
- **Violoncellos 601-603 (-4.3), Violas 601-603 (-1.5) and 589-591 (-0.4), Cor anglais 602.5-604 (-3.2):** the dolce theme's one-bar swells in the recapitulation, C c52's finding 1 again on these parts. CC rises 6 units; the layers do not carry it.
- **Trim-caused (3):** Horn 4 248-252 (-0.9; trim -5.3 from p +12.4 to mp +6.0), Horns a2 480-484, Violas 72-76 in part. A narrow fix is enough: `mix.json` Horn 4 `soft_trim_db.mp` 6.0 → 8.0 (Horns 1-3 have 8.1-9.2).
- **No headroom (11):** crescendos that start at ff (curve 114 or more): 388-391.5, 393-395, 405-407 and 480-484 on Flutes 1-2, Bassoon 1, Violins II, Violoncellos, Double basses, Horns a2. At 480-484, the allargando into the tam-tam chord, Flute 2 falls 5.2 dB (layers -3.8 from 482) and five other parts stay flat; the master still rises 5.6 dB there. Fix only Flute 2: remove the -3.8 / -4.6 rows at 482-484.
- **Diminuendos:** Violas 612-616 rise 5.1 dB (CC 73 → 51, trim +0.8 → +5.0; `SOFT_DECRESC_KEEP` 0.5 lets half the rise through). Horn 2 260-268 +4.1, Horn 1 604-606 +1.6 (trim +3.4). Fix: a per-track `soft_decresc_keep` 0.0 for Violas and Horns 1-2 in `mix.json`, read in `vol_points` where `SOFT_DECRESC_KEEP` is used. The other four (Oboe 1, Violas and Clarinet 1 at 164-168, Double basses 720-724) fall inside the hairpin and only the arrival note is lifted; leave them.

Pass: crescendos under +0.5 dB at most 12 of 252 (the 11 at the ff ceiling less Flute 2, plus one); diminuendos not falling at most 4.

### 4. Winds in the Lento crescendo of bars 9-12 lose 3.5 dB against the strings; elsewhere they keep up (measured; minor)

Bars 9-12 (32-44, p < f): winds minus strings -0.2 dB in the first quarter of the hairpin, -8.2 in the second, -3.7 at the arrival; per-stem rise winds +9.9, strings +14.4 dB. The trim takes -9.0 and -10.7 dB from the clarinets (p +5.0 / +7.1 to f -4.2 / -3.8) and -4.4 to -5.0 from the others; Clarinet 1 gains 5.2 dB over 40-44 and Clarinet 2 6.5. The strings carry the line here, so this is a balance choice more than a fault. If the critic B table wants the wind chord at f: Clarinet 1 / 2 `dyn_trim_db.f` -4.2 / -3.8 → -2.5 (the scherzo's proposed value was -1.5 / -1.0), then check bars 26-32 and 139-142.

### 5. Arc and delivery pass; the margin of bar 160 over bar 122 is thin (measured; no change asked)

- Delivered mp3: -19.8 LUFS, LRA 14.4 LU (target 14-16), p10-to-max short-term 18.9 dB (target 16-19, at the top), true peak -1.7 dBTP. Master: -20.8 LUFS, LRA 23.2 LU, p10-to-max 30.6 dB. Dvořák 9/i reference: p10-to-max 26.1 dB.
- Delivery ride: gain -0.9..+12.1 dB; 0 of 277 five-second moves of 3 dB or more reversed, 270 keep at least half. The ride is at its cap (+12.0) through bars 175-182 and at -0.2..-0.9 on bars 119-122 and 159-161.
- Climax order in the mp3 (short-term max): bar 160 -11.4 > bar 122 -12.1 > bars 167-170 -13.9 > bar 26 -14.6 > bars 139-142 -15.0 > bars 113-120 -15.9 > recapitulation 131-134 -16.1. Bar 160 over 122: 0.7 dB short-term (C c52: 1.0, limit 0.5) and 0.3 dB momentary (-10.5 against -10.8). Both are printed fff. Do not let anything in finding 2 (the 484 horn front) or a delivery change close it further; re-check after the render.
- Bar 160 arrival: bar RMS +4.1 dB over bar 159, momentary +1.7 dB over the roll's last half bar.
- Coda: solo bars 171-174 -22.5 LUFS short-term median in the mp3, pp bars 175-178 -29.4, bars 179-182 -30.2; the strings' ppp is printed only at 724 and the master falls from -44.8 dB (720) to -53.1 (726) and to -66 at the written end. Final chord after the written end: -73 dB at +0.2 s, -85 at +0.6 s.
- Tutti stops (master, re the 0.4-0.1 s before the median note-off): c55 equals c54 and c51 within 0.5 dB at every point except the bar-83 ff end (qn 331), -21.2 dB at +0.3 s against -16.8 (c54) and -15.8 (c51). qn 679: -19.5 dB at +0.3 s; qn 551: -20.3; horn end at qn 55: -20 dB at 0.48 s. Not measured against recordings this cycle.

### 6. Loop pulsing: none over the limit (measured; no change asked)

`loopscan50.py` on the c55 render, 46 held spans of 6 s or more: no single piece of 6 s or more reads 0.40 or more at 3.95 s on the 100-300 Hz band or the centroid. Highest: Bass clarinet 464 (band +0.55 at 3.95 s, but its longest piece is 2.6 s: breath splits) and 492 (+0.37 / +0.34), Bassoon 2 48 (+0.33). Master: Lento bars 1-14 +0.30 band, final chord -0.11 / +0.08, bars 175-178 -0.11 / -0.25. Long string notes outside hairpins: the fader lowers the within-note range (median 6.0 dB with, 6.7 without; 22 notes carry a dip-and-return of 2 dB or more, 12 a swell-and-return), so the re-bow and loop fills are doing their job.

## Not measured this cycle

Hairpin curve shares at 34 / 50 / 72 % (C c52 finding 4), the bar-62 and bar-84 subito limits, low-end width, decays against the recordings' rtk figures, accent 2-5 kHz fronts. The envelope rebuild leaves out the tail hold and SUBITO_TAIL, which act in rests and at the two subitos only.

## Do not touch

The c55 body and tail lifts on the theme's long notes (`steady_body55.json`) and `C55_LONGEND`; re-bow and loop fills on held string notes; CC1 following the printed curve on the Sus Marc LITE rows; the delivery chain and `master_eq` (LRA 14.4, 0 reversals); the climax order 160 > 122 > 167-170 > 26; the final chord's fade and the tutti-stop decays; the dynamic-trim tables as a whole (no `CRESC_TRIM_HOLD`: 249 of 252 crescendos are not hurt by them); the phrase arch and hairpin curves of c51-c52.
