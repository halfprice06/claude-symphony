# Cycle 16 (2026-11-11): the per-note volume automation, the bottom octave, the stops, the theme's return on one row

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c15 render). Snapshot of the tools and data before this cycle: `before/`. Scripts: `actor_scripts/`. Logs: `logs/`.

## 1. The per-note volume automation (first priority; Dan, 11 Nov)

### 1a. Tools

- `tools/score_to_parts.py`: every item of the volume envelope carries the name of the rule that wrote it. `VOL_PER_NOTE` = "on" / "cap3" / "off" (env `STP_VOL_PER_NOTE`) builds the envelope with the per-note rules on, with their sum limited to 3 dB, or without them; the slow layers (roles, hairpin gains, held decrescendos, long-note swells, divisi cuts, timpani roll levels, the final fade, and build_reaper.py's dynamic trims) are never switched. `VOL_RULE_OFF` and env `STP_VOL_OFF` leave single rules out.
- `tools/build_reaper.py` `THIN_DB` 0.1: a point is dropped when the line through its kept neighbours misses it by less than 0.1 dB (checked on the seconds axis, in dB and in a fourth-root amplitude scale). `VOL_LIN` in `score_to_parts.py` writes `vol_db` as a piecewise-linear lane, so a hairpin gain or a role ramp is two points and not a stair of grid points; `DYN_LIN_IN_HAIRPINS` does the same for the dynamic trims inside printed hairpins.
- Check of the thinning under the lock (`actor_scripts/envdump.py`: REAPER evaluates the written envelope every 5 ms, thinned against unthinned): see "Results".

### 1b. The three states, measured

The envelope is a gain after the instrument, so "off" and "cap3" were computed exactly on the c15 dry stems (`actor_scripts/envsim.py`, `simstates.sh`: stem x (new envelope - old envelope)), not range-rendered. Median level step between successive notes of a line (stem RMS over the first 0.35 s of each note from its note-on; `actor_scripts/stepmed.py`; full table `logs/stepmed_states_sim.log`, final column from the c16 render in `logs/render/stepmed_table.log`):

| line | c15 (on) | off | cap3 | verdict for the layer |
|---|---|---|---|---|
| first theme 11-26 Violins I / II / Violas | 1.88 / 1.60 / 1.87 | 2.11 / 1.43 / 1.32 | 1.63 / 1.48 / 1.42 | row levels help, most per-note steps do not |
| first theme 151-170 Violins I / II / Violas | 1.47 / 1.62 / 1.67 | 1.47 / 1.42 / 1.94 | 1.46 / 1.54 / 2.08 | Violas need their steps |
| theme in the bass 27-34 Violoncellos / Double basses | 2.21 / 1.15 | 2.26 / 2.25 | 2.00 / 1.23 | the basses' steps help (kept from 1.5 dB) |
| 27-34 Bassoon 1 / Tuba | 2.77 / 2.19 | 1.69 / 1.50 | 2.01 / 2.10 | unison boost and accent swells hurt |
| Horn 1 11-26 / 151-170 / 247-270 | 2.15 / 2.76 / 1.73 | 1.95 / 1.83 / 1.48 | 2.10 / 1.83 / 1.73 | unison boost hurts |
| Trumpet 1 muted 171-186, Bassoon 1 solo 115-122 | 1.84, 1.56 | 3.16, 1.82 | 1.84, 1.59 | fitted shapes help: kept |
| Timpani 199-210 / 247-270 | 2.11 / 1.45 | 5.00 / 2.47 | 4.66 / 2.70 | metric steps and attack lifts help: kept |
| Double basses 199-210 / 247-270 | 2.37 / 3.68 | 1.66 / 1.47 | 1.40 / 2.25 | the dips and metric steps make the steps; kept for the separation (S1), item 4e tests a short row |
| second theme, trumpet solo, cor anglais, chorale | equal in all three states | | | no per-note layer there |

A cap at 3 dB keeps most of what helps and removes little of what hurts, so the changes were made per rule.

### 1c. Final decision during the lock (Dan, 11 Nov 16:30Z, through the coordinator): no per-note volume moves at all

"yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem". Built so (`build/score_config.py`, last block): `VOL_PER_NOTE = "off"` with an empty keep list, `CHORD_CUTS = False`, `POST_SHAPES_S = {}`.

What the track envelope still holds: roles (`roles.json`, including one level per one-row span and five passage rows added after the render, below), printed hairpins and dynamics as ramps (hairpin gains, held decrescendos, the dynamic and soft trims), the held unison phrase level of Horn 1 / Horn 2 / Trumpet 1 and the other doubled winds (`UNI_BOOST_HOLD_QN`), printed player-count marks ("4 soli", "last 2 desks"), timpani roll levels over whole rolls (the printed roll hairpins, the per-dynamic roll trims and the settle of long rolls), the final fade. The four return tracks carry the stop rides.

Removed from the fader, on every track: accent swells (1,038 in c15), steady levels and fronts of the theme (506 + 3), pitch trims, row trims and row gains, note trims, metric steps (strings and timpani), the basses' and celli's repeat dips and beat gaps, brass and wind re-tongue dips, slur-pair releases, arrival weights, tenuto and long-note swells, re-bow fills, level shapes of every kind (bassoon solo, muted trumpet, sfp notch at bar 149, bar 222 / 245 fronts, dal niente fade-ins, per-pluck trims), timpani attack lifts and re-strike dips, divisi / double-stop / tremolo-chord cuts, the release fade after bar 94.

Instrument-side replacements made in this cycle:

| fault the fader covered | replacement | measured |
|---|---|---|
| staccato quarters of the theme too loud against the sustain row | velocity (`ROW_VEL_SPANS`: Violins I 100 -> 88 and 118 -> 96, Violins II 118 -> 100 in 151-170, Violas 100 -> 80, Violoncellos / Double basses 118 -> 96) | the rows answer: -3.4 to -11.0 dB for 16-22 steps (`logs/velchk_R1.log`); rows within 0.1-3.2 dB of the sustain row on range render R2 |
| tremolo and staccato rows' own level | the row's volume knob in the patch (mix.json `row_volume_db`, tools) | not isolated; the tremolo passages needed passage roles after the render (below) |
| accents | CC11 bump of 5 units (CC1 on brass and clarinets) on each printed accent (`ACCENT_BUMP_AT`) | too weak: see "now audible" |
| basses' repeated eighths running together | "Stac On Bow RRx9", 58 % of the slot, velocity 90 / 80 / 80 / 70 by position, +-5 (`ART_SPANS`, 792-840 and 984-1108) | separation median 9.8 / 11.7 / 9.9 dB on the render with no fader move (c15 with dips 14.0 / 14.2 / 13.3; "Sus MAX" without dips 0.2-4.9); under 3 dB 10 / 13 / 7 of 86 / 128 / 103 |
| theme's return on changing rows (4a) | one row ("Sus MAX"), class leads fitted on R1, repeat gap 0.09 s | below |
| Horn 1 / Horn 2 / Trumpet 1 level | held unison phrase level | stems within 0.4 dB of c15 over the movement |

The earlier per-layer rewrites of this cycle (front-weighted accents, steps keyed to the score onset, one level per run, reduced steady levels with `rowfit.py` / `notefit.py`) are in the tools and config but act only when `VOL_PER_NOTE` is "on"; they were range-rendered (R1, R2) before the decision arrived.

## 2. Bottom octave (`build/mix.json`, `build/pitch_trims.json`)

Simulated on the c15 stems first (`actor_scripts/bassband.py sim`, `logs/bassband_sim_*.txt`; RBJ models of the ReaEQ bands).

- Double basses: `mute_eq` (61.7 Hz -5, 73.4 Hz -4) and `loud_eq` (98 Hz -4, 160 Hz +3) deleted; the 150 Hz +4 bell (1 oct) replaced by 72 Hz +4 (1.5 oct). The 87.3 Hz bell stays at -12 dB: range renders at -4 and -8 dB left F2 9.9 and 5.8 dB over the median of the other pitches (the model had predicted -2). The pitch trims are off with every other per-note rule.
- Violoncellos: `eq` 170 Hz +3 -> +1, 125 Hz +3 -> +1.5; `loud_eq` (150 Hz +3) deleted; gain -4.5 -> -3.0.
- Tuba and Contrabassoon unchanged (0.1 dB on every figure in the simulation).

## 3. Stops

- `build/mix.json` `return_rides` (new, `build_reaper.py`): tail-only rides of the four return faders: +2.5 dB after the stop of bar 2 (qn 5.06), +3.0 after bar 6 (21.06), +3.0 after bar 166 (662.0), +6.5 over the chord of bar 113 (448-451.3; trombones, tuba, bassoons and basses have no send there). Simulated on the c15 stems (`actor_scripts/stopsim.py`).
- The celli / basses release fades after the stops of bars 2 and 6 (`POST_SHAPES_S` 5.0, 21.0) deleted; bar 94's stays.

## 4. Timing

- 4a: `STEADY_LINE` "Sus MAX" spans on Violins I, Violins II, Violas (792-816, 984-1056) and Violoncellos (792-816, 984-1012): no change onto a legato row left in the theme's return. Class leads start from each track's 600-632 classes and are fitted on the range render (`actor_scripts/fit16.py` -> `build/steady_leads.json`); one level per span (`steady_rows.json`); repeat gap 0.09 s; keyswitch 0.15 s before the remaining row changes there.
- 4b: Violins I entries 48 / 608 lead 0.090 / 0.066 -> 0.15 / 0.14 s. 4d: Violins I 744 entry lead 0.17 -> 0.22 s.
- 4e: range A/B under the lock (`p1cb.sh`, `cbtest.py`, `logs/cbtest_*.log`): "Stac On Bow RRx9" against "Marc Shrt RRx4" (separation median 9.8-12.8 against 8.0-11.0 dB; under 3 dB 12 / 6 / 5 against 8 / 12 / 2); "Stac On Bow RRx9" adopted on both spans.
- 4f: repeat gap 0.09 s inside the new spans. 4c, the rest of 4d and 4f: not done (below).

## 5. Crescendos

- `build_reaper.py` `CRESC_TRIM_KEEP` 0.5 with mix.json `cresc_trim_hold`: the trims fall only by half across the listed crescendos (Clarinet 1 / 2, Flute 2 1032-1048, Horn 1 1040-1048, Trombone 1 and Horn 3 880-884, Horn 2 516-520). A hold on every crescendo was simulated first (`actor_scripts/crescsim.py`): 104 hairpins would change by 1.5-5.6 dB and in 63 of them the hairpin's end would stand over the arrival, so the hold is opt-in.
- Double basses' metric steps: removed with every other per-note rule.

## Results (render of 11:09, stem fix applied)

Lock 09:45-11:13 (88 min; after the Scherzo, Movement II and Movement I): start, full rebuild of Violoncellos, build, thinning check, two range rounds (R1, R2), the 4e A/B, the final build (5 string tracks rebuilt in full for the row volumes and the basses' row; Horn 4 found stale by the state guard and rebuilt), restart, one render (`--force-memory`: REAPER 45 GB with 27 GB compressed, settled), `--mix-only` of the stem-fix roles, save, state guard 0 stale, quit. REAPER 46 GB after the render (28 GB compressed). Attack probe: 0 late or hole.

Stem fix (level only, `tools/stem_fix.py`, originals in `render_first/`): without the chord and tremolo cuts the final bars peaked at +1.9 dBFS (Violins I / II +8.1 / +8.7 dB against c15 in 271-279, Violins II +7.3 in 223-234, Violas +4.0) and the basses' short row stood 6.2 / 4.2 dB over c15. Passage roles: Violins I 1080-1116 -7.5; Violins II 888-936 -7.0, 1080-1116 -8.5; Violas 1080-1116 -4.0; Double basses 792-840 -4.0, 984-1080 -2.0 (in `roles.json`, written to REAPER with `--mix-only`). The string return stem was scaled over the same two passages by hand (`actor_scripts/retfix.py`: -3.5 and -6.0 dB), an approximation of the post-fader send.

| | c15 | c16 |
|---|---|---|
| master integrated / LRA / true peak | -20.6 LUFS / 22.9 / -1.3 dBFS | -20.5 / 23.4 / -1.8 |
| delivered integrated / LRA / TP / limiter / span | -19.8 / 14.8 / -1.5 / 2.1 dB / 19.4 dB | -19.8 / 14.8 / -1.5 / 1.2 dB / 19.3 dB |
| envelope points, all tracks (per second) | 53,696 (127) | 6,172 (15) |
| strings / winds / brass / timpani points per second (family totals) | 54.5 / 37.5 / 30.1 / 4.2 | 3.4 / 5.0 / 5.6 / 0.4 |
| notes moving 3 dB or more between note-on and next note-on (critics' measure) | 2,357 of 9,061 (851 unmarked) | 583 (60 unmarked) |
| the same from score onset + 0.02 s to the next score onset - 0.02 s | 1,562 | 333 |
| points attributable to a per-note rule | about 31,700 (59 %) | 0 (every such rule is off; `logs/verify1db.log`) |
| notes of a half or shorter with more than 1 dB inside | not counted | 325 of 7,519: 125 under a printed hairpin, 113 the release of a hairpin's gain after its arrival, 28 a dynamic change, 16 a role edge, 43 other (hairpins on the track's second staff, unison phrase ramps) |
| thinning check (REAPER's own evaluation, 5 ms grid) | | largest difference 0.10 dB (Violins I 3,495 -> 1,243 points, Double basses 6,837 -> 3,920, before the rules were switched off) |

Stops (drop at +0.3 s / time to -20 dB; limit 14.5-17 dB, 0.50 s): bar 2 17.4 -> 15.1 dB / 0.38 s; bar 6 18.0 -> 15.4 / 0.45; bar 94 15.6 -> 15.1 / 0.36; bar 113 20.5 -> 16.7 / 0.42; bar 166 18.1 -> 15.4 / 0.41; bar 204 14.3 / 0.45 -> 12.6 / 0.54 (outside both limits: the basses' and celli's level there is higher and nothing fades them); final chord 14.9 -> 15.5 / 0.39, RT60 1.42 / 1.31 s.

Bass band (share of master energy, `logs/render/bassband_c16.txt`): 56-112 Hz -14.5 -> -11.3 dB (target -11: 0.3 short), 56-71 Hz -22.7 -> -16.7, 140-355 Hz -6.6 -> -7.2, 28-56 Hz -28.4 -> -26.4; no bar over the limit (loudest bar 262 -25.7 -> -24.6 dBFS, limit -22.7); bar 223 -33.6 -> -29.1; loudness +0.10 LU.

S (29 lines; outside 25 / 60 ms): 469 / 99 of 1,401 -> 517 / 143 of 1,389 (target under 400 / 80 not met); with the codetta lines 497 / 103 of 1,484 -> 556 / 153 of 1,472. The change is the basses' eighths in 199-210 (27 / 5 of 90 -> 64 / 40 of 79 on the short row: strokes about 20-30 ms early with a wide spread; the `ROW_LEAD_S` values did not take). First theme 79 / 18 -> 75 / 17, bars 27-34 61 / 12 -> 60 / 9, recapitulation 90 / 16 -> 97 / 17, bars 247-270 54 / 19 -> 55 / 21 (target 40 / 10 not met). New one-row lines (R1 -> R2 after the lead fit): bars 199-204 40 / 8 -> 29 / 8 of 93, bars 247-264 104 / 13 -> 86 / 17 of 248. Level steps on the beat change the S reading (the scherzo's finding), so theme-line changes of a few notes are not timing.

Step medians, c15 -> c16 (`logs/render/stepmed_table.log`): Violins I theme 1.88 -> 1.32 and 1.47 -> 1.43; Violins II 1.60 -> 1.35; Violas 1.87 -> 1.42 and 1.67 -> 2.08; Violins I 199-210 2.20 -> 1.35, 247-270 1.71 -> 1.33; Horn 1 2.15 / 2.76 / 1.73 -> 1.88 / 2.00 / 1.52; Bassoon 1 27-34 2.77 -> 2.31; Tuba 2.19 -> 1.50; codetta trumpets / trombone 3.88 / 3.88 / 3.31 -> 3.02 / 2.23 / 1.46. Worse: Double basses 27-34 1.15 -> 2.32, muted Trumpet 1 1.84 -> 3.19, Bassoon 1 solo 1.56 -> 1.82, Timpani 199-210 2.11 -> 4.99 and 247-270 1.45 -> 2.47, Trumpet 1 247-270 2.04 -> 2.71.

### Now audible without the fader (measured; none was put back)

| track, bars | fault | measurement | tried / next |
|---|---|---|---|
| all strings and winds, every printed accent | accents hardly stand out | accent over neighbours, median: Flute 1 +1.6, Oboe 1 -0.6, Clarinet 1 +1.1, Bassoon 1 +0.1, Horn 1 +2.5, Horn 3 -0.9, Trumpet 1 +0.5 dB (c15 +2.4 to +4.2); 48-86 % of the woodwind accents under +1 dB | CC bump of 5 units; next: velocity plus a larger CC front below the top layer, "Sus Marc" rows on strings |
| Double basses, whole movement | uneven pitches | pitch medians F2 -7.3, F1 -6.0, B1 -4.6, E flat 2 -4.4, G1 +4.9, C sharp 2 +4.3 dB against the median (spread 12.2 dB; c15 10.2); theme in the bass 27-34 step median 2.32 dB (1.15) | EQ bell kept at -12; next: CC11 step per note / pitch |
| Double basses' eighths 199-210, 247-277 | early and uneven starts on the short row | rise against the grid: median -32 / -19 / -3 ms, 75 / 92 / 52 of 88 / 129 / 104 outside 25 ms (c15 44 / 68 / 58) | lead values did not take; next: per-row lead in `ART_SPANS`, or "Sus MAX" with a 90 ms gap |
| Horn 1, Horn 3, Trumpet 1, Trombone 1, Tuba, tongued note changes | notes run together | separation median -0.3 / -2.1 / 0.7 / 2.2 / 2.6 dB at 12 / 5 / 5 / 15 / 15 sites (with the dips 1.5 / 1.8 / 3.5 / 4.8 / 2.6) | next: longer played gap, re-tongue rows |
| Timpani, f strokes and rolls | strokes 3-4.5 dB softer, no beat weight | stem -2.8 dB over the movement (-4.5 in bars 11-34); step median 4.99 dB in 199-210 | next: stroke velocity (the scherzo measured about 3 dB per 22 steps) |
| muted Trumpet 1 171-186, Bassoon 1 solo 115-122, Trumpet 1 247-262 | uneven notes | step median 3.19 (1.84), 1.82 (1.56), 2.71 (2.04) dB | next: CC1 per note |
| strings, long notes with re-bows (chorale 223-234, final chords) | dips at re-bows | not measured on this render (c15 with fills: 0.5 to -0.9 dB; without, c15's simulation gave a step median of 2.25 against 1.93 on the celli) | next: overlap at the re-bow |
| strings, divisi chords and double stops | chords louder than single lines | Violins I / II +8 dB in 271-279 before the passage roles; elsewhere not corrected | next: CC11 per chord |
| string pizzicato (bars 51-66, 171-186) | uneven plucks | not measured on this render (c14: 16.6 dB range before the per-pluck trims, 3.1 after) | next: velocity per pluck |
| Violins II, sustain notes next to legato rows | 4 dB over the legato notes | c05 measure +4.7 dB; not re-measured | next: velocity / CC11 on the row |
| bar 204 stop | too wet | 12.6 dB at +0.3 s, 0.54 s to -20 dB | next: return ride with a negative value, or shorter releases |
| bar 149 sfp, bars 222 / 245, dal niente entries | the fitted fronts and fades are gone | not measured | next: CC11 shapes |

### Not done (for c17)

4c (Horn 1 / Trumpet 1 / Trombone 1 class leads in 247-270: no span-wise legato lead option; Trumpet 1's leads are tied to its moved-onset data), Violins II 300 (the sign of the leg_leads row could not be settled from the record), violas' repeats 816-840 (53 ms gaps), the head's repeated C on Trombone 1 / Bassoon 1, timpani stroke velocity, the per-note instrument-side levels listed above, an audit of `SLUR_PAIR_RELEASE` (82 shapes, now off). From the coordinator's relayed notes: the crescendo recount confirmed all seven listed hairpins (falls of 0.2-4.1 dB on their own stems); single-note row changes inside slurred lines remain outside the one-row spans.
