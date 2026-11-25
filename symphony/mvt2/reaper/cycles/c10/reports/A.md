# Cycle 10, critic A: articulation and phrasing (on the cycle 9 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c10-A/` (the c09-A set, defaulting to cycle 09, plus `ends.py` for phrase-end tapers and releases). Run them with `~/.venvs/claude-composes-reaper/bin/python`. Levels are dB re full scale on the c09 (pass 3) stems, and onsets are score onsets (`sq`). `wjoin2.py` gives two dips: "post" is the stem as rendered, "pre" is with the parts.json `vol_db` envelope divided out.

## What I checked that is working (measured)

- **Chords on legato patches:** no chord is sent to a monophonic legato patch (`chords_leg.py` finds none).
- **Divisi:** the Vc div. in bars 18 and 22 and the Vla div. play on Sus MAX.
- **Ties:** of 104 tied notes, none is re-attacked at the tie end.
- **Keyswitches:** every keyswitch lands 0.035-0.09 s before its note.
  - The Leg Slur/Leg BC switches inside slurs are sent while the previous note is held, which is the design.
  - No keyswitch clashes.
- **Mutes:** every string con sord./senza falls in a rest before the printed change.
- **Tremolo:** the climax tremolo (bars 61-64) sounds on all four sections. Levels per half-beat run -26 to -45 dB with no holes.
- **Timpani:** rolls start 2.5-4 dB over their body and then settle.
  - A tied roll end is absorbed into the roll, with no extra stroke.
  - The bar 82 stroke is damped by beat 3 (-85 dB at its end).
- **Harp:** it rings through its notated rests (0 to -6 dB 0.5 s after note-off). Release trails are on.
- **Phrase ends:** median taper is 1-6 dB, and releases fall 15 dB in 0.16-0.48 s.
- **Fast slurs:** the Vla slurred sextuplets (bars 58-59) on Sus MAX are even (±3 dB) and follow the crescendo (v83 -> v91).
- **Joins:** median join dips are 2.3-4.1 dB on every legato track.

## 1. The Violin I solo (bars 17-22, qn 48-65) is played by the 16-player section, enters slowly, and leaves a hole where the tutti takes over

**Where:** Violins I, qn 48-65, and the tutti entry at qn 65.

**What is wrong.** The score has "solo, senza sord." over the oboe's phrase, then "tutti (gli altri con sord.), espr., sul D" at qn 65.

The mockup plays the solo on the 1st Violins KS Master (16 players). Since c08 the only stand-ins have been CC1 +10 and the role [48, 65, -3] in `roles.json`. There are three problems:

**(a) Section sound.** The solo has the section's chorus. This is inferred: a solo line has a different timbre, not just a lower level.

**(b) Slow entries.** Both solo entries are slow to speak (measured, `shape2.py`, 20 ms steps from the score onset):
- qn 48: -71, -69, -68, -63, -62, -60, -58, -57, -55, then -49 at +0.3 s.
- qn 60: -67 to -61 for the first 0.2 s, -55 at +0.36 s, and -49 only at +0.6 s.

That is the soft section sample swelling in, and it reads as a late entry.

**(c) Hole at the tutti.** The c09 `fresh` rule cuts the solo's last note 0.03 qn before the tutti's moved onset, because the two must not legato-join on one monophonic patch.
- Measured at qn 65: -49, then -54/-56/-56/-56 from -0.1 s to +0.02 s, -51 at +0.06 s, -49 at +0.1 s, and -43 only at +0.36 s.
- That is a 6-7 dB hole of about 0.3 s exactly where the score passes the line from one player to the whole section.

**Fix: a separate solo track** (this is the "DIV A solo violin" that c08 deferred for memory). The patch is `/Volumes/MAC DRIVE/EW Hollywood Strings Diamond/Hollywood Strings Opus Instruments/1st Violins Divisi/04 Legato Slur + Port/1st Violins Leg Slur MAX DIV A.oib`.
- It is half the section (HO manual, 1st Violins (Divisi), Legato Slur). That is the closest thing on the drive to a solo, and much thinner than 16 players.
- It is a single-articulation patch, not a KS Master. If memory is still tight, use `1st Violins Leg Slur LITE DIV A.oib` in the same folder (inferred: LITE loads fewer layers).

Changes:
- `tools/score_to_parts.py`:
  - Route Violins I notes with `sq` in [48, 65) to a new track "Violin I solo" (family string, `first_art` "Leg Slur MAX", no keyswitches; the patch is single-articulation).
  - Keep the slur legato, leads and CC1 rules. Keep CC15 at 0 (senza sord.), and give it SOLO_BOOST (remove it from `SOLO_NO_BOOST` for this track only).
  - The main Violins I track rests from 48 to 65.
  - Drop the `fresh` cut at qn 65: the solo's last note (qn 63, E flat 5) keeps its full score length to 65.0, overlapping the tutti entry on a different instrument, as in the score.
  - The tutti at 65 keeps its entry lead, `entry_leads.json` 0.10 s.
- `build/roles.json`: remove Violins I [48, 65, -3].
- `build/mix.json`:
  - Add "Violin I solo" in the string group, at the same seat as Violins I (-0.55) and width 0.2.
  - Use Close + Main, with Close about 3 dB over the section's ratio, so it sits slightly forward like a soloist (inferred).
  - Start gain_db at the Vln I value minus 2. Balance it against Oboe 1 in bars 19-20 and against the Vln II/Vla accompaniment. The c08 target was the solo 1-2 dB under the oboe where they overlap, and about 4 dB over Vln II.

**Check:**
- The Vln I solo stem reaches within 4 dB of its body by +0.25 s at qn 48 and 60.
- At qn 65 the summed Vln I (solo + section) never falls more than 3 dB below its qn 64.5 level between -0.1 and +0.35 s.
- Attack gate 19/19.

## 2. Ten wind/horn legato joins still have 7-10 dB holes, and four of them lie *before* the score onset, where the early fill does not reach

**Measured** (`wjoin2.py`, dip post / pre; the 20 ms shape from `shape2.py`, with the time of the minimum relative to the score onset):

| Track | qn (bar) | step | dip post/pre | where the hole is |
|---|---|---|---|---|
| Clarinet 1 | 266 (80.3) | 82->80, v60 | **10.5 / 9.7** | -0.10 to +0.06 s (min -46 at 0.0; body -33) |
| Flute 1 | 270.5 (81.8) | 84->82, v80 | 8.8 / 7.7 | -0.06 to +0.06 s (min -56 at -0.04) |
| Horn 1 | 203 (60.75) | 66->65, v124 | 7.6 / 6.0 | -0.12 to 0.0 s (min -41) |
| Bass clarinet | 92.5 (31.8) | 56->60, v80 | 7.9 / 7.9 | +0.04 to +0.2 s (min -52) |
| Oboe 1 | 270 (81.7) | 73->72, v80 | 7.4 / 7.3 | +0.02 to +0.2 s (min -55) |
| Oboe 1 | 142 (45.5) | 73->75, v80 | 7.1 / 6.8 | +0.08 to +0.16 s (min -53) |
| Cor anglais | 132 (43.0) | 65->63, v80 | 7.2 / 7.3 | +0.02 to +0.3 s (-50..-53, body -45) |
| Cor anglais | 133.5 (43.4) | 63->65, v90 | 7.3 / 9.6 | 0 to +0.12 s (fill 4 in place) |
| Flute 1 | 128 (42.0) | 78->80, v60 | 7.6 / 6.5 | +0.38 to +0.42 s (-58) |
| Bassoon 1 | 231 (68.7) | 58->56, v60 | 7.9 / 7.8 | the whole note body, -58..-61 for 0.8 s against -52 before |

- The c08/c09 fill (`early_fills.json`, applied in `score_to_parts.py` after "c08 (A #1)") ramps from `sq - 0.02 qn` to full at `sq + 0.05 s`.
- In the first three rows the minimum lies 0.04-0.10 s *before* the score onset. The fill comes in after the hole.
- In those rows the pre-envelope dip is about the same as the post dip, so the hole is in the sample (the outgoing note's tail plus the transition), not in the envelope.

**Inferred.** These notes are the clarinet's top line in bar 80 (the reprise climax), the flute's descent into bar 82, and the cor anglais "solo, dolce cantabile" in bar 43. Each sounds like a small break in a slurred line.

**Fix:**

1. `score_to_parts.py`, early-fill block: accept an object value `{"db": X, "pre_s": P}`. The envelope is:
   - 0 at `sq - P - 0.03 s`;
   - +X at `sq - P`;
   - held to `sq + 0.10 s`;
   - back to 0 by `sq + 0.35 s`.

   Plain numbers keep the current shape.

2. `build/early_fills.json`:
   - Clarinet 1: `"266": {"db": 6, "pre_s": 0.10}`
   - Flute 1: `"270.5": {"db": 5, "pre_s": 0.06}`
   - Horn 1: `"203": {"db": 4, "pre_s": 0.10}`
   - Standard fills (dip - 3): Bass clarinet `"92.5": 5`; Oboe 1 `"270": 4`, `"142": 4`; Cor anglais `"132": 4`; Cor anglais `"133.5"` 4 -> 6.
   - Leave Fl1 128 alone: the dip is 0.4 s in, at the next transition's start.

3. Bassoon 1 qn 231 is a body sag, not a join. Add `note_trims.json` Bassoon 1 `"231": 4` (0.6 s ramp in).

**Check:**
- `WTH=6 wjoin2.py "Clarinet 1,Flute 1,Horn 1,Bass clarinet,Oboe 1,Cor anglais,Bassoon 1" -v`: each listed join is 5 dB or less post.
- No new bump: the shape over -0.2 to +0.5 s never rises more than 2 dB over the following body.

## 3. No portamento anywhere, although the score asks for one-string playing ("sul D", "sul A") on the movement's expressive rising leaps

**Measured (data).**
- The KS Masters carry a Leg Port MAX row: 1st Violins key 49, 2nd Violins 46, Celli 89 (`ks_maps.json`).
- No note in parts.json uses it.
- The c02 CC70 finger-position rule already keeps the "sul D/A/G/C" passages on one string (Vln I/II CC70 127 from qn 64.8 and 171.8).
- On one string, a rising fourth in a Romantic espressivo line is played with an audible shift slide. HO says the portamento articulation forms "a continuous pitch slide" (Opus Edition manual, Portamento script; Hollywood Strings Legato Portamento articulations).

The candidate leaps, from a scan of every Leg join of 5 semitones or more in those passages:
- **Vln I and Vln II qn 82 (bar 28.33):** F5 -> B flat 5. This is the top of the "espr., sul D" phrase, under the cresc. to mf.
- **Vln I qn 172 (bar 53):** C5 -> F5. This is the first leap of the "senza sord., sul A" entry.
- **Vc qn 83 (bar 28.67):** A flat 3 -> D flat 4, in the "cantabile" countermelody of the same phrase.

**Inferred.** These are the places where a real section would slide, and they are the melodic peaks of the two string tunes. At present every leap is a clean legato change, which reads as "sample". This is a small liberty the brief allows: it is what players do, and the score supports it with "sul D"/"sul A". Use it on these 3-4 notes only, never as a default.

**Fix (`score_to_parts.py`; a `PORT_TARGETS = {"Violins I": [82.0, 172.0], "Violins II": [82.0], "Violoncellos": [83.0]}` table):**
- Before each target, send the Leg Port MAX keyswitch at the same place the existing Leg Slur/Leg BC switches go (0.035 s before the moved onset, while the previous note is held).
- After the target's onset, switch back to the slur's articulation (the same place the next switch would go).
- Keep the target's overlap and lead. Velocity 100, not 124: velocity sets the transition speed, so the slide is audible but quick (HO manual p. 51 and the Legato Speed section).
- `build_reaper.py` loads every used row, so the row will be loaded.

**Check:**
- An f0 track (STFT peak in the 300-1000 Hz range) of the Vln I stem across qn 81.9-82.3 shows a continuous glide from about 698 to 932 Hz lasting 0.08-0.25 s, not a jump.
- The join dip (`wjoin2.py`) at these targets is no worse than now: Vln I 82 and Vc 83 are 7.2 dB and under.
- If the slide is longer than 0.3 s, lower CC5 (Legato/Portamento Time) on the track just for that note.

## 4. Exposed soft string joins still dip 8-11 dB for 0.3-0.4 s: violas in bars 73-76, Violins II in bars 20-21, the Vc cantabile in bars 26-29, and Vln I qn 67.5

**Measured** (`wjoin2.py`, post/pre equal, so the dips are in the samples):
- **Violas:**
  - qn 244 (bar 73, pp, Leg Slur 67->60): 9.4. The stem goes -50 to -58..-61 from -0.06 to +0.3 s.
  - 245.5: 7.5. 254.5 (Leg BC 65->58): 8.8, -39 to -50 for 0.25 s.
- **Violins II:** qn 59 / 60 (bars 20.7-21, pp con sord. under the Vln I solo): 8.3 / 8.2, -54 to -61 for 0.3 s.
- **Violoncellos:** qn 77 / 86 (cantabile, bars 26.7 / 29.7): 8.2 / 7.0. The Vc 77 dip is -50 to -56 over 0 to +0.2 s.
- **Violins I:** qn 67.5 (68->72, bar 23.5, the second note of the tutti espr. phrase): 8.5.
- Every other string join has a median of 2.8-3.6 dB, so these are the exceptions.

**Inferred.**
- A real section changing note under a slur dips by about 2-4 dB.
- 8-10 dB for a third of a second sounds like a missing note in an inner voice (bars 20-21, 73) or a hiccup in the tune (bar 23.5).

**Fix: early fills (the mechanism is not family-specific).** With the `pre_s` form from finding 2, because the string targets start 0.15-0.2 s early (LEG_LEAD_S) and the holes begin before `sq`:
- Violas `"244": {"db": 6, "pre_s": 0.06}`, `"245.5": 4`, `"254.5": {"db": 5, "pre_s": 0.04}`
- Violins II `"59": 5`, `"60": 5`
- Violoncellos `"77": 5`, `"86": 4`
- Violins I `"67.5": 5`

These sit in `early_fills.json`, outside the bcsoft and VLA_BC_SOFT CC rules, which stay as they are.

**Check:** `wjoin2.py "Violas,Violins II,Violoncellos,Violins I" -v`: these joins are 5 dB or less, and each track's median is unchanged within 0.3 dB.

## Also measured, not ranked

- **Vln II portato** (tenuto under slurs, bars 15-21) merges each repeated A flat with CC11 notches (38 -> 33 -> 40).
  - The stem moves 8-13 dB within a beat: -46 to -61 between qn 44.5 and 45.
  - Part of that is vibrato amplitude modulation: the median AM depth (`vib.py`) of Vln II long notes is 3.9 dB, and 6.2 dB on this note.
  - Not ranked, because the portato is audible as intended and the swing is near the sections' normal 4-6 dB AM depth. If finding 1 makes this passage more exposed, reduce the notch to 3 CC.
- **Phrase ends** (`ends.py`): strings and winds taper 1-6 dB into their releases; Bass clarinet (median 1.1 dB) and Horns 3-4 (1.2-1.5) taper least. No fix proposed.

**Do not touch:**
- The Leg Slur/Leg BC split with v124 for strings, the legato and entry leads, and VLA_BC_SOFT.
- The c08/c09 early fills.
- The same-pitch merge with notches.
- The tremolo keyswitch placement at bars 61-64 and the timpani roll table and settle.
- The harp release trails and roll timing.
- The tie handling.
- The CC70 sul D/A/G/C finger positions.
- ACCENT_DB 2 and the Tbn1 accents.
