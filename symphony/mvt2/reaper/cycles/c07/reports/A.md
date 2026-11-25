# Cycle 7, critic A: articulation and phrasing (on the cycle 6 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c07-A/` and run with `~/.venvs/claude-composes-reaper/bin/python`. `lib.py`, `arts.py` and the other c06-A scripts are copied there, with the default cycle set to 06. The new ones:
- `joins.py <cyc> q0 q1 [thr]`: every note change without a rest, on every track, in a qn window. It reports the dip at the join (60 ms power-smoothed envelope) against the bodies on either side.
- `susjoin2.py <cyc> "Track,..." [-v]`: the same check for every connected note on a non-legato Sus patch, over the whole movement.
- `bcbump.py <cyc> [-v]`: for string legato targets of 1.4 s or longer, the peak in the first 0.5 s against the note body and against the level before the note.
- `slurart.py`: printed slurs against the articulation each note got. `portato.py`: note-by-note levels in a window.

**About the c06 render.** Its onset timing cannot be trusted: entries are 0.2-0.3 s late (CHANGES.md, attacks.txt). Every timing-sensitive number below was measured on c05 too, whose timing was good, and is given for both renders. In the windows used here, the note structure in parts.json is the same in c05 and c06. A 10 ms envelope gives false dips of 5-10 dB on bass notes, because the waveform itself ripples at that window length. All join numbers here use the 60 ms smoothed envelope.

## 1. Bars 61-62 (Largamente, ff): the woodwinds' tenuto half notes are re-tongued with 6-14 dB holes at the main climax

**Where.** qn 204-212, Flute 2, Oboe 1, Clarinet 2, Bassoon 2 (and Cl1, Bn1, BCl, which play the same pattern).

**Measured.** In bars 61-62 every wind and brass part has tenuto half notes, under "Largamente" and with the strings marked "molto sostenuto". Flute 2 and the other upper winds have the tenutos inside a long slur, which makes them portato. `score_to_parts.py` handles them in two ways:
- A tenuto inside a slur goes to Sus MAX (the c04 A #4 rule).
- A tenuto at mf or louder ends 0.03 qn early (`e0 - min(0.03, 0.1*dur)`).

So each half note is a gap followed by a fresh ff Sus attack. Dips at the join (`joins.py`, c05 / c06):

| Note | c05 | c06 |
|---|---|---|
| Fl2 qn 206 (80 -> 85) | 8.7 dB, minimum at +0.31 s | 10.7 |
| Fl2 qn 208 (85 -> 89) | 12.2 dB, at +0.13 s | 14.1 |
| Ob1 qn 208 (77 -> 77) | 8.0 | 8.8 |
| Cl2 qn 208 | 6.8 | 9.0 |
| Bn2 qn 208 | 5.7 | 6.4 |

In c05, the brass (Tbn2, BTbn, Tuba, Hn3/4) at the same joins dip less than 5 dB. The large brass dips in c06 (17-22 dB at +0.45 s) come from the late render, not from parts.json. Flute 2 is the second-loudest stem in bar 62 (-31.5 dB).

**Inferred.** A real wind section plays tenuto under "Largamente / molto sostenuto" at ff broad and joined, with at most a slight pulse. A hole of 8-14 dB on every beat of bars 61-62 breaks up the climax in the highest and most audible voices.

**Fix (`tools/score_to_parts.py`, `build_track`).**
- Add `SOSTENUTO_SPANS = [(204.0, 212.0)]`, from the Largamente bars (the winds have no "sostenuto" text of their own).
- Wind/brass articulation branch (`elif n["slur"] is not None and near(q, ten_q)`): inside a sostenuto span, a portato note whose pitch differs from the previous note stays on `Leg Slur MAX` (Leg Slur on clarinets) and becomes a legato target. Add a CC11 notch of 10 CC at its onset: append `(q, 10)` to `notches`, which is currently filled for strings only; `notch()` already works for any family.
- Note-length block (`elif near(n["qn"], ten_q) and not (...)`): inside a sostenuto span, winds and brass end at `e0` with no gap if the next pitch differs. A repeated pitch (Ob1 208, 77 -> 77) ends at `e0 - 0.01` qn and gets `ENTRY_LEAD_S`-style lead of 0.04 s and velocity of at least 100.
- **Check:** `joins.py 07 200 212 4` shows no wind join in qn 204-212 deeper than 4 dB.

## 2. Viola div. (bars 23-29): each new double stop on Sus MAX opens a 4-8 dB hole about 0.2 s after the beat

**Where.** Violas, qn 66-87. "div.", p and mf, two-note chords on Sus MAX (polyphonic, so they cannot use the legato patch).

**Measured** (`susjoin2.py 05 Violas -v`, smoothed):
- qn 69: 7.4 dB at +0.25 s. qn 71: 6.6 at +0.19. qn 78: 6.8 at +0.26. qn 82: 7.5 at +0.24. qn 70 / 80: 4.5 / 4.2.
- The previous chord ends exactly on the new onset, or 0.03 qn before it on repeated pitches. The new chord has no lead.
- c06: 12 of 26 joins are 6 dB or deeper and 6 are 9 dB or deeper (median 5.6), worse because of the late render.
- The same shape at the celli div. entry at qn 53 (bar 18.7): 9.4 dB at +0.46 s in c06. That is the open c06 A #3 item.
- For comparison, the other non-legato Sus lines are fine with the smoothed envelope:
  - Cb (74 joins): median 2.2 dB, 3 of 74 at 6 dB or more.
  - Cl2 0.4, BCl 0.3, Bn2 1.0, Hn3 1.1, Hn4 1.9.

**Inferred.** The soft Sus MAX attack blooms in 200-300 ms, while the old chord is already in release. The divided violas' accompaniment chords under the violin tune in bars 23-29 pulse with a gap on almost every change.

**Fix (`score_to_parts.py`, the c06 A #3 branch in the leads loop: `elif family == "string" and n["art"] == "Sus MAX" ...`).**
- Widen the condition from "previous note on a Leg articulation" to "any previous note on the track that ends within 0.1 qn of this onset, with no rest". Exclude `short_sus` notes and notes at f or louder.
- These notes then get `ENTRY_LEAD_S["string"]` (0.12 s at CC11 ≤ 50, 0.06 s above), the CC11 pull, and velocity of at least 105, exactly as A #3 does now.
- In the note-length block, a Sus MAX string note followed by such a chord ends at the next chord's **score** onset + 0.03 qn, for a crossfade. Do not cut it at the moved onset.
- Apply this to Violas and Violoncellos only. Cb measured fine.
- **Check:** `susjoin2.py 07 Violas`: median 3 dB or less and nothing over 6 dB in qn 66-87. Vc qn 53 at 4 dB or less.

## 3. Soft Leg BC MAX targets at v124 bump 5-8 dB over the note, about 0.3-0.4 s after the bow change (con sord. accompaniment, bars 15-21)

**Where.**
- Violins II, qn 48 and 57 (bars 17 and 20, pp con sord., under the Vln I solo).
- Violas qn 48 and 148, Vc qn 45, 60, 164, 180.

**Measured** (`bcbump.py`):
- Vln II qn 48: the peak in the first 0.5 s is +7.4 dB over the note's body and +12.8 dB over the quarter note before it. qn 57: +6.5 / +12.9. `portato.py` puts the maximum at +0.39 s.
- CC11 does not cause it: CC 38 -> 39 at qn 48.
- Medians over all Leg BC targets of 1.4 s or longer: Vln II +4.1 (c05) / +3.3 (c06); Vla +4.7 / +3.8; Vln I +4.0 / +2.6; Vc +2.9 / +1.2.
- Notes at 5 dB or more: c05 11 of 31 (Vln II), 6 of 14 (Vla), 12 of 43 (Vc).
- Leg Slur MAX targets in the same tracks: medians +2.5 to +3.6.

**Inferred.**
- At v124, Leg BC MAX plays a fast, firm bow-change transition. Velocity sets transition speed (HO manual, True Legato, about lines 3401-3412).
- At pp under a solo, this reads as an accent at every bar line of the Vln II "half + tenuto quarter" figure. It is the opposite of the soft portato printed there.
- The high velocity was chosen in c02 for timing, so keep it and cancel the bump with CC11.

**Fix (`score_to_parts.py`, `contours`/`contour()`).**
- Add a kind "bcsoft" for Leg BC MAX targets with `base(q) <= DYN["pp"] + 6` (CC ≤ 40) and a note of 1.4 s or longer.
- CC11 shape: 0 at the onset, -7 CC from onset + 0.15 s to onset + 0.5 s (convert seconds with `bpm_at`), back to 0 by onset + 0.9 s.
- **Check:** `bcbump.py 07 -v`: Vln II qn 48/57 peak-body 3 dB or less. Re-run `leg.py` to confirm crossovers do not move.

## 4. Vln I "solo, senza sord." (bars 17-22) is played by the full 16-violin section

**Where.** Violins I, qn 48-65.

**Measured.**
- The text is honoured only as `SOLO_BOOST` (+8 CC) on the 1st Violins KS Master.
- The installed volumes hold no solo violin. The manual lists EW Hollywood Solo Violin, but it is not on `/Volumes/MAC DRIVE`.
- The thinnest violin sound installed is the half-section divisi set: `Hollywood Strings Opus Instruments/1st Violins Divisi/04 Legato Slur + Port/1st Violins Leg Slur MAX DIV A.oib`, or `06 Keyswitch/1st Violins KS Master DIV A.oib`.

**Inferred.** This is the only printed string solo in the movement, answered by the oboe and supported by muted Vln II/Vla/Vc. A full section with a CC boost sounds like a tutti, not like one player. The difference is in timbre, not level, so no CC or trim can produce it.

**Fix, only when memory allows.**
- At 10:22 today, REAPER held 65 GB, with 51 GB of it compressed, and 0.66 GB was free. Do not add this while those conditions hold.
- When memory allows: append a track "Violins I solo" (last, so stem numbers stay) with the DIV A Leg Slur MAX patch. Give it qn 48-65 of VlnI, with Vln I silent there. Drop `SOLO_BOOST` for it, and use the Vln I seat, closer mic, and con sord off.
- Of the deferred divisi tracks (Celli DIV B, Viola div.), this one changes the most per instance added.

## 5. Big leaps "sul G / sul C / sul A" are played as plain slur legato; Leg Port MAX is already loaded in the KS Masters

**Where.**
- Vln II qn 218 (bar 64.5, "sul G", 76 -> 62, down 14 semitones).
- Vla qn 286 (bar 87, "sul C", 60 -> 53).
- Vln I and Vln II qn 172 (bar 53, "sul A", 72 -> 77).

**Measured.**
- `cc70` already holds the string under each marking (finger-position script).
- `Leg Port MAX` is a keyswitch in every KS Master: Vln I 49, Vln II 46, Vla 43, Vc 89. So using it costs no new instance.

**Inferred.** A leap marked to stay on one string is a shift, and a Romantic Adagio player lets that shift be heard as a slide. With only five such notes this is a small, low-risk gain in style.

**Fix (`score_to_parts.py`, string articulation branch).**
- Add `PORT_NOTES = {"Violins I": [172.0], "Violins II": [172.0, 218.0], "Violas": [286.0]}`.
- Those legato targets get `ks_lookup(stem, "Leg Port MAX")`, with a keyswitch at `early_time` and a velocity of about 70. Velocity sets the slide speed, and lower is slower.
- Every other note keeps Leg Slur / Leg BC.
- **Check:** `leg.py` shows the crossover within 0.25 s, and the next note returns to Leg Slur MAX with no hole.

## 6. Checked and fine (measured)

- **Double bass Sus MAX line:** median join dip 2.2 dB (c05, smoothed).
- **Clarinet 2, bass clarinet and bassoon 2 unslurred lines; Horn 3/4 held notes:** join medians 0.3-1.9 dB.
- **Timpani roll chains:** tied eighth endings at qn 8, 203, 211 and 237 merge into the roll with no extra stroke. The opening roll sounds from qn 3 in both renders (-57 to -61 dB).
- **Con sord. (CC15):** placed in the rest before each "con sord." text for strings and for Horn 3/4.

Do not touch:
- The c06 pre-roll and the bar-0 opening checks.
- The Leg Slur/Leg BC split and its v124 legato velocity (only cancel the soft bump with CC11, finding 3).
- The c04 portato-to-Sus rule outside the Largamente bars (finding 1 is limited to SOSTENUTO_SPANS).
- The string same-pitch merge with notches, and the c06 bow-mark notches.
- Tbn1's marcato accents (+1.3 to +3.3 dB in c05).
- Harp rolls and ring.
- Cb Sus MAX joins (no lead needed).
