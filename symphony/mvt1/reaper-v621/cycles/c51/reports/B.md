# Critic B, cycle 51 (render c50): balance and levels, and the level cost of the c51 MIDI rules

Under review: `cycles/c50/render` (dry stems 01-40, returns 91-94), `build/parts.json` and `build/mix.json` (the c50 data
after its stem fix). I balance on the dry stems, K-weighted (8192 Hann FFT, hop 4096, stereo power, per 1 qn), with the
c50 actor's `bal50.py` method. Re-run on c50 it gives the actor's table to the decimal (measured). For c51 I predicted
each MIDI rule's level change and simulated it on the c50 frame powers as a per-track gain over time, then ran the same
check table on the result. The rule models are listed under each finding. Every predicted number is inferred; numbers
read off the c50 render or the patch files are measured or read.

## Manual notes (second round, c48-51: pages behind this lens's top open problems)

| Source (PDF page) | What it says | Where it applies | Render follows it? |
|---|---|---|---|
| 2021 p.53, p.64, p.150 | Velocity sets loudness and dynamic layer on shorts; samples of each recorded dynamic sit in velocity ranges (the manual's example: p 1-25, mp 26-45) | A #4: dynamics of string shorts by velocity with CC11 parked | Partly. The ranges differ per row (patch read below), so one velocity table puts different rows on different layers (finding 2) |
| 2021 p.64, p.151 | CC7 / fader for a track's ceiling, CC11 for the line inside it | All level work | Yes: levels in the volume envelope, CC11 for the line |
| 2021 p.93-94 | String shorts are round-robin instruments (9-16 takes); Repetitions is the exception "with release trails", so the other shorts have none | Celli 16ths (bars 117-121, 129-130), fugato staccatos | The AHDSR release governs the shorts' tails; A's 120 ms cap shortens them (finding 5) |
| Patches (read with `opus_state.load_oib`): Celli, 1st Violins, 2nd Violins, Violas KS Masters | Short groups have no CC11 connection; CC11 acts through the Global Group table (CC 72 -5.6, 88 -3.6, 100 -2.4, 114 -1.1, 120 -0.6 dB). Velocity zones: Celli Stac RRx9 1-36 pp / 37-68 p / 69-89 mp / 90-104 mf / 105-117 f / 118-127 ff; Celli Stac On Bow 1-62 mp / 63-110 f / 111-127 ff; Vln I Staccatissimo 1-54 / 55-89 / 90-114 / 115-127; Vln II Stac 1-55 / 56-91 / 92-115 / 116-127; Violas Stac 1-60 / 61-94 / 95-115 / 116-127. Velocity->Volume intensity 0.6 (celli, Vln II) or 1.0 (Vln I, violas) | Finding 2 | Read. Today's f notes play the celli "mf" samples, the Vln II "mp" samples, Vln I "mp"/"f" |
| 2021 p.112, p.144; Flute KS Master patch | True-legato velocity sets the transition time; "it does not affect loudness". The flute's TLeg groups have no Velocity->Volume connection | A #5 (wind legato velocity by dynamic) | Read: no level change expected (finding 5) |
| 2021 p.123-125 | Felt KS rolls: CC1 crossfades 8 layers, CC11 and velocity set loudness; Felt Cresc rolls are recorded | HP_CURVE on the timpani lanes; soft-roll low end | Measured on c50: 0.21-0.34 dB per CC1 unit on six of seven rolls; the CC7 lane adds about 0.14 dB per printed-level unit (inferred from kit §10's CC7 targets) (finding 1) |
| MANUAL-GAPS #12 (Felt Cresc), #4 (Mid mics on winds) | | | Still open, low priority for this lens |

## EW-TEMPLATE-PLAN sections this lens touches, and what is not yet applied

Not yet applied (c51 work): section 6 shorts with CC parked high (finding 2 gives a level-safe form); section 10 beat-position
velocity (on HO's zoned short rows it has to go into the volume envelope, finding 2); sections 7, 8 and 10 phrase shapes
and section 9 hairpin curves (findings 1 and 3); section 5 CC1-only macro test (not run; all our level work lives in
CC11 and the envelope); section 8 tutti entry spread and room-noise bed (not this lens). Applied with measured changes:
section 1 (Main at the seat with width 0.8), section 3 (the reduced timpani EQ and harp HPF; the timpani EQ is behind
finding 1b), sections 2 and 9 (returns and register sends; see the master note below).

**Reading the table on the master (measured).** Each return against its own family's dry stems, whole piece: R Strings
-14.6 dB, R Winds -12.5, R Brass -24.6, R Perc -8.4. In the master they add +0.15, +0.24, +0.02 and +0.58 dB to their
families. So the dry-stem table holds for the master within 0.25 dB except percussion. c49's stems carried the Opus hall
inside them, so for the tam-tam the fair comparison with c49 is tam-tam + R Perc: -7.1 dB at 484-491, inside the
-6..-7.5 window, where the dry stem reads -7.6. (Brass is 10-12 dB drier than strings and winds; that is a depth
question for the blend critic, not a level one.)

## Findings, ranked by what a listener would hear

### 1. Timpani: HP_CURVE on the roll lanes would put the bar-125 roll 1.9 dB over the Horn 1 solo; the soft rolls carry 7-12 points more of the low band because everyone else lost 2-2.5 dB below 150 Hz

**1a. Exclude the timpani from HP_CURVE (inferred from a simulation on c50 stems, roll slope measured).**

Where: the timpani's hairpins that are not long builds to f. The worst is the fff→pp diminuendo roll at 492-500 (bars
124-125). It runs under the sostenuto and under the Horn 1 "mp espr." solo of bar 125. Also hit: bar 11 (40-44, pp
crescendo to CC 86) and bars 41-42 (160-168).

Evidence. Rolls follow the printed curve twice: CC1 through `TIMP_CC1_MAP` (measured on c50 rolls at 316-324, 156-160,
40-44, 244-248, 480-484, 632-636: 0.21-0.34 dB per CC1 unit), and the CC7 lane (about 0.14 dB per printed-level unit,
inferred from kit §10's CC7 targets). C's held-note diminuendo point puts only 20 % of the fall at 60 % of the
hairpin, where the linear line has 60 %. The curve also gives a 2-4 qn crescendo 65 % of its rise at 40 %. Simulated:

| Roll | c50 | with HP_CURVE on the timpani |
|---|---|---|
| 496-500, timpani minus Horn 1 (solo) | -6.3 | +1.9 |
| 492-496, timpani minus the loudest other stem | -2.5 | +0.6 (the loudest stem) |
| bar 11, median / max re the loudest other | -7.6 / -4.9 | -4.7 / -4.1 |
| 160-168, energy-mean change | | +1.6 / +2.1 dB |

That is a long roll growing without a printed crescendo and covering a solo, against Dan's standing rule.

Fix:
- In `tools/score_to_parts.py`, where HP_CURVE is ported (the hairpin builder near line 1867), skip family "timp": the
  roll's CC1 and CC7 lanes stay linear.
- Do not apply C's held-note diminuendo point (60 % of the time, 20 % of the fall) to the timpani.

With that, every roll stays at its c50 value (simulated).

**1b. Soft rolls: take 2 dB out of the timpani's low band in the soft rolls only (measured cause, fix simulated).**

Evidence. Over each roll window I compared c49 with c50 in 30-150 Hz:

| Roll | Timpani 30-150 Hz, c49 → c50 | All other stems, c49 → c50 | Timpani share of the dry 30-150 Hz, c50 |
|---|---|---|---|
| bar 11 | -0.3 dB | -2.1 dB | 25 % |
| 13-14 | -0.7 | -2.4 | 32 % |
| 40-43 | -0.4 | -2.5 | 50 % (equal to every other stem together) |
| 127-130 | -0.1 | -2.4 | 16 % |
| 144-146 | -0.5 | -2.4 | 16 % |

K-weighted, both sides fell alike (timpani -2.3..-3.1 dB, others -2.2..-3.6). So the rolls are no louder overall, but
their bass is about 2 dB heavier against the strings' bass line. The cause is on both sides:
- the timpani's reduced family EQ (HPF 44 Hz, -6 dB at 385 Hz, +4.5 dB shelf) cut its body and kept its lows;
- the strings' 53 Hz HPF, the basses' 230 Hz cut and 35 Hz HPF, and the loss of the in-patch hall took 2-2.5 dB off
  every other stem below 150 Hz.

In the loud rolls (117-130, 158-160, 166-169) the timpani's lows fell with the rest, and the shares stayed at or under
c49's.

Fix (`build/mix.json`, Timpani). Add a `loud_eq` whose Wet is 1 only over the soft rolls:
```json
"loud_eq": {"bands": [{"band": "lowshelf", "hz": 160, "db": -3.0}],
            "points": [[0,1],[58,1],[59,0],[153,0],[154,1],[174,1],[175,0],[241,0],[242,1],[252,1],[253,0],
                       [501,0],[502,1],[514,1],[515,0],[567,0],[568,1],[586,1],[587,0],[715,0],[716,1],[728,1]]}
```
Add a +1.0 dB `LEVEL_SHAPES` row on the same spans so the roll's K level stays where c50 put it. Measured on the c50
stem, that shelf takes 1.9-2.5 dB off the soft rolls' 30-150 Hz and 0.9-1.8 dB off their K level. With the +1 dB row,
the simulated shares go 25 / 32 / 50 / 16 / 16 % → 18 / 24 / 41 / 15 / 11 %, and the roll medians re the loudest other
stay within 0.1 dB of c50's.

**1c. One render-side change (inferred).** The c50 stem fix raised the timpani's f/ff by +2 dB on the dry stem only.
c51's R Perc will carry that +2 dB too. In the roll windows the four returns together carry 10-18 dB less 30-150 Hz than
the dry stems (R Perc high-passes at 100 Hz), so this adds under 0.3 dB to the loud rolls' low band. Check bal50's "timpani + R Perc" rows on the c51 master.

### 2. String shorts (A #4): parking CC11 is a pure level swap, but A's single velocity table moves each row to a different recorded layer: celli f 16ths about -10 dB, violas mf +3 dB, alternate notes 10 dB apart in bars 117-121

Where:
- Violoncellos Stac RRx9 and Stac On Bow RRx9: 464-484, alternating rows in bars 117-121 (`meas_trem_alt`); 512-520 in
  bars 129-130; fugato 338-347.
- Violins I Staccatissimo, Violins II Stac, Violas Stac: bar 30 and bars 85-96.

Evidence:
- **CC11 on these rows (read).** It drives only the Global Group volume, so parking it at 120 raises a note by
  gg(120) − gg(old). That is +0.5 dB from CC 114, +1.8 from 100, +3.0 from 88 and +5.0 from 72. The timbre comes from
  velocity alone.
- **Today's velocities (read)** already put the f notes on or below the named layer:
  - celli Stac v96 is the "mf" zone;
  - Vln II v87 is "mp";
  - Vln I v87-95 is "mp" or "f";
  - violas mf v77 is "mp".
- **Layer steps (measured on c50).** Per note I took the 10 ms peak in the first 80 ms, minus the written envelope and
  the CC11 table:

  | Row | One zone down | Notes measured |
  |---|---|---|
  | Celli Stac, mp zone against mf zone | 10-13 dB weaker (median -28.4 against -14.5 / -17.8) | C2 only: bar 129, 12 notes, against bars 117-121 and 130, 76 notes |
  | Vln II | about -7.5 dB | 4-13 notes, pitches mixed, ±3 dB |
  | Vln I | about -3 dB | 4-13 notes, pitches mixed, ±3 dB |
  | Violas | about -3 dB | 4-13 notes, pitches mixed, ±3 dB |

- **A's table as written (f→76, ff→92, mf→62), predicted per note (inferred):**

  | Track and row | At f | Other dynamics |
  |---|---|---|
  | Celli Stac RRx9 | -9.9 dB median, 36 notes (mf zone → mp zone) | mf -1.6 |
  | Celli Stac On Bow | +0.7 (stays in its f zone, so the CC11 gain wins) | |
  | Vln I | +1.8, or -2 on the notes now in the f zone | |
  | Vln II | +2.4 | ff +0.3 |
  | Violas | | mf +3.1, ff -2.8 |

  Simulated: the celli stem at 464-484 goes from 10.8 to 14.6 dB under the other strings. In bars 117-121 consecutive
  16ths alternate between a row that drops 10 dB and one that rises 1-2 dB. The bar 127-130 roll's low-band share rises
  16 → 23 %, because the celli drop out of it.
- **Beat weights (inferred).** A's 0 / -22 / -12 / -22 on the celli at f gives 92 / 70 / 80 / 70: the beat is on the mf
  layer and the other three 16ths on the mp layer, so they come out about 10 dB under the beat (A's own target is
  1-3 dB). Inside one zone, velocity moves level only through Velocity->Volume: v96 → v104 is +0.4 dB at intensity
  0.6, if the term is 1 − I·(1 − v/127) in amplitude (inferred).
- **Wind rows (read).** A's row tuple starts with "Stac", which also matches the woodwind "Stac DblTng RRx9" rows. The
  pass-2 aliases Bassoon 1 stac, Cor anglais stac and Flute 1 stac play on them (zones 1-74 / 75-114 / 115-127,
  Velocity->Volume 0.6). Bassoon 1 stac's mf notes (v82 → 62) would drop a layer.

Fix (`tools/score_to_parts.py`, the A #4 option):
1. Restrict `SHORT_CC11_PARK` to family "string".
2. Write the CC11 park as an exact level swap. Per short-row note, add a volume step from its moved onset to the next
   onset of trim = gg(CC11 before) − gg(120) − 20·log10[(1 − I·(1 − v_new/127)) / (1 − I·(1 − v_old/127))], with gg read
   from the patch's Global Group table and I from the row's Velocity->Volume.
3. Keep each note's velocity inside the zone it plays now. Per-row tables in printed CC → velocity:
   - Celli Stac RRx9: 72→80, 88→97, 114→112;
   - Celli Stac On Bow: 88→96, 114→115;
   - Vln I Staccatissimo: 88→88, 114→95;
   - Vln II Stac: 88→87, 114→95;
   - Violas Stac: 72→77, 114→95.
4. Put A's beat weight into the envelope instead: +1.5 dB on the beat, 0 on the "and", -1 dB on the two 16ths between
   (kit §3, METRIC_DB). ±5 seeded velocity stays inside the zone.
5. If A wants the darker layers, test them in pass 2 one zone down per row. Add the layer offsets above (+10 celli
   Stac, +7.5 Vln II, +3 Vln I and violas) to the trim, and compare per-note levels with the main stem before adopting.

### 3. Phrase shapes (C #2) raise the soft brass and winds about 1-2 dB against the strings, and the coda trombone chorale by 2-3.4 dB, because the strings' last phrase is skipped

Where: everything at pp-mp. The largest local change is the trombone chorale at bars 175-178 (qn 698-716), under the
Clarinet 1 solo.

Evidence (inferred). I modelled the shapes with the finale's grouping and type rules (`symphony/mvt3/reaper-v600/tools/
score_to_parts.py` 3326-3440) and C's c51 values (start 0 strings / -8 winds and brass, rise +2 / +6, peak +10 at 0.44,
pre-end +4, end -12, drive (6, (10, 0.15), -10), dynamic scale, hairpin fades). Lane units go to dB with kit §4's slopes
(0.57 dB/CC at pp down to 0.12 at ff). Energy-mean change at flat printed dynamics:

| Family | pp | p | mp | mf-ff |
|---|---|---|---|---|
| Strings | +0.8 | +0.8 | +0.5 | +0.2..+0.3 |
| Winds | +1.9 (cor anglais, clarinets, bassoons +1.5..+2.5) | +0.4 | +0.3 | within ±0.3 |
| Horns | +1.2 | 0.0 | +0.8 | within ±0.3 |
| Trombones and tuba | +1.8 | | -0.3 | +0.7 at mf |
| Trumpets | | | -0.6 | within ±0.3 |

The strings' coda line runs unbroken from 680 to the final chord at 728, so the end rule (b ≥ end − 3.5) leaves it
unshaped. The trombones' chorale phrase gets the full arch. Simulated changes:
- pp chorale minus strings: -1.8 → +0.9 (window -1.5..-3.5);
- Clarinet 1's minimum over the loudest other, 699-706: +3.1 → +1.9;
- Horn 1 solo over the loudest other, bars 13-14: +11.3 → +13.0.

The finale's c07 measured the same kind of change on its own render: master LRA 20.5 → 23.5 LU and delivered LRA 13.5
at ratio 3.0, refit to 2.0 (`symphony/mvt3/reaper-v600/cycles/c07/CHANGES.md`).

Fix (`build/mix.json` and `build/roles.json`; these trims keep the c50 balance and leave each phrase's shape intact):
- `soft_trim_db` ppp and pp: Trombone 1, Trombone 2, Bass trombone -1.5; Tuba -0.5; Horns 1-4 -0.5; every wind track
  -1.0. Strings unchanged.
- `roles.json`: Trombone 1, Trombone 2, Bass trombone [698, 716, -1.2].
- Simulated with these: chorale -1.6, Clarinet 1 coda +3.5 / +4.8, pp low brass minus the upper strings -2.5 (c50
  -2.8), pp winds +0.7 (c50 +0.6).
- If C's (b) is ported (string phrases broken at rests of 0.5 qn or more and at printed dynamics), the strings gain about
  +0.3..+0.8 dB more at p-mp (inferred). Re-run the same-dynamic scan before trimming further.
- Refit `deliver_master.py` only if the delivered LRA leaves 14-16 LU.

### 4. Final corrections to the c50 table, with C #5 (bar 121) reconciled: Horns a2 +0.6 at 167-170, tam-tam +1.0, accompaniment -0.5 under the first theme, and C #5 without its brass cuts

Evidence (measured on c50, then simulated):
- **Trumpets a2 minus Horns a2, 167-170: +2.8** (limit +2.5). The tune is Horns a2 ff + Trumpets a2 ff + violas ff.
  The c51 rules leave it at +2.8, because both tracks get the same shapes.
- **Tam-tam fff minus all others, 484-491: -7.6 on the dry stem**, -7.1 with R Perc counted (above). C #5 as written
  moves it to -8.3, all c51 rules to -8.4.
- **Violins I theme over the loudest other, 15-22: +3.5** (edge of +3.5). The loudest other is the celli in 16 windows
  (+3.5) and the violas in 12 (+2.9).
- **Horns minus heavy brass, 123-126: -5.0.** Four horns against seven heavy brass, at Rimsky-Korsakov's "trombone ≈ two
  horns", sits near -5.4 (inferred). Leave it.
- **C #5 as written** (violins +2 to 492/496, flutes +1.5, the bar-121 ramp, brass -1.5 over 484-492.5, horns and
  timpani -1.5 over 484-490) moves brass minus strings at 115-122 / 123-126 from +0.9 / +1.6 to -0.6 / -0.2. That is
  more than 1 dB from c49 / c50 on both. HP_CURVE alone takes another -0.5 at 123-126 (strings hold their fff→p
  diminuendo longer).

Fix:
- `roles.json` Horns a2 [664.5, 679, +0.6].
- Tam-tam `gain_db` -2 → -1. The send is post-fader, so its reverb follows.
- `roles.json` Violas and Violoncellos [56, 88, -0.5]. Lowering the accompaniment keeps the violins' reverb as it is.
- C #5: keep its string and wind rows (the bar-121 ramp, flutes, Ob1 / Cl1 / BCl / Bn +1.5 at 484-486), but:
  - give Violins I / II +2 only over 484-488 and +1 over 488-492: Violins I [484, 488, -2], [488, 492, -3]; Violins II
    [484, 488, -2], [488, 492, -3], [492, 496, -4];
  - drop the brass, horn and timpani -1.5 rows.

Simulated with every c51 rule (shorts level-neutral, timpani linear) and the fixes of findings 1b, 3 and 4 (finding 5's
compensations are left out; they add at most 0.6 dB on the listed runs):

| Check | c50 | c51 rules as A and C wrote them | c51 with findings 1-4 |
|---|---|---|---|
| Brass minus strings 25-32 / 115-122 / 123-126 / 158-161 | -0.4 / +0.9 / +1.6 / -0.1 | -0.6 / -0.6 / -0.6 / -0.2 | -0.6 / -0.2 / +0.6 / -0.2 |
| Horns minus heavy brass 123-126 | -5.0 | -5.1 | -4.9 |
| Trumpets a2 minus Violins I / minus Horns a2, 167-170 | +1.5 / +2.8 | +1.0 / +2.8 | +1.0 / +2.2 |
| Tune (Hn a2 + Tpt a2 + Vla) over loudest other, 167-170 | +3.5 | +3.0 | +3.1 |
| Horn 1 solo 13-14 / Violins I theme 15-22 | +11.3 / +3.5 | +13.6 / +3.5 | +13.6 / +4.0 |
| Cor anglais minus Horn 1, 147-152 | -4.5 | -4.0 | -4.0 |
| Tam-tam fff minus all others (dry) | -7.6 | -8.4 | -7.8 (about -7.3 with R Perc) |
| pp chorale minus strings, 175-178 | -1.8 | +0.9 | -1.6 |
| Clarinet 1 over loudest other 699-706 (min / median) | +3.1 / +3.7 | +1.9 / +3.1 | +3.5 / +4.8 |
| Clarinet 1 solo over loudest other, 127-129 | +9.0 | +9.6 | +9.2 |
| Celli 16ths 464-484 minus the other strings | -10.8 | -14.6 | -11.2 |
| Roll bar 11 / 40-43 (median re loudest other, low-band share) | -7.6, 25 % / -9.4, 50 % | -4.7, 31 % / -7.6, 50 % | -7.6, 18 % / -9.7, 41 % |
| Roll 496-500 minus Horn 1 | -6.3 | +1.9 | -6.3 |
| Unchanged within 0.4 dB in every column | Horns a2 41-42, Trumpet 1 82-83, celli tune, harp, winds minus strings, cymbals, cello solo, timpani ppp | | |

The remaining brass-minus-strings drift at 115-123 is C's intended string step at the bar-122 arrival plus HP_CURVE.
Accept it, or add +0.5 dB on the brass over 488-504 if the c51 render reads under +0.5 at 123-126.

### 5. Small level effects: REP_SPLIT gaps -0.3..-0.65 dB on the repeated-note runs, the celli short lengths -0.6 dB, wind legato velocity and legato overlap none

Where and evidence:
- **A #1, REP_SPLIT gap 0.08 s / frac 0.35 / min 0.06 (inferred).** Model: from the earlier note-off the release falls
  10 dB per cap length (150 ms at mf-ff, 350 ms at p, the basses' 600 ms at pp). The kit's "too wet" note measured -8.5..-13 dB at
  150 ms after a phrase end with the 150 ms cap. Energy loss per slot:
  - basses -0.64 dB (112 repeats, 94 at mf-ff; gap 14 → 80 ms);
  - violas -0.42 (39 repeats);
  - Violins II -0.30 (15 repeats).

  No check-table row moves by more than 0.1 dB.
- **A #4, celli 16ths at 55 % with a 120 ms release cap (measured decay, inferred loss).** Isolated celli stac eighths
  (344-346) stay within 2 dB of their peak to 60-80 ms, then fall to -6 dB at 100 ms and -13 at 160 ms. Ending at 65 ms
  with a 120 ms release costs about -0.6 dB per 16th.
- **A #5, wind legato velocity 90-114 (read).** No level change on the target notes (p.144; no Velocity->Volume on the
  TLeg groups).
- **A #6, overlap in seconds.** No level change (inferred).

Fix:
- `LEVEL_SHAPES` / roles rows over A's REP_SPLIT spans at mf and louder:
  - Double basses +0.5 on 104-124, 324-328, 520-536, 554-568, 664-676;
  - Violas +0.4 on 86-100, 440-468, 552-568;
  - Violins II +0.3 on 86-100, 536-548.
- Celli +0.5 over 464-484 and 512-520.
- No trims for A #5 or A #6.
- Measure the runs on c51: per-qn K within 0.5 dB of c50, and A's repeat dips.

## Dan's standing checks through this lens (c50, measured by the actor and re-read here)
- **S1.** Repeat dips are 1.4-5.2 dB on the strings' stems. REP_SPLIT costs 0.3-0.65 dB of level there (finding 5); the
  compensation keeps the runs' balance while the dips open.
- **S3.** The bar-62 subito falls 14.0 dB by +0.3 s, with at most 8.8 dB in any 0.2 s.
- **Loops.** Bass clarinet 480 and Trombone 1 716 read 0.56 at 3.95 s on their dry stems, and the master stays under
  0.40. Trombone 1 716 is in the chorale that finding 3 lowers.
- **Accents.** Brass fronts are -16.3 dB under the body (median). No change from this lens.

Do not touch: c50's make-up gains, soft / loud trims and family EQs (every check passes except the rows corrected
above); the timpani's c49 mics, gain -7 and its f/ff +2; the basses' 230 Hz cut and register sends; the
Horns a2 bar-41 shape; the Trumpets a2 coda bell; the rows `fit_accents.py` fitted; the 600 ms basses pp cap and string
release caps; CC11 as the layer control on sustained rows; every c49 and earlier balance row not named here.
