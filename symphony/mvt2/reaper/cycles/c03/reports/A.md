# Cycle 3, critic A: articulation and phrasing (on the cycle 2 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c03-A/`. They are c02-A's scripts pointed at `cycles/c02/render/`, plus:
- `arrive.py`: time for the new pitch's harmonic band to reach -6 dB of its level at +0.6 s, split by join type;
- `rep.py`: same-pitch joins;
- `ten.py`: tenuto notes;
- `chord.py`: chord changes on Sus/Flautando;
- `mdip.py`: master-bus dips;
- `tb.py`: attack brightness of Tbn1;
- `pzon.py`, `pzv.py`, `pzb.py`: pizz onsets;
- `harp.py`: harp ring.

Bars: 1-36 = qn/3+1, 37-64 = (qn-108)/4+37, 65-92 = (qn-220)/3+65. `parts.json` (23:50) is the data the c02 render (00:06) was made from.

## 1. String repeated notes (portato and same-pitch bow changes) leave 7-15 dB holes. At bar 66 the whole mix drops 6-10 dB

**Measured.** In a legato string line, a repeated pitch is cut 0.06 qn early and re-attacked by Leg Slur MAX's sustain layer. At pp that layer takes 300+ ms to reach level. Per-stem dip at the repeat (lowest 20 ms window against the 200 ms before):

| Where | Score | Stem dips |
|---|---|---|
| Vln II bars 15-21, qn 44, 50 | portato pulses: tenuto under a two-note slur, pp con sord. (checked on the score image) | -15.3, -15.3 |
| Bar 66, qn 223 | pp re-bow of a held note | Vln II -13.1, Vla -10.5, Vc -12.2 |
| Bar 46, qn 144 | barline repeat | Vla -12.6, Vln II -7.3 |
| Bar 49, qn 156 | barline repeat | Vla -8.5, Vln II -7.5 |
| Bar 52, qn 168 | barline repeat | Vc -14.7, Vln II -11.4 |
| Bar 88, qn 289 | barline repeat | Vln II -10.7, Vc -8.7 |

Median repeat dip: Vln II -10.7, Vla -8.9, Vc -8.7 dB. For comparison, a legato join with a pitch change is now -2 to -4 dB.

On the master bus (`mdip.py`):
- qn 223 (bar 66): -6 to -10 dB for about 0.5 s. This is the largest articulation hole in the piece.
- Bars 15-18 and 88: -3 to -5 dB.

A real section changes bow on a held pitch with a dip of only a few dB. A portato pulse is a pressure swell, not a gap.

**Related (measured).** The Vln II div. sul tasto Flautando half-note chords in bars 38-40 (qn 112-122) dip -4 to -6 dB from 0.2 to 1.0 s after each change. The causes:
- the common tones are re-struck (61 at qn 112 and 118, 66 at qn 114 and 116);
- the moving voice ends exactly where the next voice starts;
- Flautando's attack is slow.

The master shows no dip there, so this matters less.

**Fix in `tools/score_to_parts.py`, `build_track()`, family "string", note-length loop, `same_pitch` branch.**
- **Merge.** When a note and the next note have the same pitch, both are on a Leg articulation, and the original gap is under 0.1 qn, merge them. The trigger is not a breath, and not a rest of 1 qn or more. To merge:
  - set the first note's `end` to the second note's end;
  - drop the second note;
  - add a CC11 notch at the second note's onset `q`: from 0 at `q - 0.06`, down to `-depth` at `q`, back to 0 at `q + 0.25`.
- **Notch depth.**
  - Portato (tenuto inside a slur): 10 CC.
  - Barline or new-bow repeat: 14 CC. That is about 3 dB, using c02's measurement of 14 CC as +2.6 dB.
  - Add the notch as a new `contours` kind, `"notch"`, so it sums with the swell/taper code. The +5 tenuto bump stays on the portato notes.
- **Flautando chords.**
  - Merge a common tone into one held note when the next chord repeats it.
  - Extend a moving voice's end 0.15 qn past the next onset (polyphonic, so this is a crossfade, not legato).
- Winds are not affected: their re-tongued repeats (Bn1 -8.7) are realistic.
- **Check with `rep.py` and `mdip.py 223 44 50 289`:**
  - stem repeat dips -2 to -5 dB;
  - master at qn 223 no lower than -3 dB.

## 2. String and horn legato still arrives 230-270 ms after the MIDI onset; velocity cannot fix it, so move the targets earlier (deferred A2c)

**Measured.**

`xover.py` (time from the MIDI onset until the new pitch's energy beats the old pitch's):

| Track | Median (ms) | p25-p75 (ms) | By velocity |
|---|---|---|---|
| Vln I | 255 | 208-285 | |
| Vln II | 272 | | |
| Vla | 240 | | v120 225, v105 305 |
| Vc | 270 | | v120 242, v105 270 |
| Hn 1 | 190 | | |
| Hn 2 | 185 | | |
| Ob 1 | 145 | | |
| Bn 1 | 135 | | |
| Fl 1 | 112 | | |
| Cl 1 | 115 | | |
| CA | 100 | | |

`arrive.py` (new pitch within 6 dB of its level):

| Track | Leg Slur (ms) | Leg BC (ms) | Re-attack after a gap under 0.3 qn (ms) |
|---|---|---|---|
| Vln I | 250 | 295 | |
| Vln II | 260 | 230 | |
| Vla | 230 | 240 | 60 |
| Vc | 212 | 250 | 55 |
| Cb (Sus only) | | | 95 |
| Fl 1 | 75 | | |
| Cl 1 | 80 | | |

- The c02 changes (legato speed on, velocity 105/120) gained only 20-40 ms over c01's 285/275/222/310.
- At ♩=52 an eighth lasts 577 ms. So every slurred string note sounds about 0.2 of a beat behind the harp, the pizz. and the flute/clarinet doublings.

**Inferred.** The patch's LegatoSpeed script offsets the sample start by at most 4800 samples (100 ms; c02-A read START_MIN/MAX from the .oib). Velocity is near the top of that range already, and what is left is the recorded transition length. A review in `guides/eastwest-hollywood-orchestra/youtube/20210531_...md` says you "have to play the notes a bit early" with these legato patches.

**Fix: new step at the end of the note-length loop in `score_to_parts.py`.** For every note with `leg_target` (Leg Slur and Leg BC):
- Move the onset earlier by `s * bpm / 60` qn at the local tempo:
  - strings: s = 0.16 s;
  - horns: 0.10 s;
  - oboe, cor anglais, bassoon, bass clarinet: 0.05 s;
  - flute and clarinet: 0.
- Move the previous note's end by the same amount, so the 0.04 qn overlap is kept.
- Never move a note before the previous onset plus 50% of the previous note's length.
- Use the original onset for CC/dynamic lookups.
- Set the Leg BC keyswitch at the new onset minus 0.02 qn.
- Set every string and horn legato-target velocity to 124. In c02, v120 was 25-80 ms faster than v105.

Optional (measured on few notes): soft string entries after a rest reach -6 dB only 300-360 ms after the onset (Vln I, Vla, Vc, Cb; n = 1-4). Moving string Sus/Leg entries at p or softer 0.06 s earlier would align them with the winds.

Check with `xover.py`. Target: string and horn medians of 80-130 ms.

## 3. Tenuto notes are cut 0.06 qn and re-attacked; at the ff Largamente (bars 61-62, "molto sostenuto") this chops the chorale into separate notes

**Measured (`ten.py`).**
- **Score (checked on the page 5 image).** Bars 61-62 are ff tenuto half notes in every part, marked "molto sostenuto".
- **Cause in the code.** Tenuto notes are excluded from Leg BC (`near(n["qn"], ten_q)` in the BC loop). The note-length loop gives them `e0 - min(0.06, 0.15*dur)`.
- **Stem dips at the joins:**

  | Part | Dip (dB) |
  |---|---|
  | Vln I | -5.9, -5.8 |
  | Vc | -8.2 |
  | Cb | -8.2 |
  | Ob 1 (repeated F) | -18.8 |
  | Fl 2 | -9.3, -13.0 |
  | Cl 2 | -10.5 |
  | Bn 1 | -9.2 |
  | Bn 2 | -8.3 |
  | Hn 4 | -7.7 |

- **Master.** Only -1 to -3 dB at qn 206, 208 and 210, because the hall and the other parts fill in. So this is smaller than finding 1, but each instrument re-starts.
- **What tenuto means.** Full value with weight: separate bows in the strings, a light re-tongue in winds and brass.

**Fix in `score_to_parts.py`.**
- **Strings.** In the Leg BC loop, drop the `near(n["qn"], ten_q)` exclusion when the next note has a different pitch. A monophonic tenuto line then joins with Leg BC MAX (0.04 qn overlap) and keeps the +5 CC tenuto bump. That bump is its weight.
- **Cb (no Leg BC).** Tenuto gap 0.02 qn.
- **Winds and brass.** Tenuto gap `min(0.03, 0.1*dur)` instead of 0.06 when the level is mf or louder, or while "molto sostenuto" / "sostenuto" is in force. Keep 0.06 at p and softer.
- Same-pitch tenutos in strings follow finding 1.

Check with `ten.py`. Target: string joins in bars 61-62 at -2 to -4 dB, and wind joins at -6 dB or shallower.

## 4. Trombone 1's quotation at bar 63: the first two accents (qn 212.5, 213) do not sound accented; the keyswitched accent at qn 218 does

**Measured (`tb.py`, `acc.py`).** Trombone 1 enters for the first time at qn 212.5: ff, "marcato", accents on e8 and c'4. (bSec.ily line 135, c069: held back for this quotation.) Its first articulation, Sus Accent MAX, is set only through the patch state (`currentKeySwitch` in `build_reaper.py state_for`). No keyswitch is sent.

| Note | Attack energy, 1.5-6 kHz, first 120 ms against 250-450 ms | Level |
|---|---|---|
| qn 212.5 | -8.8 dB | flat at -35 dB |
| qn 213 | -8.6 dB | rises from -35 to -29 dB over 0.6 s (a swell, the opposite of an accent) |
| qn 218 (same articulation, reached by the keyswitch at 217.94; same CC11 122, same velocity 121) | +5.6 dB | +3 to +4 dB over the preceding bar, then decays (the 2-4 dB accent Dan asks for) |

**Inferred.**
- The state path does not select Sus Accent MAX, so the first two notes play Sus MAX.
- The `.oib` has `currentTrigger` and `lastArticulationId` next to `currentKeySwitch` (dumped from `1TB KS Master.oib`; default currentKeySwitch 24 = Sus MAX). `state_for` sets only `currentKeySwitch`.
- Other tracks whose first articulation is not row 0 may be affected the same way:
  - Fl 1, Fl 2, Ob 1, CA, Cl 1 and Hn 1 (Leg Slur);
  - the timpani (Rls);
  - the four upper strings (Leg Slur MAX).
- The strings and Vln II/Vla/Vc switch by keyswitch at qn 2.94, so they only depend on the state for their first notes. The data could not show whether Hn 1's first phrase (bars 6-14, no keyswitch anywhere in its part) is true legato.

**Fix.**
- **`score_to_parts.py`, keyswitch loop.** Emit the first keyswitch too whenever the first note is 0.5 qn or more after qn 0, at `early_time(first note)`. For Tbn1 that is in the rest before 212.5, and the same holds for every wind and brass track. Tracks that start at qn 0 (strings, Hn 3) keep relying on the state.
- **`build_reaper.py state_for`.** Also set `articulations.currentTrigger` and `lastArticulationId` to the first articulation's entry. Copy the structure from a KS Master saved by Opus after a keyswitch, if one exists in `jobs/`.
- **Check with `tb.py`.** Expect 212.5 and 213 at +3 dB or more of attack brightness, and a 2-4 dB accent level bump.

## 5. Divisi passages still use full-section Sus MAX chords; the slurred upper cello line in bars 18 and 22 loses its legato (c02 A5, still open)

**Measured in parts.json.**
- Vc div., qn 51-54 and 63-66: the slurred upper answer and the held lower note are simultaneous. So both are Sus MAX (11 Sus notes in Vc). The upper line's slur is not rendered as legato.
- Vla div., bars 23-36: 30 Sus MAX notes.
- Vln II div. sul tasto, bars 37-44: Flautando chords with the full section on each line.

**Inferred.** Each divided line sounds with 16 players, so the texture is about twice as thick as written. This is lower priority than findings 1-4: the chord joins themselves are fine (Vla/Vc chord-change medians -0.2 to -2 dB, `chord.py`).

**Fix (as c02 A5).**
- Add one track per divided section on its DIV B KS Master:
  - `Celli Divisi/06 Keyswitch/Celli KS Master DIV B.oib`;
  - `Violas KS Master DIV B.oib`;
  - `2nd Violins KS Master DIV B.oib`.
- Switch the main track to DIV A only for the div. spans: qn 51-54 and 63-66 (Vc), 66-108 (Vla), 108-140 (Vln II).
- In `score_to_parts.py`, send the highest note at each onset inside a span to DIV B. Each half then runs its own Leg Slur logic, so the cello answer becomes legato.
- Give DIV A and DIV B the parent's mix.json entry at -3 dB.
- Optional: the 1st Violins DIV A patch, a half section, for the Vln I "solo" at qn 48-65.

## Do not touch

- **Pizz now plucks** (measured): onsets rise at 0-10 ms; drop 400 ms after peak Vla 10.6, Vc 12.6, Cb 16.0 dB. All 42 Vla pizz notes show their pitch band rising 20-35 dB.
- Tremolo and Flautando articulation loading.
- No chords on any legato patch, and the 0.04 qn slur-scoped overlap.
- **Legato joins inside slurs:** Vln I median dip now -2 dB (was -4 to -6).
- **Leg BC joins:** -4 to -5 dB (were -8 to -12). Keep the Leg BC rule, and extend it as in finding 3.
- Keyswitches placed in rests: none lands less than 0.03 qn before its note, except one each in Vln I and Vln II.
- **Harp:** rings after note-off, decaying only 2-4 dB in 0.4 s. Keep the Sus RR velocity scheme and the separate harmonics track.
- Tbn1's keyswitched accent at qn 218: +3-4 dB, not a click.
- Breath shortening; wind re-tongued repeats; the timpani articulation scheme.
