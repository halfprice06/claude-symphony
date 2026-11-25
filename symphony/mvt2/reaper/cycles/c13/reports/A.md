# Cycle 13, critic A: articulation and phrasing (on the cycle 12 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c13-A/`: the c12 set plus these new ones.
- `combo.py`: join dips on the power sum of several stems.
- `ctrldip.py`: the dip that the plan itself puts on each legato join (CC11 through the LEARNINGS dB(CC) map, plus vol_db), next to the measured dip.
- `swing.py`, `shape_avg.py`: level shapes inside long notes, measured and planned.
- `cc7fit.py`: timpani roll level against CC7.

Run them with `CYC=12 ~/.venvs/claude-composes-reaper/bin/python`. Levels are dB re full scale on the c12 stems. Onsets are score onsets (`sq`). build/parts.json (16:52) is the data that made this render. For reference, the actor measured the c12 master at -23.6 LUFS, LRA 23.9 LU, and the mp3 at -19.8 LUFS, LRA 15.7 LU (c12 CHANGES).

## Checked and working (measured)

- **Chords:** no chord goes to a legato patch (`chords_leg.py`).
- **Keyswitches:** every keyswitch lands in the preceding rest or note. The one exception is the known Ob1 207.952 (13 ms).
- **Slurs:** every slurred single-line note is on a legato articulation. The exceptions are the intended ones (Ob1 208, CA 157, the viola sextuplets) and the Vc div. figures at 51-53 and 63-65 (finding 1).
- **Unslurred wind and brass lines:** Cl2, BCl, Bn2, Cbn, Hn3/4, Tbn2, BTbn and Tuba re-tongue without holes (`susjoin2.py`: medians -2.7 to +1.3 dB, none of 9 dB or more).
- **Timpani:** the long ppp rolls (qn 3, 226, 292) hold within ±0.5 dB for 13-19 s, so they have no loop seams.
- **The tune at both climaxes, as heard:** Vln I + Fl1 + Vln II + Ob1 + Cl1 summed have a median join dip of 2.5 dB at qn 186-202 and 250-272. Only 1 of 33 joins is 6 dB or more.
  - Flute 1 alone still has 19 joins of 6-11 dB there, but it doubles Vln I in unison. Do not spend fills on those.

## 1. The cellos' divisi answers to the solo violin (bars 18 and 22, qn 51-53 and 63-65) open with a 10-15 dB hole, and their slurred figure is re-attacked. Measured; the patch choice is inferred.

**Score:** `aOneVc`, bars 18 and 22. The upper half of the cellos plays `c'8( es'8 c'4 des'4)` and `g8( aes8 bes4 g4)` "div.": an answer to the solo violin, slurred. The lower half holds the bass (`c2 bes,4`, `es2.`). The comment in the .ily says this is where the centre of attention passes to the cellos.

**Data:** both voices are on the one Celli KS Master track, so every note is a two-note chord on Sus MAX at v105. It has a -3 dB divisi cut from qn 50.9 and 62.9. The four slurred notes of each answer are re-attacked; `slurart2.py` lists 51.5, 52, 63.5, 64 and 65.

**Measured** (`shp.py`, 50 ms frames from the score onset):

| | Before the entry | Hole | Back to body |
|---|---|---|---|
| qn 51 | -52 to -54 dB (-48 half a beat earlier) | -60 to -63 from 0.0 to +0.25 s, -56 to -60 until +0.6 s | -52 by +0.65 s |
| qn 63 | -46 | -58 to -61 at -0.1..+0.05 s, -54 to -57 until +0.5 s | -47 by +0.7 s |

- Over qn 51-52.5 the answer sits at -55 to -62, while the Violin I solo holds -44 to -50 above it. That is 10-15 dB under the line it answers.
- In the same bars Vln II is at -48 to -57 and the violas are fading out (-52 to -75).

**Inferred:** the answer does not arrive. Its first beat is a hole, and the slurred figure sounds as four separate soft bow strokes on a full section that plays both voices.

**Fix:** a split track for the upper voice, built like the Violin I solo track.
- Patch: `/Volumes/MAC DRIVE/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib` (half section).
  - Dump its keyswitch map into `build/ks_maps_extra.json` with `dump_ks.py`. Load Leg Slur MAX and Sus MAX.
  - Use Close mic only, as on the solo violin track, to keep memory down.
- `tools/score_to_parts.py`:
  - Add a pitch-and-window split next to `TRACK_WINDOWS`: `TRACK_SPLITS = {"Violoncellos div": ("Violoncellos", [(51.0, 54.0), (63.0, 66.0)], 55)}`. Violoncellos notes with `sq` in a window and pitch of 55 or more go to the new track.
  - The pitches are 60/63/60/61 and 55/56/58/55. The lower voice (48, 46 and 51) stays on Violoncellos.
  - The new track keeps the slur legato rules (Leg Slur MAX, string leads, `ENTRY_LEAD_S` string 0.12 s at CC ≤ 50), SOFT_BOOST from no text, CC15 con sord. and CC70 0.
  - Append it last, after "Violin I solo", so stem numbers 01-28 do not change.
- Expected results:
  - The main Violoncellos track becomes a single line in these bars, so the divisi cut no longer applies.
  - The bass 49 -> 48 -> 46 -> 53 joins as an ordinary soft bow-change line (BC_SOFT or Leg BC) with no chord re-attack.
- `build/mix.json`: seat as Violoncellos, width 0.2. Gain is Vc gain -2 to start; set it after the render so that the answer body is 3-6 dB under the solo violin (Vln I solo bars 18/22 is -45 to -48).

**Check:**
- Summed Vc stems: no frame from -0.1 to +0.6 s of qn 51 and 63 more than 4 dB under the preceding note's body.
- `dom.py "Violoncellos div" 51 54`: own share 0.8 or more on each of the four notes.
- Attack gate passes.

## 2. At soft bow-change joins the plan adds its own 2.4-5.2 dB dip on top of the sample's sag. Worst case: the cello cantabile counter-melody, bars 23-30. Measured.

**Where:** Violoncellos qn 66-87, "unis., cantabile", p. The slurs are two-note groups (`es2 aes8( g8 | f2) g4( | aes2 c'4) | bes2( g4) ...`), so every bar line is an unslurred join. Also Vln II qn 63, 152-164 and 249, and Vla qn 48, 56 and 60.

**Measured (`holes.py`):** the Vc counter-melody joins dip:

| qn | 68 | 71 | 75 | 77 | 78 | 81 | 86 |
|---|---|---|---|---|---|---|---|
| dip (dB) | 10.5 | 6.0 | 6.4 | 7.4 | 8.5 | 7.9 | 6.6 |

In quarter-beat frames, bar 25 runs -43.9, -36.1, -37.2, -36.6, -39.2, -41.7, -45.9, -50.5 (qn 74), -53.7 (qn 75). That is about 17 dB within three beats of a p line whose printed dynamic does not change.

**Where the plan makes it (`ctrldip.py`, plan-made dip at the join):**

| qn | 68 | 71 | 75 | 78 |
|---|---|---|---|---|
| plan dip (dB) | 4.0 | 2.4 | 2.4 | 5.2 |

Three rules stack on the same instant:
- **(a) The BC_SOFT notch.** CC11 drops 49 -> 41 at each bow change (`VLA_BC_SOFT` notch 8 above CC 40; `notch_soft` 6 below).
- **(b) The swell_taper on a slur's last note.** `ends_phrase` is true at every slur end, even when the line continues legato through a bow change. It ramps to -6 CC at the join; at qn 69-71 the CC goes 53 -> 44 -> 41.
- **(c) bloomv.** It ramps qn 66 down to -5.5 dB exactly at the join with 68 (vol_db -1.0 -> -5.5, then back to -1.0 at 68.1). The note had nothing to correct: its measured level was flat (-44.9, -44.9, -43.5, -44.0, then -46.9 once the ramp acts; sample alone +0.7 dB over the note).

**Across the strings:**

| Section | Joins with a plan dip of 2 dB or more | Their measured median | Median of the other joins |
|---|---|---|---|
| Violoncellos | 19 | 5.6 | 4.4 |
| Violins II | 10 | 6.3 | 4.5 |
| Violas | 26 | 3.9 | 2.9 |

The sample's own sag (about 4.4 dB in the celli) already marks the bow change, so the notch is not needed to make it audible.

**What a listener hears (inferred):** the counter-melody swells and fades on every half note, like a hairpin per note, instead of a sustained cantabile line.

**Fix (`tools/score_to_parts.py`):**
1. Halve the bow-change notches: `VLA_BC_SOFT["notch"]` 8 -> 4 and `BC_SOFT["notch_soft"]` 6 -> 3.
2. In the contour block (about line 1067), a note whose next note joins it is not a phrase end. The next note joins it when it carries `bc_from == id(n)`, or when it is a legato target overlapped by `n`.
   - `ends_phrase = (... slur end ...) and not joined_next(n) or near(e, breath_q) or round(e, 4) in rest1`.
   - Such notes get "swell", not "swell_taper".
3. bloomv (about line 1650): skip a note whose next note joins it (the same test), and keep it for notes followed by a rest.
4. Then add early fills on the two deepest joins: `early_fills.json` Violoncellos `"68": 5` and `"78": {"db": 5, "pre_s": 0, "hold_s": 0.3}`.

**Check:**
- `ctrldip.py "Violoncellos,Violins II,Violas"`: no join with a plan dip over 2 dB. The Vc counter-melody joins (qn 68-86) all at 6 dB or less, and 68/78 at 5 or less.
- `swing.py Violoncellos -v`: in-note range of the qn 69-78 halves under 9 dB (now 9.1-13.8).
- No new 7 dB+ joins in Vln II/Vla (`TH=7 holes.py`).

## 3. Timpani crescendo and diminuendo rolls get half their planned dB: Opus treats CC7 as linear amplitude. The bar 60 roll (p < f into the Largamente) is inaudible. Measured.

**Measured (`cc7fit.py`):** inside the rolls, measured level minus vol_db fitted against 20·log10(CC7):

| Roll | CC7 | Measured change | Slope |
|---|---|---|---|
| qn 200, p < f | 33 -> 51 | +3.7 dB | 1.10 |
| qn 268, decresc. | 49 -> 31 | -2.6 dB | 0.79 |

A slope of 1.0 means linear amplitude (20·log10). `score_to_parts.py` builds CC7 as `127·10^(dB/40)`, so every dB step of a roll hairpin gets about half its value. The p (-26) to f (-16) step in `roll_db` is planned as 10 dB and delivers 4-5. KIT-LEARNINGS already noted that CC7 is "shallower than 40·log10".

**Score:** Timp bar 60: a roll at p, cresc., tied to an eighth at f (qn 203), then the ff roll at qn 204.

**Measured, qn 200-203.5:**

| | qn 200 | qn 202 | qn 203.25 |
|---|---|---|---|
| Roll level | -46.6 | -42.9 | -41.6 |

- Vln I is at -30 to -27 over the same bars. In the timpani's own band (60-250 Hz) the roll is 15-17 dB under the master at qn 200-201, -13.6 at 202-203 and -17 at 203-203.5.
- For comparison, the f roll at qn 268-271 is -8 to -10 dB in that band.
- `roles.json` Timpani [200, 203.5, -3] makes it worse. It was set in c05, when this roll measured within 1.2 dB of the tune. Since then the timpani mics and `roll_db` changed, and the roll is now 12-15 dB under the tune, so that cut is out of date.

**What a listener hears (inferred):** the timpani crescendo that should drive bars 59-60 into the Largamente cannot be heard until the ff roll starts.

**Fix (`tools/score_to_parts.py`, timpani block, after the CC7 lane):**
- For each roll (`Rls`) with a crescendo or decrescendo inside it, add `("env", ...)` breakpoints with `TIMP_HP_DB_FACTOR = 1.0` times `0.5·(roll_db(base(q)) - roll_db(base(roll start)))`. That is the half that CC7 does not deliver.
- Sample it on the 0.125 qn grid. Hold the value to the roll's end, and release it by the next onset.
  - qn 200: +5 dB by 202.75, held to 203.5.
  - qn 268: -4.6 dB by 270.75.
  - qn 168 (pp < p): +2.5 dB.
- Delete `roles.json` Timpani [200, 203.5, -3].
- Leave the static `roll_db` values and `TIMP_LOUD_ATTACK_DB` alone; their levels were tuned by measurement.

**Check:**
- The qn 200 roll grows 9 dB or more from qn 200.25 to 203.
- At qn 202-203 it is 6-9 dB under Vln I and -8 to -11 dB against the master in 60-250 Hz.
- It is never the loudest stem (BRIEF rule 5).
- The qn 268 roll falls 6-8 dB by qn 271.

## 4. Exposed wind solos still have 6-10 dB legato holes without fills. Measured.

These are solo lines with no unison doubling. The holes are found with `holes.py` and `combo.py`; `<-3 dB` is the span under the reference, in seconds from the score onset.

| Track | Passage | qn | Dip (dB) | Span | Fill now |
|---|---|---|---|---|---|
| Bass clarinet | "solo, espr.", bars 31-34; 5 of 9 joins at 6 dB or more | 92 | 7.8 | +0.05..+0.21 | |
| | | 93 | 6.8 | +0.03..+0.49 | |
| | | 98 | 6.0 | +0.09..+0.37 | |
| | | 99 | 6.3 | +0.04..+0.26 | |
| Oboe 1 | "dolce espr.", bars 45-46 | 143 | 10.1 | +0.03..+0.19 | 4 |
| | | 145 | 5.7 | | |
| Cor anglais | bars 33 and 41-42 | 97 | 6.9 | +0.02..+0.27 | |
| | | 126 | 6.6 | | |
| | | 128 | 7.4 | +0.00..+0.30 | |
| | | 129 | 5.5 | | |
| | | 131.5 | 6.6 | +0.03..+0.25 | |
| Clarinet 1 | bar 54 | 176 | 5.5 | | |
| | | 178 | 6.7 | | |

For the cor anglais, Fl1 doubles two octaves up at 126-136, and the pair still dips 6.3 dB at qn 128.

**Fix (`build/early_fills.json`, using the c08 rule dB = dip - 2, cap 8, with `hold_s` where the hole lasts past +0.3 s):**
- Bass clarinet: `"92": 6, "93": {"db": 5, "pre_s": 0, "hold_s": 0.45}, "98": {"db": 4, "pre_s": 0, "hold_s": 0.3}, "99": 4`
- Oboe 1: `"143": 8` (was 4), `"145": 4`
- Cor anglais: `"97": {"db": 5, "pre_s": 0, "hold_s": 0.25}, "126": 5, "128": {"db": 5, "pre_s": 0, "hold_s": 0.3}, "129": 4, "131.5": 5`
- Clarinet 1: `"176": 4, "178": 5`

Do not add fills to the Flute 1 climax joins (see the working list above).

**Check:** each listed join is 5 dB or less (`holes.py`), with no overshoot of more than 2 dB above the following body (`shp.py`).

## 5. Two breath marks are not audible. Measured, minor.

**Measured (`breath.py`):** 26 of 28 breaths dip 12-39 dB. The two exceptions:
- Horn 1 at qn 196 (bar 59, f, crescendo into the climax): 0.19 s of silence, a 4.4 dB dip.
- Clarinet 2 at qn 292 (pp coda): a 7.9 dB dip.

At qn 196 the note before is 1 qn long, so `e0 - min(0.25, 0.2 * dur)` gives only 0.2 qn. The release and hall tail of an f horn fill that gap.

**Fix (`score_to_parts.py`, the breath line in the note-length loop):** for wind and brass notes at CC11 72 or above, end the note 0.3 qn before the breath, in place of `min(0.25, 0.2 * dur)`. Leave the rule for soft notes unchanged.

**Check:** Hn1 qn 196 dips 8 dB or more, with the other 26 breaths unchanged.

Still open from c12, and not repeated here:
- The viola sextuplet articulation test (bars 59-60; own share 0.26).
- The bar 53 pickup, still 2.1-2.8 dB over its downbeat.

**Do not touch:**
- Leg Port on Vln I/II 82/172 and Vc 83.
- The BC_SOFT and `BC_SOFT_SKIP` articulation choices (change only the notch depth).
- The hold_s early fills.
- The pizz. step trims.
- Harp handling: rings through rests, rolls from the bottom, harmonics at 8va.
- The long timpani rolls and their settle, `TIMP_LOUD_ATTACK_DB`, and the static `roll_db` table.
- The CC15 sordino spans.
- The same-pitch merges and tie handling.
- The Tbn1 accent shapes (+2 to +4 dB).
- Keyswitch placement.
- The unslurred wind and brass Sus lines.
