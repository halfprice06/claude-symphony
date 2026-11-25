# Cycle 39, critic C: tempo, timing and transitions (on the c38 render)

Material: `cycles/c38/render` (master and 32 stems), `cycles/c38/mvt2-mockup-c38.mp3`, `cycles/c38/rendered_build/parts.json` (every qn-to-seconds conversion uses its tempo map), the c37 render and parts.json for before/after comparison, `build/score_config.py`, `build/early_fills.json`, `tools/score_to_parts.py`, `build/global.ily`, `build/mockup-events.tsv`, the May 2021 HO manual PDF pp. 143-146 (row T1 of `loop/MANUAL-READING.md`, cycle 39), `loop/MANUAL-GAPS.md`, and the c35 critic C report (the last tempo-lens report).

Methods (measured from the score onset `sq`, on the tempo map):
- Breaths: stereo-power level in 30 ms windows. The dip is the minimum in [onset - 0.6 s, onset + 0.05 s] against the mean over [onset - 1.2, onset - 0.6 s]. I also summed the wind and brass stems and the string stems into two groups.
- Entries: the same as c35. 20 ms windows with a 5 ms hop, the body at +0.4..+0.9 s, b-6 and b-3 when the stem first reaches body - 6 / - 3 dB. 129 entries after at least 0.45 s of silence.
- Joins and re-attacks: the energy at harmonics 1-4 of the note's own pitch (4096-point STFT, 5 ms hop; 8192 points below MIDI 55).
- S3: every fall of 6 dB or more within 0.35 qn in each track's `vol_db`, checked against sounding notes and against note ends in the 2 s before. The volume envelope acts after the Opus hall, so a fall there cuts the hall's ring.

## Manual notes (T1: PDF pp. 143-146)

| What the manual says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| The performance-script CC table: CC5 legato/portamento time, CC15 con sordino, CC22 mono/poly, CC36 round-robin reset, CC57 legato script, CC65 portamento script, CC69 repetitions, CC70 finger position (p.143) | Every track | Yes. CC5, CC22, CC57 and CC65 are never sent, so the patch defaults hold. CC15, CC36 (pre-roll), CC69 (pre-roll) and CC70 are sent. |
| True legato: velocity sets the transition time. About 50-60 gives a longer transition ("allowing the melody to breathe more"); 110-127 a shorter one. Velocity does not change loudness (p.144) | Every legato target. The case that matters is Violins I at qn 72 (bar 25, "tutti, con sord."): the tutti re-entry is a Leg Slur MAX target at **v63**, while Violins II play the same C5 at v124 | No, at 72. Violins I take the slow transition and land 0.33 s behind Violins II (finding 2). Elsewhere string targets are v124, and v90 for soft coda targets. |
| Con sordino on CC15, 0-63 off / 64-127 on (p.144) | Mutes on at 9.5 (Vln I/II, Vla, Vc), off at 90.5. Coda: Violas div 268.5, Vln II and Vla 273.5, Vln I 274.5, Horns 3-4 271.5 | Yes (measured in parts.json). Every CC15 change falls in a rest, 6-87 s before the next note, so no mute switch lands under a sounding note. |
| Repetition script (random detune or neighbour sample) against RR reset (consistent take order); reset by any value on CC36 (p.145) | Render-to-render repeatability | Partly. CC36 goes in the pre-roll. Timing repeats: c37 -> c38 entry b-6 median change 0.000 s, p90 0.030 s. But one join changed with identical data: Violas 266 sagged 18 dB in c38 and not at all in c37 (see "Checked"). Opus's preferences reset on CC16 (MANUAL-GAPS #10, still untried). |
| Finger position on CC70: FP1-FP4 select the string where possible; FP4 gives the warmer sound (pp.145-146) | The "sul A/D/G/C" spans | As c35 found: "sul A" is right; "sul D" sends FP4 on E♭4-F4 violin pickups and E♭3/F3 cello notes that FP4 puts on the G string. Still open; a colour issue, not a timing one. |

## Where c38 stands (measured)

- **Tempo map.** Identical to c34-c37 (402 points). Every printed tempo lands within 1-3%, as c35 listed:
  - bars 35-36: 49.2/45.0, then 60.0 at the Poco più mosso;
  - bar 47: 58.0; bar 48: 54.0; bars 49-52: 52.3-52.8 (printed 54; the phrase arcs);
  - bars 53-59: 60.0 rising to 64.0; bar 60: beats 63.0/61.0/59.0, then 47.1 on beat 4 (the caesura);
  - Largamente bars 61-63: 53.2/53.2/54.0; allargando bar 64: 50.9/46.5/43.5/40.5; Tempo I 52.0;
  - bars 78-82: 50.3, 48.7, 45.5, 45.9, 44.0; a tempo 52; bars 89-92: 48.4, 44.0, 39.9, then 36.8/35.2/20.0.
- **Final fermata.** The chord holds 6.34 s from qn 301, with CC11 falling over the last beat. Every track releases at 348.23 s.
  - Master after the release: -64.8 dB at the release, -71.3 at +0.3 s, -80.6 at +0.6 s, -99.4 at +1.0 s (c37: -63.4/-71.1/-79.2/-92.4).
  - The mp3 ends 1.57 s after the release, with the tail already at -113 dB. Nothing is cut.
- **Downbeat arrivals after the caesuras** (own-pitch b-6, s): 204: strings +0.00..+0.06, winds and brass -0.02..+0.09. 268: -0.08..+0.06 for everything except Horn 4 (+0.18; c37 +0.05).
- **Keyswitches.** 335, all before their note: minimum 19.6 ms, median 34.6 ms. No clashes.
- **S2, the gap between string and wind entries.** b-3 median: strings +0.104 s (n = 53, p90 +0.220), winds +0.019 s (n = 76). c35 measured +0.157 s for Leg Slur string entries.

## 1. The tutti breath before bar 61 (qn 204) is still heard as lost time, not as a breath. The drier hall made no gap and cut no ring (extra check; measured, the hearing judgement inferred)

Extra check: does the c38 drier hall turn the caesuras into gaps, or let a subito cut the ring? **No to both.**

**Master dips** (30 ms windows):

| breath | c37 | c38 |
|---|---|---|
| 204 | 2.0 dB | 1.7 dB |
| 196 | 1.5 dB | 1.8 dB |
| 268 | 3.1 dB | 4.0 dB |

At 268 the minimum falls at +0.03 s, so it marks the downbeat rather than a breath before it. The master never drops as far as a gap would.

**Winds and brass at 204.** Individual stems now dip 13-26 dB (c37: 10-20 dB) and stay more than 10 dB down for 0.04-0.26 s. Summed as a group they fall smoothly, about 11 dB over 0.15 s (c37: 8 dB):
- -23 dB at -0.25 s, -34 dB at -0.08 s, back to -23 dB at +0.05 s.

The fall is gradual, not a cut, so the hall still rings under it.

**Strings.** They play straight through. Their group sum *rises* into the downbeat (-18 -> -14 dB at -0.07 s), because Violins I/II, the celli and the basses join 203.88-203.92 -> 204 as led Leg BC/Leg Slur targets. The printed new bow at 204 (Vln I up-bow < then down-bow ff tenuto; basses "change bow at will") is not played.

**Lost time.** The caesura stretches beat 4 of bar 60 to 47.1 bpm (the 0.25 qn before 204 lasts 0.49 s instead of 0.26 s). `BEAT_STRETCH` 204: 0.94 then plays the downbeat at 50.8. Because nothing in the strings breathes, this 0.47 s of stretch sounds like the crescendo dragging into the climax.

**S3 scan of the envelopes.** No volume-envelope fall cuts a ring the listener can hear:
- After a note end with silence following, the only falls are on the timpani (9.45, 203.95, 210.48, 238.45). Each comes 0.2-0.9 s after the stroke or roll ends, when the tail is already 17-40 dB under the stroke (210.25-210.48: -51 -> -54 dB under a ff tutti; 238.45: below -95 dB).
- Every fall of 6 dB or more under a sounding note sits at a note boundary, as a fill release or a shape start. The bar 66 niente is in CC7 (pre-hall) and falls 7.2 dB with the ring kept, as the c38 actor measured.

**Fix (the c35 #3 test, still open):** a generic `FRESH_AT = {track: [sq]}` in `tools/score_to_parts.py`, default `{}`.
- **Mechanism.** In the SUBITO_FRESH block (around l. 2109), mark a listed note `subito_fresh` / `fresh` whatever its dynamic. The existing post-pass (around l. 2440) then undoes the legato target, gives the fresh entry lead and cuts the old note 0.03 qn before the moved onset.
- **Breath gap.** Let the note before a listed onset end `CAESURA_BREATH_QN` (0.12 qn) before it when the onset has a CAESURA, instead of the slur-break 0.05.
- **Movement II values:** `FRESH_AT = {"Violins I": [204.0], "Violins II": [204.0], "Violoncellos": [204.0], "Double basses": [204.0]}`. The violas already move to the tremolo row there.

**Pass criteria:**
- master dip in [203.75, 204.0] of 4-6 dB;
- every string b-6 at 204 within +0.06 s;
- 2-5 kHz over the first 80 ms of the string re-attacks no more than 2 dB over c38;
- limiter no higher than c38's 2.3 dB.

**If the test fails,** revert it and shorten `CAESURA[204.0]` 0.22 -> 0.10. Then the time taken matches what is heard: the winds alone breathe.

Leave 268 alone. The violins' slur runs across it as printed, and nine winds breathe 12-20 dB on their stems, which is the breath the score asks for.

## 2. Bar 25 (qn 72), "tutti, con sord.": Violins I re-enter on a slow v63 legato and land 0.33 s behind Violins II on the same C5 (measured; manual p.144)

**Where.** Violins I, C5 at sq 72. It is a Leg Slur MAX target at v63 (keyswitch 71.794), led 0.176 qn (`REATTACK_LEAD_AT` from c35). Violins II play the same C5 as a Leg BC target at v124.

**Evidence** (own-pitch b-6, c37 and c38 alike):
- Violins I: +0.385 s. Violins II: +0.050 s.
- The Violins I stem falls from -42 to -57 dB around the onset (-0.09..+0.07 s), then builds to its body (-33 dB) only by +0.7 s.

The c35 lead (0.06 -> 0.176 qn) did not move the arrival (c34 b-6 +0.245, now +0.385). The delay comes from the transition speed, not from the start time: manual p.144 says velocity 50-60 gives the long transition. c36 C saw the dip and left it because Violins II mask it in the master (within 1 dB). But the leading section of the theme's unison arrives a third of a beat late and swells in after the second violins, which blurs the downbeat of the theme's return.

**Fix.** `VEL_SET["Violins I"] = {72.0: 124}` in `build/score_config.py`: the same transition speed as Violins II. Velocity does not change loudness on a true-legato target (p.144). Keep the lead for this render.

**Check:**
- Violins I b-6 within ±0.06 s of Violins II;
- if Violins I are early by more than 0.05 s, cut `REATTACK_LEAD_AT["Violins I"][72.0]` to Violins II's 0.15 qn equivalent (about 0.17 s);
- the stem dip at 72 under 6 dB.

## 3. Coda (qn 286): the celli's pp tutti F2 reaches its level 0.25 s after the other entries on that beat (S2; measured, fill simulated)

**Where.** Violoncellos, F2 at sq 286 (bar 87, "tutti" after the 4 soli on the div track). Sus, v41, entry lead 0.12 qn. The c34 role shape already lifts the front about 4 dB.

**Evidence.** b-6 / b-3: +0.255 / +0.340 s (c37 +0.220 / +0.335). On the same beat:
- Violins II: +0.070 / +0.095
- Horn 4: -0.035 / +0.050
- Cor anglais: +0.010 / +0.055

The stem rises steadily from -61 dB at the onset to its -48 dB body at +0.45 s, so the bass of the coda chord comes in under the others and swells.

**Fix.** `build/early_fills.json` "Violoncellos": add `"286": {"db": 4, "pre_s": 0, "hold_s": 0.25}`. Simulated on the c38 stem: b-6 +0.025, b-3 +0.230, 50 ms peak +1.8 dB over the body (now +1.7), so no overshoot.

## 4. Three string entries at bar changes still reach body - 6 dB 0.12-0.14 s late (S2; measured, fills simulated)

None of these has a fill now. Simulated with the c35 fill shape (0 at onset - 0.02 s, full at the onset, held, gone 0.25 s later):

| track, sq (bar) | now b-6 / b-3 | proposed `early_fills.json` | simulated b-6 / b-3 | 50 ms peak over body |
|---|---|---|---|---|
| Double basses 184 (bar 56) | +0.128 / +0.163 | `{"db": 3, "pre_s": 0, "hold_s": 0.12}` | +0.038 / +0.128 | +1.9 (unchanged) |
| Double basses 216 (bar 64, allargando) | +0.137 / +0.172 | `{"db": 3, "pre_s": 0, "hold_s": 0.12}` | +0.042 / +0.137 | +1.5 (unchanged) |
| Violas 140 (bar 45) | +0.124 / +0.149 | `{"db": 3, "pre_s": 0, "hold_s": 0.12}` | +0.034 / +0.124 | +2.2 |

Leave the following:
- Violas 279 (+0.153): a 3 dB fill would peak +3.6 dB over the body, as c35 found.
- Violoncellos div 274 (+0.159 / +0.289): it already has a 4 dB, 0.6 s fill.

The gain is small: these are bass and inner-voice entries. Together they take the string entry median closer to the winds'.

## 5. Horn 1 at 196 and Horn 3 at 267: the attack is on time, but the note blooms 7-9 dB over 0.5 s, so the perceived attack centre sits late. More lead will not help (S2; measured, fix inferred)

c35 gave both notes `REATTACK_LEAD_AT` values (Horn 1 196: 0.10 s; Horn 3 267: 0.12 s). Their b-6 did not move:
- Horn 1 196: c34 +0.16 -> c38 +0.150 (b-3 +0.495).
- Horn 3 267: +0.165 -> +0.210 (b-3 +0.510).

The own-pitch trace shows why. The new pitch overtakes the old one at -0.06 s in both notes, so the transition is on time. Then the body grows:
- Horn 1 F♯4 (f after the bar 59 breath, Sus MAX): 25-28 dB over 0-0.3 s, then 34-36 dB by +0.6..+0.9 s.
- Horn 3 E4 (bar 80, Leg Slur MAX): 20-23 dB, a dip at +0.4 s, then 28-31 dB at +0.55..+0.75 s.

The violins at 196 (-0.03 / +0.06) and the violas at 267 (+0.00 / +0.02) reach their bodies at once, so the horn colour arrives about half a beat after the chord.

**Fix.** Level shapes, not leads (`LEVEL_SHAPES` in `build/score_config.py`, as used for Horn 1's bar 61 shape):
- Horn 1: `(195.89, 0), (195.95, 3), (196.35, 3), (196.9, 0)`.
- Horn 3: `(266.9, 0), (266.95, 3), (267.4, 3), (267.75, 0)`.

Check on a stem simulation before writing:
- b-3 within +0.25 s;
- the 50 ms peak in the first 0.6 s no more than 2 dB over the body;
- Horn 1 must not rise over the violins' f melody at 196-197 (c38: Horn 1 2.4 dB under Violins I at 186).

## 6. Bar 60 into 61: the strings' crescendo reaches its top 0.07 s before the caesura (measured; low priority, follows from finding 1)

The string group peaks at -14 dB at 203.93 (-0.07 s) and then falls 5 dB (-19 dB at -0.01 s) just as the winds come back. The ff downbeat is therefore weaker in the strings than the beat before it.

The cause is the led legato targets. Their moved onsets (203.877-203.918) put the transition sag on the downbeat itself.

If finding 1's fresh strokes are rendered, this goes away (the strokes re-attack at 204 with the entry lead). If the test is reverted, keep the legato and add join fills of 3 dB held 0.1 s on Violins I/II at 204 (`early_fills.json` keys "204") so that the downbeat is not the low point.

## Checked and fine (measured unless marked)

- **Tempo spans.** `RAMP_SPANS`, `PHRASE_ARCS`, `TEMPO_PUSH`, `BEAT_STRETCH` and `CAESURA` land the printed marks (above). The Poco più mosso, Largamente, Tempo I and a tempo changes are clean steps on their downbeats (45.0 -> 60.0 at 108, 40.5 -> 52.0 at 220, 43.3 -> 52.0 at 274).
- **qn 196 (bar 59).** Fl1, Ob1 and BCl breathe 10-23 dB on their stems. The violins dip 5 dB and re-enter on time (b-6 -0.03/-0.02). There is no CAESURA here, which is right.
- **c35 re-attack leads that worked:**
  - Violins I 249: +0.215 -> -0.045 (Violins II -0.090);
  - Horn 1 208/210: -0.180 / +0.045;
  - Oboe 1 210: +0.260 -> +0.020;
  - Violins II 218: +0.325 -> +0.070;
  - Clarinet 2 256: +0.105;
  - Flute 1 116: +0.130 (b-3 +0.435 -> +0.165).
- **Bassoon 1 144.** The crossover is on time (-0.06). Its body steps up 7 dB at +0.26 s (a sample shape); with the celli on time it is a small colour lag. No action.
- **Violas 266.** With identical MIDI and envelope, the F4 join sagged 18 dB in c38 (b-3 +0.32) and not at all in c37 (b-3 -0.025). It is a take or transition variation, not a timing rule, so do not fill it on one render. It is a reason to try the CC16 round-robin reset (MANUAL-GAPS #10) in a cycle that refits shapes anyway.
- **Mute switches and keyswitches.** Every con sordino switch falls in a rest; every keyswitch is 19.6 ms or more before its note.
- **The final fermata.** The tempo (36/36/20), the CC11 morendo, the joint release, and the tail decaying with no cut in the master and the mp3.

Do not touch: the tempo map (`RAMP_SPANS`, `PHRASE_ARCS`, `TEMPO_PUSH`, `BEAT_STRETCH`, `CAESURA` at 268 and the solo seams); the final bar, its CC11 fade and the joint release; keyswitch placement and the pre-roll CC36/CC69; the c35 `REATTACK_LEAD_AT` values that landed (listed above); the c31 entry fills and leads; `ABUT_LEAD force_at` 152/204; `GROUP_LEAD_AT` on the bar 79 run; the 268 breath with the violins' slur across it; the bar 66 niente in CC7; fx_volume 0.095 and the 160 Hz hall low cut (the caesuras did not become gaps under them).
