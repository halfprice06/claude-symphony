# Cycle 14, critic A: articulation and phrasing (on the cycle 13 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c14-A/` (the c13-A set plus `tbn.py`, `sf.py`, `ties.py`, `kscheck.py`, `slurov.py`, `vln2loure.py`, `louré.py`, `artsum.py`). Run them with `CYC=13 ~/.venvs/claude-composes-reaper/bin/python`. Levels are dB re full scale on the c13 stems, onsets are score onsets (`sq`). `build/parts.json` (17:41) is the data that made the c13 render.

## Checked and working (measured)

- No chord goes to a legato patch (`chords_leg.py`).
- All 104 printed ties are held. No tied-to note is re-attacked in any track (`ties.py`).
- No two notes of the same pitch overlap on one track.
- Every keyswitch lands at least 20 ms before its note. The one exception is the known Ob1 207.952 (13 ms) (`kscheck.py`).
- Inside printed slurs, only 6 consecutive legato notes do not overlap, and each is intended: Vln II/Vla 218 -> 220 at the Tempo I bar line, CA 157 -> 159 after the tenuto, Vla 252.5 / 269, Vc 146.
- Unslurred Sus lines re-bow or re-tongue without holes (`susjoin2.py`): Cb median 1.5 dB (1 join of 9 dB or more out of 74), Bn2 1.3, Cl2 2.8, Vla 3.0, Hn3/Hn4/Tbn1 0 or less.
- Pizzicato:
  - Viola pizz. follows its p < mp > p hairpin in velocity (v53 -> 63 -> 53).
  - The note-to-note spread is a median 2.0-3.2 dB, the largest jump 6.7-7.1 dB.
  - Harp notes ring after their written value (a smooth 1 s decay).
- Viola triplets on Leg Slur MAX (bars 37-40, pp): each note dominates 0.91 of its slot (`dom.py Violas 108 112 13`).
- Vln II con sord. portato pairs (bars 15-21, `aes'2--( aes'4--)`): the tenuto quarters sit within -5..+1 dB of their half notes (median -1.6). That is acceptable for pp accompaniment.
- Bar 63 sf tremolo chords: Vln II rises 10 dB on the sf and falls 5-7 dB in the next 0.3 s, then follows the > to p. This is an sf, so it is not held to the 2-4 dB accent rule.

## 1. Trombone 1's marcato quotation (bars 63-64, qn 212.5-220) plays legato: every unaccented note starts in a 3-5 dB hole. Measured.

**Score:** `bSecTbnOne`, `r8 e8->\ff^"marcato" c'4.-> b8 bes8 a8 | a4 gis8 a8 f4.->\> e8\mf`. This is trombone 1's first sound in the movement. It is the only solo brass line at the climax, over tremolo strings. The word "marcato" applies to the whole line, not just the three accented notes.

**Data:**
- `score_to_parts.py` reads only the `accent` scripts (line 672, `accent_q`), so the "marcato" text does nothing.
- The three accented notes (212.5, 213, 218) play Sus Accent MAX.
- The six notes in between (214.5, 215, 215.5, 216, 217, 217.5) play Sus MAX at v91 and CC11 114. Each lasts its full written value, so every note ends exactly at the next onset; 215.5 ends 0.03 qn early because of the same-pitch guard.
- vol_db gives each of these notes a 1-2.5 dB fall across its length.

**Measured (`tbn.py`, 10 ms frames from the score onset):**

| Note (qn) | Previous note's end | Minimum after onset | Body |
|---|---|---|---|
| 214.5 B3 | -26 | -31 at +0.07 s | -25..-26 |
| 215 B flat 3 | -25 | -30 at +0.07 s | -28..-29 |
| 215.5 A3 | -29 | -31 at +0.05 s | -28..-29 |
| 216 A3 | -31 | -33 at +0.04 s | -27..-28 |
| 217 G sharp 3 | -30 | -33 at +0.07 s | -28..-29 |
| 217.5 A3 | -28 | -28 (no event) | -28..-29 |

- Each new note starts 2-5 dB under the end of the previous one and reaches its body after about 0.1 s.
- No note is louder at its attack than in its body, and there is no gap between notes.
- The accented notes are weighted: 212.5 is +4 dB over its body, and 218 rises from -30 to -24 within 30 ms (+1-2 dB over its body). Those can stay.

**What a listener hears (inferred):** a smooth, swelling legato line in which the notes between the accents are joined and soft-edged. A marcato line has a weighted attack and a small break on every note.

**Fix:**
- `tools/score_to_parts.py`:
  - Add `MARCATO_SPANS = {"Trombone 1": [(212.5, 220.0)]}`, or derive it from the "marcato" text running to the next dynamic change or rest.
  - Inside a span, notes with no accent whose written value is 1 qn or less take `ks_lookup(stem, "Marc Lng RRx4")` (1TB KS Master key 29, row 6, among the default-loaded rows).
    - Velocity comes from the dynamic: ff ≈ 108, then down the > to about 85 at 217.5. Short articulations take their dynamic from velocity.
    - Keep the CC11 lane.
    - Note length: 0.75 x the written value (eighths 0.375 qn, the quarter at 216 0.75 qn).
    - The four RRs vary the repeated A3s at 215.5, 216 and 217.5.
  - The accented notes stay on Sus Accent MAX with `ACCENT_DB_AT` unchanged. End them 0.1 qn early, so the break before 214.5 and 219.5 is audible.
  - Drop the 1-2.5 dB per-note falls on the Marc Lng notes. The sample decays by itself.
- If Opus reports a state change for the row, `--midi-only` fully rebuilds only Trombone 1.
- **Fallback, if Marc Lng is far off level or timbre:** keep Sus MAX at 0.8 x length, and add the `ACCENT_DB_AT` shape at +2 dB (10 ms rise, held 0.08 qn, 0 by 0.25 qn) to each of the six notes. That stays inside Dan's 2-4 dB rule.

**Check (`tbn.py`):**
- Each of the six notes peaks 2-4 dB over its own body within 0.05 s of its onset.
- The level falls 6 dB or more between notes.
- The bodies are within 2 dB of c13 (-25..-29). If Marc Lng sits off, set a Tbn1 `note_trims` value for those onsets.
- Tbn1 is never more than 1 dB louder at 214.5-217.5 than at the 212.5 accent.
- The attack gate check at 212.5 stays ok.

## 2. Timpani rolls tied into a printed stroke end without the stroke, most audibly the f arrival at qn 203. Measured.

**Score:** four rolls are tied to a short note. A timpanist ends such a roll with a single stroke on the tied note.
- Bar 60: `aes:32` p < tied to `aes8\f` at qn 203, then rest. The f is printed on the eighth. It is the arrival that leads into the Largamente ff.
- Bar 62: the ff roll on A flat (qn 210) tied to an eighth at 211, before the qn 212 caesura.
- Bar 3 (qn 8, pp) and bar 79 (qn 237, ppp).

**Data:** LilyPond merges each tie into one MIDI note, so parts.json has one Timpani Flt Rls note: 200-203.5, 210-211.5, 3-8.5, 226-237.5.

**Measured (Timpani stem, 50 ms frames):**
- qn 202.5-203.5: -33..-35 dB, flat within ±1 dB. Nothing happens at 203; the roll stops at 203.5 and decays to -55 within 0.5 s. The ff roll enters at 204 (-29).
- qn 210.5-211.5: -37..-42, again with no event at 211.
- The pp ends at qn 8 and 237 behave the same way.

**What a listener hears (inferred):** the crescendo roll that drives bar 60 has no point of arrival. It cuts off half a beat after the printed f instead of landing on it.

**Fix (`score_to_parts.py`, timpani branch, about line 706):**
- When a roll's MIDI note runs past the last tremolo onset, and the rest is a tied note of 1 qn or less with no tremolo (203, 211, 8, 237), end the roll note at that onset + 0.03 qn.
- Add a "Timpani Flt Lng" note at the tied note's onset.
  - Its velocity comes from the existing stroke table (line 981): f ≈ 96, ff ≈ 104. At 8 and 237 the floor v53 applies, or skip those two.
  - Its CC7 comes from `timp_db` for strokes; the CC7 lane switches at the stroke onset.
- `TIMP_LOUD_ATTACK_DB` already fires for strokes printed f or louder, so 203 and 211 get their weight.
- The roll settle in vol_db should start from the stroke, not from the old roll end.

**Check:**
- Timpani at qn 203: a peak 4-8 dB over the roll's last 0.5 qn (-34) within 0.05 s, then a decay.
- The ff roll at 204 is still louder than the 203 stroke's body.
- The timpani is never the loudest stem at 203-204.
- At 211 the stroke falls into the caesura silence.

## 3. The viola sextuplets of bars 59-60 are still a smear; the same section's slurred triplets on Leg Slur MAX are clear. Measured. A test inside one render is proposed.

**Score:** violas, bars 59-60 (qn 196-204), f, slurred sixteenth-sextuplets in one-beat groups (0.157 s per note).

**Data:**
- All 44 notes play Sus MAX at v100, detached by 0.01 qn (`SHORT_SUS_DETACH`, c11).
- c03 moved them off Leg Slur MAX because legato transitions then took 160-320 ms. That was before the legato velocity went to 124 and the lead tables, which brought the string crossovers to 50-85 ms in c03-c11.

**Measured (`dom.py Violas ... 13`):**

| Passage | Articulation | Median own share of each note's slot |
|---|---|---|
| Sextuplets, qn 196-204 | Sus MAX | 0.24 |
| Triplets, qn 108-112, pp | Leg Slur MAX | 0.91 |

c11 showed that the detach did not help (0.27 -> 0.26).

**What a listener hears (inferred):** a buzzing chord cluster under the climax build, not a moving slurred figure.

**Fix (an A/B inside the next render, no range render needed):**
- In `score_to_parts.py`, at the `short_sus` branch (line 724), exempt Violas notes with `sq` in [196, 200), which is bar 59 only.
- Put them on Leg Slur MAX at v127. Overlap 0.02 qn and no lead; the lead cap already limits it to about 0.07 s.
- Bar 60 stays on Sus MAX as the control.

**Check:**
- Run `dom.py Violas 196 200 14` against `dom.py Violas 200 204 14`.
- If bar 59 reaches 0.5 or more with no onset later than +0.06 s, extend it to bar 60 next cycle. If not, revert and close the item.

## 4. Horns 1-2 a2 at the second climax (bars 79-82, qn 261-273) are one solo horn +3 dB. Inferred, low priority.

**Data:** Horn 2's 8 unison notes are dropped (`unison_dropped`), and Horn 1 plays them alone on the Solo French Horn KS Master with +3 dB.

**Measured:** Hn1 sits 13-15 dB under the master in bars 79-81 (-34.4, -36.0, -38.6 against -21.0, -21.6, -25.5).

**Inferred:** the line is an inner voice, so the gain from a true two-horn timbre is small. It is listed only because the lens asks about better patches.

**Fix, if memory allows a 30th instance:**
- Add a track "Horns 1-2 a2" on `/Volumes/MAC DRIVE/EW Hollywood Brass Diamond/Hollywood Brass Opus Instruments/2 French Horns/06 Keyswitch/2FH KS Master.oib` (Leg Slur MAX row).
- Route the notes with `TRACK_WINDOWS` {Horn 1: [(261, 274)]}.
- Remove the +3 dB unison lift for those notes.
- Set the gain from one render so the pair matches the c13 Hn1 level (-34..-39 per bar).

Do not touch:
- Tie handling, the same-pitch merges and their notches.
- Keyswitch placement.
- The Leg Port targets, BC_SOFT / `BC_SOFT_SKIP`, and the halved notches with `joined_next`.
- Viola triplets on Leg Slur MAX (0.91 own share).
- Pizzicato velocities and step trims.
- Harp ringing and rolled chords.
- The Tbn1 accent shapes at 212.5 and 218 (`ACCENT_DB_AT`).
- `TIMP_HP_DB_FACTOR`, `TIMP_LOUD_ATTACK_DB` and the static `roll_db` table.
- The sf tremolo chords at bar 63.
- `mute_eq` for Horns 3-4. The Solo Horn's "Stop" patches are stopped horn, not con sordino, so they are not a substitute.
