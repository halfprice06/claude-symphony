# Cycle 9, critic C: blend and space (review of the c08 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets (trumpets and cymbals are new here), and low-end build-up against several references. I measured the stem-fixed c08 render (`cycles/c08/render/`; score qn to file time through the `build/parts.json` tempo map). I also read the Opus states in `jobs/*.b64` and the layer tables in the KS Master `.oib` files.

References:
- the third-octave, stereo, brightness and tail metrics stored for five recordings: Brahms 1/i, 4/i, 1/ii, 4/ii (Musopen) and Dvořák 9/i (`symphony/render/critics/c00|c04/ref_*/metrics.json`);
- the movement II c26 master (same library and hall).

Scripts and output are in `/private/tmp/claude-501/mockup-loop/mvt1-c09-C/`: `rowcc.py`, `rowtab.py`, `tptlayer.py`, `brasstone.py`, `depth2.py`, `stereo.py`, `tails.py`, `bright.py`, `stemspec.py`, `stemshare.py`, `simeq.py`, `stemthird.py`, `perc2.py`, `longloop.py`, `fold.py`, `mloop.py`, `acc.py`.

## Checked and fine (measured)

- **Room.** All 32 Opus states use one hall: `S. Cal Hall Perc TS FR 3.3s`, true stereo, fx 0.19, wet 2.0, pre-fader sends.
  - Master release drop at bar 170 is 15.0 / 21.5 / 32.6 dB at 0.3 / 0.6 / 1.0 s, so it reaches -20 dB at about 0.55 s.
  - The references reach -20 dB at 0.46-0.79 s (cut-off medians 0.485 and 0.49 s).
- **Image.** Correlation 0.536, side/mid -5.2 dB, R-L +0.06 dB. Below 250 Hz 0.544, 250 Hz-4 kHz 0.545, above 4 kHz 0.509.
  - The references measure 0.49-0.55, -4.7..-5.4 dB, 0.54-0.62, 0.47-0.56 and 0.38-0.53.
  - Seats hold: Vln I sustain -7.6 dB R-L, horns -5.5..-1.8, trombones +4.6..+6.1, Vc +5.2, Cb +5.1.
- **Item 7 on the master.** 100-300 Hz / centroid autocorrelation at 3.95 s:

  | passage | 100-300 Hz | centroid |
  |---|---|---|
  | opening roll | +0.07 | +0.02 |
  | bars 117-121 | +0.11 | +0.06 |
  | bars 122-126 | -0.47 | -0.11 |
  | coda 175-180 | -0.08 | +0.01 |
  | final chord | +0.03 | -0.01 |
  | control | +0.35 | +0.07 |

- **Item 8.** 2-5 kHz over the first 80 ms minus the body, median per track: trumpets -4.8 / -14.0 / -12.8, trombones -7.7 / -13.1 / -10.5, Vln I -6.8, Ob1 -6.6, Cl1 -5.9 dB.
  - The positive maxima (Hn1 +11.6, Vla +18.7, Ob1 +8.0) are on stems that sit 12-31 dB under the master's 2-5 kHz at those moments.

## 1. Brass and clarinets: the dynamic layers are crossfaded by CC1, which the pipeline keeps at 57-87, so every printed dynamic from pp to fff plays the mp-f samples (all horns, trumpets, trombones, tuba, Clarinets 1-2)

**What is wrong.** In the Hollywood Brass KS Masters and the Clarinet KS Master, the controller that crossfades the dynamic layers is CC1 (mod wheel). CC11 is only the volume, in the Global Group. Our brass therefore does not change tone colour with the printed dynamic:
- A pp horn chord is an mf horn turned down.
- A fff trumpet is an f trumpet turned up.

This is why the trumpets needed +7/+8 dB `dyn_trim_db` at f/ff in c01. It is also why c05 found the loud tutti 2-4 kHz carried by Violins I (56%) rather than the brass (trumpets 3.5%). Next to strings, oboes and flutes, whose layers follow CC11, the brass reads as a different sample set.

**Evidence, from the patch files (measured by reading `.oib` data, `rowcc.py` / `rowtab.py`).** In each layer group, the Source-volume rescaler is driven by a MidiController with `cc: 1`.

Rows we use:
- `1TP KS Master` Sus Non Vib MAX and Leg Slur MAX;
- `1TB`, `1FH`, `1TU` Sus MAX and Leg Slur MAX;
- `CL KS Master` Sus Non Vib and Leg Slur.

For comparison:
- The string KS Masters, the FL/OB/BS/CB KS Masters and the BC KS Master drive the layers with `cc: 11`. FL/OB/BS/CB use `cc: 1` only for the Non Vib/Vib crossfade, as LEARNINGS section 3 describes.
- The controllerMap maps ID 1 to CC1.

Layer weights at CC1 20 / 34 / 46 / 58 / 64 / 72 / 80 / 88 / 96 / 104 / 114 / 124:
- **1TB Sus MAX:**
  - p: 0.88 / 0.47 / 0.12 / 0 / ...
  - mp: 0.18 / 0.56 / 0.90 / 0.95 / 0.78 / 0.56 / 0.34 / 0.11 / 0 / ...
  - f: from 0.20 at 58, 0.91-0.97 at 80-88, 0.16 at 114
  - ff: 0.11 at 80, 0.30 at 88, 0.49 at 96, 0.68 at 104, 0.92 at 114, 1.00 at 124
- **1FH / 1TU:** the same shape.
- **1TP Sus Non Vib MAX:** five layers, pp to ff. The ff layer reaches 0.89 only at CC1 114. Its ff group also has a CC1-driven Butterworth filter that opens with CC1, so brightness is also on CC1.
- **CL Sus Non Vib:** p layer up to about CC1 46, mp 46-88, f from 80.

**Evidence, what we send (measured, parts.json).** `score_to_parts.cc1_fn0` gives non-vibrato families `max(40, min(100, 64 + (v11-46)*0.3))`. On the notes, CC1 against CC11:

| track | CC1 | CC11 |
|---|---|---|
| Horns 1-4 | 57-87 | 22-124 |
| Trumpets | 60-87 (p10 77) | 34-124 |
| Trombones / bass trombone / tuba | 60-87 | 32-124 |
| Clarinets 1-2 | 60-87 | 34-124 |

So the layer mix at pp is about 0.9 mp + 0.3 f, and at fff about 1.0 f + 0.3 ff.

**Evidence, the render (measured, `tptlayer.py`: note bodies +0.15..+1.15 s, band level re 0.5-1 kHz, by CC11 bin).** The brass hardly brightens with dynamic. The patches whose layers follow CC11 brighten 7-8 dB.

| track | 2-4 kHz across bins | 4-8 kHz across bins | note |
|---|---|---|---|
| Trumpet 1, CC11 85-105 vs 105-128 | -7.1 -> -7.9 | -26.3 -> -26.7 | level +8 dB, mostly the trims |
| Horn 1, CC11 0-60 / 60-85 / 85-105 | -24.6 / -26.4 / -23.5 | | flat from pp to f |
| Violins I | | +13.5 | CC11 layers |
| Oboe 1 | | +8.6 | CC11 layers |
| Bass clarinet | | +7.5 | CC11 layers |

In the loud spans the trumpets' 4-8 kHz sits 26.5-30.3 dB under their 0.5-1 kHz (`brasstone.py`). Their centroid is 1.13-1.16 kHz, against 2.18 kHz for Violins I.

**As heard (inferred).** Soft brass chords (Lento, the coda, the final chord) sound thick and close for their level, and the ff/fff brass sounds big but not brassy. The tutti's top comes from the violins, and the brass does not blend into the same crescendo colour as the strings.

**Fix** (`tools/score_to_parts.py`, `cc1_fn0`; values in `build/score_config.py`).
- Add `CC1_DYN_TRACKS = ("Horn", "Trumpet", "Trombone", "Bass trombone", "Tuba", "Clarinet ")`, prefix match; the trailing space keeps the bass clarinet out, because its BC KS Master uses CC11.
- For those tracks, return `value_at(CC1_DYN_MAP, base(q))`, where `base(q)` is the printed dynamic curve with hairpins but without accent or fit shapes, so the gentle accents stay off the top layer:

  ```
  CC1_DYN_MAP = [(22, 18), (34, 28), (46, 42), (58, 54), (72, 68), (88, 86), (114, 108), (124, 120)]
  ```

  On the tables this puts each dynamic on its layer:
  - pp: p/pp layer;
  - mf: mp + f;
  - f: f;
  - ff: ff 0.75 + f 0.4;
  - fff: ff 1.0.
- Contrabassoon: its CC1 (57-87 now) sits inside the CB KS Master's Non Vib/Vib overlap. Both layers are full over CC1 64-72, and LEARNINGS section 3 measured beating in this overlap on the flute. Hold it at a constant 40 (Non Vib only).

This is MIDI data only (`--midi-only` on 12 brass, 2 clarinet and the contrabassoon tracks; no Opus state change). Levels will move, because the layers carry their own loudness. After the render:
- re-derive the brass and clarinet `dyn_trim_db` and `soft_trim_db` from the stems (start the trumpets' f/ff at +3.5/+4 instead of +7/+8, inferred);
- refit `accent_fits.json` for brass with `fit_accents.py` (refit rule);
- check the climax order and the limiter (the master's second and third peaks, qn 640.6 and 642.2, are trombones and tuba).

**Targets (measured on the next render):**
- trumpet and trombone 4-8 kHz re 0.5-1 kHz rising at least 5 dB from the mf to the ff bins, and the horns' 2-4 kHz at least 5 dB from the p to the f bins;
- accent 2-5 kHz first 80 ms minus the body still at most +3 dB on every brass accent heard over the texture (Dan's item 8);
- the Violins I loud 3 kHz bell (c05 C #5) re-checked. The master loud-minus-soft shape at 5 kHz is already +9.8 dB against the references' +5.3..+10.3, so if the brass brightens that bell may have to come out.

## 2. The trumpets sound nearer than the trombones and horns beside them; the flutes and oboes nearer than the clarinets and bassoons (depth, all bars)

**Evidence (measured, `depth2.py`).** Release drop after every isolated note end (note at least 0.6 s, at least 1 s of rest after it), median [IQR]:

| track | n | sustain minus +0.15..0.25 s | sustain minus +0.3..0.5 s |
|---|---|---|---|
| Trumpets 1/2/3 | 5/4/6 | 13.1 / 12.0 / 12.3 | 17.8 / 16.3 / 16.5 |
| Trombones 1/2, bass trombone | 7/7/8 | 9.1 / 9.0 / 9.7 | 14.5 / 14.5 / 16.1 |
| Horns 1-4 | 11-14 | 6.8-9.3 | 12.4-17.5 |
| Tuba | 5 | 8.7 | 14.8 |
| Flutes, oboes | 4-7 | 12.1-14.5 | 17.3-20.6 |
| Clarinets, bassoons, cor anglais | 6-12 | 8.8-12.4 | 15.5-18.7 |
| Violins I / II / violas | 5-9 | 9.7 / 5.6 / 8.5 | 18.0 / 16.5 / 16.0 |

- The trumpets have the same send as the trombones (0.45, read from the states), yet they are 3 dB drier in the early tail. The 1TP samples carry more direct sound at the same mic settings. Players at the back of the stage should have the most room in their sound, and the trumpets now have less than the oboes.
- Within the woodwinds at one send (0.35), flutes and oboes are 2-3 dB drier than the clarinets and bassoons. These are the patches whose factory Main mic is 11-40 dB under Close (LEARNINGS section 12).
- Finding 1 will make the trumpets brighter, which brings them forward again (inferred).

**Fix** (`build/mix.json`): an Opus state change, so a full rebuild of these tracks.
- Trumpet group `send` 0.45 -> 0.65 (+3.2 dB wet). Leave the Close 0.5 / Main 1.0 mics, so the direct tone does not change.
- Flute 1/2 and Oboe 1/2: a per-track `send` of 0.5 instead of the group's 0.35 (+3.1 dB), if `build_reaper.py` takes a per-track send. Otherwise add that key; the group stays 0.35 for clarinets, bassoons and the cor anglais.

**Targets:** trumpet early drop (+0.15..0.25 s) within 1 dB of the trombones' (9-10 dB); flutes and oboes within 1 dB of the clarinets and bassoons (10-12 dB). The reverb adds about 0.5-1 dB to the sustained level, so re-check the trumpet/trombone balance at bars 158-161 (c05: level within 0.4 dB).

## 3. Low end: below 125 Hz the mix sits 4-9 dB under four of the five references, and the static basses cut at 100 Hz is part of it (Double basses; all loud tutti)

**Evidence (measured, `bright.py`, `simeq.py`).** Third-octave levels re the 400-1600 Hz sum: c08 (all frames; loud 10%), mvt II c26, the four Musopen recordings, and Dvořák (lossy MP3):

| Hz | c08 | c08 loud | mvt II | Musopen B1i / B4i / B1ii / B4ii | Dvořák | c08 minus median of 5 |
|---|---|---|---|---|---|---|
| 62 | -25.8 | -28.6 | -25.5 | -9.6 / -10.0 / -9.2 / -8.4 | -31.7 | -16.2 |
| 79 | -20.1 | -22.0 | -19.6 | -14.1 / -10.5 / -11.1 / -9.3 | -22.9 | -9.0 |
| 99 | -14.8 | -15.3 | -15.4 | -8.0 / -10.8 / -10.9 / -10.0 | -19.2 | -4.0 |
| 125 | -16.9 | -18.5 | -16.0 | -9.1 / -8.5 / -12.1 / -8.9 | -10.9 | -7.8 |
| 158 | -13.1 | -14.1 | -11.6 | -11.8 / -10.2 / -13.2 / -11.3 | -8.6 | -1.8 |
| 198-250 | -11.4, -13.5 | | | -11.7..-14.4 | -9.7, -11.5 | within ±1.3 |

- The Dvořák MP3 is the only reference under us at 62-99 Hz. It is the reference that the c01 and c05 bass cuts were tuned to, together with mvt II (c05 report C #3).
- 125 Hz is under all five references by 4-8 dB, Dvořák included.
- Brahms 1/i is in the same key and has the same kind of bass and timpani writing, and it is 7.8 dB over us at 125 Hz and 6.8 dB at 99 Hz.

Where it comes from (measured, `stemshare.py`, `stemthird.py`):
- The basses supply 89% of 56-70 Hz and 38% of 89-112 Hz, but only 10% of 112-141 Hz. In the loud frames their stem has a hole at 125 Hz (99 Hz -19.1, 125 Hz -32.2, 158 Hz -25.7 re the master's 400-1600).
- Part of that hole is voicing: the G1/A♭1 pedals put harmonics at 98/147 and 104/156 Hz (inferred).
- The rest is the static `bell2` 100 Hz -5 dB (0.8 oct) plus the loud `bell2` 98 Hz -4 dB (0.5 oct), which reach into 112-141 Hz.

Simulated on the stems (zero-phase EQ on the per-stem spectra, all frames):
- Removing the static bell2: 99 Hz -14.9 -> -12.2, 79 Hz -19.9 -> -18.2, 125 Hz -17.0 -> -16.6.
- Adding Violoncellos +4 dB at 125 Hz (1 oct) as well: 125 Hz -15.0, 158 Hz -13.9 -> -12.8, 198 Hz -11.2 -> -10.3.

**Fix** (`build/mix.json`, Double basses and Violoncellos): a half step back toward the lossless references, not all the way.
- Double basses `eq` bell2 100 Hz -5 -> -2 dB (bw 0.8).
- Double basses `loud_eq` bell2 98 Hz -4 -> -2 dB.
- Violoncellos `eq`: add `{"band": "bell2", "hz": 125, "db": 3, "bw_oct": 1.0}`.

Do not chase the 62 Hz gap with EQ. Sixteen dB is beyond what the Basses KS Master's fundamentals can give (LEARNINGS section 14), and all four Musopen files share that one band at -8..-10, in four different keys (inferred: possibly room or recording-chain content).

**Targets** (loud 10%, re 400-1600 Hz): 99 Hz -12..-13 and 125 Hz -15 or higher, with 158-250 Hz unchanged within 1 dB. Check that the bass notes the c25 bell was set against (D♭2/E♭2/F2) do not rise more than 2 dB over their neighbours. Check the limiter, which was at 1.2 dB in c08.

## 4. The fff crash at the main climax rings for about one second, not through the largamente bar (Crash cymbals, qn 636, bar 160, "l.v.")

**Evidence (measured, `perc2.py`; crash stem minus master, 0.2 s windows).**

| after the hit | 4-12 kHz | broadband |
|---|---|---|
| +0.1 s | -3.3 | -12.5 |
| +0.5 s | -1.4 | -12.4 |
| +1.0 s | -6.1 | -20.5 |
| +1.5 s | -11.9 | -22.1 |
| +2.5 s | -23.5 | -30.6 |
| +4.0 s | -29.2 | -39.9 |

- The c05 target (4-12 kHz within 6 dB of the master at +1.5 s) is missed by 6 dB.
- The c07 attack shape `LEVEL_SHAPES["Crash cymbals"]` (-4 dB from 636.02 to 636.6, back to 0 at 637.2) is right for the hit and leaves the ring unsupported.
- The tam-tam at 484 holds 4-12 kHz within 3-4 dB of the master to +1.5 s, so the two big percussion strokes are now unequal.

**Fix** (`build/score_config.py`): extend the crash shape (bar 160: qn 637.2 = +0.72 s, 638.5 = +1.5 s, 644 = +4.8 s):
```
LEVEL_SHAPES["Crash cymbals"] = [[(636.0, 0.0), (636.02, -4.0), (636.6, -4.0), (637.2, 0.0), (638.5, 5.0), (644.0, 6.0)]]
```

This is level only, so it can be done with the stem fix. The crash tail is 20-30 dB under the master broadband, so +5-6 dB adds under 0.1 dB to the bar-160 loudness (inferred from the levels above). It does not touch the master peak at 636.42, which comes from the strings and horns.

**Target:** 4-12 kHz within 6 dB of the master at +1.5 s and within 12 dB at +2.5 s.

## 5. Two remaining loop pulses on held winds (Bass clarinet qn 492, bar 124; Bassoon 2 qn 48, bar 13)

**Evidence (measured, `longloop.py`, `fold.py`).**

| note | autocorrelation at 3.95 s (100-300 Hz / centroid) | folded swing | stem minus master |
|---|---|---|---|
| Bass clarinet G2, qn 492, 7.2 s, fff sostenuto | 0.78 / 0.69 | 6.9 dB level, 8.8 dB at 100-300 Hz | -13.3 dB |
| Bassoon 2 G2, qn 48, 8.4 s, Lento | 0.60 / 0.26 | 3.9 dB level | -9.3 dB |

- At qn 492 the master shows nothing: bars 122-126 read -0.47 / -0.11.
- Bassoon 2 at qn 48 is more exposed: bar 13 is a soft bar.
- Every other wind, brass and timpani note over 6 s is under 0.5 in both measures.

**Fix** (`build/score_config.py`, merging into the existing `BREATH_SPLIT_AT` dict):
```
BREATH_SPLIT_AT["Bassoon 2"] = {48.0: [51.4]}
BREATH_SPLIT_AT["Bass clarinet"] = {492.0: [496.8, 500.9]}
```
- Bassoon 2: pieces of 4.1 and 4.3 s.
- Bass clarinet: pieces of 2.9, 2.5 and 1.8 s, irregular, as c06 needed for the horns.

Keep the c08 breath dip shape.

**Target:** autocorrelation at 3.95 s under 0.4 on both stems, and no master step over 1 dB at the splits.

## 6. Tam-tam and crash, played by one player, sit at different seats, with the suspended cymbal in a third (inferred, low priority)

**Evidence (measured, `depth2.py` and the states).**
- Seats: tam-tam -0.15, crash +0.10, suspended cymbal +0.25.
- Sustain R-L: tam-tam -1.9 dB, crash +0.9, suspended cymbal +1.7.
- The score gives tam-tam and crash to player 1 ("1: Crash cym. l.v.") and the suspended cymbal to player 2. The roll at 632-636 hands over to the crash between two positions.

This was c05 C #6, deferred.

**Fix** (`build/mix.json`): Tam-tam and Crash cymbals seat +0.20; Suspended cymbal +0.30; width 0.4 for all three. Do it only when these tracks are rebuilt anyway (an Opus pan change).

## Do not touch

- The shared true-stereo hall and its settings (one IR, fx 0.19, wet 2.0, 5.5 kHz high cut, pre-fader sends).
- All seats and widths except the percussion, the side-only shelves, and the Vc/Cb widths 0.28. The image matches the references in every band.
- The string, horn, trombone and woodwind mic levels.
- The tam-tam roles and damp (4-12 kHz within 4 dB of the master to +1.5 s).
- The suspended-cymbal key 64 and lead.
- The bass-octave 140 Hz loud EQs of c08.
- GENTLE_ACCENT and `accent_fits.json` (refit, do not hand-edit, after finding 1).
- AUTO_REBOW rows and shapes, the re-strike plans and the horn breath splits at 720 (master loop autocorrelation 0.03 / -0.01 on the final chord).
- The climax order 160 > 122 > 169.
