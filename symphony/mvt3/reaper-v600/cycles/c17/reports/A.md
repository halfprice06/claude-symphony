# Cycle 17, critic A: articulation and phrasing (on the c16 render)

All numbers below were measured on `cycles/c16/render/` stems and `build/parts.json` unless marked "inferred". Stems are post-fader, so levels quoted "without the fader" have `vol_db` subtracted. Nobody heard the audio.

Limits of this report: the session was interrupted by a usage limit. Not measured: loop pulsing folded at 3.95 s, 2-5 kHz accent bursts, the Violins II sustain-next-to-legato level, the theme head's fall, the ending's string level and room (item "c16 stem fix"), the low-end judgement, harp, cymbals and bass drum. The manual was read by passage, not by full page range (third round, own choice of pages).

## Manual notes

| Manual (May 2021, PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.92-93, Staccato: "Staccato On Bow" is a stroke where the bow stops on the string; all staccato patches are round robins of 9-16 samples | Double basses, eighths of 792-840 and 984-1108 on "Stac On Bow RRx9" | The row is used. The nine samples repeat exactly in the stem (period of 9 notes) and each has its own start time (75-118 ms from note-on to half-rise), so one lead cannot align them. Finding 1. |
| p.63, Note Velocity: velocity sets loudness and dynamics on the short instruments (Staccato, Staccatissimo, Marcato) | the same eighths (velocity 90 / 80 / 80 / 70 by position), timpani strokes | Not on this row in this range: velocity 65-95 gives 0.0-0.1 dB per 10 steps (r = 0.0-0.27). The beat weight written as velocity does not sound. Timpani "Hrd Lng" does follow velocity (0.17 dB per step at 80-127). |
| p.92, Marcato Short RRx4: short with a strong attack, 4 round robins; p.92-93 Shorts MOD SPEED (CC1 moves Staccatissimo, Staccato, Staccato On Bow, Marcato Short; 8 samples) | alternative rows for the basses' eighths | "Marc Shrt RRx4" was range-tested in c16 for separation only (8.0-11.0 dB), not for start time with a half-rise measure. Open. |
| p.93, Repetitions: the same note about a dozen times with the bow changing direction, with release trails | hammered eighths 199-210, 247-277 | Not used. MANUAL-GAPS lists it; its fixed speed has to match 172-184 qn/min, so it is a test, not a default. |
| p.99-100, brass Sustain: CC1 crossfades the 4 dynamic layers; Sustain Accent: velocity sets the attack, CC1 the body; Sustain Marcato Long / Short: a weaker attack than Sustain Accent, velocity opens a low-pass on the attack | brass accents (247-262 heads, chorale, codetta) | Accents play on the plain sustain with a CC11 bump of 5 units. CC1 (the dynamic lane on brass and clarinets) carries no bump at all (measured 0 on all 13 tracks). CC11 on these tracks is volume only, and 114 -> 119 is under 1 dB. Finding 2. |
| p.100, Shorts MOD SPEED (winds / brass): CC1 0-25 Staccatissimo, 26-51 Staccato, 52-77 Marcato Short, 78-103 Marcato Long, 104-127 Marcato Long + Sus | brass tongued eighths in the codetta (bars 91-92) and bar 277 | Not used. The tongued eighths there sit on "Sus MAX" with 32-37 ms gaps and run together. Finding 3. |

MANUAL-GAPS items that bear on the findings: individual accent rows (Sus Accent, Sus Marc) stay closed for the brass by Dan's "weight, not bite"; the Repetitions row and the Marcato Long + Sus zone are untested.

## Findings, ranked

### 1. Double basses' eighths on "Stac On Bow RRx9" (bars 199-210 and 247-277; qn 792-840, 984-1108): the strokes are late, not early, and velocity does not weight the beat (measured)

What is wrong. The c16 record says the strokes read 20-30 ms early and that the `ROW_LEAD_S` values did not take. The leads did take: parts.json has the note-ons 5 ms (792-840), 20 ms (984-1056) and 40 ms (1056-1108) before the score onset. The strokes themselves are slow. Time from note-on to the half-rise of the stroke (stem high-passed at 110 Hz, 12 ms envelope, searched from note-on +20 to +165 ms):

| span | n | note-on to half-rise, median (p10-p90) | lead now | half-rise against the grid |
|---|---|---|---|---|
| 792-816 | 39 | 84 ms (54-132) | 5 ms | +79 ms |
| 816-840 | 44 | 101 ms (41-130) | 5 ms | +96 ms |
| 984-1056 | 120 | 76 ms (33-132) | 20 ms | +56 ms |
| 1056-1108 | 104 | 97 ms (68-119) | 40 ms | +57 ms |

The same measure on the other strings' short rows gives 56-85 ms from note-on (Violins II "Stac RRx9" 56, Violins I "Staccatissimo RRx9" 71, Violoncellos "Stac RRx9" 72, Violas 85) with leads of 25-45 ms, so those land about +26 to +45 ms by this measure. The basses land 30-55 ms behind the upper strings in 792-840 and 15-30 ms behind in 984-1108. Cutting the lead from 40 to 5 ms in c16 moved them the wrong way.

Why the earlier reading said "early": the actor's detector (`cbtest.py`: 30-300 Hz, 6 ms frames, first frame within 6 dB of the peak) works on notes of 43-87 Hz, whose period is 11-23 ms, with strokes 170 ms apart whose tails are only 5-13 dB under the next peak. It often fires on the previous stroke's tail. My broadband fold shows the same weakness: the mean 30 ms envelope over all strokes of a span varies by only 1-3 dB across the eighth.

The spread is in the samples. In 1056-1108 (one pitch, C2, 104 strokes) the stem repeats with a period of nine strokes to within 1 dB frame by frame. Half-rise by round-robin position: 75, 111, 76, 112, 103, 82, 93, 118, 102 ms (sd inside one position 8-24 ms). The CC16 resets at 791.97, 815.97, 983.92, 1055.86 and 1087.88 make this repeatable.

Velocity does nothing on this row at 65-95: peak level against velocity has slope -0.014 to +0.107 dB per step (r -0.03 to 0.27); on-beat strokes (velocity 87-94) and off-beat strokes (68-70) differ by 0.0-0.5 dB in three of the four spans. The stroke-to-stroke level sd of 2-3 dB is the round robin, not the metre. Pitch still sets the level: at equal velocity C2 / D2 peak at about -36 to -40 dB and E2 / F2 at -42 to -45 dB (finding 4).

Fix (actor, `build/score_config.py`, last block):
- `ROW_LEAD_S["Double basses"]["Stac On Bow RRx9"] = [(792.0, 840.0, 0.06), (984.0, 1108.0, 0.06)]`. With 0.06 s the half-rise lands at +24 / +41 / +16 / +37 ms, the same place as the upper strings' short rows. Check that `ROW_LEAD_CAP_FRAC` does not clip it (the eighth is 0.17 s; 0.06 s is 35 % of the slot). Keep `len_frac` 0.58.
- Optional and exact: a lead by round-robin position. Since the section resets make the order fixed, give stroke k after each CC16 reset the lead (its half-rise - 0.045 s): for C2, 0.030, 0.066, 0.031, 0.067, 0.058, 0.037, 0.048, 0.073, 0.057 s. This needs a per-pitch table from one range render (the positions' times differ by pitch: spread sd 31-37 ms on the mixed-pitch spans against 21 ms on C2 alone). New option in `tools/score_to_parts.py`, e.g. `RR_LEAD_S = {track: {row: {pitch: [nine values]}}}` counted from the last `cc16` reset.
- Beat weight: velocity cannot give it below 96. Either test velocities 104 / 92 / 96 / 88 on a range (the c16 A/B at 110 / 98 / 98 / 88 gave 1.1 dB between on and off the beat and stood 9-11 dB hot, so pair it with `row_volume_db` about -8 dB on this row), or put the weight in CC11 (+8 units on beats 1 and 3 from 0.02 qn before the stroke to its end; measure the row's dB per CC11 unit on the same range first).
- Judge the result with the half-rise measure above (high-pass 110 Hz, 12 ms envelope), not `cbtest.py`'s rise.

### 2. Printed accents have no room to sound: the dynamic lane sits where the layers are flat, and brass and clarinets get the bump in the wrong lane (measured; the proposed amounts partly inferred)

Accent over the mean of its two neighbours, single notes, c16 stems: Flute 1 +1.7 dB (43 % under +1 dB), Oboe 1 +0.9 (52 %), Clarinet 1 +1.6 (40 %), Bassoon 1 +1.0 (51 %), Bassoon 2 0.0 (65 %), Horn 1 +2.1 (40 %), Horn 3 +0.3 (58 %), Trumpet 1 +0.1 (60 %), Trombone 1 +0.8 (63 %), Tuba +0.6 (62 %), Violins I / II +1.5 / +1.4 (45 / 36 %), Violas +1.4, Violoncellos +1.7, Double basses +0.7.

Causes:
- Strings and woodwinds: the base CC11 at accented notes is 114 (quartiles 110-117), and 21-40 % of accents start at 118 or more. Level against CC11 on sustain rows (fader removed, medians per band): Violins I -44.4 / -41.6 / -38.6 dB at CC 60-85 / 85-105 / 105-127, about 0.15 dB per unit; inside 105-127 the slope is 0.10 (Violins I), 0.18 (Violas, Violoncellos), 0.04-0.16 (flutes), -0.06 (Oboe 1), 0.07-0.21 (bassoons). A bump of 5 is 0.5-1 dB; the ceiling of 127 allows 2 dB at most.
- Brass and clarinets (`CC1_DYN_TRACKS`): the bump was written to CC11 (114 -> 119) and CC1 has none (0 on every accent of Horns 1-4, Trumpets 1-3, Trombones, Tuba, Clarinets 1-2). CC11 is plain volume there; 114 -> 119 is well under 1 dB.
- Velocity is already +10 to +20 on accents and does nothing on sustain rows.

Fix:
- Brass and clarinets: make the accent a volume accent with no change of layer, which is "weight, not bite" by construction. Lower the resting CC11 of these 13 tracks from 114 to 100 and add the lost level as a static track gain (about +2.3 dB if the law is 40 log(cc/127); measure it on one range render). Accent: CC11 121 from 0.01 qn before the onset, held 0.12 s, back to 100 by 0.40 s (the `GENTLE_ACCENT` swell times 0.02 / 0.18 / 0.40 already in the config). That is about +3.3 dB with CC1 untouched, so no 2-5 kHz burst from the top layer. In `score_config.py`: `ACCENT_BUMP_AT` 21 for these tracks, with a new resting value (`CC11_REST = {track: 100}` or the existing dynamic-to-CC11 map) and `mix.json` gains.
- Horns only, as an alternative where the phrase is below ff: CC1 +7 (Horn 1 measures 0.42-0.49 dB per unit at 85-127, Horn 3 0.22-0.32), capped at 117 so the top layer is not reached. Do not use CC1 for the trumpets' or Trombone 2's accents at f/ff: their slope above 105 is 0.06-0.22 and -0.01.
- Strings and woodwinds: give the accent headroom by lowering the plain notes, not by pushing the accent. In phrases that carry printed accents at f or ff, plain notes at CC11 106 (ff) / 98 (f), accented notes at 124, same swell times. At the measured 0.15 dB per unit that is +2.5 to +3 dB. The static loss (about 1.2 dB at ff) goes into the track gain. For the strings the tested alternative is the "Sus Marc LITE" row on accented quarters and longer (the scherzo measured that it does not take level from velocity, so set it with `row_volume_db`).
- Target per family after the change: median accent +2.5 to +3.5 dB over neighbours, under 20 % of accents below +1 dB, and the 2-5 kHz level of the first 80 ms no more than 3 dB over the note body.

### 3. Tongued note changes that run together are the ones with gaps under 60 ms; the 90 ms gaps work (measured)

Dip between two detached notes on a sustain row (lowest 15 ms frame between them against the lower of the two note bodies), by played gap in parts.json:

| track | gap under 30 ms | 30-60 ms | 60-100 ms | over 100 ms |
|---|---|---|---|---|
| Horn 1 | 2.9 dB (n 17) | | 6.1 (68) | 7.1 (16) |
| Horn 3 | 0.6 (5) | | 6.1 (50) | 6.0 (20) |
| Trumpet 1 | 1.5 (3) | 2.0 (3) | 8.3 (31) | 9.9 (20) |
| Trombone 1 | 1.3 (9) | 1.4 (5) | 5.2 (75) | 7.7 (20) |
| Tuba | 4.2 (9) | 0.5 (3) | 12.1 (60) | 13.5 (25) |
| Bassoon 1 | 1.4 (28) | 3.5 (128) | 7.4 (24) | 11.6 (25) |
| Oboe 1 | 1.4 (25) | 2.4 (34) | 5.5 (6) | 17.3 (9) |
| Clarinet 1 | 1.1 (69) | 6.5 (52) | 6.1 (16) | 21.5 (13) |

Some of the short-gap sites are under slurs and should stay joined; my slur parse of the events file was unreliable, so the actor must filter by slur. The sites that are certainly tongued and run together:
- bars 91-92, the codetta's eighths (qn 362, 366): Trombone 1 and Tuba 32 ms gap, 0.5-2.3 dB; Bassoon 1, Clarinet 1, Flute 1 21 ms, -1.2 to +1.6 dB; Horn 1 at 360 (59 ms, 0.6 dB).
- bar 277 (qn 1106): Trumpet 1, Trombone 1, Tuba 37 ms, -1.1 to +2.5 dB; Oboe 1, Clarinet 1 24 ms.
- bars 200 / 203 (qn 796, 808): Trumpet 1 32 ms, -0.2 / 2.0 dB; Oboe 1 808-812 21-42 ms.
- the combined heads of bars 247-252 (qn 986.5, 989, 994.5, 1002.5, 1005): a "Sus" note after a "Leg Slur" note with a 23 ms gap on Horn 1, Trombone 1, Flute 1, Oboe 1, Clarinet 1: 0.5-2.5 dB. This is also the head's repeated-note problem left open in c16.
- Tuba bars 28-32 (qn 108, 113, 124): 10 ms gap, 2.2-2.8 dB.
- Bassoon 1: 49-50 ms gaps at about 45 sites from bar 51 to bar 196 with dips under 3 dB.

Fix (`build/score_config.py`): the research default is 60-100 ms (brass median 98, winds 63). Set the gap of every detached (unslurred) join on a sustain row to at least 0.09 s on brass and 0.065 s on woodwinds, including eighths: `WIND_REP_RETONGUE_SHORT["gap_s"]` 0.1 already exists for repeats; extend the same gap to changes of pitch (a `DETACH_GAP_S = {"brass": 0.09, "wind": 0.065}` floor applied after the leads, shortening the earlier note). At bars 91-92 and 277 the eighth is 0.17-0.18 s, so the played note is 80-90 ms: if the "Sus" row does not speak in that time (check the range render), move those eighths to the row the trumpets already use for staccato ("Stac DblTng RRx9") on Trombone 1 / Tuba's equivalent short row. For the Leg -> Sus joins of 247-252, end the legato note 0.09 s before the tongued note (the keyswitch stays 0.15 s early, a closed item).

The brass chorale (223-234) shows the opposite: whole notes on Tuba, Trombone 1 and Trumpet 1 dip 4-12 dB at every bar line (qn 892, 896, 900, 904, 908, 920, 924, 928). The 90 ms gap is right for marked notes, but a chorale in whole notes wants a breath of about 40-50 ms at f (inferred from idiom, the dips are measured). Set a 0.05 s gap for notes of 4 qn and longer at Maestoso (888-936), or carry a CC1 lift of 6 units across the join.

### 4. Level by pitch: double basses arco, cello and bass pizzicato (measured)

Double basses, "Sus MAX" / legato, single notes of 0.25 s or longer, fader and the CC11 curve removed (n per pitch 4-43), against the median pitch: E flat 2 -6.7 dB, E2 -3.3, F1 -2.1, F2 -2.0, B flat 2 -1.9, F sharp 1 -1.7, E flat 1 -1.4; G1 +3.1, A flat 1 +3.8, C2 +2.8, C sharp 2 +3.3, G2 +2.1; spread 10.6 dB. The 87.3 Hz bell (-12 dB, 0.15 oct) now costs E flat 2 and E2 more than it costs F2. The basses' CC11 curve (medians): CC 46 -52.5 dB, 72 -47.3, 88 -44.9, 100 -40.5, 114 -38.3, 118 -38.6: 0.37 dB per unit at 88-100, 0.16 at 100-114, flat above 114. So at ff a weak pitch cannot be raised by CC11; loud pitches can be lowered.

Fix: a per-pitch CC11 offset on the sustain and legato rows (new table, e.g. `PITCH_CC11 = {"Double basses": {31: -12, 32: -14, 36: -11, 37: -12, 43: -8}}`, added to the dynamic lane for the length of the note, clamped at 127), which takes 2-3 dB off G1, A flat 1, C2, C sharp 2 and G2. Then test on a range render (bars 11-34 and 151-170): bell -12 -> -8 with F2 at CC11 -20 (F2 stood +5.8 dB at -8 in c16; -20 units from 114 is about -5 dB on the curve). If F2 holds, E flat 2 and E2 come back by about 3 dB. This is the per-pitch fix the closed item asks for before the bell moves. Where CC11 is under 100 (mf and below), raise E flat 2 by +10 and E2 by +6.

Pizzicato, bars 51-66 and 171-186 (qn 200-264, 680-744): every pluck has velocity 41 and CC11 34. Peak range Violoncellos 11.6 and 15.4 dB (sd 3.6 / 5.0), Double basses 8.7 and 6.7 dB (sd 2.3 / 2.0). By pitch (median against the passage): Violoncellos F sharp 2 +3.1, A flat 2 +4.4, G2 +5.0, B flat 2 -5.0, E flat 3 -2.6, E flat 2 -5.3, C3 -6.2; Double basses E flat 2 +3.6, C2 +3.2, F sharp 1 -2.7, G1 -2.3, B1 -2.5. Violins II and Violas play chords there and were not measured.
Fix: velocity per pluck. `build/pluck_trims.json` (c14) already holds a fitted dB per pluck; convert it to velocity with the row's slope from one range render at velocities 31 / 41 / 51 (the theme's staccato rows answered 3.4-11 dB for 16-22 steps in c16), and write it through `ROW_VEL_SPANS` or a new `PLUCK_VEL` table. Target: range under 4 dB as in c14.

### 5. Timpani: strokes need gain, not only velocity; the beat is not weighted (measured)

"Timpani Hrd Lng" strokes, level over the first 0.25 s: velocity 80-95 -44.3 dB, 95-110 -42.6, 110-127 -41.0; slope 0.17 dB per step at 80-127 (the scherzo's 3 dB per 22 steps is 0.14). The f strokes of bars 11-34 already have velocity 89-121 (median 113) and those of 199-210 99-121, so the missing 2.8-4.5 dB is not available from velocity (127 - 113 = 14 steps = 2.4 dB at best, and none for beat weight). In 247-270 the strokes have velocity 85-117 (median 91). Stroke-to-stroke step medians 1.68 (11-34), 3.64 (199-210), 2.97 dB (247-270). On-beat strokes are 2-3 dB softer than off-beat strokes in all three passages (-42.8 against -40.4, -42.1 against -38.9, -45.2 against -43.3) although their velocity is 8-16 higher: the drum or pitch on the beat is the quieter one.

Fix:
- `build/mix.json` Timpani `gain_db` +2.5 (a static balance, allowed), and lower the roll levels by the same 2.5 dB in the roll table (CC1 on "Hrd Rls", or the per-dynamic roll trims that are whole-roll levels), so the rolls stay where they are.
- Velocity by pitch and position (`score_config.py`, the timpani velocity map): bring the two drums level first (range render: the on-beat pitch +14 steps), then strong beats +10, weak -8, inside 84-127. In 247-270 raise the base from 91 to 104.
- Check Dan's roll rule after the gain change: the timpani's share of 30-150 Hz in the rolls of 219-223 and 273-278 must not rise.

### 6. Stop of bar 204, the sfp of bar 149, and per-note fader moves still in parts.json (measured)

Bar 204 (stop at qn 814.0, 299.61 s; next onset 0.57 s later). The master falls 12.5 dB by +0.3 s (my window; the record says 12.6). The return stems are not the cause: strings return -47.3 dBFS at +0.3 s, brass -50.7. The dry Violoncellos stem is: -32.2 dBFS before the stop, -40.3 at +0.3 s (8 dB down), -47.2 at +0.5 s. It is the celli's last note, G2 (the open G string), "Sus MAX", velocity 111: after the note-off the stem is 1 dB down at +0.1 s and 4 dB at +0.2 s. Violas are 20 dB down and Double basses 17 dB down at +0.3 s. Fix on the instrument: end that one cello note 0.10 s early (qn 814.0 -> 813.72, `end_at` / `cutoff_early` in `score_config.py`) and fall CC11 from its value to 60 over the note's last 0.12 s, holding 60 until 814.6 (CC11 acts before the hall, so nothing is cut, S3). Expected: the celli about 6 dB lower at +0.3 s, the master at about 15 dB. No return ride is needed. The same open-string release should be checked at other ff stops that end on G2 or C2 in the celli.

Bar 149, sfp (qn 592). Front (0.02-0.14 s) against body (0.5-1.0 s): Horn 1 -6.9 dB, Trombone 1 -4.4, Tuba -10.6, Timpani -11.3, Violas -5.0, Double basses -7.6, Violins I -2.3, Violins II -0.2, Violoncellos -0.5; master -4.5 dB. In 0.1 s frames the violins and celli do fall (Violins II -31 -> -47 dBFS at 0.4 s) but are back at the front's level by 0.8-0.9 s and 3-4 dB over it by 1.5 s: CC11 goes 114 -> 46 at 592.83 and is already 71 at 593.5. The p lasts about 0.3 s, so the sfp reads as a hole and not as a soft held chord. Fix (CC11 only): hold CC11 50-55 from 592.8 to 594.5, then rise to the printed arrival across 594.5-600 (on Violins I / II, Violas, Violoncellos; the brass and basses already hold). Trumpet 1 rises 7 dB over the same window; check its part against the score (I did not).

Per-note fader moves still in `parts.json` `vol_db` (17,404 points before thinning). Moves of 2 dB or more inside 0.6 s: 131 inside printed hairpins, 46 at hairpin edges, 430 elsewhere. Most of the "elsewhere" class are role and dynamic edges and the final fade (1113-1114, all tracks). The ones that are single-note moves and break Dan's rule:
- Horn 1: +1.8 dB lifts lasting one note at qn 94.97-95.5, 352.75-354.12, 654.97-655.5.
- Horn 2: +2.3 dB over one note at 822.75-823.5, and 358.75-360.09, 517.75-519.5 (two notes).
- Horn 3: +3.0 dB over one note at 76.98-77.5.
- Trumpet 2: +2.3 dB over one note at 656.92-657.5 and 660.92-661.5, +3.0 at 797.73-799.0, +2.9 at 993.75-995.0.
- Trombone 1: +3.0 at 407.73-410.0.
These look like the held unison level (`UNI_BOOST_HOLD_QN`) applied to unisons of one or two notes. Give the rule a minimum span (4 qn) or move these to CC11.
- Steps of exactly +3.0 dB inside 0.03 qn (about 10 ms) just before an entry: Flute 1 168.82, Oboe 1 184.84 / 325.85 / 559.85, Clarinet 1 176.82 / 400.82, Clarinet 2 914.9 / 1055.87, Bassoon 1 199.82 / 495.8, Bassoon 2 263.86 / 871.9, Contrabassoon 139.87 / 343.86 / 871.89, Violins I 472.63, Violins II 410.63 / 456.93 / 563.43, Violas 535.63, Violoncellos 535.38 / 871.57 / 935.6, Double basses 535.63, each paired with a -3.0 dB fall over 0.25 qn later. If these are phrase levels (solo or exposed-entry roles) they are within the rule, but a 10 ms step of 3 dB is a per-entry edge: ramp them over 0.25 qn in the rest before the entry, or put them in the role table.
- Timpani: 42 instant steps of 5-10.7 dB (15.98, 19.95, 20.5, 135.98, 139.95, 159.95 ...). They are roll levels, which the rule allows, but they are zero-length steps under a ringing drum. Confirm each falls in a rest or at a roll's first stroke.
I could not reproduce the split "113 hairpin-gain releases / 43 second-staff and unison ramps" exactly; the 46 hairpin-edge moves and the list above are what I found by slope.

Re-bows: `parts.json` lists re-bows in the chorale only for the Violoncellos (four, 915-935), with a dip median of 3.6 dB and a worst of 9.7 dB, and steps of 3.6 dB median (5.5 max) across the re-bow. Elsewhere: Violoncellos six re-bows, dip median 4.6 dB, step up to 11.7 dB; Double basses six, dip median 3.0 dB, worst 10.9; Violins I / II two each with steps of 11 dB (these two are probably dynamic changes at the re-bow, not checked). Without the fills the re-bow is audible. Fix on the instrument: overlap the two notes of a re-bow by 0.12 s on "Sus MAX" (the row is polyphonic) with CC11 -6 units on the outgoing note's last 0.12 s, in `tools/space_rebows.py` / the `AUTO_REBOW` branch; target dip under 1.5 dB and step under 1 dB.

Do not touch: the 90-100 ms gaps on brass repeats and detached changes (dips 5-13 dB, they work); the CC16 section resets (they make the round robin repeat exactly, which the per-position lead in finding 1 relies on); the timpani's "Hrd Lng" velocity response and current stroke timing (half-rise +21 ms, 5 of 14 and 19 of 38 outside 25 ms by a coarse measure); the theme's staccato velocities (`ROW_VEL_SPANS`); the one-row theme spans; the return rides at bars 2, 6, 113, 166; the basses' 87.3 Hz bell until the per-pitch CC11 test of finding 4 has been range-rendered; no per-note fader move anywhere.
