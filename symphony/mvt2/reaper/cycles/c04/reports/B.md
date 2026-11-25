# Critic B, cycle 4: balance and levels (render c03)

Method. Levels are K-weighted (BS.1770 filter, LUFS-style dB) unless marked otherwise. They come from the c03 stems, which are post-fader, so they include vol_db. Per-note levels run from the score onset (`sq`) + 80 ms to min(note end, onset + 1.5 s). Per-beat and per-bar levels use the parts.json tempo map. Group sums add the power of the stems in a group. The band analysis is a Welch PSD per stem over the whole piece. Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c04-B/`: `an.py`, `fit.py`, `kbars.py`, `top.py` (`top.out` has the loudest six stems per bar with their printed dynamics), `qlev.py` (per beat), `grp.py` (group sums), `lowsrc.py` (band energy per stem), `cbvc.py` (basses against celli per bar).

What c03 fixed (measured): the soft timpani rolls now sit under the texture. The bar 2 roll measures -52.8 settling to -56, and in bars 67-70 the roll is -53.6 to -56.8 under the horn solo at -41.5 to -48. In bars 61-62 the violas (-35.1) sit 5 dB under Vln I (-30.3). In bars 41-43 the harp (-54.1) sits well under the CA solo (-45.9). The bassoons are back with the woodwinds at ff (-34.8/-35.6 per note).

## 1. At both climaxes the melody is not the top of the balance. Single wind chord tones, celli and contrabassoon are level with or above Vln I, and the flutes doubling the tune are 6-7 dB under it (measured)

Where: bars 61-62 (qn 204-212) and 79-80 (qn 262-268). In both places the melody is Vln I ff in octaves with Flutes 1-2 ff (score p. 5 and p. 7). The other parts are wind chords (ff), horns (f), celli (ff, then f in bar 79), and a bass line doubled by Cb, Cbn, BCl and Bn2.

What, per note, against Vln I:
- Bars 61-62: Vln I measures -28.1 (qn 204), -30.9 (208) and -30.5 (210).
- Celli: -26.1 at qn 204, the loudest stem at the climax, 2 dB over the tune.
- Contrabassoon: -30.0 and -30.4 at 208 and 210, level with Vln I.
- Oboe 1 -29.8 and Oboe 2 -30.1 at 210. Clarinet 1 -29.9 at 208.
- Flute 1 -35.0 and Flute 2 -35.4 to -38.8: 7 dB under the line they double.
- Bars 79-80, per beat: Vln I -31.3 to -32.5. Oboe 2, an inner chord tone, measures -28.7 to -29.5 at qn 264-266, 5 dB over Oboe 1 (-34). Clarinet 1 measures -28.3 to -30.0 at 266-268, Bassoon 1 -29.4 at 262, Cbn and Cb -31 to -34.
- Flute 1 jumps to -26.1 on the ff note at qn 262 (B♭6, after the grace run at velocity 127). Elsewhere in the passage it is -30 to -35.
- Group sums (`grp.py`), with melody = Vln I + Fl 1 + Fl 2:
  - Bars 61-62: melody -28.7, harmony (Ob, Cl, Bn1, horns, Vln II, Vla) -23.9, bass (Cb, Cbn, BCl, Bn2, Vc, timp, low brass) -24.2. The tune is 4.5 dB under the bass group.
  - Bars 79-80: melody -27.8, harmony -23.7, bass -26.8.
- Reference: Rimsky-Korsakov (Principles, "Comparison of resonance") puts one woodwind in forte at about half a string section, about -3 dB. A single oboe, clarinet or contrabassoon should therefore sit about 3 dB under the Vln I section, not level with it or above it.

Cause (measured from mix.json and parts.json): the flutes carry `dyn_trim_db` ff -6 (set in c02 against hot single notes), while the oboes carry ff +3 and the contrabassoon ff +4. The winds play at CC11 119 at qn 204, against 113 for the strings.

Fix:
- `build/mix.json`:
  - Flute 1 and Flute 2 `dyn_trim_db` ff -6 → -3.
  - Oboe 1 and Oboe 2 ff 3 → 0.
  - Contrabassoon ff 4 → 1.
  - Clarinet 1 ff -1 → -3.
- `build/note_trims.json`: Flute 1 {262: -6} (the hot B♭6), Oboe 2 {262: -4}, Bassoon 1 {262: -3}.
- `build/roles.json`: Violoncellos add [204, 212, -3].
- Targets: Vln I is the loudest single stem in every beat of qn 204-212 and 262-268. Every single wind is at least 2 dB under Vln I. Flute 1 is within 3 dB of Vln I. The melody group is within 2 dB of the bass group.

## 2. The double basses are the loudest stem under the tune in bars 28, 30, 53 and 82, sit above the celli in 23-30 and 79-82, and alone make the 63 Hz excess (measured; EQ fix inferred)

Where: Double basses in bars 23-30 (qn 66-90), 53-56 (qn 172-188) and 79-82 (qn 262-274).

What:
- Per bar, Cb minus Vc, both printed p or mf:
  - Bars 23-30: +2.9, +6.6, +2.7, +6.7, +1.3, +2.7, +6.2, +11.5 dB.
  - Bars 79-82: +10.3, +2.6, +4.9, +10.0 dB.
  - Bar 53: +4.8.
- Against the tune, the basses are the loudest stem:
  - Bar 28: Cb -40.7, all printed mf, against Vln I -43.1 and Vln II -45.4.
  - Bar 30: Cb -48.9 at p, against Vln I -51.1.
  - Bar 53: Cb -45.1 (p) against Vln I -46.5 (p).
  - qn 82: Cb -39.8 against Vln I -41.0.
- In bars 23-30 the basses play a plain p bass line under a "unis., cantabile" cello countermelody (score p. 2). The order should be violins, then celli, then violas and basses. In the render it is violins, then basses, then celli.
- Spectrum (`lowsrc.py`): in the master's 45-90 Hz band, the Cb stem alone is -0.2 dB relative to the master band. The next contributors are BCl -15.4 and Cbn -15.8. The Cb stem's 45-90 Hz energy is 24 dB above its own 710-1420 Hz band. metrics.md gives the master's 63 Hz third-octave band at +5.4 dB relative to 1 kHz, against -6.2 in the Dvorak reference. That is the open "63 Hz high" item from c03, and it is a bass-section item.
- K-weighting barely discounts 50-60 Hz (about -1 to -2 dB), so the per-bar ranking above holds without it.

Fix:
- `build/roles.json`, Double basses: [66, 90, -4], [172, 188, -3], [262, 276, -3].
- In `tools/build_reaper.py`, add a ReaEQ (REAPER stock plugin) after Opus on the Double basses track only: low shelf at 90 Hz, -4 dB. Apply it with the mix step, so `--mix-only` re-applies it, and keep its settings in mix.json (for example `"eq": {"lowshelf_hz": 90, "db": -4}` on the track). The Opus Channel EQ insert (Opus manual, "Equalizers": 3-band with a low shelf) would do the same inside the patch, but its JSON class is unknown, so ReaEQ is the safer route. The amount is inferred, so check it by measurement.
- Targets: the master's 63 Hz band at or below +1 dB relative to 1 kHz. Cb at least 2 dB under Vc in bars 23-29. Cb never the loudest stem in a bar where the violins carry the tune.

## 3. The cello countermelodies are buried by the roles cuts: 10-15 dB under the tune and level with the pp violas and basses (measured)

Where: Violoncellos, bars 23-26 (qn 66-78, "unis., cantabile", p) and bars 71-74 (qn 238-250, "cantabile", p, under the violin melody at p). Score pp. 2 and 6.

What, per beat:
- qn 68-77: Vc -52.5 to -56.9 against Vln I -36.3 to -46.5, about 10-15 dB under. The celli sit under the basses (-45.6 to -51.0) and the violas (-49 to -52), which play a plain bass line and chords.
- qn 240-249: Vc -52.1 to -56.5 against Vln I -39.6 to -45.4, and level with the pp violas (-51 to -56) and pp basses (-51.7 to -56.5).
- Bar medians in top.out: bar 72 Vc -53.8 against Vla -53.7 (pp) and Cb -55.4 (pp). Bar 74 Vc -55.7 against Vla -53.0 and Cb -53.2.
- The printed p of the celli comes out level with the printed pp of the parts around them. A cello countermelody one level under the tune should sit about 4-6 dB under it.

Cause (measured from roles.json and note_trims.json): Violoncellos [66, 90, -5] and [238, 274, -5], plus note trim {238: -6}. These cuts were set in c02, when the celli covered the tune at the climaxes. Here they land on soft cantabile passages.

Fix in `build/roles.json`, Violoncellos:
- [66, 90, -5] → [66, 90, -1].
- [238, 274, -5] → [238, 250, -1] and [250, 274, -5]. Bars 75-78 are now 4-6 dB under the tune, which is right.
- In note_trims.json, change Violoncellos {238: -6} → {238: -10}, so that this one hot note keeps its present level.
- Keep the [188, 204, -6] cut.
- Targets: Vc 4-7 dB under Vln I at qn 68-77 and 240-249, and at least 2 dB over the Cb and the pp violas.

## 4. Two equal-dynamic string chords have one line 5-12 dB too loud: Vln II in bars 63-66, celli in bar 2 (measured)

Where and what:
- qn 212 (bar 63, sf tremolo): Vln II measures -28.0 against Vln I -33.3.
- qn 216-217 (bar 64, all p tremolo): Vln II -40.8 and -39.3, against Vla -51.1 and -49.2 and Vc -46.3 and -45.8.
- qn 220-225 (bars 65-66, Vln II, Vla, Vc and Cb all pp with a decresc., "unis."):
  - Vln II measures -49.2, -44.6, -42.7, -46.9, -49.5, -50.5.
  - Vla measures -54.5 to -63.7, Vc -53.1 to -60.0, Cb -55.7 to -59.5.
  - All four tracks have the same CC11 (parts.json), so Vln II is 8-12 dB over the others from the samples alone. It also rises 6 dB inside the printed decrescendo (qn 220 → 222).
- qn 3-6 (bar 2, all strings pp): the celli Ab2 (pitch 44, Leg BC) measures -46.2 to -46.9. Vln II, Vla and Cb measure -50.2 to -54.3. That is 5-7 dB over, at the same CC11.

Fix:
- `build/roles.json`, Violins II: add [212, 216, -4] and [216, 227, -8].
- `build/note_trims.json`, Violoncellos: add {3: -5}.
- Targets: Vln II within 2 dB of Vla and Vc in qn 216-226. Vc within 2 dB of Vln II and Vla in qn 3-8.

## 5. The accompaniment is level with the solo: violas and harp under the flute solo in bars 37-40, and the harp under the violin tune in bars 53-56 (measured)

Where and what:
- Bars 37-40 (qn 108-124): Flute 1 "1." p solo, over Vla pp triplets, Vln II pp div. sul tasto and harp p chords.
  - Flute 1 measures -46.4 to -51.6 per beat.
  - Violas measure -47.2 to -53.1. They are level with or over the flute at qn 112-113 (-51.5/-50.8 against -48.8/-51.6) and at 120-121 (-48.6/-47.2 against -48.9/-46.4).
  - The harp chord beats measure -47.0 to -50.8, level with the flute at qn 108, 116 and 120.
  - Bar medians: flute -48.5, Vla -49.9 in bar 40.
- Bars 53-56 (qn 172-188): Vln I and II p → mp → mf in unison, over the harp's p → mp triplets.
  - Harp measures -42.4 to -45.2 at qn 172-175, over Vln I (-44.3 to -49.7) and level with Vln II.
  - At qn 180-187: harp -39.5 to -43.1 against Vln I -34.1 to -44.3.
  - The harp is the loudest stem in bar 53 (-43.9) and is level with Vln I in bar 55 (-41.4 against -40.0).
  - Its per-note median at mp, -42.5, is the hottest mp on the chart.
- c03 targeted the Vln II level (5 dB under the flute, achieved) but not the violas or the harp.

Fix in `build/roles.json`:
- Violas: [108, 124, -4].
- Harp: add [108, 124, -4] and [172, 188, -4], keeping [124, 140, -7].
- Targets: in qn 108-124, the violas and the harp chord beats at least 3 dB under Flute 1. In qn 172-188, the harp at least 3 dB under the louder violin section.

Do not touch: the horn solo leads in bars 7-14 and 67-70. Trombone 1's ff marcato lead in bars 63-64 and its decrescendo at qn 218-219. The c03 timpani soft-roll -6 dB and settle. The f/ff timpani rolls 2-5 dB under Vln I (qn 200-212, 262-270). The brass at f/mf under the strings in bars 61-62 (horns -34.6 each, Tbn2 -35.7, tuba -38.3, B.tbn -40.4). The divisi/double-stop cut. Harp roles [124, 140, -7] under the CA. The Violas f/ff trims. The bass clarinet solo leading the CA in bars 31-34. The volume-envelope scheme, with CC11 choosing the layer and gain in the envelope.
