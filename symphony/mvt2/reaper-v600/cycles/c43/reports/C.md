# Cycle 43, critic C: tempo, timing and transitions (on the c42 render)

Material: `cycles/c42/render` (master and 32 stems, after the stem fix), `cycles/c42/mvt2-mockup-c42.mp3`, `cycles/c42/rendered_build/parts.json` (every qn-to-seconds conversion uses its tempo map), the c35-c41 renders and parts.json for comparison, `build/score_config.py`, `build/mix.json`, `build/leg_leads.json`, `build/early_fills.json`, `build/mockup-events.tsv`, `tools/score_to_parts.py`, `tools/build_reaper.py`, `tools/pcx.py`, the c42 actor's `state_check.txt`, the c39 and c42 critic C reports, and the May 2021 HO manual PDF pp. 99 and 147-149 (row T2 of `loop/MANUAL-READING.md` for cycle 43), plus `loop/MANUAL-GAPS.md`.

Methods (all measured from the score onset `sq`):
- Levels: stereo power in 30 or 50 ms windows. Own-pitch traces: `pcx.band_env` (harmonic bands with the other pitch's harmonics excluded).
- Perceived attack: `pcx.attack_pcx` (pc = mean of the half-amplitude and the -10 dB crossings). For slow soft entries I also used the body-based arrival from c39 (b-6 / b-3: when the own-pitch band first reaches the body at +0.4..+0.9 s minus 6 / 3 dB).
- Legato joins: `tools/pcx.py` on c41 and c42 (pcX and the crossover).
- Breaths: the c39 dip measure (minimum in [onset - 0.6 s, onset + 0.05 s] against the mean over [onset - 1.2, onset - 0.6 s]), on the master, on all wind and brass stems summed, and on the string stems summed.

## Manual notes (T2: PDF pp. 99, 147-149)

| What the manual says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| A legato transition needs two notes with "no significant time gap"; the first note of a phrase has no legato (p.99) | Every legato join. Horn 4's slurred A flat 3 -> G 3 at qn 268 (bar 82) | Mostly. At Horn 4 268 the old note ends exactly at the new note-on, with no overlap and no gap. The join is then decided by event order and flips between renders (finding 4). |
| Legato instruments are monophonic by default; CC22 64-127 turns on polyphony (p.99; the 2021 text has the polarity right here, see the A2 row) | Every legato row | Yes. CC22 is never sent. Divisi chords play on Sus rows or split tracks. |
| Legato Slur Staccato adds an accent to the first note of each legato phrase (p.99) | Not used | Correct for this Adagio. No slur head in v600 is marked with an accent, except Trombone 1, which has its own treatment. |
| Bow-change legato has its own sound, independent of slur or portamento; the combined patches choose the component from the MIDI (p.99) | Leg BC MAX joins; the printed new bow at 204 | Partly. Leg BC MAX carries the unslurred joins. At 204 the strings join into the downbeat as legato targets, not on the printed new bow (c39 finding 1, left open). |
| Finger-position tables, FP1-FP4 per note: violins (p.147), violas (p.148), celli (p.149). On violins, FP4 puts E4-F sharp 4 (EW E3-F#3) on the G string. No FP puts a note above F sharp 4 on the G string | CC70 127 (FP4) on the "sul D" spans (Vln I/II 65-78 and 237-250, Vc 66-90, 138-151, 226-259), "sul A" (Vln I/II 171-188), "sul G" (Vln II 218-250) and "sul C" (Vla 218-226) | Partly. "Sul A" and the celli's "sul D" are right. On violins, "sul D" at FP4 sends F4 (MIDI 65) to the G string. Vln II "sul G" at FP4 holds C sharp 5 to E flat 5 (61-75) on the D string, which is the most the library offers. These are colour issues, not timing; c35 and c39 already noted them. |

## Extra checks, answered

1. **Horn 4 at qn 268 (+5.2 dB, 50 ms early).** It is audible on the Horn 4 stem but not in the master. The cause is a join that flips between two states on identical data. It is not the CAESURA and not a flipped Opus state. Details and the fix are in finding 4.
2. **The c42 600 ms caps and the tutti breaths.** No release runs into the breaths at 196, 204 or 268. The breaths are loud (f/ff). At CC11 that high the pp/p sample groups, which carry the 600 ms cap, are faded out, and the mf-ff groups keep 300 ms (unchanged since c41). The breath dips match the uncapped c39 render:

   | breath (qn) | master dip c39 / c40 / c41 / c42 (dB) | winds dip c42 (dB) | strings dip c42 (dB) |
   |---|---|---|---|
   | 196 | 1.9 / 2.0 / 1.8 / 2.0 | 5.5 | 2.1 |
   | 204 | 1.6 / 1.7 / 1.5 / 1.9 | 5.9 | 0.8 |
   | 268 | 4.0 / 4.7 / 4.1 / 4.3 | 4.7 | 3.0 |

   The group envelopes from 0.5 s before to 0.5 s after each breath agree with c39 within 1 dB. The exception is the strings at 196, which are 2 dB louder because of c42's +2 dB role over 190-199.6.

   Soft phrase ends do ring longer: 60 soft string ends were measured, and the tail at +0.3 s is 3-12 dB higher than in c41 on the affected notes. None runs into the next note of its own track. Three tails rise above the note's own end level, because CC11 climbs during the release (finding 5).
3. **The final chord's 7.3 dB step at 0.4-0.5 s.** It is not audible as a cut (inferred from the measurements below). No change is needed.
   - Master, in dB against the 0.3 s before the note-off, at +0.0 to +0.6 s in 0.1 s steps: -0.3, -1.9, -5.6, -11.4, -16.8, -23.6, -29.2.
   - The fall per 0.1 s is 1.6, 3.7, 5.8, 5.4, 6.8, 5.6 dB (50 ms windows; the actor's method read 7.3). The steepest step continues the steps on either side and does not break the curve.
   - The only break in slope is the hall plateau from +0.6 to +0.8 s, at -29 dB.
   - Time to -10 / -20 dB: 0.28 / 0.45 s. The recordings in the c42 C report give -10 dB at 0.20-0.40 s and -20 dB at 0.48-0.79 s, so -20 dB comes slightly early.
   - In the delivered mp3 the chord sits at -48 dBFS, 17 dB under the file's 10th-percentile 3 s level. The 0.4-0.5 s step therefore happens at -65 to -72 dBFS, and the plateau at -77 dBFS.
   - The mp3 ends 1.38 s after the note-off, with the tail below -90 dBFS. Nothing is cut.

## Where c42 stands (measured)

- **Tempo map.** Identical to c39 (402 points), so every printed tempo lands as c39 listed. The final chord lasts 6.34 s, the last beat at 20 bpm, and every track releases together at qn 304 with CC11 falling to 8.
- **Keyswitches.** 376, all before their note: minimum 19.6 ms, median 36 ms.
- **S2, entries after at least 0.45 s of silence (pc median / p90).** Strings +0.009 / +0.093 s (n = 61); winds -0.017 / +0.017 (57); brass -0.022 / +0.066 (20). All are the same as c41 within 14 ms.
- **Legato joins (pcX median).**
  - Strings: Vln I +19, Vln II +15, Vla +2, Vc +4 ms; unchanged from c41.
  - Horn 1: -19 ms.
  - Winds: Flute 1 +19, cor anglais +26, Oboe 1 +36, Bassoon 1 +39, **Clarinet 1 +56, bass clarinet +72 ms** (finding 1).

## 1. Clarinet 1 and the bass clarinet arrive late on every legato join: medians +56 and +72 ms, steady from render to render (S2; measured; audibility inferred)

**Where.**
- Bass clarinet: the solo of bars 31-36 (qn 90-108, "solo, espr.", chalumeau) and its line in bars 8-11 (qn 22-30).
- Clarinet 1: bars 54-59 (qn 175-195), the allargando and cadence of bars 77-80 (257-270), and the coda solo at 283.

**Evidence** (`tools/pcx.py`; c41 and c42 agree to the millisecond).
- Clarinet 1: all 20 joins are late, +31 to +190 ms; pcX median +56 ms, crossover median +56 ms, robust SD 21 ms. Every join uses the 0.03 s lead (`LEG_LEAD_S["Clarinet"]`). The worst are 258 (+190) and 259 (+171), in the poco allargando, and 186 / 194 (+102 / +104).
- Bass clarinet: pcX median +72 ms, crossover median +83 ms, all at the 0.05 s lead. Solo joins: 91.5 +112, 92 +42, 92.5 +73, 93 +35, 97 +43, 98 +103, 99 +86, 101 +22, 106 +58, 107 +11; also 26 +150, 32 +238, 108 +198. Onset 30 already has a +0.15 s extra and lands at +35.
- The other winds are within +19..+39 ms; the strings and Horn 1 are within ±20 ms.

At 46-52 bpm these note changes in exposed solos come 5-7% of a beat behind the harp and the held accompaniment, every time. A steady lag of this size reads as dragging (inferred).

**Fix** (`build/score_config.py`, after the LEG_LEAD_S definition; `by_name` takes the first matching key, so "Clarinet 1" must come before "Clarinet"):
```python
LEG_LEAD_S = {"Clarinet 1": 0.08, **LEG_LEAD_S}
LEG_LEAD_S["Bass clarinet"] = 0.10
```
`build/leg_leads.json` (extras added to the family lead):
- "Bass clarinet": "30" 0.15 -> 0.10 (keeps its total at 0.20 s); add "32": 0.12, "108": 0.10, "26": 0.06.
- "Clarinet 1": add "258": 0.10, "259": 0.10.

LEARNINGS section 5 says the response to added lead is not always 1:1, so re-measure every listed join.

**Accept when** (pcx.py on the next render):
- Clarinet 1 median within ±25 ms;
- bass clarinet median within ±30 ms;
- no join on either track earlier than -60 ms;
- in the bass clarinet solo, the master's join dips no deeper than c42.

## 2. Horn 1's f note after the bar 59 breath (qn 196) swells in over 0.6 s, so the counter-melody restarts half a beat late (S2; measured; fix simulated)

**Where.** Horn 1, F sharp 4 at sq 196 (bar 59, f, after its printed breath), Sus MAX, v83, `REATTACK_LEAD_AT` 0.10 s. This is c39 finding 5, not acted on since.

**Evidence** (c39 and c42 identical).
- Own-pitch band at 0.1 s steps from the onset: 21 22 24 22 26 28 30 30 30 dB.
- Broadband: -38 dB at the onset, -29 dB from +0.6 s, a 9 dB rise.
- In the first 0.4 s Horn 1 sits 4-8 dB under Violins I, then level with them.
- The rise is not caused by a late start: the envelope's f step (vol 4.4 -> 8.3 dB) is already complete by 196.14.
- The violins at 196 reach their body at once (c39: b-6 -0.03).

**Fix.** Add to `build/score_config.py`, in seconds around the score onset (the LEVEL_SHAPES_S form):
```python
LEVEL_SHAPES_S["Horn 1"] = LEVEL_SHAPES_S.get("Horn 1", []) + [(196.0, [(-0.11, 0.0), (-0.08, 5.0), (0.25, 4.0), (0.7, 0.0)])]
```
- Simulated on the c42 stem: the front rises from -38/-37 to -33/-32 dB.
- Horn 1 minus Violins I at 0 / 0.2 / 0.4 / 0.6 s: -1 / 0 / -5 / +2 dB (c42: -6 / -4 / -8 / +1).
- The 50 ms peak in the first 0.6 s is 0.5 dB over the body (c42: -0.4).
- It ends inside the note, so no tail is cut (S3).

**Accept when:** Horn 1 b-3 at 196 within +0.25 s; peak over body at most 2 dB; Horn 1 not over Violins I at 196-197.

## 3. Bar 71 (qn 238), the downbeat of A': the violas' first pp eighth swells 20 dB across its whole length and peaks as the second eighth begins (S2; measured; fix simulated)

**Where.** Violas, C4 at sq 238 (pp, "ord.", the first of a slurred eighth figure under the violins' theme and the celli's cantabile). It is an entry after the bar 66 niente. Moved onset 237.847 (`entry_leads` 0.08 s), v37. The next note, E flat 4 at 238.5, is a legato target led to 238.275.

**Evidence.**
- b-6 / b-3: +0.18 / +0.24 s, the same in every render c36-c42.
- On the same beat: celli +0.02 / +0.06, Clarinet 2 -0.02.
- Broadband from the moved onset: -66, -62 (-0.1 s), -59 (0), -57, -56, -53, -51, -48 (+0.3), -45 (+0.45 s).
- The C4 is still rising when the E flat takes over (crossover +0.55 s; score 238.5 is at +0.595 s).
- An early fill held 0.12-0.25 s moves b-6 by 0.02 s at most (simulated). The note has no body to reach before the next one arrives, so the fix has to be a front-loaded shape that flattens the swell.

**Fix.**
```python
LEVEL_SHAPES_S["Violas"] = LEVEL_SHAPES_S.get("Violas", []) + [(238.0, [(-0.21, 0.0), (-0.17, 8.0), (0.10, 6.0), (0.45, 0.0)])]
```
- Simulated on the c42 stem: -54/-52/-51 dB at -0.05 / 0 / +0.05 s (c42 -62/-59/-57), then the same as c42 from +0.45 s.
- No peak over the c42 maximum. The master moves less than 0.5 dB.

**Accept when:** Violas b-6 at 238 within +0.08 s of the celli; 50 ms peak in [238, 238.5] no higher than c42's.

## 4. Horn 4 at qn 268 (extra check 1): a slur that starts on a tied note is dropped for winds and brass, so the A flat -> G join plays either as a legato transition or as a first note, and which one varies between renders (measured; cause read in the code; inaudible in the master)

**Where.** Horn 4, bar 81-82: A flat 3 at 265, tied to 267, with the slur starting on the tied 267 (`Hn4 267 slur -1`), into G 3 at 268 and E flat 3 at 270. Horn 4 has no breath mark at 268. The score asks for a slurred line through the tutti breath.

**What happens (read).**
- The tie merges 265 + 267 into one Sus MAX note, 265.0-268.0.
- `score_to_parts.py` (the c16 A #4 block, about l. 1946) moves a slur that starts on a tied continuation onto the merged note only when `family == "string"`.
- For Horn 4 the merged note is therefore outside the slur. The 268 note becomes a slur head: on Leg Slur MAX (keyswitch 267.94), v91, no lead, and the A flat gets no overlap.
- Both notes sit on the same tick, 268.000. The KS Master's legato script then sees "no significant gap" (p.99) or a gap, depending on whether the note-off or the note-on is processed first.

**Evidence** (notes, keyswitches and CC lanes identical in c35-c42).

| render | state | G3 band 0-0.1 / 0.1-0.2 / 0.4-0.8 s (dB) | crossover |
|---|---|---|---|
| c35, c36, c37, c39, c42 | A: joined | 9.2 / 12.4 / 13.2 | +0.024 s |
| c38, c40, c41 | B: first note | -3.8 / 6.0 / 10.8 | +0.10 s |

- In both states the old A flat's partials fall the same way, so the release is not involved.
- State B sags 4-6 dB under the A flat for 0.4 s; state A rises 3.5 dB and settles.
- The flip happened in c42 although Horn 4 was not rebuilt, so it is render-to-render variation, not the build.
- The CAESURA at 268 only lengthens the held A flat (the last 0.25 qn lasts 0.47 s). The tutti breath logic does not touch Horn 4 because it has no breath mark.

**Audibility.**
- Horn 4 sits 13-17 dB under the master at 267.5-269.
- Swapping the c41 Horn 4 stem into the c42 master changes 268-268.5 by 0.1 dB overall and 0.3 dB in 400-1000 Hz.
- In state A Horn 4 is level with Horn 3 (-35.1 / -35.4 dB); in state B it is 4.5 dB under.
- Not audible in the mix (inferred). The cost is that renders do not repeat and state_check keeps flagging the note.

**Fix (generic, `tools/score_to_parts.py`).**
- In the c16 A #4 block, add a wind/brass branch: when a slur starts on the tied continuation of a monophonic wind or brass note, set `n["slur_start_sus"] = True` (the note is already on the Sus row).
- The existing note-end rule (`elif n.get("slur_start_sus") and not same_pitch: n["end"] = e0 + LEG_OVERLAP`, about l. 2449) then overlaps the A flat into the G by 0.04 qn. The KS Master joins an overlapping Sus note into a Leg Slur note as a transition (LEARNINGS section 6, c23). That is state A, which crossed on time without a lead.
- Movement II has only one other wind/brass slur that starts on a tie: Flute 1 at 208 -> 212. Its 204 tenuto already takes the earlier `sost_sus` branch (end 212.03, stable in c34-c42), so it does not change.
- Check in parts.json that only Horn 4's 265 note changes (end 268.0 -> 268.04).

## 5. Release tails (extra check 2): where CC11 climbs back during a release, the 600 ms tail rises above the note's own end level (measured; inaudible now, low priority)

**Where.** Rests of 0.5 s or more, where the next note's CC11 level is written at the note-off. The worst cases are Violas 51 (bar 18, end of a p diminuendo: CC11 28 -> 34 at 51.0), Violas 63 (28 -> 34) and Double basses 115 (42 -> 46).

**Evidence.**
- Peak of the tail in +0.1..+0.4 s against the last 0.1 s of the note: Violas 51 +3.7 dB, Violas 63 +1.9 dB, Double basses 115 +1.4 dB.
- 48 rests across all tracks have a CC11 rise of 3 CC or more within 0.6 s of the note end. On the other 45 the tail still falls.
- Violas 51 in c39 / c41 / c42 at 0.05 s steps after the end: c42 holds -51..-54 dB for 0.3 s, where c39 had fallen to -62.
- CC11 acts inside Opus on the releasing voice. `build_reaper.py` holds the volume envelope through such rests (`tail_hold`) but not CC11.
- These stems sit 12-25 dB under the master, so no listener hears it now (inferred). Longer caps, or a softer passage, would make it audible.

**Fix (generic, `tools/score_to_parts.py`, default on).** In rests of `TAIL_HOLD_MIN_S` (0.5 s) or more, hold CC11 at the value it had at the note-off until `TAIL_HOLD_LEAD_S` (0.35 s) before the next moved onset, and only then step to the next note's value. This matches build_reaper.py's volume tail hold. Leave rests shorter than 0.5 s alone: the repeat strokes and `sus_fall` rely on their own CC11 timing.

**Accept when:** no soft end's tail peaks above its last 0.1 s; the entry b-6 after these rests is unchanged.

## Checked and fine (measured unless marked)

- Tempo spans (`RAMP_SPANS`, `PHRASE_ARCS`, `TEMPO_PUSH`, `BEAT_STRETCH`, `CAESURA` 204 0.10 and 268 0.15) are unchanged since c39, and the printed changes are clean steps: Poco più mosso 45 -> 60 at 108, Tempo I 40.5 -> 52 at 220, a tempo 43.3 -> 52 at 274.
- The final fermata: the joint release at 304, the CC11 morendo to 8, and the decay (extra check 3).
- No legato or entry timing moved between c41 and c42: string join medians within 2 ms; the largest entry change was 14 ms (Violas div 81).
- Other late entries left alone:
  - Violas 279 and 66 (b-6 +0.15 / +0.14): c39 found that a fill overshoots.
  - Celli 286 (b-6 +0.03 after c39's fill; b-3 +0.30 is the slow pp body).
  - Violins II 108 (+0.11, the sul tasto pad).
- Horn 3 267 is a legato sag (5-7 dB for 0.5 s after the F4 -> E4 join), not an attack lag. A front shape simulated here overshoots by 4 dB because of the old note's tail. It belongs in auto_fills (lens A).

Do not touch: the tempo map and every tempo table (`RAMP_SPANS`, `PHRASE_ARCS`, `TEMPO_PUSH`, `BEAT_STRETCH`, `CAESURA` 204 0.10 / 268 0.15); the final bar's joint release, CC11 fade and the 600 ms pp/p string caps (the final chord decays smoothly and no breath is blurred); the mf-ff 300 ms string and 237 ms horn caps; keyswitch placement and the pre-roll CC36/CC69; the string legato leads (join medians +2..+19 ms); the c35/c39 `REATTACK_LEAD_AT` values and entry fills that landed; Flute 1's 212 join (stable on its 0.03 qn crossfade); the 268 breath with the violins' and Horn 4's slurs across it.
