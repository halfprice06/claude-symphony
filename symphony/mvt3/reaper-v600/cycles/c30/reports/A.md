# Cycle 30, critic A: articulation and phrasing (on the c29 render)

Sources: the c29 stems and master (`cycles/c29/render/`), `cycles/c29/parts_rendered.json` against `cycles/c28/parts_rendered.json` and the c28 stems, earlier stems back to c25 where a join needed a history, `cycles/c29/CHANGES.md`, `build/mockup-events.tsv`, `build/score_config.py`, the score (pages 7, 11, 14), the May 2021 HO manual and `loop/MANUAL-GAPS.md`. All numbers come from my own scripts (scratch, now deleted). Unless stated otherwise, a level is 200-6000 Hz band power in 40 ms frames, and a join "dip" is min(level 0.2-0.55 s before, level 0.3-0.65 s after) minus the minimum over -0.15..+0.35 s, with 100 ms smoothing (the c29 actor's `jt29.py` measure). "Measured" means a number from these files; "inferred" means a cause or an outcome a render still has to confirm.

This is the last cycle, so only finding 1 is proposed as a change. Findings 2-5 are listed with their measurements and left for later.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 30 (its plan ends at cycle 20), so there was no assigned reading. I read the pages behind my findings and `loop/MANUAL-GAPS.md` (Finale results c02-c28).

| Manual (May 2021 HO, page) | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.109, woodwind Sustain / Sus Expressive | Sustain dynamics come from the Mod Wheel, all 3 dynamic layers start together; the Expressive variant has a slower attack and growing vibrato. | Bassoon 1's solo (qn 456-496) on the BS KS Master's "Leg Slur Exp" | Partly. The row's slow attack shows on two legato targets that never reach their body (finding 1). The sustain-row targets of this solo (459, 460, 499, 507) reach body on time. |
| p.111-112, woodwind Legato Slur | A slur forms only with no gap and an interval of an octave or less; the patch starts 3 sustain samples and uses separate slur samples. | Bassoon 1 464 (D4 to A4, a fifth) and 475 (C4 to E flat 4) | Yes, both are slurred within an octave. The holes are inside the slur samples' crossfade, as MANUAL-GAPS c22 found for the other woodwinds (velocity did not change them). |
| p.105-106, brass Legato Slur / Legato Slur Accent | Volume on the Mod Wheel, velocity sets transition speed; Legato Slur Accent adds an accent at the attack, its strength by velocity. | Trumpets 1-2 at 968-984 (now "Sus Non Vib MAX" crossfades), Trumpet 1 at 840-856 (finding 4), Horn 1 818 | The c29 sustain-row crossfades replaced the legato row at 243; Leg Slur Accent (gap #1) is still untried and should stay untried in the final render. |
| p.106, Mutes | Muted brass patches cover several articulations; the 1TP KS Master here has only "Mute Sus", "Mute Sus Accent", "Mute StacSs DblTng RRx9" (MANUAL-GAPS c12) | Trumpet 1 con sordino, 680-792 | Yes. No muted legato row exists, so the c29 per-pitch gains are the instrument-side tool used. |
| MANUAL-GAPS #6 / c13 (round-robin reset, p.34, p.145) | A reset changes every later round-robin choice on that track up to the next reset. | Basses' repeated G at 600-608, 654-658 (finding 5) | Why finding 5 is left for later. |

## Ranked findings

### 1. Bassoon 1's solo (bars 116-119): the E flat 4 at qn 475 sounds 10 dB under the line for its whole quarter, and the mp arrival A4 at 464 sags 7 dB for 0.3 s (measured). Proposed fix.

**Where.** Bassoon 1, "solo, espress.", p, bars 115-122 (qn 456-496), on "Leg Slur Exp". 475 is the slurred C4 to E flat 4 after the held C4 of 472; 464 is the D4 to A4 leap at the mp goal of the crescendo from 461.

**Evidence (measured).**
- 475, stem: -46 dB before, -55..-58 from +20 to +340 ms after the beat, -47 only from +380 ms, which is the arrival of the next note (476's note-on is at 475's +0.29 s). Pitch check (first 3 harmonics, 80 ms windows): E flat 4 at +2..+7 against C4 at 16 before and D4 at 16-17 after. So the E flat sounds about 10 dB under its neighbours for the whole note. Stem dip 10.5 dB; master dip 5.2 dB (-44 to -47..-52), with the bassoon only 1.5 dB under the master's band level there (it is the solo).
- 464, stem: -48 before, -51..-55 from +20 to +260 ms, back to -48 at +380. A4 harmonics rise from 7-8 at the beat to 16 at +0.35 s. Stem dip 7.0, master dip 7.2 dB: the deepest master dip of any exposed legato join in the piece.
- Deterministic: 464 / 475 dips 7.7 / 10.5 (c25), 7.0 / 10.5 (c26, c27, c28, c29). c13 critic A measured the same note (475 at -53.1 against -42.8 / -45.0) and it was fixed with a +6 dB per-note envelope shape, which Dan's 11 Nov rule removed. It needs the instrument-side fix.
- The fix already works on this track: the variant-C sustain-row targets of this solo (459, 499, 507) now dip -2.1 / -2.1 / -1.4 dB, and the legato notes that follow a sustain-row target (461, 500, 508) dip 3.7 / 3.7 / 2.5 dB. The same c23 form cured Oboe 1 384 / 964 / 1014 and Clarinet 1 606 / 998 / 1014 (all under 6 dB).

**Fix (`build/score_config.py`, config only; "Sus MAX" is already loaded on this track, so no Opus state change; Bassoon 1 needs only a MIDI rebuild).**
- `_C26_RUNS["Bassoon 1"]`: weak targets `(459.0, 460.0, 499.0, 507.0)` -> `(459.0, 460.0, 464.0, 475.0, 499.0, 507.0)`. Variant C then puts each on "Sus MAX" (ART_SPANS ±0.1 qn), leads it 0.06 s (`onset_lead` `set`, rows Sus) and overlaps the previous note by 0.011 s (`gap_set` `only_at`).
- In the c26 "bn" block, remove 464.0 from `_bnq` (its `onset_lead` 0.06 s and its `vel_cap` Leg 100) and remove the `note_end` entry 463.678 (`early_s` -0.09), so variant C alone sets 464's lead and overlap, as at 459 and 499. Leave 468, 480, 500, 503 and 508 as they are.
- Velocity: the existing targets play at the dynamic's velocity (v53 at p). Check in `build/parts.json` that 475 (p) and 464 (mp) come out at the same kind of value and not at the legato v100 (inferred: a v100 note on the sustain row may tongue the slurred note).

**Pass (on the c30 stem and master):** 464 and 475 stem dips 4 dB or less and master dips 3 dB or less; the E flat at 475 within 4 dB of the D4 at 476 over its own quarter; 466 and 476 (the notes after) dip 4 dB or less; no other note in 456-496 moves by more than 1 dB on the stem. If 464 fails and 475 passes, keep 475 only.

### 2. Cor anglais 701 and 734 (bars 176 and 184): the F4 after G4 on the sustain row sits 5-6 dB low for most of its quarter (measured). Left for later; keep c29.

- Both are the same G4 to F4 step. On "Sus MAX" at v53 the F4 plays at -51 / -49 dB and reaches -45 / -44 only 0.28-0.38 s after the beat (about the next note's arrival). Stem dips 6.6 / 5.3, master 3.6 / 3.0. Nothing else sounds there (Trumpet 1 is silent at 699-706 and 732-736; the next stems are 10 dB down).
- c29 is still the better version: in 699-741 the master dips of 3 dB or more were 706 5.0 and 740 3.5 in c28, and are 701 3.6 and 734 3.0 now; the cor anglais bars 176 / 184 are 3.2 / 3.9 dB louder and now level with bars 177 / 185 (the legato row had sagged).
- Possible later fixes, both untested: a +3 dB F4 region gain on the cor anglais "Sus MAX" (an Opus state change, full rebuild, and it also lifts the other F4 notes of 683-740), or a longer lead on F4 only (it would lengthen a two-pitch overlap in a soft solo). Neither is low risk for the final render.

### 3. Trumpets' ff accented quarters at 362 / 366 (bars 91-92): now separate from the pickup, but they reach their body 100-140 ms after the beat (measured). Left for later; keep c29.

- c29 (lead 0.02 s, pickups v82): the quarter's body is 7-10 dB over the pickup's peak, so the two notes are heard apart (Trumpet 3: pickup -39, valley -42, quarter -32). Body minus 3 dB is reached at +100 ms (Trumpet 1), +120 (Trumpet 2), +140 (Trumpet 3) at 362; at 1106 at +45 / +50 / +90 ms.
- c28 (lead 0.05 s, pickups v95): the body was already there from the pickup on (-160 ms), with no separation (0.7 dB).
- A lead between the two (0.035-0.05 s with the v82 pickups) might keep both, but nothing has measured it, and the passage is a tutti ff where the strings and winds carry the beat. Not for the final render.

### 4. Trumpet 1, theme B at bar 211-212 (qn 844): a 10 dB, 0.2 s hole on the Leg Slur MAX join C sharp 5 to F5 (measured). Left for later.

- Stem: -21 at -0.1 s, -34 at +0.1 s, -28 at +0.18 s; master dip 4.3 dB. Trumpet 2 doubles the line a third below.
- The measured cure on this row is the c29 bar-243 form (the whole slur 841.6-855.9 on "Sus Non Vib MAX", 0.10 s crossfades, v95). At 243 it also raised the legato notes 4-7 dB. Here the trumpets already lead the next stem by 5-9 dB in every 2 qn window of 840-856 (e.g. 846: Trumpet 1 -25.3, Trumpet 2 -26.4, Clarinet 1 -32.9), so the same change would push the pair 10-15 dB over the texture unless CC1 / CC11 are re-fitted, which needs a range test. The coordinator also deferred this in c29.

### 5. Basses' ff repeated G pedal, qn 600-608 and 654-658 (bars 151-152, 164-165): every other repeat has no gap and arrives late (measured). Left for later.

- 30-300 Hz on the stem: 604, 608 and 658 dip 11-13 dB and recover in 0.1 s. 602, 606, 630 and 656 have no dip; the new note rises from -43 to -32 dB over 0.25-0.35 s (a slow bow-direction take on "Sus MAX", v91, 0.03 qn gaps). On the master's low band those repeats show no dip. Unchanged since c26 (identical data and stems in c28 / c29). The celli above them separate (c26 resets).
- A round-robin reset or a per-repeat lead would change every later take on the basses (MANUAL-GAPS c13: 73 notes moved by 2 dB or more after one reset). Not for the final render.

## Checks the coordinator asked for (c29 against c28)

- **Trumpets 1-2 at bars 243-246: keep as rendered, no trim (measured).** The score prints f with a < > hairpin on every tied note (970, 973, 978) under "molto espr.", with Horns 1-2 ff on the same line and the strings mf "cresc. molto" to the ff of 247. Trumpet 1 per 2 qn, c28 -> c29: 970 -38.5 -> -34.3, 972 -37.8 -> -34.7, 974 -34.8 -> -32.3, 976 -34.0 -> -33.0, 978 -45.2 -> -36.7 dB (the 978 hole is gone). The trumpets now sit 2-4 dB over Violins I / II and within -3..+2 dB of Horn 1 (ff, -31..-35). The master over these bars is +0.4..+1.4 dB over c28 and still climbs into 247 (bars 243-247: -26.2, -24.2, -23.8, -23.2, -21.5 dB). CC11 on the legato notes is 94-98 against the head's 95, so the extra level is the sustain row no longer sagging, not a louder dynamic.
- **Cor anglais 701 / 734:** finding 2; keep c29.
- **Bar 166 stop 17.6 dB:** no articulation data changed near qn 664 (only the horn pans); 0.6 dB over the band is not audible as a change of release. Leave it.
- **Trumpet 3 pickups at 362 / 366:** the "3.0 dB" is the dip between pickup and quarter; the quarter itself is 7 dB over the pickup, so the notes are separate. Keep. Timing in finding 3.
- **Trumpet 1 989:** per-note p90 988 -40.3, 989 -36.5, 991 -33.2: 989 is +0.3 dB over the mean of its neighbours (target 0..+3). Met; Trumpet 2's 989 is unchanged.
- **Flute 1 at 168:** the window 168-169 is before the flute's first note (169); the harp harmonic (-51.6) and Horn 4 (pp, -53.2) sound there. From 169 on, Flute 1 leads by 4.7-10 dB per quarter (169: -47.2 against Horn 4 -52.5; 171: -47.7 against -54.8; 172: -44.7 against violas -54.5). Met.
- **Anything worse than c28 in my lens:** only 701 / 734 (above). Bar levels that moved 1.5 dB or more with identical notes, CCs and envelope: Bassoon 1 bar 116 -2.5 (one note, 462, -2.6; it was 5 dB over its neighbours in c28 and is now closer), Flute 1 bars 106-107 -1.7 / -1.9, Violins I bars 265 / 271 -1.7, violas 265 / 270 ±1.7, Bass trombone bar 103 +2.4, Bass clarinet bar 33 +1.8. These are render variance; none needs a revert. Every other change of 1.5 dB or more is a ruled c29 change (roles at 43-50 and 95-97, muted-trumpet pitch gains, the 243 crossfades, the ruling-8 carries on Violins I 474-478 and 896-900).
- **Accents (BRIEF 4):** 104 printed brass accents and marcatos in 880-1112: 2-5 kHz over the first 80 ms minus the body (0.15-0.5 s) median -10.3 dB, p90 -2.3, highest +4.2 (Trombone 2 at 1081). Weight without bite; unchanged from c28.
- **Repeated notes (S1):** the data in 792-840, 888-936, 984-1080 and 1088-1116 is identical to c28 apart from the trumpet pickups and CC7 carries. Same-pitch repeats (peak of the new note over the valley before it, 20 ms frames): basses coda 82 repeats median 10.1 dB (1 under 3 dB, 818.5), basses Più allegro 161 repeats median 13.0 (none under 3), Trumpet 3 Più allegro 30 repeats median 6.9 (none under 3), chorale violas 10.6, Horn 1 5.6, Horn 4 8.2. Keep.
- **Other movements' notes:** tenuto quarters on "Marc Lng RRx4" / brass Portato failing as downbeat carriers (scherzo c28): not used here; do not adopt now. Timpani Hrd KS with no way back to soft sticks without a second instance: applies (the pp "near the rim" strokes at 708 and the medium-stick span 856-1016 play hard sticks); leave. Mono From Left changing every note of that horn: Horns 1-4 use it since c25 and c29 measured the levels within 0.4 dB; keep. Leg Slur transition out of an accented unslurred note leaving the next head 6 dB under: the same mechanism c29 fixed at 243, 74, 146 and 578; Horn 1 818 stays on the legato row (rejected in the c29 range test). Woodwind figure gates on harmonics 2-5: a measurement note; my pitch checks use harmonics 1-3.

**Do not touch:** the c29 sustain-row crossfades (Trumpets 1-2 and Horn 1 at 968-984, cor anglais 698.9-741, Horn 3 146 / 578, Horn 1 74) and the trumpets' level at 243-246; the trumpet pickups at v82 with the 0.02 s quarter leads; the muted-trumpet pitch gains; Bassoon 1's other variant-C targets (459, 460, 499, 507, 320) and its "Leg Slur Exp" row; the gentle brass accents; the basses' "Stac On Bow RRx9" eighths and the coda / Più allegro repeat gaps; the chorale repeat gaps; the c28 items (edge carries, trim snap, trumpet solo CC1, Trombone 1 gaps).
