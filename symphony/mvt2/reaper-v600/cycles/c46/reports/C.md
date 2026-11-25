# Cycle 46, critic C: tempo, timing and transitions (on the c45 render; ONE_TIME c46 rubato)

Method. I copied `build/` and `tools/score_to_parts.py` to a scratch folder and ran the real pipeline on the copies. Run with the current config, it reproduces `build/parts.json` exactly (all 32 tracks and the 402-point tempo map). I then ran critic C's c44 plan and my tuned version through the same pipeline and compared the parts.json files. For each version I compared lead seconds per note, keyswitch lists, keyswitch lead times, re-bow points, printed-breath gaps in seconds, silent gaps at every breath, and volume-envelope falls inside release tails.

Tempo statistics use real beat durations (60 / beat length, so caesuras count). Each beat is compared with a 17-beat moving median, as in `rubato.py`. The same code was run on the reference maps:
- Duc's Adagietto MIDI;
- Mulan and Howl's, converted with `cpr2mid.py` from the .cpr files in `mockup-reference-cn1rc0/mockup-kit/reference/cubase-vsl/`.

`rubato.py` itself gives the FINDINGS figures: Duc 8.0 % / 23.4 % / 49 / 20; Mulan and Howl's 20 % and 19 % of beats with a change. All judgements on the c45 render come from its stems and `metrics/attacks.txt`; the new map's effects are simulated.

## Manual notes (D2: May 2021 HO manual PDF pp. 101-102, read in full; `loop/MANUAL-GAPS.md` read)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 101 | Long articulations "can be held indefinitely; this is achieved by looping the samples". | The rubato lengthens the long held notes:<br>- Contrabassoon qn 87: 12.6 -> 13.2 s<br>- Bassoon 2 qn 90: 11.5 -> 11.7 s<br>- Contrabassoon qn 98: 10.9 -> 11.1 s<br>- Horn 1 qn 232: 7.3 -> 7.7 s<br>- Horn 4 qn 84: 7.2 -> 7.6 s<br>- Timpani roll qn 226: 13.5 -> 13.9 s | The strings are re-bowed (all pieces stay at 4.94 s or less after the pins in finding 3). Winds, horns and timpani are not re-bowed. Re-check them for 3.95 s loop pulsing after c46 (BRIEF item 8). |
| 101 | Sustain dynamics are on the Mod Wheel (CC1). All four layers play and CC1 crossfades them, "to create a realistic crescendo and/or decrescendo during a held note". | The hairpin curve shapes (finding 4) must bend the lane that carries the dynamics on each track: CC1 on `CC1_DYN_TRACKS` (horns, trombones, tuba, clarinets), CC11 elsewhere. | Yes. Both lanes come from `base_points`, so one curve reaches both. |
| 101 | Sustain Accent: velocity sets the attack, CC1 the body. Marcato Long/Short: velocity opens a low-pass on the marcato attack. | Trombone 1 qn 213 and 218. | Not changed here. Trombone 1 still plays the sustain with a swell (rule 9). |
| 101 | Portato: each note held nearly full length without a tie. | Viola portato eighths, qn 152.5-167.5. `CAESURA[164]` (cor anglais breath) goes from 0.10 to 0.20 s. | The 163.5 eighth's gap grows by 0.1 s while the cor anglais breathes, as an accompaniment following a soloist's breath would. Accepted. |
| 102 | Short notes have no release trails: "hold the last note of the phrase long enough to let the reverberation of that last note ring". | Pizzicato basses, viola triplets and harp before the breaths at 116 and 124. | Yes. No breath leaves the orchestra silent (finding 6), and the Spaces returns carry the room. |
| 101 | Legato Repetitions (MANUAL-GAPS #2). | Same-pitch restarts at qn 96 (bass clarinet) and 148 (Oboe 1). | The new caesuras there widen the gap. This helps S1. The rows themselves are still untried. |

## 1. Final rubato values: the c44 plan holds up against the references; deepen the section cadences and add the bar 30 close (measured on the simulated map)

**Where.** The a-tempo stretches: qn 17-102, 108-172, 220-259 and 274-292. The printed ramps and the bar 61-64 climax are unchanged.

**What is wrong in c45 (measured).**
- Beat deviation is a median 1.5 %. No beat is more than 25 % slower than the local tempo.
- The deepest breath is -22 %.
- The slow beats fall on the pickups instead of before them (c44 C #1).

**Re-measured against the references.**

| | median abs. dev. | 90th pct | beats >15 % slower | beats >25 % slower | breath depth, median (local minima under -12 %) | beat before a breath | beats with a change |
|---|---|---|---|---|---|---|---|
| Duc, Adagietto (403 beats) | 8.0 % | 23.4 % | 49 | 20 | -20 % (deepest 20: -23 to -52 %) | -1 % on average; -17 to -33 % before the deep ones | 98 % |
| Mulan (645) | 0.0 % | 8.1 % | 12 | 3 | -17 % | -13 % | 34 % |
| Howl's (734) | 0.0 % | 5.0 % | 25 | 6 | -24 % | -14 % | 20 % |
| c45 | 1.5 % | 6.1 % | 6 | 0 | -15 % | -5 % | 57 % |
| c44 plan | 3.0 % | 9.3 % | 15 | 8 | -24 % | -7 % | 79 % |
| **final (below)** | **3.0 %** | **9.5 %** | **14** | **9** | **-25 %** | **-7 %; -8 to -14 % at section ends** | 79 % |

What the reference maps add to the plan (measured):

- **Breath depth.** The plan's breaths, at -24 % median, sit between Mulan (-17 %) and Howl's (-24 %), and a little deeper than Duc's median (-20 %). That is the depth to keep.
- **Section ends.** Duc's 20 deepest breaths are two-beat broadenings: about -20 % on the beat before, then -30 to -50 %. In the plan, the A section's full close (bar 30, beat 89) is the shallowest section end, at -20 % with -11 % before it. It is shallower than the sub-phrase breaths at beats 28, 41 and 65 (-27 to -29 %), because no caesura sits at qn 90.
- **Beat 4 is not a general rule.** Duc's beat 4 averages -6.6 %, but without its breaths it is +3.0 %. The whole effect is breaths that fall on beat 4: 29 of his 52 breaths. So no generic last-beat stretch. The plan's -3.5 % on beat 4 (bars 37-64) comes from its breaths, which is right.
- **No limping alternation.** The plan's ±4 % duration contrast does not produce one. Lag-1 correlation of the beat deviations is +0.28, close to Duc's +0.19 (an alternating map would give a negative value). The median beat-to-beat change is 4.0 % (Duc 10.6 %, which includes tapping noise; the film maps 0 %). Keep ±4 %.
- **Median deviation of 3 %.** This is still under Duc's 8 %. Duc's non-breath beats alone deviate a median 6.4 % (SD 11 %). That is beat-level irregularity from following a recording, which no score mark here supports. The two film maps sit at 0 %. I would not raise it by rule before Dan has heard c46.

**Fix (`build/score_config.py` c46 block; tool step a as in c44 C #1a).**

Tool step a. In `tools/score_to_parts.py`, lines 1166-1167 (PHRASE_*) and 1237 (APEX_AGOGIC) must read `globals().get(name, default)`. As written, the tool overwrites any config value. My simulation used exactly this change.

Config values:

```
PHRASE_PUSH = 1.03; PHRASE_SLOW = (0.93, 0.84); PHRASE_SLOW_SUB = (0.97, 0.90)
PHRASE_SLOW_MAIN = (0.88, 0.80)          # plan 0.91 -> 0.88: Duc's two-beat section end
PHRASE_RETURN = 0.98; APEX_AGOGIC = 0.93
PHRASE_ARCS = [(18, 29), (29, 42, "main"), (48, 54, "sub"), (60, 66, "main"), (66, 77), (77, 90, "main"),
               (108, 116, "sub"), (116, 124), (124, 139), (139, 148, "sub"), (152, 160, "sub"), (160, 168),
               (220, 226, "sub"), (226, 237, "main"), (237, 249), (274, 286)]
APEX_LEAD[116] = "Flute 1"
CAESURA = {29.0: 0.22, 42.0: 0.18, 48.0: 0.15, 54.0: 0.10, 60.0: 0.10, 66.0: 0.20, 77.0: 0.15, 90.0: 0.15,
           96.0: 0.15, 102.0: 0.15, 116.0: 0.10, 124.0: 0.22, 139.0: 0.15, 148.0: 0.10, 164.0: 0.20, 171.0: 0.10,
           188.0: 0.12, 196.0: 0.08, 204.0: 0.10, 237.0: 0.18, 249.0: 0.15, 259.0: 0.10, 268.0: 0.15, 286.0: 0.20}
BEAT_STRETCH = {17: 1.04, 18: 0.97, 24: 0.96, 29: 1.04, 30: 0.97, 37: 1.04, 38: 1.04, 39: 0.96, 42: 0.96, 45: 0.96,
  48: 1.04, 51: 0.96, 55: 1.04, 57: 0.96, 60: 1.04, 63: 0.96, 66: 0.96, 72: 0.96, 77: 1.04, 78: 0.97, 85: 1.04,
  86: 1.04, 87: 0.96, 91: 1.04, 92: 1.04, 93: 0.96, 97: 0.96, 99: 0.96, 108: 0.96, 113: 1.04, 121: 1.04, 126: 0.96,
  131: 1.04, 132: 0.96, 136: 0.96, 140: 0.97, 145: 1.04, 147: 0.97, 148: 0.96, 152: 0.96, 155: 1.04, 160: 0.96,
  164: 0.96, 168: 0.96, 204: 0.94, 208: 0.94, 226: 0.96, 232: 0.96, 237: 1.04, 238: 0.97, 244: 0.96, 249: 1.04,
  250: 0.97, 257: 1.04, 280: 0.96, 283: 0.96, 286: 0.96, 289: 0.96}
```

Changes from the c44 plan:
- **`PHRASE_SLOW_MAIN` 0.91 -> 0.88.** The four section ends (beats 41, 65, 89, 236) now take -8 to -14 % on the beat before their -27 to -29 % breath.
- **`CAESURA[90]` 0.15 added.** The bar 30 full close rises from -20 % to -28 %. The strings' chord is held a little longer and released at 90 over the bassoon/contrabassoon pedal. No volume-envelope fall sits in those tails (finding 6).
- **`CAESURA[268]` stays 0.15 (plan 0.22).** Violas, celli, horns, Bassoon 1 and Clarinet 2 hold through it, and the violins are legato through it. This is c39's reason for 204 (a stretch under a sustained tutti sounds like dragging). 0.15 already gives -12 % inside the poco allargando.
- **`CAESURA[265]` dropped.** The plan had 0.12. See finding 2.

**Result.**
- **Length.** 353.3 s to qn 304, against 348.1 s in c45 (+5.2 s). The delivered file should be about 354.7 s (c45: 349.50 s).
- **By section.**
  - A, qn 18-42: 28.19 -> 28.70 s.
  - B, qn 108-152: 44.41 -> 45.60 s.
  - A', qn 238-274: 43.39 -> 43.87 s.
  - The climax, qn 204-220, is unchanged at 18.81 s.
- **The 14 beats more than 15 % under the local tempo.**
  - The phrase-end breaths: beats 28, 41, 53, 65, 76, 89, 115, 123, 138, 147, 236 and 248.
  - The printed rit. at 218-219.
  - Beat 285 is a breath too, at -27 %, and the final beat 303 is the printed 20 bpm fermata.
- **Pickups.** The pickups at 29, 77, 139, 237 and 249 run at about -2 %, against -8 to -14 % in c45.
- `TEMPO_PUSH`, `RAMP_SPANS`, the animando and the Largamente are unchanged.

## 2. Three of the plan's new caesuras shorten the printed breath they were meant to lengthen, and one stretches a held tutti (measured)

**Where.** Breaths at qn 196 (bass clarinet, Horn 1), 259 (Bassoon 1) and 265 (Bassoon 1).

**What is wrong.** The breath-gap code (`tools/score_to_parts.py` line 2448) cuts a wind or brass breath to `CAESURA_BREATH_QN` = 0.12 qn wherever a CAESURA exists. Otherwise the cut is 0.3 qn. The rule was written for 204 and 268, where the caesura gives the pause. Where the plan's caesura is small, the 0.18 qn lost costs more time than the caesura adds.

**Evidence (simulated gap from the note end to the next onset, c45 -> c44 plan).**
- **qn 196:** Horn 1 0.137 -> 0.052 s (no breath left); bass clarinet 0.284 -> 0.152 s.
- **qn 259:** Bassoon 1 0.338 -> 0.183 s.
- **qn 265:** Bassoon 1 0.374 -> 0.207 s.
- **What else happens at 265.** Clarinet 1, cor anglais, both flutes, both oboes, the violas and both violin sections are sustaining across the beat. Only the bassoon and horns breathe, so the stretch would drag the held chord (c39's 204 case).
- **The other new caesuras widen their breaths:**
  - 29: Horn 1 and bass clarinet 0.42 -> 0.56 s.
  - 102: bass clarinet 0.23 -> 0.35 s; Bassoon 1 0.29 -> 0.44 s.
  - 164: cor anglais 0.30 -> 0.38 s.
  - 188: Horn 1 0.24 -> 0.36 s.
  - 286: Clarinet 1 0.41 -> 0.54 s.

**Fix.**
- **Tool.** In `tools/score_to_parts.py` line 2448, add a new generic option that defaults to empty, so other movements do not change:
  `gap_ = CAESURA_BREATH_QN if any(abs(e0 - c_) < 0.01 and c_ not in globals().get("CAESURA_FULL_BREATH", ()) for c_ in CAESURA) else 0.3`
- **Config.** `CAESURA_FULL_BREATH = {196.0, 259.0}`, and no `CAESURA[265]`.
- **Result (simulated).**
  - 196: Horn 1 0.217 s, bass clarinet 0.364 s.
  - 259: Bassoon 1 0.438 s.
  - Every printed breath is now as long as in c45 or longer. The two exceptions are a few hundredths of a second shorter on the tempo-return beat: Bassoon 2 at 30 (0.314 -> 0.283 s) and at 238 (0.328 -> 0.283 s).
  - 204 and 268 keep their c45 gaps (0.136 s and 0.226 s), which is c19's decision.

## 3. Pipeline checks for the new map: S2 holds, but 20 fitted re-bow fills come loose unless the c45 points are pinned (measured)

**S2: leads and keyswitches.**
- **Leads.** Every note's lead in seconds (score time minus moved time, each on its own map) is the same as in c45 to within 12 ms, except three notes:
  - Violins II 119: 0.450 -> 0.437 s.
  - Violas 111: 0.257 -> 0.269 s.
  - Violas 249.5: 0.282 -> 0.250 s. The legato cap is a share of the previous note in qn, and beat 249 is now x1.04.
- **Keyswitch lists.** They are identical on all 32 tracks, so the Sus/Leg choices on `TEMPO_NC` did not change (c44 trap 2).
- **Keyswitch lead times.** The shortest shrink only a little: Violins II 0.070 -> 0.051 s, Violas and celli 0.066 -> 0.057 s, Bassoon 2 0.079 -> 0.068 s.
- **Probe.** `probe_attacks.py` reads the parts.json map, so the attack probe should stay at 0 (inferred). After the render, check Violas 249.5 with pcX: if it lands more than 30 ms late, add `LEG_CAP_FRAC["Violas"] += [(249.0, 250.0, 0.55)]`.

**Re-bows (c44 trap 1).** The c44 plan run on the pipeline prints 20 `REBOW_FILLS ... has no re-bow` warnings, because the automatic points are placed in seconds and move. They are:
- Violins I 264.417;
- Violins II 165.86 and 263.921;
- Violas 169.5 and 263.414;
- celli 153.366 and 165.293;
- basses 170.003, 221.8, 225.215, 227.775, 230.393, 233.038 and 235.659;
- Violoncellos div 275.527, 277.599, 279.67, 281.716 and 284.141;
- Violas div 280.439.

These include the c41/c43 basses pedal fills and the Vln I 264.417 +2.5 that HISTORY says to keep.

**Fix.** Pin the c45 automatic points by adding them to `REBOW_AT`:

```
for _t, _p in {"Violins I": [205.949, 264.417], "Violins II": [165.86, 263.921], "Violas": [169.5, 263.414],
               "Violoncellos": [153.366, 165.293],
               "Double basses": [170.003, 221.8, 225.215, 227.775, 230.393, 233.038, 235.659],
               "Violoncellos div": [275.527, 277.599, 279.67, 281.716, 284.141], "Violas div": [280.439]}.items():
    REBOW_AT[_t] = sorted(set(REBOW_AT.get(_t, []) + _p))
AUTO_REBOW_SKIP["Double basses"] = AUTO_REBOW_SKIP["Double basses"] + [164.0]
```

The basses' 164 note grows from 4.43 to 4.63 s and would get a new, unfitted automatic re-bow at 166.04. With these lines the simulation gives:
- 0 warnings;
- note sets identical to c45 on every track;
- the longest string piece 4.94 s (Violins II div 108, which was 4.81 s).

Then refit nothing. The fitted shapes sit on the same points.

**Loop check after the render.** Re-measure the 3.95 s autocorrelation on Contrabassoon 87 (13.2 s), Bassoon 2 90 (11.7 s), Horn 1 232 (7.7 s), Horn 4 84 (7.6 s) and the timpani roll at 226 (13.9 s). Each is 0.2-0.5 s longer than in c45.

## 4. Hairpin curve shapes: final values, and where they must be applied so they change no articulation decision (measured in a prototype)

**Values.** For each printed hairpin, the CC lane runs from (q, start) to (stop, target) as a quadratic Bezier. The control point sits at (q + cx * L, start + cy * (target - start)), sampled at 12 points:
- **crescendo (cx, cy) = (0.34, 0.88).** This is Mulan's measured shape: most of the rise comes early, then settles. It agrees with Part 4's early-rising phrase arch, and with c44 C #2's finding that 16 % of crescendos rise less than 1 dB.
- **diminuendo (0.68, 0.27).** This is Howl's measured shape: it holds, then falls late. Mulan's (0.72, 0.0) points the same way, but it ends at 3.6 times the average slope against Howl's 2.3, and Howl's is the lyrical, played-in file.

**Scope.**
- Hairpins of 6 s or less: 147 of the 341 printed hairpins on tracks are curved.
- Long builds stay linear. These are hairpins longer than 6 s and every hairpin starting in 172-220 or 250-259 (the animando and allargando builds). A curve that reaches 88 % in the first third would flatten a poco a poco build.
- The timpani staff ("Timp") stays linear, after Movement I's +8 dB roll lift.
- HP_NIENTE hairpins and fitted shapes (HELD_DECRESC, rebow and CC7 fits) are left alone.
- The volume-envelope hairpin ramps (hpgain, HP_SOFT dB) stay linear. They act after the hall, so a steeper late fall there could cut tails (S3).

**Implementation trap (measured).** I first bent the curve inside `base_points` (around line 1673). That flipped Violins II 243 to Leg BC MAX (keyswitches at 242.91 and 243.76, entry lead 0.14 -> 0.07 s). The curved CC11 crossed the `BC_SOFT` max_cc of 52 there.

The rule decisions read `base()`, so the same could happen with:
- `BC_SOFT`;
- the CC-range `ENTRY_LEAD_S` tuples;
- `sus_cc_by`;
- `LEG_VEL_BY_CC`.

Apply the curve where the dynamics lane is sampled into `cc11` (and `cc1` on `CC1_DYN_TRACKS`), not in the curve that the rules read. Then diff the keyswitches and leads against c45: they should match, as they did with the curve off.

**Effect (prototype, CC lane at 25 / 50 / 75 % of each hairpin).**
- Crescendos: +3 / +3 / +2 CC (median, on the 87 that changed).
- Diminuendos: +3 / +4 / +3 CC higher (held longer).
- About 0.5-1 dB. Timpani CC1, CC7, CC11 and vol_db are unchanged.
- Measure the audio after the render: hairpins on the lead lines (c44 C #2's list) should still go the printed way by at least 1 dB.

## 5. Two soft viola entries after breaths are late on the beat (S2; measured on the c45 stems)

**Where.** Violas qn 66 (bar 23, the violin theme's entry with the violas divided) and qn 188 (bar 56). Both are first notes of a Leg Slur MAX run at CC11 46-50, v50-53. Both follow breaths that c46 lengthens: CAESURA 66 goes 0.10 -> 0.20, and 188 gets 0.12.

**Evidence.** I measured every entry after a rest at a breath point on the c45 stems: the time the 10 ms RMS reaches body -10 / -6 / -3 dB, where body is the median at +0.15..+0.45 s.
- Violas 66: +0.08 / +0.16 / +0.19 s.
- Violas 188: +0.10 / +0.11 / +0.11 s.
- The other 40 entries reach body -6 dB between -0.17 and +0.07 s; the latest are Horn 3 at 204 (+0.07 s) and Horn 1 at 29 (+0.07 s). Examples:
  - Violas div at 66: -0.14 s.
  - celli at 124: +0.04 s.
  - Violin I solo at 48 and 60: +0.03 s.
- After a longer breath, a late soft entry is more exposed (inferred).

**Fix.** In `build/entry_leads.json`, Violas: `"66.0": 0.10, "188.0": 0.08`. The total stays under the 0.30 s cap. Check after the render that body -6 dB falls within ±0.05 s.

Carried item (not re-measured here): Oboe 1's legato arrivals are +46 ms late (c45 pcX median). `by_name` takes the first matching key, so insert `"Oboe 1": 0.10` ahead of `"Oboe"` in `LEG_LEAD_S`, a lead 0.04 s earlier. Re-measure pcX.

## 6. S3 at every breath: no breath cuts to silence; one existing post-hall fall sits in an exposed release (measured)

**Silence.** At all 24 caesura points, some note is always sounding in the window from 1 qn before to 0.5 qn after, in both c45 and the final map: the harp, the pedals or the held parts. No breath leaves the orchestra silent, and the hall returns are not enveloped.

**Volume-envelope falls inside release tails.** I looked from each note-off to the next onset, at most 0.8 s, on every track that rests at a breath. The falls are the same in c45 and the final map: the caesuras add none. One is worth smoothing, because the longer breath at 29 exposes it:
- **Bassoon 1 at qn 29.0-29.1:** vol_db drops +3.0 -> -3.0 dB in 0.1 qn (about 0.12 s), straight after its note-off. Only Bassoon 2 and the harp sound through the 0.56 s breath. This is a post-hall step, the S3 mechanism.
- **Fix:** where the c45 `PHRASE_SHAPE` end of the 17.9-29.0 phrase meets the next phrase's start level, hold the end value for 0.5 s after the last note-off before moving to the next phrase's level. Do this generically: no step inside 0.5 s of a note-off when the next onset is more than 0.25 qn away.

The Flute 1 fall at 124.0-124.1 (6.0 -> 1.6 dB) now comes 0.52 s after its 123.75 note-off, against 0.30 s in c45. By then the wind tail is more than 20 dB down (t20 0.32 s), so it can stay.

**Do not touch.**
- The climax tempo: `CAESURA[204] = 0.10`, `BEAT_STRETCH` 204/208 x0.94, Largamente 54, and the 216-220 allargando.
- `RAMP_SPANS` and the animando ramp, 60 -> 64.
- The c45 re-bow points and their fitted fills (pin them as in finding 3, do not refit).
- The 204 and 268 breath gaps (`CAESURA_BREATH_QN` 0.12 there).
- The entry and legato leads in seconds (they carry over to the new map unchanged).
- The c39-c45 balance items listed in HISTORY.
