# Cycle 51, critic C: tempo, timing and transitions (review of the c50 render)

## Method

I measured the c50 master, its stems and the delivered mp3 with my own numpy scripts, and read the tempo map and note data from `cycles/c50/rendered_build/` (parts.json, score_config.py, entry_leads.json, score_to_parts.py). `diff -rq build cycles/c50/rendered_build` shows no file that differs, so the live build equals the data as rendered. I did not use REAPER and changed no setting.

- Tempo: the `tempo` list of parts.json converted to seconds per beat and per bar, against the step values of `symphony/mvt2/v600/global.ily` (the printed words plus their hidden `\mt` steps).
- Audio check of the map: Violas pizzicato triplets, bars 37-39, detected on the stem; the spacing between detected attacks equals the map within 1 ms on the intervals where the detector found both notes (all of bars 38-39).
- Breaks: master level in 50 ms frames around each caesura; stems for the tutti breaths.
- Fresh entries (a note after at least 0.4 s of rest on its track): the time at which the stem reaches 6 dB under its level, against the beat. I did not measure legato joins; critic A does (727 joins).
- Delivery ride: mp3 level minus master level per beat, bars 82-92.

Each judgement is marked measured, simulated or inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 51 (its last row is cycle 47), so there was no page range to read. Items of `loop/MANUAL-GAPS.md` and `DIGEST.md` that touch this lens (pages as cited there; I did not re-read the PDF pages this cycle):

| Manual (May 2021 HO manual, PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| Legato velocity sets the transition length; 50-60 gives a longer transition (p.144; MANUAL-GAPS 6) | Legato leads on the cantabile string lines, bars 23-28 and 53-56 | Not tried. Targets play at v124 with leads fitted to it. Not asked for this cycle: it would change every fitted lead |
| Felt Cresc timpani rolls have fixed lengths and end on a stroke (p.123, p.125; MANUAL-GAPS 7) | Rolls at qn 168, 200, 261 | Not used. If used later, the take length must match the roll at the local tempo; the roll at 200 lies in the printed allargando, whose last beat finding 2 changes |
| Keyswitches: a note C-2..G8 selects the articulation for the following notes (p.160-162) | Every KS Master track | Followed. The shortest time from a keyswitch to the note it serves is 20 ms (Violins II 143.98); no note-on precedes its keyswitch (measured, 32 tracks). Attack probe: 0 late |

## Every tempo change in the c50 map: printed or not, and how large

### Printed in v600 (measured; mockup values are beat averages in bpm)

| Bars | Printed (word; hidden `\mt` steps) | Mockup |
|---|---|---|
| 1-34 | Adagio, 52 | 52 as the base; bars 1-5 exactly 52 |
| 35-36 | poco rit. (49, 45) | 51.0, 49.1, 47.7 / 46.3, 45.0, 43.7. Bar lengths 3.66 and 4.00 s (a 52 bar is 3.46 s) |
| 37 | Poco più mosso, 60 | 57.6 on the first beat, then 60 |
| 47 | poco rit. (57, 55 on beats 3-4) | 57.5, 55.0 |
| 48-52 | poco sostenuto (54) | 54 as the base |
| 53-59 | a tempo, poco a poco animando (60, 61, 62, 64) | linear, 60.0 to 64.5 |
| 60 | poco allargando (62, 58) | 63.0, 61.0, 59.0, 52.1 (57.0 without the caesura) |
| 61-63 | Largamente, 54 | 54; the downbeats of bars 61 and 62 at 50.8 |
| 64 | allargando (48, 42) | 50.9, 46.5, 43.5, 40.5 |
| 65 | Tempo I, 52 | 52 |
| 78-82 | poco allargando (50, 48, 48, 46, 44) | linear, 51.3 to 43.3; beat 267 at 42.0 |
| 83 | a tempo (52) | 52 |
| 89-92 | rit. (48, 44, 40, 36); fermata (last beat 20) | linear, 50.7 to 35.2; last beat 20.0 (3.00 s); bar 92 lasts 6.34 s |

Every printed change is realised, within 6 % on every beat. Nothing printed is missing.

### Not printed (measured)

Of the 304 beats, 51 differ from the printed tempo by more than 5 %, 27 by more than 10 % and 12 by more than 20 %. The movement is 353.3 s on this map and 345.3 s on the printed steps (+2.3 %; section A, bars 7-30, +3.9 %).

| Kind (config table) | Where | Size |
|---|---|---|
| Section-cadence broadening: `PHRASE_SLOW_MAIN` (0.88, 0.80) plus a `CAESURA` | last two beats of bars 14, 22, 30, 70 (qn 40-41, 63-64, 87-89, 235-236) | beats +14 to +18 % and +38 to +42 %; bars 4.14, 4.19, 4.11, 4.07 s (+17 to +21 %) |
| Phrase-end slowing: `PHRASE_SLOW` (0.93, 0.84) plus a `CAESURA` | bars 10, 26, 40, 44, 74, 86 (qn 27-28, 75-76, 122-123, 137-138, 247-248, 284-285); bar 51 without a caesura | last beat +32 to +41 % (bar 51 +19 %); bars +11 to +16 % |
| Sub-phrase slowing: `PHRASE_SLOW_SUB` (0.97, 0.90), some with a `CAESURA` | bars 16, 18, 20, 32, 34, 38, 46, 49, 50, 52, 66 | last beat +9 to +25 %; bars +3 to +9 % |
| Caesuras inside printed tempo spans | qn 188 and 196 (inside the animando), 204 and 259, 268 (inside the allargandos) | beat +11, +6, +11, +6, +14 % |
| Single beats at x0.93 (`APEX_AGOGIC` and the first slowing beat) | beats 20, 34, 61, 68, 82, 110, 117, 129, 157, 229, 240 | -7 % for one beat |
| `BEAT_STRETCH`, 54 single beats | bars 6-88 | +4 % or -4 % (46 ms at 52); the Largamente downbeats 204 and 208 -6 % |
| `PHRASE_PUSH`, `TEMPO_PUSH` | first halves of phrases; bars 8, 27-28, 31-33, 45-46, 75-77, 83-84 | +1.5 to +5 % |

Printed breath marks exist at 10 of the 24 caesuras (29, 102, 124, 164, 188, 196, 204, 259, 268, 286). The other 14 (42, 48, 54, 60, 65, 77, 90, 96, 116, 139, 148, 171, 237, 249) have no breath mark in any part.

## Findings

### 1. Bars 10, 14, 22, 26, 30, 40, 44, 70, 74, 86: the unprinted slowings at the phrase ends are larger than the printed ritardandi, come every four bars in section A, and at most of them the sound does not break

**What is wrong (measured).** Bar lengths in section A, where the score prints one tempo (3.46 s per bar): bars 7-9 3.51, 3.34, 3.51; bar 10 **3.97**; bars 11-13 3.40, 3.46, 3.37; bar 14 **4.14**; bar 18 3.77; bar 22 **4.19**; bar 26 **3.90**; bar 30 **4.11**. The printed poco rit. gives bar 35 3.66 s and bar 36 4.00 s. So three unprinted bars are longer than the slowest bar of the only printed ritardando of the first half, and bar 86 (4.02 s, no tempo mark) is longer than bar 89 (3.72 s), where the printed rit. begins three bars later. A listener hears a ritardando at the end of every fourth bar of the theme (bars 10, 14, 18, 22, 26, 30) and the printed one in bars 35-36 as one more of the same size.

The last beats: qn 28 +38 %, 41 +41 %, 64 +42 %, 76 +32 %, 89 +38 %, 123 +41 %, 138 +34 %, 236 +41 %, 248 +32 %, 285 +36 %. Ten beats are over the range the plan gives for a phrase-end breath (EW-TEMPLATE-PLAN section 8: 15-30 % slower). The cause is that c46 applied the arc slowing and the caesura to the same beat: at bar 14, x0.80 gives +25 % and the 0.18 s caesura takes it to +41 %. The beat after each of these runs at 52-54 (the pickups at 29, 77, 237, 249 carry `BEAT_STRETCH` 1.04), so adjacent beats differ by 35-46 %.

At most of these places the sound does not break. Master level in 50 ms frames, lowest frame of the last 0.6 s against the lower of the levels before and after: 9.5 dB at 29, 10.4 at 102 and 9.2 at 124 (all three have printed breath marks); 5.5 at 54, 4.4 at 188, 4.3 at 116, 3.5 at 164 and 249, 3.1 at 268; under 2.2 dB at the other 15, among them 42 (0.2), 65 (none), 90 (none), 237 (1.8), 286 (none). At those the held chord lasts 0.4-0.5 s longer than its printed length with no break: the pulse stops, and no breath is heard.

Inferred: Dan described Movement I's main theme as choppy and out of time. He has not said this of Movement II, but this is the place in Movement II's map where the theme's pulse is least even, and the BRIEF allows only small liberties the score supports.

**Fix.** In `build/score_config.py`, a c51 block at the end:

```python
PHRASE_SLOW = (0.96, 0.90)
PHRASE_SLOW_MAIN = (0.93, 0.86)
CAESURA.update({29.0: 0.18, 124.0: 0.18, 286.0: 0.16,            # printed solo breaths: 15-30 % band
                42.0: 0.06, 65.0: 0.06, 90.0: 0.06, 237.0: 0.06,  # section cadences, no breath printed
                54.0: 0.05, 77.0: 0.05, 139.0: 0.05, 148.0: 0.05, 249.0: 0.05})
```

`PHRASE_SLOW_SUB`, `PHRASE_PUSH`, `PHRASE_RETURN`, `APEX_AGOGIC`, `BEAT_STRETCH`, the arcs and every other caesura stay (116, 188, 196, 204: finding 2).

**Expected (simulated by rescaling the c50 map).**

| Bar | Printed | c50 | Proposed |
|---|---|---|---|
| 10 | 3.46 | 3.97 (+15 %) | 3.80 (+10 %) |
| 14 | 3.46 | 4.14 (+19 %) | 3.84 (+11 %) |
| 22 | 3.46 | 4.19 (+21 %) | 3.87 (+12 %) |
| 26 | 3.46 | 3.90 (+13 %) | 3.67 (+6 %) |
| 30 | 3.46 | 4.11 (+19 %) | 3.84 (+11 %) |
| 40 | 4.00 | 4.45 (+11 %) | 4.29 (+7 %) |
| 44 | 4.00 | 4.48 (+12 %) | 4.26 (+7 %) |
| 70 | 3.46 | 4.07 (+17 %) | 3.77 (+9 %) |
| 74 | 3.46 | 3.87 (+12 %) | 3.64 (+5 %) |
| 86 | 3.46 | 4.02 (+16 %) | 3.85 (+11 %) |
| 35, 36 (printed poco rit.) | 3.67, 4.00 | 3.66, 4.00 | unchanged |

Last beats: +27 % at 28, +29 % at 123, +25 % at 285 (the three printed solo breaths); +21 % at 41, 64, 89, 236; +15-16 % at 53, 76, 138, 248; +20 % at 147. No beat is over 30 %. Every unprinted bar is shorter than bar 36. The movement becomes 350.4 s (2.85 s shorter). Bar 51 goes from +8 % to +4 % (the arc 160-168 shares `PHRASE_SLOW`).

**Acceptance on the c51 map.** No beat without a printed tempo word more than 30 % over the printed tempo; no unprinted bar longer than 3.90 s in 3/4 at 52; bars 35-36 and 89-92 unchanged.

**What the actor must re-check.** All tracks need `--midi-only --tempo`, because leads in seconds convert through the map. Notes that end in a changed beat get shorter in seconds: the pinned re-bow segments of the Double basses after 235.659 and of the Violoncellos div after 284.141 lose 0.30 and 0.17 s (re-measure the dip and step there; the 4.1 s pedal fills are protected), and the `JOIN_NOTCH` window of the Violoncellos at (76.890, 76.988) is defined as an offset in seconds from the moved onset at 77 and must be recomputed. Wind breaths at caesuras are set in seconds (`CAESURA_BREATH_S`), so they do not change.

### 2. Measured figures that run through a caesura limp on their last note; two of these caesuras sit inside the printed animando

**What is wrong (measured from the map; the first row also on the Violas stem).** A caesura puts all its extra time into the last quarter of the beat. Where a part plays triplets or sextuplets through it, the last note or two get all of it:

| Where | Figure | Note spacing in ms | Printed there |
|---|---|---|---|
| qn 115-116, bar 38 | Violas, pizzicato triplets | 344, 344, 344, 370, 370, **470** (audio 370, 371, 470) | no breath; a tempo |
| qn 187-188, bar 56 | Harp triplets | 326, 326, **446** | breath for Clarinet 1 and Horn 1 only; inside "poco a poco animando" |
| qn 195-196, bar 58 | Violas triplets | 317, 317, **396** | breath for 4 winds; inside the animando |
| qn 203-204, bar 60 | Violas sextuplets | 173, 174, 175, 176, **210, 244** | breath for 12 winds and brass; poco allargando |

In bar 38 the last pizzicato is 27 % longer than the two before it and 41 % over the printed spacing, at a place with no printed breath, in the one texture of the movement that marks every subdivision. At 188 and 196 the map slows one beat by 11 % and 6 % in the middle of a printed accelerando; the master dips only 4.4 and 2.6 dB there, because the strings play through. At 204 the slowing agrees with the printed allargando, but it arrives in the last two sextuplets (+19 %, +39 %) instead of across the beat.

**Fix.** In `build/score_config.py` (keep the keys, so the wind breaths and `CAESURA_BREATH_S` handling stay as they are; a value of 0 leaves the tempo unchanged):

```python
CAESURA.update({116.0: 0.0, 188.0: 0.0, 196.0: 0.0})
```

Optional, for 204 (generic, in `tools/score_to_parts.py` `add_caesuras`): a table `CAESURA_SPAN_QN = globals().get("CAESURA_SPAN_QN", {})`; for a caesura listed there, take `a = q0 - span`, `d` = the seconds from `a` to `q0` on the current steps, and multiply every step inside `[a, q0)` by `d / (d + extra)` instead of replacing the last 0.25 qn. Set `CAESURA_SPAN_QN = {204.0: 1.0}` in the config. The existing exit test ("tempo changes inside the slowed span") must be skipped for a listed caesura, since the allargando ramp has steps inside the beat.

**Expected (simulated).** Triplets 115-116: 370, 370, 370. 187-188: 326, 326, 325. 195-196: 317, 317, 316. Sextuplets 203-204 with the span: 190, 190, 191, 193, 194, 195 (the beat keeps its 1.15 s). Bars 56 and 58 become 3.92 and 3.83 s (printed 3.93 and 3.87).

**Related, not asked (inferred).** Under the same pizzicato triplets the single x0.93 beats at 110 and 122 give 358 ms against 333 ms for one beat (+7.5 %). If critic A or a listener finds bars 37-40 uneven after this fix, set `APEX_AGOGIC` back to the tool default 0.96.

### 3. The final fermata is short against the bar before it, and cannot be lengthened without a new re-bow

**What is measured.** Bar 91 lasts 4.52 s. Bar 92, the fermata chord, lasts 6.34 s (beats 1.63, 1.70, 3.00 s); at the tempo the rit. has reached (36) the same bar without a fermata would last 5.0 s. The fermata adds 27 %. In the audio the chord holds -51.0 to -52.6 dB (master) for 5.0 s and falls from 5.0 s on (-53.6 at 5.0 s, -56.6 at 5.5 s, -63.5 at 6.0 s), so it sounds for about 5.5 s, 1.2 times the bar before it.

**Judgement (inferred).** A fermata on a final ppp chord is usually held at least half as long again as written (7.5 s or more here). **No change is asked this cycle**: the last bow segment of the chord already lasts about 4.1 s (from the re-bow at 302.35), and a longer last beat takes it past the 3.95 s loop period, which is Dan's item 8 on this very chord. If the lead wants a longer fermata, override the last beat's tempo (20, from the score MIDI) to 14 in the tempo shaping (4.3 s, bar 92 = 7.6 s) and add one fitted re-bow on each string track near 303.4; treat it as a re-bow task with its own dip and pulse measurements.

## Checked, no finding (measured)

- **Delivery ride over the coda (the finale's rule).** mp3 minus master per beat: +11.4 dB (bar 82 beat 1), +13.6 (bar 83), +15.2 (bar 84), +16.0 (bar 85), +16.5 (bar 86 beat 1), then +16.4 to +16.9 on every beat to the end. The rise is slow and steady (about 0.3 dB per second over bars 83-85) and stops before the Clarinet 1 solo ends. The morendo falls in the mp3 exactly as in the master: bar 91 -28.1, -30.0, -33.5 and bar 92 -35.0 (master -44.8, -46.9, -50.4, -51.9); bar 89 beat 3 to bar 92 falls 13.5 dB in the mp3 and 13.7 in the master. With `TOP_RATIO` 2.0 nothing in bars 85-92 is reversed.
- **The tutti breaths before bars 59, 61 and 82.** Gap between note end and next note-on: at 196 Flute 1 and Oboe 1 127 ms, Horn 1 217, Bass clarinet 340; at 204 the eight woodwinds 136 ms, Horn 1 and Tuba 176, Timpani 631; at 268 eight woodwinds 226 ms, Clarinet 1 377. The breathing stems dip 10-40 dB; the master dips 2.6, 1.3 and 3.1 dB, because the strings (and at 268 the horns, bassoon 1, clarinet 2) are printed without a breath and play through. At 204 Violins I have a printed down-bow and tenuto and are joined with a bow-change legato (59 ms overlap). This follows the print.
- **Fresh entries after rests (S2), 141 entries on 32 stems.** Time at which the stem reaches 6 dB under its level, against the beat, medians: Flute 1 +5 ms, Oboe 1 -5, Cor anglais -5, Clarinet 1 +20, Clarinet 2 +20, Bass clarinet -5, Bassoon 1 +18, Bassoon 2 -10, Horn 3 -22, Horn 4 -40, Timpani 0, Harp +10, Violins I +55, Violins II +50, Violoncellos +28, Double basses 0, Violas div +45. The entries my first pass flagged were checked on 40 ms envelopes and are slow swells of soft notes that are within 6-9 dB of their level on the beat (Bassoon 1 at 18 and 102, Violoncellos div at 274, Violas at 279, the low brass at 200 under their crescendo), not late attacks. The Violas' portato eighths of bars 48-51 (15 notes): 6 dB under the peak at a median of -54 ms, 3 dB under at +26 ms, peaks at +40 to +280 ms. The c29 leads hold. At the climax downbeat 204 the Tuba (note-on on the beat, no entry lead) is 15 dB under its level at 0-40 ms and 6 dB under at 40-80 ms, with the timpani stroke at 0 ms; small, no change asked.
- **Keyswitch lead times.** See the manual table: minimum 20 ms, none late.
- **Section changes.** Poco più mosso (108), poco sostenuto (152), a tempo (172), Largamente (204), Tempo I (220) and a tempo (274) each start at the printed tempo within 4-6 % on the first beat and exactly from the second.

## Noted for other lenses

- The first note of several soft wind entries swells 6-9 dB over its first 0.35 s (Bassoon 1 at 18: -59, -56, -58, -57, -55, -54, -52, -51, -50 dB in 40 ms steps from -40 ms; Bassoon 1 at 102 the same shape). Whether a printed hairpin covers this is B's question.
- `cycles/c50/CHANGES.md` and the brief give the length as 354.70 s; the score ends at 353.30 s on the map, and the mp3 runs 1.40 s past it for the tail.

Scripts and cached data are in `/private/tmp/claude-501/mockup-loop/mvt2-c51-C/` (about 70 MB). I left the folder in place, because the launcher's instruction for this run was not to delete files.

**Do not touch:** the printed tempo ramps (`RAMP_SPANS`) and every printed tempo value; the arcs' positions and `PHRASE_SLOW_SUB`, `PHRASE_PUSH`, `PHRASE_RETURN`, `BEAT_STRETCH`; the caesura keys themselves (set values, do not delete keys: the wind breaths and `CAESURA_LIFT` depend on them) and the caesuras at 48, 60, 96, 102, 164, 171, 259, 268; `CAESURA_BREATH_S` 0.34 with its skips at 204 and 268; the wind and brass breath gaps at 196, 204 and 268; the string bow-change joins at 204; the c29 Violas portato leads and the c47 wind entry leads; `TIMP_DELAY_S` 0; the 3.00 s last beat and the re-bow design of the final chord; `tools/deliver_master.py` as set in c50 (`TOP_RATIO` 2.0), whose ride lets the morendo fall 1:1.
