# Cycle 8, critic A: articulation and phrasing (on the cycle 7 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c08-A/`. Run them with `~/.venvs/claude-composes-reaper/bin/python`. The c07-A scripts were copied there with the default cycle set to 07. New scripts:
- `wjoin.py "<tracks>" [cyc] [-v]`: legato joins (60 ms smoothed envelope), with velocity, interval and CC11 for each join.
- `bloom2.py`, `fill.py`: on legato targets of 0.7 s or longer, the level of the first 0.05-0.35 s against the note body (0.4 s to end-0.1 s). Notes inside a hairpin (CC11 change of more than 6) are excluded.
- `bcx.py`: string join dips grouped by previous and target articulation (20 ms envelope).
- `ripple.py`, `shape.py`, `bodies.py`: per-note envelope detail.

The c07 render is good for timing: the attack gate passed 19 of 19, and the measurements below match c05 and c06 to within 0.2 dB where the data did not change. So the effects are deterministic and can be fixed per onset.

## 1. Wind and horn legato notes sag 5-12 dB for their first 0.3 s, then swell into the body: 35 notes in the solos

**Where.**
- Flute 1 solo, bars 37-44 and 57-59, and the bar 75-77 tune.
- Oboe 1, bars 16-20 and 44-47.
- Cor anglais, bars 33-34 and 43-44.
- Horn 1, bars 54-60 (every F4).
- Horn 2 bars 75-77, Bassoon 1 bar 79-80, Clarinet 1 bar 75.

**Measured.**
- `fill.py` checks legato targets at a flat CC11. On 35 of them the body is 5-12 dB louder than the first 0.3 s of the note. On most notes the difference is 1-3 dB (track medians +1.6 to +2.8).
- The worst notes, given as onset / pitch / dB:
  - Fl1: 111/E flat 5/+10, 118/E flat 5/+8, 132/E flat 5/+9, 134/D flat 5/+7, 189/D flat 6/+8, 198/D flat 6/+6, 250/A flat 5/+6, 256/G6/+5.
  - Ob1: 47/+6, 56/+9, 59/+6, 140/+8, 143/+6, 189/+8, 262/+5, 270.5/+6.
  - CA: 98/+6, 134/+6, 135/+6, 136/+7.
  - Hn1: 39/+6, 176/+7, 182/+7, 184/+5, 188/+6, 192/+8, 195/+10, 199/+6, 201/+12, 203/+9.
  - Hn2: 252/+6, 258/+8. Cl1: 252/+6. Bn1: 264/+6, 267/+5.
- Some pitches do this every time they occur:
  - Fl1 E flat 5: +8.6 on 4 of 4 notes. This is the F5 -> E flat 5 step in the bar 37-43 tune; its join dips are 13.8, 7.7 and 11.2 dB (`wjoin.py`).
  - Fl1 D flat 6: +6.7 on 2 of 2. Ob1 D flat 5: +7.6 on 3 of 3.
  - Horn 1 F4: +8.2 on 6 of 6 (`bloom2.py`).
- The shape at Fl1 qn 111 (`shape.py`, 20 ms steps from -0.2 s): -46, -46, -49, -53, -56, -58, -61, -60, -60, -59, -58, -57, -57, -58, -54, -51, -49, -47 dB. The note falls 14 dB below the note before it, stays down for about 0.4 s, and then recovers.
- Horn 1 F4 at qn 195 and 201: the early level is -47.4 / -48.4 dB and the body is -38.2 / -36.5 (`bodies.py`). The c07 pitch trim of -5 dB on F4 is flat across the note. It levelled the F4 bodies with their neighbours (qn 192 body -41.7, qn 193 -41.7), but it pushed the start of each F4 down further.
- CC11 and CC1 are flat across these notes (Fl1 qn 111: CC11 46, CC1 100). The sag is in the samples.
- Velocity plays a part. Median join dips by legato velocity (`wjoin.py`):
  - Fl1: v60 4.9, v80 3.3, v100 2.5 dB.
  - Cl1: v60 4.8, v80 2.4. Ob1: v60 4.7, v80 3.9.
  - Horn 1 (v124): 2.9.
  - Velocity is not the whole cause: the cor anglais at v80-90 still has a median of 5.2-6.1.
- The dips are identical in c05 and c06 (Fl1 111: 13.8 / 13.8 / 13.8), so they are deterministic.

**Inferred.** In the exposed solos, the flute, oboe and cor anglais in bars 33-47 and the horn in bars 54-60, every affected note starts thin and then swells. That sounds like a hairpin on each note, which no player would make, and it breaks up the slurred line where the score asks for one connected phrase.

**Fix.** Make the level change follow the sample's shape in time, as a trim on the start of the note.

1. **New `build/early_fills.json`:** `{track: {onset qn: dB}}`, read like `note_trims.json`. In `score_to_parts.py`, next to the c06 pitch-trim block (`vol_parts.append(("note", ...))`), add a part `("early", sq, dB)`. In `vol_db` this part:
   - ramps from 0 at `sq - 0.02 qn` to +dB at `sq + 0.05 s`;
   - holds to `sq + 0.35 s`;
   - returns to 0 by `sq + 0.6 s`.

   Convert the seconds with `qn_before`/`bpm_at` as the leads do. The value is the measured sag minus 2, capped at 8:
   - Flute 1: 111: 8, 118: 6, 132: 7, 134: 5, 189: 6, 198: 4, 250: 4, 256: 3.
   - Oboe 1: 47: 4, 56: 7, 59: 4, 140: 6, 143: 4, 189: 6, 262: 3, 270.5: 4.
   - Cor anglais: 98: 4, 134: 4, 135: 4, 136: 5.
   - Clarinet 1: 252: 4. Bassoon 1: 264: 4, 267: 3.
   - Horn 1: 39: 4, 176: 5, 182: 5, 184: 3, 188: 4, 199: 4. Horn 2: 252: 4, 258: 6.
2. **Horn F4: shaped pitch trims.** Change the F4 entries in `pitch_trims.json` (Horns 1-4, `"65"`) from a flat -5 to `{"early": 1, "body": -5}`: +1 dB to `sq + 0.35 s`, then -5 by `sq + 0.6 s`. `score_to_parts.py` then accepts either a number or this two-value form. Do not add F4 onsets to `early_fills.json`.
3. **Optional velocity test.** Do this only if a short range render is cheap. Render Fl1 qn 108-137 with legato targets at v80 instead of v60 (the `else` branch in the velocities block: `100 if sec < 0.45 else (80 if sec < 0.9 else 60)` becomes `... else 80`). If the median join dip falls from 4.9 to 3.5 dB or less, keep v80 for flute, oboe, clarinet and bassoon, and lower the fills by the measured gain.

**Check:** `fill.py "Flute 1,Oboe 1,Cor anglais,Clarinet 1,Bassoon 1,Horn 1,Horn 2"` shows no flat-CC11 target with a sag of 5 dB or more. `wjoin.py "Flute 1" 08 -v` shows qn 111, 118 and 132 at 6 dB or less. `leg.py` crossover medians stay within 0.02 s of c07.

## 2. Violas: slur-to-slur joins in the running accompaniment figures dip twice as deep as joins inside a slur (Leg BC MAX, about 9 dB against 4-5 dB)

**Where.** Violas, at every slur boundary of the slurred triplet and eighth-note accompaniment:
- bars 37-40 (qn 108-124) and 57-58 (qn 186-196), triplets under the flute and horn solos;
- bars 71-78 (qn 238-262), "unis., ord." eighths in three-note slurs, pp-p, under the Vln I tune;
- bars 2 and 16-21.

**Measured** (20 ms envelope; join dip = the louder of the two neighbouring levels minus the minimum within -0.15 to +0.25 s):

| Passage | Leg Slur joins | Leg BC joins |
|---|---|---|
| qn 238-262 | 4.8 dB (31) | 9.3 dB (14) |
| qn 108-124 | 4.6 (37) | 8.6 (7) |
| qn 186-196 | 3.9 (18) | 8.2 (5) |
| qn 0-70 | 4.2 (5) | 8.2 (6) |

- Over the whole movement the BC-minus-Slur difference is +3.0 dB for violas. It is +1.5 for Vln II, +0.7 for Vln I and 0.0 for Vc.
- Timing is not the cause: viola BC crossovers in qn 238-262 are -0.04 to +0.14 s (`leg.py`).
- Example, qn 244 (G flat 4 -> C4): the level falls from -48 to -60 dB at the bow change, stays there for about 0.3 s, and climbs back to -55.
- Inferred: these are the Violas Leg BC MAX transition samples at soft CC11 (CC 34 here).

**Inferred.** A soft accompaniment figure that is slurred in groups gets a hole of about 9 dB at every group boundary, which is every beat or half bar. It pulses, where it should be a smooth bed. A real viola section changes bow there almost without a gap at pp.

**Fix (`score_to_parts.py`, the c02 Leg BC block, `if has_bc:`).**
- On `Violas` only, when the target `o` lasts less than 0.8 s and `base(o["qn"]) <= DYN["p"] + 6`, keep `o["art"] = "Leg Slur MAX"` (do not set Leg BC MAX).
- Still set `o["bc_from"] = id(n)`, so the note-length block overlaps the notes by `LEG_OVERLAP`.
- Add the pp bow-change notch: `notches.append((o["qn"], 8))`, the same depth as the c04 pp notch.
- This keeps the bow change audible as a small dip without the BC sample's hole.
- Longer viola notes and louder passages keep Leg BC. Do not change the other string sections.

**Check:** the `bcx.py` method on Violas, qn 238-262: slur-boundary dips of 6 dB or less, with no change inside the slurs.

## 3. Viola pizzicato F4 is about 10 dB hotter than the rest of the pizz. line under the cor anglais solo (bars 41-44)

**Where.** Violas, qn 124-140: pizz. triplets at p, under "CA solo, dolce cantabile". Smaller cases: Vc pizz. B flat 2, Cb pizz. A2.

**Measured.** RMS over the first 0.12 s of each pizz. note against the track median (-49.0 dB):
- Violas:
  - F4 (65) +10.1 (3 notes: qn 124.67 -35.0, 128.67 -33.8 and 131.67 -42.8 dB peak);
  - G flat 4 (66) +2.8;
  - G flat 3 (54) -5.1, B flat 3 (58) -3.9.

  The line spans 15 dB at one printed dynamic, with one constant velocity curve (v53-63).
- Vc B flat 2 (46) +6.3 (2 notes). Cb A2 (33) +6.4 (1 note, inferred).

**Inferred.** At p under a solo, two of the three F4s stick out as accents that are not printed, about once a bar.

**Fix.** `pitch_trims.json` currently applies only to Leg articulations, or to all articulations with `_all_arts`. Add a key `"_arts": ["Pizz RRx4", "Pizzicato RRx4"]`. A track entry with it applies its trims only to notes on those articulations: change the condition in the c06 pitch-trim loop to `allart or art in arts_list or "Leg" in art`.
- Violas: `{"65": -8, "66": -2, "54": 4, "58": 3, "_arts": ["Pizz RRx4"]}`.
- Violoncellos: `{"46": -5, "_arts": ["Pizzicato RRx4"]}`.
- Because pizz. dynamics come from velocity, the volume-envelope trim changes only level, not timbre. That is what is wanted here.

**Check:** the per-pitch pizz. table (inline script in this report's scratch history; it is the c08 `bodies.py` method on the first 0.12 s) has every viola pizz. pitch within ±4 dB of the median.

## 4. Violin I "solo, senza sord." (bars 17-22) is still a 16-player section; memory now allows the DIV A patch

**Where.** Violins I, qn 48-65. The only printed string solo in the movement.

**Measured.**
- Unchanged since c07 A #4: `SOLO_BOOST` +8 CC on the 1st Violins KS Master. No solo violin library is installed.
- What changed is memory, the reason it was deferred. A fresh load is now 49 GB with 0 GB compressed, before and after the c07 render (`cycles/c07/metrics/memory.txt`). The deferral was decided at 65 GB with 51 GB compressed.
- The patch exists: `/Volumes/MAC DRIVE/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/1st Violins Divisi/04 Legato Slur + Port/1st Violins Leg Slur MAX DIV A.oib`.

**Inferred.**
- A half section is still not one player.
- Of the patches installed, it gives the solo the thinnest, most soloistic timbre: fewer players, less chorus.
- It also makes the bar 22 "tutti" entry at qn 65 a real change of texture.

**Fix.** As c07 A #4:
- Append a 28th track, "Violins I solo", at the end so stem numbers stay, with the DIV A Leg Slur MAX patch and the Vln I seat.
- Give it qn 48-65 of VlnI, with Vln I silent there.
- No `SOLO_BOOST` and no con sord. on this track.
- Build it with `--midi-only` for the other 27 tracks, then restart REAPER and render with the compression gate. If REAPER is over about 55 GB after the restart, drop it again.

**Check:** the bar 17-22 spectral centroid and level against the bar 23 tutti, and the c07 crossover check on the new track.

## 5. Checked and fine (measured)

- **Legato timing:** crossover medians are Fl1 0.043, Ob1 0.038, CA 0.003, Cl1 0.043, BCl 0.073, Bn1 0.063, Hn1 0.033, Vln I 0.013, Vln II 0.023, Vla 0.043 and Vc 0.033 s (`leg.py` on c07).
- **No chords on a monophonic legato patch:** no two notes overlap by more than 0.1 qn at one onset, or by more than 0.25 qn, on any Leg articulation (`chords_leg.py`).
- **Keyswitches:** every keyswitch comes 0.03-0.06 qn before its note. The only switches during a sounding note are Leg Slur <-> Leg BC switches inside the legato overlap, as designed, plus Tbn1, Timp and the two Largamente joins, each 0.06 qn before the next onset.
- **Viola sextuplets, bars 59-60** (Sus MAX, 0.03 qn crossfades): per-note ripple median 5.0 dB, below the 6.4 dB of a held viola note at pp. Keep them on Sus.
- **Harp harmonics** (bars 82-83) sound at the printed sounding pitch: 311.3, 347.2, 414.6, 521.5 and 621.8 Hz for E flat 4 to E flat 5 (FFT of the stem).
- **The Cb pedal** "change bow at will" (qn 220-238, 18 qn on one note) holds at -61 to -63 dB with no decay or seam. Vla/Vc/Vln II long notes at qn 274-305 are steady too.
- **Bar 63:** the sf > p tremolo falls 12 dB over the bar in Vln I, and the Tbn1 marcato solo is on top (-26 to -28 dB).

Do not touch: the Leg Slur/Leg BC split for Vln I, Vln II and Vc, and its v124 velocity; the viola sextuplets on overlapping Sus MAX; the legato leads (crossovers are on time); the c07 Largamente portato joins; the flat F4 *body* level of -5 dB (finding 1 changes only the start of the note); the harp harmonics track; the pizz. velocity curve; the bow-mark and same-pitch notches.
