# Critic B, cycle 5: balance and levels (render c04)

Method. All levels are K-weighted (BS.1770 filter applied in the frequency domain, LUFS-style dB). They come from the c04 stems, which are post-fader, so they include vol_db and the mix.json trims. Per-beat levels use the parts.json tempo map. Per-note levels run from the score onset (`sq`) + 80 ms to min(note end, onset + 1.5 s). "Melody margin" means the louder melody stem minus the loudest single non-melody stem in the same beat or bar. "Accompaniment sum" is the power sum of every non-melody stem. The melody tracks per passage were read from the score. Scripts are in `/private/tmp/claude-501/mockup-loop/c05-B/`:
- `prep.py`: K-weighted 10 ms frames.
- `lib.py`: tempo map and printed dynamics from mockup-events.tsv.
- `dyn.py`: per-note medians by printed dynamic.
- `mel.py` / `mel.out`: melody margin per bar.
- `beats.py <q0> <q1> <step> [tracks]`: per-beat table with CC11 and vol_db.
- `hot.py`: level against CC11 fit per track, plus hot notes.

What c04 fixed (measured):
- Climax bars 61-62: Vln I is now the loudest stem, with a margin of +3.5 and +3.2 dB.
- Horn solos: margins of +5 to +15 dB in bars 7-14 and +3 to +15 dB in bars 67-70.
- Bass clarinet solo in bars 31-33: +8.5 to +15 dB.
- Cor anglais solos in bars 41-51: +2.3 to +14 dB.
- Cello countermelody in bars 23-26: 3-7 dB under Vln I.

## 1. In the crescendo into the first climax (bars 57-60), the tune is level with the accompaniment. Single accompanying stems sit 0.5-1.5 dB under the tune or above it, and the tune group is 3-5 dB under the accompaniment sum (measured)

Where: qn 188-204. The melody is Vln I with Flute 1 and Oboe 1, and Vln II in sixths, rising mf/p to f. Under it:
- bass clarinet (p, then f)
- bassoons (mp, then f)
- Horn 1, "1." mp line
- violas: triplets at mp, then sextuplets at f
- Vc "espr." and Cb at mf

What (`mel.out`, `beats.py 184 204 1`):
- Melody margin per bar: bar 57 +1.2, bar 58 +1.3, bar 59 +0.5, bar 60 +1.5 dB. Melody group minus accompaniment sum: -4.9, -2.8, -3.2, -4.7 dB.
- Bass clarinet (printed p, hairpin to f at bar 59): -38.0, -36.2 and -34.1 at qn 193, 194 and 195, against Vln I -41.6, -38.2 and -39.0. It is 2-5 dB over the tune while still marked p, and at its own ff median (-33.5). Its CC11 reaches 78-83 by qn 194-195.
- Bassoon 1 at qn 196 (f; the unison note kept from Bn1+Bn2 gets +3, which nets the -5 note trim to -2): -32.9 against Vln I -34.4.
- Violas (sextuplets, f, accompaniment): 54 notes in qn 196-204 at -30 to -36, level with Vln I note for note (for example qn 202.67: Vla -30.0, Vln I -30.3). The viola f median (-35.3) is hotter than its ff median (-36.3).
- Also at Vln I's level: Horn 1 at -34.2 to -38.5 in qn 194-203 (Vln I -31.8 to -38.8), and Cb at -34.6 to -37.4 in qn 194-202. Vc is 0.5-1 dB over Vln I at qn 190-191 (-39.5/-38.8 against -40.3/-40.0) even with its [188, 204, -6] role.
- The timpani roll (p, cresc. to f) in qn 200-203 measures -38.6, -35.7, -33.0 and -36.3, against Vln I -33.1, -32.0, -31.8 and -29.3. It is within 1.2 dB of the tune at qn 202.
- Reference (Rimsky-Korsakov, Principles, "Comparison of resonance", rimsky-principles.txt line 1984): in forte, Violins I equals two wind instruments, so a single wind should sit about 3 dB under the Vln I section.

Fix:
- `build/roles.json`:
  - Bass clarinet: [188, 204, -5]
  - Violas: [196, 204, -4]
  - Double basses: [188, 204, -3]
  - Horn 1: [188, 204, -2]
  - Timpani: [200, 203.5, -3]
  - Violins I: [188, 204, +2] (positive values pass through the same `("span", ...)` path; note_trims Violas 220 +4 shows they work)
- `build/note_trims.json`:
  - Bassoon 1 196: -5 → -9
  - Violoncellos: add 190: -4
- Targets: Vln I at least 3 dB over every single non-melody stem in each beat of qn 188-204. Melody group (Vln I + Fl 1 + Ob 1) within 2 dB of the accompaniment sum. Bass clarinet under -40 before qn 196.

## 2. The second build-up (bars 75-81) has the same fault: an inner clarinet, single cello notes and Bassoon 1 are level with the tune or above it (measured)

Where: qn 250-271. The tune is Vln I (mp, then f, then ff) with Flute 1 (p) doubling an octave higher. Clarinet 1 "dolce" p is an inner line. Vc mp is the countermelody, and Bassoon 1 has a counterline in bars 79-81.

What (per note against Vln I over the same window):
- Clarinet 1, qn 252-256 (dolce p): -40.2, -38.9, -38.2 and -38.0, against Vln I -39.1, -40.0, -39.4 and -36.9. Bar 76 has a melody margin of -0.2 dB.
- Violoncellos:
  - qn 253: -38.3 against -40.2.
  - qn 261 (the f arrival): -31.4 against -35.1.
  - Both notes are 6-9 dB above the cello's own CC11 fit (`hot.py`: +5.8 and +8.4 before vol_db). The [250, 274, -5] role does not cover them.
- Bassoon 1:
  - qn 269: -31.7 against Vln I -38.0 and Flute 1 -39.3. This is the loudest stem in bar 81 and +10.5 dB over its own fit.
  - qn 262: -31.9 against -29.7, after the -3 trim.
- Per bar: melody group minus accompaniment sum is -3.0, -3.9, -2.1, -2.8, -4.2, -4.2 and -2.8 dB in bars 75-81.
- Melody margin in bars 77-79: +1.9, +0.6 and +0.9 dB.

Fix:
- `build/roles.json`:
  - Clarinet 1: [250, 258, -4]
  - Violins I: [244, 262, +2]
- `build/note_trims.json`:
  - Violoncellos: add 253: -5 and 261: -8
  - Bassoon 1: add 269: -7, and change 262: -3 → -5
- Targets: Clarinet 1 at least 3 dB under Vln I in qn 250-258. No cello or bassoon note louder than Vln I in qn 250-271. Melody margin at least +3 dB in bars 75-81.

## 3. At the mf peak of the first string tutti (bars 28-30) the celli and the violas cover the violin tune (measured)

Where: qn 80-90. All strings play p < mf > p, then p > pp (score p. 2). The tune is Vln I and Vln II in unison. The violas play divided dyads.

What:
- Bar 28: Vc -41.8 against Vln I -44.8 (`mel.out`), a melody margin of -3.0 dB. The single cello note at qn 81 (A♭3, 2 qn) measures -41.1 against Vln I -46.6 and -44.0 in the same beats.
- Violas, qn 81-84: -45.5, -44.8, -44.7 and -45.5 per dyad, level with Vln I. In qn 84-89 they sit over it: Vla -45.5 to -48.7 against Vln I -45.1 to -50.8 and Vln II -43.1 to -55.1.
- Bar 29 margin +0.6 dB and bar 30 margin -1.6 dB, with the violas the top stem in both.
- The violas carry only the divisi cut (-3) here, and the celli have [78, 90, -6], but the qn 81 note still swells.

Fix:
- `build/note_trims.json` Violoncellos: add 81: -6.
- `build/roles.json` Violas: add [80, 90, -3].
- Targets: Vln I at least 2 dB over Vla and Vc in every beat of qn 80-89. Bar 28 margin of +3 dB or more.

## 4. In the final chord (bars 89-92) the violas drop out: 4-10 dB under the other strings at the same printed pp/ppp (measured)

Where: qn 292-304, the closing A♭ chord. Score p. 8: all five string parts pp, then ppp under the fermata. The violas play "unis., sul C".

What (`lib.levq`, per span qn 292-298 / 298-301 / 301-304):
- Violas -56.1, -60.2 and -69.8.
- Vln II -51.6, -53.4 and -61.4.
- Double basses -52.3, -53.9 and -61.3.
- Vc -48.5, -51.1 and -60.3.
- Vln I -47.7, -49.8 and -58.9.
- Under the fermata the violas are 8-10 dB under everyone else. They are the only part that thins audibly as the chord fades.

Cause. It is not the trims: every string gets the global `soft_trim_db` ppp -4, and the violas' own override keeps pp at 0, where the others get -2. Measured: the fitted viola slope is 0.31 dB/CC against 0.25 for the violins, so the viola samples lose level faster as CC11 falls through pp toward ppp (CC 34 to 22). Inferred: the sul C register makes this worse.

Fix:
- `build/roles.json` Violas: add [292, 298, +4] and [298, 304, +7].
- Target: Violas within 3 dB of Vln II and Cb in each of the three spans.

## 5. Two soft timpani moments are the loudest stem: the pp→p roll in bar 52 over the cor anglais solo, and the end of the bar 81 roll into the p stroke in bar 82 (measured; release cause inferred)

What:
- Bar 52 (qn 168-172): the pp roll with its printed cresc. to p rises from -48.7 to -43.6 at qn 171.5-172. Over the same span the cor anglais solo (p, dying away) measures -48.6 to -44.7 and Vln II -49.7. The timpani are the loudest stem in the bar (metrics.md: bar 52 Timpani -48.1, top).
- Rule 5 of the brief: a long roll is never the loudest stem unless the timpani lead. A cresc. from pp to p allows growth, but not above a p solo.
- Bar 81-82 (qn 270-272):
  - At qn 270 the timpani measure -39.6 against Vln I -41.1. At qn 271 they measure -42.3 against Vln I -45.1 and Flute 1 -49.9 (printed p).
  - metrics.md lists the timpani as the top stem of bar 82 (-49.6).
  - The settle envelope steps from -5 dB back to 0 at exactly qn 271 (parts.json vol_db [265, -5] → [271, 0]), while the f roll that ends there is still ringing. The new p stroke (vel 64) measures -46.1 on its own.
- Timpani p median (-45.1) is 4 dB over the string p median (-49.4).

Fix:
- `build/roles.json` Timpani: add [168, 172, -4].
- `build/note_trims.json` Timpani: add 271: -4.
- In `tools/score_to_parts.py`, in the timpani roll settle that writes vol_db, hold the settle level until 0.5 qn after the roll's end before returning to 0. The restore at 271 then does not lift the f roll's ring.
- Target: timpani at least 3 dB under the loudest melodic stem in qn 168-172 and 270-274.

## 6. The muted horns at the close (bars 87-90, Horns 3-4 "con sord." pp) are the loudest stems, over the strings at the same pp (measured; mute timbre is outside this lens)

What:
- qn 286-292, per beat:
  - Horn 4: -47.3, -46.9, -46.0, -49.2, -50.2, -49.5.
  - Horn 3: -50.4 to -56.1.
  - Vln II: -50.2 to -54.4.
  - Violas: -51.8 to -59.0.
  - Vc: -54.4 to -56.9.
  - Cb: -52.4 to -56.5.
- metrics.md lists Horn 4 as the top stem of bars 87 and 88.
- The horns play open (README: no muted horn in the KS Master). The HO Brass "05 Mutes" folders contain only stopped-horn patches (`1FH Stop Sus.oib`), which are a brassy, stopped colour and not con sord. A con sord pp horn should sit under a pp string chord, not over it (inferred from orchestration practice; not checked against the books in this cycle).

Fix:
- `build/roles.json` Horn 3 and Horn 4: [286, 298, -6].
- Do not swap in the Stop patch.
- Target: Horn 3 and Horn 4 at least 3 dB under Vln II and the violas in qn 286-298.

Checked and not a finding:
- Wind against string CC11 range. The fitted level/CC slopes are 0.19-0.22 dB/CC for oboe, clarinets and contrabassoon, 0.25 for the violins, and 0.27-0.34 for the horns.
- This matches Rimsky-Korsakov's ratios: a wind equals one string department in piano, and is about 3 dB under it in forte.
- Measured at p: Vln I -42.9, Clarinet 1 -43.2, Flute 1 -44.6. Do not widen the woodwind ranges.
- Trombone 1's ff solo in bars 63-64 measures -24.4 for the master bar, 4.5 dB under the bar 61 tutti (-19.9). That is right for a solo.

Do not touch:
- The bar 61-62 climax trims (Vln I loudest, +3.2/+3.5).
- The horn solo leads in bars 7-14 and 67-70.
- Trombone 1's ff marcato lead and its decrescendo in bars 63-64.
- The f/ff timpani rolls settling to 5-7 dB under Vln I (qn 263-268).
- The Vc countermelody roles [66, 78, -1] and [238, 250, -3].
- The c04 Cb EQ and the climax ff dyn_trim values.
- The woodwind and string CC11 ranges (see above).
- The volume-envelope scheme (CC11 picks the layer, gain sits in the envelope).
