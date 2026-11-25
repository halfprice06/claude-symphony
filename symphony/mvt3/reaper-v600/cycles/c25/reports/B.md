# Cycle 25, critic B (balance and levels), on the c24 render

All levels are from the c24 stems and master (`cycles/c24/render/`, timed on `cycles/c24/parts_rendered.json`). "K" means K-like weighting: a 60 Hz high-pass and +4 dB above 1.5 kHz, power summed over both channels, in 10 ms frames. Comparisons with c23 use `cycles/c23/render/` timed on `cycles/c24/before/parts.json`. Stems are dry; the R returns are separate. Scripts were in the scratch folder, which has been deleted.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 25: its rows stop at cycle 20, and the third round, cycles 13-20, set no fixed pages. So I skipped the full reading and read only the pages behind my findings and `loop/MANUAL-GAPS.md`.

| What the manual says (page) | Where it applies here | Does the render follow it? |
|---|---|---|
| In the LITE string instruments, CC11 sets overall loudness and CC1 sets dynamics and vibrato together. In the MAX strings and woodwinds, CC11 sets loudness and dynamics and CC1 sets vibrato. (May 2021 manual, printed p.62-63, repeated at printed p.150; the PDF page is about one higher.) | Violins I play "Sus Marc LITE" on the ff chords at qn 0, 4, 16, 20, 372 and 584, with CC1 98 and CC11 102-123. | Partly. The +4 dB `region_gain_db` on the LITE sustain groups assumed the LITE row sits 7-9 dB low (Movement I c55). Here the row came out 7-10 dB louder than c23 at the front (finding 1). On LITE, CC11 is pure loudness, so it is the right lane for trimming these chords. |
| Harp Sustain RR: velocity 1-123 alternates Pluck and Thumb Pick, 5 dynamic levels each; velocity 124-127 plays a Nail Pick (printed p.69; DIGEST section 10). | Harp, qn 524 (bar 132): a six-note ff chord at velocity 123, the top pluck layer. Arpeggios at qn 488-520 (p, median velocity 64) and 264-328 (mf, median 83). | The velocity path works (c22). The levels do not follow the printed dynamics: the p and mf passages measure the same, and the ff chord is 13 dB over the whole orchestra (finding 2). |
| VOLUME (CC7) sets each track's overall ceiling; Expression (CC11) shapes the line (printed p.150). | Every role row, `dyn_trim_db` and hairpin gain. | Yes. My fixes below are role rows over whole passages, velocity, and CC11 or CC1. None is a per-note envelope move. |
| MANUAL-GAPS #4, Mid instead of Close mics on the woodwinds, and #5, expressive rows for espr. solos. | The cor anglais espress. line at 864-872 and the muted-trumpet / cor anglais pair at 680-744 (findings 4 and 5). | Not used. They are still open. I propose role levels first, because these lines are hidden by 3-9 dB and a row or mic swap will not move them that far. |

## 1. Violins I's marcato chords now sit 6-10 dB over the rest of the strings (bars 1-2, 5-6, 94, 147, 277; c24 regression; measured)

**Where:** Violins I at qn 0, 4, 16, 20, 372, 584 and 1104 ("Sus Marc LITE" at v92, `onset_lead` 0.085 s).

**Evidence:** Plain RMS, first 0.3 s / 0.5-1.2 s after the beat.

| qn | Violins I c23 | Violins I c24 | Violins II c24 | Violas c24 | Master front c23 -> c24 |
|---|---|---|---|---|---|
| 0 | -33.0 / -29.8 | -25.0 / -25.4 | -30.2 / -30.6 | -31.4 / -31.9 | -21.7 -> -20.1 |
| 4 | -30.3 | -23.4 | -32.7 | -33.0 | -21.0 -> -19.9 |
| 16 | -34.1 / -29.7 | -24.9 / -25.4 | -32.2 / -30.6 | -33.1 / -31.8 | -21.9 -> -20.0 |
| 372 | -34.8 | -24.8 | -32.5 | -33.9 | -20.3 -> -19.0 |
| 584 | -32.5 / -30.3 | -22.4 / -26.0 | -31.9 / -28.3 | -30.6 / -31.0 | -18.9 -> -17.2 |
| 1104 | -35.9 | -26.4 | -34.1 | -27.5 | -14.7 -> -14.3 |

- The fronts rose 7.4-10.1 dB over c23. Violins I now lead Violins II and the violas, which play the same accented chord, by 5-10 dB at the front and 4-5 dB in the body.
- In c23 the three sections were within 2.5 dB of each other.
- At qn 372 (bar 94, the codetta with the trumpets) the Violins I front (-24.8) is 5.7 dB over Trumpet 1 (-30.5).
- In bars 1 and 5 Violins I alone (K -23.6) are louder than all the brass together (K -25.0). Every woodwind is 14-17 dB under them.
- Rimsky-Korsakov (Principles, p.33): in forte, Violins I equal two woodwinds and are about equal to one horn. Here they are about 10 dB over a horn (Horn 1 front -34.8).
- The c24 peak-timing gain (+475 -> +225 ms at qn 16) came from the row, not from the level.

**Fix (keep the row, v92, the lead and the CC11 step rows):**
- `build/mix.json` Violins I `region_gain_db`, row "Sus Marc LITE": `all_db` +4 -> 0.
- Add a `cc_scale` row (`INSTR_POST`, `build/score_config.py` c24 block) on Violins I over each marcato chord: -5 dB at k 20, for 583.6-586, 15.6-18, 19.6-22, -0.2-2, 3.6-6 and 371.6-374. On LITE, CC11 is pure loudness (manual p.62), so CC11 103-123 becomes about 57-69.
- Do not lower CC1 98, because on LITE it picks the layer.
- Targets: Violins I front within 3 dB of Violins II's front, body within 1.5 dB of c23 (bar 1 about -29.8 plain), master front at qn 0 and 16 back to about -21.5.
- Check on a range with the c24 T1 starts (-3, 263.25, 535.25). If a target is missed, measure and report it rather than adjusting it by hand.

## 2. The harp's dynamics are flat at p and mf, and its ff chord in bar 132 is 13 dB over the orchestra (measured)

**Where:** Harp, qn 524 (bar 132, six notes at v123, printed ff "non arpegg." inside a tutti f accent) and qn 488-512 (bars 123-128, the p arpeggio under the bassoon's dolce solo and the cellos' espress. line).

**Evidence, bar 132 (K, highest 50 ms in the first 0.4 s):**
- Harp -19.6.
- Next loudest: Timpani -32.1, Violins I -32.7, Violoncellos -32.6, Violas -33.0, Horn 3 -34.4.
- Master -18.5.
- So the master's attack in bar 132 is the harp's chord. In the per-bar table the harp is the loudest stem by 10 dB (`metrics.md`).

**Evidence, bars 123-128 (K):**
- Harp p arpeggio -45.4.
- Bassoon 1 dolce (the line) -47.8. Violoncellos espress. -47.3.
- The harp at mf in bars 67-82 also measures -45.4. At p in 936-952 it measures -45.0. So p sounds the same as mf.
- Rimsky-Korsakov (p.33): plucked strings are easily covered by sustained instruments, so an accompanying harp p should sit under a solo bassoon p.

**Fix:**
- In `parts.json`, through the harp's velocity rule in `score_to_parts.py` or a velocity row in `build/score_config.py`: the 524 chord at velocity 96 instead of 123. Through the c22 square-law velocity path that is -4.3 dB, and it moves from the top layer to the f layer.
- `build/mix.json` Harp `dyn_trim_db` ff +2 -> -2. This also touches the final chord at 1108, where the harp is already 15 dB under the master.
- Expected bar-132 peak about -28.5 K: still over the strings, about 10 dB under the master.
- `build/roles.json` Harp [488, 512, -6] -> [488, 512, -10] (a passage level): the arpeggio about 2 dB under the bassoon and cellos.
- Targets: the harp at 524 no more than 5 dB over Violins I's peak; the harp in 488-512 at least 2 dB under Bassoon 1.

## 3. The head of theme B (bar 211, qn 840) is 7 dB under its accompaniment; the hairpin gains of bars 209-210 run on into the ff downbeat (measured)

**Where:** The melody is Trumpets 1-2, Flute 1, Oboe 1 and Clarinet 1, cantabile ff from qn 840; also qn 856. The accompaniment is all other staves, printed ff > f on the downbeat.

**Evidence (K, melody sum against everything else, 2 qn windows):**

| qn | 840 | 842 | 844 | 848 | 856 | 860 | 862 |
|---|---|---|---|---|---|---|---|
| melody minus rest (dB) | -6.9 | +0.2 | +2.2 | +0.9 | -1.5 | +0.1 | -2.9 |

- At qn 840-841.5 the violas' div. half-note chord is at -24.6 to -26.8. The trumpets are at -33.4 / -31.1, Violins I at -28.4.
- Trumpet 1's head note sags from -32 to -36 plain after its attack, and the next (legato) note is 3.7 dB louder.
- c23 measured the same (violas -26.8 / -24.6, Trumpet 1 -33.1 / -31.9), so this is long-standing, not a c24 change.
- Cause: the hairpin gains of the crescendo in 209-210 (`hpgain` [832, 839, +3] on Violas and Violins II, +4 on Bassoon 1, +2 on Horn 3, Trombone 1 and Tuba, [832, 840, +3] on Violins I) are released only over 840-842.75. The accompaniment therefore hits its printed ff 2-4 dB over its own ff. The melody gets only Trumpet 1's role +1.
- At 856 the violas (f, -32.4) are level with the ff trumpets (-32.5 / -31.4).

**Fix:**
- (a) `tools/score_to_parts.py`, the hairpin-gain release: when a crescendo hairpin ends at a printed dynamic within 1 qn (here 839 -> ff at 840), end its gain at the printed dynamic's onset (ramp to 0 by 839.75) instead of releasing it after the downbeat. Make it generic with a default, and record the Finale rows it changes.
- (b) `build/roles.json`: Trumpet 1 [840, 866, +1] -> [840, 856, +3] and [856, 866, +2]; Trumpet 2 new [840, 866, +2]; Flute 1, Oboe 1 and Clarinet 1 [840, 862, +1.5].
- Targets: melody minus rest +2 dB or more at 840 and 856; the violas at least 3 dB under Trumpet 1 in 840-842.

## 4. The espressivo line in bars 217-218 (cor anglais f, Horns 1-2 a2) is hidden 3-9 dB under held accompaniment chords (measured)

**Where:** qn 862-872. The cor anglais (f, espress.) and Horn 1 (Horn 2's unison dropped; espress.) carry the line. Violins I and II hold div. chords, f > mf, and the violas, cellos and basses hold mp.

**Evidence (K, line sum against everything else):**

| qn | 862 | 864 | 866 | 868 | 870 |
|---|---|---|---|---|---|
| line minus rest (dB) | -13.2 | -9.1 | -7.1 | -3.1 | -2.7 |

- At 864 Violins I's held chord is -33.9, against the cor anglais at -40.2 and Horn 1 at -43.7.
- This is one of the "inner lines hidden" Dan heard: the only melodic motion in these two bars.

**Fix (`build/roles.json`, passage levels):**
- Cor anglais new [863.5, 872, +4].
- Horn 1: its 863.5-871.7 +3 dB envelope step comes from the unison hold. Add a role [863.5, 872, +2] on top.
- Violins I and Violins II new [864, 872, -3].
- Target: line minus rest 0 dB or more from 864, and the cor anglais at least 2 dB over Violins I.

## 5. The muted trumpet and cor anglais (bars 171-186) sit only 2-3 dB over their pp accompaniment (measured)

**Where:** qn 680-744. The cor anglais p dolce cantabile and Trumpet 1 con sordino play in unison over Clarinet 2 and Bass clarinet (pp, dal niente), Basses pizz. pp and Violas sul tasto pp.

**Evidence (K, per bar):**
- The cor anglais is -45.2 to -50.9. The loudest accompaniment stem is often within 2-3 dB:
  - bar 172: Basses -51.6, cor anglais -48.7;
  - bar 176: Bass clarinet -52.6, cor anglais -50.9;
  - bar 180: Basses -51.7, cor anglais -48.7.
- Over the whole passage the pair is +2.0 dB over the sum of the rest.
- At the same printed p, Trumpet 1's open solo in bars 51-66 is at -45.7 and leads its pp accompaniment by 6.8 dB. The cor anglais here is 2.3 dB softer.
- The pair is in balance with itself: the cor anglais is 2.4 dB over the muted trumpet, within the 1-3 dB the c24 target asked for.

**Fix (`build/roles.json`):**
- Cor anglais new [680, 744, +2.5]; Trumpet 1 [680, 732, +2] -> [680, 732, +4.5]. This keeps the pair 1-3 dB apart.
- Clarinet 2, Bass clarinet and Double basses new [680, 744, -2].
- Target: the cor anglais at least 5 dB over the loudest accompaniment stem in every bar, and the pair at least 4 dB over the rest.
- The mp3's ride row (+3.09 on 664-744) stays as it is.

## 6. Oboe 1 in bars 143-144 and the Trumpet 3 accents: why the c24 values missed, and the next values (measured; the cause is inferred)

**Oboe 1, qn 568-576.** It is still 1.3 dB under Clarinet 1 (K) and 4.0 dB over Flute 1. The target was 4-5 dB under the clarinet.

The range did not transfer because the response is a step, not a slope. In parts.json:
- T1 (+2 dB, CC11 74-79) read 7.8 dB under.
- The c24 render (+3.5 dB, CC11 82-88) read 1.4 under.
- c23 / CTRL (+5 dB, CC11 86-98) read 1.2 under.

So the level jumps 6.4 dB between CC11 79 and 82 and barely moves above that. That looks like a dynamic-layer crossfade near 80 in the oboe's Sus MAX row (inferred: the patch's start-mode ranges say 56-93, but the measurements say there is a step).

Fix: keep CC11 where c24 has it (82-88, the brighter layer) and set the level with a held passage level, `build/roles.json` Oboe 1 new [567.5, 576, -3.5]. It covers two tied whole notes and is not a per-note move. Target: -4 to -5 dB against the clarinet.

**Trumpet 3 accents, qn 1016-1044.**
- Accented minus plain same-pitch half note: median +1.2 dB on the first 0.3 s, and 0 dB in the body.
- The accent is only in CC11 (117 against 88; planned +2.5 dB at k 20). CC1 stays flat at 79-81 on the accented notes.
- LEARNINGS (c17) says most of a CC1-layered trumpet accent comes from CC1.

Fix: add a CC1 accent bump of +7 for 0.25 s on Trumpet 3's accented notes in 1016-1044 (the same `accents` CC1 path Trumpets 1-2 use), and keep CC11 `amt_rel` 0.33. Target: +2 to +3 dB front.

**Checked, met:**
- Horn 3 is 4.1 dB under Horn 4 in 936-948 (K).
- At the 223 arrival, the timpani, bass drum and crash do not cover. Highest 50 ms against the master's -9.1: crash -20.2, bass drum -21.8, timpani -24.7.
- In the final chord: crash -20.8, bass drum -21.5, timpani -29.6, against the master's -8.5.
- The chorale against the strings: in 224-225 the brass lead Violins I by 5-7 dB; in 226-228 the winds and violins lead the brass, as printed.
- The counterstatement theme (Violas, Celli, Basses, low winds, Horns 3-4, Tuba) leads the violins' countersubject by about 4 dB.
- The bassoon solo in 115-122 is 5-6 dB over everything else.

**Do not touch:**
- the Violins I "Sus Marc LITE" row choice, v92, the 0.085 s lead and the CC11 step rows (only the level changes in finding 1);
- the harp's velocity path (c22);
- the summit ride rows and the -14 delivery chain;
- Trumpet 1's open-solo role [200, 264, +3.2];
- the chorale's brass / string balance in 224-234;
- the timpani, bass drum and crash levels at 223, 263 and 278;
- Horn 3 CC1 +12;
- Trombone 1's tongued accents;
- the c24 unison-drop layout (Trumpet 2 silent in 255-264 by design, covered by Trumpet 1's role).
