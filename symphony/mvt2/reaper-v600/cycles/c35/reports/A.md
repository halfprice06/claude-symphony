# Cycle 35, critic A: articulation and phrasing (on the c34 render)

Sources: `cycles/c34/render/` stems and master (and c33's for comparison), `cycles/c34/rendered_build/parts.json`, `build/mockup-events.tsv`, `build/score_config.py`, `build/*.json`, score pages 1-5 and 8, the May 2021 HO manual pp. 89-94 (group A1) and `loop/MANUAL-GAPS.md`. Levels are stem or master RMS in dBFS unless stated. Times are in score qn (bar/qn map in BRIEF). Scripts and scratch files were in `/private/tmp/claude-501/mockup-loop/mvt2-c35-A/` and have been deleted.

## Manual notes (A1, PDF pp. 89-94)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| DIV A / DIV B are the left or right chair of each stand, Close mics only; "the loudness of a divisi part is not much less than if the whole section were playing" (p.89) | Violin I solo (DIV A, bars 17-22), Violins II div (DIV B, bars 37-40), Violas div (DIV B), Violoncellos div (DIV A, bars 18, 21-22 and the coda 4 soli 274-286) | Yes: div tracks carry the divided voices, with gains set by measurement. The Double basses' 4 soli (bars 65-70, 87-92) still play on the full section at -3 dB, although `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` is installed (finding 5). |
| Mix the divisi Close mics with the non-divisi mics of the same articulation for the other mic positions (p.90) | all div tracks | Partly. The div tracks get a larger hall send (0.5-0.8) instead of a second, non-divisi instance. That is acceptable under the memory cap. |
| Détaché: no legato connection, a defined end, cannot be held (p.91) | violas' sotto voce portato eighths, bars 48-51 (152.5-167.5) | Yes. All 15 notes are on Detache, 0.54-0.65 s long. Peaks sit within 1.9 dB of each other (-45.7 to -47.6), and the rests drop 26-35 dB (measured). |
| Sustains are looped (p.91) | every string note over 4.5 s | Yes. On every long string hold the 100-300 Hz band autocorrelation at 3.95 s is 0.17 or less (opening chord, Cb 220-238, Vc div 274-286, Cb 271-286, final chord on every section; master final chord 0.07 max, folded swing 3.4 dB). The one exception is Cb bars 2-3 (0.67 at 4.1 s), where the period matches its own re-bow spacing over a 6.5 s span. |
| Sustain round robin alternates up and down bow; finger position on every section except the Basses; three vibrato levels (p.91) | re-bows; CC70 "sul" spans; Cb "sul A" bar 65 | Yes. Re-bows take the next round robin. The Basses get no CC70, which is correct because they have no finger-position samples. |
| Flautando: 2nd Violins only, with no finger position, no vibrato control and no round robin (p.92) | Violins II div. sul tasto, bars 37-40 | Yes for the patch. Because Flautando has no round robin, each same-pitch re-bow (div 110.05, 113.7, 116.1, 119.9; section 111.2) replays the same attack. The dips are 3.4-6.8 dB (100 ms) on the div stem, the section stem has a 6-7 dB trough at 115.25-115.5, and the master dips are 0.5-4.9 dB (measured). Small. |
| Pizzicato RRx4 or RRx2 (p.92) | violas pizz. bars 41-44 (42 notes), Cb pizz. bars 37-44 (22 notes), Cb sf pizz. 212 | Yes. All are on Pizz RRx4. The median -6 dB point falls at +0.018 s (violas) and +0.021 s (basses). Basses decay 13 dB by +0.3 s. See finding 4 for the bar 41 shape. |
| Staccato / Stac On Bow / Spiccato / Shorts MOD SPEED (pp.93-94) | none (v600 has no string shorts) | n/a |
| Repetitions patch: bow changes, release trails, no round robin (p.94); MANUAL-GAPS #2 | same-pitch repeats (S1) | Not used and not needed now. 54 of the 59 untied same-pitch repeats dip 3 dB or more on their stems. The 5 that do not are Cb 168 and 144, Violas 62 (merged) and Violins II 289/292 (coda re-bows) (measured). |
| MANUAL-GAPS #8 (4 soli on half-section patches) | Cb 220-238 and 286-304 | Not tried (finding 5). |

## Findings, ranked by what a listener hears

### 1. Bar 63: the strings' "trem. sf" has no accent in Violins I and the celli, and c34 made it worse (measured)

**Where.** Violins I, Violins II, Violas and Violoncellos, qn 211.2-212.5 (end of bar 62 into the bar 63 sf tremolo). The score prints "trem. sf" followed by a decrescendo to p in bar 64.

**What is wrong.** The sf should be the loudest moment of each string part. Instead, Violins I and the celli enter the tremolo softer than the bar 62 tenuto chord they leave, and a 3-4 dB release dip sits just before the sf.

| stem | 211.2-211.8 | 212.0-212.3 (sf) | sf minus pre, c34 | same, c33 |
|---|---|---|---|---|
| Violins I | -22.5 | -26.2 | **-3.7** | -0.6 |
| Violins II | -26.9 | -21.5 | +5.3 | +8.1 |
| Violas | -27.6 | -24.8 | +2.8 | +2.8 |
| Violoncellos | -23.7 | -25.4 | **-1.7** | +1.5 |
| Master | -15.6 | -16.5 | -0.9 | +0.3 |

At 20 ms resolution, Violins I goes -22 (at -0.4 s), down to -29/-30 around the onset, then -25/-26 from +0.07 s. The celli go -20, then -29, then -22..-25. Violins II peaks only at +0.17 s (-18), 4.7 dB over Violins I, so the sf is led by the inner violin part.

**Cause.**
- c34's climax hold (`build/score_config.py` lines 657-659: +3 dB on Violins I/II and +3.5 dB on the celli, held to 211.6 and released by 211.9) raised the last beat of bar 62 by about 3 dB.
- The c31 bar 63 CC7 lane (`_C31_BAR63["Violins I"]["cc7"]`) starts Violins I at CC7 84/94 at 212.0/212.025, which is -3.6 and -2.6 dB for the first 70 ms of the sf. The lane was computed from c31's envelope, before the c34 hold existed.
- The 2-5 kHz content in the master is level with bar 62 (37.2 at 212.125 against 37.0 at 211.25, relative units), so the sf adds no brightness either.

**Fix.**
- (a) In the c34 block, end the hold earlier on Violins I and the celli: `(211.0, 3.0), (211.5, 0.0)` in place of `(211.6, 3.0), (211.9, 0.0)`. Violins II can keep its hold.
- (b) In `_C31_BAR63["Violins I"]["cc7"]`, set 212.0, 212.025 and 212.063 to 127, 127 and 118 (no dip at the head of the sf), and recompute the four lanes with `cycles/c31/a2cc7.py` after (a). That file's comment says to recompute whenever these shapes change.
- (c) Add an sf weight in `LEVEL_SHAPES`: Violins I and Violoncellos `[(211.98, 0.0), (212.02, 2.5), (212.15, 2.5), (212.5, 0.0)]`. The release then runs alongside the existing CC7 fall, so it is not a fast fall in the envelope alone (S3).
- Targets on a stem_fix simulation:
  - Violins I and the celli at 212.0-212.3 are 2-3 dB over their own 211.2-211.8 level.
  - Violins II is no more than 2 dB over Violins I in that window.
  - The master 2-5 kHz jump at 212.0 stays under +3 dB.
  - Trombone 1's entry (moved onset 212.40) is unchanged, because everything above is back to 0 by 212.5.

### 2. Bass clarinet pedal, bars 3-6: the c34 split did not reduce the 500-1000 Hz cycle and added a 6-7 dB level step at qn 10 (extra check; measured)

**Re-measurement (critic C's stated method).** The 500-1000 Hz band level in 50 ms frames, detrended over 2 s, on qn 6.5-16.8:

| | autocorrelation, best lag in 3.5-4.5 s | folded swing | p10-p90 of the detrended level | centroid autocorrelation (3.5-4.5 s) |
|---|---|---|---|---|
| c33 (one note) | 0.41 at 4.45 s | 3.7 dB | 3.8 dB | 0.52 at 3.85 s |
| c34 (three pieces, 6 / 10 / 13.5) | 0.32 at 4.00 s | 4.4 dB | 4.8 dB | 0.12 |

- With 100, 200 and 400 ms frames, or with linear detrending, c33 reads 0.14-0.43. **C's 0.94 does not reproduce by any variant I tried.** The c34 actor's 0.32/0.44 is in the same range as mine.
- c34's remaining 0.32 sits at 4.0 s, which is the piece length (4.6 s, 4.0 s, 4.0 s), not the sample loop.
- So the 4.4 s cycle (weak by this measure even in c33) is gone, but the swing in the band did not get smaller. **Verdict: not fixed as intended.** The colour cycle was replaced by re-attack steps.

**What a listener hears (measured).** Stem level per half qn, relative to the 6.4-7.6 mean:
- c34: +2.7..+3.1 dB at 8.5-10.0, then **-3.2..-4.8 dB at 10.0-12.5**, then +1.3 at 13.0-13.5, then -2.0 at 13.5-14.0, then about 0 from 14.5.
- So there is a 6-7.5 dB step down at the qn 10 re-tongue, lasting about 2.6 s, and a 3.3 dB step at 13.5.
- Each new piece also starts brighter: the 500-1000 Hz share rises from -18.8 to -13.2 dB at 10.25, and the centroid from about 200 to 285 Hz.
- In the master, bars 4-5 are 1.1-1.6 dB softer than c33, and the chord's 80-200 Hz band (the A flat 2 fundamental) is 4-5.5 dB weaker over qn 12-14.5.

**Cause.** The c28 roles in `roles.json` `Bass clarinet` (`[8,9,-1], [9,13,-7], [13,14,-5], [14,16.75,-3]`) were fitted to the single note's sample swell (the A flat 2 sample rises about 7.5 dB from 7.75 to 9.5). Since c34 they sit on fresh pieces that start without the swell. The pieces abut with a 0.03 qn gap, so no breath is audible, only the new attack.

**Fix.**
- In `roles.json` `Bass clarinet`, replace the four roles with `[8,8.5,-1], [8.5,9,-4], [9,10,-9.5], [10,12.5,-3], [12.5,13,-5.5], [13,13.5,-6], [13.5,14,-3], [14,16.75,-3]`. Use short ramps (about 0.05 qn) at 10.0 and 13.5 so each change lands with the new piece. Keep the other roles.
- Simulate with `tools/stem_fix.py`. Target: every half qn from 6.5 to 16.5 within ±1.5 dB of the 6.4-7.6 level, and no step over 2 dB at 10.0 or 13.5.
- Optionally (inferred), play the two new pieces at v41 like the first instead of v45, to soften their brighter attack. Measure the 500-1000 Hz share at +0.3 s against the first piece.
- If the actor would rather have fewer joins, one split at 11.6 (C's original suggestion) with the same refit is the alternative. Its pieces of about 5.5 s would each hold one 4.4 s colour cycle, but the cycle would not repeat in step.

### 3. Violins II, bar 61: the 206 bow-change join sags 7-8 dB and arrives about 0.3 s late in the ff molto sostenuto (measured)

**Where.** Violins II, qn 205.775 (moved onset) into 206: G sharp 4 to C sharp 5 (MIDI 68 to 73), Leg BC MAX, v108.

**Evidence.**
- At 20 ms resolution the stem is -22 dB before the join, -27..-30 from -0.11 to +0.19 s, then -18..-20 from +0.23 to +0.43 s (4 dB over the old body).
- The join scan gives a -10.1 dB dip against the louder neighbour.
- It produces the deepest master dip of the bar 61-62 tenuto changes: -3.4 dB at 206, against -1.8 at 208 and -2.5 at 210.
- At the same moment Violins I re-bows on Sus MAX (205.949) with a 100 ms dip of only 1.3 dB.
- There is no early fill on Violins II 206; the 204 fill exists.

**Fix.**
- `build/early_fills.json` `Violins II` `"206": {"db": 5, "pre_s": 0.1, "hold_s": 0.15}`. It must be gone by about +0.4 s, because the note blooms 4 dB over its body at +0.33 s.
- Check the 30 ms peak for a transition spike before keeping it (LEARNINGS §6).
- If the fill overshoots, the alternative is the Violins I treatment: `ABUT_LEAD`/Sus MAX for this one join.
- Target: dip under 4 dB, and the new pitch within 3 dB of its body by +0.15 s (S2).

### 4. Violas pizz., bar 41: the printed pp crescendo plays as a +9 dB step on beat 3 (measured)

**Where.** Violas, qn 124-128 (pizz. triplets, pp with a crescendo hairpin to p at bar 42).

**Evidence.** Peaks per note:
- Beats 1-2 (124-125.67): -53.0, -51.3, -45.9, -51.2, -52.3, -50.9.
- Beats 3-4 (126-127.67): -41.1, -46.2, -41.2, -42.3, -41.7, -40.4.
- Bar 42 (the p arrival): -37.2 to -43.8.

So the whole crescendo happens at 126.0, and the goal bar is only about 2 dB over beats 3-4. The volume envelope jumps from -3.6 dB (125.67) to +5.8 dB (126.0). That jump comes from the role `[123.6, 125.95, -4, 0.3]` ending, plus the pizz. pitch trim 54: +4 and the downbeat metric step. Per pitch, after the envelope, MIDI 54/58 still sit about 5 dB under 56/61, so the pitch trims are in the right direction and should stay.

**Fix.**
- In `roles.json` `Violas`, make the bar 41 role a ramp across the bar: replace `[123.6, 125.95, -4, 0.3]` with `[123.6, 127.9, -4, 2.0]`, if the 4th field is the release length. Otherwise use a `LEVEL_SHAPES` entry `[(123.6,-4),(124.0,-4),(127.9,0)]`.
- Target: mean peak per beat rising monotonically over bar 41 (roughly -52, -49, -46, -43), with bar 42 2-3 dB over beat 4.
- The same check applies to the decrescendo role `[133.95, 138.2, -4, 0.5]` (bars 43-44). It now steps from -44 (133.67) to -52.8 (134.33).

### 5. The Double basses' "4 soli" pedals play on the full section; the manual's half-section patch is installed (inferred; MANUAL-GAPS #8)

**Where.** Double basses, qn 220-238 (bars 65-70, "4 soli, sul A, change bow at will", pp under Horn 1's solo) and 286-304 (bars 87-92, "4 soli", pp into the ppp final chord).

**Evidence.**
- Manual p.89: a DIV part is one chair of each stand. A half section is the nearest the library comes to four players.
- `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` is on the drive (checked).
- Now `SOLI_AS_META` plays the full section 3 dB down. The celli's 4 soli (274-286) already moved to their DIV A track in c33, so the two 4 soli passages now differ in kind.
- The full-section pedal also carries the remaining re-bow unevenness (measured):
  - In 220-238 the stem swings -51.7 to -59.6 in half-qn bins.
  - Re-bow 221.8 has a 5 dB hole from -0.25 to +0.2 s, and 225.215 steps -4.9 dB.
  - The 273.229 piece still swings about 10 dB (open since c34).

**Fix.**
- A "Double basses soli" track on `Basses KS Master DIV A.oib` (Close only, the c13 pan-centring applies), routed by `TRACK_WINDOWS` for 220-238 and 286-304, with `META_SKIP_TRACKS` so the -3 dB metà cut is not applied. Use Sus MAX rows only, a hall send of 0.5 like the other DIV tracks, and gain set from one render.
- Memory: one Close-only instance is about 0.7 GiB (M1 c35) against c34's 44 GB settled, so the actor must check the cap. If it does not fit, render this track in a second pass (MANUAL-GAPS memory plan, p.222).
- The re-bow fits for these spans would have to be redone on the new track (`fit_rebows.py --window`).
- This is inferred: the gain is a thinner, less blended tone under the horn solo and in the coda, which I cannot measure before it exists.

### 6. Timpani, bar 53: the p stroke at 172 barely stands out from the crescendo roll into it (measured)

**Where.** Timpani, the roll at 168 (pp <) into the stroke at 172 (p, Timpani Flt Lng, v72), then "damp" at 173.

**Evidence.**
- The roll reaches -41..-43 over its last 0.3 s. The stroke peaks at -40 at +0.07 s and is back to -45 by +0.15 s, so it stands +1..+2 dB over the roll's end.
- The other roll-to-stroke arrivals stand +11 dB (203, f) and +7 dB (209.5).
- The stroke marks the a tempo of bar 53 and the start of the violins' theme.

**Fix.** Use a role `Timpani [171.98, 172.5, 3]`, which is a step at full value on the stroke (LEARNINGS §10), or raise the stroke velocity from 72 to 78. Do not use `note_trims`: it ramps in over 0.6 s and would lift the ring, not the stroke. Target: stroke peak 4-6 dB over the roll's last half beat, still under the strings' bar 53 entry.

## Checked and fine (measured unless stated)

- **Legato patches never get chords.** No overlapping notes over 0.2 qn and no simultaneous onsets on any Leg row.
- **Joins in the master are small.** 638 legato joins were measured. 25 dip 6 dB or more on the stems (worst: Violins II 70 -10.1, Violins I+II 79.5 -7.8/-8.0 together, Bassoons 1+2 256/261 -7.6..-8.7), but every one of them is 2.8 dB or less in the master.
- **Keyswitches are correct.** Every printed pizz./arco/trem./sul tasto lands on its row, and ties are never re-attacked except the timpani roll-end strokes, which are by design.
- **Mutes are placed right.** CC15 on and off points match every con sord./senza sord. mark, the solo and div tracks are right, and the celli and basses stay unmuted in the coda. Horns 3-4 mute EQ from 278.
- **Breath marks are all audible.** All 44 printed wind and brass breaths dip 4-30 dB on their stems.
- **Bars 61-62 tenutos are connected.** Master dips at the half-note changes are 1.8-3.4 dB.
- **Harp rolls** go from the bottom up at 40 ms (30 ms at f).
- **Bar 66 niente** steps (-6..-7 dB) follow the printed decrescendo.

**Do not touch:**
- Trombone 1's quotation (2-5 kHz attack 4-14 dB under its body on every note; master 2-5 kHz jumps -1.7..-4.5 dB; the 213 accent 2.5-5 dB over its neighbours, 218 1.4-2.5 dB).
- The string re-bow layout and fits on the final chord, bar 66 and the opening chord (no loop pulse anywhere; final-chord master swing 3.4 dB).
- The violas' Detache portato and its CC7 levels.
- The pizz. rows and their timing.
- The Flautando sul tasto pad.
- Every breath-mark gap.
- The coda mute points.
